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
    usage errors     an unknown option and a --root that is not a directory; exit 2
                     with the argparse message on stderr (UsageErrorTests)
    record drift     temporary git repositories with one committed product and one
                     record: an APPROVED record equal to HEAD passes; drift, an absent
                     path or no named blob fails it; drift of a NEEDS CHANGES record is
                     a note; outside a git work tree top the rule is not applied
                     (RecordDriftTests, SRR package section 2.3, R13)
    record state     fixtures/record_state/: the record state rule that replaced the
                     open-Major line heuristic (SRR package item R18, readiness
                     finding R15-F2): an APPROVED record whose history names a Major
                     finding with the word Open, and whose latest iteration closes
                     it, passes; an APPROVED record with an open Major finding in its
                     latest iteration fails; an unshown findings_open count and a
                     reviewer_verdict below APPROVED fail; a later row supersedes an
                     earlier one; NEEDS CHANGES records are not held (RecordStateTests)

Run from the repository root:

    .venv/bin/python -m unittest discover -s tools/tests
"""
from __future__ import annotations

import io
import os
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
import validate_docs  # noqa: E402

FIXTURES = TOOLS / "tests" / "fixtures"
VALID = FIXTURES / "valid_project"
INVALID = FIXTURES / "invalid_project"
RECORD_STATE = FIXTURES / "record_state"
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


class UsageErrorTests(unittest.TestCase):
    """Purpose 5 of TV-003: exit 2 on a usage error, with no document validated (INSP-015 finding-5).

    Seeded faults: an unknown option, and a --root that is not a directory. Expected
    answers written from argparse's documented behavior (exit status 2, message on
    stderr) before the first run."""

    def assert_usage_error(self, result: subprocess.CompletedProcess[str], message: str) -> None:
        self.assertEqual(2, result.returncode, result.stdout + result.stderr)
        self.assertIn(message, result.stderr)
        self.assertNotIn("PASS", result.stdout)
        self.assertNotIn("FAIL", result.stdout)

    def test_unknown_option_exits_2(self) -> None:
        self.assert_usage_error(run_cli(VALID, "--bogus"), "unrecognized arguments: --bogus")

    def test_root_not_a_directory_exits_2(self) -> None:
        self.assert_usage_error(run_cli(VALID / "no-such-directory"), "root is not a directory")


RECORD_FRONT = """---
id: INSP-{n:03d}
checklist: peer-review-checklist-requirements
product: {product}
product_commit: "abcdef1"
{blobs}
verdict: {verdict}
author_agent: "author:fixture"
reviewer_agent: "reviewer:fixture"
iteration: 1
date: 2026-09-26
readiness_met: true
findings_major: 0
findings_minor: 0
findings_fixed: 0
findings_deferred: 0
effort_turns: 1
effort_minutes: 1
---
# Fixture record
"""


class RecordDriftTests(unittest.TestCase):
    """Purpose 6 of TV-003: record drift (SRR package section 2.3, R13).

    Each test builds a temporary git repository with one product file committed and one
    record, so HEAD blobs are known: the expected blob of the product is computed with
    `git hash-object` (TV-009), independently of the tool."""

    GIT_ENV = {"GIT_CONFIG_GLOBAL": "/dev/null", "GIT_CONFIG_NOSYSTEM": "1", "GIT_AUTHOR_NAME": "F", "GIT_AUTHOR_EMAIL": "f@example.invalid",
               "GIT_COMMITTER_NAME": "F", "GIT_COMMITTER_EMAIL": "f@example.invalid"}

    def git(self, root: Path, *args: str) -> str:
        return subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True, check=True, env=dict(os.environ, **self.GIT_ENV)).stdout.strip()

    def repo(self, tmp: str) -> tuple[Path, str]:
        root = Path(tmp) / "repo"
        (root / "docs/plan").mkdir(parents=True)
        (root / "docs/reviews/SRR/checklists").mkdir(parents=True)
        (root / "docs/plan/semp.md").write_text("reviewed text\n", encoding="utf-8")
        self.git(root, "init", "-q", "-b", "main")
        self.git(root, "add", "-A")
        self.git(root, "commit", "-q", "-m", "product")
        return root, self.git(root, "hash-object", "docs/plan/semp.md")

    def record(self, root: Path, verdict: str, blobs: str, n: int = 1) -> Path:
        path = root / "docs/reviews/SRR/checklists" / f"record-{n}.md"
        path.write_text(RECORD_FRONT.format(n=n, product="docs/plan/semp.md", blobs=blobs, verdict=verdict), encoding="utf-8")
        return path

    def result(self, root: Path, path: Path) -> validate_docs.FileResult:
        return relative(validate_docs.validate_all(root), root)[validate_docs.rel(path, root)]

    def test_approved_record_equal_to_head_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root, blob = self.repo(tmp)
            files = self.record(root, "APPROVED", f'product_files: ["docs/plan/semp.md@{blob}"]', 1)
            single = self.record(root, "APPROVED", f'product_blob: "{blob[:8]}"', 2)
            self.assertEqual(([], []), (self.result(root, files).errors, self.result(root, files).notes))
            self.assertEqual([], self.result(root, single).errors)

    def test_approved_record_with_drift_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root, blob = self.repo(tmp)
            path = self.record(root, "APPROVED", f'product_files: ["docs/plan/semp.md@{blob}", "docs/plan/absent.md@{blob}"]')
            (root / "docs/plan/semp.md").write_text("edited after the approval\n", encoding="utf-8")
            self.git(root, "commit", "-q", "-am", "edit")
            head = self.git(root, "rev-parse", "HEAD:docs/plan/semp.md")
            errors = self.result(root, path).errors
        self.assertEqual(2, len(errors), errors)
        self.assertTrue(errors[0].startswith(f"product_files: docs/plan/semp.md@{blob[:8]} differs from HEAD blob {head[:8]}"), errors[0])
        self.assertTrue(errors[1].startswith(f"product_files: docs/plan/absent.md@{blob[:8]} is not in HEAD"), errors[1])
        self.assertIn("R13", errors[0])

    def test_approved_record_without_blobs_fails_and_needs_changes_drift_is_a_note(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root, blob = self.repo(tmp)
            bare = self.record(root, "APPROVED", "", 1)
            open_record = self.record(root, "NEEDS CHANGES", 'product_files: ["docs/plan/semp.md@1234567"]', 2)
            bare_result, open_result = self.result(root, bare), self.result(root, open_record)
            printed = io.StringIO()
            with redirect_stdout(printed):
                validate_docs.print_results([open_result], root, quiet=False)
        self.assertEqual(1, len(bare_result.errors))
        self.assertIn("names no reviewed blob", bare_result.errors[0])
        self.assertEqual([], open_result.errors)
        self.assertEqual([f"record drift: product_files: docs/plan/semp.md@1234567 differs from HEAD blob {blob[:8]} (the committed product is not the reviewed one)"], open_result.notes)
        self.assertIn("      note: record drift:", printed.getvalue())

    def test_malformed_product_files_entry_fails_the_schema(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root, _ = self.repo(tmp)
            path = self.record(root, "NEEDS CHANGES", 'product_files: ["docs/plan/semp.md"]')
            errors = self.result(root, path).errors
        self.assertEqual(1, len(errors), errors)
        self.assertIn("product_files", errors[0])

    def test_rule_not_applied_outside_a_git_work_tree_top(self) -> None:
        results = relative(validate_docs.validate_all(VALID), VALID)
        record = results["docs/reviews/SRR/checklists/requirements-sys.md"]
        self.assertEqual([], record.errors)
        self.assertTrue(record.notes and record.notes[0].startswith("record drift rule not applied:"), record.notes)


class RecordStateTests(unittest.TestCase):
    """Known answers of the record state rule (module docstring of validate_docs.py; SRR package item R18)."""

    CHECKLISTS = "docs/reviews/SRR/checklists/"
    EXPECTED_FAILURES = {
        "approved-latest-open-major.md": ("finding-3 is a Major finding in state Open in the latest iteration's finding table",),
        "approved-open-count-unshown.md": ("findings_open is 1 and the latest iteration's finding tables show 0 open Minor finding(s)",),
        "approved-reviewer-needs-changes.md": ("reviewer_verdict is 'NEEDS CHANGES'",),
    }
    EXPECTED_PASSES = (
        "approved-historical-lines.md",
        "approved-open-minor.md",
        "approved-superseded-row.md",
        "needs-changes-open-major.md",
    )

    @classmethod
    def setUpClass(cls) -> None:
        cls.results = relative(validate_docs.validate_all(RECORD_STATE), RECORD_STATE)

    def body(self, name: str) -> str:
        text = (RECORD_STATE / self.CHECKLISTS / name).read_text(encoding="utf-8")
        return validate_docs.body_after_front_matter(text)

    def test_exactly_the_seeded_records_fail(self) -> None:
        failed = {path.removeprefix(self.CHECKLISTS) for path, result in self.results.items() if not result.passed}
        self.assertEqual(set(self.EXPECTED_FAILURES), failed)
        self.assertEqual(7, len(self.results))

    def test_approved_record_with_historical_major_open_lines_passes(self) -> None:
        """Historical count lines and earlier tables name finding-1 with Major and Open; the latest iteration closes it."""
        result = self.results[self.CHECKLISTS + "approved-historical-lines.md"]
        self.assertEqual([], result.errors)
        body = self.body("approved-historical-lines.md")
        heuristic_hits = [line for line in body.splitlines() if "finding-1" in line and " Major" in line and "Open" in line]
        self.assertGreaterEqual(len(heuristic_hits), 5, "the fixture carries the lines the replaced heuristic misread")
        self.assertEqual([], validate_docs.open_major_findings(body))
        current = validate_docs.current_findings(body)
        self.assertEqual({"finding-1", "finding-2"}, set(current))
        self.assertFalse(current["finding-1"].is_open)
        self.assertEqual("Major", current["finding-1"].severity)

    def test_approved_record_with_open_major_in_latest_iteration_fails(self) -> None:
        errors = self.results[self.CHECKLISTS + "approved-latest-open-major.md"].errors
        self.assertTrue(any("finding-3 is a Major finding in state Open" in e for e in errors), errors)
        self.assertEqual(["finding-3"], validate_docs.open_major_findings(self.body("approved-latest-open-major.md")))

    def test_seeded_failure_messages(self) -> None:
        for name, fragments in self.EXPECTED_FAILURES.items():
            errors = self.results[self.CHECKLISTS + name].errors
            for fragment in fragments:
                self.assertTrue(any(fragment in e for e in errors), (name, fragment, errors))

    def test_expected_passes(self) -> None:
        for name in self.EXPECTED_PASSES:
            self.assertEqual([], self.results[self.CHECKLISTS + name].errors, name)

    def test_later_row_supersedes_and_needs_changes_is_not_held(self) -> None:
        self.assertEqual([], validate_docs.open_major_findings(self.body("approved-superseded-row.md")))
        self.assertEqual(["finding-1"], validate_docs.open_major_findings(self.body("needs-changes-open-major.md")))

    def test_latest_iteration_section_bounds(self) -> None:
        body = "# R\n| Finding | Severity | State |\n|---|---|---|\n| finding-1 | Major | Open |\n"
        self.assertEqual(["finding-1"], validate_docs.open_major_findings(body), "no iteration heading: the whole body is read")
        body += (
            "## Iteration 2 (date)\n| Finding | Severity | Disposition |\n|---|---|---|\n| finding-1 | Major | Closed |\n"
            "### Closure as written at iteration 1\n| Finding | Severity | State |\n|---|---|---|\n| finding-1 | Major | Open |\n"
            "## Re-issue\n```\n| Finding | Severity | State |\n|---|---|---|\n| finding-1 | Major | Open |\n```\n"
        )
        self.assertEqual([], validate_docs.open_major_findings(body), "earlier-iteration blocks and fenced blocks are not read")
        section = validate_docs.latest_iteration_section(body)
        self.assertTrue(section.startswith("## Iteration 2"))
        self.assertNotIn("as written at iteration 1", section)
        self.assertIn("## Re-issue", section)

    def test_cell_reading(self) -> None:
        table = "| Finding | Iteration 1 severity | Result |\n|---|---|---|\n"
        rows = validate_docs.finding_rows(
            table
            + "| <a id=\"finding-4\"></a>F-04 (finding-4) | **Major** | **Open**, owner ruling needed |\n"
            + "| finding-5 | Major | Closed (was Open) |\n"
            + "| finding-6 | Minor (was Major) | Open |\n"
            + "| note | Major | Open |\n"
        )
        self.assertEqual([("F-04", "Major", True), ("finding-5", "Major", False), ("finding-6", "Minor", True)], [(r.finding, r.severity, r.is_open) for r in rows])
        self.assertEqual([], validate_docs.finding_rows("| # | Criterion | Answer |\n|---|---|---|\n| finding-1 | Major | Open |\n"), "not a finding table")


class RepositoryTests(unittest.TestCase):
    """Every JSON document of the repository validates (entrance product of every review)."""

    def test_repository_exit_zero(self) -> None:
        result = run_cli(validate_docs.REPO_ROOT)
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
