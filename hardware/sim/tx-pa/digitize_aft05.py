#!/usr/bin/env python3
"""Digitize AFT05MS004N Figure 13 (Pout versus Pin, 136-174 MHz VHF broadband reference circuit,
VDD 7.5 V, IDQ 100 mA; datasheet Rev. 0, 7/2014).

Input: the datasheet PDF (not committed; https://www.nxp.com/docs/en/data-sheet/AFT05MS004N.pdf, fetched
2026-09-28, SHA-256 in the README). Page 11 is rendered at 400 dpi and Figure 13 is cropped. The Pout curves
are orange: for each column the orange pixel runs are found; the top run is the 155 MHz curve and the bottom
run the 135 MHz curve (the 175 MHz curve lies on or above the 135 MHz curve). Axis calibration is from the
figure's own grid (x: log, 0.01 W to 0.2 W grid lines at measured columns; y: 0 W and 8 W on the right-hand
Pout scale). Output: aft05_pout_vs_pin_135.csv and _155.csv (Pin in W, Pout in W) and an overlay PNG. The
result is a graph read of typical data: estimate.

Usage: digitize_aft05.py PDF OUTDIR
"""
import csv
import subprocess
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

S = 400 / 150
BOX = (400, 1060, 920, 1390)  # figure 13 in 150-dpi page coordinates


def main():
    pdf, out = Path(sys.argv[1]), Path(sys.argv[2])
    out.mkdir(parents=True, exist_ok=True)
    subprocess.run(["pdftoppm", "-r", "400", "-f", "11", "-l", "11", "-png", str(pdf), str(out / "page")],
                   check=True)
    img = Image.open(out / "page-11.png").convert("RGB")
    crop = img.crop(tuple(int(v * S) for v in BOX))
    a = np.array(crop).astype(int)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    orange = (r > 200) & (g > 110) & (g < 200) & (b < 90)
    dark = (r < 90) & (g < 90) & (b < 90)
    H, W = orange.shape
    # grid: black columns more than 50 % dark inside the plot are the vertical grid lines
    cols = [x for x in range(W) if dark[:, x].sum() > 0.5 * H]
    grp = []
    for x in cols:
        if grp and x - grp[-1][-1] <= 3:
            grp[-1].append(x)
        else:
            grp.append([x])
    vx = [float(np.mean(v)) for v in grp]
    # the vertical lines are 0.01 (left frame), 0.02 .. 0.09, 0.1, 0.2 and the right frame (0.3)
    # 0.01 and 0.1 are identified as the columns whose spacing ratio matches log10
    x001, x01 = vx[0], None
    for x in vx:
        if abs((x - x001) - (vx[1] - x001) / np.log10(2)) < 6:
            x01 = x
    if x01 is None:
        raise SystemExit(f"grid not identified: {vx}")
    dec = x01 - x001
    rows_dark = [y for y in range(H) if dark[y, int(W * 0.1):int(W * 0.85)].sum() > 0.5 * W * 0.75]
    rg = []
    for y in rows_dark:
        if rg and y - rg[-1][-1] <= 3:
            rg[-1].append(y)
        else:
            rg.append([y])
    hy = [float(np.mean(v)) for v in rg]
    y0, y8 = hy[-1], None  # bottom frame is Pout 0 W; the Pout 8 W level is the 17 dB gain line
    # Left scale 9 to 25 dB over 16 intervals equal to the right scale 0 to 80 % / 0 to 8 W;
    # Pout 8 W sits on the 17 dB line: 8 of 16 intervals above the bottom frame.
    ytop = hy[0]
    y8 = y0 - (y0 - ytop) * 8 / 16
    pts = {"135": [], "155": []}
    for x in range(int(x001) + 4, W - 4):
        ys = np.where(orange[:, x])[0]
        ys = ys[ys > ytop + 0.45 * (y0 - ytop)]  # Pout curves live in the lower half (the legend text is right of 0.2 W)
        if ys.size == 0:
            continue
        runs = np.split(ys, np.where(np.diff(ys) > 1)[0] + 1)
        runs = [q for q in runs if q.size >= 4]
        if not runs:
            continue
        pin = 10 ** (np.log10(0.01) + (x - x001) / dec)
        if pin > 0.205:
            continue
        top, bot = float(runs[0].mean()), float(runs[-1].mean())
        p_top = (y0 - top) / (y0 - y8) * 8.0
        p_bot = (y0 - bot) / (y0 - y8) * 8.0
        pts["155"].append((pin, p_top, x, top))
        pts["135"].append((pin, p_bot, x, bot))
    ov = crop.copy()
    d = ImageDraw.Draw(ov)
    for k, col in (("135", (0, 0, 255)), ("155", (200, 0, 200))):
        with open(out / f"aft05_pout_vs_pin_{k}.csv", "w", newline="") as fh:
            w = csv.writer(fh)
            w.writerow(["pin_w", "pout_w"])
            for pin, p, _, _ in pts[k]:
                w.writerow([f"{pin:.5f}", f"{p:.4f}"])
        for _, _, x, y in pts[k][::6]:
            d.ellipse((x - 3, y - 3, x + 3, y + 3), outline=col, width=2)
    ov.save(out / "aft05_pout_vs_pin_overlay.png")
    (out / "page-11.png").unlink()
    print("grid x", [round(v) for v in vx], "decade px", round(dec, 1), "y0", y0, "y8", round(y8, 1))
    for k in pts:
        arr = np.array([(p[0], p[1]) for p in pts[k]])
        print(k, [round(float(np.interp(v, arr[:, 0], arr[:, 1])), 2) for v in (0.03, 0.05, 0.07, 0.1, 0.15, 0.2)])


if __name__ == "__main__":
    main()
