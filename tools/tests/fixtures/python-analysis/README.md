# Python analysis known-answer fixtures (TV-024, 03 section 6.5 item X9)

Inputs for the known-answer test of the Python static analyzer and the Python coverage tool that
`docs/cm/tool-validation/TV-024-python-analysis.md` selects (ruff and coverage.py). The tools are
not installed on 2026-09-27: their download waits on the owner (TV-024 section 9), so the answers
in `known-answers.json` are the expected ones, confirmed or corrected by TV-024 run 1.

- `clean/`: modules with no finding under the TV-024 rule set; the analyzer must exit 0.
- `seeded/`: one seeded fault per file, each of which must be reported with exactly its code.
- `cov/`: `calc.py` and two test modules; `test_calc.py` executes every line and both outcomes
  of the one branch (100 percent), `test_calc_gap.py` omits the negative case (seeded gap).

These files are fixtures: they are excluded from the gate's own scan of `tools/**/*.py`.
