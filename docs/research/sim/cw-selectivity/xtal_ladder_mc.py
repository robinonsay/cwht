#!/usr/bin/env python3
"""Tolerance (Monte Carlo) study of crystal ladder filters built from unmatched catalogue crystals.

Design method: Dishal / Zverev k-q synthesis as popularised for crystal ladders (Steder and Hardcastle,
QEX Nov/Dec 2009; Hayward, EMRFD ch. 3). Each crystal is a series resonator (Lm, Cm, Rs) with holder
capacitance C0; crystals sit in the series arms, coupling capacitors Ck in the shunt arms, and series
tuning capacitors equalise the mesh resonances. Lowpass prototype g-values are computed analytically
(Butterworth or Chebyshev), then

    k(i,i+1) = 1/sqrt(g_i g_(i+1))          normalised coupling
    q_1 = g_0 g_1, q_n = g_n g_(n+1)         normalised end Q
    Ck(i,i+1) = Cm f0 / (B k(i,i+1))         shunt coupling capacitor (k_actual = Cm/Ck)
    R_end = 2 pi Lm B / q_end - Rs           end termination (loaded Q_end = q_end f0/B)
    mesh tuning: S_i = sum(1/Ck) around mesh i; series C_t,i = 1/(S_max - S_i)

The generated LTspice deck uses .step param run 1 N and LTspice's flat()/gauss() random functions so
every run draws a fresh set of crystal parameters (frequency offset, Cm, Rs, C0) and capacitor/resistor
tolerances. The .raw is parsed with spicelib; per-run metrics are bandwidth at -3/-6/-60 dB, ripple,
insertion loss, centre-frequency error and shape factor. Results: JSON + CSV + PNG plots.

Headless only: LTspice 26.x CrossOver bundle is driven through its bundled wine, as proven in
docs/research/ltspice-batch-macos.md.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
import subprocess
import sys
import time
from dataclasses import dataclass, asdict
from pathlib import Path

import numpy as np

WINE = "/Applications/LTspice.app/Contents/SharedSupport/ltspice/bin/wine"
LTSPICE_EXE = r"C:\Program Files\ADI\LTspice\LTspice.exe"
NOISE = ("mvk-info", "VK_", "GPU", "Metal", "model:", "type:", "vendorID", "deviceID",
         "pipelineCache", "supports", "The following", "macOS GPU")


# ----------------------------------------------------------------------------------------------
# Lowpass prototype g-values (Matthaei/Young/Jones, Pozar 4th ed. section 8.3)
# ----------------------------------------------------------------------------------------------
def g_butterworth(n: int) -> list[float]:
    g = [1.0]
    for k in range(1, n + 1):
        g.append(2.0 * math.sin((2 * k - 1) * math.pi / (2 * n)))
    g.append(1.0)
    return g


def g_chebyshev(n: int, ripple_db: float) -> list[float]:
    beta = math.log(1.0 / math.tanh(ripple_db / 17.37))
    gamma = math.sinh(beta / (2 * n))
    a = [math.sin((2 * k - 1) * math.pi / (2 * n)) for k in range(1, n + 1)]
    b = [gamma ** 2 + math.sin(k * math.pi / n) ** 2 for k in range(1, n + 1)]
    g = [1.0, 2 * a[0] / gamma]
    for k in range(2, n + 1):
        g.append(4 * a[k - 2] * a[k - 1] / (b[k - 2] * g[k - 1]))
    g.append(1.0 if n % 2 == 1 else 1.0 / math.tanh(beta / 4) ** 2)
    return g


def kq_from_g(g: list[float]) -> tuple[list[float], float, float]:
    n = len(g) - 2
    k = [1.0 / math.sqrt(g[i] * g[i + 1]) for i in range(1, n)]
    q1 = g[0] * g[1]
    qn = g[n] * g[n + 1]
    return k, q1, qn


# ----------------------------------------------------------------------------------------------
# Ladder synthesis
# ----------------------------------------------------------------------------------------------
@dataclass
class Crystal:
    fs_hz: float      # series resonance
    cm_f: float       # motional capacitance (F)
    rs_ohm: float     # motional resistance
    c0_f: float       # holder (shunt) capacitance

    @property
    def lm_h(self) -> float:
        return 1.0 / ((2 * math.pi * self.fs_hz) ** 2 * self.cm_f)

    @property
    def qu(self) -> float:
        return 2 * math.pi * self.fs_hz * self.lm_h / self.rs_ohm


@dataclass
class Design:
    n: int
    bw_hz: float
    proto: str
    ripple_db: float
    k: list[float]
    q1: float
    qn: float
    ck_f: list[float]      # n-1 coupling capacitors
    ct_f: list[float]      # n series tuning capacitors (inf = none -> 0.0 means omitted)
    r1_ohm: float
    rn_ohm: float
    q_end_loaded: float
    qu: float
    f_mesh_hz: float       # common mesh resonance (design centre)


def synthesize(x: Crystal, n: int, bw_hz: float, proto: str, ripple_db: float) -> Design:
    g = g_butterworth(n) if proto == "butterworth" else g_chebyshev(n, ripple_db)
    k, q1, qn = kq_from_g(g)
    f0 = x.fs_hz
    ck = [x.cm_f * f0 / (bw_hz * ki) for ki in k]
    r1 = 2 * math.pi * x.lm_h * bw_hz / q1 - x.rs_ohm
    rn = 2 * math.pi * x.lm_h * bw_hz / qn - x.rs_ohm
    # mesh sums of 1/C for the coupling capacitors that belong to each mesh
    s = []
    for i in range(n):
        tot = 0.0
        if i > 0:
            tot += 1.0 / ck[i - 1]
        if i < n - 1:
            tot += 1.0 / ck[i]
        s.append(tot)
    smax = max(s)
    ct = []
    for si in s:
        d = smax - si
        ct.append(1.0 / d if d > 1e-3 * smax else 0.0)   # 0.0 = no tuning capacitor
    # common mesh resonance: fs * sqrt(1 + Cm * smax)
    f_mesh = f0 * math.sqrt(1.0 + x.cm_f * smax)
    return Design(n, bw_hz, proto, ripple_db, k, q1, qn, ck, ct, r1, rn,
                  q1 * f0 / bw_hz, x.qu, f_mesh)


# ----------------------------------------------------------------------------------------------
# LTspice deck generation
# ----------------------------------------------------------------------------------------------
@dataclass
class Spread:
    f_ppm: float          # half-width (uniform) or sigma (gauss) of crystal frequency error, ppm
    f_dist: str           # "flat" or "gauss"
    f_trunc_ppm: float    # truncation for gauss (0 = none)
    cm_pct_sigma: float   # gaussian sigma of Cm, percent
    cm_trunc_pct: float
    rs_min: float         # uniform Rs range, ohm
    rs_max: float
    c0_min_pf: float      # uniform C0 range
    c0_max_pf: float
    cap_pct: float        # uniform half-width of C tolerances, percent
    res_pct: float        # uniform half-width of R tolerances, percent


def fmt(v: float) -> str:
    return f"{v:.9g}"


def write_deck(path: Path, x: Crystal, d: Design, sp: Spread, runs: int, fspan_hz: float,
               points: int, seed: int | None = None, cm_actual_scale: float = 1.0) -> None:
    n = d.n
    L = []
    L.append(f"* {n}-pole crystal ladder, {d.proto} {d.ripple_db} dB, B={d.bw_hz} Hz, Monte Carlo {runs} runs")
    L.append(f"* nominal crystal fs={x.fs_hz} Hz Cm={x.cm_f*1e15:.3f} fF Rs={x.rs_ohm} ohm C0={x.c0_f*1e12:.2f} pF Lm={x.lm_h*1e3:.4f} mH Qu={x.qu:.0f}")
    L.append(f"* design k={[round(v,4) for v in d.k]} q1={d.q1:.4f} qn={d.qn:.4f} Qend_loaded={d.q_end_loaded:.0f} R1={d.r1_ohm:.2f} Rn={d.rn_ohm:.2f}")
    L.append(f"* Ck={[round(v*1e12,2) for v in d.ck_f]} pF  Ct={[round(v*1e12,2) if v else None for v in d.ct_f]} pF  f_mesh={d.f_mesh_hz:.1f} Hz")
    if seed is not None:
        L.append(f".options seed={seed}")
    L.append(f".param fs0={fmt(x.fs_hz)} cm0={fmt(x.cm_f * cm_actual_scale)} c00={fmt(x.c0_f)}")
    if cm_actual_scale != 1.0:
        L.append(f"* lot shift: simulated Cm = {cm_actual_scale} x design Cm")
    L.append(f".param tolf={fmt(sp.f_ppm*1e-6)} truncf={fmt(sp.f_trunc_ppm*1e-6)}")
    L.append(f".param cmsig={fmt(sp.cm_pct_sigma/100)} cmtr={fmt(sp.cm_trunc_pct/100)}")
    L.append(f".param rsmin={fmt(sp.rs_min)} rsmax={fmt(sp.rs_max)} c0min={fmt(sp.c0_min_pf*1e-12)} c0max={fmt(sp.c0_max_pf*1e-12)}")
    L.append(f".param captol={fmt(sp.cap_pct/100)} restol={fmt(sp.res_pct/100)}")
    for i in range(1, n + 1):
        if sp.f_dist == "flat":
            L.append(f".param ef{i}={{flat(tolf)}}")
        else:
            if sp.f_trunc_ppm > 0:
                L.append(f".param ef{i}={{limit(gauss(tolf),-truncf,truncf)}}")
            else:
                L.append(f".param ef{i}={{gauss(tolf)}}")
        L.append(f".param ec{i}={{limit(gauss(cmsig),-cmtr,cmtr)}}")
        L.append(f".param cm{i}={{cm0*(1+ec{i})}}")
        L.append(f".param fs{i}={{fs0*(1+ef{i})}}")
        L.append(f".param lm{i}={{1/(pow(2*pi*fs{i},2)*cm{i})}}")
        L.append(f".param rs{i}={{rsmin+(rsmax-rsmin)*(0.5+flat(0.5))}}")
        L.append(f".param c0_{i}={{c0min+(c0max-c0min)*(0.5+flat(0.5))}}")
    for j, ck in enumerate(d.ck_f, start=1):
        L.append(f".param ck{j}={{{fmt(ck)}*(1+flat(captol))}}")
    for i, ct in enumerate(d.ct_f, start=1):
        if ct:
            L.append(f".param ct{i}={{{fmt(ct)}*(1+flat(captol))}}")
    L.append(f".param r1={{{fmt(d.r1_ohm)}*(1+flat(restol))}} rn={{{fmt(d.rn_ohm)}*(1+flat(restol))}}")
    # topology: in --R1-- n1a --[Ct1]-- X1 -- n2 --Ck1-- gnd ... -- Xn --[Ctn]-- out --Rn-- gnd
    L.append("V1 in 0 AC 1")
    L.append("R1 in n1 {r1}")
    node = "n1"
    for i in range(1, n + 1):
        nxt = "out" if i == n else f"n{i+1}"
        a = node
        if d.ct_f[i - 1]:
            L.append(f"Ct{i} {a} t{i} {{ct{i}}}")
            a = f"t{i}"
        # crystal i between a and nxt: series Lm-Cm-Rs with parallel C0
        L.append(f"L{i} {a} m{i}a {{lm{i}}}")
        L.append(f"Cm{i} m{i}a m{i}b {{cm{i}}}")
        L.append(f"Rs{i} m{i}b {nxt} {{rs{i}}}")
        L.append(f"C0_{i} {a} {nxt} {{c0_{i}}}")
        if i < n:
            L.append(f"Ck{i} {nxt} 0 {{ck{i}}}")
        node = nxt
    L.append("Rn out 0 {rn}")
    f_lo = d.f_mesh_hz - fspan_hz
    f_hi = d.f_mesh_hz + fspan_hz
    L.append(f".ac lin {points} {fmt(f_lo)} {fmt(f_hi)}")
    L.append(f".step param run 1 {runs} 1")
    L.append(".save V(out) V(in)")
    L.append(".end")
    path.write_text("\n".join(L) + "\n")


# ----------------------------------------------------------------------------------------------
# LTspice run + parse
# ----------------------------------------------------------------------------------------------
def run_ltspice(deck: Path, timeout_s: float = 600) -> tuple[Path, Path, str]:
    cmd = [WINE, "--bottle=ltspice", "--wait-children", LTSPICE_EXE, "-b", str(deck.resolve())]
    t0 = time.time()
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout_s)
    except subprocess.TimeoutExpired:
        subprocess.run(["pkill", "-f", r"LTspice\\LTspice.exe"])
        raise RuntimeError(f"LTspice timed out after {timeout_s}s: {deck}")
    err = "\n".join(l for l in p.stderr.splitlines() if not any(s in l for s in NOISE))
    raw, log = deck.with_suffix(".raw"), deck.with_suffix(".log")
    if p.returncode != 0 or not raw.exists():
        raise RuntimeError(f"LTspice rc={p.returncode} in {time.time()-t0:.1f}s\n{err}\n"
                           f"{log.read_text(errors='replace') if log.exists() else ''}")
    ver = next((l for l in log.read_text(errors="replace").splitlines() if l.startswith("LTspice")), "?")
    return raw, log, ver


def _cross(f: np.ndarray, y: np.ndarray, level: float, i_pk: int) -> tuple[float, float]:
    """Return (f_lo, f_hi) where y crosses `level` (dB, negative relative to peak) on each side of i_pk."""
    lo = math.nan
    hi = math.nan
    for i in range(i_pk, 0, -1):
        if y[i - 1] < level <= y[i]:
            lo = f[i - 1] + (level - y[i - 1]) * (f[i] - f[i - 1]) / (y[i] - y[i - 1])
            break
    for i in range(i_pk, len(y) - 1):
        if y[i] >= level > y[i + 1]:
            hi = f[i] + (level - y[i]) * (f[i + 1] - f[i]) / (y[i + 1] - y[i])
            break
    return lo, hi


def metrics(f: np.ndarray, vout: np.ndarray, vin: np.ndarray, r1: float, rn: float,
            bw_nom: float, f_nom: float) -> dict:
    h = np.abs(vout) / np.abs(vin)
    # available-power referenced insertion loss (unequal terminations handled)
    pavail = 1.0 / (4 * r1)
    pout = h ** 2 / rn
    il_db = 10 * np.log10(pavail / pout)
    y = -il_db                                   # gain relative to lossless matched, dB (<= 0)
    i_pk = int(np.argmax(y))
    pk = y[i_pk]
    yr = y - pk
    lo3, hi3 = _cross(f, yr, -3.0, i_pk)
    lo6, hi6 = _cross(f, yr, -6.0, i_pk)
    lo60, hi60 = _cross(f, yr, -60.0, i_pk)
    bw3 = hi3 - lo3
    bw6 = hi6 - lo6
    bw60 = hi60 - lo60
    fc6 = 0.5 * (lo6 + hi6)
    # flatness: peak-to-peak variation inside the measured -3 dB band (reads up to 3 dB by construction;
    # it measures rounding from finite crystal Q as well as true ripple)
    m = (f > lo3) & (f < hi3)
    rip = float(yr[m].max() - yr[m].min()) if m.any() else math.nan
    # flatness inside the central 80 % of the nominal design bandwidth
    m2 = (f > fc6 - 0.4 * bw_nom) & (f < fc6 + 0.4 * bw_nom)
    rip_nom = float(yr[m2].max() - yr[m2].min()) if m2.any() else math.nan
    # true ripple: deepest interior valley between two passband peaks inside the -6 dB band
    # (0 for a monotone rounded passband; > 0 when crystal mistuning splits the passband)
    m6 = np.where((f > lo6) & (f < hi6))[0]
    rip_pv = 0.0
    if len(m6) > 4:
        seg = yr[m6]
        peaks = [i for i in range(1, len(seg) - 1) if seg[i] >= seg[i - 1] and seg[i] > seg[i + 1]]
        for a_, b_ in zip(peaks[:-1], peaks[1:]):
            valley = seg[a_:b_ + 1].min()
            rip_pv = max(rip_pv, float(min(seg[a_], seg[b_]) - valley))
    # attenuation at fixed offsets from the -6 dB centre
    def att_at(off: float) -> float:
        return float(-np.interp(fc6 + off, f, yr))
    return dict(il_db=float(-pk), bw3_hz=float(bw3), bw6_hz=float(bw6), bw60_hz=float(bw60),
                shape_60_6=float(bw60 / bw6) if bw6 > 0 else math.nan,
                fc6_hz=float(fc6), fc_err_hz=float(fc6 - f_nom),
                ripple_db=rip, ripple_nom_db=rip_nom, ripple_pv_db=rip_pv,
                att_p1k=att_at(+1000.0), att_m1k=att_at(-1000.0),
                att_p2k=att_at(+2000.0), att_m2k=att_at(-2000.0),
                att_p5k=att_at(+5000.0), att_m5k=att_at(-5000.0))


def parse_raw(raw: Path) -> tuple[np.ndarray, list[np.ndarray], list[np.ndarray]]:
    from spicelib import RawRead
    r = RawRead(str(raw))
    steps = r.get_steps()
    f = np.real(np.asarray(r.get_trace("frequency").get_wave(steps[0])))
    vo = [np.asarray(r.get_trace("V(out)").get_wave(s)) for s in steps]
    vi = [np.asarray(r.get_trace("V(in)").get_wave(s)) for s in steps]
    return f, vo, vi


def pct(a: np.ndarray, p: float) -> float:
    return float(np.nanpercentile(a, p))


def summarize(rows: list[dict], keys: list[str]) -> dict:
    out = {}
    for k in keys:
        a = np.array([r[k] for r in rows], dtype=float)
        out[k] = dict(min=float(np.nanmin(a)), p5=pct(a, 5), p50=pct(a, 50), p95=pct(a, 95),
                      max=float(np.nanmax(a)), mean=float(np.nanmean(a)), std=float(np.nanstd(a)),
                      nan=int(np.isnan(a).sum()))
    return out


def plot(case: str, f: np.ndarray, ys: list[np.ndarray], rows: list[dict], f_nom: float,
         bw_nom: float, out_png: Path, ver: str) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(2, 2, figsize=(12, 8))
    a = ax[0, 0]
    for y in ys[:60]:
        a.plot((f - f_nom), y, lw=0.5, alpha=0.5)
    a.set_ylim(-100, 2)
    a.set_xlabel("offset from design centre (Hz)")
    a.set_ylabel("gain re matched lossless (dB)")
    a.set_title(f"{case}: first 60 of {len(ys)} runs (wide)")
    a.grid(True, alpha=0.3)
    a = ax[0, 1]
    for y in ys[:60]:
        a.plot((f - f_nom), y, lw=0.5, alpha=0.5)
    a.set_xlim(-1.2 * bw_nom, 1.2 * bw_nom)
    a.set_ylim(-20, 1)
    a.set_xlabel("offset from design centre (Hz)")
    a.set_title("passband detail")
    a.grid(True, alpha=0.3)
    a = ax[1, 0]
    bw3 = np.array([r["bw3_hz"] for r in rows])
    a.hist(bw3[~np.isnan(bw3)], bins=30, color="tab:blue", alpha=0.8)
    a.axvline(bw_nom, color="k", ls="--")
    a.set_xlabel("-3 dB bandwidth (Hz)")
    a.set_ylabel("runs")
    a.set_title("bandwidth distribution")
    a = ax[1, 1]
    rip = np.array([r["ripple_pv_db"] for r in rows])
    fce = np.array([r["fc_err_hz"] for r in rows])
    il = np.array([r["il_db"] for r in rows])
    sc = a.scatter(fce, il, c=rip, s=10, alpha=0.8, cmap="viridis")
    fig.colorbar(sc, ax=a, label="peak-to-valley ripple (dB)")
    a.set_xlabel("centre frequency error vs design (Hz)")
    a.set_ylabel("insertion loss (dB)")
    a.set_title("insertion loss vs centre error (colour: true ripple)")
    a.grid(True, alpha=0.3)
    fig.suptitle(f"{case}  [{ver}]", fontsize=10)
    fig.tight_layout()
    fig.savefig(out_png, dpi=110)
    plt.close(fig)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--case", required=True, help="case name (used for file names)")
    ap.add_argument("--poles", type=int, default=4)
    ap.add_argument("--bw", type=float, default=500.0, help="design -3 dB bandwidth, Hz")
    ap.add_argument("--proto", choices=["butterworth", "chebyshev"], default="butterworth")
    ap.add_argument("--ripple", type=float, default=0.1, help="Chebyshev ripple, dB")
    ap.add_argument("--fs", type=float, default=9.000e6, help="nominal crystal series resonance, Hz")
    ap.add_argument("--cm", type=float, default=20e-15, help="nominal motional capacitance, F")
    ap.add_argument("--rs", type=float, default=25.0, help="nominal motional resistance, ohm (used for R_end synthesis)")
    ap.add_argument("--c0", type=float, default=4.5e-12, help="nominal holder capacitance, F")
    ap.add_argument("--runs", type=int, default=200)
    ap.add_argument("--fspan", type=float, default=6000.0, help="half sweep span, Hz")
    ap.add_argument("--points", type=int, default=6001)
    ap.add_argument("--f-ppm", type=float, default=30.0)
    ap.add_argument("--f-dist", choices=["flat", "gauss"], default="flat")
    ap.add_argument("--f-trunc-ppm", type=float, default=0.0)
    ap.add_argument("--cm-sigma-pct", type=float, default=3.0)
    ap.add_argument("--cm-trunc-pct", type=float, default=10.0)
    ap.add_argument("--rs-min", type=float, default=10.0)
    ap.add_argument("--rs-max", type=float, default=40.0)
    ap.add_argument("--c0-min-pf", type=float, default=3.5)
    ap.add_argument("--c0-max-pf", type=float, default=5.5)
    ap.add_argument("--cap-pct", type=float, default=2.0)
    ap.add_argument("--res-pct", type=float, default=1.0)
    ap.add_argument("--seed", type=int, default=None)
    ap.add_argument("--cm-actual-scale", type=float, default=1.0,
                    help="lot shift: simulate crystals whose Cm is this multiple of the design Cm (design unchanged)")
    ap.add_argument("--bw-target", type=float, default=None,
                    help="target -3 dB bandwidth for the yield criterion (default: design bandwidth)")
    ap.add_argument("--outdir", type=Path, default=Path(__file__).resolve().parent / "out")
    ap.add_argument("--figdir", type=Path, default=Path(__file__).resolve().parents[2] / "figures" / "cw-selectivity")
    ap.add_argument("--design-only", action="store_true")
    ap.add_argument("--reuse-raw", action="store_true", help="re-parse an existing out/<case>.raw instead of simulating")
    args = ap.parse_args()

    x = Crystal(args.fs, args.cm, args.rs, args.c0)
    d = synthesize(x, args.poles, args.bw, args.proto, args.ripple)
    sp = Spread(args.f_ppm, args.f_dist, args.f_trunc_ppm, args.cm_sigma_pct, args.cm_trunc_pct,
                args.rs_min, args.rs_max, args.c0_min_pf, args.c0_max_pf, args.cap_pct, args.res_pct)
    args.outdir.mkdir(parents=True, exist_ok=True)
    args.figdir.mkdir(parents=True, exist_ok=True)
    design = dict(crystal=asdict(x), lm_mH=x.lm_h * 1e3, qu=x.qu, design=asdict(d))
    print(json.dumps(design, indent=1, default=float)[:2000])
    if d.r1_ohm <= 0 or d.rn_ohm <= 0:
        print(f"WARNING: negative termination (R1={d.r1_ohm:.1f}, Rn={d.rn_ohm:.1f}): crystal Qu too low for this design")
    if args.design_only:
        return 0
    deck = args.outdir / f"{args.case}.net"
    t0 = time.time()
    if args.reuse_raw and deck.with_suffix(".raw").exists():
        # re-parse an existing simulation (same random draws, e.g. to regenerate plots or metrics)
        raw, log = deck.with_suffix(".raw"), deck.with_suffix(".log")
        ver = next((l for l in log.read_text(errors="replace").splitlines() if l.startswith("LTspice")), "?")
        print(f"reusing existing {raw.name} (no new simulation)")
    else:
        write_deck(deck, x, d, sp, args.runs, args.fspan, args.points, args.seed, args.cm_actual_scale)
        raw, log, ver = run_ltspice(deck)
    t_sim = time.time() - t0
    f, vo, vi = parse_raw(raw)
    rows = []
    ys = []
    for i, (o, n_) in enumerate(zip(vo, vi)):
        m = metrics(f, o, n_, d.r1_ohm, d.rn_ohm, args.bw, d.f_mesh_hz)
        m["run"] = i + 1
        rows.append(m)
        h = np.abs(o) / np.abs(n_)
        ys.append(-10 * np.log10((1.0 / (4 * d.r1_ohm)) / (h ** 2 / d.rn_ohm)))
    keys = ["il_db", "bw3_hz", "bw6_hz", "bw60_hz", "shape_60_6", "fc_err_hz", "ripple_db", "ripple_nom_db",
            "ripple_pv_db", "att_p1k", "att_m1k", "att_p2k", "att_m2k", "att_p5k", "att_m5k"]
    summ = summarize(rows, keys)
    # yield criteria (TBR): -3 dB bandwidth within +/-20 % of target, true ripple <= 1 dB, IL <= 8 dB
    bw_target = args.bw_target if args.bw_target else args.bw
    bw3 = np.array([r["bw3_hz"] for r in rows])
    rip = np.array([r["ripple_pv_db"] for r in rows])
    il = np.array([r["il_db"] for r in rows])
    ok = (np.abs(bw3 - bw_target) <= 0.2 * bw_target) & (rip <= 1.0) & (il <= 8.0)
    ok3 = (np.abs(bw3 - bw_target) <= 0.3 * bw_target) & (rip <= 2.0) & (il <= 10.0)
    result = dict(case=args.case, ltspice=ver, runs=args.runs, sim_seconds=round(t_sim, 1),
                  args={k: (str(v) if isinstance(v, Path) else v) for k, v in vars(args).items()},
                  design=design, summary=summ, bw_target=bw_target,
                  yield_bw20_rip1_il8=float(np.mean(ok)), yield_bw30_rip2_il10=float(np.mean(ok3)),
                  deck=str(deck), raw=str(raw))
    (args.outdir / f"{args.case}.json").write_text(json.dumps(result, indent=1, default=float))
    with (args.outdir / f"{args.case}.csv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["run"] + keys)
        w.writeheader()
        for r in rows:
            w.writerow({k: r[k] for k in ["run"] + keys})
    png = args.figdir / f"{args.case}.png"
    plot(args.case, f, ys, rows, d.f_mesh_hz, args.bw, png, ver)
    print(f"\n{ver} | {args.case}: {args.runs} runs in {t_sim:.1f} s")
    for k in keys:
        s = summ[k]
        print(f"  {k:14s} min {s['min']:9.2f}  p5 {s['p5']:9.2f}  p50 {s['p50']:9.2f}  p95 {s['p95']:9.2f}  max {s['max']:9.2f}  nan {s['nan']}")
    print(f"  yield (BW3 within +/-20 % of {bw_target:.0f} Hz, ripple_pv <= 1 dB, IL <= 8 dB): {100*np.mean(ok):.1f} %"
          f"   relaxed (+/-30 %, 2 dB, 10 dB): {100*np.mean(ok3):.1f} %")
    print(f"  plot: {png}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
