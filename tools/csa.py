#!/usr/bin/env python3
"""Configuration status accounting report generator (CM plan 05 section 6; SWE-083; TV-018).

Writes the CSA report of 05 section 6 (items 1 to 13) from the sources that section names, all
read at one git revision (default HEAD), so the report is reproducible from the commit alone:

  1 Header            git rev-parse, git ls-tree, the latest baseline/* tag, CR front matter
  2 CI status         05 Table 4-1 parsed from docs/process/05-configuration-and-data-management.md
                      at the revision; every tracked file matched by the 05 section 4.2 rule; per
                      row the file count, hash, last commit, applied and pending CRs, the INSP
                      records that name its files, and the level by the rule below; then the
                      tracked files that match no row and the files that match two rows equally
  3 Baselines         git for-each-ref refs/tags/baseline/; signature presence from the tag object;
                      pushed state only with --remote (git ls-remote), otherwise "not checked"
  4 CR register       the front matter of docs/cm/cr/CR-*.md; missing numbers are listed
  5 Editorial log     commits of <since>..<rev> with an Editorial: trailer
  6 Change log        every commit of <since>..<rev>: first line, rows touched, Refs: trailer,
                      and the trailer findings of tools/check_commit_msg.py (rules R1 and R2)
  7 Release register  release/* tags, firmware/releases/ and hardware/releases/
  8 Audit register    docs/reviews/SAR/configuration-audit.md and firmware/releases/*/configuration-audit.md
  9 Tool accreditation the index table of docs/cm/tool-validation/README.md, copied
 10 Metrics           the four metrics of 05 Table 6-1 (MSR-02 copied from docs/plan/measurements.json)
 11 Deviations        the Entries and Closures tables of docs/cm/deviations.md, copied
 12 Waivers           <a id="W<n>"> anchors of docs/reviews/*/decision-memo.md; CRs whose
                      disposition is "Approved (waiver)"
 13 Open items        tbr objects in the requirement, expectation, TPM and hazard files (hazard:
                      each control holding a tbr field), and the open items of every
                      docs/reviews/*/rfa-rid-log.json

Records: an INSP record names a file when the file is one of its product_files (path@blob, inline
or YAML block list) or the first word of a comma-separated item of its product, or lies under a
directory so named ("firmware/").

Level rule (05 section 4.1), per row: "none (absent)" without files; L3 for a Record (level L3)
row when a release/* tag exists; for a CR or Mixed row, L2 when its CR-from event has occurred
at the revision (the first gate named in the CR-from cell has its baseline/<gate> tag, or a
release/FW-* tag exists for "first release/FW-* tag"); otherwise L1 when an INSP record whose
verdict is APPROVED names a file of the row in product or product_files; otherwise L0. A CR-from
cell naming two gates, or row 28 ("date of the tool's TV record"), is marked as split. The rule
is mechanical: judgments a hand CSA adds (sub-row levels, notes) are not reproduced.

Usage (from the repository root, or with --root):
    .venv/bin/python tools/csa.py [--rev REV] [--since REF] [--date YYYY-MM-DD] [--remote]
                                   [--write | --output PATH | --check PATH] [--json PATH] [--strict]

Output goes to standard output unless --write (docs/process/configuration-status.md), --output
PATH or --check PATH (regenerate and compare, exit 1 on a difference) is given. --json writes the
derived data model. --since defaults to the latest baseline/* tag reachable from REV. --date
defaults to today. Exit status: 0 success; 1 --check found a difference, or --strict and a
tracked file matches no row or two rows; 2 usage error or a git or parse failure.
Standard library and git only (TV-009).
"""
from __future__ import annotations

import argparse
import dataclasses
import datetime as dt
import fnmatch
import json
import os
import re
import subprocess
import sys

CM_PLAN = "docs/process/05-configuration-and-data-management.md"
CSA_PATH = "docs/process/configuration-status.md"
GATES = ("SRR", "PDR", "CDR", "TRR", "SAR")
OPEN_CR_STATES = ("Draft", "Submitted", "Assessed", "Deferred")


class CsaError(Exception):
    """Exit status 2."""


# --------------------------------------------------------------------------- git helpers
class Git:
    def __init__(self, root: str):
        self.root = root

    def run(self, *args: str, check: bool = True) -> str:
        r = subprocess.run(["git", "-C", self.root, *args], capture_output=True, text=True)
        if check and r.returncode != 0:
            raise CsaError(f"git {' '.join(args[:4])} failed: {r.stderr.strip()}")
        return r.stdout

    def show(self, rev: str, path: str) -> str | None:
        r = subprocess.run(["git", "-C", self.root, "show", f"{rev}:{path}"], capture_output=True, text=True)
        return r.stdout if r.returncode == 0 else None

    def blobs(self, rev: str) -> dict[str, str]:
        out = {}
        for line in self.run("ls-tree", "-r", "-z", rev).split("\0"):
            if not line:
                continue
            meta, path = line.split("\t", 1)
            mode, kind, sha = meta.split()
            if kind == "blob":
                out[path] = sha
        return out


# --------------------------------------------------------------------------- Table 4-1
@dataclasses.dataclass
class CiRow:
    num: int
    ci: str
    specs: list[str]
    cls: str
    cr_from: str
    notes: str


def split_cells(line: str) -> list[str]:
    return [c.strip() for c in re.split(r"(?<!\\)\|", line.strip())[1:-1]]


def pathspecs(cell: str) -> list[str]:
    """Backticked pathspecs outside parentheses (text in parentheses gives examples or notes)."""
    specs, depth, i = [], 0, 0
    while i < len(cell):
        ch = cell[i]
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth = max(0, depth - 1)
        elif ch == "`":
            j = cell.find("`", i + 1)
            if j < 0:
                break
            token = cell[i + 1:j]
            if depth == 0 and token and " " not in token:
                specs.append(token)
            i = j
        i += 1
    return specs


def parse_table41(text: str) -> list[CiRow]:
    rows, inside = [], False
    for line in text.splitlines():
        if line.startswith("| # | CI | Pathspec |"):
            inside = True
            continue
        if not inside:
            continue
        if not line.startswith("|"):
            if rows:
                break
            continue
        if re.match(r"^\|\s*-", line):
            continue
        cells = split_cells(line)
        if len(cells) != 7 or not cells[0].isdigit():
            raise CsaError(f"Table 4-1 row not understood: {line[:80]}")
        rows.append(CiRow(int(cells[0]), cells[1], pathspecs(cells[2]), cells[4], cells[5], cells[6]))
    if not rows:
        raise CsaError(f"Table 4-1 not found in {CM_PLAN}")
    nums = [r.num for r in rows]
    if nums != list(range(1, len(rows) + 1)):
        raise CsaError(f"Table 4-1 rows are not numbered 1 to {len(rows)} in order")
    return rows


def spec_matches(spec: str, path: str) -> tuple[bool, bool, int]:
    """(matches, is_prefix, prefix length). A trailing / is a directory prefix; otherwise fnmatch
    in which * also matches / (05 section 4.2)."""
    if spec.endswith("/"):
        return path.startswith(spec), True, len(spec)
    return fnmatch.fnmatchcase(path, spec), False, 0


def match_row(path: str, rows: list[CiRow]) -> tuple[int | None, list[int]]:
    """Row number by the 05 section 4.2 rule, and the rows tied with it (empty when unique)."""
    explicit, prefixes = set(), {}
    for r in rows:
        for s in r.specs:
            ok, is_prefix, n = spec_matches(s, path)
            if ok and is_prefix:
                prefixes[r.num] = max(prefixes.get(r.num, 0), n)
            elif ok:
                explicit.add(r.num)
    if explicit:
        best = sorted(explicit)
        return best[0], best if len(best) > 1 else []
    if prefixes:
        top = max(prefixes.values())
        best = sorted(n for n, v in prefixes.items() if v == top)
        return best[0], best if len(best) > 1 else []
    return None, []


# --------------------------------------------------------------------------- front matter
def front_matter(text: str) -> dict:
    """Subset YAML reader for the flat front matter of CR files and peer-review records."""
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end < 0:
        return {}
    out, last = {}, None
    for line in text[4:end].splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        item = re.match(r"^\s+-\s+(.*)$", line)
        if item and last is not None:
            # YAML block list under the last key ("key:" then "  - value" lines)
            if not isinstance(out.get(last), list):
                out[last] = []
            out[last].append(scalar(item.group(1).strip()))
            continue
        if line.startswith((" ", "\t")):
            continue
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", line)
        if not m:
            last = None
            continue
        key, raw = m.group(1), m.group(2).strip()
        raw = re.sub(r"\s+#\s.*$", "", raw) if not raw.startswith(("'", '"')) else raw
        out[key] = scalar(raw)
        last = key
    return out


def scalar(raw: str):
    if raw.startswith("[") and raw.endswith("]"):
        inner = raw[1:-1].strip()
        if not inner:
            return []
        return [scalar(x.strip()) for x in re.findall(r'"[^"]*"|\'[^\']*\'|[^,]+', inner)]
    if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in "'\"":
        return raw[1:-1]
    if raw in ("null", "~", ""):
        return None
    if re.fullmatch(r"-?[0-9]+", raw):
        return int(raw)
    return raw


# --------------------------------------------------------------------------- model
@dataclasses.dataclass
class RowStatus:
    num: int
    ci: str
    cls: str
    cr_from: str
    level: str
    files: int
    hash: str
    last_commit: str
    applied_crs: list[str]
    pending_crs: list[str]
    records: list[str]


def names_any(record: dict, files: list[str]) -> bool:
    """True when an INSP record names one of the files, exactly or by a directory product ("firmware/")."""
    return any(f in record["named"] or any(f.startswith(p) for p in record["prefixes"]) for f in files)


def short(sha: str | None, n: int = 12) -> str:
    return sha[:n] if sha else "n/a"


class Csa:
    def __init__(self, root: str, rev: str, since: str | None, date: str, remote: bool):
        self.git = Git(root)
        self.rev_input = rev
        self.rev = self.git.run("rev-parse", "--verify", f"{rev}^{{commit}}").strip()
        self.date = date
        self.remote = remote
        self.blobs = self.git.blobs(self.rev)
        text = self.git.show(self.rev, CM_PLAN)
        if text is None:
            raise CsaError(f"{CM_PLAN} not found at {rev}")
        self.table = parse_table41(text)
        self.tags = self._tags()
        self.since = since or self._latest_baseline()
        self.crs = self._crs()
        self.records = self._records()

    # -- sources
    def _tags(self) -> list[dict]:
        out = []
        fmt = "%(refname:short)%00%(objecttype)%00%(objectname)%00%(*objectname)%00%(creatordate:iso-strict)"
        for line in self.git.run("for-each-ref", f"--format={fmt}", "refs/tags/").splitlines():
            name, kind, obj, peeled, date = line.split("\0")
            commit = peeled or obj
            reachable = subprocess.run(["git", "-C", self.git.root, "merge-base", "--is-ancestor", commit, self.rev],
                                       capture_output=True).returncode == 0
            out.append({"name": name, "type": kind, "object": obj, "commit": commit, "date": date, "reachable": reachable})
        return out

    def _latest_baseline(self) -> str | None:
        cands = [t for t in self.tags if t["name"].startswith("baseline/") and t["reachable"]]
        return sorted(cands, key=lambda t: t["date"])[-1]["name"] if cands else None

    def gate_occurred(self, gate: str) -> bool:
        return any(t["name"] == f"baseline/{gate.lower()}" and t["reachable"] for t in self.tags)

    def release_fw_exists(self) -> bool:
        return any(t["name"].startswith("release/FW-") and t["reachable"] for t in self.tags)

    def _crs(self) -> list[dict]:
        out = []
        for path in sorted(p for p in self.blobs if re.fullmatch(r"docs/cm/cr/CR-[0-9]{3}-[^/]+\.md", p)):
            fm = front_matter(self.git.show(self.rev, path) or "")
            fm["path"] = path
            out.append(fm)
        return out

    def _records(self) -> list[dict]:
        out = []
        for path in sorted(p for p in self.blobs if re.fullmatch(r"docs/reviews/[^/]+/checklists/[^/]+\.md", p)):
            fm = front_matter(self.git.show(self.rev, path) or "")
            if not str(fm.get("id", "")).startswith("INSP-"):
                continue
            named, prefixes = set(), []
            product = fm.get("product")
            tokens = [t.strip().split()[0] for t in product.split(",") if t.strip()] if isinstance(product, str) else []
            files = fm.get("product_files") if isinstance(fm.get("product_files"), list) else []
            tokens += [str(v).split("@", 1)[0].strip() for v in files if v]
            for t in tokens:
                if t.endswith("/"):
                    prefixes.append(t)
                else:
                    named.add(t)
            out.append({"id": fm["id"], "path": path, "verdict": fm.get("verdict"), "named": named, "prefixes": prefixes})
        return out

    # -- item 2
    def matching(self) -> tuple[dict[int, list[str]], list[str], list[tuple[str, list[int]]]]:
        by_row: dict[int, list[str]] = {r.num: [] for r in self.table}
        unmatched, ties = [], []
        for path in sorted(self.blobs):
            num, tied = match_row(path, self.table)
            if num is None:
                unmatched.append(path)
                continue
            if tied:
                ties.append((path, tied))
            by_row[num].append(path)
        return by_row, unmatched, ties

    def cr_event(self, row: CiRow) -> tuple[bool | None, bool]:
        """(occurred, split). None when the row has no CR-from event (Log, Record)."""
        if row.cls not in ("CR", "Mixed"):
            return None, False
        text = row.cr_from
        if "release/FW-" in text:
            return self.release_fw_exists(), False
        if "TV record" in text:
            return None, True
        gates = [g for g in re.findall(r"\b(SRR|PDR|CDR|TRR|SAR)\b", text)]
        if not gates:
            return None, False
        return self.gate_occurred(gates[0]), len(set(gates)) > 1

    def row_hash(self, row: CiRow, files: list[str]) -> str:
        if not files:
            return "n/a"
        if len(files) == 1:
            return f"`{files[0]}` `{short(self.blobs[files[0]])}`"
        covering = sorted((s for s in row.specs if s.endswith("/") and all(f.startswith(s) for f in files)), key=len)
        if covering:
            tree = self.git.run("rev-parse", f"{self.rev}:{covering[0].rstrip('/')}").strip()
            return f"`{covering[0]}` tree `{short(tree)}`"
        parts = []
        for s in row.specs:
            members = [f for f in files if spec_matches(s, f)[0]]
            if not members:
                continue
            if s.endswith("/") and all(f.startswith(s) for f in members):
                tree = self.git.run("rev-parse", f"{self.rev}:{s.rstrip('/')}").strip()
                parts.append(f"`{s}` tree `{short(tree)}`")
            elif len(members) == 1:
                parts.append(f"`{members[0]}` `{short(self.blobs[members[0]])}`")
            else:
                parts.append(f"`{s}`: " + ", ".join(f"`{m}` `{short(self.blobs[m])}`" for m in members))
        return "; ".join(parts)

    def last_commit(self, files: list[str]) -> str:
        if not files:
            return "n/a"
        out = self.git.run("log", "-1", "--format=%h %cs", self.rev, "--", *files).strip()
        return f"`{out.split()[0]}` {out.split()[1]}" if out else "n/a"

    def row_status(self) -> tuple[list[RowStatus], list[str], list[tuple[str, list[int]]]]:
        by_row, unmatched, ties = self.matching()
        release_any = any(t["name"].startswith("release/") and t["reachable"] for t in self.tags)
        out = []
        for row in self.table:
            files = by_row[row.num]
            occurred, split = self.cr_event(row)
            recs = sorted({r["id"] for r in self.records if names_any(r, files)}, key=lambda x: int(x[5:]))
            approved = any(r["verdict"] == "APPROVED" and names_any(r, files) for r in self.records)
            if not row.specs:
                level = "n/a (no pathspec: outside the repository)"
            elif not files:
                level = "none (absent)"
            elif "L3" in row.cls and release_any:
                level = "L3"
            elif occurred:
                level = "L2"
            else:
                level = "L1" if approved else "L0"
            if split:
                level += " (split CR-from: " + row.cr_from + ")"
            applied = [c["id"] for c in self.crs if row.num in (c.get("affected_cis") or [])
                       and str(c.get("disposition") or "").startswith("Approved")]
            pending = [c["id"] for c in self.crs if row.num in (c.get("affected_cis") or []) and c.get("status") in OPEN_CR_STATES]
            out.append(RowStatus(row.num, row.ci, row.cls, row.cr_from, level, len(files), self.row_hash(row, files),
                                 self.last_commit(files), applied, pending, recs))
        return out, unmatched, ties

    # -- item 6
    def commits(self) -> list[dict]:
        import check_commit_msg
        span = f"{self.since}..{self.rev}" if self.since else self.rev
        ctx = check_commit_msg.Context(self.git.root, self.table)
        return [check_commit_msg.check_commit(self.git.root, sha, self.table, ctx)
                for sha in self.git.run("rev-list", "--reverse", span).split()]

    # -- item 12
    def waivers(self) -> list[tuple[str, str]]:
        out = []
        for path in sorted(p for p in self.blobs if re.fullmatch(r"docs/reviews/[^/]+/decision-memo\.md", p)):
            for m in re.finditer(r'<a id="(W[0-9]+)"></a>([^|\n]*)', self.git.show(self.rev, path) or ""):
                out.append((f"{path}#{m.group(1)}", m.group(2).strip()))
        for c in self.crs:
            if str(c.get("disposition") or "") == "Approved (waiver)":
                out.append((c["id"], str(c.get("title", ""))))
        return out

    # -- item 13
    def tbrs(self) -> list[tuple[str, str, dict]]:
        out = []
        for path in sorted(p for p in self.blobs if re.fullmatch(r"docs/requirements/(.+/)?requirements\.json", p)):
            data = json.loads(self.git.show(self.rev, path) or "{}")
            items = data.get("requirements", []) if isinstance(data, dict) else []
            out.append(("requirements", path, self._count_tbr(items, len(items))))
        exp = "docs/requirements/l0-stakeholder/expectations.json"
        if exp in self.blobs:
            data = json.loads(self.git.show(self.rev, exp))
            items = [x for k in ("stakeholders", "ngos", "moes", "constraints") for x in data.get(k, []) if isinstance(x, dict)]
            out.append(("expectations", exp, self._count_tbr(items, len(items))))
        tpm = "docs/plan/tpm.json"
        if tpm in self.blobs:
            items = json.loads(self.git.show(self.rev, tpm)).get("tpms", [])
            out.append(("TPMs", tpm, self._count_tbr(items, len(items))))
        hz = "docs/safety/hazards.json"
        if hz in self.blobs:
            controls = [dict(k, id=f"{h['id']} {k.get('id')}") for h in json.loads(self.git.show(self.rev, hz)).get("hazards", [])
                        for k in h.get("controls", [])]
            out.append(("hazard controls", hz, self._count_tbr(controls, len(controls))))
        return out

    @staticmethod
    def _count_tbr(items: list[dict], total: int) -> dict:
        by_close: dict[str, list[str]] = {}
        for x in items:
            t = x.get("tbr")
            for obj in (t if isinstance(t, list) else [t] if t else []):
                close = obj.get("close_by", "none") if isinstance(obj, dict) else "none"
                by_close.setdefault(str(close), []).append(str(x.get("id")))
        return {"items": total, "by_close_by": {k: len(v) for k, v in sorted(by_close.items())},
                "ids": {k: v for k, v in sorted(by_close.items())}}

    def open_log_items(self) -> list[dict]:
        out = []
        for path in sorted(p for p in self.blobs if re.fullmatch(r"docs/reviews/[^/]+/rfa-rid-log\.json", p)):
            data = json.loads(self.git.show(self.rev, path) or "{}")
            for it in data.get("items", []):
                if it.get("state") not in ("Closed", "Withdrawn"):
                    out.append({"log": path, "id": it.get("id"), "state": it.get("state"), "title": it.get("title", "")})
        return out

    # -- metrics
    def msr02(self) -> dict | None:
        p = "docs/plan/measurements.json"
        if p not in self.blobs:
            return None
        recs = [r for r in json.loads(self.git.show(self.rev, p)).get("records", []) if r.get("id") == "MSR-02"]
        return recs[-1] if recs else None


# --------------------------------------------------------------------------- rendering
def md_escape(s) -> str:
    return str(s).replace("|", "\\|").replace("\n", " ")


def days(a: str, b: str) -> int | None:
    try:
        return (dt.date.fromisoformat(b) - dt.date.fromisoformat(str(a))).days
    except (TypeError, ValueError):
        return None


def copy_table(text: str, heading: str) -> list[str]:
    lines, on = [], False
    for line in text.splitlines():
        if line.strip() == heading:
            on = True
            continue
        if on and line.startswith("#"):
            break
        if on and line.startswith("|"):
            lines.append(line)
    return lines


def build(csa: Csa) -> tuple[str, dict]:
    g = csa.git
    rows, unmatched, ties = csa.row_status()
    commits = csa.commits()
    head_short = csa.rev[:12]
    since = csa.since or "(root)"
    L: list[str] = []
    a = L.append
    a("# cwht Configuration Status Accounting Report")
    a("")
    a(f"**Status:** Log (Table 4-1 row 35 of `{CM_PLAN}`, called 05 below). Generated by `tools/csa.py` (05 §6) at revision "
      f"`{csa.rev}` on {csa.date}. Every value below is read at that revision; nothing in this file is edited by hand (05 §6).")
    a("")
    # 1
    a("## 1. Header")
    a("")
    csa_blob = csa.blobs.get("tools/csa.py")
    latest = [t for t in csa.tags if t["name"] == csa.since]
    merged = [c["id"] for c in csa.crs if c.get("merge_sha") and latest and subprocess.run(
        ["git", "-C", g.root, "merge-base", "--is-ancestor", latest[0]["commit"], str(c["merge_sha"])], capture_output=True).returncode == 0]
    a("| Field | Value |")
    a("|---|---|")
    a(f"| Generation date | {csa.date} |")
    a(f"| Revision | `{csa.rev}` (`{csa.rev_input}`) |")
    a(f"| Generator | `tools/csa.py` blob `{short(csa_blob)}` at the revision" if csa_blob else "| Generator | `tools/csa.py` (not in the revision: run from the working tree)")
    L[-1] += " |"
    a(f"| Tracked files | {len(csa.blobs)} (`git ls-tree -r {head_short}`) |")
    if latest:
        t = latest[0]
        a(f"| Current effective baseline | `{t['name']}` (tag object `{short(t['object'])}`, commit `{short(t['commit'])}`) plus merged CRs since the tag: "
          f"{', '.join(merged) if merged else 'none'} |")
        changed = [p for p in g.run("diff", "--name-only", t["commit"], csa.rev).split()]
        ctl = []
        for p in changed:
            num, _ = match_row(p, csa.table)
            if num is None:
                continue
            row = csa.table[num - 1]
            occurred, _ = csa.cr_event(row)
            if occurred:
                ctl.append(p)
        a(f"| Class-CR content changed since the tag (rows whose CR-from event has occurred) | {len(ctl)} file(s)"
          + (": " + ", ".join(f"`{p}`" for p in ctl[:20]) + (" ..." if len(ctl) > 20 else "") if ctl else "") + " |")
    else:
        a("| Current effective baseline | none (no baseline/* tag reachable) |")
    upstream = g.run("rev-parse", "--verify", "--quiet", "refs/remotes/origin/main", check=False).strip()
    if upstream:
        ahead = g.run("rev-list", "--count", f"{upstream}..{csa.rev}").strip()
        a(f"| Local revision against `origin/main` | `origin/main` is `{upstream[:7]}` (local ref, no network command); the revision is {ahead} commit(s) ahead |")
    a("")
    # 2
    a("## 2. CI status (Table 4-1)")
    a("")
    a("Level by the rule of the `tools/csa.py` docstring (05 §4.1). Records: the `INSP-NNN` records whose `product` or `product_files` name a file of the row. "
      "Applied CRs: CRs whose disposition is Approved and whose `affected_cis` list the row; pending: CRs in Draft, Submitted, Assessed or Deferred.")
    a("")
    a("| Row | CI | Class | CR from | Level | Files | Hash at the revision | Last commit | Applied CRs; pending CRs | Peer-review records |")
    a("|---|---|---|---|---|---|---|---|---|---|")
    for r in rows:
        a(f"| {r.num} | {md_escape(r.ci)} | {r.cls} | {md_escape(r.cr_from)} | {md_escape(r.level)} | {r.files} | {r.hash} | {r.last_commit} | "
          f"{', '.join(r.applied_crs) or 'none'}; {', '.join(r.pending_crs) or 'none'} | {', '.join(r.records) or 'none'} |")
    a("")
    a(f"**Tracked files that match no row (must be empty): {len(unmatched)}.**")
    a("")
    for p in unmatched:
        a(f"- `{p}`")
    if unmatched:
        a("")
    a(f"**Tracked files that match two rows with equal precedence: {len(ties)}.**")
    a("")
    for p, tied in ties:
        a(f"- `{p}`: rows {', '.join(map(str, tied))}")
    if ties:
        a("")
    # 3
    a("## 3. Baselines")
    a("")
    remote = {}
    if csa.remote:
        for line in g.run("ls-remote", "--tags", "origin").splitlines():
            sha, ref = line.split("\t")
            remote[ref.replace("refs/tags/", "")] = sha
    bl = [t for t in csa.tags if t["name"].startswith("baseline/")]
    if not bl:
        a("None: no `baseline/*` tag exists.")
    else:
        a("| Tag | Tag object | Tagged commit | Date | Decision memo | Signed | Pushed |")
        a("|---|---|---|---|---|---|---|")
        for t in bl:
            body = g.run("cat-file", "-p", t["object"]) if t["type"] == "tag" else ""
            signed = "yes" if re.search(r"-----BEGIN (PGP|SSH) SIGNATURE-----", body) else "no"
            memo = f"docs/reviews/{t['name'].split('/', 1)[1].upper()}/decision-memo.md"
            memo_cell = f"`{memo}`" if memo in csa.blobs else "none at the revision"
            pushed = ("yes" if remote.get(t["name"]) == t["object"] else "no") if csa.remote else "not checked (run with --remote)"
            a(f"| `{t['name']}` | `{t['object']}` | `{t['commit']}` | {t['date']} | {memo_cell} | {signed} | {pushed} |")
    a("")
    # 4
    a("## 4. CR register")
    a("")
    a("Source: the front matter of each `docs/cm/cr/CR-NNN-*.md` at the revision.")
    a("")
    a("| CR | Title | Class | Status | Originator | Opened | Disposition | Dispositioned | Closed | Affected CIs (rows) | Target release | Merge SHA |")
    a("|---|---|---|---|---|---|---|---|---|---|---|---|")
    for c in csa.crs:
        a(f"| {c.get('id')} | {md_escape(c.get('title', ''))} | {c.get('class')} | {c.get('status')} | {c.get('originator')} | {c.get('date_opened')} | "
          f"{c.get('disposition') or 'none'} | {c.get('disposition_date') or 'not yet'} | {c.get('date_closed') or 'no'} | "
          f"{', '.join(map(str, c.get('affected_cis') or []))} | {c.get('target_release')} | {c.get('merge_sha') or 'null'} |")
    nums = sorted(int(str(c.get("id", "CR-0"))[3:]) for c in csa.crs if re.fullmatch(r"CR-[0-9]{3}", str(c.get("id"))))
    missing = [f"CR-{n:03d}" for n in range(1, (nums[-1] if nums else 0) + 1) if n not in nums]
    a("")
    a(f"Numbers with no CR file at the revision: {', '.join(missing) if missing else 'none'}.")
    a("")
    # 5
    a("## 5. Editorial log")
    a("")
    ed = [c for c in commits if c["editorial"]]
    a(f"Commits in `{since}..{head_short}` carrying an `Editorial:` trailer: **{len(ed) if ed else 'none'}**.")
    a("")
    for c in ed:
        a(f"- `{c['short']}` {md_escape(c['subject'])}: {md_escape(c['editorial'])} (rows {', '.join(map(str, c['rows'])) or 'none'})")
    if ed:
        a("")
    # 6
    a(f"## 6. Change log (`{since}..{head_short}`)")
    a("")
    a(f"{len(commits)} commit(s). Trailers are parsed by `git interpret-trailers --parse`; findings are those of `tools/check_commit_msg.py` "
      "(R1: `Refs:` missing on a commit that touches a CI; R2: a class-CR CI touched after its CR-from event without `CR:` or `Editorial:`).")
    a("")
    a("| Commit | First line | Rows touched | `Refs:` | Findings |")
    a("|---|---|---|---|---|")
    for c in commits:
        rows_cell = ", ".join(map(str, c["rows"])) or "none"
        if c["unmatched"]:
            rows_cell += f" (+{len(c['unmatched'])} file(s) in no row)"
        a(f"| `{c['short']}` | {md_escape(c['subject'])} | {rows_cell} | {md_escape(', '.join(c['refs'])) or 'none'} | "
          f"{md_escape('; '.join(f['level'] + ' ' + f['rule'] + ': ' + f['message'] for f in c['findings'])) or 'none'} |")
    a("")
    # 7
    a("## 7. Release register")
    a("")
    rel = [t for t in csa.tags if t["name"].startswith("release/")]
    rel_dirs = sorted({p.split("/")[0] + "/" + p.split("/")[1] + "/" for p in csa.blobs if p.startswith(("firmware/releases/", "hardware/releases/"))})
    if not rel and not rel_dirs:
        a("None: no `release/*` tag exists and neither `firmware/releases/` nor `hardware/releases/` holds a tracked file.")
    else:
        for t in rel:
            a(f"- tag `{t['name']}` -> `{t['commit']}`")
        for d in rel_dirs:
            a(f"- directory `{d}`")
    a("")
    # 8
    a("## 8. Audit register")
    a("")
    audits = sorted(p for p in csa.blobs if p == "docs/reviews/SAR/configuration-audit.md" or re.fullmatch(r"firmware/releases/[^/]+/configuration-audit\.md", p))
    a("None: no configuration audit record exists." if not audits else "\n".join(f"- `{p}`" for p in audits))
    a("")
    # 9
    a("## 9. Tool accreditation")
    a("")
    readme = csa.git.show(csa.rev, "docs/cm/tool-validation/README.md") or ""
    index = copy_table(readme, "## Index")
    a(f"Copied from the index of `docs/cm/tool-validation/README.md` (blob `{short(csa.blobs.get('docs/cm/tool-validation/README.md'))}`).")
    a("")
    L.extend(index or ["(index not found)"])
    a("")
    # 10
    a("## 10. Metrics (Table 6-1)")
    a("")
    m = csa.msr02()
    open_crs = [c for c in csa.crs if c.get("status") in OPEN_CR_STATES]
    disp = [c for c in csa.crs if c.get("disposition_date") and latest and str(c.get("disposition_date")) >= latest[0]["date"][:10]]
    lacking = [c for c in commits if any(f["rule"] in ("REFS_MISSING", "CR_TRAILER_MISSING") for f in c["findings"])]
    a("| Metric | Value | Threshold | State |")
    a("|---|---|---|---|")
    if m and m.get("value") is not None:
        v = float(m["value"])
        state = "Red" if v >= 20 else "Yellow" if v >= 10 else "Green"
        a(f"| Requirements volatility (`MSR-02`) | {m['value']} {m.get('unit', '')} ({m.get('date')}, {m.get('state')}) | 10 % yellow, 20 % red (07 §11.2) | {state} |")
    else:
        a(f"| Requirements volatility (`MSR-02`) | no value: {m.get('state') if m else 'no MSR-02 record'} in `docs/plan/measurements.json` | 10 % yellow, 20 % red (07 §11.2) | Not measured |")
    ages = ", ".join(f"{c['id']} ({c.get('status')}, {days(c.get('date_opened'), csa.date)} d)" for c in open_crs)
    a(f"| Open CRs and their age | {len(open_crs)}{': ' + ages if ages else ''} | zero past the 05 §5.2 cycle-time target | the owner compares each age with its class target (05 §5.2) |")
    cyc = ", ".join(f"{c['id']} class {c.get('class')}: {days(c.get('date_opened'), c.get('disposition_date'))} d" for c in disp)
    a(f"| CR cycle time (opened to dispositioned; the front matter has no submission date) | {cyc or 'no CR dispositioned since ' + since} | Class II one working session; Class I next review or 14 days | {'see values' if disp else 'Not applicable'} |")
    a(f"| Commits lacking mandatory trailers (REFS_MISSING or CR_TRAILER_MISSING) | {len(lacking)}{': ' + ', '.join(c['short'] for c in lacking) if lacking else ''} | 0 | {'Red' if lacking else 'Green'} |")
    a("")
    # 11
    a("## 11. Deviations from this plan")
    a("")
    dev = csa.git.show(csa.rev, "docs/cm/deviations.md")
    if dev is None:
        a("`docs/cm/deviations.md` does not exist at the revision.")
    else:
        a(f"Copied from `docs/cm/deviations.md` (blob `{short(csa.blobs.get('docs/cm/deviations.md'))}`).")
        for heading in ("## Entries", "## Closures"):
            a("")
            a(f"**{heading[3:]}**")
            a("")
            L.extend(copy_table(dev, heading) or ["(none)"])
    a("")
    # 12
    a("## 12. Waivers")
    a("")
    w = csa.waivers()
    a("None." if not w else "\n".join(f"- `{wid}`: {md_escape(text)}" for wid, text in w))
    a("")
    # 13
    a("## 13. Open items")
    a("")
    a("**Open TBRs by target review** (each `tbr` object's `close_by`; hazard controls: each control holding a `tbr` field):")
    a("")
    a("| Set | Source file | Items | Open TBRs by close_by |")
    a("|---|---|---|---|")
    tbr = csa.tbrs()
    for kind, path, cnt in tbr:
        by = ", ".join(f"{k} {v}" for k, v in cnt["by_close_by"].items()) or "0"
        a(f"| {kind} | `{path}` | {cnt['items']} | {by} |")
    a("")
    items = csa.open_log_items()
    a(f"**Open RFA and RID items** (every `docs/reviews/*/rfa-rid-log.json`, state other than Closed or Withdrawn): {len(items)}.")
    a("")
    for it in items:
        a(f"- {it['id']} ({it['state']}, `{it['log']}`): {md_escape(it['title'])}")
    a("")
    model = {
        "rev": csa.rev, "date": csa.date, "since": csa.since, "tracked_files": len(csa.blobs),
        "rows": [dataclasses.asdict(r) for r in rows], "unmatched": unmatched, "ties": [[p, t] for p, t in ties],
        "baselines": [t for t in csa.tags if t["name"].startswith("baseline/")],
        "crs": [{k: v for k, v in c.items()} for c in csa.crs], "missing_cr_numbers": missing,
        "commits": [{k: v for k, v in c.items() if k != "files"} for c in commits],
        "lacking_trailers": [c["short"] for c in lacking], "waivers": w,
        "tbrs": [[k, p, c] for k, p, c in tbr], "open_log_items": items,
    }
    return "\n".join(L).rstrip() + "\n", model


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="csa.py", description="CSA report generator (05 section 6; TV-018)")
    ap.add_argument("--root", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--rev", default="HEAD")
    ap.add_argument("--since")
    ap.add_argument("--date")
    ap.add_argument("--remote", action="store_true")
    out = ap.add_mutually_exclusive_group()
    out.add_argument("--write", action="store_true")
    out.add_argument("--output")
    out.add_argument("--check")
    ap.add_argument("--json")
    ap.add_argument("--strict", action="store_true")
    try:
        args = ap.parse_args(argv)
    except SystemExit as exc:
        return 2 if exc.code else 0
    date = args.date or dt.date.today().isoformat()
    try:
        dt.date.fromisoformat(date)
    except ValueError:
        print(f"csa: error: --date {date!r} is not YYYY-MM-DD", file=sys.stderr)
        return 2
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    try:
        csa = Csa(args.root, args.rev, args.since, date, args.remote)
        text, model = build(csa)
    except CsaError as exc:
        print(f"csa: error: {exc}", file=sys.stderr)
        return 2
    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump(model, fh, indent=1, default=list)
            fh.write("\n")
    status = 0
    if args.check:
        try:
            with open(args.check, encoding="utf-8") as fh:
                stored = fh.read()
        except OSError as exc:
            print(f"csa: error: cannot read {args.check}: {exc}", file=sys.stderr)
            return 2
        if stored != text:
            import difflib
            sys.stdout.writelines(difflib.unified_diff(stored.splitlines(True), text.splitlines(True), args.check, "regenerated"))
            print(f"csa: CHECK FAIL: {args.check} differs from the regenerated report", file=sys.stderr)
            status = 1
        else:
            print(f"csa: CHECK PASS: {args.check} equals the regenerated report", file=sys.stderr)
    elif args.write or args.output:
        path = os.path.join(args.root, CSA_PATH) if args.write else args.output
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(text)
        print(f"csa: wrote {path}", file=sys.stderr)
    else:
        sys.stdout.write(text)
    if args.strict and (model["unmatched"] or model["ties"]):
        print(f"csa: STRICT FAIL: {len(model['unmatched'])} file(s) in no row, {len(model['ties'])} in two rows", file=sys.stderr)
        status = 1
    return status


if __name__ == "__main__":
    sys.exit(main())
