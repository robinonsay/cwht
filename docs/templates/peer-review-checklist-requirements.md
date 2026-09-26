---
# Peer-review record front matter (charter section 5; docs/process/07-software-engineering-plan.md
# section 10.2). To review a product, copy this whole file to
# docs/reviews/<REVIEW>/checklists/<product-slug>.md: that copy is the single peer-review record
# (there is no peer-reviews/ folder). Fill every field below, answer every checklist item and
# fill the findings table. Both front-matter parsers (PyYAML and the subset parser of
# tools/validate_docs.py) strip a comment on its own line and a comment written after a value
# (" # ..."); this template keeps each comment on its own line for readability, and comment lines
# may stay or be deleted when filing. tools/validate_docs.py checks the record against the field
# list of docs/process/01-lifecycle-and-reviews.md section 13 (its PEER_REVIEW_RECORD_SCHEMA) and
# fails while the id, checklist_file, product_commit or date placeholder is left in place.
# Search first: 'grep' in an evidence column means: run mcp__claude-context__search_code on
# /Users/robinonsay/rust/cwht first (charter section 11 rule 1), then grep -n only to pin the hit.
#
# id: next free INSP-NNN (never reused, charter section 6)
id: INSP-NNN
checklist: peer-review-checklist-requirements
checklist_revision: C
# checklist_file: this record's own path
checklist_file: docs/reviews/<REVIEW>/checklists/<product-slug>.md
# product: exact path, or CR-NNN
product: docs/requirements/sw/sw-keyer/requirements.json
# product_commit: quoted so that an all-digit hash stays a string
product_commit: "<commit>"
# product_size: N requirements, or N sections for a plan
product_size: 14 requirements
# sprint: SW-NN-<module>, or the gate preparation such as PDR-prep
sprint: SW-NN-<module>
author_agent: <invocation id>
# reviewer_agent: never the author
reviewer_agent: <invocation id>
# criticality: safety-critical | mission-critical | neither (plan section 14.1)
criticality: safety-critical
# assurance_required: true | false, from the table of plan section 2.1.1
assurance_required: true
# assurance_reviewer_agent: invocation id, or none when assurance_required is false
assurance_reviewer_agent: <invocation id>
# iteration: 1 to 3
iteration: 1
readiness_met: true
# reviewer_verdict: APPROVED | NEEDS CHANGES (the file reviewer)
reviewer_verdict: NEEDS CHANGES
# assurance_verdict: APPROVED | NEEDS CHANGES | not-required
assurance_verdict: NEEDS CHANGES
# verdict: set by the software lead; APPROVED only when reviewer_verdict is APPROVED and
# assurance_verdict is APPROVED or not-required
verdict: NEEDS CHANGES
findings_major: 0
findings_minor: 0
findings_open: 0
findings_fixed: 0
findings_verified: 0
findings_deferred: 0
assurance_findings_major: 0
assurance_findings_minor: 0
# assurance_tasks_applied: SWEHB section 7.1 tasks applied, for example [swe-134 7.1 task 1]
assurance_tasks_applied: []
# deferred_rids: RID-<REVIEW>-NNN entered for each Deferred finding at record closure
deferred_rids: []
# items_no: checklist ids answered No
items_no: []
effort_turns: 0
effort_minutes: 0
# record_status: Open | Closed (set by the software lead, plan section 10.2)
record_status: Open
date: 2026-MM-DD
date_closed: null
---

# Peer review checklist: requirements, plans and stakeholder products

**Product types and the sections that apply.** A reviewer answers the applicable items and lists the others under `ITEMS N/A`.

| Product type | Applicable sections and items |
|---|---|
| Requirement files, any level (`docs/requirements/**/requirements.json`: SYS L1; RX, TX, PWR, CTL, ME and the firmware-wide SW file at L2; the software module files `docs/requirements/sw/sw-<sub>/requirements.json`, L2 module files in the charter's numbering) | A to F, and one row per requirement in the per-requirement validation table (WR-01 to WR-14 and V1 to V6) |
| Change Requests that touch requirements | A to F for every added or changed requirement, plus B7 and readiness R5, and one per-requirement validation row for each added or changed requirement |
| Stakeholder expectations `docs/requirements/l0-stakeholder/expectations.json` (NGO, MOE and success-criterion records) | A3, A4, A5, A7, A8; B1 to B3 (the parent is the `SI-NNN` or `CON-NNN` source); E4 (every MOE is observable and measurable); F1 to F3. Not applicable: A1, A2, A6 (NGO and MOE records are not "shall" statements and carry `NGO-`/`MOE-` ids, charter section 6), B4 to B7, C, D, E1 to E3, E5, E6, F4, G |
| ConOps `docs/conops/conops.md` (`OPS-NNN` scenarios, SE HB App. S) | A3, A4, A8; B4 (each scenario names the NGOs and MOEs it exercises; both key types where keying is involved); C5 and C6 (state names match the architecture; off-nominal scenarios present); F2; G1, G2. Others not applicable |
| Plans and process documents: `docs/process/07-software-engineering-plan.md`, the software section of `docs/vv/plan.md`, every `docs/process/0N-*.md`, `docs/plan/semp.md`, `docs/plan/technology-assessment.md` (SWE-087 b) | G (all items) and A8 |
| ADRs, until a dedicated checklist exists (the section G fallback of `docs/process/08-agent-briefing.md` section 3.1); trade studies use `docs/templates/peer-review-checklist-risk.md` section B | G1, G2, G7, G8 and A8 |

**Governing:** charter section 7 (writing rules, SE HB App. C), charter section 11 rule 4 (independence), SE HB §4.2.1.2.4 (six validation checks), `docs/process/02-requirements-and-traceability.md` section 4.2 (writing rules WR-01 to WR-14, the single banned-word list) and section 5 (validation steps V1 to V6 and the per-requirement record row), NPR 7150.2D SWE-050, SWE-051, SWE-052, SWE-055, SWE-184, SWE-087, SWE-088, SWE-089; `docs/process/07-software-engineering-plan.md` section 10 (procedure) and section 2.1.1 (when the software assurance review is required). **Used by:** an independent reviewer agent that did not author the file; a second, software assurance reviewer where the table of plan section 2.1.1 says Yes. The assurance reviewer applies the `# 7. Software Assurance` section of the SWEHB pages for the SWEs the file implements (`docs/references/md/swehb/swe-050-*.md`, `swe-051-*.md`, `swe-184-*.md`, `swe-134-*.md`) and SWEHB topic `6-2` (checklist for general software safety requirements), writes its verdict and findings into the same record and lists the tasks applied in `assurance_tasks_applied`.

Answer every item Yes, No or N/A with evidence (requirement id and field, or section number). Every No is a finding with a severity: **Major** (the requirement would be wrong, unverifiable, untraceable, unsafe or ambiguous; blocks `APPROVED`) or **Minor** (editorial or completeness item fixed before the next gate).

## Record

This file, copied to `docs/reviews/<REVIEW>/checklists/<product-slug>.md`, is the single peer-review record for the product (charter section 5; plan section 10.2). The slug is `requirements-<module>` for a requirement file, `cr-NNN` for a Change Request, `plan-<document-stem>` for a plan or process document, `expectations`, `conops` or `adr-nnn` for the other product types (a trade study is reviewed with `docs/templates/peer-review-checklist-risk.md`, slug `ts-nnn-<slug>`). `<REVIEW>` is the next gate the product feeds. The front matter above is the first thing in the file, unfenced.

### Findings (filled by the reviewer and the assurance reviewer; the owner ruling column is transcribed by Claude at the review)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | reviewer or assurance | Major or Minor | CK-REQ-xx or WR-NN or Vn | id and field, or section | what is wrong and what would fix it | Open, Fixed, Verified or Deferred | Pending, `Adopt as RID RID-<REVIEW>-NNN`, `Adopt as RFA RFA-<REVIEW>-NNN` or `No action` | `RID-<REVIEW>-NNN` and the owner decision reference, for Deferred only |

Finding rules: ids are `finding-<n>`, numbered from 1 in this record, each with the anchor `<a id="finding-<n>"></a>` in its first cell so that `checklists/<product-slug>.md#finding-<n>` resolves (01 section 13); `tools/validate_docs.py` finds findings only by that `finding-<n>` pattern. A writing-rule failure or a failed validation step is a finding like any other: its Item names the WR id (severity per 02 section 4.2: Major for WR-01, WR-03, WR-04, WR-05, WR-07, WR-11 and WR-13, Minor for the others) or the step V1 to V6 and the CK-REQ item of the mapping below. One finding may cover several requirements when the defect and the fix are the same; its Location lists them. The reviewer writes `Pending` in the owner ruling column; Claude transcribes the owner's ruling (*Adopt as RID*, *Adopt as RFA* or *No action*, 01 section 10.1) at the review. `tools/validate_docs.py` rejects `verdict: APPROVED` while any line holding a `finding-<n>` id also holds the words `Major` and `Open`, so write the state only in the State column and keep severity and state words out of the per-requirement table below. Replace the placeholder row above; do not leave it in a filed record.

### Per-requirement validation (requirement files and CRs; 02 sections 4.2 and 5; SE HB §4.2.1.2.4)

One row per requirement in the file, in id order, retired entries included; for a CR, one row per added or changed requirement. With the findings table, this table is the V1 to V6 validation record that 02 section 5 requires for every L1 requirement before SRR and for every L2 requirement before PDR (02 section 12). The columns are those of 02 section 5, in its order.

| Requirement | WR failures | V1 | V2 | V3 | V4 | V5 | V6 | CK-REQ items answered No | Disposition |
|---|---|---|---|---|---|---|---|---|---|
| REQ-<MOD>-NNN | none | Pass | Ready: customer, user | Pass | Pass | Pass | Pass | none | Pass |

| Column | Allowed values and rule |
|---|---|
| WR failures | `none`, or the ids of the 02 section 4.2 rules the requirement fails (WR-01 to WR-14). Copy the lint hits of `tools/traceability.py` for the rules 02 marks "tool" first, then judge every rule, including the cases the lint cannot see. A retired entry reads `retired` and is checked only against 02 section 11.3 (status `Closed`, tag `retired`, no `tbr` object, `rationale` beginning `Retired by `); its V1 to V6 cells read `N/A` |
| V1 | `Pass` when WR failures is `none` and the tool reports no violation for the id; `Fail` otherwise |
| V2 | `Ready:` followed by the `role` values of the stakeholder groups of 02 section 3.0 (`expectations.json` `stakeholders`) whose inputs the requirement traces to, for example `Ready: customer, user, regulator`, when every `source_id` resolves, the statement reflects the cited `SI`, `NGO`, `MOE` or `OPS` entry, and the core-input coverage of the 02 section 5 V2 criterion holds; `Fail` otherwise. The named groups are the ones Robin's confirmation speaks for (02 section 3.0 representation rule). The reviewer prepares V2; Robin performs it, and his confirmation is recorded in the V2 block below |
| V3 | `Pass`, or `Fail` followed by the failing letters of the 02 section 5 V3 criterion: (a) trace to a baselined expectation, (b) `Assumes:` items, (c) phase success criteria, (d) ICD values, (e) `Depends on:` items, (f) regulatory text, (g) `Fault tolerance:` item; for example `Fail (b, d)` |
| V4 | `Pass` or `Fail` against the 02 section 5 V4 criterion |
| V5 | `Pass` or `Fail` against the 02 section 5 V5 criterion |
| V6 | `Pass` or `Fail` against the 02 section 5 V6 criterion. At SRR every T-18 unallocated listing (from `tools/traceability.py` once T-18 is implemented, otherwise the by-hand listing of the review package, 02 section 8.5) is confirmed or corrected in this column; a necessity that is not obvious is argued in the V6 notes below |
| CK-REQ items answered No | `none`, or the section A to F item ids this requirement fails |
| Disposition | `Pass` when every cell passes (V2 `Ready:`, WR failures `none`). Otherwise the ids of the findings that carry the failures (`finding-<n>`, every `Fail` and every WR failure is in a finding); after the owner's ruling at the review Claude replaces them with the `RID-<REVIEW>-NNN` the owner adopted, or with `Pass` once every such finding is `Verified` or ruled *No action*. `Retire finding-<n>` when the reviewer finds the requirement redundant, unnecessary or superseded and the finding states the reason; before the level's baseline the author retires it per 02 section 11.3 with a `rationale` beginning `Retired by INSP-NNN: ` (this record's id) that names `checklists/<product-slug>.md#finding-<n>`, and the cell then reads `Retire`. The final values are those of 02 section 5: `Pass`, `RID-<REVIEW>-NNN` or `Retire` |

Writing rules (quick reference; 02 section 4.2 holds the pass tests and the single banned-word list, which is not copied here):

| Id | Rule | Lint (02 section 4.2 "tool") | Severity of a failure | Checklist items (02 section 5 mapping) |
|---|---|---|---|---|
| WR-01 | Terms | tool | Major | CK-REQ-A1 |
| WR-02 | Form and voice | reviewer | Minor | CK-REQ-A1 |
| WR-03 | One thought | reviewer | Major | CK-REQ-A2 |
| WR-04 | Quantified | reviewer | Major | CK-REQ-A3 |
| WR-05 | Implementation-free | reviewer | Major | CK-REQ-A5 |
| WR-06 | Product, not operations or tasks | reviewer | Minor | none (judged directly) |
| WR-07 | No unverifiable or ambiguous words | tool | Major | CK-REQ-A4 |
| WR-08 | Positive form | reviewer | Minor | none (judged directly; record why a `shall not` is admitted) |
| WR-09 | Level and location | reviewer | Minor | CK-REQ-B1, CK-REQ-F3 |
| WR-10 | Rationale content (02 section 4.3) | reviewer | Minor | CK-REQ-A7 |
| WR-11 | Verification assigned at definition | reviewer | Major | CK-REQ-E1, CK-REQ-E2 |
| WR-12 | TBD/TBR | tool | Minor | readiness R4 |
| WR-13 | Traceability fields | reviewer | Major | CK-REQ-B1, CK-REQ-B5, CK-REQ-B6 |
| WR-14 | Editorial and schema | tool, partly | Minor | CK-REQ-A6, CK-REQ-A8 |

Validation steps (quick reference; the pass criteria are those of 02 section 5, not copied here):

| Step | Question (SE HB §4.2.1.2.4) | Who | Checklist section (02 section 5 mapping) |
|---|---|---|---|
| V1 | Are the requirements written correctly? | Reviewer | A, plus WR-06 and WR-08 judged directly |
| V2 | Do the requirements satisfy stakeholders? | Robin, for every stakeholder group of 02 section 3.0, with the reviewer's trace | B4 evidence and Robin's confirmation |
| V3 | Are the requirements technically correct? | Reviewer | C |
| V4 | Are the requirements feasible? | Reviewer | D |
| V5 | Are the requirements verifiable? | Reviewer, test-author agent consulted | E |
| V6 | Are the requirements redundant or over-specified? | Reviewer | F |

V2 confirmation (one row per stakeholder group of 02 section 3.0; the reviewer fills the first three columns, Claude transcribes Robin's confirmation):

| Stakeholder group (`name` and `role`) | `represented_by` | Requirements whose V2 cell names the group (count), and those marked `Fail` (ids) | Robin's confirmation (decision memo `docs/reviews/<REVIEW>/decision-memo.md` item and date) |
|---|---|---|---|
| <`name` from `expectations.json` `stakeholders`>, <`role`> | <`represented_by`> | | |

V6 notes (only for requirements whose necessity is not obvious, and for every duplication between levels):

| Requirement | Worst outcome if omitted, or the level that keeps a cross-level duplicate (SE HB §6.2.1.2.3) |
|---|---|
| REQ-<MOD>-NNN | |

## Readiness criteria (all true before the review starts)

| # | Criterion | Evidence |
|---|---|---|
| R1 | The product validates: `.venv/bin/python tools/validate_docs.py` exits 0 | tool output line |
| R2 | `.venv/bin/python tools/traceability.py` reports no violation for the ids in the file (unique ids, parents exist, verification cases exist or are marked planned in the brief) | tool output |
| R3 | The author's return states the self-check against sections A to G below and lists the brief's acceptance criteria | author return |
| R4 | Every `TBR` has `owner`, `plan`, `close_by`; there are no `TBD` strings anywhere in the file | grep |
| R5 | For a CR: the impact assessment (cost, schedule, margins, safety, interfaces, verification) is attached | CR record |

## Participants

Author agent (not present); reviewer agent; software assurance reviewer where the table of plan section 2.1.1 says Yes (for this checklist: requirement files and CRs of safety-critical or mission-critical components of plan section 14.1, the firmware-wide SW file, this plan, the software section of `docs/vv/plan.md` and `docs/process/03-software-classification-and-rmm.md`); owner for disposition of deferred findings.

## A. Format and editorial (SE HB App. C checklists C.1, C.2, C.3; charter section 7)

| Id | Check | Evidence to inspect |
|---|---|---|
| CK-REQ-A1 | `description` contains exactly one "shall", in active voice, of the form "The <product> shall <verb> <object> <condition>"; no "will", "should", "must" | each `description` |
| CK-REQ-A2 | `description` is at most 25 words (schema note) and states one requirement only; compound "and", "or" or lists are split into separate requirements unless the coupling is intrinsic and the rationale says so | word count; conjunctions |
| CK-REQ-A3 | Every quantity has a number, a unit and a tolerance or bound (`<=`, `>=`, `+/-`, range); units are SI or the standard amateur radio unit (W, dBm, dBc, Hz, ms, µs, WPM, mV, degrees C) and spelled consistently | `description` |
| CK-REQ-A4 | Free of every word in the single project banned-word list, rule WR-07 of `docs/process/02-requirements-and-traceability.md` section 4.2 (group A modal verbs other than shall; group B unverifiable or ambiguous words from SE HB App. C.4); `tools/traceability.py` lints the same list (T-17), and the reviewer additionally rejects standalone `this`/`these`, other "ly" adverbs and "-ize" verbs standing in for a measurable criterion | `description`, `title`; tool output |
| CK-REQ-A5 | Implementation-free: states what, not how (no part numbers, algorithms or module names in `description`; those belong in `rationale` or `design_refs`) | `description` |
| CK-REQ-A6 | `title` has no "shall" language and is at most 80 characters; `id` follows `REQ-<MOD>-NNN` with the module of the file; ids are not reused (a retired item keeps its id with status `Closed`, tag `retired` and a rationale, charter section 6) | `id`, `title` |
| CK-REQ-A7 | `rationale` is present, explains why (not restating the requirement), and cites the source: `SI-NNN`, `NGO`, `MOE`, `OPS-NNN`, regulation clause (for example `47CFR97.307(e)`), `ADR-NNN`, `TS-NNN`, `HZ-NNN`, or SWE-134 item | `rationale`, `source_ids` |
| CK-REQ-A8 | Grammar, spelling and terminology match the project glossary (SEMP Appendix A; plan Annex D for software terms) and the enum spellings pinned in the SYS L1 file (state names, mode names, key types "straight key", "iambic paddle") | text |

## B. Stakeholder satisfaction and traceability (SE HB §4.2.1.2.4 check 2; SWE-051, SWE-052)

| Id | Check | Evidence to inspect |
|---|---|---|
| CK-REQ-B1 | `parent_id` names an existing higher-level requirement, or `parent_id` is null with `source_ids` and a rationale explaining the self-derivation (hazard control, ICD, ADR, SWE-134) | `parent_id`, `source_ids` |
| CK-REQ-B2 | The requirement is necessary for its parent: removing it would leave the parent unsatisfied or a hazard uncontrolled | reasoning recorded in the finding if No |
| CK-REQ-B3 | The set of children of each parent is sufficient: together they satisfy the parent (no allocation gap), checked against `docs/design/allocation.json` where it exists | allocation |
| CK-REQ-B4 | Every ConOps scenario `OPS-NNN` that touches this module is covered by at least one requirement in the file; both key types (SI-018: straight key and iambic paddles) are covered where keying is involved | `docs/conops/conops.md` |
| CK-REQ-B5 | `hazard_ids` are present on every requirement that controls or mitigates a hazard, and every software control listed in `docs/safety/hazards.json` for this module appears as a requirement (NPR 7150.2D §3.12.1 Table 1: software requirements to hazards) | hazards file |
| CK-REQ-B6 | `tags` are consistent (`safety` on every hazard-controlling requirement; `regulatory` on every Part 97 derived requirement; `revA`, `70cm-ready` as the requirement's scope states) | `tags` |
| CK-REQ-B7 | For a CR: every downstream item (children, design elements, test cases, ICDs) affected is listed and the volatility count for MSR-02 is updated | CR record |

## C. Technical correctness (SE HB §4.2.1.2.4 check 3; SWE-184)

| Id | Check | Evidence to inspect |
|---|---|---|
| CK-REQ-C1 | Values are physically and regulatorily correct: receive band 144.000 to 148.000 MHz and transmit carrier 144.001 to 147.999 MHz (REQ-SYS-008, REQ-SYS-009, TBR; ADR-016, ADR-023), emission limits per 47 CFR 97.307(e) as cited, keyer speed and timing consistent with dot = 1200/WPM ms, battery and thermal limits consistent with the hardware L2 files | cross-reference |
| CK-REQ-C2 | Values are consistent with the ICDs (`docs/icd/ICD-*`) and the hardware L2 requirements they depend on (ADC ranges, pin functions, synthesizer step) | ICDs |
| CK-REQ-C3 | Safety constraints, controls, mitigations and assumptions between hardware, operator and software are stated explicitly (SWE-184): what hardware interlock is assumed, what the operator must do, what software does | `SW-SAFE` file, `rationale` |
| CK-REQ-C4 | For `SW-SAFE`: the twelve SWE-134 provisions of `07-software-engineering-plan.md` section 14.2 are each present as a requirement with the plan's budget values or a `TBR` with `close_by: PDR`; off-nominal responses and their time limits are requirements (SWE-134 j). For every other safety-critical or mission-critical module or unit of plan section 14.1: the SWE-134 items listed for it in plan section 14.2 (second table) are present as module requirements that reference the `REQ-SW-SAFE-NNN` row they specialize | `REQ-SW-SAFE-001` to `-012`; module files; `hazards.json` |
| CK-REQ-C5 | States and modes: requirements name only states defined in the architecture (Boot, SafeState, Receive, TxPending, Transmit, Fault, ChargeInhibited) and invalid transitions are stated as rejections (NPR 7150.2D §4.2.2 g) | state names |
| CK-REQ-C6 | Undesired events and their required responses are specified (stuck key, corrupted configuration, sensor out of range, watchdog reset, brown-out, clock fault, tick overrun), not only nominal behavior (SE HB App. C.4 "undesired events") | off-nominal requirements |
| CK-REQ-C7 | Cybersecurity-tailored requirements exist where plan section 16 requires them: image integrity at boot, configuration integrity, event log content (SWE-210), no command path on the key line; no personal data field (plan section 16.6) | `SW-BOOT`, `SW-CFG`, `SW-DIAG`, `SW-KEYER` files |
| CK-REQ-C8 | Loaded data acceptance (SWE-193): requirements state what happens for valid, out-of-range and corrupted configuration and for a corrupted image | `SW-CFG`, `SW-SAFE` configuration guard, `SW-BOOT` |

## D. Feasibility (SE HB §4.2.1.2.4 check 4)

| Id | Check | Evidence to inspect |
|---|---|---|
| CK-REQ-D1 | Timing values are achievable on the RP2350 at 150 MHz with the 1 µs TIMER, the 1 kHz input sampling and the 1 ms scheduler tick of plan section 5 (for example, no requirement demands a software response faster than one sample period) | values |
| CK-REQ-D2 | Resource-related values respect the budgets (flash below 25 percent of 4 MB, RAM below 40 percent of 520 KB yellow lines, MSR-18, MSR-19) | values |
| CK-REQ-D3 | The requirement can be met without an external runtime crate (CS-02), within the target platform rules CS-34 to CS-37 and within the rustos work packages of plan section 19, or the file names the new work package | plan sections 7.7 and 19 |
| CK-REQ-D4 | Tolerances are defensible: the rationale says why the tolerance is what it is; doubling the tolerance would visibly change the product (SE HB App. C.4 "tolerances") | `rationale` |

## E. Verifiability (SE HB §4.2.1.2.4 check 5; charter section 9; SWE-066, SWE-192)

| Id | Check | Evidence to inspect |
|---|---|---|
| CK-REQ-E1 | `verification_method` is assigned and is the least costly method that can show compliance; Analysis is used only where a test is impossible before delivery or the requirement is analytical by nature | method |
| CK-REQ-E2 | `verification_note` names the pre-build class (HostUnit, Emulation, Simulation, Inspection) and the post-build class (Bench, OnAir) and, for software Test, states whether the logic is platform-independent (`04-verification-and-validation.md` section 5.2); a requirement that states a duration, latency, rate or timeout never names Emulation as its closing class (ADR-011) | `verification_note` |
| CK-REQ-E3 | Every requirement with `hazard_ids` has method Test (SWE-192) | method versus hazards |
| CK-REQ-E4 | The requirement is observable at the software boundary (inputs, outputs, pin states, timestamps, display content) so a test can assert it; internal-only wording ("the variable shall be set") is rejected | `description` |
| CK-REQ-E5 | A Bench-verified requirement can be measured with an instrument of `docs/process/04-verification-and-validation.md` section 6.1 (NanoVNA; tinySA Ultra with the calibrated 30 to 40 dB attenuator, purchase committed by the owner in SI-034 and recorded in ADR-021, its receipt recorded by ADR before TRR per charter section 9; Pico-based logic capture; 50 ohm dummy load; bench supply; multimeter), each credit-bearing only with its TV record, or names the section 6.2 alternative method it depends on | `verification_note` |
| CK-REQ-E6 | At least one `TC-*` case cites the requirement, or the brief names the test-author sprint that will write it before the baselining gate | traceability report |

## F. Non-redundancy and consistency (SE HB §4.2.1.2.4 check 6)

| Id | Check | Evidence to inspect |
|---|---|---|
| CK-REQ-F1 | No two requirements in the file, or across the firmware-wide SW file and the module files (L2), state the same thing or conflict (search for the same quantity with different values) | vector search for the quantity, then grep on units and quantities to pin |
| CK-REQ-F2 | Terminology and enum spellings are identical to the SYS L1 file and the architecture (no "PA enable" versus "PA_EN" versus "amplifier on" variation) | text |
| CK-REQ-F3 | The file has no requirement that belongs to another module (keyer timing in `SW-DISPLAY`, for example) | module scope |
| CK-REQ-F4 | `priority` (`KDR`, `Baseline`, `Goal`) is set; `Goal` items use "should" only in `rationale`, never in `description` | `priority` |

## G. Plans, process documents and decision records (SWE-087 b)

| Id | Check | Evidence to inspect |
|---|---|---|
| CK-REQ-G1 | The document expands a charter section and does not contradict the charter, `docs/process/rmm.json`, `docs/process/se-compliance-matrix.json` or an Accepted ADR; every disagreement found is listed as a finding with the conflicting sentences | charter, RMM, matrix, ADRs |
| CK-REQ-G2 | Every process step names the artifact it produces or consumes with its path and the id scheme it uses; no "as appropriate", "TBD", "should consider" without naming who decides and when | text |
| CK-REQ-G3 | Roles, independence and the owner's approval points are stated (SWE-013 plan content; charter section 2) | roles section |
| CK-REQ-G4 | Tailored requirements the document relies on are mirrored with their RMM or compliance-matrix disposition (SWE-121) | tailoring section |
| CK-REQ-G5 | The cybersecurity section identifies assets, surfaces, threats, mitigations and the tests that verify them (SWE-154, SWE-156, SWE-159) | cybersecurity section |
| CK-REQ-G6 | Measurements are named with source, threshold, storage location and analysis rule (SWE-090, SWE-093) | measurement section |
| CK-REQ-G7 | Tool claims are true and dated: every tool named exists at the stated version on the owner's machine (checked against `tools/toolchain.lock.md` and, where the reviewer can, by running its version command) and the document states honestly what the tool cannot do (for example MC/DC for Rust, timing in the emulator) | plan section 8 versus `tools/toolchain.lock.md` |
| CK-REQ-G8 | Citations use only identifiers that exist in the corpus (`SWE-NNN`, `SE-NN`, `SE HB §x.y`, App. G table ids); no NASA requirement is paraphrased as a quotation | vector search (`mcp__claude-context__search_code`, charter section 11 rule 1), then `grep -n` in `docs/references/md/` to pin |

## Completion criteria (SWE-088 b, c)

`verdict: APPROVED` when: readiness R1 to R5 were true; every applicable item answered and the others listed as N/A; for a requirement file or CR, the per-requirement validation table has a row for every requirement in scope with every WR and V1 to V6 cell filled, every `Fail` and every WR failure carried by a finding, and the V2 block names every stakeholder group of 02 section 3.0; zero open Major findings; every Minor finding fixed, or deferred with an owner decision reference and a gate; the front matter is complete with the measurements (SWE-089) filled; where plan section 2.1.1 says Yes the assurance reviewer has returned `APPROVED` (`assurance_verdict`); and `.venv/bin/python tools/validate_docs.py` passes on the record itself. Findings stay Open in the record until the software lead marks them Verified after re-reading the corrected file. On record closure each Deferred finding becomes `RID-<REVIEW>-NNN` in the `rfa-rid-log.json` of its named gate, citing this `INSP-NNN` and the finding id, and is listed in `deferred_rids` (plan section 10.2).

## Verdict format (returned by the reviewer)

```
VERDICT: APPROVED | NEEDS CHANGES
FINDINGS:
- [Major] CK-REQ-A4 (WR-07, V1) REQ-SW-KEYER-NNN description: "quickly" is unverifiable; state the latency in ms with a bound.
- [Minor] CK-REQ-A7 (WR-10) REQ-SW-KEYER-NNN rationale: cite the OPS-NNN scenario that exercises it.
ITEMS N/A: CK-REQ-G1 to CK-REQ-G8 (product is a requirements file)
MEASUREMENTS: size=N requirements; rows=N; rows_with_wr_failures=N; v_fail=V1:N V2:N V3:N V4:N V5:N V6:N; turns=N; minutes=N; major=N; minor=N
```
