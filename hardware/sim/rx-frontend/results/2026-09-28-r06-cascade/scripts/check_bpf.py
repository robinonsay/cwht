"""Checker for the rx-frontend band-pass filter runs (r01 to r04). Reads the LTspice .raw files with spicelib,
forms the front-end response as the product of the section S21s, and computes for every step:
  - passband loss of each section and of the chain, worst over 144.000 to 148.000 MHz;
  - image rejection for IF 8 MHz (TS-012 plan, low-side LO: image = f - 16 MHz) and, for the IF-change option,
    IF 10 MHz (image = f - 20 MHz), defined as REQ-SYS-033 and TC-SYS-021 define it: the response at the image
    frequency relative to the in-band response at the tuned frequency, worst over tuned frequencies 144.000 to
    148.000 MHz in 50 kHz steps;
  - the filter attenuation at the half-IF frequency (f - IF/2) relative to the tuned frequency (reported only:
    the half-IF response is a mixer product, closed in check_halfif.py and cascade.py);
  - IF feed-through rejection at 8 and 10 MHz (log-sweep decks only).
Pass/fail: REQ-SYS-033 >= 70 dB (as written, TBR). Also reported: >= 80 dB (10 dB leakage allowance proposed
here) and >= 90 dB (TS-012 revision 4 section 7.3 criterion). Writes result.json, result.md and PNG plots into
the run directory. Usage: check_bpf.py <run-dir>"""
import json, os, sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from spicelib import RawRead
plt.rcParams["axes.titlesize"] = 8.5

REQ = 70.0
ALLOW = 80.0
TS012 = 90.0
TUNE = np.round(np.arange(144.0e6, 148.0e6 + 1, 50e3), 0)
IFS = {"IF 8 MHz": 8e6, "IF 10 MHz": 10e6}


def load(raw):
    r = RawRead(raw, verbose=False)
    names = [t for t in r.get_trace_names() if t.lower().startswith("v(o")]
    names.sort()
    steps = r.get_steps()
    out = []
    for s in steps:
        f = np.real(r.get_trace("frequency").get_wave(s))
        secs = [np.abs(r.get_trace(n).get_wave(s)) for n in names]
        out.append((f, secs))
    stepinfo = r.steps if hasattr(r, "steps") else None
    return out, names, stepinfo


def interp_db(f, h_db, x):
    return np.interp(x, f, h_db)


def metrics(f, secs):
    sec_db = [20 * np.log10(np.maximum(s, 1e-300)) for s in secs]
    tot = np.sum(sec_db, axis=0)
    band = (f >= 144e6 - 1) & (f <= 148e6 + 1)
    m = {"section_loss_worst_db": [float(-interp_db(f, s, TUNE).min()) for s in sec_db],
         "section_loss_best_db": [float(-interp_db(f, s, TUNE).max()) for s in sec_db],
         "chain_loss_worst_db": float(-interp_db(f, tot, TUNE).min()),
         "chain_loss_best_db": float(-interp_db(f, tot, TUNE).max())}
    ref = [float(interp_db(f, sd, np.array([146e6]))[0]) for sd in sec_db]
    m["section_rejection_re_146_db"] = {f"{x:.0f} MHz": [float(r - interp_db(f, sd, np.array([x * 1e6]))[0]) for r, sd in zip(ref, sec_db)]
                                        for x in (124, 128, 130, 132)}
    hin = interp_db(f, tot, TUNE)
    for lab, IF in IFS.items():
        rej = hin - interp_db(f, tot, TUNE - 2 * IF)
        i = int(np.argmin(rej))
        hif = hin - interp_db(f, tot, TUNE - IF / 2)
        m[lab] = {"image_rejection_min_db": float(rej[i]), "at_tuned_mhz": float(TUNE[i] / 1e6),
                  "image_mhz": float((TUNE[i] - 2 * IF) / 1e6),
                  "halfif_filter_atten_min_db": float(hif.min()),
                  "halfif_filter_atten_max_db": float(hif.max()),
                  "pass_req_70": bool(rej[i] >= REQ), "meets_80": bool(rej[i] >= ALLOW), "meets_90": bool(rej[i] >= TS012)}
        if f.min() < IF:
            m[lab]["if_feedthrough_rejection_db"] = float(hin.min() - interp_db(f, tot, np.array([IF]))[0])
    return m, tot, sec_db


def shade(ax, ymin, ymax):
    ax.axvspan(144, 148, color="tab:green", alpha=0.12, label="2 m band 144-148 MHz")
    ax.axvspan(128, 132, color="tab:red", alpha=0.15, label="image band, IF 8 MHz (128-132)")
    ax.axvspan(124, 128, color="tab:purple", alpha=0.10, label="image band, IF 10 MHz (124-128)")
    ax.axvspan(140, 144, color="tab:orange", alpha=0.10, label="half-IF band, IF 8 MHz (140-144)")


def plot_q_design(run_dir, tag, title, res, raws, stepvals):
    f0, _ = raws[0]
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(13, 5.2))
    for (f, secs), q in zip(raws, stepvals):
        tot = np.sum([20 * np.log10(s) for s in secs], axis=0)
        sel = (f > 110e6) & (f < 170e6)
        a1.plot(f[sel] / 1e6, tot[sel], label=f"coil Q {q}")
    shade(a1, -150, 5)
    # REQ-SYS-033 line: 70 dB below the worst in-band response of the Q 100 step
    hin_min = -res[0]["metrics"]["chain_loss_worst_db"]
    a1.axhline(hin_min - REQ, color="k", ls="--", lw=1.2, label="REQ-SYS-033: 70 dB below in-band (Q 100)")
    a1.axhline(hin_min - TS012, color="k", ls=":", lw=1.0, label="TS-012 rev 4 criterion: 90 dB below")
    a1.set_xlim(110, 170); a1.set_ylim(-160, 5)
    a1.set_xlabel("frequency (MHz)"); a1.set_ylabel("front-end S21, product of sections (dB)")
    a1.set_title(f"{title}: S21"); a1.grid(alpha=0.3); a1.legend(fontsize=7, loc="lower right")
    for (f, secs), q in zip(raws, stepvals):
        tot = np.sum([20 * np.log10(s) for s in secs], axis=0)
        hin = np.interp(TUNE, f, tot)
        for lab, IF, ls in (("IF 8", 8e6, "-"), ("IF 10", 10e6, "--")):
            rej = hin - np.interp(TUNE - 2 * IF, f, tot)
            a2.plot(TUNE / 1e6, rej, ls, label=f"{lab} MHz, Q {q}")
    a2.axhline(REQ, color="k", ls="--", lw=1.5, label="REQ-SYS-033 70 dB")
    a2.axhline(ALLOW, color="grey", ls="-.", lw=1.0, label="80 dB (10 dB leakage allowance)")
    a2.axhline(TS012, color="k", ls=":", lw=1.0, label="TS-012 90 dB criterion")
    a2.set_xlabel("tuned frequency (MHz)"); a2.set_ylabel("image rejection relative to in-band (dB)")
    a2.set_title(f"{title}: image rejection vs tuned frequency"); a2.grid(alpha=0.3); a2.legend(fontsize=7, ncol=2, loc="best")
    fig.tight_layout()
    p1 = os.path.join(run_dir, f"{tag}_s21_image.png"); fig.savefig(p1, dpi=130); plt.close(fig)
    # passband zoom
    fig, ax = plt.subplots(figsize=(8, 5))
    for (f, secs), q in zip(raws, stepvals):
        sel = (f > 140e6) & (f < 152e6)
        tot = np.sum([20 * np.log10(s) for s in secs], axis=0)
        l, = ax.plot(f[sel] / 1e6, tot[sel], lw=2, label=f"chain, Q {q}")
        for k, s in enumerate(secs):
            ax.plot(f[sel] / 1e6, 20 * np.log10(s[sel]), lw=0.8, ls=":", color=l.get_color())
    ax.axvspan(144, 148, color="tab:green", alpha=0.12, label="2 m band")
    ax.axhline(-3, color="k", ls="--", lw=1, label="TS-012 3 dB passband-loss criterion")
    ax.set_ylim(-20, 1); ax.set_xlabel("frequency (MHz)"); ax.set_ylabel("S21 (dB)")
    ax.set_title(f"{title}: passband loss (solid chain, dotted sections)"); ax.grid(alpha=0.3); ax.legend(fontsize=7)
    fig.tight_layout()
    p2 = os.path.join(run_dir, f"{tag}_passband.png"); fig.savefig(p2, dpi=130); plt.close(fig)
    return [p1, p2]


def step_values(raw_path, n):
    """Read the .step values from the LTspice log next to the raw."""
    log = raw_path[:-4] + ".log"
    vals = []
    for line in open(log, errors="replace"):
        line = line.strip()
        if line.startswith(".step "):
            vals.append(line[6:])
    return vals[:n] if vals else [str(i) for i in range(n)]


def do_q(run_dir, deck, title):
    raw = os.path.join(run_dir, deck + ".raw")
    data, names, _ = load(raw)
    sv = step_values(raw, len(data))
    qv = [s.split("=")[1] for s in sv]
    res = []
    for (f, secs), s in zip(data, sv):
        m, _, _ = metrics(f, secs)
        res.append({"step": s, "metrics": m})
    plots = plot_q_design(run_dir, deck, title, res, data, qv)
    return {"deck": deck, "title": title, "steps": res, "plots": [os.path.basename(p) for p in plots]}


def do_mc(run_dir, deck, title):
    raw = os.path.join(run_dir, deck + ".raw")
    data, names, _ = load(raw)
    rows = []
    for f, secs in data:
        m, tot, _ = metrics(f, secs)
        rows.append(m)
    r8 = np.array([m["IF 8 MHz"]["image_rejection_min_db"] for m in rows])
    r10 = np.array([m["IF 10 MHz"]["image_rejection_min_db"] for m in rows])
    loss = np.array([m["chain_loss_worst_db"] for m in rows])
    l1 = np.array([m["section_loss_worst_db"][0] for m in rows])
    summ = {"n": len(rows),
            "IF 8 MHz": {"image_rejection_min_db": float(r8.min()), "p5_db": float(np.percentile(r8, 5)), "median_db": float(np.median(r8)),
                         "fraction_ge_70": float((r8 >= REQ).mean()), "fraction_ge_80": float((r8 >= ALLOW).mean()), "fraction_ge_90": float((r8 >= TS012).mean())},
            "IF 10 MHz": {"image_rejection_min_db": float(r10.min()), "p5_db": float(np.percentile(r10, 5)), "median_db": float(np.median(r10)),
                          "fraction_ge_70": float((r10 >= REQ).mean()), "fraction_ge_80": float((r10 >= ALLOW).mean()), "fraction_ge_90": float((r10 >= TS012).mean())},
            "chain_loss_worst_db": {"max": float(loss.max()), "p95": float(np.percentile(loss, 95)), "median": float(np.median(loss))},
            "bpf1_loss_worst_db": {"max": float(l1.max()), "p95": float(np.percentile(l1, 95)), "median": float(np.median(l1))},
            "section_loss_worst_db_max": [float(max(m["section_loss_worst_db"][k] for m in rows)) for k in range(len(rows[0]["section_loss_worst_db"]))],
            "section_loss_worst_db_p95": [float(np.percentile([m["section_loss_worst_db"][k] for m in rows], 95)) for k in range(len(rows[0]["section_loss_worst_db"]))],
            "section_loss_worst_db_median": [float(np.median([m["section_loss_worst_db"][k] for m in rows])) for k in range(len(rows[0]["section_loss_worst_db"]))],
            "halfif_filter_atten_min_db_IF8": float(min(m["IF 8 MHz"]["halfif_filter_atten_min_db"] for m in rows)),
            "halfif_filter_atten_min_db_IF10": float(min(m["IF 10 MHz"]["halfif_filter_atten_min_db"] for m in rows))}
    fig, axs = plt.subplots(1, 3, figsize=(16, 4.8))
    for f, secs in data:
        tot = np.sum([20 * np.log10(s) for s in secs], axis=0)
        axs[0].plot(f / 1e6, tot, lw=0.4, color="tab:blue", alpha=0.35)
    shade(axs[0], -160, 5)
    hmin = -loss.max()
    axs[0].axhline(hmin - REQ, color="k", ls="--", lw=1.2, label="REQ-SYS-033: 70 dB below worst in-band")
    axs[0].set_xlim(118, 154); axs[0].set_ylim(-160, 5); axs[0].grid(alpha=0.3)
    axs[0].set_xlabel("frequency (MHz)"); axs[0].set_ylabel("front-end S21 (dB)"); axs[0].set_title(f"{title}: {len(rows)} Monte Carlo S21")
    axs[0].legend(fontsize=6, loc="lower right")
    bins = np.linspace(min(r8.min(), r10.min()) - 2, max(r8.max(), r10.max()) + 2, 40)
    axs[1].hist(r8, bins=bins, alpha=0.7, label="IF 8 MHz (image 128-132)")
    axs[1].hist(r10, bins=bins, alpha=0.5, label="IF 10 MHz (image 124-128)")
    axs[1].axvline(REQ, color="k", ls="--", lw=1.5, label="REQ-SYS-033 70 dB")
    axs[1].axvline(ALLOW, color="grey", ls="-.", label="80 dB")
    axs[1].axvline(TS012, color="k", ls=":", label="TS-012 90 dB")
    axs[1].set_xlabel("worst image rejection over the band (dB)"); axs[1].set_ylabel("runs"); axs[1].legend(fontsize=7); axs[1].grid(alpha=0.3)
    axs[1].set_title("image rejection distribution")
    axs[2].hist(loss, bins=30, alpha=0.7, label="chain (all sections)")
    axs[2].hist(l1, bins=30, alpha=0.7, label="BPF1 (ahead of the first J310)")
    axs[2].axvline(3, color="k", ls="--", label="TS-012 3 dB criterion")
    axs[2].set_xlabel("worst passband loss 144-148 MHz (dB)"); axs[2].set_ylabel("runs"); axs[2].legend(fontsize=7); axs[2].grid(alpha=0.3)
    axs[2].set_title("passband loss distribution")
    fig.tight_layout()
    p = os.path.join(run_dir, f"{deck}_montecarlo.png"); fig.savefig(p, dpi=130); plt.close(fig)
    return {"deck": deck, "title": title, "summary": summ, "plots": [os.path.basename(p)]}


def do_leak(run_dir, deck, title):
    raw = os.path.join(run_dir, deck + ".raw")
    data, names, _ = load(raw)
    sv = step_values(raw, len(data))
    res = []
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(13, 5))
    for (f, secs), s in zip(data, sv):
        m, tot, _ = metrics(f, secs)
        res.append({"step": s, "metrics": m})
        kv = dict(x.split("=") for x in s.split())
        lab = f"stray C {float(kv['cst'])*1e12:.3g} pF, phase {'+' if float(kv['sgn']) > 0 else '-'}"
        a1.plot(f / 1e6, tot, label=lab)
        hin = np.interp(TUNE, f, tot)
        a2.plot(TUNE / 1e6, hin - np.interp(TUNE - 16e6, f, tot), label=lab + ", IF 8")
    shade(a1, -160, 5)
    a1.axhline(-res[0]["metrics"]["chain_loss_worst_db"] - REQ, color="k", ls="--", label="REQ-SYS-033 70 dB below in-band")
    a1.set_xlim(118, 154); a1.set_ylim(-170, 5); a1.grid(alpha=0.3); a1.legend(fontsize=7, loc="lower right")
    a1.set_xlabel("frequency (MHz)"); a1.set_ylabel("front-end S21 (dB)"); a1.set_title(f"{title}: S21 with stray feed-through C per section")
    a2.axhline(REQ, color="k", ls="--", lw=1.5, label="REQ-SYS-033 70 dB"); a2.axhline(TS012, color="k", ls=":", label="TS-012 90 dB")
    a2.set_xlabel("tuned frequency (MHz)"); a2.set_ylabel("image rejection (dB)"); a2.grid(alpha=0.3); a2.legend(fontsize=7)
    a2.set_title("image rejection vs stray capacitance (coil Q 100)")
    fig.tight_layout()
    p = os.path.join(run_dir, f"{deck}_leakage.png"); fig.savefig(p, dpi=130); plt.close(fig)
    return {"deck": deck, "title": title, "steps": res, "plots": [os.path.basename(p)]}


RUNS = {
    "2026-09-28-r01-bpf-ts012-baseline": [("q", "bpf_2p3_bw5", "TS-012 BPF1 2 + BPF2 3 resonators, 5 MHz design"),
                                          ("q", "bpf_2p3_bw6", "TS-012 BPF1 2 + BPF2 3 resonators, 6 MHz design"),
                                          ("mc", "bpf_2p3_bw6_mcA", "TS-012 2 + 3, 6 MHz, tolerance mode A (TS-012: 20 % caps)"),
                                          ("mc", "bpf_2p3_bw6_mcB", "TS-012 2 + 3, 6 MHz, tolerance mode B (proposed part spec)")],
    "2026-09-28-r02-bpf-three-section": [("q", "bpf_2p3p2_bw6", "2 + 3 + 2 resonators (BPF3 before the ring), 6 MHz"),
                                         ("q", "bpf_2p3p3_bw6", "2 + 3 + 3 resonators (BPF3 before the ring), 6 MHz")],
    "2026-09-28-r03-bpf-three-section-mc": [("mc", "bpf_2p3p2_bw6_mcA", "2 + 3 + 2, 6 MHz, tolerance mode A (TS-012: 20 % caps)"),
                                            ("mc", "bpf_2p3p2_bw6_mcB", "2 + 3 + 2, 6 MHz, tolerance mode B (proposed part spec)"),
                                            ("mc", "bpf_2p3p3_bw6_mcA", "2 + 3 + 3, 6 MHz, tolerance mode A (TS-012: 20 % caps)"),
                                            ("mc", "bpf_2p3p3_bw6_mcB", "2 + 3 + 3, 6 MHz, tolerance mode B (proposed part spec)")],
    "2026-09-28-r04-bpf-leakage": [("leak", "bpf_2p3p3_bw6_leak", "2 + 3 + 3, 6 MHz, Q 100")],
}


def ft(a):
    x = a.get("if_feedthrough_rejection_db")
    if x is None:
        return "not in sweep"
    return "> 150 (ideal model)" if x > 150 else f"{x:.0f}"


def md_table(out):
    L = [f"# {out['run_id']}: result", "", f"Checker: check_bpf.py. Pass criterion: REQ-SYS-033 image rejection >= {REQ:.0f} dB (TBR) at every tuned frequency 144.000 to 148.000 MHz. Also reported: >= 80 dB (10 dB leakage allowance proposed in the analysis record) and >= 90 dB (TS-012 revision 4 criterion).", ""]
    for item in out["items"]:
        L.append(f"## {item['deck']}: {item['title']}")
        L.append("")
        if "steps" in item:
            L.append("| step | BPF loss worst per section (dB) | chain loss worst (dB) | IF 8: image rej min (dB) at tuned MHz | IF 8 verdict (70 / 80 / 90) | IF 10: image rej min (dB) | IF 10 verdict (70 / 80 / 90) | half-IF filter atten, IF 8, min to max (dB) | IF feed-through rej, 8 MHz (dB) |")
            L.append("|---|---|---|---|---|---|---|---|---|")
            for s in item["steps"]:
                m = s["metrics"]; a = m["IF 8 MHz"]; b = m["IF 10 MHz"]
                v = lambda x: f"{'PASS' if x['pass_req_70'] else 'FAIL'} / {'yes' if x['meets_80'] else 'no'} / {'yes' if x['meets_90'] else 'no'}"
                L.append(f"| {s['step']} | {', '.join(f'{x:.2f}' for x in m['section_loss_worst_db'])} | {m['chain_loss_worst_db']:.2f} | {a['image_rejection_min_db']:.1f} at {a['at_tuned_mhz']:.2f} | {v(a)} | {b['image_rejection_min_db']:.1f} | {v(b)} | {a['halfif_filter_atten_min_db']:.1f} to {a['halfif_filter_atten_max_db']:.1f} | {ft(a)} |")
            L.append("")
            m0 = item["steps"][0]["metrics"]["section_rejection_re_146_db"]
            L.append(f"Per-section rejection relative to 146 MHz, step {item['steps'][0]['step']} (for the section-by-section NanoVNA check): " + "; ".join(f"{k}: {', '.join(f'{v:.1f}' for v in vals)} dB" for k, vals in m0.items()) + ".")
        else:
            s = item["summary"]
            L.append(f"N = {s['n']}.")
            L.append("")
            L.append("| quantity | IF 8 MHz | IF 10 MHz |")
            L.append("|---|---|---|")
            for k in ("image_rejection_min_db", "p5_db", "median_db", "fraction_ge_70", "fraction_ge_80", "fraction_ge_90"):
                L.append(f"| {k} | {s['IF 8 MHz'][k]:.3g} | {s['IF 10 MHz'][k]:.3g} |")
            L.append("")
            L.append(f"Chain worst passband loss: median {s['chain_loss_worst_db']['median']:.2f} dB, 95th percentile {s['chain_loss_worst_db']['p95']:.2f} dB, maximum {s['chain_loss_worst_db']['max']:.2f} dB. BPF1: median {s['bpf1_loss_worst_db']['median']:.2f}, 95th percentile {s['bpf1_loss_worst_db']['p95']:.2f}, maximum {s['bpf1_loss_worst_db']['max']:.2f} dB. Per-section worst in-band loss, median / 95th percentile / maximum: {'; '.join(f'{a:.2f} / {b:.2f} / {c:.2f}' for a, b, c in zip(s['section_loss_worst_db_median'], s['section_loss_worst_db_p95'], s['section_loss_worst_db_max']))} dB.")
            L.append("")
            L.append(f"Verdict (REQ-SYS-033, every run >= 70 dB at IF 8 MHz): {'PASS' if s['IF 8 MHz']['fraction_ge_70'] == 1.0 else 'FAIL'}; at IF 10 MHz: {'PASS' if s['IF 10 MHz']['fraction_ge_70'] == 1.0 else 'FAIL'}.")
        L.append("")
        for p in item["plots"]:
            L.append(f"![{p}]({p})")
        L.append("")
    return "\n".join(L)


if __name__ == "__main__":
    run_dir = os.path.abspath(sys.argv[1])
    rid = os.path.basename(run_dir)
    items = []
    for kind, deck, title in RUNS[rid]:
        items.append({"q": do_q, "mc": do_mc, "leak": do_leak}[kind](run_dir, deck, title))
    out = {"run_id": rid, "checker": "check_bpf.py", "requirement": "REQ-SYS-033 >= 70 dB image rejection (TBR)", "items": items}
    json.dump(out, open(os.path.join(run_dir, "result.json"), "w"), indent=1)
    open(os.path.join(run_dir, "result.md"), "w").write(md_table(out))
    print(md_table(out))
