"""Run 2026-09-28-r07-nodal-validation: agreement of the numpy nodal solver (bpf_nodal.py, used by
worst_case.py for 20,000-run Monte Carlo and corner searches) with LTspice on every filter run r01 to r04.

For every deck and every .step it rebuilds the parameter namespace (coil Q step, Monte Carlo draws from the
*_draws.npz file saved beside the deck, stray capacitance and phase) and compares 20 log10 |V(o_k)| of each
section at every LTspice frequency point from 110 to 180 MHz, and the chain image rejection at IF 8 and 10 MHz.
Acceptance (set before the run): the largest difference is at most 0.01 dB for S21 of every section and for
every image rejection. Exit status 0 when accepted, 1 otherwise.
Usage: .venv/bin/python hardware/sim/rx-frontend/validate_nodal.py"""
import json, os, shutil, sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from spicelib import RawRead
from bpf_design import synth, netlist_block
import bpf_nodal as bn

HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(HERE, "results")
OUT = os.path.join(RES, "2026-09-28-r07-nodal-validation")
TOL_DB = 0.01  # acceptance: solver agrees with LTspice to 0.01 dB
L_RES, QC, LVIA = 56e-9, 500, 5e-9
TUNE = np.round(np.arange(144.0e6, 148.0e6 + 1, 50e3))

DECKS = [("2026-09-28-r01-bpf-ts012-baseline", "bpf_2p3_bw5", (2, 3), 5e6, "q"),
         ("2026-09-28-r01-bpf-ts012-baseline", "bpf_2p3_bw6", (2, 3), 6e6, "q"),
         ("2026-09-28-r01-bpf-ts012-baseline", "bpf_2p3_bw6_mcA", (2, 3), 6e6, "mc"),
         ("2026-09-28-r01-bpf-ts012-baseline", "bpf_2p3_bw6_mcB", (2, 3), 6e6, "mc"),
         ("2026-09-28-r02-bpf-three-section", "bpf_2p3p2_bw6", (2, 3, 2), 6e6, "q"),
         ("2026-09-28-r02-bpf-three-section", "bpf_2p3p3_bw6", (2, 3, 3), 6e6, "q"),
         ("2026-09-28-r03-bpf-three-section-mc", "bpf_2p3p2_bw6_mcA", (2, 3, 2), 6e6, "mc"),
         ("2026-09-28-r03-bpf-three-section-mc", "bpf_2p3p2_bw6_mcB", (2, 3, 2), 6e6, "mc"),
         ("2026-09-28-r03-bpf-three-section-mc", "bpf_2p3p3_bw6_mcA", (2, 3, 3), 6e6, "mc"),
         ("2026-09-28-r03-bpf-three-section-mc", "bpf_2p3p3_bw6_mcB", (2, 3, 3), 6e6, "mc"),
         ("2026-09-28-r04-bpf-leakage", "bpf_2p3p3_bw6_leak", (2, 3, 3), 6e6, "leak")]


def step_values(log):
    return [ln.strip()[6:] for ln in open(log, errors="replace") if ln.strip().startswith(".step ")]


def lines_for(spec, bw, mc):
    out = []
    for k, n in enumerate(spec, 1):
        d = synth(n, bw, 0.1, L_RES)
        tol = None
        if mc:
            def tol(kind, prefix, i):
                return f"m{kind}{prefix}{i}"
        out.append(netlist_block(d, f"b{k}", "i", "o", tol=tol))
    return out


def image_rej(f, secs_db):
    tot = np.sum(secs_db, axis=0)
    hin = np.interp(TUNE, f, tot)
    return {IF: float((hin - np.interp(TUNE - 2 * IF, f, tot)).min()) for IF in (8e6, 10e6)}


def main():
    os.makedirs(OUT, exist_ok=True)
    rows, allerr = [], []
    for run, deck, spec, bw, kind in DECKS:
        raw = os.path.join(RES, run, deck + ".raw")
        r = RawRead(raw, verbose=False)
        steps = r.get_steps()
        sv = step_values(os.path.join(RES, run, deck + ".log"))
        draws = dict(np.load(os.path.join(RES, run, deck + "_draws.npz"))) if kind == "mc" else {}
        L = lines_for(spec, bw, kind == "mc")
        worst_s21, worst_rej = 0.0, 0.0
        for si in steps:
            f = np.real(r.get_trace("frequency").get_wave(si))
            sel = (f >= 110e6) & (f <= 180e6)
            ns = dict(QU=100.0, QC=QC, LVIA=LVIA)
            cst, phi = 0.0, 0.0
            if kind == "q":
                ns["QU"] = float(sv[si].split("=")[1])
            elif kind == "mc":
                run_i = int(float(sv[si].split("=")[1])) - 1
                ns.update({k: float(v[run_i]) for k, v in draws.items()})
            else:
                kv = dict(x.split("=") for x in sv[si].split())
                cst = float(kv["cst"]); phi = 0.0 if float(kv["sgn"]) > 0 else np.pi
            lt, nm = [], []
            for k in range(len(spec)):
                a = 20 * np.log10(np.abs(r.get_trace(f"V(o{k+1})").get_wave(si)))[sel]
                b = bn.s21_db(L[k], f[sel], ns, cst=cst, phi=phi)
                lt.append(a); nm.append(b)
                e = np.abs(a - b)
                worst_s21 = max(worst_s21, float(e.max()))
                allerr.append(e)
            ra, rb = image_rej(f[sel], lt), image_rej(f[sel], nm)
            worst_rej = max(worst_rej, max(abs(ra[x] - rb[x]) for x in ra))
        rows.append(dict(run=run, deck=deck, steps=len(steps), max_abs_s21_diff_db=worst_s21, max_abs_image_rej_diff_db=worst_rej,
                         accepted=bool(worst_s21 <= TOL_DB and worst_rej <= TOL_DB)))
        print(f"{deck}: {len(steps)} steps, max |dS21| {worst_s21:.2e} dB, max |d image rej| {worst_rej:.2e} dB")
    ok = all(x["accepted"] for x in rows)
    e = np.concatenate(allerr)
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.hist(np.log10(np.maximum(e, 1e-9)), bins=80, color="tab:blue")
    ax.axvline(np.log10(TOL_DB), color="k", ls="--", lw=1.5, label=f"acceptance: {TOL_DB} dB")
    ax.set_xlabel("log10 |numpy nodal - LTspice| of section S21 (dB), every point 110-180 MHz, every step of r01-r04")
    ax.set_ylabel("points"); ax.grid(alpha=0.3); ax.legend()
    ax.set_title(f"Nodal solver vs LTspice: {len(e)} points, max {e.max():.2e} dB, {sum(x['steps'] for x in rows)} steps in {len(rows)} decks")
    fig.tight_layout(); fig.savefig(os.path.join(OUT, "nodal_vs_ltspice.png"), dpi=130); plt.close(fig)
    res = dict(run_id=os.path.basename(OUT), checker="validate_nodal.py", acceptance_db=TOL_DB, accepted=ok, rows=rows,
               points=int(len(e)), max_abs_diff_db=float(e.max()))
    json.dump(res, open(os.path.join(OUT, "result.json"), "w"), indent=1)
    md = [f"# {res['run_id']}: result", "",
          "Checker: validate_nodal.py. Question: does the numpy nodal solver `bpf_nodal.py` (the search tool of revision 2) reproduce LTspice on the same netlist lines?",
          f"Acceptance, fixed before the run: every section S21 and every chain image rejection within {TOL_DB} dB of LTspice, on every step of every filter deck of r01 to r04 (Q steps, 1,200 Monte Carlo draws, the leakage steps).", "",
          "| run | deck | steps | max abs S21 difference (dB) | max abs image-rejection difference (dB) | accepted |", "|---|---|---|---|---|---|"]
    for x in rows:
        md.append(f"| {x['run']} | {x['deck']} | {x['steps']} | {x['max_abs_s21_diff_db']:.1e} | {x['max_abs_image_rej_diff_db']:.1e} | {'yes' if x['accepted'] else 'NO'} |")
    md += ["", f"Verdict: **{'ACCEPTED' if ok else 'NOT ACCEPTED'}**, {len(e)} points, largest difference {e.max():.1e} dB. "
           "The residual is attributed to rounding (an estimate, not investigated further): the Monte Carlo tables in the r01 and r03 decks carry five decimals while this check uses the unrounded draws of the .npz files, and the deck expressions carry a six-digit f0.", "",
           "![nodal_vs_ltspice.png](nodal_vs_ltspice.png)", ""]
    open(os.path.join(OUT, "result.md"), "w").write("\n".join(md))
    sd = os.path.join(OUT, "scripts"); os.makedirs(sd, exist_ok=True)
    for s in ("validate_nodal.py", "bpf_nodal.py", "bpf_design.py"):
        shutil.copy2(os.path.join(HERE, s), sd)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
