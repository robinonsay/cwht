#!/usr/bin/env python3
"""TS-012 WP-PDR-21 pre-order item: PA drive window and output power at the SMA, both finalists.

A4: Si5351A CLK1 -> 3-pole drive LPF -> 12 dB pad -> GVA-84+ (near its P1dB) -> AFT05MS004N (NXP 136-174 MHz
    reference circuit, 50 ohm input) -> output LPF and G5V-2 relay -> SMA.
A5: Si5351A CLK1 -> 3-pole drive LPF -> 18 dB pad -> GVA-84+ -> 3 dB pad -> RA07M1317M module -> output LPF
    and G5V-2 relay -> SMA.

Usage (repo root, repo venv):
    .venv/bin/python hardware/sim/tx-pa/run_pa.py all      # every run below, in order
    .venv/bin/python hardware/sim/tx-pa/run_pa.py d1|d2|d3|p1|p2|s1

Runs (each writes hardware/sim/tx-pa/results/<run-id>/: the deck, the LTspice .log and .raw, result.json and
result.md with the numbers and pass/fail, PNG plots with the limits overlaid, and a copy of this script):
    d1  GVA-84+ behavioural model check (sine power sweep; fitted P1dB and P3dB against the datasheet)
    d2  A5 drive chain, 270 corners (transient; fundamental and 3f by DFT of the .raw)
    d3  A4 drive chain, 270 corners
    p1  A5 output power at the SMA versus pack voltage (DC sweep with behavioural module, drain feed and bus load)
    p2  A4 output power at the SMA versus pack voltage
    p3  A5 output power with the drive range a select-on-test pad leaves (sensitivity for the closure path)
    s1  summary plots (Pin at the PA and Pout at the SMA versus pack voltage, both finalists) and verdicts

LTspice runs only through tools/ltspice-batch.sh (ACC-LTSPICE-001). The datasheet curves are read from
hardware/sim/tx-pa/data/ (made by digitize_ra07.py and digitize_aft05.py). Every value marked "est." in
the tables below is an estimate, not a datasheet or measured value.
"""
from __future__ import annotations

import hashlib
import json
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
REPO = HERE.parents[2]
BATCH = REPO / "tools" / "ltspice-batch.sh"
DATA = HERE / "data"
DATE = "2026-09-28"
RUNS = {
    "d1": f"{DATE}-d1-gva-model",
    "d2": f"{DATE}-d2-drive-a5",
    "d3": f"{DATE}-d3-drive-a4",
    "p1": f"{DATE}-p1-power-a5",
    "p2": f"{DATE}-p2-power-a4",
    "p3": f"{DATE}-p3-power-a5-sot",
    "s1": f"{DATE}-s1-summary",
}

# ---------------------------------------------------------------- inputs (sources in the README and record)
# Si5351A CLK1 (Skyworks Si5351-B Rev. 1.3): ZO 50 ohm typ (3.3 V VDDO, high drive); tr/tf 20-80 % 1 ns typ,
# 1.5 ns max (CL 5 pF); duty 45 to 55 % below 160 MHz; VDDO 3.0 to 3.6 V allowed. 25 ohm is the TS-012 corner.
SRC_CASES = [  # (label, VDDO, tr 20-80 %, duty)
    ("low", 3.2, 1.5e-9, 0.45),   # VDDO 3.2 V: Adafruit module LDO -3 % (est.)
    ("nom", 3.3, 1.0e-9, 0.50),
    ("high", 3.4, 0.5e-9, 0.50),  # VDDO +3 % (est.); 0.5 ns: faster than typical into a resistive load (est.)
]
RSRC = [25.0, 50.0]
FREQS = [144e6, 146e6, 148e6]
# GVA-84+ (Mini-Circuits Rev. F): gain at 0.1 GHz 22.9 min, 24.1 typ, 25.3 max; TS-012 corners 22.5 and 25.0.
GAINS = [22.5, 22.9, 24.1, 25.0, 25.3]
# P1dB at 0.1 GHz +19.4 min, +20.4 typ; Psat (3 dB compression) +21.7 typ. "high" = typ + 1 dB (est.).
P1DB_SETS = [("min", 19.4, 20.7), ("typ", 20.4, 21.7), ("high", 21.4, 22.7)]
GVA_ABSMAX_IN_DBM = 13.0
# Drive LPF (3-pole C-L-C, fc about 180 MHz): 18 pF C0G 1206 (ESR 0.1 ohm, ESL plus via 1 nH, est.);
# 82 nH Coilcraft 1812SMS class (Q 100 at 146 MHz -> 0.75 ohm, SRF about 1.2 GHz -> 0.21 pF, est.).
# Divider tap on CLK1 (100 pF plus 74LVC1G80 input): 5 pF (est.).
PADS = {  # E24 1 % pi pads (shunt, series, shunt)
    "a5_in": (62.0, 200.0, 62.0),   # 18 dB design (64.4 / 195.4 ideal)
    "a5_out": (300.0, 18.0, 300.0),  # 3 dB design (292.4 / 17.6 ideal)
    "a4_in": (82.0, 91.0, 82.0),     # 12 dB design (83.5 / 93.2 ideal): GVA near P1dB at the nominal corner
}
# Rapp limiter on the instantaneous voltage, fitted (numerically, describing function) so that the fundamental
# output compresses 1 dB and 3 dB at the P1dB and Psat values above; smoothness p is the same for all sets.
RAPP_P = 2.7046
RAPP_VSAT = {"min": 2.9921, "typ": 3.3572, "high": 3.7669}  # volts peak at the 50 ohm load

# Windows and limits
A5_PIN_MIN_MW, A5_PIN_MAX_MW = 10.0, 30.0   # RA07M1317M stability conditions (Pin 10 to 30 mW) and 30 mW maximum rating
A4_PIN_OVERDRIVE_W = 0.2                     # AFT05 Table 9 ruggedness test drive (3 dB overdrive); not a rating
H3_MIN_DBC = 25.0                            # TS-012: 3f at the GVA input at least 25 dB below the fundamental
REQ012_LO, REQ012_NOM, REQ012_HI = 3.972, 5.0, 6.295  # REQ-SYS-012 5 W +/-1 dB at the SMA (TC-SYS-011 bounds)
A5_MOD_STAB_W, A5_MOD_MAX_W = 8.0, 10.0      # module stability guarantee (Pout up to 8 W) and maximum rating
PACK = (6.4, 8.4)

# Power path (TS-012 section 7.3): pack plus drain feed 0.26 to 0.45 ohm (cells, AO3400A pair, MF-R300,
# holders, DMP3099L pair, chokes; mix of datasheet bounds and est.); 5 V bus from the pack at key-down 0.25 A
# (GVA-84+ 0.108 A typ, G5V-2 coil 0.1 A, Pico and op-amps; est., TS-012 used 0.2 A).
RFEED = [0.26, 0.35, 0.45]
IBUS = 0.25
LOSS_DB = [0.4, 0.5, 0.6]  # output LPF 0.3 to 0.5 dB (TS-012 allocation 0.4, criterion max 0.5) plus relay 0.1 dB (est.)
# A5 module: total efficiency 0.60 typ (datasheet page 4 graph read: 5.85 W at 6.0 V and 1.63 A; 10.0 W at
# 8.0 V and 2.01 A), 0.45 min (datasheet, at 6 W, 7.2 V); guaranteed Pout 6.5 W min at 7.2 V, VGG 3.5 V,
# Pin 20 mW. VGG clamp 3.08 V lowest (TS-012 revision 4: LM2940 4.75 V x 0.6493).
A5_ETA = [0.45, 0.60]
A5_POUT_MIN_72 = 6.5
A5_VGG_CLAMP_LO = 3.08
# A4 AFT05MS004N: drain efficiency 0.67 at Pin 0.1 W, 146 MHz (Figure 13 read, 135 MHz 62 % and 155 MHz 73 %);
# 0.55 low (est.). Output scales as VDD^n from the 7.5 V curve, n 1.8 / 2.0 / 2.3 (est.: the RA07M1317M
# curve gives 1.86 between 6.0 and 8.4 V). Hand-derived match on 0.8 mm FR4 with wound coils: 0 / 0.25 / 0.5 dB
# more loss than the NXP reference circuit (est.).
A4_ETA = [0.55, 0.67]
A4_N = [1.8, 2.0, 2.3]
A4_LMATCH = [0.0, 0.25, 0.5]

# Select-on-test (SOT) drive pad for A5 (REQ-SYS-144 delta admits "drive pad selection" at build): the pad is
# picked from 1 dB steps after reading the power into a 50 ohm load in place of the module; residual terms:
SOT_STEP_DB = 1.0          # pad step (E24 pi-pad sets at 1 dB steps)
SOT_MEAS_DB = 1.0          # power reading at about 17 mW: diode probe and multimeter +/-1 dB (est.)
SOT_DRIFT_DB = 0.3         # temperature and supply drift of the Si5351 edge and the GVA gain (est.)
SOT_TARGET_MW = 17.3       # geometric centre of 10 to 30 mW

INK, INK2, GRID, SURF = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
COL = {"a5": "#2a78d6", "a4": "#eb6834", "aux": "#4a3aa7", "ok": "#1baf7a"}
plt.rcParams.update({"font.size": 9, "axes.edgecolor": INK2, "axes.labelcolor": INK, "xtick.color": INK2,
                     "ytick.color": INK2, "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.6,
                     "figure.facecolor": SURF, "axes.facecolor": SURF, "legend.frameon": False,
                     "axes.titlesize": 10})


# ---------------------------------------------------------------- helpers
def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def rundir(key: str) -> Path:
    d = HERE / "results" / RUNS[key]
    d.mkdir(parents=True, exist_ok=True)
    return d


def run_ltspice(deck: Path, out: Path, timeout: int = 1200) -> dict:
    """Run the deck through tools/ltspice-batch.sh. With CWHT_PA_REPLOT=1 and an earlier run of the identical
    deck in out/ (same SHA-256 recorded in result.json), the earlier .raw is re-read instead (plots only)."""
    import os
    old = out / "result.json"
    if os.environ.get("CWHT_PA_REPLOT") == "1" and old.exists() and (out / (deck.stem + ".raw")).exists():
        prev = json.loads(old.read_text()).get("ltspice", {})
        if prev.get("deck_sha256") == sha(deck):
            return prev
    cmd = [str(BATCH), "-t", str(timeout), "-o", str(out), "-b", str(deck)]
    p = subprocess.run(cmd, capture_output=True, text=True)
    prov = [ln for ln in p.stderr.splitlines() if "ltspice-batch" in ln]
    if p.returncode != 0:
        sys.stderr.write(p.stdout + p.stderr)
        raise SystemExit(f"LTspice batch failed ({p.returncode}) for {deck.name}")
    log = out / (deck.stem + ".log")
    first = log.read_text(errors="replace").splitlines()[0] if log.exists() else ""
    return {"deck": deck.name, "deck_sha256": sha(deck), "exit": p.returncode, "log_first_line": first,
            "wrapper_provenance": prov[-3:]}


def copy_inputs(out: Path, decks: list[Path]):
    shutil.copy2(Path(__file__), out / Path(__file__).name)
    for d in decks:
        if d.parent != out:
            shutil.copy2(d, out / d.name)


def load_curve(name: str) -> np.ndarray:
    return np.loadtxt(DATA / f"{name}.csv", delimiter=",", skiprows=1)


def resample(curve: np.ndarray, xs: np.ndarray, win: float) -> np.ndarray:
    """Local mean of the digitized points within +/-win of each x (removes pixel stair steps)."""
    out = []
    for x in xs:
        m = np.abs(curve[:, 0] - x) <= win
        out.append(curve[m, 1].mean() if m.any() else np.interp(x, curve[:, 0], curve[:, 1]))
    return np.array(out)


def table_expr(var: str, xs, ys, fmt="{:.4g}") -> str:
    pairs = ",".join(f"{fmt.format(x)},{fmt.format(y)}" for x, y in zip(xs, ys))
    return f"table({var},{pairs})"


def dbm(p_w):
    return 10 * np.log10(np.asarray(p_w) / 1e-3)


def pad_loss_db(sh1, se, sh2, z0=50.0):
    """Insertion loss (dB) of a pi pad between z0 terminations (ABCD)."""
    def shunt(r):
        return np.array([[1, 0], [1 / r, 1]], dtype=complex)
    ser = np.array([[1, se], [0, 1]], dtype=complex)
    a, b, c, d = (shunt(sh1) @ ser @ shunt(sh2)).ravel()
    s21 = 2 / (a + b / z0 + c * z0 + d)
    return -20 * np.log10(abs(s21))


def drive_corners():
    """Mixed-radix order used in the drive decks: isrc fastest, then freq, P1dB set, gain, source R."""
    out = []
    for irs, rs in enumerate(RSRC):
        for ig, g in enumerate(GAINS):
            for ip, (pl, _, _) in enumerate(P1DB_SETS):
                for ifr, f in enumerate(FREQS):
                    for isrc, (sl, vddo, tr, duty) in enumerate(SRC_CASES):
                        out.append(dict(rsrc=rs, gain=g, p1db=pl, freq=f, src=sl, vddo=vddo, tr=tr, duty=duty))
    return out


# ---------------------------------------------------------------- d1: GVA-84+ model check
def deck_d1(out: Path) -> Path:
    txt = f"""* gva_check.cir: GVA-84+ behavioural model check (cwht WP-PDR-21, hardware/sim/tx-pa, run {RUNS['d1']})
* A 146 MHz sine of available power pin (dBm) from a 50 ohm source drives the model: 50 ohm input, Rapp
* limiter on the instantaneous voltage (p = {RAPP_P}, Vsat per P1dB set), 50 ohm source resistance, 50 ohm load.
* Gain 24.1 dB (datasheet typ at 0.1 GHz). The checker reads the fundamental at the load by DFT of the .raw and
* compares the 1 dB and 3 dB compression points with the datasheet (Rev. F: P1dB +20.4 typ / +19.4 min dBm,
* Psat at 3 dB compression +21.7 typ dBm) and the est. high set (+21.4 / +22.7 dBm).
.param pin=-20
.param iv=1
.step param pin -20 4 1
.step param iv 0 2 1
.param vsat=table(iv,0,{RAPP_VSAT['min']},1,{RAPP_VSAT['typ']},2,{RAPP_VSAT['high']})
.param G=pow(10,24.1/20)
.param p={RAPP_P}
V1 src 0 SIN(0 {{sqrt(8*50*1e-3*pow(10,pin/10))}} 146Meg)
Rs src gin 50
Rgin gin 0 50
Bg gs 0 V=2*{{G}}*V(gin)/pow(1+pow(abs({{G}}*V(gin))/{{vsat}},2*{{p}}),1/(2*{{p}}))
Rgo gs gout 50
Rl gout 0 50
.tran 0 60n 39n 5p
.options plotwinsize=0
.save V(gin) V(gout)
.end
"""
    p = out / "gva_check.cir"
    p.write_text(txt)
    return p


def dft_amp(t, v, f, harmonic=1, periods=3):
    """Amplitude of the given harmonic over the last whole periods (uniform resampling)."""
    T = 1 / f
    t1 = t[-1]
    t0 = t1 - periods * T
    n = periods * 1024
    tt = np.linspace(t0, t1, n, endpoint=False)
    vv = np.interp(tt, t, v)
    ph = np.exp(-2j * np.pi * harmonic * f * (tt - t0))
    return 2 * abs(np.mean(vv * ph))


def run_d1():
    out = rundir("d1")
    deck = deck_d1(out)
    prov = run_ltspice(deck, out)
    raw = RawRead(str(out / "gva_check.raw"))
    steps = raw.get_steps()
    res = {s: [] for s in RAPP_VSAT}
    pins = np.arange(-20, 5, 1.0)
    for i, _ in enumerate(steps):
        t = np.abs(raw.get_trace(raw.get_trace_names()[0]).get_wave(i))
        vo = raw.get_trace("V(gout)").get_wave(i)
        a = dft_amp(t, vo, 146e6)
        pin = pins[i % len(pins)]
        iv = i // len(pins)
        res[list(RAPP_VSAT)[iv]].append((pin, dbm(a * a / 100)))
    rows, checks = [], []
    fig, ax = plt.subplots(figsize=(6.4, 4.0))
    for k, (name, p1, p3) in enumerate(P1DB_SETS):
        arr = np.array(res[name])
        gain = arr[:, 1] - arr[:, 0]
        comp = 24.1 - gain
        pout = arr[:, 1]
        p1_sim = float(np.interp(1.0, comp, pout))
        p3_sim = float(np.interp(3.0, comp, pout))
        ok = abs(p1_sim - p1) <= 0.1 and abs(p3_sim - p3) <= 0.15
        checks.append(ok)
        rows.append(dict(set=name, p1db_target=p1, p1db_sim=round(p1_sim, 2), p3db_target=p3,
                         p3db_sim=round(p3_sim, 2), pass_=ok))
        ax.plot(pout, gain, color=[COL["a4"], COL["a5"], COL["aux"]][k], lw=2, label=f"P1dB set {name}")
        ax.plot([p1], [23.1], "o", ms=8, mfc="none", mec=[COL["a4"], COL["a5"], COL["aux"]][k], mew=2)
    ax.axhline(23.1, color=INK, lw=1, ls="--")
    ax.text(0.5, 23.15, "1 dB compression (23.1 dB)", color=INK, fontsize=8, va="bottom")
    ax.axhline(21.1, color=INK2, lw=1, ls=":")
    ax.text(0.5, 21.15, "3 dB compression (21.1 dB)", color=INK2, fontsize=8, va="bottom")
    for x, lab in ((19.4, "P1dB min 19.4"), (20.4, "P1dB typ 20.4"), (21.7, "Psat typ 21.7")):
        ax.axvline(x, color=INK2, lw=0.8, ls="-.")
        ax.text(x, 19.3, lab, rotation=90, fontsize=7, color=INK2, ha="right", va="bottom")
    ax.set_xlabel("GVA-84+ output power, fundamental (dBm)")
    ax.set_ylabel("Gain (dB)")
    ax.set_title("GVA-84+ behavioural model in LTspice: gain versus output power, 146 MHz\n"
                 "circles: datasheet P1dB (min, typ) and est. high; model gain 24.1 dB")
    ax.set_xlim(0, 24)
    ax.set_ylim(19, 25)
    ax.legend(loc="lower left")
    fig.tight_layout()
    fig.savefig(out / "gva_compression.png", dpi=150)
    plt.close(fig)
    result = {"run": RUNS["d1"], "ltspice": prov, "rows": rows, "pass": all(checks)}
    (out / "result.json").write_text(json.dumps(result, indent=2))
    md = [f"# {RUNS['d1']}: GVA-84+ behavioural model check", "",
          f"Verdict: **{'PASS' if all(checks) else 'FAIL'}** (fitted 1 dB point within 0.1 dB and 3 dB point within 0.15 dB of the targets)", "",
          "| P1dB set | P1dB target (dBm) | P1dB in LTspice | P3dB target | P3dB in LTspice | Pass |", "|---|---|---|---|---|---|"]
    for r in rows:
        md.append(f"| {r['set']} | {r['p1db_target']} | {r['p1db_sim']} | {r['p3db_target']} | {r['p3db_sim']} | {'yes' if r['pass_'] else 'no'} |")
    md += ["", "Plot: `gva_compression.png`. Deck `gva_check.cir`; LTspice log `gva_check.log`, raw `gva_check.raw`.", ""]
    (out / "result.md").write_text("\n".join(md))
    copy_inputs(out, [deck])
    print("d1", "PASS" if all(checks) else "FAIL", rows)


# ---------------------------------------------------------------- d2, d3: drive chains
def deck_drive(fin: str, out: Path) -> Path:
    n = len(RSRC) * len(GAINS) * len(P1DB_SETS) * len(FREQS) * len(SRC_CASES)
    s_vddo = ",".join(f"{i},{c[1]}" for i, c in enumerate(SRC_CASES))
    s_tr = ",".join(f"{i},{c[2] / 0.6:.4g}" for i, c in enumerate(SRC_CASES))  # 0-100 % ramp = 20-80 % / 0.6
    s_duty = ",".join(f"{i},{c[3]}" for i, c in enumerate(SRC_CASES))
    s_f = ",".join(f"{i},{f:.6g}" for i, f in enumerate(FREQS))
    s_v = ",".join(f"{i},{RAPP_VSAT[s[0]]}" for i, s in enumerate(P1DB_SETS))
    s_g = ",".join(f"{i},{g}" for i, g in enumerate(GAINS))
    s_r = ",".join(f"{i},{r}" for i, r in enumerate(RSRC))
    if fin == "a5":
        a, b, c = PADS["a5_in"]
        q1, q2, q3 = PADS["a5_out"]
        chain = f"""* 18 dB input pad (E24 1 %)
Rp1 lpf 0 {a}
Rp2 lpf gin {b}
Rp3 gin 0 {c}
* GVA-84+ behavioural: 50 ohm input, Rapp limiter, 50 ohm output
Rgin gin 0 50
Bg gs 0 V=2*{{G}}*V(gin)/pow(1+pow(abs({{G}}*V(gin))/{{vsat}},2*{{p}}),1/(2*{{p}}))
Rgo gs gout 50
* 3 dB output pad (E24 1 %) and the RA07M1317M input (datasheet ZG = ZL = 50 ohm)
Rq1 gout 0 {q1}
Rq2 gout pa_in {q2}
Rq3 pa_in 0 {q3}
Rpa pa_in 0 50
"""
        title = "A5: Si5351A CLK1 -> drive LPF -> 18 dB pad -> GVA-84+ -> 3 dB pad -> RA07M1317M input (50 ohm)"
    else:
        a, b, c = PADS["a4_in"]
        chain = f"""* 12 dB input pad (E24 1 %)
Rp1 lpf 0 {a}
Rp2 lpf gin {b}
Rp3 gin 0 {c}
* GVA-84+ behavioural: 50 ohm input, Rapp limiter, 50 ohm output
Rgin gin 0 50
Bg gs 0 V=2*{{G}}*V(gin)/pow(1+pow(abs({{G}}*V(gin))/{{vsat}},2*{{p}}),1/(2*{{p}}))
Rgo gs pa_in 50
* AFT05MS004N NXP 136-174 MHz reference circuit input (50 ohm system, datasheet Table 8)
Rpa pa_in 0 50
"""
        title = "A4: Si5351A CLK1 -> drive LPF -> 12 dB pad -> GVA-84+ -> AFT05MS004N reference-circuit input (50 ohm)"
    txt = f"""* drive_{fin}.cir: {title}
* cwht WP-PDR-21 pre-order drive-window analysis, hardware/sim/tx-pa (analysis record docs/design/analysis/pa-drive-ts012.md)
* {n} corners flattened into one .step (idx): source case (VDDO, 20-80 % edge, duty) fastest, then frequency,
* GVA-84+ P1dB set, GVA-84+ gain, Si5351 output resistance. The Si5351 CLK1 is a trapezoid Thevenin source of
* VDDO swing with the DC removed (the drive path is AC coupled) behind 25 or 50 ohm. The checker takes the
* fundamental and 3rd harmonic at V(gin) and V(pa_in) by DFT of the last three periods in the .raw.
.param idx=0
.step param idx 0 {n - 1} 1
.param isrc=idx-3*floor(idx/3)
.param ifr=floor(idx/3)-3*floor(idx/9)
.param ip1=floor(idx/9)-3*floor(idx/27)
.param ig=floor(idx/27)-{len(GAINS)}*floor(idx/{27 * len(GAINS)})
.param irs=floor(idx/{27 * len(GAINS)})
.param vddo=table(isrc,{s_vddo})
.param tr=table(isrc,{s_tr})
.param duty=table(isrc,{s_duty})
.param freq=table(ifr,{s_f})
.param vsat=table(ip1,{s_v})
.param gdb=table(ig,{s_g})
.param rsrc=table(irs,{s_r})
.param T=1/freq
.param ton=duty*T-tr
.param G=pow(10,gdb/20)
.param p={RAPP_P}
V1 vs 0 PULSE({{-duty*vddo}} {{(1-duty)*vddo}} 0 {{tr}} {{tr}} {{ton}} {{T}})
Rsrc vs clk {{rsrc}}
* divider tap on CLK1 (100 pF to the 74LVC1G80 input): 5 pF (est.)
Ctap clk 0 5p
* 3-pole drive LPF: 18 pF C0G 1206 (ESR, ESL plus via est.), 82 nH 1812SMS class (Q 100, SRF 1.2 GHz est.)
C1 clk 0 18p Rser=0.1 Lser=1n
L1 clk lpf 82n Rser=0.75 Cpar=0.21p
C2 lpf 0 18p Rser=0.1 Lser=1n
{chain}.tran 0 112n 90n 10p
.options plotwinsize=0
.save V(clk) V(gin) V(pa_in)
.end
"""
    p = out / f"drive_{fin}.cir"
    p.write_text(txt)
    return p


def analyse_drive(fin: str, key: str):
    out = rundir(key)
    deck = deck_drive(fin, out)
    prov = run_ltspice(deck, out)
    raw = RawRead(str(out / f"drive_{fin}.raw"))
    corners = drive_corners()
    steps = raw.get_steps()
    assert len(steps) == len(corners), (len(steps), len(corners))
    rows = []
    for i, c in enumerate(corners):
        t = np.abs(raw.get_trace(raw.get_trace_names()[0]).get_wave(i))
        vpa = raw.get_trace("V(pa_in)").get_wave(i)
        vg = raw.get_trace("V(gin)").get_wave(i)
        vc = raw.get_trace("V(clk)").get_wave(i)
        f = c["freq"]
        a1 = dft_amp(t, vpa, f, 1)
        g1 = dft_amp(t, vg, f, 1)
        g3 = dft_amp(t, vg, f, 3)
        m = t >= t[-1] - 3 / f
        rows.append({**c, "pin_pa_w": a1 * a1 / 100, "pin_pa_dbm": float(dbm(a1 * a1 / 100)),
                     "gva_in_dbm": float(dbm(g1 * g1 / 100)), "h3_dbc_gva_in": float(20 * np.log10(g3 / g1)),
                     "gva_in_peak_v": float(np.max(np.abs(vg[m]))),
                     "clk_vpp": float(np.max(vc[m]) - np.min(vc[m]))})
    pin = np.array([r["pin_pa_w"] for r in rows])
    h3 = np.array([r["h3_dbc_gva_in"] for r in rows])
    gin = np.array([r["gva_in_dbm"] for r in rows])
    crit = [r for r in rows if r["gain"] in (22.5, 25.0) and r["src"] == "nom"]  # TS-012 criterion corners
    pcrit = np.array([r["pin_pa_w"] for r in crit])
    nominal = next(r for r in rows if r["rsrc"] == 50 and r["gain"] == 24.1 and r["p1db"] == "typ"
                   and r["freq"] == 146e6 and r["src"] == "nom")
    lo, hi = min(rows, key=lambda r: r["pin_pa_w"]), max(rows, key=lambda r: r["pin_pa_w"])
    res = {"run": RUNS[key], "finalist": fin.upper(), "ltspice": prov, "n_corners": len(rows),
           "pad_loss_db": {k: round(float(pad_loss_db(*v)), 3) for k, v in PADS.items()},
           "pin_pa_w": {"min": float(pin.min()), "nominal": nominal["pin_pa_w"], "max": float(pin.max())},
           "pin_pa_dbm": {"min": float(dbm(pin.min())), "nominal": nominal["pin_pa_dbm"], "max": float(dbm(pin.max()))},
           "pin_pa_criterion_corners_w": {"min": float(pcrit.min()), "max": float(pcrit.max())},
           "corner_min": lo, "corner_max": hi, "nominal_corner": nominal,
           "h3_dbc_gva_in_worst": float(h3.max()), "h3_pass": bool(h3.max() <= -H3_MIN_DBC),
           "gva_in_dbm_max": float(gin.max()), "gva_absmax_pass": bool(gin.max() < GVA_ABSMAX_IN_DBM),
           "clk_vpp": {"min": float(min(r["clk_vpp"] for r in rows)), "max": float(max(r["clk_vpp"] for r in rows))}}
    if fin == "a5":
        inwin = (pin >= A5_PIN_MIN_MW * 1e-3) & (pin <= A5_PIN_MAX_MW * 1e-3)
        cw = (pcrit >= A5_PIN_MIN_MW * 1e-3) & (pcrit <= A5_PIN_MAX_MW * 1e-3)
        res.update({"window_mw": [A5_PIN_MIN_MW, A5_PIN_MAX_MW], "corners_in_window": int(inwin.sum()),
                    "corners_above_30mw": int((pin > A5_PIN_MAX_MW * 1e-3).sum()),
                    "corners_below_10mw": int((pin < A5_PIN_MIN_MW * 1e-3).sum()),
                    "criterion_corners": int(len(pcrit)), "criterion_corners_in_window": int(cw.sum()),
                    "window_pass_all_corners": bool(inwin.all()), "window_pass_criterion_corners": bool(cw.all()),
                    "spread_db": float(dbm(pin.max()) - dbm(pin.min())), "window_db": float(10 * np.log10(3.0))})
        # pad needed to bring the maximum to 30 mW, and what that does to the minimum
        shift = max(0.0, float(dbm(pin.max()) - dbm(A5_PIN_MAX_MW * 1e-3)))
        res["extra_pad_db_for_30mw"] = shift
        res["min_after_extra_pad_mw"] = float(pin.min() * 10 ** (-shift / 10) * 1e3)
    else:
        res.update({"overdrive_w": A4_PIN_OVERDRIVE_W, "corners_above_overdrive": int((pin > A4_PIN_OVERDRIVE_W).sum()),
                    "overdrive_pass": bool((pin <= A4_PIN_OVERDRIVE_W).all())})
    (out / "corners.json").write_text(json.dumps(rows, indent=1))
    # plot: Pin at the PA per corner
    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    xs = np.arange(len(rows))
    colr = np.where(np.array([r["rsrc"] for r in rows]) == 25, COL["a4"], COL["a5"])
    ax.scatter(xs, pin * 1e3, s=10, c=colr, zorder=3)
    for g_i, g in enumerate(GAINS):
        for rs_i, rs in enumerate(RSRC):
            x0 = rs_i * 135 + g_i * 27
            ax.axvline(x0 - 0.5, color=GRID, lw=0.8)
    ax.set_yscale("log")
    from matplotlib.ticker import FixedLocator, NullLocator, ScalarFormatter
    box = dict(facecolor=SURF, edgecolor="none", alpha=0.85, pad=1.5)
    if fin == "a5":
        ax.axhspan(A5_PIN_MIN_MW, A5_PIN_MAX_MW, color=COL["ok"], alpha=0.08, zorder=0)
        ax.axhline(A5_PIN_MAX_MW, color=INK, lw=1.3, ls="-", label="30 mW: module maximum rating, top of the stability window")
        ax.axhline(A5_PIN_MIN_MW, color=INK, lw=1.3, ls="--", label="10 mW: bottom of the module stability window")
        ax.set_ylim(5, 60)
        ticks = [5, 6, 8, 10, 15, 20, 30, 40, 60]
    else:
        ax.axhline(A4_PIN_OVERDRIVE_W * 1e3, color=INK, lw=1.3, ls="-", label="200 mW: AFT05 ruggedness-test drive (3 dB overdrive; not a rating)")
        ax.axhline(100, color=INK2, lw=1.1, ls="--", label="100 mW: datasheet Table 8 drive at 135 and 175 MHz")
        ax.set_ylim(40, 400)
        ticks = [40, 60, 80, 100, 150, 200, 300, 400]
    ax.yaxis.set_major_locator(FixedLocator(ticks))
    ax.yaxis.set_minor_locator(NullLocator())
    ax.yaxis.set_major_formatter(ScalarFormatter())
    ax.set_xlabel("corner index (blocks: Si5351 source 25 ohm | 50 ohm, then GVA gain 22.5, 22.9, 24.1, 25.0, 25.3 dB;\n"
                  "within a block: P1dB set x frequency x Si5351 edge/VDDO case)")
    ax.set_ylabel("Fundamental power at the PA input (mW)")
    ax.scatter([], [], s=12, c=COL["a4"], label="Si5351 output 25 ohm")
    ax.scatter([], [], s=12, c=COL["a5"], label="Si5351 output 50 ohm")
    ax.legend(loc="upper left", fontsize=7.5, ncol=2)
    ax.set_title(f"{fin.upper()} drive chain in LTspice: power into the PA input at {len(rows)} corners, 144 to 148 MHz")
    fig.tight_layout()
    fig.savefig(out / f"drive_{fin}_corners.png", dpi=150)
    plt.close(fig)
    # plot: 3f at the GVA input
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    ax.scatter(xs, h3, s=10, c=colr, zorder=3)
    ax.axhline(-H3_MIN_DBC, color=INK, lw=1.2, ls="--")
    ax.text(2, -H3_MIN_DBC + 0.5, "limit: 3f at least 25 dB below the fundamental (TS-012)", fontsize=7.5, color=INK)
    ax.scatter([], [], s=12, c=COL["a4"], label="Si5351 output 25 ohm")
    ax.scatter([], [], s=12, c=COL["a5"], label="Si5351 output 50 ohm")
    ax.legend(loc="upper right", fontsize=8)
    ax.set_xlabel("corner index (as in the drive plot)")
    ax.set_ylabel("3f relative to f at the GVA-84+ input (dBc)")
    ax.set_title(f"{fin.upper()} drive chain: third harmonic of the Si5351 square wave after the drive LPF")
    ax.set_ylim(min(-62, h3.min() - 4), -12)
    fig.tight_layout()
    fig.savefig(out / f"drive_{fin}_h3.png", dpi=150)
    plt.close(fig)
    (out / "result.json").write_text(json.dumps(res, indent=2, default=float))
    write_drive_md(out, fin, res)
    copy_inputs(out, [deck])
    print(key, json.dumps({k: res[k] for k in res if k not in ("ltspice", "corner_min", "corner_max", "nominal_corner")}, default=float))
    return res


def add_req_lines(ax):
    ax.axhline(REQ012_HI, color=INK, lw=1.2, ls="--", label="6.30 W: REQ-SYS-012 upper bound (held by the ALC)")
    ax.axhline(REQ012_NOM, color=INK, lw=1.2, ls="-", label="5.0 W: REQ-SYS-012 nominal (ALC set point)")
    ax.axhline(REQ012_LO, color=INK, lw=2.0, ls="--", label="3.97 W: REQ-SYS-012 lower bound (5 W -1 dB)")


def cstr(c):
    return (f"source {c['rsrc']:.0f} ohm, GVA gain {c['gain']} dB, P1dB set {c['p1db']}, {c['freq'] / 1e6:.0f} MHz, "
            f"Si5351 case {c['src']} (VDDO {c['vddo']} V, edge {c['tr'] * 1e9:.1f} ns, duty {c['duty']:.2f})")


def write_drive_md(out, fin, r):
    L = [f"# {r['run']}: {fin.upper()} drive chain (WP-PDR-21 drive window)", ""]
    if fin == "a5":
        L += [f"Verdict, module input window 10 to 30 mW: **{'PASS' if r['window_pass_all_corners'] else 'FAIL'}** at all "
              f"{r['n_corners']} corners ({r['corners_in_window']} in the window, {r['corners_above_30mw']} above 30 mW, "
              f"{r['corners_below_10mw']} below 10 mW); on the TS-012 criterion corners only (source 25 and 50 ohm, "
              f"gain 22.5 and 25.0 dB, 144 to 148 MHz, nominal Si5351 edge and VDDO, all P1dB sets): "
              f"**{'PASS' if r['window_pass_criterion_corners'] else 'FAIL'}** ({r['criterion_corners_in_window']} of {r['criterion_corners']}).", ""]
    else:
        L += [f"Verdict, AFT05 drive at or below the 0.2 W ruggedness-test level (informative, not a rating): "
              f"**{'PASS' if r['overdrive_pass'] else 'FAIL'}** ({r['corners_above_overdrive']} corners above).", ""]
    L += [f"Verdict, 3f at the GVA-84+ input at least 25 dB below the fundamental: **{'PASS' if r['h3_pass'] else 'FAIL'}** "
          f"(worst {r['h3_dbc_gva_in_worst']:.1f} dBc).",
          f"GVA-84+ input at most {r['gva_in_dbm_max']:.1f} dBm against the +13 dBm maximum rating: "
          f"**{'PASS' if r['gva_absmax_pass'] else 'FAIL'}**.", "",
          "| Quantity | Min | Nominal | Max |", "|---|---|---|---|",
          f"| Power into the PA input (mW) | {r['pin_pa_w']['min'] * 1e3:.1f} | {r['pin_pa_w']['nominal'] * 1e3:.1f} | {r['pin_pa_w']['max'] * 1e3:.1f} |",
          f"| Power into the PA input (dBm) | {r['pin_pa_dbm']['min']:.2f} | {r['pin_pa_dbm']['nominal']:.2f} | {r['pin_pa_dbm']['max']:.2f} |",
          f"| CLK1 pin swing, peak to peak (V) | {r['clk_vpp']['min']:.2f} | - | {r['clk_vpp']['max']:.2f} |", "",
          f"- Lowest corner: {cstr(r['corner_min'])}.",
          f"- Highest corner: {cstr(r['corner_max'])}.",
          f"- Nominal corner: {cstr(r['nominal_corner'])}.",
          f"- Pad insertion loss between 50 ohm terminations (E24 values): {r['pad_loss_db']}.", ""]
    if fin == "a5":
        L += [f"- Spread of the drive over all corners {r['spread_db']:.2f} dB against a window of {r['window_db']:.2f} dB (10 to 30 mW).",
              f"- A fixed pad {r['extra_pad_db_for_30mw']:.2f} dB larger would bring the maximum to 30 mW and the minimum to "
              f"{r['min_after_extra_pad_mw']:.1f} mW.", ""]
    L += ["Plots: `drive_%s_corners.png` (power into the PA input per corner with the window), `drive_%s_h3.png` (3f at the "
          "GVA-84+ input). Per-corner numbers: `corners.json`. Deck `drive_%s.cir`; LTspice log and raw beside it." % (fin, fin, fin), ""]
    (out / "result.md").write_text("\n".join(L))


# ---------------------------------------------------------------- p1, p2: output power versus pack voltage
def a5_tables():
    xv = np.arange(3.0, 9.76, 0.25)
    v135 = resample(load_curve("ra07_pout_vs_vdd_135"), xv, 0.08)
    v155 = resample(load_curve("ra07_pout_vs_vdd_155"), xv, 0.08)
    xp = np.arange(-9.0, 16.01, 1.0)
    p135 = resample(load_curve("ra07_pout_vs_pin_135"), xp, 0.25)
    p155 = resample(load_curve("ra07_pout_vs_pin_155"), xp, 0.25)
    xg = np.arange(2.9, 3.61, 0.05)
    g135 = resample(load_curve("ra07_pout_vs_vgg_135"), xg, 0.015)
    g155 = resample(load_curve("ra07_pout_vs_vgg_155"), xg, 0.015)
    return dict(xv=xv, v135=v135, v155=v155, xp=xp, p135=p135, p155=p155, xg=xg, g135=g135, g155=g155)


def a4_tables():
    xp = np.round(np.exp(np.linspace(np.log(0.02), np.log(0.2), 21)), 5)
    c135, c155 = load_curve("aft05_pout_vs_pin_135"), load_curve("aft05_pout_vs_pin_155")
    def rs(c):
        lx = np.log(c[:, 0])
        return np.array([c[np.abs(lx - np.log(x)) <= 0.03, 1].mean() for x in xp])
    return dict(xp=xp, p135=rs(c135), p155=rs(c155))


def deck_power(fin: str, out: Path, pins: list[float]) -> tuple[Path, list[dict]]:
    """pins: PA input power corners from the drive run (dBm for A5, W for A4): [min, nominal, max]."""
    corners = []
    if fin == "a5":
        T = a5_tables()
        dims = [("irf", RFEED), ("ieta", A5_ETA), ("ipin", pins), ("ifr", FREQS), ("ivgg", [3.5, A5_VGG_CLAMP_LO]),
                ("isp", ["typ", "min"]), ("iloss", LOSS_DB)]
    else:
        T = a4_tables()
        dims = [("irf", RFEED), ("ieta", A4_ETA), ("ipin", pins), ("ifr", FREQS), ("in", A4_N),
                ("imatch", A4_LMATCH), ("iloss", LOSS_DB)]
    n = int(np.prod([len(v) for _, v in dims]))
    # mixed radix, first dimension fastest
    radix, lines = 1, []
    for name, vals in dims:
        lines.append(f".param {name}=floor(idx/{radix})-{len(vals)}*floor(idx/{radix * len(vals)})")
        radix *= len(vals)
    import itertools
    for combo in itertools.product(*[range(len(v)) for _, v in dims][::-1]):
        combo = combo[::-1]
        corners.append({name: vals[k] for (name, vals), k in zip(dims, combo)})
    def tab(name, vals, fmt="{:.6g}"):
        return f".param {name[1:]}=table({name}," + ",".join(f"{i},{fmt.format(v)}" for i, v in enumerate(vals)) + ")"
    common = [tab("irf", RFEED), tab("ipin", pins), tab("ifr", FREQS), tab("iloss", LOSS_DB),
              ".param w=(fr-135e6)/20e6", ".param kloss=pow(10,-loss/10)"]
    if fin == "a5":
        vt135 = table_expr("x", T["xv"], T["v135"])
        vt155 = table_expr("x", T["xv"], T["v155"])
        pt135 = table_expr("pin", T["xp"], T["p135"])
        pt155 = table_expr("pin", T["xp"], T["p155"])
        pr135 = table_expr("13.0103", T["xp"], T["p135"])
        pr155 = table_expr("13.0103", T["xp"], T["p155"])
        gl135 = table_expr(str(A5_VGG_CLAMP_LO), T["xg"], T["g135"])
        gl155 = table_expr(str(A5_VGG_CLAMP_LO), T["xg"], T["g155"])
        gh135 = table_expr("3.5", T["xg"], T["g135"])
        gh155 = table_expr("3.5", T["xg"], T["g155"])
        v72_135 = table_expr("7.2", T["xv"], T["v135"])
        v72_155 = table_expr("7.2", T["xv"], T["v155"])
        model = f"""{tab('ieta', A5_ETA)}
.param ivgg_=ivgg
.param isp_=isp
* drive factor: module output at pin relative to Pin 20 mW (13.01 dBm), datasheet Pout-Pin curves at 7.2 V
.param kd=((1-w)*pow(10,{pt135}/10)+w*pow(10,{pt155}/10))/((1-w)*pow(10,{pr135}/10)+w*pow(10,{pr155}/10))
* VGG factor: output at the lowest clamp (3.08 V) relative to 3.5 V, datasheet Pout-VGG curves at 7.2 V
.param kgl=((1-w)*{gl135}+w*{gl155})/((1-w)*{gh135}+w*{gh155})
.param kv=if(ivgg_>0.5,kgl,1)
* spread factor: datasheet minimum 6.5 W at 7.2 V, VGG 3.5 V, Pin 20 mW against the typical curve
.param kmin={A5_POUT_MIN_72}/((1-w)*{v72_135}+w*{v72_155})
.param ks=if(isp_>0.5,kmin,1)
* RA07M1317M: typical Pout versus drain voltage at Pin 20 mW, VGG 3.5 V (135 and 155 MHz, interpolated in f)
.func pv(x)=(1-w)*{vt135}+w*{vt155}
Bmod pmod 0 V=pv(max(V(d),3))*kd*kv*ks
Rmod pmod 0 1meg
Bpa d 0 I=V(pmod)/(eta*max(V(d),1))
"""
        title = "A5 RA07M1317M module"
    else:
        pt135 = table_expr("pinw", T["xp"], T["p135"], fmt="{:.5g}")
        pt155 = table_expr("pinw", T["xp"], T["p155"], fmt="{:.5g}")
        model = f"""{tab('ieta', A4_ETA)}
{tab('in', A4_N)}
{tab('imatch', A4_LMATCH)}
.param pinw=pin
.param kmatch=pow(10,-match/10)
* AFT05MS004N: Pout at 7.5 V versus Pin, NXP reference circuit (Figure 13, 135 and 155 MHz, interpolated in f)
.param p75=(1-w)*{pt135}+w*{pt155}
Bmod pmod 0 V=p75*pow(max(V(d),1)/7.5,n)*kmatch
Rmod pmod 0 1meg
Bpa d 0 I=V(pmod)/(eta*max(V(d),1))
"""
        title = "A4 AFT05MS004N"
    txt = f"""* power_{fin}.cir: {title}, output power at the SMA versus pack voltage (cwht WP-PDR-21, hardware/sim/tx-pa)
* Pack EMF Vp (swept 6.4 to 8.4 V; equal to the voltage read in receive within 10 mV) behind the drain feed rfeed;
* the 5 V bus ({IBUS} A, est.) and the PA drain current Pout/(eta*Vd) load the feed, so the key-down sag is solved
* by LTspice. V(pmod) is the PA output power in watts, V(psma) the power at the SMA after the output LPF and relay.
* {n} corners flattened into one .step (idx), first dimension fastest: {', '.join(d for d, _ in dims)}.
.param idx=0
.step param idx 0 {n - 1} 1
{chr(10).join(lines)}
{chr(10).join(common)}
{model}Vp p 0 7.4
Rf p d {{rf}}
Ibus d 0 {IBUS}
Bsma psma 0 V=V(pmod)*kloss
Rsma psma 0 1meg
.dc Vp 6.4 8.4 0.05
.save V(d) V(pmod) V(psma) I(Vp)
.end
"""
    p = out / f"power_{fin}.cir"
    p.write_text(txt)
    return p, corners


def analyse_power(fin: str, key: str, drive_key: str, pins_override: list[float] | None = None):
    out = rundir(key)
    dres = json.loads((rundir(drive_key) / "result.json").read_text())
    if pins_override is not None:
        pins = pins_override
    elif fin == "a5":
        pins = [dres["pin_pa_dbm"]["min"], dres["pin_pa_dbm"]["nominal"], dres["pin_pa_dbm"]["max"]]
    else:
        pins = [dres["pin_pa_w"]["min"], dres["pin_pa_w"]["nominal"], dres["pin_pa_w"]["max"]]
    deck, corners = deck_power(fin, out, pins)
    prov = run_ltspice(deck, out)
    raw = RawRead(str(out / f"power_{fin}.raw"))
    nst = len(raw.get_steps())
    assert nst == len(corners), (nst, len(corners))
    vp = np.abs(raw.get_trace(raw.get_trace_names()[0]).get_wave(0))
    S = np.array([raw.get_trace("V(psma)").get_wave(i) for i in range(nst)])
    M = np.array([raw.get_trace("V(pmod)").get_wave(i) for i in range(nst)])
    D = np.array([raw.get_trace("V(d)").get_wave(i) for i in range(nst)])
    I = np.array([np.abs(raw.get_trace("I(Vp)").get_wave(i)) for i in range(nst)])
    if fin == "a5":
        nom = dict(irf=0.35, ieta=0.60, ipin=pins[1], ifr=146e6, ivgg=3.5, isp="typ", iloss=0.5)
        typ_mask = np.array([c["isp"] == "typ" for c in corners])
        min_mask = ~typ_mask
    else:
        nom = dict(irf=0.35, ieta=0.67, ipin=pins[1], ifr=146e6, **{"in": 2.0}, imatch=0.25, iloss=0.5)
        typ_mask = np.ones(len(corners), bool)
        min_mask = None
    inom = next(i for i, c in enumerate(corners) if all(c[k] == v for k, v in nom.items()))
    i64 = int(np.argmin(np.abs(vp - 6.4)))
    i84 = int(np.argmin(np.abs(vp - 8.4)))
    lo_typ = S[typ_mask].min(axis=0)
    hi_all = S.max(axis=0)
    res = {"run": RUNS[key], "finalist": fin.upper(), "ltspice": prov, "n_corners": len(corners),
           "pin_corners_from": RUNS[drive_key] + (" with the select-on-test pad residual (s1 method)" if pins_override else ""),
           "pin_corners": pins,
           "vpack": vp.tolist(),
           "sma_nominal_w": S[inom].tolist(), "sma_low_typ_w": lo_typ.tolist(), "sma_high_w": hi_all.tolist(),
           "module_high_w": M.max(axis=0).tolist(), "module_nominal_w": M[inom].tolist(),
           "drain_nominal_v": D[inom].tolist(), "drain_low_v": D.min(axis=0).tolist(),
           "pack_current_nominal_a": I[inom].tolist(), "pack_current_max_a": I.max(axis=0).tolist(),
           "at_6v4": {"sma_nominal_w": float(S[inom, i64]), "sma_low_typ_w": float(lo_typ[i64]),
                      "sma_high_w": float(hi_all[i64]), "drain_nominal_v": float(D[inom, i64]),
                      "drain_low_v": float(D[:, i64].min())},
           "at_8v4": {"sma_nominal_w": float(S[inom, i84]), "sma_high_w": float(hi_all[i84]),
                      "module_high_w": float(M[:, i84].max()), "module_nominal_w": float(M[inom, i84])},
           "worst_low_corner": corners[int(np.argmin(S[typ_mask][:, i64]))] if fin == "a4" else
                               [c for c, m in zip(corners, typ_mask) if m][int(np.argmin(S[typ_mask][:, i64]))],
           "nominal_corner": corners[inom]}
    res["pass_low_typ_ge_3v97_over_range"] = bool(lo_typ.min() >= REQ012_LO)
    res["pass_nominal_ge_5w_over_range"] = bool(S[inom].min() >= REQ012_NOM)
    res["low_typ_min_w"] = float(lo_typ.min())
    if fin == "a5":
        lo_min = S[min_mask].min(axis=0)
        nom_min = dict(nom, isp="min")
        inm = next(i for i, c in enumerate(corners) if all(c[k] == v for k, v in nom_min.items()))
        res["sma_low_minmodule_w"] = lo_min.tolist()
        res["sma_nominal_minmodule_w"] = S[inm].tolist()
        res["at_6v4"]["sma_low_minmodule_w"] = float(lo_min[i64])
        res["at_6v4"]["sma_nominal_minmodule_w"] = float(S[inm, i64])
        res["pass_low_minmodule_ge_3v97"] = bool(lo_min.min() >= REQ012_LO)
        res["module_high_gt_8w_at"] = float(vp[np.argmax(M.max(axis=0) > A5_MOD_STAB_W)]) if (M.max(axis=0) > A5_MOD_STAB_W).any() else None
        res["module_high_gt_10w_at"] = float(vp[np.argmax(M.max(axis=0) > A5_MOD_MAX_W)]) if (M.max(axis=0) > A5_MOD_MAX_W).any() else None
        # the lowest-output corner with VGG at 3.5 V (the ALC's own top, typical module)
        m35 = typ_mask & np.array([c["ivgg"] == 3.5 for c in corners])
        res["at_6v4"]["sma_low_typ_vgg35_w"] = float(S[m35][:, i64].min())
        # closure levers: drain feed at most 0.35 ohm (TS-012 pre-order check), VGG clamp not limiting
        rf = np.array([c["irf"] <= 0.35 for c in corners])
        v35 = np.array([c["ivgg"] == 3.5 for c in corners])
        res["at_6v4"]["sma_low_typ_rf035_w"] = float(S[typ_mask & rf][:, i64].min())
        res["at_6v4"]["sma_low_typ_rf035_vgg35_w"] = float(S[typ_mask & rf & v35][:, i64].min())
        res["at_6v4"]["sma_low_minmodule_rf035_vgg35_w"] = float(S[min_mask & rf & v35][:, i64].min())
        res["pack_v_where_low_typ_reaches_3v97"] = round(float(vp[np.argmax(lo_typ >= REQ012_LO)]), 2) if (lo_typ >= REQ012_LO).any() else None
        res["pack_v_where_low_minmodule_reaches_3v97"] = round(float(vp[np.argmax(lo_min >= REQ012_LO)]), 2) if (lo_min >= REQ012_LO).any() else None
    else:
        m20 = np.array([c["in"] == 2.0 and c["imatch"] == 0.0 for c in corners])
        res["at_6v4"]["sma_low_n2_refmatch_w"] = float(S[m20][:, i64].min())
        res["at_6v4"]["sma_high_w"] = float(hi_all[i64])
        pn = np.array([c["ipin"] >= pins[1] for c in corners])
        res["at_6v4"]["sma_low_pin_ge_nominal_w"] = float(S[pn][:, i64].min())
        res["at_8v4"]["sma_low_w"] = float(lo_typ[i84])
        nomw = S[inom]
        res["pack_v_where_nominal_reaches_3v97"] = round(float(vp[np.argmax(nomw >= REQ012_LO)]), 2) if (nomw >= REQ012_LO).any() else None
        res["pack_v_where_nominal_reaches_5w"] = round(float(vp[np.argmax(nomw >= REQ012_NOM)]), 2) if (nomw >= REQ012_NOM).any() else None
    (out / "result.json").write_text(json.dumps(res, indent=1, default=str))
    # plot
    fig, ax = plt.subplots(figsize=(7.2, 5.6))
    c = COL[fin]
    ax.fill_between(vp, lo_typ, hi_all, color=c, alpha=0.15, lw=0, label="envelope of all corners" + (" (typical module)" if fin == "a5" else ""))
    ax.plot(vp, S[inom], color=c, lw=2, label="nominal corner")
    if fin == "a5":
        ax.plot(vp, res["sma_low_minmodule_w"], color=COL["aux"], lw=2, ls="--", label="datasheet-minimum module, lowest corner")
        ax.plot(vp, M.max(axis=0), color=INK2, lw=1.2, ls="-.", label="module output, highest corner (ALC open, VGG 3.5 V)")
        ax.axhline(A5_MOD_STAB_W, color=INK2, lw=1, ls=":", label="8 W: module stability guarantee (module output)")
        ax.axhline(A5_MOD_MAX_W, color=INK2, lw=1.6, ls=":", label="10 W: module maximum rating (module output)")
    add_req_lines(ax)
    ax.set_xlim(*PACK)
    ax.set_ylim(0, 12 if fin == "a5" else 9)
    ax.set_xlabel("Pack voltage, read in receive (V)")
    ax.set_ylabel("Available power, ALC at its top (W)")
    ax.set_title(f"{fin.upper()}: power at the SMA versus pack voltage (LTspice, {len(corners)} corners)\n"
                 "key-down sag, output LPF and relay loss included")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.13), ncol=2, fontsize=7.5)
    fig.tight_layout()
    fig.savefig(out / f"power_{fin}_sma.png", dpi=150)
    plt.close(fig)
    write_power_md(out, fin, res)
    copy_inputs(out, [deck])
    print(key, json.dumps({k: res[k] for k in ("at_6v4", "at_8v4", "pass_low_typ_ge_3v97_over_range", "pass_nominal_ge_5w_over_range")}, default=str))
    return res


def write_power_md(out, fin, r):
    a, b = r["at_6v4"], r["at_8v4"]
    L = [f"# {r['run']}: {fin.upper()} output power at the SMA versus pack voltage (REQ-SYS-012)", "",
         f"Verdict, lowest corner at least 3.97 W at the SMA from 6.4 to 8.4 V" + (" (typical module)" if fin == "a5" else "") +
         f": **{'PASS' if r['pass_low_typ_ge_3v97_over_range'] else 'FAIL'}** (lowest {r['low_typ_min_w']:.2f} W).",
         f"Nominal corner at least 5.0 W (the ALC set point is reachable) over the range: **{'PASS' if r['pass_nominal_ge_5w_over_range'] else 'FAIL'}**."]
    if fin == "a5":
        L.append(f"Datasheet-minimum module (6.5 W at 7.2 V), lowest corner at least 3.97 W: **{'PASS' if r['pass_low_minmodule_ge_3v97'] else 'FAIL'}** "
                 f"({a['sma_low_minmodule_w']:.2f} W at 6.4 V; nominal corner with that module {a['sma_nominal_minmodule_w']:.2f} W).")
    L += ["", "| At the pack voltage | Nominal (W) | Lowest corner (W) | Highest corner (W) |", "|---|---|---|---|",
          f"| 6.4 V | {a['sma_nominal_w']:.2f} | {a['sma_low_typ_w']:.2f} | {a['sma_high_w']:.2f} |",
          f"| 8.4 V | {b['sma_nominal_w']:.2f} | - | {b['sma_high_w']:.2f} |", "",
          f"- Drain voltage at 6.4 V: nominal {a['drain_nominal_v']:.2f} V, lowest {a['drain_low_v']:.2f} V (key-down sag).",
          f"- Module or device output at 8.4 V: nominal {b['module_nominal_w']:.2f} W, highest corner {b['module_high_w']:.2f} W (ALC open; the ALC must hold 5 W).",
          f"- Drive corners used (from {r['pin_corners_from']}): {r['pin_corners']}.",
          f"- Lowest corner at 6.4 V: {r['worst_low_corner']}.", f"- Nominal corner: {r['nominal_corner']}."]
    if fin == "a5":
        L += [f"- Lowest corner at 6.4 V with VGG at 3.5 V (no clamp limit): {a['sma_low_typ_vgg35_w']:.2f} W.",
              f"- Module output at the highest corner (open loop, VGG 3.5 V): above 8 W (stability guarantee) from "
              f"{r['module_high_gt_8w_at'] if r['module_high_gt_8w_at'] is not None else 'nowhere below 8.4'} V; above 10 W (maximum rating) from "
              f"{r['module_high_gt_10w_at'] if r['module_high_gt_10w_at'] is not None else 'nowhere below 8.4'} V.",
              f"- Lowest corner at 6.4 V with the drain feed at most 0.35 ohm: {a['sma_low_typ_rf035_w']:.2f} W; with that and VGG at 3.5 V: "
              f"{a['sma_low_typ_rf035_vgg35_w']:.2f} W; datasheet-minimum module with both: {a['sma_low_minmodule_rf035_vgg35_w']:.2f} W.",
              f"- Lowest corner reaches 3.97 W from {r['pack_v_where_low_typ_reaches_3v97']} V (typical module) and from "
              f"{r['pack_v_where_low_minmodule_reaches_3v97']} V (datasheet-minimum module)."]
    else:
        L += [f"- Lowest corner at 6.4 V with n = 2 and the reference-circuit match loss: {a['sma_low_n2_refmatch_w']:.2f} W.",
              f"- Lowest corner at 6.4 V with the drive at or above nominal: {a['sma_low_pin_ge_nominal_w']:.2f} W; lowest corner at 8.4 V: {b['sma_low_w']:.2f} W.",
              f"- Nominal corner reaches 3.97 W from {r['pack_v_where_nominal_reaches_3v97']} V and 5.0 W from {r['pack_v_where_nominal_reaches_5w']} V."]
    L += ["", f"Plot: `power_{fin}_sma.png`. Deck `power_{fin}.cir`; LTspice log and raw beside it; numbers in `result.json`.", ""]
    (out / "result.md").write_text("\n".join(L))


# ---------------------------------------------------------------- s1: summary plots and verdicts
def sot_residual() -> dict:
    """A5 select-on-test pad: per unit (source R, gain, P1dB set, Si5351 case) only frequency varies in service."""
    rows5 = json.loads((rundir("d2") / "corners.json").read_text())
    units = {}
    for r in rows5:
        units.setdefault((r["rsrc"], r["gain"], r["p1db"], r["src"]), []).append(r["pin_pa_dbm"])
    fspan = max(max(v) - min(v) for v in units.values())
    half = fspan / 2 + SOT_STEP_DB / 2 + SOT_MEAS_DB + SOT_DRIFT_DB
    sot = {"freq_span_within_unit_db": fspan, "step_db": SOT_STEP_DB, "meas_db": SOT_MEAS_DB, "drift_db": SOT_DRIFT_DB,
           "half_width_db": half, "target_mw": SOT_TARGET_MW,
           "min_mw": SOT_TARGET_MW * 10 ** (-half / 10), "max_mw": SOT_TARGET_MW * 10 ** (half / 10)}
    sot["pass"] = bool(sot["min_mw"] >= A5_PIN_MIN_MW and sot["max_mw"] <= A5_PIN_MAX_MW)
    return sot


def run_s1():
    out = rundir("s1")
    d5 = json.loads((rundir("d2") / "result.json").read_text())
    d4 = json.loads((rundir("d3") / "result.json").read_text())
    p5 = json.loads((rundir("p1") / "result.json").read_text())
    p4 = json.loads((rundir("p2") / "result.json").read_text())
    p6f = rundir("p3") / "result.json"
    p6 = json.loads(p6f.read_text()) if p6f.exists() else None
    vp = np.array(p5["vpack"])
    sot = sot_residual()
    # Figure 1: Pin at the PA versus pack voltage (the drive chain is on regulated rails: flat in pack voltage)
    fig, axs = plt.subplots(1, 2, figsize=(10.0, 5.2))
    for ax, d, fin in ((axs[0], d5, "a5"), (axs[1], d4, "a4")):
        c = COL[fin]
        lo, nomv, hi = d["pin_pa_w"]["min"] * 1e3, d["pin_pa_w"]["nominal"] * 1e3, d["pin_pa_w"]["max"] * 1e3
        ax.fill_between(vp, lo, hi, color=c, alpha=0.18, lw=0, label=f"all drive corners ({lo:.1f} to {hi:.1f} mW)")
        ax.plot(vp, np.full_like(vp, nomv), color=c, lw=2, label=f"nominal corner ({nomv:.1f} mW)")
        clo, chi = d["pin_pa_criterion_corners_w"]["min"] * 1e3, d["pin_pa_criterion_corners_w"]["max"] * 1e3
        ax.plot(vp, np.full_like(vp, clo), color=c, lw=1, ls="--", label=f"TS-012 criterion corners ({clo:.1f} to {chi:.1f} mW)")
        ax.plot(vp, np.full_like(vp, chi), color=c, lw=1, ls="--")
        if fin == "a5":
            ax.fill_between(vp, sot["min_mw"], sot["max_mw"], facecolor="none", edgecolor=COL["ok"], hatch="///", lw=0,
                            label=f"after a select-on-test pad, est. ({sot['min_mw']:.1f} to {sot['max_mw']:.1f} mW)")
            ax.axhline(30, color=INK, lw=1.4, label="30 mW: maximum rating, top of the stability window")
            ax.axhline(10, color=INK, lw=1.4, ls="-.", label="10 mW: bottom of the stability window")
            ax.set_ylim(0, 40)
            ax.set_title("A5: power into the RA07M1317M input")
        else:
            ax.axhline(200, color=INK, lw=1.4, label="200 mW: ruggedness-test drive (not a rating)")
            ax.axhline(100, color=INK2, lw=1.1, ls=":", label="100 mW: datasheet Table 8 drive")
            ax.set_ylim(0, 240)
            ax.set_title("A4: power into the AFT05MS004N input")
        ax.set_xlim(*PACK)
        ax.set_xlabel("Pack voltage, read in receive (V)")
        ax.set_ylabel("Fundamental power at the PA input (mW)")
        ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.14), ncol=1, fontsize=7.5)
    fig.suptitle("Drive at the PA input versus pack voltage (Si5351 and GVA-84+ on regulated rails; LTspice, 270 corners each)", fontsize=10)
    fig.tight_layout()
    fig.savefig(out / "pin_at_pa_vs_pack.png", dpi=150)
    plt.close(fig)
    # Figure 2: Pout at the SMA versus pack voltage, both finalists
    fig, ax = plt.subplots(figsize=(7.4, 5.8))
    for p, fin, lab in ((p5, "a5", "A5 RA07M1317M (typical module)"), (p4, "a4", "A4 AFT05MS004N")):
        c = COL[fin]
        ax.fill_between(vp, p["sma_low_typ_w"], p["sma_high_w"], color=c, alpha=0.15, lw=0, label=f"{lab}: all corners")
        ax.plot(vp, p["sma_nominal_w"], color=c, lw=2, label=f"{lab}: nominal corner")
    ax.plot(vp, p5["sma_low_minmodule_w"], color=COL["aux"], lw=1.6, ls="--", label="A5 with a datasheet-minimum module: lowest corner")
    if p6 is not None:
        ax.plot(vp, p6["sma_low_typ_w"], color=COL["a5"], lw=1.4, ls=":", label="A5 with the select-on-test pad: lowest corner")
    add_req_lines(ax)
    ax.set_xlim(*PACK)
    ax.set_ylim(0, 10)
    ax.set_xlabel("Pack voltage, read in receive (V)")
    ax.set_ylabel("Available power at the SMA, ALC at its top (W)")
    ax.set_title("Power at the SMA versus pack voltage, A4 and A5 (LTspice)\n"
                 "key-down sag, output LPF and relay loss included; the ALC holds 5 W where the band is above it")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncol=2, fontsize=7.5)
    fig.tight_layout()
    fig.savefig(out / "pout_at_sma_vs_pack.png", dpi=150)
    plt.close(fig)
    summary = {"run": RUNS["s1"], "inputs": [RUNS[k] for k in ("d2", "d3", "p1", "p2")], "a5_sot_pad": sot,
               "a5": {"drive_window_all_corners": d5["window_pass_all_corners"],
                      "drive_window_criterion_corners": d5["window_pass_criterion_corners"],
                      "pin_mw": [d5["pin_pa_w"]["min"] * 1e3, d5["pin_pa_w"]["nominal"] * 1e3, d5["pin_pa_w"]["max"] * 1e3],
                      "h3_pass": d5["h3_pass"], "sma_6v4_low_typ_w": p5["at_6v4"]["sma_low_typ_w"],
                      "sma_6v4_nominal_w": p5["at_6v4"]["sma_nominal_w"],
                      "sma_6v4_low_minmodule_w": p5["at_6v4"]["sma_low_minmodule_w"],
                      "req012_low_typ": p5["pass_low_typ_ge_3v97_over_range"],
                      "sot_sma_6v4_low_typ_w": p6["at_6v4"]["sma_low_typ_w"] if p6 else None,
                      "sot_sma_6v4_low_minmodule_w": p6["at_6v4"]["sma_low_minmodule_w"] if p6 else None,
                      "sot_req012_low_typ": p6["pass_low_typ_ge_3v97_over_range"] if p6 else None,
                      "req012_low_minmodule": p5["pass_low_minmodule_ge_3v97"]},
               "a4": {"pin_mw": [d4["pin_pa_w"]["min"] * 1e3, d4["pin_pa_w"]["nominal"] * 1e3, d4["pin_pa_w"]["max"] * 1e3],
                      "overdrive_pass": d4["overdrive_pass"], "h3_pass": d4["h3_pass"],
                      "sma_6v4_low_w": p4["at_6v4"]["sma_low_typ_w"], "sma_6v4_nominal_w": p4["at_6v4"]["sma_nominal_w"],
                      "sma_6v4_high_w": p4["at_6v4"]["sma_high_w"], "req012_low": p4["pass_low_typ_ge_3v97_over_range"]}}
    (out / "result.json").write_text(json.dumps(summary, indent=2, default=float))
    shutil.copy2(Path(__file__), out / Path(__file__).name)
    print("s1", json.dumps(summary, default=float))


def main():
    what = sys.argv[1] if len(sys.argv) > 1 else "all"
    todo = ["d1", "d2", "d3", "p1", "p2", "p3", "s1"] if what == "all" else [what]
    for k in todo:
        if k == "d1":
            run_d1()
        elif k == "d2":
            analyse_drive("a5", "d2")
        elif k == "d3":
            analyse_drive("a4", "d3")
        elif k == "p1":
            analyse_power("a5", "p1", "d2")
        elif k == "p2":
            analyse_power("a4", "p2", "d3")
        elif k == "p3":
            sot = sot_residual()
            analyse_power("a5", "p3", "d2", [float(dbm(sot["min_mw"] * 1e-3)), float(dbm(SOT_TARGET_MW * 1e-3)),
                                              float(dbm(sot["max_mw"] * 1e-3))])
        elif k == "s1":
            run_s1()


if __name__ == "__main__":
    main()
