#!/usr/bin/env python3
"""TS-011 revision 1 thermal conditions (INSP-081 finding-1 and finding-2, INSP-087 finding-1).

Purpose. Four computations that the TS-011 revision 1 mandatory screen rests on, beside the
iteration 1 screen `thermal_screen.py` (unchanged, whose chain constants are imported here so both
use one set of values):

1. M4 heat-sink threshold (INSP-081 finding-1): the in-situ heat-sink resistance at which option
   C1 meets REQ-SYS-112 (110 C TBR at 45 C, 4.1 W, continuous key-down), and the resistances
   behind the C3 enhancing scores.
2. Guard derating (INSP-081 finding-1 item 4): a stated model that turns a catalog natural-
   convection resistance into the in-situ value behind the printed guard, replacing the unsourced
   1 K/W penalty of TS-011 revision 0 section 8 rule 3.
3. K9 trip (INSP-087 finding-1): the junction temperature at which the firmware-independent
   cut-off of REQ-SYS-181 (95 C +/-3 C) acts, for a sensor at the PA thermal pad and for one on
   the heat sink, per surviving option.
4. M8 boss and wall temperatures (INSP-081 finding-2): a two-layer finite-difference model of the
   130 x 62 mm board (top and bottom copper sheets, 1 mm cells) at the REQ-SYS-112 condition,
   which bounds the printed boss temperature at the six mounting holes and the printed wall
   facing the board, for C1 and D, and the filament heat-deflection temperature at which M8 passes
   (TS-011 revision 1 section 8 rule 15). A PA66 standoff variant that isolates the bosses is also
   computed; it is not adopted, because the printed walls still fail M8 with PETG.

Model of item 4. The PA pad regions (15 x 15 mm, top and bottom) are isothermal nodes tied by the
lumped chain of the iteration 1 screen (RthJC 3.0, via array 4.7, plane 1.0, gap pad 0.74, spread
0.3 K/W), so with no lateral loss the model reproduces the screen. Around them the two copper
sheets conduct laterally, couple to each other through the laminate and lose heat to the enclosure
inside (board-to-wall coefficient h_in) and, under C1, to the heat-sink base across the 0.4 mm air
gap. The inside wall node reaches ambient through the printed wall. Other board dissipation
(driver, bias, converters) is spread uniformly on the top sheet. Every uncertain input is swept and
the maximum over the sweep is the bound that M8 uses. Making the pad regions isothermal at the
chain temperatures maximises the lateral leak, which is conservative for the bosses and walls.

Output is developer evidence (numpy, scipy and matplotlib have no TV record of their own;
tools/toolchain.lock.md section 2, class B). WP-PDR-28 (thermal budget) supersedes every number.

Run:  .venv/bin/python hardware/sim/enclosure/board_field_thermal.py [--check]
Writes hardware/sim/enclosure/out/board-field-thermal.csv and
       docs/reviews/PDR/figures/ts011-board-field-thermal.png
--check exits 1 when a verdict differs from EXPECTED (the values stated in TS-011 revision 1).
"""
from __future__ import annotations

import argparse
import csv
import itertools
import math
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import scipy.sparse as sp  # noqa: E402
import scipy.sparse.linalg as spla  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
import thermal_screen as ts  # noqa: E402  (iteration 1 screen: chain constants and alternatives)

ROOT = Path(__file__).resolve().parents[3]
OUT_CSV = ROOT / "hardware/sim/enclosure/out/board-field-thermal.csv"
OUT_PNG = ROOT / "docs/reviews/PDR/figures/ts011-board-field-thermal.png"

P = ts.P_WORST
T_AMB = ts.T_AMB_112
TJ_MAX = ts.T_J_LIMIT
HDT = ts.HDT_PETG
M8_RULE = ts.HDT_MARGIN
M8_LIMIT = HDT - M8_RULE  # 64 C: the highest printed-part temperature that passes M8


# ------------------------------------------------------------------ 1. M4 heat-sink threshold
def chain_below_hs(alt: str) -> float:
    """Junction to the heat-sink (or enclosure hot) node, K/W, as the iteration 1 screen."""
    a = ts.ALTS[alt]
    return ts.r_junction_to_entry(a["board"]) + a.get("r_iface", 0.0) + a["r_spread"]


def tj(alt: str, r_hs: float, power: float = P, t_amb: float = T_AMB) -> float:
    return t_amb + power * (chain_below_hs(alt) + r_hs)


def r_hs_for_margin(alt: str, margin_k: float) -> float:
    """In-situ resistance at which the junction is `margin_k` below the REQ-SYS-112 limit."""
    return (TJ_MAX - margin_k - T_AMB) / P - chain_below_hs(alt)


# ------------------------------------------------------------------ 2. guard derating
SIGMA = 5.670e-8
EPS_HS = 0.85            # black anodized aluminum emissivity (typical handbook value, recalled, Low)
HS_DIMS = (0.040, 0.058, 0.023)   # m, footprint x, footprint y, overall height (TS-011 rule 3 envelope)
DS_RISE = 30.0           # K, catalog rating point of TS-011 rule 3 (natural convection, 25 C ambient)
GUARD_SLOT = 6.0         # mm, guard slot width (TS-011 rule 4)
GUARD_RIB = 3.0          # mm, guard rib width (TS-011 revision 1 rule 4, new)
F_CONV = (0.7, 0.8, 0.9)  # fraction of free-air convection kept behind the guard and pocket (Low; swept)


def h_rad(t_s: float, t_a: float, eps: float) -> float:
    ts_k, ta_k = t_s + 273.15, t_a + 273.15
    return eps * SIGMA * (ts_k ** 2 + ta_k ** 2) * (ts_k + ta_k)


def guard_model(r_ds: float, f_conv: float) -> float:
    """In-situ resistance behind the guard from a catalog free-air natural-convection value.

    Free air: the heat sink radiates from its envelope except the base face (the fin-tip face,
    two sides, two ends) and convects the rest. In situ: only the fin-tip face radiates to
    ambient, through the guard's open fraction; the sides and ends face the printed pocket walls
    and get no credit; convection keeps the fraction f_conv of its free-air value."""
    lx, ly, hz = HS_DIMS
    a_env = lx * ly + 2 * (lx * hz) + 2 * (ly * hz)
    a_tip = lx * ly
    hr = h_rad(25.0 + DS_RISE, 25.0, EPS_HS)
    g_rad_free = hr * a_env
    g_conv = 1.0 / r_ds - g_rad_free
    if g_conv <= 0:
        raise ValueError("catalog value below the radiation-only limit")
    phi = GUARD_SLOT / (GUARD_SLOT + GUARD_RIB)
    return 1.0 / (f_conv * g_conv + phi * hr * a_tip)


def r_ds_for_insitu(r_insitu: float, f_conv: float) -> float:
    lo, hi = 0.5, 30.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if guard_model(mid, f_conv) > r_insitu:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


# ------------------------------------------------------------------ 3. K9 trip
K9_T = 95.0
K9_TOL = 3.0
SENSOR_POINTS = {
    # junction-to-sensor resistance, K/W
    "PA thermal pad (top side, next to the device; K9 text of HZ-003)": lambda alt: ts.RTH_JC,
    "heat sink or enclosure hot node (REQ-SYS-181 'heat-sink' reading)": lambda alt: chain_below_hs(alt),
}


def k9_trip(alt: str, point: str) -> tuple[float, float, float]:
    r = SENSOR_POINTS[point](alt)
    return tuple(t + P * r for t in (K9_T - K9_TOL, K9_T, K9_T + K9_TOL))


# ------------------------------------------------------------------ 4. board field model
NX, NY = 130, 62          # 1 mm cells, board frame (hardware/enclosure/board-outline.json)
DX = 1e-3
K_CU = 385.0
T_OUTER = 35e-6           # m, 1 oz outer layers (pcbway-fabrication-and-assembly.md F5)
T_INNER = 35e-6           # m, inner planes taken as 1 oz (upper bound of spreading; 0.5 oz lowers it)
K_FR4_Z = 0.30            # W/(m K), laminate through-thickness (typical, Low)
T_BOARD = 1.0e-3
PAD = ((92, 107), (23, 38))   # cell index ranges of the 15 x 15 mm PA pad (board frame)
HS_FOOT = ((82, 122), (2, 60))  # heat-sink footprint cells (board frame)
HOLES = [(4.0, 4.0), (4.0, 58.0), (78.5, 4.0), (78.5, 58.0), (126.5, 4.0), (126.5, 58.0)]
FRONT_GAP = 9.1e-3        # m, board top to front wall (z 18.9 to 28.0)
BACK_GAP = 15.9e-3        # m, board bottom to back wall outside the heat sink (z 2.0 to 17.9)
PETG_K = 0.20
WALL_T = 2.0e-3
A_OUT_C1 = 0.0364 - 0.040 * 0.058  # m2, case outer area minus the heat-sink opening
A_OUT_D_FACE = 0.0154     # m2, D printed face and end caps (140 x 70 plus two 70 x 40 caps, Low)

# Sweep of the uncertain inputs (each value named in TS-011 revision 1 section 4.1 M8)
SWEEP = dict(
    coverage=(0.6, 0.9),         # copper coverage of each lumped sheet
    h_in=(5.0, 8.0),             # W/(m2 K), board to inner wall, radiation to a coated wall plus gap convection
    h_out=(6.0, 10.0),           # W/(m2 K), outer surface in still air, hand or pocket nearby
    h_gap=(20.0, 70.0),          # W/(m2 K), board bottom to heat-sink base across the 0.4 mm air gap (C1)
    q_rf=(1.0, 2.3),             # W, rest of the TX line-up in the RF section (see Q_RF_BASIS)
)
# Q_RF_BASIS: the REQ-SYS-112 rationale carries the line-up at about 11.4 W DC for 5 W
# (docs/research/pa-device-candidates.md F19, a two-stage line-up): 11.4 - 5.0 RF - 4.1 final = 2.3 W for the
# driver, match, filter and T/R losses, the upper value (Low). 1.0 W is the lower value: a 5 V MMIC driver of
# the TS-001 P1 class at about 0.5 W, plus about 0.5 W of low-pass filter and T/R bias losses
# (docs/research/tr-switch-candidates.md F14: 0.3 to 0.42 W of T/R bias) (Low).
RF_RECT = ((82, 128), (4, 58))      # RF section: the heat-sink footprint and the port end (layout WP-PDR-37)
Q_DIGITAL = 0.3                     # W, Pico 2, receiver and converters, spread over the board (Low)


def idx(layer: int, i: int, j: int) -> int:
    return layer * NX * NY + j * NX + i


def in_rect(i: int, j: int, rect) -> bool:
    (i0, i1), (j0, j1) = rect
    return i0 <= i < i1 and j0 <= j < j1


def solve_board(option: str, r_hs: float, coverage: float, h_in: float, h_out: float, h_gap: float, q_rf: float,
                q_digital: float = Q_DIGITAL, gz_scale: float = 1.0, pocket: bool = True):
    """Steady state of the two-layer board at 45 C ambient, 4.1 W in the PA.

    option "C1": heat-sink node HS under the pad (gap pad chain), heat-sink footprint coupled to
    HS by h_gap, both sides of the board lose to the printed inner wall node W.
    option "D": extrusion node HS under the pad through the 1.0 mm pad; the bottom side loses to
    the extrusion node (metal back and sides), the top side to the printed face node W.
    gz_scale = 0 removes the laminate coupling between the sheets and pocket = False the heat-sink pocket wall
    (both used only by the reproduction check)."""
    n_b = 2 * NX * NY
    J, TP, BP, HS, W = n_b, n_b + 1, n_b + 2, n_b + 3, n_b + 4
    n = n_b + 5
    rows, cols, vals = [], [], []
    rhs = np.zeros(n)
    diag = np.zeros(n)

    def link(a: int, b: int, g: float) -> None:
        rows.extend((a, b))
        cols.extend((b, a))
        vals.extend((-g, -g))
        diag[a] += g
        diag[b] += g

    def to_amb(a: int, g: float) -> None:
        diag[a] += g
        rhs[a] += g * T_AMB

    g_sheet = K_CU * (T_OUTER + T_INNER) * coverage  # W/K between neighbouring square cells
    g_z = K_FR4_Z / T_BOARD * DX * DX * gz_scale
    n_rf = sum(1 for j in range(NY) for i in range(NX) if in_rect(i, j, RF_RECT) and not in_rect(i, j, PAD))
    a_cell = DX * DX
    g_big = 50.0
    for j in range(NY):
        for i in range(NX):
            for layer in (0, 1):
                k = idx(layer, i, j)
                if i + 1 < NX:
                    link(k, idx(layer, i + 1, j), g_sheet)
                if j + 1 < NY:
                    link(k, idx(layer, i, j + 1), g_sheet)
                if in_rect(i, j, PAD):
                    link(k, TP if layer == 0 else BP, g_big)
            link(idx(0, i, j), idx(1, i, j), g_z)
            top, bot = idx(0, i, j), idx(1, i, j)
            if in_rect(i, j, PAD):
                continue
            link(top, W, h_in * a_cell)
            if option == "C1":
                if in_rect(i, j, HS_FOOT):
                    link(bot, HS, h_gap * a_cell)
                else:
                    link(bot, W, h_in * a_cell)
            else:
                link(bot, HS, h_in * a_cell)
            rhs[top] += q_digital / (NX * NY - 225)
            if in_rect(i, j, RF_RECT):
                rhs[top] += q_rf / n_rf
    a = ts.ALTS[option]
    link(J, TP, 1.0 / ts.RTH_JC)
    link(TP, BP, 1.0 / ts.R_VIA[1.0])
    link(BP, HS, 1.0 / (ts.R_PLANE + ts.R_PAD + a.get("r_iface", 0.0) + a["r_spread"]))
    rhs[J] += P
    to_amb(HS, 1.0 / r_hs)
    if option == "C1":
        a_in = A_OUT_C1 - 0.0024  # inner area, Low
        to_amb(W, 1.0 / (WALL_T / (PETG_K * a_in) + 1.0 / (h_out * A_OUT_C1)))
        # printed pocket walls between the heat-sink pocket and the inside: two sides and two ends, 15 mm deep
        a_pocket = 2 * (0.040 + 0.058) * 0.015
        if pocket:
            link(W, HS, 1.0 / (2.0 / (5.0 * a_pocket) + WALL_T / (PETG_K * a_pocket)))
    else:
        to_amb(W, 1.0 / (WALL_T / (PETG_K * A_OUT_D_FACE) + 1.0 / (h_out * A_OUT_D_FACE)))
        link(W, HS, 1.0 / (2.0 / (h_in * 0.004)))  # face-to-extrusion edge contact (end-cap joints, Low)
    rows.extend(range(n))
    cols.extend(range(n))
    vals.extend(diag)
    m = sp.csr_matrix((vals, (rows, cols)), shape=(n, n))
    t = spla.spsolve(m, rhs)
    top = t[:NX * NY].reshape(NY, NX)
    bot = t[NX * NY:n_b].reshape(NY, NX)
    return dict(top=top, bot=bot, tj=t[J], tp=t[TP], bp=t[BP], hs=t[HS], wall=t[W])


def disc_mean(field: np.ndarray, radius_mm: float) -> np.ndarray:
    """Mean of the board field over a disc of the wall gap's radius: the board area a wall element faces."""
    r = int(round(radius_mm))
    yy, xx = np.mgrid[-r:r + 1, -r:r + 1]
    ker = (xx ** 2 + yy ** 2 <= r * r).astype(float)
    ker /= ker.sum()
    pad = np.pad(field, r, mode="edge")
    out = np.zeros_like(field)
    for dy in range(-r, r + 1):
        for dx in range(-r, r + 1):
            w = ker[dy + r, dx + r]
            if w:
                out += w * pad[r + dy:r + dy + field.shape[0], r + dx:r + dx + field.shape[1]]
    return out


def wall_local(board_mean, h_in: float, h_out: float):
    """Local inner-wall temperature facing the board: board-to-wall exchange h_in against the
    conduction through the 2 mm wall and the outer film, with no lateral spreading in the wall
    (an upper bound of the peak; PETG spreads little, sheet conductance 4e-4 W/K)."""
    u_out = 1.0 / (WALL_T / PETG_K + 1.0 / h_out)
    return (h_in * board_mean + u_out * T_AMB) / (h_in + u_out)


# ---- boss models
# Revision 0 (and the iteration 1 screen): the M3 screw head sits on the board copper and the brass
# insert is in a PETG boss that carries the board; the PETG at the insert is at the board temperature at
# the hole (heat flow into the boss is negligible against the board's lateral conduction).
# Standoff variant (evaluated, not adopted; TS-011 revision 1 section 4.1 M8): every board mounting point
# is a PA66 (nylon 66) male-female M3 standoff spanning the board to a heat-set insert in a local 4 mm pad
# of the back wall (no tall printed boss); the steel screw enters the standoff from the board top by at
# most 4 mm, so at least 8 mm of nylon separates the screw from the insert. The insert then sits in the
# back wall, which the outside air cools, and the standoff is the large resistance. It isolates the bosses
# but not the walls, and a 14 mm nylon standoff is weak in the in-plane drop case.
K_PA66 = 0.25                       # W/(m K), recalled typical value (Low)
STANDOFF_AREA = 0.866 * 5.0e-3 ** 2 - math.pi / 4 * 2.5e-3 ** 2  # m2, 5 mm hexagon less a 2.5 mm tap bore
STANDOFF_NYLON = 8.0e-3             # m, nylon between the screw tip and the insert
R_STANDOFF = STANDOFF_NYLON / (K_PA66 * STANDOFF_AREA)
INSERT_RADIUS = 2.3e-3              # m, M3 heat-set insert outer radius
PAD_T = 4.0e-3                      # m, local back-wall pad thickness under the insert


def r_insert_in_wall(h_out: float, h_int: float) -> float:
    """Spreading resistance of a disc (the insert) into a PETG plate of thickness PAD_T with films
    h_out outside and h_int inside: R = K0(a/L) / (2 pi G (a/L) K1(a/L)), L = sqrt(G / (h_out + h_int))."""
    from scipy.special import k0, k1
    g = PETG_K * PAD_T
    ell = math.sqrt(g / (h_out + h_int))
    x = INSERT_RADIUS / ell
    return float(k0(x) / (2 * math.pi * g * x * k1(x)))


def boss_petg_temp(t_board: float, t_inner_wall: float, h_in: float, h_out: float, rule14: bool) -> float:
    if not rule14:
        return t_board
    t_ref = (h_out * T_AMB + h_in * t_inner_wall) / (h_out + h_in)  # the wall pad sees the outside and the inside
    r_w = r_insert_in_wall(h_out, h_in)
    return t_ref + (t_board - t_ref) * r_w / (r_w + R_STANDOFF)


def cell_of(x: float, y: float) -> tuple[int, int]:
    return min(NX - 1, int(x)), min(NY - 1, int(y))


def m8_case(option: str, r_hs: float, **kw) -> dict:
    s = solve_board(option, r_hs, **kw)
    board_max = np.maximum(s["top"], s["bot"])
    boss_board = [float(board_max[cell_of(x, y)[1], cell_of(x, y)[0]]) for x, y in HOLES]
    boss_rule14 = [boss_petg_temp(t, s["wall"], kw["h_in"], kw["h_out"], True) for t in boss_board]
    front = wall_local(disc_mean(s["top"], FRONT_GAP * 1e3), kw["h_in"], kw["h_out"])
    walls = [float(front.max())]
    if option == "C1":
        (i0, i1), (j0, j1) = HS_FOOT
        mask = np.ones_like(s["bot"], dtype=bool)
        mask[j0:j1, i0:i1] = False
        back = wall_local(disc_mean(s["bot"], BACK_GAP * 1e3), kw["h_in"], kw["h_out"])
        walls.append(float(back[mask].max()))
    # D: the back and sides are the extrusion (metal); only the printed face is scored
    return dict(kw=kw, s=s, boss_board=boss_board, boss_rule14=boss_rule14, wall_max=max(walls),
                wall_front=float(front.max()))


CENTRAL = dict(coverage=0.6, h_in=6.5, h_out=8.0, h_gap=45.0, q_rf=1.5)


def sweep_m8(option: str, r_hs: float) -> dict:
    """Worst case over SWEEP of max(boss with the screw on the copper, printed wall), plus the central case."""
    keys = list(SWEEP)
    worst = None
    lo = dict(boss_rule14=math.inf, wall=math.inf)
    for combo in itertools.product(*(SWEEP[k] for k in keys)):
        kw = dict(zip(keys, combo))
        if option == "D" and kw["h_gap"] != SWEEP["h_gap"][0]:
            continue  # h_gap has no role in D
        rec = m8_case(option, r_hs, **kw)
        lo["boss_rule14"] = min(lo["boss_rule14"], max(rec["boss_rule14"]))
        lo["wall"] = min(lo["wall"], rec["wall_max"])
        key = max(max(rec["boss_board"]), rec["wall_max"])
        if worst is None or key > worst[0]:
            worst = (key, rec)
    w = worst[1]
    # the worst of each quantity over the sweep (the argmax may differ per quantity)
    w_all = dict(boss_board=-math.inf, boss_rule14=-math.inf, wall=-math.inf, tj=-math.inf)
    for combo in itertools.product(*(SWEEP[k] for k in keys)):
        kw = dict(zip(keys, combo))
        if option == "D" and kw["h_gap"] != SWEEP["h_gap"][0]:
            continue
        rec = m8_case(option, r_hs, **kw)
        w_all["boss_board"] = max(w_all["boss_board"], max(rec["boss_board"]))
        w_all["boss_rule14"] = max(w_all["boss_rule14"], max(rec["boss_rule14"]))
        w_all["wall"] = max(w_all["wall"], rec["wall_max"])
        w_all["tj"] = max(w_all["tj"], rec["s"]["tj"])
    return dict(worst=w, maxima=w_all, minima=lo, central=m8_case(option, r_hs, **CENTRAL))


EXPECTED = dict(
    r_hs_m4_c1=(6.10, 6.13),         # K/W, INSP-081 finding-1 threshold 6.11
    r_hs_c3_2_c1=(4.88, 4.91),       # K/W, C3 score 2 (margin >= 5 K)
    r_ds_for_6p11_f08=(4.1, 4.4),    # K/W, catalog free-air value needed at f_conv 0.8
    k9_pad_trip=(107.0, 107.6),      # C, Tj at 95 C for a pad sensor
    k9_hs_trip_c1=(134.5, 135.3),    # C, Tj at 95 C for a C1 heat-sink sensor
    screen_reproduced=True,          # the board model with no lateral loss equals the iteration 1 chain
    field_tj_c1_611_le_110=True,     # the field model with the whole line-up stays at or below the screen's limit
    c1_boss_direct_pass=False,       # M8 at the bosses with the screw on the copper (revision 0)
    c1_boss_rule14_pass=True,        # M8 at the insert with the PA66 standoff variant (not adopted), worst case
    c1_wall_pass=False,              # M8 at the printed wall facing the board, worst case of the sweep
    c1_wall_central_le_limit_plus_1=True,  # central estimate within 1 K of the 64 C limit
    hdt_needed_c1=(98.5, 99.5),      # C, filament HDT at 0.45 MPa at which C1 passes M8 everywhere (rule 15)
    hdt_needed_d=(98.2, 99.2),
    d_boss_direct_pass=False,
    d_boss_rule14_pass=True,
    d_wall_pass=False,
)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    got = {}
    print("1. M4 heat-sink threshold (REQ-SYS-112, 45 C, 4.1 W in the final, continuous; iteration 1 chain):")
    for alt in ("A", "C1", "D"):
        print(f"   {alt}: chain junction to heat node {chain_below_hs(alt):.2f} K/W; "
              f"M4 pass at r_hs <= {r_hs_for_margin(alt, 0.0):.2f} K/W; C3 score 2 (>= 5 K) at <= {r_hs_for_margin(alt, 5.0):.2f}; "
              f"score 3 (>= 8 K) at <= {r_hs_for_margin(alt, 8.0):.2f}")
    got["r_hs_m4_c1"] = r_hs_for_margin("C1", 0.0)
    got["r_hs_c3_2_c1"] = r_hs_for_margin("C1", 5.0)
    for r in (4.5, 4.89, 5.5, 6.11, 7.25, 9.0):
        print(f"   C1 at {r:.2f} K/W: Tj {tj('C1', r):.1f} C")
    print("2. Guard derating (catalog free-air value at a 30 K rise to in situ):")
    for f in F_CONV:
        print(f"   f_conv {f}: 4.5 K/W catalog gives {guard_model(4.5, f):.2f} K/W in situ (+{guard_model(4.5, f) - 4.5:.2f}); "
              f"catalog needed for 6.11 in situ {r_ds_for_insitu(6.11, f):.2f}, for 5.5 {r_ds_for_insitu(5.5, f):.2f}")
    got["r_ds_for_6p11_f08"] = r_ds_for_insitu(6.11, 0.8)
    print("3. K9 trip (Tj at 92 / 95 / 98 C at the sensor, 4.1 W):")
    k9_rows = []
    for alt in ("A", "C1", "D"):
        for pt in SENSOR_POINTS:
            lo, mid, hi = k9_trip(alt, pt)
            k9_rows.append((alt, pt, lo, mid, hi))
            print(f"   {alt}, {pt}: {lo:.1f} / {mid:.1f} / {hi:.1f} C")
    got["k9_pad_trip"] = k9_trip("C1", list(SENSOR_POINTS)[0])[1]
    got["k9_hs_trip_c1"] = k9_trip("C1", list(SENSOR_POINTS)[1])[1]
    s0 = solve_board("C1", 5.5, coverage=0.6, h_in=1e-9, h_out=8.0, h_gap=1e-9, q_rf=0.0, q_digital=0.0, gz_scale=0.0,
                     pocket=False)
    got["screen_reproduced"] = abs(s0["tj"] - tj("C1", 5.5)) < 0.2
    print(f"   reproduction: board model with no lateral loss Tj {s0['tj']:.2f} C against the screen {tj('C1', 5.5):.2f} C")
    print(f"4. M8 (limit {M8_LIMIT:.0f} C), sweep {SWEEP}; central {CENTRAL}; PA66 standoff variant {R_STANDOFF:.0f} K/W")
    rows, results = [], {}
    for option, r_hs in (("C1", 5.5), ("C1", 6.11), ("D", ts.ALTS["D"]["r_amb"])):
        res = sweep_m8(option, r_hs)
        results[(option, r_hs)] = res
        c, mx, mn = res["central"], res["maxima"], res["minima"]
        row = dict(option=option, r_hs_k_per_w=r_hs,
                   tj_central_c=round(c["s"]["tj"], 1), tj_max_c=round(mx["tj"], 1),
                   pad_top_central_c=round(c["s"]["tp"], 1), hs_node_central_c=round(c["s"]["hs"], 1),
                   inner_wall_node_central_c=round(c["s"]["wall"], 1),
                   boss_screw_on_copper_central_c=round(max(c["boss_board"]), 1),
                   boss_screw_on_copper_max_c=round(mx["boss_board"], 1),
                   boss_standoff_variant_central_c=round(max(c["boss_rule14"]), 1),
                   boss_standoff_variant_range_c=f"{mn['boss_rule14']:.1f} to {mx['boss_rule14']:.1f}",
                   wall_central_c=round(c["wall_max"], 1), wall_range_c=f"{mn['wall']:.1f} to {mx['wall']:.1f}",
                   m8_limit_c=M8_LIMIT, hdt_needed_for_walls_c=round(mx["wall"] + M8_RULE, 1),
                   hdt_needed_for_m8_c=round(max(mx["wall"], mx["boss_board"]) + M8_RULE, 1),
                   worst_inputs=";".join(f"{k}={v}" for k, v in res["worst"]["kw"].items()))
        rows.append(row)
        print("  ", row)
        print("     board temperature at the six holes, worst case:", [round(v, 1) for v in res["worst"]["boss_board"]])
    c1 = results[("C1", 6.11)]
    d = results[("D", ts.ALTS["D"]["r_amb"])]
    got["field_tj_c1_611_le_110"] = c1["maxima"]["tj"] <= TJ_MAX
    got["c1_boss_direct_pass"] = c1["maxima"]["boss_board"] <= M8_LIMIT
    got["c1_boss_rule14_pass"] = c1["maxima"]["boss_rule14"] <= M8_LIMIT
    got["c1_wall_pass"] = c1["maxima"]["wall"] <= M8_LIMIT
    got["c1_wall_central_le_limit_plus_1"] = c1["central"]["wall_max"] <= M8_LIMIT + 1.0
    got["d_boss_direct_pass"] = d["maxima"]["boss_board"] <= M8_LIMIT
    got["d_boss_rule14_pass"] = d["maxima"]["boss_rule14"] <= M8_LIMIT
    got["d_wall_pass"] = d["maxima"]["wall"] <= M8_LIMIT
    got["hdt_needed_c1"] = max(c1["maxima"]["wall"], c1["maxima"]["boss_board"]) + M8_RULE
    got["hdt_needed_d"] = max(d["maxima"]["wall"], d["maxima"]["boss_board"]) + M8_RULE
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", newline="") as fh:
        wr = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        wr.writeheader()
        wr.writerows(rows)
        fh.write("\n")
        wr2 = csv.writer(fh)
        wr2.writerow(["k9_option", "sensor_point", "tj_at_92c", "tj_at_95c", "tj_at_98c"])
        for alt, pt, lo, mid, hi in k9_rows:
            wr2.writerow([alt, pt, round(lo, 1), round(mid, 1), round(hi, 1)])
    plot(results)
    errs = []
    for k, v in EXPECTED.items():
        g = got[k]
        ok = (v[0] <= g <= v[1]) if isinstance(v, tuple) else (g == v)
        if not ok:
            errs.append(f"{k}: got {g}, expected {v}")
    if args.check:
        for e in errs:
            print("MISMATCH:", e)
        print("CHECK", "FAIL" if errs else "PASS")
        return 1 if errs else 0
    return 0


def plot(results) -> None:
    fig, axes = plt.subplots(1, 3, figsize=(17, 5.6), gridspec_kw=dict(width_ratios=[1.2, 1.2, 1.05]))
    for ax, key, title in ((axes[0], ("C1", 6.11), "C1 at 6.11 K/W"), (axes[1], ("D", ts.ALTS["D"]["r_amb"]), "D")):
        w = results[key]["worst"]
        top = w["s"]["top"]
        im = ax.imshow(top, origin="lower", extent=(0, NX, 0, NY), cmap="inferno", vmin=60, vmax=100)
        if top.min() < M8_LIMIT:
            cs = ax.contour(np.arange(NX) + 0.5, np.arange(NY) + 0.5, top, levels=[M8_LIMIT], colors="cyan", linewidths=1.2)
            ax.clabel(cs, fmt="64 C", fontsize=8)
        else:
            ax.text(14, NY - 14, f"whole board above {M8_LIMIT:.0f} C (min {top.min():.0f} C)", color="white", fontsize=8.5)
        for k, (x, y) in enumerate(HOLES):
            ax.plot(x, y, "o", ms=9, mfc="none", mec="white", mew=1.8)
            ax.text(x + (4 if x < 100 else -4), y + (3 if y < 31 else -5), f"{w['boss_board'][k]:.0f}", color="white",
                    ha="center", fontsize=8.5, weight="bold")
        ax.add_patch(plt.Rectangle((PAD[0][0], PAD[1][0]), 15, 15, fill=False, ec="white", lw=1, ls="--"))
        ax.text(PAD[0][0] + 7.5, PAD[1][0] - 3.5, "PA pad", color="white", ha="center", fontsize=8)
        if key[0] == "C1":
            ax.add_patch(plt.Rectangle((HS_FOOT[0][0], HS_FOOT[1][0]), 40, 58, fill=False, ec="#d0d0d0", lw=1, ls=":"))
        ax.set_title(f"{title}: board top copper, worst case of the sweep\n(45 C ambient, 4.1 W final + {w['kw']['q_rf']} W RF section)",
                     fontsize=9.5)
        ax.set_xlabel("board X, mm (+X: antenna end)")
        ax.set_ylabel("board Y, mm")
        fig.colorbar(im, ax=ax, fraction=0.03, pad=0.02, label="C")
    ax = axes[2]
    labels = [f"{o}\n{r:.2f} K/W" for (o, r) in results]
    x = np.arange(len(labels))
    series = (("boss, screw on copper (rev 0)", "boss_board", "#c0504d", -0.27),
              ("boss insert, PA66 standoff variant", "boss_rule14", "#1f4e79", 0.0),
              ("printed wall facing the board", "wall", "#7f7f7f", 0.27))
    for name, key, col, off in series:
        hi = [res["maxima"][key] for res in results.values()]
        cen = [max(res["central"][key]) if key.startswith("boss") else res["central"]["wall_max"] for res in results.values()]
        ax.bar(x + off, hi, 0.25, color=col, label=name + " (worst)")
        ax.plot(x + off, cen, "D", color="white", mec="k", ms=5)
    ax.plot([], [], "D", color="white", mec="k", ms=5, label="central inputs")
    ax.axhline(M8_LIMIT, color="k", ls="--", lw=1)
    ax.text(-0.45, M8_LIMIT + 0.8, f"M8 limit {M8_LIMIT:.0f} C (PETG HDT 69 C less 5 K)", fontsize=8)
    ax.axhline(94.0, color="#7030a0", ls=":", lw=1.2)
    ax.text(-0.45, 95.2, "M8 limit 94 C with a filament of HDT 99 C (rule 15)", fontsize=8, color="#7030a0")
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=8.5)
    ax.set_ylim(40, 122)
    ax.set_ylabel("peak printed-part temperature, C")
    ax.set_title("M8 at the REQ-SYS-112 condition", fontsize=10)
    ax.legend(fontsize=7.5, loc="upper left")
    ax.grid(axis="y", alpha=0.3)
    fig.text(0.01, 0.01, "Circles: the six mounting holes, with the board temperature there (C). "
             "Author model (two-layer board, 1 mm cells), developer evidence; superseded by WP-PDR-28.", fontsize=8)
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    OUT_PNG.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT_PNG, dpi=120)


if __name__ == "__main__":
    sys.exit(main())
