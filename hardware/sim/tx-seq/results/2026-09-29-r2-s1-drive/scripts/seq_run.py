#!/usr/bin/env python3
"""WP-PDR-23a: key-down and key-up sequence timing, T/R relay drive and hold (D-5), ICD-TX-SW timing table.

Analysis record: docs/design/analysis/sequencer-timing.md (revision 2). Plan: docs/plan/pdr-work-plan.md
revision 6, WP-PDR-23a (section 3.0 row 23). Design basis: TS-012 revision 7, section 7.3 "Revision 6: key-down
sequence, frequency check and PA permit", section 8.1, design items D-5, D-11, D-17 and D-18.
Revision 1 (the Major findings of the independent review and of its software assurance pair): the G5V-2-H1
must-operate slope from its datasheet graph, the H1 maximum-voltage curve (applies to the imposed voltage, so
the PWM peak), the release at -10 C, the stale-ratio key-down case (R-FRESH-2), and option E (the H1 coil fed
through a hardware coil-supply limiter with a static T/R drive, no PWM) as the recommendation. New run ids
2026-09-29-r1-*; the revision 0 runs stay as the record of revision 0, each with its own script copy.
Revision 2 (the two new Major findings of the delta iteration, finding-13 and finding-14): the option E rail floor
restated from the REQ-SYS-097 tolerance (a transmission can start at 6.30 V) and the WP-PDR-21 revision 3 feed
bound with its modelled key-down current (f1070cf), with a discharge allowance during the over; the limiter
dropout requirement tightened to 0.10 V; K15-E evaluated at the restated floor; and the stale-ratio case stated on
the ratio's age at the key-down (receive age up to 1.083 s, frequency-budget.md FR-2r), not on the over length.
New run ids 2026-09-29-r2-*; the revision 1 runs stay as the record of revision 1.

Usage (repo root, repo venv):
    .venv/bin/python hardware/sim/tx-seq/seq_run.py all            # s1, s2, s3, s4 in order
    .venv/bin/python hardware/sim/tx-seq/seq_run.py s1|s2|s3|s4
    .venv/bin/python hardware/sim/tx-seq/seq_run.py all --expect   # also compare every verdict with
                                                                    # expected_states.json (exit 3 if any differs)
Stages (each writes hardware/sim/tx-seq/results/<run-id>/ with result.json, result.md, plots and a copy of the
scripts; s1 and s2 also the deck, the LTspice .log and .raw):
    s1  LTspice DC: relay coil current and driver drop for the 2N3904 (BOM row 12) and AO3400A (BOM row 22)
        low-side drivers, both coils (G5V-2 DC5 standard and G5V-2-H1 DC5), over supply, coil resistance and
        driver temperature
    s2  LTspice transient: coil current rise at pull-in, PWM hold average and ripple, decay through the
        freewheel diode, for the drive options; cross-checked against the closed-form R-L results
    s3  Python electromechanical relay model (relay_model.py) anchored to the datasheet: operate time at the
        pull-in corners for each drive option, release time with the freewheel diode, hold margin
    s4  Sequence model: the key-down and key-up schedules, every pass criterion, the ICD-TX-SW timing table
        (CSV and Markdown), the timing diagram docs/reviews/PDR/figures/timing-diagram.png and the budget plots
Exit status: 0 when every criterion passes and every check passes; 1 when every check passes and at least one
criterion is FAIL or OPEN (the results are valid and report it); 2 when a check fails (do not use the
results). With --expect: 3 if any verdict differs from expected_states.json, else 0 (checks must pass).
LTspice runs only through tools/ltspice-batch.sh (ACC-LTSPICE-001); .raw files are read with spicelib.
Developer evidence (05 section 9.1): this script has no TV record.
"""

from __future__ import annotations

import hashlib
import json
import math
import os
import shutil
import subprocess
import sys
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Rectangle  # noqa: E402
from spicelib import RawRead  # noqa: E402

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
sys.path.insert(0, str(HERE))
import relay_model as rm  # noqa: E402

BATCH = REPO / "tools" / "ltspice-batch.sh"
FIG = REPO / "docs" / "reviews" / "PDR" / "figures" / "timing-diagram.png"
RUNS = {"s1": "2026-09-29-r2-s1-drive", "s2": "2026-09-29-r2-s2-coil", "s3": "2026-09-29-r2-s3-operate",
        "s4": "2026-09-29-r2-s4-sequence"}
EXPECTED = HERE / "expected_states.json"

# plot style: reference palette slots 1 to 4 (light), text in ink tokens, 2 px lines
C1, C2, C3, C4 = "#2a78d6", "#eb6834", "#1baf7a", "#eda100"
C7 = "#4a3aa7"
INK, INK2, GRID = "#0b0b0b", "#52514e", "#d9d8d4"
plt.rcParams.update({"font.size": 9, "axes.edgecolor": INK2, "axes.labelcolor": INK, "xtick.color": INK2,
                     "ytick.color": INK2, "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.6,
                     "lines.linewidth": 2.0, "figure.dpi": 130, "savefig.dpi": 130, "axes.titlesize": 10,
                     "legend.fontsize": 8, "legend.frameon": False})

# ------------------------------------------------------------------------------------------------------------
# Inputs. Class: R requirement, D datasheet, DD derived from datasheets, A allocation (a design choice this
# analysis proposes), E estimate. Every entry is printed into the s4 result with its class and source.
# ------------------------------------------------------------------------------------------------------------
INPUTS = {
    # key input and keyer (requirements at HEAD)
    "t_sample": (1.0, "ms", "R", "REQ-SW-KEYER-019 key inputs sampled every 1.000 ms"),
    "t_assert": (2.0, "ms", "R", "REQ-SW-KEYER-018/020: key-down asserted within 2 ms of the first closed sample "
                               "(2 consecutive closed samples)"),
    "t_paddle": (3.0, "ms", "R", "REQ-SYS-043 paddle closure to element start at most 3 ms"),
    "t_keyer_tr": (0.02, "ms", "A", "keyer test point written in the same TIMER0 alarm service as the T/R drive, "
                                    "after it, within 20 us"),
    # synthesizer and frequency check (TS-012 7.3 revision 6; frequency-budget.md C-14; RP2350 datasheet 8.1.4)
    "t_i2c": (0.650, "ms", "DD", "C6 changeover writes, four bursts of 28 data bytes at 400 kHz, no reg 177 reset "
                                 "(frequency-budget.md revision 2 at 7593cea, case RL-2; under review, INSP-056)"),
    "t_pll_alloc": (1.0, "ms", "A", "TS-012 7.3 rev 6: 1 ms allocated for the writes and the PLL to settle "
                                    "(WP-PDR-20a confirms the relock time)"),
    "t_fc0_delay": (0.0006, "ms", "D", "FC0_DELAY at most 7 clk_ref cycles (Table 582) at 12 MHz"),
    "t_fc0_i12": (4.096, "ms", "D", "FC0 interval 12: '1 us * 2**interval' (Table 582 wording; 0.98 us * 4096 = "
                                    "4.014 ms is the device value, 4.096 ms bounds it)"),
    "t_fc0_i13": (8.192, "ms", "D", "FC0 interval 13, same convention"),
    "t_sw_check": (2.0, "ms", "A", "frequency-budget.md C-14: lock-status read, compare and PA_EN write"),
    # relay (Omron G5V-2 datasheet, as read for TS-012 revision 3 and re-read for this record)
    "t_op_ds": (7.0, "ms", "D", "G5V-2 operate time 7 ms max (rated voltage, coil at 23 C)"),
    "t_rel_ds": (3.0, "ms", "D", "G5V-2 release time 3 ms max (rated voltage, coil at 23 C)"),
    "t_bounce": (0.5, "ms", "DD", "G5V-2 bounce-time distribution graph, 0.3 to 0.5 ms (graph read, TS-012 rev 3)"),
    "t_settle": (7.5, "ms", "A", "configured 'T/R in TX and settled' prerequisite (07 section 14.2 row h): "
                                 "operate 7 ms + bounce 0.5 ms"),
    # PA permit, drive and envelope (TS-012 7.3 rev 6, keying-ts012.md, D-18)
    "L": (10.0, "ms", "A", "constant lead-in: T/R command to ramp start, every element of the over (TS-012 7.3)"),
    "t_lead": (2.0, "ms", "A", "TX_KEY rises 2 ms before each ramp (keying-ts012.md timing)"),
    "t_drv": (1.0, "ms", "A", "GVA-84+ supply and bias settled within 1 ms of the D-18 gate permitting (allocation; "
                              "pa-permit-gate-d18.md rev 0, under review: powered within 1.2 us, turn-on at most 0.25 ms)"),
    "t_tail": (1.0, "ms", "A", "TX_KEY falls 1 ms after each ramp ends (keying-ts012.md timing)"),
    "t_pwm_env": (4096 / 96e6 * 1e3, "ms", "DD", "envelope reference PWM period, 12 bit at clk_sys 96 MHz (D-12 C1): "
                                                 "the ramp start is quantised to it"),
    "ramp_set": ([3.0, 5.0, 8.0], "ms", "R", "REQ-SYS-014 raised-cosine 10-90 % time settings 3 to 8 ms"),
    "wpm": ([5, 15, 25, 50], "WPM", "R", "REQ-SW-KEYER-015 speed range 5 to 50 WPM"),
    "hang_dits": ([3, 30], "dits", "R", "REQ-SYS-044 / REQ-SW-KEYER-032 hang 3 to 30 dits (TBR)"),
    # end of over and faults
    "t_ord": (0.5, "ms", "A", "end of over: PA_EN low, CLK1 disable (3 I2C bytes), prescaler off, then T/R drive "
                              "off, all inside 0.5 ms (07 section 14.2 row b order)"),
    "t_rx_alloc": (50.0, "ms", "R", "REQ-SYS-036 receive sensitivity within 3 dB of MDS within 50 ms (TBR) after "
                                    "hang expiry"),
    "t_rel_alloc": (30.0, "ms", "A", "share of REQ-SYS-036 given to the T/R release (ordering, release, bounce); "
                                     "the receiver chain keeps 20 ms (WP-PDR-19 / 23b, TC-SYS-024)"),
    "t_inhibit_sw": (1.0, "ms", "A", "inhibit detected to PA_EN low (SW-SAFE service)"),
    "t_inhibit_hw": (0.1, "ms", "E", "PA_EN low to the D-18 gate clamping VGG and the module off (clamp FET and "
                                     "logic in microseconds; 0.1 ms bound)"),
    "t_rf_off_req": (20.0, "ms", "R", "REQ-SYS-004 RF-off level within 20 ms (TBR) of detecting an inhibit"),
    "t_sidetone": (0.1, "ms", "A", "sidetone PWM started within 0.1 ms of the keyer edge"),
    "t_sidetone_req": (4.0, "ms", "R", "REQ-SYS-159 sidetone within 4 ms (TBR) of the contact closure"),
    "t_key_rf_req": (15.0, "ms", "R", "REQ-SYS-160 RF rise within 15 ms (TBR) of each straight-key closure"),
    "t_leadin_req": (12.0, "ms", "R", "REQ-SYS-161 constant lead-in at most 12 ms (TBR)"),
    "t_leadin_eq": (0.5, "ms", "R", "TC-SYS-102 lead-in equality tolerance 0.5 ms (test author's, from REQ-SYS-042)"),
    # D-5 relay drive and hold
    "t_pi": (25.0, "ms", "A", "D-5: T/R drive at 100 % from t0 for 25 ms, then the hold PWM"),
    "f_hold": (25.0, "kHz", "A", "D-5 hold PWM frequency (above the audio band; ripple under 2 %)"),
    "v_hold_h1": (5.0, "V", "A", "D-5 with the H1 coil: hold at the rated 5.0 V average from the pack rail"),
    "hold_frac_std": (0.63, "-", "E", "D-5 with the standard coil: hold at 63 % of the coil voltage (thermal note's "
                                      "assumption; no datasheet hold value)"),
    # revision 1: datasheet graph reads (Omron G5V-2 K046-E1-06, PDF SHA-256 7a0edd84...fc9d55a, page 2)
    "s_mo_h1": ([0.0048, round(0.0051 * 65.0 / 62.0, 6)], "1/K", "DD",
                "G5V-2-H1 must-operate voltage slope, referenced to the 75 % worst unit at 23 C: 0.48 %/K, and 0.51 %/K "
                "taken from 20 C (0.5347 %/K from 23 C, the same must-operate voltage at 85 C). Graph 'Ambient "
                "Temperature vs. Must Operate or Must Release Voltage' (10 samples): review finding-2 read 0.48 to 0.51 "
                "%/K; the author's re-read gives 0.46 to 0.49 %/K; the band bounds both and reproduces the review's "
                "operate times (record section 3.3)"),
    "vmax_h1": ([[0.0, 180.0], [54.0, 180.0], [70.0, 151.0]], "C, %", "DD",
                "G5V-2-H1 3 to 24 VDC maximum coil voltage against ambient, graph 'Ambient Temperature vs. Maximum Coil "
                "Voltage' read: 180 % to about 54 C, straight to 151 % at 70 C (the ambient rating). Ratings note 3: "
                "'the highest voltage that can be imposed on the relay coil'; graph note: the maximum of a varying "
                "supply range, not a continuous voltage. It therefore limits the imposed (peak) voltage"),
    "t_amb_relay": ([61.4, 67.1, 70.0], "C", "DD", "relay ambient: duty-limited and continuous bay air (thermal-ts012.md) "
                                                  "and the H1 ambient rating"),
    # revision 1: option E, the coil-supply limiter (a part requirement; the part is chosen at WP-PDR-37 and 38)
    "v_lim_set": (6.30, "V", "A", "option E: limiter set point between the switched pack rail and the coil"),
    "v_lim_tol": (0.02, "-", "A", "option E: set-point tolerance over -10 to 85 C (part requirement, OD-42 gate read)"),
    "v_lim_do": (0.10, "V", "A", "option E: dropout at up to 60 mA over -10 to 85 C (part requirement, gate read; "
                                 "revision 2, finding-13: tightened from 0.20 V)"),
    "v_rx_min": (6.35, "V", "R, E", "options C and D only (revision 1 basis, kept for the comparison): lowest switched "
                                    "pack rail in receive (6.4 V less 0.05 V feed drop)"),
    "v_kd_min": (5.45, "V", "R, E", "options C and D only (revision 1 basis, kept for the comparison): lowest switched "
                                    "pack rail in key-down (6.35 V less 0.9 V at 2 A)"),
    # revision 2 (finding-13): the option E rail floor from the requirement tolerance and the WP-PDR-21 feed bound
    "v_pack_floor": (6.30, "V", "R", "lowest pack at which a transmission can start: REQ-SYS-097 3.20 V -0.05 V per "
                                    "cell, measured in receive (both cells at 3.15 V)"),
    "r_feed_hot": (0.5646, "ohm", "DD", "feed bound, +45 C key-down, every part at its datasheet maximum or upper value "
                                       "(pa-drive-ts012.md revision 3 section R3.5, f1070cf; run_a5_r3.py feed3_at)"),
    "r_feed_cold": (0.614, "ohm", "DD", "feed bound, -10 C key-down (same source)"),
    "r_feed_lever": (0.3841, "ohm", "DD", "feed at +45 C key-down with the WP-PDR-21 C2 lever: P-FET pair of at most "
                                         "0.06 ohm (an owner decision in pa-drive-ts012.md revision 3, not adopted)"),
    "i_kd_hot": (2.140, "A", "DD", "largest pack current at key-down at 6.4 V over the +45 C key-down corners with the "
                                  "feed bound (WP-PDR-21 run 2026-09-29-r3-p4-power-a5-design, .raw read; 5 V bus "
                                  "included). Taken at 6.30 V too: the current falls with the pack, so this bounds it"),
    "i_kd_cold": (2.215, "A", "DD", "the same over the -10 C key-down corners with the feed bound"),
    "i_kd_lever": (2.233, "A", "DD", "the same over the +45 C key-down corners with the lever feed"),
    "i_rx": (0.111, "A", "E", "current through the feed in receive (revision 1 basis: 0.05 V at 0.45 ohm)"),
    "i_coil_pi": (0.035, "A", "E", "the relay coil's own current at pull-in, added to the receive current (hot unit "
                                   "about 0.032 A)"),
    "v_discharge": (0.10, "V", "E", "pack fall during an over below its receive reading at the start (review "
                                   "finding-13 figure; a sensitivity is plotted in s3-keydown-hold.png)"),
    "t_air_relay_c": (67.1, "C", "DD", "relay bay air, continuous (thermal-ts012.md), for the coil's own temperature"),
    "rth_coil": (80.0, "K/W", "E", "coil-to-air thermal resistance, upper end of the 40 to 80 K/W band"),
    "v_pack_max": (8.40, "V", "R", "full pack (REQ-SYS-012)"),
    # revision 1: the stale-ratio key-down case (frequency-budget.md revision 4, R-FRESH-1 and R-FRESH-2)
    "t_refresh": (82.8, "ms", "DD", "one ratio refresh: 50 ms stage settle plus the 32.768 ms interval-15 count "
                                   "(frequency-budget.md revision 4 at d030ce2, B-19)"),
    "a_kd": (10.0, "s", "A", "largest ratio age for the interval-12 check at key-down (frequency-budget.md A_kd)"),
    "age_rx_max": (1.083, "s", "DD", "largest ratio age in receive: 1 s refresh period plus the 82.8 ms refresh "
                                     "(frequency-budget.md revision 4, FR-2r); revision 2, finding-14"),
    # revision 1: the K12 backstop and the PA-path gate see TR_DRV (SA finding-1)
    "t_rearm": (30.0, "ms", "A", "proposed to WP-PDR-26: the K12 backstop re-arms only after TR_DRV has been low "
                                 "continuously for at least this long (at or above the KU-07 release maximum)"),
}


def val(k):
    return INPUTS[k][0]


def slope_txt() -> str:
    return " to ".join(f"{100 * x:.3g}" for x in val("s_mo_h1")) + " %/K"


def vmax_h1_pct(t_amb: float) -> float:
    """G5V-2-H1 maximum coil voltage (% of rated) at ambient t_amb, graph read (INPUTS vmax_h1)."""
    pts = np.array(val("vmax_h1"))
    return float(np.interp(t_amb, pts[:, 0], pts[:, 1]))


def rail_rx_floor() -> float:
    """Revision 2 (finding-13): lowest switched pack rail at the pull-in (receive state, t0): the pack at the
    REQ-SYS-097 floor less the receive current and the coil's own current through the larger feed bound."""
    return val("v_pack_floor") - (val("i_rx") + val("i_coil_pi")) * max(val("r_feed_hot"), val("r_feed_cold"))


def rail_kd_floor(case: str = "hot", discharge: bool = True) -> float:
    """Revision 2 (finding-13): lowest switched pack rail in key-down. case: 'hot' (+45 C, feed bound as read),
    'cold' (-10 C, feed bound), 'lever' (+45 C, WP-PDR-21 C2 lever). discharge: less the fall during an over."""
    i, r = {"hot": ("i_kd_hot", "r_feed_hot"), "cold": ("i_kd_cold", "r_feed_cold"),
            "lever": ("i_kd_lever", "r_feed_lever")}[case]
    return val("v_pack_floor") - val(i) * val(r) - (val("v_discharge") if discharge else 0.0)


def v_mo_worst(t_coil: float, s_mo: float) -> float:
    """Worst unit's must-operate voltage (V) at coil temperature t_coil for an H1 slope s_mo (closed form)."""
    return rm.VPU_FRAC * 5.0 * rm.k_mo(t_coil, s_mo)


def v_lim_out(v_in: float, corner: str = "nom") -> float:
    """Option E limiter output: min(set point at the corner, input less the dropout)."""
    k = {"min": 1 - val("v_lim_tol"), "nom": 1.0, "max": 1 + val("v_lim_tol")}[corner]
    return min(val("v_lim_set") * k, v_in - val("v_lim_do"))


# Drive options for the T/R relay (section 3.2 of the record). v: supply at the coil (min, nom, max), V.
OPTIONS = {
    "A": {"coil": "std", "driver": "q", "v": (4.75, 5.00, 5.25),
          "label": "A: standard DC5 on the 5 V bus, 2N3904 (TS-012 8.3 as listed)"},
    "B": {"coil": "std", "driver": "m", "v": (4.75, 5.00, 5.25),
          "label": "B: standard DC5 on the 5 V bus, AO3400A"},
    "C": {"coil": "h1", "driver": "q", "v": (6.35, 7.40, 8.40),
          "label": "C: H1 DC5 on the switched pack rail, 2N3904"},
    "D": {"coil": "h1", "driver": "m", "v": (6.35, 7.40, 8.40),
          "label": "D: H1 DC5 on the switched pack rail, AO3400A"},
    # revision 1: E, the H1 coil through the coil-supply limiter, AO3400A on a static TR_DRV (no PWM). Coil supply
    # at pull-in: min(set point low, receive rail less dropout); nominal; set point high
    "E": {"coil": "h1", "driver": "m",
          # revision 2: the receive floor is rail_rx_floor() (finding-13), filled in below
          "v": (None, INPUTS["v_lim_set"][0], INPUTS["v_lim_set"][0] * (1 + INPUTS["v_lim_tol"][0])),
          "label": "E: H1 DC5 through a 6.3 V limiter, AO3400A, static drive"},
}
# revision 2 (finding-13): option E at pull-in is the lower of the set point's low corner and the restated receive
# floor less the dropout
OPTIONS["E"]["v"] = (min(val("v_lim_set") * (1 - val("v_lim_tol")), rail_rx_floor() - val("v_lim_do")),
                     OPTIONS["E"]["v"][1], OPTIONS["E"]["v"][2])
# Coil temperature at pull-in (C): datasheet reference, nominal, hot corners (section 3.2 table T)
T_COIL = {"cold": -10.0, "ref": 23.0, "nom": 49.0, "hot_dl": 75.0, "hot_c": 85.0}   # cold: REQ-SYS-114 (revision 1)
BOUNCE_MS = 0.5
QBJT_VCESAT_DS = 0.30    # V, onsemi 2N3904 VCE(sat) max at IC 50 mA, IB 5 mA (datasheet); used as a floor

# 1N4148 (LTspice standard.dio, OnSemi): Is, N * Vt at the deck temperature 27 C, Rs (s2 closed form)
D1N4148 = (2.52e-9, 1.752 * 1.380649e-23 * 300.15 / 1.602177e-19, 0.568)
# s3 release: freewheel with no junction drop and Rs only, which gives the slowest decay (conservative at any
# temperature: the real forward drop only speeds the decay)
D_SLOW = (1.0, 1e-12, 0.568)

AO3400A_MODEL = (".model AO3400A VDMOS(Vto=1.0 Kp=40 Rd=8m Rs=8m Rg=2 Cgs=550p Cgdmax=150p Cgdmin=40p "
                 "Cjo=120p Is=1p Rb=10m mfg=fit_E Vds=30 Ron=36m)\n"
                 # copied from LTspice 26.0.2 lib/cmp/standard.dio and standard.bjt (the batch deck has no library)
                 ".model 1N4148 D(Is=2.52n Rs=.568 N=1.752 Cjo=4p M=.4 tt=20n Iave=200m Vpk=75 mfg=OnSemi type=silicon)\n"
                 ".model 2N3904 NPN(IS=1E-14 VAF=100 Bf=300 IKF=0.4 XTB=1.5 BR=4 CJC=4E-12 CJE=8E-12 RB=20 RC=0.1 "
                 "RE=0.1 TR=250E-9 TF=350E-12 ITF=1 VTF=2 XTF=3 Vceo=40 Icrating=200m mfg=NXP)")


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def rundir(key: str) -> Path:
    d = HERE / "results" / RUNS[key]
    d.mkdir(parents=True, exist_ok=True)
    return d


def run_ltspice(deck: Path, out: Path, timeout: int = 600) -> dict:
    cmd = [str(BATCH), "-t", str(timeout), "-o", str(out), "-b", str(deck)]
    p = subprocess.run(cmd, capture_output=True, text=True)
    prov = [ln for ln in p.stderr.splitlines() if "ltspice-batch" in ln]
    if p.returncode != 0:
        sys.stderr.write(p.stdout + p.stderr)
        raise SystemExit(2)
    log = out / (deck.stem + ".log")
    lines = log.read_text(errors="replace").splitlines() if log.exists() else []
    warn = [ln for ln in lines if "warning" in ln.lower() or "error" in ln.lower()]
    return {"deck": deck.name, "deck_sha256": sha(deck), "exit": p.returncode,
            "log_first_line": lines[0] if lines else "", "log_warnings": warn, "wrapper_provenance": prov[-3:]}


def copy_scripts(out: Path):
    sd = out / "scripts"
    sd.mkdir(exist_ok=True)
    for f in ("seq_run.py", "relay_model.py"):
        shutil.copy2(HERE / f, sd / f)


def write_json(out: Path, obj: dict):
    (out / "result.json").write_text(json.dumps(obj, indent=2, default=float) + "\n")


def raw_size_manifest(out: Path) -> list[dict]:
    """CR-017 C2: a .raw over 5,000,000 bytes is not committed; its SHA-256 goes to raw.sha256."""
    rows, big = [], []
    for f in sorted(out.glob("*.raw")):
        n = f.stat().st_size
        rows.append({"file": f.name, "bytes": n, "sha256": sha(f)})
        if n > 5_000_000:
            big.append(f)
    man = out / "raw.sha256"
    if big:
        man.write_text("".join(f"# {f.name} {f.stat().st_size} bytes\n{sha(f)}  {f.name}\n" for f in big))
    elif man.exists():
        man.unlink()
    return rows


# ------------------------------------------------------------------------------------------------------------
# s1: LTspice DC operating points of the coil drive
# ------------------------------------------------------------------------------------------------------------
S1_R = {  # coil resistances stepped (ohm): each coil at -10 C min, 23 C min/nom/max, 49/75/85 C at max tolerance
    "std": [50 * 0.9 * rm.k_temp(-10), 45.0, 50.0, 55.0, 55 * rm.k_temp(49), 55 * rm.k_temp(75), 55 * rm.k_temp(85),
            45 * rm.k_temp(85)],
    "h1": [166.7 * 0.9 * rm.k_temp(-10), 150.03, 166.7, 183.37, 183.37 * rm.k_temp(49), 183.37 * rm.k_temp(75),
           183.37 * rm.k_temp(85), 150.03 * rm.k_temp(85)],
}


def s1_rlist() -> list[float]:
    return sorted(round(r, 3) for r in S1_R["std"] + S1_R["h1"])


def s1_deck(out: Path) -> Path:
    rl = " ".join(f"{r:.3f}" for r in s1_rlist())
    txt = f"""* WP-PDR-23a s1: relay coil drive, DC operating points (sequencer-timing.md section 3.2)
* Two low-side drivers on the same supply V1, each with its own coil (resistance only at DC) and 1N4148
* freewheel diode: A = 2N3904 (TS-012 BOM row 12, LTspice standard.bjt model), base from a 3.3 V GPIO
* (40 ohm pad resistance, estimate) through 220 ohm; B = AO3400A (BOM row 22; VDMOS fit to the datasheet
* RDS(on), class E), gate at 3.3 V. Coil resistance stepped over both coils and their corners; driver
* temperature stepped 25 and 70 C. Revision 1 adds branch E (option E, limiter-fed coil).
.param Rc=50
V1 vs 0 5
VG g0 0 3.3
RP g0 g 40
RcA vs ca {{Rc}}
DfA ca vs 1N4148
QA ca bA 0 2N3904
RbA g bA 220
RcB vs cb {{Rc}}
DfB cb vs 1N4148
MB cb g 0 AO3400A
* revision 1, option E: coil-supply limiter (behavioural: set point {val('v_lim_set'):g} V, dropout {val('v_lim_do'):g} V),
* then the coil and an AO3400A on a static gate
BL lim 0 V=min({val('v_lim_set'):g}, V(vs)-{val('v_lim_do'):g})
RcE lim ce {{Rc}}
DfE ce lim 1N4148
ME ce g 0 AO3400A
{AO3400A_MODEL}
.dc V1 4.5 8.6 0.01
.step param Rc list {rl}
.step temp list 25 70
.save I(RcA) I(RcB) I(RcE) V(ca) V(cb) V(ce) V(lim) V(vs) Ib(QA)
.end
"""
    p = out / "drive_dc.cir"
    p.write_text(txt)
    return p


def s1():
    out = rundir("s1")
    deck = s1_deck(out)
    prov = run_ltspice(deck, out)
    raw = RawRead(str(out / "drive_dc.raw"))
    steps = raw.get_steps()
    rlist = s1_rlist()   # LTspice sorts a .step list; the deck carries it sorted already
    temps = [25.0, 70.0]
    n_exp = len(rlist) * len(temps)
    checks = {"steps": {"expected": n_exp, "found": len(steps), "pass": len(steps) == n_exp}}
    vs_tr = raw.get_trace("V(vs)")
    rows = []
    idx = 0
    # LTspice nests the steps with the first .step (Rc) varying fastest
    for ti, tc in enumerate(temps):
        for ri, rc in enumerate(rlist):
            i = ti * len(rlist) + ri
            vs = vs_tr.get_wave(i)
            ia = raw.get_trace("I(RcA)").get_wave(i)
            ib = raw.get_trace("I(RcB)").get_wave(i)
            ie = raw.get_trace("I(RcE)").get_wave(i)
            vl = raw.get_trace("V(lim)").get_wave(i)
            for v in (4.75, 4.94, 5.0, 5.09, 5.25, 5.44, 5.45, 6.21, 6.35, 7.4, 8.4):
                a = float(np.interp(v, vs, ia))
                b = float(np.interp(v, vs, ib))
                e = float(np.interp(v, vs, ie))
                rows.append({"temp_c": tc, "r_coil": rc, "coil": "std" if rc < 100 else "h1",
                             "v_supply": v, "i_q": a, "drop_q": v - a * rc, "i_m": b, "drop_m": v - b * rc,
                             "i_e": e, "v_lim": float(np.interp(v, vs, vl)), "v_coil_e": e * rc})
            idx += 1
    # checks: KCL (coil current = V/R - drop) is by construction; check drop plausibility and a closed form for
    # the MOSFET: drop = I * Ron with Ron from the fitted model within 30 %
    ron = [r["drop_m"] / r["i_m"] for r in rows if r["i_m"] > 0.02]
    checks["mos_ron_range_mohm"] = {"min": 1e3 * min(ron), "max": 1e3 * max(ron),
                                    "pass": 0.015 < min(ron) and max(ron) < 0.060}
    qd = [r["drop_q"] for r in rows if r["i_q"] > 0.05]
    checks["q_vcesat_range_v"] = {"min": min(qd), "max": max(qd), "pass": 0.02 < min(qd) and max(qd) < 0.6}

    # fits of drop(i) = a + b i per driver at 70 C (the bay), used by s3
    fits = {}
    for drv in ("q", "m"):
        pts = [(r[f"i_{drv}"], r[f"drop_{drv}"]) for r in rows if r["temp_c"] == 70.0]
        x = np.array([p[0] for p in pts])
        y = np.array([p[1] for p in pts])
        A = np.vstack([np.ones_like(x), x]).T
        coef, *_ = np.linalg.lstsq(A, y, rcond=None)
        resid = float(np.max(np.abs(A @ coef - y)))
        fits[drv] = {"a_v": float(coef[0]), "b_ohm": float(coef[1]), "max_resid_v": resid,
                     "i_range_a": [float(x.min()), float(x.max())]}
    checks["fit_resid"] = {"q": fits["q"]["max_resid_v"], "m": fits["m"]["max_resid_v"],
                           "pass": fits["q"]["max_resid_v"] < 0.05 and fits["m"]["max_resid_v"] < 0.005}
    # revision 1: branch E against the closed form min(set, Vs - dropout) - I Ron (within 10 mV)
    dev_e = [abs(r["v_coil_e"] - min(val("v_lim_set"), r["v_supply"] - val("v_lim_do")))
             for r in rows if r["coil"] == "h1"]
    lim_dev = [abs(r["v_lim"] - min(val("v_lim_set"), r["v_supply"] - val("v_lim_do"))) for r in rows]
    checks["limiter_closed_form"] = {"max_dev_v_lim": max(lim_dev), "max_coil_minus_lim_v": max(dev_e),
                                     "pass": max(lim_dev) < 0.005 and max(dev_e) < 0.02}

    # plot: coil current against supply at the hot-max coil, both coils and drivers, with the must-operate
    # current of the worst unit
    fig, axs = plt.subplots(1, 2, figsize=(9.0, 3.6))
    for ax, coil, rsel, rng in ((axs[0], "std", 55 * rm.k_temp(85), (4.5, 5.5)),
                                (axs[1], "h1", 183.37 * rm.k_temp(85), (6.0, 8.6))):
        ri = min(range(len(rlist)), key=lambda k: abs(rlist[k] - rsel))
        i = 1 * len(rlist) + ri
        vs = vs_tr.get_wave(i)
        m = (vs >= rng[0]) & (vs <= rng[1])
        ax.plot(vs[m], 1e3 * raw.get_trace("I(RcA)").get_wave(i)[m], color=C1, label="2N3904")
        ax.plot(vs[m], 1e3 * raw.get_trace("I(RcB)").get_wave(i)[m], color=C2, label="AO3400A")
        ax.plot(vs[m], 1e3 * vs[m] / rlist[ri], color=INK2, lw=1, ls=":", label="no driver drop")
        ipu = 1e3 * rm.VPU_FRAC * 5.0 / (55.0 if coil == "std" else 183.37)
        if coil == "h1":   # revision 1: the H1 slope raises the worst unit's must-operate current at 85 C
            ipu *= rm.k_mo(85.0, max(val("s_mo_h1"))) / rm.k_temp(85.0)
        ax.axhline(ipu, color=C3, lw=1.5, ls="--", label=f"must-operate current at 85 C, worst unit ({ipu:.1f} mA)"
                   + (f"; H1 slope {100 * max(val('s_mo_h1')):.2f} %/K" if coil == "h1" else "; copper law"))
        vr = (4.75, 5.25) if coil == "std" else (6.35, 8.4)
        ax.axvspan(*vr, color="#e8f0fb", zorder=0)
        ax.set_xlabel("supply at the coil (V)")
        ax.set_ylabel("coil current (mA)")
        ax.set_title(f"{rm.COILS[coil]['label'].split(' (')[0]}: coil at 85 C, +10 % unit ({rlist[ri]:.1f} ohm)")
        ax.legend(loc="upper left")
    fig.suptitle("s1: coil current at the hot corner (drivers at 70 C); shaded: supply range of the option",
                 fontsize=9, color=INK2)
    fig.tight_layout()
    fig.savefig(out / "s1-coil-current.png")
    plt.close(fig)
    plot_s1_coil_voltage(out, raw, rlist, vs_tr)

    res = {"stage": "s1", "run_id": RUNS["s1"], "ltspice": prov, "rows": rows, "fits_70c": fits, "checks": checks,
           "raw": raw_size_manifest(out)}
    write_json(out, res)
    md = ["# s1 relay coil drive, DC operating points", "",
          f"Deck `drive_dc.cir`, LTspice exit {prov['exit']}, log first line `{prov['log_first_line']}`.", "",
          "| Driver | drop(i) fit at 70 C | residual |", "|---|---|---|"]
    for d, f in fits.items():
        md.append(f"| {'2N3904' if d == 'q' else 'AO3400A'} | {f['a_v']:.4f} V + {f['b_ohm']:.3f} ohm x i | "
                  f"{f['max_resid_v'] * 1e3:.1f} mV |")
    md += ["", "Checks: " + ", ".join(f"{k} {'PASS' if v['pass'] else 'FAIL'}" for k, v in checks.items())]
    (out / "result.md").write_text("\n".join(md) + "\n")
    copy_scripts(out)
    return res


def plot_s1_coil_voltage(out: Path, raw, rlist, vs_tr):
    """Revision 1 (finding-1, K19): the voltage imposed on the H1 coil against the pack voltage for the PWM options
    (the on-phase imposes the pack less the driver drop, whatever the duty) and for option E (LTspice branch E),
    against the maximum coil voltage read from the datasheet graph at the relay ambients; panel (b) that graph."""
    fig, axs = plt.subplots(1, 2, figsize=(11.0, 5.4))
    ax = axs[0]
    rsel = 183.37 * rm.k_temp(85)
    ri = min(range(len(rlist)), key=lambda k: abs(rlist[k] - rsel))
    i = 1 * len(rlist) + ri
    vs = vs_tr.get_wave(i)
    m = (vs >= 5.0) & (vs <= 8.6)
    ib = raw.get_trace("I(RcB)").get_wave(i)
    ie = raw.get_trace("I(RcE)").get_wave(i)
    pk = 100 * (ib[m] * rlist[ri]) / 5.0
    ax.plot(vs[m], pk, color=C2, label="C, D: on-phase (peak) voltage, any duty (AO3400A)")
    duty = np.minimum(1.0, val("v_hold_h1") / np.clip(vs[m] - 0.9, 0.1, None))
    ax.plot(vs[m], pk * duty * (vs[m] - 0.9) / vs[m], color=C2, lw=1, ls="--",
            label="C, D: hold average in key-down (rev 0 duty rule)")
    ax.plot(vs[m], np.minimum(pk, 150.0), color=C4, lw=1.2, ls=":", label="C, D: pull-in average capped at 150 % (PWM)")
    ax.plot(vs[m], 100 * ie[m] * rlist[ri] / 5.0, color=C3, label="E: limiter-fed coil, nominal set point (peak = average)")
    ax.fill_between([5.0, 8.6], 100 * v_lim_out(20, "min") / 5.0, 100 * v_lim_out(20, "max") / 5.0, color=C3, alpha=0.15,
                    lw=0, label="E: set-point tolerance +/-2 %")
    for ta, ls in zip(val("t_amb_relay"), ("-.", "--", "-")):
        ax.axhline(vmax_h1_pct(ta), color=INK, lw=1, ls=ls, label=f"H1 maximum at {ta:.1f} C ambient: {vmax_h1_pct(ta):.0f} %")
    ax.axvspan(rail_rx_floor(), val("v_pack_max"), color="#e8f0fb", zorder=0)
    ax.set_xlabel("switched pack rail (V)")
    ax.set_ylabel("voltage imposed on the coil (% of rated 5 V)")
    ax.set_ylim(80, 200)
    ax.set_title(f"(a) H1 coil voltage against the pack (coil at 85 C, +10 % unit;\nshaded: receive rail {rail_rx_floor():.2f} "
                 "to 8.4 V, revision 2 floor)",
                 fontsize=9, loc="left")
    ax.legend(fontsize=6.5, loc="upper center", bbox_to_anchor=(0.5, -0.14), ncol=2)
    ax = axs[1]
    t = np.linspace(0, 80, 161)
    ax.plot(t, [vmax_h1_pct(x) if x <= 70 else np.nan for x in t], color=INK, label="H1 3 to 24 VDC maximum coil voltage (graph read)")
    for ta in val("t_amb_relay"):
        ax.axvline(ta, color=GRID, lw=1)
        ax.text(ta + 0.5, 92, f"{ta:.1f} C", fontsize=7, color=INK2, rotation=90)
    ax.axhline(100 * 8.4 / 5.0, color=C2, lw=1.5, label="C, D at 8.4 V: 168 % imposed (pull-in or any PWM on-phase)")
    ax.axhline(100 * v_lim_out(20, "max") / 5.0, color=C3, lw=1.5,
               label=f"E: at most {100 * v_lim_out(20, 'max') / 5.0:.1f} % (limiter high corner)")
    ax.set_xlim(0, 80)
    ax.set_ylim(80, 200)
    ax.set_xlabel("relay ambient temperature (C)")
    ax.set_ylabel("maximum coil voltage (% of rated)")
    ax.set_title("(b) the datasheet limit applies to the imposed voltage\n(ratings note 3)", fontsize=9, loc="left")
    ax.legend(fontsize=6.5, loc="upper center", bbox_to_anchor=(0.5, -0.14), ncol=1)
    fig.tight_layout()
    fig.savefig(out / "s1-coil-voltage-vs-pack.png")
    plt.close(fig)


# ------------------------------------------------------------------------------------------------------------
# s2: LTspice transient of the coil drive (rise, PWM hold, freewheel decay), cross-checked in closed form
# ------------------------------------------------------------------------------------------------------------
TAU_O = rm.NOMINAL.tau_o      # nominal band member (section 3.3)
RHO = rm.NOMINAL.rho


def s2_cases():
    k85 = rm.k_temp(85.0)
    kc = rm.k_temp(-10.0)
    cases = [
        # name, coil, supply, coil R, inductance, hold duty (0 = rise only), current threshold (A)
        ("A_rise_hot", "std", 4.75, 55 * k85, TAU_O * 55, 0.0, 0.75 * 5 / 55),
        ("B_hold_hot", "std", 4.75, 55 * k85, RHO * TAU_O * 55, val("hold_frac_std"), 0.75 * 5 / 55),
        ("D_rise_hot", "h1", 6.35, 183.37 * k85, TAU_O * 183.37, 0.0, 0.75 * 5 / 183.37),
        ("D_hold_hot", "h1", 6.35, 183.37 * k85, RHO * TAU_O * 183.37, min(1.0, val("v_hold_h1") / (6.35 - 0.9)),
         0.75 * 5 / 183.37),
        ("D_rise_cold", "h1", 8.40, 150.03 * kc, TAU_O * 150.03, 0.0, 0.75 * 5 / 150.03),
        ("D_hold_cold", "h1", 8.40, 150.03 * kc, RHO * TAU_O * 150.03, val("v_hold_h1") / (8.40 - 0.9),
         0.75 * 5 / 150.03),
        # revision 1, option E (static drive, no PWM; hold duty -1 marks a DC hold): rise at the lowest limiter
        # output on the hot +10 % unit; DC hold at the highest limiter output on the cold -10 % unit, then off
        ("E_rise_hot", "h1", OPTIONS["E"]["v"][0], 183.37 * k85, TAU_O * 183.37, 0.0, 0.75 * 5 / 183.37),
        ("E_dc_cold", "h1", OPTIONS["E"]["v"][2], 150.03 * kc, RHO * TAU_O * 150.03, -1.0, 0.75 * 5 / 150.03),
    ]
    return cases


def s2_deck(out: Path, cases) -> Path:
    n = len(cases)

    def tab(ix):
        return ",".join(f"{k + 1},{c[ix]:.6g}" for k, c in enumerate(cases))
    per = 1.0 / (val("f_hold") * 1e3)
    txt = f"""* WP-PDR-23a s2: relay coil transient (sequencer-timing.md section 3.2): pull-in at 100 % from 1 ms to
* 26 ms (t_pi 25 ms), hold PWM at {val('f_hold'):g} kHz from 26 ms to 66 ms, drive off at 66 ms, decay through the
* 1N4148 freewheel diode. The coil is its resistance in series with a fixed inductance (the open-gap value for
* the rise cases, the closed-gap value for the hold cases; armature motion is in s3). AO3400A low-side driver.
* Revision 1: option E cases (static gate from 1 ms to 66 ms, no PWM; the supply is the limiter output).
.param case=1
.param Vs=table(case,{tab(2)})
.param Rc=table(case,{tab(3)})
.param Lc=table(case,{tab(4)})
.param Dh=table(case,{tab(5)})
.param Toff=table(case,{",".join(f"{k + 1},{(66e-3 if c[5] < 0 else 26e-3):.6g}" for k, c in enumerate(cases))})
V1 vs 0 {{Vs}}
Rc vs n1 {{Rc}}
L1 n1 c {{Lc}} Rser=0
D1 c vs 1N4148
M1 c g1 0 AO3400A
M2 c g2 0 AO3400A
VP g1 0 PWL(0 0 1m 0 1.0001m 3.3 {{Toff}} 3.3 {{Toff+0.1u}} 0)
VH g2 0 PULSE(0 {{3.3*(Dh>0)}} 26m 50n 50n {{max(Dh*{per:.6g}-100n,10n)}} {per:.6g} {int(40e-3 / per)})
{AO3400A_MODEL}
.tran 0 90m 0 8u
.step param case 1 {n} 1
.save I(L1)
.end
"""
    p = out / "coil_tran.cir"
    p.write_text(txt)
    return p


def decay_time(lc, rc, i0, i1, diode=D1N4148, rds=0.0):
    """Closed form of the freewheel decay L di/dt = -(R i + Vd(i)), integrated numerically."""
    is_, nvt, rs = diode
    i = np.geomspace(i0, i1, 4000)
    f = lc / (rc * i + nvt * np.log1p(i / is_) + rs * i)
    return float(-np.trapezoid(f, i))   # i runs downward from i0 to i1


def s2():
    out = rundir("s2")
    cases = s2_cases()
    deck = s2_deck(out, cases)
    prov = run_ltspice(deck, out, timeout=900)
    raw = RawRead(str(out / "coil_tran.raw"))
    steps = raw.get_steps()
    checks = {"steps": {"expected": len(cases), "found": len(steps), "pass": len(steps) == len(cases)}}
    ron = 0.036
    rows = []
    for k, c in enumerate(cases):
        name, coil, vs, rc, lc, dh, ipu = c
        t = np.abs(raw.get_trace("time").get_wave(k))
        il = raw.get_trace("I(L1)").get_wave(k)
        row = {"case": name, "coil": coil, "v_supply": vs, "r_coil": rc, "l_h": lc, "hold_duty": dh, "i_pu": ipu}
        # rise: time from 1 ms to the must-operate current
        m = t >= 1e-3
        above = np.nonzero(il[m] >= ipu)[0]
        t_pu = float(t[m][above[0]] - 1e-3) if above.size else math.inf
        i_f = vs / (rc + ron)
        tau = lc / (rc + ron)
        t_pu_cf = tau * math.log(i_f / (i_f - ipu)) if i_f > ipu else math.inf
        row.update({"t_pu_ms": 1e3 * t_pu, "t_pu_cf_ms": 1e3 * t_pu_cf, "i_full_ma": 1e3 * float(np.interp(25.9e-3, t, il)),
                    "i_full_cf_ma": 1e3 * i_f * (1 - math.exp(-24.9e-3 / tau))})
        row["mode"] = "rise" if dh == 0 else ("dc" if dh < 0 else "pwm")
        if dh != 0:
            w = (t >= 60e-3) & (t <= 66e-3)
            ih = float(np.trapezoid(il[w], t[w]) / (t[w][-1] - t[w][0]))
            row.update({"i_hold_ma": 1e3 * ih, "ripple_pct": 100 * float(il[w].max() - il[w].min()) / ih})
            if dh > 0:
                # closed form of the hold average: duty on at Vs - I Ron, off at -Vd (diode at the hold current)
                vd = D1N4148[1] * math.log1p(ih / D1N4148[0]) + D1N4148[2] * ih
                ih_cf = (dh * vs - (1 - dh) * vd) / (rc + dh * ron)
            else:
                ih_cf = vs / (rc + ron)       # DC hold (option E)
            row["i_hold_cf_ma"] = 1e3 * ih_cf
            # decay: from the hold current to 5 % of rated and to half the hold current
            ioff = float(np.interp(66e-3, t, il))
            w2 = t >= 66e-3
            for lab, thr in (("t_half_ms", ioff / 2), ("t_5pct_ms", 0.05 * 5.0 / (50 if coil == "std" else 166.7))):
                below = np.nonzero(il[w2] <= thr)[0]
                row[lab] = 1e3 * float(t[w2][below[0]] - 66e-3) if below.size else math.inf
                row[lab.replace("_ms", "_cf_ms")] = 1e3 * decay_time(lc, rc, ioff, thr)
        rows.append(row)
    # checks: LTspice against the closed forms
    dev = []
    for r in rows:
        if math.isfinite(r["t_pu_cf_ms"]) and r["mode"] == "rise":
            dev.append(abs(r["t_pu_ms"] / r["t_pu_cf_ms"] - 1))
        if "i_hold_ma" in r:
            dev.append(abs(r["i_hold_ma"] / r["i_hold_cf_ma"] - 1))
            dev.append(abs(r["t_half_ms"] / r["t_half_cf_ms"] - 1))
            dev.append(abs(r["t_5pct_ms"] / r["t_5pct_cf_ms"] - 1))
    checks["closed_form"] = {"max_rel_dev": max(dev), "limit": 0.03, "pass": max(dev) <= 0.03}
    checks["ripple"] = {"max_pct": max(r.get("ripple_pct", 0) for r in rows if r["mode"] == "pwm"), "limit": 5.0,
                        "pass": max(r.get("ripple_pct", 0) for r in rows if r["mode"] == "pwm") <= 5.0}

    fig, axs = plt.subplots(1, 3, figsize=(13.0, 3.8))
    for ax, sel, col in ((axs[0], ("A_rise_hot", "B_hold_hot"), (C1, C2)),
                         (axs[1], ("D_rise_hot", "D_hold_hot", "D_hold_cold"), (C1, C2, C3)),
                         (axs[2], ("E_rise_hot", "E_dc_cold"), (C1, C7))):
        for nm, cc in zip(sel, col):
            k = [c[0] for c in cases].index(nm)
            t = np.abs(raw.get_trace("time").get_wave(k))
            il = raw.get_trace("I(L1)").get_wave(k)
            ax.plot(1e3 * t, 1e3 * il, color=cc, lw=1.5, label=nm.replace("_", " "))
            ax.axhline(1e3 * cases[k][6], color=C4, lw=1, ls="--")
        ax.set_xlabel("time (ms)")
        ax.set_ylabel("coil current (mA)")
        ax.legend(loc="upper right")
    axs[0].set_title("standard coil, 5 V bus at 4.75 V, coil 85 C (dashed: worst-unit must-operate current)")
    axs[1].set_title("H1 coil, pack rail (6.35 V hot, 8.4 V cold)")
    axs[2].set_title(f"option E: limiter output ({OPTIONS['E']['v'][0]:.2f} V hot, {OPTIONS['E']['v'][2]:.2f} V cold), "
                     "static drive")
    for ax in axs:
        ax.title.set_fontsize(8)
    fig.suptitle("s2: drive on at 1 ms; rise cases off at 26 ms; hold cases: 25 kHz PWM from 26 to 66 ms, then off; "
                 "E_dc_cold: static drive 1 to 66 ms, then off (freewheel 1N4148)", fontsize=8, color=INK2, y=0.02, va="bottom")
    fig.tight_layout(rect=(0, 0.05, 1, 1))
    fig.savefig(out / "s2-coil-transient.png")
    plt.close(fig)

    res = {"stage": "s2", "run_id": RUNS["s2"], "ltspice": prov, "cases": rows, "checks": checks,
           "raw": raw_size_manifest(out)}
    write_json(out, res)
    md = ["# s2 relay coil transient", "", f"Deck `coil_tran.cir`, LTspice exit {prov['exit']}.", "",
          "| Case | t to Ipu (ms) LTspice / closed form | hold mA LTspice / cf | ripple % | decay to 1/2 (ms) | decay to 5 % rated (ms) |",
          "|---|---|---|---|---|---|"]
    for r in rows:
        md.append(f"| {r['case']} | {r['t_pu_ms']:.3f} / {r['t_pu_cf_ms']:.3f} | "
                  f"{r.get('i_hold_ma', float('nan')):.2f} / {r.get('i_hold_cf_ma', float('nan')):.2f} | "
                  f"{r.get('ripple_pct', float('nan')):.2f} | {r.get('t_half_ms', float('nan')):.2f} | "
                  f"{r.get('t_5pct_ms', float('nan')):.2f} |")
    md += ["", "Checks: " + ", ".join(f"{k} {'PASS' if v['pass'] else 'FAIL'}" for k, v in checks.items())]
    (out / "result.md").write_text("\n".join(md) + "\n")
    copy_scripts(out)
    return res


# ------------------------------------------------------------------------------------------------------------
# s3: electromechanical relay model at the pull-in corners (relay_model.py)
# ------------------------------------------------------------------------------------------------------------
T_SWEEP = list(range(-10, 101, 5))
VSET_SWEEP = [5.8, 6.0, 6.2, 6.3, 6.4, 6.6, 7.0, 7.4]      # option E set-point trade (revision 1)
REL_TEMPS = ("cold", "ref", "hot_c")                        # release corners (revision 1: -10 C added, finding-3)


def _drop_fun(driver: str, fits: dict):
    a, b = fits[driver]["a_v"], fits[driver]["b_ohm"]
    if driver == "q":
        # 2N3904: the LTspice model is typical; the datasheet gives VCE(sat) at most 0.30 V at 50 mA, which is
        # used as a floor at every current (conservative for this purpose)
        return lambda i: max(a + b * i, QBJT_VCESAT_DS)
    return lambda i: a + b * i


def _slopes(coil: str) -> list:
    """Must-operate slopes run per coil: None = copper law (revision 0 basis); the H1 adds its graph band."""
    return [None] + list(val("s_mo_h1")) if coil == "h1" else [None]


def _design_slopes(coil: str) -> list:
    return list(val("s_mo_h1")) if coil == "h1" else [None]


def _skey(s_mo) -> str:
    return "cu" if s_mo is None else f"{s_mo:.4f}"


def _release_holds(on: str) -> dict:
    """Voltage at the coil (V) for each release and hold case of an option (revision 1, finding-3)."""
    o = OPTIONS[on]
    if o["coil"] == "std":
        return {"full": o["v"][0], "hold63": val("hold_frac_std") * o["v"][0]}
    if on in ("C", "D"):
        vr = val("v_rx_min")
        return {"kd50": val("v_hold_h1"),                                      # key-down average of the duty rule
                "rx560": val("v_hold_h1") * val("v_pack_max") / (val("v_pack_max") - 0.9),   # end of over, 8.4 V
                "rx583": val("v_hold_h1") * vr / (vr - 0.9),                                  # end of over, 6.35 V
                "full": o["v"][2]}                                             # no D-5 hold, full pack
    # revision 2 (finding-13): the key-down holds at the restated rail floors (limiter in dropout)
    return {"e_min": o["v"][0], "e_max": o["v"][2],
            "kd_hot0": v_lim_out(rail_kd_floor("hot", False), "min"),      # +45 C, feed bound, start of the over
            "kd_hot": v_lim_out(rail_kd_floor("hot"), "min"),              # the same after the discharge allowance
            "kd_lever": v_lim_out(rail_kd_floor("lever"), "min"),          # with the WP-PDR-21 C2 lever
            "kd_cold": v_lim_out(rail_kd_floor("cold"), "min")}            # -10 C, feed bound, after the discharge


def _s3_worker(args):
    coil, pkey, fits = args
    p = next(q for q in rm.band() if q.key() == pkey)
    rl = rm.calibrate(coil, p)
    out = {"coil": coil, "params": pkey, "calibrated": rl is not None}
    if rl is None:
        return out
    ok, trel0 = rm.fit_ok(rl)
    out.update({"m": rl.m, "release_no_diode_ms": 1e3 * trel0, "anchor_release_ok": ok,
                "i_pu_ma": 1e3 * rl.ipu, "i_rel_ma": 1e3 * rl.i_release()})
    if not ok:
        return out
    t_ref, _, _ = rl.operate(rm.COILS[coil]["v_rated"], rm.no_drop)
    out["t_op_ref_ms"] = 1e3 * t_ref
    corners, sweep, rel, vset = [], [], [], []
    for s_mo in _slopes(coil):
        rl.s_mo = s_mo
        sk = _skey(s_mo)
        for on, o in OPTIONS.items():
            if o["coil"] != coil:
                continue
            drop = _drop_fun(o["driver"], fits)
            for vk, v in zip(("min", "nom", "max"), o["v"]):
                for tk, tc in T_COIL.items():
                    t, tp, _ = rl.operate(v, drop, t_coil_c=tc)
                    corners.append({"slope": sk, "option": on, "v_key": vk, "v": v, "t_key": tk, "t_coil": tc,
                                    "t_op_ms": 1e3 * t, "t_pick_ms": 1e3 * tp})
            if s_mo == _design_slopes(coil)[-1]:
                for tc in T_SWEEP:
                    t, _, _ = rl.operate(o["v"][0], drop, t_coil_c=float(tc))
                    sweep.append({"slope": sk, "option": on, "t_coil": tc, "t_op_ms": 1e3 * t})
            # release from each hold at each release corner, freewheel diode (slowest form)
            for hk, vh in _release_holds(on).items():
                for tk in REL_TEMPS:
                    tc = T_COIL[tk]
                    ih = vh / (rl.r23 * rm.k_temp(tc))
                    tr, tl, _ = rl.release(ih, t_coil_c=tc, diode=D_SLOW)
                    rel.append({"slope": sk, "option": on, "hold": hk, "t_key": tk, "t_coil": tc, "v_hold": vh,
                                "i_hold_ma": 1e3 * ih, "t_release_ms": 1e3 * tr, "t_leave_ms": 1e3 * tl,
                                "hold_over_irel": ih / rl.i_release(tc),
                                "hold_over_ipu_worst": ih / rl.i_pickup(tc)})
        if coil == "h1" and s_mo is not None:
            # option E set-point trade: operate at 85 C at the lowest limiter output, release at -10 C from the
            # highest, the lowest key-down hold at 85 C against the worst unit's must-operate current
            drop = _drop_fun("m", fits)
            r85, rc = rl.r23 * rm.k_temp(85.0), rl.r23 * rm.k_temp(-10.0)
            for vs in VSET_SWEEP:
                vlo = min(vs * (1 - val("v_lim_tol")), rail_rx_floor() - val("v_lim_do"))
                vhi = vs * (1 + val("v_lim_tol"))
                vkd = min(vs * (1 - val("v_lim_tol")), rail_kd_floor("hot") - val("v_lim_do"))
                t, _, _ = rl.operate(vlo, drop, t_coil_c=85.0)
                tr, _, _ = rl.release(vhi / rc, t_coil_c=-10.0, diode=D_SLOW)
                vset.append({"slope": sk, "v_set": vs, "v_pull": vlo, "v_hold_max": vhi, "v_hold_kd": vkd,
                             "t_op_85_ms": 1e3 * t, "t_rel_m10_ms": 1e3 * tr,
                             "hold_ratio_85": (vkd / r85) / rl.i_pickup(85.0),
                             "p_coil_85_w": vhi ** 2 / (150.03 * rm.k_temp(85.0)),
                             "vmax_pct": 100 * vhi / 5.0})
    rl.s_mo = None
    out.update({"corners": corners, "sweep": sweep, "release": rel, "vset": vset})
    return out


def _nominal(acc, coil: str):
    return next(r for r in acc if r["params"] == rm.NOMINAL.key() and r["coil"] == coil)


def s3():
    out = rundir("s3")
    fits = json.loads((rundir("s1") / "result.json").read_text())["fits_70c"]
    tasks = [(coil, p.key(), fits) for coil in ("std", "h1") for p in rm.band()]
    with ProcessPoolExecutor(max_workers=max(2, (os.cpu_count() or 4) - 1)) as ex:
        res = list(ex.map(_s3_worker, tasks))
    acc = [r for r in res if r.get("anchor_release_ok")]
    checks = {
        "calibration_ref_7ms": {"max_dev_ms": max(abs(r["t_op_ref_ms"] - 7.0) for r in acc),
                                "pass": max(abs(r["t_op_ref_ms"] - 7.0) for r in acc) < 0.01},
        "accepted_sets": {"std": sum(r["coil"] == "std" for r in acc), "h1": sum(r["coil"] == "h1" for r in acc),
                          "pass": sum(r["coil"] == "std" for r in acc) >= 10 and sum(r["coil"] == "h1" for r in acc) >= 10},
        "nominal_accepted": {"pass": any(r["params"] == rm.NOMINAL.key() for r in acc)},
    }
    # the no-motion limit of the model must reproduce the s2 LTspice rise to the must-operate current
    s2r = json.loads((rundir("s2") / "result.json").read_text())["cases"]
    dev = []
    for c in s2r:
        if c["hold_duty"] != 0:
            continue
        coil = c["coil"]
        rl = rm.Relay(coil, 55.0 if coil == "std" and c["r_coil"] > 60 else (183.37 if c["r_coil"] > 200 else 150.03),
                      rm.NOMINAL)
        rl.lo = c["l_h"]
        rl.lc = rm.NOMINAL.rho * rl.lo
        rl.ipu = c["i_pu"]
        kt = c["r_coil"] / rl.r23
        tc = rm.T_REF + (kt - 1) / rm.ALPHA_CU
        _, tp, _ = rl.operate(c["v_supply"], lambda i: 0.036 * i, t_coil_c=tc, move=False)
        dev.append({"case": c["case"], "ltspice_ms": c["t_pu_ms"], "model_ms": 1e3 * tp,
                    "rel_dev": abs(1e3 * tp / c["t_pu_ms"] - 1)})
    checks["model_vs_ltspice_rise"] = {"rows": dev, "max_rel_dev": max(d["rel_dev"] for d in dev),
                                       "pass": max(d["rel_dev"] for d in dev) < 0.01}
    # revision 1: the slope law reduces to revision 0 for s_mo = None, and the H1 slope raises the 85 C
    # must-operate voltage by the graph band exactly (closed form)
    kmo = [rm.k_mo(85.0, s) for s in val("s_mo_h1")]
    checks["slope_law"] = {"k_mo_85": kmo, "force_scale_cu": rm.force_scale(85.0, None),
                           "pass": abs(rm.force_scale(85.0, None) - 1.0) < 1e-12
                           and all(abs(k - (1 + s * 62.0)) < 1e-12 for k, s in zip(kmo, val("s_mo_h1")))}

    def design(on):
        return [_skey(s) for s in _design_slopes(OPTIONS[on]["coil"])]

    # summaries per option and corner: design band (every accepted set, every design slope) and the nominal set
    # at the worst design slope; the copper law kept for the H1 options as the revision 0 comparison
    summ, summ_cu = {}, {}
    for on in OPTIONS:
        for vk in ("min", "nom", "max"):
            for tk in T_COIL:
                for tgt, sks in ((summ, design(on)), (summ_cu, ["cu"])):
                    vals = [c["t_op_ms"] for r in acc for c in r["corners"] if c["option"] == on and c["v_key"] == vk
                            and c["t_key"] == tk and c["slope"] in sks]
                    if not vals:
                        continue
                    nomv = [c["t_op_ms"] for c in _nominal(acc, OPTIONS[on]["coil"])["corners"] if c["option"] == on and c["v_key"] == vk
                            and c["t_key"] == tk and c["slope"] in sks]
                    tgt[f"{on}|{vk}|{tk}"] = {"option": on, "v_key": vk, "t_key": tk, "nominal_ms": max(nomv),
                                              "band_min_ms": min(vals), "band_max_ms": max(vals),
                                              "no_pull_in_sets": sum(1 for x in vals if not math.isfinite(x)),
                                              "n_runs": len(vals), "slopes": sks}
    rel, rel_cu = {}, {}
    for on in OPTIONS:
        for hk in _release_holds(on):
            for tk in REL_TEMPS:
                for tgt, sks in ((rel, design(on)), (rel_cu, ["cu"])):
                    vals = [x for r in acc for x in r["release"] if x["option"] == on and x["hold"] == hk
                            and x["t_key"] == tk and x["slope"] in sks]
                    if not vals:
                        continue
                    nomv = [x["t_release_ms"] for x in _nominal(acc, OPTIONS[on]["coil"])["release"] if x["option"] == on
                            and x["hold"] == hk and x["t_key"] == tk and x["slope"] in sks]
                    tgt[f"{on}|{hk}|{tk}"] = {"option": on, "hold": hk, "t_key": tk, "v_hold": vals[0]["v_hold"],
                                              "i_hold_ma": vals[0]["i_hold_ma"],
                                              "t_release_max_ms": max(v["t_release_ms"] for v in vals),
                                              "t_release_nom_ms": max(nomv),
                                              "hold_over_irel_min": min(v["hold_over_irel"] for v in vals),
                                              "hold_over_ipu_worst": min(v["hold_over_ipu_worst"] for v in vals),
                                              "hold_over_ipu_worst_max": max(v["hold_over_ipu_worst"] for v in vals),
                                              "stays_closed_all_sets": all(v["t_leave_ms"] > 0.0 and v["hold_over_irel"] > 1.0
                                                                           for v in vals), "slopes": sks}
    vset = {}
    for vs in VSET_SWEEP:
        rows = [x for r in acc if r["coil"] == "h1" for x in r["vset"] if x["v_set"] == vs]
        vset[f"{vs:.2f}"] = {"v_set": vs, "v_pull": rows[0]["v_pull"], "v_hold_max": rows[0]["v_hold_max"],
                             "v_hold_kd": rows[0]["v_hold_kd"],
                             "t_op_85_max_ms": max(x["t_op_85_ms"] for x in rows),
                             "t_rel_m10_max_ms": max(x["t_rel_m10_ms"] for x in rows),
                             "hold_ratio_85_min": min(x["hold_ratio_85"] for x in rows),
                             "p_coil_85_w": rows[0]["p_coil_85_w"], "vmax_pct": rows[0]["vmax_pct"]}
    # revision 2 (finding-13): the model's key-down hold ratio equals the closed form V / V_mo,worst(85 C) at both
    # ends of the slope band (the ratio does not depend on the model band), and the coil's own temperature in an
    # over at the lowest pack
    dv = []
    for hk in ("kd_hot0", "kd_hot", "kd_lever"):
        r = rel[f"E|{hk}|hot_c"]
        cf = [r["v_hold"] / v_mo_worst(85.0, s_) for s_ in val("s_mo_h1")]
        dv += [abs(r["hold_over_ipu_worst"] - min(cf)), abs(r["hold_over_ipu_worst_max"] - max(cf))]
    checks["hold_ratio_closed_form"] = {"max_abs_dev": max(dv), "pass": max(dv) < 1e-9}
    coil_t = coil_temp_lowpack()
    plot_s3_keydown_hold(out, rel)
    plot_s3_operate(out, acc)
    plot_s3_release(out, rel)
    plot_s3_vset(out, vset)
    result = {"stage": "s3", "run_id": RUNS["s3"], "checks": checks, "operate": summ, "operate_cu": summ_cu,
              "release": rel, "release_cu": rel_cu, "vset": vset, "coil_temp_lowpack": coil_t,
              "rail_floors_v": {"rx": rail_rx_floor(), "kd_hot0": rail_kd_floor("hot", False),
                                "kd_hot": rail_kd_floor("hot"), "kd_lever": rail_kd_floor("lever"),
                                "kd_cold": rail_kd_floor("cold")},
              "sets": [{k: v for k, v in r.items() if k not in ("corners", "sweep", "release", "vset")} for r in res],
              "t_coil_corners_c": T_COIL, "bounce_ms": BOUNCE_MS, "s_mo_h1": val("s_mo_h1")}
    write_json(out, result)
    (out / "runs.json").write_text(json.dumps(res, default=float) + "\n")
    md = ["# s3 relay operate and release (electromechanical model), revision 2", "",
          "Rail floors (revision 2, finding-13): " + ", ".join(f"{k} {v_:.3f} V" for k, v_ in result["rail_floors_v"].items())
          + f". Coil's own temperature in an over at the lowest pack: at most {coil_t['t_coil_c']:.1f} C "
          f"(upper bound; nominal unit at the key-down voltage {coil_t['t_coil_nominal_kd_c']:.1f} C).", "",
          f"Accepted parameter sets: std {checks['accepted_sets']['std']}, h1 {checks['accepted_sets']['h1']} of 27 each. "
          f"H1 must-operate slope band {', '.join(f'{100 * s:.2f}' for s in val('s_mo_h1'))} %/K (design); copper "
          "0.393 %/K kept as the revision 0 comparison.", "",
          "| Option | supply | coil corner | nominal (ms) | band (ms) | no pull-in | copper law band max (ms) |",
          "|---|---|---|---|---|---|---|"]
    for k, s_ in summ.items():
        cu = summ_cu.get(k)
        md.append(f"| {s_['option']} | {s_['v_key']} | {s_['t_key']} | {s_['nominal_ms']:.2f} | "
                  f"{s_['band_min_ms']:.2f} to {s_['band_max_ms']:.2f} | {s_['no_pull_in_sets']} of {s_['n_runs']} | "
                  f"{cu['band_max_ms']:.2f} |" if cu else "")
    md += ["", "| Release case | coil V | hold (mA) | nominal (ms) | band max (ms) | copper law max (ms) | "
           "hold / release current, min | hold / worst must-operate |", "|---|---|---|---|---|---|---|---|"]
    for k, r in rel.items():
        cu = rel_cu.get(k, {})
        md.append(f"| {k} | {r['v_hold']:.2f} | {r['i_hold_ma']:.1f} | {r['t_release_nom_ms']:.2f} | "
                  f"{r['t_release_max_ms']:.2f} | {cu.get('t_release_max_ms', float('nan')):.2f} | "
                  f"{r['hold_over_irel_min']:.2f} | {r['hold_over_ipu_worst']:.3f} to {r['hold_over_ipu_worst_max']:.3f} |")
    md += ["", "| E set point (V) | pull-in V | hold max V | key-down hold V | operate 85 C max (ms) | release -10 C max (ms) "
           "| hold ratio 85 C min | coil W at 85 C (-10 % unit) | max % |", "|---|---|---|---|---|---|---|---|---|"]
    for r in vset.values():
        md.append(f"| {r['v_set']:.2f} | {r['v_pull']:.3f} | {r['v_hold_max']:.3f} | {r['v_hold_kd']:.3f} | "
                  f"{r['t_op_85_max_ms']:.2f} | {r['t_rel_m10_max_ms']:.2f} | {r['hold_ratio_85_min']:.3f} | "
                  f"{r['p_coil_85_w']:.3f} | {r['vmax_pct']:.1f} |")
    md += ["", "Checks: " + ", ".join(f"{k} {'PASS' if v['pass'] else 'FAIL'}" for k, v in checks.items())]
    (out / "result.md").write_text("\n".join(md) + "\n")
    copy_scripts(out)
    return result


def coil_temp_lowpack() -> dict:
    """Revision 2 (finding-13): the coil's own temperature in an over at the lowest pack. Upper bound: the coil at
    its key-up voltage all the time (the rail in receive at the pack floor, no dropout, capped at the set point's
    high corner), a -10 % unit, the upper coil-to-air resistance, over the continuous bay air; solved with the coil
    resistance at its own temperature. For comparison, a nominal unit at the key-down hold voltage (the review's
    figure of about 78 C)."""
    def solve(v, r23):
        t = 85.0
        for _ in range(100):
            t = val("t_air_relay_c") + val("rth_coil") * v ** 2 / (r23 * rm.k_temp(t))
        return t
    v_up = min(val("v_lim_set") * (1 + val("v_lim_tol")), val("v_pack_floor") - val("i_rx") * val("r_feed_hot"))
    v_kd = v_lim_out(rail_kd_floor("hot"), "min")
    t_up = solve(v_up, 150.03)
    t_nom = solve(v_kd, 166.7)
    return {"v_keyup_v": v_up, "t_coil_c": t_up, "t_coil_nominal_kd_c": t_nom,
            "hold_ratio_at_t_steep": v_kd / v_mo_worst(t_up, max(val("s_mo_h1"))),
            "hold_ratio_at_nominal_kd_steep": v_kd / v_mo_worst(t_nom, max(val("s_mo_h1")))}


def plot_s3_keydown_hold(out: Path, rel):
    """Revision 2 (finding-13): option E key-down hold against the worst unit's must-operate voltage at an 85 C coil,
    (a) against the key-down switched rail for the revision 1 and revision 2 dropout requirements, with the rail
    floors marked; (b) against the pack's fall during the over, at the feed bound as read and with the lever."""
    fig, axs = plt.subplots(1, 2, figsize=(12.5, 5.4))
    ax = axs[0]
    x = np.linspace(4.6, 6.6, 401)
    s_hi, s_lo = max(val("s_mo_h1")), min(val("s_mo_h1"))
    for do, col, lab in ((0.20, C2, "revision 1 dropout 0.20 V"), (val("v_lim_do"), C3,
                                                                 f"revision 2 dropout {val('v_lim_do'):.2f} V")):
        vc = np.minimum(val("v_lim_set") * (1 - val("v_lim_tol")), x - do)
        ax.plot(x, vc / v_mo_worst(85.0, s_hi), color=col, label=f"{lab}, steep end {100 * s_hi:.2f} %/K")
        ax.plot(x, vc / v_mo_worst(85.0, s_lo), color=col, lw=1, ls="--", label=f"{lab}, shallow end {100 * s_lo:.2f} %/K")
    ax.axhline(1.0, color=INK, lw=1.2, ls="-.", label="1.0: hold guaranteed by the datasheet")
    marks = ((5.45, f"rev 1 floor\n5.45 V", INK2, "left", 1.215),
             (rail_kd_floor("hot", False), f"rev 2, feed as read,\nstart of over\n{rail_kd_floor('hot', False):.2f} V", C1,
              "left", 1.295),
             (rail_kd_floor("hot"), f"rev 2, feed as read,\nafter {val('v_discharge'):.1f} V\ndischarge\n{rail_kd_floor('hot'):.2f} V",
              C1, "right", 1.215),
             (rail_kd_floor("lever"), f"rev 2, P-FET lever,\nafter discharge\n{rail_kd_floor('lever'):.2f} V", C7, "right", 1.14))
    for xv, lab, col, ha, ty in marks:
        ax.axvline(xv, color=col, lw=1, ls=":")
        ax.text(xv + (0.015 if ha == "left" else -0.015), ty, lab, fontsize=6.3, color=col, ha=ha, va="top",
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 0.5})
        if xv != 5.45:
            yv = min(val("v_lim_set") * (1 - val("v_lim_tol")), xv - val("v_lim_do")) / v_mo_worst(85.0, s_hi)
            ax.plot([xv], [yv], "o", color=col, ms=5, zorder=5)
            ax.annotate(f"{yv:.4f}", (xv, yv), xytext=(6 if ha == "left" else -6, -12), textcoords="offset points",
                        fontsize=7, color=col, ha=ha)
    ax.set_xlim(4.6, 6.6)
    ax.set_ylim(0.9, 1.3)
    ax.set_xlabel("switched pack rail in key-down (V)")
    ax.set_ylabel("coil voltage / worst unit's must-operate voltage at 85 C")
    ax.set_title("(a) option E key-down hold against the rail (limiter set point 6.3 V -2 %)", fontsize=9, loc="left")
    ax.legend(fontsize=6.5, loc="lower right")
    ax = axs[1]
    d = np.linspace(0.0, 0.3, 61)
    for case, col, lab in (("hot", C1, "feed bound as read (0.5646 ohm, 2.140 A)"),
                           ("lever", C7, "WP-PDR-21 P-FET lever (0.3841 ohm, 2.233 A)")):
        base = rail_kd_floor(case, False)
        vc = np.minimum(val("v_lim_set") * (1 - val("v_lim_tol")), base - d - val("v_lim_do"))
        ax.plot(d, vc / v_mo_worst(85.0, s_hi), color=col, label=f"{lab}, steep end")
        ax.plot(d, vc / v_mo_worst(85.0, s_lo), color=col, lw=1, ls="--", label=f"{lab}, shallow end")
    ax.axhline(1.0, color=INK, lw=1.2, ls="-.")
    ax.axvline(val("v_discharge"), color=INK2, lw=1, ls=":")
    ax.text(val("v_discharge") + 0.003, 0.905, f"allowance {val('v_discharge'):.2f} V", fontsize=7, color=INK2,
            rotation=90, va="bottom")
    ax.set_xlim(0, 0.3)
    ax.set_ylim(0.9, 1.3)
    ax.set_xlabel("pack fall during the over below its reading at the start (V)")
    ax.set_ylabel("coil voltage / worst unit's must-operate voltage at 85 C")
    ax.set_title(f"(b) against the discharge during the over (pack {val('v_pack_floor'):.2f} V at the start, "
                 f"dropout {val('v_lim_do'):.2f} V)", fontsize=9, loc="left")
    ax.legend(fontsize=6.5, loc="upper right")
    fig.suptitle("s3 (revision 2, finding-13): option E key-down hold at the REQ-SYS-097 floor and the WP-PDR-21 "
                 "revision 3 feed bound, coil at 85 C", fontsize=9.5, color=INK)
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    fig.savefig(out / "s3-keydown-hold.png")
    plt.close(fig)


def plot_s3_operate(out: Path, acc):
    fig, axs = plt.subplots(1, 2, figsize=(12.5, 6.2))
    lim = val("L") - BOUNCE_MS
    cols = {"A": C1, "B": C2, "C": C3, "D": C7, "E": C4}
    for ax, opts, ylim in ((axs[0], list(OPTIONS), (0, 40)), (axs[1], ["C", "D", "E"], (3, 11))):
        _plot_s3_operate_panel(ax, acc, opts, ylim, cols, lim)
    axs[0].set_title("(a) all options (40 = no pull-in)", fontsize=9, loc="left")
    axs[1].set_title("(b) H1 options C, D, E, zoomed", fontsize=9, loc="left")
    h, lab = axs[0].get_legend_handles_labels()
    fig.legend(h, lab, loc="lower center", ncol=2, fontsize=7)
    fig.suptitle("s3 (revision 2): operate time of a worst-case G5V-2 unit (must-operate 75 %, operate 7 ms at the datasheet "
                 f"point) at the lowest supply of each option.\nH1 options with the must-operate slope "
                 f"{100 * max(val('s_mo_h1')):.2f} %/K, standard coil on the copper law; solid: nominal set; dashed and "
                 "band: class E band", fontsize=8.5)
    fig.tight_layout(rect=(0, 0.13, 1, 0.94))
    fig.savefig(out / "s3-operate-vs-coil-temperature.png")
    plt.close(fig)


def _plot_s3_operate_panel(ax, acc, opts, ylim, cols, lim):
    for on in opts:
        o = OPTIONS[on]
        env_lo, env_hi, nom = [], [], []
        for tc in T_SWEEP:
            vv = [s["t_op_ms"] for r in acc for s in r["sweep"] if s["option"] == on and s["t_coil"] == tc]
            nn = [s["t_op_ms"] for s in _nominal(acc, o["coil"])["sweep"] if s["option"] == on and s["t_coil"] == tc]
            env_lo.append(min(vv))
            env_hi.append(min(max(vv), 40.0))
            nom.append(min(nn[0], 40.0))
        ax.fill_between(T_SWEEP, env_lo, env_hi, color=cols[on], alpha=0.14, lw=0)
        ax.plot(T_SWEEP, nom, color=cols[on], lw=2.6 if on == "E" else 2.0, label=f"{o['label']} at {o['v'][0]:.2f} V")
        ax.plot(T_SWEEP, env_hi, color=cols[on], lw=1, ls="--")
    ax.axhline(lim, color=INK, lw=1.2, ls="-.", label=f"limit: ramp start {val('L'):.0f} ms minus bounce {BOUNCE_MS} ms")
    ax.axhline(7.0, color=INK2, lw=1, ls=":", label="datasheet operate maximum 7 ms (rated voltage, coil 23 C)")
    for tk, tc in T_COIL.items():
        ax.axvline(tc, color=GRID, lw=1)
        ax.text(tc + 0.5, ylim[0] + 0.015 * (ylim[1] - ylim[0]), tk, color=INK2, fontsize=7, rotation=90, va="bottom")
    ax.set_ylim(*ylim)
    ax.set_xlim(-10, 100)
    ax.set_xlabel("coil temperature at pull-in (C)")
    ax.set_ylabel("operate time to contact make (ms)")


def plot_s3_release(out: Path, rel):
    # A and B share the coil and the holds, as do C and D (the release does not depend on the driver in the model)
    keys = [k for k in rel if rel[k]["option"] in ("A", "D", "E") and not rel[k]["hold"].startswith("kd_")]
    grp = {"A": "A, B", "D": "C, D", "E": "E"}
    fig, ax = plt.subplots(figsize=(9.0, 0.28 * len(keys) + 1.6))
    y = np.arange(len(keys))
    cmap = {"cold": C1, "ref": C3, "hot_c": C2}
    ax.barh(y, [rel[k]["t_release_max_ms"] for k in keys], color=[cmap[rel[k]["t_key"]] for k in keys], alpha=0.35,
            height=0.6)
    ax.barh(y, [rel[k]["t_release_nom_ms"] for k in keys], color=[cmap[rel[k]["t_key"]] for k in keys], height=0.3)
    share = val("t_rel_alloc") - val("t_ord") - BOUNCE_MS
    ax.axvline(share, color=INK, ls="-.", lw=1.2)
    ax.text(share - 0.3, len(keys) - 0.6, f"{share:.0f} ms: the 30 ms share less\nordering and bounce", fontsize=7,
            color=INK2, va="center", ha="right")
    ax.axvline(val("t_rel_ds"), color=INK2, ls=":", lw=1)
    ax.set_yticks(y, [f"{grp[rel[k]['option']]} {rel[k]['hold']} {rel[k]['v_hold']:.2f} V, {T_COIL[rel[k]['t_key']]:.0f} C "
                      f"({rel[k]['i_hold_ma']:.0f} mA)" for k in keys], fontsize=7)
    ax.set_xlabel("drive off to NC contact made (ms), freewheel diode (slowest form)\nwide bar: band maximum; thin bar: "
                  "nominal set; blue -10 C, green 23 C, orange 85 C", fontsize=8)
    ax.set_title("s3 (revision 2): release time at the end of an over, every hold voltage at -10, 23 and 85 C", fontsize=9)
    ax.set_xlim(0, 32)
    fig.tight_layout()
    fig.savefig(out / "s3-release.png")
    plt.close(fig)


def plot_s3_vset(out: Path, vset):
    v = np.array([r["v_set"] for r in vset.values()])
    fig, axs = plt.subplots(2, 2, figsize=(10.0, 6.4))
    rows = list(vset.values())
    panels = (
        (axs[0, 0], [r["t_op_85_max_ms"] + BOUNCE_MS for r in rows], val("L") - 0.0, "operate + bounce at 85 C (ms)",
         "limit: ramp at 10 ms"),
        (axs[0, 1], [val("t_ord") + r["t_rel_m10_max_ms"] + BOUNCE_MS for r in rows], val("t_rel_alloc"),
         "ordering + release + bounce at -10 C (ms)", "REQ-SYS-036 share 30 ms"),
        (axs[1, 0], [r["hold_ratio_85_min"] for r in rows], 1.0, "key-down hold / worst must-operate at 85 C",
         "1.0: guaranteed by the datasheet"),
        (axs[1, 1], [r["vmax_pct"] for r in rows], vmax_h1_pct(70.0), "highest coil voltage (% of rated)",
         "H1 maximum at 70 C (151 %)"),
    )
    for ax, yv, lim, lab, limlab in panels:
        ax.plot(v, yv, color=C1, marker="o", ms=4)
        ax.axhline(lim, color=C2, ls="-.", lw=1.2, label=limlab)
        ax.axvline(val("v_lim_set"), color=C3, lw=1.2, label=f"proposed set point {val('v_lim_set'):.2f} V")
        ax.set_xlabel(f"option E limiter set point (V), +/-2 %, dropout {val('v_lim_do'):.2f} V")
        ax.set_ylabel(lab)
        ax.legend(fontsize=7)
    axs[1, 1].plot(v, [100 * r["p_coil_85_w"] / 0.225 for r in rows], color=C7, lw=1, ls="--",
                   label="coil power at 85 C, % of the 0.225 W the 85 C corner assumes")
    axs[1, 1].legend(fontsize=7)
    fig.suptitle("s3 (revision 2): option E set-point trade at the restated rail floors, worst case over the model band "
                 "and the H1 slope band",
                 fontsize=9, color=INK)
    fig.tight_layout()
    fig.savefig(out / "s3-limiter-setpoint.png")
    plt.close(fig)


# ------------------------------------------------------------------------------------------------------------
# s4: sequence model, criteria, ICD-TX-SW timing table, timing diagram
# ------------------------------------------------------------------------------------------------------------
def worst_release(rel: dict, on: str, holds) -> dict:
    """The slowest release of option `on` over the named holds and the release corners (revision 1)."""
    rows = [r for r in rel.values() if r["option"] == on and r["hold"] in holds]
    return max(rows, key=lambda r: r["t_release_max_ms"])


def pack_reading_error_to_lose_hold() -> tuple[float, float]:
    """Options C and D (SA finding-2): the smallest high error of the pack reading, over the pack range, for which the
    duty rule D = min(1, 5.0 / (V_read - 0.9)) gives a key-down coil average below the worst unit's must-operate
    voltage at an 85 C coil. Returned for the steep and the shallow end of the H1 slope band."""
    out = []
    for s_mo in sorted(val("s_mo_h1"), reverse=True):
        vmo = rm.VPU_FRAC * 5.0 * rm.k_mo(85.0, s_mo)
        es = []
        for vt in np.linspace(val("v_rx_min"), val("v_pack_max"), 206):
            vkd = vt - 0.9
            e = (val("v_hold_h1") * vkd / vmo + 0.9) / vt - 1.0     # D (V_read) * vkd = vmo at V_read = vt (1 + e)
            es.append(e)
        out.append(max(0.0, min(es)))
    return out[0], out[1]


P4_RUN = REPO / "hardware" / "sim" / "tx-pa" / "results" / "2026-09-29-r3-p4-power-a5-design"


def p4_feed_check() -> dict:
    """Revision 2 (finding-13): re-derive the key-down pack currents (INPUTS i_kd_*) from the WP-PDR-21 revision 3
    p4 .raw when it is present and matches its committed raw.sha256 (CR-017 C2). Each .raw step is one corner; its
    feed resistance is (V(p) - V(d)) / I(Vp) at 6.4 V, which identifies the feed level and temperature case. The
    largest current in each group is compared with the input within 1 mA."""
    rawp = P4_RUN / "power_a5_design.raw"
    shap = P4_RUN / "raw.sha256"
    if not rawp.exists() or not shap.exists():
        return {"pass": True, "note": "p4 .raw not present: inputs used as recorded, not re-derived"}
    want = next(ln.split()[0] for ln in shap.read_text().splitlines() if ln.strip() and not ln.startswith("#"))
    got = sha(rawp)
    if got != want:
        return {"pass": False, "note": f"p4 .raw SHA-256 {got[:12]} does not match raw.sha256 {want[:12]}"}
    raw = RawRead(str(rawp))
    n = len(raw.get_steps())
    vp = np.abs(raw.get_trace(raw.get_trace_names()[0]).get_wave(0))
    i64 = int(np.argmin(np.abs(vp - 6.4)))
    ip = np.array([abs(raw.get_trace("I(Vp)").get_wave(i)[i64]) for i in range(n)])
    vd = np.array([raw.get_trace("V(d)").get_wave(i)[i64] for i in range(n)])
    rf = (vp[i64] - vd) / ip
    rows = {}
    for key_i, key_r in (("i_kd_hot", "r_feed_hot"), ("i_kd_cold", "r_feed_cold"), ("i_kd_lever", "r_feed_lever")):
        m = np.abs(rf - val(key_r)) < 3e-4
        rows[key_i] = {"n_corners": int(m.sum()), "i_max_a": float(ip[m].max()), "drop_max_v": float((vp[i64] - vd[m]).max()),
                       "input_a": val(key_i)}
    ok = all(r["n_corners"] > 0 and abs(r["i_max_a"] - r["input_a"]) < 1e-3 for r in rows.values())
    return {"pass": ok, "sha256": got, "v_pack": float(vp[i64]), "groups": rows}


def stale_ratio_case(det: float, q: float) -> dict:
    """Revision 1 (finding-4): key-down on a ratio older than A_kd (frequency-budget.md R-FRESH-2). The ratio refresh
    of R-FRESH-1 starts when receive resumes (t_r = 0 here) and ends at t_r + t_refresh; the worst key-down is just
    after t_r. (a) late element: the changeover waits for the refresh. (b) not radiated: every keyer element that
    starts before the refresh ends is sounded but not radiated, and the changeover (t0 = the T/R write) is taken at
    the first keyer element start at or after it, so every radiated element keeps the lead-in L."""
    L, tr = val("L"), val("t_refresh")
    by_wpm = {}
    for w in (5, 15, 25, 50):
        period = 2 * 1200 / w                      # fastest element starts: continuous dits
        by_wpm[w] = math.ceil(tr / period)
    s3r = json.loads((rundir("s3") / "result.json").read_text())
    relE = worst_release(s3r["release"], "E", ("e_min", "e_max"))
    t_rel_e = val("t_ord") + relE["t_release_max_ms"] + BOUNCE_MS
    return {"late_leadin_ms": tr + L + q, "late_key_rf_ms": det + tr + L + q,
            "skip_leadin_min_ms": L - val("t_keyer_tr"), "skip_leadin_max_ms": L + q,
            "skip_spread_ms": q + val("t_keyer_tr"), "n_skipped_max": max(by_wpm.values()),
            "n_skipped_by_wpm": ", ".join(f"{n} at {w} WPM" for w, n in by_wpm.items()),
            "t_release_e_ms": t_rel_e, "skip_relay_released": t_rel_e <= tr, "t_refresh_ms": tr,
            # revision 2 (finding-14): the case is set by the ratio's age at the closure, not by the over's length.
            # The age is the time since the last completed refresh: up to age_rx_max when the over starts, plus the
            # over (first key-down to hang expiry), plus the time from the hang expiry to the closure (up to the
            # ordering and the refresh). So the case can arise after an over longer than A_kd less those.
            "window_ms": val("t_ord") + tr,
            "over_min_s": val("a_kd") - val("age_rx_max") - (val("t_ord") + tr) / 1e3,
            "hang_max_s": max(val("hang_dits")) * 1.2 / min(val("wpm")),
            "keying_min_s": val("a_kd") - val("age_rx_max") - (val("t_ord") + tr) / 1e3
            - max(val("hang_dits")) * 1.2 / min(val("wpm"))}


def keydown_schedule(interval: int = 12, t_sw: float | None = None, relock_extra: float = 0.0,
                     L: float | None = None) -> dict:
    """Event times (ms) after t0, the T/R drive write, for the first element of an over."""
    L = val("L") if L is None else L
    t_sw = val("t_sw_check") if t_sw is None else t_sw
    t_i2c = val("t_i2c")
    pll = val("t_pll_alloc") + relock_extra
    fc0 = val("t_fc0_i12") if interval == 12 else val("t_fc0_i13")
    ev = {"t0_tr_drive": 0.0, "keyer_tp": val("t_keyer_tr"), "prescaler_on": 0.0, "i2c_done": t_i2c,
          "pll_settled": pll, "fc0_start": pll + val("t_fc0_delay"), "fc0_end": pll + val("t_fc0_delay") + fc0}
    ev["check_done"] = ev["fc0_end"] + t_sw
    ev["tr_settled_cfg"] = val("t_settle")
    ev["pa_en"] = max(ev["check_done"], ev["tr_settled_cfg"])
    ev["tx_key"] = L - val("t_lead")
    ev["drive_on"] = max(ev["pa_en"], ev["tx_key"])
    ev["drive_settled"] = ev["drive_on"] + val("t_drv")
    ev["ramp_start_min"] = L
    ev["ramp_start_max"] = L + val("t_pwm_env")
    ev["hold_pwm"] = val("t_pi")
    # lock-gated FC0 start (frequency-budget.md rev 2, 3.4.1 design response 1): latest start that still sets
    # PA_EN by TX_KEY
    ev["fc0_start_latest"] = ev["tx_key"] - t_sw - fc0 - val("t_fc0_delay")
    return ev


def leadin_min(relock_extra: float, interval: int, rule: str, t_sw: float | None = None) -> float:
    """Smallest lead-in L for which the key-down ordering criteria hold (relay criterion not included)."""
    ev = keydown_schedule(interval, t_sw=t_sw, relock_extra=relock_extra, L=0.0)
    if rule == "pa_en_before_tx_key":        # TS-012 / keying-note schedule: PA_EN, then TX_KEY 2 ms before the ramp
        return max(ev["pa_en"] + val("t_lead"), val("t_settle") + val("t_lead"))
    return max(ev["pa_en"] + val("t_drv"), val("t_settle") + val("t_drv"))   # PA_EN may follow TX_KEY


def s4():
    out = rundir("s4")
    s3r = json.loads((rundir("s3") / "result.json").read_text())
    s2r = json.loads((rundir("s2") / "result.json").read_text())
    op = s3r["operate"]
    rel = s3r["release"]
    L = val("L")
    q = val("t_pwm_env")
    ev = keydown_schedule(12)
    ev13 = keydown_schedule(13)
    ramp_max_ms = max(val("ramp_set"))
    verdicts, crit = {}, []

    def v(cid, ok, text, value, limit, basis, state=None):
        st = state or ("PASS" if ok else "FAIL")
        verdicts[cid] = st
        crit.append({"id": cid, "state": st, "criterion": text, "value": value, "limit": limit, "basis": basis})

    # K1 the plan and TS-012 criterion as written
    v("K1", ev["ramp_start_min"] - ev["t0_tr_drive"] >= 10.0, "ramp start at least 10 ms after the T/R command",
      f"{ev['ramp_start_min'] - ev['t0_tr_drive']:.3f} ms (+{q:.3f} ms PWM quantisation, later only)", ">= 10 ms",
      "schedule (A)")
    v("K1a", val("t_op_ds") + val("t_bounce") <= L, "contacts made and bounce ended before the ramp, datasheet point "
      "(rated 5.0 V at the coil, coil 23 C)", f"{val('t_op_ds') + val('t_bounce'):.1f} ms", f"<= {L:.1f} ms", "D, DD")
    # K1b the physical basis at the corners, per drive option (worst-case unit, s3)
    for on in OPTIONS:
        worst = max((op[f"{on}|{vk}|{tk}"]["band_max_ms"] for vk in ("min", "nom", "max") for tk in T_COIL), default=0)
        wk = max(((vk, tk) for vk in ("min", "nom", "max") for tk in T_COIL),
                 key=lambda k: op[f"{on}|{k[0]}|{k[1]}"]["band_max_ms"])
        nom = op[f"{on}|min|nom"]
        hot = op[f"{on}|min|hot_dl"]
        margin = L - (worst + BOUNCE_MS)
        txt = (f"option {on}: contacts made and bounce ended before the ramp at every corner, worst-case unit "
               f"(model band)")
        def f_(x):
            return f"{x:.2f} ms" if math.isfinite(x) else "no pull-in"
        valtxt = (f"worst {f_(worst)} at {wk[0]} supply, {wk[1]} coil; at the lowest supply: 49 C coil "
                  f"{f_(nom['nominal_ms'])} nominal set (band to {f_(nom['band_max_ms'])}), 75 C coil "
                  f"{f_(hot['nominal_ms'])} (band to {f_(hot['band_max_ms'])})")
        v(f"K1b-{on}", math.isfinite(worst) and margin >= 0, txt, valtxt, f"operate + {BOUNCE_MS} ms <= {L:.1f} ms",
          "E model anchored to D (s3)")
    v("K2", ev["ramp_start_max"] - (ev["keyer_tp"] - val("t_keyer_tr")) <= val("t_leadin_req"),
      "lead-in at most 12 ms (REQ-SYS-161), every element", f"{L - val('t_keyer_tr'):.3f} to {L + q:.3f} ms",
      "<= 12 ms", "schedule (A); REQ-SYS-161")
    spread = (L + q) - (L - val("t_keyer_tr"))
    v("K2b", spread <= val("t_leadin_eq"), "lead-in equal over the over within 0.5 ms (TC-SYS-102)",
      f"spread {spread:.3f} ms", "<= 0.5 ms", "schedule (A)")
    det = val("t_sample") + val("t_assert")
    k2rf = det + L + q
    v("K3", k2rf <= val("t_key_rf_req"), "straight-key contact to RF rise at most 15 ms (REQ-SYS-160), key bounce 0",
      f"{k2rf:.3f} ms ({det:.1f} detection + {L:.1f} lead-in + {q:.3f})", "<= 15 ms", "R, schedule")
    bmax = val("t_key_rf_req") - k2rf
    v("K3b", True, "largest key bounce for which K3 holds (bounce aligned with samples, worst case)",
      f"{bmax:.3f} ms", "condition on the key (WP-PDR-40 bounce capture)", "R, schedule", state="CONDITION")
    v("K4", ev["tx_key"] < ev["ramp_start_min"] and ev["pa_en"] <= ev["tx_key"],
      "clamps held and integrator parked until the ramp: the D-18 clamp on VGG releases only at TX_KEY with PA_EN "
      "high; the reference is held at 0 V until the ramp start", f"VGG clamp released at {ev['drive_on']:.1f} ms, "
      f"reference released at {L:.1f} ms", "both at or before the ramp; reference exactly at it", "schedule (A); D-18")
    v("K5", ev["check_done"] <= ev["pa_en"], "frequency check complete before PA_EN (interval 12)",
      f"check done {ev['check_done']:.3f} ms, PA_EN {ev['pa_en']:.3f} ms", "check <= PA_EN", "D, A; D-17")
    v("K6", ev["pa_en"] <= ev["tx_key"], "PA_EN before TX_KEY", f"{ev['pa_en']:.3f} <= {ev['tx_key']:.3f} ms",
      "PA_EN <= TX_KEY", "schedule (A)")
    v("K7", ev["drive_settled"] <= ev["ramp_start_min"], "driver supply and bias settled before the ramp",
      f"{ev['drive_settled']:.3f} ms", f"<= {L:.1f} ms", "A (t_drv allocation); pa-permit-gate-d18.md rev 0")
    slack_relock = ev["tx_key"] - ev["check_done"]
    v("K8", slack_relock >= 0, "Si5351A relock margin beyond the 1 ms allocation (interval 12)",
      f"{slack_relock:.3f} ms (TS-012 revisit condition assumes 3 ms)", ">= 0", "schedule", state="INFO")
    need13 = ev13["check_done"] + val("t_lead")
    need13b = ev13["check_done"] + 0.25
    v("K9", need13 <= val("t_leadin_req"), "interval-13 fallback (TS-012: check at t0 + 11, ramp at t0 + 11.5) inside "
      "the 12 ms lead-in, with PA_EN before TX_KEY and the 2 ms TX_KEY lead",
      f"needs L >= {need13:.3f} ms; only with PA_EN after TX_KEY and the D-18 turn-on bound of 0.25 ms "
      f"(pa-permit-gate-d18.md rev 0) L >= {need13b:.3f} ms, i.e. {11.5 - need13b:.2f} ms margin at 11.5 ms with no "
      f"relock margin", "<= 12 ms", "schedule")
    v("K8b", True, "latest lock-gated FC0 start that still sets PA_EN by TX_KEY (interval 12)",
      f"t0 + {ev['fc0_start_latest']:.3f} ms (frequency-budget.md rev 2 RL-4 gives 2.0 ms on a 4.0 ms interval)",
      "input to WP-PDR-20a", "D, A", state="INFO")
    # key-up and end of over
    dit50 = 1200 / 50
    hmin = min(val("hang_dits")) * dit50
    ku_margin = hmin - (L + q + ramp_max_ms + val("t_tail"))
    v("K10", ku_margin >= 0, "cold switching at key-up: T/R released only after TX_KEY is low (50 WPM, 3-dit hang, "
      "8 ms fall)", f"margin {ku_margin:.2f} ms", ">= 0", "R, schedule")
    v("K11", ku_margin >= 0, "REQ-SYS-044 floor of 3 dits against the relay and envelope timing (input to WP-PDR-23b)",
      f"{hmin:.0f} ms hang against {L + q + ramp_max_ms + val('t_tail'):.2f} ms of lead-in, fall and tail", "hang >= that",
      "R, schedule")
    # revision 1 (finding-3): the release at every release corner (-10, 23, 85 C) and every hold the option applies
    # at the end of an over; the worst case sets the criterion
    for cid, on, holds, txt in (("K12-A", "A", ("full",), "options A and B (standard coil at the full 5 V bus)"),
                                ("K12-D", "D", ("kd50", "rx560", "rx583"), "options C and D (H1, duty-rule hold: 5.0 V "
                                 "key-down, 5.6 to 5.83 V at the end of an over)"),
                                ("K12-E", "E", ("e_min", "e_max"), f"option E (H1, limiter output "
                                 f"{OPTIONS['E']['v'][0]:.2f} to {OPTIONS['E']['v'][2]:.2f} V)")):
        r = worst_release(rel, on, holds)
        t_rx = val("t_ord") + r["t_release_max_ms"] + BOUNCE_MS
        v(cid, t_rx <= val("t_rel_alloc"), f"{txt}: T/R release share of REQ-SYS-036 (ordering, release with the "
          "freewheel diode, NC bounce), worst of -10, 23 and 85 C",
          f"{t_rx:.2f} ms at {T_COIL[r['t_key']]:.0f} C from {r['v_hold']:.2f} V ({r['i_hold_ma']:.0f} mA); nominal set "
          f"{val('t_ord') + r['t_release_nom_ms'] + BOUNCE_MS:.2f} ms; margin {val('t_rel_alloc') - t_rx:.2f} ms",
          f"<= {val('t_rel_alloc'):.0f} ms of 50", "E model (s3)")
    v("K13", s2r["checks"]["ripple"]["max_pct"] <= 5.0, "hold PWM ripple at 25 kHz (options C, D; E has no PWM)",
      f"{s2r['checks']['ripple']['max_pct']:.2f} %", "<= 5 %", "LTspice (s2)")
    wD = max(op[f"{o}|{vk}|{tk}"]["band_max_ms"] for o in "CD" for vk in ("min", "nom", "max") for tk in T_COIL)
    v("K14", val("t_pi") >= 2 * wD, "D-5 pull-in at 100 % lasts at least twice the worst operate time (options C, D; "
      "E has no timed pull-in)",
      f"{val('t_pi'):.0f} ms against 2 x {wD:.2f} ms", "t_pi >= 2 t_op", "A, E (s3)")
    r63 = rel["B|hold63|hot_c"]
    v("K15-B", r63["hold_over_ipu_worst"] >= 1.0, "option B: hold at 63 % of the coil voltage guaranteed by the "
      "datasheet (hold current at least the worst unit's must-operate current)",
      f"{r63['hold_over_ipu_worst']:.2f} x; model band: hold/release current down to {r63['hold_over_irel_min']:.2f}",
      ">= 1.0", "D; E model", state=None if r63["hold_over_ipu_worst"] >= 1.0 else "OPEN")
    r5 = rel["D|kd50|hot_c"]
    r5cu = s3r["release_cu"]["D|kd50|hot_c"]
    v("K15-D", r5["hold_over_ipu_worst"] >= 1.0, "options C and D: hold at 5.0 V average guaranteed by the datasheet "
      f"(coil 85 C, H1 must-operate slope band {slope_txt()})",
      f"{r5['hold_over_ipu_worst']:.3f} to {r5['hold_over_ipu_worst_max']:.3f} x (revision 0 copper law "
      f"{r5cu['hold_over_ipu_worst']:.3f} x); a pack reading high by K22-CD's figure loses it", ">= 1.0", "D, DD")
    # revision 2 (finding-13): the key-down hold at the restated rail floor: the pack at the REQ-SYS-097 floor
    # (6.30 V), the WP-PDR-21 revision 3 feed bound and its modelled key-down current, the discharge allowance, the
    # tightened dropout. The datasheet guarantee is not shown with the feed as read: OPEN, closed by the WP-PDR-21
    # C2 lever (the owner's decision there) or by bench measurement BM-1 of the fitted unit
    rE = rel["E|kd_hot|hot_c"]
    rE0, rEl, rEc = rel["E|kd_hot0|hot_c"], rel["E|kd_lever|hot_c"], rel["E|kd_cold|cold"]
    ct = s3r["coil_temp_lowpack"]
    v("K15-E", rE["hold_over_ipu_worst"] >= 1.0, "option E: hold at the lowest key-down coil voltage guaranteed by the "
      f"datasheet (coil 85 C, slope band): pack {val('v_pack_floor'):.2f} V (REQ-SYS-097 floor), feed bound "
      f"{val('r_feed_hot'):.4f} ohm at {val('i_kd_hot'):.3f} A (WP-PDR-21 r3), {val('v_discharge'):.2f} V discharge "
      f"during the over, limiter in dropout ({val('v_lim_do'):.2f} V)",
      f"{rE['hold_over_ipu_worst']:.3f} to {rE['hold_over_ipu_worst_max']:.3f} x at {rE['v_hold']:.3f} V; at the start "
      f"of the over {rE0['hold_over_ipu_worst']:.4f} to {rE0['hold_over_ipu_worst_max']:.3f} x at {rE0['v_hold']:.3f} V; "
      f"with the WP-PDR-21 P-FET lever {rEl['hold_over_ipu_worst']:.3f} to {rEl['hold_over_ipu_worst_max']:.3f} x at "
      f"{rEl['v_hold']:.3f} V; -10 C {rEc['hold_over_ipu_worst']:.2f} x at {rEc['v_hold']:.3f} V; at the coil's own "
      f"temperature (at most {ct['t_coil_c']:.1f} C) {ct['hold_ratio_at_t_steep']:.3f} x", ">= 1.0",
      "R, D, DD, A (dropout), E (discharge)", state=None if rE["hold_over_ipu_worst"] >= 1.0 else "OPEN")
    v("K16", val("t_inhibit_sw") + val("t_inhibit_hw") <= val("t_rf_off_req"), "RF off on an inhibit "
      "(REQ-SYS-004, input to WP-PDR-23b)", f"{val('t_inhibit_sw') + val('t_inhibit_hw'):.1f} ms", "<= 20 ms", "A, E")
    st = det + val("t_sidetone")
    v("K17", st <= val("t_sidetone_req"), "sidetone onset (REQ-SYS-159, input to WP-PDR-23b), key bounce 0",
      f"{st:.1f} ms; holds for bounce up to {val('t_sidetone_req') - st:.1f} ms", "<= 4 ms", "R, A")
    gap50 = dit50 - ramp_max_ms - val("t_lead") - val("t_tail")
    v("K18", gap50 >= 0, "per-element TX_KEY windows do not overlap at 50 WPM with 8 ms ramps",
      f"gap {gap50:.1f} ms", ">= 0 (else TX_KEY stays high: merge rule)", "R, schedule")
    # revision 1 (finding-1): the H1 maximum coil voltage from the datasheet graph; ratings note 3 makes it the
    # highest voltage imposed on the coil, so for a PWM drive it is the on-phase (peak) voltage
    vm = {ta: vmax_h1_pct(ta) for ta in val("t_amb_relay")}
    pk_cd = 100 * val("v_pack_max") / 5.0
    v("K19-CD", pk_cd <= min(vm.values()), "options C and D: voltage imposed on the H1 coil at the full pack against the "
      "maximum coil voltage at the relay ambient (pull-in at 100 %, and the on-phase of any PWM, capped pull-in included)",
      f"{pk_cd:.0f} % imposed; limit " + ", ".join(f"{x:.0f} % at {ta:.1f} C" for ta, x in vm.items()),
      "imposed <= limit (ratings note 3)", "D, DD (graph)")
    pk_e = 100 * OPTIONS["E"]["v"][2] / 5.0
    v("K19-E", pk_e <= min(vm.values()), "option E: highest voltage imposed on the H1 coil (limiter high corner; no PWM, "
      "so peak = average) against the maximum coil voltage at 70 C",
      f"{pk_e:.1f} % against {min(vm.values()):.0f} % (margin {min(vm.values()) - pk_e:.1f} points)", "imposed <= limit",
      "A (limiter), DD (graph)")
    # revision 1 (finding-4): the stale-ratio key-down case (frequency-budget.md R-FRESH-2)
    stl = stale_ratio_case(det, q)
    v("K20-a", stl["late_leadin_ms"] <= val("t_leadin_req"), "R-FRESH-2 outcome (a), late element: the changeover waits "
      "for the refresh; lead-in of the first element (REQ-SYS-161) and contact to RF (REQ-SYS-160)",
      f"lead-in up to {stl['late_leadin_ms']:.2f} ms against {L:.0f} ms on the other elements; contact to RF up to "
      f"{stl['late_key_rf_ms']:.2f} ms", "<= 12 ms and equal; <= 15 ms", "DD, schedule (rejected)")
    v("K20-b", stl["skip_leadin_max_ms"] <= val("t_leadin_req") and stl["skip_spread_ms"] <= val("t_leadin_eq")
      and stl["skip_relay_released"], "R-FRESH-2 outcome (b), elements not radiated (proposed): no PA_EN on the aged "
      "ratio; the changeover starts at the first keyer element start after the refresh; every radiated element keeps "
      "the lead-in (REQ-SYS-161), the relay has released before that changeover",
      f"lead-in {stl['skip_leadin_min_ms']:.3f} to {stl['skip_leadin_max_ms']:.3f} ms on every radiated element; at most "
      f"{stl['n_skipped_max']} elements not radiated ({stl['n_skipped_by_wpm']}); T/R released by "
      f"{stl['t_release_e_ms']:.2f} ms of the {val('t_refresh'):.1f} ms refresh", "<= 12 ms, equal within 0.5 ms",
      "DD, schedule")
    v("K20-c", False, "REQ-SYS-160 in the stale-ratio case (either outcome): a straight-key closure inside the refresh "
      "window gets no RF rise within 15 ms", f"closures within {stl['window_ms']:.1f} ms of the hang expiry when the "
      f"ratio is older than {val('a_kd'):.0f} s at the closure: possible after an over (first key-down to hang expiry) "
      f"longer than {stl['over_min_s']:.2f} s, always after one longer than {val('a_kd'):.0f} s; with the "
      f"{stl['hang_max_s']:.1f} s hang that is {stl['keying_min_s']:.2f} s of keying; not radiated (b) or up to "
      f"{stl['late_key_rf_ms']:.1f} ms late (a)",
      "<= 15 ms for each closure (REQ-SYS-160 as written)", "R, DD (to the owner, section 7)")
    # revision 1 (SA finding-1): the line that the K12 backstop and the PA-path gate watch
    v("K21-CD", False, "options C and D: TR_DRV is a static level for the over (HZ-004 K12, HZ-014 K8, REQ-SYS-180 and "
      "the PA-path gate's T/R input watch it)", f"{2 * val('f_hold'):.0f} k edges per second from t0 + {val('t_pi'):.0f} ms "
      "(the D-5 hold PWM on TR_DRV)", "one rise at t0, one fall at KU-06", "A")
    relE = worst_release(rel, "E", ("e_min", "e_max"))
    kue = val("t_ord") + relE["t_release_max_ms"] + BOUNCE_MS
    v("K21-E", val("t_rearm") >= kue, "option E: TR_DRV is a static level for the over; the K12 re-arm qualification "
      "(TR_DRV low for at least T_rearm) is longer than the relay release, so a TR_DRV dip that leaves the contacts in "
      "transmit cannot re-arm it", f"2 edges per over; T_rearm {val('t_rearm'):.0f} ms against the KU-07 maximum "
      f"{kue:.2f} ms", "T_rearm >= KU-07 max", "A, E model (s3)")
    # revision 1 (SA finding-2): firmware-set coil drive parameters and their integrity
    e_loss = pack_reading_error_to_lose_hold()
    v("K22-CD", False, "options C and D: no firmware-set coil drive parameter can remove the guaranteed hold or "
      "overdrive the coil (duty from a pack reading, PWM configuration, 25 ms pull-in)",
      f"a pack reading {100 * e_loss[0]:.1f} to {100 * e_loss[1]:.1f} % high loses the guaranteed hold at 85 C; a stuck "
      f"pull-in holds {pk_cd:.0f} % continuously; no integrity provision", "no single firmware value does either",
      "D, DD, A")
    # revision 2: K22-E asks whether a firmware value can remove the hold or overdrive the coil. In option E the hold
    # is set by the pack, the feed and the limiter only, whatever the firmware does; its hardware margin is K15-E
    v("K22-E", pk_e <= min(vm.values()), "option E: no firmware-set coil drive "
      "parameter; the coil voltage is bounded in hardware whatever the firmware does",
      f"firmware sets TR_DRV on or off only; imposed at most {pk_e:.1f} %; the key-down hold is set by the pack, the "
      f"feed and the limiter, with no pack reading used (its hardware margin is K15-E, {rE['hold_over_ipu_worst']:.3f} x)",
      "no single firmware value does either", "A, D, DD")

    table = timing_table(ev, ev13, op, rel)
    write_table(out, table)
    plot_timing_diagram(out, ev, op)
    plot_budgets(out, ev, ev13)
    plot_margins(out, det)
    plot_stale_ratio(out, det, stl)
    res = {"stage": "s4", "run_id": RUNS["s4"], "inputs": {k: {"value": x[0], "unit": x[1], "class": x[2], "source": x[3]}
                                                           for k, x in INPUTS.items()},
           "options": OPTIONS, "keydown_i12": ev, "keydown_i13": ev13, "criteria": crit, "verdicts": verdicts,
           "timing_table": table,
           "checks": {"schedule_monotonic": {"pass": ev["t0_tr_drive"] <= ev["pll_settled"] <= ev["fc0_end"]
                                             <= ev["check_done"] <= ev["pa_en"] <= ev["tx_key"] < ev["ramp_start_min"]},
                      "upstream_checks": {"pass": all(c["pass"] for c in s3r["checks"].values())
                                          and all(c["pass"] for c in s2r["checks"].values())},
                      "p4_feed_current": p4_feed_check()}}
    write_json(out, res)
    md = ["# s4 sequence criteria (revision 2)", "", "| Id | State | Criterion | Value | Limit | Basis |", "|---|---|---|---|---|---|"]
    for c in crit:
        md.append(f"| {c['id']} | {c['state']} | {c['criterion']} | {c['value']} | {c['limit']} | {c['basis']} |")
    md += ["", "Checks: " + ", ".join(f"{k} {'PASS' if x['pass'] else 'FAIL'}" for k, x in res["checks"].items())]
    (out / "result.md").write_text("\n".join(md) + "\n")
    copy_scripts(out)
    return res


def timing_table(ev, ev13, op, rel):
    L, q = val("L"), val("t_pwm_env")
    # revision 1: the relay rows are option E's (the recommendation)
    wD = max(op[f"E|{vk}|{tk}"]["band_max_ms"] for vk in ("min", "nom", "max") for tk in T_COIL)
    bD = min(op[f"E|{vk}|{tk}"]["band_min_ms"] for vk in ("min", "nom", "max") for tk in T_COIL)
    relD = worst_release(rel, "E", ("e_min", "e_max"))
    t_i2c = val("t_i2c")
    R = []

    def row(i, phase, ev_, sig, owner, ref, tmin, tnom, tmax, serves, basis, verif):
        R.append({"id": i, "phase": phase, "event": ev_, "signal": sig, "owner": owner, "reference": ref,
                  "t_min_ms": tmin, "t_nom_ms": tnom, "t_max_ms": tmax, "serves": serves, "basis": basis,
                  "verification": verif})
    kd = "key-down, first element of an over"
    row("KD-01", kd, "straight-key contact first make", "KEY tip at the jack", "operator", "-", 0, 0, 0,
        "REQ-SYS-160 reference", "R", "TC-SYS-102")
    row("KD-02", kd, "key-down asserted (2 closed samples); SW-TXSEQ writes the T/R drive = t0", "TR_DRV", "SW-KEYER, SW-TXSEQ",
        "KD-01", 1.0, 2.0, 3.0, "REQ-SW-KEYER-018, 020; REQ-SYS-160", "R (bounce 0; add the key's bounce)",
        "TC-SW-KEYER-018 (HostUnit); TC-SYS-102")
    row("KD-03", kd, "keyer test point edge, same TIMER0 service, after the T/R write", "KEYER_TP", "SW-KEYER",
        "t0", 0.0, 0.01, val("t_keyer_tr"), "REQ-SYS-161 reference", "A", "Emulation event order; TC-SYS-102")
    row("KD-04", kd, "T/R drive on: TR_DRV high, a static level (no PWM); coil fed from the switched pack rail through "
        "the coil-supply limiter (option E)", "TR_DRV (GPIO level)", "SW-TXSEQ", "t0", 0, 0, 0,
        "D-5; HZ-004 K12 and the PA-path gate watch TR_DRV", "A", "Bench logic capture")
    row("KD-05", kd, "prescaler supply on (transmit-only, firmware switched)", "PRESC_EN", "SW-TXSEQ", "t0", 0, 0, 0.02,
        "D-17, D-18", "A", "Emulation event order")
    row("KD-06", kd, "I2C C6 writes, MSNA first: PLL A retune, CLK1 on, CLK0 and CLK2 off, PLL B parked (400 kHz)",
        "I2C0 SDA/SCL", "SW-SYNTH", "t0", t_i2c, t_i2c, t_i2c, "TS-012 7.3 C6", "DD (frequency-budget.md RL-2)",
        "Bench logic capture")
    row("KD-07", kd, "FC0 start, lock-gated: first LOL_A = 0 read (allocation t0 + 1.0), no later than the latest start",
        "-", "SW-SYNTH", "t0", t_i2c, val("t_pll_alloc"), ev["fc0_start_latest"], "REQ-SYS-182",
        "A (WP-PDR-20a measurement M-1 confirms relock)", "WP-PDR-20a M-1; HostUnit")
    row("KD-08", kd, "FC0 interval 12 on GPIN0 (/8 prescaler) ends", "GPIN0", "SW-SAFE (frequency verification unit)",
        "t0", t_i2c + val("t_fc0_i12"), ev["fc0_end"], ev["fc0_start_latest"] + val("t_fc0_i12") + val("t_fc0_delay"),
        "REQ-SYS-182, 154", "D (4.096 ms bound)", "HostUnit injected counts; dev-board known-clock check")
    row("KD-09", kd, "lock-status read, count compared, PA-permit decision", "-", "SW-SYNTH, SW-SAFE", "t0",
        t_i2c + val("t_fc0_i12"), ev["check_done"], ev["tx_key"], "REQ-SYS-182; 07 14.2 row h", "A (2 ms)",
        "HostUnit; Emulation")
    row("KD-10", kd, "'T/R in TX and settled' prerequisite true (time-based)", "-", "SW-TXSEQ", "t0",
        val("t_settle"), val("t_settle"), val("t_settle"), "07 14.2 row h", "A (7 + 0.5 ms)", "HostUnit")
    row("KD-11", kd, "PA_EN high (safe-state manager only), at both prerequisites, never after TX_KEY", "PA_EN",
        "SW-SAFE", "t0", val("t_settle"), ev["pa_en"], ev["tx_key"], "REQ-SYS-120; D-18", "A",
        "Emulation event order; Bench logic capture")
    row("KD-12", kd, f"T/R contacts made and bounce ended (option E, worst-case unit, H1 slope band {slope_txt()})",
        "relay pole A and B", "G5V-2-H1", "t0", bD, "-", wD + BOUNCE_MS, "cold switching (07 14.2 row b)",
        "E model (s3), option E", f"Bench BM-2: operate and bounce at {OPTIONS['E']['v'][0]:.2f} V, coil at 85 C")
    row("KD-13", kd, "TX_KEY high: D-18 gate permits, VGG clamp off, GVA-84+ supply on", "TX_KEY", "SW-TXSEQ (keyer line)",
        "t0", ev["tx_key"], ev["tx_key"], ev["tx_key"], "D-18; keying-ts012.md", "A (2 ms before the ramp)",
        "Bench logic capture")
    row("KD-14", kd, "driver supply and bias settled", "GVA-84+ VCC", "hardware (D-18)", "TX_KEY", 0.0012, "-",
        val("t_drv"), "keying loop start state", "A (1 ms); pa-permit-gate-d18.md rev 0: powered within 1.2 us",
        "WP-PDR-22 LTspice; Bench")
    row("KD-15", kd, "reference clamp released, raised-cosine ramp starts (integrator parked at 0 V until here)",
        "ENV_REF (PWM)", "SW-TXSEQ (envelope shaper)", "t0", L, L, L + q, "REQ-SYS-160, 161; TS-012 7.3",
        "A (lead-in 10 ms)", "TC-SYS-102")
    row("KD-16", kd, "mid-ramp detector plausibility check", "ADC (detector)", "SW-TXSEQ, SW-SAFE", "ramp start",
        1.5, 2.5, 4.0, "REQ-SYS-156", "A (half the ramp setting)", "HostUnit; WP-PDR-22")
    row("KD-17", kd, "no pull-in or hold phase: TR_DRV stays high until KU-06 (revision 0: hold PWM at t0 + 25 ms, "
        "withdrawn)", "TR_DRV (GPIO level)", "SW-TXSEQ", "t0", "-", "-", "-", "D-5; REQ-SYS-180 (K12 sees one level)",
        "A", "Bench logic capture: TR_DRV has 2 edges per over")
    el = "each element of the over"
    row("EL-01", el, "keyer element start", "KEYER_TP", "SW-KEYER", "-", 0, 0, 0, "REQ-SYS-161 reference", "R", "TC-SYS-102")
    row("EL-02", el, "TX_KEY high", "TX_KEY", "SW-TXSEQ", "EL-01", L - val("t_lead"), L - val("t_lead"),
        L - val("t_lead"), "D-18", "A", "Bench logic capture")
    row("EL-03", el, "ramp start", "ENV_REF", "SW-TXSEQ", "EL-01", L, L, L + q, "REQ-SYS-161 (equal lead-in)", "A",
        "TC-SYS-102")
    row("EL-04", el, "keyer element end; ramp fall starts at +L", "ENV_REF", "SW-TXSEQ", "keyer element end", L, L,
        L + q, "REQ-SYS-014", "A", "TC-SYS-013")
    row("EL-05", el, "TX_KEY low after the fall", "TX_KEY", "SW-TXSEQ", "fall end", val("t_tail"), val("t_tail"),
        val("t_tail"), "REQ-TX-014; REQ-SYS-183", "A", "Bench logic capture")
    row("EL-06", el, "TX_KEY merge rule: stays high when the next rise is due before this fall", "TX_KEY", "SW-TXSEQ",
        "-", "-", "-", "-", "no TX_KEY gap shorter than 0 ms", "A", "HostUnit")
    ku = "end of the over"
    row("KU-01", ku, "last keyer key-up; hang timer starts", "KEYER_TP", "SW-KEYER", "-", 0, 0, 0, "REQ-SYS-044", "R",
        "TC-SYS-030")
    row("KU-02", ku, "last TX_KEY low", "TX_KEY", "SW-TXSEQ", "KU-01", L + 3 + val("t_tail"), L + 5 + val("t_tail"),
        L + q + 8 + val("t_tail"), "cold switching", "A", "Bench logic capture")
    row("KU-03", ku, "hang expiry t_h (3 to 30 dits at the displayed speed)", "-", "SW-KEYER", "KU-01", 72, "-", 7200,
        "REQ-SYS-044, REQ-SW-KEYER-032", "R", "TC-SYS-030")
    row("KU-04", ku, "PA_EN low (envelope idle and TX_KEY low checked first)", "PA_EN", "SW-SAFE", "t_h", 0, 0.01, 0.02,
        "07 14.2 row b", "A", "Emulation event order")
    row("KU-05", ku, "CLK1 disabled (I2C), prescaler supply off", "I2C0, PRESC_EN", "SW-SYNTH, SW-TXSEQ", "t_h", 0.02,
        0.1, 0.3, "REQ-SYS-183", "A", "Bench logic capture")
    row("KU-06", ku, "T/R drive off: TR_DRV low (freewheel through the diode)", "TR_DRV", "SW-TXSEQ", "t_h", 0.3, 0.3,
        val("t_ord"), "07 14.2 row b order", "A", "Emulation event order")
    row("KU-07", ku, "NC contacts made, bounce ended: receive path restored (option E, worst of -10, 23, 85 C)",
        "relay poles A and B", "G5V-2-H1", "t_h", "-", val("t_ord") + relD["t_release_nom_ms"] + BOUNCE_MS,
        val("t_ord") + relD["t_release_max_ms"] + BOUNCE_MS, "REQ-SYS-036 (30 ms share)", "E model (s3)",
        "Bench BM-3: pole B continuity capture, room and cold-day; TC-SYS-024")
    row("KU-08", ku, "receive sensitivity within 3 dB of MDS", "-", "receiver (WP-PDR-19)", "t_h", "-", "-",
        val("t_rx_alloc"), "REQ-SYS-036", "R", "TC-SYS-024")
    fl = "fault path"
    row("FP-01", fl, "inhibit, flag or latched fault detected; safe_state(): PA_EN low first", "PA_EN", "SW-SAFE",
        "detection", 0, "-", val("t_inhibit_sw"), "REQ-SYS-004, 130", "A", "HostUnit fault injection; Emulation")
    row("FP-02", fl, "D-18 gate clamps VGG, GVA-84+ unpowered: RF at the RF-off level", "hardware (D-18)", "hardware",
        "PA_EN low", 0, "-", val("t_inhibit_hw"), "REQ-SYS-004, 183", "E", "Bench")
    row("FP-03", fl, "T/R to receive after PA_EN low (cold)", "TR_DRV", "SW-SAFE", "PA_EN low", 0, "-", 0.05,
        "07 14.2 row c order", "A", "Emulation event order")
    row("FB-13", "fallback (not adopted)", "FC0 interval 13 at the changeover: check done", "-", "SW-SAFE", "t0",
        ev13["check_done"], ev13["check_done"], ev13["check_done"], "frequency-budget.md C-16a fallback",
        "D, A", "see criterion K9")
    # revision 1 (finding-4): the stale-ratio key-down case, outcome (b)
    st = "stale ratio at key-down (R-FRESH-2, outcome b)"
    tr = val("t_refresh")
    row("SR-01", st, "receive resumes; ratio refresh starts (R-FRESH-1) = t_r. The rows below apply when the ratio is "
        "older than A_kd (10 s) at the closure (revision 2: set by the ratio age, possible after an over longer than "
        f"{val('a_kd') - val('age_rx_max') - (val('t_ord') + tr) / 1e3:.2f} s)",
        "-", "SW-SAFE", "t_h", 0, 0.3, val("t_ord"), "frequency-budget.md R-FRESH-1", "A", "HostUnit")
    row("SR-02", st, "keyer elements that start before the refresh ends: sidetone only, no T/R write, no PA_EN",
        "KEYER_TP, sidetone", "SW-KEYER, SW-TXSEQ, SW-SAFE", "t_r", 0, "-", tr, "R-FRESH-2; REQ-SYS-120, 182; "
        "REQ-SYS-160 not met for these closures (K20-c)", "DD, A", "HostUnit: ratio age 10.1 s, key-down at t_r + 1 ms")
    row("SR-03", st, "ratio refresh complete", "-", "SW-SAFE", "t_r", tr, tr, tr, "frequency-budget.md B-19", "DD",
        "HostUnit")
    row("SR-04", st, "first keyer element start at or after SR-03: the changeover (t0) with rows KD-02 to KD-17",
        "TR_DRV", "SW-TXSEQ", "SR-03", 0, "-", 2 * 1200 / 5, "REQ-SYS-161 (every radiated element keeps L)", "A",
        "HostUnit; Emulation event order")
    return R


def write_table(out: Path, table: list[dict]):
    import csv
    cols = ["id", "phase", "event", "signal", "owner", "reference", "t_min_ms", "t_nom_ms", "t_max_ms", "serves",
            "basis", "verification"]

    def fmt(x):
        return f"{x:.3f}" if isinstance(x, float) else str(x)
    with open(out / "icd-tx-sw-timing-table.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for r in table:
            w.writerow([fmt(r[c]) for c in cols])
    md = ["# ICD-TX-SW sequencer timing table (WP-PDR-23a, run " + RUNS["s4"] + ")", "",
          "Times in ms after the reference event. '-' = not applicable.", "",
          "| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    for r in table:
        md.append("| " + " | ".join(fmt(r[c]) for c in cols) + " |")
    (out / "icd-tx-sw-timing-table.md").write_text("\n".join(md) + "\n")


def _rc(t, t0, tr):
    x = np.clip((t - t0) / tr, 0, 1)
    return 0.5 - 0.5 * np.cos(np.pi * x)


def plot_timing_diagram(out: Path, ev, op):
    L, q = val("L"), val("t_pwm_env")
    wD = max(op[f"E|{vk}|{tk}"]["band_max_ms"] for vk in ("min", "nom", "max") for tk in T_COIL)
    bD = min(op[f"E|{vk}|{tk}"]["band_min_ms"] for vk in ("min", "nom", "max") for tk in T_COIL)
    wB_nom = op["B|min|nom"]["nominal_ms"]
    fig, axs = plt.subplots(2, 1, figsize=(11.0, 12.5), gridspec_kw={"height_ratios": [1.1, 1.0]})

    def digital(ax, y, edges, t_end, label, color=C1, hatch=None, h=0.6):
        """edges: list of (t_on, t_off)"""
        xs, ys = [0.0], [y]
        for a, b in edges:
            xs += [a, a, b, b]
            ys += [y, y + h, y + h, y]
        xs.append(t_end)
        ys.append(y)
        ax.plot(xs, ys, color=color, lw=1.6, drawstyle="default")
        ax.text(-0.01, y + h / 2, label, transform=ax.get_yaxis_transform(), ha="right", va="center", fontsize=8,
                color=INK)

    # panel (a): first element, 0 to 30 ms after the key closure
    ax = axs[0]
    d = val("t_sample") + val("t_assert")    # contact to t0 (worst, no bounce)
    T = 32.0
    rows = []
    y = 0
    ramp = 5.0
    top_end = 24.0 + val("t_sample") + 5.0   # contact opened at 24 ms; 5-sample open filter (REQ-SW-KEYER-021)
    rows.append(("key contact (KD-01)", [(0, 24.0)], C1))
    rows.append(("keyer test point, t0 + 0.02 (KD-03)", [(d + 0.02, top_end)], C1))
    rows.append(("T/R drive, static level (KD-04, 17)", [(d, T)], C2))
    rows.append(("prescaler supply (KD-05)", [(d, T)], C1))
    rows.append(("I2C writes (KD-06)", [(d, d + ev["i2c_done"])], C1))
    rows.append(("FC0 interval 12 (KD-08)", [(d + ev["fc0_start"], d + ev["fc0_end"])], C3))
    rows.append(("compare, permit (KD-09)", [(d + ev["fc0_end"], d + ev["check_done"])], C3))
    rows.append(("PA_EN (KD-11)", [(d + ev["pa_en"], T)], C7))
    rows.append(("TX_KEY (KD-13)", [(d + ev["tx_key"], T)], C7))
    labels_y = []
    for lab, e, c in rows[::-1]:
        digital(ax, y, e, T, lab, color=c)
        labels_y.append(y)
        y += 1
    # relay contact band
    ax.add_patch(Rectangle((d + bD, y + 0.05), wD + BOUNCE_MS - bD, 0.5, color=C4, alpha=0.35, lw=0))
    ax.plot([d + wD + BOUNCE_MS] * 2, [y, y + 0.6], color=C4, lw=1.5)
    ax.plot([d + wB_nom + BOUNCE_MS] * 2, [y, y + 0.6], color=C2, lw=1.5, ls="--")

    ax.text(-0.01, y + 0.3, "T/R contacts made + bounce (KD-12; E band)", transform=ax.get_yaxis_transform(),
            ha="right", va="center", fontsize=8)
    y += 1
    # envelope and RF
    t = np.linspace(0, T, 3000)
    env = _rc(t, d + L, ramp) - _rc(t, top_end + L, ramp)
    ax.plot(t, y + 0.7 * env, color=C2, lw=1.8)
    ax.text(-0.01, y + 0.35, "envelope reference = RF (KD-15)", transform=ax.get_yaxis_transform(), ha="right",
            va="center", fontsize=8)
    y += 1
    for tx, lab in ((d, f"t0 = {d:.0f} ms"), (d + ev["check_done"], f"check done t0+{ev['check_done']:.2f}"),
                    (d + ev["pa_en"], f"PA_EN t0+{ev['pa_en']:.1f}"), (d + ev["tx_key"], f"TX_KEY t0+{ev['tx_key']:.0f}"),
                    (d + L, f"ramp t0+{L:.0f} = {d + L:.0f} ms after contact")):
        ax.axvline(tx, color=GRID, lw=1, zorder=0)
    ann = [(d, "t0"), (d + ev["check_done"], f"+{ev['check_done']:.2f}"), (d + ev["pa_en"], f"+{ev['pa_en']:.1f}"),
           (d + ev["tx_key"], f"+{ev['tx_key']:.0f}"), (d + L, f"+{L:.0f}")]
    ax.text(d, y + 0.1, "t0", fontsize=7, color=INK2, ha="center")
    ax.text(d + L, y + 0.1, "t0 + 10", fontsize=7, color=INK2, ha="center")
    ax.text(0.99, 0.985, "\n".join(f"{lab}" for lab in (
        f"t0 = T/R command, {d:.0f} ms after the contact",
        f"frequency check done  t0 + {ev['check_done']:.2f} ms", f"PA_EN                  t0 + {ev['pa_en']:.2f} ms",
        f"TX_KEY                 t0 + {ev['tx_key']:.2f} ms", f"ramp start             t0 + {L:.2f} ms",
        f"relay made (E, worst)  t0 + {wD + BOUNCE_MS:.2f} ms",
        "dash-dot at 15 ms: REQ-SYS-160 (15 ms after the contact)",
        "  and REQ-SYS-161 (t0 + 12 ms) coincide at the 3 ms",
        "  detection worst case",
        "orange tick: option B (standard coil, 5 V bus at",
        f"  4.75 V, coil 49 C, worst unit) makes at t0 + {wB_nom + BOUNCE_MS:.2f}")),
        transform=ax.transAxes, ha="right", va="top", multialignment="left",
        fontsize=7, family="monospace", color=INK, bbox=dict(facecolor="white", edgecolor=GRID))
    ax.axvline(d + L + 0, color=INK, lw=0.8, ls=":")
    ax.axvline(val("t_key_rf_req"), color=C3, lw=1.2, ls="-.")

    ax.set_xlim(0, T)
    ax.set_ylim(-0.4, y + 2.6)
    ax.set_yticks([])
    ax.set_xlabel("ms after the straight-key contact closure (detection at its 3 ms worst case, no key bounce)")
    ax.set_title("(a) Key-down, first element of an over (A5, relay drive option E, ramp 5 ms): times after t0 = T/R "
                 "command", fontsize=9, loc="left")
    ax.grid(False)

    # panel (b): a short over at 50 WPM, letter A (dit dah), 3-dit hang, end of over
    ax = axs[1]
    dit = 24.0
    elems = [(0.0, dit), (2 * dit, 5 * dit)]
    t_u = elems[-1][1]
    hang = 3 * dit
    th = t_u + hang
    Tb = th + 75.0
    ramp = 5.0
    y = 0
    relD = worst_release(json.loads((rundir("s3") / "result.json").read_text())["release"], "E", ("e_min", "e_max"))
    t_nc = th + val("t_ord") + relD["t_release_nom_ms"]
    t_ncmax = th + val("t_ord") + relD["t_release_max_ms"] + BOUNCE_MS
    txk = []
    for a, b in elems:
        txk.append((a + L - val("t_lead"), b + L + ramp + val("t_tail")))
    rows = [("keyer test point (EL-01)", elems, C1),
            ("T/R drive, static level (KD-04, 17; KU-06)", [(0, th + val("t_ord"))], C2),
            ("CLK1 on, prescaler supply (KD-05, 06; KU-05)", [(0, th + 0.1)], C1),
            ("PA_EN (KD-11; KU-04)", [(ev["pa_en"], th)], C7),
            ("TX_KEY per element (EL-02, 05)", txk, C7)]
    for lab, e, c in rows[::-1]:
        digital(ax, y, e, Tb, lab, color=c)
        y += 1
    ax.add_patch(Rectangle((th + val("t_ord"), y + 0.05), t_ncmax - th - val("t_ord"), 0.5, color=C4, alpha=0.35, lw=0))
    ax.add_patch(Rectangle((bD, y + 0.05), wD + BOUNCE_MS - bD, 0.5, color=C4, alpha=0.35, lw=0))
    ax.plot([wD + BOUNCE_MS, wD + BOUNCE_MS], [y, y + 0.6], color=C4, lw=1.5)
    ax.text(-0.01, y + 0.3, "T/R operate and release (KD-12, KU-07; E band)", transform=ax.get_yaxis_transform(),
            ha="right", va="center", fontsize=8)
    ax.axvline(th + val("t_rx_alloc"), color=C3, lw=1.2, ls="-.")
    ax.text(th + val("t_rx_alloc") + 0.5, y + 0.3, "REQ-SYS-036\nt_h + 50 ms", fontsize=7, color=INK2, va="center")
    y += 1
    t = np.linspace(0, Tb, 6000)
    env = sum(_rc(t, a + L, ramp) - _rc(t, b + L, ramp) for a, b in elems)
    ax.plot(t, y + 0.7 * env, color=C2, lw=1.8)
    ax.text(-0.01, y + 0.35, "envelope reference = RF (EL-03, 04)", transform=ax.get_yaxis_transform(), ha="right",
            va="center", fontsize=8)
    y += 1
    for k, (tx, lab) in enumerate(((t_u, "last key-up"), (t_u + L + ramp + val("t_tail"), "last TX_KEY low"),
                                   (th, "t_h: hang expiry"))):
        ax.axvline(tx, color=GRID, lw=1, zorder=0)
        ax.text(tx, y + 0.05 + 0.3 * (k % 2), lab, fontsize=7, color=INK2, ha="center")
    ax.annotate("", xy=(th, y - 0.2), xytext=(t_u, y - 0.2), arrowprops=dict(arrowstyle="<->", color=INK2, lw=1))
    ax.text((t_u + th) / 2, y - 0.1, "hang 3 dits = 72 ms", fontsize=7, color=INK2, ha="center")
    ax.set_xlim(-2, Tb)
    ax.set_ylim(-0.4, y + 0.6)
    ax.set_yticks([])
    ax.set_xlabel("ms after the first keyer edge")
    ax.set_title("(b) A short over at 50 WPM (letter A), 3-dit hang, end of the over; lead-in 10 ms on every "
                 "element", fontsize=9, loc="left")
    ax.grid(False)
    fig.subplots_adjust(left=0.30, right=0.98, top=0.95, bottom=0.05, hspace=0.25)
    fig.suptitle("cwht A5 T/R and keying sequence (WP-PDR-23a, sequencer-timing.md revision 2; ICD-TX-SW timing table)",
                 fontsize=10, color=INK)
    fig.savefig(out / "timing-diagram.png")
    FIG.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIG)
    plt.close(fig)


def plot_budgets(out: Path, ev, ev13):
    fig, axs = plt.subplots(1, 2, figsize=(11.0, 4.0))
    ax = axs[0]
    det = val("t_sample") + val("t_assert")
    seen = set()
    for yy, e in ((1, ev), (0, ev13)):
        kx = det + max(e["check_done"], e["tx_key"])
        segs = [("key detection (1 ms sampling + 2 ms filter)", 0, det, C1),
                ("I2C writes + PLL relock allocation (1 ms)", det, det + e["pll_settled"], C4),
                ("FC0 count", det + e["fc0_start"], det + e["fc0_end"], C3),
                ("lock read, compare, PA_EN (2 ms)", det + e["fc0_end"], det + e["check_done"], C7),
                ("slack (relock margin)", det + e["check_done"], kx, GRID),
                (f"TX_KEY lead {val('t_lead'):.0f} ms (driver on, then ramp)", kx, kx + val("t_lead"), C2)]
        for nm, a_, b_, c in segs:
            if b_ - a_ <= 1e-6:
                continue
            ax.barh(yy, b_ - a_, left=a_, color=c, height=0.5, edgecolor="white", lw=1,
                    label=None if nm in seen else nm)
            seen.add(nm)
        end = kx + val("t_lead")
        ax.text(end + 0.2, yy, f"ramp at {end:.2f} ms", va="center", fontsize=7, color=INK)
    ax.axvline(det + val("t_leadin_req"), color=C3, ls="-.", lw=1.2)
    ax.text(det + val("t_leadin_req") + 0.1, 1.45, "REQ-SYS-161 (t0 + 12)\nREQ-SYS-160 (15)", fontsize=7, color=INK2)
    ax.set_yticks([0, 1], ["interval 13\n(fallback)", "interval 12\n(proposed)"])
    ax.set_xlim(0, 19)
    ax.set_ylim(-0.5, 2.9)
    ax.legend(loc="upper left", fontsize=7, ncol=2)
    ax.set_xlabel("ms after the straight-key contact closure (TX_KEY after PA_EN, 2 ms before the ramp)")
    ax.set_title("(a) key-down budget, schedule as proposed", fontsize=9, loc="left")
    ax = axs[1]
    rx = np.linspace(0, 5, 101)
    for interval, ls in ((12, "-"), (13, "--")):
        for rule, col, nm in (("pa_en_before_tx_key", C1, "PA_EN before TX_KEY, 2 ms lead"),
                              ("drive_settle_only", C2, "PA_EN may follow TX_KEY, 1 ms drive settle")):
            ax.plot(rx, [leadin_min(r, interval, rule) for r in rx], color=col, ls=ls,
                    label=f"interval {interval}: {nm}")
    ax.axhline(val("t_leadin_req"), color=C3, ls="-.", lw=1.2, label="REQ-SYS-161 12 ms")
    ax.axhline(val("L"), color=INK2, ls=":", lw=1.2, label="proposed lead-in 10 ms")
    ax.set_xlabel("PLL relock beyond the 1 ms allocation (ms)")
    ax.set_ylabel("smallest lead-in the ordering allows (ms)")
    ax.set_title("(b) lead-in against the Si5351A relock time (WP-PDR-20a)", fontsize=9, loc="left")
    ax.legend(loc="upper left", fontsize=7)
    fig.tight_layout()
    fig.savefig(out / "s4-keydown-budget.png")
    plt.close(fig)


def plot_margins(out: Path, det):
    fig, axs = plt.subplots(1, 2, figsize=(11.0, 3.8))
    ax = axs[0]
    b = np.linspace(0, 6, 121)
    ax.plot(b, b + det + val("L") + val("t_pwm_env"), color=C1, label="contact to ramp start (REQ-SYS-160)")
    ax.plot(b, b + det + val("t_sidetone"), color=C2, label="contact to sidetone (REQ-SYS-159)")
    ax.axhline(val("t_key_rf_req"), color=C1, ls="-.", lw=1.2, label="15 ms")
    ax.axhline(val("t_sidetone_req"), color=C2, ls="-.", lw=1.2, label="4 ms")
    ax.set_xlabel("straight-key bounce after first make, sample-aligned worst case (ms)")
    ax.set_ylabel("latency (ms)")
    ax.set_title("(a) key bounce against the latency limits", fontsize=9, loc="left")
    ax.legend(fontsize=7, loc="center right")
    ax = axs[1]
    w = np.linspace(5, 50, 91)
    for tf, c in ((3.0, C3), (5.0, C1), (8.0, C2)):
        m = 3 * 1200 / w - (val("L") + val("t_pwm_env") + tf + val("t_tail"))
        ax.plot(w, m, color=c, label=f"fall {tf:.0f} ms")
    ax.axhline(0, color=INK, lw=1)
    ax.set_xlabel("speed (WPM), hang 3 dits (the REQ-SYS-044 floor)")
    ax.set_ylabel("T/R release after the last TX_KEY low (ms)")
    ax.set_title("(b) cold-switching margin at key-up", fontsize=9, loc="left")
    ax.set_yscale("log")
    ax.set_ylim(10, 1000)
    ax.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(out / "s4-margins.png")
    plt.close(fig)


def plot_stale_ratio(out: Path, det: float, stl: dict):
    """Revision 1 (finding-4): the R-FRESH-2 case. (a) outcome (b) at 50 WPM, continuous dits keyed 1 ms after
    receive resumes on a ratio older than A_kd; (b) outcome (a)'s lead-in against the key-down time in the window and
    the number of elements outcome (b) does not radiate."""
    L, q, tr = val("L"), val("t_pwm_env"), val("t_refresh")
    fig, axs = plt.subplots(1, 2, figsize=(13.0, 5.0), gridspec_kw={"width_ratios": [1.6, 1.0]})
    ax = axs[0]
    dit, ramp = 24.0, 5.0
    starts = [1.0 + k * 2 * dit for k in range(5)]
    T = starts[-1] + dit + L + ramp + 10
    first = next(a for a in starts if a >= tr)
    y = 0

    def digital(yy, edges, color, label, hatch=None):
        xs, ys = [0.0], [yy]
        for a, b in edges:
            xs += [a, a, b, b]
            ys += [yy, yy + 0.6, yy + 0.6, yy]
        xs.append(T)
        ys.append(yy)
        ax.plot(xs, ys, color=color, lw=1.6)
        ax.text(-0.01, yy + 0.3, label, transform=ax.get_yaxis_transform(), ha="right", va="center", fontsize=8)
    rad = [a for a in starts if a >= first]
    t = np.linspace(0, T, 4000)
    env = sum(_rc(t, a + L, ramp) - _rc(t, a + dit + L, ramp) for a in rad)
    ax.plot(t, y + 0.7 * env, color=C2, lw=1.8)
    ax.text(-0.01, y + 0.35, "RF (envelope)", transform=ax.get_yaxis_transform(), ha="right", va="center", fontsize=8)
    y += 1
    digital(y, [(a + L - val("t_lead"), a + dit + L + ramp + val("t_tail")) for a in rad], C7, "TX_KEY")
    y += 1
    digital(y, [(first + 7.5, T)], C7, "PA_EN (fresh ratio only)")
    y += 1
    digital(y, [(first, T)], C2, "T/R drive (t0 = first element\nafter the refresh)")
    y += 1
    digital(y, [(a, a + dit) for a in starts], C1, "keyer and sidetone (every element)")
    for a in starts:
        if a < first:
            ax.add_patch(Rectangle((a, y - 0.05), dit, 0.7, color=C4, alpha=0.35, lw=0))
    y += 1
    ax.add_patch(Rectangle((0, y + 0.05), tr, 0.5, color=C3, alpha=0.4, lw=0))
    ax.text(-0.01, y + 0.3, "ratio refresh (R-FRESH-1)", transform=ax.get_yaxis_transform(), ha="right", va="center",
            fontsize=8)
    ax.text(tr / 2, y + 0.3, f"{tr:.1f} ms", ha="center", va="center", fontsize=7)
    ax.axvline(tr, color=GRID, lw=1, zorder=0)
    ax.axvline(first + L, color=INK, lw=0.8, ls=":")
    ax.text(first + L + 1, y + 0.9, f"ramp = t0 + {L:.0f} ms", fontsize=7, color=INK2)
    for a in starts:
        if a < first:
            ax.text(a + dit / 2, 4.75, "not\nradiated", fontsize=6.5, color=INK, ha="center", va="bottom")
    ax.set_xlim(0, T)
    ax.set_ylim(-0.4, y + 1.3)
    ax.set_yticks([])
    ax.grid(False)
    ax.set_xlabel(f"ms after receive resumes (hang expiry), ratio older than A_kd = 10 s at the key-down "
                  f"(after an over longer than {stl['over_min_s']:.2f} s)")
    ax.set_title("(a) outcome (b), proposed: 50 WPM dits keyed 1 ms after receive resumes;\nshaded elements sound "
                 "(sidetone) but are not radiated", fontsize=8.5, loc="left")
    ax = axs[1]
    tk = np.linspace(0, tr, 200)
    ax.plot(tk, tr - tk + L + q, color=C2, label="outcome (a): lead-in of the late first element")
    ax.plot(tk, det + tr - tk + L + q, color=C2, ls="--", lw=1.2, label="outcome (a): contact to RF")
    ax.axhline(val("t_leadin_req"), color=C3, ls="-.", lw=1.2, label="REQ-SYS-161 12 ms")
    ax.axhline(val("t_key_rf_req"), color=C1, ls="-.", lw=1.2, label="REQ-SYS-160 15 ms")
    ax.axhline(L + q, color=C7, lw=1.5, label=f"outcome (b): every radiated element {L + q:.2f} ms")
    ax.set_xlabel("key-down time after receive resumes (ms)")
    ax.set_ylabel("lead-in or latency (ms)")
    ax.set_ylim(0, 100)
    ax.set_title(f"(b) outcome (a) against the limits; outcome (b) drops at most\n{stl['n_skipped_max']} elements "
                 f"({stl['n_skipped_by_wpm']})", fontsize=8, loc="left")
    ax.legend(fontsize=7, loc="upper right")
    fig.subplots_adjust(left=0.17, right=0.98, bottom=0.12, top=0.84, wspace=0.22)
    fig.suptitle("s4 (revision 2): key-down on a ratio older than A_kd = 10 s at the closure (frequency-budget.md "
                 "R-FRESH-2)",
                 fontsize=9.5, color=INK)
    fig.savefig(out / "s4-stale-ratio.png")
    plt.close(fig)


# ------------------------------------------------------------------------------------------------------------
def collect_checks() -> dict:
    ch = {}
    for k in ("s1", "s2", "s3", "s4"):
        p = rundir(k) / "result.json"
        if p.exists():
            for n, c in json.loads(p.read_text())["checks"].items():
                ch[f"{k}.{n}"] = bool(c["pass"])
    return ch


def main(argv):
    stages = {"s1": s1, "s2": s2, "s3": s3, "s4": s4}
    args = [a for a in argv if not a.startswith("--")]
    expect = "--expect" in argv
    if not args or args[0] not in list(stages) + ["all"]:
        print(__doc__)
        return 2
    for k in (list(stages) if args[0] == "all" else [args[0]]):
        print(f"== {k} ({RUNS[k]})", flush=True)
        stages[k]()
    checks = collect_checks()
    bad = [k for k, ok in checks.items() if not ok]
    for k, ok in checks.items():
        print(f"check {k}: {'PASS' if ok else 'FAIL'}")
    p4 = rundir("s4") / "result.json"
    verdicts = json.loads(p4.read_text())["verdicts"] if p4.exists() else {}
    for k, s_ in verdicts.items():
        print(f"verdict {k}: {s_}")
    if bad:
        return 2
    if expect:
        exp = json.loads(EXPECTED.read_text())
        diff = {k: (exp.get(k), verdicts.get(k)) for k in set(exp) | set(verdicts) if exp.get(k) != verdicts.get(k)}
        for k, (a, b) in diff.items():
            print(f"expected {k}: {a}, found {b}")
        return 3 if diff else 0
    return 0 if all(s_ in ("PASS", "INFO", "CONDITION") for s_ in verdicts.values()) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
