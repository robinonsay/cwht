"""Known-answer tests for tools/review_trend.py (SWE-136 tool validation).

The known answers are the hand-computed values of
docs/process/01-lifecycle-and-reviews.md section 11 for
docs/templates/rfa-rid-log.example.json at T = 2026-10-12 with the SRR memo
signed 2026-10-05 and no later memo. The fixture tools/tests/fixtures/review_trend
holds a verbatim copy of that example as docs/reviews/SRR/rfa-rid-log.json, the
signed SRR memo, the peer-review record the log names, and a minimal
docs/plan/tpm.json carrying the review-trend TPM (TPM-003); --write runs on a
temporary copy so the fixture never changes.

Run from the repository root:

    .venv/bin/python -m unittest discover -s tools/tests
"""
from __future__ import annotations

import datetime as dt
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
import review_trend  # noqa: E402

FIXTURE = TOOLS / "tests" / "fixtures" / "review_trend"
TEMPLATE = review_trend.REPO_ROOT / "docs" / "templates" / "rfa-rid-log.example.json"
TOOL = TOOLS / "review_trend.py"
T = dt.date(2026, 10, 12)
MEMOS = {"SRR": dt.date(2026, 10, 5)}

# 01 section 11 known-answer table: (type, severity) -> raised, open, verified_pending, closed, withdrawn, overdue
KNOWN_ROWS = {
    ("RID", "all"): (3, 1, 0, 1, 1, 0),
    ("RID", "Major"): (1, 0, 0, 1, 0, 0),
    ("RID", "Minor"): (2, 1, 0, 0, 1, 0),
    ("RFA", "all"): (2, 1, 0, 1, 0, 0),
    ("RFA", "Blocking"): (1, 0, 0, 1, 0, 0),
    ("RFA", "Routine"): (1, 1, 0, 0, 0, 0),
}
MEASURES = ("raised", "open", "verified_pending", "closed", "withdrawn", "overdue")


def run_cli(root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(TOOL), "--root", str(root), *args], capture_output=True, text=True, check=False)


def item(ident: str, severity: str, state: str, opened: str = "2026-10-03", due_review: str | None = None, due_date: str | None = None, history: list[tuple[str, str]] | None = None) -> review_trend.Item:
    kind = ident.split("-")[0]
    steps = [review_trend.Transition(dt.date.fromisoformat(d), to) for d, to in (history or [(opened, "Open")] + ([] if state == "Open" else [(opened, state)]))]
    closed = next((s.date for s in steps if s.to in ("Closed", "Withdrawn")), None)
    return review_trend.Item(ident, kind, severity, ident.split("-")[1], state, dt.date.fromisoformat(opened), closed, due_review, dt.date.fromisoformat(due_date) if due_date else None, steps)


class KnownAnswerTests(unittest.TestCase):
    """01 section 11 hand computation on the repository template."""

    @classmethod
    def setUpClass(cls) -> None:
        log = review_trend.load_log(TEMPLATE, review_trend.REPO_ROOT, validate=True)
        cls.result = review_trend.compute([log], MEMOS, T)
        cls.srr = cls.result["reviews"]["SRR"]

    def test_counts_per_type_and_severity(self) -> None:
        rows = {(r["type"], r["severity"]): tuple(r[m] for m in MEASURES) for r in self.srr["rows"]}
        self.assertEqual(KNOWN_ROWS, rows)

    def test_derived_values(self) -> None:
        self.assertEqual(9, self.srr["age_open_median_days"])
        self.assertEqual(9, self.srr["age_open_max_days"])
        self.assertEqual(2, self.srr["age_closed_median_days"])
        self.assertIsNone(self.srr["closure_fraction_at_gate"], "undefined until the PDR memo is signed")
        self.assertIsNone(self.srr["next_gate"])
        self.assertEqual(0, self.srr["totals"]["overdue"], "both open items are due at PDR and no PDR memo is signed")
        self.assertEqual("Green", self.srr["zone"])
        self.assertEqual("Green", self.result["overall_zone"])

    def test_burndown_series(self) -> None:
        self.assertEqual(
            [
                {"date": "2026-10-03", "raised": 5, "closed_or_withdrawn": 1},
                {"date": "2026-10-05", "raised": 5, "closed_or_withdrawn": 3},
            ],
            self.srr["burndown"],
        )

    def test_fixture_log_is_the_template(self) -> None:
        self.assertEqual(
            json.loads(TEMPLATE.read_text(encoding="utf-8")),
            json.loads((FIXTURE / "docs/reviews/SRR/rfa-rid-log.json").read_text(encoding="utf-8")),
            "re-copy docs/templates/rfa-rid-log.example.json into the fixture and recompute 01 section 11",
        )

    def test_state_is_evaluated_at_t_from_history(self) -> None:
        log = review_trend.load_log(TEMPLATE, review_trend.REPO_ROOT)
        early = review_trend.compute([log], MEMOS, dt.date(2026, 10, 4))["reviews"]["SRR"]
        rows = {(r["type"], r["severity"]): r for r in early["rows"]}
        self.assertEqual(0, rows[("RID", "Major")]["closed"], "RID-SRR-001 closes on 2026-10-05")
        self.assertEqual(1, rows[("RID", "Major")]["open"], "Answered counts as open")
        before = review_trend.compute([log], MEMOS, dt.date(2026, 10, 2))["reviews"]["SRR"]
        self.assertEqual(0, before["totals"]["raised"])


class CliTests(unittest.TestCase):
    def test_text_summary_on_fixture(self) -> None:
        result = run_cli(FIXTURE, "--date", "2026-10-12")
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("overall zone Green", result.stdout)
        self.assertIn("RID   Major          1     0     0      1      0       0", result.stdout)
        self.assertIn("2026-10-05 raised 5, closed+withdrawn 3", result.stdout)

    def test_json_output_matches_known_answer(self) -> None:
        result = run_cli(FIXTURE, "--date", "2026-10-12", "--json")
        self.assertEqual(0, result.returncode, result.stderr)
        data = json.loads(result.stdout)
        self.assertEqual({"SRR": "2026-10-05"}, data["memos"])
        rows = {(r["type"], r["severity"]): tuple(r[m] for m in MEASURES) for r in data["reviews"]["SRR"]["rows"]}
        self.assertEqual(KNOWN_ROWS, rows)

    def test_repository_runs_cleanly_without_logs(self) -> None:
        result = run_cli(review_trend.REPO_ROOT, "--date", "2026-10-12")
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        if not list(review_trend.REPO_ROOT.glob(review_trend.LOG_GLOB)):
            self.assertIn("no RFA/RID log", result.stdout)

    def test_write_needs_package(self) -> None:
        self.assertEqual(2, run_cli(FIXTURE, "--write").returncode)
        self.assertEqual(2, run_cli(FIXTURE, "--write", "--package", "XDR").returncode)
        self.assertEqual(2, run_cli(FIXTURE, "--date", "12/10/2026").returncode)

    def test_invalid_log_exits_two(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "p"
            shutil.copytree(FIXTURE, root)
            log = root / "docs/reviews/SRR/rfa-rid-log.json"
            data = json.loads(log.read_text(encoding="utf-8"))
            data["items"][0]["severity"] = "Blocking"  # a RID cannot be Blocking
            log.write_text(json.dumps(data), encoding="utf-8")
            result = run_cli(root, "--date", "2026-10-12")
        self.assertEqual(2, result.returncode)
        self.assertIn("fails docs/templates/rfa-rid-log.schema.json", result.stderr)


class WriteTests(unittest.TestCase):
    """--write produces the figure and appends TPM-003 history without touching the rest of tpm.json."""

    def test_figure_and_history(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "p"
            shutil.copytree(FIXTURE, root)
            before = (root / "docs/plan/tpm.json").read_text(encoding="utf-8")
            result = run_cli(root, "--date", "2026-10-12", "--package", "PDR", "--write")
            self.assertEqual(0, result.returncode, result.stdout + result.stderr)
            figure = root / "docs/reviews/PDR/figures/review-trend.png"
            self.assertTrue(figure.is_file())
            self.assertEqual(b"\x89PNG", figure.read_bytes()[:4])
            text = (root / "docs/plan/tpm.json").read_text(encoding="utf-8")
            data = json.loads(text)
            history = data["tpms"][1]["history"]
            self.assertEqual(1, len(history))
            entry = history[0]
            self.assertEqual(("PDR", "2026-10-12", "SRR", "green", "Green"), (entry["review"], entry["date"], entry["log_review"], entry["status"], entry["zone"]))
            self.assertEqual((5, 2, 0, 2, 1, 0), tuple(entry[m] for m in MEASURES))
            self.assertEqual(round(2 / 4, 3), entry["cbe"], "closed / (raised - withdrawn) at T")
            self.assertEqual("docs/reviews/PDR/figures/review-trend.png", entry["evidence"])
            self.assertIn('{"id": "TPM-001", "key": "mass-margin", "history": [], "inline": [1, 2, 3]},', text, "other TPMs keep their formatting")
            self.assertEqual(before.split('"history": []')[0], text.split('"history": [')[0], "text before the first history array is unchanged")
            # A rerun for the same package and date replaces its entries; another date appends.
            self.assertEqual(0, run_cli(root, "--date", "2026-10-12", "--package", "PDR", "--write").returncode)
            self.assertEqual(1, len(json.loads((root / "docs/plan/tpm.json").read_text(encoding="utf-8"))["tpms"][1]["history"]))
            self.assertEqual(0, run_cli(root, "--date", "2026-10-13", "--package", "PDR", "--write").returncode)
            self.assertEqual(2, len(json.loads((root / "docs/plan/tpm.json").read_text(encoding="utf-8"))["tpms"][1]["history"]))

    def test_write_without_any_log(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "p"
            (root / "docs/plan").mkdir(parents=True)
            shutil.copy(FIXTURE / "docs/plan/tpm.json", root / "docs/plan/tpm.json")
            result = run_cli(root, "--date", "2026-09-30", "--package", "SRR", "--write")
            self.assertEqual(0, result.returncode, result.stdout + result.stderr)
            self.assertTrue((root / "docs/reviews/SRR/figures/review-trend.png").is_file())
            entry = json.loads((root / "docs/plan/tpm.json").read_text(encoding="utf-8"))["tpms"][1]["history"][0]
            self.assertIsNone(entry["log_review"])
            self.assertEqual(0, entry["raised"])
            self.assertEqual("green", entry["status"])

    def test_missing_tpm_is_an_input_error(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "p"
            shutil.copytree(FIXTURE, root)
            (root / "docs/plan/tpm.json").write_text('{"tpms": [{"id": "TPM-001", "key": "mass-margin", "history": []}]}', encoding="utf-8")
            result = run_cli(root, "--date", "2026-10-12", "--package", "PDR", "--write")
        self.assertEqual(2, result.returncode)
        self.assertIn("review-trend", result.stderr)


class ZoneTests(unittest.TestCase):
    """Alert zones of 01 section 11 on constructed logs."""

    def zone(self, items: list[review_trend.Item], memos: dict[str, dt.date | None], when: dt.date = T, review: str = "SRR") -> str:
        log = review_trend.ReviewLog(review, "fixture", items)
        return review_trend.compute([log], memos, when)["reviews"][review]["zone"]

    def test_overdue_minor_is_yellow(self) -> None:
        items = [item("RID-SRR-001", "Minor", "Open", due_date="2026-10-10")]
        self.assertEqual("Yellow", self.zone(items, {"SRR": None}))

    def test_more_than_three_overdue_is_red(self) -> None:
        items = [item(f"RID-SRR-00{n}", "Minor", "Open", due_date="2026-10-10") for n in range(1, 5)]
        self.assertEqual("Red", self.zone(items, {"SRR": None}))

    def test_major_open_after_the_memo_is_red(self) -> None:
        items = [item("RID-SRR-001", "Major", "Answered", due_review="SRR", history=[("2026-10-03", "Open"), ("2026-10-04", "Answered")])]
        self.assertEqual("Red", self.zone(items, {"SRR": dt.date(2026, 10, 5)}))
        self.assertEqual("Green", self.zone(items, {"SRR": None}), "before signing the Major RID is work in progress")

    def test_overdue_blocking_rfa_is_red(self) -> None:
        items = [item("RFA-SRR-001", "Blocking", "Open", due_date="2026-10-10")]
        self.assertEqual("Red", self.zone(items, {"SRR": None}))

    def test_closure_fraction_below_threshold_at_next_gate_is_red(self) -> None:
        closed = [item(f"RID-SRR-00{n}", "Minor", "Closed", history=[("2026-10-03", "Open"), ("2026-10-06", "Closed")]) for n in range(1, 4)]
        still_open = [item(f"RFA-SRR-00{n}", "Routine", "Open", due_review="CDR") for n in range(1, 3)]
        memos = {"SRR": dt.date(2026, 10, 5), "PDR": dt.date(2026, 11, 20)}
        log = review_trend.ReviewLog("SRR", "fixture", closed + still_open)
        data = review_trend.compute([log], memos, dt.date(2026, 11, 25))["reviews"]["SRR"]
        self.assertEqual("PDR", data["next_gate"])
        self.assertEqual(0.6, data["closure_fraction_at_gate"])
        self.assertEqual("Red", data["zone"])

    def test_overdue_by_due_review_memo(self) -> None:
        items = [item("RID-SRR-001", "Minor", "Open", due_review="PDR")]
        memos = {"SRR": dt.date(2026, 10, 5), "PDR": dt.date(2026, 11, 20)}
        self.assertEqual(0, review_trend.compute([review_trend.ReviewLog("SRR", "f", items)], memos, dt.date(2026, 11, 20))["reviews"]["SRR"]["totals"]["overdue"], "memo dated T is not before T")
        self.assertEqual(1, review_trend.compute([review_trend.ReviewLog("SRR", "f", items)], memos, dt.date(2026, 11, 21))["reviews"]["SRR"]["totals"]["overdue"])

    def test_review_order_places_delta_trrs_between_trr_and_sar(self) -> None:
        order = sorted(["SAR", "TRR-D2", "SRR", "TRR", "TRR-D1", "CDR", "PDR", "TRR-D10"], key=review_trend.review_rank)
        self.assertEqual(["SRR", "PDR", "CDR", "TRR", "TRR-D1", "TRR-D2", "TRR-D10", "SAR"], order)
        memos = {"TRR": dt.date(2027, 3, 1), "TRR-D1": dt.date(2027, 4, 1), "SAR": dt.date(2027, 6, 1)}
        self.assertEqual(("TRR-D1", dt.date(2027, 4, 1)), review_trend.next_gate("TRR", memos, dt.date(2027, 7, 1)))
        self.assertIsNone(review_trend.next_gate("TRR", memos, dt.date(2027, 3, 15)), "a memo signed after T does not count")


if __name__ == "__main__":
    unittest.main()
