"""Known-answer tests for tools/render_compliance.py (SWE-136 tool validation; 05 section 9 class B).

Fixtures under tools/tests/fixtures/compliance/:

    appendix-h.md      Verbatim Table H-1 lines of the corpus with the conversion quirks the
                       parser must handle (rows without a leading pipe, two rows on one line,
                       'b< (1)' paragraph reference, 'SE- 62' id) and a decoy row before the
                       caption; 10 rows: SE-07, SE-24, SE-31, SE-32, SE-33, SE-34, SE-38,
                       SE-44, SE-51, SE-62
    valid.json         a matrix over those rows that passes every check
    valid.md           its stored render
    stale.md           the stored render with one cell changed
    <fault>.json       valid.json with exactly one seeded fault each

The schema under test is the project schema docs/process/se-compliance-matrix.schema.json.
Each seeded fault must produce exactly its expected error string and nothing else.

Run from the repository root:

    .venv/bin/python -m unittest discover -s tools/tests
"""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
REPO = TOOLS.parent
sys.path.insert(0, str(TOOLS))
import render_compliance  # noqa: E402

FX = TOOLS / "tests" / "fixtures" / "compliance"
CORPUS = FX / "appendix-h.md"
SCHEMA = REPO / "docs" / "process" / "se-compliance-matrix.schema.json"
TOOL = TOOLS / "render_compliance.py"


def load(name: str) -> dict:
    return json.loads((FX / name).read_text(encoding="utf-8"))


def errors_of(name: str) -> list[str]:
    schema = render_compliance.load_schema(SCHEMA)
    table = render_compliance.parse_table_h1(CORPUS)
    return render_compliance.validate(load(name), schema, table)


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(TOOL), "--schema", str(SCHEMA), *args],
        capture_output=True,
        text=True,
        check=False,
    )


class CorpusParseTests(unittest.TestCase):
    def test_rows_and_order(self) -> None:
        table = render_compliance.parse_table_h1(CORPUS)
        self.assertEqual(
            ["SE-07", "SE-24", "SE-31", "SE-32", "SE-33", "SE-34", "SE-38", "SE-44", "SE-51", "SE-62"],
            list(table),
        )

    def test_quirks(self) -> None:
        table = render_compliance.parse_table_h1(CORPUS)
        self.assertEqual("5.2.2.2. b< (1)", table["SE-38"]["section"])
        self.assertEqual("6.2.8. a", table["SE-62"]["section"])
        self.assertTrue(table["SE-34"]["statement"].startswith("The technical team shall participate in the development"))
        self.assertIn('"Not Applicable"', table["SE-44"]["rationale"])

    def test_section_normalization(self) -> None:
        self.assertEqual("5.2.2.2.b(1)", render_compliance.normalize_section("5.2.2.2. b< (1)"))

    def test_real_corpus_has_62_rows(self) -> None:
        table = render_compliance.parse_table_h1(render_compliance.DEFAULT_CORPUS)
        self.assertEqual(62, len(table))
        self.assertEqual("SE-07", next(iter(table)))

    def test_missing_caption_raises(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "no-table.md"
            path.write_text("| SE-07 | 3.2.2.1 | text | rationale |  |  |\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                render_compliance.parse_table_h1(path)


class ValidFixtureTests(unittest.TestCase):
    def test_no_errors(self) -> None:
        self.assertEqual([], errors_of("valid.json"))

    def test_render_matches_stored(self) -> None:
        table = render_compliance.parse_table_h1(CORPUS)
        self.assertEqual(
            (FX / "valid.md").read_text(encoding="utf-8"),
            render_compliance.render(load("valid.json"), [], len(table)),
        )

    def test_render_has_six_h11_columns_and_revision_date(self) -> None:
        text = (FX / "valid.md").read_text(encoding="utf-8")
        self.assertIn(
            "| Req ID | NPR Section | Requirement Statement | Rationale | Comply? | Justification | Implementation reference |",
            text,
        )
        self.assertIn("- **Revision date:** 2026-09-25", text)
        self.assertIn("| SE-51 | deviation |", text)

    def test_cli_render_writes_stored_file(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "matrix.md"
            result = run_cli("--json", str(FX / "valid.json"), "--corpus", str(CORPUS), "--out", str(out))
            self.assertEqual(0, result.returncode, result.stdout + result.stderr)
            self.assertEqual((FX / "valid.md").read_text(encoding="utf-8"), out.read_text(encoding="utf-8"))

    def test_cli_check_current(self) -> None:
        result = run_cli("--json", str(FX / "valid.json"), "--corpus", str(CORPUS), "--out", str(FX / "valid.md"), "--check")
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("rows=10 corpus=10 FC=6 T=1 NA=3", result.stdout)
        self.assertIn("T ['SE-51']", result.stdout)
        self.assertIn("rendered file is current", result.stdout)

    def test_cli_check_detects_stale_render(self) -> None:
        result = run_cli("--json", str(FX / "valid.json"), "--corpus", str(CORPUS), "--out", str(FX / "stale.md"), "--check")
        self.assertEqual(1, result.returncode, result.stdout + result.stderr)
        self.assertIn(render_compliance.STALE_MESSAGE, result.stderr)

    def test_cli_empty_corpus_skips_cross_check(self) -> None:
        # A matrix whose row set does not match the fixture corpus still passes when the corpus is skipped.
        result = run_cli("--json", str(FX / "missing-row.json"), "--corpus", "", "--out", str(FX / "valid.md"), "--check")
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("corpus=skipped", result.stdout)
        self.assertIn("stale check skipped: no corpus", result.stdout)

    def test_cli_no_corpus_flag(self) -> None:
        result = run_cli("--json", str(FX / "valid.json"), "--no-corpus", "--out", str(FX / "valid.md"), "--check")
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("corpus=skipped", result.stdout)

    def test_cli_empty_corpus_still_validates_schema(self) -> None:
        result = run_cli("--json", str(FX / "t-without-relief.json"), "--corpus", "", "--out", str(FX / "valid.md"), "--check")
        self.assertEqual(1, result.returncode, result.stdout + result.stderr)
        self.assertIn("'relief_type' is a required property", result.stderr)


class SeededFaultTests(unittest.TestCase):
    """One fixture per seeded fault; the error list is exactly the expected string."""

    def test_missing_row(self) -> None:
        self.assertEqual(["ids in corpus Table H-1 but not in matrix: ['SE-34']"], errors_of("missing-row.json"))

    def test_unknown_id(self) -> None:
        self.assertEqual(["ids in matrix but not in corpus Table H-1: ['SE-98']"], errors_of("unknown-id.json"))

    def test_empty_t_justification(self) -> None:
        self.assertEqual(["schema: rows/8/justification (SE-51): '' is too short"], errors_of("empty-t-justification.json"))

    def test_altered_statement(self) -> None:
        self.assertEqual(
            ["SE-07: requirement_statement is not the verbatim Table H-1 statement"], errors_of("altered-statement.json")
        )

    def test_altered_rationale(self) -> None:
        self.assertEqual(["SE-44: rationale is not the verbatim Table H-1 rationale"], errors_of("altered-rationale.json"))

    def test_wrong_section(self) -> None:
        self.assertEqual(["SE-24: npr_section '4.2.2' differs from Table H-1 '4.2.1'"], errors_of("wrong-section.json"))

    def test_t_row_without_relief_type(self) -> None:
        self.assertEqual(["schema: rows/8 (SE-51): 'relief_type' is a required property"], errors_of("t-without-relief.json"))

    def test_relief_type_on_fc_row(self) -> None:
        self.assertEqual(["schema: rows/0 (SE-07): False schema does not allow 'deviation'"], errors_of("relief-on-fc.json"))

    def test_required_disposition(self) -> None:
        self.assertEqual(
            ["SE-44: comply 'FC' but charter section 12 (App. G guidance row) fixes 'NA'"],
            errors_of("required-disposition.json"),
        )

    def test_row_order(self) -> None:
        self.assertEqual(
            ["row order differs from Table H-1 at row 0: matrix has SE-24, Table H-1 has SE-07"], errors_of("order.json")
        )

    def test_duplicate_id(self) -> None:
        self.assertEqual(["row 10 (SE-07): duplicate se_id"], errors_of("duplicate-id.json"))

    def test_cli_exit_one_on_fault(self) -> None:
        result = run_cli("--json", str(FX / "wrong-section.json"), "--corpus", str(CORPUS), "--out", str(FX / "valid.md"), "--check")
        self.assertEqual(1, result.returncode)
        self.assertIn("compliance matrix check FAILED", result.stderr)
        self.assertIn("SE-24: npr_section '4.2.2' differs from Table H-1 '4.2.1'", result.stderr)


class ProjectMatrixTests(unittest.TestCase):
    """The committed matrix passes and its render is current (the SRR entrance check)."""

    def test_project_matrix_check(self) -> None:
        result = subprocess.run([sys.executable, str(TOOL), "--check"], capture_output=True, text=True, check=False)
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("rows=62 corpus=62", result.stdout)


if __name__ == "__main__":
    unittest.main()
