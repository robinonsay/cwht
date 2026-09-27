# TV-024: Python static analyzer and coverage tool for the project tools (ruff, coverage.py)

| Field | Value |
|---|---|
| Record | TV-024 |
| Status | **Draft: selection made, tools not installed.** The download of both packages is an owner decision (section 9, action A-1); no known-answer run exists yet. Sections 3 and 7 are the plan the first run follows |
| Class | B, evidence-generating (static analysis and statement coverage of the class B Python tools; 03 section 6.5 item X9) |
| Governs | SWE-136, SWE-070 through CM plan section 9; SWE-135 and SWE-185 (static analysis) and SWE-189 (coverage) for the tool software, as 03 section 1 (tool rows "Static analysis and secure coding" and "Unit test, repeatability, coverage") plans them for PDR |
| Due | PDR (03 section 6.5 item X9: "Claude as software lead; PDR") |
| Lock rows | `tools/toolchain.lock.md` section 1 rows ruff and coverage.py (added 2026-09-27, "selected, not installed"); section 2 and `tools/requirements.txt` at installation |
| Work package | WP-PDR-08 |
| Author | Claude, software lead and tool owner |

## 1. Selection

**Need** (03 section 1 tool rows; 03 section 6.5 item X9): a pinned static analyzer that finds defects, insecure constructs and excess complexity in `tools/**/*.py` and the simulation checkers, and a pinned coverage tool that measures the statement coverage of each tool by its known-answer tests, both run by `tools/sw_gate.sh`. SWE-135 names four items for static analysis: defects, security, coverage and complexity (NPR 7150.2D section 4.4.4, SWEHB SWE-135 section 7.1).

| Criterion | ruff | pylint with bandit | pyflakes with mccabe | coverage.py | stdlib `trace` |
|---|---|---|---|---|---|
| SWE-135 defects | yes (`F` pyflakes rules, `B` bugbear, `E`/`W`) | yes | yes (fewer rules) | n/a | n/a |
| SWE-135 security | yes (`S`, the bandit rule set ported) | yes (bandit) | no | n/a | n/a |
| SWE-135 complexity | yes (`C901` mccabe, threshold configurable) | yes | yes (mccabe) | n/a | n/a |
| Statement and branch coverage | n/a | n/a | n/a | yes (`--branch`, `--fail-under`) | statements only, no branch data, no fail threshold |
| Install footprint | one package, no dependency (a native binary in the wheel) | two packages with seven or more dependencies (astroid, dill, isort, mccabe, platformdirs, tomlkit, and bandit's own) | two packages | one package, no required dependency | none (in the Accredited TV-001 interpreter) |
| Determinism for a known-answer test | fixed rule codes, `--no-cache`, `--isolated` | stable codes | stable codes | deterministic data file | deterministic |

**Selection:** ruff for static analysis and coverage.py for coverage. Ruff covers the three static SWE-135 items with one dependency-free package; coverage.py is the only candidate with branch data and a fail threshold. The stdlib `trace` module stays the fallback for coverage if the owner declines the download; there is no stdlib fallback for the analyzer, and then X9 stays open with the code peer review as the defect check (03 section 1 current text) and a residual stated in the PDR package.

This selection constrains later work (the gate and the tool code conventions), so it is recorded here, in the TV record that the lock and 03 item X9 name; the PDR work plan assigns no ADR for it. If the owner wants an ADR, the next free number is taken when it is written (06 section 13 item 3).

## 2. Purposes (proposed)

1. `ruff check` with the rule set of section 3 on `tools/**/*.py` (fixtures excluded) and `hardware/sim/**/*.py`: exit non-zero on any finding not suppressed by a line comment `# noqa: <code>` that states its reason (SWE-135 defects, security and complexity items; complexity limit 15, the value of SWE-220 used for the firmware).
2. `coverage run --branch` of each tool's known-answer test module and `coverage report` per tool file: statement and branch coverage of the tool code by its known-answer tests (03 section 1, "Planned for PDR").
3. Gate integration in `tools/sw_gate.sh` (planned step "G5 Python static analysis" and "G6 Python tool coverage"; section 7).

## 3. Known-answer test (planned)

**Fixtures** (committed with this record): `tools/tests/fixtures/python-analysis/` with `README.md`, `clean/clean_module.py` (a function at complexity 15, not reported), `seeded/undefined_name.py` (F821), `seeded/shell_true.py` (S602), `seeded/eval_use.py` (S307), `seeded/over_limit.py` (C901, complexity 16), `cov/calc.py` with `cov/test_calc.py` (every statement and both branch outcomes) and `cov/test_calc_gap.py` (seeded gap: line 7 and the True outcome of line 6 not executed), and `known-answers.json` holding the expected answers.

**Commands:**

```
.venv/bin/ruff check --no-cache --isolated --select E,W,F,B,S,C90 --line-length 120 \
    --config 'lint.mccabe.max-complexity = 15' --output-format concise tools/tests/fixtures/python-analysis/<path>
cd tools/tests/fixtures/python-analysis/cov && ../../../../../.venv/bin/coverage run --branch -m unittest <module> \
    && ../../../../../.venv/bin/coverage report --include=calc.py --show-missing --fail-under=100
```

**Pass criteria** (`known-answers.json`): `clean/` exit 0 with no finding; each seeded file exactly its one code and exit 1; `test_calc` 4 statements, 0 missing, 2 branches, 0 partial, 100 percent, exit 0; `test_calc_gap` line 7 missing, 1 partial branch, exit 2. Run twice; both runs identical. The expected values are confirmed or corrected by run 1 and then frozen.

## 4. Result

None. The tools are not installed (section 9 action A-1).

## 5. Reproducibility

Not required for class B; planned two runs as section 3 states.

## 6. Limitations (known before the first run)

1. The first gate run on `tools/**/*.py` will report findings in existing tools written without the analyzer. Each is fixed or suppressed with a reasoned `# noqa` in a commit that also re-runs the tool's known-answer tests (a tool change is a re-validation trigger of its own TV record, CM plan section 9.2 step 4). The count of findings at the first run is recorded here.
2. Coverage of the known-answer tests measures what those tests execute; it does not by itself show the tests are adequate. Proposed rule: the gate fails when the statement coverage of a class B tool file falls below the value recorded at its last TV run (a ratchet); the first values are recorded at run 1 and the owner may set a floor at PDR.
3. Ruff is a reimplementation of the pyflakes, pycodestyle, mccabe and bandit rules; its rule codes, not the original tools, are the reference.

## 7. Gate integration (planned, made in the commit that installs the tools)

Two steps in `tools/sw_gate.sh`, each `MISSING` (exit 3, incomplete) if its executable is absent from `.venv/bin/`:

```
step "G5 Python static analysis (ruff, TV-024)" "$ROOT/.venv/bin/ruff" check --no-cache \
    --config "$ROOT/tools/ruff.toml" "$ROOT/tools" "$ROOT/hardware/sim"
step "G6 Python tool coverage (coverage.py, TV-024)" "$PY" "$ROOT/tools/py_coverage_gate.py"
```

`tools/ruff.toml` holds the section 3 rule set and excludes `tools/tests/fixtures/`. The coverage step needs a small driver that runs each tool's known-answer module under coverage and applies the ratchet of limitation 2; it is a new class B tool and is validated in this record's run 1. `tools/sw_gate.sh` is also edited by WP-PDR-09 (G0 export mode, C-179) in wave 1; the two edits are separate commits in separate hunks.

## 8. Independent review (CM plan section 9.2 step 3)

Pending, after run 1. Record `docs/reviews/PDR/checklists/tool-validation-python-analysis.md` (PDR work plan WP-PDR-08), independent reviewer plus software assurance.

## 9. Owner actions and accreditation

| Action | Recommendation | Needed by |
|---|---|---|
| A-1: permit the download from PyPI of `ruff` and `coverage` into `.venv` (`.venv/bin/pip install ruff==<v> coverage==<v>`, where `<v>` is each package's current release on the day of the permission), pinned with `==` in `tools/requirements.txt` and recorded in lock sections 1, 2 and 7 | Permit. Without it, X9 stays open and the PDR package states the residual (section 1) | B0 or B1a (Mon 09-28 or Tue 09-29), so that run 1, the gate steps and the review fit before F1 |
| A-2: after section 8, accredit | Accredit on the record's recommendation | By B4 (OD-24 (b)) |

Proposed scope statement **ACC-PYANALYSIS-001**: "Accredited for purposes 1 to 3 for ruff `<v>` and coverage.py `<v>` in the TV-001 interpreter, with the rule set of `tools/ruff.toml`."

| Decision | Date | Recorded by |
|---|---|---|
| Pending (owner: A-1, then A-2) | | |
