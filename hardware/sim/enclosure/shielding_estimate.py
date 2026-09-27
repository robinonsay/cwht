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
Verdict bands: 12 to 600 MHz (min of plane wave and H field), 1.5 and 2.2 MHz (H field), and the
1 GHz edge reported as marginal when within 3 dB of 20 dB.
Bond: two circular contacts of radius a1, a2 at distance d on a sheet Rs:
    R = Rs / (2 pi) * (ln(d/a1) + ln(d/a2)) + contact resistance.

Output is developer evidence (numpy and matplotlib have no TV record of their own).
Run:  .venv/bin/python hardware/sim/enclosure/shielding_estimate.py [--check]
Writes hardware/sim/enclosure/out/shielding.csv, out/bond.csv and
docs/reviews/PDR/figures/shielding-estimate.png. --check exits 1 if a verdict differs from
EXPECTED (the verdicts stated in the analysis note).
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
    1000.0: "upper edge of the evaluated range (author choice)",
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

EXPECTED = {
    # option: (12 to 600 MHz, design rules applied: min(plane wave, H field) total >= 20 dB,
    #          1.5 and 2.2 MHz: H-field total >= 20 dB,
    #          12 to 600 MHz with the display window open (no film): plane-wave total >= 20 dB,
    #          12 to 600 MHz with screw-only joints every 15 mm: plane-wave total >= 20 dB,
    #          1 GHz: total within 3 dB of 20 dB (marginal, set by the openings common to all options))
    "A": (True, True, False, False, True),
    "B": (True, True, False, False, True),
    "C1": (True, False, False, False, True),
    "D": (True, False, False, False, True),
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


def total_se(f_hz: float, opt: str, zw: complex, film: bool = True, seam: float = SEAM_SPACING) -> float:
    """Power (random-phase) sum of the wall and every leak: sqrt(T_wall^2 + sum T_i^2)."""
    sig, t = OPTIONS[opt]["wall"]
    depth = WALL_DEPTH[opt]
    terms = [10 ** (-slab_se(f_hz, sig, t, zw) / 20)]
    terms += [aperture_t(f_hz, length, depth) for length in APERTURES_COMMON]
    t_win = aperture_t(f_hz, WINDOW, depth)
    if film:
        fs, ft = (1.0 / (WINDOW_FILM_RS * 1e-6), 1e-6)
        t_win *= 10 ** (-slab_se(f_hz, fs, ft, zw) / 20)
    terms.append(t_win)
    n_seam = int(round(SEAM_LENGTH[opt] / seam))
    terms += [aperture_t(f_hz, seam, SEAM_OVERLAP)] * n_seam
    t_tot = min(1.0, math.sqrt(sum(x * x for x in terms)))
    return -20 * math.log10(t_tot)


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
            if f_mhz >= 1000.0:
                edge = min(se_pw_tot, se_h_tot)
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
        verdict[opt] = (hi_ok, lo_ok, open_ok, screws_ok, abs(edge - SE_REQ) <= 3.0)
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
    return rows, verdict, bond_rows, bond_ok


def plot():
    f = np.logspace(math.log10(1e6), math.log10(1.5e9), 300)
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(14, 6.0))
    for label, rs in COATINGS.items():
        sig, t = coating(rs)
        a1.semilogx(f / 1e6, [slab_se(x, sig, t, zw_h(x, R_SRC)) for x in f], lw=1.8, label=f"H, {label}")
    a1.semilogx(f / 1e6, [slab_se(x, *AL6061, zw_h(x, R_SRC)) for x in f], "k", lw=2.2, label="H, 6061 1.5 mm (off scale, >140 dB)")
    sig, t = coating(0.03)
    a1.semilogx(f / 1e6, [slab_se(x, sig, t, complex(Z0, 0)) for x in f], "--", color="#c0504d", lw=1.8,
                label="plane wave, 0.03 ohm/sq")
    a1.axhline(SE_REQ, color="grey", ls=":", lw=1.2)
    a1.text(1.05, SE_REQ + 2, "REQ-SYS-177: 20 dB (TBR)", fontsize=9)
    a1.set_ylim(0, 160)
    a1.set_xlabel("frequency, MHz")
    a1.set_ylabel("wall shielding effectiveness, dB")
    a1.set_title(f"Wall only (no apertures), source {R_SRC * 1000:.0f} mm from the wall")
    a1.grid(alpha=0.3, which="both")
    a1.legend(fontsize=7.5, loc="upper left", ncol=1, framealpha=0.95)
    colors = {"A": "#1f4e79", "B": "#6b8e23", "C1": "#c0504d", "D": "#4bacc6"}
    widths = {"A": 2.0, "B": 2.0, "C1": 4.0, "D": 1.5}
    for opt in OPTIONS:
        a2.semilogx(f / 1e6, [total_se(x, opt, complex(Z0, 0)) for x in f], color=colors[opt], lw=widths[opt],
                    label=OPTIONS[opt]["label"])
        a2.semilogx(f / 1e6, [total_se(x, opt, zw_h(x, R_SRC)) for x in f], color=colors[opt],
                    lw=widths[opt] * 0.7, ls="--")
    a2.annotate("C1 and D, H field: 9.5 dB at 1.5 MHz,\n11.8 dB at 2.2 MHz (below 20 dB)", xy=(1.6, 10),
                xytext=(3.2, 2.5), fontsize=8, arrowprops=dict(arrowstyle="->", lw=0.8))
    a2.semilogx(f / 1e6, [total_se(x, "C1", complex(Z0, 0), film=False) for x in f], color="k", lw=1.2, ls=":",
                label="C1, window without film")
    a2.semilogx(f / 1e6, [total_se(x, "C1", complex(Z0, 0), seam=SEAM_SPACING_SCREWS) for x in f], color="grey",
                lw=1.2, ls="-.", label="C1, screw joints at 15 mm, no gasket")
    for fm in SOURCES:
        a2.axvline(fm, color="grey", lw=0.5, alpha=0.5)
    a2.axhline(SE_REQ, color="grey", ls=":", lw=1.2)
    a2.set_ylim(0, 110)
    a2.set_xlabel("frequency, MHz (grey lines: source frequencies)")
    a2.set_ylabel("total shielding effectiveness, dB")
    a2.set_title("Walls + window (ITO film), openings, gasketed joints\n(solid: plane wave; dashed: H field)",
                 fontsize=10)
    a2.grid(alpha=0.3, which="both")
    a2.legend(fontsize=7.5, loc="upper right", ncol=1, framealpha=0.95, title="solid: plane wave; dashed: H field",
               title_fontsize=7.5)
    fig.text(0.01, 0.01, "Developer evidence (author estimate, Schelkunoff slab and slot-aperture models); "
             "docs/design/analysis/shielding-estimate.md.", fontsize=8)
    fig.tight_layout(rect=(0, 0.035, 1, 1))
    PNG.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(PNG, dpi=130)


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
    rows, verdict, bond_rows, bond_ok = evaluate()
    write(rows, bond_rows)
    plot()
    for r in rows:
        print(r)
    for r in bond_rows:
        print(r)
    print("verdicts (12-600 MHz rules applied, <10 MHz H field, 12-600 MHz open window, 12-600 MHz screw joints,"
          " 1 GHz marginal):", verdict)
    errs = [f"{k}: got {verdict[k]}, expected {v}" for k, v in EXPECTED.items() if verdict[k] != v]
    errs += [f"bond {k}: got {bond_ok[k]}, expected {v}" for k, v in EXPECTED_BOND.items() if bond_ok[k] != v]
    if args.check:
        for e in errs:
            print("MISMATCH:", e)
        print("CHECK", "FAIL" if errs else "PASS")
        return 1 if errs else 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
