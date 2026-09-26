#!/usr/bin/env python3
"""Render the concept block diagram of docs/design/concept.md section 5.

Source of docs/reviews/SRR/figures/concept-block-diagram.png (charter section 11
rule 3, visual closure; SRR package section 7). The blocks B01 to B22, their
labels, the module groups and every edge with its label and arrow kind are read
at run time from the Mermaid block of concept section 5, so the figure cannot
drift from the concept text. This file holds only the layout: box positions,
edge routes and the line category of each edge. It fails when the Mermaid
source and the layout disagree (a block or an edge added, removed or renamed).

    /Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/docs/reviews/SRR/figures/concept-block-diagram.py
        parse, lay out, run the layout checks, write the PNG
    ... --check
        the same checks, then compare a fresh render with the PNG on disk
        (exit 1 if it differs); writes nothing

Layout checks, each a failure (exit 1): the parsed blocks and edges equal the
layout tables; every block lies inside its module group and outside every other
group; no two blocks or groups overlap; every block label fits inside its box;
no edge segment runs through a block; no two edges run on top of each other; no
edge label, group title or legend entry overlaps a block, another label or an
edge other than its own; every drawn element lies inside the image. Edge
crossings are listed and must equal the reviewed set EXPECTED_CROSSINGS.

Presentation conventions (not in the Mermaid source): line category by colour
and weight (RF and signal, control, power; dotted for the Mermaid dotted
"association" edges); the two 3.3 V analog rail edges from B20 are drawn as rail
connectors (a short arrow at each end naming the block at the other end) instead
of two lines across the figure. Palette: the SRR deck tokens of
docs/reviews/SRR/slides/srr.css; control and power colours are slots 1 and 2 of
the dataviz reference palette (validated together, all checks pass). Font:
Source Sans Pro from the deck's reveal.js copy, the deck typeface.

Tools: matplotlib 3.11.2 in the project venv (tools/toolchain.lock.md section 2,
class B, "plots for review packages").
"""

from __future__ import annotations

import argparse
import io
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
CONCEPT = REPO / "docs" / "design" / "concept.md"
OUTPUT = HERE / "concept-block-diagram.png"
FONT_DIRS = [
    REPO / "docs" / "reviews" / "SRR" / "slides" / "reveal.js" / "dist" / "theme" / "fonts" / "source-sans-pro",
    REPO / "tools" / "slides" / "node_modules" / "reveal.js" / "dist" / "theme" / "fonts" / "source-sans-pro",
]

W, H = 1760, 860  # pixels at 100 dpi; the deck places the image at width 1760

# SRR deck tokens (docs/reviews/SRR/slides/srr.css) and dataviz reference slots 1 and 2.
INK = "#1b1b19"
INK_2 = "#52514e"
NAVY = "#0d366b"
GROUP_FILL = "#f7f7f4"
GROUP_EDGE = "#b3b2ab"
BOX_EDGE = "#0d366b"
CONTROL = "#2a78d6"
POWER = "#eb6834"
ASSOC = "#6b6a65"

BLOCK_SIZES = (12.5, 12.0, 11.5, 11.0, 10.5, 10.0)  # block label font sizes tried in turn (pt)
LABEL_SIZE = 10.5  # edge label font size (pt)

CATEGORY_STYLE = {
    "signal": dict(color=INK, lw=1.25, dashes=None),
    "control": dict(color=CONTROL, lw=1.35, dashes=None),
    "power": dict(color=POWER, lw=1.7, dashes=None),
    "assoc": dict(color=ASSOC, lw=1.1, dashes=(2.0, 2.5)),
}
# (category, text, x of the line sample, y)
LEGEND = [("signal", "RF and signal", 28, 796), ("control", "control", 28, 826), ("power", "power", 200, 796), ("assoc", "association", 200, 826)]

# ---------------------------------------------------------------------------
# Layout (pixels, origin top left, y down)
# ---------------------------------------------------------------------------

GROUP_RECTS = {
    "SW": (20, 24, 380, 226),
    "RX": (400, 24, 1225, 226),
    "CTL": (1345, 24, 1740, 590),
    "TX": (190, 262, 1225, 590),
    "ME": (20, 626, 380, 772),
    "PWR": (400, 626, 1740, 850),
}

NODE_RECTS = {
    "ANT": (20, 290, 180, 512),
    "LPF": (212, 390, 370, 480),
    "TR": (400, 390, 570, 480),
    "PA": (650, 390, 830, 480),
    "EXC": (860, 390, 990, 480),
    "SYN": (1060, 310, 1210, 480),
    "CUT": (860, 506, 1210, 580),
    "FE": (420, 54, 600, 210),
    "MIX": (640, 54, 810, 210),
    "SELA": (850, 50, 1210, 128),
    "SELB": (850, 140, 1210, 218),
    "PICO": (1360, 236, 1725, 420),
    "KEYIN": (1360, 54, 1537, 196),
    "UI": (1553, 54, 1725, 196),
    "AUD": (1420, 470, 1690, 580),
    "USBP": (1100, 668, 1320, 772),
    "CHG": (870, 668, 1060, 772),
    "PROT": (630, 668, 830, 772),
    "PACK": (420, 668, 590, 772),
    "RAILS": (1400, 668, 1725, 790),
    "ENC": (40, 662, 360, 758),
    "FW": (40, 54, 360, 210),
}

# Edge routes keyed by (source, target) as the Mermaid source writes them.
# points: polyline from the source box edge to the target box edge.
# label_at: centre of the edge label (only for edges the source labels).
# label_width: wrap width in pixels for a long label.
# connector: draw a rail connector at the target instead of a line (points is the
# stub, ending on the target box); the matching source stub is in SOURCE_STUBS.
ROUTES = {
    ("ANT", "LPF"): dict(cat="signal", points=[(180, 435), (212, 435)]),
    ("LPF", "TR"): dict(cat="signal", points=[(370, 435), (400, 435)]),
    ("TR", "PA"): dict(cat="signal", points=[(570, 435), (650, 435)], label_at=(610, 422)),
    ("TR", "FE"): dict(cat="signal", points=[(540, 390), (540, 210)], label_at=(540, 318)),
    ("EXC", "PA"): dict(cat="signal", points=[(860, 435), (830, 435)]),
    ("SYN", "EXC"): dict(cat="signal", points=[(1060, 435), (990, 435)], label_at=(1025, 422)),
    ("SYN", "MIX"): dict(cat="signal", points=[(1080, 310), (1080, 244), (725, 244), (725, 210)], label_at=(900, 244)),
    ("FE", "MIX"): dict(cat="signal", points=[(600, 132), (640, 132)]),
    ("MIX", "SELA"): dict(cat="signal", points=[(810, 89), (850, 89)]),
    ("MIX", "SELB"): dict(cat="signal", points=[(810, 179), (850, 179)]),
    ("SELA", "PICO"): dict(cat="signal", points=[(1210, 89), (1315, 89), (1315, 280), (1360, 280)], label_at=(1262, 89)),
    ("SELB", "PICO"): dict(cat="signal", points=[(1210, 179), (1270, 179), (1270, 310), (1360, 310)], label_at=(1240, 179)),
    ("KEYIN", "PICO"): dict(cat="signal", points=[(1448, 196), (1448, 236)]),
    ("UI", "PICO"): dict(cat="signal", points=[(1639, 196), (1639, 236)]),
    ("PICO", "AUD"): dict(cat="signal", points=[(1555, 420), (1555, 470)]),
    ("PICO", "CUT"): dict(cat="control", points=[(1360, 400), (1295, 400), (1295, 545), (1210, 545)], label_at=(1285, 472), label_width=112),
    ("CUT", "PA"): dict(cat="control", points=[(860, 528), (790, 528), (790, 480)]),
    ("CUT", "TR"): dict(cat="control", points=[(860, 562), (485, 562), (485, 480)]),
    ("PICO", "SYN"): dict(cat="control", points=[(1360, 360), (1210, 360)], label_at=(1285, 360)),
    ("USBP", "CHG"): dict(cat="power", points=[(1100, 720), (1060, 720)]),
    ("CHG", "PROT"): dict(cat="power", points=[(870, 720), (830, 720)]),
    ("PROT", "PACK"): dict(cat="power", points=[(630, 720), (590, 720)]),
    ("PROT", "PA"): dict(cat="power", points=[(700, 668), (700, 480)], label_at=(700, 646)),
    ("PROT", "RAILS"): dict(cat="power", points=[(730, 772), (730, 824), (1440, 824), (1440, 790)]),
    ("RAILS", "PICO"): dict(cat="power", points=[(1708, 668), (1708, 420)], label_at=(1708, 608)),
    ("RAILS", "FE"): dict(cat="power", connector=True, points=[(440, 252), (440, 210)], label_at=(432, 245), label_ha="right"),
    ("RAILS", "SYN"): dict(cat="power", connector=True, points=[(1190, 284), (1190, 310)], label_at=(1182, 290), label_ha="right", label_width=80),
    ("USBP", "CUT"): dict(cat="control", points=[(1150, 668), (1150, 580)], label_at=(1150, 646)),
    ("CHG", "PICO"): dict(cat="control", points=[(1040, 772), (1040, 800), (1375, 800), (1375, 420)], label_at=(1375, 525)),
    ("PA", "ENC"): dict(cat="assoc", points=[(668, 480), (668, 608), (330, 608), (330, 662)], label_at=(500, 608)),
    ("ANT", "ENC"): dict(cat="assoc", points=[(160, 512), (160, 662)], label_at=(160, 590)),
    ("FW", "PICO"): dict(cat="assoc", points=[(200, 54), (200, 13), (1335, 13), (1335, 250), (1360, 250)], label_at=(770, 13)),
}

# One source stub per (source, label) of the connector edges.
SOURCE_STUBS = {
    ("RAILS", "3.3 V analog"): dict(points=[(1690, 790), (1690, 820)], label_at=(1680, 820), label_ha="right"),
}

# Reviewed crossings of perpendicular edge segments (no junction; lines cross).
EXPECTED_CROSSINGS = {
    frozenset({("CUT", "TR"), ("PA", "ENC")}),
    frozenset({("CUT", "TR"), ("PROT", "PA")}),
}


# ---------------------------------------------------------------------------
# Mermaid parsing (concept section 5)
# ---------------------------------------------------------------------------

RE_NODE = re.compile(r'^([A-Za-z][A-Za-z0-9_]*)\["([^"]*)"\]$')
RE_SUBGRAPH = re.compile(r'^subgraph\s+([A-Za-z][A-Za-z0-9_]*)\["([^"]*)"\]$')
RE_LABEL = re.compile(r"^(.*) \((B[0-9]{2})\)$")
RE_ID = re.compile(r"\s*([A-Za-z][A-Za-z0-9_]*)\s*")
RE_OP = re.compile(r'\s*(?:(<-->|-->|---)(?:\|"([^"]*)"\|)?|-\.\s*"([^"]*)"\s*\.->)\s*')


class FigureError(Exception):
    pass


def mermaid_block(text: str) -> list[str]:
    start = text.find("\n## 5. System block diagram")
    if start < 0:
        raise FigureError(f"{CONCEPT}: heading '## 5. System block diagram' not found")
    fence = text.find("```mermaid", start)
    end = text.find("```", fence + 10)
    nxt = text.find("\n## ", start + 5)
    if fence < 0 or end < 0 or (0 <= nxt < fence):
        raise FigureError(f"{CONCEPT}: no ```mermaid block in section 5")
    return [ln.strip() for ln in text[fence + 10:end].splitlines() if ln.strip()]


def parse(text: str):
    nodes: dict[str, dict] = {}
    groups: dict[str, str] = {}
    edges: list[dict] = []
    stack: list[str] = []
    for ln in mermaid_block(text):
        if ln.startswith("flowchart"):
            continue
        m = RE_SUBGRAPH.match(ln)
        if m:
            stack.append(m.group(1))
            groups[m.group(1)] = m.group(2)
            continue
        if ln == "end":
            if not stack:
                raise FigureError("unbalanced 'end' in the Mermaid block")
            stack.pop()
            continue
        m = RE_NODE.match(ln)
        if m:
            lab = RE_LABEL.match(m.group(2))
            if not lab:
                raise FigureError(f"node {m.group(1)}: label does not end with a (Bnn) block id")
            nodes[m.group(1)] = dict(label=lab.group(1), block=lab.group(2), group=stack[-1] if stack else None)
            continue
        pos = 0
        m = RE_ID.match(ln, pos)
        if not m:
            raise FigureError(f"cannot parse Mermaid line: {ln}")
        src = m.group(1)
        pos = m.end()
        count = 0
        while pos < len(ln):
            op = RE_OP.match(ln, pos)
            if not op:
                raise FigureError(f"cannot parse Mermaid edge operator in: {ln}")
            nid = RE_ID.match(ln, op.end())
            if not nid:
                raise FigureError(f"edge without a target in: {ln}")
            if op.group(1) is not None:
                kind = {"-->": "arrow", "<-->": "both", "---": "line"}[op.group(1)]
                label = op.group(2)
            else:
                kind = "dotted"
                label = op.group(3)
            edges.append(dict(src=src, dst=nid.group(1), kind=kind, label=label))
            src = nid.group(1)
            pos = nid.end()
            count += 1
        if count == 0:
            raise FigureError(f"line is neither a node, a subgraph nor an edge: {ln}")
    if stack:
        raise FigureError("unclosed subgraph in the Mermaid block")
    return nodes, groups, edges


def check_model(nodes, groups, edges) -> list[str]:
    errs = []
    blocks = sorted(n["block"] for n in nodes.values())
    want = [f"B{i:02d}" for i in range(1, 23)]
    if blocks != want:
        errs.append(f"block ids are {blocks}, expected B01 to B22 once each")
    if set(nodes) != set(NODE_RECTS):
        errs.append(f"layout nodes differ from concept section 5: missing {sorted(set(nodes) - set(NODE_RECTS))}, extra {sorted(set(NODE_RECTS) - set(nodes))}")
    if set(groups) != set(GROUP_RECTS):
        errs.append(f"layout groups differ from concept section 5: missing {sorted(set(groups) - set(GROUP_RECTS))}, extra {sorted(set(GROUP_RECTS) - set(groups))}")
    keys = [(e["src"], e["dst"]) for e in edges]
    dup = sorted({k for k in keys if keys.count(k) > 1})
    if dup:
        errs.append(f"duplicate edges in concept section 5: {dup}")
    if set(keys) != set(ROUTES):
        errs.append(f"layout routes differ from concept section 5: missing {sorted(set(keys) - set(ROUTES))}, extra {sorted(set(ROUTES) - set(keys))}")
    for e in edges:
        r = ROUTES.get((e["src"], e["dst"]))
        if r is None:
            continue
        if (e["kind"] == "dotted") != (r["cat"] == "assoc"):
            errs.append(f"{e['src']} -> {e['dst']}: Mermaid kind {e['kind']} but layout category {r['cat']}")
        if bool(e["label"]) != ("label_at" in r):
            errs.append(f"{e['src']} -> {e['dst']}: label {e['label']!r} in the source but label position {'set' if 'label_at' in r else 'missing'} in the layout")
        if r.get("connector") and (e["src"], e["label"]) not in SOURCE_STUBS:
            errs.append(f"{e['src']} -> {e['dst']}: connector without a source stub for label {e['label']!r}")
    return errs


# ---------------------------------------------------------------------------
# Drawing
# ---------------------------------------------------------------------------

def setup_fonts():
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


UNITS = {"V", "s", "ms", "mA", "uA", "A", "W", "nF", "uF", "Hz", "kHz", "MHz", "k", "MB", "mm", "dB", "ohm", "C"}


def chunks(text: str) -> list[tuple[str, str]]:
    """Unbreakable chunks and the separator after each (" " or "" after a hyphen break).
    A line may break at a space, except before a number that does not follow a comma,
    colon or semicolon and before a unit that follows a number; a hyphenated word of
    14 or more characters whose two parts both have 4 or more may break after its hyphen."""
    out: list[list[str]] = []  # [chunk, sep]
    prev = ""
    for word in text.split():
        parts = word.split("-")
        pieces = [word]
        if len(word) >= 14 and len(parts) == 2 and len(parts[0]) >= 4 and len(parts[1]) >= 4:
            pieces = [parts[0] + "-", parts[1]]
        glue = bool(out) and (
            (word[0].isdigit() and prev[-1:] not in (",", ":", ";"))
            or (word.rstrip(",;") in UNITS and prev[:1].isdigit())
        )
        if glue:
            out[-1][0] += " " + pieces[0]
            out[-1][1] = " "
        else:
            out.append([pieces[0], " "])
        if len(pieces) == 2:
            out[-1][1] = ""
            out.append([pieces[1], " "])
        prev = word
    return [(c, sep) for c, sep in out]


def greedy(renderer, parts, prop, max_px: float) -> list[str]:
    lines: list[str] = []
    cur = ""
    sep = ""
    for chunk, sep_after in parts:
        trial = chunk if not cur else cur + sep + chunk
        if not cur or renderer.get_text_width_height_descent(trial, prop, ismath=False)[0] <= max_px:
            cur = trial
        else:
            lines.append(cur)
            cur = chunk
        sep = sep_after
    if cur:
        lines.append(cur)
    return lines


def wrap(renderer, text: str, prop, max_px: float) -> list[str]:
    """Balanced wrap: the fewest lines greedy wrapping gives at max_px, at the smallest width that keeps that count."""
    toks = chunks(text)
    best = greedy(renderer, toks, prop, max_px)
    lo, hi = max_px * 0.4, max_px
    for _ in range(14):
        mid = (lo + hi) / 2
        trial = greedy(renderer, toks, prop, mid)
        widths = [renderer.get_text_width_height_descent(t, prop, ismath=False)[0] for t in trial]
        if len(trial) <= len(best) and max(widths) <= max_px:
            best, hi = trial, mid
        else:
            lo = mid
    return best


def arrowhead(ax, tip, frm, color, length=10.0, width=7.0, zorder=4):
    from matplotlib.patches import Polygon

    dx, dy = tip[0] - frm[0], tip[1] - frm[1]
    n = (dx * dx + dy * dy) ** 0.5
    ux, uy = dx / n, dy / n
    bx, by = tip[0] - ux * length, tip[1] - uy * length
    px, py = -uy * width / 2, ux * width / 2
    ax.add_patch(Polygon([tip, (bx + px, by + py), (bx - px, by - py)], closed=True, fc=color, ec=color, lw=0.5, zorder=zorder))


def shorten(points, at_start: bool, at_end: bool, by=8.0):
    pts = [list(p) for p in points]
    for flag, i, j in ((at_start, 0, 1), (at_end, -1, -2)):
        if flag:
            (x0, y0), (x1, y1) = pts[i], pts[j]
            dx, dy = x1 - x0, y1 - y0
            n = (dx * dx + dy * dy) ** 0.5
            pts[i] = [x0 + dx / n * by, y0 + dy / n * by]
    return pts


def draw_line(ax, points, cat, head_start, head_end):
    st = CATEGORY_STYLE[cat]
    pts = shorten(points, head_start, head_end)
    (line,) = ax.plot([p[0] for p in pts], [p[1] for p in pts], color=st["color"], lw=st["lw"], solid_joinstyle="miter", solid_capstyle="butt", zorder=3)
    if st["dashes"]:
        line.set_dashes(st["dashes"])
    if head_end:
        arrowhead(ax, points[-1], points[-2], st["color"])
    if head_start:
        arrowhead(ax, points[0], points[1], st["color"])


def data_bbox(ax, artist, renderer, pad=0.0):
    bb = artist.get_window_extent(renderer).transformed(ax.transData.inverted())
    x0, x1 = sorted((bb.x0, bb.x1))
    y0, y1 = sorted((bb.y0, bb.y1))
    return (x0 - pad, y0 - pad, x1 + pad, y1 + pad)


def render(nodes, groups, edges, family):
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.font_manager import FontProperties
    from matplotlib.patches import Rectangle

    plt.rcParams.update({"font.family": family, "svg.hashsalt": "cwht"})
    fig = plt.figure(figsize=(W / 100, H / 100), dpi=100, facecolor="white")
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, W)
    ax.set_ylim(H, 0)
    ax.axis("off")
    renderer = fig.canvas.get_renderer()
    texts = []  # (kind, owner, artist, pad)

    for gid, (x0, y0, x1, y1) in GROUP_RECTS.items():
        ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, fc=GROUP_FILL, ec=GROUP_EDGE, lw=1.0, zorder=1))
        t = ax.text(x0 + 10, y0 + 5, groups[gid], ha="left", va="top", fontsize=12.5, fontweight="semibold", color=INK_2, zorder=2)
        texts.append(("title", gid, t, 1.0))

    fits = {}
    for nid, (x0, y0, x1, y1) in NODE_RECTS.items():
        ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, fc="white", ec=BOX_EDGE, lw=1.2, zorder=2))
        idt = ax.text((x0 + x1) / 2, y1 - 5, nodes[nid]["block"], ha="center", va="bottom", fontsize=11, fontweight="semibold", color=NAVY, zorder=5)
        texts.append(("blockid", nid, idt, 0.0))
        avail_h = (y1 - 26) - (y0 + 6)
        for fs in BLOCK_SIZES:
            prop = FontProperties(family=family, size=fs)
            lines = wrap(renderer, nodes[nid]["label"], prop, (x1 - x0) - 16)
            line_h = renderer.get_text_width_height_descent("Hg", prop, ismath=False)[1] * 1.18
            if len(lines) * line_h <= avail_h:
                break
        fits[nid] = fs
        t = ax.text((x0 + x1) / 2, (y0 + 6 + y1 - 26) / 2, "\n".join(lines), ha="center", va="center", fontsize=fs, color=INK, linespacing=1.18, zorder=5)
        texts.append(("block", nid, t, 0.0))

    label_prop_size = LABEL_SIZE
    for e in edges:
        key = (e["src"], e["dst"])
        r = ROUTES[key]
        if r.get("connector"):
            draw_line(ax, r["points"], r["cat"], False, True)
            text = f"{e['label']} from {nodes[e['src']]['block']}"
        else:
            draw_line(ax, r["points"], r["cat"], e["kind"] == "both", e["kind"] != "line")
            text = e["label"]
        if text:
            prop = FontProperties(family=family, size=label_prop_size)
            if "label_width" in r:
                text = "\n".join(wrap(renderer, text, prop, r["label_width"]))
            lx, ly = r["label_at"]
            t = ax.text(lx, ly, text, ha=r.get("label_ha", "center"), va="center", fontsize=label_prop_size, color=INK_2, linespacing=1.1, zorder=6,
                        bbox=dict(boxstyle="square,pad=0.12", fc="white", ec="none"))
            texts.append(("label", key, t, 1.5))

    for (src, lab), s in SOURCE_STUBS.items():
        targets = [nodes[e["dst"]]["block"] for e in edges if e["src"] == src and e["label"] == lab and ROUTES[(e["src"], e["dst"])].get("connector")]
        draw_line(ax, s["points"], "power", False, True)
        lx, ly = s["label_at"]
        t = ax.text(lx, ly, f"{lab} to {', '.join(targets)}", ha=s.get("label_ha", "center"), va="center", fontsize=label_prop_size, color=INK_2, zorder=6,
                    bbox=dict(boxstyle="square,pad=0.12", fc="white", ec="none"))
        texts.append(("label", ("stub", src), t, 1.5))

    for cat, name, lx, y in LEGEND:
        st = CATEGORY_STYLE[cat]
        (line,) = ax.plot([lx, lx + 30], [y, y], color=st["color"], lw=st["lw"] + 0.4, solid_capstyle="butt", zorder=3)
        if st["dashes"]:
            line.set_dashes(st["dashes"])
        t = ax.text(lx + 38, y, name, ha="left", va="center", fontsize=11.5, color=INK, zorder=5)
        texts.append(("legend", cat, t, 1.0))

    fig.canvas.draw()
    boxes = {k: data_bbox(ax, t, renderer, pad) for (_, _, t, pad) in texts for k in [id(t)]}
    return fig, ax, texts, boxes, fits


# ---------------------------------------------------------------------------
# Layout checks
# ---------------------------------------------------------------------------

def overlap(a, b, tol=0.0) -> bool:
    return a[0] < b[2] - tol and b[0] < a[2] - tol and a[1] < b[3] - tol and b[1] < a[3] - tol


def inside(inner, outer, margin=0.0) -> bool:
    return inner[0] >= outer[0] + margin and inner[1] >= outer[1] + margin and inner[2] <= outer[2] - margin and inner[3] <= outer[3] - margin


def segments(points):
    return list(zip(points[:-1], points[1:]))


def seg_hits_rect(p, q, rect) -> bool:
    """Liang-Barsky: does segment p-q enter the open rectangle."""
    x0, y0, x1, y1 = rect
    dx, dy = q[0] - p[0], q[1] - p[1]
    t0, t1 = 0.0, 1.0
    for pv, qv in ((-dx, p[0] - x0), (dx, x1 - p[0]), (-dy, p[1] - y0), (dy, y1 - p[1])):
        if pv == 0:
            if qv <= 0:
                return False
        else:
            t = qv / pv
            if pv < 0:
                t0 = max(t0, t)
            else:
                t1 = min(t1, t)
    return t0 < t1


def cross_point(s1, s2):
    (a, b), (c, d) = s1, s2
    h1, h2 = a[1] == b[1], c[1] == d[1]
    if h1 == h2:
        return None
    hs, vs = (s1, s2) if h1 else (s2, s1)
    y = hs[0][1]
    x = vs[0][0]
    xa, xb = sorted((hs[0][0], hs[1][0]))
    ya, yb = sorted((vs[0][1], vs[1][1]))
    if xa < x < xb and ya < y < yb:
        return (x, y)
    return None


def drawn_polylines(edges):
    lines = {}
    for e in edges:
        lines[(e["src"], e["dst"])] = ROUTES[(e["src"], e["dst"])]["points"]
    for (src, _), s in SOURCE_STUBS.items():
        lines[("stub", src)] = s["points"]
    return lines


def run_checks(nodes, edges, texts, boxes, fits) -> tuple[list[str], list[str]]:
    errs: list[str] = []
    info: list[str] = []
    canvas = (0, 0, W, H)
    # blocks inside their group, outside the others; no overlaps
    for nid, rect in NODE_RECTS.items():
        g = nodes[nid]["group"]
        for gid, grect in GROUP_RECTS.items():
            if gid == g and not inside(rect, grect, 4):
                errs.append(f"block {nid} is not inside group {gid}")
            if gid != g and overlap(rect, grect):
                errs.append(f"block {nid} overlaps group {gid}, which does not contain it")
    ids = list(NODE_RECTS)
    for i, a in enumerate(ids):
        for b in ids[i + 1:]:
            if overlap(NODE_RECTS[a], NODE_RECTS[b], -6):
                errs.append(f"blocks {a} and {b} overlap or are closer than 6 px")
    gids = list(GROUP_RECTS)
    for i, a in enumerate(gids):
        for b in gids[i + 1:]:
            if overlap(GROUP_RECTS[a], GROUP_RECTS[b], -10):
                errs.append(f"groups {a} and {b} overlap or are closer than 10 px")
    # text inside blocks and inside the canvas
    for kind, owner, t, _ in texts:
        bb = boxes[id(t)]
        if not inside(bb, canvas, 1):
            errs.append(f"{kind} {owner}: text is clipped by the image edge {tuple(round(v) for v in bb)}")
        if kind in ("block", "blockid") and not inside(bb, NODE_RECTS[owner], 2):
            errs.append(f"{kind} {owner}: text does not fit inside its box {tuple(round(v) for v in bb)}")
    b_text = {owner: boxes[id(t)] for kind, owner, t, _ in texts if kind == "block"}
    b_id = {owner: boxes[id(t)] for kind, owner, t, _ in texts if kind == "blockid"}
    for nid in NODE_RECTS:
        if overlap(b_text[nid], b_id[nid]):
            errs.append(f"block {nid}: label text overlaps the block id")
    # edges: no segment through a block; no two edges on top of each other
    lines = drawn_polylines(edges)
    for key, pts in lines.items():
        for p, q in segments(pts):
            if p[0] != q[0] and p[1] != q[1]:
                errs.append(f"edge {key}: segment {p}-{q} is not horizontal or vertical")
            for nid, rect in NODE_RECTS.items():
                if seg_hits_rect(p, q, (rect[0] + 1, rect[1] + 1, rect[2] - 1, rect[3] - 1)):
                    errs.append(f"edge {key}: segment {p}-{q} runs through block {nid}")
        for p in pts:
            if not inside((p[0], p[1], p[0], p[1]), canvas, 2):
                errs.append(f"edge {key}: point {p} is outside the image")
    keys = list(lines)
    crossings = set()
    for i, a in enumerate(keys):
        for b in keys[i + 1:]:
            for s1 in segments(lines[a]):
                for s2 in segments(lines[b]):
                    for axis in (0, 1):
                        o = 1 - axis
                        if s1[0][o] == s1[1][o] and s2[0][o] == s2[1][o] and abs(s1[0][o] - s2[0][o]) < 6:
                            lo = max(min(s1[0][axis], s1[1][axis]), min(s2[0][axis], s2[1][axis]))
                            hi = min(max(s1[0][axis], s1[1][axis]), max(s2[0][axis], s2[1][axis]))
                            if hi - lo > 0:
                                errs.append(f"edges {a} and {b} run on top of each other (closer than 6 px over {hi - lo:.0f} px)")
                    cp = cross_point(s1, s2)
                    if cp:
                        crossings.add(frozenset({a, b}))
                        info.append(f"crossing: {a} x {b} at {cp}")
    if crossings != EXPECTED_CROSSINGS:
        errs.append(f"edge crossings changed: now {sorted(tuple(sorted(c)) for c in crossings)}, reviewed set {sorted(tuple(sorted(c)) for c in EXPECTED_CROSSINGS)}")
    # labels, titles and legend: no overlap with blocks, other texts, or foreign edges
    free = [(kind, owner, t) for kind, owner, t, _ in texts if kind in ("label", "title", "legend")]
    for idx, (kind, owner, t) in enumerate(free):
        bb = boxes[id(t)]
        for nid, rect in NODE_RECTS.items():
            if overlap(bb, rect):
                errs.append(f"{kind} {owner}: overlaps block {nid}")
        for kind2, owner2, t2 in free[idx + 1:]:
            if overlap(bb, boxes[id(t2)]):
                errs.append(f"{kind} {owner} overlaps {kind2} {owner2}")
        for key, pts in lines.items():
            if kind == "label" and key == owner:
                continue
            for p, q in segments(pts):
                if seg_hits_rect(p, q, bb):
                    errs.append(f"{kind} {owner}: overlaps edge {key}")
                    break
    small = sorted(n for n, fs in fits.items() if fs < BLOCK_SIZES[0])
    info.append(f"block label size {BLOCK_SIZES[0]} pt except " + (", ".join(f"{n} {fits[n]} pt" for n in small) if small else "none"))
    return errs, info


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Render the concept block diagram (concept section 5).")
    ap.add_argument("--check", action="store_true", help="run the checks and compare a fresh render with the PNG on disk; write nothing")
    ap.add_argument("--output", type=Path, default=OUTPUT)
    args = ap.parse_args(argv)
    try:
        nodes, groups, edges = parse(CONCEPT.read_text(encoding="utf-8"))
    except (OSError, FigureError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    errs = check_model(nodes, groups, edges)
    if errs:
        for e in errs:
            print(f"ERROR: {e}", file=sys.stderr)
        return 1
    family = setup_fonts()
    fig, ax, texts, boxes, fits = render(nodes, groups, edges, family)
    errs, info = run_checks(nodes, edges, texts, boxes, fits)
    for i in info:
        print(f"INFO: {i}")
    if errs:
        for e in errs:
            print(f"ERROR: {e}", file=sys.stderr)
        print(f"{len(errs)} layout error(s); nothing written.", file=sys.stderr)
        return 1
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=100, facecolor="white", metadata={"Software": None})
    png = buf.getvalue()
    print(f"concept section 5: {len(nodes)} blocks, {len(groups)} groups, {len(edges)} edges; layout checks passed")
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
