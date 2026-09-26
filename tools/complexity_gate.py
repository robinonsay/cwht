#!/usr/bin/env python3
"""Cyclomatic-complexity gate for the cwht firmware (07 CS-17, CS-19, CS-38, section 14.3; SWE-220; MSR-17; gate G5).

Reads the JSON that `rust-code-analysis-cli --metrics --output-format json --paths ...`
writes (one JSON object per analysed file, concatenated; a JSON array of them is
also accepted) from standard input or --input, and applies:

* CS-17 (SWE-220): every function has cyclomatic complexity (CC) of at most
  --max (15); a function above 12 (--yellow) is reported for the design
  reviewer's attention. A function above --max fails unless a waiver of 07
  section 14.3 covers it (--waivers).
* CS-38: in a file that carries the line `// @target-only`, every function is
  straight-line (CC 1), except the CS-11 board take: a function whose body
  contains the call `::take()` is allowed one decision per such call.
* CS-19: a name-based call graph of the analysed functions (calls written as
  `name(` or `.name(` outside comments and literals) is searched for cycles;
  each cycle is REPORTed for the reviewer (07 CS-19 enforcement "G ... reports
  cycles", R). Name-based: two functions with one name are one node, so a
  report may be a false positive; a cycle through a function pointer, a trait
  object or a macro is not seen. Reports never fail the gate.

Input format assumed (rust-code-analysis 0.0.25 serialization of FuncSpace):
each space has "name", "start_line", "end_line", "kind" ("unit", "function",
"impl", "trait", ...), "spaces" (nested spaces) and "metrics"."cyclomatic"
with "sum" (the space plus every nested space) or a plain number (the space
alone). A function's own CC is its "sum" less the "sum" of its direct child
spaces (closures and nested functions are their own spaces). An own CC below 1
means the input is not in this format and stops the run (exit 2), as does an
input with no function space: an empty pipe is never a pass. The format is
checked against the hand-computed functions of 07 section 8.3 once
rust-code-analysis-cli is installed (TV-012 limitation 1).

Waivers (--waivers FILE): a JSON list of objects {"id": "W<n>", "file": path
suffix, "function": name, "cc": maximum, "memo": path of the decision memo}.
A waiver is honoured only when the memo exists under --root and names the id
(07 section 14.3: the owner's waiver W<n> in the decision memo of the next gate).

Usage:
    rust-code-analysis-cli --metrics --output-format json --paths DIR ... | \\
        .venv/bin/python tools/complexity_gate.py --max 15 [--yellow 12] [--waivers FILE] [--root PATH] [--json]

Exit status: 0 no failure; 1 a CS-17 or CS-38 failure; 2 usage error or an
input that is not understood (not JSON, no function space, own CC below 1).

Known-answer test: tools/tests/test_complexity_gate.py on tools/tests/fixtures/complexity_gate/.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from unsafe_audit import mask_rust  # noqa: E402  (shared comment and literal masker, TV-011)

REPO_ROOT = Path(__file__).resolve().parents[1]
TARGET_ONLY = "// @target-only"
TAKE_CALL = re.compile(r"::take\s*\(\s*\)")
CALL = re.compile(r"(?<![A-Za-z0-9_])([a-z_][a-z0-9_]*)\s*(?:::<[^>]*>)?\s*\(")
NOT_CALLS = frozenset({"if", "while", "for", "match", "return", "loop", "fn", "in", "as", "let", "move", "unsafe", "ref", "mut", "where", "impl", "dyn", "else", "break", "continue", "some", "ok", "err"})


class InputError(Exception):
    """The analyzer output is not understood (exit 2)."""


@dataclass
class Function:
    file: str
    name: str
    start: int
    end: int
    cc: int
    target_only: bool = False
    allowed: int | None = None  # CS-38 allowance for target-only functions


def parse_stream(text: str) -> list[dict]:
    decoder = json.JSONDecoder()
    values, i = [], 0
    while True:
        while i < len(text) and text[i].isspace():
            i += 1
        if i >= len(text):
            break
        try:
            value, i = decoder.raw_decode(text, i)
        except json.JSONDecodeError as exc:
            raise InputError(f"input is not JSON at offset {i}: {exc.msg}") from exc
        values.extend(value if isinstance(value, list) else [value])
    return values


def cc_sum(space: dict) -> float:
    metric = (space.get("metrics") or {}).get("cyclomatic")
    if isinstance(metric, dict) and isinstance(metric.get("sum"), (int, float)):
        return float(metric["sum"])
    if isinstance(metric, (int, float)):
        return float(metric) + sum(cc_sum(child) for child in space.get("spaces") or [])
    raise InputError(f"space '{space.get('name')}' has no metrics.cyclomatic sum")


def own_cc(space: dict) -> float:
    metric = (space.get("metrics") or {}).get("cyclomatic")
    if isinstance(metric, (int, float)):
        return float(metric)
    return cc_sum(space) - sum(cc_sum(child) for child in space.get("spaces") or [])


def walk(space: dict, file: str, out: list[Function]) -> None:
    for child in space.get("spaces") or []:
        if child.get("kind") == "function":
            own = own_cc(child)
            if own < 1 or abs(own - round(own)) > 1e-6:
                raise InputError(f"{file}: function '{child.get('name')}' has own CC {own}; the input is not in the assumed format")
            out.append(Function(file, str(child.get("name") or "<closure>"), int(child.get("start_line", 0)), int(child.get("end_line", 0)), int(round(own))))
        walk(child, file, out)


def functions_of(units: list[dict]) -> list[Function]:
    out: list[Function] = []
    for unit in units:
        if not isinstance(unit, dict) or "name" not in unit:
            raise InputError("a top-level value is not a file space with a 'name'")
        walk(unit, str(unit["name"]), out)
    if not out:
        raise InputError("no function space in the input; the analyzer output is empty or not understood")
    return out


def source_lines(path: Path) -> list[str] | None:
    try:
        return path.read_text(encoding="utf-8", errors="replace").split("\n")
    except OSError:
        return None


def apply_source_rules(functions: list[Function], base: Path) -> dict[str, str]:
    """Mark target-only functions with their CS-38 allowance; return {file: masked code} for the call graph."""
    masked: dict[str, str] = {}
    for file in sorted({f.file for f in functions}):
        path = Path(file) if Path(file).is_absolute() else base / file
        lines = source_lines(path)
        if lines is None:
            raise InputError(f"source file {file} named by the analyzer cannot be read (CS-38 tags and CS-19 need it)")
        code, _ = mask_rust("\n".join(lines))
        masked[file] = code
        tagged = any(line.strip() == TARGET_ONLY for line in lines)
        code_lines = code.split("\n")
        for f in functions:
            if f.file == file and tagged:
                f.target_only = True
                body = "\n".join(code_lines[max(0, f.start - 1):f.end])
                f.allowed = 1 + len(TAKE_CALL.findall(body))
    return masked


def call_cycles(functions: list[Function], masked: dict[str, str]) -> list[list[str]]:
    names = {f.name for f in functions}
    edges: dict[str, set[str]] = {n: set() for n in names}
    for f in functions:
        body_lines = masked[f.file].split("\n")[f.start - 1:f.end]
        body = "\n".join(body_lines)
        header = re.search(r"\bfn\s+" + re.escape(f.name) + r"\b", body)
        if header:
            body = body[header.end():]
        for m in CALL.finditer(body):
            callee = m.group(1)
            if callee in names and callee not in NOT_CALLS:
                edges[f.name].add(callee)
    index: dict[str, int] = {}
    low: dict[str, int] = {}
    stack: list[str] = []
    on: set[str] = set()
    cycles: list[list[str]] = []
    counter = [0]

    def strong(v: str) -> None:  # Tarjan
        index[v] = low[v] = counter[0]
        counter[0] += 1
        stack.append(v)
        on.add(v)
        for w in sorted(edges[v]):
            if w not in index:
                strong(w)
                low[v] = min(low[v], low[w])
            elif w in on:
                low[v] = min(low[v], index[w])
        if low[v] == index[v]:
            comp = []
            while True:
                w = stack.pop()
                on.discard(w)
                comp.append(w)
                if w == v:
                    break
            if len(comp) > 1 or v in edges[v]:
                cycles.append(sorted(comp))

    sys.setrecursionlimit(max(1000, 4 * len(names) + 100))
    for v in sorted(names):
        if v not in index:
            strong(v)
    return sorted(cycles)


def load_waivers(path: Path | None, root: Path) -> tuple[list[dict], list[str]]:
    if path is None:
        return [], []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise InputError(f"waiver file {path}: {exc}") from exc
    valid, problems = [], []
    for n, w in enumerate(data if isinstance(data, list) else []):
        wid, memo = str(w.get("id", "")), str(w.get("memo", ""))
        if not re.fullmatch(r"W[0-9]+", wid) or not isinstance(w.get("cc"), int) or not w.get("function") or not w.get("file"):
            problems.append(f"waiver {n}: needs id W<n>, file, function and integer cc")
            continue
        memo_path = root / memo
        if not memo_path.is_file() or not re.search(r"\b" + re.escape(wid) + r"\b", memo_path.read_text(encoding="utf-8")):
            problems.append(f"waiver {wid}: decision memo {memo} does not exist or does not name {wid} (07 section 14.3); not honoured")
            continue
        valid.append(w)
    return valid, problems


def waiver_for(f: Function, waivers: list[dict]) -> dict | None:
    for w in waivers:
        if f.name == w["function"] and f.file.endswith(w["file"]) and f.cc <= w["cc"]:
            return w
    return None


def evaluate(functions: list[Function], limit: int, yellow: int, waivers: list[dict]) -> tuple[list[str], list[str], dict]:
    fails, notes = [], []
    for f in functions:
        where = f"{f.file}:{f.start} {f.name}"
        if f.cc > limit:
            w = waiver_for(f, waivers)
            if w:
                notes.append(f"WAIVED CS-17 {where} CC {f.cc} > {limit} under {w['id']} ({w['memo']})")
            else:
                fails.append(f"CS-17 {where} CC {f.cc} > {limit} (SWE-220; 07 section 14.3 waiver absent)")
        elif f.cc > yellow:
            notes.append(f"YELLOW CS-17 {where} CC {f.cc} > {yellow} (design reviewer's attention)")
        if f.target_only and f.allowed is not None and f.cc > f.allowed:
            w = waiver_for(f, waivers)
            if w:
                notes.append(f"WAIVED CS-38 {where} CC {f.cc} > {f.allowed} under {w['id']} ({w['memo']})")
            else:
                fails.append(f"CS-38 {where} CC {f.cc} > {f.allowed} in a {TARGET_ONLY} file (straight-line target-only code; CS-11 board take allowance included)")
    ccs = [f.cc for f in functions]
    msr = {
        "functions": len(ccs),
        "max_cc": max(ccs),
        "mean_cc": round(sum(ccs) / len(ccs), 2),
        "above_12": sum(1 for c in ccs if c > 12),
        "above_15": sum(1 for c in ccs if c > 15),
        "above_yellow": sum(1 for c in ccs if c > yellow),
        "above_max": sum(1 for c in ccs if c > limit),
        "target_only_above_1": sum(1 for f in functions if f.target_only and f.cc > 1),
    }
    return fails, notes, msr


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0], formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--max", type=int, required=True, help="CS-17 limit (15)")
    parser.add_argument("--yellow", type=int, default=12, help="CS-17 attention level (12)")
    parser.add_argument("--input", type=Path, default=None, help="analyzer JSON file (default: standard input)")
    parser.add_argument("--root", type=Path, default=REPO_ROOT, help="base for relative source paths and waiver memos")
    parser.add_argument("--waivers", type=Path, default=None)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    if args.max < 1 or args.yellow < 1 or args.yellow > args.max:
        parser.error("--max and --yellow must be positive with --yellow <= --max")
    root = args.root.resolve()
    try:
        text = args.input.read_text(encoding="utf-8") if args.input else sys.stdin.read()
        functions = functions_of(parse_stream(text))
        masked = apply_source_rules(functions, root)
        waivers, problems = load_waivers(args.waivers, root)
    except (InputError, OSError) as exc:
        print(f"complexity_gate: input error: {exc}", file=sys.stderr)
        return 2
    fails, notes, msr = evaluate(functions, args.max, args.yellow, waivers)
    cycles = call_cycles(functions, masked)
    notes = [f"NOTE {p}" for p in problems] + notes
    if args.json:
        print(json.dumps({"msr_17": msr, "failures": fails, "notes": notes, "cs_19_cycles": cycles}, indent=2))
    else:
        for line in fails:
            print(f"FAIL {line}")
        for line in notes:
            print(line)
        for cycle in cycles:
            print(f"REPORT CS-19 call cycle (name-based): {' -> '.join(cycle + cycle[:1])}")
        print("MSR-17 " + ", ".join(f"{k} {v}" for k, v in msr.items()))
        print(f"complexity_gate: {'FAIL' if fails else 'PASS'} ({len(fails)} failure(s), {len(cycles)} CS-19 report(s))")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
