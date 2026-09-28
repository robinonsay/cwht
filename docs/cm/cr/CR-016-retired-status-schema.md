---
id: CR-016
title: Add the Retired status to the requirement and test-case schemas
status: Dispositioned
class: I
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
disposition: Approved
disposition_date: 2026-09-28
relook_trigger: null
relook_by: null
merge_sha: null
date_closed: null
---

# CR-016: Add the Retired status to the requirement and test-case schemas

Template: `docs/templates/change-request.md`. Process: `docs/process/05-configuration-and-data-management.md` §5.1 to §5.3. File location: this file, committed on `main` with `Refs: CR-016`. Status: **Assessed**. Work package: WP-PDR-12 of `docs/plan/pdr-work-plan.md` (revision 2), the retired-status schema CR "drafted for PDR" (plan register PCR-3; gate reader P-17; 02 section 14 CI-3). **Effectivity:** after `baseline/pdr` unless the owner rules otherwise (register PCR-3; plan section 7 row "PCR-3 retired-status schema change"). Nothing at freeze F1 waits on it.

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

**Re-validation and migration (05 Table 4-1 row 9).** Re-validation this CR triggers: `tools/validate_docs.py` over every data file validated against the two schemas, which at `33e0916` are `docs/requirements/sys/requirements.json`, `docs/requirements/tx/requirements.json`, `docs/requirements/sw/sw-keyer/requirements.json`, `docs/templates/requirements.example.json`, `docs/test_cases/sys/test_cases.json`, `docs/test_cases/tx/test_cases.json`, `docs/test_cases/sw-keyer/test_cases.json`, `docs/test_cases/sw-tool/test_cases.json` and `docs/templates/test_cases.example.json`, plus every requirement or test-case file added on `main` before the merge (the L2 files of waves 2a and 2b). Migration statement: no data file is affected, so the implementation carries no data migration. Both enums only widen (one value added, none removed or renamed, no required field added), so every entry that validates under the `baseline/srr` schemas validates unchanged under the new ones; all nine files above pass the `33e0916` schemas (author check with `jsonschema` on the committed blobs, 2026-09-27; the INSP-061 seeded and unseeded runs agree). The schema copies under `tools/tests/fixtures/` are fixtures of Table 4-1 row 28 (row 9 excludes them) and are not changed. REQ-SYS-016 and REQ-SYS-123 keep their interim markers (section 3, Q4), which is not a migration: their status stays `Closed`.

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
| Schedule | None: effective after `baseline/pdr`; §6 review Thu 10-01 and disposition at B2 Fri 10-02 (OD-37), inside the Class I cycle-time target of 05 §5.2 (next review or 14 days); if late, presented at the PDR session (register "If late") |
| Requirements and traceability | None: no REQ, TC, NGO, MOE or CON changes; REQ-SYS-016 and REQ-SYS-123 keep their interim markers; volatility contribution 0. `tools/traceability.py --report-only` on the branch: 245 requirements, 173 test cases, 0 violations, 2 warnings, as on `main`; the report files were restored with `git checkout` |
| Regulatory | None |
| Documentation | Changed by this CR: the three paths of the front matter. Consequential text for other writers at implementation (PDR work plan §5.3 and the writers in force after `baseline/pdr`): `docs/process/04-verification-and-validation.md` §3 (test-case status list and the "Retired" bullet, lines 133 and 140 at `11b1b1d`) and §7.1 and §7.3 rule 2 (the 04 writer); `docs/process/05-configuration-and-data-management.md` §4.3 identification table (the 05 writer); the `RETIRED_TAG` comment and module docstring of `tools/traceability.py` (the tool owner; no behavior change). Each is a CR hunk of its own writer or rides in this CR's merge by agreement of that writer |
| Released units | None |

Classification rationale: Class I. 05 Table 4-1 row 9 (Schemas, class CR from SRR) states that a schema CR "is Class I when it adds or changes a required field or an enum". This CR adds the value `Retired` to two `status` enums, so it is Class I by that rule, although the change has no impact on form, fit, function, interfaces, safety, verification evidence or operator procedures and changes no requirement or test case (the 05 §2 Class II definition would otherwise fit). The baselined CM rule governs; the plan register's proposal "II (reviewed, since it touches the requirement schema)" (PCR-3) is a planning estimate and does not override it (INSP-061 finding-1). Row 9's two further clauses are met as follows: the migration clause by the migration statement of section 1.1 (no data file is affected; no migration is carried), and the atomic-commit clause by step 5 (the merge commit carries both schemas, names the re-validated data files, and states the `tools/validate_docs.py` result and the unit-test count). The independent review of the impact assessment, mandatory for Class I (05 §5.2, state Assessed) and required by rule C6, is section 6.

## 5. Implementation plan

| Step | Artifact and path | Responsible | Done (SHA) |
|---|---|---|---|
| 1 | Prototype on `cr/CR-016-retired-status-schema` (the three paths of the front matter) | Claude, WP-PDR-12 author | `cd5da22`, `33e0916` |
| 2 | This CR file on `main`, state Submitted | Claude, WP-PDR-12 author | the commit that adds this file (`Refs: CR-016`) |
| 3 | Section 6 impact review, including the frozen blobs of the table above | Independent reviewer that did not author this CR (register slot Thu 10-01) | |
| 4 | Owner disposition (section 7), OD-37 at B2 Fri 10-02 | Owner | |
| 5 | After `baseline/pdr` (or the effectivity the owner rules): merge `main` into the branch (CR-015 and CR-011 also change 02; `git merge-tree` reports no conflict at `33e0916`), re-run `tools/validate_docs.py`, `tools/traceability.py --report-only` and the unit tests, have the consequential hunks of section 4 "Documentation" written by their writers, then `git merge --no-ff cr/CR-016-retired-status-schema` with message `merge(CR-016): <title>`. Per 05 Table 4-1 row 9 the merge is the one commit that carries both schemas and every data file they affect (none, section 1.1), and its message body states: the re-validated data files (the list of section 1.1 as it stands at the merge head); the `tools/validate_docs.py` result at the merge head (exit status, the pass count of those data files, and each failing file by path, which must be only failures that `main` shows before the merge and none of them a requirement or test-case file); and the unit-test count (tests run, failures, errors, skipped). If any requirement or test-case file then fails either schema, the merge waits: its migration is committed on the branch with `CR: CR-016` first, so that the merge still carries it (row 9) | Claude (CM function), with the owner's merge approval | |
| 6 | Section 9 verification; INSP-020 (02) delta iteration if 02 is then under a PDR record | Independent reviewer | |

Verification of the implementation (what the independent reviewer will check): the diff touches exactly the paths agreed at step 5; both enums hold `Retired`; `tools/validate_docs.py` validates every requirement and test-case file under the new schemas with no new failure; `tools/traceability.py` reports no new violation and still counts REQ-SYS-016 and REQ-SYS-123 as retired; a seeded check (a scratch copy with one requirement and one case set to `Retired` with a `Retired by CR-016` reason) gives no `RETIRED_INCONSISTENT`.

## 6. Independent review of the impact assessment

Mandatory for this Class I CR (05 §5.2, state Assessed) and required by PDR work plan rule C6 before the owner's disposition. Iteration 1 is INSP-061 (`docs/reviews/PDR/checklists/cr-016-retired-status-schema.md`, NEEDS CHANGES, 1 Major); its entry here follows the iteration 2 delta. The reviewer must not have authored this CR or the branch change.

| Item | Reviewer (agent invocation) | Date | Finding | Resolution |
|---|---|---|---|---|
| INSP-061 iteration 1: class (finding-1, Major) | `reviewer:WP-PDR-12-iteration-1` | 2026-09-27 | Class II proposed where 05 Table 4-1 row 9 makes an enum change Class I; row 9 migration and commit-message clauses unstated | Fixed in revision 2 (CR blob `987f72e2`, `9bda072`); Verified at INSP-061 iteration 2 |
| INSP-061 iteration 1: 02 text (finding-2, Minor) | Same | 2026-09-27 | 02 T-14, T-11, section 8.5 T-19 and section 9 rule 2 at `33e0916` still name only the interim retirement form | Lien, due the CDR readiness declaration and in any case on the branch before the CR-016 merge (INSP-061 iteration 2) |
| INSP-061 iteration 1: Documentation and Schedule (finding-3, Minor) | Same | 2026-09-27 | The 04, 05 and tool docstring hunks have no named vehicle; the step 6 delta of the INSP-061 record after the 02 re-blobbing merge is conditional | Lien, same due (INSP-061 iteration 2) |
| INSP-061 iteration 2: section 6 entry (cross item X-1) | `reviewer:WP-PDR-12-iteration-2` | 2026-09-27 | Concur Class I; every other field as iteration 1 (Documentation and Schedule "partly concur", finding-3); no open Major; the CR may go to disposition with finding-2 and finding-3 as liens | Entered here (round 1, section 6.1) |
| IR-F1 (Minor): Documentation field misses four consequential locations | Independent reviewer agent (CR-016 section 6 impact review, round 1) | 2026-09-27 | See section 6.1 | Open; author to add them to section 4 Documentation with the finding-3 fix |
| IR-F2 (Minor): stated branch base is not the fork point | Same | 2026-09-27 | See section 6.1 | Open; author to correct in the next revision |

Reviewer concurrence: concur with Class I, with effectivity after `baseline/pdr`, and with thirteen of the fourteen impact fields; Documentation partly concurred (finding-3, IR-F1). No open Major finding. The CR may go to the owner's disposition (OD-37, B2 Fri 10-02) with finding-2, finding-3, IR-F1 and IR-F2 presented as open Minor findings (section 6.1).

### 6.1 Impact review round 1: independent reviewer (2026-09-27)

Reviewer: independent reviewer agent (CR-016 section 6 impact review invocation), a separate invocation that authored no part of this CR, its branch or WP-PDR-12, and neither iteration of INSP-061. Date 2026-09-27. This round enters INSP-061 (`docs/reviews/PDR/checklists/cr-016-retired-status-schema.md`, iteration 1 at `b133a4b`, iteration 2 at `df722f7`, reviewer verdict APPROVED, record verdict held at NEEDS CHANGES until the CR-016 merge under the lead SE convention of 2026-09-27) as cross item X-1 asks, and adds its own search for missed items. The record governs its findings; the table above summarizes them.

Configuration reviewed: this file at blob `987f72e2` on `main` at `8c57710` (unchanged since `9bda072`); branch `cr/CR-016-retired-status-schema` at `33e0916`, product blobs `32d0a251`, `f8eae82a`, `09d6df9c` (recomputed, equal to the frozen table). Method: `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` first (query "retired requirement status Closed with tag retired interim marker; test case Blocked Retired by setup"), then `grep` and `git` only to pin lines and blobs.

Checks with no finding:

- Class I: correct under 05 Table 4-1 row 9 (an enum gains a value); the section 4 rationale and Q2 agree. The PCR-3 register row of the PDR work plan still says "II" (INSP-061 cross item X-2, lead SE, outside this CR).
- Effectivity after `baseline/pdr`: consistent with the plan register row PCR-3 and section 7 row "PCR-3 retired-status schema change"; nothing at F1 waits on it; the Class I cycle-time target of 05 §5.2 is met by disposition at B2.
- Branch diff against the CR: `git diff 443b2a3 33e0916` (the true fork point, IR-F2) touches exactly the three `affected_paths` (15 insertions, 14 deletions); the before-blobs on `main` at `8c57710` are still `fcdc5445` (02), `ca049dfb` and `d4b70163` (the two schemas), equal to `baseline/srr`, so no product file moved on `main` since the prototype.
- Re-validation and migration: the nine data files of section 1.1 are exactly the requirement and test-case data files on `main` at `8c57710` outside the fixture root (no wave 2a or 2b L2 file has landed yet); reviewer run with `jsonschema` (venv Python, Draft 2020-12) of the nine `main` blobs against the `33e0916` schemas: 9 of 9 PASS. No migration is needed.
- Merge feasibility: `git merge-tree --write-tree main 33e0916` is clean at `8c57710`.
- Verification plan (section 5 closing paragraph, step 5 and step 6): adequate; each check names its tool and expected result, and the seeded check was already run by INSP-061. Step 6 carries the finding-3 (b) lien.
- Safety, Verification, Requirements and traceability: concur None; the tool reads both forms (`Requirement.is_retired`, `TestCase.is_retired`, `TBR_FINAL_STATUSES`) on `main`.

Findings of this round:

| Finding | Severity | Location | Description | Fix |
|---|---|---|---|---|
| IR-F1 | Minor | Section 4 row Documentation | The search found four consequential locations outside those named in section 4 and in INSP-061 finding-3, all stating the interim form as the only retirement form: (a) 04 section 7.4 table row 7.3.2 (line 276 at `8c57710`: "retirement detected by the charter section 6 marker (requirement `Closed` with tag `retired`; case `Blocked` ...)"); (b) `docs/templates/peer-review-checklist-requirements.md` CK-REQ-A6 (line 184: "a retired item keeps its id with status `Closed`, tag `retired`") and `docs/templates/review-package.md` line 145 (column "of which retired (tag `retired`)", which after the merge would miss a `Retired` requirement from the `Closed` count and the retired count); both are Table 4-1 row 53 (CR from SRR), and a checklist change must list every `INSP-NNN` to re-run or keep; (c) `tools/traceability.py` beyond the module docstring and the `RETIRED_TAG` comment: the `RETIRED_INCONSISTENT` catalogue text (line 274, "until the schema carries Retired"; "the tag retired sits on a status other than Closed", while `check_retired` admits `Closed` or `Retired`) and the violation message of line 1633 ("retirement is status Closed with tag retired"), both printed into `docs/vv/traceability-report.md`; (d) `tools/README.md` line 87 ("until a schema CR adds `Retired`") and the T-19 row of line 129 (row 40, Log). None changes behavior; after the merge each would contradict 02 | Add (a) to (d) to section 4 Documentation, with (b) carried by a named CR under row 53 (or in `affected_paths` of this CR with the template owner's agreement) and (c) with the tool owner's agreement; fold into the finding-3 fix |
| IR-F2 | Minor | Front matter `configuration_at_origination`; preamble "Where the change is"; frozen-products table header; section 1.2 | The CR states the branch base as `11b1b1d` and the exact before and after text as `git diff 11b1b1d 33e0916`. The branch forks from `main` at `443b2a3` (`git merge-base main 33e0916`; `443b2a3` is the child of `11b1b1d` on `main`), so that command lists five files, adding the TS-001 and TS-002 errata of `443b2a3`. The product before-blobs are the same at both commits, so the review content is unaffected | Name base `443b2a3`, or give the diff as `git diff 11b1b1d...33e0916` (three dots, which resolves to the merge base) |

Measurements: impact fields checked 14; data files re-validated 9; blob identities recomputed 7; new findings 2 Minor, 0 Major. **Impact review complete: no open Major; Class I concurred.**

## 7. CCB disposition (owner)

| Field | Value |
|---|---|
| Decision | Approved |
| Class confirmed | I (concurred by the section 6 review, INSP-061 iteration 2, finding-1 Verified) |
| Date | 2026-09-28 |
| Conditions | None stated by the owner. Effectivity after `baseline/pdr` (section 12 Q3 as recommended); the merge follows section 5 step 5 |
| Rationale | Adds the Retired status to the requirement and test-case schemas (plan register PCR-3). INSP-061: finding-1 (Major) Verified; finding-2 and finding-3 Minor, liens due CDR |
| Waiver scope (if Approved (waiver)) | n/a |
| Re-look trigger and re-look-by review (if Deferred) | |
| Source | Chat transcription by Claude (configuration manager) on 2026-09-28. The presenter asked the owner to approve CR-007 to CR-016, the SRR lien fixes that passed their impact reviews (recommendation: approve all ten). Owner statement, verbatim: "Um, and then, yeah, I think you're uh, good to continue." The lead SE reads it as approval of item 1 as recommended, with the branches to merge after the section 9 checks (`docs/plan/status/status-2026-09-28.md` section 1, commit `e288add`, which transcribes the full statement); the owner is asked to correct any line |

Disposition history (append only):

| Date | Decision | New target | Source |
|---|---|---|---|
| 2026-09-28 | Approved | none | owner, `status-2026-09-28.md` section 1 (`e288add`), transcribed by Claude (configuration manager) |

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

Configuration manager pre-merge check (2026-09-28; performed at the disposition, not the independent verification, which stays pending). Method: `git merge-tree --write-tree` of the branch head with `main` (no conflict), then a trial `git merge --no-ff` in a detached scratch worktree of `main` (discarded afterwards, no ref kept), `tools/validate_docs.py` and `tools/traceability.py --report-only` on the trial merge, and the failure set compared with the baseline. Baseline on `main` at `e288add`: `tools/validate_docs.py` 102 passed, 8 failed (all record drift already on `main`: SRR `adrs-001-to-025.md`, `process-02-requirements-and-traceability.md`, `tool-validation-tv-001-to-tv-010.md`, `trade-studies-ts-001-ts-002.md`, `trade-study-ts-002-software-assurance.md`; PDR `cm-plan-05-software-assurance.md`, `configuration-status.md`, `lessons-learned.md`); `python -m unittest discover -s tools/tests` 596 run, 1 failure (`test_repository_exit_zero`, the same drift), 14 skipped; `tools/traceability.py --report-only` 0 violations, 2 warnings. Branch head `33e0916`. Scope: `git diff --stat main...` 3 files, 15 insertions, 14 deletions. Trial merge: `validate_docs.py` 102 passed, 8 failed, the baseline set (no new failure); `traceability.py --report-only`: 0 violations, 2 warnings. Merge not due: the effectivity is after `baseline/pdr` (Q3), and section 5 step 5 has the consequential 04, 05 and tool hunks written by their writers first.

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
| 2026-09-27 | Submitted | Claude (WP-PDR-12 author) | the commit that adds this file | Created with the impact assessment complete; product change prototyped on `cr/CR-016-retired-status-schema` at `33e0916`; section 6 review (rule C6) pending; effective after `baseline/pdr` unless ruled otherwise |
| 2026-09-27 | Submitted (revised) | Claude (WP-PDR-12 author) | the commit that makes this revision (`Refs: CR-016`) | INSP-061 finding-1 (Major) fixed: proposed class II to I (05 Table 4-1 row 9); classification rationale restated; row 9 re-validation list and migration statement added to section 1.1; merge-commit content added to step 5; Q2 changed. Branch and product blobs unchanged at `33e0916`. Minor findings 2 and 3 of INSP-061 are not addressed in this revision |
| 2026-09-27 | Assessed | Independent reviewer agent (CR-016 section 6 impact review) | the commit that records this row (`Refs: CR-016`) | Section 6 entered: INSP-061 iterations 1 and 2 (cross item X-1) and impact review round 1 (section 6.1); Class I and effectivity concurred; no open Major; new Minor IR-F1 (four consequential locations missing from section 4 Documentation) and IR-F2 (branch base is `443b2a3`, not `11b1b1d`); ready for OD-37 at B2 |
| 2026-09-28 | Dispositioned (Approved) | Claude (configuration manager), transcribing the owner | the commit that records this row (`Refs: CR-016`) | Owner approval of CR-007 to CR-016 as recommended (`status-2026-09-28.md` section 1); merge held at the disposition: effectivity after `baseline/pdr` (section 9 pre-merge check) |

## 12. Questions for the owner (answer with the disposition)

| # | Question | Recommendation |
|---|---|---|
| Q1 | Approve CR-016, which adds the status `Retired` to the requirement and test-case schemas and makes it the only form of a new retirement? | Approve, after the section 6 review reports no Major finding |
| Q2 | Confirm Class I | Confirm: 05 Table 4-1 row 9 makes a schema CR that adds an enum value Class I; the change adds `Retired` to two enums, migrates no data file (section 1.1) and changes no requirement or test case |
| Q3 | Effectivity: after `baseline/pdr`, or now? | After `baseline/pdr`, so the allocated baseline is written in one retirement vocabulary |
| Q4 | Keep REQ-SYS-016 and REQ-SYS-123 in their interim form (`Closed` with tag `retired`)? | Keep: a retired entry never changes status, and the tool reads both forms |

Answers recorded with the disposition (2026-09-28; the lead SE reading of the owner's approval "as recommended", the owner is asked to correct any answer): Q1 approved. Q2 Class I confirmed. Q3 effectivity after `baseline/pdr`. Q4 REQ-SYS-016 and REQ-SYS-123 keep their interim form.
