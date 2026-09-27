---
id: CR-011
title: Add the PDR rule set and the --gate, --volatility and --fix-children options to tools/traceability.py
status: Submitted
class: II
originator: Claude
date_opened: 2026-09-27
phase: B
configuration_at_origination: baseline/srr (tag on 779f93f); main at a3cacee; branch cr/CR-011-traceability-pdr-rules at 4774562
baseline_affected: baseline/srr
affected_cis: [2, 18, 28, 30, 40]
affected_paths: [tools/traceability.py, tools/tests/test_traceability.py, tools/tests/test_tools.py, tools/tests/fixtures/valid_project/docs/requirements/sys/requirements.json, tools/tests/fixtures/valid_project/docs/requirements/sys/requirements.md, tools/tests/fixtures/valid_project/firmware/cwht-core/src/keyer/straight.rs, tools/tests/fixtures/valid_project/firmware/cwht-core/src/keyer/iambic.rs, tools/tests/fixtures/valid_project/firmware/cwht-core/src/keyer/config.rs, tools/tests/fixtures/valid_project/hardware/kicad/tx-pa.kicad_sch, tools/README.md, docs/process/02-requirements-and-traceability.md, docs/cm/tool-validation/TV-002-traceability.md, docs/cm/tool-validation/evidence/traceability-2026-09-27-r6.py, docs/cm/tool-validation/evidence/traceability-2026-09-27-r6.log.txt, docs/cm/tool-validation/evidence/traceability-2026-09-27-r7.py, docs/cm/tool-validation/evidence/traceability-2026-09-27-r7.log.txt, docs/vv/traceability-report.md, docs/vv/traceability.json]
affected_ids: [TV-002, ACC-TRACE-001, ACC-TRACE-002, INSP-015, INSP-020, RFA-SRR-007]
related: [CR-002, CR-007, CR-012, RFA-SRR-007, INSP-015, INSP-020, TV-009]
target_release: none
branch: cr/CR-011-traceability-pdr-rules
disposition: null
disposition_date: null
relook_trigger: null
relook_by: null
merge_sha: null
date_closed: null
---

# CR-011: Add the PDR rule set and the --gate, --volatility and --fix-children options to tools/traceability.py

Template: `docs/templates/change-request.md`. Process: `docs/process/05-configuration-and-data-management.md` §5. This file is committed on `main`; the branch `cr/CR-011-traceability-pdr-rules` carries the product changes. Work package: WP-PDR-06 of `docs/plan/pdr-work-plan.md` (revision 2). The plan's register of phase CRs (section 6.2) does not list this CR; it is raised because `tools/traceability.py` has been under CR control since its accreditation ACC-TRACE-001 (05 Table 4-1 row 28, "Accreditation puts the tool under CR control"), and every non-editorial change to a class-CR CI after its CR-from event is a CR (05 §5.1).

**Revision 2 (2026-09-27).** The branch head moved from `4774562` to `2b004b1` for the INSP-043 finding-1 (Major) fix: `709e95f` adds `RegressionSetTests` to `tools/tests/test_traceability.py` (blob `95f1719b` becomes `6ead5641`), and `2b004b1` adds TV-002 purpose 9 (`--regression`), run 7 and its evidence (`traceability-2026-09-27-r7.py`, `.log.txt`). The tool blob `d4cde9f5` and every other branch file are unchanged. This revision states run 7 in `affected_paths`, §4 Verification, §5, §8, §9 and §11, and names in §5 step 5 the record deltas the moved blobs require. It changes no product file.

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

Plain-run behavior of every existing code is unchanged, except that a dev-board case no longer counts as closing (04 rule 7.3.12). New PDR rules follow the `check` column of 02 §8.2: warnings in a plain run, violations under `--gate`. `HAZARD_UNCONTROLLED` is a plain-run warning, not the violation 03 §8 names, because the software L2 requirements that close it are PDR products (WP-PDR-35); it is a violation under `--gate` from PDR.

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
| Schedule | Needed before the PDR readiness declaration (plan B4, Tue 10-06); the output becomes accredited evidence only after the reviews of section 5 steps 5 and 6, the disposition, the merge and ACC-TRACE-002 |
| Requirements and traceability | None added, modified or retired; volatility contribution 0 (`--volatility --from baseline/srr --dry-run`: V 0.0 % for L1, L2 and software). Orphans or uncovered requirements created: none (plain run 0 violations) |
| Regulatory | None |
| Documentation | `tools/README.md`, 02 §8.1, §8.2, §8.5, §10.4 (on the branch). Not on the branch, sent to their writers: 03 §8 and the RMM SWE-052 row (WP-PDR-17), 04 §7.4 rows 7.3.2, 7.3.4, 7.3.5, 7.3.6, 7.3.11, 7.3.12 (WP-PDR-13), `tools/toolchain.lock.md` §1.1 and §5 rows for runs 6 and 7 (WP-PDR-09; INSP-043 finding-4 lien), `docs/cm/tool-validation/README.md` TV-002 index row (tool owner; INSP-043 finding-4 lien), SEMP §4.3 allocation row and App. F F-06 (the SEMP writer, WP-PDR-13 or WP-PDR-46), 01 §3.1 item 2 (`--gate <REVIEW>`, WP-PDR-12) |
| Released units | None |

Classification rationale: Class II. The change modifies a class B evidence-generating tool and the documentation that describes it; it changes no requirement, interface, safety control, verification evidence already filed, or operator procedure, and the tool cannot change a released image (05 §5.1, "Version change of an Accredited tool": Class I only if the tool can change a released image). The independent review of section 6 is held anyway under plan rule C6 (every CR raised in the PDR phase is reviewed before disposition).

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

Verification of the implementation (what the independent reviewer checks): TV-002 section 3 re-run on an export of the branch head gives 235 tests (run 7 selection; 229 with the run 6 selection), 0 skipped, OK; the mutation checks of TV-002 runs 6 and 7 (step 3 and step 3b) are repeatable; each code against its source text (02 §8.2 to §8.5, §10.2 to §10.4; 04 §7.3 rules 4, 5, 11, 12 and §8.2; 03 §8; SRR memo §9 condition 5; RFA-SRR-007 L-7); a plain run on the merged `main` gives 0 violations; `tools/validate_docs.py` exits 0 after step 6.

## 6. Independent review of the impact assessment

Required by plan rule C6 (lesson L4), although a Class II CR that touches no requirement, ICD, hazard or test case would not need it (05 §5.2).

| Item | Reviewer (agent invocation) | Date | Finding | Resolution |
|---|---|---|---|---|
| Pending | | | | |

Reviewer concurrence: pending.

## 7. CCB disposition (owner)

| Field | Value |
|---|---|
| Decision | Pending |
| Class confirmed | Pending (proposed II) |
| Date | |
| Conditions | Proposed: merge only after section 5 steps 4 to 6 |
| Rationale | |
| Waiver scope (if Approved (waiver)) | n/a |
| Re-look trigger and re-look-by review (if Deferred) | |
| Source | |

Disposition history (append only):

| Date | Decision | New target | Source |
|---|---|---|---|
| | | | |

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

Independent verifier (agent invocation): pending.

## 10. Closure

| Field | Value |
|---|---|
| Owner merge approval | pending |
| Merge commit | pending |
| Waiver entered in CSA item 12 and affected VDDs | n/a |
| CSA regenerated | pending |
| Date closed | |

## 11. History

| Date | State | By | Commit on main | Note |
|---|---|---|---|---|
| 2026-09-27 | Submitted | Claude (tool owner, WP-PDR-06) | this commit | Implementation on the branch at `4774562` submitted with the CR for the section 6 review; merge waits for the disposition (05 §5.2) |
| 2026-09-27 | Submitted (revision 2) | Claude (tool owner, WP-PDR-06) | this commit | Branch head `2b004b1` after the INSP-043 finding-1 fix (run 7); CR file brought up to date before the section 6 review; no product file changed |
