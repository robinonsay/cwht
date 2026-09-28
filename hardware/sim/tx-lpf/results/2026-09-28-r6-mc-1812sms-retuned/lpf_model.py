"""Model data for the TS-012 transmit harmonic low-pass filter (WP-PDR-21).

Single source of every number the LTspice decks and the harmonic budget use: the filter design
(7-pole 0.1 dB Chebyshev, ripple cut-off 165 MHz, TS-012 section 7.3 and BOM rows 4, 5 and E1),
the component parasitic models (Coilcraft 1812SMS, hand-wound 24 AWG air coils, KEMET 1206 C0G),
the Monte Carlo ranges, the 47 CFR 97.307(e) limit and the PA harmonic inputs of each finalist.

Every value is tagged in SOURCES with its origin and whether it is a datasheet value (D), a derived
value (C, computed here) or an estimate (E). The analysis record docs/design/analysis/lpf-ts012.md
reproduces the table.
"""
from __future__ import annotations

import math

import numpy as np

# ---------------------------------------------------------------------------------------------
# Band, harmonics and the regulatory limit
# ---------------------------------------------------------------------------------------------
F_LO, F_HI = 144.0e6, 148.0e6            # transmit range (REQ-SYS-008)
HARMONICS = list(range(2, 11))           # 2f .. 10f; 10f of 148 MHz is 1480 MHz (span 1.5 GHz, REQ-TX-007)
Z0 = 50.0


def harmonic_band(n: int) -> tuple[float, float]:
    return n * F_LO, n * F_HI


def limit_97307e_w(p_carrier_w: float) -> float:
    """47 CFR 97.307(e), transmitter of mean power 25 W or less, 30 to 225 MHz (eCFR 2026-09-23,
    docs/references/md/regulatory/47cfr-97.307.md): a spurious emission must not exceed 25 uW and must
    be at least 40 dB below the fundamental, but need not be reduced below 10 uW.
    Returns the highest permitted spurious mean power in watts."""
    if p_carrier_w > 25.0:
        raise ValueError("the 25 W or less clause does not apply")
    return max(10e-6, min(25e-6, p_carrier_w * 1e-4))


def w_to_dbm(p_w: float) -> float:
    return 10.0 * math.log10(p_w * 1e3)


# Power steps (REQ-SYS-011 0.5, 1, 2 W within +/-1 dB; REQ-SYS-012 5 W step), evaluated at +1 dB
POWER_STEPS_W = [0.5, 1.0, 2.0, 5.0]
STEP_TOL_DB = 1.0
TARGET_DBC_5W = 60.0                     # REQ-SYS-018 design margin at the 5 W step (ADR-022)

# Requirement allocations to the filter (REQ-TX-009, 010, 011; TBR), attenuation at the filter terminals
REQ_TX = [
    ("REQ-TX-009", 288e6, 296e6, 40.0),
    ("REQ-TX-010", 432e6, 444e6, 35.0),
    ("REQ-TX-011", 576e6, 1500e6, 40.0),
]
IL_MAX_DB = 0.5                           # passband insertion loss goal at 144 to 148 MHz (TS-012 7.3, F17)

# ---------------------------------------------------------------------------------------------
# PA harmonic inputs at the PA output (before the LPF), dBc, per finalist
# ---------------------------------------------------------------------------------------------
# A5: Mitsubishi RA07M1317M datasheet (Jun 2019) 2fo -25 dBc max, 3fo -30 dBc max at Pout 6 W, VDD 7.2 V,
#     VGG adjusted (docs/research/pa-device-candidates.md F8, F16). Guaranteed only at 6 W. At the lower
#     steps the module is backed off by VGG, where the discrete Mitsubishi line-up (AN-VHF-053-A, F4)
#     shows the 2fo ratio rising to -17.4 dBc at 0.3 W: taken as -17 dBc (E). 3f and above at the lower
#     steps: -25 dBc (E, the 3fo guarantee degraded by 5 dB; the line-up's worst 3fo is -50 dBc).
#     4f and above have no data: taken equal to the 3f value of the same step (E).
# A4: NXP AFT05MS004N datasheet Rev. 0, 7/2014 carries no harmonic data (text of the datasheet
#     searched 2026-09-28: no 'harmonic' or 'dBc' entry). The assumption of pa-device-candidates.md F17
#     for a raw single-ended class-AB stage is used at every step: 2fo -15 dBc, 3fo and above -20 dBc (E).
PA_HARMONICS = {
    "A5": {
        "name": "A5 (RA07M1317M module)",
        "full": {2: -25.0, "hi": -30.0},     # 5 W step; datasheet maxima (D)
        "backoff": {2: -17.0, "hi": -25.0},  # 0.5, 1, 2 W steps and ramp instants (E)
        "basis_full": "datasheet maximum at 6 W (D)",
        "basis_backoff": "estimate: AN-VHF-053-A gate-ramp worst ratio (E)",
    },
    "A4": {
        "name": "A4 (AFT05MS004N, hand match)",
        "full": {2: -15.0, "hi": -20.0},     # no vendor data; F17 assumption (E)
        "backoff": {2: -15.0, "hi": -20.0},
        "basis_full": "no vendor data; F17 class-AB assumption (E)",
        "basis_backoff": "no vendor data; F17 class-AB assumption (E)",
    },
}


def pa_harmonic_dbc(alt: str, n: int, step_w: float) -> float:
    d = PA_HARMONICS[alt]["full" if step_w >= 5.0 else "backoff"]
    return d[2] if n == 2 else d["hi"]


# ---------------------------------------------------------------------------------------------
# Filter design: 7-pole Chebyshev, 0.1 dB ripple, ripple cut-off 165 MHz, shunt-C first
# ---------------------------------------------------------------------------------------------
N_POLES = 7
RIPPLE_DB = 0.1
FC = 165e6


def chebyshev_g(n: int, ripple_db: float) -> list[float]:
    """Prototype element values g1..gn (Matthaei, Young and Jones, eq. 4.05-2)."""
    beta = math.log(1.0 / math.tanh(ripple_db / 17.37))
    gam = math.sinh(beta / (2 * n))
    a = [math.sin((2 * k - 1) * math.pi / (2 * n)) for k in range(1, n + 1)]
    b = [gam ** 2 + math.sin(k * math.pi / n) ** 2 for k in range(1, n + 1)]
    g = [2 * a[0] / gam]
    for k in range(2, n + 1):
        g.append(4 * a[k - 2] * a[k - 1] / (b[k - 2] * g[-1]))
    return g


def design_values() -> list[float]:
    """Exact element values: C1, L2, C3, L4, C5, L6, C7 (farad, henry)."""
    w = 2 * math.pi * FC
    out = []
    for i, gk in enumerate(chebyshev_g(N_POLES, RIPPLE_DB)):
        out.append(gk / (w * Z0) if i % 2 == 0 else gk * Z0 / w)
    return out


def chebyshev_att_db(f: np.ndarray) -> np.ndarray:
    """Analytic attenuation of the ideal lossless prototype (known answer)."""
    eps2 = 10 ** (RIPPLE_DB / 10) - 1
    x = np.asarray(f, dtype=float) / FC
    t = np.where(x <= 1, np.cos(N_POLES * np.arccos(np.minimum(x, 1.0))),
                 np.cosh(N_POLES * np.arccosh(np.maximum(x, 1.0))))
    return 10 * np.log10(1 + eps2 * t ** 2)


# BOM values (TS-012 section 8.3 rows 4, 5, E1): 22 pF, 68 nH, 39 pF, 82 nH, 39 pF, 68 nH, 22 pF
BOM = [22e-12, 68e-9, 39e-12, 82e-9, 39e-12, 68e-9, 22e-12]
# Retuned set (this analysis, run r6 and r7): the same three coils, shunt capacitors 18 and 33 pF, chosen
# by retune_screen.py to move the parasitic-loaded cut-off back up (lowest worst-corner passband loss
# among the sets that keep 45 dB at 288 to 296 MHz and 40 dB at 432 to 444 MHz with no new coil value)
RETUNE = [18e-12, 68e-9, 33e-12, 82e-9, 33e-12, 68e-9, 18e-12]
COIL_POS = [1, 3, 5]      # indexes of the series inductors in BOM
CAP_POS = [0, 2, 4, 6]

# ---------------------------------------------------------------------------------------------
# Component models
# ---------------------------------------------------------------------------------------------
# Coilcraft 1812SMS Midi Spring, Document 184-1 revised 12/02/21 (read 2026-09-28 at
# https://www.coilcraft.com/getmedia/c6fe1f83-b176-469d-a071-e2edb068fef2/midi.pdf):
#   68N: L tested at 150 MHz, tolerance 5 % (J) or 2 % (G), Q typ 120 min 100 at 150 MHz, SRF min 1.5 GHz
#   82N: Q typ 120 min 100 at 150 MHz, SRF min 1.3 GHz. The BOM orders J (5 %).
#   (47N: Q typ 135 min 100, SRF min 2.1 GHz; 56N: Q typ 125 min 100, SRF min 1.5 GHz; used by the retune)
COILCRAFT = {47e-9: {"q_min": 100.0, "q_typ": 135.0, "srf_min": 2.1e9},
             56e-9: {"q_min": 100.0, "q_typ": 125.0, "srf_min": 1.5e9},
             68e-9: {"q_min": 100.0, "q_typ": 120.0, "srf_min": 1.5e9},
             82e-9: {"q_min": 100.0, "q_typ": 120.0, "srf_min": 1.3e9}}
Q_FREQ = 150e6

# KEMET C0G 1206 (C1206C220J1GACTU, C1206C390J1GACTU): tolerance J = +/-5 % (part number, D).
# ESR and ESL were not read from KEMET K-SIM: ESR 0.1 to 0.4 ohm at 100 to 500 MHz and body ESL
# 0.6 to 1.2 nH are typical published ranges for 1206 C0G MLCCs (E).
CAP_ESR = (0.1, 0.2, 0.4)          # min, nominal, max (E)
CAP_ESL = (0.6e-9, 1.0e-9, 1.2e-9)  # (E)

# Board (JLCPCB 2-layer FR4, ground pour on the bottom layer under the filter; RF board thickness
# not yet fixed: 0.8 or 1.6 mm, TS-012 8.1 and A4 match note)
EPS_R = 4.5                          # JLCPCB FR4 datasheet value about 4.5 at 1 GHz (E, not read today)


def via_inductance(h_mm: float, d_mm: float = 0.3) -> float:
    """Single through via, Goldfarb-style closed form L = 0.2 h (ln(4h/d) + 1) nH (C)."""
    return 0.2e-9 * h_mm * (math.log(4 * h_mm / d_mm) + 1)


def pad_cap(area_mm2: float, h_mm: float) -> float:
    return 8.854e-12 * EPS_R * area_mm2 * 1e-6 / (h_mm * 1e-3)


# Ground connection of each shunt capacitor: one via at 1.6 mm (1.3 nH) to two vias at 0.8 mm (0.27 nH)
VIA_L = (via_inductance(0.8) / 2, via_inductance(1.6) / 2 + 0.2e-9, via_inductance(1.6))  # (C)
# Node pad capacitance: 1206 pad (1.6 x 1.8 mm) + one or two coil pads (2.62 x 1.48 mm, Coilcraft
# land pattern), 1.6 mm to 0.8 mm dielectric (C)
_node_min = pad_cap(1.6 * 1.8 + 2.62 * 1.48, 1.6)
_node_max = pad_cap(1.6 * 1.8 + 2 * 2.62 * 1.48, 0.8)
PAD_C = (_node_min, 0.5 * (_node_min + _node_max), _node_max)
# Series trace inductance per coil (two short tracks joining coil pads to cap pads) (E)
TRACE_L = (0.5e-9, 1.0e-9, 2.0e-9)
# Stray capacitance pad to pad across a coil (fringe across the 1.7 mm gap) (E)
ACROSS_C = (0.02e-12, 0.05e-12, 0.08e-12)
# Mutual coupling between adjacent coils (parallel axes, about 8 to 10 mm apart) (E)
K_1812 = (1e-4, 0.005, 0.01)
K_AIR = (1e-4, 0.015, 0.03)
# Layout leakage around the filter (E): direct input-to-output capacitance between the end nodes and
# pads with a bottom ground pour (0.0005 to 0.005 pF), and coupling between the first and last coils
K26_1812 = (1e-4, 0.001, 0.003)
K26_AIR = (1e-4, 0.002, 0.006)
C_IO = (0.5e-15, 2e-15, 5e-15)

# ---------------------------------------------------------------------------------------------
# Hand-wound air coils, 24 AWG enamelled copper (owner's wire), wound on a 3.0 mm drill shank
# ---------------------------------------------------------------------------------------------
AWG24_BARE_MM = 0.511                 # ASTM B258 nominal (D)
AWG24_OD_MM = 0.56                    # single to heavy build enamel (E)
FORM_MM = 3.0
PITCH_MM = 1.0                        # spaced about one wire diameter, so the coil can be squeezed
LEAD_MM = 3.0                         # each lead from the last turn to the pad
RHO_CU = 1.72e-8
MU0 = 4e-7 * math.pi


def nagaoka(ratio_d_over_l: float) -> float:
    """Nagaoka coefficient, Lundin's closed form (accurate to about 3 ppm)."""
    x = ratio_d_over_l
    if x <= 1:
        return ((1 + 0.383901 * x ** 2 + 0.017108 * x ** 4) / (1 + 0.258952 * x ** 2)
                - 4 * x / (3 * math.pi))
    y = 1 / x
    return (2 * y / math.pi) * ((math.log(4 * x) - 0.5) *
                                (1 + 0.383901 * y ** 2 + 0.017108 * y ** 4) / (1 + 0.258952 * y ** 2)
                                + 0.093842 * y ** 2 + 0.002029 * y ** 4 - 0.000801 * y ** 6)


def solenoid_l(n_turns: float, d_mean_mm: float, pitch_mm: float) -> float:
    """Current-sheet inductance with Nagaoka's factor and Rosa's round-wire correction (C)."""
    d = d_mean_mm * 1e-3
    length = n_turns * pitch_mm * 1e-3
    area = math.pi * d * d / 4
    l_sheet = MU0 * n_turns ** 2 * area / length * nagaoka(d / length)
    # Rosa correction for round wire spacing (small; ks + km approximation)
    ks = 1.25 - math.log(2 * pitch_mm / AWG24_BARE_MM)
    km = 0.33
    dl = MU0 * n_turns * d / 4 * (ks + km)   # Rosa: 2 pi a N (A + B) nH, a in cm
    return l_sheet - dl


def lead_l(length_mm: float, dia_mm: float = AWG24_BARE_MM) -> float:
    l = length_mm * 1e-3
    r = dia_mm * 1e-3 / 2
    return 2e-7 * l * (math.log(2 * l / r) - 0.75)


def medhurst_c(d_mean_mm: float, length_mm: float) -> float:
    """Medhurst self-capacitance C = H D, H(l/D) fit in pF/cm (C, Low accuracy near SRF)."""
    x = length_mm / d_mean_mm
    h = 0.1126 * x + 0.08 + 0.27 / math.sqrt(x)
    return h * d_mean_mm / 10 * 1e-12


def air_coil(target_l: float, f: float = 146e6) -> dict:
    """Turns for the target inductance including two leads and the Q and SRF estimates."""
    d_mean = FORM_MM + AWG24_OD_MM
    leads = 2 * lead_l(LEAD_MM)
    n = 1.0
    while solenoid_l(n, d_mean, PITCH_MM) + leads < target_l:
        n += 0.25
    l_coil = solenoid_l(n, d_mean, PITCH_MM) + leads
    wire_len = n * math.pi * d_mean * 1e-3 + 2 * LEAD_MM * 1e-3
    delta = math.sqrt(RHO_CU / (math.pi * f * MU0))
    r_skin = RHO_CU * wire_len / (math.pi * AWG24_BARE_MM * 1e-3 * delta)
    prox = 1.8          # Medhurst proximity factor for pitch/diameter about 2 and l/D about 1.5 (E)
    r_ac = r_skin * prox
    q = 2 * math.pi * f * target_l / r_ac
    c_self = medhurst_c(d_mean, n * PITCH_MM)
    srf = 1 / (2 * math.pi * math.sqrt(target_l * c_self))
    return {"target_nH": target_l * 1e9, "turns": n, "length_mm": n * PITCH_MM, "d_mean_mm": d_mean,
            "l_calc_nH": l_coil * 1e9, "wire_mm": wire_len * 1e3, "r_ac_ohm": r_ac, "q_146": q,
            "c_self_pF": c_self * 1e12, "srf_GHz": srf / 1e9}


# ---------------------------------------------------------------------------------------------
# Monte Carlo sampling (uniform within the stated bounds; fixed seeds)
# ---------------------------------------------------------------------------------------------

def _u(rng, lo, hi, size=None):
    return rng.uniform(lo, hi, size)


def coil_params(kind: str, l_nom: float, rng=None, tol: float | None = None, corner: int = 0) -> dict:
    """Series-branch element values for one coil: L, R, Cpar, Ltrace. corner = -1/+1 gives the
    tolerance extreme with nominal parasitics; rng None and corner 0 gives the nominal."""
    if kind == "1812":
        spec = COILCRAFT[l_nom]
        tol = 0.05 if tol is None else tol
        q_rng = (spec["q_min"], 130.0)   # min 100 to typ 120 plus 10 (E above typ)
        q_nom = spec["q_min"]            # nominal taken at the minimum Q (conservative in band)
        srf_lo = spec["srf_min"]
        srf_rng = (srf_lo, 1.3 * srf_lo)
        srf_nom = srf_lo
    else:
        a = air_coil(l_nom)
        tol = 0.10 if tol is None else tol
        q_nom = a["q_146"] * 0.8
        q_rng = (a["q_146"] * 0.6, a["q_146"] * 1.0)
        srf_nom = a["srf_GHz"] * 1e9
        srf_rng = (srf_nom / math.sqrt(1.5), srf_nom / math.sqrt(0.5))   # Cself x0.5..x1.5
    if rng is None:
        l = l_nom * (1 + corner * tol)
        q, srf = q_nom, srf_nom
        cacr, ltr = ACROSS_C[1], TRACE_L[1]
    else:
        l = l_nom * (1 + _u(rng, -tol, tol))
        q = _u(rng, *q_rng)
        srf = _u(rng, *srf_rng)
        cacr = _u(rng, ACROSS_C[0], ACROSS_C[2])
        ltr = _u(rng, TRACE_L[0], TRACE_L[2])
    r = 2 * math.pi * (Q_FREQ if kind == "1812" else 146e6) * l / q
    cpar = 1 / ((2 * math.pi * srf) ** 2 * l)
    return {"L": l, "R": r, "C": cpar + cacr, "Ltr": ltr, "Q": q, "SRF": srf}


def cap_params(c_nom: float, rng=None, tol: float = 0.05, corner: int = 0) -> dict:
    if rng is None:
        return {"C": c_nom * (1 + corner * tol), "ESR": CAP_ESR[1], "ESL": CAP_ESL[1],
                "Lvia": VIA_L[1], "Cpad": PAD_C[1]}
    return {"C": c_nom * (1 + _u(rng, -tol, tol)), "ESR": _u(rng, CAP_ESR[0], CAP_ESR[2]),
            "ESL": _u(rng, CAP_ESL[0], CAP_ESL[2]), "Lvia": _u(rng, VIA_L[0], VIA_L[2]),
            "Cpad": _u(rng, PAD_C[0], PAD_C[2])}


def sample_filter(kind: str, rng=None, coil_tol: float | None = None, corner: int = 0,
                  vals: list[float] | None = None) -> dict:
    """One filter instance: dict of named parameters for the deck."""
    vals = BOM if vals is None else vals
    p = {}
    for i in CAP_POS:
        c = cap_params(vals[i], rng, corner=corner)
        for k, v in c.items():
            p[f"C{i + 1}{k}"] = v
    for i in COIL_POS:
        c = coil_params(kind, vals[i], rng, coil_tol, corner)
        for k, v in c.items():
            p[f"L{i + 1}{k}"] = v
    kr = K_1812 if kind == "1812" else K_AIR
    k26 = K26_1812 if kind == "1812" else K26_AIR
    if rng is None:
        p["K24"] = p["K46"] = kr[1]
        p["K26"] = k26[1]
        p["Cio"] = C_IO[1]
    else:
        p["K24"] = _u(rng, kr[0], kr[2])
        p["K46"] = _u(rng, kr[0], kr[2])
        p["K26"] = _u(rng, k26[0], k26[2])
        p["Cio"] = _u(rng, C_IO[0], C_IO[2])
    return p


PARAM_ORDER = (
    [f"C{i + 1}{k}" for i in CAP_POS for k in ("C", "ESR", "ESL", "Lvia", "Cpad")]
    + [f"L{i + 1}{k}" for i in COIL_POS for k in ("L", "R", "C", "Ltr", "Q", "SRF")]
    + ["K24", "K46", "K26", "Cio"])
