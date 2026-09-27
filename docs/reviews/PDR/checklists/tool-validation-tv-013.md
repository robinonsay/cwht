---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md section 13;
# docs/process/05-configuration-and-data-management.md section 9.2 step 3). Record of the independent review
# of TV-013 for ACC-MEASURE-001 (PDR work plan WP-PDR-08, record path as the plan names it).
# Item set applied: docs/templates/peer-review-checklist-tool-validation.md revision A, blob 7be809d4, on
# branch cr/CR-012-pdr-checklist-templates at 7784672 (APPROVED by INSP-033 iteration 2; CR-012 Submitted,
# not merged). The template is not on main, and tools/validate_docs.py rejects a checklist field whose
# template is absent from docs/templates/, so the checklist field names the code checklist, which this record
# applies to tools/measurements.py as item TV-G1-3 requires (03 section 6.1.1 row "Peer review"), as INSP-015
# did for the SRR Python tools.
id: INSP-041
checklist: peer-review-checklist-code
checklist_revision: B
checklist_file: docs/reviews/PDR/checklists/tool-validation-tv-013.md
product: docs/cm/tool-validation/TV-013-measurements.md
product_commit: "71bf509c948fbc8d4ae9b863f2a0226f0bf1bba0"
product_files: ["docs/cm/tool-validation/TV-013-measurements.md@9a7e2b552a4b5c10fa585b244c722b22ef9b2c6b", "docs/cm/tool-validation/evidence/measurements-2026-09-27.log.txt@8868280979b422742e7d04f6ee5869ffa37c8dd2", "tools/measurements.py@abe25acbcf3c7ae0bc3d2cd11ac490c026a61b7a", "tools/tests/test_measurements.py@7e7ba2bbdb3569ba42924b6d974bcdb70f69f58b", "tools/tests/fixtures/measurements/invalid.json@15231171b06297dfd45632bef5d22757374b0970", "tools/tests/fixtures/measurements/junit/empty.xml@a5e08f193d942833cc2b5283ff72e8740f7fa773", "tools/tests/fixtures/measurements/junit/run1.xml@cb071c37b1f13fa52fe0a9958aaababfb736f54b", "tools/tests/fixtures/measurements/junit/run2-diff.xml@7294a61c042aa6105dc84d79a702afc7518a4efb", "tools/tests/fixtures/measurements/junit/run2-same.xml@cb071c37b1f13fa52fe0a9958aaababfb736f54b", "tools/tests/fixtures/measurements/lcov/branch-condition.json@e569b1722f7fa5237f8c1b149a38e714d45b3f70", "tools/tests/fixtures/measurements/lcov/lcov.info@9368449affe9f81534ec020dcf2c983436ff343c", "tools/tests/fixtures/measurements/linkmap/cwht-app.map@e5557024967701cbee3661601e39572bf22afa80", "tools/tests/fixtures/measurements/linkmap/link.ld@8ab6e6e242e3daf0449ff34cb58f75168acabf40", "tools/tests/fixtures/measurements/linkmap/over-red-line.map@ab15c48a1463c8b124198eae273ea02d2877ea57", "tools/tests/fixtures/measurements/linkmap/small.ld@f6be72a5bfa9bcfbe99761771549e9fd95b810d1", "tools/tests/fixtures/measurements/records/records.json@5b760ab006e936e10d28130373b1c525c4dc79c1", "tools/tests/fixtures/measurements/valid.json@3938cd57aaeb99e1c5065594c915c99014d34026", "tools/toolchain.lock.md@82005d1b780e272dbf38cd8621d9707996e08f12", "docs/cm/tool-validation/README.md@b267ce08f53a5db8e32eb8cb217435a3efaf1833"]
fixture_trees: ["tools/tests/fixtures/measurements@39141b58900149f3506c2caedfa9bf8512d89669"]
tv_ids: [TV-013]
tool_class: B
tool_kind: repository-tool
acc_proposed: [ACC-MEASURE-001]
product_size: 1 record (87 lines), 6 purposes, 16 known-answer tests, 13 fixture files; tool 456 lines, test module 227 lines
sprint: PDR-prep
author_agent: "author:SRR R3 and WP-PDR-08 (Claude as software lead and tool owner)"
tool_author_agent: "author:SRR R3 (Claude as tool maintainer)"
reviewer_agent: "reviewer:WP-PDR-08-tv-013 (independent, iteration 1)"
criticality: neither
# assurance_required: the TV template (CR-012) says false; PDR work plan WP-PDR-08 names "independent reviewer
# plus SA". Section H is answered here as the template directs; the separate SA invocation the plan names is
# requested from the lead SE (return fix_requests "SA pair needed").
assurance_required: true
assurance_reviewer_agent: "pending (separate invocation, PDR work plan WP-PDR-08)"
iteration: 1
readiness_met: true
reviewer_verdict: NEEDS CHANGES
assurance_verdict: pending
verdict: NEEDS CHANGES
findings_major: 1
findings_minor: 3
findings_open: 4
findings_fixed: 0
findings_verified: 0
findings_deferred: 0
assurance_tasks_applied: [swe-136 7.1 task 1, swe-070 7.1 task 1]
deferred_rids: []
items_no: [TV-B3, TV-C2, TV-D2, TV-F3, TV-G1-2]
effort_turns: 20
effort_minutes: 30
record_status: Open
date: 2026-09-27
date_closed: null
---

# Peer review record INSP-041: TV-013, `tools/measurements.py`

**Product:** `docs/cm/tool-validation/TV-013-measurements.md` at `71bf509` (blob `9a7e2b55`), with the tool, its known-answer module and fixture at the blobs of `product_files` (unchanged since `3de1e2d`). **Checklist:** the item set of `docs/templates/peer-review-checklist-tool-validation.md` revision A (CR-012 branch `7784672`), `tool_kind` repository-tool, so sections A to F, G1 and H; the code review of item TV-G1-3 uses `docs/templates/peer-review-checklist-code.md` revision B, Rust-specific items N/A (front matter comment). **Acceptance criteria (rule C7):** every item of sections A to F, G1 and H; every purpose 1 to 6 of TV-013 section 2 has a known answer that exercises each clause it states; the 05 section 9.2 row for `tools/measurements.py`; TV-013 section 8's own request (re-run section 3 and recompute the over-red-line answers from the fixture map).

**Independence (rule C4):** this invocation authored neither the tool nor TV-013 and edited no product file. **Search first:** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: a code review of `tools/measurements.py`; the `--diff-runs`, `--link-map` and `--check-records` modes). `grep -n` was used afterwards only to pin lines. **Pending change:** WP-PDR-09 changes `tools/measurements.py` for C-185 in wave 1 (TV-013 section 8); `git rev-parse HEAD:tools/measurements.py` is still `abe25acb` at this review, so this record covers blob `abe25acb`, and the C-185 change is a re-validation trigger with its own delta.

## Reviewer re-run and checks

| Check | Command | Exit | Result | Same as record? |
|---|---|---|---|---|
| TV-C5 re-run, twice | `git archive 71bf509` into the scratchpad; `.venv/bin/python -m unittest discover -s tools/tests -p test_measurements.py` | 0, 0 | `Ran 16 tests`, `OK`, 0 skipped, both passes | yes (run 2) |
| Over-red-line answer by hand (TV-013 section 8) | read `linkmap/over-red-line.map` and `small.ld` | n/a | FLASH extent = highest LMA end: `.data` LMA `0x10000300` + `0x10` = `0x10000310`, less origin `0x10000000` = `0x310` = 784 B, 784 / 1024 = 76.5625 percent, above 70; RAM extent: `.bss` VMA `0x20000010` + `0xf0` = `0x20000100`, 256 B, 25.00 percent | yes, equals the stored `FAIL FLASH used 784 B ... 76.56 %` and `PASS RAM used 256 B ... 25.00 %` |
| Mutation 1 (finding-1) | `measurements.py:189` changed to `ok = bool(a) and a == b` in the export; module re-run | 0 | 16 tests `OK`: no test detects the removal of the "all passed" clause | n/a |
| Real tool on two identical failing runs | `measurements.py --diff-runs fail.xml fail.xml` (one `failure` case in both) | 1 | `NOT PASSED ('c', 't', 'failure')`, `FAIL identical result sets, all passed` | tool correct |
| Mutation 2 (finding-2) | `measurements.py:322` `if sup.get("id") != r.get("id"):` changed to `if False:`; module re-run | 0 | 16 tests `OK`: the "supersedes another id" rule is not exercised | n/a |
| Identity | `git rev-parse 71bf509:<path>` | 0 | tool `abe25acb`, test `7e7ba2bb`, fixture tree `39141b58`, 13 fixture files, equal to TV-013 section 1 and run 2 and to HEAD | yes |

The export and mutated copies were in the scratchpad only; the repository files were not changed.

## Record

### Findings

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | reviewer | Major | TV-B3, TV-C2 | TV-013 section 2 purpose 2; `tools/tests/test_measurements.py` `DiffRunsTests`; `measurements.py:189` | Purpose 2 states `--diff-runs` passes "only when identical, non-empty and all passed" (SWE-186, gate G3). No known answer exercises the "all passed" clause: `run2-diff.xml` fails because it differs, not because a case failed, and mutation 1 (clause removed) passes all 16 tests. The clause is what makes G3 reject two identical failing runs. The tool is correct (reviewer run above), so the gap is in the validation, which is the INSP-015 F-01 class the template makes Major. Fix: add a known answer with two identical JUnit files holding a failed case (expect exit 1 and the `NOT PASSED` line), and one with identical skipped cases if skipped is to fail too; re-run and record TV-013 run 3 | Open | Pending | |
| <a id="finding-2"></a>finding-2 | reviewer | Minor | TV-B3, TV-G1-2 | TV-013 section 2 purposes 3, 4, 6; test module | Other stated behaviour has no known answer: purpose 4 "supersedes a record of another id" (`measurements.py:322`, mutation 2 survives) and "evidence ... does not exist" (`:369`); purpose 3 the emulation report when present (`:256`) and a malformed `--branch-condition` export, exit 2 (`:248`); purpose 6 exit 2 on an unreadable JUnit file (`:167`). Fix: one test per clause, or narrow the purposes to what the tests exercise | Open | Pending | |
| <a id="finding-3"></a>finding-3 | reviewer | Minor | TV-G1-3 (code review), TV-E1 | `tools/measurements.py:372`, `:211` | (a) The MSR-18 and MSR-19 re-derivation of `--check-records` is skipped without any line when the linker script is absent (`and link_ld.is_file()`), and the default script is `../rustos/firmware/pico2/link.ld`, outside the repository; a run where it is missing prints PASS with no re-derivation note, against the tool's own "reported, never skipped" rule for evidence and against purpose 4. Fix: emit a NOTE or FAIL when a cited map cannot be re-derived. (b) `crate_of` returns the first path part (`/`) for a source outside `firmware/` or `rustos/`, so the MSR-13 line reads `MSR-13 /:` (observed by the reviewer on the `cov-kat` lcov); cosmetic for the gate, which always passes workspace paths | Open | Pending | |
| <a id="finding-4"></a>finding-4 | reviewer | Minor | TV-D2, TV-F3, TV-A3 | TV-013 title and section 1 column "State against commit `400e59d`"; lock section 1.1 row `tools/measurements.py` (line 100) and section 1.2 row (line 120); README index row TV-013 (line 37) and common owner action 3 (line 55) | The identification and indexes still describe the pre-commit state: the title says "working tree on 400e59d", section 1 says "untracked", the lock section 1.1 row records only the 2026-09-26 working-tree run (not run 2 at `d3de579`), the section 1.2 row says "untracked", the README row says "working-tree blob `abe25acb`, new" and owner action 3 still lists TV-013 as "open again". Fix: name commit `3de1e2d` and blob `abe25acb` in the title and section 1, add run 2 to lock section 1.1, update the section 1.2 and README rows and owner action 3, and state ACC-MEASURE-001 on blob `abe25acb` directly | Open | Pending | |

### Per-record results

| TV record | Tool and version | Class | Commit tested | Reviewer re-run (command, exit, result) | Items answered No | Finding ids |
|---|---|---|---|---|---|---|
| TV-013 | `tools/measurements.py` blob `abe25acb` | B | `d3de579` (run 2; blobs equal at `3de1e2d`, `71bf509` and HEAD) | `unittest -p test_measurements.py` on an export of `71bf509`, twice; exit 0; 16 OK; same | TV-B3, TV-C2, TV-D2, TV-F3, TV-G1-2 | finding-1 to finding-4 |

### Per-purpose results

| TV record | Purpose | Known answer that exercises it | Seeded fault (class B) | Cited uses of the purpose | Finding ids |
|---|---|---|---|---|---|
| TV-013 | 1 `--link-map` | `test_fw_b0_map_reproduces_the_seed_records`, `test_pass_on_the_fw_b0_map`, `test_assessment_rules` | `test_red_line` (784 B, exit 1); `test_missing_map_or_region_is_a_usage_error` | gate G2; MSR-18, MSR-19; TPM-010, TPM-011 | none |
| TV-013 | 2 `--diff-runs` | `test_identical_runs_pass` | `test_seeded_difference_fails`, `test_empty_run_fails`; no identical-failing case | gate G3; TV-020 K20-6; SWE-186 | finding-1 |
| TV-013 | 3 `--coverage` | `test_totals` (hand-counted lcov and llvm-cov JSON) | `test_optional_inputs_not_produced_and_lcov_required` (missing lcov exit 2) | gate G6; MSR-13, MSR-14 | finding-2 |
| TV-013 | 4 `--check-records` | `test_committed_records_pass_and_values_are_rederived`, `test_git_rules_not_applied_outside_a_work_tree` | `test_seeded_record_faults` (six FAIL lines), `test_rederivation_mismatch_in_a_commit` | 07 section 11.1 record rules on `docs/plan/measurements.json` | finding-2, finding-3 |
| TV-013 | 5 `--analyze` | `test_analyze_current_records` | n/a (report; the supersedes and retirement cases are in the fixture) | 07 section 11.3 | none |
| TV-013 | 6 exit statuses and no writes | `UsageTests`, the exit assertions above | usage errors exit 2 | gate step status | finding-2 |

## Readiness criteria

| # | Criterion | Answer | Evidence |
|---|---|---|---|
| R1 | Committed and identified | Yes | blobs and tree above equal at `71bf509` and HEAD; the brief's list did not name the tool, test module and fixture files, which the template requires, so this record adds them |
| R2 | Known-answer command exits 0 | Yes | reviewer re-run |
| R3 | unit tests and `validate_docs.py` pass | No, not attributable to this product | pre-existing SRR drift failures (INSP-040 readiness R3) |
| R4 | Lock rows and README index | Yes, stale (finding-4) | lock section 1.1 and 1.2 rows; README row TV-013 |
| R5 | Author return | Yes (partly) | TV-013 section 4 run 2 and the WP-PDR-08 summary |

## A. Identification

| Id | Answer | Evidence |
|---|---|---|
| TV-A1 | Yes | repository tool; the run 2 log names the blobs |
| TV-A2 | N/A | repository tool; interpreter is TV-001 |
| TV-A3 | Yes, wording stale (finding-4) | recomputed blobs `abe25acb`, `7e7ba2bb`, tree `39141b58` with 13 files |
| TV-A4 | Yes | run 2 at `d3de579` holds the three identities (`git rev-parse`) |
| TV-A5 | Yes | class B: gate G2, G3, G6 outputs are verification evidence |
| TV-A6 | Yes | unittest from the command line |

## B. Purposes

| Id | Answer | Evidence |
|---|---|---|
| TV-B1 | Yes | each purpose names the mode, output and exit |
| TV-B2 | Yes | uses found: `tools/sw_gate.sh:161`, `:251`, `:366` (G2, G3, G6); TV-020 K20-6; 07 section 11; `tools/README.md` measurements section; all map to purposes 1 to 6 |
| TV-B3 | No | finding-1 (purpose 2), finding-2 (purposes 3, 4, 6) |

## C. Known-answer test

| Id | Answer | Evidence |
|---|---|---|
| TV-C1 | Yes | `tools/tests/fixtures/measurements/`; command and 16-test criterion in section 3 |
| TV-C2 | No | purpose 2 "all passed" clause has no seeded case (finding-1) |
| TV-C3 | Yes | link map values transcribed from the TC-SW-TOOL-001-r1 gate log (independent); red-line map hand-computed (reviewer recomputed); lcov totals hand-counted; the section 3 text states each |
| TV-C4 | Yes | 05 section 9.2 row for `tools/measurements.py` (lock section 1.1 line 100) is implemented by the 16 tests |
| TV-C5 | Yes | reviewer re-run equals run 2 |

## D. Results and reproducibility

| Id | Answer | Evidence |
|---|---|---|
| TV-D1 | Yes | section 4 run 2 with commit, blobs, count; `evidence/measurements-2026-09-27.log.txt` shows 16 OK twice |
| TV-D2 | No | lock section 1.1 row lacks run 2 (finding-4) |
| TV-D3 | N/A | class B |

## E. Limitations and triggers

| Id | Answer | Evidence |
|---|---|---|
| TV-E1 | Yes, with finding-3 | limitation 4 confirmed in code (`mode_coverage` returns 0 always, `:257`); limitation 5 confirmed (`SECTION_LINE` regex `:104` reads the lld layout only); limitation 1 confirmed (no write path in the tool) |
| TV-E2 | Yes | tool, test, fixture, linker-script layout, map format, records format, interpreter, git and defect triggers |

## F. Accreditation readiness and indexes

| Id | Answer | Evidence |
|---|---|---|
| TV-F1 | Yes, wording (finding-4) | ACC-MEASURE-001 names purposes 1 to 6, blob, interpreter and git |
| TV-F2 | Yes | due PDR (05 section 13 PDR row); filed at SRR because TC-SW-TOOL-001-r2 cited it first |
| TV-F3 | No | README row and lock section 1.2 row stale (finding-4) |
| TV-F4 | Yes | section 9 pending the owner; developer evidence until then |
| TV-F5 | N/A | not yet accredited |

## G1. Repository tool

| Id | Answer | Evidence |
|---|---|---|
| TV-G1-1 | Yes | every test is fixture-only (temporary git repositories and fixture files); no repository-content test in the module |
| TV-G1-2 | No | exit 0, 1 and 2 each have known answers, but not every documented exit-2 cause (unreadable JUnit, malformed llvm-cov JSON) (finding-2) |
| TV-G1-3 | Yes, performed here | no earlier code review exists (INSP-016 line 418 leaves it to the TV record reviews); section "Code review" below |

## H. Software assurance tasks

| Id | Answer | Evidence |
|---|---|---|
| TV-H1 | Yes, with finding-1 | gate steps G2 (`--link-map`), G3 (`--diff-runs`) and G6 (`--coverage`) of 07 section 8.4 are purposes 1 to 3 |
| TV-H2 | N/A | not an analysis tool |
| TV-H3 | Yes | front matter |

## Code review of `tools/measurements.py` blob `abe25acb` (checklist `peer-review-checklist-code` revision B; Python tool, Rust-specific items N/A)

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-A2 | Yes | standard library only (`:68` to `:76`); `git` subprocess |
| CK-CODE-C1 | Yes | no bare `except`; every external failure is `UsageError` (exit 2) or a FAIL line; `main` catches `UsageError` only (`:449`) |
| CK-CODE-C2 | Yes | modes return `(status, lines)`; status 0 or 1; usage 2 |
| CK-CODE-D2 | Yes | no recursion; loops over finite inputs |
| CK-CODE-D7 | Yes | 456 lines; longest function `check_records` 77 lines (`:305` to `:381`), above the 60-line CS-18 guide, which is written for firmware; noted, not a finding |
| CK-CODE-E1 | Yes, with finding-3 | behaviour matches the docstring and TV-013 section 2 except the silent re-derivation skip (`:372`) |
| CK-CODE-E9 | Yes | no dead code found |
| CK-CODE-G1 | Yes | inputs are parsed defensively (`ET.ParseError`, `JSONDecodeError`, regex matches); `subprocess.run` with an argument list, no shell |
| CK-CODE-I1 | Yes | module docstring documents every mode and exit status |
| CK-CODE-I4 | Yes | comments state reasons (`:81` to `:83`, `:203`) |
| CK-CODE-J4 | Yes | `wc -l` 456 |
| Other items | N/A | no_std, unsafe, MMIO, panic handler, traceability tags, safety items are Rust firmware items |

## Measurements (SWE-089)

| Measure | Value |
|---|---|
| Product size | 1 record (87 lines), 6 purposes, 16 tests, 13 fixture files; tool 456 lines, test module 227 lines |
| Items checked | R1 to R5, A1 to A6, B1 to B3, C1 to C5, D1 to D3, E1 to E2, F1 to F5, G1-1 to G1-3, H1 to H3 (35), plus 11 code items |
| Items answered No | 5 (TV-B3, TV-C2, TV-D2, TV-F3, TV-G1-2); R3 No (not attributable) |
| Items N/A | TV-A2, TV-D3, TV-F5, TV-H2, G2 to G4 |
| Findings by severity | Major 1, Minor 3 |
| Findings fixed, deferred | 0, 0 |
| Iteration | 1 |
| Effort | 20 turns, 30 minutes |

No visual product was produced or changed by this review (charter section 11 rule 3).

## Cross items (outside this record's scope; for the lead SE)

- **X-1.** As INSP-040 X-1 (checklist field) and X-2 (SA pair versus the template's `assurance_required: false`).
- **X-2.** WP-PDR-09 (C-185, PASS lines) changes blob `abe25acb`; its commit re-runs section 3 and the fixes of findings 1 to 3 can ride on the same TV-013 run 3, followed by one delta of this record.

## Verdict

```
VERDICT: NEEDS CHANGES
PRODUCT: TV-013 at 71bf509c948fbc8d4ae9b863f2a0226f0bf1bba0 (tool blob abe25acb, run 2 at d3de579)
FINDINGS:
- [Major] TV-C2 purpose 2: the "all passed" clause of --diff-runs has no known answer (mutation survives).
- [Minor] TV-B3 untested clauses of purposes 3, 4 and 6.
- [Minor] code: silent skip of the MSR-18/19 re-derivation without a linker script; crate_of fallback.
- [Minor] TV-D2/TV-F3 stale title, section 1, lock and README rows.
ITEMS N/A: TV-A2, TV-D3, TV-F5, TV-H2, G2 to G4
RE-RUN: unittest discover -p test_measurements.py on an export of 71bf509; exit 0; 16 tests; same as run 2
MEASUREMENTS: size=1 record, 6 purposes; turns=20; minutes=30; major=1; minor=3
```
