# Frequency budget, band-edge guard and frequency-verification counter

| Field | Value |
|---|---|
| Product | `docs/design/analysis/frequency-budget.md` (analysis note, `analysis_kind`: budget, timing, worst-case) |
| Work package | WP-PDR-20 (`docs/plan/pdr-work-plan.md` section 3.6), wave 1a |
| Author | Claude, RF designer (TX) author invocation, 2026-09-27 |
| Checker | `hardware/sim/freq/freq_budget.py` (one command, section 7) |
| Figure | `docs/reviews/PDR/figures/frequency-budget.png` (rendered and inspected, section 7) |
| Review record | `docs/reviews/PDR/checklists/analysis-frequency-budget-and-clock-plan.md` (one record for this note and `clock-plan.md`, plan section 3.6), with `docs/templates/peer-review-checklist-analysis.md` (on `cr/CR-012-pdr-checklist-templates`, not yet on `main`) |
| Evidence status | **Developer evidence** (05 section 9.1). The checker is a class B script without a TV record. Under CK-ANA-C2 no value here closes a requirement or goes to the owner as a TBR value until a TV record covers the checker or the owner rules on developer evidence (section 6, item 1) |
| Staging | The guard values depend on REQ-TX-006 (750 Hz, TBR), which WP-PDR-22 confirms. The TS-007 part choice is decided at B1a. These values are finalized after WP-PDR-22 and ruled at B2 (plan WP-PDR-20 "Depends on"; rule C10) |
| AT RISK | No. Nothing here depends on CR-003 or CR-006 |

## 1. Question and scope

This note answers four questions:

1. Does the 1.2 kHz band-edge guard of REQ-SYS-008, REQ-SYS-009 and REQ-TX-002 keep the -60 dB keying-sideband point (REQ-TX-006) and the 26 dB bandwidth (REQ-SYS-015) inside 144.000 to 148.000 MHz? The check uses the +/-2.5 ppm reference of REQ-SYS-010 and the frequency-word error, at both band edges.
2. Which reference budget makes REQ-SYS-010 (+/-2.5 ppm for one year after calibration) and the band-edge guard hold even if the firmware calibration constant is wrong? What two-unit offset remains for RSK-002?
3. Can the independent frequency verification of REQ-SYS-182 and REQ-SYS-154 (HZ-008 K7) hold its 10 kHz window and 100 ms limit on the RP2350 crystal timebase? What prescaler ratio and sample does REQ-TX-013 need?
4. Which TBR values does this analysis propose, and which of them trigger the "else a CR" branch of their `tbr.plan`?

Identifiers served:
- Requirements: REQ-SYS-008, REQ-SYS-009, REQ-SYS-010, REQ-SYS-154, REQ-SYS-182, REQ-TX-002, REQ-TX-013.
- Inputs: REQ-TX-006, REQ-SYS-015, REQ-SYS-004, REQ-SYS-161.
- TPM-006 (`frequency-stability`); RSK-002 step S1; RSK-046 step S2.
- HZ-008 controls K4 and K7 (`docs/safety/hazards.json` 0.5.0-pha); SRR decisions 25 and 40.
- TS-007 criteria M3 and R-M3.

The receiver phase-noise and reciprocal-mixing arithmetic is in TS-007 section 4 (criterion C1). The clock harmonics are in `docs/design/analysis/clock-plan.md`.

## 2. Inputs

| Input | Value | Source | State |
|---|---|---|---|
| Band edges | 144.000 and 148.000 MHz | 47 CFR 97.301(a) (corpus: `47cfr-97.301.md` line 26, eCFR issue 2026-09-23) | Regulation |
| CW-only segment | 144.0 to 144.1 MHz (other emissions start at 144.1 MHz) | 47 CFR 97.305(a), (c) (corpus: `47cfr-97.305.md` lines 17, 58) | Regulation |
| Carrier limits | 144.0012 to 147.9988 MHz | REQ-SYS-008, REQ-SYS-009, REQ-TX-002 (TBR); SRR decision 25 | TBR |
| Reference ceiling | +/-2.5 ppm total, -10 to +45 C, one year after calibration | REQ-SYS-010 (TBR); ADR-023 item (1) | TBR |
| -60 dB keying-sideband offset | 750 Hz; research cases 614 and 735 Hz | REQ-TX-006 (TBR); `docs/research/regulatory-corpus-and-operators.md` F7 | TBR (WP-PDR-22) |
| 26 dB bandwidth | at most 350 Hz (175 Hz each side) | REQ-SYS-015 (TBR) | TBR |
| Frequency-word error | 5 Hz | **Allocation** of this note. Section 3.2 shows it is conservative for both TS-007 candidates | Allocation |
| TCXO temperature-stability classes | 0.1, 0.25, 0.5 ppm | `docs/research/2m-cw-transceiver-reference-designs.md` F21 (Medium) | Research |
| TCXO uncalibrated total | 1.5 ppm (initial, reflow, temperature -10 to +45 C, 1 yr aging, supply and load) | **Allocation**; it becomes the datasheet acceptance test R-M3 of TS-007 | Allocation |
| Aging, supply and load inside it | 0.5 ppm and 0.1 ppm | **Allocation** (engineering assumption for a TCXO class; the datasheet confirms at CDR) | Allocation |
| Calibration range and uncertainty | +/-0.9 ppm; 0.1 ppm | **Allocation**; calibration by zero-beat per RSK-002 step S4 | Allocation |
| CW filter half-bandwidth | 250 Hz | RSK-002 statement | Risk register |
| Agreement window, time limit | 10 kHz, 100 ms | REQ-SYS-182, REQ-SYS-154 (TBR); SRR decision 40 | TBR |
| RF-off time after detection | 20 ms | REQ-SYS-004 (TBR) | TBR |
| Lead-in after RX-to-TX changeover | at most 12 ms | ADR-026 section 2 (REQ-SYS-161, TBR) | TBR |
| Retune time at changeover | A1 0 ms (TX on its own Si5351A PLL); A2 below 1.5 ms (LMX2571 FastLock) | TS-007 section 3.2; F20 (High) | Research |
| Software latency of the changeover check; service period during transmit | 2 ms; 10 ms | **Allocations**, to be confirmed by the WP-PDR-32 timing analysis | Allocation |
| Prescaler ratio | 8 | **Proposal** of this note (section 3.3) | Proposal |
| Sample ceiling | below 20 MHz | REQ-TX-013 (TBR) | TBR |
| GPIN input limit | 50 MHz | RP2350 datasheet section 8.1.1.4 ("GPIN0-GPIN1 ... is limited to 50MHz"); datasheet extract `docs/extracted/rp2350-datasheet.md` at rustos commit `2ec64c0f` (read with `git show`, never from the working tree) | Datasheet |
| FC0 test interval and accuracy | interval 12: 4 ms, 500 Hz; 13: 8 ms, 250 Hz; 14: 16 ms, 125 Hz; 15: 32 ms, 62.5 Hz | RP2350 datasheet section 8.1.3, Table 541. FC0_INTERVAL (Table 582) says "0.98us * 2**interval"; this note uses 1 us, which is longer and so conservative for time | Datasheet |
| FC0 sources and status | GPIN0, GPIN1 selectable; DONE, PASS, FAST, SLOW, DIED, FAIL status | RP2350 datasheet Tables 583, 584 | Datasheet |
| RP2350 crystal (XOSC) | 12.000 MHz; +/-30 ppm tolerance, +/-30 ppm stability, +/-5 ppm first-year aging | RP2350 datasheet section 8.2.1.1, Table 596 (ABM8-272-T3) | Datasheet |
| TCXO frequency | 25.000 MHz | TS-007 section 8 (R-M4); `clock-plan.md` section 4 | Proposal |

## 3. Method and results

The checker computes every number below with exact rational arithmetic. Margins are rounded toward the limit (floored). Sums compared with a ceiling are rounded up.

### 3.1 Band-edge guard (REQ-SYS-008, 009, 010; REQ-TX-002, 006; REQ-SYS-015)

The worst case at each edge adds four terms toward that edge:
- the carrier set at the guard limit;
- the reference error at +/-2.5 ppm;
- the frequency-word error of 5 Hz;
- the keying-sideband or bandwidth offset.

The lower edge uses 144.0012 MHz minus every term. The upper edge uses 147.9988 MHz plus every term. The 2.5 ppm term is 360.003 Hz at the lower edge and 369.997 Hz at the upper edge, so the upper edge governs.

| Case | Condition | Result | Margin inside the band |
|---|---|---|---|
| C-1 | Lower edge, -60 dB point at 750 Hz | 144.0000849 MHz | +84.9 Hz |
| C-2 | Upper edge, -60 dB point at 750 Hz | 147.9999250 MHz | **+75.0 Hz** (governs) |
| C-3 | Lower edge, 26 dB half-bandwidth 175 Hz | | +659.9 Hz |
| C-4 | Upper edge, 26 dB half-bandwidth 175 Hz | | +650.0 Hz |
| C-5 | Largest REQ-TX-006 offset the guard supports | 825.0 Hz | 75.0 Hz above the 750 Hz TBR |
| C-6 | Largest reference error the guard supports at 750 Hz | 3.006 ppm | 0.506 ppm above the 2.5 ppm ceiling |
| C-7.1 to C-7.3 | Research offsets 614, 735 and 750 Hz (F7) | | +211.0, +90.0, +75.0 Hz |

Known answer: with no word error the upper margin is 1200 - 370 - 750 = 80 Hz, the SRR decision 25 arithmetic (checker KA-1).

**Finding 3.1.** The 1.2 kHz guard holds with the 5 Hz word allocation, with 75.0 Hz to spare at the upper edge. It stays valid while WP-PDR-22 confirms a REQ-TX-006 offset of at most 825.0 Hz. Above that, the "else a CR" branch of the REQ-SYS-008 `tbr.plan` applies. The margin is small compared with the uncertainty of the REQ-TX-006 offset itself, which is a TS-006 simulation result (section 5). WP-PDR-22 therefore reports the offset at every envelope setting and tolerance corner against the 825.0 Hz limit, not against 750 Hz.

### 3.2 Reference budget (REQ-SYS-010, TPM-006, RSK-002)

**Frequency-word term.** The 5 Hz allocation covers both TS-007 candidates.
- Si5351A: the PLL feedback divider with a 20-bit denominator at a 25 MHz reference gives a 3.97 Hz output step at divider 6. This is an engineering assumption: the vendor register map (AN619) is not in the corpus. Rounding to the nearest step errs by at most 2.0 Hz.
- LMX2571: its fractional denominator width is not in the corpus. The allocation is therefore a requirement on the SW-SYNTH frequency-word design, verified by HostUnit tests against an independent reference model (RSK-046 step S3). It is not a property claimed for the part.

**Two budget identities** set the reference class:

1. **Calibrated case (REQ-SYS-010 as written, "after calibration").** The firmware calibration offset removes the initial and reflow terms:
   `u_cal + temperature + aging + supply/load + word <= 2.5 ppm`
2. **Guard-protecting case (HZ-008 K4).** A calibration constant entered wrongly, but inside its allowed range, adds to the uncorrected error. So the band-edge guard holds whatever the calibration state only if:
   `uncalibrated total + calibration range + word <= 2.5 ppm`
   with the calibration range no larger than the uncalibrated total it corrects. This bound makes the calibration constant a safety-relevant configuration value of the SW-SYNTH "calibration application" unit, which is safety-critical in 07 section 14.1 (HZ-008 cause C7 names "a calibration value out of range").

| Case | Terms | Result | Limit | Margin |
|---|---|---|---|---|
| C-8 | 1.5 ppm uncalibrated + 0.9 ppm range + 0.034 ppm word | 2.434 ppm | 2.5 ppm | 0.066 ppm (9.7 Hz at 148 MHz) |
| C-9 | range 0.9 ppm vs uncalibrated 1.5 ppm | range smaller | range <= uncalibrated | holds |
| C-10.1 | Calibrated, 0.1 ppm temperature class | 0.834 ppm | 2.5 ppm | 1.666 ppm |
| C-10.2 | Calibrated, 0.25 ppm class | 0.984 ppm | 2.5 ppm | 1.516 ppm |
| C-10.3 | Calibrated, 0.5 ppm class | 1.234 ppm | 2.5 ppm | 1.266 ppm |
| C-10.xu | Share of the 1.5 ppm uncalibrated allocation left for initial and reflow | 0.8 / 0.65 / 0.4 ppm for the three classes | | datasheet test at CDR |

**Two-unit offset after calibration (RSK-002 step S1), Hz at 146 MHz.** Both units are calibrated. Each unit's residual is `u_cal + temperature + aging + supply/load`, and the word error is counted for each unit.

| Temperature class | At calibration (aging 0) | After one year (aging 0.5 ppm) | Against the 250 Hz half-passband |
|---|---|---|---|
| 0.1 ppm | 97.6 Hz | 243.6 Hz | inside, both |
| 0.25 ppm | 141.4 Hz | 287.4 Hz | inside at calibration, outside after a year |
| 0.5 ppm | 214.4 Hz | 360.4 Hz | inside at calibration, outside after a year |

**Finding 3.2.**
- REQ-SYS-010 at +/-2.5 ppm closes with margin for every class. The margin sits in the calibrated case.
- The guard-protecting identity is the binding one. It turns into two derived constraints:
  - (a) a TCXO datasheet acceptance test: uncalibrated total at most 1.5 ppm over -10 to +45 C and one year, including reflow (TS-007 R-M3);
  - (b) a firmware calibration range of at most +/-0.9 ppm (+/-133 Hz at 148 MHz), which is a new SW-SYNTH requirement (section 5).
- RSK-002 is fully mitigated only with the 0.1 ppm class, or with re-calibration within a year. Otherwise the receiver incremental tuning of RSK-002 step S3 remains the operator's tool.
- The TPM-006 current best estimate, calibrated worst case, is 0.834, 0.984 or 1.234 ppm by class, `credit: false`. The estimate becomes credit-bearing on the datasheet of the part chosen at CDR.

### 3.3 Frequency-verification counter (REQ-SYS-182, REQ-SYS-154, REQ-TX-013; HZ-008 K7)

**Architecture assumed** (proposal; the SW-SAFE design belongs to WP-PDR-32 and WP-PDR-35):
- A hardware divide-by-8 prescaler on the transmit carrier sample (taken at the exciter, ahead of the PA) drives one RP2350 GPIN input.
- The RP2350 frequency counter FC0 counts it. FC0's interval is timed by clk_ref from the XOSC (datasheet section 8.1.3), so it is independent of the synthesizer reference and of the SW-SYNTH driver.
- FC0 sets DIED when the counted clock stops. This implements the rule of REQ-SYS-182 that "no valid measurement means no agreement" in hardware.
- The prescaler input is on the TX path only, so it adds no receive line (see `clock-plan.md`).

**Sample (REQ-TX-013).** 144.0012 to 147.9988 MHz divided by 8 gives 18.000 15 to 18.499 85 MHz (C-11). This is below the 20 MHz ceiling of REQ-TX-013 and below the 50 MHz GPIN limit. A digital divider is exact, so the sample times 8 equals the carrier: the 1 kHz accuracy of REQ-TX-013 is met with no error term, and 1 kHz stays as the Test tolerance. A ratio of 16 is rejected: 144 MHz / 16 is 9.000 MHz, on the candidate IF (`clock-plan.md` section 4).

**Timebase routes.** A fault-free unit shows a disagreement between the counted and the set frequency. The window W must exceed that disagreement, or healthy units trip into Fault-safe.

- **R1, raw XOSC timebase (HZ-008 K7 text as written).** Disagreement = FC0 accuracy x 8 + TCXO error + XOSC error (65 ppm = 9 620 Hz at 147.9988 MHz).
- **R2, XOSC corrected by a constant stored at unit calibration.** Rejected. Table 596 gives only a +/-30 ppm stability band with no curve, so a room-temperature calibration cannot be shown to shrink the bound below R1's without an assumption on the crystal's temperature curve.
- **R3, XOSC corrected by a TCXO count taken in receive.** FC0 counts the TCXO on the second GPIN during receive (interval 15) and refreshes the XOSC/TCXO ratio at least once a second. In a healthy unit, carrier and TCXO are then in an exact ratio, so the TCXO error cancels. The remaining disagreement is:
  - FC0 accuracy x 8;
  - the TCXO-count quantization (62.5 Hz / 25 MHz = 2.5 ppm);
  - an allocated 1 ppm XOSC drift between refreshes.

  The refreshed ratio is accepted only within +/-67.5 ppm (XOSC 65 + TCXO 2.5). Outside that, the unit enters Fault-safe, so a gross TCXO or XOSC fault is itself detected.

| Case | Route and use | FC0 interval | Healthy disagreement | Against the 10 kHz window | Largest undetected single-fault error |
|---|---|---|---|---|---|
| C-12.iv12 | R3, check before PA_EN at changeover | 12 (4 ms) | 4 518.0 Hz | holds, margin 5 482.0 Hz | 14 518.0 Hz |
| C-12.iv13 | R3, repeated check during transmit | 13 (8 ms) | 2 518.0 Hz | holds, margin 7 482.0 Hz | 12 518.0 Hz |
| C-13.iv12 | R1, changeover | 12 | 13 990.0 Hz | **does not hold** | 23 620.0 Hz |
| C-13.iv13 | R1, transmit | 13 | 11 990.0 Hz | **does not hold** | 21 620.0 Hz |
| (table) | R1 | 14 (16 ms) | 10 990.0 Hz | does not hold | 20 620.0 Hz |

**Times.**

| Case | Path | Result | Limit | Margin |
|---|---|---|---|---|
| C-14.A1 | Changeover: no retune + 4 ms FC0 + 2 ms software | 6.00 ms | 12 ms lead-in (REQ-SYS-161, TBR) | 6.00 ms |
| C-14.A2 | Changeover: 1.5 ms FastLock + 4 ms + 2 ms | 7.50 ms | 12 ms | 4.50 ms |
| C-15 | Fault during transmit: two 8 ms intervals + 10 ms service period + 20 ms RF off (REQ-SYS-004) | 46.0 ms | 100 ms (REQ-SYS-182) | 54.0 ms |

A fault that starts inside an interval may not trip that interval, because the count mixes the good and bad frequencies. The next full interval trips it, hence two intervals in C-15.

**Finding 3.3.**
- On the raw XOSC timebase (route R1), a fault-free unit at a worst-case crystal disagrees by up to 11.99 kHz at interval 13. The adopted 10 kHz window of REQ-SYS-182 and REQ-SYS-154 would then trip healthy units. So R1 needs a window of at least 12.0 kHz at interval 13, which is the "else they change by CR" branch of the REQ-SYS-182 `tbr.plan`. Interval 13 leaves only 0.5 ms of lead-in margin for A2.
- Route R3 keeps 10 kHz and 100 ms, with 5.5 kHz and 54 ms of margin. It also lowers the largest undetected single-fault error from 21.6 kHz to 14.5 kHz. Both routes catch the gross error the hazard names (5 W on 150 to 174 MHz, HZ-008 C7).
- R3 departs from one phrase of the HZ-008 K7 text, "uses the RP2350 crystal timebase rather than the synthesizer reference". The gate stays on the XOSC, but the scale factor uses the TCXO, bounded by the 67.5 ppm plausibility test.
- **Recommendation:** R3, with FC0 on two GPIN pins, interval 12 before PA_EN and interval 13 during transmit. The K7 wording change goes to the hazards writer (section 5). If the owner prefers the K7 text as written, route R1 is taken with REQ-SYS-182 and REQ-SYS-154 at 12 kHz by CR.

## 4. Proposed TBR values (rule C10: to the owner only after this note's record is APPROVED and a TV record or owner ruling covers the checker)

| Requirement | Proposed value | Margin that supports it | `tbr.plan` step executed | "Else a CR" branch triggered? |
|---|---|---|---|---|
| REQ-SYS-008 | 144.0012 to 147.9988 MHz (1.2 kHz guard), unchanged | 75.0 Hz at the upper edge with REQ-TX-006 at 750 Hz; holds up to 825.0 Hz | "the frequency error budget and the TS-006 sideband offset confirm the 1.2 kHz guard at PDR" | No, provided WP-PDR-22 confirms at most 825.0 Hz |
| REQ-SYS-009 | Same limits as REQ-SYS-008 | same | "closes with the guard value" | No |
| REQ-TX-002 | Same limits as REQ-SYS-008 | same | "closes with REQ-SYS-008" | No |
| REQ-SYS-010 | +/-2.5 ppm, -10 to +45 C (span follows REQ-SYS-114, WP-PDR-28), one year after calibration, unchanged | calibrated case 1.266 to 1.666 ppm; guard-protecting identity 0.066 ppm with the section 3.2 constraints | "TS-NNN selects the reference grade; the error budget fixes the tolerance; span reconciled with TPM-006" (the budget lives here; WP-PDR-29 carries it into `docs/design/budgets.md`) | No |
| REQ-SYS-154 | 10 kHz, unchanged, with route R3 | 5.5 kHz (changeover), 7.5 kHz (transmit) | "TS (synthesizer and lock detect) fixes the counting tolerance" | No with R3. Yes with R1 (at least 12 kHz) |
| REQ-SYS-182 | 10 kHz and 100 ms, unchanged, with route R3 | 5.5 kHz; 54 ms | "the PDR prescaler, counter and timebase design confirms them against the counter gate time, resolution and crystal tolerance, else they change by CR" | No with R3. Yes with R1 (window at least 12 kHz; 100 ms holds) |
| REQ-TX-013 | Fixed ratio 8; sample 18.000 15 to 18.499 85 MHz, 3.3 V, below 20 MHz; within 1 kHz (exact division) | 1.5 MHz under the 20 MHz ceiling | "fixes the division ratio, the counting input and the sample accuracy" (counting input: an RP2350 GPIN pin to FC0) | No |

TPM-006: planned value +/-2.5 ppm, per the ADR-023 ceiling. Current best estimate 0.834 / 0.984 / 1.234 ppm (calibrated, by class), `credit: false`, evidence this note. The value is sent to the TPM writer (WP-PDR-29). This note does not edit `docs/plan/tpm.json`.

## 5. Derived constraints and requests to other writers (plan section 5.3; this note edits none of these files)

| To | Request |
|---|---|
| WP-PDR-16b (`docs/safety/hazards.json`, sole writer) | HZ-008 K7: replace "uses the RP2350 crystal timebase rather than the synthesizer reference" with route R3's wording: gate on the XOSC; XOSC/TCXO ratio refreshed in receive and bounded at +/-67.5 ppm; FC0 DIED status as "no valid measurement". HZ-008 K4: add the calibration-range bound of section 3.2 (calibration constant within +/-0.9 ppm). If R1 is chosen instead, K7 keeps its text and its window becomes 12 kHz |
| WP-PDR-35 (`docs/requirements/sw/**`) | New SW-SYNTH requirement: calibration constant bounded at +/-0.9 ppm, out-of-range value rejected. New SW-SAFE requirements: FC0 on the carrier sample at interval 12 before PA_EN and 13 during transmit; TCXO ratio refresh at least once a second in receive; ratio plausibility +/-67.5 ppm; DIED or FAIL as disagreement |
| WP-PDR-32 (software architecture, 07 WP-SW-14) | The frequency counter is FC0 with two GPIN inputs, not a PIO or TIMER capture. It needs a timing analysis confirming the 2 ms changeover latency and the 10 ms transmit service period allocated here |
| WP-PDR-36a (`ICD-CTL-SW` pin map) | Two GPIN-capable pins: GPIO 20 or 22 (GPIN0, GPIN1), or GPIO 12 or 14 (RP2350 datasheet GPIO function table). One carries the prescaled carrier, one the TCXO (or a divided TCXO copy) |
| WP-PDR-22 (TS-006) | Report the REQ-TX-006 offset at every setting and corner against the 825.0 Hz limit of case C-5 |
| WP-PDR-29 (`docs/design/budgets.md`, `docs/plan/tpm.json`) | Frequency budget section and TPM-006 current best estimate as in section 4 |
| WP-PDR-18 (`docs/risk/register.json`) | RSK-002: step S1 evidence is this note. It stays at likelihood 3 or above unless the 0.1 ppm class or yearly re-calibration is adopted. RSK-046: step S2 evidence is this note. The software-fault member now has an analysis (section 3.3); re-score at the Track pass |

## 6. Uncertainty and limitations

1. **Tool status.** The checker has no TV record. Its arithmetic has three known-answer self-checks (KA-1 to KA-3) and can be recomputed by hand from the tables above. Before the section 4 values go to the owner, a TV record must cover `hardware/sim/freq/*.py`, or the owner must rule to accept developer evidence. The lead SE decides which route (return, open_questions).
2. **Allocations are not datasheet values.** The allocations include the TCXO uncalibrated total, aging, supply and load, calibration uncertainty, software latency and service period. Each is a requirement on a later design or part choice, verified at CDR (datasheet Inspection, WP-PDR-32 timing analysis). A part that misses an allocation re-opens this note.
3. **REQ-TX-006 dominates the guard margin.** The 75.0 Hz margin is smaller than any plausible uncertainty of a simulated -60 dB offset. The guard is only as good as the WP-PDR-22 corner analysis.
4. **FC0 accuracy semantics.** Table 541 gives "accuracy" per interval without saying whether it is a bound or a typical value. This note treats it as a +/- bound at the counted input. The dev-board check of 07 WP-SW-14 is to confirm it with a known clock.
5. **XOSC bound.** 65 ppm is the Table 596 sum over -40 to +85 C. Over -10 to +45 C the true value is smaller, so R1's result is conservative.
6. **LMX2571 retune time.** "FastLock < 1.5 ms" (F20) is a datasheet feature statement. Its conditions for a 12 MHz jump (RX LO to TX carrier with a 9 to 10.7 MHz IF) are not in the corpus. C-14.A2 has 4.5 ms of margin for it.

## 7. Reproduction and visual closure

```
cd /Users/robinonsay/rust/cwht && .venv/bin/python hardware/sim/freq/freq_budget.py --plot
```

Expected: 27 PASS, 0 FAIL, 4 INFO lines, exit status 0 (run 2026-09-27 at the freeze commit). The figure `docs/reviews/PDR/figures/frequency-budget.png` has two panels:
- the edge margins against the REQ-TX-006 offset, with the 750 Hz TBR, the 825.0 Hz limit and the F7 cases marked;
- the healthy disagreement and the undetected-error bound per route and interval, against the 10 kHz window.

The author opened and inspected it after two layout corrections (overlapping labels).

## 8. Per-case index

C-1 to C-7 band edges; C-8 to C-10 reference identities; C-11 sample; C-12 and C-13 window per route; C-14 changeover time per alternative; C-15 transmit detection time; C-16 and C-17 informational bounds. Checker output lines carry the same ids.

## Change history

| Revision | Date | Change | Reason |
|---|---|---|---|
| 0 | 2026-09-27 | Initial issue, frozen for its first review (freeze F0, rule C2) | WP-PDR-20 wave 1a |
