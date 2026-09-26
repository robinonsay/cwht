"""Known-answer tests for tools/render_risk.py (SWE-136 tool validation; 05 section 9.1 class B).

Fixtures under tools/tests/fixtures/risk/:

    valid.json     a register that passes every check: Red by score (RSK-001), Red by the
                   safety override at L2/S5 (RSK-002, tagged software, Low confidence with a
                   hazard-analysis step), Yellow at the L1/C5 edge on Watch (RSK-003), Green at
                   the score-4 edge and Accepted (RSK-004), an aggregate (RSK-005), a Closed
                   child (RSK-006), a Realized risk with an NCR (RSK-007), and one Entered,
                   one Merged and one Declined candidate
    valid.md       the stored render of valid.json
    stale.md       valid.md with one summary cell changed
    hazards.json   hazard list for the hazard link rule cross-check
    faults.json    seeded faults: each is a list of edits to valid.json and the exact list
                   of errors validate() must report (an empty list proves an accepted branch)

Run from the repository root:

    .venv/bin/python -m unittest discover -s tools/tests
"""
from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
import render_risk  # noqa: E402

FX = TOOLS / "tests" / "fixtures" / "risk"
TOOL = TOOLS / "render_risk.py"


def load(name: str) -> dict:
    return json.loads((FX / name).read_text(encoding="utf-8"))


def errors(register: dict, gate: str | None = None, hazards: dict | None = None) -> list[str]:
    rep = render_risk.Report()
    render_risk.validate(register, rep, gate=gate, hazards=hazards)
    return rep.errors


def by_id(register: dict, rid: str) -> dict:
    return next(r for r in register["risks"] if r["id"] == rid)


def apply(register: dict, ops: list[dict]) -> dict:
    reg = copy.deepcopy(register)
    for op in ops:
        node = by_id(reg, op["risk"]) if "risk" in op else reg["candidates"][op["candidate"]]
        *parents, last = op["path"]
        for key in parents:
            node = node[key]
        if op.get("delete"):
            del node[last]
        else:
            node[last] = op["set"]
    return reg


def advance(register: dict, review: str, date: str) -> dict:
    """Append a Track-pass history entry at `review` to every active risk (process section 10 item 1)."""
    reg = copy.deepcopy(register)
    for r in reg["risks"]:
        if r["status"] in render_risk.INACTIVE:
            continue
        last = dict(r["history"][-1])
        last.update({"date": date, "review": review, "note": f"Track pass at {review}."})
        r["history"].append(last)
        r["last_assessed"] = {"date": date, "review": review}
        r["trend"] = "Stable"
    reg["updated"] = date
    return reg


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(TOOL), *args], capture_output=True, text=True, check=False)


class BandTests(unittest.TestCase):
    def test_band_edges(self) -> None:
        self.assertEqual("Green", render_risk.band(1, 4, 1))   # score 4
        self.assertEqual("Green", render_risk.band(2, 2, 1))   # score 4
        self.assertEqual("Yellow", render_risk.band(1, 5, 1))  # score 5
        self.assertEqual("Yellow", render_risk.band(5, 1, 1))  # score 5
        self.assertEqual("Yellow", render_risk.band(2, 5, 1))  # score 10, the largest product below 12
        self.assertEqual("Red", render_risk.band(3, 4, 1))     # score 12
        self.assertEqual("Red", render_risk.band(4, 3, 1))     # score 12

    def test_safety_override(self) -> None:
        self.assertEqual("Red", render_risk.band(2, 5, 5))     # L2 with safety 5: Red although score 10
        self.assertEqual("Yellow", render_risk.band(1, 5, 5))  # L1 with safety 5: Yellow (score 5)
        self.assertEqual("Yellow", render_risk.cell_band(2, 5))

    def test_override_flag(self) -> None:
        reg = load("valid.json")
        self.assertTrue(render_risk.red_by_override(by_id(reg, "RSK-002")))
        self.assertFalse(render_risk.red_by_override(by_id(reg, "RSK-001")))


class ValidFixtureTests(unittest.TestCase):
    def test_no_errors_no_warnings(self) -> None:
        rep = render_risk.Report()
        render_risk.validate(load("valid.json"), rep, hazards=load("hazards.json"))
        self.assertEqual([], rep.errors)
        self.assertEqual([], rep.warnings)

    def test_schema_accepts_fixture(self) -> None:
        rep = render_risk.Report()
        if not render_risk.validate_with_jsonschema(load("valid.json"), rep):
            self.skipTest("jsonschema not importable; run with .venv/bin/python")
        self.assertEqual([], rep.errors)

    def test_render_matches_stored(self) -> None:
        self.assertEqual((FX / "valid.md").read_text(encoding="utf-8"), render_risk.render(load("valid.json")))

    def test_software_record_is_category_or_tag(self) -> None:
        text = render_risk.render(load("valid.json"))
        self.assertIn("| Software risks (SWE-086 record: category software or tag software) | RSK-002, RSK-003 (1 category software, 1 tagged software) |", text)

    def test_override_ranked_first_and_marked(self) -> None:
        text = render_risk.render(load("valid.json"))
        self.assertIn("| 1 | [RSK-002](#rsk-002) |", text)
        self.assertIn("RSK-002 (R by safety override)", text)
        self.assertIn("| Red by safety override | RSK-002 |", text)

    def test_measures(self) -> None:
        rows = {m["review"]: m for m in render_risk.measures(load("valid.json"))}
        self.assertEqual(["Pre-SRR", "SRR"], list(rows))
        pre, srr = rows["Pre-SRR"], rows["SRR"]
        self.assertEqual((5, 1, 2, 2, 5, 0, 0), (pre["active"], pre["Red"], pre["Yellow"], pre["Green"], pre["opened"], pre["closed"], pre["accepted"]))
        self.assertEqual((6, 2, 3, 1, 2, 1, 1), (srr["active"], srr["Red"], srr["Yellow"], srr["Green"], srr["opened"], srr["closed"], srr["accepted"]))
        self.assertIsNone(pre["due_open"])
        self.assertEqual((1, 0), (srr["due_open"], srr["overdue"]))

    def test_cli_check_current(self) -> None:
        result = run_cli("--register", str(FX / "valid.json"), "--output", str(FX / "valid.md"), "--check")
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("is current", result.stdout)

    def test_cli_check_detects_stale_render(self) -> None:
        result = run_cli("--register", str(FX / "valid.json"), "--output", str(FX / "stale.md"), "--check")
        self.assertEqual(1, result.returncode, result.stdout + result.stderr)
        self.assertIn(render_risk.STALE_MESSAGE, result.stderr)

    def test_cli_render_writes_stored_file(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "register.md"
            result = run_cli("--register", str(FX / "valid.json"), "--output", str(out))
            self.assertEqual(0, result.returncode, result.stdout + result.stderr)
            self.assertEqual((FX / "valid.md").read_text(encoding="utf-8"), out.read_text(encoding="utf-8"))

    def test_cli_gate_and_hazards(self) -> None:
        ok = run_cli("--register", str(FX / "valid.json"), "--output", str(FX / "valid.md"), "--check", "--gate", "SRR", "--hazards", str(FX / "hazards.json"))
        self.assertEqual(0, ok.returncode, ok.stdout + ok.stderr)
        late = run_cli("--register", str(FX / "valid.json"), "--output", str(FX / "valid.md"), "--check", "--gate", "PDR")
        self.assertEqual(1, late.returncode, late.stdout + late.stderr)
        self.assertIn("RSK-001: last assessed at SRR, before the PDR Track pass (process section 10)", late.stderr)


class SeededFaultTests(unittest.TestCase):
    def test_each_fault_gives_exactly_its_errors(self) -> None:
        valid = load("valid.json")
        for fault in load("faults.json"):
            with self.subTest(fault=fault["name"]):
                self.assertEqual(fault["expected"], errors(apply(valid, fault["ops"])))

    def test_schema_rejects_realized_without_ncr_and_accepted_without_residual(self) -> None:
        valid = load("valid.json")
        for ops, fragment in [
            ([{"risk": "RSK-007", "path": ["related", "ncr_ids"], "set": []}], "risks/6/related"),
            ([{"risk": "RSK-004", "path": ["acceptance", "residual_score"], "delete": True}], "risks/3/acceptance"),
        ]:
            with self.subTest(fragment=fragment):
                rep = render_risk.Report()
                if not render_risk.validate_with_jsonschema(apply(valid, ops), rep):
                    self.skipTest("jsonschema not importable; run with .venv/bin/python")
                self.assertTrue(any(e.startswith(f"schema: {fragment}") for e in rep.errors), rep.errors)

    def test_fault_set_covers_required_cases(self) -> None:
        names = {f["name"] for f in load("faults.json")}
        required = {
            "score_mismatch", "red_one_active_step", "red_strategy_watch", "red_strategy_accept_while_mitigating",
            "override_red_at_L2_S5", "override_yellow_at_L1_S5", "aggregate_mismatch", "accepted_without_acceptance",
            "residual_score_mismatch", "trend_mismatch", "realized_without_ncr_or_cr", "low_confidence_without_control",
            "low_confidence_reassess_trigger_only", "software_tag_missing", "last_assessed_review_mismatch",
        }
        self.assertTrue(required <= names, sorted(required - names))


class GateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.valid = load("valid.json")
        self.at_pdr = advance(self.valid, "PDR", "2026-10-10")

    def test_gate_srr_passes(self) -> None:
        self.assertEqual([], errors(self.valid, gate="SRR"))

    def test_gate_pdr_needs_track_pass(self) -> None:
        expected = [f"{rid}: last assessed at SRR, before the PDR Track pass (process section 10)"
                    for rid in ["RSK-001", "RSK-002", "RSK-003", "RSK-004", "RSK-005", "RSK-007"]]
        self.assertEqual(expected, errors(self.valid, gate="PDR"))

    def test_gate_pdr_after_track_pass(self) -> None:
        self.assertEqual([], errors(self.at_pdr, gate="PDR"))

    def test_delta_trr_ranks_with_trr(self) -> None:
        at_trr = advance(advance(self.at_pdr, "CDR", "2026-10-20"), "TRR", "2026-11-01")
        self.assertEqual([], errors(at_trr, gate="TRR-D1"))

    def test_red_plan_approval_required_after_first_gate(self) -> None:
        reg = apply(self.at_pdr, [{"risk": "RSK-001", "path": ["mitigation", "plan_approval"], "delete": True}])
        self.assertEqual(["RSK-001: Red risk assessed at an earlier gate review has no mitigation.plan_approval (process section 8)"],
                         errors(reg, gate="PDR"))
        self.assertEqual([], errors(apply(self.valid, [{"risk": "RSK-001", "path": ["mitigation", "plan_approval"], "delete": True}]), gate="SRR"))

    def test_red_link_rule_applies_from_pdr_gate(self) -> None:
        reg = apply(self.at_pdr, [{"risk": "RSK-001", "path": ["related", "hazard_ids"], "set": []}])
        self.assertEqual(["RSK-001: Red risk has no REQ or HZ link at PDR or later (process section 11)"], errors(reg, gate="PDR"))
        # Before PDR the link is not yet required.
        self.assertEqual([], errors(apply(self.valid, [{"risk": "RSK-001", "path": ["related", "hazard_ids"], "set": []}]), gate="SRR"))

    def test_bad_gate_token(self) -> None:
        self.assertEqual(["--gate Pre-SRR is not one of SRR, PDR, CDR, TRR, TRR-Dn, SAR"], errors(self.valid, gate="Pre-SRR"))


class HazardCrossCheckTests(unittest.TestCase):
    def setUp(self) -> None:
        self.valid = load("valid.json")
        self.hazards = load("hazards.json")

    def test_back_link_missing(self) -> None:
        hz = copy.deepcopy(self.hazards)
        hz["hazards"][0]["related_risk_ids"] = []
        self.assertEqual(["HZ-001: related_risk_ids does not name RSK-001, which carries it (hazard link rule back-link)"],
                         errors(self.valid, hazards=hz))

    def test_safety_below_mapped_severity(self) -> None:
        reg = apply(self.valid, [{"risk": "RSK-001", "path": ["consequence", "safety"], "set": 3},
                                 {"risk": "RSK-001", "path": ["history", -1, "safety"], "set": 3}])
        self.assertEqual(["RSK-001: safety 3 below the minimum 4 for HZ-001 (Critical; hazard link rule)"],
                         errors(reg, hazards=self.hazards))

    def test_uncovered_hazard(self) -> None:
        hz = copy.deepcopy(self.hazards)
        hz["hazards"].append({"id": "HZ-004", "title": "Uncovered", "severity": "Marginal", "status": "Controls proposed", "related_risk_ids": []})
        self.assertEqual(["HZ-004: hazard with unverified controls is carried by no active risk (hazard link rule)"],
                         errors(self.valid, hazards=hz))

    def test_back_link_to_risk_that_does_not_carry_it(self) -> None:
        hz = copy.deepcopy(self.hazards)
        hz["hazards"][2]["related_risk_ids"] = ["RSK-003"]
        self.assertEqual(["HZ-003: related_risk_ids names RSK-003, which is not an active risk naming HZ-003"],
                         errors(self.valid, hazards=hz))


if __name__ == "__main__":
    unittest.main()
