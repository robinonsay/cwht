#!/usr/bin/env python3
"""Validate cwht JSON documents against their JSON Schemas by path convention.

Discovery conventions (paths relative to the repository root):

    docs/requirements/**/requirements.json            -> docs/requirements/schema.json
    docs/requirements/l0-stakeholder/expectations.json -> docs/requirements/l0-stakeholder/schema.json
    docs/test_cases/**/test_cases.json                -> docs/test_cases/schema.json
    docs/risk/register.json                           -> docs/risk/schema.json
    docs/safety/hazards.json                          -> docs/safety/schema.json
    docs/process/rmm.json                             -> docs/process/rmm.schema.json
    docs/process/se-compliance-matrix.json            -> docs/process/se-compliance-matrix.schema.json
    docs/plan/tpm.json                                -> docs/plan/tpm.schema.json
    docs/plan/measurements.json                       -> docs/plan/measurements.schema.json
    docs/design/allocation.json                       -> docs/design/allocation.schema.json
    docs/reviews/*/rfa-rid-log.json                   -> docs/templates/rfa-rid-log.schema.json
    docs/templates/<name>.example.json                -> docs/templates/<name>.schema.json,
                                                         else the schema aliased for <name>
    docs/reviews/*/checklists/<product-slug>.md       -> built-in peer-review record schema
                                                         (YAML front matter; charter section 5,
                                                         docs/process/01-lifecycle-and-reviews.md
                                                         section 13)
    docs/reviews/*/decision-memo.md                   -> built-in decision memo schema
                                                         (front matter of docs/templates/decision-memo.md)

A discovered document whose schema file is absent is a failure. This is a
design decision of this tool, taken from docs/process/05-configuration-and-
data-management.md: section 10.2 makes JSON authoritative only as "JSON
validated by the row 9 schemas", and Table 4-1 row 9 says every schema gates
validation evidence. A conventional path therefore names a document that
cannot be evidence until its schema exists.

Cross-file rules applied on top of the schemas:

    - every folder under docs/reviews/ is a review token of charter section 6
      (SRR, PDR, CDR, TRR, TRR-Dn, SAR);
    - an RFA/RID log names its own folder in "review", and every item carries
      that review in "review" and in its id prefix <type>-<review>- (01
      section 10.4 check 2, which is how the exact n of a TRR-Dn log is
      checked);
    - every item history is a legal path of the 01 section 10.3 state machine
      that ends in the item's state, and "closed" is the date of the terminal
      entry;
    - every verification.record of a log names an existing peer-review
      record whose product is the item's product;
    - peer-review record ids (INSP-NNN) are unique across all reviews; a
      record's checklist_file, when present, is the record's own path; the
      reviewer is not the author; an assurance reviewer other than author and
      reviewer is named for the products of 07 sections 2.1.1 and 14.1;
      APPROVED needs readiness_met true and no Major finding in state Open
      (SWE-088 b, c, d; SWE-089);
    - a decision memo names its own folder, and disposition, signed, revoked
      and baseline_tag are consistent (01 sections 11, 12.1 and 12.2);
    - no docs/reviews/*/peer-reviews/ folder exists (charter section 5 as
      amended 2026-09-25: the filled checklist is the single record);
    - record drift (SRR package section 2.3 and item R13; lead SE direction
      2026-09-26 "records name the committed blobs they reviewed"): when
      --root is the top of a git work tree with a HEAD commit, every blob a
      record names in product_files (path@blob) or product_blob (the blob of
      its single-file product) is compared with `git ls-tree HEAD` (the value
      `git rev-parse HEAD:<path>` gives). For a record whose verdict is
      APPROVED a differing or absent blob is a failure, and so is an APPROVED
      record that names no blob; for any other verdict the drift is printed
      as a note and does not fail. Outside a git work tree top (the test
      fixtures) the rule is reported as not applied.

Exit status: 0 when every discovered document validates (or none is found),
1 when any document fails, 2 on a usage error.

Usage:
    .venv/bin/python tools/validate_docs.py [--root PATH] [--quiet]
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import jsonschema
from jsonschema import validators

try:  # PyYAML is in tools/requirements.txt; the subset parser below is the fallback
    import yaml  # type: ignore
except ImportError:  # pragma: no cover - exercised only when the venv lacks PyYAML
    yaml = None

REPO_ROOT = Path(__file__).resolve().parents[1]
MAX_ERROR_MESSAGE = 240


@dataclass(frozen=True)
class Convention:
    """One document-to-schema pairing discovered by glob."""

    name: str
    document_glob: str
    schema_path: str


CONVENTIONS: tuple[Convention, ...] = (
    Convention("requirements", "docs/requirements/**/requirements.json", "docs/requirements/schema.json"),
    Convention(
        "expectations",
        "docs/requirements/l0-stakeholder/expectations.json",
        "docs/requirements/l0-stakeholder/schema.json",
    ),
    Convention("test_cases", "docs/test_cases/**/test_cases.json", "docs/test_cases/schema.json"),
    Convention("risk_register", "docs/risk/register.json", "docs/risk/schema.json"),
    Convention("hazards", "docs/safety/hazards.json", "docs/safety/schema.json"),
    Convention("rmm", "docs/process/rmm.json", "docs/process/rmm.schema.json"),
    Convention("se_compliance_matrix", "docs/process/se-compliance-matrix.json", "docs/process/se-compliance-matrix.schema.json"),
    Convention("tpm", "docs/plan/tpm.json", "docs/plan/tpm.schema.json"),
    Convention("measurements", "docs/plan/measurements.json", "docs/plan/measurements.schema.json"),
    Convention("allocation", "docs/design/allocation.json", "docs/design/allocation.schema.json"),
    Convention("rfa_rid_log", "docs/reviews/*/rfa-rid-log.json", "docs/templates/rfa-rid-log.schema.json"),
)

TEMPLATES_DIR = "docs/templates"
REVIEWS_DIR = "docs/reviews"
RFA_RID_TEMPLATE = "rfa-rid-log"
PEER_REVIEW_RECORD_GLOB = "docs/reviews/*/checklists/*.md"
DECISION_MEMO_GLOB = "docs/reviews/*/decision-memo.md"
FORBIDDEN_PEER_REVIEWS_GLOB = "docs/reviews/*/peer-reviews"
PEER_REVIEW_RECORD_LABEL = "built-in peer-review record schema (charter section 5; 01 section 13)"
DECISION_MEMO_LABEL = "built-in decision memo schema (docs/templates/decision-memo.md front matter)"
REVIEW_FOLDER_LABEL = "review folder token (charter section 6)"
REVIEW_TOKEN = re.compile(r"^(SRR|PDR|CDR|TRR|SAR|TRR-D[1-9][0-9]?)$")
BASELINED_REVIEWS = ("SRR", "PDR", "CDR", "SAR")  # charter section 8: the gates that set a baseline tag
PRODUCT_SLUG_FILE = re.compile(r"^[a-z0-9][a-z0-9._-]*\.md$")
ISO_DATE = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$")

# docs/templates/<name>.example.json whose schema lives outside docs/templates/.
TEMPLATE_SCHEMA_ALIASES: dict[str, str] = {
    "requirements": "docs/requirements/schema.json",
    "test_cases": "docs/test_cases/schema.json",
    "expectations": "docs/requirements/l0-stakeholder/schema.json",
    "register": "docs/risk/schema.json",
    "risk-register": "docs/risk/schema.json",
    "hazards": "docs/safety/schema.json",
    "rmm": "docs/process/rmm.schema.json",
    "se-compliance-matrix": "docs/process/se-compliance-matrix.schema.json",
    "tpm": "docs/plan/tpm.schema.json",
    "measurements": "docs/plan/measurements.schema.json",
    "allocation": "docs/design/allocation.schema.json",
}

# 01 section 10.3: the RFA/RID state machine. Same-state entries (lien acceptance,
# severity change) are admitted in any non-terminal state; nothing follows a terminal state.
LOG_STATES = ("Open", "Answered", "Verified", "Closed", "Withdrawn")
TERMINAL_STATES = ("Closed", "Withdrawn")
LOG_TRANSITIONS = frozenset(
    {
        ("Open", "Answered"),
        ("Answered", "Verified"),
        ("Answered", "Open"),  # Rejected verification
        ("Verified", "Open"),  # owner declines closure
        ("Verified", "Closed"),
        ("Open", "Withdrawn"),
        ("Answered", "Withdrawn"),
    }
)

# Front matter of a filled checklist, the single peer-review record of charter
# section 5. The field set is the one docs/process/01-lifecycle-and-reviews.md
# section 13 requires (id, checklist, product, product_commit, verdict, the
# finding counts and the SWE-089 measurements effort_turns, effort_minutes and
# iteration) plus the fields that make SWE-088 checkable from the record:
# author_agent and reviewer_agent (SWE-088 d, required participants; charter
# section 2 independence; NPR 7123.1D App. G Table G-19 entrance 2),
# readiness_met (SWE-088 b) and date.
COUNT_FIELDS = ("findings_major", "findings_minor", "findings_fixed", "findings_deferred", "effort_turns", "effort_minutes")
PEER_REVIEW_RECORD_SCHEMA: dict[str, Any] = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "required": [
        "id", "checklist", "product", "product_commit", "verdict",
        "author_agent", "reviewer_agent", "iteration", "date", "readiness_met",
        *COUNT_FIELDS,
    ],
    "properties": {
        "id": {"type": "string", "pattern": "^INSP-[0-9]{3}$"},
        "checklist": {"type": "string", "pattern": "^peer-review-checklist-[a-z]+(-[a-z]+)*$"},
        "checklist_revision": {"type": "string"},
        "checklist_file": {"type": "string", "pattern": "^docs/reviews/(SRR|PDR|CDR|TRR|SAR|TRR-D[1-9][0-9]?)/checklists/[a-z0-9][a-z0-9._-]*\\.md$"},
        "product": {"type": "string", "minLength": 1},
        "product_files": {
            "type": "array",
            "items": {"type": "string", "pattern": "^[^@\\s]+@[0-9a-f]{7,40}$"},
            "description": "path@git blob of every reviewed file (record drift rule, package section 2.3, R13)",
        },
        "product_blob": {"type": "string", "pattern": "^[0-9a-f]{7,40}$", "description": "git blob of a single-file product"},
        "product_commit": {
            "type": "string",
            "pattern": "^[0-9a-f]{7,40}$",
            "description": "Commit of the reviewed product; quote the value when it is all digits so YAML keeps it a string",
        },
        "author_agent": {"type": "string", "minLength": 1},
        "reviewer_agent": {"type": "string", "minLength": 1},
        "assurance_reviewer_agent": {"type": "string", "minLength": 1},
        "verdict": {"type": "string", "enum": ["APPROVED", "NEEDS CHANGES"]},
        "iteration": {"type": "integer", "minimum": 1, "maximum": 3},
        "readiness_met": {"type": "boolean"},
        "date": {"type": "string", "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$"},
        **{name: {"type": "integer", "minimum": 0} for name in COUNT_FIELDS},
    },
}

# docs/process/07-software-engineering-plan.md section 14.1 (single authoritative
# component list, charter section 10): modules whose requirement, design, code and
# test products need the software assurance second review (07 section 2.1.1).
SAFETY_CRITICAL_MODULES = ("SW-KEYER", "SW-TXSEQ", "SW-PWR", "SW-SAFE", "SW-AUDIO", "SW-BOOT", "SW-SCHED")
MISSION_CRITICAL_MODULES = ("SW-SYNTH", "SW-CFG", "SW-DISPLAY")
# 07 section 2.1.1 products that need the assurance review as a whole.
ASSURANCE_WHOLE_PRODUCTS = (
    "docs/requirements/sw/requirements.json",
    "docs/process/07-software-engineering-plan.md",
    "docs/process/03-software-classification-and-rmm.md",
    "docs/vv/plan.md",
    "docs/design/architecture.md",
)
SW_MODULE_TOKEN = re.compile(r"(?<![a-z0-9])sw-([a-z0-9]+)")
NO_ASSURANCE = "none"
FINDING_ANCHOR = re.compile(r"finding-[0-9]+")
OPEN_MAJOR = (re.compile(r"\bMajor\b"), re.compile(r"\bOpen\b"))

# Front matter of docs/templates/decision-memo.md (machine-read keys).
DECISION_MEMO_SCHEMA: dict[str, Any] = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "required": ["review", "disposition", "signed"],
    "properties": {
        "review": {"type": "string", "pattern": "^(SRR|PDR|CDR|TRR|SAR|TRR-D[1-9][0-9]?)$"},
        "package_revision": {"type": "integer", "minimum": 1},
        "disposition": {"enum": [None, "Approved", "Approved with liens"]},
        "signed": {"type": ["string", "null"], "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$"},
        "baseline_tag": {"type": ["string", "null"], "pattern": "^baseline/(srr|pdr|cdr|sar)$"},
        "revoked": {"type": ["string", "null"], "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$"},
    },
}


@dataclass
class FileResult:
    """Validation outcome for one discovered document."""

    convention: str
    document: Path
    schema: Path
    errors: list[str] = field(default_factory=list)
    schema_label: str | None = None
    notes: list[str] = field(default_factory=list)

    @property
    def passed(self) -> bool:
        return not self.errors


@dataclass
class Discovered:
    """A document paired with the schema it must satisfy."""

    convention: str
    document: Path
    schema: Path


# ----------------------------------------------------------------------------
# YAML front matter (shared with tools/traceability.py and tools/review_trend.py)
# ----------------------------------------------------------------------------

FM_KEY = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):(?:\s+(.*))?$")


def split_front_matter(text: str) -> str | None:
    """Return the text between the opening and closing '---' lines, or None."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            return "\n".join(lines[1:index])
    return None


def body_after_front_matter(text: str) -> str:
    """The text after the closing '---' of the front matter (the whole text when there is none)."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return text
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            return "\n".join(lines[index + 1 :])
    return ""


def parse_front_matter(text: str) -> dict[str, Any] | None:
    """Parse front matter delimited by '---' lines.

    Uses PyYAML (safe_load) when it is installed and falls back to the subset
    parser parse_front_matter_subset otherwise, or when PyYAML rejects the
    block. Returns None when the text does not start with a front matter block
    or the block is not a mapping.
    """
    block = split_front_matter(text)
    if block is None:
        return None
    if yaml is not None:
        try:
            data = yaml.safe_load(block)
        except yaml.YAMLError:
            data = None
        if isinstance(data, dict):
            return {str(k): v for k, v in data.items()}
    return parse_front_matter_subset(block)


def parse_front_matter_subset(block: str) -> dict[str, Any]:
    """Dependency-free parser for the template subset (04 section 7.4).

    Supported: top-level 'key: value', inline '[a, b]' lists, block lists of
    scalars ('- item') and block lists of flat maps ('- key: value' followed by
    indented 'key: value' lines), '# comments' (whole line or after a value),
    quoted strings, true/false, null and integers.
    """
    data: dict[str, Any] = {}
    list_key: str | None = None
    current_map: dict[str, Any] | None = None
    for raw in block.splitlines():
        line = raw.rstrip()
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        indented = line[0].isspace()
        stripped = line.strip()
        if stripped.startswith("- ") and list_key is not None:
            item = _strip_comment(stripped[2:].strip())
            pair = FM_KEY.match(item)
            if pair:
                current_map = {pair.group(1): _yaml_scalar(pair.group(2) or "")}
                data[list_key].append(current_map)
            else:
                current_map = None
                data[list_key].append(_yaml_scalar(item))
            continue
        pair = FM_KEY.match(stripped)
        if not pair:
            continue
        key, value = pair.group(1), _strip_comment(pair.group(2) or "")
        if indented and current_map is not None:
            current_map[key] = _yaml_scalar(value)
            continue
        current_map = None
        if value == "":
            data[key] = []
            list_key = key
        elif value.startswith("[") and value.endswith("]"):
            data[key] = [_yaml_scalar(v) for v in value[1:-1].split(",") if v.strip()]
            list_key = None
        else:
            data[key] = _yaml_scalar(value)
            list_key = None
    return data


def _strip_comment(value: str) -> str:
    value = value.strip()
    if value[:1] in ("'", '"'):
        end = value.find(value[0], 1)
        return value[: end + 1] if end != -1 else value
    if value.startswith("#"):
        return ""
    idx = value.find(" #")
    return value[:idx].rstrip() if idx != -1 else value


def _yaml_scalar(raw: str) -> Any:
    value = raw.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    lowered = value.lower()
    if lowered in ("null", "~", ""):
        return None
    if lowered == "true":
        return True
    if lowered == "false":
        return False
    if re.fullmatch(r"-?[0-9]+", value):
        return int(value)
    return value


def json_ready(value: Any) -> Any:
    """Front matter values as JSON types: YAML dates become ISO strings."""
    if isinstance(value, (dt.date, dt.datetime)):
        return value.isoformat()
    if isinstance(value, dict):
        return {str(k): json_ready(v) for k, v in value.items()}
    if isinstance(value, list):
        return [json_ready(v) for v in value]
    return value


# ----------------------------------------------------------------------------
# Discovery
# ----------------------------------------------------------------------------


def discover(root: Path) -> list[Discovered]:
    """Return every JSON document/schema pair under root, sorted by document path."""
    found: list[Discovered] = []
    for convention in CONVENTIONS:
        schema = root / convention.schema_path
        for document in sorted(root.glob(convention.document_glob)):
            if document.is_file():
                found.append(Discovered(convention.name, document, schema))
    templates = root / TEMPLATES_DIR
    if templates.is_dir():
        for example in sorted(templates.glob("*.example.json")):
            name = example.name[: -len(".example.json")]
            sibling = templates / f"{name}.schema.json"
            if sibling.is_file():
                schema = sibling
            elif name in TEMPLATE_SCHEMA_ALIASES:
                schema = root / TEMPLATE_SCHEMA_ALIASES[name]
            else:
                schema = sibling  # reported as missing
            found.append(Discovered("template_example", example, schema))
    found.sort(key=lambda item: str(item.document))
    return found


# ----------------------------------------------------------------------------
# Validation
# ----------------------------------------------------------------------------


def load_json(path: Path) -> tuple[Any, str | None]:
    """Load a JSON file. Returns (data, None) or (None, error message)."""
    try:
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle), None
    except FileNotFoundError:
        return None, f"file not found: {path}"
    except json.JSONDecodeError as exc:
        return None, f"invalid JSON at line {exc.lineno} column {exc.colno}: {exc.msg}"
    except OSError as exc:
        return None, f"cannot read: {exc}"


def build_validator(schema_path: Path, cache: dict[Path, Any]) -> tuple[Any, str | None]:
    """Return a Draft-appropriate validator for the schema, or an error message."""
    if schema_path in cache:
        return cache[schema_path], None
    schema, error = load_json(schema_path)
    if error is not None:
        return None, f"schema {rel(schema_path)}: {error}"
    validator_class = validators.validator_for(schema)
    try:
        validator_class.check_schema(schema)
    except jsonschema.SchemaError as exc:
        return None, f"schema {rel(schema_path)} is not a valid JSON Schema: {exc.message}"
    validator = validator_class(schema)
    cache[schema_path] = validator
    return validator, None


def json_pointer(error: jsonschema.ValidationError) -> str:
    """Render an error path as dotted notation, e.g. requirements[3].id."""
    parts: list[str] = []
    for element in error.absolute_path:
        if isinstance(element, int):
            parts.append(f"[{element}]")
        else:
            parts.append(("." if parts else "") + str(element))
    return "".join(parts) or "<root>"


def format_error(error: jsonschema.ValidationError) -> str:
    message = error.message.replace("\n", " ")
    if len(message) > MAX_ERROR_MESSAGE:
        message = message[: MAX_ERROR_MESSAGE - 3] + "..."
    return f"{json_pointer(error)}: {message}"


def validate_document(document: Path, schema: Path, cache: dict[Path, Any] | None = None, convention: str = "") -> FileResult:
    """Validate one document against one schema. Never raises on bad input."""
    cache = {} if cache is None else cache
    result = FileResult(convention, document, schema)
    if not schema.is_file():
        result.errors.append(f"schema not found: {rel(schema)}")
        return result
    validator, error = build_validator(schema, cache)
    if error is not None:
        result.errors.append(error)
        return result
    data, error = load_json(document)
    if error is not None:
        result.errors.append(error)
        return result
    errors = sorted(validator.iter_errors(data), key=lambda err: (json_pointer(err), err.message))
    result.errors.extend(format_error(err) for err in errors)
    return result


def validate_mapping(data: dict[str, Any], schema: dict[str, Any]) -> list[str]:
    """Schema errors of an in-memory mapping (front matter) as formatted strings."""
    validator = validators.validator_for(schema)(schema)
    return [format_error(err) for err in sorted(validator.iter_errors(data), key=lambda e: (json_pointer(e), e.message))]


def review_folder(document: Path, root: Path) -> str | None:
    """The <REVIEW> folder name of docs/reviews/<REVIEW>/..., or None outside docs/reviews/."""
    try:
        parts = document.resolve().relative_to((root / REVIEWS_DIR).resolve()).parts
    except ValueError:
        return None
    return parts[0] if len(parts) > 1 else None


def token_error(folder: str) -> str:
    return f"folder '{folder}' is not a review token (SRR, PDR, CDR, TRR, TRR-Dn, SAR; charter section 6)"


def parse_iso(value: Any) -> dt.date | None:
    if not isinstance(value, str) or not ISO_DATE.match(value):
        return None
    try:
        return dt.date.fromisoformat(value)
    except ValueError:
        return None


def item_errors(item: dict[str, Any], index: int, review: str | None) -> list[str]:
    """01 section 10.4 check 2 and the 01 section 10.3 history rules for one log item."""
    errors: list[str] = []
    ident = item.get("id") if isinstance(item.get("id"), str) else f"items[{index}]"
    where = f"items[{index}] {ident}"
    kind = item.get("type")
    if isinstance(review, str):
        if item.get("review") != review:
            errors.append(f"{where}: review '{item.get('review')}' but the log's review is '{review}' (01 section 10.4 check 2)")
        if isinstance(kind, str) and isinstance(item.get("id"), str) and not item["id"].startswith(f"{kind}-{review}-"):
            errors.append(f"{where}: id does not start with '{kind}-{review}-' (01 section 10.4 check 2; the exact n of a TRR-Dn log)")
    errors.extend(history_errors(item, where))
    return errors


def history_errors(item: dict[str, Any], where: str) -> list[str]:
    """The history is a legal 01 section 10.3 path from Open to the item's state."""
    history = item.get("history")
    if not isinstance(history, list):
        return []  # the schema reports a missing history
    entries = [h for h in history if isinstance(h, dict)]
    if not entries:
        return [f"{where}: history is empty; the first entry is from null to Open dated 'opened' (01 section 10.3)"]
    errors: list[str] = []
    first = entries[0]
    if first.get("from") is not None or first.get("to") != "Open":
        errors.append(f"{where}: history[0] is from {first.get('from')!r} to {first.get('to')!r}; the first entry is from null to Open (01 section 10.3)")
    if first.get("date") != item.get("opened"):
        errors.append(f"{where}: history[0] is dated {first.get('date')!r} but opened is {item.get('opened')!r}")
    previous = first
    for position, entry in enumerate(entries[1:], start=1):
        before, after = entry.get("from"), entry.get("to")
        if previous.get("to") in TERMINAL_STATES:
            errors.append(f"{where}: history[{position}] follows the terminal state {previous.get('to')} (Closed and Withdrawn are terminal, 01 section 10.3)")
        if before != previous.get("to"):
            errors.append(f"{where}: history[{position}] is from {before!r} but the previous entry ends in {previous.get('to')!r}")
        elif before == after:
            if before in TERMINAL_STATES:
                errors.append(f"{where}: history[{position}] is a same-state entry in the terminal state {before}")
        elif (before, after) not in LOG_TRANSITIONS:
            errors.append(f"{where}: history[{position}] {before} to {after} is not a transition of 01 section 10.3 (no state is skipped)")
        earlier, later = parse_iso(previous.get("date")), parse_iso(entry.get("date"))
        if earlier is not None and later is not None and later < earlier:
            errors.append(f"{where}: history[{position}] is dated {entry.get('date')}, before the previous entry ({previous.get('date')})")
        previous = entry
    state = item.get("state")
    if previous.get("to") != state:
        errors.append(f"{where}: state is {state!r} but the history ends in {previous.get('to')!r} (tools/review_trend.py reads states from the history)")
    closed = item.get("closed")
    if state in TERMINAL_STATES:
        terminal = next((h for h in entries if h.get("to") == state and h.get("from") != state), None)
        if terminal is not None and closed != terminal.get("date"):
            errors.append(f"{where}: closed is {closed!r} but the history enters {state} on {terminal.get('date')!r}")
    elif closed is not None:
        errors.append(f"{where}: closed is {closed!r} while the state is {state!r} (closed is set only for Closed or Withdrawn)")
    return errors


def check_rfa_rid_log(result: FileResult, root: Path, template: bool = False) -> list[tuple[int, str, str]]:
    """Cross-file rules of an RFA/RID log (01 sections 10.3, 10.4 and 10.6).

    Returns (item index, verification.record, item product) for every record
    the log names, for the product cross-check against the records. A template
    example (template=True) gets the item and history rules only.
    """
    references: list[tuple[int, str, str]] = []
    folder = None if template else review_folder(result.document, root)
    if folder is not None and not REVIEW_TOKEN.match(folder):
        result.errors.append(token_error(folder))
    data, error = load_json(result.document)
    if error is not None or not isinstance(data, dict):
        return references
    review = data.get("review")
    if folder is not None and isinstance(review, str) and review != folder:
        result.errors.append(f"review: '{review}' but the log is in docs/reviews/{folder}/ (the log names its own review)")
    items = data.get("items")
    if not isinstance(items, list):
        return references
    for index, item in enumerate(items):
        if not isinstance(item, dict):
            continue
        result.errors.extend(item_errors(item, index, review if isinstance(review, str) else None))
        if template:
            continue
        verification = item.get("verification")
        record = verification.get("record") if isinstance(verification, dict) else None
        if isinstance(record, str):
            if not (root / record).is_file():
                result.errors.append(f"items[{index}].verification.record: '{record}' does not exist (the verifying peer-review record is committed before the item is Verified)")
            else:
                references.append((index, record, item.get("product") if isinstance(item.get("product"), str) else ""))
    return references


def critical_module(product: str, slug: str) -> str | None:
    """The 07 section 14.1 safety- or mission-critical module a product belongs to, else None.

    Read from 'sw-<sub>' tokens in the product path or the record slug, and
    from path segments named after a critical module's <sub> under firmware/
    and docs/design/sw/ (code and module design products).
    """
    critical = {m.split("-", 1)[1].lower(): m for m in SAFETY_CRITICAL_MODULES + MISSION_CRITICAL_MODULES}
    text = f"{product.lower()} {slug.lower()}"
    for match in SW_MODULE_TOKEN.finditer(text):
        if match.group(1) in critical:
            return critical[match.group(1)]
    lowered = product.lower()
    if lowered.startswith("firmware/") or lowered.startswith("docs/design/sw/"):
        for part in re.split(r"[/._-]", lowered):
            if part in critical:
                return critical[part]
    return None


def assurance_reason(product: str, slug: str) -> str | None:
    """Why the product needs the software assurance reviewer (07 sections 2.1.1 and 14.1), else None."""
    base = product.split("#", 1)[0]
    if base in ASSURANCE_WHOLE_PRODUCTS:
        return f"{base} needs the assurance review as a whole (07 section 2.1.1)"
    module = critical_module(base, slug)
    if module is not None:
        kind = "safety-critical" if module in SAFETY_CRITICAL_MODULES else "mission-critical"
        return f"the product belongs to {kind} module {module} (07 section 14.1)"
    return None


def open_major_findings(body: str) -> list[str]:
    """Body lines that name a finding-<n> anchor with severity Major and state Open (01 section 13)."""
    hits: list[str] = []
    for line in body.splitlines():
        anchor = FINDING_ANCHOR.search(line)
        if anchor and all(word.search(line) for word in OPEN_MAJOR):
            hits.append(anchor.group(0))
    return hits


def validate_peer_review_record(document: Path, root: Path, templates_present: bool) -> tuple[FileResult, str | None, str | None]:
    """Validate the front matter of one filled checklist. Returns the result, its INSP id and its product."""
    result = FileResult("peer_review_record", document, document, schema_label=PEER_REVIEW_RECORD_LABEL)
    location = rel(document, root)
    folder = review_folder(document, root)
    if folder is not None and not REVIEW_TOKEN.match(folder):
        result.errors.append(token_error(folder))
    if not PRODUCT_SLUG_FILE.match(document.name):
        result.errors.append(f"file name '{document.name}' is not <product-slug>.md (lower case, digits, '.', '_' and '-')")
    try:
        text = document.read_text(encoding="utf-8")
    except OSError as exc:
        result.errors.append(f"cannot read: {exc}")
        return result, None, None
    front = parse_front_matter(text)
    if front is None:
        result.errors.append("no YAML front matter; the filled checklist is the peer-review record and carries id: INSP-NNN (charter section 5)")
        return result, None, None
    data = json_ready(front)
    result.errors.extend(validate_mapping(data, PEER_REVIEW_RECORD_SCHEMA))
    checklist_file = data.get("checklist_file")
    if isinstance(checklist_file, str) and checklist_file != location:
        result.errors.append(f"checklist_file: '{checklist_file}' but the record is {location} (one record per product, charter section 5)")
    checklist = data.get("checklist")
    if templates_present and isinstance(checklist, str) and not (root / TEMPLATES_DIR / f"{checklist}.md").is_file():
        result.errors.append(f"checklist: '{checklist}' has no template {TEMPLATES_DIR}/{checklist}.md")
    author, reviewer = data.get("author_agent"), data.get("reviewer_agent")
    if isinstance(author, str) and isinstance(reviewer, str) and author == reviewer:
        result.errors.append(f"reviewer_agent: '{reviewer}' is also the author_agent; the reviewer is never the author (charter sections 2 and 11 rule 4; NPR 7123.1D App. G Table G-19 entrance 2)")
    product = data.get("product") if isinstance(data.get("product"), str) else ""
    reason = assurance_reason(product, document.stem)
    if reason is not None:
        assurance = data.get("assurance_reviewer_agent")
        if not isinstance(assurance, str) or assurance.strip().lower() == NO_ASSURANCE:
            result.errors.append(f"assurance_reviewer_agent: {assurance!r}; {reason}, so a software assurance reviewer is a required participant (SWE-088 d)")
        elif assurance in (author, reviewer):
            result.errors.append(f"assurance_reviewer_agent: '{assurance}' is the author or the reviewer; the assurance reviewer is a distinct invocation (07 section 2.1)")
    if data.get("verdict") == "APPROVED":
        if data.get("readiness_met") is not True:
            result.errors.append("verdict: APPROVED but readiness_met is not true (SWE-088 b: established readiness criteria)")
        blocking = open_major_findings(body_after_front_matter(text))
        if blocking:
            result.errors.append(f"verdict: APPROVED but {', '.join(blocking)} is a Major finding in state Open (SWE-088 b, c: zero open Major findings)")
    ident = data.get("id")
    return result, ident if isinstance(ident, str) else None, product or None


def validate_decision_memo(document: Path, root: Path) -> FileResult:
    """Front matter of docs/reviews/<REVIEW>/decision-memo.md (01 sections 11, 12.1 and 12.2)."""
    result = FileResult("decision_memo", document, document, schema_label=DECISION_MEMO_LABEL)
    folder = review_folder(document, root)
    if folder is not None and not REVIEW_TOKEN.match(folder):
        result.errors.append(token_error(folder))
    try:
        text = document.read_text(encoding="utf-8")
    except OSError as exc:
        result.errors.append(f"cannot read: {exc}")
        return result
    front = parse_front_matter(text)
    if front is None:
        result.errors.append("no YAML front matter; the memo carries review, disposition and signed (docs/templates/decision-memo.md)")
        return result
    data = json_ready(front)
    result.errors.extend(validate_mapping(data, DECISION_MEMO_SCHEMA))
    review, disposition, signed = data.get("review"), data.get("disposition"), data.get("signed")
    if folder is not None and isinstance(review, str) and review != folder:
        result.errors.append(f"review: '{review}' but the memo is in docs/reviews/{folder}/ (the memo names its own review)")
    if (disposition is None) != (signed is None):
        result.errors.append(f"disposition {disposition!r} and signed {signed!r}: both are set by the approving session or both stay null (01 section 12.1)")
    revoked = data.get("revoked")
    if revoked is not None:
        if signed is None:
            result.errors.append("revoked is set but signed is null; only an approval can be revoked (01 section 12.2)")
        elif isinstance(revoked, str) and isinstance(signed, str) and revoked < signed:
            result.errors.append(f"revoked {revoked} is earlier than signed {signed}")
    tag = data.get("baseline_tag")
    if tag is not None:
        if signed is None:
            result.errors.append("baseline_tag is set but signed is null; the tag follows the approving memo commit (01 section 13, baseline tag row)")
        if isinstance(review, str) and review not in BASELINED_REVIEWS:
            result.errors.append(f"baseline_tag is set but {review} sets no baseline (charter section 8: baselines at SRR, PDR, CDR and SAR; docs/templates/decision-memo.md)")
        elif isinstance(review, str) and isinstance(tag, str) and tag != f"baseline/{review.lower()}":
            result.errors.append(f"baseline_tag '{tag}' but the review is {review} (baseline/{review.lower()})")
    return result


PRODUCT_FILE_ENTRY = re.compile(r"^([^@\s]+)@([0-9a-f]{7,40})$")
DRIFT_RULE = "record drift rule: an APPROVED record names the committed blobs it reviewed (SRR package section 2.3, R13)"


def head_blobs(root: Path) -> tuple[dict[str, str] | None, str]:
    """{path: blob} of HEAD when root is the top of a git work tree with a HEAD commit; else (None, reason)."""
    try:
        top = subprocess.run(["git", "-C", str(root), "rev-parse", "--show-toplevel"], capture_output=True, text=True, check=False)
    except OSError as exc:
        return None, f"git is not available ({exc})"
    if top.returncode != 0 or Path(top.stdout.strip()).resolve() != root.resolve():
        return None, f"{root} is not the top of a git work tree"
    tree = subprocess.run(["git", "-C", str(root), "ls-tree", "-r", "--full-tree", "HEAD"], capture_output=True, text=True, check=False)
    if tree.returncode != 0:
        return None, "the repository has no HEAD commit"
    blobs = {}
    for line in tree.stdout.splitlines():
        meta, _, path = line.partition("\t")
        parts = meta.split()
        if len(parts) == 3 and parts[1] == "blob":
            blobs[path] = parts[2]
    return blobs, ""


def named_blobs(data: dict[str, Any]) -> list[tuple[str, str]]:
    """(path, blob) pairs a record names in product_files and product_blob."""
    named = []
    files = data.get("product_files")
    if isinstance(files, list):
        for entry in files:
            match = PRODUCT_FILE_ENTRY.match(str(entry))
            if match:
                named.append((match.group(1), match.group(2)))
    blob, product = data.get("product_blob"), data.get("product")
    if isinstance(blob, str) and isinstance(product, str) and re.fullmatch(r"[0-9a-f]{7,40}", blob):
        named.append((product.strip(), blob))
    return named


def check_record_drift(result: FileResult, data: dict[str, Any], blobs: dict[str, str]) -> None:
    approved = data.get("verdict") == "APPROVED"
    named = named_blobs(data)
    if approved and not named:
        result.errors.append(f"verdict: APPROVED but the record names no reviewed blob in product_files (path@blob) or product_blob; {DRIFT_RULE}")
        return
    for path, blob in named:
        head = blobs.get(path)
        if head is None:
            message = f"product_files: {path}@{blob[:8]} is not in HEAD"
        elif not head.startswith(blob):
            message = f"product_files: {path}@{blob[:8]} differs from HEAD blob {head[:8]} (the committed product is not the reviewed one)"
        else:
            continue
        if approved:
            result.errors.append(f"{message}; {DRIFT_RULE}")
        else:
            result.notes.append(f"record drift: {message}")


def validate_reviews(root: Path) -> tuple[list[FileResult], dict[str, str]]:
    """Peer-review records, decision memos, folder tokens and the forbidden peer-reviews/ folder.

    Returns the results and a map of record path -> record product.
    """
    results: list[FileResult] = []
    products: dict[str, str] = {}
    templates_present = (root / TEMPLATES_DIR).is_dir()
    seen: dict[str, str] = {}
    records = [d for d in sorted(root.glob(PEER_REVIEW_RECORD_GLOB)) if d.is_file()]
    blobs, drift_off = head_blobs(root) if records else (None, "")
    for document in records:
        result, ident, product = validate_peer_review_record(document, root, templates_present)
        if blobs is None:
            if drift_off:
                result.notes.append(f"record drift rule not applied: {drift_off}")
        else:
            front = parse_front_matter(document.read_text(encoding="utf-8"))
            if front is not None:
                check_record_drift(result, json_ready(front), blobs)
        if ident is not None:
            if ident in seen:
                result.errors.append(f"id: {ident} already used by {seen[ident]} (ids are never reused, charter section 6)")
            else:
                seen[ident] = rel(document, root)
        if product is not None:
            products[rel(document, root)] = product
        results.append(result)
    for document in sorted(root.glob(DECISION_MEMO_GLOB)):
        if document.is_file():
            results.append(validate_decision_memo(document, root))
    for folder in sorted(root.glob(FORBIDDEN_PEER_REVIEWS_GLOB)):
        if folder.is_dir():
            results.append(
                FileResult(
                    "peer_review_record",
                    folder,
                    folder,
                    ["charter section 5 (amended 2026-09-25): there is no peer-reviews/ folder; the filled checklist docs/reviews/<REVIEW>/checklists/<product-slug>.md with id: INSP-NNN in its front matter is the single peer-review record"],
                    schema_label=PEER_REVIEW_RECORD_LABEL,
                )
            )
    return results, products


def check_review_folders(root: Path, results: list[FileResult]) -> list[FileResult]:
    """Every folder under docs/reviews/ is a review token; one finding per folder not already reported."""
    reviews = root / REVIEWS_DIR
    if not reviews.is_dir():
        return []
    reported = {review_folder(r.document, root) for r in results if any("is not a review token" in e for e in r.errors)}
    extra: list[FileResult] = []
    for folder in sorted(p for p in reviews.iterdir() if p.is_dir() and not p.name.startswith(".")):
        if not REVIEW_TOKEN.match(folder.name) and folder.name not in reported:
            extra.append(FileResult("review_folder", folder, folder, [token_error(folder.name) + "; docs/reviews/ holds only review folders"], schema_label=REVIEW_FOLDER_LABEL))
    return extra


def validate_all(root: Path) -> list[FileResult]:
    """Discover and validate every conventional document under root."""
    cache: dict[Path, Any] = {}
    results: list[FileResult] = []
    log_references: list[tuple[FileResult, int, str, str]] = []
    for item in discover(root):
        result = validate_document(item.document, item.schema, cache, item.convention)
        if item.convention == "rfa_rid_log":
            for index, record, product in check_rfa_rid_log(result, root):
                log_references.append((result, index, record, product))
        elif item.convention == "template_example" and item.document.name == f"{RFA_RID_TEMPLATE}.example.json":
            check_rfa_rid_log(result, root, template=True)
        results.append(result)
    review_results, products = validate_reviews(root)
    for result, index, record, product in log_references:
        recorded = products.get(record)
        if recorded is not None and product and recorded.split("#", 1)[0] != product.split("#", 1)[0]:
            result.errors.append(f"items[{index}].verification.record: {record} reviews '{recorded}', not the item's product '{product}'")
    results.extend(review_results)
    results.extend(check_review_folders(root, results))
    results.sort(key=lambda r: str(r.document))
    return results


# ----------------------------------------------------------------------------
# Reporting
# ----------------------------------------------------------------------------


def rel(path: Path, root: Path | None = None) -> str:
    """Path relative to root (or REPO_ROOT) when possible, else absolute."""
    base = root if root is not None else REPO_ROOT
    try:
        return str(path.resolve().relative_to(base.resolve()))
    except ValueError:
        return str(path)


def schema_text(result: FileResult, root: Path) -> str:
    return result.schema_label if result.schema_label is not None else rel(result.schema, root)


def print_results(results: list[FileResult], root: Path, quiet: bool) -> None:
    for result in results:
        if result.passed:
            if not quiet:
                print(f"PASS  {rel(result.document, root)}  (schema: {schema_text(result, root)})")
                for note in result.notes:
                    print(f"      note: {note}")
            continue
        print(f"FAIL  {rel(result.document, root)}  (schema: {schema_text(result, root)})")
        for error in result.errors:
            print(f"      - {error}")
        if not quiet:
            for note in result.notes:
                print(f"      note: {note}")
    if not quiet:
        passed = sum(1 for result in results if result.passed)
        failed = len(results) - passed
        if not results:
            print("validate_docs: no documents discovered under", root)
        print(f"validate_docs: {passed} passed, {failed} failed, {len(results)} checked")


def run(root: Path, quiet: bool = False) -> int:
    results = validate_all(root)
    print_results(results, root, quiet)
    return 0 if all(result.passed for result in results) else 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0], formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=REPO_ROOT, help="repository root (default: the parent of tools/)")
    parser.add_argument("--quiet", action="store_true", help="print only failures; the exit status carries the result")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    if not root.is_dir():
        parser.error(f"root is not a directory: {root}")
    return run(root, args.quiet)


if __name__ == "__main__":
    sys.exit(main())
