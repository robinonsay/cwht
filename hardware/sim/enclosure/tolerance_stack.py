#!/usr/bin/env python3
"""Mechanical tolerance stacks and load checks (docs/design/analysis/mechanical-tolerance-stack.md).

Stacks S1 to S9: worst-case sum and root-sum-square of the contributors, each compared with
the allowance the design gives (clearance per side, compression window, distance limit).
Load checks L1 (REQ-SYS-105 port retention) and L2 (REQ-SYS-116 drop, first-cut deceleration).
Every contributor value and its source are in the tables below; FDM (printed) values are the
author's planning values for an H2C print (Low) until the fit-check coupon of WP-PDR-39 measures
them. Developer evidence (numpy/matplotlib class B, no TV record of their own).
Run: .venv/bin/python hardware/sim/enclosure/tolerance_stack.py [--check]
Writes hardware/sim/enclosure/out/tolerance-stack.csv and
docs/reviews/PDR/figures/tolerance-stack.png. --check exits 1 if a verdict differs from EXPECTED.
"""
from __future__ import annotations

import argparse
import csv
import math
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

ROOT = Path(__file__).resolve().parents[3]
CSV = ROOT / "hardware/sim/enclosure/out/tolerance-stack.csv"
PNG = ROOT / "docs/reviews/PDR/figures/tolerance-stack.png"

# Shared contributors (+/- mm)
FDM_FEATURE = 0.20        # position of a printed feature from the part datum (H2C, PETG; Low, planning)
INSERT_POS = 0.20         # heat-set insert position after installation (Low)
HOLE_FLOAT = 0.10         # M3 screw (3.0) in a 3.2 mm board hole, radial
BOARD_FEAT = 0.10         # board feature position from its holes (PCBWay: drill position +/-0.075, F9)
THT_PART = 0.15           # through-hole part on the board: hole +/-0.08 plus body float
CNC_FEATURE = 0.10        # machined feature, called out on the drawing (research A5 class f equivalent)
POCKET_CLEAR = 0.10       # clearance of a machined block in a printed pocket, per side
MODULE_SOLDER = 0.30      # Pico 2 module placed and hand-soldered by the owner on its castellations (Low)

BOARD_IN_CASE = [INSERT_POS, HOLE_FLOAT]

STACKS = {
    # id: (title, contributors, allowance, basis of the allowance, rule "worst" or "rss")
    "S1": ("SMA axis to board, if the jack were board-mounted (rigid)",
           [CNC_FEATURE, FDM_FEATURE, POCKET_CLEAR] + BOARD_IN_CASE + [BOARD_FEAT], 0.10,
           "rigid board-mount SMA: about 0.1 mm misalignment before the joint is loaded (author rule)", "worst"),
    "S2": ("Jack nose in its wall opening (radial)", [THT_PART] + BOARD_IN_CASE + [FDM_FEATURE], 1.50,
           "opening 9.0 mm around a 6.0 mm nose: 1.5 mm per side", "worst"),
    "S3": ("Encoder bushing in its front-wall hole (radial)", [THT_PART] + BOARD_IN_CASE + [FDM_FEATURE], 0.75,
           "hole 8.5 mm around a 7.0 mm bushing: 0.75 mm per side", "worst"),
    "S4a": ("Display active area inside the 24.0 mm window, glass located on the board", [0.30] + BOARD_IN_CASE + [FDM_FEATURE],
            0.48, "(24.0 - 23.04)/2 per side", "worst"),
    "S4b": ("Display active area inside the 24.0 mm window, glass located in the front-shell pocket", [0.20, 0.10], 0.48,
            "(24.0 - 23.04)/2 per side; pocket 27.0 x 30.7 for glass 26.6 x 30.3", "worst"),
    "S5a": ("USB plug overmold in the 12.0 x 10.0 opening (ICD-CTL-USB)", [MODULE_SOLDER, 0.10] + BOARD_IN_CASE + [FDM_FEATURE],
            0.70, "(12.0 - 10.6)/2 per side, width", "worst"),
    "S5b": ("USB plug overmold in a 12.6 x 10.6 opening (proposed)", [MODULE_SOLDER, 0.10] + BOARD_IN_CASE + [FDM_FEATURE],
            1.00, "(12.6 - 10.6)/2 per side, width", "worst"),
    "S6a": ("Gap pad compression, heatsink fixed in a printed pocket", [0.15, 0.15, 0.10, 0.10], 0.10,
            "0.5 mm pad held between 10 % and 40 % compression: 0.375 +/-0.10 mm", "worst"),
    "S6b": ("Gap pad compression, CNC fallback pedestal (same part as the bosses)", [0.05, 0.05], 0.10,
            "as S6a", "worst"),
    "S6c": ("Gap pad compression, spring-loaded heatsink (option C design rule)", [0.15, 0.15, 0.10, 0.10], 0.60,
            "spring travel +/-0.6 mm: compression set by the spring force, not by the stack", "worst"),
    "S7": ("Board edge to inner wall", [0.20] + BOARD_IN_CASE + [FDM_FEATURE], 2.00, "2.0 mm design clearance (outline JSON)",
           "worst"),
    "S8": ("Knob skirt in a knob recess (REQ-SYS-111 1.0 mm radial)", [0.10, THT_PART] + BOARD_IN_CASE + [FDM_FEATURE], 1.00,
           "recess diameter = knob + 2 x (1.0 + 1.0): 1.0 mm per side beyond the 1.0 mm requirement", "worst"),
    "S9": ("Counterpoise hole to SMA axis (REQ-SYS-107 20 mm TBR)", [CNC_FEATURE], 8.0, "20 mm limit minus 12 mm design distance",
           "worst"),
}

SHORT = {"S1": "SMA axis to board (rigid jack case)", "S2": "jack nose in wall opening", "S3": "encoder bushing in hole",
         "S4a": "display window, glass on board", "S4b": "display window, glass in shell pocket",
         "S5a": "USB opening 12.0 x 10.0 (ICD)", "S5b": "USB opening 12.6 x 10.6 (proposed)",
         "S6a": "gap pad, heatsink fixed in pocket", "S6b": "gap pad, CNC pedestal", "S6c": "gap pad, spring-loaded heatsink",
         "S7": "board edge to inner wall", "S8": "knob skirt in recess", "S9": "counterpoise hole to SMA axis"}

EXPECTED = {"S1": False, "S2": True, "S3": True, "S4a": False, "S4b": True, "S5a": False, "S5b": True, "S6a": False,
            "S6b": True, "S6c": True, "S7": True, "S8": True, "S9": True}

# Loads
MOMENT = 4.0              # N m, REQ-SYS-105
BLOCK_ARM = 0.012         # m, shortest reaction couple arm of the 12 x 20 x 12 mm port block
BEARING_AREA = 144e-6     # m^2, 12 x 12 mm bearing face on the printed pocket
PETG_COMP = 45e6          # Pa, PETG compressive strength at 23 C, derated 20 % for 45 C: planning (Low)
INSERT_PULL = 500.0       # N, M3 heat-set insert pull-out in PETG, conservative planning value (Low)
MASS = 0.37               # kg, C1 roll-up (TS-011 section 4)
DROP_H = 1.0              # m, REQ-SYS-116 (TBR)
STOP = (0.5e-3, 1.0e-3)   # m, local crush of a filleted PETG corner on a hard floor (Low)
CELL_MASS = 0.048         # kg per cell (ICD-PWR-CELL 3.2.1)
RIB_AREA = 108e-6         # m^2 per cell, two ribs 18 x 3 mm
BOARD_MASS = 0.035        # kg board and parts
N_BOSSES = 6
E_FR4 = 22e9              # Pa, FR-4 flexural modulus, typical (Low)
BOARD_W = 0.062           # m, board width
BUTTON_F = 10.0           # N, finger press on a board-mounted button (planning)
SPANS = (0.120, 0.0745)   # m, span between supports: four corner bosses only, and the six-boss layout


def stack_values(contrib):
    return sum(contrib), math.sqrt(sum(c * c for c in contrib))


def evaluate():
    rows = []
    for sid, (title, contrib, allow, basis, rule) in STACKS.items():
        worst, rss = stack_values(contrib)
        value = worst if rule == "worst" else rss
        rows.append(dict(id=sid, title=title, worst=round(worst, 3), rss=round(rss, 3), allowance=allow, rule=rule,
                         passes=value <= allow + 1e-9, basis=basis))
    loads = {}
    f_pair = MOMENT / BLOCK_ARM
    loads["L1 bearing stress, MPa"] = round(f_pair / BEARING_AREA / 1e6, 2)
    loads["L1 bearing margin (strength / stress)"] = round(PETG_COMP / (f_pair / BEARING_AREA), 1)
    loads["L1 insert load per screw, N"] = round(f_pair / 2, 0)
    loads["L1 insert margin (pull-out / load)"] = round(INSERT_PULL / (f_pair / 2), 2)
    v = math.sqrt(2 * 9.81 * DROP_H)
    for s in STOP:
        g = v * v / (2 * s) / 9.81
        loads[f"L2 peak deceleration at {s * 1000:.1f} mm stop, g"] = round(g, 0)
        loads[f"L2 cell rib stress at {s * 1000:.1f} mm stop, MPa"] = round(CELL_MASS * g * 9.81 / RIB_AREA / 1e6, 1)
        loads[f"L2 load per board boss at {s * 1000:.1f} mm stop, N"] = round(BOARD_MASS * g * 9.81 / N_BOSSES, 0)
    loads["L2 drop energy, J"] = round(MASS * 9.81 * DROP_H, 2)
    for t in (1.0e-3, 1.2e-3, 1.6e-3):
        inertia = BOARD_W * t ** 3 / 12
        for span in SPANS:
            d = BUTTON_F * span ** 3 / (48 * E_FR4 * inertia)
            loads[f"L3 board deflection, {t * 1000:.1f} mm board, span {span * 1000:.1f} mm, mm"] = round(d * 1000, 2)
    return rows, loads


def plot(rows):
    fig, ax = plt.subplots(figsize=(14, 6.8))
    y = list(range(len(rows)))[::-1]
    for yi, r in zip(y, rows):
        ax.barh(yi + 0.18, r["worst"], height=0.34, color="#c0504d" if not r["passes"] else "#1f4e79")
        ax.barh(yi - 0.18, r["rss"], height=0.34, color="#bfbfbf")
        ax.plot([r["allowance"], r["allowance"]], [yi - 0.42, yi + 0.42], color="k", lw=2.2)
        ax.text(min(max(r["worst"], r["allowance"]), 3.0) + 0.05, yi,
                f"worst {r['worst']:.2f} / RSS {r['rss']:.2f} / allow {r['allowance']:.2f}", va="center", fontsize=8)
    ax.set_yticks(y)
    ax.set_yticklabels([f"{r['id']} {SHORT[r['id']]}" for r in rows], fontsize=8.5)
    ax.set_xlim(0, 4.0)
    ax.set_xlabel("mm (bars: worst case, dark = passes, red = fails; grey = RSS; black tick: allowance)")
    ax.set_title("Tolerance stacks against their allowances (S9 allowance 8.0 mm off scale, passes)")
    ax.grid(axis="x", alpha=0.3)
    fig.text(0.01, 0.01, "Developer evidence; FDM contributors are planning values until the WP-PDR-39 fit-check coupon.",
             fontsize=8)
    fig.subplots_adjust(left=0.24, right=0.98, top=0.93, bottom=0.12)
    PNG.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(PNG, dpi=125)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    rows, loads = evaluate()
    CSV.parent.mkdir(parents=True, exist_ok=True)
    with CSV.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    plot(rows)
    for r in rows:
        print(f"{r['id']}: worst {r['worst']} rss {r['rss']} allow {r['allowance']} -> {'PASS' if r['passes'] else 'FAIL'}"
              f"  ({r['title']})")
    for k, v in loads.items():
        print(f"{k}: {v}")
    errs = [f"{r['id']}: got {r['passes']}, expected {EXPECTED[r['id']]}" for r in rows if r["passes"] != EXPECTED[r["id"]]]
    if args.check:
        for e in errs:
            print("MISMATCH:", e)
        print("CHECK", "FAIL" if errs else "PASS")
        return 1 if errs else 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
