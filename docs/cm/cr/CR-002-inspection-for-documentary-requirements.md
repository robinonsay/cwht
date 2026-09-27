---
id: CR-002
title: Admit Inspection for hazard-tracing requirements that state a documentary or physical property
status: Dispositioned
class: I
originator: Claude
date_opened: 2026-09-26
phase: Pre-A/A
configuration_at_origination: 7647516 (SRR minutes, owner approval of the SRR; before the baseline/srr tag)
baseline_affected: baseline/srr
affected_cis: [2, 7, 15, 17, 28]
affected_paths: [docs/process/04-verification-and-validation.md, docs/requirements/sys/requirements.json, docs/test_cases/sys/test_cases.json, docs/safety/hazard-analysis.md, tools/traceability.py]
affected_ids: [REQ-SYS-122, REQ-SYS-124, REQ-SYS-137, REQ-SYS-138, TC-SYS-085, TC-SYS-086, TC-SYS-091, RSK-016, RSK-034]
related: [INSP-003, CR-001]
target_release: none
branch: cr/CR-002-inspection-for-documentary-requirements
disposition: Approved
disposition_date: 2026-09-26
relook_trigger: null
relook_by: null
merge_sha: null
date_closed: null
---

# CR-002: Admit Inspection for hazard-tracing requirements that state a documentary or physical property

Template: `docs/templates/change-request.md`. Process: `docs/process/05-configuration-and-data-management.md` §5. Source of the change: SRR package decision 113 (`docs/reviews/SRR/decisions-for-owner.md` Part 1, key decision K12), ruled as recommended by the owner on 2026-09-26 ("I concur with your recommendations for the key decisions", `docs/reviews/SRR/minutes.md`). The recommendation reads: "Approve the CR; Claude writes it and the four method changes." This file is that CR. The products it changes are not yet under the `baseline/srr` tag; the minutes place the tag after the post-ruling work R16 (package section 2.1), so the functional baseline carries this change.

## 1. Description of the change

1. `docs/process/04-verification-and-validation.md` section 3, paragraph "Hazard-tracing requirements", before: "A non-software hazard-tracing requirement (modules SYS, RX, TX, PWR, CTL, ME), which SWE-192 does not govern, uses Test where an instrument of section 6.1 can measure it; otherwise its method is Analysis, its `verification_note` begins `Analysis accepted per RSK-NNN`, and the risk register carries that `RSK-NNN` for the untested hazard control". After: the same sentence with an Inspection route inserted before "Otherwise": when the requirement states a documentary or physical property (content of the operations handbook or another controlled document, a marking or legend on the product, the surface-mount versus hand-solder placement split of the design BOM, CPL and hand-assembly file), its method is Inspection, its closing case is an Inspection case (credit row `I`), its `verification_note` begins `Inspection accepted per CR-002`, and no risk is carried.
2. 04 rule 7.3.6, before: "Every other hazard-tracing requirement has a closing case of method Test, or has method Analysis and a `verification_note` beginning `Analysis accepted per RSK-` naming a risk that exists in `docs/risk/register.json`." After: "Every other hazard-tracing requirement has a closing case of method Test; or has method Inspection, a closing Inspection case and a `verification_note` beginning `Inspection accepted per CR-002` (a documentary or physical property, section 3); or has method Analysis and a `verification_note` beginning `Analysis accepted per RSK-` naming a risk that exists in `docs/risk/register.json`." The software sentence of rule 7.3.6 (every hazard-tracing `REQ-SW-*` closes by Test, SWE-192) is unchanged.
3. 04 section 7.4 row 7.3.6: the planned tool change accepts the Inspection route; until then the procedure reviewer checks it by hand.
4. `docs/requirements/sys/requirements.json`: REQ-SYS-122 (handbook content), REQ-SYS-124 (engraved legend), REQ-SYS-137 and REQ-SYS-138 (placement split) change `verification_method` from Analysis to Inspection; each `verification_note` begins `Inspection accepted per CR-002` in place of `Analysis accepted per RSK-NNN`; the rationales drop the wording "owner disposition pending at SRR".
5. `docs/test_cases/sys/test_cases.json`: the closing cases TC-SYS-085, TC-SYS-086 and TC-SYS-091 change `verification_method` to Inspection, `type` from Simulation to Inspection, and the `Credit row:` key from `A` to `I`.
6. `docs/safety/hazard-analysis.md` section 8.1: the documentation controls REQ-SYS-122 and REQ-SYS-124 close by Inspection per CR-002.
7. `tools/traceability.py`: rule 7.3.6 (`HAZARD_REQ_NOT_TESTED`) accepts method Inspection with the `Inspection accepted per CR-002` note for modules other than `SW` and `SW-<SUB>`, with a known-answer test in `tools/tests/`.

## 2. Reason

INSP-003 finding-17 (`docs/reviews/SRR/checklists/requirements-sys.md`, Minor, lien L-6 "fix before PDR"): 04 section 3 says "If it states a physical or documentary property, the method is Inspection", but rule 7.3.6 admits only Test or Analysis with a risk note for a hazard-tracing requirement. The four requirements therefore carry Analysis, and their closing cases are typed Simulation, for properties that are checked by reading a document, an artwork or a file. The workaround while the CR is open is the present Analysis method with the `Analysis accepted per RSK-NNN` notes (RSK-016 for REQ-SYS-122 and 124; RSK-034 for REQ-SYS-137 and 138).

## 3. Alternatives considered

| Alternative | Why rejected or deferred |
|---|---|
| Do nothing | The four requirements keep a method that contradicts the 04 section 3 rule, INSP-003 finding-17 stays a lien to PDR, and the risk register carries risks for controls that are in fact fully verifiable. |
| Admit Inspection for every hazard-tracing requirement | Too broad: a hazard control that states a number or a behavior must stay Test (or Analysis with a carried risk) so that an untested control is always visible in the register. |
| Keep Analysis and retype the closing cases Inspection | Rule 7.3.3 makes a case closing only when its method equals the requirement's; the cases would become supporting and the requirements would have no closing case. |

## 4. Impact assessment (CM plan §5.3)

| Field | Assessment (numbers, IDs, paths) |
|---|---|
| Performance margins | None: no TPM, MOP or budget changes. |
| Safety | HZ-001 to HZ-007, HZ-009, HZ-011 to HZ-013 (REQ-SYS-122), HZ-001 and HZ-006 (REQ-SYS-124), HZ-015 (REQ-SYS-137, 138): the controls are unchanged; only their verification method changes, from an Analysis that is in substance a document check to an Inspection of the same artifacts. No 07 section 14.1 module changes. Hazard analysis re-issue: yes, section 8.1 wording only (item 6). RF exposure evaluation change: no. |
| Risk | RSK-016 and RSK-034 keep their scores; the four requirements leave their `Analysis accepted per` notes, and the risk owner updates the mitigation text that cites them at the next SRR Track pass (06 section 10). No risk added or closed. |
| Software classification and tailoring | None: SWE-192 (every hazard-tracing `REQ-SW-*` by Test) is unchanged; no RMM or compliance-matrix row changes. |
| Interfaces | None. |
| Operations and ConOps | None: the handbook content that REQ-SYS-122 requires is unchanged. |
| Cybersecurity | None. |
| Verification | TC-SYS-085, TC-SYS-086, TC-SYS-091 change method, type and credit row (item 5); their procedures (document, artwork and file checks) are unchanged. Credit event becomes the `I` row of 04 section 5.2 (CDR for design data, receipt for as-built). `tools/traceability.py` rule 7.3.6 changes (item 7). |
| Cost | None. |
| Schedule | Items 1 to 3 at SRR (done with this CR); items 4 to 6 before the `baseline/srr` tag (package item R16); item 7 before the PDR readiness declaration. |
| Requirements and traceability | REQ-SYS-122, REQ-SYS-124, REQ-SYS-137, REQ-SYS-138: `verification_method`, `verification_note` and rationale; no statement, parent or child changes. Volatility contribution: 4 modified L1 requirements (SWE-200), counted only if item 4 lands after the tag. |
| Regulatory | REQ-SYS-122 carries tag `regulatory`: SRR decision 30 records it as Analysis in the 06 section 14.1 item (g) record and states "REQ-SYS-122 moves to Inspection if decision 113 is approved"; this CR is that move. No 47 CFR clause changes. |
| Documentation | 04 (items 1 to 3); `docs/requirements/sys/requirements.json`; `docs/test_cases/sys/test_cases.json` and its rendering; `docs/safety/hazard-analysis.md` section 8.1; `tools/traceability.py` and `tools/README.md`; the SRR traceability report regenerated. |
| Released units | None. |

Classification rationale: Class I. The change alters the verification method of four L1 requirements and the type of their closing cases, which is a change to verification evidence (CM plan §2 Class I definition). Claude proposes Class I; the owner's ruling on decision 113 approved the CR as recommended without naming a class, so the class is confirmed at the next owner exchange (section 7).

## 5. Implementation plan

| Step | Artifact and path | Responsible | Done (SHA) |
|---|---|---|---|
| 1 | 04 section 3, rule 7.3.6, section 7.4 row 7.3.6 (section 1 items 1 to 3) | Claude (04 maintainer) | the commit that adds this file (section 8) |
| 2 | `docs/requirements/sys/requirements.json` REQ-SYS-122, 124, 137, 138 (item 4) | L1 requirements author | |
| 3 | `docs/test_cases/sys/test_cases.json` TC-SYS-085, 086, 091 (item 5) | TC-SYS test author | |
| 4 | `docs/safety/hazard-analysis.md` section 8.1 (item 6) | hazard analysis author | |
| 5 | `tools/traceability.py` rule 7.3.6 and a known-answer test (item 7) | Claude (tool owner) | `c774851` (brought forward from the PDR readiness declaration to before the `baseline/srr` tag by SRR close-out item 5, `docs/reviews/SRR/minutes.md` commit `dd39332`; re-validation TV-002 run 5) |

Verification of the implementation: the INSP-003 reviewer verifies steps 2 and 4 and closes finding-17; the INSP for the TC-SYS cases verifies step 3; `tools/traceability.py` exits 0 with no `HAZARD_REQ_NOT_TESTED` for the four requirements after step 5; until step 5 the procedure reviewer checks the Inspection route by hand (04 section 7.4 row 7.3.6).

## 6. Independent review of the impact assessment

Required (Class I). Not yet performed: the owner ruled decision 113 on the package row before this file existed; the departure from 05 §5.2 is entry 1 of `docs/cm/deviations.md`. The independent reviewer of INSP-003 reviews this section together with step 2 and records the result here.

| Item | Reviewer (agent invocation) | Date | Finding | Resolution |
|---|---|---|---|---|
| Impact assessment | pending (INSP-003 reviewer) | | | |

Reviewer concurrence: pending.

## 7. CCB disposition (owner)

| Field | Value |
|---|---|
| Decision | Approved |
| Class confirmed | Class I, confirmed by the owner on 2026-09-26: SRR close-out item 7 "CR-002 is Class I", ruled as recommended by the owner's statement "I concur with your recommendations" (`docs/reviews/SRR/minutes.md`, section "Close-out decisions (after the first close-out run)", commit `dd39332`). Before that ruling the field read: Pending, Class I proposed by Claude; the ruling did not name a class |
| Date | 2026-09-26 |
| Conditions | None |
| Rationale | SRR decision 113 (owner ruling 2026-09-26): approve a CR to 04 rule 7.3.6 admitting Inspection for requirements that state a documentary or physical property, so REQ-SYS-122, REQ-SYS-124, REQ-SYS-137 and REQ-SYS-138 close by Inspection instead of Analysis |
| Waiver scope (if Approved (waiver)) | not applicable |
| Re-look trigger and re-look-by review (if Deferred) | not applicable |
| Source | Chat transcription by Claude on 2026-09-26: owner statement "I concur with your recommendations for the key decisions" (key decision K12) and "I approve of this and the SRR", `docs/reviews/SRR/minutes.md` |

Disposition history:

| Date | Decision | New target | Source |
|---|---|---|---|
| 2026-09-26 | Approved (SRR decision 113) | none | owner ruling at the SRR session, transcribed by Claude |
| 2026-09-26 | Class I confirmed (SRR close-out item 7) | none | owner statement "I concur with your recommendations", `docs/reviews/SRR/minutes.md` commit `dd39332`, transcribed by Claude |

## 8. Implementation record

| Commit | Files | Trailer check (`CR: CR-002` present) |
|---|---|---|
| the commit that adds this file | `docs/process/04-verification-and-validation.md` (step 1) | yes |
| `c774851` | `tools/traceability.py`, `tools/tests/test_traceability.py` (step 5) | yes |

Traceability report after implementation: pending steps 2 to 5; renders regenerated: none for step 1.

## 9. Verification of implementation

| Impact item | Planned closure (from §4/§5) | Evidence (report path, TC id, analysis file) | Result |
|---|---|---|---|
| 04 rule text | Step 1 | INSP-003 reviewer delta check | pending |
| Requirement methods | Step 2 | INSP-003 finding-17 closure | pending |
| Closing cases | Step 3 | TC-SYS review record | pending |
| Hazard analysis wording | Step 4 | INSP-008 delta check | pending |
| Tool rule | Step 5 | `tools/tests/test_traceability.py` `InspectionRouteTests` (accepted SYS control, missing or misplaced note, no closing Inspection case, `SW` and `SW-<SUB>` excluded); TV-002 run 5 on an export of `c774851` (182 tests, 0 skipped, pass) and TV-002 section 4.1 run R-2: plain `tools/traceability.py` exit 0, 0 violations, no `HAZARD_REQ_NOT_TESTED` on REQ-SYS-122, 124, 137 or 138 | Pass by the tool owner's run; independent verification by the INSP-015 delta review of TV-002 run 5 pending |

Independent verifier (agent invocation): pending.

## 10. Closure

| Field | Value |
|---|---|
| Owner merge approval | pending |
| Merge commit | pending |
| Waiver entered in CSA item 12 and affected VDDs | not applicable |
| CSA regenerated | pending |
| Date closed | pending |

## 11. History

| Date | State | By | Commit on main | Note |
|---|---|---|---|---|
| 2026-09-26 | Dispositioned | Claude (process author), transcribing the owner | this file's first commit | Written after the owner approved it as SRR decision 113 (the package row served as the request); step 1 applied in the same commit |
| 2026-09-26 | Dispositioned | Claude (tool owner) | `c774851` and the commit that records this row | Step 5 implemented (`c774851`) under SRR close-out item 5; TV-002 re-validated (run 5); Class I confirmed by close-out item 7 (section 7) |
