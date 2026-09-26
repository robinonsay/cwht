# TV-003: tools/validate_docs.py (git blob 33ab5a83, working tree on 400e59d; earlier blob 2bedc2a7 committed in 28e49e6 and 400e59d)

| Field | Value |
|---|---|
| Record | TV-003 |
| Status | **Validated** (2026-09-25; re-validated 2026-09-26 with the usage-error known answer, INSP-015 finding-5; re-run at commit `400e59d` on 2026-09-26, SRR package item R5, on blob `2bedc2a7`; re-validated 2026-09-26 on blob `33ab5a83` with the record drift rule, SRR package item R13). Blob `33ab5a83` is in the working tree, not yet committed. Independent review and owner accreditation pending (sections 8 and 9) |
| Class | B, evidence-generating (CM plan section 9.1) |
| Governs | SWE-136 (NPR 7150.2D section 4.4.8), SWE-070 (section 4.5.6) through CM plan section 9 |
| Due | SRR (CM plan section 13) |
| Lock rows | `tools/toolchain.lock.md` section 1.1 row `tools/traceability.py, tools/validate_docs.py`; section 1.2 |
| Author | Claude, tool validation author (SRR package section 2 item H12) |

## 1. Identification

The tool has no version string; its version is the file content.

| File | Git blob | SHA-256 | State against commit `28e49e6` |
|---|---|---|---|
| `tools/validate_docs.py` | `2bedc2a7aaa14359e3adde6b50810314c9793033` | `96c9e264b99899bf5434b354c99a35514db69133dc0eda8e2294ec09e4479dc8` | equal (the file as committed in `28e49e6`; unchanged in `400e59d`, run 4) |
| `tools/validate_docs.py`, run 5 | `33ab5a83fc2063071e1afece416b180518d9da12` | `1a0ab22c0b37d4e48d0c694b49d723524989181d0a200685654603454f800a7c` | modified in the working tree on `400e59d` (record drift rule, purpose 6) |
| `tools/tests/test_validate_docs.py`, run 5 | `4fb5bcc756b910876340e2f254359d3d9fcf80ef` | `fbae6f77...9ed8f0a` | modified in the working tree on `400e59d` (`RecordDriftTests`) |
| `tools/tests/test_validate_docs.py` | `8944a389618686b58c557f60872238321c5a3106` (run 3; runs 1 and 2: `3b10718d`, equal to `28e49e6`) | `23f226aa...b881d281` | modified in the working tree on 2026-09-26: `UsageErrorTests` added |
| `tools/tests/test_tools.py` | `af6ed8b7d3b34338d52fef0eba76bc84d27cadb1` | `a082201d...250998b` | modified in the working tree (1 line) |
| `tools/tests/fixtures/valid_project/` | 38 files, tree digest `6a58c19d2cf0e4d8f1bde9054ef154ff406dbeb9a1dd0752de4e49b5bd2b4f30` | | 3 files modified, 2 untracked |
| `tools/tests/fixtures/invalid_project/` | 32 files, tree digest `2377caa9611bdff2407f73ca9705cd1890407885d3f0f914462d7172f1e683eb` | | equal |

Commands as in TV-002 section 1. **Install source:** the repository (CM plan Table 4-1 row 28). **Runtime:** TV-001 (Python 3.13.5, jsonschema 4.26.0) and PyYAML 6.0.3 (`yaml.safe_load` in `parse_front_matter`, with the built-in subset parser as the fallback).

## 2. Purposes covered

1. Discover every JSON document at a conventional path of `tools/README.md` (the table of `validate_docs.py`) and validate it against its schema with jsonschema (draft from `$schema`); fail a document whose schema file is absent; print one `PASS` or `FAIL` line per document with the dotted error path.
2. Validate the YAML front matter of peer-review records `docs/reviews/<REVIEW>/checklists/<product-slug>.md` against the built-in `PEER_REVIEW_RECORD_SCHEMA` (01 section 13) and apply the record rules: unique `INSP-NNN`, `checklist_file` equal to the path, reviewer different from author, assurance reviewer where 07 section 2.1.1 or 14.1 requires one, `APPROVED` only with `readiness_met: true` and no open Major finding, no `peer-reviews/` folder.
3. Validate RFA/RID logs (`docs/templates/rfa-rid-log.schema.json`) with the cross-file rules: folder is a review token, `review` equals the folder, item ids carry the review, history transitions and `closed` dates of 01 section 10.3, verification records resolve.
4. Validate decision memos against the built-in `DECISION_MEMO_SCHEMA` and their rules (01 sections 12.1 and 12.2).
5. Exit 0 when every discovered document validates, 1 on any failure, 2 on a usage error.
6. From blob `33ab5a83`: record drift (SRR package section 2.3 and item R13). When `--root` is the top of a git work tree with a HEAD commit, compare every blob a peer-review record names in `product_files` (`path@blob`, validated against the pattern `^[^@\s]+@[0-9a-f]{7,40}$`) or `product_blob` (the blob of a single-file `product`) with the HEAD tree (`git ls-tree -r --full-tree HEAD`, the value `git rev-parse HEAD:<path>` gives). For a record whose verdict is `APPROVED`, a differing blob, a path absent from HEAD, or a record that names no blob is a failure; for any other verdict the drift is printed as a `note:` line under the record and does not fail. Outside a git work tree top (the fixtures and their temporary copies) the rule is reported as not applied.

## 3. Known-answer test

**Fixtures:** `tools/tests/fixtures/valid_project/` (every conventional document valid: exit 0, no failure) and `tools/tests/fixtures/invalid_project/` (seeded schema and convention faults: exit 1 with exactly the seeded failures). `test_validate_docs.py` `PeerReviewRecordTests` seed record faults on temporary copies; `UsageErrorTests` seed two usage errors (an unknown option `--bogus`, and a `--root` that is not a directory) and require exit 2, the argparse message on stderr and no `PASS` or `FAIL` line (purpose 5; added 2026-09-26, INSP-015 finding-5); `RecordDriftTests` (added 2026-09-26, purpose 6) build a temporary git repository with one committed product and one record per case, compute the expected blob with `git hash-object` (TV-009) independently of the tool, and require: an `APPROVED` record naming the HEAD blob (in `product_files`, and in `product_blob` by an 8-digit prefix) passes with no note; after the product is edited and committed, the same record fails with "differs from HEAD blob <new blob>", and a path absent from HEAD fails with "is not in HEAD"; an `APPROVED` record with no named blob fails; a `NEEDS CHANGES` record with a stale blob passes with exactly one drift note, printed as `      note: record drift: ...`; a malformed `product_files` entry fails the schema; the `valid_project` fixture (inside the repository but not a work tree top) reports "record drift rule not applied". `test_tools.py` holds the targeted known answers of the later rules (`PeerReviewRecordRuleTests`, `LogItemAndHistoryTests`, `DecisionMemoAndFolderTests`, `NewConventionTests`, `SchemaFindingTests` and the rest listed in `tools/README.md` "Tests and fixtures").

**Run commands** (repository root):

```
.venv/bin/python -m unittest discover -v -s tools/tests -p test_validate_docs.py -k ValidProjectTests -k InvalidProjectTests -k PeerReviewRecordTests -k UsageErrorTests -k RecordDriftTests
.venv/bin/python -m unittest discover -v -s tools/tests -p test_tools.py
```

**Pass criteria:** every test passes and none is skipped. `test_validate_docs.RepositoryTests` checks the repository itself and is recorded in the lock's repository-content row, not here.

## 4. Result

| Run | Date and time (CDT) | Commit tested | Tests | Result |
|---|---|---|---|---|
| 1 | 2026-09-25 23:36 | tool and `test_validate_docs.py` equal to `28e49e6`; `test_tools.py` and `valid_project` as in section 1 | 132 (18 + 114), 0 skipped | pass |
| 2 | 2026-09-25 23:45 | same identities | 132, 0 skipped | pass |
| 3 | 2026-09-26 00:15 | tool equal to `28e49e6`; `test_validate_docs.py` blob `8944a389` (modified: `UsageErrorTests`); `test_tools.py` and both fixtures equal to runs 1 and 2 | 134 (20 + 114; `UsageErrorTests` 2), 0 skipped | pass |
| 4 | 2026-09-26 02:31 | `HEAD` `400e59d` (SRR package item R5): an export of the commit (`git archive HEAD`); tool, test modules and fixtures equal to `400e59d` (tool blob `2bedc2a7`, `test_validate_docs.py` `8944a389`) | 137 (20 + 117), 0 skipped | pass |
| 5 | 2026-09-26 02:32 | working tree on `400e59d`: tool `33ab5a83`, `test_validate_docs.py` `4fb5bcc7`; `test_tools.py` and both fixtures equal to `400e59d` | 142 (25 + 117; `RecordDriftTests` 5), 0 skipped | pass |

Output excerpt (run 2):

```
## TV-003 validate_docs.py
  Ran 18 tests; failures+errors 0; skipped 0; per class {'InvalidProjectTests': 6, 'PeerReviewRecordTests': 8, 'ValidProjectTests': 4}; PASS
  Ran 114 tests; failures+errors 0; skipped 0; ...; PASS
  RESULT TV-003 validate_docs.py: PASS (132 tests)
```

The repository-content check `test_validate_docs.RepositoryTests` failed in both runs on `schema not found: docs/plan/measurements.schema.json`: another author had written `docs/plan/measurements.json` before its schema. That is the tool's specified behavior (purpose 1: a document without its schema fails), not a tool defect. Evidence: `docs/cm/tool-validation/evidence/python-tools-2026-09-25.log.txt`. Run 3 (2026-09-26 00:15) failed the same check on the two absent schemas `docs/design/allocation.schema.json` and `docs/plan/measurements.schema.json` (INSP-015 cross item 1); evidence `evidence/python-tools-2026-09-26.log.txt`.

Run 5 evidence: `evidence/python-tools-2026-09-26-r5-worktree.log.txt`. In the same run the repository-content check `test_validate_docs.RepositoryTests` failed, as specified by purpose 6, on the two `APPROVED` records that name no reviewed blob: `docs/reviews/SRR/checklists/semp.md` (INSP-005) and `trade-studies-ts-001-ts-002.md` (INSP-013), the records whose delta verification is package item R13; a repository check, not a tool defect.

R5 re-run (2026-09-26, SRR package section 2.1 item R5; INSP-015 finding-2): section 3 run at commit `400e59d` on an export of the commit, so the result is bound to a commit that contains every file tested: every tool, test module and fixture identity line of the transcript reads "equal to HEAD". Evidence `evidence/python-tools-2026-09-26-r5-head.log.txt` (procedure `evidence/python-tools-2026-09-26-r5.py`, mode `head`).

## 5. Reproducibility

Not required for class B. Runs 1 and 2 gave identical results; run 3 adds the two usage-error tests and gives the same result on every earlier test.

## 6. Limitations

1. Conventions only: a JSON document at a path outside the conventions of purpose 1 is not validated at all.
2. The known answer of purpose 1 relies on jsonschema's reporting (TV-001); the draft and keywords outside TV-001 purpose 2 are outside this accreditation too.
3. The front-matter parser falls back to a subset parser when PyYAML is absent; the known answers ran with PyYAML 6.0.3 present, so the fallback path is covered only by the tests that call it directly (`FrontMatterTests`).
4. Runs 1 to 3 and 5 used working-tree files; run 4 is bound to commit `400e59d`. The result of run 5 carries to a commit only if the section 1 run 5 files are committed unchanged.
5. The record drift rule (purpose 6) compares with HEAD, not with the working tree: a product edited and not yet committed is not drift, and a record is checked against the last commit. It reads only `product_files` and `product_blob`; a record that names its blobs only in its body or in comments is, for an `APPROVED` record, a failure and, otherwise, not checked. It needs git on `PATH` (TV-009) and `--root` at the work tree top.
6. Output is developer evidence until section 9 records the accreditation.

## 7. Re-validation triggers

- Any change of `tools/validate_docs.py`, of `test_validate_docs.py` or `test_tools.py`, or of either fixture (CM plan section 9.2 step 4).
- A change of the interpreter, jsonschema or PyYAML (TV-001).
- A change of git (TV-009), which purpose 6 runs.
- A new convention or rule: its known answer is added before the change is used for the record.
- A defect found in the tool (an NCR per SWE-201).

## 8. Independent review (CM plan section 9.2 step 3)

Pending. Reviewer invocation, date and result are recorded here.

## 9. Accreditation (owner)

Proposed scope statement **ACC-VALDOCS-001**: "Accredited for purposes 1 to 6 for `tools/validate_docs.py` at git blob `33ab5a83fc2063071e1afece416b180518d9da12` once committed (purposes 1 to 5 at blob `2bedc2a7aaa14359e3adde6b50810314c9793033`, commits `28e49e6` and `400e59d`, for the runs made before 2026-09-26), under the TV-001 interpreter with PyYAML 6.0.3."

| Decision | Date | Recorded by |
|---|---|---|
| Pending (owner, at SRR, after section 8) | | |
