#!/usr/bin/env python3
"""WP-PDR-28 pre-order thermal model for the TS-012 finalists A4 and A5 (runner).

Runs thermal_model.py over the four layouts of LAYOUTS (A4 and A5, each as TS-012 revision 4 wrote it
and with the no-cost design changes), writes the owner-rule results directory and draws the plots:

  hardware/sim/thermal/results/<run-id>/
    verdicts.md            pass/fail per finalist and criterion, with the numbers
    summary.csv            every metric per layout and case
    inputs.csv             every input with its value, range, class (D, DD, R, E) and source
    tornado.csv            one-at-a-time sensitivity rows
    duty_sweep.csv         junction peak and sink temperature versus key-down duty
    ltspice/               electrical-analogue deck (.net), LTspice .log and .raw, comparison
    *.png                  plots, each with the requirement or limit drawn on it
    scripts/               copy of the model and this runner as run

Run:  .venv/bin/python hardware/sim/thermal/ts012_thermal.py [--run-id ID] [--no-ltspice]
LTspice runs only through tools/ltspice-batch.sh (ACC-LTSPICE-001).
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import shutil
import subprocess
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))
import thermal_model as m  # noqa: E402

COL = {"A5-R4": "#c0504d", "A5-DC": "#1f77b4", "A4-R4": "#e69f00", "A4-DC": "#2ca02c"}
LABEL = {
    "A5-R4": "A5 as TS-012 rev 4 (sink end wall at web, guard 3 mm)",
    "A5-DC": "A5 with design changes (sink outside, wrap guard, shield, vents)",
    "A4-R4": "A4 as TS-012 rev 4 (sink end wall at web, no bulkhead)",
    "A4-DC": "A4 with design changes (sink outside, wrap guard, bay, vents)",
}
ON_S = 10.0  # key-down length of the duty cases: the longest a key-down lasts (REQ-SYS-055 cutoff)


def key_duty(duty: float, on: float = ON_S):
    if duty >= 1.0:
        return lambda t: 1.0
    period = on / duty
    return lambda t: 1.0 if (t % period) < on else 0.0


def first_cross(ts, ys, level):
    idx = np.nonzero(ys >= level)[0]
    return float(ts[idx[0]]) if len(idx) else None


def periodic_peak(net: m.Net, duty: float, cycles: int = 30, dt: float = 0.25):
    """Peak junction and sink over the last cycle of a periodic key-down (10 s on) at duty, from the
    average-power steady state."""
    T0 = net.steady(duty)
    if duty >= 1.0:
        return m.tj(net, T0), T0["SINK"], T0["SINK"]
    period = ON_S / duty
    ts, xs = net.transient(cycles * period, dt, key_duty(duty), x0=T0)
    last = ts >= (cycles - 1) * period
    jn = "J2" if net.meta["fin"] == "A5" else "J"
    ij, isk = net.names.index(jn), net.names.index("SINK")
    return float(xs[last, ij].max()), float(xs[last, isk].max()), float(xs[last, isk].min())


def window_max(ts, ys, w=60.0):
    edges = np.arange(0, ts[-1] + w, w)
    tt, yy = [], []
    for a, b in zip(edges[:-1], edges[1:]):
        sel = (ts >= a) & (ts < b)
        if sel.any():
            tt.append(b)
            yy.append(ys[sel].max())
    return np.array(tt), np.array(yy)


# ------------------------------------------------------------------------------------------ cases
def run_layout(L: str):
    v = m.vals()
    res = {"layout": L}
    # 1. REQ-SYS-112 steady, continuous key-down, 45 C
    net = m.build(L, 45.0)
    T = net.steady(1.0)
    res["meta"] = dict(net.meta)
    res["ss45"] = T
    res["tj_ss"] = m.tj(net, T)
    res["petg_ss"] = m.petg_hot_faces(net, T)
    res["fr4_ss"] = m.hot_faces(net, T, "FR4")
    res["walls_ss"] = m.hot_faces(net, T, None)
    n25 = m.build(L, 25.0)
    res["tj_ss25"] = m.tj(n25, n25.steady(1.0))
    res["surf_ss45"] = m.surfaces(net, T)
    # 2. transient from a 45 C soak, continuous
    ts, xs = net.transient(3 * 3600.0, 1.0, lambda t: 1.0, every=10)
    res["tr_cont"] = (ts, xs, list(net.names))
    isk = net.names.index("SINK")
    jn = "J2" if net.meta["fin"] == "A5" else "J"
    ij = net.names.index(jn)
    ic = net.names.index("CELL")
    res["t_fw"] = first_cross(ts, xs[:, isk], v["trip_fw"])
    res["t_hw"] = first_cross(ts, xs[:, isk], v["trip_hw"])
    res["t_tj110"] = first_cross(ts, xs[:, ij], v["tj_limit"])
    res["t_cell60"] = first_cross(ts, xs[:, ic], v["cell_limit"])
    res["tj_at_hw"] = float(np.interp(res["t_hw"], ts, xs[:, ij])) if res["t_hw"] else None
    # 3. 50 % duty (10 s on, 10 s off) from a 45 C soak, 3 h
    ts5, xs5 = net.transient(3 * 3600.0, 0.5, key_duty(0.5), every=2)
    res["tr_50"] = (ts5, xs5)
    i30 = np.searchsorted(ts5, 1800.0)
    im = net.names.index("MAIN")
    res["cell_30"] = float(xs5[: i30 + 1, ic].max())
    res["main_30"] = float(xs5[: i30 + 1, im].max())
    T50 = net.steady(0.5)
    res["ss50"] = T50
    res["petg_ss50"] = m.petg_hot_faces(net, T50)
    res["t_fw50"] = first_cross(ts5, xs5[:, isk], v["trip_fw"])
    res["t_hw50"] = first_cross(ts5, xs5[:, isk], v["trip_hw"])
    pk50, _, _ = periodic_peak(net, 0.5)
    res["tj_pk50"] = pk50
    # 4. REQ-SYS-113: 25 C, 5 min continuous from a 25 C soak
    net25 = m.build(L, 25.0)
    t25, x25 = net25.transient(600.0, 0.5, lambda t: 1.0, every=2)
    res["tr_25"] = (t25, x25, list(net25.names), net25)
    i5 = np.searchsorted(t25, 300.0)
    T5 = net25.tdict(x25[i5])
    res["surf_5min"] = m.surfaces(net25, T5)
    return res


def duty_sweep(L: str):
    net = m.build(L, 45.0)
    rows = []
    for d in np.round(np.arange(0.10, 1.0001, 0.05), 2):
        pk, smax, smin = periodic_peak(net, float(d))
        rows.append(dict(layout=L, duty=float(d), tj_peak=pk, sink_max=smax, sink_min=smin,
                         cell_ss=net.steady(float(d))["CELL"]))
    return rows


def duty_limit(L: str, sweep_rows, v):
    """Firmware duty limit (TS-012 7.3 fallback): refuse a new key-down while the sink NTC reads
    above S. S is set so that a 13 s key-down (the longest the REQ-SYS-055 cutoff allows) starting
    at S keeps the junction <= 110 C, with the sink's rise over 13 s counted without losses."""
    net = m.build(L, 45.0)
    meta = net.meta
    c = net.cap["SINK"] + net.cap["CASE"]
    if meta["fin"] == "A5":
        p = meta["p_pa"]
        s = v["tj_limit"] - meta["p2"] * v["a5_rjc2"] - p * meta["r_if"] - p * 13.0 / c
    else:
        p = meta["p_pa"]
        s = v["tj_limit"] - p * (v["a4_rjc"] + meta["r_cs"]) - (p + v["a4_gva_on_sink"]) * 13.0 / c
    ok = [r for r in sweep_rows if r["tj_peak"] <= v["tj_limit"]]
    dmax = max((r["duty"] for r in ok), default=0.0)
    # REQ-SYS-118 inhibit with its NTC on the PA case (A5 flange screw; A4 pad at the tab, TS-011
    # rule 14): the junction is bounded by the trip temperature plus the case-to-junction rise alone.
    if meta["fin"] == "A5":
        rise_nom = meta["p2"] * v["a5_rjc2"]
        va = dict(v, r_feed=0.0)  # bench supply, no feed drop
        p_hi = m.dissipation("A5", va)["p_pa"]
        rise_adv = (p_hi - m.P["a5_p1"].low) * m.P["a5_rjc2"].high
    else:
        rise_nom = meta["p_pa"] * v["a4_rjc"]
        va = dict(v, a4_isat=m.P["a4_isat"].high)
        rise_adv = m.dissipation("A4", va)["p_pa"] * m.P["a4_rjc"].high
    inh = v["trip_fw"]
    # duty-limited corner: steady state at the largest duty that holds 110 C
    Td = net.steady(dmax) if dmax > 0 else None
    return dict(setpoint=s, dmax=dmax, tj_inh_nom=inh + rise_nom, tj_inh_tol=inh + 3.0 + rise_nom,
                tj_inh_adv=inh + 3.0 + rise_adv,
                dl_petg=max(m.petg_hot_faces(net, Td).values()) if Td else np.nan,
                dl_petg_part=max(m.petg_hot_faces(net, Td), key=m.petg_hot_faces(net, Td).get) if Td else "-",
                dl_fr4=max(m.hot_faces(net, Td, "FR4").values(), default=np.nan) if Td else np.nan,
                dl_cell=Td["CELL"] if Td else np.nan, dl_main=Td["MAIN"] if Td else np.nan,
                dl_bay=Td.get("BAY", Td["MAIN"]) if Td else np.nan, dl_sink=Td["SINK"] if Td else np.nan,
                dl_case=Td["CASE"] if Td else np.nan, dl_faces=m.hot_faces(net, Td, None) if Td else {})


def tornado(L: str, metric: str):
    base_v = m.vals()
    names = {
        "A5": ["a5_idd", "r_feed", "k_orient", "k_cat", "a5_bond", "k_tim", "r_spread_x", "a5_rjc2", "a5_p1",
               "eta_guard_dc", "phi_dc", "eta_wall", "r_frac", "shield_rad", "h_out_c", "sink_mass"],
        "A4": ["a4_isat", "r_feed", "k_orient", "k_cat", "a4_rjc", "a4_r_pad", "a4_r_via", "a4_r_bs",
               "a4_gva_on_sink", "eta_guard_dc", "eta_wall", "r_frac", "shield_rad", "h_out_c"],
        "cell": ["p_lm2940", "r_feed", "r_cellpath", "g_cell_main", "g_cell_wall", "h_in_c", "h_out_c",
                 "g_leads", "vent_area_dc", "main_vent_area", "relay_hold", "k_orient", "p_pico", "i_bus", "k_petg"],
        "petg": ["k_orient", "r_frac", "eta_wall", "shield_rad", "h_out_c", "h_in_c", "vent_area_dc", "k_cat",
                 "a5_idd", "k_petg", "g_leads", "main_vent_area", "relay_hold", "eta_guard_dc", "phi_dc"],
    }

    def evaluate(v):
        net = m.build(L, 45.0, v)
        if metric == "tj":
            return m.tj(net, net.steady(1.0))
        if metric == "cell50":
            return net.steady(0.5)["CELL"]
        if metric == "petg":
            T = net.steady(1.0)
            return max(m.petg_hot_faces(net, T, v).values())
        raise ValueError(metric)

    base = evaluate(base_v)
    key = metric if metric in ("cell50", "petg") else None
    plist = names["cell" if key == "cell50" else "petg" if key == "petg" else L[:2]]
    rows = []
    for p in plist:
        prm = m.P[p]
        lo = evaluate(dict(base_v, **{p: prm.low}))
        hi = evaluate(dict(base_v, **{p: prm.high}))
        rows.append(dict(layout=L, metric=metric, param=p, cls=prm.cls, base_value=prm.value, low=prm.low,
                         high=prm.high, out_base=base, out_low=lo, out_high=hi, swing=abs(hi - lo)))
    rows.sort(key=lambda r: r["swing"], reverse=True)
    return base, rows


def adverse_stack(L: str):
    """Every E and DD input at the end that raises the junction (from the tornado), together."""
    base_v = m.vals()
    _, rows = tornado(L, "tj")
    v = dict(base_v)
    for r in rows:
        v[r["param"]] = r["high"] if r["out_high"] > r["out_low"] else r["low"]
    net = m.build(L, 45.0, v)
    return m.tj(net, net.steady(1.0))


def favourable_stack(L: str):
    base_v = m.vals()
    _, rows = tornado(L, "tj")
    v = dict(base_v)
    for r in rows:
        v[r["param"]] = r["low"] if r["out_high"] > r["out_low"] else r["high"]
    net = m.build(L, 45.0, v)
    return m.tj(net, net.steady(1.0))


# ------------------------------------------------------------------------------------------ LTspice
def ltspice_check(out: Path, L: str = "A5-DC"):
    d = out / "ltspice"
    d.mkdir(exist_ok=True)
    net = m.build(L, 45.0)
    T = net.steady(1.0)
    lin = net.linearized(T)
    deck = d / "thermal_a5dc.net"
    lines = [f"* cwht WP-PDR-28 thermal network {L}, electrical analogue (1 V = 1 C, 1 A = 1 W, 1 ohm = 1 K/W, 1 F = 1 J/K)",
             "* conductances frozen at the Python steady state of the REQ-SYS-112 corner (45 C, continuous key-down)",
             "* generated by hardware/sim/thermal/ts012_thermal.py; run with tools/ltspice-batch.sh",
             "VAMB amb 0 45"]
    for k, (a, b, g) in enumerate(lin, 1):
        na = a.lower()
        nb = "amb" if b == "AMB" else b.lower()
        lines.append(f"R{k} {na} {nb} {1.0 / g:.9g}")
    for k, n in enumerate(net.names, 1):
        lines.append(f"C{k} {n.lower()} 0 {net.cap[n]:.9g}")
    p_on = net.power(1.0)
    for k, (n, p) in enumerate(zip(net.names, p_on), 1):
        if p != 0.0:
            lines.append(f"I{k} 0 {n.lower()} {p:.9g}")
    lines += [".ic " + " ".join(f"V({n.lower()})=45" for n in net.names),
              ".tran 0 7200 0 2",
              ".meas tran tj2_end FIND V(j2) AT=7200",
              ".meas tran sink_end FIND V(sink) AT=7200",
              ".meas tran cell_end FIND V(cell) AT=7200",
              ".end"]
    deck.write_text("\n".join(lines) + "\n")
    cmd = [str(ROOT / "tools/ltspice-batch.sh"), "-t", "180", "-o", str(d), "-b", str(deck)]
    pr = subprocess.run(cmd, capture_output=True, text=True)
    (d / "ltspice-batch.stderr.txt").write_text(pr.stdout + pr.stderr)
    if pr.returncode != 0:
        return dict(ok=False, rc=pr.returncode, msg=pr.stderr[-2000:])
    from spicelib import RawRead
    raw = RawRead(str(d / "thermal_a5dc.raw"))
    t_lt = np.abs(np.array(raw.get_trace("time").get_wave(0), dtype=float))
    res = {}
    # Python linear network with the same frozen conductances
    lnet = m.Net(t_amb=45.0)
    for n in net.names:
        lnet.add(n, net.cap[n])
    for a, b, g in lin:
        lnet.link(a, b, g)
    for n, p in zip(net.names, p_on):
        lnet.src(n, p)
    ts, xs = lnet.transient(7200.0, 0.5, lambda t: 1.0, every=4)
    fig, ax = plt.subplots(figsize=(9, 5))
    maxdiff = 0.0
    for n, c in (("J2", "#c0504d"), ("CASE", "#8064a2"), ("SINK", "#1f77b4"), ("EW", "#9e480e"),
                 ("BAY", "#e69f00"), ("CELL", "#2ca02c")):
        y_lt = np.array(raw.get_trace(f"V({n.lower()})").get_wave(0), dtype=float)
        y_py = np.interp(t_lt, ts, xs[:, net.names.index(n)])
        diff = float(np.max(np.abs(y_lt - y_py)[t_lt > 30]))
        maxdiff = max(maxdiff, diff)
        res[n] = dict(lt_end=float(y_lt[-1]), py_end=float(xs[-1, net.names.index(n)]), ss=T[n], maxdiff=diff)
        ax.plot(t_lt / 60, y_lt, color=c, lw=2.5, alpha=0.45, label=f"{n} LTspice")
        ax.plot(ts / 60, xs[:, net.names.index(n)], color=c, lw=1.0, ls="--", label=f"{n} Python")
    ax.axhline(110, color="k", ls=":", lw=1)
    ax.text(1, 111, "REQ-SYS-112 limit 110 C (junction)", fontsize=8)
    ax.set_xlabel("time from key-down, min (45 C soak, continuous key-down)")
    ax.set_ylabel("temperature, C")
    ax.set_title(f"LTspice electrical analogue vs Python solver, {L} linearized at the corner\n"
                 f"max |difference| after 30 s = {maxdiff:.3f} K (pass criterion 0.5 K)")
    ax.legend(fontsize=7, ncol=2)
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(out / "ltspice_crosscheck.png", dpi=130)
    plt.close(fig)
    return dict(ok=True, maxdiff=maxdiff, nodes=res, deck_sha256=hashlib.sha256(deck.read_bytes()).hexdigest())


# ------------------------------------------------------------------------------------------ plots
def plot_catalog(out: Path):
    fig, ax = plt.subplots(figsize=(8, 4.8))
    pw = np.linspace(2, 20, 100)
    ax.plot(m.CAT_P_W, m.CAT_DT_K, "o", color="#1f77b4", label="Boyd 530002 (5300 series) catalog curve, digitized")
    ax.plot(pw, pw * 2.6, "--", color="#7f7f7f", label="2.6 K/W catalog rating (TS-012 rev 4 nominal)")
    ax.plot(pw, pw * 3.4, ":", color="#7f7f7f", label="3.4 K/W (TS-012 rev 3 figure)")
    dt = np.linspace(8.7, 59, 60)
    ax.plot([m.g_cat(x) * x for x in dt], dt, "-", color="#1f77b4", lw=1, label="interpolation used by the model")
    for pp, lab in ((9.94, "A5 corner 9.94 W"), (5.55 + 0.5, "A4 corner 6.05 W")):
        dtp = np.interp(pp, m.CAT_P_W, m.CAT_DT_K)
        ax.plot([pp], [dtp], "s", color="k")
        ax.annotate(f"{lab}: {dtp:.0f} K, {dtp / pp:.2f} K/W", (pp, dtp), xytext=(pp + 1, dtp - 9), fontsize=8,
                    arrowprops=dict(arrowstyle="->", lw=0.6))
    ax.set_xlabel("heat dissipated, W")
    ax.set_ylabel("mounting-surface rise above ambient, K")
    ax.set_title("Heat sink in free air, vertical, unguarded (catalog condition)\n"
                 "the 2.6 K/W rating is not the natural-convection value at 6 to 10 W")
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(out / "sink_catalog_curve.png", dpi=130)
    plt.close(fig)


def plot_time(out: Path, results, v):
    fig, axs = plt.subplots(2, 2, figsize=(13, 9.5), sharex=True)
    for col, fin in enumerate(("A5", "A4")):
        ax, ax2 = axs[0, col], axs[1, col]
        for L in (f"{fin}-R4", f"{fin}-DC"):
            r = results[L]
            ts, xs, names = r["tr_cont"]
            sel = ts > 0
            jn = "J2" if fin == "A5" else "J"
            t110 = r["t_tj110"]
            ax.plot(ts[sel] / 60, xs[sel, names.index(jn)], color=COL[L], lw=1.8,
                    label=f"{LABEL[L]}: continuous" + (f" (110 C at {t110 / 60:.1f} min)" if t110 else ""))
            ts5, xs5 = r["tr_50"]
            tw, yw = window_max(ts5, xs5[:, names.index(jn)], w=20.0)
            ax.plot(tw / 60, yw, color=COL[L], lw=1.2, ls="--", label=f"{L}: 50 % duty (10 s on / 10 s off), peak")
            th = r["t_hw"]
            ax2.plot(ts[sel] / 60, xs[sel, names.index("SINK")], color=COL[L], lw=1.6,
                     label=f"{L} sink" + (f" (95 C trip at {th / 60:.1f} min)" if th else " (never reaches 95 C)"))
            if th:
                ax2.plot(th / 60, v["trip_hw"], "o", color=COL[L], ms=6)
            tc = r["t_cell60"]
            ax2.plot(ts[sel] / 60, xs[sel, names.index("CELL")], color=COL[L], ls="-.", lw=1.4,
                     label=f"{L} cells" + (f" (60 C at {tc / 60:.0f} min)" if tc else " (stay under 60 C)"))
            if fin == "A5":
                ax2.plot(ts[sel] / 60, xs[sel, names.index("CASE")], color=COL[L], ls=":", lw=1.4,
                         label=f"{L} module case")
        ax.axhline(v["tj_limit"], color="k", lw=1.2)
        ax.text(0.12, v["tj_limit"] + 1.5, "REQ-SYS-112 limit 110 C", fontsize=8)
        ax.set_ylabel("junction (stage-2 channel for A5), C")
        ax.set_title(f"{fin}: junction at 45 C ambient, 8.4 V pack, 5 W at the SMA")
        ax.set_ylim(40, 150)
        ax.grid(alpha=0.3, which="both")
        ax.legend(fontsize=7, loc="lower right")
        for lvl, lab in ((v["trip_hw"], "95 C sink trip (REQ-SYS-181)"), (v["trip_fw"], "85 C firmware inhibit (REQ-SYS-118)"),
                         (v["cell_limit"], "60 C cell limit and trip"), (v["case_guid"], "90 C module case guidance")):
            if fin == "A4" and lvl == v["case_guid"]:
                continue
            ax2.axhline(lvl, color="k", lw=0.8, ls="--")
            ax2.text(0.12, lvl + 0.8, lab, fontsize=7)
        ax2.set_xscale("log")
        ax2.set_xlim(0.1, 180)
        ax2.set_xlabel("time from key-down, min, log scale (45 C soak)")
        ax2.set_ylabel("temperature, C")
        ax2.set_title(f"{fin}: sink, cells" + (" and module case" if fin == "A5" else "") + ", continuous key-down")
        ax2.set_ylim(40, 130)
        ax2.grid(alpha=0.3, which="both")
        ax2.legend(fontsize=7, loc="upper left", bbox_to_anchor=(0.0, 0.93))
    fig.suptitle("Junction versus time at the REQ-SYS-112 corner (lumped RC model; estimates labelled in inputs.csv)")
    fig.tight_layout()
    fig.savefig(out / "tj_vs_time_45C.png", dpi=130)
    plt.close(fig)


def plot_duty(out: Path, sweeps, limits, v):
    fig, ax = plt.subplots(figsize=(9, 5.5))
    for L, rows in sweeps.items():
        d = [r["duty"] * 100 for r in rows]
        ax.plot(d, [r["tj_peak"] for r in rows], "-o", ms=3, color=COL[L], label=LABEL[L])
        dm = limits[L]["dmax"]
        if dm > 0:
            ax.axvline(dm * 100, color=COL[L], lw=0.7, ls=":")
            ax.text(dm * 100 + 0.5, 42 + 4 * list(sweeps).index(L), f"{L} max {dm * 100:.0f} %", fontsize=7,
                    color=COL[L])
    ax.axhline(v["tj_limit"], color="k", lw=1.2)
    ax.text(11, v["tj_limit"] + 1.5, "REQ-SYS-112 limit 110 C", fontsize=8)
    ax.set_xlabel("key-down duty, % (10 s key-downs, 45 C ambient, periodic steady state)")
    ax.set_ylabel("peak junction, C")
    ax.set_title("Junction versus duty: the continuous corner is 100 %; 50 % is heavy CW sending")
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8, loc="upper left")
    ax.set_ylim(40, 150)
    fig.tight_layout()
    fig.savefig(out / "tj_vs_duty.png", dpi=130)
    plt.close(fig)


def plot_surfaces(out: Path, results, v):
    fig, axs = plt.subplots(2, 2, figsize=(13, 9), sharex=True, sharey=True)
    for ax, L in zip(axs.flat, ("A5-R4", "A5-DC", "A4-R4", "A4-DC")):
        t25, x25, names, net25 = results[L]["tr_25"]
        series = {}
        for i in range(len(t25)):
            s = m.surfaces(net25, net25.tdict(x25[i]))
            for k, val in s.items():
                series.setdefault(k, []).append(val)
        for k, ys in series.items():
            if k.startswith("SINK (if") and results[L]["meta"].get("fins_exposed"):
                continue  # the rev 4 fin-tip curve is the same node, drawn once
            ls = ":" if k.startswith("SINK") else "-"
            ax.plot(t25 / 60, ys, ls=ls, lw=1.5, label=k.replace("GUARD", "guard outer face").replace(
                "EF", "bay wall near sink").replace("BW", "PA-bay walls").replace("MW", "main case walls"))
        ax.axhline(v["surf_limit"], color="k", lw=1.2)
        ax.axvline(5, color="k", lw=0.8, ls="--")
        ax.text(0.1, v["surf_limit"] + 0.8, "REQ-SYS-113 limit 48 C", fontsize=8)
        ax.text(5.1, 26, "5 min", fontsize=8)
        s5 = results[L]["surf_5min"]
        worst = max((val, k) for k, val in s5.items() if not k.startswith("SINK (if"))
        ax.set_title(f"{LABEL[L]}\nhottest accessible at 5 min: {worst[1]} {worst[0]:.1f} C; "
                     f"bare sink {s5['SINK (if unguarded)']:.1f} C", fontsize=9)
        ax.grid(alpha=0.3)
        ax.legend(fontsize=7, loc="upper left")
        ax.set_ylim(24, 80)
    for ax in axs[1]:
        ax.set_xlabel("time from key-down, min (25 C soak, continuous key-down)")
    for ax in axs[:, 0]:
        ax.set_ylabel("outer-face temperature, C")
    fig.suptitle("REQ-SYS-113: accessible surfaces after 5 min of continuous key-down at 25 C ambient")
    fig.tight_layout()
    fig.savefig(out / "surfaces_25C_5min.png", dpi=130)
    plt.close(fig)


def plot_petg_cells(out: Path, results, limits, v):
    fig, axs = plt.subplots(1, 3, figsize=(18, 6), gridspec_kw=dict(width_ratios=[3, 3, 1.5]))
    layouts = list(results)
    parts = ["GUARD", "EF", "EW", "BW", "BH1", "BH2", "MW"]
    names = ["guard", "bay wall\nnear sink", "end wall\nfacing sink", "PA-bay\nwalls", "bulkhead\nbay side",
             "bulkhead\nmain side", "main case\nwalls"]
    w = 0.2
    for ax, key, title in ((axs[0], "walls_ss", "Continuous key-down, steady (REQ-SYS-112 corner as written)"),
                           (axs[1], "dl_faces", "Duty-limited corner (largest duty holding 110 C), steady")):
        for k, L in enumerate(layouts):
            faces = results[L]["walls_ss"] if key == "walls_ss" else limits[L]["dl_faces"]
            for i, p in enumerate(parts):
                if p not in faces:
                    continue
                fr4 = p == "EW" and L.endswith("DC")
                ax.bar(i + (k - 1.5) * w, faces[p], width=w, color=COL[L], hatch="//" if fr4 else None,
                       edgecolor="k" if fr4 else None, label=LABEL[L] if i == 0 else None)
        ax.axhline(v["petg_crit"], color="k", lw=1.2)
        ax.text(-0.45, v["petg_crit"] + 0.8, "TS-012 PETG criterion 60 C", fontsize=8)
        ax.axhline(v["petg_hdt"], color="#9e480e", lw=1.2, ls="--")
        ax.text(-0.45, v["petg_hdt"] + 0.8, "PETG HDT 69 C (typical, estimate)", fontsize=8, color="#9e480e")
        ax.axhline(105, color="#555", lw=0.8, ls=":")
        ax.text(3.3, 105.8, "FR4 wall limit 105 C (hatched bars are FR4, not PETG)", fontsize=7, color="#555")
        ax.set_xticks(range(len(parts)))
        ax.set_xticklabels(names, fontsize=8)
        ax.set_ylabel("hot-face temperature, C")
        ax.set_title(title + ", 45 C ambient", fontsize=10)
        ax.set_ylim(40, 110)
        ax.grid(alpha=0.3, axis="y")
        ax.legend(fontsize=7, loc="upper left", bbox_to_anchor=(0.0, 0.95))
    ax = axs[2]
    for k, L in enumerate(layouts):
        r = results[L]
        ax.bar([0 + (k - 1.5) * w, 1 + (k - 1.5) * w], [r["cell_30"], r["main_30"]], width=w, color=COL[L], label=L)
    ax.axhline(v["cell_crit_a"], color="k", lw=1.2)
    ax.text(-0.45, v["cell_crit_a"] + 0.6, "criterion (a) 55 C", fontsize=8)
    ax.axhline(v["cell_limit"], color="k", lw=0.8, ls="--")
    ax.text(-0.45, v["cell_limit"] + 0.6, "60 C cell limit and trip", fontsize=8)
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["cells", "main-bay air"])
    ax.set_ylim(40, 70)
    ax.set_title("50 % duty for 30 min at 45 C,\nfrom a 45 C soak (criterion a)", fontsize=10)
    ax.grid(alpha=0.3, axis="y")
    ax.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(out / "petg_and_cells_45C.png", dpi=130)
    plt.close(fig)


def plot_tornado(out: Path, tor):
    fig, axs = plt.subplots(2, 2, figsize=(14, 10))
    titles = {("A5-DC", "tj"): "A5-DC junction, 45 C continuous (limit 110 C)",
              ("A4-DC", "tj"): "A4-DC junction, 45 C continuous (limit 110 C)",
              ("A5-DC", "cell50"): "A5-DC cells, 45 C, 50 % duty steady (criterion 55 C)",
              ("A5-DC", "petg"): "A5-DC hottest PETG face, 45 C continuous (criterion 60 C)"}
    limits = {"tj": 110.0, "cell50": 55.0, "petg": 60.0}
    for ax, (key, (base, rows)) in zip(axs.flat, tor.items()):
        rows = rows[:12][::-1]
        y = np.arange(len(rows))
        for i, r in enumerate(rows):
            lo, hi = r["out_low"] - base, r["out_high"] - base
            ax.barh(i, lo, left=base, color="#1f77b4", alpha=0.8)
            ax.barh(i, hi, left=base, color="#c0504d", alpha=0.8)
        ax.set_yticks(y)
        ax.set_yticklabels([f"{r['param']} [{r['cls']}] {r['low']:.3g}/{r['high']:.3g}" for r in rows], fontsize=7)
        ax.axvline(base, color="k", lw=1)
        ax.axvline(limits[key[1]], color="k", lw=1.5, ls="--")
        ax.text(limits[key[1]], len(rows) - 0.4, f" limit {limits[key[1]]:.0f} C", fontsize=8)
        ax.set_title(f"{titles[key]}; base {base:.1f} C", fontsize=9)
        ax.set_xlabel("C (blue: input at its low value; red: at its high value)")
        ax.grid(alpha=0.3, axis="x")
    fig.suptitle("Tornado: one input at a time from its low to its high (class D datasheet, DD derived, E estimate)")
    fig.tight_layout()
    fig.savefig(out / "tornado.png", dpi=130)
    plt.close(fig)


def plot_network(out: Path, L: str = "A5-DC"):
    net = m.build(L, 45.0)
    T = net.steady(1.0)
    pos = {"J2": (0, 6), "J1": (1.6, 6), "CASE": (0.8, 4.8), "SINK": (0.8, 3.3), "GUARD": (-1.4, 3.3),
           "EW": (2.6, 3.3), "BAY": (4.2, 3.3), "BW": (4.2, 5.0), "BH1": (4.2, 1.8), "BH2": (5.6, 1.8),
           "MAIN": (7.0, 3.3), "MW": (7.0, 5.0), "CELL": (7.0, 1.6), "AMB": (2.6, 0.0)}
    fig, ax = plt.subplots(figsize=(12, 7))
    seen = {}
    for a, b, fn in net.links:
        key = tuple(sorted((a, b)))
        seen[key] = seen.get(key, 0.0) + fn(T)
    for (a, b), g in seen.items():
        xa, ya = pos[a]
        xb, yb = pos[b]
        ax.plot([xa, xb], [ya, yb], color="#7f7f7f", lw=0.8, zorder=1)
        ax.text((xa + xb) / 2, (ya + yb) / 2, f"{1 / g:.2g}", fontsize=6.5, color="#444", ha="center",
                bbox=dict(fc="white", ec="none", pad=0.3), zorder=1.5)
    for n, (x, y) in pos.items():
        t = net.t_amb if n == "AMB" else T[n]
        ax.text(x, y, f"{n}\n{t:.1f} C", ha="center", va="center", fontsize=8,
                bbox=dict(fc="#dce6f2" if n != "AMB" else "#f2dcdb", ec="k", boxstyle="round"), zorder=3)
    ax.set_xlim(-2.4, 8.2)
    ax.set_ylim(-0.8, 6.8)
    ax.axis("off")
    ax.set_title(f"Thermal network {L} at the REQ-SYS-112 corner: node temperatures and link resistances (K/W)\n"
                 "links to AMB are summed per node; sources: J2, J1 (PA), BAY (GVA, relay, LPF), MAIN (LM2940, Pico, feed), CELL")
    fig.tight_layout()
    fig.savefig(out / "network_a5dc.png", dpi=130)
    plt.close(fig)


# ------------------------------------------------------------------------------------------ main
def fmt(x, n=1):
    return "-" if x is None else f"{x:.{n}f}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-id", default="2026-09-28-ts012-r1")
    ap.add_argument("--no-ltspice", action="store_true")
    a = ap.parse_args()
    out = HERE / "results" / a.run_id
    out.mkdir(parents=True, exist_ok=True)
    v = m.vals()

    with open(out / "inputs.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["name", "value", "low", "high", "unit", "class", "source"])
        for k, p in m.P.items():
            w.writerow([k, p.value, p.low, p.high, p.unit, p.cls, p.source])
        for pw, dt in zip(m.CAT_P_W, m.CAT_DT_K):
            w.writerow([f"boyd_curve_{pw:g}W", dt, dt - 1, dt + 1, "K", "DD", "Boyd catalog p.56, 5300 dashed curve, graph read"])

    results = {L: run_layout(L) for L in m.LAYOUTS}
    sweeps = {L: duty_sweep(L) for L in m.LAYOUTS}
    limits = {L: duty_limit(L, sweeps[L], v) for L in m.LAYOUTS}
    stacks = {L: (favourable_stack(L), adverse_stack(L)) for L in m.LAYOUTS}
    tor = {("A5-DC", "tj"): tornado("A5-DC", "tj"), ("A4-DC", "tj"): tornado("A4-DC", "tj"),
           ("A5-DC", "cell50"): tornado("A5-DC", "cell50"), ("A5-DC", "petg"): tornado("A5-DC", "petg")}

    with open(out / "duty_sweep.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(next(iter(sweeps.values()))[0].keys()))
        w.writeheader()
        for rows in sweeps.values():
            w.writerows(rows)
    with open(out / "tornado.csv", "w", newline="") as f:
        rows = [r for _, rr in tor.values() for r in rr]
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    summary = []
    for L, r in results.items():
        T = r["ss45"]
        row = dict(layout=L, p_pa_W=r["meta"]["p_pa"], i_pa_A=r["meta"]["i_pa"], tj_ss45=r["tj_ss"],
                   case_ss45=T["CASE"], sink_ss45=T["SINK"], bay_ss45=T.get("BAY", T["MAIN"]), main_ss45=T["MAIN"],
                   cell_ss45=T["CELL"], petg_max_ss45=max(r["petg_ss"].values()),
                   petg_max_part=max(r["petg_ss"], key=r["petg_ss"].get),
                   t_sink85_min=(r["t_fw"] or np.nan) / 60, t_sink95_min=(r["t_hw"] or np.nan) / 60,
                   t_tj110_min=(r["t_tj110"] or np.nan) / 60, t_cell60_min=(r["t_cell60"] or np.nan) / 60,
                   tj_pk50=r["tj_pk50"], cell_50_30min=r["cell_30"], main_50_30min=r["main_30"],
                   cell_ss50=r["ss50"]["CELL"], petg_max_ss50=max(r["petg_ss50"].values()),
                   t_sink95_50_min=(r["t_hw50"] or np.nan) / 60,
                   surf_max_5min_25C=max(val for k, val in r["surf_5min"].items() if not k.startswith("SINK (if")),
                   sink_5min_25C=r["surf_5min"]["SINK (if unguarded)"],
                   tj_favourable=stacks[L][0], tj_adverse=stacks[L][1],
                   duty_limit_setpoint=limits[L]["setpoint"], duty_max=limits[L]["dmax"],
                   tj_ss25=r["tj_ss25"], fr4_ew_ss45=max(r["fr4_ss"].values(), default=np.nan),
                   tj_inh_nom=limits[L]["tj_inh_nom"], tj_inh_tol=limits[L]["tj_inh_tol"],
                   tj_inh_adv=limits[L]["tj_inh_adv"], dl_sink=limits[L]["dl_sink"], dl_case=limits[L]["dl_case"],
                   dl_petg=limits[L]["dl_petg"], dl_petg_part=limits[L]["dl_petg_part"], dl_fr4=limits[L]["dl_fr4"],
                   dl_bay=limits[L]["dl_bay"], dl_main=limits[L]["dl_main"], dl_cell=limits[L]["dl_cell"])
        summary.append(row)
    with open(out / "summary.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(summary[0].keys()))
        w.writeheader()
        for row in summary:
            w.writerow({k: (f"{x:.3f}" if isinstance(x, float) else x) for k, x in row.items()})

    plot_catalog(out)
    plot_time(out, results, v)
    plot_duty(out, sweeps, limits, v)
    plot_surfaces(out, results, v)
    plot_petg_cells(out, results, limits, v)
    plot_tornado(out, tor)
    plot_network(out)
    lt = ltspice_check(out) if not a.no_ltspice else dict(ok=False, msg="skipped")

    # scripts as run
    sd = out / "scripts"
    sd.mkdir(exist_ok=True)
    for fn in ("thermal_model.py", "ts012_thermal.py"):
        shutil.copy2(HERE / fn, sd / fn)

    write_verdicts(out, results, summary, limits, stacks, tor, lt, v)
    print((out / "verdicts.md").read_text())


def write_verdicts(out, results, summary, limits, stacks, tor, lt, v):
    S = {r["layout"]: r for r in summary}

    def pf(ok):
        return "PASS" if ok else "FAIL"

    lines = ["# WP-PDR-28 thermal model, TS-012 finalists: results and verdicts", "",
             f"Run id `{out.name}`; model `hardware/sim/thermal/thermal_model.py`, runner `ts012_thermal.py` "
             "(copies in `scripts/`). Every number is an estimate from a lumped model whose inputs are classed in "
             "`inputs.csv` (D datasheet, DD derived from a datasheet, R requirement, E estimate).", "",
             "Corner (REQ-SYS-112): 45 C ambient, 8.4 V pack, ALC holding 5 W at the SMA, continuous key-down, "
             "steady state. REQ-SYS-113: 25 C ambient, 5 min continuous key-down from a soak.", "",
             "## Per layout", "",
             "| Metric | Limit | " + " | ".join(S) + " |", "|---|---|" + "---|" * len(S)]

    def row(name, lim, key, n=1, cmp=None):
        cells = []
        for L in S:
            x = S[L][key]
            txt = fmt(x, n) if isinstance(x, float) else str(x)
            if cmp is not None and isinstance(x, float) and not np.isnan(x):
                txt += f" {pf(cmp(x))}"
            cells.append(txt)
        lines.append(f"| {name} | {lim} | " + " | ".join(cells) + " |")

    row("PA dissipation at the corner, W", "-", "p_pa_W", 2)
    row("Junction, steady, continuous, C", "110", "tj_ss45", 1, lambda x: x <= v["tj_limit"])
    row("Junction, favourable stack of inputs, C", "110", "tj_favourable", 1, lambda x: x <= v["tj_limit"])
    row("Junction, adverse stack of inputs, C", "110", "tj_adverse", 1, lambda x: x <= v["tj_limit"])
    row("Module case (A5) or AFT05 tab (A4), C", "90 (A5 guidance)", "case_ss45", 1)
    row("Sink, steady, continuous, C", "85 / 95 trips", "sink_ss45", 1)
    row("Time to sink 85 C from soak, min", "-", "t_sink85_min", 1)
    row("Time to sink 95 C from soak, min", "-", "t_sink95_min", 1)
    row("Time to junction 110 C from soak, min", "-", "t_tj110_min", 1)
    row("Junction peak at 50 % duty (10 s on), C", "110", "tj_pk50", 1, lambda x: x <= v["tj_limit"])
    row("Max duty holding 110 C (10 s key-downs), fraction", "-", "duty_max", 2)
    row("Duty-limit sink setpoint S (refuse new key-down), C", "-", "duty_limit_setpoint", 1)
    row("Junction bound by the 85 C PA-case inhibit, nominal, C", "110", "tj_inh_nom", 1, lambda x: x <= v["tj_limit"])
    row("  same, trip at +3 C tolerance, C", "110", "tj_inh_tol", 1, lambda x: x <= v["tj_limit"])
    row("  same, +3 C and adverse dissipation and Rth, C", "110", "tj_inh_adv", 1, lambda x: x <= v["tj_limit"])
    row("Junction, continuous at 25 C ambient, C", "(info)", "tj_ss25", 1)
    row("Duty-limited corner: sink, C", "-", "dl_sink", 1)
    row("Duty-limited corner: module case / tab, C", "90 (A5)", "dl_case", 1)
    row("Duty-limited corner: hottest PETG, C", "60", "dl_petg", 1, lambda x: x <= v["petg_crit"])
    row("  which part", "-", "dl_petg_part", 1)
    row("Duty-limited corner: FR4 end wall, C", "105", "dl_fr4", 1, lambda x: x <= 105.0)
    row("Duty-limited corner: PA-bay air (relay, GVA), C", "-", "dl_bay", 1)
    row("Duty-limited corner: PA-bay air against the G5V-2 rating, C", "65", "dl_bay", 1, lambda x: x <= v["relay_amb"])
    row("Duty-limited corner: main-bay air, C", "55", "dl_main", 1, lambda x: x <= v["cell_crit_a"])
    row("Duty-limited corner: cells, steady, C", "55 / 60", "dl_cell", 1, lambda x: x <= v["cell_crit_a"])
    row("FR4 end wall, continuous, C", "105", "fr4_ew_ss45", 1, lambda x: x <= 105.0)
    row("PA-bay air (G5V-2 ambient rating 65 C), steady, continuous, C", "65", "bay_ss45", 1, lambda x: x <= v["relay_amb"])
    row("Hottest PETG hot face, continuous, C", "60 (HDT 69)", "petg_max_ss45", 1, lambda x: x <= v["petg_crit"])
    row("  which part", "-", "petg_max_part", 1)
    row("Hottest PETG hot face, 50 % duty steady, C", "60", "petg_max_ss50", 1, lambda x: x <= v["petg_crit"])
    row("Cells after 30 min at 50 % duty, C", "55 (a)", "cell_50_30min", 1, lambda x: x <= v["cell_crit_a"])
    row("Main-bay air after 30 min at 50 % duty, C", "55 (a)", "main_50_30min", 1, lambda x: x <= v["cell_crit_a"])
    row("Cells, 50 % duty steady (long session), C", "55", "cell_ss50", 1, lambda x: x <= v["cell_crit_a"])
    row("Cells, continuous steady, C", "60 trip (b)", "cell_ss45", 1)
    row("Time to cell 60 C trip, continuous, min", "-", "t_cell60_min", 1)
    row("Hottest accessible surface, 25 C, 5 min (rev 4: fin tips included), C", "48", "surf_max_5min_25C", 1,
        lambda x: x <= v["surf_limit"])
    row("Bare sink at 25 C, 5 min (needs the guard if > 48), C", "48", "sink_5min_25C", 1, lambda x: x <= v["surf_limit"])
    lines += ["", "## LTspice cross-check (A5-DC, electrical analogue)", ""]
    if lt.get("ok"):
        lines.append(f"LTspice 26.0.2 through tools/ltspice-batch.sh; deck SHA-256 `{lt['deck_sha256']}`; "
                     f"maximum difference to the Python solver after 30 s: **{lt['maxdiff']:.3f} K** "
                     f"(criterion 0.5 K): **{pf(lt['maxdiff'] <= 0.5)}**.")
        lines += ["", "| Node | LTspice at 7200 s | Python at 7200 s | Python steady | max diff K |", "|---|---|---|---|---|"]
        for n, d in lt["nodes"].items():
            lines.append(f"| {n} | {d['lt_end']:.2f} | {d['py_end']:.2f} | {d['ss']:.2f} | {d['maxdiff']:.3f} |")
    else:
        lines.append(f"Not run or failed: {lt}")
    lines += ["", "## Tornado (top five per metric)", ""]
    for (L, metric), (base, rows) in tor.items():
        lines.append(f"- {L} {metric} (base {base:.1f} C): " + "; ".join(
            f"{r['param']} [{r['cls']}] {r['out_low']:.1f} to {r['out_high']:.1f}" for r in rows[:5]))
    (out / "verdicts.md").write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
