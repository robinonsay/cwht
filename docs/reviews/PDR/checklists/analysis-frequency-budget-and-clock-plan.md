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
# Iteration 3 re-issue 2 (WP-PDR-20a iteration 2, 2026-09-29): the delta (rule C1) that verifies the two Major fixes
# of re-issue 1 (finding-11, finding-12) in frequency-budget.md revision 3 at its re-freeze F0 commit 9dc9d63, with
# r3_a5.py e4140a3d and run r3a5-20260929-02. Written with the Edit tool by reviewer:WP-PDR-20a-analysis-iter2.
# CR-012 is still not merged at HEAD 23e2388, so X-1 stands.
# Iteration 3 re-issue 3 (WP-PDR-20a iteration 3, 2026-09-29): the delta (rule C1) on frequency-budget.md revision 4 at
# its re-freeze F0 commit d030ce2, the fix of the one Major finding the SA pair raised (INSP-111 finding-13): new
# section 3.5 (the A5 reference budget), r3_a5.py a907344b with run r3a5-20260929-03, and the revision 4 edits to
# sections 1, 2, 3.2, 4 to 8. Written with the Edit tool by reviewer:WP-PDR-20a-analysis-iter3. CR-012 is still not
# merged at HEAD 081efb9, so X-1 stands.
id: INSP-056
checklist: peer-review-checklist-design
checklist_revision: A
checklist_file: docs/reviews/PDR/checklists/analysis-frequency-budget-and-clock-plan.md
product: docs/design/analysis/frequency-budget.md
# product_commit (iteration 3 re-issue 3): d030ce2, frequency-budget.md revision 4 (WP-PDR-20a re-freeze F0). Each
# blob below equals git rev-parse d030ce2:<path>, git rev-parse HEAD:<path> at HEAD 081efb9 and git hash-object
# <path> (34 of 34). The r3a5-20260929-02 and -01 run files are kept (the revision 3 and 2 records, unchanged).
# Re-issue 2 listed 25 blobs at 9dc9d63 (frequency-budget.md def3f708, r3_a5.py e4140a3d, README.md 39ae3a3b).
product_commit: "d030ce277699a984b973a45b35432cbd5334571c"
product_files: ["docs/design/analysis/frequency-budget.md@28c29b8aa34f0ed5efc857439355be90823f66bc", "hardware/sim/freq/r3_a5.py@a907344b2b658e5e7a56a7b3891805822ecea58b", "hardware/sim/freq/README.md@6af50391a7d144057bd1581139eae535169330f9", "hardware/sim/freq/results/r3a5-20260929-03/results.json@3cf60c629d345b247d925f8f7910377c84ac43fd", "hardware/sim/freq/results/r3a5-20260929-03/checker-output.txt@46aa41baea3080a0097f02b27dd95c73f3c9b4ec", "hardware/sim/freq/results/r3a5-20260929-03/r3_a5.py@a907344b2b658e5e7a56a7b3891805822ecea58b", "hardware/sim/freq/results/r3a5-20260929-03/reference-budget-a5.png@a16ed5d15aa2bee9925889ec7078e74022144177", "hardware/sim/freq/results/r3a5-20260929-03/relock-sequence.png@54cad129f28db5d9e20087fd24c04ceca7ff2fd8", "hardware/sim/freq/results/r3a5-20260929-03/ratio-freshness.png@a88ebc4bb931267b5b8ca664fbaf7bdae0e91262", "hardware/sim/freq/results/r3a5-20260929-03/xosc-slope.png@ff5d30b3ec314514aa737f349f097a02a68ff86d", "hardware/sim/freq/results/r3a5-20260929-03/r3-budget-and-buffer.png@01d10aac5b202c75204baaec0f5a6072747df24a", "hardware/sim/freq/results/r3a5-20260929-03/settle-and-guard.png@a141b33ed44a481a3ef23dd326fc536dbe75866e", "hardware/sim/freq/results/r3a5-20260929-02/results.json@920eddb5dafe4a2084cfac21321e03cf438133bf", "hardware/sim/freq/results/r3a5-20260929-02/checker-output.txt@76181155d52b0a3378d7941f087cd9cd67b48bc5", "hardware/sim/freq/results/r3a5-20260929-02/r3_a5.py@e4140a3d7629c1254afed81851db8941c1584216", "hardware/sim/freq/results/r3a5-20260929-02/relock-sequence.png@54cad129f28db5d9e20087fd24c04ceca7ff2fd8", "hardware/sim/freq/results/r3a5-20260929-02/ratio-freshness.png@a88ebc4bb931267b5b8ca664fbaf7bdae0e91262", "hardware/sim/freq/results/r3a5-20260929-02/xosc-slope.png@ff5d30b3ec314514aa737f349f097a02a68ff86d", "hardware/sim/freq/results/r3a5-20260929-02/r3-budget-and-buffer.png@01d10aac5b202c75204baaec0f5a6072747df24a", "hardware/sim/freq/results/r3a5-20260929-02/settle-and-guard.png@a141b33ed44a481a3ef23dd326fc536dbe75866e", "hardware/sim/freq/results/r3a5-20260929-01/results.json@53c58eaa1a66f7ff01adad52756d79efc5eb40f9", "hardware/sim/freq/results/r3a5-20260929-01/checker-output.txt@c73f1e60fb9d0ead825cdafbccbe5ec527795c12", "hardware/sim/freq/results/r3a5-20260929-01/r3_a5.py@eebcd167109046a0aff3cd0a238ef35470a6b155", "hardware/sim/freq/results/r3a5-20260929-01/relock-sequence.png@f9dac5c884981c38907165854f0c9ac66908e999", "hardware/sim/freq/results/r3a5-20260929-01/ratio-freshness.png@0a86c27e2cd71fd579e8055718d318f6b0122d8a", "hardware/sim/freq/results/r3a5-20260929-01/xosc-slope.png@ff5d30b3ec314514aa737f349f097a02a68ff86d", "hardware/sim/freq/results/r3a5-20260929-01/r3-budget-and-buffer.png@c0493e761f1e2571570515f88057f64184233750", "hardware/sim/thermal/thermal_model.py@54573514ad75cbae6edee930996f5fa5a745eed6", "hardware/sim/freq/freq_budget.py@d82269e6e9a7b2312d85c227d29de55236cdacc5", "docs/reviews/PDR/figures/frequency-budget.png@d77a0b3afac520643fdda042d188612b9123848e", "docs/design/analysis/clock-plan.md@07b5309613279d906bfdd3549618bb39ae8c7d81", "hardware/sim/freq/clock_plan.py@7e321b3d3355d8e94b464110292c3909483d3832", "docs/reviews/PDR/figures/clock-plan-harmonics.png@0a4d221c1c1690aa28331d0c429e65278feacb07", "docs/decisions/adr/ADR-031-clock-plan.md@58ceb119651feeadfc79a4c3d61ecfa916fa52d4"]
analysis_kind: [budget, timing, worst-case, other]
product_size: 2 notes and 1 ADR; 39 checker cases (35 PASS, 4 INFO) and 30 clock rows (5 named residual sources, 1 seeded case) in 6 IF plans; revision 2 adds 33 r3_a5.py cases (23 PASS, 10 INFO); revision 3: 52 r3_a5.py cases (38 PASS, 14 INFO); revision 4: 67 r3_a5.py cases (43 PASS, 24 INFO); 3 checkers; 8 plots
tools_used: ["venv Python 3.13.5 (TV-001 accredits the interpreter; no TV record covers hardware/sim/freq/*.py, developer evidence per 05 section 9.1)", "numpy 2.5.3 and matplotlib 3.11.2 in the venv (r3_a5.py; no TV record, developer evidence)", "hardware/sim/thermal/thermal_model.py@54573514 (INSP-112 reviewed model, no TV record, developer evidence)"]
values_proposed: ["REQ-SYS-008: 144.0012 to 147.9988 MHz; for A5 (revision 4) open on the section 3.5 option (option (b): 1.4 or 1.5 kHz guard)", "REQ-SYS-009: 144.0012 to 147.9988 MHz; for A5 open as REQ-SYS-008", "REQ-TX-002: 144.0012 to 147.9988 MHz; for A5 open as REQ-SYS-008", "REQ-SYS-010: +/-2.5 ppm, -10 to +45 C, one year after calibration; for A5 (revision 4) 2.034 ppm after a correct calibration with a range of at least +/-1.5 ppm, else-a-CR open on the section 3.5 option", "REQ-SYS-154: 10 kHz true-error limit, measured SW-SAFE threshold 5.0 kHz (route R3), lock-detect primary for the unlocked trigger; A5 (revision 3): Si5351A LOL_A, lock-gated changeover with L_max 1.9 ms, ratio age at most 10 s at interval 12 with a 2.5 ppm drift allocation, 8.0 ppm drift allocation at interval 13, TCXO load and supply conditions on the squaring stage, FC0 known-clock acceptance 532.5 Hz (interval 12) and 430.7 Hz (interval 13)", "REQ-SYS-182: 10 kHz and 100 ms (route R3; A5 conditions as REQ-SYS-154; transmit detection 46.4 ms)", "REQ-TX-013: fixed ratio 8, sample below 20 MHz, within 1 kHz", "REQ-SYS-034: 144.010 to 147.999 MHz, 3 dB above MDS", "TPM-006: cbe 0.834 / 0.984 / 1.234 ppm by class (TS-007 allocations); A5 2.034 ppm (revision 4); credit false"]
# renders_inspected (iteration 3 re-issue 3): the six run r3a5-20260929-03 PNGs (reference-budget-a5.png new; the
# other five byte-identical to r3a5-20260929-02) and frequency-budget.png, the seven renders revision 4 cites
renders_inspected: 7
sprint: PDR-prep
author_agent: "author:WP-PDR-20 wave 1a (Claude as RF designer TX); revision 2 by author:WP-PDR-20a analysis"
reviewer_agent: "reviewer:WP-PDR-20a-analysis-iter3 (independent; authored no part of WP-PDR-20 or WP-PDR-20a; iteration 3 re-issue 2 by reviewer:WP-PDR-20a-analysis-iter2; iteration 3 re-issue 1 by reviewer:WP-PDR-20a-analysis-iter1; iterations 1 to 3 by reviewer:WP-PDR-20-analysis-iter1, -iter2 and -iter3)"
# paired_record (iteration 3 re-issue 2): the software assurance pair, as INSP-111 names INSP-056 (INSP-111 X-1)
paired_record: INSP-111
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
# assurance_reviewer_agent (iteration 3 re-issue 2): INSP-111 iteration 2 (the WP-PDR-20a SA delta on 7593cea,
# commit 572ee21) returned NEEDS CHANGES with one Major (INSP-111 finding-7); its delta on the 9dc9d63 fix has not
# been filed at HEAD 23e2388
# assurance_reviewer_agent (iteration 3 re-issue 3): INSP-111 iteration 3 (f378a6a, on 9dc9d63) returned NEEDS CHANGES
# with one Major (INSP-111 finding-13). Its delta on the d030ce2 fix, INSP-111 iteration 3 re-issue 1 (93cd044),
# returned NEEDS CHANGES: finding-13 Verified, one new Major (INSP-111 finding-16, the point of finding-19 here)
assurance_reviewer_agent: "sa-reviewer:WP-PDR-20a-insp-111-delta (INSP-111 iteration 3 re-issue 1, NEEDS CHANGES at d030ce2, 93cd044; iteration 3 NEEDS CHANGES at 9dc9d63; iteration 2 NEEDS CHANGES at 7593cea); iteration 1 by sa-reviewer:WP-PDR-20-insp-056-adr-031 (APPROVED at 4153acf)"
iteration: 3
readiness_met: true
# reviewer_verdict (iteration 3 re-issue 3, WP-PDR-20a iteration 3): NEEDS CHANGES. One new Major finding (19) in the
# revision 4 content: option (c) of section 3.5 bounds later calibration entries only, not the first (factory) value,
# and is routed to the owner as keeping the band edge safe. Four new Minor findings (20 to 23) are liens (rule C1).
# This is the third iteration of the WP-PDR-20a cycle, so the lead SE escalates under rule C1 (07 section 10.2).
# Re-issue 2: APPROVED. Re-issue 1: NEEDS CHANGES
reviewer_verdict: NEEDS CHANGES
reviewer_verdict_iteration_3_reissue_2: APPROVED
reviewer_verdict_iteration_3_reissue_1: NEEDS CHANGES
# assurance_verdict: the latest committed INSP-111 verdict (iteration 3 re-issue 1 at 93cd044, NEEDS CHANGES)
assurance_verdict: NEEDS CHANGES
# verdict (iteration 3 re-issue 3): NEEDS CHANGES, by finding-19 of this record, and also held by the SA pair
# (INSP-111 not APPROVED) and X-1 (CR-012 not merged)
verdict: NEEDS CHANGES
findings_major: 8
findings_minor: 15
findings_open: 15
findings_fixed: 0
findings_verified: 8
findings_deferred: 0
assurance_tasks_applied: [swe-070 7.1 task 1, swe-134 7.1 task 1, swe-134 7.1 task 6]
deferred_rids: []
# items_no (iteration 3 re-issue 3): Major finding-19 (A5, E3, J2); Minor findings 5, 6, 7, 9, 10, 13, 14, 16, 17,
# 18, 20 to 23
items_no: [CK-ANA-A4, CK-ANA-A5, CK-ANA-D2, CK-ANA-D3, CK-ANA-E3, CK-ANA-E5, CK-ANA-F2, CK-ANA-F4, CK-ANA-H2, CK-ANA-J2]
# effort (iteration 3 re-issue 3): this delta only
effort_turns: 45
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

## Iteration 3 re-issue 2: WP-PDR-20a iteration 2, delta on finding-11 and finding-12 (Major) at 9dc9d63 (2026-09-29)

**Scope (rule C1).** A delta that verifies the two Major fixes of re-issue 1 only. The author re-froze the products at `9dc9d63` (freeze F0, rule C2): `frequency-budget.md` revision 3 `def3f708`, `r3_a5.py` `e4140a3d`, `README.md` `39ae3a3b`, and the new run `r3a5-20260929-02` (`results.json` `920eddb5`, `checker-output.txt` `76181155`, the script copy `e4140a3d`, five PNGs). Every `product_files` blob equals `git rev-parse 9dc9d63:<path>`, `git rev-parse HEAD:<path>` at `HEAD` `23e2388` and `git hash-object <path>` (25 of 25). `9dc9d63` is on `main`; the two commits after it (`a13a00e`, the author responses, and `23e2388`, INSP-034) touch no product file. Re-checked before commit at `HEAD` `abe5706`: `git diff --stat 9dc9d63 HEAD` over every product path is empty. `freq_budget.py`, `frequency-budget.png`, `thermal_model.py` and the clock-plan files are unchanged. The change was read as `git diff 7593cea 9dc9d63` on the note, the checker and the README. The same revision also carries the INSP-111 finding-7 fix (section 3.4.1 restated, the ST and G cases, M-1(c), the A5 rows of section 3.1). That fix is verified by the INSP-111 delta, not here; this delta read it only for its effect on the values this record carries (cross item X-11). The Minor findings stay liens and were not re-checked, except finding-15, whose fix is contained in the finding-11 fix (below). The re-issue 1 checklist answers stand except where this section changes them.

**Independence (rule C4).** This invocation authored no part of WP-PDR-20 or WP-PDR-20a (TS-007, TS-012, either note, ADR-031, any checker, figure or run, either author response) and wrote no earlier iteration of this record, of INSP-111 or of INSP-118. It edited no product file.

**Search first (charter section 11 rule 1; plan rule C3).** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran first (query: the WP-PDR-20a frequency budget review record and author response). Only `git log`, `git show`, `git diff`, `git rev-parse` and `sed -n` or `grep -n` on known files followed. `/Users/robinonsay/rust/rustos` was not read, in either the working tree or its objects; the FC0 facts are those of the iteration 1 record (Tables 541 and 582).

**Sources re-read (CK-ANA-A4).** Both PDFs were fetched with the web-fetch tool, which saved them outside the repository, and converted with `pdftotext -layout` in the scratchpad; nothing was added to the repository.
- Seiko Epson "TCXO / VC-TCXO TG2016SMN / TG2520SMN" brief sheet: SHA-256 `df16ac04cdec1db7eedcb21ef19c0a87f17dcf061fe55e1aafa053037d846612`, equal to the checker's `SOURCES["TCXO"]`. "Specifications (characteristics)": fo-TC "C: +/-0.5 x 10-6 Max. / -40 C to +85 C", "Standard stability version"; fo-Load "+/-0.1 x 10-6 Max.", "10 kOhm // 10 pF +/- 10 %"; fo-VCC "+/-0.1 x 10-6 Max.", "VCC +/- 5 %"; output load 10 kOhm and 10 pF with a 0.01 uF DC cut; f_tol +/-1.5 ppm after reflow at +25 C; f_age +/-0.5 ppm first year at 24 to 40 MHz; the note "Please contact us for requirements not listed". No slope, curve or dF/dT row anywhere in the text. Every value the note and the checker take agrees, and so do the section 6 item 15 values.
- Skyworks Si5351A/B/C-B data sheet Rev. 1.3: SHA-256 `f3bc5285...a4851101f`, equal to the checker's. Read for the TCXO load condition only: section 4.1.1 "The total internal XTAL load capacitance (CL) can be selected to be 0, 6, 8, or 10 pF" (Table 8 note 1, "register 183 bits 7:6"); section 6.6 "The Si5351 can be driven with a clock signal through the XA input pin", drawn with VIN = 1 Vpp through 0.1 uF and XB floating. No XA input capacitance or resistance is given for a driven XA (finding-18).

**Acceptance criteria for the delta (rule C7).** These are the cases the two fix clauses of re-issue 1 list:
- finding-11: the TCXO temperature term from a sourced slope, or the class band if none is given; a load and supply step allocation between the stage-on refresh and the stage-off check, present at every check; A_kd, or the interval-12 allocation inside its 4.26 ppm ceiling, re-derived; the interval-13 allocation and its margins re-derived; M-2 restated as limits that equal the budget; the WP-PDR-35 values restated. Both checks (interval 12 at key-down, interval 13 during the over), with REQ-SYS-154 (T + d <= 10 kHz), REQ-SYS-182 (d < T) and the TC-SYS-101 12 kHz injection at each.
- finding-12: FC0 times 2^n x 1 us (or 0.98 us with its tolerance) in `r3_a5.py` with the comment corrected; L_max, RL-5, RL-6, the M-1 branches, the U-1 times and the WP-PDR-23a request re-derived; the figure re-rendered. Every place in section 3.4, 4 and 5 that uses an FC0 time.

### Verification of the Major findings

**finding-11 (the TCXO's own change missing from the ratio drift): Verified.**

| Element of the fix | Result | Evidence |
|---|---|---|
| TCXO temperature term | Yes | `TCXO_TEMP_PPM = 2 x 0.5 = 1.0 ppm`, the fo-TC band peak to peak, at every ratio age, interval 12 included (FR-T; note section 3.4.2 drift list and table; section 6 item 12). The brief sheet gives no slope (re-read above), so the band is the only sourced bound. It holds whether the band is referred to +25 C or to its midpoint: in both readings two temperatures differ by at most 1.0 ppm |
| Load and supply step | Yes | `TCXO_STEP_PPM = 2 x 0.1 + 2 x 0.1 = 0.4 ppm` (FR-T). If each state is inside the rated load and supply range, each is within 0.1 ppm of the nominal-condition frequency per cause, so the step is at most twice each coefficient: correct. It is labelled an allocation, applied at every check, conditioned on the load and supply ranges in both stage states and both breakout clock states (section 3.4.3 revision 3 condition; requests to WP-PDR-20b, 37 and 38), with "a stage that pulls the load outside ... re-opens section 3.4.2" (section 6 item 13). The condition has an unnamed input (finding-18, Minor) |
| Ratio-error model | Yes | Section 3.4.2 now states the estimate error [f_TCXO(now) / f_TCXO(refresh)] x [f_XOSC(refresh) / f_XOSC(now)] - 1, the re-issue 1 form. The checker adds the TCXO terms to the XOSC terms as absolute values, which bounds the product to first order |
| Interval 12 re-derived | Yes | Allocation 2.5 ppm = the 2.357 ppm bound at A_kd 10 s rounded up to 0.5 ppm, inside the 4.256 ppm ceiling (FR-2). Reviewer: 0.924 x 0.08193 K/s x 10 s + 0.2 = 0.957 ppm, + 1.4 = 2.357 ppm; A_kd limit (2.5 - 1.4 - 0.2) / (0.924 x 0.08193) = 11.89 s, printed floored as 11.8 s; d12 = 8 x 500 + 147.9988 x (2.5 + 2.5) = 4 740.0 Hz; margins 260.0 Hz to T, 260.0 Hz to 10 kHz (T + d = 9 740.0 Hz), 2 260.0 Hz for the injection (12 000 - 4 740 - 5 000). All equal B-12, B-16 and B-18.iv12 and `results.json` |
| Interval 13 re-derived | Yes | Bound 6.116 + 1.4 = 7.516 ppm, allocation 8.0 ppm, inside 17.77 ppm (FR-4, FR-6). Reviewer: d13 = 8 x 250 + 147.9988 x (2.5 + 8.0) = 3 554.0 Hz; margins 1 446.0, 1 446.0 and 3 446.0 Hz. All equal B-12, B-16 and B-18.iv13 |
| FC0 accuracy ceilings | Yes | B-16a: (5 000 - 740.0) / 8 = 532.5 Hz at interval 12 and (5 000 - 1 554.0) / 8 = 430.7 Hz at interval 13 (reviewer), against Table 541 500 and 250 Hz. They replace the C-16a values for A5 as the WP-SW-14 known-clock acceptance limits (section 3.4.2, section 5 rows WP-PDR-32 and 43, section 6 item 4, the section 3.4.1 fallback text). The interval-12 limit is now 32.5 Hz above the Table 541 value; the note states it beside item 4 (the semantics of the Table 541 accuracy), which is where its sensitivity belongs |
| M-2 limits equal the budget | Yes | FR-7: M-2(a) ratio change at most 8.0 - 0.2 - 0.4 = 7.4 ppm over the over and 2.5 - 0.6 = 1.9 ppm in the first 10 s after it; M-2(b) TCXO step at most 0.4 ppm and pushing at most 0.2 ppm, measured on the carrier. The split is right: the ratio is counted in receive with the stage on, so it sees the XOSC thermal drift and the TCXO temperature change, and not the pushing or the step. Reviewer: the budget's ratio-change bounds are 5.916 + 1.0 = 6.916 ppm (inside 7.4) and 0.757 + 1.0 = 1.757 ppm (inside 1.9), so a unit that meets the analysis passes, and a unit that passes both parts is inside both allocations |
| Requests restated | Yes | WP-PDR-35: allocations 2.5 and 8.0 ppm with the TCXO terms, L_max 1.9 ms. WP-PDR-43: M-2(a) and (b) with their limits. WP-PDR-20b, 37 and 38: the load and supply conditions. WP-PDR-54: the freshness trigger at 7.52 ppm, 1.4 ppm of it TCXO |
| Figure | Yes | `ratio-freshness.png` (visual closure below) |

The re-issue 1 statement that "both checks still close inside their ceilings" is confirmed at the new values. No requirement value changes.

**finding-12 (FC0 interval times rounded down): Verified.**

| Element of the fix | Result | Evidence |
|---|---|---|
| Time basis in the checker | Yes | `T_FC0 = {iv: 2**iv x 1 us}`, with the comment now quoting Table 582 ("0.98us * 2**interval, but let's call it 1us") and calling 1 us the upper value of the tick, which is longer and so conservative for time. KA-R3 asserts 4.096, 8.192 and 32.768 ms. No use of the rounded `fb.FC0[iv][0]` times remains in `r3_a5.py` (`grep -n "fb.FC0\|tx_detection_time"`: only the accuracy column `fb.FC0[iv][1]` is used, in B-16a and the ratio quantization). `freq_budget.py` keeps its rounded times for sections 3.1 to 3.3 (finding-5, a lien), stated in section 2 and in the checker comment |
| L_max | Yes | RL-4 1.904 ms; RL-4d proposes 1.9 ms (rounded down to 0.1 ms) with PA_EN at t0 + 7.996 ms, 0.004 ms before TX_KEY, and asserts it. A 2.0 ms deadline would put PA_EN at t0 + 8.096 ms, after TX_KEY, as re-issue 1 found. The 4 us margin is at the conservative 1 us tick; at 0.98 us the count is 82 us shorter |
| RL-5, RL-6, RL-6f | Yes | 3.904 ms, 0.096 ms below the TS-012 threshold of 1 + 3 ms, reported as a request to WP-PDR-54 (the threshold is looser than any sequence inside REQ-SYS-161 allows); RL-6 -0.192 ms; the fallback as written keeps 0.308 ms (1 + 8.192 + 2 = 11.192 ms against the 11.5 ms ramp). Reviewer: all four by hand |
| M-1 branches | Yes | 1.9 - 0.65 = 1.25 ms and 3.9 - 0.65 = 3.25 ms of settle, on the proposed (floored) deadlines, in section 3.4.1 (b) and in the WP-PDR-23a request. Taking the floored 3.9 ms rather than 3.904 ms is the conservative side |
| U-1, FR-2r, B-19, B-15 | Yes | U-1 7.096 and 7.996 ms; FR-2r 1.083 s (1 + 0.050 + 0.032768); B-19 82.8 ms; B-15 2 x 8.192 + 10 + 20 = 46.4 ms. R-FRESH-2 and the refresh text follow (82.8 ms, 83 ms) |
| Requests | Yes | WP-PDR-23a (interval 12 at 4.096 ms, L_max 1.9 ms, the 0.308 ms fallback), WP-PDR-32 (1.9 ms), WP-PDR-35 (1.9 ms after t0), WP-PDR-54 (RL-5, RL-6f, section 7.3's sequence on the 4.096 ms count) |
| Figure | Yes | `relock-sequence.png` re-rendered on the 4.096 and 8.192 ms bars (visual closure below) |

The note's section 2 row "Key-down sequence" still quotes TS-012 section 7.3 as written ("PA_EN at t0 + 7 ms"). It is a faithful quote of the design input, the checker draws that row at 7.096 ms, and the WP-PDR-54 request carries the correction to TS-012. No finding.

### Reviewer re-runs

| Command | Exit | Result |
|---|---|---|
| `git archive 9dc9d63 hardware/sim/freq hardware/sim/thermal docs/reviews/PDR/figures/frequency-budget.png` into the scratchpad; `.venv/bin/python hardware/sim/freq/r3_a5.py --run-id rev-check` (4.3 s) | 0 | "RESULT: 38 pass, 0 fail, 14 info", as section 7 states; `diff` of `checker-output.txt` against the frozen one: no difference; `results.json` equal to the frozen one after removing `run_id` |
| `git hash-object` of the five regenerated PNGs | 0 | `54cad129`, `a88ebc4b`, `ff5d30b3`, `01d10aac`, `a141b33e`: byte-identical to the frozen figures |
| `cmp results/r3a5-20260929-02/r3_a5.py hardware/sim/freq/r3_a5.py` (export) | 0 | the run copy is the checker as frozen (both `e4140a3d`) |
| `.venv/bin/python hardware/sim/freq/freq_budget.py` (same export) | 0 | "RESULT: 35 pass, 0 fail", unchanged |
| Reviewer script over `results.json` (`freshness`, `budget`, `relock`) and the hand values above | 0 | every value above agrees to the printed digit |

### Visual closure (iteration 3 re-issue 2)

Six renders opened with the Read tool.
- `relock-sequence.png`: the four timelines on the 4.096 ms (green) and 8.192 ms bars. The TS-012 row sets PA_EN at about 7.1 ms; the proposed-deadline row (L_max = 1.9 ms) at 7.996 ms, just before TX_KEY, with the ramp at 10 ms; the 12 ms row (L = 3.9 ms) at about 10 ms; the fallback row in red at 11.192 ms, 0.308 ms before its 11.5 ms ramp, as its label says. The "REQ-SYS-161 12 ms" label now sits clear of the axis (a re-issue 1 cosmetic point). The lower log panel reads 0.01, 0.35, 1.25, 3.25, 2 and 10 ms, as RL-2, RL-7a and RL-7b.
- `ratio-freshness.png`: the right panel draws the ratio drift bound (solid) from 1.6 ppm at age 0 (0.2 ppm pushing and 1.4 ppm TCXO), with the revision 2 XOSC-only bound dotted beneath it; it crosses the 2.5 ppm interval-12 allocation just right of the A_kd = 10 s marker (label "limit 11.8 s") and levels at 7.52 ppm, marked at W = 190 s, under the 8.0 ppm allocation. The 4.26 and 17.77 ppm ceilings are in the legend. The left panel is unchanged. It agrees with FR-2 to FR-6.
- `r3-budget-and-buffer.png`: bars 4 740 and 9 740 Hz at interval 12 (drift 2.5 ppm) and 3 554 and 8 554 Hz at interval 13 (drift 8.0 ppm), against T = 5 kHz and the 10 kHz limit; the right panel is unchanged. It agrees with B-12 and B-16.
- `settle-and-guard.png` (new; the INSP-111 finding-7 figure): 2 891 Hz against T = 5 000 Hz, and the A5 upper-edge stack 370.0 + 5 + 5 + 750 Hz with a 70.0 Hz margin to 148.000 MHz. It agrees with ST-1 and G-2.
- `xosc-slope.png`: same blob `ff5d30b3` as re-issue 1; unchanged content.
- `frequency-budget.png` (unchanged blob `d77a0b3a`): the sections 3.1 to 3.3 figure; section 3.4 governs for A5, as re-issue 1 recorded.

### New finding at iteration 3 re-issue 2

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-18"></a>finding-18 | reviewer (re-issue 2, while checking the finding-11 step condition) | Minor | CK-ANA-A5 | `frequency-budget.md` section 2 row "TCXO step between the stage-on refresh and the stage-off check", section 3.4.3 revision 3 condition, section 5 rows WP-PDR-20b, 32 and 35, section 6 item 13 | See the note after this table | Open | Pending | CDR readiness declaration (lien, rule C1) |

**finding-18 (the load condition has an unnamed input).**
- **Defect.** The 0.4 ppm step holds only while the TCXO's total load, "the XA input, the stage input and its bias network", stays inside 10 kOhm // 10 pF +/-10 % in both stage states. The XA part of that load is not fixed anywhere. The Si5351A's internal load capacitance on XA and XB is a register setting, "0, 6, 8, or 10 pF" (data sheet section 4.1.1; Table 8 note 1, register 183 bits 7:6), and the data sheet gives no input capacitance or resistance for a clock-driven XA (section 6.6 shows only VIN = 1 Vpp through 0.1 uF). At the 10 pF setting the internal load alone is the nominal 10 pF, so the stage input, its bias network and the traces would have only the +10 % (1 pF) left in both states. The setting is a SW-SYNTH configuration constant, and no request names it, so WP-PDR-20b cannot show the condition from the note.
- **Why Minor.** No number, margin or pass changes. The condition is stated with its re-open branch (section 6 item 13), and M-2(b) measures the step directly on the carrier with a 0.4 ppm pass limit, so a wrong load cannot pass unmeasured.
- **Fix (lien).** Name register 183 XTAL_CL as an input of the condition, and state the XA input load as "not in the source" for a driven XA. Add the setting, or the rule that it is chosen to meet the condition, to the WP-PDR-20b run (both stage states at that setting) and to the WP-PDR-32 and WP-PDR-35 requests as a SW-SYNTH constant.

### Findings (iteration 3 re-issue 2 state)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| finding-1 to finding-4, finding-8 | reviewer | Major | as iterations 1 to 3 | as iterations 1 to 3 | Verified at iterations 2 and 3; sections 3.1 to 3.3 and the clock plan are unchanged at `9dc9d63` | Verified | Pending | |
| finding-5 | reviewer | Minor | CK-ANA-D3 | as iteration 1 | Lien; `freq_budget.py` keeps the rounded times for sections 3.1 to 3.3, stated in the note; the section 3.4 part was finding-12 | Open | Pending | CDR readiness declaration |
| finding-6, finding-7, finding-9, finding-10 | reviewer | Minor | as iterations 1 to 3 | as iterations 1 to 3 | Liens, not addressed (rule C1) | Open | Pending | CDR readiness declaration |
| finding-11 | reviewer | Major | CK-ANA-B1, G2-1, E5, J2 | `frequency-budget.md` sections 2, 3.4.2, 3.4.3, 4, 5, 6 items 12 and 13; `r3_a5.py` FR-T, FR-2, FR-4, FR-6, FR-7, B-16a; `ratio-freshness.png` | TCXO band 1.0 ppm and 0.4 ppm load and supply step added from the TG2520SMN brief sheet (re-read, SHA-256 equal); allocations 2.5 and 8.0 ppm inside their ceilings; margins 260.0 and 1 446.0 Hz; M-2(a) and (b) limits equal the budget; confirmed by re-run and hand check | Verified | Pending | |
| finding-12 | reviewer | Major | CK-ANA-D3, A4, E5 | `r3_a5.py` `T_FC0`, KA-R3, RL-4d; `frequency-budget.md` sections 3.4.1 to 3.4.4, 4, 5; `relock-sequence.png` | FC0 times 2^n x 1 us; L_max 1.9 ms with PA_EN at t0 + 7.996 ms; RL-5 3.904 ms, RL-6 -0.192 ms, fallback 0.308 ms, M-1 branches 1.25 and 3.25 ms, U-1 7.096 and 7.996 ms, B-15 46.4 ms; confirmed by re-run and hand check | Verified | Pending | |
| finding-13 | reviewer | Minor | CK-ANA-A4, D2 | section 3.4.1; section 6 item 8 | Lien, not addressed | Open | Pending | CDR readiness declaration |
| finding-14 | reviewer | Minor | CK-ANA-F2, A3 | section 3.4.4 option (b) | Lien, not addressed | Open | Pending | CDR readiness declaration |
| finding-15 | reviewer | Minor | CK-ANA-F4, D2 | section 3.4.2 B-16a; section 5 rows WP-PDR-32 and 43; section 6 item 4 | Fixed within the finding-11 fix: the interval-13 ceiling (now 430.7 Hz with the 8.0 ppm allocation) is stated and used as the A5 known-clock acceptance limit, and section 3.3 C-16a is limited to A1 and A2; re-computed | Verified | Pending | |
| finding-16 | reviewer | Minor | CK-ANA-A5 | section 2; section 3.4.2; section 6 item 10 | Lien. M-2(a) now logs the first 10 s after an over with a 1.9 ppm limit, which measures A_kd as the fix asked; the board-coupled heating assumption is still not stated or bounded | Open | Pending | CDR readiness declaration |
| finding-17 | reviewer | Minor | CK-ANA-H2 | section 5 | Lien, not addressed | Open | Pending | CDR readiness declaration |
| finding-18 | reviewer | Minor | CK-ANA-A5 | section 3.4.3 condition; section 5 rows WP-PDR-20b, 32, 35; section 6 item 13 | Si5351A register 183 XTAL_CL (0, 6, 8 or 10 pF on XA) not named as an input of the TCXO load condition; lien | Open | Pending | CDR readiness declaration |

### Checklist items changed at this iteration

| Id | Iteration 3 re-issue 2 answer | Evidence |
|---|---|---|
| CK-ANA-A4 | No (Minor) | TG2520SMN rows re-read and equal; FC0 time basis corrected (finding-12 Verified). The SCL basis of finding-13 remains |
| CK-ANA-A5 | No (Minor) | The TCXO load condition has an unnamed register input (finding-18); findings 6, 10 and 16 stand |
| CK-ANA-B1 | Yes | The ratio-drift model carries both factors (finding-11 Verified) |
| CK-ANA-B5 | Yes | Independent hand checks of FR-2, FR-4, FR-6, FR-7, B-12, B-16, B-16a, B-18, RL-4 to RL-6f, U-1, B-15, B-19 (above) |
| CK-ANA-C4 | Yes | Re-run on the `9dc9d63` export: same exit, identical output and `results.json`, byte-identical PNGs |
| CK-ANA-D2 | No (Minor) | Note and checker agree for every revision 3 value; findings 9 and 13 stand (finding-15 Verified) |
| CK-ANA-D3 | No (Minor) | `r3_a5.py` uses 2^n x 1 us (finding-12 Verified); the `freq_budget.py` rounded times of sections 3.1 to 3.3 remain the finding-5 lien |
| CK-ANA-E5 | Yes | The A5 conditions (A_kd 10 s with 2.5 ppm, 8.0 ppm, L_max 1.9 ms, the TCXO load and supply conditions) are supported as written; no requirement value changes, and the "else a CR" column stands |
| CK-ANA-F4 | No (Minor) | The interval-13 FC0 ceiling is stated (finding-15 Verified); the finding-6 lien stands |
| CK-ANA-G2-1 | Yes | The TCXO temperature and step lines are in the drift table with source and state (Datasheet, Allocation) |
| CK-ANA-G7-2 | Yes | TCXO band, load and supply terms allocated from the brief sheet |
| CK-ANA-I1, I2 | Yes | Six renders opened (visual closure above); values agree with the checker |
| CK-ANA-J2 | No (Minor) | The SW-SAFE and SW-SYNTH values (A_kd, both allocations, L_max 1.9 ms, the acceptance limits) now rest on verified fixes; the finding-7 lien (R3 TCXO-fault bound) stands |

### Cross items (not findings)

- **X-1.** Unchanged: CR-012 is not merged at `HEAD` `23e2388` (`git merge-base --is-ancestor` fails). The `checklist` field keeps the design checklist; the item set applied is analysis template blob `0386cc6e` (`git rev-parse cr/CR-012-pdr-checklist-templates:docs/templates/peer-review-checklist-analysis.md`).
- **X-6 (software assurance pair).** This record now names its pair (`paired_record: INSP-111`). INSP-111 iteration 2 (`572ee21`) returned NEEDS CHANGES on revision 2 with one Major (INSP-111 finding-7); the author's fix is in the same `9dc9d63`, and the INSP-111 delta on it has not been filed at `HEAD` `23e2388`. `assurance_verdict` therefore records NEEDS CHANGES. This reviewer did not apply the SA lens.
- **X-8 (iteration count).** This section is iteration 2 of the WP-PDR-20a cycle (the first delta). The schema caps `iteration` at 3, so the field stays 3 and the heading reads "Iteration 3 re-issue 2". It closes the cycle within its three iterations.
- **X-11 (the INSP-111 finding-7 content).** Revision 3 also adds the settle residual S_RAMP = 5 Hz to the A5 band-edge guard (section 3.1, G-1 to G-7): the upper-edge margin falls from 75.0 to 70.0 Hz and the REQ-TX-006 limit for A5 from 825.0 to 820.0 Hz, requested of WP-PDR-22. This record's REQ-SYS-008, 009 and REQ-TX-002 support is read accordingly: the reviewer checked 1 200 - 370.0 - 5 - 5 - 750 = 70.0 Hz and 1 200 - 370.0 - 10 = 820.0 Hz, and KA-R4 reproduces C-2 at S_RAMP = 0. Whether the 5 Hz allocation, the ST-1 tail bound and M-1(c) close INSP-111 finding-7 is for the INSP-111 delta.
- **X-12 (TS-012 revisit conditions, for WP-PDR-54).** The readings of re-issue 1 X-9 stand at the new numbers: relock open, not triggered by the source read; freshness triggered as worded (7.52 ppm, 1.4 ppm of it TCXO, so no ratio age meets 1 ppm). New for WP-PDR-54: the TS-012 relock threshold is 0.096 ms looser than any sequence inside REQ-SYS-161 allows (RL-5).
- **X-13 (the TG2520SMN tolerance observation).** The author's observation (section 6 item 15: 2.7 ppm uncalibrated against the 1.5 ppm allocation of section 3.2) was checked against the brief sheet and the values are right. It bears on section 3.2 and case C-8, which this delta does not review. The lead SE decides whether it re-opens the section 3.2 review.

### Verdict (iteration 3 re-issue 2)

```
VERDICT: NEEDS CHANGES (record verdict held by the SA pair and X-1; reviewer verdict APPROVED)
PRODUCT: docs/design/analysis/frequency-budget.md@def3f708, hardware/sim/freq/r3_a5.py@e4140a3d, hardware/sim/freq/README.md@39ae3a3b, hardware/sim/freq/results/r3a5-20260929-02/{results.json@920eddb5, checker-output.txt@76181155, r3_a5.py@e4140a3d, relock-sequence.png@54cad129, ratio-freshness.png@a88ebc4b, xosc-slope.png@ff5d30b3, r3-budget-and-buffer.png@01d10aac, settle-and-guard.png@a141b33e}, hardware/sim/thermal/thermal_model.py@54573514 (imported), hardware/sim/freq/freq_budget.py@d82269e6 and docs/reviews/PDR/figures/frequency-budget.png@d77a0b3a (unchanged) at 9dc9d63
FINDINGS:
- [Major] finding-11 Verified: TCXO band 1.0 ppm (no slope in the TG2520SMN brief sheet) and 0.4 ppm load and supply step added; interval 12: 2.5 ppm allocation, A_kd 10 s (limit 11.8 s), margin 260.0 Hz; interval 13: 7.516 ppm bound, 8.0 ppm allocation, margin 1 446.0 Hz; ceilings 4.26 and 17.77 ppm; acceptance limits 532.5 and 430.7 Hz; M-2(a) 7.4 and 1.9 ppm, M-2(b) 0.4 and 0.2 ppm, equal to the budget.
- [Major] finding-12 Verified: FC0 times 2^n x 1 us; L_max 1.9 ms (PA_EN at t0 + 7.996 ms); RL-5 3.904 ms; RL-6 -0.192 ms; fallback 0.308 ms; M-1 branches 1.25 and 3.25 ms; B-15 46.4 ms.
- [Major] finding-1 to finding-4 and finding-8 Verified at iterations 2 and 3; products unchanged.
- [Minor] finding-15 Verified with the finding-11 fix (interval-13 ceiling 430.7 Hz stated and used).
- [Minor] finding-18 (new): Si5351A register 183 XTAL_CL (0 to 10 pF on XA) not named as an input of the TCXO load condition; lien.
- [Minor] finding-5, 6, 7, 9, 10, 13, 14, 16, 17: liens due at the CDR readiness declaration (rule C1).
ITEMS N/A: R3; CK-ANA-B2, C5, E6, G2-3; G1, G3, G4, G5.
VALUES PROPOSED: REQ-SYS-154 and REQ-SYS-182 for A5, 10 kHz, 100 ms, T = 5.0 kHz on route R3 with L_max 1.9 ms, A_kd 10 s at 2.5 ppm, 8.0 ppm at interval 13, the TCXO load and supply conditions and the acceptance limits 532.5 and 430.7 Hz (supported); REQ-SYS-008, 009, REQ-TX-002 for A5 with the 820.0 Hz REQ-TX-006 limit (read, X-11); REQ-SYS-154 unlocked during transmission on A5 (open on the WP-PDR-32 U-2 choice, finding-14 lien). Other values as iteration 3.
SA PAIR: INSP-111 iteration 2 NEEDS CHANGES (finding-7 Major); its delta on 9dc9d63 not yet filed.
MEASUREMENTS: size=52 r3_a5.py cases (38 PASS, 14 INFO), 5 run plots; inputs_checked=9; renders=6; turns=35; minutes=60; major=2 verified, 0 open; minor=1 new (lien), 1 verified
```

The reviewer verdict is APPROVED: no Major finding is open, the re-run and the independent checks agree, and every render was opened. The record verdict stays NEEDS CHANGES for two reasons that are not findings of this record: INSP-111 has not returned APPROVED on revision 3 (07 sections 2.1.1 and 10.2), and the analysis template has not reached `main` through CR-012 (X-1). When both are met, the lead SE sets the record verdict to APPROVED in that commit, without another product iteration. Under rule C10, no revision 3 value goes to the owner before then.

## Measurements (SWE-089), iteration 3 re-issue 2

Items re-checked 14 (A4, A5, B1, B5, C4, D2, D3, E5, F4, G2-1, G7-2, I1, I2, J2); items answered No 8 (A4, A5, D2, D3, F2, F4, H2, J2, all Minor); findings 2 Major Verified, 1 Minor Verified (finding-15), 1 new Minor (finding-18, lien), 9 Minor liens carried; fixed 0; deferred 0; inputs checked against sources 9 (brief sheet 7: fo-TC, fo-Load, fo-VCC, output load, f_tol, f_age, the absence of a slope; Si5351A data sheet 2: section 4.1.1 and section 6.6); renders inspected 6; effort about 35 turns and 60 minutes.

## Iteration 3 re-issue 3: WP-PDR-20a iteration 3, delta on revision 4 (the INSP-111 finding-13 fix) at d030ce2 (2026-09-29)

**Scope (rule C1).** A delta on the one change the author made after re-issue 2: `frequency-budget.md` revision 4, which fixes the Major finding-13 of the software assurance pair (INSP-111 iteration 3, `f378a6a`). This record's own Major findings were all Verified at re-issue 2, so the delta reads the revision 4 content for the values this record carries: new section 3.5 (the A5 reference budget), the revision 4 edits to sections 1, 2, 3.2 (header note), 4 (REQ-SYS-008, REQ-SYS-010, TPM-006), 5 (the held rows and the new revision 4 rows), 6 (items 15 to 18), 7 and 8, the checker `r3_a5.py` `a907344b` (KA-R5, KA-R6, RB-0 to RB-8, `fig_reference`) and run `r3a5-20260929-03`. It was read as `git diff 9dc9d63 d030ce2` on the note, the checker and the README. The author re-froze at `d030ce2` (freeze F0, rule C2). Every `product_files` blob equals `git rev-parse d030ce2:<path>`, `git rev-parse HEAD:<path>` at `HEAD` `081efb9` and `git hash-object <path>` (34 of 34); the commits after `d030ce2` touch no product file (re-checked at `HEAD` `93cd044`: `git diff --stat d030ce2 HEAD` over every product path is empty). `freq_budget.py`, `frequency-budget.png`, `thermal_model.py` and the clock-plan files are unchanged. Whether the fix closes INSP-111 finding-13 is for the INSP-111 delta; this record judges the analysis. The Minor liens of this record were not re-checked.

**Independence (rule C4).** This invocation authored no part of WP-PDR-20 or WP-PDR-20a (TS-007, TS-012, either note, ADR-031, any checker, figure or run, any author response) and wrote no earlier iteration of this record, of INSP-111 or of INSP-118. It edited no product file. Findings 20 to 23 were found before any INSP-111 delta text on `d030ce2` was read. While checking the state of the SA pair the reviewer then read the INSP-111 front matter in the working tree (committed since as `93cd044`), which names the point of finding-19 below. The reviewer checked that point against the note and computed every number in finding-19 itself.

**Search first (charter section 11 rule 1; plan rule C3).** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran first (query: the INSP-111 WP-PDR-20a frequency budget record, finding-13 and the A5 reference budget). Only `git log`, `git show`, `git diff`, `git rev-parse`, `git archive` and `sed -n` or `grep -n` on known files followed. `/Users/robinonsay/rust/rustos` was not read.

**Sources re-read (CK-ANA-A4).** The TG2520SMN brief sheet was fetched again with the web-fetch tool (saved outside the repository) and converted with `pdftotext -layout` in the scratchpad; nothing was added to the repository. SHA-256 `df16ac04cdec1db7eedcb21ef19c0a87f17dcf061fe55e1aafa053037d846612`, equal to the checker's `SOURCES["TCXO"]`. "Specifications (characteristics)": f_tol "±1.5 × 10-6 Max." "After reflow, +25 °C"; fo-TC "C: ±0.5 × 10-6 Max. / -40 °C to +85 °C", "Standard stability version", with no reference temperature anywhere on the two pages (so the note's two readings are needed); fo-Load "±0.1 × 10-6 Max." "10 kΩ // 10 pF ± 10 %"; fo-VCC "±0.1 × 10-6 Max." "VCC ± 5 %"; f_age "±0.5 × 10-6 Max." "+25 °C, First year" for "24 MHz ≤ fo ≤ 40 MHz" (25 MHz is inside). No test condition for load or supply is given for f_tol. Every value `r3_a5.py` takes (`TG_TOL_PPM`, `TG_AGE_PPM`, `TCXO_TC_PPM`, `TCXO_LOAD_COEF_PPM`, `TCXO_VCC_COEF_PPM`) agrees. REQ-SYS-010 ("within +/-2.5 ppm (TBR) of the displayed frequency from -10 C to +45 C for one year after calibration") and REQ-SYS-008 (144.0012 to 147.9988 MHz, `tbr.plan` "else the guard is changed by CR") were read in `docs/requirements/sys/requirements.json` and agree with the note. The `freq_budget.py` constants the new cases reuse (`UNCAL_TOTAL_PPM` 1.5, `CAL_RANGE_PPM` 0.9, `U_CAL_PPM` 0.1, `E_WORD` 5 Hz, `SB60_OFFSET` 750 Hz, `TX_MAX` 147.9988 MHz) are unchanged at `d82269e6`.

**Acceptance criteria for the delta (rule C7).** The cases the fix clause of INSP-111 finding-13 lists, as they bear on this record's values: the A5 uncalibrated total on the brief-sheet terms against R-M3; identity 1 (REQ-SYS-010 after calibration) and identity 2 (the guard-protecting case) with the TG2520SMN; a constant wrong within +/-0.9 ppm and within the smallest range that corrects the tolerance; the +/-0.9 ppm range kept; each option named for the owner, with its arithmetic; the REQ-SYS-010, REQ-SYS-008, 009 and REQ-TX-002 rows and TPM-006 qualified for A5; the WP-PDR-35 and WP-PDR-16b requests held open. At the governing upper edge (147.9988 MHz), which governs for a positive reference error, on both readings of the fo-TC band.

### Review of the revision 4 content

| Element | Result | Evidence |
|---|---|---|
| TG2520SMN terms and uncalibrated total (RB-0) | Yes | 1.5 + 0.5 + 0.5 + 0.1 + 0.1 = 2.7 ppm (ref25) and 1.5 + 1.0 + 0.5 + 0.1 + 0.1 = 3.2 ppm (pp), against the 1.5 ppm R-M3 allocation: not met on either reading. The two readings are needed because the sheet states no reference temperature (re-read above), and taking pp as governing is the hazard-side choice. Absolute terms (load 0.1, supply 0.1) are used for the uncalibrated error and the 0.4 ppm step for a change between two states; that is the right split |
| Identity 1 after a correct calibration (RB-3) | Yes, with finding-20 | 0.1 + 1.0 + 0.5 + 0.4 + 0.034 = 2.034 ppm against 2.5 ppm, margin 0.466 ppm; the A5 guard keeps 144.0 Hz. The temperature term is the full 1.0 ppm band on both readings (a change between two temperatures), consistent with section 3.4.2. The smallest range is misstated (finding-20); REQ-SYS-010 holds either way |
| Identity 2 and the wrong constant (RB-1, RB-2, RB-5) | Yes | 2.734 ppm at zero range (ref25) against 2.5 ppm: identity 2 fails at every range. Edge margins, reviewer, exact fractions: RB-1 +40.4 / -33.6 Hz; RB-2 at +/-0.9 ppm -92.8 / -166.8 Hz; at +/-1.5 ppm -181.6 / -255.6 Hz; the guard tolerates at most 0.272 ppm of range (ref25) and fails with no calibration on pp. All equal the checker to the printed digit. The worst combination (largest uncalibrated error and a constant at the far end of its range, upper edge) is the one computed (CK-ANA-F3) |
| The 5.0 Hz difference from INSP-111 finding-13 | Confirmed | G-6 is (1 200 - 5 - 5 - 750) Hz / 147.9988 MHz = 2.972997 ppm: the word and settle terms are already taken off. Adding the 0.034 ppm word term to the reference error before comparing with G-6 counts 5 Hz twice. Reviewer: 3.6 ppm x 147.9988 MHz = 532.8 Hz; 532.8 + 5 + 5 + 750 = 1 292.8 Hz, 92.8 Hz beyond the 1.2 kHz guard (the finding's 97.8 Hz); 181.6 and 55.2 Hz likewise. The finding's conclusions stand at the corrected numbers |
| RB-4 (+/-0.9 ppm kept) | Yes | 0.6 + 2.034 = 2.634 ppm, over 2.5 ppm; guard margin +55.2 Hz |
| Option (a) (RB-6a) | Yes | 1.5 + 0.9 + 0.034 = 2.434 ppm (C-8 stands); edge margin +84.8 Hz |
| Option (b) (RB-6b) | Yes | Needed guard (148 MHz x e + 760 Hz) / (1 + e): 1 381.6 Hz at 4.2 ppm (ref25), 1 455.6 Hz at 4.7 ppm (pp); rounded up to 1.4 and 1.5 kHz; carrier limits 144.0015 to 147.9985 MHz. The lower edge needs less (1 364.8 Hz at 4.2 ppm). KA-R6 checks the function leaves exactly zero margin |
| Option (c) (RB-6c) | No: finding-19 (Major) | delta <= 2.972997 - 2.0 = 0.972 ppm and 10.8 Hz at delta = 0.9 ppm are right, but only for a stored factory offset that is itself right to its 0.1 ppm uncertainty. Nothing in the option bounds that first value |
| RB-7 and RB-8 | Yes | 2 x 1.5 ppm x 146 MHz + 10 Hz = 448.0 Hz, 2 x 2.0 ppm x 146 MHz + 10 Hz = 594.0 Hz; the C-10 re-read 0.934, 1.234, 1.734 ppm and 126.8 / 272.8, 214.4 / 360.4, 360.4 / 506.4 Hz. All equal the checker |
| Section 3.2 superseded for A5; section 4 and 5 rows held open | Yes, with finding-23 | The section 3.2 header note, the REQ-SYS-008 and REQ-SYS-010 rows, the revision 4 bullets, the inline "held open for A5" on the WP-PDR-16b and WP-PDR-35 revision 1 rows, and the new revision 4 rows. The REQ-SYS-009 and REQ-TX-002 cells still read "No" (finding-23) |
| TPM-006 for A5 | Yes | 2.034 ppm, `credit: false`, sent to WP-PDR-29 |
| Revision 3 content unchanged | Yes, with finding-21 | The 52 revision 3 case lines are unchanged word for word (reviewer `diff` of the two `checker-output.txt` files with the 15 new lines removed: no difference); the five revision 3 PNGs are byte-identical. One revision 3 computation did change below its printed precision (finding-21) |

### finding-19 (Major, new): option (c) does not bound the first calibration value, and is routed as keeping the band edge safe

- **Defect.** Option (c) accepts a calibration constant only within +/-delta of "the unit's factory offset, measured at unit calibration", stored with an integrity check. RB-6c then shows the guard holds for delta <= 0.972 ppm. That arithmetic takes the stored factory offset as right to its 0.1 ppm calibration uncertainty. Nothing in option (c) bounds or checks the factory value itself: section 6 item 18 says "a wrong factory measurement is outside what the integrity check can catch. It is covered only by the verified procedure", and the note names no bound, verification step or closing case for that procedure.
  - The first calibration is the same kind of act as the one finding-13 was about: a constant that is wrong but accepted. Under option (c) nothing in software limits it. If the first value is wrong within any plausibility bound B, the error at the -60 dB point is the RB-2 case at range B. Reviewer, exact fractions, at B = 1.5 ppm: 181.6 Hz (ref25) or 255.6 Hz (pp) beyond 148.000 MHz. A later entry within +/-0.9 ppm of that wrong stored value adds to it: 314.8 or 388.8 Hz beyond.
  - To keep the guard, the stored value's own error beyond 0.1 ppm and delta must together stay within 0.972 ppm. At delta = 0.9 ppm, that leaves 0.072 ppm for the first value, which no stated control provides.
- **Where it goes.** The option (c) row of the section 3.5 options table ("No requirement value CR"); RB-6c (a PASS whose text does not state its condition); section 4 (options (a) and (c) "keep 1.2 kHz"); the section 5 revision 4 rows: "Lead SE, for the owner" (text for the owner sheet: "Three ways to keep the band edge safe: ... (c) a software check that accepts a calibration value only close to the unit's stored factory measurement (within 0.97 ppm) and withholds transmission otherwise"), WP-PDR-35 (the option (c) requirement text) and WP-PDR-16b (K4 under option (c)).
- **Why Major.** The note sends option (c) to the owner, through the lead SE, as one of three equal ways to keep the band edge safe, and gives WP-PDR-35 and WP-PDR-16b its requirement and control text. As written it protects later entries and corruption only. The first calibration, which every unit has and which the owner does by hand, is left with the finding-13 failure mode at up to 255.6 Hz beyond the band on the governing reading (HZ-008 cause C7; 47 CFR 97.307(b)). A choice of (c) on this text would be made on an incomplete comparison: (c) looks like "no requirement CR, no part change", while it still needs a control on the first value that the note does not name. This is the hazard side, it is new in the revision 4 fix, and it goes to the owner and to the WP-PDR-35 writer during PDR, before the CDR due date of a lien (rule C1).
- **Fix (author; text and routing, no pin or timing change).**
  - State in the options table, RB-6c's text and section 6 item 18 that option (c) bounds entries after the first calibration only, with the numbers above.
  - Name what bounds or checks the first value under option (c), for example: the factory offset accepted only within a plausibility bound (at least the tolerance plus the load and supply terms) and confirmed by an independent second measurement against a reference before it is stored, with its own verification case. Or state the guard that an unchecked first value needs, which is the option (b) guard at range B.
  - Carry the result into the owner text, the WP-PDR-35 option (c) requirement text and the WP-PDR-16b K4 request (a procedural control, if that is the choice, named as one), and into the section 4 statement that (c) keeps 1.2 kHz.
  - The note still does not need to choose.

### New findings at iteration 3 re-issue 3 (finding-19 Major; findings 20 to 23 Minor, liens under rule C1)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-19"></a>finding-19 | reviewer (re-issue 3) | Major | CK-ANA-A5, E3, J2 | section 3.5 options table row (c) and RB-6c; section 4 revision 4 bullets; section 5 revision 4 rows (lead SE for the owner, WP-PDR-35, WP-PDR-16b); section 6 item 18 | Option (c) bounds later entries only; the first (factory) value is unbounded, and at B = 1.5 ppm the -60 dB point is 181.6 / 255.6 Hz beyond 148.000 MHz; routed to the owner as keeping the band edge safe (above) | Open | Pending | |
| <a id="finding-20"></a>finding-20 | reviewer (re-issue 3) | Minor | CK-ANA-A5, D2 | section 3.5 paragraph "After a correct calibration" and "Reading" bullet 2; `r3_a5.py` `CAL_RANGE_TOL` comment, RB-2 and RB-5 text; section 6 item 17 | See the note after this table | Open | Pending | CDR readiness declaration (lien) |
| <a id="finding-21"></a>finding-21 | reviewer (re-issue 3) | Minor | CK-ANA-D2, A6 | `r3_a5.py` `buffer_lines` (revision 4 line 459) and BL-1; `TCXO_TOL_PPM` (line 221, now unused); note section 7 revision 4 paragraph; `hardware/sim/freq/README.md` run table | See the note after this table | Open | Pending | CDR readiness declaration (lien) |
| <a id="finding-22"></a>finding-22 | reviewer (re-issue 3) | Minor | CK-ANA-D2, F2 | section 3.5 "Reading" bullet 3 ("whatever option is chosen below"); section 5 revision 4 rows WP-PDR-35 ("Under every option on the pp reading") and WP-PDR-16b ("a K4 condition under every option but (a)"); section 6 item 16 | See the note after this table | Open | Pending | CDR readiness declaration (lien) |
| <a id="finding-23"></a>finding-23 | reviewer (re-issue 3) | Minor | CK-ANA-E5, D2 | section 4 table rows REQ-SYS-009 and REQ-TX-002, column "Else a CR" | See the note after this table | Open | Pending | CDR readiness declaration (lien) |

**finding-20 (the smallest calibration range is stated for two different things).**
- **Defect.** (i) Section 3.5 says a correct calibration "needs a calibration range of at least +/-1.5 ppm, the +25 C tolerance. It is the smallest range", and `CAL_RANGE_TOL` is "the smallest calibration range that corrects the +25 C tolerance of every unit". A unit is calibrated in its own load and supply state, which the note itself counts as up to fo-Load + fo-VCC = 0.2 ppm from the nominal-condition frequency (the 0.1 + 0.1 of the uncalibrated total); the sheet gives no load or supply condition for f_tol. The range that fully corrects every unit at +25 C is therefore 1.7 ppm. (ii) RB-5 and "Reading" bullet 2 say "REQ-SYS-010 needs at least +/-1.5 ppm". REQ-SYS-010 needs only a range that leaves no more than its 0.466 ppm margin uncorrected: 1.5 - 0.466 = 1.034 ppm on the note's terms, 1.234 ppm with the 0.2 ppm.
- **Why Minor.** No conclusion changes. At a +/-1.5 ppm range a unit needing 1.7 ppm keeps 0.2 ppm: 2.234 ppm, inside 2.5 ppm. The option (b) guard is computed from the range bound, so 1 381.6 and 1 455.6 Hz stand for a +/-1.5 ppm bound; a +/-1.7 ppm bound would need 1 411.2 and 1 485.2 Hz (1.5 kHz on both readings), and the governing 1.5 kHz is unchanged. RB-4 becomes 2.834 ppm, still over. RB-5's "no fixed range meets both" holds (at least 1.034 ppm needed, at most 0.272 ppm tolerated).
- **Fix (lien).** State the full-correction range as tolerance plus load plus supply, or state that the calibration-state load and supply offset stays in the residual (2.234 ppm at +/-1.5 ppm). State REQ-SYS-010's own minimum range separately from the full-correction range. Add the load and supply offset to section 6 item 17.

**finding-21 (a revision 3 computation changed outside the fix).**
- **Defect.** Revision 4 replaced `TCXO_TOL_PPM` (2.5 ppm, "TCXO-derived line tolerance 2.5 ppm (clock-plan.md section 1)") by `TG_TOL_PPM` (1.5 ppm, the +25 C tolerance) in `buffer_lines`. BL-1 still prints "(+/-2.5 ppm)", and `TCXO_TOL_PPM` is now defined but unused. All 48 `buffer_lines` rows of `results.json` change (for example n = 1 against the receive range, 119 009.9375 to 119 009.9625 kHz; reviewer comparison of the `-02` and `-03` files). So the note's section 7 and the README ("`results.json` as revision 3, plus `reference_a5`") are not exact, and the change is outside the finding-13 fix (rule C1). The printed BL-1 line and `r3-budget-and-buffer.png` do not change because the shift is below their precision: at most 150 MHz x 1 ppm = 0.15 kHz at n = 6. For an uncalibrated TCXO line the governing tolerance is RB-0's 3.2 ppm, which neither value is.
- **Why Minor.** BL-1 passes by about 2 001 kHz at 1.5, 2.5 or 3.2 ppm (at 3.2 ppm the n = 6 line moves 0.48 kHz).
- **Fix (lien).** Use the RB-0 governing total (3.2 ppm) or restore `TCXO_TOL_PPM`, with the BL-1 label saying which; correct the section 7 and README statements.

**finding-22 (RB-1 is stated as holding under every option).**
- **Defect.** RB-1 is computed against the 1.2 kHz guard. Under option (b) the guard is 1.5 kHz (governing), and an uncalibrated TG2520SMN unit on the pp reading is inside by 1 500 - 3.2 ppm x 147.9985 MHz - 760 Hz = 266.4 Hz (166.4 Hz at 1.4 kHz). "This holds ... whatever option is chosen", "Under every option on the pp reading ...: no transmission without a valid constant" and "a K4 condition under every option but (a)" are therefore not right for option (b).
- **Why Minor.** The error is on the safe side: it asks WP-PDR-35 and WP-PDR-16b for a control that option (b) does not need. It would, however, count against (b) in the owner's comparison of the options.
- **Fix (lien).** State RB-1 against each option's guard and limit the two requests to the options that keep 1.2 kHz.

**finding-23 (two section 4 cells not qualified for A5).**
- **Defect.** The REQ-SYS-009 and REQ-TX-002 rows of the section 4 table keep "No" in the "Else a CR" column. The revision 4 bullet under the table says both are open for A5 on the same decision as REQ-SYS-008, whose cell says so. The table is the value list that goes to the owner under rule C10.
- **Why Minor.** The bullet directly below the table and the REQ-SYS-008 cell state it, so a reader of the section is not misled.
- **Fix (lien).** Add "For A5: open (section 3.5)" to the two cells.

### Reviewer re-runs

| Command | Exit | Result |
|---|---|---|
| `git archive d030ce2 hardware/sim/freq hardware/sim/thermal docs/reviews/PDR/figures/frequency-budget.png` into the scratchpad; `.venv/bin/python hardware/sim/freq/r3_a5.py --run-id rev-check` (4.6 s) | 0 | "RESULT: 43 pass, 0 fail, 24 info", as section 7 states; `diff` of `checker-output.txt` against the frozen one: no difference; `results.json` equal to the frozen one after removing `run_id` |
| `git hash-object` of the six regenerated PNGs | 0 | `54cad129`, `a88ebc4b`, `ff5d30b3`, `01d10aac`, `a141b33e`, `a16ed5d1`: byte-identical to the frozen figures |
| `cmp results/r3a5-20260929-03/r3_a5.py hardware/sim/freq/r3_a5.py` | 0 | the run copy is the checker as frozen (both `a907344b`) |
| `.venv/bin/python hardware/sim/freq/freq_budget.py` (same export) | 0 | "RESULT: 35 pass, 0 fail", unchanged |
| `diff` of the `-02` `checker-output.txt` against the `-03` one with the KA-R5, KA-R6 and RB lines removed | 0 | no difference: the 52 revision 3 lines are unchanged |
| Reviewer script, exact fractions, section 3.1 edge method with 760 Hz (word, settle residual, 750 Hz offset) | 0 | every section 3.5 value above to the printed digit; the finding-19, 20 and 22 numbers |
| Reviewer comparison of `results.json` `-02` and `-03` | 0 | only `reference_a5` (new), `checks`, `run_id` and `buffer_lines` (finding-21) differ |

### Visual closure (iteration 3 re-issue 3)

Seven renders opened with the Read tool.
- `reference-budget-a5.png` (new): left, the reference error of ten cases against the 1.5 ppm R-M3 line (dotted), the 2.5 ppm REQ-SYS-010 and identity 2 line (dashed) and the 2.972 ppm G-6 line (red), bars green where the -60 dB point is inside the band: (a) 2.400, correct calibration 2.000, clamped 2.600, no calibration 2.700 and 3.200 (red), (c) 2.900, wrong within +/-0.9 3.600 and 4.100, within +/-1.5 4.200 and 4.700 (all red). Right, the margins +84.8, +144.0, +55.2, +40.4, -33.6, +10.8, -92.8, -166.8, -181.6 and -255.6 Hz against the 148.000 MHz edge. Footer: the option (b) guards 1 381.6 and 1 455.6 Hz. Labels clear of the lines; axes labelled with units; the colour rule is stated in the panel title (the clamped case is green on the guard although it is over 2.5 ppm, as the colour rule says). It agrees with RB-1 to RB-6c. The (c) bar is drawn for a right factory offset only (finding-19).
- `relock-sequence.png`, `ratio-freshness.png`, `xosc-slope.png`, `r3-budget-and-buffer.png`, `settle-and-guard.png`: the same blobs as re-issue 2, and their content is as re-issue 2 describes (4.096 and 8.192 ms bars, PA_EN at 7.996 ms; drift bound from 1.6 ppm to 7.52 ppm under 8.0 ppm; 0.924 ppm/K; 4 740 / 9 740 and 3 554 / 8 554 Hz with the 25 MHz harmonics clear of every window; 2 891 Hz against 5 000 Hz and the 70.0 Hz margin).
- `frequency-budget.png` (unchanged blob `d77a0b3a`): sections 3.1 to 3.3; section 3.4 and now 3.5 govern for A5.
- Reviewer plot (scratchpad only, not a product file and not counted in `renders_inspected`): the edge margins behind findings 19, 20 and 22, from the reviewer script: +10.8 Hz for RB-6c with a right factory value; -181.6 / -255.6 Hz for a first value wrong within 1.5 ppm and -314.8 / -388.8 Hz with a later entry at +/-0.9 ppm on top; +266.4 / +166.4 Hz for an uncalibrated unit on pp under a 1.5 / 1.4 kHz guard; +14.8 Hz for a 1.7 ppm bound under the 1.5 kHz guard. Opened and checked against the numbers above.

### Findings (iteration 3 re-issue 3 state)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| finding-1 to finding-4, finding-8, finding-11, finding-12 | reviewer | Major | as iterations 1 to 3 re-issue 2 | as before | Verified; the content they rest on is unchanged at `d030ce2` (the 52 revision 3 lines and five figures are unchanged) | Verified | Pending | |
| finding-19 | reviewer | Major | CK-ANA-A5, E3, J2 | section 3.5 option (c), RB-6c; sections 4, 5, 6 item 18 | Option (c) leaves the first calibration value unbounded (181.6 / 255.6 Hz beyond at B = 1.5 ppm) and is routed as keeping the band edge safe | Open | Pending | |
| finding-5, 6, 7, 9, 10, 13, 14, 16, 17, 18 | reviewer | Minor | as before | as before | Liens, not addressed (rule C1) | Open | Pending | CDR readiness declaration |
| finding-15 | reviewer | Minor | CK-ANA-F4, D2 | as re-issue 2 | Verified at re-issue 2 | Verified | Pending | |
| finding-20 | reviewer | Minor | CK-ANA-A5, D2 | section 3.5; RB-2, RB-3, RB-5; section 6 item 17 | Full-correction range 1.7 ppm (load and supply of the calibration state), not 1.5; REQ-SYS-010's own minimum 1.034 to 1.234 ppm; no conclusion changes | Open | Pending | CDR readiness declaration |
| finding-21 | reviewer | Minor | CK-ANA-D2, A6 | `r3_a5.py` `buffer_lines`, BL-1; section 7; README | Line tolerance changed from 2.5 to 1.5 ppm outside the fix, label still 2.5 ppm; 48 `results.json` rows change below the printed precision | Open | Pending | CDR readiness declaration |
| finding-22 | reviewer | Minor | CK-ANA-D2, F2 | section 3.5 bullet 3; section 5 rows WP-PDR-35 and 16b; section 6 item 16 | RB-1 stated for every option; under option (b) an uncalibrated unit is 266.4 Hz inside | Open | Pending | CDR readiness declaration |
| finding-23 | reviewer | Minor | CK-ANA-E5, D2 | section 4 rows REQ-SYS-009, REQ-TX-002 | "Else a CR" cells not qualified for A5 | Open | Pending | CDR readiness declaration |

### Checklist items changed at this iteration

| Id | Iteration 3 re-issue 3 answer | Evidence |
|---|---|---|
| CK-ANA-A4 | No (Minor) | Every section 3.5 input re-read against the brief sheet and the requirements file and equal (above). The finding-13 lien (SCL basis) stands |
| CK-ANA-A5 | No (Major) | Option (c) rests on a right factory offset that nothing bounds (finding-19); the calibration-state load and supply offset is not stated (finding-20); findings 6, 10, 16, 18 stand |
| CK-ANA-B1 | Yes | Section 3.5 separates the absolute error (uncalibrated) from the change since calibration (identity 1), and both readings of the fo-TC band are carried |
| CK-ANA-B5 | Yes | Independent exact-fraction recomputation of RB-0 to RB-8, the guard function and the 5.0 Hz difference (above) |
| CK-ANA-C4 | Yes | Re-run on the `d030ce2` export: same exit, identical output and `results.json`, byte-identical PNGs |
| CK-ANA-D2 | No (Minor) | Findings 20 to 23; findings 9 and 13 stand |
| CK-ANA-E3 | No (Major) | RB-6c's 10.8 Hz margin at delta = 0.9 ppm is smaller than the uncovered error of the first value, and the consequence is not named where the option is offered (finding-19) |
| CK-ANA-E5 | No (Minor) | REQ-SYS-010 and REQ-SYS-008 are qualified for A5 and not sent as "No"; the REQ-SYS-009 and REQ-TX-002 cells are not (finding-23) |
| CK-ANA-F3 | Yes | The worst combination (largest uncalibrated error, constant at the far end of its range, upper edge) is the case computed |
| CK-ANA-G2-1, G2-2 | Yes | Section 3.5 terms table with source and state; totals recompute (2.7, 3.2, 2.034 ppm): differences none |
| CK-ANA-G7-2 | Yes | Tolerance after reflow, temperature band, first-year aging, load and supply all included |
| CK-ANA-H1 | Yes | HZ-008 cause C7 and control K4 are named and the K4 request is held open to WP-PDR-16b |
| CK-ANA-H3 | Yes | Change history row 4 names the date and the reason (INSP-111 iteration 3 finding-13) |
| CK-ANA-I1, I2 | Yes | Seven renders opened (above); values agree with the checker |
| CK-ANA-J2 | No (Major) | The SW-SYNTH calibration control offered as option (c) is not sufficient as a SWE-134 item g control on its own (finding-19); the finding-7 lien stands |

### Cross items (not findings)

- **X-1.** Unchanged: CR-012 is not merged at `HEAD` `93cd044` (`git merge-base --is-ancestor` fails). The `checklist` field keeps the design checklist; the item set applied is the analysis template blob `0386cc6e`.
- **X-6 (software assurance pair).** INSP-111 iteration 3 (`f378a6a`) returned NEEDS CHANGES with finding-13 (Major); the fix is `d030ce2` and the author response is `ac9cd1a`. The INSP-111 delta on `d030ce2`, iteration 3 re-issue 1 (`93cd044`), returned NEEDS CHANGES: finding-13 Verified, the 5.0 Hz correction confirmed, and new findings that match three here: INSP-111 finding-16 (Major) is this record's finding-19, INSP-111 finding-17 (Minor) is finding-22, INSP-111 finding-18 (Minor) is finding-21. Each pair should be fixed as one change and verified in both records. This reviewer did not apply the SA lens.
- **X-8 (iteration count).** This is iteration 3 of the WP-PDR-20a cycle of this record (re-issue 1, 2 and now 3). With finding-19 open, rule C1 (at most three iterations, 07 section 10.2) sends the next step to the lead SE for escalation to the owner. The fix is small (text and routing, no checker value changes), and the lead SE decides with the owner whether a fourth delta runs.
- **X-14 (INSP-055 closed).** `081efb9` closes the TS-007 record: TS-007 is superseded by TS-012. The section 5 revision 4 row to WP-PDR-20b sends the R-M3 result "for TS-007 and the clock plan"; for TS-007 it is now a record note only. Not a finding.

### Verdict (iteration 3 re-issue 3)

```
VERDICT: NEEDS CHANGES (reviewer verdict NEEDS CHANGES, finding-19; record verdict also held by the SA pair and X-1)
PRODUCT: docs/design/analysis/frequency-budget.md@28c29b8a, hardware/sim/freq/r3_a5.py@a907344b, hardware/sim/freq/README.md@6af50391, hardware/sim/freq/results/r3a5-20260929-03/{results.json@3cf60c62, checker-output.txt@46aa41ba, r3_a5.py@a907344b, reference-budget-a5.png@a16ed5d1, relock-sequence.png@54cad129, ratio-freshness.png@a88ebc4b, xosc-slope.png@ff5d30b3, r3-budget-and-buffer.png@01d10aac, settle-and-guard.png@a141b33e}, hardware/sim/thermal/thermal_model.py@54573514 (imported), hardware/sim/freq/freq_budget.py@d82269e6 and docs/reviews/PDR/figures/frequency-budget.png@d77a0b3a (unchanged) at d030ce2
FINDINGS:
- [Major] finding-19 (new): option (c) bounds calibration entries after the first only; the first (factory) value is unbounded, and a first value wrong within 1.5 ppm puts the -60 dB point 181.6 Hz (ref25) or 255.6 Hz (pp) beyond 148.000 MHz; routed to the owner, WP-PDR-35 and WP-PDR-16b as keeping the band edge safe.
- [Minor] finding-20 (new): full-correction range is 1.7 ppm with the calibration-state load and supply, and REQ-SYS-010 alone needs 1.034 to 1.234 ppm; no conclusion changes.
- [Minor] finding-21 (new): buffer_lines tolerance changed from 2.5 to 1.5 ppm outside the fix, label still 2.5 ppm; below the printed precision.
- [Minor] finding-22 (new): RB-1 stated for every option; under option (b) an uncalibrated unit is 266.4 Hz inside.
- [Minor] finding-23 (new): REQ-SYS-009 and REQ-TX-002 "else a CR" cells not qualified for A5.
- [Major] finding-1 to 4, 8, 11, 12 Verified; their content is unchanged.
- [Minor] finding-5, 6, 7, 9, 10, 13, 14, 16, 17, 18: liens due at the CDR readiness declaration (rule C1).
CONFIRMED FOR THE SA PAIR: the 5.0 Hz correction to INSP-111 finding-13 (92.8, 181.6 and 55.2 Hz, not 97.8, 186.6 and 50.2 Hz).
ITEMS N/A: R3; CK-ANA-B2, C5, E6, G2-3; G1, G3, G4, G5.
VALUES PROPOSED: REQ-SYS-010 for A5: 2.034 ppm after a correct calibration with a range of at least +/-1.5 ppm (supported), "else a CR" open on the section 3.5 option (supported as open); REQ-SYS-008, 009 and REQ-TX-002 for A5: open on the same option (supported as open; finding-23 for two cells); option (b) guard 1.5 kHz on the governing reading (supported); option (c) delta 0.972 ppm (supported only with a right first value, finding-19); TPM-006 A5 cbe 2.034 ppm, credit false (supported). Other values as re-issue 2.
SA PAIR: INSP-111 iteration 3 re-issue 1 (93cd044) NEEDS CHANGES: finding-13 Verified; new INSP-111 finding-16 (Major) = finding-19 here; INSP-111 findings 17 and 18 (Minor) = findings 22 and 21 here.
MEASUREMENTS: size=67 r3_a5.py cases (43 PASS, 24 INFO), 6 run plots; inputs_checked=14; renders=7; turns=45; minutes=80; major=1 new (open); minor=4 new (liens)
```

The reviewer verdict is NEEDS CHANGES on one Major finding (finding-19), which is new in the revision 4 fix. The rest of section 3.5 is sound: every number re-computes, the re-run is identical, and the finding-13 conclusions stand at the author's corrected figures. Under rule C10 no revision 4 value goes to the owner before this record and its SA pair are APPROVED. Because this is the third WP-PDR-20a iteration, the lead SE takes the next step under rule C1 (X-8).

## Measurements (SWE-089), iteration 3 re-issue 3

Items re-checked 20 (A4, A5, B1, B5, C4, D2, E3, E5, F3, G2-1, G2-2, G7-2, H1, H3, I1, I2, J2, and the D3 rounding of the new cases, which floors G-6 and rounds identities up, so D3 stays No only on the finding-5 lien); items answered No 10 (A4, A5, D2, D3, E3, E5, F2, F4, H2, J2; A5, E3 and J2 carry the Major finding-19); findings 1 Major new (open), 4 Minor new (liens), 10 Minor liens carried; fixed 0; deferred 0; inputs checked against sources 14 (brief sheet 6: f_tol, fo-TC with no reference temperature, f_age at 25 MHz, fo-Load, fo-VCC, no load or supply condition for f_tol; requirements 2: REQ-SYS-010 and REQ-SYS-008 with its `tbr.plan`; `freq_budget.py` constants 6); renders inspected 7; effort about 45 turns and 80 minutes.
