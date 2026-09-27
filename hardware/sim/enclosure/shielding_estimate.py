#!/usr/bin/env python3
"""Shielding and bond estimate per enclosure option (docs/design/analysis/shielding-estimate.md).

Question: does each enclosure option give REQ-SYS-177 its 20 dB (TBR) at the digital and
switching-converter frequencies, and does a sprayed coating meet the REQ-SYS-109 bond value
(0.1 ohm TBR) from its farthest point?

Wall model: exact transmission of a uniform conductive slab (thickness t, conductivity s) in a
medium of wave impedance Zw on both sides (Schelkunoff form):
    T = 1 / (cosh(g t) + 0.5 (Zw/Zm + Zm/Zw) sinh(g t)),  g = (1 + j)/delta,  Zm = (1 + j)/(s delta).
It covers the thin-film case (a coating of sheet resistance Rs, t << delta) and the thick-wall
case (6061). Zw = 377 ohm for the radiated (plane-wave) reading of REQ-SYS-177, and
Zw = 2 pi f mu0 r for the magnetic near field at source-to-wall distance r (the H-field probe
reading, status note section 3 row 8).
Apertures: amplitude transmission 2 L_i / lambda for L_i < lambda/2 (else 1), reduced by the
below-cutoff attenuation 27.3 d/L_i dB of an opening of depth d (the wall thickness) or of a
joint lip. Joints: slots of the contact spacing (3 mm with a continuous conductive gasket; the
variant with screws every 15 mm and no gasket is also computed). The display window may carry an
ITO film (thin sheet of WINDOW_FILM_RS). Wall and leaks add in power (random phase):
T = sqrt(T_wall^2 + sum T_i^2).
Verdict bands (revision 0): 12 to 600 MHz (min of plane wave and H field), 1.5 and 2.2 MHz (H field), and the
1 GHz edge reported as marginal when within 3 dB of 20 dB.
Revision 1 (INSP-083 finding-1): every clock and switching-converter source of the WP-PDR-20 clock plan
(docs/design/analysis/clock-plan.md revision 2 at 4153acf, sections 2 and 2.1) with every harmonic to
1.5 GHz (TC-SYS-107 step 1), converter harmonics between 1.5 and 12 MHz included. Per source and option the
lowest total (min of plane wave and H field) over its harmonics is reported with a verdict: "fail" below
20 dB, "not shown" when the margin is below the case's uncertainty (6 dB: the aperture and joint terms,
and the H-field wall term through the source distance; E3 of the analysis checklist), else "pass". The
limiting term (wall or openings) is reported with it. Two
opening sets are computed: "rev0" (the openings of revision 0) and "rev1" (the opening rules O1 to O3 of
the analysis note section 7).
Revision 2 (INSP-083 finding-5): the plug-inserted state. Below-cutoff attenuation exists only for an empty
opening: with a 3.5 mm plug in a jack, the plug sleeve and the collar form a coaxial line with no cutoff, and
the plug's tip and ring conductors leave the shield on the cable. Every port state is computed:
  "rev1_plug"  rules O1 to O3 of revision 1 with the key and phones plugs and a USB cable inserted: each jack
               term is its 9 mm opening with no depth credit (aperture only), the USB term is the mated
               plug-shell seam; the unfiltered jack conductors are not bounded by any model here, so no case
               of this state can be a pass (the verdict is capped at "not shown");
  "rev2"       rules O1, O2 (revision 2), O3 and O4, every port empty: each jack is a metal-nose jack whose
               nose is its sleeve contact, bonded all round to the collar by a conductive gasket ring, so its
               leaks are the contact ring (8 slots of 3 mm at the wall depth, the O3 model) and the empty nose
               bore (3.6 mm, 5 mm deep);
  "rev2_plug"  as rev2 with the key and phones plugs and a USB cable inserted: the bore is filled by the plug,
               whose sleeve is bonded at the wall through the nose, so the jack leaks are the contact rings;
               each tip and ring line leaves on the cable through its O4 filter at the jack pins (conducted
               term |H| = K_COUPLE x the filter's voltage transfer from a Z_SRC source into the Z_CM cable
               common-mode load, K_COUPLE = 1: the board-level noise is taken to appear in full on the line at
               the jack, a bound until the WP-PDR-37 layout); the USB term is the mated plug-shell seam, the
               USB conductors staying inside the cable shield that the plug shell bonds at the wall.
The governing revision 2 verdict per source is the worse of "rev2" and "rev2_plug" (TC-SYS-107 worst case).
Bond: two circular contacts of radius a1, a2 at distance d on a sheet Rs:
    R = Rs / (2 pi) * (ln(d/a1) + ln(d/a2)) + contact resistance.

Output is developer evidence (numpy and matplotlib have no TV record of their own).
Run:  .venv/bin/python hardware/sim/enclosure/shielding_estimate.py [--check]
Writes hardware/sim/enclosure/out/shielding.csv, out/shielding-sources.csv (every port state), out/bond.csv
and docs/reviews/PDR/figures/shielding-estimate.png. --check exits 1 if a verdict differs from EXPECTED,
EXPECTED_REV1, EXPECTED_REV2, EXPECTED_SCOPE or EXPECTED_BOND (the verdicts stated in the analysis note).
"""
from __future__ import annotations

import argparse
import cmath
import csv
import math
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "hardware/sim/enclosure/out"
PNG = ROOT / "docs/reviews/PDR/figures/shielding-estimate.png"

MU0 = 4e-7 * math.pi
C0 = 299_792_458.0
Z0 = 376.73
SE_REQ = 20.0            # dB, REQ-SYS-177 (TBR)
R_SRC = 0.010            # m, board to wall distance (8.5 mm front stack, rounded up; envelope drawing)
T_COAT = 50e-6           # m, dry film per coat set (recalled 1 to 2 mil class for aerosol EMI coatings, Low)

# Source frequencies (MHz) named by REQ-SYS-177 through the clock plan and the power tree:
SOURCES = {
    1.5: "charger boost (BQ25887 class)",
    2.2: "5 V buck (TPS62913 class)",
    12.0: "Pico 2 crystal",
    48.0: "USB PLL",
    144.0: "12th of 12 MHz, 3rd of 48 MHz",
    150.0: "RP2350 system clock",
    300.0: "2nd of 150 MHz",
    600.0: "4th of 150 MHz",
    750.0: "5th of 150 MHz",
    900.0: "6th of 150 MHz",
    1050.0: "7th of 150 MHz",
    1200.0: "8th of 150 MHz, 25th of 48 MHz",
    1500.0: "10th of 150 MHz, 60th of 25 MHz (TC-SYS-107 upper edge)",
}

# Materials: (conductivity S/m, thickness m)
def coating(rs: float):
    return (1.0 / (rs * T_COAT), T_COAT)

AL6061 = (2.5e7, 1.5e-3)       # 6061-T6 about 40 % IACS; wall 1.5 mm (concept 7.8)
CU_PCB = (5.8e7, 70e-6)        # PCB plate, 1 oz both faces bonded, treated as 70 um copper

# Apertures common to every option (max linear dimension, m): USB opening 12 x 10 mm
# (ICD-CTL-USB), two jack openings, two encoder holes. The display window (24 x 24 mm, diagonal
# 34 mm) is handled separately because a transparent conductive film can cover it.
APERTURES_COMMON = [0.0156, 0.009, 0.009, 0.0084, 0.0084]
WINDOW = 0.034
WINDOW_FILM_RS = 10.0          # ohm/sq, ITO-coated PET film behind the lens (recalled class value, Low)
SEAM_SPACING = 0.003           # m, equivalent contact spacing of a joint with a continuous conductive gasket
SEAM_SPACING_SCREWS = 0.015    # m, variant: bond screws every 15 mm, no gasket
SEAM_OVERLAP = 0.003           # m, overlapping lip depth of every joint (design rule proposed here)
WALL_DEPTH = {"A": 0.0015, "B": 0.0016, "C1": 0.0020, "D": 0.0020}  # m, below-cutoff depth of each opening
SEAM_LENGTH = {"A": 0.42, "B": 0.56, "C1": 0.66, "D": 0.56}  # m of joint per option (envelope drawing)

OPTIONS = {
    "A": dict(label="A: 6061 wall 1.5 mm", wall=AL6061),
    "B": dict(label="B: PCB plate, 70 um Cu", wall=CU_PCB),
    "C1": dict(label="C1: coating 0.03 ohm/sq", wall=coating(0.03)),
    "D": dict(label="D: coated printed face", wall=coating(0.03)),
}
COATINGS = {"0.01 ohm/sq (silver class)": 0.01, "0.03 ohm/sq (design value)": 0.03,
            "0.1 ohm/sq": 0.1, "0.7 ohm/sq (nickel class)": 0.7, "20 ohm/sq (carbon class)": 20.0}

# Revision 1 source inventory: (name, fundamental MHz, relative tolerance, basis). Clock plan revision 2
# (docs/design/analysis/clock-plan.md sections 2 and 2.1). Every placeable clock that runs in operation or
# at boot, every switching converter (running or not in operation), and the four residual sources.
CLOCK_SOURCES = [
    ("XOSC 12 MHz (clk_ref)", 12.0, 65e-6, "clock plan section 2"),
    ("clk_usb and clk_adc 48 MHz", 48.0, 65e-6, "clock plan section 2"),
    ("clk_sys 150 MHz", 150.0, 65e-6, "clock plan section 2"),
    ("TCXO 25 MHz", 25.0, 2.5e-6, "clock plan section 2; TS-007"),
    ("SPI SCK 18.75 MHz (synthesizer)", 18.75, 65e-6, "clock plan rule 4"),
    ("QSPI SCK 37.5 MHz", 37.5, 65e-6, "clock plan section 2"),
    ("QSPI SCK 12.5 MHz (boot, flash program)", 12.5, 65e-6, "clock plan section 2"),
    ("PCM1808 SCKI 12.5 MHz (only if TS-001 keeps B)", 12.5, 65e-6, "clock plan section 2"),
    ("BFO 9.0 to 10.7 MHz (IF-dependent)", 9.85, 0.0863, "clock plan section 4 (IF 9.000 to 10.7 MHz, WP-PDR-19)"),
    ("prescaler 18 MHz (TX only, 144 to 148 / 8)", 18.0, 0.014, "clock plan section 2"),
    ("5 V buck 2.4 MHz (synchronised)", 2.4, 65e-6, "clock plan rule 6"),
    ("charger boost 1.5 MHz +/-10 % (off in operation)", 1.5, 0.10, "clock plan section 2; power research F20"),
    ("R-1 RP2350 core regulator 3 MHz typ", 3.0, 0.20, "clock plan 2.1 R-1 (no min or max: +/-20 % assumed, Low)"),
    ("R-2 Pico 2 RT6150, about 2 MHz (Low)", 2.0, 0.25, "clock plan 2.1 R-2; display research F10 (about 2 MHz, Low)"),
    ("R-3 TPA6130A2 charge pump 300 to 500 kHz", 0.4, 0.25, "clock plan 2.1 R-3"),
    ("R-4 I2C SCL 357 to 397 kHz", 0.377, 0.053, "clock plan 2.1 R-4"),
    ("audio and sidetone PWM 150 kHz", 0.15, 65e-6, "clock plan section 2"),
    ("RP2350 ROSC 4.6 to 24 MHz (boot only, rule 11)", 14.3, 0.678, "clock plan revision 2 section 2 (off in operation)"),
    ("R-5 RP2350 LPOSC 32.768 kHz +/-20 %", 0.032768, 0.20, "clock plan revision 2 section 2.1 R-5"),
]
F_MAX_MHZ = 1500.0         # TC-SYS-107 step 1: harmonics to 1.5 GHz
U_WALL_DB = 6.0            # uncertainty where the wall term dominates: Rs gives +/-2 dB, but the H-field wall term
                           # also moves by about 5 dB when the source is at 5 mm instead of 10 mm (INSP-083
                           # finding-2), so the note's overall 6 dB is used
U_OPEN_DB = 6.0            # uncertainty where openings and joints dominate (section 8)

# Revision 2 (INSP-083 finding-5): plug-inserted state and rules O2 (revision 2) and O4. Planning values (Low)
# until WP-PDR-38 chooses the parts and WP-PDR-37 places them.
JACK_BORE = (0.0036, 0.005)    # m: metal nose bore of an empty jack (3.6 mm) and its metal length (5 mm, Low)
USB_MATED_SEAM = (0.0069, 0.003)  # m: micro-USB plug shell long side in the receptacle shell, 3 mm engagement (Low)
Z_SRC = 50.0                   # ohm, source impedance of the board-level noise on a jack line (planning)
Z_CM = 150.0                   # ohm, common-mode impedance of the cable (the usual 150 ohm conducted-emission value,
                               # recalled, not in the corpus, Low)
K_COUPLE = 1.0                 # board-level noise on the jack line at the jack pins, relative to the source (bound)
CAP_ESL, CAP_ESR = 0.6e-9, 0.05  # H, ohm: 0402 shunt capacitor with its via (recalled class values, Low)
FILTERS = {
    # O4 filters, each from the jack pin to the bonded sleeve (the nose), within 5 mm of the pin:
    # key tip and ring: series 1 kohm thick film (0.05 pF parasitic) and 10 nF shunt
    "key": dict(kind="resistor", r=1000.0, c_par=0.05e-12, c_shunt=10e-9),
    # phones tip and ring: series ferrite bead of the 600 ohm at 100 MHz class (700 ohm, 1.2 uH, 0.5 pF, 0.05 ohm
    # DC) and 10 nF shunt (796 ohm at 20 kHz against a 32 ohm earphone; amplifier load check: WP-PDR-25)
    "phones": dict(kind="bead", r=700.0, l=1.2e-6, c_par=0.5e-12, r_dc=0.05, c_shunt=10e-9),
}
PLUG_LINES = ("key", "key", "phones", "phones")   # tip and ring of the key jack and of the phones jack

# Opening sets. rev0: the openings of revision 0 (USB 12 x 10 mm opening, diagonal 15.6 mm; jack holes 9 mm;
# encoder holes 8.4 mm; all at the wall depth). rev1: the opening rules of the note section 7 item 6:
#  O1 the micro-USB receptacle sits at the inner end of a coated printed shroud that joins the wall opening
#     to the receptacle shell, bonded to the shell by a conductive gasket, so the leak into the interior is
#     the receptacle mouth (about 7.5 x 2.5 mm, Low) with the receptacle's own 5 mm depth below cutoff;
#  O2 each 3.5 mm jack nose passes through a coated printed collar 6 mm deep behind the 2 mm wall, bonded to
#     the coating (depth 8 mm for the 9 mm opening);
#  O3 each encoder's metal bushing is bonded to the coated front wall by its nut and a toothed washer, so
#     the hole is closed by metal and leaks only at the contact ring, modelled as 8 slots of 3 mm with the
#     2 mm wall depth per encoder.
OPENINGS = {
    "rev0": lambda depth: [(0.0156, depth), (0.009, depth), (0.009, depth), (0.0084, depth), (0.0084, depth)],
    "rev1": lambda depth: [(0.0075, 0.005), (0.009, depth + 0.006), (0.009, depth + 0.006)] + [(0.003, depth)] * 16,
    # revision 2 (INSP-083 finding-5); every port state
    "rev1_plug": lambda depth: [USB_MATED_SEAM] * 2 + [(0.009, 0.0)] * 2 + [(0.003, depth)] * 16,
    "rev2": lambda depth: [(0.0075, 0.005)] + [JACK_BORE] * 2 + [(0.003, depth)] * 32,
    "rev2_plug": lambda depth: [USB_MATED_SEAM] * 2 + [(0.003, depth)] * 32,
}
# Port states: (opening set, filtered lines that leave on a cable, verdict capped at "not shown")
STATES = {
    "rev0": ("rev0", (), False),
    "rev1": ("rev1", (), False),
    "rev1_plug": ("rev1_plug", (), True),
    "rev2": ("rev2", (), False),
    "rev2_plug": ("rev2_plug", PLUG_LINES, False),
}

_DENSE = {"R-5 RP2350 LPOSC 32.768 kHz +/-20 %", "RP2350 ROSC 4.6 to 24 MHz (boot only, rule 11)", "5 V buck 2.4 MHz (synchronised)", "R-1 RP2350 core regulator 3 MHz typ", "R-2 Pico 2 RT6150, about 2 MHz (Low)",
          "R-3 TPA6130A2 charge pump 300 to 500 kHz", "R-4 I2C SCL 357 to 397 kHz", "audio and sidetone PWM 150 kHz",
          "charger boost 1.5 MHz +/-10 % (off in operation)"}
_NEAR_12 = {"XOSC 12 MHz (clk_ref)", "QSPI SCK 12.5 MHz (boot, flash program)",
            "PCM1808 SCKI 12.5 MHz (only if TS-001 keeps B)", "BFO 9.0 to 10.7 MHz (IF-dependent)"}
_ALL = {name for name, *_ in CLOCK_SOURCES}
EXPECTED_REV1 = {
    # option: (every source passes with the revision 0 openings; set failing with rules O1 to O3;
    #          set "not shown" with rules O1 to O3)
    "A": (False, set(), _ALL),       # every source's harmonics reach 1.5 GHz, where A has 25.4 dB (margin 5.4 dB)
    "B": (False, {"R-5 RP2350 LPOSC 32.768 kHz +/-20 %"},  # the PCB plate is thin at 33 kHz (14.3 dB)
          _ALL - {"R-5 RP2350 LPOSC 32.768 kHz +/-20 %"}),
    "C1": (False, _DENSE, _NEAR_12),
    "D": (False, _DENSE, _NEAR_12),
}

EXPECTED_REV2 = {
    # option: (set "fail" and set "not shown", worse of rev2 and rev2_plug; set "fail" of rev1_plug).
    # A and B fail the sources below about 5 MHz in the plugged state through the conducted bound of the jack
    # lines (K_COUPLE = 1); C1 and D fail them through the wall as well. Above 10 MHz nothing fails in any option,
    # and every source reaches the plugged 1.5 GHz case at 22.0 to 22.6 dB, margin under 6 dB (not shown).
    opt: (_DENSE, _ALL - _DENSE, _ALL) for opt in ("A", "B", "C1", "D")
}
SCOPE_MHZ = 10.0           # the lower edge of PCR-9 option (a)
EXPECTED_SCOPE = {"A": 22.0, "B": 22.1, "C1": 22.3, "D": 22.3}  # dB, lowest rev2_worst total from 10 MHz to 1.5 GHz
# (A and B at 1.5 GHz, plugged; C1 and D at 10 MHz, wall and plugged jack lines; 22.6 dB at 1.5 GHz)

EXPECTED = {
    # option: (12 to 600 MHz, design rules applied: min(plane wave, H field) total >= 20 dB,
    #          1.5 and 2.2 MHz: H-field total >= 20 dB,
    #          12 to 600 MHz with the display window open (no film): plane-wave total >= 20 dB,
    #          12 to 600 MHz with screw-only joints every 15 mm: plane-wave total >= 20 dB,
    #          750 to 1500 MHz, rev0 openings, rules applied: min(plane wave, H field) total >= 20 dB)
    "A": (True, True, False, False, False),
    "B": (True, True, False, False, False),
    "C1": (True, False, False, False, False),
    "D": (True, False, False, False, False),
}
EXPECTED_BOND = {("0.03", 2): True, ("0.03", 1): True, ("0.1", 2): False, ("0.7", 2): False}


def slab_se(f_hz: float, sigma: float, t: float, zw: complex) -> float:
    delta = 1.0 / math.sqrt(math.pi * f_hz * MU0 * sigma)
    g = (1 + 1j) / delta
    zm = (1 + 1j) / (sigma * delta)
    tr = 1.0 / (cmath.cosh(g * t) + 0.5 * (zw / zm + zm / zw) * cmath.sinh(g * t))
    return -20 * math.log10(abs(tr))


def zw_h(f_hz: float, r: float) -> complex:
    return complex(2 * math.pi * f_hz * MU0 * r, 0)


def aperture_t(f_hz: float, length: float, depth: float = 0.0) -> float:
    """Amplitude transmission of one slot of largest dimension `length`; `depth` adds the
    below-cutoff attenuation 27.3 depth/length dB of a lip or wall of that depth."""
    lam = C0 / f_hz
    t = 1.0 if length >= lam / 2 else 2 * length / lam
    return t * 10 ** (-(27.3 * depth / length) / 20)


def line_t(f_hz: float, name: str) -> float:
    """Conducted term of one jack line through its O4 filter (rule O4, revision 2): K_COUPLE times the
    magnitude of the filter's voltage transfer into Z_CM from a Z_SRC source, relative to no filter."""
    fl = FILTERS[name]
    w = 2 * math.pi * f_hz
    if fl["kind"] == "resistor":
        z_ser = 1 / (1 / fl["r"] + 1j * w * fl["c_par"])
    else:
        z_ser = fl["r_dc"] + 1 / (1 / fl["r"] + 1 / (1j * w * fl["l"]) + 1j * w * fl["c_par"])
    z_sh = CAP_ESR + 1j * w * CAP_ESL + 1 / (1j * w * fl["c_shunt"])
    z_p = z_sh * Z_CM / (z_sh + Z_CM)
    return K_COUPLE * abs((z_p / (Z_SRC + z_ser + z_p)) / (Z_CM / (Z_SRC + Z_CM)))


def total_se(f_hz: float, opt: str, zw: complex, film: bool = True, seam: float = SEAM_SPACING,
             openings: str = "rev0", wall_fraction: list | None = None, lines: tuple = ()) -> float:
    """Power (random-phase) sum of the wall and every leak: sqrt(T_wall^2 + sum T_i^2). When
    wall_fraction is a list, the wall term's share of the summed power is appended to it. `lines` adds
    the conducted term of each filtered jack line that leaves on a cable (revision 2, rule O4)."""
    sig, t = OPTIONS[opt]["wall"]
    depth = WALL_DEPTH[opt]
    terms = [10 ** (-slab_se(f_hz, sig, t, zw) / 20)]
    terms += [aperture_t(f_hz, length, dpt) for length, dpt in OPENINGS[openings](depth)]
    t_win = aperture_t(f_hz, WINDOW, depth)
    if film:
        fs, ft = (1.0 / (WINDOW_FILM_RS * 1e-6), 1e-6)
        t_win *= 10 ** (-slab_se(f_hz, fs, ft, zw) / 20)
    terms.append(t_win)
    n_seam = int(round(SEAM_LENGTH[opt] / seam))
    terms += [aperture_t(f_hz, seam, SEAM_OVERLAP)] * n_seam
    t_lines = [line_t(f_hz, name) for name in lines]
    terms += t_lines
    p_sum = sum(x * x for x in terms)
    if wall_fraction is not None:
        wall_fraction.append(terms[0] ** 2 / p_sum)
        wall_fraction.append(sum(x * x for x in t_lines) / p_sum)
    t_tot = min(1.0, math.sqrt(p_sum))
    return -20 * math.log10(t_tot)


GRID_MHZ = np.logspace(math.log10(0.02), math.log10(F_MAX_MHZ), 1400)


def curves(opt: str, state: str):
    """Total SE (min of plane wave and H field) and the wall share of the leak power on GRID_MHZ, for a
    port state of STATES."""
    openings, lines, _cap = STATES[state]
    se, share, lshare = [], [], []
    for fm in GRID_MHZ:
        f = fm * 1e6
        wf_p, wf_h = [], []
        p_ = total_se(f, opt, complex(Z0, 0), openings=openings, wall_fraction=wf_p, lines=lines)
        h_ = total_se(f, opt, zw_h(f, R_SRC), openings=openings, wall_fraction=wf_h, lines=lines)
        wf = wf_h if h_ <= p_ else wf_p
        se.append(min(h_, p_))
        share.append(wf[0])
        lshare.append(wf[1])
    return np.array(se), np.array(share), np.array(lshare)


def per_source(opt: str, openings: str, cache: dict) -> list[dict]:
    """Worst verdict over every harmonic (to F_MAX_MHZ) of every CLOCK_SOURCES entry, the tolerance band
    ends included. `openings` names a port state of STATES, or "rev2_worst", the lower of rev2 and
    rev2_plug at every frequency (the governing revision 2 case)."""
    key = (opt, openings)
    if key not in cache:
        if openings == "rev2_worst":
            a, b = cache[(opt, "rev2")], cache[(opt, "rev2_plug")]
            pick = a[0] <= b[0]
            cache[key] = tuple(np.where(pick, x, y) for x, y in zip(a, b))
        else:
            cache[key] = curves(opt, openings)
    se_c, share_c, lshare_c = cache[key]
    cap = openings in STATES and STATES[openings][2]
    lg = np.log10(GRID_MHZ)
    out = []
    rank = {"pass": 0, "not shown": 1, "fail": 2}
    for name, f0, tol, basis in CLOCK_SOURCES:
        n = np.arange(1, int(F_MAX_MHZ / (f0 * (1 - tol))) + 1)
        freqs = np.concatenate([n * f0 * (1 - tol), n * f0, n * f0 * (1 + tol)])
        freqs = freqs[(freqs >= GRID_MHZ[0]) & (freqs <= F_MAX_MHZ)]
        se = np.interp(np.log10(freqs), lg, se_c)
        share = np.interp(np.log10(freqs), lg, share_c)
        lshare = np.interp(np.log10(freqs), lg, lshare_c)
        unc = np.where(share > 0.5, U_WALL_DB, U_OPEN_DB)
        verdict = np.where(se < SE_REQ, "fail", np.where(se < SE_REQ + unc, "not shown", "pass"))
        if cap:
            verdict = np.where(verdict == "pass", "not shown", verdict)
        worst = max(verdict, key=lambda v: rank[v])
        i_min = int(np.argmin(se))
        fails = freqs[verdict == "fail"]
        out.append(dict(option=opt, openings=openings, source=name, fundamental_mhz=f0,
                        harmonics_to_1500=int(len(n)), min_se_db=round(float(se[i_min]), 1),
                        at_mhz=round(float(freqs[i_min]), 2), uncertainty_db=float(unc[i_min]),
                        limiting_term="wall" if share[i_min] > 0.5 else (
                            "jack lines (conducted)" if lshare[i_min] > 0.5 else "openings and joints"),
                        verdict=worst,
                        fail_span_mhz="" if len(fails) == 0 else f"{fails.min():.2f} to {fails.max():.2f}",
                        basis=basis))
    return out


def bond_r(rs: float, d: float, a1: float, a2: float, contact: float) -> float:
    return rs / (2 * math.pi) * (math.log(d / a1) + math.log(d / a2)) + contact


def evaluate():
    rows = []
    verdict = {}
    for opt in OPTIONS:
        hi_ok = lo_ok = open_ok = screws_ok = True
        edge = None
        for f_mhz, name in SOURCES.items():
            f = f_mhz * 1e6
            sig, t = OPTIONS[opt]["wall"]
            se_pw_wall = slab_se(f, sig, t, complex(Z0, 0))
            se_h_wall = slab_se(f, sig, t, zw_h(f, R_SRC))
            se_pw_tot = total_se(f, opt, complex(Z0, 0))
            se_h_tot = total_se(f, opt, zw_h(f, R_SRC))
            se_open = total_se(f, opt, complex(Z0, 0), film=False)
            se_screws = total_se(f, opt, complex(Z0, 0), seam=SEAM_SPACING_SCREWS)
            if f_mhz > 600.0:
                edge = min(edge if edge is not None else math.inf, se_pw_tot, se_h_tot)
            elif f_mhz >= 10.0:
                hi_ok &= min(se_pw_tot, se_h_tot) >= SE_REQ
                open_ok &= se_open >= SE_REQ
                screws_ok &= se_screws >= SE_REQ
            else:
                lo_ok &= se_h_tot >= SE_REQ
            rows.append(dict(option=opt, f_mhz=f_mhz, source=name,
                             se_plane_wall_db=round(se_pw_wall, 1), se_h_wall_db=round(se_h_wall, 1),
                             se_plane_total_db=round(se_pw_tot, 1), se_h_total_db=round(se_h_tot, 1),
                             se_plane_open_window_db=round(se_open, 1), se_plane_screw_joints_db=round(se_screws, 1)))
        verdict[opt] = (hi_ok, lo_ok, open_ok, screws_ok, edge >= SE_REQ)
    # bond: part 140 mm long; bond point washer radius 3.5 mm (M3 washer), probe tip 0.5 mm,
    # 0.010 ohm contact at the screw (Low). One bond point: farthest point 140 mm away;
    # two bond points at the ends: farthest point 70 mm from the nearer one.
    bond_rows, bond_ok = [], {}
    for rs in (0.01, 0.03, 0.1, 0.7):
        for n, d in ((1, 0.140), (2, 0.070)):
            r = bond_r(rs, d, 0.0035, 0.0005, 0.010)
            bond_rows.append(dict(rs_ohm_sq=rs, bond_points=n, farthest_mm=d * 1000, r_ohm=round(r, 4),
                                  meets_0p1=r <= 0.1))
            bond_ok[(f"{rs:g}", n)] = r <= 0.1
    src_rows, cache = [], {}
    for opt in OPTIONS:
        for openings in ("rev0", "rev1", "rev1_plug", "rev2", "rev2_plug", "rev2_worst"):
            src_rows += per_source(opt, openings, cache)
    return rows, verdict, bond_rows, bond_ok, src_rows, cache


def plot(cache, src_rows):
    f = np.logspace(math.log10(2e4), math.log10(1.5e9), 340)
    fig, (a1, a2, a3) = plt.subplots(1, 3, figsize=(20, 7.0), gridspec_kw=dict(width_ratios=[1, 1.15, 1.05]))
    for label, rs in COATINGS.items():
        sig, t = coating(rs)
        a1.semilogx(f / 1e6, [slab_se(x, sig, t, zw_h(x, R_SRC)) for x in f], lw=1.8, label=f"H, {label}")
    a1.semilogx(f / 1e6, [slab_se(x, *AL6061, zw_h(x, R_SRC)) for x in f], "k", lw=2.2, label="H, 6061 1.5 mm (off scale above 0.6 MHz)")
    sig, t = coating(0.03)
    a1.semilogx(f / 1e6, [slab_se(x, sig, t, complex(Z0, 0)) for x in f], "--", color="#c0504d", lw=1.8,
                label="plane wave, 0.03 ohm/sq")
    a1.axhline(SE_REQ, color="grey", ls=":", lw=1.2)
    a1.text(0.025, SE_REQ + 2, "REQ-SYS-177: 20 dB (TBR)", fontsize=9)
    a1.set_ylim(0, 160)
    a1.set_xlabel("frequency, MHz")
    a1.set_ylabel("wall shielding effectiveness, dB")
    a1.set_title(f"Wall only (no openings), source {R_SRC * 1000:.0f} mm from the wall", fontsize=10)
    a1.grid(alpha=0.3, which="both")
    a1.legend(fontsize=7.5, loc="upper left", ncol=1, framealpha=0.95)
    colors = {"A": "#1f4e79", "B": "#6b8e23", "C1": "#c0504d", "D": "#4bacc6"}
    lg = np.log10(GRID_MHZ)
    labels = {"rev0": "revision 0 openings", "rev1": "rules O1 to O3, ports empty",
              "rev2_worst": "rules O1 to O4, worse of empty and plugged"}
    for opt in ("A", "C1"):
        for openings, lw, ls in (("rev0", 1.0, ":"), ("rev1", 1.4, "--"), ("rev2_worst", 2.6, "-")):
            se_c = cache[(opt, openings)][0]
            a2.semilogx(GRID_MHZ, se_c, color=colors[opt], lw=lw, ls=ls, label=f"{opt}, {labels[openings]}")
    a2.axvline(SCOPE_MHZ, color="grey", ls="-.", lw=1)
    a2.text(SCOPE_MHZ * 1.1, 60, "10 MHz:\nPCR-9\noption (a)", fontsize=8)
    a2.axhspan(0, SE_REQ, color="#f4cccc", alpha=0.5, lw=0)
    a2.axhspan(SE_REQ, SE_REQ + U_OPEN_DB, color="#fff2cc", alpha=0.7, lw=0)
    a2.text(0.025, 8, "fail (below 20 dB)", fontsize=8.5)
    a2.text(0.025, 22, "not shown (margin below 6 dB)", fontsize=8.5)
    a2.set_ylim(0, 110)
    a2.set_xlim(0.02, 1500)
    a2.set_xlabel("frequency, MHz (0.02 to 1500 MHz, TC-SYS-107)")
    a2.set_ylabel("total shielding, min of plane wave and H field, dB")
    a2.set_title("Walls, window film, openings, joints and plugged jack lines: total", fontsize=10)
    a2.grid(alpha=0.3, which="both")
    a2.legend(fontsize=8, loc="upper right", framealpha=0.95)
    names = [r["source"] for r in src_rows if r["option"] == "C1" and r["openings"] == "rev2_worst"]
    y = np.arange(len(names))
    vcol = {"pass": "#548235", "not shown": "#bf9000", "fail": "#c00000"}
    for off, opt in ((-0.2, "C1"), (0.2, "A")):
        rr = {r["source"]: r for r in src_rows if r["option"] == opt and r["openings"] == "rev2_worst"}
        vals = [rr[n]["min_se_db"] for n in names]
        a3.barh(y + off, vals, 0.38, color=[vcol[rr[n]["verdict"]] for n in names],
                edgecolor="k" if opt == "A" else "none", hatch="//" if opt == "A" else None)
        for yi, v, n in zip(y, vals, names):
            a3.text(v + 0.6, yi + off, f"{opt} {v:.1f} ({rr[n]['verdict']})", va="center", fontsize=6.8)
    a3.axvline(SE_REQ, color="k", ls="--", lw=1)
    a3.axvline(SE_REQ + U_OPEN_DB, color="#bf9000", ls=":", lw=1)
    a3.set_yticks(y)
    a3.set_yticklabels([n[:38] for n in names], fontsize=7.5)
    a3.invert_yaxis()
    a3.set_xlim(0, 48)
    a3.set_xlabel("lowest total over the fundamental and every harmonic to 1.5 GHz, dB")
    a3.set_title("Per source, rules O1 to O4, worse of empty and plugged ports\n(plain: C1; hatched: A); "
                 "green pass, amber not shown, red fail", fontsize=10)
    a3.grid(axis="x", alpha=0.3)
    fig.text(0.01, 0.01, "Developer evidence (author estimate, Schelkunoff slab and slot-aperture models); "
             "docs/design/analysis/shielding-estimate.md revision 2. Sources: clock-plan.md revision 2 sections 2, 2.1.",
             fontsize=8)
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    PNG.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(PNG, dpi=115)


def write(rows, bond_rows):
    OUT.mkdir(parents=True, exist_ok=True)
    for name, data in (("shielding.csv", rows), ("bond.csv", bond_rows)):
        with (OUT / name).open("w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(data[0].keys()))
            w.writeheader()
            w.writerows(data)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    rows, verdict, bond_rows, bond_ok, src_rows, cache = evaluate()
    write(rows, bond_rows)
    with (OUT / "shielding-sources.csv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(src_rows[0].keys()))
        w.writeheader()
        w.writerows(src_rows)
    plot(cache, src_rows)
    for r in src_rows:
        print("SOURCE", r)
    for r in rows:
        print(r)
    for r in bond_rows:
        print(r)
    print("verdicts (12-600 MHz rules applied, <10 MHz H field, 12-600 MHz open window, 12-600 MHz screw joints,"
          " 750-1500 MHz >= 20 dB):", verdict)
    errs = [f"{k}: got {verdict[k]}, expected {v}" for k, v in EXPECTED.items() if verdict[k] != v]
    errs += [f"bond {k}: got {bond_ok[k]}, expected {v}" for k, v in EXPECTED_BOND.items() if bond_ok[k] != v]
    for opt, (all_pass_rev0, fail_rev1, ns_rev1) in EXPECTED_REV1.items():
        r0 = [r for r in src_rows if r["option"] == opt and r["openings"] == "rev0"]
        r1 = [r for r in src_rows if r["option"] == opt and r["openings"] == "rev1"]
        got0 = all(r["verdict"] == "pass" for r in r0)
        got_f = {r["source"] for r in r1 if r["verdict"] == "fail"}
        got_n = {r["source"] for r in r1 if r["verdict"] == "not shown"}
        print(f"REV1 {opt}: rev0 all pass {got0}; rev1 fail {sorted(got_f)}; rev1 not shown {sorted(got_n)}")
        if got0 != all_pass_rev0:
            errs.append(f"{opt} rev0 all-pass: got {got0}, expected {all_pass_rev0}")
        if fail_rev1 is not None and got_f != fail_rev1:
            errs.append(f"{opt} rev1 fail set: got {sorted(got_f)}, expected {sorted(fail_rev1)}")
        if ns_rev1 is not None and got_n != ns_rev1:
            errs.append(f"{opt} rev1 not-shown set: got {sorted(got_n)}, expected {sorted(ns_rev1)}")
    for opt, (fail2, ns2, fail1p) in EXPECTED_REV2.items():
        rw = [r for r in src_rows if r["option"] == opt and r["openings"] == "rev2_worst"]
        r1p = [r for r in src_rows if r["option"] == opt and r["openings"] == "rev1_plug"]
        got_f = {r["source"] for r in rw if r["verdict"] == "fail"}
        got_n = {r["source"] for r in rw if r["verdict"] == "not shown"}
        got_1p = {r["source"] for r in r1p if r["verdict"] == "fail"}
        got_1p_pass = [r["source"] for r in r1p if r["verdict"] == "pass"]
        se_c = cache[(opt, "rev2_worst")][0]
        scope_min = round(float(se_c[GRID_MHZ >= SCOPE_MHZ].min()), 1)
        top_fail = max([float(r["fail_span_mhz"].split(" to ")[1]) for r in rw if r["fail_span_mhz"]] or [0.0])
        print(f"REV2 {opt}: worst fail {sorted(got_f)}; worst not shown {sorted(got_n)}; rev1_plug fail "
              f"{len(got_1p)}; lowest from {SCOPE_MHZ:g} MHz {scope_min} dB; highest failing harmonic {top_fail} MHz")
        if got_f != fail2:
            errs.append(f"{opt} rev2 fail set: got {sorted(got_f)}, expected {sorted(fail2)}")
        if got_n != ns2:
            errs.append(f"{opt} rev2 not-shown set: got {sorted(got_n)}, expected {sorted(ns2)}")
        if got_1p != fail1p or got_1p_pass:
            errs.append(f"{opt} rev1_plug: fail {sorted(got_1p)}, pass {got_1p_pass}")
        if abs(scope_min - EXPECTED_SCOPE[opt]) > 0.05 or not SE_REQ <= scope_min < SE_REQ + U_OPEN_DB:
            errs.append(f"{opt} lowest from {SCOPE_MHZ} MHz: got {scope_min}, expected {EXPECTED_SCOPE[opt]}")
        if top_fail >= SCOPE_MHZ:
            errs.append(f"{opt} rev2 fails at {top_fail} MHz, at or above {SCOPE_MHZ} MHz")
    if args.check:
        for e in errs:
            print("MISMATCH:", e)
        print("CHECK", "FAIL" if errs else "PASS")
        return 1 if errs else 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
