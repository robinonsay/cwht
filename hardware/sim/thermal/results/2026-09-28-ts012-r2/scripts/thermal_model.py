#!/usr/bin/env python3
"""Lumped thermal RC network of the cwht PA, heat sink and owner-printed PETG case (WP-PDR-28, TS-012).

Purpose: the TS-012 revision 4 pre-order thermal item (section 7.3) for both finalists, A4 (NXP
AFT05MS004N SOT-89 on a hand-built PA board) and A5 (Mitsubishi RA07M1317M module), each on the
Boyd 530002B02500G extrusion. This file is the model; `ts012_thermal.py` runs the cases, writes the
results directory and draws the plots.

Model (one node per part; every node has a heat capacity; ambient is a fixed-temperature node):
  J2, J1   RA07M1317M stage-2 and stage-1 channels (A5), or J the AFT05 junction (A4)
  CASE     module flange (A5) or the AFT05 tab with its pad and board tongue (A4)
  SINK     Boyd 530002B02500G, one isothermal aluminium node (57 g from the drawing)
  GUARD    printed PETG finger guard over the fins
  EF       PETG bay walls within 5 mm of the sink's inner half (layout O1 only)
  EW       PETG case end wall facing the sink's inner channel across a gap (layout O3 only)
  BAY      PA-bay air with the RF board, relay and LPF (A5), or merged into MAIN when no bulkhead
  BW       PETG walls of the PA bay (chimney slots in its top and bottom)
  BH1, BH2 the two 1.2 mm PETG walls of the double-wall bulkhead
  MAIN     main-bay air with the main board, Pico 2, LM2940 and the feed parts
  MW       PETG walls of the main bay
  CELL     the two 18650 cells in their holders
Sink to air follows the Boyd natural-convection curve (catalog page 56, graph read), split into the
outer half (outside air, behind the guard) and the inner half (bay air, or outside air facing the
end wall), each with a convective and a radiative share. The profile is symmetric about its
1.57 mm web (drawing), so each side of the web carries half of the fin area.

Conductances that depend on temperature (the catalog curve, radiation, the chimney vent) are
evaluated at the latest temperatures: steady states by fixed-point iteration, transients by
backward Euler with the conductances of the previous step (semi-implicit).

Input classes (column `cls` of PARAMS): D datasheet value; DD derived from a datasheet (drawing
dimension, graph read, or arithmetic on datasheet values); R requirement or TS-012 pass criterion;
E estimate by the author (engineering judgement, Low confidence). Every E value has a low and a high
used by the tornado.

numpy, scipy and matplotlib are class B developer tools here (tools/toolchain.lock.md section 2);
the LTspice electrical analogue in `ts012_thermal.py` cross-checks the solver.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable

import numpy as np

SIGMA = 5.670e-8  # W/(m2 K4)
K0 = 273.15


@dataclass
class Param:
    value: float
    low: float
    high: float
    unit: str
    cls: str
    source: str


# ------------------------------------------------------------------------------------------ inputs
P = {
    # --- conditions and limits
    "t_amb_112": Param(45.0, 45.0, 45.0, "C", "R", "REQ-SYS-112 continuous key-down at 45 C ambient"),
    "t_amb_113": Param(25.0, 25.0, 25.0, "C", "R", "REQ-SYS-113 5 min continuous key-down at 25 C"),
    "tj_limit": Param(110.0, 110.0, 110.0, "C", "R", "REQ-SYS-112 (TBR)"),
    "surf_limit": Param(48.0, 48.0, 48.0, "C", "R", "REQ-SYS-113 every accessible surface (TBR)"),
    "case_guid": Param(90.0, 90.0, 90.0, "C", "D", "RA07M1317M datasheet Jun 2019 p.8: Tcase below 90 C"),
    "petg_crit": Param(60.0, 60.0, 60.0, "C", "R", "TS-012 7.3 pass (c): every PETG surface <= 60 C"),
    "petg_hdt": Param(69.0, 69.0, 69.0, "C", "E", "PETG HDT 0.45 MPa typical (TS-011 M8); filament TDS not read"),
    "cell_crit_a": Param(55.0, 55.0, 55.0, "C", "R", "TS-012 7.3 pass (a): cell and main-bay air <= 55 C at 50 % duty, 30 min"),
    "cell_limit": Param(60.0, 60.0, 60.0, "C", "D", "cell discharge limit and LM393 cell trip (TS-012 7.3)"),
    "relay_amb": Param(65.0, 65.0, 65.0, "C", "D", "Omron G5V-2 standard coil, ambient operating -25 to 65 C (datasheet)"),
    "trip_fw": Param(85.0, 85.0, 85.0, "C", "R", "REQ-SYS-118 firmware inhibit 85 C +/-3 (sink NTC)"),
    "trip_hw": Param(95.0, 95.0, 95.0, "C", "R", "REQ-SYS-181 hardware trip 95 C +/-3 (sink NTC)"),
    # --- electrical corner (TS-012 7.3; drain feed resistance 0.26 to 0.45 ohm)
    "v_pack": Param(8.4, 8.4, 8.4, "V", "R", "full 2S pack, TS-012 7.3 corner"),
    "p_rf_dev": Param(5.6, 5.6, 5.6, "W", "DD", "5 W at the SMA + 0.5 dB LPF and relay loss (TS-012 7.3)"),
    "r_feed": Param(0.26, 0.26, 0.45, "ohm", "E", "TS-012 7.3 feed budget 0.26 to 0.45 ohm (minimum = hottest PA)"),
    "r_cellpath": Param(0.06, 0.05, 0.10, "ohm", "E", "cells 0.04 + holder contacts 0.02 of the feed budget (TS-012 7.3)"),
    "i_bus": Param(0.30, 0.25, 0.40, "A", "E", "5 V bus in TX: relay 0.1, GVA-84+ 0.1, Pico and rest 0.1"),
    # A5 module current at 5.6 W (datasheet min efficiency 45 % at 6 W, 7.2 V; class-B scaled)
    "a5_idd": Param(1.97, 1.79, 1.97, "A", "DD", "RA07M1317M: 1.85 A at 6 W (45 % min), x(5.6/6)^0.5, +10 % (TS-012 7.3)"),
    "a5_p1": Param(1.5, 1.2, 1.8, "W", "DD", "stage-1 share, datasheet thermal table (1.4 W at 6.5 W out)"),
    "a5_rjc2": Param(2.4, 2.16, 2.64, "K/W", "D", "RA07M1317M Rth(ch-case) stage 2 (table value; +/-10 % band E)"),
    "a5_rjc1": Param(4.5, 4.05, 4.95, "K/W", "D", "RA07M1317M Rth(ch-case) stage 1"),
    "a5_bond": Param(50e-6, 25e-6, 75e-6, "m", "E", "compound bond line (TS-012 7.3: 25 to 75 um)"),
    "a5_area": Param(1.42e-4, 1.42e-4, 1.42e-4, "m2", "DD", "flange contact 19.2 x 7.4 mm (outline drawing)"),
    "k_tim": Param(0.70, 0.60, 0.80, "W/mK", "E", "Wakefield 120 compound (TS-012 7.3 value; datasheet not re-read)"),
    "r_spread_x": Param(0.0, 0.0, 0.3, "K/W", "E", "web spreading beyond the catalog TO-220 reference"),
    # A4 AFT05 (datasheet VHF reference circuit: 6.1 W, 61.8 %, 7.5 V; no minimum)
    "a4_isat": Param(1.387, 1.261, 1.558, "A", "DD", "AFT05: 6.1 W/(0.618 x 7.5 V) x (5.6/6.1)^0.5 = 1.26 A; +10 % 1.39; 50 % hand match 1.56"),
    "a4_rjc": Param(4.4, 3.96, 4.84, "K/W", "D", "AFT05MS004N RthJC 4.4 C/W (Table 2; +/-10 % band E)"),
    "a4_r_pad": Param(0.8, 0.5, 1.5, "K/W", "E", "tab-to-via-field spreading in the top copper"),
    "a4_r_via": Param(1.1, 0.9, 1.6, "K/W", "DD", "solder-filled 1 x 3 mm slot + 30 x 0.4 mm vias, 0.8 mm board (computed)"),
    "a4_r_bs": Param(0.6, 0.4, 1.0, "K/W", "E", "board tongue to web through compound, 50 to 100 um"),
    "a4_gva_on_sink": Param(0.5, 0.0, 0.5, "W", "E", "GVA-84+ on the A4 PA board, heat to the sink"),
    # sink (Boyd 530002B02500G, catalog page 56 and drawing)
    "sink_mass": Param(57.0, 52.0, 62.0, "g", "DD", "profile area 330 to 340 mm2 (drawing, pixel count) x 63.5 mm x 2.70 g/cm3"),
    "k_cat": Param(1.0, 0.93, 1.07, "-", "DD", "catalog natural-convection curve, graph read +/-7 %"),
    "k_orient": Param(1.35, 1.10, 2.0, "-", "E", "extrusion axis horizontal; Boyd: other orientations 'can DOUBLE' R"),
    "r_frac": Param(0.35, 0.25, 0.45, "-", "E", "radiative share of the catalog conductance (black anodize)"),
    "eta_encl": Param(0.6, 0.4, 0.8, "-", "E", "inner half in the closed PA bay (O1), convective derate"),
    "eta_wall": Param(0.6, 0.45, 0.75, "-", "E", "inner half facing the end wall at 5 mm (O3), convective derate"),
    "eta_guard3": Param(0.75, 0.6, 0.85, "-", "E", "outer half behind a slotted guard 3 mm from the fin tips"),
    "phi3": Param(0.5, 0.35, 0.65, "-", "E", "plume temperature fraction at the guard, 3 mm"),
    "eta_guard_dc": Param(0.85, 0.75, 0.92, "-", "E", "outer half behind the design-change guard (end face 10 mm, wraps 3 mm)"),
    "phi_dc": Param(0.35, 0.25, 0.5, "-", "E", "plume temperature fraction at the design-change guard"),
    "shield_rad": Param(0.25, 0.15, 0.4, "-", "E", "share of the inner-half radiation reaching the end wall behind a HASL spare-board shield"),
    "main_vent_area": Param(2.0e-4, 0.0, 3.0e-4, "m2", "E", "main-bay slots, bottom and lower sides, and upper sides (each)"),
    # PETG and films
    "k_petg": Param(0.20, 0.18, 0.25, "W/mK", "E", "PETG (TS-011 value, Low)"),
    "t_wall": Param(2.0e-3, 2.0e-3, 2.0e-3, "m", "R", "case wall 2 mm (TS-012 8.5)"),
    "h_out_c": Param(4.0, 3.0, 6.0, "W/m2K", "E", "outer natural convection (radiation added, eps 0.9)"),
    "h_in_c": Param(2.5, 1.5, 4.0, "W/m2K", "E", "inner convection (radiation added, eps_eff 0.8)"),
    "g_leads": Param(0.015, 0.008, 0.03, "W/K", "E", "DC, drive and coax leads through the bulkhead"),
    "g_cell_main": Param(0.03, 0.02, 0.045, "W/K", "E", "cells to main-bay air (73 cm2, confined)"),
    "g_cell_wall": Param(0.02, 0.01, 0.03, "W/K", "E", "cells to the bottom wall (holders about 1 mm off it)"),
    "vent_area": Param(3.6e-4, 0.0, 5.0e-4, "m2", "E", "rev 4 PA-bay chimney slots, each of top and bottom (0 = blocked)"),
    "vent_area_dc": Param(5.0e-4, 2.5e-4, 6.0e-4, "m2", "E", "design-change PA-bay slots, each of top and bottom (55 % of 9.1 cm2)"),
    "relay_hold": Param(0.4, 0.3, 1.0, "-", "E", "design change: G5V-2 coil held by PWM at about 63 % voltage after pull-in (power 0.4x)"),
    "k_fr4": Param(0.30, 0.25, 0.35, "W/mK", "E", "FR4 through-plane (TS-011 value)"),
    "fr4_limit": Param(105.0, 105.0, 105.0, "C", "E", "FR4 spare-board wall, continuous (below the laminate Tg of about 130 to 140 C)"),
    "p_lm2940": Param(0.9, 0.6, 1.0, "W", "DD", "(8.4 - 0.5 - 5) V x 0.3 A (TS-012: 0.6 to 0.9 W)"),
    "p_pico": Param(0.2, 0.15, 0.3, "W", "E", "Pico 2, op-amps, Si5351 module"),
    "p_relay": Param(0.5, 0.5, 0.5, "W", "D", "G5V-2 5 V coil 100 mA (Omron datasheet, TS-012)"),
    "p_gva": Param(0.5, 0.5, 0.5, "W", "DD", "GVA-84+ 5 V, about 100 mA"),
    "c_cell": Param(92.0, 85.0, 100.0, "J/K", "E", "two 18650 about 46 g each x 1.0 J/gK"),
    # --- revision 1 (INSP finding-2): every value that build() used to hard-code, with class, source and range
    # geometry of the guard, the walls and the bulkhead (author's layout on the Boyd drawing and the TS-012 8.5
    # envelope; the case CAD does not exist yet, so each area carries a band)
    "a_guard_end": Param(29.4e-4, 26.5e-4, 32.3e-4, "m2", "DD", "guard end face over the 41.9 x 63.5 mm sink end (drawing) with its clearance; +/-10 % band E"),
    "a_guard_side": Param(56.9e-4, 51.2e-4, 62.6e-4, "m2", "DD", "guard top, bottom and profile-end faces around the 25.4 mm deep fins (drawing); +/-10 % band E"),
    "guard_solid": Param(0.5, 0.4, 0.65, "-", "E", "solid fraction of the slotted grille (finger-safe slots)"),
    "v_g": Param(0.45, 0.30, 0.60, "-", "E", "share of the outer-half radiation the grille intercepts (0.5 solid x 0.9 view)"),
    "h_gc": Param(5.0, 3.0, 8.0, "W/m2K", "E", "plume-side convection on the grille bars"),
    "a_ef": Param(28.0e-4, 25.2e-4, 30.8e-4, "m2", "DD", "O1 bay walls near the sink: 224 mm perimeter x 12.7 mm; +/-10 % band E"),
    "a_ew": Param(29.4e-4, 26.5e-4, 32.3e-4, "m2", "DD", "O3 end wall facing the inner channel, sink end face size; +/-10 % band E"),
    "t_ew_fr4": Param(1.6e-3, 0.8e-3, 1.6e-3, "m", "E", "spare JLCPCB board as end wall: main board 1.6 mm (TS-012 8.5), 0.8 mm if a PA or RF board is used"),
    "a_bw_gross": Param(29.1e-4, 26.2e-4, 32.0e-4, "m2", "DD", "PA-bay walls 2 x (70 + 42) mm x 13 mm (TS-012 8.5 stack); +/-10 % band E"),
    "bw_solid": Param(0.8, 0.7, 0.9, "-", "E", "solid share of the PA-bay walls after the chimney slots"),
    "a_bh": Param(25.0e-4, 22.5e-4, 27.5e-4, "m2", "DD", "bulkhead wall area, case cross-section less the board slots; +/-10 % band E"),
    "t_bh": Param(1.2e-3, 1.0e-3, 1.4e-3, "m", "E", "each wall of the TS-012 rev 4 double-wall bulkhead"),
    "gap_bh": Param(3.0e-3, 2.0e-3, 4.0e-3, "m", "E", "air gap between the two bulkhead walls"),
    "a_mw": Param(262.0e-4, 209.6e-4, 314.4e-4, "m2", "E", "main-case wall area from the TS-012 8.5 envelope (no CAD yet); +/-20 %"),
    # radiation and film terms
    "eps_out": Param(0.90, 0.85, 0.95, "-", "E", "PETG outer-surface emissivity"),
    "eps_in": Param(0.80, 0.70, 0.90, "-", "E", "effective inner emissivity (PETG to boards and walls)"),
    "eps_bh": Param(0.82, 0.75, 0.90, "-", "E", "effective emissivity across the bulkhead air gap (two PETG faces)"),
    "k_air": Param(0.028, 0.027, 0.029, "W/mK", "D", "air at 50 C, 0.028 W/m K (standard property tables)"),
    "gap_face": Param(2.0e-3, 1.5e-3, 3.0e-3, "m", "E", "O1 air gap between the sink profile ends and the nearest bay wall"),
    "h_rad_gap": Param(7.0, 5.0, 8.0, "W/m2K", "E", "linearised radiation across that gap (anodize to PETG)"),
    "a_gap_face": Param(4.0e-4, 2.0e-4, 6.0e-4, "m2", "E", "facing metal area across that gap"),
    "rad_f_ef": Param(0.30, 0.20, 0.45, "-", "E", "O1 inner-half radiation share to the bay walls near the sink"),
    "rad_f_bh": Param(0.40, 0.25, 0.50, "-", "E", "O1 inner-half radiation share to the bulkhead (rest to the PA-bay walls)"),
    "o3_rad_amb": Param(0.30, 0.20, 0.40, "-", "E", "O3 inner-half radiation share leaving through the gap to ambient"),
    "o3_rad_guard": Param(0.20, 0.10, 0.30, "-", "E", "O3 inner-half radiation share to the guard (rest to the end wall)"),
    "h_gapc": Param(3.0, 1.5, 5.0, "W/m2K", "E", "O3 end-wall gap air exchange coefficient"),
    "gap_share": Param(0.5, 0.3, 0.7, "-", "E", "share of the end-wall area that the gap air exchange reaches"),
    "g_case_air": Param(0.003, 0.001, 0.006, "W/K", "E", "PA case or module body to the air or wall beside it"),
    # chimney vents (orifice stack-effect formula)
    "cd_vent": Param(0.6, 0.4, 0.7, "-", "E", "discharge coefficient of the printed slots"),
    "h_stack_bay": Param(0.035, 0.025, 0.045, "m", "E", "PA-bay stack height between bottom and top slots"),
    "h_stack_main": Param(0.030, 0.020, 0.040, "m", "E", "main-bay stack height between bottom and upper side slots"),
    "rho_air": Param(1.10, 1.07, 1.13, "kg/m3", "D", "air at 45 to 60 C (standard property tables)"),
    "cp_air": Param(1007.0, 1005.0, 1009.0, "J/kgK", "D", "air (standard property tables)"),
    # heat capacities (transients only; the steady results do not depend on them)
    "cp_al": Param(896.0, 880.0, 910.0, "J/kgK", "D", "aluminium 6063 specific heat"),
    "rho_petg": Param(1270.0, 1230.0, 1290.0, "kg/m3", "E", "PETG density (filament datasheet not read)"),
    "cp_petg": Param(1200.0, 1100.0, 1300.0, "J/kgK", "E", "PETG specific heat"),
    "rho_fr4": Param(1850.0, 1800.0, 1900.0, "kg/m3", "E", "FR4 density"),
    "cp_fr4": Param(1100.0, 1000.0, 1200.0, "J/kgK", "E", "FR4 specific heat"),
    "c_bay": Param(25.0, 15.0, 40.0, "J/K", "E", "PA-bay air, RF board, relay and LPF parts"),
    "c_main": Param(60.0, 40.0, 90.0, "J/K", "E", "main-bay air, main board, Pico 2 and parts"),
    "c_case_a5": Param(3.0, 2.0, 4.5, "J/K", "E", "RA07M1317M flange and body"),
    "c_j2": Param(0.2, 0.1, 0.4, "J/K", "E", "RA07M1317M stage-2 die and its substrate share"),
    "c_j1": Param(0.1, 0.05, 0.2, "J/K", "E", "RA07M1317M stage-1 die and its substrate share"),
    "c_j_a4": Param(0.05, 0.02, 0.10, "J/K", "E", "AFT05MS004N die and SOT-89 body"),
    "c_case_a4": Param(1.0, 0.6, 1.6, "J/K", "E", "AFT05 tab, top-copper pad and board tongue"),
    # --- revision 1 (INSP finding-4): REQ-SYS-118 sensor offset and lag
    "ntc_frac_a5": Param(0.5, 0.0, 1.0, "-", "E", "A5 NTC under a flange screw on the ear outside the 19.2 mm contact face: reading = case - f x (case - sink); the screw ties the ear to the sink"),
    "ntc_frac_a4": Param(1.0, 0.5, 1.0, "-", "E", "A4 NTC on the top copper 2 mm from the tab (TS-011 rule 14): reading = tab - f x (heat flow x a4_r_pad)"),
    "tau_ntc_a5": Param(8.0, 4.0, 15.0, "s", "E", "A5 NTC time constant, lug or bead under the screw"),
    "tau_ntc_a4": Param(3.0, 1.0, 6.0, "s", "E", "A4 NTC time constant, 0603 NTC on the pad copper"),
    "t_resp": Param(0.15, 0.15, 0.15, "s", "R", "REQ-SYS-118 100 ms response plus one 20 Hz sample (HZ-003 K2)"),
    "trip_tol": Param(3.0, 3.0, 3.0, "C", "R", "REQ-SYS-118 and REQ-SYS-181 +/-3 C tolerance"),
    "inh_hyst": Param(5.0, 3.0, 10.0, "C", "E", "REQ-SYS-118 recovery hysteresis (value not yet set)"),
}

# Boyd 530002B02500G (5300 family, dashed curve, 63.5 mm) natural convection, catalog page 56
# ("Board Level Cooling Catalog", Boyd, 2024; mounting-surface rise versus heat dissipated),
# digitized from the 900 dpi render of the catalog page on 2026-09-28 (graph read, +/-1 K).
CAT_P_W = np.array([2.0, 3.0, 4.0, 5.0, 7.0, 11.0, 13.0, 15.0, 17.0, 19.8])
CAT_DT_K = np.array([8.7, 13.5, 17.4, 21.6, 28.6, 41.2, 46.3, 51.2, 55.3, 59.0])
CAT_G = CAT_P_W / CAT_DT_K


def g_cat(dt: float) -> float:
    """Catalog whole-sink conductance (W/K) at mounting-surface rise dt, free air, vertical."""
    return float(np.interp(max(dt, 0.0), CAT_DT_K, CAT_G))


def h_rad(t1: float, t2: float, eps: float) -> float:
    a, b = t1 + K0, t2 + K0
    return eps * SIGMA * (a * a + b * b) * (a + b)


def vals(overrides: dict | None = None) -> dict:
    v = {k: p.value for k, p in P.items()}
    if overrides:
        v.update(overrides)
    return v


# ------------------------------------------------------------------------------------------ network
@dataclass
class Net:
    t_amb: float
    names: list = field(default_factory=list)
    cap: dict = field(default_factory=dict)
    links: list = field(default_factory=list)  # (a, b, fn(T)->W/K)
    src_on: dict = field(default_factory=dict)
    src_off: dict = field(default_factory=dict)
    walls: dict = field(default_factory=dict)  # wall node -> (area m2, thickness m, k W/mK, material)
    meta: dict = field(default_factory=dict)

    def add(self, name: str, c: float, wall: tuple | None = None):
        self.names.append(name)
        self.cap[name] = c
        if wall is not None:
            self.walls[name] = wall

    def link(self, a: str, b: str, g):
        fn = g if callable(g) else (lambda T, g=g: g)
        self.links.append((a, b, fn))

    def src(self, node: str, p_on: float, p_off: float = 0.0):
        self.src_on[node] = self.src_on.get(node, 0.0) + p_on
        self.src_off[node] = self.src_off.get(node, 0.0) + p_off

    # --- assembly
    def _idx(self):
        return {n: i for i, n in enumerate(self.names)}

    def _matrix(self, T: dict):
        idx = self._idx()
        n = len(self.names)
        G = np.zeros((n, n))
        b_amb = np.zeros(n)
        for a, b, fn in self.links:
            g = fn(T)
            if b == "AMB":
                ia = idx[a]
                G[ia, ia] += g
                b_amb[ia] += g * self.t_amb
                continue
            ia, ib = idx[a], idx[b]
            G[ia, ia] += g
            G[ib, ib] += g
            G[ia, ib] -= g
            G[ib, ia] -= g
        return G, b_amb

    def power(self, key: float) -> np.ndarray:
        return np.array([self.src_off.get(n, 0.0) + key * (self.src_on.get(n, 0.0) - self.src_off.get(n, 0.0))
                         for n in self.names])

    def tdict(self, x: np.ndarray) -> dict:
        d = dict(zip(self.names, x))
        d["AMB"] = self.t_amb
        return d

    # --- solvers
    def steady(self, duty: float = 1.0, tol: float = 1e-7, itmax: int = 500) -> dict:
        x = np.full(len(self.names), self.t_amb + 20.0)
        p = self.power(duty)
        for _ in range(itmax):
            G, b = self._matrix(self.tdict(x))
            xn = np.linalg.solve(G, p + b)
            if np.max(np.abs(xn - x)) < tol:
                x = xn
                break
            x = 0.5 * x + 0.5 * xn
        return self.tdict(x)

    def transient(self, t_end: float, dt: float, key: Callable[[float], float], x0: dict | None = None,
                  every: int = 1):
        n = len(self.names)
        C = np.array([self.cap[k] for k in self.names])
        x = np.array([x0[k] for k in self.names]) if x0 else np.full(n, self.t_amb)
        ts, xs = [0.0], [x.copy()]
        steps = int(round(t_end / dt))
        for s in range(1, steps + 1):
            t = s * dt
            G, b = self._matrix(self.tdict(x))
            A = G + np.diag(C / dt)
            x = np.linalg.solve(A, C / dt * x + self.power(key(t - 0.5 * dt)) + b)
            if s % every == 0 or s == steps:
                ts.append(t)
                xs.append(x.copy())
        return np.array(ts), np.array(xs)

    def linearized(self, T: dict):
        """Frozen conductances at T (for the LTspice analogue and the linear cross-check)."""
        out = []
        for a, b, fn in self.links:
            out.append((a, b, fn(T)))
        return out


# ------------------------------------------------------------------------------------------ builders
LAYOUTS = {
    # TS-012 revision 4 as written: sink end wall at its web, inner half in the PA bay, guard 3 mm.
    "A5-R4": dict(fin="A5", sink="O1", guard=3, bulkhead=True, vent=True),
    # design change: whole sink outside the case end wall; the wall facing the inner channel (5 mm
    # from the fin tips) is a spare JLCPCB board (FR4) with its HASL copper toward the sink as a
    # radiation shield; guard wrapping the sink (end face 10 mm from the fins, top, bottom and profile
    # ends 3 mm); PA bay (RF board) behind that wall with larger chimney slots; relay coil held by PWM;
    # bulkhead; main-bay vent slots (bottom and sides).
    "A5-DC": dict(fin="A5", sink="O3", guard="dc", bulkhead=True, vent=True, shield=True, main_vent=True,
                  ew_fr4=True, dc=True),
    # A4 as TS-012 describes it: same sink end wall, inner half in the one case volume with the cells.
    "A4-R4": dict(fin="A4", sink="O1", guard=3, bulkhead=False, vent=False),
    # A4 with the same no-cost changes as A5-DC.
    "A4-DC": dict(fin="A4", sink="O3", guard="dc", bulkhead=True, vent=True, shield=True, main_vent=True,
                  ew_fr4=True, dc=True),
}


def dissipation(fin: str, v: dict) -> dict:
    """PA and feed heat at the corner (W) and the drain current (A)."""
    if fin == "A5":
        i_pa = v["a5_idd"]
    else:
        i_pa = v["a4_isat"]
    v_drain = v["v_pack"] - v["r_feed"] * i_pa
    p_pa = v_drain * i_pa - v["p_rf_dev"]
    i_tot = i_pa + v["i_bus"]
    p_feed_cells = i_tot ** 2 * v["r_cellpath"]
    p_feed_board = i_tot ** 2 * max(v["r_feed"] - v["r_cellpath"], 0.0)
    return dict(i_pa=i_pa, v_drain=v_drain, p_pa=p_pa, p_feed_cells=p_feed_cells, p_feed_board=p_feed_board,
                p_lpf=v["p_rf_dev"] - 5.0)


def build(layout: str, t_amb: float, v: dict | None = None) -> Net:
    """Network of one layout at ambient t_amb. Every number comes from v (PARAMS); none is hard-coded
    (revision 1, INSP finding-2), so every input is in inputs.csv and in the tornado."""
    L = LAYOUTS[layout]
    v = v if v is not None else vals()
    fin = L["fin"]
    net = Net(t_amb=t_amb)
    d = dissipation(fin, v)
    net.meta.update(layout=layout, fin=fin, **d)
    tw, kp = v["t_wall"], v["k_petg"]
    c_petg = v["rho_petg"] * v["cp_petg"]  # J/(m3 K)
    eta_g = v["eta_guard3"] if L["guard"] == 3 else v["eta_guard_dc"]
    phi = v["phi3"] if L["guard"] == 3 else v["phi_dc"]
    net.meta["fins_exposed"] = L["guard"] == 3  # rev 4 guard covers the end face only
    r = v["r_frac"]
    ko = v["k_orient"]
    eo, ei = v["eps_out"], v["eps_in"]

    def hout(Tn):
        return v["h_out_c"] + h_rad(Tn, t_amb, eo)

    def hin(t1, t2):
        return v["h_in_c"] + h_rad(t1, t2, ei)

    def wall_out(node, A):  # wall node (mid-plane) to ambient
        return lambda T: 1.0 / (1.0 / (hout(T[node]) * A) + tw / (2 * kp * A))

    def wall_in(node, other, A):  # wall node to an inside air/board node
        return lambda T: 1.0 / (1.0 / (hin(T[node], T[other]) * A) + tw / (2 * kp * A))

    def half(T):  # one side of the web: half the catalog conductance, orientation derated
        return 0.5 * v["k_cat"] * g_cat(T["SINK"] - t_amb) / ko

    def g_stack(area, h_stack, node):  # orifice stack-effect flow through a bottom and a top slot of area each
        def g(T):
            dT = max(T[node] - t_amb, 0.05)
            q = v["cd_vent"] * area / np.sqrt(2.0) * np.sqrt(2 * 9.81 * h_stack * dT / (t_amb + K0))
            return v["rho_air"] * v["cp_air"] * q
        return g

    # ---- PA and sink
    net.add("SINK", v["sink_mass"] * 1e-3 * v["cp_al"])
    if fin == "A5":
        p2 = d["p_pa"] - v["a5_p1"]
        net.add("J2", v["c_j2"])
        net.add("J1", v["c_j1"])
        net.add("CASE", v["c_case_a5"])
        net.link("J2", "CASE", 1.0 / v["a5_rjc2"])
        net.link("J1", "CASE", 1.0 / v["a5_rjc1"])
        r_if = v["a5_bond"] / (v["k_tim"] * v["a5_area"]) + v["r_spread_x"]
        net.link("CASE", "SINK", 1.0 / r_if)
        net.src("J2", p2)
        net.src("J1", v["a5_p1"])
        net.meta.update(p2=p2, r_if=r_if)
    else:
        net.add("J", v["c_j_a4"])
        net.add("CASE", v["c_case_a4"])
        net.link("J", "CASE", 1.0 / v["a4_rjc"])
        r_cs = v["a4_r_pad"] + v["a4_r_via"] + v["a4_r_bs"]
        net.link("CASE", "SINK", 1.0 / r_cs)
        net.src("J", d["p_pa"])
        net.src("SINK", v["a4_gva_on_sink"])
        net.meta.update(r_cs=r_cs)

    # ---- guard over the outer half (O1) or wrapping the whole sink (O3)
    a_guard = (v["a_guard_end"] + 0.5 * v["a_guard_side"]) if L["sink"] == "O1" else (v["a_guard_end"] + v["a_guard_side"])
    a_gs = v["guard_solid"] * a_guard  # solid part of the slotted grille, each face
    net.add("GUARD", a_gs * tw * c_petg, wall=(a_gs, tw, kp, "PETG"))
    h_gc = v["h_gc"]
    v_g = v["v_g"]
    g_plume = phi * h_gc * a_gs
    net.link("SINK", "AMB", lambda T: max(half(T) * ((1 - r) * eta_g + r * (1 - v_g)) - g_plume, 0.0))
    net.link("SINK", "GUARD", lambda T: half(T) * r * v_g + g_plume)
    net.link("GUARD", "AMB", lambda T: (1 - phi) * h_gc * a_gs + hout(T["GUARD"]) * a_gs)

    bay = "BAY" if L["bulkhead"] else "MAIN"

    # ---- inner half
    if L["sink"] == "O1":
        a_ef = v["a_ef"]
        net.add("EF", a_ef * tw * c_petg, wall=(a_ef, tw, kp, "PETG"))
        g_gap_face = (v["k_air"] / v["gap_face"] + v["h_rad_gap"]) * v["a_gap_face"]
        f_ef = v["rad_f_ef"]
        f_bh = v["rad_f_bh"] if L["bulkhead"] else 0.0
        f_bw = max(1.0 - f_ef - f_bh, 0.0)
        net.link("SINK", bay, lambda T: half(T) * (1 - r) * v["eta_encl"])
        net.link("SINK", "EF", lambda T: half(T) * r * f_ef + g_gap_face)
        net.link("EF", "AMB", wall_out("EF", a_ef))
        net.link("EF", bay, wall_in("EF", bay, a_ef))
        net.link("CASE", bay, v["g_case_air"])
        rad_bh = lambda T: half(T) * r * f_bh  # noqa: E731
        rad_bw = lambda T: half(T) * r * f_bw  # noqa: E731
    else:
        a_ew = v["a_ew"]
        if L.get("ew_fr4"):
            t_ew, k_ew = v["t_ew_fr4"], v["k_fr4"]
            net.add("EW", a_ew * t_ew * v["rho_fr4"] * v["cp_fr4"], wall=(a_ew, t_ew, k_ew, "FR4"))
        else:
            t_ew, k_ew = tw, kp
            net.add("EW", a_ew * tw * c_petg, wall=(a_ew, tw, kp, "PETG"))
        g_gapc = v["h_gapc"] * a_ew * v["gap_share"]
        f_amb, f_gd = v["o3_rad_amb"], v["o3_rad_guard"]
        f_ew = max(1.0 - f_amb - f_gd, 0.0)
        net.link("SINK", "AMB", lambda T: half(T) * ((1 - r) * v["eta_wall"] + r * f_amb))
        net.link("SINK", "GUARD", lambda T: half(T) * r * f_gd)
        sh = v["shield_rad"] if L.get("shield") else 1.0
        net.link("SINK", "EW", lambda T: half(T) * r * f_ew * sh + g_gapc)
        if L.get("shield"):  # the shield returns the rest of that radiation to the gap air and outside
            net.link("SINK", "AMB", lambda T: half(T) * r * f_ew * (1.0 - sh))
        net.link("EW", "AMB", lambda T: g_gapc)  # gap air exchange with outside
        net.link("EW", bay, lambda T: 1.0 / (1.0 / (hin(T["EW"], T[bay]) * a_ew) + t_ew / (2 * k_ew * a_ew)))
        net.link("CASE", "EW", v["g_case_air"])
        rad_bh = rad_bw = None

    # ---- PA bay (RF board, relay, LPF) and its walls
    a_bw = v["a_bw_gross"] * v["bw_solid"]
    if L["bulkhead"]:
        net.add("BAY", v["c_bay"])
        net.add("BW", a_bw * tw * c_petg, wall=(a_bw, tw, kp, "PETG"))
        net.link("BAY", "BW", wall_in("BW", "BAY", a_bw))
        net.link("BW", "AMB", wall_out("BW", a_bw))
        if rad_bw is not None:
            net.link("SINK", "BW", rad_bw)
        a_bh, t_bh = v["a_bh"], v["t_bh"]
        for w in ("BH1", "BH2"):
            net.add(w, a_bh * t_bh * c_petg, wall=(a_bh, t_bh, kp, "PETG"))
        net.link("BAY", "BH1", lambda T: 1.0 / (1.0 / (hin(T["BAY"], T["BH1"]) * a_bh) + t_bh / (2 * kp * a_bh)))
        net.link("BH1", "BH2", lambda T: 1.0 / (t_bh / (kp * a_bh) + 1.0 / ((v["k_air"] / v["gap_bh"] + h_rad(T["BH1"], T["BH2"], v["eps_bh"])) * a_bh)))
        net.link("BH2", "MAIN", lambda T: 1.0 / (1.0 / (hin(T["BH2"], T["MAIN"]) * a_bh) + t_bh / (2 * kp * a_bh)))
        if rad_bh is not None:
            net.link("SINK", "BH1", rad_bh)
        net.link("BAY", "MAIN", v["g_leads"])
        va = v["vent_area_dc"] if L.get("dc") else v["vent_area"]
        if L["vent"] and va > 0:
            net.link("BAY", "AMB", g_stack(va, v["h_stack_bay"], "BAY"))
    # ---- main bay
    net.add("MAIN", v["c_main"])
    a_mw = v["a_mw"] if L["bulkhead"] else v["a_mw"] + a_bw
    net.add("MW", a_mw * tw * c_petg, wall=(a_mw, tw, kp, "PETG"))
    net.link("MAIN", "MW", wall_in("MW", "MAIN", a_mw))
    net.link("MW", "AMB", wall_out("MW", a_mw))
    if not L["bulkhead"] and rad_bw is not None:
        net.link("SINK", "MW", rad_bw)
    if L.get("main_vent") and v["main_vent_area"] > 0:
        net.link("MAIN", "AMB", g_stack(v["main_vent_area"], v["h_stack_main"], "MAIN"))
    net.add("CELL", v["c_cell"])
    net.link("CELL", "MAIN", v["g_cell_main"])
    net.link("CELL", "MW", v["g_cell_wall"])
    # ---- sources (key-dependent: PA, GVA, LPF loss, feed I2R; session-constant: relay, LM2940, Pico)
    if fin == "A5":
        net.src(bay, v["p_gva"])
    net.src(bay, d["p_lpf"])
    p_rl = v["p_relay"] * (v["relay_hold"] if L.get("dc") else 1.0)
    net.src(bay, p_rl, p_rl)
    # the PWM relay hold also lowers the LM2940 current by the coil current (p_relay / 5 V) x (1 - hold)
    # at the LM2940 drop (8.4 - 0.5 - 5 V = 2.9 V at the corner)
    i_coil = v["p_relay"] / 5.0
    p_lm = v["p_lm2940"] - (i_coil * (1.0 - v["relay_hold"]) * (v["v_pack"] - 0.5 - 5.0) if L.get("dc") else 0.0)
    net.src("MAIN", p_lm, p_lm)
    net.src("MAIN", v["p_pico"], v["p_pico"])
    net.src("MAIN", d["p_feed_board"], v["i_bus"] ** 2 * max(v["r_feed"] - v["r_cellpath"], 0.0))
    net.src("CELL", d["p_feed_cells"], v["i_bus"] ** 2 * v["r_cellpath"])
    net.names = sorted(set(net.names), key=net.names.index)
    return net


def inhibit_run(net: Net, v: dict, set_c: float, tol: float, demand: Callable[[float], float], t_end: float,
                dt: float = 0.1, x0: dict | None = None):
    """Closed-loop transient with the REQ-SYS-118 inhibit acting on the PA-case NTC (revision 1, INSP
    finding-4). The NTC reading follows ntc_reading() through a first-order lag (tau_ntc_a5 or _a4). When
    the lagged reading reaches set_c + tol the RF ends t_resp later; transmit re-arms when the reading falls
    below set_c + tol - inh_hyst. demand(t) is the operator's key (0 or 1). Returns the junction trace, the
    reading trace, the true case trace and the list of (time, junction) at each RF-off moment."""
    n = len(net.names)
    C = np.array([net.cap[k] for k in net.names])
    x = np.array([x0[k] for k in net.names]) if x0 else np.full(n, net.t_amb)
    tau = v["tau_ntc_a5"] if net.meta["fin"] == "A5" else v["tau_ntc_a4"]
    a_f = 1.0 - np.exp(-dt / tau)
    jn = "J2" if net.meta["fin"] == "A5" else "J"
    ij, ic = net.names.index(jn), net.names.index("CASE")
    s = ntc_reading(net, net.tdict(x), v)
    trip = set_c + tol
    inhibited, t_rf_off = False, None
    steps = int(round(t_end / dt))
    ts = np.empty(steps + 1)
    tjs, rds, cas, keys = (np.empty(steps + 1) for _ in range(4))
    ts[0], tjs[0], rds[0], cas[0], keys[0] = 0.0, x[ij], s, x[ic], 0.0
    offs = []
    for k in range(1, steps + 1):
        t = k * dt
        rf = demand(t - 0.5 * dt) > 0.5 and not (inhibited and t_rf_off is not None and t - 0.5 * dt >= t_rf_off)
        G, b = net._matrix(net.tdict(x))
        x = np.linalg.solve(G + np.diag(C / dt), C / dt * x + net.power(1.0 if rf else 0.0) + b)
        s = s + a_f * (ntc_reading(net, net.tdict(x), v) - s)
        if not inhibited and s >= trip:
            inhibited, t_rf_off = True, t + v["t_resp"]
        elif inhibited and s < trip - v["inh_hyst"]:
            inhibited, t_rf_off = False, None
        if keys[k - 1] > 0.5 and not rf and demand(t - 0.5 * dt) > 0.5:  # RF ended by the inhibit
            offs.append((t, float(tjs[k - 1])))
        ts[k], tjs[k], rds[k], cas[k], keys[k] = t, x[ij], s, x[ic], 1.0 if rf else 0.0
    return dict(t=ts, tj=tjs, reading=rds, case=cas, key=keys, offs=offs, tj_max=float(tjs.max()))


def ntc_reading(net: Net, T: dict, v: dict) -> float:
    """Steady-state reading of the REQ-SYS-118 NTC on the PA case (revision 1, INSP finding-4): the A5
    NTC sits under a flange screw on the ear, pulled toward the sink; the A4 NTC sits on the top copper
    beyond the pad spreading resistance."""
    if net.meta["fin"] == "A5":
        return T["CASE"] - v["ntc_frac_a5"] * (T["CASE"] - T["SINK"])
    q = (T["CASE"] - T["SINK"]) / net.meta["r_cs"]
    return T["CASE"] - v["ntc_frac_a4"] * q * v["a4_r_pad"]


# ------------------------------------------------------------------------------------------ outputs
def tj(net: Net, T: dict) -> float:
    return T["J2"] if net.meta["fin"] == "A5" else T["J"]


def surfaces(net: Net, T: dict, v: dict | None = None) -> dict:
    """Outer-face temperature of each accessible PETG node (and the bare sink, for reference)."""
    v = v if v is not None else vals()
    tw, kp = v["t_wall"], v["k_petg"]
    out = {}
    for n in ("GUARD", "EF", "BW", "MW"):
        if n in T:
            h = v["h_out_c"] + h_rad(T[n], net.t_amb, v["eps_out"])
            ro, rw = 1.0 / h, tw / (2 * kp)
            out[n] = net.t_amb + (T[n] - net.t_amb) * ro / (ro + rw)
    out["SINK (if unguarded)"] = T["SINK"]
    if net.meta.get("fins_exposed"):
        out["SINK fin tips (rev 4: flush with case top and bottom)"] = T["SINK"]
    return out


def hot_faces(net: Net, T: dict, material: str | None = "PETG") -> dict:
    """Hot-face temperature of every wall node of the material (None = all): mid-plane plus the
    inflow from hotter nodes across half the wall (conduction t/2k)."""
    out = {}
    for n, (A, t, k, mat) in net.walls.items():
        if material is not None and mat != material:
            continue
        q = 0.0
        for a, b, fn in net.links:
            if n not in (a, b):
                continue
            o = b if a == n else a
            to = net.t_amb if o == "AMB" else T[o]
            if to > T[n]:
                q += fn(T) * (to - T[n])
        out[n] = T[n] + q * t / (2 * k * A)
    return out


def petg_hot_faces(net: Net, T: dict, v: dict | None = None) -> dict:
    return hot_faces(net, T, "PETG")
