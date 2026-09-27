---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md section 13
# is the single field list; docs/process/08-agent-briefing.md section 3.2; template
# docs/templates/peer-review-checklist-requirements.md revision C, sections A to F and the per-requirement table,
# the "Requirement files, any level" row).
# This is the separate software assurance record of the SW-KEYER software requirements and their closing
# test cases (07 section 2.1.1: SW-KEYER is safety-critical, 07 section 14.1; paired form of 07 section 10.2).
# The paired file review of the same SW-KEYER blobs is INSP-004,
# docs/reviews/SRR/checklists/requirements-tx-and-sw-keyer.md (reviewer:requirements-l2), whose
# assurance_reviewer_agent still reads "not yet dispatched" (SRR package H1 (c), H15, R6).
id: INSP-026
checklist: peer-review-checklist-requirements
checklist_revision: C
checklist_file: docs/reviews/SRR/checklists/requirements-sw-keyer-software-assurance.md
product: docs/requirements/sw/sw-keyer/requirements.json
# iteration 2: product_commit is the author's fix commit f2e02aa (finding-1); product_files are
# git rev-parse HEAD:<path> at f2e02aa (HEAD at review; working tree equal to HEAD for both).
# iteration 1 reviewed HEAD adcfe0946d2f1b5cd8f41a8f91eb4219a7fb99a1 with requirements.json@db2de344c66ff7caa5e72f922f87686fd3a7ce71
# and test_cases.json@f730056914aedfa003757f94284a020e79c67795 (both last changed in cb00792).
# INSP-004 also covers the TX files; this assurance record covers only the SW-KEYER pair, because TX is
# not a software product of 07 section 10.1.
# iteration 2 and the R8 re-issue named product_commit f2e02aa0d4bdfff8eaebbce92c32580c3dc26c30 and the blobs
# requirements.json@4d22b399f1647743dd837e731d8c05fa6be7b7bb and test_cases.json@d3c0c236651bd41332bac345fd936e199734bfe3.
# Iteration 3 (post-SRR-ruling delta, 2026-09-26): product_commit is ebe5873, the last commit that touched the
# products (cd61450 requirements, ebe5873 test cases, package item R16); product_files are git rev-parse HEAD:<path> at ebe5873
product_commit: "ebe5873a5151c19e141958e31cf9559f78f5154c"
# Re-issue 2026-09-26 (package item R8, no further product review): both blobs re-checked equal to git rev-parse HEAD:<path> at 1af795c
product_files: ["docs/requirements/sw/sw-keyer/requirements.json@f9141160c4d92ad80ae91144c2499b22292d4b16", "docs/test_cases/sw-keyer/test_cases.json@2716ca3f53d349c84f2a4a717a3b7daa1566792f"]
# inputs read (not reviewed), committed blobs at the same HEAD
# iteration 3 also read (committed at ebe5873): docs/reviews/SRR/decisions-for-owner.md@a8931d91,
# docs/reviews/SRR/minutes.md@f3ee2271, docs/safety/hazards.json 0.5.0-pha@81cacde4, docs/design/allocation.json@442de2fd
input_files: ["docs/process/07-software-engineering-plan.md@d0f8baf614b49e9c99d8fe2169093d02626ac50d", "docs/process/03-software-classification-and-rmm.md@ed270f443e2ab648480017df8ad3d0221400cf4c", "docs/safety/hazards.json@37d6cc832ed8f164e5f7e6e911a8656a56720c9f", "docs/requirements/sys/requirements.json@0da73012043cd79bb75d57c521369736141d7f1f", "docs/safety/hazard-analysis.md (HEAD adcfe09, section 7 row d line 223)"]
product_size: 39 requirements (REQ-SW-KEYER-001 to 039, all Draft; 19 tagged safety with hazard_ids; 039 added at f2e02aa); 43 test cases (TC-SW-KEYER-001 to 043, all Draft; 35 HostUnit, 8 Bench)
sprint: SRR-prep
author_agent: "author:requirements-l2 (requirements author, REQ-SW-KEYER) and test-author:requirements-l2 (independent test author, TC-SW-KEYER)"
reviewer_agent: "reviewer:INSP-026"
criticality: safety-critical
assurance_required: true
# assurance_reviewer_agent: this record IS the software assurance review; distinct from the author and
# from the paired file reviewer reviewer:requirements-l2 (INSP-004)
assurance_reviewer_agent: "reviewer:INSP-026 (software assurance function; paired file review INSP-004 by reviewer:requirements-l2)"
paired_record: INSP-004
# iteration 3: post-SRR-ruling delta verification of cd61450 and ebe5873 (package item R16)
iteration: 3
# readiness_met: false. R1 Yes (validate_docs.py exit 0), R2 Yes, R4 Yes, R5 N/A; R3 No: no author self-check
# against sections A to F is on record (the same gap INSP-004 records; package decision 115); unchanged at iteration 2
# Re-issue 2026-09-26: R3 Yes on the author self-check filed at 1af795c (package item R7), so readiness_met is true;
# iteration stays 2 (no product review)
readiness_met: true
# reviewer_verdict and assurance_verdict: APPROVED (with liens) at iteration 2: finding-1 (Major) Verified on
# f2e02aa; finding-2 to finding-6 are Minor and dispositioned "Lien: fix before PDR" (lead SE convergence
# rule 2026-09-26). verdict: NEEDS CHANGES held only by readiness R3 (package decision 115), as INSP-023
# iteration 2; no Major finding is open.
# re-issue: verdict APPROVED (with liens finding-2 to finding-7): readiness met, no Major finding open
# iteration 3: verdict APPROVED (with liens finding-2, 3, 4, 6, 7, 8, 9, 10): no Major finding open, readiness met;
# finding-5 Verified (hazards.json 0.5.0-pha, bfea9c7, SRR decision 112); finding-8, 9, 10 new Minor liens
reviewer_verdict: APPROVED
assurance_verdict: APPROVED
verdict: APPROVED
# re-issue: finding-7 (Minor) is new, raised from the author's exception E-1 (same defect as INSP-004 finding-20)
# iteration 3: finding-8, finding-9, finding-10 (Minor) are new
findings_major: 1
findings_minor: 9
findings_open: 0
findings_fixed: 0
# findings_verified: finding-1 (iteration 2) and finding-5 (iteration 3)
findings_verified: 2
# findings_deferred: the eight Minor liens (finding-2, 3, 4, 6, 7, 8, 9, 10), fix before PDR (SRR lien L-6)
findings_deferred: 8
assurance_findings_major: 1
assurance_findings_minor: 9
assurance_tasks_applied: [swe-050 7.1 task 1, swe-184 7.1 task 1, swe-134 7.1 task 1, swe-134 7.1 task 3, swe-134 7.1 task 4, swe-134 7.1 task 5, swe-134 7.1 task 6, swe-192 7.1 task 1]
deferred_rids: []
# re-issue: R3 Yes; CK-REQ-A7 No on finding-7 (lien); the others unchanged from iteration 2
# iteration 3: CK-REQ-F1 No on finding-9 (lien); the others unchanged
items_no: [CK-REQ-A7, CK-REQ-C4, CK-REQ-C5, CK-REQ-F1, SA-134-1, SA-134-6]
# effort: iterations 1 and 2 (52 turns, 80 min) plus the re-issue (12 turns, 20 min) plus iteration 3 (22 turns, 35 min)
effort_turns: 86
effort_minutes: 135
record_status: Open
date: 2026-09-26
date_closed: null
---

# Peer review record INSP-026: software assurance review of the SW-KEYER software requirements and test cases

**Verdict (iteration 3, post-SRR-ruling delta, 2026-09-26, blobs equal to HEAD `ebe5873`): APPROVED with liens finding-2, 3, 4, 6, 7, 8, 9 and 10.** The two product commits since the re-issue (`cd61450`, `ebe5873`, package item R16) apply the owner rulings correctly and introduce no Major defect; finding-5 is Verified (SRR decision 112, `bfea9c7`); three new Minor liens are raised (see "Post-SRR-ruling delta (2026-09-26, iteration 3)" at the end).

**Verdict (re-issue of iteration 2, 2026-09-26, package item R8, blobs equal to HEAD `1af795c`): APPROVED with liens finding-2 to finding-7.** Readiness R3 is now Yes: the author self-check filed at `1af795c` lists the brief's acceptance criteria and answers checklist sections A to G item by item (see "Re-issue"). The author's exception E-1 is raised as finding-7 (Minor, Lien: fix before PDR; the same defect as INSP-004 finding-20). Reviewer and assurance verdicts stay APPROVED; no Major finding is open and no finding waits on an owner ruling. The paired file review INSP-004 is re-issued the same day with `paired_record: INSP-026` and `assurance_verdict: APPROVED` (cross item X-1 done).

**Products.** `docs/requirements/sw/sw-keyer/requirements.json` (blob `db2de344c66ff7caa5e72f922f87686fd3a7ce71`) and `docs/test_cases/sw-keyer/test_cases.json` (blob `f730056914aedfa003757f94284a020e79c67795`), both `git rev-parse HEAD:<path>` at the review baseline `adcfe0946d2f1b5cd8f41a8f91eb4219a7fb99a1`, last changed in `cb00792`; the working tree equals HEAD for both. These are the same SW-KEYER blobs that INSP-004 iteration 3 names in its `product_files`. **Sources of record read:** `docs/process/07-software-engineering-plan.md` sections 2.1.1, 5 item 5, 7 (CS-35, CS-39), 10.2, 14.1, 14.2 and 15 (blob `d0f8baf6`, committed at `b301df2`); `docs/process/03-software-classification-and-rmm.md` sections 4.3 and 5 (blob `ed270f44`); `docs/safety/hazards.json` 0.4.2-pha (blob `37d6cc83`); `docs/safety/hazard-analysis.md` section 7 row d; the L1 parents in `docs/requirements/sys/requirements.json` (blob `0da73012`); INSP-004 at HEAD.

**Checklist.** `docs/templates/peer-review-checklist-requirements.md` revision C, product-type row "Requirement files, any level": readiness R1 to R5, sections A to F, the per-requirement table and the V2 block. G1 to G8 are N/A (not a plan); B7 and R5 are N/A (not a CR). `docs/templates/peer-review-checklist-software-assurance.md` does not exist (08 section 3.5: due before PDR), so, per 07 section 15 (line 658) and the template's "Used by" paragraph, the `# 7. Software Assurance` section 7.1 tasks of the SWEHB pages for the SWEs this file implements are applied directly as items SA-NNN-n: `swe-050` (task 1), `swe-184` (task 1), `swe-134` (tasks 1, 3, 4, 5, 6) and `swe-192` (task 1). SWEHB topic `6-2-checklist-for-general-software-safety-requirements.md` was opened; its content is the attachment PAT-007, which the scrape does not contain (9 lines), so it could not be applied (observation 3). The test-case file is judged under the assurance lens (SWE-192 and the 07 section 14.2 verification cells); its procedure-level review belongs to a `test-sw-keyer` record with `peer-review-checklist-test.md`.

**Citations verified in the corpus.** SWE-050, NPR 7150.2D 4.1.2 (`npr-7150-2d/04-chapter4.md` line 13); SWE-184, 4.1.4 (line 19); SWE-192, 4.5.12 (line 143); SWE-134, 3.7.3 items a to l (`03-chapter3.md` line 187 onward; item d "Operator overrides of software functions require at least two independent actions by an operator"); SWE-023, 3.7.2 (line 185). SWEHB section 7.1 tasks read at `swe-050-software-requirements.md` line 870, `swe-184-software-related-constraints-and-assumptions.md` line 805, `swe-134-safety-critical-software-design-requirements.md` lines 671 to 692, `swe-192-software-hazardous-requirements.md` line 734. No 47 CFR clause is newly cited by this record; REQ-SW-KEYER-028 cites 97.109(d), 97.203 and 97.119(b), which INSP-004 checked against the verbatim corpus.

**Search-first compliance.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: SW-KEYER SWE-134 items allocation module row; SWE-184 constraints between hardware, operator and software and the SA tasks; decision 115 author self-checks; Straight-on-tip menu action plus confirmation versus HZ-004 K2). The tool was available. One listing of the known directory `docs/reviews/SRR/checklists/` was made at the start, before the first search, to open two existing records as the assignment asks. `grep -n`, `sed -n` and read-only Python over the committed blobs (`git show HEAD:<path>`) were used afterwards only to pin lines and recompute values.

**Independence.** This reviewer did not author the SW-KEYER requirements or test cases, 07, 03, `hazards.json` or INSP-004, is a different invocation from the INSP-004 reviewer, and edited none of those files. INSP-004 was read for its findings and dispositions before this review; the section "Concurrence with INSP-004" records where this record agrees and where it differs.

**Iteration 2 (2026-09-26, HEAD `f2e02aa`).** The author reported finding-1 fixed (none disputed) in one commit, `f2e02aa` ("SW-KEYER: override path validated by the keyer per 07 section 14.2 row d (INSP-026 finding-1)"), which touches only the SW-KEYER pair and their renderings (`git show --stat f2e02aa`: requirements.json +50, requirements.md +50, test_cases.json +57, test_cases.md +104 changed lines). The reviewer read the whole diff and the new committed blobs `requirements.json@4d22b399f1647743dd837e731d8c05fa6be7b7bb` and `test_cases.json@d3c0c236651bd41332bac345fd936e199734bfe3` (`git rev-parse HEAD:<path>` at `f2e02aa`; working tree equal to HEAD). Search: `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` (07 section 14.2 row d, receiving component and minimum interval) before any manual search; read-only Python over `git show HEAD:<path>` recomputed counts and the hazard links. 07 row d (line 618) was re-read against the new text. Verification of finding-1, item by item: (1) REQ-SW-KEYER-024 now changes the mode "only after a mode-selection action and a separate confirmation that it validates as distinct operator events"; its rationale names the keyer as the receiving component, the menu output as an untrusted request that never sets the mode, and the one-sample and one-queued-event rejection, independent of the owner's concurrence with the menu path, matching 07 row d, section 5 item 5 and CS-39. (2) REQ-SW-KEYER-029 is restated the same way; the author chose the keyer as the validating receiver (test-mode state is keyer state; REQ-SYS-179 child_ids is `[REQ-SW-KEYER-029]` only, recomputed), which is option (1) of the fix and satisfies 07 row d "per receiving component". (3) New self-derived REQ-SW-KEYER-039 fixes the distinct-event rule (two different inputs in two different samples, or one input with a release and 300 ms, TBR with owner, plan and `close_by: PDR`, matching the 07 row d "minimum interval fixed at PDR"), tagged `safety` with `hazard_ids` HZ-004, Test, with HostUnit and Bench closing cases. (4) `tc_sw_keyer_024_menu_command` is replaced by `tc_sw_keyer_024_action_confirmation`, and TC-SW-KEYER-024 and 029 add request-only, faulty-menu one-sample, faulty-menu one-queued-event, confirmation-without-action, no-release and interval-minus-10-ms cases, with interval-plus-10-ms acceptance, and matching acceptance criteria. (5) TC-SW-KEYER-034 and 037 add on-target menu-fault injection (over the UART test pads of an instrumented or fault-injection build of the release commit, release image restored and verified afterwards, the same pattern TC-SW-KEYER-034 already used for its marker pads) and cite REQ-SW-KEYER-039, so the SWE-192 on-target confirmation holds for all 19 hazard requirements. No new Major defect: the new text keeps observation 2 (REQ-SW-KEYER-025 acceptance with an input closed, TC-SW-KEYER-034 step now selects and confirms with the ring closed), keeps the REQ-SW-KEYER-022 interlock after the mode change, and adds no conflict with another module. Two new Minor findings are raised (finding-5, finding-6) and dispositioned as liens. finding-1 is **Verified**.

## Findings

Ids follow the `finding-<n>` anchor rule of 01 section 13. Severity: Major blocks the baseline or leaves a NASA requirement unimplemented; Minor is fixed before the next review. Under the lead SE convergence rule of 2026-09-26 (charter section 4 item 3), every Minor finding is dispositioned "Lien: fix before PDR" and carried by the package as a Routine item; only the Major finding changes the product in this round.

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | assurance | Major | SA-134-1, SA-134-4, SA-134-6, CK-REQ-C4 (V3) | REQ-SW-KEYER-024 `description` and `rationale` (requirements.json line 687); REQ-SW-KEYER-029 (line 844); TC-SW-KEYER-024 step `tc_sw_keyer_024_menu_command` (test_cases.json line 1086) and acceptance criteria; TC-SW-KEYER-029; TC-SW-KEYER-034, 037 | SWE-134 d (NPR 7150.2D 3.7.3 d, "at least two independent actions by an operator") is allocated to the keyer as a receiving component, and the committed plan requires the keyer to enforce it itself: 07 section 14.2 row d (line 618) lists "selecting Straight-on-tip after a mono plug or any other key-input mode change (REQ-SYS-056; HZ-004 K2)" and "entering a bench test mode (REQ-SYS-179, REQ-SYS-007)" and states that "The receiving safety-critical component (`SW-TXSEQ`, `SW-KEYER` or `SW-AUDIO`) accepts an override only from two distinct operator events that it validates itself from the debounced input samples of the 1 kHz SIO sampling (CS-35) it reads directly ... with both events from one input sample rejected; a menu output is an untrusted request and never sets the protected value", and that this "holds whether or not the owner concurs" with the Proposed menu override command path; 07 section 5 item 5 (line 215) names the key-input mode and the test-mode state as safety-critical data validated by the receiving module, and CS-39 (line 306) repeats it; `hazard-analysis.md` section 7 row d (line 223) requires "a menu action plus a confirmation" for Straight-on-tip and names the keyer. The keyer file does the opposite: REQ-SW-KEYER-024 changes the mode "only on a mode-selection command from the menu", and its rationale says the confirmation is added "before the menu issues the command" and that "under either the keyer changes mode only on the command", so the protected value is set by one menu output, the case 07 says must never occur. REQ-SW-KEYER-029 starts the PARIS generator (the only keying source besides the jack, REQ-SYS-007) on a "confirmed bench-test-mode command", with the confirmation judged by the menu, not by the keyer from two operator events. The test file then verifies the unsafe behavior: `tc_sw_keyer_024_menu_command` asserts that a single mode-selection command changes the mode, and no case in the file injects a faulty menu that emits both events from one input sample or one queued event, which the 07 row d Verification cell requires "per receiving component". The INSP-004 finding-2 disposition ("the keyer statement holds under either reading") predates the receiving-side rule of 07 revision A.4 (`b301df2`, committed after the keyer file at `cb00792`) and no longer holds. Consequence: a menu fault (bounced encoder push, stale or duplicated queued event, corrupted menu state) changes the key-input mode or starts the generator without two operator actions, contributing to HZ-004 by incorrect action (SWEHB `swe-134` section 7.1 tasks 1, 4 b and 6). Fix: (1) restate REQ-SW-KEYER-024 so that the keyer changes its key-input mode only after two distinct operator events that it validates itself from its own 1 kHz input samples (two input sources, or a release between the two presses and a minimum interval, TBR to PDR), rejecting both events from one sample and treating the menu command as a request; (2) do the same for the generator start of REQ-SW-KEYER-029, or state in its rationale that `SW-TXSEQ` is the validating receiver and the keyer starts only on a start that module has validated (the 07 `SW-TXSEQ` row carries test-mode d); (3) replace `tc_sw_keyer_024_menu_command` with an action-plus-confirmation sequence, and add faulty-menu HostUnit cases (both events from one input sample; both from one queued event; confirmation without its action) to TC-SW-KEYER-024 and TC-SW-KEYER-029, with the on-target counterparts in TC-SW-KEYER-034 and 037. Cross items (not this product): REQ-SYS-056 and HZ-004 K2 name "an explicit menu selection" only and disagree with 07 row d and `hazard-analysis.md` row d (L1 author and hazard analyst). **Iteration 2: Verified** on `f2e02aa` (REQ-SW-KEYER-024, 029 restated, REQ-SW-KEYER-039 added, TC-SW-KEYER-024, 029, 034, 037 revised; see the iteration 2 paragraph) | Verified | none | |
| <a id="finding-2"></a>finding-2 | assurance | Minor | CK-REQ-C4 | All 18 `safety`-tagged requirements (REQ-SW-KEYER-002, 019 to 031, 033 to 036) | CK-REQ-C4 and 07 section 14.2 (line 628: each module requirement is written "referencing the `REQ-SW-SAFE-NNN` row it specializes") ask each keyer SWE-134 requirement to name the reserved shared row it specializes; `grep -c REQ-SW-SAFE` on the file returns 0, so the link from, for example, REQ-SW-KEYER-022 (item a) to REQ-SW-SAFE-001 or REQ-SW-KEYER-031 (items c, k, l) to REQ-SW-SAFE-003, 011, 012 exists only in prose ("SWE-134 d", "07 section 14.2, SW-KEYER items c, k and l"). The `SW-SAFE` file does not exist yet (RMM SWE-050 and SWE-184 rows: Planned for PDR), so the link cannot be made machine-checkable today. Fix: when `docs/requirements/sw/requirements.json` is written, add the `REQ-SW-SAFE-NNN` id of each specialized row to the `design_refs` or the `Why:` item of each safety requirement | Lien: fix before PDR | Pending | PDR (Routine package item; owner: SW-KEYER requirements author) |
| <a id="finding-3"></a>finding-3 | assurance | Minor | CK-REQ-C5, CK-REQ-C6, SA-134-1 | REQ-SW-KEYER-022, 024, 025; TC-SW-KEYER-022, 025 | SWE-134 b and e and SWEHB `swe-184` section 3.2 ("Software safety requirements include the modes or states of operation under which they are valid") ask for the keyer's behavior at a mode change to be stated for every keyer state. REQ-SW-KEYER-022 "withhold[s] key-down after ... mode change", but no requirement states what happens to a key-down already asserted when a mode-selection command is accepted (mid-element in a paddle mode, or during a straight-key closure), and the cases enter the mode change only from key-up (TC-SW-KEYER-022 entry paths; TC-SW-KEYER-025 selects with inputs closed but key-down already idle by the interlock). The hazard exposure is bounded (the 5 s manual-closure timeout REQ-SW-KEYER-026 and the hardware cutoff REQ-SYS-055 still apply), so this is Minor. Fix: state that an accepted mode change forces key-down idle within 1 ms (or completes the element in progress, whichever the author chooses with the reason) before the REQ-SW-KEYER-022 interlock runs, and add the mid-element and mid-closure cases | Lien: fix before PDR | Pending | PDR (Routine package item; owner: SW-KEYER requirements author and test author) |
| <a id="finding-4"></a>finding-4 | assurance | Minor | SA-134-1, SA-134-6, CK-REQ-C4 | REQ-SW-KEYER-002, 024; 07 section 14.2 `SW-KEYER` row item f (line 632) | 07 section 5 item 5 (line 215) lists the key-input mode as safety-critical state, and a corrupted mode (or Straight-input setting) in RAM changes which contact keys without any operator action, the same outcome finding-1 guards against. SWE-134 f ("detects inadvertent memory modification and recovers to a known safe state") is written for the keyer only for the key-down state (REQ-SW-KEYER-030) and the paddle memories (REQ-SW-KEYER-034), matching the 07 row f, which names only those. The persisted copy is covered by the configuration guard, not the running copy. Fix: add a requirement (or extend REQ-SW-KEYER-030) that the key-input mode and Straight-input setting are held with their complements and that a disagreement forces key-down idle and the KEY inhibit until the operator reselects; cross item for the 07 author to add the mode to the row f list | Lien: fix before PDR | Pending | PDR (Routine package item; owners: SW-KEYER requirements author; 07 author for the row f text) |
| <a id="finding-5"></a>finding-5 | assurance (iteration 2) | Minor | CK-REQ-B5, SA-134-6 | REQ-SW-KEYER-039 `hazard_ids` (requirements.json line 1147); `docs/safety/hazards.json` HZ-004 | The new REQ-SW-KEYER-039 names HZ-004, but HZ-004 in `hazards.json` 0.4.2-pha (blob `37d6cc83`, unchanged) does not list it in `requirement_ids` (recomputed; `traceability.py --report-only`: `HAZARD_INVERSE` warning for REQ-SW-KEYER-039, 0 violations), so the inverse hazard link the iteration 1 R2 evidence relied on no longer holds for every keyer safety requirement. The keyer file is correct; the gap is in the hazard record, outside the author's scope. Fix: the hazard analyst adds REQ-SW-KEYER-039 to HZ-004 `requirement_ids` (K2 and K13 controls) in the next `hazards.json` revision (cross item X-5) | Lien: fix before PDR | Pending | PDR (Routine package item; owner: hazard analyst) |
| <a id="finding-6"></a>finding-6 | assurance (iteration 2) | Minor | CK-REQ-A1, CK-REQ-A3, V2 | REQ-SW-KEYER-039 `description` | The statement "accept two operator events as distinct only from different input samples showing different inputs, or a release and 300 ms (TBR)" is compressed: the second branch does not say that the release lies between the two presses on the same input and that 300 ms is the minimum from the first press to the second, nor that the events are control-input (button and encoder) samples; those bounds are only in the rationale, and the cases (TC-SW-KEYER-024, 029 minus and plus 10 ms) read them from there. The requirement is also self-derived and Robin's concurrence is pending in the V2 record. Not Major: the rationale, the 07 row d text and the cases agree on one meaning. Fix: restate as, for example, "The keyer firmware shall accept two control-input operator events as distinct only when they occur on different inputs in different samples, or on one input with a release between them and at least 300 ms (TBR) from the first press to the second", and record Robin's V2 concurrence with the other self-derived requirements | Lien: fix before PDR | Pending | PDR (Routine package item; owner: SW-KEYER requirements author) |
| <a id="finding-7"></a>finding-7 | assurance (re-issue, from author exception E-1) | Minor | CK-REQ-A7 (WR-10) | REQ-SW-KEYER-024, 029, 039 `rationale` | Introduced by the `f2e02aa` fix of finding-1. 02 section 4.3 limits `rationale` to 120 words; at blob `4d22b399` REQ-SW-KEYER-024 has 198, 029 has 160 and 039 has 215 (whitespace count; none exceeded 120 at `db2de344`). The safety content is correct and agrees with 07 section 14.2 row d; only the form breaks WR-10, which 02 section 4.2 makes Minor. Same defect as INSP-004 finding-20 (paired file review); one fix closes both. Fix: state the validation rule once, in REQ-SW-KEYER-039, cite it from 024 and 029, and bring each rationale to 120 words or fewer | Lien: fix before PDR | Pending | PDR (Routine package item; owner: SW-KEYER requirements author) |

### Lien table (convergence rule, 2026-09-26)

| Lien | Finding | Severity | Disposition | Owner | Due | Package carriage |
|---|---|---|---|---|---|---|
| L-1 | finding-2 | Minor | Lien: fix before PDR | SW-KEYER requirements author | PDR (with the `SW-SAFE` file) | Routine item |
| L-2 | finding-3 | Minor | Lien: fix before PDR | SW-KEYER requirements author and test author | PDR | Routine item |
| L-3 | finding-4 | Minor | Lien: fix before PDR | SW-KEYER requirements author; 07 author (row f text) | PDR | Routine item |
| L-4 | finding-5 | Minor | Lien: fix before PDR | Hazard analyst (`hazards.json` HZ-004) | PDR | Routine item |
| L-5 | finding-6 | Minor | Lien: fix before PDR | SW-KEYER requirements author | PDR | Routine item |
| L-6 | finding-7 | Minor | Lien: fix before PDR | SW-KEYER requirements author (one fix with INSP-004 finding-20) | PDR | Routine item |

## Readiness criteria (all true before the review starts)

| # | Criterion | Answer | Evidence |
|---|---|---|---|
| R1 | The product validates: `tools/validate_docs.py` exits 0 | Yes | Run 2026-09-26 at HEAD `adcfe09` before this record was written: `validate_docs: 40 passed, 0 failed, 40 checked`, including `PASS docs/test_cases/sw-keyer/test_cases.json`; the requirements file passes against `docs/requirements/schema.json` |
| R2 | `tools/traceability.py` reports no violation for the ids in the file | Yes | `--report-only` exit 0: 237 requirements, 170 test cases, 0 violations, 2 warnings (`SYS_UNALLOCATED` REQ-SYS-125 and REQ-SYS-148, outside this product); no `HAZARD_INVERSE` warning remains for any REQ-SW-KEYER id (INSP-004 finding-16 resolved in `hazards.json` 0.4.2-pha; recomputed: every `hazard_ids` entry of the 18 safety requirements appears in the named hazard's `requirement_ids`). Iteration 2 at `f2e02aa`: exit 0, 238 requirements, 170 test cases, 0 violations, 3 warnings: the two above and `HAZARD_INVERSE` for the new REQ-SW-KEYER-039 (finding-5, Minor lien) |
| R3 | The author's return states the self-check against sections A to G and the brief's acceptance criteria | Yes (re-issue 2026-09-26); No at iterations 1 and 2 | Re-issue: section "Author self-check" (filed at `1af795c`), verified in "Re-issue". Iterations 1 and 2: no requirements-author return with a self-check was supplied with this assignment; INSP-004 records the same gap (its `items_no` holds R3) and package decision 115 lists INSP-004 |
| R4 | Every TBR has owner, plan, close_by; no TBD in the file | Yes | `grep -c -w TBD`: 0 in both files. Ten requirements carry a `tbr` object (009, 014, 017, 018, 020, 021, 022, 026, 032, 036), each with `owner`, `plan` and `close_by: PDR` (checked by script) |
| R5 | For a CR: impact assessment attached | N/A | Not a CR |

## Software assurance tasks applied (SWEHB section 7.1 tabs)

| Id | SWEHB task | Answer | Evidence |
|---|---|---|---|
| SA-050-1 | `swe-050` 7.1 task 1: all software requirements established, captured and documented as part of the technical specification | Yes | 38 REQ-SW-KEYER at Draft under the requirement schema, rendered in `docs/requirements/sw/sw-keyer/requirements.md`; every requirement has a parent or a `Self-derived:` rationale (034, 035, 036, 038); every one has at least one closing case (script: 0 uncovered). SRR entrance row 25 needs the file at Draft (package H15; baseline at PDR, charter section 7) |
| SA-184-1 | `swe-184` 7.1 task 1: requirements contain the safety constraints, controls, mitigations and assumptions between hardware, operator and software | Yes | All 18 safety requirements carry a `Depends on:` item naming the hardware bound (REQ-SYS-055 cutoff, REQ-SYS-119 pull-downs, REQ-TX-014 and REQ-TX-003 AND gate) and the operator's role (opens the contact, removes the plug, makes the menu selection), and a `Fault tolerance:` item citing `hazard-analysis.md` 8.1 (script check). The hardware versus software precedence at a keying fault is stated (REQ-SW-KEYER-026: firmware at 5 s acts before the 7.5 s hardware floor). The mode-change state gap is finding-3 |
| SA-134-1 | `swe-134` 7.1 task 1: requirements implement items a to l | No | Against the 07 `SW-KEYER` row (line 632): a REQ-SW-KEYER-022 (key-down withheld at boot, reset, mode change); b keyer modes 001 to 012 as behaviors, invalid-state gap finding-3; c 031; d 024, 029 and 039 as 07 row d requires (finding-1 Verified at iteration 2); e 022 (key-down rejected while the interlock is pending) and 029 (confirmation without selection rejected, TC-SW-KEYER-029); f 030, 034 (mode not covered, finding-4); g 019, 020, 021, 036; h 030 and 028; i 028 (key-down only from debounced inputs or the confirmed generator; RF needs the second condition, REQ-SYS-120); j 026 (5 s) and 031 (1 ms); k, l 031. Iteration 2: remains No only for item f (finding-4, Lien) |
| SA-134-3 | `swe-134` 7.1 task 3: values of safety-critical loaded data tested | Yes | The keyer's loaded settings are speed, switchpoint, hang and the Straight-input setting; out-of-range values are rejected with the previous value kept (REQ-SW-KEYER-037; TC-SW-KEYER-009, 015, 032) and no key-line pattern changes any of them (REQ-SW-KEYER-038; TC-SW-KEYER-040). Configuration-record integrity belongs to `SW-CFG` and the configuration guard |
| SA-134-4 | `swe-134` 7.1 task 4: partitioning or isolation; safety-critical data isolated from non-safety-critical | Yes (iteration 2; No at iteration 1) | Iteration 2: REQ-SW-KEYER-024, 029 and 039 treat every menu output as an untrusted request and validate the two events from the keyer's own control-input samples (finding-1 Verified). Iteration 1: 07 section 5 item 5 and CS-39 make every menu event an untrusted request validated by the receiving module; REQ-SW-KEYER-024 and 029 accept the menu's command as the decision (finding-1). Positive evidence: REQ-SW-KEYER-038 isolates the settings from the key line; the no-gap watchdog stays in the safe-state manager (REQ-SW-KEYER-019 rationale, HZ-004 K4) |
| SA-134-5 | `swe-134` 7.1 task 5: participate in reviews of safety-critical products | Yes | This record (07 section 2.1.1, SW-KEYER safety-critical) |
| SA-134-6 | `swe-134` 7.1 task 6: SWE-134 implementation consistent with the system hazard analysis | No | Recomputed from `hazards.json` 0.4.2-pha: HZ-001, HZ-004 and HZ-010 name "Keyer and keying output"; every keyer control is carried (HZ-004 K1 022, 023, 035; K2 002, 024, 025; K3 026, 027; K7 031; K8 030, 034; K9 019, 020, 021, 036; K13 028, 029; HZ-010 K3 019, 020, 021, 036; HZ-001 K3 026) and the inverse links hold. Inconsistent: `hazard-analysis.md` section 7 row d (line 223) requires a menu action plus a confirmation for Straight-on-tip, which REQ-SW-KEYER-024 did not implement at iteration 1 (finding-1, Verified at iteration 2); key-input mode integrity (finding-4, Lien); the new REQ-SW-KEYER-039 is not yet in HZ-004 `requirement_ids` (finding-5, Lien). Remains No at iteration 2 on the two liens |
| SA-192-1 | `swe-192` 7.1 task 1: requirements tracing to a hazard verified through test | Yes | All 18 requirements with `hazard_ids` have `verification_method` Test, a HostUnit closing case and a Bench on-target case (TC-SW-KEYER-019, 034 to 039; script: 0 without Bench), per 04 T-SW-TARGET. The faulty-menu case missing from TC-SW-KEYER-024 and 029 was part of finding-1. Iteration 2: 19 requirements with `hazard_ids`, all Test, each with a HostUnit and a Bench case (REQ-SW-KEYER-039: TC-SW-KEYER-024, 029 HostUnit; 034, 037 Bench); faulty-menu cases present |

## Checklist items (sections A to F)

Items outside the assurance lens were re-checked on the committed blobs and are answered with the evidence found; the full per-requirement WR and V1 to V6 judgment of these blobs is INSP-004 iteration 3, with which this record concurs except where a finding says otherwise.

| Id | Answer | Evidence |
|---|---|---|
| CK-REQ-A1 | Yes | One "shall" per `description` (script; five hits were "shall," before a mode phrase, read and correct), active voice, subject "The keyer firmware" |
| CK-REQ-A2 | Yes | Longest description 24 words (REQ-SW-KEYER-007, 008); no compound requirement found |
| CK-REQ-A3 | Yes | Every quantity has a number, unit and bound (1.000 ms +/-0.010 ms, 2 and 5 samples, 500 samples, 20 ms, 5 s, 1 ms, 3 to 30 dits, 5 to 50 WPM, 50 frames/s and 50 detents/s) |
| CK-REQ-A4 | Yes | `traceability.py` T-17 lint: no hit for the module |
| CK-REQ-A5 | Yes | Descriptions name no module, part or algorithm; the complement method sits in the REQ-SW-KEYER-030 `Constraint:` item |
| CK-REQ-A6 | Yes | Titles at most 80 characters, no "shall"; ids REQ-SW-KEYER-001 to 038 contiguous, none reused |
| CK-REQ-A7 | Yes | Rationales carry `Why:` with a source; concurred with INSP-004 (its remaining `items_no` A7 is its own open lien, finding-17 area) |
| CK-REQ-A8 | Yes | "straight key", "iambic paddle", `KEY inhibit`, Straight, Iambic A and B, Ultimatic, Bug match the SYS file and ConOps Table 3.4-4 |
| CK-REQ-B1 | Yes | 34 parented to REQ-SYS entries that list them in `child_ids` (tool); 034, 035, 036, 038 self-derived with a `Self-derived:` rationale and Robin's concurrence pending in INSP-004's V2 block |
| CK-REQ-B2 | Yes | Each safety requirement implements a named `hazards.json` control (SA-134-6) |
| CK-REQ-B3 | Yes | Concurred with INSP-004 finding-7 closure (REQ-SYS-051 and 054 held by CTL and the safe-state manager) |
| CK-REQ-B4 | Yes | Both key types covered (Straight 001, 002, 018; paddle 003 to 012, 017); OPS-013, OPS-017, OPS-021 cited |
| CK-REQ-B5 | Yes | Every software control of `hazards.json` naming the keyer appears as a requirement and every `hazard_ids` link is inverse-linked (R2) |
| CK-REQ-B6 | Yes | `safety` tag on exactly the 18 requirements with `hazard_ids` (script: none either way); `regulatory` on 028 |
| CK-REQ-C1 | Yes | Timing consistent with dot = 1200/WPM ms; 5 s timeout below the 7.5 s hardware floor |
| CK-REQ-C2 | Yes | `ICD-CTL-KEY` in `design_refs` of the key-line requirements (INSP-004 finding-3 closure, re-read) |
| CK-REQ-C3 | Yes | SA-184-1 |
| CK-REQ-C4 | No | finding-1 (item d, Verified at iteration 2), finding-2 (no `REQ-SW-SAFE-NNN` reference), finding-4 (item f for the mode) |
| CK-REQ-C5 | No | finding-3; state names used are architecture or ConOps names (no `KeyClosed`) |
| CK-REQ-C6 | Yes, with finding-3 | Stuck key (026), corrupted state (030, 034), keyer error and safe-state command (031), closure without plug (036), out-of-range settings (037) are specified; the mode change during key-down is finding-3 |
| CK-REQ-C7 | Yes | No command path on the key line (REQ-SW-KEYER-038, TC-SW-KEYER-040 flood and crafted patterns); no personal data field |
| CK-REQ-C8 | N/A | The keyer holds no loaded configuration record of its own (`SW-CFG`); setting acceptance is SA-134-3 |
| CK-REQ-D1 | Yes | No response faster than one 1 ms sample; 1 ms responses (030, 031, 033, 034) are one sample period |
| CK-REQ-D2 | N/A | No resource value in the file |
| CK-REQ-D3 | Yes | Behind the HAL traits; WP-SW-02 (SIO sampling) named in 07 section 19 |
| CK-REQ-D4 | Yes | Tolerances argued in the rationales (INSP-004 findings 8, 10, 15 closures) |
| CK-REQ-E1 | Yes | All 38 Test |
| CK-REQ-E2 | Yes | Every `verification_note` names HostUnit with the mock clock and, for hazard requirements, the Bench T-SW-TARGET case; no timing requirement closes on Emulation |
| CK-REQ-E3 | Yes | All 18 hazard requirements are Test (SWE-192) |
| CK-REQ-E4 | Yes | Observable at key-down output, sidetone gate, display interface and settings read-back |
| CK-REQ-E5 | Yes | Bench cases use the Pico-based keying fixture and logic capture of 04 section 6.1 |
| CK-REQ-E6 | Yes | Every requirement cited by at least one case (script) |
| CK-REQ-F1 | Yes | No duplicate or conflicting quantity inside the module; the conflict found is with 07 row d (finding-1) |
| CK-REQ-F2 | Yes | Enum spellings match the SYS file |
| CK-REQ-F3 | Yes | No requirement belongs to another module; finding-1 option (2) keeps test-mode entry validation where 07 places it |
| CK-REQ-F4 | Yes | `priority` set on all 38 (36 Baseline, 2 KDR); no "should" in a description |
| CK-REQ-G1 to G8 | N/A | Not a plan |
| CK-REQ-B7 | N/A | Not a CR |

## Per-requirement validation (assurance lens; 02 sections 4.2 and 5)

Severity and state are kept out of this table (they are in the findings table). The WR and V columns concur with INSP-004 iteration 3 on the same blobs, re-checked here only for the safety requirements; V2 values are those of INSP-004.

| Requirement | WR failures | V1 | V2 | V3 | V4 | V5 | V6 | CK-REQ items answered No | Disposition |
|---|---|---|---|---|---|---|---|---|---|
| REQ-SW-KEYER-001 | none | Pass | Ready: customer, user | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SW-KEYER-002 | none | Pass | Ready: customer, user, guest operator | Pass | Pass | Pass | Pass | CK-REQ-C4 | finding-2, finding-4 |
| REQ-SW-KEYER-003 | none | Pass | Ready: customer, user | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SW-KEYER-004 | none | Pass | Ready: customer, user | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SW-KEYER-005 | none | Pass | Ready: customer, user | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SW-KEYER-006 | none | Pass | Ready: customer, user | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SW-KEYER-007 | none | Pass | Ready: customer, user | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SW-KEYER-008 | none | Pass | Ready: customer, user | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SW-KEYER-009 | none | Pass | Ready: customer, user | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SW-KEYER-010 | none | Pass | Ready: customer, user | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SW-KEYER-011 | none | Pass | Ready: customer, user | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SW-KEYER-012 | none | Pass | Ready: customer, user | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SW-KEYER-013 | none | Pass | Ready: customer, user | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SW-KEYER-014 | none | Pass | Ready: customer, user | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SW-KEYER-015 | none | Pass | Ready: customer, user | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SW-KEYER-016 | none | Pass | Ready: customer, user | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SW-KEYER-017 | none | Pass | Ready: customer, user | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SW-KEYER-018 | none | Pass | Ready: customer, user | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SW-KEYER-019 | none | Pass | Ready: customer, user, guest operator | Pass | Pass | Pass | Pass | CK-REQ-C4 | finding-2 |
| REQ-SW-KEYER-020 | none | Pass | Ready: customer, user, guest operator | Pass | Pass | Pass | Pass | CK-REQ-C4 | finding-2 |
| REQ-SW-KEYER-021 | none | Pass | Ready: customer, user, guest operator | Pass | Pass | Pass | Pass | CK-REQ-C4 | finding-2 |
| REQ-SW-KEYER-022 | none | Pass | Ready: customer, user, guest operator | Pass | Pass | Pass | Pass | CK-REQ-C4, CK-REQ-C5 | finding-2, finding-3 |
| REQ-SW-KEYER-023 | none | Pass | Ready: customer, user, guest operator | Pass | Pass | Pass | Pass | CK-REQ-C4 | finding-2 |
| REQ-SW-KEYER-024 | none | Pass | Ready: customer, user, guest operator | Pass (iteration 2; Fail (g) at iteration 1) | Pass | Pass | Pass | CK-REQ-C4, CK-REQ-C5 | finding-1 (Verified), finding-2, finding-3, finding-4 |
| REQ-SW-KEYER-025 | none | Pass | Ready: customer, user, guest operator | Pass | Pass | Pass | Pass | CK-REQ-C4, CK-REQ-C5 | finding-2, finding-3 |
| REQ-SW-KEYER-026 | none | Pass | Ready: customer, user, guest operator, public | Pass | Pass | Pass | Pass | CK-REQ-C4 | finding-2 |
| REQ-SW-KEYER-027 | none | Pass | Ready: customer, user, guest operator | Pass | Pass | Pass | Pass | CK-REQ-C4 | finding-2 |
| REQ-SW-KEYER-028 | none | Pass | Ready: customer, user, guest operator, regulator | Pass | Pass | Pass | Pass | CK-REQ-C4 | finding-2 |
| REQ-SW-KEYER-029 | none | Pass | Ready: customer, user, guest operator | Pass (iteration 2; Fail (g) at iteration 1) | Pass | Pass | Pass | CK-REQ-C4 | finding-1 (Verified), finding-2 |
| REQ-SW-KEYER-030 | none | Pass | Ready: customer, user, guest operator | Pass | Pass | Pass | Pass | CK-REQ-C4 | finding-2 |
| REQ-SW-KEYER-031 | none | Pass | Ready: customer, user, guest operator | Pass | Pass | Pass | Pass | CK-REQ-C4 | finding-2 |
| REQ-SW-KEYER-032 | none | Pass | Ready: customer, user | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SW-KEYER-033 | none | Pass | Ready: customer, user, guest operator | Pass | Pass | Pass | Pass | CK-REQ-C4 | finding-2 |
| REQ-SW-KEYER-034 | none | Pass | Ready: customer, user, guest operator | Pass | Pass | Pass | Pass | CK-REQ-C4 | finding-2 |
| REQ-SW-KEYER-035 | none | Pass | Ready: customer, user, guest operator | Pass | Pass | Pass | Pass | CK-REQ-C4 | finding-2 |
| REQ-SW-KEYER-036 | none | Pass | Ready: customer, user, guest operator | Pass | Pass | Pass | Pass | CK-REQ-C4 | finding-2 |
| REQ-SW-KEYER-037 | none | Pass | Ready: customer, user | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SW-KEYER-038 | none | Pass | Ready: customer, user, guest operator | Pass | Pass | Pass | Pass | none | Pass |
| REQ-SW-KEYER-039 (iteration 2) | none | Pass | Pending: self-derived, Robin's concurrence pending (02 section 2.3) | Pass | Pass | Pass | Pass | CK-REQ-C4 | finding-2, finding-5, finding-6 |

V2 confirmation: carried by the paired record INSP-004 (its V2 block names every stakeholder group of 02 section 3.0 for these 38 requirements); this record adds no V2 cell that differs from it.

V6 notes: none beyond INSP-004; finding-4 would add one requirement, which is necessary because the running key-input mode is otherwise unprotected safety-critical state.

## Concurrence with INSP-004 (the paired file review of the same blobs)

- Concur with the closures of INSP-004 findings 2, 3, 4, 7 to 11, 14, 15 and 16 for the SW-KEYER file, re-checked on blob `db2de344`, except the item (d) part of finding-2: its disposition ("the keyer statement holds under either reading") does not survive 07 revision A.4 row d, which makes the keyer validate the two operator events itself; raised here as finding-1 (Major).
- Concur with INSP-004 finding-17 (reference points of REQ-SW-KEYER-016, 017, 026) as a Minor lien; not duplicated.
- INSP-004 front matter still reads `assurance_reviewer_agent: assurance:requirements-sw-keyer (separate invocation, not yet dispatched)` and `assurance_verdict: pending`; under 01 section 13 and 07 section 10.2 it should name this record (`paired_record: INSP-026`) and copy `assurance_verdict: NEEDS CHANGES` (cross item X-1).

## Observations (not findings)

1. The paired-record rule of 01 section 13 expects the assurance record to carry "the same `product` and product blobs" as the file review. INSP-004's `product` is the TX file and it names four blobs; this record names only the two SW-KEYER blobs, because the TX files are not a software product of 07 section 10.1 and need no assurance review. The two SW-KEYER blobs are identical to INSP-004's.
2. REQ-SW-KEYER-025 deliberately accepts a mode selection while an input reads closed (REQ-SYS-163, mono plug). This is safe only because the REQ-SW-KEYER-022 interlock re-runs on the new mode's inputs, which TC-SW-KEYER-025 `_disarmed` checks; the fix of finding-1 must keep that acceptance for the two-event sequence.
3. SWEHB topic 6.2 (PAT-007, checklist for general software safety requirements) is an attachment the corpus scrape does not hold; it was not applied. The per-SWE completeness of the SWEHB scrape is tracked by RSK-009.

## Cross items (for Claude; outside this reviewer's scope)

- **X-1.** INSP-004: set `paired_record: INSP-026`, name this record in `assurance_reviewer_agent` and copy `assurance_verdict` (07 section 10.2; 01 section 13).
- **X-2.** REQ-SYS-056 (L1 author) and `hazards.json` HZ-004 K2 (hazard analyst): align "an explicit menu selection" with 07 row d and `hazard-analysis.md` section 7 row d (menu action plus confirmation, validated by the receiving component).
- **X-3.** 07 author: add the key-input mode and Straight-input setting to the `SW-KEYER` row item f (finding-4).
- **X-4.** Package: carry L-1 to L-5 as Routine items; finding-1 (Major) is Verified at iteration 2 on `f2e02aa` and no longer held against H15 (row 25) or H1 (c); this record stays NEEDS CHANGES only on readiness R3 (decision 115).
- **X-5.** Hazard analyst: add REQ-SW-KEYER-039 to HZ-004 `requirement_ids` in `hazards.json` (finding-5); INSP-004 should note the new requirement and the revised blobs `4d22b399` and `d3c0c236` when it next iterates.

## Tool runs (2026-09-26, HEAD `adcfe09`)

| Command | Exit | Result |
|---|---|---|
| `.venv/bin/python tools/validate_docs.py` (before writing this record) | 0 | 40 passed, 0 failed |
| `.venv/bin/python tools/traceability.py --report-only` | 0 | 237 requirements, 170 test cases, 0 violations, 2 warnings (outside this product); the tracked report was rewritten with identical content (`git status` clean for `docs/vv/`) |
| `.venv/bin/python tools/validate_docs.py` (with this record) | 0 | 46 passed, 0 failed (the count includes records other reviewers filed concurrently); this record PASS against the built-in peer-review record schema |
| `.venv/bin/python tools/validate_docs.py` (iteration 2, HEAD `f2e02aa`, before this revision) | 0 | 47 passed, 0 failed, including both SW-KEYER products |
| `.venv/bin/python tools/traceability.py --report-only` (iteration 2) | 0 | 238 requirements, 170 test cases, 0 violations, 3 warnings (`HAZARD_INVERSE` REQ-SW-KEYER-039, finding-5; `SYS_UNALLOCATED` REQ-SYS-125, 148); the tracked `docs/vv/` report files it rewrote were restored with `git checkout` (outside this reviewer's scope) |
| `.venv/bin/python tools/validate_docs.py` (iteration 2, after this revision) | 0 | 47 passed, 0 failed; `PASS docs/reviews/SRR/checklists/requirements-sw-keyer-software-assurance.md` |

## Verdict

```
VERDICT: NEEDS CHANGES (iteration 2: held only by readiness R3; reviewer and assurance verdicts APPROVED with liens L-1 to L-5)
FINDINGS:
- [Major] SA-134-1, SA-134-4, SA-134-6, CK-REQ-C4 (V3) REQ-SW-KEYER-024, 029; TC-SW-KEYER-024, 029: SWE-134 d not implemented as 07 section 14.2 row d requires (finding-1, Verified at iteration 2 on f2e02aa).
- [Minor] CK-REQ-C4 safety requirements name no REQ-SW-SAFE-NNN row (finding-2, Lien: fix before PDR).
- [Minor] CK-REQ-C5, C6 key-down behavior at an accepted mode change unstated (finding-3, Lien: fix before PDR).
- [Minor] SA-134-1 item f: running key-input mode not integrity-protected (finding-4, Lien: fix before PDR).
- [Minor] CK-REQ-B5 REQ-SW-KEYER-039 not in HZ-004 requirement_ids (finding-5, Lien: fix before PDR).
- [Minor] CK-REQ-A1, A3 REQ-SW-KEYER-039 statement compressed; V2 concurrence pending (finding-6, Lien: fix before PDR).
ITEMS N/A: CK-REQ-G1 to G8, CK-REQ-B7, CK-REQ-C8, CK-REQ-D2, R5
MEASUREMENTS: size=39 requirements + 43 cases; rows=39; rows_with_wr_failures=0; v_fail=V1:0 V2:0 V3:0 V4:0 V5:0 V6:0; items_no=5; major=1; minor=5; open=0; verified=1; deferred(lien)=5; iteration=2; turns=52; minutes=80
```

Iteration 2: finding-1 is Verified on `f2e02aa`; every other finding is a Minor lien (L-1 to L-5), so the reviewer and assurance verdicts are APPROVED with liens and no Major finding is open. The record verdict stays NEEDS CHANGES only on readiness R3 (package decision 115), as INSP-023 iteration 2 does; it becomes APPROVED when R3 is met or waived. Iteration 1 text: the record verdict is NEEDS CHANGES on finding-1 (Major, then open) and, independently, readiness R3 (package decision 115). When finding-1 is fixed in the two files and verified at iteration 2 against the new committed blobs, the assurance verdict becomes APPROVED with liens L-1 to L-3; the record verdict follows once R3 is met or waived.

## Author self-check (readiness R3; package item R7; filed 2026-09-26)

**Written by the SW-KEYER requirements author, not the reviewer or the assurance function.** Author: `author:requirements-l2` (Claude in the requirements author role of 08 section 3.1, for REQ-SW-KEYER; the TC-SW-KEYER cases belong to the independent test author and are not self-checked here). This section is the author's return that readiness R3 of `docs/templates/peer-review-checklist-requirements.md` revision C asks for ("The author's return states the self-check against sections A to G below and lists the brief's acceptance criteria"). It is filed in this record because 01 section 13 says no record lives only in conversation and 07 section 10.2 (Readiness criteria row) says the brief's acceptance criteria are listed in the review record. The same author files the matching self-check for the paired file review in INSP-004 (`requirements-tx-and-sw-keyer.md`, section "Author self-check"), which also covers REQ-TX. Every other section of this record, the front matter, the R3 answer, the assurance task answers and `readiness_met` belong to the reviewer and the assurance function and are unchanged; the reviewer answers R3 again when it re-issues the record (package item R8). No product file was changed (convergence rule, charter section 4 item 3).

**Product state checked.** HEAD `5b1f2cf`. `git hash-object` of `sw/sw-keyer/requirements.json` equals the HEAD blob and the blob named in `product_files` (`4d22b399`), so the self-check applies to the blob this record read at iteration 2. `hazards.json` is now 0.4.3-pha (`c6bf757e`, commit `ade0e09`, OQ-SAF statuses only); the scan below used it.

**Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: where an author self-check and readiness R3 are recorded; decision 115 and the self-check location; the requirements author brief). `grep -n` and Python scans on known paths followed, only to pin lines.

**Method.** The Python scan described in the INSP-004 author self-check, applied to the 39 REQ-SW-KEYER entries, plus: the evidence classes of the cases citing each of the 19 hazard controls; `Depends on:` and `Fault tolerance:` on every `safety` requirement; `REQ-SW-SAFE` references; the self-derived set. Judgment items were answered by re-reading the requirements the scan, this record's findings and the 07 section 14.2 SW-KEYER row named.

### Brief's acceptance criteria

The authoring brief is not on record. The acceptance criteria are those of the INSP-004 author self-check (AC-1 to AC-12, from the 08 section 3.1 requirements row, 02, 07 section 14.2 and 04 section 5.2), restricted here to SW-KEYER, with the results on `4d22b399`:

| AC | Acceptance criterion | Result | Evidence |
|---|---|---|---|
| AC-1 | Validates against the requirement schema | Met | `tools/validate_docs.py`: PASS |
| AC-2 | No `tools/traceability.py` violation | Met, one warning | 0 violations; `HAZARD_INVERSE` REQ-SW-KEYER-039 (finding-5, lien; the hazard file belongs to the hazard analysis author) |
| AC-3 | Writing rules WR-01 to WR-14 | Met with liens and exception E-1 | Scan: 39 of 39 clean on WR-01, 07, 08, 12, 14. 039 wording is finding-6 (lien). Rationales of 024 (198 words), 029 (160) and 039 (215) exceed the 120 of 02 section 4.3 (E-1) |
| AC-4 | L1 parent or `Self-derived:` | Met | 034, 035, 036, 038, 039 lead with `Self-derived:`; the others name an L1 parent (package decision 112 for concurrence) |
| AC-5 | Hazard links; `safety` tag; SWE-184 `Depends on:`; `Fault tolerance:` | Met, except the 039 inverse link | 19 hazard controls, each `safety`, each with both items |
| AC-6 | Interface pairing | Met | REQ-SW-KEYER-001 tagged `interface` with ICD-CTL-KEY |
| AC-7 | Verification at definition; timing never closes on Emulation | Met | 39 Test; every note names its closing case, which cites the requirement; no Emulation closing class |
| AC-8 | Hazard controls verified by test (SWE-192) | Met | 19 of 19 have a Bench case (T-SW-TARGET); 18 also have a HostUnit case (observation O-1) |
| AC-9 | SWE-134 items of the 07 section 14.2 SW-KEYER row present | Met with liens | finding-1 Verified (item d: 024, 029, 039). finding-2 (no `REQ-SW-SAFE-NNN` reference; scan: 0) and finding-4 (item f for the mode) are liens |
| AC-10 | TBR policy; no TBD | Met | 11 TBRs (the ten of R4 plus 039), each complete with `close_by: PDR`; no TBD |
| AC-11 | Draft | Met | 39 of 39 |
| AC-12 | No em dash | Met | 0 |

### Self-check against checklist sections A to G

| Item | Author answer | Evidence |
|---|---|---|
| CK-REQ-A1 to A6, A8 | Yes | AC-3; A1 and A3 for 039 carry the finding-6 lien |
| CK-REQ-A7 | No (E-1) | E-1 |
| CK-REQ-B1, B2, B3 | Yes | AC-4; no duplicate description |
| CK-REQ-B4 | Yes | Straight key (001, 002) and paddles (003 to 010) |
| CK-REQ-B5 | Yes, except 039 | AC-2, AC-5 (finding-5) |
| CK-REQ-B6 | Yes | AC-5 |
| CK-REQ-B7 | N/A | Not a CR |
| CK-REQ-C1, C2, C3 | Yes | Timing on dot = 1200/WPM ms; ICD-CTL-KEY in `design_refs`; AC-5 |
| CK-REQ-C4 | No (liens) | finding-2, finding-4 |
| CK-REQ-C5 | No (lien) | finding-3 (mode change during key-down); no state name outside the architecture and ConOps list (scan) |
| CK-REQ-C6 | Yes, with finding-3 | Stuck key 026, corrupted state 030 and 034, keyer error 031, closure without plug 036, out-of-range settings 037 |
| CK-REQ-C7 | Yes | 038: no command path on the key line |
| CK-REQ-C8 | N/A | No loaded configuration record in SW-KEYER |
| CK-REQ-D1 | Yes | 019: 1.000 ms +/-0.010 ms sampling |
| CK-REQ-D2, D3 | N/A | No flash, RAM or crate value |
| CK-REQ-D4 | Yes | Tolerances argued in the rationales (reviewer D4 answer re-read) |
| CK-REQ-E1 to E6 | Yes | AC-7, AC-8 |
| CK-REQ-F1 to F4 | Yes | No duplicate or conflicting statement; ConOps spellings; module scope; `priority` set (Baseline 37, KDR 2), no `should` |
| CK-REQ-G1 to G8 | N/A | Not a plan |

**Author exception E-1 (new, Minor, for the reviewer to disposition).** The same as E-1 of the INSP-004 author self-check: the `f2e02aa` fix of finding-1 took the rationales of REQ-SW-KEYER-024 to 198 words and 029 to 160, and added 039 with 215, against the 120-word limit of 02 section 4.3 (at `db2de344` none exceeded 120). Proposed fix before PDR under the convergence rule; no product change in this run.

**Author observation O-1 (for the assurance evidence, not a product defect).** SA-192-1 (iteration 2) states that each of the 19 hazard controls has "a HostUnit and a Bench case". REQ-SW-KEYER-019 (sampling period) has only its Bench closing case TC-SW-KEYER-019; its note names the HostUnit sampling-schedule check as supporting evidence without a case. SWE-192 and CK-REQ-E3 are met by the Bench test.

### Author's statement

The self-check agrees with this record's iteration 2 reviewer and assurance answers and disputes no finding. It adds one Minor discrepancy (E-1) and one evidence observation (O-1). finding-2 to finding-6 are liens the author fixes before the PDR readiness declaration (finding-5 with the hazard analysis author). Commands: `tools/validate_docs.py` before this section: exit 1, 47 passed, 1 failed, 48 checked; the one failure is `docs/reviews/SRR/checklists/hazard-analysis.md` (record drift against the hazard files committed at `ade0e09`), outside this record and present before the edit. `tools/traceability.py --report-only` (output to the scratchpad): exit 0, 238 requirements, 170 test cases, 0 violations, 3 warnings.

## Re-issue (2026-09-26, SRR package item R8; no further product review)

**Scope and independence.** Written by a new invocation of `reviewer:INSP-026` in the reviewer role, which is also the software assurance function for this record (charter section 2). It did not author the SW-KEYER requirements or test cases or the author self-check above, it is not the INSP-004 file reviewer, and it edited no product file and no author section. It re-issues this record without a further product review, as package item R8 provides once the author self-check of item R7 exists. The convergence rule of 2026-09-26 (charter section 4 item 3) applies: only Major findings change products, and every Minor finding stays a lien, "fix before PDR".

**Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: peer review record readiness fields R1 to R4 with the author self-check and `readiness_met`; the TC-SYS-060 bracket and INSP-025, for the sibling record). `grep -n` then only pinned lines in `tools/validate_docs.py`, `docs/process/02-requirements-and-traceability.md` and the records.

**Product state.** HEAD `1af795c`. `git rev-parse HEAD:<path>` and `git hash-object` equal the blobs named in `product_files`: `requirements.json` `4d22b399`, `test_cases.json` `d3c0c236` (last changed in `f2e02aa`, the blobs iteration 2 reviewed). No product changed since iteration 2, so no delta verification is needed. One input changed: `docs/safety/hazards.json` 0.4.2-pha to 0.4.3-pha (`ade0e09`, OQ-SAF-007, 025 and 026 statuses only; no control or `control_req_ids` changed), so finding-5 stands as written (REQ-SW-KEYER-039 is still not in HZ-004 `requirement_ids`; recomputed at HEAD).

**Readiness R3 against the author self-check.** R3 of `docs/templates/peer-review-checklist-requirements.md` revision C reads "The author's return states the self-check against sections A to G below and lists the brief's acceptance criteria". The section "Author self-check" (filed at `1af795c`) meets it:
- It lists twelve acceptance criteria (AC-1 to AC-12, those of the INSP-004 self-check restricted to SW-KEYER), each with a result and evidence on `4d22b399`; the governing sources are named in the INSP-004 self-check it points to. The authoring brief is not on record; taking the criteria from the documents the 08 section 3.1 requirements row names, with 07 section 14.2 for the SWE-134 items, is acceptable for R3, because every criterion traces to a governing document and none is weaker than the checklist.
- It answers every item of sections A to G (B7, C8, D2, D3 and G1 to G8 as N/A with reasons), and its "No" answers (A7, C4, C5) are this record's finding-2, 3, 4 and the new finding-7.
- It names the blob it checked, which equals `product_files` and HEAD (confirmed above), and says the test cases belong to the independent test author.

**Spot checks of the author's claims at HEAD** (read-only Python over `git show HEAD:<path>`):
- AC-5: 19 requirements with `hazard_ids`, each with both a `Depends on:` and a `Fault tolerance:` item. Agrees.
- AC-4: `Self-derived:` leads REQ-SW-KEYER-034, 035, 036, 038 and 039. Agrees.
- AC-7: all 39 requirements use Test. Agrees.
- AC-9 and finding-2: no `REQ-SW-SAFE` reference in the file (0). Agrees.
- AC-3 and E-1: rationales of REQ-SW-KEYER-024 198, 029 160 and 039 215 words. Agrees.
- O-1: of the 19 hazard controls, REQ-SW-KEYER-019 alone has no HostUnit case; its closing case TC-SW-KEYER-019 is Bench. Agrees (see erratum below).

**Author exception E-1.** Confirmed against 02 section 4.3 (120-word limit); rated Minor as WR-10 (02 section 4.2). The safety content of the three rationales is not in question (finding-1 Verified at iteration 2). Raised as finding-7, "Lien: fix before PDR" (L-6), owner the SW-KEYER requirements author; INSP-004 raises the same defect as its finding-20, and one fix closes both.

**Erratum to SA-192-1 (reviewer evidence, not a product finding).** The iteration 2 evidence of SA-192-1 says each of the 19 hazard-tracing requirements has "a HostUnit and a Bench case". At `d3c0c236` 18 do; REQ-SW-KEYER-019 (the 1 kHz sampling period) has only its Bench closing case TC-SW-KEYER-019 (T-SW-TARGET), and its note names the HostUnit sampling-schedule check as supporting evidence without a case. SWE-192 task 1 asks that requirements tracing to a hazard are verified through test, which the Bench on-target case does, so the SA-192-1 answer stays Yes; only the evidence wording is corrected here. Whether a HostUnit case for the sampling schedule is wanted is the test author's call at PDR (cross item X-6).

- **X-6.** Test author: decide whether REQ-SW-KEYER-019 gets a HostUnit case for the sampling schedule its note names, or the note drops the reference (PDR).

**Pairing (01 section 13; 07 sections 2.1.1 and 10.2).** This record names the SW-KEYER `product` and blobs of INSP-004 and `paired_record: INSP-004`. INSP-004 is re-issued the same day with `paired_record: INSP-026`, `assurance_reviewer_agent` naming this record and `assurance_verdict: APPROVED`, which equals this record's verdict; cross item X-1 is done. X-4 (package carriage of the liens) now includes L-6.

**Findings at the re-issue.**

| Finding | Severity | State | Closes on |
|---|---|---|---|
| finding-1 | Major | Closed (Verified, iteration 2, on `f2e02aa`) | |
| finding-2 to finding-6 | Minor | Lien: fix before PDR | L-1 to L-5 (iteration 2 lien table) |
| finding-7 | Minor | Lien: fix before PDR (new) | L-6: SW-KEYER requirements author, PDR readiness declaration |

No Major finding is open, so no finding needs an owner ruling or a package decision number. Package decision 115 (waiver of the self-check) is no longer needed for this record. The V2 concurrence of the self-derived requirements (package decision 112) governs the baseline status of the Draft file, not a finding of this record.

**Answers changed at the re-issue.** R3 changes from No to Yes. CK-REQ-A7 changes from Yes to No (finding-7, lien). CK-REQ-C4, C5, SA-134-1 and SA-134-6 stay No (liens finding-2 to finding-4). R1, R2 and R4 stay Yes (R2: 0 violations; the `HAZARD_INVERSE` warning for REQ-SW-KEYER-039 is finding-5); R5 stays N/A. `readiness_met: true`. Reviewer verdict, assurance verdict and record verdict: APPROVED with liens finding-2 to finding-7.

**Tool runs at the re-issue (2026-09-26, HEAD `1af795c`, repository root, `.venv/bin/python`).** `tools/traceability.py --report-only`: exit 0, 238 requirements, 170 test cases, 0 violations, 3 warnings (`HAZARD_INVERSE` REQ-SW-KEYER-039, finding-5; `SYS_UNALLOCATED` REQ-SYS-125 and 148); the rewritten `docs/vv/traceability-report.md` and `traceability.json` were restored with `git checkout` (outside this scope). `tools/render_risk.py --check --gate SRR --hazards docs/safety/hazards.json`: exit 0. `tools/validate_docs.py` after this re-issue (record drift check included): exit 1, 48 passed, 1 failed, 49 checked; this record PASS with no drift note; the one failure is `docs/reviews/SRR/checklists/hazard-analysis.md` (record drift against the hazard files committed at `ade0e09`), outside this scope and present before this re-issue. `python -m unittest discover -s tools/tests`: 392 tests, 391 pass; the one failure is `test_validate_docs.RepositoryTests.test_repository_exit_zero` on the same `hazard-analysis.md` drift. HEAD moved to `09d48be` during this re-issue through other reviewers' record commits only (`git diff --name-only 1af795c 09d48be` lists 11 files, all under `docs/reviews/SRR/checklists/`), so the product blobs named here are also the blobs at `09d48be`.

**Editorial change to earlier reviewer text (no content change).** The open-Major rule of `tools/validate_docs.py` (`open_major_findings`, line 664) reads any body line that names a `finding-<n>` and contains both the words "Major" and "Open" as an open Major finding. The iteration 2 verdict paragraph quoted the iteration 1 state of the Major finding with the capitalized state word; this re-issue wrote "(Major, then open)" there. No finding state, count or answer changed.

**Measurements (re-issue, SWE-089).** Items re-checked: R1 to R5, six author claims, finding-5 against `hazards.json` 0.4.3-pha and the two product blobs; items answered No: 5 (CK-REQ-A7, C4, C5, SA-134-1, SA-134-6, all on liens); new findings: 1 (finding-7, Minor); effort 12 turns, 20 minutes (added to the front matter totals).

```
RE-ISSUE (2026-09-26, HEAD 1af795c, package item R8): VERDICT: APPROVED (with liens finding-2 to finding-7); reviewer APPROVED; assurance APPROVED; paired file review INSP-004
FINDINGS: finding-1 Major Closed (iteration 2); finding-2 to finding-7 Minor, Lien: fix before PDR (L-1 to L-6); open Major 0
READINESS: R1 Yes, R2 Yes, R3 Yes (author self-check at 1af795c verified), R4 Yes, R5 N/A; readiness_met true
PRODUCTS: sw-keyer/requirements.json@4d22b399, sw-keyer/test_cases.json@d3c0c236 (unchanged since f2e02aa)
MEASUREMENTS: re-issue no=5; new findings=1; turns=12; minutes=20; cumulative turns=64, minutes=100
```

`record_status` stays Open: the liens are neither Verified nor Deferred by an owner decision, and the software lead closes the record (07 section 10.2, action tracking).

## Post-SRR-ruling delta (2026-09-26, iteration 3)

**Scope and independence.** Written by a new invocation of `reviewer:INSP-026` in the reviewer role, which is also the software assurance function for this record (charter section 2). The owner approved the SRR on 2026-09-26 (disposition Approved with liens L-1 to L-7, `docs/reviews/SRR/minutes.md`) and ruled every decision of `docs/reviews/SRR/decisions-for-owner.md` as recommended. This section delta-verifies every commit since the re-issue that touched the products, under the assurance lens. This reviewer authored none of the changed files and edited no product, no author section and no earlier reviewer text; the sections above are the historical record and are unchanged except the front matter fields that carry the current state and the dated verdict line added above the re-issue verdict. The convergence rule of 2026-09-26 (charter section 4 item 3) applies: only a Major finding changes a product, and every Minor finding is a lien, "fix before PDR", carried by SRR lien L-6.

**Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (query: SRR decision 48 menu tunables debounce and decision 50 debounce values ratified). `grep -n` then only pinned decision rows 9, 37, 41, 43, 44, 47, 48, 50 and 112 in `decisions-for-owner.md`, OQ-SAF-027 in `hazards.json` and the checklist item wording; read-only Python over `git show <rev>:<path>` produced the field-level diffs, the rationale word counts, the HZ-004 control links and the `allocation.json` rows.

**Commits reviewed.** `git log f2e02aa..HEAD -- <both products>` lists four commits; `5f647f2` and `1af795c` change neither product (records only; `git show --stat`), so two product commits are in scope:
- `cd61450` "Requirements: apply SRR owner rulings of 2026-09-26 to L1 and L2 (package item R16)": `requirements.json` 4d22b399 to f9141160 (18 insertions, 17 deletions), 16 field changes in 13 requirements; no statement (`description`), `verification_method`, `hazard_ids` or `tags` changed; one `source_ids` change.
- `ebe5873` "Test cases: apply SRR owner rulings of 2026-09-26 to TC-SYS, TC-TX and TC-SW-KEYER (package item R16)": `test_cases.json` d3c0c236 to 2716ca3f, the `setup` field of four cases only; no step, acceptance criterion, `requirement_ids` or type changed.

**Delta verification, change by change** (each against the Recommendation cell of the cited decision, which is the ruling text).

| Location | Change | Ruling cited | Assurance judgment |
|---|---|---|---|
| REQ-SW-KEYER-007, 010 `rationale` | "D-KN1, Proposed, owner decision pending at SRR" becomes "adopted by SRR decision 43" | 43: all five modes, Iambic A default | Correct; no behavior change |
| REQ-SW-KEYER-020, 021 `rationale` | Records that decision 50 ratified 2 ms make and 5 ms break (TBR until the bounce capture) and that decision 48 names the debounce among the menu tunables, which the fixed counts do not provide; the conflict is carried to PDR | 50: ratify, debounce closes by the bench capture; 48: expose switchpoint and debounce only | Decision 50 applied correctly. Decision 48 is not applied to the statements; the author states the conflict instead of changing a safety requirement, and the hazard analyst raised OQ-SAF-027 (`hazards.json` 0.5.0-pha). From the assurance side this is the right handling: an operator-set make filter above 2 samples would break REQ-SW-KEYER-017 and the fixed counts on which HZ-004 K9 and HZ-010 K3 rest, so the safer fixed count stands until the owner decides. The unresolved disagreement between the file and a ruling is finding-9 (Minor). Both rationales now exceed 120 words (finding-10) |
| REQ-SW-KEYER-022 `rationale`, `tbr.plan` | Decision 50 ratified the 500 ms interlock; TBR kept to PDR for the HostUnit bounce study | 50 | Correct; TBR complete (owner, plan, `close_by: PDR`) |
| REQ-SW-KEYER-024 `rationale` | D-KN8 "adopted by SRR decision 44 ... menu selection only in revision A"; the override command path is safety-critical "as SRR decision 9 ... concurs" | 44: menu only in revision A; 9: override command path safety-critical as 03 proposes | Correct. The receiving-side validation of finding-1 is kept word for word (menu output an untrusted request, one-sample and one-queued-event rejection), and it now holds with the concurrence rather than regardless of it, so the SWE-134 d implementation is unchanged |
| REQ-SW-KEYER-026 `rationale`, `tbr.plan` | D-KN3 "adopted by SRR decision 37"; TBR plan: 5 s adopted, the HostUnit study at PDR confirms it "and fixes the configurable range (2 to 6 s)" | 37: 5 s manual timeout including the Bug dah | 5 s and the Bug dah agree with the ruling. The retained "configurable range (2 to 6 s)" is not among the tunables decision 48 exposes; part of finding-9 |
| REQ-SW-KEYER-032 `rationale`, `tbr`, `source_ids` | Decision 47 adopted the 3 to 30 dit range and accepted ADR-026 (superseding ADR-010, hang kept in SW-KEYER); ADR-026 added to `source_ids` | 47: adopt as written and accept ADR-026 | Correct; statement "3 to 30 dits (TBR) of the displayed speed" equals the ruling; ADR-010 kept in `source_ids` as history, ADR-026 added (SRR lien L-7 item) |
| REQ-SW-KEYER-034, 035, 036, 038, 039 `rationale` | "Robin's concurrence is pending in the V2 record" becomes "Robin concurred ... by SRR decision 112" | 112: concur with all five | Correct; closes the V2 part of finding-6 (the statement part stays) |
| TC-SW-KEYER-019, 038 `setup` | The paddle-watchdog note now names REQ-SYS-054 and the 2 s squeeze limit REQ-SYS-184, "adopted by SRR decision 37" | 37: the HZ-004 K4 no-gap watchdog with the 2 s squeeze limit | Correct. Single-paddle PARIS at 50 and 20 WPM has word gaps of 7 dits and no squeeze, so neither case reaches the watchdog or the squeeze limit; TC-SW-KEYER-038 straight-key holds of at most 4 s stay below the 5 s of REQ-SW-KEYER-026 |
| TC-SW-KEYER-037 `setup` | "bench test modes force it: REQ-SYS-187, HZ-004 K13, adopted by SRR decision 41" | 41: forced 0.5 W, 120 s timeout, exit on reset, not persistent | Correct; the case keys the generator for 30 s (step 8) and waits 60 s unconfirmed (step 6), both inside the 120 s mode timeout of REQ-SYS-188, and step 6 restarts through reset as REQ-SYS-190 requires |
| TC-SW-KEYER-034 `setup` | The "TBR values" sentence adds REQ-SW-KEYER-036 | none cited | Correct in substance: REQ-SW-KEYER-036 is in the case's `requirement_ids` and carries a TBR, so the sentence was incomplete before. The change cites no decision and the commit message does not list it (observation 4) |

No change weakens a safety requirement, removes a hazard link or a closing case, or alters an acceptance criterion. `traceability.py --report-only` at HEAD reports no violation or warning for any REQ-SW-KEYER or TC-SW-KEYER id. **No new Major defect.**

**Findings resolved by the rulings.** No Major finding was open at the re-issue (finding-1 Verified at iteration 2), so no Major closes here. Two Minor findings are affected:
- finding-5 is **Verified**: `hazards.json` 0.5.0-pha (`bfea9c7`, package item R16) adds REQ-SW-KEYER-039 to HZ-004 `requirement_ids` and to the `control_req_ids` of K2 and K13 (recomputed at HEAD), as SRR decision 112 (owner ruling 2026-09-26) directs; the `HAZARD_INVERSE` warning is gone (`traceability.py --report-only`, below).
- finding-6 is **partly resolved**: the V2 concurrence it named is recorded by SRR decision 112 in `cd61450`; the compressed statement of REQ-SW-KEYER-039 is unchanged at f9141160, so the lien stands for the statement only.

**New findings (Minor, liens due PDR).**
- **finding-8** (SA-134-1, CK-REQ-B5, V6). SRR decision 41 adds REQ-SYS-188 (bench test mode left at most 120 s after entry, HZ-004 K13), and `allocation.json` 0.3.0-srr allocates it to `SW-SAFE` and `SW-KEYER` with the note "SW-KEYER owns the test-mode generator (REQ-SW-KEYER-029); SW-SAFE the mode timeout". No REQ-SW-KEYER requirement is its child (`child_ids` empty), and neither REQ-SW-KEYER-028 nor 029 states that the PARIS generator stops, with key-down idle, when the test mode ends (timeout, exit or reset); HZ-004 K13 lists 028, 029 and 039 as its keyer controls. Minor because the L2 file is Draft with its baseline at PDR, the timeout itself belongs to the `SW-SAFE` file that does not exist yet, and the L1 note for the sibling REQ-SYS-184 already plans the SW child at PDR. Fix: add a keyer requirement (or extend REQ-SW-KEYER-029) that the generator stops and key-down goes idle within 1 ms of the test mode ending, tagged `safety` with HZ-004, with a HostUnit case and the on-target step in TC-SW-KEYER-037.
- **finding-9** (CK-REQ-F1). SRR decision 48 rules that the switchpoint and the debounce are exposed in the menu and the other timing values stay build-time defaults. REQ-SW-KEYER-020 and 021 still fix the debounce counts as "not operator-configurable", REQ-SW-KEYER-037 range-checks no debounce setting, and the REQ-SW-KEYER-026 TBR plan still names a "configurable range (2 to 6 s)" for the manual-closure timeout, which decision 48 does not expose. The file thus disagrees with an owner ruling in two directions. The author recorded the debounce conflict and OQ-SAF-027 tracks it, so it is visible and the safe fixed counts hold meanwhile. Assurance condition for the resolution: if the owner keeps the debounce operator-set, the range must keep the make filter inside the 2 ms of REQ-SW-KEYER-017 and the break filter at 6 samples or fewer, REQ-SW-KEYER-037 must reject out-of-range debounce values as safety-critical loaded data (SWE-134 item 3 task, SA-134-3), and HZ-004 K9 and HZ-010 K3 are restated; otherwise a CR records the owner keeping the counts fixed. The 026 plan either drops "configurable" or the owner adds the timeout to the tunables.
- **finding-10** (CK-REQ-A7, WR-10). `cd61450` lengthened the rationales of REQ-SW-KEYER-020 from 116 to 174 words and 021 from 120 to 156, past the 120-word limit of 02 section 4.3; 024 (208), 029 (160) and 039 (220) stay over it (finding-7). Same defect class as finding-7; one fix closes both.

**Findings at iteration 3.**

| Finding | Severity | State | Closes on |
|---|---|---|---|
| finding-1 | Major | Closed (Verified, iteration 2, on `f2e02aa`) | |
| finding-2 | Minor | Lien: fix before PDR | L-1 (unchanged; the `SW-SAFE` file is still Planned) |
| finding-3 | Minor | Lien: fix before PDR | L-2 (unchanged; no ruling addresses key-down at a mode change) |
| finding-4 | Minor | Lien: fix before PDR | L-3 (unchanged) |
| finding-5 | Minor | Verified (iteration 3; `bfea9c7`, SRR decision 112) | |
| finding-6 | Minor | Lien: fix before PDR (statement only; V2 concurrence recorded by SRR decision 112 in `cd61450`) | L-5 |
| finding-7 | Minor | Lien: fix before PDR | L-6 (with finding-10) |
| finding-8 | Minor | Lien: fix before PDR (new) | L-7: SW-KEYER requirements author and test author, with the `SW-SAFE` file |
| finding-9 | Minor | Lien: fix before PDR (new) | L-8: owner ruling on OQ-SAF-027 at PDR; SW-KEYER requirements author; hazard analyst for K9, K3 |
| finding-10 | Minor | Lien: fix before PDR (new) | L-9: SW-KEYER requirements author (one fix with finding-7) |

L-7 to L-9 are this record's lien numbers and are carried by SRR lien L-6 (every Minor finding of the review records, fix before PDR). No Major finding is open and none waits on an owner ruling.

**Answers changed at iteration 3.** CK-REQ-B5 stays Yes and its only exception (finding-5) is Verified. CK-REQ-F1 changes from Yes to No (finding-9, lien). SA-134-6 stays No, now on finding-4 alone. SA-134-1 stays No (finding-4, finding-8). CK-REQ-A7 stays No (finding-7, finding-10). SA-134-3 stays Yes for the settings the file defines; finding-9 records the condition for a debounce setting. R1 to R4 stay Yes, R5 N/A; `readiness_met: true`.

**Observations (not findings).**
4. The TC-SW-KEYER-034 `setup` change in `ebe5873` (REQ-SW-KEYER-036 added to the TBR-values sentence) applies no SRR decision and is not in the commit message; it is a correct completeness fix, noted for configuration traceability.
5. `traceability.py --report-only` at HEAD reports four `HAZARD_REQ_NOT_TESTED` violations on REQ-SYS-122, 124, 137 and 138, retyped Inspection by SRR decision 113 (CR-002) in `cd61450`. They are outside this product; cross item X-7.

**Cross items.**
- **X-7.** L1 author and the INSP-001 reviewer: REQ-SYS-122, 124, 137, 138 fail rule 7.3.6 after the decision 113 retype (4 violations at `ebe5873`).
- **X-8.** INSP-004 (paired file review of the same blobs): note blobs f9141160 and 2716ca3f and findings 8 to 10 when it records its post-ruling delta; the assurance verdict to copy is APPROVED.
- **X-9.** Hazard analyst: resolve OQ-SAF-027 with the owner before PDR (finding-9) and add the finding-8 keyer requirement to HZ-004 K13 once written.

**Tool runs at iteration 3 (2026-09-26, HEAD `ebe5873`, repository root, `.venv/bin/python`).** `tools/traceability.py --report-only`: exit 0 (report-only mode), 245 requirements, 173 test cases, 4 violations (REQ-SYS-122, 124, 137, 138, observation 5), 2 warnings (`SYS_UNALLOCATED` REQ-SYS-125, 148); none on a REQ-SW-KEYER or TC-SW-KEYER id and no `HAZARD_INVERSE` warning; `docs/vv/traceability-report.md` and `traceability.json` restored with `git checkout`. `tools/validate_docs.py` with this section: exit 1, 39 passed, 11 failed, 50 checked; this record PASS (no drift: both `product_files` blobs equal HEAD); the eleven failures are other SRR records (drift against the R16 product commits, being re-issued by their own reviewers concurrently), outside this scope.

**Measurements (iteration 3, SWE-089).** Items re-checked: 16 requirement field changes, 4 case setup changes, 9 rulings, finding-5 and finding-6; items answered No: 6 (CK-REQ-A7, C4, C5, F1, SA-134-1, SA-134-6, all on liens); new findings: 3 Minor; verified: 1 (finding-5); effort 22 turns, 35 minutes (added to the front matter totals).

```
ITERATION 3 (2026-09-26, HEAD ebe5873, post-SRR-ruling delta, package item R16): VERDICT: APPROVED (with liens finding-2, 3, 4, 6, 7, 8, 9, 10); reviewer APPROVED; assurance APPROVED
DELTA: cd61450 (requirements.json 4d22b399 -> f9141160), ebe5873 (test_cases.json d3c0c236 -> 2716ca3f); rulings 9, 37, 41, 43, 44, 47, 48, 50, 112 checked; no new Major
FINDINGS: finding-1 Major Closed; finding-5 Minor Verified (decision 112, bfea9c7); finding-8, 9, 10 Minor new liens; open Major 0
MEASUREMENTS: size=39 requirements + 43 cases; items_no=6; major=1; minor=9; open=0; verified=2; deferred(lien)=8; turns=22; minutes=35; cumulative turns=86, minutes=135
```
