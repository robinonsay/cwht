#!/usr/bin/env python3
"""TS-011 thermal screen: first-cut PA heat path per enclosure alternative.

Purpose: mandatory screening rows M4 (REQ-SYS-112, REQ-SYS-113) and M8 (printed-part
heat-deflection margin) of docs/decisions/trade-studies/TS-011-enclosure.md, and the
TS-004 thickness screen. This is the TS-011 author's screen, not the thermal budget:
docs/design/analysis/thermal-budget.md (WP-PDR-28a and 28b) supersedes every number.

Model: lumped thermal network. Junction to the heat-entry point of the enclosure part
through RthJC, the via array (TS-004 thickness), plane spreading and the gap pad; the
enclosure part is one capacitive node to ambient; printed guard and printed rim nodes are
coupled to it where the alternative has them. Inputs and sources are in INPUTS below and in
TS-011 Appendix A. Output is developer evidence (numpy and matplotlib have no TV record of
their own; tools/toolchain.lock.md section 2, class B).

Run:  .venv/bin/python hardware/sim/enclosure/thermal_screen.py [--check]
Writes: hardware/sim/enclosure/out/thermal-screen.csv and
        docs/reviews/PDR/figures/ts011-thermal-screen.png
--check exits 1 when a verdict differs from EXPECTED (the values stated in TS-011).
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

ROOT = Path(__file__).resolve().parents[3]
OUT_CSV = ROOT / "hardware/sim/enclosure/out/thermal-screen.csv"
OUT_PNG = ROOT / "docs/reviews/PDR/figures/ts011-thermal-screen.png"

# ---------------------------------------------------------------- inputs
P_WORST = 4.1      # W, PD54008L-E at 5 W out, 55 % drain efficiency (TS-001 M5 row: 3.1 to 4.1 W)
P_NOM = 3.33       # W, 60 % efficiency (pcbway-export-and-vendor-questions.md F17)
RTH_JC = 3.0       # K/W, PD54008L-E (TS-001 P1 M5 row, 3 C/W)
R_VIA = {1.0: 4.7, 1.2: 5.7, 1.6: 7.6}  # K/W, 25 vias 0.30 mm, 25 um wall (F16; 1.2 mm scaled by length)
R_PLANE = 1.0      # K/W, plane spreading (F17)
R_PAD = 0.74       # K/W, 0.5 mm gap pad, 3 W/mK, 15 x 15 mm (F18)
T_SURF_LIMIT = 48.0   # C, REQ-SYS-113 (TBR, owner limit SI-039)
T_J_LIMIT = 110.0     # C, REQ-SYS-112 (TBR)
T_AMB_113 = 25.0      # C, REQ-SYS-113 condition
T_AMB_112 = 45.0      # C, REQ-SYS-112 condition
T_KEYDOWN = 300.0     # s, REQ-SYS-113: 5 min continuous key-down
HDT_PETG = 69.0       # C, PETG heat-deflection temperature at 0.45 MPa, typical datasheet value (Low; owner fetches the filament TDS)
HDT_MARGIN = 5.0      # K, M8 pass rule of TS-011
T_STORE = 60.0        # C, REQ-SYS-115 storage upper bound (TBR)
C_AL = 0.896          # J/(g K), aluminum
C_PETG = 1.2          # J/(g K), PETG (Low)

# Alternatives: enclosure node to ambient (K/W), node heat capacity (J/K), spreading from the
# pad to the node (K/W), board thickness (mm), printed parts coupled to the hot node.
ALTS = {
    "A": dict(label="A CNC 6061 box (fallback)", r_amb=2.6, cap=157 * C_AL, r_spread=0.5, board=1.0,
              printed=False, guard=None, rim=None),
    "B": dict(label="B catalog extrusion + PCB plates", r_amb=2.9, cap=110 * C_AL, r_spread=0.8, board=1.6,
              printed=False, guard=None, rim=None),
    "C1": dict(label="C1 PETG case, guarded fin heatsink", r_amb=5.5, cap=50 * C_AL, r_spread=0.3, board=1.0,
               printed=True, guard=dict(g_hot=0.016, g_amb=0.030, cap=5 * C_PETG),
               rim=dict(g_hot=0.020, g_amb=0.040, cap=10 * C_PETG)),
    "C1e": dict(label="C1e variant: C1 with the fins exposed", r_amb=5.0, cap=50 * C_AL, r_spread=0.3,
                board=1.0, printed=True, guard=None, rim=dict(g_hot=0.020, g_amb=0.040, cap=10 * C_PETG)),
    "C2": dict(label="C2 PETG case, internal heatsink", r_amb=10.9, cap=60 * C_AL, r_spread=0.3, board=1.0,
               printed=True, guard=None, rim=dict(g_hot=0.25, g_amb=0.06, cap=10 * C_PETG)),
    "C3": dict(label="C3 PETG case, flat Al back plate", r_amb=8.5, cap=79 * C_AL, r_spread=1.5, board=1.0,
               printed=True, guard=None, rim=dict(g_hot=0.020, g_amb=0.040, cap=10 * C_PETG)),
    # D: the board is held by the printed face, the PA pad presses on the extrusion floor through a 1.0 mm gap
    # pad (stack +/-0.5 mm, mechanical-tolerance-stack.md S6 class): r_iface adds 0.74 K/W to the junction chain.
    "D": dict(label="D extruded body + printed face and ends", r_amb=3.3, cap=90 * C_AL, r_spread=0.8, r_iface=0.74, board=1.0,
              printed=True, guard=None, rim=dict(g_hot=1.0, g_amb=0.02, cap=10 * C_PETG)),
}
# Which node is accessible (REQ-SYS-113 set): the hot node itself unless a guard hides it.
ACCESSIBLE_HOT = {"A": True, "B": True, "C1": False, "C1e": True, "C2": False, "C3": True, "D": True}
# C2: the accessible face is the PETG wall over the internal heatsink: the rim node models it.

EXPECTED = {  # verdicts stated in TS-011 section 4 (M4 and M8) and TS-004 section 4
    "A": dict(m4_113=True, m4_112=True, m8=None),
    "B": dict(m4_113=True, m4_112=False, m8=None),
    "C1": dict(m4_113=True, m4_112=True, m8=True),
    "C1e": dict(m4_113=True, m4_112=True, m8=True),
    "C2": dict(m4_113=True, m4_112=False, m8=False),
    "C3": dict(m4_113=True, m4_112=False, m8=True),
    "D": dict(m4_113=True, m4_112=True, m8=True),
}
EXPECTED_TS004 = {1.0: True, 1.2: False, 1.6: False}  # C1 path, 4.1 W, REQ-SYS-112


def r_junction_to_entry(board: float) -> float:
    return RTH_JC + R_VIA[board] + R_PLANE + R_PAD


def simulate(alt: dict, power: float, t_amb: float, t_end: float, dt: float = 0.5):
    """Explicit Euler on the hot node plus optional guard and rim nodes. Returns time series."""
    g_amb = 1.0 / alt["r_amb"]
    t_hot = t_g = t_r = t_amb
    ts, hot, guard, rim = [], [], [], []
    t = 0.0
    while t <= t_end + 1e-9:
        ts.append(t)
        hot.append(t_hot + power * alt["r_spread"])  # heat-entry end of the hot part
        guard.append(t_g)
        rim.append(t_r)
        q_out = g_amb * (t_hot - t_amb)
        q_g = q_r = 0.0
        if alt["guard"]:
            gd = alt["guard"]
            q_g = gd["g_hot"] * (t_hot - t_g)
            t_g += dt * (q_g - gd["g_amb"] * (t_g - t_amb)) / gd["cap"]
        if alt["rim"]:
            rm = alt["rim"]
            q_r = rm["g_hot"] * (t_hot - t_r)
            t_r += dt * (q_r - rm["g_amb"] * (t_r - t_amb)) / rm["cap"]
        # Guard and rim are observers: r_amb is the whole in-situ path, so the heat they draw is
        # not credited to the hot node (conservative for the junction and for the printed parts).
        t_hot += dt * (power - q_out) / alt["cap"]
        t += dt
    return ts, hot, guard, rim


def steady(alt: dict, power: float, t_amb: float):
    """Steady state of the hot node, junction, and printed nodes (rim is the printed contact)."""
    rise = power * alt["r_amb"]  # guard and rim are observers (see simulate)
    t_hot = t_amb + rise
    t_entry = t_hot + power * alt["r_spread"]
    t_j = t_entry + power * (r_junction_to_entry(alt["board"]) + alt.get("r_iface", 0.0))
    t_print = None
    if alt["rim"]:
        rm = alt["rim"]
        t_print = t_amb + rise * rm["g_hot"] / (rm["g_hot"] + rm["g_amb"])
    if alt["guard"]:
        gd = alt["guard"]
        t_guard = t_amb + rise * gd["g_hot"] / (gd["g_hot"] + gd["g_amb"])
        t_print = max(t_print or t_guard, t_guard)
    return t_hot, t_entry, t_j, t_print


def evaluate():
    rows, series = [], {}
    for key, alt in ALTS.items():
        ts, hot, guard, rim = simulate(alt, P_WORST, T_AMB_113, 900.0)
        i5 = ts.index(T_KEYDOWN)
        acc = []
        if ACCESSIBLE_HOT[key]:
            acc.append(hot[i5])
        if alt["guard"]:
            acc.append(guard[i5])
        if alt["rim"]:
            acc.append(rim[i5])
        t_acc5 = max(acc)
        _, _, tj_w, t_print = steady(alt, P_WORST, T_AMB_112)
        _, _, tj_n, _ = steady(alt, P_NOM, T_AMB_112)
        m8 = None
        margin_oper = margin_store = None
        if alt["printed"]:
            margin_oper = HDT_PETG - t_print
            margin_store = HDT_PETG - T_STORE
            m8 = min(margin_oper, margin_store) >= HDT_MARGIN
        rows.append(dict(
            alt=key, label=alt["label"], board_mm=alt["board"],
            t_access_5min_c=round(t_acc5, 1), margin_113_k=round(T_SURF_LIMIT - t_acc5, 1),
            tj_45c_worst_c=round(tj_w, 1), tj_45c_nom_c=round(tj_n, 1),
            margin_112_k=round(T_J_LIMIT - tj_w, 1),
            t_printed_peak_c=None if t_print is None else round(t_print, 1),
            hdt_margin_oper_k=None if margin_oper is None else round(margin_oper, 1),
            hdt_margin_store_k=None if margin_store is None else round(margin_store, 1),
            m4_113=t_acc5 <= T_SURF_LIMIT, m4_112=tj_w <= T_J_LIMIT, m8=m8,
        ))
        series[key] = (ts, [max(v) for v in zip(*(
            ([hot] if ACCESSIBLE_HOT[key] else []) + ([guard] if alt["guard"] else []) + ([rim] if alt["rim"] else [])
        ))])
    ts004 = {}
    c1 = dict(ALTS["C1"])
    for board in (1.0, 1.2, 1.6):
        c1["board"] = board
        _, _, tj, _ = steady(c1, P_WORST, T_AMB_112)
        ts004[board] = round(tj, 1)
    return rows, series, ts004


def write_csv(rows):
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)


def plot(rows, series, ts004):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.2), gridspec_kw=dict(width_ratios=[1.35, 1]))
    colors = {"A": "#1f4e79", "B": "#6b8e23", "C1": "#c0504d", "C1e": "#f08080", "C2": "#e69f00", "C3": "#8064a2", "D": "#4bacc6"}
    for key, (ts, acc) in series.items():
        ax1.plot([t / 60 for t in ts], acc, color=colors[key], lw=2, label=ALTS[key]["label"])
    ax1.axhline(T_SURF_LIMIT, color="k", ls="--", lw=1)
    ax1.text(14.8, T_SURF_LIMIT + 0.4, "REQ-SYS-113: 48 C (TBR)", fontsize=9, ha="right")
    ax1.axvline(T_KEYDOWN / 60, color="grey", ls=":", lw=1)
    ax1.text(T_KEYDOWN / 60 + 0.1, 26, "5 min", fontsize=9, color="grey")
    ax1.set_xlabel("time from key-down, min (25 C ambient, 4.1 W)")
    ax1.set_ylabel("hottest accessible face, C")
    ax1.set_title("REQ-SYS-113 screen: hottest accessible face")
    ax1.set_xlim(0, 15)
    ax1.grid(alpha=0.3)
    ax1.set_ylim(24, 62)
    ax1.legend(fontsize=8, loc="upper left", ncol=2)
    keys = [r["alt"] for r in rows]
    tj = [r["tj_45c_worst_c"] for r in rows]
    bars = ax2.bar(keys, tj, color=[colors[k] for k in keys])
    for b, v in zip(bars, tj):
        ax2.text(b.get_x() + b.get_width() / 2, v - 9, f"{v:.0f}", ha="center", fontsize=9, color="white",
                 weight="bold")
    ax2.axhline(T_J_LIMIT, color="k", ls="--", lw=1)
    ax2.text(-0.45, 141, "dashed: REQ-SYS-112 limit 110 C (TBR)", fontsize=9, ha="left")
    ax2.set_ylim(0, 150)
    ax2.set_ylabel("PA junction, steady, C")
    ax2.set_title("REQ-SYS-112 screen: 45 C ambient, 4.1 W, continuous")
    ax2.grid(axis="y", alpha=0.3)
    note = "TS-004 (C1 path): Tj = " + ", ".join(f"{t} C at {b} mm" for b, t in ts004.items())
    fig.text(0.01, 0.01, note + ". Author screen, developer evidence; superseded by WP-PDR-28.", fontsize=8)
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    OUT_PNG.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT_PNG, dpi=130)


def check(rows, ts004) -> list[str]:
    errs = []
    for r in rows:
        exp = EXPECTED[r["alt"]]
        for k, v in exp.items():
            if r[k] != v:
                errs.append(f"{r['alt']} {k}: got {r[k]}, expected {v}")
    for b, ok in EXPECTED_TS004.items():
        if (ts004[b] <= T_J_LIMIT) != ok:
            errs.append(f"TS-004 {b} mm: Tj {ts004[b]} C, expected pass={ok}")
    return errs


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    rows, series, ts004 = evaluate()
    write_csv(rows)
    plot(rows, series, ts004)
    for r in rows:
        print(r)
    print("TS-004 C1 path Tj at 45 C, 4.1 W:", ts004)
    print("C1 sensitivity, steady Tj at 45 C by in-situ heatsink resistance (K/W):")
    for r_hs in (4.5, 5.5, 6.5, 7.5, 8.5):
        alt = dict(ALTS["C1"], r_amb=r_hs)
        vals = [round(steady(alt, pw, T_AMB_112)[2], 1) for pw in (P_WORST, P_NOM, 0.8 * P_WORST)]
        print(f"  R_hs {r_hs}: 4.1 W continuous {vals[0]} C; 3.33 W continuous {vals[1]} C; 80 % duty of 4.1 W {vals[2]} C")
    errs = check(rows, ts004)
    if args.check:
        for e in errs:
            print("MISMATCH:", e)
        print("CHECK", "FAIL" if errs else "PASS")
        return 1 if errs else 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
