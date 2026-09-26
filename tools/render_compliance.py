#!/usr/bin/env python3
"""Render and validate the cwht NPR 7123.1D compliance matrix.

Reads docs/process/se-compliance-matrix.json and checks it:

1. against docs/process/se-compliance-matrix.schema.json (jsonschema);
2. against the corpus copy of NPR 7123.1D Appendix H, Table H-1
   (docs/references/md/npr-7123-1d/14-appendixh.md): same row set, same row
   order, same paragraph reference, and the requirement statement and
   rationale copied verbatim (whitespace-normalized comparison);
3. against the dispositions fixed by the charter (section 12 tailoring
   register; section 1 customization rule), REQUIRED_DISPOSITIONS below.

Then writes docs/process/se-compliance-matrix.md with the six columns of
NPR 7123.1D App. H.1.1 (identifier, paragraph reference, requirement
statement, rationale, Comply?, Justification) plus the cwht implementation
reference, and a tailoring-detail table for the T rows. The render carries the
JSON's revision_date, never today's date, so re-rendering unchanged JSON gives
a byte-identical file.

Exit status 0 on success, 1 on any validation error. Without --check the
markdown is written even when validation fails, so the failure is visible in
the rendered file. With --check nothing is written and the run also fails when
the rendered file on disk differs from a fresh render (stale); the stale check
needs the corpus, because the render records the corpus cross-check, and is
skipped with a printed note when the corpus is skipped.

Usage (from the repository root):
    .venv/bin/python tools/render_compliance.py              # validate and render
    .venv/bin/python tools/render_compliance.py --check      # validate, stale check, no write
    .venv/bin/python tools/render_compliance.py --no-corpus  # skip the Table H-1 cross-check
    .venv/bin/python tools/render_compliance.py --corpus ''  # same as --no-corpus

Known-answer tests: tools/tests/test_render_compliance.py with fixtures under
tools/tests/fixtures/compliance/ (SWE-136; CM plan section 9).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

try:
    from jsonschema import validators
except ImportError:  # pragma: no cover - the venv of tools/toolchain.lock.md section 2 has jsonschema
    validators = None

REPO = Path(__file__).resolve().parents[1]
DEFAULT_JSON = REPO / "docs" / "process" / "se-compliance-matrix.json"
DEFAULT_MD = REPO / "docs" / "process" / "se-compliance-matrix.md"
DEFAULT_SCHEMA = REPO / "docs" / "process" / "se-compliance-matrix.schema.json"
DEFAULT_CORPUS = REPO / "docs" / "references" / "md" / "npr-7123-1d" / "14-appendixh.md"

COMPLY_CODES = ("FC", "T", "NA")
STALE_MESSAGE = "rendered file is stale: re-run tools/render_compliance.py without --check and commit the result"

# A Table H-1 row: the id cell, then paragraph reference, requirement statement
# and rationale. The machine conversion writes some ids as "SE- 60", starts some
# rows without a leading pipe and puts two rows on one line ("|| SE-34"); the
# pattern accepts all three forms. No cell of Table H-1 contains a pipe.
H1_ROW = re.compile(
    r"(?:^|\|)[ \t]*SE-\s?(\d{2})[ \t]*\|([^|\n]*)\|([^|\n]*)\|([^|\n]*)\|",
    re.MULTILINE,
)

# Dispositions fixed by docs/process/00-charter.md. Section 12: contracted-effort
# requirements SE-24 to SE-31 NA; SE-44 NA; SE-51 and SE-52 tailored; SE-62 fully
# compliant; HSI SE-65 and SE-66 customized, which section 1 codes FC.
REQUIRED_DISPOSITIONS: dict[str, tuple[str, str]] = {
    **{f"SE-{n}": ("NA", "charter section 12 (contracted-effort row)") for n in range(24, 32)},
    "SE-44": ("NA", "charter section 12 (App. G guidance row)"),
    "SE-51": ("T", "charter section 12 (App. G guidance row)"),
    "SE-52": ("T", "charter section 12 (App. G guidance row)"),
    "SE-62": ("FC", "charter section 12 (App. G guidance row)"),
    "SE-65": ("FC", "charter sections 1 and 12 (HSI row, customized)"),
    "SE-66": ("FC", "charter sections 1 and 12 (HSI row, customized)"),
}


def normalize(text: str) -> str:
    """Collapse whitespace runs so that line wrapping does not count as a change."""
    return " ".join(text.split())


def normalize_section(text: str) -> str:
    """Paragraph reference without spaces or the stray '<' of the conversion ('5.2.2.2. b< (1)')."""
    return re.sub(r"[\s<]", "", text)


def parse_table_h1(corpus_path: Path) -> dict[str, dict[str, str]]:
    """Return {se_id: {section, statement, rationale}} in Table H-1 order."""
    text = corpus_path.read_text(encoding="utf-8")
    start = text.find("Table H-1")
    if start < 0:
        raise ValueError(f"'Table H-1' not found in {corpus_path}")
    end = text.find("Submitted By", start)
    body = text[start:] if end < 0 else text[start:end]
    table: dict[str, dict[str, str]] = {}
    for match in H1_ROW.finditer(body):
        se_id = f"SE-{match.group(1)}"
        if se_id in table:
            continue
        table[se_id] = {
            "section": match.group(2).strip(),
            "statement": match.group(3).strip(),
            "rationale": match.group(4).strip(),
        }
    if not table:
        raise ValueError(f"no SE-NN rows found after 'Table H-1' in {corpus_path}")
    return table


def load_schema(schema_path: Path) -> dict[str, Any]:
    return json.loads(schema_path.read_text(encoding="utf-8"))


def _row_label(matrix: dict[str, Any], path: list[Any]) -> str:
    pointer = "/".join(str(p) for p in path) or "/"
    if len(path) >= 2 and path[0] == "rows" and isinstance(path[1], int):
        rows = matrix.get("rows")
        if isinstance(rows, list) and 0 <= path[1] < len(rows) and isinstance(rows[path[1]], dict):
            se_id = rows[path[1]].get("se_id", "?")
            return f"{pointer} ({se_id})"
    return pointer


def schema_errors(matrix: Any, schema: dict[str, Any]) -> list[str]:
    """Return 'schema: <pointer>: <message>' strings, sorted, for every schema violation."""
    if validators is None:
        return ["schema: jsonschema is not installed in this interpreter (use .venv/bin/python)"]
    validator_cls = validators.validator_for(schema)
    validator_cls.check_schema(schema)
    validator = validator_cls(schema)
    found = []
    for err in validator.iter_errors(matrix):
        path = list(err.absolute_path)
        label = _row_label(matrix, path) if isinstance(matrix, dict) else "/"
        found.append(f"schema: {label}: {err.message}")
    return sorted(found)


def corpus_errors(rows: list[dict[str, Any]], table: dict[str, dict[str, str]]) -> list[str]:
    """Row set, order, paragraph reference and verbatim text against Table H-1."""
    errors: list[str] = []
    ids = [r.get("se_id") for r in rows if isinstance(r, dict)]
    matrix_set = {i for i in ids if isinstance(i, str)}
    corpus_ids = list(table)
    missing = sorted(set(corpus_ids) - matrix_set)
    unknown = sorted(matrix_set - set(corpus_ids))
    if missing:
        errors.append(f"ids in corpus Table H-1 but not in matrix: {missing}")
    if unknown:
        errors.append(f"ids in matrix but not in corpus Table H-1: {unknown}")
    if not missing and not unknown and len(ids) == len(set(ids)) and ids != corpus_ids:
        first = next(i for i, (a, b) in enumerate(zip(ids, corpus_ids)) if a != b)
        errors.append(
            f"row order differs from Table H-1 at row {first}: matrix has {ids[first]}, Table H-1 has {corpus_ids[first]}"
        )
    for row in rows:
        if not isinstance(row, dict):
            continue
        se_id = row.get("se_id")
        ref = table.get(se_id) if isinstance(se_id, str) else None
        if ref is None:
            continue
        section = row.get("npr_section")
        if isinstance(section, str) and normalize_section(section) != normalize_section(ref["section"]):
            errors.append(f"{se_id}: npr_section '{section}' differs from Table H-1 '{ref['section']}'")
        statement = row.get("requirement_statement")
        if isinstance(statement, str) and normalize(statement) != normalize(ref["statement"]):
            errors.append(f"{se_id}: requirement_statement is not the verbatim Table H-1 statement")
        rationale = row.get("rationale")
        if isinstance(rationale, str) and normalize(rationale) != normalize(ref["rationale"]):
            errors.append(f"{se_id}: rationale is not the verbatim Table H-1 rationale")
    return errors


def disposition_errors(rows: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    for row in rows:
        if not isinstance(row, dict):
            continue
        se_id = row.get("se_id")
        if se_id in REQUIRED_DISPOSITIONS:
            want, source = REQUIRED_DISPOSITIONS[se_id]
            got = row.get("comply")
            if got != want:
                errors.append(f"{se_id}: comply '{got}' but {source} fixes '{want}'")
    return errors


def duplicate_errors(rows: list[dict[str, Any]]) -> list[str]:
    seen: set[str] = set()
    errors: list[str] = []
    for index, row in enumerate(rows):
        se_id = row.get("se_id") if isinstance(row, dict) else None
        if not isinstance(se_id, str):
            continue
        if se_id in seen:
            errors.append(f"row {index} ({se_id}): duplicate se_id")
        seen.add(se_id)
    return errors


def validate(
    matrix: Any,
    schema: dict[str, Any],
    table: dict[str, dict[str, str]] | None,
) -> list[str]:
    """Return every validation error (empty list when the matrix is valid)."""
    errors = schema_errors(matrix, schema)
    rows = matrix.get("rows") if isinstance(matrix, dict) else None
    if not isinstance(rows, list):
        return errors
    errors.extend(duplicate_errors(rows))
    if table is not None:
        errors.extend(corpus_errors(rows, table))
    errors.extend(disposition_errors(rows))
    return errors


def _cell(text: Any) -> str:
    """Escape a value for a Markdown table cell."""
    return str(text if text is not None else "").replace("|", "\\|").replace("\n", " ").strip()


def render(matrix: dict[str, Any], errors: list[str], corpus_count: int | None) -> str:
    rows = [r for r in matrix.get("rows", []) if isinstance(r, dict)]
    counts = {code: sum(1 for r in rows if r.get("comply") == code) for code in COMPLY_CODES}

    out: list[str] = []
    out.append(f"# {matrix.get('title', 'NPR 7123.1D Compliance Matrix')}")
    out.append("")
    out.append(
        "Generated by `tools/render_compliance.py` from `docs/process/se-compliance-matrix.json` "
        "(schema `docs/process/se-compliance-matrix.schema.json`). Do not edit this file; edit the JSON "
        "and re-run the script."
    )
    out.append("")
    out.append(f"- **Status:** {matrix.get('status', '')}")
    out.append(f"- **Revision date:** {matrix.get('revision_date', '')}")
    out.append(f"- **Source table:** {matrix.get('source', '')}")
    out.append(f"- **Governing tailoring:** {matrix.get('governing_tailoring', '')}")
    approval = matrix.get("approval", {}) if isinstance(matrix.get("approval"), dict) else {}
    out.append(
        f"- **Submitted by:** {approval.get('submitted_by', '')} · "
        f"**Approved by:** {approval.get('approved_by') or 'pending'} · "
        f"**Approval record:** {approval.get('approval_memo', '')}"
    )
    out.append("")

    out.append("## Validation")
    out.append("")
    if errors:
        out.append(f"**FAILED** ({len(errors)} error(s)):")
        out.append("")
        for e in errors:
            out.append(f"- {e}")
    else:
        corpus_note = (
            f"; row set, order, paragraph references, requirement statements and rationales match the "
            f"{corpus_count} rows of corpus Table H-1"
            if corpus_count
            else "; corpus cross-check skipped"
        )
        out.append(
            f"PASSED: {len(rows)} rows valid against the schema{corpus_note}; "
            "charter section 12 dispositions hold."
        )
    out.append("")

    out.append("## Summary")
    out.append("")
    out.append("| Comply code | Meaning | Count |")
    out.append("|---|---|---|")
    meanings = matrix.get("comply_codes", {}) if isinstance(matrix.get("comply_codes"), dict) else {}
    for code in COMPLY_CODES:
        out.append(f"| {code} | {_cell(meanings.get(code, ''))} | {counts[code]} |")
    out.append(f"| **Total** | | **{len(rows)}** |")
    out.append("")

    def listing(code: str) -> str:
        items = [
            f"{r.get('se_id')} ({str(r['short_form']).rstrip('.')})" if r.get("short_form") else str(r.get("se_id"))
            for r in rows
            if r.get("comply") == code
        ]
        return "; ".join(items) or "none"

    out.append("### Tailored requirements (owner approval required)")
    out.append("")
    out.append(listing("T"))
    out.append("")
    out.append("### Not applicable requirements")
    out.append("")
    out.append(listing("NA"))
    out.append("")

    notes = matrix.get("field_notes", {})
    if isinstance(notes, dict) and notes:
        out.append("## Field notes")
        out.append("")
        for k, v in notes.items():
            out.append(f"- **{k}:** {v}")
        out.append("")

    out.append("## Matrix (NPR 7123.1D App. H.1.1 columns plus implementation reference)")
    out.append("")
    out.append(
        "| Req ID | NPR Section | Requirement Statement | Rationale | Comply? | Justification | "
        "Implementation reference |"
    )
    out.append("|---|---|---|---|---|---|---|")
    for r in rows:
        out.append(
            "| {se_id} | {sec} | {stmt} | {rat} | {comply} | {just} | {ref} |".format(
                se_id=_cell(r.get("se_id")),
                sec=_cell(r.get("npr_section")),
                stmt=_cell(r.get("requirement_statement")),
                rat=_cell(r.get("rationale")),
                comply=_cell(r.get("comply")),
                just=_cell(r.get("justification")),
                ref=_cell(r.get("implementation_ref")),
            )
        )
    out.append("")

    tailored = [r for r in rows if r.get("comply") == "T"]
    out.append("## Tailoring detail (NPR 7123.1D §2.2.1.2 relief type, §2.2.1.3 risk evaluation and approval)")
    out.append("")
    if tailored:
        out.append("| Req ID | Relief type | Risk evaluation | Tailoring approval |")
        out.append("|---|---|---|---|")
        for r in tailored:
            out.append(
                f"| {_cell(r.get('se_id'))} | {_cell(r.get('relief_type'))} | {_cell(r.get('risk_evaluation'))} | "
                f"{_cell(approval.get('approval_memo', ''))} |"
            )
    else:
        out.append("none")
    out.append("")
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=(__doc__ or "").split("\n\n")[0])
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON, help="matrix JSON path")
    parser.add_argument("--out", type=Path, default=DEFAULT_MD, help="markdown output path")
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA, help="matrix JSON Schema path")
    parser.add_argument(
        "--corpus",
        type=str,
        default=str(DEFAULT_CORPUS),
        help="corpus copy of NPR 7123.1D Appendix H; an empty string skips the Table H-1 cross-check",
    )
    parser.add_argument("--no-corpus", action="store_true", help="skip the Table H-1 cross-check")
    parser.add_argument("--check", action="store_true", help="validate and check the rendered file is current; write nothing")
    args = parser.parse_args(argv)

    try:
        matrix = json.loads(args.json.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"error: cannot read {args.json}: {exc}", file=sys.stderr)
        return 1
    try:
        schema = load_schema(args.schema)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"error: cannot read schema {args.schema}: {exc}", file=sys.stderr)
        return 1

    table: dict[str, dict[str, str]] | None = None
    if not args.no_corpus and args.corpus.strip():
        corpus_path = Path(args.corpus)
        try:
            table = parse_table_h1(corpus_path)
        except (OSError, ValueError) as exc:
            print(f"error: cannot parse corpus {corpus_path}: {exc}", file=sys.stderr)
            return 1

    errors = validate(matrix, schema, table)
    rendered = render(matrix if isinstance(matrix, dict) else {}, errors, len(table) if table else None)

    stale: list[str] = []
    stale_note = ""
    if args.check:
        if table is None:
            # The committed render records the corpus cross-check; without the
            # corpus it cannot be reproduced, so only the validation is reported.
            stale_note = " (stale check skipped: no corpus)"
        else:
            try:
                current = args.out.read_text(encoding="utf-8")
            except OSError:
                current = None
            if current != rendered:
                stale.append(STALE_MESSAGE)
            else:
                stale_note = " and rendered file is current"
    else:
        args.out.write_text(rendered, encoding="utf-8")
        print(f"wrote {args.out}")

    rows = matrix.get("rows", []) if isinstance(matrix, dict) else []
    rows = [r for r in rows if isinstance(r, dict)] if isinstance(rows, list) else []
    counts = {c: sum(1 for r in rows if r.get("comply") == c) for c in COMPLY_CODES}
    ids = {c: [r.get("se_id") for r in rows if r.get("comply") == c] for c in ("T", "NA")}
    print(
        f"rows={len(rows)} corpus={len(table) if table else 'skipped'} "
        f"FC={counts['FC']} T={counts['T']} NA={counts['NA']}"
    )
    print(f"T {ids['T']}")
    print(f"NA {ids['NA']}")
    failures = errors + stale
    if failures:
        print(f"compliance matrix check FAILED with {len(failures)} error(s):", file=sys.stderr)
        for e in failures:
            print(f"  - {e}", file=sys.stderr)
        return 1
    print("validation PASSED" + stale_note)
    return 0


if __name__ == "__main__":
    sys.exit(main())
