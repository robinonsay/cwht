#!/usr/bin/env python3
"""Render the interface-plane figures of the five external ICD stubs.

Source of docs/icd/figures/ICD-<A>-<B>-plane.png for ICD-CTL-KEY, ICD-CTL-PHONES,
ICD-TX-ANT, ICD-CTL-USB and ICD-PWR-CELL (docs/templates/icd.md section 3.1.1:
every physical interface carries a rendered figure; charter section 11 rule 3,
visual closure; checklist docs/templates/peer-review-checklist-design.md item
CK-DES-I4). Every number drawn is a value of the ICD tables it illustrates; a
value that is (TBR) in the ICD is drawn with "(TBR)".

    /Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/docs/icd/figures/render_icd_figures.py
        lay out, run the layout checks, write the five PNGs
    ... --check
        the same checks, then compare fresh renders with the PNGs on disk
        (exit 1 if any differs); writes nothing
    ... --only ICD-CTL-KEY
        render one figure
    ... --draft DIR
        write the PNGs into DIR even when a layout check fails (iteration only)

Layout checks, each a failure (exit 1): every text lies inside the image;
no two checked texts overlap; no checked text overlaps a component box other
than the one it labels.

Palette and font follow docs/reviews/SRR/figures/concept-block-diagram.py (SRR
deck tokens; Source Sans Pro from the deck's reveal.js copy, DejaVu Sans as a
fallback with a warning). Tools: matplotlib 3.11.2 in the project venv
(tools/toolchain.lock.md section 2, class B, plots for review packages).
"""

from __future__ import annotations

import argparse
import io
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Circle, FancyBboxPatch, Polygon, Rectangle  # noqa: E402

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
FONT_DIRS = (
    REPO / "docs" / "reviews" / "SRR" / "slides" / "reveal.js" / "dist" / "theme" / "fonts" / "source-sans-pro",
    REPO / "tools" / "slides" / "node_modules" / "reveal.js" / "dist" / "theme" / "fonts" / "source-sans-pro",
)

INK = "#1b1b19"
INK_2 = "#52514e"
NAVY = "#0d366b"
GROUP_FILL = "#f7f7f4"
GROUP_EDGE = "#b3b2ab"
EXT_FILL = "#eef3fa"
CONTROL = "#2a78d6"
POWER = "#eb6834"
ASSOC = "#6b6a65"
PLANE = "#b3261e"
METAL = "#c9c8c2"
METAL_DARK = "#8d8c86"
TBR_NOTE = "Values marked (TBR) are open; owner, plan and close-by are in section 6 of the ICD."

W, H = 1600, 1000


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


class Canvas:
    """A pixel-coordinate drawing surface (origin bottom left) with layout checks."""

    def __init__(self, name: str, family: str, width: int = W, height: int = H):
        plt.rcParams.update({"font.family": family, "svg.hashsalt": "cwht"})
        self.name = name
        self.w, self.h = width, height
        self.fig = plt.figure(figsize=(width / 100, height / 100), dpi=100, facecolor="white")
        self.ax = self.fig.add_axes([0, 0, 1, 1])
        self.ax.set_xlim(0, width)
        self.ax.set_ylim(0, height)
        self.ax.axis("off")
        self.texts: list[tuple[object, str | None]] = []
        self.boxes: dict[str, tuple[float, float, float, float]] = {}
        self._n = 0

    # -- text ---------------------------------------------------------------
    def text(self, x, y, s, ha="left", va="center", fs=12.5, color=INK, weight="normal", owner=None, check=True, rotation=0, style="normal"):
        t = self.ax.text(x, y, s, ha=ha, va=va, fontsize=fs, color=color, fontweight=weight, rotation=rotation, linespacing=1.2, zorder=8, fontstyle=style)
        if check:
            self.texts.append((t, owner))
        return t

    def header(self, title, subtitle):
        self.text(30, self.h - 32, title, fs=19, weight="semibold", color=NAVY)
        self.text(30, self.h - 62, subtitle, fs=12.5, color=INK_2)
        self.text(30, 22, TBR_NOTE + " Source: docs/icd/figures/render_icd_figures.py.", fs=11.5, color=INK_2)

    # -- shapes -------------------------------------------------------------
    def box(self, x, y, w, h, label=None, fs=12.5, fill="white", edge=NAVY, lw=1.4, weight="normal", name=None, color=INK, ha="center", register=True, round_=True):
        self._n += 1
        name = name or f"box{self._n}"
        style = "round,pad=0,rounding_size=6" if round_ else "square,pad=0"
        self.ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=style, fc=fill, ec=edge, lw=lw, zorder=4))
        if register:
            self.boxes[name] = (x, y, x + w, y + h)
        if label:
            tx = x + w / 2 if ha == "center" else x + 10
            self.text(tx, y + h / 2, label, ha=ha, va="center", fs=fs, weight=weight, owner=name, color=color)
        return name

    def panel(self, x, y, w, h, title=None, fill=GROUP_FILL, edge=GROUP_EDGE):
        self.ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=10", fc=fill, ec=edge, lw=1.2, zorder=1))
        if title:
            self.text(x + 14, y + h - 18, title, fs=13.5, weight="semibold", color=INK_2)

    def rect(self, x, y, w, h, fill=METAL, edge=METAL_DARK, lw=1.2, z=3, hatch=None):
        self.ax.add_patch(Rectangle((x, y), w, h, fc=fill, ec=edge, lw=lw, zorder=z, hatch=hatch))

    def poly(self, pts, fill=METAL, edge=METAL_DARK, lw=1.2, z=3):
        self.ax.add_patch(Polygon(pts, closed=True, fc=fill, ec=edge, lw=lw, zorder=z))

    def line(self, pts, color=INK, lw=1.4, dash=None, z=3):
        (ln,) = self.ax.plot([p[0] for p in pts], [p[1] for p in pts], color=color, lw=lw, zorder=z, solid_capstyle="butt")
        if dash:
            ln.set_dashes(dash)
        return ln

    def arrow(self, p0, p1, color=INK, lw=1.4, head=10, z=5, both=False):
        self.line([p0, p1], color=color, lw=lw, z=z)
        self._head(p1, p0, color, head, z)
        if both:
            self._head(p0, p1, color, head, z)

    def _head(self, tip, frm, color, length, z):
        import math

        dx, dy = tip[0] - frm[0], tip[1] - frm[1]
        d = math.hypot(dx, dy) or 1.0
        ux, uy = dx / d, dy / d
        bx, by = tip[0] - ux * length, tip[1] - uy * length
        px, py = -uy * length * 0.38, ux * length * 0.38
        self.ax.add_patch(Polygon([tip, (bx + px, by + py), (bx - px, by - py)], closed=True, fc=color, ec=color, lw=0.5, zorder=z))

    def dot(self, x, y, color=INK, r=4):
        self.ax.add_patch(Circle((x, y), r, fc=color, ec=color, zorder=6))

    def ground(self, x, y, color=INK):
        self.line([(x, y), (x, y - 12)], color=color)
        for i, half in enumerate((12, 8, 4)):
            self.line([(x - half, y - 12 - 5 * i), (x + half, y - 12 - 5 * i)], color=color, lw=1.4)

    def rail(self, x, y, label, color=INK):
        self.line([(x, y), (x, y + 12)], color=color)
        self.line([(x - 12, y + 12), (x + 12, y + 12)], color=color, lw=1.8)
        self.text(x, y + 26, label, ha="center", fs=11.5, color=color)

    def resistor_h(self, x0, x1, y, label=None, above=True, fs=11.5, color=INK):
        """Horizontal IEC resistor between x0 and x1 (body 46 x 16 px, centered)."""
        xm = (x0 + x1) / 2
        self.line([(x0, y), (xm - 23, y)], color=color)
        self.line([(xm + 23, y), (x1, y)], color=color)
        self.ax.add_patch(Rectangle((xm - 23, y - 8), 46, 16, fc="white", ec=color, lw=1.4, zorder=5))
        if label:
            self.text(xm, y + (24 if above else -24), label, ha="center", fs=fs)

    def resistor_v(self, x, y0, y1, label=None, right=True, fs=11.5, color=INK):
        ym = (y0 + y1) / 2
        self.line([(x, y0), (x, ym - 23)], color=color)
        self.line([(x, ym + 23), (x, y1)], color=color)
        self.ax.add_patch(Rectangle((x - 8, ym - 23), 16, 46, fc="white", ec=color, lw=1.4, zorder=5))
        if label:
            self.text(x + (16 if right else -16), ym, label, ha="left" if right else "right", fs=fs)

    def cap_v(self, x, y0, y1, label=None, right=True, fs=11.5, color=INK):
        ym = (y0 + y1) / 2
        self.line([(x, y0), (x, ym + 5)], color=color)
        self.line([(x, ym - 5), (x, y1)], color=color)
        self.line([(x - 14, ym + 5), (x + 14, ym + 5)], color=color, lw=2.2)
        self.line([(x - 14, ym - 5), (x + 14, ym - 5)], color=color, lw=2.2)
        if label:
            self.text(x + (22 if right else -22), ym, label, ha="left" if right else "right", fs=fs)

    def cap_h(self, x0, x1, y, label=None, above=True, fs=11.5, color=INK):
        xm = (x0 + x1) / 2
        self.line([(x0, y), (xm - 5, y)], color=color)
        self.line([(xm + 5, y), (x1, y)], color=color)
        self.line([(xm - 5, y - 14), (xm - 5, y + 14)], color=color, lw=2.2)
        self.line([(xm + 5, y - 14), (xm + 5, y + 14)], color=color, lw=2.2)
        if label:
            self.text(xm, y + (28 if above else -28), label, ha="center", fs=fs)

    def plane(self, x, y0, y1, label="Interface plane", at=None, ha="center"):
        self.line([(x, y0), (x, y1)], color=PLANE, lw=2.0, dash=(7, 5), z=7)
        lx, ly = at if at else (x, y1 + 16)
        self.text(lx, ly, label, ha=ha, fs=12.5, weight="semibold", color=PLANE)

    # -- checks -------------------------------------------------------------
    def check(self) -> list[str]:
        self.fig.canvas.draw()
        renderer = self.fig.canvas.get_renderer()
        errs: list[str] = []
        boxes = []
        for t, owner in self.texts:
            bb = t.get_window_extent(renderer)
            rect = (bb.x0, bb.y0, bb.x1, bb.y1)
            label = t.get_text().replace("\n", " / ")[:60]
            if rect[0] < 2 or rect[1] < 2 or rect[2] > self.w - 2 or rect[3] > self.h - 2:
                errs.append(f"{self.name}: text outside the image: {label!r}")
            boxes.append((rect, owner, label))
        for i in range(len(boxes)):
            for j in range(i + 1, len(boxes)):
                a, b = boxes[i][0], boxes[j][0]
                if a[0] < b[2] - 1 and b[0] < a[2] - 1 and a[1] < b[3] - 1 and b[1] < a[3] - 1:
                    errs.append(f"{self.name}: texts overlap: {boxes[i][2]!r} and {boxes[j][2]!r}")
        for rect, owner, label in boxes:
            for name, (x0, y0, x1, y1) in self.boxes.items():
                if name == owner:
                    continue
                if rect[0] < x1 - 1 and x0 < rect[2] - 1 and rect[1] < y1 - 1 and y0 < rect[3] - 1:
                    errs.append(f"{self.name}: text {label!r} overlaps box {name}")
        return errs

    def png(self) -> bytes:
        buf = io.BytesIO()
        self.fig.savefig(buf, format="png", dpi=100, facecolor="white", metadata={"Software": None})
        plt.close(self.fig)
        return buf.getvalue()


# ---------------------------------------------------------------------------
# ICD-CTL-KEY
# ---------------------------------------------------------------------------

def trs_plug(c: Canvas, x, y, mono=False, k=1.0, left=False):
    """3.5 mm plug drawn horizontally; handle at the left and tip at the right,
    or mirrored (tip pointing left) with left=True. x is the handle's outer end.
    Returns the x of the tip segment start (the tip insulator edge)."""
    sgn = -1 if left else 1

    def X(u):
        return x + sgn * u * k

    def R(u0, u1, yy0, hh, fill, edge, z):
        a, b = sorted((X(u0), X(u1)))
        c.rect(a, yy0, b - a, hh, fill=fill, edge=edge, z=z)

    R(0, 110, y - 22 * k, 44 * k, "#3b3a36", "#1b1b19", 4)
    R(110, 260 if mono else 228, y - 12 * k, 24 * k, METAL, METAL_DARK, 4)
    if not mono:
        R(228, 234, y - 12 * k, 24 * k, "#1b1b19", "#1b1b19", 5)
        R(234, 290, y - 12 * k, 24 * k, METAL, METAL_DARK, 4)
        R(290, 296, y - 12 * k, 24 * k, "#1b1b19", "#1b1b19", 5)
        t0 = 296
    else:
        R(260, 266, y - 12 * k, 24 * k, "#1b1b19", "#1b1b19", 5)
        t0 = 266
    c.poly([(X(t0), y - 12 * k), (X(t0 + 44), y - 12 * k), (X(t0 + 60), y), (X(t0 + 44), y + 12 * k), (X(t0), y + 12 * k)], fill=METAL, edge=METAL_DARK, z=4)
    return X(t0)


def fig_key(family) -> Canvas:
    c = Canvas("ICD-CTL-KEY", family)
    c.header("ICD-CTL-KEY: key and paddle jack to the controller key inputs (SRR stub, Preliminary)",
             "Jack J1 pin-out, plugs accepted and the per-line input network of section 3.2.5; the ring line repeats the tip network.")
    # External side
    c.panel(20, 60, 520, 830, "External side: KEY (SI-018, SI-034, CON-012)", fill=EXT_FILL)
    c.text(40, 818, "TRS plug: paddle, bug or TRS-wired straight key", fs=13, weight="semibold")
    tip0 = trs_plug(c, 60, 730)
    c.text(115, 682, "Handle", ha="center", fs=11.5, color=INK_2)
    c.text(230, 682, "Sleeve: common", ha="center", fs=12)
    c.text(322, 774, "Ring: dah", ha="center", fs=12)
    c.line([(322, 762), (322, 744)], color=INK_2, lw=1.0)
    c.text(tip0 + 30, 682, "Tip: dit or\nstraight key", ha="center", fs=12)
    c.text(40, 600, "TS mono plug: straight key", fs=13, weight="semibold")
    trs_plug(c, 60, 545, mono=True)
    c.text(40, 480, "The sleeve spans the ring spring, so the ring reads\nclosed permanently (OPS-013): the interlock refuses\ntransmit until the operator selects Straight-on-tip.", fs=12, va="center")
    c.text(40, 390, "Keying device on each line", fs=13, weight="semibold")
    c.text(40, 330, "Passive contact, or an open-collector or MOSFET\noutput switching the line to the sleeve.\nClosed: at most 500 ohm (about 0.15 V at 0.3 mA).\nOpen: at least 100 kohm. Sinks up to 0.30 mA.", fs=12)
    c.text(40, 200, "Headphones in this jack read as a closed key\nand are refused by the interlock (0.30 mA, harmless).", fs=12)
    # Plane and jack
    c.plane(570, 90, 855, "Interface plane: J1 panel face")
    jx0, jx1 = 585, 745
    c.box(jx0, 370, jx1 - jx0, 440, None, fill="white", edge=NAVY, name="J1")
    c.text((jx0 + jx1) / 2, 788, "J1", ha="center", fs=15, weight="semibold", color=NAVY, owner="J1")
    c.text((jx0 + jx1) / 2, 752, "SJ1-3535N\nclass (TBR)", ha="center", fs=11.5, color=INK_2, owner="J1")
    pins = {"2 tip": 700, "3 ring": 590, "5 ring switch": 520, "4 tip switch": 460, "1 sleeve": 400}
    for lab, py in pins.items():
        c.text(jx0 + 12, py, lab, ha="left", fs=12, owner="J1")
        c.line([(jx1, py), (jx1 + 25, py)])
    # Right side panel
    c.panel(760, 60, 820, 830, "Side A: CTL (key inputs B13, Pico 2 B12); network values TBR (ADR-009)")
    y = 700
    c.text(785, 842, "Tip line KEY_TIP (J1-2)", fs=12.5, weight="semibold", color=NAVY)
    c.line([(jx1 + 25, y), (790, y)])
    c.dot(790, y)
    c.cap_v(790, y, 652)
    c.ground(790, 652)
    c.text(760, 764, "C1 100 pF C0G\n(optional)", ha="left", fs=11)
    c.line([(790, 744), (790, 706)], color=INK_2, lw=0.8)
    c.line([(790, y), (880, y)])
    c.dot(880, y)
    c.line([(880, y), (880, 690)])
    c.box(858, 652, 44, 38, "D1", fs=11, name="D1")
    c.ground(880, 652)
    c.text(880, 812, "D1 TPD2E2U06\nlevel 4 clamp", ha="center", fs=11)
    c.line([(880, 792), (880, 706)], color=INK_2, lw=0.8)
    c.resistor_h(880, 1010, y, "R1 1.0 kohm")
    c.dot(1010, y)
    c.resistor_v(1010, y, 800, "R2 10 kohm")
    c.rail(1010, 800, "3V3")
    c.line([(1010, y), (1100, y)])
    c.dot(1100, y)
    c.cap_v(1100, y, 652, "C2 4.7 nF")
    c.ground(1100, 652)
    c.line([(1100, y), (1215, y)])
    c.dot(1215, y)
    c.line([(1215, y), (1215, 735)])
    c.box(1193, 735, 44, 38, "D2", fs=11, name="D2")
    c.line([(1215, 773), (1215, 785)])
    c.rail(1215, 785, "3V3")
    c.text(1250, 812, "D2 BAT54S to\n3V3 and GND", ha="left", fs=11)
    c.line([(1215, y), (1330, y)])
    c.box(1330, 575, 230, 185, "RP2350 pads KEY_TIP and\nKEY_RING, read active low:\nIE 1, SCHMITT 1, OD 1,\nPUE 0, PDE 0, ISO 0", fs=11.5, name="pad")
    c.arrow((1445, 575), (1445, 542), color=CONTROL)
    c.box(1330, 470, 230, 72, "SW-KEYER: sampled 1 ms,\nmake 2 ms, break 5 ms (TBR)", fs=11.5, name="keyer")
    # ring line
    c.line([(jx1 + 25, 590), (800, 590)])
    c.box(800, 568, 470, 44, "KEY_RING (J1-3): same network as KEY_TIP; one D1 covers both", fs=11.5, name="ring", fill=GROUP_FILL, edge=INK_2)
    c.arrow((1270, 590), (1330, 590))
    # plug detect
    c.line([(jx1 + 25, 520), (775, 520), (775, 430), (1330, 430)], color=CONTROL)
    c.box(1330, 395, 230, 70, "KEY_DET GPIO, 100 kohm\npull-down (TBR)", fs=11.5, name="det")
    c.text(1050, 450, "no plug: shunt ties J1-5 to the ring (reads high); plug in: low", ha="center", fs=11, color=INK_2)
    # sleeve
    c.line([(jx1 + 25, 400), (765, 400), (765, 385)])
    c.ground(765, 385)
    c.text(790, 368, "Sleeve bonded to signal ground at the jack; J1-4 not connected", fs=11, color=INK_2)
    # numbers
    c.box(780, 80, 780, 250, None, fill="white", edge=GROUP_EDGE, name="numbers")
    lines = [
        "Closed at 500 ohm or less: pad below 0.6 V against VIL 0.8 V (erratum E9 leakage included).",
        "Open at 100 kohm or more: pad at least 2.0 V (VIH); open line at 3.29 V.",
        "Bias at most 0.30 mA per line (contact shorted; pad 0.33 V at 100 ohm); RC 47 us release, 5.2 us closure.",
        "Abuse -5 V to +12 V DC, 10 min, 50 mA source limit (TBR); ESD IEC 61000-4-2 level 4.",
        "Interlock: each used input open 500 ms (TBR) before transmit arms.",
        "No key-line gesture is a command (CS-30); stuck closure ends at 5 s (TBR), hardware at 7.5 to 13 s (TBR).",
        "Lead pair: common-mode suppression at least 500 ohm at 146 MHz (TBR).",
    ]
    for i, s in enumerate(lines):
        c.text(795, 305 - 32 * i, s, fs=11.5, owner="numbers")
    return c


def fig_phones(family) -> Canvas:
    c = Canvas("ICD-CTL-PHONES", family)
    c.header("ICD-CTL-PHONES: headphone jack and audio output limits (SRR stub, Preliminary)",
             "Mono audio on tip and ring, bounded by a fixed passive ceiling and fixed gain ahead of the jack, independent of firmware.")
    c.panel(20, 60, 1030, 830, "Side A: CTL (audio B15, Pico 2 B12)")
    y = 720
    c.box(40, 668, 210, 104, "RP2350 PWM audio\n73 to 146 kHz, 10 to 11 bit;\nlimiter, cap and fades\nin firmware", fs=11.5, name="pwm")
    c.resistor_h(250, 360, y, "R1 10 kohm")
    c.dot(360, y)
    c.resistor_v(360, y, 630, None)
    c.text(345, 675, "R2\n953 ohm", ha="right", fs=11)
    c.ground(360, 630)
    c.line([(360, y), (430, y)])
    c.dot(430, y)
    c.cap_v(430, y, 630, "C1\n56 nF")
    c.ground(430, 630)
    c.resistor_h(430, 545, y, "R3 1 kohm")
    c.dot(545, y)
    c.cap_v(545, y, 630, "C2\n47 nF")
    c.ground(545, 630)
    c.cap_h(545, 650, y, "input coupling")
    c.line([(650, y), (700, y)])
    c.box(700, 600, 200, 180, "TPA6132A2 class\n0 dB gain, 3.3 V\ncharge pump,\nshort-circuit protected;\n80 dB off-isolation", fs=11.5, name="amp")
    c.text(390, 790, "Ceiling network: k = 0.0870 (-21.2 dB); poles 3.27 and 3.39 kHz", fs=11.5, color=INK_2)
    # outputs
    jx0, jx1 = 1085, 1245
    c.line([(900, 720), (jx0 - 25, 720)])
    c.line([(900, 640), (jx0 - 25, 640)])
    c.text(990, 736, "PHONES_L", ha="center", fs=11.5, color=NAVY)
    c.text(990, 656, "PHONES_R", ha="center", fs=11.5, color=NAVY)
    c.text(990, 690, "same mono signal", ha="center", fs=11, color=INK_2)
    # enable and detect
    c.box(700, 440, 200, 74, "PHONES_EN GPIO,\nhardware pull-down", fs=11.5, name="en")
    c.arrow((800, 514), (800, 598), color=CONTROL)
    c.box(400, 470, 260, 74, "PHONES_DET GPIO, Schmitt;\ncontact J2-4 or J2-5 (TBR)", fs=11.5, name="det")
    c.line([(jx0 - 25, 560), (530, 560), (530, 544)], color=CONTROL)
    c.line([(jx0 - 25, 500), (1045, 500), (1045, 560)], color=CONTROL, dash=(5, 4))
    c.text(930, 578, "detect (tip switch per HZ-005 K6)", ha="center", fs=11, color=INK_2)
    c.text(40, 405, "Firmware at the plane: detect debounced 50 ms; amplifier enabled only with a plug and after the source\nidles 20 ms at mid-scale; output ramps from zero over 100 ms; amplifier off with no plug (REQ-SYS-077).", fs=11.5)
    # sleeve
    c.line([(jx0 - 25, 430), (1035, 430), (1035, 422)])
    c.ground(1035, 422)
    c.text(1020, 452, "AGND", ha="right", fs=11)
    # plane and jack
    c.plane(1070, 90, 855, "Interface plane: J2 panel face")
    c.box(jx0, 380, jx1 - jx0, 440, None, name="J2")
    c.text((jx0 + jx1) / 2, 798, "J2", ha="center", fs=15, weight="semibold", color=NAVY, owner="J2")
    c.text((jx0 + jx1) / 2, 764, "SJ1-3535N\nclass (TBR)", ha="center", fs=11.5, color=INK_2, owner="J2")
    for lab, py in {"2 tip (L)": 720, "3 ring (R)": 640, "4 tip switch": 560, "5 ring switch": 500, "1 sleeve": 430}.items():
        c.text(jx1 - 12, py, lab, ha="right", fs=12, owner="J2")
        c.line([(jx0 - 25, py), (jx0, py)])
    # external
    c.panel(1260, 60, 320, 830, "External: PHONES (CON-013)", fill=EXT_FILL)
    c.text(1275, 818, "Headphones or earbuds,\n16 to 64 ohm", fs=13, weight="semibold", va="top")
    t = trs_plug(c, 1560, 700, k=0.72, left=True)
    c.text(1310, 648, "Tip: left", ha="center", fs=11.5)
    c.text(1375, 752, "Ring: right", ha="center", fs=11.5)
    c.line([(1375, 740), (1375, 712)], color=INK_2, lw=1.0)
    c.text(1450, 648, "Sleeve: ground", ha="center", fs=11.5)
    trs_plug(c, 1560, 560, k=0.72, left=True, mono=True)
    c.text(1275, 490, "TS mono plug: the ring\nchannel is shorted to the\nsleeve; tolerated without\ndamage (REQ-SYS-079).", fs=11.5, va="center")
    c.text(1275, 370, "A key plugged in here by\nmistake is an output short\nthe amplifier survives\n(RSK-039).", fs=11.5, va="center")
    # limits
    c.box(40, 80, 990, 290, None, fill="white", edge=GROUP_EDGE, name="limits")
    c.text(55, 348, "Limits at the jack into 32 ohm (section 3.2.7.2)", fs=12.5, weight="semibold", owner="limits")
    lines = [
        "Hardware ceiling, independent of firmware: 100 mVrms +/-10 percent (TBR) for a full-scale 700 Hz sine.",
        "Any digital pattern: at most 150 mVrms (TBR); after any single component failure: at most 150 mVrms (TBR).",
        "Default firmware cap 30 mVrms (TBR) until the operator acknowledges; transients below 10 mV peak (TBR).",
        "Load 16 to 64 ohm; channels within 1 dB (TBR); survives an indefinite short of tip or ring to the sleeve.",
        "Derived SPL at 100 mVrms: 96.5 dB for EN 50332-2 boundary headphones, 101.6 dB for the most sensitive earbuds.",
        "ESD IEC 61000-4-2 level 4 at the jack; common-mode suppression at least 500 ohm at 146 MHz (TBR).",
    ]
    for i, s_ in enumerate(lines):
        c.text(55, 312 - 36 * i, s_, fs=11.5, owner="limits")
    return c


def fig_ant(family) -> Canvas:
    c = Canvas("ICD-TX-ANT", family)
    c.header("ICD-TX-ANT: SMA antenna port, electrical and mechanical load path (SRR stub, Preliminary)",
             "Schematic section through the end wall: the enclosure boss, not the PCB, carries the antenna moment; geometry is fixed in the enclosure model at PDR.")
    c.panel(20, 60, 780, 830, "Side A: TX (B01 to B04) inside the enclosure")
    c.panel(870, 60, 710, 830, "External: ANT (SI-008; SMA-plug antennas, F7)", fill=EXT_FILL)
    ya = 600
    # wall and boss
    c.rect(805, 330, 25, 520, fill=METAL, edge=METAL_DARK, z=2, hatch="//")
    c.rect(770, ya - 70, 60, 140, fill=METAL, edge=METAL_DARK, z=2, hatch="//")
    # jack body through the boss
    c.rect(700, ya - 15, 215, 30, fill="#e4e3de", edge=METAL_DARK, z=4, hatch="|||")
    c.rect(732, ya - 42, 38, 84, fill="#d6d5cf", edge=METAL_DARK, z=5)
    # lug and nut
    c.rect(830, ya - 44, 8, 88, fill="#b87333", edge="#7a4a1f", z=5)
    c.rect(830, ya - 110, 8, 70, fill="#b87333", edge="#7a4a1f", z=5)
    c.rect(838, ya - 32, 22, 64, fill="#a9a8a2", edge=METAL_DARK, z=5)
    # counterpoise wire
    c.line([(834, ya - 110), (834, ya - 150), (900, ya - 200), (1060, ya - 250)], color="#b87333", lw=2.2, z=4)
    c.text(1070, ya - 250, "48 cm counterpoise wire", ha="left", fs=11.5)
    # antenna plug and whip
    c.rect(915, ya - 26, 58, 52, fill="#a9a8a2", edge=METAL_DARK, z=5)
    c.rect(973, ya - 16, 52, 32, fill="#3b3a36", edge="#1b1b19", z=5)
    c.line([(1025, ya), (1450, ya)], color="#3b3a36", lw=4.5, z=4)
    c.text(944, ya + 44, "SMA plug\n(male pin)", ha="center", fs=11)
    c.arrow((1440, ya + 90), (1440, ya + 8), color=POWER, lw=2.2, head=13)
    c.text(1440, ya + 110, "10 N side load", ha="center", fs=12, weight="semibold", color=POWER)
    c.arrow((830, ya - 60), (1440, ya - 60), color=INK_2, lw=1.0, both=True)
    c.text(1135, ya - 42, "0.40 m: 4.0 N m about the port, any direction", ha="center", fs=12)
    # plane
    c.plane(830, 90, 840, "Interface plane: outer surface of the end wall", at=(845, 828), ha="left")
    # annotations with leaders
    c.text(245, 770, "SMA jack, female body, stainless,\n1/4-36 UNS-2A, 500 mating cycles", ha="left", fs=11.5)
    c.line([(505, 770), (722, ya + 17)], color=INK_2, lw=0.9)
    c.text(590, 832, "Boss wall at least 2.5 mm; hole 6.55 +0.05/-0.00 mm;\nanti-rotation flat (TBR)", ha="center", fs=11.5)
    c.line([(690, 810), (792, ya + 72)], color=INK_2, lw=0.9)
    c.text(1010, 745, "7.9 mm hex nut; antenna plug\nfinger-tight, 0.45 to 0.56 N m (TBR),\nnever a wrench", ha="left", fs=11.5)
    c.line([(1005, 745), (855, ya + 34)], color=INK_2, lw=0.9)
    c.text(1070, ya - 150, "Counterpoise lug under the nut: within 20 mm (TBR),\nat most 10 mohm to the jack shell (TBR)", ha="left", fs=11.5)
    c.line([(1066, ya - 150), (840, ya - 100)], color=INK_2, lw=0.9)
    # inside: PCB, blocks, pigtail
    c.rect(50, 392, 690, 16, fill="#3d6b4f", edge="#27452f", z=3)
    c.text(60, 372, "Main PCB", fs=11, color=INK_2)
    c.box(50, 420, 170, 70, "PA and driver\n(B04)", fs=11.5, name="pa")
    c.box(250, 420, 170, 70, "T/R relay (B03),\nunpowered: RX", fs=11.5, name="tr")
    c.box(450, 420, 150, 70, "Harmonic LPF\n(B02)", fs=11.5, name="lpf")
    c.box(625, 420, 90, 70, "board RF\nconnector", fs=11, name="conn")
    c.arrow((220, 455), (250, 455))
    c.arrow((420, 455), (450, 455))
    c.arrow((600, 455), (625, 455))
    c.box(250, 540, 170, 60, "RX front end\n(B08), LNA off in TX", fs=11, name="rx")
    c.arrow((335, 490), (335, 540))
    pts = []
    for i in range(21):
        t_ = i / 20
        p0, p1, p2 = (715, 455), (790, 470), (700, ya)
        pts.append(((1 - t_) ** 2 * p0[0] + 2 * (1 - t_) * t_ * p1[0] + t_ ** 2 * p2[0], (1 - t_) ** 2 * p0[1] + 2 * (1 - t_) * t_ * p1[1] + t_ ** 2 * p2[1]))
    c.line(pts, color=INK, lw=2.6, z=4)
    c.text(245, 680, "Compliant PCB connection: RG-316 pigtail, or a\nPCB-mount bulkhead jack with a tolerance stack (TBR).\nThe PCB carries no antenna moment.", ha="left", fs=11.5)
    # bottom boxes
    c.box(40, 80, 740, 250, None, fill="white", edge=GROUP_EDGE, name="mech")
    c.text(55, 305, "Mechanical (sections 3.2.1, 3.2.2, 3.2.7.3)", fs=12.5, weight="semibold", owner="mech")
    for i, s_ in enumerate([
        "4.0 N m in any direction: no jack rotation, return-loss change within 1 dB (TBR).",
        "500 mating cycles: return loss within 1 dB (TBR) of its initial value.",
        "Reference whips 18 g (0.48 m) to 85 g (1.02 m): gravity moments 0.042 to 0.43 N m.",
        "Port on one end face (REQ-SYS-175); counterpoise attachment bonded to the shell.",
        "Stainless neck yield above 4.0 N m (TBR); brass neck, context: 2.4 to 3.6 N m.",
    ]):
        c.text(55, 272 - 34 * i, s_, fs=11.5, owner="mech")
    c.box(890, 80, 670, 250, None, fill="white", edge=GROUP_EDGE, name="elec")
    c.text(905, 305, "Electrical at the port (sections 3.2.4, 3.2.7.1)", fs=12.5, weight="semibold", owner="elec")
    for i, s_ in enumerate([
        "50 ohm; carrier 144.001 to 147.999 MHz (TBR); emission A1A only.",
        "5 W step +/-1 dB (TBR); at least 4.0 W into SWR 2:1 (TBR).",
        "Survives 60 s of 5 W keying at 80 percent duty into SWR 10:1, open, short.",
        "Spurious at most 25 uW (47 CFR 97.307(e)); design target 60 dBc (TBR).",
        "Peak 25.1 V at 5 W + 1 dB, 45.6 V into SWR 10:1; SMA rated 500 V peak.",
        "Receive: survives +27 dBm (TBR); port emissions at most -57 dBm (TBR).",
    ]):
        c.text(905, 272 - 34 * i, s_, fs=11.5, owner="elec")
    return c


def fig_usb(family) -> Canvas:
    c = Canvas("ICD-CTL-USB", family, height=1080)
    c.header("ICD-CTL-USB: Pico 2 micro-USB for firmware loading and charge input (SRR stub, Preliminary)",
             "Top: what crosses the connector plane and where VBUS goes inside the radio. Bottom: the wall opening, to scale.")
    # ---- top schematic
    c.panel(20, 470, 380, 520, "External: USB host or charger", fill=EXT_FILL)
    c.panel(440, 470, 1140, 520, "Side A: CTL (Pico 2 module B12, USB take-off B16); PWR cites for charge power")
    c.box(40, 600, 200, 300, "USB host computer\nor 5 V charger\n(any USB 2.0 port\nor adapter; SI-022,\nCON-010)", fs=12, name="host")
    rows = {"VBUS": 880, "D+": 730, "D-": 700, "GND": 620}
    for k_, yy in rows.items():
        c.line([(240, yy), (400, yy)], color=POWER if k_ == "VBUS" else (CONTROL if k_.startswith("D") else INK), lw=1.8 if k_ == "VBUS" else 1.4)
    c.text(320, 896, "VBUS 5 V", ha="center", fs=11.5, color=POWER)
    c.text(320, 746, "D+, D-", ha="center", fs=11.5, color=CONTROL)
    c.text(320, 636, "GND", ha="center", fs=11.5)
    c.plane(420, 480, 955, "Interface plane: receptacle mouth", at=(392, 505), ha="right")
    c.box(400, 580, 44, 340, None, fill=METAL, edge=METAL_DARK, name="recept")
    c.text(470, 560, "micro-B receptacle on the module", ha="left", fs=11.5, color=INK_2)
    c.panel(480, 590, 580, 355, None, fill="white", edge=NAVY)
    c.text(500, 928, "Pico 2 module (SC1631)", fs=12.5, weight="semibold", color=NAVY)
    # VBUS row
    c.line([(444, 880), (1100, 880)], color=POWER, lw=1.8)
    c.text(700, 864, "1 VBUS to castellation pin 40, 500 mA total", ha="left", fs=11.5, color=POWER)
    c.dot(560, 880, color=POWER)
    c.line([(560, 880), (560, 846)], color=POWER)
    c.box(538, 812, 44, 34, "D1", fs=11, name="d1")
    c.line([(560, 812), (560, 790)], color=POWER)
    c.line([(560, 790), (1080, 790)], color=POWER, lw=1.4)
    c.text(600, 806, "VSYS: the controller runs from USB, switch on or off", ha="left", fs=11.5)
    c.dot(1000, 880, color=POWER)
    c.line([(1000, 880), (1000, 772)], color=POWER)
    c.box(880, 700, 165, 72, "GPIO24 VBUS\nsense: firmware\nTX inhibit", fs=11, name="gpio24")
    # data rows
    c.line([(444, 730), (560, 730)], color=CONTROL)
    c.line([(444, 700), (560, 700)], color=CONTROL)
    c.text(452, 745, "3 D+", ha="left", fs=11)
    c.text(452, 684, "2 D-", ha="left", fs=11)
    c.box(560, 650, 300, 120, "RP2350 USB (27 ohm series)\nbootloader: UF2 target, picotool\napplication: USB serial banner,\nrestart-to-bootloader command", fs=11.5, name="rpusb")
    # GND
    c.line([(444, 620), (1100, 620), (1100, 612)])
    c.ground(1100, 612)
    c.text(452, 636, "5 GND (4 ID not used)", ha="left", fs=11)
    # right-hand boxes
    c.box(1130, 850, 435, 90, "BQ25887 charger (PWR): operates 3.9 to 6.2 V,\nover-voltage 6.2 to 6.6 V; input limit about 450 mA\n(TBR); charge paused with the switch on", fs=11.5, name="chg")
    c.line([(1100, 880), (1130, 880)], color=POWER, lw=1.8)
    c.dot(1100, 880, color=POWER)
    c.line([(1100, 880), (1110, 880), (1110, 770), (1130, 770)], color=POWER)
    c.box(1130, 730, 435, 80, "Own VBUS divider: hardware TX inhibit, PA-path\nenable forced low (REQ-SYS-092); no TX supply\nfrom USB alone (REQ-SYS-149)", fs=11.5, name="hwinh")
    c.line([(1080, 790), (1090, 790), (1090, 680), (1130, 680)], color=POWER)
    c.box(1130, 640, 435, 75, "5 V bus to VSYS through a VBUS-gated P-FET OR,\nso the two sources never back-feed", fs=11.5, name="or")
    c.text(1135, 560, "Host protocol, UF2 format, serial trace: ICD-SW-HOST (PDR).", fs=11.5, color=INK_2)
    c.text(1135, 530, "Firmware load works with the cells removed (REQ-SYS-133).", fs=11.5, color=INK_2)
    c.text(1135, 500, "RF stays off in the bootloader (REQ-SYS-119).", fs=11.5, color=INK_2)
    # ---- bottom left: section at the opening, 10 px per mm
    c.panel(20, 80, 760, 380, "Section at the opening, to scale (10 px per mm)")
    xw = 400
    c.rect(xw, 310, 25, 110, fill=METAL, edge=METAL_DARK, z=3, hatch="//")
    c.rect(xw, 100, 25, 110, fill=METAL, edge=METAL_DARK, z=3, hatch="//")
    c.poly([(xw, 310), (xw + 8, 310), (xw, 318)], fill="white", edge=METAL_DARK, z=4)
    c.poly([(xw, 210), (xw + 8, 210), (xw, 202)], fill="white", edge=METAL_DARK, z=4)
    c.line([(xw, 95), (xw, 425)], color=PLANE, lw=1.6, dash=(6, 4), z=6)
    c.rect(440, 221, 320, 16, fill="#3d6b4f", edge="#27452f", z=3)
    c.rect(418, 237, 342, 10, fill="#2d5a3c", edge="#1d3a27", z=3)
    c.rect(405, 247, 60, 26, fill="#d6d5cf", edge=METAL_DARK, z=4)
    c.rect(250, 217, 145, 86, fill="#3b3a36", edge="#1b1b19", z=4)
    c.rect(395, 251, 50, 18, fill="#e4e3de", edge=METAL_DARK, z=5)
    c.line([(60, 260), (250, 260)], color="#3b3a36", lw=6, z=3)
    c.text(322, 330, "Plug overmold at most\n10.6 x 8.5 mm", ha="center", fs=11)
    c.line([(225, 210), (398, 210)], color=INK_2, lw=0.8)
    c.line([(225, 310), (398, 310)], color=INK_2, lw=0.8)
    c.arrow((232, 214), (232, 306), color=INK_2, lw=1.0, head=8, both=True)
    c.text(226, 322, "opening 10.0 mm", ha="right", fs=11)
    c.text(495, 405, "Wall at most about 2.5 mm at the opening (TBR)", ha="left", fs=11)
    c.line([(492, 405), (425, 390)], color=INK_2, lw=0.8)
    c.text(495, 360, "Receptacle face 0 to 1.0 mm inside the outer surface", ha="left", fs=11)
    c.line([(492, 360), (407, 273)], color=INK_2, lw=0.8)
    c.text(495, 315, "Plug shell about 5 mm seats in the receptacle", ha="left", fs=11)
    c.line([(492, 315), (440, 269)], color=INK_2, lw=0.8)
    c.text(495, 180, "Pico 2 edge 1.3 mm behind the receptacle face", ha="left", fs=11)
    c.line([(492, 180), (420, 238)], color=INK_2, lw=0.8)
    c.text(495, 140, "Carrier PCB; opening centre about 2.3 mm above\nits top face (TBR)", ha="left", fs=11)
    c.line([(492, 150), (470, 222)], color=INK_2, lw=0.8)
    c.text(xw - 6, 112, "outer\nsurface", ha="right", fs=10.5, color=PLANE)
    # ---- bottom right: front view, 20 px per mm
    c.panel(800, 80, 780, 380, "Front view of the wall opening, to scale (20 px per mm)")
    cx, cy = 1000, 250
    c.ax.add_patch(FancyBboxPatch((cx - 130, cy - 110), 260, 220, boxstyle="round,pad=0,rounding_size=30", fc="#e9e8e3", ec=METAL_DARK, lw=1.0, zorder=3))
    c.ax.add_patch(FancyBboxPatch((cx - 120, cy - 100), 240, 200, boxstyle="round,pad=0,rounding_size=20", fc="white", ec=INK, lw=1.6, zorder=4))
    ov = FancyBboxPatch((cx - 106, cy - 85), 212, 170, boxstyle="round,pad=0,rounding_size=10", fc="none", ec=CONTROL, lw=1.4, zorder=5)
    ov.set_linestyle((0, (5, 4)))
    c.ax.add_patch(ov)
    # receptacle body about 8 mm wide (display-and-ui-parts.md F21, Pico 2 Figure 3 reading) and about
    # 2.6 mm high (twice the 1.3 mm half-height of F21, Low confidence), centred in the opening
    c.rect(cx - 80, cy - 26, 160, 52, fill="#d6d5cf", edge=METAL_DARK, z=5)
    c.arrow((cx - 120, cy - 128), (cx + 120, cy - 128), color=INK_2, lw=1.0, head=8, both=True)
    c.text(cx, cy - 144, "12.0 mm", ha="center", fs=11)
    c.arrow((cx + 148, cy - 100), (cx + 148, cy + 100), color=INK_2, lw=1.0, head=8, both=True)
    c.text(cx + 158, cy, "10.0 mm", ha="left", fs=11)
    for i, s_ in enumerate([
        "Opening 12.0 x 10.0 mm, R1 corners,",
        "45 degree chamfer on the outside",
        "Dashed: largest micro-B overmold",
        "10.6 x 8.5 mm (0.7 mm clearance)",
        "Receptacle: 10,000 insertion cycles;",
        "power contacts 1 and 5 rated 1.8 A",
        "Grey: receptacle about 8 x 2.6 mm",
        "(height Low confidence, F21)",
    ]):
        c.text(1245, 350 - 36 * i, s_, ha="left", fs=11.5)
    return c


def cell_in_holder(c: Canvas, x0, y0, plus_left: bool, label: str):
    """Keystone 1043P outline (77 x 20.65 mm) with an 18650 cell (65 x 18.5 mm), 8 px per mm."""
    k = 8.0
    hw, hh = 77 * k, 20.65 * k
    c.rect(x0, y0, hw, hh, fill="#2f2f2c", edge="#1b1b19", z=2)
    cw, ch = 65 * k, 18.5 * k
    cx0 = x0 + (hw - cw) / 2
    cy0 = y0 + (hh - ch) / 2
    c.ax.add_patch(FancyBboxPatch((cx0, cy0), cw, ch, boxstyle="round,pad=0,rounding_size=10", fc="#4f7cb3", ec="#23466f", lw=1.2, zorder=3))
    nub_x = cx0 - 8 if plus_left else cx0 + cw
    c.rect(nub_x, cy0 + ch / 2 - 22, 8, 44, fill=METAL, edge=METAL_DARK, z=3)
    # holder contacts
    c.rect(x0 + 4, y0 + hh / 2 - 34, 14, 68, fill=METAL, edge=METAL_DARK, z=4)
    c.rect(x0 + hw - 18, y0 + hh / 2 - 34, 14, 68, fill=METAL, edge=METAL_DARK, z=4)
    lp, rp = ("+", "-") if plus_left else ("-", "+")
    c.text(cx0 + 26, y0 + hh / 2, lp, ha="center", fs=22, weight="semibold", color="white", check=False)
    c.text(cx0 + cw - 26, y0 + hh / 2, rp, ha="center", fs=22, weight="semibold", color="white", check=False)
    c.text(x0 + hw / 2, y0 + hh / 2, label, ha="center", fs=12.5, color="white", weight="semibold")
    # plane: the cell terminals at the holder contacts
    pl = Rectangle((cx0 - 14, cy0 - 5), cw + 28, ch + 10, fc="none", ec=PLANE, lw=1.8, zorder=7)
    pl.set_linestyle((0, (7, 5)))
    c.ax.add_patch(pl)
    return (x0, x0 + hw, y0, y0 + hh)


def fig_cell(family) -> Canvas:
    c = Canvas("ICD-PWR-CELL", family)
    c.header("ICD-PWR-CELL: two 18650 cells in Keystone 1043P holders, protection thresholds (SRR stub, Preliminary)",
             "Top view of the holder pair to scale (8 px per mm) with the pack terminals and the layers that sense each cell; red dashed outline: the interface plane.")
    c.panel(20, 300, 790, 600, "External: CELL (SI-023, CON-011) in the holders")
    c.panel(830, 300, 750, 600, "Side A: PWR (charger B17, protection B18, holders B19)")
    h1 = cell_in_holder(c, 110, 640, plus_left=True, label="Cell 1 (top): 18650 Li-ion, unprotected")
    h2 = cell_in_holder(c, 110, 450, plus_left=False, label="Cell 2 (bottom): 18650 Li-ion, unprotected")
    # nets: BAT+ at holder 1 left, MID at the right between holder 1 (-) and holder 2 (+), BAT- at holder 2 left
    xb = [846, 856, 866]  # bus verticals: BAT+, MID, BAT-
    ym1 = 640 + 20.65 * 4
    ym2 = 450 + 20.65 * 4
    c.line([(110, ym1), (80, ym1), (80, 840), (1370, 840)], color=POWER, lw=3.0)
    c.text(95, 856, "BAT+ (holder 1 +)", ha="left", fs=11.5, color=POWER)
    c.line([(726, ym1), (746, ym1), (746, ym2), (726, ym2)], color=POWER, lw=3.0)
    c.dot(746, 627, color=POWER)
    c.line([(746, 627), (xb[1], 627)], color=CONTROL, lw=1.2)
    c.text(752, 610, "MID", ha="left", fs=11.5, color=CONTROL)
    c.line([(110, ym2), (80, ym2), (80, 420), (1370, 420)], color=POWER, lw=3.0)
    c.text(95, 404, "BAT- (holder 2 -), ahead of the protector FETs", ha="left", fs=11.5, color=POWER)
    # sense bus
    c.dot(xb[0], 840, color=CONTROL, r=3)
    c.dot(xb[2], 420, color=CONTROL, r=3)
    c.line([(xb[0], 840), (xb[0], 500)], color=CONTROL, lw=1.1)
    c.line([(xb[1], 627), (xb[1], 500)], color=CONTROL, lw=1.1)
    c.line([(xb[1], 627), (xb[1], 790)], color=CONTROL, lw=1.1)
    c.line([(xb[2], 420), (xb[2], 790)], color=CONTROL, lw=1.1)
    boxes = [
        (740, "Charger BQ25887 class: VBAT, MID through 300 ohm,\ncell ADC; balancing to 400 mA above 3.7 V"),
        (655, "Protector S-8252 class: OV 4.25 V, UV 2.50 V, over-current;\ndual N-FET in the pack negative"),
        (570, "Secondary over-voltage, BQ29209 class, 4.30 V (TBR),\nits own sense connections"),
        (485, "RP2350 ADC: pack / 3 reads 0 to 8.70 V, MID x 0.68 reads\n0 to 4.35 V (TBR); pin clamps; dual-path check"),
    ]
    for yb, lab in boxes:
        c.box(890, yb, 460, 64, lab, fs=11.5, name=f"layer{yb}")
        for i, xv in enumerate(xb):
            yy = yb + 20 + 12 * i
            c.line([(xv, yy), (890, yy)], color=CONTROL, lw=1.0)
    c.text(890, 462, "Each layer on its own Kelvin route from the holder tabs (TBR)", ha="left", fs=11.5, color=CONTROL)
    c.box(1370, 800, 195, 80, "Fuse or PTC, then P+\n6.0 to 8.4 V: PA rail,\nswitch, 5 V buck", fs=11.5, name="pplus")
    c.box(1370, 380, 195, 80, "Protector FETs to\nsystem GND; charger\nand protector always live", fs=11.5, name="gnd")
    # NTC
    c.rect(380, 640 + 20.65 * 8 - 22, 28, 12, fill="#1b1b19", edge="#1b1b19", z=6)
    c.line([(394, 640 + 20.65 * 8 - 10), (394, 862), (1120, 862), (1120, 804)], color=INK_2, lw=1.0, dash=(4, 3))
    c.text(420, 822, "NTC 103AT-2 on cell 1 (TBR): charger TS input and firmware", ha="left", fs=11)
    # holder info
    c.text(40, 360, "Keystone 1043P (TBR): 77 x 20.65 x 14.86 mm, pins 71.64 mm apart; owner hand-soldered.", fs=11.5)
    c.text(40, 332, "Accepts unprotected 18650 (reference INR18650-30Q, 64.85 +/-0.15 mm); 68 to 70 mm protected cells do not fit.", fs=11.5)
    # thresholds
    c.box(20, 60, 1560, 225, None, fill="white", edge=GROUP_EDGE, name="thr")
    c.text(35, 262, "Thresholds applied to each cell (section 3.2.4)", fs=12.5, weight="semibold", owner="thr")
    col1 = [
        "Pack 6.0 to 8.4 V (2 x 3.0 to 4.2 V), 7.2 V nominal; key-down 1.3 to 2.1 A (TBR) at 5 W.",
        "Charge CC-CV to 4.20 V +/-0.5 percent per cell (TBR); only 0 C to 45 C (TBR); 15 h timer (TBR).",
        "Over-voltage 4.25 to 4.30 V (TBR) at the protector; 4.30 V (TBR) at the secondary layer.",
        "Under-voltage 2.50 V +/-0.05 V (TBR) in hardware; firmware 3.20 V inhibit, 3.00 V power-down (TBR).",
    ]
    col2 = [
        "Discharge trip 3 A to 10 A (TBR); fuse or PTC carries the 2.1 A pulses.",
        "Charge refused: cells differ by more than 300 mV (TBR) or outside 2.5 to 4.3 V (TBR).",
        "Dual-path check 100 mV (TBR); a reversed cell: no damage, at most 10 mA (TBR).",
        "Pack current switched off at most 50 uA (TBR); cell over-temperature power-down 60 C (TBR).",
    ]
    for i, s_ in enumerate(col1):
        c.text(35, 222 - 40 * i, s_, fs=11.5, owner="thr")
    for i, s_ in enumerate(col2):
        c.text(830, 222 - 40 * i, s_, fs=11.5, owner="thr")
    return c


FIGURES = {
    "ICD-CTL-KEY": fig_key,
    "ICD-CTL-PHONES": fig_phones,
    "ICD-TX-ANT": fig_ant,
    "ICD-CTL-USB": fig_usb,
    "ICD-PWR-CELL": fig_cell,
}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true", help="check layout and compare with the PNGs on disk; write nothing")
    ap.add_argument("--only", choices=sorted(FIGURES), help="render one figure")
    ap.add_argument("--draft", type=Path, help="write the PNGs into this directory even when a layout check fails (for iteration)")
    args = ap.parse_args(argv)
    family = setup_fonts()
    names = [args.only] if args.only else list(FIGURES)
    failures: list[str] = []
    for name in names:
        c = FIGURES[name](family)
        errs = c.check()
        data = c.png()
        failures.extend(errs)
        out = HERE / f"{name}-plane.png"
        if args.draft:
            args.draft.mkdir(parents=True, exist_ok=True)
            (args.draft / out.name).write_bytes(data)
        if args.check:
            if not out.exists() or out.read_bytes() != data:
                failures.append(f"{name}: {out.name} differs from a fresh render")
        elif not errs and not args.draft:
            out.write_bytes(data)
            print(f"wrote {out.relative_to(REPO)}")
    for f in failures:
        print("FAIL", f, file=sys.stderr)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
