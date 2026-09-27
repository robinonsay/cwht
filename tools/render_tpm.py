#!/usr/bin/env python3
"""TPM status table and trend plots for a review package (SEMP section 7.4; TV-017).

Reads docs/plan/tpm.json and writes, for one review, into docs/reviews/<REVIEW>/figures/:

    tpm-status.png         the full TPM table with the alert colour of each TPM (1920 x 1080 px)
    tpm-table.md           the same table in Markdown, for the review package
    tpm-trend-<key>.png    one trend plot per TPM that has at least one numeric cbe in its history
                           (1600 x 900 px); the review-trend TPM (key review-trend) is plotted by
                           tools/review_trend.py (01 section 11) and is only listed in the table

Status of each TPM at REVIEW (conventions.status_rule of tpm.json; the tool never re-evaluates a
recorded colour, because the phase margin policies and thresholds are prose):
  - the status of the last history entry whose review token equals REVIEW;
  - otherwise, when REVIEW is listed in reporting_review (a TRR-D<n> review matches "TRR-Dn"),
    red with the reason "no estimate at a reporting review", which the status rule makes red,
    and the latest earlier entry, if any, is shown as the carried value;
  - otherwise "not due" (grey), with the latest earlier entry shown as the carried value.
History entries dated after --date (default: today) are ignored.

Data checks, each a failure with exit status 1 and nothing written: tpms is a non-empty list;
ids match TPM-NNN and ids and keys are unique; every history entry has a review token of the
tpm.schema.json pattern, a YYYY-MM-DD date, a numeric or null cbe, a status of green, yellow or
red, and a boolean credit; each history is in date order. Schema validation of the whole file is
tools/validate_docs.py (TV-003); this tool checks only what it draws.

Usage:
    .venv/bin/python tools/render_tpm.py --review PDR [--tpm PATH] [--out DIR] [--date YYYY-MM-DD] [--check]

--check performs the data checks and prints the table without writing anything. Exit status: 0
success; 1 a data check failed (nothing written); 2 usage error or unreadable input.
Tools: the TV-001 interpreter with matplotlib 3.11.2 (lock section 2).
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys
from dataclasses import dataclass

REVIEW_RE = re.compile(r"^(SRR|PDR|CDR|TRR|SAR|TRR-D[1-9][0-9]?)$")
ENTRY_REVIEW_RE = re.compile(r"^(SRR|PDR|CDR|TRR|SAR|TRR-D[1-9][0-9]?|status-[0-9]{4}-[0-9]{2}-[0-9]{2})$")
DATE_RE = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$")
STATUSES = ("green", "yellow", "red")
REVIEW_TREND_KEY = "review-trend"

# Palette (status chips) and ink, shared with the SRR figure set of tools/render_review_figures.py.
COLOURS = {"green": "#2e7d32", "yellow": "#f2c200", "red": "#c62828", "not due": "#9e9e9e"}
INK, INK2, RULE = "#1b1b19", "#52514e", "#d6d5d0"
TABLE_W, TABLE_H = 1920, 1080
TREND_W, TREND_H = 1600, 900
# Table layout in pixels from the top-left corner (used by the known-answer pixel check).
TOP, HEADER_H, LEFT = 120, 44, 40
CHIP_X, CHIP_W = 1240, 120


class DataError(Exception):
    """A data check failed: exit status 1, nothing written."""


@dataclass
class Row:
    tpm_id: str
    key: str
    name: str
    units: str
    status: str            # green | yellow | red | not due
    reason: str            # "entry" | "no estimate at a reporting review" | "not a reporting review"
    cbe: float | None
    entry_review: str | None
    entry_date: str | None
    credit: bool | None
    evidence: str
    planned: float | None


def _is_number(x) -> bool:
    return isinstance(x, (int, float)) and not isinstance(x, bool)


def validate(data) -> list[dict]:
    tpms = data.get("tpms") if isinstance(data, dict) else None
    if not isinstance(tpms, list) or not tpms:
        raise DataError("tpms is missing or empty")
    ids, keys = set(), set()
    for t in tpms:
        tid, key = t.get("id"), t.get("key")
        if not isinstance(tid, str) or not re.fullmatch(r"TPM-[0-9]{3}", tid):
            raise DataError(f"bad TPM id {tid!r}")
        if tid in ids:
            raise DataError(f"duplicate id {tid}")
        if not isinstance(key, str) or key in keys:
            raise DataError(f"{tid}: missing or duplicate key {key!r}")
        ids.add(tid)
        keys.add(key)
        if not isinstance(t.get("reporting_review", []), list):
            raise DataError(f"{tid}: reporting_review is not a list")
        last = ""
        for i, h in enumerate(t.get("history", [])):
            where = f"{tid} history[{i}]"
            if not ENTRY_REVIEW_RE.match(str(h.get("review", ""))):
                raise DataError(f"{where}: review token {h.get('review')!r} is not a gate or status-YYYY-MM-DD token")
            if not DATE_RE.match(str(h.get("date", ""))):
                raise DataError(f"{where}: date {h.get('date')!r} is not YYYY-MM-DD")
            if h.get("cbe") is not None and not _is_number(h.get("cbe")):
                raise DataError(f"{where}: cbe {h.get('cbe')!r} is neither a number nor null")
            if h.get("status") not in STATUSES:
                raise DataError(f"{where}: status {h.get('status')!r} is not green, yellow or red")
            if not isinstance(h.get("credit"), bool):
                raise DataError(f"{where}: credit {h.get('credit')!r} is not true or false")
            if h["date"] < last:
                raise DataError(f"{where}: date {h['date']} is earlier than the entry before it ({last})")
            last = h["date"]
    return tpms


def reports_at(tpm: dict, review: str) -> bool:
    listed = tpm.get("reporting_review", [])
    return review in listed or (review.startswith("TRR-D") and "TRR-Dn" in listed)


def build_rows(data, review: str, asof: str) -> list[Row]:
    rows = []
    for t in validate(data):
        hist = [h for h in t.get("history", []) if h["date"] <= asof]
        own = [h for h in hist if h["review"] == review]
        planned = t.get("planned_value") if _is_number(t.get("planned_value")) else None
        units = str(t.get("units", ""))
        if own:
            h, status, reason = own[-1], own[-1]["status"], "entry"
        else:
            h = hist[-1] if hist else None
            if reports_at(t, review):
                status, reason = "red", "no estimate at a reporting review"
            else:
                status, reason = "not due", "not a reporting review"
        rows.append(Row(t["id"], t["key"], str(t.get("name", "")), units, status, reason,
                        h["cbe"] if h else None, h["review"] if h else None, h["date"] if h else None,
                        h["credit"] if h else None, str(h.get("evidence", "")) if h else "", planned))
    return rows


def trend_points(tpm: dict, asof: str) -> list[tuple[str, str, float, str]]:
    return [(h["review"], h["date"], float(h["cbe"]), h["status"])
            for h in tpm.get("history", []) if h["date"] <= asof and _is_number(h.get("cbe"))]


def short_units(units: str) -> str:
    u = re.split(r"[;(]", units, maxsplit=1)[0].strip()
    return u if len(u) <= 26 else u[:25] + "."


def fmt_cbe(cbe) -> str:
    return "none" if cbe is None else f"{cbe:g}"


def markdown(rows: list[Row], review: str, asof: str) -> str:
    out = [f"# TPM status at {review}", "",
           f"Generated by `tools/render_tpm.py --review {review}` from `docs/plan/tpm.json` (entries dated on or before {asof}). "
           "Status is the recorded status of the TPM's own entry for this review; a TPM without one is red when this review is "
           "one of its reporting reviews (conventions.status_rule: no estimate) and not due otherwise.", "",
           "| TPM | Key | Name | CBE | Units | Status | Basis | Entry | Credit | Evidence |",
           "|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        entry = f"{r.entry_review} {r.entry_date}" if r.entry_review else "none"
        credit = "n/a" if r.credit is None else str(r.credit).lower()
        out.append(f"| {r.tpm_id} | `{r.key}` | {r.name} | {fmt_cbe(r.cbe)} | {r.units} | {r.status} | {r.reason} | {entry} | "
                   f"{credit} | {r.evidence or 'none'} |")
    counts = {s: sum(1 for r in rows if r.status == s) for s in ("green", "yellow", "red", "not due")}
    out += ["", "Counts: " + ", ".join(f"{k} {v}" for k, v in counts.items()) + f"; {len(rows)} TPMs.", ""]
    return "\n".join(out)


def row_y(i: int, n: int) -> float:
    """Top edge (pixels from the top) of table row i of n."""
    return TOP + HEADER_H + i * row_h(n)


def row_h(n: int) -> float:
    return (TABLE_H - TOP - HEADER_H - 60) / max(n, 1)


def draw_table(rows: list[Row], review: str, asof: str, path: str) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.patches import Rectangle

    fig = plt.figure(figsize=(TABLE_W / 100, TABLE_H / 100), dpi=100, facecolor="white")
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, TABLE_W)
    ax.set_ylim(TABLE_H, 0)
    ax.axis("off")
    ax.text(LEFT, 48, f"TPM status at {review}", fontsize=26, fontweight="bold", color=INK, va="center")
    ax.text(LEFT, 90, f"docs/plan/tpm.json, entries on or before {asof}. Red without an entry: no estimate at a reporting review.",
            fontsize=15, color=INK2, va="center")
    cols = [(LEFT, "TPM"), (170, "Key"), (520, "CBE"), (700, "Units"), (1000, "Entry"), (CHIP_X, "Status"), (1400, "Basis"), (1760, "Credit")]
    for x, label in cols:
        ax.text(x, TOP + HEADER_H / 2, label, fontsize=16, fontweight="bold", color=INK, va="center")
    ax.plot([LEFT, TABLE_W - LEFT], [TOP + HEADER_H, TOP + HEADER_H], color=INK, lw=1.2)
    h = row_h(len(rows))
    fs = max(9.0, min(15.0, h * 0.42))
    for i, r in enumerate(rows):
        y0 = row_y(i, len(rows))
        yc = y0 + h / 2
        ax.plot([LEFT, TABLE_W - LEFT], [y0 + h, y0 + h], color=RULE, lw=0.8)
        entry = f"{r.entry_review} {r.entry_date}" if r.entry_review else "none"
        basis = {"entry": "own entry", "no estimate at a reporting review": "no estimate", "not a reporting review": "not due"}[r.reason]
        credit = "n/a" if r.credit is None else ("yes" if r.credit else "no")
        for x, text in ((LEFT, r.tpm_id), (170, r.key), (520, fmt_cbe(r.cbe)), (700, short_units(r.units)),
                        (1000, entry), (1400, basis), (1760, credit)):
            ax.text(x, yc, text, fontsize=fs, color=INK, va="center")
        ax.add_patch(Rectangle((CHIP_X, y0 + h * 0.15), CHIP_W, h * 0.7, facecolor=COLOURS[r.status], edgecolor="none"))
        ax.text(CHIP_X + CHIP_W / 2, yc, r.status, fontsize=fs, color="white" if r.status in ("green", "red") else INK,
                va="center", ha="center", fontweight="bold")
    fig.savefig(path, dpi=100, metadata={"Software": None})
    plt.close(fig)


def draw_trend(tpm: dict, points, review: str, path: str) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig = plt.figure(figsize=(TREND_W / 100, TREND_H / 100), dpi=100, facecolor="white")
    ax = fig.add_axes([0.08, 0.14, 0.88, 0.74])
    xs = list(range(len(points)))
    ys = [p[2] for p in points]
    ax.plot(xs, ys, color=INK2, lw=1.5, zorder=2)
    ax.scatter(xs, ys, s=140, c=[COLOURS[p[3]] for p in points], edgecolors=INK, zorder=3)
    for x, y in zip(xs, ys):
        ax.annotate(f"{y:g}", (x, y), textcoords="offset points", xytext=(0, 12), ha="center", fontsize=13, color=INK)
    planned = tpm.get("planned_value")
    if _is_number(planned):
        ax.axhline(planned, color=COLOURS["green"], ls="--", lw=1.5, label=f"planned value {planned:g}")
        ax.legend(loc="best", fontsize=12, frameon=False)
    ax.set_xticks(xs)
    ax.set_xticklabels([f"{p[0]}\n{p[1]}" for p in points], fontsize=12)
    ax.set_xlim(-0.5, max(len(points) - 0.5, 0.5))
    ax.set_ylabel(short_units(str(tpm.get("units", ""))), fontsize=14)
    ax.grid(axis="y", color=RULE)
    fig.text(0.08, 0.95, f"{tpm['id']} {tpm.get('name', '')} ({tpm['key']})", fontsize=18, fontweight="bold", color=INK, va="center")
    fig.text(0.08, 0.915, f"Trend to {review}: cbe of each history entry, marker colour = recorded status", fontsize=12, color=INK2, va="center")
    fig.savefig(path, dpi=100, metadata={"Software": None})
    plt.close(fig)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="render_tpm.py", description="TPM status table and trend plots (TV-017)")
    ap.add_argument("--review", required=True)
    ap.add_argument("--tpm", default=None)
    ap.add_argument("--out", default=None)
    ap.add_argument("--date", default=None)
    ap.add_argument("--root", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--check", action="store_true")
    try:
        args = ap.parse_args(argv)
    except SystemExit as exc:
        return 2 if exc.code else 0
    if not REVIEW_RE.match(args.review):
        print(f"render_tpm: error: review {args.review!r} is not SRR, PDR, CDR, TRR, TRR-D<n> or SAR", file=sys.stderr)
        return 2
    asof = args.date or dt.date.today().isoformat()
    if not DATE_RE.match(asof):
        print(f"render_tpm: error: --date {asof!r} is not YYYY-MM-DD", file=sys.stderr)
        return 2
    tpm_path = args.tpm or os.path.join(args.root, "docs", "plan", "tpm.json")
    out = args.out or os.path.join(args.root, "docs", "reviews", args.review, "figures")
    try:
        with open(tpm_path, encoding="utf-8") as fh:
            data = json.load(fh)
    except (OSError, ValueError) as exc:
        print(f"render_tpm: error: cannot read {tpm_path}: {exc}", file=sys.stderr)
        return 2
    try:
        rows = build_rows(data, args.review, asof)
    except DataError as exc:
        print(f"render_tpm: DATA ERROR {exc}; nothing written", file=sys.stderr)
        return 1
    table = markdown(rows, args.review, asof)
    if args.check:
        print(table)
        return 0
    if not os.path.isdir(out):
        print(f"render_tpm: error: output directory {out} does not exist", file=sys.stderr)
        return 2
    written = []
    path = os.path.join(out, "tpm-status.png")
    draw_table(rows, args.review, asof, path)
    written.append(path)
    path = os.path.join(out, "tpm-table.md")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(table)
    written.append(path)
    for t in data["tpms"]:
        pts = trend_points(t, asof)
        if t["key"] == REVIEW_TREND_KEY:
            print(f"render_tpm: {t['id']} {t['key']}: trend plotted by tools/review_trend.py, not here", file=sys.stderr)
            continue
        if not pts:
            print(f"render_tpm: {t['id']} {t['key']}: no numeric cbe on or before {asof}, no trend plot", file=sys.stderr)
            continue
        path = os.path.join(out, f"tpm-trend-{t['key']}.png")
        draw_trend(t, pts, args.review, path)
        written.append(path)
    counts = {s: sum(1 for r in rows if r.status == s) for s in ("green", "yellow", "red", "not due")}
    for p in written:
        print(f"render_tpm: wrote {p}")
    print(f"render_tpm: {args.review}: {len(rows)} TPMs; " + ", ".join(f"{k} {v}" for k, v in counts.items()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
