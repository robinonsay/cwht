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
id: INSP-056
checklist: peer-review-checklist-design
checklist_revision: A
checklist_file: docs/reviews/PDR/checklists/analysis-frequency-budget-and-clock-plan.md
product: docs/design/analysis/frequency-budget.md
product_commit: "9ac2c42d1ff7b82e3734506aba14dec8eadc3923"
product_files: ["docs/design/analysis/frequency-budget.md@1a7be266d1a309391aea99b51dd4a2a82e892d4c", "docs/design/analysis/clock-plan.md@6e733d06f4a05c4b2505e1c1b4a175556cd631b6", "hardware/sim/freq/freq_budget.py@3cd21cb19c9f4835ac7505829af99379e2610dd5", "hardware/sim/freq/clock_plan.py@b21bc3b8cc18b07c426bb3a75704da5f3958b037", "docs/reviews/PDR/figures/frequency-budget.png@7ecf505fd974469caabbc9fdad7bf255e3d9be90", "docs/reviews/PDR/figures/clock-plan-harmonics.png@c22bb722aaa32f7ef2bace0e338506336c96b85a"]
analysis_kind: [budget, timing, worst-case, other]
product_size: 2 notes; 31 checker cases (27 PASS, 4 INFO) and 22 clocks in 6 IF plans; 2 checkers; 2 plots
tools_used: ["venv Python 3.13.5 (TV-001 accredits the interpreter; no TV record covers hardware/sim/freq/*.py, developer evidence per 05 section 9.1)"]
values_proposed: ["REQ-SYS-008: 144.0012 to 147.9988 MHz", "REQ-SYS-009: 144.0012 to 147.9988 MHz", "REQ-TX-002: 144.0012 to 147.9988 MHz", "REQ-SYS-010: +/-2.5 ppm, -10 to +45 C, one year after calibration", "REQ-SYS-154: 10 kHz", "REQ-SYS-182: 10 kHz and 100 ms (route R3)", "REQ-TX-013: fixed ratio 8, sample below 20 MHz, within 1 kHz", "REQ-SYS-034: 144.010 to 147.999 MHz, 3 dB above MDS", "TPM-006: cbe 0.834 / 0.984 / 1.234 ppm by class, credit false"]
renders_inspected: 2
sprint: PDR-prep
author_agent: "author:WP-PDR-20 wave 1a (Claude as RF designer TX)"
reviewer_agent: "reviewer:WP-PDR-20-analysis-iter1 (independent; authored no part of WP-PDR-20)"
# criticality: the frequency budget sets the window, times and calibration bound of the SW-SAFE frequency
# verification unit and the SW-SYNTH frequency-word path (07 section 14.1, safety-critical by SRR decision 9);
# section J answered here
criticality: safety-critical
# assurance_required: a stand-alone analysis note is not a row of 07 section 2.1.1 (template comment); the
# product path and slug carry no sw-<sub> token
assurance_required: false
assurance_reviewer_agent: none
iteration: 1
readiness_met: true
reviewer_verdict: NEEDS CHANGES
assurance_verdict: not-required
verdict: NEEDS CHANGES
findings_major: 4
findings_minor: 3
findings_open: 7
findings_fixed: 0
findings_verified: 0
findings_deferred: 0
assurance_tasks_applied: [swe-070 7.1 task 1, swe-134 7.1 task 1, swe-134 7.1 task 6]
deferred_rids: []
items_no: [CK-ANA-A4, CK-ANA-B1, CK-ANA-D3, CK-ANA-E3, CK-ANA-E5, CK-ANA-F1, CK-ANA-F4, CK-ANA-J2]
effort_turns: 44
effort_minutes: 80
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
