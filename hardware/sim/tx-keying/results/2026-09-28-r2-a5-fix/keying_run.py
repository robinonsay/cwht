#!/usr/bin/env python3
"""Keying envelope and key-click analysis for the TS-012 finalists A4 and A5 (WP-PDR-22 pre-order item).

cwht, hardware/sim/tx-keying. Analysis record: docs/design/analysis/keying-ts012.md.

Revision 1 (review of revision 0, Major findings 1 to 3): power steps 0.5, 1, 2 and 5 W and packs 6.4, 7.4 and
8.4 V; threshold corners from a sourced budget (THRESHOLD_BUDGET) and a threshold sweep; the A5 PA table from
the project's digitized curves; every element checked, element 1 on its own; REQ-TX-005 (+/-10 %) asserted
separately from TC-SYS-013 (+/-0.5 ms). Run ids were 2026-09-28-r1-*; the revision 0 run folders stay, superseded.

Revision 2 (review of revision 1, INSP-116 iteration 2, finding-10 to finding-14): run ids 2026-09-28-r2-*
(the r1 folders stay, superseded). The threshold budget takes the die maximum and the die-to-NTC difference per
finalist from thermal-ts012.md (sections 4.1 and 8 change 6) and the NTC coefficient residual on both sides
(finding-12); the 'fix' record runs add the stored-trim corners; a new variant 'sens' sweeps VSH in 0.02 V steps
for element 1 with the residual offset, the 6.4 and 8.4 V packs and sub-threshold slopes of 65 and 150 dB/V
(finding-13); every stage compares its FAIL states with expected_states.json and exits 3 on a difference
(finding-11); the 'setpoint' criterion is labelled as this analysis's model-health check (finding-11).

Stages (run in order; each writes into results/<run-id>/):
  detchar           read the LTspice runs of det_char.cir (TS-012 zero-bias detector) and det_char_biased.cir
                    (biased detector with reference diode) in results/2026-09-28-det-char*/: static law of each
                    1N5711W ALC detector at 146 MHz -> det_law.csv, det_law.png, result.json
  deck FIN VAR      generate keying_FIN_VAR.cir (FIN = a4 | a5; VAR = asis: the loop as TS-012 rev. 4 writes it;
                    sweep0: revision 0 mitigated design, threshold sweep; fix: revision 1 design over every step,
                    pack, setting and the record corners; sweep1: revision 1 design, threshold sweep), run it through
                    tools/ltspice-batch.sh, analyse the .raw (spicelib), write result.json and result.csv (pass/fail
                    per criterion and run) and the plots (envelope, spectrum, keyup_level, corners and t1090 for
                    fix; window for the sweeps), and copy the deck and this script into the run directory
  replot FIN VAR    as deck, from the existing .raw of the run, without running LTspice (deck must be unchanged)
                    (VAR sens, revision 2: element 1 only, 7 sensitivity cases x 31 VSH x 4 steps x 3 settings;
                    plots sens_curves.png and sens_windows.png)
  summary           cross-run summary.png, windows.png and summary.json, the analytic PWM carrier ripple
                    (pwm_ripple.png), the analytic loop margin of the revision 1 loop, and (revision 2) the
                    element-1 windows of every sensitivity case against every threshold budget (margins)

Exit status (revision 2, finding-11; 08 section 3.4, CK-ANA-E4): 0 when every FAIL state of the run equals the
expected FAIL states recorded for its run id in expected_states.json (with the reason); 3 when a criterion fails
that is not expected, or an expected FAIL now passes (both are printed); 2 on a tool error (LTspice wrapper).
The summary stage also exits 3 if the design rules it checks fail (feedforward PWM at 122 kHz, phase margin).
'deck FIN VAR --accept' writes the run's FAIL states into expected_states.json; it refuses when a criterion that
the design must pass fails (FORBIDDEN_FAIL below). The file is committed and reviewed with the results.

Every LTspice run goes through tools/ltspice-batch.sh (ACC-LTSPICE-001); the GUI is never opened.

Model (envelope domain; the 146 MHz carrier is simulated only in the detector decks):
  VAR asis (TS-012 revision 4 section 7.3 as written): firmware raised-cosine table x setpoint -> 12-bit PWM
  updated every 32.768 us -> 2-pole RC -> MCP6002 inverting integrator (macro: GBW 1 MHz, rails 0 to 5 V;
  Rin 10 k, Cf, idle bias 4.7 M to +5 V) -> 0.654 divider (1.77 k Thevenin, 10 nF on the VGG node) -> PA static
  transfer P(VGG) from the datasheet graph (dBm table, scaled for drain voltage) x drive gate (CLK1 and GVA-84+
  bias, 10 us) x relay contact -> 0.5 dB LPF and relay loss -> amplitude at the 50 ohm load -> zero-bias
  detector static law -> 22 us video pole -> integrator.
  VAR sweep0 (revision 0 mitigated design): the same PA, gate and contact, plus a feedforward VGG table (second
  PWM channel, nominal inverse PA curve), the loop as a bipolar trim of +/-0.25 V (ideal difference integrator
  about mid-rail with rails, reset while parked), a biased detector with a reference diode (4.7 us video pole),
  a reference table predistorted by that detector's law and a firmware setpoint limited at the low pack end.
  VAR fix and sweep1 (revision 1 design): as sweep0, but the trim is held between elements (integrator input
  opened while parked, no reset; mid-rail at power-on), its authority is +/-0.4 V, and the detector tap is
  switched up 7 dB at the 0.5 and 1 W steps. Corners: PA curve shift VSH (threshold budget) and residual
  error-amplifier offset VOS (+/-1 mV).
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
PADATA = REPO / "hardware" / "sim" / "tx-pa" / "data"
DETRUN = RESULTS / "2026-09-28-det-char"
DATE = "2026-09-28"
REV = "r2"   # revision 2 of the analysis (INSP-116 finding-10 to 14); the r1 and revision 0 run folders stay, superseded

# ---------------------------------------------------------------- requirement limits
REQ = {
    "bw26_hz": 350.0,          # REQ-SYS-015: 26 dB bandwidth (97.3(a)(8) power containment) <= 350 Hz (TBR)
    "side_offset_hz": 750.0,   # REQ-TX-006: every 10 Hz cell beyond 750 Hz ...
    "side_db": -60.0,          # ... at least 60 dB below total mean power (TBR)
    "t1090_rel_tol": 0.10,     # REQ-TX-005 / TC-TX-005: 10-to-90 % times within +/-10 % (TBR) of the command
    "t1090_tol_ms": 0.5,       # TC-SYS-013: 10-to-90 % time equal to the setting within +/-0.5 ms
    "shape_tol": 0.05,         # TC-SYS-013: normalized envelope within 5 % of full scale of the ideal
    "overshoot_db": 0.2,       # TS-012 section 7.3 WP-PDR-22 criterion
    "setpoint_db": 0.5,        # NOT a requirement: this analysis's model-health check that the loop reaches the
                               # (pack-limited) setpoint within 0.5 dB, i.e. no windup; REQ-SYS-012 itself is
                               # +/-1 dB of 5 W and is not assessed here (revision 2, finding-11 (c))
    "vgg_max": 3.5,            # RA07M1317M rating condition (Pout 10 W at VGG <= 3.5 V); A5 only
    "keyup_dbm": -30.0,        # REQ-TX-014: <= 1 uW with TX_KEY deasserted, PA_EN asserted, exciter driven
    "rfoff_dbm": -57.0,        # REQ-SYS-183: <= -57 dBm in every RF-ended state
}

# ---------------------------------------------------------------- PA transfer tables
# A5: Mitsubishi RA07M1317M datasheet (publication Jun. 2019), page 5 "Output power, drain current versus
# gate voltage", VDD 7.2 V, Pin 20 mW. Revision 1 (review finding-2 (iv)): the project's digitized curves
# (hardware/sim/tx-pa/data/ra07_pout_vs_vgg_135.csv and _155.csv, digitize_ra07.py, overlays inspected there)
# averaged for 146 MHz on a 0.02 V grid from 2.32 V (below it the trace is the graph floor, about 0.07 W, the
# line width); revision 0's hand read sat up to 0.1 V off them. Below 2.32 V the table continues with an
# ESTIMATED 100 dB/V sub-threshold slope (the digitized foot is 63 to 71 dB/V; sensitivity in the record).
def _a5_digitized():
    a = np.loadtxt(PADATA / "ra07_pout_vs_vgg_135.csv", delimiter=",", skiprows=1)
    b = np.loadtxt(PADATA / "ra07_pout_vs_vgg_155.csv", delimiter=",", skiprows=1)
    vv = [round(2.32 + 0.02 * i, 2) for i in range(0, 55)] + [3.5, 3.6, 3.7, 3.8, 3.9]
    vv = sorted(set(v for v in vv if v <= 3.9))
    return [(v, round(float(0.5 * (np.interp(v, a[:, 0], a[:, 1]) + np.interp(v, b[:, 0], b[:, 1]))), 4))
            for v in vv]


def _a5_vdd_scale(vds):
    """Pout(VD) / Pout(7.2 V) from the digitized Pout versus VDD curves (VGG 3.5 V, Pin 20 mW), mean of 135
    and 155 MHz; applied to the whole VGG curve (assumption: the curve shape does not move with VDD)."""
    out = {}
    cs = [np.loadtxt(PADATA / f"ra07_pout_vs_vdd_{f}.csv", delimiter=",", skiprows=1) for f in (135, 155)]
    for vd in vds:
        out[vd] = float(np.mean([np.interp(vd, c[:, 0], c[:, 1]) / np.interp(7.2, c[:, 0], c[:, 1]) for c in cs]))
    return out


A5_W = _a5_digitized()
# drain voltage after key-down sag at the 6.4, 7.4 and 8.4 V pack (TS-012 section 7.3: 5.5 to 5.9 V at 6.4 V,
# 7.9 V at 8.4 V; 6.7 V at 7.4 V interpolated). The full-power sag is used at every step (conservative for
# the setpoint, immaterial for the shape: the feedforward table uses the same measured pack voltage).
A5_SCALE = _a5_vdd_scale((5.5, 6.7, 7.9))
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
A4_SCALE = {vd: (vd / 7.5) ** 2 * (3.6 / 6.45) / (6.1 / 7.5) ** 2 for vd in (6.1, 7.1, 8.1)}

SUBTH_DB_PER_V = 100.0  # ESTIMATE, see above

# power steps (REQ-SYS-011: 0.5, 1 and 2 W; REQ-SYS-012: 5 W; REQ-SYS-064: 1 W is the default) and the pack
# voltages of TC-TX-005 (6.4, 7.4 and 8.4 V)
STEPS_W = [0.5, 1.0, 2.0, 5.0]
PACKS_V = [6.4, 7.4, 8.4]

FIN = {
    "a5": dict(
        name="A5 (RA07M1317M module, VGG loop)", table=A5_W, scale=A5_SCALE, vd={6.4: 5.5, 7.4: 6.7, 8.4: 7.9},
        # leakage with VGG = 0 and the exciter driven: 20 mW in, module isolation 30 dB (TS-012 section 7.3
        # backwave figure; the datasheet says the input "attenuates up to 60 dB", not a guaranteed limit)
        pleak_dbm=-17.0, pleak_best_dbm=13.0 - 60.0,
        cf_asis=16e-9, cf_mitig=2.8e-9, vcap=3.46,
    ),
    "a4": dict(
        name="A4 (AFT05MS004N discrete, gate-bias loop)", table=A4_W, scale=A4_SCALE, vd={6.4: 6.1, 7.4: 7.1, 8.4: 8.1},
        # leakage with VGS = 0 and the GVA-84+ driving 0.1 W: current through Crss (1.63 pF at 7.5 V,
        # datasheet Table 5) from a gate swing of about 2 V peak into the 2.56 ohm load line: about -19 dBm
        # (ESTIMATE, derived in the record)
        pleak_dbm=-19.0, pleak_best_dbm=-23.0,
        cf_asis=7e-9, cf_mitig=1.2e-9, vcap=3.0,
    ),
}


def pset_for(fin, vd, step, var):
    """Firmware setpoint: the step, limited at a low pack voltage to 90 % of what the PA makes at the VGG cap
    (rounded down to 0.1 W; design change 5 of the record). The as-written loop has no limit."""
    if var == "asis":
        return step
    f = FIN[fin]
    tab = f["table"]
    pmax = f["scale"][vd] * float(np.interp(f["vcap"], [v for v, _ in tab], [p for _, p in tab])) \
        * 10 ** (-LOSS_DB / 10)
    return min(step, math.floor(10 * 0.9 * pmax) / 10)


# Threshold corner (VSH, volts): the PA table is evaluated at VGG - VSH, so VSH < 0 moves the curve to lower
# VGG (earlier onset: lower threshold, more drive, hotter die) and VSH > 0 the other way; the firmware
# feedforward table keeps the nominal curve. Revision 1 derives the corners from the budget THRESHOLD_BUDGET
# (sourced terms, record section 3.2) instead of revision 0's unsourced +/-0.1 V, and adds a sweep of VSH.
VSH_SWEEP = [round(-0.30 + 0.05 * i, 2) for i in range(13)]   # -0.30 .. +0.30 V
# VOS: residual error-amplifier offset after the firmware zero calibration (ESTIMATE: one 12-bit ADC step at
# 3.3 V is 0.8 mV). VOS > 0 acts like VSH < 0 (the integrator runs up), so the record corners pair them.

# Sensitivity cases of element 1 (revision 2, finding-13), variant 'sens': (label, pack V, VOS V, sub-threshold
# slope below the graphs in dB/V, ESTIMATE range: the digitized A5 foot is 63 to 71 dB/V). The firmware
# feedforward table follows the same slope in each case: the per-unit calibration of item 7 reads the curve down
# to the biased detector's visibility floor (-35.5 dB re 5 W, about 1.4 mW), below the graphs' foot (0.11 W A5,
# 0.05 W A4), so the firmware knows the unit's foot; the case changes how steeply the PA responds there to the
# residual shift VSH. VOS > 0 acts like VSH < 0, so the offset window is the low edge of "+1 mV" with the high
# edge of "-1 mV".
SENS_CASES = [("nominal", 7.4, 0.0, 100.0), ("VOS +1 mV", 7.4, 1e-3, 100.0), ("VOS -1 mV", 7.4, -1e-3, 100.0),
              ("pack 6.4 V", 6.4, 0.0, 100.0), ("pack 8.4 V", 8.4, 0.0, 100.0),
              ("slope 65 dB/V", 7.4, 0.0, 65.0), ("slope 150 dB/V", 7.4, 0.0, 150.0)]
VSH_FINE = [round(-0.30 + 0.02 * i, 2) for i in range(31)]   # -0.30 .. +0.30 V in 0.02 V


TPER_S = 48e-3   # one dit period (element 1 only)
_MITIG = dict(tg=1e-3, pred=True, ff=True, det="biased", ktrim=0.1, hold=False, boost=False)
VAR = {
    "asis": dict(short="as written (TS-012 rev. 4)", name="as written in TS-012 revision 4", tg=1e-3, pred=False,
                 ff=False, det="zero", steps=[5.0], packs=[6.4, 8.4], corners=[(0.0, 0.0)],
                 save="V(al) V(vgg) V(vref) V(detf)", tstart=0.0),
    # revision 0 mitigated design (record section 5.2 items 1 to 6): threshold sweep at the 7.4 V pack, every
    # step and setting; its trim integrator is reset at every element, so every element is a "first" element
    "sweep0": dict(_MITIG, short="rev. 0 mitigated design, threshold sweep",
                   name="revision 0 mitigated design (trim reset at every element), threshold sweep at 7.4 V pack",
                   steps=[0.5, 5.0], packs=[7.4], corners=[(v, 0.0) for v in VSH_SWEEP], save="V(al)", tstart=0.095),
    # revision 1 design (section 5.2 items 1 to 10): the trim integrator is held between elements instead of
    # reset (item 9), its authority is +/-0.4 V (KTRIM 0.16, Cf scaled to keep the loop gain), and the detector
    # tap is switched up 7 dB at the 0.5 and 1 W steps (item 10). Element 1 starts with the trim at mid-rail,
    # the state after power-on (or a stale hold), and is reported on its own.
    "fix": dict(_MITIG, short="rev. 1 design", name="revision 1 design (held trim +/-0.4 V, detector tap +7 dB "
                                                    "at 0.5 and 1 W, per-unit calibrated feedforward)",
                ktrim=0.16, hold=True, boost=True, steps=STEPS_W, packs=PACKS_V, corners=None,
                save="V(al) V(vgg)", tstart=0.0),
    "sweep1": dict(_MITIG, short="rev. 1 design, threshold sweep",
                   name="revision 1 design, threshold sweep at 7.4 V pack", ktrim=0.16, hold=True, boost=True,
                   steps=STEPS_W, packs=[7.4], corners=[(v, 0.0) for v in VSH_SWEEP], save="V(al)", tstart=0.0),
    # revision 2 (finding-13): element 1 of the revision 1 design only (the deck stops at 48 ms), 0.02 V sweep of
    # VSH for each sensitivity case of SENS_CASES
    "sens": dict(_MITIG, short="rev. 1 design, element 1 sensitivity",
                 name="revision 1 design, element 1 only, VSH sweep in 0.02 V for the offset, pack and "
                      "sub-threshold slope cases", ktrim=0.16, hold=True, boost=True, steps=STEPS_W, packs=[7.4],
                 corners=[], cases=SENS_CASES, save="V(al)", tstart=0.0, tstop=TPER_S, first_only=True),
}
BOOST = math.sqrt(5.0)   # detector tap switched up 7 dB (power x 5) at steps <= 1 W: 1 W looks like 5 W


# ---------------------------------------------------------------- threshold budget (record section 3.2)
# Each term: (label, low V, high V, class, source). Sign convention of VSH above. D datasheet, DD derived from
# a datasheet or a project result, E estimate. "Uncalibrated" is the nominal datasheet table used for every
# unit (revision 0's assumption for A4); "calibrated" is a per-unit feedforward table measured at build with
# the drive on (design change 7 of the record); "compensated" adds a firmware threshold correction from the
# PA NTC (design change 8).
DV_PER_DB = 0.5 / 3.0      # V of curve shift per dB of drive (reviewer's Figure 12 reading: +0.5 V when Pin
                           # halves); E, and applied to A5 by analogy (no A5 data)
TC_V_PER_C = (-2.5e-3, -1.3e-3)   # LDMOS threshold temperature coefficient range (E, web sources in record)
T_CAL, T_DIE = 25.0, (-10.0, 110.0)  # calibration bench temperature; die range: REQ-SYS-114 cold start to the
# junction bound that thermal-ts012.md section 8 change 6 sets: the REQ-SYS-118 inhibit on the PA case at about
# 81 C (A5) or 77 C (A4) at the NTC holds the junction at 110 C with the sensor adverse and the +3 C tolerance
# (thermal note section 4.1). With the 85 C setpoint instead, the junction reaches 113.9 C (A5) and 117.1 C (A4)
# at the trip (same table), 0.010 and 0.018 V more on the uncalibrated and calibrated low ends (revision 2,
# finding-12 (ii); stated in the record).
# Per finalist (revision 2, finding-12): the highest NTC reading in service (the inhibit setpoint) and the
# die-to-NTC-reading difference at that point, 110 C minus the setpoint (29 K A5, 33 K A4; with the 85 C setpoint
# the thermal note gives 28.9 and 32.1 K, the same within 1 K). Class E (the thermal note's temperatures are
# estimates).
T_NTC_MAX = {"a5": 81.0, "a4": 77.0}
DIE_TO_NTC_K = {f: T_DIE[1] - T_NTC_MAX[f] for f in ("a5", "a4")}
TC_FW = -1.9e-3            # firmware compensation coefficient (design change 8)
TC_RES = 0.6e-3            # its residual against the true coefficient, -1.3 to -2.5 mV/C (either sign)
_temp_lo, _temp_hi = TC_V_PER_C[0] * (T_DIE[1] - T_CAL), TC_V_PER_C[0] * (T_DIE[0] - T_CAL)
_drive_in_unit_db = 0.17 + 0.10    # 144 to 148 MHz half-span (max span 0.34 dB, pa-drive runs r1-d2 and
                                   # r1-d3) plus the 0.1 dB drive change over temperature (pa-drive 3.1)
THRESHOLD_BUDGET = {
    "a4": {
        "uncalibrated": [
            ("VGS(th) unit spread 1.7 / 2.2 / 2.5 V", -0.5, 0.3, "D", "AFT05MS004N Rev. 0 Table 5"),
            ("drive unit spread 46 to 180 mW about 89 mW", -3.06 * DV_PER_DB, 2.89 * DV_PER_DB, "DD, E",
             "pa-drive-ts012 run r1-d3; Figure 12 shift"),
            ("die temperature -10 to 110 C, cal. 25 C", _temp_lo, _temp_hi, "E", "TC -1.3 to -2.5 mV/C"),
            ("hand read of Figure 12", -0.05, 0.05, "E", "this record"),
        ],
        "calibrated": [
            ("per-unit table residual", -0.02, 0.02, "E", "this record"),
            ("drive in one unit: band and temperature", -_drive_in_unit_db * DV_PER_DB,
             _drive_in_unit_db * DV_PER_DB, "DD, E", "pa-drive r1-d3; section 3.1"),
            ("die temperature -10 to 110 C, cal. 25 C", _temp_lo, _temp_hi, "E", "TC -1.3 to -2.5 mV/C"),
        ],
    },
    "a5": {
        "uncalibrated": [
            ("module VGG curve unit spread (none published; AFT05 class by analogy)", -0.5, 0.3, "E",
             "by analogy with AFT05 Table 5"),
            ("drive 11.0 to 27.2 mW in service (select-on-test pad)", -1.97 * DV_PER_DB, 1.97 * DV_PER_DB,
             "DD, E", "pa-drive-ts012 section 4.2"),
            ("die temperature -10 to 110 C, cal. 25 C", _temp_lo, _temp_hi, "E", "TC -1.3 to -2.5 mV/C"),
            ("digitized typical curve (line width)", -0.02, 0.02, "E", "tx-pa/data overlays"),
        ],
        "calibrated": [
            ("per-unit table residual", -0.02, 0.02, "E", "this record"),
            ("drive in one unit: band and temperature", -_drive_in_unit_db * DV_PER_DB,
             _drive_in_unit_db * DV_PER_DB, "DD, E", "pa-drive r1-d2; section 3.1"),
            ("die temperature -10 to 110 C, cal. 25 C", _temp_lo, _temp_hi, "E", "TC -1.3 to -2.5 mV/C"),
        ],
    },
}
# NTC compensation (design change 8): firmware shifts the table by -1.9 mV/C x (T_NTC - T_CAL). Residual
# (revision 2, finding-12): the coefficient residual (+/-0.6 mV/C) acts with either sign at either end of the NTC
# range (hot: up to T_NTC_MAX - 25 C above the bench; cold: 35 K below), so both ends take the larger of the two
# spans; plus, on the low side, the die running DIE_TO_NTC_K above the NTC reading during a key-down, at -2.5
# mV/C. ESTIMATES.
def _comp_term(fin):
    span = max(T_NTC_MAX[fin] - T_CAL, T_CAL - T_DIE[0])
    lo = -TC_RES * span + TC_V_PER_C[0] * DIE_TO_NTC_K[fin]
    hi = TC_RES * span
    return ("die temperature after NTC compensation (residual both sides; die-to-NTC %.0f K)" % DIE_TO_NTC_K[fin],
            lo, hi, "E", "this record; thermal-ts012 4.1 and 8 change 6")


for _f in ("a4", "a5"):
    THRESHOLD_BUDGET[_f]["compensated"] = [t for t in THRESHOLD_BUDGET[_f]["calibrated"]
                                           if not t[0].startswith("die")] + [_comp_term(_f)]


# Stored trim (design change 9, firmware part): the trim is read by the ADC at key-up, stored with the NTC
# reading, and folded into the feedforward offset at the next element 1 (revision 2: at every element, the
# per-element capture, finding-14), so element 1 starts from it. Its residual: ADC step and the feedforward PWM
# step; the drive change since the capture (QSY across the band, temperature); the die temperature change since
# the capture after NTC compensation (0.6 mV/C over the NTC range, -10 C to T_NTC_MAX); and the die-to-NTC
# difference present at the capture (0 to DIE_TO_NTC_K, per finalist, revision 2), which is gone at the next
# element 1 (the die has cooled to the NTC), so the curve sits to the right of the stored value by up to 2.5
# mV/C x DIE_TO_NTC_K.
for _f in ("a4", "a5"):
    _rng = T_NTC_MAX[_f] - T_DIE[0]
    THRESHOLD_BUDGET[_f]["stored"] = [
        ("stored trim: ADC step and feedforward PWM step", -0.01, 0.01, "E", "this record"),
        ("drive change since the capture: band and temperature", -_drive_in_unit_db * DV_PER_DB,
         _drive_in_unit_db * DV_PER_DB, "DD, E", "pa-drive r1-d2, r1-d3; section 3.1"),
        ("die temperature change since the capture, NTC compensated (0.6 mV/C over %.0f K)" % _rng,
         -TC_RES * _rng, TC_RES * _rng, "E", "this record"),
        ("die-to-NTC difference at the capture (0 to %.0f K), gone at element 1" % DIE_TO_NTC_K[_f], 0.0,
         -TC_V_PER_C[0] * DIE_TO_NTC_K[_f], "E", "thermal-ts012 4.1 and 8 change 6"),
    ]


def budget_totals(fin):
    """Worst-case sum and root-sum-square of each budget case (low, high)."""
    out = {}
    for case, terms in THRESHOLD_BUDGET[fin].items():
        lo = sum(t[1] for t in terms)
        hi = sum(t[2] for t in terms)
        rlo = -math.sqrt(sum(min(t[1], 0) ** 2 for t in terms))
        rhi = math.sqrt(sum(max(t[2], 0) ** 2 for t in terms))
        out[case] = dict(wc=(lo, hi), rss=(rlo, rhi))
    return out


def corners_for(fin, var):
    """(VSH, VOS) corners of a variant. The record corners of 'fix' (the revision 1 design, which includes the
    per-unit calibration and the NTC compensation) are the worst-case sums of the compensated budget (element 1
    after power-on without a stored trim) and, from revision 2 (finding-13), of the stored-trim budget (element 1
    of every over), each paired with the residual offset that acts the same way. The wider calibrated-only
    budget is covered by the sweep (held elements pass over the whole +/-0.3 V)."""
    c = VAR[var]["corners"]
    if c is not None:
        return c
    bt = budget_totals(fin)
    lo, hi = bt["compensated"]["wc"]
    slo, shi = bt["stored"]["wc"]
    return [(0.0, 0.0), (round(lo, 3), 1e-3), (round(hi, 3), -1e-3), (round(slo, 3), 1e-3), (round(shi, 3), -1e-3)]


SETTINGS_MS = [3.0, 5.0, 8.0]
TPER, TDIT, TLEAD, TCLK, TC = 48e-3, 24e-3, 10e-3, 8e-3, 7.5e-3
TQ = 32.768e-6
NEL = 8
RIN, RIDLE, KDIV, RTH, CVGG = 10e3, 4.7e6, 0.654, 1.77e3, 10e-9
# mitigated variant: the loop output is a trim of 0.1 V per volt (0 to 0.5 V) added to a feedforward VGG
# table (second PWM channel) computed from the nominal PA curve for KFF of the wanted amplitude
KTRIM, KFF = 0.1, 1.0
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
def run_params(fin, var):
    """One row per LTspice step: corner, pack voltage, power step and envelope setting (in that nesting)."""
    f, v = FIN[fin], VAR[var]
    A, D = det_law(v["det"])
    r = RIN / RIDLE
    rows = []
    if v.get("cases"):
        # variant 'sens' (revision 2): case, then VSH (0.02 V), then step, then setting
        for ci, (label, pack, vos, sub) in enumerate(v["cases"]):
            vd = f["vd"][pack]
            for vsh in VSH_FINE:
                for step in v["steps"]:
                    for tset in SETTINGS_MS:
                        pset = pset_for(fin, vd, step, var)
                        aset = math.sqrt(100 * pset)
                        dset = float(det_of([aset], A, D)[0])
                        db = BOOST if (v.get("boost") and step <= 1.0) else 1.0
                        rows.append(dict(tset_ms=tset, pack=pack, vd=vd, step_w=step, vsh=vsh, vos=vos, case=ci,
                                         case_label=label, sub=sub, scale=f["scale"][vd], pset=pset, aset=aset,
                                         dset=dset, vset=(dset + 5 * r) / (1 + r), db=db))
        return rows
    for vsh, vos in corners_for(fin, var):
        for pack in v["packs"]:
            vd = f["vd"][pack]
            for step in v["steps"]:
                for tset in SETTINGS_MS:
                    pset = pset_for(fin, vd, step, var)
                    aset = math.sqrt(100 * pset)
                    dset = float(det_of([aset], A, D)[0])
                    vset = (dset + 5 * r) / (1 + r)
                    db = BOOST if (v.get("boost") and step <= 1.0) else 1.0
                    rows.append(dict(tset_ms=tset, pack=pack, vd=vd, step_w=step, vsh=vsh, vos=vos,
                                     scale=f["scale"][vd], pset=pset, aset=aset, dset=dset, vset=vset, db=db))
    return rows


def gen_deck(fin, var):
    f, v = FIN[fin], VAR[var]
    rows = run_params(fin, var)
    A, D = det_law(v["det"])
    tab = dbm_table(f["table"])
    ktrim = v.get("ktrim", KTRIM)
    # the mitigated Cf scales with the trim gain so that the loop gain (and margin) is unchanged
    cf = f["cf_mitig"] * ktrim / KTRIM if v["ff"] else f["cf_asis"]
    runtab = lambda key: spice_table([(i + 1, row[key]) for i, row in enumerate(rows)])  # noqa: E731
    # detector table in the deck: amplitude -> Vdet; below the first point the square law (0 at 0)
    # (a point at -1 V first: LTspice table() mis-evaluates an argument exactly equal to the first abscissa)
    dpts = [(-1.0, 0.0), (0.0, 0.0)] + [(a, d) for a, d in zip(A, D)]
    L = []
    L.append(f"* keying_{fin}_{var}.cir: keying envelope loop, TS-012 finalist {f['name']}, {v['name']}")
    L.append("* cwht WP-PDR-22 pre-order item; generated by hardware/sim/tx-keying/keying_run.py; record")
    L.append("* docs/design/analysis/keying-ts012.md. Envelope-domain behavioural deck (no RF carrier).")
    npc = len(v["packs"]) * len(v["steps"]) * len(SETTINGS_MS)
    L.append(f"* Steps: for each corner in turn, the packs {v['packs']} V (drain {[f['vd'][p] for p in v['packs']]} V),")
    L.append(f"* within each the power steps {v['steps']} W, within each the 3, 5, 8 ms (10-90 %) settings:")
    if v.get("cases"):
        nv = len(VSH_FINE) * len(v["steps"]) * len(SETTINGS_MS)
        L.append(f"* (variant sens: for each case in turn, VSH {VSH_FINE[0]:+.2f} to {VSH_FINE[-1]:+.2f} V in 0.02 V, within each")
        L.append("* the steps and settings; the pack of the case; element 1 only)")
        for i, (label, pack, vos, sub) in enumerate(v["cases"]):
            L.append(f"*   runs {nv * i + 1}..{nv * i + nv}: {label}: pack {pack} V, offset {vos * 1e3:+.1f} mV, "
                     f"PA sub-threshold slope {sub:g} dB/V")
    for i, (vsh, vos) in enumerate(corners_for(fin, var)):
        L.append(f"*   runs {npc * i + 1}..{npc * i + npc}: PA curve shifted {vsh:+.3f} V, error-amplifier offset {vos * 1e3:+.1f} mV")
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
    L.append(f".param DB=table(run,{runtab('db')})")
    if v.get("cases"):
        L.append(f".param SUB=table(run,{runtab('sub')})")
    L.append(f".param PLEAK={10 ** ((f['pleak_dbm'] - 30) / 10):.6g}")
    L.append(f".param LOSS={10 ** (-LOSS_DB / 10):.6f} KDIV={KDIV} KTRIM={ktrim} KFF={KFF}")
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
        L.append("* DB: detector tap factor (1, or BOOST at the 0.5 and 1 W steps of the revision 1 design)")
        L.append(f"Bref refraw 0 V=table(DB*ASET*env(time),{spice_table(dpts)})")
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
        if v.get("hold"):
            L.append("* revision 1: the integrator input is opened while parked, so the trim is HELD between elements")
            L.append("* (no reset); it starts at mid-rail at t = 0 (power-on)")
            L.append(f"Gi 0 xi value={{(1-V(park))*(V(vref)-V(detf)+VOS)/{RIN:g}}}")
        else:
            L.append(f"Gi 0 xi value={{(V(vref)-V(detf)+VOS)/{RIN:g}}}")
        L.append(f"Ci xi 0 {cf:.4g}")
        L.append("Dih xi vh DI")
        L.append("Dil vl xi DI")
        L.append("Vh vh 0 2.485")
        L.append("Vl vl 0 -2.485")
        if not v.get("hold"):
            L.append("S2 xi 0 park 0 SWC")
        L.append("Bo out 0 V=2.5+V(xi)")
        L.append(".model DI D(Ron=1 Roff=1e12 Vfwd=0)")
        L.append("* feedforward VGG table (second 12-bit PWM, same update and 2-pole RC as the reference): the nominal")
        L.append("* inverse PA curve at the run's drain voltage for KFF of the wanted amplitude, 0 V when the table is 0")
        if v.get("cases"):
            # revision 2 (sens): the firmware table's foot follows the run's SUB (calibrated unit, see SENS_CASES)
            v0, p0 = f["table"][0]
            d0 = 10 * math.log10(p0 * 1e3)
            inv = [(round(d0 - 1.0, 4), v0)] + [(10 * math.log10(y * 1e3), x) for x, y in f["table"]]
            L.append("* feedforward foot below the graphs at SUB dB/V (the per-unit calibration reads it down to the")
            L.append("* detector's visibility floor)")
            L.append(".func ffd(x) {10*log10(max((KFF*ASET*x)**2/100/LOSS/SCALE,1e-20)*1e3)}")
            L.append(f"Bff ffraw 0 V=(env(time)>0)*max(table(max(ffd(env(time)),{d0:.6g}),{spice_table(sorted(inv))})"
                     f"-max({d0:.6g}-ffd(env(time)),0)/SUB,0)")
        else:
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
    if v.get("cases"):
        # revision 2 (finding-13): below the first graph point V0 the PA is extended at SUB dB/V (per run); the
        # table itself starts 1 V below V0 at the V0 value, so its first abscissa is never evaluated
        v0, p0 = f["table"][0]
        main = [(round(v0 - 1.0, 3), 10 * math.log10(p0 * 1e3))] + [(x, 10 * math.log10(y * 1e3)) for x, y in f["table"]]
        L.append(f"* PA sub-threshold extension below {v0} V at SUB dB/V (65, 100 or 150; the firmware table follows it)")
        L.append(f"Bpg pg 0 V=SCALE*pow(10,(table(max(V(vgg)-VSH,{v0}),{spice_table(main)})"
                 f"-SUB*max({v0}-(V(vgg)-VSH),0)-30)/10)")
    else:
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
        L.append("* detector static law from run 2026-09-28-det-char-biased and its 4.7 us video pole (10 k, 470 pF);")
        L.append("* DB is the tap factor (the diode sees DB times the amplitude of the 5 W design tap)")
        L.append(f"Bdet d0 0 V=table(DB*V(al),{spice_table(dpts)})")
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
    L.append(f".save {v['save']}")
    L.append(f".tran 0 {v.get('tstop', NEL * TPER)} {v['tstart']} 20u")
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


ELEMENTS = range(2, NEL)   # elements 3 to 8 (0-based 2..7): every element in the saved window after start-up
KPLOT = 3                  # element 4: the element drawn in the envelope and key-up plots


def element_metrics(tu, au, k, tset):
    """10-to-90 % rise and fall, shape errors and top amplitude of element k (0-based)."""
    tr = tset / RC_1090
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
    return dict(atop=atop, an=an, rise=rise, fall=fall, e_r=e_r, e_f=e_f)


def analyse(fin, var, rundir, rows):
    raw = RawRead(str(rundir / f"keying_{fin}_{var}.raw"))
    names = raw.get_trace_names()
    # a .tran start time (TSTART > 0) is written as the raw header "Offset": the time axis starts at 0 there
    toff = float(raw.get_raw_property().get("Offset", 0.0))
    out = []
    fin_d = FIN[fin]
    for s, row in zip(raw.get_steps(), rows):
        t = np.abs(raw.get_trace("time").get_wave(s)) + toff
        a = raw.get_trace("V(al)").get_wave(s)
        vgg = raw.get_trace("V(vgg)").get_wave(s) if "V(vgg)" in names else None
        vref = raw.get_trace("V(vref)").get_wave(s) if "V(vref)" in names else None
        tset = row["tset_ms"] * 1e-3
        tr = tset / RC_1090
        dtu = 10e-6
        if VAR[var].get("first_only"):
            # variant 'sens' (revision 2): element 1 only (time and shape against REQ-TX-005 and TC-SYS-013)
            tu0 = np.arange(0.0, TPER, dtu)
            m1 = element_metrics(tu0, np.interp(tu0, t, a), 0, tset)
            ok1 = not (math.isnan(m1["rise"]) or math.isnan(m1["fall"]))
            d1 = [m1["rise"] - tset, m1["fall"] - tset] if ok1 else [float("nan")]
            res = dict(run=int(s) + 1, tset_ms=row["tset_ms"], pack=row["pack"], vd=row["vd"], step_w=row["step_w"],
                       vsh=row["vsh"], vos=row["vos"], case=row["case"], case_label=row["case_label"],
                       sub_db_per_v=row["sub"], pset_w=row["pset"], ptop_w=m1["atop"] ** 2 / 100,
                       first_rise_ms=m1["rise"] * 1e3, first_fall_ms=m1["fall"] * 1e3,
                       first_err_pct=100 * max(d1, key=abs) / tset if ok1 else float("nan"),
                       first_shape_err=max(m1["e_r"], m1["e_f"]))
            fe = abs(res["first_err_pct"]) / 100 * tset if ok1 else float("inf")
            res["pass"] = dict(first_t1090_req_tx005=bool(fe <= REQ["t1090_rel_tol"] * tset + 1e-12),
                               first_t1090_tc_sys013=bool(fe <= REQ["t1090_tol_ms"] * 1e-3 + 1e-12),
                               first_shape=bool(res["first_shape_err"] <= REQ["shape_tol"]))
            res["_trace"] = dict(t=t, a=a, atop=m1["atop"])
            out.append(res)
            continue
        tu = np.arange(2 * TPER, NEL * TPER, dtu)
        au = np.interp(tu, t, a)
        # every element in the window (revision 1: the worst element is reported, element 4 is plotted)
        per = {k: element_metrics(tu, au, k, tset) for k in ELEMENTS}
        dev = {k: max(abs(m["rise"] - tset), abs(m["fall"] - tset)) if not (math.isnan(m["rise"]) or
                      math.isnan(m["fall"])) else 9.0 for k, m in per.items()}
        kw = max(dev, key=dev.get)
        kd = KPLOT * TPER
        atop = per[KPLOT]["atop"]
        an = per[KPLOT]["an"]
        rises = [per[k]["rise"] for k in ELEMENTS]
        falls = [per[k]["fall"] for k in ELEMENTS]
        e_r = max(per[k]["e_r"] for k in ELEMENTS)
        e_f = max(per[k]["e_f"] for k in ELEMENTS)
        ov_db = 20 * math.log10(max(float(np.max(au)) / atop, 1e-9))
        sp = spectrum_metrics(tu, au)
        spi = spectrum_metrics(tu, ideal_envelope(tu, tset))
        # RF-off windows around key-up of element 4: ramp end TE to gate TE+TG, then after the gate
        k = KPLOT
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
        a_gate = float(np.interp(tg - 20e-6, t, a))
        rise_w, fall_w = per[kw]["rise"], per[kw]["fall"]
        res = dict(
            run=int(s) + 1, tset_ms=row["tset_ms"], pack=row["pack"], vd=row["vd"], step_w=row["step_w"],
            vsh=row["vsh"], vos=row["vos"], pset_w=row["pset"],
            ptop_w=atop ** 2 / 100,
            # worst element (largest |10-90 time - setting| of rise or fall) and the range over elements 3 to 8
            rise_ms=rise_w * 1e3, fall_ms=fall_w * 1e3, worst_element=kw + 1,
            rise_ms_min=min(rises) * 1e3, rise_ms_max=max(rises) * 1e3,
            fall_ms_min=min(falls) * 1e3, fall_ms_max=max(falls) * 1e3,
            shape_err_rise=e_r, shape_err_fall=e_f, overshoot_db=ov_db,
            bw26_hz=sp["bw26_hz"], side_max_db=sp["side_max_db"], side_max_at_hz=sp["side_max_at_hz"],
            off60_hz=sp["off60_hz"], vgg_max=float(np.max(vgg)) if vgg is not None else float("nan"),
            ideal_bw26_hz=spi["bw26_hz"], ideal_side_max_db=spi["side_max_db"],
            keyup_window_max_dbm=p_w1_max, keyup_loop_tail_max_dbm=p_tail_max, loop_tail_at_gate_dbm=p_tail_gate,
            at_gate_dbm=p_at_gate, gate_step_rel_db=20 * math.log10(max(a_gate / atop, 1e-12)),
            after_gate_max_dbm=p_w2_max,
        )
        tmax = max(abs(min(rises) - tset), abs(max(rises) - tset), abs(min(falls) - tset), abs(max(falls) - tset))
        ok_t = not any(math.isnan(x) for x in rises + falls)
        res["t1090_err_ms"] = tmax * 1e3 if ok_t else float("nan")
        # signed worst deviation in percent of the setting (the larger in magnitude of the extremes)
        devs = [x - tset for x in rises + falls]
        res["t1090_err_pct"] = 100 * max(devs, key=abs) / tset if ok_t else float("nan")
        # element 1 (trim at mid-rail: the first element after power-on or a stale hold), when saved
        first = None
        if toff < TLEAD - 3e-3:
            tu0 = np.arange(0.0, TPER, dtu)
            m1 = element_metrics(tu0, np.interp(tu0, t, a), 0, tset)
            if not (math.isnan(m1["rise"]) or math.isnan(m1["fall"])):
                d1 = [m1["rise"] - tset, m1["fall"] - tset]
                first = dict(first_rise_ms=m1["rise"] * 1e3, first_fall_ms=m1["fall"] * 1e3,
                             first_err_pct=100 * max(d1, key=abs) / tset,
                             first_shape_err=max(m1["e_r"], m1["e_f"]))
            else:
                first = dict(first_rise_ms=float("nan"), first_fall_ms=float("nan"), first_err_pct=float("nan"),
                             first_shape_err=float("nan"))
            res.update(first)
        res["pass"] = dict(
            # REQ-TX-005 (TC-TX-005): every element's rise and fall within +/-10 % (TBR) of the setting
            t1090_req_tx005=bool(ok_t and tmax <= REQ["t1090_rel_tol"] * tset + 1e-12),
            # TC-SYS-013 (REQ-SYS-014): within +/-0.5 ms of the setting
            t1090_tc_sys013=bool(ok_t and tmax <= REQ["t1090_tol_ms"] * 1e-3 + 1e-12),
            shape=bool(max(e_r, e_f) <= REQ["shape_tol"]),
            overshoot=bool(ov_db <= REQ["overshoot_db"]),
            bw26=bool(res["bw26_hz"] <= REQ["bw26_hz"]),
            sideband=bool(res["side_max_db"] <= REQ["side_db"]),
            # REQ-TX-014 read as the settled key-up state: the level just before the drive gate, 1 ms after the
            # ramp end (includes the modelled gate-off leakage PLEAK, an estimate)
            keyup_1uW=bool(p_at_gate <= REQ["keyup_dbm"]),
            vgg=bool(res["vgg_max"] <= REQ["vgg_max"]) if (fin == "a5" and vgg is not None) else True,
            setpoint=bool(abs(10 * math.log10(res["ptop_w"] / row["pset"])) <= REQ["setpoint_db"]),  # model health
        )
        if first is not None:
            fe = abs(first["first_err_pct"]) / 100 * tset
            res["pass"]["first_t1090_req_tx005"] = bool(fe <= REQ["t1090_rel_tol"] * tset + 1e-12)
            res["pass"]["first_t1090_tc_sys013"] = bool(fe <= REQ["t1090_tol_ms"] * 1e-3 + 1e-12)
            res["pass"]["first_shape"] = bool(first["first_shape_err"] <= REQ["shape_tol"])
        res["_trace"] = dict(t=t, a=a, vgg=vgg, vref=vref, tu=tu, an=an, sp=sp, spi=spi,
                             kd=kd, tr=tr, te=te, tg=tg, atop=atop, pdbm=pdbm)
        out.append(res)
    return out


def plot_columns(var):
    """(pack, step) of each plot column: both packs for the single-step as-written runs, else every step at
    the 7.4 V pack (the other packs are in t1090.png and corners.png)."""
    v = VAR[var]
    if len(v["steps"]) == 1:
        return [(p, v["steps"][0]) for p in v["packs"]]
    pk = 7.4 if 7.4 in v["packs"] else v["packs"][0]
    return [(pk, st) for st in v["steps"]]


def pick(res, tset, pack, step, vsh=0.0, vos=0.0):
    return [x for x in res if x["tset_ms"] == tset and x["pack"] == pack and x["step_w"] == step
            and abs(x["vsh"] - vsh) < 1e-9 and abs(x["vos"] - vos) < 1e-12][0]


def ok_time(r):
    return r["pass"]["t1090_req_tx005"] and r["pass"]["t1090_tc_sys013"] and r["pass"]["shape"] \
        and r["pass"]["overshoot"]


def plots(fin, var, rundir, res):
    title = f"{fin.upper()} {VAR[var]['short']}"
    cols = plot_columns(var)
    nc = len(cols)
    # --- envelope versus time: element 4 per setting (rows) and column
    fig, axes = plt.subplots(3, nc, figsize=(4.4 * nc + 1, 11), squeeze=False)
    for i, tset in enumerate(SETTINGS_MS):
        for j, (pack, step) in enumerate(cols):
            r = pick(res, tset, pack, step)
            tr_ = r["_trace"]
            ax = axes[i, j]
            t0 = tr_["kd"]
            m = (tr_["t"] >= t0 + 6e-3) & (tr_["t"] <= t0 + TPER + 2e-3)
            tt = (tr_["t"][m] - t0) * 1e3
            an = tr_["a"][m] / tr_["atop"]
            ax.plot(tt, an, lw=1.4, label="RF amplitude at the load (normalized)")
            tu, anu, tr = tr_["tu"], tr_["an"], tr_["tr"]
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
            for lv in (0.1, 0.9):
                ax.axhline(lv, color="0.5", lw=0.4, ls=":")
            ax.axvline(TLEAD * 1e3, color="g", lw=0.6)
            ax.axvline((tr_["te"] - t0) * 1e3, color="m", lw=0.6)
            ax.axvline((tr_["tg"] - t0) * 1e3, color="r", lw=0.8, ls=":")
            ax2 = ax.twinx()
            ax2.plot(tt, tr_["vgg"][m], color="tab:orange", lw=0.8, label="VGG (V)")
            if tr_["vref"] is not None:
                ax2.plot(tt, tr_["vref"][m], color="tab:green", lw=0.8, label="reference (V)")
            ax2.set_ylim(0, 4)
            ax2.set_ylabel("VGG, reference (V)", fontsize=7)
            lim = REQ["t1090_rel_tol"] * tset
            ax.set_title(f"{tset:.0f} ms, {step:g} W step (set {r['pset_w']:.1f} W), pack {pack} V\n"
                         f"10-90 rise {r['rise_ms_min']:.2f}..{r['rise_ms_max']:.2f}, fall {r['fall_ms_min']:.2f}.."
                         f"{r['fall_ms_max']:.2f} ms (REQ-TX-005 {tset - lim:.1f}..{tset + lim:.1f});"
                         f" shape {100 * max(r['shape_err_rise'], r['shape_err_fall']):.1f} % (5 %)",
                         fontsize=7.5, color="k" if ok_time(r) else "r")
            ax.set_ylim(-0.05, 1.25)
            ax.set_xlabel("ms from key-down; green ramp start, magenta ramp end, red dotted drive gate", fontsize=6.5)
            ax.set_ylabel("normalized amplitude", fontsize=8)
            ax.grid(True, lw=0.3)
            if i == 0 and j == 0:
                h1, l1 = ax.get_legend_handles_labels()
                h2, l2 = ax2.get_legend_handles_labels()
                ax.legend(h1 + h2, l1 + l2, fontsize=6, loc="upper right")
    fig.suptitle(f"Keying envelope, {title}: 50 WPM dits, element 4 drawn;\ntimes are the range over elements 3 "
                 f"to 8 (red title = fails REQ-TX-005, TC-SYS-013 time or shape)", fontsize=10)
    fig.tight_layout()
    fig.savefig(rundir / "envelope.png", dpi=100)
    plt.close(fig)

    # --- spectrum with the requirement mask
    fig, axes = plt.subplots(3, nc, figsize=(4.4 * nc + 1, 11), squeeze=False)
    for i, tset in enumerate(SETTINGS_MS):
        for j, (pack, step) in enumerate(cols):
            r = pick(res, tset, pack, step)
            sp, spi = r["_trace"]["sp"], r["_trace"]["spi"]
            ax = axes[i, j]
            m = harmonic_cells(sp["cc"])
            ax.plot(spi["cc"][m], spi["cells_db"][m], color="0.55", lw=0.6,
                    label="ideal raised cosine of the setting (no PA, no loop)")
            ax.plot(sp["cc"][m], sp["cells_db"][m], lw=0.9, color="tab:blue",
                    label="simulated RF envelope: 10 Hz cells holding a dit-rate line, rel. total power")
            ax.axvspan(-REQ["bw26_hz"] / 2, REQ["bw26_hz"] / 2, color="g", alpha=0.08,
                       label="REQ-SYS-015 350 Hz (26 dB bandwidth)")
            ax.axvline(-r["bw26_hz"] / 2, color="g", lw=0.8, ls="--")
            ax.axvline(r["bw26_hz"] / 2, color="g", lw=0.8, ls="--", label="simulated 26 dB bandwidth")
            ax.plot([-5000, -750, -750, 750, 750, 5000], [-60, -60, 0, 0, -60, -60], "r", lw=1.2,
                    label="REQ-TX-006 mask: -60 dB beyond 750 Hz")
            ax.set_xlim(-5000, 5000)
            ax.set_ylim(-120, 0)
            ok = r["pass"]["bw26"] and r["pass"]["sideband"]
            ax.set_title(f"{tset:.0f} ms, {step:g} W, pack {pack} V: 26 dB BW {r['bw26_hz']:.0f} Hz;\nworst cell "
                         f"beyond 750 Hz {r['side_max_db']:.1f} dB at {r['side_max_at_hz']:.0f} Hz", fontsize=7.5,
                         color="k" if ok else "r")
            ax.set_xlabel("offset from carrier (Hz)", fontsize=7)
            ax.set_ylabel("dB", fontsize=8)
            ax.grid(True, lw=0.3)
            if i == 0 and j == 0:
                ax.legend(fontsize=6, loc="upper right")
    fig.suptitle(f"Keying spectrum, {title}: 50 WPM continuous dits (6 periods, elements 3 to 8)", fontsize=10)
    fig.tight_layout()
    fig.savefig(rundir / "spectrum.png", dpi=100)
    plt.close(fig)

    # --- RF level at key-up (log scale) with REQ-TX-014 and REQ-SYS-183
    fig, axes = plt.subplots(1, 3, figsize=(15, 4.6), sharey=True)
    for i, tset in enumerate(SETTINGS_MS):
        ax = axes[i]
        for (pack, step) in cols:
            r = pick(res, tset, pack, step)
            tr_ = r["_trace"]
            t0 = tr_["kd"]
            m = (tr_["t"] >= t0 + TLEAD + TDIT - 2e-3) & (tr_["t"] <= t0 + TPER + TCLK + 3e-3)
            ax.plot((tr_["t"][m] - t0) * 1e3, tr_["pdbm"][m], lw=1.0, label=f"{step:g} W, pack {pack} V")
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


def corner_label(vsh, vos):
    return f"VSH {vsh:+.3f} V, VOS {vos * 1e3:+.0f} mV"


def plots_corners(fin, var, rundir, res):
    """Envelopes of every record corner at the 7.4 V pack, per setting (rows) and step (columns): element 1 (the
    trim starts from mid-rail) solid, element 4 dashed. Every pack is in t1090.png and result.csv."""
    title = f"{fin.upper()} {VAR[var]['short']}"
    cs = corners_for(fin, var)
    cols_c = ["tab:blue", "tab:red", "tab:green", "tab:purple", "tab:orange"]
    steps = VAR[var]["steps"]
    pack = 7.4 if 7.4 in VAR[var]["packs"] else VAR[var]["packs"][0]
    fig, axes = plt.subplots(3, len(steps), figsize=(4.4 * len(steps) + 1, 11.5), squeeze=False)
    for i, tset in enumerate(SETTINGS_MS):
        for j, step in enumerate(steps):
            ax = axes[i, j]
            notes = []
            for ci, (vsh, vos) in enumerate(cs):
                r = pick(res, tset, pack, step, vsh, vos)
                tr_ = r["_trace"]
                for k, ls in ((0, "-"), (KPLOT, "--")):
                    t0 = k * TPER
                    m = (tr_["t"] >= t0 + 6e-3) & (tr_["t"] <= t0 + TPER + 2e-3)
                    if not np.any(m):
                        continue
                    ax.plot((tr_["t"][m] - t0) * 1e3, tr_["a"][m] / tr_["atop"], color=cols_c[ci % 5],
                            lw=1.0 if k == 0 else 0.8, ls=ls,
                            label=(f"{corner_label(vsh, vos)}, element {k + 1}") if (i == 0 and j == 0) else None)
                bad = sorted(set(k.replace("first_", "el.1 ") for k, v in r["pass"].items()
                                 if not v and k not in ("keyup_1uW",)))
                if "first_err_pct" in r:
                    notes.append(f"{vsh:+.2f} V: el.1 {r['first_err_pct']:+.1f} %, "
                                 f"shape {100 * r['first_shape_err']:.1f} %" + (" FAIL" if bad else ""))
            anyfail = any(n.endswith("FAIL") for n in notes)
            ax.set_ylim(-0.05, 1.25)
            ax.grid(True, lw=0.3)
            ax.set_title(f"{tset:.0f} ms, {step:g} W, pack {pack} V\n" + "\n".join(notes), fontsize=6.5,
                         color="r" if anyfail else "k")
            ax.set_xlabel("ms from the element's key-down", fontsize=7)
            if i == 0 and j == 0:
                ax.legend(fontsize=5.5, loc="upper right")
    fig.suptitle(f"{title}: record corners (nominal; compensated and stored-trim budgets, worst-case sums, residual "
                 f"offset acting the same way). Solid: element 1 (trim from mid-rail); dashed: element 4 (held trim).\n"
                 f"Red title: a corner fails REQ-TX-005 or TC-SYS-013 at element 1. Corner order in each title: "
                 f"nominal, compensated low, compensated high, stored-trim low, stored-trim high", fontsize=9.5)
    fig.tight_layout()
    fig.savefig(rundir / "corners.png", dpi=100)
    plt.close(fig)


def plot_t1090(fin, var, rundir, res):
    """Every run: worst 10-90 error (% of the setting) against REQ-TX-005 and TC-SYS-013, shape error against
    5 %, worst cell beyond 750 Hz against -60 dB."""
    title = f"{fin.upper()} {VAR[var]['short']}"
    cs = corners_for(fin, var)
    fig, axes = plt.subplots(1, 3, figsize=(17, 5.2))
    marks = {6.4: "v", 7.4: "o", 8.4: "^"}
    setc = {3.0: "tab:blue", 5.0: "tab:orange", 8.0: "tab:purple"}
    steps = VAR[var]["steps"]
    for r in res:
        ci = [i for i, c in enumerate(cs) if abs(c[0] - r["vsh"]) < 1e-9 and abs(c[1] - r["vos"]) < 1e-12][0]
        x = steps.index(r["step_w"]) * (len(cs) + 1) + ci + 0.12 * (SETTINGS_MS.index(r["tset_ms"]) - 1)
        kw = dict(color=setc[r["tset_ms"]], marker=marks.get(r["pack"], "o"), ms=5, ls="none")
        axes[0].plot(x, r["t1090_err_pct"], **kw)
        axes[1].plot(x, 100 * max(r["shape_err_rise"], r["shape_err_fall"]), **kw)
        axes[2].plot(x, r["side_max_db"], **kw)
        if "first_err_pct" in r:
            kf = dict(kw, mfc="none", ms=7)
            axes[0].plot(x + 0.3, r["first_err_pct"], **kf)
            axes[1].plot(x + 0.3, 100 * r["first_shape_err"], **kf)
    for ax in axes:
        ax.set_xticks([k * (len(cs) + 1) + (len(cs) - 1) / 2 for k in range(len(steps))])
        ax.set_xticklabels([f"{s:g} W step" for s in steps], fontsize=8)
        ax.grid(True, lw=0.3)
    axes[0].axhspan(-100 * REQ["t1090_rel_tol"], 100 * REQ["t1090_rel_tol"], color="g", alpha=0.1)
    for y in (-10, 10):
        axes[0].axhline(y, color="r", lw=1.2)
    for tset, c in setc.items():
        for sg in (-1, 1):
            axes[0].axhline(sg * 100 * 0.5 / tset, color=c, lw=0.7, ls="--")
    axes[0].set_ylabel("worst 10-90 % time error over elements 3 to 8 (% of setting)")
    axes[0].set_title("REQ-TX-005 +/-10 % (red); TC-SYS-013 +/-0.5 ms (dashed, per setting colour)", fontsize=9)
    axes[1].axhline(100 * REQ["shape_tol"], color="r", lw=1.2)
    axes[1].set_ylabel("shape error, worst element (% of full scale)")
    axes[1].set_title("TC-SYS-013 raised-cosine shape: 5 % (red)", fontsize=9)
    axes[2].axhline(REQ["side_db"], color="r", lw=1.2)
    axes[2].set_ylabel("worst 10 Hz cell beyond 750 Hz (dB rel. total power)")
    axes[2].set_title("REQ-TX-006: -60 dB (red)", fontsize=9)
    from matplotlib.lines import Line2D
    h = [Line2D([], [], color=c, marker="o", ls="none", label=f"{t:.0f} ms setting") for t, c in setc.items()]
    h += [Line2D([], [], color="k", marker=m, ls="none", label=f"pack {p} V") for p, m in marks.items()
          if p in VAR[var]["packs"]]
    h += [Line2D([], [], color="k", marker="o", ls="none", label="elements 3 to 8 (filled)"),
          Line2D([], [], color="k", marker="o", mfc="none", ls="none", label="element 1, trim from mid-rail (hollow)")]
    axes[0].legend(handles=h, fontsize=7, loc="best")
    fig.suptitle(f"{title}: every run (steps x corners x packs x settings). Corners in each step group, left to "
                 f"right: " + ", ".join(corner_label(*c) for c in cs), fontsize=9.5)
    fig.tight_layout()
    fig.savefig(rundir / "t1090.png", dpi=105)
    plt.close(fig)


def window_of(res, fin, step, tset=None, which="steady"):
    """Contiguous VSH interval about 0 over which every keying criterion passes (per step; worst setting).
    which: "steady" (elements 3 to 8, with the spectrum) or "first" (element 1 time and shape only)."""
    ok = {}
    for r in res:
        if r["step_w"] != step or (tset is not None and r["tset_ms"] != tset):
            continue
        p = r["pass"]
        if which == "first":
            if "first_shape" not in p:
                return (float("nan"), float("nan"))
            good = p["first_t1090_req_tx005"] and p["first_t1090_tc_sys013"] and p["first_shape"]
        else:
            good = p["t1090_req_tx005"] and p["t1090_tc_sys013"] and p["shape"] and p["overshoot"] \
                and p["bw26"] and p["sideband"] and p["setpoint"] and p["vgg"]
        ok[r["vsh"]] = ok.get(r["vsh"], True) and good
    vs = sorted(ok)
    if not ok.get(0.0, False):
        return (float("nan"), float("nan"))
    i0 = vs.index(0.0)
    lo = i0
    while lo - 1 >= 0 and ok[vs[lo - 1]]:
        lo -= 1
    hi = i0
    while hi + 1 < len(vs) and ok[vs[hi + 1]]:
        hi += 1
    return (vs[lo], vs[hi])


def _edge(xs, ys, lim, side):
    """VSH where |y| first reaches lim moving from 0 towards side (-1 or +1), linear interpolation."""
    pts = sorted(zip(xs, ys), key=lambda p: p[0] * side)
    pts = [p for p in pts if p[0] * side >= -1e-12]
    prev = None
    for x, y in pts:
        if math.isnan(y) or abs(y) > lim:
            if prev is None or math.isnan(y):
                return prev[0] if prev else float("nan")
            x0, y0 = prev
            return x0 + (lim - abs(y0)) * (x - x0) / (abs(y) - abs(y0))
        prev = (x, y)
    return float("inf") * side


def window_interp(res, step, which="steady"):
    """Interpolated window edges (V) per setting on REQ-TX-005 (10 %), TC-SYS-013 (0.5 ms, 5 %) and, for the
    steady elements, REQ-TX-006 (-60 dB); returns {setting: (lo, hi, binding criterion lo, hi)} and the
    worst over settings."""
    out = {}
    for tset in SETTINGS_MS:
        rr = [r for r in res if r["step_w"] == step and r["tset_ms"] == tset]
        xs = [r["vsh"] for r in rr]
        if which == "first":
            if "first_err_pct" not in rr[0]:
                return {}
            crit = {"REQ-TX-005": ([r["first_err_pct"] for r in rr], 100 * REQ["t1090_rel_tol"]),
                    "TC-SYS-013 time": ([r["first_err_pct"] for r in rr], 100 * 0.5 / tset),
                    "TC-SYS-013 shape": ([100 * r["first_shape_err"] for r in rr], 100 * REQ["shape_tol"])}
        else:
            crit = {"REQ-TX-005": ([r["t1090_err_pct"] for r in rr], 100 * REQ["t1090_rel_tol"]),
                    "TC-SYS-013 time": ([r["t1090_err_pct"] for r in rr], 100 * 0.5 / tset),
                    "TC-SYS-013 shape": ([100 * max(r["shape_err_rise"], r["shape_err_fall"]) for r in rr],
                                         100 * REQ["shape_tol"]),
                    "REQ-TX-006": ([r["side_max_db"] + 120 for r in rr], 60.0)}
        lo, hi, blo, bhi = -float("inf"), float("inf"), "", ""
        for name, (ys, lim) in crit.items():
            e_lo, e_hi = _edge(xs, ys, lim, -1), _edge(xs, ys, lim, +1)
            if e_lo > lo:
                lo, blo = e_lo, name
            if e_hi < hi:
                hi, bhi = e_hi, name
        if math.isinf(lo):
            lo, blo = min(xs), "none within the sweep"
        if math.isinf(hi):
            hi, bhi = max(xs), "none within the sweep"
        out[f"{tset:g}ms"] = [lo, hi, blo, bhi]
    out["all"] = [max(v[0] for v in out.values()), min(v[1] for v in out.values())]
    return out


def plot_window(fin, var, rundir, res):
    """Threshold sweep: worst 10-90 error, shape error and worst sideband cell against VSH, per setting (columns)
    and step (lines), with the limits and the threshold budget bands."""
    title = f"{fin.upper()} {VAR[var]['short']}"
    bt = budget_totals(fin)
    fig, axes = plt.subplots(3, 3, figsize=(17, 12))
    stc = {0.5: "tab:red", 1.0: "tab:orange", 2.0: "tab:green", 5.0: "tab:blue"}
    for j, tset in enumerate(SETTINGS_MS):
        for step in VAR[var]["steps"]:
            rr = sorted([r for r in res if r["tset_ms"] == tset and r["step_w"] == step], key=lambda r: r["vsh"])
            x = [r["vsh"] for r in rr]
            axes[0, j].plot(x, [r["t1090_err_pct"] for r in rr], "o-", color=stc[step], ms=3,
                            label=f"{step:g} W, elements 3 to 8")
            axes[1, j].plot(x, [100 * max(r["shape_err_rise"], r["shape_err_fall"]) for r in rr], "o-",
                            color=stc[step], ms=3)
            axes[2, j].plot(x, [r["side_max_db"] for r in rr], "o-", color=stc[step], ms=3)
            if "first_err_pct" in rr[0]:
                axes[0, j].plot(x, [r["first_err_pct"] for r in rr], "x--", color=stc[step], ms=4, lw=0.9,
                                label=f"{step:g} W, element 1 (trim from mid-rail)")
                axes[1, j].plot(x, [100 * r["first_shape_err"] for r in rr], "x--", color=stc[step], ms=4, lw=0.9)
        axes[0, j].axhline(10, color="r", lw=1.2)
        axes[0, j].axhline(-10, color="r", lw=1.2, label="REQ-TX-005 +/-10 %")
        axes[0, j].axhline(100 * 0.5 / tset, color="k", lw=0.8, ls="--")
        axes[0, j].axhline(-100 * 0.5 / tset, color="k", lw=0.8, ls="--", label="TC-SYS-013 +/-0.5 ms")
        axes[0, j].set_ylim(-40, 40)
        axes[1, j].axhline(5, color="r", lw=1.2, label="TC-SYS-013 5 %")
        axes[1, j].set_ylim(0, 15)
        axes[2, j].axhline(-60, color="r", lw=1.2, label="REQ-TX-006 -60 dB")
        axes[2, j].set_ylim(-90, -40)
        axes[0, j].set_title(f"{tset:.0f} ms setting: worst 10-90 time error (% of setting)", fontsize=9)
        axes[1, j].set_title(f"{tset:.0f} ms: shape error, worst element (% of full scale)", fontsize=9)
        axes[2, j].set_title(f"{tset:.0f} ms: worst 10 Hz cell beyond 750 Hz (dB)", fontsize=9)
        for i in range(3):
            ax = axes[i, j]
            ax.grid(True, lw=0.3)
            for case, col, a_ in (("calibrated", "tab:purple", 0.10), ("compensated", "tab:green", 0.18)):
                lo, hi = bt[case]["wc"]
                ax.axvspan(lo, hi, color=col, alpha=a_, label=f"threshold budget, {case} (worst-case sum)"
                           if (i == 0 and j == 0) else None)
            ax.axvline(0, color="0.4", lw=0.5)
            ax.set_xlabel("VSH: PA curve shift against the feedforward table (V; < 0 earlier onset)", fontsize=7)
        axes[0, j].legend(fontsize=6.5, loc="upper right")
    fig.suptitle(f"{title} (7.4 V pack): tolerable threshold window per step (solid: elements 3 to 8; dashed: "
                 f"element 1 where saved).\nShaded: the threshold budgets of the "
                 f"record section 3.2 (uncalibrated off scale: {bt['uncalibrated']['wc'][0]:+.2f} to "
                 f"{bt['uncalibrated']['wc'][1]:+.2f} V)", fontsize=10)
    fig.tight_layout()
    fig.savefig(rundir / "window.png", dpi=100)
    plt.close(fig)


def sens_windows(res):
    """Element-1 windows of the 'sens' variant (revision 2, finding-13): per case and step, the interpolated edges
    (window_interp) and the conservative grid edges (last passing 0.02 V point, window_of), and the worst over
    the steps; plus the composite offset case (low edge of VOS +1 mV, high edge of VOS -1 mV)."""
    out = {}
    for label, *_ in SENS_CASES:
        rr = [r for r in res if r["case_label"] == label]
        d = {}
        for st in STEPS_W:
            wi = window_interp(rr, st, "first")
            d[f"{st:g}W"] = dict(interp=wi["all"], grid=list(window_of(rr, None, st, None, "first")),
                                 per_setting={k: v for k, v in wi.items() if k != "all"})
        d["all"] = dict(interp=[max(d[f"{st:g}W"]["interp"][0] for st in STEPS_W),
                                min(d[f"{st:g}W"]["interp"][1] for st in STEPS_W)],
                        grid=[max(d[f"{st:g}W"]["grid"][0] for st in STEPS_W),
                              min(d[f"{st:g}W"]["grid"][1] for st in STEPS_W)],
                        worst_step_lo=min(STEPS_W, key=lambda st: -d[f"{st:g}W"]["interp"][0]),
                        worst_step_hi=min(STEPS_W, key=lambda st: d[f"{st:g}W"]["interp"][1]))
        out[label] = d
    out["offset +/-1 mV"] = {"all": dict(interp=[out["VOS +1 mV"]["all"]["interp"][0], out["VOS -1 mV"]["all"]["interp"][1]],
                                         grid=[out["VOS +1 mV"]["all"]["grid"][0], out["VOS -1 mV"]["all"]["grid"][1]])}
    return out


SENS_COLORS = {"nominal": "k", "VOS +1 mV": "tab:red", "VOS -1 mV": "tab:blue", "pack 6.4 V": "tab:orange",
               "pack 8.4 V": "tab:purple", "slope 65 dB/V": "tab:green", "slope 150 dB/V": "tab:brown"}


def plots_sens(fin, var, rundir, res, sw):
    """sens_curves.png: element-1 time error and shape error against VSH at the 2 W step (the worst step at
    nominal), one line per case, per setting, with the limits and the budget bands. sens_windows.png: the window
    of every case and step (interpolated bar, grid-edge ticks) against the compensated and stored-trim budgets."""
    title = f"{fin.upper()} {VAR[var]['short']}"
    bt = budget_totals(fin)
    fig, axes = plt.subplots(2, 3, figsize=(17, 9.5))
    for j, tset in enumerate(SETTINGS_MS):
        for label, *_ in SENS_CASES:
            rr = sorted([r for r in res if r["case_label"] == label and r["step_w"] == 2.0 and r["tset_ms"] == tset],
                        key=lambda r: r["vsh"])
            x = [r["vsh"] for r in rr]
            axes[0, j].plot(x, [r["first_err_pct"] for r in rr], "o-", ms=2.5, lw=1.0, color=SENS_COLORS[label],
                            label=label)
            axes[1, j].plot(x, [100 * r["first_shape_err"] for r in rr], "o-", ms=2.5, lw=1.0,
                            color=SENS_COLORS[label], label=label)
        for sg in (-1, 1):
            axes[0, j].axhline(sg * 10, color="r", lw=1.4, label="REQ-TX-005 +/-10 %" if sg > 0 else None)
            axes[0, j].axhline(sg * 100 * 0.5 / tset, color="k", lw=0.8, ls="--",
                               label="TC-SYS-013 +/-0.5 ms" if sg > 0 else None)
        axes[1, j].axhline(5, color="r", lw=1.4, label="TC-SYS-013 shape 5 %")
        axes[0, j].set_ylim(-40, 40)
        axes[1, j].set_ylim(0, 15)
        for i in range(2):
            ax = axes[i, j]
            for case, col, a_ in (("compensated", "tab:green", 0.10), ("stored", "tab:cyan", 0.18)):
                lo, hi = bt[case]["wc"]
                ax.axvspan(lo, hi, color=col, alpha=a_, label=f"{case} budget, worst-case sum" if (i == 0) else None)
            ax.axvline(0, color="0.4", lw=0.5)
            ax.grid(True, lw=0.3)
            ax.set_xlabel("VSH (V; < 0 earlier onset)", fontsize=8)
        axes[0, j].set_title(f"2 W step, {tset:.0f} ms: element 1 10-90 time error (% of setting)", fontsize=9)
        axes[1, j].set_title(f"2 W step, {tset:.0f} ms: element 1 shape error (% of full scale)", fontsize=9)
    axes[0, 0].legend(fontsize=6.5, loc="upper right", ncol=2)
    fig.suptitle(f"{title}: element 1 (trim from mid-rail) against VSH, 0.02 V steps, per sensitivity case "
                 f"(offset, pack, PA sub-threshold slope)", fontsize=10)
    fig.tight_layout()
    fig.savefig(rundir / "sens_curves.png", dpi=100)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(13, 8))
    y, yt, yl = 0, [], []
    for st in STEPS_W + ["all"]:
        key = f"{st:g}W" if st != "all" else "all"
        for label, *_ in SENS_CASES:
            w = sw[label][key]
            lo, hi = w["interp"]
            ax.plot([lo, hi], [y, y], color=SENS_COLORS[label], lw=3 if st == "all" else 2)
            ax.plot(w["grid"], [y, y], "|", color="k", ms=9)
            yt.append(y)
            yl.append(f"{'worst over steps' if st == 'all' else f'{st:g} W'}: {label}")
            y += 1
        if st == "all":
            w = sw["offset +/-1 mV"]["all"]
            ax.plot(w["interp"], [y, y], color="tab:red", lw=3, ls="--")
            ax.plot(w["grid"], [y, y], "|", color="k", ms=9)
            yt.append(y)
            yl.append("worst over steps: offset +/-1 mV (low edge of +1 mV, high edge of -1 mV)")
            y += 1
        y += 0.6
    for case, col, a_ in (("compensated", "tab:green", 0.10), ("stored", "tab:cyan", 0.20)):
        lo, hi = bt[case]["wc"]
        ax.axvspan(lo, hi, color=col, alpha=a_, label=f"{case} budget, worst-case sum {lo:+.3f} / {hi:+.3f} V")
        rlo, rhi = bt[case]["rss"]
        for xv in (rlo, rhi):
            ax.axvline(xv, color=col, lw=1.0, ls=":")
    ax.plot([], [], color="0.3", ls=":", label="dotted: the same budgets, RSS")
    ax.plot([], [], "|", color="k", ms=9, label="ticks: last passing 0.02 V grid point (conservative)")
    ax.set_yticks(yt)
    ax.set_yticklabels(yl, fontsize=6.5)
    ax.invert_yaxis()
    ax.set_xlim(-0.60, 0.32)
    ax.axvline(0, color="0.5", lw=0.6)
    ax.grid(True, axis="x", lw=0.3)
    ax.legend(fontsize=7, loc="upper left")
    ax.set_xlabel("VSH (V): element 1 passes REQ-TX-005 and TC-SYS-013 (time, shape) inside each bar (interpolated "
                  "edges);\na budget passes where its band lies inside the bar", fontsize=9)
    ax.set_title(f"{title}: element-1 windows per step and sensitivity case against the threshold budgets",
                 fontsize=10)
    fig.tight_layout()
    fig.savefig(rundir / "sens_windows.png", dpi=100)
    plt.close(fig)


# ---------------------------------------------------------------- expected FAIL states (revision 2, finding-11)
EXPECTED_FILE = HERE / "expected_states.json"
# Criteria that the design under test must pass in every run of the variant; --accept refuses to record a FAIL of
# these as expected (the revision 1 design must pass every element-3-to-8 keying criterion everywhere).
FORBIDDEN_FAIL = {
    "fix": ["t1090_req_tx005", "t1090_tc_sys013", "shape", "overshoot", "bw26", "sideband", "vgg", "setpoint"],
    "sweep1": ["t1090_req_tx005", "t1090_tc_sys013", "shape", "overshoot", "bw26", "sideband", "vgg", "setpoint"],
}
EXPECTED_WHY = {
    "asis": "the loop as TS-012 revision 4 writes it; expected to fail (record section 4.2)",
    "sweep0": "revision 0 design over a VSH sweep beyond its window; failures outside the window are the result "
              "(record section 4.3); REQ-TX-014 fails on the gate-off leakage estimate",
    "sweep1": "revision 1 design: elements 3 to 8 must pass everywhere (FORBIDDEN_FAIL); element 1 fails outside "
              "its window (the sweep goes beyond it); REQ-TX-014 fails on the leakage estimate",
    "fix": "revision 1 design at the budget corners: elements 3 to 8 must pass everywhere (FORBIDDEN_FAIL); element "
           "1 fails where the corner lies outside the finalist's window (record section 4.4.3); REQ-TX-014 fails "
           "on the leakage estimate",
    "sens": "element 1 over a VSH sweep beyond its window: failures outside the window are the result (record "
            "section 4.4.3)",
}


def check_expected(run_id, var, fails, accept=False):
    """Compare the run's FAIL states {criterion: [runs]} with expected_states.json. Returns (status, detail)."""
    actual = {k: sorted(v) for k, v in fails.items() if v}
    forb = [k for k in FORBIDDEN_FAIL.get(var, []) if k in actual]
    try:
        book = json.loads(EXPECTED_FILE.read_text())
    except FileNotFoundError:
        book = {}
    if accept:
        if forb:
            return "REFUSED", dict(forbidden_fail={k: actual[k] for k in forb})
        book[run_id] = dict(why=EXPECTED_WHY.get(var, ""), expected_fail=actual)
        # one line per criterion (run lists can hold hundreds of runs)
        lines = ["{"]
        items = sorted(book.items())
        for i, (rid, e) in enumerate(items):
            lines.append(f' {json.dumps(rid)}: {{"why": {json.dumps(e["why"])}, "expected_fail": {{')
            crit = list(e["expected_fail"].items())
            for j, (kk, vv) in enumerate(crit):
                lines.append(f'  {json.dumps(kk)}: {json.dumps(vv)}' + ("," if j < len(crit) - 1 else ""))
            lines.append(" }}" + ("," if i < len(items) - 1 else ""))
        lines.append("}")
        EXPECTED_FILE.write_text("\n".join(lines) + "\n")
        return "ACCEPTED", dict(expected_fail=actual)
    exp = book.get(run_id, {}).get("expected_fail")
    if exp is None:
        return "NO EXPECTED STATES", dict(actual_fail=actual, forbidden_fail={k: actual[k] for k in forb})
    unexp = {k: sorted(set(v) - set(exp.get(k, []))) for k, v in actual.items()}
    unexp = {k: v for k, v in unexp.items() if v}
    nowpass = {k: sorted(set(v) - set(actual.get(k, []))) for k, v in exp.items()}
    nowpass = {k: v for k, v in nowpass.items() if v}
    status = "AS EXPECTED" if not (unexp or nowpass or forb) else "DIFFERS"
    return status, dict(unexpected_fail=unexp, expected_fail_now_pass=nowpass,
                        forbidden_fail={k: actual[k] for k in forb})


def stage_deck(fin, var, rerun=True, accept=False):
    """rerun=False (stage 'replot') analyses and plots the existing .raw of the run without running LTspice;
    the deck must be unchanged (it is compared with the copy in the run directory)."""
    name, rows = gen_deck(fin, var)
    run_id = f"{DATE}-{REV}-{fin}-{var}"
    rundir = RESULTS / run_id
    rundir.mkdir(parents=True, exist_ok=True)
    if rerun:
        cmd = [str(WRAPPER), "-t", "900", "-o", str(rundir), "-b", str(HERE / name)]
        p = subprocess.run(cmd, capture_output=True, text=True)
        (rundir / "wrapper.txt").write_text(p.stderr[-4000:])
        print(p.stderr.strip().splitlines()[-1])
        if p.returncode != 0:
            print(f"LTspice run failed ({p.returncode})", file=sys.stderr)
            sys.exit(2)
    elif (HERE / name).read_bytes() != (rundir / name).read_bytes():
        print("replot refused: the generated deck differs from the deck of the run; rerun the deck", file=sys.stderr)
        sys.exit(2)
    res = analyse(fin, var, rundir, rows)
    sw = None
    if var == "sens":
        sw = sens_windows(res)
        plots_sens(fin, var, rundir, res, sw)
    elif var.startswith("sweep"):
        plot_window(fin, var, rundir, res)
    else:
        plots(fin, var, rundir, res)
        if len(corners_for(fin, var)) > 1:
            plots_corners(fin, var, rundir, res)
            plot_t1090(fin, var, rundir, res)
    clean = [{k: v for k, v in r.items() if k != "_trace"} for r in res]
    allpass = {k: all(r["pass"][k] for r in clean) for k in clean[0]["pass"]}
    fails = {k: [r["run"] for r in clean if not r["pass"][k]] for k in clean[0]["pass"]}
    summary = dict(run_id=run_id, revision=REV, finalist=FIN[fin]["name"], variant=VAR[var]["name"], deck=name,
                   limits=REQ, steps_w=VAR[var]["steps"], packs_v=VAR[var]["packs"],
                   drain_v={str(p): FIN[fin]["vd"][p] for p in VAR[var]["packs"]},
                   corners=[dict(vsh=c[0], vos=c[1]) for c in corners_for(fin, var)],
                   sens_cases=[dict(label=c[0], pack=c[1], vos=c[2], subth_db_per_v=c[3]) for c in
                               VAR[var].get("cases", [])],
                   threshold_budget={case: dict(terms=[dict(term=t[0], lo_v=t[1], hi_v=t[2], cls=t[3], source=t[4])
                                                       for t in terms], **{k: list(v) for k, v in
                                                                            budget_totals(fin)[case].items()})
                                     for case, terms in THRESHOLD_BUDGET[fin].items()},
                   leakage_dbm_modelled=FIN[fin]["pleak_dbm"], leakage_dbm_best_estimate=FIN[fin]["pleak_best_dbm"],
                   subthreshold_slope_db_per_v=SUBTH_DB_PER_V, pa_table_w=FIN[fin]["table"],
                   all_steps_pass=allpass, failing_runs=fails, steps=clean)
    if var.startswith("sweep"):
        summary["window_interp_v"] = {wh: {f"{st:g}W": window_interp(res, st, wh) for st in VAR[var]["steps"]}
                                      for wh in ("steady", "first")}
        summary["window_v"] = {wh: {f"{st:g}W": {f"{ts:g}ms": list(window_of(res, fin, st, ts, wh))
                                                  for ts in SETTINGS_MS} | {"all": list(window_of(res, fin, st, None, wh))}
                                    for st in VAR[var]["steps"]} for wh in ("steady", "first")}
    if sw is not None:
        summary["sens_windows_v"] = sw
    status, detail = check_expected(run_id, var, fails, accept)
    summary["expected_state_check"] = dict(status=status, file="hardware/sim/tx-keying/expected_states.json",
                                           **detail)
    (rundir / "result.json").write_text(json.dumps(summary, indent=1))
    keys = ["run", "case_label", "sub_db_per_v", "tset_ms", "pack", "vd", "step_w", "vsh", "vos", "pset_w", "ptop_w",
            "first_rise_ms", "first_fall_ms", "first_err_pct", "first_shape_err"] if var == "sens" else ["run", "tset_ms", "pack", "vd", "step_w", "vsh", "vos", "pset_w", "ptop_w", "rise_ms_min", "rise_ms_max",
            "fall_ms_min", "fall_ms_max", "t1090_err_ms", "t1090_err_pct", "worst_element", "shape_err_rise",
            "shape_err_fall", "overshoot_db", "bw26_hz", "side_max_db", "side_max_at_hz", "off60_hz", "vgg_max",
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
        if var == "sens":
            continue
        print(f"run {r['run']} {r['tset_ms']:g} ms {r['step_w']:g} W pack {r['pack']} VSH {r['vsh']:+.3f} "
              f"VOS {r['vos']*1e3:+.0f}m: top {r['ptop_w']:.2f} W err {r['t1090_err_pct']:+.1f}% "
              f"(rise {r['rise_ms_min']:.2f}..{r['rise_ms_max']:.2f} fall {r['fall_ms_min']:.2f}..{r['fall_ms_max']:.2f}) "
              f"shape {100*max(r['shape_err_rise'], r['shape_err_fall']):.1f}% bw26 {r['bw26_hz']:.0f} "
              f"side {r['side_max_db']:.1f} gate {r['at_gate_dbm']:.1f} vgg {r['vgg_max']:.2f} "
              f"{'' if all(r['pass'].values()) else 'FAIL:' + ','.join(k for k, v in r['pass'].items() if not v)}")
    if var.startswith("sweep"):
        print(json.dumps({wh: {st: w["all"] for st, w in d.items()} for wh, d in summary["window_v"].items()}))
        print(json.dumps({wh: {st: [round(x, 3) for x in w.get("all", [])] for st, w in d.items()}
                          for wh, d in summary["window_interp_v"].items()}))
    if sw is not None:
        for label, d in sw.items():
            print(f"sens {label}: interp {[round(x, 3) for x in d['all']['interp']]} grid {d['all']['grid']}")
    print(f"expected-state check {run_id}: {status} {json.dumps(detail)[:1500]}")
    if status in ("DIFFERS", "NO EXPECTED STATES", "REFUSED"):
        sys.exit(3)


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
        v = VAR["fix"]
        ktrim = v["ktrim"]
        rc = RIN * f["cf_mitig"] * ktrim / KTRIM
        for vd, sc in f["scale"].items():
            vg = np.array([x for x, _ in f["table"]])
            amp = np.sqrt(100 * np.array([p for _, p in f["table"]]) * sc * 10 ** (-LOSS_DB / 10))
            da = np.diff(amp) / np.diff(vg)
            am = 0.5 * (amp[1:] + amp[:-1])
            # tap factor 1 (2 and 5 W steps: every amplitude up to 5 W) and BOOST (0.5 and 1 W steps: amplitudes
            # up to 1 W at the load, which the diode sees BOOST times larger)
            for db, amax in ((1.0, 1e9), (BOOST, math.sqrt(100 * 1.0))):
                dd = db * np.interp(db * am, 0.5 * (A[1:] + A[:-1]), np.diff(D) / np.diff(A))
                k = np.where(am <= amax, ktrim * da * dd, 0.0)
                pts = (("steepest", int(np.argmax(k))),)
                if db == 1.0:
                    pts += (("near 5 W", int(np.argmin(np.abs(am - 22.36)))),)
                for label, i in pts:
                    wc = k[i] / rc
                    pm = 90 - math.degrees(math.atan(wc * RTH * CVGG)) - math.degrees(math.atan(wc * 1e3 * 4.7e-9))
                    out.append(dict(finalist=fin, drain_v=vd, tap_factor=db, point=label, amplitude_v=float(am[i]),
                                    crossover_hz=float(wc / 2 / math.pi), phase_margin_deg=float(pm)))
    return out


def stage_summary():
    runs = {}
    for fin in ("a4", "a5"):
        for var in ("asis", "fix"):
            p = RESULTS / f"{DATE}-{REV}-{fin}-{var}" / "result.json"
            runs[(fin, var)] = json.loads(p.read_text())
    sweeps = {(fin, var): json.loads((RESULTS / f"{DATE}-{REV}-{fin}-{var}" / "result.json").read_text())
              for fin in ("a4", "a5") for var in ("sweep0", "sweep1")}
    sens = {fin: json.loads((RESULTS / f"{DATE}-{REV}-{fin}-sens" / "result.json").read_text())
            for fin in ("a4", "a5")}
    outdir = RESULTS / f"{DATE}-{REV}-summary"
    outdir.mkdir(exist_ok=True)
    # worst case over steps, packs and corners, per setting
    fig, axes = plt.subplots(2, 3, figsize=(19, 10))

    # revision 2: the rev. 1 design runs are split by corner family, so the element-1 panels show the first
    # element of an over (nominal and stored-trim corners) apart from the power-on case without a stored trim
    # (compensated corners)
    def _family(fin, st):
        bt = budget_totals(fin)["compensated"]["wc"]
        return "compensated" if any(abs(st["vsh"] - round(b, 3)) < 1e-9 for b in bt) else "stored"
    groups = []
    for (fin, var), s_ in runs.items():
        if var == "fix":
            for fam, lab in (("stored", "rev. 1 design:\nnominal and\nstored trim"),
                             ("compensated", "rev. 1 design:\ncompensated\n(no stored trim)")):
                groups.append(((fin, var, lab), dict(s_, steps=[st for st in s_["steps"] if _family(fin, st) == fam])))
        else:
            groups.append(((fin, var, "as written\n(TS-012 rev. 4)" if var == "asis" else VAR[var]["short"]), s_))
    metrics = (("t1090_err_pct", 100 * REQ["t1090_rel_tol"], "% of setting",
                "10-90 % time error, elements 3 to 8, worst |value| (REQ-TX-005 10 %)", (0, 60), True),
               ("first_err_pct", 100 * REQ["t1090_rel_tol"], "% of setting",
                "10-90 % time error, element 1 (trim from mid-rail), worst |value| (REQ-TX-005 10 %)", (0, 60), True),
               ("shape_pct", 100 * REQ["shape_tol"], "% of full scale",
                "shape error, elements 3 to 8 (TC-SYS-013 5 %)", (0, 30), False),
               ("first_shape_pct", 100 * REQ["shape_tol"], "% of full scale",
                "shape error, element 1 (TC-SYS-013 5 %)", (0, 30), False),
               ("side_max_db", REQ["side_db"], "dB rel. total mean power",
                "worst 10 Hz cell beyond 750 Hz (REQ-TX-006 -60 dB)", (-100, -30), False),
               ("at_gate_dbm", REQ["keyup_dbm"], "dBm",
                "level at the drive gate, 1 ms after ramp end (REQ-TX-014 -30 dBm)", (-40, 20), False))

    def val_of(st, key):
        if key == "shape_pct":
            return 100 * max(st["shape_err_rise"], st["shape_err_fall"])
        if key == "first_shape_pct":
            return 100 * st.get("first_shape_err", float("nan"))
        return st.get(key, float("nan"))
    setcols = {3.0: "tab:blue", 5.0: "tab:orange", 8.0: "tab:purple"}
    worst = {}
    for ax, (key, lim, yl, t, ylim, absval) in zip(axes.flat, metrics):
        for gi, ((fin, var, glab), s_) in enumerate(groups):
            for si, tset in enumerate(SETTINGS_MS):
                vals = [val_of(st, key) for st in s_["steps"] if st["tset_ms"] == tset]
                vals = [abs(v) if absval else v for v in vals if not math.isnan(v)]
                val = max(vals)
                worst[f"{fin}-{var}-{glab.replace(chr(10), ' ')}-{key}-{tset:g}ms"] = val
                x = gi * 4 + si
                ok = val <= lim
                ax.bar(x, val - ylim[0], bottom=ylim[0], color=setcols[tset], edgecolor="k" if ok else "r",
                       linewidth=0.5 if ok else 2.0, label=f"{tset:.0f} ms setting" if gi == 0 else None)
                ax.text(x, min(val, ylim[1]) + 0.01 * (ylim[1] - ylim[0]), "ok" if ok else "FAIL", ha="center",
                        fontsize=6, color="k" if ok else "r")
        ax.axhline(lim, color="r", lw=1.2)
        ax.set_xticks([gi * 4 + 1 for gi in range(len(groups))])
        ax.set_xticklabels([f"{fin.upper()}\n{glab}" for (fin, var, glab), _ in groups], fontsize=6.5)
        ax.set_ylim(*ylim)
        ax.set_ylabel(yl, fontsize=8)
        ax.set_title(t, fontsize=8.5)
        ax.grid(True, axis="y", lw=0.3)
    axes[0, 0].legend(fontsize=8, loc="upper right")
    fig.suptitle("TS-012 keying analysis, revision 2: worst case per setting over power steps, packs and the record "
                 "corners (as written: 5 W only, no corners; rev. 1 design: compensated and stored-trim budget "
                 "corners with the offset). Red outline = fails", fontsize=10)
    fig.tight_layout()
    fig.savefig(outdir / "summary.png", dpi=110)
    plt.close(fig)

    # threshold windows against the budgets (revision 2: element 1 from the 0.02 V sensitivity runs, every case)
    win_cases = ["nominal", "offset +/-1 mV", "pack 6.4 V", "pack 8.4 V", "slope 65 dB/V", "slope 150 dB/V"]
    fig, ax = plt.subplots(figsize=(13, 9))
    y, yt, yl = 0, [], []
    for fin in ("a4", "a5"):
        bt = budget_totals(fin)
        for case, col in (("calibrated", "tab:purple"), ("compensated", "tab:green"), ("stored", "tab:cyan")):
            lo, hi = bt[case]["wc"]
            rlo, rhi = bt[case]["rss"]
            ax.plot([lo, hi], [y, y], color=col, lw=7, alpha=0.5, solid_capstyle="butt")
            ax.plot([rlo, rhi], [y, y], color=col, lw=2)
            ax.text(hi + 0.005, y, f"{lo:+.3f} / {hi:+.3f} (RSS {rlo:+.3f} / {rhi:+.3f})", fontsize=6, va="center")
            yt.append(y)
            yl.append(f"{fin.upper()} budget, {case}: worst-case sum (thick), RSS (thin)")
            y += 1
        for lab in win_cases:
            lo, hi = sens[fin]["sens_windows_v"][lab]["all"]["interp"]
            ax.plot([lo, hi], [y, y], color=SENS_COLORS.get(lab, "tab:red"), lw=2.5)
            ax.plot([lo, hi], [y, y], "|", color="k", ms=10)
            ax.text(hi + 0.005, y, f"{lo:+.3f} / {hi:+.3f}", fontsize=6, va="center")
            yt.append(y)
            yl.append(f"{fin.upper()} window, rev. 1 design, element 1, worst step: {lab}")
            y += 1
        for var, which, lab in (("sweep0", "steady", "rev. 0 design, every element"),
                                ("sweep1", "steady", "rev. 1 design, elements 3 to 8")):
            w = sweeps[(fin, var)]["window_interp_v"][which]
            lo = max(d["all"][0] for d in w.values())
            hi = min(d["all"][1] for d in w.values())
            full = (lo <= min(VSH_SWEEP) + 1e-9 and hi >= max(VSH_SWEEP) - 1e-9)
            ax.plot([lo, hi], [y, y], color="0.4" if full else "k", lw=2, ls=":" if full else "-")
            ax.plot([lo, hi], [y, y], "|", color="k", ms=10)
            yt.append(y)
            yl.append(f"{fin.upper()} window {lab}, worst step" + (" (whole sweep)" if full else ""))
            y += 1
        y += 0.7
    ax.set_yticks(yt)
    ax.set_yticklabels(yl, fontsize=6.5)
    ax.invert_yaxis()
    ax.axvline(0, color="0.5", lw=0.6)
    ax.set_xlim(-0.35, 0.45)
    ax.set_xlabel("VSH, PA curve shift against the feedforward table (V); a budget passes where it lies inside "
                  "the window of the same finalist")
    ax.grid(True, axis="x", lw=0.3)
    ax.set_title("Threshold windows (worst over steps and settings; element 1 from the 0.02 V sensitivity runs, "
                 "interpolated edges)\nagainst the threshold budgets of record section 3.2 (revision 2)", fontsize=9.5)
    fig.tight_layout()
    fig.savefig(outdir / "windows.png", dpi=110)
    plt.close(fig)

    # margins of every element-1 window case against every budget (revision 2, finding-13); > 0 inside
    margins = {}
    for fin in ("a4", "a5"):
        bt = budget_totals(fin)
        sw = sens[fin]["sens_windows_v"]
        margins[fin] = {}
        for lab in win_cases:
            wlo, whi = sw[lab]["all"]["interp"]
            glo, ghi = sw[lab]["all"]["grid"]
            margins[fin][lab] = {"window_interp": [wlo, whi], "window_grid": [glo, ghi]}
            for case in ("compensated", "stored"):
                for kind in ("wc", "rss"):
                    blo, bhi = bt[case][kind]
                    margins[fin][lab][f"{case}_{kind}"] = dict(
                        lo=blo - wlo, hi=whi - bhi, min=min(blo - wlo, whi - bhi),
                        min_grid=min(blo - glo, ghi - bhi), verdict="PASS" if min(blo - wlo, whi - bhi) >= 0 else "FAIL")
        # sub-threshold slope at which the stored-trim worst-case margin reaches zero (linear between cases)
        pts = [(65.0, margins[fin]["slope 65 dB/V"]["stored_wc"]["min"]),
               (100.0, margins[fin]["nominal"]["stored_wc"]["min"]),
               (150.0, margins[fin]["slope 150 dB/V"]["stored_wc"]["min"])]
        zero = None
        for (s0, m0), (s1, m1) in zip(pts[:-1], pts[1:]):
            if (m0 >= 0) != (m1 >= 0):
                zero = s0 + m0 * (s1 - s0) / (m0 - m1)
        margins[fin]["stored_wc_margin_vs_slope"] = dict(points=pts, zero_crossing_db_per_v=zero)
    summ_margins = margins
    # element 1 in the 'fix' record runs, per corner (every pack, step and setting)
    fix_el1 = {}
    for fin in ("a4", "a5"):
        s_ = runs[(fin, "fix")]
        d = {}
        for c in s_["corners"]:
            rr = [st for st in s_["steps"] if abs(st["vsh"] - c["vsh"]) < 1e-9 and abs(st["vos"] - c["vos"]) < 1e-12]
            bad = [st["run"] for st in rr if not (st["pass"]["first_t1090_req_tx005"] and
                                                   st["pass"]["first_t1090_tc_sys013"] and st["pass"]["first_shape"])]
            d[corner_label(c["vsh"], c["vos"])] = dict(runs=len(rr), failing=len(bad), failing_runs=bad,
                                                       worst_err_pct=max(abs(st["first_err_pct"]) for st in rr),
                                                       worst_shape_pct=100 * max(st["first_shape_err"] for st in rr))
        fix_el1[fin] = d
    summ = {f"{fin}-{var}": dict(failing_criteria={k: len(v) for k, v in s["failing_runs"].items() if v},
                                 steps=len(s["steps"]),
                                 bw26_hz_max=max(st["bw26_hz"] for st in s["steps"]),
                                 side_db_max=max(st["side_max_db"] for st in s["steps"]),
                                 keyup_at_gate_dbm_max=max(st["at_gate_dbm"] for st in s["steps"]),
                                 loop_tail_at_gate_dbm_max=max(st["loop_tail_at_gate_dbm"] for st in s["steps"]),
                                 shape_err_max=max(max(st["shape_err_rise"], st["shape_err_fall"]) for st in s["steps"]),
                                 t1090_err_pct_max=max(abs(st["t1090_err_pct"]) for st in s["steps"]),
                                 first_err_pct_max=max(abs(st.get("first_err_pct", 0)) for st in s["steps"]),
                                 first_shape_err_max=max(st.get("first_shape_err", 0) for st in s["steps"]))
            for (fin, var), s in runs.items()}
    summ["worst_per_setting"] = worst
    summ["element1_window_margins_v"] = summ_margins
    summ["fix_element1_by_corner"] = fix_el1
    summ["expected_state_checks"] = {f"{fin}-{var}": json.loads((RESULTS / f"{DATE}-{REV}-{fin}-{var}" /
                                                                 "result.json").read_text())
                                     .get("expected_state_check", {}).get("status")
                                     for fin in ("a4", "a5") for var in ("asis", "sweep0", "fix", "sweep1", "sens")}
    summ["windows_interp_v"] = {f"{fin}-{var}": sweeps[(fin, var)]["window_interp_v"] for (fin, var) in sweeps}
    summ["threshold_budget_totals_v"] = {fin: budget_totals(fin) for fin in ("a4", "a5")}
    rip = pwm_ripple()
    summ["pwm_ripple"] = rip
    summ["loop_margin_mitigated"] = loop_margin()
    fig, ax = plt.subplots(figsize=(10, 5.4))
    labs, vals, cols = [], [], []
    for r in rip:
        for path, key in (("feedforward", "ff_sideband_dbc"), ("reference", "ref_sideband_dbc")):
            labs.append(f"{r['finalist'].upper()} {path}\n{r['pwm_hz']/1e3:.1f} kHz ({r['bits']}-bit)")
            vals.append(r[key])
            cols.append("tab:green" if r[key] <= REQ["side_db"] else "tab:red")
    x = np.arange(len(labs))
    ax.bar(x, np.array(vals) + 120, bottom=-120, color=cols)
    for xi, v in zip(x, vals):
        m_ = REQ["side_db"] - v
        ax.text(xi, v + 1.5, f"{v:.1f}\n" + (f"margin {m_:.1f} dB" if m_ >= 0 else f"over by {-m_:.1f} dB"),
                ha="center", fontsize=6)
    ax.axhline(REQ["side_db"], color="k", lw=1.2, label="REQ-TX-006: -60 dB beyond 750 Hz")
    ax.set_xticks(x)
    ax.set_xticklabels(labs, rotation=90, fontsize=7)
    ax.set_ylabel("PWM carrier sideband (dBc, each side)")
    ax.set_ylim(-120, 0)
    ax.grid(True, axis="y", lw=0.3)
    ax.legend(fontsize=8)
    sl = {r["finalist"]: r["pa_slope_v_per_v"] for r in rip}
    ax.set_title("Mitigated loop: PWM carrier sidebands at duty 0.5 (analytic; green pass, red fail; value and "
                 "margin to -60 dB on each bar)\nsteepest PA slope at the highest drain voltage: A5 "
                 f"{sl['a5']:.1f} V/V, A4 {sl['a4']:.1f} V/V (ratio {sl['a5'] / sl['a4']:.1f})", fontsize=9)
    fig.tight_layout()
    fig.savefig(outdir / "pwm_ripple.png", dpi=120)
    plt.close(fig)
    # design-rule checks of this stage (revision 2, finding-11): the feedforward PWM at 122 kHz passes REQ-TX-006
    # for both finalists, the loop phase margin is at least 45 degrees everywhere, and every deck run's FAIL
    # states are as expected
    rules = dict(
        pwm_122k_feedforward_passes=all(r["ff_sideband_dbc"] <= REQ["side_db"] for r in rip if r["bits"] == 10),
        phase_margin_ge_45=all(m["phase_margin_deg"] >= 45.0 for m in summ["loop_margin_mitigated"]),
        every_run_as_expected=all(v == "AS EXPECTED" for v in summ["expected_state_checks"].values()),
    )
    summ["design_rule_checks"] = rules
    (outdir / "summary.json").write_text(json.dumps(summ, indent=1))
    shutil.copy(Path(__file__), outdir / Path(__file__).name)
    print(json.dumps({k: summ[k] for k in ("pwm_ripple", "element1_window_margins_v", "fix_element1_by_corner",
                                           "expected_state_checks", "design_rule_checks")}, indent=1))
    if not all(rules.values()):
        print("summary: a design-rule check fails", file=sys.stderr)
        sys.exit(3)


if __name__ == "__main__":
    if sys.argv[1] == "detchar":
        stage_detchar()
    elif sys.argv[1] == "deck":
        stage_deck(sys.argv[2], sys.argv[3], accept="--accept" in sys.argv[4:])
    elif sys.argv[1] == "replot":
        stage_deck(sys.argv[2], sys.argv[3], rerun=False, accept="--accept" in sys.argv[4:])
    elif sys.argv[1] == "summary":
        stage_summary()
    else:
        sys.exit(__doc__)
