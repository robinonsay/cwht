#!/usr/bin/env python3
"""TS-012 WP-PDR-21 pre-order item: PA drive window and output power at the SMA, both finalists.

A4: Si5351A CLK1 -> 3-pole drive LPF -> 12 dB pad -> GVA-84+ (near its P1dB) -> AFT05MS004N (NXP 136-174 MHz
    reference circuit, 50 ohm input) -> output LPF and G5V-2 relay -> SMA.
A5: Si5351A CLK1 -> 3-pole drive LPF -> 18 dB pad -> GVA-84+ -> 3 dB pad -> RA07M1317M module -> output LPF
    and G5V-2 relay -> SMA.

Usage (repo root, repo venv):
    .venv/bin/python hardware/sim/tx-pa/run_pa.py all      # every revision 1 run below (d2 to s1), in order
    .venv/bin/python hardware/sim/tx-pa/run_pa.py d1|d2|d3|d4|p1|p2|p3|s1

Runs (each writes hardware/sim/tx-pa/results/<run-id>/: the deck, the LTspice .log and .raw, result.json and
result.md with the numbers and pass/fail, PNG plots with the limits overlaid, and a copy of this script):
    d1  GVA-84+ behavioural model check (sine power sweep; fitted P1dB and P3dB against the datasheet).
        Unchanged since revision 0 and not part of "all" (its folder keeps the revision 0 script copy).
    d2  A5 drive chain, 810 corners: 270 part corners x 3 coax lengths (transient; fundamental and 3f by DFT)
    d3  A4 drive chain, 810 corners
    d4  coax-length bound: the extreme drive corners of both finalists swept over half a wavelength of coax
    p1  A5 output power at the SMA versus pack voltage (DC sweep with behavioural module, drain feed and bus
        load), 648 part corners x 7 temperature cases
    p2  A4 output power at the SMA versus pack voltage, 1458 part corners x 7 temperature cases
    p3  A5 output power with the drive range a select-on-test pad leaves (the closure path)
    s1  summary plots, the select-on-test overdrive margin, the closure margin with its uncertainty, verdicts

Revision 1 (2026-09-28, review of the analysis note, Major findings 1 and 2, Minor finding 3):
    - the CLK1-to-drive-LPF interface is modelled as designed (TS-012 section 8.1: Si5351 on the main board,
      drive LPF on the RF board in the PA bay, joined by a 50 ohm coax through the bulkhead); only the prescaler
      tap and the pin stub load the CLK1 pin; the pin load is reported against Si5351 Table 7 (CL at most 15 pF);
    - temperature cases for REQ-SYS-114 (-10 to +45 C ambient): drain feed per part, PA case temperature
      factor, output-loss copper term (all estimates, labelled);
    - every nominal, lowest and highest corner and every lever figure is written with its full parameter set.

Revision 2 (2026-09-28, iteration 2 of the review, INSP-114: Major finding-9, Minor findings 3 to 8 and 10):
    - one thermal state per question (finding-9): every low-bound temperature case is steady key-down at its
      ambient, with the PA case temperature solved in the deck from the module dissipation and the WP-PDR-28
      case-to-ambient resistance, and the drain-feed parts and the output-loss copper term at their own key-down
      temperatures; the high-side open-loop case is the start of a key-down from a -10 C soak. A 25 C
      start-of-key-down case (the datasheet condition, PA case 25 C) is kept as an informative row;
    - VGG at the revision-4 clamp (3.08 / 3.27 / 3.46 V: minimum, nominal, maximum) and at the C3 lever value
      3.30 V (finding-3); no figure uses 3.5 V any more;
    - output loss from the WP-PDR-21 LPF revision 2 recommended build (run r13, commit 92e3805): 0.5 dB (TS-012
      allocation, low corner), 0.84 dB (r13 Monte Carlo median plus the relay), 1.86 dB (r13 worst case plus the
      relay), replacing the 0.4 to 0.6 dB allocation and the uncertainty term based on the withdrawn runs r6 and r7
      (cross item X-5);
    - select-on-test pad set built from real E24 pads with a largest gap of at most 0.8 dB, the step term taken
      from the set's own largest gap, and the reading term as an allocation with its sensitivity (finding-4);
    - exit status 0 / 1 / 2 (all criteria met / a criterion fails / a check fails) and --expect, which compares
      every verdict with the list in the analysis record (finding-5);
    - result wording and plot titles (finding-7), the A4 temperature plot range (finding-10).

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
    "d1": f"{DATE}-d1-gva-model",          # revision 0 run, still valid (model check only)
    "d2": f"{DATE}-r1-d2-drive-a5",
    "d3": f"{DATE}-r1-d3-drive-a4",
    "d4": f"{DATE}-r1-d4-coax-bound",
    "d5": f"{DATE}-r1-d5-drive-a5-pinpad",   # design-request option: 6 dB pad at the CLK1 end of the coax
    # revision 2: the drive decks are unchanged, so d2 to d5 keep their revision 1 run folders (their outputs are
    # re-read from the same .raw by the revision 2 checker); the power and summary runs are new.
    "p1": f"{DATE}-r2-p1-power-a5",
    "p2": f"{DATE}-r2-p2-power-a4",
    "p3": f"{DATE}-r2-p3-power-a5-sot",
    "s1": f"{DATE}-r2-s1-summary",
}
REVISION = 2
# Verdicts of every run (criteria and checks), filled by the runs and read by main() for the exit status.
VERDICTS: dict[str, dict[str, dict]] = {}


def verdict(run: str, name: str, ok: bool, kind: str = "criterion", detail: str = ""):
    """Record one verdict. kind "criterion": a pass criterion of the analysis (a FAIL is a valid result that the
    record reports); kind "check": a numerical or model check (a FAIL means the results must not be used)."""
    VERDICTS.setdefault(run, {})[name] = {"pass": bool(ok), "kind": kind, "detail": detail}
    return bool(ok)

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
# Revision 2 (finding-8): TS-012 section 7.3 names "the GVA-84+ S-parameters"; this model is a flat 50 ohm block with
# the 0.1 GHz gain limits instead (Rev. F input and output return loss at 0.1 GHz 22.9 and 23.3 dB, so the flat 50 ohm
# ports are a small departure). Rev. F gives typical gain only at 0.1 GHz (24.1 dB) and 1.0 GHz (21.7 dB); at 146 MHz
# the typical gain is 0.1 dB (linear in frequency) to 0.4 dB (linear in log frequency) below the 0.1 GHz value (est.).
# Direction: the 0.1 GHz limits overstate the drive by up to 0.4 dB, conservative for overdrive and optimistic for
# underdrive; the select-on-test pad measures it out; in the closure figure it is the GVA_146_UNC term below.
GAINS = [22.5, 22.9, 24.1, 25.0, 25.3]
# P1dB at 0.1 GHz +19.4 min, +20.4 typ; Psat (3 dB compression) +21.7 typ. "high" = typ + 1 dB (est.).
P1DB_SETS = [("min", 19.4, 20.7), ("typ", 20.4, 21.7), ("high", 21.4, 22.7)]
GVA_ABSMAX_IN_DBM = 13.0
# Drive LPF (3-pole C-L-C, fc about 180 MHz): 18 pF C0G 1206 (ESR 0.1 ohm, ESL plus via 1 nH, est.);
# 82 nH Coilcraft 1812SMS class (Q 100 at 146 MHz -> 0.75 ohm, SRF about 1.2 GHz -> 0.21 pF, est.).
# Divider tap on CLK1 (100 pF plus 74LVC1G80 input): 5 pF (est.).
#
# CLK1-to-drive-LPF interface (revision 1, finding-1). TS-012 section 8.1 puts the Si5351 (Adafruit 2045) on the
# main board and the drive LPF, pads and GVA-84+ on the RF board in the PA bay; section 7.3 says only the DC,
# drive and coax leads pass the bulkhead. CLK1 therefore reaches the drive LPF through a 50 ohm coax from the
# Adafruit board's optional SMA ("for RF work, an optional SMA connector", adafruit.com/product/2045, read
# 2026-09-28). That is the output topology Skyworks recommends (Si5351-B Rev. 1.3 section 7.6, Figure 16: a
# ZO = 50 ohm trace, series resistor 0 ohm, at the default high drive). The only lumped load on the CLK1 pin is
# the prescaler tap and the pin stub; the drive LPF's 18 pF input capacitor sits at the far end of the line.
C_TAP_PF = 5.0       # 100 pF coupling into the 74LVC1G80 input (est.; a series resistor after the 100 pF, as the
                     # spur plan proposes, only lowers it)
C_STUB_PF = 2.0      # header pin, pads and the main-board stub to the tap (est.)
CL_MAX_PF = 15.0     # Si5351-B Rev. 1.3 Table 7: load capacitance at most 15 pF (TA -40 to 85 C)
COAX_M = [0.05, 0.10, 0.15]   # coax length through the bulkhead (est.; set by the CDR layout), nominal 0.10 m
COAX_VF = 0.66       # RG-174 class, PE dielectric (est.); RG-316 (PTFE, 0.695) is electrically shorter
COAX_Z0 = 50.0       # lossless line: 146 MHz loss of RG-174 class coax is about 0.05 dB in 15 cm (est.), ignored,
                     # which is conservative for the overdrive question
C_LIGHT = 299792458.0
# d4 length bound: half a wavelength in the coax at 144 MHz is 0.687 m, so 0.005 to 0.70 m covers every
# electrical length the line can present (the input impedance repeats every half wavelength).
D4_LEN = [0.005] + [round(0.025 * k, 3) for k in range(1, 29)]
D4_SETS = [  # (label, source R, GVA gain, P1dB set, Si5351 case): the corners that set the extremes in d2 and d3
    ("max, 25 ohm", 25.0, 25.3, "high", "high"),
    ("max, 50 ohm", 50.0, 25.3, "high", "high"),
    ("nominal", 50.0, 24.1, "typ", "nom"),
    ("min, 25 ohm", 25.0, 22.5, "min", "low"),
    ("min, 50 ohm", 50.0, 22.5, "min", "low"),
]
PADS = {  # E24 1 % pi pads (shunt, series, shunt)
    "a5_in": (62.0, 200.0, 62.0),   # 18 dB design (64.4 / 195.4 ideal)
    "a5_out": (300.0, 18.0, 300.0),  # 3 dB design (292.4 / 17.6 ideal)
    "a4_in": (82.0, 91.0, 82.0),     # 12 dB design (83.5 / 93.2 ideal): GVA near P1dB at the nominal corner
    # revision 1 design-request option (run d5): 6 dB at the CLK1 pin end of the coax, 12 dB on the RF board
    "pin": (150.0, 36.0, 150.0),     # 6 dB design (150.5 / 37.4 ideal)
    "a5_in_rf": (82.0, 91.0, 82.0),  # 12 dB, the A4 values
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
RFEED = [0.26, 0.35, 0.45]   # at 25 C part temperature (the TS-012 section 7.3 budget)
IBUS = 0.25
# Output loss, LPF plus the G5V-2 relay (revision 2, cross item X-5). The WP-PDR-21 LPF analysis revision 2
# (docs/design/analysis/lpf-ts012.md at commit 92e3805; hardware/sim/tx-lpf README) withdrew the retuned values of
# runs r6 and r7 and recommends the BOM values with 2 % parts (run r13): passband loss at 144 to 148 MHz 0.74 dB Monte
# Carlo median and 1.76 dB at the searched worst case; no build meets TS-012's 0.5 dB. Relay 0.1 dB (est.).
#   low 0.5 dB: TS-012 allocation (LPF 0.4 + relay 0.1), below every LPF result: conservative for the high side;
#   nominal 0.84 dB: r13 median 0.74 + relay 0.1;  high 1.86 dB: r13 worst case 1.76 + relay 0.1.
LOSS_DB = [0.5, 0.84, 1.86]
LOSS_RELAY_DB = 0.1
LOSS_LPF_MEDIAN_DB = 0.84   # the LPF-at-median lever figures take the output loss at most this value
# A5 module: total efficiency 0.60 typ (datasheet page 4 graph read: 5.85 W at 6.0 V and 1.63 A; 10.0 W at
# 8.0 V and 2.01 A), 0.45 min (datasheet, at 6 W, 7.2 V); guaranteed Pout 6.5 W min at 7.2 V, VGG 3.5 V,
# Pin 20 mW. VGG clamp (TS-012 revision 4, section 7.3 "Drive gating"): 0.654 divider of 1 % resistors from the
# LM2940 output (4.75 to 5.25 V over temperature), ratio 0.6493 to 0.6584: at least 4.75 x 0.6493 = 3.08 V, nominal
# 5.0 x 0.654 = 3.27 V, at most 5.25 x 0.6584 = 3.46 V (revision 2, finding-3: revision 1 used 3.5 V, which the
# clamp cannot reach). C3 lever: a pack-dependent clamp holding VGG at 3.30 to 3.50 V at the 6.4 V pack end (the
# 3.5 V upper end is the RA07M1317M "Pout 10 W at VGG 3.5 V or less" rating condition); lever figures at 3.30 V.
A5_ETA = [0.45, 0.60]
A5_POUT_MIN_72 = 6.5
A5_VGG = [3.08, 3.27, 3.30, 3.46]   # clamp minimum, clamp nominal, C3 lever minimum, clamp maximum
A5_VGG_NOM, A5_VGG_C3, A5_VGG_MAX_DESIGN = 3.27, 3.30, 3.46
A5_VGG_DESIGN = [3.08, 3.27, 3.46]  # the revision-4 clamp as designed (the "lowest", "nominal", "highest" figures)
# A4 AFT05MS004N: drain efficiency 0.67 at Pin 0.1 W, 146 MHz (Figure 13 read, 135 MHz 62 % and 155 MHz 73 %);
# 0.55 low (est.). Output scales as VDD^n from the 7.5 V curve, n 1.8 / 2.0 / 2.3 (est.: the RA07M1317M
# curve gives 1.86 between 6.0 and 8.4 V). Hand-derived match on 0.8 mm FR4 with wound coils: 0 / 0.25 / 0.5 dB
# more loss than the NXP reference circuit (est.).
A4_ETA = [0.55, 0.67]
A4_N = [1.8, 2.0, 2.3]
A4_LMATCH = [0.0, 0.25, 0.5]

# Select-on-test (SOT) drive pad for A5 (a one-time build alignment; it needs the REQ-SYS-144 delta of TS-012
# section 8.10, which is Proposed, not baselined). The pad is picked at build from a set of E24 pi pads after reading
# the power into a 50 ohm load in place of the module, with the unit's own coax in place. Residual terms in service
# (revision 2, finding-4):
SOT_MAX_GAP_DB = 0.8       # the pad set is built from real E24 pads (e24_pad_set) with adjacent losses at most this
                           # far apart; the step term is half the set's own largest gap, not an assumed step
SOT_MEAS_DB = 1.0          # level reading at about 17 mW: an allocation (+/-1.0 dB), not a characterized value. C1
                           # passes only if the reading method is shown at this level to be within it. Basis of the
                           # candidates: tinySA Ultra "absolute power level accuracy after power level calibration of
                           # +/- 2dB" (tinysa.org/wiki/pmwiki.php?n=TinySA4.Specification, read 2026-09-28): does not
                           # meet it alone; 1N5711 diode probe on the owner's Fluke 174 at about 1.3 V peak: the diode
                           # drop is a large fraction of the peak, so the probe needs its forward drop measured at the
                           # probe's own load current (DC, Fluke 174) and a check at this level (no basis yet).
SOT_MEAS_SENS_DB = [0.5, 1.0, 1.5, 2.0]   # reading uncertainties for the sensitivity table and plot
SOT_DRIFT_DB = 0.3         # in-service drift over -10 to +45 C and the supply (est., revision 1 breakdown):
                           # GVA-84+ gain 0.0004 dB/C typ at 0.1 GHz (Rev. F) over -10 to +89 C bay air: 0.04 dB;
                           # C0G, 1812SMS and 1 % resistor drift: under 0.05 dB (est.); Si5351 edge and swing
                           # drift inside its Table 7 limits (which hold at TA -40 to 85 C): 0.2 dB (est.)
SOT_TARGET_MW = 17.3       # geometric centre of 10 to 30 mW
DRIVE_TEMP_DB = 0.1        # fixed-pad drive: temperature allowance on the 25 C corners (est.; same terms as above
                           # without the Si5351 edge drift, which the Si5351 corner cases already bound)

# Temperature cases (revision 1, finding-2; revision 2, finding-9). REQ-SYS-114 asks REQ-SYS-012 to hold from -10 C
# to +45 C ambient. Revision 2 puts every case of a question in one thermal state:
#   "kd"   steady key-down at the ambient (the low-bound state for REQ-SYS-012: every part at its hottest). The PA
#          case is solved in the deck, Tc = Ta + Rth_ca x Pdiss, Pdiss = Pout (1/eta - 1) + Pin;
#   "soak" the start of a key-down after a soak at the ambient (every part at the ambient): the high-side state for
#          the open-loop question at -10 C, and at 25 C the datasheet condition (PA case 25 C), kept as an
#          informative row that equals revision 1's 25 C case.
# Case-to-ambient resistance (WP-PDR-28, hardware/sim/thermal run 2026-09-28-ts012-r2, verdicts.md):
#   A5: module case 105.69 C at 9.94 W and 45 C ambient (V05, A5-DC): (105.69 - 45) / 9.94 = 6.11 K/W (est.; the
#       run's band on that case is +19.9 / -9.6 K, which the 100 C bound case covers on the hot side);
#   A4: AFT05 tab 98.2 C at 5.55 W and 45 C (run 2026-09-28-ts012-r1, A4-DC; r2 changed only transient heat capacities
#       and lists no A4 tab row): 9.6 K/W (est.).
RTH_CA = {"a5": 6.11, "a4": 9.6}
# Drain feed parts at 25 C part temperature (TS-012 section 7.3; min, max ohm). Each non-cell part is at the ambient
# plus a key-down rise ("kd") or at the ambient ("soak"), and its resistance moves linearly with its temperature
# (lo coefficient with the min value, hi coefficient with the max value). Sources and classes:
#   cells: Molicel P28A datasheet (INR18650P28A-V1-80093, read 2026-09-28): DC IR 20 mohm (10 A, 1 s), so the pair
#     is 0.04 ohm at 23 C; TS-012's 0.06 is an estimate. Cells take a multiplier per ambient from the datasheet's
#     2.8 A discharge-temperature curves, which include the cells' own heating at that current: -10 C x3.0 to x3.3
#     (graph read at mid capacity: 0 C about 0.11 V and -20 C about 0.27 V under 23 C, so about 0.19 V at -10 C,
#     40 to 68 mohm more per cell), 25 C x1.0, +45 C x0.90 to x1.00 (the 45 C curve lies on the 23 C one) (est.).
#   AO3400A and DMP3099L pairs: RDS(on) +0.57 %/K (lo) and +0.50 %/K (hi) (est.; no datasheet curve read here);
#     junction at key-down 15 to 50 K above ambient (main-bay air 10 to 15 K above ambient in WP-PDR-28, plus
#     self-heating) (est.). At +45 C this gives x1.20 to x1.35, revision 1's hot values; soaked at -10 C, x0.80 to
#     x0.83, revision 1's cold values.
#   MF-R300 polyfuse (PTC below trip): +0.29 %/K (lo) and +0.43 %/K (hi), same rise as the MOSFETs (est.; revision 1's
#     hot x1.10 to x1.30).
#   holder contacts: x1.0 (est.). Chokes: copper +0.39 %/K, 5.6 to 44 K above ambient (est.; revision 1's hot x1.10
#     to x1.25).
FEED_CELLS = {"n": "cells, two P28A", "min": 0.04, "max": 0.06,
              "mult": {-10: (3.0, 3.3), 25: (1.0, 1.0), 45: (0.90, 1.00)}}
FEED_PARTS = [  # (part, min, max at 25 C, (tc lo, tc hi) per K, (key-down rise lo, hi) K)
    ("AO3400A pair", 0.04, 0.06, (0.0057, 0.0050), (15.0, 50.0)),
    ("MF-R300", 0.02, 0.08, (0.0029, 0.0043), (15.0, 50.0)),
    ("holder contacts", 0.02, 0.04, (0.0, 0.0), (0.0, 0.0)),
    ("DMP3099L pair", 0.13, 0.20, (0.0057, 0.0050), (15.0, 50.0)),
    ("chokes", 0.01, 0.01, (0.0039, 0.0039), (5.6, 44.0)),
]
# PA output at case temperature Tc: neither the RA07M1317M (all data at Tcase 25 C; operating case range -30 to
# +110 C) nor the AFT05MS004N datasheet gives output versus temperature. Estimate: saturated output of a silicon
# MOSFET stage falls as its on-resistance rises (about +0.6 %/K): with a 5.4 V drain and a 0.8 V knee at 25 C the
# (VDD - Vknee)^2 law gives -0.0095 dB/K; the range taken is -0.005 to -0.015 dB/K (est., Low), applied to Tc - 25 C.
# Low-bound cases take no gain below a 25 C case (conservative); the high-side soak case at -10 C takes the full law
# at -0.015 dB/K, +0.53 dB. Bound case: PA case 100 C at 45 C ambient (the REQ-SYS-181 sink trip 95 C +3 C plus
# 0.4 K/W x 5.9 W of interface rise, est.), for the Rth band of WP-PDR-28.
# Output-loss copper term: the LPF coils at PA-bay air. At 146 MHz the coil resistance is skin-effect limited, so it
# rises as the square root of the copper resistivity, +0.195 %/K (half of copper's +0.39 %/K); revision 1 used +0.39 %/K
# on the 0.4 dB allocation (+0.1 dB hot). Revision 2 applies it to the whole LPF part of the loss (conservative: part of
# the loss is mismatch and C0G dielectric loss, which do not rise with copper temperature).
# Bay air at key-down: ambient + 44 K (WP-PDR-28 revision 0 bay air up to 89 C at 45 C, est., conservative against
# the 67 C of r2 for A5-DC); at soak: the ambient.
BAY_RISE_KD = 44.0
CU_TC = 0.00195   # skin-effect copper: R_ac rises as sqrt(rho), half of +0.39 %/K (est.; applied to the whole LPF loss, conservative)
TC_CASES = [  # (key, label, ambient C, state, fixed PA case C or None, PA coefficient dB/K, no gain below 25 C)
    ("t25soak", "25 C, start of key-down (case 25 C)", 25, "soak", 25.0, -0.015, True),
    ("t25a", "25 C, key-down, -0.005 dB/K", 25, "kd", None, -0.005, True),
    ("t25b", "25 C, key-down, -0.015 dB/K", 25, "kd", None, -0.015, True),
    ("cold0", "-10 C, key-down, PA no cold gain", -10, "kd", None, -0.015, True),
    ("coldhi", "-10 C, start of key-down, PA +0.53 dB", -10, "soak", -10.0, -0.015, False),
    ("hot45a", "+45 C, key-down, -0.005 dB/K", 45, "kd", None, -0.005, True),
    ("hot45b", "+45 C, key-down, -0.015 dB/K", 45, "kd", None, -0.015, True),
    ("hot100a", "+45 C, case 100 C bound, -0.005 dB/K", 45, "kd", 100.0, -0.005, True),
    ("hot100b", "+45 C, case 100 C bound, -0.015 dB/K", 45, "kd", 100.0, -0.015, True),
]
TC_SHORT = {"t25soak": "25 C\nkey-down start", "t25a": "25 C key-down\n-0.005 dB/K", "t25b": "25 C key-down\n-0.015 dB/K",
            "cold0": "-10 C key-down\nno cold gain", "coldhi": "-10 C start\n+0.53 dB", "hot45a": "+45 C key-down\n-0.005 dB/K",
            "hot45b": "+45 C key-down\n-0.015 dB/K", "hot100a": "+45 C, 100 C\n-0.005 dB/K", "hot100b": "+45 C, 100 C\n-0.015 dB/K"}
TC_REF = "t25a"      # the 25 C key-down case that the "25 C" figures of revision 2 quote (with t25b beside it)
# Terms of the closure figure not carried as corners (revision 1, finding-2 E3; revision 2: the LPF term is now a
# corner of the output loss, and the GVA-84+ gain at 146 MHz is added, finding-8). One-sided or symmetric, in dB.
CLOSURE_UNC = [  # (term, low dB, high dB, basis)
    ("RA07M1317M curve graph read", -0.07, 0.07, "+/-0.1 W reading error at about 6 W (estimate)"),
    ("GVA-84+ in LM2940 dropout at 6.4 V (drive down, module near saturation)", -0.05, 0.0,
     "slope of the digitized RA07M1317M Pout-Pin curve at 7.2 V: about 0.08 dB per dB of drive from 7 to 10 dBm and "
     "0.005 dB per dB above, for up to 0.5 dB less drive (estimate)"),
    ("GVA-84+ gain at 146 MHz below its 0.1 GHz value (finding-8)", -0.03, 0.0,
     "Rev. F typical gain 24.1 dB at 0.1 GHz and 21.7 dB at 1.0 GHz: 0.1 to 0.4 dB less at 146 MHz, times the "
     "0.08 dB/dB module slope (estimate)"),
]

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
        def provs(o):   # every "ltspice" provenance block in the earlier result (d4 has four)
            if isinstance(o, dict):
                for k, v in o.items():
                    if k == "ltspice" and isinstance(v, dict):
                        yield v
                    else:
                        yield from provs(v)
            elif isinstance(o, list):
                for v in o:
                    yield from provs(v)
        for prev in provs(json.loads(old.read_text())):
            if prev.get("deck") == deck.name and prev.get("deck_sha256") == sha(deck):
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
    """Mixed-radix order used in the d2 and d3 decks: isrc fastest, then freq, P1dB set, gain, source R, coax."""
    out = []
    for cx in COAX_M:
        for irs, rs in enumerate(RSRC):
            for ig, g in enumerate(GAINS):
                for ip, (pl, _, _) in enumerate(P1DB_SETS):
                    for ifr, f in enumerate(FREQS):
                        for isrc, (sl, vddo, tr, duty) in enumerate(SRC_CASES):
                            out.append(dict(rsrc=rs, gain=g, p1db=pl, freq=f, src=sl, vddo=vddo, tr=tr, duty=duty,
                                            coax_m=cx))
    return out


def d4_corners():
    """Order used in the d4 decks: length fastest, then corner set, then frequency."""
    src = {s[0]: s for s in SRC_CASES}
    out = []
    for f in FREQS:
        for lab, rs, g, pl, sc in D4_SETS:
            for ln in D4_LEN:
                _, vddo, tr, duty = src[sc]
                out.append(dict(set=lab, rsrc=rs, gain=g, p1db=pl, freq=f, src=sc, vddo=vddo, tr=tr, duty=duty,
                                coax_m=ln))
    return out


def radix_lines(dims):
    """.param lines that split the flat step index idx into mixed-radix digits (first dimension fastest)."""
    radix, lines = 1, []
    for name, n in dims:
        lines.append(f".param {name}=floor(idx/{radix})-{n}*floor(idx/{radix * n})")
        radix *= n
    return lines, radix


def feed_parts_at(ambient: float | None, state: str, level: int) -> list[tuple[str, float, float]]:
    """Per part (name, resistance ohm, multiplier) at level 0, 1, 2 (low, TS-012 criterion, high at 25 C part
    temperature). ambient None: every part at 25 C (the reference). Each part moves from its minimum to its maximum
    with the level, and so do its temperature coefficient, its key-down rise and the cell multiplier."""
    x = level / 2.0
    out = []
    c = FEED_CELLS
    m = (1.0, 1.0) if ambient is None else c["mult"][int(ambient)]
    mc = m[0] + x * (m[1] - m[0])
    out.append((c["n"], (c["min"] + x * (c["max"] - c["min"])) * mc, mc))
    for name, lo, hi, tcs, rise in FEED_PARTS:
        r25 = lo + x * (hi - lo)
        if ambient is None:
            mult = 1.0
        else:
            t = ambient + ((rise[0] + x * (rise[1] - rise[0])) if state == "kd" else 0.0)
            mult = 1.0 + (tcs[0] + x * (tcs[1] - tcs[0])) * (t - 25.0)
        out.append((name, r25 * mult, mult))
    return out


def feed_at(case_key: str | None, level: int) -> float:
    """Drain feed resistance (ohm) for a temperature case at level 0, 1, 2; scaled so that every part at 25 C gives
    exactly RFEED (0.26, 0.35, 0.45 ohm, the TS-012 budget)."""
    ref = sum(r for _, r, _ in feed_parts_at(None, "soak", level))
    if case_key is None:
        return RFEED[level]
    tc = tc_by_key(case_key)
    return RFEED[level] * sum(r for _, r, _ in feed_parts_at(tc[2], tc[3], level)) / ref


def copper_db_per_db(tc) -> float:
    """Output-loss copper term as a fraction of the LPF part of the loss (dB per dB), for a temperature case."""
    bay = tc[2] + (BAY_RISE_KD if tc[3] == "kd" else 0.0)
    return CU_TC * (bay - 25.0)


def tc_by_key(k):
    return next(c for c in TC_CASES if c[0] == k)


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


def dft_c(t, v, f, harmonic=1, periods=3):
    """Complex phasor of the given harmonic over the last whole periods (same resampling as dft_amp)."""
    T = 1 / f
    t1 = t[-1]
    t0 = t1 - periods * T
    n = periods * 1024
    tt = np.linspace(t0, t1, n, endpoint=False)
    vv = np.interp(tt, t, v)
    return 2 * np.mean(vv * np.exp(-2j * np.pi * harmonic * f * (tt - t0)))


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
    verdict("d1", "check: GVA-84+ model 1 dB and 3 dB points within 0.1 and 0.15 dB of the datasheet", all(checks), "check")
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


# ---------------------------------------------------------------- d2, d3, d4: drive chains
def chain_text(fin: str, pinpad: bool = False) -> tuple[str, str]:
    if fin == "a5":
        a, b, c = PADS["a5_in_rf"] if pinpad else PADS["a5_in"]
        q1, q2, q3 = PADS["a5_out"]
        chain = f"""* {'12 dB RF-board input pad (E24 1 %; 6 dB of the 18 dB moved to the pin end)' if pinpad else '18 dB input pad (E24 1 %)'}
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
        title = "A5: Si5351A CLK1 -> coax -> drive LPF -> 18 dB pad -> GVA-84+ -> 3 dB pad -> RA07M1317M input (50 ohm)"
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
        title = "A4: Si5351A CLK1 -> coax -> drive LPF -> 12 dB pad -> GVA-84+ -> AFT05MS004N reference-circuit input (50 ohm)"
    return chain, title


def deck_drive(fin: str, out: Path, mode: str = "full", tstep: str = "20p", pinpad: bool = False) -> Path:
    """mode "full": the d2/d3 corners (drive_corners order); "d4": the coax-length bound (d4_corners order);
    "tstep": the d4 sets at the nominal coax length with a 10 ps step (numerical check of the 20 ps step)."""
    src = {s[0]: s for s in SRC_CASES}
    if mode == "full":
        dims = [("isrc", len(SRC_CASES)), ("ifr", len(FREQS)), ("ip1", len(P1DB_SETS)), ("ig", len(GAINS)),
                ("irs", len(RSRC)), ("icx", len(COAX_M))]
        tables = [("vddo", "isrc", [c[1] for c in SRC_CASES]), ("tr", "isrc", [c[2] / 0.6 for c in SRC_CASES]),
                  ("duty", "isrc", [c[3] for c in SRC_CASES]), ("freq", "ifr", FREQS),
                  ("vsat", "ip1", [RAPP_VSAT[s[0]] for s in P1DB_SETS]), ("gdb", "ig", GAINS),
                  ("rsrc", "irs", RSRC), ("clen", "icx", COAX_M)]
        name = f"drive_{fin}.cir"
        order = ("source case (VDDO, 20-80 % edge, duty) fastest, then frequency, GVA-84+ P1dB set, GVA-84+ gain, "
                 "Si5351 output resistance, coax length")
    else:
        lens = D4_LEN if mode == "d4" else [COAX_M[1]]
        dims = [("ilen", len(lens)), ("iset", len(D4_SETS)), ("ifr", len(FREQS))]
        tables = [("clen", "ilen", lens), ("rsrc", "iset", [s[1] for s in D4_SETS]),
                  ("gdb", "iset", [s[2] for s in D4_SETS]), ("vsat", "iset", [RAPP_VSAT[s[3]] for s in D4_SETS]),
                  ("vddo", "iset", [src[s[4]][1] for s in D4_SETS]),
                  ("tr", "iset", [src[s[4]][2] / 0.6 for s in D4_SETS]),
                  ("duty", "iset", [src[s[4]][3] for s in D4_SETS]), ("freq", "ifr", FREQS)]
        name = f"coax_{fin}.cir" if mode == "d4" else f"tstep_{fin}.cir"
        order = "coax length fastest, then corner set (" + "; ".join(s[0] for s in D4_SETS) + "), then frequency"
    lines, n = radix_lines(dims)
    tabs = []
    for pname, iname, vals in tables:
        tabs.append(f".param {pname}=" + (f"table({iname}," + ",".join(f"{i},{v:.6g}" for i, v in enumerate(vals)) + ")"
                                          if len(vals) > 1 else f"{vals[0]:.6g}"))
    chain, title = chain_text(fin, pinpad)
    if pinpad:
        e1, e2, e3 = PADS["pin"]
        title += " (design-request option: 6 dB pad at the CLK1 end of the coax)"
        line = f"""* design-request option (revision 1): 6 dB pi pad (E24 1 %) on the main board at the CLK1 pin, before the coax
Rpp1 clk 0 {e1}
Rpp2 clk ppo {e2}
Rpp3 ppo 0 {e3}
* 50 ohm coax through the bulkhead (lossless; velocity factor {COAX_VF}, length clen in metres)
T1 ppo 0 lpfin 0 Td={{clen/({COAX_VF}*{C_LIGHT:.0f})}} Z0={COAX_Z0:g}"""
    else:
        line = f"""* 50 ohm coax through the bulkhead (lossless; velocity factor {COAX_VF}, length clen in metres)
T1 clk 0 lpfin 0 Td={{clen/({COAX_VF}*{C_LIGHT:.0f})}} Z0={COAX_Z0:g}"""
    txt = f"""* {name}: {title}
* cwht WP-PDR-21 pre-order drive-window analysis, revision 1, hardware/sim/tx-pa (record docs/design/analysis/pa-drive-ts012.md)
* {n} steps flattened into one .step (idx): {order}.
* The Si5351 CLK1 is a trapezoid Thevenin source of VDDO swing with the DC removed (the drive path is AC coupled)
* behind 25 or 50 ohm. Interface as designed (TS-012 section 8.1): the prescaler tap and the pin stub load the pin
* on the main board; a 50 ohm coax (Si5351 Rev. 1.3 Figure 16 topology) carries CLK1 through the bulkhead to the
* drive LPF on the RF board. The checker takes the fundamental and 3rd harmonic at V(gin) and V(pa_in), and the
* pin impedance V(clk)/I(Rsrc) at the fundamental, by DFT of the last three periods in the .raw.
.param idx=0
.step param idx 0 {n - 1} 1
{chr(10).join(lines)}
{chr(10).join(tabs)}
.param T=1/freq
.param ton=duty*T-tr
.param G=pow(10,gdb/20)
.param p={RAPP_P}
V1 vs 0 PULSE({{-duty*vddo}} {{(1-duty)*vddo}} 0 {{tr}} {{tr}} {{ton}} {{T}})
Rsrc vs clk {{rsrc}}
* lumped load on the CLK1 pin (main board): prescaler tap (100 pF into the 74LVC1G80) {C_TAP_PF:g} pF (est.) and
* header pin, pads and stub {C_STUB_PF:g} pF (est.): {C_TAP_PF + C_STUB_PF:g} pF against the Table 7 maximum of {CL_MAX_PF:g} pF
Ctap clk 0 {C_TAP_PF:g}p
Cstub clk 0 {C_STUB_PF:g}p
{line}
* 3-pole drive LPF on the RF board: 18 pF C0G 1206 (ESR, ESL plus via est.), 82 nH 1812SMS class (Q 100, SRF 1.2 GHz est.)
C1 lpfin 0 18p Rser=0.1 Lser=1n
L1 lpfin lpf 82n Rser=0.75 Cpar=0.21p
C2 lpf 0 18p Rser=0.1 Lser=1n
{chain}.tran 0 112n 90n {tstep}
.options plotwinsize=0
.save V(clk) V(gin) V(pa_in) I(Rsrc)
.end
"""
    p = out / name
    p.write_text(txt)
    return p


def read_drive_raw(fin: str, raw_path: Path, corners: list[dict]) -> list[dict]:
    raw = RawRead(str(raw_path))
    steps = raw.get_steps()
    assert len(steps) == len(corners), (len(steps), len(corners))
    tname = raw.get_trace_names()[0]
    rows = []
    for i, c in enumerate(corners):
        t = np.abs(raw.get_trace(tname).get_wave(i))
        vpa = raw.get_trace("V(pa_in)").get_wave(i)
        vg = raw.get_trace("V(gin)").get_wave(i)
        vc = raw.get_trace("V(clk)").get_wave(i)
        ir = raw.get_trace("I(Rsrc)").get_wave(i)
        f = c["freq"]
        a1 = dft_amp(t, vpa, f, 1)
        g1 = dft_amp(t, vg, f, 1)
        g3 = dft_amp(t, vg, f, 3)
        y = dft_c(t, ir, f, 1) / dft_c(t, vc, f, 1)   # pin admittance at the fundamental (current into the load)
        m = t >= t[-1] - 3 / f
        pin_dbm = float(dbm(a1 * a1 / 100))
        rows.append({**c, "pin_pa_w": a1 * a1 / 100, "pin_pa_dbm": pin_dbm,
                     "gva_in_dbm": float(dbm(g1 * g1 / 100)), "h3_dbc_gva_in": float(20 * np.log10(g3 / g1)),
                     "gva_out_dbm": pin_dbm + (float(pad_loss_db(*PADS["a5_out"])) if fin == "a5" else 0.0),
                     "gva_in_peak_v": float(np.max(np.abs(vg[m]))),
                     "clk_vpp": float(np.max(vc[m]) - np.min(vc[m])),
                     "pin_load_cp_pf": float(y.imag / (2 * np.pi * f) * 1e12),
                     "pin_load_rp_ohm": float(1 / y.real) if y.real != 0 else float("inf"),
                     "pin_load_absz_ohm": float(abs(1 / y))})
    return rows


def is_nominal_drive(r):
    return (r["rsrc"] == 50 and r["gain"] == 24.1 and r["p1db"] == "typ" and r["freq"] == 146e6 and r["src"] == "nom"
            and abs(r["coax_m"] - COAX_M[1]) < 1e-9)


def analyse_drive(fin: str, key: str, pinpad: bool = False):
    out = rundir(key)
    deck = deck_drive(fin, out, "full", pinpad=pinpad)
    prov = run_ltspice(deck, out)
    corners = drive_corners()
    rows = read_drive_raw(fin, out / f"drive_{fin}.raw", corners)
    pin = np.array([r["pin_pa_w"] for r in rows])
    h3 = np.array([r["h3_dbc_gva_in"] for r in rows])
    gin = np.array([r["gva_in_dbm"] for r in rows])
    crit = [r for r in rows if r["gain"] in (22.5, 25.0) and r["src"] == "nom"]  # TS-012 criterion corners
    pcrit = np.array([r["pin_pa_w"] for r in crit])
    nominal = next(r for r in rows if is_nominal_drive(r))
    lo, hi = min(rows, key=lambda r: r["pin_pa_w"]), max(rows, key=lambda r: r["pin_pa_w"])
    res = {"run": RUNS[key], "finalist": fin.upper(), "ltspice": prov, "n_corners": len(rows), "pinpad_option": pinpad,
           "interface": {"c_tap_pf": C_TAP_PF, "c_stub_pf": C_STUB_PF, "lumped_pin_c_pf": C_TAP_PF + C_STUB_PF,
                         "cl_max_pf": CL_MAX_PF, "lumped_pin_c_pass": bool(C_TAP_PF + C_STUB_PF <= CL_MAX_PF),
                         "coax_m": COAX_M, "coax_vf": COAX_VF, "coax_z0": COAX_Z0},
           "pad_loss_db": {k: round(float(pad_loss_db(*v)), 3) for k, v in PADS.items()},
           "pin_pa_w": {"min": float(pin.min()), "nominal": nominal["pin_pa_w"], "max": float(pin.max())},
           "pin_pa_dbm": {"min": float(dbm(pin.min())), "nominal": nominal["pin_pa_dbm"], "max": float(dbm(pin.max()))},
           "pin_pa_criterion_corners_w": {"min": float(pcrit.min()), "max": float(pcrit.max())},
           "corner_min": lo, "corner_max": hi, "nominal_corner": nominal,
           "h3_dbc_gva_in_worst": float(h3.max()), "h3_pass": bool(h3.max() <= -H3_MIN_DBC),
           "gva_in_dbm_max": float(gin.max()), "gva_absmax_pass": bool(gin.max() < GVA_ABSMAX_IN_DBM),
           "gva_out_dbm": {"nominal": nominal["gva_out_dbm"], "max": float(max(r["gva_out_dbm"] for r in rows))},
           "clk_vpp": {"min": float(min(r["clk_vpp"] for r in rows)), "max": float(max(r["clk_vpp"] for r in rows))},
           "pin_load": {"cp_pf_min": float(min(r["pin_load_cp_pf"] for r in rows)),
                        "cp_pf_max": float(max(r["pin_load_cp_pf"] for r in rows)),
                        "rp_ohm_min": float(min(r["pin_load_rp_ohm"] for r in rows)),
                        "absz_ohm_min": float(min(r["pin_load_absz_ohm"] for r in rows)),
                        "absz_ohm_max": float(max(r["pin_load_absz_ohm"] for r in rows))},
           "per_coax": {}}
    for cx in COAX_M:
        sel = [r for r in rows if abs(r["coax_m"] - cx) < 1e-9]
        ps = np.array([r["pin_pa_w"] for r in sel])
        pc = np.array([r["pin_pa_w"] for r in sel if r["gain"] in (22.5, 25.0) and r["src"] == "nom"])
        d = {"min_mw": float(ps.min() * 1e3), "max_mw": float(ps.max() * 1e3),
             "crit_min_mw": float(pc.min() * 1e3), "crit_max_mw": float(pc.max() * 1e3)}
        if fin == "a5":
            d.update({"above_30mw": int((ps > A5_PIN_MAX_MW * 1e-3).sum()), "below_10mw": int((ps < A5_PIN_MIN_MW * 1e-3).sum()),
                      "crit_in_window": int(((pc >= A5_PIN_MIN_MW * 1e-3) & (pc <= A5_PIN_MAX_MW * 1e-3)).sum()),
                      "crit_n": int(len(pc)), "overdrive_margin_db": float(10 * np.log10(A5_PIN_MAX_MW * 1e-3 / ps.max()))})
        else:
            d.update({"above_overdrive": int((ps > A4_PIN_OVERDRIVE_W).sum()),
                      "overdrive_margin_db": float(10 * np.log10(A4_PIN_OVERDRIVE_W / ps.max()))})
        res["per_coax"][f"{cx:.2f}"] = d
    lim = A5_PIN_MAX_MW * 1e-3 if fin == "a5" else A4_PIN_OVERDRIVE_W
    res["overdrive_margin_db"] = float(10 * np.log10(lim / pin.max()))
    res["overdrive_margin_with_temp_db"] = res["overdrive_margin_db"] - DRIVE_TEMP_DB
    if fin == "a5":
        inwin = (pin >= A5_PIN_MIN_MW * 1e-3) & (pin <= A5_PIN_MAX_MW * 1e-3)
        cw = (pcrit >= A5_PIN_MIN_MW * 1e-3) & (pcrit <= A5_PIN_MAX_MW * 1e-3)
        res.update({"window_mw": [A5_PIN_MIN_MW, A5_PIN_MAX_MW], "corners_in_window": int(inwin.sum()),
                    "corners_above_30mw": int((pin > A5_PIN_MAX_MW * 1e-3).sum()),
                    "corners_below_10mw": int((pin < A5_PIN_MIN_MW * 1e-3).sum()),
                    "criterion_corners": int(len(pcrit)), "criterion_corners_in_window": int(cw.sum()),
                    "window_pass_all_corners": bool(inwin.all()), "window_pass_criterion_corners": bool(cw.all()),
                    "spread_db": float(dbm(pin.max()) - dbm(pin.min())), "window_db": float(10 * np.log10(3.0))})
    else:
        res.update({"overdrive_w": A4_PIN_OVERDRIVE_W, "corners_above_overdrive": int((pin > A4_PIN_OVERDRIVE_W).sum()),
                    "overdrive_pass": bool((pin <= A4_PIN_OVERDRIVE_W).all())})
    vk = key
    verdict(vk, "check: one .raw step per corner", len(rows) == len(corners), "check")
    verdict(vk, f"{fin.upper()} lumped CLK1 pin load at most 15 pF (Si5351 Table 7)", res["interface"]["lumped_pin_c_pass"])
    if pinpad:
        verdict(vk, "A5 option d5: equivalent CLK1 pin load at most 15 pF at every corner",
                res["pin_load"]["cp_pf_max"] <= CL_MAX_PF, detail=f"{res['pin_load']['cp_pf_max']:.1f} pF")
    verdict(vk, f"{fin.upper()} 3f at the GVA-84+ input at least 25 dB below f", res["h3_pass"],
            detail=f"{res['h3_dbc_gva_in_worst']:.1f} dBc")
    verdict(vk, f"{fin.upper()} GVA-84+ input below +13 dBm", res["gva_absmax_pass"])
    if fin == "a5":
        verdict(vk, "A5 module input 10 to 30 mW at every corner (fixed pad)", res["window_pass_all_corners"],
                detail=f"{res['pin_pa_w']['min'] * 1e3:.1f} to {res['pin_pa_w']['max'] * 1e3:.1f} mW")
        verdict(vk, "A5 module input 10 to 30 mW at the TS-012 criterion corners (fixed pad)", res["window_pass_criterion_corners"])
    else:
        verdict(vk, "A4 drive at most the 0.2 W ruggedness-test level (informative)", res["overdrive_pass"],
                detail=f"{res['overdrive_margin_db']:+.2f} dB")
    res["verdicts"] = VERDICTS.get(vk, {})
    (out / "corners.json").write_text(json.dumps(rows, indent=1))
    plot_drive(out, fin, rows, pinpad)
    (out / "result.json").write_text(json.dumps(res, indent=2, default=float))
    write_drive_md(out, fin, res)
    copy_inputs(out, [deck])
    print(key, json.dumps({k: res[k] for k in res if k not in ("ltspice", "corner_min", "corner_max", "nominal_corner")}, default=float))
    return res


CX_COL = {0.05: "#2a78d6", 0.10: "#4a3aa7", 0.15: "#eb6834"}


def plot_drive(out: Path, fin: str, rows: list[dict], pinpad: bool = False):
    tag = "6 dB pad at the pin end (design-request option)" if pinpad else "coax to the RF board, as designed"
    from matplotlib.ticker import FixedLocator, NullLocator, ScalarFormatter
    nb = len(rows) // len(COAX_M)
    pin = np.array([r["pin_pa_w"] for r in rows])
    h3 = np.array([r["h3_dbc_gva_in"] for r in rows])
    xs = np.arange(len(rows)) % nb
    cols = [CX_COL[round(r["coax_m"], 2)] for r in rows]
    # plot 1: power into the PA input per corner, all coax lengths
    fig, ax = plt.subplots(figsize=(7.6, 5.4))
    ax.scatter(xs, pin * 1e3, s=7, c=cols, zorder=3)
    for g_i in range(len(GAINS)):
        for rs_i in range(len(RSRC)):
            ax.axvline(rs_i * 135 + g_i * 27 - 0.5, color=GRID, lw=0.8)
    ax.axvline(134.5, color=INK2, lw=1.0)
    ax.set_yscale("log")
    if fin == "a5":
        ax.axhspan(A5_PIN_MIN_MW, A5_PIN_MAX_MW, color=COL["ok"], alpha=0.08, zorder=0)
        ax.axhline(A5_PIN_MAX_MW, color=INK, lw=1.3, ls="-", label="30 mW: module maximum rating, top of the stability window")
        ax.axhline(A5_PIN_MIN_MW, color=INK, lw=1.3, ls="--", label="10 mW: bottom of the module stability window")
        ax.set_ylim(4, 60)
        ticks = [4, 5, 6, 8, 10, 15, 20, 30, 40, 60]
        ytxt = 50
    else:
        ax.axhline(A4_PIN_OVERDRIVE_W * 1e3, color=INK, lw=1.3, ls="-", label="200 mW: AFT05 ruggedness-test drive (3 dB overdrive; not a rating)")
        ax.axhline(100, color=INK2, lw=1.1, ls="--", label="100 mW: datasheet Table 8 drive at 135 and 175 MHz")
        ax.set_ylim(40, 400)
        ticks = [40, 60, 80, 100, 150, 200, 300, 400]
        ytxt = 330
    ax.text(67, ytxt, "Si5351 output 25 ohm", ha="center", fontsize=7.5, color=INK2)
    ax.text(202, ytxt, "Si5351 output 50 ohm", ha="center", fontsize=7.5, color=INK2)
    ax.yaxis.set_major_locator(FixedLocator(ticks))
    ax.yaxis.set_minor_locator(NullLocator())
    ax.yaxis.set_major_formatter(ScalarFormatter())
    ax.set_xlabel("part corner index (blocks: Si5351 source 25 ohm | 50 ohm, then GVA gain 22.5, 22.9, 24.1, 25.0, 25.3 dB;\n"
                  "within a block: P1dB set x frequency x Si5351 edge/VDDO case)")
    ax.set_ylabel("Fundamental power at the PA input (mW)")
    for cx in COAX_M:
        ax.scatter([], [], s=12, c=CX_COL[round(cx, 2)], label=f"coax {cx * 100:.0f} cm (VF {COAX_VF})")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.2), fontsize=7, ncol=2)
    ax.set_title(f"{fin.upper()} drive chain in LTspice (revision 1, {tag}):\npower into the PA input, "
                 f"{len(rows)} corners (270 part corners x 3 coax lengths), 144 to 148 MHz, 25 C")
    fig.tight_layout()
    fig.savefig(out / f"drive_{fin}_corners.png", dpi=150)
    plt.close(fig)
    # plot 2: 3f at the GVA input
    fig, ax = plt.subplots(figsize=(6.8, 4.0))
    ax.scatter(xs, h3, s=7, c=cols, zorder=3)
    ax.axhline(-H3_MIN_DBC, color=INK, lw=1.2, ls="--")
    ax.text(2, -H3_MIN_DBC + 0.5, "limit: 3f at least 25 dB below the fundamental (TS-012)", fontsize=7.5, color=INK)
    for cx in COAX_M:
        ax.scatter([], [], s=12, c=CX_COL[round(cx, 2)], label=f"coax {cx * 100:.0f} cm")
    ax.legend(loc="upper right", fontsize=8)
    ax.set_xlabel("part corner index (as in the drive plot)")
    ax.set_ylabel("3f relative to f at the GVA-84+ input (dBc)")
    ax.set_title(f"{fin.upper()} drive chain ({tag}):\nthird harmonic of the Si5351 square wave after the drive LPF", fontsize=9.5)
    ax.set_ylim(min(-62, h3.min() - 4), -12)
    fig.tight_layout()
    fig.savefig(out / f"drive_{fin}_h3.png", dpi=150)
    plt.close(fig)
    # plot 3: the CLK1 pin load
    cp = np.array([r["pin_load_cp_pf"] for r in rows])
    fig, ax = plt.subplots(figsize=(7.2, 5.0))
    ax.scatter(xs, cp, s=7, c=cols, zorder=3)
    ax.axhline(CL_MAX_PF, color=INK, lw=1.4, ls="-", label=f"{CL_MAX_PF:g} pF: Si5351 Table 7 load capacitance maximum")
    ax.axhline(C_TAP_PF + C_STUB_PF, color=COL["ok"], lw=1.4, ls="--",
               label=f"{C_TAP_PF + C_STUB_PF:g} pF: lumped load on the pin as designed (tap and stub, est.)")
    ax.axhline(23.0, color=INK2, lw=1.0, ls=":", label="23 pF: revision 0 deck (LPF and tap on the pin, not the design)")
    for cx in COAX_M:
        ax.scatter([], [], s=12, c=CX_COL[round(cx, 2)], label=f"equivalent shunt C at f, coax {cx * 100:.0f} cm")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.14), fontsize=7, ncol=2)
    ax.set_xlabel("part corner index (as in the drive plot)")
    ax.set_ylabel("Equivalent shunt capacitance at the CLK1 pin (pF)")
    ax.set_ylim(min(0, cp.min() - 3), max(30, cp.max() + 3))
    ax.set_title(f"{fin.upper()}: load on the Si5351 CLK1 pin at the fundamental (LTspice, revision 1,\n"
                 f"{tag}):\nIm(Y)/(2 pi f) of I(Rsrc)/V(clk); negative would be inductive", fontsize=9)
    fig.tight_layout()
    fig.savefig(out / f"drive_{fin}_pinload.png", dpi=150)
    plt.close(fig)


def run_d4():
    out = rundir("d4")
    corners = d4_corners()
    res = {"run": RUNS["d4"], "lengths_m": D4_LEN, "coax_vf": COAX_VF, "sets": [s[0] for s in D4_SETS], "finalists": {}}
    decks = []
    fig, axs = plt.subplots(1, 2, figsize=(11.0, 4.9))
    for ax, fin in zip(axs, ("a5", "a4")):
        deck = deck_drive(fin, out, "d4")
        decks.append(deck)
        prov = run_ltspice(deck, out)
        rows = read_drive_raw(fin, out / f"coax_{fin}.raw", corners)
        pin = np.array([r["pin_pa_w"] for r in rows])
        lim = A5_PIN_MAX_MW * 1e-3 if fin == "a5" else A4_PIN_OVERDRIVE_W
        des = [r for r in rows if COAX_M[0] - 1e-9 <= r["coax_m"] <= COAX_M[-1] + 1e-9]
        pdes = np.array([r["pin_pa_w"] for r in des])
        hi = max(rows, key=lambda r: r["pin_pa_w"])
        lo = min(rows, key=lambda r: r["pin_pa_w"])
        d = {"ltspice": prov, "n_steps": len(rows), "max_mw_any_length": float(pin.max() * 1e3),
             "min_mw_any_length": float(pin.min() * 1e3), "corner_max": hi, "corner_min": lo,
             "max_mw_design_range": float(pdes.max() * 1e3), "min_mw_design_range": float(pdes.min() * 1e3),
             "overdrive_margin_any_length_db": float(10 * np.log10(lim / pin.max())),
             "overdrive_margin_any_length_with_temp_db": float(10 * np.log10(lim / pin.max())) - DRIVE_TEMP_DB,
             "pin_load_cp_pf_range_any_length": [float(min(r["pin_load_cp_pf"] for r in rows)),
                                                 float(max(r["pin_load_cp_pf"] for r in rows))]}
        if fin == "a5":
            d["below_10mw_any_length"] = int((pin < A5_PIN_MIN_MW * 1e-3).sum())
            d["above_30mw_any_length"] = int((pin > A5_PIN_MAX_MW * 1e-3).sum())
        res["finalists"][fin.upper()] = d
        (out / f"coax_{fin}_steps.json").write_text(json.dumps(rows, indent=1))
        setcol = {D4_SETS[0][0]: COL["a4"], D4_SETS[1][0]: "#b3401a", D4_SETS[2][0]: INK2,
                  D4_SETS[3][0]: COL["a5"], D4_SETS[4][0]: COL["aux"]}
        fls = {144e6: ":", 146e6: "-", 148e6: "--"}
        for s in D4_SETS:
            for f in FREQS:
                sel = [r for r in rows if r["set"] == s[0] and r["freq"] == f]
                ax.plot([r["coax_m"] * 100 for r in sel], [r["pin_pa_w"] * 1e3 for r in sel], color=setcol[s[0]],
                        ls=fls[f], lw=1.4, label=f"{s[0]}" if f == 146e6 else None)
        ax.axvspan(COAX_M[0] * 100, COAX_M[-1] * 100, color=COL["ok"], alpha=0.08, lw=0)
        ax.text(10, 0.97, "design range\n5 to 15 cm (est.)", transform=ax.get_xaxis_transform(), ha="center", va="top",
                fontsize=7, color=INK2)
        ax.set_yscale("log")
        from matplotlib.ticker import FixedLocator, NullLocator, ScalarFormatter
        if fin == "a5":
            ax.axhline(A5_PIN_MAX_MW, color=INK, lw=1.4, label="30 mW: module maximum rating")
            ax.axhline(A5_PIN_MIN_MW, color=INK, lw=1.4, ls="-.", label="10 mW: bottom of the stability window")
            ax.set_ylim(4, 60)
            ticks = [4, 5, 6, 8, 10, 15, 20, 30, 40, 60]
            ax.set_title("A5: power into the RA07M1317M input versus coax length")
        else:
            ax.axhline(200, color=INK, lw=1.4, label="200 mW: AFT05 ruggedness-test drive (not a rating)")
            ax.axhline(100, color=INK2, lw=1.1, ls=":", label="100 mW: datasheet Table 8 drive")
            ax.set_ylim(40, 300)
            ticks = [40, 60, 80, 100, 150, 200, 300]
            ax.set_title("A4: power into the AFT05MS004N input versus coax length")
        ax.yaxis.set_major_locator(FixedLocator(ticks))
        ax.yaxis.set_minor_locator(NullLocator())
        ax.yaxis.set_major_formatter(ScalarFormatter())
        ax.set_xlim(0, 70)
        ax.set_xlabel(f"Coax length, CLK1 to the drive LPF (cm; VF {COAX_VF})")
        ax.set_ylabel("Fundamental power at the PA input (mW)")
        ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.17), ncol=2, fontsize=7)
    fig.suptitle("Coax-length bound (LTspice, revision 1): extreme part corners over every electrical length (half a wavelength\n"
                 "is 69 cm at 144 MHz, so 0 to 70 cm covers every length); line style 144 (dotted), 146 (solid), 148 MHz (dashed)", fontsize=9.5)
    fig.tight_layout()
    fig.savefig(out / "coax_length_bound.png", dpi=150)
    plt.close(fig)
    # numerical check of the 20 ps step: the d4 sets at 0.10 m with a 10 ps step, against d2/d3 at 20 ps
    chk = {}
    for fin, dkey in (("a5", "d2"), ("a4", "d3")):
        deck = deck_drive(fin, out, "tstep", tstep="10p")
        decks.append(deck)
        prov = run_ltspice(deck, out)
        cs = [dict(c, coax_m=COAX_M[1]) for c in d4_corners() if c["coax_m"] == D4_LEN[0]]
        rows10 = read_drive_raw(fin, out / f"tstep_{fin}.raw", cs)
        ref = json.loads((rundir(dkey) / "corners.json").read_text())
        diffs = []
        for r in rows10:
            m = next(x for x in ref if x["rsrc"] == r["rsrc"] and x["gain"] == r["gain"] and x["p1db"] == r["p1db"]
                     and x["freq"] == r["freq"] and x["src"] == r["src"] and abs(x["coax_m"] - COAX_M[1]) < 1e-9)
            diffs.append((abs(m["pin_pa_dbm"] - r["pin_pa_dbm"]), abs(m["h3_dbc_gva_in"] - r["h3_dbc_gva_in"])))
        dd = np.array(diffs)
        chk[fin.upper()] = {"ltspice": prov, "n": len(rows10), "max_diff_pin_db": float(dd[:, 0].max()),
                            "max_diff_h3_db": float(dd[:, 1].max()),
                            "pass": bool(dd[:, 0].max() <= 0.02 and dd[:, 1].max() <= 0.5)}
    res["timestep_check"] = chk
    for fin_, c_ in chk.items():
        verdict("d4", f"check: {fin_} 10 ps step against 20 ps within 0.02 dB (power) and 0.5 dB (3f)", c_["pass"], "check",
                f"{c_['max_diff_pin_db']:.4f} dB, {c_['max_diff_h3_db']:.3f} dB")
    verdict("d4", "A5 module input at most 30 mW at any coax length (fixed pad)",
            res["finalists"]["A5"]["overdrive_margin_any_length_db"] >= 0,
            detail=f"{res['finalists']['A5']['overdrive_margin_any_length_db']:+.2f} dB")
    verdict("d4", "A4 drive at most 0.2 W at any coax length (informative)",
            res["finalists"]["A4"]["overdrive_margin_any_length_db"] >= 0,
            detail=f"{res['finalists']['A4']['overdrive_margin_any_length_db']:+.2f} dB")
    res["verdicts"] = VERDICTS.get("d4", {})
    (out / "result.json").write_text(json.dumps(res, indent=2, default=float))
    L = [f"# {RUNS['d4']}: coax-length bound and time-step check (revision 1, finding-1)", "",
         f"Every electrical length of the 50 ohm coax (0.5 to 70 cm at VF {COAX_VF}; the line repeats every half "
         f"wavelength, 69 cm at 144 MHz) for the part corners that set the extremes ({'; '.join(s[0] for s in D4_SETS)}), "
         f"144, 146 and 148 MHz; 25 C.", "",
         "| Finalist | Max over any length (mW) | Min over any length (mW) | Max, 5 to 15 cm (mW) | Min, 5 to 15 cm (mW) | Overdrive margin, any length (dB) | Same with the 0.1 dB temperature allowance (dB) |",
         "|---|---|---|---|---|---|---|"]
    for fin, d in res["finalists"].items():
        L.append(f"| {fin} | {d['max_mw_any_length']:.1f} | {d['min_mw_any_length']:.1f} | {d['max_mw_design_range']:.1f} | "
                 f"{d['min_mw_design_range']:.1f} | {d['overdrive_margin_any_length_db']:+.2f} | {d['overdrive_margin_any_length_with_temp_db']:+.2f} |")
    L += ["", "Overdrive limit: 30 mW for A5 (module maximum rating); 200 mW for A4 (ruggedness-test drive, not a rating). "
          "A negative margin means that some length and part corner exceed the limit with the fixed pad.", ""]
    for fin, d in res["finalists"].items():
        L += [f"- {fin} highest step: {cstr(d['corner_max'])}.",
              f"- {fin} lowest step: {cstr(d['corner_min'])}.",
              f"- {fin} equivalent shunt capacitance at the CLK1 pin over every length: {d['pin_load_cp_pf_range_any_length'][0]:.1f} "
              f"to {d['pin_load_cp_pf_range_any_length'][1]:.1f} pF (informative; the lumped load is {C_TAP_PF + C_STUB_PF:g} pF)."]
    L += ["", "Time-step check (the d2 and d3 decks use a 20 ps maximum step; the same 15 corners at 10 cm rerun with 10 ps):", ""]
    for fin, c in chk.items():
        L.append(f"- {fin}: largest difference {c['max_diff_pin_db']:.4f} dB in PA input power and {c['max_diff_h3_db']:.3f} dB in 3f "
                 f"(criteria 0.02 dB and 0.5 dB): **{'PASS' if c['pass'] else 'FAIL'}**.")
    L += ["", "Plot: `coax_length_bound.png`. Steps: `coax_a5_steps.json`, `coax_a4_steps.json`. Decks `coax_a5.cir`, `coax_a4.cir`, "
          "`tstep_a5.cir`, `tstep_a4.cir`; LTspice logs and raws beside them.", ""]
    (out / "result.md").write_text("\n".join(L))
    copy_inputs(out, decks)
    print("d4", json.dumps({k: {kk: vv for kk, vv in v.items() if kk not in ("ltspice", "corner_max", "corner_min")}
                            for k, v in res["finalists"].items()}, default=float), json.dumps(chk, default=str)[:400])
    return res


def add_req_lines(ax):
    ax.axhline(REQ012_HI, color=INK, lw=1.2, ls="--", label="6.30 W: REQ-SYS-012 upper bound (held by the ALC)")
    ax.axhline(REQ012_NOM, color=INK, lw=1.2, ls="-", label="5.0 W: REQ-SYS-012 nominal (ALC set point)")
    ax.axhline(REQ012_LO, color=INK, lw=2.0, ls="--", label="3.97 W: REQ-SYS-012 lower bound (5 W -1 dB)")


def cstr(c):
    s = (f"source {c['rsrc']:.0f} ohm, GVA gain {c['gain']} dB, P1dB set {c['p1db']}, {c['freq'] / 1e6:.0f} MHz, "
         f"Si5351 case {c['src']} (VDDO {c['vddo']} V, edge {c['tr'] * 1e9:.1f} ns, duty {c['duty']:.2f})")
    if "coax_m" in c:
        s += f", coax {c['coax_m'] * 100:.1f} cm"
    return s


def write_drive_md(out, fin, r):
    L = [f"# {r['run']}: {fin.upper()} drive chain (WP-PDR-21 drive window), revision 1", "",
         f"Interface (TS-012 section 8.1 layout): CLK1 on the main board, 50 ohm coax of "
         f"{', '.join(f'{x * 100:.0f}' for x in COAX_M)} cm (VF {COAX_VF}, est.) to the drive LPF on the RF board. "
         f"Lumped load on the CLK1 pin: tap {C_TAP_PF:g} pF + stub {C_STUB_PF:g} pF = {C_TAP_PF + C_STUB_PF:g} pF (estimates) "
         f"against the Si5351 Table 7 maximum of {CL_MAX_PF:g} pF: **{'PASS' if r['interface']['lumped_pin_c_pass'] else 'FAIL'}**. "
         f"All corners at 25 C; the drive moves by at most {DRIVE_TEMP_DB} dB over -10 to +45 C (estimate, see the analysis record).", ""]
    if r.get("pinpad_option"):
        L[2:2] = [f"**Design-request option, not the TS-012 revision 4 design:** a 6 dB pi pad {PADS['pin']} ohm (E24 1 %) on the "
                  f"main board at the CLK1 pin, before the coax, and a 12 dB pad {PADS['a5_in_rf']} ohm on the RF board in place "
                  f"of the 18 dB pad (total {pad_loss_db(*PADS['pin']) + pad_loss_db(*PADS['a5_in_rf']):.2f} dB against 18.42 dB).", ""]
    if fin == "a5":
        L += [f"Verdict, module input window 10 to 30 mW, taken over all {r['n_corners']} corners: "
              f"**{'PASS' if r['window_pass_all_corners'] else 'FAIL'}** ({r['corners_in_window']} corners inside the window, "
              f"{r['corners_above_30mw']} above 30 mW, {r['corners_below_10mw']} below 10 mW). Taken over the TS-012 criterion "
              f"corners only (source 25 and 50 ohm, gain 22.5 and 25.0 dB, 144 to 148 MHz, nominal Si5351 edge and VDDO, all "
              f"P1dB sets, all coax lengths): **{'PASS' if r['window_pass_criterion_corners'] else 'FAIL'}** "
              f"({r['criterion_corners_in_window']} of {r['criterion_corners']} inside).",
              f"Overdrive margin, fixed pad (highest corner against 30 mW): {r['overdrive_margin_db']:+.2f} dB; "
              f"{r['overdrive_margin_with_temp_db']:+.2f} dB with the {DRIVE_TEMP_DB} dB temperature allowance.", ""]
    else:
        L += [f"Verdict, AFT05 drive at or below the 0.2 W ruggedness-test level (informative, not a rating): "
              f"**{'PASS' if r['overdrive_pass'] else 'FAIL'}** ({r['corners_above_overdrive']} corners above; margin "
              f"{r['overdrive_margin_db']:+.2f} dB, {r['overdrive_margin_with_temp_db']:+.2f} dB with the temperature allowance).", ""]
    L += [f"Verdict, 3f at the GVA-84+ input at least 25 dB below the fundamental: **{'PASS' if r['h3_pass'] else 'FAIL'}** "
          f"(worst {r['h3_dbc_gva_in_worst']:.1f} dBc).",
          f"GVA-84+ input at most {r['gva_in_dbm_max']:.1f} dBm against the +13 dBm maximum rating: "
          f"**{'PASS' if r['gva_absmax_pass'] else 'FAIL'}**. GVA-84+ output: nominal {r['gva_out_dbm']['nominal']:.1f} dBm, "
          f"highest {r['gva_out_dbm']['max']:.1f} dBm.", "",
          "| Quantity | Min | Nominal | Max |", "|---|---|---|---|",
          f"| Power into the PA input (mW) | {r['pin_pa_w']['min'] * 1e3:.1f} | {r['pin_pa_w']['nominal'] * 1e3:.1f} | {r['pin_pa_w']['max'] * 1e3:.1f} |",
          f"| Power into the PA input (dBm) | {r['pin_pa_dbm']['min']:.2f} | {r['pin_pa_dbm']['nominal']:.2f} | {r['pin_pa_dbm']['max']:.2f} |",
          f"| CLK1 pin swing, peak to peak (V) | {r['clk_vpp']['min']:.2f} | - | {r['clk_vpp']['max']:.2f} |",
          f"| CLK1 pin load at f, equivalent shunt C (pF; informative) | {r['pin_load']['cp_pf_min']:.1f} | - | {r['pin_load']['cp_pf_max']:.1f} |",
          f"| CLK1 pin load at f, magnitude (ohm) | {r['pin_load']['absz_ohm_min']:.1f} | - | {r['pin_load']['absz_ohm_max']:.1f} |", "",
          "| Coax (cm) | Min (mW) | Max (mW) | Criterion corners (mW) | " + ("Above 30 mW | Below 10 mW | Overdrive margin (dB) |" if fin == "a5" else "Above 0.2 W | Overdrive margin (dB) |"),
          "|---|---|---|---|" + ("---|---|---|" if fin == "a5" else "---|---|")]
    for cx, d in r["per_coax"].items():
        row = f"| {float(cx) * 100:.0f} | {d['min_mw']:.1f} | {d['max_mw']:.1f} | {d['crit_min_mw']:.1f} to {d['crit_max_mw']:.1f} | "
        row += (f"{d['above_30mw']} | {d['below_10mw']} | {d['overdrive_margin_db']:+.2f} |" if fin == "a5"
                else f"{d['above_overdrive']} | {d['overdrive_margin_db']:+.2f} |")
        L.append(row)
    L += ["", f"- Lowest corner: {cstr(r['corner_min'])}.",
          f"- Highest corner: {cstr(r['corner_max'])}.",
          f"- Nominal corner: {cstr(r['nominal_corner'])}.",
          f"- Pad insertion loss between 50 ohm terminations (E24 values): {r['pad_loss_db']}.", ""]
    if fin == "a5":
        L += [f"- Spread of the drive over all corners {r['spread_db']:.2f} dB against a window of {r['window_db']:.2f} dB (10 to 30 mW).", ""]
    L += [f"Plots: `drive_{fin}_corners.png` (power into the PA input per corner and coax length, with the limits), "
          f"`drive_{fin}_h3.png` (3f at the GVA-84+ input), `drive_{fin}_pinload.png` (load on the CLK1 pin against "
          f"Table 7). Per-corner numbers: `corners.json`. Deck `drive_{fin}.cir`; LTspice log and raw beside it.", ""]
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
        dims = [("irf", RFEED), ("ieta", A5_ETA), ("ipin", pins), ("ifr", FREQS), ("ivgg", A5_VGG),
                ("isp", ["typ", "min"]), ("iloss", LOSS_DB), ("itc", [c[0] for c in TC_CASES])]
    else:
        T = a4_tables()
        dims = [("irf", RFEED), ("ieta", A4_ETA), ("ipin", pins), ("ifr", FREQS), ("in", A4_N),
                ("imatch", A4_LMATCH), ("iloss", LOSS_DB), ("itc", [c[0] for c in TC_CASES])]
    n = int(np.prod([len(v) for _, v in dims]))
    # mixed radix, first dimension fastest
    radix, lines = 1, []
    for name, vals in dims:
        lines.append(f".param {name}=floor(idx/{radix})-{len(vals)}*floor(idx/{radix * len(vals)})")
        radix *= len(vals)
    import itertools
    for combo in itertools.product(*[range(len(v)) for _, v in dims][::-1]):
        combo = combo[::-1]
        c = {name: vals[k] for (name, vals), k in zip(dims, combo)}
        c["rf_ohm"] = feed_at(c["itc"], RFEED.index(c["irf"]))
        corners.append(c)
    def tab(name, vals, fmt="{:.6g}"):
        return f".param {name[1:]}=table({name}," + ",".join(f"{i},{fmt.format(v)}" for i, v in enumerate(vals)) + ")"
    def tctab(pname, vals, fmt="{:.6g}"):
        return f".param {pname}=table(itc," + ",".join(f"{i},{fmt.format(v)}" for i, v in enumerate(vals)) + ")"
    # temperature cases (revision 2, finding-9): drain feed per case and level at that case's part temperatures;
    # PA case temperature fixed (soak and bound cases) or solved from the dissipation (key-down cases); PA
    # coefficient and the no-gain-below-25-C rule; copper term on the LPF part of the output loss
    rf_flat = [feed_at(tc[0], lv) for tc in TC_CASES for lv in range(len(RFEED))]
    pinw_expr = "pow(10,(pin-30)/10)" if fin == "a5" else "pin"
    common = [f"* temperature cases (itc): " + "; ".join(f"{i} {tc[1]}" for i, tc in enumerate(TC_CASES)),
              f".param rf=table(itc*{len(RFEED)}+irf," + ",".join(f"{i},{v:.5g}" for i, v in enumerate(rf_flat)) + ")",
              "* ambient (C); fixed PA case (C; -999: solved from the dissipation); PA coefficient (dB/K above 25 C);",
              "* no gain below a 25 C case (1) or the full law (0); copper term (dB per dB of LPF loss)",
              tctab("ta", [tc[2] for tc in TC_CASES]),
              tctab("tcfix", [tc[4] if tc[4] is not None else -999 for tc in TC_CASES]),
              tctab("coef", [tc[5] for tc in TC_CASES]),
              tctab("ng", [1 if tc[6] else 0 for tc in TC_CASES]),
              tctab("cu", [copper_db_per_db(tc) for tc in TC_CASES]),
              f".param rth={RTH_CA[fin]}",
              f".param pinw_pa={pinw_expr}",
              tab("ipin", pins), tab("ifr", FREQS), tab("iloss", LOSS_DB),
              ".param w=(fr-135e6)/20e6",
              f".param kloss=pow(10,-(loss+(loss-{LOSS_RELAY_DB})*cu)/10)"]
    thermal = """* PA case temperature: fixed, or ambient plus Rth_ca times the PA dissipation Pout (1/eta - 1) + Pin (WP-PDR-28)
Btc tc 0 V=if(tcfix>-500,tcfix,ta+rth*(V(pmod)*(1/eta-1)+pinw_pa))
Rtc tc 0 1meg
.func kt(t)=pow(10,coef*if(ng>0.5,max(t-25,0),t-25)/10)
"""
    if fin == "a5":
        vt135 = table_expr("x", T["xv"], T["v135"])
        vt155 = table_expr("x", T["xv"], T["v155"])
        pt135 = table_expr("pin", T["xp"], T["p135"])
        pt155 = table_expr("pin", T["xp"], T["p155"])
        pr135 = table_expr("13.0103", T["xp"], T["p135"])
        pr155 = table_expr("13.0103", T["xp"], T["p155"])
        gh135 = table_expr("3.5", T["xg"], T["g135"])
        gh155 = table_expr("3.5", T["xg"], T["g155"])
        kvl = []
        for j, vg in enumerate(A5_VGG):
            g135 = table_expr(f"{vg}", T["xg"], T["g135"])
            g155 = table_expr(f"{vg}", T["xg"], T["g155"])
            kvl.append(f".param kv{j}=((1-w)*{g135}+w*{g155})/((1-w)*{gh135}+w*{gh155})")
        kv_sel = f"kv{len(A5_VGG) - 1}"
        for j in range(len(A5_VGG) - 2, -1, -1):
            kv_sel = f"if(ivgg_<{j + 0.5},kv{j},{kv_sel})"
        v72_135 = table_expr("7.2", T["xv"], T["v135"])
        v72_155 = table_expr("7.2", T["xv"], T["v155"])
        model = f"""{tab('ieta', A5_ETA)}
.param ivgg_=ivgg
.param isp_=isp
* drive factor: module output at pin relative to Pin 20 mW (13.01 dBm), datasheet Pout-Pin curves at 7.2 V
.param kd=((1-w)*pow(10,{pt135}/10)+w*pow(10,{pt155}/10))/((1-w)*pow(10,{pr135}/10)+w*pow(10,{pr155}/10))
* VGG factor: output at VGG {', '.join(f'{v}' for v in A5_VGG)} V relative to 3.5 V (the Pout-VDD curve's condition),
* datasheet Pout-VGG curves at 7.2 V, Pin 20 mW (revision 2: the revision-4 clamp and the C3 lever, finding-3)
{chr(10).join(kvl)}
.param kv={kv_sel}
* spread factor: datasheet minimum 6.5 W at 7.2 V, VGG 3.5 V, Pin 20 mW against the typical curve
.param kmin={A5_POUT_MIN_72}/((1-w)*{v72_135}+w*{v72_155})
.param ks=if(isp_>0.5,kmin,1)
* RA07M1317M: typical Pout versus drain voltage at Pin 20 mW, VGG 3.5 V (135 and 155 MHz, interpolated in f)
.func pv(x)=(1-w)*{vt135}+w*{vt155}
{thermal}Bmod pmod 0 V=pv(max(V(d),3))*kd*kv*ks*kt(V(tc))
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
{thermal}Bmod pmod 0 V=p75*pow(max(V(d),1)/7.5,n)*kmatch*kt(V(tc))
Rmod pmod 0 1meg
Bpa d 0 I=V(pmod)/(eta*max(V(d),1))
"""
        title = "A4 AFT05MS004N"
    txt = f"""* power_{fin}.cir: {title}, output power at the SMA versus pack voltage (cwht WP-PDR-21, hardware/sim/tx-pa, revision {REVISION})
* Pack EMF Vp (swept 6.4 to 8.4 V; equal to the voltage read in receive within 10 mV) behind the drain feed rfeed;
* the 5 V bus ({IBUS} A, est.) and the PA drain current Pout/(eta*Vd) load the feed, so the key-down sag is solved
* by LTspice, together with the PA case temperature V(tc) of the key-down cases. V(pmod) is the PA output power in
* watts, V(psma) the power at the SMA after the output LPF and relay.
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
.save V(d) V(pmod) V(psma) V(tc) I(Vp)
.end
"""
    p = out / f"power_{fin}.cir"
    p.write_text(txt)
    return p, corners


RUN_LABEL = {"p1": "drive as designed (fixed 18 dB pad, coax 5 to 15 cm)",
             "p2": "drive as designed (fixed 12 dB pad, coax 5 to 15 cm)",
             "p3": "select-on-test drive pad (in-service band of s1)"}


def run_key(r: dict) -> str:
    return next(k for k, v in RUNS.items() if v == r["run"])


def pstr(c: dict, tcase_c: float | None = None) -> str:
    """A power-model corner in words (revision 1, finding-3: every quoted corner with its full parameter set;
    revision 2: the PA case temperature at 6.4 V and the copper term of the case)."""
    tc = tc_by_key(c["itc"])
    pin_s = f"{c['ipin']:.2f} dBm" if c["ipin"] > 1 else f"{c['ipin'] * 1e3:.1f} mW"
    s = (f"{tc[1]}; drain feed level {c['irf']:.2f} ohm at 25 C part temperature ({c['rf_ohm']:.3f} ohm in this case); "
         f"efficiency {c['ieta']:.2f}; PA input {pin_s}; {c['ifr'] / 1e6:.0f} MHz; ")
    if "ivgg" in c:
        s += f"VGG {c['ivgg']} V; {'typical' if c['isp'] == 'typ' else 'datasheet-minimum'} module; "
    else:
        s += f"VDD exponent n {c['in']}; hand-match extra loss {c['imatch']} dB; "
    s += f"output loss {c['iloss']} dB (copper term +{(c['iloss'] - LOSS_RELAY_DB) * copper_db_per_db(tc):.3f} dB)"
    if tcase_c is not None:
        s += f"; PA case {tcase_c:.1f} C at 6.4 V"
    return s


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
    prov = run_ltspice(deck, out, timeout=3000)   # about 10 min for 11664 or 13122 corners when the lock is free
    raw = RawRead(str(out / f"power_{fin}.raw"))
    nst = len(raw.get_steps())
    verdict(key, "check: one .raw step per corner", nst == len(corners), "check", f"{nst} steps, {len(corners)} corners")
    assert nst == len(corners), (nst, len(corners))
    vp = np.abs(raw.get_trace(raw.get_trace_names()[0]).get_wave(0))
    S = np.array([raw.get_trace("V(psma)").get_wave(i) for i in range(nst)])
    M = np.array([raw.get_trace("V(pmod)").get_wave(i) for i in range(nst)])
    D = np.array([raw.get_trace("V(d)").get_wave(i) for i in range(nst)])
    TCW = np.array([raw.get_trace("V(tc)").get_wave(i) for i in range(nst)])
    i64 = int(np.argmin(np.abs(vp - 6.4)))
    i84 = int(np.argmin(np.abs(vp - 8.4)))
    tck = np.array([c["itc"] for c in corners])
    # check: the case temperature LTspice solved equals the thermal law recomputed from its own output (key-down cases)
    dev = 0.0
    for i, c in enumerate(corners):
        tc = tc_by_key(c["itc"])
        if tc[4] is None:
            pinw = 10 ** ((c["ipin"] - 30) / 10) if fin == "a5" else c["ipin"]
            want = tc[2] + RTH_CA[fin] * (M[i, i64] * (1 / c["ieta"] - 1) + pinw)
            dev = max(dev, abs(want - TCW[i, i64]))
    verdict(key, "check: PA case temperature solved by LTspice equals the thermal law within 0.01 K", dev <= 0.01, "check",
            f"largest difference {dev:.2e} K at 6.4 V")
    if fin == "a5":
        nomd = dict(irf=0.35, ieta=0.60, ipin=pins[1], ifr=146e6, ivgg=A5_VGG_NOM, isp="typ", iloss=LOSS_DB[1])
        typ = np.array([c["isp"] == "typ" for c in corners])
        design = np.array([c["ivgg"] in A5_VGG_DESIGN for c in corners])
    else:
        nomd = dict(irf=0.35, ieta=0.67, ipin=pins[1], ifr=146e6, **{"in": 2.0}, imatch=0.25, iloss=LOSS_DB[1])
        typ = np.ones(len(corners), bool)
        design = np.ones(len(corners), bool)
    lev = np.array([c["irf"] <= 0.35 for c in corners])   # C2 lever: feed at most 0.35 ohm at 25 C part temperature
    if fin == "a5":
        lev = lev & np.array([c["ivgg"] == A5_VGG_C3 for c in corners])   # C3 lever: VGG 3.30 V at the 6.4 V end
    med = np.array([c["iloss"] <= LOSS_LPF_MEDIAN_DB + 1e-9 for c in corners])   # LPF at most its r13 median
    # every design lever at its best at once (feed 0.26 ohm, output loss 0.5 dB, and VGG 3.46 V for A5 or no extra
    # match loss for A4): what no design choice in this note's ranges can beat, with the typical PA
    stack = np.array([c["irf"] == RFEED[0] and c["iloss"] == LOSS_DB[0] for c in corners])
    stack &= np.array([(c["ivgg"] == A5_VGG_MAX_DESIGN) if fin == "a5" else (c["imatch"] == A4_LMATCH[0]) for c in corners])

    def idx_of(mask, col, fn):
        ii = np.where(mask)[0]
        return int(ii[fn(S[ii, col])])

    by_tc = {}
    for tc in TC_CASES:
        k = tc[0]
        m = tck == k
        inom = next(i for i, c in enumerate(corners) if c["itc"] == k and all(c[a] == b for a, b in nomd.items()))
        ilo = idx_of(m & typ & design, i64, np.argmin)
        ilom = idx_of(m & typ & design & med, i64, np.argmin)
        ihi = idx_of(m & design, i64, np.argmax)
        ilev = idx_of(m & typ & lev, i64, np.argmin)
        ilevm = idx_of(m & typ & lev & med, i64, np.argmin)
        ist = idx_of(m & typ & stack, i64, np.argmin)
        lo_curve = S[m & typ & design].min(axis=0)
        lom_curve = S[m & typ & design & med].min(axis=0)
        d = {"label": tc[1], "ambient_c": tc[2], "state": tc[3], "pa_case_fixed_c": tc[4], "pa_coef_db_per_k": tc[5],
             "no_gain_below_25c": tc[6], "copper_db_per_db": copper_db_per_db(tc),
             "feed_ohm": [feed_at(k, lv) for lv in range(len(RFEED))],
             "at_6v4": {"sma_nominal_w": float(S[inom, i64]), "sma_low_typ_w": float(S[ilo, i64]),
                        "sma_low_typ_lpfmed_w": float(S[ilom, i64]),
                        "sma_high_w": float(S[ihi, i64]), "sma_low_typ_levers_w": float(S[ilev, i64]),
                        "sma_low_typ_levers_lpfmed_w": float(S[ilevm, i64]),
                        "sma_low_typ_stack_w": float(S[ist, i64]),
                        "drain_nominal_v": float(D[inom, i64]), "drain_low_v": float(D[m, i64].min()),
                        "pa_case_nominal_c": float(TCW[inom, i64]), "pa_case_levers_c": float(TCW[ilev, i64]),
                        "pa_case_levers_lpfmed_c": float(TCW[ilevm, i64]), "pa_case_max_c": float(TCW[m, i64].max()),
                        "pa_case_min_c": float(TCW[m, i64].min())},
             "at_8v4": {"sma_nominal_w": float(S[inom, i84]), "module_nominal_w": float(M[inom, i84]),
                        "module_high_w": float(M[m & design, i84].max()), "sma_high_w": float(S[m & design, i84].max()),
                        "pa_case_high_c": float(TCW[m & design, i84].max())},
             "corner_nominal": corners[inom], "corner_low_typ_6v4": corners[ilo], "corner_high_6v4": corners[ihi],
             "corner_low_typ_lpfmed_6v4": corners[ilom],
             "corner_low_typ_levers_6v4": corners[ilev], "corner_low_typ_levers_lpfmed_6v4": corners[ilevm],
             "corner_low_typ_stack_6v4": corners[ist],
             "sma_low_typ_curve_w": lo_curve.tolist(), "sma_low_typ_lpfmed_curve_w": lom_curve.tolist(),
             "sma_nominal_curve_w": S[inom].tolist(),
             "pack_v_low_typ_reaches_3v97": round(float(vp[np.argmax(lo_curve >= REQ012_LO)]), 2) if (lo_curve >= REQ012_LO).any() else None,
             "pack_v_low_typ_lpfmed_reaches_3v97": round(float(vp[np.argmax(lom_curve >= REQ012_LO)]), 2) if (lom_curve >= REQ012_LO).any() else None,
             "pack_v_nominal_reaches_3v97": round(float(vp[np.argmax(S[inom] >= REQ012_LO)]), 2) if (S[inom] >= REQ012_LO).any() else None,
             "pack_v_nominal_reaches_5w": round(float(vp[np.argmax(S[inom] >= REQ012_NOM)]), 2) if (S[inom] >= REQ012_NOM).any() else None,
             "pass_low_typ_ge_3v97_over_range": bool(lo_curve.min() >= REQ012_LO),
             "pass_low_typ_levers_ge_3v97_at_6v4": bool(S[ilev, i64] >= REQ012_LO),
             "pass_low_typ_levers_lpfmed_ge_3v97_at_6v4": bool(S[ilevm, i64] >= REQ012_LO)}
        x = d["at_6v4"]
        for nm, w in (("margin_low_typ_levers_db", x["sma_low_typ_levers_w"]),
                      ("margin_low_typ_levers_lpfmed_db", x["sma_low_typ_levers_lpfmed_w"]),
                      ("margin_low_typ_db", x["sma_low_typ_w"]), ("margin_low_typ_lpfmed_db", x["sma_low_typ_lpfmed_w"]),
                      ("margin_nominal_db", x["sma_nominal_w"]), ("margin_stack_db", x["sma_low_typ_stack_w"])):
            x[nm] = float(10 * np.log10(w / REQ012_LO))
        if fin == "a5":
            mm = m & ~typ & design
            ilm = idx_of(mm, i64, np.argmin)
            ilml = idx_of(m & ~typ & lev, i64, np.argmin)
            ilmlm = idx_of(m & ~typ & lev & med, i64, np.argmin)
            lo_min_curve = S[mm].min(axis=0)
            d["sma_low_minmodule_lpfmed_curve_w"] = S[mm & med].min(axis=0).tolist()
            x["sma_low_minmodule_w"] = float(S[ilm, i64])
            x["sma_low_minmodule_levers_w"] = float(S[ilml, i64])
            x["sma_low_minmodule_levers_lpfmed_w"] = float(S[ilmlm, i64])
            d["corner_low_minmodule_levers_6v4"] = corners[ilml]
            d["corner_low_minmodule_levers_lpfmed_6v4"] = corners[ilmlm]
            d["sma_low_minmodule_curve_w"] = lo_min_curve.tolist()
            d["pack_v_low_minmodule_reaches_3v97"] = round(float(vp[np.argmax(lo_min_curve >= REQ012_LO)]), 2) if (lo_min_curve >= REQ012_LO).any() else None
            mh = M[m & design].max(axis=0)
            d["module_high_curve_w"] = mh.tolist()
            d["module_high_gt_8w_at"] = round(float(vp[np.argmax(mh > A5_MOD_STAB_W)]), 2) if (mh > A5_MOD_STAB_W).any() else None
            d["module_high_gt_10w_at"] = round(float(vp[np.argmax(mh > A5_MOD_MAX_W)]), 2) if (mh > A5_MOD_MAX_W).any() else None
        else:
            d["at_8v4"]["sma_low_w"] = float(lo_curve[i84])
        by_tc[k] = d
    tref = by_tc[TC_REF]
    low_cases = [k for k in by_tc if k != "coldhi"]   # the low bound takes the key-down cases (and the 25 C soak row)
    # sensitivity at 6.4 V in the reference 25 C key-down case: for each input, the dB spread across its values,
    # averaged over the other corners (as-designed corners only for A5: the C3 VGG level is a lever, not a tolerance)
    sens = {}
    dimkeys = [k for k in corners[0] if k not in ("itc", "rf_ohm")]
    iref = [i for i, c in enumerate(corners) if c["itc"] == TC_REF and design[i]]
    for dk in dimkeys:
        groups = {}
        for i in iref:
            other = tuple(corners[i][o] for o in dimkeys if o != dk)
            groups.setdefault(other, []).append(10 * np.log10(S[i, i64]))
        sens[dk] = float(np.mean([max(g) - min(g) for g in groups.values() if len(g) > 1]))
    groups = {}
    for i, c in enumerate(corners):
        if c["itc"] in low_cases and design[i]:
            groups.setdefault(tuple(c[o] for o in dimkeys), []).append(10 * np.log10(S[i, i64]))
    sens["temperature (the low-bound cases)"] = float(np.mean([max(g) - min(g) for g in groups.values()]))
    kd_cases = [k for k in low_cases if tc_by_key(k)[3] == "kd"]
    res = {"run": RUNS[key], "revision": REVISION, "finalist": fin.upper(), "ltspice": prov, "n_corners": len(corners),
           "run_label": RUN_LABEL[key], "rth_ca_k_per_w": RTH_CA[fin], "loss_db": LOSS_DB,
           "temperature_cases": [{"key": c[0], "label": c[1], "ambient_c": c[2], "state": c[3], "pa_case_fixed_c": c[4],
                                  "pa_coef_db_per_k": c[5], "no_gain_below_25c": c[6]} for c in TC_CASES],
           "reference_case": TC_REF,
           "pin_corners_from": RUNS[drive_key] + (" with the select-on-test pad residual (s1 method)" if pins_override else ""),
           "pin_corners": pins, "vpack": vp.tolist(), "by_tc": by_tc, "sensitivity_6v4_ref_db": sens,
           # reference-case keys (25 C ambient, steady key-down, -0.005 dB/K)
           "sma_nominal_w": tref["sma_nominal_curve_w"], "sma_low_typ_w": tref["sma_low_typ_curve_w"],
           "at_6v4": tref["at_6v4"], "at_8v4": tref["at_8v4"], "nominal_corner": tref["corner_nominal"],
           "worst_low_corner": tref["corner_low_typ_6v4"],
           "pass_low_typ_ge_3v97_over_range_25c_kd": bool(by_tc["t25a"]["pass_low_typ_ge_3v97_over_range"]
                                                         and by_tc["t25b"]["pass_low_typ_ge_3v97_over_range"]),
           "pass_low_typ_ge_3v97_all_temperatures": bool(all(by_tc[k]["pass_low_typ_ge_3v97_over_range"] for k in kd_cases)),
           "worst_low_typ_6v4_all_temperatures_w": float(min(by_tc[k]["at_6v4"]["sma_low_typ_w"] for k in kd_cases)),
           "worst_nominal_6v4_all_temperatures_w": float(min(by_tc[k]["at_6v4"]["sma_nominal_w"] for k in kd_cases))}
    rk = key
    verdict(rk, f"{fin.upper()} lowest corner at least 3.97 W from 6.4 to 8.4 V, 25 C key-down",
            res["pass_low_typ_ge_3v97_over_range_25c_kd"])
    verdict(rk, f"{fin.upper()} lowest corner at least 3.97 W from 6.4 to 8.4 V, every key-down case",
            res["pass_low_typ_ge_3v97_all_temperatures"])
    verdict(rk, f"{fin.upper()} nominal corner at least 3.97 W at 6.4 V, every key-down case",
            bool(all(by_tc[k]["at_6v4"]["sma_nominal_w"] >= REQ012_LO for k in kd_cases)))
    if fin == "a5":
        res.update({
            "pass_levers_ge_3v97_at_6v4_all_temperatures": bool(all(by_tc[k]["pass_low_typ_levers_ge_3v97_at_6v4"] for k in kd_cases)),
            "pass_levers_lpfmed_ge_3v97_at_6v4_all_temperatures": bool(all(by_tc[k]["pass_low_typ_levers_lpfmed_ge_3v97_at_6v4"] for k in kd_cases)),
            "pass_levers_lpfmed_ge_3v97_at_6v4_25c_kd": bool(by_tc["t25a"]["pass_low_typ_levers_lpfmed_ge_3v97_at_6v4"]
                                                            and by_tc["t25b"]["pass_low_typ_levers_lpfmed_ge_3v97_at_6v4"]),
            "worst_levers_6v4_all_temperatures_w": float(min(by_tc[k]["at_6v4"]["sma_low_typ_levers_w"] for k in kd_cases)),
            "worst_levers_lpfmed_6v4_all_temperatures_w": float(min(by_tc[k]["at_6v4"]["sma_low_typ_levers_lpfmed_w"] for k in kd_cases)),
            "sma_low_minmodule_w": tref["sma_low_minmodule_curve_w"],
            "module_high_8v4_all_temperatures_w": float(max(by_tc[k]["at_8v4"]["module_high_w"] for k in by_tc))})
        verdict(rk, "A5 lowest with C2 and C3, LPF at its median, at least 3.97 W at 6.4 V, 25 C key-down",
                res["pass_levers_lpfmed_ge_3v97_at_6v4_25c_kd"])
        verdict(rk, "A5 lowest with C2 and C3, LPF at its median, at least 3.97 W at 6.4 V, every key-down case",
                res["pass_levers_lpfmed_ge_3v97_at_6v4_all_temperatures"])
        verdict(rk, "A5 lowest with C2 and C3, LPF at its worst case, at least 3.97 W at 6.4 V, every key-down case",
                res["pass_levers_ge_3v97_at_6v4_all_temperatures"])
        verdict(rk, "A5 open loop at 8.4 V: module output at most 8 W (stability conditions), every case",
                res["module_high_8v4_all_temperatures_w"] <= A5_MOD_STAB_W)
        verdict(rk, "A5 open loop at 8.4 V: module output at most 10 W (maximum rating), every case",
                res["module_high_8v4_all_temperatures_w"] <= A5_MOD_MAX_W)
    res["verdicts"] = VERDICTS.get(rk, {})
    (out / "result.json").write_text(json.dumps(res, indent=1, default=str))
    plot_power(out, fin, res)
    write_power_md(out, fin, res)
    copy_inputs(out, [deck])
    print(key, json.dumps({k: (v["at_6v4"], v["at_8v4"]) for k, v in by_tc.items()}, default=str)[:3000])
    return res


TC_COL = {"t25soak": "#7fa7cf", "t25a": "#0f5e9c", "t25b": "#0a3d66", "cold0": "#2a78d6", "coldhi": "#8fb8ea",
          "hot45a": "#eb6834", "hot45b": "#b3401a", "hot100a": "#c2185b", "hot100b": "#7a0e3a"}


def plot_power(out: Path, fin: str, r: dict):
    vp = np.array(r["vpack"])
    c = COL[fin]
    tref = r["by_tc"][TC_REF]
    lab_run = r["run_label"]
    # plot 1: reference-case nominal and the lowest corner of every case versus pack voltage
    fig, ax = plt.subplots(figsize=(9.0, 7.2))
    ax.plot(vp, tref["sma_nominal_curve_w"], color=c, lw=2.2, label=f"nominal corner, {tref['label']}")
    for k, d in r["by_tc"].items():
        if k == "coldhi":
            continue
        ax.plot(vp, d["sma_low_typ_lpfmed_curve_w"], color=TC_COL[k], lw=1.5 if k == TC_REF else 1.1,
                ls="-" if k == TC_REF else "--", label=f"lowest{', typical module' if fin == 'a5' else ''}, LPF median: {d['label']}")
    ax.plot(vp, tref["sma_low_typ_curve_w"], color=INK, lw=1.3, ls=(0, (2, 2)),
            label=f"lowest{', typical module' if fin == 'a5' else ''}, LPF worst case: {tref['label']}")
    if fin == "a5":
        ax.plot(vp, tref["sma_low_minmodule_lpfmed_curve_w"], color=COL["aux"], lw=1.6, ls="-.",
                label=f"datasheet-minimum module, lowest corner, LPF median: {tref['label']}")
        ax.plot(vp, r["by_tc"]["coldhi"]["module_high_curve_w"], color=INK2, lw=1.2, ls=(0, (1, 1)),
                label="module output, highest corner, -10 C start of key-down, +0.53 dB, ALC open (VGG 3.46 V)")
        ax.axhline(A5_MOD_STAB_W, color=INK2, lw=1, ls=":", label="8 W: module stability guarantee (module output)")
        ax.axhline(A5_MOD_MAX_W, color=INK2, lw=1.6, ls=":", label="10 W: module maximum rating (module output)")
    add_req_lines(ax)
    ax.set_xlim(*PACK)
    ax.set_ylim(0, 12.5 if fin == "a5" else 9)
    ax.set_xlabel("Pack voltage, read in receive (V)")
    ax.set_ylabel("Available power, ALC at its top (W)")
    ax.set_title(f"{fin.upper()}, {lab_run}: power at the SMA versus pack voltage\n"
                 f"(LTspice, revision {REVISION}, {r['n_corners']} corners; key-down sag, PA self-heating, output LPF "
                 f"{LOSS_DB[0]} / {LOSS_DB[1]} / {LOSS_DB[2]} dB with relay)", fontsize=9.5)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.1), ncol=2, fontsize=6.8)
    fig.tight_layout()
    fig.savefig(out / f"power_{fin}_sma.png", dpi=150)
    plt.close(fig)
    # plot 2: at 6.4 V per temperature case
    fig, ax = plt.subplots(figsize=(10.0, 6.4))
    keys = [k for k in r["by_tc"] if k != "coldhi"]
    x = np.arange(len(keys))
    series = [("sma_nominal_w", f"nominal corner (VGG {A5_VGG_NOM} V, LPF median)" if fin == "a5" else "nominal corner (LPF median)", c, "o"),
              ("sma_low_typ_lpfmed_w", "lowest corner" + (", typical module, as designed" if fin == "a5" else "") + ", LPF at most its median", INK2, "^"),
              ("sma_low_typ_w", "lowest corner" + (", typical module, as designed" if fin == "a5" else "") + ", LPF worst case", INK, "v")]
    if fin == "a5":
        series += [("sma_low_typ_levers_lpfmed_w", f"lowest, typical module, C2 and C3 (feed at most 0.35 ohm at 25 C, VGG {A5_VGG_C3} V), LPF at most its median", COL["ok"], "s"),
                   ("sma_low_typ_levers_w", "same, LPF worst case", "#0e7a54", "P"),
                   ("sma_low_minmodule_levers_lpfmed_w", "lowest, datasheet-minimum module, C2 and C3, LPF at most its median", COL["aux"], "D")]
    series += [("sma_low_typ_stack_w", "lowest" + (", typical module" if fin == "a5" else "") + ", every design lever at its best: feed 0.26 ohm, output loss 0.5 dB, "
                + ("VGG 3.46 V" if fin == "a5" else "no extra match loss"), "#b3401a", "*")]
    allv = []
    for j, (kk, lab, col, mk) in enumerate(series):
        ys = [r["by_tc"][k]["at_6v4"][kk] for k in keys]
        allv += ys
        ax.plot(x + (j - (len(series) - 1) / 2) * 0.1, ys, mk, color=col, ms=6.5, label=lab, ls="none")
    add_req_lines(ax)
    ax.set_xticks(x)
    ax.set_xticklabels([TC_SHORT[k] + f"\ncase {r['by_tc'][k]['at_6v4']['pa_case_levers_lpfmed_c' if fin == 'a5' else 'pa_case_nominal_c']:.0f} C"
                        for k in keys], fontsize=6.8)
    ax.set_ylim(np.floor((min(allv) - 0.25) * 2) / 2, 6.6)
    ax.set_ylabel("Power at the SMA at 6.4 V pack (W)")
    ax.set_title(f"{fin.upper()}, {lab_run}: power at the SMA at the 6.4 V pack end per temperature case (revision {REVISION})\n"
                 f"PA coefficient -0.005 or -0.015 dB/K above a 25 C case (estimate, no vendor data); tick label: PA case at "
                 f"{'the C2 and C3 corner' if fin == 'a5' else 'the nominal corner'}", fontsize=9)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.24), ncol=1, fontsize=7.2)
    fig.tight_layout()
    fig.savefig(out / f"power_{fin}_temperature.png", dpi=150)
    plt.close(fig)


SENS_NAMES = {"irf": "drain feed", "ieta": "efficiency", "ipin": "drive", "ifr": "frequency", "ivgg": "VGG clamp",
              "isp": "module spread (typical against datasheet minimum)", "iloss": "output loss", "in": "VDD exponent",
              "imatch": "hand-match loss"}


def write_power_md(out, fin, r):
    tref = r["by_tc"][TC_REF]
    a, b = tref["at_6v4"], tref["at_8v4"]
    vd = r["verdicts"]
    L = [f"# {r['run']}: {fin.upper()} output power at the SMA versus pack voltage (REQ-SYS-012), revision {REVISION}", "",
         f"Drive: {r['run_label']}. Every figure is an estimate built on graph-read typical vendor curves and estimated feed, "
         "efficiency, loss and thermal terms (analysis record section 3); the corners bound the stated input ranges, not the "
         "unknowns listed as limitations.", "",
         f"Thermal state (revision 2, finding-9): the key-down cases are steady key-down at their ambient, with the PA case solved "
         f"from the dissipation (Rth case to ambient {RTH_CA[fin]} K/W, WP-PDR-28) and the feed parts and the copper term at "
         f"their key-down temperatures; the soak rows are the start of a key-down. Output loss {LOSS_DB} dB (LPF revision 2 "
         f"run r13 plus the relay: allocation, median, worst case). Reference case for the \"25 C\" figures: {tref['label']}.", "",
         "Verdicts:"]
    for n_, v in vd.items():
        L.append(f"- {n_}: **{'PASS' if v['pass'] else 'FAIL'}**" + (f" ({v['detail']})" if v.get("detail") else "") + ".")
    L += ["", "| Temperature case | Feed low / C2 / high (ohm) | PA case at 6.4 V, nominal / " + ("C2 and C3" if fin == "a5" else "hottest") +
          " corner (C) | Nominal at 6.4 V (W) | Lowest, LPF median (W) | Lowest, LPF worst (W) | "
          + ("With C2 and C3, LPF median (W; margin dB) | With C2 and C3, LPF worst (W; margin dB) | Datasheet-minimum module, C2 and C3, LPF median (W) | " if fin == "a5" else "")
          + "Every design lever at its best (W; margin dB) | Highest at 6.4 V (W) | Lowest (LPF median) reaches 3.97 W from (V) | Output at 8.4 V, highest (W) |",
          "|---|---|---|---|---|---|" + ("---|---|---|" if fin == "a5" else "") + "---|---|---|---|"]
    for k, d in r["by_tc"].items():
        x = d["at_6v4"]
        tcs = f"{x['pa_case_nominal_c']:.1f} / {x['pa_case_levers_lpfmed_c'] if fin == 'a5' else x['pa_case_max_c']:.1f}"
        row = (f"| {d['label']} | {' / '.join(f'{v:.3f}' for v in d['feed_ohm'])} | {tcs} | {x['sma_nominal_w']:.2f} | "
               f"{x['sma_low_typ_lpfmed_w']:.2f} | {x['sma_low_typ_w']:.2f} | ")
        if fin == "a5":
            row += (f"{x['sma_low_typ_levers_lpfmed_w']:.2f} ({x['margin_low_typ_levers_lpfmed_db']:+.2f}) | "
                    f"{x['sma_low_typ_levers_w']:.2f} ({x['margin_low_typ_levers_db']:+.2f}) | {x['sma_low_minmodule_levers_lpfmed_w']:.2f} | ")
        reach = d["pack_v_low_typ_lpfmed_reaches_3v97"]
        row += (f"{x['sma_low_typ_stack_w']:.2f} ({x['margin_stack_db']:+.2f}) | {x['sma_high_w']:.2f} | "
                f"{reach if reach is not None else 'above 8.4'} | {d['at_8v4']['module_high_w']:.2f} |")
        L.append(row)
    L += ["", f"Corners at 6.4 V in the reference case, {tref['label']} (full parameter sets):",
          f"- Nominal ({a['sma_nominal_w']:.2f} W): {pstr(tref['corner_nominal'], a['pa_case_nominal_c'])}.",
          f"- Lowest, LPF worst case ({a['sma_low_typ_w']:.2f} W): {pstr(tref['corner_low_typ_6v4'])}.",
          f"- Lowest, LPF at most its median ({a['sma_low_typ_lpfmed_w']:.2f} W): {pstr(tref['corner_low_typ_lpfmed_6v4'])}.",
          f"- Highest ({a['sma_high_w']:.2f} W): {pstr(tref['corner_high_6v4'])}.",
          f"- Lowest with every design lever at its best ({a['sma_low_typ_stack_w']:.2f} W): {pstr(tref['corner_low_typ_stack_6v4'])}."]
    if fin == "a5":
        L += [f"- Lowest with the C2 and C3 levers, LPF at most its median ({a['sma_low_typ_levers_lpfmed_w']:.2f} W): "
              f"{pstr(tref['corner_low_typ_levers_lpfmed_6v4'], a['pa_case_levers_lpfmed_c'])}.",
              f"- Lowest with the C2 and C3 levers, LPF worst case ({a['sma_low_typ_levers_w']:.2f} W): "
              f"{pstr(tref['corner_low_typ_levers_6v4'], a['pa_case_levers_c'])}.",
              f"- Datasheet-minimum module, lowest with the levers, LPF at most its median ({a['sma_low_minmodule_levers_lpfmed_w']:.2f} W): "
              f"{pstr(tref['corner_low_minmodule_levers_lpfmed_6v4'])}."]
    kd_cases = [k for k in r["by_tc"] if tc_by_key(k)[3] == "kd"]
    fld = "sma_low_typ_levers_lpfmed_w" if fin == "a5" else "sma_low_typ_lpfmed_w"
    worst_k = min(kd_cases, key=lambda k: r["by_tc"][k]["at_6v4"][fld])
    wd = r["by_tc"][worst_k]
    wc = wd["corner_low_typ_levers_lpfmed_6v4" if fin == "a5" else "corner_low_typ_lpfmed_6v4"]
    L += [f"- Worst key-down case ({wd['label']}), lowest{' with the levers' if fin == 'a5' else ''}, LPF at most its median "
          f"({wd['at_6v4'][fld]:.2f} W): {pstr(wc)}.",
          "", f"- Drain voltage at 6.4 V, reference case: nominal {a['drain_nominal_v']:.2f} V, lowest {a['drain_low_v']:.2f} V (key-down sag).",
          f"- {'Module' if fin == 'a5' else 'Device'} output at 8.4 V, reference case: nominal {b['module_nominal_w']:.2f} W, highest corner "
          f"{b['module_high_w']:.2f} W (ALC open; the ALC must hold 5 W).",
          f"- Nominal corner reaches 3.97 W from {tref['pack_v_nominal_reaches_3v97']} V and 5.0 W from {tref['pack_v_nominal_reaches_5w']} V "
          f"in the reference case.",
          f"- Drive corners used (from {r['pin_corners_from']}): {r['pin_corners']}.",
          "- Sensitivity at 6.4 V in the reference case (dB spread across each input's values, averaged over the other corners; "
          "the temperature row over the low-bound cases): " + "; ".join(
              f"{SENS_NAMES.get(k, k)} {v:.2f}" for k, v in sorted(r["sensitivity_6v4_ref_db"].items(), key=lambda kv: -kv[1])) + "."]
    if fin == "a5":
        c = r["by_tc"]["coldhi"]
        L += [f"- Open loop at 8.4 V (VGG at the clamp maximum {A5_VGG_MAX_DESIGN} V), highest corner: {b['module_high_w']:.2f} W in the "
              f"reference case, {c['at_8v4']['module_high_w']:.2f} W at the -10 C start of key-down with the +0.53 dB estimate; above 8 W "
              f"(stability conditions) from {tref['module_high_gt_8w_at']} V (reference) and {c['module_high_gt_8w_at']} V (-10 C); "
              f"above 10 W (maximum rating) from {tref['module_high_gt_10w_at'] or 'nowhere below 8.4'} V (reference) and "
              f"{c['module_high_gt_10w_at'] or 'nowhere below 8.4'} V (-10 C) (input to WP-PDR-22)."]
    L += ["", f"Plots: `power_{fin}_sma.png` (versus pack voltage, with the lowest corner per temperature case), "
          f"`power_{fin}_temperature.png` (at 6.4 V per temperature case, against 3.97 W). Deck `power_{fin}.cir`; LTspice log "
          f"and raw beside it; numbers in `result.json`.", ""]
    (out / "result.md").write_text("\n".join(L))


# ---------------------------------------------------------------- s1: summary plots and verdicts
E24 = [1.0, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2.0, 2.2, 2.4, 2.7, 3.0, 3.3, 3.6, 3.9, 4.3, 4.7, 5.1, 5.6, 6.2, 6.8, 7.5, 8.2, 9.1]


def e24_pads_all(lo_db: float = 3.0, hi_db: float = 30.0) -> list[dict]:
    """Every symmetric E24 1 % pi pad (shunt, series, shunt; 10 ohm to 2 kohm) with at least 25 dB return loss."""
    vals = [round(m * 10 ** e, 1) for e in (1, 2, 3) for m in E24 if 10 <= m * 10 ** e <= 2000]
    out = []
    for sh in vals:
        for se in vals:
            loss = float(pad_loss_db(sh, se, sh))
            if not lo_db <= loss <= hi_db:
                continue
            zin = 1 / (1 / sh + 1 / (se + 1 / (1 / sh + 1 / 50.0)))
            rl = min(60.0, -20 * np.log10(abs((zin - 50) / (zin + 50)) + 1e-12))   # 60 dB shown as "at least 60"
            if rl >= 25:
                out.append(dict(shunt=sh, series=se, loss_db=round(loss, 2), rl_db=round(float(rl), 1)))
    return sorted(out, key=lambda d: d["loss_db"])


def e24_pad_set(need_lo: float, need_hi: float, max_gap: float = SOT_MAX_GAP_DB) -> list[dict]:
    """A set of E24 pads covering the needed losses with adjacent losses at most max_gap apart (revision 2,
    finding-4): start at the largest pad not above the lowest need, then take each time the largest pad within
    max_gap of the last one (ties: the better return loss), until a pad reaches the highest need. Every needed loss
    then lies within half the set's largest gap of a pad."""
    pads = e24_pads_all()
    first = max((p for p in pads if p["loss_db"] <= need_lo), key=lambda p: (p["loss_db"], p["rl_db"]))
    sel = [first]
    while sel[-1]["loss_db"] < need_hi:
        cand = [p for p in pads if sel[-1]["loss_db"] < p["loss_db"] <= sel[-1]["loss_db"] + max_gap]
        sel.append(max(cand, key=lambda p: (p["loss_db"], p["rl_db"])))
    return sel


def sot_band(fspan: float, step_half: float, meas: float, drift: float = SOT_DRIFT_DB) -> dict:
    half = fspan / 2 + step_half + meas + drift
    mx, mn = SOT_TARGET_MW * 10 ** (half / 10), SOT_TARGET_MW * 10 ** (-half / 10)
    return {"meas_db": meas, "half_width_db": half, "min_mw": mn, "max_mw": mx,
            "overdrive_margin_db": float(10 * np.log10(A5_PIN_MAX_MW / mx)),
            "underdrive_margin_db": float(10 * np.log10(mn / A5_PIN_MIN_MW)),
            "pass": bool(mn >= A5_PIN_MIN_MW and mx <= A5_PIN_MAX_MW)}


def sot_residual(dkey: str = "d2") -> dict:
    """A5 select-on-test pad: per built unit (source R, gain, P1dB set, Si5351 case, coax length) only frequency,
    the pad step, the level reading and drift vary in service; the pad is chosen at build with the unit's own coax
    in place and read at 146 MHz."""
    rows5 = json.loads((rundir(dkey) / "corners.json").read_text())
    pinpad = dkey == "d5"
    pad_now = float(pad_loss_db(*PADS["a5_in_rf" if pinpad else "a5_in"]))
    units = {}
    for r in rows5:
        units.setdefault((r["rsrc"], r["gain"], r["p1db"], r["src"], r["coax_m"]), {})[r["freq"]] = r["pin_pa_dbm"]
    fspan = max(max(v.values()) - min(v.values()) for v in units.values())
    tgt = float(dbm(SOT_TARGET_MW * 1e-3))
    need = [pad_now + (v[146e6] - tgt) for v in units.values()]
    pads = e24_pad_set(min(need), max(need))
    gaps = np.diff([p["loss_db"] for p in pads])
    step_half = float(gaps.max() / 2)
    # the in-service residual per unit: the chosen pad is the one nearest the need (worst unit: half the largest gap)
    resid = [min(abs(n_ - p["loss_db"]) for p in pads) for n_ in need]
    band = sot_band(fspan, step_half, SOT_MEAS_DB)
    rss = float(np.sqrt((fspan / 2) ** 2 + step_half ** 2 + SOT_MEAS_DB ** 2 + SOT_DRIFT_DB ** 2))
    avail = float(10 * np.log10(A5_PIN_MAX_MW / SOT_TARGET_MW))
    sot = {"drive_run": RUNS[dkey], "pinpad_option": pinpad, "freq_span_within_unit_db": fspan,
           "pad_set_max_gap_db": float(gaps.max()), "step_half_db": step_half, "largest_residual_in_units_db": float(max(resid)),
           "meas_db": SOT_MEAS_DB, "drift_db": SOT_DRIFT_DB, "half_width_db": band["half_width_db"], "half_width_rss_db": rss,
           "target_mw": SOT_TARGET_MW, "min_mw": band["min_mw"], "max_mw": band["max_mw"],
           "overdrive_margin_db": band["overdrive_margin_db"], "underdrive_margin_db": band["underdrive_margin_db"],
           "overdrive_margin_rss_db": avail - rss,
           "reading_break_even_db": float(avail - (fspan / 2 + step_half + SOT_DRIFT_DB)),
           "sensitivity": [sot_band(fspan, step_half, m) for m in SOT_MEAS_SENS_DB],
           "pad_as_built_db": pad_now, "pad_needed_db": [float(min(need)), float(max(need))], "pads": pads,
           "pass": band["pass"]}
    return sot


def run_s1():
    out = rundir("s1")
    ld = lambda k: json.loads((rundir(k) / "result.json").read_text())
    d5, d4, dq, dop = ld("d2"), ld("d3"), ld("d4"), ld("d5")
    p5, p4, p6 = ld("p1"), ld("p2"), ld("p3")
    vp = np.array(p5["vpack"])
    sot = sot_residual("d2")
    sot_opt = sot_residual("d5")
    verdict("s1", f"A5 select-on-test drive 10 to 30 mW in service, reading allocation +/-{SOT_MEAS_DB} dB", sot["pass"],
            detail=f"{sot['min_mw']:.1f} to {sot['max_mw']:.1f} mW, overdrive margin {sot['overdrive_margin_db']:+.2f} dB")
    tsa = next(s for s in sot["sensitivity"] if abs(s["meas_db"] - 2.0) < 1e-9)
    verdict("s1", "A5 select-on-test drive 10 to 30 mW with a tinySA Ultra reading alone (+/-2 dB published)", tsa["pass"],
            detail=f"overdrive margin {tsa['overdrive_margin_db']:+.2f} dB")
    verdict("s1", f"A5 option d5 select-on-test drive 10 to 30 mW, reading allocation +/-{SOT_MEAS_DB} dB", sot_opt["pass"],
            detail=f"{sot_opt['min_mw']:.1f} to {sot_opt['max_mw']:.1f} mW")
    # ---- Figure 1: Pin at the PA versus pack voltage (regulated rails: flat in pack voltage)
    fig, axs = plt.subplots(1, 2, figsize=(10.4, 5.6))
    for ax, d, fin in ((axs[0], d5, "a5"), (axs[1], d4, "a4")):
        c = COL[fin]
        lo, nomv, hi = d["pin_pa_w"]["min"] * 1e3, d["pin_pa_w"]["nominal"] * 1e3, d["pin_pa_w"]["max"] * 1e3
        ax.fill_between(vp, lo, hi, color=c, alpha=0.18, lw=0, label=f"fixed pad, all corners, coax 5 to 15 cm ({lo:.1f} to {hi:.1f} mW)")
        ax.plot(vp, np.full_like(vp, nomv), color=c, lw=2, label=f"nominal corner, coax 10 cm ({nomv:.1f} mW)")
        clo, chi = d["pin_pa_criterion_corners_w"]["min"] * 1e3, d["pin_pa_criterion_corners_w"]["max"] * 1e3
        ax.plot(vp, np.full_like(vp, clo), color=c, lw=1, ls="--", label=f"TS-012 criterion corners ({clo:.1f} to {chi:.1f} mW)")
        ax.plot(vp, np.full_like(vp, chi), color=c, lw=1, ls="--")
        q = dq["finalists"][fin.upper()]
        ax.plot(vp, np.full_like(vp, q["max_mw_any_length"]), color=INK2, lw=1, ls=(0, (1, 1)),
                label=f"fixed pad, any coax length (d4): {q['min_mw_any_length']:.1f} to {q['max_mw_any_length']:.1f} mW")
        ax.plot(vp, np.full_like(vp, q["min_mw_any_length"]), color=INK2, lw=1, ls=(0, (1, 1)))
        if fin == "a5":
            ax.fill_between(vp, sot["min_mw"], sot["max_mw"], facecolor="none", edgecolor=COL["ok"], hatch="///", lw=0,
                            label=f"select-on-test pad in service, reading +/-{SOT_MEAS_DB} dB, est. ({sot['min_mw']:.1f} to {sot['max_mw']:.1f} mW)")
            ax.axhline(30, color=INK, lw=1.4, label="30 mW: maximum rating, top of the stability window")
            ax.axhline(10, color=INK, lw=1.4, ls="-.", label="10 mW: bottom of the stability window")
            ax.set_ylim(0, 55)
            ax.set_title("A5: power into the RA07M1317M input")
        else:
            ax.axhline(200, color=INK, lw=1.4, label="200 mW: ruggedness-test drive (not a rating)")
            ax.axhline(100, color=INK2, lw=1.1, ls=":", label="100 mW: datasheet Table 8 drive")
            ax.set_ylim(0, 260)
            ax.set_title("A4: power into the AFT05MS004N input")
        ax.set_xlim(*PACK)
        ax.set_xlabel("Pack voltage, read in receive (V)")
        ax.set_ylabel("Fundamental power at the PA input (mW)")
        ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.14), ncol=1, fontsize=7)
    fig.suptitle(f"Drive at the PA input versus pack voltage (revision {REVISION}: coax interface; Si5351 and GVA-84+ on regulated rails)", fontsize=10)
    fig.tight_layout()
    fig.savefig(out / "pin_at_pa_vs_pack.png", dpi=150)
    plt.close(fig)
    # ---- Figure 2: Pout at the SMA versus pack voltage, both finalists, 25 C key-down and the worst key-down case
    fig, ax = plt.subplots(figsize=(7.8, 6.8))
    kd = [t[0] for t in TC_CASES if t[3] == "kd"]
    for p, fin, lab in ((p5, "a5", "A5 (typical module)"), (p4, "a4", "A4")):
        c = COL[fin]
        ref = p["by_tc"][TC_REF]
        env_lo = np.min([p["by_tc"][k]["sma_low_typ_lpfmed_curve_w"] for k in kd], axis=0)
        ax.fill_between(vp, env_lo, ref["sma_low_typ_lpfmed_curve_w"], color=c, alpha=0.15, lw=0,
                        label=f"{lab}: lowest corner, LPF median, 25 C key-down down to the worst key-down case")
        ax.plot(vp, ref["sma_low_typ_lpfmed_curve_w"], color=c, lw=1.2, ls="--", label=f"{lab}: lowest corner, LPF median, 25 C key-down")
        ax.plot(vp, ref["sma_low_typ_curve_w"], color=c, lw=1.0, ls=":", label=f"{lab}: lowest corner, LPF worst case, 25 C key-down")
        ax.plot(vp, ref["sma_nominal_curve_w"], color=c, lw=2, label=f"{lab}: nominal corner, 25 C key-down")
    ax.plot(vp, p6["by_tc"][TC_REF]["sma_low_typ_lpfmed_curve_w"], color=COL["ok"], lw=1.4, ls="-.",
            label="A5 with the select-on-test pad: lowest corner, LPF median, 25 C key-down")
    add_req_lines(ax)
    ax.set_xlim(*PACK)
    ax.set_ylim(0, 10)
    ax.set_xlabel("Pack voltage, read in receive (V)")
    ax.set_ylabel("Available power at the SMA, ALC at its top (W)")
    ax.set_title(f"Power at the SMA versus pack voltage, A4 and A5 (LTspice, revision {REVISION})\n"
                 f"25 C key-down is the -0.005 dB/K case; LPF median {LOSS_DB[1]} dB, worst case {LOSS_DB[2]} dB with relay (estimates)", fontsize=9.2)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.11), ncol=1, fontsize=7)
    fig.tight_layout()
    fig.savefig(out / "pout_at_sma_vs_pack.png", dpi=150)
    plt.close(fig)
    # ---- Closure margin at 6.4 V (A5, C2 and C3 levers) with the terms not carried as corners
    ulo = sum(u[1] for u in CLOSURE_UNC)
    uhi = sum(u[2] for u in CLOSURE_UNC)
    clos = {}
    for run, p in (("p1", p5), ("p3", p6)):
        clos[run] = {}
        for k, d in p["by_tc"].items():
            if k == "coldhi":
                continue
            x = d["at_6v4"]
            clos[run][k] = {"label": d["label"], "pa_case_c": x["pa_case_levers_lpfmed_c"]}
            for tag, fw, fm in (("lpfmed", "sma_low_typ_levers_lpfmed_w", "sma_low_minmodule_levers_lpfmed_w"),
                                ("lpfworst", "sma_low_typ_levers_w", "sma_low_minmodule_levers_w")):
                m = float(10 * np.log10(x[fw] / REQ012_LO))
                clos[run][k][tag] = {"w": x[fw], "margin_db": m, "margin_low_db": m + ulo, "margin_high_db": m + uhi,
                                     "minmodule_margin_db": float(10 * np.log10(x[fm] / REQ012_LO))}
    keys = list(clos["p1"].keys())
    x = np.arange(len(keys))
    fig, axs = plt.subplots(1, 2, figsize=(15.5, 6.8), sharey=True)
    for ax, tag, ttl in ((axs[0], "lpfmed", f"output LPF at its r13 median ({LOSS_DB[1]} dB with the relay)"),
                         (axs[1], "lpfworst", f"output LPF at its r13 worst case ({LOSS_DB[2]} dB with the relay)")):
        for j, (run, col, lab) in enumerate((("p1", COL["a5"], "fixed pad as designed (p1)"), ("p3", COL["ok"], "select-on-test pad (p3)"))):
            ms = np.array([clos[run][k][tag]["margin_db"] for k in keys])
            ax.errorbar(x + (j - 0.5) * 0.2, ms, yerr=[ms - np.array([clos[run][k][tag]["margin_low_db"] for k in keys]),
                                                      np.array([clos[run][k][tag]["margin_high_db"] for k in keys]) - ms],
                        fmt="s", color=col, ms=5.5, capsize=3.5, lw=1.3, label=f"typical module with C2 and C3, {lab}")
        mm = np.array([clos["p1"][k][tag]["minmodule_margin_db"] for k in keys])
        ax.plot(x + 0.3, mm, "D", color=COL["aux"], ms=4.5, label="datasheet-minimum module with C2 and C3 (p1)")
        ax.axhline(0, color=INK, lw=2, ls="--", label="0 dB: REQ-SYS-012 lower bound, 3.97 W at the SMA")
        ax.set_xticks(x)
        ax.set_xticklabels([TC_SHORT[k] + f"\ncase {clos['p1'][k]['pa_case_c']:.0f} C" for k in keys], fontsize=6.5)
        ax.set_title(ttl, fontsize=9)
    h_, l_ = axs[0].get_legend_handles_labels()
    fig.legend(h_, l_, loc="lower center", ncol=2, fontsize=7.5)
    axs[0].set_ylabel("Margin to 3.97 W at 6.4 V pack (dB)")
    fig.suptitle(f"A5 closure margin at the 6.4 V end (revision {REVISION}): lowest corner with C2 (feed at most 0.35 ohm at 25 C) and C3 "
                 f"(VGG {A5_VGG_C3} V)\nerror bars: terms not carried as corners ({ulo:+.2f} / {uhi:+.2f} dB: graph read, LM2940 "
                 "dropout, GVA-84+ gain at 146 MHz); tick label: PA case at the p1 corner, LPF median", fontsize=9.5)
    fig.tight_layout(rect=(0, 0.08, 1, 1))
    fig.savefig(out / "a5_closure_margin.png", dpi=150)
    plt.close(fig)
    # ---- Overdrive margin (A5)
    od = [("fixed pad, coax 5 cm", d5["per_coax"]["0.05"]["overdrive_margin_db"]),
          ("fixed pad, coax 10 cm", d5["per_coax"]["0.10"]["overdrive_margin_db"]),
          ("fixed pad, coax 15 cm", d5["per_coax"]["0.15"]["overdrive_margin_db"]),
          ("fixed pad, any length (d4)", dq["finalists"]["A5"]["overdrive_margin_any_length_db"]),
          ("option: 6 dB at the pin, fixed pad (d5)", dop["overdrive_margin_db"]),
          (f"select-on-test, as designed, reading +/-{SOT_MEAS_DB} dB", sot["overdrive_margin_db"]),
          (f"select-on-test, option d5, reading +/-{SOT_MEAS_DB} dB", sot_opt["overdrive_margin_db"]),
          ("select-on-test, tinySA Ultra alone (+/-2 dB)", tsa["overdrive_margin_db"])]
    fig, ax = plt.subplots(figsize=(10.4, 5.6))
    y = np.arange(len(od))
    vals = np.array([v for _, v in od])
    temp = np.array([DRIVE_TEMP_DB] * 5 + [0.0, 0.0, 0.0])  # SOT half-width already holds the drift term
    ax.barh(y, vals, color=[COL["a4"] if v - t < 0 else COL["ok"] for v, t in zip(vals, temp)], height=0.55)
    ax.errorbar(vals, y, xerr=[temp, np.zeros_like(temp)], fmt="none", ecolor=INK, capsize=3, lw=1)
    for yy, v in zip(y, vals):
        ax.text(1.45, yy, f"{v:+.2f} dB", va="center", ha="right", fontsize=8)
    ax.axvline(0, color=INK, lw=2, label="0 dB: 30 mW, module maximum rating")
    ax.set_yticks(y)
    ax.set_yticklabels([n for n, _ in od], fontsize=7.5)
    ax.invert_yaxis()
    ax.set_xlim(-2.4, 1.5)
    ax.set_xlabel("Overdrive margin: 10 log10(30 mW / highest in-service drive) (dB)")
    ax.set_title(f"A5 overdrive margin against the RA07M1317M 30 mW maximum rating (revision {REVISION})\n"
                 f"error bars: {DRIVE_TEMP_DB} dB temperature allowance (fixed-pad rows); select-on-test rows include\n"
                 f"every in-service term (worst-case sum; pad step from the E24 set's largest gap, {sot['pad_set_max_gap_db']:.2f} dB)", fontsize=9)
    ax.legend(loc="lower left", fontsize=7.5)
    fig.tight_layout()
    fig.subplots_adjust(left=0.27)
    fig.savefig(out / "a5_overdrive_margin.png", dpi=150)
    plt.close(fig)
    # ---- Select-on-test sensitivity to the level reading (finding-4)
    fig, ax = plt.subplots(figsize=(8.0, 6.2))
    mgrid = np.linspace(0, 2.5, 126)
    for s_, col, lab in ((sot, COL["a5"], "as designed (coax, pad on the RF board)"), (sot_opt, COL["aux"], "option d5 (6 dB at the pin)")):
        fixed = s_["freq_span_within_unit_db"] / 2 + s_["step_half_db"] + SOT_DRIFT_DB
        ax.plot(mgrid, 10 * np.log10(A5_PIN_MAX_MW / SOT_TARGET_MW) - fixed - mgrid, color=col, lw=2,
                label=f"{lab}: margin to 30 mW and to 10 mW (equal by the centred target)")
    ax.axhline(0, color=INK, lw=2, ls="--", label="0 dB: drive at 30 mW (or 10 mW) at the worst in-service condition")
    for mv, txt in ((0.5, "+/-0.5 dB"), (SOT_MEAS_DB, f"+/-{SOT_MEAS_DB} dB: allocation (C1)"), (1.5, "+/-1.5 dB"),
                    (2.0, "+/-2 dB: tinySA Ultra published\nabsolute accuracy")):
        ax.axvline(mv, color=INK2, lw=0.8, ls=":")
        if mv < 1.9:
            ax.text(mv - 0.03, -1.15, txt, fontsize=7, color=INK2, va="bottom", ha="right", rotation=90)
        else:
            ax.text(mv + 0.03, 1.15, txt, fontsize=7, color=INK2, va="top", ha="left")
    ax.axvline(sot["reading_break_even_db"], color=COL["a4"], lw=1.2, ls="-.",
               label=f"break-even reading uncertainty, as designed: +/-{sot['reading_break_even_db']:.2f} dB")
    ax.set_xlim(0, 2.5)
    ax.set_ylim(-1.2, 1.2)
    ax.set_xlabel("Level-reading uncertainty at about 17 mW, build alignment (+/- dB)")
    ax.set_ylabel("Worst in-service margin inside 10 to 30 mW (dB)")
    ax.set_title(f"A5 select-on-test pad: margin against the level-reading uncertainty (revision {REVISION}, finding-4)\n"
                 f"other terms: frequency span / 2 {sot['freq_span_within_unit_db'] / 2:.2f} dB, half the E24 set's largest gap "
                 f"{sot['step_half_db']:.2f} dB, drift {SOT_DRIFT_DB} dB (estimates)", fontsize=9)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.14), fontsize=7.3)
    fig.tight_layout()
    fig.savefig(out / "a5_sot_reading_sensitivity.png", dpi=150)
    plt.close(fig)
    summary = {"run": RUNS["s1"], "revision": REVISION, "inputs": [RUNS[k] for k in ("d2", "d3", "d4", "d5", "p1", "p2", "p3")],
               "a5_sot_pad": sot, "a5_sot_pad_option_d5": sot_opt, "closure_uncertainty_terms": CLOSURE_UNC,
               "a5_closure_margin": clos, "a5_overdrive_margin_db": dict(od),
               "a5": {"drive_window_all_corners": d5["window_pass_all_corners"],
                      "drive_window_criterion_corners": d5["window_pass_criterion_corners"],
                      "pin_mw": [d5["pin_pa_w"]["min"] * 1e3, d5["pin_pa_w"]["nominal"] * 1e3, d5["pin_pa_w"]["max"] * 1e3],
                      "h3_pass": d5["h3_pass"], "sma_6v4_ref": p5["at_6v4"],
                      "levers_lpfmed_all_temperatures": p5["pass_levers_lpfmed_ge_3v97_at_6v4_all_temperatures"],
                      "sot_levers_lpfmed_all_temperatures": p6["pass_levers_lpfmed_ge_3v97_at_6v4_all_temperatures"],
                      "module_high_8v4_all_temperatures_w": p5["module_high_8v4_all_temperatures_w"]},
               "a4": {"pin_mw": [d4["pin_pa_w"]["min"] * 1e3, d4["pin_pa_w"]["nominal"] * 1e3, d4["pin_pa_w"]["max"] * 1e3],
                      "overdrive_pass": d4["overdrive_pass"], "h3_pass": d4["h3_pass"], "sma_6v4_ref": p4["at_6v4"],
                      "worst_low_6v4_all_temperatures_w": p4["worst_low_typ_6v4_all_temperatures_w"]},
               "verdicts": VERDICTS.get("s1", {})}
    (out / "result.json").write_text(json.dumps(summary, indent=2, default=float))
    L = [f"# {RUNS['s1']}: summary, select-on-test pad, overdrive and closure margins (revision {REVISION})", "",
         "Verdicts:"]
    for n_, v in VERDICTS.get("s1", {}).items():
        L.append(f"- {n_}: **{'PASS' if v['pass'] else 'FAIL'}**" + (f" ({v['detail']})" if v.get("detail") else "") + ".")
    L += ["", "## A5 select-on-test drive pad (estimate)", "",
          "| Interface | Frequency span in a unit (dB) | Half the pad set's largest gap (dB) | Band half-width, worst-case sum (dB) | Same, RSS (dB) | In-service drive (mW) | Overdrive margin to 30 mW (dB) | Margin above 10 mW (dB) | Break-even reading (+/- dB) | Pad set (dB) | Verdict |",
          "|---|---|---|---|---|---|---|---|---|---|---|"]
    for lab, s in (("as designed (coax, 18 dB pad on the RF board)", sot), ("option d5 (6 dB at the pin, 12 dB on the RF board)", sot_opt)):
        L.append(f"| {lab} | {s['freq_span_within_unit_db']:.2f} | {s['step_half_db']:.2f} | {s['half_width_db']:.2f} | {s['half_width_rss_db']:.2f} | "
                 f"{s['min_mw']:.1f} to {s['max_mw']:.1f} | {s['overdrive_margin_db']:+.2f} (RSS {s['overdrive_margin_rss_db']:+.2f}) | "
                 f"{s['underdrive_margin_db']:+.2f} | {s['reading_break_even_db']:.2f} | {len(s['pads'])} pads, {s['pads'][0]['loss_db']:.2f} to "
                 f"{s['pads'][-1]['loss_db']:.2f} ({s['pad_needed_db'][0]:.2f} to {s['pad_needed_db'][1]:.2f} needed) | **{'PASS' if s['pass'] else 'FAIL'}** |")
    L += ["", f"Half-width = frequency span / 2 + half the pad set's largest gap + level reading (allocation +/-{SOT_MEAS_DB} dB; "
          f"no characterization at 17 mW yet) + drift over -10 to +45 C and supply ({SOT_DRIFT_DB} dB, est.: GVA-84+ 0.04 dB from its "
          "datasheet coefficient, passives under 0.05 dB, Si5351 edge and swing 0.2 dB).", "",
          "Sensitivity to the level reading (as designed):", "",
          "| Reading (+/- dB) | In-service drive (mW) | Overdrive margin (dB) | Margin above 10 mW (dB) | Verdict |", "|---|---|---|---|---|"]
    for s in sot["sensitivity"]:
        L.append(f"| {s['meas_db']:.1f} | {s['min_mw']:.1f} to {s['max_mw']:.1f} | {s['overdrive_margin_db']:+.2f} | "
                 f"{s['underdrive_margin_db']:+.2f} | **{'PASS' if s['pass'] else 'FAIL'}** |")
    L += ["", "The tinySA Ultra's published absolute accuracy is +/-2 dB after level calibration "
          "(tinysa.org/wiki/pmwiki.php?n=TinySA4.Specification, read 2026-09-28).", "",
          f"E24 1 % pi pads of the as-designed set (largest gap {sot['pad_set_max_gap_db']:.2f} dB, return loss at least 25 dB):", "",
          "| Loss (dB) | Shunt, series, shunt (ohm) | Return loss (dB) |", "|---|---|---|"]
    for pd in sot["pads"]:
        L.append(f"| {pd['loss_db']:.2f} | {pd['shunt']:g}, {pd['series']:g}, {pd['shunt']:g} | "
                 f"{'at least 60' if pd['rl_db'] >= 60 else format(pd['rl_db'], '.1f')} |")
    L += ["", f"E24 1 % pi pads of the option d5 set (largest gap {sot_opt['pad_set_max_gap_db']:.2f} dB): " +
          "; ".join(f"{pd['loss_db']:.2f} dB ({pd['shunt']:g}, {pd['series']:g}, {pd['shunt']:g})" for pd in sot_opt["pads"]) + ".",
          "", "## A5 overdrive margin against 30 mW", "", "| Case | Margin (dB) |", "|---|---|"]
    for n_, v in od:
        L.append(f"| {n_} | {v:+.2f} |")
    L += ["", f"Fixed-pad rows carry a further {DRIVE_TEMP_DB} dB temperature allowance (estimate) not included above.", "",
          f"## A5 closure margin at 6.4 V (lowest corner, typical module, C2 and C3: feed at most 0.35 ohm at 25 C, VGG {A5_VGG_C3} V)", "",
          "| Temperature case | PA case (C) | p1, LPF median (W; margin dB; with the terms) | p1, LPF worst (W; margin dB; with the terms) | p3, LPF median (W; margin dB; with the terms) | p3, LPF worst (W; margin dB; with the terms) | Datasheet-minimum module, p1, LPF median (dB) |",
          "|---|---|---|---|---|---|---|"]

    def cell(e):
        return f"{e['w']:.2f}; {e['margin_db']:+.2f}; {e['margin_low_db']:+.2f} to {e['margin_high_db']:+.2f}"
    for k in keys:
        a_, b_ = clos["p1"][k], clos["p3"][k]
        L.append(f"| {a_['label']} | {a_['pa_case_c']:.1f} | {cell(a_['lpfmed'])} | {cell(a_['lpfworst'])} | {cell(b_['lpfmed'])} | "
                 f"{cell(b_['lpfworst'])} | {a_['lpfmed']['minmodule_margin_db']:+.2f} |")
    L += ["", "Terms not carried as corners (added to the margin as a range):"]
    for t, lo_, hi_, basis in CLOSURE_UNC:
        L.append(f"- {t}: {lo_:+.2f} / {hi_:+.2f} dB ({basis}).")
    L += ["", "Plots: `pin_at_pa_vs_pack.png`, `pout_at_sma_vs_pack.png`, `a5_closure_margin.png`, `a5_overdrive_margin.png`, "
          "`a5_sot_reading_sensitivity.png`.", ""]
    (out / "result.md").write_text("\n".join(L))
    shutil.copy2(Path(__file__), out / Path(__file__).name)
    print("s1", json.dumps({"sot": {k: v for k, v in sot.items() if k not in ("pads", "sensitivity")},
                            "sot_opt": {k: v for k, v in sot_opt.items() if k not in ("pads", "sensitivity")},
                            "closure": clos, "od": od}, default=float)[:4000])


# Verdicts the analysis record reports (revision 2, section 8.1). --expect compares every verdict of the runs made
# with this list, so that a changed verdict is detected (finding-5). Filled from the revision 2 run of 2026-09-28.
EXPECTED: dict[str, dict[str, bool]] = {
    'd2': {
        'check: one .raw step per corner': True,
        'A5 lumped CLK1 pin load at most 15 pF (Si5351 Table 7)': True,
        'A5 3f at the GVA-84+ input at least 25 dB below f': True,
        'A5 GVA-84+ input below +13 dBm': True,
        'A5 module input 10 to 30 mW at every corner (fixed pad)': False,
        'A5 module input 10 to 30 mW at the TS-012 criterion corners (fixed pad)': False,
    },
    'd3': {
        'check: one .raw step per corner': True,
        'A4 lumped CLK1 pin load at most 15 pF (Si5351 Table 7)': True,
        'A4 3f at the GVA-84+ input at least 25 dB below f': True,
        'A4 GVA-84+ input below +13 dBm': True,
        'A4 drive at most the 0.2 W ruggedness-test level (informative)': True,
    },
    'd4': {
        'check: A5 10 ps step against 20 ps within 0.02 dB (power) and 0.5 dB (3f)': True,
        'check: A4 10 ps step against 20 ps within 0.02 dB (power) and 0.5 dB (3f)': True,
        'A5 module input at most 30 mW at any coax length (fixed pad)': False,
        'A4 drive at most 0.2 W at any coax length (informative)': True,
    },
    'd5': {
        'check: one .raw step per corner': True,
        'A5 lumped CLK1 pin load at most 15 pF (Si5351 Table 7)': True,
        'A5 option d5: equivalent CLK1 pin load at most 15 pF at every corner': True,
        'A5 3f at the GVA-84+ input at least 25 dB below f': True,
        'A5 GVA-84+ input below +13 dBm': True,
        'A5 module input 10 to 30 mW at every corner (fixed pad)': False,
        'A5 module input 10 to 30 mW at the TS-012 criterion corners (fixed pad)': False,
    },
    'p1': {
        'check: one .raw step per corner': True,
        'check: PA case temperature solved by LTspice equals the thermal law within 0.01 K': True,
        'A5 lowest corner at least 3.97 W from 6.4 to 8.4 V, 25 C key-down': False,
        'A5 lowest corner at least 3.97 W from 6.4 to 8.4 V, every key-down case': False,
        'A5 nominal corner at least 3.97 W at 6.4 V, every key-down case': False,
        'A5 lowest with C2 and C3, LPF at its median, at least 3.97 W at 6.4 V, 25 C key-down': False,
        'A5 lowest with C2 and C3, LPF at its median, at least 3.97 W at 6.4 V, every key-down case': False,
        'A5 lowest with C2 and C3, LPF at its worst case, at least 3.97 W at 6.4 V, every key-down case': False,
        'A5 open loop at 8.4 V: module output at most 8 W (stability conditions), every case': False,
        'A5 open loop at 8.4 V: module output at most 10 W (maximum rating), every case': False,
    },
    'p2': {
        'check: one .raw step per corner': True,
        'check: PA case temperature solved by LTspice equals the thermal law within 0.01 K': True,
        'A4 lowest corner at least 3.97 W from 6.4 to 8.4 V, 25 C key-down': False,
        'A4 lowest corner at least 3.97 W from 6.4 to 8.4 V, every key-down case': False,
        'A4 nominal corner at least 3.97 W at 6.4 V, every key-down case': False,
    },
    'p3': {
        'check: one .raw step per corner': True,
        'check: PA case temperature solved by LTspice equals the thermal law within 0.01 K': True,
        'A5 lowest corner at least 3.97 W from 6.4 to 8.4 V, 25 C key-down': False,
        'A5 lowest corner at least 3.97 W from 6.4 to 8.4 V, every key-down case': False,
        'A5 nominal corner at least 3.97 W at 6.4 V, every key-down case': False,
        'A5 lowest with C2 and C3, LPF at its median, at least 3.97 W at 6.4 V, 25 C key-down': False,
        'A5 lowest with C2 and C3, LPF at its median, at least 3.97 W at 6.4 V, every key-down case': False,
        'A5 lowest with C2 and C3, LPF at its worst case, at least 3.97 W at 6.4 V, every key-down case': False,
        'A5 open loop at 8.4 V: module output at most 8 W (stability conditions), every case': False,
        'A5 open loop at 8.4 V: module output at most 10 W (maximum rating), every case': False,
    },
    's1': {
        'A5 select-on-test drive 10 to 30 mW in service, reading allocation +/-1.0 dB': True,
        'A5 select-on-test drive 10 to 30 mW with a tinySA Ultra reading alone (+/-2 dB published)': False,
        'A5 option d5 select-on-test drive 10 to 30 mW, reading allocation +/-1.0 dB': True,
    },
}


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    what = args[0] if args else "all"
    todo = ["d2", "d3", "d4", "d5", "p1", "p2", "p3", "s1"] if what == "all" else [what]
    for k in todo:
        if k == "d1":
            run_d1()
        elif k == "d2":
            analyse_drive("a5", "d2")
        elif k == "d3":
            analyse_drive("a4", "d3")
        elif k == "d4":
            run_d4()
        elif k == "d5":
            analyse_drive("a5", "d5", pinpad=True)
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
    # exit status (revision 2, finding-5): 0 every criterion met and every check passed; 1 every check passed and at
    # least one criterion failed (the results are valid and report the failure); 2 a check failed (do not use)
    failed_checks = [(r, n) for r, d in VERDICTS.items() for n, v in d.items() if v["kind"] == "check" and not v["pass"]]
    failed_crit = [(r, n) for r, d in VERDICTS.items() for n, v in d.items() if v["kind"] == "criterion" and not v["pass"]]
    print("\nVerdicts:")
    for r, d in VERDICTS.items():
        for n, v in d.items():
            print(f"  {r}: {'PASS' if v['pass'] else 'FAIL'}  {n}" + (f" ({v['detail']})" if v["detail"] else ""))
    if what == "all":
        (rundir("s1") / "verdicts.json").write_text(json.dumps(VERDICTS, indent=1))
    code = 2 if failed_checks else (1 if failed_crit else 0)
    if "--expect" in sys.argv:
        diff = [(r, n, v["pass"], EXPECTED.get(r, {}).get(n)) for r, d in VERDICTS.items() for n, v in d.items()
                if EXPECTED.get(r, {}).get(n) != v["pass"]]
        for r, n, got, exp in diff:
            print(f"  VERDICT CHANGED: {r}: {n}: now {'PASS' if got else 'FAIL'}, record says "
                  f"{'not listed' if exp is None else ('PASS' if exp else 'FAIL')}")
        print(f"--expect: {len(diff)} verdict(s) differ from the analysis record")
        code = 3 if diff else 0
    print(f"exit status {code}")
    sys.exit(code)


if __name__ == "__main__":
    main()
