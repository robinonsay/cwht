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
# Iteration 2 (2026-09-27): delta verification of finding-1 (Major) on TV-002 run 7. product_commit is the CR-011
# branch head 2b004b1 (commits 709e95f test module, 2b004b1 TV-002 and run 7 evidence); iteration 1 read 4774562.
# The tool blob d4cde9f5 is unchanged; the CR-011 file is on main, unchanged at d597899b.
product_commit: "2b004b17bf94ecf3dc3591cbc34892e6620ad8a7"
product_files: ["docs/cm/tool-validation/TV-002-traceability.md@94ae3af57e6d5527ccd5ff76ab7aa8724fb0b395", "docs/cm/tool-validation/evidence/traceability-2026-09-27-r7.py@e6f3785628ee376a921a1176883f475c086ab656", "docs/cm/tool-validation/evidence/traceability-2026-09-27-r7.log.txt@1e30bb222b51ecdf3800f6bb5c4a243ce94f0ef3", "tools/tests/test_traceability.py@6ead56414127f9c13cd39e3662a2118e2acd470e", "tools/traceability.py@d4cde9f54386373017f21825d4fd7cc0a42ac373", "tools/tests/test_tools.py@f8289a443f6ca2d837ab2df07df5a3dfc0722f27", "tools/README.md@d61156d8966178e958df4539adab60e8c0ff8b0d", "docs/process/02-requirements-and-traceability.md@d4934d0e7c9648c13ea7d50c1b28faba45b86c00", "docs/cm/tool-validation/evidence/traceability-2026-09-27-r6.py@220ae2e0118fe13e8237b628d6192a0c67e3c44e", "docs/cm/tool-validation/evidence/traceability-2026-09-27-r6.log.txt@e26b24368088c56bf18c920b34a12e5dfdd1966a", "docs/vv/traceability-report.md@f49f4215b34179caca551dcfd9a348fdf17c288e", "docs/vv/traceability.json@0f0ea6ef18bdcabd3cba6ef9d6853296de6c476f", "docs/cm/cr/CR-011-traceability-pdr-rules.md@d597899b9f442bfc9c3983cb28f15998eb78c197"]
# fixture_trees: git trees at product_commit (git rev-parse 4774562:<dir>, equal at 2b004b1); the unchanged identities of TV-002
# section 1 (validate_docs.py 3aa03681, test_traceability_srr_rules.py 86606485) were checked at the same commit
fixture_trees: ["tools/tests/fixtures/valid_project@bcd898307e93113336cf9b1045d7a8ce827f42cc", "tools/tests/fixtures/invalid_project@6a046bae3fe2a86c2e4b00a41954f1946b5e3b1f"]
tv_ids: [TV-002]
tool_class: B
tool_kind: repository-tool
acc_proposed: [ACC-TRACE-002]
product_size: "iteration 2: 1 record (TV-002 at 2b004b1, 226 lines), 9 purposes, 235 known-answer tests (86 + 32 + 117), 74 fixture files (42 + 32, unchanged), 4 evidence files (run 6 and run 7); tool 4156 lines (unchanged). Iteration 1: 191-line record, 8 purposes, 229 tests"
sprint: PDR-prep
author_agent: "author:WP-PDR-06 (Claude as tool owner and software lead, CR-011)"
tool_author_agent: "author:WP-PDR-06 (Claude as tool owner, CR-011)"
reviewer_agent: "reviewer:WP-PDR-06-code-and-tv (independent invocation, authored no part of CR-011 or TV-002)"
criticality: neither
# assurance_required: the TV template (CR-012) says false and makes section H this reviewer's task; PDR work plan
# WP-PDR-06 names a separate SA second review (tool used for credit), requested from the lead SE ("SA pair needed")
assurance_required: true
assurance_reviewer_agent: "pending: separate software assurance invocation, record docs/reviews/PDR/checklists/code-tools-traceability-software-assurance.md (plan WP-PDR-06)"
iteration: 2
readiness_met: true
reviewer_verdict: APPROVED
assurance_verdict: pending
# verdict: held at NEEDS CHANGES (a) until the SA pair is APPROVED and (b) while the reviewed blobs are on the CR-011
# branch only (record drift rule; the INSP-037 hold); set APPROVED at the CR-011 merge with these blobs unchanged.
verdict: NEEDS CHANGES
findings_major: 1
findings_minor: 4
findings_open: 0
findings_fixed: 0
findings_verified: 1
findings_deferred: 0
assurance_tasks_applied: [swe-136 7.1 task 1, swe-070 7.1 task 1]
deferred_rids: []
# items_no: TV-B2 answered Yes at iteration 2 (finding-1 Verified); the rest are the Minor liens
items_no: [TV-B3, TV-D1, TV-D2, TV-E1, TV-E2, TV-F3, TV-F5]
effort_turns: 62
effort_minutes: 90
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

## Iteration 2: delta verification of finding-1 (Major) (2026-09-27, TV-002 run 7)

**Scope (rule C1).** Iteration 2 is a delta that verifies the Major fix only. Product: TV-002 blob `94ae3af5` at the CR-011 branch head `2b004b1`, with the run 7 procedure `evidence/traceability-2026-09-27-r7.py` (blob `e6f37856`) and log (blob `1e30bb22`), and the test module `tools/tests/test_traceability.py` blob `6ead5641` (commit `709e95f`). Every `product_files` entry equals `git rev-parse 2b004b1:<path>`; the fixture trees are still `bcd89830` and `6a046bae`; the CR-011 file equals `git rev-parse main:<path>` (`d597899b`). `git diff --stat 4774562 2b004b1` touches four files only: TV-002, the two run 7 evidence files and the test module. The tool blob `d4cde9f5`, `test_tools.py`, `tools/README.md`, 02, the run 6 evidence and the regenerated report and JSON are unchanged, so the iteration 1 answers of sections A, C to H and the code review INSP-042 stand for them. The delta was read as `git diff --word-diff 4774562 2b004b1`.

**Independence (rule C4).** This invocation authored no part of CR-011, TV-002 (any run), the tool or the test module, did not write iteration 1 of this record, and edited no product file.

**Search first (charter section 11 rule 1).** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (query: the INSP-043 review of WP-PDR-06, TV-002 and `--regression`). `grep -n` afterwards only pinned lines in the tool, 04 and `tools/README.md`.

**Software assurance participant.** Unchanged from iteration 1: the SA second review of plan WP-PDR-06 (`code-tools-traceability-software-assurance.md`) is a separate invocation and is not filed ("SA pair needed").

### Reviewer re-run (iteration 2)

| # | Check | Result |
|---|---|---|
| V7 | The run 7 procedure, run by this reviewer from a detached scratch worktree at `2b004b1` (removed after use): `traceability-2026-09-27-r7.py 2b004b1 a3cacee <scratch> --rustos /Users/robinonsay/rust/rustos` (rustos read by `git show` only) | exit 0. The output equals the committed run 7 log line for line except the first line (the commit hashed: `2b004b1` here, `709e95f` there; the test module and every other identity are equal at both). Identities as TV-002 "Identities for run 7"; 86 + 32 + 117 = 235 tests, OK, 0 skipped; step 3: the thirteen PDR classes fail on predecessor blob `12de3545` with the run 6 per-class counts; step 3b: M1 to M6 killed with 5, 2, 3, 1, 5 and 4 failures; step 4 on the `2b004b1` checkout: plain exit 0, 0 violations, 95 warnings; `--gate PDR` exit 1, 379 violations; code counts equal to R-3 and R-4 |
| V8 | Six further mutants written by this reviewer (not in the procedure), each one exact text substitution in the export, `RegressionSetTests` run against each | all killed: R1 retirement read as status `Retired` only (1 failure, the `Blocked`/`Retired by ` form); R2 `any` over touched replaced by `all` (2); R3 one-way prefix, argument is a prefix of the reference only (1); R4 no trailing `/` strip (1); R5 reverse sort order (3); R6 ATP cases selected by id prefix with the `Blocked` retirement form kept (1) |
| V9 | Full suite `unittest discover -s tools/tests` at `2b004b1` | 477 tests, 1 failure (`test_validate_docs.RepositoryTests.test_repository_exit_zero`), 3 skipped. The failure is `validate_docs.py` 48 passed, 2 failed: INSP-020 and INSP-015, the record drift TV-002 limitation 6 states (as at iteration 1; CR-011 section 5 step 6) |
| V10 | Tool text against purpose 9 (`regression_set`, `design_ref_matches`, `TestCase.is_retired`, `--regression` branch of `main`, `load_test_cases`) | Purpose 9 describes the code: `Passed` and `Bench` filter; `affected` built with `any` over arguments and `design_refs`; match on equality or a `/` boundary after stripping a trailing `/`; ATP cases by module `ATP` (from the file's module) and `not is_retired`, the two 02 section 11.3 forms; one id per line from `sorted`; exit 0 before any report is written |
| V11 | Limitation 9 (b) against the branch requirement files | The distinct `design_refs` at `2b004b1` are one `firmware/` path (`firmware/cwht-core/src/keyer/`), one `rustos:firmware/` path, seven `ICD-<A>-<B>` ids and element ids `B02` to `B07`: equal to the list the limitation gives |

### Verification of finding-1 (Major)

| # | Expected fix element (iteration 1) | Run 7 text (TV-002 blob `94ae3af5`) | Independent check | Result |
|---|---|---|---|---|
| 1 | Add a purpose for `--regression` | Section 2 purpose 9: input (`DESIGN_REF ...`), output (sorted ids, exit 0, no report), the filter, the matching rule, the live-ATP reading, and the cited uses 04 rule 7.3.10, 04 section 10.5 hardware and firmware-release forms, 02 section 8.1 | V10. The cited uses equal the two 04 section 10.5 bullets that call the option (the hardware set and "Firmware release on a delivered unit") and rule 7.3.10; 04 section 7.4 row 7.3.10 and `tools/README.md` already say "every live `TC-ATP` case", so the reading is the project's documented one, not the tool author's alone | Holds |
| 2 | Name its known answer and seeded fault | Section 3 run 7 paragraph: `RegressionSetTests`, the ATP case added in memory or in a temporary copy, the statuses, retirement forms and matching cases, the seeded faults | Read the six tests against the paragraph: every listed case is asserted with an exact expected list; expected lists are written by hand, none produced by the tool (TV-C3); neither fixture changes (V7 tree digests) | Holds |
| 3 | Exercise the "plus every `TC-ATP-NNN` case" clause | `test_live_atp_case_is_always_in_the_set`, `test_retired_atp_case_is_not_in_the_set`, `test_cli_prints_the_atp_case` | The clause is exercised through the library and the command line, with the ATP case in its own `docs/test_cases/atp/test_cases.json` file for the CLI (the real load path); M1, M2, R1 and R6 show the tests detect a removed or mis-scoped ATP clause | Holds |
| 4 | Negative control | Section 4 step 3b, M1 to M6 | V7 reproduces 6 of 6; V8 adds 6 of 6 | Holds |
| 5 | State what the tool does not cover | Section 6 limitation 9 (a) to (d) | Each part checked: (a) an unknown argument prints the ATP set alone (true by V10: no validation of arguments); (b) pin move and ID-only matching (V11); (c) receipt inspection and `TC-VAL` regression are outside the printed set, and the firmware form's Bench filter is the `Passed` Bench filter; (d) live ATP only | Holds |
| 6 | Extend the ACC-TRACE-002 scope | Section 9: "Accredited for purposes 1 to 9 ...", extension dated and attributed to finding-1; condition names this iteration 2 delta | Read | Holds |
| 7 | No out-of-scope change | Header status update, run 7 identities, section 4 row 7 and R-4, section 8 run 7 review line | The four changed files only; the header update's numbers (235 tests, six mutants killed) equal V7; no em dash in the changed files | Holds |

**finding-1: Verified.** Every cited use of the tool is now covered by a purpose with a known answer and a seeded fault, and ACC-TRACE-002 requests purpose 9. Item TV-B2 changes from No to Yes; TV-C2 and TV-F1 hold for purpose 9; TV-H1 and TV-H2 no longer carry the finding-1 exception.

**Per-purpose result, purpose 9.** Known answer `RegressionSetTests` (6 tests); seeded faults: Bench case not `Passed`, case not Bench, retired ATP case in either form, matching without a `/` boundary, a design-unit id and the empty string as arguments; cited uses 04 section 7.3 rule 10, section 10.5 (hardware set, firmware release on a delivered unit), 02 section 8.1; findings none (bounded by limitation 9).

**Scan of the delta for new defects.** None of Major or Minor weight. Two notes, no finding: (i) purpose 9 says a design-unit id "touches only itself"; the code would also match a reference `B21/<x>` on the `/` boundary, but no such reference form exists in the project (V11) or in 02 T-15, so the statement is true for every valid reference. (ii) The lock section 1.1 and section 5 rows and the `docs/cm/tool-validation/README.md` TV-002 row now lag run 7 as well as run 6; this is inside the finding-4 lien, whose fix covers the latest run.

### Findings (iteration 2; current state of every finding of this record)

| Finding | Severity | State | Disposition |
|---|---|---|---|
| finding-1 | Major | Verified | Closed at iteration 2 on TV-002 run 7, blob `94ae3af5`, test module `6ead5641` (table above) |
| finding-2 | Minor | Lien: fix before CDR | New TV number versus re-validation inside TV-002 for blob `d4cde9f5`; needs the owner's ruling (05 section 9.2 steps 4 and 5). Owner: Claude as tool owner, to put the question to the owner at the next session; due the CDR readiness declaration; listed in PDR package section 15 |
| finding-3 | Minor | Lien: fix before CDR | TV-002 section 7 OS major version trigger; owner Claude as tool owner; same due |
| finding-4 | Minor | Lien: fix before CDR | Run 6 time; lock section 1.1 and 5 rows (WP-PDR-09 writer) and the tool-validation README row lag run 6 and now run 7; owner Claude as tool owner (README, TV-002) and WP-PDR-09 (lock); due before the CR-011 merge where possible, at the latest the CDR readiness declaration |
| finding-5 | Minor | Lien: fix before CDR | Purpose 8 schema claim and the T-13 and T-12 limitations (INSP-042 finding-5, 1, 3); owner Claude as tool owner; same due |

Findings by severity: 1 Major (Verified), 4 Minor (liens). Zero Major findings remain. No new finding.

### Measurements (SWE-089), iteration 2

Items re-checked: finding-1 expected-fix elements 7; product blobs 13 plus 2 fixture trees; tool runs 3 (run 7 procedure, reviewer mutants, full suite); mutants 12 (6 of the procedure, 6 of this reviewer), all killed. New findings: 0. Findings verified: 1 (Major). Iteration 2 effort: 32 turns, 45 minutes; cumulative 62 turns, 90 minutes (front matter).

### Record verdict

**Reviewer verdict: APPROVED**, with liens finding-2 to finding-5. The record `verdict` stays NEEDS CHANGES for two reasons. (a) The software assurance second review that plan WP-PDR-06 names is not filed (SA pair needed). (b) The reviewed blobs are on the CR-011 branch only, so an APPROVED verdict on `main` would fail the record drift rule. The software lead sets `verdict: APPROVED` at the CR-011 merge, when the SA pair is APPROVED and the blobs are unchanged. Any change to a blob of `product_files` before then needs a further delta iteration (rule C2). The owner's ruling on finding-2 and ACC-TRACE-002 are outside this verdict.

```
VERDICT (iteration 2, 2026-09-27): reviewer APPROVED (with liens finding-2 to finding-5); record verdict NEEDS CHANGES (held: SA pair not filed; branch-only blobs)
PRODUCT: TV-002 94ae3af5 at 2b004b1 (run 7 on 709e95f), tool d4cde9f5 unchanged
FINDINGS: finding-1 Major Verified; finding-2 to finding-5 Minor, lien due CDR; no Major open; no new finding
ITEMS N/A: TV-D3 (class B), TV-G2 to TV-G4 (repository tool)
RE-RUN: run 7 procedure at 2b004b1, exit 0, 235 tests, 6 of 6 mutants killed, output equal to the committed log; 6 reviewer mutants killed
MEASUREMENTS: elements verified=7; tool runs=3; new findings=0; iteration 2 turns=32, minutes=45; cumulative turns=62, minutes=90
```
