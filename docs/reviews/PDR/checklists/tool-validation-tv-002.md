---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md section 13;
# docs/process/05-configuration-and-data-management.md section 9.2 step 3). Record of the independent review
# of TV-002 run 6 for ACC-TRACE-002 (PDR work plan WP-PDR-06, record path as the plan names it).
# Item set applied: docs/templates/peer-review-checklist-tool-validation.md revision A, blob 7be809d4, on
# branch cr/CR-012-pdr-checklist-templates at 7784672 (APPROVED by INSP-033 iteration 2; CR-012 Submitted,
# not merged). The template is not on main, and tools/validate_docs.py rejects a checklist field whose
# template is absent from docs/templates/, so the checklist field names the code checklist, as INSP-040 and
# INSP-041 did for the other PDR tool records; the code review of item TV-G1-3 is INSP-042
# (docs/reviews/PDR/checklists/code-tools-traceability.md) at the same blob.
id: INSP-043
checklist: peer-review-checklist-code
checklist_revision: B
checklist_file: docs/reviews/PDR/checklists/tool-validation-tv-002.md
product: docs/cm/tool-validation/TV-002-traceability.md
product_commit: "4774562e41b2319814fa4fe0ad3075ba70d3bb72"
product_files: ["docs/cm/tool-validation/TV-002-traceability.md@1fe6fb756cc21180487c2148de0d02d676d3be37", "docs/cm/tool-validation/evidence/traceability-2026-09-27-r6.py@220ae2e0118fe13e8237b628d6192a0c67e3c44e", "docs/cm/tool-validation/evidence/traceability-2026-09-27-r6.log.txt@e26b24368088c56bf18c920b34a12e5dfdd1966a", "tools/traceability.py@d4cde9f54386373017f21825d4fd7cc0a42ac373", "tools/tests/test_traceability.py@95f1719b637834719212624b105f54f4a6cfd8b1", "tools/tests/test_tools.py@f8289a443f6ca2d837ab2df07df5a3dfc0722f27", "tools/README.md@d61156d8966178e958df4539adab60e8c0ff8b0d", "docs/process/02-requirements-and-traceability.md@d4934d0e7c9648c13ea7d50c1b28faba45b86c00", "tools/tests/fixtures/valid_project/docs/requirements/sys/requirements.json@d0a10e0bb645f016bdf77eebeca0fedfb142240a", "tools/tests/fixtures/valid_project/docs/requirements/sys/requirements.md@5b8f8d87935af6432e713d6d0afc80747e022589", "tools/tests/fixtures/valid_project/firmware/cwht-core/src/keyer/straight.rs@e5f98357d15d9d7aa50be0a2d13dea67566d57cd", "tools/tests/fixtures/valid_project/firmware/cwht-core/src/keyer/iambic.rs@e5f98357d15d9d7aa50be0a2d13dea67566d57cd", "tools/tests/fixtures/valid_project/firmware/cwht-core/src/keyer/config.rs@e5f98357d15d9d7aa50be0a2d13dea67566d57cd", "tools/tests/fixtures/valid_project/hardware/kicad/tx-pa.kicad_sch@b42ba81e76a76cc8a013e23bac36d3c2277ed5c4", "docs/vv/traceability-report.md@f49f4215b34179caca551dcfd9a348fdf17c288e", "docs/vv/traceability.json@0f0ea6ef18bdcabd3cba6ef9d6853296de6c476f", "docs/cm/cr/CR-011-traceability-pdr-rules.md@d597899b9f442bfc9c3983cb28f15998eb78c197"]
# fixture_trees: git trees at product_commit (git rev-parse 4774562:<dir>); the unchanged identities of TV-002
# section 1 (validate_docs.py 3aa03681, test_traceability_srr_rules.py 86606485) were checked at the same commit
fixture_trees: ["tools/tests/fixtures/valid_project@bcd898307e93113336cf9b1045d7a8ce827f42cc", "tools/tests/fixtures/invalid_project@6a046bae3fe2a86c2e4b00a41954f1946b5e3b1f"]
tv_ids: [TV-002]
tool_class: B
tool_kind: repository-tool
acc_proposed: [ACC-TRACE-002]
product_size: 1 record (191 lines), 8 purposes, 229 known-answer tests (80 + 32 + 117), 74 fixture files (42 + 32), 2 evidence files; tool 4156 lines
sprint: PDR-prep
author_agent: "author:WP-PDR-06 (Claude as tool owner and software lead, CR-011)"
tool_author_agent: "author:WP-PDR-06 (Claude as tool owner, CR-011)"
reviewer_agent: "reviewer:WP-PDR-06-code-and-tv (independent invocation, authored no part of CR-011 or TV-002)"
criticality: neither
# assurance_required: the TV template (CR-012) says false and makes section H this reviewer's task; PDR work plan
# WP-PDR-06 names a separate SA second review (tool used for credit), requested from the lead SE ("SA pair needed")
assurance_required: true
assurance_reviewer_agent: "pending: separate software assurance invocation, record docs/reviews/PDR/checklists/code-tools-traceability-software-assurance.md (plan WP-PDR-06)"
iteration: 1
readiness_met: true
reviewer_verdict: NEEDS CHANGES
assurance_verdict: pending
verdict: NEEDS CHANGES
findings_major: 1
findings_minor: 4
findings_open: 5
findings_fixed: 0
findings_verified: 0
findings_deferred: 0
assurance_tasks_applied: [swe-136 7.1 task 1, swe-070 7.1 task 1]
deferred_rids: []
items_no: [TV-B2, TV-B3, TV-D1, TV-D2, TV-E1, TV-E2, TV-F3, TV-F5]
effort_turns: 30
effort_minutes: 45
record_status: Open
date: 2026-09-27
date_closed: null
---

# Peer review record INSP-043: TV-002 run 6, `tools/traceability.py` blob `d4cde9f5` (WP-PDR-06, CR-011)

**Product:** `docs/cm/tool-validation/TV-002-traceability.md` blob `1fe6fb75` at the CR-011 branch head `4774562`, with the tool, known-answer modules, fixture changes, evidence procedure and log of run 6 at the blobs of `product_files` (every entry equal to `git rev-parse 4774562:<path>`). **Checklist:** the item set of `docs/templates/peer-review-checklist-tool-validation.md` revision A (CR-012 branch `7784672`, blob `7be809d4`); `tool_kind` repository-tool, so sections A to F, G1 and H apply, and G2 to G4 are N/A. The code review that item TV-G1-3 requires is INSP-042 (`docs/reviews/PDR/checklists/code-tools-traceability.md`), same reviewer invocation, same blob.

**Acceptance criteria (rule C7):** every clause of 05 section 9.2 steps 1 to 5 and of the `tools/traceability.py` row of its known-answer table; every item TV-A1 to TV-H3 of the template; every purpose of TV-002 section 2 (1 to 8) checked against a known answer; every use of the tool that the repository cites (item TV-B2).

**Independence (rule C4):** this invocation authored no part of CR-011, TV-002 or the tool. **Search first:** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (the two queries of INSP-042); `grep -n` pinned lines afterwards.

## Reviewer re-run and checks

| # | Check | Result |
|---|---|---|
| V1 | Identities in the export of `4774562` (`git hash-object`, `shasum -a 256`) | `traceability.py` `d4cde9f5` / `e1de5466...080e`; `test_traceability.py` `95f1719b` / `489faa66...7a01`; `test_tools.py` `f8289a44` / `837e0fb8...fef1`; `test_traceability_srr_rules.py` `86606485` / `7c8f10a4...9776`; `validate_docs.py` `3aa03681` / `e06c72a1...6092`: all equal to TV-002 section 1 "Identities for run 6" |
| V2 | Fixture digests recomputed with the function `tree` of `evidence/python-tools-2026-09-25.py` | `valid_project` 42 files `e0bf2533...c1c`, `invalid_project` 32 files `2377caa9...3eb`: equal to the record. Git trees at `4774562`: `bcd89830`, `6a046bae` (front matter `fixture_trees`) |
| V3 | Section 3 run 6 commands in the export | exit 0; 80, 32 and 117 tests; `OK`; none skipped: equal to run 6 (229) |
| V4 | Mutation check repeated (predecessor blob `12de3545` from `a3cacee`) | all 13 PDR classes fail, per-class counts equal to the run 6 log section 3 |
| V5 | Repository run R-3 repeated on the branch worktree, plain and `--gate PDR` | plain exit 0, 0 violations, 95 warnings; gate exit 1, 379 violations; code counts equal to R-3 |
| V6 | The regenerated `docs/vv/traceability-report.md` and `traceability.json` of the branch against V5 | equal except the HEAD short SHA (`4411a09`, the commit they were made at) and the `generated` date |

## Record

### Findings

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | reviewer | Major | TV-B2 | TV-002 section 2 (purposes 1 to 8) and section 9 ACC-TRACE-002 | A cited use of the tool is covered by no purpose: `tools/traceability.py --regression <design_ref...>` prints the hardware regression set (04 section 7.3 rule 10 and section 10.5; 02 section 8.1 option table), and ACC-TRACE-002 would accredit "purposes 1 to 8" only, so regression-set output would stay developer evidence. A known answer exists (`ValidProjectTests.test_regression_set`: the tx-pa sheet gives `TC-SYS-002`, the rx sheet gives none, the CLI prefix form exits 0), but the "plus every `TC-ATP-NNN` case" clause of rule 7.3.10 is not exercised (no ATP case in `valid_project`). Fix: add a purpose for `--regression` naming its known answer and seeded fault, add an ATP case to the known answer (in memory, as the PDR classes do) or state the ATP clause as a limitation, and extend the ACC-TRACE-002 scope | Open | Pending | |
| <a id="finding-2"></a>finding-2 | reviewer | Minor | TV-F5 | TV-002 header, section 4 run 6, section 9 last row | 05 section 9.2 step 4 ("no new TV number unless the version changed") and step 5 (a version change of an Accredited tool is "a CR ... plus a new TV record") call for a new TV number for blob `d4cde9f5`; the record appends run 6 and ACC-TRACE-002 to TV-002, as run 5 did for CR-002 and as plan WP-PDR-06 ("TV-002 re-validation") directs. Fix: the owner rules which reading applies (a new TV record, or re-validation inside TV-002 for a repository tool changed by an approved CR, then written into 05 section 9.2 by its writer); the record then cites the ruling | Open | Pending | |
| <a id="finding-3"></a>finding-3 | reviewer | Minor | TV-E2 | TV-002 section 7 | The triggers omit "a version change ... of the OS major version" of 05 section 9.2 step 4. Fix: add it | Open | Pending | |
| <a id="finding-4"></a>finding-4 | reviewer | Minor | TV-D1, TV-D2, TV-F3 | TV-002 section 4 row 6; `tools/toolchain.lock.md` section 1.1 row `tools/traceability.py, tools/validate_docs.py` (line 85) and section 5 row (line 246); `docs/cm/tool-validation/README.md` row TV-002 (line 26), all at `4774562` | Run 6 has a date but no time. The lock section 1.1 row still names only the SRR known-answer classes and no run 6, and the lock section 5 row and the README index row still read "blob `0a867523` ... Accredited", while the record header states run 6 on `d4cde9f5` pending review. CR-011 section 4 routes the lock rows to WP-PDR-09; the README index row is routed nowhere. Fix: add the run 6 time; update the README index row on the branch; WP-PDR-09 updates the lock rows before the merge | Open | Pending | |
| <a id="finding-5"></a>finding-5 | reviewer | Minor | TV-B3, TV-E1 | TV-002 section 2 purpose 8 and section 6 | Purpose 8 claims the MSR-02 record is appended "only after the whole file passes" the schema; the tool appends with no check when the schema is absent or unreadable or `jsonschema` is missing (INSP-042 finding-5). Section 6 also omits two limitations that bound cited uses: T-13 counts a change as covered when any approved CR lists the id, without the exact-string comparison of 02 section 10.3 item 2 (INSP-042 finding-1), and T-12 checks fewer evidence cells than limitation 8 implies (INSP-042 finding-3). Fix: narrow purpose 8 or fix the tool, and add the two limitations | Open | Pending | |

### Per-record results

| TV record | Tool and version | Class | Commit tested | Reviewer re-run (command, exit, result) | Items answered No | Finding ids |
|---|---|---|---|---|---|---|
| TV-002 | `tools/traceability.py`, blob `d4cde9f5` (no version string; version = blob) | B | `4411a09` (tool, test modules and fixtures equal at `4774562`) | the three section 3 commands with the run 6 selection in an export of `4774562`; exit 0 each; 229 tests, none skipped; same as run 6 | TV-B2, TV-B3, TV-D1, TV-D2, TV-E1, TV-E2, TV-F3, TV-F5 | finding-1 to finding-5 |

### Per-purpose results

| TV record | Purpose | Known answer that exercises it | Seeded fault (class B) | Cited uses of the purpose in the project | Finding ids |
|---|---|---|---|---|---|
| TV-002 | 1 (rule catalogue on the root; exit 1 on a violation) | `ValidProjectTests`, `InvalidProjectTests`, `test_tools.py` (one known answer per catalogue code, guarded by `CatalogueKnownAnswerTests`) | the `invalid_project` seeded set, exact code sets asserted | charter section 7; 01 section 3.1 item 2; 02 sections 8.2 and 8.5; 04 section 7.3 | none |
| TV-002 | 2 (T-21, T-18 SRR form) | `test_traceability_srr_rules.py` 32 tests | seeded stakeholder and allocation faults | 02 T-18, T-21 | none |
| TV-002 | 3 (report and data file; `--report-only` exit 0) | `InvalidProjectTests.test_report_only_exits_zero`, report-section assertions, `RetiredAndReportSectionTests` | `invalid_project` exits 1 without the option | 01 section 3.1 item 2 (per-review report and JSON); 07 section 11 MSR-01, 03, 04, 23 | none |
| TV-002 | 4 (`--render`) | `test_tools.py` render classes (`RENDER_STALE`) | a hand-edited rendered file | 02 section 8.1; charter section 5 | none |
| TV-002 | 5 (`--gate`) | `GateOptionTests` (6), `OnTargetAtSarTests`, `SafetyPartTests.test_no_marked_part_at_pdr`, `GitHistoryRuleTests.test_not_a_git_root` | `--gate QDR` exits 2; each promoted code checked at, before and after its gate | 02 section 8.1 entrance mode; 01 section 3.1 item 2 once it adds `--gate` (INSP-042 X-1) | none |
| TV-002 | 6 (PDR rules on the root) | `DesignReferenceTests`, `MeasureRuleTests`, `IcdPairingTests`, `HazardControlTests`, `SafetyPartTests`, `AdrBackReferenceTests`, `EvidenceRuleAdditionTests`, `RetiredAndReportSectionTests` | one change per test from `valid_project` (for example `B99`, an unpaired side, an ICD named `ICD-SW-CTL`, a dev-board case with `Credit row: T-HW`) | 02 T-15, T-16, T-20, T-22; 03 section 8; 04 rules 7.3.4, 7.3.5, 7.3.12; RFA-SRR-007 L-7; SRR memo section 9 condition 5 | INSP-042 finding-6 (assertion breadth) |
| TV-002 | 7 (git-history rules) | `GitHistoryRuleTests` (9) on temporary repositories | a deleted case and stakeholder, forbidden transitions, a retirement naming an unapproved CR, an uncovered Class I change, a stale case | 02 T-04, T-12, T-13; 04 rule 7.3.11 | finding-5 |
| TV-002 | 8 (`--volatility`, `--fix-children`) | `VolatilityTests` (3; hand count 4 of 6 = 66.7 %), `FixChildrenTests` | a schema that refuses a second record (exit 2, nothing written); an emptied `child_ids` | 02 section 10.4 (SWE-200, MSR-02, TPM-012); 02 section 8.1 | finding-5 |
| TV-002 | (none) `--regression` | `ValidProjectTests.test_regression_set` | an rx sheet with no Bench case gives an empty set | 04 section 7.3 rule 10, section 10.5 | finding-1 |

## Readiness criteria

| # | Answer | Evidence |
|---|---|---|
| R1 | Yes | Every file committed at `4774562`; `product_files` names each changed file by blob; the unchanged fixture files are covered by `fixture_trees` and the V2 digests (the brief froze the changed files only; the template asks for fixture files one by one, which is a record-completeness note for the re-issue, not a product finding) |
| R2 | Yes | V3 |
| R3 | Yes | V3 and INSP-042 C2 (471 tests, OK). `validate_docs.py` on the branch fails only on the SRR records INSP-015 and INSP-020 (record drift), as TV-002 limitation 6 states; on `main` the product files are not present, so R3 is read on the export |
| R4 | No (Minor) | The lock rows exist but lag run 6 (finding-4); the README index row exists but lags (finding-4) |
| R5 | Yes | The author summary and TV-002 sections 2, 3, 4 and 9 list purposes, uses, known answers, runs and ACC-TRACE-002 |

## A. Identification

| Id | Answer | Evidence |
|---|---|---|
| TV-A1 | Yes | No version string; the version is the blob (TV-002 section 1); V1 |
| TV-A2 | Yes | Install source: the repository (05 Table 4-1 row 28), no installer, stated in section 1 |
| TV-A3 | Yes | V1, V2 |
| TV-A4 | Yes | Run 6 names `4411a09`; `git diff --stat 4411a09 4774562` touches only TV-002, the two evidence files, the regenerated report and JSON, and 02, so tool, test modules and fixtures are identical at both |
| TV-A5 | Yes | Class B: the output is cited as review and inspection evidence (charter section 7) and enters no release |
| TV-A6 | Yes | Scripted procedure `evidence/traceability-2026-09-27-r6.py`; no GUI step |

## B. Purposes

| Id | Answer | Evidence |
|---|---|---|
| TV-B1 | Yes | Each of purposes 1 to 8 names an input and an observable output or exit status. Purposes 5 to 8 are long single lines listing codes, which is acceptable because each code has its own known answer |
| TV-B2 | No | finding-1 (`--regression` uncovered). Other cited uses found by search (01 section 3.1 item 2, 02 sections 8 and 10.4, 04 section 7.3, 07 section 11 measurements, charter section 7) map to purposes 1 to 8 |
| TV-B3 | No | finding-5 (purpose 8 schema check). The code lists of purposes 5 to 7 equal the codes the PDR classes exercise (V3, V4) |

## C. Known-answer test

| Id | Answer | Evidence |
|---|---|---|
| TV-C1 | Yes | Fixtures under `tools/tests/fixtures/`; commands and pass criteria in section 3 |
| TV-C2 | Yes | Every purpose 1 to 8 has a known answer with a seeded fault (per-purpose table); the negative control is the mutation check V4 |
| TV-C3 | Yes | Expected answers are written in the tests by hand (fixture edits, exact locations, the 66.7 % hand count); none is produced by the tool |
| TV-C4 | Yes | 05 section 9.2 table row for the tool: the fixture-only classes pass, `valid_project` exits 0 with zero findings and `invalid_project` exits 1 with exactly the seeded codes (`InvalidProjectTests.test_violation_codes_exactly_the_seeded_set` in V3); `RepositoryTests` excluded |
| TV-C5 | Yes | V3 |

## D. Results and reproducibility

| Id | Answer | Evidence |
|---|---|---|
| TV-D1 | No | Run 6 row has no time (finding-4); the rest (commit, count, excerpt, committed log `e26b2436`) supports the row (V1 to V5 reproduce it) |
| TV-D2 | No | Lock section 1.1 not updated for run 6 (finding-4) |
| TV-D3 | N/A | Class B |

## E. Limitations and re-validation triggers

| Id | Answer | Evidence |
|---|---|---|
| TV-E1 | No | Confirmed true by reading the code or a run: limitation 6 (V5, INSP-042 C8), 7 (`check_history`, `:2933`; `test_not_a_git_root`), 8 (`HAZARD_UNCONTROLLED` severity, `SAFETY_PART_UNTRACED` field). Missing: finding-5 |
| TV-E2 | No | finding-3 |

## F. Accreditation readiness, schedule and indexes

| Id | Answer | Evidence |
|---|---|---|
| TV-F1 | Yes | ACC-TRACE-002 names purposes, the blob, `validate_docs.py` blob `3aa03681`, the TV-001 interpreter and TV-009 git; purpose 7 states the git work-tree precondition. The scope must grow with finding-1 |
| TV-F2 | Yes | Header "Due": SRR, run 6 before the PDR readiness declaration (plan WP-PDR-06; 04 section 7.4) |
| TV-F3 | No | finding-4 |
| TV-F4 | Yes | Section 9 last row requests; the status line and limitation 6 state developer evidence until the owner records ACC-TRACE-002 |
| TV-F5 | No | CR-011 (Class II) is named; the new TV number is not (finding-2) |

## G1. Repository tool

| Id | Answer | Evidence |
|---|---|---|
| TV-G1-1 | Yes | `RepositoryTests` are outside the section 3 selection; limitation 4 names the two `SchemaTripwireTests` in `test_tools.py` that still read repository content |
| TV-G1-2 | Yes | Exit 0 (`ValidProjectTests.test_cli_exit_zero`, `--report-only`, `--dry-run`), 1 (`InvalidProjectTests.test_cli_exit_one`, `--gate PDR` on `valid_project`), 2 (`--gate QDR`, `VolatilityTests.test_usage_errors`, schema refusal). The module docstring does not document exit 2 (INSP-042 finding-7) |
| TV-G1-3 | Yes | INSP-042 at blob `d4cde9f5` |

G2, G3 and G4: N/A (repository tool).

## H. Software assurance tasks

| Id | Answer | Evidence |
|---|---|---|
| TV-H1 | Yes | swe-136 7.1 task 1: the tool maintains the traceability that SWE-052 requires; its purposes cover the uses the process documents cite except `--regression` (finding-1). No 07 section 8.4 gate step calls the tool |
| TV-H2 | Yes | swe-070 7.1 task 1: the tool's output (matrices, Inspection-class traceability checks) is qualification evidence; the purposes cover the analyses that cite it (04 section 7.3; 01 section 3.1 item 2) with finding-1 excepted |
| TV-H3 | Yes | Front matter `assurance_tasks_applied`; results above. The separate SA second review the plan names is not this record |

## Measurements (SWE-089)

Items checked 33 (R1 to R5, A1 to A6, B1 to B3, C1 to C5, D1 to D3, E1, E2, F1 to F5, G1-1 to G1-3, H1 to H3); answered No 8 (plus R4); N/A 1 in sections A to H (D3) and G2 to G4; findings 1 Major, 4 Minor; iteration 1; effort 30 turns, 45 minutes.

## Record verdict

`NEEDS CHANGES`: finding-1 is Major under the template's rule ("an uncovered cited use is Major"). Its fix is a purpose line, an ATP known answer or limitation, and the ACC-TRACE-002 scope; iteration 2 is a delta that verifies it (rule C1). The four Minor findings are liens due at the CDR readiness declaration if not fixed with the Major. The owner's rulings on finding-2 (TV number) and the separate SA second review (plan WP-PDR-06) are outside this verdict. An APPROVED verdict on `main` also needs CR-011 merged with these blobs unchanged (record drift rule).

```
VERDICT: NEEDS CHANGES
PRODUCT: TV-002 at 4774562 (run 6 on 4411a09)
FINDINGS:
- [Major] TV-B2 TV-002 section 2: --regression (04 rule 7.3.10, section 10.5) is covered by no purpose; ATP clause not exercised.
- [Minor] TV-F5 TV-002 section 9: new TV number for blob d4cde9f5 per 05 section 9.2 steps 4 and 5 not taken; owner ruling needed.
- [Minor] TV-E2 TV-002 section 7: OS major version trigger missing.
- [Minor] TV-D1, TV-D2, TV-F3: run 6 time missing; lock section 1.1 and 5 rows and the README index row lag run 6.
- [Minor] TV-B3, TV-E1 TV-002 sections 2 and 6: purpose 8 schema claim wider than the tool; T-13 and T-12 limitations missing.
ITEMS N/A: TV-D3 (class B), TV-G2 to TV-G4 (repository tool)
RE-RUN: the three section 3 commands in an export of 4774562; exit 0; 229 tests; same as record run 6
MEASUREMENTS: size=1 record, 8 purposes; turns=30; minutes=45; major=1; minor=4
```
