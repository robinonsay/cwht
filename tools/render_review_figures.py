#!/usr/bin/env python3
"""Review-package figures for the cwht gate reviews (charter section 4 items 1 and 2).

Renders the figures a review package and its slide deck show (entrance-criteria
board, success-criteria board, requirements by group, key driving requirements,
hazard matrices, TPM board, ConOps modes and scenarios; a 5x5 risk matrix and a
concept block diagram are also implemented, outside the SRR set, see SRR below)
into docs/reviews/<REVIEW>/figures/. Statuses are read from the
review package docs/reviews/<REVIEW>/package.md; counts are read from the product
files (docs/requirements/sys/requirements.json, docs/safety/hazards.json,
docs/risk/register.json, docs/plan/tpm.json, docs/conops/conops.md). Short labels,
layouts and the concept block diagram are presentation literals of the review's
figure set (FIGURE_SETS below); every literal that restates repository content is
checked against that content before anything is drawn, and a disagreement stops the
run with exit status 1 and nothing written. Re-ratings that a deck review asks the
package to carry are explicit overrides of the figure set, printed on every run;
once the package carries one, the run prints it as redundant so it can be removed.

Only the SRR figure set exists; a later review adds its own set (a new entry of
FIGURE_SETS with its labels and the figure names it uses) with a known-answer test.
This is the controlled successor of the SRR deck figure generator that was kept
outside the repository (deck-review finding F2; package section 2 item H10).

Figures are drawn at their slide pixel size (dpi 100), so a 20 pt label is about
28 px on the 1920 x 1080 slide, in Source Sans Pro from the reveal.js theme of
tools/slides/ when that font is installed (npm install in tools/slides/) and in
the matplotlib default font otherwise, with a notice.

Usage:
    .venv/bin/python tools/render_review_figures.py --review SRR [--root PATH] [--out DIR] [--check] [FIGURE ...]

    --review   review token whose figure set and package are used (SRR)
    --root     repository root (default: the parent of tools/)
    --out      output directory (default: <root>/docs/reviews/<REVIEW>/figures)
    --check    read and cross-check every input, print the counts, write nothing
    FIGURE     figure names to render (default: every figure of the set)

Exit status: 0 figures written (or --check passed), 1 an input disagrees with the
package or the figure set, or an input is missing (nothing is written), 2 usage
error (unknown review token, a review without a figure set, an unknown figure).

The known-answer test is tools/tests/test_render_review_figures.py on the fixture
tools/tests/fixtures/review_figures/. The tool is class B review-evidence tooling
without a TV record yet (SWE-136), so its figures are developer evidence until
the record exists.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable

import matplotlib

matplotlib.use("Agg")
import matplotlib.patheffects as pe  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib import font_manager  # noqa: E402
from matplotlib.patches import FancyBboxPatch, Patch, Rectangle  # noqa: E402

TOOLS = Path(__file__).resolve().parent
REPO_ROOT = TOOLS.parent
REVIEW_TOKEN = re.compile(r"^(SRR|PDR|CDR|TRR|SAR|TRR-D[1-9][0-9]?)$")  # charter section 6
FONT_DIR = TOOLS / "slides" / "node_modules" / "reveal.js" / "dist" / "theme" / "fonts" / "source-sans-pro"
FONT_FILES = ("source-sans-pro-regular.ttf", "source-sans-pro-semibold.ttf", "source-sans-pro-italic.ttf")

SYS_REQUIREMENTS = Path("docs/requirements/sys/requirements.json")
HAZARDS = Path("docs/safety/hazards.json")
RISKS = Path("docs/risk/register.json")
TPMS = Path("docs/plan/tpm.json")
CONOPS = Path("docs/conops/conops.md")

# Ink and chrome (light surface); the status tint only groups, the label text carries the meaning.
SURF = "#ffffff"
INK = "#0b0b0b"
INK2 = "#52514e"
MUTED = "#898781"
GRID = "#e1e0d9"
AXIS = "#c3c2b7"
NAVY = "#0d366b"
ST = {
    "red": ("#fbe1e1", "#d03b3b"),
    "serious": ("#fde6da", "#ec835a"),
    "yellow": ("#fdf0cc", "#d99a00"),
    "green": ("#dcf3dc", "#0ca30c"),
    "grey": ("#f0efec", "#a9a79f"),
}
CAT = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100"]  # categorical slots 1 to 4, fixed order
LANES = ("Not met", "Partially met", "Met")
LANE_COLOR = {"Not met": "red", "Partially met": "yellow", "Met": "green"}


class FigureDataError(Exception):
    """An input is missing or disagrees with the package or the figure set (exit status 1)."""


# ----------------------------------------------------------------------------
# Figure set: the presentation literals of one review
# ----------------------------------------------------------------------------


@dataclass
class FigureSet:
    """Labels, overrides and layouts of one review's figures. Every restated fact is cross-checked."""

    review: str
    figures: tuple[str, ...]
    entrance_section: str = "4. Entrance-criteria checklist"
    success_section: str = "20. Success criteria self-assessment"
    requirements_section: str = "8. Requirements and traceability status"
    group_table_intro: str = "L1 requirements by functional group"
    entrance_labels: dict[str, str] = field(default_factory=dict)
    entrance_overrides: dict[str, tuple[str, str]] = field(default_factory=dict)
    tool_run_rows: frozenset[str] = frozenset()
    entrance_notes: dict[str, str] = field(default_factory=dict)
    success_labels: dict[str, str] = field(default_factory=dict)
    success_overrides: dict[str, tuple[str, str]] = field(default_factory=dict)
    success_footer: tuple[str, ...] = ()
    group_labels: dict[str, str] = field(default_factory=dict)
    kdr_text: tuple[tuple[str, tuple[tuple[str, str], ...]], ...] = ()
    kdr_columns: tuple[tuple[int, ...], ...] = ()
    tpm_rows: tuple[tuple[str, str, str, str], ...] = ()  # (number, name, current-value text, note)
    status_rule_red: frozenset[str] = frozenset()
    tpm_footer: str = ""
    nominal: tuple[tuple[str, str], ...] = ()
    off_nominal: tuple[tuple[str, str], ...] = ()
    concept: Callable[[Any], None] | None = None


@dataclass
class Context:
    root: Path
    spec: FigureSet
    package: "Package"
    log: list[str] = field(default_factory=list)

    def note(self, text: str) -> None:
        self.log.append(text)


# ----------------------------------------------------------------------------
# Package reader (the package is the source of every status)
# ----------------------------------------------------------------------------


class Package:
    def __init__(self, path: Path):
        if not path.is_file():
            raise FigureDataError(f"review package {path} does not exist")
        self.path = path
        self.lines = path.read_text(encoding="utf-8").split("\n")

    def section(self, heading_prefix: str) -> list[str]:
        """Lines of the section whose heading text starts with heading_prefix, up to the next heading of the same or a higher level."""
        out: list[str] = []
        on, level = False, 0
        for line in self.lines:
            match = re.match(r"^(#+) ", line)
            if match:
                if on and len(match.group(1)) <= level:
                    break
                if not on and line[len(match.group(0)):].startswith(heading_prefix):
                    on, level = True, len(match.group(1))
                    continue
            if on:
                out.append(line)
        if not out:
            raise FigureDataError(f"package section '{heading_prefix}' not found in {self.path}")
        return out


def md_rows(lines: list[str]) -> list[list[str]]:
    """Body rows of the first Markdown table in lines, as lists of stripped cells."""
    rows: list[list[str]] = []
    seen_separator = False
    for line in lines:
        if not line.startswith("|"):
            if seen_separator and rows:
                break
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-{3,}:?", c) for c in cells):
            seen_separator = True
            continue
        if seen_separator:
            rows.append(cells)
    return rows


def status_of(text: str) -> str:
    """Normalize a package status cell to Not met, Partially met, Met with lien not allowed or Met."""
    t = text.replace("*", "").strip()
    if t.startswith("Not met"):
        return "Not met"
    if t.startswith("Partially met") or t.startswith("Partial"):
        return "Partially met"
    if t.startswith("Met with lien not allowed"):
        return "Met with lien not allowed"
    if t.startswith("Met"):
        return "Met"
    raise FigureDataError(f"unrecognized status text: {text!r}")


def apply_overrides(kind: str, rows: dict[str, str], overrides: dict[str, tuple[str, str]], log: list[str]) -> dict[str, str]:
    """Figure-set re-ratings the package must carry; each is logged, and logged as redundant once the package carries it."""
    result = dict(rows)
    for cid, (new, why) in overrides.items():
        if cid not in result:
            raise FigureDataError(f"{kind} override {cid} names no row of the package")
        old = result[cid]
        if old == new:
            log.append(f"{kind} {cid}: override redundant (package already reads {new}); remove it")
        else:
            log.append(f"{kind} {cid}: package reads {old}; figure shows {new} ({why})")
            result[cid] = new
    return result


def load_json(ctx: Context, relative: Path) -> Any:
    path = ctx.root / relative
    if not path.is_file():
        raise FigureDataError(f"{relative} does not exist")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise FigureDataError(f"{relative} is not valid JSON: {exc}") from exc


def lanes_for(kind: str, status: dict[str, str]) -> dict[str, list[str]]:
    lanes: dict[str, list[str]] = {lane: [] for lane in LANES}
    for cid, value in status.items():
        if value not in lanes:
            raise FigureDataError(f"{kind} {cid}: status '{value}' has no lane; the figure set must override it to one of {', '.join(LANES)}")
        lanes[value].append(cid)
    return lanes


# ----------------------------------------------------------------------------
# Data (pure: read, cross-check, return what is drawn)
# ----------------------------------------------------------------------------


def entrance_data(ctx: Context) -> dict[str, list[tuple[str, str, str]]]:
    """Entrance lanes: (id with a dagger for tool-run rows, label, gate) per status, in package order."""
    spec = ctx.spec
    rows = md_rows(ctx.package.section(spec.entrance_section))
    status, gate = {}, {}
    for row in rows:
        if len(row) < 6:
            raise FigureDataError(f"entrance row {row[:1]} has {len(row)} cells; the table needs # | criterion | gate | evidence | commit | status")
        status[row[0]] = status_of(row[5])
        gate[row[0]] = "Hard" if row[2].startswith("Hard") else ("Soft" if row[2].startswith("Soft") else row[2])
    if set(status) != set(spec.entrance_labels):
        raise FigureDataError(f"entrance rows and figure-set labels differ: {sorted(set(status) ^ set(spec.entrance_labels))}")
    status = apply_overrides("entrance row", status, spec.entrance_overrides, ctx.log)
    lanes = lanes_for("entrance row", status)
    return {
        lane: [(cid + ("†" if cid in spec.tool_run_rows else ""), spec.entrance_labels[cid], gate[cid]) for cid in ids]
        for lane, ids in lanes.items()
    }


def success_data(ctx: Context) -> dict[str, list[tuple[str, str]]]:
    spec = ctx.spec
    rows = md_rows(ctx.package.section(spec.success_section))
    status = {row[0]: status_of(row[3]) for row in rows}
    if set(status) != set(spec.success_labels):
        raise FigureDataError(f"success criteria and figure-set labels differ: {sorted(set(status) ^ set(spec.success_labels))}")
    status = apply_overrides("success criterion", status, spec.success_overrides, ctx.log)
    return {lane: [(cid, spec.success_labels[cid]) for cid in ids] for lane, ids in lanes_for("success criterion", status).items()}


def sys_requirements(ctx: Context) -> list[dict[str, Any]]:
    data = load_json(ctx, SYS_REQUIREMENTS)
    reqs = data.get("requirements") if isinstance(data, dict) else None
    if not isinstance(reqs, list):
        raise FigureDataError(f"{SYS_REQUIREMENTS} has no requirements list")
    return [r for r in reqs if isinstance(r, dict)]


def is_retired(req: dict[str, Any]) -> bool:
    return "retired" in (req.get("tags") or [])


def requirements_data(ctx: Context) -> dict[str, Any]:
    """[(label, total, retired, T, A, I, D, KDR, TBR)] per package group; each package row must equal the file."""
    reqs = sys_requirements(ctx)
    by_id = {r.get("id"): r for r in reqs}
    section = ctx.package.section(ctx.spec.requirements_section)
    start = next((i for i, line in enumerate(section) if line.startswith(ctx.spec.group_table_intro)), None)
    if start is None:
        raise FigureDataError(f"package section '{ctx.spec.requirements_section}' has no line starting '{ctx.spec.group_table_intro}'")
    groups, seen = [], set()
    for row in md_rows(section[start:]):
        match = re.match(r"^(.*?) \(([\d, ]+)\)$", row[0])
        if not match:
            continue  # the total row
        name, ids = match.group(1), [f"REQ-SYS-{n.strip()}" for n in match.group(2).split(",")]
        label = next((v for k, v in ctx.spec.group_labels.items() if name.startswith(k)), None)
        if label is None:
            raise FigureDataError(f"package group '{name}' has no figure-set label")
        missing = [i for i in ids if i not in by_id]
        if missing:
            raise FigureDataError(f"package group '{name}' names {', '.join(missing)}, absent from {SYS_REQUIREMENTS}")
        rs = [by_id[i] for i in ids]
        seen.update(ids)
        live = [x for x in rs if not is_retired(x)]
        methods = Counter(x.get("verification_method") for x in live)
        group = (label, len(rs), len(rs) - len(live), methods["Test"], methods["Analysis"], methods["Inspection"],
                 methods["Demonstration"], sum(1 for x in rs if x.get("priority") == "KDR"), sum(1 for x in rs if x.get("tbr")))
        try:
            package_row = (int(row[1]), int(row[3]), *[int(v) for v in row[7].split("/")], int(row[4]), int(row[6]))
        except (IndexError, ValueError) as exc:
            raise FigureDataError(f"package group '{name}': unreadable counts {row[1:8]}") from exc
        if package_row != group[1:]:
            raise FigureDataError(f"package group '{label}': package {package_row} differs from {SYS_REQUIREMENTS} {group[1:]} (total, retired, T, A, I, D, KDR, TBR)")
        groups.append(group)
    if seen != set(by_id):
        raise FigureDataError(f"requirements in no package group or in a group but not in the file: {sorted(set(by_id) ^ seen)}")
    live = [r for r in reqs if not is_retired(r)]
    return {
        "groups": groups,
        "total": len(reqs),
        "live": len(live),
        "methods": Counter(r.get("verification_method") for r in live),
        "tbr": sum(1 for r in reqs if r.get("tbr")),
    }


def kdr_data(ctx: Context) -> dict[str, Any]:
    reqs = {r.get("id"): r for r in sys_requirements(ctx)}
    kdr_ids = {i for i, r in reqs.items() if r.get("priority") == "KDR"}
    shown = {f"REQ-SYS-{num}" for _, items in ctx.spec.kdr_text for num, _ in items}
    if shown != kdr_ids:
        raise FigureDataError(f"KDR figure-set entries and KDR requirements differ: {sorted(shown ^ kdr_ids)}")
    groups = [
        (name, [(num, text, reqs[f"REQ-SYS-{num}"].get("verification_method", ""), bool(reqs[f"REQ-SYS-{num}"].get("tbr"))) for num, text in items])
        for name, items in ctx.spec.kdr_text
    ]
    placed = sorted(i for column in ctx.spec.kdr_columns for i in column)
    if placed != list(range(len(groups))):
        raise FigureDataError(f"kdr_columns place groups {placed}; every one of the {len(groups)} groups goes in exactly one column")
    return {"groups": groups, "count": len(kdr_ids)}


SEVERITIES = ("Catastrophic", "Critical", "Marginal", "Negligible")
LIKELIHOODS = ("A", "B", "C", "D", "E")
LEVEL_COLOR = {"High": "red", "Serious": "serious", "Medium": "yellow", "Low": "green"}


def hazards_data(ctx: Context) -> dict[str, Any]:
    data = load_json(ctx, HAZARDS)
    try:
        matrix = data["scales"]["risk_matrix"]
        hazards = {}
        for hz in data["hazards"]:
            residual = hz["residual_risk"]
            hazards[hz["id"][3:]] = (hz["severity"], hz["likelihood"], hz["initial_risk"], residual["severity"], residual["likelihood"], residual["level"])
    except (KeyError, TypeError) as exc:
        raise FigureDataError(f"{HAZARDS}: missing field {exc}") from exc
    for severity in SEVERITIES:
        for likelihood in LIKELIHOODS:
            level = matrix.get(severity, {}).get(likelihood)
            if level not in LEVEL_COLOR:
                raise FigureDataError(f"{HAZARDS} scales.risk_matrix[{severity}][{likelihood}] is '{level}', not one of {', '.join(LEVEL_COLOR)}")
    for key, (s0, l0, _, s1, l1, _) in hazards.items():
        if s0 not in SEVERITIES or s1 not in SEVERITIES or l0 not in LIKELIHOODS or l1 not in LIKELIHOODS:
            raise FigureDataError(f"HZ-{key}: severity or likelihood outside the matrix")
    cells: dict[str, dict[tuple[str, str], list[str]]] = {"initial": defaultdict(list), "residual": defaultdict(list)}
    for key, value in hazards.items():
        cells["initial"][(value[0], value[1])].append(key)
        cells["residual"][(value[3], value[4])].append(key)
    return {"matrix": matrix, "hazards": hazards, "cells": cells, "version": data.get("version", "")}


def risk_band(likelihood: int, consequence: int, safety: int) -> str:
    """06 section 5 bands with the safety override: a safety consequence of 5 at likelihood 2 or more is Red."""
    if safety == 5 and likelihood >= 2:
        return "Red"
    return cell_band(likelihood, consequence)


def cell_band(likelihood: int, consequence: int) -> str:
    score = likelihood * consequence
    return "Red" if score >= 12 else ("Yellow" if score >= 5 else "Green")


def risk_data(ctx: Context) -> dict[str, Any]:
    data = load_json(ctx, RISKS)
    try:
        active = [r for r in data["risks"] if r["status"] not in ("Closed", "Retired")]
        cells: dict[tuple[int, int], list[str]] = defaultdict(list)
        overridden: dict[tuple[int, int], list[str]] = defaultdict(list)
        bands: Counter[str] = Counter()
        for risk in active:
            consequence = max(risk["consequence"].values())
            likelihood = risk["likelihood"]
            band = risk_band(likelihood, consequence, risk["consequence"].get("safety", 0))
            bands[band] += 1
            cells[(likelihood, consequence)].append(risk["id"][4:])
            if band != cell_band(likelihood, consequence):
                overridden[(likelihood, consequence)].append(risk["id"])
    except (KeyError, TypeError, ValueError) as exc:
        raise FigureDataError(f"{RISKS}: unreadable risk entry ({exc})") from exc
    return {"active": len(active), "cells": cells, "overridden": overridden, "bands": bands}


def tpm_data(ctx: Context) -> list[tuple[str, str, str, str, str]]:
    """(number, name, value text, zone, note): zone from the review's history entry, else the status rule, else Not reported."""
    data = load_json(ctx, TPMS)
    try:
        by_number = {t["id"][4:]: t for t in data["tpms"]}
    except (KeyError, TypeError) as exc:
        raise FigureDataError(f"{TPMS}: unreadable tpms list ({exc})") from exc
    listed = {row[0] for row in ctx.spec.tpm_rows}
    if set(by_number) != listed:
        raise FigureDataError(f"TPM figure-set rows and {TPMS} tpms differ: {sorted(set(by_number) ^ listed)}")
    zones = {"red": "Red", "yellow": "Yellow", "green": "Green"}
    rows = []
    for number, name, current, note in ctx.spec.tpm_rows:
        history = [e for e in by_number[number].get("history", []) if e.get("review") == ctx.spec.review]
        if history:
            status = history[-1].get("status")
            if status not in zones:
                raise FigureDataError(f"TPM-{number}: {ctx.spec.review} history status '{status}' is not red, yellow or green")
            zone = zones[status]
            cbe = history[-1].get("cbe")
            if cbe is not None and str(cbe).rstrip("0").rstrip(".") not in current.replace(",", ""):
                raise FigureDataError(f"TPM-{number}: figure text '{current}' does not carry the {ctx.spec.review} cbe {cbe} of {TPMS}")
        elif number in ctx.spec.status_rule_red:
            zone = "Red"
        else:
            zone = "Not reported"
        rows.append((number, name, current, zone, note))
    return rows


def conops_data(ctx: Context) -> dict[str, Any]:
    path = ctx.root / CONOPS
    if not path.is_file():
        raise FigureDataError(f"{CONOPS} does not exist")
    text = path.read_text(encoding="utf-8")
    try:
        nominal = text[text.index("### 6.1 Nominal scenarios"):text.index("### 6.2 Off-nominal scenarios")]
    except ValueError as exc:
        raise FigureDataError(f"{CONOPS} lacks the headings '### 6.1 Nominal scenarios' and '### 6.2 Off-nominal scenarios'") from exc
    off = text[text.index("### 6.2 Off-nominal scenarios"):]
    end = re.search(r"\n## ", off)
    off = off[:end.start()] if end else off
    ids_nominal = re.findall(r"^### OPS-(\d{3}) ", nominal, re.M)
    ids_off = re.findall(r"^### OPS-(\d{3}) ", off, re.M)
    if ids_nominal != [n for n, _ in ctx.spec.nominal]:
        raise FigureDataError(f"nominal scenarios of {CONOPS} {ids_nominal} differ from the figure set {[n for n, _ in ctx.spec.nominal]}")
    if ids_off != [n for n, _ in ctx.spec.off_nominal]:
        raise FigureDataError(f"off-nominal scenarios of {CONOPS} {ids_off} differ from the figure set {[n for n, _ in ctx.spec.off_nominal]}")
    return {"nominal": list(ctx.spec.nominal), "off_nominal": list(ctx.spec.off_nominal)}


def concept_data(ctx: Context) -> dict[str, Any]:
    if ctx.spec.concept is None:
        raise FigureDataError(f"the {ctx.spec.review} figure set has no concept drawing")
    return {}


# ----------------------------------------------------------------------------
# Drawing helpers
# ----------------------------------------------------------------------------


def use_fonts(log: list[str]) -> None:
    missing = [f for f in FONT_FILES if not (FONT_DIR / f).is_file()]
    if missing:
        log.append(f"font Source Sans Pro not found under {FONT_DIR} (npm install in tools/slides/); figures use the matplotlib default font")
        plt.rcParams["font.family"] = "DejaVu Sans"
    else:
        for name in FONT_FILES:
            font_manager.fontManager.addfont(str(FONT_DIR / name))
        plt.rcParams["font.family"] = "Source Sans Pro"
    plt.rcParams["svg.fonttype"] = "none"


def canvas(w_px: int, h_px: int):
    fig = plt.figure(figsize=(w_px / 100, h_px / 100), dpi=100, facecolor=SURF)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, w_px)
    ax.set_ylim(h_px, 0)
    ax.axis("off")
    return fig, ax


def box(ax, x, y, w, h, fill, edge, lw=2.0, r=10, z=2):
    patch = FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}", facecolor=fill, edgecolor=edge, linewidth=lw, zorder=z)
    ax.add_patch(patch)
    return patch


def wrap_px(fig, text: str, fontsize: float, max_px: float) -> list[str]:
    """Greedy word wrap by rendered width in pixels (dpi 100)."""
    renderer = fig.canvas.get_renderer()
    lines, current = [], ""
    for word in text.split(" "):
        trial = (current + " " + word).strip()
        probe = fig.text(0, 0, trial, fontsize=fontsize)
        width = probe.get_window_extent(renderer).width
        probe.remove()
        if width <= max_px or not current:
            current = trial
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def save(fig, out: Path, name: str) -> Path:
    path = out / name
    fig.savefig(path, dpi=100, facecolor=SURF)
    plt.close(fig)
    return path


def arrow(ax, p, q, color=INK2, lw=2.0, style="-|>", ls="-", z=1, ms=16):
    ax.annotate("", xy=q, xytext=p, zorder=z, arrowprops=dict(arrowstyle=style, color=color, lw=lw, linestyle=ls, shrinkA=0, shrinkB=0, mutation_scale=ms))


def poly(ax, pts, color=INK2, lw=2.0, ls="-", z=1, head=True, ms=16):
    xs, ys = zip(*pts)
    if len(pts) > 2:
        ax.plot(xs[:-1], ys[:-1], color=color, lw=lw, ls=ls, zorder=z, solid_capstyle="butt")
    if head:
        arrow(ax, pts[-2], pts[-1], color=color, lw=lw, ls=ls, z=z, ms=ms)
    else:
        ax.plot(xs[-2:], ys[-2:], color=color, lw=lw, ls=ls, zorder=z)


def lbl(ax, x, y, s, fs=16, ha="center", color=INK2):
    ax.text(x, y, s, fontsize=fs, color=color, ha=ha, va="center", zorder=5, bbox=dict(boxstyle="round,pad=0.18", facecolor="#ffffff", edgecolor="none"))


# ----------------------------------------------------------------------------
# Renderers (draw what the data functions returned)
# ----------------------------------------------------------------------------


def draw_entrance(ctx: Context, lanes: dict[str, list[tuple[str, str, str]]], out: Path) -> Path:
    w, h, row_h, fs, id_w = 1760, 850, 43, 20, 70
    fig, ax = canvas(w, h)
    gap = 24
    lane_w = (w - gap * (len(lanes) - 1)) / len(lanes)
    for i, (title, items) in enumerate(lanes.items()):
        x = i * (lane_w + gap)
        fill, edge = ST[LANE_COLOR[title]]
        box(ax, x + 2, 2, lane_w - 4, h - 4, "#ffffff", AXIS, lw=1.5, r=12, z=1)
        box(ax, x + 2, 2, lane_w - 4, 64, fill, edge, lw=2, r=12, z=2)
        ax.text(x + 22, 34, title, fontsize=24, fontweight="semibold", color=INK, va="center", zorder=3)
        ax.text(x + lane_w - 22, 34, f"{len(items)}", fontsize=26, fontweight="semibold", color=INK, va="center", ha="right", zorder=3)
        y = 66 + 12 + row_h / 2
        for cid, label, gate in items:
            ax.text(x + 20, y, cid, fontsize=fs, fontweight="semibold", color=INK, va="center", zorder=3)
            ax.text(x + 20 + id_w, y, label, fontsize=fs, color=INK, va="center", zorder=3)
            ax.text(x + lane_w - 20, y, gate, fontsize=fs - 3, color=INK2, va="center", ha="right", zorder=3, fontweight="semibold" if gate == "Hard" else "normal")
            y += row_h
        if title in ctx.spec.entrance_notes:
            ax.text(x + 20, h - 22, ctx.spec.entrance_notes[title], fontsize=fs - 3, color=INK2, va="bottom", zorder=3, linespacing=1.3)
    return save(fig, out, "entrance-checklist.png")


def draw_success(ctx: Context, lanes: dict[str, list[tuple[str, str]]], out: Path) -> Path:
    w, h = 1760, 790
    fig, ax = canvas(w, h)
    gap = 24
    lane_w = (w - 2 * gap) / 3
    x = 0.0
    for title, items in lanes.items():
        fill, edge = ST[LANE_COLOR[title]]
        box(ax, x + 2, 2, lane_w - 4, h - 86, "#ffffff", AXIS, lw=1.5, r=12, z=1)
        box(ax, x + 2, 2, lane_w - 4, 64, fill, edge, lw=2, r=12, z=2)
        ax.text(x + 20, 34, title, fontsize=24, fontweight="semibold", color=INK, va="center", zorder=3)
        ax.text(x + lane_w - 20, 34, f"{len(items)}", fontsize=26, fontweight="semibold", color=INK, va="center", ha="right", zorder=3)
        y = 66 + 34
        for cid, label in items:
            lines = wrap_px(fig, label, 19, lane_w - 108 - 24)
            ax.text(x + 20, y, cid, fontsize=19, fontweight="semibold", color=INK, va="center", zorder=3)
            for j, line in enumerate(lines):
                ax.text(x + 108, y + j * 28, line, fontsize=19, color=INK, va="center", zorder=3)
            y += 28 * len(lines) + 18
        x += lane_w + gap
    for k, line in enumerate(ctx.spec.success_footer):
        ax.text(0, h - 52 + 32 * k, line, fontsize=18, color=INK2, ha="left", va="center")
    return save(fig, out, "success-criteria.png")


def draw_requirements(ctx: Context, data: dict[str, Any], out: Path) -> Path:
    groups, methods = data["groups"], data["methods"]
    retired = data["total"] - data["live"]
    fig = plt.figure(figsize=(17.6, 8.3), dpi=100, facecolor=SURF)
    ax = fig.add_axes([0.25, 0.13, 0.48, 0.79])
    ax2 = fig.add_axes([0.765, 0.13, 0.215, 0.79], sharey=ax)
    ys = list(range(len(groups)))[::-1]
    names = ["Test", "Analysis", "Inspection", "Demonstration"]
    widest = max((g[1] for g in groups), default=1)
    most_tbr = max((g[8] for g in groups), default=1)
    for yy, g in zip(ys, groups):
        left = 0
        for value, color in zip(list(g[3:7]) + [g[2]], CAT + ["#c3c2b7"]):
            if value:
                ax.barh(yy, value, left=left, height=0.62, color=color, edgecolor=SURF, linewidth=2, zorder=3)
                ax.text(left + value / 2, yy, str(value), ha="center", va="center", fontsize=17 if value >= 2 else 16, color="#ffffff" if color in (CAT[0], CAT[1]) else INK, zorder=4)
                left += value
        ax.text(left + 0.5, yy, f"{g[1]}", va="center", fontsize=20, fontweight="semibold", color=INK)
        ax2.barh(yy, g[8], height=0.62, color="#6da7ec", edgecolor=SURF, linewidth=2, zorder=3)
        ax2.text(g[8] + 0.4, yy, f"{g[8]}", va="center", fontsize=20, color=INK)
    ax.set_yticks(ys)
    ax.set_yticklabels([g[0] for g in groups], fontsize=20, color=INK)
    ax.set_xlim(0, max(29, widest + 3))
    ax2.set_xlim(0, max(20, most_tbr + 3))
    for a in (ax, ax2):
        a.tick_params(axis="x", labelsize=17, colors=MUTED)
        a.grid(axis="x", color=GRID, linewidth=1, zorder=0)
        for side in ("top", "right", "left"):
            a.spines[side].set_visible(False)
        a.spines["bottom"].set_color(AXIS)
        a.tick_params(axis="y", length=0)
    plt.setp(ax2.get_yticklabels(), visible=False)
    ax.set_title(f"L1 requirements by verification method ({data['live']} non-retired, {retired} retired)", fontsize=21, color=INK, loc="left", pad=14, fontweight="semibold")
    ax2.set_title(f"With an open TBR ({data['tbr']})", fontsize=21, color=INK, loc="left", pad=14, fontweight="semibold")
    handles = [Patch(color=c, label=f"{n} ({methods[n]})") for c, n in zip(CAT, names)]
    handles.append(Patch(color="#c3c2b7", label=f"Retired ({retired})"))
    fig.legend(handles=handles, loc="lower left", bbox_to_anchor=(0.245, 0.0), ncol=5, frameon=False, fontsize=18, handlelength=1.2, columnspacing=1.6)
    return save(fig, out, "requirements-by-group.png")


def draw_kdr(ctx: Context, data: dict[str, Any], out: Path) -> Path:
    groups = data["groups"]
    w, h = 1760, 720
    fig, ax = canvas(w, h)
    column_w, gap = 425, 20
    entry_h, head_h = 84, 54
    for ci, members in enumerate(ctx.spec.kdr_columns):
        x = ci * (column_w + gap)
        y = 4
        for gi in members:
            name, items = groups[gi]
            group_h = head_h + entry_h * len(items) + 10
            box(ax, x + 2, y, column_w - 4, group_h, "#ffffff", AXIS, lw=1.5, r=12, z=1)
            box(ax, x + 2, y, column_w - 4, head_h, "#e8f0fb", "#86b6ef", lw=1.5, r=12, z=2)
            ax.text(x + 18, y + head_h / 2, name, fontsize=20, fontweight="semibold", color=NAVY, va="center", zorder=3)
            yy = y + head_h + 8
            for num, text, method, tbr in items:
                ax.text(x + 18, yy + 22, f"REQ-SYS-{num}", fontsize=20, fontweight="semibold", color=INK, va="center", zorder=3)
                ax.text(x + column_w - 18, yy + 22, method + ("  TBR" if tbr else ""), fontsize=18, color=INK2, va="center", ha="right", zorder=3)
                ax.text(x + 18, yy + 56, text, fontsize=18.5, color=INK, va="center", zorder=3)
                yy += entry_h
            y += group_h + 16
    ax.text(w - 4, h - 22, f"{data['count']} KDRs; right tag = verification method, TBR = value open until PDR (package section 8)", fontsize=18, color=INK2, ha="right", va="center")
    return save(fig, out, "kdr-map.png")


def draw_hazards(ctx: Context, data: dict[str, Any], out: Path) -> Path:
    matrix = data["matrix"]
    w, hh = 1030, 740
    fig, ax = canvas(w, hh)
    cell_w, cell_h = 79, 126
    left0, top = 176, 110
    for pi, (title, key) in enumerate((("Initial (uncontrolled)", "initial"), ("Residual (controls allocated)", "residual"))):
        x0 = left0 + pi * (5 * cell_w + 36)
        ax.text(x0, 36, title, fontsize=22, fontweight="semibold", color=INK, va="center")
        for li, likelihood in enumerate(LIKELIHOODS):
            ax.text(x0 + li * cell_w + cell_w / 2, top - 22, likelihood, fontsize=20, color=INK2, ha="center", va="center")
        cells = data["cells"][key]
        for si, severity in enumerate(SEVERITIES):
            if pi == 0:
                ax.text(left0 - 14, top + si * cell_h + cell_h / 2, severity, fontsize=20, color=INK2, ha="right", va="center")
            for li, likelihood in enumerate(LIKELIHOODS):
                level = matrix[severity][likelihood]
                fill, _ = ST[LEVEL_COLOR[level]]
                x, y = x0 + li * cell_w, top + si * cell_h
                ax.add_patch(Rectangle((x, y), cell_w, cell_h, facecolor=fill, edgecolor="#ffffff", linewidth=3))
                ids = sorted(cells.get((severity, likelihood), []))
                for j, k in enumerate(ids):
                    ax.text(x + cell_w / 2, y + 22 + j * 25, k, fontsize=19, fontweight="semibold", color=INK, ha="center", va="center")
                if len(ids) < 4:
                    ax.text(x + cell_w / 2, y + cell_h - 16, level, fontsize=13.5, color=INK2, ha="center", va="center")
        ax.text(x0 + 2.5 * cell_w, top + 4 * cell_h + 26, "Likelihood A (frequent) to E (improbable)", fontsize=16, color=INK2, ha="center", va="center")
    lx, ly = left0, top + 4 * cell_h + 68
    for level in ("High", "Serious", "Medium", "Low"):
        fill, edge = ST[LEVEL_COLOR[level]]
        ax.add_patch(Rectangle((lx, ly - 14), 34, 28, facecolor=fill, edgecolor=edge, linewidth=1.5))
        ax.text(lx + 44, ly, level, fontsize=19, color=INK, va="center")
        lx += 150
    ax.text(lx, ly, "Numbers: HZ-0nn", fontsize=18, color=INK2, va="center")
    return save(fig, out, "hazard-matrix.png")


def draw_risk(ctx: Context, data: dict[str, Any], out: Path) -> Path:
    cells, overridden, bands = data["cells"], data["overridden"], data["bands"]
    w, h = 1760, 830
    fig, ax = canvas(w, h)
    x0, y0, cw, ch = 250, 96, 296, 136
    consequence_names = ["1 Negligible", "2 Minor", "3 Moderate", "4 Major", "5 Critical"]
    likelihood_names = {5: "5 Near certain", 4: "4 Likely", 3: "3 Possible", 2: "2 Unlikely", 1: "1 Very unlikely"}
    for ci, name in enumerate(consequence_names):
        ax.text(x0 + ci * cw + cw / 2, y0 - 24, name, fontsize=20, color=INK2, ha="center", va="center")
    ax.text(x0 + 2.5 * cw, 18, "Consequence (maximum dimension) across, likelihood down", fontsize=18, color=INK2, ha="center", va="center")
    band_color = {"Red": "red", "Yellow": "yellow", "Green": "green"}
    for row, likelihood in enumerate([5, 4, 3, 2, 1]):
        ax.text(x0 - 16, y0 + row * ch + ch / 2, likelihood_names[likelihood], fontsize=20, color=INK2, ha="right", va="center")
        for ci, consequence in enumerate([1, 2, 3, 4, 5]):
            band = cell_band(likelihood, consequence)
            fill, _ = ST[band_color[band]]
            x, y = x0 + ci * cw, y0 + row * ch
            ax.add_patch(Rectangle((x, y), cw, ch, facecolor=fill, edgecolor="#ffffff", linewidth=4))
            ids = sorted(cells.get((likelihood, consequence), []))
            ax.text(x + 10, y + 18, f"{band[0]} {likelihood * consequence}", fontsize=16, color=INK2, va="center")
            if ids:
                ax.text(x + cw - 10, y + 18, f"{len(ids)}", fontsize=20, fontweight="semibold", color=INK, va="center", ha="right")
                for j in range(0, len(ids), 6):
                    ax.text(x + 10, y + 46 + (j // 6) * 25, "  ".join(ids[j:j + 6]), fontsize=17, color=INK, va="center")
            if overridden.get((likelihood, consequence)):
                ax.text(x + 10, y + ch - 20, "Red by safety override", fontsize=16, color="#9b1c1c", fontweight="semibold", va="center")
    lx, ly = x0, y0 + 5 * ch + 36
    for band in ("Red", "Yellow", "Green"):
        fill, edge = ST[band_color[band]]
        ax.add_patch(Rectangle((lx, ly - 14), 34, 28, facecolor=fill, edgecolor=edge, linewidth=1.5))
        ax.text(lx + 44, ly, f"{band} {bands[band]}", fontsize=20, color=INK, va="center")
        lx += 190
    ax.text(lx + 10, ly, f"{data['active']} active risks; cell numbers are RSK-0nn; corner = band and score L x C", fontsize=18, color=INK2, va="center")
    return save(fig, out, "risk-matrix.png")


def draw_tpm(ctx: Context, rows: list[tuple[str, str, str, str, str]], out: Path) -> Path:
    w, h = 1760, 780
    fig, ax = canvas(w, h)
    ncol = 5
    nrow = max(4, -(-len(rows) // ncol))  # the 20-tile SRR grid is the minimum, so a short set keeps the tile height
    gap = 18
    tile_w = (w - gap * (ncol - 1)) / ncol
    tile_h = (h - 60 - gap * (nrow - 1)) / nrow
    zone_color = {"Red": "red", "Yellow": "yellow", "Green": "green", "Not reported": "grey"}
    for i, (num, name, current, zone, note) in enumerate(rows):
        r, c = divmod(i, ncol)
        x, y = c * (tile_w + gap), r * (tile_h + gap)
        fill, edge = ST[zone_color[zone]]
        box(ax, x + 2, y + 2, tile_w - 4, tile_h - 4, fill, edge, lw=2, r=12)
        ax.text(x + 18, y + 32, f"TPM-{num}", fontsize=19, fontweight="semibold", color=INK, va="center")
        reported = zone != "Not reported"
        ax.text(x + tile_w - 16, y + 32, zone + (f" ({note})" if note else ""), fontsize=17, fontweight="semibold" if reported else "normal", color=INK if reported else INK2, va="center", ha="right")
        ax.text(x + 18, y + 80, name, fontsize=22, color=INK, va="center")
        ax.text(x + 18, y + 124, current, fontsize=19, color=INK if reported else INK2, va="center")
    if ctx.spec.tpm_footer:
        ax.text(0, h - 22, ctx.spec.tpm_footer, fontsize=18, color=INK2, va="center")
    return save(fig, out, "tpm-status.png")


def draw_conops(ctx: Context, data: dict[str, Any], out: Path) -> Path:
    nominal, off_nominal = data["nominal"], data["off_nominal"]
    w, h = 1760, 830
    fig, ax = canvas(w, h)
    mode_fill, mode_edge = "#e8f0fb", "#3b5b8c"
    fault_fill, fault_edge = ST["red"]

    def mode(x, y, bw, bh, name, sub=None, fill=mode_fill, edge=mode_edge):
        box(ax, x, y, bw, bh, fill, edge, lw=2, r=10, z=3)
        if sub:
            ax.text(x + bw / 2, y + 30, name, fontsize=21, fontweight="semibold", color=INK, ha="center", va="center", zorder=4)
            ax.text(x + bw / 2, y + bh - 28, sub, fontsize=16, color=INK2, ha="center", va="center", zorder=4)
        else:
            ax.text(x + bw / 2, y + bh / 2, name, fontsize=21, fontweight="semibold", color=INK, ha="center", va="center", zorder=4)

    # Modes and simplified transitions of ConOps section 3.4 (Table 3.4-2 has all of them).
    box(ax, 330, 30, 700, 590, "#fafaf5", "#9a988f", lw=1.5, r=14, z=1)
    ax.text(350, 58, "Radio on (switch on)", fontsize=19, fontweight="semibold", color=INK2, va="center", zorder=2)
    mode(40, 70, 210, 70, "Off")
    mode(40, 300, 210, 90, "Charging", "switch off, USB in")
    mode(40, 690, 250, 80, "Firmware-update")
    mode(560, 90, 220, 70, "Self-test")
    mode(495, 260, 350, 110, "Receive", "flags and inhibits gate Arm")
    mode(345, 500, 215, 70, "Transmit-keyed")
    mode(580, 500, 180, 70, "Tune")
    mode(790, 500, 200, 70, "Bench-test")
    mode(540, 700, 280, 80, "Fault-safe (latched)", fill=fault_fill, edge=fault_edge)
    poly(ax, [(250, 105), (560, 118)])
    lbl(ax, 405, 96, "T01 switch on")
    poly(ax, [(115, 140), (115, 300)])
    lbl(ax, 115, 220, "T02 USB in")
    poly(ax, [(185, 300), (185, 140)])
    lbl(ax, 205, 175, "T04", ha="left")
    poly(ax, [(250, 330), (300, 330), (300, 145), (560, 145)])
    lbl(ax, 300, 250, "T05")
    poly(ax, [(40, 118), (18, 118), (18, 730), (40, 730)])
    lbl(ax, 18, 560, "T03", fs=15)
    poly(ax, [(670, 160), (670, 260)])
    lbl(ax, 670, 210, "T08 pass")
    poly(ax, [(560, 370), (470, 500)])
    poly(ax, [(500, 500), (590, 370)])
    lbl(ax, 505, 440, "T10 / T11", ha="right")
    poly(ax, [(650, 370), (650, 500)])
    poly(ax, [(700, 500), (700, 370)])
    lbl(ax, 712, 440, "T12 / T13", ha="left")
    poly(ax, [(770, 370), (860, 500)])
    poly(ax, [(900, 500), (810, 370)])
    lbl(ax, 900, 425, "T14 / T15")
    poly(ax, [(640, 620), (640, 700)])
    lbl(ax, 640, 660, "T09, T17 fault")
    poly(ax, [(820, 740), (1060, 740), (1060, 118), (780, 118)])
    lbl(ax, 1060, 400, "T24 ack")
    ax.text(40, 800, "Entered by T03, or by T07 and T16 (host command)", fontsize=15, color=INK2, ha="left", va="center")
    ax.text(350, 598, "Simplified; all transitions T01 to T25 are in ConOps Table 3.4-2", fontsize=15, color=INK2, va="center")
    x1 = 1120
    ax.text(x1, 40, f"Nominal scenarios ({len(nominal)})", fontsize=21, fontweight="semibold", color=INK, va="center")
    for i, (n, t) in enumerate(nominal):
        y = 80 + i * 32
        ax.text(x1, y, f"OPS-{n}", fontsize=17, fontweight="semibold", color=NAVY, va="center")
        ax.text(x1 + 100, y, t, fontsize=17, color=INK, va="center")
    y0 = 80 + len(nominal) * 32 + 26
    ax.text(x1, y0, f"Off-nominal scenarios ({len(off_nominal)})", fontsize=21, fontweight="semibold", color=INK, va="center")
    for i, (n, t) in enumerate(off_nominal):
        y = y0 + 40 + i * 32
        ax.text(x1, y, f"OPS-{n}", fontsize=17, fontweight="semibold", color="#9b1c1c", va="center")
        ax.text(x1 + 100, y, t, fontsize=17, color=INK, va="center")
    return save(fig, out, "conops-modes-scenarios.png")


def draw_concept(ctx: Context, data: dict[str, Any], out: Path) -> Path:
    fig, ax = canvas(1760, 860)
    ctx.spec.concept(ax)
    return save(fig, out, "concept-block-diagram.png")


def srr_concept(ax) -> None:
    """Concept block diagram of docs/design/concept.md section 5 (blocks B01 to B22), a presentation literal."""
    def group(x, y, bw, bh, title):
        box(ax, x, y, bw, bh, "#fafaf5", "#9a988f", lw=1.5, r=14, z=1)
        ax.text(x + 14, y + 20, title, fontsize=17, fontweight="semibold", color=INK2, va="center", zorder=2)

    def blk(x, y, bw, bh, text, bid, fs=15.5, fill="#ffffff", edge="#3b5b8c"):
        box(ax, x, y, bw, bh, fill, edge, lw=1.8, r=8, z=3)
        ax.text(x + bw / 2, y + bh / 2 - 9, text, fontsize=fs, color=INK, ha="center", va="center", zorder=4, linespacing=1.05)
        ax.text(x + bw / 2, y + bh - 13, bid, fontsize=13.5, color=INK2, ha="center", va="center", zorder=4, fontweight="semibold")

    sig, ctl, pwr = "#3a3936", "#2a78d6", "#eb6834"
    ring = [pe.Stroke(linewidth=6, foreground="#ffffff"), pe.Normal()]

    def line(pts, color=sig, head=True, lw=2.2, ls="-", z=2):
        xs, ys = zip(*pts)
        drawn = ax.plot(xs, ys, color=color, lw=lw, ls=ls, zorder=z, solid_capstyle="butt")[0]
        drawn.set_path_effects(ring)
        if head:
            ax.annotate("", xy=pts[-1], xytext=pts[-2], zorder=z + 0.1, arrowprops=dict(arrowstyle="-|>", color=color, lw=lw, shrinkA=0, shrinkB=0, mutation_scale=16))

    def tag(x, y, s, color=INK2, ha="center"):
        ax.text(x, y, s, fontsize=14, color=color, ha=ha, va="center", zorder=6, bbox=dict(boxstyle="round,pad=0.15", facecolor="#ffffff", edgecolor="none"))

    group(20, 20, 360, 215, "SW  firmware")
    group(400, 20, 830, 215, "RX  receiver")
    group(20, 255, 1210, 325, "TX  transmitter and frequency generation")
    group(1320, 20, 420, 560, "CTL  controller, UI and audio")
    group(20, 610, 360, 230, "ME  enclosure")
    group(400, 610, 1340, 230, "PWR  power")
    blk(40, 50, 320, 165, "cwht-app on rustos pico2 drivers;\ncwht-core logic behind the\napi traits, host-tested;\nruns on the Pico 2 (B12)", "B22")
    blk(420, 50, 180, 165, "Front end:\nBPF, LNA with\nswitched supply,\nRX protection", "B08")
    blk(640, 50, 170, 165, "Mixer and\npost-mixer\namplifier", "B09")
    blk(850, 45, 365, 85, "Candidate A: 8-pole crystal filter,\nIF amp, analog AGC, product detector", "B10", fs=15)
    blk(850, 140, 365, 85, "Candidate B: 1.0 kHz roofing ladder,\nfixed gain, PCM1808 I2S ADC, DSP", "B11", fs=15)
    blk(40, 380, 160, 100, "SMA jack,\nboss-retained", "B01")
    blk(225, 380, 165, 100, "Harmonic LPF\nat the port", "B02")
    blk(420, 380, 180, 100, "T/R relay,\nfails to receive", "B03")
    blk(640, 380, 190, 100, "Driver and PA,\ngate-bias ALC,\nenvelope", "B04")
    blk(860, 380, 140, 100, "Exciter,\nTX buffer", "B05")
    blk(1050, 290, 165, 190, "Synthesizer\nwith TCXO:\nSi5351A or\nLMX2571", "B06")
    blk(870, 490, 345, 82, "HW PA-enable cutoff, T_max 10 s;\nTX inhibit while charging", "B07", fs=14.5)
    blk(1335, 50, 192, 150, "Key inputs: TRS,\n10 k pull-up, 1 k,\n4.7 nF, TPD2E2U06", "B13", fs=14.5)
    blk(1540, 50, 185, 150, "LS013B7DH03 LCD,\ntwo PEC11R\nencoders,\ntwo B3F", "B14", fs=14.5)
    blk(1335, 245, 390, 165, "Pico 2 module\nRP2350, 4 MB flash, micro-USB", "B12", fs=18, fill="#e8f0fb")
    blk(1335, 450, 350, 110, "Audio: PWM DAC, reconstruction,\nTPA6132A2, jack with detect,\nDNP I2S DAC", "B15", fs=14.5)
    blk(40, 645, 320, 175, "CNC 6061 body: PA pedestal\n(heat path), SMA boss,\nLCD window, engraved\nlegend, printed knobs", "B21")
    blk(420, 650, 180, 95, "2S 18650 in two\n1043P holders", "B19")
    blk(640, 650, 190, 95, "S-8252, dual\nN-FET, BQ29209", "B18")
    blk(870, 650, 190, 95, "BQ25887 2S\ncharger", "B17")
    blk(1100, 650, 235, 95, "USB 5 V via Pico 2\nVBUS, 500 mA", "B16")
    blk(1400, 650, 320, 150, "Power switch, 5 V\nsynchronous buck, 3.3 V\nlow-noise LDO (analog\nrail to RX and synthesizer)", "B20", fs=15)
    line([(200, 430), (225, 430)], head=False)
    line([(390, 430), (420, 430)], head=False)
    line([(600, 430), (640, 430)], head=False)
    tag(620, 408, "TX")
    line([(510, 380), (510, 215)])
    tag(510, 300, "RX position")
    line([(600, 132), (640, 132)])
    line([(810, 100), (850, 88)])
    line([(810, 170), (850, 182)])
    line([(860, 430), (830, 430)])
    line([(1050, 430), (1000, 430)])
    tag(1025, 398, "TX\ncarrier")
    line([(1132, 290), (1132, 245), (725, 245), (725, 215)])
    tag(930, 245, "LO, BFO")
    line([(1215, 88), (1272, 88), (1272, 285), (1335, 285)])
    tag(1272, 150, "audio")
    line([(1215, 182), (1250, 182), (1250, 325), (1335, 325)])
    tag(1250, 250, "I2S")
    line([(1431, 200), (1431, 245)])
    line([(1632, 245), (1632, 200)])
    line([(1632, 200), (1632, 245)])
    line([(1510, 410), (1510, 450)])
    line([(1335, 370), (1215, 370)], color=ctl)
    ax.text(1280, 350, "I2C/SPI", fontsize=14, color=ctl, ha="center", va="center", zorder=6)
    line([(1335, 395), (1305, 395), (1305, 532), (1215, 532)], color=ctl)
    ax.text(1267, 464, "TX_KEY,\nstep,\nrelay", fontsize=14, color=ctl, ha="center", va="center", zorder=6, linespacing=1.15)
    line([(870, 532), (720, 532), (720, 480)], color=ctl)
    line([(720, 532), (510, 532), (510, 480)], color=ctl)
    line([(965, 650), (965, 572)], color=ctl)
    tag(965, 600, "charge active", color=ctl)
    line([(1100, 697), (1060, 697)], color=pwr)
    line([(870, 697), (830, 697)], color=pwr)
    line([(640, 697), (600, 697)], color=pwr, head=False)
    line([(800, 650), (800, 480)], color=pwr)
    tag(800, 605, "protected pack", color=pwr)
    line([(735, 745), (735, 818), (1560, 818), (1560, 800)], color=pwr)
    line([(1705, 650), (1705, 410)], color=pwr)
    ax.text(1713, 595, "5 V", fontsize=14, color=pwr, ha="left", va="center", zorder=6)
    line([(190, 480), (190, 645)], color=MUTED, ls=(0, (2, 3)), head=False)
    tag(190, 562, "retention")
    lx, ly = 1262, 596
    for color, text in ((sig, "RF and signal"), (ctl, "control"), (pwr, "power")):
        ax.plot([lx, lx + 36], [ly, ly], color=color, lw=3)
        ax.text(lx + 44, ly, text, fontsize=15, color=INK, va="center")
        lx += 120 if text != "RF and signal" else 178


# name -> (data function, draw function, output file, summary of the data for the log)
FIGURES: dict[str, tuple[Callable[[Context], Any], Callable[[Context, Any, Path], Path], str, Callable[[Any], str]]] = {
    "entrance": (entrance_data, draw_entrance, "entrance-checklist.png", lambda d: "entrance counts " + str({k: len(v) for k, v in d.items()})),
    "success": (success_data, draw_success, "success-criteria.png", lambda d: "success counts " + str({k: len(v) for k, v in d.items()})),
    "requirements": (requirements_data, draw_requirements, "requirements-by-group.png", lambda d: f"requirements {d['total']} total, {d['live']} non-retired, methods {dict(d['methods'])}, TBR {d['tbr']}, {len(d['groups'])} groups"),
    "kdr": (kdr_data, draw_kdr, "kdr-map.png", lambda d: f"KDRs {d['count']} in {len(d['groups'])} groups"),
    "hazards": (hazards_data, draw_hazards, "hazard-matrix.png", lambda d: f"hazards {len(d['hazards'])} from hazards.json {d['version']}"),
    "risk": (risk_data, draw_risk, "risk-matrix.png", lambda d: f"risks {d['active']} active, bands {dict(d['bands'])}, safety override {sorted(i for ids in d['overridden'].values() for i in ids)}"),
    "tpm": (tpm_data, draw_tpm, "tpm-status.png", lambda d: "TPM zones " + str(dict(Counter(r[3] for r in d)))),
    "conops": (conops_data, draw_conops, "conops-modes-scenarios.png", lambda d: f"scenarios {len(d['nominal'])} nominal, {len(d['off_nominal'])} off-nominal"),
    "concept": (concept_data, draw_concept, "concept-block-diagram.png", lambda d: "concept block diagram (literal)"),
}


# ----------------------------------------------------------------------------
# The SRR figure set (docs/reviews/SRR/package.md revision 2, deck review of 2026-09-25)
# ----------------------------------------------------------------------------

# The SRR set leaves out "risk" and "concept": since 2026-09-25 22:53 docs/reviews/SRR/figures/risk-matrix.png
# and concept-block-diagram.png have their own generators beside them (risk-matrix.py reads tools/render_risk.py,
# concept-block-diagram.py reads the Mermaid block of concept section 5), and a default run of this tool must not
# overwrite their renders. The two figure functions stay in FIGURES, with their known-answer tests, until Claude
# chooses one generator per figure; adding a name back to this tuple is the whole change.
SRR = FigureSet(
    review="SRR",
    figures=("entrance", "success", "requirements", "kdr", "hazards", "tpm", "conops"),
    entrance_labels={
        "S1": "Agenda, success criteria agreed", "S2": "Prior RFAs and RIDs (first gate)",
        "S3": "Independent reviewer records", "S4": "Traceability report passes",
        "S5": "TBD/TBR list complete", "S6": "Proposed tailoring listed", "S7": "Risk register current",
        "S8": "TPM status current", "S9": "Visual products rendered", "S10": "Lessons learned reviewed",
        "S11": "Review deck rendered, inspected", "1": "Stakeholders and expectations",
        "2": "Goals and objectives", "3": "MOEs and success criteria", "4": "Concept feasible",
        "5": "Alternative concepts analyzed", "6": "Descope options", "7": "L1 requirements, allocation",
        "8": "Method and note for every L1", "9": "SEMP with HSI section", "10": "ConOps scenarios",
        "11": "Risk approach and assessment", "12": "CM plan", "13": "Document tree defined",
        "14": "Safety analysis, SC determination", "15": "Single point failure philosophy",
        "16": "Acceptance data requirements", "17": "External interface ICD stubs",
        "18": "MOPs, TPMs and KDRs", "19": "Cost estimate and basis", "20": "Technology and toolchain proof",
        "21": "Phase B plan", "22": "Classification record and RMM", "23": "Software plans (preliminary)",
        "24": "Compliance matrix populated", "25": "Regulatory REQ-TX-* file", "26": "Preliminary V&V approach",
        "27": "Maintenance and support concept", "28": "Regulatory corpus present",
    },
    entrance_overrides={
        "10": ("Partially met", "ConOps INSP record missing, the gap that rates rows 1 to 4, 9 and 12 Partially met"),
    },
    tool_run_rows=frozenset({"S4", "8", "24"}),  # Met on the output of a tool without a TV record (package section 2 item H12)
    entrance_notes={
        "Not met": "A Hard row that is not met blocks the\nreadiness declaration and cannot be a lien\n(package section 2; review process 12.2)",
        "Met": "† Met on a tool run with no TV record\nyet: developer evidence, not credited\n(package section 2, item H12)",
    },
    success_labels={
        "4.4-1": "L1 responds to NGOs, MOEs, ConOps", "4.4-2": "Mature enough to begin Phase B",
        "4.4-3": "Allocation and control process", "4.4-4": "Interfaces identified; external ICD stubs missing (row 17, Hard); no lien allowed",
        "4.4-5": "V&V approach for every requirement", "4.4-6": "Major risks and mitigations; 24 Red plans await approval",
        "4.4-7": "Objectives clear, concept feasible; INSP records missing", "4.4-8": "Evaluation criteria; existing assets",
        "4.4-9": "Technical planning for Phase B; SEMP INSP record missing", "4.4-10": "HSI aspects in planning; SEMP INSP record missing",
        "4.4-11": "Fault tolerance in requirements", "4.4-12": "Software SRR-point criteria",
        "C1": "Gate criteria met or on liens", "C2": "Charter, SEMP, RMM compliance", "C3": "TBD and TBR plans",
        "C4": "Tailoring recorded; owner approval pending", "C5": "Software life-cycle criteria",
        "C6": "Risks with accepted residual",
    },
    success_overrides={
        "4.4-4": ("Not met", "no Met-with-lien shortfall may touch interfaces (01 section 12.2)"),
        "4.4-6": ("Partially met", "owner approval of the 24 Red plans pending, as C6"),
        "4.4-7": ("Partially met", "INSP records missing, as entrance row 4"),
        "4.4-9": ("Partially met", "SEMP INSP record missing, as entrance row 9"),
        "4.4-10": ("Partially met", "SEMP INSP record missing, as entrance row 9"),
        "C4": ("Partially met", "owner approval of the tailoring pending"),
    },
    success_footer=(
        "Partially met: the content exists and its INSP record or owner approval is pending, the rating the "
        "entrance rows give the same gap (4.4-6, 4.4-7, 4.4-9, 4.4-10, C4).",
        "4.4-4 is Not met: no lien may touch interfaces (review process 12.2). The chair rules each criterion "
        "Met, Met with lien or Not met.",
    ),
    group_labels={
        "Operating modes": "Operating modes, safe state, faults",
        "Transmitter": "Transmitter, frequency, emissions",
        "Receiver": "Receiver",
        "Keying": "Keying and keyer",
        "Operator interface": "Operator interface, operator model",
        "Audio": "Audio and hearing protection",
        "Power": "Power, battery and charging",
        "Mechanical": "Mechanical, thermal, environment",
        "RF exposure": "RF exposure, operations docs",
        "Firmware": "Firmware and software platform",
        "Production": "Production, sourcing, cost, growth",
    },
    kdr_text=(
        ("Transmitter and emissions", (
            ("008", "Carrier 144.001 to 147.999 MHz"),
            ("010", "Carrier within +/-2.5 ppm, 1 year"),
            ("012", "5 W step within +/-1 dB, 6.4 to 8.4 V"),
            ("017", "Every spurious at most 25 uW"),
            ("018", "Spurious at least 60 dB below carrier"),
        )),
        ("Keying and keyer", (
            ("038", "Straight-key keying"),
            ("039", "Iambic paddle keying"),
            ("042", "Element timing +/-1 % or +/-0.5 ms"),
            ("055", "Hardware cutoff 7.5 to 13 s"),
        )),
        ("Receiver", (("022", "MDS at most -140 dBm in 500 Hz"),)),
        ("Mechanical and thermal", (
            ("102", "Mass at most 350 g"),
            ("103", "Envelope 140 x 70 x 40 mm"),
            ("112", "PA junction at most 110 C"),
        )),
        ("Power", (("094", "8 h at 1:9 on 3000 mAh cells"),)),
        ("RF exposure", (("121", "Exposure evaluation before on-air"),)),
        ("Firmware platform", (("128", "Application runs on host and target"),)),
        ("Production and sourcing", (
            ("137", "Every SMT part placed by PCBWay"),
            ("140", "Stocked at DigiKey, Mouser, PCBWay"),
        )),
    ),
    kdr_columns=((0,), (1, 2), (3, 4, 5), (6, 7)),
    tpm_rows=(
        ("001", "Mass margin", "no estimate at SRR", "status rule"),
        ("002", "Power margin", "-189 % (RX 1.44 W vs 0.5 W)", ""),
        ("003", "Review trend", "no RFA or RID", ""),
        ("004", "PA efficiency", "58 % (target 60 %)", ""),
        ("005", "RX MDS", "no estimate", ""),
        ("006", "Frequency stability", "no estimate", ""),
        ("007", "Spurious margin", "17 dB (target 7 dB)", ""),
        ("008", "Battery life at 1:9", "9.5 h (target 8 h)", ""),
        ("009", "PCB area", "no estimate", ""),
        ("010", "Flash margin", "no estimate", ""),
        ("011", "RAM margin", "no estimate", ""),
        ("012", "Req. volatility", "no baseline yet", ""),
        ("013", "Keyer timing", "no estimate", ""),
        ("014", "Unit cost", "USD 557 (USD 610 TBR)", ""),
        ("015", "Carrier power", "no estimate", ""),
        ("016", "Enclosure envelope", "no estimate at SRR", "status rule"),
        ("017", "SC coverage", "no estimate", ""),
        ("018", "Verification closure", "no estimate", ""),
        ("019", "NCR trend", "0 open NCRs", ""),
        ("020", "Interface maturity", "0 %", ""),
    ),
    status_rule_red=frozenset({"001", "016"}),  # no estimate at a reporting review: Red by the status rule (package section 10)
    tpm_footer="SRR entries carry credit: false. Required leading indicators: TPM-001 mass, TPM-002 power, TPM-003 review trend (SE-62 to SE-64).",
    nominal=(
        ("001", "Unboxing and first power-on"),
        ("002", "Charging from USB"),
        ("003", "Tuning and listening"),
        ("004", "CQ and a QSO with the paddle"),
        ("005", "A straight-key QSO"),
        ("006", "A licensed friend operates"),
        ("007", "Changing the power step"),
        ("008", "Tune carrier, antenna check"),
        ("009", "Low battery"),
        ("010", "Storage and transport"),
        ("011", "Firmware update over USB"),
        ("012", "Kit assembly and hand-over"),
    ),
    off_nominal=(
        ("013", "Mono plug or stuck key"),
        ("014", "Over-temperature in transmit"),
        ("015", "Missing or detuned antenna"),
        ("016", "Charging fault"),
        ("017", "RF pickup on leads"),
        ("018", "Bystander too close"),
        ("019", "Unlicensed guest present"),
        ("020", "Operation at a band edge"),
        ("021", "Reset during transmit"),
        ("022", "Keying held at the face"),
    ),
    concept=srr_concept,
)

FIGURE_SETS: dict[str, FigureSet] = {"SRR": SRR}


# ----------------------------------------------------------------------------
# Entry point
# ----------------------------------------------------------------------------


def collect(ctx: Context, names: list[str]) -> dict[str, Any]:
    """Read and cross-check every input of the named figures; raises FigureDataError before anything is drawn."""
    return {name: FIGURES[name][0](ctx) for name in names}


def render(ctx: Context, names: list[str], out: Path, data: dict[str, Any]) -> list[Path]:
    use_fonts(ctx.log)
    out.mkdir(parents=True, exist_ok=True)
    return [FIGURES[name][1](ctx, data[name], out) for name in names]


def run(review: str, root: Path, out: Path | None = None, figures: list[str] | None = None, check: bool = False,
        figure_sets: dict[str, FigureSet] | None = None) -> tuple[int, list[str]]:
    """Returns (exit status, printed lines). Exit 0 done, 1 data disagreement (nothing written), 2 usage."""
    sets = FIGURE_SETS if figure_sets is None else figure_sets
    lines: list[str] = []
    if not REVIEW_TOKEN.match(review):
        return 2, [f"error: '{review}' is not a review token of charter section 6 (SRR, PDR, CDR, TRR, TRR-Dn, SAR)"]
    spec = sets.get(review)
    if spec is None:
        return 2, [f"error: no figure set is defined for {review}; add one to FIGURE_SETS with its known-answer test"]
    names = list(figures) if figures else list(spec.figures)
    unknown = [n for n in names if n not in spec.figures]
    if unknown:
        return 2, [f"error: figure(s) {', '.join(unknown)} not in the {review} set ({', '.join(spec.figures)})"]
    try:
        ctx = Context(root=root, spec=spec, package=Package(root / "docs" / "reviews" / review / "package.md"))
        data = collect(ctx, names)
    except FigureDataError as exc:
        return 1, [f"error: {exc}; nothing written"]
    lines += [f"  {line}" for line in ctx.log]
    lines += [f"  {FIGURES[name][3](data[name])}" for name in names]
    if check:
        lines.append(f"render_review_figures: {review} check passed for {len(names)} figure(s); nothing written")
        return 0, lines
    ctx.log.clear()
    target = out if out is not None else root / "docs" / "reviews" / review / "figures"
    written = render(ctx, names, target, data)
    lines += [f"  {line}" for line in ctx.log]
    lines += [str(path) for path in written]
    return 0, lines


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0], formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--review", required=True, help="review token (SRR)")
    parser.add_argument("--root", type=Path, default=REPO_ROOT, help="repository root (default: the parent of tools/)")
    parser.add_argument("--out", type=Path, default=None, help="output directory (default: <root>/docs/reviews/<REVIEW>/figures)")
    parser.add_argument("--check", action="store_true", help="read and cross-check every input, write nothing")
    parser.add_argument("figures", nargs="*", help="figure names (default: the whole set)")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    if not root.is_dir():
        parser.error(f"root is not a directory: {root}")
    status, lines = run(args.review, root, args.out.resolve() if args.out else None, args.figures, args.check)
    stream = sys.stderr if status else sys.stdout
    for line in lines:
        print(line, file=stream)
    return status


if __name__ == "__main__":
    sys.exit(main())
