"""Checker for the half-IF (2RF - 2LO = IF) runs of the mixers (run r05). For every .step it resamples the saved
IF-port voltage onto a uniform grid over the saved window (an integer number of 250 ns periods, the common period
of the 4 MHz-spaced tones), takes the single-bin DFT at 8.000 MHz, and converts it to power into the port load
(ring: 50 ohm; JFET: the 330 ohm tank load, used only as a ratio). For each mixer configuration (set) it reports:
  - conversion gain Gc of the wanted tone (144.000 MHz, LO 136 MHz), IF power minus available RF power;
  - the half-IF product (tone at 140.000 MHz) IF power at each drive level, its fitted slope (dB/dB, expected 2)
    and the 2nd-order intercept referred to the mixer input, IIP2_hif = 2 P_in - (P_if,hif - Gc) ... solved as
    P_eq = P_if,hif - Gc (equivalent input level of the response); IIP2_hif = 2 P_in - P_eq.
The front-end referral to the antenna and the REQ-SYS-033 verdict are made in cascade.py, which reads result.json.
Usage: check_halfif.py <run-dir>"""
import json, os, sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from spicelib import RawRead
from scipy.interpolate import CubicSpline
plt.rcParams["axes.titlesize"] = 9

FIF = 8.0e6
FLOOR_DBC = -84.0
FLOOR_NOTE = ("numerical floor: the matched 50 % ring gives a response proportional to the input (slope 1) at about -81 dBc "
              "with a 20 ps maximum step and -86 dBc with 5 ps, independent of reltol, so it is time-step error; the "
              "10 ps decks are taken to have a floor near -84 dBc (estimate). Points less than 10 dB above it are not "
              "used for the intercept; a set with none gives a lower bound on IIP2.")


def if_power(t, v, rload, t0, t1):
    # cubic-spline resampling: linear interpolation of the variable-step LTspice points left an error floor
    # near -81 dBc (tried first, 2026-09-28); the spline error for 20 ps steps is below -190 dBc (estimate)
    n = 65536
    tu = np.linspace(t0, t1, n, endpoint=False)
    keep = np.concatenate(([True], np.diff(t) > 1e-15))  # drop near-duplicate points (dt down to 5e-21 s seen)
    vu = CubicSpline(t[keep], v[keep])(tu)
    ph = np.exp(-2j * np.pi * FIF * tu)
    a = 2 * np.abs(np.mean(vu * ph))  # peak amplitude at 8 MHz
    return 10 * np.log10(max(a, 1e-30) ** 2 / (2 * rload) / 1e-3)


def runs_of(run_dir, deck):
    """(raw path, step index, case) for a stepped deck, or for one deck per case (deck_cNN.net)."""
    cases = json.load(open(os.path.join(run_dir, deck + "_cases.json")))
    single = os.path.join(run_dir, deck + ".raw")
    if os.path.exists(single):
        r = RawRead(single, verbose=False)
        return [(r, s, c) for s, c in zip(r.get_steps(), cases)], []
    items, missing = [], []
    for i, c in enumerate(cases, 1):
        p = os.path.join(run_dir, f"{deck}_c{i:02d}.raw")
        log = os.path.join(run_dir, f"{deck}_c{i:02d}.log")
        ok = os.path.exists(p) and os.path.exists(log) and "Simulation Failed" not in open(log, errors="replace").read()
        if ok:
            items.append((RawRead(p, verbose=False), 0, c))
        else:
            missing.append(dict(c, case=i))
    return items, missing


def analyse(run_dir, deck, node, rload, label):
    items, missing = runs_of(run_dir, deck)
    out = []
    for r, s, c in items:
        t = np.real(r.get_trace("time").get_wave(s))
        v = np.real(r.get_trace(node).get_wave(s))
        t = np.abs(t)  # LTspice marks some time points negative in compressed raws; plotwinsize=0 keeps them positive
        t1 = t.max()
        t0 = t1 - 250e-9  # one common period of every tone (all on a 4 MHz grid)
        p = if_power(t, v, rload, t0, t1)
        out.append(dict(c, p_if_dbm=float(p), window_ns=float((t1 - t0) * 1e9)))
    sets = {}
    for o in out:
        sets.setdefault(o["set"], []).append(o)
    # Relative floor: the matched 50 % set (set 0) has no physical 2RF - 2LO product in a balanced ring; if its
    # response grows with slope near 1 it is the time-step floor, and its level is used for every set.
    floor_rel = FLOOR_DBC
    s0 = sets.get(0, [])
    w0 = [o for o in s0 if abs(o["f"] - 144e6) < 1]
    h0 = [o for o in s0 if abs(o["f"] - 140e6) < 1 and o["p"] > -100]
    if w0 and len(h0) >= 2:
        g0 = w0[0]["p_if_dbm"] - w0[0]["p"]
        r0 = np.array([o["p_if_dbm"] - o["p"] - g0 for o in h0])
        sl = np.polyfit([o["p"] for o in h0], [o["p_if_dbm"] for o in h0], 1)[0]
        if abs(sl - 1) < 0.2:
            floor_rel = float(np.max(r0))
    summary = []
    for k in sorted(sets):
        rows = sets[k]
        w = [o for o in rows if abs(o["f"] - 144e6) < 1]
        z = [o for o in rows if abs(o["f"] - 140e6) < 1 and o["p"] <= -100]
        h = sorted([o for o in rows if abs(o["f"] - 140e6) < 1 and o["p"] > -100], key=lambda o: o["p"])
        floor_abs = max(o["p_if_dbm"] for o in z) if z else None  # highest IF level with the tone 100 dB or more down
        gc = w[0]["p_if_dbm"] - w[0]["p"]
        pin = np.array([o["p"] for o in h]); pif = np.array([o["p_if_dbm"] for o in h])
        slope, icpt = np.polyfit(pin, pif, 1)
        peq = pif - gc
        iip2 = 2 * pin - peq
        rel = pif - (pin + gc)
        ok = rel > floor_rel + 10  # at least 10 dB above the relative (time-step) floor
        if floor_abs is not None:
            ok &= pif > floor_abs + 10  # and 10 dB above the absolute floor of the zero-RF case
        if ok.any():
            iip2_fixed = float(np.min(iip2[ok]))  # lowest (worst) intercept among the valid points
            bound = False
        else:
            fl = max(pin.max() + gc + floor_rel, floor_abs if floor_abs is not None else -1e9)
            iip2_fixed = float(2 * pin.max() - (fl + 10 - gc))  # response below floor + 10 dB: lower bound
            bound = True
        summary.append(dict(set=k, duty=rows[0]["d"], gc_db=float(gc), fitted_slope=float(slope),
                            pin_dbm=pin.tolist(), p_if_hif_dbm=pif.tolist(), p_eq_dbm=peq.tolist(),
                            iip2_hif_dbm_each=iip2.tolist(), iip2_hif_dbm=iip2_fixed, iip2_is_lower_bound=bound,
                            floor_if_dbm_zero_rf=floor_abs, points_used=ok.tolist(),
                            rel_response_at_pin_dbc=(pif - (pin + gc)).tolist()))
    return out, summary, missing, floor_rel


def plot(run_dir, deck, summary, label, floor_rel):
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(13, 5))
    for s in summary:
        if deck == "halfif_ring":
            lab = f"set {s['set']} (duty {s['duty']*100:.0f} %{', matched' if s['set']==0 else ', mismatched'})"
        else:
            lab = f"set {s['set']} (LO duty {s['duty']*100:.0f} %)"
        a1.plot(s["pin_dbm"], s["p_eq_dbm"], "o-", label=lab)
        x = np.linspace(-80, 0, 50)
        a1.plot(x, 2 * x - s["iip2_hif_dbm"], ":", lw=0.8, color=a1.lines[-1].get_color())
    x = np.linspace(-80, 0, 50)
    a1.plot(x, x, "k-", lw=0.8, label="wanted tone (equivalent level = input level)")
    if deck == "halfif_ring":  # measured from the matched set; the JFET floor cases did not converge
        a1.plot(x, x + floor_rel, color="grey", ls="-.", lw=1, label=f"time-step floor ({floor_rel:.1f} dBc, not physical)")
    a1.axvspan(-58.5, -51.8, color="tab:orange", alpha=0.15, label="mixer input for a -70 dBm antenna tone (front-end gain 11.5 to 18.2 dB, r06)")
    a1.plot([-58.5, -51.8], [-140 + 11.5, -140 + 18.2], "k--", lw=2.5, label="REQ-SYS-033 limit at that input (-140 dBm at the antenna + gain)")
    a1.set_xlabel("half-IF tone at the mixer RF port (dBm available)"); a1.set_ylabel("equivalent input level of the IF response (dBm)")
    a1.set_title(f"{label}: half-IF response (2RF - 2LO), dotted = slope-2 extrapolation")
    a1.grid(alpha=0.3); a1.legend(fontsize=7); a1.set_ylim(-260, 10)
    a2.bar([str(s["set"]) for s in summary], [s["iip2_hif_dbm"] for s in summary], color=["white" if s["iip2_is_lower_bound"] else "tab:blue" for s in summary],
           edgecolor="tab:blue", hatch=None)
    for i, s_ in enumerate(summary):
        a2.text(i, s_["iip2_hif_dbm"] + 1, ("lower bound " if s_["iip2_is_lower_bound"] else "") + f"{s_['iip2_hif_dbm']:.1f}", ha="center", fontsize=8)
    a2.set_xlabel("configuration set (ring: 0 = matched, 50 % duty; JFET: LO duty 50 and 45 %)"); a2.set_ylabel("half-IF IIP2 at the mixer input (dBm)")
    a2.set_title(f"{label}: half-IF IIP2 per set (white = bound)"); a2.grid(alpha=0.3, axis="y")
    fig.tight_layout()
    p = os.path.join(run_dir, f"{deck}_halfif.png"); fig.savefig(p, dpi=130); plt.close(fig)
    return os.path.basename(p)


if __name__ == "__main__":
    run_dir = os.path.abspath(sys.argv[1])
    res = {"run_id": os.path.basename(run_dir), "checker": "check_halfif.py", "note": FLOOR_NOTE, "mixers": {}}
    md = [f"# {res['run_id']}: result", "", "Checker: check_halfif.py. This run characterizes the mixers; the REQ-SYS-033 verdict for the half-IF response is made in the cascade run (r06) with the front-end gain and the filter attenuation at the half-IF frequency.", ""]
    for deck, node, rload, label in (("halfif_ring", "V(ct1)", 50.0, "A5 diode ring, 4 x 1N5711"),
                                     ("halfif_jfet", "V(d)", 330.0, "A4 single J310 mixer")):
        if not os.path.exists(os.path.join(run_dir, deck + "_cases.json")):
            continue
        out, summ, missing, floor_rel = analyse(run_dir, deck, node, rload, label)
        png = plot(run_dir, deck, summ, label, floor_rel)
        res["mixers"][deck] = {"label": label, "steps": out, "sets": summ, "plot": png, "missing_cases": missing, "relative_floor_dbc": floor_rel}
        md += [f"## {deck}: {label}", "", "| set | LO duty | Gc (dB) | zero-RF floor at 8 MHz (dBm) | half-IF tone levels (dBm) | IF response re wanted at same level (dBc) | points used | fitted slope, all points (dB/dB) | IIP2 half-IF (dBm, slope 2, worst valid point) |", "|---|---|---|---|---|---|---|---|---|"]
        for s in summ:
            fz = s['floor_if_dbm_zero_rf']
            md.append(f"| {s['set']} | {s['duty']*100:.0f} % | {s['gc_db']:.2f} | {'-' if fz is None else f'{fz:.1f}'} | {', '.join(f'{x:.0f}' for x in s['pin_dbm'])} | {', '.join(f'{x:.1f}' for x in s['rel_response_at_pin_dbc'])} | {', '.join('y' if u else 'n' for u in s['points_used'])} | {s['fitted_slope']:.2f} | {('>= ' if s['iip2_is_lower_bound'] else '')}{s['iip2_hif_dbm']:.1f} |")
        md += ["", f"Relative (time-step) floor used: {floor_rel:.1f} dBc (from the matched set when its response has slope near 1, else {FLOOR_DBC:.0f} dBc)."]
        if missing:
            md += ["", "Cases that did not complete in LTspice (not used): " + "; ".join(f"case {m['case']} ({m['f']/1e6:.0f} MHz, {m['p']} dBm, duty {m['d']*100:.0f} %)" for m in missing)]
        md += ["", f"![{png}]({png})", ""]
    json.dump(res, open(os.path.join(run_dir, "result.json"), "w"), indent=1)
    open(os.path.join(run_dir, "result.md"), "w").write("\n".join(md) + "\n")
    print("\n".join(md))
