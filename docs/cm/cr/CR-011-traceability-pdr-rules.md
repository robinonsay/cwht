---
id: CR-011
title: Add the PDR rule set and the --gate, --volatility and --fix-children options to tools/traceability.py
status: Dispositioned
class: II
originator: Claude
date_opened: 2026-09-27
phase: B
configuration_at_origination: baseline/srr (tag on 779f93f); main at a3cacee; branch cr/CR-011-traceability-pdr-rules at 4774562
baseline_affected: baseline/srr
affected_cis: [2, 18, 28, 30, 40]
affected_paths: [tools/traceability.py, tools/tests/test_traceability.py, tools/tests/test_tools.py, tools/tests/fixtures/valid_project/docs/requirements/sys/requirements.json, tools/tests/fixtures/valid_project/docs/requirements/sys/requirements.md, tools/tests/fixtures/valid_project/firmware/cwht-core/src/keyer/straight.rs, tools/tests/fixtures/valid_project/firmware/cwht-core/src/keyer/iambic.rs, tools/tests/fixtures/valid_project/firmware/cwht-core/src/keyer/config.rs, tools/tests/fixtures/valid_project/hardware/kicad/tx-pa.kicad_sch, tools/README.md, docs/process/02-requirements-and-traceability.md, docs/cm/tool-validation/TV-002-traceability.md, docs/cm/tool-validation/evidence/traceability-2026-09-27-r6.py, docs/cm/tool-validation/evidence/traceability-2026-09-27-r6.log.txt, docs/cm/tool-validation/evidence/traceability-2026-09-27-r7.py, docs/cm/tool-validation/evidence/traceability-2026-09-27-r7.log.txt, docs/vv/traceability-report.md, docs/vv/traceability.json]
affected_ids: [TV-002, ACC-TRACE-001, ACC-TRACE-002, INSP-015, INSP-020, RFA-SRR-007]
related: [CR-002, CR-003, CR-006, CR-007, CR-008, CR-009, CR-012, RFA-SRR-007, INSP-015, INSP-020, TV-009]
target_release: none
branch: cr/CR-011-traceability-pdr-rules
disposition: Approved
disposition_date: 2026-09-28
relook_trigger: null
relook_by: null
merge_sha: null
date_closed: null
---

# CR-011: Add the PDR rule set and the --gate, --volatility and --fix-children options to tools/traceability.py

Template: `docs/templates/change-request.md`. Process: `docs/process/05-configuration-and-data-management.md` §5. This file is committed on `main`; the branch `cr/CR-011-traceability-pdr-rules` carries the product changes. Work package: WP-PDR-06 of `docs/plan/pdr-work-plan.md` (revision 2). The plan's register of phase CRs (section 6.2) does not list this CR; it is raised because `tools/traceability.py` has been under CR control since its accreditation ACC-TRACE-001 (05 Table 4-1 row 28, "Accreditation puts the tool under CR control"), and every non-editorial change to a class-CR CI after its CR-from event is a CR (05 §5.1).

**Revision 2 (2026-09-27).** The branch head moved from `4774562` to `2b004b1` for the INSP-043 finding-1 (Major) fix: `709e95f` adds `RegressionSetTests` to `tools/tests/test_traceability.py` (blob `95f1719b` becomes `6ead5641`), and `2b004b1` adds TV-002 purpose 9 (`--regression`), run 7 and its evidence (`traceability-2026-09-27-r7.py`, `.log.txt`). The tool blob `d4cde9f5` and every other branch file are unchanged. This revision states run 7 in `affected_paths`, §4 Verification, §5, §8, §9 and §11, and names in §5 step 5 the record deltas the moved blobs require. It changes no product file.

**Revision 3 (2026-09-27).** Resolves the section 6.1 round 1 Major finding IR-F1 (section 6.2). Section 1 now names the seven new codes that are violations in a plain run. Section 4 rows Requirements and traceability and Schedule, and the new section 4.1, state the effect on the open L0, L1 and `TC-SYS` CRs with trial numbers and the merge condition. `related` adds CR-003, CR-006, CR-008 and CR-009. Section 5 verification, the section 7 proposed Conditions and a section 9 row re-run the plain run after each later requirement CR merge. The Minor findings IR-F2 to IR-F5 are not resolved in this revision (plan rule C1). The branch head `2b004b1` and every product file are unchanged.

## 1. Description of the change

`tools/traceability.py` blob `12de3545` (commit `c774851`) becomes blob `d4cde9f5` (commit `4411a09` on the branch). The change adds the rules and options that 02 §8.5 and 04 §7.4 date at PDR, and three items carried from SRR:

| Item | Rule and source | New or changed code or option |
|---|---|---|
| Entrance mode | 02 §8.1, §8.2 gate column | `--gate <SRR\|PDR\|CDR\|TRR\|SAR>`: `GATE_ERROR_FROM` promotes a listed warning to a violation from its gate on; gate-only rules `TBR_DUE_AT_GATE` (T-14), the PDR form of T-18 (`SYS_UNALLOCATED`: a live L2 child or the tag `leaf`), `BASELINE_NOT_READ`, and `HAZARD_REQ_NOT_ON_TARGET` for `Verified` at SAR (01 §8.6) |
| Git history | 02 T-04, T-12, T-13; 04 rule 7.3.11 | `BASELINE_ID_MISSING`, `TRANSITION_FORBIDDEN`, `CHANGE_UNCOVERED` (02 §10.2 classes, approved-CR or editorial-commit coverage, editorial log), `CASE_STALE`, against the most recent `baseline/*` tag along the first-parent history |
| Design references | 02 T-15; 03 §8 (SWE-052 Table 1 row 3) | `DESIGN_REF_UNRESOLVED` (element id, ICD file, `.kicad_sch`, `.rs`, `rustos:<path>` read by `git show` at the lock §3 commit; option `--rustos`), `DESIGN_REF_MISSING`, `DESIGN_ELEMENT_ORPHAN`, `DESIGN_REF_INVERSE`, `REUSED_TAG_NO_REF` |
| Measures | 02 T-16, T-20 | `KDR_WITHOUT_MOP`, `MOE_WITHOUT_MOP` |
| ICD pairing | 02 T-22, §3.5 | `ICD_NAME`, `ICD_UNPAIRED`, `ICD_SECTION4_MISMATCH`; report section 14 |
| Hazards | 03 §8; 02 T-08; 04 rule 7.3.6 | `HAZARD_UNCONTROLLED`; `HAZARD_INVERSE` an Error under `--gate` |
| Evidence | 04 rules 7.3.4 (PCA-05; SEMP App. F F-06), 7.3.5, 7.3.12 | `CLOSED_NOT_INSTALLED`, `VAL_PHASE_MISSING`, `DEVBOARD_CASE_CLOSING` (a dev-board case is never closing) |
| ADR back-reference | RFA-SRR-007 item L-7 | `ADR_BACKREF_MISSING`; report section 15 |
| Safety-critical hardware parts | SRR decision memo §9 condition 5 | `SAFETY_PART_UNTRACED`, on the proposed field `elements[].safety_critical` of `docs/design/allocation.json` (the field and its schema change belong to WP-PDR-31); report section 17 |
| Report sections | 02 §8.1 planned sections; 04 §7.4 row 7.3.2 | 12 changes since the baseline and editorial log, 13 retired entries, 16 stakeholders; section 11 shows each code's severity under `--gate` |
| Volatility | 02 §10.4 (SWE-200, MSR-02, TPM-012) | `--volatility --from <ref> [--to <ref>] [--dry-run]`: appends `MSR-02` to `docs/plan/measurements.json` after a schema check |
| Children | 02 §8.1, T-06 | `--fix-children` |

Plain-run behavior of every existing code is unchanged. Seven new codes are violations in a plain run, because their sources set E in the `check` column of 02 §8.2 or make the run fail (04 §7.4): `BASELINE_ID_MISSING` (02 T-04), `TRANSITION_FORBIDDEN` (02 T-12), `CHANGE_UNCOVERED` (02 T-13), `CLOSED_NOT_INSTALLED` (02 T-11; 04 rule 7.3.4), `CASE_STALE` (04 rule 7.3.11), `DEVBOARD_CASE_CLOSING` (04 rule 7.3.12: a dev-board case is never closing) and `VAL_PHASE_MISSING` (04 rule 7.3.5). IR-F1 names the first six; a comparison of the check catalogues of blobs `12de3545` and `d4cde9f5` adds `VAL_PHASE_MISSING`. `TBR_DUE_AT_GATE` is a violation only under `--gate`. Every other new rule has W in the `check` column of 02 §8.2 (T-15, T-16, T-18, T-20) or has no 02 row: it is a warning in a plain run and a violation under `--gate` from the gate that `GATE_ERROR_FROM` names. On today's `main` merged with the branch the seven codes find nothing (section 4). The three history codes then fail every later change to an L0 entry, an L1 requirement or a `TC-SYS` case that no approved CR covers (section 4.1). `HAZARD_UNCONTROLLED` is a plain-run warning, not the violation 03 §8 names, because the software L2 requirements that close it are PDR products (WP-PDR-35); it is a violation under `--gate` from PDR.

Other files on the branch: known answers in `tools/tests/test_traceability.py` (thirteen new classes, temporary git repositories for the history rules) and the `Swe052CoverageTests` states in `tools/tests/test_tools.py`; `valid_project` gains the design units its `design_refs` name, `B21` on `REQ-SYS-006` and `mop_ids` on its two KDRs; `tools/README.md` traceability section; 02 §8.1 (options, inputs, outputs), §8.2 lead sentence, §8.5 (implementation status with the five codes INSP-020 finding-8 found unbound, carried item C-126) and §10.4 ("planned option" removed); TV-002 run 6 with ACC-TRACE-002 requested; `docs/vv/traceability-report.md` and `traceability.json` regenerated.

## 2. Reason

The PDR readiness declaration is blocked until every tool row due at PDR has a passing unit test (04 §7.4; 02 §8.5), and plan WP-PDR-06 delivers them (carried items C-026 tool part, C-068, C-069, C-111, C-126, C-183, C-184; RFA-SRR-007 L-7). Workaround while the CR is open: the reviewers apply the 02 §8.2 gate column and the planned checks by hand, as at SRR (tools/README.md "Not implemented, with gates" at `a3cacee`).

## 3. Alternatives considered

| Alternative | Why rejected or deferred |
|---|---|
| Do nothing | The PDR readiness declaration is blocked (04 §7.4); every PDR check would be manual, which is what the lessons of SRR (plan §1.4 L5, L6) advise against |
| Commit the tool change on `main` as a Log change | Not allowed: the tool is a class-CR CI since ACC-TRACE-001 (05 Table 4-1 row 28); CR-002 changed it through its CR |
| Make the new PDR rules violations in a plain run | Every commit on `main` would fail until the PDR products exist; 02 §8.2 sets W in the `check` column and E in the `gate` column for these rules |

## 4. Impact assessment (CM plan §5.3)

| Field | Assessment (numbers, IDs, paths) |
|---|---|
| Performance margins | None: no TPM or MOP value changes. The tool newly reports `KDR_WITHOUT_MOP` and `MOE_WITHOUT_MOP` (repository: 0 and 1, MOE-013) |
| Safety | None to a hazard or control. The tool newly reports `HAZARD_UNCONTROLLED` for HZ-002, HZ-007, HZ-008, HZ-011 (firmware role, no REQ-SW-* yet: WP-PDR-35 and WP-PDR-16 close them) and reads the safety-critical part field of SRR memo §9 condition 5. No 07 §14.1 module changes; hazard analysis and RF exposure evaluation unchanged |
| Risk | None added or re-scored. RSK-009 (process completeness) is helped: the PDR checks become automatic |
| Software classification and tailoring | None: `rmm.json` rows unchanged. 03 §8 (SWE-052 table) and the RMM SWE-052 row now lag the tool (rows 2 and 3 enforced); their update belongs to WP-PDR-17, the 03 writer (plan §5.3) |
| Interfaces | None: no ICD changes; the tool reads ICD names, front matter and section 4 |
| Operations and ConOps | None (no operator procedure, handbook or maintenance instruction) |
| Cybersecurity | None: no USB firmware-load or key-input path |
| Verification | Tool validation: TV-002 run 6 (section 4 of the record): 229 known-answer tests, 0 skipped, pass on an export of `4411a09`; mutation check against blob `12de3545` fails every new class. TV-002 run 7 (revision 2, INSP-043 finding-1): 235 known-answer tests (86 + 32 + 117), 0 skipped, pass on an export of `709e95f`, with purpose 9 (`--regression`, 04 §7.3 rule 10 and §10.5) and its `TC-ATP` clause exercised by `RegressionSetTests`; the six mutants M1 to M6 of `regression_set` and `design_ref_matches` are killed; repository run R-4 equal to R-3. Repository run R-3: plain 0 violations, 95 warnings; `--gate PDR` 379 violations, the PDR work still open. No TC-* changes. Record drift: the SRR records INSP-015 and INSP-020 name the earlier blobs, so `tools/validate_docs.py` and `test_validate_docs.RepositoryTests` fail on the branch until their delta iterations (section 5 step 6) |
| Cost | None |
| Schedule | Needed before the PDR readiness declaration (plan B4, Tue 10-06); the output becomes accredited evidence only after the reviews of section 5 steps 5 and 6, the disposition, the merge and ACC-TRACE-002. Interaction with the requirement CRs (IR-F1; section 4.1): the owner disposes CR-003 and CR-006 (OD-02, OD-03) and CR-008 and CR-009 (OD-37) from B0 (Mon 09-28) on. CR-011 merges only when the plain run on its merge tree gives 0 violations. Each of CR-003, CR-006, CR-008 and CR-009, merged before or after CR-011, needs its disposition Approved on `main` and every L0, L1 and `TC-SYS` id its branch changes listed in `affected_ids`. CR-008 as submitted fails this (164 ids), so CR-008 revises `affected_ids` before its disposition. Otherwise the CR merged second is blocked: CR-008 if CR-011 merges first, CR-011 if CR-008 merges first |
| Requirements and traceability | None added, modified or retired by this CR; volatility contribution 0 (`--volatility --from baseline/srr --dry-run`: V 0.0 % for L1, L2 and software). Orphans or uncovered requirements created: none (plain run on `main` at `a244b05` merged with `2b004b1`: 0 violations, 96 warnings; author trial of 2026-09-27). **Effect on other CRs (IR-F1; section 4.1).** From the merge on, a plain run checks 02 T-04, T-12 and T-13 against `baseline/srr`. An L0 entry, L1 requirement or `TC-SYS` case with a Class I or Class II difference (02 §10.2) fails with `CHANGE_UNCOVERED` unless its id is listed in `affected_ids` by a CR in `docs/cm/cr/` whose `disposition` begins with `Approved`. Only a change made entirely in editorial commits is exempt. The check reads the tree against the tag, so merge order does not avoid it: a change merged before CR-011 fails the first plain run after CR-011 merges. Affected: CR-003, CR-006, CR-008 and CR-009, and every later L0, L1 or `TC-SYS` CR (L2 requirements and their cases join at `baseline/pdr`). Trial result: CR-008 as submitted gives 208 `CHANGE_UNCOVERED`, and 164 with its disposition Approved, because its `affected_ids` omit changed ids. CR-009 gives 5 while Submitted and 0 once Approved. CR-003 and CR-006 have no branch to trial. The merge condition is in section 4.1 |
| Regulatory | None |
| Documentation | `tools/README.md`, 02 §8.1, §8.2, §8.5, §10.4 (on the branch). Not on the branch, sent to their writers: 03 §8 and the RMM SWE-052 row (WP-PDR-17), 04 §7.4 rows 7.3.2, 7.3.4, 7.3.5, 7.3.6, 7.3.11, 7.3.12 (WP-PDR-13), `tools/toolchain.lock.md` §1.1 and §5 rows for runs 6 and 7 (WP-PDR-09; INSP-043 finding-4 lien), `docs/cm/tool-validation/README.md` TV-002 index row (tool owner; INSP-043 finding-4 lien), SEMP §4.3 allocation row and App. F F-06 (the SEMP writer, WP-PDR-13 or WP-PDR-46), 01 §3.1 item 2 (`--gate <REVIEW>`, WP-PDR-12) |
| Released units | None |

Classification rationale: Class II. The change modifies a class B evidence-generating tool and the documentation that describes it; it changes no requirement, interface, safety control, verification evidence already filed, or operator procedure, and the tool cannot change a released image (05 §5.1, "Version change of an Accredited tool": Class I only if the tool can change a released image). The independent review of section 6 is held anyway under plan rule C6 (every CR raised in the PDR phase is reviewed before disposition).

### 4.1 Effect on open CRs and merge condition (IR-F1)

Author trials of 2026-09-27: scratch detached worktree holding `main` at `a244b05` merged with the branch head `2b004b1`, plain run of the branch tool; then each open CR branch merged on top, run as submitted and again with its CR file's `disposition` set to `Approved` and committed; merges discarded, no ref kept. Codes other than `CHANGE_UNCOVERED` gave 0 in every trial.

| CR (branch head) | Levels its change touches | Plain run with the CR Submitted | Plain run with the disposition Approved | Condition before it merges |
|---|---|---|---|---|
| CR-011 alone | none | 0 violations, 96 warnings | n/a | none |
| CR-008 (`c629198`), CR file revision 2 on `main` | L1, `TC-SYS` | 208 `CHANGE_UNCOVERED` | 164 `CHANGE_UNCOVERED` (128 `REQ-SYS`, 36 `TC-SYS`), all Class II fields of 02 §10.2: `tbr` 57, `expected_artifacts` 36, `rationale` and `tbr` 17, `source_ids` 15, `source_ids` and `tbr` 13, `rationale` 12, `rationale`, `source_ids` and `tbr` 8, `verification_note` 3, three other combinations 1 each. Example: REQ-SYS-002 `rationale`, REQ-SYS-004 `tbr`, changed on the branch and absent from `affected_ids` | `affected_ids` lists every id the branch changes, or the branch drops the changes it does not mean to make, before the disposition. The finding goes to the CR-008 author through its section 6 impact reviewer; this CR does not edit CR-008 |
| CR-009 (`64eb688`) | L0 | 5 `CHANGE_UNCOVERED` | 0 | Disposition Approved on `main` before the merge (05 §5.2 already requires it) |
| CR-003, CR-006 (no branch) | L0, L1, `TC-SYS` (`affected_paths` of each) | not trialled | not trialled | As CR-008: every L0, L1 and `TC-SYS` id the implementation changes is in `affected_ids`; if the implementation reaches an id the CR does not list, the CR is revised before the merge |
| CR-010, CR-012, CR-013, CR-015, CR-016 | none | 0 violations (trial on `main` at `8c57710`) | n/a | none from CR-011 |
| CR-014 (`367b3dd`) | none (no requirement, expectation or test case file) | not trialled: the branch conflicts with `main` in `docs/cm/tool-validation/README.md` and `tools/toolchain.lock.md`, files CR-011 does not change | n/a | none from CR-011 |
| Any later CR | L0, L1, `TC-SYS`; L2 and its cases after `baseline/pdr` | fails until the disposition is Approved on `main` | 0 if `affected_ids` is complete | as CR-003 |

Merge order does not remove the effect, because `CHANGE_UNCOVERED` compares the tree with `baseline/srr`. If CR-008 merges first as submitted, CR-011's own merge fails its plain run. If CR-011 merges first, CR-008's merge fails. Proposed condition (section 7): CR-011 and each CR above merge only when the plain run on the merge commit gives 0 violations. Until a requirement CR is disposed, a plain run on its prototype branch merged with `main` fails with `CHANGE_UNCOVERED` on the ids that CR lists. A reviewer of that branch counts those findings as expected and any other finding as a defect. After each later merge the plain run is re-run on `main` (section 5, section 9).

## 5. Implementation plan

| Step | Artifact and path | Responsible | Done (SHA) |
|---|---|---|---|
| 1 | `tools/traceability.py`, tests, fixtures, `tools/README.md`, 02 §8.1, §8.2, §8.5, §10.4 on the branch | Claude (tool owner, WP-PDR-06) | `4411a09` |
| 2 | TV-002 run 6, evidence procedure and log, regenerated `docs/vv/traceability-report.md` and `traceability.json` on the branch | Claude (tool owner) | `89fac92` |
| 3 | 02 §8.5 evidence line and TV-002 limitation 6: the record drift of INSP-015 and INSP-020 | Claude (tool owner) | `4774562` |
| 3a | INSP-043 finding-1 (Major) fix: `RegressionSetTests` in `tools/tests/test_traceability.py` (blob `6ead5641`); TV-002 purpose 9, limitation 9, run 7 and the ACC-TRACE-002 scope purposes 1 to 9 (blob `94ae3af5`); run 7 evidence procedure and log | Claude (tool owner) | `709e95f`, `2b004b1` |
| 4 | Section 6 impact review of this CR | Independent reviewer (did not author CR-011) | pending |
| 5 | Product reviews frozen at the branch blobs: `docs/reviews/PDR/checklists/code-tools-traceability.md` (INSP-042, reviewer APPROVED at `4774562`), `code-tools-traceability-software-assurance.md` (not filed), `tool-validation-tv-002.md` (INSP-043, reviewer APPROVED at iteration 2 on `2b004b1`) (plan WP-PDR-06 Records; checklists of CR-012 / WP-PDR-03). Before a record verdict is set APPROVED at the merge (lead SE convention of 2026-09-27), every `product_files` blob must equal the merged blob: INSP-042 names `tools/tests/test_traceability.py` at `95f1719b`, which step 3a changed to `6ead5641`, so INSP-042 needs a delta iteration naming the new blob; and INSP-042 and INSP-043 name this CR file at `d597899b`, which this revision and sections 6, 7 and 10 change, so each record's delta at the merge names the CR file blob it then reads, or drops the CR file from `product_files` as context rather than product | Independent reviewer and software assurance reviewer | INSP-042 iteration 1 `d9a78e0`; INSP-043 iterations 1 and 2 `d9a78e0`, `b77a9e5`; SA record and INSP-042 delta pending |
| 6 | Delta iterations of the SRR records INSP-015 (`docs/reviews/SRR/checklists/tool-validation-tv-001-to-tv-010.md`) and INSP-020 (`docs/reviews/SRR/checklists/process-02-requirements-and-traceability.md`) naming the new blobs (clears the record drift) | Their reviewers | pending |
| 7 | Owner disposition (section 7) and merge `merge(CR-011): ...`; then the owner records ACC-TRACE-002 in TV-002 section 9 | Owner; Claude merges | pending |

Verification of the implementation (what the independent reviewer checks): TV-002 section 3 re-run on an export of the branch head gives 235 tests (run 7 selection; 229 with the run 6 selection), 0 skipped, OK; the mutation checks of TV-002 runs 6 and 7 (step 3 and step 3b) are repeatable; each code against its source text (02 §8.2 to §8.5, §10.2 to §10.4; 04 §7.3 rules 4, 5, 11, 12 and §8.2; 03 §8; SRR memo §9 condition 5; RFA-SRR-007 L-7); a plain run on the merged `main` gives 0 violations; after each later merge of a CR that changes an L0 entry, an L1 requirement or a `TC-SYS` case (CR-003, CR-006, CR-008, CR-009 and later CRs; section 4.1), the plain run is re-run on that merge commit and gives 0 violations, recorded in section 9; `tools/validate_docs.py` exits 0 after step 6.

## 6. Independent review of the impact assessment

Required by plan rule C6 (lesson L4), although a Class II CR that touches no requirement, ICD, hazard or test case would not need it (05 §5.2).

| Item | Reviewer (agent invocation) | Date | Finding | Resolution |
|---|---|---|---|---|
| Pending | | | | |

Reviewer concurrence: pending.

### 6.1 Impact review round 1: independent reviewer (2026-09-27)

Reviewer: independent reviewer agent (CR-011 impact review invocation), a separate invocation that authored no part of this CR, of WP-PDR-06, of TV-002 runs 6 and 7, and none of the records INSP-042, INSP-043 or INSP-051. Date 2026-09-27. The table and the "pending" line above are the template placeholders and are left as written; this round is the first review entry. Configuration reviewed: this file at blob `892670b6` (revision 2) on `main` at `6086319`; branch `cr/CR-011-traceability-pdr-rules` at `2b004b1` (merge base `a3cacee`). Method: `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` first (queries: the 03 section 8 hazard-trace rows; "WP-PDR-06 traceability tool PDR rules"; "invoke tools/traceability.py in a script, hook or gate"; "02 section 10.2 change classes"), then `grep` and `git` only to pin lines and blobs; `git diff --stat main...cr/CR-011-traceability-pdr-rules`; `git merge-tree --write-tree main cr/CR-011-traceability-pdr-rules`; a scratch detached worktree (removed after use, no ref kept) holding `main` at `fefcf55` merged with `2b004b1`, in which the reviewer ran the branch tool, `tools/validate_docs.py` and the unit tests, and then trial-merged each open CR branch on top (merges aborted; no commit reached any branch). LTspice was not run.

| Item | Reviewer (agent invocation) | Date | Finding | Resolution |
|---|---|---|---|---|
| IR-F1 (Major) Plain-run severity misstated; the interaction with open requirement CRs is not assessed | Independent reviewer agent (CR-011 impact review) | 2026-09-27 | Section 1 says "New PDR rules follow the `check` column of 02 §8.2: warnings in a plain run, violations under `--gate`". In blob `d4cde9f5` six new codes are plain-run violations (check catalogue lines 352 to 357): `DEVBOARD_CASE_CLOSING`, `CLOSED_NOT_INSTALLED`, `BASELINE_ID_MISSING`, `TRANSITION_FORBIDDEN`, `CHANGE_UNCOVERED`, `CASE_STALE`. That is what 02 T-04, T-12 and T-13 ask (check column E), so the tool is right and the CR text is wrong. The consequence is not in section 4. After the merge every plain run (07 §8.4 gate G4, 05 §8.3 release precondition (a), each reviewer's "traceability exit 0" check) fails on any L0, L1 or `TC-SYS` change that no approved CR lists in `affected_ids`. Reviewer trial on the merged tree: `cr/CR-008-srr-liens-l1-and-tc-sys` merged on top gives 208 `CHANGE_UNCOVERED`; with the CR-008 disposition set to Approved in the trial and the merge committed, still 164 (for example REQ-SYS-002 `rationale` and REQ-SYS-004 `tbr`, changed on that branch and absent from its `affected_ids`; Class II fields under 02 §10.2). `cr/CR-009-l0-conops-srr-liens`: 5 while Submitted, 0 if Approved. `cr/CR-010-*`, `cr/CR-015-*`, `cr/CR-016-*`: 0. So the section 4 rows "Requirements and traceability: None" and the Verification line "a plain run on the merged `main` gives 0 violations" hold only for today's `main` and depend on the merge order. The owner disposing CR-011 and CR-008 at B0 would not know that merging CR-011 first blocks CR-008 as submitted, and that every requirement CR branch fails a plain run until its disposition | Author: correct the section 1 sentence (name the six plain-run violation codes and their 02 sources). In section 4 rows Requirements and traceability and Schedule, state the effect on open CRs (CR-003, CR-006, CR-008, CR-009 and any later L0, L1 or `TC-SYS` CR) with the trial numbers above, and propose the merge order or the condition (for example: CR-008 `affected_ids` completed before either merge; the finding goes to the CR-008 author through its impact reviewer). Add CR-008 and CR-009 to `related`. In the section 5 verification line, re-run the plain run after each later CR merge |
| IR-F2 (Minor) Record deltas at the merge are incomplete | Independent reviewer agent (CR-011 impact review) | 2026-09-27 | Section 5 step 5 names only `tools/tests/test_traceability.py` (INSP-042) and this CR file (INSP-042, INSP-043). `tools/validate_docs.py` with HEAD at the trial merge also shows: INSP-042 on `docs/cm/tool-validation/TV-002-traceability.md@1fe6fb75` (now `94ae3af5`) and `tools/README.md@d61156d8`; INSP-043 on `tools/README.md@d61156d8`; INSP-051 (filed at `db43b82`, the software assurance pair of INSP-043, not named in this CR) on `tools/README.md@d61156d8` and this file at `d597899b`; and INSP-038 (TV-014, WP-PDR-07, `tool-validation-tv-014-to-tv-019.md`) on `tools/README.md@54f97c64`. Cause: `main` changed `tools/README.md` at `573f9f5` (LTspice paragraph) after the merge base `a3cacee`; the merge auto-merges to a new blob (`369ad8a1` in the trial) that no record has read. The software assurance record `code-tools-traceability-software-assurance.md` (pair of INSP-042) is still not filed | Author: in section 5 step 5 list INSP-042 (test module, TV-002, README, CR file), INSP-043 (README, CR file), INSP-051 (README, CR file) and INSP-038 (README, owner WP-PDR-07), and state that the delta reads the merged README blob, including the LTspice paragraph |
| IR-F3 (Minor) The `validate_docs.py` exit-0 criterion is not reachable by this CR alone | Independent reviewer agent (CR-011 impact review) | 2026-09-27 | Section 5 ends "`tools/validate_docs.py` exits 0 after step 6", and section 8 records 2 failures at the branch head. On `main` at `fefcf55` `validate_docs.py` already fails 8 records (63 passed): the CR-007 records, the SRR ADR and TS records, INSP-015 on `docs/cm/tool-validation/README.md` and `tools/toolchain.lock.md`, INSP-020 on `docs/requirements/README.md`. The merged tree fails the same 8. The step 6 deltas of INSP-015 and INSP-020 clear only the CR-011 part of their drift | Author: restate the criterion as "no `validate_docs.py` failure attributable to a CR-011 blob", and compare with the first parent of the merge commit, not `a3cacee` |
| IR-F4 (Minor) Plain-run severity of the hazard rows departs from 03 §8 with no carrier CR | Independent reviewer agent (CR-011 impact review) | 2026-09-27 | 03 §8 row 2 (lines 358 to 362) reads "Before PDR: `HAZARD_UNCONTROLLED` (violation: ...); promote `HAZARD_INVERSE` to a violation". The tool makes both plain-run warnings and violations only under `--gate` (`HAZARD_INVERSE` from SRR, `HAZARD_UNCONTROLLED` from PDR; `GATE_ERROR_FROM`). Section 1 discloses this, and the `--gate PDR` readiness run enforces both, so the control is not weakened at the gate. The plain run (gate G4) does not enforce what the baselined 03 states, and no owner ruling covers the difference. Section 4 sends 03 §8 to WP-PDR-17 as a writer task, but 03 is a class-CR CI, so aligning it needs a CR | Author: name the carrier (a CR-010 revision or a new CR from WP-PDR-17). Add to the section 7 proposed Conditions that the owner accepts the plain-run warning severity of the two hazard codes until that CR merges |
| IR-F5 (Minor) `related` is incomplete; the committed report goes stale at the merge | Independent reviewer agent (CR-011 impact review) | 2026-09-27 | `related` omits CR-015 and CR-016, which also edit 02 (trial merges on top of this branch: no conflict, 0 violations), and CR-010 (03 and RMM, IR-F4). The branch `docs/vv/traceability-report.md` and `traceability.json` were generated on HEAD `4411a09`. A plain run on the merged tree changes them (the CR row reads "15 files" instead of "6 files", and the HEAD line changes). The `rustos:` design-ref message also depends on where the checkout sits: from a worktree without `--rustos` it prints "rustos repository not found at ..." instead of "not in rustos at 2ec64c0" | Author: add CR-010, CR-015 and CR-016 to `related`. In section 5 step 7, regenerate the report in the merge commit from the main checkout (Table 4-1 row 18, Log). State the `--rustos` default-path dependence in the README or in a TV-002 limitation |

Items checked with no finding:

- Class II is correct under 05 §5.1 and §2. The tool cannot change a released image. No requirement, ICD, hazard, test case or filed evidence changes. `affected_cis` [2, 18, 28, 30, 40] match Table 4-1 rows for 02, the report, `tools/`, TV records and `tools/README.md`.
- `affected_paths` equal the branch contents: `git diff --stat main...cr/CR-011-traceability-pdr-rules` gives exactly the 18 listed paths (4275 insertions, 845 deletions). `git ls-tree 2b004b1` gives the blobs of sections 1 and 5 (`d4cde9f5`, `6ead5641`, `94ae3af5`). All five branch commits carry the `CR: CR-011` trailer (`git log --format='%(trailers:key=CR)'`).
- Effectivity: `target_release: none`, no released unit. `git merge-tree` against `main` merges cleanly (only `tools/README.md` auto-merged).
- Reviewer re-run on the merged tree:
  - `unittest tools.tests.test_traceability`: 87 tests OK. `discover -s tools/tests`: 514 tests, the only failure is `test_repository_exit_zero` on the pre-existing drift of IR-F3.
  - Plain run: 245 requirements, 173 test cases, 0 violations, 95 warnings.
  - `--gate PDR`: 379 violations, equal to section 4.
  - The mutation checks and the volatility dry run were not repeated. They belong to the section 9 verifier.
- No requirement or control is weakened beyond IR-F4. The dev-board change (`DEVBOARD_CASE_CLOSING`, 04 rule 7.3.12) tightens closure, and every other new rule adds a check.
- The plan's file ownership (5.3) is respected: `tools/traceability.py` has WP-PDR-06 as its only writer, and the 03, 04, 07, SEMP, lock and 01 follow-ons are sent to their writers in section 4.

Reviewer concurrence: concur with Class II and with the change. Do not concur with disposition until IR-F1 is resolved. **Impact review complete, with findings: 1 Major (IR-F1), 4 Minor (IR-F2 to IR-F5).** The CR stays Submitted. The author revises sections 1, 4 and 5 and re-submits for a re-check of IR-F1, and resolves the Minor findings in the same revision or states why not.

### 6.2 Author response to round 1 (revision 3, 2026-09-27)

| Finding | Response | Where |
|---|---|---|
| IR-F1 (Major) | Accepted. Section 1 names the plain-run violation codes with their sources. The comparison of the check catalogues of blobs `12de3545` and `d4cde9f5` finds seven, not six: `VAL_PHASE_MISSING` (04 rule 7.3.5) is also new and a violation. Author re-run on `main` at `a244b05` (which carries CR-008 revision 2) reproduces the reviewer's numbers: CR-008 208, and 164 when Approved; CR-009 5, and 0 when Approved. Sections 4 and 4.1 state the effect on CR-003, CR-006, CR-008, CR-009 and later CRs and the merge condition. The CR-008 `affected_ids` gap goes to the CR-008 author through its impact reviewer. `related` adds CR-003, CR-006, CR-008 and CR-009. Section 5 verification and section 9 re-run the plain run after each later CR merge | Revision 3: front matter; sections 1, 4, 4.1, 5, 7, 9, 11 |
| IR-F2 to IR-F5 (Minor) | Not resolved in this revision (plan rule C1: the author fixes the Major findings first). They stay open for the next revision or the disposition | none |

Re-check of IR-F1 by the round 1 reviewer or another independent invocation: pending.

### 6.3 Impact review round 2: delta re-check of IR-F1 (2026-09-27)

Reviewer: independent reviewer agent (CR-011 IR-F1 delta invocation). It authored no part of this CR, of WP-PDR-06, of TV-002 runs 6 and 7, of the revision 3 fix, or of the records INSP-042, INSP-043 or INSP-051. Date 2026-09-27. Scope: plan rule C1 delta. It verifies the Major fix only and does not re-review IR-F2 to IR-F5. Configuration reviewed: this file at blob `b636fc94` (revision 3, commit `0bbb1e2`, the only file in that commit; `git diff 86ff3b0 0bbb1e2` gives 35 insertions and 6 deletions); branch `cr/CR-011-traceability-pdr-rules` at `2b004b1`, unchanged, with tool blob `d4cde9f5`. `main` was at `9664775` when the trials ran. No commit after `0bbb1e2` changes this file, `docs/requirements/`, `docs/test_cases/` or the CR-008 and CR-009 files.

Method:

- `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` first (query: the 02 §8.2 check and gate columns of T-04, T-11 to T-13). Then `git show` and `grep` were used only to pin lines.
- The `CHECK_CATALOGUE` tuples of tool blobs `12de3545` and `d4cde9f5` were compared with a Python AST extraction.
- The source of `check_history`, `check_changes`, `approved_crs_listing`, `level_of` and the T-14 gate rule in `d4cde9f5` was read.
- One scratch detached worktree was used: `main` at `9664775` merged with `2b004b1`. In it the reviewer ran the plain run with `--rustos /Users/robinonsay/rust/rustos`, then merged each open CR branch on top as submitted, and for CR-008 and CR-009 again with the CR file `disposition` set to `Approved` and committed. Each trial was reset. The worktree was removed after use, no ref was kept, nothing was pushed, and LTspice was not run.

| Check | Result |
|---|---|
| R2-1 Section 1 plain-run codes | Verified. The catalogue comparison gives 22 new codes, with no existing code removed or re-graded. Eight new codes are `VIOLATION`: `BASELINE_ID_MISSING`, `TRANSITION_FORBIDDEN`, `CHANGE_UNCOVERED`, `CLOSED_NOT_INSTALLED`, `CASE_STALE`, `DEVBOARD_CASE_CLOSING`, `VAL_PHASE_MISSING` and `TBR_DUE_AT_GATE`. `TBR_DUE_AT_GATE` fires only when `project.gate is not None` (T-14 block). So seven are plain-run violations, as revision 3 states, and the author's correction of the round 1 count (six) is right. The fourteen other new codes are `WARNING`, and each is in `GATE_ERROR_FROM` at PDR. The sources hold: 02 §8.2 rows T-04, T-11, T-12 and T-13 have E in the `check` column, and T-14 states "At `gate R` ... is an Error". T-15, T-16, T-18, T-20 and T-22 have W in `check` and E@PDR in `gate` |
| R2-2 Scope of the history codes (section 1, section 4 row, section 4.1) | Verified against the code. `check_changes` compares the working tree with `baseline/srr` (`snapshot_at(tag)` against `snapshot_working`), so merge order does not avoid it. An id is covered when a CR in `docs/cm/cr/` whose `disposition` begins with `Approved` lists it in `affected_ids` (`cr_approved`, `approved_crs_listing`). An uncovered id is exempt only when every commit that touched it is editorial and nothing is uncommitted. A difference in editorial fields only is not Class I or II. L2 is skipped until a `baseline/pdr` tag exists (`LEVEL_BASELINE`). See IR-F6 (b) for the test-case level |
| R2-3 Trial numbers, section 4 and 4.1 | Reproduced on `main` at `9664775`, a later `main` than the author's `a244b05`. CR-011 alone: 245 requirements, 173 test cases, 0 violations, 96 warnings. CR-008 (`c629198`) as submitted: 208 `CHANGE_UNCOVERED`. With the disposition Approved: 164 (128 `REQ-SYS`, 36 `TC-SYS`), with the same field split as section 4.1 (57, 36, 17, 15, 13, 12, 8, 3, and 1 each for three combinations). REQ-SYS-002 `rationale` and REQ-SYS-004 `tbr` are both at `a47e992`. CR-009 (head now `56b4bcd`): 5 while Submitted, 0 when Approved. No other code fired in any trial. CR-010 `5cd87cf`, CR-012 `7784672`, CR-013 `41c588c`, CR-015 `7efd900`, CR-016 `33e0916` and CR-014 `fd000c6`: clean merge, 0 violations, 96 warnings each. `git branch` lists no `cr/CR-003-*` or `cr/CR-006-*`, which confirms "no branch" |
| R2-4 Merge condition and owner information | Verified. Section 4 Schedule, section 4.1 and the section 7 proposed Conditions each state the effect. Either merge order blocks the second CR while CR-008 `affected_ids` are incomplete. The condition is "0 violations on the merge commit". CR-008 completes `affected_ids` before its disposition, and the gap goes to the CR-008 author through its impact reviewer (this CR does not edit CR-008, which respects plan 5.3). The re-run after each later L0, L1 or `TC-SYS` merge is in section 5 verification and section 9. The owner disposing at B0 now sees the interaction |
| R2-5 `related` | Verified: CR-003, CR-006, CR-008 and CR-009 are added. CR-010, CR-015 and CR-016 are still absent (IR-F5, open) |
| R2-6 Scope of the revision | The diff touches only the front matter `related`, the revision 3 note, sections 1, 4, 4.1, 5 (verification paragraph), 6.2, 7 (Conditions), 9 (one row) and 11. No product file or branch commit changed. The Minor findings are left open with the rule C1 reason in section 6.2 |

New finding, round 2:

| Item | Reviewer (agent invocation) | Date | Finding | Resolution |
|---|---|---|---|---|
| IR-F6 (Minor) Revision 3 wording is narrower or older than the code and the branches | Independent reviewer agent (CR-011 IR-F1 delta) | 2026-09-27 | (a) Section 1 lists the W sources of the other new rules as "(T-15, T-16, T-18, T-20)". The three ICD codes (`ICD_NAME`, `ICD_UNPAIRED`, `ICD_SECTION4_MISMATCH`) come from T-22, which is also W in `check` and E@PDR, so T-22 is missing from that list. (b) Sections 1, 4 and 4.1 and the section 7 Conditions say `TC-SYS` case. `level_of` makes any test case that cites a `REQ-SYS-*` id an L1 case, whatever its module. On `main`, `TC-SW-TOOL-001` (REQ-SYS-127, 128, 133) is therefore under `CHANGE_UNCOVERED` from the merge, and a CR that edits it must list it. (c) Section 4.1 names CR-009 at `64eb688`, but the branch is now at `56b4bcd` (conops only; the trial result is unchanged). It says CR-014 at `367b3dd` conflicts with `main` and was not trialled, but the branch is now at `fd000c6`, merges cleanly and gives 0 violations. None of these changes the IR-F1 conclusion or the proposed Conditions | Author, in the next revision or with IR-F2 to IR-F5: add T-22 to the section 1 list. Replace "`TC-SYS` case" with "L1 test case (a case citing a `REQ-SYS` id, `TC-SYS` or any other module)" where the scope is stated. Refresh the section 4.1 heads for CR-009 and CR-014, or date the table to its trial `main` |

Reviewer concurrence, round 2: **IR-F1 (Major) is closed (Verified).** Every item of the round 1 resolution is done, and the reviewer reproduced the trial numbers independently on a later `main`. No Major finding is open. Open Minor findings: IR-F2 to IR-F5 (round 1) and IR-F6 (round 2), to be resolved in a later revision or carried to the disposition with the owner's agreement. The reviewer concurs with Class II, with the change, and with the CR proceeding to the owner disposition on the section 7 proposed Conditions. The CR stays Submitted, and section 5 steps 5 and 6 are still pending.

## 7. CCB disposition (owner)

| Field | Value |
|---|---|
| Decision | Approved |
| Class confirmed | II (proposed II; concurred in sections 6.1 and 6.3) |
| Date | 2026-09-28 |
| Conditions | None stated by the owner beyond the proposed conditions, adopted with the recommendation (lead SE reading): merge only after section 5 steps 4 to 6; merge only when the plain run on the merge commit gives 0 violations; each later L0, L1 or `TC-SYS` CR merges only with its disposition Approved on `main` and its changed ids in `affected_ids`, and the plain run is re-run after each such merge (section 4.1). The clause "CR-008 completes its `affected_ids` before its disposition" was not met: CR-008 is dispositioned in the same commit with R1-F2 open, so it becomes a condition on the CR-008 merge |
| Rationale | `tools/traceability.py` is under CR control since ACC-TRACE-001; the PDR rule set and options are dated at PDR by 02 and 04. Section 6.3: IR-F1 (Major) Verified; IR-F2 to IR-F6 Minor and open |
| Waiver scope (if Approved (waiver)) | n/a |
| Re-look trigger and re-look-by review (if Deferred) | |
| Source | Chat transcription by Claude (configuration manager) on 2026-09-28. The presenter asked the owner to approve CR-007 to CR-016, the SRR lien fixes that passed their impact reviews (recommendation: approve all ten). Owner statement, verbatim: "Um, and then, yeah, I think you're uh, good to continue." The lead SE reads it as approval of item 1 as recommended, with the branches to merge after the section 9 checks (`docs/plan/status/status-2026-09-28.md` section 1, commit `e288add`, which transcribes the full statement); the owner is asked to correct any line |

Disposition history (append only):

| Date | Decision | New target | Source |
|---|---|---|---|
| 2026-09-28 | Approved | none | owner, `status-2026-09-28.md` section 1 (`e288add`), transcribed by Claude (configuration manager) |

## 8. Implementation record

| Commit | Files | Trailer check (`CR: CR-011` present) |
|---|---|---|
| `4411a09` | tool, tests, fixtures, README, 02 | yes |
| `89fac92` | TV-002, evidence, `docs/vv/traceability-report.md`, `traceability.json` | yes |
| `4774562` | 02 §8.5 evidence line, TV-002 limitation 6 | yes |
| `709e95f` | `tools/tests/test_traceability.py` (`RegressionSetTests`, INSP-043 finding-1) | yes |
| `2b004b1` | TV-002 purpose 9, limitation 9, run 7, ACC-TRACE-002 scope; `evidence/traceability-2026-09-27-r7.py`, `.log.txt` | yes |

Traceability report after implementation: `docs/vv/traceability-report.md` on the branch (plain run, 0 violations, 95 warnings; not regenerated after `4411a09`, since the tool and the repository data it reads are unchanged, and run 7 repository run R-4 equals R-3); renders regenerated: none. Author check of the branch head `2b004b1` (2026-09-27, scratch worktree, removed after use): `unittest discover -s tools/tests` 477 tests, 1 failure (`test_validate_docs.RepositoryTests.test_repository_exit_zero`), 3 skipped; `tools/validate_docs.py` 48 passed, 2 failed (INSP-015 and INSP-020, the record drift of §4 Verification and step 6), equal to INSP-043 iteration 2 check V9.

## 9. Verification of implementation

| Impact item | Planned closure (from §4/§5) | Evidence (report path, TC id, analysis file) | Result |
|---|---|---|---|
| Verification | TV-002 runs 6 and 7 re-run by the reviewer | `docs/cm/tool-validation/TV-002-traceability.md` §4; `evidence/traceability-2026-09-27-r6.log.txt`, `evidence/traceability-2026-09-27-r7.log.txt`; INSP-043 checks V3 to V9 | pending |
| Documentation | 02 and README consistent with the tool | the three records of section 5 step 5 | pending |
| Requirements and traceability | Plain run 0 violations on the CR-011 merge commit and after each later merge of CR-003, CR-006, CR-008, CR-009 or a later L0, L1 or `TC-SYS` CR (section 4.1) | plain-run summary line and merge SHA per merge | pending |

Independent verifier (agent invocation): pending.

Configuration manager pre-merge check (2026-09-28; performed at the disposition, not the independent verification, which stays pending). Method: `git merge-tree --write-tree` of the branch head with `main` (no conflict), then a trial `git merge --no-ff` in a detached scratch worktree of `main` (discarded afterwards, no ref kept), `tools/validate_docs.py` and `tools/traceability.py --report-only` on the trial merge, and the failure set compared with the baseline. Baseline on `main` at `e288add`: `tools/validate_docs.py` 102 passed, 8 failed (all record drift already on `main`: SRR `adrs-001-to-025.md`, `process-02-requirements-and-traceability.md`, `tool-validation-tv-001-to-tv-010.md`, `trade-studies-ts-001-ts-002.md`, `trade-study-ts-002-software-assurance.md`; PDR `cm-plan-05-software-assurance.md`, `configuration-status.md`, `lessons-learned.md`); `python -m unittest discover -s tools/tests` 596 run, 1 failure (`test_repository_exit_zero`, the same drift), 14 skipped; `tools/traceability.py --report-only` 0 violations, 2 warnings. Branch head `2b004b1`. Trial merge: `validate_docs.py` 101 passed, 9 failed; one new failure, `docs/reviews/PDR/checklists/tool-validation-tv-015-to-tv-019.md` (INSP-088, APPROVED, names `tools/README.md@a5e9cab6`; the branch changes it to `c872e3d8`). Plain run of the branch tool on the trial merge: 245 requirements, 173 test cases, 0 violations, 96 warnings (section 4.1 row "CR-011 alone"). Merge held: section 5 step 5 (INSP-042 carries `assurance_verdict: pending`; INSP-042 and INSP-043 pin this file at a superseded blob) and step 6 (INSP-015 and INSP-020 deltas) are not done; INSP-088 needs a delta on the new `tools/README.md` blob (the CR-014 step 7a practice).

## 10. Closure

| Field | Value |
|---|---|
| Owner merge approval | 2026-09-28, with the disposition: "their branches merge after the section 9 checks" (lead SE reading, `docs/plan/status/status-2026-09-28.md` section 1). Merge held at the disposition: see the section 9 configuration manager pre-merge check |
| Merge commit | pending |
| Waiver entered in CSA item 12 and affected VDDs | n/a |
| CSA regenerated | pending |
| Date closed | |

## 11. History

| Date | State | By | Commit on main | Note |
|---|---|---|---|---|
| 2026-09-27 | Submitted | Claude (tool owner, WP-PDR-06) | this commit | Implementation on the branch at `4774562` submitted with the CR for the section 6 review; merge waits for the disposition (05 §5.2) |
| 2026-09-27 | Submitted (revision 2) | Claude (tool owner, WP-PDR-06) | this commit | Branch head `2b004b1` after the INSP-043 finding-1 fix (run 7); CR file brought up to date before the section 6 review; no product file changed |
| 2026-09-27 | Submitted (revision 3) | Claude (tool owner, WP-PDR-06) | this commit | Section 6.1 IR-F1 (Major) resolved: section 1 plain-run codes, section 4 and 4.1 effect on open CRs and merge condition, `related`, section 5 and 9 re-runs; IR-F1 re-check pending; Minor findings open |
| 2026-09-28 | Dispositioned (Approved) | Claude (configuration manager), transcribing the owner | the commit that records this row (`Refs: CR-011`) | Owner approval of CR-007 to CR-016 as recommended (`status-2026-09-28.md` section 1); merge held at the disposition: section 5 steps 5 and 6 not done; new INSP-088 drift on `tools/README.md` (section 9 pre-merge check) |
