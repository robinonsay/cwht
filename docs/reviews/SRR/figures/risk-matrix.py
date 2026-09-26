#!/usr/bin/env python3
"""Render the 5x5 risk matrix of docs/risk/register.json.

Source of docs/reviews/SRR/figures/risk-matrix.png (charter section 5 "Risk
register (5x5) ... + rendered matrix"; 01 entrance criterion S7; SRR package
sections 7 and 11). The scoring rules are not restated here: the likelihood and
consequence names, the maximum-dimension placement, the cell band and the safety
override come from tools/render_risk.py, which implements
docs/process/06-risk-and-decision-analysis.md sections 7 and 8.

    /Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/docs/reviews/SRR/figures/risk-matrix.py
        validate the register, cross-check, lay out, write the PNG
    ... --check
        the same, then compare a fresh render with the PNG on disk (exit 1 if
        it differs); writes nothing

Failures (exit 1): the register fails the render_risk.py validation (JSON Schema
and structural rules); the cell contents differ from the "5x5 matrix (active
risks)" table of docs/risk/register.md (so the figure and the controlled
Markdown render agree); a drawn id count differs from the active-risk count;
any text leaves its cell or the image, or two texts overlap.

Palette: the SRR deck status tokens of docs/reviews/SRR/slides/srr.css (band
backgrounds and band text colours); every band is also named by its letter, so
colour is never the only cue. Font: Source Sans Pro from the deck's reveal.js
copy. Tools: matplotlib 3.11.2 in the project venv (tools/toolchain.lock.md
section 2, class B, "plots for review packages").
"""

from __future__ import annotations

import argparse
import io
import json
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
sys.path.insert(0, str(REPO / "tools"))
import render_risk as rr  # noqa: E402  (scoring rules of 06 sections 7 and 8)

REGISTER = REPO / "docs" / "risk" / "register.json"
REGISTER_MD = REPO / "docs" / "risk" / "register.md"
OUTPUT = HERE / "risk-matrix.png"
FONT_DIRS = [
    REPO / "docs" / "reviews" / "SRR" / "slides" / "reveal.js" / "dist" / "theme" / "fonts" / "source-sans-pro",
    REPO / "tools" / "slides" / "node_modules" / "reveal.js" / "dist" / "theme" / "fonts" / "source-sans-pro",
]

W, H = 1760, 830  # pixels at 100 dpi; the deck places the image at width 1760

INK = "#1b1b19"
INK_2 = "#52514e"
BAND_BG = {"Red": "#fbe1e1", "Yellow": "#fdf0cc", "Green": "#dcf3dc"}
BAND_TEXT = {"Red": "#b42323", "Yellow": "#8a5a00", "Green": "#0b6b0b"}

GRID_X0, GRID_X1 = 250, 1730
GRID_Y0, GRID_Y1 = 92, 752
GAP = 4
PAD = 8
OVERRIDE_MARK = "*"


class FigureError(Exception):
    pass


def setup_fonts() -> str:
    from matplotlib import font_manager

    for d in FONT_DIRS:
        reg = d / "source-sans-pro-regular.ttf"
        semi = d / "source-sans-pro-semibold.ttf"
        if reg.exists() and semi.exists():
            font_manager.fontManager.addfont(str(reg))
            font_manager.fontManager.addfont(str(semi))
            return "Source Sans Pro"
    print("WARNING: Source Sans Pro not found; falling back to DejaVu Sans (the PNG will differ)", file=sys.stderr)
    return "DejaVu Sans"


def load_register() -> dict:
    register = json.loads(REGISTER.read_text(encoding="utf-8"))
    rep = rr.Report()
    used = rr.validate_with_jsonschema(register, rep)
    if not used:
        raise FigureError("jsonschema not importable; run with /Users/robinonsay/rust/cwht/.venv/bin/python")
    rr.validate(register, rep)
    if rep.errors:
        raise FigureError("register.json fails tools/render_risk.py validation: " + "; ".join(rep.errors))
    return register


def cells_from_register(register: dict):
    active = [r for r in register["risks"] if r["status"] not in rr.INACTIVE]
    cells: dict[tuple[int, int], list[dict]] = {}
    for r in active:
        cells.setdefault((r["likelihood"], rr.max_consequence(r)), []).append(r)
    for v in cells.values():
        v.sort(key=lambda r: r["id"])
    return active, cells


def cells_from_markdown() -> dict[tuple[int, int], list[str]]:
    """The '5x5 matrix (active risks)' table of register.md, as written by tools/render_risk.py."""
    text = REGISTER_MD.read_text(encoding="utf-8")
    start = text.find("## 5x5 matrix (active risks)")
    if start < 0:
        raise FigureError(f"{REGISTER_MD}: section '5x5 matrix (active risks)' not found")
    rows = [ln for ln in text[start:].splitlines()[1:] if ln.startswith("| **")]
    out: dict[tuple[int, int], list[str]] = {}
    for ln in rows[:5]:
        cols = [c.strip() for c in ln.strip().strip("|").split("|")]
        likelihood = int(re.match(r"\*\*([1-5]) ", cols[0]).group(1))
        for c, cell in enumerate(cols[1:6], start=1):
            ids = re.findall(r"RSK-[0-9]{3}", cell)
            if ids:
                out[(likelihood, c)] = sorted(ids)
    if len(rows) < 5:
        raise FigureError(f"{REGISTER_MD}: the matrix table has {len(rows)} likelihood rows, expected 5")
    return out


def cell_rect(likelihood: int, consequence: int):
    cw = (GRID_X1 - GRID_X0 + GAP) / 5
    rh = (GRID_Y1 - GRID_Y0 + GAP) / 5
    x0 = GRID_X0 + (consequence - 1) * cw
    y0 = GRID_Y0 + (5 - likelihood) * rh
    return (x0, y0, x0 + cw - GAP, y0 + rh - GAP)


def data_bbox(ax, artist, renderer):
    bb = artist.get_window_extent(renderer).transformed(ax.transData.inverted())
    x0, x1 = sorted((bb.x0, bb.x1))
    y0, y1 = sorted((bb.y0, bb.y1))
    return (x0, y0, x1, y1)


def overlap(a, b) -> bool:
    return a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]


def inside(inner, outer, margin=0.0) -> bool:
    return inner[0] >= outer[0] + margin and inner[1] >= outer[1] + margin and inner[2] <= outer[2] - margin and inner[3] <= outer[3] - margin


def render(register: dict, active, cells, family):
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.font_manager import FontProperties
    from matplotlib.patches import Rectangle

    plt.rcParams.update({"font.family": family})
    fig = plt.figure(figsize=(W / 100, H / 100), dpi=100, facecolor="white")
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, W)
    ax.set_ylim(H, 0)
    ax.axis("off")
    renderer = fig.canvas.get_renderer()
    texts = []  # (owner, artist, container rect or None)

    t = ax.text((GRID_X0 + GRID_X1) / 2, 14, "Consequence (maximum of the five dimensions) across, likelihood down",
                ha="center", va="top", fontsize=13, color=INK_2)
    texts.append(("heading", t, None))
    for c in range(1, 6):
        x0, _, x1, _ = cell_rect(5, c)
        t = ax.text((x0 + x1) / 2, GRID_Y0 - 12, f"{c} {rr.CONSEQUENCE_NAME[c]}", ha="center", va="bottom", fontsize=15, color=INK)
        texts.append((f"column {c}", t, None))
    for lk in range(1, 6):
        _, y0, _, y1 = cell_rect(lk, 1)
        t = ax.text(GRID_X0 - 16, (y0 + y1) / 2, f"{lk} {rr.LIKELIHOOD_NAME[lk]}", ha="right", va="center", fontsize=15, color=INK)
        texts.append((f"row {lk}", t, None))

    id_prop = FontProperties(family=family, size=13)
    drawn = 0
    for lk in range(1, 6):
        for c in range(1, 6):
            rect = cell_rect(lk, c)
            x0, y0, x1, y1 = rect
            band = rr.cell_band(lk, c)
            ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, fc=BAND_BG[band], ec="none", zorder=1))
            t = ax.text(x0 + PAD, y0 + 6, f"{rr.BAND_MARK[band]} {lk * c}", ha="left", va="top", fontsize=11.5, color=BAND_TEXT[band], zorder=3)
            texts.append((f"cell {lk},{c} corner", t, rect))
            risks = cells.get((lk, c), [])
            if not risks:
                continue
            t = ax.text(x1 - PAD, y0 + 4, str(len(risks)), ha="right", va="top", fontsize=15, fontweight="semibold", color=INK, zorder=3)
            texts.append((f"cell {lk},{c} count", t, rect))
            labels = [r["id"].split("-")[1] + (OVERRIDE_MARK if rr.red_by_override(r) else "") for r in risks]
            lines, cur = [], ""
            for lab in labels:
                trial = lab if not cur else cur + "  " + lab
                if cur and renderer.get_text_width_height_descent(trial, id_prop, ismath=False)[0] > (x1 - x0) - 2 * PAD:
                    lines.append(cur)
                    cur = lab
                else:
                    cur = trial
            lines.append(cur)
            drawn += len(labels)
            t = ax.text(x0 + PAD, y0 + 30, "\n".join(lines), ha="left", va="top", fontsize=13, color=INK, linespacing=1.3, zorder=3)
            texts.append((f"cell {lk},{c} ids", t, rect))
            if any(rr.red_by_override(r) for r in risks):
                t = ax.text(x0 + PAD, y1 - 6, f"{OVERRIDE_MARK} Red by safety override", ha="left", va="bottom", fontsize=12.5,
                            fontweight="semibold", color=BAND_TEXT["Red"], zorder=3)
                texts.append((f"cell {lk},{c} override note", t, rect))

    by_band = Counter(rr.risk_band(r) for r in active)
    n_override = sum(1 for r in active if rr.red_by_override(r))
    x = GRID_X0
    ly = GRID_Y1 + 30
    for band in ("Red", "Yellow", "Green"):
        ax.add_patch(Rectangle((x, ly - 12), 28, 24, fc=BAND_BG[band], ec=BAND_TEXT[band], lw=1.2, zorder=2))
        label = f"{band} {by_band.get(band, 0)}"
        if band == "Red" and n_override:
            label += f" ({n_override} by safety override)"
        t = ax.text(x + 38, ly, label, ha="left", va="center", fontsize=15, color=INK, zorder=3)
        texts.append((f"legend {band}", t, None))
        fig.canvas.draw()
        x = data_bbox(ax, t, renderer)[2] + 34
    t = ax.text(x + 10, ly, f"{len(active)} active risks; cell numbers are RSK-nnn; corner: cell band and score L x C", ha="left", va="center",
                fontsize=13, color=INK_2, zorder=3)
    texts.append(("legend note", t, None))
    t = ax.text(GRID_X0, ly + 34, f"{OVERRIDE_MARK} safety consequence 5 at likelihood 2 or more is Red whatever the cell band (06 section 7).   "
                f"Source: docs/risk/register.json {register['version']}, updated {register['updated']}; scored by tools/render_risk.py.",
                ha="left", va="center", fontsize=11.5, color=INK_2, zorder=3)
    texts.append(("source note", t, None))

    fig.canvas.draw()
    boxes = {id(a): data_bbox(ax, a, renderer) for _, a, _ in texts}
    return fig, texts, boxes, drawn


def run_checks(active, cells, texts, boxes, drawn) -> list[str]:
    errs = []
    if drawn != len(active):
        errs.append(f"{drawn} ids drawn, {len(active)} active risks")
    canvas = (0, 0, W, H)
    for owner, a, rect in texts:
        bb = boxes[id(a)]
        if not inside(bb, canvas, 1):
            errs.append(f"{owner}: text is clipped by the image edge {tuple(round(v) for v in bb)}")
        if rect is not None and not inside(bb, rect, 2):
            errs.append(f"{owner}: text leaves its cell {tuple(round(v) for v in bb)}")
    for i, (o1, a1, _) in enumerate(texts):
        for o2, a2, _ in texts[i + 1:]:
            if overlap(boxes[id(a1)], boxes[id(a2)]):
                errs.append(f"{o1} overlaps {o2}")
    return errs


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Render the 5x5 risk matrix of docs/risk/register.json.")
    ap.add_argument("--check", action="store_true", help="run the checks and compare a fresh render with the PNG on disk; write nothing")
    ap.add_argument("--output", type=Path, default=OUTPUT)
    args = ap.parse_args(argv)
    try:
        register = load_register()
        active, cells = cells_from_register(register)
        md = cells_from_markdown()
    except (OSError, json.JSONDecodeError, FigureError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    fig_cells = {k: sorted(r["id"] for r in v) for k, v in cells.items()}
    if fig_cells != md:
        print("ERROR: register.json cells differ from the docs/risk/register.md matrix; run tools/render_risk.py first", file=sys.stderr)
        for k in sorted(set(fig_cells) | set(md)):
            if fig_cells.get(k) != md.get(k):
                print(f"  cell L{k[0]} C{k[1]}: register.json {fig_cells.get(k)} register.md {md.get(k)}", file=sys.stderr)
        return 1
    family = setup_fonts()
    fig, texts, boxes, drawn = render(register, active, cells, family)
    errs = run_checks(active, cells, texts, boxes, drawn)
    if errs:
        for e in errs:
            print(f"ERROR: {e}", file=sys.stderr)
        print(f"{len(errs)} layout error(s); nothing written.", file=sys.stderr)
        return 1
    bands = Counter(rr.risk_band(r) for r in active)
    print(f"register {register['version']} ({register['updated']}): {len(active)} active risks, Red {bands['Red']}, Yellow {bands['Yellow']}, Green {bands['Green']}; "
          f"cells agree with register.md; layout checks passed")
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=100, facecolor="white", metadata={"Software": None})
    png = buf.getvalue()
    if args.check:
        current = args.output.read_bytes() if args.output.exists() else None
        if current != png:
            print(f"ERROR: {args.output} is stale; run without --check", file=sys.stderr)
            return 1
        print(f"{args.output} is current")
        return 0
    args.output.write_bytes(png)
    print(f"wrote {args.output} ({W} x {H} px)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
