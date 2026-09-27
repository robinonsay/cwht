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
3. Can the independent frequency verification of REQ-SYS-182 and REQ-SYS-154 (HZ-008 K7) hold its 10 kHz window and 100 ms limit on the RP2350 crystal timebase? What prescaler ratio and sample does REQ-TX-013 need? How are both REQ-SYS-154 triggers ("unlocked" and "off its set frequency by over 10 kHz") detected at both moments ("on key-down" and "during transmission"), and how fast?
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
| Agreement window, time limit | 10 kHz measured agreement, 100 ms | REQ-SYS-182 (TBR); SRR decision 40 | TBR |
| Synthesizer true-error limit | Fault-safe when "off its set frequency by over 10 kHz" (a true error, not a measured one) | REQ-SYS-154 (TBR); SRR decision 40 | TBR |
| Measured detection threshold T | 5.0 kHz | **Proposal** of this note (section 3.3, revision 1); an SW-SAFE L2 value, distinct from the 10 kHz system values | Proposal |
| Fault-injection offset | 12 kHz above or below the set frequency | REQ-SYS-154 and REQ-SYS-182 verification notes; TC-SYS-101 procedure | Verification case |
| Lock-detect sample period during transmission | at most 10 ms | **Allocation** of this note (section 3.3, revision 1), to be confirmed by the WP-PDR-32 timing analysis | Allocation |
| Lock-detect means | A2 (recommended): LMX2571 lock-detect indication, form not in the corpus (a TS-007 value-of-information item 4 question; INSP-055 finding-4 asks TS-007 to add it). A1: Si5351A loss-of-lock status read over I2C (register map AN619 not in the corpus) | TS-007 section 1 recommendation; 07 section 14.2 `SW-SYNTH` rows, items g and l | Research gap |
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

**Measured threshold and true-error limit (revision 1, INSP-056 finding-1).** Two limits apply, and they are not the same quantity:
- REQ-SYS-154 bounds the **true** error: Fault-safe when the synthesizer is off its set frequency by over 10 kHz.
- The counter sees only the **measured** error, which differs from the true error by up to the healthy disagreement d.

A measured threshold T therefore meets REQ-SYS-154 only if two conditions hold:
- no false trip: d < T;
- no missed trip: T + d <= 10 kHz, so any true error over 10 kHz measures above T.

With a 10 kHz measured threshold (revision 0), a true error up to 10 kHz + d passes: 14 518 Hz at interval 12. That did not meet REQ-SYS-154. This revision proposes a **measured threshold T = 5.0 kHz** for both intervals. It lies inside the R3 interval at interval 12 (4 518 < T <= 5 482 Hz) and at interval 13 (2 518 < T <= 7 482 Hz). T is an SW-SAFE design value (L2, WP-PDR-35). REQ-SYS-154 (10 kHz true error) and REQ-SYS-182 (10 kHz measured agreement) keep their values: a measured agreement within 5 kHz is also an agreement within 10 kHz, so RF is still withheld whenever the measurement disagrees by more than 10 kHz.

| Case | Route and use | FC0 interval | Healthy disagreement d | No false trip: d < T = 5 kHz | Largest undetected true error T + d, against REQ-SYS-154 10 kHz | TC-SYS-101 12 kHz injection: 12 kHz - d > T |
|---|---|---|---|---|---|---|
| C-12.iv12, C-16.iv12, C-18.iv12 | R3, check before PA_EN at changeover | 12 (4 ms) | 4 518.0 Hz | holds, margin 482.0 Hz | 9 518.0 Hz, margin 482.0 Hz | trips, margin 2 482.0 Hz |
| C-12.iv13, C-16.iv13, C-18.iv13 | R3, repeated check during transmit | 13 (8 ms) | 2 518.0 Hz | holds, margin 2 482.0 Hz | 7 518.0 Hz, margin 2 482.0 Hz | trips, margin 4 482.0 Hz |
| C-13.iv12 | R1, changeover | 12 | 13 990.0 Hz | no T exists below 10 kHz | at least 27 609.9 Hz (T just above d) | not applicable |
| C-13.iv13 | R1, transmit | 13 | 11 990.0 Hz | no T exists below 10 kHz | at least 23 609.9 Hz | not applicable |
| (table) | R1 | 14 (16 ms) | 10 990.0 Hz | no T exists below 10 kHz | at least 21 609.9 Hz | not applicable |

C-12w checks that T (5 kHz) does not exceed the REQ-SYS-182 10 kHz window. Under R1, no threshold meets both conditions with REQ-SYS-154 at 10 kHz, because d alone exceeds 10 kHz. R1 would need REQ-SYS-154 at 23.7 kHz or more (interval 13) and the REQ-SYS-182 window at 12.0 kHz or more, both by CR.

**Sensitivity to the FC0 accuracy (C-16a).** The 482 Hz margin at interval 12 is small beside the 4 000 Hz FC0 term inside d. Both conditions hold while the FC0 accuracy at the counted input is at most 560.2 Hz at interval 12, against the 500 Hz of Table 541, and at most 560.2 Hz at interval 13, against its 250 Hz. The 560 Hz ceiling at interval 12 becomes the acceptance limit of the FC0 known-clock check on the dev board (07 WP-SW-14; section 6 item 4). If that check fails, the changeover check moves to interval 13: C-14.A2 then takes 11.5 ms, 0.5 ms inside the 12 ms lead-in.

**Effect on TC-SYS-101.** With T = 5 kHz, the 12 kHz injection of TC-SYS-101 (and of the REQ-SYS-182 verification note) measures at least 7 482 Hz at interval 12 and at least 9 482 Hz at interval 13, so it trips at key-down and during the over, with 2 482 Hz and 4 482 Hz to spare (C-18). The case needs no change: its acceptance criteria and its 12 kHz injection stand as written. The threshold itself is verified at L2 by HostUnit cases with injected counts on both sides of T (request to WP-PDR-35, section 5).

**Unlocked synthesizer (revision 1, INSP-056 finding-2).** REQ-SYS-154 also calls for Fault-safe when the synthesizer is unlocked, whatever its frequency. An unlocked VCO can sit inside T for a while as it drifts, so the counter alone does not catch every unlocked state. Two means apply, and the device lock-detect indication is the primary one:

| Case | Moment | Primary means | Second means | Time budget | Result |
|---|---|---|---|---|---|
| U-1.A1, U-1.A2 | Unlocked at key-down (before PA_EN) | `SW-SYNTH` reads the lock-detect indication after the last synthesizer write and again immediately before it sets the `PA_EN` frequency prerequisite (07 section 14.2 `SW-SYNTH` items g and l). The read is inside the 2 ms software allocation of C-14 | The FC0 interval 12 check (C-12): an unlocked output more than 5.482 kHz off trips; FC0 DIED catches a stopped output | changeover 6.00 ms (A1) and 7.50 ms (A2), inside the 12 ms lead-in (REQ-SYS-161) | PA_EN is never set with an unlocked synthesizer |
| U-2 | Unlocked during transmission | `SW-SYNTH` samples the lock-detect indication at least every 10 ms (allocation), or takes it as a GPIO edge interrupt if the part has a lock-detect pin, and requests Fault-safe on loss of lock | The FC0 interval 13 repeated check (C-15, 46.0 ms to RF off) | 10 ms to detection + 20 ms RF off (REQ-SYS-004) = 30.0 ms, inside the 100 ms of REQ-SYS-182, which bounds detection plus the fall for frequency faults | RF off within 30 ms of loss of lock; 70 ms margin |

REQ-SYS-154 sets no time of its own. REQ-SYS-004 bounds the RF-off time after detection (20 ms), and REQ-SYS-182 bounds detection plus the fall (100 ms) for the same fault family, so the U-2 budget is checked against both.

The lock-detect form for the recommended line-up is a research gap. The LMX2571 lock-detect indication (a pin, or a status register read over SPI) is not in the corpus. It belongs to TS-007 value-of-information item 4, the LMX2571 datasheet read, which INSP-055 finding-4 asks TS-007 to extend with the lock-detect output. The allocations therefore cover both forms:
- **Lock-detect pin:** one RP2350 GPIO input, read by `SW-SYNTH` (request to WP-PDR-36a).
- **Status register only:** an SPI status read in each 10 ms service period during transmission. The read is a transmit-time SPI transaction, so it adds no receive line (`clock-plan.md` rule 4).

If the LMX2571 offers neither form, an unlocked VCO within 9.518 kHz of the set frequency is not detected before it drifts past T. The "unlocked" trigger of REQ-SYS-154 would then be met only for an unlock that the counter sees, and REQ-SYS-154 would need a CR to restate that trigger. This is the "else a CR" branch for the unlock half, decided when value-of-information item 4 is answered (TS-007 section 8, before CDR).

For A1 (Si5351A as transmit synthesizer, not recommended), the loss-of-lock status bit is read over I2C with the same 10 ms period. Its register map (AN619) is not in the corpus.

**Times.**

| Case | Path | Result | Limit | Margin |
|---|---|---|---|---|
| C-14.A1 | Changeover: no retune + 4 ms FC0 + 2 ms software | 6.00 ms | 12 ms lead-in (REQ-SYS-161, TBR) | 6.00 ms |
| C-14.A2 | Changeover: 1.5 ms FastLock + 4 ms + 2 ms | 7.50 ms | 12 ms | 4.50 ms |
| C-15 | Fault during transmit: two 8 ms intervals + 10 ms service period + 20 ms RF off (REQ-SYS-004) | 46.0 ms | 100 ms (REQ-SYS-182) | 54.0 ms |

A fault that starts inside an interval may not trip that interval, because the count mixes the good and bad frequencies. The next full interval trips it, hence two intervals in C-15.

**Finding 3.3.**
- On the raw XOSC timebase (route R1), a fault-free unit at a worst-case crystal disagrees by up to 11.99 kHz at interval 13. The adopted 10 kHz window of REQ-SYS-182 would then trip healthy units, and no measured threshold can meet the 10 kHz true-error limit of REQ-SYS-154. R1 therefore needs, by CR, a REQ-SYS-182 window of at least 12.0 kHz and a REQ-SYS-154 limit of at least 23.7 kHz at interval 13. This is the "else they change by CR" branch of the REQ-SYS-182 `tbr.plan`. Interval 13 leaves only 0.5 ms of lead-in margin for A2.
- Route R3 with the measured threshold T = 5.0 kHz meets REQ-SYS-154 (10 kHz true error) and REQ-SYS-182 (10 kHz, 100 ms) as written. The margins are 482 Hz at interval 12 and 2 482 Hz at interval 13, both sides of T, and 54 ms in time. The largest undetected synthesizer error is 9.518 kHz under R3, against at least 23.6 kHz under R1. Both routes catch the gross error the hazard names (5 W on 150 to 174 MHz, HZ-008 C7).
- The 12 kHz injection of TC-SYS-101 trips under R3 at both intervals (C-18); the case stands as written.
- Both REQ-SYS-154 triggers have a detection means at both moments. The unlocked trigger rests on the device lock-detect indication, read before PA_EN and every 10 ms during transmission (U-1, U-2; 30 ms to RF off), with the counter as the second means. Its form on the LMX2571 is TS-007 value-of-information item 4.
- R3 departs from one phrase of the HZ-008 K7 text, "uses the RP2350 crystal timebase rather than the synthesizer reference". The gate stays on the XOSC, but the scale factor uses the TCXO, bounded by the 67.5 ppm plausibility test.
- **Recommendation:** R3, with FC0 on two GPIN pins, interval 12 before PA_EN and interval 13 during transmit, and a measured threshold of 5.0 kHz. The K7 wording change goes to the hazards writer (section 5). If the owner prefers the K7 text as written, route R1 is taken, with REQ-SYS-182 at 12 kHz or more and REQ-SYS-154 at 23.7 kHz or more by CR.

## 4. Proposed TBR values (rule C10: to the owner only after this note's record is APPROVED and a TV record or owner ruling covers the checker)

| Requirement | Proposed value | Margin that supports it | `tbr.plan` step executed | "Else a CR" branch triggered? |
|---|---|---|---|---|
| REQ-SYS-008 | 144.0012 to 147.9988 MHz (1.2 kHz guard), unchanged | 75.0 Hz at the upper edge with REQ-TX-006 at 750 Hz; holds up to 825.0 Hz | "the frequency error budget and the TS-006 sideband offset confirm the 1.2 kHz guard at PDR" | No, provided WP-PDR-22 confirms at most 825.0 Hz |
| REQ-SYS-009 | Same limits as REQ-SYS-008 | same | "closes with the guard value" | No |
| REQ-TX-002 | Same limits as REQ-SYS-008 | same | "closes with REQ-SYS-008" | No |
| REQ-SYS-010 | +/-2.5 ppm, -10 to +45 C (span follows REQ-SYS-114, WP-PDR-28), one year after calibration, unchanged | calibrated case 1.266 to 1.666 ppm; guard-protecting identity 0.066 ppm with the section 3.2 constraints | "TS-NNN selects the reference grade; the error budget fixes the tolerance; span reconciled with TPM-006" (the budget lives here; WP-PDR-29 carries it into `docs/design/budgets.md`) | No |
| REQ-SYS-154 | 10 kHz true-error limit, unchanged, with route R3 and the measured threshold T = 5.0 kHz (an SW-SAFE L2 value, distinct from this limit). Unlocked trigger: device lock-detect indication read before PA_EN and at least every 10 ms during transmission, with the counter as the second means | Off-frequency: 482 Hz (changeover) and 2 482 Hz (transmit) on both sides of T (C-12, C-16). Unlocked: 30.0 ms to RF off, 70 ms inside 100 ms (U-2). TC-SYS-101 12 kHz injection trips with 2 482 Hz to spare (C-18); the case is unchanged | "TS (synthesizer and lock detect) fixes the counting tolerance": the counting tolerance is T = 5.0 kHz; the lock-detect means is as stated | No with R3, provided the LMX2571 exposes a lock-detect indication (TS-007 value-of-information item 4); if it does not, a CR restates the unlocked trigger. Yes with R1 (at least 23.7 kHz) |
| REQ-SYS-182 | 10 kHz and 100 ms, unchanged, with route R3 | measured threshold 5.0 kHz is within the 10 kHz window (C-12w); healthy margin 482 Hz; 54 ms | "the PDR prescaler, counter and timebase design confirms them against the counter gate time, resolution and crystal tolerance, else they change by CR" | No with R3. Yes with R1 (window at least 12 kHz; 100 ms holds) |
| REQ-TX-013 | Fixed ratio 8; sample 18.000 15 to 18.499 85 MHz, 3.3 V, below 20 MHz; within 1 kHz (exact division) | 1.5 MHz under the 20 MHz ceiling | "fixes the division ratio, the counting input and the sample accuracy" (counting input: an RP2350 GPIN pin to FC0) | No |

TPM-006: planned value +/-2.5 ppm, per the ADR-023 ceiling. Current best estimate 0.834 / 0.984 / 1.234 ppm (calibrated, by class), `credit: false`, evidence this note. The value is sent to the TPM writer (WP-PDR-29). This note does not edit `docs/plan/tpm.json`.

## 5. Derived constraints and requests to other writers (plan section 5.3; this note edits none of these files)

| To | Request |
|---|---|
| WP-PDR-16b (`docs/safety/hazards.json`, sole writer) | HZ-008 K7: replace "uses the RP2350 crystal timebase rather than the synthesizer reference" with route R3's wording: gate on the XOSC; XOSC/TCXO ratio refreshed in receive and bounded at +/-67.5 ppm; FC0 DIED status as "no valid measurement"; a measured threshold of 5.0 kHz, so that a true error over 10 kHz always trips. HZ-008 C8 and K7: name the device lock-detect indication as the primary means for the unlocked cause, with the counter as the second means. HZ-008 K4: add the calibration-range bound of section 3.2 (calibration constant within +/-0.9 ppm). If R1 is chosen instead, K7 keeps its text, its window becomes 12 kHz and the REQ-SYS-154 limit at least 23.7 kHz |
| WP-PDR-35 (`docs/requirements/sw/**`) | New SW-SYNTH requirements: calibration constant bounded at +/-0.9 ppm, out-of-range value rejected; lock-detect indication read after every write and immediately before the `PA_EN` frequency prerequisite is set; lock-detect sampled at least every 10 ms during transmission, loss of lock requesting Fault-safe (07 section 14.2 items g, l). New SW-SAFE requirements: FC0 on the carrier sample at interval 12 before PA_EN and 13 during transmit; measured threshold 5.0 kHz (disagreement above 5.0 kHz is a disagreement); TCXO ratio refresh at least once a second in receive; ratio plausibility +/-67.5 ppm; DIED or FAIL as disagreement. Test author: HostUnit cases with injected counts at 4.9 and 5.1 kHz and with an injected lock-detect loss before PA_EN and during transmission |
| WP-PDR-32 (software architecture, 07 WP-SW-14) | The frequency counter is FC0 with two GPIN inputs, not a PIO or TIMER capture. It needs a timing analysis confirming the 2 ms changeover latency (now including the lock-detect read), the 10 ms transmit service period and the 10 ms lock-detect sample period allocated here. The FC0 known-clock check on the dev board has the acceptance limit 560 Hz at interval 12 (C-16a) |
| WP-PDR-36a (`ICD-CTL-SW` pin map) | Two GPIN-capable pins: GPIO 20 or 22 (GPIN0, GPIN1), or GPIO 12 or 14 (RP2350 datasheet GPIO function table). One carries the prescaled carrier, one the TCXO (or a divided TCXO copy). One GPIO input for the synthesizer lock-detect pin, if TS-007 value-of-information item 4 shows the LMX2571 has one |
| WP-PDR-22 (TS-006) | Report the REQ-TX-006 offset at every setting and corner against the 825.0 Hz limit of case C-5 |
| WP-PDR-29 (`docs/design/budgets.md`, `docs/plan/tpm.json`) | Frequency budget section and TPM-006 current best estimate as in section 4 |
| WP-PDR-18 (`docs/risk/register.json`) | RSK-002: step S1 evidence is this note. It stays at likelihood 3 or above unless the 0.1 ppm class or yearly re-calibration is adopted. RSK-046: step S2 evidence is this note. The software-fault member now has an analysis (section 3.3); re-score at the Track pass |

## 6. Uncertainty and limitations

1. **Tool status.** The checker has no TV record. Its arithmetic has three known-answer self-checks (KA-1 to KA-3) and can be recomputed by hand from the tables above. Before the section 4 values go to the owner, a TV record must cover `hardware/sim/freq/*.py`, or the owner must rule to accept developer evidence. The lead SE decides which route (return, open_questions).
2. **Allocations are not datasheet values.** The allocations include the TCXO uncalibrated total, aging, supply and load, calibration uncertainty, software latency and service period. Each is a requirement on a later design or part choice, verified at CDR (datasheet Inspection, WP-PDR-32 timing analysis). A part that misses an allocation re-opens this note.
3. **REQ-TX-006 dominates the guard margin.** The 75.0 Hz margin is smaller than any plausible uncertainty of a simulated -60 dB offset. The guard is only as good as the WP-PDR-22 corner analysis.
4. **FC0 accuracy semantics.** Table 541 gives "accuracy" per interval without saying whether it is a bound or a typical value. This note treats it as a +/- bound at the counted input. The dev-board check of 07 WP-SW-14 is to confirm it with a known clock, against the 560 Hz ceiling at interval 12 that the 5.0 kHz threshold needs (C-16a).
5. **XOSC bound.** 65 ppm is the Table 596 sum over -40 to +85 C. Over -10 to +45 C the true value is smaller, so R1's result is conservative.
6. **LMX2571 retune time.** "FastLock < 1.5 ms" (F20) is a datasheet feature statement. Its conditions for a 12 MHz jump (RX LO to TX carrier with a 9 to 10.7 MHz IF) are not in the corpus. C-14.A2 has 4.5 ms of margin for it.
7. **Lock-detect form.** The LMX2571 lock-detect indication and its latency are not in the corpus (TS-007 value-of-information item 4, as INSP-055 finding-4 asks it to be extended). U-1 and U-2 assume the indication is valid within the 10 ms sample period.

## 7. Reproduction and visual closure

```
cd /Users/robinonsay/rust/cwht && .venv/bin/python hardware/sim/freq/freq_budget.py --plot
```

Expected: 35 PASS, 0 FAIL, 4 INFO lines, exit status 0 (revision 1, run 2026-09-27). The figure `docs/reviews/PDR/figures/frequency-budget.png` has two panels:
- the edge margins against the REQ-TX-006 offset, with the 750 Hz TBR, the 825.0 Hz limit and the F7 cases marked;
- the healthy disagreement and the largest undetected true error per route and interval (R3 at the 5 kHz threshold, R1 at the smallest threshold that avoids false trips), against the 5 kHz threshold and the 10 kHz REQ-SYS-154 limit.

The author opened and inspected it after two layout corrections (overlapping labels). Revision 1 re-rendered it and moved the two limit labels into the legend after one inspection showed them over the bars.

## 8. Per-case index

C-1 to C-7 band edges; C-8 to C-10 reference identities; C-11 sample; C-12w threshold within the REQ-SYS-182 window; C-12 no false trip per interval (R3); C-13 R1 per interval (informational, with the limits R1 needs); C-14 changeover time per alternative; C-15 transmit detection time; C-16 REQ-SYS-154 true-error limit per interval (R3); C-16a FC0 accuracy ceiling (informational); C-17 plausibility bound (informational); C-18 TC-SYS-101 12 kHz injection per interval; U-1 unlocked at key-down per alternative; U-2 unlocked during transmission. The REQ-SYS-154 cases are: off-frequency at key-down C-12.iv12, C-16.iv12, C-18.iv12; off-frequency during transmission C-12.iv13, C-16.iv13, C-18.iv13, C-15; unlocked at key-down U-1; unlocked during transmission U-2. Checker output lines carry the same ids.

## Change history

| Revision | Date | Change | Reason |
|---|---|---|---|
| 0 | 2026-09-27 | Initial issue, frozen for its first review (freeze F0, rule C2) | WP-PDR-20 wave 1a |
| 1 | 2026-09-27 | Section 3.3: measured threshold T = 5.0 kHz distinct from the REQ-SYS-154 true-error limit, with the no-false-trip and no-missed-trip conditions, the FC0 accuracy ceiling and the effect on TC-SYS-101 (cases C-12w, C-16, C-16a, C-18); unlocked-synthesizer cases at key-down and during transmission with the lock-detect means and time budget (U-1, U-2). Sections 1, 2, 4, 5, 6, 7, 8 and the figure follow. Minor findings 5 to 7 are not addressed in this revision (rule C1) | INSP-056 finding-1 and finding-2 (Major) |
