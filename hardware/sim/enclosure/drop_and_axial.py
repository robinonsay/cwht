#!/usr/bin/env python3
"""Drop per face and axial plug and bushing stacks (docs/design/analysis/mechanical-tolerance-stack.md
revision 1, sections 6 and 4.1; INSP-084 finding-1).

REQ-SYS-116 names "each face" and "with the antenna fitted"; REQ-SYS-108 names "fully seated" plugs.
This script adds, beside the iteration 1 stacks of tolerance_stack.py (unchanged):

- D rows: one drop row per face and per internal load path, for the six faces of the option C1 case,
  with the +X face computed twice (whip fitted, corner impact: a moment on the port block; end-on:
  the connector strikes first). Each row gives the load at a 1.0 mm and a 0.5 mm stopping distance
  (1000 g and 2000 g), the element that carries it, its capacity (planning values, Low) and the
  margin (capacity / load). The pass rule is the TS-011 M2 rule, margin >= 1.5 at 2000 g; a row
  between 1.0 and 1.5 is "not shown"; below 1.0 it fails. Rows that fail on the revision 0 design
  carry the design rule of TS-011 revision 1 section 8 that the rule row then checks.
- A rows: the axial stacks of the key jack, the headphone jack and the micro-USB receptacle (plug
  fully seated through the wall), and the encoder bushing thread engagement through the front wall.

Every input and its source is in the tables below. Developer evidence (venv Python, matplotlib
class B, no TV record of its own).
Run: .venv/bin/python hardware/sim/enclosure/drop_and_axial.py [--check]
Writes hardware/sim/enclosure/out/drop-and-axial.csv and docs/reviews/PDR/figures/drop-and-axial.png.
--check exits 1 if a verdict differs from EXPECTED.
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
CSV = ROOT / "hardware/sim/enclosure/out/drop-and-axial.csv"
PNG = ROOT / "docs/reviews/PDR/figures/drop-and-axial.png"

G = 9.81
DROP_H = 1.0                 # m, REQ-SYS-116 (TBR)
STOPS = (1.0e-3, 0.5e-3)     # m, local crush of the landing printed face or corner (Low)
MASS = 0.375                 # kg, TS-011 Appendix A.1 roll-up for C1 (INSP-084 finding-5: 0.375, not 0.37)
M = dict(cells=0.096, holders=0.022, board=0.035, heatsink=0.050, display=0.0036, port_block=0.008)
PASS_MARGIN = 1.5            # TS-011 M2 margin rule

# Capacities (planning values, recalled typical data, Low; TS-011 Appendix B.3 item 3 fetches the filament TDS)
PETG_COMP = 45e6             # Pa, PETG compressive strength derated for 45 C (tolerance analysis section 2)
PETG_FLEX = 60e6             # Pa, PETG flexural strength derated for 45 C (Low)
FR4_Z_COMP = 250e6           # Pa, FR-4 compressive strength through the thickness (Low)
FR4_FLEX = 400e6             # Pa, FR-4 flexural strength (Low)
INSERT_PULL = 500.0          # N, M3 heat-set insert pull-out (tolerance analysis section 2)
HOLDER_COMP = 40e6           # Pa, cell holder body (glass-filled nylon or PBT class) bearing (Low)

# Geometry (hardware/enclosure/board-outline.json and TS-011 section 8 rules)
GUARD_SOLID_AREA = 0.33 * 48e-3 * 66e-3   # m2, guard frame and grille ribs, 6 mm slots and 3 mm ribs (rule 4)
LEDGE_AREA = 160e-6          # m2, heat-sink pocket ledges (tolerance analysis section 6)
RIB_AREA = 2 * 108e-6        # m2, back-shell cell ribs, two cells (tolerance analysis section 6)
BOSS_ANNULUS = math.pi / 4 * (7.5e-3 ** 2 - 4.6e-3 ** 2)  # m2, boss top around the insert
N_BOSS = 6
BOSS_H = 15.9e-3             # m, boss height, back wall to board (Z stack 2.0 to 17.9)
BOSS_D = 7.5e-3
GUSSET_FACTOR = 4.0          # section-modulus gain of four 1.5 mm gussets to the back wall (rule 20, Low)
BOARD_W = 62e-3
BOARD_T = 1.0e-3
SPAN_HS = 48e-3              # m, bosses at x 78.5 and 126.5 on either side of the heat sink
SPAN_CELLS = 74.5e-3         # m, bosses at x 4 and 78.5 on either side of the holders
POST_AREA = math.pi / 4 * (6e-3) ** 2  # m2, one printed front-shell post on a 6 mm copper-free pad
N_POST_HS = 2                # rule 18: two posts within 10 mm of the PA pad
N_POST_CELLS = 4             # rule 18: four posts over the holder bodies (two of them the button posts)
FRONT_FACE_AREA = 0.0080     # m2, flat front face less its openings (Low)
BLOCK_ARM = 12e-3            # m, shortest couple arm of the port block (L1)
BLOCK_BEARING = 144e-6       # m2, 12 x 12 mm pocket face (L1)
BLOCK_END_AREA_REV0 = 20e-3 * 12e-3   # m2, port block inner face on the pocket (revision 0)
BLOCK_END_AREA_RULE = 20e-3 * 20e-3   # m2, rule 6 revision 1: 20 x 20 x 2 mm inner flange
WHIP_MOMENT = 4.0            # N m, REQ-SYS-105: the moment of a 10 N push on a 40 cm whip (antenna-and-erp F8)
DYN_FACTOR = 2.0             # suddenly applied load on an elastic system (textbook factor, Low)
HOLDER_END_AREA = 2 * 20e-3 * 14e-3   # m2, the two holder end walls on the back-shell end ribs (rule 19)
GLASS_AREA = 26.6e-3 * 30.3e-3


def accel(stop: float) -> float:
    return G * DROP_H / stop  # m/s2, from v^2 = 2 g h and v^2 = 2 a s


def drop_rows():
    rows = []

    def add(face, case, carrier, load_fn, cap, unit, rule, design):
        vals = []
        for s in STOPS:
            load = load_fn(accel(s))
            vals.append((load, cap / load))
        m2000 = vals[1][1]
        verdict = "pass" if m2000 >= PASS_MARGIN else ("not shown" if m2000 >= 1.0 else "fail")
        rows.append(dict(id=f"D{len(rows) + 1}", face=face, case=case, carrier=carrier, unit=unit,
                         load_1000g=round(vals[0][0], 2), load_2000g=round(vals[1][0], 2),
                         capacity=round(cap, 2), margin_1000g=round(vals[0][1], 2), margin_2000g=round(m2000, 2),
                         verdict=verdict, design=design, rule=rule))

    mpa = 1e6
    # -Z back face: the guard frame lands first (it protrudes 10 mm)
    add("-Z back", "unit on the guard frame", "printed guard frame and ribs",
        lambda a: MASS * a / GUARD_SOLID_AREA / mpa, PETG_COMP / mpa, "MPa", "rule 4 (3 mm ribs)", "rev1")
    add("-Z back", "heat sink on its pocket ledges", "back-shell ledges 160 mm2",
        lambda a: M["heatsink"] * a / LEDGE_AREA / mpa, PETG_COMP / mpa, "MPa", "", "rev0")
    add("-Z back", "cells on the back-shell ribs", "two rib pairs, 216 mm2",
        lambda a: M["cells"] * a / RIB_AREA / mpa, PETG_COMP / mpa, "MPa", "", "rev0")
    add("-Z back", "board and holders on the boss tops", "six boss annuli",
        lambda a: (M["board"] + M["holders"]) * a / N_BOSS / BOSS_ANNULUS / mpa, PETG_COMP / mpa, "MPa", "", "rev0")
    # +Z front face: the flat face lands (knob tops recessed, rule 17)
    add("+Z front", "unit on the front face", "front shell, 8000 mm2",
        lambda a: MASS * a / FRONT_FACE_AREA / mpa, PETG_COMP / mpa, "MPa", "rule 17 (knob tops 0.5 mm below the face)",
        "rev1")

    def board_bending(mass, span):
        # central load on a simply supported 62 mm wide, 1.0 mm board: sigma = (P L / 4) / (b t^2 / 6)
        return lambda a: (mass * a * span / 4) / (BOARD_W * BOARD_T ** 2 / 6) / mpa
    add("+Z front", "heat sink toward the board, no post (revision 0)", "board in bending, 48 mm span",
        board_bending(M["heatsink"], SPAN_HS), FR4_FLEX / mpa, "MPa", "", "rev0")
    add("+Z front", "heat sink toward the board, two posts (rule 18)", "board in compression at 2 posts",
        lambda a: M["heatsink"] * a / (N_POST_HS * POST_AREA) / mpa, FR4_Z_COMP / mpa, "MPa", "rule 18", "rev1")
    add("+Z front", "posts under the heat-sink load (rule 18)", "two printed posts",
        lambda a: M["heatsink"] * a / (N_POST_HS * POST_AREA) / mpa, PETG_COMP / mpa, "MPa", "rule 18", "rev1")
    add("+Z front", "cells and holders toward the board, no post (revision 0)", "board in bending, 74.5 mm span",
        board_bending(M["cells"] + M["holders"], SPAN_CELLS), FR4_FLEX / mpa, "MPa", "", "rev0")
    add("+Z front", "cells and holders, four posts (rule 18)", "four printed posts",
        lambda a: (M["cells"] + M["holders"]) * a / (N_POST_CELLS * POST_AREA) / mpa, PETG_COMP / mpa, "MPa",
        "rule 18", "rev1")
    add("+Z front", "board pulls on the inserts", "six M3 inserts in pull-out",
        lambda a: M["board"] * a / N_BOSS, INSERT_PULL, "N", "", "rev0")
    add("+Z front", "display glass on its pocket floor", "front-shell pocket",
        lambda a: M["display"] * a / GLASS_AREA / mpa, PETG_COMP / mpa, "MPa", "", "rev0")
    # +Y and -Y side faces
    add("+/-Y side", "cells sideways on the rib pairs", "two rib pairs",
        lambda a: M["cells"] * a / RIB_AREA / mpa, PETG_COMP / mpa, "MPa", "", "rev0")

    def boss_bend(gusset):
        z = math.pi * BOSS_D ** 3 / 32 * gusset
        return lambda a: ((M["board"] + M["holders"]) * a / N_BOSS * BOSS_H) / z / mpa
    add("+/-X, +/-Y", "board and holders in-plane on the bosses, plain bosses (revision 0)", "boss root in bending",
        boss_bend(1.0), PETG_FLEX / mpa, "MPa", "", "rev0")
    add("+/-X, +/-Y", "board and holders in-plane, gusseted bosses (rule 20)", "boss root with four gussets",
        boss_bend(GUSSET_FACTOR), PETG_FLEX / mpa, "MPa", "rule 20", "rev1")
    # +X antenna end
    add("+X end", "whip fitted, corner impact: moment on the port block, pocket bearing", "printed pocket face 144 mm2",
        lambda a: DYN_FACTOR * WHIP_MOMENT / BLOCK_ARM / BLOCK_BEARING / mpa, PETG_COMP / mpa, "MPa",
        "rule 6 (block captured between the shells)", "rev0")
    add("+X end", "whip fitted, corner impact: moment on the port block, screws alone", "two M3 inserts in pull-out",
        lambda a: DYN_FACTOR * WHIP_MOMENT / BLOCK_ARM / 2, INSERT_PULL, "N", "", "rev0")
    add("+X end", "end-on, connector strikes first: block on its pocket (revision 0)", "pocket face 20 x 12 mm",
        lambda a: MASS * a / BLOCK_END_AREA_REV0 / mpa, PETG_COMP / mpa, "MPa", "", "rev0")
    add("+X end", "end-on: block with its 20 x 20 mm flange (rule 6)", "pocket face 20 x 20 mm",
        lambda a: MASS * a / BLOCK_END_AREA_RULE / mpa, PETG_COMP / mpa, "MPa", "rule 6", "rev1")
    add("+/-X ends", "cells along X on the holder end walls and end ribs (rule 19)", "holder end walls on ribs",
        lambda a: M["cells"] * a / HOLDER_END_AREA / mpa, HOLDER_COMP / mpa, "MPa", "rule 19", "rev1")
    return rows


# ---------------------------------------------------------------- axial stacks
JACK_RECESS_NOM = 1.0e-3     # m, rule 21: jack nose face 1.0 mm behind the -X outer face (was flush to 0.5 mm proud)
JACK_X_TOL = [0.15e-3, 0.20e-3, 0.10e-3, 0.20e-3]  # THT part, insert, screw float, printed face (S2 contributors)
OPENING_JACK = 9.0e-3
PLUG_OVERMOLD_MAX = 7.0e-3   # m, admitted plug: overmold diameter at most 7.0 mm over its first 2 mm (definition, rule 21)
S2_WORST = 0.65e-3           # m, radial stack of the jack nose (tolerance_stack.py S2)
USB_FACE_DEPTH = 3.7e-3      # m, receptacle face behind the outer face: 3.0 board gap + 2.0 wall - 1.3 overhang (Low)
USB_TOL = [0.30e-3, 0.10e-3, 0.20e-3, 0.10e-3, 0.20e-3]  # module solder, module, insert, float, printed face (S5)
USB_OVERMOLD_LEN_MIN = 8.0e-3  # m, micro-B plug overmold length that can enter the shroud (Low)
ENC_GAP_BODY_TO_WALL = 28.0e-3 - (18.9e-3 + 6.5e-3)  # m, body top (6.5 mm body, Low) to the wall inner face
WALL = 2.0e-3
WASHER = 0.5e-3              # m, toothed washer of rule O3
NUT = 2.0e-3                 # m, panel nut
ENC_Z_TOL = [0.20e-3, 0.20e-3, 0.30e-3, 0.20e-3]  # insert, boss height (FDM), encoder body height, wall thickness
BUSHING_LEN_RULE = 9.0e-3    # m, rule 22: bushing thread length from the body at least 9 mm
BUSHING_LEN_SHORT = 7.0e-3   # m, a 7 mm bushing, for comparison


def axial_rows():
    rows = []
    tol = sum(JACK_X_TOL)
    r_min, r_max = JACK_RECESS_NOM - tol, JACK_RECESS_NOM + tol
    radial_room = (OPENING_JACK - PLUG_OVERMOLD_MAX) / 2 - S2_WORST  # overmold centred on the nose, nose off-centre by S2
    for name in ("key jack", "headphone jack"):
        ok = r_min > 0 and radial_room > 0 and r_max <= 2.0e-3
        rows.append(dict(id=f"A{len(rows) + 1}", item=f"{name}: plug fully seated through the -X wall",
                         value=f"nose recess {r_min * 1e3:.2f} to {r_max * 1e3:.2f} mm; overmold <= 7.0 mm in a 9.0 mm opening, "
                               f"radial room {radial_room * 1e3:.2f} mm with the nose off-centre by the S2 worst case",
                         allowance="recess > 0 (the end face lands, not the jack); recess <= 2.0 mm (the overmold's first 2 mm); "
                                   "radial room > 0",
                         verdict="pass" if ok else "fail", rule="rule 21"))
    tol_u = sum(USB_TOL)
    d_max = USB_FACE_DEPTH + tol_u
    ok = d_max <= USB_OVERMOLD_LEN_MIN
    rows.append(dict(id=f"A{len(rows) + 1}", item="micro-USB: plug fully seated through the O1 shroud",
                     value=f"receptacle face {USB_FACE_DEPTH * 1e3 - tol_u * 1e3:.1f} to {d_max * 1e3:.1f} mm behind the outer face; "
                           "shroud keeps 12.6 x 10.6 mm to the receptacle face plane",
                     allowance="overmold (10.6 x 8.5 mm) enters up to its 8.0 mm length; S5b radial clearance held over the depth",
                     verdict="pass" if ok else "fail", rule="rule O1 (shroud end flange at the receptacle face plane)"))
    tol_e = sum(ENC_Z_TOL)
    need = ENC_GAP_BODY_TO_WALL + WALL + WASHER + NUT
    for length, label in ((BUSHING_LEN_SHORT, "7 mm bushing"), (BUSHING_LEN_RULE, "9 mm bushing (rule 22)")):
        spare = length - need - tol_e
        rows.append(dict(id=f"A{len(rows) + 1}", item=f"encoder bushing thread engagement through the front wall, {label}",
                         value=f"thread beyond a fully engaged nut: {spare * 1e3:.2f} mm worst case "
                               f"(needs {need * 1e3:.1f} mm plus {tol_e * 1e3:.1f} mm of stack)",
                         allowance=">= 0 mm (full nut engagement at the worst case)",
                         verdict="pass" if spare >= 0 else "fail",
                         rule="rule 22 (bushing >= 9 mm; inner jam nut set to the wall at assembly)"))
    return rows


EXPECTED_DROP = {  # verdict by case, at 2000 g
    "unit on the guard frame": "pass", "heat sink on its pocket ledges": "pass", "cells on the back-shell ribs": "pass",
    "board and holders on the boss tops": "pass", "unit on the front face": "pass",
    "heat sink toward the board, no post (revision 0)": "fail",
    "heat sink toward the board, two posts (rule 18)": "pass", "posts under the heat-sink load (rule 18)": "pass",
    "cells and holders toward the board, no post (revision 0)": "fail",
    "cells and holders, four posts (rule 18)": "pass", "board pulls on the inserts": "pass",
    "display glass on its pocket floor": "pass", "cells sideways on the rib pairs": "pass",
    "board and holders in-plane on the bosses, plain bosses (revision 0)": "fail",
    "board and holders in-plane, gusseted bosses (rule 20)": "pass",
    "whip fitted, corner impact: moment on the port block, pocket bearing": "pass",
    "whip fitted, corner impact: moment on the port block, screws alone": "pass",
    "end-on, connector strikes first: block on its pocket (revision 0)": "not shown",
    "end-on: block with its 20 x 20 mm flange (rule 6)": "pass",
    "cells along X on the holder end walls and end ribs (rule 19)": "pass",
}
EXPECTED_AXIAL = ["pass", "pass", "pass", "fail", "pass"]


def plot(drows, arows):
    import textwrap
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(18, 8.6), gridspec_kw=dict(width_ratios=[1.35, 1]))
    y = list(range(len(drows)))[::-1]
    col = {"pass": "#548235", "not shown": "#bf9000", "fail": "#c00000"}
    for yi, r in zip(y, drows):
        a1.barh(yi, min(r["margin_2000g"], 12), color=col[r["verdict"]], hatch="//" if r["design"] == "rev0" else None,
                edgecolor="k", lw=0.4)
        a1.plot(min(r["margin_1000g"], 12), yi, "D", color="white", mec="k", ms=5)
        a1.text(min(r["margin_2000g"], 12) + 0.15, yi, f"{r['margin_2000g']:.2f}" + (" (off scale)" if r["margin_2000g"] > 12 else ""),
                va="center", fontsize=7.5)
    a1.axvline(PASS_MARGIN, color="k", ls="--", lw=1)
    a1.axvline(1.0, color="#c00000", ls=":", lw=1)
    a1.set_yticks(y)
    a1.set_yticklabels([f"{r['id']} {r['face']}: " + textwrap.shorten(r["case"], 58, placeholder="...") for r in drows],
                       fontsize=7.3)
    a1.set_xlim(0, 13)
    a1.set_xlabel("margin = capacity / load at 2000 g (bar) and 1000 g (diamond); dashed: 1.5 (TS-011 M2 rule)")
    a1.set_title("REQ-SYS-116 drop, 1.0 m, per face and load path (C1, 0.375 kg)\n"
                 "hatched: revision 0 design; plain: revision 1 rule or unchanged path", fontsize=10)
    a1.grid(axis="x", alpha=0.3)
    a2.axis("off")
    txt = "REQ-SYS-108 axial stacks and encoder thread engagement\n\n"
    for r in arows:
        body = textwrap.fill(f"{r['item']}. {r['value']}.", 70, initial_indent="   ", subsequent_indent="   ")
        txt += f"{r['id']} {r['verdict'].upper()} ({r['rule']})\n{body}\n\n"
    a2.text(0.02, 1.0, txt, va="top", fontsize=8.0, family="monospace")
    fig.text(0.01, 0.01, "Planning capacities (Low); developer evidence; docs/design/analysis/mechanical-tolerance-stack.md revision 1.",
             fontsize=8)
    fig.subplots_adjust(left=0.235, right=0.99, top=0.92, bottom=0.08, wspace=0.08)
    PNG.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(PNG, dpi=115)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    drows, arows = drop_rows(), axial_rows()
    CSV.parent.mkdir(parents=True, exist_ok=True)
    with CSV.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(drows[0].keys()))
        w.writeheader()
        w.writerows(drows)
        fh.write("\n")
        w2 = csv.DictWriter(fh, fieldnames=list(arows[0].keys()))
        w2.writeheader()
        w2.writerows(arows)
    plot(drows, arows)
    for r in drows:
        print(f"{r['id']} {r['face']:14s} {r['case'][:70]:70s} load {r['load_1000g']}/{r['load_2000g']} {r['unit']} "
              f"cap {r['capacity']} margin {r['margin_1000g']}/{r['margin_2000g']} {r['verdict']}")
    for r in arows:
        print(f"{r['id']} {r['item']}: {r['value']} -> {r['verdict']}")
    errs = [f"{r['case']}: got {r['verdict']}, expected {EXPECTED_DROP.get(r['case'])}" for r in drows
            if EXPECTED_DROP.get(r["case"]) != r["verdict"]]
    errs += [f"{r['id']}: got {r['verdict']}, expected {e}" for r, e in zip(arows, EXPECTED_AXIAL) if r["verdict"] != e]
    if args.check:
        for e in errs:
            print("MISMATCH:", e)
        print("CHECK", "FAIL" if errs else "PASS")
        return 1 if errs else 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
