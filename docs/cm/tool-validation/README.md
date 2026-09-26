# Tool validation records (SWE-136)

**Governs:** SWE-136 (NPR 7150.2D section 4.4.8: validate and accredit the software tools required to develop or maintain software) and SWE-070 (section 4.5.6: validated and accredited models, simulations and analysis tools), through the procedure of `docs/process/05-configuration-and-data-management.md` section 9 (the CM plan). **Charter:** section 5 (`docs/cm/tool-validation/TV-NNN-<tool>.md`, summarized in `tools/toolchain.lock.md`), section 6 (`TV-NNN`; `ACC-<TOOL>-NNN` scope statements held inside their TV record), section 8 (every analysis or build tool has a documented sanity check). **Maintainer:** Claude (software lead). **Accreditation authority:** the owner (CM plan section 9.2 step 3).

## Record format

Every record carries, in this order, the fields of CM plan section 9.2 step 1 and the two decisions of step 3:

1. Identification: tool name, exact version string and the command that produced it, install source with installer URL and SHA-256 (lock section 7), the SHA-256 or git blob of every file validated, and whether each file equals a commit.
2. Class (CM plan section 9.1) and the purposes accreditation covers, one line each.
3. Known-answer test: description, fixture paths under `tools/tests/fixtures/<tool>/`, run command, pass criteria with the seeded faults.
4. Result: date and time, commit tested, test count, output excerpt, evidence file.
5. Reproducibility (required for class A: two runs, identical output hash, normalized where the tool writes time stamps).
6. Limitations.
7. Re-validation triggers (CM plan section 9.2 step 4 plus the tool's own).
8. Independent review (CM plan section 9.2 step 3).
9. Accreditation: the proposed `ACC-<TOOL>-NNN` scope statement and the owner's decision, recorded as "Accredited for purposes 1 to n at version v".

**Status values.** *Validated*: steps 1 and 2 of CM plan section 9.2 are done and the known-answer test passed. *Reviewed*: the independent reviewer's check (step 3) is recorded with no open Major finding. *Accredited*: the owner's decision is recorded in section 9 of the record and the tool is entered as Accredited in `tools/toolchain.lock.md`. Until a tool is Accredited its output is developer evidence only (CM plan section 9.1).

## Index

| Record | Tool and version | Class | Due (CM plan section 13) | Status (2026-09-25) |
|---|---|---|---|---|
| [TV-001](TV-001-python-jsonschema.md) | venv Python 3.13.5 with jsonschema 4.26.0 | B | SRR | Validated (re-validated 2026-09-26 after INSP-015 finding-1); review and accreditation pending |
| [TV-002](TV-002-traceability.md) | `tools/traceability.py` (working-tree blob `0a867523`) | B | SRR | Validated; review and accreditation pending |
| [TV-003](TV-003-validate-docs.md) | `tools/validate_docs.py` (blob `2bedc2a7`, equal to commit `28e49e6`) | B | SRR | Validated (re-validated 2026-09-26 after INSP-015 finding-5); review and accreditation pending |
| [TV-004](TV-004-render-rmm.md) | `tools/render_rmm.py` (blob `2386a37f`, equal to `28e49e6`) | B | SRR | Validated; review and accreditation pending |
| [TV-005](TV-005-render-compliance.md) | `tools/render_compliance.py` (blob `d67d6b5e`, equal to `28e49e6`) | B | SRR | Validated; review and accreditation pending |
| [TV-006](TV-006-render-risk.md) | `tools/render_risk.py` (blob `d38ba1dd`, equal to `28e49e6`) | B | SRR | Validated; review and accreditation pending |
| [TV-007](TV-007-review-trend.md) | `tools/review_trend.py` (blob `04493157`, equal to `28e49e6`) | B | SRR | Validated; review and accreditation pending |
| [TV-008](TV-008-render-deck-chromium.md) | `tools/slides/render_deck.py` (blob `b42425e9`, equal to `28e49e6`) with the Chromium headless shell 1223 (Chrome for Testing 148.0.7778.96) | B | SRR | Validated (re-validated 2026-09-26 after INSP-015 finding-5); review and accreditation pending |
| [TV-009](TV-009-git.md) | git 2.50.1 (Apple Git-155) | B | SRR | Validated; review and accreditation pending |
| [TV-010](TV-010-render-review-figures.md) | `tools/render_review_figures.py` (untracked blob `979beb13`) | B | SRR | Validated; review and accreditation pending |

The sanity checks of the tools whose TV records fall due at PDR, CDR or TRR (kicad-cli, LTspice, the Rust toolchain, clippy, picotool, OpenSCAD with FreeCAD, and the rest of `tools/toolchain.lock.md` section 1.1) are recorded in the lock, not here.

## Evidence

`evidence/` holds, for every run recorded, the transcript (`<tool>-<date>.log.txt`: commands, observed output, pass or fail), the exact procedure run (`<tool>-<date>.sh` or `.py`; a record of what was run, not a controlled tool) and every render inspected (`*.png`). The records cite these files by name. The 2026-09-26 files (`python-jsonschema-2026-09-26.*`, `python-tools-2026-09-26.*`) are the re-runs after review INSP-015 (`docs/reviews/SRR/checklists/tool-validation-tv-001-to-tv-010.md`).

## Common owner actions at SRR

1. Assign the independent review of TV-001 to TV-010 (CM plan section 9.2 step 3). No checklist template for TV records exists in `docs/templates/`; `docs/process/08-agent-briefing.md` section 3.5 holds a review without its checklist, so the checklist is written first (open item of the author's return).
2. After review, record in section 9 of each record either the proposed accreditation statement with its date or a refusal with the reason.
3. Authorize the commit of the tool validation set (SRR package section 2 item H17; INSP-015 finding-2). No record can yet name a commit that contains what it tested (CM plan section 9.2 step 1, "commit SHA tested"), so none can be accredited until this is done. The commit, made by Claude only after the owner's authorization, holds:
   - tools: `tools/traceability.py` (modified), `tools/render_review_figures.py` (untracked);
   - tests: `tools/tests/test_tools.py`, `test_traceability.py`, `test_validate_docs.py`, `test_render_deck.py` (modified), `test_git_known_answer.py`, `test_render_review_figures.py`, `test_traceability_srr_rules.py` (untracked);
   - fixtures: `tools/tests/fixtures/valid_project/` (modified and untracked files), `git/`, `schema/`, `review_figures/`, `kicad/`, `ltspice/`, `rust/`, `picotool/`, `openscad/` (untracked);
   - records and evidence: all of `docs/cm/tool-validation/`, and `tools/toolchain.lock.md`.

   After the commit, Claude re-runs `evidence/python-tools-2026-09-26.py` and `evidence/python-jsonschema-2026-09-26.sh` on it (every identity line must then read "unchanged from HEAD"), appends a result row naming the commit to section 4 of each record, updates the lock section 1.1 rows with the commit, and removes this action. Until then the results are bound to the file identities (git blob, SHA-256, fixture tree digest) that each record lists.
