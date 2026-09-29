"""Revision 2 filter runs of the rx-frontend block (review findings 1, 2 and 5 on
docs/design/analysis/rx-bpf-ts012.md):

  r08-bpf-tolerance-corners  finding 1: 20,000-run Monte Carlo (numpy nodal solver, validated in r07) and the
                             worst-case corner of the tolerance box (TC-SYS-021 procedure step 4), for two
                             alignment models and tolerance modes A and B; LTspice re-simulation of every
                             corner and a 1,000-run LTspice Monte Carlo of the proposed filter.
  r09-bpf-port-impedance     finding 2: the sections between J310 port impedances instead of 50 ohm: the
                             datasheet-derived cases (J310 input 56 to 125 ohm, source-gate C, drain 50 to
                             200 ohm) and a VSWR design-input sweep; LTspice re-simulation of the cases.
  r10-bpf-leakage-corner     finding 5: per-section stray capacitance with a worst-phase bound, at nominal and
                             at the design-input corner; LTspice re-simulation at SGN +1 and -1.
  r12-bpf-residual-design-input  review iteration 2, finding 6 (revision 3 of the note): the alignment residual
                             sweep and the largest residual that holds REQ_SYS_033_DB, at the design-input corner
                             (mode B, aligned at 50 ohm, every internal port within VSWR 1.2, 0.03 pF per section,
                             worst-phase bound), with the 50 ohm and ports-only corners for reference; LTspice
                             re-simulation at the limit, at the +/-0.3 % estimate and at +/-0.75 %.

Usage (from the repo root):
  .venv/bin/python hardware/sim/rx-frontend/worst_case.py prepare r08|r09|r10|r12   (numpy work, writes decks)
  .venv/bin/python hardware/sim/rx-frontend/run_sims.py <run-id>                 (LTspice via the wrapper)
  .venv/bin/python hardware/sim/rx-frontend/worst_case.py check r08|r09|r10|r12     (reads the .raw, verdicts, plots)
Exit status of check: 0 when every configuration named as proposed passes its acceptance, 1 otherwise.

Acceptance for REQ-SYS-033 (TC-SYS-021) used here, fixed before these runs:
  (a) the worst-case corner over the stated tolerance box, at every tuned frequency 144.0 to 148.0 MHz at
      100 kHz spacing, is at least REQ_SYS_033_DB below the in-band response; nominal alone is not enough;
  (b) a Monte Carlo is reported as a build-yield estimate only. When a yield is claimed it needs zero runs
      below REQ_SYS_033_DB in N runs, giving an upper bound 1 - 0.05^(1/N) on the fraction of builds below it at
      95 % confidence (N = 2,996 for 0.1 %); with k > 0 failures the Clopper-Pearson 95 % interval is given.
"""
import json, math, os, shutil, sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from spicelib import RawRead
import tolerance as T
from tolerance import Port, P50
import make_decks as MD

REQ_SYS_033_DB = 70.0      # REQ-SYS-033: image and IF responses at least 70 dB (TBR) below the in-band response
TS012_DB = 90.0            # TS-012 revision 4 section 7.3 criterion (reported only)
MATCH_DB = 0.01            # LTspice re-simulation must agree with the numpy prediction to this (r07 basis)
N_MC = 20000               # numpy Monte Carlo runs (reproduces the reviewer's sample size)
N_MC_LT = 1000             # LTspice Monte Carlo runs (raw-file size bound)
SEED = 20260928 + 8        # r08 seed (numpy default_rng); the r03 seed was 20260928
HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(HERE, "results")
RUN = {"r08": "2026-09-28-r08-bpf-tolerance-corners", "r09": "2026-09-28-r09-bpf-port-impedance",
       "r10": "2026-09-28-r10-bpf-leakage-corner", "r12": "2026-09-28-r12-bpf-residual-design-input"}
TUNE = T.tune_grid(100e3)
W0 = 2 * math.pi * T.Section(2, 1).d["f0"]
plt.rcParams["axes.titlesize"] = 9

CONFIGS = [  # key, spec, IF, label, role
    ("2p3_if8", (2, 3), 8e6, "2 + 3, IF 8 MHz (TS-012 revision 4)", "baseline"),
    ("2p3p3_if8", (2, 3, 3), 8e6, "2 + 3 + 3, IF 8 MHz (revision 1 proposal)", "proposed"),
    ("2p3p4_if8", (2, 3, 4), 8e6, "2 + 3 + 4, IF 8 MHz (margin lever, new here)", "lever"),
    ("2p3p2_if10", (2, 3, 2), 10e6, "2 + 3 + 2, IF 10 MHz (alternative)", "alternative"),
]
CASES = [("none", "A"), ("none", "B"), ("at50", "A"), ("at50", "B")]
CASE_LABEL = {("none", "A"): "mode A, no re-alignment (rev 1 model)", ("none", "B"): "mode B, no re-alignment (rev 1 model)",
              ("at50", "A"): "mode A, aligned at 50 ohm", ("at50", "B"): "mode B, aligned at 50 ohm"}
VSWR_DI = 1.2              # proposed design input: every internal port within VSWR 1.2 of 50 ohm (r09)
CST_DI = 0.03e-12          # proposed design input: stray input-to-output capacitance per section (r10)
PHASES = np.linspace(0, 2 * np.pi, 16, endpoint=False)


def outdir(r):
    p = os.path.join(RES, RUN[r]); os.makedirs(p, exist_ok=True); return p


def ports_on_circle(S, n=8):
    if S <= 1.0:
        return [P50]
    g = (S - 1) / (S + 1)
    out = []
    for ph in np.linspace(0, 2 * np.pi, n, endpoint=False):
        G = g * np.exp(1j * ph); Y = 1 / (50 * (1 + G) / (1 - G))
        out.append(Port(float(1 / Y.real), float(Y.imag / W0), f"VSWR {S:g} at {math.degrees(ph):.0f} deg"))
    return out


def port_sets(spec, S):
    """Port candidates per section: the antenna port of BPF1 stays 50 ohm (the REQ-SYS-033 reference); every
    internal port (J310 inputs and drains, ring RF port) is anywhere on the VSWR-S circle."""
    c = ports_on_circle(S)
    return [([P50] if k == 0 else c, c) for k in range(len(spec))]


def fr_of(IF):
    return np.concatenate([TUNE, TUNE - 2 * IF])


def section_search(sec, IF, pins, pouts, align, cst=0.0, bound=False, qu=100.0, vertices=True):
    """Minimum over the tolerance vertices (or nominal only) and over the port candidates of the section
    rejection at every tuned frequency. With cst > 0 and bound=True the leak phase is taken worst separately
    at the tuned and at the image frequency (a bound). Returns rmin (len TUNE) and the argmin record per f."""
    if vertices:
        V, mult = sec.vertices()
    else:
        V, mult = np.zeros((1, len(sec.keys)), int), {}
    fr = fr_of(IF)
    nt = len(TUNE)
    best = np.full(nt, np.inf); arg = [None] * nt
    for a, pin in enumerate(pins):
        for b, pout in enumerate(pouts):
            if cst > 0:
                H = np.array([sec.resp_db(fr, mult, align=align, pin=pin, pout=pout, qu=qu, cst=cst, phi=p) for p in PHASES])
                H = H.reshape((len(PHASES), -1, len(fr)))
                ht, hi = H[..., :nt], H[..., nt:]
                if bound:
                    R = ht.min(axis=0) - hi.max(axis=0); ph_t = ht.argmin(axis=0); ph_i = hi.argmax(axis=0)
                else:
                    R = ht[0] - hi[0]; ph_t = ph_i = np.zeros_like(R, int)
            else:
                h = sec.resp_db(fr, mult, align=align, pin=pin, pout=pout, qu=qu).reshape((-1, len(fr)))
                R = h[:, :nt] - h[:, nt:]; ph_t = ph_i = np.zeros_like(R, int)
            iv = R.argmin(axis=0)
            for j in range(nt):
                if R[iv[j], j] < best[j]:
                    best[j] = R[iv[j], j]
                    arg[j] = dict(vertex=V[iv[j]].tolist(), pin=a, pout=b, ph_t=int(ph_t[iv[j], j]), ph_i=int(ph_i[iv[j], j]))
    return best, arg


def chain_corner(spec, IF, mode, align, S=1.0, cst=0.0, bound=False, res=T.RES):
    secs = T.chain_sections(spec, mode, res)
    ps = port_sets(spec, S)
    tot = np.zeros(len(TUNE)); per = []
    for sec, (pins, pouts) in zip(secs, ps):
        r, arg = section_search(sec, IF, pins, pouts, align, cst=cst, bound=bound, vertices=(mode != "0"))
        tot += r; per.append((sec, r, arg, pins, pouts))
    j = int(np.argmin(tot))
    return dict(value=float(tot[j]), at_mhz=float(TUNE[j] / 1e6), per_f=tot, j=j, sections=per)


def corner_case(cc, align, qu=100.0, cst=0.0, phase_mode="t"):
    """LTspice case dict (values_deck format) for the corner at the worst tuned frequency of chain_corner."""
    j = cc["j"]; case = {"QU": qu}
    for k0, (sec, r, arg, pins, pouts) in enumerate(cc["sections"]):
        k = k0 + 1; a = arg[j]
        pin, pout = pins[a["pin"]], pouts[a["pout"]]
        mult = T.corner_mult(sec, a["vertex"]) if sec.mode != "0" else {}
        ns = sec.ns_for(mult, align=align, pin=pin, pout=pout, qu=qu)
        for key in sec.keys:
            case[key] = float(ns[key])
        case.update({f"RS{k}": pin.r, f"CI{k}": pin.c, f"RL{k}": pout.r, f"CL{k}": pout.c})
        if cst > 0:
            ph = PHASES[a["ph_t"] if phase_mode == "t" else a["ph_i"]]
            sgn = 1.0 if math.cos(ph) >= 0 else -1.0  # LTspice can only take a real SGN: nearest of +1 and -1
            case.update({f"CST{k}": cst, f"SGN{k}": sgn})
    return case


def predict_case(spec, IF, case):
    """numpy prediction of the chain rejection (per tuned f) and section responses for an LTspice case."""
    fr = fr_of(IF); nt = len(TUNE); tot = 0; secs_db = []
    for k0, n in enumerate(spec):
        k = k0 + 1
        sec = T.Section(n, k, "0")
        ns = sec.base_ns(case.get("QU", 100.0))
        for key in sec.keys:
            ns[key] = case.get(key, 1.0)
        sgn = case.get(f"SGN{k}", 0.0)
        h = T.bn.s21_db(sec.lines, fr, ns, rs=case.get(f"RS{k}", 50.0), rl=case.get(f"RL{k}", 50.0),
                        cin=case.get(f"CI{k}", 0.0), cout=case.get(f"CL{k}", 0.0),
                        cst=case.get(f"CST{k}", 0.0) if sgn else 0.0, phi=0.0 if sgn >= 0 else math.pi)
        secs_db.append(h); tot = tot + h[:nt] - h[nt:]
    return tot, secs_db


def read_cases(run_dir, deck, spec, IF, cases):
    """LTspice transducer S21 per section and chain rejection per case (a 2 V source, so |S21|^2 = |V|^2 RS/RL)."""
    r = RawRead(os.path.join(run_dir, deck + ".raw"), verbose=False)
    out = []
    fr = fr_of(IF); nt = len(TUNE)
    for si, case in zip(r.get_steps(), cases):
        f = np.real(r.get_trace("frequency").get_wave(si))
        # LTspice sorts an .ac list in ascending order: map every requested frequency to its point
        idx = np.array([int(np.argmin(np.abs(f - x))) for x in fr])
        assert np.allclose(f[idx], fr, rtol=0, atol=1.0), "frequency list mismatch"
        secs_db = []
        for k in range(1, len(spec) + 1):
            v = np.abs(r.get_trace(f"V(o{k})").get_wave(si))[idx]
            secs_db.append(20 * np.log10(v) + 10 * np.log10(case.get(f"RS{k}", 50.0) / case.get(f"RL{k}", 50.0)))
        tot = np.sum([s[:nt] - s[nt:] for s in secs_db], axis=0)
        out.append((tot, secs_db))
    return out


def copy_scripts(d):
    sd = os.path.join(d, "scripts"); os.makedirs(sd, exist_ok=True)
    for s in ("worst_case.py", "tolerance.py", "bpf_nodal.py", "bpf_design.py", "make_decks.py", "run_sims.py", "validate_nodal.py"):
        shutil.copy2(os.path.join(HERE, s), sd)


# ------------------------------------------------------------------------------------------------ r08
def mc_numpy(spec, IF, mode, align, n, seed):
    rng = np.random.default_rng(seed)
    secs = T.chain_sections(spec, mode)
    draws = [s.draws(rng, n) for s in secs]
    rej = np.zeros((n, len(TUNE))); loss = np.zeros((n, len(spec)))
    fr = fr_of(IF); nt = len(TUNE)
    for c0 in range(0, n, 2000):
        sl = slice(c0, min(n, c0 + 2000))
        for k, (s, dr) in enumerate(zip(secs, draws)):
            h = s.resp_db(fr, {key: v[sl] for key, v in dr.items()}, align=align)
            rej[sl] += h[:, :nt] - h[:, nt:]
            loss[sl, k] = -h[:, :nt].min(axis=1)
    return rej.min(axis=1), loss, draws


def stats(x, n_fail):
    n = len(x)
    lo, hi = T.clopper_pearson(n_fail, n)
    return dict(n=n, min=float(x.min()), p01=float(np.percentile(x, 0.1)), p1=float(np.percentile(x, 1)),
                p5=float(np.percentile(x, 5)), median=float(np.median(x)), n_below_70=int(n_fail),
                frac_below_70=n_fail / n, cp95=[lo, hi], zero_fail_upper95=T.zero_fail_upper(n) if n_fail == 0 else None)


def prepare_r08():
    d = outdir("r08")
    out = {"run_id": RUN["r08"], "seed": SEED, "n_mc": N_MC, "tune_step_khz": 100, "configs": {}}
    decks = []
    for key, spec, IF, label, role in CONFIGS:
        cfg = {"label": label, "role": role, "spec": spec, "if_mhz": IF / 1e6, "cases": {}}
        # nominal at Q 100
        nom = chain_corner(spec, IF, "0", "at50")
        cfg["nominal_q100"] = nom["value"]
        lt_cases = [dict(QU=100.0)]; names = ["nominal Q 100"]
        for align, mode in CASES:
            cc = chain_corner(spec, IF, mode, align)
            x, loss, _ = mc_numpy(spec, IF, mode, align, N_MC, SEED)
            st = stats(x, int((x < REQ_SYS_033_DB).sum()))
            # polish check at the worst tuned frequency (interior minimum search)
            pol = 0.0
            for sec, r, arg, pins, pouts in cc["sections"]:
                w = T.worst_corner(sec, np.array([TUNE[cc["j"]]]), IF, polish_at=[TUNE[cc["j"]]], align=align, n_random=6)
                pol += list(w["polish"].values())[0]["r_db"]
            cfg["cases"][f"{align}-{mode}"] = dict(label=CASE_LABEL[(align, mode)], corner_db=cc["value"], corner_at_mhz=cc["at_mhz"],
                                                  corner_polished_db=pol, mc=st,
                                                  loss_p95=[float(np.percentile(loss[:, k], 95)) for k in range(len(spec))],
                                                  loss_max=[float(loss[:, k].max()) for k in range(len(spec))])
            np.save(os.path.join(d, f"mc20k_{key}_{align}_{mode}.npy"), x.astype(np.float32))
            lt_cases.append(corner_case(cc, align)); names.append(f"corner {CASE_LABEL[(align, mode)]}")
        # residual sensitivity (aligned, mode B)
        cfg["residual_sweep"] = {f"{r:g}": chain_corner(spec, IF, "B", "at50", res=r)["value"] for r in (0.001, 0.002, 0.003, 0.005, 0.0075, 0.01, 0.015)}
        # loss corner per section at Q 100, mode B aligned, 50 ohm (cascade input)
        cfg["loss_corner_q100_modeB_at50"] = [T.loss_corner(s, TUNE, align="at50")[0] for s in T.chain_sections(spec, "B")]
        pred = [predict_case(spec, IF, c)[0].min() for c in lt_cases]
        cfg["ltspice_cases"] = [dict(name=nm, predicted_db=float(p)) for nm, p in zip(names, pred)]
        deck = f"bpf_{key}_corners"
        MD.values_deck(deck + ".net", f"IF {IF/1e6:.0f} MHz, nominal and worst-case tolerance corners (r08)", spec, lt_cases, fr_of(IF))
        json.dump(lt_cases, open(os.path.join(MD.DECKS, deck + "_cases.json"), "w"), indent=1)
        decks.append(deck + ".net")
        out["configs"][key] = cfg
        print(key, "nominal", round(nom["value"], 2), {k: round(v["corner_db"], 2) for k, v in cfg["cases"].items()})
    # LTspice Monte Carlo of the proposed 2 + 3 + 3 filter (1,000 runs): rev 1 model mode A, aligned modes A, B
    spec, IF = (2, 3, 3), 8e6
    for align, mode in (("none", "A"), ("at50", "A"), ("at50", "B")):
        rng = np.random.default_rng(SEED + 100)
        secs = T.chain_sections(spec, mode)
        cases = [dict(QU=100.0) for _ in range(N_MC_LT)]
        for s in secs:
            dr = s.draws(rng, N_MC_LT)
            ns = s.ns_for(dr, align=align)
            for key in s.keys:
                for i in range(N_MC_LT):
                    cases[i][key] = float(ns[key][i])
        deck = f"bpf_2p3p3_if8_mc{N_MC_LT}_{align}_{mode}"
        MD.values_deck(deck + ".net", f"Monte Carlo N={N_MC_LT} seed {SEED + 100}, {CASE_LABEL[(align, mode)]} (r08)", spec, cases, fr_of(IF))
        json.dump(cases, open(os.path.join(MD.DECKS, deck + "_cases.json"), "w"))
        decks.append(deck + ".net")
    out["decks"] = decks
    json.dump(out, open(os.path.join(d, "prepare.json"), "w"), indent=1, default=float)
    print("decks:", decks)


def check_r08():
    d = outdir("r08")
    P = json.load(open(os.path.join(d, "prepare.json")))
    res = dict(P); res["checker"] = "worst_case.py check r08"; res["requirement"] = f"REQ-SYS-033 >= {REQ_SYS_033_DB:.0f} dB (TBR)"
    ok_all = True
    md = [f"# {RUN['r08']}: result", "",
          f"Checker: worst_case.py check r08. Requirement: REQ-SYS-033, image response at least {REQ_SYS_033_DB:.0f} dB (TBR) below the in-band response at every tuned frequency 144.0 to 148.0 MHz (100 kHz spacing, TC-SYS-021). "
          "Acceptance (fixed before the run): (a) the worst-case corner of the tolerance box passes; (b) a Monte Carlo is a yield estimate only (zero runs below 70 dB in N runs bounds the failing fraction at 1 - 0.05^(1/N) with 95 % confidence).",
          f"Coil Q 100, capacitor Q 500, 5 nH vias, residual tuning +/-0.3 % in frequency (estimate), 50 ohm ports. Numpy Monte Carlo N = {N_MC}, seed {SEED}; LTspice re-simulates every corner (agreement limit {MATCH_DB} dB) and runs a {N_MC_LT}-run Monte Carlo of 2 + 3 + 3.", ""]
    md += ["| configuration | nominal Q 100 (dB) | case | worst-case corner (dB) at tuned MHz | LTspice corner (dB) | MC 20k min / p0.1 / p1 / median (dB) | MC runs below 70 dB (95 % interval) | verdict (corner) |",
           "|---|---|---|---|---|---|---|---|"]
    for key, spec, IF, label, role in CONFIGS:
        cfg = P["configs"][key]
        deck = f"bpf_{key}_corners"
        cases = json.load(open(os.path.join(d, deck + "_cases.json")))
        lt = read_cases(d, deck, spec, IF, cases)
        ltmin = [float(t.min()) for t, _ in lt]
        for c, v in zip(cfg["ltspice_cases"], ltmin):
            c["ltspice_db"] = v; c["agree"] = bool(abs(v - c["predicted_db"]) <= MATCH_DB)
            ok_all &= c["agree"]
        cfg["nominal_q100_ltspice"] = ltmin[0]
        for i, (align, mode) in enumerate(CASES, 1):
            cs = cfg["cases"][f"{align}-{mode}"]
            cs["corner_ltspice_db"] = ltmin[i]
            cs["verdict"] = "PASS" if ltmin[i] >= REQ_SYS_033_DB else "FAIL"
            m = cs["mc"]
            iv = f"{m['n_below_70']} of {m['n']} = {100*m['frac_below_70']:.3g} % ({100*m['cp95'][0]:.4g} to {100*m['cp95'][1]:.4g} %)"
            md.append(f"| {label} | {ltmin[0]:.1f} | {cs['label']} | {cs['corner_db']:.2f} at {cs['corner_at_mhz']:.1f} | {ltmin[i]:.2f} | {m['min']:.1f} / {m['p01']:.1f} / {m['p1']:.1f} / {m['median']:.1f} | {iv} | **{cs['verdict']}** |")
        cfg["verdict_design_case"] = cfg["cases"]["at50-B"]["verdict"]
    md += ["", "Interior search: a bounded L-BFGS-B minimisation from the worst vertex and six random interior points at the worst tuned frequency found no point below the vertex (column `corner_polished_db` in result.json), so each corner is a vertex of the box.", ""]
    # residual sensitivity table
    md += ["Residual tuning after alignment (mode B, aligned at 50 ohm), worst-case corner (dB):", "",
           "| configuration | " + " | ".join(f"+/-{float(r)*100:g} %" for r in P["configs"]["2p3p3_if8"]["residual_sweep"]) + " |",
           "|---|" + "---|" * len(P["configs"]["2p3p3_if8"]["residual_sweep"])]
    for key, spec, IF, label, role in CONFIGS:
        md.append(f"| {label} | " + " | ".join(f"{v:.1f}" for v in P["configs"][key]["residual_sweep"].values()) + " |")
    # LTspice MC
    md += ["", f"LTspice Monte Carlo of 2 + 3 + 3 at IF 8 MHz, N = {N_MC_LT}, seed {SEED + 100}:", "",
           "| case | LTspice min / p1 / median (dB) | runs below 70 dB | 95 % bound or interval on the failing fraction | numpy 20k min / median, same case (dB) | max numpy-LTspice difference, same draws (dB) |", "|---|---|---|---|---|---|"]
    res["ltspice_mc"] = {}
    for align, mode in (("none", "A"), ("at50", "A"), ("at50", "B")):
        deck = f"bpf_2p3p3_if8_mc{N_MC_LT}_{align}_{mode}"
        cases = json.load(open(os.path.join(d, deck + "_cases.json")))
        lt = read_cases(d, deck, (2, 3, 3), 8e6, cases)
        x = np.array([t.min() for t, _ in lt])
        diff = max(abs(float(t.min()) - float(predict_case((2, 3, 3), 8e6, c)[0].min())) for (t, _), c in zip(lt[:200], cases[:200]))
        ok_all &= diff <= MATCH_DB
        kf = int((x < REQ_SYS_033_DB).sum())
        st = stats(x, kf)
        res["ltspice_mc"][f"{align}-{mode}"] = dict(stats=st, max_diff_first200_db=diff)
        np.save(os.path.join(d, f"mc{N_MC_LT}_ltspice_{align}_{mode}.npy"), x.astype(np.float32))
        b = (f"< {100*st['zero_fail_upper95']:.2g} % (zero failures)" if kf == 0 else f"{100*st['cp95'][0]:.2g} to {100*st['cp95'][1]:.2g} %")
        n20 = P["configs"]["2p3p3_if8"]["cases"][f"{align}-{mode}"]["mc"]
        md.append(f"| {CASE_LABEL[(align, mode)]} | {st['min']:.1f} / {st['p1']:.1f} / {st['median']:.1f} | {kf} | {b} | {n20['min']:.1f} / {n20['median']:.1f} | {diff:.1e} |")
    # plots
    plots = plot_r08(d, P, res)
    md += [""] + [f"![{p}]({p})" for p in plots] + [""]
    prop_ok = all(P["configs"][k]["cases"]["at50-B"]["verdict"] == "PASS" for k, s, i, l, role in CONFIGS if role == "proposed")
    md += [f"Verdict (proposed configuration 2 + 3 + 3, mode B, aligned at 50 ohm, 50 ohm ports): **{'PASS' if prop_ok else 'FAIL'}**; LTspice agreement with every numpy prediction: {'yes' if ok_all else 'NO'}.",
           "Mode A (TS-012 20 % capacitors) and the no-re-alignment model are reported, not proposed. Ports and leakage are added in r09 and r10.", ""]
    res["verdict_proposed"] = prop_ok; res["ltspice_agreement"] = ok_all
    json.dump(res, open(os.path.join(d, "result.json"), "w"), indent=1, default=float)
    open(os.path.join(d, "result.md"), "w").write("\n".join(md))
    copy_scripts(d)
    print("\n".join(md))
    return prop_ok and ok_all


def plot_r08(d, P, res):
    plots = []
    # 1. corner summary
    fig, ax = plt.subplots(figsize=(13, 5.6))
    x = np.arange(len(CONFIGS)); wdt = 0.13
    ax.bar(x - 2.5 * wdt, [P["configs"][k]["nominal_q100_ltspice"] if "nominal_q100_ltspice" in P["configs"][k] else P["configs"][k]["nominal_q100"] for k, *_ in CONFIGS], wdt, label="nominal, Q 100", color="0.6")
    cols = {("none", "A"): "tab:red", ("none", "B"): "tab:orange", ("at50", "A"): "tab:purple", ("at50", "B"): "tab:blue"}
    for i, (al, mo) in enumerate(CASES):
        v = [P["configs"][k]["cases"][f"{al}-{mo}"].get("corner_ltspice_db", P["configs"][k]["cases"][f"{al}-{mo}"]["corner_db"]) for k, *_ in CONFIGS]
        ax.bar(x + (i - 1.5) * wdt, v, wdt, label=f"worst-case corner, {CASE_LABEL[(al, mo)]} (LTspice)", color=cols[(al, mo)])
    ax.plot(x + 2.5 * wdt, [P["configs"][k]["cases"]["at50-B"]["mc"]["min"] for k, *_ in CONFIGS], "k^", ms=8, label="MC 20k minimum, mode B aligned")
    ax.plot(x + 2.5 * wdt, [P["configs"][k]["cases"]["none-A"]["mc"]["min"] for k, *_ in CONFIGS], "rv", ms=8, label="MC 20k minimum, mode A rev 1 model")
    ax.axhline(REQ_SYS_033_DB, color="k", ls="--", lw=1.5, label="REQ-SYS-033: 70 dB")
    ax.axhline(TS012_DB, color="k", ls=":", lw=1, label="TS-012 90 dB criterion")
    ax.set_xticks(x); ax.set_xticklabels([c[3] for c in CONFIGS], fontsize=8)
    ax.set_ylabel("worst image rejection over 144-148 MHz (dB)"); ax.set_ylim(20, 120); ax.grid(alpha=0.3, axis="y")
    ax.legend(fontsize=7, ncol=2, loc="upper left"); ax.set_title("r08: nominal, worst-case tolerance corners and Monte Carlo minima (coil Q 100, 50 ohm ports, no leakage)")
    fig.tight_layout(); p = "corners_summary.png"; fig.savefig(os.path.join(d, p), dpi=130); plt.close(fig); plots.append(p)
    # 2. MC distributions (numpy 20k) and the lower tail against LTspice 1000
    fig, axs = plt.subplots(1, 3, figsize=(20, 5.4))
    for ax, key in zip(axs[:2], ("2p3p3_if8", "2p3p2_if10")):
        for al, mo in CASES:
            xx = np.load(os.path.join(d, f"mc20k_{key}_{al}_{mo}.npy"))
            ax.hist(xx, bins=np.arange(40, 115, 0.5), histtype="step", lw=1.4, color=cols[(al, mo)], label=f"{CASE_LABEL[(al, mo)]}: min {xx.min():.1f}, corner {P['configs'][key]['cases'][al+'-'+mo]['corner_db']:.1f}")
            ax.axvline(P["configs"][key]["cases"][f"{al}-{mo}"]["corner_db"], color=cols[(al, mo)], ls=":", lw=1.2)
        ax.axvline(REQ_SYS_033_DB, color="k", ls="--", lw=1.5, label="REQ-SYS-033 70 dB")
        ax.set_yscale("log"); ax.set_ylim(0.8, 5000)
        ax.set_xlabel("worst image rejection over the band (dB); dotted: worst-case corner"); ax.set_ylabel(f"runs (of {N_MC})")
        ax.set_title(f"{dict((c[0], c[3]) for c in CONFIGS)[key]}: numpy Monte Carlo {N_MC} runs"); ax.grid(alpha=0.3); ax.legend(fontsize=6.5, loc="upper right")
    ax = axs[2]
    for al, mo in (("none", "A"), ("at50", "A"), ("at50", "B")):
        xx = np.sort(np.load(os.path.join(d, f"mc20k_2p3p3_if8_{al}_{mo}.npy")))
        xl = np.sort(np.load(os.path.join(d, f"mc{N_MC_LT}_ltspice_{al}_{mo}.npy")))
        ax.step(xx, np.arange(1, len(xx) + 1) / len(xx), where="post", color=cols[(al, mo)], label=f"numpy {N_MC}, {CASE_LABEL[(al, mo)]}")
        ax.step(xl, np.arange(1, len(xl) + 1) / len(xl), where="post", color=cols[(al, mo)], ls="--", label=f"LTspice {N_MC_LT}, same case (other seed)")
        ax.axvline(P["configs"]["2p3p3_if8"]["cases"][f"{al}-{mo}"]["corner_db"], color=cols[(al, mo)], ls=":", lw=1.2)
    ax.axvline(REQ_SYS_033_DB, color="k", ls="--", lw=1.5, label="REQ-SYS-033 70 dB")
    ax.axhline(0.001, color="grey", ls="-.", lw=1, label="0.1 % of builds")
    ax.set_yscale("log"); ax.set_ylim(3e-5, 1); ax.set_xlim(45, 90)
    ax.set_xlabel("worst image rejection (dB); dotted: worst-case corner"); ax.set_ylabel("fraction of builds at or below")
    ax.set_title("2 + 3 + 3, IF 8: lower tail, numpy vs LTspice"); ax.grid(alpha=0.3, which="both"); ax.legend(fontsize=6.5, loc="lower right")
    fig.tight_layout(); p = "mc20k_distributions.png"; fig.savefig(os.path.join(d, p), dpi=120); plt.close(fig); plots.append(p)
    # 3. residual sweep
    fig, ax = plt.subplots(figsize=(8, 5))
    for key, spec, IF, label, role in CONFIGS:
        rs = P["configs"][key]["residual_sweep"]
        ax.plot([float(r) * 100 for r in rs], list(rs.values()), "o-", label=label)
    ax.axhline(REQ_SYS_033_DB, color="k", ls="--", lw=1.5, label="REQ-SYS-033 70 dB")
    ax.axvline(0.3, color="grey", ls=":", label="assumed residual +/-0.3 % (estimate)")
    ax.set_xlabel("residual resonator tuning error after alignment (+/- % in frequency)"); ax.set_ylabel("worst-case corner image rejection (dB)")
    ax.set_title("r08: worst-case corner vs alignment residual (mode B, aligned at 50 ohm, Q 100)"); ax.grid(alpha=0.3); ax.legend(fontsize=7)
    fig.tight_layout(); p = "corner_vs_residual.png"; fig.savefig(os.path.join(d, p), dpi=130); plt.close(fig); plots.append(p)
    # 4. LTspice corner responses of 2+3+3: chain rejection vs tuned frequency
    fig, ax = plt.subplots(figsize=(9, 5))
    key, spec, IF = "2p3p3_if8", (2, 3, 3), 8e6
    cases = json.load(open(os.path.join(d, f"bpf_{key}_corners_cases.json")))
    lt = read_cases(d, f"bpf_{key}_corners", spec, IF, cases)
    names = ["nominal Q 100"] + [CASE_LABEL[c] for c in CASES]
    for (t, _), nm, c in zip(lt, names, ["0.4"] + [cols[c] for c in CASES]):
        ax.plot(TUNE / 1e6, t, "-", color=c, lw=1.6, label=f"{nm}: min {t.min():.1f} dB")
    ax.axhline(REQ_SYS_033_DB, color="k", ls="--", lw=1.5, label="REQ-SYS-033 70 dB")
    ax.set_xlabel("tuned frequency (MHz)"); ax.set_ylabel("image rejection, IF 8 MHz (dB)")
    ax.set_title("r08 LTspice: 2 + 3 + 3 at the worst-case corners (each corner chosen at the worst tuned frequency)")
    ax.grid(alpha=0.3); ax.legend(fontsize=7)
    fig.tight_layout(); p = "corner_2p3p3_ltspice.png"; fig.savefig(os.path.join(d, p), dpi=130); plt.close(fig); plots.append(p)
    return plots


# ------------------------------------------------------------------------------------------------ r09
J310_IN = [Port(56.0, 0.0, "J310 input 56 ohm (gfs 18 mS max)"), Port(83.0, 0.0, "J310 input 83 ohm (Re yig 12 mS typ)"),
           Port(125.0, 0.0, "J310 input 125 ohm (gfs 8 mS min)"), Port(56.0, 5e-12, "56 ohm || 5 pF (Csg max)"),
           Port(125.0, 5e-12, "125 ohm || 5 pF")]
J310_DR = [Port(50.0, 0.0, "drain port 50 ohm"), Port(100.0, 0.0, "drain port 100 ohm"), Port(200.0, 0.0, "drain port 200 ohm"),
           Port(200.0, 2.5e-12, "200 ohm || 2.5 pF (Cdg max)")]
VSWRS = (1.0, 1.1, 1.2, 1.35, 1.5, 1.75, 2.0)


def j310_case(spec, IF, pin_list, pl, pd, mode, align):
    """Chain rejection with the J310 ports: BPF1 out = pl, BPF2 in = pd, BPF2 out = pl, BPF3 in = pd, BPF3 out 50."""
    secs = T.chain_sections(spec, mode)
    ports = [(P50, pl)] + [(pd, pl)] * (len(spec) - 2) + [(pd, P50)] if len(spec) == 3 else [(P50, pl), (pd, P50)]
    tot = np.zeros(len(TUNE)); per = []
    for sec, (pin, pout) in zip(secs, ports):
        r, arg = section_search(sec, IF, [pin], [pout], align, vertices=(mode != "0"))
        tot += r; per.append((sec, r, arg, [pin], [pout]))
    j = int(np.argmin(tot))
    return dict(value=float(tot[j]), at_mhz=float(TUNE[j] / 1e6), per_f=tot, j=j, sections=per)


def prepare_r09():
    d = outdir("r09")
    out = {"run_id": RUN["r09"], "configs": {}}
    decks = []
    for key, spec, IF, label, role in CONFIGS:
        if key == "2p3_if8":
            continue
        cfg = {"label": label, "j310": [], "vswr": {}}
        lt_cases, names = [], []
        for pl in [P50] + J310_IN:
            for pd in J310_DR:
                row = {"load": pl.label, "drain": pd.label}
                for mode, align in (("0", "at50"), ("B", "at50"), ("B", "incircuit")):
                    cc = j310_case(spec, IF, None, pl, pd, mode, align)
                    row[f"{mode}-{align}"] = cc["value"]
                    if (mode, align) in (("0", "at50"), ("B", "at50")) and (pl.r, pl.c, pd.r, pd.c) in ((50, 0, 50, 0), (125, 0, 200, 0), (83, 0, 200, 0), (125, 5e-12, 200, 0), (50, 0, 200, 0), (125, 0, 50, 0)):
                        lt_cases.append(corner_case(cc, align)); names.append(f"{'nominal' if mode == '0' else 'mode B corner'}, load {pl.label}, {pd.label}")
                cfg["j310"].append(row)
        for S in VSWRS:
            cfg["vswr"][f"{S:g}"] = {}
            for mode, align in (("0", "at50"), ("B", "at50"), ("B", "incircuit"), ("A", "at50")):
                cc = chain_corner(spec, IF, mode, align, S=S)
                cfg["vswr"][f"{S:g}"][f"{mode}-{align}"] = cc["value"]
                if S in (1.2, 1.5) and (mode, align) == ("B", "at50"):
                    lt_cases.append(corner_case(cc, align)); names.append(f"mode B corner, every internal port on VSWR {S:g}")
        # BPF1 loss (transducer) with the J310 input as its load, nominal Q 120 and Q 100 (cascade input)
        s1 = T.Section(spec[0], 1, "0")
        cfg["bpf1_loss"] = {pl.label: {f"Q{q}": float(-s1.resp_db(TUNE, {}, align="at50", pout=pl, qu=q).min()) for q in (100, 120)} for pl in [P50] + J310_IN}
        pred = [float(predict_case(spec, IF, c)[0].min()) for c in lt_cases]
        cfg["ltspice_cases"] = [dict(name=n, predicted_db=p) for n, p in zip(names, pred)]
        deck = f"bpf_{key}_ports"
        MD.values_deck(deck + ".net", f"IF {IF/1e6:.0f} MHz, J310 port impedances and VSWR design-input corners (r09)", spec, lt_cases, fr_of(IF))
        json.dump(lt_cases, open(os.path.join(MD.DECKS, deck + "_cases.json"), "w"), indent=1)
        decks.append(deck + ".net")
        out["configs"][key] = cfg
        print(key, {S: round(v["B-at50"], 1) for S, v in cfg["vswr"].items()})
    out["decks"] = decks
    json.dump(out, open(os.path.join(d, "prepare.json"), "w"), indent=1)


def check_r09():
    d = outdir("r09")
    P = json.load(open(os.path.join(d, "prepare.json")))
    res = dict(P); res["checker"] = "worst_case.py check r09"
    ok_all = True
    md = [f"# {RUN['r09']}: result", "",
          "Checker: worst_case.py check r09. Question (review finding 2): what do the MMBFJ310 port impedances do to the image rejection and to the BPF1 loss, and what port tolerance must the J310 stages meet?",
          "J310 values: onsemi (Fairchild) MMBFJ309/MMBFJ310 datasheet Rev. 1.5, https://www.onsemi.com/pdf/datasheet/mmbfj310-d.pdf, read 2026-09-28: gfs 8 to 18 mS (1 kHz), Re(yig) 12 mS typ (common gate, 100 MHz, VDS 10 V, ID 10 mA), Csg 4.1 typ / 5.0 max pF and Cdg 2.0 typ / 2.5 max pF (VGS -10 V). Grounded-gate input resistance taken as 1/gfs = 56 to 125 ohm, 83 ohm typical; the drain port impedance is undefined in TS-012 (50 to 200 ohm assumed, estimate).",
          "Alignment: at50 = every resonator aligned on the NanoVNA with the section between 50 ohm ports, then placed in circuit; incircuit = aligned with the J310 ports connected. Coil Q 100, mode B tolerances for the corners.", ""]
    for key, spec, IF, label, role in CONFIGS:
        if key not in P["configs"]:
            continue
        cfg = P["configs"][key]
        cases = json.load(open(os.path.join(d, f"bpf_{key}_ports_cases.json")))
        lt = read_cases(d, f"bpf_{key}_ports", spec, IF, cases)
        for c, (t, _) in zip(cfg["ltspice_cases"], lt):
            c["ltspice_db"] = float(t.min()); c["agree"] = bool(abs(c["ltspice_db"] - c["predicted_db"]) <= MATCH_DB); ok_all &= c["agree"]
        md += [f"## {label}", "", "J310 port cases (worst image rejection over the band, dB):", "",
               "| BPF1 and BPF2 load (J310 input) | BPF2 and BPF3 source (J310 drain) | nominal, aligned at 50 | mode B corner, aligned at 50 | mode B corner, aligned in circuit |", "|---|---|---|---|---|"]
        for r in cfg["j310"]:
            md.append(f"| {r['load']} | {r['drain']} | {r['0-at50']:.1f} | {r['B-at50']:.1f} | {r['B-incircuit']:.1f} |")
        md += ["", "Every internal port anywhere on a VSWR circle around 50 ohm (8 phases; BPF1's antenna port stays 50 ohm), worst-case corner (dB):", "",
               "| VSWR | nominal | mode B, aligned at 50 | mode B, aligned in circuit | mode A, aligned at 50 |", "|---|---|---|---|---|"]
        for S, v in cfg["vswr"].items():
            md.append(f"| {S} | {v['0-at50']:.1f} | {v['B-at50']:.1f} | {v['B-incircuit']:.1f} | {v['A-at50']:.1f} |")
        md += ["", "BPF1 worst in-band transducer loss with the J310 input as its load (dB): " + "; ".join(f"{k}: {v['Q120']:.2f} (Q 120), {v['Q100']:.2f} (Q 100)" for k, v in cfg["bpf1_loss"].items()) + ".", "",
               "LTspice re-simulation of the named cases:", "", "| case | numpy (dB) | LTspice (dB) | agree |", "|---|---|---|---|"]
        for c in cfg["ltspice_cases"]:
            md.append(f"| {c['name']} | {c['predicted_db']:.2f} | {c['ltspice_db']:.2f} | {'yes' if c['agree'] else 'NO'} |")
        di = cfg["vswr"][f"{VSWR_DI:g}"]["B-at50"]
        cfg["design_input_verdict"] = "PASS" if di >= REQ_SYS_033_DB else "FAIL"
        md += ["", f"With the proposed design input (every internal port within VSWR {VSWR_DI:g} of 50 ohm, aligned at 50 ohm, mode B): worst-case corner {di:.1f} dB, **{cfg['design_input_verdict']}** (before leakage, r10).", ""]
    plots = plot_r09(d, P)
    md += [f"![{p}]({p})" for p in plots] + ["", f"LTspice agreement with every numpy prediction: {'yes' if ok_all else 'NO'}.", ""]
    res["ltspice_agreement"] = ok_all
    json.dump(res, open(os.path.join(d, "result.json"), "w"), indent=1)
    open(os.path.join(d, "result.md"), "w").write("\n".join(md))
    copy_scripts(d)
    print("\n".join(md))
    return ok_all and all(P["configs"][k]["design_input_verdict"] == "PASS" for k, s, i, l, role in CONFIGS if role == "proposed" and k in P["configs"])


def plot_r09(d, P):
    plots = []
    fig, axs = plt.subplots(1, 2, figsize=(15, 5.5))
    ax = axs[0]
    for key, cfg in P["configs"].items():
        Ss = [float(s) for s in cfg["vswr"]]
        l, = ax.plot(Ss, [v["B-at50"] for v in cfg["vswr"].values()], "o-", label=f"{cfg['label']}: mode B corner, aligned at 50")
        ax.plot(Ss, [v["0-at50"] for v in cfg["vswr"].values()], "s:", color=l.get_color(), ms=4, label=f"{cfg['label']}: nominal")
    ax.axhline(REQ_SYS_033_DB, color="k", ls="--", lw=1.5, label="REQ-SYS-033 70 dB")
    ax.axvline(VSWR_DI, color="grey", ls=":", label=f"proposed design input VSWR {VSWR_DI:g}")
    ax.set_xlabel("VSWR of every internal port (J310 inputs, J310 drains, ring) around 50 ohm, worst phase")
    ax.set_ylabel("worst image rejection (dB)"); ax.set_ylim(55, 115); ax.grid(alpha=0.3); ax.legend(fontsize=6.5)
    ax.set_title("r09: image rejection vs port mismatch (Q 100, no leakage)")
    ax = axs[1]
    cfg = P["configs"]["2p3p3_if8"]
    labs = [f"{r['load'].split(' (')[0]}\n{r['drain'].split(' (')[0]}" for r in cfg["j310"]]
    x = np.arange(len(labs))
    ax.bar(x - 0.2, [r["0-at50"] for r in cfg["j310"]], 0.4, label="nominal, aligned at 50", color="0.6")
    ax.bar(x + 0.2, [r["B-at50"] for r in cfg["j310"]], 0.4, label="mode B corner, aligned at 50", color="tab:blue")
    ax.axhline(REQ_SYS_033_DB, color="k", ls="--", lw=1.5, label="REQ-SYS-033 70 dB")
    ax.set_xticks(x); ax.set_xticklabels(labs, rotation=90, fontsize=5.5); ax.set_ylim(50, 95)
    ax.set_ylabel("worst image rejection (dB)"); ax.grid(alpha=0.3, axis="y"); ax.legend(fontsize=7)
    ax.set_title("r09: 2 + 3 + 3 at IF 8 with datasheet J310 port values (load = J310 input, source = drain)")
    fig.tight_layout(); p = "ports_sensitivity.png"; fig.savefig(os.path.join(d, p), dpi=130); plt.close(fig); plots.append(p)
    fig, ax = plt.subplots(figsize=(8, 4.6))
    for key, cfg in P["configs"].items():
        ks = list(cfg["bpf1_loss"]); ax.plot(range(len(ks)), [cfg["bpf1_loss"][k]["Q120"] for k in ks], "o-", label=f"{cfg['label']}, Q 120")
        break
    ax.plot(range(len(ks)), [cfg["bpf1_loss"][k]["Q100"] for k in ks], "s--", label="same, Q 100")
    ax.axhline(2.5, color="k", ls="--", label="proposed BPF1 limit 2.5 dB (rev 1 section 5)")
    ax.set_xticks(range(len(ks))); ax.set_xticklabels([k.split(" (")[0] for k in ks], rotation=20, fontsize=7)
    ax.set_ylabel("BPF1 worst in-band transducer loss (dB)"); ax.grid(alpha=0.3); ax.legend(fontsize=7)
    ax.set_title("r09: BPF1 loss with the first J310 input as its load (nominal parts)")
    fig.tight_layout(); p = "bpf1_loss_vs_j310_input.png"; fig.savefig(os.path.join(d, p), dpi=130); plt.close(fig); plots.append(p)
    return plots


# ------------------------------------------------------------------------------------------------ r10
CSTS = (0.0, 0.003e-12, 0.01e-12, 0.02e-12, 0.03e-12, 0.05e-12, 0.1e-12)


def prepare_r10():
    d = outdir("r10")
    out = {"run_id": RUN["r10"], "configs": {}}
    decks = []
    for key, spec, IF, label, role in CONFIGS:
        if key == "2p3_if8":
            continue
        cfg = {"label": label, "sweep": {}}
        lt_cases, names = [], []
        for cst in CSTS:
            row = {}
            for tag, mode, S in (("nominal", "0", 1.0), ("modeB-50ohm", "B", 1.0), ("design-input", "B", VSWR_DI)):
                cc = chain_corner(spec, IF, mode, "at50", S=S, cst=cst, bound=True)
                row[tag] = cc["value"]
                if tag == "design-input" and cst in (0.0, CST_DI, 0.1e-12):
                    for pm in ("t", "i"):
                        c = corner_case(cc, "at50", cst=cst, phase_mode=pm)
                        lt_cases.append(c); names.append(f"design-input corner, stray {cst*1e12:g} pF, SGN from the {'tuned' if pm == 't' else 'image'}-frequency worst phase")
                        if cst == 0.0:
                            break
            cfg["sweep"][f"{cst*1e12:g}"] = row
        cfg["design_input_corner_db"] = cfg["sweep"][f"{CST_DI*1e12:g}"]["design-input"]
        pred = [float(predict_case(spec, IF, c)[0].min()) for c in lt_cases]
        cfg["ltspice_cases"] = [dict(name=n, predicted_db=p) for n, p in zip(names, pred)]
        deck = f"bpf_{key}_leak_corner"
        MD.values_deck(deck + ".net", f"IF {IF/1e6:.0f} MHz, stray C per section at the design-input corner (r10)", spec, lt_cases, fr_of(IF))
        json.dump(lt_cases, open(os.path.join(MD.DECKS, deck + "_cases.json"), "w"), indent=1)
        decks.append(deck + ".net")
        out["configs"][key] = cfg
        print(key, {k: {t: round(v, 1) for t, v in r.items()} for k, r in cfg["sweep"].items()})
    out["decks"] = decks
    json.dump(out, open(os.path.join(d, "prepare.json"), "w"), indent=1)


def check_r10():
    d = outdir("r10")
    P = json.load(open(os.path.join(d, "prepare.json")))
    res = dict(P); res["checker"] = "worst_case.py check r10"
    ok_all = True
    md = [f"# {RUN['r10']}: result", "",
          "Checker: worst_case.py check r10. Question (review finding 5): how much stray input-to-output capacitance per section is tolerable when the tolerances and ports are at their corners, with the leak phase unknown?",
          f"Worst-phase bound: the leak is an ideal copy of the section input voltage times exp(j phi) through the stray C; phi takes 16 values and is chosen worst separately at the tuned and at the image frequency, per section (a bound: one physical leak has one phase). Design-input corner: mode B, aligned at 50 ohm, residual +/-0.3 %, every internal port within VSWR {VSWR_DI:g}, coil Q 100. LTspice can take only a real SGN (+1 or -1), so its re-simulation checks the model at those phases (agreement {MATCH_DB} dB), not the bound.", ""]
    for key, spec, IF, label, role in CONFIGS:
        if key not in P["configs"]:
            continue
        cfg = P["configs"][key]
        cases = json.load(open(os.path.join(d, f"bpf_{key}_leak_corner_cases.json")))
        lt = read_cases(d, f"bpf_{key}_leak_corner", spec, IF, cases)
        for c, (t, _) in zip(cfg["ltspice_cases"], lt):
            c["ltspice_db"] = float(t.min()); c["agree"] = bool(abs(c["ltspice_db"] - c["predicted_db"]) <= MATCH_DB); ok_all &= c["agree"]
        md += [f"## {label}", "", "| stray C per section (pF) | nominal, 50 ohm (dB) | mode B corner, 50 ohm ports (dB) | design-input corner, VSWR 1.2 ports (dB) |", "|---|---|---|---|"]
        for k, r in cfg["sweep"].items():
            md.append(f"| {k} | {r['nominal']:.1f} | {r['modeB-50ohm']:.1f} | {r['design-input']:.1f} |")
        v = cfg["design_input_corner_db"]
        cfg["verdict"] = "PASS" if v >= REQ_SYS_033_DB else "FAIL"
        md += ["", f"At the proposed stray limit of {CST_DI*1e12:g} pF per section: design-input corner {v:.1f} dB, **{cfg['verdict']}**, margin {v - REQ_SYS_033_DB:+.1f} dB.", "",
               "| LTspice case | numpy (dB) | LTspice (dB) | agree |", "|---|---|---|---|"]
        for c in cfg["ltspice_cases"]:
            md.append(f"| {c['name']} | {c['predicted_db']:.2f} | {c['ltspice_db']:.2f} | {'yes' if c['agree'] else 'NO'} |")
        md.append("")
    fig, ax = plt.subplots(figsize=(10, 5.5))
    for key, cfg in P["configs"].items():
        xs = [float(k) for k in cfg["sweep"]][1:]
        l, = ax.plot(xs, [r["design-input"] for r in list(cfg["sweep"].values())[1:]], "o-", label=f"{cfg['label']}: design-input corner")
        ax.plot(xs, [r["modeB-50ohm"] for r in list(cfg["sweep"].values())[1:]], "s--", color=l.get_color(), ms=4, label="  mode B corner, 50 ohm ports")
        ax.plot(xs, [r["nominal"] for r in list(cfg["sweep"].values())[1:]], ":", color=l.get_color(), label="  nominal")
    ax.set_xscale("log"); ax.axhline(REQ_SYS_033_DB, color="k", ls="--", lw=1.5, label="REQ-SYS-033 70 dB")
    ax.axvline(CST_DI * 1e12, color="grey", ls=":", label=f"proposed limit {CST_DI*1e12:g} pF per section")
    ax.set_xlabel("stray input-to-output capacitance per section (pF), worst-phase bound"); ax.set_ylabel("worst image rejection (dB)")
    ax.set_ylim(40, 110); ax.grid(alpha=0.3, which="both"); ax.legend(fontsize=6.5, ncol=2, loc="lower left")
    ax.set_title("r10: per-section leakage at the corners (whole-chain antenna-to-mixer leak not included)")
    fig.tight_layout(); p = "leakage_corner.png"; fig.savefig(os.path.join(d, p), dpi=130); plt.close(fig)
    md += [f"![{p}]({p})", "", f"LTspice agreement with every numpy prediction: {'yes' if ok_all else 'NO'}.", ""]
    res["ltspice_agreement"] = ok_all
    json.dump(res, open(os.path.join(d, "result.json"), "w"), indent=1)
    open(os.path.join(d, "result.md"), "w").write("\n".join(md))
    copy_scripts(d)
    print("\n".join(md))
    return ok_all and all(P["configs"][k]["verdict"] == "PASS" for k, s, i, l, role in CONFIGS if role == "proposed" and k in P["configs"])


# ------------------------------------------------------------------------------------------------ r12
# Review iteration 2, finding 6: the re-alignment residual limit at the design-input corner. Acceptance, fixed
# before the run:
#   (a) the residual limit of a configuration is the largest residual (+/- fraction of frequency, per resonator)
#       at which its design-input corner still meets REQ_SYS_033_DB. The corner is non-increasing in the residual
#       because the tolerance boxes are nested (a larger residual contains the smaller box); this is checked on the
#       grid. The limit is found by bisection to RES_TOL and stated rounded DOWN to 0.01 %;
#   (b) the proposed 2 + 3 + 3 passes r12 when its design-input corner meets REQ_SYS_033_DB at the stated limit
#       and at the +/-0.3 % estimate, the grid is monotone and every LTspice case agrees with numpy to MATCH_DB.
#       The +/-0.75 % value of revision 2 is reported (it is expected to fail).
RES_GRID = (0.0005, 0.001, 0.0015, 0.002, 0.0025, 0.003, 0.0032, 0.0035, 0.004, 0.005, 0.006, 0.0075, 0.01, 0.0125, 0.015)
RES_TOL = 1e-6             # bisection resolution on the residual (0.0001 % of frequency)
RES_EST = T.RES            # the +/-0.3 % estimate of revision 1 and 2
RES_REV2 = 0.0075          # the +/-0.75 % limit stated in revision 2 (withdrawn by revision 3)
R12_CONFIGS = [c for c in CONFIGS if c[0] != "2p3_if8"]
R12_VARIANTS = [  # tag, VSWR, stray C, label
    ("50ohm", 1.0, 0.0, "mode B, aligned at 50 ohm, 50 ohm ports, no stray (r08)"),
    ("ports", VSWR_DI, 0.0, f"+ every internal port within VSWR {VSWR_DI:g} (r09)"),
    ("di", VSWR_DI, CST_DI, f"design-input corner: + {CST_DI*1e12:g} pF per section, worst phase (r10)"),
]


def _r12_value(key, tag, res, want_cases=False):
    spec, IF = next((c[1], c[2]) for c in R12_CONFIGS if c[0] == key)
    S, cst = next((v[1], v[2]) for v in R12_VARIANTS if v[0] == tag)
    cc = chain_corner(spec, IF, "B", "at50", S=S, cst=cst, bound=cst > 0, res=res)
    out = dict(key=key, tag=tag, res=res, value=cc["value"], at_mhz=cc["at_mhz"])
    if want_cases:
        out["cases"] = [corner_case(cc, "at50", cst=cst, phase_mode=pm) for pm in (("t", "i") if cst > 0 else ("t",))]
    return out


def _r12_bisect(key, tag, lo, hi):
    """lo passes, hi fails; returns the limit and every evaluated point."""
    pts = []
    while hi - lo > RES_TOL:
        mid = 0.5 * (lo + hi)
        v = _r12_value(key, tag, mid)["value"]; pts.append((mid, v))
        lo, hi = (mid, hi) if v >= REQ_SYS_033_DB else (lo, mid)
    return dict(key=key, tag=tag, limit=lo, fail_at=hi, points=pts)


def prepare_r12():
    from concurrent.futures import ProcessPoolExecutor
    d = outdir("r12")
    out = {"run_id": RUN["r12"], "grid": list(RES_GRID), "res_tol": RES_TOL, "configs": {}}
    with ProcessPoolExecutor(max_workers=min(12, os.cpu_count() or 1)) as ex:
        jobs = [ex.submit(_r12_value, k, v[0], r) for k, *_ in R12_CONFIGS for v in R12_VARIANTS for r in RES_GRID]
        grid = [j.result() for j in jobs]
        for key, spec, IF, label, role in R12_CONFIGS:
            out["configs"][key] = {"label": label, "role": role, "spec": spec, "if_mhz": IF / 1e6, "variants": {}}
            for tag, S, cst, vl in R12_VARIANTS:
                g = [(p["res"], p["value"], p["at_mhz"]) for p in grid if p["key"] == key and p["tag"] == tag]
                vals = [v for _, v, _ in g]
                mono = all(b <= a + 1e-9 for a, b in zip(vals, vals[1:]))
                out["configs"][key]["variants"][tag] = dict(label=vl, vswr=S, cst_pf=cst * 1e12, grid=g, monotone=mono)
        bis = {}
        for key, *_ in R12_CONFIGS:
            for tag, *_ in R12_VARIANTS:
                g = out["configs"][key]["variants"][tag]["grid"]
                fails = [i for i, (_, v, _) in enumerate(g) if v < REQ_SYS_033_DB]
                if not fails:
                    out["configs"][key]["variants"][tag]["limit"] = None  # passes over the whole grid
                    continue
                i = fails[0]
                lo = g[i - 1][0] if i > 0 else 0.0
                bis[(key, tag)] = ex.submit(_r12_bisect, key, tag, lo, g[i][0])
        for (key, tag), j in bis.items():
            b = j.result(); vv = out["configs"][key]["variants"][tag]
            vv["limit"] = b["limit"]; vv["limit_stated"] = math.floor(b["limit"] * 1e4 + 1e-9) / 1e4
            vv["bisection_points"] = b["points"]
        # values at the stated limit, the estimate and the rev 2 limit, with LTspice cases (design-input variant)
        want = {}
        for key, *_ in R12_CONFIGS:
            vv = out["configs"][key]["variants"]["di"]
            pts = {"estimate": RES_EST, "rev2_limit": RES_REV2}
            if vv.get("limit") is not None:
                pts = {"stated_limit": vv["limit_stated"], **pts}
            for name, r in pts.items():
                want[(key, name)] = ex.submit(_r12_value, key, "di", r, True)
        chk = {k: j.result() for k, j in want.items()}
    decks = []
    for key, spec, IF, label, role in R12_CONFIGS:
        cfg = out["configs"][key]; vv = cfg["variants"]["di"]
        cfg["points"] = {}
        lt_cases, names = [], []
        for (k, name), p in chk.items():
            if k != key:
                continue
            cfg["points"][name] = dict(res=p["res"], value=p["value"], at_mhz=p["at_mhz"])
            for pm, c in zip(("tuned", "image"), p["cases"]):
                lt_cases.append(c); names.append(f"design-input corner at +/-{100*p['res']:.4g} % ({name}), SGN from the {pm}-frequency worst phase")
        # sensitivity at the estimate: central difference over the 0.25 and 0.35 % grid points, dB per 0.1 %
        for tag in ("50ohm", "ports", "di"):
            gg = {round(r, 6): v for r, v, _ in cfg["variants"][tag]["grid"]}
            cfg["variants"][tag]["slope_db_per_0p1pct_at_0p3"] = (gg[0.0025] - gg[0.0035]) / 1.0
        cfg["margin_at_estimate_db"] = cfg["points"]["estimate"]["value"] - REQ_SYS_033_DB
        pred = [float(predict_case(spec, IF, c)[0].min()) for c in lt_cases]
        cfg["ltspice_cases"] = [dict(name=n, predicted_db=p) for n, p in zip(names, pred)]
        deck = f"bpf_{key}_resid"
        MD.values_deck(deck + ".net", f"IF {IF/1e6:.0f} MHz, design-input corner at the residual limit, the estimate and +/-0.75 % (r12)", spec, lt_cases, fr_of(IF))
        json.dump(lt_cases, open(os.path.join(MD.DECKS, deck + "_cases.json"), "w"), indent=1)
        decks.append(deck + ".net")
        print(key, {t: (v.get("limit"), [round(x[1], 2) for x in v["grid"]]) for t, v in cfg["variants"].items()})
    out["decks"] = decks
    json.dump(out, open(os.path.join(d, "prepare.json"), "w"), indent=1, default=float)


def check_r12():
    d = outdir("r12")
    P = json.load(open(os.path.join(d, "prepare.json")))
    res = dict(P); res["checker"] = "worst_case.py check r12"; res["requirement"] = f"REQ-SYS-033 >= {REQ_SYS_033_DB:.0f} dB (TBR)"
    ok_all = True
    md = [f"# {RUN['r12']}: result", "",
          "Checker: worst_case.py check r12. Question (review iteration 2, finding 6): what alignment residual does the design-input corner of section 5 need, and how sensitive is the 2 + 3 + 3 margin to the +/-0.3 % residual estimate?",
          f"Requirement: REQ-SYS-033, image response at least {REQ_SYS_033_DB:.0f} dB (TBR) below the in-band response at every tuned frequency 144.0 to 148.0 MHz (100 kHz spacing, TC-SYS-021), at the worst-case corner.",
          f"Design-input corner: mode B, aligned at 50 ohm, coil Q 100, every internal port within VSWR {VSWR_DI:g} (8 phases), {CST_DI*1e12:g} pF stray per section with the worst-phase bound (16 phases). Residual: each resonator L x [1 - 2 r, 1 + 2 r], a +/- r error in frequency after alignment.",
          f"Acceptance (fixed before the run): (a) the residual limit is the largest r at which the design-input corner meets {REQ_SYS_033_DB:.0f} dB, by bisection to {RES_TOL*100:g} % (the corner is non-increasing in r because the boxes are nested; checked on the grid), stated rounded down to 0.01 %; (b) 2 + 3 + 3 passes r12 when it meets {REQ_SYS_033_DB:.0f} dB at the stated limit and at the +/-0.3 % estimate, the grid is monotone and every LTspice case agrees with numpy to {MATCH_DB} dB.",
          "LTspice takes a real SGN (+1 or -1) only, so its cases check the model at those phases, not the worst-phase bound (as in r10).", ""]
    grid = P["grid"]
    md += ["## Worst-case corner against the residual (dB)", "",
           "| configuration | corner | " + " | ".join(f"+/-{100*r:g} %" for r in grid) + " | monotone |",
           "|---|---|" + "---|" * len(grid) + "---|"]
    for key, spec, IF, label, role in R12_CONFIGS:
        for tag, *_ in R12_VARIANTS:
            v = P["configs"][key]["variants"][tag]
            ok_all &= v["monotone"]
            md.append(f"| {label} | {v['label']} | " + " | ".join(f"{x[1]:.2f}" for x in v["grid"]) + f" | {'yes' if v['monotone'] else 'NO'} |")
    md += ["", "## Residual limit that holds 70 dB, and the sensitivity at the +/-0.3 % estimate", "",
           "| configuration | corner | residual limit (bisection) | stated limit | slope at +/-0.3 % (dB per 0.1 %) |", "|---|---|---|---|---|"]
    for key, spec, IF, label, role in R12_CONFIGS:
        for tag, *_ in R12_VARIANTS:
            v = P["configs"][key]["variants"][tag]
            lim = f"+/-{100*v['limit']:.4f} %" if v.get("limit") is not None else f"above +/-{100*grid[-1]:g} %"
            st = f"+/-{100*v['limit_stated']:.2f} %" if v.get("limit") is not None else f"at least +/-{100*grid[-1]:g} %"
            md.append(f"| {label} | {v['label']} | {lim} | {st} | {v['slope_db_per_0p1pct_at_0p3']:.2f} |")
    md += ["", "## Design-input corner at the stated limit, the estimate and the revision 2 limit (LTspice model check)", "",
           "| configuration | point | residual | corner, worst-phase bound (dB) | verdict |", "|---|---|---|---|---|"]
    for key, spec, IF, label, role in R12_CONFIGS:
        cfg = P["configs"][key]
        for name, p in cfg["points"].items():
            p["verdict"] = "PASS" if p["value"] >= REQ_SYS_033_DB else "FAIL"
            md.append(f"| {label} | {name.replace('_', ' ')} | +/-{100*p['res']:.4g} % | {p['value']:.2f} | **{p['verdict']}** ({p['value'] - REQ_SYS_033_DB:+.2f} dB) |")
    md += ["", "| configuration | LTspice case | numpy (dB) | LTspice (dB) | agree |", "|---|---|---|---|---|"]
    lt_all = {}
    for key, spec, IF, label, role in R12_CONFIGS:
        cfg = P["configs"][key]
        cases = json.load(open(os.path.join(d, f"bpf_{key}_resid_cases.json")))
        lt = read_cases(d, f"bpf_{key}_resid", spec, IF, cases)
        lt_all[key] = lt
        for c, (t, _) in zip(cfg["ltspice_cases"], lt):
            c["ltspice_db"] = float(t.min()); c["agree"] = bool(abs(c["ltspice_db"] - c["predicted_db"]) <= MATCH_DB); ok_all &= c["agree"]
            md.append(f"| {label} | {c['name']} | {c['predicted_db']:.3f} | {c['ltspice_db']:.3f} | {'yes' if c['agree'] else 'NO'} |")
    plots = plot_r12(d, P)
    md += [""] + [f"![{p}]({p})" for p in plots] + [""]
    c3 = P["configs"]["2p3p3_if8"]; v3 = c3["variants"]["di"]
    prop_ok = bool(v3.get("limit") is not None and c3["points"]["stated_limit"]["value"] >= REQ_SYS_033_DB
                   and c3["points"]["estimate"]["value"] >= REQ_SYS_033_DB)
    head = RES_EST - v3["limit_stated"] if v3.get("limit") is not None else float("nan")
    md += [f"Verdict (2 + 3 + 3, design-input corner): **{'PASS' if prop_ok else 'FAIL'}** at the +/-0.3 % estimate ({c3['points']['estimate']['value']:.2f} dB, margin {c3['margin_at_estimate_db']:+.2f} dB) "
           f"and at the stated residual limit +/-{100*v3['limit_stated']:.2f} %; at the revision 2 limit +/-0.75 % it is {c3['points']['rev2_limit']['value']:.2f} dB (**{c3['points']['rev2_limit']['verdict']}**). "
           f"The slope at the estimate is {v3['slope_db_per_0p1pct_at_0p3']:.2f} dB per 0.1 %, so the 0.2 dB margin is {100*(v3['limit_stated'] - RES_EST):.2f} % of residual headroom. "
           f"LTspice agreement and monotone grid: {'yes' if ok_all else 'NO'}.", ""]
    res["verdict_proposed"] = prop_ok; res["ltspice_agreement_and_monotone"] = ok_all
    json.dump(res, open(os.path.join(d, "result.json"), "w"), indent=1, default=float)
    open(os.path.join(d, "result.md"), "w").write("\n".join(md))
    copy_scripts(d)
    print("\n".join(md))
    return prop_ok and ok_all


def plot_r12(d, P):
    plots = []
    styles = {"50ohm": ":", "ports": "--", "di": "-"}
    fig, ax = plt.subplots(figsize=(10.5, 6))
    for key, spec, IF, label, role in R12_CONFIGS:
        cfg = P["configs"][key]; col = None
        for tag, *_ in R12_VARIANTS:
            v = cfg["variants"][tag]
            xs = [100 * x[0] for x in v["grid"]]; ys = [x[1] for x in v["grid"]]
            l, = ax.plot(xs, ys, styles[tag], color=col, marker="o" if tag == "di" else None, ms=3.5, lw=1.8 if tag == "di" else 1.1,
                         label=f"{label.split(' (')[0]}: {v['label'].split(':')[0] if tag == 'di' else v['label']}")
            col = l.get_color()
        v = cfg["variants"]["di"]
        if v.get("limit") is not None:
            ax.plot([100 * v["limit"]], [REQ_SYS_033_DB], "D", color=col, ms=8, mec="k")
            ax.annotate(f"limit +/-{100*v['limit_stated']:.2f} %", (100 * v["limit"], REQ_SYS_033_DB), xytext={"2p3p3_if8": (6, -18), "2p3p2_if10": (-78, -20)}.get(key, (6, 8)),
                        textcoords="offset points", fontsize=8, color=col, fontweight="bold", bbox=dict(fc="white", ec="none", alpha=0.85, pad=1))
    ax.axhline(REQ_SYS_033_DB, color="k", ls="--", lw=1.5, label="REQ-SYS-033 70 dB (TBR)")
    ax.axvline(100 * RES_EST, color="grey", ls=":", lw=1.2, label="+/-0.3 % residual (estimate)")
    ax.axvline(100 * RES_REV2, color="tab:red", ls="-.", lw=1.0, label="+/-0.75 % limit of revision 2 (withdrawn)")
    ax.set_xlabel("residual resonator tuning error after alignment (+/- % in frequency)"); ax.set_ylabel("worst-case corner image rejection (dB)")
    ax.set_title("r12: corner vs alignment residual. Solid: design-input corner (mode B, VSWR 1.2 ports, 0.03 pF, worst phase); diamonds: 70 dB limit")
    ax.set_xlim(0, 100 * RES_GRID[-1] + 0.05); ax.set_ylim(55, 100); ax.grid(alpha=0.3); ax.legend(fontsize=6.8, ncol=2, loc="upper right")
    fig.tight_layout(); p = "residual_design_input.png"; fig.savefig(os.path.join(d, p), dpi=130); plt.close(fig); plots.append(p)
    # zoom on 2 + 3 + 3 around the estimate, every evaluated point (grid and bisection)
    cfg = P["configs"]["2p3p3_if8"]; v = cfg["variants"]["di"]
    pts = sorted([(x[0], x[1]) for x in v["grid"]] + [tuple(x) for x in v.get("bisection_points", [])])
    fig, ax = plt.subplots(figsize=(9.5, 5.5))
    xs = np.array([100 * a for a, _ in pts]); ys = np.array([b for _, b in pts])
    m = (xs >= 0.15) & (xs <= 0.55)
    ax.plot(xs[m], ys[m], "o-", color="tab:blue", ms=4, label="2 + 3 + 3, IF 8 MHz: design-input corner (grid and bisection points)")
    ax.axhline(REQ_SYS_033_DB, color="k", ls="--", lw=1.5, label="REQ-SYS-033 70 dB (TBR)")
    ax.axvspan(0.15, 100 * v["limit"], color="tab:green", alpha=0.08, label=f"residual that holds 70 dB: up to +/-{100*v['limit']:.3f} % (stated +/-{100*v['limit_stated']:.2f} %)")
    ax.axvline(100 * RES_EST, color="grey", ls=":", lw=1.2, label="+/-0.3 % residual (estimate)")
    e = cfg["points"]["estimate"]
    ax.annotate(f"{e['value']:.2f} dB at +/-0.3 %: margin {e['value'] - REQ_SYS_033_DB:+.2f} dB\nslope {v['slope_db_per_0p1pct_at_0p3']:.2f} dB per 0.1 %",
                (100 * RES_EST, e["value"]), xytext=(0.17, 72.6), fontsize=8, arrowprops=dict(arrowstyle="->", color="grey"))
    for c in cfg["ltspice_cases"]:
        r = float(c["name"].split("+/-")[1].split(" %")[0])
        if 0.15 <= r <= 0.55:
            ax.plot([r], [c["ltspice_db"]], "x", color="tab:orange", ms=8, mew=2)
    ax.plot([], [], "x", color="tab:orange", ms=8, mew=2, label="LTspice at SGN +1 or -1 (model check; not the worst-phase bound, so it sits above)")
    ax.set_xlim(0.15, 0.55); ax.set_ylim(66, 74.5); ax.grid(alpha=0.3); ax.legend(fontsize=7, loc="lower left")
    ax.set_xlabel("residual resonator tuning error after alignment (+/- % in frequency)"); ax.set_ylabel("worst-case corner image rejection (dB)")
    ax.set_title("r12: 2 + 3 + 3 at the design-input corner, sensitivity to the residual near the +/-0.3 % estimate")
    fig.tight_layout(); p = "residual_2p3p3_zoom.png"; fig.savefig(os.path.join(d, p), dpi=130); plt.close(fig); plots.append(p)
    return plots


if __name__ == "__main__":
    cmd, r = sys.argv[1], sys.argv[2]
    if cmd == "prepare":
        {"r08": prepare_r08, "r09": prepare_r09, "r10": prepare_r10, "r12": prepare_r12}[r]()
    elif cmd == "check":
        ok = {"r08": check_r08, "r09": check_r09, "r10": check_r10, "r12": check_r12}[r]()
        sys.exit(0 if ok else 1)
    else:
        sys.exit(f"unknown command {cmd}")
