#!/usr/bin/env python3
"""WP-PDR-21 revision 5 (A5): the one Major finding of the delta review of revision 4, and only that (rule C1).

finding-31 (CK-ANA-A5/F2/D2/H1): the reject rule of the clamp step acts on the believed spread (the true spread plus
    the reading error), so a module up to +1.5 + g- = +2.49 dB above the typical curve passes when it is read low by the
    bound. Revision 4 said the +1.5 dB rule bounds the true upper spread and that the HZ-001 cause "a stronger module"
    is detected; both are wrong. The open-loop ceiling still holds (the clamp is set from the reading), but the
    pack current and the module dissipation with the ALC at its top rise at the low-pack end.
    Revision 5 adds the unit case "true +1.5 + g- dB, read low by g-" (believed exactly at the reject threshold) to the
    power decks (runs p4 and p5, the new unit case only; the seven revision 4 unit cases are the r4-p4 and r4-p5 runs,
    unchanged) and restates, over the whole population that passes the rule, the open-loop ceiling, the pack current
    and the module dissipation (run s5). Run s5 also sweeps the replica over the true spread and the reading error
    inside the passing region to show that the added case is the worst one for the pack current.

Usage (repo root, repo venv):
    .venv/bin/python hardware/sim/tx-pa/run_a5_r5.py all          # p4, p5, s5 in order
    .venv/bin/python hardware/sim/tx-pa/run_a5_r5.py p4|p5|s5
    add --expect to compare every verdict with the list of the analysis record section R5.6 (exit 3 on a change)

Inputs kept from revision 4 (not rerun): r4-s2 (drive band), the step terms (step_guard), the r4-p4 and r4-p5 decks and
their .raw files (kept on the owner's Mac, checked against the committed raw.sha256 before they are read). LTspice runs
only through tools/ltspice-batch.sh (ACC-LTSPICE-001), by run_pa.run_ltspice. Every value is an estimate.
"""
from __future__ import annotations

import hashlib
import json
import sys
import tempfile
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import run_a5_r4 as R4  # noqa: E402  (revision 4: step terms, deck writer, clamp closed form, replica)
R3 = R4.R3
P = R4.P
from run_pa import plt, INK, INK2, COL  # noqa: E402

DATE = "2026-09-30"
REVISION = 5
RUNS5 = {
    "r5p4": f"{DATE}-r5-p4-power-a5-design",
    "r5p5": f"{DATE}-r5-p5-power-a5-clamp-b",
    "r5s5": f"{DATE}-r5-s5-pass-population",
}
P.RUNS.update(RUNS5)
VERDICTS = P.VERDICTS
verdict = P.verdict
VKEY5 = {"r5p4": "p4", "r5p5": "p5", "r5s5": "s5"}
R4K = {"r5p4": "r4p4", "r5p5": "r4p5"}
TAG = {"r4p4": "D-9 (8 W)", "r4p5": "scenario B (10 W)"}
HOLD_A = {"MF-R300 hold at 23 C": 3.00, "at 50 C": 2.31, "at 60 C": 2.04}   # Bourns MF-R REV. AR 09/26 derating table (D)


def rundir(k: str) -> Path:
    return P.rundir(k)


def copy_inputs(out: Path, decks: list[Path]):
    import shutil
    shutil.copy2(Path(__file__), out / Path(__file__).name)
    for nm in ("run_a5_r4.py", "run_a5_r3.py", "run_pa.py"):
        shutil.copy2(HERE / nm, out / nm)
    for d in decks:
        if d.parent != out:
            shutil.copy2(d, out / d.name)


def added_case(g: dict) -> tuple[str, str, float, float]:
    """The unit the reject rule lets through with the largest true spread: believed exactly at the threshold, read low."""
    gm = g["g_minus_db"]
    x = R4.STEP_X_TOP_DB + gm
    return (f"+{x:.2f} dB true (believed +{R4.STEP_X_TOP_DB:g} dB, the reject threshold), read low", "typ", x, -gm)


def module_vd(vp, rf, eta, pin_dbm, f, vgg, ks, tc_key, T, xg, g135, g155, iters=120):
    """run_a5_r4.module_vec with the drain voltage returned too (for the pack current IBUS + Pmod / (eta Vd))."""
    vp, rf, eta, pin_dbm, f, vgg, ks = [np.asarray(a, dtype=float) for a in (vp, rf, eta, pin_dbm, f, vgg, ks)]
    tc = P.tc_by_key(tc_key)
    w = (f - 135e6) / 20e6
    pv = lambda x: (1 - w) * np.interp(x, T["xv"], T["v135"]) + w * np.interp(x, T["xv"], T["v155"])
    pt = lambda p: (1 - w) * 10 ** (np.interp(p, T["xp"], T["p135"]) / 10) + w * 10 ** (np.interp(p, T["xp"], T["p155"]) / 10)
    kd = pt(pin_dbm) / pt(13.0103)
    gv = lambda v: (1 - w) * np.interp(v, xg, g135) + w * np.interp(v, xg, g155)
    kv = gv(vgg) / gv(3.5)
    vd = np.array(np.broadcast_to(vp, np.broadcast(vp, rf, eta, pin_dbm, f, vgg, ks).shape), dtype=float)
    pm = np.zeros(vd.shape)
    for _ in range(iters):
        tcc = tc[4] if tc[4] is not None else tc[2] + P.RTH_CA["a5"] * (pm * (1 / eta - 1) + 10 ** ((pin_dbm - 30) / 10))
        dt = np.asarray(tcc) - 25.0
        kt = 10 ** (tc[5] * (np.maximum(dt, 0) if tc[6] else dt) / 10)
        pm = pv(np.maximum(vd, 3.0)) * kd * kv * ks * kt
        vd = 0.5 * vd + 0.5 * (vp - rf * (P.IBUS + pm / (eta * np.maximum(vd, 1.0))))
    return pm, vd


def read_deck(out: Path, deck_name: str, corners: list[dict]) -> dict:
    from spicelib import RawRead
    raw = RawRead(str(out / deck_name.replace(".cir", ".raw")))
    nst = len(raw.get_steps())
    vp = np.abs(raw.get_trace(raw.get_trace_names()[0]).get_wave(0))
    tr = lambda nm, f=lambda a: a: np.array([f(raw.get_trace(nm).get_wave(i)) for i in range(nst)])
    return {"nst": nst, "vp": vp, "M": tr("V(pmod)"), "TC": tr("V(tc)"), "VG": tr("V(vg)"), "VD": tr("V(d)"),
            "IP": tr("I(Vp)", np.abs), "corners": corners}


def population_stats(D: dict, units: list) -> dict:
    """Per unit case and temperature case: highest module output, pack current, module dissipation, PA case temperature
    (design feeds low, mid, bound; ALC at its top; over 6.4 to 8.4 V and at 6.4 V)."""
    vp, M, TC, IP, C = D["vp"], D["M"], D["TC"], D["IP"], D["corners"]
    i64 = int(np.argmin(np.abs(vp - 6.4)))
    eta = np.array([c["ieta"] for c in C])
    pinw = np.array([10 ** ((c["ipin"] - 30) / 10) for c in C])
    PD = M * (1 / eta - 1)[:, None] + pinw[:, None]
    ul = np.array([c["iu"] for c in C])
    tk = np.array([c["itc"] for c in C])
    design = np.isin(np.array([c["irf"] for c in C]), ["low", "mid", "bound"])
    out = {}
    for u in units:
        d = {}
        for tc in P.TC_CASES:
            m = (ul == u[0]) & (tk == tc[0]) & design
            ma = (ul == u[0]) & (tk == tc[0])
            d[tc[0]] = {"module_high_w": float(M[ma].max()), "pack_current_max_a": float(IP[m].max()),
                        "pack_current_6v4_a": float(IP[m][:, i64].max()), "pdiss_max_w": float(PD[m].max()),
                        "pdiss_6v4_w": float(PD[m][:, i64].max()), "case_max_c": float(TC[m].max()),
                        "pack_current_curve_a": IP[m].max(axis=0).tolist(), "pdiss_curve_w": PD[m].max(axis=0).tolist()}
        out[u[0]] = d
    return out


# ---------------------------------------------------------------- p4 / p5: the added unit case in the revision 4 deck
def run_p(key: str):
    import os
    out = rundir(key)
    k4 = R4K[key]
    V = VKEY5[key]
    s2 = json.loads((R4.rundir("r4s2") / "result.json").read_text())
    r4 = json.loads((R4.rundir(k4) / "result.json").read_text())
    g = R4.step_guard(s2)
    verdict(V, "check: the step terms and the step target equal revision 4's (g-, g+, target within 1e-9)",
            abs(g["g_minus_db"] - r4["step_guard"]["g_minus_db"]) < 1e-9 and abs(g["g_plus_db"] - r4["step_guard"]["g_plus_db"]) < 1e-9,
            "check", f"g- {g['g_minus_db']:.4f} dB, g+ {g['g_plus_db']:.4f} dB")
    ceil_w, design_w = R4.CEIL[k4]
    tgt = design_w * 10 ** (-g["g_minus_db"] / 10)
    pins = r4["pins_dbm"]
    units = [added_case(g)]
    u = units[0]
    verdict(V, "check: the added case's believed spread (true + error) equals the reject threshold (+1.5 dB) within 1e-9 dB",
            abs(u[2] + u[3] - R4.STEP_X_TOP_DB) < 1e-9, "check", f"true {u[2]:+.4f} dB, error {u[3]:+.4f} dB")
    deck, corners = R4.deck_p4r4(out, k4, pins, units, tgt)
    txt = deck.read_text().splitlines()
    txt[0] = "* power_a5_step.cir: A5 RA07M1317M, per-unit clamp step, revision 5: the added unit case of finding-31 only"
    txt[1] = (f"* (cwht WP-PDR-21 revision 5, hardware/sim/tx-pa/run_a5_r5.py {V}; record docs/design/analysis/pa-drive-ts012.md "
              f"section R5; the deck of revision 4 run {R4.RUNS4[k4]} with one unit case)")
    deck.write_text("\n".join(txt) + "\n")
    os.environ.setdefault("CWHT_LTSPICE_LOCK_WAIT", "14400")
    prov = P.run_ltspice(deck, out, timeout=14400)
    (out / "result.json").write_text(json.dumps({"run": RUNS5[key], "ltspice": prov}))
    D = read_deck(out, "power_a5_step.cir", corners)
    vp, M, TCW, VG, VD, IP = D["vp"], D["M"], D["TC"], D["VG"], D["VD"], D["IP"]
    verdict(V, "check: one .raw step per corner", D["nst"] == len(corners), "check", f"{D['nst']} steps")
    dev = 0.0
    for i, c in enumerate(corners):
        tc = P.tc_by_key(c["itc"])
        if tc[4] is None:
            want = tc[2] + P.RTH_CA["a5"] * (M[i] * (1 / c["ieta"] - 1) + 10 ** ((c["ipin"] - 30) / 10))
            dev = max(dev, float(np.max(np.abs(want - TCW[i]))))
    verdict(V, "check: PA case temperature equals the thermal law within 0.01 K at every pack voltage", dev <= 0.01, "check",
            f"largest difference {dev:.2e} K")
    T, xg, g135, g155, mc = R4.model_consts()
    lvs = [l[0] for l in R4.FEED3_LEVELS]
    top_py, dv = {}, 0.0
    for i, c in enumerate(corners):
        kk = (c["irf"], c["ieta"], c["ipin"])
        if kk not in top_py:
            top_py[kk] = R4.clamp_top_unit(vp, c["ieta"], c["ipin"], lvs.index(c["irf"]), u[1], u[2] + u[3], tgt, T, mc)
        want = top_py[kk] + c["ivgg"]
        dv = max(dv, float(np.max(np.abs(VG[i] - want) / (1e-3 * np.abs(want) + 1e-4))))
    verdict(V, "check: the deck clamp equals the checker's per-unit clamp within LTspice's reltol (0.1 % + 0.1 mV) at every pack voltage",
            dv <= 1.0, "check", f"largest difference {dv:.2f} of the tolerance")
    verdict(V, "check: VGG at most 3.50 V at every corner and pack voltage", float(VG.max()) <= 3.5 + 1e-4, "check", f"highest {float(VG.max()):.4f} V")
    kcl = 0.0
    for i, c in enumerate(corners):
        want = P.IBUS + M[i] / (c["ieta"] * np.maximum(VD[i], 1.0))
        kcl = max(kcl, float(np.max(np.abs(IP[i] / want - 1))))
    # tolerance: LTspice's reltol (0.1 %) on each of the two solved quantities V(pmod) and V(d), so 0.2 % on their ratio
    verdict(V, "check: pack current equals IBUS + Pmod / (eta Vd) within 0.2 % (reltol on V(pmod) and V(d)) at every corner and pack voltage", kcl <= 2e-3, "check",
            f"largest deviation {kcl * 100:.4f} %")
    # independent replica at 6.4 and 8.4 V, every corner (module output and pack current)
    rep = 0.0
    for vpk in (6.4, 8.4):
        j = int(np.argmin(np.abs(vp - vpk)))
        for tc in P.TC_CASES:
            ii = [i for i, c in enumerate(corners) if c["itc"] == tc[0]]
            cc = [corners[i] for i in ii]
            rf = np.array([c["rf_ohm"] for c in cc])
            eta = np.array([c["ieta"] for c in cc])
            pin = np.array([c["ipin"] for c in cc])
            fr = np.array([c["ifr"] for c in cc])
            vg = np.array([float(top_py[(c["irf"], c["ieta"], c["ipin"])][j]) + c["ivgg"] for c in cc])
            pm, vd = module_vd(np.full(len(cc), vpk), rf, eta, pin, fr, vg, np.full(len(cc), 10 ** (u[2] / 10)), tc[0], T, xg, g135, g155)
            ipk = P.IBUS + pm / (eta * np.maximum(vd, 1.0))
            rep = max(rep, float(np.max(np.abs(pm / M[ii, j] - 1))), float(np.max(np.abs(ipk / IP[ii, j] - 1))))
    verdict(V, "check: the Python replica equals the deck at 6.4 and 8.4 V within 0.5 % (module output and pack current, every corner)",
            rep <= 5e-3, "check", f"largest deviation {rep * 100:.3f} %")
    st = population_stats(D, units)[u[0]]
    kd = [tc[0] for tc in P.TC_CASES if tc[3] == "kd"]
    i64, i84 = int(np.argmin(np.abs(vp - 6.4))), int(np.argmin(np.abs(vp - 8.4)))
    res = {"run": RUNS5[key], "revision": REVISION, "ltspice": prov, "revision4_run": R4.RUNS4[k4], "n_deck_steps": len(corners),
           "vpack": vp.tolist(), "pins_dbm": pins, "ceiling_w": ceil_w, "design_w": design_w, "step_guard": g, "step_target_w": tgt,
           "unit": list(u), "vgg_offsets": R4.OFFS[k4], "by_tc": st, "kd_cases": kd,
           "module_high_all_w": float(M.max()), "module_high_all_8v4_w": float(M[:, i84].max()),
           "clamp_top_6v4": [float(min(t[i64] for t in top_py.values())), float(max(t[i64] for t in top_py.values()))],
           "clamp_top_8v4": [float(min(t[i84] for t in top_py.values())), float(max(t[i84] for t in top_py.values()))],
           "module_high_curve_w": M.max(axis=0).tolist()}
    verdict(V, f"A5 open loop, the added unit case (true +1.5 + g- dB, read low; believed at the reject threshold), 6.4 to 8.4 V, every case: module output at most {ceil_w:g} W",
            res["module_high_all_w"] <= ceil_w, detail=f"{res['module_high_all_w']:.3f} W")
    res["verdicts"] = VERDICTS.get(V, {})
    (out / "result.json").write_text(json.dumps(res, indent=0, default=str))
    # plot: the added case against pack voltage (module output highest, pack current and dissipation per key-down case)
    fig, axs = plt.subplots(1, 3, figsize=(15.5, 5.6))
    ax = axs[0]
    ax.plot(vp, res["module_high_curve_w"], color=INK, lw=1.8, label="module output, highest over every corner and case")
    ax.axhline(ceil_w, color=INK2, lw=1.4, ls=":", label=f"{ceil_w:g} W ceiling ({TAG[k4]})")
    ax.set_ylim(0, 11)
    ax.set_ylabel("Module output, ALC at its top (W)")
    ax.set_title("Module output (open loop above the ALC)", fontsize=9)
    for ax, fld, ylab, ttl in ((axs[1], "pack_current_curve_a", "Pack current, ALC at its top (A)", "Pack current, highest per key-down case"),
                               (axs[2], "pdiss_curve_w", "Module dissipation, ALC at its top (W)", "Module dissipation, highest per key-down case")):
        for k in kd:
            ax.plot(vp, st[k][fld], color=P.TC_COL[k], lw=1.3, label=P.tc_by_key(k)[1])
        ax.set_ylabel(ylab)
        ax.set_title(ttl, fontsize=9)
    for nm, a in HOLD_A.items():
        axs[1].axhline(a, color=INK2, lw=0.9, ls="--")
        axs[1].text(8.38, a + 0.02, nm, ha="right", va="bottom", fontsize=6.5, color=INK2)
    for ax in axs:
        ax.set_xlim(6.4, 8.4)
        ax.set_xlabel("Pack voltage, read in receive (V)")
        ax.grid(True, color="#e4e3df", lw=0.6)
    axs[0].legend(loc="lower center", fontsize=7)
    h, l = axs[1].get_legend_handles_labels()
    fig.legend(h, l, loc="lower center", ncol=4, fontsize=7.5)
    fig.suptitle(f"{V} (revision 5): A5, {TAG[k4]}, the added unit case: {u[0]} "
                 f"(g- {g['g_minus_db']:.2f} dB; step target {tgt:.2f} W); LTspice, {len(corners)} steps", fontsize=9.5)
    fig.tight_layout(rect=(0, 0.09, 1, 0.96))
    png = f"power_a5_added_case_{'d9' if k4 == 'r4p4' else 'clampb'}.png"
    fig.savefig(out / png, dpi=150)
    plt.close(fig)
    L = [f"# {res['run']}: A5 {TAG[k4]}, the added unit case of finding-31 (revision 5)", "",
         f"Deck: the revision 4 deck of `{R4.RUNS4[k4]}` with one unit case, {u[0]}: true spread {u[2]:+.3f} dB above the typical curve, "
         f"reading error {u[3]:+.3f} dB, believed {u[2] + u[3]:+.3f} dB. Step target {tgt:.3f} W (design {design_w} W, g- {g['g_minus_db']:.3f} dB). "
         f"{len(corners)} LTspice steps. All figures estimates.", "",
         "Checks and verdicts:"]
    for n, v in res["verdicts"].items():
        L.append(f"- {n}: **{'PASS' if v['pass'] else 'FAIL'}**" + (f" ({v['detail']})" if v["detail"] else ""))
    L += ["", f"Clamp top: {res['clamp_top_6v4'][0]:.3f} to {res['clamp_top_6v4'][1]:.3f} V at 6.4 V, "
          f"{res['clamp_top_8v4'][0]:.3f} to {res['clamp_top_8v4'][1]:.3f} V at 8.4 V.", "",
          "| Temperature case | Highest module output (W) | Pack current, 6.4 to 8.4 V (A) | Pack current at 6.4 V (A) | Module dissipation, 6.4 to 8.4 V (W) | PA case, highest (C) |",
          "|---|---|---|---|---|---|"]
    for tc in P.TC_CASES:
        d = st[tc[0]]
        L.append(f"| {tc[1]} | {d['module_high_w']:.2f} | {d['pack_current_max_a']:.2f} | {d['pack_current_6v4_a']:.2f} | "
                 f"{d['pdiss_max_w']:.2f} | {d['case_max_c']:.1f} |")
    L += ["", f"Plot `{png}`. Deck `power_a5_step.cir`; LTspice log beside it; `.raw` per `raw.sha256` when over 5,000,000 bytes.", ""]
    (out / "result.md").write_text("\n".join(L))
    copy_inputs(out, [deck])
    res["kept_raw"] = R3.raw_manifest(out)
    (out / "result.json").write_text(json.dumps(res, indent=0, default=str))
    print(key, json.dumps({"module_high_all_w": res["module_high_all_w"],
                           "pack": {k: st[k]["pack_current_max_a"] for k in kd}, "pdiss": {k: st[k]["pdiss_max_w"] for k in kd}}))
    return res


# ---------------------------------------------------------------- s5: the population that passes the reject rule
def r4_data(k4: str) -> tuple[dict, dict]:
    """Re-read a revision 4 power run: the .raw is checked against its committed raw.sha256 and the deck is regenerated
    from run_a5_r4.py and compared with the committed deck's SHA-256 (so the corner list is the one the .raw holds)."""
    d4 = R4.rundir(k4)
    r4 = json.loads((d4 / "result.json").read_text())
    man = [l.split() for l in (d4 / "raw.sha256").read_text().splitlines() if l and not l.startswith("#")]
    ok_raw = all(hashlib.sha256((d4 / nm).read_bytes()).hexdigest() == h for h, nm in man)
    s2 = json.loads((R4.rundir("r4s2") / "result.json").read_text())
    g = R4.step_guard(s2)
    tgt = R4.CEIL[k4][1] * 10 ** (-g["g_minus_db"] / 10)
    units = R4.unit_cases(g)
    with tempfile.TemporaryDirectory() as td:
        deck, corners = R4.deck_p4r4(Path(td), k4, r4["pins_dbm"], units, tgt)
        sha_regen = hashlib.sha256(deck.read_bytes()).hexdigest()
    ok_deck = sha_regen == r4["ltspice"]["deck_sha256"] == hashlib.sha256((d4 / "power_a5_step.cir").read_bytes()).hexdigest()
    D = read_deck(d4, "power_a5_step.cir", corners)
    return {"D": D, "units": units, "ok_raw": ok_raw, "ok_deck": ok_deck, "r4": r4, "g": g}, r4


def replica_sweep(k4: str, g: dict, pins: list, tgt: float, vpk: float, cases: list[str], xs, es):
    """Highest pack current and module dissipation (ALC at its top, design feeds) over (true spread x, error e)."""
    T, xg, g135, g155, mc = R4.model_consts()
    offs = R4.OFFS[k4]
    I = np.full((len(es), len(xs)), np.nan)
    Pd = np.full((len(es), len(xs)), np.nan)
    rows = [(k, lv, eta, pin, f, o) for k in cases for lv in range(3) for eta in P.A5_ETA for pin in pins for f in P.FREQS for o in offs]
    tops = {}
    for ie, e in enumerate(es):
        for ix, x in enumerate(xs):
            bel = x + e
            if bel > R4.STEP_X_TOP_DB + 1e-5:
                continue
            best_i, best_p = 0.0, 0.0
            for k in cases:
                rk = [r for r in rows if r[0] == k]
                rf = np.array([R3.feed3_at(k, r[1]) for r in rk])
                eta = np.array([r[2] for r in rk])
                pin = np.array([r[3] for r in rk])
                fr = np.array([r[4] for r in rk])
                vg = []
                for r in rk:
                    tk = (round(bel, 9), r[1], r[2], r[3])
                    if tk not in tops:
                        tops[tk] = float(R4.clamp_top_unit(np.array([vpk]), r[2], r[3], r[1], "typ", bel, tgt, T, mc)[0])
                    vg.append(tops[tk] + r[5])
                pm, vd = module_vd(np.full(len(rk), vpk), rf, eta, pin, fr, np.array(vg), np.full(len(rk), 10 ** (x / 10)), k, T, xg, g135, g155)
                best_i = max(best_i, float(np.max(P.IBUS + pm / (eta * np.maximum(vd, 1.0)))))
                best_p = max(best_p, float(np.max(pm * (1 / eta - 1) + 10 ** ((pin - 30) / 10))))
            I[ie, ix], Pd[ie, ix] = best_i, best_p
    return I, Pd


def run_s5():
    out = rundir("r5s5")
    V = "s5"
    res = {"run": RUNS5["r5s5"], "revision": REVISION, "scenarios": {}}
    kd = [tc[0] for tc in P.TC_CASES if tc[3] == "kd"]
    curves = {}
    for key in ("r5p4", "r5p5"):
        k4 = R4K[key]
        a, r4 = r4_data(k4)
        verdict(V, f"check: the revision 4 .raw of {R4.RUNS4[k4]} matches its committed raw.sha256", a["ok_raw"], "check")
        verdict(V, f"check: run_a5_r4.py regenerates the committed revision 4 deck of {R4.RUNS4[k4]} (SHA-256 equal)", a["ok_deck"], "check")
        r5 = json.loads((rundir(key) / "result.json").read_text())
        s4 = population_stats(a["D"], a["units"])
        s5c = r5["by_tc"]
        added = r5["unit"][0]
        g = a["g"]
        pop = []
        for u in a["units"] + [tuple(r5["unit"])]:
            bel = u[2] + u[3]
            st = s4.get(u[0]) if u[0] in s4 else s5c
            pop.append({"unit": u[0], "base": u[1], "true_db": u[2], "error_db": u[3], "believed_db": bel,
                        "passes_rule": bool(bel <= R4.STEP_X_TOP_DB + 1e-9),
                        "module_high_w": max(st[k]["module_high_w"] for k in st),
                        "pack_current_max_a": {k: st[k]["pack_current_max_a"] for k in st},
                        "pdiss_max_w": {k: st[k]["pdiss_max_w"] for k in st},
                        "case_max_c": {k: st[k]["case_max_c"] for k in st}})
        passing = [p for p in pop if p["passes_rule"]]
        r4pop = [p for p in pop if p["unit"] != added]
        summ = {}
        for tc in P.TC_CASES:
            k = tc[0]
            summ[k] = {"label": tc[1],
                       "pack_current_r4_a": max(p["pack_current_max_a"][k] for p in r4pop),
                       "pack_current_a": max(p["pack_current_max_a"][k] for p in passing),
                       "pack_current_unit": max(passing, key=lambda p: p["pack_current_max_a"][k])["unit"],
                       "pdiss_r4_w": max(p["pdiss_max_w"][k] for p in r4pop),
                       "pdiss_w": max(p["pdiss_max_w"][k] for p in passing),
                       "pdiss_unit": max(passing, key=lambda p: p["pdiss_max_w"][k])["unit"],
                       "case_r4_c": max(p["case_max_c"][k] for p in r4pop),
                       "case_c": max(p["case_max_c"][k] for p in passing)}
        ceil_w = R4.CEIL[k4][0]
        high = max(p["module_high_w"] for p in passing)
        verdict(V, f"A5 open loop, every unit that passes the reject rule (believed spread at most +1.5 dB, true spread up to +1.5 + g- dB), "
                   f"6.4 to 8.4 V, every case: module output at most {ceil_w:g} W ({TAG[k4]})", high <= ceil_w, detail=f"{high:.3f} W")
        # the replica sweep over the passing region (25 C and +45 C key-down, at 6.4 V where the added case peaks)
        xs = np.round(np.arange(0.0, R4.STEP_X_TOP_DB + g["g_minus_db"] + 1e-9, (R4.STEP_X_TOP_DB + g["g_minus_db"]) / 20), 6)
        es = np.round(np.linspace(-g["g_minus_db"], g["g_plus_db"], 13), 6)
        sw = {}
        for k in ("t25a", "hot45a"):
            vpk = float(np.array(a["D"]["vp"])[int(np.argmax(np.array(s5c[k]["pack_current_curve_a"])))])
            I, Pd = replica_sweep(k4, g, r4["pins_dbm"], r5["step_target_w"], vpk, [k], xs, es)
            ie, ix = np.unravel_index(np.nanargmax(I), I.shape)
            sw[k] = {"vpack": vpk, "I": I.tolist(), "Pd": Pd.tolist(), "argmax_true_db": float(xs[ix]), "argmax_error_db": float(es[ie]),
                     "max_a": float(np.nanmax(I)), "deck_added_a": float(np.array(s5c[k]["pack_current_curve_a"]).max())}
        corner_ok = all(abs(sw[k]["argmax_true_db"] - (R4.STEP_X_TOP_DB + g["g_minus_db"])) < 1e-6 and abs(sw[k]["argmax_error_db"] + g["g_minus_db"]) < 1e-6
                        and abs(sw[k]["max_a"] / sw[k]["deck_added_a"] - 1) < 5e-3 for k in sw)
        verdict(V, f"check: over the passing region the replica's highest pack current is at the added case (true +1.5 + g-, read low) and equals the deck within 0.5 % ({TAG[k4]})",
                corner_ok, "check", "; ".join(f"{k}: replica {sw[k]['max_a']:.3f} A at ({sw[k]['argmax_true_db']:+.2f}, {sw[k]['argmax_error_db']:+.2f}) dB, "
                                               f"deck {sw[k]['deck_added_a']:.3f} A" for k in sw))
        res["scenarios"][TAG[k4]] = {"revision4_run": R4.RUNS4[k4], "revision5_run": RUNS5[key], "ceiling_w": ceil_w, "step_guard": g,
                                     "population": pop, "summary": summ, "module_high_passing_w": high,
                                     "sweep": {"xs": xs.tolist(), "es": es.tolist(), **sw}}
        vp = np.array(a["D"]["vp"])
        curves[TAG[k4]] = {"vp": vp, "r4": {k: np.max([s4[u[0]][k]["pack_current_curve_a"] for u in a["units"]], axis=0) for k in ("t25a", "hot45a")},
                           "r5": {k: np.array(s5c[k]["pack_current_curve_a"]) for k in ("t25a", "hot45a")},
                           "r4p": {k: np.max([s4[u[0]][k]["pdiss_curve_w"] for u in a["units"]], axis=0) for k in ("t25a", "hot45a")},
                           "r5p": {k: np.array(s5c[k]["pdiss_curve_w"]) for k in ("t25a", "hot45a")}}
    res["verdicts"] = VERDICTS.get(V, {})
    (out / "result.json").write_text(json.dumps(res, indent=0, default=str))
    # plot 1: the passing region with the replica's pack current (scenario B, 25 C key-down), the unit cases marked
    sB = res["scenarios"]["scenario B (10 W)"]
    fig, axs = plt.subplots(1, 2, figsize=(14.2, 6.0))
    for ax, sc in zip(axs, ("scenario B (10 W)", "D-9 (8 W)")):
        s = res["scenarios"][sc]
        xs, es = np.array(s["sweep"]["xs"]), np.array(s["sweep"]["es"])
        I = np.array(s["sweep"]["t25a"]["I"], dtype=float)
        im = ax.pcolormesh(xs, es, I, shading="nearest", cmap="Blues")
        cb = fig.colorbar(im, ax=ax)
        cb.set_label(f"Highest pack current, 25 C key-down, at {s['sweep']['t25a']['vpack']:.2f} V (A)", fontsize=8)
        xx = np.linspace(-0.1, 2.7, 10)
        ax.plot(xx, R4.STEP_X_TOP_DB - xx, color=INK, lw=1.6, label="reject threshold: believed spread (true + error) = +1.5 dB")
        ax.axhline(-s["step_guard"]["g_minus_db"], color=INK2, lw=0.9, ls=":")
        ax.axhline(s["step_guard"]["g_plus_db"], color=INK2, lw=0.9, ls=":", label="reading bound: -g- and +g+")
        ax.axvline(R4.STEP_X_TOP_DB, color=COL["a4"], lw=1.1, ls="--", label="+1.5 dB: the true bound revision 4 stated")
        for p in s["population"]:
            if p["base"] != "typ":
                continue
            new = p["unit"].startswith("+2")
            ax.plot(p["true_db"], p["error_db"], "*" if new else ("o" if p["passes_rule"] else "x"), ms=13 if new else 8,
                    color=COL["a4"] if new else (COL["ok"] if p["passes_rule"] else INK), mec=INK, ls="none")
            right = p["true_db"] > 2.0
            ax.annotate(f"true {p['true_db']:+.2f}, error {p['error_db']:+.2f} dB\n{p['pack_current_max_a']['t25a']:.2f} A"
                        + ("" if p["passes_rule"] else " (rejected by the rule)"),
                        (p["true_db"], p["error_db"]), textcoords="offset points", xytext=(-8, -30) if right else (7, 9),
                        ha="right" if right else "left", fontsize=6.8, bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.8))
        ax.set_xlim(-0.1, 2.7)
        ax.set_ylim(-1.45, 1.3)
        ax.set_xlabel("True spread of the module above the typical curve (dB)")
        ax.set_ylabel("Reading error of the step, read minus true (dB)")
        ax.set_title(f"{sc}: passing units lie on or left of the black line, inside the dotted bound", fontsize=8.5)
    h, l = axs[0].get_legend_handles_labels()
    fig.legend(h, l, loc="lower center", ncol=3, fontsize=7.5)
    fig.suptitle("s5 (revision 5): the reject rule acts on the believed spread; a unit up to +1.5 + g- dB passes when read low (replica, pack current with the ALC at its top)", fontsize=9.5)
    fig.tight_layout(rect=(0, 0.06, 1, 0.96))
    fig.savefig(out / "pass_population.png", dpi=150)
    plt.close(fig)
    # plot 2: pack current and dissipation against pack voltage, revision 4 population and with the added case
    fig, axs = plt.subplots(1, 2, figsize=(14.2, 6.0))
    sty = {"scenario B (10 W)": (COL["a5"], "-"), "D-9 (8 W)": (COL["aux"], "-")}
    for sc, cv in curves.items():
        col, _ = sty[sc]
        for k, ls in (("t25a", "-"), ("hot45a", "--")):
            lab = "25 C key-down" if k == "t25a" else "+45 C key-down"
            axs[0].plot(cv["vp"], cv["r5"][k], color=col, lw=2.0, ls=ls, label=f"{sc}, {lab}: with the added case (revision 5)")
            axs[0].plot(cv["vp"], cv["r4"][k], color=col, lw=0.9, ls=ls, alpha=0.55, label=f"{sc}, {lab}: revision 4 unit cases")
            axs[1].plot(cv["vp"], cv["r5p"][k], color=col, lw=2.0, ls=ls, label=f"{sc}, {lab}: with the added case")
            axs[1].plot(cv["vp"], cv["r4p"][k], color=col, lw=0.9, ls=ls, alpha=0.55, label=f"{sc}, {lab}: revision 4 unit cases")
    for nm, a in HOLD_A.items():
        axs[0].axhline(a, color=INK2, lw=0.9, ls=":")
        axs[0].text(8.38, a + 0.02, nm, ha="right", va="bottom", fontsize=7, color=INK2)
    axs[0].set_ylabel("Pack current, ALC at its top, highest (A)")
    axs[1].set_ylabel("Module dissipation, ALC at its top, highest (W)")
    for ax in axs:
        ax.set_xlim(6.4, 8.4)
        ax.set_xlabel("Pack voltage, read in receive (V)")
        ax.grid(True, color="#e4e3df", lw=0.6)
    h, l = axs[0].get_legend_handles_labels()
    fig.legend(h, l, loc="lower center", ncol=2, fontsize=7)
    axs[0].set_title("Pack current (request R3-3 to WP-PDR-24)", fontsize=9)
    axs[1].set_title("Module dissipation (HZ-003, WP-PDR-28)", fontsize=9)
    fig.suptitle("s5 (revision 5): the added case (true +2.49 dB, read low) sets the pack current and the dissipation at the low-pack end (LTspice, r4 and r5 decks)", fontsize=9.5)
    fig.tight_layout(rect=(0, 0.17, 1, 0.96))
    fig.savefig(out / "pack_current_dissipation.png", dpi=150)
    plt.close(fig)
    L = [f"# {res['run']}: the population that passes the clamp step's reject rule (revision 5, finding-31)", "",
         "The reject rule acts on the believed spread (true spread plus reading error): a unit passes when its believed spread is at most "
         f"+{R4.STEP_X_TOP_DB:g} dB. Revision 4's seven unit cases (runs r4-p4, r4-p5, re-read) and the added case (runs r5-p4, r5-p5). "
         "Design feeds (low, mid, bound); ALC at its top; 6.4 to 8.4 V. All figures estimates.", "", "Checks and verdicts:"]
    for n, v in res["verdicts"].items():
        L.append(f"- {n}: **{'PASS' if v['pass'] else 'FAIL'}**" + (f" ({v['detail']})" if v["detail"] else ""))
    for sc, s in res["scenarios"].items():
        L += ["", f"## {sc}", "", "| Unit case | True (dB) | Error (dB) | Believed (dB) | Passes the rule | Highest module (W) | Pack current 25 C / +45 C key-down (A) | Dissipation 25 C / +45 C key-down (W) |",
              "|---|---|---|---|---|---|---|---|"]
        for p in s["population"]:
            L.append(f"| {p['unit']} | {p['true_db']:+.2f} | {p['error_db']:+.2f} | {p['believed_db']:+.2f} | {'yes' if p['passes_rule'] else 'no'} | "
                     f"{p['module_high_w']:.2f} | {p['pack_current_max_a']['t25a']:.2f} / {p['pack_current_max_a']['hot45a']:.2f} | "
                     f"{p['pdiss_max_w']['t25a']:.2f} / {p['pdiss_max_w']['hot45a']:.2f} |")
        L += ["", "| Temperature case | Pack current, revision 4 cases (A) | Pack current, passing population (A) | Dissipation, revision 4 cases (W) | Dissipation, passing population (W) | PA case, revision 4 / passing (C) |",
              "|---|---|---|---|---|---|"]
        for k, d in s["summary"].items():
            L.append(f"| {d['label']} | {d['pack_current_r4_a']:.2f} | {d['pack_current_a']:.2f} | {d['pdiss_r4_w']:.2f} | {d['pdiss_w']:.2f} | {d['case_r4_c']:.1f} / {d['case_c']:.1f} |")
        L.append(f"\nHighest module output over the passing population: {s['module_high_passing_w']:.3f} W (ceiling {s['ceiling_w']:g} W).")
    L += ["", "Plots `pass_population.png` (the passing region with the replica's pack current), `pack_current_dissipation.png`.", ""]
    (out / "result.md").write_text("\n".join(L))
    copy_inputs(out, [])
    print("s5", json.dumps({sc: {k: (s["summary"][k]["pack_current_a"], s["summary"][k]["pdiss_w"]) for k in kd} for sc, s in res["scenarios"].items()}))
    return res


EXPECTED: dict[str, dict[str, bool]] = {  # the verdict list of the analysis record section R5.6 (2026-09-30)
    'p4': {
        "check: the step terms and the step target equal revision 4's (g-, g+, target within 1e-9)": True,
        "check: the added case's believed spread (true + error) equals the reject threshold (+1.5 dB) within 1e-9 dB": True,
        'check: one .raw step per corner': True,
        'check: PA case temperature equals the thermal law within 0.01 K at every pack voltage': True,
        "check: the deck clamp equals the checker's per-unit clamp within LTspice's reltol (0.1 % + 0.1 mV) at every pack voltage": True,
        'check: VGG at most 3.50 V at every corner and pack voltage': True,
        'check: pack current equals IBUS + Pmod / (eta Vd) within 0.2 % (reltol on V(pmod) and V(d)) at every corner and pack voltage': True,
        'check: the Python replica equals the deck at 6.4 and 8.4 V within 0.5 % (module output and pack current, every corner)': True,
        'A5 open loop, the added unit case (true +1.5 + g- dB, read low; believed at the reject threshold), 6.4 to 8.4 V, every case: module output at most 8 W': True,
    },
    'p5': {
        "check: the step terms and the step target equal revision 4's (g-, g+, target within 1e-9)": True,
        "check: the added case's believed spread (true + error) equals the reject threshold (+1.5 dB) within 1e-9 dB": True,
        'check: one .raw step per corner': True,
        'check: PA case temperature equals the thermal law within 0.01 K at every pack voltage': True,
        "check: the deck clamp equals the checker's per-unit clamp within LTspice's reltol (0.1 % + 0.1 mV) at every pack voltage": True,
        'check: VGG at most 3.50 V at every corner and pack voltage': True,
        'check: pack current equals IBUS + Pmod / (eta Vd) within 0.2 % (reltol on V(pmod) and V(d)) at every corner and pack voltage': True,
        'check: the Python replica equals the deck at 6.4 and 8.4 V within 0.5 % (module output and pack current, every corner)': True,
        'A5 open loop, the added unit case (true +1.5 + g- dB, read low; believed at the reject threshold), 6.4 to 8.4 V, every case: module output at most 10 W': True,
    },
    's5': {
        'check: the revision 4 .raw of 2026-09-29-r4-p4-power-a5-design matches its committed raw.sha256': True,
        'check: run_a5_r4.py regenerates the committed revision 4 deck of 2026-09-29-r4-p4-power-a5-design (SHA-256 equal)': True,
        'A5 open loop, every unit that passes the reject rule (believed spread at most +1.5 dB, true spread up to +1.5 + g- dB), 6.4 to 8.4 V, every case: module output at most 8 W (D-9 (8 W))': True,
        "check: over the passing region the replica's highest pack current is at the added case (true +1.5 + g-, read low) and equals the deck within 0.5 % (D-9 (8 W))": True,
        'check: the revision 4 .raw of 2026-09-29-r4-p5-power-a5-clamp-b matches its committed raw.sha256': True,
        'check: run_a5_r4.py regenerates the committed revision 4 deck of 2026-09-29-r4-p5-power-a5-clamp-b (SHA-256 equal)': True,
        'A5 open loop, every unit that passes the reject rule (believed spread at most +1.5 dB, true spread up to +1.5 + g- dB), 6.4 to 8.4 V, every case: module output at most 10 W (scenario B (10 W))': True,
        "check: over the passing region the replica's highest pack current is at the added case (true +1.5 + g-, read low) and equals the deck within 0.5 % (scenario B (10 W))": True,
    },
}


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    what = args[0] if args else "all"
    order = ["p4", "p5", "s5"]
    todo = order if what == "all" else [what]
    fns = {"p4": lambda: run_p("r5p4"), "p5": lambda: run_p("r5p5"), "s5": run_s5}
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
