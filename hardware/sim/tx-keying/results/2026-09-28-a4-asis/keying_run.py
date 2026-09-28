#!/usr/bin/env python3
"""Keying envelope and key-click analysis for the TS-012 finalists A4 and A5 (WP-PDR-22 pre-order item).

cwht, hardware/sim/tx-keying. Analysis record: docs/design/analysis/keying-ts012.md.

Stages (run in order; each writes into results/<run-id>/):
  detchar           read the LTspice runs of det_char.cir (TS-012 zero-bias detector) and det_char_biased.cir
                    (biased detector with reference diode) in results/2026-09-28-det-char*/: static law of each
                    1N5711W ALC detector at 146 MHz -> det_law.csv, det_law.png, result.json
  deck FIN VAR      generate keying_FIN_VAR.cir (FIN = a4 | a5, VAR = asis | mitig), run it through
                    tools/ltspice-batch.sh, analyse the .raw (spicelib), write result.json, result.csv,
                    envelope.png, spectrum.png, keyup_level.png (and corners.png for mitig), and copy the deck
                    and this script into the run directory
  replot FIN VAR    as deck, from the existing .raw of the run, without running LTspice (deck must be unchanged)
  summary           cross-run summary.png and summary.json, the analytic PWM carrier ripple (pwm_ripple.png)
                    and the analytic loop margin of the mitigated loop

Every LTspice run goes through tools/ltspice-batch.sh (ACC-LTSPICE-001); the GUI is never opened.

Model (envelope domain; the 146 MHz carrier is simulated only in the detector decks):
  VAR asis (TS-012 revision 4 section 7.3 as written): firmware raised-cosine table x setpoint -> 12-bit PWM
  updated every 32.768 us -> 2-pole RC -> MCP6002 inverting integrator (macro: GBW 1 MHz, rails 0 to 5 V;
  Rin 10 k, Cf, idle bias 4.7 M to +5 V) -> 0.654 divider (1.77 k Thevenin, 10 nF on the VGG node) -> PA static
  transfer P(VGG) from the datasheet graph (dBm table, scaled for drain voltage) x drive gate (CLK1 and GVA-84+
  bias, 10 us) x relay contact -> 0.5 dB LPF and relay loss -> amplitude at the 50 ohm load -> zero-bias
  detector static law -> 22 us video pole -> integrator.
  VAR mitig: the same PA, gate and contact, plus a feedforward VGG table (second PWM channel, nominal inverse
  PA curve), the loop as a bipolar trim of +/-0.25 V (ideal difference integrator about mid-rail with rails,
  reset while parked), a biased detector with a reference diode (4.7 us video pole), a reference table
  predistorted by that detector's law and a firmware setpoint limited at the low pack end; corners on the PA
  threshold (+/-0.1 V) and on the residual loop offset (+/-1 mV).
All model numbers that are graph reads or estimates are labelled so in the tables below and in the record.
"""
import json
import math
import shutil
import subprocess
import sys
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from spicelib import RawRead  # noqa: E402

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
RESULTS = HERE / "results"
WRAPPER = REPO / "tools" / "ltspice-batch.sh"
DETRUN = RESULTS / "2026-09-28-det-char"
DATE = "2026-09-28"

# ---------------------------------------------------------------- requirement limits
REQ = {
    "bw26_hz": 350.0,          # REQ-SYS-015: 26 dB bandwidth (97.3(a)(8) power containment) <= 350 Hz (TBR)
    "side_offset_hz": 750.0,   # REQ-TX-006: every 10 Hz cell beyond 750 Hz ...
    "side_db": -60.0,          # ... at least 60 dB below total mean power (TBR)
    "t1090_tol_ms": 0.5,       # TC-SYS-013: 10-to-90 % time equal to the setting within +/-0.5 ms
    "shape_tol": 0.05,         # TC-SYS-013: normalized envelope within 5 % of full scale of the ideal
    "overshoot_db": 0.2,       # TS-012 section 7.3 WP-PDR-22 criterion
    "vgg_max": 3.5,            # RA07M1317M rating condition (Pout 10 W at VGG <= 3.5 V); A5 only
    "keyup_dbm": -30.0,        # REQ-TX-014: <= 1 uW with TX_KEY deasserted, PA_EN asserted, exciter driven
    "rfoff_dbm": -57.0,        # REQ-SYS-183: <= -57 dBm in every RF-ended state
}

# ---------------------------------------------------------------- PA transfer tables
# A5: Mitsubishi RA07M1317M datasheet (publication Jun. 2019), page 5 "Output power, drain current versus
# gate voltage", VDD 7.2 V, Pin 20 mW; graph read 2026-09-28 at 135 and 155 MHz and averaged for 146 MHz.
# Points at 2.2 V and above are graph reads (resolution about 0.05 W); below 2.2 V the graph shows "about 0"
# and the table continues with an ESTIMATED 100 dB/V sub-threshold slope (sensitivity in the record).
A5_W = [(2.2, 0.08), (2.3, 0.17), (2.4, 0.55), (2.5, 1.25), (2.6, 2.4), (2.7, 3.85), (2.8, 5.1),
        (2.9, 6.3), (3.0, 7.1), (3.1, 7.65), (3.2, 8.0), (3.3, 8.18), (3.4, 8.3), (3.5, 8.4),
        (3.75, 8.8), (4.0, 9.4)]
# Drain-voltage scale: datasheet page 4, Pout versus VDD at VGG 3.5 V, Pin 20 mW, 155 MHz (graph read):
# 5.5 V 4.8 W, 7.2 V 7.75 W, 7.9 V 9.1 W. Scale = P(VD) / P(7.2 V), applied to the whole VGG curve
# (assumption: the curve shape does not move with VDD).
A5_SCALE = {5.5: 4.8 / 7.75, 7.9: 9.1 / 7.75}
# A4: NXP AFT05MS004N datasheet Rev. 0, 7/2014, Figure 12 (VHF broadband reference circuit, 155 MHz,
# VDD 7.5 V, Pin 0.1 W), graph read 2026-09-28 (main plot and Detail A). The graph stops at 2.35 V
# (5.6 W, still rising); the points above 2.35 V are ESTIMATES that saturate near the 6.2 W of Figure 11
# (Pin 0.1 W). Below 1.2 V: ESTIMATED 100 dB/V sub-threshold slope.
A4_W = [(1.2, 0.05), (1.3, 0.17), (1.4, 0.40), (1.5, 0.72), (1.6, 1.05), (1.7, 1.5), (1.8, 2.0),
        (1.9, 2.6), (2.0, 3.2), (2.1, 3.9), (2.2, 4.6), (2.3, 5.3), (2.35, 5.6), (2.5, 6.1),
        (2.7, 6.35), (3.0, 6.45), (3.5, 6.5), (5.0, 6.55)]
# A4 scale: TS-012 section 1 gives about 3.2 W at the SMA at the 6.4 V pack end (adversarial C2), i.e.
# 3.6 W at the device (0.5 dB loss) at about 6.1 V drain; at 8.4 V pack (8.1 V drain) the V^2 law with the
# same match derating gives 0.988 of the 7.5 V table. Both ESTIMATES.
A4_SCALE = {6.1: 3.6 / 6.45, 8.1: (8.1 / 7.5) ** 2 * (3.6 / 6.45) / (6.1 / 7.5) ** 2}

SUBTH_DB_PER_V = 100.0  # ESTIMATE, see above

FIN = {
    "a5": dict(
        name="A5 (RA07M1317M module, VGG loop)", table=A5_W, scale=A5_SCALE, vd_lo=5.5, vd_hi=7.9,
        # leakage with VGG = 0 and the exciter driven: 20 mW in, module isolation 30 dB (TS-012 section 7.3
        # backwave figure; the datasheet says the input "attenuates up to 60 dB", not a guaranteed limit)
        pleak_dbm=-17.0, pleak_best_dbm=13.0 - 60.0,
        cf_asis=16e-9, cf_mitig=2.8e-9, pset_lo_mitig=4.0,
    ),
    "a4": dict(
        name="A4 (AFT05MS004N discrete, gate-bias loop)", table=A4_W, scale=A4_SCALE, vd_lo=6.1, vd_hi=8.1,
        # leakage with VGS = 0 and the GVA-84+ driving 0.1 W: current through Crss (1.63 pF at 7.5 V,
        # datasheet Table 5) from a gate swing of about 2 V peak into the 2.56 ohm load line: about -19 dBm
        # (ESTIMATE, derived in the record)
        pleak_dbm=-19.0, pleak_best_dbm=-23.0,
        cf_asis=7e-9, cf_mitig=1.2e-9, pset_lo_mitig=2.9,
    ),
}

VAR = {
    "asis": dict(short="as written (TS-012 rev. 4)", name="as written in TS-012 revision 4", tg=1e-3, pred=False, ff=False, det="zero"),
    "mitig": dict(short="mitigated", name="mitigated (feedforward VGG table, loop as trim, detector predistortion, "
                       "biased detector, low-pack setpoint)", tg=1e-3, pred=True, ff=True, det="biased"),
}

SETTINGS_MS = [3.0, 5.0, 8.0]
TPER, TDIT, TLEAD, TCLK, TC = 48e-3, 24e-3, 10e-3, 8e-3, 7.5e-3
TQ = 32.768e-6
NEL = 8
RIN, RIDLE, KDIV, RTH, CVGG = 10e3, 4.7e6, 0.654, 1.77e3, 10e-9
# mitigated variant: the loop output is a trim of 0.1 V per volt (0 to 0.5 V) added to a feedforward VGG
# table (second PWM channel) computed from the nominal PA curve for KFF of the wanted amplitude
KTRIM, KFF = 0.1, 1.0
# module-to-module threshold spread corner applied to the simulated PA (not to the firmware table): the
# PA table is evaluated at VGG - VSH (ESTIMATE of lot spread; neither datasheet gives a threshold spread for
# the transfer curve, the AFT05 gives VGS(th) 1.7 to 2.5 V at 67 uA)
# mitigated variant corners (VSH, VOS): nominal, PA threshold -0.1 and +0.1 V, residual error-amplifier
# offset +1 and -1 mV after the firmware zero calibration (ESTIMATE: one 12-bit ADC step at 3.3 V is 0.8 mV)
CORNERS_MITIG = [(0.0, 0.0), (-0.1, 0.0), (0.1, 0.0), (0.0, 1e-3), (0.0, -1e-3)]
LOSS_DB = 0.5
RC_1090 = (math.acos(-0.8) - math.acos(0.8)) / math.pi  # 0.5903: 10-90 % time / full transition


# ---------------------------------------------------------------- helpers
def dbm_table(points, knee_extra=6):
    """(VGG, W) points -> list of (VGG, dBm) with the estimated sub-threshold extension below."""
    v0, p0 = points[0]
    d0 = 10 * math.log10(p0 * 1e3)
    out = []
    for k in range(knee_extra, 0, -1):
        v = v0 - 0.5 * k
        out.append((round(v, 3), d0 - SUBTH_DB_PER_V * (v0 - v)))
    out += [(v, 10 * math.log10(p * 1e3)) for v, p in points]
    return out


def det_law(key="zero"):
    rows = np.loadtxt(RESULTS / DET[key]["run"] / "det_law.csv", delimiter=",", skiprows=1)
    return rows[:, 0], rows[:, 1]


def det_of(a, A, D):
    """Detector static law, log-log interpolation, 0 at 0."""
    a = np.asarray(a, dtype=float)
    out = np.zeros_like(a)
    m = a > 0
    out[m] = np.exp(np.interp(np.log(np.clip(a[m], A[0], A[-1])), np.log(A), np.log(D)))
    small = m & (a < A[0])
    out[small] = D[0] * (a[small] / A[0]) ** 2  # square law below the first point
    return out


def spice_table(pairs):
    return ",".join(f"{x:.6g},{y:.6g}" for x, y in pairs)


# ---------------------------------------------------------------- stage: detector characterization
DET = {
    "zero": dict(run="2026-09-28-det-char", deck="det_char.cir",
                 label="TS-012 detector: series 1N5711W, zero bias, 47 k load"),
    "biased": dict(run="2026-09-28-det-char-biased", deck="det_char_biased.cir",
                   label="mitigated detector: shunt 1N5711W at 21 uA with matched reference diode"),
}
AMPS = [0.05, 0.1, 0.2, 0.35, 0.6, 1, 1.7, 3, 5, 9, 15, 22.36, 28]


def read_meas(logpath, name="vdet"):
    """The .meas table of an LTspice log (LTspice integrates over time; the solver step is variable,
    so a sample mean of the .raw would be biased)."""
    log = logpath.read_text().splitlines()
    i0 = [i for i, l in enumerate(log) if l.startswith(f"Measurement: {name}")][0]
    vals = []
    for l in log[i0 + 2:]:
        f = l.split()
        if len(f) < 2 or not f[0].isdigit():
            break
        vals.append(float(f[1]))
    return vals


def stage_detchar():
    laws = {}
    for key, d in DET.items():
        rundir = RESULTS / d["run"]
        vals = read_meas(rundir / (Path(d["deck"]).stem + ".log"))
        raw = RawRead(str(rundir / (Path(d["deck"]).stem + ".raw")))  # the .raw is the record; step count
        assert len(raw.get_steps()) == len(AMPS) == len(vals), (len(vals), len(AMPS))
        with open(rundir / "det_law.csv", "w") as f:
            f.write("amplitude_at_load_vpk,vdet_v\n")
            for a, v in zip(AMPS, vals):
                f.write(f"{a},{v:.6e}\n")
        laws[key] = np.array(vals)
    A = np.array(AMPS)
    p_dbm = 10 * np.log10(A ** 2 / 100 * 1e3)
    for key, d in DET.items():
        rundir = RESULTS / d["run"]
        D = laws[key]
        fig, ax = plt.subplots(figsize=(8.5, 5.2))
        ax.loglog(A, D, "o-", label="LTspice, 146 MHz: " + d["label"])
        if key == "biased":
            ax.loglog(A, laws["zero"], "s-", color="0.6", ms=4, label="for comparison: " + DET["zero"]["label"])
        ax.loglog(A, D[5] * (A / A[5]) ** 2, "--", lw=0.8, label="square law through the 1 V point")
        ax.loglog(A, D[-2] * (A / A[-2]), ":", lw=0.8, label="linear law through the 5 W point")
        ax.axhline(4.5e-3, color="orange", lw=0.8)
        ax.text(0.06, 5.2e-3, "MCP6002 Vos 4.5 mV max", fontsize=7, color="orange")
        ax.axhline(10.6e-3, color="purple", lw=0.8)
        ax.text(0.06, 1.25e-2, "TS-012 idle-bias offset about 10.6 mV (10 k / 4.7 M)", fontsize=7, color="purple")
        ax.axvline(22.36, color="k", lw=0.6)
        ax.text(22.36, 2.5, " 5 W", fontsize=8)
        ax.set_xlabel("RF amplitude at the 50 ohm load (V peak)")
        ax.set_ylabel("detector output (V)")
        ax.set_title(f"ALC detector static law (run {d['run']})")
        ax.grid(True, which="both", lw=0.3)
        ax.legend(fontsize=7, loc="lower right")
        ax.set_ylim(1e-6, 5)
        ax2 = ax.twiny()
        ax2.set_xscale("log")
        ax2.set_xlim(ax.get_xlim())
        dbm_ticks = [-10, 0, 10, 20, 30, 37]
        ax2.set_xticks([math.sqrt(100 * 10 ** (t / 10) / 1e3) for t in dbm_ticks])
        ax2.set_xticklabels([str(t) for t in dbm_ticks])
        ax2.minorticks_off()
        ax2.set_xlabel("power at the load (dBm)")
        fig.tight_layout()
        fig.savefig(rundir / "det_law.png", dpi=130)
        plt.close(fig)
        blind = {}
        for off in (4.5e-3, 10.6e-3):
            blind[f"{off*1e3:.1f}mV"] = float(np.exp(np.interp(math.log(off), np.log(D), np.log(A))))
        res = {"run_id": d["run"], "deck": d["deck"], "detector": d["label"],
               "points": [{"amplitude_vpk": a, "power_dbm": round(float(p), 2), "vdet_v": float(v)}
                          for a, p, v in zip(AMPS, p_dbm, D)],
               "vdet_at_5W": float(np.interp(22.36, A, D)),
               "amplitude_where_output_equals_offset_vpk": blind,
               "note": "the loop cannot regulate below the amplitude at which the detector output equals the "
                       "loop offset (blind zone); 5 W is 22.36 V peak"}
        (rundir / "result.json").write_text(json.dumps(res, indent=1))
        shutil.copy(HERE / d["deck"], rundir / d["deck"])
        shutil.copy(Path(__file__), rundir / Path(__file__).name)
        print("detector law", key, res["amplitude_where_output_equals_offset_vpk"])


# ---------------------------------------------------------------- stage: deck generation
def corners(var):
    """(VSH, VOS) corners: PA threshold shift (V) and residual error-amplifier offset (V)."""
    return CORNERS_MITIG if VAR[var]["ff"] else [(0.0, 0.0)]


def run_params(fin, var):
    f, v = FIN[fin], VAR[var]
    A, D = det_law(v["det"])
    r = RIN / RIDLE
    rows = []
    for vsh, vos in corners(var):
        for vd in (f["vd_lo"], f["vd_hi"]):
            for tset in SETTINGS_MS:
                pset = 5.0
                if var == "mitig" and vd == f["vd_lo"]:
                    pset = f["pset_lo_mitig"]
                aset = math.sqrt(100 * pset)
                dset = float(det_of([aset], A, D)[0])
                vset = (dset + 5 * r) / (1 + r)
                rows.append(dict(tset_ms=tset, vd=vd, vsh=vsh, vos=vos, scale=f["scale"][vd], pset=pset,
                                 aset=aset, dset=dset, vset=vset))
    return rows


def gen_deck(fin, var):
    f, v = FIN[fin], VAR[var]
    rows = run_params(fin, var)
    A, D = det_law(v["det"])
    tab = dbm_table(f["table"])
    cf = f["cf_mitig"] if v["ff"] else f["cf_asis"]
    runtab = lambda key: spice_table([(i + 1, row[key]) for i, row in enumerate(rows)])  # noqa: E731
    # detector table in the deck: amplitude -> Vdet; below the first point the square law (0 at 0)
    # (a point at -1 V first: LTspice table() mis-evaluates an argument exactly equal to the first abscissa)
    dpts = [(-1.0, 0.0), (0.0, 0.0)] + [(a, d) for a, d in zip(A, D)]
    L = []
    L.append(f"* keying_{fin}_{var}.cir: keying envelope loop, TS-012 finalist {f['name']}, {v['name']}")
    L.append("* cwht WP-PDR-22 pre-order item; generated by hardware/sim/tx-keying/keying_run.py; record")
    L.append("* docs/design/analysis/keying-ts012.md. Envelope-domain behavioural deck (no RF carrier).")
    L.append("* Steps: 3, 5, 8 ms (10-90 %) at the low then the high drain voltage, for each corner in turn:")
    for i, (vsh, vos) in enumerate(corners(var)):
        L.append(f"*   runs {6 * i + 1}..{6 * i + 6}: PA curve shifted {vsh:+.1f} V, error-amplifier offset {vos * 1e3:+.1f} mV")
    L.append("* 50 WPM continuous dits: key down 24 ms, up 24 ms; relay command at key-down of element 1,")
    L.append("* contact closed at 7.5 ms; CLK1 and GVA-84+ bias on at 8 ms; ramp start 10 ms after each key-down;")
    L.append(f"* drive gated off {v['tg']*1e3:.0f} ms after each ramp end; VGG and integrator clamps applied at the gate.")
    L.append(f".param TPER={TPER} TDIT={TDIT} TLEAD={TLEAD} TCLK={TCLK} TC={TC} TQ={TQ} TG={v['tg']}")
    L.append(".param run=1")
    L.append(f".param TSET=table(run,{spice_table([(i + 1, row['tset_ms'] * 1e-3) for i, row in enumerate(rows)])})")
    L.append(f".param TR={{TSET/{RC_1090:.6f}}}")
    L.append(".param TE={TLEAD+TDIT+TR}")
    L.append(f".param SCALE=table(run,{runtab('scale')})")
    L.append(f".param VSH=table(run,{runtab('vsh')})")
    L.append(f".param VOS=table(run,{runtab('vos')})")
    L.append(f".param ASET=table(run,{runtab('aset')})")
    L.append(f".param VSET=table(run,{runtab('vset')})")
    L.append(f".param PLEAK={10 ** ((f['pleak_dbm'] - 30) / 10):.6g}")
    L.append(f".param LOSS={10 ** (-LOSS_DB / 10):.6f} KDIV={KDIV} KTRIM={KTRIM} KFF={KFF}")
    L.append(f".step param run 1 {len(rows)} 1")
    L.append(".func tm(x) {x-TPER*floor(x/TPER)}")
    L.append(".func rc(u) {if(u<TLEAD,0,if(u<TLEAD+TR,0.5*(1-cos(pi*(u-TLEAD)/TR)),"
             "if(u<TLEAD+TDIT,1,if(u<TE,0.5*(1+cos(pi*(u-TLEAD-TDIT)/TR)),0))))}")
    L.append(".func env(x) {rc(tm(floor(x/TQ)*TQ))}")
    L.append(".func wnd(u,a,b) {(u>=a)*(u<b)}")
    L.append(".func onw(x,a,b) {max(wnd(tm(x),a,b),(x>=TPER)*wnd(tm(x)+TPER,a,b))}")
    L.append("V5 v5 0 5")
    if not v["ff"]:
        L.append("* firmware reference: raised-cosine table x VSET, 12-bit PWM updated every 32.768 us, 2-pole RC")
        L.append("Bref refraw 0 V=VSET*env(time)")
    else:
        L.append("* firmware reference: raised-cosine amplitude table predistorted by the detector law (table of")
        L.append("* run 2026-09-28-det-char-biased), 12-bit PWM updated every 32.768 us, 2-pole RC")
        L.append(f"Bref refraw 0 V=table(ASET*env(time),{spice_table(dpts)})")
    L.append("R1 refraw r1 4.7k")
    L.append("C1 r1 0 10n")
    L.append("R2 r1 vref 4.7k")
    L.append("C2 vref 0 10n")
    if not v["ff"]:
        L.append("* error amplifier as TS-012 describes it (MCP6002 half on the 5 V bus): inverting integrator,")
        L.append("* reference on the non-inverting input, idle-bias resistor from +5 V on the inverting input")
        L.append("XU1 vref inn out v5 OPA")
        L.append(f"Rin detf inn {RIN:g}")
        L.append(f"Cf inn out {cf:.4g}")
        L.append(f"Ridle v5 inn {RIDLE:g}")
        L.append("* VGG node: divider Thevenin (0.654 = 5.1k/(2.7k+5.1k), 1.77 k), 10 nF")
        L.append("Bvt vt 0 V=KDIV*V(out)")
    else:
        L.append("* error amplifier: difference integrator about a 2.5 V mid-rail (bipolar trim), modelled as an ideal")
        L.append("* integrator with rails: V(out) = 2.5 V + integral of (Vref - Vdet + VOS)/(RIN*CF), limited to 0..5 V,")
        L.append("* reset to 2.5 V while parked; it does not load the reference or the detector (buffered inputs, e.g.")
        L.append("* an MCP6002 difference integrator with the spare half as buffer; WP-PDR-22 sets the circuit).")
        L.append("* VOS is the residual input offset after the firmware zero calibration.")
        L.append(f"Gi 0 xi value={{(V(vref)-V(detf)+VOS)/{RIN:g}}}")
        L.append(f"Ci xi 0 {cf:.4g}")
        L.append("Dih xi vh DI")
        L.append("Dil vl xi DI")
        L.append("Vh vh 0 2.485")
        L.append("Vl vl 0 -2.485")
        L.append("S2 xi 0 park 0 SWC")
        L.append("Bo out 0 V=2.5+V(xi)")
        L.append(".model DI D(Ron=1 Roff=1e12 Vfwd=0)")
        L.append("* feedforward VGG table (second 12-bit PWM, same update and 2-pole RC as the reference): the nominal")
        L.append("* inverse PA curve at the run's drain voltage for KFF of the wanted amplitude, 0 V when the table is 0")
        L.append(f"Bff ffraw 0 V=(env(time)>0)*max(table(10*log10(max((KFF*ASET*env(time))**2/100/LOSS/SCALE,1e-20)*1e3),"
                 f"{spice_table(sorted((d, vg) for vg, d in tab))}),0)")
        L.append("R3 ffraw f1 4.7k")
        L.append("C3 f1 0 10n")
        L.append("R4 f1 ff 4.7k")
        L.append("C4 ff 0 10n")
        L.append("* VGG node: feedforward plus the loop trim, KTRIM volts per volt of the error amplifier about")
        L.append("* mid-rail (+/-0.25 V authority), not below 0 V (Schottky clamp), 1.77 k, 10 nF")
        L.append("Bvt vt 0 V=max(KTRIM*(V(out)-2.5)+V(ff),0)")
    L.append(f"Rth vt vgg {RTH:g}")
    L.append(f"Cg vgg 0 {CVGG:g}")
    L.append("* clamps (open collector, on at reset): VGG node held low and integrator parked outside the window")
    L.append("* ramp start .. drive gate")
    L.append("Bpk park 0 V=1-onw(time,TLEAD,TE+TG)")
    L.append("S1 vgg 0 park 0 SWC")
    if not v["ff"]:
        L.append("S2 out inn park 0 SWC")
    L.append("S4 vref 0 park 0 SWC")
    L.append(".model SWC SW(Ron=10 Roff=1e9 Vt=0.5 Vh=0.05)")
    L.append("* PA static transfer (dBm at the reference drain voltage) scaled for the drain voltage, curve shifted")
    L.append("* by VSH (module-to-module threshold corner)")
    L.append(f"Bpg pg 0 V=SCALE*pow(10,(table(V(vgg)-VSH,{spice_table(tab)})-30)/10)")
    L.append("* drive gate: CLK1 enable and GVA-84+ bias, 10 us")
    L.append("Bd dr0 0 V=onw(time,TCLK,TE+TG)")
    L.append("Rd dr0 dr 1k")
    L.append("Cd dr 0 10n")
    L.append("* relay pole A contact (closes 7.5 ms after the relay command)")
    L.append("Bc cont 0 V=time>TC")
    L.append("* power and amplitude at the 50 ohm load (after 0.5 dB LPF and relay loss); PLEAK is the output with")
    L.append("* the gate off and the exciter driven (estimate, see the record)")
    L.append("Bpl pl 0 V=V(cont)*V(dr)*(V(pg)+PLEAK)*LOSS")
    L.append("Bal al 0 V=sqrt(100*max(V(pl),0))")
    if not v["ff"]:
        L.append("* detector static law from run 2026-09-28-det-char and its 22 us video pole (47 k, 470 pF)")
        L.append(f"Bdet d0 0 V=table(V(al),{spice_table(dpts)})")
        L.append("Rv d0 detf 1k")
        L.append("Cv detf 0 22n")
    else:
        L.append("* detector static law from run 2026-09-28-det-char-biased and its 4.7 us video pole (10 k, 470 pF)")
        L.append(f"Bdet d0 0 V=table(V(al),{spice_table(dpts)})")
        L.append("Rv d0 detf 1k")
        L.append("Cv detf 0 4.7n")
    L.append("* op-amp macro: gm stage, Aol 112 dB, GBW 1 MHz, internal node and output limited to the rails")
    L.append(".subckt OPA inp inn out vcc")
    L.append("G1 0 x inp inn 1m")
    L.append("Rx x 0 4e8")
    L.append("Cx x 0 159p")
    L.append("Dhi x vcc DI")
    L.append("Dlo 0 x DI")
    L.append("Bo o 0 V=limit(V(x),0.015,V(vcc)-0.015)")
    L.append("Ro o out 20")
    L.append(".model DI D(Ron=1 Roff=1e12 Vfwd=0)")
    L.append(".ends OPA")
    L.append(".save V(al) V(vgg) V(vref) V(detf)")
    L.append(f".tran 0 {NEL * TPER} 0 20u")
    L.append(".options reltol=1e-4")
    L.append(".end")
    name = f"keying_{fin}_{var}.cir"
    (HERE / name).write_text("\n".join(L) + "\n")
    return name, rows


# ---------------------------------------------------------------- analysis
def raised_cosine(t, t0, tr, rising=True):
    u = np.clip((t - t0) / tr, 0, 1)
    rc = 0.5 * (1 - np.cos(np.pi * u))
    return rc if rising else 1 - rc


def crossing(t, y, level, rising=True):
    if rising:
        idx = np.where((y[:-1] < level) & (y[1:] >= level))[0]
    else:
        idx = np.where((y[:-1] > level) & (y[1:] <= level))[0]
    if len(idx) == 0:
        return float("nan")
    i = idx[0]
    return float(t[i] + (level - y[i]) * (t[i + 1] - t[i]) / (y[i + 1] - y[i]))


def shape_error(t, an, tset, rising):
    """Max |normalized envelope - ideal raised cosine of the set 10-90 time|, best time alignment."""
    tr = tset / RC_1090
    t50 = crossing(t, an, 0.5, rising)
    best = 9.0
    for sh in np.linspace(-2e-3, 2e-3, 401):
        t0 = t50 - tr / 2 + sh
        ideal = raised_cosine(t, t0, tr, rising)
        m = (t > t0 - 3e-3) & (t < t0 + tr + 3e-3)
        e = float(np.max(np.abs(an[m] - ideal[m])))
        best = min(best, e)
    return best


def spectrum_metrics(tu, a):
    n = len(a)
    dt = tu[1] - tu[0]
    X = np.fft.fftshift(np.fft.fft(a)) / n
    f = np.fft.fftshift(np.fft.fftfreq(n, dt))
    P = np.abs(X) ** 2
    Ptot = P.sum()
    # 26 dB bandwidth (47 CFR 97.3(a)(8), power containment): smallest symmetric band with
    # P_outside <= P_inside * 10^-2.6
    af = np.abs(f)
    order = np.argsort(af)
    csum = np.cumsum(P[order])
    frac = 10 ** -2.6
    k = np.where((Ptot - csum) <= csum * frac)[0][0]
    bw26 = 2 * af[order][k]
    # 10 Hz cells relative to total mean power
    edges = np.arange(-50e3, 50e3 + 10, 10.0)
    cells, _ = np.histogram(f, bins=edges, weights=P)
    cc = 0.5 * (edges[:-1] + edges[1:])
    cells_db = 10 * np.log10(np.maximum(cells, 1e-30) / Ptot)
    beyond = np.abs(cc) > REQ["side_offset_hz"]
    side = float(np.max(cells_db[beyond]))
    fside = float(cc[beyond][np.argmax(cells_db[beyond])])
    # offset beyond which every cell is below -60 dB
    over = np.where(cells_db > REQ["side_db"])[0]
    off60 = float(np.max(np.abs(cc[over]))) if len(over) else 0.0
    return dict(bw26_hz=float(bw26), side_max_db=side, side_max_at_hz=fside, off60_hz=off60,
                f=f, P=P / Ptot, cc=cc, cells_db=cells_db)


def ideal_envelope(tu, tset):
    """Ideal raised-cosine keyed envelope of the same timing (the firmware table without PA or loop)."""
    tr = tset / RC_1090
    u = tu - TPER * np.floor(tu / TPER)
    return np.where(u < TLEAD, 0, np.where(u < TLEAD + tr, 0.5 * (1 - np.cos(np.pi * (u - TLEAD) / tr)),
                    np.where(u < TLEAD + TDIT, 1, np.where(u < TLEAD + TDIT + tr,
                             0.5 * (1 + np.cos(np.pi * (u - TLEAD - TDIT) / tr)), 0))))


def analyse(fin, var, rundir, rows):
    raw = RawRead(str(rundir / f"keying_{fin}_{var}.raw"))
    out = []
    fin_d = FIN[fin]
    for s, row in zip(raw.get_steps(), rows):
        t = np.abs(raw.get_trace("time").get_wave(s))
        a = raw.get_trace("V(al)").get_wave(s)
        vgg = raw.get_trace("V(vgg)").get_wave(s)
        vref = raw.get_trace("V(vref)").get_wave(s)
        vdet = raw.get_trace("V(detf)").get_wave(s)
        tset = row["tset_ms"] * 1e-3
        tr = tset / RC_1090
        dtu = 10e-6
        tu = np.arange(2 * TPER, NEL * TPER, dtu)
        au = np.interp(tu, t, a)
        # element 4 (index 3) for the time-domain checks
        k = 3
        kd = k * TPER
        flat = (tu > kd + TLEAD + tr + 2e-3) & (tu < kd + TLEAD + TDIT - 1e-3)
        atop = float(np.median(au[flat]))
        an = au / atop
        wr = (tu > kd + TLEAD - 3e-3) & (tu < kd + TLEAD + TDIT - 1e-3)
        wf = (tu > kd + TLEAD + TDIT - 3e-3) & (tu < kd + TPER)
        rise = crossing(tu[wr], an[wr], 0.9) - crossing(tu[wr], an[wr], 0.1)
        fall = crossing(tu[wf], an[wf], 0.1, False) - crossing(tu[wf], an[wf], 0.9, False)
        e_r = shape_error(tu[wr], an[wr], tset, True)
        e_f = shape_error(tu[wf], an[wf], tset, False)
        ov_db = 20 * math.log10(max(float(np.max(au)) / atop, 1e-9))
        sp = spectrum_metrics(tu, au)
        spi = spectrum_metrics(tu, ideal_envelope(tu, tset))
        # RF-off windows around key-up of element k: ramp end TE to gate TE+TG, then after the gate
        te = kd + TLEAD + TDIT + tr
        tg = te + VAR[var]["tg"]
        w1 = (t >= te) & (t < tg - 20e-6)
        w2 = (t >= tg + 0.2e-3) & (t < (k + 1) * TPER + TCLK - 0.1e-3)
        pdbm = 10 * np.log10(np.maximum(a ** 2 / 100, 1e-30) * 1e3)
        p_w1_max = float(np.max(pdbm[w1]))
        p_at_gate = float(np.interp(tg - 20e-6, t, pdbm))
        p_w2_max = float(np.max(pdbm[w2])) if np.any(w2) else float("nan")
        # loop tail alone: the modelled gate-off leakage (PLEAK, an estimate) removed
        pleak_w = 10 ** ((fin_d["pleak_dbm"] - 30) / 10) * 10 ** (-LOSS_DB / 10)
        ptail = np.maximum(a[w1] ** 2 / 100 - pleak_w, 1e-30)
        p_tail_max = float(10 * np.log10(np.max(ptail) * 1e3))
        p_tail_gate = float(10 * np.log10(max(float(np.interp(tg - 20e-6, t, a)) ** 2 / 100 - pleak_w, 1e-18) * 1e3))
        # amplitude step removed by the drive gate, relative to the top amplitude
        a_gate = float(np.interp(tg - 20e-6, t, a))
        res = dict(
            run=int(s) + 1, tset_ms=row["tset_ms"], vd=row["vd"], vsh=row["vsh"], vos=row["vos"], pset_w=row["pset"],
            ptop_w=atop ** 2 / 100, rise_ms=rise * 1e3, fall_ms=fall * 1e3,
            shape_err_rise=e_r, shape_err_fall=e_f, overshoot_db=ov_db,
            bw26_hz=sp["bw26_hz"], side_max_db=sp["side_max_db"], side_max_at_hz=sp["side_max_at_hz"],
            off60_hz=sp["off60_hz"], vgg_max=float(np.max(vgg)),
            ideal_bw26_hz=spi["bw26_hz"], ideal_side_max_db=spi["side_max_db"],
            keyup_window_max_dbm=p_w1_max, keyup_loop_tail_max_dbm=p_tail_max, loop_tail_at_gate_dbm=p_tail_gate, at_gate_dbm=p_at_gate, gate_step_rel_db=20 * math.log10(max(a_gate / atop, 1e-12)),
            after_gate_max_dbm=p_w2_max,
        )
        res["pass"] = dict(
            t1090=bool(abs(res["rise_ms"] - row["tset_ms"]) <= REQ["t1090_tol_ms"]
                       and abs(res["fall_ms"] - row["tset_ms"]) <= REQ["t1090_tol_ms"]),
            shape=bool(max(e_r, e_f) <= REQ["shape_tol"]),
            overshoot=bool(ov_db <= REQ["overshoot_db"]),
            bw26=bool(res["bw26_hz"] <= REQ["bw26_hz"]),
            sideband=bool(res["side_max_db"] <= REQ["side_db"]),
            # REQ-TX-014 read as the settled key-up state: the level just before the drive gate, 1 ms after the
            # ramp end (includes the modelled gate-off leakage PLEAK, an estimate)
            keyup_1uW=bool(p_at_gate <= REQ["keyup_dbm"]),
            vgg=bool(res["vgg_max"] <= REQ["vgg_max"]) if fin == "a5" else True,
            setpoint=bool(abs(10 * math.log10(res["ptop_w"] / row["pset"])) <= 0.5),
        )
        res["_trace"] = dict(t=t, a=a, vgg=vgg, vref=vref, vdet=vdet, tu=tu, an=an, sp=sp, spi=spi,
                             kd=kd, tr=tr, te=te, tg=tg, atop=atop, pdbm=pdbm)
        out.append(res)
    return out


def plots(fin, var, rundir, res):
    fin_d = FIN[fin]
    title = f"{fin.upper()} {VAR[var]['short']}"
    # --- envelope versus time: one element per setting, both drain voltages
    fig, axes = plt.subplots(3, 2, figsize=(13, 11), sharex=False)
    for i, tset in enumerate(SETTINGS_MS):
        for j, vd in enumerate((fin_d["vd_lo"], fin_d["vd_hi"])):
            r = [x for x in res if x["tset_ms"] == tset and x["vd"] == vd and x["vsh"] == 0 and x["vos"] == 0][0]
            tr_ = r["_trace"]
            ax = axes[i, j]
            t0 = tr_["kd"]
            m = (tr_["t"] >= t0 + 6e-3) & (tr_["t"] <= t0 + TPER + 2e-3)
            tt = (tr_["t"][m] - t0) * 1e3
            an = tr_["a"][m] / tr_["atop"]
            ax.plot(tt, an, lw=1.4, label="RF amplitude at the load (normalized)")
            # ideal raised cosine of the set time, aligned on the simulated 50 % points
            tu = tr_["tu"]
            anu = tr_["an"]
            tr = tr_["tr"]
            wr = (tu > t0 + TLEAD - 3e-3) & (tu < t0 + TLEAD + TDIT - 1e-3)
            wf = (tu > t0 + TLEAD + TDIT - 3e-3) & (tu < t0 + TPER)
            t50r = crossing(tu[wr], anu[wr], 0.5, True)
            t50f = crossing(tu[wf], anu[wf], 0.5, False)
            tg = np.linspace(t0 + 6e-3, t0 + TPER + 2e-3, 3000)
            if not (math.isnan(t50r) or math.isnan(t50f)):
                ideal = np.where(tg < t50r + tr / 2 + 1e-3, raised_cosine(tg, t50r - tr / 2, tr, True),
                                 raised_cosine(tg, t50f - tr / 2, tr, False))
                ax.plot((tg - t0) * 1e3, ideal, "k--", lw=0.8, label="ideal raised cosine (REQ-SYS-014)")
                ax.fill_between((tg - t0) * 1e3, ideal - 0.05, ideal + 0.05, color="k", alpha=0.08,
                                label="+/-5 % of full scale (TC-SYS-013)")
            ax.axvline(TLEAD * 1e3, color="g", lw=0.6)
            ax.axvline((tr_["te"] - t0) * 1e3, color="m", lw=0.6)
            ax.axvline((tr_["tg"] - t0) * 1e3, color="r", lw=0.8, ls=":")
            ax2 = ax.twinx()
            ax2.plot(tt, tr_["vgg"][m], color="tab:orange", lw=0.8, label="VGG (V)")
            ax2.plot(tt, tr_["vref"][m], color="tab:green", lw=0.8, label="reference (V)")
            ax2.set_ylim(0, 4)
            ax2.set_ylabel("VGG, reference (V)", fontsize=8)
            p = r["pass"]
            ax.set_title(f"{tset:.0f} ms, drain {vd} V: rise {r['rise_ms']:.2f} / fall {r['fall_ms']:.2f} ms "
                         f"(set {tset:.0f} +/-0.5); shape err {100*max(r['shape_err_rise'], r['shape_err_fall']):.1f} %; "
                         f"overshoot {r['overshoot_db']:.2f} dB",
                         fontsize=8, color="k" if (p['t1090'] and p['shape'] and p['overshoot']) else "r")
            ax.set_ylim(-0.05, 1.25)
            ax.set_xlabel("time from key-down (ms); green ramp start, magenta ramp end, red dotted drive gate",
                          fontsize=7)
            ax.set_ylabel("normalized amplitude")
            ax.grid(True, lw=0.3)
            if i == 0 and j == 0:
                h1, l1 = ax.get_legend_handles_labels()
                h2, l2 = ax2.get_legend_handles_labels()
                ax.legend(h1 + h2, l1 + l2, fontsize=7, loc="upper right")
    fig.suptitle(f"Keying envelope, {title}: 50 WPM dits, element 4", fontsize=11)
    fig.tight_layout()
    fig.savefig(rundir / "envelope.png", dpi=110)
    plt.close(fig)

    # --- spectrum with the requirement mask
    fig, axes = plt.subplots(3, 2, figsize=(13, 11))
    for i, tset in enumerate(SETTINGS_MS):
        for j, vd in enumerate((fin_d["vd_lo"], fin_d["vd_hi"])):
            r = [x for x in res if x["tset_ms"] == tset and x["vd"] == vd and x["vsh"] == 0 and x["vos"] == 0][0]
            sp = r["_trace"]["sp"]
            ax = axes[i, j]
            spi = r["_trace"]["spi"]
            m = harmonic_cells(sp["cc"])
            ax.plot(spi["cc"][m], spi["cells_db"][m], color="0.55", lw=0.6,
                    label="ideal raised cosine of the setting (no PA, no loop)")
            ax.plot(sp["cc"][m], sp["cells_db"][m], lw=0.9, color="tab:blue",
                    label="simulated RF envelope: 10 Hz cells holding a dit-rate line, rel. total power")
            ax.axvspan(-REQ["bw26_hz"] / 2, REQ["bw26_hz"] / 2, color="g", alpha=0.08,
                       label="REQ-SYS-015 350 Hz (26 dB bandwidth)")
            ax.axvline(-r["bw26_hz"] / 2, color="g", lw=0.8, ls="--")
            ax.axvline(r["bw26_hz"] / 2, color="g", lw=0.8, ls="--", label=f"26 dB bandwidth {r['bw26_hz']:.0f} Hz")
            mx = np.array([-5000, -750, -750, 750, 750, 5000])
            my = np.array([-60, -60, 0, 0, -60, -60])
            ax.plot(mx, my, "r", lw=1.2, label="REQ-TX-006 mask: -60 dB beyond 750 Hz")
            ax.set_xlim(-5000, 5000)
            ax.set_ylim(-120, 0)
            ok = r["pass"]["bw26"] and r["pass"]["sideband"]
            ax.set_title(f"{tset:.0f} ms, drain {vd} V: 26 dB BW {r['bw26_hz']:.0f} Hz; worst cell beyond 750 Hz "
                         f"{r['side_max_db']:.1f} dB at {r['side_max_at_hz']:.0f} Hz", fontsize=8,
                         color="k" if ok else "r")
            ax.set_xlabel("offset from carrier (Hz)")
            ax.set_ylabel("dB")
            ax.grid(True, lw=0.3)
            if i == 0 and j == 0:
                ax.legend(fontsize=7, loc="upper right")
    fig.suptitle(f"Keying spectrum, {title}: 50 WPM continuous dits (6 periods, elements 3 to 8)", fontsize=11)
    fig.tight_layout()
    fig.savefig(rundir / "spectrum.png", dpi=110)
    plt.close(fig)

    # --- RF level at key-up (log scale) with REQ-TX-014 and REQ-SYS-183
    fig, axes = plt.subplots(1, 3, figsize=(15, 4.6), sharey=True)
    for i, tset in enumerate(SETTINGS_MS):
        ax = axes[i]
        for vd in (fin_d["vd_lo"], fin_d["vd_hi"]):
            r = [x for x in res if x["tset_ms"] == tset and x["vd"] == vd and x["vsh"] == 0 and x["vos"] == 0][0]
            tr_ = r["_trace"]
            t0 = tr_["kd"]
            m = (tr_["t"] >= t0 + TLEAD + TDIT - 2e-3) & (tr_["t"] <= t0 + TPER + TCLK + 3e-3)
            ax.plot((tr_["t"][m] - t0) * 1e3, tr_["pdbm"][m], lw=1.0, label=f"drain {vd} V")
            ax.axvline((tr_["te"] - t0) * 1e3, color="m", lw=0.6)
            ax.axvline((tr_["tg"] - t0) * 1e3, color="r", lw=0.8, ls=":")
        ax.axhline(REQ["keyup_dbm"], color="orange", lw=1.2, label="REQ-TX-014 1 uW (-30 dBm)")
        ax.axhline(REQ["rfoff_dbm"], color="r", lw=1.2, label="REQ-SYS-183 -57 dBm")
        ax.set_ylim(-120, 45)
        ax.set_title(f"{tset:.0f} ms setting: magenta ramp end, red dotted drive gate", fontsize=9)
        ax.set_xlabel("time from key-down (ms)")
        ax.grid(True, lw=0.3)
        if i == 0:
            ax.set_ylabel("power at the load (dBm)")
            ax.legend(fontsize=7, loc="upper right")
    fig.suptitle(f"Key-up RF level, {title}. Below -100 dBm after the gate is the model floor (drive off); the real "
                 "floor is the estimate of the record.\nThe step at 56 ms is the next element's CLK1 enable "
                 "(backwave at the modelled gate-off leakage).", fontsize=9)
    fig.tight_layout()
    fig.savefig(rundir / "keyup_level.png", dpi=110)
    plt.close(fig)


def harmonic_cells(cc):
    """Cells whose centre lies within 5 Hz of a multiple of the 20.83 Hz dit-pair rate (for plotting only;
    the checks use every cell)."""
    k = np.round(cc * TPER)
    return np.abs(cc - k / TPER) <= 5.0


def plots_corners(fin, var, rundir, res):
    fin_d = FIN[fin]
    title = f"{fin.upper()} {VAR[var]['short']}"
    cols = ["tab:blue", "tab:red", "tab:green", "tab:purple", "tab:orange"]
    fig, axes = plt.subplots(3, 4, figsize=(17, 11))
    for i, tset in enumerate(SETTINGS_MS):
        for j, vd in enumerate((fin_d["vd_lo"], fin_d["vd_hi"])):
            axe, axs = axes[i, 2 * j], axes[i, 2 * j + 1]
            for ci, (vsh, vos) in enumerate(corners(var)):
                r = [x for x in res if x["tset_ms"] == tset and x["vd"] == vd and x["vsh"] == vsh
                     and x["vos"] == vos][0]
                tr_ = r["_trace"]
                t0 = tr_["kd"]
                m = (tr_["t"] >= t0 + 6e-3) & (tr_["t"] <= t0 + TPER + 2e-3)
                ok = all(r["pass"].values())
                axe.plot((tr_["t"][m] - t0) * 1e3, tr_["a"][m] / tr_["atop"], color=cols[ci], lw=1.0,
                         label=f"VSH {vsh:+.1f} V, VOS {vos*1e3:+.0f} mV: "
                               f"{'pass' if ok else 'FAIL ' + ','.join(k for k, v in r['pass'].items() if not v)}")
                sp = tr_["sp"]
                mm = harmonic_cells(sp["cc"])
                axs.plot(sp["cc"][mm], sp["cells_db"][mm], color=cols[ci], lw=0.7)
            axe.set_title(f"{tset:.0f} ms, drain {vd} V: envelope", fontsize=8)
            axe.set_ylim(-0.05, 1.25)
            axe.grid(True, lw=0.3)
            axe.legend(fontsize=6, loc="upper right")
            axe.set_xlabel("ms from key-down", fontsize=7)
            axs.plot([-5000, -750, -750, 750, 750, 5000], [-60, -60, 0, 0, -60, -60], "r", lw=1.0)
            axs.axvspan(-175, 175, color="g", alpha=0.08)
            axs.set_xlim(-3000, 3000)
            axs.set_ylim(-120, 0)
            axs.grid(True, lw=0.3)
            axs.set_title(f"{tset:.0f} ms, drain {vd} V: spectrum, REQ-TX-006 mask (red), 350 Hz (green)",
                          fontsize=8)
            axs.set_xlabel("Hz from carrier", fontsize=7)
    fig.suptitle(f"{title}: corners (PA curve shifted -0.1, 0, +0.1 V; residual loop offset -1, 0, +1 mV)",
                 fontsize=10)
    fig.tight_layout()
    fig.savefig(rundir / "corners.png", dpi=105)
    plt.close(fig)


def stage_deck(fin, var, rerun=True):
    """rerun=False (stage 'replot') analyses and plots the existing .raw of the run without running LTspice;
    the deck must be unchanged (its SHA-256 is checked against the copy in the run directory)."""
    name, rows = gen_deck(fin, var)
    run_id = f"{DATE}-{fin}-{var}"
    rundir = RESULTS / run_id
    rundir.mkdir(parents=True, exist_ok=True)
    if rerun:
        cmd = [str(WRAPPER), "-t", "600", "-o", str(rundir), "-b", str(HERE / name)]
        p = subprocess.run(cmd, capture_output=True, text=True)
        (rundir / "wrapper.txt").write_text(p.stderr[-4000:])
        print(p.stderr.strip().splitlines()[-1])
        if p.returncode != 0:
            sys.exit(f"LTspice run failed ({p.returncode})")
    elif (HERE / name).read_bytes() != (rundir / name).read_bytes():
        sys.exit("replot refused: the generated deck differs from the deck of the run; rerun the deck")
    res = analyse(fin, var, rundir, rows)
    plots(fin, var, rundir, res)
    if len(corners(var)) > 1:
        plots_corners(fin, var, rundir, res)
    clean = [{k: v for k, v in r.items() if k != "_trace"} for r in res]
    allpass = {k: all(r["pass"][k] for r in clean) for k in clean[0]["pass"]}
    summary = dict(run_id=run_id, finalist=FIN[fin]["name"], variant=VAR[var]["name"], deck=name,
                   limits=REQ, leakage_dbm_modelled=FIN[fin]["pleak_dbm"],
                   leakage_dbm_best_estimate=FIN[fin]["pleak_best_dbm"],
                   subthreshold_slope_db_per_v=SUBTH_DB_PER_V, steps=clean, all_steps_pass=allpass)
    (rundir / "result.json").write_text(json.dumps(summary, indent=1))
    keys = ["run", "tset_ms", "vd", "vsh", "vos", "pset_w", "ptop_w", "rise_ms", "fall_ms", "shape_err_rise", "shape_err_fall",
            "overshoot_db", "bw26_hz", "side_max_db", "side_max_at_hz", "off60_hz", "vgg_max",
            "keyup_window_max_dbm", "keyup_loop_tail_max_dbm", "loop_tail_at_gate_dbm", "at_gate_dbm",
            "gate_step_rel_db", "ideal_bw26_hz", "ideal_side_max_db"]
    with open(rundir / "result.csv", "w") as f:
        f.write(",".join(keys + ["pass_" + k for k in clean[0]["pass"]]) + "\n")
        for r in clean:
            f.write(",".join(f"{r[k]:.4g}" if isinstance(r[k], float) else str(r[k]) for k in keys)
                    + "," + ",".join("PASS" if r["pass"][k] else "FAIL" for k in r["pass"]) + "\n")
    shutil.copy(HERE / name, rundir / name)
    shutil.copy(Path(__file__), rundir / Path(__file__).name)
    for r in clean:
        print(f"run {r['run']} {r['tset_ms']} ms VD {r['vd']} VSH {r['vsh']:+.1f} VOS {r['vos']*1e3:+.0f}m: top {r['ptop_w']:.2f} W rise {r['rise_ms']:.2f} "
              f"fall {r['fall_ms']:.2f} shape {100*max(r['shape_err_rise'], r['shape_err_fall']):.1f}% "
              f"ov {r['overshoot_db']:.2f} dB bw26 {r['bw26_hz']:.0f} side {r['side_max_db']:.1f}@{r['side_max_at_hz']:.0f} "
              f"keyup {r['keyup_window_max_dbm']:.1f} tail {r['keyup_loop_tail_max_dbm']:.1f}/{r['loop_tail_at_gate_dbm']:.1f} gate {r['at_gate_dbm']:.1f} vgg {r['vgg_max']:.2f} "
              f"{'' if all(r['pass'].values()) else 'FAIL:' + ','.join(k for k, v in r['pass'].items() if not v)}")


def rc2_gain(f, r=4.7e3, c=10e-9):
    """|H| of the loaded 2-section RC ladder (R1 C1 R2 C2, equal parts) at frequency f."""
    w = 2 * math.pi * f
    zc = 1 / (1j * w * c)
    z2 = r + zc                      # second section seen from node 1
    z1 = zc * z2 / (zc + z2)         # node 1 to ground
    v1 = z1 / (r + z1)
    return abs(v1 * zc / z2)


def pwm_ripple():
    """PWM carrier sidebands on the RF output (analytic; the decks model the duty staircase, not the carrier).
    Worst duty 0.5: fundamental amplitude (2/pi)*3.3 V; through the 2-pole 4.7 k / 10 nF filter; on the VGG
    path also the VGG node pole (1.77 k, 10 nF); on the reference path through the closed loop (|T| about
    fc/f with fc 1.5 kHz) and the detector slope at 5 W. Sideband level = 20 log10(dA / (2 A)) re carrier."""
    out = []
    fc_loop = 1.5e3
    for fin in ("a4", "a5"):
        f = FIN[fin]
        tab = f["table"]
        vg = np.array([v for v, _ in tab])
        pw = np.array([p for _, p in tab]) * max(f["scale"].values())
        amp = np.sqrt(100 * pw * 10 ** (-LOSS_DB / 10))
        slope = float(np.max(np.diff(amp) / np.diff(vg)))   # V of RF amplitude per V of VGG, steepest
        A, D = det_law("biased")
        dslope = float((D[-2] - D[-3]) / (A[-2] - A[-3]))    # detector slope near 5 W (V per V)
        for fpwm, bits in ((30.5e3, 12), (61.0e3, 11), (122.1e3, 10)):
            v1 = (2 / math.pi) * 3.3 * rc2_gain(fpwm)
            vgg_node = 1 / abs(1 + 1j * 2 * math.pi * fpwm * RTH * CVGG)
            # feedforward path: the FF PWM spans VGG directly (0 to 3.3 V)
            dA_ff = v1 * vgg_node * slope
            sb_ff = 20 * math.log10(dA_ff / (2 * 22.36))
            # reference path: ripple on the reference -> closed loop -> detector-equivalent -> amplitude
            dA_ref = v1 * (fc_loop / fpwm) / dslope
            sb_ref = 20 * math.log10(dA_ref / (2 * 22.36))
            out.append(dict(finalist=fin, pwm_hz=fpwm, bits=bits, filter_gain=rc2_gain(fpwm),
                            pa_slope_v_per_v=slope, ff_sideband_dbc=sb_ff, ref_sideband_dbc=sb_ref))
    return out


def loop_margin():
    """Small-signal loop gain of the mitigated loop at each point of the PA table (analytic, first order):
    L(s) = KTRIM * dA/dVGG * dVdet/dA / (s RIN CF) / (1 + s tau_vgg) / (1 + s tau_det). Returns the
    crossover and phase margin at the steepest point and at the 5 W point."""
    out = []
    A, D = det_law("biased")
    for fin in ("a4", "a5"):
        f = FIN[fin]
        rc = RIN * f["cf_mitig"]
        for vd, sc in f["scale"].items():
            vg = np.array([v for v, _ in f["table"]])
            amp = np.sqrt(100 * np.array([p for _, p in f["table"]]) * sc * 10 ** (-LOSS_DB / 10))
            da = np.diff(amp) / np.diff(vg)
            am = 0.5 * (amp[1:] + amp[:-1])
            dd = np.interp(am, 0.5 * (A[1:] + A[:-1]), np.diff(D) / np.diff(A))
            k = KTRIM * da * dd
            for label, i in (("steepest", int(np.argmax(k))), ("near 5 W", int(np.argmin(np.abs(am - 22.36))))):
                wc = k[i] / rc
                pm = 90 - math.degrees(math.atan(wc * RTH * CVGG)) - math.degrees(math.atan(wc * 1e3 * 4.7e-9))
                out.append(dict(finalist=fin, drain_v=vd, point=label, amplitude_v=float(am[i]),
                                crossover_hz=float(wc / 2 / math.pi), phase_margin_deg=float(pm)))
    return out


def stage_summary():
    runs = {}
    for fin in ("a4", "a5"):
        for var in ("asis", "mitig"):
            p = RESULTS / f"{DATE}-{fin}-{var}" / "result.json"
            runs[(fin, var)] = json.loads(p.read_text())
    outdir = RESULTS / f"{DATE}-summary"
    outdir.mkdir(exist_ok=True)
    # worst case over drain voltage and corners, per setting
    fig, axes = plt.subplots(1, 3, figsize=(16, 5.2))
    groups = [(k, s_) for k, s_ in runs.items()]
    metrics = (("bw26_hz", REQ["bw26_hz"], "Hz", "26 dB bandwidth, worst case (REQ-SYS-015 <= 350 Hz)", (0, 600)),
               ("side_max_db", REQ["side_db"], "dB rel. total mean power",
                "worst 10 Hz cell beyond 750 Hz (REQ-TX-006 <= -60 dB)", (-100, -30)),
               ("at_gate_dbm", REQ["keyup_dbm"], "dBm",
                "level 1 ms after ramp end, at the drive gate (REQ-TX-014 <= -30 dBm)", (-40, 20)))
    setcols = {3.0: "tab:blue", 5.0: "tab:orange", 8.0: "tab:purple"}
    for ax, (key, lim, yl, t, ylim) in zip(axes, metrics):
        for gi, ((fin, var), s_) in enumerate(groups):
            for si, tset in enumerate(SETTINGS_MS):
                val = max(st[key] for st in s_["steps"] if st["tset_ms"] == tset)
                x = gi * 4 + si
                ok = val <= lim
                ax.bar(x, val - ylim[0], bottom=ylim[0], color=setcols[tset], edgecolor="k" if ok else "r",
                       linewidth=0.5 if ok else 2.0, label=f"{tset:.0f} ms setting" if gi == 0 else None)
                ax.text(x, val + 0.01 * (ylim[1] - ylim[0]), "ok" if ok else "FAIL", ha="center", fontsize=6,
                        color="k" if ok else "r")
        ax.axhline(lim, color="r", lw=1.2)
        ax.set_xticks([gi * 4 + 1 for gi in range(len(groups))])
        ax.set_xticklabels([f"{fin.upper()}\n{VAR[var]['short']}" for (fin, var), _ in groups], fontsize=8)
        ax.set_ylim(*ylim)
        ax.set_ylabel(yl)
        ax.set_title(t, fontsize=9)
        ax.grid(True, axis="y", lw=0.3)
    axes[0].legend(fontsize=8, loc="upper left")
    fig.suptitle("TS-012 keying analysis: worst case over drain voltage and corners, per envelope setting "
                 "(red outline = fails the requirement)", fontsize=10)
    fig.tight_layout()
    fig.savefig(outdir / "summary.png", dpi=120)
    plt.close(fig)
    summ = {f"{fin}-{var}": dict(all_steps_pass=s["all_steps_pass"],
                                 bw26_hz_max=max(st["bw26_hz"] for st in s["steps"]),
                                 side_db_max=max(st["side_max_db"] for st in s["steps"]),
                                 keyup_at_gate_dbm_max=max(st["at_gate_dbm"] for st in s["steps"]),
                                 loop_tail_at_gate_dbm_max=max(st["loop_tail_at_gate_dbm"] for st in s["steps"]),
                                 shape_err_max=max(max(st["shape_err_rise"], st["shape_err_fall"]) for st in s["steps"]),
                                 t1090_err_ms_max=max(max(abs(st["rise_ms"] - st["tset_ms"]), abs(st["fall_ms"] - st["tset_ms"]))
                                                      for st in s["steps"]),
                                 steps=len(s["steps"]))
            for (fin, var), s in runs.items()}
    rip = pwm_ripple()
    summ["pwm_ripple"] = rip
    summ["loop_margin_mitigated"] = loop_margin()
    fig, ax = plt.subplots(figsize=(9, 4.8))
    labs, vals, cols = [], [], []
    for r in rip:
        for path, key in (("feedforward", "ff_sideband_dbc"), ("reference", "ref_sideband_dbc")):
            labs.append(f"{r['finalist'].upper()} {path}\n{r['pwm_hz']/1e3:.1f} kHz ({r['bits']}-bit)")
            vals.append(r[key])
            cols.append("tab:green" if r[key] <= REQ["side_db"] else "tab:red")
    x = np.arange(len(labs))
    ax.bar(x, np.array(vals) + 120, bottom=-120, color=cols)
    ax.axhline(REQ["side_db"], color="k", lw=1.2, label="REQ-TX-006: -60 dB beyond 750 Hz")
    ax.set_xticks(x)
    ax.set_xticklabels(labs, rotation=90, fontsize=7)
    ax.set_ylabel("PWM carrier sideband (dBc, each side)")
    ax.set_ylim(-120, 0)
    ax.grid(True, axis="y", lw=0.3)
    ax.legend(fontsize=8)
    ax.set_title("Mitigated loop: PWM carrier sidebands at duty 0.5 (analytic; green pass, red fail)", fontsize=9)
    fig.tight_layout()
    fig.savefig(outdir / "pwm_ripple.png", dpi=120)
    plt.close(fig)
    (outdir / "summary.json").write_text(json.dumps(summ, indent=1))
    shutil.copy(Path(__file__), outdir / Path(__file__).name)
    print(json.dumps(summ, indent=1))


if __name__ == "__main__":
    if sys.argv[1] == "detchar":
        stage_detchar()
    elif sys.argv[1] == "deck":
        stage_deck(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == "replot":
        stage_deck(sys.argv[2], sys.argv[3], rerun=False)
    elif sys.argv[1] == "summary":
        stage_summary()
    else:
        sys.exit(__doc__)
