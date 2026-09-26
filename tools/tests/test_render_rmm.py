"""Known-answer tests for tools/render_rmm.py (SWE-136 tool validation; 05 section 9 class B).

Fixtures under tools/tests/fixtures/rmm/:

    appendix-c.md          App. C Table 2 excerpt: three Class A rows (SWE-020, SWE-023,
                           SWE-141) and one row without an X in Class A (SWE-042)
    chapters/              chapter excerpts whose [SWE-NNN] tags equal the Class A set
    chapters-mismatch/     the same plus an extra [SWE-042] tag
    repo/                  fixture repository root for the status rule
                           (docs/process/existing.md exists, nothing else)
    valid.json, valid.md   a matrix that passes every check and its stored render
    stale.md               the stored render with one cell changed
    <fault>.json           valid.json with exactly one seeded fault each

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
sys.path.insert(0, str(TOOLS))
import render_rmm  # noqa: E402

FX = TOOLS / "tests" / "fixtures" / "rmm"
CORPUS = FX / "appendix-c.md"
CHAPTERS = FX / "chapters"
CHAPTERS_MISMATCH = FX / "chapters-mismatch"
REPO_ROOT = FX / "repo"
TOOL = TOOLS / "render_rmm.py"


def load(name: str) -> dict:
    return json.loads((FX / name).read_text(encoding="utf-8"))


def errors_of(name: str, chapters: Path = CHAPTERS) -> list[str]:
    return render_rmm.check(load(name), CORPUS, chapters, REPO_ROOT)


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(TOOL), "--corpus", str(CORPUS), "--chapters", str(CHAPTERS), "--repo", str(REPO_ROOT), *args],
        capture_output=True,
        text=True,
        check=False,
    )


class CorpusParseTests(unittest.TestCase):
    def test_table_parse(self) -> None:
        table = render_rmm.parse_table(CORPUS)
        self.assertEqual(["SWE-020", "SWE-023", "SWE-141", "SWE-042"], list(table))
        self.assertEqual({"A", "B", "C", "D", "E"}, table["SWE-020"]["classes"])
        self.assertEqual({"B", "C"}, table["SWE-042"]["classes"])
        self.assertEqual("HQ OSMA", table["SWE-141"]["authority"])

    def test_class_a_set(self) -> None:
        self.assertEqual({"SWE-020", "SWE-023", "SWE-141"}, render_rmm.parse_class_a_set(CORPUS))

    def test_chapter_tags(self) -> None:
        self.assertEqual({"SWE-020", "SWE-023", "SWE-141"}, render_rmm.parse_chapter_tags(CHAPTERS))
        self.assertEqual({"SWE-020", "SWE-023", "SWE-141", "SWE-042"}, render_rmm.parse_chapter_tags(CHAPTERS_MISMATCH))

    def test_named_paths_skip_placeholders(self) -> None:
        text = ("see docs/process/existing.md, docs/reviews/<REVIEW>/package.md, docs/vv/ncr/NCR-NNN.md, "
                "tools/tests/**, firmware/releases/VDD-vX.Y.Z.md and docs/vv/reports/TC-SW-COV-001-r<N>.md.")
        self.assertEqual(["docs/process/existing.md"], render_rmm.named_paths(text))


class ValidFixtureTests(unittest.TestCase):
    def test_no_errors(self) -> None:
        self.assertEqual([], errors_of("valid.json"))

    def test_render_matches_stored(self) -> None:
        rendered = render_rmm.render(load("valid.json"))
        self.assertEqual((FX / "valid.md").read_text(encoding="utf-8"), rendered + "\n")
        # App. C.2 content of the rendered matrix: Table 2 authority per row (c.2.d) and the
        # verbatim requirement statement (c.2.c), including an HQ authority row.
        self.assertIn("| NPR § | SWE | Short title | NPR authority |", rendered)
        self.assertIn("| 3.6.2 | SWE-141 | IV&V on Category 1 and 2 projects | HQ OSMA |", rendered)
        self.assertIn("| SWE-141 | NA | IV&V on Category 1 and 2 projects | HQ OSMA |", rendered)
        self.assertIn("- **SWE-020** (3.5.1): The project manager shall classify each system", rendered)
        self.assertIn(render_rmm.AUTHORITY, rendered)

    def test_cli_check_exit_zero_and_lists_ids(self) -> None:
        result = run_cli("--rmm", str(FX / "valid.json"), "--out", str(FX / "valid.md"), "--check")
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("FC=1, T=1, NA=1", result.stdout)
        self.assertIn("In place=2 [SWE-020, SWE-141]", result.stdout)
        self.assertIn("T [SWE-023]", result.stdout)
        self.assertIn("NA [SWE-141]", result.stdout)
        self.assertIn("is current", result.stdout)

    def test_cli_render_writes_stored_file(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "rmm.md"
            result = run_cli("--rmm", str(FX / "valid.json"), "--out", str(out))
            self.assertEqual(0, result.returncode, result.stdout + result.stderr)
            self.assertEqual((FX / "valid.md").read_text(encoding="utf-8"), out.read_text(encoding="utf-8"))

    def test_cli_check_detects_stale_render(self) -> None:
        result = run_cli("--rmm", str(FX / "valid.json"), "--out", str(FX / "stale.md"), "--check")
        self.assertEqual(1, result.returncode, result.stdout + result.stderr)
        self.assertIn(render_rmm.STALE_MESSAGE, result.stderr)

    def test_no_corpus_and_no_status_flags(self) -> None:
        errors = render_rmm.check(load("status-planned-no-label.json"), None, None, None)
        self.assertEqual([], errors)


class SeededFaultTests(unittest.TestCase):
    """One fixture per seeded fault; the error list is exactly the expected string."""

    def test_missing_class_a_row(self) -> None:
        self.assertEqual(["Class A rows in App. C but not in rmm.json: ['SWE-141']"], errors_of("missing-row.json"))

    def test_extra_row(self) -> None:
        self.assertEqual(["rows in rmm.json that are not Class A rows of App. C: ['SWE-042']"], errors_of("extra-row.json"))

    def test_altered_requirement_text(self) -> None:
        self.assertEqual(
            ["SWE-023: requirement_text is not the verbatim Table 2 statement (whitespace-normalized comparison)"],
            errors_of("altered-text.json"),
        )

    def test_wrong_npr_section(self) -> None:
        self.assertEqual(["SWE-020: npr_section '3.5.2' differs from Table 2 section '3.5.1'"], errors_of("wrong-section.json"))

    def test_fc_row_with_rationale(self) -> None:
        self.assertEqual(["row 0 (SWE-020): FC row must have tailoring_rationale null"], errors_of("fc-with-rationale.json"))

    def test_t_row_with_short_residual_risk(self) -> None:
        self.assertEqual(["row 1 (SWE-023): T/NA row needs a residual_risk of at least 20 characters"], errors_of("t-short-residual.json"))

    def test_in_place_row_naming_absent_path(self) -> None:
        self.assertEqual(
            ["SWE-020: status 'In place' but named path does not exist: ['docs/process/absent.md'] "
             "(label the future item 'Planned for <gate>' or set status Planned)"],
            errors_of("status-in-place-missing.json"),
        )

    def test_planned_row_without_label(self) -> None:
        self.assertEqual(
            ["SWE-023: status 'Planned' but every named path exists and no 'Planned for <gate>' names the future "
             "artifact or execution (set status In place or add the label)"],
            errors_of("status-planned-no-label.json"),
        )

    def test_chapter_tag_mismatch(self) -> None:
        self.assertEqual(
            ["[SWE-NNN] tags in chapters 3 to 5 without a Class A row in App. C: ['SWE-042']"],
            errors_of("valid.json", CHAPTERS_MISMATCH),
        )

    def test_cli_exit_one_on_fault(self) -> None:
        result = run_cli("--rmm", str(FX / "wrong-section.json"), "--out", str(FX / "valid.md"), "--check")
        self.assertEqual(1, result.returncode)
        self.assertIn("rmm.json check FAILED", result.stderr)
        self.assertIn("SWE-020: npr_section '3.5.2' differs from Table 2 section '3.5.1'", result.stderr)


if __name__ == "__main__":
    unittest.main()
