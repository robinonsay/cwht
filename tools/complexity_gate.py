#!/usr/bin/env python3
"""Cyclomatic-complexity gate for the cwht firmware (07 CS-17, CS-19, CS-38, section 14.3; SWE-220; MSR-17; gate G5).

Reads the JSON that `rust-code-analysis-cli --metrics --output-format json --paths ...`
writes (one JSON object per analysed file, concatenated; a JSON array of them is
also accepted) from standard input or --input, and applies:

* The CC measure (CR-005, SRR close-out item 4): the own cyclomatic
  complexity that rust-code-analysis-cli 0.0.25 reports (every `match` arm
  counts, `_` included; a bare `loop` counts as a decision), plus one for each
  `let ... else` statement of the function, which the analyzer does not count.
* CS-17 (SWE-220): every function has CC of at most --max (15); a function
  above 12 (--yellow) is reported for the design reviewer's attention. A
  function above --max fails unless a waiver of 07 section 14.3 covers it
  (--waivers).
* CS-38: in a file that carries the line `// @target-only`, every function is
  straight-line (CC 1) except for the per-file allowance of CR-001 and CR-005,
  credited to the function whose body holds each item:
  - one for each CS-11 failure arm: a `let Some(..) = ..::take() else { .. }`
    (board take) or `let Ok(..) = .. else { .. }` (driver construction)
    statement whose else block is exactly `safe_state_halt()` (CR-001);
  - one for the bare `loop` of each CS-19 halt loop: the `#[panic_handler]`
    function and the function `safe_state_halt` (CR-005);
  - one for the bare `loop` of the CS-19 main loop in `cwht-app::main`
    (CR-005 amendment of 2026-09-27, SRR close-out item A): the top-level
    function `main` (not a method, not nested) of a file that is a binary
    crate root (a `[[bin]]` `path`, default `src/main.rs`) of the package
    whose nearest `Cargo.toml` names it `cwht-app`.
  Each item is credited once, to the function that holds it: a second bare
  `loop` in the same function is not covered, and one function's allowance
  never covers another function's decision (no pooling across functions). A
  two-arm `match` failure branch is not recognized (the analyzer counts both
  arms): it fails closed.
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
input with no function space: an empty pipe is never a pass. The fixture
analyzer outputs tools/tests/fixtures/complexity_gate/rca.json and
rca-main-loop.json are real rust-code-analysis-cli 0.0.25 output on the
fixture sources (TV-012 section 3). A function space that is a direct child of
the file space is top-level (the CS-19 main-loop rule needs it).

A `let ... else` is recognized in the comment- and literal-masked source: a
statement-initial `let` whose statement reaches, at bracket depth 0 and before
its `;`, an `else` not directly preceded by `}` (Rust rejects a let-else
initializer that ends in `}`). It is credited to the innermost function space
whose line range holds the `let` line; a line that is the first or last line
of a nested space is shared, and a let-else on it is counted for both spaces
(over-count, never under-count).

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
import tomllib
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from unsafe_audit import mask_rust  # noqa: E402  (shared comment and literal masker, TV-011)

REPO_ROOT = Path(__file__).resolve().parents[1]
TARGET_ONLY = "// @target-only"
TAKE_CALL = re.compile(r"::take\s*\(\s*\)")
LET = re.compile(r"(?<![A-Za-z0-9_])let(?![A-Za-z0-9_])")
ELSE = re.compile(r"else(?![A-Za-z0-9_])")
HALT_BODY = re.compile(r"^safe_state_halt\s*\(\s*\)\s*;?$")
BARE_LOOP = re.compile(r"(?<![A-Za-z0-9_])loop\s*\{")
HALT_FN = "safe_state_halt"
MAIN_CRATE = "cwht-app"  # 07 CS-19: the main loop in `cwht-app::main` (CR-005 amendment, SRR close-out item A)
MAIN_FN = "main"
PANIC_ATTR = re.compile(r"#\[\s*panic_handler\s*\]")
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
    cc: int  # the CR-005 measure: rca_cc + let_else
    rca_cc: int = 0  # own CC as the analyzer reports it
    let_else: int = 0  # `let ... else` statements credited to this function (CR-005)
    children: tuple[tuple[int, int], ...] = ()  # line ranges of the direct child spaces
    top_level: bool = False  # a direct child of the file space (not a method, not nested in a function or module)
    target_only: bool = False
    allowed: int | None = None  # CS-38 allowance for target-only functions: 1 + arms + halt_loop + main_loop
    arms: int = 0  # admitted CS-11 failure arms (CR-001)
    halt_loop: int = 0  # CS-19 halt loop allowance (CR-005)
    main_loop: int = 0  # CS-19 main loop allowance of `cwht-app::main` (CR-005 amendment, SRR close-out item A)


@dataclass
class LetElse:
    line: int  # 1-based line of the `let` keyword
    pattern: str
    init: str
    block: str  # text inside the else braces


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


def walk(space: dict, file: str, out: list[Function], depth: int = 0) -> None:
    for child in space.get("spaces") or []:
        if child.get("kind") == "function":
            own = own_cc(child)
            if own < 1 or abs(own - round(own)) > 1e-6:
                raise InputError(f"{file}: function '{child.get('name')}' has own CC {own}; the input is not in the assumed format")
            kids = tuple((int(k.get("start_line", 0)), int(k.get("end_line", 0))) for k in child.get("spaces") or [])
            cc = int(round(own))
            out.append(Function(file, str(child.get("name") or "<closure>"), int(child.get("start_line", 0)), int(child.get("end_line", 0)), cc, rca_cc=cc, children=kids, top_level=depth == 0))
        walk(child, file, out, depth + 1)


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


def _prev_char(code: str, i: int) -> str:
    j = i - 1
    while j >= 0 and code[j].isspace():
        j -= 1
    return code[j] if j >= 0 else ""


def _closing(code: str, i: int) -> int:
    """Index of the bracket closing the one at i, or -1."""
    depth = 0
    for k in range(i, len(code)):
        if code[k] in "([{":
            depth += 1
        elif code[k] in ")]}":
            depth -= 1
            if depth == 0:
                return k
    return -1


def let_else_sites(code: str) -> list[LetElse]:
    """Every `let ... else { .. }` statement of comment- and literal-masked Rust code (CR-005)."""
    sites: list[LetElse] = []
    for m in LET.finditer(code):
        if _prev_char(code, m.start()) not in ("", ";", "{", "}", "]"):
            continue  # `if let`, `while let`, let chains: not a let statement
        depth, eq, k = 0, -1, m.end()
        while k < len(code):
            c = code[k]
            if c in "([{":
                depth += 1
            elif c in ")]}":
                depth -= 1
                if depth < 0:
                    break
            elif depth == 0 and c == ";":
                break
            elif depth == 0 and c == "=" and eq < 0 and code[k + 1:k + 2] not in ("=", ">") and code[k - 1] not in "<>!=":
                eq = k
            elif depth == 0 and eq >= 0 and ELSE.match(code, k) and not (code[k - 1].isalnum() or code[k - 1] == "_"):
                if _prev_char(code, k) != "}":
                    j = k + 4
                    while j < len(code) and code[j].isspace():
                        j += 1
                    end = _closing(code, j) if j < len(code) and code[j] == "{" else -1
                    if end > 0:
                        sites.append(LetElse(code.count("\n", 0, m.start()) + 1, code[m.end():eq].strip(), code[eq + 1:k].strip(), code[j + 1:end].strip()))
                    break
            k += 1
    return sites


def own_lines(f: Function) -> set[int]:
    """Lines of f that are not strictly inside a direct child space (shared boundary lines stay)."""
    return {ln for ln in range(f.start, f.end + 1) if not any(a < ln < b for a, b in f.children)}


def is_admitted_arm(site: LetElse) -> bool:
    """A CS-11 failure arm of CR-001: board take or driver construction, else block only safe_state_halt()."""
    if not HALT_BODY.match(site.block):
        return False
    if site.pattern.startswith("Some") and TAKE_CALL.search(site.init):
        return True
    return site.pattern.startswith("Ok")


def is_panic_handler(f: Function, code_lines: list[str]) -> bool:
    k = f.start - 1  # 0-based index of the fn line
    if 0 <= k < len(code_lines) and PANIC_ATTR.search(code_lines[k].split("fn", 1)[0]):
        return True
    k -= 1
    while k >= 0:
        line = code_lines[k].strip()
        if not line:
            k -= 1
            continue
        if not line.startswith("#["):
            return False
        if PANIC_ATTR.search(line):
            return True
        k -= 1
    return False


_MANIFESTS: dict[Path, tuple[str | None, frozenset[Path]]] = {}


def package_of(path: Path) -> tuple[str | None, frozenset[Path]]:
    """Package name and binary crate roots from the nearest Cargo.toml above path (Cargo's rule).

    The roots are each `[[bin]]` `path`, and `src/main.rs` when there is no `[[bin]]` table or one
    without a `path`. A manifest that cannot be read or parsed, or has no `[package]` name, gives
    (None, no roots): the CS-19 main-loop allowance is then not credited (fails closed)."""
    for folder in path.resolve().parents:
        manifest = folder / "Cargo.toml"
        if not manifest.is_file():
            continue
        if folder not in _MANIFESTS:
            try:
                data = tomllib.loads(manifest.read_text(encoding="utf-8"))
            except (OSError, UnicodeDecodeError, tomllib.TOMLDecodeError):
                data = {}
            package = data.get("package")
            name = package.get("name") if isinstance(package, dict) else None
            bins = [b for b in data.get("bin") or [] if isinstance(b, dict)]
            roots = {(folder / b["path"]).resolve() for b in bins if isinstance(b.get("path"), str)}
            if not bins or any(not isinstance(b.get("path"), str) for b in bins):
                roots.add((folder / "src" / "main.rs").resolve())
            _MANIFESTS[folder] = (name if isinstance(name, str) else None, frozenset(roots))
        return _MANIFESTS[folder]
    return None, frozenset()


def is_cwht_app_main(f: Function, path: Path) -> bool:
    """The function of 07 CS-19 that holds the main loop: `cwht-app::main`, the top-level `main` of a
    binary crate root of the package `cwht-app` (CR-005 amendment of 2026-09-27)."""
    if f.name != MAIN_FN or not f.top_level:
        return False
    name, roots = package_of(path)
    return name == MAIN_CRATE and path.resolve() in roots


def apply_source_rules(functions: list[Function], base: Path) -> dict[str, str]:
    """Add the CR-005 let-else count to each function's CC and mark target-only functions with their
    CS-38 allowance (CR-001, CR-005); return {file: masked code} for the call graph."""
    masked: dict[str, str] = {}
    for file in sorted({f.file for f in functions}):
        path = Path(file) if Path(file).is_absolute() else base / file
        lines = source_lines(path)
        if lines is None:
            raise InputError(f"source file {file} named by the analyzer cannot be read (CS-38 tags, CR-005 let-else and CS-19 need it)")
        code, _ = mask_rust("\n".join(lines))
        masked[file] = code
        tagged = any(line.strip() == TARGET_ONLY for line in lines)
        code_lines = code.split("\n")
        sites = let_else_sites(code)
        for f in functions:
            if f.file != file:
                continue
            mine = own_lines(f)
            own_sites = [s for s in sites if s.line in mine]
            f.let_else = len(own_sites)
            f.cc = f.rca_cc + f.let_else
            if tagged:
                f.target_only = True
                f.arms = sum(1 for s in own_sites if is_admitted_arm(s))
                body = "\n".join(code_lines[i - 1] for i in sorted(mine) if 0 < i <= len(code_lines))
                if (f.name == HALT_FN or is_panic_handler(f, code_lines)) and BARE_LOOP.search(body):
                    f.halt_loop = 1
                elif is_cwht_app_main(f, path) and BARE_LOOP.search(body):
                    f.main_loop = 1
                f.allowed = 1 + f.arms + f.halt_loop + f.main_loop
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


def allowances(functions: list[Function]) -> dict[str, dict[str, int]]:
    """Per-file CS-38 allowance of CR-001 and CR-005: the admitted items of every tagged file (reported;
    each function is checked against its own items only)."""
    out: dict[str, dict[str, int]] = {}
    for f in functions:
        if f.target_only:
            a = out.setdefault(f.file, {"allowance": 0, "cs11_failure_arms": 0, "cs19_halt_loops": 0, "cs19_main_loops": 0})
            a["cs11_failure_arms"] += f.arms
            a["cs19_halt_loops"] += f.halt_loop
            a["cs19_main_loops"] += f.main_loop
            a["allowance"] += f.arms + f.halt_loop + f.main_loop
    return out


def evaluate(functions: list[Function], limit: int, yellow: int, waivers: list[dict]) -> tuple[list[str], list[str], dict]:
    fails, notes = [], []
    for f in functions:
        where = f"{f.file}:{f.start} {f.name}"
        if f.let_else:
            notes.append(f"COUNT {where} CC {f.cc} = analyzer {f.rca_cc} + {f.let_else} let ... else (CR-005)")
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
                fails.append(f"CS-38 {where} CC {f.cc} > {f.allowed} in a {TARGET_ONLY} file (straight-line target-only code; allowance {f.arms} CS-11 failure arm(s), {f.halt_loop} CS-19 halt loop(s) and {f.main_loop} CS-19 main loop(s), CR-001 and CR-005)")
    for file, a in sorted(allowances(functions).items()):
        notes.append(f"ALLOWANCE CS-38 {file}: {a['allowance']} ({a['cs11_failure_arms']} CS-11 failure arm(s), {a['cs19_halt_loops']} CS-19 halt loop(s), {a['cs19_main_loops']} CS-19 main loop(s); CR-001, CR-005)")
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
        print(json.dumps({"msr_17": msr, "failures": fails, "notes": notes, "cs_19_cycles": cycles, "cs_38_allowances": allowances(functions)}, indent=2))
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
