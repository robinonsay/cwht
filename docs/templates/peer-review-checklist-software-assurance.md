---
# Peer-review record front matter (charter sections 2 and 5; docs/process/01-lifecycle-and-reviews.md
# section 13; docs/process/07-software-engineering-plan.md sections 2.1.1, 10.2 and 15). This is the
# software assurance second review. Its default form is the paired assurance record of 07 section
# 10.2: copy this whole file to docs/reviews/<REVIEW>/checklists/<product-slug>-software-assurance.md,
# where <product-slug> is the slug of the file review record of the same product. That copy is the
# single assurance record for the product (there is no peer-reviews/ folder). When the assurance
# review is written into the file review record instead (the other form 07 section 10.2 allows),
# copy sections A to H of this file into that record and fill its assurance fields; the front matter
# below is then not used. Both front-matter parsers (PyYAML and the subset parser of
# tools/validate_docs.py) strip a comment on its own line and a comment written after a value
# (" # ..."); this template keeps each comment on its own line for readability, and comment lines may
# stay or be deleted when filing. tools/validate_docs.py checks the record against the field list of
# 01 section 13 (its PEER_REVIEW_RECORD_SCHEMA) and fails while the id, checklist_file,
# product_commit or date placeholder is left in place.
# Search first: 'grep' in an evidence column means: run mcp__claude-context__search_code on
# /Users/robinonsay/rust/cwht first (charter section 11 rule 1), then grep -n only to pin the hit.
#
# id: next free INSP-NNN (never reused, charter section 6); Claude assigns it in the assignment block
id: INSP-NNN
checklist: peer-review-checklist-software-assurance
checklist_revision: A
# checklist_file: this record's own path
checklist_file: docs/reviews/<REVIEW>/checklists/<product-slug>-software-assurance.md
# product: the same product path as the paired file review record (01 section 13, paired_record)
product: <product path>
# product_commit: the freeze commit, the same as the paired record's; quoted so that an all-digit
# hash stays a string
product_commit: "<commit>"
# product_files: path@git blob of every reviewed file, equal to the paired record's list
product_files: ["<path>@<blob>"]
# paired_record: the INSP-NNN of the file review record of the same product
paired_record: INSP-NNN
# product_type: the 07 section 2.1.1 row that routes the product here: requirements, plans,
# trade-study-or-adr, design, code, test, ncr, mcdc-or-unsafe-audit (section B of this checklist)
product_type: <row>
# criticality: safety-critical | mission-critical | neither, from the 07 section 14.1 component the
# product belongs to (a Proposed row of 14.1 counts as its proposed criticality); the plans row of
# 07 section 2.1.1 is Yes in every column, so a plan may be neither and still be reviewed here
criticality: safety-critical
# product_size: N requirements, N lines, N cases, N sections
product_size: <size>
# sprint: the gate preparation or the software sprint, for example PDR-prep or SW-NN-<module>
sprint: PDR-prep
# author_agent: the product's author invocation
author_agent: <invocation id>
# reviewer_agent: this assurance invocation; never the author and never the file reviewer of the
# paired record (07 section 2.1)
reviewer_agent: <invocation id>
assurance_required: true
# assurance_reviewer_agent: the same invocation, written in the SRR paired-record form
# "<invocation id> (software assurance function; paired file review INSP-NNN by <file reviewer id>)"
# (INSP-017, INSP-018, INSP-026, INSP-027, INSP-030). tools/validate_docs.py requires this field to
# differ, as a string, from author_agent and reviewer_agent, and the form also records the pairing
assurance_reviewer_agent: "<invocation id> (software assurance function; paired file review INSP-NNN by <file reviewer id>)"
# iteration: 1 to 3 (07 section 10.2)
iteration: 1
readiness_met: true
# reviewer_verdict and assurance_verdict: this invocation's verdict, APPROVED | NEEDS CHANGES; in a
# paired assurance record the two are equal
reviewer_verdict: NEEDS CHANGES
assurance_verdict: NEEDS CHANGES
# verdict: set by Claude as software lead; APPROVED only when this assurance review and the paired
# file review are both APPROVED (07 section 10.2 completion criteria)
verdict: NEEDS CHANGES
# findings_* and assurance_findings_* count the same findings in a paired assurance record, so the
# 07 section 11.3 trends count them once (07 section 10.2 Record row)
findings_major: 0
findings_minor: 0
findings_open: 0
findings_fixed: 0
findings_verified: 0
findings_deferred: 0
assurance_findings_major: 0
assurance_findings_minor: 0
# assurance_tasks_applied: every SWEHB section 7.1 task applied, as "swe-NNN 7.1 task n", taken from
# the task rows SA-B1 requires (section B); tasks answered N/A are listed in the task table with their relief
assurance_tasks_applied: []
# swe134_items_checked: the SWE-134 items a to l answered in section C (empty for criticality neither)
swe134_items_checked: []
# deferred_rids: RID-<REVIEW>-NNN entered for each Deferred finding at record closure
deferred_rids: []
# items_no: checklist ids answered No
items_no: []
effort_turns: 0
effort_minutes: 0
# record_status: Open | Closed (set by Claude as software lead)
record_status: Open
date: 2026-MM-DD
date_closed: null
---

# Peer review checklist: software assurance second review

**Purpose.** This checklist consolidates the software assurance tasking that `docs/process/07-software-engineering-plan.md` section 15 assigns to the software assurance reviewer, and it is the closure of the 07 section 15 row "5.17 item 13: SA requirements mapping and tasking": section B is the SWE-to-task table that plans, per product type, which SWEHB section 7.1 tasks the assurance reviewer applies. It does not replace the file review: the file reviewer applies the product-type checklist (`peer-review-checklist-requirements.md`, `-design.md`, `-code.md`, `-test.md`, `-risk.md` section B, `-analysis.md`), and this review adds the assurance lens.

**When it is used.** Only on the products that 07 section 2.1.1 (the single dispatch rule) marks Yes for the component's criticality (07 section 14.1). This checklist does not widen or narrow that table; a product that should be routed here and is not is reported as a cross item to the software lead, not reviewed on the reviewer's own initiative.

**Governing:** NPR 7150.2D SWE-022 (3.6.1) and SWE-023 (3.7.2), both dispositioned T in `docs/process/rmm.json` because NASA-STD-8739.8 is not in the corpus (charter section 1; 07 section 15); SWE-205 (3.7.1), SWE-134 (3.7.3) items a to l, SWE-219 (3.7.4), SWE-220 (3.7.5), SWE-052 (3.12.1), SWE-087, SWE-088, SWE-089 (5.3.2 to 5.3.4); the `# 7. Software Assurance` section (7.1 tasking, 7.2 products) of each SWEHB page `docs/references/md/swehb/swe-NNN-*.md`, whose tasks are quoted "From NASA-STD-8739.8B"; SWEHB topic `8-10-facility-software-with-safety-considerations.md` section 6 (the SWEs whose assurance tasks carry the safety-critical designation, stated there to be the same as in topic 8.15, the SA Tasking Checklist Tool); SWEHB `swe-205-*.md` section 7.7.2 (considerations when identifying software hazard causes); 07 sections 2.1, 2.1.1, 10.2, 14 and 15; `docs/process/03-software-classification-and-rmm.md` sections 4 and 5; charter sections 2 and 10. **Used by:** the software assurance reviewer, an independent invocation that is neither the product's author nor the file reviewer of the paired record (07 section 2.1; charter section 11 rule 4).

**Relief and limits.** NASA-STD-8739.8 itself is not in the corpus, so the task text used here is the SWEHB quotation of it, and the standard's own minimum task set cannot be enumerated beyond those quotations (07 section 15 rows "5.17 item 13" and "5.17 item 14"; `rmm.json` rows SWE-022 and SWE-023, T). A task that the project cannot apply is answered N/A with the `rmm.json` row or the 07 section that relieves it. A task with no relief on record is applied, or its absence is a finding.

Answer every applicable item and task Yes, No or N/A with evidence (file and line, requirement or hazard id and field, tool output pasted, render path, or the paired record's item and answer). Every No is a finding. **Major**: a software contribution to a hazard is missing from the hazard data; a hazard-tracing software requirement has no Test closing case (SWE-192); a SWE-134 item that 07 section 14.2 allocates to the component has no provision at the product's maturity; a safety-critical component is not listed as such, or its criteria disagree with the union rule of 03 section 4.1; traceability to hazards is one-way; a safety-critical coverage or complexity shortfall has no waiver on record (SWE-219, SWE-220); the paired review was not independent or its record names other blobs; a safety-critical designated task of section B is skipped with no relief on record. **Minor**: a stale citation, an incomplete rationale or a record-keeping gap that changes no safety conclusion.

## Record

This file, copied to `docs/reviews/<REVIEW>/checklists/<product-slug>-software-assurance.md`, is the paired assurance record of 07 section 10.2 (01 section 13, optional field `paired_record`). The file review record of the same product carries `paired_record` naming this record's `INSP-NNN`, names this reviewer in `assurance_reviewer_agent` and copies `assurance_verdict` from this record; each reviewer updates only its own record, and the author edits neither. The front matter above is the first thing in the file, unfenced.

### Findings (filled by the assurance reviewer; the owner ruling column is transcribed by Claude at the review)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | assurance | Major or Minor | SA-xx or `swe-NNN 7.1 task n` | file and line, or id and field | what is wrong and what would fix it | Open, Fixed, Verified or Deferred | Pending, `Adopt as RID RID-<REVIEW>-NNN`, `Adopt as RFA RFA-<REVIEW>-NNN` or `No action` | `RID-<REVIEW>-NNN` and the owner decision reference, for Deferred only |

Finding rules: ids are `finding-<n>`, numbered from 1 in this record, each with the anchor `<a id="finding-<n>"></a>` in its first cell so that `checklists/<product-slug>-software-assurance.md#finding-<n>` resolves (01 section 13). A defect already raised by the paired file review is cited by that record's finding id and not raised again; the assurance reviewer raises it here only when the assurance lens changes its severity, and says so. The reviewer writes `Pending` in the owner ruling column; Claude transcribes the owner's ruling (01 section 10.1). `tools/validate_docs.py` rejects `verdict: APPROVED` while any line holding a `finding-<n>` id also holds the words `Major` and `Open`, so write the state only in the State column and keep severity and state words out of the task table. Replace the placeholder row above; do not leave it in a filed record.

### Task table (one row per task of the section B row for `product_type`, of the section B "Every product type" row, and of every other SWE the product implements)

| Task | Safety-critical designation (SWEHB 8.10 section 6) | Applied | Result and evidence | Relief (N/A only) | Finding ids |
|---|---|---|---|---|---|
| swe-NNN 7.1 task n | SC or blank | Yes, No or N/A | what was checked and what was found, with evidence | `rmm.json` row or 07 section | `finding-<n>` or none |

## Readiness criteria (all true before the review starts)

| # | Criterion | Evidence |
|---|---|---|
| R1 | The product is committed and frozen, and `product_files` equals the paired record's list (the same blobs; PDR work plan rule C2) | `git rev-parse` output; paired record front matter |
| R2 | The 07 section 2.1.1 row and the component criticality are identified (`product_type`, `criticality`) from the 07 section 14.1 list at the product's commit | 07 sections 2.1.1 and 14.1 |
| R3 | `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/validate_docs.py` exits 0 on the product's files, and `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/traceability.py --report-only --output <reviewer scratch directory>/traceability-report.md` reports no violation for the ids the product touches (the absolute `--output` keeps the run from rewriting `docs/vv/traceability-report.md`) | tool output |
| R4 | The paired file review is filed or in progress under its own invocation, and the assurance reviewer authored no part of the product and is not that file reviewer | paired record `author_agent`, `reviewer_agent` |

## A. Dispatch, independence and record integrity (07 sections 2.1, 2.1.1, 10.2)

| Id | Check | Evidence to inspect |
|---|---|---|
| SA-A1 | The product belongs to a 07 section 2.1.1 row marked Yes for its component's criticality; the row and criticality are stated with the 14.1 line they come from | 07 sections 2.1.1 and 14.1 |
| SA-A2 | Independence holds: author, file reviewer and assurance reviewer are three different invocations, recorded in both records (charter section 2; 07 section 2.1) | both records' front matter |
| SA-A3 | Both records name the same product and the same blobs; a product change after either review is covered by a delta iteration of both records (rule C2) | both records |
| SA-A4 | The paired file review used the checklist 07 section 10.1 and 08 section 3.5 assign to the product type and answered every applicable item with evidence (SWEHB `swe-088` section 7.1 task 1: the NPR 7150.2D 5.3.3 criteria a to d met) | paired record |

## B. SWE-to-task table by product type (07 section 15 row "5.17 item 13" closure; SWEHB section 7.1 of each page)

The assurance reviewer applies every task in the row of its `product_type` and in the row "Every product type". The rows are the planned minimum, not the limit. 07 section 15 directs the assurance reviewer to the `# 7. Software Assurance` section "of the SWEHB page for each SWE the product implements". So the reviewer also applies the section 7.1 tasks of any other SWE that the product implements: a SWE the product cites as satisfied, or whose `rmm.json` row names the product. The reviewer adds one task-table row per such task. **SC** marks a task that SWEHB topic 8.10 section 6 lists as a safety-related assurance and safety task (the designation it states is the same as in topic 8.15); for a product of a safety-critical component an SC task is never answered N/A without relief on record. Tasks are cited as `swe-NNN 7.1 task n` in the page's numbering; SWE-065 tasks carry the part letter (a to d) of the page.

| `product_type` (07 section 2.1.1 row) | SWEHB section 7.1 tasks to apply |
|---|---|
| Every product type (applied in addition to the product's own row) | swe-134 task 5 (SC): met by this review, which is the assurance participation in a review of a product 07 section 2.1.1 routes (the basis line of 07 section 2.1.1 cites this task), answered Yes with this record as evidence; swe-022 task 1 (SC): performed against the project's software assurance plan (07 section 15) by this review, and the NASA-STD-8739.8 part is relieved by `rmm.json` SWE-022 T (the standard is not in the corpus), both stated in the task row |
| `requirements`: software requirement files `docs/requirements/sw/**/requirements.json` and CRs touching them | swe-050 task 1; swe-051 task 1 (SC); swe-052 tasks 1 and 2 (2 SC); swe-184 task 1 (SC); swe-134 tasks 1 and 6 (SC); swe-205 task 4 (SC); swe-023 task 1 (SC; relief `rmm.json` SWE-023 T for the standard's own list, applied against 07 section 14); swe-157 task 1 as tailored in 07 section 16.3; swe-210 task 1 as tailored in 07 section 16.5; swe-139 task 1 (SC) |
| `plans`: 07, the software section of `docs/vv/plan.md`, 03, 05 and TS-002 | swe-013 tasks 1 and 2 (SC; task 2 is met by 07 section 15 as the software assurance plan); swe-024 tasks 1 to 3 (SC); swe-039 tasks 7 and 8 (8 SC); swe-121 tasks 1 and 2 (SC); swe-125 tasks 1 and 2 (SC; task 2 relief `rmm.json` SWE-022 T); swe-139 task 1 (SC); swe-087 task 3; swe-090 task 1; swe-154 task 1, swe-156 task 1 and swe-159 tasks 1 and 2 for the cybersecurity section (07 section 16); for 07: swe-036 tasks 1 and 2 (SC; 07 section 1.3 implements SWE-036, `rmm.json` SWE-036 FC; task 2 is checked against the "Owner action on receipt" column of 07 section 1.3); for 03: swe-020 task 1 (SC), swe-176 task 1 (SC), swe-205 tasks 1 to 5 (SC); for 05: swe-079 task 1, swe-080 tasks 1 to 3 (1 SC), swe-081 tasks 1 and 2 (2 SC), swe-082 tasks 1 and 2, swe-083 task 1, swe-084 task 1, swe-085 tasks 1 and 2, swe-187 tasks 1 and 2; for the V&V plan software section: swe-065 part a tasks 1 and 2 (2 SC), swe-071 task 1 (SC), swe-191 task 1 (SC), swe-192 task 1 (SC); for TS-002: swe-033 tasks 1 to 3 (2 SC), swe-027 task 1 |
| `trade-study-or-adr` whose decision constrains a 07 section 14.1 component | swe-033 tasks 1 to 3 (2 SC); swe-039 task 4; swe-057 task 2; swe-134 tasks 4 and 6 (SC); swe-027 task 1 (reused or OSS component chosen); swe-136 task 1 and swe-070 task 1 when the decision selects a tool, emulator or model; swe-205 task 3 (SC) when the decision adds or moves a component |
| `design`: software section of `docs/design/architecture.md`; module design `docs/design/software-design.md` sections or `docs/design/sw/<module>.md` | swe-057 tasks 1 and 2; swe-058 tasks 1 to 5 (4 SC); swe-134 tasks 1, 4 and 6 (SC); swe-143 task 1; swe-205 task 3 (SC); swe-052 task 1 (design components trace to requirements and code) |
| `code`: every file of a safety-critical or mission-critical component, and every file that contains `unsafe` | swe-060 tasks 1 and 2; swe-061 tasks 1 and 2; swe-207 task 1; swe-185 task 1; swe-135 tasks 1 to 7 (2, 5 and 6 SC); swe-134 task 2 (SC); swe-134 task 3 (SC) for code that holds safety-critical loaded data or its defaults and range limits (the configuration guard's persisted record, 07 section 14.1; loaded items of 07 section 9.7): the values are covered by tests; swe-087 task 4 (SC); swe-062 tasks 1 and 2 (1 SC); swe-219 task 1 (SC) and swe-220 tasks 1 and 2 (SC) for safety-critical components |
| `test`: `TC-SW-*` cases, test code, emulation scenarios, dev-board checks | swe-065 part b tasks 1 and 2 (2 SC, items a to e), part c tasks 1 to 3; swe-066 tasks 1 to 3 (2 and 3 SC; task 2 witnessing: the owner witnesses Bench and OnAir runs, 07 section 2.1, and the assurance reviewer confirms the witnessed log); swe-071 task 1 (SC); swe-186 task 1; swe-187 tasks 1 and 2; swe-189 task 1; swe-190 tasks 1 to 3; swe-191 tasks 1 to 4 (1 SC); swe-192 task 1 (SC); swe-193 tasks 1 to 3; swe-134 task 3 (SC; the safety-critical loaded data are the persisted configuration and calibration record of the configuration guard, 07 section 14.1, and the firmware image, 07 section 9.7; their values are confirmed tested by the swe-193 cases); swe-068 task 3 (SC; `rmm.json` SWE-068 FC: the test results are sufficient verification artifacts for the hazard controls of `docs/safety/hazards.json` the cases close); swe-211 task 1; swe-062 task 1 (SC) |
| `ncr`: NCR touching firmware (severity confirmation, 04 section 10.3) | swe-201 tasks 1 and 2; swe-202 tasks 1 to 4; swe-203 tasks 1 and 2; swe-204 tasks 1 to 4 for high-severity NCRs; swe-080 task 1 (SC) |
| `mcdc-or-unsafe-audit`: MC/DC tables of `TC-SW-COV-001-r<N>`, `firmware/unsafe-audit.md` at CDR and SAR | swe-219 task 1 (SC); swe-135 task 5 (SC); swe-134 task 2 (SC); swe-061 task 2 (07 CS-05 to CS-07) |

**SC tasks that are not in the table, by decision.** SWEHB topic 8.10 section 6 also designates swe-015 task 1, swe-151 task 1, swe-016 task 2 and swe-174 task 2. Their products are the cost model `docs/plan/cost-estimate.md` (`rmm.json` SWE-015 and SWE-151, T), the schedule `docs/plan/schedule.md` (SWE-016, T) and Center measurement reporting (SWE-174, NA). 07 section 2.1.1 does not route any of them to the assurance reviewer, and this checklist does not widen that table ("When it is used"). Their absence is therefore the 07 section 2.1.1 decision, not a gap. A change of that routing is a change of 07 by CR. Every other SC task of 8.10 section 6 appears in at least one row above.

| Id | Check | Evidence to inspect |
|---|---|---|
| SA-B1 | Every task of the product type's row, of the row "Every product type" and of every other SWE the product implements (07 section 15) is in the task table with Applied Yes, No or N/A, and `assurance_tasks_applied` lists every Yes and No row | task table; front matter; the product's SWE citations and `rmm.json` rows |
| SA-B2 | Every N/A row cites the `rmm.json` row or the 07 section that relieves it; an SC task of a safety-critical product is never N/A without it | task table; `rmm.json` |
| SA-B3 | Every task answered No is carried by a finding | task table; findings table |

## C. SWE-134 items a to l (applies when `criticality` is safety-critical or mission-critical; 07 section 14.2; 03 section 5)

For each item 07 section 14.2 applies to the product's module or unit (the "Items applied" column of its module table, with the shared provision of the first table and the module-specific provision of the second), check that the provision exists at the product's maturity: a requirement at SRR and PDR (requirements row), a design element at PDR and CDR (design row), code at the code review (code row), and a closing Test case (test row). List the items answered in `swe134_items_checked`.

| Id | SWE-134 item (NPR 7150.2D 3.7.3) | Check at the product's maturity |
|---|---|---|
| SA-C-a | a. Initialized to a known safe state at first start and restarts | The boot and restart path reaches the safe state before any safety-critical output is enabled |
| SA-C-b | b. Safe transitions between all predefined known states | Every state and transition of the component is defined and none bypasses the safe-state manager |
| SA-C-c | c. Termination to a known safe state | Every termination path (fault, power-down, panic handler) ends in the safe state |
| SA-C-d | d. Operator overrides need at least two independent actions | Every override of the component needs the action and a separate confirmation |
| SA-C-e | e. Out-of-sequence commands rejected where they can cause a hazard | Command sequencing is checked for every hazardous command |
| SA-C-f | f. Inadvertent memory modification detected with recovery to a safe state | Integrity checks of safety-critical state and the stored configuration exist, with the recovery path |
| SA-C-g | g. Integrity checks on inputs and outputs | Range and plausibility checks on every safety-relevant input and output of the component |
| SA-C-h | h. Prerequisite checks before safety-critical commands | Each safety-critical command checks its prerequisites (07 section 14.2 row h) |
| SA-C-i | i. No single software event or action initiates an identified hazard | The single-event argument of 07 section 14.2 row i holds for the component |
| SA-C-j | j. Response to an off-nominal condition within the time needed to prevent the hazard | Each response time is bounded by an analysis or a test with its limit (`peer-review-checklist-analysis.md` CK-ANA-G6-4 where an analysis carries it) |
| SA-C-k | k. Error handling | Every error path of the component is handled, none is silently ignored |
| SA-C-l | l. The software can place the system in a safe state | The command or condition that places the system in the safe state is reachable from every state of the component |

## D. Software safety analysis and hazard traceability (SWEHB `swe-205` and `swe-052` section 7.1; SWE-184, SWE-192)

| Id | Check | Evidence to inspect |
|---|---|---|
| SA-D1 | swe-205 task 1: `docs/safety/hazards.json` names every known software contribution of the product's component by action, inaction and incorrect action; the reviewer walks the relevant considerations of SWEHB `swe-205-*.md` section 7.7.2 (for example control of safety-critical hardware, interlocks, inhibits, cautions and warnings, stored sequences, common-cause faults, operator disabling of controls) and records each that applies | `hazards.json` `causes`, `firmware_role`; section 7.7.2 list |
| SA-D2 | swe-205 tasks 2 and 3: the component's criticality and criteria in 07 section 14.1 and 03 section 4.3 equal the union rule of 03 section 4.1 over `hazards.json`; a new or renamed component is assessed | 03 section 4; 07 section 14.1 |
| SA-D3 | swe-205 task 4 and swe-052 task 2: every hazard with a software contribution traces to software requirements and back, both ways, with zero `HAZARD_CONTROL_UNTRACED` and zero `HAZARD_INVERSE` for the product's ids | R3 output; `hazards.json`; requirement files |
| SA-D4 | swe-184 task 1: every safety-tagged software requirement of the component carries its `Depends on:` rationale item naming hardware requirements and `OPS-NNN` operator actions | requirement rationales |
| SA-D5 | swe-192 task 1: every hazard-tracing software requirement has a closing case of method Test, with no exception (04 section 3; `rmm.json` SWE-192 FC) | test case files; R3 output |
| SA-D6 | swe-205 task 5: the software safety analysis (the hazard analysis with software controls traced and tested, plus the fault trees of 07 section 14.2 item i, 07 section 15) is updated for the product's change | `hazard-analysis.md`; 07 section 14.2 |

## E. Peer review, change and configuration assurance (SWEHB `swe-087`, `swe-088`, `swe-089`, `swe-080`, `swe-081`, `swe-187` section 7.1)

| Id | Check | Evidence to inspect |
|---|---|---|
| SA-E1 | swe-087 tasks 1 and 2 and swe-088 task 2: the product's earlier review findings (earlier iterations, liens) are addressed and verified, and none is closed without evidence | earlier records |
| SA-E2 | swe-089 task 1: both records carry the SWE-089 measurements of 07 section 10.3 | both records' front matter |
| SA-E3 | swe-080 tasks 2 and 3 and swe-081 task 2: a change to a controlled item followed its route (CR with `CR:` trailer after the CR-from event, `Editorial:` trailer for an editorial change, `Refs:` for Log and Record classes; 05 sections 4.5 and 5.1), and safety-critical items and hazard data are under configuration management | `git log` of the product files; CR files |
| SA-E4 | swe-187 tasks 1 and 2 (test and code rows): items under test are under configuration management before testing, and a credit run names a tagged release with its VDD (04 section 5.2) | release tags; reports |

## F. Assurance risks, metrics and reporting (07 section 15 rows "5.17 item 10" and "5.17 item 14")

| Id | Check | Evidence to inspect |
|---|---|---|
| SA-F1 | Every assurance concern that is not a product defect is submitted as a risk entry with tag `assurance` to the risk register writer, or named as an existing `RSK-NNN` | findings; `docs/risk/register.json` |
| SA-F2 | The record supplies the MSR-20 and MSR-21 roll-up inputs of 07 section 10.3 (findings by severity and state, including `assurance_findings_major` and `assurance_findings_minor`, items answered No, effort) | front matter |
| SA-F3 | The review package's "Software assurance findings" section (07 section 15 rows "5.17 items 2 and 3") can be written from this record alone: verdict, open findings, tasks applied, reliefs used | record body |

## Completion criteria (SWE-088 b, c; 07 section 10.2)

`assurance_verdict: APPROVED` when: readiness R1 to R4 were true; every task that SA-B1 requires is in the task table and every applicable item of sections A, C, D, E and F is answered, the others listed as N/A with their relief; zero open Major findings; every Minor finding fixed, or deferred with an owner decision reference and a gate (a Minor finding raised after the first APPROVED verdict is a lien due at the next readiness declaration, PDR work plan rule C1); `assurance_tasks_applied` and `swe134_items_checked` are filled; the front matter is complete with the measurements (SWE-089) filled; and `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/validate_docs.py` passes on the record itself. The software lead sets `verdict: APPROVED` on both records only when this record and the paired file review are both APPROVED (07 section 10.2). Findings stay Open until Claude marks them Verified after re-reading the corrected files at their new blobs. On record closure each Deferred finding becomes `RID-<REVIEW>-NNN` in the `rfa-rid-log.json` of its named gate, citing this `INSP-NNN` and the finding id, and is listed in `deferred_rids`. Acceptance of a residual software safety risk is the owner's decision as SMA TA in a decision memo or CR disposition block, never this record's.

## Verdict format (returned by the assurance reviewer)

```
ASSURANCE VERDICT: APPROVED | NEEDS CHANGES
PRODUCT: <path>@<blob>[, ...] at <product_commit>; PAIRED RECORD: INSP-NNN
PRODUCT TYPE: <row>; CRITICALITY: <safety-critical | mission-critical | neither>
FINDINGS:
- [Major] swe-192 7.1 task 1 (SA-D5) REQ-SW-<SUB>-NNN traces to HZ-NNN and has no closing Test case.
- [Minor] SA-F1 the stale-emulator concern is not submitted as a risk entry with tag assurance.
TASKS APPLIED: swe-NNN 7.1 task n, ...
TASKS N/A (relief): swe-125 7.1 task 2 (rmm.json SWE-022 T), ...
SWE-134 ITEMS CHECKED: a, b, ...
MEASUREMENTS: size=<size>; tasks=N; tasks_no=N; turns=N; minutes=N; major=N; minor=N
```
