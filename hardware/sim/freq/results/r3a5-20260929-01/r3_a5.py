#!/usr/bin/env python3
"""Route R3 frequency-verification budget for A5: Si5351A relock, TCXO ratio freshness, receive-only buffer.

Product: docs/design/analysis/frequency-budget.md revision 2, section 3.4 (WP-PDR-20a, PDR work plan
revision 6 section 3.0 row 20). It answers the two TS-012 section 10 revisit conditions of revision 6
(the Si5351A PLL relock time against its 1 ms allocation; the XOSC/TCXO ratio's freshness over a long
over against its 1 ppm allocation) and re-states the route R3 budget of D-17 for A5.

Run from the repository root:

    .venv/bin/python hardware/sim/freq/r3_a5.py --run-id r3a5-20260929-01

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
T_FC0 = {iv: fb.FC0[iv][0] for iv in (12, 13, 15)}  # N: RP2350 Table 541 intervals (1 us scale, conservative)

# Route R3 budget (N unless marked)
TX_MAX = fb.TX_MAX
T_MEAS = fb.T_MEAS                     # N: measured threshold T = 5.0 kHz (SW-SAFE, WP-PDR-35)
L_154 = fb.L_154                       # R: REQ-SYS-154 10 kHz true-error limit
F_INJ = fb.F_INJ                       # R: TC-SYS-101 12 kHz injection
Q_TCXO_PPM = fb.FC0[15][1] / fb.TCXO_REF / fb.PPM   # N: 62.5 Hz at 25 MHz = 2.5 ppm ratio quantization
DRIFT_KD_ALLOC = fb.XOSC_DRIFT_R3      # N: 1 ppm XOSC drift allocation (TS-012 section 10 condition 2)

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
        lo, hi = f * (1 - TCXO_TOL_PPM * fb.PPM), f * (1 + TCXO_TOL_PPM * fb.PPM)
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
    check("KA-R2", healthy(12, DRIFT_KD_ALLOC) == fb.healthy_disagreement("R3", 12),
          f"R3 interval 12 with the 1 ppm drift reproduces frequency-budget C-12.iv12: {ceil1(healthy(12, 1))} Hz")
    check("KA-R3", l_max(12, T_RAMP_NOM + 0 * MS, g=F(3) * MS) == T_RELOCK_ALLOC,
          "TS-012 sequence: 1 ms writes and settle + 4 ms + 2 ms = PA_EN at t0 + 7 ms, 3 ms before the ramp at t0 + 10 ms")

    # ---- Relock (RL)
    tw = c6_write_time()
    twr = c6_write_time(reset=True)
    tw_std = c6_write_time(F_SCL_STD)
    trd = lol_read_time()
    rmax = ramp_limit()
    lm12_nom = l_max(12, T_RAMP_NOM)
    lm12_max = l_max(12, rmax)
    lm13_max = l_max(13, rmax)
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
    check("RL-4", lm12_nom >= T_RELOCK_ALLOC, f"largest writes-plus-settle time L with interval 12 and the TS-012 ramp at t0 + 10 ms "
          f"(PA_EN no later than TX_KEY at t0 + 8 ms) = {float(lm12_nom/MS):.3f} ms >= 1 ms allocation (slack {float((lm12_nom-T_RELOCK_ALLOC)/MS):.3f} ms)")
    check("RL-5", lm12_max == T_REVISIT, f"with the ramp moved to its limit t0 + {float(rmax/MS):.0f} ms (REQ-SYS-161 12 ms, REQ-SYS-160 "
          f"15 - 3 ms): L max = {float(lm12_max/MS):.3f} ms, which is the TS-012 revisit threshold 1 + 3 ms")
    check("RL-6", lm13_max <= 0, f"interval 13 at the changeover (the TS-012 fallback) leaves L max = {float(lm13_max/MS):.3f} ms with the "
          "2 ms drive power-up before the ramp: the fallback cannot absorb any relock time (finding for WP-PDR-23a)")
    settle_nom = lm12_nom - tw
    settle_max = lm12_max - tw
    check("RL-7a", T_FREQ_MAX <= T_RELOCK_ALLOC - tw, f"if TFREQ bounds the MSNA retune: settle {float(T_FREQ_MAX/MS):.3f} ms <= "
          f"{floor3((T_RELOCK_ALLOC-tw)/MS)} ms left in the 1 ms allocation after the writes")
    info("RL-7b", f"if only TRDY bounds it: {float(T_RDY_MAX/MS):.0f} ms > {floor3(settle_max/MS)} ms, the largest settle time any "
                  f"sequence inside REQ-SYS-161 allows (and > {floor3(settle_nom/MS)} ms with the TS-012 ramp): the TS-012 revisit "
                  "condition would trigger. The source neither confirms nor excludes it")
    info("RL-8", "verdict: the 1 ms allocation is NOT CONFIRMED by a source (the relock time is not specified). The frequency check is "
                 "self-validating (a PLL still settling gives a count outside T and PA_EN stays low), so the relock time bounds "
                 "availability (a late or lost first element), not safety. Design response: lock-gated start of the interval-12 count "
                 f"with a deadline of t0 + {float(lm12_nom/MS):.1f} ms for the writes and the settle (TS-012 ramp kept); closure by the "
                 "dev-board measurement M-1")

    # ---- Freshness (FR)
    env = xo_slope_envelope()
    s_max = env["s_max"]
    check("FR-1", env["n_admissible"] > 0, f"AT-cut curves inside the Table 596 +/-30 ppm band: {env['n_admissible']} admitted; "
          f"largest |slope| over {T_XO_OPER[0]:.0f} to {T_XO_OPER[1]:.0f} C = {ceil3(s_max)} ppm/K (a1 {env['arg']['a1']:.3f}, "
          f"a3 {env['arg']['a3']:.2e}, Ti {env['arg']['ti']:.1f} C, at {env['arg']['t_at']:.1f} C)")
    dT_local = DP_PICO * RTH_PICO
    rate_local = dT_local / TAU_PICO_MIN

    # key-down age A_kd: the largest ratio age for which the drift stays within the 1 ppm allocation
    bb_short = bay_band(60.0)
    rate_bay = bb_short["base_rate"] + bb_short["band_rate"]
    rate_tot = rate_bay + rate_local
    a_kd_limit = (float(DRIFT_KD_ALLOC) - float(PUSH_PPM)) / (s_max * rate_tot)
    a_kd = math.floor(a_kd_limit)  # proposed value, whole seconds, rounded down
    d_kd = s_max * rate_tot * a_kd + float(PUSH_PPM)
    check("FR-2", d_kd <= float(DRIFT_KD_ALLOC), f"key-down check (interval 12) on a ratio no older than A_kd = {a_kd} s: drift "
          f"{ceil3(s_max)} ppm/K x ({ceil3(rate_bay)} K/s bay + {ceil3(rate_local)} K/s local) x {a_kd} s + {float(PUSH_PPM)} ppm "
          f"pushing = {ceil3(d_kd)} ppm <= 1 ppm allocation (A_kd limit {floor1(a_kd_limit)} s)")
    check("FR-2r", float(T_REFRESH) + float(T_BUF_SETTLE + T_FC0[15]) <= a_kd,
          f"in receive the ratio is at most {float(T_REFRESH) + float(T_BUF_SETTLE + T_FC0[15]):.3f} s old (1 s refresh + "
          f"{float((T_BUF_SETTLE + T_FC0[15])/MS):.1f} ms buffer settle and interval-15 count) <= A_kd")

    W = float(T_OVER_MAX) + a_kd
    bb = bay_band(W)
    dT_bay = bb["base_dT"] + bb["band_dT"]
    d_over = s_max * (dT_bay + dT_local) + float(PUSH_PPM)
    info("FR-3", f"window W = A_kd {a_kd} s + longest over {float(T_OVER_MAX):.0f} s (REQ-SYS-180) = {W:.0f} s; main-bay change "
          f"nominal {ceil3(bb['base_dT'])} K ({bb['worst_key'][0]}, {bb['worst_key'][1]:.0f} C) + band {ceil3(bb['band_dT'])} K = "
          f"{ceil3(dT_bay)} K; local Pico 2 step {ceil3(dT_local)} K")
    info("FR-4", f"XOSC drift bound over the longest over = {ceil3(s_max)} x ({ceil3(dT_bay)} + "
          f"{ceil3(dT_local)}) K + {float(PUSH_PPM)} = {ceil3(d_over)} ppm > the 1 ppm allocation: the TS-012 condition 'ratio fresh "
          "over a long over within 1 ppm' is NOT met as worded (revisit condition triggered)")
    dc12 = drift_ceiling(12)
    dc13 = drift_ceiling(13)
    info("FR-5", f"the aged ratio cannot serve an interval-12 check: drift ceiling at interval 12 = {floor3(dc12)} ppm "
          f"< {ceil3(d_over)} ppm (so interval 12 is used only on a ratio no older than A_kd)")
    d13_alloc = F(math.ceil(d_over * 2) , 2)  # proposed allocation: the bound rounded up to 0.5 ppm
    check("FR-6", d13_alloc <= dc13, f"during the over (interval 13) the aged ratio is inside the drift ceiling {floor3(dc13)} ppm; "
          f"proposed allocation {float(d13_alloc)} ppm (bound {ceil3(d_over)} ppm rounded up to 0.5 ppm), margin to the ceiling "
          f"{floor3(dc13 - d13_alloc)} ppm")

    # ---- Budget (B), with the split drift
    for iv, dr, use in ((12, DRIFT_KD_ALLOC, "key-down check before PA_EN, ratio age <= A_kd"),
                        (13, d13_alloc, "checks during the over, ratio from before the over")):
        d = healthy(iv, dr)
        check(f"B-12.iv{iv}", d < T_MEAS, f"{use}: healthy disagreement {ceil1(d)} Hz < T 5000 Hz (margin {floor1(T_MEAS-d)} Hz)")
        check(f"B-16.iv{iv}", T_MEAS + d <= L_154, f"{use}: largest undetected true error {ceil1(T_MEAS+d)} Hz <= REQ-SYS-154 10 kHz "
              f"(margin {floor1(L_154-T_MEAS-d)} Hz)")
        check(f"B-18.iv{iv}", F_INJ - d > T_MEAS, f"{use}: TC-SYS-101 12 kHz injection measures >= {floor1(F_INJ-d)} Hz > T (margin "
              f"{floor1(F_INJ-d-T_MEAS)} Hz)")
    check("B-15", fb.tx_detection_time(13) <= fb.T_LIMIT, f"fault during transmission detected and RF off in {float(fb.tx_detection_time(13)/MS):.0f} ms <= 100 ms")
    check("B-11", TX_MAX / fb.PRESCALE < fb.GPIN_MAX and fb.TCXO_REF < fb.GPIN_MAX,
          "GPIN0 carrier/8 18.50 MHz and GPIN1 TCXO 25.000 MHz are both below the 50 MHz GPIN limit")
    t_refresh = T_BUF_SETTLE + T_FC0[15]
    check("B-19", t_refresh < T_REFRESH, f"ratio refresh in receive: buffer settle {float(T_BUF_SETTLE/MS):.0f} ms + interval 15 "
          f"{float(T_FC0[15]/MS):.1f} ms = {float(t_refresh/MS):.1f} ms per refresh (buffer on {float(t_refresh/T_REFRESH*100):.1f} % of receive)")

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
                    settle_left_in_alloc_ms=float((T_RELOCK_ALLOC - tw) / MS), settle_max_ramp10_ms=float(settle_nom / MS),
                    settle_max_ramp12_ms=float(settle_max / MS), tfreq_ms=float(T_FREQ_MAX / MS), trdy_max_ms=float(T_RDY_MAX / MS),
                    trdy_typ_ms=float(T_RDY_TYP / MS), verdict="1 ms allocation not confirmed by a source; lock-gated start; closure by M-1"),
        freshness=dict(s_max_ppm_per_K=s_max, s_arg=env["arg"], n_admissible=env["n_admissible"], rate_bay_K_s=rate_bay,
                       rate_local_K_s=rate_local, A_kd_s=a_kd, A_kd_limit_s=a_kd_limit, drift_kd_ppm=d_kd, window_s=W,
                       dT_bay_nominal_K=bb["base_dT"], dT_bay_band_K=bb["band_dT"], dT_bay_worst_case=list(bb["worst_key"]),
                       dT_local_K=dT_local, drift_over_ppm=d_over, drift_ceiling_iv12_ppm=float(dc12),
                       drift_ceiling_iv13_ppm=float(dc13), drift_alloc_iv13_ppm=float(d13_alloc),
                       tornado_top=bb["tornado"][:8],
                       cases={f"{k[0]} {k[1]:.0f} C": dict(rise=v["rise"], fall=v["fall"], rate=v["rate"]) for k, v in bb["cases"].items()},
                       verdict="1 ppm over the longest over not met; budget closes with A_kd on the key-down check and the interval-13 allocation"),
        budget={f"iv{iv}": dict(healthy_Hz=float(healthy(iv, dr)), margin_T_Hz=float(T_MEAS - healthy(iv, dr)),
                                undetected_Hz=float(T_MEAS + healthy(iv, dr)), drift_ppm=float(dr))
                for iv, dr in ((12, DRIFT_KD_ALLOC), (13, d13_alloc))},
        buffer_lines=lines,
    )
    plots = dict(env=env, bb=bb, bb_short=bb_short, W=W, a_kd=a_kd, d_over=d_over, d13=float(d13_alloc), dc12=float(dc12),
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
        (f"latest, ramp kept at 10 ms (L = {r['L_max_iv12_ramp10_ms']:.1f} ms)", r["L_max_iv12_ramp10_ms"], 12, 10.0),
        (f"latest, ramp at 12 ms limit (L = {r['L_max_iv12_ramp12_ms']:.1f} ms)", r["L_max_iv12_ramp12_ms"], 12, 12.0),
        ("interval-13 fallback, L = 1 ms (infeasible)", 1.0, 13, 12.0),
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
    ax1.text(float(T_LEADIN / MS) + 0.1, -0.45, "REQ-SYS-161 12 ms", color="red", fontsize=7)
    ax1.set_xlim(0, 22)
    ax1.set_yticks([])
    ax1.set_xlabel("time after the changeover command t0 (ms)")
    ax1.set_title("Key-down sequence: C6 I2C writes at 400 kHz (dark blue), PLL settle (light blue), FC0 count (green), "
                  "software 2 ms (orange);\nPA_EN (triangle; red = later than 2 ms before the ramp), ramp start (purple bar)", fontsize=9)
    ax1.grid(alpha=0.3, axis="x")
    # Panel 2: sourced bounds against the settle budget (log)
    items = [
        ("TFREQ max (DS Table 5), if it covers an MSNA change", r["tfreq_ms"], "#2ca02c"),
        ("settle left in the 1 ms allocation after the writes", r["settle_left_in_alloc_ms"], "#1f77b4"),
        ("largest settle, TS-012 ramp kept at 10 ms", r["settle_max_ramp10_ms"], "#1f77b4"),
        ("largest settle, ramp at the 12 ms limit (TS-012 revisit threshold)", r["settle_max_ramp12_ms"], "#1f77b4"),
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
    drift = np.minimum(p["s_max"] * p["rate_tot"] * ages, p["s_max"] * (top + p["dT_local"])) + float(PUSH_PPM)
    ax2.plot(ages, drift, color="#1f77b4", lw=1.8, label="XOSC drift bound since the last refresh")
    ax2.axhline(1.0, color="#2ca02c", ls="--", lw=1, label="1 ppm allocation (key-down check, interval 12)")
    ax2.axhline(p["dc12"], color="#2ca02c", ls=":", lw=1, label=f"interval-12 ceiling {p['dc12']:.2f} ppm (zero margin)")
    ax2.axhline(p["d13"], color="#ff7f0e", ls="--", lw=1, label=f"proposed interval-13 allocation {p['d13']:.1f} ppm")
    ax2.axhline(p["dc13"], color="#ff7f0e", ls=":", lw=1, label=f"interval-13 ceiling {p['dc13']:.2f} ppm (zero margin)")
    ax2.axvline(p["a_kd"], color="gray", ls="-.", lw=1)
    ax2.text(p["a_kd"] + 2, 12.5, f"A_kd = {p['a_kd']} s", fontsize=8)
    ax2.plot([p["W"]], [p["d_over"]], "o", color="#d62728")
    ax2.annotate(f"{p['d_over']:.2f} ppm at W", xy=(p["W"], p["d_over"]), xytext=(p["W"] - 80, p["d_over"] + 3.0), fontsize=8,
                 arrowprops=dict(arrowstyle="->", lw=0.8))
    ax2.set_xlabel("ratio age at the check (s)")
    ax2.set_ylabel("XOSC drift (ppm)")
    ax2.set_ylim(0, 20)
    ax2.set_title("TCXO ratio freshness: drift bound against the allocations\n(interval 12 only on a fresh ratio; interval 13 during the over)", fontsize=9)
    ax2.grid(alpha=0.3)
    ax2.legend(fontsize=7, loc="upper left")
    fig.suptitle("cwht route R3, A5: XOSC/TCXO ratio freshness over the longest over (r3_a5.py, developer evidence)", fontsize=10)
    fig.tight_layout()
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
    shutil.copy2(Path(__file__), out / Path(__file__).name)
    print(f"outputs: {out}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
