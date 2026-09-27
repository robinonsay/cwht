---
id: CR-009
title: Fix the SRR peer review liens of the L0 set, the ConOps and the concept
status: Submitted
class: I
originator: Claude
date_opened: 2026-09-27
phase: B
configuration_at_origination: baseline/srr (tag on 779f93f); HEAD ab2af2d on main
baseline_affected: baseline/srr
affected_cis: [5, 6, 52]
affected_paths: [docs/requirements/l0-stakeholder/expectations.json, docs/requirements/l0-stakeholder/expectations.md, docs/conops/conops.md, docs/design/concept.md]
affected_ids: [NGO-021, NGO-026, MOE-012, CON-006, CON-007, OPS-020]
related: [INSP-001, INSP-002, CR-003, CR-006, REQ-SYS-053, REQ-SYS-054, REQ-SYS-116, REQ-SYS-117, REQ-SYS-184, REQ-SYS-187, MOE-006, SI-014]
target_release: none
branch: cr/CR-009-l0-conops-srr-liens
disposition: null
disposition_date: null
relook_trigger: null
relook_by: null
merge_sha: null
date_closed: null
---

# CR-009: Fix the SRR peer review liens of the L0 set, the ConOps and the concept

Template: `docs/templates/change-request.md`. Process: `docs/process/05-configuration-and-data-management.md` §5.1 to §5.3 and `docs/process/02-requirements-and-traceability.md` §10.2 and §10.3. File location: this file, committed on `main` with `Refs: CR-009`. The product changes are prototyped on the branch `cr/CR-009-l0-conops-srr-liens` at commit `9001813` (05 §5.2, Submitted: "Branch ... may be opened for prototyping; nothing merges"). Status: **Submitted**. The independent review of section 6 is required before the owner's disposition (PDR work plan rule C6, lesson L4). Originating work package: WP-PDR-10 of `docs/plan/pdr-work-plan.md` (revision 2), which closes carried items C-009, C-010, C-011 and C-013 to C-017.

## 1. Description of the change

Every change below fixes a Minor finding that the SRR peer review records carry as "Lien: fix before PDR" (`docs/reviews/SRR/checklists/expectations.md`, record INSP-001; `docs/reviews/SRR/checklists/conops-and-concept.md`, record INSP-002). No numeric value, mode, transition, requirement, hazard control or test case changes. The prototype commit `9001813` holds the exact text; the tables below give each before and after.

### 1.1 L0 expectations (`expectations.json`, re-rendered `expectations.md`)

| Entry, field | Finding | Before | After | Class (02 §10.2) |
|---|---|---|---|---|
| NGO-026 `rationale` | INSP-001 finding-12 | "...are adopted as TBR by the same decision (REQ-SYS-116 and REQ-SYS-117 carry them: owner Robin, plan the PDR enclosure analysis, close_by PDR)." | "...are adopted as TBR by the same decision; REQ-SYS-116 and REQ-SYS-117 carry them, and the `tbr` object of each of those requirements holds the one owner, plan and close_by of its TBR (charter section 7)." | II |
| CON-006 `source_ids` | INSP-001 finding-13 | 47CFR97.7, 97.5(c), 97.103(b), 97.115(b), 97.109(b), 97.109(d), 97.203(d), SI-019, SI-030 | The same with SI-014 inserted after 47CFR97.203(d) | II |
| CON-007 `source_ids` | INSP-001 finding-13 | 47CFR97.313(a), 47CFR97.313(b), SI-003 | 47CFR97.313(a), 47CFR97.313(b), SI-014, SI-003 | II |
| NGO-021 `statement` | INSP-001 finding-15 | "a squeeze of both paddle contacts held longer than 2 s stops keying" | "a squeeze of both paddle contacts held longer than 2 s in Iambic A, Iambic B or Ultimatic mode stops keying" | I |
| NGO-021 `rationale` | INSP-001 finding-15 | "...with the 2 s squeeze limit (REQ-SYS-184) in place of..." | "...with the 2 s squeeze limit (REQ-SYS-184, which applies in Iambic A, Iambic B and Ultimatic mode; in Bug mode a squeeze is bounded by the 5 s manual timeout of REQ-SYS-053 and by REQ-SYS-054) in place of..." | II |
| MOE-012 `success_criterion` | INSP-001 finding-15 | "2 s for a squeeze of both paddle contacts; ... and a squeeze within 2 s" | "2 s for a squeeze of both paddle contacts in Iambic A, Iambic B or Ultimatic mode; ... and a squeeze in those modes within 2 s" | I |

The mode scope is the one REQ-SYS-184 already states ("in Iambic A, Iambic B or Ultimatic mode", SRR decision 37), so the L0 text stops overstating the L1 limit; the Bug-mode squeeze stays bounded by REQ-SYS-053 and REQ-SYS-054, which the rationale now says.

INSP-001 finding-16 (carried item C-012: CON-015 and NGO-006 in the CR-003 impact assessment) is not in this CR. Its expected fix is satisfied by CR-003 revision 3 (`d9a215a`) section 1.4, which changes the CON-015 title, statement, rationale and `source_ids` and the NGO-006 statement, rationale and `source_ids` with SI-037 and SI-039; the product change lands with CR-003's implementation (WP-PDR-02).

### 1.2 ConOps (`docs/conops/conops.md`, revision 5)

| Location | Finding | Before | After | Class |
|---|---|---|---|---|
| Section 2.2, hazard row | INSP-002 finding-20 | "`docs/safety/hazards.json` (version 0.3.0-pha), `docs/safety/hazard-analysis.md` \| HZ-001 to HZ-015 and their phases" | "... (checked at version 0.5.0-pha for revision 5; the PDR re-issue supersedes it) \| HZ-001 to HZ-015 at 0.5.0-pha and their phases" | II |
| Section 2.2, risk row | INSP-002 finding-19 | "`docs/risk/register.json` \| RSK-001 to RSK-059" | "... (a Log-class file updated continuously; checked at version 0.6.0-pre-srr for revision 5) \| RSK-001 to RSK-065 at 0.6.0-pre-srr; section 8 cites each entry by id" | II |
| Section 8 lead paragraph | INSP-002 finding-19 | "(`docs/risk/register.json`, RSK-001 to RSK-059)" | "(`docs/risk/register.json`, RSK-001 to RSK-065 at version 0.6.0-pre-srr)" | II |
| Appendix D status header | INSP-002 finding-21 | "Status (2026-09-26, products at commit 400e59d; rows D5, D7, D9, D13, D15, D18 and D19 updated for the SRR rulings of 2026-09-26)" | "Status (re-checked 2026-09-27 against the products at commit `ab2af2d` for revision 5; revision 4 statuses were written on 2026-09-26 against the products at commit `400e59d`, rows D5, D7, D9, D13, D15, D18 and D19 against commit `cd61450` after the SRR rulings)" | II |
| Appendix D statuses re-checked at `ab2af2d` | INSP-002 finding-21 (the header now names a check commit, so the statuses are re-checked there) | D5 "Edited ... closes when ... INSP-003 verifies"; D6, D10 "closes when the INSP-008 reviewer verifies"; D15 "Open: ADR-014 section 2 unchanged"; D18 "closes with item D5" | D5 Closed (INSP-003 post-SRR-ruling delta, decision 37 row; the quoted clear condition corrected to the statement's "until both paddles open"); D6 and D10 Closed for the hazard part (INSP-008 iteration 3); D15 Closed (the ADR-014 erratum line of 2026-09-26 cites OET 65 Supplement B, SRR decision 18); D18 Closed with D5. D9, D11, D12, D13, D14, D17, D19 stay Open, each now naming its PDR work package (WP-PDR-14, 16, 16, 29, 30, 43, and 23 with 32) | II |
| OPS-020 step 5 | INSP-002 finding-25 | "...keys continuous dits at 50 WPM from the Bench-test mode into the dummy load, and measures the spectrum on the tinySA Ultra at its narrowest RBW: every part..." | "...at the 5 W step, the worst case (at full drive the gate-bias envelope and any compression can sharpen the keying edges). The owner keys continuous dits at 50 WPM from the iambic paddle in Transmit-keyed mode into the dummy load through the calibrated attenuator, in bursts with the paddle released between them; if the paddle watchdog ends a burst (REQ-SYS-054), releasing both paddles clears it (Table 3.4-4 row 3). Bench-test mode is not used, because it holds the transmitter at 0.5 W for the whole mode (REQ-SYS-187; SRR package decision 41). The tinySA Ultra at its narrowest RBW holds the maximum over as many bursts as its sweep needs: every part..." (the rest of the step unchanged) | I (a change to an `OPS` scenario, 02 §10.2) |
| Status line; revision history row 5 | Record of this revision | "Draft for SRR (functional baseline candidate), revision 4" | "Functional baseline (`baseline/srr`, revision 4). Revision 5 of 2026-09-27, proposed by CR-009 and not in the baseline until that CR is approved and merged..."; row 5 lists every change | II |

### 1.3 Concept (`docs/design/concept.md`, revision 3)

| Location | Finding | Before | After | Class |
|---|---|---|---|---|
| Section 15 "Feeds" | INSP-002 finding-26 | "performance values in sections 7 and 14 are the proposed L1 values with their sources" | "performance values in sections 7 and 14 are L1 values, each marked as the conventions paragraph states: an owner decision with its `SI-NNN`, a value the owner ruled at SRR on 2026-09-26 with its decision number, or a value still carried as TBR with `close_by` PDR" | II |
| Revision line; revision history row 3 | Record of this revision | "Revision: 2 of 2026-09-26 ..." | Revision 2 named as in `baseline/srr`; revision 3 proposed by CR-009 | II |

## 2. Reason

The SRR records INSP-001 (liens finding-12, 13, 15, 16) and INSP-002 (liens finding-19, 20, 21, 25, 26) carry these Minor findings as "Lien: fix before PDR", due at the PDR readiness declaration (charter section 4 item 3; `docs/reviews/SRR/package.md` section 20.1). The files are in the functional baseline (05 Table 4-1 rows 5, 6 and 52, "CR from" SRR), so a non-editorial fix needs an approved CR (05 §5.1 row 1; 01 §10.5: evidence kind `cr` for "every non-editorial fix to a baselined item, including a lien closed after the gate's baseline tag"). None of the fixes is editorial under 05 §2: they change a statement, a scenario step, `source_ids`, IDs and version numbers. The PDR work plan assigns them to WP-PDR-10 and PDR entrance criterion E-13 (ConOps baselined and consistent) depends on them. Workaround while the CR is open: none needed; the defects are wording and traceability defects with no conflicting value in the baseline (INSP-001 and INSP-002 rate every one Minor).

## 3. Alternatives considered

| Alternative | Why rejected or deferred |
|---|---|
| Do nothing | The nine liens stay open at the PDR readiness declaration; a Minor RID not fixed before the next review breaks charter section 4 item 3 and entrance criterion S2/S3 evidence, and E-13 cannot be shown. |
| Commit the fixes on `main` with an `Editorial:` trailer | Not permitted: 05 §2 says never editorial for a change to a number, an ID or a status; NGO-021, MOE-012 and OPS-020 are Class I fields under 02 §10.2. |
| Fold the fixes into CR-003 or CR-006 | Rejected: both CRs are in their own review and disposition cycle (OD-02, OD-03) and neither is about these liens; mixing them would delay both and blur each CR's verification. The shared files are ordered by the plan section 5.3 writer order instead (section 5 below). |
| Split into a Class I CR (NGO-021, MOE-012, OPS-020) and a Class II CR (the rest) | Rejected: one small change set on four files; one CR, one review and one disposition cost the owner less. The class is the highest of the parts. |
| Quote the REQ-SYS-116 and REQ-SYS-117 `tbr` plan in NGO-026 instead of citing it | Rejected: WP-PDR-11 rewords the L1 `tbr` owner fields and WP-PDR-45 closes the TBRs at PDR; a quote would go stale again, a citation cannot. |
| Put the band-edge acceptance at the 0.5 W Bench-test step | Rejected: the finding's point is that 0.5 W is not the worst case; the 5 W step is. |

## 4. Impact assessment (CM plan §5.3)

| Field | Assessment (numbers, IDs, paths) |
|---|---|
| Performance margins | None: no MOP, TPM or budget value changes. The OPS-020 measurement now covers the 5 W step, which is the case REQ-SYS-015 (26 dB bandwidth at most 350 Hz, Analysis) and MOE-006 bound; no margin changes. |
| Safety | None: no hazard, control or 07 §14.1 component changes. NGO-021 and MOE-012 now state the same mode scope as REQ-SYS-184 and HZ-004 K4; the Bug-mode squeeze is bounded by REQ-SYS-053 (5 s) and REQ-SYS-054, as before. The 5 W band-edge keying is into a dummy load through the attenuator with the paddle watchdog, the 7.5 to 13 s independent cutoff (REQ-SYS-055) and the transmission-length backstop (REQ-SYS-180) active, the same controls as any Transmit-keyed use. Hazard analysis re-issue: no. RF exposure evaluation change: no. |
| Risk | None: no RSK added, closed or re-scored; the ConOps now cites the register range and version it was checked against. |
| Software classification and tailoring | None: no classification, `rmm.json` or compliance-matrix row changes. |
| Interfaces | None: no ICD changes; no external-interface change. |
| Operations and ConOps | OPS-020 step 5 changes the owner's acceptance procedure: the band-edge measurement is keyed from the paddle at the 5 W step in Transmit-keyed mode instead of from Bench-test. This makes the CR Class I (05 §5.3). No mode, transition, operator procedure outside acceptance, operations handbook or maintenance instruction changes (`docs/ops/` does not exist yet). |
| Cybersecurity | None: neither the USB firmware-load path nor the key-input command path changes (07 §16). |
| Verification | No TC invalidated. The closing case of the band-edge clause of MOE-006 is written by the V&V plan and TC-VAL authors at PDR (WP-PDR-43); it takes the OPS-020 step 5 procedure (5 W, paddle, Transmit-keyed, max hold over bursts). REQ-SYS-015 stays closed by Analysis (SRR decision 30). Evidence class unchanged. No decision table or independence-pair test is affected. |
| Cost | None: no BOM, fabrication or instrument change; the calibrated attenuator is already required by MOE-006. |
| Schedule | None on vendors or gates. Order: this CR is dispositioned and merged before WP-PDR-02 implements CR-003 and CR-006 on `expectations.json` and `conops.md` (plan section 5.3 writer order WP-PDR-10, then WP-PDR-02); the §6 review and the disposition are requested for B1a Tue 09-29 (section 7). If the disposition is later than CR-003's, the CR merged second rebases its hunks (CR-003 touches CON-015, CON-026, NGO-006, NGO-007, MOE-013, OPS-012, the ConOps section 4 rows and the section 8 risk cell at line 704, and concept lines 26 to 379; CR-006 touches CON-024, NGO-009, NGO-010, NGO-027, NGO-028, MOE-001, MOE-002, MOE-007 and ConOps lines 41, 369, 427, 455, 528, 849 and 853, all at `39a6b13`; no entry or line in common with this CR except the revision-history tables of the ConOps and the concept, where each CR appends its own row). |
| Requirements and traceability | L1: none added, modified, deleted or retired. L0 Class I: NGO-021 (`statement`), MOE-012 (`success_criterion`); Class II: NGO-021 and NGO-026 (`rationale`), CON-006 and CON-007 (`source_ids`, SI-014 added per 02 §3.2 rule 4). ConOps Class I: OPS-020 step 5. Parents and children: none change; SI-014 already exists. Volatility (02 §10.4, N_start 190 L1 requirements at `baseline/srr`): A = 0, M = 0, R = 0, contribution 0 %. `tools/traceability.py --root <branch worktree>` at `9001813`: exit 0, 245 requirements, 173 test cases, 0 violations, 2 warnings (SYS_UNALLOCATED REQ-SYS-125 and REQ-SYS-148, both present on `main`), no RENDER_STALE. |
| Regulatory | None: 47 CFR 97.307 and 97.3(a)(8) are applied as before; the SI-014 citation in CON-006 and CON-007 adds the stakeholder input that makes Part 97 applicable (02 §3.2 rule 4) and changes no clause. |
| Documentation | With this CR (branch): `expectations.json` and its rendering `expectations.md` (re-rendered by `tools/traceability.py --render`); `conops.md` revision 5; `concept.md` revision 3. After merge: the SRR records INSP-001 and INSP-002 get their delta iterations (plan WP-PDR-10), and the SRR log secretary moves the items (WP-PDR-15). The traceability report on `main` is regenerated at the next Log commit of `docs/vv/`. No VDD or package manifest exists. |
| Released units | None: no unit exists. |

Classification rationale: Class I, because NGO-021's statement, MOE-012's success criterion and an `OPS` scenario step change (02 §10.2 names "any change to an MOE, constraint or NGO statement" and "any change to ... an `OPS` scenario" as Class I), and the OPS-020 change alters an operator acceptance procedure (05 §5.3, Operations and ConOps). The other parts are Class II; the CR takes the higher class. Adapted from the SE HB §6.5.1.2.3 major change.

## 5. Implementation plan

| Step | Artifact and path | Responsible | Done (SHA) |
|---|---|---|---|
| 1 | L0 fixes of section 1.1 in `expectations.json`; `expectations.md` re-rendered | Claude (L0 author, WP-PDR-10) | Prototyped on the branch at `9001813` |
| 2 | ConOps revision 5 (section 1.2) | Claude (ConOps author, WP-PDR-10) | Prototyped on the branch at `9001813` |
| 3 | Concept revision 3 (section 1.3) | Claude (concept author, WP-PDR-10) | Prototyped on the branch at `9001813` |
| 4 | `tools/traceability.py` and `tools/validate_docs.py` on the branch | Claude | Run at `9001813`: traceability exit 0 (0 violations, 2 warnings, no RENDER_STALE); validate_docs 48 of 50, the two failures being the record drift rule on INSP-001 and INSP-002, which name the `baseline/srr` blobs; they clear when the step 6 delta iterations name the frozen blobs below, before the merge; the schema check of `expectations.json` passes |
| 5 | After approval: rebase the branch onto `main` if `main` moved these files, re-render, re-run step 4, merge `--no-ff` with the owner's merge approval | Claude (CM) | |
| 6 | Delta iterations of INSP-001 and INSP-002 verify each finding on the frozen blobs (below) | Independent reviewer (new invocations of `reviewer:expectations` and `reviewer:conops-concept`) | |

Frozen products for review (plan rule C2), at branch commit `9001813`: `docs/requirements/l0-stakeholder/expectations.json@60df49c9767802b7dc7fb1d1b4f73cc758301f98`, `docs/requirements/l0-stakeholder/expectations.md@4de665a1217ed4d0b9347e91a1a74133e5fc4ac3`, `docs/conops/conops.md@8415dba2dc5e753c7bf538c35b524463b0cd656d`, `docs/design/concept.md@ee0d6e92e85c890a27a9f44e090e9d972f2696da`.

Verification of the implementation (what the independent reviewer checks): each before and after of section 1 against the blob; that no other line of the four files changed (`git diff ab2af2d 9001813`); REQ-SYS-184's mode scope against NGO-021 and MOE-012; SI-014 in CON-006 and CON-007 and no other regulatory constraint missing it; that the NGO-026 citation matches the `tbr` objects of REQ-SYS-116 and REQ-SYS-117; each re-checked Appendix D status against the named record or file at `ab2af2d`; OPS-020 step 5 against REQ-SYS-054, REQ-SYS-187, MOE-006 and Table 3.4-4 row 3; `tools/traceability.py` with no RENDER_STALE and no violation naming an L0 id or `OPS-020`; the concept section 5 block unchanged (the render `docs/reviews/SRR/figures/concept-block-diagram.png` stays current).

## 6. Independent review of the impact assessment

Required (Class I). Not yet performed. The review is requested before the owner's disposition (plan rule C6).

| Item | Reviewer (agent invocation) | Date | Finding | Resolution |
|---|---|---|---|---|
| Pending | | | | |

Reviewer concurrence: pending.

## 7. CCB disposition (owner)

Not dispositioned. Requested at owner session B1a (Tue 09-29), after the section 6 review, so that the branch merges before WP-PDR-02 implements CR-003 and CR-006 on the same files. Questions for the owner are in section 12.

| Field | Value |
|---|---|
| Decision | |
| Class confirmed | |
| Date | |
| Conditions | |
| Rationale | |
| Waiver scope (if Approved (waiver)) | n/a |
| Re-look trigger and re-look-by review (if Deferred) | |
| Source | |

Disposition history (append only):

| Date | Decision | New target | Source |
|---|---|---|---|
| | | | |

## 8. Implementation record

Not yet implemented (the branch holds a prototype only).

| Commit | Files | Trailer check (`CR: CR-009` present) |
|---|---|---|
| `9001813` (prototype, branch `cr/CR-009-l0-conops-srr-liens`) | `expectations.json`, `expectations.md`, `conops.md`, `concept.md` | Present |

Traceability report after implementation: to be regenerated at merge; renders regenerated: `docs/requirements/l0-stakeholder/expectations.md`.

## 9. Verification of implementation

| Impact item | Planned closure (from §4/§5) | Evidence (report path, TC id, analysis file) | Result |
|---|---|---|---|
| | | | |

Independent verifier (agent invocation): pending.

## 10. Closure

| Field | Value |
|---|---|
| Owner merge approval | |
| Merge commit | |
| Waiver entered in CSA item 12 and affected VDDs | n/a |
| CSA regenerated | |
| Date closed | |

## 11. History

| Date | State | By | Commit on main | Note |
|---|---|---|---|---|
| 2026-09-27 | Draft, then Submitted | Claude (WP-PDR-10 author) | `1f7d138` | Created with the impact assessment complete; product prototype on the branch at `9001813` |
| 2026-09-27 | Submitted | Claude (WP-PDR-10 author) | this file's commit | Prototype commit message corrected (validate_docs result) by amending the unpushed branch commit `f511e02` to `9001813`; the four product blobs are unchanged; section 5 step 4 corrected to the post-commit validate_docs result |

## 12. Questions for the owner (answer with the disposition)

1. Approve CR-009 as Class I? Recommendation: approve.
2. OPS-020 step 5: accept the band-edge acceptance at the 5 W step, keyed from the paddle in Transmit-keyed mode with the tinySA holding the maximum over bursts? Recommendation: accept; the 5 W step is the worst case for the keying sidebands, and Bench-test cannot reach it (REQ-SYS-187).
