#!/usr/bin/env python3
"""Clock plan harmonic checker: every clock of the cwht plan against the 2 m band, the CW-only
segment, the IF window, the image band and the LO band, for each candidate IF plan.

Product: docs/design/analysis/clock-plan.md and ADR-031 (WP-PDR-20, PDR work plan section 3.6).
Run from the repository root:

    .venv/bin/python hardware/sim/freq/clock_plan.py            # check, print tables, exit status
    .venv/bin/python hardware/sim/freq/clock_plan.py --plot     # also render the figure

Exit status 0 when every rule of ADR-031 (section "RULES") holds for the proposed plan, 1 otherwise.
Arithmetic is exact (fractions.Fraction); a clock line is the interval n*f*(1 +/- tol).

Tool status (05 section 9.1): class B evidence-generating script without a TV record; its output is
developer evidence (peer-review-checklist-analysis CK-ANA-C2). Standard library only for the
numbers; matplotlib renders the figure.
"""
from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path

MHz = F(10**6)
kHz = F(10**3)
PPM = F(1, 10**6)

# Bands (source next to each)
RF = (144 * MHz, 148 * MHz)                         # 47 CFR 97.301(a)
CW_SEG = (F("144.010") * MHz, F("144.100") * MHz)   # 47 CFR 97.305(a), (c): 144.0-144.1 CW only; lower bound REQ-SYS-034
SYS034 = (F("144.010") * MHz, F("147.999") * MHz)   # REQ-SYS-034 (TBR) receive range
XOSC_LINE_EXCL = (F("144.000") * MHz - F("9.4") * kHz, F("144.000") * MHz + F("9.4") * kHz)  # REQ-SYS-034 rationale
IF_HALF = 5 * kHz                                   # ALLOCATION: IF window +/-5 kHz (REQ-SYS-025 -60 dB BW 2.5 kHz, doubled)
SIDETONE = F(600)                                   # ADR-026 / keyer research C13: default sidetone 600 Hz = BFO offset
XOSC_PPM = F(65)                                    # RP2350 datasheet Table 596: 30 + 30 + 5 ppm
TCXO_PPM = F("2.5")                                 # REQ-SYS-010 ceiling

# IF plans (TS-001 section 3.3: IF 9.000, 9.0106 or 10.7 MHz; low- or high-side LO)
IF_PLANS = [("9.000", "low"), ("9.000", "high"), ("9.0106", "low"), ("9.0106", "high"), ("10.7", "low"), ("10.7", "high")]


@dataclass
class Clock:
    name: str
    f: F               # nominal Hz (for a range, the lower end)
    f_hi: F            # upper end (== f for a fixed clock)
    tol_ppm: F
    cls: str           # "clear" (>= 4 MHz, must have no in-band line) or "dense" (< 4 MHz)
    status: str        # fixed / proposed / option / rejected / tx-only / by-design
    source: str
    coherent: bool = False   # derived from XOSC so that 144 MHz / f is an integer (line exactly on 144.000 MHz)


def lines_in(clk: Clock, band, nmax=None):
    """Harmonic numbers n whose line interval [n f_lo (1-tol), n f_hi (1+tol)] meets band."""
    lo, hi = band
    out = []
    n = 1
    top = hi / (clk.f * (1 - clk.tol_ppm * PPM))
    while n <= top and (nmax is None or n <= nmax):
        a = n * clk.f * (1 - clk.tol_ppm * PPM)
        b = n * clk.f_hi * (1 + clk.tol_ppm * PPM)
        if b >= lo and a <= hi:
            out.append((n, a, b))
        n += 1
    return out


def plan_bands(if_mhz: str, side: str):
    IF = F(if_mhz) * MHz
    if side == "low":
        lo_band = (RF[0] - IF, RF[1] - IF)
        img = (RF[0] - 2 * IF, RF[1] - 2 * IF)
    else:
        lo_band = (RF[0] + IF, RF[1] + IF)
        img = (RF[0] + 2 * IF, RF[1] + 2 * IF)
    return IF, lo_band, img, (IF - IF_HALF, IF + IF_HALF)


def clocks_base():
    """The plan: every clock with its status and source."""
    c = []
    c.append(Clock("XOSC 12 MHz (Pico 2 crystal, clk_ref)", 12 * MHz, 12 * MHz, XOSC_PPM, "clear", "fixed", "Pico 2 ABM8-272-T3; RP2350 Table 596", True))
    c.append(Clock("clk_usb / clk_adc 48 MHz (PLL_USB)", 48 * MHz, 48 * MHz, XOSC_PPM, "clear", "fixed", "RP2350 8.1 Table 537: clk_adc must be 48 MHz", True))
    c.append(Clock("clk_sys = clk_peri 150 MHz (PLL_SYS)", 150 * MHz, 150 * MHz, XOSC_PPM, "clear", "fixed", "07 WP-SW-11 (150 MHz)"))
    c.append(Clock("TCXO 25.000 MHz", 25 * MHz, 25 * MHz, TCXO_PPM, "clear", "proposed", "TS-007 R-M4, this plan"))
    c.append(Clock("TCXO 26.000 MHz (alternative)", 26 * MHz, 26 * MHz, TCXO_PPM, "clear", "rejected", "F21 Abracon ATX-13 frequency"))
    c.append(Clock("TCXO 27.000 MHz (alternative)", 27 * MHz, 27 * MHz, TCXO_PPM, "clear", "rejected", "F16 Si5351 25 or 27 MHz"))
    c.append(Clock("Prescaler output /8 (TX only)", F("144.0012") * MHz / 8, F("147.9988") * MHz / 8, TCXO_PPM, "clear", "tx-only", "REQ-TX-013 proposal"))
    # SPI serial clocks from clk_peri 150 MHz: SCK = 150 MHz / d, d even (CPSDVSR even x (1+SCR))
    for d in (6, 8, 10, 12, 16, 24, 26, 30):
        st = "proposed" if d == 8 else ("rejected" if d >= 26 else "allowed")
        c.append(Clock(f"SPI SCK 150/{d} = {float(150/F(d)):.4g} MHz", 150 * MHz / d, 150 * MHz / d, XOSC_PPM, "clear", st, "RP2350 12.3 SSPCPSR/SCR; clear-set rule"))
    # Dense-class clocks (< 4 MHz): lines unavoidable; placement rule is coherence with 144.000 MHz
    c.append(Clock("I2C SCL 400 kHz (150 MHz / 375)", 400 * kHz, 400 * kHz, XOSC_PPM, "dense", "proposed", "RP2350 12.2 IC_FS_SCL_HCNT+LCNT = 375", True))
    c.append(Clock("Audio and sidetone PWM 150 kHz (TOP+1 = 1000)", 150 * kHz, 150 * kHz, XOSC_PPM, "dense", "proposed", "RP2350 12.5; audio research F1 (TOP 1023 = 146.48 kHz)", True))
    c.append(Clock("Audio PWM 146.484 kHz (TOP+1 = 1024)", 150 * MHz / 1024, 150 * MHz / 1024, XOSC_PPM, "dense", "rejected", "audio research F1"))
    c.append(Clock("5 V buck sync 2.4 MHz (12 MHz / 5)", F("2.4") * MHz, F("2.4") * MHz, XOSC_PPM, "dense", "proposed", "HZ-008 K6 buck synchronised; WP-PDR-24 part", True))
    c.append(Clock("5 V buck free-running 2.2 MHz (+/-10 %)", F("1.98") * MHz, F("2.42") * MHz, F(0), "dense", "rejected", "power research F19 (2.2 MHz)"))
    c.append(Clock("Charger boost 1.5 MHz (free-running, +/-10 %)", F("1.35") * MHz, F("1.65") * MHz, F(0), "dense", "off-in-op", "power research F20 (1.5 MHz); off while the radio is on (REQ-SYS-093, HZ-011 K2)"))
    c.append(Clock("PCM1808 SCKI 12.288 MHz (option B, 256 fs at 48 kS/s)", F("12.288") * MHz, F("12.288") * MHz, F(50), "clear", "rejected", "TS-001 option B; cw-selectivity F12"))
    c.append(Clock("PCM1808 SCKI 12.5 MHz (option B, 150 MHz / 12)", F("12.5") * MHz, F("12.5") * MHz, XOSC_PPM, "clear", "option", "this plan (fs = 48.83 kS/s)"))
    return c


def bfo_clock(if_mhz: str) -> Clock:
    IF = F(if_mhz) * MHz
    return Clock(f"BFO {if_mhz} MHz +/- 1 kHz (Si5351A)", IF - kHz, IF + kHz, TCXO_PPM, "clear", "by-design", "TS-001 option A product detector")


def lo_clock(if_mhz: str, side: str) -> Clock:
    IF = F(if_mhz) * MHz
    if side == "low":
        return Clock("RX LO (low side)", RF[0] - IF, RF[1] - IF, TCXO_PPM, "clear", "by-design", "TS-001 F-A")
    return Clock("RX LO (high side)", RF[0] + IF, RF[1] + IF, TCXO_PPM, "clear", "by-design", "TS-001 F-A")


def fmt_lines(ls):
    return "; ".join(f"n={n}: {float(a/MHz):.4f}-{float(b/MHz):.4f}" for n, a, b in ls) if ls else "none"


def evaluate(verbose=True):
    """Return (failures, findings table rows)."""
    fails = []
    rows = []
    clocks = clocks_base()
    # Rule R1: every proposed/fixed clear-class clock has no line in the REQ-SYS-034 range except a
    # coherent line inside the 144.000 MHz exclusion.
    for c in clocks:
        rf = lines_in(c, RF)
        in034 = [l for l in lines_in(c, SYS034)]
        cw = lines_in(c, CW_SEG)
        rows.append((c, rf, in034, cw))
        active = c.status in ("fixed", "proposed", "allowed")
        if c.cls == "clear" and active:
            bad = [l for l in in034 if not (c.coherent and l[1] >= XOSC_LINE_EXCL[0] and l[2] <= XOSC_LINE_EXCL[1])]
            if bad:
                fails.append(f"RULE-1 {c.name}: line in REQ-SYS-034 range: {fmt_lines(bad)}")
            coh_bad = [l for l in rf if c.coherent and not (l[1] >= XOSC_LINE_EXCL[0] and l[2] <= XOSC_LINE_EXCL[1])]
            if coh_bad:
                fails.append(f"RULE-1b {c.name}: coherent line outside the exclusion: {fmt_lines(coh_bad)}")
        # Rule R2: no line of any proposed or fixed clock in the CW-only segment 144.010-144.100 MHz,
        # except the unsynchronisable charger (tracked as a level item, RSK-040)
        if active and cw:
            fails.append(f"RULE-2 {c.name}: line in the CW-only segment: {fmt_lines(cw)}")
        # Rule R3: dense proposed clocks are XOSC-coherent (144 MHz / f integer)
        if c.cls == "dense" and c.status == "proposed":
            q = RF[0] / c.f
            if q.denominator != 1 or not c.coherent:
                fails.append(f"RULE-3 {c.name}: not coherent with 144.000 MHz (144 MHz / f = {float(q):.4f})")
    return fails, rows, clocks


def plan_matrix(clocks):
    """Per IF plan: hits of the BFO, LO and every active clock in the IF window, image band and LO band."""
    out = []
    for if_mhz, side in IF_PLANS:
        IF, lo_band, img, ifw = plan_bands(if_mhz, side)
        bfo = bfo_clock(if_mhz)
        lo = lo_clock(if_mhz, side)
        hits = {"BFO in RF": lines_in(bfo, RF), "BFO in CW seg": lines_in(bfo, CW_SEG)}
        extra = {"IF window": [], "image band": [], "LO band": []}
        for c in clocks + [lo]:
            if c.status not in ("fixed", "proposed", "allowed", "by-design", "tx-only"):
                continue
            if c.name.startswith("RX LO"):
                continue
            for key, band in (("IF window", ifw), ("image band", img), ("LO band", lo_band)):
                ls = lines_in(c, band)
                if ls and c.cls == "dense":
                    extra[key].append(f"{c.name} [dense, coherent] {len(ls)} line(s)")
                elif ls:
                    extra[key].append(f"{c.name} {fmt_lines(ls)}")
        # Si5351A output ceiling for the RX LO (F16: 200 MHz; high side needs divider 4, VCO 600-900 MHz)
        vco6 = (lo.f * 6, lo.f_hi * 6)
        vco4 = (lo.f * 4, lo.f_hi * 4)
        si_ok6 = vco6[0] >= 600 * MHz and vco6[1] <= 900 * MHz
        si_ok4 = vco4[0] >= 600 * MHz and vco4[1] <= 900 * MHz
        out.append((if_mhz, side, hits, extra, img, lo_band, si_ok6, si_ok4))
    return out


def report():
    fails, rows, clocks = evaluate()
    print("TABLE clocks: name | class | status | lines in 144-148 MHz | lines in CW-only segment 144.010-144.100")
    for c, rf, in034, cw in rows:
        print(f"  {c.name} | {c.cls} | {c.status} | {('coherent ' if c.coherent else '')}{len(rf)} line(s): {fmt_lines(rf) if len(rf) <= 3 else fmt_lines(rf[:2]) + ' ... ' + fmt_lines(rf[-1:])} | {fmt_lines(cw)}")
    print("\nTABLE SPI clear set from 150 MHz (even divisor d): d -> SCK MHz, in-band lines")
    clear = []
    for d in range(2, 64, 2):
        ck = Clock("x", 150 * MHz / d, 150 * MHz / d, XOSC_PPM, "clear", "x", "")
        n = lines_in(ck, RF)
        if not n:
            clear.append(d)
        print(f"  d={d}: {float(150/F(d)):.4f} MHz: {fmt_lines(n)}")
    print("  clear divisors:", clear)
    print("\nTABLE IF plans (BFO +/-1 kHz, LO, image, IF window):")
    for if_mhz, side, hits, extra, img, lo_band, s6, s4 in plan_matrix(clocks):
        print(f"  IF {if_mhz} {side}-side: image {float(img[0]/MHz):.3f}-{float(img[1]/MHz):.3f}, LO {float(lo_band[0]/MHz):.3f}-{float(lo_band[1]/MHz):.3f} MHz; "
              f"Si5351A LO with /6 in VCO range: {s6}, with /4: {s4}")
        print(f"    BFO harmonics in 144-148: {fmt_lines(hits['BFO in RF'])}; in CW-only segment: {fmt_lines(hits['BFO in CW seg'])}")
        for k, v in extra.items():
            print(f"    {k}: {'; '.join(v) if v else 'none'}")
    print()
    for f_ in fails:
        print("FAIL", f_)
    print(f"RESULT: {len(fails)} rule failure(s) in the proposed plan")
    return 1 if fails else 0


def plot(out: Path):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    clocks = [c for c in clocks_base() if c.status in ("fixed", "proposed", "tx-only", "rejected", "off-in-op")]
    extra = [bfo_clock("9.0106"), bfo_clock("9.000"), bfo_clock("10.7")]
    allc = clocks + extra
    fig, ax = plt.subplots(figsize=(12, 7))
    lo, hi = 124 * MHz, 170 * MHz
    ax.axvspan(144, 148, color="tab:blue", alpha=0.10, label="2 m band 144-148 MHz")
    ax.axvspan(144.010, 144.100, color="tab:green", alpha=0.35, label="CW-only segment 144.010-144.100")
    ax.axvspan(126.0, 130.0, color="tab:orange", alpha=0.12, label="image, IF 9 MHz low side")
    ax.axvspan(135.0, 139.0, color="tab:purple", alpha=0.10, label="LO, IF 9 MHz low side")
    for i, c in enumerate(allc):
        ls = lines_in(c, (lo, hi))
        colour = {"fixed": "k", "proposed": "tab:green", "tx-only": "tab:gray", "rejected": "tab:red", "by-design": "tab:brown", "off-in-op": "tab:olive"}[c.status]
        for n, a, b in ls[:400]:
            if (b - a) < F("0.05") * MHz:
                ax.plot([float((a + b) / 2 / MHz)], [i], marker="|", markersize=14 if c.cls == "clear" else 5,
                        mew=2.2 if c.cls == "clear" else 0.8, color=colour, linestyle="none")
            else:
                ax.plot([float(a / MHz), float(b / MHz)], [i, i], color=colour, lw=5, solid_capstyle="butt")
            if c.cls == "clear" and len(ls) < 12:
                ax.text(float((a + b) / 2 / MHz), i + 0.3, f"{n}", fontsize=6, ha="center")
    ax.set_yticks(range(len(allc)))
    ax.set_yticklabels([f"{c.name} [{c.status}]" for c in allc], fontsize=7)
    ax.set_xlim(float(lo / MHz), float(hi / MHz))
    ax.set_xlabel("frequency (MHz); marks are harmonic lines n*f with tolerance; number = harmonic order")
    ax.set_title("cwht clock plan: harmonic lines against the 2 m band, image and LO bands (developer evidence)\n"
                 "colour = status: black fixed, green proposed, red rejected, grey TX only, brown BFO by design, olive off in operation", fontsize=9)
    ax.grid(alpha=0.3, axis="x")
    ax.legend(fontsize=7, loc="lower right")
    fig.tight_layout()
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out, dpi=130)
    print(f"figure: {out}")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--plot", action="store_true", help="render docs/reviews/PDR/figures/clock-plan-harmonics.png")
    a = ap.parse_args(argv)
    rc = report()
    if a.plot:
        plot(Path("docs/reviews/PDR/figures/clock-plan-harmonics.png"))
    return rc


if __name__ == "__main__":
    sys.exit(main())
