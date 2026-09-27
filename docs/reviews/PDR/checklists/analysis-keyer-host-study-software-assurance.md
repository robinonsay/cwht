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
# product_commit and product_files: equal to INSP-071 (readiness R1; rule C2). Every blob equals
# git rev-parse 82cf086:<path> and HEAD:<path> at HEAD 9b20ea5 (2026-09-27); all are on main, so the lead SE
# branch-only convention concerns only the checklist template
product_commit: "82cf08655dbaf89a139ce64927158130f8e574e9"
product_files: ["docs/design/analysis/keyer-host-study.md@39b43044230ce9513b525e6b4417b722d1eebe6d", "docs/design/analysis/keyer-host-study/keyer_model.py@39e6f92cffd45c9aa60d29fdd485633a6b77f748", "docs/design/analysis/keyer-host-study/check_keyer_host_study.py@0fda48d9630b4d85d90d6f5b17f3c67b277ae4c2", "docs/design/analysis/keyer-host-study/keyer-host-study-results.json@ef3d199da4f4bbb771de55e911f788b4ed024282", "docs/design/analysis/keyer-host-study/keyer-squeeze-vs-speed.png@010c2daf423c684520478bdb4bf9862a1e96af0f", "docs/design/analysis/keyer-host-study/keyer-nogap-vs-speed.png@514851a41e0b6f599bad00a350be87e3a4f44f3a", "docs/design/analysis/keyer-host-study/keyer-squeeze-timeline.png@e474a5ca3e1b7f3cd29a171a395d6e6ac278b103"]
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
reviewer_agent: "sa-reviewer:WP-PDR-33-keyer-host-study"
assurance_required: true
assurance_reviewer_agent: "sa-reviewer:WP-PDR-33-keyer-host-study (software assurance function; paired file review INSP-071 by reviewer:WP-PDR-33-keyer-host-study-iter1)"
iteration: 1
readiness_met: true
# reviewer_verdict and assurance_verdict: two Major findings (finding-1, finding-2), so NEEDS CHANGES (07 section
# 10.2; PDR work plan rule C1)
reviewer_verdict: NEEDS CHANGES
assurance_verdict: NEEDS CHANGES
# verdict: set by Claude as software lead (07 section 10.2). NEEDS CHANGES: both this record and INSP-071 are
# NEEDS CHANGES. Even when both are APPROVED, the record verdict stays held until CR-012 merges with the template
# blob unchanged (lead SE convention of 2026-09-27, INSP-031 practice) and INSP-071 carries this pairing
verdict: NEEDS CHANGES
findings_major: 2
findings_minor: 3
findings_open: 5
findings_fixed: 0
findings_verified: 0
findings_deferred: 0
assurance_findings_major: 2
assurance_findings_minor: 3
assurance_tasks_applied: ["swe-134 7.1 task 5", "swe-022 7.1 task 1", "swe-057 7.1 task 2", "swe-058 7.1 task 1", "swe-058 7.1 task 2", "swe-058 7.1 task 3", "swe-058 7.1 task 4", "swe-058 7.1 task 5", "swe-134 7.1 task 1", "swe-134 7.1 task 4", "swe-134 7.1 task 6", "swe-205 7.1 task 3", "swe-052 7.1 task 1", "swe-070 7.1 task 1", "swe-192 7.1 task 1", "swe-205 7.1 task 1", "swe-205 7.1 task 4", "swe-205 7.1 task 5", "swe-052 7.1 task 2", "swe-087 7.1 task 1", "swe-088 7.1 task 1", "swe-089 7.1 task 1", "swe-081 7.1 task 2"]
swe134_items_checked: [a, d, f, g, h, i, j]
deferred_rids: []
items_no: ["swe-057 7.1 task 2", "swe-058 7.1 task 3", "swe-058 7.1 task 4", "swe-134 7.1 task 1", "swe-134 7.1 task 4", "swe-134 7.1 task 6", "swe-070 7.1 task 1", "swe-205 7.1 task 1", "swe-205 7.1 task 5", SA-C-f, SA-C-g, SA-C-i, SA-C-j, SA-D1, SA-D6, SA-F1]
effort_turns: 42
effort_minutes: 70
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
| <a id="finding-1"></a>finding-1 | assurance | Major | swe-058 7.1 task 4; swe-134 7.1 tasks 1 and 6; SA-C-j; SA-D6 | Note section 6.2, lines 173 and 183 ("No rev A source produces one: the keyer never inserts a gap longer than one dit by itself"); section 3.4 line 90 (the count resets on a qualifying gap); section 8 row REQ-SYS-054 | The proposed REQ-SYS-054 gap (2 dit times) is shown only against fault streams from a correct keyer. K4 exists for keyer faults: `hazards.json` HZ-004 K4 runs it "not by the keyer engine, so that a keyer fault that produces a stream does not also disable it", "whatever the element pattern"; causes C4 (engine fault, "timeouts misconfigured") and C7 (corrupted keying state) and coverage rows 4, 6, 10 and 11 of `hazard-analysis.md` section 5 depend on it. The claim "the keyer never inserts a gap longer than one dit" assumes the engine the monitor guards. A space-timing or ratio fault that stretches the inter-element space to 2 dits or more makes every space a qualifying gap under the proposed rule. Because the model also resets the identical-element count on a qualifying gap, K4 (i) is defeated with (ii). Reviewer run of the frozen `paddle_watchdog` over 180 s: held-dit stream with 2-dit spaces, current rule trips at 30.24 s (5 WPM), 30.0 s (15), 18.34 s (25), 9.17 s (50), proposed rule never; alternating stream with 2-dit spaces, current rule 30.0 to 30.08 s at every speed, proposed never; 3-dit spaces at 15 to 50 WPM: current trips (12.2 to 30.1 s), proposed never. For these streams the firmware control column of rows 4 and 6 becomes "none" and only K12 at 150 to 180 s remains, which changes a safety conclusion that the owner as SMA TA would rule on (plan rule C10). INSP-071 finding-1 covers the other side (false trips in Bug and Straight sending) and is not raised again. Fix: analyse the missed-detection side for keyer-fault streams (space stretched by a factor up to the largest the gap threshold admits, ratio and weight corruption, a stuck element timer) under the current and the proposed rule, at 5 to 50 WPM. Then either choose a gap rule, with a count that a sub-word gap does not reset, that keeps these streams caught and still passes the correct-sending corpus, or state the coverage given up as a residual and route it to WP-PDR-16 for the section 5 coverage table and the section 8 fault trees, so that it appears in the CR and its impact review (rule C6) | Open | Pending | |
| <a id="finding-2"></a>finding-2 | assurance | Major | swe-057 7.1 task 2; swe-134 7.1 tasks 1 and 4; swe-205 7.1 task 1; SA-C-f, SA-C-g, SA-C-i | Note section 8 rows REQ-SYS-054 and REQ-SYS-184 ("at the selected speed"); sections 6.1 and 6.2; section 9 (no request names the speed source) | Both changed values are in dit times at the selected speed, so the `SW-SAFE` monitor, which 07 section 14.1 line 594 places outside the keyer "so that a keyer-engine fault cannot disable it", now depends on a keyer parameter. The note does not state where `SW-SAFE` reads the speed or how that value is protected. The keyer speed is not in the configuration guard's field list (03 section 4.3 line 176 and 07 section 14.1 line 596: "power step, tune level, guest lock, frequency calibration, thermal thresholds, keyer mode, debounce"). Its range checks REQ-SW-KEYER-015 and REQ-SW-KEYER-037 are in the monitored keyer and carry no `hazard_ids`. Reviewer run of the frozen model with a monitor speed value higher than the stream speed: 5 WPM stream with the monitor at 11 or 15 WPM, 10 WPM with 25, 20 WPM with 50, held and alternating. The current rule trips at 15.3 to 30.0 s. The proposed rule never trips, because a monitor value more than twice the true element rate makes every 1-dit space a qualifying gap. In the other direction a value below the 5 WPM floor lengthens the squeeze stop past the note's 4.80 s bound (20 dits: 6.0 s at 4 WPM, 24 s at 1 WPM), and a zero speed has no defined limit. So one corrupted or mismatched value disables K4 (i) and (ii) (SWE-134 i, single event), and neither the note, the hazard data nor any request names this software contribution (SWEHB `swe-205` section 7.7.2 considerations 15 and 16, independence and common cause). Fix: state in the proposed CR wording and in section 9 that `SW-SAFE` takes the speed from the configuration-guarded record, held with its complement and range-checked 5 to 50 WPM (SWE-134 f and g), or derives the dit length from the TX_KEY read-back itself. Bound the fault-side stop times at the range ends and for a mismatched value. Send the field-list change to the 03 and 07 writer (WP-PDR-17) and the new cause to WP-PDR-16 | Open | Pending | |
| <a id="finding-3"></a>finding-3 | assurance | Minor | swe-134 7.1 task 6; SA-D6 | Note section 9, first bullet ("CR triggers", line 245) | The CR trigger list names the requirements, mirrors, HZ-004 K4, ConOps, concept, TC-SYS-038 and ICD-CTL-KEY. It omits the texts that hold the same numbers as SWE-134 item j provisions: `hazard-analysis.md` section 7 row j ("30 s without a 7-dit or 500 ms gap, squeeze 2 s"), which 07 section 14.2 makes the governing text for provision numbers, and its section 5 coverage rows 4 and 5; 07 section 14.2 row j (line 624, the same values) and the `SW-SAFE` module row (line 637, "with the row j values"); and the reserved REQ-SW-SAFE-010 child. If the CR follows the list as written, the SWE-134 j provision and the hazard analysis would disagree with REQ-SYS-054 and REQ-SYS-184. Fix: add these texts, with their writers (WP-PDR-16; the 07 writer WP-PDR-47; WP-PDR-35), to the section 9 list | Open | Pending | |
| <a id="finding-4"></a>finding-4 | assurance | Minor | swe-205 7.1 task 1; SA-C-j; SA-D1 | Note section 6.5 (line 195) and request R-2 (line 247) | The note finds that a configuration-store sector update stops the processor for 0.407 s with interrupts masked and XIP off (A-7). During that time every safety monitor stops, not only the 1 kHz key sampler: the software contribution is by inaction. R-2 constrains only Transmit-keyed and key-closed states and goes to the firmware design writers (WP-PDR-32, WP-PDR-41). It does not go to the hazard data writer (WP-PDR-16) or to the SW-SAFE requirement writer (WP-PDR-35), and the stall is not compared with the other 07 section 14.2 row j budgets that are shorter than 0.407 s (REQ-SYS-004 carrier end 20 ms, thermal 100 ms, audio fault mute 10 ms, charge disable within one supervision period). RSK-021 covers a hang or corruption during the write, not the monitor stall. Fix: route R-2 to WP-PDR-16 as a candidate software cause and to WP-PDR-35 as a `SW-SAFE` constraint (no store write outside Receive with PA off and the key inputs open), and state which row j budgets are active in the states where a write is allowed | Open | Pending | |
| <a id="finding-5"></a>finding-5 | assurance | Minor | swe-070 7.1 task 1; SA-F1 | Note section 10 (line 262, "owner action proposed in the author's return"); header row "Credit" | The model has no TV record. `rmm.json` SWE-070 (FC) plans "the validation evidence (TV-NNN) of ... the Python checkers" for PDR, so the proposed safety values would reach the owner on an unaccredited model unless a TV record exists or the owner rules on developer evidence. The note states that condition correctly. INSP-071 routes it as cross item X-1. No owner action is in plan section 6.1, and no assurance risk entry exists. The assurance lens raises it as a finding, because the values set safety-critical `SW-KEYER` and `SW-SAFE` thresholds. Fix: before B2, either file a class B TV record for `keyer_model.py` (the F6 and F7 golden vectors as the known-answer test and a seeded fault; 05 section 9.1) or add the owner action to plan section 6.1. In both cases submit the concern to the risk register writer (WP-PDR-18) as an entry tagged `assurance` | Open | Pending | |

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
