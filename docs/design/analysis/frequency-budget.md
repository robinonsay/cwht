# Frequency budget, band-edge guard and frequency-verification counter

| Field | Value |
|---|---|
| Product | `docs/design/analysis/frequency-budget.md` (analysis note, `analysis_kind`: budget, timing, worst-case) |
| Work package | WP-PDR-20 (`docs/plan/pdr-work-plan.md` section 3.6), wave 1a; **revision 2: WP-PDR-20a** (plan revisions 6 and 7, section 3.0 row 20: the route R3 budget of D-17, the Si5351A relock time against its 1 ms allocation, the TCXO ratio freshness over a long over against its 1 ppm allocation), wave W-A |
| Author | Claude, RF designer (TX) author invocation, 2026-09-27 (revisions 0 and 1); Claude, WP-PDR-20a analysis author invocation, 2026-09-29 (revision 2) |
| Checker | `hardware/sim/freq/freq_budget.py` (sections 3.1 to 3.3, unchanged in revision 2) and `hardware/sim/freq/r3_a5.py` (section 3.4, new in revision 2, run `r3a5-20260929-01`); one command each, section 7 |
| Figure | `docs/reviews/PDR/figures/frequency-budget.png` (sections 3.1 to 3.3); `hardware/sim/freq/results/r3a5-20260929-01/relock-sequence.png`, `ratio-freshness.png`, `xosc-slope.png`, `r3-budget-and-buffer.png` (section 3.4). All rendered and inspected (section 7) |
| Review record | `docs/reviews/PDR/checklists/analysis-frequency-budget-and-clock-plan.md` (INSP-056; one record for this note and `clock-plan.md`, plan section 3.6), with `docs/templates/peer-review-checklist-analysis.md` (on `cr/CR-012-pdr-checklist-templates`, not yet on `main`). Revision 2 is reviewed as the WP-PDR-20a delta of INSP-056 with its software assurance pair (plan row 20: "the INSP-056 and INSP-111 deltas with the SA pair"); the lead SE assigns the iterations |
| Evidence status | **Developer evidence** (05 section 9.1). Both checkers are class B scripts without a TV record; `r3_a5.py` also imports the WP-PDR-28a thermal model (`hardware/sim/thermal/thermal_model.py`, unchanged). Under CK-ANA-C2 no value here closes a requirement or goes to the owner as a TBR value until a TV record covers the checkers or the owner rules on developer evidence (section 6, item 1) |
| Staging | The guard values depend on REQ-TX-006 (750 Hz, TBR), which WP-PDR-22 confirms. The TS-007 part choice is decided at B1a. These values are finalized after WP-PDR-22 and ruled at B2 (plan WP-PDR-20 "Depends on"; rule C10) |
| AT RISK | Revisions 0 and 1: no. **Revision 2: AT RISK (A5 CRs)** (plan rules C8 and C13): section 3.4 uses REQ-SYS-160, 161 and 180 as they stand before the S1 disposition of CR-003 revision 4, CR-006 revision 3 and CR-018; it is re-checked against the disposition before F1 |

## 1. Question and scope

This note answers four questions:

1. Does the 1.2 kHz band-edge guard of REQ-SYS-008, REQ-SYS-009 and REQ-TX-002 keep the -60 dB keying-sideband point (REQ-TX-006) and the 26 dB bandwidth (REQ-SYS-015) inside 144.000 to 148.000 MHz? The check uses the +/-2.5 ppm reference of REQ-SYS-010 and the frequency-word error, at both band edges.
2. Which reference budget makes REQ-SYS-010 (+/-2.5 ppm for one year after calibration) and the band-edge guard hold even if the firmware calibration constant is wrong? What two-unit offset remains for RSK-002?
3. Can the independent frequency verification of REQ-SYS-182 and REQ-SYS-154 (HZ-008 K7) hold its 10 kHz window and 100 ms limit on the RP2350 crystal timebase? What prescaler ratio and sample does REQ-TX-013 need? How are both REQ-SYS-154 triggers ("unlocked" and "off its set frequency by over 10 kHz") detected at both moments ("on key-down" and "during transmission"), and how fast?
4. Which TBR values does this analysis propose, and which of them trigger the "else a CR" branch of their `tbr.plan`?
5. **(Revision 2, WP-PDR-20a.)** For A5, the design the owner chose (TS-012 revision 7 section 10; D-17), does route R3 still hold at the changeover and over a whole over? Three parts:
   - the Si5351A PLL A relock after the changeover writes, read from a source, against the 1 ms allocation of the TS-012 section 7.3 key-down sequence;
   - the age of the XOSC/TCXO ratio at each check, with the squaring stage off in transmission, against the 1 ppm XOSC drift allocation;
   - the receive-only TCXO squaring stage and the 150.000 MHz line.

   Both of the first two are TS-012 section 10 revisit conditions of revision 6. Section 3.4 answers them.

Identifiers served:
- Requirements: REQ-SYS-008, REQ-SYS-009, REQ-SYS-010, REQ-SYS-154, REQ-SYS-182, REQ-TX-002, REQ-TX-013.
- Inputs: REQ-TX-006, REQ-SYS-015, REQ-SYS-004, REQ-SYS-161.
- TPM-006 (`frequency-stability`); RSK-002 step S1; RSK-046 step S2.
- HZ-008 controls K4 and K7 (`docs/safety/hazards.json` 0.5.0-pha); SRR decisions 25 and 40.
- TS-007 criteria M3 and R-M3.
- Revision 2: TS-012 decision A5 and design items D-12 (C6), D-17 and D-18; TS-012 section 10 revisit conditions on the relock time and the ratio freshness; REQ-SYS-160, REQ-SYS-180; INSP-110 finding-25 (the squaring stage, as it bears on the refresh time).

The receiver phase-noise and reciprocal-mixing arithmetic is in TS-007 section 4 (criterion C1). The clock harmonics are in `docs/design/analysis/clock-plan.md`.

**Revision 2 and TS-007.** Sections 3.1 to 3.3 were written for the TS-007 alternatives: A1, a Si5351A with the carrier on its own PLL, and A2, the recommended LMX2571. TS-012 supersedes TS-007. A5 is neither alternative: the Si5351A of A1 is used, but its PLL A carries the receive LO and is retuned to the carrier at every changeover, as A2's synthesizer was. Section 3.4 governs for A5 wherever it differs from sections 3.3 and 4. The clk_sys 96 MHz re-run of `clock-plan.md` and the ADR-031 revision (also WP-PDR-20a) are not in this note.

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
| **Revision 2 inputs (section 3.4)** | | | |
| Si5351A timing | TRDY power-up time, "From VDD = VDDmin to valid output clock, CL = 5 pF, fCLKn > 1 MHz": typ 2 ms, max 10 ms. TFREQ output frequency transition time, "fCLKn > 1 MHz": max 10 us. TOE output enable time: max 10 us. **No PLL lock or relock time is given** | Skyworks Si5351A/B/C-B data sheet Rev. 1.3 (August 27, 2021), Table 5 "AC Characteristics", page 9. Read 2026-09-29 through the web-fetch tool from the Skyworks site (PDF SHA-256 `f3bc5285...a4851101f`); text taken with pdftotext in the session scratchpad; no file added to the repository | Datasheet |
| Si5351A status and reset | Register 0 bit 5 LOL_A, "PLL A Loss Of Lock Status ... 0: PLL A is operating normally. 1: PLL A is unlocked" (page 13). Register 177 PLLA_RST "Writing a 1 to this bit will reset PLLA. This is a self clearing bit". Data sheet Figure 10 applies the PLLA and PLLB soft reset (reg 177 = 0xAC) after a configuration write. I2C Standard-Mode 100 kbps or Fast-Mode 400 kbps, burst writes with auto address increment (data sheet section 5) | Skyworks AN619 Rev. 0.8 (September 23, 2021), Registers 0 and 177. Read as above (PDF SHA-256 `0135b3a3...4783f36b`) | Application note |
| C6 changeover writes | MSNA (reg 26 to 33, 8 bytes), CLK0 to CLK2 control (reg 16 to 18), output enable (reg 3), MSNB (reg 34 to 41, 8 bytes); optional PLL reset (reg 177) | `spurs-ts012.md` option C6; TS-012 D-12; register numbers from AN619 | Design (TS-012) |
| I2C SCL with the ADR-031 counts at clk_sys 96 MHz | about 256 kHz | `spurs-ts012.md` section 6, "I2C" (counts to be re-derived by WP-PDR-32) | Analysis |
| Key-down sequence | t0 = changeover command, after 1 ms sampling and the 2 ms make filter; 1 ms for writes and settle (allocation); FC0 interval 12 from t0 + 1 ms; 2 ms software; PA_EN at t0 + 7 ms; TX_KEY at t0 + 8 ms; ramp at t0 + 10 ms. The GVA-84+ is powered and its bias clamp released when TX_KEY, PA_EN and Q are all true (D-18) | TS-012 section 7.3 revision 6, D-18 | Design (TS-012) |
| Contact-to-RF latency | RF rise within 15 ms of each straight-key closure | REQ-SYS-160 (TBR) | TBR |
| Longest over with RF | RF ends 150 s to 180 s into continuous transmit and is held off until receive resumes | REQ-SYS-180 (TBR) | TBR |
| XOSC crystal curve | AT-cut cubic about its inflection: third-order coefficient 0.8e-4 to 1.3e-4 ppm/K^3, inflection 20 to 35 C, first-order term free inside the Table 596 band | Standard AT-cut crystal model (Bechmann's coefficients as summarized in the crystal literature); not in the corpus, not read in this invocation | **Estimate, Low** |
| Crystal temperature in service | -10 to +65 C | REQ-SYS-010 span; thermal note main-bay long-session value 57.8 C plus its band and the local rise | Estimate |
| Main-bay (Pico 2) temperature transients | the MAIN node of the thermal model, layouts A5-DC and A5-R4, ambients -10, 25, 45 C, with its 86 ranged inputs | `hardware/sim/thermal/thermal_model.py` (WP-PDR-28a, `thermal-ts012.md`), imported unchanged | Model (developer evidence) |
| Pico 2 local step at the changeover | 0.03 W change of the board's own dissipation, 47 K/W board to air, time constant 30 s (rate) | **Estimates, Low** (board area and a convective coefficient near 10 W/m2K) | Estimate |
| XOSC pushing at the changeover | 0.2 ppm | **Allocation** (3.3 V rail step); confirmed by measurement M-2 | Allocation |
| Squaring-stage settle after power-up | 50 ms | **Allocation**: a requirement on the stage that answers INSP-110 finding-25 | Allocation |

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

### 3.4 Route R3 for A5: Si5351A relock, ratio freshness and the receive-only squaring stage (revision 2, WP-PDR-20a)

**The A5 arrangement** (TS-012 D-12, D-17, D-18; the key-down sequence of TS-012 section 7.3, revision 6):
- The Adafruit Si5351A runs from the TG2520SMN on XA.
- In receive, PLL A drives CLK0, the LO, and PLL B drives CLK2, the 8 MHz BFO.
- At the changeover command t0, the C6 writes retune PLL A to the carrier multiplier, power up CLK1, power down CLK0 and CLK2, and park PLL B on the PLL A multiplier.
- The /8 prescaler drives GPIN0.
- The TCXO drives GPIN1 through a squaring stage that is powered only in receive.
- FC0 counts interval 12 before PA_EN and interval 13 during transmission, against the measured threshold T = 5.0 kHz.

Checker `hardware/sim/freq/r3_a5.py`, run `r3a5-20260929-01`: 23 PASS, 0 FAIL, 10 INFO. The case ids below are its output lines.

#### 3.4.1 Si5351A PLL relock at the changeover (TS-012 section 10, revisit condition 1)

**What the sources say.** The Skyworks data sheet (Rev. 1.3) and AN619 (Rev. 0.8) were read for a lock, settle or acquisition time (RL-0, RL-1). **Neither gives a PLL lock time or a relock time after a feedback-divider (MSNA) change.** Three timing values exist, and none of them decides:

| Sourced value | What it covers | Bearing on the relock |
|---|---|---|
| TFREQ, output frequency transition time, at most 10 us (fCLKn > 1 MHz) | a frequency change at an output | Table 5 does not say whether it covers a PLL feedback change or only a MultiSynth change. If it covers the MSNA retune, the relock fits the allocation with 0.34 ms to spare (RL-7a) |
| TRDY, power-up time, typ 2 ms, max 10 ms | power-up to a valid output: NVM copy, system initialization and PLL acquisition from power-up | A superset of a relock, so it is an upper bound only on that reading. At 10 ms it exceeds every settle time the sequence allows (RL-7b) |
| TOE, output enable time, at most 10 us | CLK1 enable | Negligible |

AN619 gives the lock status, register 0 bit 5 LOL_A, readable over I2C. It gives the PLL reset in register 177. The data sheet's Figure 10 procedure applies the reset after a configuration write; whether the changeover writes need it is not stated.

**Time the sequence allows.**
- The C6 writes are four I2C bursts of 28 data bytes. At 400 kHz Fast-Mode they take **0.650 ms**, or 0.723 ms with the reg 177 reset (RL-2). That leaves **0.35 ms** of the 1 ms allocation for the PLL to settle.
- At 100 kHz Standard-Mode the same writes take 2.6 ms (RL-2s).
- At the SCL of about 256 kHz that the ADR-031 counts give at clk_sys 96 MHz (`spurs-ts012.md` section 6), they take 1.016 ms, over the allocation before any settle time (RL-2b).
- One LOL_A read takes 0.098 ms, inside the 2 ms software allocation (RL-3).

Let L be the time from t0 to the start of the FC0 count, writes included. PA_EN must be set no later than 2 ms before the ramp. That is TX_KEY at t0 + 8 ms against the ramp at t0 + 10 ms, the drive power-up time the TS-012 sequence keeps.

| Case | Sequence | Largest L | Largest settle after the 0.65 ms writes |
|---|---|---|---|
| RL-4 | Interval 12, ramp kept at t0 + 10 ms (the TS-012 sequence with PA_EN at TX_KEY) | **2.0 ms** | 1.35 ms |
| RL-5 | Interval 12, ramp moved to t0 + 12 ms, the limit of both REQ-SYS-161 (12 ms) and REQ-SYS-160 (15 ms less the 3 ms before t0) | 4.0 ms, which is the TS-012 revisit threshold of 1 + 3 ms | 3.35 ms |
| RL-6 | Interval 13 at the changeover (the TS-012 fallback), ramp at t0 + 12 ms | **0 ms** | none |

**Reading.**
- The 1 ms allocation is **not confirmed by a source**. The relock time is not specified.
- The revisit condition is therefore neither triggered nor excluded by the read. The source bounds a relock at 0.01 ms if TFREQ applies, and at 10 ms only through TRDY.
- The TS-012 fallback rule for a triggered condition (the check moves to interval 13 and the ramp to 11.5 ms) is no remedy for a slow relock. Interval 13 at the changeover leaves no time for any relock with the 2 ms drive power-up before the ramp (RL-6). TS-012's fallback keeps only 0.5 ms between PA_EN at t0 + 11 ms and the ramp at t0 + 11.5 ms, which WP-PDR-23a has to accept or reject. The fallback still serves its other trigger, an FC0 known-clock check above 560 Hz, if 23a accepts the 0.5 ms.

**Why the relock time is an availability question, not a safety one.** The key-down check is self-validating. A count taken while PLL A is still settling includes the old LO frequency, 8 MHz away. At interval 12, a transient of more than about 2.5 us inside the 4 ms count moves the mean by more than T (8 MHz x 2.5 us / 4 ms = 5 kHz), so PA_EN stays low. That is a late or lost first element, not RF at an unchecked frequency.

A transient that averages inside T while the loop ends at a wrong frequency is caught by the interval-13 checks during transmission, within the 46 ms of C-15. That is inside the 100 ms "or end it" branch of REQ-SYS-182. This is the argument the INSP-118 record makes for the allocation (`ts-012-design-to-cost-software-assurance.md`, item (3)); it holds for any relock time.

**Design response (proposal; requests in section 5).**
1. **Lock-gated start.** SW-SYNTH issues the C6 writes at t0, with MSNA first. It then polls LOL_A until the bit reads 0, and starts FC0 interval 12 on GPIN0 at the first 0 read, and no later than t0 + L_max. Here L_max = 2.0 ms, so the TS-012 ramp at t0 + 10 ms is kept.
   - If LOL_A is still 1 at L_max, or the count disagrees, PA_EN is not set for that element.
   - LOL_A is not credited as proof of settling. AN619 describes it as a reference or lock-range fault indication, so the FC0 count stays the credited means.
   - The lead-in stays constant (REQ-SYS-161), because the ramp time does not depend on when the count starts.
2. **I2C at Fast-Mode.** Derived constraint: SCL of at least 263 kHz, so that the 260 SCL clocks of the C6 writes and a TFREQ-scale settle fit the 1 ms allocation (RL-2b); 400 kHz is recommended. The WP-PDR-32 re-derivation of the I2C counts at 96 MHz must meet it.
3. **No reg 177 reset at the changeover**, unless measurement M-1 shows that the retune needs it. A reset restarts acquisition, and the data sheet gives no time for it.
4. **Measurement M-1** (dev board: a Pico 2 and the Adafruit Si5351A with a 25 MHz reference; 07 WP-SW-14, beside the FC0 known-clock check):
   - Set CLK1 to VCO/48 (about 17 to 18.5 MHz, inside the GPIN limit).
   - Issue the C6 writes from an LO setting to a carrier setting at 144.010, 146.000 and 147.990 MHz.
   - Time the settle two ways. First, poll LOL_A with timestamps. Second, start an interval-12 count at a delay D after the last write, stepping D from 0 to 3.4 ms in 0.05 ms steps over repeated changeovers. The smallest D whose counts all agree within T/8 at the counted input bounds the settle, because any transient longer than about 2.5 us inside a count fails it (see above).
   - Short intervals (8 or 9) are too coarse for this: 8 kHz at the input at interval 8.
   - Take 20 changeovers at each frequency.
   - Pass: settle at most 0.35 ms, which keeps the 1 ms allocation at 400 kHz. If it is at most 1.35 ms, the sequence stands with L_max = 2.0 ms. If it is at most 3.35 ms, the ramp moves toward t0 + 12 ms, a WP-PDR-23a timing-table change inside REQ-SYS-161 and REQ-SYS-160 with no requirement delta. Above that, a design change is needed: for example, retune at the first key sample instead of at t0, which gains up to the 3 ms of sampling and make filter and needs a receive-restore path for a rejected closure.

**Finding 3.4.1.**
- Revisit condition 1 is **open, not triggered by the source read**. The source does not specify the relock time.
- WP-PDR-32 and WP-PDR-36a can be written now: the lock-gated structure, the pins and the timing table do not depend on the measured value, which only sets L_max and, in the worst branch, the ramp time.
- No requirement or CR-018 row changes.
- The TS-012 fallback rule does not cover this trigger (RL-6). That is a request to WP-PDR-54 (the TS-012 record) and to WP-PDR-23a.

#### 3.4.2 XOSC/TCXO ratio freshness (TS-012 section 10, revisit condition 2)

**Where the ratio's age matters.**
- The squaring stage is off from t0 until receive resumes, so every check during an over uses the last ratio taken before the over.
- The ratio's age at a check is its age at t0, plus the time into the over. RF can run at most 180 s into an over (REQ-SYS-180), so no check with RF comes later than that.
- The first element's check is at interval 12, whose drift ceiling is 4.26 ppm at zero margin (FR-5). The checks during the over are at interval 13, whose ceiling is 17.77 ppm (FR-6). The ceiling is the largest drift for which T = 5.0 kHz still meets d < T and T + d <= 10 kHz.
- Revision 1 put one 1 ppm allocation on both.

**Drift bound.** The drift is the XOSC slope times the crystal's temperature change, plus pushing.

| Term | Value | Basis |
|---|---|---|
| Largest XOSC slope in service | **0.924 ppm/K** (FR-1) | 15 392 AT-cut curves admitted inside the +/-30 ppm Table 596 band over -40 to +85 C. Largest slope over -10 to +65 C: at 25 C, first-order term -0.924 ppm/K, third-order 1.3e-4 ppm/K^3 (`xosc-slope.png`). Estimate, Low |
| Main-bay (Pico 2) change over the window W = A_kd + 180 s = 190 s | nominal **2.589 K** (A5-R4 at -10 C, continuous transmit from the receive steady state), RSS band +2.404 K, total **4.993 K** (FR-3) | Thermal model MAIN node, both A5 layouts, three ambients, heating and cooling (`ratio-freshness.png` left). The band is dominated by the feed resistance: r_feed 0.26 to 0.45 ohm adds 2.245 K, and c_main 40 to 90 J/K adds 0.812 K |
| Pico 2 local step | 1.41 K (0.03 W x 47 K/W, taken in full with no time-constant credit) | Estimate, Low |
| Pushing | 0.2 ppm | Allocation (M-2) |
| **Drift over the longest over** | 0.924 x (4.993 + 1.41) + 0.2 = **6.116 ppm** (FR-4) | |

**Reading.**
- **Revisit condition 2 is triggered as worded.** The ratio cannot be kept within 1 ppm over the longest over: the bound is 6.12 ppm, and at the bounding rates the drift reaches 1 ppm after about 10 s (A_kd below).
- The bound also exceeds the interval-12 ceiling of 4.26 ppm (FR-5). So an aged ratio must never serve an interval-12 check.
- It is well inside the interval-13 ceiling of 17.77 ppm.
- The budget therefore closes, **with no requirement change**, by splitting the drift term by check:

| Check | Ratio age | Drift allocation | Healthy d | Margin to T | Largest undetected true error | 12 kHz injection |
|---|---|---|---|---|---|---|
| B-*.iv12: key-down, before PA_EN | at most **A_kd = 10 s** | 1 ppm (unchanged) | 4 518.0 Hz | 482.0 Hz | 9 518.0 Hz (margin 482.0 Hz) | trips, margin 2 482.0 Hz |
| B-*.iv13: during the over | at most A_kd + 180 s | **6.5 ppm** (proposed: the 6.116 ppm bound rounded up to 0.5 ppm) | 3 332.0 Hz | 1 668.0 Hz | 8 332.0 Hz (margin 1 668.0 Hz) | trips, margin 3 668.0 Hz |

**A_kd.** A_kd is the largest ratio age at the key-down check for which the drift stays within 1 ppm. The largest rate of change is 0.035 K/s in the main bay (0.017 K/s nominal plus its band, over any window) plus 0.047 K/s from the local step (1.41 K over a 30 s time constant). With the 0.2 ppm pushing, the limit is 10.57 s, and **A_kd = 10 s** is proposed (FR-2: 0.957 ppm).

In receive the ratio is never older than 1.082 s: the 1 s refresh plus the 50 ms stage settle and the 32 ms interval-15 count (FR-2r). So A_kd binds only on a key-down that follows an over by less than one refresh.

**Two rules the split needs** (requests to WP-PDR-23a, 32 and 35, section 5):
- **R-FRESH-1: refresh at once on return to receive.** When receive resumes after an over, the squaring stage is powered and one ratio refresh is started at once.
- **R-FRESH-2: no interval-12 check on a ratio older than A_kd.** If the ratio is older than 10 s at t0, because the operator keyed again before the refresh of R-FRESH-1 completed, PA_EN is not set on the aged ratio. One refresh (at most 82 ms) completes first.
  - Whether the changeover waits for it (that element is then late, outside REQ-SYS-160) or the element is not radiated is for 23a and 32 to fix. Both outcomes are on the safe side.
  - The case needs a key-down within about 82 ms of the hang expiring, after an over longer than 10 s.

**FC0 is a single counter.** A refresh in progress at t0 must be abandoned so that the interval-12 count can start at t0 + L. R-FRESH-2 then decides whether the older ratio may be used. WP-PDR-32 confirms from the RP2350 data sheet that writing FC0_SRC stops a count in progress. This invocation did not read the RP2350 data sheet.

**Measurement M-2** (the assembled unit on the bench, 07 WP-SW-14 and the WP-PDR-43 bench plan):
- Log the ratio in receive, averaging 16 interval-15 counts for a resolution near 0.6 ppm. The averaging holds if the count quantization dithers; if it does not, build a longer software gate from successive counts.
- Transmit into the dummy load at 5 W, at the highest duty the keyer limits allow, until REQ-SYS-180 ends RF (150 to 180 s).
- Log the ratio at once on return to receive.
- Pass: the change is at most 6.5 ppm, and the step across one changeover without RF (pushing) is at most 0.2 ppm.

**Finding 3.4.2.**
- Revisit condition 2 **triggers as worded**: 6.12 ppm over the longest over, against 1 ppm.
- The route R3 budget still closes for REQ-SYS-154 and REQ-SYS-182 **as written, with T = 5.0 kHz and intervals 12 and 13 unchanged**. It needs the ratio-age rule at the key-down check (A_kd = 10 s, with R-FRESH-1 and R-FRESH-2) and a 6.5 ppm drift allocation for the checks during the over.
- No CR-018 row changes. Under the plan's rule for this condition (plan section 10.6, the "§10 revisit conditions of revision 6" row: "a trigger goes to the owner at S1 if it changes CR-018, else at S2"), the trigger goes to the owner at S2.
- The TS-012 fallback (interval 13 at the changeover) is not needed for this trigger.

#### 3.4.3 Receive-only squaring stage and the 150.000 MHz line

- **In transmission.** The stage's supply is off from t0 until receive resumes, so the stage adds nothing to the 150.000 MHz line (25 MHz x 6). The `spurs-ts012.md` figure stands: plan PB high estimate -12.1 dBm at the SMA, 3.9 dB over 25 uW, a residual line closing at the bench (BL-2).
  - The unpowered stage's input must neither load nor rectify the TCXO, which also drives XA. That needs a partial-power-down input, or an isolating series element sized with the stage: a part constraint for WP-PDR-37 and 38.
- **In receive.** Harmonics 1 to 8 of the squared 25 MHz, with the 2.5 ppm TCXO tolerance, fall in none of the receive windows: 144.010 to 147.999 MHz, the 8 MHz IF, the LO and image bands for either injection side (BL-1, `r3-budget-and-buffer.png` right). The nearest is 150.000 MHz, 2.0 MHz above the receive range. The stage adds level, not new frequencies, to the 25 MHz lines `clock-plan.md` already carries.
- **Refresh time.** The 50 ms settle allocation plus the 32 ms interval-15 count is 82 ms per refresh, 8.2 % of receive if the stage is power-cycled each second (B-19). It can also stay on through receive, which only helps.
- **The stage itself is not designed here.** TS-012 revision 8 section 8.1 note 3 records INSP-110 finding-25: a 74LVC1G17 Schmitt buffer cannot be self-biased, and a stage that toggles at the TCXO's 0.8 V peak-to-peak minimum is still to be named. The 50 ms settle allocation is a requirement on that stage. Its valid-clock run is requested of WP-PDR-20b, beside the prescaler-tap run at 1.66 Vpp. Until it runs, a stage that does not toggle reads as FC0 DIED, so RF is withheld: safe, but at a cost in availability.

#### 3.4.4 The unlocked trigger on A5, and I2C during transmission

For A5 the device lock-detect indication of U-1 and U-2 is the Si5351A **LOL_A bit** (AN619 register 0 bit 5), read over I2C. This closes, for A5, the research gap of section 3.3: the lock-detect form was a TS-007 value-of-information item 4 question for the LMX2571, and the "else a CR" branch for a part without a lock-detect indication no longer applies.
- **U-1 (key-down) is unchanged.** The read after the writes and before PA_EN is inside the 2 ms software allocation (RL-3). The A5 changeover time is 1 + 4 + 2 = 7.0 ms with the allocation, and at most 2.0 + 4 + 2 = 8.0 ms with L_max. Both are inside the 12 ms lead-in.
- **U-2 (during transmission) conflicts with D-12 (C6: "I2C only in the lead-in").** U-2 samples the indication at least every 10 ms during transmission, and on the 10-MSOP Si5351A that is an I2C read, since only the Si5351C has an INTR pin (data sheet section 4.6). TS-012 and the spur plan admit no I2C traffic in transmission. The options, for WP-PDR-32 and 35 with the spur plan's owner:
  - (a) Admit one register-0 read (4 bytes, 0.098 ms at 400 kHz) per 10 ms service period, and add its SCL line set to the transmit spur inventory.
  - (b) Read LOL_A only in key-up gaps and at each element's key-down. Then an unlock that stays inside T during a long element is caught only by the counter once it drifts past T.

  This note does not choose. With (b), the REQ-SYS-154 "unlocked during transmission" case rests on the counter alone, and the U-2 row of section 3.3 must be restated. Whether that needs a REQ-SYS-154 wording CR is a question for the requirement owner (the owner, on the WP-PDR-35 proposal).

**Finding 3.4.** Route R3 holds for A5 with REQ-SYS-154 and REQ-SYS-182 as written and the section 3.3 threshold, intervals and times unchanged, on these conditions:
- the lock-gated changeover (L_max 2.0 ms, Fast-Mode I2C of at least 263 kHz);
- the ratio-age rule at the key-down check (A_kd 10 s, R-FRESH-1 and R-FRESH-2);
- the interval-13 drift allocation of 6.5 ppm.

The two TS-012 revisit conditions stand as follows:
- **Relock: open**, not triggered by the source read; closure by M-1.
- **Freshness: triggered as worded**, and closed in the budget without a requirement change; confirmation by M-2.

Two items are open for other writers: the U-2 I2C conflict, and the squaring stage of INSP-110 finding-25.

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

**Revision 2 (A5, section 3.4).** No proposed value in this table changes:
- **REQ-SYS-154 and REQ-SYS-182** keep 10 kHz, 100 ms and T = 5.0 kHz on route R3, with the section 3.4 conditions: the lock-gated changeover, the ratio-age rule at the key-down check (A_kd = 10 s) and the 6.5 ppm interval-13 drift allocation.
- **Changed margins.** The margins at interval 13 fall from 2 482.0 Hz to 1 668.0 Hz, because the drift allocation there rises from 1 to 6.5 ppm. The interval-12 margins are unchanged at 482.0 Hz.
- **REQ-SYS-154, "else a CR" column.** For A5 the lock-detect indication exists (Si5351A LOL_A), so the LMX2571 branch no longer applies. It is replaced by the open U-2 question of section 3.4.4: if lock status is not read during transmission, the unlocked trigger during transmission rests on the counter, and the requirement owner decides whether the REQ-SYS-154 wording needs a CR.
- **Revisit conditions.** The TS-012 conditions give no value change: the relock condition is open (M-1), and the freshness condition triggered and closed in the budget (M-2 confirms). Under rule C10 these values still go to the owner only on this note's APPROVED record.

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

**Revision 2 requests (section 3.4; A5). This note edits none of these files.**

| To | Request |
|---|---|
| WP-PDR-23a (key-down and key-up sequence, ICD-TX-SW timing table) | Write the changeover as lock-gated: C6 writes at t0 with MSNA first, LOL_A polled, FC0 interval 12 started at the first LOL_A = 0 or at t0 + L_max = 2.0 ms, PA_EN only on agreement, and the ramp fixed at t0 + 10 ms so that the lead-in stays constant. Carry the M-1 branches: settle at most 1.35 ms, sequence unchanged; at most 3.35 ms, ramp toward t0 + 12 ms. Accept or reject the TS-012 fallback's 0.5 ms from PA_EN to the ramp: with the 2 ms drive power-up of the nominal sequence, interval 13 at the changeover leaves no relock time (RL-6). Fix the R-FRESH-2 outcome for a key-down on a ratio older than A_kd = 10 s: late element or element not radiated |
| WP-PDR-32 (software architecture) | The lock-gated changeover and the L_max deadline. I2C SCL of at least 263 kHz in the count re-derivation at clk_sys 96 MHz (400 kHz recommended; 256 kHz fails, RL-2b). No reg 177 reset at the changeover unless M-1 needs one. FC0 as a single counter: confirm from the RP2350 data sheet that writing FC0_SRC stops a count in progress, so that a receive refresh can be abandoned at t0. R-FRESH-1 and R-FRESH-2. Resolve the U-2 I2C conflict of section 3.4.4, option (a) or (b), with the spur plan's owner |
| WP-PDR-35 (`docs/requirements/sw/**`) | SW-SAFE: the ratio age at an interval-12 check is at most 10 s, else no PA_EN on that ratio; refresh at once on return to receive; checks during an over at interval 13 only; the 6.5 ppm drift allocation is the design basis for T at interval 13 (T itself unchanged at 5.0 kHz). SW-SYNTH: LOL_A (Si5351A register 0 bit 5) is the lock-detect indication, read after the C6 writes and before PA_EN; the read during transmission follows the WP-PDR-32 resolution of U-2. HostUnit cases: an injected ratio age of 9.9 and 10.1 s at key-down; a LOL_A that stays 1 until after L_max; a refresh abandoned at t0 |
| WP-PDR-36a (`ICD-CTL-SW` pin map) | No change from revision 1: GPIN0 carrier/8, GPIN1 TCXO from the squaring stage (GPIO 20 and 22, or 12 and 14). Add one GPIO for the squaring-stage supply switch (on in receive, off from t0), unless WP-PDR-37 derives it from an existing receive-only rail. No lock-detect pin: the 10-MSOP Si5351A has none |
| WP-PDR-20b | The squaring stage that answers INSP-110 finding-25, with its valid-clock run at the TCXO's 0.8 V peak-to-peak minimum and the Si5351A XA input in parallel. Its settle after power-up must be at most 50 ms. Its unpowered input must neither load nor rectify the TCXO |
| WP-PDR-37 and 38 (schematic, BOM) | The squaring stage part with a partial-power-down input (or an isolating element) and a switched supply. The Si5351A I2C bus on its own RP2350 instance (TS-007 SA finding-3) with pull-ups sized for Fast-Mode |
| WP-PDR-43 (V&V plan), 07 WP-SW-14 (dev-board checks) | M-1: Si5351A relock time after the C6 writes (section 3.4.1, pass criteria there). M-2: XOSC/TCXO ratio change over a 180 s transmission and across a changeover without RF (section 3.4.2; pass at most 6.5 ppm and 0.2 ppm). Both beside the FC0 known-clock check (560 Hz at interval 12) |
| WP-PDR-54 (TS-012 record, sole writer) | TS-012 section 10, revision 6 revisit conditions: relock **open**, not triggered by the source read (Si5351A data sheet Rev. 1.3 and AN619 Rev. 0.8 give no relock time), closing by M-1; freshness **triggered as worded** (6.12 ppm over the longest over), closed in the budget without a requirement change (A_kd 10 s at interval 12, 6.5 ppm at interval 13); the stated consequence "the check moves to interval 13 and the lead-in to 11.5 ms" does not remedy a slow relock (RL-6). For the owner at S2 (plan section 10.6 row) |
| WP-PDR-16b (`docs/safety/hazards.json`) | HZ-008 K7, in addition to the revision 1 wording: the ratio used at the key-down check is at most 10 s old. HZ-008 C8: the lock-detect indication on A5 is Si5351A LOL_A |

## 6. Uncertainty and limitations

1. **Tool status.** The checker has no TV record. Its arithmetic has three known-answer self-checks (KA-1 to KA-3) and can be recomputed by hand from the tables above. Before the section 4 values go to the owner, a TV record must cover `hardware/sim/freq/*.py`, or the owner must rule to accept developer evidence. The lead SE decides which route (return, open_questions).
2. **Allocations are not datasheet values.** The allocations include the TCXO uncalibrated total, aging, supply and load, calibration uncertainty, software latency and service period. Each is a requirement on a later design or part choice, verified at CDR (datasheet Inspection, WP-PDR-32 timing analysis). A part that misses an allocation re-opens this note.
3. **REQ-TX-006 dominates the guard margin.** The 75.0 Hz margin is smaller than any plausible uncertainty of a simulated -60 dB offset. The guard is only as good as the WP-PDR-22 corner analysis.
4. **FC0 accuracy semantics.** Table 541 gives "accuracy" per interval without saying whether it is a bound or a typical value. This note treats it as a +/- bound at the counted input. The dev-board check of 07 WP-SW-14 is to confirm it with a known clock, against the 560 Hz ceiling at interval 12 that the 5.0 kHz threshold needs (C-16a).
5. **XOSC bound.** 65 ppm is the Table 596 sum over -40 to +85 C. Over -10 to +45 C the true value is smaller, so R1's result is conservative.
6. **LMX2571 retune time.** "FastLock < 1.5 ms" (F20) is a datasheet feature statement. Its conditions for a 12 MHz jump (RX LO to TX carrier with a 9 to 10.7 MHz IF) are not in the corpus. C-14.A2 has 4.5 ms of margin for it.
7. **Lock-detect form.** The LMX2571 lock-detect indication and its latency are not in the corpus (TS-007 value-of-information item 4, as INSP-055 finding-4 asks it to be extended). U-1 and U-2 assume the indication is valid within the 10 ms sample period. **Revision 2:** for A5 the indication is the Si5351A LOL_A bit (AN619). Its latency after a real loss of lock is not specified; AN619 ties it to a reference outside the lock range or an invalid reference.
8. **(Revision 2) The relock time is unspecified.** Section 3.4.1 rests on the absence of a value in the data sheet and AN619, and on the self-validating check. The 0.650 ms write time assumes 9 SCL clocks per byte plus one per START and STOP at exactly 400 kHz. A slower SCL or clock stretching lengthens it in proportion.
9. **(Revision 2) The XOSC slope is a model.** The AT-cut cubic, its third-order coefficient and its inflection are literature values, not a datasheet read (Low). The slope bound comes from the Table 596 band, which bounds the first-order term. A crystal outside that band, or a different cut, re-opens section 3.4.2.
10. **(Revision 2) The crystal temperature is the thermal model's MAIN node.** That node lumps the main-bay air, the main board and the Pico 2 (c_main 40 to 90 J/K). The crystal's own lag behind the node is not credited. The local Pico 2 step (0.03 W, 47 K/W) is an estimate taken in full, and the band is a one-at-a-time RSS, as in the thermal note. M-2 measures the result directly.
11. **(Revision 2) Continuous transmit bounds the heating.** The heating case keys the transmitter for the whole 190 s window, which REQ-SYS-055 and the keyer never allow (13 s key-downs at most), so it bounds any keying pattern from above. The cooling case starts from the continuous steady state, which is not reachable in service either.

## 7. Reproduction and visual closure

```
cd /Users/robinonsay/rust/cwht && .venv/bin/python hardware/sim/freq/freq_budget.py --plot
```

Expected: 35 PASS, 0 FAIL, 4 INFO lines, exit status 0 (revision 1, run 2026-09-27). The figure `docs/reviews/PDR/figures/frequency-budget.png` has two panels:
- the edge margins against the REQ-TX-006 offset, with the 750 Hz TBR, the 825.0 Hz limit and the F7 cases marked;
- the healthy disagreement and the largest undetected true error per route and interval (R3 at the 5 kHz threshold, R1 at the smallest threshold that avoids false trips), against the 5 kHz threshold and the 10 kHz REQ-SYS-154 limit.

The author opened and inspected it after two layout corrections (overlapping labels). Revision 1 re-rendered it and moved the two limit labels into the legend after one inspection showed them over the bars.

**Revision 2 (section 3.4):**

```
cd /Users/robinonsay/rust/cwht && .venv/bin/python hardware/sim/freq/r3_a5.py --run-id r3a5-20260929-01
```

Expected: 23 PASS, 0 FAIL, 10 INFO lines, exit status 0 (run 2026-09-29, about 5 s). The run directory `hardware/sim/freq/results/r3a5-20260929-01/` holds `checker-output.txt`, `results.json` (every case, the relock and freshness summaries, the thermal cases and tornado, the buffer lines), a copy of the script and four figures:
- `relock-sequence.png`: the key-down timelines (TS-012, latest with the ramp kept, latest with the ramp at 12 ms, the interval-13 fallback) and the sourced timing values against the settle budget on a log scale;
- `ratio-freshness.png`: the MAIN-node change over the over (both A5 layouts, three ambients, heating and cooling) and the drift bound against the ratio age, with the 1 ppm and 6.5 ppm allocations and the two ceilings;
- `xosc-slope.png`: the admissible AT-cut curves in the Table 596 band and the slope envelope in service;
- `r3-budget-and-buffer.png`: d and T + d per check against T and 10 kHz, and the 25 MHz harmonics against the receive windows.

`freq_budget.py` is unchanged and still gives 35 PASS, 0 FAIL. The author opened each revision 2 figure after rendering and re-rendered two of them after one inspection: labels over the title in `r3-budget-and-buffer.png`, and the 12 ms label over the title in `relock-sequence.png`.

## 8. Per-case index

C-1 to C-7 band edges; C-8 to C-10 reference identities; C-11 sample; C-12w threshold within the REQ-SYS-182 window; C-12 no false trip per interval (R3); C-13 R1 per interval (informational, with the limits R1 needs); C-14 changeover time per alternative; C-15 transmit detection time; C-16 REQ-SYS-154 true-error limit per interval (R3); C-16a FC0 accuracy ceiling (informational); C-17 plausibility bound (informational); C-18 TC-SYS-101 12 kHz injection per interval; U-1 unlocked at key-down per alternative; U-2 unlocked during transmission. The REQ-SYS-154 cases are: off-frequency at key-down C-12.iv12, C-16.iv12, C-18.iv12; off-frequency during transmission C-12.iv13, C-16.iv13, C-18.iv13, C-15; unlocked at key-down U-1; unlocked during transmission U-2. Checker output lines carry the same ids.

Revision 2 (`r3_a5.py`):
- KA-R1 to KA-R3 known answers.
- RL-0 to RL-8 relock: sources; writes at 400 kHz, 256 kHz and 100 kHz; the LOL_A read; L max per sequence; the TFREQ and TRDY readings; the verdict.
- FR-1 to FR-6 freshness: slope bound; A_kd; the receive age; the window; the drift over the over; the interval-12 and interval-13 ceilings.
- B-11, B-12.iv12 and iv13, B-15, B-16.iv12 and iv13, B-18.iv12 and iv13, B-19: the A5 budget and the refresh time.
- BL-1 and BL-2: the squaring-stage lines in receive and in transmission.

For A5 the REQ-SYS-154 cases are: off-frequency at key-down B-12.iv12, B-16.iv12, B-18.iv12 with FR-2; off-frequency during transmission B-12.iv13, B-16.iv13, B-18.iv13, B-15 with FR-6; unlocked at key-down U-1 (section 3.4.4, RL-3); unlocked during transmission U-2, open on the I2C conflict of section 3.4.4.

## Change history

| Revision | Date | Change | Reason |
|---|---|---|---|
| 0 | 2026-09-27 | Initial issue, frozen for its first review (freeze F0, rule C2) | WP-PDR-20 wave 1a |
| 1 | 2026-09-27 | Section 3.3: measured threshold T = 5.0 kHz distinct from the REQ-SYS-154 true-error limit, with the no-false-trip and no-missed-trip conditions, the FC0 accuracy ceiling and the effect on TC-SYS-101 (cases C-12w, C-16, C-16a, C-18); unlocked-synthesizer cases at key-down and during transmission with the lock-detect means and time budget (U-1, U-2). Sections 1, 2, 4, 5, 6, 7, 8 and the figure follow. Minor findings 5 to 7 are not addressed in this revision (rule C1) | INSP-056 finding-1 and finding-2 (Major) |
| 2 | 2026-09-29 | WP-PDR-20a, for A5 (TS-012 revision 7 decision; D-12, D-17, D-18). New section 3.4 with the checker `r3_a5.py` (run `r3a5-20260929-01`). Si5351A relock read from the data sheet Rev. 1.3 and AN619 Rev. 0.8: no relock time specified; the lock-gated changeover with L_max 2.0 ms; Fast-Mode I2C constraint; M-1. Ratio freshness: 6.12 ppm over the longest over, triggering the TS-012 condition as worded; the budget closes with A_kd = 10 s at the key-down check and 6.5 ppm at interval 13; R-FRESH-1, R-FRESH-2; M-2. Squaring stage and the 150 MHz line; LOL_A as the A5 lock-detect indication; the U-2 I2C conflict. Header, sections 1, 2, 4 to 8 follow. Sections 3.1 to 3.3, `freq_budget.py` and `frequency-budget.png` unchanged. INSP-056 Minor findings 5 to 7 and 9 not addressed (rule C1) | WP-PDR-20a (plan revisions 6 and 7, section 3.0 row 20); TS-012 section 10 revisit conditions of revision 6 |
