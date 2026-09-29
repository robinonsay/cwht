---
# Peer-review record front matter (charter sections 2 and 5; docs/process/01-lifecycle-and-reviews.md
# section 13 is the single field list; docs/process/07-software-engineering-plan.md sections 2.1.1, 10.2
# and 15). This is the paired software assurance record (07 section 10.2 Record row) of INSP-056
# (docs/reviews/PDR/checklists/analysis-frequency-budget-and-clock-plan.md, iteration 3, reviewer verdict
# APPROVED, committed 7209bad), which records assurance_verdict pending for "software assurance pair of
# INSP-056 for ADR-031, to be dispatched by the lead SE; 07 section 2.1.1" (its cross item X-6). Dispatch:
# 07 section 2.1.1 row "Trade studies and ADRs whose decision constrains a safety-critical or
# mission-critical component"; rules C4 and C9 of the PDR work plan.
# Checklist applied: docs/templates/peer-review-checklist-software-assurance.md revision A AS ON ITS CR-012
# BRANCH (cr/CR-012-pdr-checklist-templates at 7784672, blob 5b13528504868b2add0f0b1e329c63aa2b54cdf4; not
# merged, absent from main at 3aed3c4). tools/validate_docs.py fails a record whose `checklist` names a
# template absent from main, so the `checklist` field names peer-review-checklist-design, the checklist the
# 07 section 2.1.1 row assigns to ADRs (sections A, B, H) and the field INSP-056 carries, at its main
# revision B; `assurance_checklist` names the template actually applied (the INSP-074 form).
# id: the brief assigned no id. INSP-111 is above every id on main (HEAD 3aed3c4), on every cr/ branch and in
# the working tree (highest INSP-110). INSP-108 and INSP-109 stay free, as the INSP-110 record reserved them
# for concurrent records.
id: INSP-111
checklist: peer-review-checklist-design
checklist_revision: B
assurance_checklist: "docs/templates/peer-review-checklist-software-assurance.md@5b13528504868b2add0f0b1e329c63aa2b54cdf4 (revision A, branch cr/CR-012-pdr-checklist-templates at 7784672)"
checklist_file: docs/reviews/PDR/checklists/analysis-frequency-budget-and-clock-plan-software-assurance.md
product: docs/design/analysis/frequency-budget.md
# product_commit and product_files (iteration 2, the WP-PDR-20a delta; rule C2 freeze F0): frequency-budget.md
# revision 2 with its new checker and run, committed at 7593cea on main (plan revision 7 section 3.0 row 20: "the
# INSP-056 and INSP-111 deltas with the SA pair"). Each blob equals git rev-parse 7593cea:<path>, git rev-parse
# HEAD:<path> and git hash-object <path> at HEAD fd12ced (checked 2026-09-29); git merge-base --is-ancestor
# 7593cea main is true. freq_budget.py is unchanged (d82269e6) and is listed because r3_a5.py imports it.
# ADR-031, clock-plan.md, clock_plan.py and the two iteration 1 figures are unchanged at fd12ced and are not
# in the iteration 2 product (the clk_sys 96 MHz re-run and the ADR-031 revision of row 20 are not written yet;
# frequency-budget.md section 1 says so). Iteration 1 reviewed the seven blobs of product_files_iteration_1 at
# 4153acf, with the assurance lens on ADR-031 (INSP-056 X-6)
product_commit: "7593cea717e17fe2e542cb1cebb1d36c1fc948f6"
product_files: ["docs/design/analysis/frequency-budget.md@14229c9dfd943bc463eadab399f2bdbe8ac7f9cd", "hardware/sim/freq/r3_a5.py@eebcd167109046a0aff3cd0a238ef35470a6b155", "hardware/sim/freq/freq_budget.py@d82269e6e9a7b2312d85c227d29de55236cdacc5", "hardware/sim/freq/results/r3a5-20260929-01/results.json@53c58eaa1a66f7ff01adad52756d79efc5eb40f9", "hardware/sim/freq/results/r3a5-20260929-01/checker-output.txt@c73f1e60fb9d0ead825cdafbccbe5ec527795c12", "hardware/sim/freq/results/r3a5-20260929-01/r3_a5.py@eebcd167109046a0aff3cd0a238ef35470a6b155", "hardware/sim/freq/results/r3a5-20260929-01/relock-sequence.png@f9dac5c884981c38907165854f0c9ac66908e999", "hardware/sim/freq/results/r3a5-20260929-01/ratio-freshness.png@0a86c27e2cd71fd579e8055718d318f6b0122d8a", "hardware/sim/freq/results/r3a5-20260929-01/xosc-slope.png@ff5d30b3ec314514aa737f349f097a02a68ff86d", "hardware/sim/freq/results/r3a5-20260929-01/r3-budget-and-buffer.png@c0493e761f1e2571570515f88057f64184233750"]
product_commit_iteration_1: "4153acf1006f919fc1e6ff72715f6f2694d9dead"
product_files_iteration_1: ["docs/design/analysis/frequency-budget.md@79d47fbbcae7fbfc5dde43ebde5c6e6b20917f94", "docs/design/analysis/clock-plan.md@07b5309613279d906bfdd3549618bb39ae8c7d81", "hardware/sim/freq/freq_budget.py@d82269e6e9a7b2312d85c227d29de55236cdacc5", "hardware/sim/freq/clock_plan.py@7e321b3d3355d8e94b464110292c3909483d3832", "docs/reviews/PDR/figures/frequency-budget.png@d77a0b3afac520643fdda042d188612b9123848e", "docs/reviews/PDR/figures/clock-plan-harmonics.png@0a4d221c1c1690aa28331d0c429e65278feacb07", "docs/decisions/adr/ADR-031-clock-plan.md@58ceb119651feeadfc79a4c3d61ecfa916fa52d4"]
# inputs read at iteration 2 (not reviewed), at HEAD fd12ced
input_files_iteration_2: ["docs/plan/pdr-work-plan.md (revision 7; section 3.0 row 20, section 4.1 waiver rows 32 and 36a, rules C1 to C13)", "docs/decisions/trade-studies/TS-012-design-to-cost-hand-built.md (section 7.3 revision 6 key-down sequence and 'During the over'; section 10 revisit conditions)", "docs/reviews/PDR/checklists/ts-012-design-to-cost-software-assurance.md (INSP-118 iteration 1 item (3))", "docs/process/07-software-engineering-plan.md (sections 14.1 and 14.2, rows SW-SYNTH frequency-word path and frequency verification unit)", "docs/safety/hazards.json 0.5.0-pha (HZ-008 C7, C8)", "docs/requirements/sys/requirements.json (REQ-SYS-154 with its verification note, 160, 161, 180, 182)", "docs/design/analysis/clock-plan.md@07b53096 (section 2 row I2C SCL)", "docs/design/analysis/spurs-ts012.md (section 4.3, I2C)", "hardware/sim/thermal/thermal_model.py@54573514 (imported by the checker, unchanged)", "Skyworks Si5351A/B/C-B data sheet Rev. 1.3 (web-fetch tool, PDF SHA-256 f3bc5285...a4851101f, equal to the checker's; Table 5 and the features list, read with pdftotext in the scratchpad)", "Skyworks AN619 Rev. 0.8 (web-fetch tool, PDF SHA-256 0135b3a3...4783f36b, equal to the checker's; Register 0 bit 5 LOL_A, Register 1 LOL_A_STKY, Register 177)", "docs/references/md/swehb/ (swe-039, 065, 071, 134, 205 section 7.1)", "docs/templates/peer-review-checklist-software-assurance.md@5b135285 (git show, branch cr/CR-012)"]
# inputs read at iteration 1 (not reviewed)
input_files: ["docs/reviews/PDR/checklists/analysis-frequency-budget-and-clock-plan.md (INSP-056, iteration 3, committed 7209bad)", "docs/reviews/PDR/checklists/ts-007-synthesizer-and-reference-software-assurance.md (INSP-074)", "docs/process/07-software-engineering-plan.md (sections 2.1.1, 14.1, 14.2)", "docs/safety/hazards.json 0.5.0-pha (HZ-002, HZ-007, HZ-008)", "docs/requirements/sys/requirements.json (REQ-SYS-034, 074, 082, 088, 093, 097, 099)", "docs/process/05-configuration-and-data-management.md (Table 4-1, sections 4.5, 9.1)", "docs/decisions/adr/ADR-051-wp-sw-11-clocks.md (header)", "docs/research/power-tree-and-charging.md (F14, F15, Baseline topology)", "docs/research/audio-output-and-hearing-safety.md (F1)", "docs/plan/pdr-work-plan.md (sections 5.1, 5.3)", "rustos docs/extracted/rp2350-datasheet.md at 2ec64c0f (git show only; section 8.1.1.2, Table 605)", "docs/references/md/swehb/ (swe-022, 027, 033, 039, 052, 057, 070, 080, 081, 087, 088, 089, 134, 136, 205 section 7.1)"]
paired_record: INSP-056
product_type: trade-study-or-adr
# criticality: safety-critical. ADR-031 section 2 item 9 adds a step, with a read-back and a fault path, to the
# WP-SW-11 clocks and PLL driver, which 07 section 14.1 lists in the row "Drivers these depend on" ("clocks and
# PLL (TICKS, XOSC, PLL_SYS: every timing budget depends on them)", criteria inherited) and 07 section 14.2
# allocates a, g, j, k ("pico2 clocks and PLL (WP-SW-11)"); item 4 fixes the SPI divisor of the SW-SYNTH
# frequency-word path (07 section 14.1 row "Frequency control, transmit frequency-word path", HZ-008)
# criticality at iteration 2: safety-critical. Section 3.4 sets the key-down prerequisites and the design response
# of the frequency verification unit (SW-SAFE) and the SW-SYNTH frequency-word path, both Proposed safety-critical
# in 07 section 14.1 (HZ-008; 07 section 14.2 rows a, b, f, g, h, i, k, l for each)
criticality: safety-critical
product_size: "iteration 2: 1 analysis note revision 2 (492 lines; new section 3.4, 150 lines, 4 subsections, 2 revisit conditions, 2 measurements M-1 and M-2, 2 rules R-FRESH-1 and R-FRESH-2, 14 revision 2 requests), 1 new checker (725 lines, 33 output lines: 23 PASS, 10 INFO), 4 figures. Iteration 1: 1 ADR (164 lines; 9 decision items, 4 options, 6 assumptions), read with clock-plan.md revision 2 (186 lines, rule 11) and the checker clock_plan.py (30 clock rows, 5 residual sources, 1 seeded case)"
sprint: PDR-prep
author_agent: "author:WP-PDR-20a analysis (Claude, invocation of 2026-09-29; revision 2). Iteration 1 product: author:WP-PDR-20 wave 1a (Claude as RF designer TX)"
reviewer_agent: "sa-reviewer:WP-PDR-20a-insp-111-delta"
reviewer_agent_iteration_1: "sa-reviewer:WP-PDR-20-insp-056-adr-031"
assurance_required: true
assurance_reviewer_agent: "sa-reviewer:WP-PDR-20a-insp-111-delta (software assurance function, iteration 2; iteration 1 by sa-reviewer:WP-PDR-20-insp-056-adr-031; paired file review INSP-056, whose WP-PDR-20a delta is dispatched beside this one and is not yet filed at HEAD fd12ced)"
# iteration 2 of this record is iteration 1 of the WP-PDR-20a delta (new content, reviewed in full under rule C1);
# the rule C1 escalation count for the delta starts here
iteration: 2
# readiness_met: R1 to R3 hold at iteration 2; R4 holds for independence (this invocation is neither the
# WP-PDR-20a author nor any INSP-056 reviewer) and is pending for the filing of the INSP-056 delta, which the lead
# SE dispatched concurrently under plan row 20 (cross item X-6 of iteration 2). Iteration 1: R1 to R4 held
readiness_met: true
# reviewer_verdict and assurance_verdict at iteration 2: NEEDS CHANGES, one Major finding (finding-7) open on
# section 3.4.1. Iteration 1 (ADR-031 at 4153acf): APPROVED, zero Major, six Minor liens (rule C1)
reviewer_verdict: NEEDS CHANGES
assurance_verdict: NEEDS CHANGES
reviewer_verdict_iteration_1: APPROVED
assurance_verdict_iteration_1: APPROVED
# verdict: set by Claude as software lead (07 section 10.2). Held at NEEDS CHANGES: the product blobs are on
# main, but the checklist applied exists only on cr/CR-012-pdr-checklist-templates (lead SE convention of
# 2026-09-27), and INSP-056 does not yet name this record (paired_record, assurance_reviewer_agent,
# assurance_verdict; each reviewer updates only its own record, cross item X-1). The software lead sets
# APPROVED on both records when INSP-056 carries the pairing and CR-012 merges with the template blobs
# unchanged (INSP-056 X-1 holds for the analysis template 0386cc6e as well)
# At iteration 2 the record verdict is held at NEEDS CHANGES by finding-7 (Major) as well
verdict: NEEDS CHANGES
# findings (all iterations): finding-1 to finding-6 (iteration 1, Minor, Open liens); finding-7 (iteration 2,
# Major, Open); finding-8 to finding-12 (iteration 2, Minor, Open)
findings_major: 1
findings_minor: 11
findings_open: 12
findings_fixed: 0
findings_verified: 0
findings_deferred: 0
assurance_findings_major: 1
assurance_findings_minor: 11
assurance_tasks_applied: ["swe-134 7.1 task 5", "swe-022 7.1 task 1", "swe-033 7.1 task 1", "swe-033 7.1 task 2", "swe-033 7.1 task 3", "swe-039 7.1 task 3", "swe-039 7.1 task 4", "swe-057 7.1 task 2", "swe-134 7.1 task 1", "swe-134 7.1 task 4", "swe-134 7.1 task 6", "swe-205 7.1 task 1", "swe-205 7.1 task 3", "swe-071 7.1 task 1", "swe-136 7.1 task 1", "swe-070 7.1 task 1", "swe-080 7.1 task 1", "swe-080 7.1 task 2", "swe-081 7.1 task 2", "swe-087 7.1 task 2", "swe-089 7.1 task 1"]
assurance_tasks_applied_iteration_1: ["swe-134 7.1 task 5", "swe-022 7.1 task 1", "swe-033 7.1 task 1", "swe-033 7.1 task 2", "swe-033 7.1 task 3", "swe-039 7.1 task 4", "swe-057 7.1 task 2", "swe-134 7.1 task 4", "swe-134 7.1 task 6", "swe-136 7.1 task 1", "swe-070 7.1 task 1", "swe-205 7.1 task 3", "swe-205 7.1 task 1", "swe-134 7.1 task 1", "swe-052 7.1 task 2", "swe-080 7.1 task 1", "swe-080 7.1 task 2", "swe-081 7.1 task 2", "swe-087 7.1 task 2", "swe-088 7.1 task 1", "swe-089 7.1 task 1"]
swe134_items_checked: [b, c, e, g, h, i, j, k, l]
swe134_items_checked_iteration_1: [a, c, e, g, h, i, j, k, l]
deferred_rids: []
items_no: ["swe-033 7.1 task 2", "swe-039 7.1 task 3", "swe-057 7.1 task 2", "swe-134 7.1 task 1", "swe-134 7.1 task 6", "swe-205 7.1 task 1", "swe-205 7.1 task 3", "swe-071 7.1 task 1", "swe-080 7.1 task 1", SA-C-b, SA-C-e, SA-C-g, SA-C-h, SA-C-j, SA-D1, SA-D2, SA-D6]
items_no_iteration_1: ["swe-033 7.1 task 2", "swe-057 7.1 task 2", "swe-134 7.1 task 4", "swe-134 7.1 task 6", "swe-136 7.1 task 1", "swe-070 7.1 task 1", "swe-205 7.1 task 3", "swe-205 7.1 task 1", "swe-134 7.1 task 1", "swe-052 7.1 task 2", "swe-080 7.1 task 1", "swe-080 7.1 task 2", "swe-088 7.1 task 1", SA-A4, SA-C-e, SA-C-h, SA-C-j, SA-D1, SA-D2, SA-D6, SA-E3]
# effort: iteration 1 40 turns, 70 minutes; iteration 2 45 turns, 95 minutes
effort_turns: 85
effort_minutes: 165
date_iteration_2: 2026-09-29
record_status: Open
date: 2026-09-27
date_closed: null
---

# Peer review record INSP-111: software assurance pair of INSP-056, ADR-031 clock plan (WP-PDR-20)

**Product.** The seven `product_files` of INSP-056 iteration 3 at freeze commit `4153acf` (freeze F0, rule C2): `frequency-budget.md` `79d47fbb`, `clock-plan.md` `07b53096`, `freq_budget.py` `d82269e6`, `clock_plan.py` `7e321b3d`, `frequency-budget.png` `d77a0b3a`, `clock-plan-harmonics.png` `0a4d221c` and `docs/decisions/adr/ADR-031-clock-plan.md` `58ceb119`. Each blob is equal at `4153acf`, at `HEAD` and in the working tree (`git rev-parse`, `git hash-object`), and `4153acf` is on `main`. The assurance lens is applied to ADR-031, the product that routes this pair (INSP-056 cross item X-6); `clock-plan.md` revision 2 (rule 11 and the section 5 requests) and the checker are read where ADR-031 rests on them. The frequency-budget values were reviewed by INSP-056 and by the TS-007 pair INSP-074, and are not reviewed again here. **Paired record:** INSP-056, reviewer verdict APPROVED at iteration 3 (five Major findings Verified, five Minor liens), record verdict held for this pair and for CR-012.

**Checklist.** `docs/templates/peer-review-checklist-software-assurance.md` revision A as on its CR-012 branch (`7784672`, blob `5b135285`): readiness R1 to R4, sections A to F, the section B row `trade-study-or-adr` plus the row "Every product type", and the section 7.1 tasks of the other SWEs ADR-031 touches. It is branch-only; see the front matter for the `checklist` field.

**Acceptance criteria (rule C7).**
- Every task of the section B rows `trade-study-or-adr` and "Every product type" is in the task table, including the conditional swe-136 and swe-070 rows, because ADR-031 section 4.3 selects `clock_plan.py` as the tool of a verification case.
- The section 7.1 tasks of every other SWE the ADR touches: SWE-205 (it moves part of HZ-008 K6 into firmware), SWE-134 task 1 (item 9 is a design step of a safety-critical driver), SWE-052 (derived software requirements of a hazard control), SWE-080 and SWE-081 (change route of the product), SWE-087, SWE-088 and SWE-089 (the paired review).
- Every SWE-134 item that 07 section 14.2 allocates to the WP-SW-11 driver (a, g, j, k), plus c, e, h, i and l, because item 9 adds a register write whose premature issue locks the chip (RP2350 Table 605). Each is checked at ADR maturity: the decision neither precludes nor weakens the provision.
- Every safety-critical component outside WP-SW-11 on which an ADR-031 rule or constant acts: `SW-SYNTH` (SPI divisor 8), `SW-PWR` and `SW-AUDIO` (the R-4 I2C traffic rule, the R-2 GPIO23 mode, the PWM TOP).
- HZ-008 K6 (the control ADR-031 implements) walked by action, inaction and incorrect action (SWEHB `swe-205` 7.1 task 1).

**Independence (rule C4).** This invocation authored no part of WP-PDR-20 (TS-007, the frequency budget, the clock plan, ADR-031, the checkers, the figures) and wrote no iteration of INSP-055, INSP-056 or INSP-074. It is neither the author nor any of the three file reviewers of INSP-056. It edited no product file.

**Search first (charter section 11 rule 1).** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search. Queries: the software assurance template and paired-record fields; 07 section 14.1 and the WP-SW-11 SWE-134 row; HZ-008 K6; ADR-051 bring-up and poll budget; BQ25887 I2C reads in battery supervision; DORMANT or SLEEP use in cwht; audio PWM TOP and the level cap. On `/Users/robinonsay/rust/rustos`: the ROSC CTRL ENABLE field. The one datasheet passage quoted below was re-read from the committed object `git show 2ec64c0f:docs/extracted/rp2350-datasheet.md`; the rustos working tree was not read. Before the search tool was loaded, one `wc -l` of known paths and one `git status` and `git log` ran (no search). `grep -n`, `awk` and a Python walk of `hazards.json` and `requirements.json` were used afterwards only to pin lines, SWEHB section 7.1 task lists and field values.

## Findings (iteration 1)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | assurance | Minor | `swe-057 7.1 task 2`, `swe-134 7.1 task 4`, `swe-080 7.1 task 1`, SA-C-j | ADR-031 section 2 item 8 (R-2, R-4), item 4 (audio and sidetone PWM); section 4.3 ("Safety-critical software scope changed: no. ... Item 9 adds one step to it") | See the note after this table | Open | Pending | CDR readiness declaration (lien, rule C1) |
| <a id="finding-2"></a>finding-2 | assurance | Minor | `swe-205 7.1 task 1`, `swe-205 7.1 task 3`, `swe-134 7.1 task 6`, `swe-052 7.1 task 2`, `swe-033 7.1 task 2`, SA-D1, SA-D2, SA-D6 | ADR-031 sections 4.1 (the four "new, derived" SW rows) and 4.3 ("Hazard analysis update required: yes. The HZ-008 K6 text gets items 2, 3, 5, 6, 8 and 9"); `hazards.json` 0.5.0-pha HZ-008 K6 | See the note after this table | Open | Pending | CDR readiness declaration (lien, rule C1) |
| <a id="finding-3"></a>finding-3 | assurance | Minor | `swe-134 7.1 task 1`, SA-C-e, SA-C-h | ADR-031 section 2 item 9, third bullet ("It repeats the disable and the read-back after every DORMANT exit ... and on every switched-core power-up"); `clock-plan.md` section 5 request to WP-PDR-35 (HostUnit check) | See the note after this table | Open | Pending | CDR readiness declaration (lien, rule C1) |
| <a id="finding-4"></a>finding-4 | assurance | Minor | `swe-136 7.1 task 1`, `swe-070 7.1 task 1` | ADR-031 section 4.3, verification cases, second bullet ("an Inspection case that runs `clock_plan.py` against the configuration constants of the firmware (WP-PDR-35 and 43)") | See the note after this table | Open | Pending | CDR readiness declaration (lien, rule C1) |
| <a id="finding-5"></a>finding-5 | assurance | Minor | `swe-080 7.1 task 2`, SA-E3 | Commits `802347b` and `4153acf` (ADR-031 revisions 1 and 2), trailers | See the note after this table | Open | Pending | CDR readiness declaration (lien, rule C1) |
| <a id="finding-6"></a>finding-6 | assurance | Minor | `swe-088 7.1 task 1`, SA-A4 | INSP-056 (all iterations) against ADR-031; ADR-031 header row "Independent reviewer" | See the note after this table | Open | Pending | CDR readiness declaration (lien, rule C1) |

**finding-1 (constraints on safety-critical components other than WP-SW-11 are not assessed).**
- **Defect.** Section 4.3 assesses the safety-critical scope only for the WP-SW-11 step of item 9. Three other ADR-031 rules act on safety-critical components, and the ADR states no safety consequence or precedence for any of them.
  - **R-4 I2C traffic rule** (item 8: "transactions only on events or on polls no faster than once a second, each at most 1 ms"). The I2C bus carries the BQ25887 ADC reads of `SW-PWR` ("Sensing: BQ25887 ADC over I2C (VBAT, VCELLBOT, ICHG, TS)", `docs/research/power-tree-and-charging.md` Baseline topology). These serve the cell-sensor temperature of REQ-SYS-099 (HZ-007 K4, power down above 60 C) and the charger-ADC path of HZ-002 K4 ("charger ADC over I2C and RP2350 divider"). The bus also carries the TPA6130A2 volume of `SW-AUDIO` (HZ-005) if WP-PDR-25 keeps that amplifier. The `SW-PWR` supervision period is still "fixed at PDR" (07 section 14.2 row j). So the rule can bind an item j response time that has no value yet. It is also one budget shared by safety-critical and other I2C users (`swe-134` 7.1 task 4, partitioning).
  - **R-2 GPIO23 mode** ("GPIO23 driven high (PWM) while the receiver is on, subject to assumption 5"; assumption 5 "otherwise PFM is kept"). The Pico 2 SMPS mode sets the RP2350 ADC reference offset, "about 150 uA x 200 = ~30 mV", which "varies with sampling and temperature"; forcing PWM with GPIO23 high is one of the remedies (`power-tree-and-charging.md` F14). The dissimilar RP2350 cell-voltage path of REQ-SYS-088 and the per-cell 3.20 V threshold of REQ-SYS-097 ("measured in receive") rest on that ADC and its calibration against the charger ADC (F15; RSK-056). The ADR does not require that calibration and measurement run in the same SMPS mode.
  - **Audio and sidetone PWM TOP** (item 4: TOP + 1 = 1000, or 25 x an odd number with an IF of 9.000 MHz). This is the full-scale divisor of the `SW-AUDIO` output path, whose level cap (REQ-SYS-074) and limiter are safety-critical (HZ-005). The audio research derived its figures at TOP = 1023 (`audio-output-and-hearing-safety.md` F1). The ADR does not route TOP to `SW-AUDIO` as a scaling constant from which the cap is computed.
- **Why Minor.** No violation is shown today. A 1 s poll is plausible for a cell temperature, event-driven writes allow a fault mute, and the hardware layers stay in place: the independent cell protector (REQ-SYS-083) and the audio output ceiling (REQ-SYS-071 to 073). What is missing is the assessment and the precedence rule, not a working control.
- **Fix (lien).** Add one line per affected component to section 4.3, each with a request:
  - (a) R-4 yields to every safety-critical transaction (the `SW-PWR` supervision reads, the `SW-AUDIO` cap and mute writes). Otherwise, show that the `SW-PWR` supervision period is 1 s or longer and still meets its item j response. Requests to WP-PDR-35 and WP-PDR-32.
  - (b) GPIO23 is held in one stated mode during every `SW-PWR` ADC measurement and during its calibration. Requests to WP-PDR-24 and WP-PDR-35; the risk request is SA-F1.
  - (c) TOP is a `SW-AUDIO` configuration constant, and the cap is derived from it and checked by HostUnit. Requests to WP-PDR-35 and WP-PDR-25.

**finding-2 (the software part of HZ-008 K6 is not traced or assessed).**
- **Defect.** `hazards.json` 0.5.0-pha records HZ-008 K6 as `type` Design, `allocation` CTL, `independent_of_firmware` false, `control_req_ids` [REQ-SYS-034]. ADR-031 moves part of K6 into firmware:
  - the ROSC disable (item 9);
  - GPIO23 high in receive (R-2);
  - the I2C traffic rule (R-4);
  - no clock generator or output taking the LPOSC (R-5);
  - clk_usb gated to USB enumeration (item 5);
  - the 2.4 MHz buck SYNC from a crystal-derived RP2350 output (item 4).
  Section 4.1 sends the derived SW requirements to WP-PDR-35, and section 4.3 asks WP-PDR-16b only for the K6 text. Three things are not requested:
  - (i) The derived SW requirements carry `hazard_ids` HZ-008 and join K6 `control_req_ids` (charter section 7; 02 rule T-08). SWE-192 then requires a Test closing case for each. The HostUnit checks of section 4.1 qualify. The `clock_plan.py` Inspection case of section 4.3 can only be supporting.
  - (ii) The input to WP-PDR-16b and to the 03 PDR re-run (WP-PDR-17) that K6 now has software content. HZ-008 `firmware_role.components` names none of these units. Under the union rule of 03 section 4.1, either they join as mitigation (criterion c), or the hazard analysis records why the software part of K6 is not a safety function. For example, K6 may control receive birdies and board-level clock lines rather than the out-of-band carrier of C7.
  - (iii) The software contributions to K6. Inaction: the ROSC left running (the seeded case, 2 rule failures). Incorrect action: a ROSC DISABLE written while clk_ref or clk_sys still runs from the ROSC, which "the chip will lock up" (RP2350 Table 605). That stops the clocks and the watchdog tick, and it freezes the outputs. At bring-up the safe outputs are already asserted (07 section 14.2 row a), so they hold safe.
- **Why Minor.** Nothing in the ADR is wrong on the hazard record as it stands. The determination the missing items feed belongs to WP-PDR-16b and WP-PDR-17 at the PDR re-run, and the K6 text update is already requested. **Note for the lead SE:** if WP-PDR-16b rules that the software part of K6 is a safety function, a missing contribution then becomes a Major item against the hazard data, not against this ADR.
- **Fix (lien).** Add requests (i) and (iii) to section 4.3 for WP-PDR-35 and WP-PDR-16b, and request (ii) for WP-PDR-16b and WP-PDR-17. Correct "Safety-critical software scope changed: no" to "pending the HZ-008 K6 determination at the PDR re-run".

**finding-3 (the repeated ROSC disable has no stated prerequisite).**
- **Defect.** Item 9, first bullet, places the disable after "clk_ref runs from the crystal and clk_sys from PLL_SYS, each confirmed by its SELECTED read-back". That is the datasheet prerequisite: "Before stopping the ROSC, you must switch the reference clock generator and the system clock generator to an alternate source" (section 8.1.1.2), and "The system clock must be switched to another source before setting this field to DISABLE otherwise the chip will lock up" (Table 605). The third bullet repeats "the disable and the read-back" after every DORMANT exit and on every switched-core power-up, and it does not restate that prerequisite. The WP-PDR-35 HostUnit check requested in `clock-plan.md` section 5 asserts the order for the bring-up only.
- **Why Minor.**
  - The search found no DORMANT use in cwht.
  - A switched-core power-up runs the boot path, and so the bring-up with its read-backs (`clock-plan.md` rule 11 says so; the ADR does not).
  - An invalid CTRL code "will enable the oscillator" (Table 605), so a corrupted write fails to a running ROSC, not to a lock-up.
  - The repeat is therefore not a present hazard. It is a design statement a driver writer could implement out of order.
- **Fix (lien).** State that every repeat runs only after both SELECTED read-backs, or that it is the boot-path bring-up itself. Extend the requested HostUnit check to the repeat path. Or drop the DORMANT clause and add the revisit condition "DORMANT used".

**finding-4 (the checker becomes a verification tool without a validation record).**
- **Defect.** Section 4.3 makes `clock_plan.py` the tool of an Inspection case on the firmware's configuration constants. 05 section 9.1 classes such a tool B ("Output is cited as verification, inspection, audit or review evidence"), and a class B tool needs a "TV record before first cited use". INSP-056 `tools_used` records "no TV record covers hardware/sim/freq/*.py, developer evidence per 05 section 9.1". The ADR does not name the TV need.
- **Why Minor.** No case exists yet, and the checker is not cited for credit today.
- **Fix (lien).** Add to section 4.3: a TV-NNN record for `clock_plan.py` (class B, known-answer test with a seeded fault; the `--rosc-running` case is a ready seed, exit 1 with 2 rule failures) before the first cited use. The case stays supporting to the REQ-SYS-034 Test (finding-2 (i)).

**finding-5 (revision commits without the Refs trailer).**
- **Defect.** 05 section 4.5 makes `Refs:` "mandatory whenever a CI is touched (... ADR ...)". Commits `802347b` and `4153acf` revise ADR-031, the clock plan, the checker and the figure (05 Table 4-1 rows 13, 24, 33, 49). Their only trailer is `Co-Authored-By` (`git log -1 --format='%(trailers)'`). `tools/check_commit_msg.py --range <c>^..<c>` reports "FAIL REFS_MISSING 802347b: touches rows 13, 24, 33, 49 and has no Refs: trailer" and the same for `4153acf`. The tool is Validated but not yet accredited (TV-019), so the trailer read is the evidence. The freeze commit `9ac2c42` is INSP-074 finding-4 and is not raised again. No class-CR row is past its CR-from event, so no `CR:` trailer was needed.
- **Fix (lien).** History is not rewritten. The lead SE lists `802347b` and `4153acf` in the CSA change log as RID candidates for the PDR (the INSP-074 finding-4 practice), and the next ADR-031 commit carries `Refs: ADR-031, WP-PDR-20`.

**finding-6 (ADR-031 has no design-checklist file review).**
- **Defect.** 07 section 2.1.1 reviews an ADR with `peer-review-checklist-design.md` sections A, B and H. ADR-031's own header says "This ADR's own review uses `peer-review-checklist-design.md` sections A, B and H; the lead SE assigns the record". INSP-056 took ADR-031 into its `product_files` at iteration 2 and checked items 2 to 9 for consistency with `clock-plan.md` and the datasheet. It applied the analysis item set (CK-ANA), not design sections A, B and H. So these items have no file-review answer for ADR-031:
  - CK-DES-A7 (the component list equals 07 section 14.1);
  - CK-DES-B2 (each hazard with a software control traced to its unit);
  - CK-DES-H1 (no contradiction with an Accepted ADR; the ADR-023 item (5) refinement is flagged open by ADR-031 section 7 itself);
  - CK-DES-H4 (citations).
  The ADR header row "Independent reviewer" still reads "Pending" and describes INSP-056 as the record "which reviews `clock-plan.md`".
- **Why Minor.** This record answers the A7 and B2 substance under the assurance lens (sections C and D; findings 1 and 2), and INSP-056 re-checked the item 9 datasheet citations. No safety conclusion changes. This record does not replace the file review.
- **Fix (lien).** The lead SE either has the INSP-056 reviewer add a design A, B, H section for ADR-031 as a delta (reviewer-owned, no product change), or assigns ADR-031 its own design record. The author updates the header row to name the record.

No Major finding. None of the six findings changes the clock plan, the REQ-SYS-034 proposal or the INSP-056 verdict. They change what ADR-031 must carry into the hazard data, the derived SW requirements, the tool records and the review record.

### Task table

| Task | Safety-critical designation (SWEHB 8.10 section 6) | Applied | Result and evidence | Relief (N/A only) | Finding ids |
|---|---|---|---|---|---|
| swe-134 7.1 task 5 | SC | Yes | This record is the assurance participation in the review of a product that 07 section 2.1.1 routes (row "Trade studies and ADRs", safety-critical column Yes) | | none |
| swe-022 7.1 task 1 | SC | Yes | Performed against the project software assurance plan, 07 section 15, with this template. The NASA-STD-8739.8 part is relieved (next column) | NASA-STD-8739.8 part: `rmm.json` SWE-022 T (standard not in the corpus) | none |
| swe-033 7.1 task 1 | | Yes | The decision acquires no software. The clocks driver is developed in rustos (TS-002 alternative A0, ADR-027; ADR-051 for WP-SW-11). The parts it selects (TCXO 25.000 MHz, a buck with a SYNC input) are hardware choices of WP-PDR-24 and TS-007 | | none |
| swe-033 7.1 task 2 | SC | No | The safety obligations of the derived software work (hazard trace, Test closing case, criticality input) are not flowed to WP-PDR-35 and WP-PDR-16b | | finding-2 |
| swe-033 7.1 task 3 | | Yes | Section 4.4 assesses RSK-040 (step S1 evidence, residual family not mitigated by frequency). Assumptions 1 to 6 each name the confirming WP, the gate and the fallback. Assumption 6 names the REQ-SYS-034 consequence if WP-PDR-41 does not adopt item 9 (tracked as INSP-056 X-7) | | none |
| swe-039 7.1 task 4 | | Yes | Source data assessed. `clock_plan.py` re-run on a `git archive 4153acf` export in the scratchpad: exit 0, "RESULT: 0 rule failure(s) in the proposed plan; 5 named residual source(s)". `--rosc-running`: exit 1, "FAIL RULE-1", "FAIL RULE-2", "RESULT: 2 rule failure(s)". Both as ADR-031 option A states. The Table 605 DISABLE code 0xd1e and its lock-up note, and the section 8.1.1.2 DORMANT and switched-core lines, re-read from `git show 2ec64c0f:docs/extracted/rp2350-datasheet.md`: as quoted | | none |
| swe-057 7.1 task 2 | | No | Architecture against the safety requirements: the effects of R-4, R-2 and the PWM TOP on `SW-PWR` and `SW-AUDIO` are not assessed | | finding-1 |
| swe-134 7.1 task 4 | SC | No | Partitioning: R-4 creates one I2C traffic budget shared by safety-critical (`SW-PWR`, `SW-AUDIO`) and other users, with no precedence stated. The SW-SYNTH SPI divisor (item 4) raises no isolation question beyond INSP-074 finding-3, which is not raised again | | finding-1 |
| swe-134 7.1 task 6 | SC | No | The SWE-134 provisions item 9 adds are consistent with the WP-SW-11 row (a, g, j, k: read-back, bounded wait, fault). The hazard analysis does not yet carry the software part of K6 that the ADR creates | | finding-2 |
| swe-027 7.1 task 1 | | N/A | Condition not met: no COTS, GOTS, MOTS, OSS or reused software is acquired | Conditional task of the section B row ("reused or OSS component chosen"); 07 section 17.1 | none |
| swe-136 7.1 task 1 | | No | Condition met: section 4.3 selects `clock_plan.py` as the tool of an Inspection case on firmware constants (class B, 05 section 9.1). No TV record is named | | finding-4 |
| swe-070 7.1 task 1 | | No | As swe-136: a model whose output would qualify flight software constants, not validated or accredited, and the ADR does not plan it | | finding-4 |
| swe-205 7.1 task 3 | SC | No | The decision adds software functions that implement a hazard control (K6) and names them for no component in the hazard analysis. The input to the 03 PDR re-run is not stated | | finding-2 |
| swe-205 7.1 task 1 | SC | No | K6 walked by action, inaction and incorrect action. Inaction: ROSC not disabled; GPIO23 left in PFM; periodic I2C polls above the rule. Incorrect action: ROSC DISABLE before the clock switch (lock-up); LPOSC routed to a clk_gpout output. None is in the hazard data | | finding-2 |
| swe-134 7.1 task 1 | SC | No | Item 9 is analysed against items a, c, e, g, h, i, j, k and l (section C). The repeat path lacks the prerequisite of bullet 1 | | finding-3 |
| swe-052 7.1 task 2 | SC | No | The derived SW requirements of section 4.1 are not stated to trace to HZ-008 (K6). The current set reports 0 violations (R3) because none exists yet | | finding-2 |
| swe-080 7.1 task 1 | SC | No | The proposed change is analysed for WP-SW-11 only; its impacts on `SW-PWR` and `SW-AUDIO` and on the hazard data are not | | finding-1, finding-2 |
| swe-080 7.1 task 2 | | No | The change route of the product files: two revision commits without `Refs:` | | finding-5 |
| swe-081 7.1 task 2 | SC | Yes | ADR-031, the clock plan, the checker and the figures are committed at `4153acf` on `main`. `docs/safety/hazards.json` is under row control with the single writer WP-PDR-16b (plan section 5.3), and the ADR routes its K6 text change there | | none |
| swe-087 7.1 task 2 | | Yes | INSP-056 findings 1 to 4 and 8 (Major) are Verified with evidence at iterations 2 and 3. Findings 5, 6, 7, 9 and 10 (Minor) are Open liens due at the CDR readiness declaration (rule C1). None is closed without evidence | | none |
| swe-088 7.1 task 1 | | No | NPR 7150.2D 5.3.3 criteria a to d met for the analysis notes (checklist, readiness, tracked findings, measurements). For ADR-031 the checklist 07 section 2.1.1 assigns (design A, B, H) was not applied | | finding-6 |
| swe-089 7.1 task 1 | | Yes | INSP-056 carries the SWE-089 measurements (front matter `effort_turns` 30, `effort_minutes` 45, finding counts, `items_no`, and a measurements section per iteration). This record carries its own | | none |

## Readiness criteria

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | Product committed and frozen; `product_files` equal to the paired record's | Yes | `git rev-parse 4153acf:<path>`, `git rev-parse HEAD:<path>` and `git hash-object <path>` for the seven files: all equal the INSP-056 `product_files`. `git log 4153acf..HEAD` touches none of them |
| R2 | Product type and criticality identified | Yes | 07 section 2.1.1 row "Trade studies and ADRs whose decision constrains a safety-critical or mission-critical component" (`trade-study-or-adr`). Safety-critical by the 07 section 14.1 drivers row (clocks and PLL, WP-SW-11) and the `SW-SYNTH` frequency-word path row |
| R3 | `validate_docs.py` on the product files; `traceability.py --report-only --output <scratch>` clean for the ids the product touches | Yes | `traceability.py --report-only --output` to the scratchpad: "245 requirements, 173 test cases, 0 violation(s), 2 warning(s)" (REQ-SYS-125 and REQ-SYS-148, not touched by ADR-031); `git status docs/vv` clean afterwards. The ADR and analysis files carry no schema; `validate_docs.py`: see Commands |
| R4 | Paired file review filed under its own invocation; this reviewer is neither author nor file reviewer | Yes | INSP-056 `author_agent` "author:WP-PDR-20 wave 1a"; `reviewer_agent` "reviewer:WP-PDR-20-analysis-iter3" (iterations 1 and 2 by -iter1 and -iter2); this record `reviewer_agent` "sa-reviewer:WP-PDR-20-insp-056-adr-031" |

## A. Dispatch, independence and record integrity

| Id | Answer | Evidence |
|---|---|---|
| SA-A1 | Yes | 07 section 2.1.1 row 3, safety-critical column Yes. ADR-031 item 9 constrains WP-SW-11 and item 4 constrains `SW-SYNTH`, both in 07 section 14.1. INSP-056 X-6 states the same routing |
| SA-A2 | Yes | Four invocations: the author, the three file reviewers of INSP-056 (none of whom applied the SA lens; X-6 says so), and this assurance reviewer. INSP-056 names this pair as separate ("to be dispatched by the lead SE") |
| SA-A3 | Yes | Same product, same seven blobs, same commit `4153acf`. No product change after INSP-056 iteration 3 |
| SA-A4 | No | INSP-056 answered the analysis item set with evidence for both notes. For ADR-031 it did not apply design sections A, B and H (finding-6) |

## B. SWE-to-task table

| Id | Answer | Evidence |
|---|---|---|
| SA-B1 | Yes | The task table holds every task of the rows `trade-study-or-adr` and "Every product type", including the conditional swe-136 and swe-070 rows whose condition is met. It adds swe-205 task 1, swe-134 task 1, swe-052 task 2, swe-080 tasks 1 and 2, swe-081 task 2, swe-087 task 2, swe-088 task 1 and swe-089 task 1 for the SWEs the ADR touches. `assurance_tasks_applied` lists every Yes and No row |
| SA-B2 | Yes | One N/A row (swe-027), a conditional task whose condition is not met, with the 07 section named. No SC task is N/A |
| SA-B3 | Yes | Each No row cites a finding (finding-1 to finding-6) |

## C. SWE-134 items a to l (ADR maturity: the decision neither precludes nor weakens the 07 section 14.2 provision)

07 section 14.2 allocates a, g, j and k to the WP-SW-11 driver. Items c, e, h, i and l are also checked because item 9 adds a register write that locks the chip if it is issued early. Items b, d and f are N/A: ADR-031 adds no state machine, no operator override and no RAM safety state.

| Id | Answer | Evidence |
|---|---|---|
| SA-C-a | Yes | The ROSC step comes after the crystal and PLL_SYS switch, in the clock bring-up. 07 section 14.2 row a runs the clock bring-up after the safe outputs are asserted. The ROSC state at reset does not affect the safe outputs |
| SA-C-b | N/A | No state or transition added |
| SA-C-c | Yes | A read-back failure returns a ClockFault. ADR-051 halts in the safe state (REQ-SYS-130), with the ROSC left running as a fault-state item (item 9, last bullet) |
| SA-C-d | N/A | No operator override |
| SA-C-e | No | The first disable is ordered after both SELECTED read-backs. The repeat is not (finding-3) |
| SA-C-f | N/A | No RAM safety state added |
| SA-C-g | Yes | STATUS.ENABLED = 0 read back (Table 612; ENABLED means "enabled but not necessarily running", so 0 is the right post-condition, as INSP-056 iteration 3 confirmed). The existing XOSC STABLE and PLL LOCK read-backs of the row are untouched |
| SA-C-h | No | Prerequisite before a command whose early issue locks the chip: stated for bullet 1 only (finding-3) |
| SA-C-i | Yes | After bring-up neither clk_ref nor clk_sys runs from the ROSC, so a single stray DISABLE is harmless. A corrupted code "will enable the oscillator" (Table 605), which fails to a birdie, not a lock-up. The SW-SYNTH divisor adds no shared path with the verification unit |
| SA-C-j | No | The ROSC wait is bounded by the ADR-051 poll budget, a loop bound independent of TIMER0 (row j holds for WP-SW-11). The R-4 rule can bind the `SW-PWR` item j response, and that is not assessed (finding-1) |
| SA-C-k | Yes | Stuck ENABLED gives its own ClockFault variant (`clock-plan.md` section 5 request to WP-PDR-41); no error is dropped |
| SA-C-l | Yes | The safe state stays reachable from every bring-up step. Stopping the ROSC removes no fallback: resus switches clk_sys to clk_ref, and clk_ref runs from the XOSC whether or not the ROSC runs (section 8.1.4; INSP-056 iteration 3) |

## D. Software safety analysis and hazard traceability

| Id | Answer | Evidence |
|---|---|---|
| SA-D1 | No | HZ-008 K6 walked with SWEHB `swe-205` section 7.7.2 in mind: control of hardware (the buck SYNC, GPIO23), stored configuration (the divisors and TOP), common cause (the shared I2C budget). The software contributions of K6 are not in the hazard data (finding-2 (iii)). The TCXO and shared-bus common causes of the frequency path are INSP-056 finding-7 and INSP-074 finding-3 |
| SA-D2 | No | 07 section 14.1 lists WP-SW-11 and `SW-SYNTH`. The K6 software functions the ADR adds are not stated as an input to the 03 PDR re-run (finding-2 (ii)) |
| SA-D3 | N/A | No software requirement is written by an ADR. The system ids it touches (REQ-SYS-034, HZ-008) report no traceability violation (R3). The trace of the future SW requirements is finding-2 (i) |
| SA-D4 | N/A | No safety-tagged software requirement is written by this product |
| SA-D5 | N/A | No hazard-tracing software requirement is written by this product. The Test closing case the derived requirements will need is carried in finding-2 (i) |
| SA-D6 | No | The K6 text update is requested; the firmware-role assessment of the new K6 software functions is not (finding-2) |

## E. Peer review, change and configuration assurance

| Id | Answer | Evidence |
|---|---|---|
| SA-E1 | Yes | INSP-056 Majors 1 to 4 and 8 Verified at iterations 2 and 3 with evidence; Minors 5, 6, 7, 9 and 10 Open as liens (rule C1). INSP-074 cross item X-2 (the SA routing of the analysis record) is resolved by this pair |
| SA-E2 | Yes | Both records carry the SWE-089 fields |
| SA-E3 | No | `802347b` and `4153acf` have no `Refs:` trailer (finding-5). ADRs are Record class (05 Table 4-1 row 13); a Proposed ADR may be revised, and no `CR:` trailer was due |
| SA-E4 | N/A | Test and code rows only; no test or credit run |

## F. Assurance risks, metrics and reporting

| Id | Answer | Evidence |
|---|---|---|
| SA-F1 | Yes | One assurance concern that is not a product defect goes to the register writer WP-PDR-18 as a member of RSK-056 with tag `assurance`. It reads: "Given the Pico 2 SMPS mode (GPIO23, PFM by default, PWM in receive only under ADR-031 R-2 and assumption 5) sets the RP2350 ADC reference offset of about 30 mV that varies with sampling (power-tree-and-charging F14), there is a possibility that the RP2350 cell-voltage path is calibrated in one mode and read in the other, adversely impacting the REQ-SYS-088 dual-path threshold and the REQ-SYS-097 per-cell transmit inhibit, leading to nuisance or missed inhibits." The lead SE forwards it (cross item X-3). The assumption 6 dependency (WP-PDR-41 adopting item 9 before B2) is already INSP-056 X-7 and is not re-entered |
| SA-F2 | Yes | Front matter: findings by severity and state, `assurance_findings_major` 0, `assurance_findings_minor` 6, `items_no`, effort |
| SA-F3 | Yes | The package "Software assurance findings" section can take from this record: assurance verdict APPROVED; six Minor liens, Open; 21 tasks applied (13 answered No), 1 N/A with its condition; SWE-022 relief used |

## Cross items for the lead SE (not findings on ADR-031)

- **X-1.** INSP-056 still reads `assurance_reviewer_agent: "pending (...)"` and `assurance_verdict: pending`, and it has no `paired_record`. Its reviewer updates it to `paired_record: INSP-111`, names this reviewer, and copies `assurance_verdict: APPROVED` (07 section 10.2 Record row). The record verdicts of both then follow the lead SE convention for the branch-only templates (INSP-056 X-1).
- **X-2.** INSP-056 front matter names `checklist_revision: A` for the design checklist, and `main` carries revision B. This record names B. The INSP-056 reviewer aligns the field at the X-1 update.
- **X-3.** The SA-F1 risk request goes to WP-PDR-18 (the register's single writer, plan section 5.3).
- **X-4.** Findings 1 and 2 carry requests to WP-PDR-35, WP-PDR-32, WP-PDR-24, WP-PDR-25, WP-PDR-16b and WP-PDR-17. The author sends them with the next ADR-031 revision (plan section 5.3; the author edits none of those files).
- **X-5.** The six Minor findings arrive after INSP-056's first APPROVED verdict, so under rule C1 they are liens due at the CDR readiness declaration, listed in package section 15, and they do not reopen the product before the B2 value ruling.

## Commands

- `git rev-parse 4153acf:<path>`, `git rev-parse HEAD:<path>`, `git hash-object <path>` for the seven product files: equal to `product_files`. `git merge-base --is-ancestor 4153acf main`: true.
- `.venv/bin/python hardware/sim/freq/clock_plan.py` on a `git archive 4153acf` export in the scratchpad: exit 0, "RESULT: 0 rule failure(s) in the proposed plan; 5 named residual source(s)". With `--rosc-running`: exit 1, "RESULT: 2 rule failure(s) in the proposed plan; 5 named residual source(s)".
- `.venv/bin/python tools/traceability.py --report-only --output <scratchpad>/traceability-report.md`: 0 violations, 2 warnings; `docs/vv/` unchanged.
- `.venv/bin/python tools/check_commit_msg.py --range 802347b^..802347b` and `--range 4153acf^..4153acf`: "FAIL REFS_MISSING" for each (tool Validated, not accredited, TV-019; the evidence is the trailer read).
- `git -C /Users/robinonsay/rust/rustos show 2ec64c0f:docs/extracted/rp2350-datasheet.md`, lines 41352 to 41358 (Table 605) and 37446 to 37454 (section 8.1.1.2): as quoted.
- `.venv/bin/python tools/validate_docs.py`: this record passes (see the return).

## Visual closure

`docs/reviews/PDR/figures/clock-plan-harmonics.png` (blob `0a4d221c`) was opened with the Read tool. The ROSC row is olive ("off in operation", "disabled in operation by rule 11"), the LPOSC, I2C, charge-pump and core-regulator rows are magenta residual bars, the RT6150 row carries the "frequency not in the corpus" note, and the audio PWM row shows TOP + 1 = 1000 proposed against the rejected TOP + 1 = 1024 (finding-1 (c)). All agree with ADR-031 items 4, 8 and 9.

## Measurements (SWE-089)

Tasks in the table: 22 (21 applied, 1 N/A). Tasks answered No: 13. Checklist items answered No: 8 (SA-A4, SA-C-e, SA-C-h, SA-C-j, SA-D1, SA-D2, SA-D6, SA-E3). SWE-134 items checked: 9 (b, d, f N/A). Findings: 0 Major, 6 Minor, all Open (liens, rule C1). Iteration 1. Renders inspected: 1. Effort: 40 turns, about 70 minutes.

## Iteration 2: WP-PDR-20a delta, `frequency-budget.md` revision 2 section 3.4 (2026-09-29, HEAD `fd12ced`)

**Product.** The ten `product_files` of the front matter at freeze commit `7593cea` (freeze F0, rule C2): `frequency-budget.md` revision 2 `14229c9d`, the new checker `hardware/sim/freq/r3_a5.py` `eebcd167`, its run `r3a5-20260929-01` (`results.json` `53c58eaa`, `checker-output.txt` `c73f1e60`, the script copy `eebcd167`, four PNGs), and `freq_budget.py` `d82269e6`, unchanged and imported. Each blob is equal at `7593cea`, at `HEAD` `fd12ced` and in the working tree; `7593cea` is on `main`. The two commits after it (`8d5bc0a`, `fd12ced`) touch no product file. Sections 3.1 to 3.3 are unchanged from the blob INSP-056 approved and are read only where section 3.4 rests on them. This iteration is iteration 1 of the WP-PDR-20a delta (new content, reviewed in full; rule C1). **Paired record:** INSP-056, whose WP-PDR-20a delta is dispatched beside this one and is not yet filed (cross item X-6).

**Assurance lens.** The safety-critical firmware and hardware controls section 3.4 sets or depends on: the key-down prerequisites of `PA_EN` (the interval-12 count, the lock-status read, the ratio age), the lock-gated changeover and its deadline, the ratio-age rules R-FRESH-1 and R-FRESH-2, the interval-13 drift allocation, the FC0 single-counter abandon path, the receive-only squaring stage and its supply switch, the LOL_A lock-detect indication for the REQ-SYS-154 unlocked trigger, and the closure measurements M-1 and M-2. Components: the frequency verification unit (`SW-SAFE`) and the `SW-SYNTH` frequency-word path, both Proposed safety-critical (07 section 14.1; 07 section 14.2 rows a, b, f, g, h, i, k, l). Hazard: HZ-008 causes C7 and C8, control K7.

**Checklist.** As iteration 1: `peer-review-checklist-software-assurance.md` revision A at `5b135285` (branch-only). The template has no section B row for an analysis note. The row `trade-study-or-adr` is applied because section 3.4 sets design constraints on two 07 section 14.1 components, with the row "Every product type" and the section 7.1 tasks of the SWEs the note touches: swe-134 task 1 (the design response is a SW-SAFE and SW-SYNTH design step), swe-205 tasks 1 and 3, swe-039 task 3 and swe-071 task 1 (M-1 and M-2 are the named verification of a hazard-control condition), swe-136 and swe-070 (a new class B checker importing the thermal model), swe-080, swe-081, swe-087 and swe-089.

**Acceptance criteria (rule C7).**
- Revisit condition 1 (relock): the claim that a slow relock costs availability and not safety, at both moments the check serves (the interval-12 count before `PA_EN`; the frequency at the ramp and during the first element), and M-1's ability to close it.
- Revisit condition 2 (freshness): both checks (interval 12 with A_kd; interval 13 with 6.5 ppm), the ratio age at each, and every path by which an aged or stale value can reach the `PA_EN` decision (after an over, the abandon at t0, a refresh not completed).
- REQ-SYS-154: both triggers ("unlocked", "off its set frequency by over 10 kHz") at both moments ("on key-down", "during transmission") on A5, with the TC-SYS-101 closing case.
- The squaring stage by action, inaction and incorrect action of its supply switch.
- The derived I2C constraint and its routing.
- 07 section 14.2 items b, c, e, g, h, i, j, k and l for the two components, at analysis maturity.

**Independence (rule C4).** This invocation authored no part of WP-PDR-20 or 20a (the note, either checker, the run, the figures, TS-012, the spur plan, the thermal model) and wrote no iteration of INSP-056, INSP-074, INSP-110 or INSP-118, nor iteration 1 of this record. It edited no product file.

**Search first (charter section 11 rule 1).** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search. Queries: WP-PDR-20a, route R3 and the Si5351A relock; the INSP-056 and INSP-111 records; the I2C SCL counts at clk_sys 96 MHz and option C6; the rule for datasheet sources. Before the tool was loaded no search ran. `grep`, `sed` and a Python walk of `requirements.json`, `hazards.json` and `register.json` were used afterwards only to pin lines and fields. The rustos repository was not read.

**Sources re-read.** The Skyworks data sheet and AN619 were fetched through the web-fetch tool. Their PDF SHA-256 values equal the checker's (`f3bc5285...a4851101f`, `0135b3a3...4783f36b`). They were converted with `pdftotext` in the scratchpad; no file was added to the repository.
- Data sheet Rev. 1.3, August 27, 2021, Table 5: TRDY typ 2, max 10 ms; TBYP typ 0.5, max 1 ms; TOE max 10 us; TFREQ max 10 us at fCLKn > 1 MHz. No lock, settle or acquisition time anywhere in the text; the features list names "Glitchless frequency changes". As the note states.
- AN619 Rev. 0.8, September 23, 2021: Register 0 bit 5 LOL_A, "PLL A Loss Of Lock Status", with the cause of a loss of lock given as the reference frequency forcing "the PLL to operate outside of its lock range", or a reference that "fails to meet the minimum requirements of a valid input signal". Register 1 bit 5 LOL_A_STKY is the sticky copy. Register 177 bit 5 PLLA_RST is self-clearing. As the note states (section 2 and limitation 7).

### Findings (iteration 2)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-7"></a>finding-7 | assurance | Major | `swe-134 7.1 task 1`, `swe-039 7.1 task 3`, `swe-071 7.1 task 1`, SA-C-h | `frequency-budget.md` section 3.4.1 "Why the relock time is an availability question, not a safety one", measurement M-1, finding 3.4.1; `r3_a5.py` RL-8; section 3.1 case C-2 | See the note after this table | Open | Pending | |
| <a id="finding-8"></a>finding-8 | assurance | Minor | `swe-134 7.1 task 1`, SA-C-b | Section 3.4.1 "Design response" item 1; the M-1 branches; section 5 revision 2 requests to WP-PDR-23a and 35 | See the note after this table | Open | Pending | |
| <a id="finding-9"></a>finding-9 | assurance | Minor | `swe-057 7.1 task 2`, `swe-134 7.1 task 6`, SA-C-j, SA-D6 | Section 3.4.4 (first paragraph, U-2); finding 3.4; section 4 revision 2 bullet "REQ-SYS-154, else a CR column" and the REQ-SYS-154 row | See the note after this table | Open | Pending | |
| <a id="finding-10"></a>finding-10 | assurance | Minor | `swe-033 7.1 task 2`, `swe-134 7.1 task 1`, SA-C-e, SA-C-g | Section 3.4.2 "FC0 is a single counter", R-FRESH-1 and R-FRESH-2, the interval-13 row; section 5 revision 2 requests to WP-PDR-32 and 35 | See the note after this table | Open | Pending | |
| <a id="finding-11"></a>finding-11 | assurance | Minor | `swe-205 7.1 task 1`, `swe-205 7.1 task 3`, SA-D1 | Section 3.4.3 "In transmission"; BL-2; section 5 revision 2 request to WP-PDR-36a (squaring-stage supply GPIO) | See the note after this table | Open | Pending | |
| <a id="finding-12"></a>finding-12 | assurance | Minor | `swe-080 7.1 task 1` | Section 3.4.1 "Time the sequence allows" and design response item 2; RL-2, RL-2b; M-1 pass criterion; section 5 revision 2 request to WP-PDR-32 | See the note after this table | Open | Pending | |

**finding-7 (Major): the self-validation argument bounds the mean frequency over the count, not the frequency at the ramp, and M-1 cannot see the difference.**
- **Defect, the argument.** Section 3.4.1 treats a count taken during the settle as one that "includes the old LO frequency, 8 MHz away", so that "a transient of more than about 2.5 us inside the 4 ms count moves the mean by more than T". From that it concludes that the relock time bounds availability, not safety, and that the argument "holds for any relock time". RL-8 prints the same premise: "a PLL still settling gives a count outside T".
  - A counter measures cycles, that is the integral of the frequency over its interval. The premise holds for the large-signal (slewing, cycle-slipping) part of a retune, where the error has one sign and is large.
  - It does not hold for the linear tail of a charge-pump PLL. Once the phase error at the phase detector is inside a reference period (40 ns at 25 MHz), the error the tail can add to a count is at most the phase error at the count's start minus that at its end. That is two reference periods, 80 ns, or about 12 cycles of a 146 MHz carrier: 2.9 kHz over the 4 ms interval, inside T = 5 kHz. The instantaneous excursion of a ringing tail can meanwhile exceed 10 kHz.
  - So an interval-12 count that agrees shows that the mean over t0 + L to t0 + L + 4 ms was inside T + d. It does not show the frequency at the ramp (t0 + 10 ms) or during the first element's rise. The second paragraph, the interval-13 checks within 46 ms, covers a loop that ends at a wrong frequency, not a tail that is still decaying when RF starts.
- **Why it is new in revision 2.** In section 3.3 the A1 carrier had its own PLL and A2 had a stated retune time. In A5, PLL A retunes by the 8 MHz IF at the first element of every over, 10 ms before the ramp. The only sourced bound on acquisition is TRDY at 10 ms, which is the ramp time itself. Section 3.1 carries a 5 Hz frequency-word error and has 75.0 Hz of margin at the upper edge (C-2). A settle residual at the ramp is not in that budget, and section 3.4 does not re-examine it.
- **Defect, the closure means.** M-1 measures the settle as the smallest delay D at which interval-12 counts "all agree within T/8 at the counted input" (625 Hz at GPIN0, against the FC0 accuracy of 500 Hz at interval 12, Table 541). Two problems follow:
  - by the bound above, a linear tail passes that metric;
  - its resolution, about 1 kHz carrier-referred at best, is an order of magnitude coarser than the 75 Hz margin.

  M-1's second method, timestamped LOL_A reads, measures no frequency (AN619 ties LOL_A to the reference, see the sources above). M-1's pass criterion, "settle at most 0.35 ms", can therefore be met while the output is still outside the section 3.1 budget at the ramp.
- **Why Major.** This argument is the stated basis for three conclusions:
  - the unsourced relock time is an availability item only (RL-8, finding 3.4.1);
  - WP-PDR-32 and 36a can be written now;
  - no requirement or CR-018 row changes.

  It is the rationale of a `PA_EN` prerequisite of HZ-008 K7 (07 section 14.2: frequency verification unit item h; `SW-SYNTH` item l). The measurement named to close revisit condition 1 cannot detect the failure mode the argument leaves out. The physical tail of the Si5351A is probably microseconds long (TFREQ 10 us; "Glitchless frequency changes" in the data sheet features). No source states that for an MSNA change, and that gap is what revisit condition 1 exists to close.
- **Fix.**
  - (a) Restate section 3.4.1 and RL-8. The count bounds the integrated error over its own interval. The slewing part of a slow relock is caught, which costs availability. The linear tail is not caught, so the frequency at the ramp needs a bound on the settle.
  - (b) Add to M-1 a time-resolved measurement of the CLK1 (or GPIN0) frequency from the last C6 write through t0 + 12 ms, at the three test frequencies. Give it a pass criterion at the ramp time stated against section 3.1: for example, the residual error inside the 5 Hz frequency-word allocation, or a named settle allocation carried into C-2 with the 75.0 Hz margin recomputed. The method is the author's choice (for example an oscilloscope capture with instantaneous-frequency analysis, or an SDR quadrature capture), on the WP-PDR-43 bench list.
  - (c) Carry the settle residual at the ramp in section 3.1 for A5, as a named term or inside the 5 Hz term with the reason, and in the M-1 branch ladder.
  - (d) The note cites INSP-118 item (3), which states the same premise. Correcting the note is the author's; cross item X-7 routes the INSP-118 wording.

**finding-8 (Minor): the lock gate adds no settle time if LOL_A does not assert on a retune.**
- **Defect.** Design response item 1 starts FC0 interval 12 "at the first 0 read" of LOL_A, no later than L_max. AN619 ties LOL_A to a reference outside the PLL's lock range or an invalid reference. It does not say LOL_A asserts during an MSNA retune with a valid reference, and the note itself says LOL_A "is not credited as proof of settling".
  - If LOL_A stays 0, the first read returns 0 at about t0 + 0.75 ms (0.650 ms of writes plus the 0.098 ms read). The count then starts with no settle time, and the gate implements "count right after the writes".
  - The M-1 ladder then fails its own middle branch. "At most 1.35 ms, the sequence stands with L_max = 2.0 ms" does not follow: for a settle between 0.35 and 1.35 ms, the lock-gated count starts inside the settle and disagrees, so every first element is lost.
  - The requests to WP-PDR-23a and 35 carry the same start condition.
- **Why Minor.** The failure direction is availability: `PA_EN` is not set.
- **Fix.**
  - Start the count at the later of the first LOL_A = 0 read and t0 + D_s, where D_s is M-1's measured settle plus a stated margin, capped at L_max.
  - Add to M-1 a log of whether LOL_A and LOL_A_STKY (register 1) assert at all on the C6 retune.
  - Carry the start rule in the 23a and 35 requests, with a HostUnit case at D_s.

**finding-9 (Minor): on A5 the unlocked trigger during transmission is not closed, but the conclusions state it as met.**
- **Defect.**
  - (i) Section 3.4.4 says LOL_A "closes, for A5, the research gap" and the "else a CR" branch "no longer applies"; section 4 repeats this. AN619 gives LOL_A's cause as a reference outside the lock range or an invalid reference. HZ-008 C8 names "the PLL unlocked, locked to a wrong value or to a reference harmonic". Which of these modes LOL_A flags is not sourced; limitation 7 says only that its latency is unspecified.
  - (ii) U-2 is unresolved. Option (a) conflicts with D-12; option (b) leaves the counter as the only means. Finding 3.4 and the section 4 REQ-SYS-154 row ("read ... at least every 10 ms during transmission") nevertheless state the unlocked trigger as met with the requirement as written. That holds only with option (a).
  - (iii) The REQ-SYS-154 closing case TC-SYS-101 forces "loss of lock ... during an over" and expects no carrier, and 07 section 14.2 `SW-SYNTH` item l requires Fault-safe for "an unlocked ... synthesizer ... during transmission". With option (b) both need restating. The note names neither.
- **Why Minor.** The counter covers the gross unlocks HZ-008 names: a VCO that leaves the loop moves far outside T, and a stopped output reads DIED. The open question is disclosed and routed to WP-PDR-32 and 35.
- **Fix.**
  - State finding 3.4 and the section 4 row as conditional on U-2 option (a).
  - State LOL_A's coverage as AN619 gives it. Keep the "else a CR" branch open for the modes it does not cover until a dev-board fault injection (reference removed; MSNA set outside the VCO range) shows what LOL_A flags. That injection can be run beside M-1.
  - Name TC-SYS-101 and 07 section 14.2 `SW-SYNTH` item l in the U-2 requests, and send the HZ-008 C8 wording to WP-PDR-16b.

**finding-10 (Minor): the freshness and source of the values `PA_EN` rests on are not bound.**
- **Defect, (i) the abandon path.** Section 3.4.2 adds the rule that "A refresh in progress at t0 must be abandoned". The requests ask WP-PDR-32 to confirm that writing FC0_SRC stops a count, and give WP-PDR-35 a HostUnit case "a refresh abandoned at t0". None requires that the result used for the key-down decision comes from the count started at t0 + L on GPIN0. A failing sequence:
  1. An over shorter than A_kd ends, and R-FRESH-1 starts a refresh.
  2. The operator keys within the 82 ms of that refresh, so it is abandoned.
  3. The FC0 result still holds the previous over's last interval-13 carrier count, at the same set frequency.
  4. A read that does not check a DONE set by the new count finds agreement, and `PA_EN` is set with no count of the retuned PLL.

  A C7 or C8 fault at that retune then goes undetected until the interval-13 checks, up to 46 ms (C-15). 07 section 14.2 (frequency verification unit, item g) names "stuck count" plausibility, and the requests do not tie it to this path.
- **Defect, (ii) no ratio-age ceiling during the over.** The 6.5 ppm interval-13 allocation holds for a ratio up to A_kd + 180 s old. That rests on REQ-SYS-180, a hardware backstop (SRR decision 38), and on R-FRESH-1. SW-SAFE gets no ratio-age ceiling of its own for interval-13 checks, and section 3.4.2 does not name the dependency. With the backstop failed, the drift is bounded only by the change from the receive steady state to the continuous-transmit steady state, which the note does not compute against the 17.77 ppm ceiling.
- **Why Minor.** (i) is ended within 46 ms, inside the REQ-SYS-182 "or end it within 100 ms" branch. (ii) needs a second, independent failure.
- **Fix.** Requests to WP-PDR-35:
  - The key-down decision uses only a result whose count started after the last C6 write, on GPIN0, with DONE set by that count. Add a HostUnit case with a stale result that matches the set frequency.
  - An interval-13 ratio-age ceiling: A_kd + 180 s, or the age at which the drift bound reaches the ceiling. Beyond it the check reads as a disagreement.
  - Name REQ-SYS-180 as a dependency in section 3.4.2.

**finding-11 (Minor): the squaring-stage supply switch is a new firmware output that bears on the 150 MHz spurious line, and its inaction case is not assessed.**
- **Defect.** Section 3.4.3 and the 36a request add a GPIO that powers the squaring stage in receive and turns it off from t0. "The stage adds nothing to the 150.000 MHz line" rests on that output being off in transmission.
  - The spur-plan figure the note keeps has no room for a 25 MHz square-wave source left on: plan PB high estimate -12.1 dBm at the SMA, 3.9 dB over 25 uW, a residual line closing at the bench.
  - The inaction case (a firmware fault leaves the stage powered in transmission) is not assessed.
  - The output is not assigned to a component, has no stated reset or Fault-safe state, and no request goes to WP-PDR-16b (HZ-008, 97.307(e)).
- **Why Minor.** The note already offers WP-PDR-37 the option to derive the stage supply from a receive-only rail. That option removes the software contribution.
- **Fix.** Prefer the hardware derivation. If a GPIO is kept:
  - state the line level with the stage on in transmission, or a bound on it;
  - assign the output to a component, off at reset and in Fault-safe;
  - send the software contribution to WP-PDR-16b.

**finding-12 (Minor): the write time assumes exactly 400 kHz, and the SCL constraint is not routed to the ADR-031 revision.**
- **Defect.** RL-2 (0.650 ms, 0.35 ms left) and the M-1 pass threshold ("settle at most 0.35 ms") assume an SCL of exactly 400 kHz.
  - The reviewed clock plan models the RP2350 master at "I2C SCL 357.1 to 396.8 kHz (375 ic_clk plus a 20 to 300 ns rise time)" (`clock-plan.md` section 2; INSP-056 finding-4). At 357 kHz the 260 SCL clocks take 0.728 ms and leave 0.27 ms.
  - The derived constraint "SCL at least 263 kHz" goes only to WP-PDR-32. Plan row 20 puts the clk_sys 96 MHz `clock_plan.py` re-run and the ADR-031 revision in WP-PDR-20a itself. ADR-031's I2C rule, the I2C residual line set (R-4) and the spur plan's lead-in I2C lines all change with SCL.
- **Why Minor.** It affects availability only, and the lock-gated sequence absorbs it within L_max.
- **Fix.**
  - State the write time over the achievable SCL range, rise time included, and use the lowest value in the M-1 pass threshold.
  - State the constraint as the SCL including the rise time.
  - Route it to the ADR-031 revision of WP-PDR-20a and to the spur plan's owner.

**Verified with no finding (iteration 2).**
- **Checker reproduced.** `r3_a5.py` was re-run on a `git archive 7593cea` export in the scratchpad: exit 0, "RESULT: 23 pass, 0 fail, 10 info", about 4.3 s. `checker-output.txt` is identical apart from the run id. `results.json` differs only in `run_id`. The script copy equals `r3_a5.py`. `freq_budget.py` gives 35 PASS.
- **Hand re-computation.**
  - The C6 writes are 92 + 47 + 29 + 92 = 260 SCL clocks: 0.650 ms at 400 kHz and 1.016 ms at 256 kHz. The minimum SCL is 260 / 0.990 ms = 262.6 kHz.
  - L_max is 10 - 2 - 4 - 2 = 2.0 ms (RL-4), 12 - 2 - 4 - 2 = 4.0 ms (RL-5) and 12 - 2 - 8 - 2 = 0 ms (RL-6).
  - The drift ceilings are (5 000 - 4 370) / 148.0 = 4.26 ppm at interval 12 and (5 000 - 2 370) / 148.0 = 17.77 ppm at interval 13.
  - d at interval 13 is 2 518 + 5.5 x 148.0 = 3 332 Hz.
  - A_kd is 0.8 / (0.924 x 0.082) = 10.6 s, and 10 s is proposed.
  - The interval-12 detection arithmetic, 8 MHz x 2.5 us / 4 ms = 5 kHz, is correct as arithmetic (finding-7 is about its premise).
- **Failure directions that hold.**
  - R-FRESH-2 withholds `PA_EN` on an aged ratio.
  - LOL_A still 1 at L_max gives no `PA_EN`.
  - A stage that does not toggle reads DIED, so RF is withheld.
  - A cross-attributed count fails safe: a 25 MHz TCXO count read as carrier/8 disagrees by about 6.5 MHz at GPIN0, and a carrier count taken as the ratio fails the +/-67.5 ppm plausibility test.
  - While CLK1 slews with `PA_EN` low, the drive is unpowered (D-18), and the key-up level of about -61 dBm (A5) is under REQ-SYS-183.
- **Other points.** The RL-6 finding against the TS-012 fallback is correct and routed (WP-PDR-54, 23a). The requests keep the Si5351A on its own I2C instance (INSP-074 finding-3). The Evidence status row and section 6 item 1 state the class B checker and the missing TV record (CK-ANA-C2), consistent with iteration 1 finding-4. Sections 3.1 to 3.3 and `freq_budget.py` are unchanged, and INSP-056 Minor findings 5 to 7 and 9 are stated as not addressed (rule C1).

### Findings (iteration 2; current state of every finding of this record)

| Finding | Severity | State | Note |
|---|---|---|---|
| finding-1 | Minor | Open | Iteration 1 lien on ADR-031 (rule C1), due at the CDR readiness declaration; unchanged, ADR-031 not revised |
| finding-2 | Minor | Open | As finding-1 |
| finding-3 | Minor | Open | As finding-1 |
| finding-4 | Minor | Open | As finding-1. `frequency-budget.md` section 6 item 1 now states the TV need for `hardware/sim/freq/*.py`, which includes `clock_plan.py`; the ADR-031 section 4.3 text is unchanged |
| finding-5 | Minor | Open | As finding-1. The new commit `7593cea` carries `Refs:` (check_commit_msg PASS) |
| finding-6 | Minor | Open | As finding-1 |
| finding-7 | Major | Open | Iteration 2; blocks the WP-PDR-20a delta |
| finding-8 | Minor | Open | Iteration 2; before the delta's first APPROVED verdict, so the author may fix it with finding-7, else it becomes a lien at that verdict (rule C1) |
| finding-9 | Minor | Open | As finding-8 |
| finding-10 | Minor | Open | As finding-8 |
| finding-11 | Minor | Open | As finding-8 |
| finding-12 | Minor | Open | As finding-8 |

### Task table (iteration 2)

| Task | Safety-critical designation (SWEHB 8.10 section 6) | Applied | Result and evidence | Relief (N/A only) | Finding ids |
|---|---|---|---|---|---|
| swe-134 7.1 task 5 | SC | Yes | This record is the assurance participation in the review of section 3.4, which sets `PA_EN` prerequisites of two Proposed safety-critical components | | none |
| swe-022 7.1 task 1 | SC | Yes | Performed against 07 section 15 with this template; NASA-STD-8739.8 part relieved | `rmm.json` SWE-022 T | none |
| swe-033 7.1 task 1 | | Yes | No software acquired; the Si5351A and the squaring stage are hardware items (TS-012, WP-PDR-20b, 37, 38) | | none |
| swe-033 7.1 task 2 | SC | No | The safety obligations of the derived SW-SAFE work: the result freshness on the abandon path and the interval-13 age ceiling are not flowed to WP-PDR-35 | | finding-10 |
| swe-033 7.1 task 3 | | Yes | Section 6 items 7 to 11 state the new uncertainties. The relock-time schedule risk goes to the register writer (SA-F1 below) | | none |
| swe-039 7.1 task 3 | | No | Verification adequacy: M-1 cannot observe a settle tail at the ramp. M-2 is adequate for the drift it bounds | | finding-7 |
| swe-039 7.1 task 4 | | Yes | Source data assessed: both PDFs re-read with equal SHA-256; the Table 5 values, the absence of a lock time and the AN619 register text as the note quotes them. The thermal model is imported unchanged (`54573514`) | | none |
| swe-057 7.1 task 2 | | No | The unlocked trigger during transmission rests on an unresolved architecture choice (U-2), and the conclusions state it as met | | finding-9 |
| swe-134 7.1 task 1 | SC | No | 07 section 14.2 items b, c, e, g, h, i, j, k and l checked for the design response (section C below). Items h, e, g and b carry findings | | finding-7, finding-8, finding-10 |
| swe-134 7.1 task 4 | SC | Yes | The Si5351A bus is kept on its own RP2350 instance (request to 37 and 38). FC0 is a single counter shared by the ratio and the carrier checks, which is analysed and whose cross-attribution fails safe (verified above) | | none |
| swe-134 7.1 task 6 | SC | No | The claims about the HZ-008 C8 coverage of LOL_A and the REQ-SYS-154 unlocked trigger during transmission are not consistent with what the hazard analysis will need | | finding-9 |
| swe-205 7.1 task 1 | SC | No | Walked by action, inaction and incorrect action. New contributions not sent to the hazard writer: the stage supply left on in transmission (inaction); a stale FC0 result consumed on the abandon path (incorrect action) | | finding-10, finding-11 |
| swe-205 7.1 task 3 | SC | No | The squaring-stage supply switch is a new firmware function that bears on HZ-008, and it is assigned to no component | | finding-11 |
| swe-071 7.1 task 1 | SC | No | The planned verification of the K7 condition (M-1) does not cover the off-nominal case of a tail at the ramp | | finding-7 |
| swe-136 7.1 task 1 | | Yes | The new checker is class B, developer evidence, with the TV need stated (Evidence status row; section 6 item 1). It is not cited for credit | | none |
| swe-070 7.1 task 1 | | Yes | The thermal model is imported as developer evidence (WP-PDR-28a), and the crystal model is labelled Estimate, Low (section 6 item 9) | | none |
| swe-080 7.1 task 1 | SC | No | The impacts of the change on the other writers are listed in 14 requests; the SCL constraint misses the ADR-031 revision and the spur plan | | finding-12 |
| swe-080 7.1 task 2 | | Yes | `7593cea` carries `Refs:`; `tools/check_commit_msg.py --range 7593cea^..7593cea`: PASS (rows 24, 49). No class-CR row past its CR-from event | | none |
| swe-081 7.1 task 2 | SC | Yes | All product files are committed at `7593cea` on `main`. `hazards.json` stays under WP-PDR-16b; the note routes its K7 and C8 text there | | none |
| swe-087 7.1 task 2 | | Yes | INSP-056 Majors stay Verified. Its Minors 5 to 7 and 9, and this record's finding-1 to finding-6, are stated as unaddressed liens | | none |
| swe-088 7.1 task 1 | | N/A | The paired file review's WP-PDR-20a delta is not filed at `fd12ced`, so NPR 7150.2D 5.3.3 a to d cannot yet be checked for it (cross item X-6) | 07 section 10.2 (the paired reviews run as separate invocations; the lead SE dispatched both under plan row 20) | none |
| swe-089 7.1 task 1 | | Yes | This record carries the iteration 2 measurements | | none |

### Checklist items changed at iteration 2

| Id | Answer | Evidence |
|---|---|---|
| SA-A1 | Yes | 07 section 2.1.1 routes a product that constrains a safety-critical component; the SW-SAFE frequency verification unit and the `SW-SYNTH` word path (07 section 14.1, Proposed) |
| SA-A2 | Yes | The WP-PDR-20a author, the INSP-056 delta reviewer (not yet filed) and this reviewer are separate invocations |
| SA-A3 | Yes | This record names the `7593cea` blobs. INSP-056 names them when its delta is filed (X-6) |
| SA-A4 | N/A | The INSP-056 delta is not filed; checked at the next iteration (X-6) |
| SA-B1 to SA-B3 | Yes | Task table above; every No row carries a finding; one N/A row with its relief |
| SA-C-a | N/A | The delta adds no start or restart behaviour. `PA_EN` is refused after reset until the first verification (07 section 14.2), unchanged |
| SA-C-b | No | The changeover states (writes, gated wait, count, compare) are defined, but the gate condition does not implement the intended wait (finding-8) |
| SA-C-c | Yes | Every failed prerequisite ends with `PA_EN` not set; disagreement leads to Fault-safe (section 3.3, unchanged) |
| SA-C-d, SA-C-f | N/A | No override; no RAM safety state added |
| SA-C-e | No | The abandon of a refresh at t0 has no sequencing rule that binds the consumed result to the new count (finding-10 (i)) |
| SA-C-g | No | Ratio plausibility and the age at interval 12 are stated. There is no age ceiling at interval 13 and no stale-result check on the abandon path (finding-10) |
| SA-C-h | No | The `PA_EN` prerequisite set (count, LOL_A, age) rests on a count premise that does not cover the frequency at the ramp (finding-7) |
| SA-C-i | Yes | Every single software fault found here is ended by a second means within REQ-SYS-182's 100 ms (the interval-13 checks, 46 ms). No single event radiates at a wrong frequency beyond that |
| SA-C-j | No | Off-frequency: 46 ms, bounded. Unlocked during transmission: 30 ms only with U-2 option (a), unbounded by LOL_A with option (b) (finding-9) |
| SA-C-k | Yes | LOL_A still 1 at L_max, DIED and FAIL all give no `PA_EN` |
| SA-C-l | Yes | Fault-safe is reachable from every step of the changeover |
| SA-D1 | No | Two software contributions are not sent to WP-PDR-16b (finding-10 (i), finding-11) |
| SA-D2 | No | The note adds or moves no component, but the new squaring-stage supply switch is a firmware function assigned to none (finding-11) |
| SA-D3 to SA-D5 | N/A | No software requirement is written by this product; `traceability.py` 0 violations (Commands) |
| SA-D6 | No | K7 age wording and C8 LOL_A are requested; the C8 coverage statement must follow AN619 (finding-9) |
| SA-E1 | Yes | As swe-087 above |
| SA-E2 | Yes | Measurements below |
| SA-E3 | Yes | As swe-080 task 2 above |
| SA-E4 | N/A | No test or credit run |
| SA-F1 | Yes | One concern goes to WP-PDR-18 with tag `assurance` (X-8) |
| SA-F2, SA-F3 | Yes | Front matter and this section |

### Readiness (iteration 2)

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | Product committed and frozen | Yes | `git rev-parse 7593cea:<path>`, `HEAD:<path>` and `git hash-object` equal for the ten files. `git log 7593cea..HEAD` touches none of them |
| R2 | Product type and criticality | Yes | Section B row `trade-study-or-adr` applied (no analysis row in the template); safety-critical by the two Proposed 07 section 14.1 rows |
| R3 | `validate_docs.py`, `traceability.py --report-only` | Yes | See Commands |
| R4 | Paired file review filed; independence | Partly | Independence holds (C4 above). The INSP-056 delta is dispatched concurrently and not yet filed (X-6) |

### Cross items (iteration 2, for the lead SE; not findings on the note)

- **X-6.** The INSP-056 WP-PDR-20a delta is not filed at `fd12ced`. When it is, its reviewer names `paired_record: INSP-111` and this record's iteration 2 verdict (iteration 1 X-1 still applies: INSP-056 carries `assurance_verdict: pending` and no `paired_record`). SA-A3, SA-A4 and swe-088 task 1 are checked at the next iteration of this record.
- **X-7.** INSP-118 item (3) (`ts-012-design-to-cost-software-assurance.md`) states the same premise as finding-7 ("a PLL still settling gives a count outside T"). TS-012 section 7.3 cites it. Route the correction to the INSP-118 reviewer as a lien, and to WP-PDR-54 for the TS-012 text with the relock result.
- **X-8 (SA-F1).** Risk request to WP-PDR-18 (tag `assurance`; a new entry or a member of RSK-046, at the writer's choice): "Given the Si5351A relock after an MSNA change is not specified (the data sheet gives TRDY at most 10 ms from power-up as its only acquisition bound) and LOL_A is tied by AN619 to reference faults, there is a possibility that M-1 finds a settle, to the tolerance finding-7 asks for, above 3.35 ms, adversely impacting the A5 key-down sequence and the ICD-TX-SW timing table after WP-PDR-23a and 36a have used them, leading to the design change of section 3.4.1 (retune at the first key sample with a receive-restore path) late in the PDR or at CDR."
- **X-9.** Plan row 20 also puts the clk_sys 96 MHz `clock_plan.py` re-run and the ADR-031 revision in WP-PDR-20a (section 1 of the note says they are not in it). WP-PDR-20a reaches APPROVED only with that part and its INSP-111 delta. Finding-12's routing belongs there.
- **X-10.** Plan section 4.1 lets WP-PDR-32 and 36a use 20a once 20a is APPROVED. The fix for finding-7 is text plus an M-1 criterion, and it changes no pin; the ramp time in the 23a timing table may move only through the M-1 ladder, as the note already states. The delta can therefore be re-frozen and verified at once; nothing needs to wait for a calendar slot (owner direction, status note 2026-09-29 section 8).
- **X-11.** Minor findings 8 to 12 are raised before the delta's first APPROVED verdict. The author may fix them with finding-7, and any not fixed become liens at that verdict (rule C1). The next iteration of this record verifies finding-7 only.

### Commands (iteration 2)

- `git rev-parse 7593cea:<path>`, `git rev-parse HEAD:<path>`, `git hash-object <path>` for the ten product files: equal. `git merge-base --is-ancestor 7593cea main`: true. `git log --oneline 7593cea..HEAD`: `8d5bc0a`, `fd12ced`, neither touching a product file.
- `git archive 7593cea hardware/sim docs/design/analysis | tar -x -C <scratchpad>/exp`, then `.venv/bin/python hardware/sim/freq/r3_a5.py --run-id sa-rerun` there: exit 0, "RESULT: 23 pass, 0 fail, 10 info". `diff` of `checker-output.txt` with the run id normalized: identical. `cmp` of `results.json`: differs only at the `run_id` line. `cmp` of the script copy: identical. `freq_budget.py` in the same export: "RESULT: 35 pass, 0 fail".
- `shasum -a 256` of the two PDFs the web-fetch tool saved: `f3bc5285fccafa3fcd06e9a7fa6abb67fb43e8c23f6147b14caecc9a4851101f` and `0135b3a37195189e38cbd58ca504460814c691eeb1fdbe275806cfcd4783f36b`, equal to `r3_a5.py` SOURCES. `pdftotext -layout` into the scratchpad; Table 5 and AN619 Registers 0, 1 and 177 read as quoted above.
- `.venv/bin/python tools/check_commit_msg.py --range 7593cea^..7593cea`: "PASS 7593cea: rows 24, 49".
- `.venv/bin/python tools/traceability.py --report-only --output <scratchpad>/traceability-report.md`: "245 requirements, 173 test cases, 0 violation(s), 2 warning(s)" (REQ-SYS-125 and REQ-SYS-148, not touched by the note); `git status docs/vv` clean afterwards.
- `.venv/bin/python tools/validate_docs.py`: this record PASS; 110 passed, 7 failed, 117 checked. The 7 failures are records this delta does not touch, the same set as before this edit.

### Visual closure (iteration 2)

All four figures of the run were opened with the Read tool before this record cites them:
- `relock-sequence.png`: four timelines with PA_EN marks and the ramp bars; the fallback row's PA_EN is red at t0 + 11 ms against the ramp at t0 + 12 ms. The log panel shows TFREQ 0.01 ms, the 0.35, 1.35 and 3.35 ms settle budgets, and TRDY 2 and 10 ms. As in RL-4 to RL-7b.
- `ratio-freshness.png`: the MAIN-node traces near 2.3 to 2.6 K at 190 s under the 4.99 K band line. The drift bound rises to 6.12 ppm at W against the 1 and 6.5 ppm allocations and the 4.26 and 17.77 ppm ceilings, with A_kd = 10 s marked. As in FR-2 to FR-6.
- `xosc-slope.png`: the admitted curves inside the +/-30 ppm band, and the slope envelope inside +/-0.924 ppm/K over -10 to 65 C. As in FR-1.
- `r3-budget-and-buffer.png`: d of 4 518 and 3 332 Hz and T + d of 9 518 and 8 332 Hz, against the 5 and 10 kHz lines. The harmonic panel draws 1 x 25 to 6 x 25 MHz clear of every window. It does not draw 7 x 25 and 8 x 25 MHz, which BL-1 checks and which lie above the drawn windows. That is a display limit (the plot code draws lines up to 170 MHz), not a finding.

### Measurements (iteration 2)

Tasks in the table: 22 (21 applied, 1 N/A). Tasks answered No: 9. Checklist items answered No: 8 (SA-C-b, SA-C-e, SA-C-g, SA-C-h, SA-C-j, SA-D1, SA-D2, SA-D6). SWE-134 items checked: 9 (b, c, e, g, h, i, j, k, l; a, d and f N/A). New findings: 1 Major, 5 Minor, all Open. Record totals: 1 Major and 11 Minor, all Open. Renders inspected: 4. Effort: 45 turns, about 95 minutes.

### Verdict (iteration 2)

**Assurance verdict for the WP-PDR-20a delta: NEEDS CHANGES.** There is one Major finding, finding-7. The key-down count validates the mean frequency over its own 4 ms, not the frequency at the ramp. The measurement named to close revisit condition 1 cannot detect a settle tail. Section 3.1's budget does not carry a settle residual, and A5 makes one possible at every first element.

The rest of section 3.4 holds on the assurance side:
- the freshness split (A_kd 10 s at interval 12, 6.5 ppm at interval 13) with R-FRESH-1 and R-FRESH-2;
- the self-validating failure direction for the slewing part of a slow relock;
- the fail-safe cross-attribution on the single counter;
- the receive-only stage lines;
- the RL-6 result against the TS-012 fallback.

The five Minor findings (8 to 12) tighten the lock gate, the unlocked trigger, value freshness, the stage switch and the SCL routing. The record verdict stays NEEDS CHANGES.
