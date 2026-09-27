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
# product_commit: iteration 3 (delta, 2026-09-27) re-identifies the product at main 3aed3c4: the lock and README
# drifted (b45c8654 to e1c811b0, 87fb1e8c to 7c90f143, commits 2bfe001 to 1db319a, WP-PDR-07 only); every hunk
# was read and none touches a TV-013 or measurements.py line; the other 20 blobs and the fixture tree are unchanged.
# Iteration 2 (delta, 2026-09-27) reviewed the blobs frozen at c827202 (TV-013, run 3 evidence,
# lock, README) with the test module and the two new fixtures of c28dd60 (equal at c827202 and HEAD); tool blob
# abe25acb unchanged. Iteration 1 reviewed 71bf509: TV-013 9a7e2b55, test module 7e7ba2bb, fixture tree
# 39141b58 (13 files), lock 82005d1b, README b267ce08
product_commit: "3aed3c4362c6ffc03a1265bf0d63a6893990d165"
product_files: ["docs/cm/tool-validation/TV-013-measurements.md@71a676ef74ba9990dc307d97ed82015f06be5ec2", "docs/cm/tool-validation/evidence/measurements-2026-09-27.log.txt@8868280979b422742e7d04f6ee5869ffa37c8dd2", "docs/cm/tool-validation/evidence/measurements-2026-09-27-r3.log.txt@eff9035ff7a85ac9c7e7778d755ed5f028510909", "tools/measurements.py@abe25acbcf3c7ae0bc3d2cd11ac490c026a61b7a", "tools/tests/test_measurements.py@7ccc293e102f58c62d676b94074bc17b3232e166", "tools/tests/fixtures/measurements/invalid.json@15231171b06297dfd45632bef5d22757374b0970", "tools/tests/fixtures/measurements/junit/empty.xml@a5e08f193d942833cc2b5283ff72e8740f7fa773", "tools/tests/fixtures/measurements/junit/run1.xml@cb071c37b1f13fa52fe0a9958aaababfb736f54b", "tools/tests/fixtures/measurements/junit/run2-diff.xml@7294a61c042aa6105dc84d79a702afc7518a4efb", "tools/tests/fixtures/measurements/junit/run2-same.xml@cb071c37b1f13fa52fe0a9958aaababfb736f54b", "tools/tests/fixtures/measurements/junit/run-failing.xml@13eb0ded84967e44f211202655fc0b66c42bd120", "tools/tests/fixtures/measurements/junit/run-skipped.xml@11e505175f394fbe934624cffc91371ea0faf775", "tools/tests/fixtures/measurements/lcov/branch-condition.json@e569b1722f7fa5237f8c1b149a38e714d45b3f70", "tools/tests/fixtures/measurements/lcov/lcov.info@9368449affe9f81534ec020dcf2c983436ff343c", "tools/tests/fixtures/measurements/linkmap/cwht-app.map@e5557024967701cbee3661601e39572bf22afa80", "tools/tests/fixtures/measurements/linkmap/link.ld@8ab6e6e242e3daf0449ff34cb58f75168acabf40", "tools/tests/fixtures/measurements/linkmap/over-red-line.map@ab15c48a1463c8b124198eae273ea02d2877ea57", "tools/tests/fixtures/measurements/linkmap/small.ld@f6be72a5bfa9bcfbe99761771549e9fd95b810d1", "tools/tests/fixtures/measurements/records/records.json@5b760ab006e936e10d28130373b1c525c4dc79c1", "tools/tests/fixtures/measurements/valid.json@3938cd57aaeb99e1c5065594c915c99014d34026", "tools/toolchain.lock.md@e1c811b08b742e8ad24ff053efc9c4476fbffd29", "docs/cm/tool-validation/README.md@7c90f14310f7deedf518596bc57c5b4c7e2fc277"]
fixture_trees: ["tools/tests/fixtures/measurements@ed4414ecd9336349d4ba03cd8257b0079d470d8d"]
tv_ids: [TV-013]
tool_class: B
tool_kind: repository-tool
acc_proposed: [ACC-MEASURE-001]
product_size: 1 record (92 lines), 6 purposes, 18 known-answer tests, 15 fixture files; tool 456 lines, test module 256 lines
sprint: PDR-prep
author_agent: "author:SRR R3 and WP-PDR-08 (Claude as software lead and tool owner)"
tool_author_agent: "author:SRR R3 (Claude as tool maintainer)"
reviewer_agent: "reviewer:WP-PDR-08-tv-013-iter3 (independent; authored no part of WP-PDR-08 or the tool; iteration 2 by reviewer:WP-PDR-08-tv-013-iter2, iteration 1 by reviewer:WP-PDR-08-tv-013)"
criticality: neither
# assurance_required: the TV template (CR-012) says false; PDR work plan WP-PDR-08 names "independent reviewer
# plus SA". Section H is answered here as the template directs; the separate SA invocation the plan names is
# filed as INSP-049 (iteration 3 of this record names the pairing, 07 section 2.1.1 and 10.2 Record row).
assurance_required: true
assurance_reviewer_agent: "sa-reviewer:WP-PDR-08-tv-013 (paired record INSP-049, docs/reviews/PDR/checklists/tool-validation-tv-013-software-assurance.md; 07 section 2.1.1)"
paired_record: INSP-049
iteration: 3
readiness_met: true
reviewer_verdict: APPROVED
# assurance_verdict: copied from the paired record INSP-049 (iteration 1, APPROVED; one Minor lien)
assurance_verdict: APPROVED
# verdict: held at NEEDS CHANGES (lead SE convention of 2026-09-27): both lenses are APPROVED and every product
# blob is on main, but the item set applied exists only on the unmerged branch cr/CR-012-pdr-checklist-templates
# (template blob 7be809d4 at 7784672); the software lead sets APPROVED on INSP-041 and INSP-049 when CR-012
# merges with that template blob unchanged
verdict: NEEDS CHANGES
findings_major: 1
findings_minor: 3
# findings_open: no finding is Open; finding-1 Verified, finding-2 to finding-4 liens due CDR (rule C1)
findings_open: 0
findings_fixed: 0
findings_verified: 1
findings_deferred: 0
assurance_tasks_applied: [swe-136 7.1 task 1, swe-070 7.1 task 1]
deferred_rids: []
# items_no: at iteration 2 (TV-C2 and TV-D2 of iteration 1 are Yes; TV-B3 stays No for finding-2 only)
items_no: [TV-B3, TV-F3, TV-G1-2]
effort_turns: 40
effort_minutes: 57
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

## Iteration 2: delta verification of finding-1 (Major) (2026-09-27)

**Scope (rule C1).** Iteration 2 is a delta that verifies the Major fix only. Products at the frozen blobs of `product_files`: TV-013 blob `71a676ef`, evidence `measurements-2026-09-27-r3.log.txt` blob `eff9035f`, lock `b45c8654` and README `87fb1e8c` (from `c827202`); test module `7ccc293e`, fixtures `junit/run-failing.xml` `13eb0ded` and `junit/run-skipped.xml` `11e50517`, fixture tree `ed4414ec` (15 files) (from `c28dd60`). Each blob was recomputed with `git rev-parse c827202:<path>` and `git rev-parse HEAD:<path>` at HEAD `c827202`: all equal to the brief. The tool itself is unchanged (`tools/measurements.py` blob `abe25acb`, the blob of iteration 1). The delta was read as `git diff 71bf509 c827202` on TV-013, the test module, the fixture directory, the lock and the README (WP-PDR-08 hunks only).

**Independence (rule C4).** This invocation authored neither the tool nor any part of WP-PDR-08, did not write iteration 1 of this record, and edited no product file. **Search first:** as INSP-040 iteration 2 (`mcp__claude-context__search_code` first; `grep -n` only to pin lines). **Software assurance participant:** not performed here (fix request "SA pair needed").

### Reviewer checks (iteration 2)

| Check | Command | Exit | Result | Same as record? |
|---|---|---|---|---|
| TV-C5 re-run, twice | `git archive c827202 tools` into the scratchpad; `.venv/bin/python -m unittest discover -s tools/tests -p test_measurements.py` | 0, 0 | `Ran 18 tests`, `OK`, both passes | yes (run 3: 18 OK twice) |
| Mutation 1 of iteration 1 | in the export, `measurements.py:189` changed to `ok = bool(a) and a == b`; module re-run | 1 | `FAILED (failures=2)`: `test_identical_failing_runs_fail` and `test_identical_skipped_runs_fail` | yes (run 3 mutation check, log lines 51 to 56) |
| Expected output by hand | read `junit/run-failing.xml` and `run-skipped.xml` against `measurements.py:185` to `:192` | n/a | each file has 3 cases, one `failure` (or `skipped`) on `cwht-core::heartbeat` `spin_wait_counts`; compared with itself: `passed in both: 2`, no DIFF line, one `NOT PASSED ('cwht-core::heartbeat', 'spin_wait_counts', 'failure'|'skipped')`, `FAIL identical result sets, all passed (SWE-186)`, exit 1; equal to the stored assertions | yes |

The export and the mutated copy were in the scratchpad only.

### Verification of finding-1 (Major)

| # | Expected fix element (iteration 1) | Product now | Independent check | Result |
|---|---|---|---|---|
| 1 | A known answer with two identical JUnit files holding a failed case: exit 1 and the `NOT PASSED` line | `test_identical_failing_runs_fail` with `junit/run-failing.xml`, asserting exit 1 and the exact three output lines | Hand derivation and reviewer run above; the pair is identical and non-empty, so only the "all passed" clause can fail it | Holds |
| 2 | One with identical skipped cases, if skipped is to fail | `test_identical_skipped_runs_fail` with `junit/run-skipped.xml`; TV-013 section 3 states a skipped case is not passed | Same; a mutation treating `skipped` as passed would also be caught by this test | Holds |
| 3 | Re-run and record TV-013 run 3 | Section 4 row 3 at `c28dd60`, 18 tests twice, mutation check; section 1 identifies the new test blob and fixture tree; section 3 pass criteria now 18 tests, `DiffRunsTests` 5; lock section 1.1 row and lock log row updated | Evidence log `eff9035f` equals the row (identities, two passes of 18 OK, mutation 2 of 18 fail); reviewer run agrees | Holds |

**finding-1: Verified.** Purpose 2 now has a known answer for each of its three clauses (identical, non-empty, all passed), and the iteration 1 mutation is killed. TV-C2 is Yes. TV-D2 is also Yes now: the lock section 1.1 row names run 3 at a commit.

### Scan of the delta for new defects

No new finding. The two tests compare a file with itself (same path twice); that isolates the "all passed" clause as intended, and the "identical" clause remains covered by `test_seeded_difference_fails`. The run 3 record, the evidence log and the lock row agree.

### Findings (iteration 2; current state of every finding of this record)

| Finding | Severity | State | Disposition |
|---|---|---|---|
| finding-1 | Major | Verified | Closed at iteration 2 on test module `7ccc293e`, fixtures `13eb0ded` and `11e50517`, TV-013 `71a676ef` run 3 |
| finding-2 | Minor | Lien: fix before CDR | Untested clauses of purposes 3, 4 and 6 (mutation 2 still survives: the new tests do not touch `--check-records`). Owner: Claude as tool owner (WP-PDR-08; the tool change rides on the WP-PDR-09 C-185 revision of `tools/measurements.py`, X-2); due the CDR readiness declaration; listed in PDR package section 15 |
| finding-3 | Minor | Lien: fix before CDR | Silent MSR-18/19 re-derivation skip and `crate_of` fallback (observed again in the INSP-040 iteration 2 reviewer run: `MSR-13 /: lines 5/6`). Same owner, due and route |
| finding-4 | Minor | Lien: fix before CDR | Partly fixed: lock section 1.1 row now names run 3. Still stale: TV-013 title ("working tree on 400e59d"), section 1 column "State against commit `400e59d`" row for the tool ("untracked (new)"), lock section 1.2 row ("untracked"), README row TV-013 ("working-tree blob `abe25acb`, new"; no run 3) and common owner action 3. Same owner and due |

Findings by severity: 1 Major (Verified), 3 Minor (liens). Zero Major findings remain.

### Checklist answers changed at iteration 2

| Id | Iteration 1 | Iteration 2 | Evidence |
|---|---|---|---|
| TV-C2 | No | Yes | identical failing and skipped runs seeded |
| TV-D2 | No | Yes | lock section 1.1 row names run 3 at `c28dd60` |
| TV-B3 | No | No (finding-2 only, lien) | purpose 2 now fully exercised |
| TV-F3 | No | No (finding-4, lien) | README row and lock section 1.2 row still stale |
| TV-G1-2 | No | No (finding-2, lien) | unchanged |

### Measurements (SWE-089), iteration 2

Items re-checked: finding-1 expected-fix elements 3; product blobs 8 identities; reviewer runs 3 (two passes, one mutation). New findings: 0. Findings verified: 1 (Major). Iteration 2 effort: 8 turns, 12 minutes; cumulative 28 turns, 42 minutes (front matter).

### Record verdict

**Reviewer verdict: APPROVED**, with liens finding-2 to finding-4. The record `verdict` stays NEEDS CHANGES until the separate software assurance invocation of WP-PDR-08 is filed and APPROVED (SA pair needed). This APPROVED reviewer lens covers tool blob `abe25acb`; the WP-PDR-09 C-185 change of `tools/measurements.py` is a re-validation trigger (TV-013 section 7) and needs its own delta iteration of this record.

```
VERDICT (iteration 2, 2026-09-27): reviewer APPROVED (with liens finding-2 to finding-4); record verdict NEEDS CHANGES (held: SA pair not filed)
PRODUCT: TV-013 71a676ef at c827202; tool abe25acb; test module 7ccc293e and fixture tree ed4414ec at c28dd60
FINDINGS: finding-1 Major Verified; finding-2 to finding-4 Minor, lien due CDR; no Major open
ITEMS N/A: TV-A2, TV-D3, TV-F5, TV-H2, G2 to G4 (unchanged)
RE-RUN: unittest discover -p test_measurements.py on an export of c827202, twice; exit 0; 18 tests OK; mutation 1 fails 2 of 18; same as run 3
MEASUREMENTS: elements verified=3; new findings=0; iteration 2 turns=8, minutes=12; cumulative turns=28, minutes=42
```

## Iteration 3: delta re-identification of the drifted blobs (2026-09-27)

**Scope (rule C1).** A delta, not a new review: two of the 22 blobs of `product_files` drifted on main after iteration 2, `tools/toolchain.lock.md` `b45c8654` to `e1c811b0` and `docs/cm/tool-validation/README.md` `87fb1e8c` to `7c90f143`, through commits `2bfe001`, `d9c7f69`, `99feb43`, `f47360a`, `bd78bd5` and `1db319a` (all WP-PDR-07: TV-014 runs 4 to 6 and accreditation, TV-015 to TV-019 filing). The brief named `be96420b` and `f4757da2`, the blobs at `bd78bd5`; main moved on to `1db319a` before this iteration, so this record takes the current blobs at main `3aed3c4`. The tool, the test module, the fixture tree `ed4414ec`, TV-013 `71a676ef` and both evidence logs were recomputed with `git rev-parse HEAD:<path>` and equal iteration 2. No reviewer re-run is needed: no executable, fixture or expected value changed.

**Independence (rule C4).** This invocation authored no part of WP-PDR-07, WP-PDR-08 or the tool, wrote neither earlier iteration nor INSP-049, and edited no product file. **Search first:** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` (query: the lock row and TV-013 validation status of `tools/measurements.py`) ran before any `grep`.

### Hunks read (`git diff c827202 3aed3c4`)

| File | Hunk (new lines) | Content | Touches TV-013 or `tools/measurements.py`? |
|---|---|---|---|
| lock | 11 to 12, 14 | kicad-cli, LTspice and CrossOver rows of section 1: TV-014 status and wrapper blob `88b71475`, Accredited | No |
| lock | 45 to 46 | OpenSCAD and FreeCAD rows: TV-015 status | No |
| lock | 67 to 68, 70, 96 | section 1.1 rows kicad-cli, `normalize_fab.py`, LTspice, scad2step: run results | No |
| lock | 101 to 103 | new section 1.1 rows `render_tpm.py`, `csa.py`, `check_commit_msg.py` (after the `measurements.py` row at line 100, which is unchanged) | No |
| lock | 122, 124 to 128 | section 1.2 rows `render_tpm.py`, `csa.py`, `check_commit_msg.py`, `ltspice-batch.sh`, `normalize_fab.py`, `scad2step.py`: "not written" to "exists" | No (the `measurements.py` row moves from line 120 to 123, text unchanged) |
| lock | 177 | section 1.4 finding 15 (orphaned Wine services, TV-014 run 4) | No |
| lock | 269 to 274 | section 2 index rows TV-014 to TV-019 | No (TV-013 row, now line 268, unchanged) |
| lock | 312 to 316 | five log rows for WP-PDR-07 (TV-014 runs 4 to 6, TV-015 run 2, wave 1a tools) | No |
| README | 38 to 43 | index row TV-014 updated (Validated, Accredited ACC-LTSPICE-001); new rows TV-015 to TV-019 | No (TV-013 row, line 37, unchanged) |

Every line of the lock and README that names `measurements` or TV-013 was compared as text at `c827202` and at `3aed3c4`: identical (same digest of the extracted lines), only line numbers shift. The drift therefore changes no answer of this record.

### Effect on the findings

| Finding | State | Iteration 3 note |
|---|---|---|
| finding-1 | Verified (iteration 2) | unaffected |
| finding-2 | Lien: fix before CDR | unaffected |
| finding-3 | Lien: fix before CDR | unaffected |
| finding-4 | Lien: fix before CDR | unaffected in substance, still stale; locations now lock section 1.2 row line 123 (was 120), lock section 2 row TV-013 line 268, README row TV-013 line 37 and owner action 3 line 60 (was 55). The new README rows TV-014 to TV-019 each name a committed blob and run commit, which makes the TV-013 row ("working-tree blob `abe25acb`, new") the only index row of a committed PDR tool still described as uncommitted; no new finding (same defect, same fix) |

New findings: 0. No Major is open; the three Minor findings stay liens due the CDR readiness declaration (PDR package section 15).

### Pairing (07 section 10.2 Record row)

This iteration names the paired software assurance record INSP-049 (`tool-validation-tv-013-software-assurance.md`, `assurance_verdict: APPROVED`, one Minor lien) in `paired_record` and `assurance_reviewer_agent`, and copies its assurance verdict. INSP-049 names the same `product_files` as iteration 2 (lock `b45c8654`, README `87fb1e8c`); its own delta for the same drift is for its reviewer (each reviewer updates only its own record); this record's reading of the hunks above applies unchanged to the assurance lens, since no hunk touches the product.

### Measurements (SWE-089), iteration 3

Blob identities recomputed: 22 and one fixture tree. Hunks read: 13 (lock 12, README 1). New findings: 0. Iteration 3 effort: 12 turns, 15 minutes; cumulative 40 turns, 57 minutes (front matter). Iteration count 3 of the 07 section 10.2 maximum, reached with no Major open, so no escalation.

### Record verdict (iteration 3)

**Reviewer verdict: APPROVED** (liens finding-2 to finding-4), unchanged. **Assurance verdict: APPROVED** (INSP-049). **Record verdict: NEEDS CHANGES, held** under the lead SE convention: the checklist item set applied exists only on the unmerged `cr/CR-012-pdr-checklist-templates` (`7784672`, template blob `7be809d4`). The software lead sets APPROVED on this record and INSP-049 when CR-012 merges with that template blob unchanged. The WP-PDR-09 C-185 change of `tools/measurements.py` remains a re-validation trigger needing its own delta.

```
VERDICT (iteration 3, 2026-09-27): reviewer APPROVED (liens finding-2 to finding-4); assurance APPROVED (INSP-049); record verdict NEEDS CHANGES (held: CR-012 template not merged)
PRODUCT: TV-013 71a676ef at main 3aed3c4; tool abe25acb; test module 7ccc293e; fixture tree ed4414ec; lock e1c811b0; README 7c90f143
FINDINGS: finding-1 Major Verified; finding-2 to finding-4 Minor, lien due CDR; no new finding; no Major open
DRIFT: lock and README hunks of 2bfe001 to 1db319a read; none touches TV-013 or tools/measurements.py
MEASUREMENTS: identities=22 blobs + 1 tree; hunks=13; new findings=0; iteration 3 turns=12, minutes=15; cumulative turns=40, minutes=57
```
