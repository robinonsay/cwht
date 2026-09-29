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
# Iteration 3 (delta, rule C1) at the re-freeze F0 commit 4153acf: the finding-8 fix only. clock-plan.md,
# ADR-031, clock_plan.py and clock-plan-harmonics.png changed; frequency-budget.md, freq_budget.py and
# frequency-budget.png are unchanged since 802347b. CR-012 is still not merged at 4153acf, so X-1 stands.
# Iteration 3 re-issue 1 (WP-PDR-20a, 2026-09-29): the full review (rule C1 iteration 1 of the WP-PDR-20a cycle)
# of frequency-budget.md revision 2 at its F0 commit 7593cea: new section 3.4 (route R3 for A5), the new checker
# r3_a5.py with run r3a5-20260929-01, and the revision 2 edits to sections 1, 2 and 4 to 8. The schema caps
# iteration at 3, so it is recorded as "Iteration 3 re-issue 1" (precedent INSP-117, INSP-110); the body calls it
# WP-PDR-20a iteration 1 (cross item X-8). Written into this record with the Edit tool by
# reviewer:WP-PDR-20a-analysis-iter1. The clock-plan.md, clock_plan.py, ADR-031 and clock-plan-harmonics.png
# blobs are unchanged since 4153acf and are listed for the record drift rule only; the WP-PDR-20a clock-plan work
# (clock_plan.py at clk_sys 96 MHz, the ADR-031 revision) is not in 7593cea and is not reviewed here. CR-012 is
# still not merged at HEAD f6ac3f0 (git merge-base --is-ancestor fails), so X-1 stands.
id: INSP-056
checklist: peer-review-checklist-design
checklist_revision: A
checklist_file: docs/reviews/PDR/checklists/analysis-frequency-budget-and-clock-plan.md
product: docs/design/analysis/frequency-budget.md
# product_commit (iteration 3 re-issue 1): 7593cea, frequency-budget.md revision 2 (WP-PDR-20a, freeze F0). Each
# blob below equals git rev-parse 7593cea:<path>, git rev-parse HEAD:<path> at HEAD f6ac3f0 and git hash-object
# <path> (17 of 17). thermal_model.py is imported unchanged by r3_a5.py (the INSP-112 blob). Iteration 3 listed 7
# blobs at 4153acf (frequency-budget.md 79d47fbb).
product_commit: "7593cea717e17fe2e542cb1cebb1d36c1fc948f6"
product_files: ["docs/design/analysis/frequency-budget.md@14229c9dfd943bc463eadab399f2bdbe8ac7f9cd", "hardware/sim/freq/r3_a5.py@eebcd167109046a0aff3cd0a238ef35470a6b155", "hardware/sim/freq/README.md@450bbd8cec8e6500d8817a70719652a4edc97853", "hardware/sim/freq/results/r3a5-20260929-01/results.json@53c58eaa1a66f7ff01adad52756d79efc5eb40f9", "hardware/sim/freq/results/r3a5-20260929-01/checker-output.txt@c73f1e60fb9d0ead825cdafbccbe5ec527795c12", "hardware/sim/freq/results/r3a5-20260929-01/r3_a5.py@eebcd167109046a0aff3cd0a238ef35470a6b155", "hardware/sim/freq/results/r3a5-20260929-01/relock-sequence.png@f9dac5c884981c38907165854f0c9ac66908e999", "hardware/sim/freq/results/r3a5-20260929-01/ratio-freshness.png@0a86c27e2cd71fd579e8055718d318f6b0122d8a", "hardware/sim/freq/results/r3a5-20260929-01/xosc-slope.png@ff5d30b3ec314514aa737f349f097a02a68ff86d", "hardware/sim/freq/results/r3a5-20260929-01/r3-budget-and-buffer.png@c0493e761f1e2571570515f88057f64184233750", "hardware/sim/thermal/thermal_model.py@54573514ad75cbae6edee930996f5fa5a745eed6", "hardware/sim/freq/freq_budget.py@d82269e6e9a7b2312d85c227d29de55236cdacc5", "docs/reviews/PDR/figures/frequency-budget.png@d77a0b3afac520643fdda042d188612b9123848e", "docs/design/analysis/clock-plan.md@07b5309613279d906bfdd3549618bb39ae8c7d81", "hardware/sim/freq/clock_plan.py@7e321b3d3355d8e94b464110292c3909483d3832", "docs/reviews/PDR/figures/clock-plan-harmonics.png@0a4d221c1c1690aa28331d0c429e65278feacb07", "docs/decisions/adr/ADR-031-clock-plan.md@58ceb119651feeadfc79a4c3d61ecfa916fa52d4"]
analysis_kind: [budget, timing, worst-case, other]
product_size: 2 notes and 1 ADR; 39 checker cases (35 PASS, 4 INFO) and 30 clock rows (5 named residual sources, 1 seeded case) in 6 IF plans; revision 2 adds 33 r3_a5.py cases (23 PASS, 10 INFO); 3 checkers; 6 plots
tools_used: ["venv Python 3.13.5 (TV-001 accredits the interpreter; no TV record covers hardware/sim/freq/*.py, developer evidence per 05 section 9.1)", "numpy 2.5.3 and matplotlib 3.11.2 in the venv (r3_a5.py; no TV record, developer evidence)", "hardware/sim/thermal/thermal_model.py@54573514 (INSP-112 reviewed model, no TV record, developer evidence)"]
values_proposed: ["REQ-SYS-008: 144.0012 to 147.9988 MHz", "REQ-SYS-009: 144.0012 to 147.9988 MHz", "REQ-TX-002: 144.0012 to 147.9988 MHz", "REQ-SYS-010: +/-2.5 ppm, -10 to +45 C, one year after calibration", "REQ-SYS-154: 10 kHz true-error limit, measured SW-SAFE threshold 5.0 kHz (route R3), lock-detect primary for the unlocked trigger; A5 (revision 2): Si5351A LOL_A, lock-gated changeover, ratio age at most 10 s at interval 12, 6.5 ppm drift allocation at interval 13", "REQ-SYS-182: 10 kHz and 100 ms (route R3; A5 conditions as REQ-SYS-154)", "REQ-TX-013: fixed ratio 8, sample below 20 MHz, within 1 kHz", "REQ-SYS-034: 144.010 to 147.999 MHz, 3 dB above MDS", "TPM-006: cbe 0.834 / 0.984 / 1.234 ppm by class, credit false"]
renders_inspected: 5
sprint: PDR-prep
author_agent: "author:WP-PDR-20 wave 1a (Claude as RF designer TX); revision 2 by author:WP-PDR-20a analysis"
reviewer_agent: "reviewer:WP-PDR-20a-analysis-iter1 (independent; authored no part of WP-PDR-20 or WP-PDR-20a; iterations 1 to 3 by reviewer:WP-PDR-20-analysis-iter1, -iter2 and -iter3)"
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
# assurance_reviewer_agent (iteration 3 re-issue 1): the INSP-111 pair (sa-reviewer:WP-PDR-20-insp-056-adr-031)
# returned APPROVED on the 4153acf blobs (d77fcc2). Plan row 20 asks for the INSP-111 delta on WP-PDR-20a; that
# delta has not run on 7593cea, and the lead SE dispatches it (rule C4)
assurance_required: true
assurance_reviewer_agent: "sa-reviewer:WP-PDR-20-insp-056-adr-031 (INSP-111, APPROVED at 4153acf); WP-PDR-20a delta on 7593cea pending, to be dispatched by the lead SE"
iteration: 3
readiness_met: true
# reviewer_verdict (iteration 3 re-issue 1, WP-PDR-20a iteration 1): NEEDS CHANGES; two new Major findings on
# section 3.4 (finding-11, TCXO term missing from the ratio drift; finding-12, FC0 interval times rounded down
# set the L_max deadline), five new Minor findings (13 to 17). Findings 5, 6, 7, 9 and 10 stay Open as liens
reviewer_verdict: NEEDS CHANGES
# assurance_verdict: the INSP-111 delta for revision 2 has not run
assurance_verdict: pending
# verdict: NEEDS CHANGES (open Major findings 11 and 12; SA delta pending; X-1)
verdict: NEEDS CHANGES
findings_major: 7
findings_minor: 10
findings_open: 12
findings_fixed: 0
findings_verified: 5
findings_deferred: 0
assurance_tasks_applied: [swe-070 7.1 task 1, swe-134 7.1 task 1, swe-134 7.1 task 6]
deferred_rids: []
# items_no (iteration 3 re-issue 1, revision 2 content): findings 11 to 17, plus the earlier liens
items_no: [CK-ANA-A4, CK-ANA-A5, CK-ANA-B1, CK-ANA-D2, CK-ANA-D3, CK-ANA-E5, CK-ANA-F2, CK-ANA-F4, CK-ANA-G2-1, CK-ANA-H2, CK-ANA-J2]
effort_turns: 45
effort_minutes: 90
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

## Iteration 3: delta verification of finding-8 (Major) (2026-09-27)

**Scope (rule C1).** A delta that verifies the one open Major fix, finding-8, only. The author re-froze the products at `4153acf` (freeze F0, rule C2), which is also `HEAD` at review time: `clock-plan.md` `07b53096`, ADR-031 `58ceb119`, `clock_plan.py` `7e321b3d` and `clock-plan-harmonics.png` `0a4d221c`. `frequency-budget.md` `79d47fbb`, `freq_budget.py` `d82269e6` and `frequency-budget.png` `d77a0b3a` are unchanged since `802347b`. Each blob was checked equal at `HEAD` (`git rev-parse HEAD:<path>`) and in the working tree (`git hash-object`). `4153acf` is on `main`, and no product blob lives only on a `cr/` branch. The change was read as `git diff 802347b 4153acf` on `clock-plan.md`, ADR-031 and `clock_plan.py`. This is the third and last iteration before escalation to the owner (rule C1; 07 section 10.2). Minor findings 5, 6, 7 and 9 were not addressed (rule C1) and were not re-checked. The iteration 1 and 2 checklist answers stand except where this section changes them.

**Independence (rule C4).** This invocation authored no part of WP-PDR-20 (TS-007, both notes, ADR-031, the checkers, the figures, revision 2) and did not write iterations 1 or 2 of this record, or INSP-055 or INSP-074. It edited no product file.

**Search first (charter section 11 rule 1).** The step that loaded the search tool also ran one `git log`, `git show --stat` and `ls` of this directory (no search). `mcp__claude-context__search_code` then ran before every manual search. Queries on `/Users/robinonsay/rust/cwht`: the INSP-056 record and finding-8; TRNG use in the cwht firmware; the ADR-051 clock bring-up. On `/Users/robinonsay/rust/rustos`: the ROSC CTRL and STATUS registers; the TRNG entropy source. `grep` and `sed -n` afterwards only pinned lines of known files. RP2350 text was read only from the committed object `git show 2ec64c0f:docs/extracted/rp2350-datasheet.md`, exported to the scratchpad. The search index returned rustos extract text; every quoted line below was re-read from that committed object. The rustos working tree was not read.

**Acceptance criteria for the delta (rule C7).** These are the cases the finding-8 fix clause lists:
- ROSC added, with its range and datasheet lines, and either route (a) (a disable rule, with requests to WP-PDR-41 and WP-PDR-35 and a HostUnit check) or route (b) (a named residual source).
- LPOSC added as a named residual source, or shown to be stopped in operation.
- Checker, figure, rule 2, the REQ-SYS-034 row and ADR-031 updated to match.

The governing output ("harmonic table of every clock against 144 to 148 MHz and the IF") is checked against both ends of 144.010 to 147.999 MHz and the CW-only segment 144.010 to 144.100 MHz. For the ROSC, both datasheet ranges are checked (4.6 to 19.6 MHz without randomisation, 4.6 to 24.0 MHz with it). For the LPOSC, both Table 615 ranges are checked (initial and trimmed). For rule 11, every state in which the ROSC restarts is checked: power-up, DORMANT exit and switched-core power-up.

### Verification of finding-8

**finding-8 (RP2350 oscillators missing from the inventory): Verified.** The author took route (a) for the ROSC and made the LPOSC residual R-5.

| Element of the fix | Result | Evidence |
|---|---|---|
| ROSC in the inventory with range and source | Yes | `clock-plan.md` section 2 row "RP2350 ring oscillator (ROSC), 4.6 to 24.0 MHz", status off in operation (rule 11). The quotes from section 8.3.1 match the extract: the range at lines 41089 to 41091 and "You can disable the ROSC" at line 41093, both inside the note's range 41086 to 41093; "started automatically during RP2350 power up" is at line 41082. The new class "Off in operation" in section 1 covers it and the charger boost |
| Route (a): rule 11 is correct against the datasheet | Yes | Order: "The system clock must be switched to another source before setting this field to DISABLE otherwise the chip will lock up" (Table 605, line 41353), and the rule disables only after both SELECTED read-backs. Encoding: 0xd1e is DISABLE (Table 605). Read-back: STATUS.ENABLED is bit 12, RO, "Oscillator is enabled but not necessarily running and stable" (Table 612, line 41599), so ENABLED = 0 is the right post-condition. Fault: the read-back failure gives a ClockFault, consistent with the other ADR-051 steps |
| Rule 11: every ROSC restart state covered | Yes | Power-up: the ROSC "is started automatically during RP2350 power up" (8.3.1), so the bring-up disables it. DORMANT: "When exiting DORMANT mode, the ROSC restarts in the same configuration" (8.1.1.2, line 37453). Switched-core power-up: "The ROSC is unpowered when the switched-core domain is powered down, but starts immediately when the switched-core powers up" (line 37451), and Table 101 confirms that clk_ref runs from the ROSC at switched-core power-up. Rule 11 repeats the disable after both. The DORMANT repeat is redundant when the ROSC was already disabled (the "same configuration" is disabled), but it does no harm and the rule is correct either way |
| "Nothing needs the ROSC after bring-up" | Yes | Resus "switches clk_sys to a known good clock source (clk_ref)" (8.1.4, line 37973), and clk_ref runs from the XOSC. With the ROSC running but not selected, resus behaves the same, so stopping the ROSC loses no fallback. POWMAN USE_FAST_POWCK reset 1 selects clk_ref (line 34510). Reviewer: the cwht search found no TRNG or ROSC RANDOMBIT use in cwht |
| Fault state | Yes | After a ClockFault the ROSC may still clock the chip. The radio stays in the ADR-051 safe state (REQ-SYS-130), so these lines occur in a fault state, not in operation. Stated in rule 11, last item |
| Fallback named | Yes | ADR-031 assumption 6 and revisit condition: without rule 11 the ROSC is R-6 and the REQ-SYS-034 range support does not hold. The `clock-plan.md` section 5 range row states the same "else" branch |
| Requests | Yes | WP-PDR-41 (the ADR-051 and WP-SW-11 writer; ADR-051 is outside WP-PDR-20's files, plan section 5.3), WP-PDR-35 (SW-CTL requirement with a HostUnit check: the CTRL write comes after both read-backs, and a stuck ENABLED gives the fault), WP-PDR-16b (rule 11 into HZ-008 K6), and TC-SYS-022 (a pre-step that confirms the ROSC is off) |
| ROSC order counts | Yes | Reviewer: CW-only segment, n = ceil(144.010 / 24.0) = 7 to floor(144.100 / 4.6) = 31, which is 25 orders. Band, n = 6 (6 x 24.0 = 144.000 MHz) to floor(148 / 4.6) = 32. Neighbouring intervals overlap because n x 24.0 >= (n + 1) x 4.6 for every n >= 1, so they cover the band. Without randomisation: ceil(144.010 / 19.6) = 8, so orders 8 to 31 (limitation 8). All agree with the checker and the note |
| LPOSC as residual R-5 | Yes | Table 615 (lines 41668 to 41685): F0.initial 26.2144 / 32.768 / 39.3216 kHz, F0.trimmed 32.27648 / 33.25952 kHz, drift +/-14 % with temperature and +/-20 % with supply. Cannot be stopped: Table 487 MODE "This feature has been removed" (line 34212), and Table 101 WAITING_POWCK "The solution is to not stop LPOSC when the switched-core power domain is powered" (line 6704). Reviewer counts: untrimmed n = ceil(144 / 0.0393216) = 3 663 to floor(148 / 0.0262144) = 5 645, which is 1 983 intervals; trimmed 4 330 to 4 585, which is 256; CW-only segment 3 663 to 5 496, which is 1 834. Coverage holds because n x f_hi >= (n + 1) x f_lo for n >= 2 (untrimmed) and n >= 33 (trimmed). All agree with the checker. Control is level only, plus the allocated rule that no clock generator, clk_gpout or frequency-counter output takes the LPOSC in operation |
| Rule 2, REQ-SYS-034 rows, ADR-031 | Yes | Rule 2 now covers R-1 to R-5 and adds "the ROSC meets it only by rule 11". The section 5 range row is conditioned on rule 11, and the allowance row covers R-1 to R-5. ADR-031: context (five residual sources plus the ROSC), research consulted, assumptions 4 and 6, items 2 and 8, new item 9 (it matches rule 11 point by point), option A, section 4.1 (new SW-CTL row and the LPOSC routing rule), 4.2, 4.3 (Test with R-1 to R-5 active and the ROSC confirmed off), 4.4, memo wording, revisit conditions and change log. None contradicts `clock-plan.md` revision 2 |
| Checker | Yes | `ROSC_RANGE`, `LPOSC_INITIAL`, `LPOSC_TRIMMED` equal the datasheet values. The ROSC status is `off-in-op` normally and `fixed` under `--rosc-running`, so rules 1 and 2 test it only in the seeded case. The `merged` and `covers` helpers are correct for intervals sorted by lower end (reviewer read) |

### Reviewer re-runs

| Command | Exit | Result |
|---|---|---|
| `git archive 4153acf hardware/sim/freq <two PNGs>` into the scratchpad; `.venv/bin/python hardware/sim/freq/clock_plan.py --plot` | 0 | "RESULT: 0 rule failure(s) in the proposed plan; 5 named residual source(s)"; table "RP2350 oscillators" as quoted above; 30 clock rows |
| `.venv/bin/python hardware/sim/freq/clock_plan.py --rosc-running` (same export) | 1 | "FAIL RULE-1" and "FAIL RULE-2" for the ROSC (n = 7 to 32 in range, 7 to 31 in the CW-only segment); "RESULT: 2 rule failure(s) in the proposed plan; 5 named residual source(s)". The seeded case catches the ROSC left running, as the note says |
| `.venv/bin/python hardware/sim/freq/freq_budget.py` (same export) | 0 | "RESULT: 35 pass, 0 fail" (unchanged product; run only to confirm) |
| `git hash-object` of the regenerated `clock-plan-harmonics.png` | 0 | `0a4d221c`: byte-identical to the frozen figure |

### Visual closure (iteration 3)

Both frozen figures were opened with the Read tool (2 renders).
- `clock-plan-harmonics.png`: the title names "olive off in operation" and "magenta named residual". The LPOSC row ([residual], magenta) and the ROSC row ([off-in-op], olive, labelled "disabled in operation by rule 11") are each one merged bar across 124 to 170 MHz, as reproduction section 7 says. The other rows match iteration 2. The legend still covers the XOSC n = 14 label at 168 MHz (cosmetic, as before).
- `frequency-budget.png`: unchanged blob; opened to confirm the render is the frozen one.

### New finding at iteration 3

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-10"></a>finding-10 | reviewer (iteration 3, while checking the finding-8 completeness claim) | Minor | CK-ANA-A5 | `clock-plan.md` section 2 and rule 11; ADR-031 item 9 | See the note after this table | Open | Pending | CDR readiness declaration (lien, rule C1) |

**finding-10 (TRNG ring oscillator not stated).**
- **Defect.** The RP2350 TRNG has its own ring oscillator. It is "a free-running oscillator with no direct connection to the system clocks" (section 12.12.1, extract lines 91111 to 91155). It runs only while TRNG RND_SOURCE_ENABLE.RND_SRC_EN = 1, and its reset value is 0 (Table 1267). The datasheet gives no frequency for it. The note does not mention it, and rule 11 covers only the main ROSC and its RANDOMBIT and COUNT registers.
- **Why Minor.** It is not running in operation as the design stands: the reset value is 0, and cwht has no TRNG use (reviewer search). So no case of "every clock running in operation" is missing. What is missing is a stated assumption, with its control, that the TRNG entropy source stays disabled in operation. Whether the bootrom leaves it disabled after boot is not in the corpus.
- **Fix (lien).** Add the TRNG ring oscillator to section 2 as off in operation. Extend rule 11, the WP-PDR-35 request and ADR-031 item 9 so that RND_SRC_EN reads 0 after bring-up (or the TRNG is held in reset), with the same read-back pattern. Otherwise name it residual R-6 with "frequency not in the corpus".

### Findings (iteration 3 state)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| finding-1 | reviewer | Major | CK-ANA-E3, E5, F1 | `frequency-budget.md` section 3.3, section 4 | Verified at iteration 2 (product unchanged) | Verified | Pending | |
| finding-2 | reviewer | Major | CK-ANA-F1 | `frequency-budget.md` section 3.3 | Verified at iteration 2 (product unchanged) | Verified | Pending | |
| finding-3 | reviewer | Major | CK-ANA-F1, A6 | `clock-plan.md` sections 2, 2.1, 3, 5; ADR-031 | Verified at iteration 2; the revision 2 edits keep R-1 to R-4 as they were | Verified | Pending | |
| finding-4 | reviewer | Major | CK-ANA-A4, B1 | `clock-plan.md` R-4, rule 4; `clock_plan.py`; ADR-031 item 4 | Verified at iteration 2; the I2C table re-runs the same | Verified | Pending | |
| finding-5 | reviewer | Minor | CK-ANA-D3 | as iteration 1 | Not addressed, not re-checked (rule C1); lien due at the CDR readiness declaration | Open | Pending | CDR readiness declaration |
| finding-6 | reviewer | Minor | CK-ANA-F4, A5 | as iteration 1 | Not addressed, not re-checked (rule C1); lien | Open | Pending | CDR readiness declaration |
| finding-7 | reviewer | Minor | CK-ANA-J2, H1 | as iteration 1 | Not addressed, not re-checked (rule C1); lien | Open | Pending | CDR readiness declaration |
| finding-8 | reviewer | Major | CK-ANA-F1, E5 | `clock-plan.md` sections 1, 2, 2.1, 3 (rules 2 and 11), 5, 6, 7; ADR-031 sections 1 to 8; `clock_plan.py`; figure | ROSC off in operation by rule 11 (route (a)), with seeded case `--rosc-running`; LPOSC residual R-5; confirmed against the datasheet, re-run and render | Verified | Pending | |
| finding-9 | reviewer | Minor | CK-ANA-D2 | `frequency-budget.md` section 3.3 row U-1 | Not addressed (rule C1); lien | Open | Pending | CDR readiness declaration |
| finding-10 | reviewer | Minor | CK-ANA-A5 | `clock-plan.md` section 2, rule 11; ADR-031 item 9 | TRNG ring oscillator not stated as off in operation; lien | Open | Pending | CDR readiness declaration |

### Checklist items changed at this iteration

| Id | Iteration 3 answer | Evidence |
|---|---|---|
| CK-ANA-A5 | No (Minor) | The assumption that the TRNG entropy source stays disabled is not stated (finding-10); finding-6 is also still open |
| CK-ANA-E5 | Yes | The REQ-SYS-034 range proposal is now supported, and it is conditioned on rule 11 with the "else" branch (R-6, assumption 6) named |
| CK-ANA-F1 | Yes | Every clock running in operation is in the inventory: the ROSC is off in operation by rule 11, and the LPOSC is residual R-5. Both ROSC ranges and both LPOSC ranges were checked against both band ends and the CW-only segment |
| CK-ANA-I1, I2 | Yes | Two renders opened; the new rows agree with the checker output |

### Cross items (not findings)

- **X-1.** Unchanged: CR-012 is not merged at `4153acf` (`git merge-base --is-ancestor` fails). The `checklist` field keeps the design checklist. The analysis template blob is still `0386cc6e` on the branch.
- **X-6 (software assurance pair).** Still required (07 section 2.1.1, ADR-031), and it has not run: no paired record exists for INSP-056. Rule 11 adds a safety-critical WP-SW-11 step with a fault path, and the SA pair should cover it. This reviewer did not apply the SA lens.
- **X-7.** Rule 11 is a request to WP-PDR-41, and ADR-031 assumption 6 carries it. Until WP-PDR-41 adopts it, the firmware as written matches the seeded case (2 rule failures). The owner ruling of REQ-SYS-034 at B2 (rule C10) therefore rests on assumption 6 being confirmed before B2, as the ADR states.

### Verdict (iteration 3)

```
VERDICT: NEEDS CHANGES (record verdict held; reviewer verdict APPROVED)
PRODUCT: docs/design/analysis/frequency-budget.md@79d47fbb, docs/design/analysis/clock-plan.md@07b53096, hardware/sim/freq/freq_budget.py@d82269e6, hardware/sim/freq/clock_plan.py@7e321b3d, docs/reviews/PDR/figures/frequency-budget.png@d77a0b3a, docs/reviews/PDR/figures/clock-plan-harmonics.png@0a4d221c, docs/decisions/adr/ADR-031-clock-plan.md@58ceb119 at 4153acf
FINDINGS:
- [Major] finding-8 Verified: ROSC off in operation by rule 11 (route (a), CTRL.ENABLE 0xd1e after both SELECTED read-backs, STATUS.ENABLED read-back with fault, repeated after DORMANT exit and switched-core power-up), fallback R-6 named, seeded case exits 1; LPOSC residual R-5 (Tables 487, 101, 615).
- [Major] finding-1 to finding-4 Verified at iteration 2, products unchanged or consistent.
- [Minor] finding-10 (new): TRNG ring oscillator not stated as off in operation; lien due at the CDR readiness declaration.
- [Minor] finding-5, 6, 7, 9 Open, not addressed (rule C1); liens due at the CDR readiness declaration.
VALUES PROPOSED: REQ-SYS-008, 009, REQ-TX-002, REQ-SYS-010, REQ-TX-013, TPM-006, REQ-SYS-154, REQ-SYS-182 as iteration 2 (supported); REQ-SYS-034: 144.010 to 147.999 MHz, 3 dB above MDS (supported, given rule 11 per ADR-031 assumption 6)
SA PAIR: required (07 section 2.1.1, ADR-031); not yet run
MEASUREMENTS: size=39 checker cases, 30 clock rows, 6 IF plans, 1 ADR; renders=2; turns=30; minutes=45; major=5 (5 verified, 0 open); minor=5 open (liens)
```

The record verdict is held at NEEDS CHANGES for two reasons. First, the SA pair (X-6) has not returned APPROVED (07 sections 2.1.1 and 10.2). Second, under the lead SE convention of 2026-09-27, the analysis template blob `0386cc6e` has to reach `main` through CR-012 (X-1). When both are met, the record verdict is set to APPROVED in that commit, without another product iteration. Under rule C10, no value of either note goes to the owner before then.

## Measurements (SWE-089), iteration 3

Items re-checked 5 (A5, E5, F1, I1, I2); items answered No 5 (A5, D2, D3, F4, J2, all Minor); findings 5 Major (all Verified), 5 Minor (Open, liens); fixed 0; deferred 0; iteration 3; renders inspected 2; effort 30 turns, about 45 minutes.

## Iteration 3 re-issue 1: WP-PDR-20a iteration 1, frequency-budget.md revision 2 (route R3 for A5) (2026-09-29)

**Scope (rule C1).** A full review of the revision 2 content: section 3.4 (3.4.1 relock, 3.4.2 ratio freshness, 3.4.3 squaring stage, 3.4.4 LOL_A and U-2), the new checker `hardware/sim/freq/r3_a5.py` (`eebcd167`) with run `r3a5-20260929-01`, and the revision 2 edits to the header and sections 1, 2 and 4 to 8, read as `git diff 4153acf 7593cea` on the note. The author froze the products at `7593cea` (freeze F0, rule C2). Every `product_files` blob equals `git rev-parse 7593cea:<path>`, `git rev-parse HEAD:<path>` at `HEAD` `f6ac3f0` and `git hash-object <path>`; no product blob lives only on a `cr/` branch. Sections 3.1 to 3.3, `freq_budget.py` and `frequency-budget.png` are unchanged and were not re-reviewed (a re-run confirms them). The clock-plan half of WP-PDR-20a (`clock_plan.py` at clk_sys 96 MHz, the ADR-031 revision) is not in `7593cea`; the note says so in section 1. Minor findings 5, 6, 7, 9 and 10 stay liens (rule C1); findings 5 and 9 bear on this revision and are cross-referenced below.

**Independence (rule C4).** This invocation authored no part of WP-PDR-20 or WP-PDR-20a (TS-007, TS-012, either note, ADR-031, any checker, figure or run) and wrote no earlier iteration of this record, of INSP-111 or of INSP-118. It edited no product file.

**Search first (charter section 11 rule 1; plan rule C3).** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any `grep` or `find` (queries: the WP-PDR-20a products and record; the TG2520SMN parameters; the A5 board and bay placement; the datasheet-reading practice). The index returned a pre-freeze text of the note header; every quote below was re-read from the `7593cea` objects. `grep -n` afterwards only pinned lines in known files. `/Users/robinonsay/rust/rustos` was not read, in either the working tree or its objects; RP2350 facts are taken from the iteration 1 record (Tables 541, 582, 596).

**Sources re-read (CK-ANA-A4).** The two Skyworks PDFs were fetched with the web-fetch tool (the project's datasheet practice, as in INSP-110 and the `hardware/sim/tx-pa` README), cached outside the repository and converted with `pdftotext` in the scratchpad; nothing was added to the repository. SHA-256: data sheet `f3bc5285...a4851101f`, AN619 `0135b3a3...4783f36b`, both equal to the checker's `SOURCES`. Checked against the checker constants and the note's section 2 rows:
- Data sheet Rev. 1.3, August 27, 2021, Table 5 "AC Characteristics": TRDY "From VDD = VDDmin to valid output clock, CL = 5 pF, fCLKn > 1 MHz", typ 2, max 10 ms; TOE max 10 us; TFREQ "fCLKn > 1 MHz", max 10 us. No lock, settle or acquisition time anywhere in the text (searched). Section 5: "Standard-Mode (100 kbps) or Fast-Mode (400 kbps) and supports burst data transfer with auto address increments"; reg0[6:5] LOL_A, LOL_B. Section 4.6: only the Si5351C in the 20-QFN has INTR. Figure 10: "Apply PLLA and PLLB soft reset Reg. 177 = 0xAC" after the configuration write. All agree.
- AN619 Rev. 0.8, September 23, 2021: register 0 bit 5 LOL_A, "0: PLL A is operating normally. 1: PLL A is unlocked", loss of lock when the reference forces the PLL "outside of its lock range" or fails the input requirements; register 177 PLLA_RST "Writing a 1 to this bit will reset PLLA. This is a self clearing bit". All agree. AN619 also gives register 1 bit 5 LOL_A_STKY, a sticky bit that "remains high until cleared", which the note does not use (finding-14).
- Requirements at `HEAD`: REQ-SYS-160 "begin the RF rise within 15 ms (TBR)"; REQ-SYS-161 "the same lead-in of at most 12 ms (TBR) after the receive-to-transmit changeover"; REQ-SYS-180 "end RF, independently of firmware, at 150 s to 180 s (TBR) of continuous transmit and hold it off until receive resumes". TS-012 section 7.3 (the sequence, PA_EN at t0 + 7 ms, TX_KEY at t0 + 8 ms, ramp at t0 + 10 ms, the interval-13 fallback with the ramp at 11.5 ms) and section 10 (relock exceeds 1 ms "by more than the 3 ms between the check and the ramp"; 1 ppm freshness). Plan section 10.6 row "a trigger goes to the owner at S1 if it changes CR-018, else at S2". All agree with the note.
- Inputs that disagree: the FC0 interval times (finding-12; the checker takes the Table 541 rounded 4, 8 and 32 ms, not 2^n x 1 us), and the I2C SCL of "exactly 400 kHz" against this project's own SCL model (finding-13).

**Acceptance criteria (rule C7), from plan section 3.0 row 20 (WP-PDR-20a), TS-012 section 10 and the governing requirements.**
- Relock: the Si5351A relock time read from a source against the 1 ms allocation; the TS-012 threshold (1 ms exceeded by more than 3 ms); the key-down sequence with the ramp at t0 + 10 ms and at its limit; the interval-13 fallback.
- Freshness: the ratio age at every check with the squaring stage off in transmission, over the longest over REQ-SYS-180 allows (180 s), against the 1 ppm allocation; both checks, interval 12 (key-down) and interval 13 (during the over); both A5 layouts; ambient -10 and +45 C; heating and cooling.
- Route R3 budget (D-17): FC0 on GPIN0 and GPIN1 below the GPIN limit; intervals 12 and 13; REQ-SYS-154 all four cases (off-frequency and unlocked, at key-down and during transmission); REQ-SYS-182 both branches; the TC-SYS-101 12 kHz injection at both intervals; the squaring stage powered only in receive and its 150.000 MHz line; its lines against every receive window (144.010 to 147.999 MHz, the 8 MHz IF, the LO and image bands for both injection sides).

### Reviewer re-runs

| Command | Exit | Result |
|---|---|---|
| `git archive 7593cea hardware/sim/freq hardware/sim/thermal docs/reviews/PDR/figures/frequency-budget.png` into the scratchpad; `.venv/bin/python hardware/sim/freq/r3_a5.py --run-id rev-check` (4.3 s) | 0 | "RESULT: 23 pass, 0 fail, 10 info"; `checker-output.txt` equal to the frozen one line for line (only the `outputs:` path differs); `results.json` equal to the frozen one after removing `run_id` |
| `git hash-object` of the four regenerated PNGs | 0 | `f9dac5c8`, `0a86c27e`, `ff5d30b3`, `c0493e76`: byte-identical to the frozen figures |
| `cmp results/r3a5-20260929-01/r3_a5.py hardware/sim/freq/r3_a5.py` (export) | 0 | the run copy is the checker as frozen (both `eebcd167`) |
| `.venv/bin/python hardware/sim/freq/freq_budget.py` (same export) | 0 | "RESULT: 35 pass, 0 fail", unchanged |

### Independent checks (CK-ANA-B5, G2-2)

- **I2C time.** Bursts of 8, 3, 1 and 8 data bytes, each 9 x (2 + n) + 2 SCL clocks: 92 + 47 + 29 + 92 = 260 clocks. At 400 kHz 0.650 ms; 256 kHz 1.0156 ms; 100 kHz 2.600 ms; SCL for 1 ms less TFREQ: 260 / 0.990 ms = 262.6 kHz, so 263 kHz. LOL_A read 9 x 4 + 3 = 39 clocks, 0.0975 ms. All agree with RL-2, RL-2s, RL-2b and RL-3.
- **L max** as the checker computes it: 10 - 2 - 4 - 2 = 2.0 ms; 12 - 2 - 4 - 2 = 4.0 ms; 12 - 2 - 8 - 2 = 0 ms. The arithmetic agrees; the 4 and 8 ms inputs do not (finding-12).
- **Slope bound, by a different method.** For Ti = 25 C and a3 = 1.3e-4 ppm/K^3 the admissible first-order term is limited by the interior extremum (2/3) abs(a1) sqrt(abs(a1) / (3 a3)) <= 30 ppm, so abs(a1)^1.5 <= 45 sqrt(3.9e-4) = 0.8887 and abs(a1) <= 0.9243 ppm/K. The slope at 25 C is a1 itself, so the 0.924 ppm/K of FR-1 is the closed-form answer, not a grid artefact.
- **Freshness.** A_kd limit (1 - 0.2) / (0.924 x (0.035 + 0.047)) = 10.57 s; drift at 10 s 0.957 ppm (the checker prints 0.958 after rounding up; the note's 0.957 is `results.json` 0.95703). FR-4: 0.924 x (4.993 + 1.41) + 0.2 = 6.116 ppm. Ceilings: interval 12, (5 000 - 4 000 - 370.0) / 147.9988 = 4.257 ppm; interval 13, (5 000 - 2 000 - 370.0) / 147.9988 = 17.77 ppm (both conditions give the same value because T = L/2).
- **Budget.** d12 = 4 000 + 147.9988 x 3.5 = 4 518.0 Hz; d13 = 2 000 + 147.9988 x 9.0 = 3 332.0 Hz; T + d 9 518.0 and 8 332.0 Hz; injection 12 000 - d = 7 482.0 and 8 668.0 Hz. All agree with B-12, B-16 and B-18.
- **Squaring-stage lines.** 6 x 25 MHz x (1 - 2.5 ppm) = 149.999625 MHz, 2.001 MHz above 147.999 MHz, and 150.000375 MHz is 2.010 MHz below the high-side LO band (152.010 MHz); 5 x 25 MHz is 3.010 MHz below the low-side image band (128.010 MHz); the other harmonics are further from every window. Agrees with BL-1 (nearest 2 001 kHz).
- **Self-validating check (section 3.4.1).** A settling transient of equivalent full-error duration tau moves the interval-12 mean by 8 MHz x tau / 4.096 ms; it exceeds T = 5 kHz for tau above 2.56 us. Agrees with the note's 2.5 us to within the finding-12 rounding. The argument that a slow relock costs availability, not an unchecked carrier, holds: the GVA-84+ is unpowered until PA_EN, TX_KEY and Q are all true (D-18), and a loop that settles to a wrong frequency is caught at interval 13 within C-15.

### Findings (iteration 3 re-issue 1)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-11"></a>finding-11 | reviewer | Major | CK-ANA-B1, G2-1, E5, J2 | `frequency-budget.md` section 3.4.2 ("The drift is the XOSC slope times the crystal's temperature change, plus pushing", the drift table, the A_kd paragraph, the split table), section 2 revision 2 rows, section 5 rows WP-PDR-35 and WP-PDR-43 (M-2 pass); `r3_a5.py` FR-2, FR-4, FR-6, `healthy()` | See the note after this table | Open | Pending | |
| <a id="finding-12"></a>finding-12 | reviewer | Major | CK-ANA-D3, A4, E5 | `r3_a5.py` `T_FC0 = {iv: fb.FC0[iv][0] ...}` with the comment "(1 us scale, conservative)"; RL-4, RL-5, RL-6, RL-8, FR-2r, B-19; `frequency-budget.md` section 3.4.1 (L table, design response item 1, M-1 pass branches), 3.4.4 (U-1 times), section 5 row WP-PDR-23a; `relock-sequence.png` | See the note after this table | Open | Pending | |
| <a id="finding-13"></a>finding-13 | reviewer | Minor | CK-ANA-A4, D2 | `frequency-budget.md` section 3.4.1 "Time the sequence allows" (0.650 ms, 0.35 ms left), M-1 pass ("settle at most 0.35 ms, which keeps the 1 ms allocation at 400 kHz"), section 6 item 8 | The write time assumes SCL exactly 400 kHz. This project's own SCL model (`clock-plan.md` R-4, INSP-056 finding-4 Verified; RP2350 section 12.2.14) gives 357.1 to 396.8 kHz for the 400 kHz-nominal counts over the 20 to 300 ns rise range, so the C6 writes take 0.655 to 0.728 ms and leave 0.272 to 0.345 ms of the 1 ms allocation (reviewer: 260 / 396.8 kHz and 260 / 357.1 kHz); the bus-free time between the four bursts and the software gaps are also not counted. Item 8 says a slower SCL lengthens the time "in proportion" but does not bound it. No pass or fail changes (RL-2 holds at 0.728 ms). Fix: state the write time over the SCL range the WP-PDR-32 counts give (or the clock-plan R-4 range), and write the M-1 pass criterion as "writes plus settle at most 1 ms at the measured SCL" | Open | Pending | |
| <a id="finding-14"></a>finding-14 | reviewer | Minor | CK-ANA-F2, A3 | `frequency-budget.md` section 3.4.4, option (b) and the paragraph after it; section 4 revision 2 "else a CR" bullet | Option (b) says an unlock that stays inside T during a long element "is caught only by the counter once it drifts past T", and the REQ-SYS-154 CR question is put to the owner on that basis. AN619 register 1 bit 5 LOL_A_STKY "is triggered when the LOL_A bit ... is triggered high. It remains high until cleared", so under (b) an unlock during an element is latched and read at the next key-up gap or key-down read (the element itself is bounded by REQ-SYS-055, 13 s). That changes the stated consequence of (b) and the CR question. The sticky bit also sets during each changeover relock and has to be cleared after lock. Fix: add LOL_A_STKY to option (b) and to the WP-PDR-32 and 35 requests (clear after the lock-gated start; read at every key-up gap), and restate the consequence | Open | Pending | |
| <a id="finding-15"></a>finding-15 | reviewer | Minor | CK-ANA-F4, D2 | `frequency-budget.md` section 3.3 C-16a text ("at most 560.2 Hz at interval 13"), section 6 item 4, section 5 row WP-PDR-43 ("560 Hz at interval 12") | With the 6.5 ppm allocation at interval 13 the FC0 accuracy ceiling there falls from 560.2 Hz to 458.5 Hz (reviewer: 8a + 147.9988 x 9.0 < 5 000 gives a < 458.5 Hz; the T + d <= 10 kHz condition gives the same). Section 3.4 does not restate it, and section 3.4 "governs for A5 wherever it differs" leaves the dev-board acceptance for interval 13 implicit. No pass or fail changes (Table 541 gives 250 Hz at interval 13). Fix: state the interval-13 ceiling for the checks during the over, and use it in the WP-SW-14 known-clock acceptance | Open | Pending | |
| <a id="finding-16"></a>finding-16 | reviewer | Minor | CK-ANA-A5 | `frequency-budget.md` section 2 row "Pico 2 local step at the changeover", section 3.4.2 A_kd paragraph, section 6 item 10 | The crystal temperature is the MAIN air node plus the Pico 2's own 0.03 W step. The Pico 2 is soldered flat on the main board at the sink end of the main bay, beside the LM2940 and on the same board as the feed parts (TS-012 section 8.1), whose dissipation steps with the transmit current (r_feed is the leading tornado term, 2.245 K of the 2.404 K band). Heat reaching the crystal through the board, faster than through the air node, is not stated as an assumption, and it sets the 0.047 K/s local rate and so A_kd. Same class as INSP-117 finding-17. The ceilings leave room (4.26 ppm at interval 12 against the 1 ppm allocation), so no pass or fail changes at the estimate. Fix: state the assumption and its direction, bound a board-coupled term (or make it a layout condition), and have M-2 log the ratio in the first 10 s after an over so that A_kd is measured, not only the 180 s change | Open | Pending | |
| <a id="finding-17"></a>finding-17 | reviewer | Minor | CK-ANA-H2 | `frequency-budget.md` section 5, revision 2 requests table | The revision 2 requests go to WP-PDR-23a, 32, 35, 36a, 20b, 37, 38, 43, 54 and 16b, but none to WP-PDR-18. Section 3.4.1 leaves the relock time unspecified with a design-change branch above 3.35 ms (retune at the first key sample, with a receive-restore path), and section 3.4.3 leaves the squaring stage unnamed (INSP-110 finding-25); both are schedule and design risks that close only by M-1, M-2 and the WP-PDR-20b run. Fix: send them to WP-PDR-18 as RSK-046 step evidence or as new-entry requests | Open | Pending | |

**finding-11 (the TCXO's own change is missing from the ratio drift).**
- **Defect.** Under route R3 the carrier estimate is the GPIN0 count scaled by the last XOSC/TCXO ratio. In a healthy unit the carrier is N x f_TCXO(now), so the scaled estimate differs from the set frequency by [f_TCXO(now) / f_TCXO(refresh)] x [f_XOSC(refresh) / f_XOSC(now)] - 1. Revision 1 could drop the TCXO factor because the ratio was at most about 1 s old. Revision 2 ages the ratio over a whole over, and the note budgets only the XOSC factor. Two TCXO terms are missing:
  - **The TCXO's temperature change since the refresh.** The TG2520SMN sits on the Adafruit breakout in the main bay: the RF board list of TS-012 section 8.1 has no synthesizer, and CLK1 reaches the RF board by coax through the bulkhead from a main-board stub (`hardware/sim/tx-pa/run_pa.py` revision 2 comment). It therefore sees about the same 4.99 K plus local rise as the XOSC. The note has no TG2520SMN slope; the only source in the corpus is the +/-0.5 ppm class (`docs/research/2m-cw-transceiver-reference-designs.md` F21, Medium; TS-007 value-of-information item 5 asks for the datasheet). Without a slope, the change over any temperature step is bounded only by the class band: up to 1.0 ppm peak to peak.
  - **The TCXO load and supply step between refresh and transmission.** Every ratio is counted with the squaring stage powered, and every check in transmission runs with it off (D-17). The stage's input is in parallel with the Si5351A XA input on the TCXO's rated load (TS-012 section 7.3, D-17: "so that the TCXO's rated load is kept with the Si5351A's XA input in parallel"). The note itself requires the unpowered input "must neither load nor rectify the TCXO", but it gives no allocation for the load pull that remains. The changeover also powers CLK0 and CLK2 down and CLK1 up on the breakout that feeds the TCXO. This is a systematic step present at every check, interval 12 included, not only on an aged ratio.
- **Effect.** The results that change are these.
  - Interval 13: the reviewer's band-only bound is 6.116 + 1.0 = 7.12 ppm before any load step, over the proposed 6.5 ppm allocation. With a 7.5 ppm allocation, d13 = 2 000 + 147.9988 x 10.0 = 3 480.0 Hz and the margin is 1 520.0 Hz, not 1 668.0 Hz. It is still inside the 17.77 ppm ceiling.
  - Interval 12: A_kd = 10 s fills 0.957 ppm of the 1 ppm allocation with XOSC terms alone, so any TCXO step above 0.043 ppm breaks the allocation that A_kd is derived from. The check still closes inside the 4.26 ppm ceiling.
  - The M-2 pass limit of 6.5 ppm measures the ratio, which includes both TCXO terms, so the budget and the acceptance test disagree.
- **Why Major.** A budget line that sets proposed values is missing (template: "an input value that sets a result is wrong or has no source"; "changes ... a proposed value"). The affected values are A_kd = 10 s, the 6.5 ppm allocation, the 1 668.0 Hz margin, the M-2 pass criterion and the C-16a interval-13 ceiling. They go to WP-PDR-35 as SW-SAFE values of a safety-critical unit and to the owner at S2. The safety conclusion does not change: both checks close inside their ceilings.
- **Fix.**
  - Add the TCXO terms to section 3.4.2 and the checker: temperature drift from a sourced TG2520SMN slope, or the class band if no slope is given, and a load and supply step allocation between the stage-on refresh and the stage-off transmission (confirmed by M-2, or by a refresh with the stage held on through the first key-down check).
  - Re-derive A_kd, or give the interval-12 check a larger allocation inside its 4.26 ppm ceiling, and re-derive the interval-13 allocation and margins.
  - Restate M-2 as a ratio-change limit that equals the new budget, and restate the WP-PDR-35 values.

**finding-12 (the FC0 interval times are rounded down and set the L_max deadline).**
- **Defect.** `r3_a5.py` takes the FC0 times from `freq_budget.py` (`FC0 = {12: 4 ms, 13: 8 ms, 15: 32 ms}`, the Table 541 rounded values), and its comment calls them "1 us scale, conservative". The count lasts 2^n x 0.98 us, which Table 582 rounds to 1 us (iteration 1 record, CK-ANA-A4). Interval 12 is therefore 4.014 ms (0.98 us) or 4.096 ms (1 us), and interval 13 is 8.03 or 8.19 ms. These times are rounded toward the limit, the defect of finding-5.
- **Why it is now Major.** In revision 1 no pass or fail changed (finding-5, Minor lien). In revision 2 the rounded time sets a proposed design constant, L_max = 2.0 ms, the SW-SYNTH deadline sent to WP-PDR-23a, 32 and 35. With the 1 us basis:
  - L_max = 10 - 2 - 4.096 - 2 = 1.904 ms (1.986 ms at 0.98 us). With the proposed t0 + 2.0 ms deadline, PA_EN comes at t0 + 8.096 ms, after TX_KEY, which leaves 1.904 ms between drive power-up and the ramp against the 2 ms the note requires. The margin sign flips (-0.096 ms).
  - RL-5 becomes 3.904 ms, not "the TS-012 revisit threshold 1 + 3 ms". A relock of 3.3 to 3.35 ms settle no longer fits with the ramp at 12 ms.
  - The M-1 branches become at most 1.254 ms and at most 3.254 ms of settle (not 1.35 and 3.35 ms). The TS-012 fallback keeps 0.308 ms between PA_EN and the ramp, not 0.5 ms. The receive refresh is 82.8 ms, not 82 ms (FR-2r, B-19).
  - `relock-sequence.png` draws the 4 and 8 ms bars.
- **Fix.**
  - Use 2^n x 1 us (or 0.98 us with its tolerance) for the FC0 times in `r3_a5.py`, and correct the comment. Fixing finding-5 in `freq_budget.py` fixes both checkers.
  - Re-derive L_max (1.9 ms), RL-5, RL-6, the M-1 branches, the U-1 times and the WP-PDR-23a request, and re-render the figure.

### Per-case results (revision 2, A5)

| Case | Condition | Governing id and limit | Result (checker output) | Margin with sign | Uncertainty | Reviewer re-check | Finding ids |
|---|---|---|---|---|---|---|---|
| RL-1, RL-7a, RL-7b | Relock time from the sources | TS-012 section 10: 1 ms allocation | not specified; TFREQ 10 us (applicability not stated), TRDY max 10 ms | not established (the source does not decide) | the source | sources re-read, same | none |
| RL-2 | C6 writes at 400 kHz | 1 ms writes and settle | 0.650 ms | +0.350 ms | SCL | hand: 260 clocks; 0.728 ms at 357.1 kHz | finding-13 |
| RL-2b, RL-2s | Writes at 256 and 100 kHz | 1 ms | 1.016 and 2.600 ms | -0.016 and -1.600 ms (reported as not holding) | SCL | hand: same | none |
| RL-4 | L max, interval 12, ramp at t0 + 10 ms | PA_EN 2 ms before the ramp | 2.000 ms | +1.000 ms over the allocation | FC0 time | 1 us basis: 1.904 ms; PA_EN margin -0.096 ms at the proposed 2.0 ms deadline | finding-12 |
| RL-5 | L max, interval 12, ramp at t0 + 12 ms | REQ-SYS-161 12 ms; REQ-SYS-160 15 ms; TS-012 threshold 4 ms | 4.000 ms | 0 against the threshold | FC0 time | 1 us basis: 3.904 ms | finding-12 |
| RL-6 | Interval 13 at the changeover | as RL-5 | 0.000 ms | none left | FC0 time | 1 us basis: -0.192 ms | finding-12 |
| FR-1 | XOSC slope, -10 to +65 C | Table 596 band | 0.924 ppm/K | n/a | AT-cut model (E, Low) | closed form 0.9243 ppm/K | none |
| FR-2 | Interval 12 on a ratio at most A_kd = 10 s old | 1 ppm allocation | 0.957 ppm | +0.043 ppm | rates (E, Low); TCXO terms absent | hand: same | finding-11, finding-16 |
| FR-2r | Ratio age in receive | at most A_kd | 1.082 s | +8.9 s | FC0 time | 1 us basis: 1.083 s | finding-12 |
| FR-4 | Drift over the longest over | 1 ppm (TS-012 condition, as worded) | 6.116 ppm | -5.116 ppm (reported: condition triggered) | thermal model band; TCXO terms absent | hand: same; with a 1.0 ppm TCXO band 7.12 ppm | finding-11 |
| FR-5, FR-6 | Drift ceilings | T = 5.0 kHz conditions | 4.256 and 17.77 ppm; allocation 6.5 ppm | +11.27 ppm at interval 13 | as FR-4 | hand: same | finding-11 |
| B-12.iv12, B-16.iv12, B-18.iv12 | Key-down check, healthy, 147.9988 MHz | REQ-SYS-182 (d < T); REQ-SYS-154 10 kHz; TC-SYS-101 | 4 518.0, 9 518.0, 7 482.0 Hz | +482.0, +482.0, +2 482.0 Hz | FC0 accuracy (C-16a); TCXO step | hand: same | finding-11 |
| B-12.iv13, B-16.iv13, B-18.iv13 | Checks during the over, aged ratio | as above | 3 332.0, 8 332.0, 8 668.0 Hz | +1 668.0, +1 668.0, +3 668.0 Hz | as above | hand: same; 7.5 ppm gives +1 520.0 Hz | finding-11, finding-15 |
| B-15 | Fault during transmission | REQ-SYS-182 100 ms | 46 ms | +54 ms | FC0 time | 1 us basis 46.4 ms (finding-5) | none |
| B-11 | GPIN0 and GPIN1 inputs | GPIN 50 MHz | 18.50 and 25.000 MHz | +31.5 and +25.0 MHz | none | hand: same | none |
| B-19 | Refresh time | 1 s refresh | 82.0 ms | +918 ms | settle allocation | 1 us basis 82.8 ms | finding-12 |
| BL-1 | Squared 25 MHz, n = 1 to 8, every receive window | REQ-SYS-034 range; IF; LO; image | no line in a window; nearest 150.000 MHz | +2 001 kHz | 2.5 ppm | hand: same | none |
| BL-2 | Stage off in transmission | 150.000 MHz spur line (spurs-ts012) | unchanged, -12.1 dBm, 3.9 dB over 25 uW | residual line, as stated | the spur plan's | read: consistent with `spurs-ts012.md` as cited | none |
| U-1 (A5) | Unlocked at key-down | REQ-SYS-154 | LOL_A read inside T_SW (RL-3, 0.098 ms); changeover 7.0 to 8.0 ms | +4.0 ms against 12 ms | FC0 time | 1 us basis 7.1 to 8.1 ms | finding-12 |
| U-2 (A5) | Unlocked during transmission | REQ-SYS-154 | open: the I2C read conflicts with C6; options (a) and (b) routed to WP-PDR-32 and 35 | not established; stated as open | option choice | read | finding-14 |

### Checklist answers for the revision 2 content (iteration 3 re-issue 1)

| Id | Answer | Evidence |
|---|---|---|
| R1 | Yes | 17 blobs equal at `7593cea`, `HEAD` `f6ac3f0` and the working tree |
| R2 | Yes | `r3_a5.py --run-id` exit 0, 23 PASS, 0 FAIL, 10 INFO, as section 7 states; `freq_budget.py` 35 PASS |
| R3 | N/A | `results.json` is a run output under no schema |
| R4 | Yes | The author summary and the note state the questions, inputs, results, margins, limitations (items 8 to 11) and the requests |
| R5 | Yes | No `TBD` in the note (0 matches); REQ-SYS-160, 161, 180 named as TBR |
| R6 | Yes | The four run PNGs and `frequency-budget.png` exist at the cited paths |
| CK-ANA-A1 | Yes | Question 5 and the revision 2 identifiers (D-12, D-17, D-18, the section 10 conditions, REQ-SYS-160, 180, INSP-110 finding-25) exist |
| CK-ANA-A2 | Yes | The design data are TS-012 revision 7 section 7.3 and 8.1, the spur plan C6 and D-17, D-18; AT RISK (A5 CRs) stated under rules C8 and C13 |
| CK-ANA-A3 | Yes | Every revision 2 input has a source and a state column; the AT-cut model and the Pico 2 step are labelled estimates (Low) |
| CK-ANA-A4 | No | Sources re-read (above). Disagreements: FC0 times (finding-12), SCL (finding-13) |
| CK-ANA-A5 | No (Minor) | Board-coupled heating at the crystal not stated (finding-16); finding-6 and finding-10 liens stand |
| CK-ANA-A6 | Yes | Consequences go as requests (section 5); the commit edits only the note and `hardware/sim/freq/` |
| CK-ANA-B1 | No | The ratio-drift model omits the TCXO factor (finding-11); the I2C and sequence models are right for their purpose |
| CK-ANA-B2 | N/A | No vendor model; the thermal model is the INSP-112 reviewed blob |
| CK-ANA-B3 | Yes | KA-R1 to KA-R3; KA-R2 reproduces C-12.iv12 |
| CK-ANA-B4 | Yes | Grid steps stated (a1 0.002 ppm/K, 501 and 301 temperature points, 1 s transient step); the slope bound matches the closed form, so the grid does not move it |
| CK-ANA-B5 | Yes | Independent checks above, including a closed-form slope bound |
| CK-ANA-B6 | Yes | Section 6 items 8 to 11 and the estimate labels; the TCXO terms are missing (finding-11) |
| CK-ANA-C1 | Yes | venv Python 3.13.5 (lock row), numpy 2.5.3, matplotlib 3.11.2 |
| CK-ANA-C2 | Yes | Developer evidence stated in the header and section 6 item 1; the thermal model import named |
| CK-ANA-C3 | Yes | One command, headless |
| CK-ANA-C4 | Yes | Re-run on the export: same exit, same output and `results.json`, byte-identical PNGs |
| CK-ANA-C5 | N/A | No TV record |
| CK-ANA-D1 | Yes | ppm to Hz at 147.9988 MHz; K, K/s, ms, us |
| CK-ANA-D2 | No (Minor) | Note and checker agree except the SCL basis against `clock-plan.md` R-4 (finding-13) and the C-16a interval-13 value (finding-15); finding-9 lien stands |
| CK-ANA-D3 | No | FC0 times rounded toward the limit (finding-12); margins are floored and bounds ceiled otherwise |
| CK-ANA-D4 | Yes | Each constant carries its source and class letter next to it |
| CK-ANA-E1 | Yes | REQ-SYS-160, 161, 180 and TS-012 section 10 quoted with ids |
| CK-ANA-E2 | Yes | Margins limit minus result, signs right at the stated inputs |
| CK-ANA-E3 | Yes | The relock condition is reported as not confirmed, not as passing; FR-4 is reported as triggered |
| CK-ANA-E4 | Yes | Every acceptance value in section 3.4 is a PASS/FAIL line; the checker exits 1 on any FAIL |
| CK-ANA-E5 | No | No requirement value changes, and the "else a CR" column is restated. But the proposed A_kd, 6.5 ppm and L_max values are not supported as written (findings 11 and 12) |
| CK-ANA-E6 | N/A | No new TPM value |
| CK-ANA-E7 | Yes | No closing credit; M-1 and M-2 named |
| CK-ANA-F1 | Yes | Every acceptance case above has a row. U-2 on A5 is analysed with two options and stated as open for WP-PDR-32 |
| CK-ANA-F2 | No (Minor) | The unlock-during-an-element case under option (b) omits LOL_A_STKY (finding-14) |
| CK-ANA-F3 | Yes | Continuous transmit from the receive steady state (heating) and from the transmit steady state (cooling), worst layout and ambient, plus the RSS band |
| CK-ANA-F4 | No (Minor) | The interval-13 FC0 ceiling is not restated (finding-15); the FR-2 margin (0.043 ppm) has its rate inputs stated |
| CK-ANA-G2-1 | No | The TCXO line is missing from the drift budget (finding-11) |
| CK-ANA-G2-2 | Yes | Totals recomputed; no difference at the stated inputs |
| CK-ANA-G2-3 | N/A | `docs/design/budgets.md` has no frequency section yet |
| CK-ANA-G2-4 | Yes | Receive (refresh), changeover and transmission |
| CK-ANA-G6-1 | Yes | XOSC time base, FC0 intervals and SCL stated (their values: findings 12, 13) |
| CK-ANA-G6-2 | Yes | Writes, settle, count, software, drive power-up and ramp summed against REQ-SYS-161 and 160 |
| CK-ANA-G6-3 | Yes | No emulation-derived time |
| CK-ANA-G6-4 | Yes | Slow relock gives a withheld element; a wrong settled frequency is caught within C-15, HZ-008 K7 named |
| CK-ANA-G7-1 | Yes | Extreme value plus the one-at-a-time RSS band, as the thermal note |
| CK-ANA-G7-2 | Yes | XOSC stability band and pushing allocated; the TCXO temperature and load terms are finding-11 |
| CK-ANA-H1 | Yes | HZ-008 K7 and C8 requests to WP-PDR-16b; `hazards.json` not edited |
| CK-ANA-H2 | No (Minor) | No WP-PDR-18 request (finding-17) |
| CK-ANA-H3 | Yes | Change history revision 2, 2026-09-29, with the reason and the INSP-056 delta named in the header |
| CK-ANA-I1 | Yes | Five renders opened with the Read tool (visual closure below) |
| CK-ANA-I2 | Yes | Labelled axes with units, limits labelled with ids, legends; values agree with the checker (the drawn FC0 bars carry finding-12) |
| CK-ANA-J1 | Yes | The checkers and the thermal model are not accredited, and the note restricts their use |
| CK-ANA-J2 | No | The SW-SAFE and SW-SYNTH values the note sets for swe-134 items h and l (A_kd, the interval-13 allocation, the L_max deadline) rest on findings 11 and 12 |
| CK-ANA-J3 | Yes | `assurance_tasks_applied` unchanged; results above |

### Visual closure (iteration 3 re-issue 1)

Five renders opened with the Read tool.
- `relock-sequence.png`: four timelines with writes, settle, count, software, the PA_EN triangle and the ramp bar. PA_EN is at 7, 8 and 10 ms (black) and at 11 ms for the fallback row (red, 1 ms before a 12 ms ramp). The lower panel is on a log axis: 0.01, 0.35, 1.35, 3.35, 2 and 10 ms, as in RL-2, RL-7a and RL-7b. Two cosmetic points: the fallback row draws the ramp at 12 ms, the RL-6 case, while TS-012's fallback puts it at 11.5 ms; and the "REQ-SYS-161 12 ms" label touches the lower axis. The count bars are 4 and 8 ms (finding-12).
- `ratio-freshness.png`: left, the MAIN-node traces for both layouts, three ambients, heating and cooling, all under the 4.99 K line (2.59 + 2.40 K). Right, the drift bound rises from 0.2 ppm to 6.12 ppm at W = 190 s, crossing 1 ppm at the A_kd = 10 s marker. The 1 ppm, 4.26 ppm, 6.5 ppm and 17.77 ppm lines are in the legend. It agrees with FR-2 to FR-6.
- `xosc-slope.png`: 125 of 15 392 admitted curves inside the +/-30 ppm band. The red curve with the largest slope touches +30 ppm near -24 C. The slope envelope lies within the +/-0.924 ppm/K lines. It agrees with FR-1 and with the reviewer's closed form.
- `r3-budget-and-buffer.png`: bars 4 518 and 9 518 Hz at interval 12, 3 332 and 8 332 Hz at interval 13, against T = 5 kHz and the 10 kHz limit. Harmonics 1 to 6 of 25 MHz are drawn against the six windows, with 150 MHz clear of the receive range. It agrees with B-12, B-16 and BL-1.
- `frequency-budget.png` (unchanged blob): its R3 interval-13 bar still shows the revision 1 value (2.5 kHz at 1 ppm). Section 3.4 governs for A5, and the note says so; no finding.

### Findings (iteration 3 re-issue 1 state)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| finding-1 to finding-4, finding-8 | reviewer | Major | as iterations 1 to 3 | as iterations 1 to 3 | Verified at iterations 2 and 3; sections 3.1 to 3.3 and the clock plan are unchanged at `7593cea` | Verified | Pending | |
| finding-5 | reviewer | Minor | CK-ANA-D3 | as iteration 1 | Lien; its defect now also sets L_max in section 3.4, raised separately as finding-12 | Open | Pending | CDR readiness declaration |
| finding-6, finding-7, finding-9, finding-10 | reviewer | Minor | as iterations 1 to 3 | as iterations 1 to 3 | Liens, not addressed (rule C1) | Open | Pending | CDR readiness declaration |
| finding-11 | reviewer | Major | CK-ANA-B1, G2-1, E5, J2 | `frequency-budget.md` section 3.4.2; `r3_a5.py` | TCXO temperature and load terms missing from the ratio drift; A_kd, 6.5 ppm, margins and the M-2 limit change | Open | Pending | |
| finding-12 | reviewer | Major | CK-ANA-D3, A4, E5 | `r3_a5.py` `T_FC0`; section 3.4.1 | FC0 times 4 and 8 ms (rounded down) set L_max = 2.0 ms; at 1 us x 2^n L_max is 1.904 ms and the PA_EN margin at the proposed deadline is -0.096 ms | Open | Pending | |
| finding-13 | reviewer | Minor | CK-ANA-A4, D2 | section 3.4.1; section 6 item 8 | SCL exactly 400 kHz against the clock-plan R-4 range of 357.1 to 396.8 kHz | Open | Pending | |
| finding-14 | reviewer | Minor | CK-ANA-F2, A3 | section 3.4.4 option (b) | LOL_A_STKY not used; changes the stated consequence of option (b) | Open | Pending | |
| finding-15 | reviewer | Minor | CK-ANA-F4, D2 | C-16a; section 6 item 4 | Interval-13 FC0 ceiling 458.5 Hz with 6.5 ppm, not restated | Open | Pending | |
| finding-16 | reviewer | Minor | CK-ANA-A5 | section 2; section 3.4.2; section 6 item 10 | Board-coupled heating at the crystal not stated or bounded; sets A_kd | Open | Pending | |
| finding-17 | reviewer | Minor | CK-ANA-H2 | section 5 | No risk request to WP-PDR-18 for the unspecified relock and the unnamed squaring stage | Open | Pending | |

### Cross items (not findings)

- **X-1.** Unchanged: CR-012 is not merged at `HEAD` `f6ac3f0`, so the `checklist` field keeps the design checklist. The item set applied is analysis template blob `0386cc6e`.
- **X-6 (software assurance).** INSP-111 returned APPROVED on the `4153acf` blobs. Plan row 20 asks for "the INSP-056 and INSP-111 deltas with the SA pair" for WP-PDR-20a. Revision 2 sets SW-SAFE and SW-SYNTH values (L_max, A_kd, the lock-gated start, LOL_A, R-FRESH-1 and 2), so the INSP-111 delta is required. It has not run. This reviewer did not apply the SA lens.
- **X-8 (iteration count).** This section is iteration 1 of the WP-PDR-20a review of new content (section 3.4 and a new checker), reviewed in full under rule C1. It is not a fourth delta on the WP-PDR-20 findings. The schema caps `iteration` at 3, so the field stays 3 and the heading reads "Iteration 3 re-issue 1". Whether the WP-PDR-20a cycle has its own three iterations before escalation (07 section 10.2) is for the lead SE to confirm.
- **X-9 (the revisit conditions).** The reviewer agrees with the readings the note gives to WP-PDR-54 for the TS-012 record. The relock condition is open and not triggered by the source read: the data sheet and AN619 were re-read, and they give no relock time. The freshness condition triggers as worded. Findings 11 and 12 change the numbers that go with both readings, but neither reading. The TS-012 fallback does not remedy a slow relock (RL-6, which is still infeasible on the 1 us basis). Under the plan section 10.6 row, the freshness trigger goes to the owner at S2 on this record once it is APPROVED (rule C10).
- **X-10 (WP-PDR-32 and 36a).** The note says 32 and 36a "can be written now". The reviewer agrees for the structure: the lock-gated start, the pins and the squaring-stage supply GPIO do not depend on findings 11 and 12. Those findings change only the numbers, L_max (1.9 ms) and A_kd. 32 and 36a may therefore be drafted on this F0 text. Under plan rule C10 and the row 20 "APPROVED by" order, they take their values from the APPROVED record.

### Verdict (iteration 3 re-issue 1)

```
VERDICT: NEEDS CHANGES
PRODUCT: docs/design/analysis/frequency-budget.md@14229c9d, hardware/sim/freq/r3_a5.py@eebcd167, hardware/sim/freq/README.md@450bbd8c, hardware/sim/freq/results/r3a5-20260929-01/{results.json@53c58eaa, checker-output.txt@c73f1e60, r3_a5.py@eebcd167, relock-sequence.png@f9dac5c8, ratio-freshness.png@0a86c27e, xosc-slope.png@ff5d30b3, r3-budget-and-buffer.png@c0493e76}, hardware/sim/thermal/thermal_model.py@54573514 (imported), hardware/sim/freq/freq_budget.py@d82269e6 and docs/reviews/PDR/figures/frequency-budget.png@d77a0b3a (unchanged) at 7593cea
FINDINGS:
- [Major] finding-11 CK-ANA-B1/G2-1/E5/J2: the ratio drift omits the TCXO's own temperature change (up to 1.0 ppm on the +/-0.5 ppm class band, no slope sourced) and the TCXO load and supply step between the stage-on refresh and stage-off transmission; the 6.5 ppm allocation (bound 7.12 ppm or more), A_kd = 10 s, the 1 668.0 Hz margin and the M-2 limit change. Both checks still close inside their 4.26 and 17.77 ppm ceilings.
- [Major] finding-12 CK-ANA-D3/A4/E5: the FC0 times are the Table 541 rounded 4 and 8 ms, labelled "1 us scale, conservative"; at 2^n x 1 us, L_max = 1.904 ms, not 2.0 ms (PA_EN margin -0.096 ms at the proposed deadline); RL-5 3.904 ms; M-1 branches 1.254 and 3.254 ms; fallback 0.308 ms.
- [Minor] finding-13: SCL exactly 400 kHz against clock-plan R-4 (357.1 to 396.8 kHz): writes 0.655 to 0.728 ms.
- [Minor] finding-14: AN619 LOL_A_STKY not used in U-2 option (b).
- [Minor] finding-15: interval-13 FC0 accuracy ceiling 458.5 Hz with 6.5 ppm, not restated.
- [Minor] finding-16: board-coupled heating at the Pico 2 crystal not stated or bounded (sets A_kd).
- [Minor] finding-17: no WP-PDR-18 risk request.
- [Minor] finding-5, 6, 7, 9, 10: liens, not re-checked (rule C1).
ITEMS N/A: R3; CK-ANA-B2, C5, E6, G2-3; G1, G3, G4, G5.
VALUES PROPOSED: REQ-SYS-154 and REQ-SYS-182 for A5, 10 kHz, 100 ms, T = 5.0 kHz on route R3 (supported for the values themselves, with both checks inside their ceilings; the A5 conditions A_kd 10 s, 6.5 ppm and L_max 2.0 ms are not supported as written: findings 11 and 12); REQ-SYS-154 unlocked during transmission on A5 (open on the WP-PDR-32 U-2 choice, finding-14). Other values as iteration 3.
SA PAIR: INSP-111 delta on 7593cea required (plan row 20); not yet run.
MEASUREMENTS: size=33 r3_a5.py cases (23 PASS, 10 INFO), 4 new plots; inputs_checked=21; renders=5; turns=45; minutes=90; major=2 new (open); minor=5 new (open)
```

Next: the author fixes finding-11 and finding-12, and at their option the Minor findings 13 to 17 (rule C1 allows Minor fixes before the first APPROVED verdict of this cycle). The author then re-freezes, and the next iteration is a delta on the two Major findings. The lead SE dispatches the INSP-111 delta. Under rule C10, no revision 2 value goes to the owner before this record and its SA pair are APPROVED.

## Measurements (SWE-089), iteration 3 re-issue 1

Items checked 51 applicable for the revision 2 content (readiness 5, A 6, B 5, C 4, D 4, E 6, F 4, G 9, H 3, I 2, J 3; N/A items excluded); items answered No 11 (A4, A5, B1, D2, D3, E5, F2, F4, G2-1, H2, J2); findings 2 Major, 5 Minor new (open); fixed 0; deferred 0; inputs checked against sources 21 (data sheet 7, AN619 3, requirements 3, TS-012 and plan 5, checker constants 3); renders inspected 5; effort about 45 turns and 90 minutes.

## Author response to iteration 3 re-issue 1 (WP-PDR-20a revision 3, 2026-09-29)

Written by the WP-PDR-20a author invocation (not a reviewer). It records the fixes for the reviewer's verification; it changes no verdict, finding state or front-matter field of this record. Under rule C1 only the Major findings are fixed. The Minor findings 13 to 17 and the liens 5, 6, 7, 9 and 10 are not addressed.

**Re-freeze F0 (rule C2): commit `9dc9d63`.** Product blobs at `9dc9d63`: `frequency-budget.md` revision 3 `def3f708`; `r3_a5.py` `e4140a3d`; `hardware/sim/freq/README.md` `39ae3a3b`; the new run `r3a5-20260929-02`: `results.json` `920eddb5`, `checker-output.txt` `76181155`, the script copy `e4140a3d`, `relock-sequence.png` `54cad129`, `ratio-freshness.png` `a88ebc4b`, `xosc-slope.png` `ff5d30b3` (unchanged content), `r3-budget-and-buffer.png` `01d10aac`, `settle-and-guard.png` `a141b33e` (new, for INSP-111 finding-7). Unchanged: `freq_budget.py` `d82269e6`, `frequency-budget.png` `d77a0b3a`, `thermal_model.py` `54573514`, the clock-plan files. The run `r3a5-20260929-01` is kept as the revision 2 record. Reproduce: `.venv/bin/python hardware/sim/freq/r3_a5.py --run-id r3a5-20260929-02`, exit 0, "RESULT: 38 pass, 0 fail, 14 info"; `freq_budget.py` still 35 PASS.

| Finding | Fix (where) | New values |
|---|---|---|
| finding-11 (Major) | TCXO terms added to the ratio drift: note section 2 (three revision 3 rows), section 3.4.2 (drift bound, table, readings, split table, B-16a, A_kd, M-2), 3.4.3 (load and supply conditions), finding 3.4, sections 4, 5 (WP-PDR-20b, 32, 35, 37 and 38, 43, 54), 6 items 12, 13; checker `TCXO_*` constants, FR-T, FR-2, FR-4, FR-6, FR-7, B-16a, `ratio-freshness.png`. Source read: Seiko Epson TG2520SMN brief sheet ((c) 2025, PDF SHA-256 `df16ac04...7d846612`, web-fetch tool, pdftotext in the scratchpad): fo-TC version C +/-0.5 ppm over -40 to +85 C with **no slope**; fo-Load +/-0.1 ppm at 10 kOhm // 10 pF +/-10 %; fo-VCC +/-0.1 ppm at VCC +/-5 % | TCXO temperature 1.0 ppm (the band, at any ratio age); step 0.4 ppm (2 x 0.1 + 2 x 0.1, conditions on the stage and its supply). Interval 12: allocation **2.5 ppm** (bound at A_kd 2.358 ppm), A_kd **10 s kept** (limit 11.8 s), d 4 740.0 Hz, margin **260.0 Hz**, injection margin 2 260.0 Hz. Interval 13: bound 7.516 ppm, allocation **8.0 ppm**, d 3 554.0 Hz, margin **1 446.0 Hz**, injection margin 3 446.0 Hz. Ceilings 4.256 and 17.77 ppm unchanged. FC0 accuracy ceilings for A5 532.5 Hz (interval 12) and 430.7 Hz (interval 13), stated because this fix changes them. M-2(a): ratio change at most 7.4 ppm over the over and 1.9 ppm in the first 10 s; M-2(b): TCXO step at most 0.4 ppm, pushing at most 0.2 ppm, measured on the carrier |
| finding-12 (Major) | `T_FC0 = 2^n x 1 us` in the checker, comment corrected (KA-R3); note section 2 FC0 row, 3.4 intro, 3.4.1 (L table, readings, design response item 1, M-1 ladder), 3.4.2 (FR-2r, R-FRESH-2), 3.4.3 (refresh), 3.4.4 (U-1), finding 3.4, sections 4, 5 (WP-PDR-23a, 32, 35, 54); `relock-sequence.png` re-rendered on 4.096 and 8.192 ms bars, with the TS-012 fallback row at its 11.5 ms ramp. `freq_budget.py` keeps its rounded times (finding-5 lien, not re-opened) | L_max **1.9 ms** (RL-4 1.904 ms rounded down; RL-4d: PA_EN at t0 + 7.996 ms; 2.0 ms would give t0 + 8.096 ms). RL-5 3.904 ms, 0.096 ms below the TS-012 threshold (request to WP-PDR-54). RL-6 -0.192 ms. RL-6f fallback 0.308 ms. M-1 branches 1.25 and 3.25 ms (on the proposed 1.9 and 3.9 ms). U-1 7.096 and 7.996 ms. FR-2r 1.083 s. B-19 82.8 ms. B-15 46.4 ms |

**Cross-reference.** INSP-111 finding-7 (Major, SA pair) is fixed in the same revision: section 3.4.1 and RL-8 restated (the count bounds its own mean; ST-1 linear-tail bound 2 890.7 Hz; ST-2 slewing 2.56 us), M-1 part (c) time-resolved with a pass criterion at the ramp (ST-3), and the 5 Hz settle residual carried in section 3.1 for A5 (G-1 to G-7: upper-edge margin 70.0 Hz, REQ-TX-006 limit 820.0 Hz). Its response is in the INSP-111 record.

**Observation for the lead SE (not a fix; rule C1).** The same brief sheet gives +/-1.5 ppm frequency tolerance after reflow and +/-0.5 ppm first-year aging at 25 MHz. With the band and the two coefficients that sums to 2.7 ppm uncalibrated, against the 1.5 ppm allocation of section 3.2 (TS-007 R-M3, case C-8). The note records it as section 6 item 15 and does not re-examine section 3.2.
