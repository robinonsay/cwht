# TV-010: tools/render_review_figures.py (git blob 979beb13)

| Field | Value |
|---|---|
| Record | TV-010 |
| Status | **Validated** (2026-09-25) on the working-tree file identified in section 1, which is not yet committed. Independent review and owner accreditation pending (sections 8 and 9) |
| Class | B, evidence-generating (CM plan section 9.1: its figures are review-package and deck evidence, charter section 4 items 1 and 2) |
| Governs | SWE-136 (NPR 7150.2D section 4.4.8), SWE-070 (section 4.5.6) through CM plan section 9 |
| Due | SRR (CM plan section 13, SRR row; its known-answer row is in CM plan section 9.2). Assigned with SRR package section 2 item H12 (the controlled figure generator of item H10) |
| Lock rows | `tools/toolchain.lock.md` section 1.1 row `tools/render_review_figures.py`; section 1.2 |
| Author | Claude, tool validation author |

## 1. Identification

| File | Git blob | SHA-256 | State against commit `28e49e6` |
|---|---|---|---|
| `tools/render_review_figures.py` | `979beb139d13df8a64e295b2c6aac0d71a83c0e0` | `58643ecd37583f1c392ca24c2440229a5c305a5aa7c3a26d8abcdfdcd61e0865` | untracked |
| `tools/tests/test_render_review_figures.py` | `ff5d81facd2d95718be681270238c6c980f2494c` | `cd572a0f...e64c1d53` | untracked |
| `tools/tests/fixtures/review_figures/` (miniature `package.md`, `requirements.json`, `hazards.json`, `register.json`, `tpm.json`, `conops.md`) | 6 files, tree digest `9cab14eb7ea5fa650fb2bc34d87b7386e86dce7a039afc32a0b25311450475ae` | | untracked |

**Install source:** the repository (CM plan Table 4-1 row 28). **Runtime:** TV-001 interpreter; matplotlib 3.11.2 (venv, lock section 2; installed `RECORD` SHA-256 `3e94b1a680a17f79d06837edcab0f1233f871d97e94b858a023fd3eccd106c93`); font Source Sans Pro from `tools/slides/node_modules/reveal.js/dist/theme/fonts/source-sans-pro/` (reveal.js 5.2.1, TV-008 section 1), else DejaVu Sans with a printed notice.

## 2. Purposes covered

1. Read the statuses of a review package (`docs/reviews/<REVIEW>/package.md`: entrance section 4, requirements section 8 with its functional-group table, success section 20) and the counts of the product files (`docs/requirements/sys/requirements.json`, `docs/safety/hazards.json`, `docs/risk/register.json`, `docs/plan/tpm.json`, the section 6 headings of `docs/conops/conops.md`).
2. Cross-check every literal of the review's figure set that restates repository content (labels against package rows, group rows against the requirement file, KDR list against the `KDR` priorities, TPM rows and text against `tpm.json`, scenario lists against the ConOps) and exit 1 with nothing written on any disagreement; print figure-set overrides, and report an override as redundant once the package carries it.
3. Render the figures of the set (entrance board, success board, requirements by group, KDR map, hazard matrices, TPM board, ConOps modes and scenarios; the risk matrix and concept block diagram are implemented but outside the SRR set) at their slide pixel sizes into `docs/reviews/<REVIEW>/figures/` or `--out`; with `--check`, read and cross-check only and write nothing.
4. Exit 0 when written or checked, 1 on a disagreement or missing input, 2 on a usage error (unknown review token, no figure set for the review, figure outside the set).

## 3. Known-answer test

**Fixture:** `tools/tests/fixtures/review_figures/`: a miniature SRR package and product files whose counts are the known answers, with a fixture figure set (`FIXTURE_SET` in the test module) whose labels match the fixture package.

**Run command** (repository root):

```
.venv/bin/python -m unittest discover -v -s tools/tests -p test_render_review_figures.py -k ParserTests -k DataKnownAnswerTests -k RunTests
```

**Pass criteria:** all 32 selected tests pass, none skipped: every parser (`ParserTests`), every drawn value and every cross-check including each disagreement case (`DataKnownAnswerTests`), and the run behavior (`RunTests`: usage errors exit 2, `--check` writes nothing and prints the stored counts, a disagreement exits 1 and writes nothing, all nine figures render at their stored pixel sizes, the default output folder, the SRR set composition, the CLI against the fixture). `RepositoryTests` (the SRR `--check` on the repository completes without a traceback) is repository content and is recorded in the lock's repository-content row.

**Inspection (added by this record):** the nine fixture figures were rendered once more with the fixture figure set (`rrf.run("SRR", FIXTURE, out=<temporary>, figure_sets={"SRR": FIXTURE_SET})`, the call of `test_render_every_figure_at_its_slide_size`) and each was opened and compared with the fixture inputs.

## 4. Result

| Run | Date and time (CDT) | Commit tested | Tests | Result |
|---|---|---|---|---|
| 1 | 2026-09-25 23:36 | `HEAD` `28e49e6`; tool, test and fixture untracked, identities of section 1 | 32 (`ParserTests` 7, `DataKnownAnswerTests` 18, `RunTests` 7), 0 skipped | pass |
| Inspection | 2026-09-25 23:38 | same | 9 PNGs | pass: entrance counts Not met 1, Partially met 2 (the fixture re-rating of row 2 applied), Met 1 with the dagger note; success counts 2, 0, 1 with the two footer lines; requirements by group Transmitter 3 (Test, Analysis, Retired) and Receiver 2 (Inspection, Demonstration), 1 open TBR; KDR map REQ-SYS-001 (Test, TBR) and REQ-SYS-004 (Inspection); hazard matrices HZ-001 B to D Catastrophic and HZ-002 C to E Marginal; risk matrix RSK-001 at L4 C4 (R 16), RSK-002 at L2 C5 marked Red by safety override, RSK-003 at L1 C2, legend Red 2, Yellow 0, Green 1; TPM board TPM-001 Red by the status rule, TPM-002 Yellow, TPM-003 not reported; ConOps modes with OPS-001 nominal and OPS-002 off-nominal; concept block diagram legible. Every value equals the fixture inputs and the test's stored answers |
| 2 | 2026-09-25 23:45 | same identities | 32, 0 skipped | pass |

Renders inspected: `docs/cm/tool-validation/evidence/render-review-figures-fixture-*.png` (nine files). Evidence: `docs/cm/tool-validation/evidence/python-tools-2026-09-25.log.txt`.

## 5. Reproducibility

Not required for class B. The runs gave identical results. PNG bytes are not compared (font rasterization); the criteria are the drawn values, the cross-checks and the pixel sizes.

## 6. Limitations

1. **Uncommitted tool.** The validated file, its test and its fixture are untracked; the accreditation, when given, covers blob `979beb13` only.
2. **Literals.** Short labels, layouts, the ConOps modes diagram and the concept block diagram are literals of the review's figure set. The tool cross-checks every literal that restates repository content, but the modes diagram's states and transitions and the concept diagram's blocks are drawn as written in the source; the known-answer test checks their pixel size, not their drawing. Their correctness rests on the figure author's inspection (charter section 11 rule 3) and the visual-product checklist review.
3. Axis ranges of the requirements-by-group figure: the main axis runs from 0 to max(29, largest group count + 3) and the open-TBR axis from 0 to max(20, largest open-TBR count + 3) (`draw_requirements`, `tools/render_review_figures.py` lines 621 and 622), so both extend with the data and no bar is drawn outside its axis. The fixture render shows the minimum ranges (0 to 29 with the last tick at 25, and 0 to 20; `evidence/render-review-figures-fixture-requirements-by-group.png`, reopened 2026-09-26). The known-answer test does not check axis limits: the extension branch (a group count above 26 or an open-TBR count above 17) has no known answer, and a figure in which it applies rests on the author's inspection of that render (limitation 2). Corrected 2026-09-26 after review INSP-015 finding-4; the earlier text described fixed ranges the code does not have.
4. Only the SRR figure set exists; `--review PDR` exits 2 until a PDR set with its own known-answer test is added, which is a new version of the tool.
5. Output is developer evidence until section 9 records the accreditation.

## 7. Re-validation triggers

- Any change of the tool, its test module or its fixture (CM plan section 9.2 step 4).
- A new figure set or figure.
- A change of matplotlib, of the font files, or of the interpreter (TV-001).
- A defect found in a figure that the tool caused (an NCR per SWE-201).

## 8. Independent review (CM plan section 9.2 step 3)

Pending. The reviewer re-runs section 3 and opens the nine inspection PNGs. Reviewer invocation, date and result are recorded here.

## 9. Accreditation (owner)

Proposed scope statement **ACC-FIGS-001**: "Accredited for purposes 1 to 4 for `tools/render_review_figures.py` at git blob `979beb139d13df8a64e295b2c6aac0d71a83c0e0`, SRR figure set only, under the TV-001 interpreter and matplotlib 3.11.2, for figures whose render is inspected by the author (limitation 2)."

| Decision | Date | Recorded by |
|---|---|---|
| Pending (owner, at SRR, after section 8) | | |
