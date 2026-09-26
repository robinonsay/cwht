"""Known-answer tests for tools/validate_docs.py (SWE-136 tool validation).

    valid_project    every conventional document validates, including an SRR
                     RFA/RID log whose verification record is the filled checklist
                     docs/reviews/SRR/checklists/requirements-sys.md (charter
                     section 5 as amended 2026-09-25); exit 0
    invalid_project  a requirements file missing 'rationale', an id that violates
                     the schema pattern, a risk register and a hazard list without
                     their schemas, a template example without a schema, an SRR log
                     filed under docs/reviews/PDR/ with a missing verification
                     record, peer-review records with bad front matter, a reused
                     INSP id, a record under a non-review folder, and a forbidden
                     peer-reviews/ folder; exit 1

Run from the repository root:

    .venv/bin/python -m unittest discover -s tools/tests
"""
from __future__ import annotations

import io
import subprocess
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
import validate_docs  # noqa: E402

FIXTURES = TOOLS / "tests" / "fixtures"
VALID = FIXTURES / "valid_project"
INVALID = FIXTURES / "invalid_project"
TOOL = TOOLS / "validate_docs.py"

EXPECTED_INVALID_FAILURES = {
    "docs/requirements/rx/requirements.json",
    "docs/requirements/sys/requirements.json",
    "docs/reviews/PDR/rfa-rid-log.json",
    "docs/reviews/QDR/checklists/notes.md",
    "docs/reviews/SRR/checklists/requirements-sys.md",
    "docs/reviews/SRR/checklists/requirements-tx.md",
    "docs/reviews/SRR/peer-reviews",
    "docs/risk/register.json",
    "docs/safety/hazards.json",
    "docs/templates/broken.example.json",
}


def run_cli(root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(TOOL), "--root", str(root), *args], capture_output=True, text=True, check=False)


def relative(results: list[validate_docs.FileResult], root: Path) -> dict[str, validate_docs.FileResult]:
    return {validate_docs.rel(r.document, root): r for r in results}


class ValidProjectTests(unittest.TestCase):
    def test_every_document_passes(self) -> None:
        results = validate_docs.validate_all(VALID)
        self.assertTrue(results, "no documents discovered")
        self.assertEqual([], [f"{validate_docs.rel(r.document, VALID)}: {r.errors}" for r in results if not r.passed])

    def test_conventions_discovered(self) -> None:
        found = relative(validate_docs.validate_all(VALID), VALID)
        for path in (
            "docs/requirements/sys/requirements.json",
            "docs/requirements/sw/sw-keyer/requirements.json",
            "docs/requirements/l0-stakeholder/expectations.json",
            "docs/test_cases/sys/test_cases.json",
            "docs/risk/register.json",
            "docs/safety/hazards.json",
            "docs/process/rmm.json",
            "docs/reviews/SRR/rfa-rid-log.json",
            "docs/templates/requirements.example.json",
            "docs/templates/rfa-rid-log.example.json",
        ):
            self.assertIn(path, found)

    def test_cli_exit_zero(self) -> None:
        result = run_cli(VALID)
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("0 failed", result.stdout)

    def test_run_returns_zero_and_quiet_prints_nothing(self) -> None:
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            status = validate_docs.run(VALID, quiet=True)
        self.assertEqual(0, status)
        self.assertEqual("", buffer.getvalue())


class InvalidProjectTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.results = relative(validate_docs.validate_all(INVALID), INVALID)

    def test_cli_exit_one(self) -> None:
        result = run_cli(INVALID)
        self.assertEqual(1, result.returncode, result.stdout + result.stderr)

    def test_exactly_the_seeded_documents_fail(self) -> None:
        failed = {path for path, r in self.results.items() if not r.passed}
        self.assertEqual(EXPECTED_INVALID_FAILURES, failed)

    def test_missing_required_property(self) -> None:
        errors = self.results["docs/requirements/rx/requirements.json"].errors
        self.assertTrue(any("'rationale' is a required property" in e for e in errors), errors)

    def test_id_pattern_violation(self) -> None:
        errors = self.results["docs/requirements/sys/requirements.json"].errors
        self.assertTrue(any("REQ-sys-004" in e and "does not match" in e for e in errors), errors)

    def test_document_without_schema_is_a_failure(self) -> None:
        for path in ("docs/risk/register.json", "docs/safety/hazards.json", "docs/templates/broken.example.json"):
            errors = self.results[path].errors
            self.assertTrue(any(e.startswith("schema not found") for e in errors), errors)

    def test_schema_valid_files_still_pass(self) -> None:
        self.assertTrue(self.results["docs/requirements/tx/requirements.json"].passed)
        self.assertTrue(self.results["docs/test_cases/sys/test_cases.json"].passed)


class PeerReviewRecordTests(unittest.TestCase):
    """Charter section 5 (amended 2026-09-25): the filled checklist is the single peer-review record."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.valid = relative(validate_docs.validate_all(VALID), VALID)
        cls.invalid = relative(validate_docs.validate_all(INVALID), INVALID)

    def test_checklist_record_path_is_accepted_by_the_log_schema(self) -> None:
        log = self.valid["docs/reviews/SRR/rfa-rid-log.json"]
        self.assertTrue(log.passed, log.errors)
        record = self.valid["docs/reviews/SRR/checklists/requirements-sys.md"]
        self.assertTrue(record.passed, record.errors)
        self.assertEqual(validate_docs.PEER_REVIEW_RECORD_LABEL, record.schema_label)

    def test_repository_schema_pattern_names_checklists(self) -> None:
        schema = validate_docs.load_json(validate_docs.REPO_ROOT / "docs/templates/rfa-rid-log.schema.json")[0]
        pattern = schema["definitions"]["verification"]["properties"]["record"]["pattern"]
        self.assertIn("/checklists/", pattern)
        self.assertNotIn("peer-reviews", pattern)

    def test_old_peer_reviews_path_is_rejected_by_the_schema(self) -> None:
        import json
        import tempfile

        data = validate_docs.load_json(VALID / "docs/reviews/SRR/rfa-rid-log.json")[0]
        data["items"][0]["verification"]["record"] = "docs/reviews/SRR/peer-reviews/INSP-001.md"
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "rfa-rid-log.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            result = validate_docs.validate_document(path, VALID / "docs/templates/rfa-rid-log.schema.json")
        self.assertTrue(any("verification.record" in e and "does not match" in e for e in result.errors), result.errors)

    def test_log_folder_and_record_existence(self) -> None:
        errors = self.invalid["docs/reviews/PDR/rfa-rid-log.json"].errors
        self.assertTrue(any("review: 'SRR' but the log is in docs/reviews/PDR/" in e for e in errors), errors)
        self.assertTrue(any("missing-record.md' does not exist" in e for e in errors), errors)
        self.assertEqual(2, len(errors), "the log is otherwise schema-valid")

    def test_record_front_matter_rules(self) -> None:
        errors = self.invalid["docs/reviews/SRR/checklists/requirements-sys.md"].errors
        for fragment in ("'INSP-1' does not match", "product_commit: 0 is not of type 'string'", "'OK' is not one of", "checklist_file:"):
            self.assertTrue(any(fragment in e for e in errors), (fragment, errors))

    def test_record_ids_are_unique(self) -> None:
        self.assertTrue(self.invalid["docs/reviews/SRR/checklists/requirements-rx.md"].passed, "the first holder of INSP-002 passes")
        errors = self.invalid["docs/reviews/SRR/checklists/requirements-tx.md"].errors
        self.assertEqual(["id: INSP-002 already used by docs/reviews/SRR/checklists/requirements-rx.md (ids are never reused, charter section 6)"], errors)

    def test_non_review_folder_and_missing_front_matter(self) -> None:
        errors = self.invalid["docs/reviews/QDR/checklists/notes.md"].errors
        self.assertTrue(any("'QDR' is not a review token" in e for e in errors), errors)
        self.assertTrue(any("no YAML front matter" in e for e in errors), errors)

    def test_peer_reviews_folder_is_forbidden(self) -> None:
        errors = self.invalid["docs/reviews/SRR/peer-reviews"].errors
        self.assertEqual(1, len(errors))
        self.assertIn("no peer-reviews/ folder", errors[0])


class RepositoryTests(unittest.TestCase):
    """Every JSON document of the repository validates (entrance product of every review)."""

    def test_repository_exit_zero(self) -> None:
        result = run_cli(validate_docs.REPO_ROOT)
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
