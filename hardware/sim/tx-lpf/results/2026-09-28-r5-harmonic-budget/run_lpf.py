#!/usr/bin/env python3
"""TS-012 harmonic low-pass filter analysis (WP-PDR-21): deck writer, LTspice runner, checker, plots.

Usage (from any directory, with the repo venv):
    .venv/bin/python hardware/sim/tx-lpf/run_lpf.py r1        # nominal: ideal, ideal-BOM, 1812SMS, air coil
    .venv/bin/python hardware/sim/tx-lpf/run_lpf.py r2        # Monte Carlo, Coilcraft 1812SMS
    .venv/bin/python hardware/sim/tx-lpf/run_lpf.py r3        # Monte Carlo, 24 AWG air coils as wound (+/-10 %)
    .venv/bin/python hardware/sim/tx-lpf/run_lpf.py r4        # Monte Carlo, 24 AWG air coils aligned (+/-3 %)
    .venv/bin/python hardware/sim/tx-lpf/run_lpf.py r5        # harmonic budget per finalist (reads r2 to r4)
    .venv/bin/python hardware/sim/tx-lpf/run_lpf.py all

Each run writes hardware/sim/tx-lpf/results/<run-id>/: the deck, the LTspice .log and .raw (r1 to r4),
result.json and result.md (numbers and pass/fail), PNG plots with the limits overlaid, and a copy of the
two scripts that produced them. LTspice runs only through tools/ltspice-batch.sh (ACC-LTSPICE-001).
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
}
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


def filter_real(s: str, p: dict, param: bool = False) -> list[str]:
    """Filter with parasitics. With param=True the values are {names} bound by .param lines."""
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
    for f in ("run_lpf.py", "lpf_model.py", "retune_screen.py"):
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
    """(legal: highest over the steps at +1 dB of P + H - limit; 60 dBc target at the 5 W step)."""
    legal = -1e9
    for step in M.POWER_STEPS_W:
        p_w = step * 10 ** (M.STEP_TOL_DB / 10)
        lim = M.w_to_dbm(M.limit_97307e_w(p_w))
        legal = max(legal, M.w_to_dbm(p_w) + M.pa_harmonic_dbc(alt, n, step) - lim)
    target = M.pa_harmonic_dbc(alt, n, 5.0) + M.TARGET_DBC_5W
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
                label=f"{alt}: needed for 97.307(e) 25 uW (worst step)" if label else None)
        ax.plot(xs, tgt, ls="none", marker=mk, ms=6, mfc=INK2, mec=INK2,
                label=f"{alt}: needed for 60 dBc target at 5 W" if label else None)
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


def do_mc(run: str):
    out = outdir(run)
    deck = out / f"lpf_{run}.cir"
    screen_note = None
    if run in ("r6", "r7"):
        import retune_screen as RS
        kind = MC_KIND[run][0]
        coils = RS.COILS_1812 if kind == "1812" else [x * 1e-9 for x in range(50, 92, 2)]
        ranked = RS.screen(kind, coils)
        fmtv = lambda v: [round(x * 1e12) if i % 2 == 0 else round(x * 1e9) for i, x in enumerate(v)]
        scr = {"criterion": "worst corner (all L, C at -tol and +tol; every capacitor ESR 0.4 ohm) passband loss, "
                            "among symmetric E24 capacitor and coil sets with at least 45 dB at 288 to 296 MHz and 40 dB "
                            "at 432 to 444 MHz at the -tol corner (ABCD model, no coupling or leakage)",
               "bom": {"values_pF_nH": fmtv(M.BOM), **RS.evaluate(kind, M.BOM)},
               "chosen": {"values_pF_nH": fmtv(M.RETUNE), **RS.evaluate(kind, M.RETUNE)},
               "top10": [{"values_pF_nH": fmtv(v), **e} for _, v, e in ranked[:10]], "n_passing": len(ranked)}
        (out / "retune_screen.json").write_text(json.dumps(scr, indent=2))
        screen_note = scr
    insts = write_mc_deck(deck, run)
    prov = run_ltspice(deck)
    raw = RawRead(str(out / f"lpf_{run}.raw"))
    steps = raw.get_steps()
    tr = raw.get_trace("V(out_m)")
    f = np.abs(raw.get_trace("frequency").get_wave(steps[0]))
    waves = np.array([tr.get_wave(s) for s in steps])
    vin = raw.get_trace("V(in_m)")
    s11 = np.array([vin.get_wave(s) - 1 for s in steps])
    assert waves.shape[0] == len(insts), (waves.shape, len(insts))
    per = [metrics(f, w, r) for w, r in zip(waves, s11)]
    # log cross-checks: the L4 value echoed by .meas equals the CSV for every step, and the .meas S21 at
    # 288 MHz equals the value read from the .raw (two readers of the same run)
    meas = parse_meas(out / f"lpf_{run}.log")
    echo = [10 ** (v / 20) for v in meas["echo_l4"]]
    echo_ok = len(echo) == len(insts) and all(abs(e - i["L4L"]) / i["L4L"] < 1e-6 for e, i in zip(echo, insts))
    k288 = int(np.argmin(np.abs(f - 288e6)))
    raw288 = db(waves[:, k288])
    xcheck_ok = len(meas["s21_288"]) == len(insts) and float(np.max(np.abs(np.array(meas["s21_288"]) - raw288))) < 1e-3
    echo_ok = echo_ok and xcheck_ok
    keys = ["il_max_dB", "il_diss_max_dB", "rl_min_dB"] + [f"att_{n}f_dB" for n in M.HARMONICS] + [f"att_{n}_dB" for n, *_ in M.REQ_TX]
    agg = {}
    for k in keys:
        vals = np.array([p[k] for p in per])
        agg[k] = {"min": float(vals.min()), "p01": float(np.percentile(vals, 1)), "median": float(np.median(vals)),
                  "p99": float(np.percentile(vals, 99)), "max": float(vals.max()),
                  "corner_low": float(vals[0]), "corner_high": float(vals[1])}
    passes = [all(req_pass(p).values()) for p in per]
    worst = {"il_max_dB": agg["il_max_dB"]["max"]}
    worst.update({k: agg[k]["min"] for k in keys if k.startswith("att_")})
    verdict = {name: worst[f"att_{name}_dB"] >= lim for name, _, _, lim in M.REQ_TX}
    verdict["IL"] = worst["il_max_dB"] <= M.IL_MAX_DB
    res = {"run": RUNS[run], "label": MC_KIND[run][2], "n_runs": len(insts), "seed": SEEDS[run],
           "ltspice": prov.splitlines(), "echo_check_L4_pass": echo_ok, "stats": agg, "worst": worst,
           "verdict_worst_case": verdict, "yield_all_pass": float(np.mean(passes)),
           "scripts_sha256": snapshot_scripts(out)}
    (out / "result.json").write_text(json.dumps(res, indent=2))

    # Plot: MC spread wide
    fig, ax = plt.subplots(figsize=(10, 6.8))
    overlay_requirements(ax)
    c = {"r2": COL["1812"], "r3": COL["air"], "r4": COL["air_al"], "r6": "#4a3aa7", "r7": "#e87ba4"}[run]
    d = db(waves)
    for w in d[2:]:
        ax.plot(f / 1e6, w, color=c, lw=0.4, alpha=0.12)
    ax.plot(f / 1e6, d.max(axis=0), color=c, lw=1.6, label=f"{MC_KIND[run][2]}: envelope of {len(insts)} runs")
    ax.plot(f / 1e6, d.min(axis=0), color=c, lw=1.6)
    ax.set_xlim(0, 1600)
    ax.set_ylim(-140, 8)
    ax.set_xlabel("Frequency (MHz)")
    ax.set_ylabel("S21 (dB)")
    ax.set_title(f"Monte Carlo S21 spread, {MC_KIND[run][2]} (run {run})", color=INK)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.11), fontsize=7.5, ncol=2)
    fig.tight_layout()
    fig.savefig(out / "s21_mc_wide.png", dpi=150)
    plt.close(fig)

    # Plot: MC passband
    fig, ax = plt.subplots(figsize=(8, 4.5))
    for w in d[2:]:
        ax.plot(f / 1e6, -w, color=c, lw=0.5, alpha=0.2)
    ax.plot(f / 1e6, -d[0], color=INK2, lw=1.2, ls="-.", label="corner: all L, C at -tol")
    ax.plot(f / 1e6, -d[1], color=INK2, lw=1.2, ls=":", label="corner: all L, C at +tol")
    ax.axvspan(144, 148, color=GRID, lw=0)
    ax.plot([144, 148], [M.IL_MAX_DB] * 2, color=INK, lw=1.6, ls="--", label="0.5 dB goal, 144 to 148 MHz")
    ax.set_xlim(100, 200)
    ax.set_ylim(0, 3)
    ax.set_xlabel("Frequency (MHz)")
    ax.set_ylabel("Insertion loss, -S21 (dB)")
    ax.set_title(f"Monte Carlo passband loss, {MC_KIND[run][2]} (run {run})", color=INK)
    ax.legend(loc="upper left", fontsize=7.5)
    fig.tight_layout()
    fig.savefig(out / "il_mc_passband.png", dpi=150)
    plt.close(fig)

    # Plot: histograms against the limits
    fig, axs = plt.subplots(1, 4, figsize=(12, 3.4))
    items = [("att_2f_dB", "Min S21 atten. 288-296 MHz (dB)", 40.0, "ge"),
             ("att_3f_dB", "Min atten. 432-444 MHz (dB)", 35.0, "ge"),
             ("att_REQ-TX-011_dB", "Min atten. 576-1500 MHz (dB)", 40.0, "ge"),
             ("il_max_dB", "Max IL 144-148 MHz (dB)", M.IL_MAX_DB, "le")]
    for axh, (k, lab, lim, sense) in zip(axs, items):
        vals = np.array([p[k] for p in per])
        axh.hist(vals, bins=30, color=c, edgecolor="#fcfcfb", linewidth=0.5)
        axh.axvline(lim, color=INK, ls="--", lw=1.6)
        axh.text(0.03, 0.97, f"limit {'<=' if sense == 'le' else '>='} {lim:g} (dashed)", transform=axh.transAxes,
                 color=INK, fontsize=7, va="top", bbox=dict(facecolor="#fcfcfb", edgecolor="none", pad=1.5))
        axh.set_xlabel(lab, fontsize=8)
        axh.set_ylabel("runs")
    fig.suptitle(f"Monte Carlo distributions, {MC_KIND[run][2]} (run {run}, {len(insts)} runs)", color=INK)
    fig.tight_layout()
    fig.savefig(out / "mc_histograms.png", dpi=150)
    plt.close(fig)

    L = [f"# Run {res['run']}: Monte Carlo, {res['label']}", "",
         f"Deck `lpf_{run}.cir` ({len(insts)} steps: run 1 all L and C at -tol, run 2 at +tol, "
         f"runs 3 to {len(insts)} uniform random, seed {SEEDS[run]}; every value in `mc_values.csv`). "
         "LTspice AC 2 to 1600 MHz in 2 MHz steps.", "",
         f"Log cross-checks (L4 value echoed by .meas equals the CSV for every step; .meas S21 at 288 MHz equals "
         f"the .raw value within 0.001 dB for every step): "
         f"**{'PASS' if echo_ok else 'FAIL'}**.", "",
         "| Quantity | Worst | 1st pct | Median | Corner -tol | Corner +tol | Limit | Verdict |", "|---|---|---|---|---|---|---|---|"]
    rows = [("il_max_dB", "IL max 144-148 MHz (dB)", M.IL_MAX_DB, "le", "IL"),
            ("att_2f_dB", "Min atten. 288-296 MHz (dB)", 40.0, "ge", "REQ-TX-009"),
            ("att_3f_dB", "Min atten. 432-444 MHz (dB)", 35.0, "ge", "REQ-TX-010"),
            ("att_REQ-TX-011_dB", "Min atten. 576-1500 MHz (dB)", 40.0, "ge", "REQ-TX-011")]
    for k, lab, lim, sense, key in rows:
        s = agg[k]
        w = s["max"] if sense == "le" else s["min"]
        p = s["p99"] if sense == "le" else s["p01"]
        L.append(f"| {lab} | {w:.2f} | {p:.2f} | {s['median']:.2f} | {s['corner_low']:.2f} | {s['corner_high']:.2f} | "
                 f"{'<=' if sense == 'le' else '>='} {lim:g} | {'PASS' if verdict[key] else 'FAIL'} |")
    L += ["", f"Dissipative part of the loss (|S21|^2 / (1 - |S11|^2), max over 144 to 148 MHz): worst "
          f"{agg['il_diss_max_dB']['max']:.2f} dB, median {agg['il_diss_max_dB']['median']:.2f} dB; the rest of the "
          "insertion loss is mismatch from detuning.", "",
          f"Input return loss over 144 to 148 MHz: worst {agg['rl_min_dB']['min']:.1f} dB, median "
          f"{agg['rl_min_dB']['median']:.1f} dB (reported, no criterion).", "",
          "Worst attenuation per harmonic band (dB): " +
          ", ".join(f"{n}f {agg[f'att_{n}f_dB']['min']:.1f}" for n in M.HARMONICS), "",
          f"Yield (runs meeting all four criteria): {100 * res['yield_all_pass']:.1f} %.", "",
          "Plots: `s21_mc_wide.png`, `il_mc_passband.png`, `mc_histograms.png`.", ""]
    if screen_note:
        L += ["Value screen (`retune_screen.json`, ABCD model, stacked worst corner with every ESR at 0.4 ohm): BOM "
              f"{screen_note['bom']['values_pF_nH']} gives {screen_note['bom']['il_worst']:.2f} dB, the chosen set "
              f"{screen_note['chosen']['values_pF_nH']} gives {screen_note['chosen']['il_worst']:.2f} dB with "
              f"{screen_note['chosen']['att2_lo']:.1f} dB at 2f; best of {screen_note['n_passing']} passing sets "
              f"{screen_note['top10'][0]['values_pF_nH']} gives {screen_note['top10'][0]['il_worst']:.2f} dB.", ""]
    (out / "result.md").write_text("\n".join(L))
    return res


def do_r5():
    out = outdir("r5")
    builds = {}
    for run in ("r2", "r3", "r4", "r6", "r7"):
        j = json.loads((HERE / "results" / RUNS[run] / "result.json").read_text())
        builds[run] = {"label": j["label"], "att": {n: j["stats"][f"att_{n}f_dB"]["min"] for n in M.HARMONICS},
                       "il": j["stats"]["il_max_dB"]["max"]}
    res = {"run": RUNS["r5"], "inputs": {r: RUNS[r] for r in builds}, "pa_inputs": M.PA_HARMONICS, "results": {}}
    for alt in ("A5", "A4"):
        res["results"][alt] = {}
        for run, b in builds.items():
            rows, ok_legal, ok_target = [], True, True
            for n in M.HARMONICS:
                a = b["att"][n]
                for step in M.POWER_STEPS_W:
                    p_w = step * 10 ** (M.STEP_TOL_DB / 10)
                    p_dbm = M.w_to_dbm(p_w)
                    h = M.pa_harmonic_dbc(alt, n, step)
                    spur = p_dbm + h - a
                    lim = M.w_to_dbm(M.limit_97307e_w(p_w))
                    rows.append({"n": n, "step_W": step, "P_dBm": p_dbm, "H_dBc": h, "A_dB": a, "spur_dBm": spur,
                                 "limit_dBm": lim, "margin_dB": lim - spur})
                    ok_legal &= spur <= lim
                # 60 dBc target at the 5 W step (relative)
                rel = M.pa_harmonic_dbc(alt, n, 5.0) - a
                ok_target &= rel <= -M.TARGET_DBC_5W
                rows[-1]["rel_dBc_5W"] = rel
            # keying ramp: every instantaneous level from 1 mW to 6.3 W, back-off ratios below 5 W
            ramp_margin = 1e9
            for p_w in np.logspace(-3, np.log10(6.3), 400):
                for n in M.HARMONICS:
                    h = M.pa_harmonic_dbc(alt, n, 5.0 if p_w >= 5.0 else 0.5)
                    spur = M.w_to_dbm(p_w) + h - b["att"][n]
                    ramp_margin = min(ramp_margin, M.w_to_dbm(M.limit_97307e_w(p_w)) - spur)
            min_legal = min(r["margin_dB"] for r in rows)
            min_target = min(-M.TARGET_DBC_5W - r["rel_dBc_5W"] for r in rows if "rel_dBc_5W" in r)
            res["results"][alt][run] = {"build": b["label"], "rows": rows, "legal_pass": bool(ok_legal),
                                        "legal_min_margin_dB": min_legal, "target60_pass": bool(ok_target),
                                        "target60_min_margin_dB": min_target, "ramp_min_margin_dB": ramp_margin,
                                        "il_worst_dB": b["il"]}
    res["scripts_sha256"] = snapshot_scripts(out)
    (out / "result.json").write_text(json.dumps(res, indent=2))

    # Plot: spur at the antenna per harmonic; row 1 the 5 W step, row 2 the worst of the 0.5, 1 and 2 W steps
    fig, axs = plt.subplots(2, 2, figsize=(12, 8.6), sharey=True, sharex=True)
    cols = {"r2": COL["1812"], "r3": COL["air"], "r4": COL["air_al"], "r6": "#4a3aa7", "r7": "#e87ba4"}
    offs = {"r2": -0.28, "r3": -0.14, "r4": 0.0, "r6": 0.14, "r7": 0.28}
    for col, alt in enumerate(("A5", "A4")):
        for row, steps in enumerate(([5.0], [0.5, 1.0, 2.0])):
            ax = axs[row, col]
            for run in builds:
                rows = [r for r in res["results"][alt][run]["rows"] if r["step_W"] in steps]
                xs, ys = [], []
                for n in M.HARMONICS:
                    worst = max((r for r in rows if r["n"] == n), key=lambda r: r["spur_dBm"] - r["limit_dBm"])
                    xs.append(n + offs[run])
                    ys.append(worst["spur_dBm"])
                ax.plot(xs, ys, ls="none", marker="o", ms=6, color=cols[run], label=builds[run]["label"])
            ax.axhline(M.w_to_dbm(25e-6), color=INK, ls="--", lw=1.6)
            ax.text(10.45, M.w_to_dbm(25e-6) + 1, "97.307(e): 25 uW (-16 dBm)", ha="right", fontsize=7.5, color=INK)
            if row == 0:
                ax.axhline(M.w_to_dbm(5.0 * 10 ** 0.1) - M.TARGET_DBC_5W, color=INK2, ls=":", lw=1.4)
                ax.text(10.45, M.w_to_dbm(5.0 * 10 ** 0.1) - M.TARGET_DBC_5W - 3.5,
                        "REQ-SYS-018: 60 dBc below 6.3 W (-22 dBm)", ha="right", fontsize=7.5, color=INK2)
            ax.set_xticks(M.HARMONICS)
            ax.set_xticklabels([f"{n}f" for n in M.HARMONICS])
            ax.set_xlim(1.5, 10.5)
            ax.set_ylim(-95, -10)
            ax.set_title(f"{M.PA_HARMONICS[alt]['name']}: " + ("5 W step +1 dB (6.3 W)" if row == 0 else
                         "worst of the 0.5, 1, 2 W steps +1 dB"), color=INK, fontsize=9)
            if col == 0:
                ax.set_ylabel("Harmonic at the antenna port (dBm)")
            if row == 1:
                ax.set_xlabel("Harmonic, worst Monte Carlo filter of each build")
    h, lab = axs[0, 0].get_legend_handles_labels()
    fig.legend(h, lab, loc="lower center", ncol=3, fontsize=8)
    fig.suptitle("Harmonic budget: PA harmonic level minus worst-case LPF attenuation (run r5)", color=INK)
    fig.tight_layout(rect=(0, 0.07, 1, 1))
    fig.savefig(out / "harmonic_budget.png", dpi=150)
    plt.close(fig)

    L = [f"# Run {res['run']}: harmonic budget per finalist", "",
         "Spur at the antenna = carrier at the step +1 dB + PA harmonic ratio - worst Monte Carlo LPF attenuation "
         "in the harmonic band (runs r2 to r4). Limit: 47 CFR 97.307(e) for 25 W or less: at most 25 uW, at least "
         "40 dB below the carrier, need not be below 10 uW; 25 uW binds at every step (0.5 to 6.3 W). Target: "
         "REQ-SYS-018 60 dBc at the 5 W step. Ramp: every instantaneous level 1 mW to 6.3 W.", "",
         "| Finalist | Filter build | 97.307(e) all steps | Min margin (dB) | Ramp min margin (dB) | 60 dBc at 5 W | Min margin (dB) |",
         "|---|---|---|---|---|---|---|"]
    for alt in ("A5", "A4"):
        for run in builds:
            r = res["results"][alt][run]
            L.append(f"| {alt} | {r['build']} | {'PASS' if r['legal_pass'] else 'FAIL'} | {r['legal_min_margin_dB']:.1f} | "
                     f"{r['ramp_min_margin_dB']:.1f} | {'PASS' if r['target60_pass'] else 'FAIL'} | {r['target60_min_margin_dB']:.1f} |")
    L += ["", "PA harmonic inputs (at the PA output): A5 2f -25 dBc, 3f and above -30 dBc at the 5 W step "
          "(RA07M1317M datasheet maxima at 6 W; 4f and above estimated equal to 3f); at 0.5, 1 and 2 W 2f -17 dBc and "
          "3f and above -25 dBc (estimates). A4 2f -15 dBc, 3f and above -20 dBc at every step (estimate; no vendor data).",
          "", "Plot: `harmonic_budget.png`.", ""]
    (out / "result.md").write_text("\n".join(L))
    return res


if __name__ == "__main__":
    which = sys.argv[1:] or ["all"]
    if which == ["all"]:
        which = ["r1", "r2", "r3", "r4", "r6", "r7", "r5"]
    for w in which:
        r = do_r1() if w == "r1" else do_r5() if w == "r5" else do_mc(w)
        print(f"{w}: done -> {RUNS[w]}")
