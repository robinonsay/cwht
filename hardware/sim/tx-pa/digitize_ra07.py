#!/usr/bin/env python3
"""Digitize the RA07M1317M typical-performance curves (datasheet, publication date Jun. 2019).

Input: the datasheet PDF (not committed; https://www.mitsubishielectric.com/semiconductors/hf/products/
datasheet/ra07m1317m.pdf, fetched 2026-09-28, SHA-256 recorded in the README). Pages 3 and 4 are rendered at
400 dpi with pdftoppm, the four plots used here are cropped, the grid lines are located automatically (rows
or columns more than 60 % dark), and the solid Pout curve is tracked column by column from a start point
with a slope predictor, ignoring pixels on grid lines. Output: a CSV per plot, and an overlay PNG of the
tracked points on the crop for visual closure (the curve is typical data, a graph read: estimate).

Usage: digitize_ra07.py PDF OUTDIR
"""
import csv
import subprocess
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage

# Crop boxes in 200-dpi display coordinates x 1.17 (as viewed), converted to 400 dpi below.
S = 400 / 200 * 1.17
PLOTS = {
    # name: (page, box, x axis (first, last, unit), y axis (top value, bottom value), start y value)
    "ra07_pout_vs_vdd_155": (4, (840, 410, 1320, 830), (2.0, 10.0), (20.0, 0.0), 0.67),
    "ra07_pout_vs_vdd_135": (4, (195, 410, 675, 830), (2.0, 10.0), (20.0, 0.0), 0.8),
    "ra07_pout_vs_pin_155": (3, (760, 890, 1210, 1290), (-10.0, 20.0), (45.0, 0.0), 26.6),
    "ra07_pout_vs_pin_135": (3, (180, 890, 620, 1290), (-10.0, 20.0), (45.0, 0.0), 26.5),
    "ra07_pout_vs_vgg_155": (5, (820, 410, 1274, 821), (1.5, 4.0), (12.0, 0.0), 0.15),
    "ra07_pout_vs_vgg_135": (5, (179, 410, 632, 821), (1.5, 4.0), (12.0, 0.0), 0.15),
}


def groups(idx):
    out = []
    for i in idx:
        if out and i - out[-1][-1] <= 2:
            out[-1].append(i)
        else:
            out.append([i])
    return [float(np.mean(g)) for g in out]


def track(a, rows, cols, y0_px, x_first, x_last):
    """Follow the thick solid curve from column x_first to x_last."""
    H, W = a.shape
    mask = a.copy()
    for r in rows:
        mask[max(0, int(r) - 3):int(r) + 4, :] = False
    for c in cols:
        mask[:, max(0, int(c) - 3):int(c) + 4] = False
    # Keep only long connected strokes: the solid curve survives, the dashes of the IDD and Gp curves
    # (each shorter than 30 px) and the text labels are removed, except where a dash touches the curve.
    lab, n = ndimage.label(mask, structure=np.ones((3, 3)))
    keep = np.zeros(n + 1, bool)
    for i, sl in enumerate(ndimage.find_objects(lab), start=1):
        if sl is not None and (sl[1].stop - sl[1].start) >= 30:
            keep[i] = True
    mask = keep[lab]
    pts = []
    y_prev, x_prev, slope = y0_px, int(x_first) + 4, 0.0
    for x in range(int(x_first) + 5, int(x_last) - 4):
        col = np.where(mask[:, x])[0]
        if col.size == 0:
            continue
        runs = []  # (top, bottom) of each dark run of 3 px or more
        for g in np.split(col, np.where(np.diff(col) > 1)[0] + 1):
            if g.size >= 3:
                runs.append((float(g[0]), float(g[-1])))
        if not runs:
            continue
        pred = y_prev + slope * (x - x_prev)
        def dist(r):
            return 0.0 if r[0] <= pred <= r[1] else min(abs(r[0] - pred), abs(r[1] - pred))
        top, bot = min(runs, key=dist)
        if dist((top, bot)) > 12:
            continue
        merged = (bot - top) > 9  # two curves overlap (a crossing): keep the heading
        y = min(max(pred, top + 3), bot - 3) if merged else 0.5 * (top + bot)
        y_prev, x_prev = y, x
        pts.append((x, y))
        if len(pts) >= 10 and not merged:
            # slope from a straight-line fit over the last 60 tracked columns (holds the heading
            # through a crossing with the dashed IDD or Gp curve)
            xs, ys = zip(*pts[-60:])
            slope = float(np.polyfit(xs, ys, 1)[0])
    return pts


def main():
    pdf, out = Path(sys.argv[1]), Path(sys.argv[2])
    out.mkdir(parents=True, exist_ok=True)
    for page in (3, 4, 5):
        subprocess.run(["pdftoppm", "-r", "400", "-f", str(page), "-l", str(page), "-png", str(pdf),
                        str(out / "page")], check=True)
    for name, (page, box, (x0v, x1v), (ytv, ybv), ystart) in PLOTS.items():
        img = Image.open(out / f"page-{page:02d}.png").convert("L")
        crop = img.crop(tuple(int(v * S) for v in box))
        a = np.array(crop) < 128
        H, W = a.shape
        rows = groups([y for y in range(H) if a[y].sum() > 0.6 * W])
        cols = groups([x for x in range(W) if a[:, x].sum() > 0.6 * H])
        ytop, ybot, xl, xr = rows[0], rows[-1], cols[0], cols[-1]
        def px2x(px):
            return x0v + (px - xl) / (xr - xl) * (x1v - x0v)
        def px2y(py):
            return ybv + (ybot - py) / (ybot - ytop) * (ytv - ybv)
        y0_px = ybot - (ystart - ybv) / (ytv - ybv) * (ybot - ytop)
        pts = track(a, rows, cols, y0_px, xl, xr)
        with open(out / f"{name}.csv", "w", newline="") as fh:
            w = csv.writer(fh)
            w.writerow(["x", "y"])
            for px, py in pts:
                w.writerow([f"{px2x(px):.4f}", f"{px2y(py):.4f}"])
        ov = crop.convert("RGB")
        d = ImageDraw.Draw(ov)
        for px, py in pts[::4]:
            d.ellipse((px - 3, py - 3, px + 3, py + 3), outline=(220, 0, 0), width=2)
        ov.save(out / f"{name}_overlay.png")
        print(name, len(pts), "points; x", round(px2x(pts[0][0]), 2), "to", round(px2x(pts[-1][0]), 2))
    for page in (3, 4, 5):
        (out / f"page-{page:02d}.png").unlink()


if __name__ == "__main__":
    main()
