"""Receiver noise and gain cascade (REQ-SYS-022 MDS, TPM-005) and the half-IF referral (REQ-SYS-033) for the
TS-012 finalists. Revision 2 (review findings 2, 3 and 4 on docs/design/analysis/rx-bpf-ts012.md):
  - band-pass losses from the numpy nodal solver on the deck netlists (bpf_nodal.py, agreement with LTspice
    within 0.002 dB on every r01 to r04 step, run r07): nominal at coil Q 120; the TC-SYS-017 filter corner is the
    worst in-band loss over the vertices of the mode B tolerance box (aligned at 50 ohm, coil Q 100) with every
    internal port anywhere within VSWR 1.2 of 50 ohm (the design input of run r09);
  - a J310 port case (finding 2): BPF1 loaded by the MMBFJ310 grounded-gate input at 1/gfs(min) = 125 ohm;
  - the MDS is compared with REQ-SYS-022 and with the TPM-005 PDR margin policy and thresholds of
    docs/plan/tpm.json (finding 3);
  - the image column takes the r08 to r10 worst-case corners;
  - exit status 1 when REQ-SYS-022 fails at the TC-SYS-017 corner for any configuration named proposed,
    0 otherwise (finding 4).
Writes results/2026-09-28-r11-cascade-tpm005/ (result.json, result.md, PNG plots). The r06 run keeps its own
copy of the revision 1 script. Usage: .venv/bin/python hardware/sim/rx-frontend/cascade.py

Every device value that is not an LTspice result is an estimate with its basis given in STAGE_NOTES; the
LTspice-derived numbers are marked "sim". MDS = -174 dBm/Hz + 10 log10(500 Hz) + NF = -147 dBm + NF
(REQ-SYS-022 verification note; docs/research/2m-cw-transceiver-reference-designs.md F14)."""
import json, math, os, shutil, sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import tolerance as T
from tolerance import Port, P50

HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(HERE, "results")
OUT = os.path.join(RES, "2026-09-28-r11-cascade-tpm005")
REQ_MDS = -140.0         # REQ-SYS-022: MDS at most -140 dBm (TBR) in 500 Hz
GOAL_MDS = -142.0        # REQ-SYS-023: -142 dBm (Goal)
TPM005_PDR = -142.0      # TPM-005 rx-mds margin_policy PDR: cascade gives <= -142 dBm (docs/plan/tpm.json)
TPM005_RED = -137.0      # TPM-005 threshold_red: more than 3 dB worse than -140 dBm; yellow between the two
REQ_IMG = 70.0           # REQ-SYS-033: image and IF responses at least 70 dB (TBR) below in-band
KTB = -174.0 + 10 * math.log10(500.0)

STAGE_NOTES = {
    "relay": "G5V-2 pole, 1N5711 clamp pair and input trace: 0.3 dB nominal, 0.5 dB corner (estimate, Low: signal relay not rated at VHF)",
    "j310": "MMBFJ310 grounded gate: gain 12 dB nominal / 10 dB corner, NF 2.5 / 3.0 dB (estimate from onsemi MMBFJ310 datasheet Gpg 16 dB typ at 100 MHz and NF 3.0 dB typ at 450 MHz, both at VDS 10 V, ID 10 mA; derated for the 5 V rail and tuned-drain loss)",
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


VSWR_DI = 1.2
J310_IN_MIN_GFS = Port(125.0, 0.0, "J310 input 1/gfs(min) = 125 ohm")
TUNE = T.tune_grid(100e3)


def ports_on_circle(S, n=8):
    w0 = 2 * math.pi * T.Section(2, 1).d["f0"]
    g = (S - 1) / (S + 1); out = []
    for ph in np.linspace(0, 2 * np.pi, n, endpoint=False):
        G = g * np.exp(1j * ph); Y = 1 / (50 * (1 + G) / (1 - G))
        out.append(Port(float(1 / Y.real), float(Y.imag / w0)))
    return out


def section_losses(spec):
    """Worst in-band transducer loss per section (dB) for the four cascade cases."""
    nom, j310, cor = [], [], []
    circ = ports_on_circle(VSWR_DI)
    for k, n in enumerate(spec, 1):
        s0 = T.Section(n, k, "0")
        nom.append(float(-s0.resp_db(TUNE, {}, align="at50", qu=120.0).min()))
        pout = J310_IN_MIN_GFS if k == 1 else P50
        j310.append(float(-s0.resp_db(TUNE, {}, align="at50", pout=pout, qu=120.0).min()))
        sb = T.Section(n, k, "B")
        V, mult = sb.vertices()
        worst = 0.0
        for pin in ([P50] if k == 1 else circ):
            for po in circ:
                h = sb.resp_db(TUNE, mult, align="at50", pin=pin, pout=po, qu=100.0)
                worst = max(worst, float((-h.min(axis=-1)).max()))
        cor.append(worst)
    return nom, j310, cor


def tpm005(mds):
    if mds <= TPM005_PDR:
        return "Green"
    return "Yellow" if mds <= TPM005_RED else "Red"


def image_corners(key):
    """Worst image rejection (dB) from runs r08 (tolerance corner, 50 ohm), r09 (ports VSWR 1.2) and r10
    (ports VSWR 1.2 and 0.03 pF stray per section, worst-phase bound)."""
    out = {}
    try:
        r8 = load("2026-09-28-r08-bpf-tolerance-corners", "result.json")["configs"][key]
        out["nominal_q100"] = r8["nominal_q100_ltspice"]
        out["corner_modeB"] = r8["cases"]["at50-B"]["corner_ltspice_db"]
        out["corner_modeA"] = r8["cases"]["at50-A"]["corner_ltspice_db"]
        out["mc20k_min_modeA_rev1"] = r8["cases"]["none-A"]["mc"]["min"]
    except (FileNotFoundError, KeyError):
        pass
    try:
        out["ports_vswr12"] = load("2026-09-28-r09-bpf-port-impedance", "result.json")["configs"][key]["vswr"][f"{VSWR_DI:g}"]["B-at50"]
    except (FileNotFoundError, KeyError):
        pass
    try:
        out["design_input"] = load("2026-09-28-r10-bpf-leakage-corner", "result.json")["configs"][key]["design_input_corner_db"]
    except (FileNotFoundError, KeyError):
        pass
    return out


CONFIGS = [
    dict(key="A5-ts012", label="A5 as TS-012 rev 4 (BPF 2+3, IF 8)", mixer="ring", if_mhz=8, spec=(2, 3), img="2p3_if8", finalist="A5", role="baseline"),
    dict(key="A5-R1", label="A5 + BPF3 (2+3+3, IF 8)", mixer="ring", if_mhz=8, spec=(2, 3, 3), img="2p3p3_if8", finalist="A5", role="proposed"),
    dict(key="A5-R3", label="A5 + BPF3 of 4 (2+3+4, IF 8)", mixer="ring", if_mhz=8, spec=(2, 3, 4), img="2p3p4_if8", finalist="A5", role="lever"),
    dict(key="A5-R2", label="A5, IF 10 MHz, 2+3+2 (alternative)", mixer="ring", if_mhz=10, spec=(2, 3, 2), img="2p3p2_if10", finalist="A5", role="alternative"),
    dict(key="A4-ts012", label="A4 as TS-012 rev 4 (BPF 2+3, JFET mixer)", mixer="jfet", if_mhz=8, spec=(2, 3), img="2p3_if8", finalist="A4", role="baseline"),
    dict(key="A4-R1", label="A4 + BPF3 (2+3+3, JFET mixer)", mixer="jfet", if_mhz=8, spec=(2, 3, 3), img="2p3p3_if8", finalist="A4", role="proposed"),
    dict(key="A4-R3", label="A4 + BPF3 of 4 (2+3+4, JFET mixer)", mixer="jfet", if_mhz=8, spec=(2, 3, 4), img="2p3p4_if8", finalist="A4", role="lever"),
]
CASES = [("nominal", "nominal: coil Q 120, nominal parts, 50 ohm ports"),
         ("j310", "J310 port: BPF1 into 125 ohm (1/gfs min), else nominal"),
         ("filter_corner", "TC-SYS-017 filter corner: Q 100, mode B vertices, ports VSWR 1.2"),
         ("stack", "stack: filter corner and every device at its corner")]


def main():
    os.makedirs(OUT, exist_ok=True)
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
    loss_cache = {}
    rows = []
    for cfg in CONFIGS:
        if cfg["spec"] not in loss_cache:
            loss_cache[cfg["spec"]] = section_losses(cfg["spec"])
        L_nom, L_j, L_cor = loss_cache[cfg["spec"]]
        r = {"nominal": build(cfg, False, L_nom, ring_gc), "j310": build(cfg, False, L_j, ring_gc),
             "filter_corner": build(cfg, False, L_cor, ring_gc), "stack": build(cfg, True, L_cor, ring_gc)}
        hif_att = 0.0  # worst tuning puts the half-IF in the passband (r01 to r04: 0.0 to 0.3 dB)
        hres = {}
        for tag, rr in (("nominal", r["nominal"]), ("corner", r["stack"])):
            pmix = -70.0 + rr["g_fe_db"] - hif_att
            if cfg["mixer"] == "ring":
                peq_mix = 2 * pmix - ring_iip2; floor_peq = pmix + ring_floor
            else:
                peq_mix = (2 * pmix - jf_iip2) if jf_iip2 is not None else None; floor_peq = None
            peq_ant = None if peq_mix is None else peq_mix - rr["g_fe_db"]
            hres[tag] = dict(p_mixer_dbm=pmix, p_eq_antenna_dbm=peq_ant,
                             floor_bound_antenna_dbm=None if floor_peq is None else floor_peq - rr["g_fe_db"],
                             pass_=None if peq_ant is None else bool(peq_ant <= -140.0))
        img = image_corners(cfg["img"])
        row = dict(cfg=cfg, losses=dict(nominal_q120=L_nom, j310_q120=L_j, corner_q100_modeB_vswr12=L_cor),
                   image=img, halfif=hres, isolation_needed_db=REQ_IMG + r["nominal"]["g_fe_db"])
        for tag, _ in CASES:
            row[tag] = r[tag]
            row[f"mds_{tag}"] = r[tag]["mds_dbm"]
            row[f"req022_{tag}"] = "PASS" if r[tag]["mds_dbm"] <= REQ_MDS else "FAIL"
            row[f"tpm005_{tag}"] = tpm005(r[tag]["mds_dbm"])
        rows.append(row)
    # ---- plots
    fig, axs = plt.subplots(2, 4, figsize=(21, 10))
    for ax, r in zip(axs.flat, rows):
        st = r["nominal"]["stages"]; names = [n for n, _, _ in st]; xx = np.arange(len(names))
        ax.plot(xx, r["nominal"]["running_nf"], "o-", color="tab:blue", label="cumulative NF, nominal")
        ax.plot(xx, r["filter_corner"]["running_nf"], "s--", color="tab:orange", ms=4, label="cumulative NF, TC-SYS-017 filter corner")
        ax.plot(xx, r["stack"]["running_nf"], "^:", color="tab:red", ms=4, label="cumulative NF, stack")
        ax.axhline(7.0, color="k", ls="--", lw=1, label="NF 7 dB = MDS -140 dBm (REQ-SYS-022)")
        ax.axhline(5.0, color="green", ls=":", lw=1, label="NF 5 dB = MDS -142 dBm (TPM-005 PDR margin)")
        ax.axhline(10.0, color="red", ls=":", lw=1, label="NF 10 dB = MDS -137 dBm (TPM-005 red)")
        ax.set_ylim(0, 19); ax.set_ylabel("NF at the antenna port (dB)")
        ax.set_xticks(xx); ax.set_xticklabels(names, rotation=60, ha="right", fontsize=7)
        ax.set_title(f"{r['cfg']['label']}\nMDS {r['mds_nominal']:.1f} / {r['mds_filter_corner']:.1f} / {r['mds_stack']:.1f} dBm (nominal / corner / stack)", fontsize=8)
        ax.grid(alpha=0.3)
        if r is rows[0]:
            ax.legend(fontsize=6, loc="upper left")
    for ax in list(axs.flat)[len(rows):]:
        ax.axis("off")
    fig.tight_layout(); p1 = os.path.join(OUT, "cascade_nf_gain.png"); fig.savefig(p1, dpi=110); plt.close(fig)

    fig, axs = plt.subplots(1, 2, figsize=(18, 6.2))
    ax = axs[0]
    x = np.arange(len(rows)); w = 0.2
    ax.axhspan(-150, TPM005_PDR, color="tab:green", alpha=0.10, label="TPM-005 Green (PDR margin policy: -142 dBm or better)")
    ax.axhspan(TPM005_PDR, TPM005_RED, color="gold", alpha=0.15, label="TPM-005 Yellow (-142 to -137 dBm)")
    ax.axhspan(TPM005_RED, -125, color="tab:red", alpha=0.10, label="TPM-005 Red (worse than -137 dBm)")
    for i, (tag, lab) in enumerate(CASES):
        ax.bar(x + (i - 1.5) * w, [r[f"mds_{tag}"] + 150 for r in rows], w, bottom=-150, label=lab)
    ax.axhline(REQ_MDS, color="k", ls="--", lw=1.5, label="REQ-SYS-022: -140 dBm")
    ax.set_ylim(-127, -145); ax.set_xticks(x); ax.set_xticklabels([r["cfg"]["key"] for r in rows], fontsize=8)
    ax.set_ylabel("MDS in 500 Hz (dBm); axis inverted, lower bar end = more sensitive")
    ax.set_title("r11: MDS against REQ-SYS-022 and the TPM-005 thresholds"); ax.legend(fontsize=6.5, loc="lower right"); ax.grid(alpha=0.3, axis="y")
    ax = axs[1]
    keys = [("nominal_q100", "nominal, Q 100 (r08)"), ("corner_modeA", "corner, mode A aligned (r08)"), ("corner_modeB", "corner, mode B aligned (r08)"),
            ("ports_vswr12", "corner, + ports VSWR 1.2 (r09)"), ("design_input", "corner, + ports + 0.03 pF stray (r10)")]
    for i, (k, lab) in enumerate(keys):
        ax.bar(x + (i - 2) * 0.16, [r["image"].get(k, np.nan) for r in rows], 0.16, label=lab)
    ax.axhline(REQ_IMG, color="k", ls="--", lw=1.5, label="REQ-SYS-033: 70 dB")
    ax.set_xticks(x); ax.set_xticklabels([r["cfg"]["key"] for r in rows], fontsize=8); ax.set_ylim(30, 115)
    ax.set_ylabel("worst image rejection (dB)"); ax.legend(fontsize=7, loc="upper left"); ax.grid(alpha=0.3, axis="y")
    ax.set_title("Image rejection, filters only (whole-chain board leak not included)")
    fig.tight_layout(); p2 = os.path.join(OUT, "cascade_verdicts.png"); fig.savefig(p2, dpi=130); plt.close(fig)

    res = dict(run_id=os.path.basename(OUT), checker="cascade.py", ktb_500hz_dbm=KTB, stage_notes=STAGE_NOTES,
               tpm005=dict(pdr_margin_policy_dbm=TPM005_PDR, red_above_dbm=TPM005_RED, source="docs/plan/tpm.json TPM-005 rx-mds"),
               ring=dict(gc_matched_db=ring_gc, iip2_hif_worst_dbm=ring_iip2, relative_floor_dbc=ring_floor),
               jfet=dict(iip2_hif_worst_dbm=jf_iip2), rows=rows)
    json.dump(res, open(os.path.join(OUT, "result.json"), "w"), indent=1, default=str)
    md = ["# 2026-09-28-r11-cascade-tpm005: result", "",
          f"Checker: cascade.py (revision 2). MDS = {KTB:.1f} dBm + NF (500 Hz). REQ-SYS-022: MDS at most -140 dBm (TBR); TC-SYS-017 acceptance: at most -140 dBm at every tolerance corner. "
          f"TPM-005 (rx-mds, docs/plan/tpm.json): PDR margin policy {TPM005_PDR:.0f} dBm or better (Green); Yellow from {TPM005_PDR:.0f} to {TPM005_RED:.0f} dBm; Red worse than {TPM005_RED:.0f} dBm.",
          "Filter losses: numpy nodal solver on the deck netlists (run r07: within 0.002 dB of LTspice). Every device value is an estimate (stage notes below).", "",
          "| configuration | BPF worst loss per section: nominal Q 120 / J310 port / TC-SYS-017 corner (dB) | NF nominal / J310 port / corner / stack (dB) | MDS nominal / J310 port / corner / stack (dBm) | REQ-SYS-022 nominal / J310 / corner / stack | TPM-005 nominal / J310 / corner / stack | gain to mixer (dB) | image: corner mode B / + ports / + stray (dB) | half-IF at antenna, nominal / stack (dBm) |",
          "|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        L = r["losses"]
        f3 = lambda xs: ", ".join(f"{x:.2f}" for x in xs)
        im = r["image"]; g = lambda k: f"{im[k]:.1f}" if k in im else "n/a"
        h = r["halfif"]; hv = lambda t: "no result" if h[t]["p_eq_antenna_dbm"] is None else f"{h[t]['p_eq_antenna_dbm']:.0f}"
        md.append(f"| {r['cfg']['label']} | {f3(L['nominal_q120'])} / {f3(L['j310_q120'])} / {f3(L['corner_q100_modeB_vswr12'])} | "
                  + " / ".join(f"{r[t]['nf_db']:.2f}" for t, _ in CASES) + " | " + " / ".join(f"{r['mds_' + t]:.1f}" for t, _ in CASES) + " | "
                  + " / ".join(r["req022_" + t] for t, _ in CASES) + " | " + " / ".join(r["tpm005_" + t] for t, _ in CASES)
                  + f" | {r['nominal']['g_fe_db']:.1f} | {g('corner_modeB')} / {g('ports_vswr12')} / {g('design_input')} | {hv('nominal')} / {hv('corner')} |")
    md += ["", f"Ring: matched conversion gain {ring_gc:.2f} dB (LTspice r05); worst half-IF IIP2 {ring_iip2:.1f} dBm. JFET mixer: worst valid half-IF IIP2 {('%.1f dBm' % jf_iip2) if jf_iip2 is not None else 'none'}.", "",
           "Stage values (estimates unless marked sim):", ""]
    md += [f"- {k}: {v}" for k, v in STAGE_NOTES.items()]
    md += ["", "Stage tables (nominal):", ""]
    for r in rows:
        md.append(f"**{r['cfg']['label']}**: " + "; ".join(f"{n} NF {nf:.2f} G {g:+.2f}" for n, nf, g in r["nominal"]["stages"]) + (f"; image-noise term {r['nominal']['image_noise_db']:.2f} dB" if r['nominal']['image_noise_db'] else ""))
        md.append("")
    bad = [r["cfg"]["key"] for r in rows if r["cfg"]["role"] == "proposed" and r["req022_filter_corner"] == "FAIL"]
    md += [f"Verdict REQ-SYS-022 at the TC-SYS-017 filter corner, proposed configurations: {'FAIL for ' + ', '.join(bad) if bad else 'PASS'}. "
           f"No configuration meets the TPM-005 PDR margin policy ({TPM005_PDR:.0f} dBm) in any case." if all(r[f'tpm005_{t}'] != 'Green' for r in rows for t, _ in CASES) else "Some cases meet the TPM-005 PDR margin policy.", "",
           f"Checker exit status: {1 if bad else 0}.", "",
           "![cascade_nf_gain.png](cascade_nf_gain.png)", "", "![cascade_verdicts.png](cascade_verdicts.png)", ""]
    open(os.path.join(OUT, "result.md"), "w").write("\n".join(md))
    sd = os.path.join(OUT, "scripts"); os.makedirs(sd, exist_ok=True)
    for s in ("cascade.py", "bpf_design.py", "bpf_nodal.py", "tolerance.py", "check_bpf.py", "check_halfif.py"):
        shutil.copy2(os.path.join(HERE, s), sd)
    print("\n".join(md))
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
