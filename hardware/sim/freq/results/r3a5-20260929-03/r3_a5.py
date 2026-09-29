#!/usr/bin/env python3
"""Route R3 frequency-verification budget for A5: Si5351A relock, TCXO ratio freshness, receive-only buffer.

Product: docs/design/analysis/frequency-budget.md revision 4, sections 3.4 and 3.5 and the A5 rows of section 3.1
(WP-PDR-20a, PDR work plan revision 6 section 3.0 row 20). It answers the two TS-012 section 10 revisit
conditions of revision 6 (the Si5351A PLL relock time against its 1 ms allocation; the XOSC/TCXO ratio's
freshness over a long over against its 1 ppm allocation) and re-states the route R3 budget of D-17 for A5.

Revision 3 (fixes the Major findings of INSP-056 iteration 3 re-issue 1 and INSP-111 iteration 2):
  - INSP-056 finding-11: the ratio drift carries the TCXO's own terms (temperature change on the
    +/-0.5 ppm band of the TG2520SMN brief sheet, no slope given; load and supply step between the
    stage-on refresh and the stage-off transmission from its fo-Load and fo-VCC rows); the interval-12
    allocation, A_kd, the interval-13 allocation and the margins are re-derived (FR-T, FR-2, FR-4 to FR-6).
  - INSP-056 finding-12: the FC0 interval times are 2^n x 1 us (4.096, 8.192, 32.768 ms), not the rounded
    Table 541 values; L_max, RL-5, RL-6, the fallback gap, FR-2r, B-15 and B-19 follow.
  - INSP-111 finding-7: a count bounds only the mean frequency over its own interval; a linear PLL tail can
    pass it (ST-1). The settle residual at the ramp is a named allocation carried into the A5 band-edge
    guard (G-1 to G-7) and closed by the time-resolved measurement M-1(c) (ST-3).

Revision 4 (fixes the Major finding-13 of INSP-111 iteration 3; frequency-budget.md revision 4, section 3.5):
  - the A5 reference budget with the TG2520SMN brief-sheet terms (tolerance after reflow, fo-TC band, first-year
    aging, fo-Load, fo-VCC): identity 1 (REQ-SYS-010 after calibration) and identity 2 (guard-protecting case) of
    section 3.2, and the A5 band-edge guard with a wrong calibration constant, on two readings of the fo-TC band
    (referred to +25 C; 1.0 ppm peak to peak, which governs) (KA-R5, KA-R6, RB-0 to RB-8);
  - the three options named for the owner's decision, as arithmetic only: (a) a TCXO that meets R-M3, (b) a guard
    CR, (c) a software integrity control on the calibration constant (RB-6a to RB-6c). The script does not choose.
  Every revision 3 case is unchanged.

Run from the repository root:

    .venv/bin/python hardware/sim/freq/r3_a5.py --run-id r3a5-20260929-03

Writes results.json, checker-output.txt, the figures and a copy of this script to
hardware/sim/freq/results/<run-id>/. Exit status 0 when every PASS/FAIL assertion holds, 1 otherwise.
INFO lines carry results that are not pass/fail (open items, sourced values that do not decide).

Tool status (05 section 9.1): class B evidence-generating script with no TV record; developer evidence
(CK-ANA-C2). Exact rational arithmetic (fractions) for the budget; numpy for the thermal transients
(the reviewed WP-PDR-28a thermal model, imported unchanged) and the crystal slope envelope; matplotlib
only draws. Every input constant carries its source and class next to it:
  D  datasheet or application note read in this invocation (Skyworks, see SOURCES)
  N  a value of the reviewed frequency-budget.md revision 1 (INSP-056 APPROVED), imported from freq_budget.py
  R  a requirement (TBR) or a TS-012 decision
  A  an allocation of this note (a requirement on a later design or measurement)
  E  an engineering estimate (Low confidence unless stated)
"""
from __future__ import annotations

import argparse
import json
import math
import shutil
import sys
from fractions import Fraction as F
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT / "hardware/sim/thermal"))
import freq_budget as fb  # noqa: E402  (reviewed checker, INSP-056; imported, not modified)
import thermal_model as tm  # noqa: E402  (reviewed thermal model, WP-PDR-28a; imported, not modified)

MS = F(1, 1000)
US = F(1, 10**6)

# ----------------------------------------------------------------------------------------------
# SOURCES read in this invocation (2026-09-29, web-fetch tool; the tool cached each PDF, the author
# converted it to text with pdftotext in the session scratchpad; no file was added to the repository)
# ----------------------------------------------------------------------------------------------
SOURCES = {
    "DS": "Skyworks Si5351A/B/C-B data sheet, Rev. 1.3, August 27, 2021, "
          "https://www.skyworksinc.com/-/media/Skyworks/SL/documents/public/data-sheets/Si5351-B.pdf "
          "(PDF SHA-256 f3bc5285fccafa3fcd06e9a7fa6abb67fb43e8c23f6147b14caecc9a4851101f)",
    "AN619": "Skyworks AN619 'Manually Generating an Si5351 Register Map for 10-MSOP and 20-QFN Devices', "
             "Rev. 0.8, September 23, 2021, "
             "https://www.skyworksinc.com/-/media/Skyworks/SL/documents/public/application-notes/AN619.pdf "
             "(PDF SHA-256 0135b3a37195189e38cbd58ca504460814c691eeb1fdbe275806cfcd4783f36b)",
    # Revision 3 (INSP-056 finding-11): read 2026-09-29 through the web-fetch tool, converted with pdftotext in the
    # session scratchpad; no file added to the repository.
    "TCXO": "Seiko Epson 'TCXO / VC-TCXO TG2016SMN / TG2520SMN' brief sheet (2 pages, (c) Seiko Epson Corporation 2025, "
            "PDF created 2025-06-25), https://download.epsondevice.com/td/pdf/brief/TG2520SMN_en.pdf "
            "(PDF SHA-256 df16ac04cdec1db7eedcb21ef19c0a87f17dcf061fe55e1aafa053037d846612)",
}

# ----------------------------------------------------------------------------------------------
# INPUTS
# ----------------------------------------------------------------------------------------------
# Si5351A timing (D). DS Table 5 "AC Characteristics" (page 9), VDD 2.5 or 3.3 V +/-10 %, TA -40 to 85 C:
T_RDY_MAX = 10 * MS        # D: Power-up Time TRDY, "From VDD = VDDmin to valid output clock, CL = 5 pF, fCLKn > 1 MHz",
T_RDY_TYP = 2 * MS         #    typ 2, max 10 ms. Includes NVM copy, system initialization and PLL acquisition from power-up.
T_FREQ_MAX = 10 * US       # D: Output Frequency Transition Time TFREQ, "fCLKn > 1 MHz", max 10 us. The table does not say
                           #    whether it covers a PLL feedback-divider (MSNA) change or only a MultiSynth change.
T_OE_MAX = 10 * US         # D: Output Enable Time TOE, "From OEB pulled low to valid clock output", max 10 us.
# The DS and AN619 give no PLL lock time and no relock time for a feedback-divider change (searched: "lock",
# "settl", "acquisition"). AN619 Register 0 bit 5 LOL_A "PLL A Loss Of Lock Status ... 0: PLL A is operating
# normally. 1: PLL A is unlocked" (page 13); Register 177 PLLA_RST "Writing a 1 to this bit will reset PLLA.
# This is a self clearing bit"; DS Figure 10 (page 21) applies "PLLA and PLLB soft reset, Reg. 177 = 0xAC" after
# a configuration write. DS section 5: I2C "Standard-Mode (100 kbps) or Fast-Mode (400 kbps) and supports burst
# data transfer with auto address increments".
F_SCL_FAST = 400_000       # D: DS section 5 and Table 9, Fast-Mode 400 kbps
F_SCL_STD = 100_000        # D: Standard-Mode 100 kbps
F_SCL_ADR031 = 256_000     # N: spurs-ts012.md section 6 "I2C": with the ADR-031 counts SCL becomes about 256 kHz at
                           #    clk_sys 96 MHz; the counts are re-derived for 96 MHz by WP-PDR-32

# The C6 changeover writes (spurs-ts012.md option C6, TS-012 section 7.3 revision 6 sequence), as I2C bursts.
# Register numbers from AN619 (Registers 3, 16 to 18, 26 to 33, 34 to 41, 177). Each write burst on the wire:
# START, address byte, register byte, n data bytes, STOP. Each byte is 9 SCL clocks (8 bits + ACK); START and STOP
# are counted as one SCL period each (conservative against the Fast-Mode setup and hold minima).
C6_WRITES = [
    ("MSNA P1..P3 (reg 26-33): PLL A from the RX LO multiplier to the carrier multiplier", 8),
    ("CLK0..CLK2 control (reg 16-18): CLK1 powered up, CLK0 and CLK2 powered down", 3),
    ("Output enable (reg 3): CLK1 enabled, CLK0 and CLK2 disabled", 1),
    ("MSNB P1..P3 (reg 34-41): PLL B parked on the PLL A multiplier (C6)", 8),
]
C6_RESET = ("PLL soft reset (reg 177), DS Figure 10 procedure", 1)
LOL_READ_BYTES = 4         # status read: address+W, register 0, repeated START, address+R, one data byte

# Key-down sequence (R: TS-012 section 7.3 revision 6; ADR-026 and the requirements below)
T_LEADIN = fb.T_LEADIN                 # R: REQ-SYS-161 lead-in <= 12 ms after the changeover (TBR)
T_REQ160 = 15 * MS                     # R: REQ-SYS-160 RF rise within 15 ms of contact closure (TBR)
T_FRONT = 3 * MS                       # R: TS-012 7.3: 1 ms sampling + 2 ms make filter before t0 (changeover)
T_RAMP_NOM = 10 * MS                   # R: TS-012 7.3 revision 6: ramp at t0 + 10 ms (relay operate 7 + bounce 0.5 + 2.5)
T_TXKEY = 8 * MS                       # R: TS-012 7.3 revision 6: TX_KEY at t0 + 8 ms; GVA-84+ powered and bias clamp
                                       #    released when TX_KEY, PA_EN and Q are all true (D-18 NAND)
G_PA_TO_RAMP = T_RAMP_NOM - T_TXKEY    # R: 2 ms from the drive power-up (max(TX_KEY, PA_EN)) to the ramp, as TS-012
T_RELOCK_ALLOC = 1 * MS                # R: TS-012 7.3 revision 6: 1 ms for "the writes and the PLL to settle"
T_REVISIT = T_RELOCK_ALLOC + 3 * MS    # R: TS-012 section 10: triggers if the relock exceeds 1 ms by more than 3 ms
T_SW = fb.T_SW                         # N: 2 ms software (lock-status read and compare), frequency-budget C-14
# Revision 3 (INSP-056 finding-12): the count lasts 2^interval x 0.98 us (RP2350 Table 582 FC0_INTERVAL, "0.98us *
# 2**interval, but let's call it 1us"). The time budget takes 2^interval x 1 us, which is longer than the 0.98 us value
# and so conservative for time: 4.096, 8.192 and 32.768 ms. (freq_budget.py keeps the rounded 4, 8 and 32 ms of Table
# 541 for sections 3.1 to 3.3; that is its lien finding-5, not re-opened here.)
FC0_TICK = US                          # D (N): 1 us, the upper value of the 0.98 us tick
T_FC0 = {iv: (2 ** iv) * FC0_TICK for iv in (12, 13, 15)}
L_MAX_STEP = F(1, 10) * MS             # the proposed L_max deadline is rounded down to 0.1 ms

# Route R3 budget (N unless marked)
TX_MAX = fb.TX_MAX
T_MEAS = fb.T_MEAS                     # N: measured threshold T = 5.0 kHz (SW-SAFE, WP-PDR-35)
L_154 = fb.L_154                       # R: REQ-SYS-154 10 kHz true-error limit
F_INJ = fb.F_INJ                       # R: TC-SYS-101 12 kHz injection
Q_TCXO_PPM = fb.FC0[15][1] / fb.TCXO_REF / fb.PPM   # N: 62.5 Hz at 25 MHz = 2.5 ppm ratio quantization
DRIFT_R1_ALLOC = fb.XOSC_DRIFT_R3      # N: 1 ppm XOSC drift allocation of revision 1 (TS-012 section 10 condition 2),
                                       #    used only for the known answer KA-R2

# TCXO terms of the ratio drift (revision 3, INSP-056 finding-11). Under R3 the carrier estimate is the GPIN0 count
# scaled by the last XOSC/TCXO ratio, so a healthy unit's estimate errs by [f_TCXO(now)/f_TCXO(refresh)] x
# [f_XOSC(refresh)/f_XOSC(now)] - 1: the TCXO's own change since the refresh counts as well as the XOSC's.
# D: TG2520SMN brief sheet, "Specifications (characteristics)" table (SOURCES["TCXO"]):
TCXO_TC_PPM = F("0.5")                 # D: fo-TC, version C, "+/-0.5 x 10-6 Max. / -40 C to +85 C". No slope is given.
TCXO_TEMP_PPM = 2 * TCXO_TC_PPM        #    Bound on the change over ANY temperature step: the band, 1.0 ppm peak to peak
TCXO_LOAD_COEF_PPM = F("0.1")          # D: fo-Load "+/-0.1 x 10-6 Max.", "10 kOhm // 10 pF +/- 10 %"
TCXO_VCC_COEF_PPM = F("0.1")           # D: fo-VCC "+/-0.1 x 10-6 Max.", "VCC +/- 5 %"
# A: the step between the stage-on refresh and the stage-off check. With the squaring stage on and off, and the
#    breakout in its receive and transmit clock states, the TCXO load stays inside 10 kOhm // 10 pF +/- 10 % and its
#    supply inside 3.3 V +/- 5 % (conditions on WP-PDR-20b, 37 and 38). Each state is then within the coefficient of
#    the nominal-condition frequency, so the step between two states is at most twice each coefficient.
TCXO_STEP_PPM = 2 * TCXO_LOAD_COEF_PPM + 2 * TCXO_VCC_COEF_PPM   # 0.4 ppm; confirmed by measurement M-2(b)
ALLOC_STEP = F(1, 2)                   # allocations are the bound rounded up to 0.5 ppm (revision 2 convention)

# A5 reference budget (revision 4, INSP-111 finding-13). D: the same TG2520SMN brief sheet table (SOURCES["TCXO"];
# re-read in the revision 4 invocation, PDF SHA-256 equal):
TG_TOL_PPM = F("1.5")                  # D: f_tol "+/-1.5 x 10-6 Max.", "After reflow, +25 C"
TG_AGE_PPM = F("0.5")                  # D: f_age "+/-0.5 x 10-6 Max.", "+25 C, First year", 24 MHz <= fo <= 40 MHz (25 MHz)
# fo-TC: the brief sheet does not state the reference temperature of the +/-0.5 ppm band. Two readings of the
# temperature term of the ABSOLUTE (uncalibrated) error, |f(T) - f(+25 C)|:
#   "ref25": the band is referred to the +25 C frequency, so |f(T) - f(25 C)| <= 0.5 ppm (the INSP-111 finding-13 figure);
#   "pp":    the band is a 1.0 ppm peak-to-peak window of unstated centre, so |f(T) - f(25 C)| <= 1.0 ppm. This is the
#            reading section 3.4.2 uses for a change between two temperatures; it governs (conservative, hazard side)
#            until the full datasheet (TS-007 value-of-information item 5) states the reference.
TC_ABS = {"ref25": TCXO_TC_PPM, "pp": TCXO_TEMP_PPM}
READING_GOV = "pp"
R_M3_PPM = fb.UNCAL_TOTAL_PPM          # N: TS-007 R-M3 acceptance test, uncalibrated total <= 1.5 ppm (section 3.2 allocation)
CAL_RANGE_TOL = TG_TOL_PPM             # smallest calibration range that corrects the +25 C tolerance of every unit
GUARD_STEP = F(100)                    # a guard CR value is the needed guard rounded up to 0.1 kHz

# Settle residual at the ramp (revision 3, INSP-111 finding-7)
T_REF_PERIOD = 1 / fb.TCXO_REF         # 40 ns at 25 MHz: the phase-detector period of PLL A
S_RAMP = F(5)                          # A: settle residual of the carrier at and after the ramp (t0 + 10 ms), Hz,
                                       #    carrier referred: a named term of the A5 band-edge guard (section 3.1),
                                       #    closed by the time-resolved measurement M-1(c)
M1C_WINDOW = 1 * MS                    # A: M-1(c) analysis window (one beat period at the 1 kHz beat)
M1C_BEAT = F(1000)                     # A: M-1(c) beat frequency between CLK1 and the steady reference, Hz
F_CLK1_M1 = F(18_250_000)              # M-1 sets CLK1 to VCO/48, about 17 to 18.5 MHz (section 3.4.1); mid value
M1C_RES_MAX = S_RAMP / 3               # A: M-1(c) resolution must be at most a third of the allocation

# Ratio freshness (A and E)
T_OVER_MAX = F(180)                    # R: REQ-SYS-180 ends RF at 150 to 180 s (TBR) of continuous transmit and holds
                                       #    it off until receive resumes: no RF, so no check, later than 180 s into an over
T_REFRESH = F(1)                       # N: ratio refreshed at least once a second in receive (frequency-budget 3.3)
T_BUF_SETTLE = 50 * MS                 # A: TCXO squaring stage settle after power-up (bias network), before the first
                                       #    interval-15 count after an over; covers a 10 ms coupling time constant x 5.
                                       #    A requirement on the stage that answers INSP-110 finding-25 (TS-012 rev 8
                                       #    section 8.1 note 3), whose valid-clock run is requested of WP-PDR-20b
PUSH_PPM = F(2, 10)                    # A: XOSC supply and load pushing at the changeover (Pico 2 3.3 V rail step),
                                       #    to be confirmed by the dev-board measurement M-2
DP_PICO = 0.03                         # E: change of the Pico 2 board's own dissipation between receive and transmit, W
RTH_PICO = 47.0                        # E: Pico 2 board to main-bay air, K/W (51 x 21 mm, both faces, h about 10 W/m2K)
TAU_PICO_MIN = 30.0                    # E: shortest Pico 2 board time constant considered, s (C about 2.7 J/K x 47 K/W
                                       #    gives about 127 s; 30 s is taken for the rate, conservative)
# XOSC crystal: RP2350 datasheet Table 596 (ABM8-272-T3) as read in frequency-budget.md revision 1 (N):
XO_STAB_PPM = float(fb.XOSC_STAB)      # N: +/-30 ppm stability over -40 to +85 C (referred to 25 C)
XO_T_RANGE = (-40.0, 85.0)             # N: the Table 596 stability range
# AT-cut frequency-temperature model (E, Low; not in the corpus): df/f = a1 (T - Ti) + a3 (T - Ti)^3 about the
# inflection Ti (the quadratic term is zero about the inflection by construction). The third-order coefficient of
# AT-cut quartz is about 1.1e-4 ppm/K^3 (Bechmann's coefficients, as summarized in the standard crystal
# literature); the range below and Ti 20 to 35 C are swept to cover the literature spread. a1 (set by the cut
# angle) is not assumed: every a1 that keeps the curve inside the Table 596 band is admitted.
A3_RANGE = (0.8e-4, 1.3e-4)
TI_RANGE = (20.0, 35.0)
T_XO_OPER = (-10.0, 65.0)              # E: crystal temperature in service: -10 C cold soak (REQ-SYS-010 span) to the
                                       #    main-bay long-session value 57.8 C plus its band and the local rise (thermal note)

# Receive-only buffer lines (the squared 25 MHz is counted only in receive)
RX_RANGE = (F("144.010") * fb.MHz, F("147.999") * fb.MHz)  # R: REQ-SYS-034 receive range
F_IF = 8 * fb.MHz                      # R: TS-012 D-15, IF 8 MHz
IF_HALF = 5 * fb.kHz                   # E: IF window half-width considered (the CW crystal filter is far narrower)
TCXO_TOL_PPM = fb.REF_CEIL_PPM         # N: TCXO-derived line tolerance 2.5 ppm (clock-plan.md section 1)

LAYOUTS = ("A5-DC", "A5-R4")           # the two A5 layouts of the thermal note (A5-DC carries the D-1 to D-5 items)
AMBIENTS = (-10.0, 25.0, 45.0)         # C: REQ-SYS-010 span ends and room
SENSOR_PARAMS = ("ntc_frac_a5", "ntc_frac_a4", "tau_ntc_a5", "tau_ntc_a4", "inh_hyst")


def ceil1(x) -> float:
    return math.ceil(float(x) * 10) / 10


def floor1(x) -> float:
    return math.floor(float(x) * 10) / 10


def ceil3(x) -> float:
    return math.ceil(float(x) * 1000) / 1000


def floor3(x) -> float:
    return math.floor(float(x) * 1000) / 1000


# ----------------------------------------------------------------------------------------------
# 1. Relock: I2C time, sequence limits, sourced bounds
# ----------------------------------------------------------------------------------------------
def i2c_burst_time(n_data: int, f_scl: int, read: bool = False) -> F:
    if read:
        clocks = 9 * n_data + 3      # START, repeated START, STOP
    else:
        clocks = 9 * (2 + n_data) + 2
    return F(clocks, f_scl)


def c6_write_time(f_scl: int = F_SCL_FAST, reset: bool = False) -> F:
    t = sum(i2c_burst_time(n, f_scl) for _, n in C6_WRITES)
    if reset:
        t += i2c_burst_time(C6_RESET[1], f_scl)
    return t


def lol_read_time(f_scl: int = F_SCL_FAST) -> F:
    return i2c_burst_time(LOL_READ_BYTES, f_scl, read=True)


def l_max(interval: int, ramp: F, g: F = G_PA_TO_RAMP) -> F:
    """Largest writes-plus-settle time L (from t0) that keeps PA_EN at or before ramp - g:
    t0 + L + interval + T_SW <= ramp - g, with the ramp inside REQ-SYS-161 and REQ-SYS-160."""
    return ramp - g - T_FC0[interval] - T_SW


def ramp_limit() -> F:
    return min(T_LEADIN, T_REQ160 - T_FRONT)


def floor_step(x: F, step: F) -> F:
    return F(math.floor(x / step)) * step


def ceil_step(x, step: F) -> F:
    return F(math.ceil(F(x) / step)) * step


def edge_margins_a5(offset: F, s_ramp: F = None):
    """A5 band-edge margins (Hz): the section 3.1 method with the settle residual at the ramp added to the word term."""
    return fb.edge_margins(offset, e_word=fb.E_WORD + (S_RAMP if s_ramp is None else s_ramp))


def tail_count_shift(interval: int) -> F:
    """Largest shift of an interval count (Hz, carrier referred) that the linear tail of a charge-pump PLL can cause
    (INSP-111 finding-7): once the phase error at the phase detector is inside one reference period, the error a tail
    adds to a count is at most the phase error at the count's start minus that at its end, two reference periods."""
    return 2 * T_REF_PERIOD * TX_MAX / T_FC0[interval]


def slew_detect_time(interval: int) -> F:
    """Shortest full-error slewing transient (old LO frequency, one IF away) that moves the count by more than T."""
    return T_MEAS * T_FC0[interval] / F_IF


def m1c_resolution() -> F:
    """M-1(c) resolution, carrier referred: a D flip-flop samples CLK1 with the steady reference, so each beat edge is
    known to one reference period; one beat period per window, two edges."""
    t_q = 1 / F_CLK1_M1
    df_clk1 = M1C_BEAT ** 2 * t_q * F(1414, 1000)
    return df_clk1 / F_CLK1_M1 * TX_MAX


# A5 reference budget (revision 4, INSP-111 finding-13). All values in ppm of the carrier, reference terms only; the
# 5 Hz word term and the 5 Hz settle residual enter through the band-edge method (edge_margins_a5) or, for the
# identities, as the word term in ppm, as section 3.2 does.
def a5_uncal(reading: str) -> F:
    """TG2520SMN uncalibrated total: tolerance after reflow + temperature term + first-year aging + load + supply."""
    return TG_TOL_PPM + TC_ABS[reading] + TG_AGE_PPM + TCXO_LOAD_COEF_PPM + TCXO_VCC_COEF_PPM


def a5_cal_residual() -> F:
    """Error after a correct calibration, relative to the calibration condition: calibration uncertainty + the
    temperature change since calibration (the 1.0 ppm band, section 3.4.2) + first-year aging + the load and
    supply step between the calibration state and the use state (0.4 ppm, section 3.4.2)."""
    return fb.U_CAL_PPM + TCXO_TEMP_PPM + TG_AGE_PPM + TCXO_STEP_PPM


def identity2(uncal: F, cal_range: F) -> F:
    """Section 3.2 identity 2 (guard-protecting case): uncalibrated total + calibration range + word."""
    return uncal + cal_range + fb.e_word_ppm()


def guard_a5_min_margin(ref_ppm: F) -> F:
    """Smaller of the two A5 band-edge margins (Hz) at the -60 dB point with a reference error ref_ppm (section 3.1
    method, word 5 Hz + settle residual S_RAMP). Negative: the -60 dB point lies outside 144.000 to 148.000 MHz."""
    lo, hi = fb.edge_margins(fb.SB60_OFFSET, ppm=ref_ppm, e_word=fb.E_WORD + S_RAMP)
    return min(lo, hi)


def guard_needed(ref_ppm: F) -> F:
    """Smallest band-edge guard G (Hz) that keeps the A5 -60 dB point inside the band at both edges with ref_ppm:
    upper edge (148 MHz - G)(1 + e) + word + S_RAMP + offset <= 148 MHz; lower edge (144 MHz + G)(1 - e) - ... >= 144 MHz."""
    e = ref_ppm * fb.PPM
    k = fb.E_WORD + S_RAMP + fb.SB60_OFFSET
    return max((fb.BAND_HI * e + k) / (1 + e), (fb.BAND_LO * e + k) / (1 - e))


# ----------------------------------------------------------------------------------------------
# 2. XOSC slope envelope (AT-cut cubic inside the Table 596 band)
# ----------------------------------------------------------------------------------------------
def xo_slope_envelope(n_a3=6, n_ti=7, a1_step=0.002):
    T_band = np.linspace(*XO_T_RANGE, 501)
    T_op = np.linspace(*T_XO_OPER, 301)
    s_max, arg = 0.0, None
    env_hi = np.full_like(T_op, -np.inf)
    env_lo = np.full_like(T_op, np.inf)
    n_adm = 0
    a1_grid = np.arange(-2.0, 1.0 + a1_step / 2, a1_step)
    for a3 in np.linspace(*A3_RANGE, n_a3):
        for ti in np.linspace(*TI_RANGE, n_ti):
            xb = T_band - ti
            x25 = 25.0 - ti
            f = a1_grid[:, None] * xb[None, :] + a3 * xb[None, :] ** 3
            f25 = a1_grid * x25 + a3 * x25 ** 3
            dev = np.max(np.abs(f - f25[:, None]), axis=1)
            ok = dev <= XO_STAB_PPM
            for a1 in a1_grid[ok]:
                n_adm += 1
                s = a1 + 3 * a3 * (T_op - ti) ** 2
                env_hi = np.maximum(env_hi, s)
                env_lo = np.minimum(env_lo, s)
                sm = float(np.max(np.abs(s)))
                if sm > s_max:
                    s_max, arg = sm, dict(a1=float(a1), a3=float(a3), ti=float(ti),
                                          t_at=float(T_op[int(np.argmax(np.abs(s)))]))
    return dict(s_max=s_max, arg=arg, n_admissible=n_adm, T=T_op, env_hi=env_hi, env_lo=env_lo)


# ----------------------------------------------------------------------------------------------
# 3. Main-bay temperature change over a window (thermal model, nominal and one-at-a-time band)
# ----------------------------------------------------------------------------------------------
def bay_change(L: str, t_amb: float, window: float, v: dict | None = None, dt: float = 1.0):
    """Heating: from the receive steady state (key 0), key held 1 for `window` (continuous transmit, the upper
    bound on heating). Cooling: from the continuous steady state (key 1), key 0 for `window`. Returns the rise,
    the fall and the largest |dT/dt| of the MAIN node, with the traces."""
    net = tm.build(L, t_amb, v)
    im = net.names.index("MAIN")
    t_h, x_h = net.transient(window, dt, lambda t: 1.0, x0=net.steady(0.0))
    t_c, x_c = net.transient(window, dt, lambda t: 0.0, x0=net.steady(1.0))
    yh, yc = x_h[:, im], x_c[:, im]
    rate = max(float(np.max(np.abs(np.diff(yh) / np.diff(t_h)))), float(np.max(np.abs(np.diff(yc) / np.diff(t_c)))))
    return dict(rise=float(yh[-1] - yh[0]), fall=float(yc[0] - yc[-1]), rate=rate,
                trace_h=(t_h, yh - yh[0]), trace_c=(t_c, yc[0] - yc))


def swept_params():
    return [k for k, p in tm.P.items() if p.low != p.high and p.cls != "R" and k not in SENSOR_PARAMS]


def bay_band(window: float):
    """Worst nominal case over layouts and ambients, and the RSS of the one-at-a-time upward swings of every ranged
    thermal input (the thermal note's tornado method), for the change over `window` and for the rate."""
    base_v = tm.vals()
    cases = {}
    for L in LAYOUTS:
        for ta in AMBIENTS:
            cases[(L, ta)] = bay_change(L, ta, window, base_v)
    worst_key = max(cases, key=lambda k: max(cases[k]["rise"], cases[k]["fall"]))
    rate_key = max(cases, key=lambda k: cases[k]["rate"])
    base = cases[worst_key]
    base_dT = max(base["rise"], base["fall"])
    rows, up2_dT, up2_rate = [], 0.0, 0.0
    L, ta = worst_key
    Lr, tar = rate_key
    base_rate = cases[rate_key]["rate"]
    for p in swept_params():
        prm = tm.P[p]
        outs = []
        for val in (prm.low, prm.high):
            v = dict(base_v, **{p: val})
            r = bay_change(L, ta, window, v)
            rr = r if (Lr, tar) == (L, ta) else bay_change(Lr, tar, window, v)
            outs.append((max(r["rise"], r["fall"]), rr["rate"]))
        up_dT = max(0.0, outs[0][0] - base_dT, outs[1][0] - base_dT)
        up_rate = max(0.0, outs[0][1] - base_rate, outs[1][1] - base_rate)
        up2_dT += up_dT ** 2
        up2_rate += up_rate ** 2
        rows.append(dict(param=p, low=prm.low, high=prm.high, dT_low=outs[0][0], dT_high=outs[1][0],
                         rate_low=outs[0][1], rate_high=outs[1][1], up_dT=up_dT, up_rate=up_rate))
    rows.sort(key=lambda r: -r["up_dT"])
    return dict(cases=cases, worst_key=worst_key, rate_key=rate_key, base_dT=base_dT, base_rate=base_rate,
                band_dT=math.sqrt(up2_dT), band_rate=math.sqrt(up2_rate), tornado=rows)


# ----------------------------------------------------------------------------------------------
# 4. R3 budget with the drift term split by check
# ----------------------------------------------------------------------------------------------
def healthy(interval: int, drift_ppm) -> F:
    q = fb.fc0_quant_carrier(interval)
    return q + TX_MAX * (Q_TCXO_PPM + F(drift_ppm)) * fb.PPM


def drift_ceiling(interval: int) -> F:
    """Largest XOSC drift (ppm) since the last refresh for which T still meets both threshold conditions."""
    rest = fb.fc0_quant_carrier(interval) + TX_MAX * Q_TCXO_PPM * fb.PPM
    return min(T_MEAS - rest, L_154 - T_MEAS - rest) / (TX_MAX * fb.PPM)


# ----------------------------------------------------------------------------------------------
# 5. Receive-only buffer: squared 25 MHz lines against the receive windows
# ----------------------------------------------------------------------------------------------
def buffer_lines(n_max: int = 8):
    ref = fb.TCXO_REF
    windows = {
        "receive range 144.010-147.999 MHz": RX_RANGE,
        "IF 8 MHz +/-5 kHz": (F_IF - IF_HALF, F_IF + IF_HALF),
        "low-side LO 136.010-139.999 MHz": (RX_RANGE[0] - F_IF, RX_RANGE[1] - F_IF),
        "high-side LO 152.010-155.999 MHz": (RX_RANGE[0] + F_IF, RX_RANGE[1] + F_IF),
        "low-side image 128.010-131.999 MHz": (RX_RANGE[0] - 2 * F_IF, RX_RANGE[1] - 2 * F_IF),
        "high-side image 160.010-163.999 MHz": (RX_RANGE[0] + 2 * F_IF, RX_RANGE[1] + 2 * F_IF),
    }
    out = []
    for n in range(1, n_max + 1):
        f = n * ref
        lo, hi = f * (1 - TG_TOL_PPM * fb.PPM), f * (1 + TG_TOL_PPM * fb.PPM)
        for name, (a, b) in windows.items():
            gap = max(a - hi, lo - b)   # > 0: outside, distance to the nearest window edge
            out.append(dict(n=n, f_MHz=float(f / fb.MHz), window=name, clear_kHz=float(gap / fb.kHz)))
    return out, windows


# ----------------------------------------------------------------------------------------------
# CHECKS
# ----------------------------------------------------------------------------------------------
def run(verbose=True):
    res = []

    def check(case, ok, text):
        res.append((case, bool(ok), text))

    def info(case, text):
        res.append((case, None, text))

    # Known answers
    check("KA-R1", i2c_burst_time(8, F_SCL_FAST) == F(92, 400_000), "8-byte write burst at 400 kHz = 92 SCL clocks = 230 us")
    check("KA-R2", healthy(12, DRIFT_R1_ALLOC) == fb.healthy_disagreement("R3", 12),
          f"R3 interval 12 with the revision 1 drift of 1 ppm reproduces frequency-budget C-12.iv12: {ceil1(healthy(12, 1))} Hz")
    check("KA-R3", T_FC0[12] == F(4096, 10**6) and T_FC0[13] == F(8192, 10**6) and T_FC0[15] == F(32768, 10**6),
          "FC0 interval times 2^n x 1 us: interval 12 = 4.096 ms, 13 = 8.192 ms, 15 = 32.768 ms (RP2350 Table 582)")
    lo0, hi0 = fb.edge_margins(fb.SB60_OFFSET)
    check("KA-R4", edge_margins_a5(fb.SB60_OFFSET, s_ramp=F(0)) == (lo0, hi0),
          f"A5 guard with no settle residual reproduces frequency-budget C-2: upper margin {floor1(hi0)} Hz")

    # ---- Relock (RL)
    tw = c6_write_time()
    twr = c6_write_time(reset=True)
    tw_std = c6_write_time(F_SCL_STD)
    trd = lol_read_time()
    rmax = ramp_limit()
    lm12_nom = l_max(12, T_RAMP_NOM)
    lm12_max = l_max(12, rmax)
    lm13_max = l_max(13, rmax)
    l_prop = floor_step(lm12_nom, L_MAX_STEP)          # proposed deadline, rounded down to 0.1 ms
    l_prop12 = floor_step(lm12_max, L_MAX_STEP)        # the same with the ramp at its 12 ms limit
    info("RL-0", "Sources: " + SOURCES["DS"] + "; " + SOURCES["AN619"])
    info("RL-1", "DS Table 5 and AN619: no PLL lock or relock time is specified for a feedback-divider change. Sourced timing "
                 f"values: TFREQ output frequency transition <= {float(T_FREQ_MAX/US):.0f} us (fCLKn > 1 MHz; applicability to an MSNA "
                 f"change not stated); TRDY power-up to valid output typ {float(T_RDY_TYP/MS):.0f} ms, max {float(T_RDY_MAX/MS):.0f} ms "
                 "(includes PLL acquisition from power-up); TOE <= 10 us. Lock status: AN619 register 0 bit 5 LOL_A")
    check("RL-2", tw <= T_RELOCK_ALLOC, f"C6 changeover writes at 400 kHz Fast-Mode = {ceil3(tw/MS)} ms (with the reg 177 PLL reset "
          f"{ceil3(twr/MS)} ms) inside the 1 ms writes-and-settle allocation; settle time left {floor3((T_RELOCK_ALLOC-tw)/MS)} ms "
          f"({floor3((T_RELOCK_ALLOC-twr)/MS)} ms with the reset)")
    check("RL-2s", tw_std > T_RELOCK_ALLOC, f"at 100 kHz Standard-Mode the same writes take {ceil3(tw_std/MS)} ms, over the allocation: "
          "the Si5351A bus must run Fast-Mode (derived constraint)")
    tw_adr = c6_write_time(F_SCL_ADR031)
    clocks = tw * F_SCL_FAST
    f_min = clocks / (T_RELOCK_ALLOC - T_FREQ_MAX)
    info("RL-2b", f"at the SCL of about 256 kHz that the ADR-031 counts give at clk_sys 96 MHz the writes take {ceil3(tw_adr/MS)} ms, "
                  f"over the 1 ms allocation; the smallest SCL that leaves TFREQ inside it is {math.ceil(float(f_min)/1000)} kHz "
                  f"({int(clocks)} SCL clocks): derived constraint for the WP-PDR-32 count re-derivation (400 kHz Fast-Mode recommended)")
    info("RL-3", f"lock-status read (register 0) at 400 kHz = {ceil3(trd/MS)} ms, inside the 2 ms software allocation T_SW")
    check("RL-4", lm12_nom >= T_RELOCK_ALLOC, f"largest writes-plus-settle time L with interval 12 ({float(T_FC0[12]/MS):.3f} ms) and the "
          f"TS-012 ramp at t0 + 10 ms (PA_EN no later than TX_KEY at t0 + 8 ms) = {float(lm12_nom/MS):.3f} ms >= 1 ms allocation "
          f"(slack {float((lm12_nom-T_RELOCK_ALLOC)/MS):.3f} ms)")
    pa_prop = l_prop + T_FC0[12] + T_SW
    check("RL-4d", pa_prop <= T_RAMP_NOM - G_PA_TO_RAMP, f"proposed deadline L_max = {float(l_prop/MS):.1f} ms (RL-4 rounded down to 0.1 ms): "
          f"PA_EN at t0 + {float(pa_prop/MS):.3f} ms <= TX_KEY at t0 + 8 ms (margin {float((T_RAMP_NOM-G_PA_TO_RAMP-pa_prop)/MS):.3f} ms); "
          f"a 2.0 ms deadline would set PA_EN at t0 + {float((2*MS + T_FC0[12] + T_SW)/MS):.3f} ms, after TX_KEY")
    check("RL-5", lm12_max >= T_RELOCK_ALLOC, f"with the ramp moved to its limit t0 + {float(rmax/MS):.0f} ms (REQ-SYS-161 12 ms, REQ-SYS-160 "
          f"15 - 3 ms): L max = {float(lm12_max/MS):.3f} ms, {float((T_REVISIT-lm12_max)/MS):.3f} ms below the TS-012 revisit threshold "
          f"of 1 + 3 ms: a relock inside the threshold as worded can still miss every sequence inside REQ-SYS-161 (request to WP-PDR-54)")
    check("RL-6", lm13_max <= 0, f"interval 13 ({float(T_FC0[13]/MS):.3f} ms) at the changeover with the 2 ms drive power-up before a "
          f"12 ms ramp leaves L max = {float(lm13_max/MS):.3f} ms: the TS-012 fallback cannot absorb any relock time (finding for WP-PDR-23a)")
    fb_pa = T_RELOCK_ALLOC + T_FC0[13] + T_SW
    info("RL-6f", f"TS-012 fallback as written (1 ms allocation, interval 13, ramp at t0 + 11.5 ms): PA_EN at t0 + {float(fb_pa/MS):.3f} ms, "
                  f"{float((F(115, 10)*MS - fb_pa)/MS):.3f} ms before the ramp, against the 2 ms drive power-up of the nominal sequence")
    settle_nom = l_prop - tw
    settle_max = l_prop12 - tw
    check("RL-7a", T_FREQ_MAX <= T_RELOCK_ALLOC - tw, f"if TFREQ bounds the MSNA retune: settle {float(T_FREQ_MAX/MS):.3f} ms <= "
          f"{floor3((T_RELOCK_ALLOC-tw)/MS)} ms left in the 1 ms allocation after the writes")
    info("RL-7b", f"if only TRDY bounds it: {float(T_RDY_MAX/MS):.0f} ms > {floor3(settle_max/MS)} ms, the largest settle time any "
                  f"sequence inside REQ-SYS-161 allows (and > {floor3(settle_nom/MS)} ms with the TS-012 ramp): the TS-012 revisit "
                  "condition would trigger. The source neither confirms nor excludes it")
    info("RL-8", "verdict: the 1 ms allocation is NOT CONFIRMED by a source (the relock time is not specified). The key-down count "
                 "bounds the mean frequency over its own interval only. It catches the slewing part of a slow relock (ST-2), so that "
                 "part costs availability (a late or lost first element, PA_EN low). It does not catch a linear PLL tail (ST-1), and it "
                 "does not verify the frequency at the ramp: that needs a bound on the settle, the named settle residual S_RAMP of the "
                 f"A5 band-edge guard (G-2), closed by the time-resolved measurement M-1(c). Design response: lock-gated start of the "
                 f"interval-12 count with a deadline of t0 + {float(l_prop/MS):.1f} ms (TS-012 ramp kept); closure of both parts by M-1")

    # ---- Settle tail and the count (ST), INSP-111 finding-7
    tail12 = tail_count_shift(12)
    check("ST-1", tail12 < T_MEAS, f"a linear PLL tail (phase error inside one 40 ns reference period) shifts an interval-12 count by at "
          f"most 2 x 40 ns x 147.9988 MHz / {float(T_FC0[12]/MS):.3f} ms = {ceil1(tail12)} Hz < T 5000 Hz: such a tail can pass the "
          "key-down count, so the count does not bound the frequency at the ramp (reported: the count is not credited for it)")
    tsl = slew_detect_time(12)
    info("ST-2", f"slewing part: a full-error transient (old LO, 8 MHz away) longer than {float(tsl/US):.2f} us inside the interval-12 "
                 "count moves its mean by more than T, so PA_EN stays low: availability, not an unchecked carrier")
    res_m1c = m1c_resolution()
    check("ST-3", res_m1c <= M1C_RES_MAX, f"M-1(c) time-resolved CLK1 frequency: D flip-flop beat of CLK1 ({float(F_CLK1_M1/fb.MHz):.2f} MHz, "
          f"VCO/48) against a steady reference {float(M1C_BEAT):.0f} Hz away, beat edges timestamped by an RP2350 PIO; resolution per "
          f"{float(M1C_WINDOW/MS):.0f} ms window {ceil3(res_m1c)} Hz carrier referred <= S_RAMP/3 = {ceil3(M1C_RES_MAX)} Hz")

    # ---- A5 band-edge guard with the settle residual (G), section 3.1 for A5
    g_lo, g_hi = edge_margins_a5(fb.SB60_OFFSET)
    check("G-1", g_lo > 0, f"A5 lower edge -60 dB point, word 5 Hz + settle residual {float(S_RAMP):.0f} Hz: margin {floor1(g_lo)} Hz")
    check("G-2", g_hi > 0, f"A5 upper edge -60 dB point, word 5 Hz + settle residual {float(S_RAMP):.0f} Hz: margin {floor1(g_hi)} Hz "
          f"(C-2 was {floor1(hi0)} Hz)")
    b_lo, b_hi = edge_margins_a5(fb.BW26_HALF)
    check("G-3", b_lo > 0, f"A5 lower edge 26 dB half-bandwidth: margin {floor1(b_lo)} Hz")
    check("G-4", b_hi > 0, f"A5 upper edge 26 dB half-bandwidth: margin {floor1(b_hi)} Hz")
    g_mo = fb.max_offset_supported(e_word=fb.E_WORD + S_RAMP)
    check("G-5", g_mo >= fb.SB60_OFFSET, f"A5: largest REQ-TX-006 offset the 1.2 kHz guard supports = {floor1(g_mo)} Hz (C-5 was "
          f"{floor1(fb.max_offset_supported())} Hz): the WP-PDR-22 limit for A5")
    g_mp = fb.max_ppm_supported(e_word=fb.E_WORD + S_RAMP)
    check("G-6", g_mp >= fb.REF_CEIL_PPM, f"A5: largest reference error the guard supports at 750 Hz = {floor3(g_mp)} ppm")
    for i, off in enumerate(fb.F7_OFFSETS, 1):
        a, b = edge_margins_a5(off)
        check(f"G-7.{i}", min(a, b) > 0, f"A5, F7 offset {int(off)} Hz: min edge margin {floor1(min(a, b))} Hz")

    # ---- A5 reference budget (RB), revision 4, INSP-111 finding-13 (section 3.5 of the note)
    ew = fb.e_word_ppm()
    check("KA-R5", identity2(fb.UNCAL_TOTAL_PPM, fb.CAL_RANGE_PPM) == fb.guard_identity()
          and guard_a5_min_margin(fb.REF_CEIL_PPM) == g_hi,
          f"identity 2 with the section 3.2 allocations reproduces C-8 ({ceil3(fb.guard_identity())} ppm), and the A5 guard "
          f"function at 2.5 ppm reproduces G-2 ({floor1(g_hi)} Hz)")
    gk = guard_needed(fb.REF_CEIL_PPM)
    ek, kk = fb.REF_CEIL_PPM * fb.PPM, fb.E_WORD + S_RAMP + fb.SB60_OFFSET
    res_hi = fb.BAND_HI - ((fb.BAND_HI - gk) * (1 + ek) + kk)
    res_lo = (fb.BAND_LO + gk) * (1 - ek) - kk - fb.BAND_LO
    check("KA-R6", min(res_hi, res_lo) == 0 and gk < fb.BAND_HI - fb.TX_MAX,
          f"the needed-guard function at 2.5 ppm gives {ceil1(gk)} Hz, at which the governing A5 edge margin is exactly 0 "
          f"(the 1.2 kHz guard exceeds it by about the G-2 margin)")
    unc = {r: a5_uncal(r) for r in TC_ABS}
    cres = a5_cal_residual()
    rb = dict(uncal_ppm={r: float(v) for r, v in unc.items()}, cal_residual_ppm=float(cres), reading_governs=READING_GOV,
              g6_ppm=float(g_mp), r_m3_ppm=float(R_M3_PPM), cases={})

    def rbcase(key, label, ref):
        m = guard_a5_min_margin(ref)
        rb["cases"][key] = dict(label=label, ref_ppm=float(ref), margin_Hz=float(m))
        return m

    info("RB-0", f"TG2520SMN terms (brief sheet, as FR-T): tolerance after reflow at +25 C {float(TG_TOL_PPM)} ppm; fo-TC band "
                 f"+/-{float(TCXO_TC_PPM)} ppm over -40 to +85 C with no stated reference temperature; first-year aging at 25 MHz "
                 f"{float(TG_AGE_PPM)} ppm; fo-Load {float(TCXO_LOAD_COEF_PPM)} and fo-VCC {float(TCXO_VCC_COEF_PPM)} ppm. Uncalibrated "
                 f"total {float(unc['ref25'])} ppm with the band referred to +25 C, {float(unc['pp'])} ppm with the band read as 1.0 ppm "
                 f"peak to peak (governs, the section 3.4.2 reading); TS-007 R-M3 allocation {float(R_M3_PPM)} ppm: R-M3 NOT met for "
                 "RB2 (TG2520SMN) on either reading")
    for r in TC_ABS:
        m0 = rbcase(f"uncal_{r}", f"no calibration ({r})", unc[r])
        info(f"RB-1.{r}", f"no calibration, or a constant of 0: reference {float(unc[r])} ppm; identity 2 at range 0 = "
                          f"{ceil3(identity2(unc[r], 0))} ppm > 2.5 ppm; A5 guard at the -60 dB point: margin {floor1(m0)} Hz "
                          f"({'inside' if m0 > 0 else 'OUTSIDE'} the band; G-6 supports {floor3(g_mp)} ppm)")
    for r in TC_ABS:
        m9 = rbcase(f"wrong09_{r}", f"constant wrong within +/-0.9 ppm ({r})", unc[r] + fb.CAL_RANGE_PPM)
        m15 = rbcase(f"wrong15_{r}", f"constant wrong within +/-1.5 ppm ({r})", unc[r] + CAL_RANGE_TOL)
        info(f"RB-2.{r}", f"constant wrong inside its range ({r}): range +/-{float(fb.CAL_RANGE_PPM)} ppm gives "
                          f"{float(unc[r] + fb.CAL_RANGE_PPM)} ppm of reference (identity 2 {ceil3(identity2(unc[r], fb.CAL_RANGE_PPM))} ppm "
                          f"> 2.5 ppm), -60 dB point {-floor1(m9) if m9 < 0 else 0} Hz beyond the band; range +/-{float(CAL_RANGE_TOL)} ppm "
                          f"(the smallest that corrects the +25 C tolerance) gives {float(unc[r] + CAL_RANGE_TOL)} ppm (identity 2 "
                          f"{ceil3(identity2(unc[r], CAL_RANGE_TOL))} ppm), {-floor1(m15) if m15 < 0 else 0} Hz beyond. Word and settle "
                          "residual counted once each, through the band-edge method")
    ok_cal = cres + ew <= fb.REF_CEIL_PPM
    mc = rbcase("cal_correct", "correct calibration (range >= 1.5 ppm)", cres)
    check("RB-3", ok_cal, f"REQ-SYS-010 after a correct calibration with a range of at least +/-{float(CAL_RANGE_TOL)} ppm: u_cal "
          f"{float(fb.U_CAL_PPM)} + temperature change {float(TCXO_TEMP_PPM)} + aging {float(TG_AGE_PPM)} + load and supply step "
          f"{float(TCXO_STEP_PPM)} + word {ceil3(ew)} = {ceil3(cres + ew)} ppm <= 2.5 ppm (margin {floor3(fb.REF_CEIL_PPM - cres - ew)} ppm); "
          f"A5 guard margin {floor1(mc)} Hz. TPM-006 current best estimate for A5: {ceil3(cres + ew)} ppm, credit false")
    resid09 = TG_TOL_PPM - fb.CAL_RANGE_PPM
    mcl = rbcase("cal_clamp09", "unit at +1.5 ppm, range clamped at +/-0.9 ppm", resid09 + cres)
    info("RB-4", f"with the +/-{float(fb.CAL_RANGE_PPM)} ppm range kept, a unit at +{float(TG_TOL_PPM)} ppm keeps "
                 f"{float(resid09)} ppm uncorrected: {ceil3(resid09 + cres + ew)} ppm after calibration > REQ-SYS-010 2.5 ppm "
                 f"(guard margin {floor1(mcl)} Hz)")
    rmax_guard = {r: g_mp - unc[r] for r in TC_ABS}
    info("RB-5", "no fixed calibration range meets both REQ-SYS-010 for every unit and the guard: REQ-SYS-010 needs at least "
                 f"+/-{float(CAL_RANGE_TOL)} ppm; the guard tolerates at most {floor3(rmax_guard['ref25'])} ppm (ref25) or "
                 f"{floor3(rmax_guard['pp'])} ppm (pp: the guard fails even with no calibration); identity 2 fails at every range, "
                 f"{ceil3(identity2(unc['ref25'], 0))} ppm at range 0")
    # Options for the owner (named, not chosen)
    ok_a = identity2(R_M3_PPM, fb.CAL_RANGE_PPM) <= fb.REF_CEIL_PPM
    ma = rbcase("opt_a_rm3", "option (a): R-M3 part, constant wrong within +/-0.9 ppm", R_M3_PPM + fb.CAL_RANGE_PPM)
    check("RB-6a", ok_a and ma > 0, f"option (a), a TCXO that meets R-M3 ({float(R_M3_PPM)} ppm): identity 2 with +/-"
          f"{float(fb.CAL_RANGE_PPM)} ppm = {ceil3(identity2(R_M3_PPM, fb.CAL_RANGE_PPM))} ppm <= 2.5 ppm (C-8 stands); A5 guard "
          f"with a wrong constant {floor1(ma)} Hz inside")
    gneed = {r: guard_needed(unc[r] + CAL_RANGE_TOL) for r in TC_ABS}
    gcr = {r: ceil_step(gneed[r], GUARD_STEP) for r in TC_ABS}
    rb["guard_needed_Hz"] = {r: float(v) for r, v in gneed.items()}
    rb["guard_cr_Hz"] = {r: float(v) for r, v in gcr.items()}
    info("RB-6b", f"option (b), a guard CR on REQ-SYS-008, 009 and REQ-TX-002 with the range at +/-{float(CAL_RANGE_TOL)} ppm: needed "
                  f"guard {ceil1(gneed['ref25'])} Hz (ref25) and {ceil1(gneed['pp'])} Hz (pp), so {float(gcr['ref25'])/1000:.1f} or "
                  f"{float(gcr['pp'])/1000:.1f} kHz (carrier limits {float((fb.BAND_LO + gcr['pp'])/fb.MHz):.4f} to "
                  f"{float((fb.BAND_HI - gcr['pp'])/fb.MHz):.4f} MHz on the governing reading); REQ-SYS-010 holds (RB-3)")
    d_max = g_mp - cres
    d_prop = floor_step(d_max, F(1, 10))
    md = rbcase("opt_c_delta", f"option (c): constant within +/-{float(d_prop)} ppm of the stored factory offset", cres + d_prop)
    rb.update(delta_max_ppm=float(d_max), delta_prop_ppm=float(d_prop))
    check("RB-6c", md > 0, f"option (c), a software integrity control: the constant is accepted only within +/-delta of the unit's "
          f"measured factory offset, held with an integrity check and entered only by the verified procedure. A wrong constant "
          f"inside that bound errs by at most {float(cres)} + delta ppm; the guard holds for delta <= {floor3(d_max)} ppm (at "
          f"delta = {float(d_prop)} ppm, margin {floor1(md)} Hz). A rejected constant must not fall back to 0: that is RB-1 "
          f"({'outside' if rb['cases']['uncal_pp']['margin_Hz'] < 0 else 'inside'} the band on the governing reading), so it "
          "withholds transmission")
    # Two-unit offset and the section 3.2 C-10 re-read with the band-change reading (finding-13 last bullet)
    tu = {}
    for age in (F(0), TG_AGE_PPM):
        per = fb.U_CAL_PPM + TCXO_TEMP_PPM + age + TCXO_STEP_PPM
        tu[float(age)] = 2 * per * fb.F_REF_TWO_UNIT * fb.PPM + 2 * fb.E_WORD
    rb["two_unit_Hz"] = {str(k): float(v) for k, v in tu.items()}
    info("RB-7", f"A5 two-unit offset after calibration at 146 MHz (RSK-002 step S1; per unit u_cal + 1.0 band change + aging + "
                 f"0.4 step, word per unit): {ceil1(tu[0.0])} Hz at calibration, {ceil1(tu[float(TG_AGE_PPM)])} Hz after one "
                 f"year, both outside the {float(fb.HALF_PASSBAND):.0f} Hz half-passband")
    c10 = []
    for c in fb.TEMP_CLASSES_PPM:
        cal = fb.U_CAL_PPM + 2 * c + fb.AGING_PPM + fb.SUPPLY_LOAD_PPM + ew
        t0 = 2 * (fb.U_CAL_PPM + 2 * c + fb.SUPPLY_LOAD_PPM) * fb.F_REF_TWO_UNIT * fb.PPM + 2 * fb.E_WORD
        t1 = 2 * (fb.U_CAL_PPM + 2 * c + fb.AGING_PPM + fb.SUPPLY_LOAD_PPM) * fb.F_REF_TWO_UNIT * fb.PPM + 2 * fb.E_WORD
        c10.append(dict(cls=float(c), cal_ppm=float(cal), two_unit_0_Hz=float(t0), two_unit_1y_Hz=float(t1)))
    rb["c10_band_change"] = c10
    info("RB-8", "section 3.2 C-10 and the two-unit table re-read with a class of c ppm as a 2c change (the section 3.4.2 reading): "
                 + "; ".join(f"class {r['cls']}: {ceil3(r['cal_ppm'])} ppm <= 2.5, two units {ceil1(r['two_unit_0_Hz'])} / "
                             f"{ceil1(r['two_unit_1y_Hz'])} Hz" for r in c10)
                 + " (at calibration / after one year; TS-007 classes, not A5)")

    # ---- Freshness (FR)
    env = xo_slope_envelope()
    s_max = env["s_max"]
    check("FR-1", env["n_admissible"] > 0, f"AT-cut curves inside the Table 596 +/-30 ppm band: {env['n_admissible']} admitted; "
          f"largest |slope| over {T_XO_OPER[0]:.0f} to {T_XO_OPER[1]:.0f} C = {ceil3(s_max)} ppm/K (a1 {env['arg']['a1']:.3f}, "
          f"a3 {env['arg']['a3']:.2e}, Ti {env['arg']['ti']:.1f} C, at {env['arg']['t_at']:.1f} C)")
    dT_local = DP_PICO * RTH_PICO
    rate_local = dT_local / TAU_PICO_MIN
    tcxo_fixed = float(TCXO_TEMP_PPM + TCXO_STEP_PPM)
    info("FR-T", f"TCXO terms (TG2520SMN brief sheet, {SOURCES['TCXO'][:60]}...): temperature change since the refresh bounded by "
                 f"the fo-TC band +/-{float(TCXO_TC_PPM)} ppm = {float(TCXO_TEMP_PPM)} ppm peak to peak (no slope is given, so the band "
                 f"holds for any temperature step, and for any ratio age); load and supply step between the stage-on refresh and the "
                 f"stage-off check 2 x {float(TCXO_LOAD_COEF_PPM)} (fo-Load, 10 kOhm // 10 pF +/-10 %) + 2 x {float(TCXO_VCC_COEF_PPM)} "
                 f"(fo-VCC, VCC +/-5 %) = {float(TCXO_STEP_PPM)} ppm, present at every check (interval 12 included), on the condition that "
                 "both states stay inside those load and supply ranges; together "
                 f"{tcxo_fixed} ppm")

    # key-down check (interval 12): the drift is XOSC (slope x rate x age + pushing) + the TCXO terms
    bb_short = bay_band(60.0)
    rate_bay = bb_short["base_rate"] + bb_short["band_rate"]
    rate_tot = rate_bay + rate_local
    A_KD = 10                                          # proposed ratio-age limit at the key-down check, s (kept from revision 2)
    d_kd_xo = s_max * rate_tot * A_KD + float(PUSH_PPM)
    d_kd = d_kd_xo + tcxo_fixed
    alloc12 = ceil_step(d_kd, ALLOC_STEP)             # interval-12 allocation: the bound at A_kd rounded up to 0.5 ppm
    a_kd_limit = (float(alloc12) - tcxo_fixed - float(PUSH_PPM)) / (s_max * rate_tot)
    a_kd = A_KD
    dc12 = drift_ceiling(12)
    dc13 = drift_ceiling(13)
    check("FR-2", d_kd <= float(alloc12) and a_kd <= a_kd_limit and alloc12 <= dc12,
          f"key-down check (interval 12) on a ratio no older than A_kd = {a_kd} s: XOSC {ceil3(s_max)} ppm/K x ({ceil3(rate_bay)} K/s "
          f"bay + {ceil3(rate_local)} K/s local) x {a_kd} s + {float(PUSH_PPM)} ppm pushing = {ceil3(d_kd_xo)} ppm, + TCXO "
          f"{tcxo_fixed} ppm = {ceil3(d_kd)} ppm <= proposed interval-12 allocation {float(alloc12)} ppm (rounded up to 0.5 ppm) "
          f"<= interval-12 ceiling {floor3(dc12)} ppm; A_kd limit at that allocation {floor1(a_kd_limit)} s (A_kd = {a_kd} s kept)")
    t_age_rx = T_REFRESH + T_BUF_SETTLE + T_FC0[15]
    check("FR-2r", t_age_rx <= a_kd,
          f"in receive the ratio is at most {ceil3(t_age_rx)} s old (1 s refresh + "
          f"{float((T_BUF_SETTLE + T_FC0[15])/MS):.3f} ms buffer settle and interval-15 count) <= A_kd")

    W = float(T_OVER_MAX) + a_kd
    bb = bay_band(W)
    dT_bay = bb["base_dT"] + bb["band_dT"]
    d_over_xo = s_max * (dT_bay + dT_local) + float(PUSH_PPM)
    d_over = d_over_xo + tcxo_fixed
    info("FR-3", f"window W = A_kd {a_kd} s + longest over {float(T_OVER_MAX):.0f} s (REQ-SYS-180) = {W:.0f} s; main-bay change "
          f"nominal {ceil3(bb['base_dT'])} K ({bb['worst_key'][0]}, {bb['worst_key'][1]:.0f} C) + band {ceil3(bb['band_dT'])} K = "
          f"{ceil3(dT_bay)} K; local Pico 2 step {ceil3(dT_local)} K")
    info("FR-4", f"ratio drift bound over the longest over = XOSC {ceil3(s_max)} x ({ceil3(dT_bay)} + {ceil3(dT_local)}) K + "
          f"{float(PUSH_PPM)} = {ceil3(d_over_xo)} ppm, + TCXO {tcxo_fixed} ppm = {ceil3(d_over)} ppm > the 1 ppm allocation: the "
          "TS-012 condition 'ratio fresh over a long over within 1 ppm' is NOT met as worded (revisit condition triggered)")
    info("FR-5", f"the aged ratio cannot serve an interval-12 check: drift ceiling at interval 12 = {floor3(dc12)} ppm "
          f"< {ceil3(d_over)} ppm (so interval 12 is used only on a ratio no older than A_kd)")
    d13_alloc = ceil_step(d_over, ALLOC_STEP)         # proposed allocation: the bound rounded up to 0.5 ppm
    check("FR-6", d13_alloc <= dc13, f"during the over (interval 13) the aged ratio is inside the drift ceiling {floor3(dc13)} ppm; "
          f"proposed allocation {float(d13_alloc)} ppm (bound {ceil3(d_over)} ppm rounded up to 0.5 ppm), margin to the ceiling "
          f"{floor3(dc13 - d13_alloc)} ppm")
    # M-2 pass limits that equal the budget: the ratio (counted with the stage on, in receive) sees the XOSC thermal drift
    # and the TCXO temperature change, but not the pushing or the TCXO step, which exist only in the transmit state
    m2a_over = d13_alloc - PUSH_PPM - TCXO_STEP_PPM
    m2a_kd = alloc12 - PUSH_PPM - TCXO_STEP_PPM
    info("FR-7", f"M-2(a) ratio-change pass limits equal to the budget: over the longest over <= {float(m2a_over)} ppm (interval-13 "
                 f"allocation {float(d13_alloc)} less pushing {float(PUSH_PPM)} and TCXO step {float(TCXO_STEP_PPM)}); in the first "
                 f"A_kd = {a_kd} s after an over <= {float(m2a_kd)} ppm (interval-12 allocation {float(alloc12)} less the same). "
                 f"M-2(b) transmit-state step (pushing + TCXO step, seen only on the carrier): <= {float(PUSH_PPM)} ppm XOSC and "
                 f"<= {float(TCXO_STEP_PPM)} ppm TCXO")

    # ---- Budget (B), with the split drift
    for iv, dr, use in ((12, alloc12, "key-down check before PA_EN, ratio age <= A_kd"),
                        (13, d13_alloc, "checks during the over, ratio from before the over")):
        d = healthy(iv, dr)
        check(f"B-12.iv{iv}", d < T_MEAS, f"{use}: healthy disagreement {ceil1(d)} Hz < T 5000 Hz (margin {floor1(T_MEAS-d)} Hz)")
        check(f"B-16.iv{iv}", T_MEAS + d <= L_154, f"{use}: largest undetected true error {ceil1(T_MEAS+d)} Hz <= REQ-SYS-154 10 kHz "
              f"(margin {floor1(L_154-T_MEAS-d)} Hz)")
        check(f"B-18.iv{iv}", F_INJ - d > T_MEAS, f"{use}: TC-SYS-101 12 kHz injection measures >= {floor1(F_INJ-d)} Hz > T (margin "
              f"{floor1(F_INJ-d-T_MEAS)} Hz)")
        rest = d - fb.fc0_quant_carrier(iv)
        acc = min(T_MEAS - rest, L_154 - T_MEAS - rest) / fb.PRESCALE
        check(f"B-16a.iv{iv}", fb.FC0[iv][1] < acc, f"{use}: FC0 accuracy ceiling at the counted input {floor1(acc)} Hz against "
              f"Table 541 {float(fb.FC0[iv][1])} Hz (the dev-board known-clock acceptance limit for A5 at interval {iv})")
    t_tx = 2 * T_FC0[13] + fb.T_TASK + fb.T_RF_OFF
    check("B-15", t_tx <= fb.T_LIMIT, f"fault during transmission detected and RF off in 2 x {float(T_FC0[13]/MS):.3f} + 10 + 20 = "
          f"{ceil1(t_tx/MS)} ms <= 100 ms")
    check("B-11", TX_MAX / fb.PRESCALE < fb.GPIN_MAX and fb.TCXO_REF < fb.GPIN_MAX,
          "GPIN0 carrier/8 18.50 MHz and GPIN1 TCXO 25.000 MHz are both below the 50 MHz GPIN limit")
    t_refresh = T_BUF_SETTLE + T_FC0[15]
    check("B-19", t_refresh < T_REFRESH, f"ratio refresh in receive: buffer settle {float(T_BUF_SETTLE/MS):.0f} ms + interval 15 "
          f"{float(T_FC0[15]/MS):.3f} ms = {ceil1(t_refresh/MS)} ms per refresh (buffer on {ceil1(t_refresh/T_REFRESH*100)} % of receive)")

    # ---- Buffer lines (BL)
    lines, windows = buffer_lines()
    worst = min(lines, key=lambda r: r["clear_kHz"])
    check("BL-1", all(r["clear_kHz"] > 0 for r in lines), f"squared 25 MHz harmonics 1 to 8 (+/-2.5 ppm) fall in no receive window; "
          f"nearest: n = {worst['n']} ({worst['f_MHz']:.3f} MHz) {worst['clear_kHz']:.0f} kHz from the {worst['window']}")
    info("BL-2", "transmit: the buffer supply is off from t0 until receive resumes, so the buffer adds nothing to the 150.000 MHz "
                 "line; the spurs-ts012 figure stands (plan PB high estimate -12.1 dBm at the SMA, 3.9 dB over 25 uW, a residual "
                 "line closing at the bench). The unpowered buffer input must neither load nor rectify the TCXO (partial power-down "
                 "input: a part constraint for WP-PDR-37 and 38)")

    summary = dict(
        relock=dict(t_writes_ms=float(tw / MS), t_writes_reset_ms=float(twr / MS), t_writes_std_ms=float(tw_std / MS),
                    t_lol_read_ms=float(trd / MS), t_writes_256k_ms=float(c6_write_time(F_SCL_ADR031) / MS),
                    scl_min_kHz=float(c6_write_time() * F_SCL_FAST / (T_RELOCK_ALLOC - T_FREQ_MAX)) / 1000, L_max_iv12_ramp10_ms=float(lm12_nom / MS),
                    L_max_iv12_ramp12_ms=float(lm12_max / MS), L_max_iv13_ramp12_ms=float(lm13_max / MS),
                    L_max_proposed_ms=float(l_prop / MS), L_max_proposed_ramp12_ms=float(l_prop12 / MS),
                    pa_en_proposed_ms=float(pa_prop / MS), fallback_pa_en_ms=float(fb_pa / MS),
                    fallback_gap_ms=float((F(115, 10) * MS - fb_pa) / MS), t_fc0_ms={iv: float(t / MS) for iv, t in T_FC0.items()},
                    settle_left_in_alloc_ms=float((T_RELOCK_ALLOC - tw) / MS), settle_max_ramp10_ms=float(settle_nom / MS),
                    settle_max_ramp12_ms=float(settle_max / MS), tfreq_ms=float(T_FREQ_MAX / MS), trdy_max_ms=float(T_RDY_MAX / MS),
                    trdy_typ_ms=float(T_RDY_TYP / MS), verdict="1 ms allocation not confirmed by a source; lock-gated start; the count bounds its own mean only; "
                            "settle residual at the ramp closed by M-1(c)"),
        settle=dict(tail_count_shift_iv12_Hz=float(tail12), slew_detect_us=float(tsl / US), s_ramp_Hz=float(S_RAMP),
                    m1c_resolution_Hz=float(res_m1c), m1c_res_max_Hz=float(M1C_RES_MAX),
                    guard_a5=dict(sb60_lo_Hz=float(g_lo), sb60_hi_Hz=float(g_hi), bw26_lo_Hz=float(b_lo), bw26_hi_Hz=float(b_hi),
                                  max_offset_Hz=float(g_mo), max_ppm=float(g_mp), c2_hi_Hz=float(hi0),
                                  terms_hi_Hz=dict(reference=float(fb.TX_MAX * fb.REF_CEIL_PPM * fb.PPM), word=float(fb.E_WORD),
                                                   settle=float(S_RAMP), sideband=float(fb.SB60_OFFSET)))),
        freshness=dict(s_max_ppm_per_K=s_max, s_arg=env["arg"], n_admissible=env["n_admissible"], rate_bay_K_s=rate_bay,
                       rate_local_K_s=rate_local, A_kd_s=a_kd, A_kd_limit_s=a_kd_limit, drift_kd_ppm=d_kd, window_s=W,
                       drift_kd_xosc_ppm=d_kd_xo, drift_over_xosc_ppm=d_over_xo, tcxo_temp_ppm=float(TCXO_TEMP_PPM),
                       tcxo_step_ppm=float(TCXO_STEP_PPM), drift_alloc_iv12_ppm=float(alloc12),
                       m2a_limit_over_ppm=float(m2a_over), m2a_limit_kd_ppm=float(m2a_kd), t_age_rx_s=float(t_age_rx),
                       dT_bay_nominal_K=bb["base_dT"], dT_bay_band_K=bb["band_dT"], dT_bay_worst_case=list(bb["worst_key"]),
                       dT_local_K=dT_local, drift_over_ppm=d_over, drift_ceiling_iv12_ppm=float(dc12),
                       drift_ceiling_iv13_ppm=float(dc13), drift_alloc_iv13_ppm=float(d13_alloc),
                       tornado_top=bb["tornado"][:8],
                       cases={f"{k[0]} {k[1]:.0f} C": dict(rise=v["rise"], fall=v["fall"], rate=v["rate"]) for k, v in bb["cases"].items()},
                       verdict="1 ppm over the longest over not met; budget closes with A_kd on the key-down check and the interval-13 allocation"),
        budget={f"iv{iv}": dict(healthy_Hz=float(healthy(iv, dr)), margin_T_Hz=float(T_MEAS - healthy(iv, dr)),
                                undetected_Hz=float(T_MEAS + healthy(iv, dr)), drift_ppm=float(dr))
                for iv, dr in ((12, alloc12), (13, d13_alloc))},
        buffer_lines=lines,
        reference_a5=rb,
    )
    plots = dict(env=env, bb=bb, bb_short=bb_short, W=W, a_kd=a_kd, d_over=d_over, d13=float(d13_alloc), dc12=float(dc12),
                 d12=float(alloc12), a_kd_limit=a_kd_limit, tcxo_fixed=tcxo_fixed,
                 dc13=float(dc13), s_max=s_max, rate_tot=rate_tot, dT_local=dT_local, lines=lines, windows=windows)
    return res, summary, plots


# ----------------------------------------------------------------------------------------------
# FIGURES
# ----------------------------------------------------------------------------------------------
def fig_relock(out: Path, s):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    r = s["relock"]
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 7.2), gridspec_kw=dict(height_ratios=[1.25, 1]))
    # Panel 1: timelines
    rows = [
        ("TS-012 rev 6 (1 ms allocation)", 1.0, 12, 10.0),
        (f"proposed deadline, ramp at 10 ms (L_max = {r['L_max_proposed_ms']:.1f} ms)", r["L_max_proposed_ms"], 12, 10.0),
        (f"latest, ramp at 12 ms limit (L = {r['L_max_proposed_ramp12_ms']:.1f} ms)", r["L_max_proposed_ramp12_ms"], 12, 12.0),
        (f"TS-012 fallback: interval 13, ramp 11.5 ms ({r['fallback_gap_ms']:.3f} ms PA_EN to ramp)", 1.0, 13, 11.5),
    ]
    for i, (lab, L, iv, ramp) in enumerate(rows):
        y = len(rows) - 1 - i
        tw = r["t_writes_ms"]
        ax1.barh(y, tw, left=0, color="#1f77b4", height=0.5)
        ax1.barh(y, max(L - tw, 0), left=tw, color="#aec7e8", height=0.5)
        fc = float(T_FC0[iv] / MS)
        ax1.barh(y, fc, left=L, color="#2ca02c", height=0.5)
        ax1.barh(y, 2.0, left=L + fc, color="#ff7f0e", height=0.5)
        pa = L + fc + 2.0
        ok = pa <= ramp - 2.0 + 1e-9
        ax1.plot([pa], [y], marker="v", color="k" if ok else "red", ms=9)
        ax1.plot([ramp], [y], marker="|", color="purple", ms=22, mew=2.5)
        ax1.text(12.9, y, lab, va="center", fontsize=8)
    ax1.axvline(float(T_LEADIN / MS), color="red", ls="--", lw=1)
    ax1.text(float(T_LEADIN / MS) + 0.1, 3.3, "REQ-SYS-161 12 ms", color="red", fontsize=7)
    ax1.set_xlim(0, 22)
    ax1.set_yticks([])
    ax1.set_xlabel("time after the changeover command t0 (ms)")
    ax1.set_ylim(-0.6, 3.7)
    ax1.set_title("Key-down sequence: C6 I2C writes at 400 kHz (dark blue), PLL settle (light blue), FC0 count 2^n x 1 us (green), "
                  "software 2 ms (orange);\nPA_EN (triangle; red = later than 2 ms before the ramp), ramp start (purple bar)", fontsize=9)
    ax1.grid(alpha=0.3, axis="x")
    # Panel 2: sourced bounds against the settle budget (log)
    items = [
        ("TFREQ max (DS Table 5), if it covers an MSNA change", r["tfreq_ms"], "#2ca02c"),
        ("settle left in the 1 ms allocation after the writes", r["settle_left_in_alloc_ms"], "#1f77b4"),
        ("largest settle, proposed L_max with the TS-012 ramp at 10 ms", r["settle_max_ramp10_ms"], "#1f77b4"),
        ("largest settle, ramp at the 12 ms limit", r["settle_max_ramp12_ms"], "#1f77b4"),
        ("TRDY typ (DS Table 5), power-up to valid output", r["trdy_typ_ms"], "#d62728"),
        ("TRDY max (DS Table 5), power-up to valid output", r["trdy_max_ms"], "#d62728"),
    ]
    for i, (lab, v, c) in enumerate(items):
        y = len(items) - 1 - i
        ax2.barh(y, v, color=c, height=0.55)
        ax2.text(v * 1.15, y, f"{v:.3g} ms  {lab}", va="center", fontsize=8)
    ax2.set_xscale("log")
    ax2.set_xlim(0.005, 400)
    ax2.set_yticks([])
    ax2.set_xlabel("time (ms, log scale)")
    ax2.set_title("Si5351A relock: no lock time in the data sheet or AN619; the sourced values bracket the settle budget", fontsize=9)
    ax2.grid(alpha=0.3, axis="x", which="both")
    fig.suptitle("cwht route R3, A5: Si5351A PLL relock at the changeover (r3_a5.py, developer evidence)", fontsize=10)
    fig.tight_layout()
    fig.savefig(out, dpi=130)
    plt.close(fig)


def fig_fresh(out: Path, s, p):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fr = s["freshness"]
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.5, 4.8))
    cols = {"A5-DC": "#1f77b4", "A5-R4": "#c0504d"}
    for (L, ta), c in p["bb"]["cases"].items():
        t, y = c["trace_h"]
        ax1.plot(t, y, color=cols[L], lw=1.2 if ta == 45 else 0.8, ls="-" if ta != -10 else ":",
                 label=f"{L} {ta:.0f} C heating" if ta in (45.0, -10.0) else None)
        t, y = c["trace_c"]
        ax1.plot(t, y, color=cols[L], lw=0.8, ls="--", label=f"{L} {ta:.0f} C cooling" if ta == 45.0 else None)
    top = fr["dT_bay_nominal_K"] + fr["dT_bay_band_K"]
    ax1.axhline(top, color="k", ls="-.", lw=1)
    ax1.text(4, top + 0.05, f"worst nominal {fr['dT_bay_nominal_K']:.2f} K + band {fr['dT_bay_band_K']:.2f} K = {top:.2f} K", fontsize=8)
    ax1.axvline(p["W"], color="gray", ls=":", lw=1)
    ax1.text(p["W"] - 2, 0.1, f"W = {p['W']:.0f} s", fontsize=8, ha="right")
    ax1.set_xlabel("time into the over (s)")
    ax1.set_ylabel("main-bay (Pico 2) temperature change (K)")
    ax1.set_title("Thermal model MAIN node: continuous transmit from receive steady\nstate (heating) and receive from transmit steady state (cooling)", fontsize=9)
    ax1.grid(alpha=0.3)
    ax1.legend(fontsize=7, loc="lower right")
    # Panel 2: drift bound against ratio age
    ages = np.linspace(0, p["W"], 400)
    # rate-limited growth, capped by the full-window bound
    drift_xo = np.minimum(p["s_max"] * p["rate_tot"] * ages, p["s_max"] * (top + p["dT_local"])) + float(PUSH_PPM)
    drift = drift_xo + p["tcxo_fixed"]
    ax2.plot(ages, drift, color="#1f77b4", lw=1.8, label=f"ratio drift bound: XOSC + TCXO {p['tcxo_fixed']:.1f} ppm (band 1.0, step 0.4)")
    ax2.plot(ages, drift_xo, color="#1f77b4", lw=1.0, ls=":", label="XOSC part only (revision 2 bound)")
    ax2.axhline(p["d12"], color="#2ca02c", ls="--", lw=1, label=f"proposed interval-12 allocation {p['d12']:.1f} ppm (key-down check)")
    ax2.axhline(p["dc12"], color="#2ca02c", ls=":", lw=1, label=f"interval-12 ceiling {p['dc12']:.2f} ppm (zero margin)")
    ax2.axhline(p["d13"], color="#ff7f0e", ls="--", lw=1, label=f"proposed interval-13 allocation {p['d13']:.1f} ppm")
    ax2.axhline(p["dc13"], color="#ff7f0e", ls=":", lw=1, label=f"interval-13 ceiling {p['dc13']:.2f} ppm (zero margin)")
    ax2.axvline(p["a_kd"], color="gray", ls="-.", lw=1)
    ax2.text(p["a_kd"] + 2, 12.5, f"A_kd = {p['a_kd']} s\n(limit {math.floor(p['a_kd_limit'] * 10) / 10:.1f} s)", fontsize=8)
    ax2.plot([p["W"]], [p["d_over"]], "o", color="#d62728")
    ax2.annotate(f"{p['d_over']:.2f} ppm at W", xy=(p["W"], p["d_over"]), xytext=(p["W"] - 80, p["d_over"] + 3.0), fontsize=8,
                 arrowprops=dict(arrowstyle="->", lw=0.8))
    ax2.set_xlabel("ratio age at the check (s)")
    ax2.set_ylabel("ratio drift since the refresh (ppm)")
    ax2.set_ylim(0, 20)
    ax2.set_title("TCXO ratio freshness: drift bound against the allocations\n(interval 12 only on a fresh ratio; interval 13 during the over)", fontsize=9)
    ax2.grid(alpha=0.3)
    ax2.legend(fontsize=7, loc="upper left")
    fig.suptitle("cwht route R3, A5: XOSC/TCXO ratio freshness over the longest over (r3_a5.py, developer evidence)", fontsize=10)
    fig.tight_layout()
    fig.savefig(out, dpi=130)
    plt.close(fig)


def fig_settle(out: Path, s):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    st = s["settle"]
    g = st["guard_a5"]
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.5, 4.6), gridspec_kw=dict(width_ratios=[1, 1.3]))
    # Panel 1: what the key-down count can and cannot see
    labs = ["largest count shift\nfrom a linear tail\n(2 x 40 ns, ST-1)", "measured\nthreshold T"]
    vals = [st["tail_count_shift_iv12_Hz"], float(T_MEAS)]
    ax1.bar([0, 1], vals, color=["#d62728", "#2ca02c"], width=0.55)
    for i, v in enumerate(vals):
        ax1.text(i, v + 80, f"{v:.0f} Hz", ha="center", fontsize=8)
    ax1.set_xticks([0, 1])
    ax1.set_xticklabels(labs, fontsize=8)
    ax1.set_ylim(0, 6500)
    ax1.set_ylabel("shift of the interval-12 count mean (Hz, carrier referred)")
    ax1.set_title(f"Interval-12 count ({float(T_FC0[12]/MS):.3f} ms): a linear PLL tail stays inside T,\nso the count does not "
                  f"verify the frequency at the ramp (slewing > {st['slew_detect_us']:.2f} us is caught)", fontsize=9)
    ax1.grid(alpha=0.3, axis="y")
    # Panel 2: A5 upper-edge guard with the settle residual
    terms = [("reference 2.5 ppm", g["terms_hi_Hz"]["reference"], "#1f77b4"), ("word 5 Hz", g["terms_hi_Hz"]["word"], "#9467bd"),
             (f"settle residual S_RAMP {g['terms_hi_Hz']['settle']:.0f} Hz", g["terms_hi_Hz"]["settle"], "#d62728"),
             ("-60 dB offset 750 Hz", g["terms_hi_Hz"]["sideband"], "#ff7f0e")]
    left = 0.0
    for lab, v, c in terms:
        ax2.barh(0, v, left=left, color=c, height=0.5, label=f"{lab}: {v:.1f} Hz")
        left += v
    ax2.barh(0, g["sb60_hi_Hz"], left=left, color="#2ca02c", height=0.5, alpha=0.5, label=f"margin {g['sb60_hi_Hz']:.1f} Hz (C-2 was {g['c2_hi_Hz']:.1f} Hz)")
    ax2.axvline(1200, color="k", ls="--", lw=1)
    ax2.text(1195, 0.42, "band edge 148.000 MHz\n(1.2 kHz above 147.9988 MHz)", fontsize=7, ha="right")
    ax2.text(20, -0.8, f"M-1(c) resolution {st['m1c_resolution_Hz']:.2f} Hz per 1 ms window (limit S_RAMP/3 = {st['m1c_res_max_Hz']:.2f} Hz)",
             va="center", fontsize=7)
    ax2.text(20, -1.3, f"M-1(c) pass: |f - f_final| <= {st['s_ramp_Hz']:.0f} Hz in every window from the ramp", va="center", fontsize=7)
    ax2.set_xlim(0, 1300)
    ax2.set_ylim(-1.7, 1.2)
    ax2.set_yticks([])
    ax2.set_xlabel("offset above the upper carrier limit 147.9988 MHz (Hz)")
    ax2.set_title("A5 upper band edge (G-2): the settle residual at the ramp as a named term", fontsize=9)
    ax2.legend(fontsize=7, loc="upper left")
    ax2.grid(alpha=0.3, axis="x")
    fig.suptitle("cwht route R3, A5: what the key-down count verifies, and the settle residual at the ramp (r3_a5.py, developer evidence)",
                 fontsize=10)
    fig.tight_layout()
    fig.savefig(out, dpi=130)
    plt.close(fig)


def fig_reference(out: Path, s):
    """Revision 4 (INSP-111 finding-13): the A5 reference budget, reference error per case against the limits, and the
    position of the -60 dB point against the band edge."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    rb = s["reference_a5"]
    cs = rb["cases"]
    order = [("opt_a_rm3", "(a) R-M3 part (1.5 ppm),\nconstant wrong within +/-0.9"),
             ("cal_correct", "TG2520SMN, correct\ncalibration (range >= 1.5)"),
             ("cal_clamp09", "TG2520SMN at +1.5 ppm,\nrange clamped at +/-0.9"),
             ("uncal_ref25", "TG2520SMN, no calibration\n(band referred to +25 C)"),
             ("uncal_pp", "TG2520SMN, no calibration\n(band 1.0 ppm p-p, governs)"),
             ("opt_c_delta", f"(c) constant within +/-{rb['delta_prop_ppm']:.1f}\nof the stored factory offset"),
             ("wrong09_ref25", "constant wrong within\n+/-0.9 (ref25)"),
             ("wrong09_pp", "constant wrong within\n+/-0.9 (pp, governs)"),
             ("wrong15_ref25", "constant wrong within\n+/-1.5 (ref25)"),
             ("wrong15_pp", "constant wrong within\n+/-1.5 (pp, governs)")]
    y = np.arange(len(order))[::-1]
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13.5, 6.4), sharey=True, gridspec_kw=dict(width_ratios=[1.1, 1]))
    refs = [cs[k]["ref_ppm"] for k, _ in order]
    marg = [cs[k]["margin_Hz"] for k, _ in order]
    col = ["#2ca02c" if m > 0 else "#d62728" for m in marg]
    ax1.barh(y, refs, color=col, height=0.6)
    for yi, v in zip(y, refs):
        ax1.text(v + 0.05, yi, f"{v:.3f}", va="center", fontsize=7, bbox=dict(fc="white", ec="none", pad=0.5))
    ax1.axvline(rb["r_m3_ppm"], color="#7f7f7f", ls=":", lw=1.2, label=f"TS-007 R-M3 allocation {rb['r_m3_ppm']:.1f} ppm (uncalibrated)")
    ax1.axvline(2.5, color="k", ls="--", lw=1.2, label="REQ-SYS-010 and identity 2 limit 2.5 ppm")
    ax1.axvline(rb["g6_ppm"], color="#d62728", ls="-", lw=1.2, label=f"A5 guard supports {floor3(rb['g6_ppm'])} ppm (G-6)")
    ax1.set_yticks(y)
    ax1.set_yticklabels([lab for _, lab in order], fontsize=7.5)
    ax1.set_xlim(0, 6.6)
    ax1.set_xlabel("reference error, ppm of the carrier (word and settle residual not included)")
    ax1.set_title("A5 reference error per case (green: -60 dB point inside the band; red: outside)", fontsize=9)
    ax1.legend(fontsize=7, loc="upper right")
    ax1.grid(alpha=0.3, axis="x")
    ax2.barh(y, marg, color=col, height=0.6)
    for yi, v in zip(y, marg):
        ax2.text(v + (6 if v >= 0 else -6), yi, f"{v:+.1f} Hz", va="center", ha="left" if v >= 0 else "right", fontsize=7)
    ax2.axvline(0, color="k", lw=1.2)
    ax2.text(-5, y[0] + 0.55, "band edge 148.000 MHz (upper edge governs)", fontsize=7, ha="right")
    ax2.set_xlim(-340, 210)
    ax2.set_ylim(-0.7, len(order) - 0.2)
    ax2.set_xlabel("margin of the -60 dB point inside the band (Hz)")
    ax2.set_title("-60 dB point against the band edge (750 Hz offset, word 5 Hz, S_RAMP 5 Hz)", fontsize=9)
    ax2.grid(alpha=0.3, axis="x")
    gn = rb["guard_needed_Hz"]
    fig.text(0.5, 0.01, f"(b) guard CR with range +/-1.5 ppm: needed {gn['ref25']:.1f} Hz (ref25) or {gn['pp']:.1f} Hz (pp), "
             f"so {rb['guard_cr_Hz']['ref25']/1000:.1f} or {rb['guard_cr_Hz']['pp']/1000:.1f} kHz. (c): a rejected or missing constant "
             "must withhold transmission, since no calibration is outside the band on the governing reading", fontsize=8, ha="center")
    fig.suptitle("cwht A5 reference budget with the TG2520SMN: the calibration bound against the band edge "
                 "(r3_a5.py revision 4, developer evidence)", fontsize=10)
    fig.tight_layout(rect=(0, 0.035, 1, 1))
    fig.savefig(out, dpi=130)
    plt.close(fig)


def fig_slope(out: Path, p):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    env = p["env"]
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.4))
    T = np.linspace(*XO_T_RANGE, 251)
    rng = np.random.default_rng(1)
    # draw a sample of admissible curves
    shown = 0
    for a3 in np.linspace(*A3_RANGE, 3):
        for ti in np.linspace(*TI_RANGE, 3):
            for a1 in np.arange(-1.2, 0.4, 0.05):
                f = a1 * (T - ti) + a3 * (T - ti) ** 3
                f25 = a1 * (25 - ti) + a3 * (25 - ti) ** 3
                if np.max(np.abs(f - f25)) <= XO_STAB_PPM:
                    ax1.plot(T, f - f25, color="#1f77b4", lw=0.4, alpha=0.5)
                    shown += 1
    a = env["arg"]
    f = a["a1"] * (T - a["ti"]) + a["a3"] * (T - a["ti"]) ** 3
    f25 = a["a1"] * (25 - a["ti"]) + a["a3"] * (25 - a["ti"]) ** 3
    ax1.plot(T, f - f25, color="#d62728", lw=1.8, label="curve with the largest slope in service")
    ax1.axhline(XO_STAB_PPM, color="k", ls="--", lw=0.8)
    ax1.axhline(-XO_STAB_PPM, color="k", ls="--", lw=0.8, label="Table 596 +/-30 ppm band")
    ax1.axvspan(*T_XO_OPER, color="gold", alpha=0.15, label="crystal temperature in service")
    ax1.set_xlabel("crystal temperature (C)")
    ax1.set_ylabel("frequency change from 25 C (ppm)")
    ax1.set_title(f"Admissible AT-cut curves ({shown} of {env['n_admissible']} drawn)", fontsize=9)
    ax1.grid(alpha=0.3)
    ax1.legend(fontsize=7, loc="lower right")
    ax2.fill_between(env["T"], env["env_lo"], env["env_hi"], color="#1f77b4", alpha=0.3, label="slope envelope, all admitted curves")
    ax2.axhline(env["s_max"], color="#d62728", ls="--", lw=1, label=f"|slope| bound {env['s_max']:.3f} ppm/K")
    ax2.axhline(-env["s_max"], color="#d62728", ls="--", lw=1)
    ax2.set_xlabel("crystal temperature (C)")
    ax2.set_ylabel("slope (ppm/K)")
    ax2.set_title("XOSC frequency-temperature slope in service (model: E, Low)", fontsize=9)
    ax2.grid(alpha=0.3)
    ax2.legend(fontsize=7, loc="lower center")
    fig.suptitle("cwht RP2350 XOSC (ABM8-272-T3): slope bound used for the ratio drift (r3_a5.py, developer evidence)", fontsize=10)
    fig.tight_layout()
    fig.savefig(out, dpi=130)
    plt.close(fig)


def fig_budget(out: Path, s, p):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    b = s["budget"]
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.5, 4.6), gridspec_kw=dict(width_ratios=[1, 1.25]))
    labs = [f"interval 12\nkey-down, fresh ratio\n(drift {b['iv12']['drift_ppm']:.1f} ppm)",
            f"interval 13\nduring the over, aged ratio\n(drift {b['iv13']['drift_ppm']:.1f} ppm)"]
    hd = [b["iv12"]["healthy_Hz"] / 1000, b["iv13"]["healthy_Hz"] / 1000]
    ud = [b["iv12"]["undetected_Hz"] / 1000, b["iv13"]["undetected_Hz"] / 1000]
    x = np.arange(2)
    ax1.bar(x - 0.2, hd, width=0.4, label="healthy disagreement d (must be < T)")
    ax1.bar(x + 0.2, ud, width=0.4, label="largest undetected true error T + d")
    for i in range(2):
        ax1.text(x[i] - 0.2, hd[i] + 0.15, f"{hd[i]*1000:.0f}", ha="center", fontsize=8)
        ax1.text(x[i] + 0.2, ud[i] + 0.15, f"{ud[i]*1000:.0f}", ha="center", fontsize=8)
    ax1.axhline(float(T_MEAS) / 1000, color="tab:green", ls="-.", lw=1, label="measured threshold T = 5 kHz")
    ax1.axhline(float(L_154) / 1000, color="tab:red", ls="--", lw=1, label="REQ-SYS-154 10 kHz")
    ax1.set_xticks(x)
    ax1.set_xticklabels(labs, fontsize=8)
    ax1.set_ylim(0, 14.5)
    ax1.set_ylabel("carrier-referred (kHz) at 147.9988 MHz")
    ax1.set_title("Route R3 budget with the drift term split by check", fontsize=9)
    ax1.grid(alpha=0.3, axis="y")
    ax1.legend(fontsize=7, loc="upper center", ncol=2)
    # Panel 2: buffer harmonic lines vs receive windows
    wins = p["windows"]
    colors = ["#2ca02c", "#9467bd", "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22"]
    for i, (name, (a, bb)) in enumerate(wins.items()):
        lo, hi = float(a / fb.MHz), float(bb / fb.MHz)
        w = max(hi - lo, 0.4)
        ax2.barh(i, w, left=lo if hi - lo > 0.4 else lo - 0.2, color=colors[i], alpha=0.6, height=0.5)
        ax2.text(170.5, i, name, va="center", fontsize=7)
    for n in range(1, 9):
        f = n * 25.0
        if 0 <= f <= 170:
            ax2.axvline(f, color="#d62728", lw=1)
            ax2.text(f + 1, -0.55, f"{n}x25", color="#d62728", fontsize=7, ha="left")
    ax2.set_xlim(0, 215)
    ax2.set_ylim(-0.8, len(wins) - 0.4)
    ax2.set_yticks([])
    ax2.set_xlabel("frequency (MHz)")
    ax2.set_title("Receive-only TCXO buffer: 25 MHz harmonics (red) against the receive windows", fontsize=9)
    ax2.grid(alpha=0.3, axis="x")
    fig.suptitle("cwht route R3, A5: budget and receive-only buffer lines (r3_a5.py, developer evidence)", fontsize=10)
    fig.tight_layout()
    fig.savefig(out, dpi=130)
    plt.close(fig)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--run-id", required=True)
    a = ap.parse_args(argv)
    out = HERE / "results" / a.run_id
    out.mkdir(parents=True, exist_ok=True)
    res, summary, plots = run()
    lines, fails, n_pass = [], 0, 0
    for case, ok, text in res:
        tag = "INFO" if ok is None else ("PASS" if ok else "FAIL")
        lines.append(f"{tag} {case}: {text}")
        fails += ok is False
        n_pass += ok is True
    lines.append("")
    lines.append("TORNADO main-bay change over W (top 8 upward swings, K): " + "; ".join(
        f"{r['param']} {r['up_dT']:.3f}" for r in summary["freshness"]["tornado_top"]))
    lines.append(f"RESULT: {n_pass} pass, {fails} fail, {sum(1 for r in res if r[1] is None)} info")
    text = "\n".join(lines)
    print(text)
    (out / "checker-output.txt").write_text(text + "\n")
    summary["checks"] = [dict(case=c, result=("INFO" if ok is None else ("PASS" if ok else "FAIL")), text=t) for c, ok, t in res]
    summary["sources"] = SOURCES
    summary["run_id"] = a.run_id
    summary["exit_status"] = 1 if fails else 0
    (out / "results.json").write_text(json.dumps(summary, indent=1, default=float) + "\n")
    fig_relock(out / "relock-sequence.png", summary)
    fig_fresh(out / "ratio-freshness.png", summary, plots)
    fig_slope(out / "xosc-slope.png", plots)
    fig_budget(out / "r3-budget-and-buffer.png", summary, plots)
    fig_settle(out / "settle-and-guard.png", summary)
    fig_reference(out / "reference-budget-a5.png", summary)
    shutil.copy2(Path(__file__), out / Path(__file__).name)
    print(f"outputs: {out}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
