---
# Peer-review record front matter (charter sections 2 and 5; docs/process/01-lifecycle-and-reviews.md section 13
# is the single field list; docs/process/07-software-engineering-plan.md sections 2.1.1, 10.2 and 15).
# This is the paired software assurance record (07 section 10.2) of INSP-071
# (docs/reviews/PDR/checklists/analysis-keyer-host-study.md, reviewer:WP-PDR-33-keyer-host-study-iter1), at the
# record path PDR work plan WP-PDR-33 "Records" names and INSP-071 names in assurance_reviewer_agent and cross
# item X-2 ("SA for the keyer safety values").
# Checklist applied: docs/templates/peer-review-checklist-software-assurance.md revision A AS ON ITS CR-012 BRANCH
# (cr/CR-012-pdr-checklist-templates at 7784672, blob 5b13528504868b2add0f0b1e329c63aa2b54cdf4; CR-012 not merged,
# git merge-base --is-ancestor 7784672 main false on 2026-09-27). The `checklist` field names
# peer-review-checklist-design revision B, the checklist INSP-071 names, because tools/validate_docs.py fails a
# record whose `checklist` names a template absent from main, and the lead SE convention of 2026-09-27 does not
# change the validator. `assurance_checklist` names the template actually applied (the INSP-062 and INSP-074 form).
# id: INSP-075 is above every id on main at HEAD 9b20ea5 (highest INSP-074), on every cr/ branch and in the
# untracked records of the working tree (INSP-071 to INSP-073, pending renumbering by the lead SE)
id: INSP-075
checklist: peer-review-checklist-design
checklist_revision: B
assurance_checklist: "docs/templates/peer-review-checklist-software-assurance.md@5b13528504868b2add0f0b1e329c63aa2b54cdf4 (revision A, branch cr/CR-012-pdr-checklist-templates at 7784672)"
checklist_file: docs/reviews/PDR/checklists/analysis-keyer-host-study-software-assurance.md
product: docs/design/analysis/keyer-host-study.md
# product_commit and product_files (iteration 3 re-issue 1, the fourth pass, 2026-09-28): 7fe558a, the WP-PDR-33 revision 4 commit that
# answers finding-7 (freeze F0 again, rule C2). The 9 blobs equal git rev-parse 7fe558a:<path> and HEAD:<path> at
# HEAD 0caa0cc (0caa0cc touches only the thermal note); all are on main. product_files_iteration_3 keeps the
# b4a75a1 blobs of iteration 3, product_files_iteration_2 the 8c12b5a blobs and product_files_iteration_1 the
# 82cf086 blobs
product_commit: "7fe558ae628478805164b22278d1d56f1ce8ca72"
product_files: ["docs/design/analysis/keyer-host-study.md@32f4a1391a4db9aa266d3c3a602531c41f0f5e76", "docs/design/analysis/keyer-host-study/keyer_model.py@f67ced4261a1bf8890a996a1edd0b7499e7554f8", "docs/design/analysis/keyer-host-study/check_keyer_host_study.py@1de9aa64de5fd7afae73a15881464423e66a099f", "docs/design/analysis/keyer-host-study/keyer-host-study-results.json@1e91e0c031e40e40bc747928309dd4d6a0137bfa", "docs/design/analysis/keyer-host-study/keyer-nogap-fault-coverage.png@f5b4f5956dd5c08c6d49f79c7bd043ca14cd1188", "docs/design/analysis/keyer-host-study/keyer-nogap-short-interval.png@bc0cffb4f8cdafceb56c1debfe0a39491aeab64d", "docs/design/analysis/keyer-host-study/keyer-nogap-vs-speed.png@cd1b0bab427d9541ceaa5ae59502dd3110b6fc78", "docs/design/analysis/keyer-host-study/keyer-squeeze-timeline.png@e474a5ca3e1b7f3cd29a171a395d6e6ac278b103", "docs/design/analysis/keyer-host-study/keyer-squeeze-vs-speed.png@010c2daf423c684520478bdb4bf9862a1e96af0f"]
product_files_iteration_3: ["docs/design/analysis/keyer-host-study.md@a980ec5c1f1aa3f6537e8106c8ad5245be4d7996", "docs/design/analysis/keyer-host-study/keyer_model.py@b7fb84888661b6e3ac9198f29ff49eeb1cbea70b", "docs/design/analysis/keyer-host-study/check_keyer_host_study.py@3ac6e15b8282c7265fd7e81f242c6f1432e8df91", "docs/design/analysis/keyer-host-study/keyer-host-study-results.json@ed3d0c2221ebe546d044984d1ab31590fbb26867", "docs/design/analysis/keyer-host-study/keyer-nogap-fault-coverage.png@415dcfede13794998cfb2bf609d7c2f18c6704d5", "docs/design/analysis/keyer-host-study/keyer-nogap-vs-speed.png@4273d468d51717f15f171066d2f367499def28d5", "docs/design/analysis/keyer-host-study/keyer-squeeze-timeline.png@e474a5ca3e1b7f3cd29a171a395d6e6ac278b103", "docs/design/analysis/keyer-host-study/keyer-squeeze-vs-speed.png@010c2daf423c684520478bdb4bf9862a1e96af0f"]
product_files_iteration_2: ["docs/design/analysis/keyer-host-study.md@1dd0fb7d4c047e54e6bfabf73145ff1cd4c97590", "docs/design/analysis/keyer-host-study/keyer_model.py@d28613af318d2d7e0160973329512e2b88b71d98", "docs/design/analysis/keyer-host-study/check_keyer_host_study.py@f72f3a6ac5a6684f8a1b793a954dfb1f8b6ad524", "docs/design/analysis/keyer-host-study/keyer-host-study-results.json@7f4f0afdc013ffa43c124ff36c4d87de74a0ec97", "docs/design/analysis/keyer-host-study/keyer-nogap-fault-coverage.png@63395cf1c0eb4b9341f13f3259f00acba876091a", "docs/design/analysis/keyer-host-study/keyer-nogap-vs-speed.png@e9d3687accd75b5821b351e606922630d6ae5325", "docs/design/analysis/keyer-host-study/keyer-squeeze-timeline.png@e474a5ca3e1b7f3cd29a171a395d6e6ac278b103", "docs/design/analysis/keyer-host-study/keyer-squeeze-vs-speed.png@010c2daf423c684520478bdb4bf9862a1e96af0f"]
product_files_iteration_1: ["docs/design/analysis/keyer-host-study.md@39b43044230ce9513b525e6b4417b722d1eebe6d", "docs/design/analysis/keyer-host-study/keyer_model.py@39e6f92cffd45c9aa60d29fdd485633a6b77f748", "docs/design/analysis/keyer-host-study/check_keyer_host_study.py@0fda48d9630b4d85d90d6f5b17f3c67b277ae4c2", "docs/design/analysis/keyer-host-study/keyer-host-study-results.json@ef3d199da4f4bbb771de55e911f788b4ed024282", "docs/design/analysis/keyer-host-study/keyer-squeeze-vs-speed.png@010c2daf423c684520478bdb4bf9862a1e96af0f", "docs/design/analysis/keyer-host-study/keyer-nogap-vs-speed.png@514851a41e0b6f599bad00a350be87e3a4f44f3a", "docs/design/analysis/keyer-host-study/keyer-squeeze-timeline.png@e474a5ca3e1b7f3cd29a171a395d6e6ac278b103"]
# inputs read (not reviewed), blobs at HEAD 9b20ea5
input_files: ["docs/reviews/PDR/checklists/analysis-keyer-host-study.md@4cd9a95cfd17e9044599bb437dec3b3f41f89418 (INSP-071)", "docs/process/07-software-engineering-plan.md@bfe05f4327e79fa15c24d2cf8c14249804f946a8", "docs/process/03-software-classification-and-rmm.md@ed270f443e2ab648480017df8ad3d0221400cf4c", "docs/process/rmm.json@e326ddd1b7296d7d7fe172be6f33535cee3192d7", "docs/safety/hazards.json@81cacde47d4f2066ecac3947f3acf65e646b1ad0", "docs/safety/hazard-analysis.md@52c8ce16856499afc1b701e1ddb103788fcb1af9", "docs/requirements/sys/requirements.json@f128235ee109cdc325e37c32000ebf9d6027454d", "docs/requirements/sw/sw-keyer/requirements.json@f9141160c4d92ad80ae91144c2499b22292d4b16", "docs/plan/pdr-work-plan.md@bf0c9b6653162b91fe5fff8d55af2dfcb837001a", "docs/templates/peer-review-checklist-analysis.md@0386cc6e78da65578b1cce8b2f793cd3db224921 (CR-012 branch)"]
paired_record: INSP-071
# product_type: 07 section 2.1.1 has no row for a stand-alone analysis note (the analysis template on the CR-012
# branch, lines 55 to 62, says so). The dispatch is PDR work plan WP-PDR-33 ("SA for the keyer safety values").
# The note fixes design values of SW-KEYER and SW-SAFE (thresholds, the watchdog load, a build parameter, requests
# R-1 to R-3 to the firmware design), so the section B row `design` is applied, plus the tasks of every other SWE
# the note implements (swe-070 for the model, swe-205, swe-192, swe-052); cross item X-1
product_type: design
# criticality: 07 section 14.1 rows "Keyer and keying output" (SW-KEYER, line 589) and "Safe-state manager" with
# the TX_KEY no-gap and squeeze watchdog unit (SW-SAFE, line 594), both safety-critical
criticality: safety-critical
product_size: "1 note (276 lines, 12 sections), 1 model (631 lines), 1 checker (522 lines, 348 assertions), 1 results file, 3 plots; 10 requirement values; assurance lens on 4 changed or new safety values (REQ-SYS-054 gap, REQ-SYS-184 limit, watchdog load, manual-timeout build range) and 7 requests"
sprint: PDR-prep
author_agent: "author:WP-PDR-33 wave 1a (Claude as software lead, keyer)"
reviewer_agent: "sa-reviewer:WP-PDR-33-keyer-host-study (iteration 1); iteration 2 by sa-reviewer:WP-PDR-33-keyer-host-study-iter2 (independent; authored no part of WP-PDR-33 or its revision 2); iteration 3 by sa-reviewer:WP-PDR-33-keyer-host-study-iter3 (independent; authored no part of WP-PDR-33 or its revisions 2 and 3); iteration 3 re-issue 1 (fourth pass) by sa-reviewer:WP-PDR-33-keyer-host-study-iter4 (independent; authored no part of WP-PDR-33 or its revisions 2 to 4)"
assurance_required: true
assurance_reviewer_agent: "sa-reviewer:WP-PDR-33-keyer-host-study (software assurance function; paired file review INSP-071 by reviewer:WP-PDR-33-keyer-host-study-iter1)"
# iteration: stays 3 (validate_docs.py schema maximum; precedent INSP-009, INSP-038); the fourth pass of 2026-09-28 is
# the body section "Iteration 3 re-issue 1", and the rule C1 escalation is cross item X-7
iteration: 3
readiness_met: true
# reviewer_verdict and assurance_verdict (iteration 3 re-issue 1, the fourth pass, 2026-09-28): finding-1, finding-2, finding-6 and finding-7
# Verified; the new finding-8 (Major) is Open, so NEEDS CHANGES (07 section 10.2; PDR work plan rule C1)
reviewer_verdict: NEEDS CHANGES
assurance_verdict: NEEDS CHANGES
# verdict: set by Claude as software lead (07 section 10.2). NEEDS CHANGES: both this record and INSP-071 are
# NEEDS CHANGES. Even when both are APPROVED, the record verdict stays held until CR-012 merges with the template
# blob unchanged (lead SE convention of 2026-09-27, INSP-031 practice) and INSP-071 carries this pairing
verdict: NEEDS CHANGES
findings_major: 5
findings_minor: 3
findings_open: 4
findings_fixed: 0
findings_verified: 4
findings_deferred: 0
assurance_findings_major: 5
assurance_findings_minor: 3
assurance_tasks_applied: ["swe-134 7.1 task 5", "swe-022 7.1 task 1", "swe-057 7.1 task 2", "swe-058 7.1 task 1", "swe-058 7.1 task 2", "swe-058 7.1 task 3", "swe-058 7.1 task 4", "swe-058 7.1 task 5", "swe-134 7.1 task 1", "swe-134 7.1 task 4", "swe-134 7.1 task 6", "swe-205 7.1 task 3", "swe-052 7.1 task 1", "swe-070 7.1 task 1", "swe-192 7.1 task 1", "swe-205 7.1 task 1", "swe-205 7.1 task 4", "swe-205 7.1 task 5", "swe-052 7.1 task 2", "swe-087 7.1 task 1", "swe-088 7.1 task 1", "swe-089 7.1 task 1", "swe-081 7.1 task 2"]
swe134_items_checked: [a, d, f, g, h, i, j]
deferred_rids: []
items_no: ["swe-057 7.1 task 2", "swe-058 7.1 task 3", "swe-058 7.1 task 4", "swe-134 7.1 task 1", "swe-134 7.1 task 4", "swe-134 7.1 task 6", "swe-070 7.1 task 1", "swe-205 7.1 task 1", "swe-205 7.1 task 5", SA-C-f, SA-C-g, SA-C-i, SA-C-j, SA-D1, SA-D6, SA-F1, "iteration 2: swe-058 7.1 task 4 (finding-6)", "iteration 2: SA-C-i (finding-6)", "iteration 3: swe-058 7.1 task 4 (finding-7)", "iteration 3: SA-C-i (finding-7)", "iteration 3 re-issue 1: swe-058 7.1 task 4 (finding-8)", "iteration 3 re-issue 1: SA-C-i (finding-8)"]
effort_turns: 97
effort_minutes: 185
record_status: Open
date: 2026-09-27
date_closed: null
---

# Peer review record INSP-075: software assurance pair of INSP-071, keyer host study (WP-PDR-33, iteration 1)

**Product.** `docs/design/analysis/keyer-host-study.md` blob `39b43044` at freeze commit `82cf086` (freeze F0, rule C2), with the model `keyer_model.py` (`39e6f92c`), checker `check_keyer_host_study.py` (`0fda48d9`), results `keyer-host-study-results.json` (`ef3d199d`) and plots `keyer-squeeze-vs-speed.png` (`010c2daf`), `keyer-nogap-vs-speed.png` (`514851a4`), `keyer-squeeze-timeline.png` (`e474a5ca`). Every blob equals `git rev-parse 82cf086:<path>` and `HEAD:<path>` at HEAD `9b20ea5`; `git log 82cf086..HEAD` shows no later change to any product file. All blobs are on main, so the lead SE convention for branch-only blobs concerns only the checklist template. **Checklist applied:** `docs/templates/peer-review-checklist-software-assurance.md` revision A as on its CR-012 branch (blob `5b135285`, branch head `7784672`, not merged; see the front matter). **Paired record:** INSP-071 (committed `40e0d5e`, blob `4cd9a95c`), file reviewer `reviewer:WP-PDR-33-keyer-host-study-iter1`, reviewer verdict NEEDS CHANGES (1 Major, 3 Minor).

**Scope and acceptance criteria (rule C7).** Every task that section B assigns to the rows "Every product type" and `design`, and the section 7.1 tasks of the other SWEs the note implements (SWE-070 for the model, SWE-205, SWE-192, SWE-052, SWE-134 items). The SWE-134 items the proposed values touch (section C), checked against 07 section 14.2 rows a, d, f, g, h, i, j and the `SW-KEYER` and `SW-SAFE` module rows (07 lines 632 and 637). For every proposed or confirmed value: the fault side (the HZ-004 causes C1 to C10 and the `hazard-analysis.md` section 5 coverage rows 1 to 12 that the value controls), not only the false-trip side that INSP-071 covered; the independence of K4 that 07 section 14.1 line 594 and `hazards.json` HZ-004 K4 state ("run by the safe-state manager on the TX_KEY read-back and not by the keyer engine, so that a keyer fault that produces a stream does not also disable it", "whatever the element pattern"); the routing of every new software contribution to the hazard data writer (WP-PDR-16, plan section 5.3).

**Independence (rule C4; 07 section 2.1).** This invocation authored no part of the note, the model, the checker, the plots or the design data analysed, is not the file reviewer of INSP-071, and edited no product file. Author, file reviewer and assurance reviewer are three different invocations. INSP-071 was read first for the pairing only; the fault-side checks and counter-examples below are this reviewer's own.

**Search first (charter section 11 rule 1).** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: the 07 section 2.1.1 dispatch rows for analyses; the keyer speed range and the configuration guard field list). `grep -n` then only pinned lines in 07, 03, `hazard-analysis.md`, the plan, the SWEHB pages and the frozen model; Python extraction read the `hazards.json`, `rmm.json` and requirement rows. No rustos file was read.

## Record

### Findings

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | assurance | Major | swe-058 7.1 task 4; swe-134 7.1 tasks 1 and 6; SA-C-j; SA-D6 | Note section 6.2, lines 173 and 183 ("No rev A source produces one: the keyer never inserts a gap longer than one dit by itself"); section 3.4 line 90 (the count resets on a qualifying gap); section 8 row REQ-SYS-054 | The proposed REQ-SYS-054 gap (2 dit times) is shown only against fault streams from a correct keyer. K4 exists for keyer faults: `hazards.json` HZ-004 K4 runs it "not by the keyer engine, so that a keyer fault that produces a stream does not also disable it", "whatever the element pattern"; causes C4 (engine fault, "timeouts misconfigured") and C7 (corrupted keying state) and coverage rows 4, 6, 10 and 11 of `hazard-analysis.md` section 5 depend on it. The claim "the keyer never inserts a gap longer than one dit" assumes the engine the monitor guards. A space-timing or ratio fault that stretches the inter-element space to 2 dits or more makes every space a qualifying gap under the proposed rule. Because the model also resets the identical-element count on a qualifying gap, K4 (i) is defeated with (ii). Reviewer run of the frozen `paddle_watchdog` over 180 s: held-dit stream with 2-dit spaces, current rule trips at 30.24 s (5 WPM), 30.0 s (15), 18.34 s (25), 9.17 s (50), proposed rule never; alternating stream with 2-dit spaces, current rule 30.0 to 30.08 s at every speed, proposed never; 3-dit spaces at 15 to 50 WPM: current trips (12.2 to 30.1 s), proposed never. For these streams the firmware control column of rows 4 and 6 becomes "none" and only K12 at 150 to 180 s remains, which changes a safety conclusion that the owner as SMA TA would rule on (plan rule C10). INSP-071 finding-1 covers the other side (false trips in Bug and Straight sending) and is not raised again. Fix: analyse the missed-detection side for keyer-fault streams (space stretched by a factor up to the largest the gap threshold admits, ratio and weight corruption, a stuck element timer) under the current and the proposed rule, at 5 to 50 WPM. Then either choose a gap rule, with a count that a sub-word gap does not reset, that keeps these streams caught and still passes the correct-sending corpus, or state the coverage given up as a residual and route it to WP-PDR-16 for the section 5 coverage table and the section 8 fault trees, so that it appears in the CR and its impact review (rule C6) | Verified (iteration 2, 8c12b5a) | Pending | |
| <a id="finding-2"></a>finding-2 | assurance | Major | swe-057 7.1 task 2; swe-134 7.1 tasks 1 and 4; swe-205 7.1 task 1; SA-C-f, SA-C-g, SA-C-i | Note section 8 rows REQ-SYS-054 and REQ-SYS-184 ("at the selected speed"); sections 6.1 and 6.2; section 9 (no request names the speed source) | Both changed values are in dit times at the selected speed, so the `SW-SAFE` monitor, which 07 section 14.1 line 594 places outside the keyer "so that a keyer-engine fault cannot disable it", now depends on a keyer parameter. The note does not state where `SW-SAFE` reads the speed or how that value is protected. The keyer speed is not in the configuration guard's field list (03 section 4.3 line 176 and 07 section 14.1 line 596: "power step, tune level, guest lock, frequency calibration, thermal thresholds, keyer mode, debounce"). Its range checks REQ-SW-KEYER-015 and REQ-SW-KEYER-037 are in the monitored keyer and carry no `hazard_ids`. Reviewer run of the frozen model with a monitor speed value higher than the stream speed: 5 WPM stream with the monitor at 11 or 15 WPM, 10 WPM with 25, 20 WPM with 50, held and alternating. The current rule trips at 15.3 to 30.0 s. The proposed rule never trips, because a monitor value more than twice the true element rate makes every 1-dit space a qualifying gap. In the other direction a value below the 5 WPM floor lengthens the squeeze stop past the note's 4.80 s bound (20 dits: 6.0 s at 4 WPM, 24 s at 1 WPM), and a zero speed has no defined limit. So one corrupted or mismatched value disables K4 (i) and (ii) (SWE-134 i, single event), and neither the note, the hazard data nor any request names this software contribution (SWEHB `swe-205` section 7.7.2 considerations 15 and 16, independence and common cause). Fix: state in the proposed CR wording and in section 9 that `SW-SAFE` takes the speed from the configuration-guarded record, held with its complement and range-checked 5 to 50 WPM (SWE-134 f and g), or derives the dit length from the TX_KEY read-back itself. Bound the fault-side stop times at the range ends and for a mismatched value. Send the field-list change to the 03 and 07 writer (WP-PDR-17) and the new cause to WP-PDR-16 | Verified (iteration 2, 8c12b5a) | Pending | |
| <a id="finding-3"></a>finding-3 | assurance | Minor | swe-134 7.1 task 6; SA-D6 | Note section 9, first bullet ("CR triggers", line 245) | The CR trigger list names the requirements, mirrors, HZ-004 K4, ConOps, concept, TC-SYS-038 and ICD-CTL-KEY. It omits the texts that hold the same numbers as SWE-134 item j provisions: `hazard-analysis.md` section 7 row j ("30 s without a 7-dit or 500 ms gap, squeeze 2 s"), which 07 section 14.2 makes the governing text for provision numbers, and its section 5 coverage rows 4 and 5; 07 section 14.2 row j (line 624, the same values) and the `SW-SAFE` module row (line 637, "with the row j values"); and the reserved REQ-SW-SAFE-010 child. If the CR follows the list as written, the SWE-134 j provision and the hazard analysis would disagree with REQ-SYS-054 and REQ-SYS-184. Fix: add these texts, with their writers (WP-PDR-16; the 07 writer WP-PDR-47; WP-PDR-35), to the section 9 list | Open | Pending | |
| <a id="finding-4"></a>finding-4 | assurance | Minor | swe-205 7.1 task 1; SA-C-j; SA-D1 | Note section 6.5 (line 195) and request R-2 (line 247) | The note finds that a configuration-store sector update stops the processor for 0.407 s with interrupts masked and XIP off (A-7). During that time every safety monitor stops, not only the 1 kHz key sampler: the software contribution is by inaction. R-2 constrains only Transmit-keyed and key-closed states and goes to the firmware design writers (WP-PDR-32, WP-PDR-41). It does not go to the hazard data writer (WP-PDR-16) or to the SW-SAFE requirement writer (WP-PDR-35), and the stall is not compared with the other 07 section 14.2 row j budgets that are shorter than 0.407 s (REQ-SYS-004 carrier end 20 ms, thermal 100 ms, audio fault mute 10 ms, charge disable within one supervision period). RSK-021 covers a hang or corruption during the write, not the monitor stall. Fix: route R-2 to WP-PDR-16 as a candidate software cause and to WP-PDR-35 as a `SW-SAFE` constraint (no store write outside Receive with PA off and the key inputs open), and state which row j budgets are active in the states where a write is allowed | Open | Pending | |
| <a id="finding-5"></a>finding-5 | assurance | Minor | swe-070 7.1 task 1; SA-F1 | Note section 10 (line 262, "owner action proposed in the author's return"); header row "Credit" | The model has no TV record. `rmm.json` SWE-070 (FC) plans "the validation evidence (TV-NNN) of ... the Python checkers" for PDR, so the proposed safety values would reach the owner on an unaccredited model unless a TV record exists or the owner rules on developer evidence. The note states that condition correctly. INSP-071 routes it as cross item X-1. No owner action is in plan section 6.1, and no assurance risk entry exists. The assurance lens raises it as a finding, because the values set safety-critical `SW-KEYER` and `SW-SAFE` thresholds. Fix: before B2, either file a class B TV record for `keyer_model.py` (the F6 and F7 golden vectors as the known-answer test and a seeded fault; 05 section 9.1) or add the owner action to plan section 6.1. In both cases submit the concern to the risk register writer (WP-PDR-18) as an entry tagged `assurance` | Open | Pending | |
| <a id="finding-6"></a>finding-6 | assurance (iteration 2) | Major | swe-058 7.1 task 4; swe-134 7.1 task 1; swe-205 7.1 task 1; SA-C-i, SA-C-j | Note section 6.2 revision 2 table row "Reference interval r" and "Coverage given up (residual ...)"; section 8 row REQ-SYS-054 ("Residual: text-like fault streams"); section 9 R-8 (a); `keyer_model.watchdog_relative` (no lower bound on r) | Revision 2 takes r as the shortest key-up interval on TX_KEY in the preceding 10 s with no lower bound (only the 1 ms read-back quantisation). One short key-up interval therefore sets r for 10 s: every normal space becomes a qualifying gap (item (ii) never runs out) and a word gap (item (i-a) resets at every element), and the interval breaks the pattern that (i-b) matches. Reviewer runs of the frozen `watchdog_relative` over 180 s: a held-dit stream, an alternating stream and a held-dit stream with 2-dit spaces, each with one 1 ms key-up glitch inside an element every 5 s, are not stopped by K4 at 5, 15, 25 or 50 WPM (12 of 12 cases); the current rule (`paddle_watchdog`, `gap_rule_current`) stops all 12 at 6.07 to 30.24 s. With the glitch every 2 s or 9 s, 23 of 24 cases escape (one stops, 50 WPM held dit every 9 s, by count at 6.12 s). Without any glitch, one inter-element space shortened to 0.4 dit every 5 s lets the alternating stream escape at every speed, where the current rule stops it at 9.18 to 30.0 s. These streams are periodic keyer-fault streams, not text-like ones, so they fall outside the residual the note states and routes (R-8 (a)) and contradict "Revision 2 stops every periodic and equal-element stream". A short key-up interval on the read-back can come from the fault that makes the stream (timing or ratio corruption) or from a read-back disturbance while transmitting, so the defeat needs no second independent event. For them the firmware control column of `hazard-analysis.md` section 5 rows 4, 6 and 10 becomes "none" and only K12 (150 to 180 s) remains, a regression against the current rule that the owner would rule on unaware (rule C10). Fix: bound r from below (for example a floor at or above the shortest space a correct keyer at 50 WPM can emit, and read-back intervals below a stated minimum treated as no gap and not as a reference), or take r from a robust statistic of the window rather than its minimum. Re-run the fault catalogue with short-interval variants (a 1 ms glitch and a shortened space at intervals of 1 to 10 s) and the correct-sending corpora P, B and S, and state any remaining short-interval residual in section 6.2, section 8 and R-8 | Verified (iteration 3, b4a75a1) | Pending | |
| <a id="finding-7"></a>finding-7 | assurance (iteration 3) | Major | swe-058 7.1 task 4; swe-134 7.1 task 1; swe-205 7.1 task 1; SA-C-i, SA-C-j | Note revision 3 section 6.2 line 213 ("so a rare short interval, from a fault or a disturbance, no longer sets r"), line 246 ("Every variant with a short interval every 5 s or more is stopped at every speed"), line 248 residual class (3) ("needs a short interval at least every 3 s at 5 WPM", "none missed at 15 WPM and above", "11 of 384 missed and 8 stopped late (39.1 to 117.2 s)", "A single short interval, or short intervals every 5 s or more, no longer defeats K4"); section 8 row REQ-SYS-054; section 9 R-8 (a) | The lower quartile resists a rare short interval only when a 10 s window holds many key-up intervals. At 5 WPM a periodic fault stream holds 7 to 21 of them, and one spurious key-down element of 10 ms or more (above `GLITCH_MS`, so an element, not a glitch pulse) splits a space into two short key-up intervals. Two such elements in 10 s, one every 5 s, or one every 9 s in the slower streams, make the short parts the lower quartile: r drops to about half a dit, every normal space becomes a qualifying gap, and the extra element breaks the (i-a) and (i-b) runs. Reviewer runs of the frozen `watchdog_relative` (b4a75a1) over 300 s from an idle key, with a key-down pulse of 10, 11, 15, 30 or 60 ms in the middle of a space every 5 s or every 9 s: the alternating, held-dit 2-dit-space and held-dah streams at 5 WPM are not stopped by K4 (30 of 30 pulse lengths and rates; share of short intervals 0.25 to 0.43). The current rule stops all of them at 30.0 to 30.24 s. The same pulse every 1 or 2 s escapes at 15 WPM (held dit, alternating, 2-dit spaces, held dah) and at 25 WPM (alternating, 2-dit spaces, held dah). Key-up breaks of 10 ms and 12 ms escape at 5 WPM every 1 s in all four streams and every 2 s in three. A space shortened to 0.4 dit every 4 s stops the 5 WPM held-dah stream only at 118.46 s. These cases lie inside the formal class (3) definition (the share reaches 0.25), so the residual as defined is not exceeded. But the note tells the owner that class (3) needs a short interval at least every 3 s at 5 WPM, that none is missed at 15 WPM and above, that 11 of 384 variants escape, and that short intervals every 5 s or more no longer defeat K4. A single spurious element every 9 s defeats K4 items (i) and (ii) at 5 WPM, a lower rate than the finding-6 case (every 5 s), and the element can come from the fault that makes the stream, so no second independent event is needed. The owner ruling on class (3) (rule C10) and the R-8 (a) routing to WP-PDR-16 would rest on that understatement. The 384-variant catalogue inserts only intervals that add one short key-up interval (the 1 ms key-down pulse is filtered), so it never tests an unfiltered spurious element. Fix: add key-down pulses from `GLITCH_MS` to at least one dit (and key-up breaks of 10 to 15 ms) every 1 to 10 s to the short-interval variants. Then either make the reference robust at low interval counts (for example a minimum number of intervals in the reference set, a longer reference window at low interval counts, or excluding the two parts of a space split by an element shorter than a stated fraction of r), or restate class (3) in sections 6.2 and 8, R-8 (a) and the CR wording with the rate and speed bounds the runs show, and withdraw the "rare short interval" and "every 5 s or more" statements | Verified (iteration 4, 7fe558a) | Pending | |
| <a id="finding-8"></a>finding-8 | assurance (iteration 4) | Major | swe-058 7.1 task 4; swe-134 7.1 task 1; swe-205 7.1 task 1; SA-C-i, SA-C-j | Note revision 4 section 6.2 table row "Split filter" and the paragraph after the table ("Taking the smaller of r and e keeps the filter off the elements of a stream whose spaces are more than twice its elements"); residual classes (1) to (3); section 7 row "Keyer-fault streams" ("revision 4 stops ... every periodic stream"); section 8 row REQ-SYS-054; R-8 (a); `keyer_model.watchdog_relative` split test (`SPLIT_FRAC`, `REF_MIN_N`, `kd_now`) | The split filter hides a key-down of 10 ms or more that is shorter than half the smaller of r and e (e: lower quartile of the key-down durations of 10 s). In a periodic keyer-fault stream whose shortest element is a quarter or less of its elements and whose spaces are longer than that element, the shortest element is a regular element of the stream, not a spurious one, yet it lies near the split threshold. As the 10 s window slides, e moves between that element and the longer ones, so the filter hides the element in some cycles and not in others. Each change breaks the (i-b) period run; the (i-a) equal-element run is broken by the other elements; and qualifying gaps (2 r or more) inside the cycle restart the (ii) window. The note does not analyse the filter on such streams. The catalogue and the 1568 variants hold none, and the checker asserts "rev4 stops every variant that rev3 stops" only over the variants. Reviewer run of the frozen 7fe558a model (`probe6.py`): 1500 random periodic cycles of 2 to 6 elements (element 0.5 to 6 dits, space 1 to 9 dits), at 5, 15, 25 and 50 WPM, over 300 s from an idle key. Revision 4 stops 1376 and revision 3 stops 1393. Revision 4 misses 17 that revision 3 stops; 11 of these revision 3 stops before the 150 s K12 floor, and the current rule stops 4 of them at 30.0 to 30.16 s. Revision 4 stops 30 more later than both revision 3 and 30 s plus one cycle; the current rule stops 5 of these at 30.0 to 30.08 s, and revision 4 only at 30.95 to 95.56 s (four of the five after 72 s). Revision 4 stops none that revision 3 misses, and all 47 have split pulses. Examples, with the cycle as (element, space) in dits: (3,1) (2,2.5) (2,3) (3,5) (0.5,2) at 15 WPM, current 30.0 s, revision 3 49.32 s, revision 4 never. (6,2) (3,3) (1,5) (4,5) (4,2.5) at 15 WPM, with a full dit as the shortest element: current 30.0 s, revision 3 72.92 s, revision 4 never (26 split pulses in 300 s, about a quarter of its dits). (3,2) (3,7) (0.5,3) (3,7) (3,1) at 50 WPM: revision 3 20.02 s, revision 4 never. A hand-built cycle (`probe5.py`) of three dahs and a dit, with 3-dit spaces and a 7-dit gap after the dit, is stopped by revision 4 at 50 WPM only at 30.02 s (revision 3: 20.04 s) and at 5 WPM at 270.5 s (revision 3: 200.4 s). These streams repeat with a period of 1 to 6 elements and have no short key-up interval. They are therefore in none of residual classes (1) to (3), and they contradict section 7 ("every periodic stream"). One keyer fault (a ratio, weight or pattern fault) produces the stream, so no second event is needed. For these streams the firmware control column of `hazard-analysis.md` section 5 rows 4, 6 and 10 becomes "none", and only K12 (150 to 180 s) remains. That is a regression against revision 3, and in part against the current rule, on which the owner would rule unaware (rule C10). Fix: make the split decision independent of the element pattern of a periodic stream. Examples: split a pulse only when each of its two key-up parts is shorter than half r; split it only when it is shorter than half the shortest element that recurs in the window; or do not let a split pulse break an (i-b) run whose period holds without it. Otherwise state this class as a fourth residual, with its extent, and route it. In both cases, add periodic cycles with a minority short element and long spaces to the catalogue, and assert revision 4 against revision 3 over a randomised periodic set as well as over the variants | Open | Pending | |

Two Major findings: `assurance_verdict` NEEDS CHANGES (07 section 10.2; rule C1). The interlock (REQ-SYS-052, REQ-SW-KEYER-022), manual-closure timeout (REQ-SYS-053, REQ-SW-KEYER-026), hang recovery with a 1.0 s load (REQ-SYS-131), bench and tone timeouts (REQ-SYS-188, REQ-SYS-189), plug presence (REQ-SW-KEYER-036) and the 128 count and 30 s window stand from the assurance lens. The findings bound only the changed REQ-SYS-054 gap and REQ-SYS-184 limit, and their routing. Concurrence with INSP-071: finding-1 (Bug and Straight scope) at Major, unchanged by the assurance lens; findings 2 to 4 at Minor.

### Task table

| Task | Safety-critical designation (SWEHB 8.10 section 6) | Applied | Result and evidence | Relief (N/A only) | Finding ids |
|---|---|---|---|---|---|
| swe-134 7.1 task 5 (every type) | SC | Yes | This record is the assurance participation in the review of a product that sets `SW-KEYER` and `SW-SAFE` safety values (07 section 14.1 lines 589 and 594) | | none |
| swe-022 7.1 task 1 (every type) | SC | Yes | Performed against the software assurance plan, 07 section 15, by this review | NASA-STD-8739.8 part: `rmm.json` SWE-022 T (standard not in the corpus) | none |
| swe-057 7.1 task 1 (design) | | N/A | The note has no architecture content | 07 section 2.1.1 row "Design": the architecture product is the software section of `docs/design/architecture.md` (WP-PDR-32), reviewed with SA in plan wave 2a | |
| swe-057 7.1 task 2 (design) | | No | The K4 placement in `SW-SAFE` meets its safety purpose only if its thresholds do not depend on keyer data; the proposed values make them depend on the keyer speed with no stated source | | finding-2 |
| swe-058 7.1 task 1 (design) | | Yes | Each value was checked against its requirement text, `tbr.plan` and verification note. The gaps are INSP-071 finding-1 and finding-2 (concurred) and finding-3 here | | finding-3 |
| swe-058 7.1 task 2 (design) | | Yes | R-1 (load 1.0 s, fed only after every monitor ran) agrees with the 07 section 14.2 `SW-SCHED` row (j) and REQ-SYS-131. R-2 agrees with the masked-write rule of `peer-review-checklist-design.md` CK-DES-D9. The note defines no code units, and none is needed at analysis maturity | | none |
| swe-058 7.1 task 3 (design) | | No | The proposed gap rule adds an undesired behaviour: missed detection of keyer-fault streams with 2-dit or longer spaces | | finding-1 |
| swe-058 7.1 task 4 (design) | SC | No | K4 "whatever the element pattern" is not kept for the fault class the monitor exists for | | finding-1 |
| swe-058 7.1 task 5 (design) | | Yes | This record's own design analysis: fault-side runs of the frozen model (Commands) and the speed-mismatch case | | finding-1, finding-2 |
| swe-134 7.1 task 1 (design) | SC | No | Section C: items f, g, i, j are not met by the proposed values as stated | | finding-1, finding-2 |
| swe-134 7.1 task 4 (design) | SC | No | Logical isolation of the `SW-SAFE` monitor data from the keyer data is not stated for the speed value | | finding-2 |
| swe-134 7.1 task 6 (design) | SC | No | The proposed values would disagree with `hazard-analysis.md` section 5 rows 4 and 6 and section 7 row j unless the hazard analysis changes with them. The trigger list omits those texts | | finding-1, finding-3, finding-4 |
| swe-143 7.1 task 1 (design) | | N/A | No architecture review is held on this product | 07 section 2.1.1 row "Design": the SWE-143 review is plan wave 2a "architecture review iteration 1 (SWE-143 with SA)" | |
| swe-205 7.1 task 3 (design) | SC | Yes | The note adds or moves no component; `SW-KEYER` and `SW-SAFE` as in 07 section 14.1 | | none |
| swe-052 7.1 task 1 (design) | | Yes | Section 1 traces every value to its requirement, `tbr.plan` and hazard control; no code exists at this maturity | | none |
| swe-070 7.1 task 1 (model) | | No | `keyer_model.py` is neither validated nor accredited (no TV record). The note marks every result as developer evidence (05 section 9.1). The `rmm.json` SWE-070 PDR plan is not met, and no owner action is recorded | | finding-5 |
| swe-136 7.1 task 1 | | N/A | matplotlib renders plots only (class C); the venv interpreter is TV-001; the model is assessed under swe-070 | 07 section 17.3 and 05 section 9.1 class C | |
| swe-192 7.1 task 1 | SC | Yes | REQ-SYS-052, 053, 054, 131, 184, 188, 189 and REQ-SW-KEYER-022, 026, 036 have method Test with closing cases (TC-SYS-038 and others). R3 run: 0 violations, no HAZARD_REQ_NOT_TESTED. Note section 10 claims no closure | | none |
| swe-205 7.1 task 1 | SC | No | Two software contributions found by or introduced with the note are not routed to the hazard data: the speed value on which K4 depends, and the 0.407 s stall of every monitor | | finding-2, finding-4 |
| swe-205 7.1 task 4 | SC | Yes | Section D, SA-D3 | | none |
| swe-205 7.1 task 5 | SC | No | The software safety analysis update for the changed K4 coverage is not requested | | finding-1, finding-3 |
| swe-052 7.1 task 2 | SC | Yes | Section D, SA-D3: HZ-004 K1, K3, K4, K7, K9, K13 and HZ-005 K9 trace to the requirements and back | | none |
| swe-134 7.1 task 3 | SC | N/A | Values of safety-critical loaded data are tested at the test products; the note proposes that the keyer speed becomes one (finding-2) | 07 section 9.7 (loaded data, SWE-193 cases) | |
| swe-087 7.1 task 1 | | Yes | INSP-071 and this record are the peer review of the product, reported in `docs/reviews/PDR/checklists/` | | none |
| swe-087 7.1 task 2, swe-088 7.1 task 2 | | N/A | Iteration 1: no finding is accepted or fixed yet | 07 section 10.2 (fixes verified in the delta iteration) | |
| swe-088 7.1 task 1 | | Yes | Section A, SA-A4 | | none |
| swe-089 7.1 task 1 | | Yes | Section E, SA-E2 | | none |
| swe-081 7.1 task 2 | SC | Yes | The product is committed on main at `82cf086`; `hazards.json` and `hazard-analysis.md` are under CM (05 Table 4-1) | | none |

## Readiness criteria

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | Frozen, and the same blobs as the paired record | Yes | `git rev-parse 82cf086:<path>` and `HEAD:<path>` equal each of the 7 blobs of INSP-071 `product_files` |
| R2 | Row and criticality identified | Yes | `product_type` design and `criticality` safety-critical from 07 section 14.1 lines 589 and 594; routing by plan WP-PDR-33 (X-1) |
| R3 | validate_docs and traceability clean for the ids touched | Yes | `tools/traceability.py --report-only --output <scratch>/traceability-report.md`: 245 requirements, 173 test cases, 0 violations, 2 warnings (REQ-SYS-125, REQ-SYS-148 SYS_UNALLOCATED, not ids of this product); `docs/vv/` unchanged. `validate_docs.py` run before commit |
| R4 | Paired review filed by its own invocation; this reviewer independent | Yes | INSP-071 `author_agent` and `reviewer_agent` differ from this invocation |

## A. Dispatch, independence and record integrity

| Id | Answer | Evidence |
|---|---|---|
| SA-A1 | Yes, with X-1 | Routed by PDR work plan WP-PDR-33 ("SA for the keyer safety values", plan line 573). 07 section 2.1.1 (lines 110 to 127) has no row for a stand-alone analysis note, and the analysis template on the CR-012 branch (lines 55 to 62) sets `assurance_required: false` for one. INSP-071 sets it true. The component rows are 07 section 14.1 lines 589 (`SW-KEYER`) and 594 (`SW-SAFE` no-gap and squeeze watchdog), safety-critical. The dispatch gap goes to the software lead as cross item X-1 (the template routes a gap that way) |
| SA-A2 | Yes | Three invocations: author `author:WP-PDR-33 wave 1a`, file reviewer `reviewer:WP-PDR-33-keyer-host-study-iter1`, this reviewer |
| SA-A3 | Yes | Same `product`, `product_commit` `82cf086` and 7 blobs as INSP-071 |
| SA-A4 | Yes | INSP-071 applied the analysis checklist revision A (CR-012 branch blob `0386cc6e`, the checklist the CR-012 file table assigns to analyses), answered every item of R, A to F, G6, G7, H, I, J with evidence and a 25-row per-case table, and recorded the re-run (CK-ANA-C4) and hand checks (CK-ANA-B5). SWE-088 criteria a to d are met: checklist, readiness, findings with state, participants named |

## B. SWE-to-task table

| Id | Answer | Evidence |
|---|---|---|
| SA-B1 | Yes | Task table: row "Every product type", row `design`, and the tasks of SWE-070, SWE-136, SWE-192, SWE-205, SWE-052, SWE-134 task 3, SWE-087, SWE-088, SWE-089 and SWE-081 that the note or its review implements. `assurance_tasks_applied` lists every Yes and No row |
| SA-B2 | Yes | N/A rows cite 07 section 2.1.1 row "Design", 07 section 17.3 with 05 section 9.1, 07 section 9.7 and 07 section 10.2. The only SC task answered N/A is swe-134 task 3, relieved by 07 section 9.7 |
| SA-B3 | Yes | Every No row cites a finding |

## C. SWE-134 items a to l (07 section 14.2; `SW-KEYER` and `SW-SAFE` module rows)

| Id | Answer | Evidence |
|---|---|---|
| SA-C-a | Yes | The interlock of 500 consecutive open samples after boot, reset and mode change (note section 6.3) meets row a and the `SW-KEYER` row (a; REQ-SYS-052). Reviewer re-run of the checker: the `interlock` cases pass |
| SA-C-b | N/A | The note sets no state or transition; the `match (state, event)` design is WP-PDR-32 and WP-PDR-41 work |
| SA-C-c | N/A | No termination path is set by the note |
| SA-C-d | Yes | The manual-closure timeout range 2 to 6 s becomes a build parameter, not an operator setting (section 6.4, R-6). This keeps row d ("Rev A offers no override of ... the key-down timeouts") |
| SA-C-e | N/A | No command sequencing is set by the note |
| SA-C-f | No | The proposed thresholds make the keyer speed a value on which K4 depends, and its complement storage and guard are not stated (finding-2) |
| SA-C-g | No | The plug-presence coverage limit is recorded (R-4). The speed input to the monitor has no stated range or plausibility check in `SW-SAFE` (finding-2) |
| SA-C-h | Yes | The timeouts and watchdogs "not expired" remain `PA_EN` prerequisites (row h), unaffected by the values |
| SA-C-i | No | One corrupted or mismatched speed value disables K4 (i) and (ii) under the proposed rule (finding-2). A keyer space-timing fault escapes K4 (finding-1) |
| SA-C-j | No | Response times for REQ-SYS-052, 053, 131, 188, 189 and the squeeze stop for a correct keyer are bounded with margins (sections 6.1, 6.3 to 6.6). The K4 response to keyer-fault streams is lost under the proposed gap (finding-1). The 0.407 s monitor stall is not compared with the other row j budgets (finding-4) |
| SA-C-k | N/A | No error path is set by the note |
| SA-C-l | N/A | The monitors end keying; entry to the safe state is not set by the note |

## D. Software safety analysis and hazard traceability

| Id | Answer | Evidence |
|---|---|---|
| SA-D1 | No | SWEHB `swe-205` section 7.7.2 walked. Considerations 6 and 10 (monitoring and interlocks: K1, K3, K4) apply and are addressed. Considerations 14, 15 and 16 (new hazard causes, independence of the controls, common cause) apply to the proposed values and are not addressed (finding-1, finding-2). Consideration 27 (analysis software leading to safety decisions) applies to the unaccredited model (finding-5). The monitor stall is an inaction contribution not routed (finding-4) |
| SA-D2 | Yes | The note changes no component or criterion; 07 section 14.1 and 03 section 4.3 unchanged |
| SA-D3 | Yes | R3: 0 violations, no `HAZARD_CONTROL_UNTRACED` or `HAZARD_INVERSE`. HZ-004 K4 `control_req_ids` REQ-SYS-054, REQ-SYS-184 and the K1, K3, K7, K9 lists match the requirements' `hazard_ids` |
| SA-D4 | Yes | REQ-SW-KEYER-022, 026 and 036 carry `Depends on:` items naming REQ-SYS-119, REQ-SYS-055, REQ-TX-014, ICD-CTL-KEY section 3.2.5 and OPS-013 |
| SA-D5 | Yes | Every hazard-tracing requirement in scope has a closing Test case (R3; `rmm.json` SWE-192 FC) |
| SA-D6 | No | The hazard analysis update that the proposed values need (section 5 rows 4 to 6, section 7 row j, the section 8 fault tree of HZ-004) is not requested (finding-1, finding-3) |

## E. Peer review, change and configuration assurance

| Id | Answer | Evidence |
|---|---|---|
| SA-E1 | N/A | First review of the product; no earlier findings |
| SA-E2 | Yes | INSP-071 and this record carry the SWE-089 fields of 07 section 10.3 (findings by severity and state, items answered No, effort, size) |
| SA-E3 | Yes | `git show --stat 82cf086` adds only the WP-PDR-33 product files. No requirement, hazard or ICD file is edited, so no CR route applied. The changes go out as the PCR-8 and PCR-9 triggers of plan section 6.2 |
| SA-E4 | N/A | No test is run for credit; the checker is developer evidence (finding-5) |

## F. Assurance risks, metrics and reporting

| Id | Answer | Evidence |
|---|---|---|
| SA-F1 | No | The model-accreditation concern is not submitted as an `assurance` risk entry (finding-5). The other concerns are product defects (findings 1 to 4) |
| SA-F2 | Yes | Front matter: `assurance_findings_major` 2, `assurance_findings_minor` 3, `items_no`, effort |
| SA-F3 | Yes | Verdict, open findings, tasks applied and reliefs are in this record |

## Cross items for the software lead (not findings on the note)

- **X-1.** 07 section 2.1.1 has no row for stand-alone analysis notes that set values of a section 14.1 component. PDR work plan WP-PDR-33 routes this one, and the analysis template tells the file reviewer to set `assurance_required: false` for such a note. The PDR work plan and 07 give different dispatch rules (the gap INSP-047 finding-2 found for CR-007). For the 07 writer (WP-PDR-47, plan section 5.3): add an "Analyses setting values of a section 14.1 component" row, or state that the plan routes them.
- **X-2.** INSP-071 still reads `assurance_reviewer_agent: "pending (...)"`, `assurance_verdict: pending` and `assurance_tasks_applied: []`, and has no `paired_record`. Each reviewer updates only its own record. The software lead transcribes the pairing (INSP-075, NEEDS CHANGES).
- **X-3.** Finding-1 and finding-2 bound the same two values as INSP-071 finding-1. One delta iteration of the note can answer all three together, followed by a delta of both records (rule C1).

## Commands

- `git rev-parse 82cf086:<path>` and `HEAD:<path>` for the 7 product files: all equal. `git log 82cf086..HEAD` on the product paths: only the INSP-071 record commit `40e0d5e`.
- `git archive 82cf086 docs/design/analysis/keyer-host-study | tar -x` into the scratchpad, then `.venv/bin/python docs/design/analysis/keyer-host-study/check_keyer_host_study.py`: 348 PASS, "0 failed assertion(s)", exit 0. `cmp` of the regenerated results file and three PNGs against `git show 82cf086:<path>`: identical.
- Reviewer script on the frozen `keyer_model.paddle_watchdog`, `gap_rule_current` and `gap_rule_proposed`: held-dit and alternating streams with 1, 2 and 3-dit spaces at 5, 15, 25 and 50 WPM over 180 s (finding-1). The 1-dit rows reproduce the note's section 6.2 table (30.0, 20.4, 12.24, 6.12 s). Streams at 5, 10 and 20 WPM checked with monitor speeds of 11, 15, 25 and 50 WPM (finding-2).
- `tools/traceability.py --report-only --output <scratch>/traceability-report.md`: exit 0, 0 violations; `git status docs/vv/` clean.
- The three renders were opened and inspected. The axes, limits and labels agree with note sections 6.1 and 6.2, and the timeline shows the period released at 4.32 s.
- `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/validate_docs.py`: run on this record before its commit.

## Measurements (SWE-089)

Tasks in the task table 29 rows (23 applied Yes or No, 6 N/A); tasks answered No 9; section items checked 38 (R1 to R4, SA-A1 to A4, B1 to B3, C-a to C-l, D1 to D6, E1 to E4, F1 to F3), answered No 7; findings 2 Major, 3 Minor; fixed 0; deferred 0; iteration 1; effort 42 turns, about 70 minutes; renders inspected 3; reviewer model runs 2 scripts (32 stream cases).

## Verdict

```
ASSURANCE VERDICT: NEEDS CHANGES
PRODUCT: docs/design/analysis/keyer-host-study.md@39b43044 (with the model, checker, results and 3 plots of INSP-071) at 82cf086; PAIRED RECORD: INSP-071
PRODUCT TYPE: design (routed by PDR work plan WP-PDR-33; X-1); CRITICALITY: safety-critical
FINDINGS:
- [Major] swe-058 7.1 task 4 (SA-C-j) the proposed 2-dit gap and the count reset let keyer-fault streams with 2-dit or longer spaces escape K4 (i) and (ii); not analysed or routed.
- [Major] swe-134 7.1 task 4 (SA-C-i) dit-relative thresholds make SW-SAFE K4 depend on the keyer speed with no stated protected source; one mismatched value disables K4.
- [Minor] swe-134 7.1 task 6 the CR trigger list omits hazard-analysis section 7 row j and section 5 rows, 07 section 14.2 row j, the SW-SAFE module row and REQ-SW-SAFE-010.
- [Minor] swe-205 7.1 task 1 the 0.407 s monitor stall is not routed to WP-PDR-16 or WP-PDR-35 nor compared with the other row j budgets.
- [Minor] swe-070 7.1 task 1 (SA-F1) no TV record and no owner action for ruling on developer evidence; no assurance risk entry.
TASKS APPLIED: swe-134 7.1 task 5, swe-022 7.1 task 1, swe-057 7.1 task 2, swe-058 7.1 tasks 1 to 5, swe-134 7.1 tasks 1, 4, 6, swe-205 7.1 tasks 1, 3, 4, 5, swe-052 7.1 tasks 1, 2, swe-070 7.1 task 1, swe-192 7.1 task 1, swe-087 7.1 task 1, swe-088 7.1 task 1, swe-089 7.1 task 1, swe-081 7.1 task 2
TASKS N/A (relief): swe-057 7.1 task 1 and swe-143 7.1 task 1 (07 section 2.1.1 row Design, WP-PDR-32); swe-136 7.1 task 1 (07 section 17.3, 05 section 9.1 class C); swe-134 7.1 task 3 (07 section 9.7); swe-087 7.1 task 2 and swe-088 7.1 task 2 (07 section 10.2)
SWE-134 ITEMS CHECKED: a, d, f, g, h, i, j
MEASUREMENTS: size=1 note, 1 model, 1 checker, 1 results file, 3 plots; tasks=29; tasks_no=9; turns=42; minutes=70; major=2; minor=3
```

## Iteration 2: delta verification of finding-1 and finding-2 (Major) (2026-09-27, HEAD `ae29a98`)

**Scope (rule C1).** Only the two Major findings of iteration 1 and the product changes that answer them: note revision 2 (`1dd0fb7d`), `keyer_model.py` (`d28613af`), `check_keyer_host_study.py` (`f72f3a6a`), results (`7f4f0afd`) and the plots, all at `8c12b5a`. Findings 3 to 5 (Minor) are not re-checked; the note's status row says revision 2 does not address them, and they stay Open as liens. The author's summary for this delta states that no new edit or commit was made after `8c12b5a`.

**Independence (rule C4).** This invocation (`sa-reviewer:WP-PDR-33-keyer-host-study-iter2`) authored no part of the note, its revision 2, the model, the checker or the plots, is neither the iteration 1 assurance reviewer nor either INSP-071 reviewer, and edited no product file. The counter-examples below are this reviewer's own.

**Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` (revision 2 gap rule, `SW-SAFE` speed source, configuration guard) ran before any `grep`, which then only pinned lines in the note, the model and INSP-071. No rustos file was read.

**Freeze.** `git rev-parse 8c12b5a:<path>` equals `HEAD:<path>` at `ae29a98` for all 8 product files; `git log 8c12b5a..HEAD` on the product paths is empty.

### finding-1: Verified

| Fix element asked in iteration 1 | Revision 2 | Reviewer check | Result |
|---|---|---|---|
| Analyse keyer-fault streams (stretched spaces, ratio and weight corruption, stuck element timer) at 5 to 50 WPM under the current and proposed rules | Section 6.2 fault catalogue, 13 stream kinds at 5, 15, 25, 50 WPM, from idle and after 15 s of correct sending, under the current, revision 1 and revision 2 rules (`nogap_fault_catalogue`, `nogap_fault_missed`) | Checker re-run in the scratchpad: 555 PASS, 0 failed, exit 0; results file and 4 PNGs byte-identical to `8c12b5a` | Yes |
| The iteration 1 counter-examples caught | Rows "held dit, 2 dits" and "alternating, 3 dits" | Reviewer run of `watchdog_relative`, 180 s, from idle: held 2-dit spaces 30.24 / 30.0 / 18.34 / 9.17 s; alternating 2-dit 30.0 / 30.08 / 24.62 / 12.31 s; alternating 3-dit 30.0 / 30.0 / 30.0 / 15.38 s at 5 / 15 / 25 / 50 WPM. All 12 stop (iteration 1 proposal: none) | Yes |
| A count that a sub-word gap does not reset | (i-a) resets only on a word gap (4 r or 2 s); (i-b) period count 1 to 6 | Model lines of `watchdog_relative` read: `count_a` resets on `word` or a different duration only | Yes |
| Residual stated and routed to WP-PDR-16, into the CR and its impact review | Section 6.2 "Coverage given up"; section 8 row REQ-SYS-054; section 9 CR triggers and R-8 (a), (b) | Read | Yes for the streams the fix set out to catch. The short-interval defeat is a new defect of the revision 2 rule, raised as finding-6 |
| Correct-sending side still passes | 3790 streams of P, B and S, no trip; 9.91 s longest span | Checker assertions pass (re-run above); INSP-071 iteration 2 covers this side | Yes |

The plot `keyer-nogap-fault-coverage.png` was opened and inspected: two panels (15 and 50 WPM, fault after 15 s of correct sending), stop time against the space after every element (1 to 8 dits) for the three rules, the 30 s and 40 s reference lines and the "not stopped" band at 62 s. The revision 2 curves stay at or under 40 s at every space length, and they agree with the section 6.2 table.

### finding-2: Verified

| Fix element asked in iteration 1 | Revision 2 | Reviewer check | Result |
|---|---|---|---|
| K4 items (i) and (ii) independent of a keyer speed | Section 6.2: the rule reads only TX_KEY, "uses no keyer parameter"; section 8 row REQ-SYS-054; R-10 "The TX_KEY monitor reads no keyer data" | `inspect.signature(keyer_model.watchdog_relative)` has no speed parameter; its constants are `REF_WINDOW_S`, `GAP_FACTOR`, `WORD_FACTOR`, `ABS_GAP_S`, `SAME_TOL`, `MAX_PERIOD` | Yes |
| Squeeze speed from the configuration-guarded record, complement, 5 to 50 WPM | Section 6.1 "Speed source"; section 8 row REQ-SYS-184; `squeeze_limit_monitor_ms` (failure falls back to 50 WPM) | Reviewer sweep of `squeeze_limit_monitor_ms` over None, -1, 0, 1, 4, 5, 6, 7.5, 11, 12, 13, 25, 49, 50, 51, 255, with and without a complement failure: limit 2000 to 4800 ms, never undefined | Yes |
| Bound fault-side stops at the range ends and for a mismatched value | `squeeze_speed_source`, `squeeze_speed_mismatch`: 2.00 to 4.80 s; a higher monitor value only shortens the limit | Consistent with the sweep; checker assertions pass | Yes |
| Field-list change to the 03 and 07 writer; new cause to WP-PDR-16 | R-9 (WP-PDR-17, 03 section 4.3 and 07 section 14.1 guard row); R-8 (c) (WP-PDR-16) | Read | Yes |

### New finding (iteration 2)

finding-6 (Major, table above): the revision 2 reference interval has no lower bound, so one short key-up interval on TX_KEY every few seconds disables K4 items (i) and (ii) for periodic fault streams that the current rule stops. Reviewer scripts `probe.py` and `probe2.py` in the scratchpad run the frozen `watchdog_relative` and `paddle_watchdog` on those streams (Commands). The fix path is the note author's; the finding asks only that the rule bound r or that the residual be stated and routed.

### Commands (iteration 2)

- `git rev-parse 8c12b5a:<path>` and `HEAD:<path>` for the 8 product files: all equal; `git log 8c12b5a..HEAD` on the product paths: empty.
- `git archive 8c12b5a docs/design/analysis/keyer-host-study | tar -x` into the scratchpad, then `.venv/bin/python docs/design/analysis/keyer-host-study/check_keyer_host_study.py`: 555 PASS, "0 failed assertion(s)", exit 0, 39.5 s. `cmp` of the results file and the 4 PNGs against `git show 8c12b5a:<path>`: identical.
- Reviewer script `probe.py`: the iteration 1 counter-examples (12 cases) and the 1 ms glitch every 2, 5 and 9 s on held and alternating streams (24 cases) under `watchdog_relative`; continuous key-down with a 1 ms dropout every 1 and 5 s (stops at 30.0 s, window).
- Reviewer script `probe2.py`: a 1 ms glitch every 5 s and a space shortened to 0.4 dit (0.9 dit for the 2-dit stream) every 5 s, on held, alternating and held 2-dit streams at 5, 15, 25, 50 WPM, under `watchdog_relative` and `paddle_watchdog` with `gap_rule_current`.
- `squeeze_limit_monitor_ms` sweep (finding-2).
- `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/validate_docs.py`: run on this record before its commit.

### Measurements (SWE-089), iteration 2

Majors re-checked 2, Verified 2; fix elements checked 9 (finding-1 5, finding-2 4), all Yes; new findings 1 Major; renders inspected 1 (`keyer-nogap-fault-coverage.png`); reviewer model runs: 64 fault streams (12 counter-example, 24 glitch, 4 dropout in `probe.py`; 24 glitch or short-space streams in `probe2.py`, each under both rules) and 32 squeeze-limit values; effort about 20 turns and 40 minutes (front matter totals include iteration 1).

### Verdict (iteration 2)

```
ASSURANCE VERDICT: NEEDS CHANGES
PRODUCT: docs/design/analysis/keyer-host-study.md@1dd0fb7d (with the model, checker, results and 4 plots) at 8c12b5a; PAIRED RECORD: INSP-071
FINDINGS:
- [Major] finding-1 Verified: stretched-space fault streams are stopped by the revision 2 rule; catalogue, residual and routing present.
- [Major] finding-2 Verified: K4 (i) and (ii) read no keyer parameter; the squeeze speed is guarded, range-checked and bounded to 2.00 to 4.80 s; R-8 (c), R-9, R-10 routed.
- [Major] finding-6 Open: no lower bound on the reference interval r; a short key-up interval every few seconds disables K4 (i) and (ii) for periodic fault streams the current rule stops; not in the stated residual.
- [Minor] findings 3, 4, 5 Open (not re-checked; liens).
RECORD VERDICT: NEEDS CHANGES (open Major; held in any case until CR-012 merges with the template blob unchanged, lead SE convention of 2026-09-27)
```

### Cross item (iteration 2, for the software lead)

- **X-4.** INSP-071 iteration 2 copies `assurance_verdict` NEEDS CHANGES and `assurance_findings_major: 2` from iteration 1 of this record. After this delta the values are NEEDS CHANGES and 3. finding-6 bears on INSP-071 item "Confirmed for every key mode" only on the fault side; INSP-071 finding-5 (correct-sending dependence on A-5) is a separate matter.

## Iteration 3: delta verification of finding-6 (Major) (2026-09-27, HEAD `b4a75a1`)

**Scope (rule C1).** Delta iteration on note revision 3 (commit `b4a75a1`, freeze F0 again, rule C2), verifying only the fix of finding-6, the one open Major. Minor findings 3 to 5 were not touched by the author and are not re-checked (liens). **Product.** The 8 blobs of the front matter `product_files`; each equals `git rev-parse b4a75a1:<path>` and `HEAD:<path>` at HEAD `b4a75a1`, and all are on main. **Independence.** This invocation (sa-reviewer:WP-PDR-33-keyer-host-study-iter3) authored no part of WP-PDR-33 or its revisions, is not the INSP-071 reviewer and edited no product file. **Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` (query: the revision 3 glitch filter and lower-quartile reference) ran before any `grep -n`, which only pinned note lines 213, 246 and 248 and the checker section 5e. No rustos file was read.

### finding-6: Verified

| Fix element asked in iteration 2 | Revision 3 | Reviewer check | Result |
|---|---|---|---|
| Bound r from below or take r from a robust statistic | Section 6.2 table rows "Glitch filter" (10 ms, `GLITCH_MS`) and "Reference interval r" (nearest-rank lower quartile of the clean key-up intervals of 10 s, `REF_QUANTILE`, `REF_WINDOW_S`); section 8 row REQ-SYS-054; R-10 | Read `watchdog_relative` (b4a75a1): intervals under 10 ms bridged; pulses under 10 ms are no element, stay key-down for (ii), and their interval is kept out of the reference set; `ref_now` takes index ceil(0.25 n) - 1 of the sorted set | Yes |
| The finding-6 defeat (1 ms key-up glitch every few seconds) closed | Section 6.2 short-interval table row "1 ms key-up break": revision 3 0 of 96 not stopped | Reviewer re-run of the checker: the 12 finding-6 streams are stopped by revision 3 and not by revision 2; `watchdog_rev2` equals the frozen 8c12b5a `watchdog_relative` on 212 reviewer streams (48 perturbed periodic, 20 random-order, each speed; 0 differing) | Yes |
| Re-run the fault catalogue with short-interval variants (1 ms glitch, shortened space, every 1 to 10 s) and corpora P, B and S | Checker section 5e: 384 variants (1 ms and 15 ms key-up breaks, 1 ms key-down pulses, shortened spaces; every 1, 2, 3, 5, 9, 10 s; 4 streams; 5, 15, 25, 50 WPM); corpora P, B, S never trip (longest span 16.94 s, margin 13.1 s); 156 of 156 uniform catalogue streams stopped by 39.6 s | Checker run in the scratchpad from `git archive b4a75a1`: 563 PASS, "0 failed assertion(s)", exit 0, 43.7 s; results JSON and the 4 PNGs byte-identical to the committed blobs | Yes |
| State any remaining short-interval residual in section 6.2, section 8 and R-8 | Residual class (3) defined by share (key-up intervals of 10 ms or more and under half the other spaces are a quarter or more of the key-up intervals in some 10 s), in section 6.2, section 8 row REQ-SYS-054, R-8 (a), R-10, L-6, A-12 | Every reviewer counter-example below meets the share definition (0.25 to 0.43), so the defined class holds. Its stated extent does not: new finding-7 | Yes (definition); extent under finding-7 |
| Renders | `keyer-nogap-fault-coverage.png`, `keyer-nogap-vs-speed.png` re-rendered | Both opened and inspected: legends name revision 3 (lower-quartile reference); the vs-speed annotation reads 16.94 s, no trip; the fault-coverage curves agree with the section 6.2 table (39.6 s worst after sending) | Yes |

finding-6 is Verified for the defect it names (no lower bound on r; one short key-up interval set r for 10 s) and for the fix elements it asked.

### New finding (iteration 3)

finding-7 (Major, table above): the lower quartile is robust only when a 10 s window holds many key-up intervals. At 5 WPM a single spurious key-down element of 10 ms or more every 9 s defeats K4 items (i) and (ii) on three of the four periodic streams that the current rule stops at 30.0 to 30.24 s, and pulses every 1 to 2 s do so at 15 and 25 WPM. The cases meet the formal class (3) definition, but the note tells the owner that class (3) needs a short interval every 3 s or less at 5 WPM, that none escapes at 15 WPM and above, and that short intervals every 5 s or more no longer defeat K4. The 384-variant catalogue never inserts an unfiltered spurious element. The fix path is the author's (robust reference at low counts, or a restated class (3) extent with the missing variants run).

### Commands (iteration 3)

- `git rev-parse b4a75a1:<path>` and `HEAD:<path>` for the 8 product files: all equal; `git log b4a75a1..HEAD -- docs/design/analysis`: empty; `git diff 8c12b5a b4a75a1 -- docs/design/analysis/keyer-host-study.md` read in full.
- `git archive b4a75a1 docs/design/analysis/keyer-host-study | tar -x` and `git archive 8c12b5a ...` into the scratchpad; `.venv/bin/python docs/design/analysis/keyer-host-study/check_keyer_host_study.py` on the b4a75a1 copy: 563 PASS, 0 failed, exit 0, 43.7 s; `cmp` of the results file and the 4 PNGs against `git show b4a75a1:<path>`: identical.
- Reviewer script `probe3.py`: (A) `watchdog_rev2` (b4a75a1) against the frozen 8c12b5a `watchdog_relative` on 212 streams, 0 differing; (B) 288 adversarial variants outside the checker catalogue (11 ms and 20 ms key-down pulses in a space every 1, 2, 5 s; 10 ms and 12 ms key-up breaks every 1, 2, 4, 5 s; a 1 ms break in every element; a 5 ms pulse in every space; shortened space and 15 ms break every 4, 6, 7 s) on the four streams at 5, 15, 25, 50 WPM under revision 3 and the current rule: revision 3 misses 47 and stops 1 late (118.46 s), the current rule stops all 288.
- Reviewer script `probe4.py`: key-down pulses of 10, 11, 15, 30, 60 ms every 5, 9, 10 s at 5 and 15 WPM with the checker's `short_share` measure: 30 escapes at 5 WPM (every 5 and 9 s), share 0.25 to 0.43; none at every 10 s.
- Renders opened: `keyer-nogap-fault-coverage.png`, `keyer-nogap-vs-speed.png`.
- `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/validate_docs.py`: run on this record before its commit.

### Measurements (SWE-089), iteration 3

Majors re-checked 1, Verified 1; fix elements checked 5, all Yes; new findings 1 Major; renders inspected 2; reviewer model runs: 212 equivalence streams, 288 adversarial variants (each under revision 3 and the current rule), 60 pulse-length and rate streams; effort about 15 turns and 35 minutes (front matter totals include iterations 1 and 2).

### Verdict (iteration 3)

```
ASSURANCE VERDICT: NEEDS CHANGES
PRODUCT: docs/design/analysis/keyer-host-study.md@a980ec5c (with the model, checker, results and 4 plots) at b4a75a1; PAIRED RECORD: INSP-071
FINDINGS:
- [Major] finding-1, finding-2 Verified (iteration 2).
- [Major] finding-6 Verified: glitch filter and lower-quartile reference; the 1 ms glitch defeat is closed; 384 variants run; residual class (3) defined and routed.
- [Major] finding-7 Open: at 5 WPM one spurious key-down element of 10 ms or more every 9 s (every 1 to 2 s at 15 and 25 WPM) defeats K4 (i) and (ii); the note's stated extent of class (3) understates this.
- [Minor] findings 3, 4, 5 Open (not re-checked; liens).
RECORD VERDICT: NEEDS CHANGES (open Major; held in any case until CR-012 merges with the template blob unchanged, lead SE convention of 2026-09-27)
```

### Cross item (iteration 3, for the software lead)

- **X-5.** INSP-071 carries `assurance_verdict` and `assurance_findings_major` from this record; after this delta they are NEEDS CHANGES and 4.

## Iteration 3 re-issue 1: delta verification of finding-7 (Major), the fourth review pass (2026-09-28, HEAD `0caa0cc`)

**Iteration count and escalation (rule C1; 07 section 10.2).** This is the fourth review pass on the note. The front matter keeps `iteration: 3`, the record schema maximum (precedent INSP-009 and INSP-038, "iteration 3 re-issue"); the body and the finding states call it iteration 4. Rule C1 allows at most three iterations before escalation to the owner. No owner authorization of a fourth iteration was found (`grep -rn INSP-075 docs/plan/` returns nothing on 2026-09-28), and this pass leaves a Major open, so the escalation is due now: see cross item X-7.

**Scope (rule C1).** Delta pass on note revision 4 (commit `7fe558a`, freeze F0 again, rule C2), verifying only the fix of finding-7, the one open Major. Minor findings 3 to 5 were not touched by the author (status row) and are not re-checked; they stay Open as liens. **Product.** The 9 blobs of the front matter `product_files` (the new plot `keyer-nogap-short-interval.png` added). Each equals `git rev-parse 7fe558a:<path>`, `HEAD:<path>` and the working tree at HEAD `0caa0cc`, and all are on main. `git log 7fe558a..HEAD -- docs/design/analysis` shows only `0caa0cc` (the WP-PDR-28 thermal note), which touches no product file. **Independence (rule C4).** This invocation (`sa-reviewer:WP-PDR-33-keyer-host-study-iter4`) authored no part of WP-PDR-33 or its revisions 2 to 4, is neither an earlier INSP-075 reviewer nor an INSP-071 reviewer, and edited no product file. The counter-examples below are this reviewer's own. **Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` (query: INSP-075 keyer host study review record finding-7) ran before any `grep`, which then only pinned note lines and the checker section 5e. No rustos file was read.

### finding-7: Verified

| Fix element asked in iteration 3 | Revision 4 | Reviewer check | Result |
|---|---|---|---|
| Add key-down pulses from `GLITCH_MS` to at least one dit, and key-up breaks of 10 to 15 ms, every 1 to 10 s, to the short-interval variants | Section 6.2 short-interval table: 1568 variants (key-up breaks 1, 10, 12, 15 ms; key-down elements 1, 10, 11, 15, 30, 60 ms and 0.25, 0.5, 1 dit; shortened space; every 1, 2, 3, 5, 7, 9, 10 s; four streams; 5, 15, 25, 50 WPM) under the current rule and revisions 2, 3 and 4; `perturb_short_interval` generalised | Checker section 5e read. Checker run in the scratchpad from `git archive 7fe558a`: 571 PASS, "0 failed assertion(s)", exit 0, 88.6 s; results JSON and the 5 PNGs byte-identical to the committed blobs | Yes |
| Make the reference robust at low interval counts (one of three suggested forms), or restate class (3) | Both. Split filter (`SPLIT_FRAC` 0.5 of min(r, e), `REF_MIN_N` 4): a split pulse is no element, stays key-down for (ii) and keeps its key-up interval out of the reference set. Class (3) restated from the quarter share (k at least n/7, n/3, n/4 insertions per 10 s; at 5 WPM two spurious elements under 10 s apart can suffice) in section 6.2, section 8, R-8 (a) and the CR wording | Model diff `b4a75a1..7fe558a` read: `kd_now` takes the nearest-rank lower quartile of key-downs of 10 ms or more; the split test uses r and e as they stand at the pulse start; `watchdog_rev3` is `split_frac=None`. On 1500 reviewer streams `watchdog_rev3` equals `watchdog_relative(split_frac=None)` (0 differing) | Yes for finding-7. The filter itself raises finding-8 |
| The finding-7 counter-examples stopped | Revision 4 stops all 30 at 30.0 to 30.24 s (checker assertion) | Reviewer script `probe7.py` with its own insertion code (not `perturb_short_interval`): a 10, 11, 15, 30 or 60 ms key-down pulse centred in a space every 5 or 9 s, alternating, held-dit 2-dit-space and held-dah streams at 5 WPM, 300 s: revision 3 stops 0 of 30; revision 4 stops 30 of 30 at 30.0 to 30.24 s, the same as the current rule | Yes |
| Withdraw the "rare short interval" and "every 5 s or more" statements | Section 6.2 "Revision 3 proposal ... does not hold": both statements named and withdrawn; revision 3 withdrawn; history row 4 | Read; neither statement remains in the note | Yes |
| Renders | New `keyer-nogap-short-interval.png`; `keyer-nogap-fault-coverage.png` and `keyer-nogap-vs-speed.png` re-rendered | All three opened and inspected. The short-interval plot shows per speed the variants not stopped within 30 s plus one cycle against the insertion interval, with the limit-0 line; at 5 WPM revision 4 reads 47, 32, 14, 6, 6, 6, 0, as in section 6.2. The fault-coverage curves stay at or under 40 s. The vs-speed annotation reads 16.94 s, no trip | Yes |

finding-7 is Verified for the defect it names (the understated extent of class (3) and the unfiltered spurious element at low interval counts) and for the fix elements it asked.

### Findings (iteration 3 re-issue 1, fourth pass)

| Finding | Severity | State | Note |
|---|---|---|---|
| finding-1 | Major | Verified (iteration 2) | |
| finding-2 | Major | Verified (iteration 2) | |
| finding-3 | Minor | Open | Not re-checked (lien) |
| finding-4 | Minor | Open | Not re-checked (lien) |
| finding-5 | Minor | Open | Not re-checked (lien) |
| finding-6 | Major | Verified (iteration 3) | |
| finding-7 | Major | Verified (iteration 4) | This delta |
| finding-8 | Major | Open | New; full text in the findings table above |

### New finding (iteration 3 re-issue 1, fourth pass)

finding-8 (Major, table above): the split filter's threshold depends on e, the lower quartile of the key-downs, so in a periodic fault stream whose shortest element is a quarter or less of its elements the filter hides that regular element in some cycles and not in others. This breaks the (i-b) period run. Of 1500 random periodic cycles, 17 that revision 3 stops are never stopped by revision 4 (4 of them stopped by the current rule at 30.0 to 30.16 s), and 30 more stop later than revision 3 and 30 s plus one cycle. None of these is in residual classes (1) to (3), and section 7 states that revision 4 stops every periodic stream. The fix path is the author's: a split decision that does not depend on the pattern of a periodic stream, or a stated and routed fourth residual. In both cases the catalogue and the checker need periodic cycles with a minority short element.

### Commands (iteration 3 re-issue 1)

- `git rev-parse 7fe558a:<path>`, `HEAD:<path>` and `git hash-object <path>` for the 9 product files: all equal. `git log 7fe558a..HEAD -- docs/design/analysis`: `0caa0cc` only (thermal note). `git diff b4a75a1 7fe558a` read for the note and the model.
- `git archive 7fe558a docs/design/analysis/keyer-host-study | tar -x` into the scratchpad, then `.venv/bin/python docs/design/analysis/keyer-host-study/check_keyer_host_study.py`: 571 PASS, 0 failed, exit 0, 88.6 s. `cmp` of the results file and the 5 PNGs against `git show 7fe558a:<path>`: identical.
- Reviewer script `probe7.py`: the 30 finding-7 streams, plus the held-dit stream, built with the reviewer's own pulse insertion, under the current rule and revisions 3 and 4.
- Reviewer script `probe5.py`: hand-built periodic cycles with one short element (3, 4 or 5 dahs and a dit, or 2 dahs and a dit, with 2.5 or 3-dit spaces and a 6 to 7-dit gap) at 5, 15, 25, 50 WPM; plus a first random set of 1500 cycles.
- Reviewer script `probe6.py`: 1500 random periodic cycles of 2 to 6 elements (seed 75; element 0.5, 1, 2, 3, 4 or 6 dits; space 1, 2, 2.5, 3, 4, 5, 7 or 9 dits; 5, 15, 25 or 50 WPM; 300 s from idle) under the current rule, `watchdog_rev3`, `watchdog_relative(split_frac=None)` and `watchdog_relative`, with the split-pulse count; results in the scratchpad `probe6.json`.
- Renders opened: `keyer-nogap-short-interval.png`, `keyer-nogap-fault-coverage.png`, `keyer-nogap-vs-speed.png`.
- `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/validate_docs.py`: run on this record before its commit.

### Measurements (SWE-089), iteration 3 re-issue 1

Majors re-checked 1, Verified 1; fix elements checked 5, all Yes; new findings 1 Major; renders inspected 3; reviewer model runs: 30 finding-7 streams and 10 held-dit streams (`probe7.py`), 24 hand-built and 1500 random periodic streams (`probe5.py`), 1500 random periodic streams under four rule settings (`probe6.py`); effort about 20 turns and 40 minutes (front matter totals include iterations 1 to 3).

### Verdict (iteration 3 re-issue 1, fourth pass)

```
ASSURANCE VERDICT: NEEDS CHANGES
PRODUCT: docs/design/analysis/keyer-host-study.md@32f4a139 (with the model, checker, results and 5 plots) at 7fe558a; PAIRED RECORD: INSP-071
FINDINGS:
- [Major] finding-1, finding-2 Verified (iteration 2); finding-6 Verified (iteration 3).
- [Major] finding-7 Verified: split filter added; 1568 short-interval variants run; all 30 finding-7 streams stopped by 30.24 s; class (3) restated with its extent; the two wrong statements withdrawn.
- [Major] finding-8 Open: the split filter hides a regular short element of a periodic fault stream in some cycles and not in others; 17 of 1500 random periodic cycles that revision 3 stops escape K4 and 30 stop later; not in any stated residual class.
- [Minor] findings 3, 4, 5 Open (not re-checked; liens).
RECORD VERDICT: NEEDS CHANGES (open Major after the third iteration: owner escalation due under rule C1, X-7; held in any case until CR-012 merges with the template blob unchanged, lead SE convention of 2026-09-27)
```

### Cross items (iteration 3 re-issue 1, for the software lead)

- **X-6.** INSP-071 carries `assurance_verdict` and `assurance_findings_major` from this record; after this delta they are NEEDS CHANGES and 5.
- **X-7.** Rule C1 escalation. finding-8 is a Major still open after the fourth review pass on the note. INSP-075 has had three iterations and this re-issue. The software lead puts the choice to the owner at the next session and records it in the status note, as for INSP-038 (status note 2026-09-27 sections 7 and 9). The routes are: (1) authorize one more fix and delta on finding-8; (2) accept revision 3 or revision 4 with the finding-8 class stated as a K4 residual bounded by K12 and routed to WP-PDR-16 (rule C10); or (3) keep the baselined REQ-SYS-054 rule, which stops 4 of the 17 finding-8 misses (at 30.0 to 30.16 s) and misses the other 13, and which trips correct Bug and Straight sending (INSP-071 finding-1). This record does not choose.
