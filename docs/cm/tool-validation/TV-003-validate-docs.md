# TV-003: tools/validate_docs.py (git blob 3aa03681, commit 96af250; earlier blobs 33ab5a83, validated in the working tree on 400e59d and committed in 3de1e2d, and 2bedc2a7, committed in 28e49e6 and 400e59d)

| Field | Value |
|---|---|
| Record | TV-003 |
| Status | **Validated** (2026-09-25; re-validated 2026-09-26 with the usage-error known answer, INSP-015 finding-5; re-run at commit `400e59d` on 2026-09-26, SRR package item R5, on blob `2bedc2a7`; re-validated 2026-09-26 on blob `33ab5a83` with the record drift rule, SRR package item R13). Blob `33ab5a83` is in the working tree, not yet committed. Independent review and owner accreditation pending (sections 8 and 9). Update 2026-09-26 06:11: blob `33ab5a83` was committed in `3de1e2d`; re-validated on blob `3aa03681`, commit `96af250`, with the record state rule (purpose 7; SRR package item R18, readiness finding R15-F2), run 6 of section 4 |
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
| `tools/validate_docs.py`, run 6 | `3aa0368147b9af3e6e1546f808afb7aedf7f2226` | `e06c72a1b71229f4fa1b14d2be009721b1fbc84219a1aa48cc05621536b06092` | committed in `96af250` (record state rule, purpose 7) |
| `tools/tests/test_validate_docs.py`, run 6 | `c70d2c932a3b0965a2adb7827d8cfb5c4e005025` | `467121e4d9e770a2707af97cf2c64494349cd320328ede2dfa1ea803f7b63a62` | committed in `96af250` (`RecordStateTests`) |
| `tools/tests/test_tools.py`, run 6 | `ed003bad762332310f0bc4d63346ac875f0e0554` | `8408518e994909db7d08b39d800f0f7cd22afc8567e9d1ef06aee470dec5d823` | unchanged since `1d423e5` |
| `tools/tests/fixtures/record_state/`, run 6 | 9 files, git tree `b7c20457f2ae8c4d0fec41b52abd127003aa34ff` | | added in `96af250` |
| `tools/tests/fixtures/valid_project/`, `invalid_project/`, run 6 | git trees `827f6ca930befb9a6cb75f4f620697b47bdfd245`, `6a046bae3fe2a86c2e4b00a41954f1946b5e3b1f` at `96af250` | | unchanged by run 6 |

Commands as in TV-002 section 1. **Install source:** the repository (CM plan Table 4-1 row 28). **Runtime:** TV-001 (Python 3.13.5, jsonschema 4.26.0) and PyYAML 6.0.3 (`yaml.safe_load` in `parse_front_matter`, with the built-in subset parser as the fallback).

## 2. Purposes covered

1. Discover every JSON document at a conventional path of `tools/README.md` (the table of `validate_docs.py`) and validate it against its schema with jsonschema (draft from `$schema`); fail a document whose schema file is absent; print one `PASS` or `FAIL` line per document with the dotted error path.
2. Validate the YAML front matter of peer-review records `docs/reviews/<REVIEW>/checklists/<product-slug>.md` against the built-in `PEER_REVIEW_RECORD_SCHEMA` (01 section 13) and apply the record rules: unique `INSP-NNN`, `checklist_file` equal to the path, reviewer different from author, assurance reviewer where 07 section 2.1.1 or 14.1 requires one, `APPROVED` only with `readiness_met: true` and no open Major finding, no `peer-reviews/` folder.
3. Validate RFA/RID logs (`docs/templates/rfa-rid-log.schema.json`) with the cross-file rules: folder is a review token, `review` equals the folder, item ids carry the review, history transitions and `closed` dates of 01 section 10.3, verification records resolve.
4. Validate decision memos against the built-in `DECISION_MEMO_SCHEMA` and their rules (01 sections 12.1 and 12.2).
5. Exit 0 when every discovered document validates, 1 on any failure, 2 on a usage error.
6. From blob `33ab5a83`: record drift (SRR package section 2.3 and item R13). When `--root` is the top of a git work tree with a HEAD commit, compare every blob a peer-review record names in `product_files` (`path@blob`, validated against the pattern `^[^@\s]+@[0-9a-f]{7,40}$`) or `product_blob` (the blob of a single-file `product`) with the HEAD tree (`git ls-tree -r --full-tree HEAD`, the value `git rev-parse HEAD:<path>` gives). For a record whose verdict is `APPROVED`, a differing blob, a path absent from HEAD, or a record that names no blob is a failure; for any other verdict the drift is printed as a `note:` line under the record and does not fail. Outside a git work tree top (the fixtures and their temporary copies) the rule is reported as not applied.
7. From blob `3aa03681` (commit `96af250`; SRR package item R18, readiness finding R15-F2): the record state rule of the tool header replaces the line heuristic of purpose 2 ("no open Major finding", which read any body line holding a `finding-<n>` anchor with the words Major and Open, so historical count lines such as "open Major 0" held an `APPROVED` record). An `APPROVED` record fails when `readiness_met` is not true; when `reviewer_verdict`, if present, is not `APPROVED`; when a finding table of the latest iteration section has a current row (the last row of that finding in document order) whose id cell is `finding-<n>` or `F-<nn>`, whose severity cell begins with Major and whose state cell begins with Open; or when `findings_open`, if present, is above zero and the latest iteration section does not show that many open Minor findings. The latest iteration section starts at the first heading naming the highest "iteration N" and runs to the end of the body, less any block under a heading naming a lower iteration; fenced blocks, prose, count summaries and earlier-iteration tables are not read.

## 3. Known-answer test

**Fixtures:** `tools/tests/fixtures/valid_project/` (every conventional document valid: exit 0, no failure) and `tools/tests/fixtures/invalid_project/` (seeded schema and convention faults: exit 1 with exactly the seeded failures). `test_validate_docs.py` `PeerReviewRecordTests` seed record faults on temporary copies; `UsageErrorTests` seed two usage errors (an unknown option `--bogus`, and a `--root` that is not a directory) and require exit 2, the argparse message on stderr and no `PASS` or `FAIL` line (purpose 5; added 2026-09-26, INSP-015 finding-5); `RecordDriftTests` (added 2026-09-26, purpose 6) build a temporary git repository with one committed product and one record per case, compute the expected blob with `git hash-object` (TV-009) independently of the tool, and require: an `APPROVED` record naming the HEAD blob (in `product_files`, and in `product_blob` by an 8-digit prefix) passes with no note; after the product is edited and committed, the same record fails with "differs from HEAD blob <new blob>", and a path absent from HEAD fails with "is not in HEAD"; an `APPROVED` record with no named blob fails; a `NEEDS CHANGES` record with a stale blob passes with exactly one drift note, printed as `      note: record drift: ...`; a malformed `product_files` entry fails the schema; the `valid_project` fixture (inside the repository but not a work tree top) reports "record drift rule not applied". `RecordStateTests` (added 2026-09-26, purpose 7) run the validator on `tools/tests/fixtures/record_state/` (seven records, table in its `README.md`) and require: exactly three records fail; `approved-historical-lines.md` (INSP-101, `APPROVED`, whose iteration 1 table, count lines, fenced verdict block and a later "as written at iteration 1" block name finding-1 with Major and Open, and whose iteration 2 table closes it) passes, and at least five of its lines match the replaced heuristic; `approved-latest-open-major.md` (INSP-102, `APPROVED`, finding-3 Major Open in the iteration 2 table) fails with "finding-3 is a Major finding in state Open"; `approved-open-count-unshown.md` fails on `findings_open` 1 with no open Minor row; `approved-reviewer-needs-changes.md` fails on `reviewer_verdict`; an open Minor finding passes; a later iteration 3 row closing F-01 supersedes an earlier iteration 3 row that holds it Open; a `NEEDS CHANGES` record with an open Major finding passes; section bounds, fenced blocks, HTML anchors in the id cell, "Closed (was Open)" and "Minor (was Major)" cells and a non-finding table are read as specified. `test_tools.py` holds the targeted known answers of the later rules (`PeerReviewRecordRuleTests`, `LogItemAndHistoryTests`, `DecisionMemoAndFolderTests`, `NewConventionTests`, `SchemaFindingTests` and the rest listed in `tools/README.md` "Tests and fixtures").

**Run commands** (repository root):

```
.venv/bin/python -m unittest discover -v -s tools/tests -p test_validate_docs.py -k ValidProjectTests -k InvalidProjectTests -k PeerReviewRecordTests -k UsageErrorTests -k RecordDriftTests -k RecordStateTests
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
| 6 | 2026-09-26 06:11 | `HEAD` `96af250` (SRR package item R18): tool `3aa03681`, `test_validate_docs.py` `c70d2c93`, `test_tools.py` `ed003bad`, fixture `record_state/` tree `b7c20457`, all equal to the commit (working tree clean for these paths) | 150 (33 + 117; `RecordStateTests` 8), 0 skipped | pass |

Output excerpt (run 2):

```
## TV-003 validate_docs.py
  Ran 18 tests; failures+errors 0; skipped 0; per class {'InvalidProjectTests': 6, 'PeerReviewRecordTests': 8, 'ValidProjectTests': 4}; PASS
  Ran 114 tests; failures+errors 0; skipped 0; ...; PASS
  RESULT TV-003 validate_docs.py: PASS (132 tests)
```

The repository-content check `test_validate_docs.RepositoryTests` failed in both runs on `schema not found: docs/plan/measurements.schema.json`: another author had written `docs/plan/measurements.json` before its schema. That is the tool's specified behavior (purpose 1: a document without its schema fails), not a tool defect. Evidence: `docs/cm/tool-validation/evidence/python-tools-2026-09-25.log.txt`. Run 3 (2026-09-26 00:15) failed the same check on the two absent schemas `docs/design/allocation.schema.json` and `docs/plan/measurements.schema.json` (INSP-015 cross item 1); evidence `evidence/python-tools-2026-09-26.log.txt`.

Run 5 evidence: `evidence/python-tools-2026-09-26-r5-worktree.log.txt`. In the same run the repository-content check `test_validate_docs.RepositoryTests` failed, as specified by purpose 6, on the two `APPROVED` records that name no reviewed blob: `docs/reviews/SRR/checklists/semp.md` (INSP-005) and `trade-studies-ts-001-ts-002.md` (INSP-013), the records whose delta verification is package item R13; a repository check, not a tool defect.

Run 6 (2026-09-26 06:11, SRR package item R18): the known-answer set passes at `96af250`. The full directory (`-m unittest discover -s tools/tests`) ran 400 tests with 1 failure, the repository-content check `test_validate_docs.RepositoryTests`: `validate_docs.py` exits 1 on the record drift of INSP-008 (`checklists/hazard-analysis.md` names the 0.4.2-pha hazard blobs; package item R17), not on a tool defect. On the 30 SRR records the rule of purpose 7 passes every `APPROVED` record, would pass INSP-002 (`conops-and-concept.md`) as `APPROVED`, and still finds the open Major findings of INSP-003 (finding-6), INSP-011 (F-01, F-04) and INSP-016 (F-01, F-02). Evidence: this record and the commit message of `96af250`; no log file was written.

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
7. The record state rule (purpose 7) reads finding tables only: a record that states a finding's state only in prose or under `### finding-<n>` headings is judged by its front matter (`readiness_met`, `reviewer_verdict`, `findings_open`), so an `APPROVED` record with `findings_open: 0` and no finding table passes on the front matter alone. The state word is read as the first alphabetic word of a state cell, capitalized as Open; a reviewer who writes an open state as "open" or "Pending" is not read as Open. The latest iteration is found from headings that name "iteration N"; a record whose latest review block is headed without that phrase is read from the first heading that names its highest iteration.

## 7. Re-validation triggers

- Any change of `tools/validate_docs.py`, of `test_validate_docs.py` or `test_tools.py`, or of either fixture (CM plan section 9.2 step 4).
- A change of the interpreter, jsonschema or PyYAML (TV-001).
- A change of git (TV-009), which purpose 6 runs.
- A new convention or rule: its known answer is added before the change is used for the record.
- A defect found in the tool (an NCR per SWE-201).

## 8. Independent review (CM plan section 9.2 step 3)

Pending. Reviewer invocation, date and result are recorded here.

## 9. Accreditation (owner)

Proposed scope statement **ACC-VALDOCS-001**: "Accredited for purposes 1 to 6 for `tools/validate_docs.py` at git blob `33ab5a83fc2063071e1afece416b180518d9da12` once committed (purposes 1 to 5 at blob `2bedc2a7aaa14359e3adde6b50810314c9793033`, commits `28e49e6` and `400e59d`, for the runs made before 2026-09-26), under the TV-001 interpreter with PyYAML 6.0.3." Proposed extension (2026-09-26, run 6): purposes 1 to 7 at git blob `3aa0368147b9af3e6e1546f808afb7aedf7f2226`, commit `96af250`, for runs made from 2026-09-26 06:11; purpose 2's open-Major clause is then read as purpose 7.

| Decision | Date | Recorded by |
|---|---|---|
| Pending (owner, at SRR, after section 8) | | |
