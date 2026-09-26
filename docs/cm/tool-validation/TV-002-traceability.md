# TV-002: tools/traceability.py (git blob 0a867523)

| Field | Value |
|---|---|
| Record | TV-002 |
| Status | **Validated** (2026-09-25; re-run at commit `400e59d` on 2026-09-26, SRR package item R5) on the file identified in section 1, committed unchanged in `400e59d`. Independent review and owner accreditation pending (sections 8 and 9) |
| Class | B, evidence-generating (CM plan section 9.1) |
| Governs | SWE-136 (NPR 7150.2D section 4.4.8), SWE-070 (section 4.5.6) through CM plan section 9; the tool checks SWE-052 (NPR 7150.2D section 3.12.1 Table 1) as charter section 7 adopts it |
| Due | SRR (CM plan section 13) |
| Lock rows | `tools/toolchain.lock.md` section 1.1 row `tools/traceability.py, tools/validate_docs.py`; section 1.2 |
| Author | Claude, tool validation author (SRR package section 2 item H12) |

## 1. Identification

The tool has no version string; its version is the content of the file, identified by its git blob and SHA-256.

| File | Git blob (`git hash-object`) | SHA-256 | State against commit `28e49e6` |
|---|---|---|---|
| `tools/traceability.py` | `0a867523f78c224afdaa938735911b5df8f2920c` | `150571ceaaee1a935fef4385eb502c8f8fd200c75095d37a92f32331684ec49a` | modified in the working tree (235 lines added and 4 removed against `28e49e6`, `git diff --numstat 28e49e6 -- tools/traceability.py`; corrected 2026-09-26 after INSP-015 finding-6 by another author on 2026-09-25: the T-21 and T-18 rules) |
| `tools/validate_docs.py` (imported: schema loading, front-matter parser) | `2bedc2a7aaa14359e3adde6b50810314c9793033` | `96c9e264b99899bf5434b354c99a35514db69133dc0eda8e2294ec09e4479dc8` | equal |
| `tools/tests/test_traceability.py` | `d76b06976ba62d374d8c30a8eb08a4cb57d394e7` | `493d81f8...9edf780` | modified |
| `tools/tests/test_traceability_srr_rules.py` | `86606485debd4569954847c5a48e7dd62bbcbcab` | `7c8f10a4...d09776` | untracked |
| `tools/tests/test_tools.py` | `af6ed8b7d3b34338d52fef0eba76bc84d27cadb1` | `a082201d...250998b` | modified |
| `tools/tests/fixtures/valid_project/` | 38 files, tree digest `6a58c19d2cf0e4d8f1bde9054ef154ff406dbeb9a1dd0752de4e49b5bd2b4f30` | | 3 files modified, 2 untracked (`docs/design/`) |
| `tools/tests/fixtures/invalid_project/` | 32 files, tree digest `2377caa9611bdff2407f73ca9705cd1890407885d3f0f914462d7172f1e683eb` | | equal |

Commands: `git hash-object <file>`; `shasum -a 256 <file>`; `git diff --quiet HEAD -- <file>`; the tree digest is the SHA-256 of the sorted list of `<sha256>  <path>` lines (procedure `docs/cm/tool-validation/evidence/python-tools-2026-09-25.py`, function `tree`). **Install source:** the repository (CM plan Table 4-1 row 28); no installer. **Runtime:** the venv Python and jsonschema of TV-001, PyYAML 6.0.3 through `validate_docs.py`.

## 2. Purposes covered

1. Check the requirement, expectation, test-case, hazard, risk-link, verification-report and NCR files of a repository root against the rule catalogue of the tool (`CHECK_CATALOGUE` in the source; `tools/README.md` "Rule coverage"): unique ids, parent or documented self-derived rationale, every Draft or Active requirement verified by at least one case, every case citing at least one requirement, status and evidence rules, hazard-control union (charter section 7), writing-rule word list, report and NCR front matter and artifact hashes; exit 1 on any Violation.
2. The SRR rules `STAKEHOLDERS_MISSING` (02 T-21) and `SYS_UNALLOCATED` (02 T-18, warning listing at SRR) from `docs/design/allocation.json`.
3. Write the traceability report (`docs/vv/traceability-report.md` or `--output`) and its data file (`traceability.json` or `--json`), with `--report-only` exiting 0 whatever the findings.
4. With `--render`, write `expectations.md` and every `requirements.md` from their JSON before the checks.

## 3. Known-answer test

**Fixtures:** `tools/tests/fixtures/valid_project/` (a complete miniature project: the tool must find no finding) and `tools/tests/fixtures/invalid_project/` (the same with seeded faults: orphan requirement, test case without a requirement, duplicate id, TBR on a Verified requirement, software hazard control without a Test case, unresolved `RSK-NNN`, bad report and NCR artifact hashes, writing-rule violations; lock section 1.1). `test_tools.py` adds one targeted known answer for every catalogue code that no fixture seeds, with a guard test that fails when a code has no test (`CatalogueKnownAnswerTests`, `CatalogueTests`); `test_traceability_srr_rules.py` holds the T-21 and T-18 known answers.

**Run commands** (repository root):

```
.venv/bin/python -m unittest discover -v -s tools/tests -p test_traceability.py -k ValidProjectTests -k InvalidProjectTests -k WordListTests
.venv/bin/python -m unittest discover -v -s tools/tests -p test_traceability_srr_rules.py -k CatalogueTests -k StakeholdersKnownAnswerTests -k AllocationKnownAnswerTests
.venv/bin/python -m unittest discover -v -s tools/tests -p test_tools.py
```

**Pass criteria:** every test passes and none is skipped; `valid_project` exits 0 with zero findings; `invalid_project` exits 1 with exactly the seeded code set. The repository-content classes (`test_traceability.RepositoryTests`, `test_traceability_srr_rules` `FixtureSchemaTripwireTests` and `RepositoryAllocationTests`) are not part of this test; they are run and recorded separately (lock section 1.1 repository-content row).

## 4. Result

| Run | Date and time (CDT) | Commit tested | Tests | Result |
|---|---|---|---|---|
| 1 | 2026-09-25 23:36 | `HEAD` `28e49e6` with the working-tree files of section 1 | 173 (27 + 32 + 114), 0 skipped | pass |
| 2 | 2026-09-25 23:45 | same file identities as run 1 | 173, 0 skipped | pass |
| 3 | 2026-09-26 02:31 | `HEAD` `400e59d` (SRR package item R5): an export of the commit (`git archive HEAD`); tool, test modules and fixtures equal to `400e59d` | 176 (27 + 32 + 117), 0 skipped | pass |
| 4 | 2026-09-26 02:32 | working tree on `400e59d`: this tool, its test modules and both fixtures equal to `400e59d`; `tools/validate_docs.py` blob `33ab5a83` (the record drift rule, TV-003 run 5) | 176, 0 skipped | pass |

Output excerpt (run 2):

```
## TV-002 traceability.py
  Ran 27 tests; failures+errors 0; skipped 0; per class {'InvalidProjectTests': 15, 'ValidProjectTests': 10, 'WordListTests': 2}; PASS
  Ran 32 tests; failures+errors 0; skipped 0; per class {'AllocationKnownAnswerTests': 14, 'CatalogueTests': 3, 'StakeholdersKnownAnswerTests': 15}; PASS
  Ran 114 tests; failures+errors 0; skipped 0; per class {... 32 classes ...}; PASS
  RESULT TV-002 traceability.py: PASS (173 tests)
```

Evidence: `docs/cm/tool-validation/evidence/python-tools-2026-09-25.log.txt` (both runs, every file identity, per-class counts).

R5 re-run (2026-09-26, SRR package section 2.1 item R5; INSP-015 finding-2): section 3 run at commit `400e59d` on an export of the commit, so the result is bound to a commit that contains every file tested: every tool, test module and fixture identity line of the transcript reads "equal to HEAD". Evidence `evidence/python-tools-2026-09-26-r5-head.log.txt` (procedure `evidence/python-tools-2026-09-26-r5.py`, mode `head`); run 4: `evidence/python-tools-2026-09-26-r5-worktree.log.txt`.

## 5. Reproducibility

Not required for class B (CM plan section 9.2 step 1). Runs 1 and 2 gave identical results on identical file identities.

## 6. Limitations

1. **Uncommitted tool.** The validated file is a working-tree blob. The accreditation, when given, covers blob `0a867523` only; if the file is committed unchanged the blob, and so this record, carries over; any edit is a new version (section 7). Until then no evidence row may cite a commit for the tool (review process section 3.1 item 1).
2. **Rules not implemented.** SWE-052 Table 1 rows 3 (requirements to design components) and 4 (design components to code) and the other codes of `tools/README.md` "Not implemented, with gates" are not checked; the tool's pass says nothing about them, and the manual checks named there remain required.
3. **Known answers are per rule.** Each code is shown to fire on its seeded fault and not on the valid fixture; combinations of faults beyond those seeded are not tested.
4. `test_tools.py` contains two `SchemaTripwireTests` that compare fixture schema copies with the repository schemas (repository content). They pass today; a repository schema edit without a fixture re-copy fails them without any tool defect. They should move to the repository-content row (cross-document item of this record's author).
5. Output is developer evidence until section 9 records the accreditation (CM plan section 9.1).

## 7. Re-validation triggers

- Any change of `tools/traceability.py` or `tools/validate_docs.py` (a new blob is a new version), of the three test modules or of either fixture (CM plan section 9.2 step 4).
- A change of the interpreter, jsonschema or PyYAML (TV-001 triggers).
- A new rule code: the catalogue guard test fails until its known answer exists.
- A defect found in the tool (an NCR per SWE-201).

## 8. Independent review (CM plan section 9.2 step 3)

Pending. The reviewer checks this record, re-runs section 3, and checks that each seeded fault of `invalid_project` and each targeted test of `test_tools.py` asserts an exact code set. Reviewer invocation, date and result are recorded here.

## 9. Accreditation (owner)

Proposed scope statement **ACC-TRACE-001**: "Accredited for purposes 1 to 4 for `tools/traceability.py` at git blob `0a867523f78c224afdaa938735911b5df8f2920c` with `tools/validate_docs.py` at blob `2bedc2a7aaa14359e3adde6b50810314c9793033`, under the TV-001 interpreter, for the rule codes implemented at that blob."

| Decision | Date | Recorded by |
|---|---|---|
| Pending (owner, at SRR, after section 8) | | |
