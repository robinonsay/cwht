#!/usr/bin/env python3
"""Review-trend TPM (NPR 7123.1D SE-64) for cwht: RFA and RID counts, burndown and alert zone.

Implements docs/process/01-lifecycle-and-reviews.md section 11 (charter section 4
item 5). Inputs, all read from the repository so every value is reproducible:

    docs/reviews/*/rfa-rid-log.json      the RFA/RID logs, validated against
                                         docs/templates/rfa-rid-log.schema.json
    docs/reviews/*/decision-memo.md      front matter key 'signed' (ISO date or null):
                                         the gate date of that review
    --date YYYY-MM-DD                    the package date T (default: today)

Computed per review R, per type (RID, RFA) and severity (all, Major, Minor,
Blocking, Routine), with every state evaluated at T from the item history:

    raised            items of R opened on or before T
    open              items in state Open or Answered at T
    verified_pending  items in state Verified at T
    closed            items in state Closed at T (closed <= T)
    withdrawn         items in state Withdrawn at T
    overdue           open or verified_pending items whose due_date < T, or whose
                      due_review has a decision memo signed before T
    closure_fraction_at_gate
                      closed / (raised - withdrawn) at the signing date of the next
                      gate (the first review after R in the order SRR, PDR, CDR,
                      TRR, TRR-D1, TRR-D2, ..., SAR whose memo is signed, on or
                      before T); undefined until then or when raised == withdrawn
    age_open          median and maximum of T - opened over open items, in days
    age_closed        median of closed - opened over closed items, in days
    burndown          for every date on which an item was raised, closed or
                      withdrawn: cumulative raised and cumulative closed plus
                      withdrawn (the dates where the plotted step lines move)

Alert zone per review at T (SE HB 6.7.1.2.1 colour coding, 01 section 11), in
this order: Red when R is dispositioned (memo signed on or before T) and a Major
RID or Blocking RFA of R is not Closed or Withdrawn, or closure_fraction_at_gate
< 0.8, or overdue > 3; else Green when overdue == 0; else Yellow when every
overdue item is Minor or Routine and closure_fraction_at_gate is >= 0.8 or
undefined; else Red. The overall zone is the worst review zone (Green with no
log).

Outputs: a text summary on stdout (or the JSON result with --json). With
--write --package REVIEW (the review whose package is being built) the tool
also writes docs/reviews/<REVIEW>/figures/review-trend.png and appends one
history entry per logged review to the TPM keyed review-trend (TPM-003) in
docs/plan/tpm.json, replacing entries of an earlier run for the same package
and date; only that history array is rewritten in the file.

Exit status: 0 when every zone is Green or Yellow (including when no log exists
yet), 1 when any zone is Red (01 section 11: a Red zone blocks the readiness
declaration), 2 on a usage error or invalid input.

Usage:
    .venv/bin/python tools/review_trend.py [--root PATH] [--date YYYY-MM-DD] [--json]
    .venv/bin/python tools/review_trend.py --package REVIEW --write [--root PATH] [--date YYYY-MM-DD]
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import statistics
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
import validate_docs  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[1]
LOG_GLOB = "docs/reviews/*/rfa-rid-log.json"
MEMO_GLOB = "docs/reviews/*/decision-memo.md"
LOG_SCHEMA = Path("docs/templates/rfa-rid-log.schema.json")
TPM_FILE = Path("docs/plan/tpm.json")
TPM_KEY = "review-trend"
TPM_ID = "TPM-003"
FIGURE_NAME = "review-trend.png"
REVIEW_TOKEN = re.compile(r"^(SRR|PDR|CDR|TRR|SAR|TRR-D([1-9][0-9]?))$")
BASE_ORDER = ("SRR", "PDR", "CDR", "TRR")

OPEN_STATES = ("Open", "Answered")
PENDING_STATES = ("Verified",)
NOT_TERMINAL = OPEN_STATES + PENDING_STATES
SEVERITIES: dict[str, tuple[str, ...]] = {"RID": ("Major", "Minor"), "RFA": ("Blocking", "Routine")}
BLOCKING_SEVERITIES = ("Major", "Blocking")
CLOSURE_THRESHOLD = 0.8
OVERDUE_RED_LIMIT = 3
GREEN, YELLOW, RED = "Green", "Yellow", "Red"
ZONE_RANK = {GREEN: 0, YELLOW: 1, RED: 2}

# Figure styling (dataviz reference palette, light surface; categorical slots 1 and 2).
SURFACE = "#fcfcfb"
TEXT_PRIMARY = "#0b0b0b"
TEXT_SECONDARY = "#52514e"
GRID = "#e4e3df"
SERIES_RAISED = "#2a78d6"
SERIES_CLOSED = "#eb6834"


class InputError(Exception):
    """An input file is missing, unreadable or invalid (exit status 2)."""


def review_rank(token: str) -> tuple[int, int]:
    """Position in the life-cycle order SRR, PDR, CDR, TRR, TRR-D1, TRR-D2, ..., SAR."""
    match = REVIEW_TOKEN.match(token)
    if match is None:
        return (99, 0)
    if token in BASE_ORDER:
        return (BASE_ORDER.index(token), 0)
    if token == "SAR":
        return (5, 0)
    return (4, int(match.group(2)))


def parse_date(value: Any, where: str) -> dt.date | None:
    """An ISO date from JSON or YAML (string or date); None for null."""
    if value is None:
        return None
    if isinstance(value, dt.datetime):
        return value.date()
    if isinstance(value, dt.date):
        return value
    if isinstance(value, str):
        try:
            return dt.date.fromisoformat(value)
        except ValueError as exc:
            raise InputError(f"{where}: '{value}' is not an ISO date") from exc
    raise InputError(f"{where}: {value!r} is not an ISO date")


# ----------------------------------------------------------------------------
# Data model
# ----------------------------------------------------------------------------


@dataclass
class Transition:
    date: dt.date
    to: str


@dataclass
class Item:
    id: str
    type: str
    severity: str
    review: str
    state: str
    opened: dt.date
    closed: dt.date | None
    due_review: str | None
    due_date: dt.date | None
    history: list[Transition] = field(default_factory=list)

    def state_at(self, when: dt.date) -> str | None:
        """State at the end of day 'when' from the history; None when not yet raised."""
        if self.opened > when:
            return None
        state = "Open"
        for step in self.history:
            if step.date <= when:
                state = step.to
        return state

    def terminal_date(self) -> dt.date | None:
        """Date the item entered Closed or Withdrawn, from the history, else the closed field."""
        for step in self.history:
            if step.to in ("Closed", "Withdrawn"):
                return step.date
        return self.closed if self.state in ("Closed", "Withdrawn") else None


@dataclass
class ReviewLog:
    review: str
    path: str
    items: list[Item]


def load_log(path: Path, root: Path | None = None, validate: bool = True) -> ReviewLog:
    """Load one RFA/RID log; with validate, check it against the schema first."""
    location = validate_docs.rel(path, root) if root is not None else str(path)
    if validate and root is not None:
        result = validate_docs.validate_document(path, root / LOG_SCHEMA)
        if not result.passed:
            raise InputError(f"{location} fails {LOG_SCHEMA}: " + "; ".join(result.errors[:5]))
    data, error = validate_docs.load_json(path)
    if error is not None or not isinstance(data, dict):
        raise InputError(f"{location}: {error or 'not a JSON object'}")
    items: list[Item] = []
    for index, raw in enumerate(data.get("items", [])):
        where = f"{location} items[{index}]"
        history = sorted(
            (Transition(parse_date(h.get("date"), f"{where}.history") or dt.date.min, str(h.get("to"))) for h in raw.get("history", []) if isinstance(h, dict)),
            key=lambda step: step.date,
        )
        opened = parse_date(raw.get("opened"), f"{where}.opened")
        if opened is None:
            raise InputError(f"{where}: opened is required")
        items.append(
            Item(
                id=str(raw.get("id")),
                type=str(raw.get("type")),
                severity=str(raw.get("severity")),
                review=str(raw.get("review")),
                state=str(raw.get("state")),
                opened=opened,
                closed=parse_date(raw.get("closed"), f"{where}.closed"),
                due_review=raw.get("due_review") if isinstance(raw.get("due_review"), str) else None,
                due_date=parse_date(raw.get("due_date"), f"{where}.due_date"),
                history=history,
            )
        )
    return ReviewLog(review=str(data.get("review")), path=location, items=items)


def load_logs(root: Path) -> list[ReviewLog]:
    logs = [load_log(path, root) for path in sorted(root.glob(LOG_GLOB)) if path.is_file()]
    return sorted(logs, key=lambda log: review_rank(log.review))


def load_memo_dates(root: Path) -> dict[str, dt.date | None]:
    """Review token -> 'signed' date of docs/reviews/<REVIEW>/decision-memo.md (None while unsigned)."""
    dates: dict[str, dt.date | None] = {}
    for path in sorted(root.glob(MEMO_GLOB)):
        review = path.parent.name
        front = validate_docs.parse_front_matter(path.read_text(encoding="utf-8"))
        if front is None or "signed" not in front:
            raise InputError(f"{validate_docs.rel(path, root)}: no front matter key 'signed' (docs/templates/decision-memo.md)")
        dates[review] = parse_date(front.get("signed"), f"{validate_docs.rel(path, root)} signed")
    return dates


# ----------------------------------------------------------------------------
# Measures
# ----------------------------------------------------------------------------


def is_overdue(item: Item, when: dt.date, memos: dict[str, dt.date | None]) -> bool:
    if item.state_at(when) not in NOT_TERMINAL:
        return False
    if item.due_date is not None and item.due_date < when:
        return True
    if item.due_review is not None:
        signed = memos.get(item.due_review)
        return signed is not None and signed < when
    return False


def counts(items: list[Item], when: dt.date, memos: dict[str, dt.date | None]) -> dict[str, int]:
    states = [item.state_at(when) for item in items]
    return {
        "raised": sum(1 for s in states if s is not None),
        "open": sum(1 for s in states if s in OPEN_STATES),
        "verified_pending": sum(1 for s in states if s in PENDING_STATES),
        "closed": sum(1 for s in states if s == "Closed"),
        "withdrawn": sum(1 for s in states if s == "Withdrawn"),
        "overdue": sum(1 for item in items if is_overdue(item, when, memos)),
    }


def next_gate(review: str, memos: dict[str, dt.date | None], when: dt.date) -> tuple[str, dt.date] | None:
    """The first review after 'review' in the life-cycle order whose memo is signed on or before 'when'."""
    later = sorted((token for token, signed in memos.items() if signed is not None and signed <= when and review_rank(token) > review_rank(review)), key=review_rank)
    if not later:
        return None
    signed = memos[later[0]]
    assert signed is not None
    return later[0], signed


def closure_fraction(items: list[Item], at: dt.date, memos: dict[str, dt.date | None]) -> float | None:
    c = counts(items, at, memos)
    denominator = c["raised"] - c["withdrawn"]
    return None if denominator <= 0 else c["closed"] / denominator


def days(later: dt.date, earlier: dt.date) -> int:
    return (later - earlier).days


def burndown(items: list[Item], when: dt.date) -> list[dict[str, Any]]:
    events = {item.opened for item in items if item.opened <= when}
    events |= {d for d in (item.terminal_date() for item in items) if d is not None and d <= when}
    series = []
    for day in sorted(events):
        series.append(
            {
                "date": day.isoformat(),
                "raised": sum(1 for item in items if item.opened <= day),
                "closed_or_withdrawn": sum(1 for item in items if item.state_at(day) in ("Closed", "Withdrawn")),
            }
        )
    return series


def zone_for(log: ReviewLog, when: dt.date, memos: dict[str, dt.date | None], fraction: float | None) -> tuple[str, list[str]]:
    """Alert zone of one review at 'when' with the reasons that decided it."""
    reasons: list[str] = []
    signed = memos.get(log.review)
    dispositioned = signed is not None and signed <= when
    blocking_open = [i.id for i in log.items if i.severity in BLOCKING_SEVERITIES and i.state_at(when) in NOT_TERMINAL]
    overdue_items = [i for i in log.items if is_overdue(i, when, memos)]
    if dispositioned and blocking_open:
        reasons.append(f"Major RID or Blocking RFA open after the {log.review} memo: {', '.join(blocking_open)}")
    if fraction is not None and fraction < CLOSURE_THRESHOLD:
        reasons.append(f"closure_fraction_at_gate {fraction:.2f} < {CLOSURE_THRESHOLD}")
    if len(overdue_items) > OVERDUE_RED_LIMIT:
        reasons.append(f"overdue {len(overdue_items)} > {OVERDUE_RED_LIMIT}")
    if reasons:
        return RED, reasons
    if not overdue_items:
        return GREEN, ["overdue 0 and no Major RID or Blocking RFA open from a dispositioned review"]
    blocking_overdue = [i.id for i in overdue_items if i.severity in BLOCKING_SEVERITIES]
    if not blocking_overdue:
        return YELLOW, [f"overdue {len(overdue_items)}, all Minor or Routine: {', '.join(i.id for i in overdue_items)}"]
    return RED, [f"overdue Major RID or Blocking RFA: {', '.join(blocking_overdue)}"]


def review_result(log: ReviewLog, when: dt.date, memos: dict[str, dt.date | None]) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    for kind, severities in SEVERITIES.items():
        of_kind = [i for i in log.items if i.type == kind]
        rows.append({"type": kind, "severity": "all", **counts(of_kind, when, memos)})
        for severity in severities:
            rows.append({"type": kind, "severity": severity, **counts([i for i in of_kind if i.severity == severity], when, memos)})
    gate = next_gate(log.review, memos, when)
    fraction = closure_fraction(log.items, gate[1], memos) if gate is not None else None
    open_ages = [days(when, i.opened) for i in log.items if i.state_at(when) in OPEN_STATES]
    closed_ages = [days(i.terminal_date() or when, i.opened) for i in log.items if i.state_at(when) == "Closed"]
    zone, reasons = zone_for(log, when, memos, fraction)
    total = counts(log.items, when, memos)
    signed = memos.get(log.review)
    return {
        "log": log.path,
        "memo_signed": signed.isoformat() if signed is not None else None,
        "rows": rows,
        "totals": total,
        "closure_fraction_at_T": None if total["raised"] - total["withdrawn"] <= 0 else round(total["closed"] / (total["raised"] - total["withdrawn"]), 3),
        "next_gate": gate[0] if gate else None,
        "closure_fraction_at_gate": None if fraction is None else round(fraction, 3),
        "age_open_median_days": statistics.median(open_ages) if open_ages else None,
        "age_open_max_days": max(open_ages) if open_ages else None,
        "age_closed_median_days": statistics.median(closed_ages) if closed_ages else None,
        "zone": zone,
        "zone_reasons": reasons,
        "burndown": burndown(log.items, when),
    }


def compute(logs: list[ReviewLog], memos: dict[str, dt.date | None], when: dt.date) -> dict[str, Any]:
    reviews = {log.review: review_result(log, when, memos) for log in logs}
    overall = max((r["zone"] for r in reviews.values()), key=lambda z: ZONE_RANK[z], default=GREEN)
    return {
        "date": when.isoformat(),
        "memos": {k: (v.isoformat() if v else None) for k, v in sorted(memos.items(), key=lambda kv: review_rank(kv[0]))},
        "overall_zone": overall,
        "reviews": reviews,
    }


# ----------------------------------------------------------------------------
# Outputs
# ----------------------------------------------------------------------------


def text_summary(result: dict[str, Any]) -> str:
    lines = [f"review_trend: T = {result['date']}; overall zone {result['overall_zone']}"]
    if not result["reviews"]:
        lines.append(f"review_trend: no RFA/RID log under {LOG_GLOB}; nothing to trend yet")
        return "\n".join(lines)
    for review, data in result["reviews"].items():
        lines.append("")
        lines.append(f"{review} ({data['log']}; memo signed {data['memo_signed'] or 'not yet'}): zone {data['zone']} ({'; '.join(data['zone_reasons'])})")
        lines.append(f"  {'type':5s} {'severity':9s} {'raised':>6s} {'open':>5s} {'verif':>5s} {'closed':>6s} {'withdr':>6s} {'overdue':>7s}")
        for row in data["rows"]:
            lines.append(
                f"  {row['type']:5s} {row['severity']:9s} {row['raised']:6d} {row['open']:5d} {row['verified_pending']:5d} {row['closed']:6d} {row['withdrawn']:6d} {row['overdue']:7d}"
            )
        fraction = data["closure_fraction_at_gate"]
        fraction_text = "undefined (next gate not signed)" if fraction is None else f"{fraction} at the {data['next_gate']} memo"
        lines.append(
            f"  closure_fraction_at_gate: {fraction_text}; "
            f"age_open median {data['age_open_median_days']} max {data['age_open_max_days']} days; age_closed median {data['age_closed_median_days']} days"
        )
        lines.append("  burndown: " + "; ".join(f"{p['date']} raised {p['raised']}, closed+withdrawn {p['closed_or_withdrawn']}" for p in data["burndown"]))
    return "\n".join(lines)


def history_entries(result: dict[str, Any], package: str, figure: str) -> list[dict[str, Any]]:
    """TPM-003 history entries (docs/plan/tpm.json conventions.history_entry_shape)."""
    entries: list[dict[str, Any]] = []
    status = {GREEN: "green", YELLOW: "yellow", RED: "red"}
    if not result["reviews"]:
        entries.append(
            {
                "review": package, "date": result["date"], "cbe": None, "status": "green", "evidence": figure, "credit": False,
                "note": "No RFA/RID log exists at T; tools/review_trend.py (process indicator, credit not applicable)",
                "log_review": None, "raised": 0, "open": 0, "verified_pending": 0, "closed": 0, "withdrawn": 0, "overdue": 0,
                "closure_fraction_at_gate": None, "zone": GREEN,
            }
        )
        return entries
    for review, data in result["reviews"].items():
        totals = data["totals"]
        entries.append(
            {
                "review": package, "date": result["date"], "cbe": data["closure_fraction_at_T"], "status": status[data["zone"]], "evidence": figure, "credit": False,
                "note": f"{review} log {data['log']}: closure fraction at T; zone reasons: {'; '.join(data['zone_reasons'])}; tools/review_trend.py (process indicator, credit not applicable)",
                "log_review": review, **{k: totals[k] for k in ("raised", "open", "verified_pending", "closed", "withdrawn", "overdue")},
                "closure_fraction_at_gate": data["closure_fraction_at_gate"], "zone": data["zone"],
            }
        )
    return entries


def update_tpm_history(tpm_path: Path, entries: list[dict[str, Any]]) -> None:
    """Replace only the history array of the review-trend TPM, keeping the rest of the file byte for byte."""
    if not tpm_path.is_file():
        raise InputError(f"{tpm_path} not found; the review-trend TPM ({TPM_ID}) is registered there")
    text = tpm_path.read_text(encoding="utf-8")
    data = json.loads(text)
    tpm = next((t for t in data.get("tpms", []) if isinstance(t, dict) and (t.get("key") == TPM_KEY or t.get("id") == TPM_ID)), None)
    if tpm is None or not isinstance(tpm.get("history"), list):
        raise InputError(f"{tpm_path}: no TPM keyed '{TPM_KEY}' with a history array")
    key_at = text.find(f'"key": "{TPM_KEY}"')
    history_at = text.find('"history":', key_at)
    next_key = text.find('"key":', key_at + 1)
    if key_at < 0 or history_at < 0 or (0 <= next_key < history_at):
        raise InputError(f"{tpm_path}: cannot locate the history array of the '{TPM_KEY}' TPM")
    start = text.index("[", history_at)
    current, end = json.JSONDecoder().raw_decode(text, start)
    if current != tpm["history"]:
        raise InputError(f"{tpm_path}: located history array differs from the parsed one; file not changed")
    replaced = {(e["review"], e["date"]) for e in entries}
    history = [h for h in current if not (isinstance(h, dict) and (h.get("review"), h.get("date")) in replaced)] + entries
    line_start = text.rfind("\n", 0, history_at) + 1
    indent = text[line_start:history_at]
    serialized = json.dumps(history, indent=2, ensure_ascii=False).replace("\n", "\n" + indent)
    updated = text[:start] + serialized + text[end:]
    check = json.loads(updated)
    tpm_after = next(t for t in check["tpms"] if t.get("key") == TPM_KEY or t.get("id") == TPM_ID)
    if tpm_after["history"] != history:
        raise InputError(f"{tpm_path}: history rewrite did not round-trip; file not changed")
    tpm_path.write_text(updated, encoding="utf-8")


def plot(result: dict[str, Any], logs: list[ReviewLog], figure_path: Path) -> None:
    """Burndown step lines per review with the gate dates marked (01 section 11)."""
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.dates as mdates
    import matplotlib.pyplot as plt

    when = dt.date.fromisoformat(result["date"])
    panels = max(1, len(result["reviews"]))
    fig, axes = plt.subplots(panels, 1, figsize=(8.0, 2.9 * panels + 0.6), squeeze=False, facecolor=SURFACE)
    plt.rcParams.update({"font.size": 9})
    if not result["reviews"]:
        ax = axes[0][0]
        ax.set_facecolor(SURFACE)
        ax.axis("off")
        ax.text(0.5, 0.5, f"No RFA/RID log exists as of {result['date']}\nreview-trend TPM ({TPM_ID}): zone Green", ha="center", va="center", color=TEXT_SECONDARY, fontsize=11)
    gate_dates = {k: dt.date.fromisoformat(v) for k, v in result["memos"].items() if v}
    by_review = {log.review: log for log in logs}
    for ax, (review, data) in zip((row[0] for row in axes), result["reviews"].items()):
        ax.set_facecolor(SURFACE)
        log = by_review[review]
        start = min(i.opened for i in log.items) if log.items else when
        days_axis = [start + dt.timedelta(days=n) for n in range((when - start).days + 1)]
        raised = [sum(1 for i in log.items if i.opened <= d) for d in days_axis]
        closed = [sum(1 for i in log.items if i.state_at(d) in ("Closed", "Withdrawn")) for d in days_axis]
        ax.step(days_axis, raised, where="post", color=SERIES_RAISED, linewidth=2, label="raised (cumulative)", solid_joinstyle="round")
        ax.step(days_axis, closed, where="post", color=SERIES_CLOSED, linewidth=2, label="closed + withdrawn (cumulative)", solid_joinstyle="round")
        top = max(raised + [1])
        for token, signed in sorted(gate_dates.items(), key=lambda kv: kv[1]):
            if start <= signed <= when:
                ax.axvline(signed, color=TEXT_SECONDARY, linewidth=1)
                ax.text(signed, top * 1.27, f" {token} memo", color=TEXT_SECONDARY, va="top", ha="left", fontsize=8)
        ax.axvline(when, color=GRID, linewidth=1)
        ax.text(when, 0.05 * top, f" T {when.isoformat()}", color=TEXT_SECONDARY, ha="left", va="bottom", fontsize=8)
        ax.annotate(f"{raised[-1]} raised", (days_axis[-1], raised[-1]), textcoords="offset points", xytext=(6, 2), color=TEXT_PRIMARY, fontsize=8)
        ax.annotate(f"{closed[-1]} closed + withdrawn", (days_axis[-1], closed[-1]), textcoords="offset points", xytext=(6, -10), color=TEXT_PRIMARY, fontsize=8)
        ax.set_ylim(0, top * 1.3)
        ax.set_xlim(start - dt.timedelta(days=1), when + dt.timedelta(days=max(3, (when - start).days // 4)))
        ax.yaxis.get_major_locator().set_params(integer=True)
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
        for label in ax.get_xticklabels():  # each panel has its own date range: label every panel
            label.set_rotation(30)
            label.set_horizontalalignment("right")
        ax.grid(axis="y", color=GRID, linewidth=1)
        for spine in ("top", "right"):
            ax.spines[spine].set_visible(False)
        for spine in ("left", "bottom"):
            ax.spines[spine].set_color(GRID)
        ax.tick_params(colors=TEXT_SECONDARY, labelsize=8)
        fraction = data["closure_fraction_at_gate"]
        ax.set_title(
            f"{review} RFA/RID burndown: zone {data['zone']}; open {data['totals']['open']}, overdue {data['totals']['overdue']}, "
            f"closure at next gate {'n/a' if fraction is None else f'{fraction:.2f}'}",
            loc="left", color=TEXT_PRIMARY, fontsize=10,
        )
        ax.set_ylabel("items", color=TEXT_SECONDARY)
        ax.legend(loc="upper left", bbox_to_anchor=(1.01, 1.0), frameon=False, fontsize=8, labelcolor=TEXT_PRIMARY)
    fig.suptitle(f"Review trend ({TPM_ID}, NPR 7123.1D SE-64) at T = {result['date']}: overall zone {result['overall_zone']}", x=0.01, ha="left", color=TEXT_PRIMARY, fontsize=11)
    fig.tight_layout()
    figure_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(figure_path, dpi=150, facecolor=SURFACE, bbox_inches="tight")
    plt.close(fig)


# ----------------------------------------------------------------------------
# Entry point
# ----------------------------------------------------------------------------


def run(root: Path, when: dt.date, package: str | None = None, write: bool = False, as_json: bool = False) -> int:
    logs = load_logs(root)
    memos = load_memo_dates(root)
    result = compute(logs, memos, when)
    print(json.dumps(result, indent=2) if as_json else text_summary(result))
    if write:
        assert package is not None
        figure = Path("docs/reviews") / package / "figures" / FIGURE_NAME
        plot(result, logs, root / figure)
        update_tpm_history(root / TPM_FILE, history_entries(result, package, str(figure)))
        if not as_json:
            print(f"review_trend: wrote {figure} and {len(history_entries(result, package, str(figure)))} history entr(ies) to {TPM_FILE} ({TPM_ID})")
    return 1 if result["overall_zone"] == RED else 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0], formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=REPO_ROOT, help="repository root (default: the parent of tools/)")
    parser.add_argument("--date", default=None, help="package date T as YYYY-MM-DD (default: today)")
    parser.add_argument("--package", default=None, help="review whose package is being built (SRR, PDR, CDR, TRR, TRR-Dn, SAR); required with --write")
    parser.add_argument("--write", action="store_true", help="write docs/reviews/<PACKAGE>/figures/review-trend.png and append the TPM-003 history in docs/plan/tpm.json")
    parser.add_argument("--json", action="store_true", help="print the computed result as JSON instead of the text summary")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    if not root.is_dir():
        parser.error(f"root is not a directory: {root}")
    try:
        when = dt.date.fromisoformat(args.date) if args.date else dt.date.today()
    except ValueError:
        parser.error(f"--date {args.date!r} is not YYYY-MM-DD")
    if args.write and (args.package is None or not REVIEW_TOKEN.match(args.package)):
        parser.error("--write needs --package with a review token (SRR, PDR, CDR, TRR, TRR-Dn, SAR)")
    try:
        return run(root, when, args.package, args.write, args.json)
    except InputError as exc:
        print(f"review_trend: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
