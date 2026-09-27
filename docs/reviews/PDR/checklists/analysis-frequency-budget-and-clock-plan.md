---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md section 13;
# docs/process/08-agent-briefing.md sections 3.4 and 3.5). Independent review of the two WP-PDR-20 analysis
# notes, one record as PDR work plan section 3.6 names it. Iteration 1 at freeze F0 (rule C2).
# X-1 (checklist field): the item set applied is docs/templates/peer-review-checklist-analysis.md revision A,
# blob 0386cc6e, on branch cr/CR-012-pdr-checklist-templates at 7784672 (reviewed by INSP-031, CR-012 not
# merged). The template is not on main, and tools/validate_docs.py rejects a checklist field whose template is
# absent from docs/templates/, so the field names the design checklist (SEMP section 7.2 design analyses), as
# INSP-040 and INSP-041 did for the branch-only tool-validation template. The delta iteration after CR-012
# merges switches the field to peer-review-checklist-analysis.
# Iteration 2 (delta, rule C1) at the re-freeze F0 commit 802347b: the four Major fixes of iteration 1, on the
# seven blobs below (ADR-031 is now in product_files, so its record is this one). CR-012 is still not merged at
# 8abb467 (branch cr/CR-012-pdr-checklist-templates), so X-1 stands and the checklist field is unchanged.
id: INSP-056
checklist: peer-review-checklist-design
checklist_revision: A
checklist_file: docs/reviews/PDR/checklists/analysis-frequency-budget-and-clock-plan.md
product: docs/design/analysis/frequency-budget.md
product_commit: "802347bb9b6549fe7ee4a8005ce7605fc2cabc3a"
product_files: ["docs/design/analysis/frequency-budget.md@79d47fbbcae7fbfc5dde43ebde5c6e6b20917f94", "docs/design/analysis/clock-plan.md@8582121a860eb75dd093b62c9d6bb03cd5acd363", "hardware/sim/freq/freq_budget.py@d82269e6e9a7b2312d85c227d29de55236cdacc5", "hardware/sim/freq/clock_plan.py@b939229725b0e1f37a723d7399dcda72c990a8fe", "docs/reviews/PDR/figures/frequency-budget.png@d77a0b3afac520643fdda042d188612b9123848e", "docs/reviews/PDR/figures/clock-plan-harmonics.png@19f47e3d8a1307ec478b98be68f673da08191562", "docs/decisions/adr/ADR-031-clock-plan.md@a578ca16aa6e5d23269b2591205f3d1e696ebf14"]
analysis_kind: [budget, timing, worst-case, other]
product_size: 2 notes and 1 ADR; 39 checker cases (35 PASS, 4 INFO) and 28 clock rows (4 named residual sources) in 6 IF plans; 2 checkers; 2 plots
tools_used: ["venv Python 3.13.5 (TV-001 accredits the interpreter; no TV record covers hardware/sim/freq/*.py, developer evidence per 05 section 9.1)"]
values_proposed: ["REQ-SYS-008: 144.0012 to 147.9988 MHz", "REQ-SYS-009: 144.0012 to 147.9988 MHz", "REQ-TX-002: 144.0012 to 147.9988 MHz", "REQ-SYS-010: +/-2.5 ppm, -10 to +45 C, one year after calibration", "REQ-SYS-154: 10 kHz true-error limit, measured SW-SAFE threshold 5.0 kHz (route R3), lock-detect primary for the unlocked trigger", "REQ-SYS-182: 10 kHz and 100 ms (route R3)", "REQ-TX-013: fixed ratio 8, sample below 20 MHz, within 1 kHz", "REQ-SYS-034: 144.010 to 147.999 MHz, 3 dB above MDS", "TPM-006: cbe 0.834 / 0.984 / 1.234 ppm by class, credit false"]
renders_inspected: 2
sprint: PDR-prep
author_agent: "author:WP-PDR-20 wave 1a (Claude as RF designer TX)"
reviewer_agent: "reviewer:WP-PDR-20-analysis-iter2 (independent; authored no part of WP-PDR-20; iteration 1 by reviewer:WP-PDR-20-analysis-iter1)"
# criticality: the frequency budget sets the window, times and calibration bound of the SW-SAFE frequency
# verification unit and the SW-SYNTH frequency-word path (07 section 14.1, safety-critical by SRR decision 9);
# section J answered here
criticality: safety-critical
# assurance_required: iteration 1 set false (a stand-alone analysis note is not a row of 07 section 2.1.1).
# Iteration 2: ADR-031 is now a product file of this record, and 07 section 2.1.1 row "Trade studies and ADRs
# whose decision constrains a safety-critical or mission-critical component" applies: ADR-031 section 2 item 4
# fixes configuration constants of the WP-SW-11 clocks driver and of SW-SYNTH (SPI divisor 8), both
# safety-critical in 07 section 14.1 (ADR-031 section 4.3 names WP-SW-11 safety-critical), and item 8 adds SW
# requirements (GPIO23, I2C traffic rule). The SA pair is a separate invocation (rule C4); it is not done here
assurance_required: true
assurance_reviewer_agent: "pending (software assurance pair of INSP-056 for ADR-031, to be dispatched by the lead SE; 07 section 2.1.1)"
iteration: 2
readiness_met: true
reviewer_verdict: NEEDS CHANGES
assurance_verdict: pending
verdict: NEEDS CHANGES
findings_major: 5
findings_minor: 4
findings_open: 5
findings_fixed: 0
findings_verified: 4
findings_deferred: 0
assurance_tasks_applied: [swe-070 7.1 task 1, swe-134 7.1 task 1, swe-134 7.1 task 6]
deferred_rids: []
items_no: [CK-ANA-D2, CK-ANA-D3, CK-ANA-E5, CK-ANA-F1, CK-ANA-F4, CK-ANA-J2]
effort_turns: 40
effort_minutes: 60
record_status: Open
date: 2026-09-27
date_closed: null
---

# Peer review record: frequency budget and clock plan (INSP-056, iteration 1)

**Products:** `docs/design/analysis/frequency-budget.md` (`1a7be266`) and `docs/design/analysis/clock-plan.md` (`6e733d06`) with checkers `hardware/sim/freq/freq_budget.py` (`3cd21cb1`) and `hardware/sim/freq/clock_plan.py` (`b21bc3b8`) and figures `docs/reviews/PDR/figures/frequency-budget.png` (`7ecf505f`) and `clock-plan-harmonics.png` (`c22bb722`), at freeze commit `9ac2c42` (rule C2). The blobs equal `HEAD` on 2026-09-27 (checked at `c90df2d` and again at `9bda072` before commit). No product blob lives on a `cr/` branch. ADR-031 is not in this record (its record is to be assigned by the lead SE); findings 3 and 4 bear on its rules 2, 4 and 6.

**Checklist:** the item set of `peer-review-checklist-analysis.md` revision A (CR-012 branch, blob `0386cc6e`; front matter X-1). `analysis_kind` budget, timing, worst-case and other (frequency plan): sections A to F, G2, G6, G7, H, I, and J (criticality safety-critical).

**Acceptance criteria (rule C7, every case the governing clauses enumerate):**
- REQ-SYS-008, 009, REQ-TX-002: both band edges (144.0012 and 147.9988 MHz), with the REQ-SYS-010 ceiling, the REQ-TX-006 offset and the REQ-SYS-015 bandwidth.
- REQ-SYS-010: -10 to +45 C, one year after calibration, every reference class the note offers.
- REQ-SYS-154: both detection triggers ("unlocked", "off its set frequency by over 10 kHz"), each at both moments ("on key-down", "during transmission").
- REQ-SYS-182: both branches ("withhold RF" before key-down, "or end it within 100 ms"), window 10 kHz, the release-build test frequencies at the guard edges.
- REQ-TX-013: 3.3 V sample, below 20 MHz, fixed ratio, within 1 kHz, at both carrier limits.
- REQ-SYS-034: both ends of 144.010 to 147.999 MHz; the WP-PDR-20 output "harmonic table of every clock against 144 to 148 MHz and the IF, USB PLL off when not enumerated"; every IF plan TS-001 leaves open (9.000, 9.0106, 10.7 MHz, each side).
- HZ-008 causes C5, C7, C8 and controls K4, K6, K7 where the notes bound them.

**Search rule.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` (record rules, lock detect, Pico 2 regulators, RSK-040) and on `/Users/robinonsay/rust/rustos` (FC0 Table 541, I2C SCL timing section 12.2.14, core voltage regulator section 6.3) preceded every `grep`. RP2350 text was read only with `git show 2ec64c0f:docs/extracted/rp2350-datasheet.md`; the rustos working tree was not read.

## Findings (iteration 1)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | reviewer | Major | CK-ANA-E3, E5, F1 | `frequency-budget.md` section 3.3 table (column "Largest undetected single-fault error"), Finding 3.3, section 4 row REQ-SYS-154 | REQ-SYS-154 requires Fault-safe when the synthesizer is "off its set frequency by over 10 kHz", a true-error condition. The note uses 10 kHz as the measured window, so with route R3 a true error of 10.0 to 14.5 kHz (interval 12) or 10.0 to 12.5 kHz (interval 13) passes undetected: the note's own C-16 bound (14 518 Hz) shows the requirement as written is not met. It also means the TC-SYS-101 fault injection "a synthesizer 12 kHz off its set frequency" may not trip at interval 12. The section 4 proposal "10 kHz, unchanged ... No [CR] with R3" does not follow. Fix: either (a) propose a measured detection threshold T with healthy disagreement < T <= 10 kHz minus disagreement (R3: 4 518 < T <= 5 482 Hz at interval 12; 2 518 < T <= 7 482 Hz at interval 13), stating that the REQ-SYS-182 agreement window and the REQ-SYS-154 true-error limit are then distinct values, or (b) propose the REQ-SYS-154 value that the 10 kHz window does guarantee (at least 14.6 kHz at interval 12), which is the "else a CR" branch; in both cases name the consequence for TC-SYS-101 | Open | Pending | |
| <a id="finding-2"></a>finding-2 | reviewer | Major | CK-ANA-F1 | `frequency-budget.md` sections 1 (question 3), 3.3 and 4 row REQ-SYS-154 | The "unlocked" trigger of REQ-SYS-154, at key-down and during transmission, has no case. Its `tbr.plan` names "(synthesizer and lock detect)", HZ-008 C8 names "the PLL unlocked", and 07 section 14.2 (SW-SYNTH rows, items g and l) requires lock detect after every write and Fault-safe on unlock. The note proposes to close the REQ-SYS-154 TBR without saying how unlock is detected (device lock-detect status or pin, FC0 DIED or out-of-window count), with what latency during transmission against REQ-SYS-004 (20 ms), or whether an unlocked VCO inside the window is caught. Fix: add the two unlocked cases to the per-case index with the detection means for the recommended TS-007 line-up and the time budget, or state unlock detection as a WP-PDR-32 or 35 allocation with its limit | Open | Pending | |
| <a id="finding-3"></a>finding-3 | reviewer | Major | CK-ANA-F1, A6 | `clock-plan.md` section 2 inventory, section 3 rules 2 and 6, section 5 row REQ-SYS-034; ADR-031 section 2 items 2 and 6 | The inventory, which WP-PDR-20 defines as "every clock", omits switching and clock sources that run in operation: the RP2350 on-chip core voltage regulator, which runs in switching mode whenever the cores run (RP2350 datasheet section 6.3.1.1, Normal mode "operates in a switching mode"; pin VREG_LX to an inductor, Table 1431); the Pico 2 module's RT6150 buck-boost (PFM by default, GPIO23 selects PWM; `docs/research/power-tree-and-charging.md` F18), which RSK-040, the risk this note serves at step S1, names in its condition; the headphone amplifier charge pump (RSK-040 condition, display report F15); and the QSPI flash clock. Rule 6 ("a free-running switching regulator may not run while the receiver is on") and rule 2 cannot hold for the first two, which cannot be turned off, so the "0 rule failures" result is not established. Fix: add each source with its frequency or range (or "not in the corpus" with a value-of-information item), classify it, and either show it meets the rules (for example GPIO23 forcing PWM at a known frequency) or restate rules 2 and 6 and the REQ-SYS-034 proposal with these sources as named residual lines | Open | Pending | |
| <a id="finding-4"></a>finding-4 | reviewer | Major | CK-ANA-A4, B1 | `clock-plan.md` section 2 row "I2C SCL 400 kHz (150 MHz / 375)", rule 4 last sentence; `clock_plan.py` I2C `Clock(...)` entry marked coherent; ADR-031 section 2 item 4 | The I2C input is wrong. The RP2350 I2C master does not produce SCL = clk_sys / (HCNT + LCNT): "SCL_High_time = [(HCNT + IC_*_SPKLEN + 7) * ic_clk] + SCL_Fall_time" and "SCL_low_time = [(LCNT + 1) * ic_clk] - SCL_Fall_time + SCL_Rise_time" (RP2350 datasheet section 12.2.14, Figure 89), and the rise time depends on the pull-ups and bus capacitance ("beyond the control of the DW_apb_i2c"). The SCL rate is therefore neither 400 kHz nor coherent with 144.000 MHz, and its lines, about 0.38 to 0.40 MHz apart, can fall in 144.010 to 144.100 MHz. I2C runs in receive (A1 tuning; the TPA6130A2 volume and the BQ25887 ADC reads of the power tree, power research "Baseline topology"). The rule 2 and rule 3 results for I2C do not follow. Fix: model SCL with the section 12.2.14 equations and a rise-time range, classify I2C as a non-coherent dense clock, and either keep I2C traffic out of receive, or show its lines miss the CW segment over the rise-time range, or name it as a residual line; correct the rule 4 divisor statement | Open | Pending | |
| <a id="finding-5"></a>finding-5 | reviewer | Minor | CK-ANA-D3 | `frequency-budget.md` section 2 row "FC0 test interval" ("this note uses 1 us, which is longer and so conservative for time"); `freq_budget.py` `FC0` dict and the unused `FC0_SCALE` | The checker uses the Table 541 rounded times (4, 8, 16, 32 ms), not 1 us x 2^n: interval 12 is 4.014 ms (0.98 us, Table 582) or 4.096 ms (1 us), interval 13 is 8.03 or 8.19 ms. The rounding is toward the limit, not conservative as stated. Reviewer re-computation with 1 us: C-14.A2 7.60 ms (margin 4.40 ms, not 4.50); C-15 46.4 ms (margin 53.6 ms). No pass or fail changes. Fix: use 1 us x 2^n (or 0.98 us with a stated tolerance) in the checker and the tables | Open | Pending | |
| <a id="finding-6"></a>finding-6 | reviewer | Minor | CK-ANA-F4, A5 | `frequency-budget.md` section 3.2 two-unit table (0.1 ppm class after one year: 243.6 Hz against 250 Hz); TS-007 R-C | The 6.4 Hz margin rests on the temperature term being +/-class relative to the frequency at the calibration temperature. If the class is specified about the span midpoint (the corpus has no datasheet to decide it), a room-temperature calibration leaves up to twice the class: the 0.1 ppm class then gives 272.8 Hz, outside 250 Hz. The conclusion "only 0.1 ppm keeps two units inside" therefore needs its sensitivity stated (margin within twice its uncertainty). RSK-002 step S1 also asks for "the worst-case two-unit offset" before calibration, which the note does not state (reviewer: 2 x (1.5 ppm x 146 MHz + 5 Hz) = 448 Hz). Fix: add both, and make the R-C preference conditional on the datasheet's temperature reference | Open | Pending | |
| <a id="finding-7"></a>finding-7 | reviewer | Minor | CK-ANA-J2, H1 | `frequency-budget.md` section 3.3 route R3; Finding 3.3 bullet 2 ("lowers the largest undetected single-fault error from 21.6 kHz to 14.5 kHz") | The 14.5 kHz bound covers synthesizer faults only. Under R3 a TCXO fault shifts carrier and TCXO count together and reads as agreement until the ratio plausibility test trips. That test accepts a ratio within +/-67.5 ppm of nominal, so with a healthy XOSC at +65 ppm a TCXO error up to 132.5 ppm (19.6 kHz at 147.9988 MHz) passes. This is the fault class the K7 phrase "rather than the synthesizer reference" guards against, and the owner needs it to choose between R3 and R1 (R1: 21.6 kHz). Gross errors (150 to 174 MHz, HZ-008 C7) are caught by both. Fix: add the TCXO-fault row to the route table and restate the comparison in Finding 3.3 and in the K7 request to WP-PDR-16b | Open | Pending | |

Four Major findings are open, so the reviewer verdict is NEEDS CHANGES. Under rule C10 none of the section 4 or section 5 values of either note goes to the owner until this record is APPROVED. The reviewer's checks support the REQ-SYS-008, 009, 010, REQ-TX-002 and REQ-TX-013 proposals, which the findings do not affect (see VALUES PROPOSED below).

## Per-case results

| Case | Condition | Governing id and limit | Result (checker output) | Margin with sign | Uncertainty | Reviewer re-check | Finding ids |
|---|---|---|---|---|---|---|---|
| C-1 | Lower edge, 144.0012 MHz, -2.5 ppm, -5 Hz, -750 Hz | REQ-SYS-008 and REQ-TX-006: -60 dB point inside 144.000 MHz | 144.0000849 MHz | +84.9 Hz | REQ-TX-006 offset (WP-PDR-22) | hand: 1200 - 360.003 - 5 - 750 = 84.997 Hz | none |
| C-2 | Upper edge, 147.9988 MHz, +2.5 ppm, +5 Hz, +750 Hz | REQ-SYS-008 and REQ-TX-006: inside 148.000 MHz | 147.9999250 MHz | +75.0 Hz | as C-1; stated in section 6 item 3 | hand: 1200 - 369.997 - 5 - 750 = 75.003 Hz | none |
| C-3, C-4 | Both edges, 26 dB half-bandwidth 175 Hz | REQ-SYS-015 (350 Hz) inside the band | 659.9 and 650.0 Hz | +659.9 and +650.0 Hz | small | re-run: same | none |
| C-5 | Largest -60 dB offset the guard supports | REQ-SYS-008 guard | 825.0 Hz | +75.0 Hz over 750 Hz | as C-1 | hand: 1200 - 369.997 - 5 = 825.003 Hz | none |
| C-6 | Largest reference error at 750 Hz | REQ-SYS-010 2.5 ppm | 3.006 ppm | +0.506 ppm | none | hand: 445 / 147.9988 = 3.0068 ppm | none |
| C-7.1 to C-7.3 | Research offsets 614, 735, 750 Hz | REQ-TX-006 | 211.0, 90.0, 75.0 Hz | positive | as C-1 | re-run: same | none |
| C-8 | Wrong calibration inside +/-0.9 ppm, uncalibrated 1.5 ppm | REQ-SYS-010 and HZ-008 K4: 2.5 ppm | 2.434 ppm | +0.066 ppm (9.7 Hz) | allocations (section 6 item 2) | hand: 1.5 + 0.9 + 5 / 147.9988 = 2.4338 ppm | none |
| C-9 | Calibration range against uncalibrated total | range <= total | 0.9 <= 1.5 ppm | holds | none | inspection | none |
| C-10.1 to C-10.3 | Calibrated, classes 0.1, 0.25, 0.5 ppm, -10 to +45 C, one year | REQ-SYS-010: 2.5 ppm | 0.834, 0.984, 1.234 ppm | +1.666, +1.516, +1.266 ppm | allocations | hand: 0.1 + class + 0.5 + 0.1 + 0.034 | none |
| Two-unit | Two calibrated units, 146 MHz, after one year | RSK-002: 250 Hz | 243.6, 287.4, 360.4 Hz | +6.4, -37.4, -110.4 Hz | temperature reference of the class | hand: 2 x (0.8 ppm x 146 MHz) + 10 = 243.6 Hz | finding-6 |
| C-11 | Prescaled sample at both carrier limits | REQ-TX-013: below 20 MHz; GPIN 50 MHz | 18.000150 to 18.499850 MHz | +1.50 MHz | exact division | hand: 147.9988 / 8 = 18.49985 | none |
| C-12.iv12 | R3, healthy, before PA_EN, 147.9988 MHz | REQ-SYS-182: 10 kHz window | 4 518.0 Hz | +5 482.0 Hz | FC0 accuracy semantics (section 6 item 4) | hand: 4 000 + 370.0 + 148.0 | none |
| C-12.iv13 | R3, healthy, during transmit | REQ-SYS-182: 10 kHz | 2 518.0 Hz | +7 482.0 Hz | as above | hand: 2 000 + 370.0 + 148.0 | none |
| C-13.iv12, iv13 | R1 raw XOSC, healthy | REQ-SYS-182: 10 kHz | 13 990.0 and 11 990.0 Hz | -3 990.0 and -1 990.0 Hz (reported as not holding) | XOSC bound conservative (section 6 item 5) | hand: 4 000 (2 000) + 370 + 9 620 | none |
| C-14.A1, A2 | Changeover check, interval 12 | REQ-SYS-161: 12 ms lead-in | 6.00 and 7.50 ms | +6.00 and +4.50 ms | FC0 interval time | 1 us basis: 6.10 and 7.60 ms, +5.90 and +4.40 ms | finding-5 |
| C-15 | Fault during transmit: 2 intervals + 10 ms + 20 ms | REQ-SYS-182: 100 ms | 46.0 ms | +54.0 ms | allocations (WP-PDR-32) | 1 us basis: 46.4 ms, +53.6 ms | finding-5 |
| C-16 | Undetected synthesizer error, R3 interval 12 | REQ-SYS-154: Fault-safe when over 10 kHz off | 14 518.0 Hz | -4 518 Hz against the requirement's 10 kHz | as C-12 | hand: 10 000 + 4 518 | finding-1 |
| C-16b | Undetected TCXO fault, R3 (not in the note) | HZ-008 K7 | not computed | reviewer: 132.5 ppm = 19.6 kHz | XOSC bound | hand: (67.5 + 65) ppm x 147.9988 MHz | finding-7 |
| REQ-SYS-154 unlock | Unlocked at key-down and during transmission | REQ-SYS-154 | no case | none | none | not re-checked (absent) | finding-2 |
| CP-1 | Clear-class lines in 144.010 to 147.999 MHz, every proposed and fixed clock | REQ-SYS-034 range; ADR-031 rule 1 | only the coherent 144.000 MHz line (143.9906 to 144.0094 MHz) | +0.64 kHz below 144.010 MHz | XOSC 65 ppm | hand: 144 MHz x 65 ppm = 9.36 kHz; SPI clear set d <= 24 checked by (d - 1)/d < 0.96 | finding-3 (inventory) |
| CP-2 | Any line in 144.010 to 144.100 MHz from a clock running in operation | ADR-031 rule 2; 47 CFR 97.305(a), (c) | 0 failures for the listed clocks | not established | I2C model; missing sources | re-run: 0 failures for the listed clocks | finding-3, finding-4 |
| CP-3 | Dense-class coherence (PWM 150 kHz, buck 2.4 MHz, I2C) | ADR-031 rule 3 | coherent | not established for I2C | I2C SCL model | hand: 144 / 0.15 = 960, 144 / 2.4 = 60 | finding-4 |
| CP-4.1 to CP-4.6 | IF plans 9.000, 9.0106, 10.7 MHz, low and high side: BFO 16th harmonic, LO band, image band, IF window | REQ-SYS-034; TS-001 inputs | table of section 4 | BFO line in band for 9.0106 MHz (144.153 to 144.186 MHz) and at 144.000 to 144.016 MHz for 9.000 MHz with the BFO above the IF, both stated | BFO duty-cycle error unbounded (stated) | hand: 16 x 9.0096 = 144.1536, 16 x 9.0116 = 144.1856; 13 x 10.7 = 139.1, 14 x 10.7 = 149.8 | none |
| CP-5 | clk_usb and clk_adc 48 MHz | HZ-008 K6 "USB PLL off when not enumerated" | 3rd harmonic on the 144.000 MHz line; PLL_USB cannot stop while the ADC runs | stated as a K6 text request | none | clk_adc "Must be 48MHz" as cited | none |

## Readiness criteria

| # | Answer | Evidence |
|---|---|---|
| R1 | Yes | `git rev-parse 9ac2c42:<path>` equals every `product_files` blob; equal at `HEAD` `c90df2d` and `9bda072` |
| R2 | Yes | `.venv/bin/python hardware/sim/freq/freq_budget.py --plot`: exit 0, "RESULT: 27 pass, 0 fail" with 4 INFO lines, as `frequency-budget.md` section 7 states; `clock_plan.py --plot`: exit 0, "RESULT: 0 rule failure(s) in the proposed plan", as `clock-plan.md` section 7 states. No LTspice deck is involved |
| R3 | N/A | No JSON product file |
| R4 | Yes | The author summary and each note state the questions, the evidence status (developer evidence), inputs, results, margins, limitations and the proposed values |
| R5 | Yes | No `TBD` in either note; every TBR relied on is named with its id (REQ-SYS-004, 008, 009, 010, 015, 034, 154, 161, 182; REQ-TX-002, 006, 013) |
| R6 | Yes | Both figures exist at the cited paths and were opened |

## A. Question, scope and traceable inputs

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-A1 | Yes | `frequency-budget.md` section 1 lists four questions and every id served; `clock-plan.md` section 1 lists REQ-SYS-034, HZ-008 K6, RSK-040 S1 and ADR-023 item (5). All ids exist (requirement files read; `hazards.json` HZ-008 K4, K6, K7 and causes C5, C7, C8 read) |
| CK-ANA-A2 | Yes | No schematic exists; the design data are TS-007 (same freeze), concept section 7.4 and named research findings. "AT RISK: No" in both headers is correct (no dependence on CR-003 or CR-006) |
| CK-ANA-A3 | Yes | Input tables cite regulation (corpus lines verified: `47cfr-97.301.md` line 26 "2 m ... 144-148"; `47cfr-97.305.md` lines 17 and 58), requirement ids with TBR state, RP2350 datasheet sections with table numbers, research findings with confidence, and label allocations as "Allocation" or "Proposal" |
| CK-ANA-A4 | No | Every result-setting input was checked against its source: band edges, CW segment, requirement values (read from the requirement files), FC0 Table 541 (4 ms 500 Hz to 32 ms 62.5 Hz, extract lines 37955 to 37965), Table 582 ("0.98us * 2**interval, but let's call it 1us"), GPIN 50 MHz (extract line 37593), Table 596 (+/-30, +/-30, +/-5 ppm, lines 40641 to 40653), F21 classes, RSK-002 250 Hz. Disagreements: the I2C SCL rate (finding-4) and the FC0 time basis (finding-5) |
| CK-ANA-A5 | Yes, with finding-6 | Assumptions listed with direction (sections 2 and 6); the calibration-temperature assumption is not bounded (finding-6) |
| CK-ANA-A6 | Yes, with finding-3 | Consequences go as requests to the plan section 5.3 writers (WP-PDR-16b, 18, 19, 22, 24, 25, 29, 32, 35, 36a); no file outside the notes was edited. The omitted sources of finding-3 have no request |

## B. Model validity

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-B1 | No | The budget is a linear worst-case sum, and the line model n x f x (1 +/- tol) is right for synchronous clocks. The I2C model is not (finding-4) |
| CK-ANA-B2 | N/A | No vendor model file |
| CK-ANA-B3 | Yes | Known answers KA-1 (SRR decision 25 arithmetic, 80 Hz), KA-2 (369.997 Hz) and KA-3 (2 000 Hz) in the checker; clock lines are hand-checkable |
| CK-ANA-B4 | N/A | Exact rational arithmetic, no numerical settings |
| CK-ANA-B5 | Yes | The reviewer reproduced C-1, C-2, C-5, C-6, C-8, C-10, C-12, C-13, C-15, the two-unit table, the XOSC exclusion and the BFO lines by hand (per-case table); all agree |
| CK-ANA-B6 | Yes | `frequency-budget.md` section 6 lists tool status, allocations, the REQ-TX-006 dominance, FC0 accuracy semantics, the XOSC bound and FastLock conditions; `clock-plan.md` section 6 lists line level, research values and VCO placement |

## C. Tools, validation status and reproducibility

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-C1 | Yes | venv Python 3.13.5 (`.venv/bin/python --version`), the version of the `tools/toolchain.lock.md` venv row |
| CK-ANA-C2 | Yes | No TV record covers `hardware/sim/freq/*.py` (TV-024 covers static analysis only and is Draft); both notes mark the results developer evidence and hold the values from the owner until a TV record or an owner ruling (frequency budget section 6 item 1 and the section 4 heading) |
| CK-ANA-C3 | Yes | One command per note from the repository root; no GUI |
| CK-ANA-C4 | Yes | Both checkers re-run on a `git archive 9ac2c42` export in the scratchpad: same exit status and values; the regenerated PNGs hash to `7ecf505f` and `c22bb722`, byte-identical to the frozen figures |
| CK-ANA-C5 | N/A | No TV record, so no stated limitation applies |

## D. Units, arithmetic and consistency

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-D1 | Yes | ppm to Hz at the stated frequency (147.9988 MHz at the upper edge, 146 MHz for RSK-002); kHz and ms throughout |
| CK-ANA-D2 | Yes | Note tables equal the checker lines (C-1 to C-17 and the tables); TS-007 section 4 quotes C-14 as in the note |
| CK-ANA-D3 | No | Margins floored and sums ceiled as stated, except the FC0 times (finding-5) |
| CK-ANA-D4 | Yes | Each constant carries its source id in a comment next to it (`W_WINDOW`, `T_LIMIT`, `T_RF_OFF`, `T_LEADIN`, `SAMPLE_CEIL`, `GPIN_MAX`, `TX_MIN`, `TX_MAX`, `REF_CEIL_PPM`, `SYS034`, `CW_SEG`) |

## E. Results, margins, proposed values and credit

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-E1 | Yes | Limits quoted with ids from the requirement files; regulation cited with corpus file and line |
| CK-ANA-E2 | Yes | Margin conventions stated ("distance inside the band"; limit minus result); TPM-006 `threshold_yellow` "2.5 to 4 ppm": every cbe is below 2.5 ppm |
| CK-ANA-E3 | No | The 75.0 Hz guard margin is smaller than its uncertainty and the note says so with the consequence (WP-PDR-22 reports against 825 Hz): acceptable. The REQ-SYS-154 case is reported as holding although the note's own bound shows it does not (finding-1) |
| CK-ANA-E4 | Yes | `freq_budget.py` asserts C-1 to C-12, C-14 and C-15 and exits 1 on any FAIL; `clock_plan.py` asserts rules 1 to 3 and exits 1 on any failure. The R1 cases are INFO by design (route not recommended) |
| CK-ANA-E5 | No | The section 4 and 5 tables give id, value, margin, `tbr.plan` step and the "else a CR" branch, and neither note edits a requirement file. The REQ-SYS-154 proposal is not supported (findings 1 and 2), nor the REQ-SYS-034 proposal (findings 3 and 4) |
| CK-ANA-E6 | Yes | TPM-006 cbe by class with `credit: false`, sent to WP-PDR-29; `tpm.json` not edited |
| CK-ANA-E7 | Yes | No closing credit claimed; REQ-SYS-010 (Analysis) is supporting at PDR and closes on the CDR part datasheet |

## F. Every case named

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-F1 | No | Cases as listed in the acceptance criteria. Missing: the REQ-SYS-154 true-error trigger at both moments (finding-1), the REQ-SYS-154 unlocked trigger at both moments (finding-2), and the omitted sources of "every clock" (finding-3) |
| CK-ANA-F2 | Yes | HZ-008 C7 (wrong word, calibration out of range: K4 bound, C-8) and C8 (gross error: R1 and R3) analysed; the C8 "unlocked" part is finding-2 |
| CK-ANA-F3 | Yes | Every term added toward the edge at the governing (upper) edge; R1 and R3 at the highest carrier |
| CK-ANA-F4 | No | C-2 sensitivity to REQ-TX-006 is given (C-5 and the figure); the two-unit 0.1 ppm case (6.4 Hz margin) has none (finding-6) |

## G. Kind-specific items

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-G2-1 | Yes | Every budget line has a source and a state column (Regulation, TBR, Allocation, Research, Datasheet, Proposal) |
| CK-ANA-G2-2 | Yes | Totals recomputed (per-case table); differences none |
| CK-ANA-G2-3 | N/A | `docs/design/budgets.md` has no frequency section yet; it is requested from WP-PDR-29 |
| CK-ANA-G2-4 | Yes | Receive (TCXO refresh, R3), changeover and transmit columns; standby and charging change no frequency term |
| CK-ANA-G6-1 | Yes | FC0 timebase clk_ref from the XOSC, tolerance 65 ppm, stated |
| CK-ANA-G6-2 | Yes | C-14 and C-15 sum retune, count, software latency, service period and RF-off time; the software terms are allocations to WP-PDR-32 |
| CK-ANA-G6-3 | Yes | No emulation-derived time |
| CK-ANA-G6-4 | Yes | C-15 46.0 ms against the REQ-SYS-182 100 ms, HZ-008 K7 named |
| CK-ANA-G7-1 | Yes | Extreme-value sum, stated |
| CK-ANA-G7-2 | Yes | TCXO initial, reflow, temperature, aging, supply and load allocated; XOSC tolerance, stability and first-year aging from Table 596 |

## H. Hazards, risks and records

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-H1 | Yes, with finding-7 | K4 and K7 text changes (frequency budget) and the K6 text change (clock plan) sent to WP-PDR-16b, not edited here. The R3 comparison sent with them is incomplete (finding-7) |
| CK-ANA-H2 | Yes | RSK-002 and RSK-046 (frequency budget section 5) and RSK-040 (clock plan section 5) sent to WP-PDR-18 |
| CK-ANA-H3 | Yes | Change history revision 0, 2026-09-27, freeze F0, in both notes |

## I. Visual closure

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-I1 | Yes | `docs/reviews/PDR/figures/frequency-budget.png` and `clock-plan-harmonics.png` opened with the Read tool (2 renders); both regenerate byte-identical |
| CK-ANA-I2 | Yes | Frequency budget: labelled axes with units, the 750 Hz TBR line and the 825.0 Hz limit labelled, F7 cases marked, legend; right panel with the REQ-SYS-182 10 kHz window labelled and both bar series in the legend; values agree with the checker (75.0 Hz; 4.5, 2.5 and 14.5 kHz bars). Clock plan: every clock row with the status colour key in the title, harmonic orders printed, the 2 m band, CW segment, image and LO bands shaded and in the legend. The XOSC n = 14 label at 168 MHz sits under the legend (cosmetic, no finding) |

## J. Software assurance items (criticality safety-critical)

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-J1 | Yes | swe-070 7.1 task 1: the checkers are not accredited, and the notes restrict their use accordingly (CK-ANA-C2) |
| CK-ANA-J2 | No | swe-134 7.1 tasks 1 and 6: the values set for item h (PA_EN prerequisite, 10 kHz agreement) and item l (Fault-safe on unlock or off-frequency) are not consistent with REQ-SYS-154 as written (findings 1 and 2); the R3 departure from the K7 independence phrase is routed to the hazards writer without its TCXO-fault bound (finding-7) |
| CK-ANA-J3 | Yes | `assurance_tasks_applied` lists the three tasks; results above |

## Items N/A

R3; CK-ANA-B2, B4, C5, G2-3; G1 (no simulation deck), G3 (thermal), G4 (RF exposure), G5 (cascade; the TS-007 phase-noise arithmetic is reviewed in INSP-055).

## Verdict

```
VERDICT: NEEDS CHANGES
PRODUCT: docs/design/analysis/frequency-budget.md@1a7be266, docs/design/analysis/clock-plan.md@6e733d06, hardware/sim/freq/freq_budget.py@3cd21cb1, hardware/sim/freq/clock_plan.py@b21bc3b8, docs/reviews/PDR/figures/frequency-budget.png@7ecf505f, docs/reviews/PDR/figures/clock-plan-harmonics.png@c22bb722 at 9ac2c42
FINDINGS:
- [Major] finding-1 CK-ANA-E3/E5/F1: REQ-SYS-154 true-error trigger not met with a 10 kHz measured window (undetected to 14.5 kHz).
- [Major] finding-2 CK-ANA-F1: REQ-SYS-154 unlocked trigger has no case.
- [Major] finding-3 CK-ANA-F1/A6: clock inventory omits the RP2350 switching core regulator, the Pico 2 RT6150, the headphone charge pump and the QSPI clock.
- [Major] finding-4 CK-ANA-A4/B1: I2C SCL is not clk_sys/(HCNT+LCNT) and is not coherent (RP2350 section 12.2.14).
- [Minor] finding-5 CK-ANA-D3: FC0 interval times rounded toward the limit.
- [Minor] finding-6 CK-ANA-F4/A5: two-unit 0.1 ppm margin sensitivity; uncalibrated two-unit offset missing.
- [Minor] finding-7 CK-ANA-J2/H1: R3 undetected TCXO-fault bound (19.6 kHz) missing.
VALUES PROPOSED: REQ-SYS-008, 009, REQ-TX-002: 144.0012 to 147.9988 MHz (supported, subject to WP-PDR-22 <= 825.0 Hz); REQ-SYS-010: +/-2.5 ppm (supported); REQ-TX-013: ratio 8, < 20 MHz, 1 kHz (supported); REQ-SYS-182: 10 kHz, 100 ms with R3 (supported, finding-7 open); REQ-SYS-154: 10 kHz (not supported, findings 1 and 2); REQ-SYS-034: 144.010 to 147.999 MHz, 3 dB (not supported, findings 3 and 4); TPM-006 cbe (supported, credit false)
MEASUREMENTS: size=31 checker cases, 22 clocks, 6 IF plans; inputs_checked=24; renders=2; turns=44; minutes=80; major=4; minor=3
```

## Commands

- `git rev-parse 9ac2c42:<path>` and `HEAD:<path>` for the six product files: equal to `product_files`.
- `git archive 9ac2c42 hardware/sim/freq docs/reviews/PDR/figures` into the scratchpad; `.venv/bin/python hardware/sim/freq/freq_budget.py --plot` exit 0; `.venv/bin/python hardware/sim/freq/clock_plan.py --plot` exit 0; `git hash-object` of both PNGs equals the frozen blobs.
- `git show 2ec64c0f:docs/extracted/rp2350-datasheet.md` (rustos, committed object) for Tables 541, 582, 596, sections 6.3 and 12.2.14.
- `.venv/bin/python tools/validate_docs.py`: exit 0 with this record (see the return).

## Measurements (SWE-089)

Items checked 59 applicable (readiness 6, A 6, B 6, C 5, D 4, E 7, F 4, G 10, H 3, I 2, J 3, less the N/A items); items answered No 8; findings 4 Major, 3 Minor; fixed 0; deferred 0; iteration 1; renders inspected 2; effort 44 turns, about 80 minutes (shared session with INSP-055).

## Iteration 2: delta verification of finding-1 to finding-4 (Major) (2026-09-27)

**Scope (rule C1).** A delta that verifies the four Major fixes only. The products were re-frozen at `802347b` (freeze F0, rule C2): `frequency-budget.md` `79d47fbb`, `clock-plan.md` `8582121a`, `freq_budget.py` `d82269e6`, `clock_plan.py` `b9392297`, `frequency-budget.png` `d77a0b3a`, `clock-plan-harmonics.png` `19f47e3d`, and now ADR-031 `a578ca16`. Each blob is equal at `802347b`, at `HEAD` (`8abb467`) and in the working tree (`git rev-parse` and `git hash-object`). No product blob lives on a `cr/` branch, so the record verdict is set in this commit. The change was read as `git diff 9ac2c42 802347b` on the two notes and ADR-031, together with the checker functions each fix touches. The iteration 1 blobs are in the front matter of `8fea433`. The iteration 1 checklist answers stand except where this section changes them. Minor findings 5 to 7 were not addressed (rule C1) and were not re-checked.

**Independence (rule C4).** This invocation authored no part of WP-PDR-20 (TS-007, both notes, ADR-031, the checkers, the figures) and did not write iteration 1 of this record or INSP-055 or INSP-074. It edited no product file.

**Search first (charter section 11 rule 1).** One `git log`, `git status` and `grep -n "WP-PDR-20"` over the plan file (a known path) ran in the same step that loaded the search tool. That order is recorded here as a deviation. `mcp__claude-context__search_code` then ran before every other manual search. Queries on `/Users/robinonsay/rust/cwht`: the INSP-056 record and the WP-PDR-20 products; the REQ-SYS-154 and 182 wording; ROSC use in the cwht clock configuration; display-module oscillators. On `/Users/robinonsay/rust/rustos`: RP2350 ROSC and LPOSC. `grep` afterwards only pinned lines. RP2350 and Pico 2 text was read only from committed objects, `git show 2ec64c0f:docs/extracted/rp2350-datasheet.md` and `pico-2-datasheet.md`, exported to the scratchpad. The rustos working tree was not read.

**Acceptance criteria for the delta (rule C7).**
- REQ-SYS-154, "on key-down or during transmission when its synthesizer is unlocked or off its set frequency by over 10 kHz". That gives four cases: off-frequency at key-down, off-frequency during transmission, unlocked at key-down, and unlocked during transmission.
- REQ-SYS-182, "withhold RF, or end it within 100 ms, unless ... agrees ... within 10 kHz". Both branches, with the no-false-trip condition at the release-build frequencies 144.0012 and 147.9988 MHz.
- TC-SYS-101 and the REQ-SYS-182 verification note: the 12 kHz injection, at key-down and during an over.
- The WP-PDR-20 output "harmonic table of every clock against 144 to 148 MHz and the IF". Every source that runs in operation, against both ends of 144.010 to 147.999 MHz and against the CW-only segment 144.010 to 144.100 MHz.
- I2C SCL over the whole rise-time range; the QSPI SCK over every CLKDIV the plan allows.
- ADR-031 items 2, 3, 4, 6, 7 and 8 against `clock-plan.md` revision 1.

### Verification of the Major findings

**finding-1 (REQ-SYS-154 true error against the measured window): Verified.**

| Element of the fix | Result | Evidence |
|---|---|---|
| Measured threshold T distinct from the 10 kHz true-error limit, with both conditions | Yes | Section 3.3 "Measured threshold and true-error limit": no false trip d < T; no missed trip T + d <= 10 kHz. `undetected_bound("R3")` = T + d (checker lines 183 to 191), the correct bound for measured = true + e with abs(e) <= d |
| T = 5.0 kHz inside the R3 interval at both intervals | Yes | Checker "TABLE R3 threshold interval": 4518.0 < T <= 5482.0 (iv12), 2518.0 < T <= 7482.0 (iv13). Reviewer hand check: d12 = 8 x 500 + 370 + 148 = 4 518 Hz, 5 000 - 4 518 = 482 Hz, 10 000 - 9 518 = 482 Hz; d13 = 8 x 250 + 518 = 2 518 Hz, both margins 2 482 Hz |
| REQ-SYS-182 unchanged and consistent | Yes | C-12w: T <= 10 kHz, so RF is withheld on every disagreement over 10 kHz. REQ-SYS-182 is a "withhold unless agrees within 10 kHz" statement, so a tighter SW-SAFE threshold satisfies it. The release-build edges keep d < T (C-12, at TX_MAX) |
| TC-SYS-101 consequence named | Yes | C-18: 12 000 - 4 518 = 7 482 Hz > T (margin 2 482 Hz); 12 000 - 2 518 = 9 482 Hz (margin 4 482 Hz). The case needs no change |
| Sensitivity of the 482 Hz margin | Yes | C-16a: 8a + 518 < 5 000 and 5 518 + 8a <= 10 000 give a <= 560.25 Hz at both intervals (reviewer). It is stated as the WP-SW-14 dev-board acceptance limit, with interval 13 as the fallback (C-14.A2 11.5 ms, stated) |
| R1 alternative restated | Yes | `min_154_limit("R1", 13)` = 11 990 + 2 000 + 9 620 = 23 610 Hz (reviewer), "at least 23.7 kHz" in section 3.3 and section 4, both by CR |
| Values table | Yes | Section 4 row REQ-SYS-154 gives the limit, the threshold and the "else a CR" branch; T goes to WP-PDR-35 as an L2 value, and no requirement file is edited |

**finding-2 (unlocked trigger): Verified.**

| Element of the fix | Result | Evidence |
|---|---|---|
| Case at key-down | Yes | U-1.A1 and U-1.A2: the lock-detect indication is read after the last write and just before the `PA_EN` prerequisite (07 section 14.2 `SW-SYNTH` items g and l), inside the 2 ms software allocation of C-14. The FC0 interval 12 check is the second means. Checker: PASS, 6.00 and 7.50 ms within the 12 ms lead-in |
| Case during transmission | Yes | U-2: 10 ms lock-detect sample (allocation to WP-PDR-32) + 20 ms (REQ-SYS-004) = 30.0 ms. The checker compares it with the 100 ms of REQ-SYS-182 and with C-15 (46.0 ms). REQ-SYS-154 sets no time of its own (statement read), so using the REQ-SYS-182 time is a reasonable proxy and is stated as such |
| Unlocked inside the window | Yes | An unlocked VCO inside T is caught only by lock detect. The note says so and names the "else a CR" branch if the LMX2571 has no lock-detect indication (section 3.3, section 4 last column) |
| Research gap routed | Yes | The lock-detect form goes to TS-007 value-of-information item 4 (INSP-055 finding-4 is Minor on the same gap, confirmed). Pin or SPI status forms are covered by requests to WP-PDR-36a and 35, and A1 by the Si5351A status bit (AN619 is not in the corpus, stated) |
| Requests | Yes | WP-PDR-35: the lock-detect requirements and the HostUnit cases at 4.9 and 5.1 kHz; WP-PDR-32: the timing analysis; WP-PDR-16b: HZ-008 C8 and K7 wording; WP-PDR-36a: the pin |

One wording error in the U-1 row is new finding-9 (Minor). No result changes.

**finding-3 (clock inventory): Verified for the four sources it named.** The new omission found while checking the completeness claim is new finding-8 (Major).

| Element of the fix | Result | Evidence |
|---|---|---|
| RP2350 core regulator (R-1) | Yes | Section 2.1: typical 3 MHz only, with no min or max (datasheet Table 1441 row fsw, extract line 100935 area). Switching whenever the core runs: "In Normal mode, the regulator operates in a switching mode" (extract line 32844). Low power mode is not possible under software control (line 32905). The 48th harmonic reaches 144.010 MHz at +69.4 ppm (reviewer: 10 kHz / 144 MHz = 69.44 ppm) |
| Pico 2 RT6150 (R-2) | Yes | Pico 2 datasheet section 5.4 (extract lines 697 to 702): PS low gives PFM, PS high gives PWM, and PWM under heavy load "irrespective of the PS pin state". The frequency is not in the corpus (VOI-CP-2). The GPIO23-high proposal, with its battery cost, goes to WP-PDR-24 and 29 |
| TPA6130A2 charge pump (R-3) | Yes | 300 to 500 kHz (display research F15). Reviewer count: n from ceil(144.010 / 0.5) = 289 to floor(144.100 / 0.3) = 480, 192 intervals, equal to the checker. Whether R-3 exists depends on D-UI-05 (WP-PDR-25) |
| QSPI SCK | Yes | CLKDIV reset `0x04` and "Odd and even divisors are supported" (extract line 93386); boot `CLKDIV is set to 12` (line 28498). Clear set 1 to 24: a line needs n/d in [0.96007, 0.98666], and (d - 1)/d < 0.96 for d <= 24 (reviewer). The checker table agrees; CLKDIV 25 is the first coherent one, 26 the first in the band |
| Rules 2 and 6 and REQ-SYS-034 restated | Yes | Rule 2 applies to placeable clocks, rule 6 separates switchers that can be synchronised or switched off from R-1 to R-3, and new rule 10 governs level. For the residual lines, the REQ-SYS-034 allowance row says the Analysis gives no support and the Test is the evidence. The TRR "else a CR" branch is named |
| ADR-031 | Yes | Context, assumptions 4 and 5, items 2, 6, 7 and 8, option A, sections 4.1, 4.3 and 4.4, the memo wording and the revisit conditions all follow revision 1 and match `clock-plan.md` section 2.1 |

**finding-4 (I2C SCL model): Verified.**

| Element of the fix | Result | Evidence |
|---|---|---|
| Section 12.2.14 equations | Yes | Quoted in the checker (lines 44 to 47) and in section 2.1 R-4, as in the datasheet (extract lines 75469 to 75470). The fall time cancels in the period: (HCNT + SPKLEN + 7) + (LCNT + 1) ic_clk + tr. ic_clk is clk_sys (line 73861) |
| Rise-time range and SCL | Yes | Reviewer: 160 + 8 + 7 + 199 + 1 = 375 ic_clk = 2.500 us; 1 / 2.520 us = 396.8 kHz, 1 / 2.800 us = 357.1 kHz; 144 MHz / SCL = 362.9 to 403.2, which is not a single integer, so SCL is non-coherent. The 20 to 300 ns range is labelled an allocation, and the 300 ns Fast-mode ceiling "not in the corpus" |
| CW-segment count | Yes | n = ceil(144.010 / 0.3968) = 363 to floor(144.100 / 0.3571) = 403: 41 intervals, as the checker says |
| Classification and control | Yes | Residual R-4, non-coherent, with the receive traffic rule (event-driven, no poll faster than once a second, each transaction at most 1 ms), sent to WP-PDR-32 and 35. The REQ-SYS-034 Test runs with traffic generated. Rule 3 now excludes I2C |
| Rule 4 divisor statement | Yes | "I2C SCL 400 kHz with HCNT + LCNT = 375" has been removed. Rule 4 and ADR-031 item 4 state the counts and the range. The counts meet the constraints of section 12.2.14.1 (LCNT 199 > SPKLEN + 7 = 15) |

### Reviewer re-runs

| Command | Exit | Result |
|---|---|---|
| `git archive 802347b hardware/sim/freq <two PNGs>` into the scratchpad; `.venv/bin/python hardware/sim/freq/freq_budget.py --plot` | 0 | "RESULT: 35 pass, 0 fail", 4 INFO (C-13.iv12, C-13.iv13, C-16a, C-17), as `frequency-budget.md` section 7 says |
| `.venv/bin/python hardware/sim/freq/clock_plan.py --plot` (same export) | 0 | "RESULT: 0 rule failure(s) in the proposed plan; 4 named residual source(s)", as `clock-plan.md` section 7 says |
| `git hash-object` of the regenerated PNGs | 0 | `d77a0b3a` and `19f47e3d`: byte-identical to the frozen figures |

### Visual closure (iteration 2)

Both frozen figures were opened with the Read tool (2 renders).
- `frequency-budget.png`, right panel: the REQ-SYS-154 10 kHz limit (red dashed) and the 5 kHz threshold T (green dash-dot) are both in the legend, not over the bars. The R3 bars show healthy disagreement 4.5, 2.5 and 1.5 kHz, all under T, and undetected error 9.5, 7.5 and 6.5 kHz, all under 10 kHz. The R1 bars show 14.0, 12.0 and 11.0 kHz against 27.6, 23.6 and 21.6 kHz. These agree with the checker.
- `clock-plan-harmonics.png`: the title wraps onto three lines and names the magenta residual class. The four residual rows are drawn: I2C, the charge pump and the regulator as full-span bars, and the RT6150 with the text "frequency not in the corpus". The QSPI 37.5 MHz n = 4 mark is at 150 MHz.
- The legend still covers the XOSC n = 14 label at 168 MHz. This is cosmetic and not a finding, as in iteration 1.

### New findings at iteration 2

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-8"></a>finding-8 | reviewer (iteration 2, while verifying the finding-3 completeness claim) | Major | CK-ANA-F1, CK-ANA-E5 | `clock-plan.md` section 2 inventory, section 2 result line ("The rules hold for every source that can be placed"), section 5 row REQ-SYS-034 range; ADR-031 section 1 ("Every other clock can be placed") and section 2 header | See the note after this table | Open | Pending | |
| <a id="finding-9"></a>finding-9 | reviewer (iteration 2) | Minor | CK-ANA-D2 | `frequency-budget.md` section 3.3, unlocked table row U-1, column "Second means" | See the note after this table | Open | Pending | |

**finding-8 (RP2350 oscillators missing from the inventory).**
- **Defect.** The inventory still omits two RP2350 oscillators that run in operation:
  - **Ring oscillator (ROSC).** "It provides the clock to the cores during boot". It runs at "a nominal 11MHz" and "is guaranteed to be in the range 4.6MHz to 19.6MHz without randomisation and 4.6MHz to 24.0MHz with randomisation" (RP2350 datasheet section 8.3.1, extract lines 41086 to 41093). It stops only if software disables it: "You can disable the ROSC once you've switched the system clocks to the XOSC". After DORMANT it restarts "in the same configuration" (section 8.1.1.2).
  - **Low-power oscillator (LPOSC).** Nominal 32.768 kHz, an RC oscillator that starts with the core supply, with an initial accuracy of +/-20 % and +/-1.5 % after trimming (section 8.4, extract lines 41641 and 41663).
- **Why the ROSC matters.** The cwht clock bring-up, ADR-051 section 2 (WP-SW-11), moves clk_ref and clk_sys off the ROSC but never stops it. So the ROSC is a clear-class clock, running in operation, whose frequency cannot be placed. Harmonic orders 8 to 31 can fall in 144.010 to 144.100 MHz (24 orders; for example n = 13 at 11.0777 to 11.0846 MHz).
- **Why the LPOSC matters.** It is a dense, non-coherent source with lines about 33 kHz apart in every band.
- **Consequence.** The claim of rules 1 and 2 ("0 rule failures", "Every other clock can be placed"), the REQ-SYS-034 range support and the HZ-008 K6 expected-birdie list are not established. The defect class is the same as finding-3.
- **Fix.** Add both sources, with their ranges and datasheet lines.
  - For the ROSC, choose one of two routes. Either (a) add a rule that the clocks driver disables the ROSC once clk_ref and clk_sys run from the XOSC and PLL_SYS, and again after any DORMANT exit, with a request to the WP-SW-11 and ADR-051 writer and to WP-PDR-35 for an SW-CTL requirement and its HostUnit check. Or (b) name it residual R-5.
  - Name the LPOSC as a residual source (R-6), or show that it is stopped in operation.
  - Update the checker, the figure, rule 2, the REQ-SYS-034 row and ADR-031 to match.

**finding-9 (U-1 threshold wording).**
- **Defect.** The U-1 row says "an unlocked output more than 5.482 kHz off trips". With T = 5.0 kHz and d = 4 518 Hz at interval 12, a trip is guaranteed only above T + d = 9.518 kHz. An error from 5.482 to 9.518 kHz may pass. The same section later states the correct 9.518 kHz bound.
- **Effect.** No result changes, since lock detect is the primary means.
- **Fix.** Replace 5.482 with 9.518 kHz, and say that errors above T - d = 0.482 kHz may trip.

### Findings (iteration 2 state)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| finding-1 | reviewer | Major | CK-ANA-E3, E5, F1 | `frequency-budget.md` section 3.3, section 4 row REQ-SYS-154 | Measured threshold T = 5.0 kHz distinct from the 10 kHz true-error limit; both conditions, C-16a sensitivity and C-18 for TC-SYS-101 confirmed by re-run and hand check | Verified | Pending | |
| finding-2 | reviewer | Major | CK-ANA-F1 | `frequency-budget.md` section 3.3 table U-1, U-2; section 4; section 5 | Unlocked trigger at both moments with the lock-detect means, the time budget and the "else a CR" branch; confirmed | Verified | Pending | |
| finding-3 | reviewer | Major | CK-ANA-F1, A6 | `clock-plan.md` sections 2, 2.1, 3, 5; ADR-031 | Core regulator, RT6150, charge pump and QSPI SCK added and classified; rules 2 and 6 and REQ-SYS-034 restated; confirmed against the datasheets (the further omission is finding-8) | Verified | Pending | |
| finding-4 | reviewer | Major | CK-ANA-A4, B1 | `clock-plan.md` section 2.1 R-4, rule 4; `clock_plan.py`; ADR-031 item 4 | I2C modelled per section 12.2.14 over 20 to 300 ns rise, non-coherent residual R-4 with a traffic rule; confirmed | Verified | Pending | |
| finding-5 | reviewer | Minor | CK-ANA-D3 | as iteration 1 | Not re-checked (delta, not addressed) | Open | Pending | |
| finding-6 | reviewer | Minor | CK-ANA-F4, A5 | as iteration 1 | Not re-checked (delta, not addressed) | Open | Pending | |
| finding-7 | reviewer | Minor | CK-ANA-J2, H1 | as iteration 1 | Not re-checked (delta, not addressed) | Open | Pending | |
| finding-8 | reviewer | Major | CK-ANA-F1, E5 | `clock-plan.md` section 2 and 5; ADR-031 sections 1 and 2 | ROSC (4.6 to 24 MHz, not stopped by ADR-051) and LPOSC (32.768 kHz +/-20 %) missing from "every clock" | Open | Pending | |
| finding-9 | reviewer | Minor | CK-ANA-D2 | `frequency-budget.md` section 3.3 row U-1 | "more than 5.482 kHz off trips" should be 9.518 kHz (T + d) | Open | Pending | |

### Checklist items changed at this iteration

| Id | Iteration 2 answer | Evidence |
|---|---|---|
| CK-ANA-A4 | Yes | I2C input corrected (finding-4 Verified); the FC0 time basis of finding-5 is Minor and open |
| CK-ANA-B1 | Yes | I2C model per section 12.2.14 (finding-4 Verified) |
| CK-ANA-D2 | No (Minor) | Note text and checker agree except the U-1 wording (finding-9) |
| CK-ANA-E3 | Yes | REQ-SYS-154 reported against the true-error limit with signed margins; the 482 Hz margin has its sensitivity (C-16a) |
| CK-ANA-E5 | No | REQ-SYS-154 and 182 proposals now supported; the REQ-SYS-034 range proposal is not, because the inventory is incomplete (finding-8) |
| CK-ANA-F1 | No | All four REQ-SYS-154 cases are present (off-frequency and unlocked, at key-down and during transmission). The "every clock" case is incomplete (finding-8) |
| CK-ANA-J2 | No (Minor) | swe-134 items h and l are now consistent with REQ-SYS-154 (findings 1, 2 Verified); the finding-7 TCXO-fault bound is still open |
| CK-ANA-I1, I2 | Yes | Two renders opened (visual closure above) |

### Cross items (not findings)

- **X-1.** Unchanged: CR-012 is not merged at `8abb467`, so the `checklist` field keeps the design checklist.
- **X-6 (software assurance pair).** ADR-031 is now a product of this record. 07 section 2.1.1, row "Trade studies and ADRs whose decision constrains a safety-critical or mission-critical component", therefore requires an SA pair. The reason is that ADR-031 item 4 fixes configuration constants of the WP-SW-11 clocks driver and the SW-SYNTH SPI, both safety-critical in 07 section 14.1. `assurance_required` is now true and `assurance_verdict` is pending. The record verdict cannot become APPROVED until the pair is APPROVED. This reviewer did not apply the SA lens.
- **X-7.** Route (a) of finding-8 is a request to the ADR-051 and WP-SW-11 writer (plan WP-PDR-41). ADR-051 is outside WP-PDR-20's files, so the WP-PDR-20 author sends it as a request (plan section 5.3) and does not edit it.

### Verdict (iteration 2)

```
VERDICT: NEEDS CHANGES
PRODUCT: docs/design/analysis/frequency-budget.md@79d47fbb, docs/design/analysis/clock-plan.md@8582121a, hardware/sim/freq/freq_budget.py@d82269e6, hardware/sim/freq/clock_plan.py@b9392297, docs/reviews/PDR/figures/frequency-budget.png@d77a0b3a, docs/reviews/PDR/figures/clock-plan-harmonics.png@19f47e3d, docs/decisions/adr/ADR-031-clock-plan.md@a578ca16 at 802347b
FINDINGS:
- [Major] finding-1 Verified: measured threshold T = 5.0 kHz distinct from the 10 kHz true-error limit; margins 482 / 2 482 Hz; TC-SYS-101 trips.
- [Major] finding-2 Verified: unlocked trigger at key-down (U-1) and during transmission (U-2, 30 ms), lock detect primary, CR branch named.
- [Major] finding-3 Verified: core regulator, RT6150, charge pump, QSPI SCK added; residual lines R-1 to R-3; rules restated.
- [Major] finding-4 Verified: I2C SCL 357.1 to 396.8 kHz per section 12.2.14, residual R-4 with a traffic rule.
- [Major] finding-8 (new): ROSC (4.6 to 24 MHz, left running by ADR-051) and LPOSC (32.768 kHz) missing from the inventory.
- [Minor] finding-9 (new): U-1 second-means wording 5.482 kHz should be 9.518 kHz.
- [Minor] finding-5 to finding-7 carried Open (not addressed, not re-checked, rule C1).
VALUES PROPOSED: REQ-SYS-008, 009, REQ-TX-002, REQ-SYS-010, REQ-TX-013, TPM-006 as iteration 1 (supported); REQ-SYS-154: 10 kHz true error with T = 5.0 kHz and lock detect (supported, subject to TS-007 value-of-information item 4 and the C-16a dev-board limit); REQ-SYS-182: 10 kHz, 100 ms with R3 (supported; finding-7 Minor open); REQ-SYS-034: 144.010 to 147.999 MHz, 3 dB (not supported, finding-8)
SA PAIR: required (07 section 2.1.1, ADR-031); pending
MEASUREMENTS: size=39 checker cases, 28 clock rows, 6 IF plans, 1 ADR; renders=2; turns=40; minutes=60; major=5 (4 verified, 1 new open); minor=4 open
```

Next: the author fixes finding-8 (and finding-9 at their option) and re-freezes. Iteration 3 of this record is then a delta on finding-8. It is the last iteration before escalation to the owner (rule C1; 07 section 10.2). The lead SE dispatches the SA pair for ADR-031 (X-6). Under rule C10, no value of either note goes to the owner until this record, with its SA pair, is APPROVED.
