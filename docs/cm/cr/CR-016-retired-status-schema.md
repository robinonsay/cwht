---
id: CR-016
title: Add the Retired status to the requirement and test-case schemas
status: Submitted
class: II
originator: Claude
date_opened: 2026-09-27
phase: B
configuration_at_origination: baseline/srr (tag on 779f93f); change set prepared on branch base 11b1b1d (main); branch head 33e0916
baseline_affected: baseline/srr
affected_cis: [2, 9]
affected_paths: [docs/requirements/schema.json, docs/test_cases/schema.json, docs/process/02-requirements-and-traceability.md]
affected_ids: []
related: [CR-015, INSP-020, CR-011]
target_release: none
branch: cr/CR-016-retired-status-schema
disposition: null
disposition_date: null
relook_trigger: null
relook_by: null
merge_sha: null
date_closed: null
---

# CR-016: Add the Retired status to the requirement and test-case schemas

Template: `docs/templates/change-request.md`. Process: `docs/process/05-configuration-and-data-management.md` §5.1 to §5.3. File location: this file, committed on `main` with `Refs: CR-016`. Status: **Submitted**. Work package: WP-PDR-12 of `docs/plan/pdr-work-plan.md` (revision 2), the retired-status schema CR "drafted for PDR" (plan register PCR-3; gate reader P-17; 02 section 14 CI-3). **Effectivity:** after `baseline/pdr` unless the owner rules otherwise (register PCR-3; plan section 7 row "PCR-3 retired-status schema change"). Nothing at freeze F1 waits on it.

**Where the change is.** The product change is prototyped on `cr/CR-016-retired-status-schema`, head `33e0916` on base `11b1b1d` (`cd5da22`, then `33e0916`, which drops a status migration so that no requirement changes status). The exact before and after text is `git diff 11b1b1d 33e0916`. Nothing merges before the owner's disposition and the section 9 verification.

Frozen products for review (PDR work plan rule C2), at branch commit `33e0916`:

| File (Table 4-1 row) | Blob on `main` at `11b1b1d` | Blob at `33e0916` |
|---|---|---|
| `docs/requirements/schema.json` (row 9) | as on `main` | `32d0a2516d91a635f5690790944db334a97aa987` |
| `docs/test_cases/schema.json` (row 9) | as on `main` | `f8eae82a3d0684b4703b90cddf82d7042f2ddb87` |
| `docs/process/02-requirements-and-traceability.md` (row 2) | `fcdc5445` (the `baseline/srr` blob) | `09d6df9c5554e4270f54d05c22eaa612079adb98` |

## 1. Description of the change

### 1.1 Schemas (Table 4-1 row 9)

| File | Before | After |
|---|---|---|
| `docs/requirements/schema.json`, `requirements[].status.enum` | `["Draft", "Active", "Verified", "Closed"]` | `["Draft", "Active", "Verified", "Closed", "Retired"]` |
| `docs/test_cases/schema.json`, `test_cases[].status.enum` | `["Draft", "Active", "Passed", "Failed", "Blocked"]` | `["Draft", "Active", "Passed", "Failed", "Blocked", "Retired"]` |

No other schema field changes. The L0 schema already carries `Retired` with `retired_by` and is not touched.

### 1.2 `docs/process/02-requirements-and-traceability.md` (Table 4-1 row 2)

| Location | Before (summary) | After (summary) |
|---|---|---|
| §2.3 tag row `retired` | "the interim retirement marker of section 11.3" | part of the interim marker of a requirement retired before CR-016; never added to a new retirement |
| §8.2 T-10 | a retired requirement is "status `Closed` with tag `retired`" | status `Retired`, or the interim form |
| §8.2 T-19 | "status `Closed` and tag `retired` until a schema CR adds `Retired`"; tag on any status other than `Closed` is an error; a retired case is `Blocked` with the `Retired by ` setup | status `Retired`, or the interim form; the tag on a status other than `Closed` or `Retired` is an error; a retired case is `Retired`, or the interim `Blocked` form, with the `Retired by ` setup |
| §8.3 requirement transitions | retirement is "`Closed` with tag `retired`" | retirement is `Retired`; a retired requirement changes to nothing, in either form |
| §8.4 test-case transitions | retirement is `Blocked` with the `Retired by ` setup, "the interim marker until a schema CR adds `Retired`" | retirement is `Retired` with the `Retired by ` setup; a retired case changes to nothing, in either form |
| §11.3 lead paragraph, table and procedure step 1 | the schemas are not changed by this process; the interim markers apply until the CR; step 1 sets the interim marker | CR-016 added `Retired`; every retirement after it sets `status: "Retired"`; entries retired under the interim markers keep them for the life of the repository (a retired entry never changes status, §8.3), and the tool recognizes both forms (T-19). On 2026-09-27 the interim-marked entries are REQ-SYS-016 and REQ-SYS-123, and no test case is retired |

02 section 14 row CI-3, which points to this CR, is changed by CR-015, not here.

## 2. Reason

- Charter section 6: "a retired item keeps its ID with status *Retired* where its schema has that status, otherwise status *Closed* with tag `retired`". The requirement and test-case schemas lack the status, so every retirement uses the interim markers of 02 §11.3, which overload `Closed` (accepted at SAR, 04 §5.3) and `Blocked` (cannot run) with a second meaning read only from a tag or a `setup` prefix.
- 02 §11.3 (baselined): "Claude drafts that CR for the PDR package and Robin decides it at PDR (05 Table 4-1 row 9 puts the schemas under CR from SRR)". 02 §14 CI-3: "the schema CR is drafted for PDR". PDR work plan WP-PDR-12 outputs and register PCR-3.
- Workaround while the CR is open: the interim markers, which `tools/traceability.py` already recognizes (T-19; `Requirement.is_retired` and the test-case equivalent accept status `Retired` and the interim forms).

## 3. Alternatives considered

| Alternative | Why rejected or deferred |
|---|---|
| Keep the interim markers permanently | The charter's first choice is status *Retired* where the schema has it; `Closed` and `Blocked` keep a double meaning that every reader and reviewer must decode from a tag or a text prefix |
| Migrate REQ-SYS-016 and REQ-SYS-123 to `Retired` in the same change | A status change of an L1 requirement is Class I (02 §10.2) and a retired entry never changes status (02 §8.3); the first prototype `cd5da22` carried a one-time migration, dropped at `33e0916`. The tool treats both forms alike, so nothing is gained by moving them |
| Make it effective before `baseline/pdr` | The allocated baseline is being written in waves 2a and 2b; a status vocabulary change during that work invites mixed forms in the new L2 files. The owner may rule an earlier effectivity at the disposition |
| Add a `retired_by` field to requirements and test cases, as the L0 schema has | The reason text with `Retired by CR-NNN` is already required and checked (T-19); a second field would store the same link twice (02 §7, store once) |

## 4. Impact assessment (CM plan §5.3)

| Field | Assessment (numbers, IDs, paths) |
|---|---|
| Performance margins | None: no TPM, MOP or budget |
| Safety | None: no hazard or control changes; a retired hazard-control requirement is excluded from T-08 coverage exactly as today (the tool already reads both forms). Hazard analysis re-issue: no. RF exposure evaluation change: no |
| Risk | None: no RSK added, closed or re-scored |
| Software classification and tailoring | None: no `rmm.json`, 03 or compliance-matrix row changes |
| Interfaces | None: no ICD |
| Operations and ConOps | None |
| Cybersecurity | None |
| Verification | None: no TC added, modified or invalidated; no case is retired today. A case retired after the merge uses status `Retired` |
| Cost | None |
| Schedule | None: effective after `baseline/pdr`; §6 review Thu 10-01 and disposition at B2 Fri 10-02 (OD-37); if late, presented at the PDR session (register "If late") |
| Requirements and traceability | None: no REQ, TC, NGO, MOE or CON changes; REQ-SYS-016 and REQ-SYS-123 keep their interim markers; volatility contribution 0. `tools/traceability.py --report-only` on the branch: 245 requirements, 173 test cases, 0 violations, 2 warnings, as on `main`; the report files were restored with `git checkout` |
| Regulatory | None |
| Documentation | Changed by this CR: the three paths of the front matter. Consequential text for other writers at implementation (PDR work plan §5.3 and the writers in force after `baseline/pdr`): `docs/process/04-verification-and-validation.md` §3 (test-case status list and the "Retired" bullet, lines 133 and 140 at `11b1b1d`) and §7.1 and §7.3 rule 2 (the 04 writer); `docs/process/05-configuration-and-data-management.md` §4.3 identification table (the 05 writer); the `RETIRED_TAG` comment and module docstring of `tools/traceability.py` (the tool owner; no behavior change). Each is a CR hunk of its own writer or rides in this CR's merge by agreement of that writer |
| Released units | None |

Classification rationale: Class II. The change modifies configuration documentation (two schemas and a process document) without impact to form, fit, function, interchangeability, interfaces, safety, verification evidence or operator procedures (05 §2, Class II definition), and changes no requirement or test case. The register proposes Class II "reviewed, since it touches the requirement schema"; the section 6 review is held (rule C6).

## 5. Implementation plan

| Step | Artifact and path | Responsible | Done (SHA) |
|---|---|---|---|
| 1 | Prototype on `cr/CR-016-retired-status-schema` (the three paths of the front matter) | Claude, WP-PDR-12 author | `cd5da22`, `33e0916` |
| 2 | This CR file on `main`, state Submitted | Claude, WP-PDR-12 author | the commit that adds this file (`Refs: CR-016`) |
| 3 | Section 6 impact review, including the frozen blobs of the table above | Independent reviewer that did not author this CR (register slot Thu 10-01) | |
| 4 | Owner disposition (section 7), OD-37 at B2 Fri 10-02 | Owner | |
| 5 | After `baseline/pdr` (or the effectivity the owner rules): merge `main` into the branch (CR-015 and CR-011 also change 02; `git merge-tree` reports no conflict at `33e0916`), re-run `tools/validate_docs.py`, `tools/traceability.py --report-only` and the unit tests, have the consequential hunks of section 4 "Documentation" written by their writers, then `git merge --no-ff cr/CR-016-retired-status-schema` with message `merge(CR-016): <title>` | Claude (CM function), with the owner's merge approval | |
| 6 | Section 9 verification; INSP-020 (02) delta iteration if 02 is then under a PDR record | Independent reviewer | |

Verification of the implementation (what the independent reviewer will check): the diff touches exactly the paths agreed at step 5; both enums hold `Retired`; `tools/validate_docs.py` validates every requirement and test-case file under the new schemas with no new failure; `tools/traceability.py` reports no new violation and still counts REQ-SYS-016 and REQ-SYS-123 as retired; a seeded check (a scratch copy with one requirement and one case set to `Retired` with a `Retired by CR-016` reason) gives no `RETIRED_INCONSISTENT`.

## 6. Independent review of the impact assessment

Required by PDR work plan rule C6 (and the register: "reviewed, since it touches the requirement schema") before the owner's disposition: not yet performed. The reviewer must not have authored this CR or the branch change.

| Item | Reviewer (agent invocation) | Date | Finding | Resolution |
|---|---|---|---|---|
| | | | | |

Reviewer concurrence: pending.

## 7. CCB disposition (owner)

| Field | Value |
|---|---|
| Decision | Not dispositioned |
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

| Commit | Files | Trailer check (`CR: CR-016` present) |
|---|---|---|
| `cd5da22` (branch `cr/CR-016-retired-status-schema`, prototype) | the three paths of the front matter | yes |
| `33e0916` (branch; migration dropped) | `docs/process/02-requirements-and-traceability.md` | yes |

Traceability report after implementation: pending (step 5); renders regenerated: none.

## 9. Verification of implementation

| Impact item | Planned closure (from §4/§5) | Evidence (report path, TC id, analysis file) | Result |
|---|---|---|---|
| Tools unaffected (prototype) | `tools/validate_docs.py` and the unit tests show no new failure against the base | Author run in a worktree of `cd5da22`, with and without the change (`git stash`): `validate_docs.py` fails the same 5 records either way, all SRR records failing the drift rule for products changed on `main` after their review (`adrs-001-to-025.md`, `process-02-requirements-and-traceability.md`, `tool-validation-tv-001-to-tv-010.md`, `trade-studies-ts-001-ts-002.md`, `trade-study-ts-002-software-assurance.md`); unit tests 461 run, 1 failure (`RepositoryTests.test_repository_exit_zero`, the same drift), 16 skipped; `traceability.py --report-only` exit 0, 245 requirements, 173 test cases, 0 violations, 2 warnings (author run, 2026-09-27) | Pending independent verification |
| Merge feasibility | No conflict with CR-015 and CR-011, which also change 02 | `git merge-tree --write-tree` of `33e0916` with `cr/CR-015-process-liens-01-02-08`, `cr/CR-011-traceability-pdr-rules` and `cr/CR-008-srr-liens-l1-and-tc-sys`: no conflict (author run, 2026-09-27) | Pending independent verification |

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
| 2026-09-27 | Submitted | Claude (WP-PDR-12 author) | the commit that adds this file | Created with the impact assessment complete; product change prototyped on `cr/CR-016-retired-status-schema` at `33e0916`; section 6 review (rule C6) pending; effective after `baseline/pdr` unless ruled otherwise |

## 12. Questions for the owner (answer with the disposition)

| # | Question | Recommendation |
|---|---|---|
| Q1 | Approve CR-016, which adds the status `Retired` to the requirement and test-case schemas and makes it the only form of a new retirement? | Approve, after the section 6 review reports no Major finding |
| Q2 | Confirm Class II | Confirm: two schema enums and the 02 retirement text; no requirement or test case changes |
| Q3 | Effectivity: after `baseline/pdr`, or now? | After `baseline/pdr`, so the allocated baseline is written in one retirement vocabulary |
| Q4 | Keep REQ-SYS-016 and REQ-SYS-123 in their interim form (`Closed` with tag `retired`)? | Keep: a retired entry never changes status, and the tool reads both forms |
