# TV-004: tools/render_rmm.py (git blob 2386a37f, commit 28e49e6)

| Field | Value |
|---|---|
| Record | TV-004 |
| Status | **Validated** (2026-09-25). Independent review and owner accreditation pending (sections 8 and 9) |
| Class | B, evidence-generating (CM plan section 9.1) |
| Governs | SWE-136 (NPR 7150.2D section 4.4.8), SWE-070 (section 4.5.6) through CM plan section 9; the tool checks the RMM of SWE-125 and SWE-139 against NPR 7150.2D App. C |
| Due | SRR (CM plan section 13; 03 section 6.1) |
| Lock rows | `tools/toolchain.lock.md` section 1.1 row `tools/render_rmm.py`; section 1.2 |
| Author | Claude, tool validation author (SRR package section 2 item H12) |

## 1. Identification

| File | Git blob | SHA-256 | State against commit `28e49e6` |
|---|---|---|---|
| `tools/render_rmm.py` | `2386a37fbfb9d7d06c333e0f00981b6fc67e1f27` | `face0b9e5135585a583a6912e4ae6eda793e515e72e1ad9f2f52a453ee9c1896` | equal |
| `tools/tests/test_render_rmm.py` | `0454936bf20498078de9ae2861af727c3a66350e` | `58f58a7f...1c4295` | equal |
| `tools/tests/fixtures/rmm/` | 17 files, tree digest `fa7f91afec62aa69e01f5fe73cde09720a7c7a6df4d7e09836bfddd69c6f89ce` | | equal |

The tool imports only the Python standard library. **Install source:** the repository (CM plan Table 4-1 row 28). **Runtime:** TV-001 interpreter.

## 2. Purposes covered

1. Check `docs/process/rmm.json` (or `--rmm`): structure (required fields, id format, no duplicate ids, `class_a_applicable` true, disposition FC, T or NA, status Planned or In place, authority, implementation and responsible present); disposition rules (T and NA rows carry `tailoring_rationale` and `residual_risk` of the minimum length, FC rows carry neither); exit 1 on any error.
2. Cross-check the row set and every row's `npr_section`, `authority_npr` and verbatim `requirement_text` against NPR 7150.2D App. C Table 2 in the corpus copy (`--corpus`), and the Class A set against the `[SWE-NNN]` tags of chapters 3 to 5 (`--chapters`).
3. Apply the status rule of 03 section 6.3 (an In place row names no absent repository path unless it carries `Planned for <gate>`; a Planned row names an absent path or carries that label) against a repository root (`--repo`).
4. Render `docs/process/rmm.md` (or `--out`), and with `--check` fail when the rendered file differs from a fresh render.

## 3. Known-answer test

**Fixtures:** `tools/tests/fixtures/rmm/`: a valid matrix `valid.json` with its stored render `valid.md`, an App. C extract `appendix-c.md`, chapter extracts `chapters/` and `chapters-mismatch/`, a miniature repository `repo/` for the status rule, and one seeded fixture per fault: missing Class A row, extra row, altered `requirement_text`, wrong `npr_section`, FC row with a rationale, T row with a short `residual_risk`, In place row naming an absent path, Planned row without a `Planned for <gate>` label, chapter-tag mismatch, stale `rmm.md` (03 section 6.1).

**Run command** (repository root): `.venv/bin/python -m unittest discover -v -s tools/tests -p test_render_rmm.py`

**Pass criteria:** all tests pass, none skipped: `valid.json` renders to the stored `valid.md`, passes `--check` and lists its ids; each seeded fixture fails with exactly its expected error string; the CLI exits 1 on a fault.

## 4. Result

| Run | Date and time (CDT) | Commit tested | Tests | Result |
|---|---|---|---|---|
| 1 | 2026-09-25 23:36 | `28e49e6` (tool, test module and fixture byte-identical to the commit) | 20 (`CorpusParseTests` 4, `ValidFixtureTests` 6, `SeededFaultTests` 10), 0 skipped | pass |
| 2 | 2026-09-25 23:45 | same | 20, 0 skipped | pass |

Earlier runs, on the working tree at `b8214ca`, are in lock section 1.1 (2026-09-25, 18:23 and 19:36: pass, 20 tests). Evidence: `docs/cm/tool-validation/evidence/python-tools-2026-09-25.log.txt`.

## 5. Reproducibility

Not required for class B. Runs 1 and 2 gave identical results.

## 6. Limitations

1. The App. C and chapter parsers are validated on fixture extracts that reproduce the corpus layout; their correctness on the full corpus files (`docs/references/md/npr-7150-2d/09-appendixc.md`, chapters 3 to 5) rests on those extracts being faithful and on the corpus conversion (`tools/refs/`, class C, not accredited). A corpus re-conversion is a re-validation trigger.
2. The verbatim comparison is exact string equality after the tool's own whitespace handling; it cannot tell a transcription error in the corpus copy from one in `rmm.json`.
3. The status rule reads path mentions in free text; a path written in a form the tool's `named_paths` does not recognize is not checked (placeholder paths are skipped by design, `test_named_paths_skip_placeholders`).
4. Output is developer evidence until section 9 records the accreditation.

## 7. Re-validation triggers

- Any change of the tool, its test module or its fixtures (CM plan section 9.2 step 4).
- A change of the interpreter (TV-001).
- A re-conversion or edit of the NPR 7150.2D corpus files the tool reads.
- A defect found in the tool (an NCR per SWE-201).

## 8. Independent review (CM plan section 9.2 step 3)

Pending. Reviewer invocation, date and result are recorded here.

## 9. Accreditation (owner)

Proposed scope statement **ACC-RMM-001**: "Accredited for purposes 1 to 4 for `tools/render_rmm.py` at git blob `2386a37fbfb9d7d06c333e0f00981b6fc67e1f27` (commit `28e49e6`), under the TV-001 interpreter."

| Decision | Date | Recorded by |
|---|---|---|
| Pending (owner, at SRR, after section 8) | | |
