#!/usr/bin/env python3
"""TS-012 transmit clock spur plan (WP-PDR-20 pre-order item added by TS-012 revision 4, adversarial R-3).

Product: docs/design/analysis/spurs-ts012.md. Block README: hardware/sim/freq/README.md.

Question: which clock lines from 118 to 175 MHz exist while the radio transmits, how strong is each at
the GVA-84+ input and at the antenna after the chain gain and the harmonic low-pass filter, and which
clock, firmware or layout choice moves or holds each one under the budget?

Budget (TS-012 section 7.3): 25 uW at the SMA is -16 dBm (47 CFR 97.307(e), REQ-SYS-017); the 60 dBc
target at 5 W is -23 dBm (REQ-SYS-018, TBR). With about 45 dB from the GVA-84+ input to the SMA the
limits referred to the GVA-84+ input are about -61 dBm and -68 dBm.

Method (every level here is an ESTIMATE, Low confidence, unless marked otherwise):
  * Line inventory per plan: B0 (TS-012 revision 4 as written: clk_sys 125 MHz in transmit, clk_adc
    continuous from PLL_USB, QSPI clk_sys/4, /8 prescaler on a 100 pF tap, Si5351 CLK0 and CLK2
    powered down with PLL B left running), B1 (the ADR-031 values: clk_sys 150 MHz, otherwise as B0) and
    P (proposed here). Each line has a source level range and a coupling range; the result is a
    [low, high] range.
  * Three injection points:
      pre  a level on the Si5351 CLK1 net, stated in dBc of the CLK1 carrier; it passes the drive
           low-pass and pad with the carrier, so at the SMA it keeps its dBc, corrected by the drive
           and harmonic filter response at the line against the carrier (the ALC holds 5 W);
      gva  an absolute level coupled in at the GVA-84+ input; at the SMA it is P + G_eff, with
           G_eff = 37 dBm - P_carrier(GVA input), because the ALC sets the total gain;
      rel  a carrier-relative sideband (AM from supply or VGG ripple, Si5351 PLL spurs), in dBc at the
           PA output.
  * Filters: drive low-pass (3-pole Butterworth, 170 MHz, with the 18 dB pad) and harmonic low-pass
    (7-pole 0.1 dB Chebyshev, 165 MHz) from the LTspice run of tx_spur_filters.cir (ideal and Q = 60
    variants; the Q = 60 variant is used); the analytic prototypes are checked against it.
  * GVA-84+ and PA gain taken flat over 118 to 175 MHz (no credit for the module's 135 to 175 MHz
    band edge), as TS-012 does.
  * A saturated final stage is taken to add a mirror line at 2 fc - fs, 6 dB under the line (ESTIMATE).
  * Coincident lines (the 144.000 MHz line) add in amplitude (worst phase) for the high end.
  * Board coupling from the microstrip crosstalk rule Kc = 1 / (1 + (D/H)^2) (Howard Johnson, High-Speed
    Digital Design, rule of thumb) times the electrical length 2 pi l / lambda_eff for short runs.

Verdict per line: pass if the high estimate is at or under the limit; "not shown" if the range spans it;
fail if even the low estimate exceeds it. TS-012 pass criterion: every line at most -68 dBm at the
GVA-84+ input (estimate), or a layout, clock or firmware change named for it.

Revision 1 (2026-09-28, independent review of revision 0, Major finding-1 and finding-2):
  * Each named change is either CREDITED (its effect is in the numbers of plans P and PB) or NAMED only (effect not
    quantified). A line whose high estimate stays over the 60 dBc target after the credited changes is a RESIDUAL
    line. The TS-012 criterion is reported twice: in the numbers (PASS only with no residual line) and by its
    wording ("met by wording only: N residual lines ..."), never as a bare PASS when residual lines remain.
  * C7 (/8 prescaler tap): the valid 74LVC1G80 clock is checked in LTspice (tx_spur_c7_tap.cir, against Nexperia
    Rev. 17 VIH, VIL, tW and the input transition rate) and the kickback isolation is read from LTspice
    (tx_spur_c7_iso.cir) instead of the revision 0 divider db20((330 + 25) / 25).
  * T1 (150 MHz trap) is sized with its carrier cost in LTspice (tx_spur_trap.cir).

Run from the repository root (LTspice only through the wrapper, ACC-LTSPICE-001):
    for d in tx_spur_filters tx_spur_bpf_tol tx_spur_c7_tap tx_spur_c7_iso tx_spur_trap; do
        tools/ltspice-batch.sh -t 900 -o hardware/sim/freq/results/<run-id> -b hardware/sim/freq/$d.cir; done
    .venv/bin/python hardware/sim/freq/tx_spur_plan.py --run-id <run-id>
Writes results.json, lines.csv and the PNG figures in the run directory.
Exit status: 0 if plans P and PB meet 60 dBc and 25 uW in the numbers for both finalists; 1 if residual lines
remain (TS-012 7.3 met by wording only) or the filter cross-check fails; 2 if an input is missing or the C7
design value is not a valid clock; 3 if a residual line has no change named at all.

Tool status: class B evidence-generating script without a TV record (developer evidence). numpy,
matplotlib and spicelib from the project venv.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
import sys
from dataclasses import dataclass, field, asdict
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from spicelib import RawRead  # noqa: E402

ROOT = Path(__file__).resolve().parents[3]
BLOCK = ROOT / "hardware/sim/freq"

# ---------------------------------------------------------------- budget and chain (TS-012 section 7.3)
P_CARRIER_ANT = 37.0          # dBm, 5 W at the SMA (REQ-SYS-012 step; TS-012 7.3)
LIM_LEGAL_ANT = -16.0         # dBm, 25 uW (47 CFR 97.307(e); REQ-SYS-017)
LIM_TARGET_ANT = P_CARRIER_ANT - 60.0   # dBm, 60 dBc (REQ-SYS-018, TBR) = -23 dBm
G_REF = 45.0                  # dB, TS-012's GVA-input-to-SMA figure; used only to refer levels to the GVA input
LIM_LEGAL_GVA = LIM_LEGAL_ANT - G_REF    # -61 dBm
LIM_TARGET_GVA = LIM_TARGET_ANT - G_REF  # -68 dBm
WINDOW = (118.0, 175.0)       # MHz, TS-012 7.3 (both LPF passbands with margin)
CARRIERS = (144.050, 146.000, 147.950)   # MHz; 144.05 and 147.95 are the TS-012 bench-check carriers
SWEEP = np.round(np.arange(144.010, 147.9901, 0.02), 3)

# Si5351 CLK1 at the pin, 50 ohm load: +9 to +10.4 dBm (TS-012 7.3), +12.9 dBm with a 25 ohm source.
P_CLK1 = (9.0, 12.9)
# Carrier at the GVA-84+ input: CLK1 + drive LPF + 18 dB pad (A5); A4 runs the GVA-84+ at P1dB (TS-012 7.3,
# "GVA-84+ at its P1dB limit"): +19.4 to +20.4 dBm out, gain 22.5 to 25 dB compressed by about 1 dB (ESTIMATE).
FINALISTS = {
    "A5": dict(label="A5 (RA07M1317M module, TCXO)", reference="TCXO TG2520SMN, clipped sine into XA"),
    "A4": dict(label="A4 (AFT05MS004N, no TCXO)", reference="Adafruit module 25 MHz crystal on the Si5351 XO"),
}
P_CAR_GVA_A4 = (-5.0, -2.0)   # dBm, ESTIMATE from P1dB 19.4 to 20.4 dBm and 21.5 to 24 dB compressed gain

C0 = 299_792_458.0
ER_EFF = 3.3                  # FR4 microstrip effective permittivity (textbook value, Medium)
H_MAIN = 1.6                  # mm, main board and Adafruit module thickness (TS-012 8.1: 1.6 mm main board)


def db20(x: float) -> float:
    return 20.0 * math.log10(max(x, 1e-30))


def dbm_from_vpk(v: float) -> float:
    """Equivalent level of a sinusoid of peak v volts into 50 ohm."""
    return 10.0 * math.log10(max(v, 1e-30) ** 2 / (2.0 * 50.0) / 1e-3)


def crosstalk_loss_db(d_mm: float, h_mm: float, l_mm: float, f_mhz: float) -> float:
    """Coupling loss between two traces over a ground pour: Kc = 1/(1+(D/H)^2) times min(1, 2 pi l/lambda)."""
    kc = 1.0 / (1.0 + (d_mm / h_mm) ** 2)
    lam_mm = C0 / (f_mhz * 1e6 * math.sqrt(ER_EFF)) * 1e3
    lf = min(1.0, 2.0 * math.pi * l_mm / lam_mm)
    return -db20(kc * lf)


# Path classes: (min loss, max loss) in dB at frequency f; geometry ranges are ESTIMATES pending layout (CDR).
def path_loss(kind: str, f: float) -> tuple[float, float]:
    if kind == "module":      # on the Adafruit Si5351 board: net to CLK1 trace, 3 to 8 mm, 10 mm parallel
        return crosstalk_loss_db(3, H_MAIN, 10, f), crosstalk_loss_db(8, H_MAIN, 10, f)
    if kind == "prescaler":   # /8 output trace to the CLK1 / drive-filter net, 5 to 15 mm, 20 to 10 mm parallel
        return crosstalk_loss_db(5, H_MAIN, 20, f), crosstalk_loss_db(15, H_MAIN, 10, f)
    if kind == "prescaler_p":  # proposed: /8 output routed at least 15 to 25 mm from the CLK1 net
        return crosstalk_loss_db(15, H_MAIN, 20, f), crosstalk_loss_db(25, H_MAIN, 10, f)
    if kind == "pico_trace":  # Pico 2 GPIO or QSPI trace to the GVA-84+ input on the RF board (other board, bay)
        return crosstalk_loss_db(20, H_MAIN, 20, f) + 5.0, crosstalk_loss_db(50, H_MAIN, 20, f) + 10.0
    if kind == "pdn":         # Pico 2 ground and supply noise into the drive chain (assumption, no formula)
        return 40.0, 70.0
    if kind == "pdn_p":       # proposed layout rules (section 6 of the note): Pico 2 at least 30 mm from the
        return 50.0, 75.0     # GVA-84+ input, CLK1 in coax or coplanar line, one-point ground (ESTIMATE)
    raise ValueError(kind)


# ---------------------------------------------------------------- source level models (ESTIMATES)
def square_harmonic_vpk(vpp: float, n: int, f0: float, tr_ns: float, duty_err: float) -> float:
    """Peak amplitude of harmonic n of a trapezoid wave (50 % duty +/- duty_err), rise time tr."""
    d = 0.5 + duty_err
    a = 2.0 * vpp / (n * math.pi) * abs(math.sin(n * math.pi * d))
    x = n * f0 * 1e6 * tr_ns * 1e-9
    sinc = 1.0 if x == 0 else abs(math.sin(math.pi * x) / (math.pi * x))
    return a * sinc


def square_line_dbm(vpp, n, f0, tr_range, duty_err_range) -> tuple[float, float]:
    vals = [dbm_from_vpk(square_harmonic_vpk(vpp, n, f0, tr, de)) for tr in tr_range for de in duty_err_range]
    return min(vals), max(vals)


# RP2350 on-die current: VREG_VIN 11.0 to 14.7 mA at 3.3 V (datasheet Table 1446, CoreMark 150 MHz and
# hello_serial) gives about 25 to 35 mA on DVDD at 1.1 V after the regulator (ESTIMATE); scaled with clk_sys.
I_CORE_150 = (0.020, 0.035)   # A at 150 MHz (ESTIMATE, lower end widened)
Z_PDN = (0.1, 0.5)            # ohm, Pico 2 core decoupling at 100 to 200 MHz (ESTIMATE)
I_REF_DOMAIN = (0.001, 0.003)  # A, clk_ref (12 MHz) domain: ticks, timers, watchdog, PLL references (ESTIMATE)
I_ADC_DOMAIN = (0.0003, 0.001)  # A, clk_adc domain (ESTIMATE)
I_PLL_USB = (0.0005, 0.002)   # A, PLL_USB output clock tree when running (ESTIMATE)
CROSS_REL = (-30.0, -20.0)    # dB, on-die cross-domain products against their clk_sys parent (ESTIMATE)


def pdn_dbm(i_range, scale=1.0) -> tuple[float, float]:
    lo = dbm_from_vpk(2.0 * i_range[0] * scale * Z_PDN[0])
    hi = dbm_from_vpk(2.0 * i_range[1] * scale * Z_PDN[1])
    return lo, hi


# ---------------------------------------------------------------- plans
PLANS = {
    "B0": dict(label="B0: TS-012 rev 4 as written", clk_sys=125.0, qspi_div=4, qspi_activity=(0.1, 1.0),
               adc="continuous", pll_usb=True, pll_b="running", prescaler="tap", pwm_coherent=False),
    "B1": dict(label="B1: ADR-031 values (150 MHz)", clk_sys=150.0, qspi_div=4, qspi_activity=(0.1, 1.0),
               adc="continuous", pll_usb=True, pll_b="running", prescaler="tap", pwm_coherent=True),
    "P": dict(label="P: proposed transmit clock plan", clk_sys=96.0, qspi_div=2, qspi_activity=(0.0, 0.0),
              adc="burst", pll_usb=False, pll_b="parked", prescaler="isolated", pwm_coherent=True),
    "PB": dict(label="PB: P plus option C10 (drive bandpass)", clk_sys=96.0, qspi_div=2, qspi_activity=(0.0, 0.0),
               adc="burst", pll_usb=False, pll_b="parked", prescaler="isolated", pwm_coherent=True, drive="bpf"),
}
ADC_BURST_DUTY = (0.005, 0.02)   # proposed: 8 to 16 conversions (16 to 32 us plus start-up) every 1.6 ms (ESTIMATE)
F_XOSC = 12.0
F_REF = 25.0
F_BFO = 8.0                      # TS-012 A5: 8.000 MHz ladder, BFO on CLK2 (IF 8 MHz)
F_VCO_B = 800.0                  # PLL B VCO for an 8 MHz BFO with MS2 = 100 (assumption; any 600 to 900 MHz)
F_PWM = 0.150                    # MHz, audio/sidetone and envelope-reference PWM (ADR-031 rule 3)
F_SW = {"RT6150 (Pico 2, about 2 MHz, Low)": 2.0, "RP2350 core regulator (3 MHz typ)": 3.0}

# Changes named per family (the proposed plans P and PB); the analysis note section 6 lists them with owners.
# Revision 1 (review finding-1 item b): each family separates the changes whose effect is CREDITED in the numbers of
# plans P and PB (the model applies them) from the changes that are only NAMED (effect not quantified, not in the
# numbers). A line whose high estimate stays over a limit after the credited changes is a RESIDUAL line, whatever
# is named for it; the TS-012 7.3 wording "or a change named for it" is reported separately and never as PASS.
# "kind": moves (a clock or firmware choice removes the line from the window) | level | none.
CHANGE = {
    "clk_sys": dict(text="C1: clk_sys = clk_peri = 96 MHz in every state (PLL_SYS FBDIV 120, POSTDIV1 5, POSTDIV2 3); fundamental below 118 MHz, 2nd harmonic 192 MHz",
                    kind="moves", credited=["C1"], named=[]),
    "xosc": dict(text="cannot be moved (Pico 2 crystal); layout rules L1 to L3 (credited in the path loss, 50 to 75 dB)",
                 kind="level", credited=["L1-L3"], named=[]),
    "cross": dict(text="C1 puts every on-die product on the 12 MHz grid (120, 132, 144, 156, 168 MHz); L1 to L3 (credited)",
                  kind="moves", credited=["C1", "L1-L3"], named=[]),
    "adc": dict(text="C2: clk_adc from PLL_SYS / 2 (AUXSRC CLKSRC_PLL_SYS, DIV 2) enabled only for conversion bursts (ENABLE bit); C3: PLL_USB powered down (PWR.PD, VCOPD) outside USB",
                kind="moves", credited=["C2", "C3"], named=[]),
    "qspi": dict(text="C4: QSPI CLKDIV 2 (48 MHz, lines only on 144.000 MHz) and the transmit-path code and data in SRAM so the flash is idle during key-down",
                 kind="moves", credited=["C4"], named=[]),
    "ref": dict(text="cannot be moved (Si5351A reference 25 MHz, clock-plan rule 7); F1 Si5351 VDD filter named, effect not quantified (not credited)",
                kind="level", credited=[], named=["F1"]),
    "tcxo": dict(text="L4: TCXO output lead at most 10 mm and at least 8 mm from the CLK1 trace, named, not credited (path range 3 to 8 mm kept); treats the lead only, not the on-die feedthrough",
                 kind="level", credited=[], named=["L4"]),
    "pfd": dict(text="none (on-die PLL)", kind="none", credited=[], named=[]),
    "frac": dict(text="C5: PLL A multiplier rule, fractional part not within 0.002 of an integer; named, not credited (it sets where a fractional spur falls, not its level)",
                 kind="level", credited=[], named=["C5"]),
    "bfo_xtalk": dict(text="C6: in transmit PLL B is parked on the PLL A multiplier and CLK2 and CLK0 are powered down and disabled (register 3)",
                      kind="moves", credited=["C6"], named=[]),
    "vco_b": dict(text="C6 (as above): VCO B leakage through MS1 then falls on the carrier", kind="moves", credited=["C6"], named=[]),
    "presc_kick": dict(text="C7 (revision 1): {rser:g} ohm in series after the 100 pF tap, sized for a valid 74LVC1G80 clock; LTspice reverse isolation {iso:.1f} dB credited. "
                            "Named, not credited: each 74LVC1G80 on its own bead and 100 nF; C7b buffer gate ahead of the /8 chain; option C9 (/4 prescaler) moves the lines out of the window",
                       kind="level", credited=["C7"], named=["C7 supply beads", "C7b", "C9"]),
    "presc_trace": dict(text="C8: 470 ohm series resistor at the /8 output and the /8 trace 15 to 25 mm from the CLK1 net (L5), credited; option C9 (/4 prescaler) named",
                        kind="level", credited=["C8", "L5"], named=["C9"]),
    "pwm_trace": dict(text="none needed (coherent 150 kHz comb, ADR-031 rule 3)", kind="none", credited=[], named=[]),
    "pwm_vgg": dict(text="none needed; derived requirement to WP-PDR-22: PWM ripple at VGG at most 3.3 mV peak", kind="none", credited=[], named=[]),
    "supply": dict(text="F3: GVA-84+ supply through a ferrite bead and 22 uF (ripple at most 3 mV at 1 to 10 MHz), credited; derived requirement to WP-PDR-22 and WP-PDR-24",
                   kind="level", credited=["F3"], named=[]),
}

# C7 design (revision 1, review finding-2). The series resistor is chosen from the LTspice valid-clock run
# (tx_spur_c7_tap.cir); its reverse isolation is read from tx_spur_c7_iso.cir; both are set in main().
RSER_C7 = 47.0                # ohm, E12: the largest value of the run with at least VCLK_MARGIN at every corner
VIH_LVC, VIL_LVC = 2.0, 0.8   # V, Nexperia 74LVC1G80 Rev. 17 (12 Nov 2024) Table 7, VCC 2.7 to 3.6 V
VM_LVC = 1.5                  # V, Table 9 measurement point, VCC 3.0 to 3.6 V
TW_MIN_LVC = 2.5e-9           # s, Table 8 CP pulse width HIGH or LOW, minimum, -40 to +125 C
DTDV_MAX_LVC = 10e-9          # s/V, Table 6 input transition rise and fall rate, VCC 2.7 to 5.5 V
FMAX_MIN_LVC = 160e6          # Hz, Table 8 fmax minimum, VCC 3.0 to 3.6 V, -40 to +85 C
CI_LVC = 5e-12                # F, Table 7 CI typical (no maximum given)
VCLK_MARGIN = 0.10            # V, required beyond VIH and VIL: the bias spread (VCC 3.3 V +/-3 % est., 1 % resistors,
                              # +/-0.06 V) plus 0.04 V
C7 = dict(rser=RSER_C7, iso_db=0.0)   # filled in main() from the LTspice runs


@dataclass
class Line:
    plan: str
    finalist: str
    carrier: float
    family: str
    source: str
    f: float
    inj: str                 # pre | gva | rel
    lo: float                # dBc (pre, rel) or dBm (gva), low estimate (after coupling)
    hi: float
    basis: str
    change: str = ""
    change_kind: str = ""    # moves (clock or firmware choice removes or moves it) | level (layout or circuit) | none
    credited: list = field(default_factory=list)   # changes whose effect is in the numbers (plans P and PB only)
    named: list = field(default_factory=list)      # changes named but not credited
    mirror: bool = False
    ant_lo: float = 0.0
    ant_hi: float = 0.0
    gva_lo: float = 0.0
    gva_hi: float = 0.0
    verdict_target: str = ""
    verdict_legal: str = ""
    contributors: list = field(default_factory=list)


# ---------------------------------------------------------------- filters (LTspice)
class Filters:
    def __init__(self, raw_path: Path):
        raw = RawRead(str(raw_path))
        f = np.real(raw.get_trace("frequency").get_wave(0))
        self.f_mhz = f / 1e6

        def s21(node):
            return 20 * np.log10(np.abs(raw.get_trace(f"V({node})").get_wave(0)) * 2.0)

        self.drive = s21("outdq")        # includes the 18 dB pad
        self.drive_bpf = s21("outb")     # option C10 bandpass, 18 dB pad, Q 60
        self.drive_ideal = s21("outd")
        self.out = s21("outoq")
        self.out_ideal = s21("outo")

    def hd(self, fmhz, plan="P"):
        tr = self.drive_bpf if PLANS[plan].get("drive") == "bpf" else self.drive
        return float(np.interp(fmhz, self.f_mhz, tr))

    def ho(self, fmhz):
        return float(np.interp(fmhz, self.f_mhz, self.out))


def analytic_butter3(f, fc):
    return -10 * np.log10(1 + (f / fc) ** 6)


def analytic_cheby(f, fc, n=7, ripple=0.1):
    eps2 = 10 ** (ripple / 10) - 1
    x = np.asarray(f, dtype=float) / fc
    t = np.where(np.abs(x) <= 1, np.cos(n * np.arccos(np.clip(x, -1, 1))), np.cosh(n * np.arccosh(np.maximum(x, 1))))
    return -10 * np.log10(1 + eps2 * t ** 2)


# ---------------------------------------------------------------- line inventory
def in_window(f):
    return WINDOW[0] <= f <= WINDOW[1]


def build_lines(plan_id: str, fin: str, fc: float) -> list[Line]:
    p = PLANS[plan_id]
    L: list[Line] = []

    proposed = plan_id in ("P", "PB")

    def add(family, source, f, inj, lo, hi, basis, change_key):
        if in_window(f):
            ch = CHANGE[change_key]
            text, kind = ch["text"].format(rser=C7["rser"], iso=C7["iso_db"]), ch["kind"]
            cred, named = (list(ch["credited"]), list(ch["named"])) if proposed else ([], ch["credited"] + ch["named"])
            if p.get("drive") == "bpf" and inj == "pre":
                text += "; C10: drive bandpass in place of the drive low-pass (credited)"
                kind = "level" if kind == "none" else kind
                cred.append("C10")
            L.append(Line(plan_id, fin, fc, family, source, round(f, 4), inj, lo, hi, basis, text, change_kind=kind,
                          credited=cred, named=named))

    fsys = p["clk_sys"]
    scale = fsys / 150.0
    sys_src = pdn_dbm(I_CORE_150, scale)
    pdn_kind = "pdn_p" if plan_id in ("P", "PB") else "pdn"   # layout rules L1 to L3 in P and PB

    # 1. On-die RP2350 lines |a fsys + b 12| (a = 0: XOSC harmonics; b = 0: clk_sys harmonics; else cross)
    seen = set()
    for a in (0, 1, 2):
        for b in range(-15, 16):
            f = a * fsys + b * F_XOSC
            if f <= 0 or not in_window(f) or (a == 0 and b <= 0):
                continue
            key = round(f, 4)
            if (a, key) in seen:
                continue
            seen.add((a, key))
            if a == 0:
                src = pdn_dbm(I_REF_DOMAIN)
                fam, name, ck = "RP2350 XOSC 12 MHz", f"XOSC 12 MHz x {b}", "xosc"
            elif b == 0:
                src = sys_src
                fam, name, ck = "RP2350 clk_sys", f"clk_sys {fsys:g} MHz x {a}", "clk_sys"
            else:
                src = (sys_src[0] + CROSS_REL[0], sys_src[1] + CROSS_REL[1])
                fam, name, ck = "RP2350 on-die products", f"{a} x {fsys:g} {'+' if b > 0 else '-'} {abs(b)} x 12 MHz", "cross"
            pl = path_loss(pdn_kind, f)
            add(fam, name, f, "gva", src[0] - pl[1], src[1] - pl[0],
                f"on-die current into the Pico 2 PDN ({Z_PDN[0]} to {Z_PDN[1]} ohm), path {pdn_kind} {pl[0]:.0f} to {pl[1]:.0f} dB", ck)

    # 2. clk_adc 48 MHz x 3 and PLL_USB
    if p["adc"] == "continuous":
        src = pdn_dbm(I_ADC_DOMAIN)
        pl = path_loss("pdn", 144.0)
        add("RP2350 clk_adc / PLL_USB", "clk_adc 48 MHz x 3 (continuous)", 144.0, "gva", src[0] - pl[1], src[1] - pl[0],
            "clk_adc domain current, continuous", "adc")
        if p["pll_usb"]:
            src = pdn_dbm(I_PLL_USB)
            add("RP2350 clk_adc / PLL_USB", "PLL_USB 48 MHz x 3 (running)", 144.0, "gva", src[0] - pl[1], src[1] - pl[0],
                "PLL_USB output clock tree", "adc")
    else:
        src = pdn_dbm(I_ADC_DOMAIN)
        pl = path_loss("pdn_p", 144.0)
        dl, dh = (10 * math.log10(d) for d in ADC_BURST_DUTY)
        add("RP2350 clk_adc / PLL_USB", "clk_adc 48 MHz x 3 (bursts, PLL_SYS / 2)", 144.0, "gva",
            src[0] - pl[1] + dl, src[1] - pl[0] + dh, f"mean power of burst duty {ADC_BURST_DUTY}", "adc")

    # 3. QSPI SCK on the Pico 2 module (trace source), activity factor as mean power
    act = p["qspi_activity"]
    if act[1] > 0:
        fq = fsys / p["qspi_div"]
        for n in range(1, 12):
            f = n * fq
            if not in_window(f):
                continue
            lv = square_line_dbm(3.3, n, fq, (1.0, 2.0), (0.0, 0.02))
            pl = path_loss("pico_trace", f)
            add("RP2350 QSPI SCK", f"QSPI SCK {fq:g} MHz x {n}", f, "gva",
                lv[0] - pl[1] + 10 * math.log10(max(act[0], 1e-3)), lv[1] - pl[0] + 10 * math.log10(act[1]),
                f"3.3 V trace, tr 1 to 2 ns, activity {act}", "qspi")

    # 4. 25 MHz reference: Si5351 on-die feedthrough to CLK1 (dBc) and the external reference lead
    for n in (5, 6, 7):
        f = n * F_REF
        add("Si5351 reference 25 MHz", f"25 MHz x {n}, Si5351 on-die feedthrough to CLK1", f, "pre", -75.0, -50.0,
            "no datasheet figure; below the -35 to -50 dBc output-to-output crosstalk reported for full-swing outputs (Low)", "ref")
        if fin == "A5":
            h = (-40.0, -25.0)       # clipped-sine harmonic 5 to 7 against a 0.8 Vpp fundamental (ESTIMATE)
            v0 = dbm_from_vpk(0.4)
            kind = "module"
            pl = path_loss(kind, f)
            add("Si5351 reference 25 MHz", f"25 MHz x {n}, TCXO lead near CLK1", f, "pre",
                v0 + h[0] - pl[1] - P_CLK1[1], v0 + h[1] - pl[0] - P_CLK1[0],
                f"TG2520SMN clipped sine 0.8 Vpp, harmonic {h} dBc, path module {pl[0]:.0f} to {pl[1]:.0f} dB", "tcxo")
        else:
            h = (-55.0, -40.0)       # crystal node, near sinusoidal (ESTIMATE)
            v0 = dbm_from_vpk(0.5)
            pl = path_loss("module", f)
            add("Si5351 reference 25 MHz", f"25 MHz x {n}, crystal node near CLK1", f, "pre",
                v0 + h[0] - pl[1] - P_CLK1[1], v0 + h[1] - pl[0] - P_CLK1[0],
                f"Si5351 XO crystal node 1 Vpp, harmonic {h} dBc", "tcxo")

    # 5. Si5351 PLL A spurs on the carrier (carrier-relative)
    for off in (-F_REF, F_REF):
        add("Si5351 PLL spurs", f"PFD reference spur fc {'+' if off > 0 else '-'} 25 MHz", fc + off, "pre", -85.0, -65.0,
            "VCO spur at the 25 MHz PFD offset, divided by 6 (-15.6 dB) (Low)", "pfd")
    for off in (-2.0, -0.5, 0.5, 2.0):
        add("Si5351 PLL spurs", f"fractional / integer-boundary spur fc {off:+g} MHz (representative)", fc + off, "pre",
            -80.0, -60.0, "PA3FWM tn42b: about -80 dBc in theory, measured worse (Low); offset depends on the fraction", "frac")

    # 6. Si5351 PLL B and CLK2 (BFO) products
    if p["pll_b"] == "running":
        for k in (1, 2):
            for sgn in (-1, 1):
                add("Si5351 PLL B / CLK2", f"CLK2 BFO product fc {'+' if sgn > 0 else '-'} {k} x 8 MHz (CLK2 powered down, PLL B running)",
                    fc + sgn * k * F_BFO, "pre", -75.0, -55.0,
                    "residual after CLK2 power-down; -35 to -50 dBc when the output runs (pavelmc Si5351_issues, NT7S part 8) (Low)", "bfo_xtalk")
        add("Si5351 PLL B / CLK2", f"VCO B {F_VCO_B:g} MHz / 6 through MS1", F_VCO_B / 6.0, "pre", -70.0, -50.0,
            "VCO B leakage into MS1 (Low)", "vco_b")

    # 7. /8 prescaler
    f8 = fc / 8.0
    for n in (7, 9):
        f = n * f8
        # (a) output-trace harmonic coupled to the CLK1 net
        lv = square_line_dbm(3.3, n, f8, (1.0, 2.0), (0.0, 0.01))
        if p["prescaler"] == "tap":
            pl = path_loss("prescaler", f)
            extra = (0.0, 0.0)
        else:
            pl = path_loss("prescaler_p", f)
            # 470 ohm series into a 5 to 8 pF GPIO and trace load: first-order low-pass on the trace
            extra = tuple(10 * math.log10(1 + (f / (1e-6 / (2 * math.pi * 470 * c))) ** 2) for c in (5e-12, 8e-12))
        add("/8 prescaler", f"/8 output x {n} ({n}/8 fc) on the trace", f, "pre",
            lv[0] - pl[1] - max(extra) - P_CLK1[1], lv[1] - pl[0] - min(extra) - P_CLK1[0],
            f"3.3 V, tr 1 to 2 ns; path {pl[0]:.0f} to {pl[1]:.0f} dB; RC {min(extra):.1f} to {max(extra):.1f} dB", "presc_trace")
        # (b) sidebands fc +/- fc/8 from the divider's input kickback and shared supply onto the CLK1 net
        if p["prescaler"] == "tap":
            lo, hi = -65.0, -45.0
            b = "100 pF tap on CLK1, shared VCC: fc +/- fc/8 sidebands (Low)"
        else:
            # Revision 1 (finding-2): revision 0 credited db20((330 + 25) / 25) = 23 dB, which ignores the flip-flop's
            # input capacitance and stops the clock (LTspice tx_spur_c7_tap.cir). The credit is now the LTspice
            # reverse isolation of the valid-clock resistor (tx_spur_c7_iso.cir, smallest over models and corners).
            iso = C7["iso_db"]
            lo, hi = -65.0 - iso, -45.0 - iso
            b = (f"{C7['rser']:g} ohm series tap, {iso:.1f} dB reverse isolation (LTspice, credited); separate supply per "
                 f"flip-flop named, not credited")
        add("/8 prescaler", f"/8 kickback sideband ({n}/8 fc)", f, "pre", lo, hi, b, "presc_kick")

    # 8. PWM comb (150 kHz): trace harmonics and VGG ripple sidebands
    fp = F_PWM if p["pwm_coherent"] else 125.0 / 834.0
    for f in np.arange(math.ceil(WINDOW[0] / fp) * fp, WINDOW[1], fp * 25):   # every 25th line kept for the plot
        n = int(round(f / fp))
        lv = square_line_dbm(3.3, n, fp, (2.0, 5.0), (0.0, 0.0))
        pl = path_loss("pico_trace", f)
        add("PWM comb", f"PWM {fp * 1e3:.2f} kHz x {n}", float(f), "gva", lv[0] - pl[1], lv[1] - pl[0],
            "3.3 V GPIO, tr 2 to 5 ns, every 25th line of the comb shown", "pwm_trace")
    s_vgg = 0.6                      # 1/V: relative amplitude slope at 5 W (TS-012 7.3 graph points, 4 W at 3.0 V, 7 W at 3.5 V)
    rip = (2.1 / (150.0 / 1.0) ** 2, 2.1 / (150.0 / 3.0) ** 2)  # V at VGG: 2-pole RC, corner 1 to 3 kHz (ESTIMATE)
    for k in (1, 2):
        for sgn in (-1, 1):
            add("VGG / supply sidebands", f"envelope-reference PWM ripple, fc {'+' if sgn > 0 else '-'} {k} x 150 kHz", fc + sgn * k * F_PWM, "rel",
                db20(s_vgg * rip[0] / 2) - 6 * (k - 1), db20(s_vgg * rip[1] / 2) - 6 * (k - 1),
                "AM index m = 0.6/V x ripple; ripple 0.23 to 0.84 mV (2-pole RC, 1 to 3 kHz)", "pwm_vgg")

    # 9. Switcher sidebands through the GVA-84+ bias and the Si5351 VDD
    for name, fsw in F_SW.items():
        for k in (1, 2, 3):
            for sgn in (-1, 1):
                rip = (0.3e-3, 3e-3) if plan_id in ("P", "PB") else (1e-3, 10e-3)   # F3 filter in P and PB
                dg = (0.3 * rip[0], 1.0 * rip[1])   # dB: 0.3 to 1 dB/V gain sensitivity (ESTIMATE)
                m = tuple(0.115 * x for x in dg)
                add("VGG / supply sidebands", f"{name} ripple on the GVA-84+ bias, fc {'+' if sgn > 0 else '-'} {k} x {fsw:g} MHz",
                    fc + sgn * k * fsw, "rel", db20(m[0] / 2) - 6 * (k - 1), db20(m[1] / 2) - 6 * (k - 1),
                    f"ripple {rip[0] * 1e3:g} to {rip[1] * 1e3:g} mV at the GVA-84+ Vcc", "supply")
    return L


# ---------------------------------------------------------------- evaluation
def g_eff(fin: str, flt: Filters, fc: float, plan: str = "P") -> tuple[float, float]:
    if fin == "A5":
        pc = (P_CLK1[0] + flt.hd(fc, plan), P_CLK1[1] + flt.hd(fc, plan))
    else:
        pc = P_CAR_GVA_A4
    return P_CARRIER_ANT - pc[1], P_CARRIER_ANT - pc[0]


def evaluate(lines: list[Line], flt: Filters) -> list[Line]:
    out = []
    for ln in lines:
        fc = ln.carrier
        dho = flt.ho(ln.f) - flt.ho(fc)
        if ln.inj == "pre":
            d = flt.hd(ln.f, ln.plan) - flt.hd(fc, ln.plan)
            ln.ant_lo = P_CARRIER_ANT + ln.lo + d + dho
            ln.ant_hi = P_CARRIER_ANT + ln.hi + d + dho
        elif ln.inj == "gva":
            g = g_eff(ln.finalist, flt, fc, ln.plan)
            ln.ant_lo = ln.lo + g[0] + dho
            ln.ant_hi = ln.hi + g[1] + dho
        else:
            ln.ant_lo = P_CARRIER_ANT + ln.lo + dho
            ln.ant_hi = P_CARRIER_ANT + ln.hi + dho
        out.append(ln)
        # mirror line of a saturated final stage (not for carrier-relative sidebands, already symmetric)
        if ln.inj != "rel" and ln.family != "Si5351 PLL spurs" and abs(ln.f - fc) > 0.01:
            fm = round(2 * fc - ln.f, 4)
            if in_window(fm):
                m = Line(**{**asdict(ln), "f": fm, "mirror": True, "source": f"mirror of {ln.source}"})
                m.ant_lo, m.ant_hi = ln.ant_lo - 6.0 - dho + (flt.ho(fm) - flt.ho(fc)), ln.ant_hi - 6.0 - dho + (flt.ho(fm) - flt.ho(fc))
                out.append(m)
    return out


def combine(lines: list[Line]) -> list[Line]:
    """Coincident lines (within 1 kHz): amplitude sum for the high end, strongest for the low end."""
    groups: dict = {}
    for ln in lines:
        groups.setdefault(round(ln.f, 3), []).append(ln)
    res = []
    for f, g in groups.items():
        if len(g) == 1:
            res.append(g[0])
            continue
        hi = db20(sum(10 ** (x.ant_hi / 20) for x in g))
        lo = max(x.ant_lo for x in g)
        top = max(g, key=lambda x: x.ant_hi)
        c = Line(**{**asdict(top), "source": f"{len(g)} coincident lines at {f:.3f} MHz (amplitude sum)"})
        c.ant_lo, c.ant_hi = lo, hi
        c.contributors = [f"{x.source}: {x.ant_lo:.1f} to {x.ant_hi:.1f} dBm" for x in g]
        c.change = "; ".join(sorted({x.change for x in g if x.change}))
        c.change_kind = "/".join(sorted({x.change_kind for x in g}))
        c.credited = sorted({y for x in g for y in x.credited})
        c.named = sorted({y for x in g for y in x.named})
        res.append(c)
    return res


def verdicts(lines: list[Line]) -> None:
    for ln in lines:
        ln.gva_lo, ln.gva_hi = ln.ant_lo - G_REF, ln.ant_hi - G_REF
        for lim, attr in ((LIM_TARGET_ANT, "verdict_target"), (LIM_LEGAL_ANT, "verdict_legal")):
            v = "pass" if ln.ant_hi <= lim else ("fail" if ln.ant_lo > lim else "not shown")
            setattr(ln, attr, v)


def run_case(plan_id, fin, fc, flt):
    lines = combine(evaluate(build_lines(plan_id, fin, fc), flt))
    verdicts(lines)
    return lines


# ---------------------------------------------------------------- figures
COL = {"pre": "#2a78d6", "gva": "#eb6834", "rel": "#1baf7a"}
INJ_LABEL = {"pre": "on the Si5351 CLK1 net (Si5351 feedthrough and PLL spurs, prescaler, reference lead)",
             "gva": "coupled at the GVA-84+ input (RP2350 on-die, QSPI, PWM)",
             "rel": "carrier sidebands (VGG and supply ripple)"}


def spectrum_axes(ax, lines, fc, title):
    ax.axvspan(WINDOW[0], WINDOW[1], color="#f1f0ec", zorder=0)
    for inj in ("pre", "gva", "rel"):
        sel = [x for x in lines if x.inj == inj]
        if not sel:
            continue
        f = np.array([x.f for x in sel])
        lo = np.array([x.gva_lo for x in sel])
        hi = np.array([x.gva_hi for x in sel])
        ax.vlines(f, lo, hi, color=COL[inj], lw=2.2, alpha=0.85, zorder=3)
        ax.scatter(f, hi, s=18, color=COL[inj], zorder=4, label=INJ_LABEL[inj], edgecolor="white", linewidth=0.6)
    ax.axhline(LIM_LEGAL_GVA, color="#0b0b0b", lw=1.4, zorder=2)
    ax.axhline(LIM_TARGET_GVA, color="#52514e", lw=1.4, ls="--", zorder=2)
    ax.text(WINDOW[1] + 0.5, LIM_LEGAL_GVA + 1, "-61 dBm: 25 uW at the SMA (97.307(e))", fontsize=7.5, ha="left", va="bottom", color="#0b0b0b")
    ax.text(WINDOW[1] + 0.5, LIM_TARGET_GVA - 1, "-68 dBm: 60 dBc target", fontsize=7.5, ha="left", va="top", color="#52514e")
    ax.axvline(fc, color="#8a8984", lw=0.8, ls=":")
    ax.text(fc + 0.6, -148, f"carrier {fc:.3f} MHz", fontsize=7, ha="left", va="bottom", color="#52514e")
    # label the worst few lines
    worst = sorted([x for x in lines if x.verdict_target != "pass"], key=lambda x: -x.gva_hi)
    used = []
    for x in worst[:7]:
        if any(abs(x.f - u) < 3.5 for u in used):
            continue
        used.append(x.f)
        ax.annotate(short(x), (x.f, x.gva_hi), xytext=(0, 7), textcoords="offset points", fontsize=6.6,
                    ha="center", va="bottom", color="#0b0b0b", rotation=90)
    ax.set_xlim(112, 196)
    ax.set_ylim(-150, -10)
    ax.set_title(title, fontsize=10, loc="left")
    ax.set_ylabel("level referred to GVA-84+ input (dBm)\n(= antenna level - 45 dB)", fontsize=8.5)
    ax.grid(axis="y", color="#e4e3df", lw=0.6)
    ax.tick_params(labelsize=8)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)


def short(x: Line) -> str:
    if "coincident" in x.source:
        return f"{x.f:.3f} (sum)"
    return f"{x.f:.3f}" + (" (mirror)" if x.mirror else "")


def fig_spectrum(res, out: Path, fin: str, fc: float):
    fig, axes = plt.subplots(4, 1, figsize=(11, 17), sharex=True)
    for ax, pid in zip(axes, ("B0", "B1", "P", "PB")):
        lines = res[(pid, fin, fc)]
        n_bad = sum(1 for x in lines if x.ant_hi > LIM_TARGET_ANT)
        n_leg = sum(1 for x in lines if x.ant_hi > LIM_LEGAL_ANT)
        spectrum_axes(ax, lines, fc, f"{PLANS[pid]['label']}  |  {FINALISTS[fin]['label']}  |  "
                                     f"{n_bad} of {len(lines)} lines over -68 dBm, {n_leg} over -61 dBm (high estimate)")
    h, lab = axes[0].get_legend_handles_labels()
    fig.legend(h, lab, loc="lower center", ncol=2, fontsize=8, frameon=False)
    axes[-1].set_xlabel("frequency (MHz); shaded: 118 to 175 MHz window of TS-012 7.3; labels: MHz of lines over -68 dBm at the high estimate", fontsize=8.5)
    fig.suptitle("Transmit clock lines at 5 W: estimated range (bar) and high estimate (dot) against the TS-012 budget (all levels ESTIMATES)",
                 fontsize=11, x=0.01, ha="left")
    fig.tight_layout(rect=(0, 0.035, 0.93, 0.98))
    fig.savefig(out, dpi=130)
    plt.close(fig)


def fig_antenna(res, flt: Filters, out: Path, fc: float):
    fig, axes = plt.subplots(2, 2, figsize=(15, 9.5), sharex=True, sharey=True)
    for row, fin in enumerate(("A5", "A4")):
        for col, pid in enumerate(("P", "PB")):
            ax = axes[row][col]
            lines = res[(pid, fin, fc)]
            for inj in ("pre", "gva", "rel"):
                sel = [x for x in lines if x.inj == inj]
                f = np.array([x.f for x in sel])
                ax.vlines(f, [x.ant_lo for x in sel], [x.ant_hi for x in sel], color=COL[inj], lw=2.2, alpha=0.85)
                ax.scatter(f, [x.ant_hi for x in sel], s=18, color=COL[inj], edgecolor="white", linewidth=0.6, label=INJ_LABEL[inj])
            ax.axhline(LIM_LEGAL_ANT, color="#0b0b0b", lw=1.4)
            ax.axhline(LIM_TARGET_ANT, color="#52514e", lw=1.4, ls="--")
            ax.text(196, LIM_LEGAL_ANT + 1, "-16 dBm (25 uW)", fontsize=7.5, va="bottom", ha="right")
            ax.text(196, LIM_TARGET_ANT - 1, "-23 dBm (60 dBc at 5 W)", fontsize=7.5, va="top", ha="right", color="#52514e")
            fr = flt.f_mhz
            m = (fr >= 112) & (fr <= 196)
            ax.plot(fr[m], P_CARRIER_ANT + flt.out[m] - flt.ho(fc), color="#8a8984", lw=1.2,
                    label="harmonic LPF response + 37 dBm (LTspice, Q 60)")
            ax.axvline(fc, color="#8a8984", lw=0.8, ls=":")
            resid = sorted([x for x in lines if x.ant_hi > LIM_TARGET_ANT], key=lambda x: -x.ant_hi)
            used = []
            for x in resid[:6]:
                if any(abs(x.f - u) < 3.0 for u in used):
                    continue
                used.append(x.f)
                ax.annotate(f"{x.f:.2f}", (x.f, x.ant_hi), xytext=(0, 6), textcoords="offset points", fontsize=6.8, ha="center", rotation=90)
            n_leg = sum(1 for x in resid if x.ant_hi > LIM_LEGAL_ANT)
            ax.set_title(f"{FINALISTS[fin]['label']}, plan {pid}, carrier {fc:.3f} MHz:\n"
                         f"{len(resid)} residual lines over -23 dBm, {n_leg} over -16 dBm (high estimate)", fontsize=9.5, loc="left")
            ax.set_ylim(-110, 45)
            ax.set_xlim(112, 196)
            ax.grid(axis="y", color="#e4e3df", lw=0.6)
            for sp in ("top", "right"):
                ax.spines[sp].set_visible(False)
            ax.tick_params(labelsize=8)
            if col == 0:
                ax.set_ylabel("level at the SMA (dBm)", fontsize=8.5)
            if row == 1:
                ax.set_xlabel("frequency (MHz); labels: MHz of residual lines", fontsize=8.5)
    axes[0][0].legend(loc="upper left", fontsize=7, frameon=False)
    fig.suptitle("Plans P and PB at the SMA after every credited change (all levels ESTIMATES; bar = low to high estimate)",
                 fontsize=10.5, x=0.01, ha="left")
    fig.tight_layout(rect=(0, 0, 1, 0.96))
    fig.savefig(out, dpi=130)
    plt.close(fig)


def fig_sweep(sweep, counts, counts_legal, out: Path):
    fig, axes = plt.subplots(3, 1, figsize=(11, 11), sharex=True)
    style = {"B0": ("#eb6834", (0, (1, 1)), 3.2), "B1": ("#2a78d6", "-", 1.6), "P": ("#1baf7a", "-", 2.0), "PB": ("#4a3aa7", "-", 2.0)}
    for (pid, fin), vals in sweep.items():
        c, ls, lw = style[pid]
        ls = ls if fin == "A5" else (0, (5, 2))
        axes[0].plot(SWEEP, vals, color=c, ls=ls, lw=lw, label=f"{pid}, {fin}")
        axes[1].plot(SWEEP, counts[(pid, fin)], color=c, ls=ls, lw=lw)
        axes[2].plot(SWEEP, counts_legal[(pid, fin)], color=c, ls=ls, lw=lw)
    ax = axes[0]
    ax.axhline(LIM_TARGET_ANT, color="#52514e", lw=1.4, ls="--")
    ax.axhline(LIM_LEGAL_ANT, color="#0b0b0b", lw=1.4)
    ax.text(144.02, LIM_TARGET_ANT + 0.4, "-23 dBm: 60 dBc at 5 W", fontsize=8, va="bottom", color="#52514e")
    ax.text(144.02, LIM_LEGAL_ANT + 0.4, "-16 dBm: 25 uW", fontsize=8, va="bottom")
    ax.set_ylim(-26, 3)
    ax.set_ylabel("strongest line at the SMA,\nhigh estimate (dBm)", fontsize=9)
    ax.set_title("Worst transmit clock line (118 to 175 MHz) over the carrier range, after the credited changes of each plan",
                 fontsize=10, loc="left")
    axes[1].set_ylabel("residual lines above -23 dBm\n(60 dBc) at the high estimate", fontsize=9)
    axes[2].set_ylabel("residual lines above -16 dBm\n(25 uW) at the high estimate", fontsize=9)
    axes[2].set_xlabel("carrier frequency (MHz); solid A5, dashed A4", fontsize=9)
    for a in axes:
        a.grid(axis="y", color="#e4e3df", lw=0.6)
        a.set_xlim(144.0, 148.0)
        for sp in ("top", "right"):
            a.spines[sp].set_visible(False)
        a.tick_params(labelsize=8)
    h, lab = axes[0].get_legend_handles_labels()
    fig.legend(h, [f"{x}  ({PLANS[x.split(',')[0]]['label'].split(': ')[1]})" if x.endswith("A5") else x for x in lab],
               loc="lower center", ncol=4, fontsize=7.5, frameon=False)
    fig.tight_layout(rect=(0, 0.07, 1, 1))
    fig.savefig(out, dpi=130)
    plt.close(fig)


def fig_filters(flt: Filters, out: Path, check: dict):
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.8))
    f = flt.f_mhz
    ax = axes[0]
    ax.plot(f, flt.drive_ideal, color="#2a78d6", lw=2, label="LTspice, ideal")
    ax.plot(f, flt.drive, color="#eb6834", lw=1.4, ls="--", label="LTspice, inductor Q 60")
    ax.plot(f, analytic_butter3(f, 170.0) - 18.0, color="#0b0b0b", lw=0.9, ls=":", label="analytic Butterworth - 18 dB")
    ax.axvspan(*WINDOW, color="#f1f0ec", zorder=0)
    ax.plot(f, flt.drive_bpf, color="#1baf7a", lw=1.6, label="LTspice, option C10 bandpass, Q 60")
    ax.set_title("Drive filter + 18 dB pad (to the GVA-84+ input)", fontsize=10, loc="left")
    ax.set_ylim(-60, -15)
    ax2 = axes[1]
    ax2.plot(f, flt.out_ideal, color="#2a78d6", lw=2, label="LTspice, ideal")
    ax2.plot(f, flt.out, color="#eb6834", lw=1.4, ls="--", label="LTspice, inductor Q 60")
    ax2.plot(f, analytic_cheby(f, 165.0), color="#0b0b0b", lw=0.9, ls=":", label="analytic Chebyshev 0.1 dB")
    ax2.axvspan(*WINDOW, color="#f1f0ec", zorder=0)
    for fx, lab in ((288, "40 dB req. at 288 MHz"), (432, "35 dB req. at 432 MHz")):
        ax2.plot([fx], [-40 if fx == 288 else -35], marker="v", color="#e34948", ms=8)
        ax2.text(fx, (-40 if fx == 288 else -35) + 3, lab, fontsize=7.5, ha="center")
    ax2.set_ylim(-100, 5)
    ax2.set_title("Harmonic low-pass (7-pole Chebyshev, 165 MHz)", fontsize=10, loc="left")
    for a in axes:
        a.set_xlabel("frequency (MHz)", fontsize=9)
        a.set_ylabel("S21 (dB)", fontsize=9)
        a.grid(color="#e4e3df", lw=0.6)
        a.legend(fontsize=7.5, frameon=False, loc="lower left")
        for s in ("top", "right"):
            a.spines[s].set_visible(False)
    fig.suptitle(f"Filter transfers used by the spur plan (max LTspice-analytic difference 100 to 500 MHz: "
                 f"drive {check['drive_max_diff_db']:.3f} dB, harmonic {check['out_max_diff_db']:.3f} dB)",
                 fontsize=9.5, x=0.01, ha="left")
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    fig.savefig(out, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------- option C10 tolerance corners (LTspice)
def c10_tolerance(raw_path: Path, flt: "Filters") -> dict | None:
    """Corners kl, kc in {0.95, 0.98, 1, 1.02, 1.05} of tx_spur_bpf_tol.cir. Pass, at every 2 % corner: S21 at 144 and
    148 MHz within 3 dB of the nominal C10 value at 146 MHz, and at least 10 dB of rejection at 125 MHz against the
    passband. The 5 % corners are reported (pass_5pct) for J-tolerance parts."""
    if not raw_path.exists():
        return None
    raw = RawRead(str(raw_path))
    steps = raw.get_steps()
    f = np.real(raw.get_trace("frequency").get_wave(steps[0])) / 1e6
    nom = flt.hd(146.0, "PB")
    corners, curves = [], []
    grid = (0.95, 0.98, 1.0, 1.02, 1.05)
    ks = [(kl, kc) for kl in grid for kc in grid]   # .step order: kl outer, kc inner
    for i, st in enumerate(steps):
        w = 20 * np.log10(np.abs(raw.get_trace("V(outb)").get_wave(st)) * 2.0)
        kl, kc = ks[i] if i < len(ks) else (float("nan"), float("nan"))
        s144, s148, s125 = (float(np.interp(x, f, w)) for x in (144.0, 148.0, 125.0))
        corners.append(dict(kl=kl, kc=kc, s144_dB=round(s144, 2), s148_dB=round(s148, 2), s125_dB=round(s125, 2),
                            passband_dev_dB=round(max(abs(s144 - nom), abs(s148 - nom)), 2),
                            rejection_125_dB=round(min(s144, s148) - s125, 1)))
        curves.append((kl, kc, f, w))
    def okc(c):
        return c["passband_dev_dB"] <= 3.0 and c["rejection_125_dB"] >= 10.0
    ok = all(okc(c) for c in corners if max(abs(c["kl"] - 1), abs(c["kc"] - 1)) <= 0.021)
    ok5 = all(okc(c) for c in corners)
    return dict(nominal_146_dB=round(nom, 2), corners=corners, pass_=ok, pass_5pct=ok5, curves=curves)


# ---------------------------------------------------------------- ADR-031 receive-band re-check for C1 (96 MHz)
def rx_check_clk_sys(fsys_mhz: float = 96.0) -> dict:
    """ADR-031 rules 1 and 4 for the clear-class clocks derived from clk_sys = fsys: no line of n f (1 +/- 65 ppm)
    in 144.010 to 147.999 MHz (REQ-SYS-034 receive range). Covers clk_sys, SPI SCK fsys/d (d even 2 to 24),
    QSPI SCK fsys/CLKDIV (1 to 24) and the dense PWM coherence (TOP+1 = fsys / 150 kHz)."""
    from fractions import Fraction as Fr
    lo, hi, tol = Fr("144.010"), Fr("147.999"), Fr(65, 10**6)
    fs = Fr(fsys_mhz).limit_denominator(1000)

    def hits(f):
        out = []
        n = 1
        while n * f * (1 - tol) <= hi:
            a, b = n * f * (1 - tol), n * f * (1 + tol)
            if b >= lo and a <= hi:
                out.append(f"n={n}: {float(a):.4f} to {float(b):.4f} MHz")
            n += 1
        return out

    res = {"clk_sys": hits(fs)}
    res["spi"] = {f"{fsys_mhz:g}/{d}": hits(fs / d) for d in range(2, 25, 2) if fs / d >= 4}
    res["qspi"] = {f"{fsys_mhz:g}/{d}": hits(fs / d) for d in range(1, 25) if fs / d >= 4}
    top = fs * 1000 / Fr(150)
    res["pwm_top_plus_1_for_150kHz"] = str(top)
    res["pwm_coherent_with_144MHz"] = (Fr(144000, 150).denominator == 1 and top.denominator == 1)
    bad = [k for k, v in res["spi"].items() if v] + [k for k, v in res["qspi"].items() if v] + (["clk_sys"] if res["clk_sys"] else [])
    res["clear_class_with_rx_band_line"] = bad
    return res


def fig_c10(tol, out: Path):
    fig, ax = plt.subplots(figsize=(10, 5))
    for kl, kc, f, w in tol["curves"]:
        nominal = kl == 1.0 and kc == 1.0
        two = max(abs(kl - 1), abs(kc - 1)) <= 0.021
        ax.plot(f, w, color="#1baf7a" if nominal else ("#2a78d6" if two else "#c3c2b7"), lw=2.4 if nominal else (1.1 if two else 0.8),
                zorder=3 if nominal else (2 if two else 1), label="nominal" if nominal else None)
    ax.plot([], [], color="#2a78d6", lw=1.1, label="2 % corners (G parts): pass criterion")
    ax.plot([], [], color="#c3c2b7", lw=0.8, label="5 % corners (J parts): reported")
    nom = tol["nominal_146_dB"]
    ax.axhspan(nom - 3, nom + 3, xmin=0, xmax=1, color="#f1f0ec", zorder=0)
    ax.axvspan(144, 148, color="#e4e3df", zorder=0)
    ax.axhline(nom - 3, color="#52514e", lw=1.2, ls="--")
    ax.text(101, nom - 3.4, f"pass: 144 and 148 MHz within 3 dB of the nominal {nom:.1f} dB", fontsize=8, va="top", color="#52514e")
    two = [c for c in tol["corners"] if max(abs(c["kl"] - 1), abs(c["kc"] - 1)) <= 0.021]
    worst = max(c["passband_dev_dB"] for c in two)
    wr = min(c["rejection_125_dB"] for c in two)
    w5 = max(c["passband_dev_dB"] for c in tol["corners"])
    r5 = min(c["rejection_125_dB"] for c in tol["corners"])
    ax.set_title(f"Option C10 drive bandpass + 18 dB pad (LTspice). 2 % corners: passband deviation {worst:.1f} dB, 125 MHz rejection "
                 f"{wr:.1f} dB: {'PASS' if tol['pass_'] else 'FAIL'}\n5 % corners: {w5:.1f} dB and {r5:.1f} dB: "
                 f"{'pass' if tol['pass_5pct'] else 'fail'} (J parts not admitted for C10)", fontsize=9.5, loc="left")
    ax.set_xlim(100, 200)
    ax.set_ylim(-60, -15)
    ax.set_xlabel("frequency (MHz); dark band: 144 to 148 MHz", fontsize=9)
    ax.set_ylabel("S21 to the GVA-84+ input (dB)", fontsize=9)
    ax.grid(color="#e4e3df", lw=0.6)
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    ax.legend(fontsize=8, frameon=False, loc="lower right")
    fig.tight_layout()
    fig.savefig(out, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------- C7 prescaler tap: valid clock and isolation (finding-2)
TAP_RSER = (0.001, 47.0, 100.0, 150.0, 220.0, 330.0)


def c7_tap(raw_path: Path) -> dict:
    """tx_spur_c7_tap.cir: per corner, the CP pin minimum and maximum over the last three periods, the margins to
    VIL and VIH, the HIGH and LOW widths at VM 1.5 V, and the slowest input transition through 0.8 to 2.0 V."""
    raw = RawRead(str(raw_path))
    rows = []
    for i in raw.get_steps():
        isrc, ifr, irs, icp, ir = i % 3, (i // 3) % 2, (i // 6) % 2, (i // 12) % 2, i // 24
        f = (144e6, 148e6)[ifr]
        t = np.real(raw.get_trace("time").get_wave(i))
        v = np.real(raw.get_trace("V(pin)").get_wave(i))
        vc = np.real(raw.get_trace("V(clk)").get_wave(i))
        m = t >= t[-1] - 3.0 / f
        tt, vv = t[m], v[m]
        up = np.where((vv[:-1] < VM_LVC) & (vv[1:] >= VM_LVC))[0]
        dn = np.where((vv[:-1] >= VM_LVC) & (vv[1:] < VM_LVC))[0]

        def cross(k):
            return tt[k] + (VM_LVC - vv[k]) * (tt[k + 1] - tt[k]) / (vv[k + 1] - vv[k])
        tu, td = [cross(k) for k in up], [cross(k) for k in dn]
        highs = [min(x for x in td if x > u) - u for u in tu if any(x > u for x in td)]
        lows = [min(x for x in tu if x > d) - d for d in td if any(x > d for x in tu)]
        # transition rate through VIL..VIH: the time the rising edge spends between 0.8 and 2.0 V, per volt
        dv = np.gradient(vv, tt)
        band = (vv > VIL_LVC) & (vv < VIH_LVC) & (dv > 0)
        slow = float(np.max(1.0 / dv[band])) if np.any(band) else float("nan")
        rows.append(dict(rser=TAP_RSER[ir], src=("low", "nom", "high")[isrc], f_MHz=f / 1e6, rsrc=(25, 50)[irs],
                         cpad_pF=(1, 3)[icp], vmin=round(float(vv.min()), 3), vmax=round(float(vv.max()), 3),
                         clk_vpp=round(float(vc[m].max() - vc[m].min()), 3),
                         margin_vil=round(VIL_LVC - float(vv.min()), 3), margin_vih=round(float(vv.max()) - VIH_LVC, 3),
                         tw_high_ns=round(min(highs) * 1e9, 2) if highs else None,
                         tw_low_ns=round(min(lows) * 1e9, 2) if lows else None,
                         dtdv_ns_per_V=round(slow * 1e9, 2), t=tt, v=vv))
    per_r = {}
    for r in TAP_RSER:
        sel = [x for x in rows if x["rser"] == r]
        mv = min(min(x["margin_vil"], x["margin_vih"]) for x in sel)
        tw = min(min(x["tw_high_ns"] or 0, x["tw_low_ns"] or 0) for x in sel)
        dtdv = max(x["dtdv_ns_per_V"] for x in sel)
        per_r[r] = dict(worst_margin_V=round(mv, 3), worst_tw_ns=round(tw, 2), worst_dtdv_ns_per_V=round(dtdv, 2),
                        valid=bool(mv >= VCLK_MARGIN and tw * 1e-9 >= TW_MIN_LVC and dtdv * 1e-9 <= DTDV_MAX_LVC),
                        pin_min_V=min(x["vmin"] for x in sel), pin_max_V=max(x["vmax"] for x in sel),
                        pin_max_of_min_V=max(x["vmin"] for x in sel), pin_min_of_max_V=min(x["vmax"] for x in sel))
    rmax = max((r for r in TAP_RSER if per_r[r]["valid"]), default=None)
    return dict(rows=rows, per_rser=per_r, rser_max_valid=rmax,
                clk_vpp_range=[min(x["clk_vpp"] for x in rows), max(x["clk_vpp"] for x in rows)])


def c7_iso(raw_path: Path) -> dict:
    """tx_spur_c7_iso.cir: |V(clk)| at each Rser against Rser = 0 (same source resistance and pad capacitance), over
    the 7/8 fc and 9/8 fc ranges, for the current-injection (I) and ground-bounce (G) kickback models."""
    raw = RawRead(str(raw_path))
    f = np.real(raw.get_trace("frequency").get_wave(0)) / 1e6
    band = ((f >= 126.0) & (f <= 129.5)) | ((f >= 162.0) & (f <= 166.5))
    ref, curves = {}, {}
    for i, sp in enumerate(raw.steps):
        k = (sp["rsrc"], sp["cpad"])
        for mdl in ("I", "G"):
            a = np.abs(raw.get_trace(f"V(clk{mdl})").get_wave(i))
            curves[(sp["rser"], k, mdl)] = a
            if sp["rser"] < 1.0:
                ref[(k, mdl)] = a
    per_r = {}
    for (r, k, mdl), a in curves.items():
        iso = 20 * np.log10(ref[(k, mdl)] / a)
        d = per_r.setdefault(r, dict(min_db=1e9, max_db=-1e9))
        d["min_db"] = min(d["min_db"], float(np.min(iso[band])))
        d["max_db"] = max(d["max_db"], float(np.max(iso[band])))
    for r in per_r:
        per_r[r] = {k2: round(v, 2) for k2, v in per_r[r].items()}
        per_r[r]["revision0_claim_db"] = round(db20((r + 25.0) / 25.0), 1)
    return dict(per_rser=per_r, f=f, curves=curves, ref=ref)


def fig_c7(tap: dict, iso: dict, out: Path):
    fig, axes = plt.subplots(1, 3, figsize=(15, 5.2))
    ax = axes[0]
    rs = np.array(TAP_RSER)
    rs_plot = np.where(rs < 1, 0, rs)
    lo = [tap["per_rser"][r]["pin_max_of_min_V"] for r in TAP_RSER]
    hi = [tap["per_rser"][r]["pin_min_of_max_V"] for r in TAP_RSER]
    for x in tap["rows"]:
        xr = 0 if x["rser"] < 1 else x["rser"]
        ax.plot([xr, xr], [x["vmin"], x["vmax"]], color="#c3c2b7", lw=0.8, zorder=1)
    ax.plot(rs_plot, lo, "o-", color="#2a78d6", lw=1.8, label="pin low swing, worst corner (highest minimum)")
    ax.plot(rs_plot, hi, "o-", color="#eb6834", lw=1.8, label="pin high swing, worst corner (lowest maximum)")
    ax.axhline(VIH_LVC, color="#0b0b0b", lw=1.3)
    ax.axhline(VIL_LVC, color="#0b0b0b", lw=1.3)
    ax.axhline(VIH_LVC + VCLK_MARGIN, color="#52514e", lw=1, ls="--")
    ax.axhline(VIL_LVC - VCLK_MARGIN, color="#52514e", lw=1, ls="--")
    ax.text(262, VIH_LVC - 0.03, "VIH 2.0 V", fontsize=7.5, va="top", ha="center", backgroundcolor="white")
    ax.text(262, VIL_LVC + 0.03, "VIL 0.8 V", fontsize=7.5, va="bottom", ha="center", backgroundcolor="white")
    ax.text(5, VIH_LVC + VCLK_MARGIN + 0.02, f"+{VCLK_MARGIN:.2f} V margin (bias spread)", fontsize=7, va="bottom", color="#52514e")
    ax.axvline(C7["rser"], color="#1baf7a", lw=1.5)
    ax.text(C7["rser"] + 4, 2.9, f"C7 rev 1: {C7['rser']:g} ohm", fontsize=8, color="#1baf7a")
    ax.axvline(330, color="#e34948", lw=1.2, ls=":")
    ax.text(326, 2.9, "rev 0: 330 ohm", fontsize=8, color="#e34948", ha="right")
    ax.set_xlabel("series resistor after the 100 pF tap (ohm)", fontsize=9)
    ax.set_ylabel("74LVC1G80 CP pin voltage (V)", fontsize=9)
    ax.set_ylim(0, 3.1)
    rmax = tap["rser_max_valid"]
    ax.set_title(f"Valid clock (LTspice, 24 corners per value; grey: every corner)\nlargest valid: {rmax:g} ohm; 330 ohm: "
                 f"worst margin {tap['per_rser'][330.0]['worst_margin_V']:+.2f} V (FAIL)", fontsize=9.5, loc="left")
    ax.legend(fontsize=7, frameon=False, loc="center right")
    # waveforms at the worst corner for 47 and 330 ohm
    ax = axes[1]
    for r, c in ((0.001, "#8a8984"), (C7["rser"], "#1baf7a"), (330.0, "#e34948")):
        sel = [x for x in tap["rows"] if x["rser"] == r]
        w = min(sel, key=lambda x: min(x["margin_vil"], x["margin_vih"]))
        tt = (w["t"] - w["t"][0]) * 1e9
        ax.plot(tt, w["v"], color=c, lw=1.6, label=f"{0 if r < 1 else r:g} ohm: {w['src']} source, {w['rsrc']} ohm, "
                                                     f"{w['f_MHz']:.0f} MHz, pad {w['cpad_pF']} pF")
    ax.axhline(VIH_LVC, color="#0b0b0b", lw=1.3)
    ax.axhline(VIL_LVC, color="#0b0b0b", lw=1.3)
    ax.axhline(VM_LVC, color="#52514e", lw=0.8, ls=":")
    ax.set_xlabel("time (ns), last three periods", fontsize=9)
    ax.set_ylabel("CP pin (V)", fontsize=9)
    ax.set_ylim(0, 3.1)
    ax.set_title("CP pin at each value's worst corner", fontsize=9.5, loc="left")
    ax.legend(fontsize=7, frameon=False, loc="upper right")
    ax = axes[2]
    iso_min = [iso["per_rser"][r]["min_db"] for r in TAP_RSER]
    iso_max = [iso["per_rser"][r]["max_db"] for r in TAP_RSER]
    claim = [db20((r + 25.0) / 25.0) for r in TAP_RSER]
    ax.fill_between(rs_plot, iso_min, iso_max, color="#2a78d6", alpha=0.25, label="LTspice, both kickback models, all corners")
    ax.plot(rs_plot, iso_min, "o-", color="#2a78d6", lw=1.8, label="LTspice, smallest (credited)")
    ax.plot(rs_plot, claim, "s--", color="#e34948", lw=1.4, label="revision 0: db20((R + 25) / 25)")
    ax.axvspan(-5, rmax, color="#e8f5ee", zorder=0)
    ax.text(rmax / 2, 0.97, "valid\nclock", fontsize=8, color="#1baf7a", ha="center", va="top", transform=ax.get_xaxis_transform())
    ax.axvline(C7["rser"], color="#1baf7a", lw=1.5)
    ax.set_xlabel("series resistor (ohm)", fontsize=9)
    ax.set_ylabel("reverse isolation of the kickback at 7/8 and 9/8 fc (dB)", fontsize=9)
    ax.set_title(f"Isolation credited: {C7['iso_db']:.1f} dB at {C7['rser']:g} ohm.\nRevision 0 claimed 23 dB at 330 ohm; "
                 f"LTspice: {iso['per_rser'][330.0]['min_db']:.1f} dB,\nand 330 ohm stops the clock", fontsize=9.5, loc="left")
    ax.set_xlim(-5, 340)
    ax.legend(fontsize=7, frameon=False, loc="upper left", bbox_to_anchor=(0.22, 1.0))
    for a in axes:
        a.grid(color="#e4e3df", lw=0.6)
        for sp in ("top", "right"):
            a.spines[sp].set_visible(False)
        a.tick_params(labelsize=8)
    fig.suptitle("Change C7 (/8 prescaler tap on CLK1): 74LVC1G80 input levels (Nexperia Rev. 17 Table 7) and the reverse isolation it buys",
                 fontsize=10.5, x=0.01, ha="left")
    fig.tight_layout(rect=(0, 0, 1, 0.93))
    fig.savefig(out, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------- T1 trap sizing with its carrier cost (finding-1 c)
T1_CARRIERS = (144.010, 144.050, 146.000, 147.990)


def t1_trap(raw_path: Path) -> dict:
    raw = RawRead(str(raw_path))
    f = np.real(raw.get_trace("frequency").get_wave(0)) / 1e6
    rows, curves = [], []
    for i, sp in enumerate(raw.steps):
        a = 20 * np.log10(np.abs(raw.get_trace("V(n)").get_wave(i)) / np.abs(raw.get_trace("V(n2)").get_wave(i)))
        att150 = -float(np.interp(150.0, f, a))
        loss = {f"{fc:.3f}": round(-float(np.interp(fc, f, a)), 2) for fc in T1_CARRIERS}
        rows.append(dict(L_nH=round(sp["lt"] * 1e9, 1), C_pF=round(1e12 / ((2 * math.pi * 150e6) ** 2 * sp["lt"]), 3),
                         Q=sp["qt"], att_150_dB=round(att150, 2), carrier_loss_dB=loss,
                         relative_suppression_dB={k: round(att150 - v, 2) for k, v in loss.items()}))
        curves.append((sp["lt"], sp["qt"], f, a))
    return dict(rows=rows, f=f, curves=curves)


def t1_verdict(t1: dict, need_target: float, need_legal: float) -> dict:
    top = f"{T1_CARRIERS[-1]:.3f}"
    best = max(r["relative_suppression_dB"][top] for r in t1["rows"])
    legal = [r for r in t1["rows"] if r["relative_suppression_dB"][top] >= need_legal]
    cheapest = min(legal, key=lambda r: r["carrier_loss_dB"][top]) if legal else None
    return dict(
        need_relative_dB_for_60dBc=round(need_target, 1), need_relative_dB_for_25uW=round(need_legal, 1),
        best_relative_suppression_at_147990_dB=round(best, 2),
        meets_60dBc_at_147990_any_size=bool(best >= need_target),
        cheapest_for_25uW_at_147990=cheapest,
        verdict=("WITHDRAWN as the fallback: no size reaches the 60 dBc suppression at 147.990 MHz "
                 f"(best {best:.1f} dB against {need_target:.1f} dB), and the 25 uW suppression costs at least "
                 f"{cheapest['carrier_loss_dB'][top] if cheapest else float('nan'):.1f} dB of carrier at 147.990 MHz "
                 "that neither drive chain has to spare (WP-PDR-21 runs d2 and p1/p2)") if best < need_target else
                "feasible for 60 dBc at 147.990 MHz: carry its carrier loss into WP-PDR-21")


def fig_t1(t1: dict, v: dict, out: Path):
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.2))
    ax = axes[0]
    top = f"{T1_CARRIERS[-1]:.3f}"
    for q, c in ((60, "#eb6834"), (100, "#2a78d6")):
        sel = sorted([r for r in t1["rows"] if r["Q"] == q], key=lambda r: r["L_nH"])
        x = [r["carrier_loss_dB"][top] for r in sel]
        y = [r["relative_suppression_dB"][top] for r in sel]
        ax.plot(x, y, "o-", color=c, lw=1.8, label=f"inductor Q {q}, carrier 147.990 MHz")
        for r, xi, yi in zip(sel, x, y):
            ax.annotate(f"{r['L_nH']:g} nH", (xi, yi), xytext=(4, -10 if q == 60 else 4), textcoords="offset points", fontsize=6.5, color=c)
        x2 = [r["carrier_loss_dB"]["144.050"] for r in sel]
        y2 = [r["relative_suppression_dB"]["144.050"] for r in sel]
        ax.plot(x2, y2, "o:", color=c, lw=1.0, alpha=0.7, label=f"inductor Q {q}, carrier 144.050 MHz")
    ax.axhline(v["need_relative_dB_for_60dBc"], color="#52514e", lw=1.4, ls="--")
    ax.axhline(v["need_relative_dB_for_25uW"], color="#0b0b0b", lw=1.4)
    ax.text(0.3, v["need_relative_dB_for_60dBc"] + 0.2, f"needed for 60 dBc: {v['need_relative_dB_for_60dBc']:.1f} dB", fontsize=8, color="#52514e", va="bottom")
    ax.text(12, v["need_relative_dB_for_25uW"] + 0.2, f"needed for 25 uW: {v['need_relative_dB_for_25uW']:.1f} dB", fontsize=8, va="bottom")
    ax.set_xlabel("carrier loss of the trap (dB)", fontsize=9)
    ax.set_ylabel("150 MHz suppression relative to the carrier (dB)", fontsize=9)
    ax.set_title("T1 trade: relative suppression against carrier loss (LTspice)\n"
                 + ("T1 WITHDRAWN as the fallback" if not v["meets_60dBc_at_147990_any_size"] else "T1 feasible"), fontsize=9.5, loc="left")
    ax.legend(fontsize=7, frameon=False, loc="lower right")
    ax = axes[1]
    for lt, q, f, a in t1["curves"]:
        if q != 100:
            continue
        ax.plot(f, a, lw=1.3, label=f"{lt * 1e9:g} nH, Q 100")
    ax.axvspan(144.0, 148.0, color="#f1f0ec", zorder=0)
    ax.axvline(150.0, color="#e34948", lw=1, ls=":")
    ax.text(150.1, -38, "150.000 MHz", fontsize=7.5, color="#e34948")
    ax.set_xlabel("frequency (MHz); shaded: 144 to 148 MHz", fontsize=9)
    ax.set_ylabel("transfer against the node with no trap (dB)", fontsize=9)
    ax.set_ylim(-40, 1)
    ax.set_title("Series-LC trap at 150 MHz on a 50 ohm node, Q 100", fontsize=9.5, loc="left")
    ax.legend(fontsize=7, frameon=False, loc="lower left")
    for a in axes:
        a.grid(color="#e4e3df", lw=0.6)
        for sp in ("top", "right"):
            a.spines[sp].set_visible(False)
        a.tick_params(labelsize=8)
    fig.tight_layout()
    fig.savefig(out, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------- main
def residual_view(x: Line) -> dict:
    return dict(f=x.f, source=x.source, ant_lo=round(x.ant_lo, 1), ant_hi=round(x.ant_hi, 1),
                gva_lo=round(x.gva_lo, 1), gva_hi=round(x.gva_hi, 1), over_60dBc_dB=round(x.ant_hi - LIM_TARGET_ANT, 1),
                over_25uW=bool(x.ant_hi > LIM_LEGAL_ANT), over_25uW_dB=round(x.ant_hi - LIM_LEGAL_ANT, 1),
                credited=x.credited, named_not_credited=x.named, change=x.change, contributors=x.contributors)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-id", required=True)
    args = ap.parse_args()
    rd = BLOCK / "results" / args.run_id
    need = {n: rd / f"{n}.raw" for n in ("tx_spur_filters", "tx_spur_c7_tap", "tx_spur_c7_iso", "tx_spur_trap")}
    for n, path in need.items():
        if not path.exists():
            print(f"missing {path}: run tools/ltspice-batch.sh -o {rd} -b hardware/sim/freq/{n}.cir first")
            return 2
    flt = Filters(need["tx_spur_filters"])

    # C7: valid clock and the isolation it buys (finding-2); the design value must be valid at every corner
    tap = c7_tap(need["tx_spur_c7_tap"])
    iso = c7_iso(need["tx_spur_c7_iso"])
    if not tap["per_rser"][RSER_C7]["valid"]:
        print(f"C7 design value {RSER_C7:g} ohm does not give a valid clock at every corner: {tap['per_rser'][RSER_C7]}")
        return 2
    C7["rser"] = RSER_C7
    C7["iso_db"] = iso["per_rser"][RSER_C7]["min_db"]

    # analytic cross-check of the ideal LTspice filters
    f = flt.f_mhz
    check = {
        "drive_max_diff_db": float(np.max(np.abs(flt.drive_ideal - (analytic_butter3(f, 170.0) - 18.0)))),
        "out_max_diff_db": float(np.max(np.abs(flt.out_ideal - analytic_cheby(f, 165.0)))),
        "out_ideal_288_db": float(np.interp(288, f, flt.out_ideal)),
        "out_ideal_432_db": float(np.interp(432, f, flt.out_ideal)),
        "out_q60_288_db": flt.ho(288), "out_q60_432_db": flt.ho(432),
        "out_q60_passband_loss_146_db": flt.ho(146.0),
        "drive_q60_146_db": flt.hd(146.0),
    }
    check["pass"] = check["drive_max_diff_db"] < 0.05 and check["out_max_diff_db"] < 0.05

    res = {}
    for pid in PLANS:
        for fin in FINALISTS:
            for fc in CARRIERS:
                res[(pid, fin, fc)] = run_case(pid, fin, fc, flt)
    sweep, counts, counts_legal = {}, {}, {}
    for pid in PLANS:
        for fin in FINALISTS:
            cases = [run_case(pid, fin, float(fc), flt) for fc in SWEEP]
            sweep[(pid, fin)] = [max(x.ant_hi for x in c) for c in cases]
            counts[(pid, fin)] = [sum(1 for x in c if x.ant_hi > LIM_TARGET_ANT) for c in cases]
            counts_legal[(pid, fin)] = [sum(1 for x in c if x.ant_hi > LIM_LEGAL_ANT) for c in cases]

    # outputs
    with open(rd / "lines.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["plan", "finalist", "carrier_MHz", "f_MHz", "family", "source", "injection", "mirror",
                    "ant_lo_dBm", "ant_hi_dBm", "gva_ref_lo_dBm", "gva_ref_hi_dBm", "verdict_60dBc", "verdict_25uW",
                    "residual_60dBc", "residual_25uW", "basis", "change_named", "credited_in_numbers", "named_not_credited",
                    "contributors"])
        for (pid, fin, fc), lines in res.items():
            for x in sorted(lines, key=lambda x: x.f):
                w.writerow([pid, fin, fc, f"{x.f:.4f}", x.family, x.source, x.inj, x.mirror, f"{x.ant_lo:.1f}",
                            f"{x.ant_hi:.1f}", f"{x.gva_lo:.1f}", f"{x.gva_hi:.1f}", x.verdict_target, x.verdict_legal,
                            x.ant_hi > LIM_TARGET_ANT, x.ant_hi > LIM_LEGAL_ANT, x.basis, x.change,
                            " + ".join(x.credited), " + ".join(x.named), " | ".join(x.contributors)])

    summary = {}
    for (pid, fin, fc), lines in res.items():
        key = f"{pid}/{fin}/{fc:.3f}"
        worst = max(lines, key=lambda x: x.ant_hi)
        resid = sorted([x for x in lines if x.ant_hi > LIM_TARGET_ANT], key=lambda x: -x.ant_hi)
        summary[key] = dict(
            lines=len(lines),
            target_pass=sum(1 for x in lines if x.verdict_target == "pass"),
            target_not_shown=sum(1 for x in lines if x.verdict_target == "not shown"),
            target_fail=sum(1 for x in lines if x.verdict_target == "fail"),
            legal_not_shown=sum(1 for x in lines if x.verdict_legal == "not shown"),
            legal_fail=sum(1 for x in lines if x.verdict_legal == "fail"),
            worst=dict(f=worst.f, source=worst.source, ant_lo=round(worst.ant_lo, 1), ant_hi=round(worst.ant_hi, 1),
                       gva_hi=round(worst.gva_hi, 1)),
            residual_60dBc=len(resid),
            residual_25uW=sum(1 for x in resid if x.ant_hi > LIM_LEGAL_ANT),
            residual_lines=[residual_view(x) for x in resid],
            residual_without_any_named_change=sum(1 for x in resid if not x.credited and not x.named),
        )

    crit = {}
    for fin in FINALISTS:
        c = {}
        for pid in PLANS:
            cs = [summary[f"{pid}/{fin}/{fc:.3f}"] for fc in CARRIERS]
            n_res = max(x["residual_60dBc"] for x in cs)
            n_leg = max(x["residual_25uW"] for x in cs)
            unnamed = sum(x["residual_without_any_named_change"] for x in cs)
            if pid in ("P", "PB"):
                if n_res == 0:
                    numbers = "PASS (every line under the 60 dBc target at the high estimate)"
                else:
                    numbers = (f"RESIDUAL: up to {n_res} lines over the 60 dBc target at the three carriers "
                               f"({min(counts[(pid, fin)])} to {max(counts[(pid, fin)])} over the band), "
                               f"{n_leg} over 25 uW at the high estimate")
                wording = ("not met: a residual line has no change named" if unnamed else
                           ("met in the numbers" if n_res == 0 else
                            f"met by wording only: {n_res} residual lines not shown, {n_leg} over 25 uW, closing at the bench"))
            else:
                numbers = f"as written: up to {n_res} lines over 60 dBc, {n_leg} over 25 uW (no change applied)"
                wording = "not met as written"
            c[pid] = dict(
                ts012_criterion_numbers=numbers,
                ts012_criterion_wording=wording,
                residual_60dBc_max_over_carriers=n_res,
                residual_25uW_max_over_carriers=n_leg,
                residual_60dBc_min_max_over_band=[min(counts[(pid, fin)]), max(counts[(pid, fin)])],
                residual_25uW_min_max_over_band=[min(counts_legal[(pid, fin)]), max(counts_legal[(pid, fin)])],
                worst_line_ant_hi_dBm_over_band=round(max(sweep[(pid, fin)]), 1),
                worst_line_gva_ref_hi_dBm_over_band=round(max(sweep[(pid, fin)]) - G_REF, 1),
                all_lines_under_60dBc_at_high_estimate=bool(max(sweep[(pid, fin)]) <= LIM_TARGET_ANT),
                all_lines_under_25uW_at_high_estimate=bool(max(sweep[(pid, fin)]) <= LIM_LEGAL_ANT),
                residual_without_any_named_change=unnamed,
            )
        crit[fin] = c

    # T1: the suppression the residual 150.000 MHz line needs, from plan PB (the recommended drive chain)
    l150 = [x for fin in FINALISTS for fc in CARRIERS for x in res[("PB", fin, fc)] if abs(x.f - 150.0) < 0.001]
    hi150 = max(x.ant_hi for x in l150)
    t1 = t1_trap(need["tx_spur_trap"])
    t1v = t1_verdict(t1, hi150 - LIM_TARGET_ANT, hi150 - LIM_LEGAL_ANT)
    t1v["line_150_ant_hi_dBm_PB"] = round(hi150, 1)

    # exit status: 0 only if plans P and PB meet both limits in the numbers for both finalists
    n_resid = sum(crit[fin][pid]["residual_60dBc_max_over_carriers"] for fin in FINALISTS for pid in ("P", "PB"))
    n_unnamed = sum(crit[fin][pid]["residual_without_any_named_change"] for fin in FINALISTS for pid in ("P", "PB"))
    if not check["pass"]:
        overall, code = "FAIL (filter cross-check)", 1
    elif n_unnamed:
        overall, code = "FAIL (a residual line has no named change)", 3
    elif n_resid:
        overall, code = "RESIDUAL (TS-012 7.3 met by wording only; residual lines close at the bench)", 1
    else:
        overall, code = "PASS", 0

    result = dict(
        run_id=args.run_id,
        analysis="docs/design/analysis/spurs-ts012.md",
        script="hardware/sim/freq/tx_spur_plan.py",
        decks=["hardware/sim/freq/tx_spur_filters.cir", "hardware/sim/freq/tx_spur_bpf_tol.cir",
               "hardware/sim/freq/tx_spur_c7_tap.cir", "hardware/sim/freq/tx_spur_c7_iso.cir", "hardware/sim/freq/tx_spur_trap.cir"],
        confidence="ESTIMATE (Low): source levels and coupling are engineering estimates pending layout; filters, the C7 tap and T1 from LTspice (ideal or estimated parts)",
        exit_status={"0": "P and PB meet 60 dBc and 25 uW in the numbers", "1": "residual lines (met by wording only) or filter check failed",
                     "2": "missing input or invalid C7 design value", "3": "a residual line has no named change"},
        limits=dict(ant_legal_dBm=LIM_LEGAL_ANT, ant_target_dBm=LIM_TARGET_ANT, gva_ref_gain_dB=G_REF,
                    gva_legal_dBm=LIM_LEGAL_GVA, gva_target_dBm=LIM_TARGET_GVA),
        filter_check=check,
        g_eff_dB={fin: [round(v, 1) for v in g_eff(fin, flt, 146.0)] for fin in FINALISTS},
        plans={pid: v["label"] for pid, v in PLANS.items()},
        c7=dict(source="Nexperia 74LVC1G80 Rev. 17 (12 Nov 2024): Table 7 VIH 2.0 V, VIL 0.8 V (VCC 2.7 to 3.6 V), CI 5 pF typ; "
                       "Table 8 tW 2.5 ns min, fmax 160 MHz min (VCC 3.0 to 3.6 V, -40 to +85 C); Table 6 input transition 10 ns/V max",
                criterion=f"at every corner the CP pin goes below VIL - {VCLK_MARGIN} V and above VIH + {VCLK_MARGIN} V; tW >= 2.5 ns at VM 1.5 V; transition <= 10 ns/V",
                fmax_check=f"first flip-flop clocked at fc <= 148 MHz against fmax 160 MHz min: margin {160 - 148} MHz (8 %)",
                design_rser_ohm=RSER_C7, credited_isolation_dB=C7["iso_db"],
                rser_max_valid_ohm=tap["rser_max_valid"], clk1_pin_vpp_range=tap["clk_vpp_range"],
                per_rser={f"{r:g}": {**tap["per_rser"][r], **iso["per_rser"][r]} for r in TAP_RSER},
                revision0_330ohm="INVALID CLOCK: worst margin %+.2f V; LTspice isolation %.1f dB against the 23 dB claimed" %
                                 (tap["per_rser"][330.0]["worst_margin_V"], iso["per_rser"][330.0]["min_db"]),
                corners=[{k: v for k, v in x.items() if k not in ("t", "v")} for x in tap["rows"]]),
        t1_trap=dict(**t1v, rows=t1["rows"]),
        adr031_rx_check_clk_sys_96=rx_check_clk_sys(96.0),
        criterion=crit,
        cases=summary,
        overall=overall,
    )

    tol = c10_tolerance(rd / "tx_spur_bpf_tol.raw", flt)
    if tol is not None:
        result["c10_tolerance"] = {k: v for k, v in tol.items() if k != "curves"}
        result["c10_tolerance"]["pass"] = result["c10_tolerance"].pop("pass_")
        fig_c10(tol, rd / "c10-tolerance.png")
    (rd / "results.json").write_text(json.dumps(result, indent=1))
    fig_filters(flt, rd / "filters.png", check)
    for fin in FINALISTS:
        fig_spectrum(res, rd / f"spectrum-gva-{fin}-144.050.png", fin, 144.050)
    fig_antenna(res, flt, rd / "antenna-P-PB-144.050.png", 144.050)
    fig_antenna(res, flt, rd / "antenna-P-PB-147.950.png", 147.950)
    fig_sweep(sweep, counts, counts_legal, rd / "worst-line-vs-carrier.png")
    fig_c7(tap, iso, rd / "c7-prescaler-tap.png")
    fig_t1(t1, t1v, rd / "t1-trap.png")

    print(json.dumps(dict(overall=overall, criterion=crit, c7={k: result["c7"][k] for k in ("design_rser_ohm", "credited_isolation_dB", "rser_max_valid_ohm", "revision0_330ohm")},
                          t1={k: v for k, v in t1v.items() if k != "cheapest_for_25uW_at_147990"}), indent=1))
    for pid in ("P", "PB"):
        for fin in FINALISTS:
            for fc in CARRIERS:
                s_ = summary[f"{pid}/{fin}/{fc:.3f}"]
                print(f"{pid} {fin} {fc:.3f}: residual {s_['residual_60dBc']} over 60 dBc, {s_['residual_25uW']} over 25 uW: " +
                      "; ".join(f"{x['f']:.3f} {x['ant_hi']:+.1f} dBm ({x['source'][:50]})" for x in s_["residual_lines"]))
    print(f"exit status {code}: {overall}")
    return code


if __name__ == "__main__":
    sys.exit(main())
