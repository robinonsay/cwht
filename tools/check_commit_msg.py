#!/usr/bin/env python3
"""Commit-message and trailer check of the CM plan (05 section 4.5 "Commit message" and "Checks"; TV-019).

Rules (each finding is FAIL unless marked WARN):
  SUBJECT             the first line is "<type>(<scope>): <summary>" with type one of feat, fix,
                      docs, test, tool, hw, sim, editorial, release, baseline, chore, or merge
                      (05 section 4.5 "Merges to main": merge(CR-NNN) or merge(<slug>)); a merge
                      commit must use type merge and a non-merge commit must not
  REFS_MISSING        the commit touches a file of a Table 4-1 row (a CI) and has no Refs: trailer
  REFS_UNRECOGNIZED   the Refs: trailer names no identifier of 05 section 4.5 or charter section 6
                      (REQ, TC, ICD, ADR, TS, RSK, HZ, NCR, RFA, RID, SI, TV, CR, INSP, MSR, NGO,
                      MOE, MOP, TPM, OPS, CON, CS, OQ, ACC, WP-SW, SW-NN sprint, FW-vX.Y.Z,
                      HW-MB-rev<X>-<n>, ME-ENC-rev<X>-<n>, CWHT-A-NNN, or a review name); other
                      tokens (for example WP-PDR-07) may accompany a recognized one
  CR_TRAILER_MISSING  the commit touches a file of a class-CR row whose CR-from event occurred
                      before the commit (baseline/<gate> tag, or a release/FW-* tag, reachable
                      from the commit's first parent) and has neither a CR: CR-NNN nor an
                      Editorial: trailer; a merge whose subject is merge(CR-NNN) satisfies it;
                      for the tools row (Table 4-1 row 28, CR from "date of the tool's TV
                      record") the rule applies to the tool files an Accredited row of the
                      docs/cm/tool-validation/README.md index names ("Accreditation puts the
                      tool under CR control")
  CR_ID_BAD           a CR: trailer value is not CR-NNN
  MIXED_ROW (WARN)    a file of a Mixed row whose CR-from event occurred is touched without CR:
                      or Editorial: (its Notes say which parts are CR-controlled; a reviewer decides)
  SPLIT_CR_FROM (WARN) the same for a row whose CR-from cell names more than one gate
Not checked: Co-Authored-By (whether an agent wrote the commit is not visible in git).
Trailers are parsed by git itself (git interpret-trailers --parse, TV-009), so a Refs: line that
git does not read as a trailer (for example one separated from the trailer block by a blank
line) counts as missing. Table 4-1 is read from docs/process/05-configuration-and-data-management.md
through tools/csa.py (TV-018).

Usage (from the repository root, or with --root):
    .venv/bin/python tools/check_commit_msg.py MSGFILE
        hook mode: the commit-msg hook argument; files from git diff --cached --name-only, Table
        4-1 and tags as of HEAD (the parent of the commit being made)
    .venv/bin/python tools/check_commit_msg.py --range A..B
        audit mode (05 section 4.5 "Checks"): every commit of the range, Table 4-1 at B
    .venv/bin/python tools/check_commit_msg.py --message-file MSGFILE --files PATH... [--parent REV]
        check a message against an explicit file list (tests and dry runs)

Hook install (owner action; this tool never installs itself): from the repository root,
    printf '#!/bin/sh\\nexec .venv/bin/python tools/check_commit_msg.py "$1"\\n' > .git/hooks/commit-msg
    chmod 755 .git/hooks/commit-msg
Exit status: 0 no FAIL finding (WARN findings allowed); 1 at least one FAIL finding; 2 usage
error or a git failure.
"""
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import csa  # noqa: E402

TYPES = ("feat", "fix", "docs", "test", "tool", "hw", "sim", "editorial", "release", "baseline", "chore", "merge")
SUBJECT_RE = re.compile(r"^(?P<type>[a-z]+)\((?P<scope>[^()\s][^()]*)\): \S")
REVIEW = r"(?:SRR|PDR|CDR|TRR|TRR-D[1-9][0-9]?|SAR)"
RECOGNIZED = re.compile("^(?:" + "|".join([
    r"REQ-(?:SYS|RX|TX|PWR|CTL|ME|SW|SW-[A-Z0-9]+)-[0-9]{3}",
    r"TC-(?:SYS|RX|TX|PWR|CTL|ME|SW|SW-[A-Z0-9]+|VAL|ATP|SW-COV|SW-REG|SW-TOOL)-[0-9]{3}",
    r"ICD-[A-Z]+-[A-Z]+", r"(?:ADR|TS|RSK|HZ|NCR|SI|TV|CR|INSP|NGO|MOE|MOP|TPM|OPS|CON)-[0-9]{3}",
    rf"(?:RFA|RID)-{REVIEW}-[0-9]{{3}}", r"(?:MSR|CS)-[0-9]{2}", r"OQ-[A-Z]+-[0-9]{3}", r"ACC-[A-Z0-9]+-[0-9]{3}",
    r"WP-SW-[0-9]{2}", r"SW-[0-9]{2}-[a-z0-9-]+", r"FW-v[0-9]+\.[0-9]+\.[0-9]+(?:-rc[0-9]+)?",
    r"(?:HW-MB|ME-ENC)-rev[A-Z]-[0-9]+", r"CWHT-A-[0-9]{3}", REVIEW,
]) + ")$")
CI_KINDS_FAIL = ("REFS_MISSING", "CR_TRAILER_MISSING")


class Context:
    """Table 4-1, tags and accredited tool paths, evaluated per parent commit."""

    def __init__(self, root: str, table: list):
        self.root = root
        self.table = table
        self._tags = None
        self._accredited: dict[str, set[str]] = {}

    def git(self, *args, check=True) -> str:
        r = subprocess.run(["git", "-C", self.root, *args], capture_output=True, text=True)
        if check and r.returncode != 0:
            raise csa.CsaError(f"git {' '.join(args[:4])} failed: {r.stderr.strip()}")
        return r.stdout

    def tags(self) -> list[tuple[str, str]]:
        if self._tags is None:
            self._tags = []
            for line in self.git("for-each-ref", "--format=%(refname:short) %(objectname) %(*objectname)", "refs/tags/").splitlines():
                parts = line.split()
                self._tags.append((parts[0], parts[2] if len(parts) > 2 else parts[1]))
        return self._tags

    def _ancestor(self, a: str, b: str) -> bool:
        return subprocess.run(["git", "-C", self.root, "merge-base", "--is-ancestor", a, b], capture_output=True).returncode == 0

    def event_before(self, row, parent: str | None) -> tuple[bool | None, bool]:
        """(occurred at parent, split) for a CR or Mixed row; (None, False) otherwise."""
        if row.cls not in ("CR", "Mixed") or parent is None:
            return None, False
        if "release/FW-" in row.cr_from:
            return any(n.startswith("release/FW-") and self._ancestor(c, parent) for n, c in self.tags()), False
        if "TV record" in row.cr_from:
            return None, False
        gates = re.findall(r"\b(SRR|PDR|CDR|TRR|SAR)\b", row.cr_from)
        if not gates:
            return None, False
        name = f"baseline/{gates[0].lower()}"
        return any(n == name and self._ancestor(c, parent) for n, c in self.tags()), len(set(gates)) > 1

    def accredited_tools(self, parent: str | None) -> set[str]:
        key = parent or ""
        if key not in self._accredited:
            text = ""
            if parent:
                text = self.git("show", f"{parent}:docs/cm/tool-validation/README.md", check=False)
            paths = set()
            for line in text.splitlines():
                if line.startswith("| [TV-") and "**Accredited**" in line:
                    cells = csa.split_cells(line)
                    paths.update(re.findall(r"`(tools/[^`\s]+)`", cells[1] if len(cells) > 1 else ""))
            self._accredited[key] = paths
        return self._accredited[key]


def parse_trailers(root: str, message: str) -> list[tuple[str, str]]:
    r = subprocess.run(["git", "-C", root, "interpret-trailers", "--parse"], input=message, capture_output=True, text=True)
    if r.returncode != 0:
        raise csa.CsaError(f"git interpret-trailers failed: {r.stderr.strip()}")
    out = []
    for line in r.stdout.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            out.append((k.strip(), v.strip()))
    return out


def clean_message(text: str) -> str:
    """git's default cleanup for an editor message: drop comment lines and trailing blank lines."""
    return "\n".join(line for line in text.splitlines() if not line.startswith("#")).strip() + "\n"


def evaluate(ctx: Context, message: str, files: list[str], parent: str | None, is_merge: bool | None) -> dict:
    lines = message.strip().splitlines()
    subject = lines[0] if lines else ""
    trailers = parse_trailers(ctx.root, message)
    refs = [t.strip() for k, v in trailers if k.lower() == "refs" for t in v.split(",") if t.strip()]
    crs = [v for k, v in trailers if k.lower() == "cr"]
    editorial = "; ".join(v for k, v in trailers if k.lower() == "editorial")
    findings = []

    def add(level, rule, msg):
        findings.append({"level": level, "rule": rule, "message": msg})

    m = SUBJECT_RE.match(subject)
    if not m or m.group("type") not in TYPES:
        add("FAIL", "SUBJECT", f"first line {subject[:72]!r} is not '<type>(<scope>): <summary>' with a 05 section 4.5 type")
    elif is_merge is True and m.group("type") != "merge":
        add("FAIL", "SUBJECT", "a merge commit's first line is merge(CR-NNN): or merge(<slug>): (05 section 4.5)")
    elif is_merge is False and m.group("type") == "merge":
        add("FAIL", "SUBJECT", "type merge on a commit that is not a merge")
    merge_cr = bool(m and m.group("type") == "merge" and re.fullmatch(r"CR-[0-9]{3}", m.group("scope")))
    rows, unmatched = set(), []
    cr_rows, warn_rows = set(), {}
    accredited = ctx.accredited_tools(parent)
    for f in files:
        num, _ = csa.match_row(f, ctx.table)
        if num is None:
            unmatched.append(f)
            continue
        rows.add(num)
        row = ctx.table[num - 1]
        if "TV record" in row.cr_from and f in accredited:
            cr_rows.add(num)
            continue
        occurred, split = ctx.event_before(row, parent)
        if not occurred:
            continue
        if row.cls == "Mixed":
            warn_rows.setdefault(num, "MIXED_ROW")
        elif split:
            warn_rows.setdefault(num, "SPLIT_CR_FROM")
        else:
            cr_rows.add(num)
    if rows and not refs:
        add("FAIL", "REFS_MISSING", f"touches rows {', '.join(map(str, sorted(rows)))} and has no Refs: trailer")
    elif refs and not any(RECOGNIZED.match(r) for r in refs):
        add("FAIL", "REFS_UNRECOGNIZED", f"Refs: {', '.join(refs)} names no identifier of 05 section 4.5 or charter section 6")
    for v in crs:
        if not re.fullmatch(r"CR-[0-9]{3}", v):
            add("FAIL", "CR_ID_BAD", f"CR: {v!r} is not CR-NNN")
    has_cr = any(re.fullmatch(r"CR-[0-9]{3}", v) for v in crs) or merge_cr
    if cr_rows and not (has_cr or editorial):
        add("FAIL", "CR_TRAILER_MISSING", f"touches class-CR rows {', '.join(map(str, sorted(cr_rows)))} after their CR-from event "
                                          "without a CR: or Editorial: trailer")
    for num, rule in sorted(warn_rows.items()):
        if not (has_cr or editorial):
            add("WARN", rule, f"row {num} ({ctx.table[num - 1].cls}, CR from {ctx.table[num - 1].cr_from}) touched without CR: or Editorial:")
    return {"subject": subject, "rows": sorted(rows), "unmatched": unmatched, "refs": refs, "cr": crs,
            "editorial": editorial, "findings": findings}


def check_commit(root: str, sha: str, table: list, ctx: Context | None = None) -> dict:
    ctx = ctx or Context(root, table)
    parents = ctx.git("rev-list", "--parents", "-n", "1", sha).split()[1:]
    message = ctx.git("log", "-1", "--format=%B", sha)
    parent = parents[0] if parents else None
    if parent:
        files = ctx.git("diff", "--name-only", "--no-renames", parent, sha).split("\n")
    else:
        files = ctx.git("show", "--name-only", "--format=", sha).split("\n")
    info = evaluate(ctx, message, [f for f in files if f], parent, len(parents) > 1)
    info.update({"sha": ctx.git("rev-parse", sha).strip(), "short": ctx.git("rev-parse", "--short=7", sha).strip()})
    return info


def report(label: str, info: dict) -> int:
    fails = [f for f in info["findings"] if f["level"] == "FAIL"]
    for f in info["findings"]:
        print(f"{f['level']} {f['rule']} {label}: {f['message']}")
    if not info["findings"]:
        print(f"PASS {label}: rows {', '.join(map(str, info['rows'])) or 'none'}; Refs: {', '.join(info['refs']) or 'none'}")
    return 1 if fails else 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="check_commit_msg.py", description="05 section 4.5 commit-message check (TV-019)")
    ap.add_argument("msgfile", nargs="?")
    ap.add_argument("--root", default=None)
    ap.add_argument("--range", dest="range_")
    ap.add_argument("--message-file")
    ap.add_argument("--files", nargs="*")
    ap.add_argument("--parent")
    try:
        args = ap.parse_args(argv)
    except SystemExit as exc:
        return 2 if exc.code else 0
    modes = [bool(args.msgfile), bool(args.range_), bool(args.message_file)]
    if sum(modes) != 1 or (args.files is not None and not args.message_file):
        print("check_commit_msg: error: give exactly one of MSGFILE, --range A..B, or --message-file F --files ...", file=sys.stderr)
        return 2
    try:
        root = args.root or subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True, check=True).stdout.strip()
        git = csa.Git(root)
        if args.range_:
            end = args.range_.split("..", 1)[1] if ".." in args.range_ else args.range_
            table = csa.parse_table41(git.show(end or "HEAD", csa.CM_PLAN) or "")
            ctx = Context(root, table)
            shas = git.run("rev-list", "--reverse", args.range_).split()
            status = 0
            for sha in shas:
                info = check_commit(root, sha, table, ctx)
                status |= report(info["short"], info)
            print(f"check_commit_msg: {len(shas)} commit(s) in {args.range_}; {'FAIL' if status else 'PASS'}")
            return status
        path = args.msgfile or args.message_file
        try:
            with open(path, encoding="utf-8") as fh:
                message = clean_message(fh.read())
        except OSError as exc:
            print(f"check_commit_msg: error: cannot read {path}: {exc}", file=sys.stderr)
            return 2
        if args.message_file:
            files = args.files or []
            parent = args.parent
            table_text = git.show(parent or "HEAD", csa.CM_PLAN)
        else:
            files = [f for f in git.run("diff", "--cached", "--name-only", "--no-renames").split("\n") if f]
            parent = git.run("rev-parse", "--verify", "--quiet", "HEAD", check=False).strip() or None
            # Table 4-1 as staged: the index version of the CM plan (":path").
            table_text = git.run("show", f":{csa.CM_PLAN}", check=False)
        table = csa.parse_table41(table_text or "")
        is_merge = os.path.exists(os.path.join(root, ".git", "MERGE_HEAD")) if args.msgfile else None
        info = evaluate(Context(root, table), message, files, parent, is_merge)
        return report(os.path.basename(path), info)
    except (csa.CsaError, subprocess.CalledProcessError) as exc:
        print(f"check_commit_msg: error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
