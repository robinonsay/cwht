---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md section 13
# is the single field list; docs/process/08-agent-briefing.md section 3.2). Checklist:
# docs/templates/peer-review-checklist-requirements.md revision C, section G and CK-REQ-A8, as PDR work plan
# WP-PDR-03 names. Product: the new software assurance checklist template of CR-012 (Submitted, Class II),
# frozen on branch cr/CR-012-pdr-checklist-templates at ac9b7a5 (rule C2). The 08 delta and the CR-012
# checks shared by the three WP-PDR-03 records are in INSP-031
# (docs/reviews/PDR/checklists/template-peer-review-checklist-analysis.md).
id: INSP-032
checklist: peer-review-checklist-requirements
checklist_revision: C
checklist_file: docs/reviews/PDR/checklists/template-peer-review-checklist-software-assurance.md
product: docs/templates/peer-review-checklist-software-assurance.md
product_commit: "ac9b7a5cfc61aa03e5520c13be505a68f206f6fe"
product_files: ["docs/templates/peer-review-checklist-software-assurance.md@22b7b6afd241d7bd2deddfe45d9318cab5f0243b", "docs/templates/peer-review-checklist-analysis.md@0386cc6e78da65578b1cce8b2f793cd3db224921", "docs/templates/peer-review-checklist-tool-validation.md@c94fa383a952cde434da7f63eb00ae5d699996d6", "docs/process/08-agent-briefing.md@56c540113110b0d8916219d3cb531d6a76587713", "docs/cm/cr/CR-012-pdr-checklist-templates.md@02f2796402b0c6643686ffbe3cf4318cf4698155"]
product_size: 1 template (226 lines, sections R, A to F, SWE-to-task table of 8 product types)
sprint: PDR-prep
author_agent: "author:WP-PDR-03 (Claude as checklist owner)"
reviewer_agent: "reviewer:WP-PDR-03-templates"
criticality: neither
# assurance_required: true. This template is the closure of 07 section 15 row "5.17 item 13: SA
# requirements mapping and tasking", so it is part of the software assurance plan (NPR 7150.2D 6.1 item k,
# 07 section 15); 07 section 2.1.1 row "Software plans" is Yes in every column, and SWEHB swe-087 section
# 7.1 task 3 is "Perform peer reviews on software assurance and software safety plans". The assurance
# reviewer is a separate invocation (rule C4); it is not yet assigned (fix request "SA pair needed").
assurance_required: true
assurance_reviewer_agent: "not yet assigned (SA pair needed; paired record to be filed as template-peer-review-checklist-software-assurance-software-assurance.md)"
iteration: 1
readiness_met: true
reviewer_verdict: NEEDS CHANGES
assurance_verdict: NEEDS CHANGES
verdict: NEEDS CHANGES
findings_major: 1
findings_minor: 2
findings_open: 3
findings_fixed: 0
findings_verified: 0
findings_deferred: 0
assurance_findings_major: 0
assurance_findings_minor: 0
assurance_tasks_applied: []
deferred_rids: []
items_no: [CK-REQ-G1, CK-REQ-G2]
effort_turns: 16
effort_minutes: 30
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
