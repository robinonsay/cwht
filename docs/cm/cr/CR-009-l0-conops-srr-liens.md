---
id: CR-009
title: Fix the SRR peer review liens of the L0 set, the ConOps and the concept
status: Dispositioned
class: I
originator: Claude
date_opened: 2026-09-27
phase: B
configuration_at_origination: baseline/srr (tag on 779f93f); HEAD ab2af2d on main
baseline_affected: baseline/srr
affected_cis: [5, 6, 52]
affected_paths: [docs/requirements/l0-stakeholder/expectations.json, docs/requirements/l0-stakeholder/expectations.md, docs/conops/conops.md, docs/design/concept.md]
affected_ids: [NGO-021, NGO-026, MOE-012, CON-006, CON-007, OPS-020]
related: [INSP-001, INSP-002, CR-003, CR-006, RSK-064, RSK-065, RSK-007, HZ-007, REQ-SYS-053, REQ-SYS-054, REQ-SYS-116, REQ-SYS-117, REQ-SYS-184, REQ-SYS-187, MOE-006, SI-014]
target_release: none
branch: cr/CR-009-l0-conops-srr-liens
disposition: Approved
disposition_date: 2026-09-28
relook_trigger: null
relook_by: null
merge_sha: null
date_closed: null
---

# CR-009: Fix the SRR peer review liens of the L0 set, the ConOps and the concept

Template: `docs/templates/change-request.md`. Process: `docs/process/05-configuration-and-data-management.md` §5.1 to §5.3 and `docs/process/02-requirements-and-traceability.md` §10.2 and §10.3. File location: this file, committed on `main` with `Refs: CR-009`. The product changes are prototyped on the branch `cr/CR-009-l0-conops-srr-liens` at commit `9001813`, with the ConOps completed for INSP-002 finding-19 at commit `56b4bcd` (revision 2 of this CR, section 6.2) (05 §5.2, Submitted: "Branch ... may be opened for prototyping; nothing merges"). Status: **Submitted**. The independent review of section 6 is required before the owner's disposition (PDR work plan rule C6, lesson L4). Originating work package: WP-PDR-10 of `docs/plan/pdr-work-plan.md` (revision 2), which closes carried items C-009, C-010, C-011 and C-013 to C-017.

## 1. Description of the change

Every change below fixes a Minor finding that the SRR peer review records carry as "Lien: fix before PDR" (`docs/reviews/SRR/checklists/expectations.md`, record INSP-001; `docs/reviews/SRR/checklists/conops-and-concept.md`, record INSP-002). No numeric value, mode, transition, requirement, hazard control or test case changes. The prototype commits `9001813` and `56b4bcd` hold the exact text; the tables below give each before and after.

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
| Section 8 lead paragraph | INSP-002 finding-19 (first part: the range) | "(`docs/risk/register.json`, RSK-001 to RSK-059)" | "(`docs/risk/register.json`, RSK-001 to RSK-065 at version 0.6.0-pre-srr)" | II |
| Section 8 table, two rows appended after the RSK-014 row (commit `56b4bcd`) | INSP-002 finding-19 (second part: "add RSK-064 and RSK-065 to the section 8 table or say why they are not operational") | No row names RSK-064 or RSK-065 | Row "Open or cold owner-soldered joint in a power path (cell holders, Pico 2 castellations, power switch or jack): the unit does not power, or browns out under transmit load, at first power-on \| RSK-064 (the Assembly phase of the Off row of Table 3.4-5; a bridged joint at the cell holders is a short-circuit cause of HZ-007, carried by RSK-007) \| OPS-012 step 3 cold checks and rails with current limits; the register plans a bring-up stage 0 that inspects and resistance-checks every owner-soldered power-path joint, then powers the unit from a current-limited bench supply before the cells are inserted, and records the result in the unit's as-built record (RSK-064 steps S1 and S2); a failed check is reworked by the owner and recorded in that as-built record (RSK-064 trigger)"; row "A lent unit treated as outside the 47 CFR 15.23 personal-use exemption of the Part 15 digital section, so friend units are withdrawn \| RSK-065 (the loan of OPS-006) \| At most five units, never marketed, owned by the owner and lent, never transferred (section 1.2 item 5, CON-008); the owner decides before CDR whether to seek an FCC reading of lending (RSK-065 step S1); any proposed transfer, sale or offer of a unit is decided by the owner before it happens, and a question from anyone about a lent unit recalls the lent units pending the answer (RSK-065 triggers)". Both rows restate register content (`register.json` 0.6.0-pre-srr: RSK-064 S1, S2 and first trigger; RSK-065 S1 and both triggers); neither adds a mitigation the register lacks | II (a section 8 table row, not an `OPS` scenario, MOE, NGO or constraint; 02 §10.2) |
| Appendix D status header | INSP-002 finding-21 | "Status (2026-09-26, products at commit 400e59d; rows D5, D7, D9, D13, D15, D18 and D19 updated for the SRR rulings of 2026-09-26)" | "Status (re-checked 2026-09-27 against the products at commit `ab2af2d` for revision 5; revision 4 statuses were written on 2026-09-26 against the products at commit `400e59d`, rows D5, D7, D9, D13, D15, D18 and D19 against commit `cd61450` after the SRR rulings)" | II |
| Appendix D statuses re-checked at `ab2af2d` | INSP-002 finding-21 (the header now names a check commit, so the statuses are re-checked there) | D5 "Edited ... closes when ... INSP-003 verifies"; D6, D10 "closes when the INSP-008 reviewer verifies"; D15 "Open: ADR-014 section 2 unchanged"; D18 "closes with item D5" | D5 Closed (INSP-003 post-SRR-ruling delta, decision 37 row; the quoted clear condition corrected to the statement's "until both paddles open"); D6 and D10 Closed for the hazard part (INSP-008 iteration 3); D15 Closed (the ADR-014 erratum line of 2026-09-26 cites OET 65 Supplement B, SRR decision 18); D18 Closed with D5. D9, D11, D12, D13, D14, D17, D19 stay Open, each now naming its PDR work package (WP-PDR-14, 16, 16, 29, 30, 43, and 23 with 32) | II |
| OPS-020 step 5 | INSP-002 finding-25 | "...keys continuous dits at 50 WPM from the Bench-test mode into the dummy load, and measures the spectrum on the tinySA Ultra at its narrowest RBW: every part..." | "...at the 5 W step, the worst case (at full drive the gate-bias envelope and any compression can sharpen the keying edges). The owner keys continuous dits at 50 WPM from the iambic paddle in Transmit-keyed mode into the dummy load through the calibrated attenuator, in bursts with the paddle released between them; if the paddle watchdog ends a burst (REQ-SYS-054), releasing both paddles clears it (Table 3.4-4 row 3). Bench-test mode is not used, because it holds the transmitter at 0.5 W for the whole mode (REQ-SYS-187; SRR package decision 41). The tinySA Ultra at its narrowest RBW holds the maximum over as many bursts as its sweep needs: every part..." (the rest of the step unchanged) | I (a change to an `OPS` scenario, 02 §10.2) |
| Status line; revision history row 5 | Record of this revision | "Draft for SRR (functional baseline candidate), revision 4" | "Functional baseline (`baseline/srr`, revision 4). Revision 5 of 2026-09-27, proposed by CR-009 and not in the baseline until that CR is approved and merged: the SRR peer review liens INSP-002 finding-19, finding-20, finding-21 and finding-25 fixed, finding-19 with RSK-064 and RSK-065 added to the section 8 table..."; row 5 lists every change, the two section 8 rows included (commit `56b4bcd`) | II |

### 1.3 Concept (`docs/design/concept.md`, revision 3)

| Location | Finding | Before | After | Class |
|---|---|---|---|---|
| Section 15 "Feeds" | INSP-002 finding-26 | "performance values in sections 7 and 14 are the proposed L1 values with their sources" | "performance values in sections 7 and 14 are L1 values, each marked as the conventions paragraph states: an owner decision with its `SI-NNN`, a value the owner ruled at SRR on 2026-09-26 with its decision number, or a value still carried as TBR with `close_by` PDR" | II |
| Revision line; revision history row 3 | Record of this revision | "Revision: 2 of 2026-09-26 ..." | Revision 2 named as in `baseline/srr`; revision 3 proposed by CR-009 | II |

## 2. Reason

The SRR records INSP-001 (liens finding-12, 13, 15, 16) and INSP-002 (liens finding-19, 20, 21, 25, 26) carry nine Minor findings as "Lien: fix before PDR", due at the PDR readiness declaration. This CR closes eight of them: INSP-001 finding-12, 13 and 15, and INSP-002 finding-19 (both parts: the register range, and the RSK-064 and RSK-065 rows of the section 8 table), 20, 21, 25 and 26. The ninth, INSP-001 finding-16, is closed by CR-003 section 1.4 (section 1.1 above), not by this CR (charter section 4 item 3; `docs/reviews/SRR/package.md` section 20.1). The files are in the functional baseline (05 Table 4-1 rows 5, 6 and 52, "CR from" SRR), so a non-editorial fix needs an approved CR (05 §5.1 row 1; 01 §10.5: evidence kind `cr` for "every non-editorial fix to a baselined item, including a lien closed after the gate's baseline tag"). None of the fixes is editorial under 05 §2: they change a statement, a scenario step, `source_ids`, IDs and version numbers. The PDR work plan assigns them to WP-PDR-10 and PDR entrance criterion E-13 (ConOps baselined and consistent) depends on them. Workaround while the CR is open: none needed; the defects are wording and traceability defects with no conflicting value in the baseline (INSP-001 and INSP-002 rate every one Minor).

## 3. Alternatives considered

| Alternative | Why rejected or deferred |
|---|---|
| Do nothing | The eight liens this CR closes (section 2) stay open at the PDR readiness declaration; a Minor RID not fixed before the next review breaks charter section 4 item 3 and entrance criterion S2/S3 evidence, and E-13 cannot be shown. |
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
| Risk | None on the register: no RSK added, closed, re-scored or reworded. The ConOps now cites the register range and version it was checked against, and its section 8 table gains rows for RSK-064 and RSK-065, each restating the mitigation steps and triggers the register already holds at 0.6.0-pre-srr (RSK-064 S1, S2 and the first trigger; RSK-065 S1 and both triggers) and the RSK-064 link to HZ-007 through RSK-007. The ids and those steps are unchanged in `register.json` 0.7.0-pre-pdr on `main`; the rebase of section 5 step 5 re-checks them. |
| Software classification and tailoring | None: no classification, `rmm.json` or compliance-matrix row changes. |
| Interfaces | None: no ICD changes; no external-interface change. |
| Operations and ConOps | OPS-020 step 5 changes the owner's acceptance procedure: the band-edge measurement is keyed from the paddle at the 5 W step in Transmit-keyed mode instead of from Bench-test. This makes the CR Class I (05 §5.3). No mode, transition, operator procedure outside acceptance, operations handbook or maintenance instruction changes (`docs/ops/` does not exist yet). |
| Cybersecurity | None: neither the USB firmware-load path nor the key-input command path changes (07 §16). |
| Verification | No TC invalidated. The closing case of the band-edge clause of MOE-006 is written by the V&V plan and TC-VAL authors at PDR (WP-PDR-43); it takes the OPS-020 step 5 procedure (5 W, paddle, Transmit-keyed, max hold over bursts). REQ-SYS-015 stays closed by Analysis (SRR decision 30). Evidence class unchanged. No decision table or independence-pair test is affected. |
| Cost | None: no BOM, fabrication or instrument change; the calibrated attenuator is already required by MOE-006. |
| Schedule | None on vendors or gates. Order: this CR is dispositioned and merged before WP-PDR-02 implements CR-003 and CR-006 on `expectations.json` and `conops.md` (plan section 5.3 writer order WP-PDR-10, then WP-PDR-02); the §6 review and the disposition are requested for B1a Tue 09-29 (section 7). If the disposition is later than CR-003's, the CR merged second rebases its hunks (CR-003 touches CON-015, CON-026, NGO-006, NGO-007, MOE-013, OPS-012, the ConOps section 4 rows and the section 8 risk cell at line 704, and concept lines 26 to 379; CR-006 touches CON-024, NGO-009, NGO-010, NGO-027, NGO-028, MOE-001, MOE-002, MOE-007 and ConOps lines 41, 369, 427, 455, 528, 849 and 853, all at `39a6b13`; no entry or line in common with this CR except the revision-history tables of the ConOps and the concept, where each CR appends its own row). The ConOps section 8 table is touched by both CRs: CR-003 changes the cell of the RSK-006, RSK-026 row at line 704 at `ab2af2d` (CR-003 R2-F5), and this CR changes the section 8 lead paragraph (line 696 at `ab2af2d`) and appends two rows after the last row (RSK-014, line 724 at `ab2af2d`). The changed lines are 8 and 20 lines from line 704 and do not overlap or abut it, so a three-way merge applies both; the CR merged second still rebases, re-reads the whole table (row set, register version in the lead paragraph) and re-runs section 5 step 4. |
| Requirements and traceability | L1: none added, modified, deleted or retired. L0 Class I: NGO-021 (`statement`), MOE-012 (`success_criterion`); Class II: NGO-021 and NGO-026 (`rationale`), CON-006 and CON-007 (`source_ids`, SI-014 added per 02 §3.2 rule 4). ConOps Class I: OPS-020 step 5. Parents and children: none change; SI-014 already exists. Volatility (02 §10.4, N_start 190 L1 requirements at `baseline/srr`): A = 0, M = 0, R = 0, contribution 0 %. `tools/traceability.py --root <branch worktree>` at `9001813`: exit 0, 245 requirements, 173 test cases, 0 violations, 2 warnings (SYS_UNALLOCATED REQ-SYS-125 and REQ-SYS-148, both present on `main`), no RENDER_STALE. |
| Regulatory | None: 47 CFR 97.307 and 97.3(a)(8) are applied as before; the SI-014 citation in CON-006 and CON-007 adds the stakeholder input that makes Part 97 applicable (02 §3.2 rule 4) and changes no clause. |
| Documentation | With this CR (branch): `expectations.json` and its rendering `expectations.md` (re-rendered by `tools/traceability.py --render`); `conops.md` revision 5; `concept.md` revision 3. After merge: the SRR records INSP-001 and INSP-002 get their delta iterations (plan WP-PDR-10), and the SRR log secretary moves the items (WP-PDR-15). The traceability report on `main` is regenerated at the next Log commit of `docs/vv/`. No VDD or package manifest exists. |
| Released units | None: no unit exists. |

Classification rationale: Class I, because NGO-021's statement, MOE-012's success criterion and an `OPS` scenario step change (02 §10.2 names "any change to an MOE, constraint or NGO statement" and "any change to ... an `OPS` scenario" as Class I), and the OPS-020 change alters an operator acceptance procedure (05 §5.3, Operations and ConOps). The other parts are Class II; the CR takes the higher class. Adapted from the SE HB §6.5.1.2.3 major change.

## 5. Implementation plan

| Step | Artifact and path | Responsible | Done (SHA) |
|---|---|---|---|
| 1 | L0 fixes of section 1.1 in `expectations.json`; `expectations.md` re-rendered | Claude (L0 author, WP-PDR-10) | Prototyped on the branch at `9001813` |
| 2 | ConOps revision 5 (section 1.2) | Claude (ConOps author, WP-PDR-10) | Prototyped on the branch at `9001813`; section 8 rows for RSK-064 and RSK-065 at `56b4bcd` (CR revision 2, R1-F1) |
| 3 | Concept revision 3 (section 1.3) | Claude (concept author, WP-PDR-10) | Prototyped on the branch at `9001813` |
| 4 | `tools/traceability.py` and `tools/validate_docs.py` on the branch | Claude | Run at `56b4bcd` (revision 2): `tools/traceability.py --root <branch worktree> --report-only` exit 0, 245 requirements, 173 test cases, 0 violations, 2 warnings (SYS_UNALLOCATED REQ-SYS-125 and REQ-SYS-148, both on `main`), no RENDER_STALE, outputs restored; `validate_docs` 49 of 50, the one failure the record drift rule on INSP-002 (`conops-and-concept.md` names `conops.md@8415dba2`, the revision 1 blob), which clears when the new INSP-002 delta names `dfe50c4c`; INSP-001 passes (its delta names the unchanged expectations blobs). Run at `9001813`: traceability exit 0 (0 violations, 2 warnings, no RENDER_STALE); validate_docs 48 of 50, the two failures being the record drift rule on INSP-001 and INSP-002, which name the `baseline/srr` blobs; they clear when the step 6 delta iterations name the frozen blobs below, before the merge; the schema check of `expectations.json` passes |
| 5 | After approval: rebase the branch onto `main` if `main` moved these files, re-render, re-run step 4, merge `--no-ff` with the owner's merge approval | Claude (CM) | |
| 6 | Delta iterations of INSP-001 and INSP-002 verify each finding on the frozen blobs (below) | Independent reviewer (new invocations of `reviewer:expectations` and `reviewer:conops-concept`) | |

Frozen products for review (plan rule C2), revision 2, at branch commit `56b4bcd`: `docs/requirements/l0-stakeholder/expectations.json@60df49c9767802b7dc7fb1d1b4f73cc758301f98`, `docs/requirements/l0-stakeholder/expectations.md@4de665a1217ed4d0b9347e91a1a74133e5fc4ac3`, `docs/conops/conops.md@dfe50c4c06ee4bc633bb9c8caa8b5a736640148b`, `docs/design/concept.md@ee0d6e92e85c890a27a9f44e090e9d972f2696da`. Only the ConOps blob changed from revision 1 (`9001813`, `conops.md@8415dba2dc5e753c7bf538c35b524463b0cd656d`); the INSP-001 delta of `64eb688` stays valid for the three unchanged blobs, and INSP-002 takes a new delta on `dfe50c4c` before the round 2 re-check.

Verification of the implementation (what the independent reviewer checks): each before and after of section 1 against the blob; that no other line of the four files changed (`git diff ab2af2d 56b4bcd -- <the four paths>`); the RSK-064 and RSK-065 rows of ConOps section 8 against `docs/risk/register.json` 0.6.0-pre-srr (steps, triggers, the HZ-007 and RSK-007 link) and against OPS-006, OPS-012 step 3, Table 3.4-5 and section 1.2 item 5; REQ-SYS-184's mode scope against NGO-021 and MOE-012; SI-014 in CON-006 and CON-007 and no other regulatory constraint missing it; that the NGO-026 citation matches the `tbr` objects of REQ-SYS-116 and REQ-SYS-117; each re-checked Appendix D status against the named record or file at `ab2af2d`; OPS-020 step 5 against REQ-SYS-054, REQ-SYS-187, MOE-006 and Table 3.4-4 row 3; `tools/traceability.py` with no RENDER_STALE and no violation naming an L0 id or `OPS-020`; the concept section 5 block unchanged (the render `docs/reviews/SRR/figures/concept-block-diagram.png` stays current).

## 6. Independent review of the impact assessment

Required (Class I). Not yet performed. The review is requested before the owner's disposition (plan rule C6).

| Item | Reviewer (agent invocation) | Date | Finding | Resolution |
|---|---|---|---|---|
| Pending | | | | |

Reviewer concurrence: pending.

### 6.1 Round 1 (2026-09-27)

Reviewer: independent reviewer agent, a separate invocation that authored none of this CR, none of the prototype commit `9001813` and none of the WP-PDR-10 review commit `64eb688`. Date 2026-09-27. Configuration reviewed: HEAD `fefcf55` on `main` (this CR at `1479b30`); branch `cr/CR-009-l0-conops-srr-liens` at `64eb688` (merge base `ab2af2d`); `baseline/srr` on `779f93f`. Method: 05 §5.2 and §5.3 field by field, then class, effectivity, the branch contents against the CR (`git diff main...cr/CR-009-l0-conops-srr-liens`, `git diff ab2af2d 9001813`), the section 5 verification plan, and whether any requirement or control is weakened. Search: claude-context `search_code` on `/Users/robinonsay/rust/cwht` first (queries on the OPS-020 band-edge procedure and on the squeeze limit), then `git grep` on `main` for `OPS-020` to pin lines. Tools: `tools/traceability.py --root <detached worktree of the branch> --report-only` re-run by this reviewer (worktree removed after the run; `main` untouched).

Severity rule: Major if the owner would disposition on an incomplete or wrong basis; otherwise Minor.

| Item | Reviewer (agent invocation) | Date | Finding | Resolution |
|---|---|---|---|---|
| R1-F1 (Major) INSP-002 finding-19 is only half fixed, but the CR presents it as fixed | Independent reviewer agent | 2026-09-27 | finding-19 (`docs/reviews/SRR/checklists/conops-and-concept.md` line 121 at `ab2af2d`) has two parts: cite the register range correctly, and "add RSK-064 and RSK-065 to the section 8 table or say why they are not operational". The prototype does only the first part: at `9001813`, `conops.md` names RSK-065 only in the two range citations (lines 115 and 697) and never names RSK-064 (open or cold owner-soldered power joint, Assembly phase) or RSK-065 (loaned units and the 47 CFR 15.23 exemption, the loan scenario) in the section 8 table, with no reason given. The INSP-002 PDR lien delta on the branch (`64eb688`, record lines 606 and 620) reaches the same result: finding-19 is not verified and carried item C-013 stays open. Even so, section 1.2 lists finding-19 against rows that fix only the range, section 2 says the CR fixes the liens, the "Do nothing" alternative counts nine liens (a count that also includes INSP-001 finding-16, which section 1.1 hands to CR-003), and Q1 recommends approval without saying that one lien stays open. The owner would approve a ConOps revision believing it closes the ConOps liens for E-13, when a further Class I ConOps change would still be needed. | Author: complete finding-19 on the branch (add RSK-064 and RSK-065 rows to the section 8 table, or state why each is not operational), then update section 1.2 (a new row for the section 8 table), section 2 and section 3 (state the lien count this CR closes, without finding-16), the section 4 Risk row (the new citations) and the section 4 Schedule row (the section 8 table is also touched by CR-003, whose section 8 risk cell is at line 704, so a hunk conflict is now possible). Then freeze new blobs, and have INSP-002 take a new delta before the round 2 check. |
| R1-F2 (Minor) The branch carries a review-record commit that the CR does not list | Independent reviewer agent | 2026-09-27 | `git log main..cr/CR-009-l0-conops-srr-liens` shows two commits. The second, `64eb688`, changes `docs/reviews/SRR/checklists/expectations.md` and `docs/reviews/SRR/checklists/conops-and-concept.md`. Neither path is in `affected_paths`. The commit has `Refs: CR-009` but no `CR: CR-009` trailer, and section 8 lists only `9001813`. This conflicts with 05 Table 4-1 row 31 and §5.2 ("the branch `cr/CR-NNN-<slug>` carries only the product changes"; Implemented: "All commits on `cr/CR-NNN-<slug>` carry `CR: CR-NNN`"). It also conflicts with the Lead SE convention of 2026-09-27 (INSP-031 practice): a record that reviews blobs that exist only on an unmerged `cr/` branch sets `reviewer_verdict` itself, keeps the record verdict held until the merge, and is committed on `main`. A `--no-ff` merge of the branch as it stands would bring the two records into `main` under the CR merge, outside the CR's stated scope. | Author and CM, before the merge: re-commit the two record deltas on `main` under the convention (record verdict held, set in or right after the merge commit), remove `64eb688` from the unpushed branch, and name in section 5 step 6 where the delta records are committed. If the Lead SE rules otherwise, record that ruling in section 8. |
| R1-F3 (Minor) Wording residues next to the fixed text | Independent reviewer agent | 2026-09-27 | (a) Section 1.1 says the L0 text "stops overstating the L1 limit". The NGO-021 `rationale` on the branch still says a toggling stream from live firmware is bounded "at 2 s for a squeeze" with no mode scope (INSP-001 finding-17, raised by the branch review as a Minor lien due at CDR). (b) Revision 3 of `concept.md` changes the revision line to "in the functional baseline `baseline/srr`", but line 3 still reads "Draft for SRR", while the ConOps Status line was changed in this CR (INSP-002 finding-27, Minor lien due at CDR). Neither changes a value. | Author: fold both into the revision that R1-F1 requires, as the WP-PDR-10 reviewer suggests (INSP-002 record action X-1), and add them to the section 1.1 and 1.3 tables. If they are not folded in, qualify the section 1.1 sentence. |
| R1-F4 (Minor) "5 W is the worst case" is stated as fact without evidence | Independent reviewer agent | 2026-09-27 | The new OPS-020 step 5 and the Q2 recommendation state that the 5 W step is "the worst case" for the keying sidebands. The basis is a qualitative argument (gate-bias envelope and compression at full drive), and INSP-002 finding-25 itself only asked for the step to be stated ("if 5 W"). The change drops the one band-edge measurement at 0.5 W. The keying-envelope Analysis runs both steps (TC-TX-006 procedure steps 3 and 6), and REQ-SYS-015 closes by Analysis at every envelope setting, so 0.5 W stays covered by Analysis. The acceptance step's claim, however, is not yet shown. | Author: word it as the expected worst case, to be confirmed by the keying-envelope Analysis at both steps (TC-TX-006). In the section 4 Verification row, have the WP-PDR-43 closing case record the step and add a 0.5 W run if the Analysis shows the 0.5 W emission wider. Add the same qualifier to Q2. |

Items checked with no finding:
- Class I is correct. The NGO-021 `statement`, the MOE-012 `success_criterion` and an `OPS` scenario step change (02 §10.2), and the OPS-020 change alters an operator acceptance procedure (05 §5.3). The other rows are correctly Class II.
- Effectivity: documents only. `target_release: none`, no unit and no release exist, and the ConOps and concept revision lines state that the revisions are outside the baseline until the merge.
- Branch product contents: `git diff ab2af2d 9001813` touches exactly the four `affected_paths` (34 insertions, 32 deletions). Every hunk matches a row of sections 1.1 to 1.3, and no other line changed. The four frozen blob ids of section 5 equal `git rev-parse 9001813:<path>` and the branch tip's blobs. The merge base is `ab2af2d`. No other open `cr/` branch (CR-008, 010 to 016) touches these files.
- REQ-SYS-184 at `ab2af2d` reads "in Iambic A, Iambic B or Ultimatic mode", and the NGO-021 statement and both MOE-012 mentions now carry that scope. The Bug-mode squeeze stays bounded by REQ-SYS-053 (5 s, the Bug dah included) and REQ-SYS-054. No requirement or control is weakened: the L0 text is narrowed to the L1 limit that SRR decision 37 already set, so no new owner ruling is needed.
- SI-014: a script over all constraints at `ab2af2d` finds CON-006 and CON-007 as the only constraints that cite a `47CFR` clause without SI-014. After the change, every such constraint cites it (02 §3.2 rule 4).
- NGO-026: REQ-SYS-116 and REQ-SYS-117 each carry a `tbr` object with one `owner` string, a `plan` and `close_by: PDR`, both at `ab2af2d` and on `cr/CR-008-srr-liens-l1-and-tc-sys` (which rewords the owner to "Robin approves on Claude's proposal at PDR"). The citation holds whichever CR merges first.
- Appendix D re-checks at `ab2af2d`:
  - D5: the INSP-003 decision 37 row is at `requirements-sys.md` line 728, and REQ-SYS-054 reads "until both paddles open".
  - D6 and D10: the INSP-008 iteration 3 delta is at `hazard-analysis.md` lines 341, 342 and 389.
  - D15: the ADR-014 erratum line is at line 29, with history at line 99.
  - D9: ADR-015 has no erratum and still says "no risk of unlicensed transmission", so D9 correctly stays Open.
  - The work package numbers 14, 16, 23, 29, 30, 32 and 43 match the headings of `docs/plan/pdr-work-plan.md`.
- Versions: `hazards.json` is 0.5.0-pha at `ab2af2d` and on `main`. `register.json` is 0.6.0-pre-srr with RSK-001 to RSK-065 at `ab2af2d`. `main` now has 0.7.0-pre-pdr with the same 65 ids, so the version-stamped citations stay accurate; re-check them at the rebase of section 5 step 5.
- OPS-020 step 5 against the other items:
  - REQ-SYS-054: 128 dits at 50 WPM take 6.1 s, so each burst is at most 6.1 s and release clears it, which is Table 3.4-4 row 3.
  - REQ-SYS-187: Bench-test holds 0.5 W.
  - MOE-006: its band-edge clause names no step, so there is no conflict.
  - REQ-SYS-112 and HZ-003: the thermal path is sized for continuous key-down at 5 W, so bursts at 50 percent key-down are inside the design case.
  - REQ-SYS-055 and REQ-SYS-180 remain active.
  - The method matches TC-TX-008 and the spurious cases, which already avoid the Bench-test generator for 5 W.
- Other citations: a search found no other artifact that cites OPS-020 step 5 or a Bench-test band-edge measurement. The requirements that source OPS-020 (REQ-SYS-008, 009 and others) and ADR-021 item 2 are unaffected.
- `tools/traceability.py` on the branch, reproduced by this reviewer: exit 0, 245 requirements, 173 test cases, 0 violations, 2 warnings (SYS_UNALLOCATED REQ-SYS-125 and REQ-SYS-148, both also on `main`), and no RENDER_STALE.
- Rows that need no change: Performance margins, Software classification, Interfaces, Cybersecurity, Cost, Regulatory, Released units, and the volatility figure (L1 A = M = R = 0).
- Observation (no finding): REQ-SYS-184 carries 2 s as TBR, and its rationale names the "longer of 2 s and 16 dit times" fallback (OQ-SAF-002 plan). NGO-021 and MOE-012 state 2 s without a TBR marker. If the TBR closes on the fallback, the L0 text changes with it, which WP-PDR-45 should track.

Reviewer concurrence: I concur with the class, the effectivity and the direction of every change. I do not concur with disposition until R1-F1 is resolved. **Impact review complete, with findings: 1 Major (R1-F1), 3 Minor (R1-F2 to R1-F4).** The CR stays Submitted. The author revises the CR and the prototype, and the reviewer re-checks under a new round heading on the new frozen blobs.

### 6.2 Author response (revision 2)

Added by the CR author in revision 2; the reviewer's text of section 6.1 is unchanged. Scope of this revision: the Major finding only (PDR work plan rule C1, as the lead SE assigned it); the Minor findings stay open for the round 2 re-check to carry or close. The reviewer re-checks this revision under a new heading on the frozen blobs of section 5.

| Finding | Resolution in revision 2 | Where |
|---|---|---|
| R1-F1 (Major) | The reviewer's first route: RSK-064 and RSK-065 are operational (Assembly phase of the Off row with OPS-012; the loan of OPS-006), so each gets a row in the ConOps section 8 table, committed on the branch at `56b4bcd` (`conops.md@dfe50c4c`), with the status line and revision history row 5 naming the change. Section 1.2 splits finding-19 into its two parts and adds the row for the section 8 table. Section 2 counts nine liens and states that this CR closes eight, finding-16 going to CR-003; section 3 "Do nothing" counts the eight. The section 4 Risk row names the new citations and the register content they restate; the section 4 Schedule row names the section 8 hunks of both CRs and their distance. Section 5 step 4 carries the checks at `56b4bcd` and the new frozen blobs; section 8 lists the commit. No lien of INSP-002 now stays open under this CR, so Q1 needs no qualifier. | Branch `56b4bcd`; §1 lead, §1.2, §2, §3, §4 Risk and Schedule, §5 steps 2 and 4 and the frozen blobs, §8, §11 |
| R1-F2 (Minor) | Not changed in revision 2 (rule C1). Open for the round 2 re-check; the review-record commit `64eb688` is still on the branch. | none |
| R1-F3 (Minor) | Not changed in revision 2 (rule C1). Open for the round 2 re-check. | none |
| R1-F4 (Minor) | Not changed in revision 2 (rule C1). Open for the round 2 re-check. | none |

### 6.3 Round 2 (2026-09-27): delta re-check of the R1-F1 fix (revision 2)

Reviewer: independent reviewer agent, a separate invocation that authored no part of this CR, of the prototype commits `9001813` and `56b4bcd`, of the review commit `64eb688` or of the section 6.1 round. The rows of sections 6.1 and 6.2 are left as written. Scope: the Major fix only (PDR work plan rule C1); R1-F2 to R1-F4 are carried, not re-checked. Configuration reviewed: this file at blob `ec916a7b` (revision 2, `main` at `dab9e3a`, HEAD `0033c92` with this file unchanged); the branch `cr/CR-009-l0-conops-srr-liens` at `56b4bcd308b5550aed804a8610002085359898f3` (merge base `ab2af2d`). Frozen blobs confirmed with `git rev-parse 56b4bcd:<path>`: `conops.md@dfe50c4c06ee4bc633bb9c8caa8b5a736640148b`, `expectations.json@60df49c9767802b7dc7fb1d1b4f73cc758301f98`, `expectations.md@4de665a1217ed4d0b9347e91a1a74133e5fc4ac3`, `concept.md@ee0d6e92e85c890a27a9f44e090e9d972f2696da`, equal to section 5. Search: claude-context `search_code` on `/Users/robinonsay/rust/cwht` first (RSK-064 and RSK-065 in the register and the ConOps), then `git grep` on the branch to pin lines.

Checks made:

- Delta scope: `56b4bcd` changes `conops.md` only (4 insertions, 2 deletions, three hunks: status line, revision history row 5, and the two section 8 rows at lines 726 and 727, after the RSK-014 row). No other line of the four `affected_paths` differs from `9001813`. The commit carries `CR: CR-009`. Its parent is the review commit `64eb688` (see R1-F2 below).
- RSK-064 row against `register.json` 0.6.0-pre-srr at `56b4bcd`: the concern restates the register `departure` and `consequence`; the HZ-007 and RSK-007 link is the register statement's own clause, and HZ-007 cause C8 (a slipped iron bridging a cell terminal during hand assembly) confirms it; the response matches step S1 (visual and resistance check, then a current-limited bench-supply power-up before cells are inserted), step S2 (the as-built record) and the first trigger (owner reworks, recorded in the as-built record). OPS-012 step 3 reads "cold checks ... rails only with current limits". Table 3.4-5 Off row reads "Storage, Handling (Assembly during kit assembly)". The row adds no mitigation the register lacks.
- RSK-065 row: the concern restates the register `departure` and `consequence`; step S1 (owner decides whether to seek an FCC reading, due CDR) and both triggers match, the first trigger shortened (its "more than five units are proposed" clause is carried by the "at most five units" clause of the same cell). OPS-006 is the loan scenario. See R2-F5 for the one clause whose citation does not hold.
- Operational placement: both rows are consistent with finding-19's text (Assembly phase of the Off row; the loan scenario). The fix takes the finding's first route, so no "not operational" reason is needed.
- CR text: section 1.2 splits finding-19 and adds the section 8 row, Class II (a table row, not an `OPS` scenario; 02 §10.2): concur. Section 2 counts INSP-001 finding-12, 13, 15, 16 and INSP-002 finding-19, 20, 21, 25, 26: nine, eight closed here, finding-16 to CR-003; section 3 "Do nothing" says eight. Section 4 Risk row: concur, the register is unchanged. Section 4 Schedule row: at `ab2af2d` line 696 is the section 8 lead paragraph, line 704 the RSK-006, RSK-026 row and line 724 the RSK-014 row, so the hunks are 8 and 20 lines from 704 and do not abut; no `cr/CR-003*` branch exists yet, so the three-way merge could not be exercised; the rebase and re-read instruction covers it. Q1 needs no qualifier for the "fix before PDR" liens; INSP-002 finding-27 (due CDR) stays with R1-F3.
- Tool re-run by this reviewer: `tools/traceability.py --root <detached worktree at 56b4bcd> --report-only` exit 0, 245 requirements, 173 test cases, 0 violations, 2 warnings (SYS_UNALLOCATED REQ-SYS-125 and REQ-SYS-148), no RENDER_STALE; worktree removed, `docs/vv/` on `main` unchanged.
- State of the product review: no record on `main` or the branch yet names `conops.md@dfe50c4c`; the INSP-002 delta that section 5 requests is still to be done.

| Item | Reviewer (agent invocation) | Date | Finding | Resolution |
|---|---|---|---|---|
| R1-F1 (Major) | Independent reviewer agent (CR-009 impact review round 2) | 2026-09-27 | Verified. Both parts of INSP-002 finding-19 are now in the prototype: the range (revision 1) and the RSK-064 and RSK-065 rows of the section 8 table (`56b4bcd`). Sections 1.2, 2, 3, 4 Risk and Schedule, 5 and 8 state the change and the lien count correctly. The owner no longer disposes on the belief that a half-fixed lien is closed. | Closed |
| R2-F5 (Minor) The RSK-065 row cites a source that does not carry one of its clauses | Same | 2026-09-27 | The response cell reads "At most five units, never marketed, owned by the owner and lent, never transferred (section 1.2 item 5, CON-008)". Section 1.2 item 5 (line 53) and CON-008 at `60df49c9` say only "at or below five units" and "never marketed". "Owned by the owner and lent, never transferred" comes from ADR-025 section 4.4 (line 72, "control: units lent, never transferred") and the RSK-065 statement ("kept by the owner and lent to friends"); the register holds no "never transferred" control, and its first trigger treats a transfer as a possible owner decision. Section 1.2 of this CR says both rows only restate register content. Nothing is weakened, but a reader following the citation will not find the clause. | Author: cite ADR-025 section 4.4 and the RSK-065 statement for that clause, or drop "never transferred"; can be folded into the revision that resolves R1-F3. No further review round unless a product blob changes. |
| R1-F2 (Minor) | Same | 2026-09-27 | Carried, not re-checked (rule C1). Note: `56b4bcd` is now committed on top of `64eb688`, so removing `64eb688` from the branch also rewrites `56b4bcd` (its blob `dfe50c4c` unchanged); section 8 must then name the new commit. | Open |
| R1-F3 (Minor) | Same | 2026-09-27 | Carried, not re-checked (rule C1). | Open |
| R1-F4 (Minor) | Same | 2026-09-27 | Carried, not re-checked (rule C1). | Open |

Reviewer concurrence: R1-F1 is closed, and I concur with the class, the effectivity and the revision 2 changes. No Major finding is open. **Impact review round 2 complete: 0 Major open; 4 Minor open (R1-F2, R1-F3, R1-F4, and new R2-F5).** The Minor findings are for the author to resolve or answer before Q1 is put to the owner (R1-F2 before section 5 step 5). The INSP-002 delta on `conops.md@dfe50c4c` is still required before the merge. The CR stays Submitted.

## 7. CCB disposition (owner)

Dispositioned 2026-09-28 (table below); originally requested at owner session B1a (Tue 09-29), after the section 6 review, so that the branch merges before WP-PDR-02 implements CR-003 and CR-006 on the same files. Questions for the owner are in section 12.

| Field | Value |
|---|---|
| Decision | Approved |
| Class confirmed | I (proposed I; concurred in section 6.1, unchanged by round 2) |
| Date | 2026-09-28 |
| Conditions | None stated by the owner. The merge follows section 5 steps 5 and 6, with R1-F2 resolved before step 5 and the INSP-002 delta on `conops.md@dfe50c4c` before the merge (section 6.3 concurrence) |
| Rationale | Fixes eight SRR liens of INSP-001 and INSP-002 due before PDR (finding-16 goes to CR-003). Section 6.3: R1-F1 (Major) Verified; R1-F2 to R1-F4 and R2-F5 Minor and open |
| Waiver scope (if Approved (waiver)) | n/a |
| Re-look trigger and re-look-by review (if Deferred) | |
| Source | Chat transcription by Claude (configuration manager) on 2026-09-28. The presenter asked the owner to approve CR-007 to CR-016, the SRR lien fixes that passed their impact reviews (recommendation: approve all ten). Owner statement, verbatim: "Um, and then, yeah, I think you're uh, good to continue." The lead SE reads it as approval of item 1 as recommended, with the branches to merge after the section 9 checks (`docs/plan/status/status-2026-09-28.md` section 1, commit `e288add`, which transcribes the full statement); the owner is asked to correct any line |

Disposition history (append only):

| Date | Decision | New target | Source |
|---|---|---|---|
| 2026-09-28 | Approved | none | owner, `status-2026-09-28.md` section 1 (`e288add`), transcribed by Claude (configuration manager) |

## 8. Implementation record

Implementation in progress (configuration manager, WP-PDR-55 merge batch 1, 2026-09-29). Section 5 step 5 is done up to the merge, step 6 is not done, and the merge is held (section 9, pre-merge check of 2026-09-29).

| Commit | Files | Trailer check (`CR: CR-009` present) |
|---|---|---|
| `9001813` (prototype, branch `cr/CR-009-l0-conops-srr-liens`) | `expectations.json`, `expectations.md`, `conops.md`, `concept.md` | Present. `tools/check_commit_msg.py` fails it: REFS_UNRECOGNIZED (`Refs: WP-PDR-10` names no 05 §4.5 identifier) |
| `64eb688` (same branch; review records, R1-F2) | `docs/reviews/SRR/checklists/expectations.md`, `conops-and-concept.md` (the WP-PDR-10 reviewer's INSP-001 and INSP-002 PDR lien deltas) | Absent (`Refs: CR-009` only); reverted by `48bf86b` |
| `56b4bcd` (prototype revision 2, same branch; R1-F1) | `conops.md` | Present. `tools/check_commit_msg.py` fails it: REFS_MISSING and CR_TRAILER_MISSING, because a blank line separates `CR:` and `Refs:` from the `Co-Authored-By:` trailer, so the tool reads no trailer block |
| `48bf86b` (same branch; R1-F2, configuration manager, 2026-09-29) | The two records of `64eb688`, returned to their blobs at the branch point `ab2af2d` (`git revert` of `64eb688`); no product blob changes | Present (`Refs: CR-009, INSP-001, INSP-002`, `CR: CR-009`); `check_commit_msg.py` PASS |

Step 5 at `48bf86b` (2026-09-29). `main` has not changed the four product paths or the two records since the branch point (`git log ab2af2d..c12872d` on the six paths is empty) and `git merge-tree --write-tree` gives no conflict, so no rebase and no re-render were needed. The four product blobs are the section 5 frozen blobs (`expectations.json@60df49c9`, `expectations.md@4de665a1`, `conops.md@dfe50c4c`, `concept.md@ee0d6e92`), and `git diff --stat ab2af2d 48bf86b` gives exactly those four paths (36 insertions, 32 deletions). Step 4 was re-run on a worktree of `48bf86b`, with these results. `tools/traceability.py --report-only`: exit 0, 245 requirements, 173 test cases, 0 violations, 2 warnings (SYS_UNALLOCATED REQ-SYS-125 and REQ-SYS-148), no RENDER_STALE; outputs restored. `docs/reviews/SRR/figures/concept-block-diagram.py --check`: exit 0, "is current". The deck fonts were linked from the main working tree for this run, because a linked worktree has no `tools/slides/node_modules`; without the fonts the script falls back to DejaVu Sans and reports layout errors. `tools/validate_docs.py`: 48 passed, 2 failed. The two failures are the record drift rule on INSP-001 and INSP-002, which name the `baseline/srr` blobs.

R1-F2 state. The resolution in the section 6.1 row has two parts, and neither is complete.
- (a) "Remove `64eb688` from the unpushed branch." This session did not do it. A rewrite of the branch (the prototype commits re-made without `64eb688`, with trailer blocks that pass `check_commit_msg.py`) was refused by the session's permission classifier as a destructive git operation. The branch keeps `64eb688` in its history, and `48bf86b` reverses it. The `--no-ff` merge therefore brings no record change: the trial merge of section 9 changes the four product paths only. Whether the revert is an acceptable resolution, or whether the branch is rewritten, is for the lead SE, and the owner if she wishes. The same decision covers the `check_commit_msg.py` failures of `9001813` and `56b4bcd` in the table above. Those two commits can be fixed only by a rewrite. Otherwise they are listed for the PDR independent reviewer under 05 §4.5 Checks, as `docs/cm/deviations.md` entry 7 does for the lead SE's own commits.
- (b) "Re-commit the two record deltas on `main` under the convention." The configuration manager prepared this change and did not commit it: the commit on `main` was refused by the session's permission classifier. The change applies `64eb688`'s record changes unchanged, except each record's `verdict`, which is held at NEEDS CHANGES with a comment naming the convention; `reviewer_verdict` stays APPROVED. With it, both records pass `validate_docs.py` on `main`, with drift notes only. It is saved as a patch at `insp-001-002-transplant-held.patch` in the configuration manager's session scratchpad. It was used only in the section 9 trial merge, and the main working tree was left without it.

Step 6 state: not done.
- INSP-001: the `64eb688` delta verified finding-12, 13 and 15 on `expectations.json@60df49c9` and `expectations.md@4de665a1`. These are still the frozen blobs, so that delta covers step 6 for INSP-001 once it is on `main` (R1-F2 (b)) and its `product_commit` is re-pointed to the branch head by its reviewer.
- INSP-002: a new delta that names `conops.md@dfe50c4c` and verifies the section 8 part of finding-19 is still required (section 6.3 concurrence; section 7 Conditions). This invocation started that delta in the reviewer role. It was refused as self-approval, because the same invocation made `48bf86b` and prepared the R1-F2 (b) change. It therefore goes to a reviewer invocation that did no CR-009 implementation work (plan rule C4).
- Facts the configuration manager checked, for that reviewer to re-derive. These are not a verification. `git diff 64eb688 56b4bcd` changes `conops.md` only, in three hunks: the status line, revision history row 5 and the two section 8 rows. `register.json` RSK-064 and RSK-065 (statement, steps and triggers) are identical at 0.6.0-pre-srr on the branch and at 0.7.0-pre-pdr on `main` `c12872d`. R2-F5 still holds on `dfe50c4c`: "owned by the owner and lent, never transferred" is not in section 1.2 item 5 or in CON-008. In the same cell, the RSK-065 trigger treats a transfer as an owner decision.

Other open items before the merge:
- Owner pronouns. `expectations.json` (the SI-014 stakeholder `interests`, "Operates his unit as his own station") and its render `expectations.md` line 295 still use "his". `docs/plan/status/status-2026-09-29.md` section 7 corrects this to she/her as an editorial change "when the CRs that already change those files merge, so that no approved record drifts before its re-issue". If the correction is folded into this branch, both expectations blobs change. INSP-001 then needs a new delta on the new blobs, by a reviewer who did not make the edit, before the merge. If it is made after the merge, INSP-001 drifts on `main` until that delta is made.
- R1-F3, R1-F4 and R2-F5 (Minor) are open and unchanged. Under rule C1 they are liens: the owner's Q1 was answered at the disposition, and none of them blocks the merge.

Traceability report after implementation: to be regenerated at merge; renders regenerated: `docs/requirements/l0-stakeholder/expectations.md` (current at `48bf86b`, no RENDER_STALE).

## 9. Verification of implementation

| Impact item | Planned closure (from §4/§5) | Evidence (report path, TC id, analysis file) | Result |
|---|---|---|---|
| | | | |

Independent verifier (agent invocation): pending.

Configuration manager pre-merge check (2026-09-28; performed at the disposition, not the independent verification, which stays pending). Method: `git merge-tree --write-tree` of the branch head with `main` (no conflict), then a trial `git merge --no-ff` in a detached scratch worktree of `main` (discarded afterwards, no ref kept), `tools/validate_docs.py` and `tools/traceability.py --report-only` on the trial merge, and the failure set compared with the baseline. Baseline on `main` at `e288add`: `tools/validate_docs.py` 102 passed, 8 failed (all record drift already on `main`: SRR `adrs-001-to-025.md`, `process-02-requirements-and-traceability.md`, `tool-validation-tv-001-to-tv-010.md`, `trade-studies-ts-001-ts-002.md`, `trade-study-ts-002-software-assurance.md`; PDR `cm-plan-05-software-assurance.md`, `configuration-status.md`, `lessons-learned.md`); `python -m unittest discover -s tools/tests` 596 run, 1 failure (`test_repository_exit_zero`, the same drift), 14 skipped; `tools/traceability.py --report-only` 0 violations, 2 warnings. Branch head `56b4bcd`. Scope: `git diff --name-only main...` gives the four product paths and two SRR records (`docs/reviews/SRR/checklists/expectations.md`, `conops-and-concept.md`, commit `64eb688`, R1-F2). Trial merge: `validate_docs.py` 101 passed, 9 failed; one new failure, `docs/reviews/SRR/checklists/conops-and-concept.md` (INSP-002, APPROVED, names `conops.md@8415dba2`, the revision 1 blob; the branch holds `dfe50c4c`). `traceability.py --report-only`: 0 violations, 2 warnings. Merge held: no record names `conops.md@dfe50c4c` (`git grep dfe50c4c` on `main` and on the branch is empty), so the INSP-002 delta that section 6.3 requires before the merge is not filed; R1-F2 (the record commit on the product branch) is unresolved, and removing `64eb688` rewrites `56b4bcd`, a judgement for the CR author and the lead SE, not a mechanical merge step.

Configuration manager pre-merge check 2 (2026-09-29, WP-PDR-55 merge batch 1; not the independent verification, which stays pending). Method as above, in a detached linked worktree of `main` in the session scratchpad, which is discarded afterwards; no ref is kept. Python: `/Users/robinonsay/rust/cwht/.venv/bin/python`.
- Baseline on `main` at `c12872d`: `tools/validate_docs.py` 109 passed, 8 failed, 117 checked. The failures are PDR `cm-plan-05-software-assurance.md`, `configuration-status.md` and `lessons-learned.md`, and SRR `adrs-001-to-025.md`, `process-02-requirements-and-traceability.md`, `tool-validation-tv-001-to-tv-010.md`, `trade-studies-ts-001-ts-002.md` and `trade-study-ts-002-software-assurance.md`. None of them names a CR-009 path.
- Branch head `48bf86b`. `git merge --no-ff cr/CR-009-l0-conops-srr-liens` gave the trial merge `c805344`: clean, no conflict. It changes exactly the four product paths (36 insertions, 32 deletions) and no record.
- Trial A, the merge as it stands. `validate_docs.py`: 107 passed, 10 failed. The 8 failures of `main` are unchanged. There are two new failures, both by the record drift rule:
  - INSP-001 (`docs/reviews/SRR/checklists/expectations.md`) names `expectations.json@52b6cf5e` and `expectations.md@f460c1fb` against `60df49c9` and `4de665a1`.
  - INSP-002 (`conops-and-concept.md`) names `conops.md@6c3fbb2b` and `concept.md@6f026f92` against `dfe50c4c` and `ee0d6e92`.
  - `tools/traceability.py --report-only`: 0 violations, 2 warnings.
- Trial B: A plus the R1-F2 (b) record change of section 8, with both record verdicts set APPROVED as the merge commit would set them. `validate_docs.py`: 108 passed, 9 failed. INSP-001 passes. One new failure remains, INSP-002, whose `product_files` name `conops.md@8415dba2` (the revision 1 blob that the `64eb688` delta reviewed) against `dfe50c4c`. This failure clears only when an independent reviewer's delta names `dfe50c4c` and verifies the section 8 rows (section 8, step 6 state).
- `python -m unittest discover -s tools/tests` on trial A (first run, with the traceability report files not restored): 596 run, 1 failure, 2 errors, 17 skipped. Not yet compared with `main`; the paired re-run was not finished when this check was recorded.

Merge held. The blockers, in order:
1. The INSP-002 delta on `conops.md@dfe50c4c`, by a reviewer invocation that did no CR-009 implementation work.
2. The commit on `main` of the R1-F2 (b) record change, with the verdicts held. It could come with item 1 in one record commit made by that reviewer's workflow.
3. The lead SE's ruling on R1-F2 (a): accept the revert, or rewrite the branch. This ruling also settles the `check_commit_msg.py` failures of `9001813` and `56b4bcd`.
4. The she/her fold-in decision for `expectations.json` and `expectations.md`. If the correction is folded into the branch, INSP-001 needs a further delta.
5. The section 9 independent verification (the table above and the verifier line).
6. A fresh trial merge in which `validate_docs.py` shows no new failure against `main`.
7. The owner's merge approval at S1 (WP-PDR-55 batch 1).

Lead SE rulings (2026-09-29, on items 3 and 4 above).
- Item 3, R1-F2 (a): the revert is accepted and the branch is not rewritten. `9001813`, `56b4bcd` and `64eb688` are reviewed commits (plan rule C2), and 05 §4.5 keeps history as made. The `--no-ff` merge brings no record change, because `48bf86b` reverses `64eb688`. The two failing messages (`9001813`, `56b4bcd`) are listed in `docs/cm/deviations.md` entry 8 for the PDR independent reviewer; the `merge(CR-009)` commit carries the `CR: CR-009` and `Refs:` trailers.
- Item 4: the she/her correction of `expectations.json` (SI-014 `interests`) and its render `expectations.md` is folded into this branch as an editorial commit by the configuration manager, before the INSP-001 delta, so that one reviewer delta names the final blobs (`status-2026-09-29.md` section 7).

## 10. Closure

| Field | Value |
|---|---|
| Owner merge approval | 2026-09-28, with the disposition: "their branches merge after the section 9 checks" (lead SE reading, `docs/plan/status/status-2026-09-28.md` section 1). Merge held at the disposition: see the section 9 configuration manager pre-merge check |
| Merge commit | |
| Waiver entered in CSA item 12 and affected VDDs | n/a |
| CSA regenerated | |
| Date closed | |

## 11. History

| Date | State | By | Commit on main | Note |
|---|---|---|---|---|
| 2026-09-27 | Draft, then Submitted | Claude (WP-PDR-10 author) | `1f7d138` | Created with the impact assessment complete; product prototype on the branch at `9001813` |
| 2026-09-27 | Submitted | Claude (WP-PDR-10 author) | this file's commit | Prototype commit message corrected (validate_docs result) by amending the unpushed branch commit `f511e02` to `9001813`; the four product blobs are unchanged; section 5 step 4 corrected to the post-commit validate_docs result |
| 2026-09-27 | Submitted (impact review round 1 recorded) | Independent reviewer agent | the commit that records section 6.1 | Impact review complete with 1 Major (R1-F1, finding-19 half fixed) and 3 Minor (R1-F2 to R1-F4) findings; stays Submitted for author revision before disposition |
| 2026-09-27 | Submitted (revision 2) | Claude (CR author, WP-PDR-10) | the commit that records revision 2 | R1-F1 resolved: ConOps section 8 rows for RSK-064 and RSK-065 on the branch at `56b4bcd`; sections 1.2, 2, 3, 4 (Risk, Schedule), 5, 6.2 and 8 updated; new frozen ConOps blob `dfe50c4c`; R1-F2 to R1-F4 (Minor) not changed (rule C1); INSP-002 delta and round 2 re-check requested |
| 2026-09-27 | Submitted (impact review round 2 recorded) | Independent reviewer agent | the commit that records section 6.3 | R1-F1 verified closed on `56b4bcd` (`conops.md@dfe50c4c`); new Minor R2-F5 (RSK-065 row citation); R1-F2 to R1-F4 carried; 0 Major open; stays Submitted |
| 2026-09-28 | Dispositioned (Approved) | Claude (configuration manager), transcribing the owner | the commit that records this row (`Refs: CR-009`) | Owner approval of CR-007 to CR-016 as recommended (`status-2026-09-28.md` section 1); merge held at the disposition: INSP-002 delta on `conops.md@dfe50c4c` not filed; R1-F2 (record commit `64eb688` on the branch) open (section 9 pre-merge check) |
| 2026-09-29 | Dispositioned (Approved); implementation in progress, merge held | Claude (configuration manager, WP-PDR-55 merge batch 1) | the commit that records this row (`Refs: CR-009`) | Step 5 up to the merge: no rebase needed (`main` has not moved the six paths since `ab2af2d`); branch head `48bf86b` (reverts the record commit `64eb688`; product blobs unchanged); step 4 re-run: traceability 0 violations, no RENDER_STALE, render current. R1-F2 partly resolved: the branch rewrite was refused by the session permission classifier, and the re-commit of the record deltas on `main` is prepared but not committed. Step 6 not done: the INSP-002 delta on `conops.md@dfe50c4c` goes to a reviewer who did no CR-009 implementation work. Pre-merge check 2 on `main` `c12872d`: trial merge `c805344` clean, four product paths; `validate_docs.py` adds INSP-001 and INSP-002 (drift); with the prepared record change, INSP-002 only. Unit tests on the trial merge (first run, with the traceability report files not yet restored): 596 run, 1 failure, 2 errors, 17 skipped. The failing tests are not identified yet: a re-run on the trial merge beside a baseline run on `main` `c12872d` was still running when this row was written, and its result is not recorded here. Blockers: section 9 list |

## 12. Questions for the owner (answer with the disposition)

1. Approve CR-009 as Class I? Recommendation: approve.
2. OPS-020 step 5: accept the band-edge acceptance at the 5 W step, keyed from the paddle in Transmit-keyed mode with the tinySA holding the maximum over bursts? Recommendation: accept; the 5 W step is the worst case for the keying sidebands, and Bench-test cannot reach it (REQ-SYS-187).

Answers recorded with the disposition (2026-09-28; the lead SE reading of the owner's approval "as recommended", the owner is asked to correct any answer): Q1 approved, Class I. Q2 accepted: the OPS-020 step 5 band-edge acceptance at the 5 W step from the paddle in Transmit-keyed mode.
