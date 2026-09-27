"""Known-answer tests for tools/complexity_gate.py (SWE-136 tool validation; 07 CS-17, CS-19, CS-38; SWE-220; MSR-17;
CR-001 per-file allowance; CR-005 counting convention; CR-005 amendment of 2026-09-27, the CS-19 main loop of
cwht-app::main, SRR close-out item A).

Fixture tools/tests/fixtures/complexity_gate/:
  src/core.rs, src/app.rs  sources the analyzer output names (app.rs carries // @target-only)
  rca.json                 real rust-code-analysis-cli 0.0.25 output on those two files, written by
                               cd tools/tests/fixtures/complexity_gate && \\
                               rust-code-analysis-cli --metrics --output-format json --paths src/core.rs --paths src/app.rs > rca.json
                           (AnalyzerEndToEndTests re-runs that command and compares when the analyzer is installed)
  waivers.json             W1 (over_limit, CC 16, named in the memo) and W2 (memo lacks W2)
  cwht-app/Cargo.toml      names the package cwht-app, [[bin]] path src/main.rs (the CS-19 main-loop rule reads it)
  cwht-app/src/main.rs, cwht-app/src/tasks.rs   target-only sources of that package
  rca-main-loop.json       real rust-code-analysis-cli 0.0.25 output on them, written by
                               cd tools/tests/fixtures/complexity_gate && \\
                               rust-code-analysis-cli --metrics --output-format json \\
                                   --paths cwht-app/src/main.rs --paths cwht-app/src/tasks.rs > rca-main-loop.json
  docs/reviews/CDR/decision-memo.md  names W1 only
Expected answers, derived by hand from the sources with the CR-005 convention (analyzer: 1, plus one per
if and else-if, per match arm with `_` included, per loop, while and for; the gate adds one per let ... else):
  analyzer own CC  app.rs main 1, safe_state_halt 2, panic 2, spin 2, wrong_arm 1, extra 2;
                   core.rs straight 1, branchy 5, at_limit 15, over_limit 16, let_else_limit 15, with_closure 2,
                   <anonymous> 2 (the closure; with_closure sum 4), not_let_else 3, ping 2, pong 1, fact 2, uses_string 1
  let ... else     main 2, wrong_arm 1, let_else_limit 1, <anonymous> 1; none in not_let_else (an if-else
                   initializer and an if let), in the comment of ping or in the string of uses_string
  gate CC          main 3, wrong_arm 2, let_else_limit 16, <anonymous> 3, others as the analyzer
  CS-38 allowance  main 1 + 2 CS-11 failure arms = 3; safe_state_halt and panic (#[panic_handler]) 1 + 1 halt
                   loop = 2; spin (a bare loop in another function), wrong_arm (else block is not
                   safe_state_halt()) and extra 1; file allowance 4 (2 arms, 2 halt loops)
  Result           18 functions, CC sum 80, mean 4.44, max 16, three above 12, two above 15, six target-only
                   above 1; CS-17 fails over_limit and let_else_limit; CS-38 fails spin, wrong_arm and extra;
                   CS-19 cycles fact -> fact and ping -> pong -> ping. main of src/app.rs gets no main-loop
                   allowance (no cwht-app package, no loop).
Expected answers for rca-main-loop.json (CR-005 amendment; analyzer, let ... else, gate CC, allowance items):
  main.rs main (top-level, crate root of cwht-app)  2 (its main loop), 2, 4; 1 + 2 CS-11 arms + 1 main loop = 4: pass
  main.rs safe_state_halt  2, 0, 2; 1 + 1 halt loop = 2: pass
  main.rs panic            1, 0, 1; 1 (no loop): pass
  main.rs idle             2, 0, 2; 1: CS-38 fail (a bare loop in another function)
  main.rs Runner::main     2, 0, 2; 1: CS-38 fail (a method named main is not cwht-app::main)
  tasks.rs main            2, 0, 2; 1: CS-38 fail (not the crate root file)
  Result                   6 functions, CC sum 13, mean 2.17, max 4, five target-only above 1, three failures;
                           file allowance of main.rs 4 (2 arms, 1 halt loop, 1 main loop), of tasks.rs 0.

Run from the repository root:
    .venv/bin/python -m unittest discover -s tools/tests -p test_complexity_gate.py
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
import complexity_gate as cg  # noqa: E402
from unsafe_audit import mask_rust  # noqa: E402

FIXTURE = TOOLS / "tests" / "fixtures" / "complexity_gate"
TOOL = TOOLS / "complexity_gate.py"
RCA = FIXTURE / "rca.json"
RCA_MAIN = FIXTURE / "rca-main-loop.json"
ANALYZER = "rust-code-analysis-cli"


def run_cli(*args: str, stdin: str | None = None) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, str(TOOL), "--root", str(FIXTURE), *args], input=stdin, capture_output=True, text=True, check=False)


def fixture_functions() -> list[cg.Function]:
    functions = cg.functions_of(cg.parse_stream(RCA.read_text(encoding="utf-8")))
    cg.apply_source_rules(functions, FIXTURE)
    return functions


def sites(code: str) -> list[tuple[int, str, str, str]]:
    return [(s.line, s.pattern, s.init, s.block) for s in cg.let_else_sites(mask_rust(code)[0])]


def one_file_run(tmp: str, source: str, spaces: list[dict]) -> list[cg.Function]:
    Path(tmp, "a.rs").write_text(source, encoding="utf-8")
    functions = cg.functions_of([{"name": "a.rs", "kind": "unit", "spaces": spaces}])
    cg.apply_source_rules(functions, Path(tmp))
    return functions


def crate_run(tmp: str, manifest: str | None, sources: dict[str, tuple[str, list[dict]]]) -> list[cg.Function]:
    """Write a package under tmp (Cargo.toml when manifest is not None) and apply the source rules to its files."""
    cg._MANIFESTS.clear()
    root = Path(tmp)
    if manifest is not None:
        (root / "Cargo.toml").write_text(manifest, encoding="utf-8")
    units = []
    for rel, (source, spaces) in sources.items():
        (root / rel).parent.mkdir(parents=True, exist_ok=True)
        (root / rel).write_text(source, encoding="utf-8")
        units.append({"name": rel, "kind": "unit", "spaces": spaces})
    functions = cg.functions_of(units)
    cg.apply_source_rules(functions, root)
    return functions


CWHT_APP = '[package]\nname = "cwht-app"\nversion = "0.0.0"\n\n[[bin]]\nname = "cwht-app"\npath = "src/main.rs"\n'
MAIN_WITH_LOOP = ("// @target-only\n"
                  "fn main() -> ! {\n"
                  "    let Some(board) = Board::take() else {\n        safe_state_halt()\n    };\n"
                  "    let Ok(mut led) = board.output(25) else { safe_state_halt() };\n"
                  "    loop {\n        step(&mut led);\n    }\n"
                  "}\n")  # main spans lines 2 to 10; analyzer CC 2 (the loop)


def space(name: str, start: int, end: int, cc: int, children: list[dict] | None = None) -> dict:
    kids = children or []
    total = cc + sum(k["metrics"]["cyclomatic"]["sum"] for k in kids)
    return {"name": name, "kind": "function", "start_line": start, "end_line": end, "spaces": kids, "metrics": {"cyclomatic": {"sum": float(total)}}}


class ParseKnownAnswerTests(unittest.TestCase):
    def test_own_cc_of_every_function(self) -> None:
        functions = cg.functions_of(cg.parse_stream(RCA.read_text(encoding="utf-8")))
        self.assertEqual(
            [("main", 1), ("safe_state_halt", 2), ("panic", 2), ("spin", 2), ("wrong_arm", 1), ("extra", 2),
             ("straight", 1), ("branchy", 5), ("at_limit", 15), ("over_limit", 16), ("let_else_limit", 15), ("with_closure", 2),
             ("<anonymous>", 2), ("not_let_else", 3), ("ping", 2), ("pong", 1), ("fact", 2), ("uses_string", 1)],
            [(f.name, f.rca_cc) for f in functions],
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


@unittest.skipUnless(shutil.which(ANALYZER), f"{ANALYZER} not installed (TV-012 end-to-end check)")
class AnalyzerEndToEndTests(unittest.TestCase):
    """TV-012 limitation 1 closure: rca.json is what the pinned analyzer writes on the fixture sources."""

    def test_pinned_version(self) -> None:
        out = subprocess.run([ANALYZER, "--version"], capture_output=True, text=True, check=False).stdout.strip()
        self.assertEqual("rust-code-analysis-cli 0.0.25", out)

    def test_fixture_is_the_analyzer_output(self) -> None:
        result = subprocess.run([ANALYZER, "--metrics", "--output-format", "json", "--paths", "src/core.rs", "--paths", "src/app.rs"],
                                cwd=FIXTURE, capture_output=True, text=True, check=False)
        self.assertEqual(0, result.returncode, result.stderr)
        by_name = lambda units: sorted(units, key=lambda u: u["name"])  # noqa: E731
        self.assertEqual(by_name(cg.parse_stream(RCA.read_text(encoding="utf-8"))), by_name(cg.parse_stream(result.stdout)))

    def test_main_loop_fixture_is_the_analyzer_output(self) -> None:
        result = subprocess.run([ANALYZER, "--metrics", "--output-format", "json", "--paths", "cwht-app/src/main.rs", "--paths", "cwht-app/src/tasks.rs"],
                                cwd=FIXTURE, capture_output=True, text=True, check=False)
        self.assertEqual(0, result.returncode, result.stderr)
        by_name = lambda units: sorted(units, key=lambda u: u["name"])  # noqa: E731
        self.assertEqual(by_name(cg.parse_stream(RCA_MAIN.read_text(encoding="utf-8"))), by_name(cg.parse_stream(result.stdout)))


class LetElseTests(unittest.TestCase):
    """CR-005: one is added for each `let ... else`, which the analyzer does not count."""

    def test_fixture_sites(self) -> None:
        self.assertEqual([(24, "Some(y)", "x", "return 0"), (30, "Some(y)", "x", "return 0")], sites((FIXTURE / "src" / "core.rs").read_text(encoding="utf-8")))
        self.assertEqual([(5, "Some(board)", "Board::take()", "safe_state_halt()"), (8, "Ok(led)", "board.output(25)", "safe_state_halt()"),
                          (26, "Ok(pin)", "board.output(1)", "return 0")], sites((FIXTURE / "src" / "app.rs").read_text(encoding="utf-8")))

    def test_gate_cc_is_analyzer_plus_let_else(self) -> None:
        got = {f.name: (f.rca_cc, f.let_else, f.cc) for f in fixture_functions()}
        self.assertEqual((1, 2, 3), got["main"])
        self.assertEqual((1, 1, 2), got["wrong_arm"])
        self.assertEqual((15, 1, 16), got["let_else_limit"])
        self.assertEqual((2, 1, 3), got["<anonymous>"], "the closure's let-else is the closure's")
        self.assertEqual((2, 0, 2), got["with_closure"], "and not its parent's")
        self.assertEqual((3, 0, 3), got["not_let_else"])
        self.assertEqual(80, sum(f.cc for f in fixture_functions()))

    def test_forms_that_are_not_let_else(self) -> None:
        self.assertEqual([], sites("fn f(c: bool, o: Option<u8>) {\n    let a = if c { 1 } else { 2 };\n    if let Some(v) = o { g(v) } else { g(a) }\n}\n"))
        self.assertEqual([], sites("fn f(o: Option<u8>) {\n    while let Some(v) = o { g(v) }\n    if c && let Some(v) = o { g(v) } else { h() }\n}\n"))
        self.assertEqual([], sites("fn f() {\n    // let Some(x) = y else { z };\n    let s = \"let Some(x) = y else { z };\";\n}\n"))
        self.assertEqual([], sites("fn f(a: u8, b: u8) -> bool {\n    let e = a == b;\n    let m = match a { 0 => 1, _ => 2 };\n    e\n}\n"))

    def test_forms_that_are_let_else(self) -> None:
        self.assertEqual([(2, "Some(x)", "v.iter().find(|y| { **y > 1 })", "return")],
                         sites("fn f(v: &[u8]) {\n    let Some(x) = v.iter().find(|y| { **y > 1 }) else { return };\n}\n"))
        source = ("fn f() -> ! {\n"
                  "    let Ok(p) = make(\n        1,\n    ) else {\n        safe_state_halt()\n    };\n"
                  "    #[allow(unused)] let (Some(a), Some(b)) = (p.a, p.b) else { return };\n"
                  "}\n")
        self.assertEqual([(2, "Ok(p)", "make(\n        1,\n    )", "safe_state_halt()"), (7, "(Some(a), Some(b))", "(p.a, p.b)", "return")], sites(source))

    def test_shared_line_is_counted_for_both_spaces(self) -> None:
        source = "fn f(o: Option<u8>) -> u8 {\n    let g = |x: Option<u8>| { let Some(y) = x else { return 0 }; y };\n    g(o)\n}\n"
        with tempfile.TemporaryDirectory() as tmp:
            functions = one_file_run(tmp, source, [space("f", 1, 4, 1, [space("<anonymous>", 2, 2, 1)])])
        self.assertEqual([("f", 1, 2), ("<anonymous>", 1, 2)], [(f.name, f.let_else, f.cc) for f in functions], "over-count, never under-count")


class AllowanceTests(unittest.TestCase):
    """CS-38 allowance of CR-001 (CS-11 failure arms) and CR-005 (CS-19 halt loops)."""

    def test_fixture_allowances(self) -> None:
        allowed = {f.name: (f.target_only, f.allowed, f.arms, f.halt_loop, f.main_loop) for f in fixture_functions() if f.file == "src/app.rs"}
        self.assertEqual({"main": (True, 3, 2, 0, 0), "safe_state_halt": (True, 2, 0, 1, 0), "panic": (True, 2, 0, 1, 0),
                          "spin": (True, 1, 0, 0, 0), "wrong_arm": (True, 1, 0, 0, 0), "extra": (True, 1, 0, 0, 0)}, allowed)
        self.assertEqual({"src/app.rs": {"allowance": 4, "cs11_failure_arms": 2, "cs19_halt_loops": 2, "cs19_main_loops": 0}}, cg.allowances(fixture_functions()))
        self.assertTrue(all(not f.target_only and f.allowed is None for f in fixture_functions() if f.file == "src/core.rs"))

    def test_admitted_arm_forms(self) -> None:
        arm = cg.LetElse
        self.assertTrue(cg.is_admitted_arm(arm(1, "Some(b)", "Rp2350::take()", "safe_state_halt()")))
        self.assertTrue(cg.is_admitted_arm(arm(1, "Ok(mut led)", "gpio.output_from_handle(p)", "safe_state_halt();")))
        self.assertFalse(cg.is_admitted_arm(arm(1, "Some(b)", "table.get(3)", "safe_state_halt()")), "Some arm without a take")
        self.assertFalse(cg.is_admitted_arm(arm(1, "Ok(p)", "make()", "return")), "failure branch is not safe_state_halt()")
        self.assertFalse(cg.is_admitted_arm(arm(1, "Ok(p)", "make()", "log(); safe_state_halt()")), "another statement in the failure branch")

    def test_halt_loop_allowance_needs_the_function_and_its_loop(self) -> None:
        source = ("// @target-only\n"
                  "#[panic_handler]\n"
                  "fn on_panic(_i: &PanicInfo) -> ! {\n    safe_state_halt()\n}\n"
                  "#[inline(never)] #[panic_handler] fn p2(_i: &PanicInfo) -> ! { loop {} }\n"
                  "fn safe_state_halt() -> ! {\n    if READY { g() }\n    h()\n}\n")
        with tempfile.TemporaryDirectory() as tmp:
            functions = one_file_run(tmp, source, [space("on_panic", 3, 5, 1), space("p2", 6, 6, 2), space("safe_state_halt", 7, 10, 2)])
        self.assertEqual([("on_panic", 0, 1), ("p2", 1, 2), ("safe_state_halt", 0, 1)], [(f.name, f.halt_loop, f.allowed) for f in functions])


class MainLoopTests(unittest.TestCase):
    """CR-005 amendment of 2026-09-27 (SRR close-out item A): +1 CS-38 allowance for the CS-19 main loop of cwht-app::main."""

    def test_fixture_main_loop_allowance(self) -> None:
        cg._MANIFESTS.clear()
        functions = cg.functions_of(cg.parse_stream(RCA_MAIN.read_text(encoding="utf-8")))
        cg.apply_source_rules(functions, FIXTURE)
        got = sorted((f.file, f.start, f.name, f.top_level, f.rca_cc, f.let_else, f.cc, f.arms, f.halt_loop, f.main_loop, f.allowed) for f in functions)
        self.assertEqual([
            ("cwht-app/src/main.rs", 4, "main", True, 2, 2, 4, 2, 0, 1, 4),
            ("cwht-app/src/main.rs", 14, "safe_state_halt", True, 2, 0, 2, 0, 1, 0, 2),
            ("cwht-app/src/main.rs", 19, "panic", True, 1, 0, 1, 0, 0, 0, 1),
            ("cwht-app/src/main.rs", 23, "idle", True, 2, 0, 2, 0, 0, 0, 1),
            ("cwht-app/src/main.rs", 30, "main", False, 2, 0, 2, 0, 0, 0, 1),
            ("cwht-app/src/tasks.rs", 4, "main", True, 2, 0, 2, 0, 0, 0, 1),
        ], got)

    def test_gate_on_the_fixture(self) -> None:
        result = run_cli("--max", "15", "--input", str(RCA_MAIN))
        self.assertEqual(1, result.returncode, result.stdout + result.stderr)
        lines = result.stdout.splitlines()
        tail = "in a // @target-only file (straight-line target-only code; allowance 0 CS-11 failure arm(s), 0 CS-19 halt loop(s) and 0 CS-19 main loop(s), CR-001 and CR-005)"
        self.assertEqual(sorted([
            f"FAIL CS-38 cwht-app/src/main.rs:23 idle CC 2 > 1 {tail}",
            f"FAIL CS-38 cwht-app/src/main.rs:30 main CC 2 > 1 {tail}",
            f"FAIL CS-38 cwht-app/src/tasks.rs:4 main CC 2 > 1 {tail}",
        ]), sorted(line for line in lines if line.startswith("FAIL")))
        self.assertEqual(["COUNT cwht-app/src/main.rs:4 main CC 4 = analyzer 2 + 2 let ... else (CR-005)"], [line for line in lines if line.startswith("COUNT")])
        self.assertEqual([
            "ALLOWANCE CS-38 cwht-app/src/main.rs: 4 (2 CS-11 failure arm(s), 1 CS-19 halt loop(s), 1 CS-19 main loop(s); CR-001, CR-005)",
            "ALLOWANCE CS-38 cwht-app/src/tasks.rs: 0 (0 CS-11 failure arm(s), 0 CS-19 halt loop(s), 0 CS-19 main loop(s); CR-001, CR-005)",
        ], [line for line in lines if line.startswith("ALLOWANCE")])
        self.assertIn("MSR-17 functions 6, max_cc 4, mean_cc 2.17, above_12 0, above_15 0, above_yellow 0, above_max 0, target_only_above_1 5", lines)
        self.assertEqual("complexity_gate: FAIL (3 failure(s), 0 CS-19 report(s))", lines[-1])

    def test_main_with_loop_passes_at_cc_4(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            functions = crate_run(tmp, CWHT_APP, {"src/main.rs": (MAIN_WITH_LOOP, [space("main", 2, 10, 2)])})
        (main,) = functions
        self.assertEqual((2, 2, 4, 2, 0, 1, 4), (main.rca_cc, main.let_else, main.cc, main.arms, main.halt_loop, main.main_loop, main.allowed))
        fails, _, _ = cg.evaluate(functions, 15, 12, [])
        self.assertEqual([], fails)

    def test_second_bare_loop_in_main_still_fails(self) -> None:
        source = MAIN_WITH_LOOP.replace("        step(&mut led);\n", "        step(&mut led);\n        loop {}\n")
        with tempfile.TemporaryDirectory() as tmp:
            functions = crate_run(tmp, CWHT_APP, {"src/main.rs": (source, [space("main", 2, 11, 3)])})
        (main,) = functions
        self.assertEqual((5, 1, 4), (main.cc, main.main_loop, main.allowed), "one item per function: the second loop is not covered")
        fails, _, _ = cg.evaluate(functions, 15, 12, [])
        self.assertEqual(["CS-38 src/main.rs:2 main CC 5 > 4 in a // @target-only file (straight-line target-only code; allowance 2 CS-11 failure arm(s), 0 CS-19 halt loop(s) and 1 CS-19 main loop(s), CR-001 and CR-005)"], fails)

    def test_bare_loop_in_another_function_still_fails(self) -> None:
        source = MAIN_WITH_LOOP + "fn idle() -> ! {\n    loop {}\n}\n"
        with tempfile.TemporaryDirectory() as tmp:
            functions = crate_run(tmp, CWHT_APP, {"src/main.rs": (source, [space("main", 2, 10, 2), space("idle", 11, 13, 2)])})
        self.assertEqual([("main", 1, 4), ("idle", 0, 1)], [(f.name, f.main_loop, f.allowed) for f in functions])
        fails, _, _ = cg.evaluate(functions, 15, 12, [])
        self.assertEqual(1, len(fails))
        self.assertTrue(fails[0].startswith("CS-38 src/main.rs:11 idle CC 2 > 1"), fails)

    def test_no_pooling_across_functions(self) -> None:
        source = ("// @target-only\nfn main() -> ! {\n    run()\n}\n"
                  "fn run() -> ! {\n    loop {}\n}\n")
        with tempfile.TemporaryDirectory() as tmp:
            functions = crate_run(tmp, CWHT_APP, {"src/main.rs": (source, [space("main", 2, 4, 1), space("run", 5, 7, 2)])})
        self.assertEqual([("main", 0, 1), ("run", 0, 1)], [(f.name, f.main_loop, f.allowed) for f in functions], "the credit needs the loop in main itself")
        self.assertEqual(1, len(cg.evaluate(functions, 15, 12, [])[0]))

    def test_identification_of_cwht_app_main(self) -> None:
        spaces = [space("main", 2, 10, 2)]
        cases = [
            ("package not named cwht-app", CWHT_APP.replace('name = "cwht-app"\nversion', 'name = "other-app"\nversion'), "src/main.rs", 0),
            ("no Cargo.toml above the file", None, "src/main.rs", 0),
            ("unparsable Cargo.toml", "[package\nname = cwht-app", "src/main.rs", 0),
            ("[[bin]] path is the crate root", CWHT_APP.replace("src/main.rs", "src/entry.rs"), "src/entry.rs", 1),
            ("src/main.rs is not a bin root when every [[bin]] names another path", CWHT_APP.replace("src/main.rs", "src/entry.rs"), "src/main.rs", 0),
            ("default bin root without [[bin]]", '[package]\nname = "cwht-app"\n', "src/main.rs", 1),
        ]
        for label, manifest, rel, expected in cases:
            with self.subTest(label), tempfile.TemporaryDirectory() as tmp:
                (main,) = crate_run(tmp, manifest, {rel: (MAIN_WITH_LOOP, spaces)})
                self.assertEqual((expected, 3 + expected), (main.main_loop, main.allowed))

    def test_nested_or_untagged_main_gets_no_credit(self) -> None:
        nested = "// @target-only\nfn outer() {\n    fn main() -> ! {\n        loop {}\n    }\n}\n"
        with tempfile.TemporaryDirectory() as tmp:
            functions = crate_run(tmp, CWHT_APP, {"src/main.rs": (nested, [space("outer", 2, 6, 1, [space("main", 3, 5, 2)])])})
        self.assertEqual([("outer", True, 0), ("main", False, 0)], [(f.name, f.top_level, f.main_loop) for f in functions])
        untagged = MAIN_WITH_LOOP.replace("// @target-only\n", "// host code\n")
        with tempfile.TemporaryDirectory() as tmp:
            (main,) = crate_run(tmp, CWHT_APP, {"src/main.rs": (untagged, [space("main", 2, 10, 2)])})
        self.assertEqual((False, None, 0), (main.target_only, main.allowed, main.main_loop), "CS-38 applies to // @target-only files only")


class GateKnownAnswerTests(unittest.TestCase):
    def test_gate_without_waivers(self) -> None:
        result = run_cli("--max", "15", "--input", str(RCA))
        self.assertEqual(1, result.returncode, result.stdout + result.stderr)
        lines = result.stdout.splitlines()
        self.assertEqual(
            [
                "FAIL CS-38 src/app.rs:21 spin CC 2 > 1 in a // @target-only file (straight-line target-only code; allowance 0 CS-11 failure arm(s), 0 CS-19 halt loop(s) and 0 CS-19 main loop(s), CR-001 and CR-005)",
                "FAIL CS-38 src/app.rs:25 wrong_arm CC 2 > 1 in a // @target-only file (straight-line target-only code; allowance 0 CS-11 failure arm(s), 0 CS-19 halt loop(s) and 0 CS-19 main loop(s), CR-001 and CR-005)",
                "FAIL CS-38 src/app.rs:30 extra CC 2 > 1 in a // @target-only file (straight-line target-only code; allowance 0 CS-11 failure arm(s), 0 CS-19 halt loop(s) and 0 CS-19 main loop(s), CR-001 and CR-005)",
                "FAIL CS-17 src/core.rs:17 over_limit CC 16 > 15 (SWE-220; 07 section 14.3 waiver absent)",
                "FAIL CS-17 src/core.rs:22 let_else_limit CC 16 > 15 (SWE-220; 07 section 14.3 waiver absent)",
            ],
            [line for line in lines if line.startswith("FAIL")],
        )
        self.assertEqual(
            [
                "COUNT src/app.rs:4 main CC 3 = analyzer 1 + 2 let ... else (CR-005)",
                "COUNT src/app.rs:25 wrong_arm CC 2 = analyzer 1 + 1 let ... else (CR-005)",
                "COUNT src/core.rs:22 let_else_limit CC 16 = analyzer 15 + 1 let ... else (CR-005)",
                "COUNT src/core.rs:29 <anonymous> CC 3 = analyzer 2 + 1 let ... else (CR-005)",
            ],
            [line for line in lines if line.startswith("COUNT")],
        )
        self.assertEqual(["YELLOW CS-17 src/core.rs:12 at_limit CC 15 > 12 (design reviewer's attention)"], [line for line in lines if line.startswith("YELLOW")])
        self.assertIn("ALLOWANCE CS-38 src/app.rs: 4 (2 CS-11 failure arm(s), 2 CS-19 halt loop(s), 0 CS-19 main loop(s); CR-001, CR-005)", lines)
        self.assertEqual(
            ["REPORT CS-19 call cycle (name-based): fact -> fact", "REPORT CS-19 call cycle (name-based): ping -> pong -> ping"],
            [line for line in lines if line.startswith("REPORT")],
        )
        self.assertIn("MSR-17 functions 18, max_cc 16, mean_cc 4.44, above_12 3, above_15 2, above_yellow 3, above_max 2, target_only_above_1 6", lines)
        self.assertEqual("complexity_gate: FAIL (5 failure(s), 2 CS-19 report(s))", lines[-1])

    def test_waiver_needs_the_memo(self) -> None:
        result = run_cli("--max", "15", "--input", str(RCA), "--waivers", str(FIXTURE / "waivers.json"))
        self.assertEqual(1, result.returncode, "let_else_limit and the CS-38 functions still fail")
        self.assertIn("WAIVED CS-17 src/core.rs:17 over_limit CC 16 > 15 under W1 (docs/reviews/CDR/decision-memo.md)", result.stdout)
        self.assertIn("NOTE waiver W2: decision memo docs/reviews/CDR/decision-memo.md does not exist or does not name W2", result.stdout)
        self.assertIn("FAIL CS-17 src/core.rs:22 let_else_limit CC 16 > 15", result.stdout, "W1 names over_limit only")
        self.assertNotIn("FAIL CS-17 src/core.rs:17", result.stdout)

    def test_stdin_pass_when_limits_hold(self) -> None:
        units = cg.parse_stream(RCA.read_text(encoding="utf-8"))
        core = next(u for u in units if u["name"] == "src/core.rs")
        core["spaces"] = [s for s in core["spaces"] if s["name"] in ("straight", "branchy")]
        app = next(u for u in units if u["name"] == "src/app.rs")
        app["spaces"] = [s for s in app["spaces"] if s["name"] in ("main", "safe_state_halt", "panic")]
        result = run_cli("--max", "15", stdin=json.dumps(core) + "\n" + json.dumps(app))
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("complexity_gate: PASS (0 failure(s), 0 CS-19 report(s))", result.stdout)

    def test_json_output(self) -> None:
        result = run_cli("--max", "15", "--input", str(RCA), "--json")
        data = json.loads(result.stdout)
        self.assertEqual(16, data["msr_17"]["max_cc"])
        self.assertEqual([["fact"], ["ping", "pong"]], data["cs_19_cycles"])
        self.assertEqual({"src/app.rs": {"allowance": 4, "cs11_failure_arms": 2, "cs19_halt_loops": 2, "cs19_main_loops": 0}}, data["cs_38_allowances"])
        self.assertEqual(5, len(data["failures"]))


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
