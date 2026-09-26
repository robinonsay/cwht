"""Known-answer tests for tools/complexity_gate.py (SWE-136 tool validation; 07 CS-17, CS-19, CS-38; SWE-220; MSR-17).

Fixture tools/tests/fixtures/complexity_gate/:
  src/core.rs, src/app.rs  sources the analyzer output names (app.rs carries // @target-only and a
                           Board::take() in main)
  rca.json                 hand-written analyzer output in the rust-code-analysis FuncSpace format:
                           own CC straight 1, branchy 5, at_limit 15, over_limit 16, with_closure 2
                           (sum 4 with its closure of 2), <anonymous> 2, ping 2, pong 1, fact 2,
                           uses_string 1; main 2, halt 1, extra 2
  waivers.json             W1 (over_limit, CC 16, named in the memo) and W2 (memo lacks W2)
  docs/reviews/CDR/decision-memo.md  names W1 only
Expected answers (hand-computed from those values): 13 functions, CC sum 52, mean 4.0, max 16,
two above 12, one above 15; CS-17 fails over_limit; CS-38 fails extra (main is allowed CC 2 for
its one ::take() call); CS-19 cycles fact -> fact and ping -> pong -> ping, and none from the
comment in ping or the string in uses_string.

Run from the repository root:
    .venv/bin/python -m unittest discover -s tools/tests -p test_complexity_gate.py
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
import complexity_gate as cg  # noqa: E402

FIXTURE = TOOLS / "tests" / "fixtures" / "complexity_gate"
TOOL = TOOLS / "complexity_gate.py"
RCA = FIXTURE / "rca.json"


def run_cli(*args: str, stdin: str | None = None) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, str(TOOL), "--root", str(FIXTURE), *args], input=stdin, capture_output=True, text=True, check=False)


class ParseKnownAnswerTests(unittest.TestCase):
    def test_own_cc_of_every_function(self) -> None:
        functions = cg.functions_of(cg.parse_stream(RCA.read_text(encoding="utf-8")))
        self.assertEqual(
            [("straight", 1), ("branchy", 5), ("at_limit", 15), ("over_limit", 16), ("with_closure", 2), ("<anonymous>", 2),
             ("ping", 2), ("pong", 1), ("fact", 2), ("uses_string", 1), ("main", 2), ("halt", 1), ("extra", 2)],
            [(f.name, f.cc) for f in functions],
        )

    def test_array_and_plain_number_forms(self) -> None:
        units = [{"name": "src/core.rs", "kind": "unit", "spaces": [
            {"name": "straight", "kind": "function", "start_line": 3, "end_line": 5, "spaces": [], "metrics": {"cyclomatic": 1}},
            {"name": "branchy", "kind": "function", "start_line": 7, "end_line": 9, "spaces": [], "metrics": {"cyclomatic": 5}}],
            "metrics": {"cyclomatic": 0}}]
        functions = cg.functions_of(cg.parse_stream(json.dumps(units)))
        self.assertEqual([("straight", 1), ("branchy", 5)], [(f.name, f.cc) for f in functions])

    def test_inputs_not_understood(self) -> None:
        with self.assertRaisesRegex(cg.InputError, "no function space"):
            cg.functions_of(cg.parse_stream(""))
        with self.assertRaisesRegex(cg.InputError, "not JSON"):
            cg.parse_stream("{not json")
        bad = {"name": "a.rs", "spaces": [{"name": "f", "kind": "function", "start_line": 1, "end_line": 2, "spaces": [
            {"name": "g", "kind": "function", "start_line": 1, "end_line": 1, "spaces": [], "metrics": {"cyclomatic": {"sum": 3}}}],
            "metrics": {"cyclomatic": {"sum": 2}}}]}
        with self.assertRaisesRegex(cg.InputError, "own CC -1.0"):
            cg.functions_of([bad])


class GateKnownAnswerTests(unittest.TestCase):
    def test_gate_without_waivers(self) -> None:
        result = run_cli("--max", "15", "--input", str(RCA))
        self.assertEqual(1, result.returncode, result.stdout + result.stderr)
        lines = result.stdout.splitlines()
        self.assertEqual(
            [
                "FAIL CS-17 src/core.rs:16 over_limit CC 16 > 15 (SWE-220; 07 section 14.3 waiver absent)",
                "FAIL CS-38 src/app.rs:13 extra CC 2 > 1 in a // @target-only file (straight-line target-only code; CS-11 board take allowance included)",
            ],
            [line for line in lines if line.startswith("FAIL")],
        )
        self.assertIn("YELLOW CS-17 src/core.rs:11 at_limit CC 15 > 12 (design reviewer's attention)", lines)
        self.assertEqual(
            ["REPORT CS-19 call cycle (name-based): fact -> fact", "REPORT CS-19 call cycle (name-based): ping -> pong -> ping"],
            [line for line in lines if line.startswith("REPORT")],
        )
        self.assertIn("MSR-17 functions 13, max_cc 16, mean_cc 4.0, above_12 2, above_15 1, above_yellow 2, above_max 1, target_only_above_1 2", lines)

    def test_waiver_needs_the_memo(self) -> None:
        result = run_cli("--max", "15", "--input", str(RCA), "--waivers", str(FIXTURE / "waivers.json"))
        self.assertEqual(1, result.returncode, "extra still fails CS-38")
        self.assertIn("WAIVED CS-17 src/core.rs:16 over_limit CC 16 > 15 under W1 (docs/reviews/CDR/decision-memo.md)", result.stdout)
        self.assertIn("NOTE waiver W2: decision memo docs/reviews/CDR/decision-memo.md does not exist or does not name W2", result.stdout)
        self.assertNotIn("FAIL CS-17", result.stdout)

    def test_stdin_pass_when_limits_hold(self) -> None:
        units = [json.loads(line) for line in RCA.read_text(encoding="utf-8").splitlines()]
        core = units[0]
        core["spaces"] = [s for s in core["spaces"] if s["name"] in ("straight", "branchy")]
        result = run_cli("--max", "15", stdin=json.dumps(core))
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("complexity_gate: PASS (0 failure(s), 0 CS-19 report(s))", result.stdout)

    def test_board_take_allowance(self) -> None:
        functions = cg.functions_of(cg.parse_stream(RCA.read_text(encoding="utf-8")))
        cg.apply_source_rules(functions, FIXTURE)
        allowed = {f.name: (f.target_only, f.allowed) for f in functions if f.file == "src/app.rs"}
        self.assertEqual({"main": (True, 2), "halt": (True, 1), "extra": (True, 1)}, allowed)

    def test_json_output(self) -> None:
        result = run_cli("--max", "15", "--input", str(RCA), "--json")
        data = json.loads(result.stdout)
        self.assertEqual(16, data["msr_17"]["max_cc"])
        self.assertEqual([["fact"], ["ping", "pong"]], data["cs_19_cycles"])


class UsageTests(unittest.TestCase):
    def test_usage_and_input_errors_exit_two(self) -> None:
        self.assertEqual(2, run_cli().returncode, "--max is required")
        self.assertEqual(2, run_cli("--max", "10", "--yellow", "12", "--input", str(RCA)).returncode)
        self.assertEqual(2, run_cli("--max", "15", stdin="").returncode, "an empty pipe is never a pass")
        with tempfile.TemporaryDirectory() as tmp:
            missing = Path(tmp) / "rca.json"
            missing.write_text(json.dumps({"name": "src/none.rs", "spaces": [{"name": "f", "kind": "function", "start_line": 1, "end_line": 1, "spaces": [], "metrics": {"cyclomatic": {"sum": 1}}}]}), encoding="utf-8")
            result = run_cli("--max", "15", "--input", str(missing))
        self.assertEqual(2, result.returncode)
        self.assertIn("cannot be read", result.stderr)


if __name__ == "__main__":
    unittest.main()
