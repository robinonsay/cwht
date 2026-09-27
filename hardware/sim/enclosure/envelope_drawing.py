#!/usr/bin/env python3
"""Board outline and envelope drawing with geometric checks (TS-011, TS-004; WP-PDR-27).

Reads hardware/enclosure/board-outline.json, renders
docs/reviews/PDR/figures/board-outline-envelope.png (back view and X-Z section) and asserts:
  E1 the board fits inside the option C inner outline with at least 1.5 mm clearance;
  E2 the Z stack is contiguous and ends at the case outer thickness; case plus heatsink
     protrusion is within the REQ-SYS-103 40 mm (TBR);
  E3 the heatsink footprint clears every boss keep-out and the holder keep-out;
  E4 the PA thermal pad lies inside the heatsink footprint;
  E5 the test finger (12 mm, TBR) entering a guard slot does not reach the fin tips;
  E6 the heatsink height fits between the gap pad and the protrusion allowance.
Run: .venv/bin/python hardware/sim/enclosure/envelope_drawing.py [--check]
--check exits 1 on any failed assertion. Developer evidence (matplotlib, class B, no TV record).
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Circle, Rectangle  # noqa: E402

ROOT = Path(__file__).resolve().parents[3]
SRC = ROOT / "hardware/enclosure/board-outline.json"
PNG = ROOT / "docs/reviews/PDR/figures/board-outline-envelope.png"
FINGER_D = 12.0     # mm, REQ-SYS-113 test finger (TBR)
GAP_PAD_COMPRESSED = 0.375  # mm, 0.5 mm pad at 25 % compression


def finger_penetration(slot_w: float, d: float = FINGER_D) -> float:
    r = d / 2
    if slot_w >= d:
        return math.inf
    return r - math.sqrt(r * r - (slot_w / 2) ** 2)


def rect_circle_clear(rx, ry, cx, cy, rad) -> bool:
    nx = min(max(cx, rx[0]), rx[1])
    ny = min(max(cy, ry[0]), ry[1])
    return math.hypot(cx - nx, cy - ny) >= rad


def checks(d: dict) -> list[tuple[str, bool, str]]:
    out = []
    env = d["envelope"]
    wall = env["wall_thickness_printed"]
    lx, ly, lz = env["option_c_case_outer"]
    bx, by = d["board"]["outline"]
    ox, oy, _ = d["board"]["origin_in_enclosure"]
    cx_lo, cx_hi = ox - wall, (lx - wall) - (ox + bx)
    cy_lo, cy_hi = oy - wall, (ly - wall) - (oy + by)
    cmin = min(cx_lo, cx_hi, cy_lo, cy_hi)
    out.append(("E1 board clearance to inner wall >= 1.5 mm", cmin >= 1.5, f"min {cmin:.2f} mm"))
    zs = d["z_stack"]
    contiguous = all(abs(zs[i]["z1"] - zs[i + 1]["z0"]) < 1e-9 for i in range(len(zs) - 1))
    total = lz + env["heatsink_protrusion_allowance_z"]
    ok2 = contiguous and abs(zs[-1]["z1"] - lz) < 1e-9 and zs[0]["z0"] == 0.0 and total <= 40.0
    out.append(("E2 Z stack contiguous, case + protrusion <= 40 mm", ok2, f"case {lz} + {env['heatsink_protrusion_allowance_z']} = {total} mm"))
    hs = d["heatsink"]
    hx = [hs["position_x_y_in_board_frame"][0], hs["position_x_y_in_board_frame"][0] + hs["footprint"][0]]
    hy = [hs["position_x_y_in_board_frame"][1], hs["position_x_y_in_board_frame"][1] + hs["footprint"][1]]
    rad = d["mounting"]["boss_diameter_bottom_keepout"] / 2
    boss_ok = all(rect_circle_clear(hx, hy, h[0], h[1], rad) for h in d["mounting"]["holes"])
    hold = d["keepouts_bottom"][0]
    hold_ok = hx[0] >= hold["x"][1] or hx[1] <= hold["x"][0]
    out.append(("E3 heatsink clears bosses and holders", boss_ok and hold_ok, f"heatsink x {hx}, y {hy}"))
    pad = d["keepouts_bottom"][2]
    pad_ok = hx[0] <= pad["x"][0] and pad["x"][1] <= hx[1] and hy[0] <= pad["y"][0] and pad["y"][1] <= hy[1]
    out.append(("E4 PA pad inside heatsink footprint", pad_ok, f"pad x {pad['x']}, y {pad['y']}"))
    pen = finger_penetration(6.0)
    rec = hs["fin_tip_recess_behind_guard_min"]
    out.append(("E5 finger through 6.0 mm slot does not reach fins", pen < rec, f"penetration {pen:.2f} mm < recess {rec} mm"))
    z_board_bottom = d["board"]["origin_in_enclosure"][2]
    avail = z_board_bottom - GAP_PAD_COMPRESSED + env["heatsink_protrusion_allowance_z"] - rec - hs["guard_thickness"]
    out.append(("E6 heatsink height fits", hs["overall_height_max"] <= avail, f"{hs['overall_height_max']} <= {avail:.2f} mm"))
    return out


def draw(d: dict, results) -> None:
    env = d["envelope"]
    lx, ly, lz = env["option_c_case_outer"]
    wall = env["wall_thickness_printed"]
    ox, oy, oz = d["board"]["origin_in_enclosure"]
    bx, by = d["board"]["outline"]
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(12, 10.5), gridspec_kw=dict(height_ratios=[1.05, 1]))
    # back view: looking at the back face (from -Z); X to the right, Y up
    a1.add_patch(Rectangle((0, 0), lx, ly, fill=False, lw=2, ec="k"))
    a1.add_patch(Rectangle((wall, wall), lx - 2 * wall, ly - 2 * wall, fill=False, lw=1, ec="k", ls="--"))
    a1.add_patch(Rectangle((ox, oy), bx, by, fc="#dfe9d6", ec="#3a6b1f", lw=1.5))
    hold = d["keepouts_bottom"][0]
    a1.add_patch(Rectangle((ox + hold["x"][0], oy + hold["y"][0]), hold["x"][1] - hold["x"][0], hold["y"][1] - hold["y"][0],
                           fc="#9dc3e6", ec="#1f4e79", alpha=0.8))
    a1.text(ox + 40, oy + 31, "cell holders, 2 x Keystone 1043P\n(bottom side, 14.86 mm)", ha="center", va="center", fontsize=9)
    hs = d["heatsink"]
    hx0, hy0 = hs["position_x_y_in_board_frame"]
    a1.add_patch(Rectangle((ox + hx0, oy + hy0), hs["footprint"][0], hs["footprint"][1], fc="#bfbfbf", ec="#404040", hatch="||",
                           alpha=0.8))
    a1.text(ox + hx0 + hs["footprint"][0] / 2, oy + 52, f"heatsink {hs['footprint'][0]:.0f} x {hs['footprint'][1]:.0f}\n<= 5.5 K/W in situ",
            ha="center", fontsize=8.5, bbox=dict(fc="white", ec="none", alpha=0.85))
    pad = d["keepouts_bottom"][2]
    a1.add_patch(Rectangle((ox + pad["x"][0], oy + pad["y"][0]), 15, 15, fc="#f4b183", ec="#c55a11", lw=1.5))
    a1.text(ox + 100, oy + 31, "PA pad\n15 x 15", ha="center", va="center", fontsize=8)
    for hx, hy in d["mounting"]["holes"]:
        a1.add_patch(Circle((ox + hx, oy + hy), d["mounting"]["boss_diameter_bottom_keepout"] / 2, fc="#ffe699", ec="#7f6000"))
        a1.add_patch(Circle((ox + hx, oy + hy), 1.6, fc="white", ec="k"))
    a1.add_patch(Rectangle((lx - wall - 10, 25), 12, 20, fc="#a5a5a5", ec="k"))
    a1.text(lx + 1.5, 35, "SMA\n(+X end)", va="center", fontsize=8.5)
    a1.text(-1.5, 35, "KEY, USB,\nPHONES\n(-X end)", va="center", ha="right", fontsize=8.5)
    a1.annotate(f"board {bx:.0f} x {by:.0f} x {d['board']['thickness']} mm (TS-004)", xy=(ox + 2, oy + by - 2), xytext=(10, 76),
                fontsize=9, arrowprops=dict(arrowstyle="->", lw=0.8))
    a1.text(0, -7, f"case outer {lx:.0f} x {ly:.0f} x {lz:.0f} mm (REQ-SYS-103: 140 x 70 x 40 TBR); wall {wall} mm; "
            "yellow: M3 bosses (6)", fontsize=9)
    a1.set_xlim(-22, lx + 16)
    a1.set_ylim(-10, 82)
    a1.set_aspect("equal")
    a1.set_title("Plan (X-Y projection, Y up): board outline, bottom-side keep-outs, bosses, heatsink")
    a1.set_xlabel("X, mm")
    a1.set_ylabel("Y, mm")
    # section X-Z at Y = 35
    a2.add_patch(Rectangle((0, 0), lx, lz, fill=False, lw=2, ec="k"))
    for z in d["z_stack"]:
        a2.axhline(z["z0"], color="grey", lw=0.4, ls=":")
    a2.add_patch(Rectangle((ox, oz), bx, d["board"]["thickness"], fc="#3a6b1f"))
    a2.add_patch(Rectangle((ox + hold["x"][0], oz - hold["z_below_board"]), hold["x"][1] - hold["x"][0], hold["z_below_board"],
                           fc="#9dc3e6", ec="#1f4e79"))
    base_top = oz - GAP_PAD_COMPRESSED
    hz = hs["overall_height_max"]
    a2.add_patch(Rectangle((ox + hx0, base_top - hs["base_thickness_min"]), hs["footprint"][0], hs["base_thickness_min"],
                           fc="#7f7f7f"))
    a2.add_patch(Rectangle((ox + hx0, base_top - hz), hs["footprint"][0], hz - hs["base_thickness_min"], fc="#d0d0d0",
                           ec="#404040", hatch="--"))
    a2.text(ox + hx0 + hs["footprint"][0] / 2, base_top - hz / 2, "fins, parallel to X", ha="center", fontsize=8,
            bbox=dict(fc="white", ec="none", alpha=0.8))
    guard_z = base_top - hz - hs["fin_tip_recess_behind_guard_min"]
    gt = hs["guard_thickness"]
    a2.add_patch(Rectangle((ox + hx0 - 4, guard_z - gt), hs["footprint"][0] + 8, gt, fc="#f8cbad", ec="#c55a11", hatch=".."))
    a2.plot([ox + hx0 - 4, ox + hx0 - 4], [guard_z - gt, 0], color="#c55a11", lw=1.5)
    a2.plot([ox + hx0 + hs["footprint"][0] + 4] * 2, [guard_z - gt, 0], color="#c55a11", lw=1.5)
    a2.text(ox + hx0 + hs["footprint"][0] / 2, guard_z - gt - 3.5, "printed guard frame and grille, 6 mm slots", ha="center",
            fontsize=8)
    a2.axhline(-env["heatsink_protrusion_allowance_z"], color="k", lw=0.8, ls="--")
    a2.text(2, -env["heatsink_protrusion_allowance_z"] - 3, "REQ-SYS-103 envelope limit (40 mm from the front face)", fontsize=8)
    a2.add_patch(Rectangle((lx - wall - 10, 19.5), 12, 8.5, fc="#a5a5a5", ec="k"))
    a2.plot([lx, lx + 12], [23.5, 23.5], color="k", lw=4)
    a2.text(lx + 1, 26, "SMA", fontsize=8.5)
    a2.add_patch(Rectangle((wall, 19.9), 10, 4, fc="#d9d9d9", ec="k"))
    a2.text(wall + 11, 21.2, "jacks and USB at -X end", fontsize=8)
    for z in d["z_stack"]:
        a2.text(lx + 14, (z["z0"] + z["z1"]) / 2, f"{z['z0']:.1f} to {z['z1']:.1f}: {z['layer'].split(' (')[0]}", fontsize=7.5,
                va="center")
    a2.set_xlim(-5, lx + 75)
    a2.set_ylim(guard_z - 10, lz + 4)
    a2.set_aspect("equal")
    a2.set_title("Section X-Z at Y = 35 mm (option C): Z stack, holders, heatsink behind the guard, port block")
    a2.set_xlabel("X, mm")
    a2.set_ylabel("Z, mm")
    txt = "; ".join(f"{name.split(' ')[0]} {'PASS' if ok else 'FAIL'}" for name, ok, _ in results)
    fig.text(0.01, 0.005, "Checks: " + txt + ". Source hardware/enclosure/board-outline.json. Draft, AT RISK (CR-003, CR-006).",
             fontsize=8.5)
    fig.tight_layout(rect=(0, 0.02, 1, 1))
    PNG.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(PNG, dpi=120)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    d = json.loads(SRC.read_text())
    results = checks(d)
    draw(d, results)
    for name, ok, detail in results:
        print(f"{'PASS' if ok else 'FAIL'}  {name}: {detail}")
    bad = [r for r in results if not r[1]]
    if args.check:
        print("CHECK", "FAIL" if bad else "PASS")
        return 1 if bad else 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
