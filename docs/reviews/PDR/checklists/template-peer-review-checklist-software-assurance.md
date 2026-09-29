---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md section 13
# is the single field list; docs/process/08-agent-briefing.md section 3.2). Checklist:
# docs/templates/peer-review-checklist-requirements.md revision C, section G and CK-REQ-A8, as PDR work plan
# WP-PDR-03 names. Product: the new software assurance checklist template of CR-012 (Submitted, Class II),
# frozen on branch cr/CR-012-pdr-checklist-templates at ac9b7a5 for iteration 1 and at 7784672 for the
# iteration 2 delta (rule C2). The 08 delta and the CR-012
# checks shared by the three WP-PDR-03 records are in INSP-031
# (docs/reviews/PDR/checklists/template-peer-review-checklist-analysis.md).
id: INSP-032
checklist: peer-review-checklist-requirements
checklist_revision: C
checklist_file: docs/reviews/PDR/checklists/template-peer-review-checklist-software-assurance.md
product: docs/templates/peer-review-checklist-software-assurance.md
# product_commit: iteration 2 delta at the branch head 7784672 (iteration 1: ac9b7a5). Iteration 3 (delta, 2026-09-29,
# CR-012 pre-merge check 2): the CR-015 branch head 7efd900 (base 7784672), which holds the combined 08 blob and the
# three template blobs unchanged
product_commit: "7efd900b4011a7959f99bef00cba3a0b732cf8b1"
# product_files iteration 3: 08 56c54011 replaced by 374fd777 (git rev-parse 7efd900:<path>, the blob main holds after
# the CR-015 merge). The CR file entry "docs/cm/cr/CR-012-pdr-checklist-templates.md@91c8c6261a4b2bd9b3d789676c1188b54f022ddd"
# is dropped (CR-012 IR-F5; INSP-060 precedent at fd12ced): the CR file is a record on main appended at each lifecycle
# step, so a pinned blob never equals HEAD after the merge (section "Iteration 3"). The three template blobs are unchanged.
product_files: ["docs/templates/peer-review-checklist-software-assurance.md@5b13528504868b2add0f0b1e329c63aa2b54cdf4", "docs/templates/peer-review-checklist-tool-validation.md@7be809d4ceb9a202473eb19da3627fe0cd427900", "docs/templates/peer-review-checklist-analysis.md@0386cc6e78da65578b1cce8b2f793cd3db224921", "docs/process/08-agent-briefing.md@374fd777b1f05e408c133ed1f222b6cb90865114"]
product_size: 1 template (229 lines, sections R, A to F, SWE-to-task table of 8 product types plus the row "Every product type")
sprint: PDR-prep
author_agent: "author:WP-PDR-03 (Claude as checklist owner)"
reviewer_agent: "reviewer:WP-PDR-03-templates"
criticality: neither
# assurance_required: true. This template is the closure of 07 section 15 row "5.17 item 13: SA
# requirements mapping and tasking", so it is part of the software assurance plan (NPR 7150.2D 6.1 item k,
# 07 section 15); 07 section 2.1.1 row "Software plans" is Yes in every column, and SWEHB swe-087 section
# 7.1 task 3 is "Perform peer reviews on software assurance and software safety plans". The assurance
# reviewer is a separate invocation (rule C4); it was not yet assigned at iteration 2 (fix request "SA pair needed").
# Iteration 3: the pair is filed as INSP-046 (template-peer-review-checklist-software-assurance-software-assurance.md,
# commit d566e01, iteration 1, assurance_verdict APPROVED on the 7784672 blobs). This record takes paired_record and
# assurance_reviewer_agent from it (01 section 13 paired form; 07 section 10.2); the reviewer of this record makes that update.
assurance_required: true
assurance_reviewer_agent: "sa-reviewer:WP-PDR-03-templates (INSP-046 iteration 1, APPROVED on the 7784672 blobs; its re-pin delta on 08 374fd777 is pending, a software assurance invocation)"
paired_record: INSP-046
# iteration 3: delta for the CR-012 and CR-015 merge batch (CR-012 section 9 pre-merge check 2, record delta 2)
iteration: 3
readiness_met: true
# reviewer_verdict: APPROVED at iteration 2 (finding-1 Verified; finding-2 and finding-3 Minor liens, rule C1); unchanged at
# iteration 3 (no new finding in this record; INSP-031 finding-3 covers this template's completion criteria)
reviewer_verdict: APPROVED
# assurance_verdict: at iteration 2 the paired assurance record was not yet filed. Iteration 3: equal to the verdict of the
# filed pair INSP-046 (assurance_verdict APPROVED, iteration 1), as 01 section 13 requires of a file review with a paired record
assurance_verdict: APPROVED
# verdict: held at NEEDS CHANGES (a) until the paired assurance record is APPROVED (07 section 10.2) and
# (b) while the reviewed blobs are on the CR branch only: tools/validate_docs.py fails an APPROVED record
# whose product_files are not in main HEAD (record drift rule; same hold as INSP-031). The software lead
# sets APPROVED when both conditions clear (section "Iteration 2", "Record verdict")
# Iteration 3: (a) now reads: INSP-046 is APPROVED but still names 08 56c54011 and the CR file at 91c8c626; its re-pin delta
# (software assurance role) must name the same four blobs as this record (07 section 10.2). (b) now reads: the 08 blob is the
# CR-015 one, so the software lead sets APPROVED on both records in the CR-015 merge commit (or the commit right after it)
verdict: NEEDS CHANGES
findings_major: 1
findings_minor: 2
# findings_open: 0 at iteration 2; finding-2 and finding-3 (Minor) are liens due the CDR readiness declaration
# (PDR work plan rule C1, lesson L1), listed in the iteration 2 lien table, not Deferred RIDs
findings_open: 0
findings_fixed: 0
findings_verified: 1
findings_deferred: 0
assurance_findings_major: 0
assurance_findings_minor: 0
assurance_tasks_applied: []
deferred_rids: []
# items_no: CK-REQ-G1 stays No on finding-3 (lien) although finding-1 is Verified; CK-REQ-G2 stays No on finding-2 (lien)
items_no: [CK-REQ-G1, CK-REQ-G2]
# effort: iteration 1 (16 turns, 30 min) plus iteration 2 delta (16 turns, 25 min) plus iteration 3 delta (8 turns, 15 min)
effort_turns: 40
effort_minutes: 70
record_status: Open
date: 2026-09-27
date_closed: null
---

# Peer review record INSP-032: software assurance checklist template (WP-PDR-03, CR-012)

**Product:** `docs/templates/peer-review-checklist-software-assurance.md`, blob `22b7b6af`, on branch `cr/CR-012-pdr-checklist-templates` at `ac9b7a5` (identity checked with `git ls-tree ac9b7a5`). **Checklist:** `docs/templates/peer-review-checklist-requirements.md` revision C, section G and CK-REQ-A8 (PDR work plan WP-PDR-03). **Acceptance criteria (rule C7):** the plan output "NASA-STD-8739.8 style SA items as far as the corpus allows; 07 §2.1.1", the 07 section 15 row "5.17 item 13" closure (a SWE-to-task table that plans the SWEHB section 7.1 tasks per product type), every product type 07 section 2.1.1 marks Yes, every SWE-134 item a to l (NPR 7150.2D 3.7.3), and every safety-critical designated task of SWEHB topic 8.10 section 6 for the products the table routes.

**Independence (rule C4):** this invocation authored no part of WP-PDR-03 or CR-012 and edited no product file. **Search first:** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: SWEHB 8.10 section 6 safety-related SA tasks; peer review record of a checklist template). `grep` and a Python extraction of the SWEHB section 7.1 lists were used afterwards only to pin tasks.

**Software assurance participant.** This record is the file review. The SA second review of this template is required (see the front matter) and is not performed here: a reviewer does not apply both lenses (rule C4; 07 section 2.1). The record `verdict` stays NEEDS CHANGES until the paired assurance record is APPROVED.

## Record

### Findings

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | reviewer | Major | CK-REQ-G1 | Section B table (lines 145 to 154) and the task-table rule (line 117, line 143) | Section B leaves out safety-critical (SC) tasks that SWEHB topic 8.10 section 6 lists as tasks that "must be performed for Safety Critical software", for products it routes, and the task table is limited to "one row per task of the section B row", which narrows 07 section 15 ("the `# 7. Software Assurance` section ... of the SWEHB page for each SWE the product implements"). Missing: (a) `swe-134` 7.1 task 3 (SC: "Confirm that the values of the safety-critical loaded data, uplinked data, rules, and scripts that affect hazardous system behavior have been tested"), in no row, although the configuration guard's persisted record is safety-critical loaded data (07 section 14.1) and the test row carries `swe-193`; (b) `swe-036` 7.1 tasks 1 and 2 (both SC; `rmm.json` SWE-036 FC; 07 section 1.3 implements SWE-036) in the `plans` row; (c) `swe-134` task 5 (SC, participate in reviews of safety-critical products) and `swe-022` task 1 (SC; relief `rmm.json` SWE-022 T) in no row, where the table should show them as met by the review itself and as relieved; (d) `swe-068` task 3 (SC; `rmm.json` SWE-068 FC; test results as verification artifacts for the hazard reports) in no row; (e) the SC tasks of `swe-015`, `swe-151`, `swe-016` and `swe-174` belong to products 07 section 2.1.1 does not route (cost, schedule, Center reporting), which the section should state so that their absence is a decision, not a gap. Fix: add (a) to the `test` and `code` rows, (b) to `plans`, (c) and (d) as stated, (e) as a note; and add to the task-table rule that the reviewer also applies the section 7.1 tasks of any other SWE the product implements (07 section 15) | Open | Pending | |
| <a id="finding-2"></a>finding-2 | reviewer | Minor | CK-REQ-G2 | Section B `product_type` list (lines 34 to 36, 145 to 154); `peer-review-checklist-analysis.md` lines 55 to 62 | The analysis template says an analysis record whose product path or slug carries the `sw-<sub>` token of a 07 section 14.1 module "is then held with the assurance reviewer" (because `tools/validate_docs.py` requires one). This template has no `product_type` for an analysis, so SA-B1 has no task set for that record. Fix: add a row `analysis` (for example `swe-070` task 1, `swe-134` tasks 1 and 6 (SC), `swe-192` task 1 (SC) where the analysis sets a hazard-control value), or state which existing row applies | Open | Pending | |
| <a id="finding-3"></a>finding-3 | reviewer | Minor | CK-REQ-G1 | Readiness R4 (line 130) with R1 (line 127) | R4 accepts a paired file review that is "filed or in progress"; 07 section 10.2 (Record row) dispatches the paired assurance record "after the file review is filed", and R1 of this template needs the paired record's `product_files` to compare. Fix: R4 reads "filed" | Open | Pending | |

## Readiness criteria

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | Product validates | Yes | A filled copy as `requirements-sw-keyer-software-assurance.md` (product `docs/requirements/sw/sw-keyer/requirements.json`, placeholders replaced by valid values only) passes `tools/validate_docs.py --root <export of ac9b7a5>`, including the rule that a `sw-keyer` product needs an assurance reviewer distinct as a string from author and reviewer |
| R2 | Traceability clean | N/A | No requirement or test case is touched |
| R3 | Author self-check | Yes | Author summary; CR-012 sections 1.1 and 9 |
| R4 | No TBD | Yes | `grep -n TBD` on the blob: none |
| R5 | CR impact assessment | Yes | CR-012 section 4 (INSP-031, section "CR-012") |

## G. Plans, process documents and decision records (SWE-087 b)

| Id | Answer | Evidence |
|---|---|---|
| CK-REQ-G1 | No | Agrees with charter sections 1 and 2 (NASA-STD-8739.8 not in the corpus; SA by independent reviewer agents), 07 sections 2.1, 2.1.1, 10.2, 14 and 15, 03 sections 4 and 5, and `rmm.json` (SWE-022 and SWE-023 T; SWE-192 FC as SA-D5 states). Disagreements: the section B task rule narrows 07 section 15 (finding-1); R4 against 07 section 10.2 (finding-3) |
| CK-REQ-G2 | No | Every item names its evidence file and field (`hazards.json` `causes` and `firmware_role`, 07 section 14.2 "Items applied" column, R3 command with the absolute `--output`, which also moves `traceability.json` beside it, verified in `tools/traceability.py` line 2762). Gap: no `product_type` for an analysis routed by the validator (finding-2) |
| CK-REQ-G3 | Yes | Three distinct invocations (author, file reviewer, assurance reviewer), SA-A2; the file review record copies the assurance verdict and each reviewer edits only its own record (Record section, equal to 07 section 10.2); residual safety risk accepted only by the owner as SMA TA (completion criteria) |
| CK-REQ-G4 | Yes | Reliefs are cited from `rmm.json` rows SWE-022 and SWE-023 (both T, verified) and from 07 sections 15, 16.3 and 16.5 (verified to exist); "Relief and limits" states that the standard's own minimum task set cannot be enumerated |
| CK-REQ-G5 | N/A | The template plans the cybersecurity tasks (`swe-154`, `swe-156`, `swe-159` for the plan's section 16) but has no cybersecurity section of its own |
| CK-REQ-G6 | Yes | SA-F2: MSR-20 and MSR-21 inputs of 07 section 10.3; front matter counts, `swe134_items_checked`, `assurance_tasks_applied` |
| CK-REQ-G7 | Yes | Tools named: `tools/validate_docs.py` (the record rule for the paired form and the string-distinct `assurance_reviewer_agent` reproduced by the reviewer's filled copy) and `tools/traceability.py --report-only --output` (the flag exists, line 2778) |
| CK-REQ-G8 | Yes | See the task verification below; SWE numbering pinned in `npr-7150-2d/03-chapter3.md` (3.6.1 SWE-022, 3.7.1 SWE-205, 3.7.2 SWE-023, 3.7.3 SWE-134, 3.7.4 SWE-219, 3.7.5 SWE-220, 3.12.1 SWE-052) and `05-chapter5.md` (5.3.2 to 5.3.4, SWE-087 to 089); SWEHB `swe-205` section 7.7.2 exists ("Considerations when identifying software subsystem hazard causes") |
| CK-REQ-A8 | Yes | Terms match 07 (software assurance reviewer, paired assurance record, software lead); no em dashes |

## Every case named (rule C7)

**07 section 2.1.1 rows marked Yes, against the `product_type` values.** Software requirement files: `requirements`. Software plans: `plans` (07, the V&V plan software section, 03, 05, TS-002 each with its sub-list). Trade studies and ADRs constraining a 14.1 component: `trade-study-or-adr`. Design: `design`. Code: `code` (including `unsafe` files of "neither" components). Test cases, test code, emulation scenarios, dev-board checks: `test`. NCR touching firmware: `ncr`. MC/DC tables and the unsafe audit list: `mcdc-or-unsafe-audit`. The row "Other process documents" is No in every column and correctly has no type. All eight Yes rows are covered.

**SWE-134 items a to l.** SA-C-a to SA-C-l are the twelve items of NPR 7150.2D 3.7.3 in order, each paraphrased without quotation marks, which the citation rule allows; none is missing.

**Task numbers and SC marks.** Every `swe-NNN 7.1 task n` the template cites was checked against the section 7.1 list of its SWEHB page (a Python extraction of the numbered tasks of each page): all 61 SWE pages cited exist and every cited task number exists (for example `swe-039` has tasks 1 to 8, `swe-135` 1 to 7, `swe-191` and `swe-202` and `swe-204` 1 to 4, `swe-065` parts a, b, c with 2, 2 and 3 tasks). Every SC mark in the template matches SWEHB topic 8.10 section 6 (033 task 2; 013 tasks 1 and 2; 024 tasks 1 to 3; 039 task 8; 121 and 125 tasks 1 and 2; 139 task 1; 020 and 176 task 1; 205 tasks 1 to 5; 023 task 1; 134 tasks 1 to 6; 219 task 1; 220 tasks 1 and 2; 052 task 2; 051 and 184 task 1; 058 task 4; 135 tasks 2, 5 and 6; 062 task 1; 065a and 065b task 2; 066 tasks 2 and 3; 071, 191, 192 task 1; 080 task 1; 081 task 2; 087 task 4). No task is marked SC that 8.10 does not list. The SC tasks of 8.10 section 6 absent from section B are finding-1.

**Plan output.** "NASA-STD-8739.8 style SA items as far as the corpus allows": sections C to F with the SWEHB quotations of the standard; "07 §2.1.1": section A and the `product_type` rule. Present, subject to finding-1.

## Verdict format

```
VERDICT: NEEDS CHANGES
FINDINGS:
- [Major] CK-REQ-G1 section B omits SC tasks of SWEHB 8.10 section 6 (swe-134 task 3, swe-036 tasks 1 and 2, swe-068 task 3; swe-134 task 5 and swe-022 task 1 not shown as met or relieved) and narrows 07 section 15.
- [Minor] CK-REQ-G2 no product_type for an analysis that validate_docs routes to the assurance reviewer.
- [Minor] CK-REQ-G1 R4 "filed or in progress" against 07 section 10.2 "after the file review is filed".
ITEMS N/A: CK-REQ-G5
SA PAIR: required (07 section 2.1.1 plans row; swe-087 7.1 task 3), not yet assigned
MEASUREMENTS: size=1 template; items=9; items_no=2; tasks_checked=61 pages; turns=16; minutes=30; major=1; minor=2
```

## Iteration 2: delta verification of the Major fix (2026-09-27, branch head `7784672`)

**Scope (rule C1).** Iteration 2 is a delta that verifies the Major fix only. Product: `docs/templates/peer-review-checklist-software-assurance.md` blob `5b13528504868b2add0f0b1e329c63aa2b54cdf4` at `7784672` (`git ls-tree 7784672` checked for all five `product_files` blobs; the CR-012 blob `91c8c626` checked with `git ls-tree 4552943`). `git diff --stat ac9b7a5 7784672`: 2 files, 25 insertions, 14 deletions, only the software assurance and tool validation templates; the analysis template (`0386cc6e`) and 08 (`56c54011`) are unchanged, so the INSP-031 answers on them stand. The fix commit carries the trailer `CR: CR-012` (CR-012 section 5 step 6) and its message lists no hunk outside the two templates. CR-012 at `91c8c626` records the new blobs in its header table and in sections 8, 9 and 11.

**Independence (rule C4).** This invocation authored no part of WP-PDR-03, CR-012 or the fix commit, and edited no product file. It is the file review only; the software assurance lens is not applied here (SA pair needed, unchanged from iteration 1).

**Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: WP-PDR-03 checklist templates review record path; iteration 2 delta verification record practice; SWEHB topic 8.10 section 6 safety-critical SASS tasks). `grep -n` and a Python extraction were used afterwards only to pin lines and task numbers.

### Verification of finding-1 (Major)

| Part of finding-1 | Fix at blob `5b135285` | Check | Result |
|---|---|---|---|
| (a) `swe-134` 7.1 task 3 (SC) in no row | `code` row line 152 and `test` row line 153 carry `swe-134 task 3 (SC)`, tied to the configuration guard's persisted record (07 section 14.1 line 596 of 07 on `main`) and the loaded items of 07 section 9.7 (line 414, SWE-193) | SWEHB `swe-134` section 7.1 task 3 reads "Confirm that the values of the safety-critical loaded data, uplinked data, rules, and scripts that affect hazardous system behavior have been tested" | Verified |
| (b) `swe-036` tasks 1 and 2 (SC) missing from `plans` | `plans` row line 149: "for 07: swe-036 tasks 1 and 2 (SC ...)", task 2 checked against the "Owner action on receipt" column of 07 section 1.3 | `rmm.json` SWE-036 disposition FC; 07 section 1.3 heading "(SWE-036; NPR 7150.2D §6.1)" and its column "Owner action on receipt" (07 line 35); SWEHB `swe-036` task 2 is the government action on receipt of deliverables | Verified |
| (c) `swe-134` task 5 and `swe-022` task 1 (SC) shown nowhere | New row "Every product type" line 147: task 5 met by the review itself; task 1 performed against 07 section 15 with the NASA-STD-8739.8 part relieved by `rmm.json` SWE-022 T | `rmm.json` SWE-022 disposition T; 07 section 2.1.1 basis line (07 line 126) cites `swe-134` task 5 as the task says | Verified |
| (d) `swe-068` task 3 (SC) in no row | `test` row line 153: "swe-068 task 3 (SC; `rmm.json` SWE-068 FC ...)" | `rmm.json` SWE-068 disposition FC; SWEHB `swe-068` task 3 reads "Confirm that test results are sufficient verification artifacts for the hazard reports" | Verified |
| (e) absence of the `swe-015`, `swe-151`, `swe-016`, `swe-174` SC tasks not stated | Note line 157 "SC tasks that are not in the table, by decision" | `rmm.json`: SWE-015 T, SWE-151 T, SWE-016 T, SWE-174 NA, as the note says; 8.10 section 6 designates 015 task 1, 151 task 1, 174 task 2 and 016 task 2, as the note says; the note cites "When it is used" (line 97), which exists | Verified |
| Task-table rule narrowed 07 section 15 | Section B lead paragraph line 143, task-table heading line 117, SA-B1 line 161, the `assurance_tasks_applied` comment line 76 and the completion criteria line 214 all take "every other SWE the product implements (07 section 15)" | The added wording repeats 07 section 15 ("of the SWEHB page for each SWE the product implements"); the five places agree with each other | Verified |

**Every case named (rule C7): SWEHB topic 8.10 section 6 against section B at `5b135285`.** The reviewer extracted every SWE row and SC task number of 8.10 section 6 (36 rows) and located each in section B: 033 task 2 (trade, TS-002); 013 tasks 1, 2; 024 tasks 1 to 3; 036 tasks 1, 2 (new); 039 task 8; 139 task 1; 121 tasks 1, 2; 125 tasks 1, 2 (all `plans`); 015 task 1, 151 task 1, 174 task 2, 016 task 2 (the note, by decision); 020 task 1, 176 task 1 (`plans`, 03); 022 task 1 (new "Every product type" row); 205 tasks 1 to 5 (`plans` 03; 4 in `requirements`; 3 in trade and `design`); 023 task 1 (`requirements`); 134 tasks 1 to 6 (1 `requirements` and `design`; 2 `code` and `mcdc-or-unsafe-audit`; 3 `code` and `test`, new; 4 trade and `design`; 5 "Every product type", new; 6 `requirements`, trade and `design`); 219 task 1 and 220 tasks 1, 2 (`code`); 052 task 2, 051 task 1, 184 task 1 (`requirements`); 058 task 4 (`design`); 135 tasks 2, 5, 6 (`code`); 062 task 1 (`code`, `test`); 065a task 2 (`plans`, V&V); 065b task 2 (`test`); 066 tasks 2, 3 (`test`); 068 task 3 (`test`, new); 071, 191, 192 task 1 (`test` and `plans`); 080 task 1 (`plans` 05, `ncr`); 081 task 2 (`plans` 05); 087 task 4 (`code`). No SC task of 8.10 section 6 is missing, and the four the note names are the only ones outside the rows. The four new task citations exist in their SWEHB section 7.1 lists (`swe-036` 1 and 2, `swe-134` 3 and 5, `swe-068` 3, `swe-022` 1).

**Readiness at iteration 2.** R1 Yes: a filled copy of the template at `5b135285`, `requirements-sw-keyer-software-assurance.md` (product `docs/requirements/sw/sw-keyer/requirements.json`, placeholders replaced by valid values only), passes `tools/validate_docs.py --root <git export of 7784672>`. R2 N/A. R3 Yes (author summary; CR-012 sections 8 and 9 at `91c8c626`). R4 Yes (`grep -n TBD` on the blob: none; no em dash). R5 Yes (CR-012 section 4). `readiness_met: true`.

**Scan of the delta for new defects.** None found. The new row "Every product type" is not a `product_type` value, and the table says it applies "in addition to the product's own row", so SA-B1 stays decidable.

### Findings (iteration 2; current state of every finding of this record)

| Finding | Severity | State | Disposition |
|---|---|---|---|
| finding-1 | Major | Verified | Closed at iteration 2 on blob `5b135285` (table above) |
| finding-2 | Minor | Lien: fix before CDR | Not addressed at `7784672` (author election, rule C1). Owner: Claude as checklist owner; due the CDR readiness declaration; listed in PDR package section 15 |
| finding-3 | Minor | Lien: fix before CDR | R4 still reads "filed or in progress" (line 130). Owner and due event as finding-2 |

### Record verdict

The file reviewer's verdict is APPROVED, with liens finding-2 and finding-3. The record `verdict` stays NEEDS CHANGES for two reasons. (a) The software assurance second review is required and has not been filed (07 section 10.2; the front matter `assurance_required: true`). (b) The reviewed blobs are on the CR branch, not in `main` HEAD, so an APPROVED record would fail the record drift rule of `tools/validate_docs.py` (the same hold as INSP-031). The software lead sets `verdict: APPROVED` when the paired assurance record is APPROVED and CR-012 has merged with these blobs unchanged.

```
VERDICT (iteration 2, 2026-09-27): reviewer APPROVED (with liens finding-2, finding-3); record verdict NEEDS CHANGES (held: SA pair not filed; branch-only blobs)
PRODUCT: cr/CR-012-pdr-checklist-templates at 7784672; peer-review-checklist-software-assurance.md 5b135285
FINDINGS: finding-1 Major Verified; finding-2, finding-3 Minor liens due CDR; no Major open
SA PAIR: required (07 section 2.1.1 plans row; swe-087 7.1 task 3), not yet assigned
MEASUREMENTS: blobs re-checked 5; SC rows of 8.10 section 6 checked 36; new findings 0; iteration 2 16 turns, 25 minutes; cumulative 32 turns, 55 minutes
```

## Iteration 3: delta on the combined 08 blob, re-pin of the CR file and the filed SA pair (2026-09-29, `main` `1864ab2`, branch heads `7784672` and `7efd900`)

**Why.** CR-012 pre-merge check 2 (CR-012 section 9, commit `1864ab2`) found that this record pins 08 at `56c54011`, which CR-015 replaces with `374fd777`, and the CR-012 file at `91c8c626`, which later steps have changed (now `5aa567d2`), so its verdict could not be set at the merges. It also found that `assurance_reviewer_agent` and `assurance_verdict` still said the SA pair was not filed, although INSP-046 is filed. The configuration manager asked this record's reviewer role for a delta (record delta 2).

**Scope (rule C1).** A delta. The software assurance template blob `5b135285` is unchanged (`git rev-parse 7efd900:docs/templates/peer-review-checklist-software-assurance.md`), and so are the other two templates. Only the 08 blob, the CR file pin and the pair fields change. The software assurance lens is not applied here (rule C4; 07 section 2.1).

**Independence (rule C4) and search first.** A new invocation of this record's reviewer role (`reviewer:WP-PDR-03-templates`). It authored no part of CR-012, CR-015, their branches, INSP-046 or the earlier record deltas, and edited no product file. It does not perform or change the software assurance review; it copies the filed INSP-046 verdict into this record, as 01 section 13 asks of the file review record. `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any `grep`.

**08 hunks.** The six CR-015 hunks of `git diff 7784672 7efd900 -- docs/process/08-agent-briefing.md` are read in INSP-031 iteration 3 (the record that carries the checks shared by the three WP-PDR-03 records). None of them changes CR-012 text: the 11 lines CR-012 adds are present unchanged in `374fd777`, including the section 3.5 row `peer-review-checklist-software-assurance.md` (line 155), and none of the 9 lines CR-012 removes comes back. For this template in particular: hunk 3 (section 3.1, line 83) gives trade studies "the SA pair where 07 section 2.1.1 says Yes", which agrees with the template's `trade-study-or-adr` row (line 150, "whose decision constrains a 07 section 14.1 component"); hunk 4 (section 3.2, lines 112 and 113) brings the held-verdict rule for branch-only blobs, which the template does not contradict, and the Minor-lien rule of 01 section 12.3 item 2, which this template's completion criterion (line 214) does not match; that is INSP-031 finding-3 (Minor, a lien due the CDR readiness declaration), not raised again here.

**CR file (dropped from `product_files`).** This record reviewed the CR file at `91c8c626`. INSP-031 iteration 2 read `91c8c626` to `f689b05c` and INSP-031 iteration 3 read `f689b05c` to `5aa567d2`: sections 1, 2, 3 and 5 of CR-012 are unchanged since `f689b05c`, and the later changes are front matter state, a section 4.1 listing paragraph and sections 6.2 to 11. The CR file is dropped from `product_files` and identified here as reviewed at `91c8c626`, with the later hunks read in INSP-031.

**Pair fields.** INSP-046 (`docs/reviews/PDR/checklists/template-peer-review-checklist-software-assurance-software-assurance.md`, commit `d566e01`) is filed at iteration 1 with `assurance_verdict: APPROVED`, `paired_record: INSP-032` and `assurance_reviewer_agent` `sa-reviewer:WP-PDR-03-templates`. This record now carries `paired_record: INSP-046`, that assurance reviewer, and `assurance_verdict: APPROVED`. INSP-046 still names 08 `56c54011` and the CR file at `91c8c626`, so the two records no longer name the same blobs until INSP-046's own re-pin delta (a software assurance invocation) names 08 `374fd777` and drops the CR file. That delta is outside this record and this invocation.

### Findings (iteration 3; current state of every finding of this record)

| Finding | Severity | State | Disposition |
|---|---|---|---|
| finding-1 | Major | Verified | Closed at iteration 2 on blob `5b135285`; the blob is unchanged |
| finding-2 | Minor | Lien: fix before CDR | Unchanged at `5b135285`. Owner: Claude as checklist owner; due the CDR readiness declaration |
| finding-3 | Minor | Lien: fix before CDR | Unchanged at `5b135285` (R4 still reads "filed or in progress"). Owner and due event as finding-2 |

Open Major: 0. New findings in this record: 0 (INSP-031 finding-3 covers the completion criterion of this template).

`tools/validate_docs.py` on `main` at `1864ab2` with this delta in the working tree: PASS on this record (drift of the branch-only blobs printed as notes). Verdict trial on a scratch trial merge of CR-012 then CR-015 into `main` at `39257a8`, with the iteration 3 deltas of INSP-031 to INSP-033 committed and `verdict: APPROVED` set: this record PASS with no drift note; 117 passed, 0 failed (details in INSP-031 iteration 3, "Checks run").

### Record verdict (iteration 3)

Reviewer verdict: APPROVED, with liens finding-2 and finding-3; assurance verdict APPROVED (INSP-046). Record `verdict` held at NEEDS CHANGES until (a) INSP-046's re-pin delta names the same four blobs and (b) CR-012 and CR-015 have both merged. The software lead then sets `verdict: APPROVED` on both records in the CR-015 merge commit or the commit right after it. A later merge that re-blobs 08 (CR-017, batch 2) needs a further delta of both records first.

```
DELTA ITERATION 3 (2026-09-29): VERDICT: reviewer APPROVED; assurance APPROVED (INSP-046); record verdict held until the INSP-046 re-pin delta and the CR-015 merge
PRODUCTS: templates 5b135285, 7be809d4, 0386cc6e (unchanged); 08 56c54011 -> 374fd777 (CR-015 head 7efd900); CR-012 file dropped (reviewed at 91c8c626)
FINDINGS: finding-1 Major Verified; finding-2, finding-3 Minor liens due CDR; new findings 0; open Major 0
SA PAIR: INSP-046 filed (paired_record set); its re-pin delta pending (software assurance invocation)
MEASUREMENTS: hunks=6 (read in INSP-031 iteration 3); turns=8; minutes=15; cumulative turns=40, minutes=70
```
