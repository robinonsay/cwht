#!/usr/bin/env python3
"""TS-012 harmonic low-pass filter analysis (WP-PDR-21): deck writer, LTspice runner, checker, plots.

Revision 2 (review of revision 1, findings 1 to 5): the worst case is now the worst instance of a corner
search over the whole parameter box (worst_case.py), run in LTspice beside a Monte Carlo with signed coil
coupling; the harmonic budget takes the harmonic relative to the carrier that reaches the antenna (the
passband loss of the same instance is included), covers the 6.4, 7.2 and 8.4 V pack cases, and the script
exits non-zero when a criterion fails.

Usage (from any directory, with the repo venv):
    .venv/bin/python hardware/sim/tx-lpf/run_lpf.py r1     # nominal: ideal, ideal-BOM, 1812SMS, air coil
    .venv/bin/python hardware/sim/tx-lpf/run_lpf.py r8     # worst case + MC, 1812SMS, BOM values
    .venv/bin/python hardware/sim/tx-lpf/run_lpf.py r9     # worst case + MC, air coils as wound, BOM values
    .venv/bin/python hardware/sim/tx-lpf/run_lpf.py r10    # worst case + MC, air coils aligned, BOM values
    .venv/bin/python hardware/sim/tx-lpf/run_lpf.py r11    # worst case + MC, 1812SMS, retuned 18/33 pF
    .venv/bin/python hardware/sim/tx-lpf/run_lpf.py r12    # worst case + MC, air coils aligned, retuned
    .venv/bin/python hardware/sim/tx-lpf/run_lpf.py r13    # worst case + MC, 1812SMS and C0G at 2 %, BOM values
    .venv/bin/python hardware/sim/tx-lpf/run_lpf.py r14    # worst case + MC, 1812SMS and C0G at 2 %, 22/68/36/82
    .venv/bin/python hardware/sim/tx-lpf/run_lpf.py r15    # harmonic budget per finalist (reads r8 to r14)
    .venv/bin/python hardware/sim/tx-lpf/run_lpf.py r16    # worst case + MC of the screened trap variant (rejected)
    .venv/bin/python hardware/sim/tx-lpf/run_lpf.py all

Revision 1 runs r2 to r7 (Monte Carlo) and r5 (budget) are kept as the record of revision 1 and are
superseded; each is reproduced by the copy of the scripts in its own results folder.

Each run writes hardware/sim/tx-lpf/results/<run-id>/: the deck, the LTspice .log and .raw, result.json and
result.md (numbers and pass/fail), PNG plots with the limits overlaid, and a copy of the scripts that
produced them. LTspice runs only through tools/ltspice-batch.sh (ACC-LTSPICE-001).

Exit status: 0 every criterion met and every check passed; 1 every check passed and at least one criterion
failed (the results are valid and report the failure); 2 a check failed (known answer or cross-check: the
results must not be used).
"""
from __future__ import annotations

import csv
import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from spicelib import RawRead  # noqa: E402

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import lpf_model as M  # noqa: E402
import lpf_nodal as N  # noqa: E402
import worst_case as W  # noqa: E402

REPO = HERE.parents[2]
BATCH = REPO / "tools" / "ltspice-batch.sh"
DATE = "2026-09-28"
RUNS = {
    "r1": f"{DATE}-r1-nominal",
    "r2": f"{DATE}-r2-mc-1812sms",
    "r3": f"{DATE}-r3-mc-air-aswound",
    "r4": f"{DATE}-r4-mc-air-aligned",
    "r5": f"{DATE}-r5-harmonic-budget",
    "r6": f"{DATE}-r6-mc-1812sms-retuned",
    "r7": f"{DATE}-r7-mc-air-aligned-retuned",
    "r8": f"{DATE}-r8-wc-1812sms-bom",
    "r9": f"{DATE}-r9-wc-air-aswound-bom",
    "r10": f"{DATE}-r10-wc-air-aligned-bom",
    "r11": f"{DATE}-r11-wc-1812sms-retuned",
    "r12": f"{DATE}-r12-wc-air-aligned-retuned",
    "r13": f"{DATE}-r13-wc-1812sms-bom-2pct",
    "r14": f"{DATE}-r14-wc-1812sms-22-36-2pct",
    "r15": f"{DATE}-r15-harmonic-budget-rev2",
    "r16": f"{DATE}-r16-wc-1812sms-trap-screen",
}
LEGACY = ("r2", "r3", "r4", "r5", "r6", "r7")
STATUS = {"checks_failed": [], "criteria_failed": []}
N_MC = 250
SEEDS = {"r2": 21001, "r3": 21002, "r4": 21003, "r6": 21006, "r7": 21007}
MC_KIND = {"r2": ("1812", None, "Coilcraft 1812SMS (J, 5 %), BOM values"),
           "r3": ("air", 0.10, "24 AWG air coils as wound (+/-10 %), BOM values"),
           "r4": ("air", 0.03, "24 AWG air coils aligned (+/-3 %), BOM values"),
           "r6": ("1812", None, "Coilcraft 1812SMS (J, 5 %), retuned 18/33 pF"),
           "r7": ("air", 0.03, "24 AWG air coils aligned (+/-3 %), retuned 18/33 pF")}
MC_VALUES = {"r2": M.BOM, "r3": M.BOM, "r4": M.BOM, "r6": M.RETUNE, "r7": M.RETUNE}

# Palette (dataviz reference instance, light mode); limits and requirements in text ink
INK, INK2, GRID = "#0b0b0b", "#52514e", "#e4e3df"
COL = {"ideal": "#8a8984", "idealbom": "#4a3aa7", "1812": "#2a78d6", "air": "#eb6834", "air_al": "#1baf7a"}
plt.rcParams.update({"font.size": 9, "axes.edgecolor": INK2, "axes.labelcolor": INK, "xtick.color": INK2,
                     "ytick.color": INK2, "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.6,
                     "figure.facecolor": "#fcfcfb", "axes.facecolor": "#fcfcfb", "legend.frameon": False})


# ---------------------------------------------------------------------------------------------
# Deck writing
# ---------------------------------------------------------------------------------------------

def fmt(x: float) -> str:
    return f"{x:.6e}"


def filter_ideal(s: str, vals: list[float]) -> list[str]:
    """Lossless ladder C1 L2 C3 L4 C5 L6 C7 between in{s} and out{s}."""
    nodes = [f"in{s}", f"a1{s}", f"a2{s}", f"out{s}"]
    out = [f"V{s} src{s} 0 AC 2", f"RS{s} src{s} in{s} 50", f"RL{s} out{s} 0 50"]
    for j, i in enumerate(M.CAP_POS):
        out.append(f"C{i + 1}{s} {nodes[j]} 0 {fmt(vals[i])}")
    for j, i in enumerate(M.COIL_POS):
        out.append(f"L{i + 1}{s} {nodes[j]} {nodes[j + 1]} {fmt(vals[i])} Rser=0")
    return out


def filter_real(s: str, p: dict, param: bool = False, traps=()) -> list[str]:
    """Filter with parasitics. With param=True the values are {names} bound by .param lines. traps: the
    coil numbers (2, 4, 6) that carry a trap capacitor (C + ESR + ESL) across the coil body."""
    v = (lambda k: "{" + k + "}") if param else (lambda k: fmt(p[k]))
    nodes = [f"in{s}", f"a1{s}", f"a2{s}", f"out{s}"]
    out = [f"V{s} src{s} 0 AC 2", f"RS{s} src{s} in{s} 50", f"RL{s} out{s} 0 50"]
    for j, i in enumerate(M.CAP_POS):
        n, c = nodes[j], f"C{i + 1}"
        out += [f"CP{c}{s} {n} 0 {v(c + 'Cpad')}",
                f"{c}{s} {n} {c}x1{s} {v(c + 'C')}",
                f"R{c}{s} {c}x1{s} {c}x2{s} {v(c + 'ESR')}",
                f"LE{c}{s} {c}x2{s} {c}x3{s} {v(c + 'ESL')} Rser=0",
                f"LV{c}{s} {c}x3{s} 0 {v(c + 'Lvia')} Rser=0"]
    for j, i in enumerate(M.COIL_POS):
        a, b, lname = nodes[j], nodes[j + 1], f"L{i + 1}"
        half = ("{" + lname + "Ltr/2}") if param else fmt(p[lname + "Ltr"] / 2)
        out += [f"LTa{lname}{s} {a} {lname}y1{s} {half} Rser=0",
                f"{lname}{s} {lname}y1{s} {lname}y2{s} {v(lname + 'L')} Rser=0",
                f"R{lname}{s} {lname}y2{s} {lname}y3{s} {v(lname + 'R')}",
                f"CS{lname}{s} {lname}y1{s} {lname}y3{s} {v(lname + 'C')}",
                f"LTb{lname}{s} {lname}y3{s} {b} {half} Rser=0"]
    for n in traps:
        ln = f"L{n}"
        out.append(f"CT{ln}{s} {ln}y1{s} {ln}y3{s} {v(ln + 'Ct')} Rser={v(ln + 'CtESR')} Lser={v(ln + 'CtESL')}")
    out += [f"K24{s} L2{s} L4{s} {v('K24')}", f"K46{s} L4{s} L6{s} {v('K46')}",
            f"K26{s} L2{s} L6{s} {v('K26')}", f"CIO{s} in{s} out{s} {v('Cio')}"]
    return out


def write_nominal_deck(path: Path) -> dict:
    ideal = M.design_values()
    p1812 = M.sample_filter("1812")
    pair = M.sample_filter("air")
    lines = [f"* cwht TS-012 harmonic LPF, run r1 nominal ({DATE}); generated by run_lpf.py, do not edit",
             "* _i ideal exact Chebyshev 0.1 dB fc 165 MHz; _b ideal with BOM values;",
             "* _c Coilcraft 1812SMS with parasitics; _w 24 AWG air coils with parasitics. S21 = V(out)."]
    lines += filter_ideal("_i", ideal) + filter_ideal("_b", M.BOM)
    lines += filter_real("_c", p1812) + filter_real("_w", pair)
    # loss decomposition of the 1812SMS build: _q coil loss only (cap ESR 0), _e cap ESR only (coil R 0)
    pq = dict(p1812, **{f"C{i + 1}ESR": 1e-6 for i in M.CAP_POS})
    pe = dict(p1812, **{f"L{i + 1}R": 1e-6 for i in M.COIL_POS})
    lines += filter_real("_q", pq) + filter_real("_e", pe)
    lines += [".ac lin 3200 0.5e6 1600e6",
              ".save V(in_i) V(out_i) V(in_b) V(out_b) V(in_c) V(out_c) V(in_w) V(out_w) V(out_q) V(out_e)"]
    for s in ("_i", "_b", "_c", "_w"):
        for f in (146e6, 148e6, 288e6, 432e6):
            lines.append(f".meas AC s21{s}_{int(f / 1e6)} FIND V(out{s}) AT {f:.0f}")
    lines += [".end", ""]
    path.write_text("\n".join(lines))
    return {"ideal": ideal, "1812": p1812, "air": pair}


def write_mc_deck(path: Path, run: str) -> list[dict]:
    kind, tol, label = MC_KIND[run]
    rng = np.random.default_rng(SEEDS[run])
    vals = MC_VALUES[run]
    insts = [M.sample_filter(kind, None, tol, corner=-1, vals=vals), M.sample_filter(kind, None, tol, corner=+1, vals=vals)]
    insts += [M.sample_filter(kind, rng, tol, vals=vals) for _ in range(N_MC)]
    n = len(insts)
    lines = [f"* cwht TS-012 harmonic LPF, run {run} Monte Carlo: {label} ({DATE}); generated by run_lpf.py",
             f"* run 1 = all L and C at -tol, run 2 = all at +tol (nominal parasitics), runs 3..{n} uniform random,",
             f"* numpy default_rng seed {SEEDS[run]}; values also in mc_values.csv. S21 = V(out_m)."]
    lines.append(f".step param run 1 {n} 1")
    for name in M.PARAM_ORDER:
        if name.endswith("Q") or name.endswith("SRF"):
            continue
        pairs = [f"{k + 1},{fmt(inst[name])}" for k, inst in enumerate(insts)]
        chunk = [", ".join(pairs[i:i + 8]) for i in range(0, len(pairs), 8)]
        lines.append(f".param {name}=table(run, " + chunk[0] + ("," if len(chunk) > 1 else ")"))
        for ci, c in enumerate(chunk[1:], start=1):
            lines.append("+ " + c + ("," if ci < len(chunk) - 1 else ")"))
    lines += filter_real("_m", {}, param=True)
    lines += [".ac lin 800 2e6 1600e6", ".save V(out_m) V(in_m)"]
    for f in (146e6, 148e6, 288e6, 432e6):
        lines.append(f".meas AC s21_{int(f / 1e6)} FIND V(out_m) AT {f:.0f}")
    lines.append(".meas AC rl_146 FIND V(in_m)-1 AT 146e6")
    lines.append(".meas AC rl_148 FIND V(in_m)-1 AT 148e6")
    lines.append(".meas AC echo_L4 PARAM L4L")
    lines += [".end", ""]
    path.write_text("\n".join(lines))
    with open(path.parent / "mc_values.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["run"] + list(M.PARAM_ORDER))
        for k, inst in enumerate(insts):
            w.writerow([k + 1] + [f"{inst[p]:.6e}" for p in M.PARAM_ORDER])
    return insts


def run_ltspice(deck: Path) -> str:
    cmd = [str(BATCH), "-t", "900", "-o", str(deck.parent), "-b", str(deck)]
    env = dict(os.environ, CWHT_LTSPICE_LOCK_WAIT="3600")   # other blocks share the one-run-at-a-time lock
    r = subprocess.run(cmd, capture_output=True, text=True, env=env)
    prov = r.stderr.strip()
    if r.returncode != 0:
        raise SystemExit(f"ltspice-batch failed ({r.returncode}):\n{r.stdout}\n{prov}")
    # the wrapper judges only that LTspice ran; a .meas that LTspice could not evaluate is a deck error here
    log = deck.with_suffix(".log").read_text(errors="replace")
    bad = [ln for ln in log.splitlines() if "not found" in ln.lower() or "^^^" in ln or "error" in ln.lower()]
    if bad:
        raise SystemExit("deck error in the LTspice log:\n" + "\n".join(bad))
    deck.with_name("ltspice_provenance.txt").write_text(prov + "\n")
    return prov


def parse_meas(log: Path) -> dict:
    """Per-step .meas results of an AC log: {name: [magnitude dB per step]}."""
    res, cur = {}, None
    for ln in log.read_text(errors="replace").splitlines():
        if ln.startswith("Measurement:"):
            cur = ln.split(":", 1)[1].strip().lower()
            res[cur] = []
        elif cur and ln.strip() and ln.strip()[0].isdigit() and "(" in ln:
            res[cur].append(float(ln.split("(", 1)[1].split("dB", 1)[0]))
        elif not ln.strip():
            cur = None if cur and res.get(cur) else cur
    return res


def snapshot_scripts(out: Path) -> dict:
    hashes = {}
    for f in ("run_lpf.py", "lpf_model.py", "retune_screen.py", "lpf_nodal.py", "worst_case.py"):
        shutil.copy2(HERE / f, out / f)
        hashes[f] = hashlib.sha256((HERE / f).read_bytes()).hexdigest()
    return hashes


# ---------------------------------------------------------------------------------------------
# Metrics
# ---------------------------------------------------------------------------------------------

def db(x):
    return 20 * np.log10(np.maximum(np.abs(x), 1e-30))


def band_min_att(f, s21, lo, hi):
    m = (f >= lo - 1) & (f <= hi + 1)
    return float(np.min(-db(s21[m])))


def metrics(f, s21, s11=None) -> dict:
    pb = (f >= M.F_LO - 1) & (f <= M.F_HI + 1)
    out = {"il_max_dB": float(np.max(-db(s21[pb]))), "il_146_dB": float(np.interp(146e6, f, -db(s21)))}
    for n in M.HARMONICS:
        lo, hi = M.harmonic_band(n)
        out[f"att_{n}f_dB"] = band_min_att(f, s21, lo, hi)
    for name, lo, hi, _ in M.REQ_TX:
        out[f"att_{name}_dB"] = band_min_att(f, s21, lo, hi)
    if s11 is not None:
        out["rl_min_dB"] = float(np.min(-db(s11[pb])))
        # dissipative part of the loss: |S21|^2 / (1 - |S11|^2); the rest is mismatch (detuning)
        g = np.abs(s21[pb]) ** 2 / np.maximum(1 - np.abs(s11[pb]) ** 2, 1e-12)
        out["il_diss_max_dB"] = float(np.max(-10 * np.log10(g)))
    return out


def req_pass(mt: dict) -> dict:
    res = {name: mt[f"att_{name}_dB"] >= lim for name, _, _, lim in M.REQ_TX}
    res["IL"] = mt["il_max_dB"] <= M.IL_MAX_DB
    return res


# ---------------------------------------------------------------------------------------------
# Requirement points for the S21 plots
# ---------------------------------------------------------------------------------------------

def required_att(alt: str, n: int) -> tuple[float, float]:
    """Needed A(nf) - IL(f), the harmonic attenuation less the carrier loss of the same filter (revision 2):
    (legal: highest over the steps at +1 dB and the pack voltages of P + H - limit; the 60 dBc target at the
    5 W step, highest over the pack voltages)."""
    legal, target = -1e9, -1e9
    for v in M.PACK_V:
        for step in M.POWER_STEPS_W:
            p_w = step * 10 ** (M.STEP_TOL_DB / 10)
            lim = M.w_to_dbm(M.limit_97307e_w(p_w))
            legal = max(legal, M.w_to_dbm(p_w) + M.pa_harmonic_dbc(alt, n, step, v) - lim)
        target = max(target, M.pa_harmonic_dbc(alt, n, 5.0, v) + M.TARGET_DBC_5W)
    return legal, target


def overlay_requirements(ax, fmax=1.6e9, label=True):
    # REQ-TX allocation masks (filter-level)
    for i, (name, lo, hi, lim) in enumerate(M.REQ_TX):
        ax.plot([lo / 1e6, hi / 1e6], [-lim, -lim], color=INK, lw=1.6, ls="--",
                label="REQ-TX-009/010/011 allocation (filter)" if (i == 0 and label) else None)
    # finalist points at the harmonic band centres
    for alt, mk in (("A5", "s"), ("A4", "^")):
        xs, leg, tgt = [], [], []
        for n in M.HARMONICS:
            lo, hi = M.harmonic_band(n)
            if lo > fmax:
                continue
            a, t = required_att(alt, n)
            xs.append((lo + hi) / 2e6)
            leg.append(-a)
            tgt.append(-t)
        ax.plot(xs, leg, ls="none", marker=mk, ms=8, mfc="none", mec=INK, mew=1.4,
                label=f"{alt}: A(nf) - IL(f) needed for 97.307(e) 25 uW (worst step, 6.4 to 8.4 V)" if label else None)
        ax.plot(xs, tgt, ls="none", marker=mk, ms=6, mfc=INK2, mec=INK2,
                label=f"{alt}: A(nf) - IL(f) needed for the 60 dBc target at 5 W (6.4 to 8.4 V)" if label else None)
    for n in M.HARMONICS:
        lo, hi = M.harmonic_band(n)
        ax.axvspan(lo / 1e6, hi / 1e6, color=GRID, alpha=0.8, lw=0)
        ax.text((lo + hi) / 2e6, 3, f"{n}f", ha="center", va="bottom", fontsize=7, color=INK2)


# ---------------------------------------------------------------------------------------------
# Runs
# ---------------------------------------------------------------------------------------------

def outdir(run: str) -> Path:
    d = HERE / "results" / RUNS[run]
    d.mkdir(parents=True, exist_ok=True)
    return d


def do_r1():
    out = outdir("r1")
    deck = out / "lpf_r1.cir"
    params = write_nominal_deck(deck)
    prov = run_ltspice(deck)
    raw = RawRead(str(out / "lpf_r1.raw"))
    f = np.abs(raw.get_trace("frequency").get_wave())
    tr = {s: (raw.get_trace(f"V(in{s})").get_wave(), raw.get_trace(f"V(out{s})").get_wave())
          for s in ("_i", "_b", "_c", "_w")}
    decomp = {s: float(np.max(-db(raw.get_trace(f"V(out{s})").get_wave()[(f >= M.F_LO - 1) & (f <= M.F_HI + 1)])))
              for s in ("_q", "_e")}
    res = {"run": RUNS["r1"], "ltspice": prov.splitlines(), "variants": {},
           "il_decomposition_1812_dB": {"coil loss only": decomp["_q"], "capacitor ESR only": decomp["_e"]}}
    names = {"_i": "ideal exact", "_b": "ideal BOM values", "_c": "Coilcraft 1812SMS + parasitics",
             "_w": "24 AWG air coils + parasitics"}
    for s, (vin, vout) in tr.items():
        mt = metrics(f, vout, vin - 1)
        mt["pass"] = req_pass(mt)
        res["variants"][names[s]] = mt
    # known answer: ideal exact vs the analytic Chebyshev
    ana = M.chebyshev_att_db(f)
    sim = -db(tr["_i"][1])
    ok = ana < 150
    ka = {"max_abs_err_dB": float(np.max(np.abs(sim[ok] - ana[ok]))),
          "at": {f"{int(x / 1e6)} MHz": [float(np.interp(x, f, sim)), float(M.chebyshev_att_db(np.array([x]))[0])]
                 for x in (146e6, 148e6, 288e6, 296e6, 432e6, 444e6)}}
    ka["pass"] = ka["max_abs_err_dB"] <= 0.05
    res["known_answer"] = ka
    if not ka["pass"]:
        STATUS["checks_failed"].append("r1 known answer")
    for name, mt in res["variants"].items():
        if name.startswith("ideal"):
            continue
        for k, ok in mt["pass"].items():
            if not ok:
                STATUS["criteria_failed"].append(f"r1 {name}: {k}")
    res["air_coils"] = {f"{int(L * 1e9)} nH": M.air_coil(L) for L in (68e-9, 82e-9)}
    res["nominal_params"] = {k: {kk: float(vv) for kk, vv in v.items()} for k, v in params.items() if k != "ideal"}
    res["scripts_sha256"] = snapshot_scripts(out)

    # Plot 1: wide S21
    fig, ax = plt.subplots(figsize=(10, 6.8))
    overlay_requirements(ax)
    style = {"_i": ("ideal", 1.0, ":"), "_b": ("idealbom", 1.0, "-"), "_c": ("1812", 2.0, "-"), "_w": ("air", 2.0, "-")}
    for s, (vin, vout) in tr.items():
        c, lw, ls = style[s]
        ax.plot(f / 1e6, db(vout), color=COL[c], lw=lw, ls=ls, label=names[s])
    ax.set_xlim(0, 1600)
    ax.set_ylim(-140, 8)
    ax.set_xlabel("Frequency (MHz)")
    ax.set_ylabel("S21 (dB)")
    ax.set_title("TS-012 7-pole Chebyshev LPF, nominal S21 with the harmonic limit points (run r1)", color=INK)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.11), fontsize=7.5, ncol=2)
    fig.tight_layout()
    fig.savefig(out / "s21_nominal_wide.png", dpi=150)
    plt.close(fig)

    # Plot 2: passband insertion loss
    fig, ax = plt.subplots(figsize=(8, 4.5))
    for s, (vin, vout) in tr.items():
        c, lw, ls = style[s]
        ax.plot(f / 1e6, -db(vout), color=COL[c], lw=lw, ls=ls, label=names[s])
    ax.axvspan(144, 148, color=GRID, lw=0)
    ax.plot([144, 148], [M.IL_MAX_DB] * 2, color=INK, lw=1.6, ls="--", label="0.5 dB goal, 144 to 148 MHz")
    ax.set_xlim(100, 200)
    ax.set_ylim(0, 3)
    ax.set_xlabel("Frequency (MHz)")
    ax.set_ylabel("Insertion loss, -S21 (dB)")
    ax.set_title("Passband insertion loss, nominal (run r1)", color=INK)
    ax.legend(loc="upper left", fontsize=7.5)
    fig.tight_layout()
    fig.savefig(out / "il_nominal_passband.png", dpi=150)
    plt.close(fig)

    # Plot 3: return loss
    fig, ax = plt.subplots(figsize=(8, 4.5))
    for s, (vin, vout) in tr.items():
        c, lw, ls = style[s]
        ax.plot(f / 1e6, -db(vin - 1), color=COL[c], lw=lw, ls=ls, label=names[s])
    ax.axvspan(144, 148, color=GRID, lw=0)
    ax.plot([144, 148], [10, 10], color=INK, lw=1.6, ls="--", label="10 dB (VSWR 1.9) reference, not a requirement")
    ax.set_xlim(100, 200)
    ax.set_ylim(0, 45)
    ax.set_xlabel("Frequency (MHz)")
    ax.set_ylabel("Input return loss, -S11 (dB)")
    ax.set_title("Passband input return loss seen by the PA, nominal (run r1)", color=INK)
    ax.legend(loc="upper right", fontsize=7.5)
    fig.tight_layout()
    fig.savefig(out / "rl_nominal_passband.png", dpi=150)
    plt.close(fig)

    (out / "result.json").write_text(json.dumps(res, indent=2))
    write_r1_md(out, res)
    return res


def write_r1_md(out: Path, res: dict):
    L = [f"# Run {res['run']}: nominal S21 of the TS-012 harmonic LPF", "",
         "Deck `lpf_r1.cir`, LTspice AC 0.5 to 1600 MHz in 0.5 MHz steps, 50 ohm source and load. "
         "S21 = V(out) with a 2 V AC source.", "",
         f"Known answer (ideal exact element values against the analytic 0.1 dB Chebyshev): max error "
         f"{res['known_answer']['max_abs_err_dB']:.4f} dB where the analytic value is under 150 dB; "
         f"**{'PASS' if res['known_answer']['pass'] else 'FAIL'}** (criterion 0.05 dB).", "",
         "| Variant | IL max 144-148 (dB) | RL min (dB) | 2f min (dB) | 3f min (dB) | 576-1500 MHz min (dB) | 7f (dB) | Verdict (40/35/40 dB, 0.5 dB) |",
         "|---|---|---|---|---|---|---|---|"]
    dec = res["il_decomposition_1812_dB"]
    for name, mt in res["variants"].items():
        ok = all(mt["pass"].values())
        L.append(f"| {name} | {mt['il_max_dB']:.3f} | {mt['rl_min_dB']:.1f} | {mt['att_2f_dB']:.1f} | {mt['att_3f_dB']:.1f} | "
                 f"{mt['att_REQ-TX-011_dB']:.1f} | {mt['att_7f_dB']:.1f} | {'PASS' if ok else 'FAIL: ' + ', '.join(k for k, v in mt['pass'].items() if not v)} |")
    L += ["", f"Loss decomposition of the nominal 1812SMS build (max over 144 to 148 MHz): coil loss alone "
          f"{dec['coil loss only']:.3f} dB, capacitor ESR alone {dec['capacitor ESR only']:.3f} dB.", "",
          "Plots: `s21_nominal_wide.png`, `il_nominal_passband.png`, `rl_nominal_passband.png`.", ""]
    (out / "result.md").write_text("\n".join(L))




# ---------------------------------------------------------------------------------------------
# Revision 2: worst case (corner search) and Monte Carlo per build
# ---------------------------------------------------------------------------------------------
TRAP_VALS = [10e-12, 47e-9, 20e-12, 68e-9, 20e-12, 47e-9, 10e-12]
TRAPS = {2: 5.6e-12, 6: 5.6e-12}
MID_VALS = [22e-12, 68e-9, 36e-12, 82e-9, 36e-12, 68e-9, 22e-12]
REV2 = {
    "r8": dict(kind="1812", coil_tol=None, cap_tol=0.05, vals=M.BOM, traps=None, seed=21008, color=COL["1812"],
               label="Coilcraft 1812SMS (J, 5 %), BOM values 22/68/39/82"),
    "r9": dict(kind="air", coil_tol=0.10, cap_tol=0.05, vals=M.BOM, traps=None, seed=21009, color=COL["air"],
               label="24 AWG air coils as wound (+/-10 %), BOM values"),
    "r10": dict(kind="air", coil_tol=0.03, cap_tol=0.05, vals=M.BOM, traps=None, seed=21010, color=COL["air_al"],
                label="24 AWG air coils aligned (+/-3 %), BOM values"),
    "r11": dict(kind="1812", coil_tol=None, cap_tol=0.05, vals=M.RETUNE, traps=None, seed=21011, color="#4a3aa7",
                label="Coilcraft 1812SMS (J, 5 %), retuned 18/68/33/82"),
    "r12": dict(kind="air", coil_tol=0.03, cap_tol=0.05, vals=M.RETUNE, traps=None, seed=21012, color="#e87ba4",
                label="24 AWG air coils aligned (+/-3 %), retuned 18/68/33/82"),
    "r13": dict(kind="1812", coil_tol=0.02, cap_tol=0.02, vals=M.BOM, traps=None, seed=21013, color="#0f7b8a",
                label="Coilcraft 1812SMS (G, 2 %) and C0G (G, 2 %), BOM values 22/68/39/82"),
    "r14": dict(kind="1812", coil_tol=0.02, cap_tol=0.02, vals=MID_VALS, traps=None, seed=21014, color="#b8860b",
                label="Coilcraft 1812SMS (G, 2 %) and C0G (G, 2 %), 22/68/36/82"),
    "r16": dict(kind="1812", coil_tol=0.05, cap_tol=0.05, vals=TRAP_VALS, traps=TRAPS, seed=21016, color="#7f8c8d",
                label="Screened and rejected: 1812SMS (J), 10/47/20/68 with 5.6 pF traps across L2 and L6"),
}
WC_ROW = {"il": "IL max 144-148 MHz", "att2": "Min atten. 288-296 MHz", "att3": "Min atten. 432-444 MHz",
          "atthi": "Min atten. 576-1500 MHz", "eff2": "Min A(2f) - IL(f)", "eff3": "Min A(3f) - IL(f)",
          "effhi": "Min A(nf) - IL(f), n = 4 to 10"}
RL_REF = 0.75   # revision 1's proposed criterion, checked here only to answer review finding-1


def deck_names(traps) -> list[str]:
    names = [n for n in M.PARAM_ORDER if not (n.endswith("Q") or n.endswith("SRF"))]
    for n in sorted(traps or {}):
        names += [f"L{n}{k}" for k in M.TRAP_FREE]
    return names


def write_wc_deck(path: Path, run: str, insts: list[dict], n_mc_steps: int) -> None:
    cfg = REV2[run]
    names = deck_names(cfg["traps"])
    n = len(insts)
    lines = [f"* cwht TS-012 harmonic LPF, run {run} (revision 2): {cfg['label']} ({DATE}); generated by run_lpf.py",
             f"* steps 1 and 2: every L and C at -tol and +tol (nominal parasitics); steps 3 to {n_mc_steps}: uniform",
             f"* random over the parameter box (numpy seed {cfg['seed']}, signed coil coupling); steps {n_mc_steps + 1} "
             f"to {n}: worst-case corners",
             "* found by worst_case.py, one per metric (" + ", ".join(W.METRICS) + "). Every value in mc_values.csv.",
             "* S21 = V(out_m), S11 = V(in_m) - 1 (2 V source, 50 ohm)."]
    lines.append(f".step param run 1 {n} 1")
    for name in names:
        pairs = [f"{k + 1},{fmt(inst[name])}" for k, inst in enumerate(insts)]
        chunk = [", ".join(pairs[i:i + 8]) for i in range(0, len(pairs), 8)]
        lines.append(f".param {name}=table(run, " + chunk[0] + ("," if len(chunk) > 1 else ")"))
        for ci, c in enumerate(chunk[1:], start=1):
            lines.append("+ " + c + ("," if ci < len(chunk) - 1 else ")"))
    lines += filter_real("_m", {}, param=True, traps=sorted(cfg["traps"] or {}))
    fl = [f"{x:.0f}" for x in M.FREQS]
    lines.append(".ac list " + " ".join(fl[:12]))
    for i in range(12, len(fl), 12):
        lines.append("+ " + " ".join(fl[i:i + 12]))
    lines.append(".save V(out_m) V(in_m)")
    for f in (146e6, 148e6, 288e6, 432e6):
        lines.append(f".meas AC s21_{int(f / 1e6)} FIND V(out_m) AT {f:.0f}")
    lines.append(".meas AC echo_L4 PARAM L4L")
    lines += [".end", ""]
    path.write_text("\n".join(lines))
    with open(path.parent / "mc_values.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["run", "kind"] + names + [k for k in insts[0] if k.endswith("Q") or k.endswith("SRF")])
        extra = [k for k in insts[0] if k.endswith("Q") or k.endswith("SRF")]
        for k, inst in enumerate(insts):
            kind = ("corner -tol" if k == 0 else "corner +tol" if k == 1 else "monte carlo" if k < n_mc_steps
                    else f"worst case {W.METRICS[k - n_mc_steps]}")
            w.writerow([k + 1, kind] + [f"{inst[p]:.6e}" for p in names] + [f"{inst[p]:.6e}" for p in extra])


def metrics2(f, s21, s11) -> dict:
    """Revision 2 metrics on the .ac list grid (M.FREQS): as metrics(), plus eff_n = min over the carriers
    144 to 148 MHz (0.25 MHz) of A(nf) - IL(f), the harmonic relative to the carrier at the antenna."""
    out = metrics(f, s21, s11)
    a = -db(s21)
    def at(targets):
        i = np.searchsorted(f, targets)
        i = np.clip(i, 1, f.size - 1)
        i = np.where(np.abs(f[i - 1] - targets) < np.abs(f[i] - targets), i - 1, i)
        if float(np.max(np.abs(f[i] - targets))) > 1.0:
            raise SystemExit("frequency grid does not hold every carrier harmonic")
        return i

    ipb = at(M.PB_FINE)
    for n in M.HARMONICS:
        ih = at(n * M.PB_FINE)
        out[f"eff_{n}f_dB"] = float(np.min(a[ih] - a[ipb]))
    out["eff_hi_dB"] = min(out[f"eff_{n}f_dB"] for n in range(4, 11))
    out["att_hi_dB"] = out["att_REQ-TX-011_dB"]
    return out


WC_KEY = {"il": ("il_max_dB", "max"), "att2": ("att_2f_dB", "min"), "att3": ("att_3f_dB", "min"),
          "atthi": ("att_REQ-TX-011_dB", "min"), "eff2": ("eff_2f_dB", "min"), "eff3": ("eff_3f_dB", "min"),
          "effhi": ("eff_hi_dB", "min")}


def do_wc(run: str):
    cfg = REV2[run]
    out = outdir(run)
    kind = cfg["kind"]
    space = W.Space(kind, cfg["vals"], cfg["coil_tol"], cfg["cap_tol"], cfg["traps"])
    names = space.names
    rng = np.random.default_rng(cfg["seed"])
    free = [M.sample_free(space.b, names, None, -1), M.sample_free(space.b, names, None, +1)]
    free += [M.sample_free(space.b, names, rng) for _ in range(N_MC)]
    n_mc = len(free)
    insts = [M.deck_params(kind, fr) for fr in free]
    # worst Monte Carlo step per metric (nodal model), used as one start of the corner search
    wc = {}
    for m in W.METRICS:
        vals = np.array([W.metric_value(p, m) for p in insts])
        k = int(np.argmax(vals) if m == "il" else np.argmin(vals))
        r = W.search(space, m, extra_starts=[(f"worst Monte Carlo step {k + 1}", free[k])], n_random=6)
        wc[m] = r
        print(f"  {run} {m}: {r['value_dB']:.3f} dB (from {r['from_start']})", flush=True)
    insts += [wc[m]["deck"] for m in W.METRICS]
    deck = out / f"lpf_{run}.cir"
    write_wc_deck(deck, run, insts, n_mc)
    prov = run_ltspice(deck)
    raw = RawRead(str(out / f"lpf_{run}.raw"))
    steps = raw.get_steps()
    f = np.abs(raw.get_trace("frequency").get_wave(steps[0]))
    s21 = np.array([raw.get_trace("V(out_m)").get_wave(s) for s in steps])
    s11 = np.array([raw.get_trace("V(in_m)").get_wave(s) - 1 for s in steps])
    checks = {}
    checks["step_count"] = s21.shape[0] == len(insts)
    checks["grid_is_deck_list"] = f.size == M.FREQS.size and float(np.max(np.abs(f - M.FREQS))) < 1.0
    per = [metrics2(f, a, b) for a, b in zip(s21, s11)]
    # known answer 1: the nodal model of the search against LTspice at every step and every frequency
    err = 0.0
    for p, a in zip(insts, s21):
        sn, _ = N.s_params(f, p)
        m = db(a) > -120
        err = max(err, float(np.max(np.abs(db(sn)[m] - db(a)[m]))))
    checks["nodal_vs_ltspice_max_dB"] = err
    checks["nodal_vs_ltspice"] = err < 0.01
    # known answer 2: every corner's metric in LTspice equals the search value
    dev = {m: per[n_mc + i][WC_KEY[m][0]] - wc[m]["value_dB"] for i, m in enumerate(W.METRICS)}
    checks["corner_metric_deviation_dB"] = dev
    checks["corner_metrics"] = all(abs(d) < 0.01 for d in dev.values())
    # log cross-checks of revision 1: echoed L4 and the .meas S21 at 288 MHz against the .raw
    meas = parse_meas(out / f"lpf_{run}.log")
    echo = [10 ** (v / 20) for v in meas["echo_l4"]]
    checks["echo_L4"] = len(echo) == len(insts) and all(abs(e - i["L4L"]) / i["L4L"] < 1e-6 for e, i in zip(echo, insts))
    k288 = int(np.argmin(np.abs(f - 288e6)))
    checks["meas_288_vs_raw"] = (len(meas["s21_288"]) == len(insts) and
                                 float(np.max(np.abs(np.array(meas["s21_288"]) - db(s21[:, k288])))) < 1e-3)
    checks_ok = all(v for k, v in checks.items() if isinstance(v, bool))
    if not checks_ok:
        STATUS["checks_failed"].append(f"{run}: " + ", ".join(k for k, v in checks.items() if v is False))

    keys = (["il_max_dB", "il_diss_max_dB", "rl_min_dB", "eff_hi_dB"] + [f"att_{n}f_dB" for n in M.HARMONICS]
            + [f"eff_{n}f_dB" for n in M.HARMONICS] + [f"att_{n}_dB" for n, *_ in M.REQ_TX])
    agg = {}
    for k in keys:
        v_all = np.array([p[k] for p in per])
        v_mc = v_all[:n_mc]
        agg[k] = {"mc_min": float(v_mc.min()), "mc_p01": float(np.percentile(v_mc, 1)),
                  "mc_median": float(np.median(v_mc)), "mc_p99": float(np.percentile(v_mc, 99)),
                  "mc_max": float(v_mc.max()), "corner_low": float(v_all[0]), "corner_high": float(v_all[1]),
                  "all_min": float(v_all.min()), "all_max": float(v_all.max()),
                  "wc_steps": {m: float(v_all[n_mc + i]) for i, m in enumerate(W.METRICS)}}
    worst = {"il_max_dB": agg["il_max_dB"]["all_max"]}
    worst.update({k: agg[k]["all_min"] for k in keys if k != "il_max_dB"})
    mc_worst = {"il_max_dB": agg["il_max_dB"]["mc_max"]}
    mc_worst.update({k: agg[k]["mc_min"] for k in keys if k != "il_max_dB"})
    verdict = {name: worst[f"att_{name}_dB"] >= lim for name, _, _, lim in M.REQ_TX}
    verdict["IL"] = worst["il_max_dB"] <= M.IL_MAX_DB
    for k, ok in verdict.items():
        if not ok:
            STATUS["criteria_failed"].append(f"{run}: {k} at the worst case")
    passes = [all(req_pass(p).values()) for p in per[:n_mc]]
    # the worst-2f corner's layout terms (review finding-1: the two-via layout rule is the lowest-2f corner)
    corner2 = wc["att2"]["free"]
    via_note = {f"C{i + 1}Lvia_nH": corner2[f"C{i + 1}Lvia"] * 1e9 for i in M.CAP_POS}
    res = {"run": RUNS[run], "revision": 2, "label": cfg["label"], "kind": kind, "values": cfg["vals"],
           "traps": cfg["traps"], "coil_tol": cfg["coil_tol"], "cap_tol": cfg["cap_tol"], "n_steps": len(insts),
           "n_mc_steps": n_mc, "seed": cfg["seed"], "ltspice": prov.splitlines(), "checks": checks,
           "checks_pass": checks_ok, "stats": agg, "worst_case": worst, "mc_worst": mc_worst,
           "verdict_worst_case": verdict, "meets_0p75_dB_at_worst_case": worst["il_max_dB"] <= RL_REF,
           "yield_mc_all_four": float(np.mean(passes)),
           "search": {m: {k: v for k, v in wc[m].items() if k not in ("deck",)} for m in W.METRICS},
           "worst_2f_corner_via_L_nH": via_note, "via_L_bounds_nH": [x * 1e9 for x in M.VIA_L],
           "scripts_sha256": snapshot_scripts(out)}
    (out / "result.json").write_text(json.dumps(res, indent=2, default=float))
    plots_wc(run, out, f, s21, per, n_mc, wc)
    write_wc_md(run, out, res)
    return res


def plots_wc(run, out, f, s21, per, n_mc, wc):
    cfg = REV2[run]
    c = cfg["color"]
    d = db(s21)
    fm = f / 1e6
    base = np.isin(f, M.BASE_GRID)
    wcols = {"il": "#c0392b", "att2": "#d35400", "att3": "#6d4c41", "atthi": "#7f8c8d", "eff2": "#8e44ad",
             "eff3": "#2c3e50", "effhi": "#95a5a6"}
    # S21 wide
    fig, ax = plt.subplots(figsize=(10, 7.2))
    overlay_requirements(ax)
    for w in d[2:n_mc]:
        ax.plot(fm[base], w[base], color=c, lw=0.4, alpha=0.10)
    ax.plot(fm[base], d[:n_mc][:, base].max(axis=0), color=c, lw=1.4, label=f"Monte Carlo envelope ({n_mc} steps)")
    ax.plot(fm[base], d[:n_mc][:, base].min(axis=0), color=c, lw=1.4)
    for i, m in enumerate(W.METRICS):
        if m in ("att2", "atthi", "il"):
            ax.plot(fm[base], d[n_mc + i][base], color=wcols[m], lw=1.1, ls="--" if m != "il" else "-.",
                    label=f"worst-case corner for: {WC_ROW[m]}")
    ax.set_xlim(0, 1600)
    ax.set_ylim(-140, 8)
    ax.set_xlabel("Frequency (MHz)")
    ax.set_ylabel("S21 (dB)")
    ax.set_title(f"S21: Monte Carlo and worst-case corners, {cfg['label']} (run {run})", color=INK, fontsize=9)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.1), fontsize=7.2, ncol=2)
    fig.tight_layout()
    fig.savefig(out / "s21_wc_wide.png", dpi=150)
    plt.close(fig)
    # zoom on 2f and 3f with the needed A(nf) levels
    fig, axs = plt.subplots(1, 2, figsize=(11, 4.4))
    for ax, n in zip(axs, (2, 3)):
        lo, hi = M.harmonic_band(n)
        sel = (f >= lo - 40e6) & (f <= hi + 40e6)
        for w in d[2:n_mc]:
            ax.plot(fm[sel], -w[sel], color=c, lw=0.4, alpha=0.12)
        for i, m in enumerate(W.METRICS):
            if m in (f"att{n}", f"eff{n}"):
                ax.plot(fm[sel], -d[n_mc + i][sel], color=wcols[m], lw=1.6, ls="-" if m.startswith("att") else ":",
                        label=f"attenuation of the worst-case corner for: {WC_ROW[m]}")
        ax.axvspan(lo / 1e6, hi / 1e6, color=GRID, lw=0)
        req = {2: 40.0, 3: 35.0}[n]
        ax.axhline(req, color=INK, lw=1.6, ls="--", label=f"REQ-TX-{9 if n == 2 else 10:03d} {req:g} dB (filter)")
        for alt, ls in (("A5", ":"), ("A4", "-.")):
            leg, tgt = required_att(alt, n)
            ax.axhline(tgt, color=INK2, lw=1.2, ls=ls, label=f"{alt}: A - IL needed for 60 dBc at 5 W ({tgt:.0f} dB)")
        ax.set_xlabel("Frequency (MHz)")
        ax.set_ylabel("Attenuation, -S21 (dB)")
        ax.set_title(f"{n}f band ({lo / 1e6:.0f} to {hi / 1e6:.0f} MHz)", color=INK, fontsize=9)
        ax.set_ylim(20, 110)
        ax.legend(loc="upper left", fontsize=6.8)
    fig.suptitle(f"Harmonic bands, {cfg['label']} (run {run})", color=INK, fontsize=9)
    fig.tight_layout()
    fig.savefig(out / "harmonic_bands_wc.png", dpi=150)
    plt.close(fig)
    # passband
    fig, ax = plt.subplots(figsize=(8, 4.6))
    sel = (f >= 100e6) & (f <= 200e6)
    for w in d[2:n_mc]:
        ax.plot(fm[sel], -w[sel], color=c, lw=0.5, alpha=0.18)
    ax.plot(fm[sel], -d[0][sel], color=INK2, lw=1.1, ls="-.", label="corner: all L, C at -tol (rev. 1)")
    ax.plot(fm[sel], -d[1][sel], color=INK2, lw=1.1, ls=":", label="corner: all L, C at +tol (rev. 1)")
    i_il = W.METRICS.index("il")
    ax.plot(fm[sel], -d[n_mc + i_il][sel], color=wcols["il"], lw=1.8, label="worst-case corner for passband loss")
    ax.axvspan(144, 148, color=GRID, lw=0)
    ax.plot([144, 148], [M.IL_MAX_DB] * 2, color=INK, lw=1.8, ls="--", label="0.5 dB criterion (WP-PDR-21)")
    ax.plot([144, 148], [RL_REF] * 2, color=INK2, lw=1.2, ls="--", label="0.75 dB (revision 1 proposal, withdrawn)")
    ax.set_xlim(100, 200)
    ax.set_ylim(0, 4)
    ax.set_xlabel("Frequency (MHz)")
    ax.set_ylabel("Insertion loss, -S21 (dB)")
    ax.set_title(f"Passband loss, {cfg['label']} (run {run})", color=INK, fontsize=8.5)
    ax.legend(loc="upper left", fontsize=7)
    fig.tight_layout()
    fig.savefig(out / "il_wc_passband.png", dpi=150)
    plt.close(fig)
    # histograms with the worst-case value and the limits
    items = [("il_max_dB", "Max IL 144-148 MHz (dB)", M.IL_MAX_DB, "le", "il"),
             ("att_2f_dB", "Min atten. 288-296 MHz (dB)", 40.0, "ge", "att2"),
             ("att_3f_dB", "Min atten. 432-444 MHz (dB)", 35.0, "ge", "att3"),
             ("att_REQ-TX-011_dB", "Min atten. 576-1500 MHz (dB)", 40.0, "ge", "atthi"),
             ("eff_2f_dB", "Min A(2f) - IL(f) (dB)", None, "ge", "eff2")]
    fig, axs = plt.subplots(1, 5, figsize=(15, 3.6))
    for axh, (k, lab, lim, sense, m) in zip(axs, items):
        vals = np.array([p[k] for p in per[:n_mc]])
        wv = per[n_mc + W.METRICS.index(m)][k]
        axh.hist(vals, bins=30, color=c, edgecolor="#fcfcfb", linewidth=0.5)
        if lim is not None:
            axh.axvline(lim, color=INK, ls="--", lw=1.6)
        else:
            for alt, ls in (("A5", ":"), ("A4", "-.")):
                axh.axvline(required_att(alt, 2)[1], color=INK, ls=ls, lw=1.4)
        axh.axvline(wv, color=wcols[m], lw=2.0)
        txt = (f"limit {'<=' if sense == 'le' else '>='} {lim:g} (dashed)" if lim is not None else
               f"60 dBc need: A5 {required_att('A5', 2)[1]:.0f} (dotted), A4 {required_att('A4', 2)[1]:.0f} (dash-dot)")
        axh.text(0.03, 0.97, txt + f"\nworst case {wv:.2f} (solid)", transform=axh.transAxes, color=INK, fontsize=6.5,
                 va="top", bbox=dict(facecolor="#fcfcfb", edgecolor="none", pad=1.5))
        refs = [lim] if lim is not None else [required_att("A5", 2)[1], required_att("A4", 2)[1]]
        lo_x = min(vals.min(), wv, *refs)
        hi_x = max(vals.max(), wv, *refs)
        pad = 0.08 * (hi_x - lo_x + 1e-9)
        axh.set_xlim(lo_x - pad, hi_x + pad)
        axh.set_xlabel(lab, fontsize=8)
        axh.set_ylabel("Monte Carlo steps")
    fig.suptitle(f"Monte Carlo distributions and the worst-case corner, {cfg['label']} (run {run})", color=INK,
                 fontsize=9)
    fig.tight_layout()
    fig.savefig(out / "mc_wc_histograms.png", dpi=150)
    plt.close(fig)


def write_wc_md(run, out, res):
    s, w, mw, ck = res["stats"], res["worst_case"], res["mc_worst"], res["checks"]
    L = [f"# Run {res['run']}: worst case and Monte Carlo, {res['label']}", "",
         f"Deck `lpf_{run}.cir`, {res['n_steps']} steps: 1 and 2 every L and C at -tol and +tol (nominal parasitics); "
         f"3 to {res['n_mc_steps']} uniform random over the parameter box (seed {res['seed']}, coil coupling signed); "
         f"{res['n_mc_steps'] + 1} to {res['n_steps']} the worst-case corners that `worst_case.py` found, one per "
         "metric. Every parameter of every step is in `mc_values.csv`. LTspice `.ac list` on the grid of "
         "`lpf_model.FREQS` (2 MHz to 1.6 GHz, the carriers 144 to 148 MHz in 0.25 MHz steps and every harmonic of "
         "each).", "",
         f"Checks: nodal model against LTspice at every step and frequency, max {ck['nodal_vs_ltspice_max_dB']:.2e} dB "
         f"(criterion 0.01 dB) **{'PASS' if ck['nodal_vs_ltspice'] else 'FAIL'}**; every corner's metric in LTspice "
         f"equals the search value within 0.01 dB **{'PASS' if ck['corner_metrics'] else 'FAIL'}**; L4 echo "
         f"**{'PASS' if ck['echo_L4'] else 'FAIL'}**; .meas S21 at 288 MHz against the .raw "
         f"**{'PASS' if ck['meas_288_vs_raw'] else 'FAIL'}**.", "",
         "| Quantity (dB) | Worst case (corner search, LTspice) | Monte Carlo worst | MC 1st/99th pct | MC median | "
         "Rev. 1 corner -tol / +tol | Limit | Verdict (worst case) |", "|---|---|---|---|---|---|---|---|"]
    rows = [("il_max_dB", "IL max 144-148 MHz", M.IL_MAX_DB, "le", "IL"),
            ("att_2f_dB", "Min atten. 288-296 MHz", 40.0, "ge", "REQ-TX-009"),
            ("att_3f_dB", "Min atten. 432-444 MHz", 35.0, "ge", "REQ-TX-010"),
            ("att_REQ-TX-011_dB", "Min atten. 576-1500 MHz", 40.0, "ge", "REQ-TX-011"),
            ("eff_2f_dB", "Min A(2f) - IL(f)", None, "ge", None),
            ("eff_3f_dB", "Min A(3f) - IL(f)", None, "ge", None),
            ("eff_hi_dB", "Min A(nf) - IL(f), n 4 to 10", None, "ge", None)]
    for k, lab, lim, sense, key in rows:
        a = s[k]
        wv = w[k]
        mv = mw[k]
        pct = a["mc_p99"] if sense == "le" else a["mc_p01"]
        lim_s = "-" if lim is None else f"{'<=' if sense == 'le' else '>='} {lim:g}"
        ver = "-" if key is None else ("PASS" if res["verdict_worst_case"][key] else "FAIL")
        L.append(f"| {lab} | {wv:.2f} | {mv:.2f} | {pct:.2f} | {a['mc_median']:.2f} | "
                 f"{a['corner_low']:.2f} / {a['corner_high']:.2f} | {lim_s} | {ver} |")
    L += ["", f"Revision 1's proposed 0.75 dB criterion at the worst case: "
          f"**{'met' if res['meets_0p75_dB_at_worst_case'] else 'not met'}** ({w['il_max_dB']:.2f} dB).", "",
          f"Dissipative part of the loss (|S21|^2 / (1 - |S11|^2)): MC median {s['il_diss_max_dB']['mc_median']:.2f} dB, "
          f"MC worst {s['il_diss_max_dB']['mc_max']:.2f} dB, worst of every step {s['il_diss_max_dB']['all_max']:.2f} dB. "
          f"Input return loss 144 to 148 MHz: MC median {s['rl_min_dB']['mc_median']:.1f} dB, worst of every step "
          f"{s['rl_min_dB']['all_min']:.1f} dB.", "",
          "Worst A(nf) - IL(f) per harmonic, every step (dB): " +
          ", ".join(f"{n}f {s[f'eff_{n}f_dB']['all_min']:.1f}" for n in M.HARMONICS), "",
          f"Monte Carlo yield (steps 1 to {res['n_mc_steps']} meeting all four filter criteria): "
          f"{100 * res['yield_mc_all_four']:.1f} %.", "",
          "Worst-case corner of the 2f attenuation, ground-via inductance of each shunt capacitor (nH): " +
          ", ".join(f"{k[:2]} {v:.2f}" for k, v in res["worst_2f_corner_via_L_nH"].items()) +
          f" (range {res['via_L_bounds_nH'][0]:.2f} to {res['via_L_bounds_nH'][2]:.2f} nH; the low end is two vias "
          "per capacitor on a 0.8 mm board).", "",
          "Corner search per metric (value, the start it came from, parameters at a bound):", ""]
    for m in W.METRICS:
        r = res["search"][m]
        L.append(f"- {WC_ROW[m]}: {r['value_dB']:.3f} dB from '{r['from_start']}' ({r['params_at_a_bound']} of "
                 f"{r['n_params']} parameters at a bound; nominal {r['nominal_dB']:.3f} dB).")
    L += ["", "Plots: `s21_wc_wide.png`, `harmonic_bands_wc.png`, `il_wc_passband.png`, `mc_wc_histograms.png`.", ""]
    (out / "result.md").write_text("\n".join(L))


# ---------------------------------------------------------------------------------------------
# Revision 2: harmonic budget per finalist (run r15)
# ---------------------------------------------------------------------------------------------
BUDGET_BUILDS = ["r8", "r9", "r10", "r11", "r12", "r13", "r14"]
SHORT = {"r8": "1812SMS J\nBOM", "r9": "air as wound\nBOM", "r10": "air aligned\nBOM", "r11": "1812SMS J\nretuned",
         "r12": "air aligned\nretuned", "r13": "1812SMS G\nBOM, 2 % C", "r14": "1812SMS G\n22/36, 2 % C"}
MODULE_W_64V = (4.46, 5.13)   # A5 module output at the 6.4 V pack end, TS-012 revision 4 section 7.3 (graph read, E)
RELAY_DB = 0.1                # G5V-2 relay loss, TS-012 section 7.3 (E)
FLOOR_W = 5.0 * 10 ** (-0.1)  # REQ-SYS-012: 5 W -1 dB = 3.97 W at the SMA


def budget_case(alt: str, eff: dict) -> dict:
    """97.307(e) at every step and pack voltage, every ramp instant, and the 60 dBc target at the 5 W step
    per pack voltage, for one set of A(nf) - IL(f) values (dB, per harmonic order)."""
    rows = []
    for v in M.PACK_V:
        for step in M.POWER_STEPS_W:
            p_w = step * 10 ** (M.STEP_TOL_DB / 10)
            p_dbm = M.w_to_dbm(p_w)
            lim = M.w_to_dbm(M.limit_97307e_w(p_w))
            for n in M.HARMONICS:
                h = M.pa_harmonic_dbc(alt, n, step, v)
                spur = p_dbm + h - eff[n]
                rows.append({"pack_V": v, "step_W": step, "n": n, "P_dBm": p_dbm, "H_dBc": h, "A_minus_IL_dB": eff[n],
                             "spur_dBm": spur, "limit_dBm": lim, "margin_dB": lim - spur})
    b = min(rows, key=lambda r: r["margin_dB"])
    target = {}
    for v in M.PACK_V:
        ms = [(eff[n] - (M.TARGET_DBC_5W + M.pa_harmonic_dbc(alt, n, 5.0, v)), n) for n in M.HARMONICS]
        m, n = min(ms)
        target[str(v)] = {"margin_dB": m, "binding_order": n, "pass": m >= 0}
    ramp = {}
    for v in M.PACK_V:
        worst = (1e9, None, None)
        for p_w in np.logspace(-3, np.log10(6.3), 400):
            for n in M.HARMONICS:
                h = M.pa_harmonic_dbc(alt, n, 5.0 if p_w >= 5.0 else 0.5, v)
                mg = M.w_to_dbm(M.limit_97307e_w(p_w)) - (M.w_to_dbm(p_w) + h - eff[n])
                if mg < worst[0]:
                    worst = (mg, float(p_w), n)
        ramp[str(v)] = {"margin_dB": worst[0], "at_W": worst[1], "order": worst[2]}
    return {"rows": rows, "legal_min_margin_dB": b["margin_dB"], "legal_pass": b["margin_dB"] >= 0,
            "legal_binding": {k: b[k] for k in ("pack_V", "step_W", "n")}, "target60": target,
            "target60_min_margin_dB": min(t["margin_dB"] for t in target.values()),
            "target60_pass": all(t["pass"] for t in target.values()), "ramp": ramp,
            "ramp_min_margin_dB": min(r["margin_dB"] for r in ramp.values())}


def do_budget():
    out = outdir("r15")
    builds = {}
    for run in BUDGET_BUILDS:
        j = json.loads((HERE / "results" / RUNS[run] / "result.json").read_text())
        st = j["stats"]
        builds[run] = {"label": j["label"], "checks_pass": j["checks_pass"],
                       "eff_wc": {n: st[f"eff_{n}f_dB"]["all_min"] for n in M.HARMONICS},
                       "eff_mc": {n: st[f"eff_{n}f_dB"]["mc_min"] for n in M.HARMONICS},
                       "il": {"mc_median": st["il_max_dB"]["mc_median"], "mc_worst": st["il_max_dB"]["mc_max"],
                              "worst_case": st["il_max_dB"]["all_max"]}}
    res = {"run": RUNS["r15"], "revision": 2, "inputs": {r: RUNS[r] for r in builds}, "pa_inputs": M.PA_HARMONICS,
           "pack_V": M.PACK_V, "results": {}, "a5_power_6v4": {}}
    for alt in ("A5", "A4"):
        res["results"][alt] = {}
        for run, b in builds.items():
            wc = budget_case(alt, b["eff_wc"])
            mc = budget_case(alt, b["eff_mc"])
            res["results"][alt][run] = {"build": b["label"], "worst_case": wc, "mc_worst": mc}
            if not wc["legal_pass"]:
                STATUS["criteria_failed"].append(f"r15 {alt} {run}: 97.307(e) at the worst case")
            if not wc["target60_pass"]:
                STATUS["criteria_failed"].append(f"r15 {alt} {run}: 60 dBc target at the worst case")
    for run, b in builds.items():
        rows = {}
        for basis, il in b["il"].items():
            p = [mw * 10 ** (-(il + RELAY_DB) / 10) for mw in MODULE_W_64V]
            rows[basis] = {"il_dB": il, "sma_W": p, "margin_dB": [10 * np.log10(x / FLOOR_W) for x in p]}
        res["a5_power_6v4"][run] = rows
    res["scripts_sha256"] = snapshot_scripts(out)
    (out / "result.json").write_text(json.dumps(res, indent=2, default=float))
    plots_budget(out, res, builds)
    write_budget_md(out, res, builds)
    return res


def plots_budget(out, res, builds):
    cols = {r: REV2[r]["color"] for r in builds}
    nb = len(builds)
    offs = {r: (i - (nb - 1) / 2) * 0.1 for i, r in enumerate(builds)}
    # 1. spur level at the antenna per order
    fig, axs = plt.subplots(2, 2, figsize=(13, 9.2), sharey=True, sharex=True)
    for col, alt in enumerate(("A5", "A4")):
        for row, steps in enumerate(([5.0], [0.5, 1.0, 2.0])):
            ax = axs[row, col]
            for run in builds:
                for basis, mfc in (("worst_case", cols[run]), ("mc_worst", "none")):
                    rows = [r for r in res["results"][alt][run][basis]["rows"] if r["step_W"] in steps]
                    xs, ys = [], []
                    for n in M.HARMONICS:
                        w = max((r for r in rows if r["n"] == n), key=lambda r: r["spur_dBm"] - r["limit_dBm"])
                        xs.append(n + offs[run])
                        ys.append(w["spur_dBm"])
                    ax.plot(xs, ys, ls="none", marker="o", ms=5.5, mec=cols[run], mfc=mfc,
                            label=(builds[run]["label"] if basis == "worst_case" else None))
            ax.axhline(M.w_to_dbm(25e-6), color=INK, ls="--", lw=1.6)
            ax.text(10.45, M.w_to_dbm(25e-6) + 1, "97.307(e): 25 uW (-16 dBm)", ha="right", fontsize=7.5, color=INK)
            if row == 0:
                y60 = M.w_to_dbm(5.0 * 10 ** 0.1) - M.TARGET_DBC_5W
                ax.axhline(y60, color=INK2, ls=":", lw=1.4)
                ax.text(10.45, y60 - 3.5, "REQ-SYS-018: 60 dBc below 6.3 W (-22 dBm)", ha="right", fontsize=7.5,
                        color=INK2)
            ax.set_xticks(M.HARMONICS)
            ax.set_xticklabels([f"{n}f" for n in M.HARMONICS])
            ax.set_xlim(1.4, 10.6)
            ax.set_ylim(-100, -5)
            ax.set_title(f"{M.PA_HARMONICS[alt]['name']}: " + ("5 W step +1 dB (6.3 W), worst pack voltage"
                         if row == 0 else "worst of the 0.5, 1, 2 W steps +1 dB and the pack voltages"),
                         color=INK, fontsize=9)
            if col == 0:
                ax.set_ylabel("Harmonic at the antenna port (dBm)")
            if row == 1:
                ax.set_xlabel("Harmonic order (filled: worst-case corner; hollow: Monte Carlo worst)")
    h, lab = axs[0, 0].get_legend_handles_labels()
    fig.legend(h, lab, loc="lower center", ncol=2, fontsize=7.5)
    fig.suptitle("Harmonic budget, revision 2: PA harmonic minus [A(nf) - IL(f)] of the filter (run r15)", color=INK)
    fig.tight_layout(rect=(0, 0.1, 1, 1))
    fig.savefig(out / "harmonic_budget.png", dpi=150)
    plt.close(fig)
    # 2. margins: 60 dBc target (top) and 97.307(e) (bottom) per pack voltage
    vcol = {"6.4": "#2a78d6", "7.2": "#1baf7a", "8.4": "#eb6834"}
    fig, axs = plt.subplots(2, 2, figsize=(13, 8.6), sharex=True)
    x = np.arange(nb)
    for col, alt in enumerate(("A5", "A4")):
        for row, what in enumerate(("target", "legal")):
            ax = axs[row, col]
            for k, v in enumerate(M.PACK_V):
                vs = str(v)
                wc_v, mc_v = [], []
                for run in builds:
                    r = res["results"][alt][run]
                    if what == "target":
                        wc_v.append(r["worst_case"]["target60"][vs]["margin_dB"])
                        mc_v.append(r["mc_worst"]["target60"][vs]["margin_dB"])
                    else:
                        wc_v.append(min(q["margin_dB"] for q in r["worst_case"]["rows"] if q["pack_V"] == v))
                        mc_v.append(min(q["margin_dB"] for q in r["mc_worst"]["rows"] if q["pack_V"] == v))
                xx = x + (k - 1) * 0.26
                ax.bar(xx, wc_v, width=0.24, color=vcol[vs], label=f"{v} V pack, worst case")
                ax.plot(xx, mc_v, ls="none", marker="D", ms=4.5, mfc="none", mec=INK,
                        label="Monte Carlo worst" if k == 0 else None)
                for xi, yi in zip(xx, wc_v):
                    ax.text(xi, yi + (0.4 if yi >= 0 else -0.4), f"{yi:.2f}" if abs(yi) < 0.95 else f"{yi:.1f}",
                            ha="center",
                            va="bottom" if yi >= 0 else "top", fontsize=6, color=INK2)
            ax.axhline(0, color=INK, lw=1.6, ls="--")
            ax.set_ylabel("Margin (dB)")
            ttl = ("60 dBc target at the 5 W step (REQ-SYS-018, REQ-TX-008)" if what == "target"
                   else "97.307(e) 25 uW, worst step (0.5 to 6.3 W)")
            ax.set_title(f"{M.PA_HARMONICS[alt]['name']}: {ttl}", color=INK, fontsize=9)
            ax.text(0.01, 0.02, "dashed line: requirement (margin 0)", transform=ax.transAxes, fontsize=7, color=INK)
            ax.set_xticks(x)
            ax.set_xticklabels([SHORT[r] for r in builds], fontsize=7)
    h, lab = axs[0, 0].get_legend_handles_labels()
    fig.legend(h, lab, loc="lower center", ncol=4, fontsize=8)
    fig.suptitle("Harmonic margins per filter build and pack voltage (run r15)", color=INK)
    fig.tight_layout(rect=(0, 0.05, 1, 1))
    fig.savefig(out / "harmonic_margins.png", dpi=150)
    plt.close(fig)
    # 3. A5 REQ-SYS-012 at the 6.4 V pack end
    fig, ax = plt.subplots(figsize=(11, 4.8))
    bcol = {"mc_median": "#1baf7a", "mc_worst": "#2a78d6", "worst_case": "#c0392b"}
    blab = {"mc_median": "filter loss: MC median", "mc_worst": "filter loss: MC worst",
            "worst_case": "filter loss: worst case"}
    for k, basis in enumerate(("mc_median", "mc_worst", "worst_case")):
        for i, run in enumerate(builds):
            lo, hi = res["a5_power_6v4"][run][basis]["margin_dB"]
            xx = i + (k - 1) * 0.25
            ax.plot([xx, xx], [lo, hi], color=bcol[basis], lw=7, solid_capstyle="butt",
                    label=blab[basis] if i == 0 else None)
            ax.text(xx, hi + 0.05, f"{hi:+.2f}", ha="center", va="bottom", fontsize=6, color=INK2)
            ax.text(xx, lo - 0.05, f"{lo:+.2f}", ha="center", va="top", fontsize=6, color=INK2)
    ax.axhline(0, color=INK, lw=1.6, ls="--", label="REQ-SYS-012 floor 3.97 W at the SMA")
    ax.set_xticks(range(nb))
    ax.set_xticklabels([SHORT[r] for r in builds], fontsize=7)
    ax.set_ylabel("Margin to 3.97 W (dB)")
    ax.set_title("A5 power at the SMA at the 6.4 V pack end: module 4.46 to 5.13 W (TS-012 7.3), relay 0.1 dB, "
                 "filter loss per build (bar = module range)", color=INK, fontsize=8.5)
    ax.legend(loc="lower left", fontsize=7.5)
    fig.tight_layout()
    fig.savefig(out / "a5_power_margin_6v4.png", dpi=150)
    plt.close(fig)


def write_budget_md(out, res, builds):
    L = [f"# Run {res['run']}: harmonic budget per finalist, revision 2", "",
         "Harmonic at the antenna = carrier at the step +1 dB + PA harmonic ratio - [A(nf) - IL(f)], where A(nf) - IL(f) "
         "is the worst over the carriers 144 to 148 MHz of the attenuation at the harmonic less the passband loss at "
         "that carrier, in the same filter instance (review finding-4). Worst case: the worst of every LTspice step "
         "of runs r8 to r14 (Monte Carlo and the worst-case corners); Monte Carlo worst: steps 1 to 252 only. "
         "Pack voltages 6.4, 7.2 and 8.4 V (REQ-SYS-017, REQ-TX-007, REQ-SYS-012; review finding-3): A5 at the 5 W "
         "step takes the datasheet maxima at 6.4 and 7.2 V and the back-off convention at 8.4 V; every lower step "
         "takes the back-off convention (lpf_model.pa_state). Limit: 47 CFR 97.307(e), 25 uW binds at every step. "
         "Target: REQ-SYS-018 60 dBc at the 5 W step.", "",
         "| Finalist | Filter build | 97.307(e): min margin (dB), where | Ramp min margin (dB) | 60 dBc at 6.4 / 7.2 / 8.4 V: margin (dB) | 60 dBc verdict | Monte Carlo worst: 97.307(e) / 60 dBc min margin (dB) |",
         "|---|---|---|---|---|---|---|"]
    for alt in ("A5", "A4"):
        for run in builds:
            r = res["results"][alt][run]
            w, m = r["worst_case"], r["mc_worst"]
            bd = w["legal_binding"]
            t = w["target60"]
            L.append(f"| {alt} | {r['build']} | {'PASS' if w['legal_pass'] else 'FAIL'} {w['legal_min_margin_dB']:.1f} "
                     f"({bd['n']}f, {bd['step_W']:g} W, {bd['pack_V']} V) | {w['ramp_min_margin_dB']:.1f} | "
                     + " / ".join(f"{t[str(v)]['margin_dB']:+.2f}" for v in M.PACK_V) +
                     f" | {'PASS' if w['target60_pass'] else 'FAIL'} | {m['legal_min_margin_dB']:.1f} / "
                     f"{m['target60_min_margin_dB']:+.1f} |")
    L += ["", "A5 power at the SMA at the 6.4 V pack end (REQ-SYS-012 floor 3.97 W; module 4.46 to 5.13 W from TS-012 "
          "section 7.3, relay 0.1 dB):", "",
          "| Filter build | Loss MC median / MC worst / worst case (dB) | Margin with the MC median loss (dB) | "
          "with the MC worst (dB) | with the worst case (dB) |", "|---|---|---|---|---|"]
    for run in builds:
        a = res["a5_power_6v4"][run]
        L.append(f"| {builds[run]['label']} | {a['mc_median']['il_dB']:.2f} / {a['mc_worst']['il_dB']:.2f} / "
                 f"{a['worst_case']['il_dB']:.2f} | "
                 + " | ".join(f"{a[b]['margin_dB'][0]:+.2f} to {a[b]['margin_dB'][1]:+.2f}"
                              for b in ("mc_median", "mc_worst", "worst_case")) + " |")
    L += ["", "PA harmonic inputs at the PA output: A5 full state 2f -25 dBc, 3f and above -30 dBc (RA07M1317M datasheet "
          "maxima at 6 W, 7.2 V; 4f and above estimated equal to 3f); A5 back-off state 2f -17 dBc, 3f and above -25 "
          "dBc (estimates). A4 2f -15 dBc, 3f and above -20 dBc at every step and pack voltage (estimate; no vendor "
          "data).", "", "Plots: `harmonic_budget.png`, `harmonic_margins.png`, `a5_power_margin_6v4.png`.", ""]
    (out / "result.md").write_text("\n".join(L))


if __name__ == "__main__":
    which = sys.argv[1:] or ["all"]
    if which == ["all"]:
        which = ["r1"] + [r for r in REV2 if r != "r16"] + ["r15", "r16"]
    for w in which:
        if w in LEGACY:
            raise SystemExit(f"{w} is a revision 1 run (superseded); reproduce it with the script copies in "
                             f"hardware/sim/tx-lpf/results/{RUNS[w]}/")
        if w == "r1":
            do_r1()
        elif w == "r15":
            do_budget()
        elif w in REV2:
            do_wc(w)
        else:
            raise SystemExit(f"unknown run {w}")
        print(f"{w}: done -> {RUNS[w]}", flush=True)
    for k in ("checks_failed", "criteria_failed"):
        for item in STATUS[k]:
            print(f"{k[:-7].upper()} FAILED: {item}")
    code = 2 if STATUS["checks_failed"] else 1 if STATUS["criteria_failed"] else 0
    print(f"exit status {code} (0 all met; 1 criterion failed, results valid; 2 check failed, results invalid)")
    sys.exit(code)
