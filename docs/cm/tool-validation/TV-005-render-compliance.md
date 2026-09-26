# TV-005: tools/render_compliance.py (git blob d67d6b5e, commit 28e49e6)

| Field | Value |
|---|---|
| Record | TV-005 |
| Status | **Validated** (2026-09-25). Independent review and owner accreditation pending (sections 8 and 9) |
| Class | B, evidence-generating (CM plan section 9.1) |
| Governs | SWE-136 (NPR 7150.2D section 4.4.8), SWE-070 (section 4.5.6) through CM plan section 9; the tool checks the NPR 7123.1D App. H compliance matrix (`docs/process/se-compliance-matrix.json`) |
| Due | SRR (CM plan section 13) |
| Lock rows | `tools/toolchain.lock.md` section 1.1 row `tools/render_compliance.py`; section 1.2 |
| Author | Claude, tool validation author (SRR package section 2 item H12) |

## 1. Identification

| File | Git blob | SHA-256 | State against commit `28e49e6` |
|---|---|---|---|
| `tools/render_compliance.py` | `d67d6b5e601a64b013b64e8de3cd0fc3deb96ffa` | `24d09c18ed2141bd21c3cf3a69d3b42dd713cf9329ec2691b3ab32db47ffc171` | equal |
| `tools/tests/test_render_compliance.py` | `c40a7f1f514d3784efcbef300d301391d9de84c0` | `98a7a85b...0355685` | equal |
| `tools/tests/fixtures/compliance/` | 15 files, tree digest `a95aad4632621207139c863b87bcb098dd63190cb1e7dd68386bceb63d3a2b43` | | equal |
| `docs/process/se-compliance-matrix.schema.json` (read by the fixture tests: the project schema is the schema under test) | `ef156b0fcfaaca3b44543154a454b0a965e72a2c` | | equal |
| `docs/references/md/npr-7123-1d/14-appendixh.md` (read by `test_real_corpus_has_62_rows`) | `8afa36e0d61a8d2f8072d8d0721ed94b5ea4b59b` | | equal |

The tool uses jsonschema (TV-001) for the schema check and the standard library otherwise. **Install source:** the repository (CM plan Table 4-1 row 28).

## 2. Purposes covered

1. Validate the compliance matrix JSON (`--json`) against its schema (`--schema`) with jsonschema.
2. Cross-check the matrix against NPR 7123.1D App. H Table H-1 in the corpus copy (`--corpus`; `--no-corpus` or an empty corpus path skips only the cross-check): row set, order, SE-NN statement and rationale text, section, disposition rules (a tailored row carries its justification and relief type, a fully compliant row carries none, the required disposition where the matrix convention fixes one).
3. Render the matrix Markdown (`--out`) with the six H-1 columns and the revision date, and with `--check` fail when the rendered file differs from a fresh render.
4. Exit 0 when valid and current, non-zero on any fault.

## 3. Known-answer test

**Fixtures:** `tools/tests/fixtures/compliance/`: `valid.json` with its stored render `valid.md`, an App. H extract `appendix-h.md`, `stale.md`, and one fixture per seeded fault. The seeded fault list, fixed here as lock section 1.1 requires, with the exact error each must give (`SeededFaultTests`):

| Fixture | Seeded fault | Expected error (exact) |
|---|---|---|
| `missing-row.json` | a Table H-1 row absent | `ids in corpus Table H-1 but not in matrix: ['SE-34']` |
| `unknown-id.json` | an id not in Table H-1 | `ids in matrix but not in corpus Table H-1: ['SE-98']` |
| `empty-t-justification.json` | tailored row with an empty justification | `schema: rows/8/justification (SE-51): '' is too short` |
| `altered-statement.json` | statement not verbatim | `SE-07: requirement_statement is not the verbatim Table H-1 statement` |
| `altered-rationale.json` | rationale not verbatim | `SE-44: rationale is not the verbatim Table H-1 rationale` |
| `wrong-section.json` | section differs | `SE-24: npr_section '4.2.2' differs from Table H-1 '4.2.1'` (also the CLI case: exit 1, `compliance matrix check FAILED`) |
| `t-without-relief.json` | tailored row without relief type | `schema: rows/8 (SE-51): 'relief_type' is a required property` |
| `relief-on-fc.json` | relief type on a fully compliant row | `schema: rows/0 (SE-07): False schema does not allow 'deviation'` |
| `required-disposition.json` | disposition other than the one charter section 12 fixes | `SE-44: comply 'FC' but charter section 12 (App. G guidance row) fixes 'NA'` |
| `order.json` | rows out of Table H-1 order | `row order differs from Table H-1 at row 0: matrix has SE-24, Table H-1 has SE-07` |
| `duplicate-id.json` | an id twice | `row 10 (SE-07): duplicate se_id` |
| `stale.md` | rendered file out of date | `--check` fails (`test_cli_check_detects_stale_render`) |

**Run command** (repository root):

```
.venv/bin/python -m unittest discover -v -s tools/tests -p test_render_compliance.py -k CorpusParseTests -k ValidFixtureTests -k SeededFaultTests
```

**Pass criteria:** all selected tests pass, none skipped: each seeded fault gives exactly its expected error string and a CLI exit of 1; `valid.json` gives no error and renders to `valid.md`; `--check` passes on the current render and fails on `stale.md`. `ProjectMatrixTests` (the repository matrix `--check`, `rows=62 corpus=62`) checks repository content and is recorded in the lock's repository-content row.

## 4. Result

| Run | Date and time (CDT) | Commit tested | Tests | Result |
|---|---|---|---|---|
| 1 | 2026-09-25 23:36 | `28e49e6` (tool, test, fixture and the two repository inputs of section 1 byte-identical to the commit) | 26 (`CorpusParseTests` 5, `ValidFixtureTests` 9, `SeededFaultTests` 12), 0 skipped | pass |
| 2 | 2026-09-25 23:45 | same | 26, 0 skipped | pass |

The repository check `ProjectMatrixTests` passed in both runs. The earlier run of 19:36 on the working tree at `b8214ca` (27 tests, whole module) is in lock section 1.1. Evidence: `docs/cm/tool-validation/evidence/python-tools-2026-09-25.log.txt`.

## 5. Reproducibility

Not required for class B. Runs 1 and 2 gave identical results.

## 6. Limitations

1. The fixture tests validate against the project schema `docs/process/se-compliance-matrix.schema.json`, not a fixture copy, and `test_real_corpus_has_62_rows` reads the full corpus file: a schema or corpus edit can change this known-answer result without any tool change. Both inputs are identified in section 1; a change of either is a re-validation trigger.
2. The corpus parser is validated on the extract `appendix-h.md` and on the row count and first id of the full App. H copy; the cross-check is only as correct as the corpus conversion (`tools/refs/`, class C).
3. Output is developer evidence until section 9 records the accreditation.

## 7. Re-validation triggers

- Any change of the tool, its test module or its fixtures (CM plan section 9.2 step 4).
- A change of `docs/process/se-compliance-matrix.schema.json` or of the App. H corpus copy.
- A change of the interpreter or jsonschema (TV-001).
- A defect found in the tool (an NCR per SWE-201).

## 8. Independent review (CM plan section 9.2 step 3)

Pending. Reviewer invocation, date and result are recorded here.

## 9. Accreditation (owner)

Proposed scope statement **ACC-COMPL-001**: "Accredited for purposes 1 to 4 for `tools/render_compliance.py` at git blob `d67d6b5e601a64b013b64e8de3cd0fc3deb96ffa` (commit `28e49e6`), with the schema and corpus copy of section 1, under the TV-001 interpreter."

| Decision | Date | Recorded by |
|---|---|---|
| Pending (owner, at SRR, after section 8) | | |
