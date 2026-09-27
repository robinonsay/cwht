# TV-017: tools/render_tpm.py (git blob f37985d6, commit c90df2d)

| Field | Value |
|---|---|
| Record | TV-017 |
| Status | **Validated** 2026-09-27 (known-answer run 1 at commit `c90df2d`: 12 tests passed, 0 skipped; fixture renders inspected). Independent review and owner accreditation pending (sections 8 and 9) |
| Class | B, evidence-generating (CM plan section 9.1: the TPM table and trend plots are review evidence for SE-43 and SE-61) |
| Governs | SWE-136 (NPR 7150.2D section 4.4.8) through CM plan section 9; SEMP section 7.4 (TPM reporting); `docs/plan/tpm.json` conventions `status_rule` and `reporting_interval` |
| Due | PDR (CM plan section 13 PDR row). First cited use: `docs/reviews/PDR/figures/tpm-status.png` and the trend plots of WP-PDR-29 |
| Lock rows | `tools/toolchain.lock.md` section 1.1 row `tools/render_tpm.py`; section 1.2 row `tools/render_tpm.py`; section 2 (matplotlib 3.11.2, pillow 12.3.0); section 5 |
| Author | Claude, tool owner (WP-PDR-07, wave 1a) |

## 1. Identification

| Item | Identity | State |
|---|---|---|
| `tools/render_tpm.py` | git blob `f37985d67e94998c9de4f790dccac7592f9ccd34`, SHA-256 `95a0cffb9a480533035a408ac096280b748ebd2e416f2e824455bde6b0b0193e`, 323 lines | committed in `c90df2d` (the first blob, `86ff3b0`, named `docs/plan/tpm.json` in its header for any input and drew the planned line on the frame; found by the author's render inspection before the validation run) |
| `tools/tests/test_render_tpm.py` | git blob `a6b93352bffd5c15907e4e37209cfe5911c8b17d`, SHA-256 `18f5232b54fd88823382acd3032726a5ba49c85256d861841783b7e85cf8239c`, 12 tests | committed in `86ff3b0` |
| `tools/tests/fixtures/render_tpm/` | 2 files (`tpm.json`, `expected.json`), git tree `9a6aff2536b65027c9fc4eb0a424a92fd139dcc9`, digest `02c031f263c08afa0f98e99bababa18f76a13a853ddea10fc760aa6ce63942d0` | committed in `86ff3b0` |
| `docs/plan/tpm.json` (read by `RepositoryTests` only) | git blob `e7f2070d93f4abeed28c32e48670dcef90930bb0` | repository content, not the validation |
| Runtime | TV-001 interpreter (Python 3.13.5), matplotlib 3.11.2 (Agg), pillow 12.3.0 (test only) | lock section 2 |

**Install source:** the repository (CM plan Table 4-1 row 28); matplotlib and pillow from `tools/requirements.txt` (lock section 2).

## 2. Purposes covered

1. Give, for one review token (SRR, PDR, CDR, TRR, TRR-D<n>, SAR) and an as-of date, the status of every TPM of a `tpm.json`: the recorded status of the TPM's last history entry for that review; red ("no estimate at a reporting review") when there is none and the review is in `reporting_review` (a TRR-D<n> matches `TRR-Dn`); "not due" otherwise; with the carried value of the latest earlier entry. Entries dated after the as-of date are ignored.
2. Refuse, with exit 1 and nothing written, a `tpm.json` whose drawn data are malformed: no TPM, a bad or duplicate id, a missing or duplicate key, a history entry with a review token outside the schema pattern, a date not YYYY-MM-DD, a cbe that is neither a number nor null (booleans included), a status other than green, yellow or red, a credit that is not a boolean, or dates out of order.
3. Write the table `tpm-status.png` (1920 x 1080 px, one status chip per TPM in its status colour), `tpm-table.md` (the same rows and the counts), and `tpm-trend-<key>.png` (1600 x 900 px) for each TPM with a numeric cbe, except `review-trend` (plotted by `tools/review_trend.py`), each point the cbe of one history entry in its recorded colour; `--check` writes nothing.

Not covered: the tool does not evaluate margin policies or thresholds (they are prose; the recorded status is shown), and it does not validate `tpm.json` against its schema (TV-003 does). The pixel content of the trend plots is checked by inspection, not by a known answer (limitation 2).

## 3. Known-answer test

**Fixture:** `tools/tests/fixtures/render_tpm/tpm.json` (seven TPMs, one per status case: own entry green; status note then own entry yellow; `review-trend`; only an SRR entry at a reporting review; no history at a reporting review; not a reporting review, with a later TRR-D2 entry; a PDR entry dated after the as-of date) and `expected.json` (rows, counts, trend points, chip colours, image sizes and seeded faults, derived by hand from the status rule before the first run). Module `tools/tests/test_render_tpm.py`.

| Class | Known answer |
|---|---|
| `RowKnownAnswerTests` (3) | the seven rows at PDR as of 2026-10-06 and at TRR-D2 as of 2027-02-01 (status, basis, cbe, entry token and date, credit) equal `expected.json`; the trend points of five TPMs equal their lists (status-note entry included, null cbe excluded, the late entry excluded) |
| `RenderTests` (5) | exit 0; exactly `tpm-status.png`, `tpm-table.md` and the four expected trend files; counts "green 2, yellow 1, red 3, not due 1"; review-trend skipped with its message; pixel sizes 1920 x 1080 and 1600 x 900; in each of the seven table rows the pixel 8 px inside the chip has the RGB of the row's expected status within 3 per channel; two Markdown rows and the counts line verbatim; `--check` prints the table and writes nothing |
| `SeededFaultTests` (2) | each of the ten seeded faults of `expected.json` (duplicate key, duplicate id, bad id, status blue, cbe string, cbe boolean, credit string, review token MCR, date 25-09-2026, dates out of order) exits 1 with its exact message and writes nothing; an empty `tpms` exits 1 |
| `UsageTests` (1) | exit 2 for no `--review`, review MCR, the placeholder TRR-Dn, a bad `--date`, an absent or unparseable `tpm.json`, an absent output directory and an unknown option |
| `RepositoryTests` (1) | repository content, recorded separately: `docs/plan/tpm.json` passes the data checks at PDR (`--check` exit 0) |

**Run command:** `bash docs/cm/tool-validation/evidence/pdr-tools-2026-09-27.sh TV-017 > docs/cm/tool-validation/evidence/render-tpm-<date>-run<N>.log.txt`; part C is `.venv/bin/python -m unittest discover -v -s tools/tests -p test_render_tpm.py`; part E renders the fixture at PDR as of 2026-10-06 and copies `tpm-status.png` and one trend plot into the evidence folder for inspection.

**Pass criteria:** part C exits 0 with 12 tests run and passed, none skipped (11 fixture tests and the repository test); part E exits 0; both renders are opened and inspected.

## 4. Result

| Run | Date and time (CDT) | Commit tested | Result |
|---|---|---|---|
| 1 | 2026-09-27 12:48 | `c90df2d` (tool `f37985d6`, module `a6b93352`, fixture tree `9a6aff25`, every identity "unchanged from HEAD") | **Pass.** 12 of 12 in 1.2 s, 0 skipped; part E exit 0. Renders inspected: `evidence/render-tpm-fixture-tpm-status.png` (SHA-256 `af7a8ac9db09332f303feebfccdd436fb1b218603d0e580a73557f9e7e0f39ad`: seven legible rows, chips green, yellow, green, red, red, grey, red as expected, subtitle names the fixture file) and `evidence/render-tpm-fixture-trend-own-yellow-after-status-note.png` (SHA-256 `bca50ca4971cbaecdaa33d628fa4efc3098c4fbb4a7a93ea1ba823de4d10dda8`: points 2 (red, status-2026-09-30) and 5 (yellow, PDR), the planned line at 7 inside the frame with its legend). Transcript `evidence/render-tpm-2026-09-27-run1.log.txt` |

Author's observation on the repository content (not the validation): at PDR as of 2026-09-27, `docs/plan/tpm.json` renders 19 TPMs red ("no estimate at a reporting review") and TPM-017 not due, because no PDR history entry exists yet; those entries are WP-PDR-29 work.

## 5. Reproducibility

Not required for class B. The PNGs are written with the `Software` metadata removed; `RenderTests` depends only on sizes and sampled pixels.

## 6. Limitations

1. Status is transcribed, never computed from the margin policy (section 2); a wrong recorded colour is shown as recorded. The TPM owner's status determination is reviewed with the TPM record (`docs/reviews/PDR/checklists/tpm-definitions.md`, WP-PDR-29).
2. The trend plots' drawn content is validated through the trend points of the data model and by inspection of the renders; no pixel known answer checks marker positions.
3. The table fits about 25 TPMs at a legible size (row height shrinks with the count; font 9 to 15 pt).
4. Long units are shortened in the PNG (the text before the first "(" or ";", at most 26 characters); the Markdown keeps the full text.
5. Output is developer evidence until section 9 records the accreditation (CM plan section 9.1).

## 7. Re-validation triggers

- Any change of `tools/render_tpm.py`, `tools/tests/test_render_tpm.py` or `tools/tests/fixtures/render_tpm/` (CM plan section 9.2 step 4).
- A version change of matplotlib or pillow (lock section 2), of the TV-001 interpreter, or a macOS major version change.
- A change of `docs/plan/tpm.schema.json` history-entry pattern or of `conventions.status_rule` in `tpm.json`.
- A defect found in the tool (an NCR per SWE-201).

## 8. Independent review (CM plan section 9.2 step 3)

Pending. Record: `docs/reviews/PDR/checklists/tool-validation-tv-014-to-tv-019.md` (PDR work plan WP-PDR-07).

## 9. Accreditation (owner)

Proposed scope statement **ACC-TPM-001**: "Accredited for purposes 1 to 3 for `tools/render_tpm.py` at git blob `f37985d67e94998c9de4f790dccac7592f9ccd34` with the TV-001 interpreter and matplotlib 3.11.2, within the limitations of section 6."

| Decision | Date | Recorded by |
|---|---|---|
| Pending (owner, after the section 8 review is APPROVED) | | |
