---
# Peer-review record front matter (charter section 5; docs/plan/semp.md section 7.1;
# docs/safety/hazard-analysis.md section 3). To review the hazard analysis, copy this whole file to
# docs/reviews/<REVIEW>/checklists/safety-hazard-analysis.md: that copy is the single peer-review
# record (there is no peer-reviews/ folder). Fill every field below, answer every applicable
# checklist item, fill the per-hazard table and the findings table. Both front-matter parsers
# (PyYAML and the subset parser of tools/validate_docs.py) strip a comment on its own line and a
# comment written after a value (" # ..."); this template keeps each comment on its own line for
# readability, and comment lines may stay or be deleted when filing. tools/validate_docs.py checks
# the record against the field list of docs/process/01-lifecycle-and-reviews.md section 13 (its
# PEER_REVIEW_RECORD_SCHEMA) and fails while the id, checklist_file, product_commit or date
# placeholder is left in place.
# Search first: 'grep' in an evidence column means: run mcp__claude-context__search_code on
# /Users/robinonsay/rust/cwht first (charter section 11 rule 1), then grep -n only to pin the hit.
#
# id: next free INSP-NNN (never reused, charter section 6); Claude assigns it in the assignment block
id: INSP-NNN
checklist: peer-review-checklist-safety
checklist_revision: A
# checklist_file: this record's own path
checklist_file: docs/reviews/<REVIEW>/checklists/safety-hazard-analysis.md
# product: the hazard analysis; its data file below is reviewed with it as one product (see Record)
product: docs/safety/hazard-analysis.md
# product_commit: quoted so that an all-digit hash stays a string
product_commit: "<commit>"
# data_file and data_file_version: the source of record reviewed with the analysis, and its
# top-level "version" value at product_commit (for example 0.2.0-pha)
data_file: docs/safety/hazards.json
data_file_version: <version>
# product_size: N hazards, N controls, N open questions
product_size: 15 hazards
# sprint: the gate preparation, for example SRR-prep
sprint: SRR-prep
author_agent: <invocation id>
# reviewer_agent: never the author
reviewer_agent: <invocation id>
# criticality: neither. 07 section 2.1.1 takes the criticality of a software component; the hazard
# analysis belongs to none, it determines the 07 section 14.1 set
criticality: neither
# assurance_required: false. 07 section 2.1.1 does not list the hazard analysis; the SWEHB SWE-205
# section 7.1 assurance tasks are items CK-SAF-F1 to F4 of this checklist, done by the reviewer as
# the software assurance function (charter section 2), and the transcription of the determination
# into 03 is assessed separately under peer-review-checklist-classification with its own assurance
# reviewer
assurance_required: false
# assurance_reviewer_agent: invocation id, or none when assurance_required is false
assurance_reviewer_agent: none
# iteration: 1 to 3
iteration: 1
readiness_met: true
# reviewer_verdict: APPROVED | NEEDS CHANGES (the file reviewer)
reviewer_verdict: NEEDS CHANGES
# assurance_verdict: APPROVED | NEEDS CHANGES | not-required
assurance_verdict: not-required
# verdict: set by Claude as lead SE; APPROVED only when reviewer_verdict is APPROVED and
# assurance_verdict is APPROVED or not-required
verdict: NEEDS CHANGES
findings_major: 0
findings_minor: 0
findings_open: 0
findings_fixed: 0
findings_verified: 0
findings_deferred: 0
# assurance_tasks_applied: the SWEHB section 7.1 tasks applied, for example
# [swe-205 7.1 task 1, swe-205 7.1 task 2, swe-205 7.1 task 3, swe-205 7.1 task 4]
assurance_tasks_applied: []
# deferred_rids: RID-<REVIEW>-NNN entered for each Deferred finding at record closure
deferred_rids: []
# items_no: checklist ids answered No
items_no: []
effort_turns: 0
effort_minutes: 0
# record_status: Open | Closed (set by Claude as lead SE)
record_status: Open
date: 2026-MM-DD
date_closed: null
---

# Peer review checklist: hazard analysis and hazard data

**Product.** The hazard analysis `docs/safety/hazard-analysis.md` together with its source of record `docs/safety/hazards.json` (schema `docs/safety/schema.json`), reviewed as one product at every gate the analysis feeds: SRR (preliminary hazard analysis, SWEHB 5.24 safety phases 0 and 1), PDR (controls allocated), CDR (verifications assigned), TRR (test safety provisions) and SAR (controls verified or residual accepted). **Governing:** `docs/plan/semp.md` section 7.1 (hazard scope, closure authority); `docs/safety/hazard-analysis.md` section 3 (identification, severity and likelihood scales, matrix and required response, initial versus residual, owner decisions and TBRs), which SEMP section 7.1 adopts, and sections 6 to 10 and 12; `docs/safety/schema.json`; charter sections 7 (each control's `control_req_ids`, the hazard's `requirement_ids` equal to their union), 9 (evidence classes) and 10 (SWE-134 a to l components); `docs/process/02-requirements-and-traceability.md` section 7 row 2 and rule T-08; the hazard link rule of `docs/process/06-risk-and-decision-analysis.md` section 1; NPR 7150.2D SWE-205 (safety-critical determination), SWE-052 (§3.12.1 Table 1, software requirements to hazards), SWE-134, SWE-184, SWE-192; NPR 7123.1D App. G Table G-4 entrance criterion 6.9 (preliminary system safety analysis) and success criterion 14 (single point failure and fault tolerance philosophy reflected in requirements), carried as SRR entrance rows 14 and 15 of `docs/process/01-lifecycle-and-reviews.md` section 4.3; SWEHB `5-24-hazard-report-minimum-content.md` (minimum content per hazard); SWEHB `swe-205-determination-of-safety-critical-software.md` section 7.1 (software assurance tasks); SE HB App. N (technical peer reviews). **Used by:** an independent reviewer agent that did not author the analysis or the data file (charter sections 2 and 11 rule 4).

Answer every item Yes, No or N/A with evidence (hazard id and field, analysis section and table row, or pasted tool output). Every No is a finding. **Major**: a hazard of the SEMP section 7.1 scope list is missing; a hazard record lacks SWEHB 5.24 content; a severity or likelihood disagrees with the section 3.2 or 3.3 anchors; a High or Serious hazard lacks the section 3.4 minimum controls; a Critical or Catastrophic hazard has an operator procedure or documentation as its only control; `requirement_ids` is not the union of the controls' `control_req_ids` or a hazard-to-requirement link is one-way; a software contribution to a hazard is not identified; the section 6 determination does not follow the union rule; a hazard with unverified controls is carried by no risk; a regulatory limit is misquoted. **Minor**: a stale status or count, wording, a missing citation or an incomplete rationale that does not change a level or a determination.

## Record

This file, copied to `docs/reviews/<REVIEW>/checklists/safety-hazard-analysis.md`, is the single peer-review record for the hazard analysis (charter section 5). The slug follows the `<type>-<product-stem>` rule of `docs/process/01-lifecycle-and-reviews.md` section 13 with type `safety` and stem `hazard-analysis`; `<REVIEW>` is the next gate the analysis feeds. The front matter above is the first thing in the file, unfenced.

One product, two files: `hazards.json` is the analysis's source of record and both files change in one commit (`hazard-analysis.md` section 13), so one record reviews both and `product` names the analysis. `tools/validate_docs.py` compares an RFA/RID log item's `product` with the `product` of the record its `verification.record` names, exactly (the part before any `#`). An item adopted from this record, or verified by it, therefore carries `product: docs/safety/hazard-analysis.md` and names the `hazards.json` element (hazard id, control id, field or `OQ-SAF-NNN`) in its description, even when the defect sits in `hazards.json`.

### Findings (filled by the reviewer; the owner ruling column is transcribed by Claude at the review)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | reviewer | Major or Minor | CK-SAF-xx | file, hazard id and field, or section and row | what is wrong and what would fix it | Open, Fixed, Verified or Deferred | Pending, `Adopt as RID RID-<REVIEW>-NNN`, `Adopt as RFA RFA-<REVIEW>-NNN` or `No action` | `RID-<REVIEW>-NNN` and the owner decision reference, for Deferred only |

Finding rules: ids are `finding-<n>`, numbered from 1 in this record, each with the anchor `<a id="finding-<n>"></a>` in its first cell so that `checklists/safety-hazard-analysis.md#finding-<n>` resolves (01 section 13). The reviewer writes `Pending` in the owner ruling column; Claude transcribes the owner's ruling (*Adopt as RID*, *Adopt as RFA* or *No action*, 01 section 10.1) at the review. `tools/validate_docs.py` rejects `verdict: APPROVED` while any line holding a `finding-<n>` id also holds the words `Major` and `Open`, so write the state only in the State column and do not quote an `Open` status of an open question inside a finding row (write "not answered" instead). Replace the placeholder row above; do not leave it in a filed record.

### Per-hazard results (one row per hazard in `hazards.json`)

| Hazard | Record content and scales (B1 to B4) | Controls meet the section 3.4 response (C2 to C4) | Trace union and back-links (D1, D2) | Software contributions and components (F1, F2) | Risk link two-way (D6) | Finding ids |
|---|---|---|---|---|---|---|
| HZ-NNN | Yes or No | Yes or No | Yes or No | Yes, No or N/A (no firmware on any path) | Yes, No or N/A (Controls verified, Accepted or Retired) | `finding-<n>` or none |

## Readiness criteria (all true before the review starts)

| # | Criterion | Evidence |
|---|---|---|
| R1 | `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/validate_docs.py` exits 0 (convention `hazards`: `docs/safety/hazards.json` against `docs/safety/schema.json`) | tool output line |
| R2 | `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/traceability.py --report-only --output <reviewer scratch directory>/traceability-report.md` reports none of the violations `HAZARD_ID_FORMAT`, `HAZARD_UNRESOLVED`, `HAZARD_CONTROL_UNTRACED`, `SAFETY_TAG_NO_HAZARD`, `HAZARD_REQ_NOT_TESTED`, `HAZARD_REQ_NOT_ON_TARGET`; every `HAZARD_INVERSE` warning is listed in the author's return (it becomes a violation from PDR, 02 section 8.5 row T-08). The absolute `--output` keeps the run from rewriting `docs/vv/traceability-report.md` | tool output |
| R3 | `cd /Users/robinonsay/rust/cwht && .venv/bin/python tools/render_risk.py --check --gate <REVIEW> --hazards docs/safety/hazards.json` exits 0 (hazard link rule, 06 section 1) | tool output |
| R4 | The author's return states the `hazards.json` version the analysis transcribes and lists the hazards added, re-rated or retired and the open questions raised or closed since the previous review | author return |
| R5 | No `TBD` string in either file; every control `tbr` object has `owner`, `plan` and `close_by` | vector search, then grep to pin |

## A. Method, scope and scales (`hazard-analysis.md` sections 1 to 3; SEMP section 7.1)

| Id | Check | Evidence to inspect |
|---|---|---|
| CK-SAF-A1 | Scope: every item of the SEMP section 7.1 hazard scope list maps to at least one `HZ-NNN`, and `hazard-analysis.md` section 1 states the mapping item by item; every hazard beyond the list states why it is added; every exclusion (mission-only failures) states why no hazard follows | SEMP section 7.1; analysis section 1; hazard list section 4 |
| CK-SAF-A2 | Identification (section 3.1): the sources named there were each consulted, including every `SI-NNN`, the ConOps modes, off-nominal scenarios and bench test modes, the risk register and the regulatory corpus; every HZ-candidate item of a research report committed since the previous review is a hazard, part of one, or rejected with a reason | vector search for "HZ-candidate" in `docs/research/`, then grep to pin; `hazards.json` `sources` |
| CK-SAF-A3 | Severity scale (section 3.2): operational definitions per level; each level maps to the register safety level of 06 section 7 as `scales.severity` of `hazards.json` records it (the mapping the hazard link rule uses); every regulatory threshold in a definition (for example the 47 CFR 1.1310 limits, 47 CFR 97.3(a)(23)) agrees with `docs/references/md/regulatory/` | analysis section 3.2; `hazards.json` `scales`; corpus files |
| CK-SAF-A4 | Likelihood scale (section 3.3): anchors are operational and assessed in the uncontrolled state against the fleet horizon of section 2 (build quantity SI-035) | analysis sections 2 and 3.3 |
| CK-SAF-A5 | Matrix and required response (section 3.4): the matrix equals `scales` in `hazards.json` (the schema enforces it for `initial_risk` and `residual_risk.level`); every deviation from the conventional cells is stated with its reason; a required response is stated for every level | analysis section 3.4; R1 output |
| CK-SAF-A6 | Initial versus residual (section 3.5): `residual_risk` counts only controls that have an implementing requirement; each `Requirement pending` control is excluded from the residual and has its `open_questions` request; each residual states its `condition` | `hazards.json` `controls[].status`, `residual_risk`, `open_questions` |
| CK-SAF-A7 | Owner decisions and TBRs (section 3.6): every control number that rests on an undecided proposal reads "Proposed, owner decision pending at <gate>" and the hazard's `decisions_pending` names the decision by its research id; every control `tbr` closes by PDR when an L1 requirement carries the number and by CDR only when the number lives in L2 requirements alone (charter section 7) | `controls[].text`, `controls[].tbr`, `decisions_pending` |
| CK-SAF-A8 | Operating context (section 2): every assumption agrees with the current stakeholder inputs, ConOps and owner decisions (operator model, postures, power steps, charging and USB behaviour, keying modes, assembly model SI-031); a superseded assumption is a finding | analysis section 2; `stakeholder-inputs.md`; `conops.md`; ADRs |

## B. Hazard records (`hazards.json`; SWEHB 5.24 minimum content; `docs/safety/schema.json`)

| Id | Check | Evidence to inspect |
|---|---|---|
| CK-SAF-B1 | Content (SWEHB 5.24 items 1 to 4): each hazard states the scenario, exposed persons, operating phases, causes with their initiating domain, the worst credible effect with the quantities that set its severity, the risk (severity, likelihood, initial level with rationale and confidence), controls with barriers and warnings, and the verification note per control. The schema checks presence; the reviewer checks that each field says something specific to the hazard | each hazard record |
| CK-SAF-B2 | Severity follows the section 3.2 definition of the worst credible effect in the uncontrolled state; any exposure above an FCC limit, for any person, is Critical (section 3.2 rule) | `severity`, `effects`, `rationale` |
| CK-SAF-B3 | Likelihood follows the section 3.3 anchors (a single common operator error or component fault is B; two independent faults are E) with the anchor named in the rationale | `likelihood`, `rationale` |
| CK-SAF-B4 | One exposed population or one energy path per hazard (the section 3.1 split rule); no two hazards describe the same scenario | hazard list |
| CK-SAF-B5 | Status fits the gate: at SRR `Controls proposed` or later, and `Identified` is a finding; at PDR `Controls allocated`; at SAR `Controls verified` or `Accepted` (schema `status` description; analysis section 9 item 4) | `status` |
| CK-SAF-B6 | `history` is append-only (the entries present at the previously reviewed commit are unchanged, compared with `git show <commit>:docs/safety/hazards.json` for the `product_commit` of the previous safety record or the previous baseline tag; N/A for the first review) and its last entry equals the current severity, likelihood, risk and status (analysis section 13) | `history` |
| CK-SAF-B7 | The hazard list of analysis section 4 equals `hazards.json` for every hazard (id, title, severity, likelihood, initial, residual, firmware role, related risks), and the counts line under it recomputes | analysis section 4 |

## C. Controls, fault tolerance and single point failures (sections 3.4, 7 and 8; SWE-134; Table G-4 success criterion 14)

| Id | Check | Evidence to inspect |
|---|---|---|
| CK-SAF-C1 | Each control's `type`, `allocation` and `independent_of_firmware` are true to its text: `independent_of_firmware` is true only when the control acts with no firmware involvement; the `allocation` module can implement it | `controls[]` |
| CK-SAF-C2 | Required response (section 3.4): every High initial hazard has at least one allocated control that is independent of firmware and is neither `Software` nor `Operator procedure`; every Serious residual has at least two independent controls, one of them neither software nor procedure, each verified by Test, with the owner acceptance path named | High and Serious hazards |
| CK-SAF-C3 | No Critical or Catastrophic hazard has an operator procedure or documentation as its only control (section 8.1 item 6) | Critical and Catastrophic hazards |
| CK-SAF-C4 | Every control requirement of a Critical or Catastrophic hazard closes by Test, or appears in the section 8.1 item 7 exception table with the accepting risk and a `verification_note` beginning `Analysis accepted per RSK-NNN` (04 section 7.3 rule 6; T-08 `HAZARD_REQ_NOT_TESTED`) | section 8.1 table; requirement `verification_method` and `verification_note` |
| CK-SAF-C5 | Fault tolerance philosophy (section 8.1) is stated for keying, PA enable, charging and thermal protection (01 section 4.3 row 15) and is reflected in requirements: each philosophy item names the requirement ids whose rationale carries the `Fault tolerance:` item (02 section 4.3 item 5), and each branch the analysis says is not met is a single point failure row with a closing decision (Table G-4 success criterion 14) | section 8.1; requirement rationales |
| CK-SAF-C6 | Single point failure list (section 8.2): every entry of every hazard's `single_point_failures` appears in the list and every list row names a hazard that carries it; each row has a disposition with a closing gate, a closing decision or an accepting risk | section 8.2; `single_point_failures` |
| CK-SAF-C7 | Every `Requirement pending` control has an `open_questions` entry naming the addressee, the missing requirement and `close_by` | `controls[].status`; `open_questions` |
| CK-SAF-C8 | SWE-134 mapping (section 7): items a to l each have a cwht provision, the requirement ids that implement it today or the reserved `REQ-SW-SAFE-NNN` id with its closing gate, the components, and a verification evidence class of charter section 9 (HostUnit primary; Emulation for event order only, never timing); the Hazards column equals the hazards whose `swe134_items` list the item (the reviewer recomputes it) | section 7; `swe134_items` |

## D. Traceability and risk linkage (charter section 7; 02 section 7 row 2 and rule T-08; SWE-052, SWE-184, SWE-192; 06 section 1)

| Id | Check | Evidence to inspect |
|---|---|---|
| CK-SAF-D1 | For every hazard, `requirement_ids` equals the union of its controls' `control_req_ids` (tool warning `HAZARD_INVERSE`; the reviewer recomputes and pastes the differences, or "none") | `hazards.json`; R2 output |
| CK-SAF-D2 | Both directions hold: every requirement a hazard names lists that hazard in `hazard_ids` and carries the tag `safety`, and every requirement whose `hazard_ids` lists a hazard is named by one of that hazard's controls (`HAZARD_INVERSE`, `HAZARD_CONTROL_UNTRACED`, `SAFETY_TAG_NO_HAZARD`) | requirement files; R2 output |
| CK-SAF-D3 | Every requirement named by a control implements that control: its rationale names the hazard and the control id (analysis section 9 item 2) | requirement `rationale` |
| CK-SAF-D4 | Every `safety`-tagged `SW` or `SW-<SUB>` requirement named by a control has the `Depends on:` rationale item naming existing hardware requirements and `OPS-NNN` operator actions (SWE-184; 02 section 4.3 item 4) | software requirement files |
| CK-SAF-D5 | Every hazard-tracing requirement has a closing case of method Test (SWE-192 for `SW` and `SW-<SUB>`, no exception; 04 section 7.3 rule 6 for the other modules, with the Analysis exception of CK-SAF-C4) | R2 output (`HAZARD_REQ_NOT_TESTED`); test case files |
| CK-SAF-D6 | Hazard link rule (06 section 1): every hazard not in `Controls verified`, `Accepted` or `Retired` is carried by at least one active risk whose `related.hazard_ids` names it, the hazard's `related_risk_ids` names every such risk back, and each such risk's safety consequence is at least the level the hazard's severity maps to; analysis section 12 equals the register | R3 output; `docs/risk/register.json`; analysis section 12 |
| CK-SAF-D7 | The field contract of analysis section 9 item 1 matches what `tools/traceability.py` reads (`requirement_ids`, `controls[].control_req_ids`) and the hazard trace section of the traceability report lists every hazard | analysis section 9; traceability report |

## E. Safety-critical software determination (section 6; SWE-205; 03 section 4.1)

| Id | Check | Evidence to inspect |
|---|---|---|
| CK-SAF-E1 | Each hazard's `firmware_role.criteria` is supported by its narrative and by the NASA-STD-8739.8B para 3.2 criteria as reproduced in SWEHB `7-02-classification-and-safety-criticality.md` section 1.2; `criteria` is empty only when firmware has no role in the hazard; `safety_critical` is true exactly when `criteria` is non-empty | `firmware_role`; analysis section 5 |
| CK-SAF-E2 | The section 6.2 table equals the union rule of 03 section 4.1 applied to `hazards.json`: a component is safety-critical when a hazard with non-empty criteria names it in `firmware_role.components`, and its criteria are the union over those hazards (the reviewer recomputes the table and pastes the differences, or "none") | analysis section 6.2; `hazards.json` |
| CK-SAF-E3 | Every difference between section 6.2 and 03 section 4.3 or 07 section 14.1 is listed in analysis section 6.3 or 11.1 and carried by an `OQ-SAF-NNN` with `close_by` | sections 6.3 and 11.1; 03 section 4.3; 07 section 14.1 |
| CK-SAF-E4 | A component treated as mission-critical only (03 section 4.3) is not named in `firmware_role.components` of a hazard with non-empty criteria unless the analysis proposes it as safety-critical with its criteria | `firmware_role.components`; 03 section 4.3 |

## F. Software assurance tasks (SWEHB `swe-205-determination-of-safety-critical-software.md` section 7.1; charter section 2)

| Id | Check | Evidence to inspect |
|---|---|---|
| CK-SAF-F1 | Task 1: for every hazard with firmware on a causal or control path, `causes` names the software contribution by action, inaction and incorrect action (for example a keyer or sequencer fault, a wrong frequency word, a corrupt image load, a missed timeout); the per-hazard table records the result | `causes`, `firmware_role` |
| CK-SAF-F2 | Tasks 2 and 3: the hazard records identify the software components associated with each hazard (`firmware_role.components`, in the 03 section 4.3 and 07 section 14.1 names), and every component that is new or renamed since the previous gate is assessed for safety criticality | `firmware_role.components`; previous baseline of `hazards.json` |
| CK-SAF-F3 | Task 4: traceability between the software requirements and the hazards with software contributions exists in both directions (CK-SAF-D2 for modules `SW` and `SW-<SUB>`; zero `HAZARD_CONTROL_UNTRACED`) | R2 output |
| CK-SAF-F4 | The tasks applied are listed in `assurance_tasks_applied` in the front matter, and each task's result is stated in this record | front matter |

## G. Open questions, regulation and gate maturity

| Id | Check | Evidence to inspect |
|---|---|---|
| CK-SAF-G1 | Every `open_questions` entry has addressee, hazard ids, request, status and `close_by`; every entry whose `close_by` is this gate or earlier is `Answered`, `Closed` or `Withdrawn` with a `resolution`, or is listed in the review package as an owner decision; a status that the products already answer is corrected | `open_questions`; package decision list |
| CK-SAF-G2 | Every `decisions_pending` research id appears in the package decision list with a recommendation | `decisions_pending`; package |
| CK-SAF-G3 | Every regulatory citation (47 CFR 1.1307, 1.1310, 2.1093, 97.13, 97.307 and any other) agrees with the verbatim corpus in `docs/references/md/regulatory/`; every research citation `docs/research/<file>.md F<n>` resolves and carries its confidence tag | corpus files; research reports |
| CK-SAF-G4 | Gate maturity (analysis section 9 item 4; SEMP section 7.1): SRR, all known hazards with causes, proposed controls and risk (SWEHB 5.24 phases 0 and 1); PDR, no control left `Requirement pending`, the hazard-to-requirement table and the final single point failure list, no High residual (section 3.4); CDR, the hazard-control-verification table with every control requirement's `TC-*`; TRR, the section 10 provisions in the `Safety:` line of every Bench and OnAir case (04 section 7.3 rule 7); SAR, every control verified or the residual accepted by the owner in the decision memo | the sections named for the gate |
| CK-SAF-G5 | Test and bench safety provisions (section 10) cover every hazard reachable during hand assembly, bench test and the first on-air series, with the named abort for every keyed step | analysis section 10 |

## Completion criteria (SWE-088 b, c)

`verdict: APPROVED` when: readiness R1 to R5 were true; every applicable item is answered and the others are listed as N/A; the per-hazard table has one row per hazard; zero open Major findings; every Minor finding fixed, or deferred with an owner decision reference and a gate; `assurance_tasks_applied` lists the tasks of section F; the front matter is complete with the measurements (SWE-089) filled; and `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/validate_docs.py` passes on the record itself. Findings stay Open until Claude marks them Verified after re-reading the corrected files. On record closure each Deferred finding becomes `RID-<REVIEW>-NNN` in the `rfa-rid-log.json` of its named gate, citing this `INSP-NNN` and the finding id, with `product: docs/safety/hazard-analysis.md`, and is listed in `deferred_rids`. Hazard closure itself (every control verified, residual accepted) is the owner's decision as SMA TA in a decision memo (SEMP section 7.1), never this record's.

## Verdict format (returned by the reviewer)

```
VERDICT: APPROVED | NEEDS CHANGES
FINDINGS:
- [Major] CK-SAF-D1 HZ-NNN: requirement_ids lacks REQ-SYS-NNN, which control Kn names in control_req_ids.
- [Minor] CK-SAF-G1 OQ-SAF-NNN: the products answer it (REQ-SYS-NNN) but its status is not updated.
ITEMS N/A: none
MEASUREMENTS: size=N hazards; turns=N; minutes=N; major=N; minor=N
```
