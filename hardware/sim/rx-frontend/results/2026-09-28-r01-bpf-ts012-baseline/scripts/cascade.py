"""Receiver noise and gain cascade (REQ-SYS-022 MDS) and the half-IF referral (REQ-SYS-033) for the TS-012
finalists, with the band-pass filter losses taken from the LTspice runs r01 to r03 and the mixer data from r05.
Writes results/2026-09-28-r06-cascade/ (result.json, result.md, PNG plots).
Usage: .venv/bin/python hardware/sim/rx-frontend/cascade.py

Every device value that is not an LTspice result is an estimate with its basis given in STAGE_NOTES; the
LTspice-derived numbers are marked "sim". MDS = -174 dBm/Hz + 10 log10(500 Hz) + NF = -147 dBm + NF
(REQ-SYS-022 verification note; docs/research/2m-cw-transceiver-reference-designs.md F14)."""
import json, math, os, shutil
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(HERE, "results")
OUT = os.path.join(RES, "2026-09-28-r06-cascade")
REQ_MDS = -140.0   # REQ-SYS-022 (TBR)
GOAL_MDS = -142.0  # REQ-SYS-023 (Goal, TBR)
KTB = -174.0 + 10 * math.log10(500.0)

STAGE_NOTES = {
    "relay": "G5V-2 pole, 1N5711 clamp pair and input trace: 0.3 dB nominal, 0.5 dB corner (estimate, Low: signal relay not rated at VHF)",
    "j310": "MMBFJ310 grounded gate: gain 12 dB nominal / 10 dB corner, NF 2.5 / 3.0 dB (estimate from onsemi MMBFJ310 datasheet Gpg 16 dB typ at 100 MHz and NF 3.0 dB typ at 450 MHz, both at VDS 10 V, ID 10 mA; derated for the 5 V rail and tuned-drain loss)",
    "pad": "3 dB pad between BPF3 and the ring (proposed with the third section: fixes the filter termination against the ring's LO-varying RF port)",
    "ring": "diode ring, 4 x 1N5711: conversion loss = LTspice r05 Gc (matched set) + 1.0 dB nominal / + 2.0 dB corner for BN-43-202 core and winding loss not modelled (estimate); SSB NF = loss",
    "jfet": "single J310 mixer (A4): conversion gain +3 dB nominal / 0 dB corner, SSB NF 10 / 12 dB (estimate, Low: no A4 schematic or measurement exists; typical of a source-injected JFET mixer)",
    "diplexer": "diplexer 0.5 dB (estimate)",
    "pma": "2N3904 post-mixer amplifier: gain 15 dB, NF 5 dB nominal / 6 dB corner (estimate)",
    "xtal": "6-pole 500 Hz ladder at 8.000 MHz: loss 10 dB nominal / 12 dB corner (estimate from docs/research/cw-selectivity-options.md F7: 10.7 dB for 6 poles at 9 MHz, Rs 15 ohm); at 10 MHz +1 dB (f0/B scaling, estimate)",
    "ifa": "two 2N3904 IF stages: 20 dB each, NF 5 dB (estimate); product detector NF 15 dB (estimate)",
    "image_noise": "two-section front ends: the second J310's own output noise in the image band reaches the mixer unfiltered, so its noise counts twice (term F_J2 / G_before_J2 added; conservative, input taken at 290 K)",
}


def load(run, name):
    return json.load(open(os.path.join(RES, run, name)))


def bpf_losses():
    """Worst in-band loss per section: nominal at coil Q 120 (catalog typical; hand-wound estimate similar or
    higher) from r01/r02, and the tolerance corner as the 95th percentile of Monte Carlo mode B (coil Q 100,
    proposed part specification) from r01/r03."""
    q = {}
    for run in ("2026-09-28-r01-bpf-ts012-baseline", "2026-09-28-r02-bpf-three-section"):
        for it in load(run, "result.json")["items"]:
            if "steps" in it:
                for st in it["steps"]:
                    q[(it["deck"], st["step"])] = st["metrics"]
    mc = {}
    for run in ("2026-09-28-r01-bpf-ts012-baseline", "2026-09-28-r03-bpf-three-section-mc"):
        for it in load(run, "result.json")["items"]:
            if "summary" in it:
                mc[it["deck"]] = it["summary"]
    return q, mc


def cascade(stages):
    """stages: list of (name, nf_db, gain_db). Returns total NF (dB), gain (dB), running NF and gain lists."""
    F = 1.0
    G = 1.0
    runF, runG = [], []
    for i, (name, nf, g) in enumerate(stages):
        f = 10 ** (nf / 10)
        F = f if i == 0 else F + (f - 1) / G
        G *= 10 ** (g / 10)
        runF.append(10 * math.log10(F))
        runG.append(10 * math.log10(G))
    return runF[-1], runG[-1], runF, runG


def build(cfg, corner, bpf_loss, ring_gc):
    """corner: device values at their corner (True) or nominal (False); bpf_loss: the section losses to use."""
    c = corner
    st = [("relay, clamps", 0.5 if c else 0.3, -(0.5 if c else 0.3))]
    jg, jn = (10.0, 3.0) if c else (12.0, 2.5)
    L = bpf_loss
    st.append(("BPF1", L[0], -L[0]))
    st.append(("J310 #1", jn, jg))
    st.append(("BPF2", L[1], -L[1]))
    st.append(("J310 #2", jn, jg))
    if len(L) == 3:
        st.append(("BPF3", L[2], -L[2]))
        if cfg.get("pad", False):
            st.append(("3 dB pad", 3.0, -3.0))
    if cfg["mixer"] == "ring":
        lm = -ring_gc + (2.0 if c else 1.0)
        st.append(("diode ring", lm, -lm))
    else:
        g, nf = (0.0, 12.0) if c else (3.0, 10.0)
        st.append(("JFET mixer", nf, g))
    st.append(("diplexer", 0.5, -0.5))
    st.append(("2N3904 PMA", 6.0 if c else 5.0, 15.0))
    xl = (12.0 if c else 10.0) + (1.0 if cfg["if_mhz"] == 10 else 0.0)
    st.append(("crystal ladder", xl, -xl))
    st.append(("IF amp 1", 5.0, 20.0))
    st.append(("IF amp 2", 5.0, 20.0))
    st.append(("product det.", 15.0, 0.0))
    nf, g, rF, rG = cascade(st)
    img_term = 0.0
    if len(L) == 2:
        # gain before the second J310 (linear) and its noise factor
        gb = 10 ** ((st[0][2] + st[1][2] + st[2][2] + st[3][2]) / 10)
        fj = 10 ** (jn / 10)
        F = 10 ** (nf / 10) + fj / gb
        img_term = 10 * math.log10(F) - nf
        nf = 10 * math.log10(F)
    nfe = 5 + (1 if len(L) == 3 else 0) + (1 if cfg.get("pad", False) else 0)
    gfe = sum(s[2] for s in st[:nfe])  # antenna to mixer RF port
    return dict(stages=st, nf_db=nf, gain_db=g, running_nf=rF, running_gain=rG, image_noise_db=img_term,
                mds_dbm=KTB + nf, g_fe_db=gfe)


CONFIGS = [
    dict(key="A5-ts012", label="A5 as TS-012 rev 4 (BPF 2+3, IF 8)", mixer="ring", if_mhz=8, deck="bpf_2p3_bw6", mc="bpf_2p3_bw6_mcB", finalist="A5"),
    dict(key="A5-R1", label="A5 + BPF3 (2+3+3, IF 8), proposed", mixer="ring", if_mhz=8, deck="bpf_2p3p3_bw6", mc="bpf_2p3p3_bw6_mcB", finalist="A5"),
    dict(key="A5-R1p", label="A5 + BPF3 + 3 dB pad before the ring", mixer="ring", if_mhz=8, deck="bpf_2p3p3_bw6", mc="bpf_2p3p3_bw6_mcB", finalist="A5", pad=True),
    dict(key="A5-R2", label="A5, IF 10 MHz, BPF 2+3+2 (alternative)", mixer="ring", if_mhz=10, deck="bpf_2p3p2_bw6", mc="bpf_2p3p2_bw6_mcB", finalist="A5"),
    dict(key="A4-ts012", label="A4 as TS-012 rev 4 (BPF 2+3, JFET mixer)", mixer="jfet", if_mhz=8, deck="bpf_2p3_bw6", mc="bpf_2p3_bw6_mcB", finalist="A4"),
    dict(key="A4-R1", label="A4 + BPF3 (2+3+3, JFET mixer)", mixer="jfet", if_mhz=8, deck="bpf_2p3p3_bw6", mc="bpf_2p3p3_bw6_mcB", finalist="A4"),
]


def main():
    os.makedirs(OUT, exist_ok=True)
    q, mc = bpf_losses()
    hif = load("2026-09-28-r05-halfif-mixers", "result.json")["mixers"]
    ring = hif["halfif_ring"]
    ring_gc = [s for s in ring["sets"] if s["set"] == 0][0]["gc_db"]
    ring_iip2 = min(s["iip2_hif_dbm"] for s in ring["sets"] if s["set"] != 0)
    ring_floor = ring["relative_floor_dbc"]
    jf = hif.get("halfif_jfet")
    jf_iip2 = None
    if jf and jf["sets"]:
        vals = [s["iip2_hif_dbm"] for s in jf["sets"] if not s["iip2_is_lower_bound"]]
        jf_iip2 = min(vals) if vals else None
    rows = []
    for cfg in CONFIGS:
        mq = q[(cfg["deck"], "qu=120")]
        L_nom = mq["section_loss_worst_db"]
        L_cor = mc[cfg["mc"]]["section_loss_worst_db_p95"]
        nom = build(cfg, False, L_nom, ring_gc)
        fco = build(cfg, False, L_cor, ring_gc)   # filter corner: Monte Carlo mode B p95 losses, devices nominal
        cor = build(cfg, True, L_cor, ring_gc)    # stack: filter corner and every device at its corner at once
        iflab = f"IF {cfg['if_mhz']} MHz"
        # image rejection: nominal Q 100 and Q 120, MC modes A and B minimum
        q100 = q[(cfg["deck"], "qu=100")][iflab]["image_rejection_min_db"]
        q120 = mq[iflab]["image_rejection_min_db"]
        mcb = mc[cfg["mc"]][iflab]["image_rejection_min_db"]
        mca = mc[cfg["mc"].replace("mcB", "mcA")][iflab]["image_rejection_min_db"]
        hif_att = min(mc[cfg["mc"]][f"halfif_filter_atten_min_db_IF{cfg['if_mhz']}"], q[(cfg["deck"], "qu=100")][iflab]["halfif_filter_atten_min_db"])
        hif_att = max(hif_att, 0.0)
        # half-IF referral for a -70 dBm antenna tone (TS-012 rev 4 section 7.3 criterion)
        hres = {}
        for tag, r in (("nominal", nom), ("corner", cor)):
            pmix = -70.0 + r["g_fe_db"] - hif_att
            if cfg["mixer"] == "ring":
                peq_mix = 2 * pmix - ring_iip2
                floor_peq = pmix + ring_floor  # the time-step floor, not physical
            else:
                peq_mix = (2 * pmix - jf_iip2) if jf_iip2 is not None else None
                floor_peq = None
            peq_ant = None if peq_mix is None else peq_mix - r["g_fe_db"]
            hres[tag] = dict(p_mixer_dbm=pmix, p_eq_antenna_dbm=peq_ant,
                             floor_bound_antenna_dbm=None if floor_peq is None else floor_peq - r["g_fe_db"],
                             pass_=None if peq_ant is None else bool(peq_ant <= -140.0))
        # leakage: isolation needed from the antenna port to the mixer RF port at the image frequency
        iso_needed = 70.0 + nom["g_fe_db"]
        rows.append(dict(cfg=cfg, nominal=nom, filter_corner=fco, corner=cor, bpf_loss_nominal_q120=L_nom, bpf_loss_corner_mcB_p95=L_cor,
                         image=dict(q100_nominal=q100, q120_nominal=q120, mc_modeA_min=mca, mc_modeB_min=mcb,
                                    pass_70=bool(min(q100, mcb) >= 70.0), pass_70_modeA=bool(mca >= 70.0)),
                         halfif_filter_atten_db=hif_att, halfif=hres, isolation_needed_db=iso_needed,
                         mds_pass_nominal=bool(nom["mds_dbm"] <= REQ_MDS), mds_pass_filter_corner=bool(fco["mds_dbm"] <= REQ_MDS),
                         mds_pass_corner=bool(cor["mds_dbm"] <= REQ_MDS)))
    # plots
    fig, axs = plt.subplots(2, 3, figsize=(17, 10))
    for ax, r in zip(axs.flat, rows):
        st = r["nominal"]["stages"]
        names = [n for n, _, _ in st]
        xx = np.arange(len(names))
        ax.plot(xx, r["nominal"]["running_nf"], "o-", color="tab:blue", label="cumulative NF, nominal")
        ax.plot(xx, r["filter_corner"]["running_nf"], "s--", color="tab:orange", ms=4, label="cumulative NF, filter corner")
        ax.axhline(7.0, color="k", ls="--", lw=1, label="NF 7 dB = MDS -140 dBm (REQ-SYS-022)")
        ax.axhline(5.0, color="grey", ls=":", lw=1, label="NF 5 dB = MDS -142 dBm (goal)")
        ax.set_ylim(0, 12); ax.set_ylabel("NF at the antenna port (dB)")
        ax.set_xticks(xx); ax.set_xticklabels(names, rotation=60, ha="right", fontsize=7)
        a2 = ax.twinx()
        a2.plot(xx, r["nominal"]["running_gain"], "^:", color="tab:green", ms=4, label="cumulative gain, nominal")
        a2.set_ylim(-10, 80); a2.set_ylabel("gain (dB)", color="tab:green")
        extra = f"; + image noise {r['nominal']['image_noise_db']:.2f} dB" if r["nominal"]["image_noise_db"] else ""
        ax.set_title(f"{r['cfg']['label']}\nNF {r['nominal']['nf_db']:.2f} / {r['filter_corner']['nf_db']:.2f} dB, MDS {r['nominal']['mds_dbm']:.1f} / {r['filter_corner']['mds_dbm']:.1f} dBm (nominal / filter corner){extra}", fontsize=8)
        ax.grid(alpha=0.3)
        if r is rows[0]:
            h1, l1 = ax.get_legend_handles_labels(); h2, l2 = a2.get_legend_handles_labels()
            ax.legend(h1 + h2, l1 + l2, fontsize=6.5, loc="upper left")
    fig.tight_layout(); p1 = os.path.join(OUT, "cascade_nf_gain.png"); fig.savefig(p1, dpi=120); plt.close(fig)

    fig, axs = plt.subplots(1, 3, figsize=(17, 5.5))
    labs = [r["cfg"]["key"] for r in rows]
    x = np.arange(len(rows))
    axs[0].bar(x - 0.27, [r["nominal"]["mds_dbm"] for r in rows], 0.27, label="nominal (Q 120, nominal devices)")
    axs[0].bar(x, [r["filter_corner"]["mds_dbm"] for r in rows], 0.27, label="filter corner (MC mode B p95 losses)")
    axs[0].bar(x + 0.27, [r["corner"]["mds_dbm"] for r in rows], 0.27, label="stack (filter corner + every device corner)")
    axs[0].axhline(REQ_MDS, color="k", ls="--", label="REQ-SYS-022: -140 dBm")
    axs[0].axhline(GOAL_MDS, color="grey", ls=":", label="REQ-SYS-023 goal: -142 dBm")
    axs[0].set_ylim(-130, -146); axs[0].set_xticks(x); axs[0].set_xticklabels(labs, rotation=20, fontsize=8)
    axs[0].set_ylabel("MDS in 500 Hz (dBm); axis inverted, taller bar = more sensitive"); axs[0].set_title("MDS against REQ-SYS-022"); axs[0].legend(fontsize=7); axs[0].grid(alpha=0.3, axis="y")
    axs[1].bar(x - 0.3, [r["image"]["q100_nominal"] for r in rows], 0.2, label="nominal, Q 100")
    axs[1].bar(x - 0.1, [r["image"]["q120_nominal"] for r in rows], 0.2, label="nominal, Q 120")
    axs[1].bar(x + 0.1, [r["image"]["mc_modeB_min"] for r in rows], 0.2, label="MC mode B minimum (proposed parts)")
    axs[1].bar(x + 0.3, [r["image"]["mc_modeA_min"] for r in rows], 0.2, label="MC mode A minimum (TS-012 20 %)")
    axs[1].axhline(70, color="k", ls="--", label="REQ-SYS-033: 70 dB"); axs[1].axhline(90, color="k", ls=":", label="TS-012 90 dB")
    axs[1].set_xticks(x); axs[1].set_xticklabels(labs, rotation=20, fontsize=8); axs[1].set_ylabel("worst image rejection (dB)")
    axs[1].set_ylim(0, 110)
    axs[1].set_title("Image rejection (filters only; board leakage not included)"); axs[1].legend(fontsize=7, ncol=2, loc="upper left"); axs[1].grid(alpha=0.3, axis="y")
    for tag, mk, col in (("nominal", "o", "tab:blue"), ("corner", "s", "tab:green")):
        xs = [i for i, r in enumerate(rows) if r["halfif"][tag]["p_eq_antenna_dbm"] is not None]
        ys = [rows[i]["halfif"][tag]["p_eq_antenna_dbm"] for i in xs]
        axs[2].plot(xs, ys, mk, color=col, ms=9, ls="none", label=f"{tag} gains (stack corner)" if tag == "corner" else "nominal gains (worst case: highest gain)")
    fb = [(i, r["halfif"]["nominal"]["floor_bound_antenna_dbm"]) for i, r in enumerate(rows) if r["halfif"]["nominal"]["floor_bound_antenna_dbm"] is not None]
    axs[2].plot([a for a, b in fb], [b for a, b in fb], "r_", ms=22, mew=2, ls="none", label="ring time-step floor, referred (not physical)")
    axs[2].axhline(-140, color="k", ls="--", label="REQ-SYS-033 at -70 dBm: -140 dBm")
    axs[2].set_ylim(-200, -120); axs[2].set_xticks(x); axs[2].set_xticklabels(labs, rotation=20, fontsize=8)
    axs[2].set_ylabel("equivalent antenna level of the half-IF response (dBm)")
    axs[2].set_title("Half-IF, -70 dBm tone at f - 4 MHz (lower is better)"); axs[2].legend(fontsize=7, loc="upper right"); axs[2].grid(alpha=0.3)
    fig.tight_layout(); p2 = os.path.join(OUT, "cascade_verdicts.png"); fig.savefig(p2, dpi=130); plt.close(fig)

    res = dict(run_id="2026-09-28-r06-cascade", checker="cascade.py", ktb_500hz_dbm=KTB, stage_notes=STAGE_NOTES,
               ring=dict(gc_matched_db=ring_gc, iip2_hif_worst_dbm=ring_iip2, relative_floor_dbc=ring_floor),
               jfet=dict(iip2_hif_worst_dbm=jf_iip2), rows=rows)
    json.dump(res, open(os.path.join(OUT, "result.json"), "w"), indent=1, default=str)
    md = ["# 2026-09-28-r06-cascade: result", "",
          f"Checker: cascade.py. MDS = {KTB:.1f} dBm + NF (500 Hz). REQ-SYS-022: MDS at most -140 dBm (TBR). REQ-SYS-033: image and half-IF responses at least 70 dB below the in-band response (TBR).", "",
          "| configuration | BPF worst loss per section, nominal Q 120 (dB) | same, MC mode B p95 (dB) | NF nominal / filter corner / stack (dB) | MDS nominal / filter corner / stack (dBm) | REQ-SYS-022 (nominal and filter corner) | gain to mixer (dB) | image rej: Q 100 / Q 120 / MC B min / MC A min (dB) | REQ-SYS-033 image | half-IF equivalent at antenna, nominal / corner (dBm) | REQ-SYS-033 half-IF | isolation needed, antenna to mixer at the image (dB) |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        h = r["halfif"]
        hv = lambda t: "no result" if h[t]["p_eq_antenna_dbm"] is None else f"{h[t]['p_eq_antenna_dbm']:.0f}"
        hp = "open (no valid JFET run)" if h["corner"]["pass_"] is None else ("PASS" if h["corner"]["pass_"] and h["nominal"]["pass_"] else "FAIL")
        md.append(f"| {r['cfg']['label']} | {', '.join(f'{x:.2f}' for x in r['bpf_loss_nominal_q120'])} | {', '.join(f'{x:.2f}' for x in r['bpf_loss_corner_mcB_p95'])} | {r['nominal']['nf_db']:.2f} / {r['filter_corner']['nf_db']:.2f} / {r['corner']['nf_db']:.2f} | {r['nominal']['mds_dbm']:.1f} / {r['filter_corner']['mds_dbm']:.1f} / {r['corner']['mds_dbm']:.1f} | {'PASS' if r['mds_pass_nominal'] and r['mds_pass_filter_corner'] else ('PASS nominal, FAIL filter corner' if r['mds_pass_nominal'] else 'FAIL')} | {r['nominal']['g_fe_db']:.1f} | {r['image']['q100_nominal']:.1f} / {r['image']['q120_nominal']:.1f} / {r['image']['mc_modeB_min']:.1f} / {r['image']['mc_modeA_min']:.1f} | {'PASS' if r['image']['pass_70'] else 'FAIL'} | {hv('nominal')} / {hv('corner')} | {hp} | {r['isolation_needed_db']:.0f} |")
    md += ["", f"Ring: matched conversion gain {ring_gc:.2f} dB (LTspice, IF port into 50 ohm); worst half-IF IIP2 over the mismatched sets {ring_iip2:.1f} dBm; relative time-step floor {ring_floor:.1f} dBc.",
           f"JFET mixer: worst valid half-IF IIP2 {('%.1f dBm' % jf_iip2) if jf_iip2 is not None else 'none (see r05)'}.", "",
           "Stage values (estimates unless marked sim):", ""]
    md += [f"- {k}: {v}" for k, v in STAGE_NOTES.items()]
    md += ["", "Stage tables (nominal):", ""]
    for r in rows:
        md.append(f"**{r['cfg']['label']}**: " + "; ".join(f"{n} NF {nf:.2f} G {g:+.2f}" for n, nf, g in r["nominal"]["stages"]) + (f"; image-noise term {r['nominal']['image_noise_db']:.2f} dB" if r['nominal']['image_noise_db'] else ""))
        md.append("")
    md += ["![cascade_nf_gain.png](cascade_nf_gain.png)", "", "![cascade_verdicts.png](cascade_verdicts.png)", ""]
    open(os.path.join(OUT, "result.md"), "w").write("\n".join(md))
    sd = os.path.join(OUT, "scripts"); os.makedirs(sd, exist_ok=True)
    for s in ("cascade.py", "bpf_design.py", "check_bpf.py", "check_halfif.py"):
        shutil.copy2(os.path.join(HERE, s), sd)
    print("\n".join(md))


if __name__ == "__main__":
    main()
