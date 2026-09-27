#!/usr/bin/env python3
"""Fabrication-file normalization for cwht release packages (CM plan section 8.2; TV-016).

kicad-cli 10.0.6 writes its export time into Gerber, drill, Gerber job, drill
report, STEP and PDF files, so two exports of the same board never hash the
same. This tool removes exactly the time stamps of the CM plan section 8.2
normalization table and nothing else, then hashes the result:

    Gerber  *.gbr        delete lines matching ^%TF\\.CreationDate,.*
                         ^G04 #@! TF\\.CreationDate,.* and ^G04 Created by KiCad .* date .*
    Excellon *.drl       delete lines matching ^; DRILL file .* date .* and ^; #@! TF\\.CreationDate,.*
    Gerber job *.gbrjob  replace the value of the "CreationDate" member with "normalized"
    Drill report *.rpt   delete lines matching ^Created on .*
    STEP *.step, *.stp   replace the time-stamp argument of FILE_NAME( with 'normalized'
    PDF *.pdf            replace the digits of /CreationDate (D:...) and /ModDate (D:...)
                         with zeros of the same length
    CSV *.csv            none (the CPL and BOM carry no date)
    Zip *.zip            not normalized and not listed: the raw hash is the upload identity
                         (SHA256SUMS); each member is normalized by its own type and listed
                         as <zip path>!<member name>

Any other file type is hashed as it is and reported with the rule "raw" on
standard error (no rule of the table applies to it).

Usage (from any directory; paths are resolved against the current directory):

    .venv/bin/python tools/normalize_fab.py [--root DIR] [--write DIR] PATH...
        print "<sha256>  <name>" for every file, sorted by name (shasum format),
        where <name> is the path relative to --root (default: each directory
        argument itself, or the directory of a file argument)
    ... --sums FILE PATH...
        also write that list to FILE (the SHA256SUMS.normalized of a package)
    ... --check FILE PATH...
        compare with a stored list; exit 1 on any difference, printing each
        added, missing or changed name
    --write DIR writes each normalized file to DIR/<name> for inspection

Files named SHA256SUMS, SHA256SUMS.normalized and the --sums or --check file
itself are never listed. Directories are walked recursively; names starting
with "." are skipped.

Exit status: 0 success (and, with --check, every hash equal); 1 --check found a
difference; 2 usage error, unreadable input, a bad zip, or no file to list.
Standard library only; interpreter per TV-001.
"""
from __future__ import annotations

import argparse
import hashlib
import io
import os
import re
import sys
import zipfile

EXCLUDED_NAMES = {"SHA256SUMS", "SHA256SUMS.normalized"}

GERBER_DELETE = [
    re.compile(rb"^%TF\.CreationDate,.*"),
    re.compile(rb"^G04 #@! TF\.CreationDate,.*"),
    re.compile(rb"^G04 Created by KiCad .* date .*"),
]
DRILL_DELETE = [
    re.compile(rb"^; DRILL file .* date .*"),
    re.compile(rb"^; #@! TF\.CreationDate,.*"),
]
REPORT_DELETE = [re.compile(rb"^Created on .*")]
GBRJOB_DATE = re.compile(rb'("CreationDate"\s*:\s*)"[^"]*"')
# FILE_NAME( 'name', 'time stamp', ... ): STEP strings double an embedded quote.
STEP_FILE_NAME = re.compile(rb"(FILE_NAME\s*\(\s*'(?:[^']|'')*'\s*,\s*)'(?:[^']|'')*'", re.S)
PDF_DATE = re.compile(rb"(/(?:CreationDate|ModDate)\s*\(D:)([^)]*)(\))")


class UsageError(Exception):
    """Raised for exit status 2."""


def _delete_lines(data: bytes, patterns: list[re.Pattern]) -> tuple[bytes, int]:
    out, removed = [], 0
    for line in data.splitlines(keepends=True):
        body = line.rstrip(b"\r\n")
        if any(p.match(body) for p in patterns):
            removed += 1
            continue
        out.append(line)
    return b"".join(out), removed


def _zero_digits(match: re.Match) -> bytes:
    return match.group(1) + re.sub(rb"[0-9]", b"0", match.group(2)) + match.group(3)


def normalize(name: str, data: bytes) -> tuple[bytes, str, int]:
    """Return (normalized bytes, rule name, number of substitutions) for a file name and content."""
    ext = os.path.splitext(name.lower())[1]
    if ext == ".gbr":
        out, n = _delete_lines(data, GERBER_DELETE)
        return out, "gerber", n
    if ext == ".drl":
        out, n = _delete_lines(data, DRILL_DELETE)
        return out, "excellon", n
    if ext == ".rpt":
        out, n = _delete_lines(data, REPORT_DELETE)
        return out, "drill-report", n
    if ext == ".gbrjob":
        out, n = GBRJOB_DATE.subn(rb'\1"normalized"', data)
        return out, "gerber-job", n
    if ext in (".step", ".stp"):
        out, n = STEP_FILE_NAME.subn(rb"\1'normalized'", data, count=1)
        return out, "step", n
    if ext == ".pdf":
        out, n = PDF_DATE.subn(_zero_digits, data)
        return out, "pdf", n
    if ext == ".csv":
        return data, "csv-none", 0
    return data, "raw", 0


def _walk(path: str) -> list[str]:
    found = []
    for base, dirs, files in os.walk(path):
        dirs[:] = sorted(d for d in dirs if not d.startswith("."))
        for f in sorted(files):
            if not f.startswith("."):
                found.append(os.path.join(base, f))
    return found


def collect(paths: list[str], root: str | None, skip: set[str]) -> list[tuple[str, str]]:
    """Return sorted (name, absolute path) pairs for every file to list."""
    items: dict[str, str] = {}
    for p in paths:
        ap = os.path.abspath(p)
        if os.path.isdir(ap):
            base = os.path.abspath(root) if root else ap
            files = _walk(ap)
        elif os.path.isfile(ap):
            base = os.path.abspath(root) if root else os.path.dirname(ap)
            files = [ap]
        else:
            raise UsageError(f"no such file or directory: {p}")
        for f in files:
            if os.path.basename(f) in EXCLUDED_NAMES or f in skip:
                continue
            name = os.path.relpath(f, base)
            if name.startswith(".."):
                raise UsageError(f"{f} is outside --root {base}")
            if name in items and items[name] != f:
                raise UsageError(f"two inputs give the same name {name}")
            items[name] = f
    return sorted(items.items())


def entries(pairs: list[tuple[str, str]], write_dir: str | None, log) -> list[tuple[str, str]]:
    """Normalize every file (zip members one by one) and return sorted (name, sha256) pairs."""
    result = []
    for name, path in pairs:
        with open(path, "rb") as fh:
            data = fh.read()
        if name.lower().endswith(".zip"):
            try:
                zf = zipfile.ZipFile(io.BytesIO(data))
            except zipfile.BadZipFile as exc:
                raise UsageError(f"{name}: not a readable zip ({exc})") from exc
            for member in sorted(zf.namelist()):
                if member.endswith("/"):
                    continue
                mname = f"{name}!{member}"
                out, rule, n = normalize(member, zf.read(member))
                result.append(_emit(mname, out, rule, n, write_dir, log))
            continue
        out, rule, n = normalize(name, data)
        result.append(_emit(name, out, rule, n, write_dir, log))
    return sorted(result)


def _emit(name, out, rule, n, write_dir, log):
    digest = hashlib.sha256(out).hexdigest()
    log(f"normalize_fab: {name}: rule {rule}, {n} substitution(s)")
    if write_dir:
        dest = os.path.join(write_dir, name.replace("!", os.sep))
        os.makedirs(os.path.dirname(dest) or ".", exist_ok=True)
        with open(dest, "wb") as fh:
            fh.write(out)
    return name, digest


def format_sums(rows: list[tuple[str, str]]) -> str:
    return "".join(f"{digest}  {name}\n" for name, digest in rows)


def parse_sums(text: str) -> dict[str, str]:
    table = {}
    for i, line in enumerate(text.splitlines(), 1):
        if not line.strip():
            continue
        m = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
        if not m:
            raise UsageError(f"stored list line {i} is not '<sha256>  <name>': {line!r}")
        table[m.group(2)] = m.group(1)
    return table


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="normalize_fab.py", description=__doc__.split("\n\n")[0])
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--root")
    ap.add_argument("--write")
    group = ap.add_mutually_exclusive_group()
    group.add_argument("--sums")
    group.add_argument("--check")
    ap.add_argument("--quiet", action="store_true", help="no per-file lines on standard error")
    try:
        args = ap.parse_args(argv)
    except SystemExit as exc:
        return 2 if exc.code else 0
    log = (lambda _m: None) if args.quiet else (lambda m: print(m, file=sys.stderr))
    try:
        if not args.paths:
            raise UsageError("no input path")
        skip = {os.path.abspath(p) for p in (args.sums, args.check) if p}
        pairs = collect(args.paths, args.root, skip)
        if not pairs:
            raise UsageError("no file to list")
        rows = entries(pairs, args.write, log)
        if args.check:
            try:
                with open(args.check, encoding="utf-8") as fh:
                    stored = parse_sums(fh.read())
            except OSError as exc:
                raise UsageError(f"cannot read {args.check}: {exc}") from exc
            now = dict(rows)
            diffs = []
            for name in sorted(set(stored) | set(now)):
                if name not in now:
                    diffs.append(f"MISSING {name}")
                elif name not in stored:
                    diffs.append(f"ADDED {name}")
                elif stored[name] != now[name]:
                    diffs.append(f"CHANGED {name}")
            sys.stdout.write(format_sums(rows))
            for d in diffs:
                print(f"normalize_fab: {d}", file=sys.stderr)
            print(f"normalize_fab: check {'FAIL' if diffs else 'PASS'}: {len(now)} listed, "
                  f"{len(diffs)} difference(s) against {args.check}", file=sys.stderr)
            return 1 if diffs else 0
        text = format_sums(rows)
        sys.stdout.write(text)
        if args.sums:
            with open(args.sums, "w", encoding="utf-8") as fh:
                fh.write(text)
        return 0
    except (UsageError, OSError) as exc:
        print(f"normalize_fab: error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
