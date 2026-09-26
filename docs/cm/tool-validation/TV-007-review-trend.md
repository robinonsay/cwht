# TV-007: tools/review_trend.py (git blob 04493157, commit 28e49e6)

| Field | Value |
|---|---|
| Record | TV-007 |
| Status | **Validated** (2026-09-25). Independent review and owner accreditation pending (sections 8 and 9) |
| Class | B, evidence-generating (CM plan section 9.1) |
| Governs | SWE-136 (NPR 7150.2D section 4.4.8), SWE-070 (section 4.5.6) through CM plan section 9; the tool computes the review-trend TPM (TPM-003) of charter section 4 item 5 and NPR 7123.1D SE-64 as 01 section 11 defines it |
| Due | SRR (CM plan section 13) |
| Lock rows | `tools/toolchain.lock.md` section 1.1 row `tools/review_trend.py`; section 1.2 |
| Author | Claude, tool validation author (SRR package section 2 item H12) |

## 1. Identification

| File | Git blob | SHA-256 | State against commit `28e49e6` |
|---|---|---|---|
| `tools/review_trend.py` | `04493157ae1c3245ca600bf1c29069dfe3192810` | `24c10c039b3b5fe4679f7ee92cf837ccffc6851fd420362ce84c19b7b13f46d6` | equal |
| `tools/validate_docs.py` (imported) | `2bedc2a7aaa14359e3adde6b50810314c9793033` | see TV-003 | equal |
| `tools/tests/test_review_trend.py` | `1f3ab0067b9ce33ebedefaf2a460664d2a978bdb` | `97d6a781...1d3945` | equal |
| `tools/tests/fixtures/review_trend/` | 6 files, tree digest `c7d63b0f247b4f294700a7c3a3616f8a72b5a146dc4cb57125dedc979217a45e` | | equal |
| `docs/templates/rfa-rid-log.example.json` (the known-answer input, read from the repository) | `0e913114286a3099875f4c9fd67f2b0ce5ef67cd` | | equal |
| `docs/templates/rfa-rid-log.schema.json` (log schema) | `38898b0c260c3292fbc65c59d632790ad4e650f7` | | equal |
| `docs/reviews/SRR/rfa-rid-log.json` (read by `test_repository_runs_cleanly_without_logs`) | `0dc293ade799df101d760ada148d683e585d0f36` | | equal |

**Install source:** the repository (CM plan Table 4-1 row 28). **Runtime:** TV-001 (Python, jsonschema through `validate_docs.py`) and matplotlib 3.11.2 (venv, lock section 2) for `--write`.

## 2. Purposes covered

1. Read every `docs/reviews/*/rfa-rid-log.json` (schema-checked first) and the `signed` dates of the decision memos, evaluate every item's state at the package date `T` from its history, and compute per review and item type the raised, open, verified-pending, closed, withdrawn and overdue counts, the closure fraction at the next gate and the zone (01 section 11), printed as a table or with `--json`.
2. With `--package <REVIEW> --write`, write `docs/reviews/<REVIEW>/figures/review-trend.png` (burndown per logged review) and append one `TPM-003` history entry per logged review to `docs/plan/tpm.json` (fields of `conventions.history_entry_shape`), replacing the entries of a rerun for the same package and date.
3. Exit 0 when every zone is Green or Yellow (and when no log exists), 1 when any zone is Red, 2 on a usage error or invalid input.

## 3. Known-answer test

**Fixtures:** `tools/tests/fixtures/review_trend/` (6 files: a copy of `docs/templates/rfa-rid-log.example.json` as `docs/reviews/SRR/rfa-rid-log.json`, the SRR `decision-memo.md`, the peer-review record the log cites with its checklist stub, a copy of the log schema, and a `docs/plan/tpm.json` carrying `TPM-003`) and the repository template itself. The known answers are the counts hand-computed in 01 section 11 for the template at `T` = 2026-10-12.

**Run command** (repository root): `.venv/bin/python -m unittest discover -v -s tools/tests -p test_review_trend.py`

**Pass criteria:** all 20 tests pass, none skipped: the per-type and per-severity counts, derived values, burndown series and state-at-`T` evaluation equal 01 section 11 (`KnownAnswerTests`); text and JSON output, usage and invalid-log exits (`CliTests`); figure written and history appended, no log, missing `TPM-003` (`WriteTests`); the seven zone rules (`ZoneTests`).

## 4. Result

| Run | Date and time (CDT) | Commit tested | Tests | Result |
|---|---|---|---|---|
| 1 | 2026-09-25 23:36 | `28e49e6` (tool, test, fixture and the repository inputs of section 1 byte-identical to the commit) | 20 (`KnownAnswerTests` 5, `CliTests` 5, `WriteTests` 3, `ZoneTests` 7), 0 skipped | pass |
| 2 | 2026-09-25 23:45 | same | 20, 0 skipped | pass |

Earlier runs on the working tree at `b8214ca` (18:23 one repository-content failure, then 18:28 and 19:36 pass) are in lock section 1.1. Evidence: `docs/cm/tool-validation/evidence/python-tools-2026-09-25.log.txt`.

## 5. Reproducibility

Not required for class B. Runs 1 and 2 gave identical results.

## 6. Limitations

1. **Repository inputs in the tool's test.** `KnownAnswerTests` compute the known answers from the repository template `docs/templates/rfa-rid-log.example.json` (validated against the repository schema), `test_fixture_log_is_the_template` compares the fixture copy with that template, and `test_repository_runs_cleanly_without_logs` runs the tool on the repository root, whose `docs/reviews/SRR/rfa-rid-log.json` exists since 2026-09-25 (the test passes and checks the no-log message only when no log exists). A template, schema or SRR-log edit can therefore fail the tool's known-answer run without a tool defect. Lock section 1.1 planned to move the template test to the repository-content row before this record; that move is not done (test modules are outside this record's author's scope), so the three repository inputs are identified in section 1 and are re-validation triggers.
2. Known limitations of the tool itself (`tools/README.md`): the memo key `revoked` (01 section 12.2) is not read, so a revoked review stays dispositioned; a log or memo in a folder that is not a review token is read and ranked after SAR (`validate_docs.py` fails that case).
3. The figure of `--write` is checked for existence and the history entry for its fields, not for its drawing; the figure is inspected by the package author (charter section 11 rule 3).
4. Output is developer evidence until section 9 records the accreditation.

## 7. Re-validation triggers

- Any change of `tools/review_trend.py`, `tools/validate_docs.py`, the test module or the fixture (CM plan section 9.2 step 4).
- A change of the three repository inputs of section 1, or of 01 section 11.
- A change of the interpreter, jsonschema or matplotlib (TV-001; lock section 2).
- A defect found in the tool (an NCR per SWE-201).

## 8. Independent review (CM plan section 9.2 step 3)

Pending. Reviewer invocation, date and result are recorded here.

## 9. Accreditation (owner)

Proposed scope statement **ACC-TREND-001**: "Accredited for purposes 1 to 3 for `tools/review_trend.py` at git blob `04493157ae1c3245ca600bf1c29069dfe3192810` (commit `28e49e6`) with `tools/validate_docs.py` at blob `2bedc2a7`, under the TV-001 interpreter and matplotlib 3.11.2, subject to limitation 2."

| Decision | Date | Recorded by |
|---|---|---|
| Pending (owner, at SRR, after section 8) | | |
