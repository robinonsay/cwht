#!/usr/bin/env python3
"""Render and check the cwht Requirements Mapping Matrix.

Reads docs/process/rmm.json, checks it and renders docs/process/rmm.md grouped
by NPR section with a disposition count summary and the In place id list. Per
NPR 7150.2D App. C.2 the rendered matrix lists, for every row, the section
reference, the identifier, the requirement statement (verbatim, listed under
each section table) and the Table 2 authority (column "NPR authority"); the
tailored and not-applicable mirror table carries the NPR authority as well.

Checks (every one is an error; exit status 1 on any):
  1. Structure: required fields, id format, no duplicate ids, class_a_applicable
     true, disposition in FC/T/NA, status in Planned/In place, authority text,
     implementation and responsible present.
  2. Disposition rules: T and NA rows carry tailoring_rationale and
     residual_risk of at least MIN_TEXT characters; FC rows carry null in both
     (NPR 7150.2D section 2.2.5 Note; SWE-126 a.(4)).
  3. Corpus cross-check against NPR 7150.2D App. C Table 2: the row set equals
     the Class A set; every row's npr_section, authority_npr and verbatim
     requirement_text equal its Table 2 cells (App. C.2.c).
  4. Chapter cross-check: the Class A set equals the [SWE-NNN] tags of
     chapters 3, 4 and 5 of the corpus.
  5. Status rule (record section 6.3): an In place row names no repository
     path that is absent unless the text carries "Planned for <gate>"; a
     Planned row names at least one absent repository path or carries
     "Planned for <gate>" naming the future artifact or execution.
  6. Stale render (--check only): the current --out file equals the render of
     the JSON; otherwise "rmm.md is stale; run without --check".

Standard library only. The script locates the repository from its own path, so
it may be run from any directory.

Usage (validation commands of docs/process/03-software-classification-and-rmm.md
section 6.1; run from /Users/robinonsay/rust/cwht, all four must exit 0):
    .venv/bin/python tools/validate_docs.py                # 1. JSON Schema check, incl. rmm.json
    .venv/bin/python tools/render_rmm.py                   # 2. checks 1 to 5 and render
    .venv/bin/python tools/render_rmm.py --check           # 3. checks 1 to 6, write nothing
    .venv/bin/python -m unittest discover -s tools/tests   # 4. known-answer tests (SWE-136)

Other forms:
    .venv/bin/python tools/render_rmm.py --rmm PATH --out PATH --corpus PATH --chapters DIR --repo DIR
    .venv/bin/python tools/render_rmm.py --no-corpus-check   # skip checks 3 and 4
    .venv/bin/python tools/render_rmm.py --no-status-check   # skip check 5

Known-answer tests (command 4 above; the SWE-136 evidence for this tool):
tools/tests/test_render_rmm.py with fixtures under tools/tests/fixtures/rmm/;
this tool alone:
    .venv/bin/python -m unittest tools/tests/test_render_rmm.py
"""
import argparse
import json
import re
import sys
from collections import Counter, OrderedDict
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DEFAULT_RMM = REPO / "docs/process/rmm.json"
DEFAULT_OUT = REPO / "docs/process/rmm.md"
DEFAULT_CORPUS = REPO / "docs/references/md/npr-7150-2d/09-appendixc.md"
DEFAULT_CHAPTERS = REPO / "docs/references/md/npr-7150-2d"
CHAPTER_FILES = ("03-chapter3.md", "04-chapter4.md", "05-chapter5.md")

DISPOSITIONS = OrderedDict([("FC", "Fully compliant"), ("T", "Tailored"), ("NA", "Not applicable")])
STATUSES = ("Planned", "In place")
REQUIRED_FIELDS = (
    "swe", "npr_section", "npr_group", "section_title", "short_title", "requirement_text",
    "class_a_applicable", "authority_npr", "disposition", "implementation",
    "tailoring_rationale", "residual_risk", "authority", "responsible", "status", "charter_ref",
)
# Fields that must be a string of at least MIN_TEXT characters on T and NA rows
# and null on FC rows (NPR 7150.2D section 2.2.5 Note: rationale and risk evaluation).
TAILORING_TEXT_FIELDS = ("tailoring_rationale", "residual_risk")
MIN_TEXT = 20
AUTHORITY = "Owner as ETA, SMA TA, HMTA and CIO/SAISO designee"
TABLE_HEADER = "| Section | SWE #"
STALE_MESSAGE = "rmm.md is stale; run without --check"

# Repository paths named in an implementation field. Placeholders (NNN, <...>,
# *, X.Y.Z, -r<N>) are patterns, not paths, and are not existence-checked.
PATH_RE = re.compile(r"(?<![\w/])(?:docs|tools|firmware|hardware)/[\w./<>*-]*[\w/>*]")
PLACEHOLDER_RE = re.compile(r"NNN|<|\*|X\.Y\.Z|vX|-r<|-Dn")
GATE_MARKER_RE = re.compile(r"\bPlanned for (?:SRR|PDR|CDR|TRR(?:-Dn)?|SAR)\b")


def norm(s):
    """Whitespace-normalize a table cell or JSON string for comparison."""
    return " ".join(str(s or "").split())


def parse_table(corpus: Path):
    """Parse NPR 7150.2D App. C Table 2 from the corpus markdown.

    Returns an ordered dict SWE id -> {"section", "text", "authority", "classes"}
    for every requirement row (rows with a three-digit SWE number). "classes" is
    the set of class letters (A to E) whose column carries an X.
    """
    rows = OrderedDict()
    in_table = False
    for line in corpus.read_text(encoding="utf-8").splitlines():
        if line.startswith(TABLE_HEADER):
            in_table = True
            continue
        if not in_table:
            continue
        if not line.startswith("|"):
            if rows:
                break
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 9 or set(cells[0]) <= set("- "):
            continue
        if not re.fullmatch(r"\d{3}", cells[1]):
            continue
        classes = {letter for letter, cell in zip("ABCDE", cells[4:9]) if cell == "X"}
        rows[f"SWE-{cells[1]}"] = {
            "section": cells[0],
            "text": cells[2],
            "authority": cells[3],
            "classes": classes,
        }
    return rows


def parse_class_a_set(corpus: Path):
    """Return the set of SWE ids with an X in the Class A column of Table 2."""
    return {swe for swe, row in parse_table(corpus).items() if "A" in row["classes"]}


def parse_chapter_tags(chapters: Path):
    """Return the set of [SWE-NNN] tags in chapters 3, 4 and 5 of the corpus."""
    tags = set()
    for name in CHAPTER_FILES:
        f = chapters / name
        if f.exists():
            tags |= {f"SWE-{n}" for n in re.findall(r"\[SWE-(\d{3})\]", f.read_text(encoding="utf-8"))}
    return tags


def named_paths(text: str):
    """Concrete repository paths named in an implementation field (placeholders skipped)."""
    out = []
    for m in PATH_RE.findall(text or ""):
        p = m.rstrip(".,;:")
        if PLACEHOLDER_RE.search(p):
            continue
        if p not in out:
            out.append(p)
    return out


def check_status(rows, repo: Path):
    """Check 5: status against the existence of the named repository paths."""
    errors = []
    for r in rows:
        swe = r.get("swe", "?")
        text = r.get("implementation") or ""
        paths = named_paths(text)
        missing = [p for p in paths if not (repo / p).exists()]
        marked = bool(GATE_MARKER_RE.search(text))
        if r.get("status") == "In place":
            if missing and not marked:
                errors.append(
                    f"{swe}: status 'In place' but named path does not exist: {missing} "
                    "(label the future item 'Planned for <gate>' or set status Planned)"
                )
        elif r.get("status") == "Planned":
            if not missing and not marked:
                errors.append(
                    f"{swe}: status 'Planned' but every named path exists and no 'Planned for <gate>' "
                    "names the future artifact or execution (set status In place or add the label)"
                )
    return errors


def check(rmm: dict, corpus: Path, chapters: Path = None, repo: Path = None):
    """Checks 1 to 5. corpus=None skips 3 and 4; repo=None skips 5."""
    errors = []
    rows = rmm.get("rows")
    if not isinstance(rows, list):
        return ["'rows' is missing or not a list"]
    seen = set()
    by_swe = {}
    for i, r in enumerate(rows):
        tag = f"row {i} ({r.get('swe', '?')})"
        for f in REQUIRED_FIELDS:
            if f not in r:
                errors.append(f"{tag}: missing field '{f}'")
        swe = r.get("swe", "")
        if not re.fullmatch(r"SWE-\d{3}", swe):
            errors.append(f"{tag}: bad swe id")
        if swe in seen:
            errors.append(f"{tag}: duplicate swe id")
        seen.add(swe)
        by_swe[swe] = r
        if r.get("class_a_applicable") is not True:
            errors.append(f"{tag}: class_a_applicable must be true")
        if r.get("disposition") not in DISPOSITIONS:
            errors.append(f"{tag}: disposition must be one of {list(DISPOSITIONS)}")
        if r.get("status") not in STATUSES:
            errors.append(f"{tag}: status must be one of {STATUSES}")
        if r.get("authority") != AUTHORITY:
            errors.append(f"{tag}: authority must be '{AUTHORITY}'")
        for field in TAILORING_TEXT_FIELDS:
            value = r.get(field)
            if r.get("disposition") in ("T", "NA"):
                if not isinstance(value, str) or len(value.strip()) < MIN_TEXT:
                    errors.append(f"{tag}: T/NA row needs a {field} of at least {MIN_TEXT} characters")
            elif value is not None:
                errors.append(f"{tag}: FC row must have {field} null")
        if not isinstance(r.get("implementation"), str) or len(r["implementation"].strip()) < MIN_TEXT:
            errors.append(f"{tag}: implementation too short")
        if not r.get("responsible"):
            errors.append(f"{tag}: responsible is empty")
    if corpus is not None:
        if not corpus.exists():
            errors.append(f"corpus file not found: {corpus}")
        else:
            table = parse_table(corpus)
            expected = {swe for swe, row in table.items() if "A" in row["classes"]}
            missing = sorted(expected - seen)
            extra = sorted(seen - expected)
            if missing:
                errors.append(f"Class A rows in App. C but not in rmm.json: {missing}")
            if extra:
                errors.append(f"rows in rmm.json that are not Class A rows of App. C: {extra}")
            if not expected:
                errors.append("corpus parse found no Class A rows; table format changed?")
            # Per-row cross-check of the values the record claims are taken from Table 2
            # (npr_section, authority_npr, verbatim requirement_text per App. C.2.c).
            for swe in sorted(seen & expected):
                r = by_swe[swe]
                t = table[swe]
                if norm(r.get("npr_section")) != norm(t["section"]):
                    errors.append(f"{swe}: npr_section '{r.get('npr_section')}' differs from Table 2 section '{t['section']}'")
                if norm(r.get("authority_npr")) != norm(t["authority"]):
                    errors.append(f"{swe}: authority_npr '{r.get('authority_npr')}' differs from Table 2 authority '{t['authority']}'")
                if norm(r.get("requirement_text")) != norm(t["text"]):
                    errors.append(f"{swe}: requirement_text is not the verbatim Table 2 statement (whitespace-normalized comparison)")
            # Chapter cross-check: the Class A set equals the [SWE-NNN] tags of chapters 3 to 5.
            if chapters is not None and expected:
                tags = parse_chapter_tags(chapters)
                if not tags:
                    errors.append(f"no [SWE-NNN] tags found under {chapters}; chapter files missing?")
                else:
                    only_table = sorted(expected - tags)
                    only_chapters = sorted(tags - expected)
                    if only_table:
                        errors.append(f"Class A rows in App. C without a [SWE-NNN] tag in chapters 3 to 5: {only_table}")
                    if only_chapters:
                        errors.append(f"[SWE-NNN] tags in chapters 3 to 5 without a Class A row in App. C: {only_chapters}")
    if repo is not None:
        errors.extend(check_status(rows, repo))
    return errors


def esc(s):
    """Escape for a Markdown table cell."""
    if s is None:
        return ""
    return str(s).replace("|", "\\|").replace("\n", " ").strip()


def group_key(g):
    return tuple(int(p) for p in g.split("."))


def ids_with(rows, field, value):
    return [r["swe"] for r in rows if r.get(field) == value]


def summary_line(rows):
    """One-line summary printed by main(): counts and the In place, T and NA id lists."""
    disp = Counter(r["disposition"] for r in rows)
    parts = [f"{len(rows)} rows", ", ".join(f"{k}={disp.get(k, 0)}" for k in DISPOSITIONS)]
    in_place = ids_with(rows, "status", "In place")
    parts.append(f"In place={len(in_place)} [{', '.join(in_place)}]")
    parts.append(f"T [{', '.join(ids_with(rows, 'disposition', 'T'))}]")
    parts.append(f"NA [{', '.join(ids_with(rows, 'disposition', 'NA'))}]")
    return "; ".join(parts)


def render(rmm: dict) -> str:
    meta = rmm["meta"]
    rows = rmm["rows"]
    disp = Counter(r["disposition"] for r in rows)
    stat = Counter(r["status"] for r in rows)
    out = []
    out.append("# cwht Requirements Mapping Matrix (NPR 7150.2D App. C, Class A)\n")
    out.append("Generated by `tools/render_rmm.py` from `docs/process/rmm.json`. Do not edit this file; edit the JSON and re-render.\n")
    out.append("| Field | Value |")
    out.append("|---|---|")
    out.append(f"| Project | {esc(meta['project'])} |")
    out.append(f"| Governing document | {esc(meta['npr'])} |")
    out.append(f"| Row source | {esc(meta['source_table'])} |")
    out.append(f"| Software class elected (charter section 1) | {esc(meta['software_class_elected'])} |")
    out.append(f"| App. D assessment by the letter | {esc(meta['software_class_app_d_assessment'])} |")
    out.append(f"| Classification record | `{esc(meta['classification_record'])}` |")
    out.append(f"| Tailoring authority | {esc(meta['authority'])} |")
    out.append(f"| Generated on | {esc(meta['generated_on'])} |")
    ap = meta["approval"]
    out.append(f"| Approval status | {esc(ap['status'])} |")
    out.append(f"| Signature block (decision memo) | `{esc(ap['memo'])}` |")
    out.append(f"| Approved by / on | {esc(ap['approved_by']) or 'not yet signed'} / {esc(ap['approved_on']) or 'n/a'} |")
    out.append("")
    out.append("## Disposition summary\n")
    out.append("| Disposition | Meaning | Rows | SWE ids |")
    out.append("|---|---|---:|---|")
    for code, meaning in DISPOSITIONS.items():
        ids = ids_with(rows, "disposition", code)
        shown = "all other rows" if code == "FC" else ", ".join(ids)
        out.append(f"| {code} | {meaning} | {disp.get(code, 0)} | {shown} |")
    out.append(f"| **Total** | Class A rows of App. C Table 2 | **{len(rows)}** | |")
    out.append("")
    out.append("| Status | Rows | SWE ids |")
    out.append("|---|---:|---|")
    for s in STATUSES:
        ids = ids_with(rows, "status", s)
        shown = "all other rows" if s == "Planned" else ", ".join(ids)
        out.append(f"| {s} | {stat.get(s, 0)} | {shown} |")
    out.append("")
    out.append(
        "Status rule (record section 6.3): In place means the requirement is satisfied today by artifacts that exist in the repository; "
        "Planned means satisfaction needs an artifact or an execution that does not yet exist, named in the implementation text with its gate "
        "(\"Planned for <gate>\") or as an absent repository path. `tools/render_rmm.py` enforces the rule.\n"
    )
    out.append("Per section:\n")
    out.append("| NPR section | Title | FC | T | NA | Total |")
    out.append("|---|---|---:|---:|---:|---:|")
    groups = OrderedDict()
    for r in sorted(rows, key=lambda r: (group_key(r["npr_group"]), group_key(r["npr_section"]))):
        groups.setdefault((r["npr_group"], r["section_title"]), []).append(r)
    for (g, title), grows in groups.items():
        c = Counter(r["disposition"] for r in grows)
        out.append(f"| {g} | {esc(title)} | {c.get('FC', 0)} | {c.get('T', 0)} | {c.get('NA', 0)} | {len(grows)} |")
    out.append("")
    out.append("## Tailored and not-applicable rows (mirror into the software plan per SWE-121)\n")
    out.append("Each row carries the rationale (what is relieved and why) and the residual risk with its mitigation, as NPR 7150.2D section 2.2.5 Note and SWE-126 a.(4) require of a request for relief.\n")
    out.append("| SWE | Disp. | Short title | NPR authority | Tailoring rationale | Residual risk |")
    out.append("|---|---|---|---|---|---|")
    for (g, title), grows in groups.items():
        for r in grows:
            if r["disposition"] in ("T", "NA"):
                out.append(
                    f"| {r['swe']} | {r['disposition']} | {esc(r['short_title'])} | {esc(r['authority_npr'])} | "
                    f"{esc(r['tailoring_rationale'])} | {esc(r['residual_risk'])} |"
                )
    out.append("")
    out.append("## Matrix by NPR section\n")
    out.append(
        "Columns: NPR section, SWE id, short title, NPR authority (the Table 2 authority column, App. C.2.d), disposition "
        "(FC / T / NA), status, responsible role(s), charter section(s) governing the row, implementation on cwht, tailoring "
        "rationale and residual risk (T and NA only). The verbatim requirement statement of every row (App. C.2.c) is listed "
        "under its section table. Tailoring authority recorded for every row (`authority`): " + esc(meta["authority"]) + ", "
        "standing in for the NPR authority of the row (record section 6.2).\n"
    )
    for (g, title), grows in groups.items():
        out.append(f"### {g} {esc(title)}\n")
        out.append("| NPR § | SWE | Short title | NPR authority | Disp. | Status | Responsible | Charter | Implementation | Tailoring rationale | Residual risk |")
        out.append("|---|---|---|---|---|---|---|---|---|---|---|")
        for r in grows:
            resp = "; ".join(r["responsible"])
            out.append(
                f"| {esc(r['npr_section'])} | {esc(r['swe'])} | {esc(r['short_title'])} | {esc(r['authority_npr'])} | "
                f"{esc(r['disposition'])} | {esc(r['status'])} | {esc(resp)} | {esc(r['charter_ref'])} | "
                f"{esc(r['implementation'])} | {esc(r['tailoring_rationale'])} | {esc(r['residual_risk'])} |"
            )
        out.append("")
        out.append("Requirement statements (verbatim, App. C.2.c):\n")
        for r in grows:
            out.append(f"- **{esc(r['swe'])}** ({esc(r['npr_section'])}): {esc(r['requirement_text'])}")
        out.append("")
    out.append("## Signature block\n")
    out.append(
        "This matrix is approved by the owner acting as Engineering Technical Authority and SMA Technical Authority (charter section 2), "
        "as CIO/SAISO designee for the section 3.11 relief (NPR 7150.2D sections 2.2.1 and 2.2.6) and as Health and Medical Technical "
        "Authority for the health and medical implications of the tailoring (App. C.3; section 2.2.1), who also accepts as the risk taker "
        "the human safety risk of the SWE-022, SWE-023 and SWE-219 tailoring (NPR 7150.2D section 2.2.1). "
        "The signature is section 7.1 of the decision memo named above; it records the git hash of the commit whose `docs/process/rmm.json` "
        "content was approved, and the approver and date are carried in this matrix (`meta.approval`, SWE-126 b). Rows dispositioned T or "
        "NA constitute the approved tailoring (NPR 7150.2D section 2.2, SWE-121, SWE-125).\n"
    )
    return "\n".join(out)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--rmm", type=Path, default=DEFAULT_RMM)
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--corpus", type=Path, default=DEFAULT_CORPUS)
    ap.add_argument("--chapters", type=Path, default=DEFAULT_CHAPTERS, help="directory holding 03-chapter3.md, 04-chapter4.md, 05-chapter5.md")
    ap.add_argument("--repo", type=Path, default=REPO, help="root against which named repository paths are existence-checked")
    ap.add_argument("--check", action="store_true", help="check only (including the stale-render check); do not write the rendered file")
    ap.add_argument("--no-corpus-check", action="store_true", help="skip the App. C and chapter cross-checks")
    ap.add_argument("--no-status-check", action="store_true", help="skip the status-versus-path rule")
    args = ap.parse_args(argv)

    rmm = json.loads(args.rmm.read_text(encoding="utf-8"))
    errors = check(
        rmm,
        None if args.no_corpus_check else args.corpus,
        None if args.no_corpus_check else args.chapters,
        None if args.no_status_check else args.repo,
    )
    rendered = None
    if not errors:
        rendered = render(rmm) + "\n"
        if args.check:
            current = args.out.read_text(encoding="utf-8") if args.out.exists() else None
            if current != rendered:
                errors.append(STALE_MESSAGE)
    if errors:
        print("rmm.json check FAILED:", file=sys.stderr)
        for e in errors:
            print("  -", e, file=sys.stderr)
        return 1
    print("rmm.json OK: " + summary_line(rmm["rows"]))
    if args.check:
        print(f"{args.out} is current")
        return 0
    args.out.write_text(rendered, encoding="utf-8")
    print(f"rendered {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
