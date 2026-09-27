#!/usr/bin/env python3
"""Frequency error budget, band-edge guard and frequency-verification counter checker.

Product: docs/design/analysis/frequency-budget.md (WP-PDR-20, PDR work plan section 3.6).
Run from the repository root:

    .venv/bin/python hardware/sim/freq/freq_budget.py            # check, print, exit status
    .venv/bin/python hardware/sim/freq/freq_budget.py --plot     # also render the figure

Exit status 0 when every assertion of section "ASSERTIONS" holds, 1 otherwise.
Arithmetic uses fractions.Fraction (exact); printed values are rounded toward the limit
(a margin is floored, a sum is ceiled) at 0.1 Hz or 0.001 ppm.

Tool status (05 section 9.1): this script is a class B evidence-generating tool with no TV
record; its output is developer evidence until a TV record covers it or the owner rules on it
(peer-review-checklist-analysis CK-ANA-C2). Interpreter: the TV-001 venv Python 3.13.5; the
checker uses only the standard library (fractions, math, argparse); matplotlib renders the
figure and produces no number.

Every input constant carries its source in the comment next to it.
"""
from __future__ import annotations

import argparse
import math
import sys
from fractions import Fraction as F
from pathlib import Path

MHz = F(10**6)
kHz = F(10**3)
PPM = F(1, 10**6)

# ----------------------------------------------------------------------------------------
# INPUTS (source next to each value)
# ----------------------------------------------------------------------------------------
BAND_LO = 144 * MHz                  # 47 CFR 97.301(a) (corpus 47cfr-97.301.md line 26): 144-148 MHz
BAND_HI = 148 * MHz
CW_SEG_HI = F("144.1") * MHz         # 47 CFR 97.305(a), (c) (corpus 47cfr-97.305.md lines 17, 58): 144.1-148 non-CW
TX_MIN = F("144.0012") * MHz         # REQ-SYS-008, REQ-SYS-009, REQ-TX-002 (TBR): 1.2 kHz guard, SRR decision 25
TX_MAX = F("147.9988") * MHz
REF_CEIL_PPM = F("2.5")              # REQ-SYS-010 (TBR), ADR-023 item (1): +/-2.5 ppm total after calibration
SB60_OFFSET = F(750)                 # REQ-TX-006 (TBR, WP-PDR-22 confirms): -60 dB keying-sideband offset, Hz
BW26_HALF = F(350, 2)                # REQ-SYS-015 (TBR): 26 dB bandwidth <= 350 Hz, half each side, Hz
E_WORD = F(5)                        # ALLOCATION (this note): frequency-word quantization and rounding, Hz
F7_OFFSETS = [F(614), F(735), F(750)]  # docs/research/regulatory-corpus-and-operators.md F7: -60 dB point cases

# Reference (TCXO) allocations for the budget identities (section 4 of the note). Engineering
# allocations, not datasheet values: the TS-007 reference criterion R-M3 turns them into the
# datasheet acceptance test for the part chosen at CDR.
UNCAL_TOTAL_PPM = F("1.5")           # ALLOCATION: TCXO initial + reflow + temperature (-10 to +45 C) + 1 yr aging + supply and load
CAL_RANGE_PPM = F("0.9")             # ALLOCATION: firmware calibration-constant range (SW-SYNTH bound), +/-
U_CAL_PPM = F("0.1")                 # ALLOCATION: calibration uncertainty (zero-beat against a reference, RSK-002 S4)
AGING_PPM = F("0.5")                 # ALLOCATION: 1 yr aging inside UNCAL_TOTAL, used for the calibrated case
SUPPLY_LOAD_PPM = F("0.1")           # ALLOCATION: supply and load pull inside UNCAL_TOTAL
TEMP_CLASSES_PPM = [F("0.1"), F("0.25"), F("0.5")]  # docs/research/2m-cw-transceiver-reference-designs.md F21 (Medium)
HALF_PASSBAND = F(250)               # RSK-002: 500 Hz CW filter half-bandwidth, Hz
F_REF_TWO_UNIT = 146 * MHz           # RSK-002 and TPM-006 report Hz at 146 MHz

# Frequency-verification counter (REQ-SYS-154, REQ-SYS-182, REQ-TX-013; HZ-008 K7)
W_WINDOW = 10 * kHz                  # REQ-SYS-182 (TBR, SRR decision 40): measured agreement window
L_154 = 10 * kHz                     # REQ-SYS-154 (TBR, SRR decision 40): true-error limit ("off its set frequency by over 10 kHz")
T_MEAS = 5 * kHz                     # PROPOSAL (INSP-056 finding-1 fix option (a)): measured detection threshold of SW-SAFE,
                                     # a distinct L2 value: healthy disagreement < T_MEAS and T_MEAS + healthy <= L_154
F_INJ = 12 * kHz                     # REQ-SYS-154 and REQ-SYS-182 verification notes, TC-SYS-101: injected 12 kHz offset
T_LOCK_POLL = F(10, 1000)            # ALLOCATION (INSP-056 finding-2): lock-detect indication sampled at least every service
                                     # period during transmission (WP-PDR-32 timing analysis confirms), s
T_LIMIT = F(100, 1000)               # REQ-SYS-182 (TBR): RF withheld or ended within 100 ms, s
T_RF_OFF = F(20, 1000)               # REQ-SYS-004 (TBR): RF-off within 20 ms of detection, s
T_LEADIN = F(12, 1000)               # REQ-SYS-161 via ADR-026 (TBR): lead-in <= 12 ms after RX-to-TX changeover, s
T_SW = F(2, 1000)                    # ALLOCATION: software start/read/compare latency of the check at changeover, s
T_TASK = F(10, 1000)                 # ALLOCATION: service period of the SW-SAFE check during transmit, s
T_RETUNE = {"A1": F(0), "A2": F(15, 10000)}  # A1: TX on its own Si5351 PLL, no retune; A2: LMX2571 FastLock < 1.5 ms (F20)
PRESCALE = 8                         # PROPOSAL (this note): hardware divide-by-8 on the carrier sample
SAMPLE_CEIL = 20 * MHz               # REQ-TX-013 (TBR): sample below 20 MHz
GPIN_MAX = 50 * MHz                  # RP2350 datasheet section 8.1.1.4: GPIN0-GPIN1 limited to 50 MHz
# RP2350 datasheet section 8.1.3 Table 541: FC0_INTERVAL -> (interval s, accuracy Hz at the counted input)
FC0 = {12: (F(4, 1000), F(500)), 13: (F(8, 1000), F(250)), 14: (F(16, 1000), F(125)), 15: (F(32, 1000), F("62.5"))}
FC0_SCALE = F(98, 100)               # Table 582: "0.98us * 2**interval, but let's call it 1us"; the budget uses 1.0 (longer)
# RP2350 datasheet section 8.2.1.1 Table 596 (Pico 2 crystal ABM8-272-T3): tolerance, stability, first-year aging
XOSC_TOL, XOSC_STAB, XOSC_AGE = F(30), F(30), F(5)
TCXO_REF = 25 * MHz                  # TS-007 recommendation and clock plan: 25.000 MHz reference
TCXO_CAL_INTERVAL = 15               # route R3: TCXO counted during receive at interval 15
XOSC_DRIFT_R3 = F(1)                 # ALLOCATION: XOSC drift between two TCXO refreshes (<= 1 s apart), ppm
IV_CHANGEOVER = 12                   # PROPOSAL: FC0 interval of the check before PA_EN (4 ms)
IV_TRANSMIT = 13                     # PROPOSAL: FC0 interval of the repeated check during transmit (8 ms)
TCXO_PLAUS_PPM = XOSC_TOL + XOSC_STAB + XOSC_AGE + REF_CEIL_PPM  # route R3 plausibility bound on the XOSC/TCXO ratio


def hz(x: F) -> float:
    return float(x)


def floor1(x: F) -> float:
    """Round toward minus infinity at 0.1 (used for margins)."""
    return math.floor(float(x) * 10) / 10


def ceil1(x: F) -> float:
    """Round toward plus infinity at 0.1 (used for sums compared with a ceiling)."""
    return math.ceil(float(x) * 10) / 10


def ceil3(x: F) -> float:
    return math.ceil(float(x) * 1000) / 1000


def floor3(x: F) -> float:
    return math.floor(float(x) * 1000) / 1000


# ----------------------------------------------------------------------------------------
# 1. Band-edge guard arithmetic (REQ-SYS-008, 009, 010; REQ-TX-002, 006; ADR-023)
# ----------------------------------------------------------------------------------------
def edge_margins(offset: F, ppm: F = REF_CEIL_PPM, e_word: F = E_WORD):
    """Margins (Hz) of the lowest and highest emission point against the band edges.

    Lower edge: carrier at TX_MIN, reference error -ppm, word error -e_word, sideband -offset.
    Upper edge: carrier at TX_MAX, reference error +ppm, word error +e_word, sideband +offset.
    Convention: margin = distance inside the band (positive passes).
    """
    lo_point = TX_MIN - TX_MIN * ppm * PPM - e_word - offset
    hi_point = TX_MAX + TX_MAX * ppm * PPM + e_word + offset
    return lo_point - BAND_LO, BAND_HI - hi_point


def max_offset_supported(ppm: F = REF_CEIL_PPM, e_word: F = E_WORD) -> F:
    """Largest -60 dB offset the 1.2 kHz guard supports at both edges (upper edge governs)."""
    lo = (TX_MIN - BAND_LO) - TX_MIN * ppm * PPM - e_word
    hi = (BAND_HI - TX_MAX) - TX_MAX * ppm * PPM - e_word
    return min(lo, hi)


def max_ppm_supported(offset: F = SB60_OFFSET, e_word: F = E_WORD) -> F:
    lo = ((TX_MIN - BAND_LO) - e_word - offset) / (TX_MIN * PPM)
    hi = ((BAND_HI - TX_MAX) - e_word - offset) / (TX_MAX * PPM)
    return min(lo, hi)


# ----------------------------------------------------------------------------------------
# 2. Reference budget identities (REQ-SYS-010, TPM-006, RSK-002)
# ----------------------------------------------------------------------------------------
def e_word_ppm() -> F:
    return E_WORD / (TX_MAX * PPM)


def guard_identity() -> F:
    """Worst case with a wrong calibration inside its range: UNCAL + CAL_RANGE + word."""
    return UNCAL_TOTAL_PPM + CAL_RANGE_PPM + e_word_ppm()


def calibrated_total(temp_ppm: F, aging: F = AGING_PPM) -> F:
    """REQ-SYS-010 case: after calibration the initial and reflow terms are removed."""
    return U_CAL_PPM + temp_ppm + aging + SUPPLY_LOAD_PPM + e_word_ppm()


def two_unit_offset_hz(temp_ppm: F, aging: F) -> F:
    per_unit = U_CAL_PPM + temp_ppm + aging + SUPPLY_LOAD_PPM
    return 2 * per_unit * F_REF_TWO_UNIT * PPM + 2 * E_WORD


# ----------------------------------------------------------------------------------------
# 3. Frequency-verification counter (REQ-SYS-154, 182; REQ-TX-013)
# ----------------------------------------------------------------------------------------
def fc0_quant_carrier(interval: int) -> F:
    return FC0[interval][1] * PRESCALE


def healthy_disagreement(route: str, interval: int) -> F:
    """Largest |measured - set| (Hz, carrier referred) of a fault-free unit at TX_MAX."""
    q = fc0_quant_carrier(interval)
    ref = TX_MAX * REF_CEIL_PPM * PPM          # true carrier vs set: the TCXO error
    if route == "R1":                           # raw XOSC timebase (HZ-008 K7 text as written)
        xo = TX_MAX * (XOSC_TOL + XOSC_STAB + XOSC_AGE) * PPM
        return q + ref + xo
    if route == "R3":                           # XOSC timebase corrected by a TCXO count taken in receive
        q_t = FC0[TCXO_CAL_INTERVAL][1] / TCXO_REF    # relative quantization of the TCXO count
        drift = XOSC_DRIFT_R3 * PPM
        return q + TX_MAX * (q_t + drift)       # the TCXO error cancels: the ratio is exact in a healthy unit
    raise ValueError(route)


def undetected_bound(route: str, interval: int, window: F = T_MEAS) -> F:
    """Largest true synthesizer error (single fault in the frequency word or PLL) that can pass a
    measured threshold `window` (default: the proposed SW-SAFE threshold T_MEAS)."""
    q = fc0_quant_carrier(interval)
    if route == "R1":
        return window + q + TX_MAX * (XOSC_TOL + XOSC_STAB + XOSC_AGE) * PPM
    if route == "R3":
        return window + healthy_disagreement("R3", interval)
    raise ValueError(route)


def min_window(route: str, interval: int) -> F:
    return healthy_disagreement(route, interval)


def min_154_limit(route: str, interval: int) -> F:
    """Smallest REQ-SYS-154 true-error limit a threshold that never trips a healthy unit can meet:
    the threshold must exceed the healthy disagreement, so the limit is the undetected bound at it."""
    return undetected_bound(route, interval, window=healthy_disagreement(route, interval))


def fc0_accuracy_ceiling(interval: int, threshold: F = T_MEAS) -> F:
    """Largest FC0 accuracy (Hz at the counted input) for which R3 still meets both threshold
    conditions: 8a + rest < T and T + 8a + rest <= L_154."""
    rest = healthy_disagreement("R3", interval) - fc0_quant_carrier(interval)
    return min(threshold - rest, L_154 - threshold - rest) / PRESCALE


def changeover_time(alt: str, interval: int) -> F:
    return T_RETUNE[alt] + FC0[interval][0] + T_SW


def tx_detection_time(interval: int) -> F:
    """Fault during transmit: at most two back-to-back intervals, the service period, then RF off."""
    return 2 * FC0[interval][0] + T_TASK + T_RF_OFF


# ----------------------------------------------------------------------------------------
# ASSERTIONS
# ----------------------------------------------------------------------------------------
def run_checks(verbose: bool = True) -> list[tuple[str, bool, str]]:
    res: list[tuple[str, bool, str]] = []

    def check(case: str, ok: bool, text: str):
        res.append((case, ok, text))

    def info(case: str, text: str):
        res.append((case, None, text))

    # Known-answer self test (hand arithmetic of the note section 3.1, and of SRR decision 25)
    lo_m, hi_m = edge_margins(SB60_OFFSET, e_word=F(0))
    check("KA-1", floor1(hi_m) == 80.0, f"upper -60 dB margin with no word error = {floor1(hi_m)} Hz (hand: 1200-370-750 = 80)")
    check("KA-2", abs(hz(TX_MAX * REF_CEIL_PPM * PPM) - 369.997) < 0.001, "2.5 ppm at 147.9988 MHz = 369.997 Hz")
    check("KA-3", fc0_quant_carrier(13) == 2000, "FC0 interval 13 accuracy 250 Hz x 8 = 2000 Hz at the carrier")

    # C-1 .. C-4: band-edge cases (both edges, the governing -60 dB point and the 26 dB half-bandwidth)
    lo_m, hi_m = edge_margins(SB60_OFFSET)
    check("C-1", lo_m > 0, f"lower edge -60 dB point margin {floor1(lo_m)} Hz (REQ-SYS-008, REQ-TX-006)")
    check("C-2", hi_m > 0, f"upper edge -60 dB point margin {floor1(hi_m)} Hz (REQ-SYS-008, REQ-TX-006)")
    lo26, hi26 = edge_margins(BW26_HALF)
    check("C-3", lo26 > 0, f"lower edge 26 dB half-bandwidth margin {floor1(lo26)} Hz (REQ-SYS-015)")
    check("C-4", hi26 > 0, f"upper edge 26 dB half-bandwidth margin {floor1(hi26)} Hz (REQ-SYS-015)")
    mo = max_offset_supported()
    check("C-5", mo >= SB60_OFFSET, f"largest REQ-TX-006 offset the 1.2 kHz guard supports = {floor1(mo)} Hz")
    mp = max_ppm_supported()
    check("C-6", mp >= REF_CEIL_PPM, f"largest reference error the guard supports at 750 Hz = {floor3(mp)} ppm")
    for i, off in enumerate(F7_OFFSETS, start=1):
        a, b = edge_margins(off)
        check(f"C-7.{i}", min(a, b) > 0, f"F7 offset {int(off)} Hz: min edge margin {floor1(min(a, b))} Hz")

    # C-8 .. C-10: reference identities (REQ-SYS-010, TPM-006)
    gi = guard_identity()
    check("C-8", gi <= REF_CEIL_PPM, f"guard identity UNCAL {float(UNCAL_TOTAL_PPM)} + CAL {float(CAL_RANGE_PPM)} + word {ceil3(e_word_ppm())} = {ceil3(gi)} ppm <= 2.5 ppm")
    check("C-9", CAL_RANGE_PPM <= UNCAL_TOTAL_PPM, "calibration range does not exceed the uncalibrated total it corrects")
    for i, t in enumerate(TEMP_CLASSES_PPM, start=1):
        ct = calibrated_total(t)
        check(f"C-10.{i}", ct <= REF_CEIL_PPM, f"calibrated total, {float(t)} ppm temperature class = {ceil3(ct)} ppm <= 2.5 ppm (REQ-SYS-010)")
        check(f"C-10.{i}u", AGING_PPM + SUPPLY_LOAD_PPM + t <= UNCAL_TOTAL_PPM,
              f"{float(t)} ppm class leaves {floor3(UNCAL_TOTAL_PPM - AGING_PPM - SUPPLY_LOAD_PPM - t)} ppm for initial and reflow inside the 1.5 ppm uncalibrated allocation")

    # C-11: counter sample (REQ-TX-013) and GPIN limit
    smax = TX_MAX / PRESCALE
    check("C-11", smax < SAMPLE_CEIL and smax < GPIN_MAX, f"prescaled sample max {float(smax/MHz):.6f} MHz < 20 MHz (REQ-TX-013) and < 50 MHz (GPIN)")
    check("C-11b", (TX_MIN / PRESCALE) > 0, f"prescaled sample min {float(TX_MIN/PRESCALE/MHz):.6f} MHz")

    # C-12 .. C-18: frequency verification threshold, true-error limit and times (REQ-SYS-182, 154)
    check("C-12w", T_MEAS <= W_WINDOW, f"measured threshold T = {float(T_MEAS)} Hz <= REQ-SYS-182 10 kHz window: RF only on measured agreement within 10 kHz")
    for iv, use in ((IV_CHANGEOVER, "changeover check before PA_EN"), (IV_TRANSMIT, "check during transmit")):
        hd3 = healthy_disagreement("R3", iv)
        check(f"C-12.iv{iv}", hd3 < T_MEAS, f"R3 {use}, interval {iv}: healthy disagreement {ceil1(hd3)} Hz < T {float(T_MEAS)} Hz, no false trip (margin {floor1(T_MEAS-hd3)} Hz)")
        ub = undetected_bound("R3", iv)
        check(f"C-16.iv{iv}", ub <= L_154, f"R3 {use}, interval {iv}: largest undetected true error T + healthy = {ceil1(ub)} Hz <= REQ-SYS-154 10 kHz (margin {floor1(L_154-ub)} Hz)")
        inj = F_INJ - hd3
        check(f"C-18.iv{iv}", inj > T_MEAS, f"R3 {use}, interval {iv}: TC-SYS-101 12 kHz injection measures at least {floor1(inj)} Hz > T, trips (margin {floor1(inj-T_MEAS)} Hz)")
        hd1 = healthy_disagreement("R1", iv)
        info(f"C-13.iv{iv}", f"R1 (raw XOSC) {use}, interval {iv}: healthy disagreement {ceil1(hd1)} Hz; no threshold meets both conditions with REQ-SYS-154 at 10 kHz; "
                             f"smallest REQ-SYS-154 limit R1 supports = {ceil1(min_154_limit('R1', iv))} Hz, smallest REQ-SYS-182 window {ceil1(hd1)} Hz")
    info("C-16a", f"FC0 accuracy ceiling at the counted input for R3 with T = {float(T_MEAS)} Hz: interval {IV_CHANGEOVER} {floor1(fc0_accuracy_ceiling(IV_CHANGEOVER))} Hz "
                  f"(Table 541: {float(FC0[IV_CHANGEOVER][1])} Hz), interval {IV_TRANSMIT} {floor1(fc0_accuracy_ceiling(IV_TRANSMIT))} Hz (Table 541: {float(FC0[IV_TRANSMIT][1])} Hz)")
    for alt in ("A1", "A2"):
        t = changeover_time(alt, IV_CHANGEOVER)
        check(f"C-14.{alt}", t <= T_LEADIN, f"{alt} changeover check (retune + FC0 interval {IV_CHANGEOVER} + software) = {float(t*1000):.2f} ms <= 12 ms lead-in (margin {float((T_LEADIN-t)*1000):.2f} ms)")
    td = tx_detection_time(IV_TRANSMIT)
    check("C-15", td <= T_LIMIT, f"transmit detection + RF off = {float(td*1000):.1f} ms <= 100 ms (margin {float((T_LIMIT-td)*1000):.1f} ms)")
    # U-1, U-2: REQ-SYS-154 "unlocked" trigger (INSP-056 finding-2)
    for alt in ("A1", "A2"):
        t = changeover_time(alt, IV_CHANGEOVER)
        check(f"U-1.{alt}", t <= T_LEADIN, f"{alt} unlocked at key-down: lock-detect read after the last write and before PA_EN inside the 2 ms software allocation, "
                                           f"with the FC0 interval {IV_CHANGEOVER} check as the second means: {float(t*1000):.2f} ms <= 12 ms lead-in")
    tu = T_LOCK_POLL + T_RF_OFF
    check("U-2", tu <= T_LIMIT and tu <= td, f"unlocked during transmission: lock-detect sample period {float(T_LOCK_POLL*1000):.0f} ms + RF off {float(T_RF_OFF*1000):.0f} ms (REQ-SYS-004) = "
                                              f"{float(tu*1000):.1f} ms <= 100 ms (REQ-SYS-182 time) and <= the FC0 path C-15 {float(td*1000):.1f} ms (margin {float((T_LIMIT-tu)*1000):.1f} ms)")
    info("C-17", f"R3 plausibility bound on the XOSC/TCXO ratio = +/-{float(TCXO_PLAUS_PPM)} ppm")
    return res


def report(res) -> int:
    fails = 0
    for case, ok, text in res:
        tag = "INFO" if ok is None else ("PASS" if ok else "FAIL")
        print(f"{tag} {case}: {text}")
        fails += (ok is False)
    # Tables the note reproduces
    print("\nTABLE two-unit offset after calibration (RSK-002), Hz at 146 MHz:")
    for t in TEMP_CLASSES_PPM:
        for age in (F(0), AGING_PPM):
            v = two_unit_offset_hz(t, age)
            print(f"  temp {float(t)} ppm, aging {float(age)} ppm: {ceil1(v)} Hz vs half-passband 250 Hz -> {'inside' if v <= HALF_PASSBAND else 'outside'}")
    print("\nTABLE counter routes (carrier referred, Hz, TX_MAX):")
    for route in ("R1", "R3"):
        for iv in (12, 13, 14):
            print(f"  {route} interval {iv}: healthy {ceil1(healthy_disagreement(route, iv))}, min threshold {ceil1(min_window(route, iv))}, "
                  f"undetected at T = 5 kHz {ceil1(undetected_bound(route, iv))} ({'T valid' if healthy_disagreement(route, iv) < T_MEAS else 'T below healthy: false trips'}), "
                  f"smallest REQ-SYS-154 limit {ceil1(min_154_limit(route, iv))}")
    print("\nTABLE R3 threshold interval (Hz): healthy < T <= 10 kHz - healthy")
    for iv in (12, 13):
        hd = healthy_disagreement("R3", iv)
        print(f"  interval {iv}: {ceil1(hd)} < T <= {floor1(L_154 - hd)}; proposed T = {float(T_MEAS)}")
    print("\nTABLE changeover time (ms) by interval:")
    for alt in ("A1", "A2"):
        print("  " + alt + ": " + ", ".join(f"iv{iv} {float(changeover_time(alt, iv)*1000):.2f}" for iv in (12, 13, 14)))
    n_pass = sum(1 for r in res if r[1] is True)
    print(f"\nRESULT: {n_pass} pass, {fails} fail")
    return 1 if fails else 0


def plot(out: Path) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.6))
    offs = [F(x) for x in range(550, 901, 5)]
    lo = [floor1(edge_margins(o)[0]) for o in offs]
    hi = [floor1(edge_margins(o)[1]) for o in offs]
    ax1.plot([float(o) for o in offs], lo, label="lower edge (144.0012 MHz carrier)")
    ax1.plot([float(o) for o in offs], hi, label="upper edge (147.9988 MHz carrier)")
    ax1.axhline(0, color="k", lw=0.8)
    ax1.axvline(750, color="tab:red", ls="--", lw=1)
    ax1.annotate("REQ-TX-006 750 Hz (TBR)\nupper margin %.1f Hz" % floor1(edge_margins(SB60_OFFSET)[1]),
                 xy=(750, floor1(edge_margins(SB60_OFFSET)[1])), xytext=(765, 215), fontsize=8,
                 arrowprops=dict(arrowstyle="->", lw=0.8))
    ax1.axvline(float(max_offset_supported()), color="tab:gray", ls=":", lw=1)
    ax1.text(float(max_offset_supported()) + 5, 100, "limit %.1f Hz" % floor1(max_offset_supported()), fontsize=8)
    for x in (614, 735):
        ax1.axvline(x, color="tab:green", ls=":", lw=0.8)
    ax1.text(560, -40, "green dotted: F7 cases 614, 735 Hz", fontsize=7, color="tab:green")
    ax1.set_xlabel("-60 dB keying-sideband offset from carrier (Hz)")
    ax1.set_ylabel("margin inside band edge (Hz)")
    ax1.set_title("Band-edge guard 1.2 kHz, reference +/-2.5 ppm, word 5 Hz")
    ax1.grid(alpha=0.3)
    ax1.legend(fontsize=8, loc="upper right")

    labels, healthy, und = [], [], []
    for route in ("R1", "R3"):
        for iv in (12, 13, 14):
            labels.append(f"{route}\niv {iv}")
            hd = healthy_disagreement(route, iv)
            healthy.append(float(hd) / 1000)
            # R3: at the proposed threshold T; R1: at the smallest threshold that never trips a healthy unit
            und.append(float(undetected_bound(route, iv) if route == "R3" else min_154_limit(route, iv)) / 1000)
    x = range(len(labels))
    ax2.bar([i - 0.2 for i in x], healthy, width=0.4, label="healthy disagreement (must be < threshold T)")
    ax2.bar([i + 0.2 for i in x], und, width=0.4, label="largest undetected true error (R3 at T; R1 at smallest T)")
    ax2.axhline(float(L_154) / 1000, color="tab:red", ls="--", lw=1, label="REQ-SYS-154 true-error limit 10 kHz (TBR)")
    ax2.axhline(float(T_MEAS) / 1000, color="tab:green", ls="-.", lw=1, label="R3 measured threshold T = 5 kHz (proposal)")
    ax2.set_xticks(list(x))
    ax2.set_xticklabels(labels, fontsize=8)
    ax2.set_ylabel("carrier-referred frequency (kHz)")
    ax2.set_ylim(0, 34)
    ax2.set_title("Frequency verification (R1 raw XOSC, R3 TCXO-corrected)")
    ax2.grid(alpha=0.3, axis="y")
    ax2.legend(fontsize=7, loc="upper right")
    fig.suptitle("cwht frequency budget (docs/design/analysis/frequency-budget.md), developer evidence", fontsize=10)
    fig.tight_layout()
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out, dpi=130)
    print(f"figure: {out}")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--plot", action="store_true", help="render docs/reviews/PDR/figures/frequency-budget.png")
    a = ap.parse_args(argv)
    rc = report(run_checks())
    if a.plot:
        plot(Path("docs/reviews/PDR/figures/frequency-budget.png"))
    return rc


if __name__ == "__main__":
    sys.exit(main())
