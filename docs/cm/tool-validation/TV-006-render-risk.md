# TV-006: tools/render_risk.py (git blob d38ba1dd, commit 28e49e6)

| Field | Value |
|---|---|
| Record | TV-006 |
| Status | **Validated** (2026-09-25; re-run at commit `400e59d` on 2026-09-26, SRR package item R5). Independent review and owner accreditation pending (sections 8 and 9) |
| Class | B, evidence-generating (CM plan section 9.1) |
| Governs | SWE-136 (NPR 7150.2D section 4.4.8), SWE-070 (section 4.5.6) through CM plan section 9; the tool checks and renders the risk register of `docs/process/06-risk-and-decision-analysis.md` (06 section 12) |
| Due | SRR (CM plan section 13) |
| Lock rows | `tools/toolchain.lock.md` section 1.1 row `tools/render_risk.py`; section 1.2 |
| Author | Claude, tool validation author (SRR package section 2 item H12) |

## 1. Identification

| File | Git blob | SHA-256 | State against commit `28e49e6` |
|---|---|---|---|
| `tools/render_risk.py` | `d38ba1dd25ac8ef5ecb04ce5b1ea907bb60eee8c` | `fd3fcbd92f5282a65a41d791d6554d83ac002ccec018607c8017ac61b7947836` | equal |
| `tools/tests/test_render_risk.py` | `05d695a4dd8c7d0510fd9a2c078584d6e3316b21` | `54c9ad7e...417fb01f` | equal |
| `tools/tests/fixtures/risk/` (`valid.json`, `valid.md`, `stale.md`, `faults.json`, `hazards.json`) | 5 files, tree digest `3a594f973adbb7c16af2d2d944eced06110abb51811e9bd234dd125aeb1ea8c1` | | equal |
| `docs/risk/schema.json` (read by `validate_with_jsonschema`, the tool's `SCHEMA`) | `473cd797db582ae2dc4ed14fa83213c3bf2a6d09` | | equal |

The tool uses jsonschema (TV-001) for the schema check and the standard library otherwise. **Install source:** the repository (CM plan Table 4-1 row 28).

## 2. Purposes covered

1. Check `docs/risk/register.json` (`--register`): schema (jsonschema, `docs/risk/schema.json`), score equal to likelihood times maximum consequence, band edges and the safety override, aggregate likelihood of children, strategy, status and step rules for Red risks, acceptance and residual rules, trend, Realized links, Low-confidence rules, software tag, `last_assessed` and history rules, triggers, candidates (06 sections 3, 5, 8, 9, 12).
2. With `--gate <REVIEW>`, apply the gate rules (Track pass before PDR, Red plan approval after the first gate, Red requirement or hazard link from PDR, gate token); with `--hazards`, the hazard link rule (back-links, safety not below the mapped severity, every hazard covered).
3. Render the register Markdown (`--output`), ranked, with the measures table, and with `--check` fail when the rendered file differs from a fresh render (`register.md is stale; run without --check`).
4. Exit 0 when the register passes, 1 on any error.

## 3. Known-answer test

**Fixtures:** `tools/tests/fixtures/risk/`: `valid.json` with its stored render `valid.md`, `stale.md`, `hazards.json` for the hazard rule, and `faults.json`: 23 seeded faults, each a list of edit operations on `valid.json` with the exact error list it must give (the file is the fault list of record): `score_mismatch`, `red_one_active_step`, `red_strategy_watch`, `red_strategy_accept_while_mitigating`, `red_status_watch`, `override_red_at_L2_S5`, `override_yellow_at_L1_S5` (no error), `aggregate_mismatch`, `accepted_without_acceptance`, `acceptance_without_residual`, `residual_score_mismatch`, `trend_mismatch`, `realized_without_ncr_or_cr`, `low_confidence_without_control`, `low_confidence_reassess_trigger_only` (no error), `low_confidence_research_strategy` (no error), `software_tag_missing`, `last_assessed_review_mismatch`, `active_risk_without_trigger`, `last_history_without_safety`, `candidate_not_in_source`, `declined_candidate_without_rationale`, `candidate_unknown_risk`. `test_fault_set_covers_required_cases` fails if a required case is removed from the file.

**Run command** (repository root): `.venv/bin/python -m unittest discover -v -s tools/tests -p test_render_risk.py`

**Pass criteria:** all tests pass, none skipped (the schema tests skip when jsonschema is missing, so a skip is a failure of this check): band edges at scores 4, 5, 10 and 12, the safety override at L1 and L2, ranking and measures reproduce stored values; `valid.json` gives no error or warning, renders to `valid.md` and passes `--check`, `--gate SRR` and `--hazards`; each seeded fault gives exactly its stored errors; each gate and hazard case gives its expected error (06 section 12).

## 4. Result

| Run | Date and time (CDT) | Commit tested | Tests | Result |
|---|---|---|---|---|
| 1 | 2026-09-25 23:36 | `28e49e6` (tool, test, fixture and `docs/risk/schema.json` byte-identical to the commit) | 27 (`BandTests` 3, `ValidFixtureTests` 10, `SeededFaultTests` 3 of which one runs the 23 faults as subtests, `GateTests` 7, `HazardCrossCheckTests` 4), 0 skipped | pass |
| 2 | 2026-09-25 23:45 | same | 27, 0 skipped | pass |
| 3 | 2026-09-26 02:31 | `HEAD` `400e59d` (SRR package item R5): an export of the commit (`git archive HEAD`); tool, test modules and fixtures equal to `400e59d` | 27, 0 skipped | pass |

Earlier runs on the working tree at `b8214ca` (18:33 and 19:36, 27 tests, pass) are in lock section 1.1. Evidence: `docs/cm/tool-validation/evidence/python-tools-2026-09-25.log.txt`.

R5 re-run (2026-09-26, SRR package section 2.1 item R5; INSP-015 finding-2): section 3 run at commit `400e59d` on an export of the commit, so the result is bound to a commit that contains every file tested: every tool, test module and fixture identity line of the transcript reads "equal to HEAD". Evidence `evidence/python-tools-2026-09-26-r5-head.log.txt` (procedure `evidence/python-tools-2026-09-26-r5.py`, mode `head`).

## 5. Reproducibility

Not required for class B. Runs 1 and 2 gave identical results.

## 6. Limitations

1. The schema check uses the repository schema `docs/risk/schema.json`, not a fixture copy; a schema edit can change the result of `test_schema_accepts_fixture` and of the two schema subtests without a tool change (a re-validation trigger).
2. The 23 faults are single faults on one valid register; interactions of several faults in one risk are not tested.
3. The scales and bands are the project-defined ones of 06 (charter section 1: NPR 8000.4 is not adopted); the accreditation says the tool applies 06 as written, not that 06 is right.
4. Output is developer evidence until section 9 records the accreditation.

## 7. Re-validation triggers

- Any change of the tool, its test module or its fixtures (CM plan section 9.2 step 4).
- A change of `docs/risk/schema.json`, or of the scales, bands or rules of 06 that the tool implements.
- A change of the interpreter or jsonschema (TV-001).
- A defect found in the tool (an NCR per SWE-201).

## 8. Independent review (CM plan section 9.2 step 3)

Pending. Reviewer invocation, date and result are recorded here.

## 9. Accreditation (owner)

Proposed scope statement **ACC-RISK-001**: "Accredited for purposes 1 to 4 for `tools/render_risk.py` at git blob `d38ba1dd25ac8ef5ecb04ce5b1ea907bb60eee8c` (commit `28e49e6`), with `docs/risk/schema.json` at blob `473cd797`, under the TV-001 interpreter."

| Decision | Date | Recorded by |
|---|---|---|
| Pending (owner, at SRR, after section 8) | | |
