#!/usr/bin/env python3
"""Software measurements for cwht (07 sections 8.2, 8.4 and 11; SWE-090, SWE-093; gates G2, G3 and G6).

One mode per invocation:

--link-map MAP [--link-ld LD]
    Gate G2 (MSR-18, MSR-19). Region origin and length come from the MEMORY
    block of the rustos pico2 linker script (default ../rustos/firmware/pico2/link.ld);
    use per region is the highest end address of any output section placed in
    it (LMA for FLASH, VMA for RAM) less the origin, which is the extent the
    linker's own memory report gives. Fails (exit 1) above the TPM-010 and
    TPM-011 red lines applied to those regions (flash unused below 30 percent,
    RAM unused below 25 percent; docs/plan/tpm.json) until the allocated-region
    sizes of 07 section 19 WP-SW-08 exist. Prints the MSR-18 and MSR-19 values
    with their 07 section 11.2 assessment (MSR-18 Yellow above 25 percent of
    4 MB, Red above 50; MSR-19 Yellow above 40 percent of 520 KB, Red above 60).

--diff-runs RUN1 RUN2
    Gate G3 (SWE-186, 07 section 9.2). Compares the (classname, name, outcome)
    sets of two JUnit files; passes only when they are identical, non-empty and
    every case passed.

--coverage LCOV [--branch-condition JSON] [--emu JSON]
    Gate G6 summary (MSR-13, MSR-14, emulation). Line, function and branch
    totals per crate from the lcov file (the crate is the directory under
    firmware/ or the rustos crate path); the totals of the llvm-cov JSON export
    of the nightly branch and condition run; the emulation report. An optional
    input that was not produced (its gate step was MISSING or SKIP) is reported
    as NOT PRODUCED; the lcov file is required. The 100 percent thresholds are
    enforced by cargo llvm-cov --fail-under in the gate, not here.

--check-records [--file PATH] [--against REV]
    The cross-record rules of 07 section 11.1 that JSON Schema cannot express,
    on docs/plan/measurements.json: every id is in the section 11.2 catalog
    (MSR-01 to MSR-28); records are in append order (no date earlier than the
    record before it) and `updated` is the latest record date; every
    `supersedes` names an earlier record of the same id; the records at REV
    (default HEAD) are an unchanged prefix of the file (append-only); every
    evidence hash of a Measured record equals the file as it stood at the first
    commit containing the record (the working tree when no commit contains it
    yet), reported, never skipped; and the MSR-18 and MSR-19 values of a record
    whose evidence includes a link map are re-derived from that map (the
    re-derivation known answer of 07 section 11.1). Git rules need --root to be
    the top of a git work tree; otherwise they are reported as not applied.

--analyze [--file PATH]
    07 section 11.3: prints the current record of each (id, scope), resolving
    supersedes (a record retires the one it names; the first Measured record of
    an id retires that id's Not yet measured record), with its recorded
    assessment, and the count per assessment. Trend plots into
    docs/reviews/<REVIEW>/figures/ are not implemented (TV-013 limitation).

The tool never writes docs/plan/measurements.json or docs/plan/tpm.json: the
append of new records and the TPM mirror of 07 section 11.1 are due with the
first image that contains application modules (FW-B1) and are not implemented
(TV-013 limitation).

Usage:
    .venv/bin/python tools/measurements.py [--root PATH] MODE ...

Exit status: 0 pass; 1 a gate criterion or record rule failed (FAIL lines);
2 usage error or an unreadable required input.

Known-answer test: tools/tests/test_measurements.py on tools/tests/fixtures/measurements/.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LINK_LD = "../rustos/firmware/pico2/link.ld"
DEFAULT_RECORDS = "docs/plan/measurements.json"
RED_LINE_USED_PCT = {"FLASH": 70.0, "RAM": 75.0}  # TPM-010 unused below 30 %, TPM-011 unused below 25 %
MSR18_BASE, MSR19_BASE = 4 * 1024 * 1024, 520 * 1024  # 07 section 11.2 units: % of 4 MB, % of 520 KB
MSR18_RULE, MSR19_RULE = (25.0, 50.0), (40.0, 60.0)  # Yellow above, Red above
CATALOG = {f"MSR-{n:02d}" for n in range(1, 29)}
UNITS = {"": 1, "K": 1024, "M": 1024 * 1024}


class UsageError(Exception):
    """A required input is missing or unreadable (exit 2)."""


# ----------------------------------------------------------------------------
# G2 link map
# ----------------------------------------------------------------------------


def memory_regions(link_ld: str) -> dict[str, tuple[int, int]]:
    regions = {}
    for m in re.finditer(r"\b(FLASH|RAM)\s*\([a-z]*\)\s*:\s*ORIGIN\s*=\s*(0x[0-9a-fA-F]+)\s*,\s*LENGTH\s*=\s*(\d+)([KM]?)", link_ld):
        regions[m.group(1)] = (int(m.group(2), 16), int(m.group(3)) * UNITS[m.group(4)])
    return regions


SECTION_LINE = re.compile(r"^\s*([0-9a-f]+)\s+([0-9a-f]+)\s+([0-9a-f]+)\s+\d+ (\.[^ ]+)$")


def link_map_usage(map_text: str, link_ld: str) -> dict[str, dict[str, float]]:
    """{region: {used, length, pct}} from an lld link map and the linker script."""
    regions = memory_regions(link_ld)
    if set(regions) != {"FLASH", "RAM"}:
        raise UsageError(f"linker script MEMORY block names {sorted(regions)}, not FLASH and RAM")
    end: dict[str, int | None] = {"FLASH": None, "RAM": None}
    for line in map_text.splitlines():
        m = SECTION_LINE.match(line)
        if not m:
            continue
        vma, lma, size = (int(m.group(i), 16) for i in (1, 2, 3))
        for name, addr in (("FLASH", lma), ("RAM", vma)):
            origin, length = regions[name]
            if origin <= addr < origin + length:
                end[name] = max(end[name] or origin, addr + size)
    result = {}
    for name, (origin, length) in regions.items():
        if end[name] is None:
            raise UsageError(f"no output section of the link map lies in region {name}")
        used = end[name] - origin
        result[name] = {"used": used, "length": length, "pct": 100.0 * used / length}
    return result


def assess(pct: float, rule: tuple[float, float]) -> str:
    return "Red" if pct > rule[1] else ("Yellow" if pct > rule[0] else "Green")


def msr_18_19(usage: dict[str, dict[str, float]]) -> dict[str, dict[str, Any]]:
    flash, ram = usage["FLASH"]["used"], usage["RAM"]["used"]
    p18, p19 = round(100.0 * flash / MSR18_BASE, 2), round(100.0 * ram / MSR19_BASE, 2)
    return {
        "MSR-18": {"bytes": int(flash), "percent_of_4MB": p18, "assessment": assess(p18, MSR18_RULE)},
        "MSR-19": {"bytes": int(ram), "percent_of_520KB": p19, "assessment": assess(p19, MSR19_RULE)},
    }


def mode_link_map(map_path: Path, ld_path: Path) -> tuple[int, list[str]]:
    for p in (map_path, ld_path):
        if not p.is_file():
            raise UsageError(f"{p} does not exist")
    usage = link_map_usage(map_path.read_text(encoding="utf-8"), ld_path.read_text(encoding="utf-8"))
    lines, ok = [], True
    for name, u in usage.items():
        within = u["pct"] <= RED_LINE_USED_PCT[name]
        ok = ok and within
        lines.append(f"{'PASS' if within else 'FAIL'} {name} used {int(u['used'])} B of {int(u['length'])} B = {u['pct']:.2f} % (red line {RED_LINE_USED_PCT[name]} % used, TPM-{'010' if name == 'FLASH' else '011'})")
    for msr, v in msr_18_19(usage).items():
        lines.append(f"{msr} " + ", ".join(f"{k} {v[k]}" for k in v))
    return (0 if ok else 1), lines


# ----------------------------------------------------------------------------
# G3 JUnit comparison
# ----------------------------------------------------------------------------


def junit_results(path: Path) -> set[tuple[str, str, str]]:
    try:
        root = ET.parse(path).getroot()
    except (OSError, ET.ParseError) as exc:
        raise UsageError(f"{path}: {exc}") from exc
    out = set()
    for case in root.iter("testcase"):
        tags = {child.tag for child in case}
        if tags & {"failure", "rerunFailure", "flakyFailure"}:
            outcome = "failure"
        elif tags & {"error", "rerunError", "flakyError"}:
            outcome = "error"
        elif "skipped" in tags:
            outcome = "skipped"
        else:
            outcome = "passed"
        out.add((case.get("classname") or "", case.get("name") or "", outcome))
    return out


def mode_diff_runs(first: Path, second: Path) -> tuple[int, list[str]]:
    a, b = junit_results(first), junit_results(second)
    lines = [f"run 1: {len(a)} cases, run 2: {len(b)} cases, passed in both: {sum(1 for r in a & b if r[2] == 'passed')}"]
    lines += [f"DIFF {'run 1 only' if r in a else 'run 2 only'} {r}" for r in sorted(a ^ b)]
    lines += [f"NOT PASSED {r}" for r in sorted(a | b) if r[2] != "passed"]
    ok = bool(a) and a == b and all(r[2] == "passed" for r in a)
    if not a:
        lines.append("FAIL run 1 holds no test case")
    lines.append(f"{'PASS' if ok else 'FAIL'} identical result sets, all passed (SWE-186)")
    return (0 if ok else 1), lines


# ----------------------------------------------------------------------------
# G6 coverage summary
# ----------------------------------------------------------------------------


def crate_of(source: str) -> str:
    parts = Path(source).parts
    for anchor in ("rustos", "firmware"):  # rustos first: its crates sit under rustos/firmware/
        if anchor in parts:
            i = len(parts) - 1 - parts[::-1].index(anchor)
            rest = parts[i + 1:]
            if anchor == "rustos" and rest[:1] == ("firmware",):
                rest = rest[1:]
            if rest:
                return rest[0] if anchor == "firmware" else "rustos/" + rest[0]
    return parts[0] if parts else "?"


def lcov_totals(text: str) -> dict[str, dict[str, int]]:
    totals: dict[str, dict[str, int]] = {}
    current = None
    keys = {"LF": "lines_found", "LH": "lines_hit", "FNF": "functions_found", "FNH": "functions_hit", "BRF": "branches_found", "BRH": "branches_hit"}
    for line in text.splitlines():
        if line.startswith("SF:"):
            current = totals.setdefault(crate_of(line[3:].strip()), {k: 0 for k in keys.values()})
        elif current is not None and ":" in line and line.split(":", 1)[0] in keys:
            current[keys[line.split(":", 1)[0]]] += int(line.split(":", 1)[1])
        elif line.strip() == "end_of_record":
            current = None
    return totals


def pct(hit: int, found: int) -> str:
    return "n/a" if found == 0 else f"{100.0 * hit / found:.2f} %"


def mode_coverage(lcov: Path, branch: Path | None, emu: Path | None) -> tuple[int, list[str]]:
    if not lcov.is_file():
        raise UsageError(f"lcov file {lcov} does not exist (G6 stable coverage step)")
    totals = lcov_totals(lcov.read_text(encoding="utf-8"))
    if not totals:
        raise UsageError(f"{lcov} holds no SF record")
    lines = []
    for crate, t in sorted(totals.items()):
        lines.append(f"MSR-13 {crate}: lines {t['lines_hit']}/{t['lines_found']} = {pct(t['lines_hit'], t['lines_found'])}, functions {t['functions_hit']}/{t['functions_found']} = {pct(t['functions_hit'], t['functions_found'])}, branches {t['branches_hit']}/{t['branches_found']} = {pct(t['branches_hit'], t['branches_found'])} (regions: cargo llvm-cov report)")
    if branch is None or not branch.is_file():
        lines.append(f"MSR-14 NOT PRODUCED ({branch or 'no --branch-condition'}): the nightly branch and condition step did not write it")
    else:
        try:
            data = json.loads(branch.read_text(encoding="utf-8"))
            items = data["data"][0]["totals"]
        except (json.JSONDecodeError, KeyError, IndexError, TypeError) as exc:
            raise UsageError(f"{branch} is not an llvm-cov JSON export ({exc})") from exc
        for key in sorted(items):
            v = items[key]
            if isinstance(v, dict) and {"count", "covered"} <= set(v):
                lines.append(f"MSR-14 {key}: {v['covered']}/{v['count']} = {pct(int(v['covered']), int(v['count']))}")
    if emu is None or not emu.is_file():
        lines.append(f"emulation report NOT PRODUCED ({emu or 'no --emu'}): tools/emu_run.sh prints SKIP until the PDR emulator ADR")
    else:
        lines.append(f"emulation report {emu}: {emu.stat().st_size} bytes (format defined with the emulator ADR; not interpreted)")
    return 0, lines


# ----------------------------------------------------------------------------
# Records
# ----------------------------------------------------------------------------


def git(root: Path, *args: str, binary: bool = False) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=not binary, check=False)


def git_top(root: Path) -> bool:
    r = git(root, "rev-parse", "--show-toplevel")
    return r.returncode == 0 and Path(r.stdout.strip()).resolve() == root.resolve()


def load_records(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise UsageError(f"{path}: {exc}") from exc
    if not isinstance(data, dict) or not isinstance(data.get("records"), list):
        raise UsageError(f"{path} has no records list")
    return data


def evidence_entries(record: dict) -> list[tuple[str, str]]:
    out = []
    for item in record.get("evidence") or []:
        m = re.fullmatch(r"(\S+) sha256=([0-9a-f]{64})", item)
        if m:
            out.append((m.group(1), m.group(2)))
    return out


def head_state(root: Path, rev: str, epath: str, digest: str) -> str:
    """Triage aid for a failed evidence check: the file at rev is equal, differs or is absent."""
    blob = git(root, "show", f"{rev}:{epath}", binary=True)
    if blob.returncode != 0:
        return "absent"
    return "equal to the record" if hashlib.sha256(blob.stdout).hexdigest() == digest else "differs from the record"


def key_of(record: dict) -> tuple[str, str, str]:
    return (record.get("id", ""), record.get("scope", ""), record.get("date", ""))


def check_records(root: Path, rel: str, against: str, link_ld: Path) -> tuple[int, list[str]]:
    path = root / rel
    data = load_records(path)
    records = data["records"]
    fails, notes = [], []
    previous = None
    seen: list[tuple[str, str, str]] = []
    for i, r in enumerate(records):
        where = f"records[{i}] {r.get('id')} '{str(r.get('scope'))[:60]}'"
        if r.get("id") not in CATALOG:
            fails.append(f"{where}: id is not in the 07 section 11.2 catalog MSR-01 to MSR-28")
        if previous and str(r.get("date", "")) < previous:
            fails.append(f"{where}: date {r.get('date')} is earlier than the record before it ({previous}); records are appended (07 section 11.1)")
        previous = str(r.get("date", previous or ""))
        sup = r.get("supersedes")
        if isinstance(sup, dict):
            target = (sup.get("id"), sup.get("scope"), sup.get("date"))
            if sup.get("id") != r.get("id"):
                fails.append(f"{where}: supersedes a record of another id ({sup.get('id')})")
            elif target not in seen:
                fails.append(f"{where}: supersedes {target[0]} '{str(target[1])[:60]}' {target[2]}, which is not an earlier record")
        seen.append(key_of(r))
    latest = max((str(r.get("date", "")) for r in records), default="")
    if records and data.get("updated") != latest:
        fails.append(f"updated is {data.get('updated')} but the latest record date is {latest} (07 section 11.1)")
    if not git_top(root):
        notes.append(f"git rules not applied: {root} is not the top of a git work tree")
        return report(fails, notes, len(records))
    at_rev = git(root, "show", f"{against}:{rel}")
    if at_rev.returncode != 0:
        notes.append(f"{rel} is not in {against}; append-only rule not applied")
    else:
        try:
            old = json.loads(at_rev.stdout).get("records", [])
        except json.JSONDecodeError:
            old = []
            fails.append(f"{rel} at {against} is not JSON")
        if records[:len(old)] != old:
            first = next((i for i, (a, b) in enumerate(zip(records, old)) if a != b), min(len(records), len(old)))
            fails.append(f"records differ from {against} at index {first}: records are appended, never edited or deleted (07 section 11.1)")
    commits = [c for c in git(root, "log", "--reverse", "--format=%H", "--", rel).stdout.split() if c]
    versions: dict[str, list] = {}
    for c in commits:
        shown = git(root, "show", f"{c}:{rel}")
        try:
            versions[c] = json.loads(shown.stdout).get("records", []) if shown.returncode == 0 else []
        except json.JSONDecodeError:
            versions[c] = []
    checked = 0
    for i, r in enumerate(records):
        if r.get("state") != "Measured":
            continue
        where = f"records[{i}] {r.get('id')} '{str(r.get('scope'))[:60]}' {r.get('date')}"
        commit = next((c for c in commits if r in versions[c]), None)
        for epath, digest in evidence_entries(r):
            checked += 1
            if commit:
                blob = git(root, "show", f"{commit}:{epath}", binary=True)
                content = blob.stdout if blob.returncode == 0 else None
                at = commit[:8]
            else:
                content = (root / epath).read_bytes() if (root / epath).is_file() else None
                at = "the working tree (record not yet committed)"
            if content is None or hashlib.sha256(content).hexdigest() != digest:
                problem = "does not exist" if content is None else "sha256 differs"
                fails.append(f"{where}: evidence {epath} {problem} at {at}; at {against}: {head_state(root, against, epath, digest)} (07 section 11.1 evidence preservation)")
                continue
            if epath.endswith(".map") and r.get("id") in ("MSR-18", "MSR-19") and link_ld.is_file():
                derived = msr_18_19(link_map_usage(content.decode("utf-8"), link_ld.read_text(encoding="utf-8")))[r["id"]]
                value = r.get("value") if isinstance(r.get("value"), dict) else {}
                mismatch = {k: (value.get(k), v) for k, v in derived.items() if k != "assessment" and value.get(k) != v}
                if mismatch:
                    fails.append(f"{where}: re-derived value differs from the record: {mismatch}")
                else:
                    notes.append(f"{where}: value re-derived from {epath}: {derived}")
    notes.append(f"{checked} evidence hash(es) checked against the first commit containing each record")
    return report(fails, notes, len(records))


def report(fails: list[str], notes: list[str], count: int) -> tuple[int, list[str]]:
    lines = [f"FAIL {f}" for f in fails] + [f"NOTE {n}" for n in notes]
    lines.append(f"measurements: {count} records, {'FAIL' if fails else 'PASS'} ({len(fails)} failure(s))")
    return (1 if fails else 0), lines


def current_records(records: list[dict]) -> list[dict]:
    current: dict[tuple[str, str], dict] = {}
    for r in records:
        sup = r.get("supersedes")
        if isinstance(sup, dict):
            current.pop((sup.get("id"), sup.get("scope")), None)
        if r.get("state") == "Measured":
            for k in [k for k, v in current.items() if k[0] == r.get("id") and v.get("state") == "Not yet measured"]:
                current.pop(k)
        current[(r.get("id"), r.get("scope"))] = r
    return sorted(current.values(), key=lambda r: (r.get("id", ""), r.get("scope", "")))


def mode_analyze(path: Path) -> tuple[int, list[str]]:
    records = load_records(path)["records"]
    current = current_records(records)
    lines = []
    for r in current:
        value = json.dumps(r.get("value"), separators=(",", ":"))
        lines.append(f"{r.get('id')} | {str(r.get('scope'))[:70]} | {r.get('state')} | {value[:80]} | {r.get('assessment')} | {r.get('date')}")
    tally: dict[str, int] = {}
    for r in current:
        tally[r.get("assessment", "?")] = tally.get(r.get("assessment", "?"), 0) + 1
    lines.append("current records: " + ", ".join(f"{k} {v}" for k, v in sorted(tally.items())) + f"; {len(current)} of {len(records)} records are current")
    return 0, lines


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0], formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=REPO_ROOT)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--link-map", type=Path, metavar="MAP")
    mode.add_argument("--diff-runs", type=Path, nargs=2, metavar=("RUN1", "RUN2"))
    mode.add_argument("--coverage", type=Path, metavar="LCOV")
    mode.add_argument("--check-records", action="store_true")
    mode.add_argument("--analyze", action="store_true")
    parser.add_argument("--link-ld", type=Path, default=None)
    parser.add_argument("--branch-condition", type=Path, default=None)
    parser.add_argument("--emu", type=Path, default=None)
    parser.add_argument("--file", default=DEFAULT_RECORDS, help="records file relative to --root")
    parser.add_argument("--against", default="HEAD", help="revision for the append-only rule")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    if not root.is_dir():
        parser.error(f"root is not a directory: {root}")
    link_ld = (root / (args.link_ld or Path(DEFAULT_LINK_LD))).resolve()
    try:
        if args.link_map:
            status, lines = mode_link_map(args.link_map, link_ld)
        elif args.diff_runs:
            status, lines = mode_diff_runs(*args.diff_runs)
        elif args.coverage:
            status, lines = mode_coverage(args.coverage, args.branch_condition, args.emu)
        elif args.check_records:
            status, lines = check_records(root, args.file, args.against, link_ld)
        else:
            status, lines = mode_analyze(root / args.file)
    except UsageError as exc:
        print(f"measurements: error: {exc}", file=sys.stderr)
        return 2
    for line in lines:
        print(line)
    return status


if __name__ == "__main__":
    sys.exit(main())
