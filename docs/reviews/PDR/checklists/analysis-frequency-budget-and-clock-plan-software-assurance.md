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
# product_commit and product_files: equal to INSP-056 iteration 3 (readiness R1; rule C2). Each blob equals
# git rev-parse 4153acf:<path>, git rev-parse HEAD:<path> and git hash-object <path> at HEAD 8c57710 and
# again at 3aed3c4 (checked 2026-09-27); 4153acf is an ancestor of main, so no product blob is branch-only.
# The assurance lens is applied to ADR-031, the product file that routes this record (INSP-056 X-6); the
# other six blobs are read where ADR-031 rests on them
product_commit: "4153acf1006f919fc1e6ff72715f6f2694d9dead"
product_files: ["docs/design/analysis/frequency-budget.md@79d47fbbcae7fbfc5dde43ebde5c6e6b20917f94", "docs/design/analysis/clock-plan.md@07b5309613279d906bfdd3549618bb39ae8c7d81", "hardware/sim/freq/freq_budget.py@d82269e6e9a7b2312d85c227d29de55236cdacc5", "hardware/sim/freq/clock_plan.py@7e321b3d3355d8e94b464110292c3909483d3832", "docs/reviews/PDR/figures/frequency-budget.png@d77a0b3afac520643fdda042d188612b9123848e", "docs/reviews/PDR/figures/clock-plan-harmonics.png@0a4d221c1c1690aa28331d0c429e65278feacb07", "docs/decisions/adr/ADR-031-clock-plan.md@58ceb119651feeadfc79a4c3d61ecfa916fa52d4"]
# inputs read (not reviewed)
input_files: ["docs/reviews/PDR/checklists/analysis-frequency-budget-and-clock-plan.md (INSP-056, iteration 3, committed 7209bad)", "docs/reviews/PDR/checklists/ts-007-synthesizer-and-reference-software-assurance.md (INSP-074)", "docs/process/07-software-engineering-plan.md (sections 2.1.1, 14.1, 14.2)", "docs/safety/hazards.json 0.5.0-pha (HZ-002, HZ-007, HZ-008)", "docs/requirements/sys/requirements.json (REQ-SYS-034, 074, 082, 088, 093, 097, 099)", "docs/process/05-configuration-and-data-management.md (Table 4-1, sections 4.5, 9.1)", "docs/decisions/adr/ADR-051-wp-sw-11-clocks.md (header)", "docs/research/power-tree-and-charging.md (F14, F15, Baseline topology)", "docs/research/audio-output-and-hearing-safety.md (F1)", "docs/plan/pdr-work-plan.md (sections 5.1, 5.3)", "rustos docs/extracted/rp2350-datasheet.md at 2ec64c0f (git show only; section 8.1.1.2, Table 605)", "docs/references/md/swehb/ (swe-022, 027, 033, 039, 052, 057, 070, 080, 081, 087, 088, 089, 134, 136, 205 section 7.1)"]
paired_record: INSP-056
product_type: trade-study-or-adr
# criticality: safety-critical. ADR-031 section 2 item 9 adds a step, with a read-back and a fault path, to the
# WP-SW-11 clocks and PLL driver, which 07 section 14.1 lists in the row "Drivers these depend on" ("clocks and
# PLL (TICKS, XOSC, PLL_SYS: every timing budget depends on them)", criteria inherited) and 07 section 14.2
# allocates a, g, j, k ("pico2 clocks and PLL (WP-SW-11)"); item 4 fixes the SPI divisor of the SW-SYNTH
# frequency-word path (07 section 14.1 row "Frequency control, transmit frequency-word path", HZ-008)
criticality: safety-critical
product_size: 1 ADR (164 lines; 9 decision items, 4 options, 6 assumptions), read with clock-plan.md revision 2 (186 lines, rule 11) and the checker clock_plan.py (30 clock rows, 5 residual sources, 1 seeded case)
sprint: PDR-prep
author_agent: "author:WP-PDR-20 wave 1a (Claude as RF designer TX)"
reviewer_agent: "sa-reviewer:WP-PDR-20-insp-056-adr-031"
assurance_required: true
assurance_reviewer_agent: "sa-reviewer:WP-PDR-20-insp-056-adr-031 (software assurance function; paired file review INSP-056 by reviewer:WP-PDR-20-analysis-iter3, iterations 1 and 2 by reviewer:WP-PDR-20-analysis-iter1 and -iter2)"
iteration: 1
readiness_met: true
# reviewer_verdict and assurance_verdict: APPROVED at iteration 1 (rule C1): zero Major findings; six Minor
# findings. INSP-056, the file review of the same product, reached its first APPROVED verdict at iteration 3,
# so under rule C1 these Minor findings are liens due at the CDR readiness declaration and change no product now
reviewer_verdict: APPROVED
assurance_verdict: APPROVED
# verdict: set by Claude as software lead (07 section 10.2). Held at NEEDS CHANGES: the product blobs are on
# main, but the checklist applied exists only on cr/CR-012-pdr-checklist-templates (lead SE convention of
# 2026-09-27), and INSP-056 does not yet name this record (paired_record, assurance_reviewer_agent,
# assurance_verdict; each reviewer updates only its own record, cross item X-1). The software lead sets
# APPROVED on both records when INSP-056 carries the pairing and CR-012 merges with the template blobs
# unchanged (INSP-056 X-1 holds for the analysis template 0386cc6e as well)
verdict: NEEDS CHANGES
findings_major: 0
findings_minor: 6
findings_open: 6
findings_fixed: 0
findings_verified: 0
findings_deferred: 0
assurance_findings_major: 0
assurance_findings_minor: 6
assurance_tasks_applied: ["swe-134 7.1 task 5", "swe-022 7.1 task 1", "swe-033 7.1 task 1", "swe-033 7.1 task 2", "swe-033 7.1 task 3", "swe-039 7.1 task 4", "swe-057 7.1 task 2", "swe-134 7.1 task 4", "swe-134 7.1 task 6", "swe-136 7.1 task 1", "swe-070 7.1 task 1", "swe-205 7.1 task 3", "swe-205 7.1 task 1", "swe-134 7.1 task 1", "swe-052 7.1 task 2", "swe-080 7.1 task 1", "swe-080 7.1 task 2", "swe-081 7.1 task 2", "swe-087 7.1 task 2", "swe-088 7.1 task 1", "swe-089 7.1 task 1"]
swe134_items_checked: [a, c, e, g, h, i, j, k, l]
deferred_rids: []
items_no: ["swe-033 7.1 task 2", "swe-057 7.1 task 2", "swe-134 7.1 task 4", "swe-134 7.1 task 6", "swe-136 7.1 task 1", "swe-070 7.1 task 1", "swe-205 7.1 task 3", "swe-205 7.1 task 1", "swe-134 7.1 task 1", "swe-052 7.1 task 2", "swe-080 7.1 task 1", "swe-080 7.1 task 2", "swe-088 7.1 task 1", SA-A4, SA-C-e, SA-C-h, SA-C-j, SA-D1, SA-D2, SA-D6, SA-E3]
effort_turns: 40
effort_minutes: 70
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
