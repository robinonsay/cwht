#!/usr/bin/env python3
"""WP-PDR-21 revision 4 (A5): the two Major findings of the independent review of revision 3, and only those (rule C1).

finding-1 (CK-ANA-B6/E3/F3/E5): revision 3's s2 applied half the 144 to 148 MHz in-unit span symmetrically, but the pad
    is chosen at 146 MHz, so the drive of a unit moves from its 146 MHz value by +0.36 / -0.78 dB, not +/-0.57 dB.
    Revision 4 (run s2): one-sided terms from the 146 MHz value; the target is re-centred for the one-sided band
    (18.2 mW, TBR) so that the +/-1.0 dB (TBR) reading allocation still holds 10 to 30 mW; the selection frequency
    146 MHz is stated. Revision 3's 17.3 mW is kept as an informative row (it needs +/-0.8 dB).
finding-2 (CK-ANA-A5/B6/E3/F3/H1): the clamp tops of revision 3 (D-9 at 8 W, scenario B at 10 W) were set on the
    typical-module curve; the datasheet gives no maximum and the margins were inside the +/-0.07 dB graph-read term.
    Revision 4 makes the ceiling a per-unit build step: the unit's open-loop output is read at build and the clamp is
    trimmed so that the unit's highest open-loop case makes the step target, ceiling x 10^(-g-/10), where g- covers the
    reading and the other step terms (step_guard). A unit read low by the full bound then makes the ceiling; a unit read
    high by the full bound makes the ceiling x 10^(-(g- + g+)/10), and that unit sets the reach (runs p4, p5). A unit
    whose clamp would fall outside the trim range is rejected at build, which bounds the upper spread. Run s4 shows
    the fixed-clamp alternative against the upper spread, the step's terms, a replica over the module spread and the
    reading break-even. Run s3 restates the REQ-SYS-012 basis and delta.

Usage (repo root, repo venv):
    .venv/bin/python hardware/sim/tx-pa/run_a5_r4.py all          # s2, p4, p5, s4, s3 in order
    .venv/bin/python hardware/sim/tx-pa/run_a5_r4.py s2|p4|p5|s4|s3
    add --expect to compare every verdict with the list of the analysis record section R4.10 (exit 3 on a change)

Inputs kept from revision 3 (not rerun; results/2026-09-29-r3-d6, -d7, -k1): the drive corners, the coax bound and the
17 mW reading bound. LTspice runs only through tools/ltspice-batch.sh (ACC-LTSPICE-001), by run_pa.run_ltspice. Every
value marked "est." is an estimate, not a datasheet or measured value.
"""
from __future__ import annotations

import itertools
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import run_a5_r3 as R3  # noqa: E402  (revision 3: d6, d7, k1 results, the feed reads, the module replica, helpers)
P = R3.P
from run_pa import plt, INK, INK2, GRID, COL  # noqa: E402

DATE = "2026-09-29"
REVISION = 4
RUNS4 = {
    "r4s2": f"{DATE}-r4-s2-sot-pad",
    "r4p4": f"{DATE}-r4-p4-power-a5-design",
    "r4p5": f"{DATE}-r4-p5-power-a5-clamp-b",
    "r4s4": f"{DATE}-r4-s4-clamp-step",
    "r4s3": f"{DATE}-r4-s3-req012-basis",
}
P.RUNS.update(RUNS4)
VERDICTS = P.VERDICTS
verdict = P.verdict
VKEY = {"r4s2": "s2", "r4p4": "p4", "r4p5": "p5", "r4s4": "s4", "r4s3": "s3"}   # verdict run names (record R4.10)


def rundir(k: str) -> Path:
    return P.rundir(k)


def copy_inputs(out: Path, decks: list[Path]):
    import shutil
    shutil.copy2(Path(__file__), out / Path(__file__).name)
    shutil.copy2(HERE / "run_a5_r3.py", out / "run_a5_r3.py")
    shutil.copy2(HERE / "run_pa.py", out / "run_pa.py")
    for d in decks:
        if d.parent != out:
            shutil.copy2(d, out / d.name)


def db(x):
    return float(10 * np.log10(x))


# ---------------------------------------------------------------- s2: select-on-test pad, one-sided terms (finding-1)
SEL_F_HZ = 146e6          # the pad is selected at 146 MHz (the reading of section R3.4 is taken there)
A5_PIN_MIN_MW, A5_PIN_MAX_MW = P.A5_PIN_MIN_MW, P.A5_PIN_MAX_MW


def run_s2():
    out = rundir("r4s2")
    rows = json.loads((R3.rundir("d6") / "corners.json").read_text())
    k1 = json.loads((R3.rundir("k1") / "result.json").read_text())
    d7 = json.loads((R3.rundir("d7") / "result.json").read_text())
    s2r3 = json.loads((R3.rundir("s2") / "result.json").read_text())
    pad18 = float(P.pad_loss_db(*P.PADS["a5_in"]))
    units = {}
    for r in rows:
        units.setdefault((r["rsrc"], r["gain"], r["p1db"], r["src"], r["coax_m"], r["bpf"], r["qbpf"]), {})[r["freq"]] = r["pin_pa_dbm"]
    # one-sided in-unit terms from the 146 MHz value (the value the pad is chosen on)
    ups = {k: max(v.values()) - v[SEL_F_HZ] for k, v in units.items()}
    dns = {k: v[SEL_F_HZ] - min(v.values()) for k, v in units.items()}
    up, dn = float(max(ups.values())), float(max(dns.values()))
    k_up, k_dn = max(ups, key=ups.get), max(dns, key=dns.get)
    fspan = float(max(max(v.values()) - min(v.values()) for v in units.values()))
    step_half, drift = float(s2r3["step_half_db"]), float(s2r3["drift_db"])   # the pad set's gap and drift terms, as r3
    meas = float(k1["reading_bound_db"])
    # target re-centred for the one-sided band: equal margins to 10 and 30 mW -> sqrt(10 x 30) x 10^((dn - up)/20)
    t_star = float(np.sqrt(A5_PIN_MIN_MW * A5_PIN_MAX_MW) * 10 ** ((dn - up) / 20))
    target = round(t_star, 1)

    def band(m, tgt=target):
        hi = up + step_half + m + drift
        lo = dn + step_half + m + drift
        mx, mn = tgt * 10 ** (hi / 10), tgt * 10 ** (-lo / 10)
        return {"meas_db": m, "target_mw": tgt, "up_db": hi, "down_db": lo, "min_mw": mn, "max_mw": mx,
                "overdrive_margin_db": db(A5_PIN_MAX_MW / mx), "underdrive_margin_db": db(mn / A5_PIN_MIN_MW),
                "pass": bool(mn >= A5_PIN_MIN_MW and mx <= A5_PIN_MAX_MW)}

    # pad set for the new target (the needed loss shifts by the target change); the set and its gap are re-derived
    tgt_dbm = float(P.dbm(target * 1e-3))
    need = [pad18 + (v[SEL_F_HZ] - tgt_dbm) for v in units.values()]
    pads = P.e24_pad_set(min(need), max(need))
    gaps = np.diff([q["loss_db"] for q in pads])
    step_half4 = float(gaps.max() / 2)
    if step_half4 > step_half + 1e-9:   # a wider gap would widen the band: carry it
        step_half = step_half4
    b = band(meas)
    b_alloc = band(P.SOT_MEAS_DB)
    b_r3_alloc = band(P.SOT_MEAS_DB, P.SOT_TARGET_MW)
    b_r3_m2 = band(meas, P.SOT_TARGET_MW)
    b_r3_08 = band(0.8, P.SOT_TARGET_MW)
    # break-even reading at each target (the smaller of the two margins reaches 0)
    def break_even(tgt):
        return float(min(db(A5_PIN_MAX_MW / tgt) - (up + step_half + drift), db(tgt / A5_PIN_MIN_MW) - (dn + step_half + drift)))
    res = {"run": RUNS4["r4s2"], "revision": REVISION, "drive_run": R3.RUNS3["d6"], "reading_run": R3.RUNS3["k1"],
           "selection_frequency_hz": SEL_F_HZ, "n_units": len(units),
           "in_unit_up_from_146_db": up, "in_unit_down_from_146_db": dn, "in_unit_span_db": fspan,
           "unit_up_worst": list(map(str, k_up)), "unit_down_worst": list(map(str, k_dn)),
           "step_half_db": step_half, "drift_db": drift, "reading_db": meas, "target_centre_mw": t_star, "target_mw": target,
           "pad_as_built_db": pad18, "pad_needed_db": [float(min(need)), float(max(need))], "pads": pads,
           "pad_set_max_gap_db": float(gaps.max()), "band": b, "band_at_allocation": b_alloc,
           "r3_target_at_allocation": b_r3_alloc, "r3_target_m2": b_r3_m2, "r3_target_at_0p8": b_r3_08,
           "reading_break_even_db": break_even(target), "reading_break_even_r3_target_db": break_even(P.SOT_TARGET_MW),
           "sensitivity": [band(m) for m in (0.25, 0.5, meas, 0.8, 1.0, 1.5, 2.0)],
           "revision3": {"target_mw": P.SOT_TARGET_MW, "band_mw": [s2r3["band"]["min_mw"], s2r3["band"]["max_mw"]],
                         "half_span_db": fspan / 2}}
    V = "s2"
    verdict(V, "A5 select-on-test drive 10 to 30 mW in service with the k1 reading bound (one-sided terms from 146 MHz, 18.2 mW target)",
            b["pass"], detail=f"{b['min_mw']:.2f} to {b['max_mw']:.2f} mW, margins {b['underdrive_margin_db']:+.2f} / {b['overdrive_margin_db']:+.2f} dB")
    verdict(V, "A5 select-on-test drive 10 to 30 mW at the +/-1.0 dB reading allocation (one-sided terms, 18.2 mW target)",
            b_alloc["pass"], detail=f"{b_alloc['min_mw']:.2f} to {b_alloc['max_mw']:.2f} mW")
    verdict(V, "Revision 3 target 17.3 mW at the +/-1.0 dB allocation with the one-sided terms (the finding-1 case)",
            b_r3_alloc["pass"], detail=f"{b_r3_alloc['min_mw']:.2f} to {b_r3_alloc['max_mw']:.2f} mW")
    verdict(V, "A5 select-on-test drive 10 to 30 mW with a tinySA Ultra reading alone (+/-2 dB published)",
            band(2.0)["pass"], detail=f"margins {band(2.0)['underdrive_margin_db']:+.2f} / {band(2.0)['overdrive_margin_db']:+.2f} dB")
    res["verdicts"] = VERDICTS.get(V, {})
    # plot
    from matplotlib.ticker import FixedLocator, NullLocator, ScalarFormatter
    fig, axs = plt.subplots(1, 2, figsize=(12.4, 5.2))
    ax = axs[0]
    ms = np.linspace(0, 2.2, 45)
    bs = [band(m, target) for m in ms]
    ax.fill_between(ms, [x["min_mw"] for x in bs], [x["max_mw"] for x in bs], color=COL["a5"], alpha=0.22,
                    label=f"in-service band, one-sided terms, target {target:.1f} mW (revision 4)")
    bs = [band(m, P.SOT_TARGET_MW) for m in ms]
    ax.plot(ms, [x["min_mw"] for x in bs], color=COL["a4"], lw=1.4, ls="--",
            label=f"band edges, one-sided terms, target {P.SOT_TARGET_MW} mW (revision 3)")
    ax.plot(ms, [x["max_mw"] for x in bs], color=COL["a4"], lw=1.4, ls="--")
    ax.axhline(30, color=INK, lw=1.3, label="30 mW: module maximum rating")
    ax.axhline(10, color=INK, lw=1.3, ls="--", label="10 mW: bottom of the stability window")
    ax.axvline(meas, color=COL["ok"], lw=1.6, label=f"k1 reading bound, method M2: +/-{meas:.2f} dB")
    ax.axvline(1.0, color=INK2, lw=1.0, ls=":", label="allocation +/-1.0 dB (TBR)")
    ax.axvline(res["reading_break_even_db"], color=COL["a5"], lw=0.9, ls=(0, (1, 1)),
               label=f"break-even at {target:.1f} mW: +/-{res['reading_break_even_db']:.2f} dB")
    ax.axvline(res["reading_break_even_r3_target_db"], color=COL["a4"], lw=0.9, ls=(0, (1, 1)),
               label=f"break-even at {P.SOT_TARGET_MW} mW: +/-{res['reading_break_even_r3_target_db']:.2f} dB")
    ax.set_yscale("log")
    ax.set_ylim(6, 50)
    ax.yaxis.set_major_locator(FixedLocator([6, 8, 10, 15, 20, 30, 40, 50]))
    ax.yaxis.set_minor_locator(NullLocator())
    ax.yaxis.set_major_formatter(ScalarFormatter())
    ax.set_xlim(0, 2.2)
    ax.set_xlabel("Level-reading uncertainty at the target (+/- dB)")
    ax.set_ylabel("Module input in service (mW)")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.15), ncol=2, fontsize=6.5)
    ax.set_title("r4-s2: select-on-test drive band, pad chosen at 146 MHz,\none-sided in-unit terms (+%.2f / -%.2f dB)" % (up, dn), fontsize=9)
    ax = axs[1]
    for yy, (lab, v1, v2) in zip((1, 0), (("above the 146 MHz value", up, up), ("below the 146 MHz value", dn, dn))):
        left = 0
        parts = [("frequency, one-sided from 146 MHz", v1), ("half the pad set's largest gap", step_half), ("level reading (k1, M2)", meas),
                 ("drift in service", drift)]
        for i, (pl, v) in enumerate(parts):
            ax.barh(yy, v, left=left, color=[INK2, COL["aux"], COL["ok"], COL["a4"]][i], label=(f"{pl}" if yy == 1 else None))
            left += v
        ax.text(left + 0.03, yy, f"{left:.2f} dB", va="center", fontsize=8)
    ax.plot([db(A5_PIN_MAX_MW / target)] * 2, [0.6, 1.4], color=INK, lw=1.4, label=f"room to 30 mW from {target:.1f} mW: {db(A5_PIN_MAX_MW / target):.2f} dB")
    ax.plot([db(target / A5_PIN_MIN_MW)] * 2, [-0.4, 0.4], color=INK, lw=1.4, ls="--", label=f"room to 10 mW from {target:.1f} mW: {db(target / A5_PIN_MIN_MW):.2f} dB")
    ax.set_yticks([1, 0])
    ax.set_yticklabels(["upward\n(toward 30 mW)", "downward\n(toward 10 mW)"], fontsize=8)
    ax.set_xlim(0, 3.2)
    ax.set_xlabel("Band edge from the target, worst-case sum (dB)")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.15), fontsize=7, ncol=2)
    ax.set_title(f"Terms per side at the M2 reading: band {b['min_mw']:.1f} to {b['max_mw']:.1f} mW", fontsize=9)
    fig.tight_layout()
    fig.savefig(out / "sot_band_r4.png", dpi=150)
    plt.close(fig)
    (out / "result.json").write_text(json.dumps(res, indent=1, default=float))
    L = [f"# {res['run']}: select-on-test pad on the D-13 bandpass chain, one-sided terms (revision 4, finding-1)", "",
         f"Units: {len(units)} (d6). The pad is chosen at {SEL_F_HZ / 1e6:.0f} MHz with the unit's own coax in place. Per unit the "
         f"drive over 144 to 148 MHz moves from its 146 MHz value by at most +{up:.3f} dB and -{dn:.3f} dB (revision 3 used "
         f"+/-{fspan / 2:.3f} dB, half the {fspan:.3f} dB span).", "",
         "| Term | Upward (dB) | Downward (dB) |", "|---|---|---|",
         f"| Frequency, one-sided from the 146 MHz value | {up:.3f} | {dn:.3f} |",
         f"| Half the pad set's largest gap | {step_half:.3f} | {step_half:.3f} |",
         f"| Level reading, k1 method M2 | {meas:.3f} | {meas:.3f} |",
         f"| Drift in service | {drift:.3f} | {drift:.3f} |",
         f"| **Sum** | **{b['up_db']:.3f}** | **{b['down_db']:.3f}** |", "",
         f"Target re-centred: sqrt(10 x 30) x 10^((down - up)/20) = {t_star:.2f} mW, taken as **{target:.1f} mW (TBR)**.", "",
         f"In service at {target:.1f} mW with the M2 reading: {b['min_mw']:.2f} to {b['max_mw']:.2f} mW, margins "
         f"{b['underdrive_margin_db']:+.2f} dB above 10 mW and {b['overdrive_margin_db']:+.2f} dB below 30 mW: **{'PASS' if b['pass'] else 'FAIL'}**.",
         f"At the +/-1.0 dB allocation: {b_alloc['min_mw']:.2f} to {b_alloc['max_mw']:.2f} mW (**{'PASS' if b_alloc['pass'] else 'FAIL'}**). "
         f"Break-even reading +/-{res['reading_break_even_db']:.2f} dB.",
         f"Revision 3 target {P.SOT_TARGET_MW} mW with the one-sided terms: M2 {b_r3_m2['min_mw']:.2f} to {b_r3_m2['max_mw']:.2f} mW; "
         f"+/-1.0 dB {b_r3_alloc['min_mw']:.2f} to {b_r3_alloc['max_mw']:.2f} mW (**{'PASS' if b_r3_alloc['pass'] else 'FAIL'}**); "
         f"+/-0.8 dB {b_r3_08['min_mw']:.2f} to {b_r3_08['max_mw']:.2f} mW; break-even +/-{res['reading_break_even_r3_target_db']:.2f} dB.", "",
         f"Pad losses needed at {target:.1f} mW: {min(need):.2f} to {max(need):.2f} dB. Pad set ({len(pads)} E24 1 % pi pads, largest gap "
         f"{gaps.max():.2f} dB):", "", "| Loss (dB) | Shunt, series, shunt (ohm) | Return loss (dB) |", "|---|---|---|"]
    for q in pads:
        L.append(f"| {q['loss_db']:.2f} | {q['shunt']:g}, {q['series']:g}, {q['shunt']:g} | {q['rl_db']:.1f} |")
    L += ["", "| Reading uncertainty (dB) | Band at the target (mW) | Margin above 10 mW (dB) | Margin below 30 mW (dB) | Verdict |", "|---|---|---|---|---|"]
    for x in res["sensitivity"]:
        L.append(f"| +/-{x['meas_db']:.2f} | {x['min_mw']:.2f} to {x['max_mw']:.2f} | {x['underdrive_margin_db']:+.2f} | {x['overdrive_margin_db']:+.2f} | {'PASS' if x['pass'] else 'FAIL'} |")
    L += ["", "Plot `sot_band_r4.png`.", ""]
    (out / "result.md").write_text("\n".join(L))
    copy_inputs(out, [])
    print("s2", json.dumps({k: res[k] for k in ("in_unit_up_from_146_db", "in_unit_down_from_146_db", "target_centre_mw", "target_mw",
                                                 "band", "band_at_allocation", "r3_target_at_allocation", "reading_break_even_db")}, default=float))
    return res


# ---------------------------------------------------------------- the per-unit clamp step (finding-2)
# The build step (proposed; the circuit that makes the clamp trimmable is WP-PDR-22's): with the ALC held at its top
# (firmware test mode, VGG at the clamp), the bench supply at 8.4 V through the pack-resistance fixture, the unit into
# the dummy load at 18 to 28 C, the open-loop power at the SMA is read with the diode probe at 144.05, 146.00 and
# 147.95 MHz (3 s key-down each). The unit's module output is that reading plus the unit's own output loss (NanoVNA
# S21, TC-TX-009 to 011). The model of this record projects it to the unit's highest open-loop case in service (the
# -10 C start and the 25 C start of a key-down); the clamp is trimmed so that projection makes the step target,
# ceiling_design x 10^(-g-/10); the reading is repeated after the trim. A unit whose clamp would have to go below the
# trim range is rejected at build. The terms of the step (worst-case sum; e is read minus true, dB):
STEP_READ_REL = 0.15            # TC-SYS-010 acceptance bound: combined probe power uncertainty at most 15 % (the case's
                                # criterion; the characterized value replaces it at build if smaller)
STEP_TERMS_OTHER = [            # (term, dB, class)
    ("unit output loss (LPF and relay) from the NanoVNA S21 at 144, 146 and 148 MHz", 0.10, "est."),
    ("trim resolution: half of a 0.1 dB step", 0.05, "est.; WP-PDR-22 sets the step"),
    ("RA07M1317M curve graph read (VGG and VDD curves, from the bench point to the service cases)", 0.07, "est., revision 2 term"),
    ("bench temperature and self-heating during the 3 s reading, projected to the service case", 0.05, "est."),
]
STEP_X_TOP_DB = 1.5             # trim range: a module up to +1.5 dB above the typical curve (est.); above it, rejected
CEIL = {"r4p4": (8.0, 7.9), "r4p5": (10.0, 9.9)}   # (ceiling W, design value W): D-9 as specified, clamp scenario B


def step_guard(s2: dict, read_rel: float = STEP_READ_REL) -> dict:
    """The step's error bound, one-sided: g_minus (the unit read low: the clamp too high) and g_plus (read high)."""
    T = P.a5_tables()
    # drive drift in service against the drive at the step, times the module's Pout-Pin slope at the top of the band
    pmax = float(P.dbm(s2["band"]["max_mw"] * 1e-3))
    sl = 0.0
    for f in P.FREQS:
        w = (f - 135e6) / 20e6
        pt = lambda p: (1 - w) * 10 ** (np.interp(p, T["xp"], T["p135"]) / 10) + w * 10 ** (np.interp(p, T["xp"], T["p155"]) / 10)
        sl = max(sl, abs(db(pt(pmax + s2["drift_db"]) / pt(pmax))), abs(db(pt(pmax) / pt(pmax - s2["drift_db"]))))
    other = [list(t) for t in STEP_TERMS_OTHER] + [["drive drift in service (s2 drift %.2f dB) times the module Pout-Pin slope at %.1f mW" %
                                                    (s2["drift_db"], s2["band"]["max_mw"]), sl, "digitized curve (est.)"]]
    so = float(sum(t[1] for t in other))
    r_lo = db(1 / (1 - read_rel)) if read_rel < 1 else 99.0   # read low by 15 %: the true value is 1/0.85 of the reading
    r_hi = db(1 + read_rel)
    return {"read_rel": read_rel, "read_low_db": r_lo, "read_high_db": r_hi, "other": other, "other_sum_db": so,
            "g_minus_db": r_lo + so, "g_plus_db": r_hi + so}


def unit_cases(g: dict) -> list[tuple[str, str, float, float]]:
    """(label, base, true spread dB, error e dB): the step believes the unit is x + e."""
    gm, gp = g["g_minus_db"], g["g_plus_db"]
    return [("typical, read exactly", "typ", 0.0, 0.0),
            ("typical, read high by the bound", "typ", 0.0, gp),
            ("typical, read low by the bound", "typ", 0.0, -gm),
            (f"+{STEP_X_TOP_DB:g} dB (trim-range top), read high", "typ", STEP_X_TOP_DB, gp),
            (f"+{STEP_X_TOP_DB:g} dB (trim-range top), read low", "typ", STEP_X_TOP_DB, -gm),
            ("datasheet minimum, read high", "min", 0.0, gp),
            ("datasheet minimum, read low", "min", 0.0, -gm)]


XG4 = np.round(np.arange(2.30, 3.601, 0.05), 3)   # VGG grid (revision 3 started at 2.40 V; the digitized curve starts at 2.27 V)


def vgg_tables4():
    g135 = P.resample(P.load_curve("ra07_pout_vs_vgg_135"), XG4, 0.015)
    g155 = P.resample(P.load_curve("ra07_pout_vs_vgg_155"), XG4, 0.015)
    return XG4, g135, g155


def model_consts():
    """Per frequency: w, the relative VGG curve kv_f(x) = gv_f(x)/gv_f(3.5) on XG4, the datasheet-minimum factor."""
    T = P.a5_tables()
    xg, g135, g155 = vgg_tables4()
    out = {}
    for f in P.FREQS:
        w = (f - 135e6) / 20e6
        gv = (1 - w) * g135 + w * g155
        gref = (1 - w) * np.interp(3.5, xg, g135) + w * np.interp(3.5, xg, g155)
        v72 = (1 - w) * np.interp(7.2, T["xv"], T["v135"]) + w * np.interp(7.2, T["xv"], T["v155"])
        out[f] = {"w": w, "kv": gv / gref, "kmin": P.A5_POUT_MIN_72 / v72}
    return T, xg, g135, g155, out


KT_OPEN = {k: 10 ** (P.tc_by_key(k)[5] * (P.tc_by_key(k)[4] - 25.0) / 10) for k in ("coldhi", "t25soak")}   # fixed case


def pv_f(T, w, x):
    return (1 - w) * np.interp(x, T["xv"], T["v135"]) + w * np.interp(x, T["xv"], T["v155"])


def kd_f(T, w, pin_dbm):
    pt = lambda p: (1 - w) * 10 ** (np.interp(p, T["xp"], T["p135"]) / 10) + w * 10 ** (np.interp(p, T["xp"], T["p155"]) / 10)
    return pt(pin_dbm) / pt(13.0103)


def clamp_top_unit(vp, eta, pin_dbm, lv, base, xa_db, tgt, T, mc):
    """The per-unit clamp top (the checker's form of the deck's Bvg): the VGG at which the believed unit (base, x + e)
    makes tgt at its highest open-loop case (-10 C start, 25 C start), minimum over the three frequencies, capped at
    3.50 V. Closed form: at the target the drain voltage solves vd^2 - (Vp - rf IBUS) vd + rf tgt / eta = 0."""
    vp = np.asarray(vp, dtype=float)
    top = np.full(vp.shape, 3.5)
    for key in ("coldhi", "t25soak"):
        rf = R3.feed3_at(key, lv)
        a = vp - rf * P.IBUS
        vd = 0.5 * (a + np.sqrt(np.maximum(a * a - 4 * rf * tgt / eta, 0.0)))
        for f in P.FREQS:
            c = mc[f]
            ks = (c["kmin"] if base == "min" else 1.0) * 10 ** (xa_db / 10)
            need = tgt / (pv_f(T, c["w"], np.maximum(vd, 3.0)) * kd_f(T, c["w"], pin_dbm) * ks * KT_OPEN[key])
            top = np.minimum(top, np.interp(need, c["kv"], XG4))
    return top


def module_vec(vp, rf, eta, pin_dbm, f, vgg, ks, tc_key, T, xg, g135, g155, iters=120):
    """Vectorized replica of the deck's module model (every argument may be an array of one shape)."""
    vp, rf, eta, pin_dbm, f, vgg, ks = [np.asarray(a, dtype=float) for a in (vp, rf, eta, pin_dbm, f, vgg, ks)]
    tc = P.tc_by_key(tc_key)
    w = (f - 135e6) / 20e6
    pv = lambda x: (1 - w) * np.interp(x, T["xv"], T["v135"]) + w * np.interp(x, T["xv"], T["v155"])
    pt = lambda p: (1 - w) * 10 ** (np.interp(p, T["xp"], T["p135"]) / 10) + w * 10 ** (np.interp(p, T["xp"], T["p155"]) / 10)
    kd = pt(pin_dbm) / pt(13.0103)
    gv = lambda v: (1 - w) * np.interp(v, xg, g135) + w * np.interp(v, xg, g155)
    kv = gv(vgg) / gv(3.5)
    vd = np.array(vp)
    pm = np.zeros(np.broadcast(vp, rf, eta, pin_dbm, f, vgg, ks).shape)
    for _ in range(iters):
        tcc = tc[4] if tc[4] is not None else tc[2] + P.RTH_CA["a5"] * (pm * (1 / eta - 1) + 10 ** ((pin_dbm - 30) / 10))
        dt = np.asarray(tcc) - 25.0
        kt = 10 ** (tc[5] * (np.maximum(dt, 0) if tc[6] else dt) / 10)
        pm = pv(np.maximum(vd, 3.0)) * kd * kv * ks * kt
        vd = 0.5 * vd + 0.5 * (vp - rf * (P.IBUS + pm / (eta * np.maximum(vd, 1.0))))
    return pm


# ---------------------------------------------------------------- p4 / p5 (revision 4): the deck with the per-unit clamp
FEED3_LEVELS = R3.FEED3_LEVELS
LOSS3, LOSS3_DESIGN = R3.LOSS3, R3.LOSS3_DESIGN
OFFS = {"r4p4": R3.VGG_OFF, "r4p5": R3.CLAMPB_OFF}
STEP_SET = ("typical, read exactly", "typical, read high by the bound", "typical, read low by the bound",
            f"+{STEP_X_TOP_DB:g} dB (trim-range top), read high", f"+{STEP_X_TOP_DB:g} dB (trim-range top), read low")
MIN_SET = ("datasheet minimum, read high", "datasheet minimum, read low")


def deck_p4r4(out: Path, key: str, pins: list[float], units, tgt: float) -> tuple[Path, list[dict]]:
    offs = OFFS[key]
    T, xg, g135, g155, mc = model_consts()
    dims = [("irf", [l[0] for l in FEED3_LEVELS]), ("ieta", P.A5_ETA), ("ipin", pins), ("ifr", P.FREQS), ("ivgg", offs),
            ("iu", [u[0] for u in units]), ("itc", [c[0] for c in P.TC_CASES])]
    n = int(np.prod([len(v) for _, v in dims]))
    radix, lines = 1, []
    for name, vals in dims:
        lines.append(f".param {name}=floor(idx/{radix})-{len(vals)}*floor(idx/{radix * len(vals)})")
        radix *= len(vals)
    corners = []
    for combo in itertools.product(*[range(len(v)) for _, v in dims][::-1]):
        combo = combo[::-1]
        c = {name: vals[k] for (name, vals), k in zip(dims, combo)}
        c["rf_ohm"] = R3.feed3_at(c["itc"], [l[0] for l in FEED3_LEVELS].index(c["irf"]))
        corners.append(c)
    def tab(name, vals, fmt="{:.6g}"):
        return f".param {name[1:]}=table({name}," + ",".join(f"{i},{fmt.format(v)}" for i, v in enumerate(vals)) + ")"
    def tctab(pname, vals):
        return f".param {pname}=table(itc," + ",".join(f"{i},{v:.6g}" for i, v in enumerate(vals)) + ")"
    rf_flat = [R3.feed3_at(tc[0], lv) for tc in P.TC_CASES for lv in range(len(FEED3_LEVELS))]
    te = lambda var, xs, ys, fmt="{:.7g}": P.table_expr(var, xs, ys, fmt)   # 7 digits: the clamp inversion is sensitive on the flat top of the VGG curve
    vt135, vt155 = te("x", T["xv"], T["v135"]), te("x", T["xv"], T["v155"])
    pt135, pt155 = te("pin", T["xp"], T["p135"]), te("pin", T["xp"], T["p155"])
    pr135, pr155 = te("13.0103", T["xp"], T["p135"]), te("13.0103", T["xp"], T["p155"])
    gx135, gx155 = te("x", xg, g135), te("x", xg, g155)
    gh135, gh155 = te("3.5", xg, g135), te("3.5", xg, g155)
    v72_135, v72_155 = te("7.2", T["xv"], T["v135"]), te("7.2", T["xv"], T["v155"])
    fl = [f"{f / 1e6:.0f}" for f in P.FREQS]
    kdf, ksf, invf = [], [], []
    for f, fs in zip(P.FREQS, fl):
        c = mc[f]
        w = c["w"]
        kdf.append(f".param kd{fs}=((1-{w:g})*pow(10,{pt135}/10)+{w:g}*pow(10,{pt155}/10))/((1-{w:g})*pow(10,{pr135}/10)+{w:g}*pow(10,{pr155}/10))")
        ksf.append(f".param ksa{fs}=if(ubase>0.5,{c['kmin']:.6g},1)*pow(10,ua/10)")
        invf.append(f".func inv{fs}(y)=" + te("y", c["kv"], xg, fmt="{:.6g}"))
    rfc = [R3.feed3_at("coldhi", lv) for lv in range(len(FEED3_LEVELS))]
    rfs = [R3.feed3_at("t25soak", lv) for lv in range(len(FEED3_LEVELS))]
    tops = []
    for fs, f in zip(fl, P.FREQS):
        w = mc[f]["w"]
        for rn, ktn in (("rfc", "ktc"), ("rfs", "kts")):
            tops.append(f"inv{fs}(need(x,{rn},{w:g},kd{fs},ksa{fs},{ktn}))")
    topexpr = "3.5"
    for t in tops:
        topexpr = f"min({topexpr},{t})"
    ceil_w, design_w = CEIL[key]
    txt = f"""* power_a5_step.cir: A5 RA07M1317M, output power at the SMA versus pack voltage, per-unit clamp step (revision 4)
* (cwht WP-PDR-21 revision 4, hardware/sim/tx-pa/run_a5_r4.py {VKEY[key]}; record docs/design/analysis/pa-drive-ts012.md section R4)
* As revision 3 (power_a5_design.cir) with: the drive band of r4-s2 ({', '.join(f'{10 ** (p / 10):.2f}' for p in pins)} mW);
* the clamp top set per unit by the build step: VGG(Vp) = top(Vp) + offset, top(Vp) the VGG at which the unit the step
* believes (base, spread ua = ux + e dB) makes tgt = {tgt:.5g} W at its highest open-loop case (-10 C start and 25 C
* start, each of 144, 146, 148 MHz, the unit's own feed, efficiency and drive), capped at 3.50 V; closed form below.
* tgt = {design_w} W x 10^(-g-/10) for the {ceil_w:g} W ceiling. Offsets {', '.join(f'{o:g}' for o in offs)} V.
* Unit cases (iu): {'; '.join(f'{i} {u[0]} (x {u[2]:+.3f}, e {u[3]:+.3f} dB)' for i, u in enumerate(units))}.
* The output loss (LPF plus relay, {LOSS3} dB, with the copper term cu per temperature case) scales the module output only:
* the checker applies it to V(pmod) (power at the SMA = V(pmod) x 10^(-(loss + (loss - {P.LOSS_RELAY_DB}) cu)/10)), as revision 3's Bsma did.
* {n} corners flattened into one .step (idx), first dimension fastest: {', '.join(d for d, _ in dims)}.
.param idx=0
.step param idx 0 {n - 1} 1
{chr(10).join(lines)}
* temperature cases (itc): {'; '.join(f'{i} {tc[1]}' for i, tc in enumerate(P.TC_CASES))}
.param rf=table(itc*{len(FEED3_LEVELS)}+irf,{','.join(f'{i},{v:.5g}' for i, v in enumerate(rf_flat))})
.param rfc=table(irf,{','.join(f'{i},{v:.5g}' for i, v in enumerate(rfc))})
.param rfs=table(irf,{','.join(f'{i},{v:.5g}' for i, v in enumerate(rfs))})
{tctab('ta', [tc[2] for tc in P.TC_CASES])}
{tctab('tcfix', [tc[4] if tc[4] is not None else -999 for tc in P.TC_CASES])}
{tctab('coef', [tc[5] for tc in P.TC_CASES])}
{tctab('ng', [1 if tc[6] else 0 for tc in P.TC_CASES])}
{tctab('cu', [P.copper_db_per_db(tc) for tc in P.TC_CASES])}
.param rth={P.RTH_CA['a5']}
.param pinw_pa=pow(10,(pin-30)/10)
{tab('ipin', pins)}
{tab('ifr', P.FREQS)}
{tab('ivgg', offs)}
{tab('ieta', P.A5_ETA)}
.param ubase=table(iu,{','.join(f'{i},{1 if u[1] == "min" else 0}' for i, u in enumerate(units))})
.param ux=table(iu,{','.join(f'{i},{u[2]:.6g}' for i, u in enumerate(units))})
.param ua=table(iu,{','.join(f'{i},{u[2] + u[3]:.6g}' for i, u in enumerate(units))})
.param tgt={tgt:.6g}
.param ktc={KT_OPEN['coldhi']:.6g}
.param kts={KT_OPEN['t25soak']:.6g}
.param w=(fr-135e6)/20e6
* drive factor: datasheet Pout-Pin curves at 7.2 V, relative to Pin 20 mW
.param kd=((1-w)*pow(10,{pt135}/10)+w*pow(10,{pt155}/10))/((1-w)*pow(10,{pr135}/10)+w*pow(10,{pr155}/10))
* spread factor of the true unit: typical curve, or datasheet minimum 6.5 W at 7.2 V, times 10^(ux/10)
.param kmin={P.A5_POUT_MIN_72}/((1-w)*{v72_135}+w*{v72_155})
.param ks=if(ubase>0.5,kmin,1)*pow(10,ux/10)
.func pv(x)=(1-w)*{vt135}+w*{vt155}
.func gv(x)=(1-w)*{gx135}+w*{gx155}
.param gref=(1-w)*{gh135}+w*{gh155}
* per-unit clamp (the build step): per frequency, the believed unit's drive factor, spread factor and inverse VGG curve
{chr(10).join(kdf)}
{chr(10).join(ksf)}
{chr(10).join(invf)}
.func pvw(x,ww)=(1-ww)*{vt135}+ww*{vt155}
.func vdq(x,r)=0.5*((x-r*{P.IBUS})+sqrt(max(pow(x-r*{P.IBUS},2)-4*r*tgt/eta,0)))
.func need(x,r,ww,kdw,ksw,ktw)=tgt/(pvw(max(vdq(x,r),3),ww)*kdw*ksw*ktw)
.func topc(x)={topexpr}
Btc tc 0 V=if(tcfix>-500,tcfix,ta+rth*(V(pmod)*(1/eta-1)+pinw_pa))
Rtc tc 0 1meg
.func kt(t)=pow(10,coef*if(ng>0.5,max(t-25,0),t-25)/10)
Bvg vg 0 V=topc(V(p))+vgg
Rvg vg 0 1meg
Bmod pmod 0 V=pv(max(V(d),3))*kd*gv(V(vg))/gref*ks*kt(V(tc))
Rmod pmod 0 1meg
Bpa d 0 I=V(pmod)/(eta*max(V(d),1))
Vp p 0 7.4
Rf p d {{rf}}
Ibus d 0 {P.IBUS}
.dc Vp 6.4 8.4 0.05
.save V(d) V(pmod) V(tc) V(vg) I(Vp)
.end
"""
    pth = out / "power_a5_step.cir"
    pth.write_text(txt)
    return pth, corners


def run_p4r4(key: str):
    import os
    out = rundir(key)
    V = VKEY[key]
    s2 = json.loads((rundir("r4s2") / "result.json").read_text())
    g = step_guard(s2)
    units = unit_cases(g)
    ceil_w, design_w = CEIL[key]
    tgt = design_w * 10 ** (-g["g_minus_db"] / 10)
    pins = [float(P.dbm(s2["band"]["min_mw"] * 1e-3)), float(P.dbm(s2["target_mw"] * 1e-3)), float(P.dbm(s2["band"]["max_mw"] * 1e-3))]
    offs = OFFS[key]
    deck, corners = deck_p4r4(out, key, pins, units, tgt)
    os.environ.setdefault("CWHT_LTSPICE_LOCK_WAIT", "14400")
    prov = P.run_ltspice(deck, out, timeout=14400)
    (out / "result.json").write_text(json.dumps({"run": RUNS4[key], "ltspice": prov}))   # lets CWHT_PA_REPLOT=1 re-read this .raw
    from spicelib import RawRead
    raw = RawRead(str(out / "power_a5_step.raw"))
    nst = len(raw.get_steps())
    verdict(V, "check: one .raw step per corner", nst == len(corners), "check", f"{nst} steps")
    vp = np.abs(raw.get_trace(raw.get_trace_names()[0]).get_wave(0))
    M = np.array([raw.get_trace("V(pmod)").get_wave(i) for i in range(nst)])
    TCW = np.array([raw.get_trace("V(tc)").get_wave(i) for i in range(nst)])
    VG = np.array([raw.get_trace("V(vg)").get_wave(i) for i in range(nst)])
    IP = np.array([np.abs(raw.get_trace("I(Vp)").get_wave(i)) for i in range(nst)])
    corners_deck = corners
    i64, i84 = int(np.argmin(np.abs(vp - 6.4))), int(np.argmin(np.abs(vp - 8.4)))
    ulab = np.array([c["iu"] for c in corners])
    uidx = {u[0]: u for u in units}
    # checks: thermal law; the deck clamp against the checker's closed form; the clamp makes the step target
    dev = 0.0
    for i, c in enumerate(corners):
        tc = P.tc_by_key(c["itc"])
        if tc[4] is None:
            want = tc[2] + P.RTH_CA["a5"] * (M[i] * (1 / c["ieta"] - 1) + 10 ** ((c["ipin"] - 30) / 10))
            dev = max(dev, float(np.max(np.abs(want - TCW[i]))))
    verdict(V, "check: PA case temperature equals the thermal law within 0.01 K at every pack voltage", dev <= 0.01, "check",
            f"largest difference {dev:.2e} K")
    T, xg, g135, g155, mc = model_consts()
    lvs = [l[0] for l in FEED3_LEVELS]
    top_py = {}
    dv = 0.0
    for i, c in enumerate(corners):
        u = uidx[c["iu"]]
        kk = (c["irf"], c["ieta"], c["ipin"], c["iu"])
        if kk not in top_py:
            top_py[kk] = clamp_top_unit(vp, c["ieta"], c["ipin"], lvs.index(c["irf"]), u[1], u[2] + u[3], tgt, T, mc)
        want = top_py[kk] + c["ivgg"]
        dv = max(dv, float(np.max(np.abs(VG[i] - want) / (1e-3 * np.abs(want) + 1e-4))))
    verdict(V, "check: the deck clamp equals the checker's per-unit clamp within LTspice's reltol (0.1 % + 0.1 mV) at every pack voltage",
            dv <= 1.0, "check", f"largest difference {dv:.2f} of the tolerance")
    vgmax = float(VG.max())
    verdict(V, "check: VGG at most 3.50 V at every corner and pack voltage", vgmax <= 3.5 + 1e-4, "check", f"highest {vgmax:.4f} V")
    # identity: a unit read exactly makes tgt at its highest open-loop case where its clamp is below 3.50 V
    tck = np.array([c["itc"] for c in corners])
    off0 = np.array([c["ivgg"] == 0.0 for c in corners])
    exact = ulab == "typical, read exactly"
    idn = []
    for kk, top in top_py.items():
        if kk[3] != "typical, read exactly":
            continue
        m = off0 & exact & np.isin(tck, ["coldhi", "t25soak"]) & np.array([(c["irf"], c["ieta"], c["ipin"]) == kk[:3] for c in corners])
        hi = M[m].max(axis=0)
        sel = top < 3.5 - 1e-6
        if sel.any():
            idn.append(float(np.max(np.abs(hi[sel] / tgt - 1))))
    idn_max = max(idn) if idn else 0.0
    verdict(V, "check: a unit read exactly makes the step target at its highest open-loop case where its clamp is below 3.50 V (within 0.2 %)",
            idn_max <= 0.002, "check", f"largest deviation {idn_max * 100:.3f} %")
    hit_floor = float(min(t.min() for t in top_py.values()) + min(offs))
    verdict(V, "check: every clamp VGG (top plus window offset) above the VGG grid floor (2.30 V)", hit_floor > XG4[0] + 1e-6, "check",
            f"lowest {hit_floor:.3f} V")
    # expand the deck corners by the output-loss dimension (the checker applies the loss; revision 3's deck did it in Bsma)
    rep = np.repeat(np.arange(len(corners_deck)), len(LOSS3))
    corners = [dict(c, iloss=L) for c in corners_deck for L in LOSS3]
    cu = np.array([P.copper_db_per_db(P.tc_by_key(c["itc"])) for c in corners])
    loss = np.array([c["iloss"] for c in corners])
    kl = 10 ** (-(loss + (loss - P.LOSS_RELAY_DB) * cu) / 10)
    M, TCW, VG, IP = M[rep], TCW[rep], VG[rep], IP[rep]
    S = M * kl[:, None]
    ulab = np.array([c["iu"] for c in corners])
    tck = np.array([c["itc"] for c in corners])
    exact = ulab == "typical, read exactly"
    rfl = np.array([c["irf"] for c in corners])
    design = np.isin(rfl, ["low", "mid", "bound"]) & np.isin(loss, LOSS3_DESIGN)
    step = np.isin(ulab, STEP_SET)
    mins = np.isin(ulab, MIN_SET)
    readhi = np.isin(ulab, ["typical, read high by the bound", f"+{STEP_X_TOP_DB:g} dB (trim-range top), read high"])
    nomd = dict(irf="mid", ieta=0.60, ipin=pins[1], ifr=146e6, ivgg=offs[1], iu="typical, read exactly", iloss=0.84)
    kd_cases = [tc[0] for tc in P.TC_CASES if tc[3] == "kd"]
    def lo_at(mask, col):
        ii = np.where(mask)[0]
        j = int(ii[np.argmin(S[ii, col])])
        return float(S[j, col]), corners[j], float(TCW[j, col])
    def reach(curve):
        ok = curve >= P.REQ012_LO
        return round(float(vp[np.argmax(ok)]), 2) if ok.any() else None
    by = {}
    for tc in P.TC_CASES:
        k = tc[0]
        m = tck == k
        inom = next(i for i, c in enumerate(corners) if c["itc"] == k and all(c[a] == b for a, b in nomd.items()))
        d = {"label": tc[1], "feed_ohm": {l[0]: R3.feed3_at(k, j) for j, l in enumerate(FEED3_LEVELS)}}
        sets = {
            "low_step_lpfmed": m & step & design & (loss <= 0.84 + 1e-9),
            "low_step_lpf99": m & step & design & (loss <= 1.03 + 1e-9),
            "low_step_lpfworst": m & step & design,
            "low_exact_lpf99": m & exact & design & (loss <= 1.03 + 1e-9),
            "low_readhi_lpf99": m & readhi & design & (loss <= 1.03 + 1e-9),
            "low_min_lpfmed": m & mins & design & (loss <= 0.84 + 1e-9),
            "low_min_lpf99": m & mins & design & (loss <= 1.03 + 1e-9),
            "low_min_lpfworst": m & mins & design,
            "lever_pfet_step_lpfworst": m & step & np.isin(rfl, ["low", "mid", "lever"]) & np.isin(loss, LOSS3_DESIGN),
            "lever_both_step": m & step & np.isin(rfl, ["low", "mid", "lever"]) & np.isin(loss, [0.84, 1.03, 1.34]),
        }
        d["at_6v4"] = {"nominal_w": float(S[inom, i64]), "nominal_pa_case_c": float(TCW[inom, i64])}
        d["at_8v4"] = {"nominal_w": float(S[inom, i84])}
        d["curves"] = {"nominal": S[inom].tolist()}
        d["reach_3v97"] = {"nominal": reach(S[inom])}
        d["corners"] = {"nominal": corners[inom]}
        for nm, mask in sets.items():
            w64, c64, t64 = lo_at(mask, i64)
            curve = S[mask].min(axis=0)
            d["at_6v4"][nm + "_w"] = w64
            d["at_6v4"][nm + "_margin_db"] = db(w64 / P.REQ012_LO)
            d["at_6v4"][nm + "_pa_case_c"] = t64
            d["at_8v4"][nm + "_w"] = float(curve[i84])
            d["curves"][nm] = curve.tolist()
            d["reach_3v97"][nm] = reach(curve)
            d["corners"][nm] = c64
        d["module_high_curve_w"] = M[m].max(axis=0).tolist()
        d["module_high_step_curve_w"] = M[m & (step | mins)].max(axis=0).tolist()
        d["pack_current_max_a"] = float(IP[m & design].max())
        by[k] = d
    unc_lo = sum(u[1] for u in P.CLOSURE_UNC)
    unc_hi = sum(u[2] for u in P.CLOSURE_UNC)
    per_unit_high = {u[0]: float(M[ulab == u[0]].max()) for u in units}
    res = {"run": RUNS4[key], "revision": REVISION, "ltspice": prov, "n_corners": len(corners), "n_deck_steps": len(corners_deck), "vpack": vp.tolist(),
           "pins_dbm": pins, "pins_mw": [10 ** (p / 10) for p in pins], "ceiling_w": ceil_w, "design_w": design_w,
           "step_guard": g, "step_target_w": tgt, "units": units, "vgg_offsets": offs, "loss_db": LOSS3,
           "feed_levels": lvs, "feed_25c_ohm": {l[0]: R3.feed3_at(None, j) for j, l in enumerate(FEED3_LEVELS)},
           "unmodelled_db": [unc_lo, unc_hi], "by_tc": by, "kd_cases": kd_cases, "module_high_per_unit_w": per_unit_high,
           "vg_6v4_range": [float(VG[:, i64].min()), float(VG[:, i64].max())], "vg_8v4_range": [float(VG[:, i84].min()), float(VG[:, i84].max())],
           "clamp_top_8v4_per_unit": {u[0]: [float(min(t[i84] for kk, t in top_py.items() if kk[3] == u[0])),
                                             float(max(t[i84] for kk, t in top_py.items() if kk[3] == u[0]))] for u in units},
           "clamp_top_6v4_per_unit": {u[0]: [float(min(t[i64] for kk, t in top_py.items() if kk[3] == u[0])),
                                             float(max(t[i64] for kk, t in top_py.items() if kk[3] == u[0]))] for u in units}}
    worst = lambda kk: float(min(by[k]["at_6v4"][kk] for k in kd_cases))
    for kk in ("nominal_w", "low_step_lpfmed_w", "low_step_lpf99_w", "low_step_lpfworst_w", "low_exact_lpf99_w", "low_readhi_lpf99_w",
               "low_min_lpfmed_w", "low_min_lpf99_w", "low_min_lpfworst_w", "lever_pfet_step_lpfworst_w", "lever_both_step_w"):
        res["worst_kd_6v4_" + kk] = worst(kk)
        res["worst_kd_8v4_" + kk] = float(min(by[k]["at_8v4"][kk] for k in kd_cases))
    res["module_high_all_w"] = float(M.max())
    res["module_high_all_8v4_w"] = float(M[:, i84].max())
    verdict(V, f"A5 open loop, every unit that passes the build step (reading within its bound), 6.4 to 8.4 V, every case: module output at most {ceil_w:g} W",
            res["module_high_all_w"] <= ceil_w, detail=f"{res['module_high_all_w']:.2f} W")
    verdict(V, "A5 nominal corner at least 3.97 W at 6.4 V in every key-down case", res["worst_kd_6v4_nominal_w"] >= P.REQ012_LO,
            detail=f"{res['worst_kd_6v4_nominal_w']:.2f} W")
    verdict(V, "A5 lowest corner (step basis: module typical to +1.5 dB, reading at its bound, LPF at most its MC 99th percentile) at least 3.97 W at 6.4 V, every key-down case",
            res["worst_kd_6v4_low_step_lpf99_w"] >= P.REQ012_LO, detail=f"{res['worst_kd_6v4_low_step_lpf99_w']:.2f} W")
    verdict(V, "A5 lowest corner (step basis, LPF at most its MC 99th percentile) at least 3.97 W at 8.4 V, every key-down case",
            res["worst_kd_8v4_low_step_lpf99_w"] >= P.REQ012_LO, detail=f"{res['worst_kd_8v4_low_step_lpf99_w']:.2f} W")
    res["verdicts"] = VERDICTS.get(V, {})
    (out / "result.json").write_text(json.dumps(res, indent=0, default=str))
    plot_p4r4(out, res, key)
    write_p4r4_md(out, res, key)
    copy_inputs(out, [deck])
    res["kept_raw"] = R3.raw_manifest(out)
    (out / "result.json").write_text(json.dumps(res, indent=0, default=str))
    print(key, json.dumps({k: v for k, v in res.items() if k.startswith("worst_") or k in ("step_target_w", "module_high_all_w")}, default=str))
    return res


def plot_p4r4(out: Path, r: dict, key: str):
    vp = np.array(r["vpack"])
    by = r["by_tc"]
    tag = "D-9 ceiling 8 W" if key == "r4p4" else "clamp scenario B, ceiling 10 W"
    fig, ax = plt.subplots(figsize=(9.6, 7.6))
    ref = by["t25a"]
    ax.plot(vp, ref["curves"]["nominal"], color=COL["a5"], lw=2.2, label="nominal corner (typical unit read exactly), 25 C key-down")
    for k in r["kd_cases"]:
        ax.plot(vp, by[k]["curves"]["low_step_lpf99"], color=P.TC_COL[k], lw=1.1, ls="--",
                label=f"lowest, step basis, LPF at most MC 99 %: {by[k]['label']}")
    ax.plot(vp, ref["curves"]["low_exact_lpf99"], color=INK2, lw=1.5, label="lowest, typical unit read exactly, LPF MC 99 %: 25 C key-down")
    ax.plot(vp, ref["curves"]["low_min_lpf99"], color=COL["aux"], lw=1.5, ls="-.", label="lowest, datasheet-minimum module, LPF MC 99 %: 25 C key-down")
    hi = np.max([by[k]["module_high_curve_w"] for k in by], axis=0)
    ax.plot(vp, hi, color=INK, lw=1.4, ls=(0, (1, 1)), label=f"module output, highest over every unit case and temperature case, ALC open")
    ax.axhline(8.0, color=INK2, lw=1, ls=":", label="8 W: module stability guarantee (module output)")
    ax.axhline(10.0, color=INK2, lw=1.6, ls=":", label="10 W: module maximum rating (module output)")
    P.add_req_lines(ax)
    ax.set_xlim(6.4, 8.4)
    ax.set_ylim(0, 11)
    ax.set_xlabel("Pack voltage, read in receive (V)")
    ax.set_ylabel("Available power, ALC at its top (W)")
    ax.set_title(f"{VKEY[key]} (revision 4): A5, {tag}, per-unit clamp step (target {r['step_target_w']:.2f} W, g- {r['step_guard']['g_minus_db']:.2f} dB, "
                 f"g+ {r['step_guard']['g_plus_db']:.2f} dB)\npower at the SMA versus pack voltage, LTspice, {r['n_deck_steps']} steps ({r['n_corners']} corners with the output loss)", fontsize=9)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.1), ncol=2, fontsize=6.4)
    fig.tight_layout()
    fig.savefig(out / f"power_a5_step_{'d9' if key == 'r4p4' else 'clampb'}_sma.png", dpi=150)
    plt.close(fig)
    fig, ax = plt.subplots(figsize=(10.4, 6.8))
    keys = [k for k in by if k != "coldhi"]
    x = np.arange(len(keys))
    series = [("nominal_w", "nominal corner", COL["a5"], "o"),
              ("low_exact_lpf99_w", "lowest, typical unit read exactly, LPF at most MC 99 %", INK2, "^"),
              ("low_step_lpf99_w", "lowest, step basis (typical to +1.5 dB, reading at its bound), LPF at most MC 99 %", "#0e7a54", "s"),
              ("low_step_lpfworst_w", "lowest, step basis, LPF worst case (1.76 dB)", INK, "v"),
              ("low_min_lpf99_w", "lowest, datasheet-minimum module, LPF at most MC 99 %", COL["aux"], "D")]
    allv = []
    for j, (kk, lab, col, mk) in enumerate(series):
        ys = [by[k]["at_6v4"][kk] for k in keys]
        allv += ys
        ax.plot(x + (j - (len(series) - 1) / 2) * 0.12, ys, mk, color=col, ms=6.5, ls="none", label=lab)
    P.add_req_lines(ax)
    ax.set_xticks(x)
    ax.set_xticklabels([P.TC_SHORT[k] for k in keys], fontsize=6.8)
    ax.set_ylim(np.floor((min(allv) - 0.25) * 2) / 2, 6.6)
    ax.set_ylabel("Power at the SMA at 6.4 V pack (W)")
    ax.set_title(f"{VKEY[key]} (revision 4): A5, {tag}, per-unit clamp step: power at the SMA at 6.4 V per temperature case", fontsize=9)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.16), ncol=1, fontsize=7.2)
    fig.tight_layout()
    fig.savefig(out / f"power_a5_step_{'d9' if key == 'r4p4' else 'clampb'}_temperature.png", dpi=150)
    plt.close(fig)


def write_p4r4_md(out: Path, r: dict, key: str):
    by = r["by_tc"]
    g = r["step_guard"]
    L = [f"# {r['run']}: A5 output power at the SMA with the per-unit clamp step, ceiling {r['ceiling_w']:g} W (revision 4)", "",
         f"Drive band (r4-s2): {r['pins_mw'][0]:.2f} / {r['pins_mw'][1]:.2f} / {r['pins_mw'][2]:.2f} mW. Step: design value {r['design_w']} W, "
         f"g- {g['g_minus_db']:.3f} dB, g+ {g['g_plus_db']:.3f} dB, step target {r['step_target_w']:.3f} W. VGG window offsets {r['vgg_offsets']} V. "
         f"LPF plus relay {r['loss_db']} dB. All figures estimates.", "",
         "| Unit case | Highest module output, any case and pack voltage (W) | Clamp top at 6.4 V (V) | Clamp top at 8.4 V (V) |", "|---|---|---|---|"]
    for u in r["units"]:
        a, b = r["clamp_top_6v4_per_unit"][u[0]], r["clamp_top_8v4_per_unit"][u[0]]
        L.append(f"| {u[0]} | {r['module_high_per_unit_w'][u[0]]:.2f} | {a[0]:.3f} to {a[1]:.3f} | {b[0]:.3f} to {b[1]:.3f} |")
    L += ["", "At 6.4 V per temperature case (W; margin to 3.97 W in dB):", "",
          "| Case | Nominal | Step basis, LPF median | Step basis, LPF MC 99 % | Step basis, LPF worst | Typical read exactly, LPF MC 99 % | Min. module, LPF MC 99 % | Levers, step basis |",
          "|---|---|---|---|---|---|---|---|"]
    for k, d in by.items():
        a = d["at_6v4"]
        L.append(f"| {d['label']} | {a['nominal_w']:.2f} | {a['low_step_lpfmed_w']:.2f} ({a['low_step_lpfmed_margin_db']:+.2f}) | "
                 f"{a['low_step_lpf99_w']:.2f} ({a['low_step_lpf99_margin_db']:+.2f}) | {a['low_step_lpfworst_w']:.2f} ({a['low_step_lpfworst_margin_db']:+.2f}) | "
                 f"{a['low_exact_lpf99_w']:.2f} ({a['low_exact_lpf99_margin_db']:+.2f}) | {a['low_min_lpf99_w']:.2f} ({a['low_min_lpf99_margin_db']:+.2f}) | "
                 f"{a['lever_both_step_w']:.2f} ({a['lever_both_step_margin_db']:+.2f}) |")
    L += ["", "At 8.4 V per temperature case (W):", "", "| Case | Nominal | Step basis, LPF MC 99 % | Typical read exactly, LPF MC 99 % | Min. module, LPF MC 99 % |", "|---|---|---|---|---|"]
    for k, d in by.items():
        a = d["at_8v4"]
        L.append(f"| {d['label']} | {a['nominal_w']:.2f} | {a['low_step_lpf99_w']:.2f} | {a['low_exact_lpf99_w']:.2f} | {a['low_min_lpf99_w']:.2f} |")
    L += ["", f"Highest module output over every corner and pack voltage: {r['module_high_all_w']:.2f} W (ceiling {r['ceiling_w']:g} W).",
          "Largest pack current at key-down (design corners): " + ", ".join(f"{d['label']} {d['pack_current_max_a']:.2f} A" for d in by.values()) + ".",
          "", "Every quoted lowest corner with its parameters is in `result.json` (`by_tc.<case>.corners`).",
          f"Plots `power_a5_step_{'d9' if key == 'r4p4' else 'clampb'}_sma.png`, `power_a5_step_{'d9' if key == 'r4p4' else 'clampb'}_temperature.png`; deck `power_a5_step.cir`.", ""]
    (out / "result.md").write_text("\n".join(L))


# ---------------------------------------------------------------- s4: the clamp step (finding-2)
S4_SPREADS = [("min", 0.0), ("typ", 0.0), ("typ", 0.5), ("typ", 1.0), ("typ", 1.5)]
S4_U = [0.0, 0.3, 0.5, 1.0, 1.5]      # upper spread of a module above the typical curve (dB) for the fixed-clamp table
S4_READ = [0.0, 0.02, 0.05, 0.10, 0.15, 0.20]   # reading uncertainty (relative) for the break-even
GRAPH_READ_DB = 0.07


def _grid(vp, pins, feeds_lv, cases, loss_max, offs):
    """Corner arrays for the replica: (case, feed level, eta, pin, f, offset, loss)."""
    rows = []
    for k in cases:
        for lv in feeds_lv:
            for eta in P.A5_ETA:
                for pin in pins:
                    for f in P.FREQS:
                        for o in offs:
                            rows.append((k, lv, eta, pin, f, o))
    return rows


def replica_low(vp, pins, base, x_db, e_db, tgt, offs, loss_max, T, xg, g135, g155, mc, kd_cases):
    """Lowest power at the SMA at pack voltage vp over the step basis corners of one unit (base, x) read with error e."""
    best = np.inf
    lvs = range(3)
    for k in kd_cases:
        tc = P.tc_by_key(k)
        for lv in lvs:
            rf = R3.feed3_at(k, lv)
            for eta in P.A5_ETA:
                for pin in pins:
                    top = float(clamp_top_unit(np.array([vp]), eta, pin, lv, base, x_db + e_db, tgt, T, mc)[0])
                    for f in P.FREQS:
                        ks = (mc[f]["kmin"] if base == "min" else 1.0) * 10 ** (x_db / 10)
                        pm = module_vec(vp, rf, eta, pin, f, top + min(offs), ks, k, T, xg, g135, g155)
                        for L in [x for x in LOSS3_DESIGN if x <= loss_max + 1e-9]:
                            best = min(best, float(pm) * 10 ** (-(L + (L - P.LOSS_RELAY_DB) * P.copper_db_per_db(tc)) / 10))
    return best


def replica_high(vp, pins, base, x_db, e_db, tgt, T, xg, g135, g155, mc):
    """Highest module output (open loop, window top) of one unit at pack voltage vp over the open-loop cases."""
    best = 0.0
    for k in ("coldhi", "t25soak"):
        for lv in range(4):
            rf = R3.feed3_at(k, lv)
            for eta in P.A5_ETA:
                for pin in pins:
                    top = float(clamp_top_unit(np.array([vp]), eta, pin, lv, base, x_db + e_db, tgt, T, mc)[0])
                    for f in P.FREQS:
                        ks = (mc[f]["kmin"] if base == "min" else 1.0) * 10 ** (x_db / 10)
                        best = max(best, float(module_vec(vp, rf, eta, pin, f, top, ks, k, T, xg, g135, g155)))
    return best


def fixed_high(vp, top, pins, u_db, T, xg, g135, g155):
    """Revision 3's fixed clamp (top at vp) with a module u_db above the typical curve: highest open-loop module output."""
    best = 0.0
    for k in ("coldhi", "t25soak"):
        for lv in range(4):
            rf = R3.feed3_at(k, lv)
            for eta in P.A5_ETA:
                for f in P.FREQS:
                    best = max(best, float(module_vec(vp, rf, eta, pins[2], f, top, 10 ** (u_db / 10), k, T, xg, g135, g155)))
    return best


def fixed_top_for(vp, pins, u_db, target, T, xg, g135, g155):
    """A fixed clamp set on the bounded upper spread: the top at which a module u_db above typical makes target."""
    from scipy.optimize import brentq
    h = lambda v: fixed_high(vp, v, pins, u_db, T, xg, g135, g155) - target
    return 3.5 if h(3.5) <= 0 else float(brentq(h, XG4[0] + 0.01, 3.5, xtol=1e-5))


def fixed_low(vp, top, pins, offs, loss_max, T, xg, g135, g155, kd_cases):
    best = np.inf
    for k in kd_cases:
        tc = P.tc_by_key(k)
        for lv in range(3):
            rf = R3.feed3_at(k, lv)
            for eta in P.A5_ETA:
                for pin in pins:
                    for f in P.FREQS:
                        pm = float(module_vec(vp, rf, eta, pin, f, top + min(offs), 1.0, k, T, xg, g135, g155))
                        for L in [x for x in LOSS3_DESIGN if x <= loss_max + 1e-9]:
                            best = min(best, pm * 10 ** (-(L + (L - P.LOSS_RELAY_DB) * P.copper_db_per_db(tc)) / 10))
    return best


def run_s4():
    out = rundir("r4s4")
    V = "s4"
    s2 = json.loads((rundir("r4s2") / "result.json").read_text())
    p4 = json.loads((rundir("r4p4") / "result.json").read_text())
    p5 = json.loads((rundir("r4p5") / "result.json").read_text())
    p4r3 = json.loads((R3.rundir("p4") / "result.json").read_text())
    p5r3 = json.loads((R3.rundir("p5") / "result.json").read_text())
    T, xg, g135, g155, mc = model_consts()
    pins = p4["pins_dbm"]
    kd = p4["kd_cases"]
    g = step_guard(s2)
    unc_lo = p4["unmodelled_db"][0]
    need_w = P.REQ012_LO * 10 ** (-unc_lo / 10)    # the basis must reach this for 3.97 W with the unmodelled terms
    res = {"run": RUNS4["r4s4"], "revision": REVISION, "power_runs": [RUNS4["r4p4"], RUNS4["r4p5"]], "step_guard": g,
           "need_w_for_3v97_with_terms": need_w}
    # (a) revision 3's fixed clamps against the upper spread, and a fixed clamp set on a bounded upper spread
    fixed = {}
    for tag, pr3, ceil, dsg, offs in (("D-9 (8 W)", p4r3, 8.0, 7.9, R3.VGG_OFF), ("scenario B (10 W)", p5r3, 10.0, 9.9, R3.CLAMPB_OFF)):
        top_r3 = pr3["vgg_top_8v4"]
        pins_r3 = pr3["pins_dbm"]
        rows = []
        for u in S4_U:
            hi_r3 = fixed_high(8.4, top_r3, pins_r3, u, T, xg, g135, g155)
            top_u = fixed_top_for(8.4, pins, u + GRAPH_READ_DB, dsg, T, xg, g135, g155)
            lo_u = fixed_low(8.4, top_u, pins, offs, 1.03, T, xg, g135, g155, kd)
            rows.append({"u_db": u, "r3_top_v": top_r3, "high_with_r3_clamp_w": hi_r3, "top_for_u_v": top_u,
                         "typical_lowest_8v4_lpf99_w": lo_u, "margin_with_terms_db": db(lo_u / P.REQ012_LO) + unc_lo})
        fixed[tag] = {"ceiling_w": ceil, "rows": rows}
    res["fixed_clamp"] = fixed
    fb = fixed["scenario B (10 W)"]["rows"]
    u03 = next(r for r in fb if abs(r["u_db"] - 0.3) < 1e-9)
    verdict(V, "Revision 3 fixed clamp scenario B (typical-module top): module output at most 10 W for a module 0.3 dB above typical (finding-2)",
            u03["high_with_r3_clamp_w"] <= 10.0, detail=f"{u03['high_with_r3_clamp_w']:.2f} W")
    verdict(V, "Fixed clamp scenario B set on a module 0.3 dB above typical (+0.07 dB graph read): typical unit at least 3.97 W at 8.4 V with the terms (finding-2)",
            u03["margin_with_terms_db"] >= 0, detail=f"{u03['typical_lowest_8v4_lpf99_w']:.2f} W, {u03['margin_with_terms_db']:+.2f} dB with the terms")
    # (b) the step replica over the module spread, both ceilings, at 8.4 and 6.4 V; checked against the decks
    spread = {}
    chk = []
    for key, pr in (("r4p4", p4), ("r4p5", p5)):
        tgt = pr["step_target_w"]
        offs = pr["vgg_offsets"]
        rows = []
        for base, x in S4_SPREADS:
            for e in (-g["g_minus_db"], 0.0, g["g_plus_db"]):
                r = {"base": base, "x_db": x, "e_db": e}
                for vpk in (6.4, 8.4):
                    r[f"low_lpf99_{vpk}"] = replica_low(vpk, pins, base, x, e, tgt, offs, 1.03, T, xg, g135, g155, mc, kd)
                    r[f"high_{vpk}"] = replica_high(vpk, pins, base, x, e, tgt, T, xg, g135, g155, mc)
                rows.append(r)
        spread[key] = rows
        # deck check at 8.4 V: the step basis minimum and the highest module
        by = pr["by_tc"]
        deck_lo = min(by[k]["at_8v4"]["low_step_lpf99_w"] for k in kd)
        rep_lo = min(r["low_lpf99_8.4"] for r in rows if r["base"] == "typ" and r["x_db"] in (0.0, STEP_X_TOP_DB))
        deck_hi = pr["module_high_all_8v4_w"]
        rep_hi = max(r["high_8.4"] for r in rows if r["base"] == "typ" and r["x_db"] in (0.0, STEP_X_TOP_DB) or r["base"] == "min")
        chk.append((key, deck_lo, rep_lo, deck_hi, rep_hi))
    ok = all(abs(a / b - 1) < 0.005 and abs(c / d - 1) < 0.005 for _, a, b, c, d in chk)
    verdict(V, "check: the replica equals the r4 decks at 8.4 V within 0.5 % (step basis lowest, highest module)", ok, "check",
            "; ".join(f"{VKEY[k]}: {b:.3f} against {a:.3f} W, {d:.3f} against {c:.3f} W" for k, a, b, c, d in chk))
    res["spread"] = spread
    res["replica_check"] = [{"run": k, "deck_low_w": a, "replica_low_w": b, "deck_high_w": c, "replica_high_w": d} for k, a, b, c, d in chk]
    # (c) reading break-even, scenario B and D-9: the step basis at 8.4 V against the reading uncertainty
    be = {}
    for key, pr in (("r4p4", p4), ("r4p5", p5)):
        offs = pr["vgg_offsets"]
        rows = []
        for rr in S4_READ:
            gg = step_guard(s2, rr)
            tgt = CEIL[key][1] * 10 ** (-gg["g_minus_db"] / 10)
            lo = min(replica_low(8.4, pins, "typ", x, gg["g_plus_db"], tgt, offs, 1.03, T, xg, g135, g155, mc, kd) for x in (0.0, STEP_X_TOP_DB))
            rows.append({"read_rel": rr, "g_minus_db": gg["g_minus_db"], "g_plus_db": gg["g_plus_db"], "step_target_w": tgt,
                         "low_8v4_w": lo, "margin_with_terms_db": db(lo / P.REQ012_LO) + unc_lo})
        be[key] = rows
    res["break_even"] = be
    rb = be["r4p5"]
    res["break_even_note"] = ("at a perfect reading the other step terms alone leave the scenario B basis at "
                              f"{rb[0]['low_8v4_w']:.2f} W at 8.4 V ({rb[0]['margin_with_terms_db']:+.2f} dB with the terms)")
    res["verdicts"] = VERDICTS.get(V, {})
    # plot
    fig, axs = plt.subplots(1, 3, figsize=(18.5, 6.6))
    ax = axs[0]
    for tag, col in (("D-9 (8 W)", COL["a4"]), ("scenario B (10 W)", COL["a5"])):
        rr = fixed[tag]["rows"]
        us = [r["u_db"] for r in rr]
        ax.plot(us, [r["high_with_r3_clamp_w"] for r in rr], "o-", color=col, label=f"{tag}: highest module, revision 3 clamp (typical-module top)")
        ax.plot(us, [r["typical_lowest_8v4_lpf99_w"] for r in rr], "s--", color=col,
                label=f"{tag}: typical unit's lowest at the SMA, clamp set on +u (+0.07 dB)")
    ax.axhline(10.0, color=INK, lw=1.4, label="10 W: module maximum rating")
    ax.axhline(8.0, color=INK, lw=1.2, ls=":", label="8 W: stability guarantee")
    ax.axhline(need_w, color=INK, lw=2.0, ls="--", label=f"{need_w:.2f} W: 3.97 W with the unmodelled terms")
    ax.set_xlabel("Module output above the typical curve, u (dB)")
    ax.set_ylabel("Power at 8.4 V pack (W)")
    ax.set_ylim(0, 12.5)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), fontsize=6.6)
    ax.set_title("s4 (a): a fixed clamp against the module's upper spread, 8.4 V\n(the datasheet gives no maximum)", fontsize=9)
    ax = axs[1]
    terms = [("probe reading, TC-SYS-010 bound 15 % (low / high)", g["read_low_db"], g["read_high_db"])] + \
            [(t[0], t[1], t[1]) for t in g["other"]]
    yy = np.arange(len(terms))[::-1]
    for y, (lab, lo, hi) in zip(yy, terms):
        ax.barh(y + 0.18, lo, height=0.34, color=COL["a4"])
        ax.barh(y - 0.18, hi, height=0.34, color=COL["a5"])
    from matplotlib.patches import Patch
    ax.legend(handles=[Patch(color=COL["a4"], label=f"g-: unit read low (clamp too high); sum {g['g_minus_db']:.2f} dB"),
                       Patch(color=COL["a5"], label=f"g+: unit read high (clamp too low); sum {g['g_plus_db']:.2f} dB")],
              loc="upper center", bbox_to_anchor=(0.5, -0.12), fontsize=7)
    ax.set_yticks(yy)
    ax.set_yticklabels([t[0][:60] + ("..." if len(t[0]) > 60 else "") for t in terms], fontsize=6.4)
    ax.set_xlabel("Term (dB)")
    ax.set_title("s4 (b): terms of the per-unit clamp step (worst-case sum)", fontsize=9)
    ax = axs[2]
    for key, col, tag in (("r4p4", COL["a4"], "D-9 (8 W)"), ("r4p5", COL["a5"], "scenario B (10 W)")):
        rr = be[key]
        ax.plot([100 * r["read_rel"] for r in rr], [r["low_8v4_w"] for r in rr], "o-", color=col,
                label=f"{tag}: step basis lowest at 8.4 V (read high by the bound)")
    ax.axhline(need_w, color=INK, lw=2.0, ls="--", label=f"{need_w:.2f} W: 3.97 W with the unmodelled terms")
    ax.axvline(100 * STEP_READ_REL, color=INK2, lw=1.2, ls=":", label="TC-SYS-010 acceptance bound, 15 %")
    ax.set_xlabel("Open-loop power reading uncertainty at the step (+/- %)")
    ax.set_ylabel("Lowest at the SMA at 8.4 V (W), LPF at most MC 99 %")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), fontsize=7)
    ax.set_title("s4 (c): the step's reading against the reach at 8.4 V\n(replica of the r4 deck model)", fontsize=9)
    fig.tight_layout(w_pad=2.5)
    fig.savefig(out / "clamp_step.png", dpi=150, bbox_inches="tight")
    plt.close(fig)
    (out / "result.json").write_text(json.dumps(res, indent=1, default=float))
    L = [f"# {res['run']}: the clamp ceiling as a per-unit build step (revision 4, finding-2)", "",
         "## (a) Fixed clamp against the module's upper spread (8.4 V, Python replica of the deck model)", "",
         "| Ceiling | u (dB) | Highest module with the revision 3 clamp (top V) (W) | Fixed top set on +u +0.07 dB (V) | Typical unit's lowest, LPF MC 99 % (W) | With the terms (dB) |", "|---|---|---|---|---|---|"]
    for tag, d in fixed.items():
        for r in d["rows"]:
            L.append(f"| {tag} | {r['u_db']:.1f} | {r['high_with_r3_clamp_w']:.2f} ({r['r3_top_v']:.3f}) | {r['top_for_u_v']:.3f} | "
                     f"{r['typical_lowest_8v4_lpf99_w']:.2f} | {r['margin_with_terms_db']:+.2f} |")
    L += ["", "## (b) Terms of the step (worst-case sum)", "", "| Term | Low side, g- (dB) | High side, g+ (dB) | Class |", "|---|---|---|---|",
          f"| Open-loop power reading, diode probe at the TC-SYS-010 bound (15 %) | {g['read_low_db']:.3f} | {g['read_high_db']:.3f} | TC-SYS-010 criterion |"]
    for t in g["other"]:
        L.append(f"| {t[0]} | {t[1]:.3f} | {t[1]:.3f} | {t[2]} |")
    L += [f"| **Sum** | **{g['g_minus_db']:.3f}** | **{g['g_plus_db']:.3f}** | |", "",
          "## (c) Replica over the module spread (every key-down case, LPF at most its MC 99th percentile; highest over the open-loop cases)", ""]
    for key, rows in spread.items():
        L += [f"### {VKEY[key]}: ceiling {CEIL[key][0]:g} W, step target {json.loads((rundir(key) / 'result.json').read_text())['step_target_w']:.3f} W", "",
              "| Module | e (dB) | Lowest at 6.4 V (W) | Lowest at 8.4 V (W) | Highest at 6.4 V (W) | Highest at 8.4 V (W) |", "|---|---|---|---|---|---|"]
        for r in rows:
            L.append(f"| {'datasheet minimum' if r['base'] == 'min' else f'typical {r['x_db']:+.1f} dB'} | {r['e_db']:+.2f} | {r['low_lpf99_6.4']:.2f} | "
                     f"{r['low_lpf99_8.4']:.2f} | {r['high_6.4']:.2f} | {r['high_8.4']:.2f} |")
        L.append("")
    L += ["Replica against the decks at 8.4 V: " + "; ".join(f"{VKEY[c['run']]}: lowest {c['replica_low_w']:.3f} / {c['deck_low_w']:.3f} W, highest "
                                                              f"{c['replica_high_w']:.3f} / {c['deck_high_w']:.3f} W" for c in res["replica_check"]), "",
          "## (d) Reading break-even (step basis at 8.4 V, read high by the bound)", "",
          "| Ceiling | Reading (+/- %) | g- (dB) | g+ (dB) | Step target (W) | Lowest at 8.4 V (W) | With the terms (dB) |", "|---|---|---|---|---|---|---|"]
    for key, rows in be.items():
        for r in rows:
            L.append(f"| {CEIL[key][0]:g} W | {100 * r['read_rel']:.0f} | {r['g_minus_db']:.3f} | {r['g_plus_db']:.3f} | {r['step_target_w']:.3f} | "
                     f"{r['low_8v4_w']:.2f} | {r['margin_with_terms_db']:+.2f} |")
    L += ["", f"Note: {res['break_even_note']}.", "", "Plot `clamp_step.png`.", ""]
    (out / "result.md").write_text("\n".join(L))
    copy_inputs(out, [])
    print("s4", json.dumps({"fixed_B_u0.3": u03, "check": res["replica_check"], "break_even_B": be["r4p5"]}, default=float))
    return res


# ---------------------------------------------------------------- s3 (revision 4): REQ-SYS-012 basis and delta
S3_COVER = [
    ("nominal_w", "nominal corner (typical unit read exactly)"),
    ("low_step_lpfmed_w", "lowest, step basis, LPF at most its Monte Carlo median"),
    ("low_step_lpf99_w", "lowest, step basis, LPF at most its Monte Carlo 99th percentile"),
    ("low_step_lpfworst_w", "lowest, step basis, LPF at its searched worst case"),
    ("low_exact_lpf99_w", "lowest, typical unit read exactly, LPF MC 99th percentile (informative)"),
    ("low_min_lpfmed_w", "lowest, datasheet-minimum module, LPF median"),
    ("low_min_lpf99_w", "lowest, datasheet-minimum module, LPF MC 99th percentile"),
    ("low_min_lpfworst_w", "lowest, datasheet-minimum module, LPF worst case"),
    ("lever_pfet_step_lpfworst_w", "lever: P-FET pair at most 0.06 ohm, step basis, LPF worst"),
    ("lever_both_step_w", "levers: P-FET pair and the r14 LPF, step basis"),
]
S3_BASIS = "low_step_lpf99_w"


def s3_rows(pr: dict) -> list[dict]:
    by, kd = pr["by_tc"], pr["kd_cases"]
    unc_lo, unc_hi = pr["unmodelled_db"]
    rows = []
    for key, lab in S3_COVER:
        w = min(by[k]["at_6v4"][key] for k in kd)
        kw = min(kd, key=lambda k: by[k]["at_6v4"][key])
        m = db(w / P.REQ012_LO)
        env = np.min([by[k]["curves"][key[:-2]] for k in kd], axis=0)
        reach = [by[k]["reach_3v97"].get(key[:-2]) for k in kd]
        rows.append({"key": key, "label": lab, "worst_w": float(w), "worst_case": by[kw]["label"], "margin_db": m,
                     "margin_with_terms_db": [m + unc_lo, m + unc_hi], "dev_from_5w_with_terms_db": db(w / P.REQ012_NOM) + unc_lo,
                     "worst_8v4_w": float(min(by[k]["at_8v4"][key] for k in kd)),
                     "min_over_range_w": float(env.min()), "v_at_min": float(np.array(pr["vpack"])[int(np.argmin(env))]),
                     "pack_v_reaches_3v97_worst": (None if any(x is None for x in reach) else float(max(reach)))})
    return rows


def s3_proposal(pr: dict, tag: str, V: str) -> dict:
    """Lower limit of the form: -x dB at 6.4 V, rising linearly in dB to -y dB at v1, -y dB from v1 to 8.4 V (x, y in
    0.1 dB, y at least 1.0); the smallest y for which such a line lies under the basis envelope with the unmodelled
    terms at every pack voltage, and for that y the lowest v1 (0.05 V grid)."""
    by, kd = pr["by_tc"], pr["kd_cases"]
    unc_lo = pr["unmodelled_db"][0]
    vp = np.array(pr["vpack"])
    env = np.min([by[k]["curves"][S3_BASIS[:-2]] for k in kd], axis=0)
    env_db = 10 * np.log10(env / P.REQ012_NOM) + unc_lo
    x = float(np.ceil(-env_db[0] * 10 - 1e-9) / 10)
    best = None
    for y10 in range(10, int(round(x * 10)) + 1):
        y = y10 / 10
        for j in range(len(vp)):
            v1 = vp[j]
            lim = np.where(vp >= v1, -y, -x + (x - y) * (vp - 6.4) / max(v1 - 6.4, 1e-9)) if v1 > 6.4 + 1e-9 else np.full(vp.shape, -y)
            if np.all(env_db >= lim - 1e-9):
                best = (y, float(v1), lim)
                break
        if best:
            break
    outp = {"x_db": x, "env_w": env.tolist(), "env_db_with_terms": env_db.tolist()}
    if best:
        y, v1, lim = best
        outp.update({"y_db": y, "v1": v1, "limit_db": lim.tolist(), "limit_w": (P.REQ012_NOM * 10 ** (lim / 10)).tolist(),
                     "low_end_w": float(P.REQ012_NOM * 10 ** (-x / 10)), "plateau_w": float(P.REQ012_NOM * 10 ** (-y / 10))})
        verdict(V, f"check: the proposed REQ-SYS-012 limit line lies under the basis with the unmodelled terms ({tag})", True, "check",
                f"-{x:.1f} dB at 6.4 V, -{y:.1f} dB from {v1:.2f} V")
    else:   # no rising-to-plateau line with the plateau at or above the 6.4 V value: not a check failure, a result
        verdict(V, f"A5 a REQ-SYS-012 delta of the stated form (lower limit rising from 6.4 V to a plateau) holds on the basis ({tag})", False,
                detail=f"basis lowest {float(env.min()):.2f} W at {float(vp[int(np.argmin(env))]):.2f} V")
    return outp


def run_s3():
    out = rundir("r4s3")
    V = "s3"
    p4 = json.loads((rundir("r4p4") / "result.json").read_text())
    p5 = json.loads((rundir("r4p5") / "result.json").read_text())
    s4 = json.loads((rundir("r4s4") / "result.json").read_text())
    unc_lo, unc_hi = p4["unmodelled_db"]
    vp = np.array(p4["vpack"])
    rows4, rows5 = s3_rows(p4), s3_rows(p5)
    prop4, prop5 = s3_proposal(p4, "D-9 ceiling with the step", V), s3_proposal(p5, "clamp scenario B with the step", V)
    res = {"run": RUNS4["r4s3"], "revision": REVISION, "power_runs": [RUNS4["r4p4"], RUNS4["r4p5"]], "clamp_step_run": RUNS4["r4s4"],
           "unmodelled_db": [unc_lo, unc_hi], "basis": S3_BASIS, "vpack": vp.tolist(),
           "d9": {"rows": rows4, "proposal": prop4, "step_target_w": p4["step_target_w"], "module_high_w": p4["module_high_all_w"]},
           "clamp_b": {"rows": rows5, "proposal": prop5, "step_target_w": p5["step_target_w"], "module_high_w": p5["module_high_all_w"]}}
    b4 = next(r for r in rows4 if r["key"] == S3_BASIS)
    b5 = next(r for r in rows5 if r["key"] == S3_BASIS)
    verdict(V, "A5 REQ-SYS-012 as baselined (5 W -1 dB) at 6.4 V on the step basis with the terms, clamp scenario B",
            b5["margin_with_terms_db"][0] >= 0, detail=f"{b5['margin_with_terms_db'][0]:+.2f} dB")
    verdict(V, "A5 REQ-SYS-012 lower bound at 8.4 V on the step basis with the terms, D-9 ceiling (8 W)",
            db(b4["worst_8v4_w"] / P.REQ012_LO) + unc_lo >= 0, detail=f"{b4['worst_8v4_w']:.2f} W")
    verdict(V, "A5 REQ-SYS-012 lower bound at 8.4 V on the step basis with the terms, clamp scenario B (10 W)",
            db(b5["worst_8v4_w"] / P.REQ012_LO) + unc_lo >= 0, detail=f"{b5['worst_8v4_w']:.2f} W")
    res["verdicts"] = VERDICTS.get(V, {})
    # plot
    fig, axs = plt.subplots(1, 2, figsize=(15.5, 7.0), gridspec_kw={"width_ratios": [1.25, 1.0]})
    ax = axs[0]
    for pr, prop, tag, ls in ((p4, prop4, "D-9 8 W", "--"), (p5, prop5, "clamp B 10 W", "-")):
        by, kd = pr["by_tc"], pr["kd_cases"]
        for key, lab, col in (("nominal", "nominal", COL["a5"]), ("low_step_lpf99", "step basis, LPF MC 99 %", "#0e7a54"),
                              ("low_exact_lpf99", "typical read exactly, LPF MC 99 %", INK2), ("low_min_lpf99", "min. module, LPF MC 99 %", COL["aux"])):
            e = np.min([by[k]["curves"][key] for k in kd], axis=0)
            ax.plot(vp, e, color=col, lw=1.5, ls=ls, label=f"{tag}: {lab}")
        if prop.get("limit_w"):
            ax.plot(vp, prop["limit_w"], color=COL["a4"] if tag.startswith("clamp") else "#b3401a", lw=2.2, ls=ls,
                    label=f"proposed low limit ({tag}): -{prop['x_db']:.1f} dB at 6.4 V, -{prop['y_db']:.1f} dB from {prop['v1']:.2f} V")
    env = np.array(prop5["env_w"])
    ax.fill_between(vp, env * 10 ** (unc_lo / 10), env, color="#0e7a54", alpha=0.15, label="clamp B step basis with the unmodelled terms")
    P.add_req_lines(ax)
    ax.set_xlim(6.4, 8.4)
    ax.set_ylim(0.0, 6.8)
    ax.set_xlabel("Pack voltage, read in receive (V)")
    ax.set_ylabel("Available power at the SMA (W), ALC at its top;\nminimum over the key-down cases")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncol=2, fontsize=6.4)
    ax.set_title("r4-s3: REQ-SYS-012 basis with the per-unit clamp step, A5\n(dashed: D-9 8 W ceiling, r4-p4; solid: clamp scenario B 10 W, r4-p5)", fontsize=9)
    ax = axs[1]
    labs = [r["label"].replace("lowest, ", "").replace("Monte Carlo", "MC") for r in rows4]
    y = np.arange(len(rows4))[::-1]
    for yy, r4, r5 in zip(y, rows4, rows5):
        for r, dy, col in ((r4, 0.15, COL["a4"]), (r5, -0.15, COL["a5"])):
            lo, hi = r["margin_with_terms_db"]
            ax.plot([lo, hi], [yy + dy, yy + dy], color=col, lw=4, solid_capstyle="butt", alpha=0.45)
            ax.plot(r["margin_db"], yy + dy, "o", color=col, ms=5)
    ax.plot([], [], "o-", color=COL["a4"], label="D-9 8 W ceiling with the step")
    ax.plot([], [], "o-", color=COL["a5"], label="clamp scenario B 10 W with the step")
    ax.axvline(0, color=INK, lw=1.4)
    ax.set_yticks(y)
    ax.set_yticklabels(labs, fontsize=6.3)
    ax.set_xlabel("Margin to 3.97 W at 6.4 V, worst key-down case (dB)\nbar: with the unmodelled terms")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), fontsize=7)
    ax.set_title("Margin at 6.4 V per coverage set", fontsize=9)
    fig.tight_layout(w_pad=3.0)
    fig.savefig(out / "req012_basis_r4.png", dpi=150, bbox_inches="tight")
    plt.close(fig)
    (out / "result.json").write_text(json.dumps(res, indent=1, default=float))
    L = [f"# {res['run']}: REQ-SYS-012 basis with the per-unit clamp step (revision 4)", "",
         f"From {RUNS4['r4p4']} (D-9 8 W ceiling) and {RUNS4['r4p5']} (clamp scenario B, 10 W ceiling, 0.03 V window), each with the "
         f"per-unit clamp step of {RUNS4['r4s4']}. The step basis: module typical to +{STEP_X_TOP_DB:g} dB (the trim range), the step's reading "
         f"anywhere in its bound, LPF at most its MC 99th percentile, every key-down case. Unmodelled terms {unc_lo:+.2f} / {unc_hi:+.2f} dB. All estimates.", ""]
    for tag, rw, prop, pr in (("D-9 8 W ceiling with the step (r4-p4)", rows4, prop4, p4), ("Clamp scenario B with the step (r4-p5)", rows5, prop5, p5)):
        L += [f"## {tag}: step target {pr['step_target_w']:.3f} W, highest module {pr['module_high_all_w']:.2f} W", "",
              "| Coverage | Worst key-down case | At 6.4 V (W) | Margin to 3.97 W (dB) | With the terms (dB) | From 5 W with the terms (dB) | At 8.4 V (W) | Lowest over 6.4 to 8.4 V (W, at V) |",
              "|---|---|---|---|---|---|---|---|"]
        for r in rw:
            L.append(f"| {r['label']} | {r['worst_case']} | {r['worst_w']:.2f} | {r['margin_db']:+.2f} | {r['margin_with_terms_db'][0]:+.2f} to "
                     f"{r['margin_with_terms_db'][1]:+.2f} | {r['dev_from_5w_with_terms_db']:+.2f} | {r['worst_8v4_w']:.2f} | {r['min_over_range_w']:.2f} ({r['v_at_min']:.2f}) |")
        if prop.get("limit_w"):
            L += ["", f"Delta on the basis: 5 W +1/-{prop['x_db']:.1f} dB ({prop['low_end_w']:.2f} W) at 6.4 V, rising linearly in dB to "
                      f"+1/-{prop['y_db']:.1f} dB ({prop['plateau_w']:.2f} W) at {prop['v1']:.2f} V, and +1/-{prop['y_db']:.1f} dB from there to 8.4 V.", ""]
        else:
            L += ["", "No limit line of the stated form found.", ""]
    L += ["Plot `req012_basis_r4.png`; the verdicts of every revision 4 run in `verdicts.json`.", ""]
    (out / "result.md").write_text("\n".join(L))
    (out / "verdicts.json").write_text(json.dumps(VERDICTS, indent=1))
    copy_inputs(out, [])
    print("s3", json.dumps({"d9": {k: v for k, v in prop4.items() if k not in ("env_w", "env_db_with_terms", "limit_db", "limit_w")},
                            "b": {k: v for k, v in prop5.items() if k not in ("env_w", "env_db_with_terms", "limit_db", "limit_w")}}))
    return res


# ---------------------------------------------------------------- main
EXPECTED: dict[str, dict[str, bool]] = {  # the verdict list of the analysis record section R4.10 (2026-09-29)
    's2': {
        'A5 select-on-test drive 10 to 30 mW in service with the k1 reading bound (one-sided terms from 146 MHz, 18.2 mW target)': True,
        'A5 select-on-test drive 10 to 30 mW at the +/-1.0 dB reading allocation (one-sided terms, 18.2 mW target)': True,
        'Revision 3 target 17.3 mW at the +/-1.0 dB allocation with the one-sided terms (the finding-1 case)': False,
        'A5 select-on-test drive 10 to 30 mW with a tinySA Ultra reading alone (+/-2 dB published)': False,
    },
    'p4': {
        'check: one .raw step per corner': True,
        'check: PA case temperature equals the thermal law within 0.01 K at every pack voltage': True,
        "check: the deck clamp equals the checker's per-unit clamp within LTspice's reltol (0.1 % + 0.1 mV) at every pack voltage": True,
        'check: VGG at most 3.50 V at every corner and pack voltage': True,
        'check: a unit read exactly makes the step target at its highest open-loop case where its clamp is below 3.50 V (within 0.2 %)': True,
        'check: every clamp VGG (top plus window offset) above the VGG grid floor (2.30 V)': True,
        'A5 open loop, every unit that passes the build step (reading within its bound), 6.4 to 8.4 V, every case: module output at most 8 W': True,
        'A5 nominal corner at least 3.97 W at 6.4 V in every key-down case': False,
        'A5 lowest corner (step basis: module typical to +1.5 dB, reading at its bound, LPF at most its MC 99th percentile) at least 3.97 W at 6.4 V, every key-down case': False,
        'A5 lowest corner (step basis, LPF at most its MC 99th percentile) at least 3.97 W at 8.4 V, every key-down case': False,
    },
    'p5': {
        'check: one .raw step per corner': True,
        'check: PA case temperature equals the thermal law within 0.01 K at every pack voltage': True,
        "check: the deck clamp equals the checker's per-unit clamp within LTspice's reltol (0.1 % + 0.1 mV) at every pack voltage": True,
        'check: VGG at most 3.50 V at every corner and pack voltage': True,
        'check: a unit read exactly makes the step target at its highest open-loop case where its clamp is below 3.50 V (within 0.2 %)': True,
        'check: every clamp VGG (top plus window offset) above the VGG grid floor (2.30 V)': True,
        'A5 open loop, every unit that passes the build step (reading within its bound), 6.4 to 8.4 V, every case: module output at most 10 W': True,
        'A5 nominal corner at least 3.97 W at 6.4 V in every key-down case': False,
        'A5 lowest corner (step basis: module typical to +1.5 dB, reading at its bound, LPF at most its MC 99th percentile) at least 3.97 W at 6.4 V, every key-down case': False,
        'A5 lowest corner (step basis, LPF at most its MC 99th percentile) at least 3.97 W at 8.4 V, every key-down case': False,
    },
    's4': {
        'Revision 3 fixed clamp scenario B (typical-module top): module output at most 10 W for a module 0.3 dB above typical (finding-2)': False,
        'Fixed clamp scenario B set on a module 0.3 dB above typical (+0.07 dB graph read): typical unit at least 3.97 W at 8.4 V with the terms (finding-2)': False,
        'check: the replica equals the r4 decks at 8.4 V within 0.5 % (step basis lowest, highest module)': True,
    },
    's3': {
        'A5 a REQ-SYS-012 delta of the stated form (lower limit rising from 6.4 V to a plateau) holds on the basis (D-9 ceiling with the step)': False,
        'check: the proposed REQ-SYS-012 limit line lies under the basis with the unmodelled terms (clamp scenario B with the step)': True,
        'A5 REQ-SYS-012 as baselined (5 W -1 dB) at 6.4 V on the step basis with the terms, clamp scenario B': False,
        'A5 REQ-SYS-012 lower bound at 8.4 V on the step basis with the terms, D-9 ceiling (8 W)': False,
        'A5 REQ-SYS-012 lower bound at 8.4 V on the step basis with the terms, clamp scenario B (10 W)': False,
    },
}


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    what = args[0] if args else "all"
    order = ["s2", "p4", "p5", "s4", "s3"]
    todo = order if what == "all" else [what]
    fns = {"s2": run_s2, "p4": lambda: run_p4r4("r4p4"), "p5": lambda: run_p4r4("r4p5"), "s4": run_s4, "s3": run_s3}
    for k in todo:
        fns[k]()
    failed_checks = [(r, n) for r, d in VERDICTS.items() for n, v in d.items() if v["kind"] == "check" and not v["pass"]]
    failed_crit = [(r, n) for r, d in VERDICTS.items() for n, v in d.items() if v["kind"] == "criterion" and not v["pass"]]
    print("\nVerdicts:")
    for r, d in VERDICTS.items():
        for n, v in d.items():
            print(f"  {r}: {'PASS' if v['pass'] else 'FAIL'}  {n}" + (f" ({v['detail']})" if v["detail"] else ""))
    code = 2 if failed_checks else (1 if failed_crit else 0)
    if "--expect" in sys.argv:
        diff = [(r, n, v["pass"], EXPECTED.get(r, {}).get(n)) for r, d in VERDICTS.items() for n, v in d.items()
                if EXPECTED.get(r, {}).get(n) != v["pass"]]
        for r, n, got, exp in diff:
            print(f"  VERDICT CHANGED: {r}: {n}: now {'PASS' if got else 'FAIL'}, record says "
                  f"{'not listed' if exp is None else ('PASS' if exp else 'FAIL')}")
        print(f"--expect: {len(diff)} verdict(s) differ from the analysis record")
        code = 3 if diff else 0
    print(f"exit status {code}")
    sys.exit(code)


if __name__ == "__main__":
    main()
