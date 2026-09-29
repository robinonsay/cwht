#!/usr/bin/env python3
"""WP-PDR-21 revision 3 (A5 only, owner decision of 2026-09-29): drive pad, the REQ-SYS-012 low-pack basis, REQ-SYS-144.

A5 (TS-012 revision 7 section 10, design items D-7, D-8, D-9, D-13, D-14 of section 8.14):
    Si5351A CLK1 -> 5 to 15 cm coax (D-8) -> 2-resonator drive bandpass (D-13, spurs C10) -> select-on-test pi pad
    (D-7) -> GVA-84+ -> 3 dB pad -> RA07M1317M module -> output LPF (D-14, BOM values, 2 % parts) and G5V-2 relay -> SMA.

Usage (repo root, repo venv):
    .venv/bin/python hardware/sim/tx-pa/run_a5_r3.py all          # every revision 3 run below, in order
    .venv/bin/python hardware/sim/tx-pa/run_a5_r3.py d6|d7|k1|s2|p4|s3
    add --expect to compare every verdict with the list of the analysis record section 8.1 (exit 3 on a change)

Runs (each writes hardware/sim/tx-pa/results/<run-id>/: deck(s), LTspice .log and .raw (a .raw over 5,000,000
bytes stays on the owner's Mac and is named in the folder's raw.sha256, CR-017), result.json, result.md, PNG plots,
and a copy of this script and of run_pa.py, whose helpers it imports):
    d6  A5 drive chain with the D-13 drive bandpass and the fixed 18 dB pad: 810 part corners x 5 bandpass tolerance
        cases x 2 coil Q values = 8100 corners (transient; fundamental, 3f and the CLK1 pin load by DFT)
    d7  coax-length bound of the bandpass chain (every electrical length, the extreme part corners) and the 10 ps
        time-step check of d6
    k1  the select-on-test level reading at about 17 mW: 1N5711-class diode probe on the Fluke 174 across the
        50 ohm load, with its forward drop measured at DC at two currents (LTspice transient and DC; the reading
        equation and its residual error over diode parameters, temperature, frequency and harmonic content)
    s2  the select-on-test pad set for the bandpass chain and the in-service drive band with the k1 reading term
    p4  A5 output power at the SMA versus pack voltage with the adopted design: drive band of s2, D-9 VGG clamp
        (3.30 to 3.50 V at 6.4 V, open-loop module at most 8 W at 8.4 V from a -10 C start), D-14 LPF loss, drain
        feed from the datasheet reads (C2), 9 temperature cases
    s3  the REQ-SYS-012 low-pack basis (lowest available power per case, the pack voltage at which 3.97 W is
        reached, the proposed delta values) and the verdict list

LTspice runs only through tools/ltspice-batch.sh (ACC-LTSPICE-001), by run_pa.run_ltspice. Every value marked "est."
is an estimate, not a datasheet or measured value.
"""
from __future__ import annotations

import itertools
import json
import shutil
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import run_pa as P  # noqa: E402  (helpers, inputs and the GVA-84+ model of revisions 0 to 2)
from run_pa import plt, INK, INK2, GRID, COL  # noqa: E402

DATE = "2026-09-29"
REVISION = 3
RUNS3 = {
    "d6": f"{DATE}-r3-d6-drive-a5-bpf",
    "d7": f"{DATE}-r3-d7-coax-bound-bpf",
    "k1": f"{DATE}-r3-k1-probe-17mw",
    "s2": f"{DATE}-r3-s2-sot-pad",
    "p4": f"{DATE}-r3-p4-power-a5-design",
    "p5": f"{DATE}-r3-p5-power-a5-clamp-b",
    "s3": f"{DATE}-r3-s3-req012-basis",
}
P.RUNS.update(RUNS3)
VERDICTS = P.VERDICTS
verdict = P.verdict


def rundir(k: str) -> Path:
    return P.rundir(k)


def copy_inputs(out: Path, decks: list[Path]):
    shutil.copy2(Path(__file__), out / Path(__file__).name)
    shutil.copy2(HERE / "run_pa.py", out / "run_pa.py")
    for d in decks:
        if d.parent != out:
            shutil.copy2(d, out / d.name)


def raw_manifest(out: Path):
    """CR-017: every .raw over 5,000,000 bytes in the run folder is named in raw.sha256 (comment line with the size,
    then the shasum -a 256 line), and is not committed."""
    import hashlib
    big = sorted(p for p in out.iterdir() if p.suffix.lower() == ".raw" and p.stat().st_size > 5_000_000)
    lines = []
    for p in big:
        lines.append(f"# {p.name} {p.stat().st_size} bytes")
        lines.append(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}")
    man = out / "raw.sha256"
    if big:
        man.write_text("\n".join(lines) + "\n")
    elif man.exists():
        man.unlink()
    return [p.name for p in big]


# ---------------------------------------------------------------- D-13 drive bandpass (spurs C10), read values
# Topology and values: docs/design/analysis/spurs-ts012.md option C10 and hardware/sim/freq/tx_spur_filters.cir
# circuit B: series 7.5 pF, resonator 47 nH || 16 pF, coupling 2.4 pF, resonator 47 nH || 16 pF, series 7.5 pF.
# Coil: Coilcraft 1812SMS-47NG (Document 184-1, "Midi Spring Air Core Inductors", read 2026-09-29 through the
# web-fetch tool from coilcraft.com, SHA-256 e8ce1b27f9bea463...): 47 nH, tolerance G = 2 %, Q typ 135 and min 100 at
# 150 MHz, SRF min 2.1 GHz, DCR max 5.6 mohm (D). Revision 2's est. Q 60 of the spur note is replaced by the read
# minimum. The coil's parallel capacitance 1/((2 pi SRF)^2 L) = 0.12 pF at the minimum SRF.
# Capacitors (C0G, 0805 or 1206): 16 pF at G = +/-2 % (D, the part-number code); 7.5 pF and 2.4 pF are below 10 pF,
# where C0G tolerance is absolute: B = +/-0.1 pF (est.: the tolerance code; the part is read at the ordering gate),
# not 2 % as the spur note assumed (+/-4.2 % for 2.4 pF). ESR 0.1 ohm, ESL plus via 1 nH on the shunt capacitors and
# 0.5 nH on the series ones (est., as the revision 2 drive LPF).
# Tolerance cases (joint, the detuning directions): nom; low (L -2 %, 16 pF -2 %, 7.5 and 2.4 pF -0.1 pF); high (all
# +); low with the coupling capacitor high; high with the coupling capacitor low. Coil Q 100 and 135.
BPF_L_NH, BPF_CSER_PF, BPF_CRES_PF, BPF_CCPL_PF = 47.0, 7.5, 16.0, 2.4
BPF_SRF_MIN_HZ = 2.1e9
BPF_Q = [100.0, 135.0]
BPF_CASES = [  # (label, kL, kCres, dCser pF, dCcpl pF)
    ("nom", 1.00, 1.00, 0.0, 0.0),
    ("low", 0.98, 0.98, -0.1, -0.1),
    ("high", 1.02, 1.02, 0.1, 0.1),
    ("low, coupling high", 0.98, 0.98, -0.1, 0.1),
    ("high, coupling low", 1.02, 1.02, 0.1, -0.1),
]
F_Q_HZ = 146e6   # the coil series resistance is 2 pi f L / Q at the carrier (Q read at 150 MHz)


def bpf_text(q_expr: str = "{qbpf}", kl: str = "{kl}", kc: str = "{kc}", ds: str = "{dcs}", dc: str = "{dcc}") -> str:
    lpar = 1.0 / ((2 * np.pi * BPF_SRF_MIN_HZ) ** 2 * BPF_L_NH * 1e-9)
    return f"""* D-13 drive bandpass (spurs C10) on the RF board: 1812SMS-47NG (Q {q_expr} at 150 MHz, SRF 2.1 GHz min), C0G
Cs1 lpfin b1 {{({BPF_CSER_PF}+{ds[1:-1]})*1p}} Rser=0.1 Lser=0.5n
L1 b1 0 {{{BPF_L_NH}n*{kl[1:-1]}}} Rser={{2*pi*{F_Q_HZ:.0f}*{BPF_L_NH}n*{kl[1:-1]}/{q_expr[1:-1]}}} Cpar={lpar * 1e12:.3f}p
Cr1 b1 0 {{{BPF_CRES_PF}p*{kc[1:-1]}}} Rser=0.1 Lser=1n
Cc b1 b2 {{({BPF_CCPL_PF}+{dc[1:-1]})*1p}} Rser=0.1 Lser=0.5n
L2 b2 0 {{{BPF_L_NH}n*{kl[1:-1]}}} Rser={{2*pi*{F_Q_HZ:.0f}*{BPF_L_NH}n*{kl[1:-1]}/{q_expr[1:-1]}}} Cpar={lpar * 1e12:.3f}p
Cr2 b2 0 {{{BPF_CRES_PF}p*{kc[1:-1]}}} Rser=0.1 Lser=1n
Cs2 b2 lpf {{({BPF_CSER_PF}+{ds[1:-1]})*1p}} Rser=0.1 Lser=0.5n
"""


def bpf_corners_full():
    """Order of the d6 deck: isrc fastest, then freq, P1dB set, gain, source R, coax, bandpass case, coil Q."""
    out = []
    for iq, q in enumerate(BPF_Q):
        for ib, b in enumerate(BPF_CASES):
            for c in P.drive_corners():
                out.append(dict(c, bpf=b[0], qbpf=q))
    return out


T_END_NS, T_START_NS = 250, 228   # the bandpass rings down with tau about 2 Q_L / w (about 20 ns): 10 tau before the DFT window


def deck_d6(out: Path, mode: str = "full", tstep: str = "20p", t_end_ns: int = T_END_NS) -> tuple[Path, list[dict]]:
    """mode "full": d6 (8100 corners); "d7": coax length bound (the P.D4_SETS corners, nominal bandpass, both Q);
    "tstep": the D4 sets at 10 cm, nominal bandpass, Q 100, 10 ps step."""
    src = {s[0]: s for s in P.SRC_CASES}
    if mode == "full":
        dims = [("isrc", 3), ("ifr", 3), ("ip1", 3), ("ig", 5), ("irs", 2), ("icx", 3), ("ib", len(BPF_CASES)),
                ("iq", len(BPF_Q))]
        tables = [("vddo", "isrc", [c[1] for c in P.SRC_CASES]), ("tr", "isrc", [c[2] / 0.6 for c in P.SRC_CASES]),
                  ("duty", "isrc", [c[3] for c in P.SRC_CASES]), ("freq", "ifr", P.FREQS),
                  ("vsat", "ip1", [P.RAPP_VSAT[s[0]] for s in P.P1DB_SETS]), ("gdb", "ig", P.GAINS),
                  ("rsrc", "irs", P.RSRC), ("clen", "icx", P.COAX_M)]
        corners = bpf_corners_full()
        name = "drive_a5_bpf.cir"
        order = ("source case fastest, then frequency, GVA-84+ P1dB set, GVA-84+ gain, Si5351 output resistance, coax "
                 "length, bandpass tolerance case, coil Q")
    else:
        lens = P.D4_LEN if mode == "d7" else [P.COAX_M[1]]
        qs = BPF_Q if mode == "d7" else [BPF_Q[0]]
        dims = [("ilen", len(lens)), ("iset", len(P.D4_SETS)), ("ifr", 3), ("ib", 1), ("iq", len(qs))]
        tables = [("clen", "ilen", lens), ("rsrc", "iset", [s[1] for s in P.D4_SETS]),
                  ("gdb", "iset", [s[2] for s in P.D4_SETS]), ("vsat", "iset", [P.RAPP_VSAT[s[3]] for s in P.D4_SETS]),
                  ("vddo", "iset", [src[s[4]][1] for s in P.D4_SETS]),
                  ("tr", "iset", [src[s[4]][2] / 0.6 for s in P.D4_SETS]),
                  ("duty", "iset", [src[s[4]][3] for s in P.D4_SETS]), ("freq", "ifr", P.FREQS)]
        corners = []
        for q in qs:
            for f in P.FREQS:
                for lab, rs, g, pl, sc in P.D4_SETS:
                    for ln in lens:
                        _, vddo, tr, duty = src[sc]
                        corners.append(dict(set=lab, rsrc=rs, gain=g, p1db=pl, freq=f, src=sc, vddo=vddo, tr=tr,
                                            duty=duty, coax_m=ln, bpf="nom", qbpf=q))
        name = "coax_a5_bpf.cir" if mode == "d7" else "tstep_a5_bpf.cir"
        order = "coax length fastest, then corner set, then frequency, then coil Q (nominal bandpass)"
    lines, n = P.radix_lines(dims)
    assert n == len(corners), (n, len(corners))
    tabs = []
    for pname, iname, vals in tables:
        tabs.append(f".param {pname}=" + (f"table({iname}," + ",".join(f"{i},{v:.6g}" for i, v in enumerate(vals)) + ")"
                                          if len(vals) > 1 else f"{vals[0]:.6g}"))
    bcases = BPF_CASES if mode == "full" else BPF_CASES[:1]
    qv = BPF_Q if mode != "tstep" else BPF_Q[:1]
    for pname, j in (("kl", 1), ("kc", 2), ("dcs", 3), ("dcc", 4)):
        vals = [b[j] for b in bcases]
        tabs.append(f".param {pname}=" + ("table(ib," + ",".join(f"{i},{v:.6g}" for i, v in enumerate(vals)) + ")"
                                          if len(vals) > 1 else f"{vals[0]:.6g}"))
    tabs.append(".param qbpf=" + ("table(iq," + ",".join(f"{i},{v:.6g}" for i, v in enumerate(qv)) + ")"
                                   if len(qv) > 1 else f"{qv[0]:.6g}"))
    chain, _ = P.chain_text("a5")
    txt = f"""* {name}: A5 Si5351A CLK1 -> coax -> D-13 drive bandpass -> 18 dB pad -> GVA-84+ -> 3 dB pad -> RA07M1317M input (50 ohm)
* cwht WP-PDR-21 revision 3 (A5), hardware/sim/tx-pa/run_a5_r3.py (record docs/design/analysis/pa-drive-ts012.md)
* {n} steps flattened into one .step (idx): {order}.
* Source, CLK1 pin load, coax, pads and GVA-84+ model as revisions 1 and 2 (run_pa.py); the drive LPF of TS-012
* revision 4 is replaced by the D-13 bandpass (TS-012 revision 7 section 8.14).
.param idx=0
.step param idx 0 {n - 1} 1
{chr(10).join(lines)}
{chr(10).join(tabs)}
.param T=1/freq
.param ton=duty*T-tr
.param G=pow(10,gdb/20)
.param p={P.RAPP_P}
V1 vs 0 PULSE({{-duty*vddo}} {{(1-duty)*vddo}} 0 {{tr}} {{tr}} {{ton}} {{T}})
Rsrc vs clk {{rsrc}}
* lumped load on the CLK1 pin (main board): prescaler tap {P.C_TAP_PF:g} pF and stub {P.C_STUB_PF:g} pF (est.)
Ctap clk 0 {P.C_TAP_PF:g}p
Cstub clk 0 {P.C_STUB_PF:g}p
* D-8: 50 ohm coax through the bulkhead (lossless; velocity factor {P.COAX_VF}, length clen in metres)
T1 clk 0 lpfin 0 Td={{clen/({P.COAX_VF}*{P.C_LIGHT:.0f})}} Z0={P.COAX_Z0:g}
{bpf_text()}{chain}.tran 0 {t_end_ns}n {t_end_ns - 22}n {tstep}
.options plotwinsize=0
.save V(clk) V(gin) V(pa_in) I(Rsrc)
.end
"""
    p = out / name
    p.write_text(txt)
    return p, corners


def read_rows(raw: Path, corners: list[dict]) -> list[dict]:
    return P.read_drive_raw("a5", raw, corners)


def is_nominal_bpf(r):
    return P.is_nominal_drive(r) and r["bpf"] == "nom" and r["qbpf"] == BPF_Q[0]


def run_d6():
    out = rundir("d6")
    deck, corners = deck_d6(out, "full")
    prov = P.run_ltspice(deck, out, timeout=14400)
    rows = read_rows(out / "drive_a5_bpf.raw", corners)
    verdict("d6", "check: one .raw step per corner", len(rows) == len(corners), "check", f"{len(rows)} steps")
    pin = np.array([r["pin_pa_w"] for r in rows])
    h3 = np.array([r["h3_dbc_gva_in"] for r in rows])
    gin = np.array([r["gva_in_dbm"] for r in rows])
    cp = np.array([r["pin_load_cp_pf"] for r in rows])
    nominal = next(r for r in rows if is_nominal_bpf(r))
    crit = np.array([r["pin_pa_w"] for r in rows if r["gain"] in (22.5, 25.0) and r["src"] == "nom"])
    lo, hi = min(rows, key=lambda r: r["pin_pa_w"]), max(rows, key=lambda r: r["pin_pa_w"])
    inwin = (pin >= 10e-3) & (pin <= 30e-3)
    # the LPF chain of revision 1 (d2) at the same 810 part corners, for the comparison the D-13 condition asks
    d2 = json.loads((P.rundir("d2") / "corners.json").read_text())
    d2nom = next(r for r in d2 if P.is_nominal_drive(r))
    res = {"run": RUNS3["d6"], "revision": REVISION, "ltspice": prov, "n_corners": len(rows),
           "bpf": {"L_nH": BPF_L_NH, "Cser_pF": BPF_CSER_PF, "Cres_pF": BPF_CRES_PF, "Ccpl_pF": BPF_CCPL_PF,
                   "Q": BPF_Q, "cases": [b[0] for b in BPF_CASES]},
           "pad_in_db": float(P.pad_loss_db(*P.PADS["a5_in"])),
           "pin_pa_mw": {"min": float(pin.min() * 1e3), "nominal": nominal["pin_pa_w"] * 1e3, "max": float(pin.max() * 1e3)},
           "pin_pa_dbm": {"min": float(P.dbm(pin.min())), "nominal": nominal["pin_pa_dbm"], "max": float(P.dbm(pin.max()))},
           "criterion_corners_mw": [float(crit.min() * 1e3), float(crit.max() * 1e3)],
           "corners_in_window": int(inwin.sum()), "corners_below_10mw": int((pin < 10e-3).sum()),
           "corners_above_30mw": int((pin > 30e-3).sum()), "spread_db": float(P.dbm(pin.max()) - P.dbm(pin.min())),
           "overdrive_margin_db": float(10 * np.log10(30e-3 / pin.max())),
           "h3_dbc_worst": float(h3.max()), "gva_in_dbm_max": float(gin.max()),
           "gva_out_dbm_max": float(max(r["gva_out_dbm"] for r in rows)),
           "clk_vpp": [float(min(r["clk_vpp"] for r in rows)), float(max(r["clk_vpp"] for r in rows))],
           "pin_load_cp_pf": [float(cp.min()), float(cp.max())],
           "pin_load_absz_ohm": [float(min(r["pin_load_absz_ohm"] for r in rows)), float(max(r["pin_load_absz_ohm"] for r in rows))],
           "nominal_corner": nominal, "corner_min": lo, "corner_max": hi,
           "lpf_chain_d2_nominal_mw": d2nom["pin_pa_w"] * 1e3,
           "nominal_vs_lpf_chain_db": nominal["pin_pa_dbm"] - d2nom["pin_pa_dbm"],
           "per_case": {}}
    for q in BPF_Q:
        for b in BPF_CASES:
            sel = np.array([r["pin_pa_w"] for r in rows if r["bpf"] == b[0] and r["qbpf"] == q])
            nm = next(r for r in rows if P.is_nominal_drive(r) and r["bpf"] == b[0] and r["qbpf"] == q)
            res["per_case"][f"{b[0]}, Q {q:g}"] = {"min_mw": float(sel.min() * 1e3), "max_mw": float(sel.max() * 1e3),
                                                   "nominal_part_corner_mw": nm["pin_pa_w"] * 1e3}
    verdict("d6", "A5 lumped CLK1 pin load at most 15 pF (Si5351 Table 7)", P.C_TAP_PF + P.C_STUB_PF <= P.CL_MAX_PF)
    verdict("d6", "A5 equivalent CLK1 pin load at most 15 pF at every corner (bandpass chain)", cp.max() <= P.CL_MAX_PF,
            detail=f"{cp.min():.1f} to {cp.max():.1f} pF")
    verdict("d6", "A5 3f at the GVA-84+ input at least 25 dB below f", h3.max() <= -P.H3_MIN_DBC, detail=f"{h3.max():.1f} dBc")
    verdict("d6", "A5 GVA-84+ input below +13 dBm", gin.max() < P.GVA_ABSMAX_IN_DBM, detail=f"{gin.max():.1f} dBm")
    verdict("d6", "A5 module input 10 to 30 mW at every corner (fixed 18 dB pad, bandpass chain)", bool(inwin.all()),
            detail=f"{pin.min() * 1e3:.1f} to {pin.max() * 1e3:.1f} mW; {int((pin < 10e-3).sum())} under 10 mW, "
                   f"{int((pin > 30e-3).sum())} over 30 mW of {len(rows)}")
    res["verdicts"] = VERDICTS.get("d6", {})
    (out / "corners.json").write_text(json.dumps(rows, indent=0))
    plot_d6(out, rows, res)
    (out / "result.json").write_text(json.dumps(res, indent=1, default=float))
    write_d6_md(out, res)
    copy_inputs(out, [deck])
    res["kept_raw"] = raw_manifest(out)
    (out / "result.json").write_text(json.dumps(res, indent=1, default=float))
    print("d6", json.dumps({k: res[k] for k in ("pin_pa_mw", "corners_in_window", "corners_below_10mw",
                                                 "corners_above_30mw", "h3_dbc_worst", "pin_load_cp_pf",
                                                 "nominal_vs_lpf_chain_db")}, default=float))
    return res


def plot_d6(out: Path, rows: list[dict], res: dict):
    from matplotlib.ticker import FixedLocator, NullLocator, ScalarFormatter
    fig, axs = plt.subplots(1, 2, figsize=(11.5, 5.2), gridspec_kw={"width_ratios": [1.5, 1]})
    ax = axs[0]
    cols = {"nom": INK2, "low": COL["a5"], "high": COL["a4"], "low, coupling high": COL["aux"], "high, coupling low": "#b3401a"}
    labels = [f"{b[0]}, Q {q:g}" for q in BPF_Q for b in BPF_CASES]
    for j, lab in enumerate(labels):
        b, q = lab.rsplit(", Q ", 1)
        sel = np.array([r["pin_pa_w"] * 1e3 for r in rows if r["bpf"] == b and r["qbpf"] == float(q)])
        xs = j + 0.8 * (np.random.default_rng(j).random(len(sel)) - 0.5)
        ax.scatter(xs, sel, s=2, color=cols[b], alpha=0.5, zorder=3)
    ax.axhspan(10, 30, color=COL["ok"], alpha=0.08, zorder=0)
    ax.axhline(30, color=INK, lw=1.3, label="30 mW: module maximum rating, top of the stability window")
    ax.axhline(10, color=INK, lw=1.3, ls="--", label="10 mW: bottom of the stability window")
    ax.set_yscale("log")
    ax.set_ylim(3, 60)
    ax.yaxis.set_major_locator(FixedLocator([3, 4, 5, 6, 8, 10, 15, 20, 30, 40, 60]))
    ax.yaxis.set_minor_locator(NullLocator())
    ax.yaxis.set_major_formatter(ScalarFormatter())
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels([l.replace(", Q", "\nQ") for l in labels], rotation=60, fontsize=6.5, ha="right")
    ax.set_ylabel("Fundamental power at the RA07M1317M input (mW)")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.30), fontsize=7)
    ax.set_title(f"d6: drive with the D-13 bandpass and the fixed 18 dB pad, {len(rows)} corners\n"
                 f"(each column: 810 part corners with coax 5 to 15 cm; 25 C)", fontsize=9)
    ax = axs[1]
    cp = np.array([r["pin_load_cp_pf"] for r in rows])
    h3 = np.array([r["h3_dbc_gva_in"] for r in rows])
    ax.scatter(cp, h3, s=2, color=COL["a5"], alpha=0.4)
    ax.axvline(P.CL_MAX_PF, color=INK, lw=1.2, label="15 pF: Si5351 Table 7 load maximum")
    ax.axhline(-P.H3_MIN_DBC, color=INK, lw=1.2, ls="--", label="-25 dBc: TS-012 3f limit at the GVA-84+ input")
    ax.set_xlabel("Equivalent shunt capacitance at the CLK1 pin at f (pF)")
    ax.set_ylabel("3f relative to f at the GVA-84+ input (dBc)")
    ax.set_xlim(min(0, cp.min() - 2), max(30, cp.max() + 2))
    ax.set_ylim(min(-70, h3.min() - 3), -15)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.14), fontsize=7)
    ax.set_title("CLK1 pin load and 3f, every d6 corner", fontsize=9)
    fig.tight_layout()
    fig.savefig(out / "drive_a5_bpf_corners.png", dpi=150)
    plt.close(fig)


def write_d6_md(out: Path, r: dict):
    L = [f"# {r['run']}: A5 drive chain with the D-13 drive bandpass (revision 3)", "",
         f"{r['n_corners']} corners: 270 part corners (Si5351 25 and 50 ohm, 3 edge and VDDO cases, GVA-84+ gain 22.5 to "
         f"25.3 dB, 3 P1dB sets, 144, 146, 148 MHz) x coax 5, 10, 15 cm x 5 bandpass tolerance cases x coil Q 100 and 135; "
         f"fixed 18 dB pad ({r['pad_in_db']:.2f} dB); 25 C. All values estimates (graph reads and est. parasitics).", "",
         "| Quantity | Min | Nominal | Max | Limit | Verdict |", "|---|---|---|---|---|---|",
         f"| Power into the module (mW) | {r['pin_pa_mw']['min']:.1f} | {r['pin_pa_mw']['nominal']:.1f} | {r['pin_pa_mw']['max']:.1f} | 10 to 30 | "
         f"{'PASS' if r['corners_in_window'] == r['n_corners'] else 'FAIL'}: {r['corners_below_10mw']} under 10 mW, {r['corners_above_30mw']} over 30 mW |",
         f"| TS-012 criterion corners (mW) | {r['criterion_corners_mw'][0]:.1f} | - | {r['criterion_corners_mw'][1]:.1f} | 10 to 30 | - |",
         f"| 3f at the GVA-84+ input (dBc) | - | - | {r['h3_dbc_worst']:.1f} | at most -25 | {'PASS' if r['h3_dbc_worst'] <= -25 else 'FAIL'} |",
         f"| GVA-84+ input (dBm) | - | - | {r['gva_in_dbm_max']:.1f} | below +13 | {'PASS' if r['gva_in_dbm_max'] < 13 else 'FAIL'} |",
         f"| GVA-84+ output (dBm) | - | - | {r['gva_out_dbm_max']:.1f} | P1dB min 19.4 | informative |",
         f"| CLK1 pin equivalent shunt C (pF) | {r['pin_load_cp_pf'][0]:.1f} | - | {r['pin_load_cp_pf'][1]:.1f} | at most 15 | {'PASS' if r['pin_load_cp_pf'][1] <= 15 else 'FAIL'} |",
         f"| CLK1 pin impedance magnitude (ohm) | {r['pin_load_absz_ohm'][0]:.0f} | - | {r['pin_load_absz_ohm'][1]:.0f} | - | informative |",
         f"| CLK1 swing at the tap (Vpp) | {r['clk_vpp'][0]:.2f} | - | {r['clk_vpp'][1]:.2f} | - | input to WP-PDR-20 |", "",
         f"Nominal part corner with the bandpass (nominal parts, Q 100): {r['pin_pa_mw']['nominal']:.1f} mW, "
         f"{r['nominal_vs_lpf_chain_db']:+.2f} dB against the revision 1 low-pass chain (d2, {r['lpf_chain_d2_nominal_mw']:.1f} mW).", "",
         "Per bandpass case (810 part corners each):", "", "| Case | Min (mW) | Max (mW) | Nominal part corner (mW) |", "|---|---|---|---|"]
    for k, v in r["per_case"].items():
        L.append(f"| {k} | {v['min_mw']:.1f} | {v['max_mw']:.1f} | {v['nominal_part_corner_mw']:.1f} |")
    L += ["", f"- Lowest corner: {P.cstr(r['corner_min'])}, bandpass {r['corner_min']['bpf']}, Q {r['corner_min']['qbpf']:g}.",
          f"- Highest corner: {P.cstr(r['corner_max'])}, bandpass {r['corner_max']['bpf']}, Q {r['corner_max']['qbpf']:g}.", "",
          "Plot `drive_a5_bpf_corners.png`; every corner in `corners.json`; deck `drive_a5_bpf.cir`.", ""]
    (out / "result.md").write_text("\n".join(L))


def run_d7():
    out = rundir("d7")
    deck, corners = deck_d6(out, "d7")
    prov = P.run_ltspice(deck, out, timeout=7200)
    rows = read_rows(out / "coax_a5_bpf.raw", corners)
    pin = np.array([r["pin_pa_w"] for r in rows])
    res = {"run": RUNS3["d7"], "revision": REVISION, "ltspice": prov, "n_steps": len(rows),
           "max_mw_any_length": float(pin.max() * 1e3), "min_mw_any_length": float(pin.min() * 1e3),
           "corner_max": max(rows, key=lambda r: r["pin_pa_w"]), "corner_min": min(rows, key=lambda r: r["pin_pa_w"]),
           "pin_load_cp_pf_any_length": [float(min(r["pin_load_cp_pf"] for r in rows)), float(max(r["pin_load_cp_pf"] for r in rows))],
           "h3_dbc_worst_any_length": float(max(r["h3_dbc_gva_in"] for r in rows))}
    # per built unit at 146 MHz over every length: the loss the select-on-test pad must supply (target 17.3 mW)
    tgt = float(P.dbm(P.SOT_TARGET_MW * 1e-3))
    pad18 = float(P.pad_loss_db(*P.PADS["a5_in"]))
    need = [pad18 + (r["pin_pa_dbm"] - tgt) for r in rows if r["freq"] == 146e6]
    res["pad_needed_any_length_db"] = [float(min(need)), float(max(need))]
    # frequency span within a unit (same set, length and Q) over every length
    spans = {}
    for r in rows:
        spans.setdefault((r["set"], r["coax_m"], r["qbpf"]), []).append(r["pin_pa_dbm"])
    res["freq_span_within_unit_any_length_db"] = float(max(max(v) - min(v) for v in spans.values()))
    json.dump(rows, open(out / "coax_a5_bpf_steps.json", "w"), indent=0)
    # numerical check: the D4 sets at 10 cm, nominal bandpass, Q 100, with a 10 ps step and 400 ns of settling against the
    # d6 rows (20 ps, 250 ns)
    deck10, cs10 = deck_d6(out, "tstep", tstep="10p", t_end_ns=400)
    prov10 = P.run_ltspice(deck10, out)
    r10 = read_rows(out / "tstep_a5_bpf.raw", cs10)
    ref = json.loads((rundir("d6") / "corners.json").read_text())
    diffs = []
    for r in r10:
        m = next(x for x in ref if x["rsrc"] == r["rsrc"] and x["gain"] == r["gain"] and x["p1db"] == r["p1db"]
                 and x["freq"] == r["freq"] and x["src"] == r["src"] and abs(x["coax_m"] - 0.10) < 1e-9
                 and x["bpf"] == "nom" and x["qbpf"] == BPF_Q[0])
        diffs.append((abs(m["pin_pa_dbm"] - r["pin_pa_dbm"]), abs(m["h3_dbc_gva_in"] - r["h3_dbc_gva_in"])))
    dd = np.array(diffs)
    res["timestep_check"] = {"ltspice": prov10, "n": len(r10), "max_diff_pin_db": float(dd[:, 0].max()),
                             "max_diff_h3_db": float(dd[:, 1].max())}
    verdict("d7", "check: 10 ps step and 400 ns settling against 20 ps and 250 ns within 0.02 dB (power) and 0.5 dB (3f)",
            bool(dd[:, 0].max() <= 0.02 and dd[:, 1].max() <= 0.5), "check",
            f"{dd[:, 0].max():.4f} dB, {dd[:, 1].max():.3f} dB")
    verdict("d7", "A5 module input at most 30 mW at any coax length (fixed pad, bandpass chain)", pin.max() <= 30e-3,
            detail=f"{pin.max() * 1e3:.1f} mW")
    res["verdicts"] = VERDICTS.get("d7", {})
    # plot
    from matplotlib.ticker import FixedLocator, NullLocator, ScalarFormatter
    fig, ax = plt.subplots(figsize=(8.0, 5.0))
    setcol = {P.D4_SETS[0][0]: COL["a4"], P.D4_SETS[1][0]: "#b3401a", P.D4_SETS[2][0]: INK2,
              P.D4_SETS[3][0]: COL["a5"], P.D4_SETS[4][0]: COL["aux"]}
    fls = {144e6: ":", 146e6: "-", 148e6: "--"}
    for s in P.D4_SETS:
        for f in P.FREQS:
            sel = [r for r in rows if r["set"] == s[0] and r["freq"] == f and r["qbpf"] == BPF_Q[0]]
            ax.plot([r["coax_m"] * 100 for r in sel], [r["pin_pa_w"] * 1e3 for r in sel], color=setcol[s[0]], ls=fls[f],
                    lw=1.4, label=f"{s[0]}" if f == 146e6 else None)
    ax.axvspan(5, 15, color=COL["ok"], alpha=0.08, lw=0)
    ax.axhline(30, color=INK, lw=1.4, label="30 mW: module maximum rating")
    ax.axhline(10, color=INK, lw=1.4, ls="-.", label="10 mW: bottom of the stability window")
    ax.set_yscale("log")
    ax.set_ylim(3, 60)
    ax.yaxis.set_major_locator(FixedLocator([3, 4, 5, 6, 8, 10, 15, 20, 30, 40, 60]))
    ax.yaxis.set_minor_locator(NullLocator())
    ax.yaxis.set_major_formatter(ScalarFormatter())
    ax.set_xlim(0, 70)
    ax.set_xlabel(f"Coax length, CLK1 to the drive bandpass (cm; VF {P.COAX_VF})")
    ax.set_ylabel("Fundamental power at the RA07M1317M input (mW)")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.14), ncol=2, fontsize=7)
    ax.set_title("d7: bandpass chain, fixed 18 dB pad, extreme part corners over every coax length\n"
                 "(nominal bandpass, coil Q 100; 144 dotted, 146 solid, 148 MHz dashed; green: 5 to 15 cm)", fontsize=9)
    fig.tight_layout()
    fig.savefig(out / "coax_length_bound_bpf.png", dpi=150)
    plt.close(fig)
    (out / "result.json").write_text(json.dumps(res, indent=1, default=float))
    L = [f"# {res['run']}: coax-length bound of the bandpass chain and the time-step check (revision 3)", "",
         f"- Over every length (0.5 to 70 cm) the fixed-pad drive spans {res['min_mw_any_length']:.1f} to {res['max_mw_any_length']:.1f} mW.",
         f"- Highest step: {P.cstr(res['corner_max'])}, Q {res['corner_max']['qbpf']:g}.",
         f"- Lowest step: {P.cstr(res['corner_min'])}, Q {res['corner_min']['qbpf']:g}.",
         f"- Pad loss a unit needs at 146 MHz for 17.3 mW, any length: {res['pad_needed_any_length_db'][0]:.2f} to {res['pad_needed_any_length_db'][1]:.2f} dB.",
         f"- Frequency span of the drive within one unit, any length: {res['freq_span_within_unit_any_length_db']:.2f} dB.",
         f"- CLK1 pin equivalent shunt C over every length: {res['pin_load_cp_pf_any_length'][0]:.1f} to {res['pin_load_cp_pf_any_length'][1]:.1f} pF.",
         f"- 3f at the GVA-84+ input, worst over every length: {res['h3_dbc_worst_any_length']:.1f} dBc.",
         f"- Numerical check: 15 corners at 10 ps and 400 ns against d6 at 20 ps and 250 ns: {res['timestep_check']['max_diff_pin_db']:.4f} dB power, "
         f"{res['timestep_check']['max_diff_h3_db']:.3f} dB 3f (criteria 0.02 and 0.5 dB).", "",
         "Plot `coax_length_bound_bpf.png`; steps in `coax_a5_bpf_steps.json`; decks `coax_a5_bpf.cir`, `tstep_a5_bpf.cir`.", ""]
    (out / "result.md").write_text("\n".join(L))
    copy_inputs(out, [deck, deck10])
    res["kept_raw"] = raw_manifest(out)
    (out / "result.json").write_text(json.dumps(res, indent=1, default=float))
    print("d7", json.dumps({k: res[k] for k in ("max_mw_any_length", "min_mw_any_length", "pad_needed_any_length_db",
                                                 "freq_span_within_unit_any_length_db", "timestep_check")}, default=str)[:800])
    return res


# ---------------------------------------------------------------- k1: the select-on-test level reading at about 17 mW
# Method (proposed here for REQ-SYS-144 and TS-012 D-7; 04 section 6.2 probe): the module is replaced by a 50 ohm load
# (1 %) at the RA07M1317M input pad; a 1N5711-class diode probe (series diode, 10 nF hold capacitor) across it is read on
# the owner's Fluke 174 (DC volts +/-(0.15 % + 2 counts), status note 2026-09-28 section 2; input resistance 10 Mohm,
# est., the 170-series nominal, not read: the method cancels it because the same meter is the DC load below).
# Forward-drop characterization (bench supply, the same probe and the same meter, the same day and temperature):
# (1) supply through the diode into the Fluke alone, set so the Fluke reads the RF reading's value: Vf1 = Vs - Vout at
# I1 = Vout / Rm; (2) the same with a 1.00 Mohm 1 % resistor across the Fluke: Vf2 at I2 = 11 I1; the ideality n and
# Is from the two points of I = Is (exp(Vf / n Vt) - 1) (n_from_two; the simple (Vf2 - Vf1) / (Vt ln 11) is wrong here
# because I1 is only a few times Is). Reading equation (ideal-diode peak detector in periodic steady state, the average
# diode current equal to the DC load current at both the RF and the DC point): I0(Vpk / n Vt) = exp((Vdc + Vf1) / n Vt),
# solved for Vpk; P = Vpk^2 / (2 x 50). Revision 2's "forward drop measured at DC" alone (Vpk = Vdc + Vf1) leaves the
# conduction term n Vt ln(I0(x) e^-x) out, about 80 mV at 1.3 V peak (checked below as method M0).
# Even-harmonic content (GVA-84+ 2f, Si5351 2f at duty 0.45) moves the positive peak by up to +/- its relative amplitude;
# the probe is read in both polarities (diode reversed) and the two peaks averaged (method M2), which cancels it to
# first order. Odd harmonics are not cancelled.
# Diode: the HSMS-280x SPICE parameters the keying deck uses for the 1N5711W (IS 3e-8, N 1.08, RS 30, CJO 1.6p;
# surrogate, est.) and single-parameter excursions around them.
K1_RM = 10e6
K1_R2 = 1.0e6
K1_RLOAD = 50.0
K1_SETS = [  # (label, Is, N, Rs, Cjo pF)
    ("S0 HSMS-280x surrogate", 3e-8, 1.08, 30.0, 1.6),
    ("S1 Is / 10", 3e-9, 1.08, 30.0, 1.6),
    ("S2 Is x 10", 3e-7, 1.08, 30.0, 1.6),
    ("S3 N 1.00", 3e-8, 1.00, 30.0, 1.6),
    ("S4 N 1.15", 3e-8, 1.15, 30.0, 1.6),
    ("S5 Rs 10 ohm", 3e-8, 1.08, 10.0, 1.6),
    ("S6 Rs 50 ohm", 3e-8, 1.08, 50.0, 1.6),
    ("S7 Cjo 2.2 pF", 3e-8, 1.08, 30.0, 2.2),
]
K1_PMW = [10.0, 17.3, 30.0]            # true fundamental power into 50 ohm without the probe
K1_HARM = [  # (label, harmonic, dBc, phase deg): bounds, est. (d6 3f at the GVA input at most -34 dBc; GVA-84+ 2f est.
             # from OIP3 +35.8 dBm, Rev. F: about -37 dBc at +15 dBm; Si5351 2f at duty 0.45 after the bandpass about -39 dBc)
    ("none", 2, -200.0, 0.0),
    ("2f -30 dBc, 0 deg", 2, -30.0, 0.0),
    ("2f -30 dBc, 180 deg", 2, -30.0, 180.0),
    ("3f -30 dBc, 0 deg", 3, -30.0, 0.0),
    ("3f -30 dBc, 180 deg", 3, -30.0, 180.0),
]
K1_POL = [1, -1]
K1_D = [round(0.02 + 0.01 * k, 3) for k in range(39)]   # hold voltage below the load-node peak, grid (V)
K1_F = 146e6
K1_TDC = [20.0, 25.0, 30.0]            # DC characterization at the RF reading's temperature (25 C) and +/-5 K
K1_C_LEAD_PF = 1.0                     # probe tip and housing at the load node (est.)
K1_FLUKE_GAIN, K1_FLUKE_COUNT = 0.0015, 0.002   # +/-(0.15 % + 2 counts) on the 6 V range (1 mV count)
K1_RLOAD_TOL = 0.01


def k1_cases():
    out = []
    for iset, s in enumerate(K1_SETS):
        for ip, pmw in enumerate(K1_PMW):
            for ih, h in enumerate(K1_HARM):
                for ipol, pol in enumerate(K1_POL):
                    for idd, d in enumerate(K1_D):
                        out.append(dict(iset=iset, pmw=pmw, harm=h[0], pol=pol, d=d))
    return out


def deck_k1(out: Path) -> tuple[Path, Path, list[dict]]:
    cs = k1_cases()
    dims = [("idd", len(K1_D)), ("ipol", 2), ("ih", len(K1_HARM)), ("ip", len(K1_PMW)), ("iset", len(K1_SETS))]
    lines, n = P.radix_lines(dims)
    assert n == len(cs)
    def tab(name, idx, vals):
        return f".param {name}=table({idx}," + ",".join(f"{i},{v:.6g}" for i, v in enumerate(vals)) + ")"
    T = 1 / K1_F
    t_end = 30 * T
    txt = f"""* probe_rf.cir: the select-on-test level reading, RF part (cwht WP-PDR-21 revision 3, run_a5_r3.py k1)
* A {K1_F / 1e6:g} MHz source behind 50 ohm (the 3 dB pad and GVA-84+ output, 50 ohm) into the 50 ohm load that replaces
* the RA07M1317M; fundamental amplitude at the load a1 = sqrt(2 x 50 x P) without the probe; one harmonic of relative
* amplitude hr at phase ph (0: its peak on the fundamental's peak); polarity pol (the probe diode reversed is the source negated). The probe: {K1_C_LEAD_PF:g} pF
* tip and housing at the load node (est.), a series diode, then the 10 nF hold capacitor's path (0.1 ohm, 1 nH, est.)
* to the hold voltage Vh, held as an ideal DC source (10 nF is 0.11 ohm at {K1_F / 1e6:g} MHz and its voltage does not
* move within the window). The checker finds, for each case, the Vh at which the average diode current equals the
* meter's DC current Vh / {K1_RM / 1e6:g} Mohm (the periodic steady state of the real probe), from a grid of Vh
* below the load peak a1 (step d); average over the last 4 of 30 carrier periods.
* {n} steps, idx = d grid fastest, then polarity, harmonic case, power, diode set.
.param idx=0
.step param idx 0 {n - 1} 1
{chr(10).join(lines)}
{tab('dd', 'idd', K1_D)}
{tab('pol', 'ipol', K1_POL)}
{tab('hn', 'ih', [h[1] for h in K1_HARM])}
{tab('hr', 'ih', [10 ** (h[2] / 20) for h in K1_HARM])}
{tab('ph', 'ih', [h[3] for h in K1_HARM])}
{tab('pw', 'ip', [p * 1e-3 for p in K1_PMW])}
{tab('dis', 'iset', [s[1] for s in K1_SETS])}
{tab('dn', 'iset', [s[2] for s in K1_SETS])}
{tab('drs', 'iset', [s[3] for s in K1_SETS])}
{tab('dcj', 'iset', [s[4] * 1e-12 for s in K1_SETS])}
.param a1=sqrt(2*{K1_RLOAD:g}*pw)
.param vh=a1-dd
B1 src 0 V=pol*2*a1*(cos(2*pi*{K1_F:.0f}*time)+hr*cos(hn*2*pi*{K1_F:.0f}*time+ph*pi/180))
Rs src load 50
Rl load 0 {K1_RLOAD:g}
Clead load 0 {K1_C_LEAD_PF:g}p
D1 load hold DPROBE
Rh hold hx 0.1
Lh hx hy 1n
Vh hy 0 {{vh}}
.model DPROBE D(Is={{dis}} N={{dn}} Rs={{drs}} Cjo={{dcj}} Vj=0.65 M=0.5 Eg=0.69 Xti=2 BV=75 Ibv=1e-5)
.options method=gear
.tran 0 {t_end * 1e9:.4f}n {26 * T * 1e9:.4f}n 25p
.save I(D1)
.end
"""
    prf = out / "probe_rf.cir"
    prf.write_text(txt)
    # DC part: forward drop against current, every diode set, at the three characterization temperatures
    dtx = f"""* probe_dc.cir: the select-on-test level reading, DC forward-drop part (cwht WP-PDR-21 revision 3, run_a5_r3.py k1)
* A current source through the probe diode (series resistance included) from 1 nA to 10 uA; V(a) is the forward drop.
* Steps: diode set (iset), temperature.
.param iset=0
.step param iset 0 {len(K1_SETS) - 1} 1
.step temp list {' '.join(f'{t:g}' for t in K1_TDC)}
{tab('dis', 'iset', [s[1] for s in K1_SETS])}
{tab('dn', 'iset', [s[2] for s in K1_SETS])}
{tab('drs', 'iset', [s[3] for s in K1_SETS])}
{tab('dcj', 'iset', [s[4] * 1e-12 for s in K1_SETS])}
I1 0 a 1n
D1 a 0 DPROBE
.model DPROBE D(Is={{dis}} N={{dn}} Rs={{drs}} Cjo={{dcj}} Vj=0.65 M=0.5 Eg=0.69 Xti=2 BV=75 Ibv=1e-5)
.dc dec I1 1n 10u 400
.save V(a)
.end
"""
    pdc = out / "probe_dc.cir"
    pdc.write_text(dtx)
    return prf, pdc, cs


def n_from_two(vf1: float, i1: float, vf2: float, i2: float, t_c: float) -> float:
    """Ideality n of I = Is (exp(Vf / n Vt) - 1) through the two DC points (Is eliminated; exact, because at the
    probe's current of about 0.12 uA the diode is not far above Is and the '-1' term matters)."""
    from scipy.optimize import brentq
    vt = 1.380649e-23 * (t_c + 273.15) / 1.602176634e-19
    def f(n):
        isat = i1 / np.expm1(vf1 / (n * vt))
        return isat * np.expm1(vf2 / (n * vt)) - i2
    return float(brentq(f, 0.5, 3.0))


def _vpk_from_reading(vdc: float, vf1: float, n: float, t_c: float = 25.0) -> float:
    """Solve I0(Vpk / n Vt) = exp((Vdc + Vf1) / n Vt) for Vpk (ideal-diode peak detector, exact form)."""
    from scipy.optimize import brentq
    from scipy.special import i0e
    vt = 1.380649e-23 * (t_c + 273.15) / 1.602176634e-19
    y = (vdc + vf1) / (n * vt)
    fx = lambda x: np.log(i0e(x)) + x - y
    x = brentq(fx, 1e-6, y + 50)
    return float(x * n * vt)


def run_k1():
    out = rundir("k1")
    prf, pdc, cs = deck_k1(out)
    prov_rf = P.run_ltspice(prf, out, timeout=7200)
    prov_dc = P.run_ltspice(pdc, out, timeout=600)
    from spicelib import RawRead
    raw = RawRead(str(out / "probe_rf.raw"))
    nst = len(raw.get_steps())
    verdict("k1", "check: one .raw step per RF case", nst == len(cs), "check", f"{nst} steps")
    T = 1 / K1_F
    iavg = []
    for i in range(nst):
        t = np.abs(raw.get_trace(raw.get_trace_names()[0]).get_wave(i))
        idd = raw.get_trace("I(D1)").get_wave(i)
        m = t >= t[-1] - 4 * T
        tt = np.linspace(t[-1] - 4 * T, t[-1], 4 * 2048, endpoint=False)
        iavg.append(float(np.mean(np.interp(tt, t[m], idd[m]))))
    iavg = np.array(iavg)
    # DC: forward drop against current per set and temperature
    rdc = RawRead(str(out / "probe_dc.raw"))
    idc_axis = np.abs(rdc.get_trace(rdc.get_trace_names()[0]).get_wave(0))
    vf = {}
    # LTspice orders nested .step with the first .step fastest: iset fastest, then temp
    for it, tc in enumerate(K1_TDC):
        for iset in range(len(K1_SETS)):
            vf[(iset, tc)] = np.array(rdc.get_trace("V(a)").get_wave(it * len(K1_SETS) + iset))
    verdict("k1", "check: one DC sweep per diode set and temperature", len(rdc.get_steps()) == len(K1_SETS) * len(K1_TDC), "check")

    def vf_at(iset, tc, i):
        return float(np.interp(np.log(i), np.log(idc_axis), vf[(iset, tc)]))

    # equilibrium hold voltage per case (log-linear interpolation of the average current across the d grid)
    groups = {}
    for c, ia in zip(cs, iavg):
        groups.setdefault((c["iset"], c["pmw"], c["harm"], c["pol"]), []).append((c, ia))
    eq = {}
    bad = 0
    n_extrap = 0
    for key, lst in groups.items():
        a1 = np.sqrt(2 * K1_RLOAD * key[1] * 1e-3)
        vh = np.array([a1 - c["d"] for c, _ in lst])
        ia = np.array([x for _, x in lst])
        g = np.log(np.maximum(ia, 1e-18)) - np.log(vh / K1_RM)
        o = np.argsort(vh)
        vh, g, ia = vh[o], g[o], ia[o]
        f = ia - vh / K1_RM
        j = np.where((f[:-1] > 0) & (f[1:] <= 0))[0]
        if len(j) != 1 or ia[j[0]] <= 0:
            bad += 1
            continue
        j = int(j[0])
        if ia[j + 1] > 0:     # log-linear between the bracketing points (the average current is near-exponential in Vh)
            v = vh[j] + (vh[j + 1] - vh[j]) * g[j] / (g[j] - g[j + 1])
        else:                 # the upper point has a reverse average current: extrapolate the log-linear law of the two
            j0 = j - 1        # points below the root
            sl = (np.log(ia[j]) - np.log(ia[j0])) / (vh[j] - vh[j0])
            from scipy.optimize import brentq
            v = brentq(lambda x: np.log(ia[j]) + sl * (x - vh[j]) - np.log(x / K1_RM), vh[j], vh[j + 1])
            n_extrap += 1
        eq[key] = float(v)
    verdict("k1", "check: one bracketed equilibrium per RF case", bad == 0, "check",
            f"{bad} unbracketed of {len(groups)}; {n_extrap} by the log-linear law of the two grid points below the root")
    vt = lambda tc: 1.380649e-23 * (tc + 273.15) / 1.602176634e-19
    rows = []
    for (iset, pmw, harm, pol), vdc in eq.items():
        if pol != 1:
            continue
        vdc_n = eq.get((iset, pmw, harm, -1))
        for tdc in K1_TDC:
            r = {"set": K1_SETS[iset][0], "iset": iset, "p_true_mw": pmw, "harm": harm, "t_dc_c": tdc, "vdc": vdc,
                 "vdc_neg": vdc_n}
            res_m = {}
            for tag, v in (("pos", vdc), ("neg", vdc_n)):
                i1 = v / K1_RM
                i2 = v / (K1_RM * K1_R2 / (K1_RM + K1_R2))
                vf1, vf2 = vf_at(iset, tdc, i1), vf_at(iset, tdc, i2)
                n_est = n_from_two(vf1, i1, vf2, i2, 25.0)   # only n Vt enters: a fixed Vt is exact
                vp1 = _vpk_from_reading(v, vf1, n_est, 25.0)
                res_m[tag] = {"vf1": vf1, "n_est": n_est, "vp_m0": v + vf1, "vp_m1": vp1}
            ptrue = pmw * 1e-3
            db = lambda vp: float(10 * np.log10(vp ** 2 / (2 * K1_RLOAD) / ptrue))
            r.update({"vf1": res_m["pos"]["vf1"], "n_est": res_m["pos"]["n_est"],
                      "err_m0_db": db(res_m["pos"]["vp_m0"]), "err_m1_db": db(res_m["pos"]["vp_m1"]),
                      "err_m2_db": db(0.5 * (res_m["pos"]["vp_m1"] + res_m["neg"]["vp_m1"]))})
            # meter term on the M1/M2 estimate: gain on the supply reading plus 3 x 2 counts (Vdc, Vs, Vout), and
            # the n term: +/-2 counts on each of the two DC readings that set Vf2 - Vf1
            vp = res_m["pos"]["vp_m1"]
            e_m = K1_FLUKE_GAIN * (vdc + res_m["pos"]["vf1"]) + 3 * K1_FLUKE_COUNT
            r["meter_db"] = float(20 * np.log10(1 + e_m / vp))
            n0 = res_m["pos"]["n_est"]
            i1p = vdc / K1_RM
            i2p = vdc / (K1_RM * K1_R2 / (K1_RM + K1_R2))
            vf1p = res_m["pos"]["vf1"]
            vf2p = vf_at(iset, tdc, i2p)
            n_hi = n_from_two(vf1p, i1p, vf2p + 2 * K1_FLUKE_COUNT, i2p, 25.0)   # Vf2 - Vf1 read 2 x 2 counts high
            vp_hi = _vpk_from_reading(vdc, vf1p, n_hi, 25.0)
            r["n_term_db"] = float(abs(20 * np.log10(vp_hi / vp)))
            rows.append(r)
    ld_db = float(10 * np.log10(1 + K1_RLOAD_TOL))   # 1 % load: about half the resistance change in the voltage, x2 in power
    at_t = [r for r in rows if r["t_dc_c"] == 25.0]
    def rng(key, sel):
        v = [r[key] for r in sel]
        return [float(min(v)), float(max(v))]
    no_even = [r for r in rows if not r["harm"].startswith("2f")]
    res = {"run": RUNS3["k1"], "revision": REVISION, "ltspice": prov_rf, "dc": {"ltspice": prov_dc}, "n_rf_steps": nst,
           "sets": [s[0] for s in K1_SETS], "p_mw": K1_PMW, "harmonic_cases": [h[0] for h in K1_HARM],
           "t_dc_c": K1_TDC, "rows": rows,
           "err_db": {
               "m0_dc_drop_only_25c_no_harm": rng("err_m0_db", [r for r in at_t if r["harm"] == "none"]),
               "m1_25c_no_harm": rng("err_m1_db", [r for r in at_t if r["harm"] == "none"]),
               "m1_all": rng("err_m1_db", rows),
               "m2_all": rng("err_m2_db", rows),
               "m2_25c": rng("err_m2_db", at_t),
               "m1_all_no_even_harm": rng("err_m1_db", no_even)},
           "meter_db_max": float(max(r["meter_db"] for r in rows)), "n_term_db_max": float(max(r["n_term_db"] for r in rows)),
           "load_db": ld_db}
    e = res["err_db"]["m2_all"]
    res["reading_bound_db"] = float(max(abs(e[0]), abs(e[1])) + res["meter_db_max"] + res["n_term_db_max"] + ld_db)
    e1 = res["err_db"]["m1_all"]
    res["reading_bound_m1_db"] = float(max(abs(e1[0]), abs(e1[1])) + res["meter_db_max"] + res["n_term_db_max"] + ld_db)
    verdict("k1", "A5 select-on-test reading (method M2, both polarities) within the +/-1.0 dB allocation (worst-case sum)",
            res["reading_bound_db"] <= 1.0, detail=f"+/-{res['reading_bound_db']:.2f} dB")
    verdict("k1", "Revision 2 reading (forward drop at DC only, M0) within +/-1.0 dB at 25 C with no harmonic",
            max(abs(x) for x in res["err_db"]["m0_dc_drop_only_25c_no_harm"]) <= 1.0,
            detail=f"{res['err_db']['m0_dc_drop_only_25c_no_harm'][0]:+.2f} to {res['err_db']['m0_dc_drop_only_25c_no_harm'][1]:+.2f} dB")
    res["verdicts"] = VERDICTS.get("k1", {})
    plot_k1(out, res)
    (out / "result.json").write_text(json.dumps(res, indent=1, default=float))
    write_k1_md(out, res)
    copy_inputs(out, [prf, pdc])
    res["kept_raw"] = raw_manifest(out)
    (out / "result.json").write_text(json.dumps(res, indent=1, default=float))
    print("k1", json.dumps({k: res[k] for k in ("err_db", "meter_db_max", "n_term_db_max", "load_db", "reading_bound_db",
                                                 "reading_bound_m1_db")}, default=float))
    return res


def plot_k1(out: Path, res: dict):
    rows = res["rows"]
    fig, axs = plt.subplots(1, 2, figsize=(11.8, 5.0))
    ax = axs[0]
    hc = {"none": INK2, "2f -30 dBc, 0 deg": COL["a4"], "2f -30 dBc, 180 deg": "#b3401a",
          "3f -30 dBc, 0 deg": COL["a5"], "3f -30 dBc, 180 deg": COL["aux"]}
    xs = {s: i for i, s in enumerate(res["sets"])}
    for r in rows:
        if r["t_dc_c"] != 25.0 or abs(r["p_true_mw"] - 17.3) > 1e-9:
            continue
        x = xs[r["set"]]
        off = {"none": -0.24, "2f -30 dBc, 0 deg": -0.12, "2f -30 dBc, 180 deg": 0.0, "3f -30 dBc, 0 deg": 0.12,
               "3f -30 dBc, 180 deg": 0.24}[r["harm"]]
        ax.scatter(x + off, r["err_m0_db"], marker="x", s=18, color=hc[r["harm"]])
        ax.scatter(x + off, r["err_m1_db"], marker="o", s=14, facecolors="none", edgecolors=hc[r["harm"]])
        ax.scatter(x + off, r["err_m2_db"], marker="o", s=14, color=hc[r["harm"]])
    for h, c in hc.items():
        ax.scatter([], [], s=14, color=c, label=h)
    ax.scatter([], [], marker="x", color=INK, label="M0: forward drop at DC only (revision 2)")
    ax.scatter([], [], marker="o", facecolors="none", edgecolors=INK, label="M1: with the conduction term")
    ax.scatter([], [], marker="o", color=INK, label="M2: M1, both polarities averaged")
    ax.axhspan(-1, 1, color=COL["ok"], alpha=0.08)
    ax.axhline(0, color=GRID, lw=1)
    ax.set_xticks(range(len(res["sets"])))
    ax.set_xticklabels([s.split(" ", 1)[1] if " " in s else s for s in res["sets"]], rotation=35, ha="right", fontsize=7)
    ax.set_ylabel("Reading error at 17.3 mW (dB, read minus true)")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.30), ncol=2, fontsize=6.5)
    ax.set_title("k1: probe reading error at 17.3 mW, 146 MHz, per diode set\n"
                 "(DC characterization at the reading temperature; green: the +/-1.0 dB allocation)", fontsize=9)
    ax = axs[1]
    terms = [("M2 residual, worst of every case", max(abs(x) for x in res["err_db"]["m2_all"])),
             ("Fluke 174: 0.15 % + 3 x 2 counts", res["meter_db_max"]), ("ideality n from two DC readings", res["n_term_db_max"]),
             ("50 ohm load, 1 %", res["load_db"])]
    b = 0
    for i, (lab, v) in enumerate(terms):
        ax.barh(0, v, left=b, color=[COL["a5"], COL["aux"], COL["a4"], INK2][i], label=f"{lab}: {v:.2f} dB")
        b += v
    ax.axvline(1.0, color=INK, lw=1.3, label="+/-1.0 dB: reading allocation of revision 2")
    ax.axvline(res.get("break_even_db", 1.54), color=INK, lw=1.0, ls="--", label="break-even of revision 2 (+/-1.54 dB)")
    ax.set_xlim(0, 1.8)
    ax.set_yticks([])
    ax.set_xlabel("Reading uncertainty, worst-case sum (+/- dB)")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.18), fontsize=7)
    ax.set_title(f"Method M2 reading bound: +/-{res['reading_bound_db']:.2f} dB (estimate)", fontsize=9)
    fig.tight_layout()
    fig.savefig(out / "probe_reading_error.png", dpi=150)
    plt.close(fig)


def write_k1_md(out: Path, r: dict):
    e = r["err_db"]
    L = [f"# {r['run']}: the select-on-test level reading at about 17 mW (revision 3)", "",
         "Diode probe across the 50 ohm load that replaces the module, read on the Fluke 174; forward drop measured at DC "
         "at the meter's own current and at 11 times it (1.00 Mohm across the meter). LTspice: RF periodic steady state "
         f"({r['n_rf_steps']} steps) and DC forward drop; the checker solves the equilibrium hold voltage and applies the "
         "reading equations. All figures are estimates (surrogate diode model).", "",
         "| Quantity | Range (dB, read minus true) |", "|---|---|",
         f"| M0 (revision 2: Vpk = Vdc + Vf at DC), 25 C, no harmonic | {e['m0_dc_drop_only_25c_no_harm'][0]:+.3f} to {e['m0_dc_drop_only_25c_no_harm'][1]:+.3f} |",
         f"| M1 (with the conduction term), 25 C, no harmonic | {e['m1_25c_no_harm'][0]:+.3f} to {e['m1_25c_no_harm'][1]:+.3f} |",
         f"| M1, every case (harmonics, DC at +/-5 K) | {e['m1_all'][0]:+.3f} to {e['m1_all'][1]:+.3f} |",
         f"| M1, every case without the 2f cases | {e['m1_all_no_even_harm'][0]:+.3f} to {e['m1_all_no_even_harm'][1]:+.3f} |",
         f"| M2 (M1 in both polarities, averaged), every case | {e['m2_all'][0]:+.3f} to {e['m2_all'][1]:+.3f} |", "",
         f"Terms added in the worst direction: Fluke 174 {r['meter_db_max']:.3f} dB; ideality from the two DC readings "
         f"{r['n_term_db_max']:.3f} dB; 1 % load {r['load_db']:.3f} dB.", "",
         f"**Reading bound, method M2: +/-{r['reading_bound_db']:.2f} dB** (M1: +/-{r['reading_bound_m1_db']:.2f} dB), "
         "against the +/-1.0 dB allocation of revision 2.", "",
         "Plot `probe_reading_error.png`; every case in `result.json` (`rows`); decks `probe_rf.cir`, `probe_dc.cir`.", ""]
    (out / "result.md").write_text("\n".join(L))


# ---------------------------------------------------------------- s2: select-on-test pad for the bandpass chain
SOT_DRIFT_DB = P.SOT_DRIFT_DB   # 0.3 dB (revision 2 breakdown); the bandpass drift is added below from d6
TCL_MAX_PPM = 70.0              # 1812SMS temperature coefficient of inductance +5 to +70 ppm/C (Document 184-1, D)
BAY_AIR_C = (-10.0, 89.0)       # PA-bay air range at the drive chain (revision 2 section 3.1; WP-PDR-28 revision 0)


def run_s2():
    out = rundir("s2")
    rows = json.loads((rundir("d6") / "corners.json").read_text())
    k1 = json.loads((rundir("k1") / "result.json").read_text())
    d7 = json.loads((rundir("d7") / "result.json").read_text())
    pad18 = float(P.pad_loss_db(*P.PADS["a5_in"]))
    tgt = float(P.dbm(P.SOT_TARGET_MW * 1e-3))
    units = {}
    for r in rows:
        units.setdefault((r["rsrc"], r["gain"], r["p1db"], r["src"], r["coax_m"], r["bpf"], r["qbpf"]), {})[r["freq"]] = r["pin_pa_dbm"]
    fspan = max(max(v.values()) - min(v.values()) for v in units.values())
    need = [pad18 + (v[146e6] - tgt) for v in units.values()]
    pads = P.e24_pad_set(min(need), max(need))
    gaps = np.diff([q["loss_db"] for q in pads])
    step_half = float(gaps.max() / 2)
    # bandpass drift in service: the coil's TCL (at most +70 ppm/C) over the bay-air range moves L by up to
    # 70e-6 x 64 K = 0.45 % (C0G about 0); d6 gives the drive change for a joint 2 % L and C move (the "high" and "low"
    # cases, resonance moved 2 %); an L-only 0.45 % move shifts the resonance 0.22 %, 0.11 of that; per part corner
    dl = TCL_MAX_PPM * 1e-6 * max(BAY_AIR_C[1] - 25.0, 25.0 - BAY_AIR_C[0])
    sens = []
    idx = {(r["rsrc"], r["gain"], r["p1db"], r["src"], r["coax_m"], r["freq"], r["bpf"], r["qbpf"]): r["pin_pa_dbm"] for r in rows}
    for (rs, g, p1, sc, cx, b, q), v in units.items():
        if b != "nom":
            continue
        for f in P.FREQS:
            base = idx[(rs, g, p1, sc, cx, f, "nom", q)]
            for bb in ("low", "high"):
                sens.append(abs(idx[(rs, g, p1, sc, cx, f, bb, q)] - base))
    bpf_drift = float(max(sens) * (dl / 2) / 0.02)
    drift = SOT_DRIFT_DB + bpf_drift
    meas = float(k1["reading_bound_db"])
    def band(m):
        half = fspan / 2 + step_half + m + drift
        mx, mn = P.SOT_TARGET_MW * 10 ** (half / 10), P.SOT_TARGET_MW * 10 ** (-half / 10)
        return {"meas_db": m, "half_width_db": half, "min_mw": mn, "max_mw": mx,
                "overdrive_margin_db": float(10 * np.log10(30.0 / mx)), "underdrive_margin_db": float(10 * np.log10(mn / 10.0)),
                "pass": bool(mn >= 10.0 and mx <= 30.0)}
    b = band(meas)
    b_alloc = band(P.SOT_MEAS_DB)
    avail = float(10 * np.log10(30.0 / P.SOT_TARGET_MW))
    rss = float(np.sqrt((fspan / 2) ** 2 + step_half ** 2 + meas ** 2 + drift ** 2))
    res = {"run": RUNS3["s2"], "revision": REVISION, "drive_run": RUNS3["d6"], "reading_run": RUNS3["k1"],
           "n_units": len(units), "freq_span_within_unit_db": fspan, "pad_as_built_db": pad18,
           "pad_needed_db": [float(min(need)), float(max(need))], "pad_needed_any_length_db": d7["pad_needed_any_length_db"],
           "pads": pads, "pad_set_max_gap_db": float(gaps.max()), "step_half_db": step_half,
           "drift_db": drift, "drift_parts_db": {"revision 2 terms": SOT_DRIFT_DB, "bandpass TCL": bpf_drift},
           "reading_db": meas, "band": b, "band_at_allocation": b_alloc, "half_width_rss_db": rss,
           "overdrive_margin_rss_db": avail - rss, "reading_break_even_db": float(avail - (fspan / 2 + step_half + drift)),
           "sensitivity": [band(m) for m in (0.25, 0.5, meas, 1.0, 1.5, 2.0)],
           "revision2": {"pads": 14, "range_db": [13.48, 22.04], "band_mw": [11.3, 26.5], "overdrive_margin_db": 0.54}}
    verdict("s2", "A5 select-on-test drive 10 to 30 mW in service with the k1 reading bound (bandpass chain)", b["pass"],
            detail=f"{b['min_mw']:.1f} to {b['max_mw']:.1f} mW, overdrive margin {b['overdrive_margin_db']:+.2f} dB, reading +/-{meas:.2f} dB")
    verdict("s2", "A5 select-on-test drive 10 to 30 mW at the +/-1.0 dB reading allocation (bandpass chain)", b_alloc["pass"],
            detail=f"{b_alloc['min_mw']:.1f} to {b_alloc['max_mw']:.1f} mW")
    verdict("s2", "A5 select-on-test drive 10 to 30 mW with a tinySA Ultra reading alone (+/-2 dB published)",
            band(2.0)["pass"], detail=f"overdrive margin {band(2.0)['overdrive_margin_db']:+.2f} dB")
    res["verdicts"] = VERDICTS.get("s2", {})
    # plot: in-service band against the reading uncertainty
    fig, axs = plt.subplots(1, 2, figsize=(11.5, 4.8))
    ax = axs[0]
    ms = np.linspace(0, 2.2, 45)
    bs = [band(m) for m in ms]
    ax.fill_between(ms, [x["min_mw"] for x in bs], [x["max_mw"] for x in bs], color=COL["a5"], alpha=0.25,
                    label="in-service drive band, worst-case sum")
    ax.axhline(30, color=INK, lw=1.3, label="30 mW: module maximum rating")
    ax.axhline(10, color=INK, lw=1.3, ls="--", label="10 mW: bottom of the stability window")
    ax.axvline(meas, color=COL["ok"], lw=1.6, label=f"k1 reading bound, method M2: +/-{meas:.2f} dB")
    ax.axvline(1.0, color=INK2, lw=1.0, ls=":", label="revision 2 allocation +/-1.0 dB")
    ax.axvline(2.0, color=COL["a4"], lw=1.0, ls="-.", label="tinySA Ultra alone, +/-2 dB published")
    ax.axvline(res["reading_break_even_db"], color=INK, lw=0.9, ls=(0, (1, 1)), label=f"break-even +/-{res['reading_break_even_db']:.2f} dB")
    ax.set_yscale("log")
    from matplotlib.ticker import FixedLocator, NullLocator, ScalarFormatter
    ax.set_ylim(6, 50)
    ax.yaxis.set_major_locator(FixedLocator([6, 8, 10, 15, 20, 30, 40, 50]))
    ax.yaxis.set_minor_locator(NullLocator())
    ax.yaxis.set_major_formatter(ScalarFormatter())
    ax.set_xlim(0, 2.2)
    ax.set_xlabel("Level-reading uncertainty at about 17 mW (+/- dB)")
    ax.set_ylabel("Module input in service (mW)")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.16), ncol=2, fontsize=6.8)
    ax.set_title("s2: select-on-test drive band (bandpass chain) against the reading uncertainty", fontsize=9)
    ax = axs[1]
    terms = [("frequency, half the in-unit span", fspan / 2), ("half the pad set's largest gap", step_half),
             ("level reading (k1, M2)", meas), ("drift in service", drift)]
    left = 0
    for i, (lab, v) in enumerate(terms):
        ax.barh(0, v, left=left, color=[INK2, COL["aux"], COL["ok"], COL["a4"]][i], label=f"{lab}: {v:.2f} dB")
        left += v
    ax.axvline(avail, color=INK, lw=1.3, label=f"available to 30 mW from 17.3 mW: {avail:.2f} dB")
    ax.set_yticks([])
    ax.set_xlim(0, 3.0)
    ax.set_xlabel("Half-width of the in-service band (dB)")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.16), fontsize=7)
    ax.set_title(f"Band half-width {b['half_width_db']:.2f} dB (worst-case sum), {rss:.2f} dB (RSS)", fontsize=9)
    fig.tight_layout()
    fig.savefig(out / "sot_band.png", dpi=150)
    plt.close(fig)
    (out / "result.json").write_text(json.dumps(res, indent=1, default=float))
    L = [f"# {res['run']}: select-on-test pad for the D-13 bandpass chain (revision 3)", "",
         f"Units: {len(units)} (source R, GVA gain, P1dB set, Si5351 case, coax 5 to 15 cm, bandpass case, coil Q). "
         "The pad is chosen at build at 146 MHz for 17.3 mW, with the unit's own coax in place; in service only frequency, "
         "the pad step, the reading and drift remain.", "",
         "| Term | dB |", "|---|---|",
         f"| Frequency span within a unit (144 to 148 MHz), half | {fspan / 2:.3f} |",
         f"| Half the pad set's largest gap | {step_half:.3f} |",
         f"| Level reading, k1 method M2 bound | {meas:.3f} |",
         f"| Drift: revision 2 terms {SOT_DRIFT_DB} dB plus the bandpass coil TCL {bpf_drift:.3f} dB | {drift:.3f} |",
         f"| **Half-width, worst-case sum (RSS)** | **{b['half_width_db']:.3f} ({rss:.3f})** |", "",
         f"In-service drive {b['min_mw']:.1f} to {b['max_mw']:.1f} mW: overdrive margin {b['overdrive_margin_db']:+.2f} dB "
         f"({avail - rss:+.2f} dB RSS), margin above 10 mW {b['underdrive_margin_db']:+.2f} dB: **{'PASS' if b['pass'] else 'FAIL'}**. "
         f"At the +/-1.0 dB allocation: {b_alloc['min_mw']:.1f} to {b_alloc['max_mw']:.1f} mW. Break-even reading "
         f"+/-{res['reading_break_even_db']:.2f} dB.", "",
         f"Pad losses the units need: {min(need):.2f} to {max(need):.2f} dB (coax 5 to 15 cm); "
         f"{d7['pad_needed_any_length_db'][0]:.2f} to {d7['pad_needed_any_length_db'][1]:.2f} dB at any coax length (d7).", "",
         f"Pad set ({len(pads)} E24 1 % pi pads, largest gap {gaps.max():.2f} dB):", "", "| Loss (dB) | Shunt, series, shunt (ohm) | Return loss (dB) |", "|---|---|---|"]
    for q in pads:
        L.append(f"| {q['loss_db']:.2f} | {q['shunt']:g}, {q['series']:g}, {q['shunt']:g} | {q['rl_db']:.1f} |")
    L += ["", "| Reading uncertainty (dB) | Band (mW) | Overdrive margin (dB) | Verdict |", "|---|---|---|---|"]
    for x in res["sensitivity"]:
        L.append(f"| +/-{x['meas_db']:.2f} | {x['min_mw']:.1f} to {x['max_mw']:.1f} | {x['overdrive_margin_db']:+.2f} | {'PASS' if x['pass'] else 'FAIL'} |")
    L += ["", "Plot `sot_band.png`.", ""]
    (out / "result.md").write_text("\n".join(L))
    copy_inputs(out, [])
    print("s2", json.dumps({k: res[k] for k in ("freq_span_within_unit_db", "step_half_db", "drift_db", "reading_db",
                                                 "band", "pad_needed_db", "reading_break_even_db")}, default=float))
    return res


# ---------------------------------------------------------------- p4: power at the SMA with the adopted A5 design
# Drain feed from the datasheet reads (C2; revision 2 carried estimates). Per part at 25 C: (low, high) ohm, temperature
# coefficient below and above 25 C (per K), key-down rise (low, high) K, source.
#   cells, two Molicel P28A: 0.04 (DC IR 20 mohm each, D) to 0.06 (est.); ambient multipliers as revision 2 (G).
#   AO3400A pair: 0.038 (typ 19 mohm at VGS 4.5 V, Fig. 3, G) to 0.064 (32 mohm max at VGS 4.5 V, D; Rev 3.1 July 2023,
#     SHA-256 9c60d0b6...); +0.56 %/K (Fig. 4, normalized 1.70 at 150 C, G; used below 25 C too, est.).
#   MF-R300: 0.020 (Rmin, D) to 0.080 (R1max, one hour after a trip or reflow, D; Rmax as delivered 0.05; Bourns MF-R
#     series REV. AR 09/26, SHA-256 d22f0f06...); +0.29 to +0.43 %/K (est.; the datasheet gives no curve below trip).
#   holder contacts: 0.02 to 0.04 (est.).
#   DMP3099L pair: 0.110 (typ about 55 mohm at VGS -6 V between the Fig. 3 curves, G) to 0.198 (99 mohm max at VGS -4.5 V,
#     D, the bound for |VGS| of 5.9 to 6.4 V; DS36081 Rev. 5-2 May 2025, SHA-256 06f30303...); +0.44 %/K above 25 C and
#     +0.37 %/K below (Fig. 5, normalized 1.55 at 150 C and 0.72 at -50 C, G).
#   chokes: 0.01 (est.), copper +0.39 %/K.
# Levels: "low" every part at its low value, "mid" halfway, "bound" every part at its datasheet maximum or estimated
# upper value, and "lever" = bound with the P-FET pair replaced by a pair of at most 0.06 ohm (a part to be selected).
FEED3 = [  # (name, lo, hi, tc below 25 C (lo, hi), tc above 25 C (lo, hi), key-down rise (lo, hi))
    ("AO3400A pair", 0.038, 0.064, (0.0056, 0.0056), (0.0056, 0.0056), (15.0, 50.0)),
    ("MF-R300", 0.020, 0.080, (0.0029, 0.0043), (0.0029, 0.0043), (15.0, 50.0)),
    ("holder contacts", 0.02, 0.04, (0.0, 0.0), (0.0, 0.0), (0.0, 0.0)),
    ("DMP3099L pair", 0.110, 0.198, (0.0037, 0.0037), (0.0044, 0.0044), (15.0, 50.0)),
    ("chokes", 0.01, 0.01, (0.0039, 0.0039), (0.0039, 0.0039), (5.6, 44.0)),
]
FEED3_LEVELS = [("low", 0.0, None), ("mid", 0.5, None), ("bound", 1.0, None), ("lever", 1.0, 0.06)]
LOSS3 = [0.84, 1.03, 1.34, 1.86]   # r13 MC median, r13 MC 99th percentile (0.93), r14 worst case (1.24, the lever), r13
                                   # worst case (1.76), each plus the 0.1 dB relay (lpf-ts012.md revision 2, 92e3805)
LOSS3_DESIGN = [0.84, 1.03, 1.86]
VGG_OFF = [-0.20, -0.10, 0.0]      # D-9 window below its top: 3.30 / 3.40 / 3.50 V at 6.4 V
VGG_TOP_64 = 3.50
OPEN_LOOP_TARGET_W = 7.9           # the D-9 top at 8.4 V is set so the highest corner makes this (0.05 dB under 8 W)
# Clamp scenario B (p5; an input to WP-PDR-22, not a design decision here): the open-loop ceiling at the 10 W maximum
# rating instead of the 8 W stability guarantee (9.9 W, 0.04 dB under), and a reference-based clamp whose window is
# 0.03 V (est.: a 0.1 % shunt reference and 0.1 % resistors, +/-0.3 %, plus the MCP6002 offset, about +/-15 mV).
CLAMPB_OFF = [-0.03, -0.015, 0.0]
CLAMPB_TARGET_W = 9.9
CLAMPB_LABEL = " clamp scenario B (s3 trade): 10 W ceiling, 0.03 V window."


def feed3_parts(ambient: float | None, state: str, lv: int) -> list[tuple[str, float]]:
    name, x, pfet = FEED3_LEVELS[lv]
    c = P.FEED_CELLS
    m = (1.0, 1.0) if ambient is None else c["mult"][int(ambient)]
    out = [(c["n"], (c["min"] + x * (c["max"] - c["min"])) * (m[0] + x * (m[1] - m[0])))]
    for nm, lo, hi, tcl, tch, rise in FEED3:
        r25 = lo + x * (hi - lo)
        if nm == "DMP3099L pair" and pfet is not None:
            r25 = pfet
        if ambient is None:
            out.append((nm, r25))
            continue
        t = ambient + ((rise[0] + x * (rise[1] - rise[0])) if state == "kd" else 0.0)
        tc = (tcl if t < 25 else tch)
        out.append((nm, r25 * (1.0 + (tc[0] + x * (tc[1] - tc[0])) * (t - 25.0))))
    return out


def feed3_at(case_key: str | None, lv: int) -> float:
    if case_key is None:
        return sum(r for _, r in feed3_parts(None, "soak", lv))
    tc = P.tc_by_key(case_key)
    return sum(r for _, r in feed3_parts(tc[2], tc[3], lv))


def a5_vgg_tables():
    xg = np.round(np.arange(2.40, 3.601, 0.05), 3)
    g135 = P.resample(P.load_curve("ra07_pout_vs_vgg_135"), xg, 0.015)
    g155 = P.resample(P.load_curve("ra07_pout_vs_vgg_155"), xg, 0.015)
    return xg, g135, g155


def py_module_w(vp, rf, eta, pin_dbm, f, vgg, typ, tcase_key, T, xg, g135, g155):
    """Python replica of the deck's module model at one pack voltage (for the D-9 top at 8.4 V only; the deck result
    is the record)."""
    w = (f - 135e6) / 20e6
    pv = lambda x: (1 - w) * np.interp(x, T["xv"], T["v135"]) + w * np.interp(x, T["xv"], T["v155"])
    pt = lambda p: (1 - w) * 10 ** (np.interp(p, T["xp"], T["p135"]) / 10) + w * 10 ** (np.interp(p, T["xp"], T["p155"]) / 10)
    kd = pt(pin_dbm) / pt(13.0103)
    gv = lambda v: (1 - w) * np.interp(v, xg, g135) + w * np.interp(v, xg, g155)
    kv = gv(vgg) / gv(3.5)
    ks = 1.0 if typ else P.A5_POUT_MIN_72 / pv(7.2)
    tc = P.tc_by_key(tcase_key)
    tcase = tc[4] if tc[4] is not None else None
    vd = vp
    pm = 0.0
    for _ in range(200):
        tcc = tcase if tcase is not None else tc[2] + P.RTH_CA["a5"] * (pm * (1 / eta - 1) + 10 ** ((pin_dbm - 30) / 10))
        dt = tcc - 25.0
        kt = 10 ** (tc[5] * (max(dt, 0) if tc[6] else dt) / 10)
        pm = pv(max(vd, 3.0)) * kd * kv * ks * kt
        vd_new = vp - rf * (P.IBUS + pm / (eta * max(vd, 1.0)))
        vd = 0.5 * vd + 0.5 * vd_new
    return float(pm)


CLAMP_GRID_V = [round(6.4 + 0.1 * k, 2) for k in range(21)]


def clamp_top_curve(pins, T, xg, g135, g155, target: float = OPEN_LOOP_TARGET_W) -> list[float]:
    """The most generous clamp that keeps the open-loop ceiling at every pack voltage: at each grid voltage the top of
    the window is the VGG at which the highest corner (-10 C start) makes the target, capped at 3.50 V (the
    RA07M1317M "Pout 10 W at VGG 3.5 V or less" condition and the D-9 top at 6.4 V). The deck interpolates linearly."""
    from scipy.optimize import brentq
    rf = feed3_at("coldhi", 0)
    out = []
    for v in CLAMP_GRID_V:
        def hi(g):
            return max(py_module_w(v, rf, eta, pins[2], f, g, True, "coldhi", T, xg, g135, g155)
                       for eta in P.A5_ETA for f in P.FREQS) - target
        out.append(VGG_TOP_64 if hi(VGG_TOP_64) <= 0 else float(brentq(hi, 2.45, VGG_TOP_64)))
    return out


def deck_p4(out: Path, pins: list[float], vtop: list[float], offs: list[float] | None = None,
            target: float = OPEN_LOOP_TARGET_W, label: str = "") -> tuple[Path, list[dict]]:
    offs = VGG_OFF if offs is None else offs
    T = P.a5_tables()
    xg, g135, g155 = a5_vgg_tables()
    dims = [("irf", [l[0] for l in FEED3_LEVELS]), ("ieta", P.A5_ETA), ("ipin", pins), ("ifr", P.FREQS), ("ivgg", offs),
            ("isp", ["typ", "min"]), ("iloss", LOSS3), ("itc", [c[0] for c in P.TC_CASES])]
    n = int(np.prod([len(v) for _, v in dims]))
    radix, lines = 1, []
    for name, vals in dims:
        lines.append(f".param {name}=floor(idx/{radix})-{len(vals)}*floor(idx/{radix * len(vals)})")
        radix *= len(vals)
    corners = []
    for combo in itertools.product(*[range(len(v)) for _, v in dims][::-1]):
        combo = combo[::-1]
        c = {name: vals[k] for (name, vals), k in zip(dims, combo)}
        c["rf_ohm"] = feed3_at(c["itc"], [l[0] for l in FEED3_LEVELS].index(c["irf"]))
        corners.append(c)
    def tab(name, vals, fmt="{:.6g}"):
        return f".param {name[1:]}=table({name}," + ",".join(f"{i},{fmt.format(v)}" for i, v in enumerate(vals)) + ")"
    def tctab(pname, vals):
        return f".param {pname}=table(itc," + ",".join(f"{i},{v:.6g}" for i, v in enumerate(vals)) + ")"
    rf_flat = [feed3_at(tc[0], lv) for tc in P.TC_CASES for lv in range(len(FEED3_LEVELS))]
    vt135 = P.table_expr("x", T["xv"], T["v135"])
    vt155 = P.table_expr("x", T["xv"], T["v155"])
    pt135 = P.table_expr("pin", T["xp"], T["p135"])
    pt155 = P.table_expr("pin", T["xp"], T["p155"])
    pr135 = P.table_expr("13.0103", T["xp"], T["p135"])
    pr155 = P.table_expr("13.0103", T["xp"], T["p155"])
    gx135 = P.table_expr("x", xg, g135)
    gx155 = P.table_expr("x", xg, g155)
    gh135 = P.table_expr("3.5", xg, g135)
    gh155 = P.table_expr("3.5", xg, g155)
    v72_135 = P.table_expr("7.2", T["xv"], T["v135"])
    v72_155 = P.table_expr("7.2", T["xv"], T["v155"])
    vtop84 = vtop[-1]
    vtab = P.table_expr("x", CLAMP_GRID_V, vtop, fmt="{:.5g}")
    txt = f"""* power_a5_design.cir: A5 RA07M1317M, output power at the SMA versus pack voltage with the adopted design
* (cwht WP-PDR-21 revision 3, hardware/sim/tx-pa/run_a5_r3.py p4; record docs/design/analysis/pa-drive-ts012.md)
* As revision 2 (power_a5.cir) with: the drive band of the select-on-test pad on the bandpass chain (s2); the D-9
* pack-dependent VGG clamp, VGG(Vp) = top(Vp) + offset, top(Vp) the most generous clamp that holds the open-loop ceiling:
* at each 0.1 V the VGG at which the highest corner from a -10 C start makes {target} W, capped at {VGG_TOP_64} V ({vtop[0]:.3f} V at
* 6.4 V, {vtop84:.4f} V at 8.4 V); offsets {', '.join(f'{o:g}' for o in offs)} V;{label}
* the drain feed from the datasheet reads per part and temperature case; the D-14 LPF loss corners {LOSS3} dB.
* {n} corners flattened into one .step (idx), first dimension fastest: {', '.join(d for d, _ in dims)}.
.param idx=0
.step param idx 0 {n - 1} 1
{chr(10).join(lines)}
* temperature cases (itc): {'; '.join(f'{i} {tc[1]}' for i, tc in enumerate(P.TC_CASES))}
.param rf=table(itc*{len(FEED3_LEVELS)}+irf,{','.join(f'{i},{v:.5g}' for i, v in enumerate(rf_flat))})
{tctab('ta', [tc[2] for tc in P.TC_CASES])}
{tctab('tcfix', [tc[4] if tc[4] is not None else -999 for tc in P.TC_CASES])}
{tctab('coef', [tc[5] for tc in P.TC_CASES])}
{tctab('ng', [1 if tc[6] else 0 for tc in P.TC_CASES])}
{tctab('cu', [P.copper_db_per_db(tc) for tc in P.TC_CASES])}
.param rth={P.RTH_CA['a5']}
.param pinw_pa=pow(10,(pin-30)/10)
{tab('ipin', pins)}
{tab('ifr', P.FREQS)}
{tab('iloss', LOSS3)}
{tab('ivgg', offs)}
{tab('ieta', P.A5_ETA)}
.param w=(fr-135e6)/20e6
.param kloss=pow(10,-(loss+(loss-{P.LOSS_RELAY_DB})*cu)/10)
.param isp_=isp
* drive factor: datasheet Pout-Pin curves at 7.2 V, relative to Pin 20 mW
.param kd=((1-w)*pow(10,{pt135}/10)+w*pow(10,{pt155}/10))/((1-w)*pow(10,{pr135}/10)+w*pow(10,{pr155}/10))
* spread factor: datasheet minimum 6.5 W at 7.2 V against the typical curve
.param kmin={P.A5_POUT_MIN_72}/((1-w)*{v72_135}+w*{v72_155})
.param ks=if(isp_>0.5,kmin,1)
.func pv(x)=(1-w)*{vt135}+w*{vt155}
* D-9 clamp: VGG as a function of the pack voltage V(p) (read in receive; the clamp divider is fed from the pack)
.func vggof(x)={vtab}+vgg
.func gv(x)=(1-w)*{gx135}+w*{gx155}
.param gref=(1-w)*{gh135}+w*{gh155}
Btc tc 0 V=if(tcfix>-500,tcfix,ta+rth*(V(pmod)*(1/eta-1)+pinw_pa))
Rtc tc 0 1meg
.func kt(t)=pow(10,coef*if(ng>0.5,max(t-25,0),t-25)/10)
Bvg vg 0 V=vggof(V(p))
Rvg vg 0 1meg
Bmod pmod 0 V=pv(max(V(d),3))*kd*gv(V(vg))/gref*ks*kt(V(tc))
Rmod pmod 0 1meg
Bpa d 0 I=V(pmod)/(eta*max(V(d),1))
Vp p 0 7.4
Rf p d {{rf}}
Ibus d 0 {P.IBUS}
Bsma psma 0 V=V(pmod)*kloss
Rsma psma 0 1meg
.dc Vp 6.4 8.4 0.05
.save V(d) V(pmod) V(psma) V(tc) V(vg) I(Vp)
.end
"""
    pth = out / "power_a5_design.cir"
    pth.write_text(txt)
    return pth, corners


def run_p4(key: str = "p4", offs: list[float] | None = None, target: float = OPEN_LOOP_TARGET_W, label: str = ""):
    offs = VGG_OFF if offs is None else offs
    out = rundir(key)
    s2 = json.loads((rundir("s2") / "result.json").read_text())
    pins = [float(P.dbm(s2["band"]["min_mw"] * 1e-3)), float(P.dbm(P.SOT_TARGET_MW * 1e-3)), float(P.dbm(s2["band"]["max_mw"] * 1e-3))]
    T = P.a5_tables()
    xg, g135, g155 = a5_vgg_tables()
    vtop = clamp_top_curve(pins, T, xg, g135, g155, target)
    vtop84 = vtop[-1]
    deck, corners = deck_p4(out, pins, vtop, offs, target, label)
    prov = P.run_ltspice(deck, out, timeout=6000)
    from spicelib import RawRead
    raw = RawRead(str(out / "power_a5_design.raw"))
    nst = len(raw.get_steps())
    verdict(key, "check: one .raw step per corner", nst == len(corners), "check", f"{nst} steps")
    vp = np.abs(raw.get_trace(raw.get_trace_names()[0]).get_wave(0))
    S = np.array([raw.get_trace("V(psma)").get_wave(i) for i in range(nst)])
    M = np.array([raw.get_trace("V(pmod)").get_wave(i) for i in range(nst)])
    TCW = np.array([raw.get_trace("V(tc)").get_wave(i) for i in range(nst)])
    VG = np.array([raw.get_trace("V(vg)").get_wave(i) for i in range(nst)])
    IP = np.array([np.abs(raw.get_trace("I(Vp)").get_wave(i)) for i in range(nst)])
    i64, i84 = int(np.argmin(np.abs(vp - 6.4))), int(np.argmin(np.abs(vp - 8.4)))
    # checks: thermal law at every pack voltage of every key-down corner (INSP-114 finding-11 (ii)); VGG at 6.4 V
    dev = 0.0
    for i, c in enumerate(corners):
        tc = P.tc_by_key(c["itc"])
        if tc[4] is None:
            want = tc[2] + P.RTH_CA["a5"] * (M[i] * (1 / c["ieta"] - 1) + 10 ** ((c["ipin"] - 30) / 10))
            dev = max(dev, float(np.max(np.abs(want - TCW[i]))))
    verdict(key, "check: PA case temperature equals the thermal law within 0.01 K at every pack voltage", dev <= 0.01, "check",
            f"largest difference {dev:.2e} K")
    vg64 = [float(VG[:, i64].min()), float(VG[:, i64].max())]
    verdict(key, f"check: VGG {VGG_TOP_64 + min(offs):.2f} to {VGG_TOP_64:.2f} V at 6.4 V", abs(vg64[0] - VGG_TOP_64 - min(offs)) < 1e-3 and abs(vg64[1] - VGG_TOP_64) < 1e-3, "check",
            f"{vg64[0]:.3f} to {vg64[1]:.3f} V")
    tck = np.array([c["itc"] for c in corners])
    typ = np.array([c["isp"] == "typ" for c in corners])
    rfl = np.array([c["irf"] for c in corners])
    loss = np.array([c["iloss"] for c in corners])
    design = np.isin(rfl, ["low", "mid", "bound"]) & np.isin(loss, LOSS3_DESIGN)
    nomd = dict(irf="mid", ieta=0.60, ipin=pins[1], ifr=146e6, ivgg=offs[1], isp="typ", iloss=0.84)
    by = {}
    kd_cases = [tc[0] for tc in P.TC_CASES if tc[3] == "kd"]
    def lo_at(mask, col):
        ii = np.where(mask)[0]
        j = int(ii[np.argmin(S[ii, col])])
        return float(S[j, col]), corners[j], float(TCW[j, col])
    def reach(curve):
        ok = curve >= P.REQ012_LO
        return round(float(vp[np.argmax(ok)]), 2) if ok.any() else None
    for tc in P.TC_CASES:
        k = tc[0]
        m = tck == k
        inom = next(i for i, c in enumerate(corners) if c["itc"] == k and all(c[a] == b for a, b in nomd.items()))
        d = {"label": tc[1], "feed_ohm": {l[0]: feed3_at(k, j) for j, l in enumerate(FEED3_LEVELS)}}
        sets = {
            "nominal": None,
            "low_typ_lpfmed": m & typ & design & (loss <= 0.84 + 1e-9),
            "low_typ_lpf99": m & typ & design & (loss <= 1.03 + 1e-9),
            "low_typ_lpfworst": m & typ & design,
            "low_min_lpfmed": m & ~typ & design & (loss <= 0.84 + 1e-9),
            "low_min_lpf99": m & ~typ & design & (loss <= 1.03 + 1e-9),
            "low_min_lpfworst": m & ~typ & design,
            "lever_pfet_typ_lpfworst": m & typ & np.isin(rfl, ["low", "mid", "lever"]) & np.isin(loss, LOSS3_DESIGN),
            "lever_r14_typ": m & typ & np.isin(rfl, ["low", "mid", "bound"]) & np.isin(loss, [0.84, 1.03, 1.34]),
            "lever_both_typ": m & typ & np.isin(rfl, ["low", "mid", "lever"]) & np.isin(loss, [0.84, 1.03, 1.34]),
        }
        d["at_6v4"] = {"nominal_w": float(S[inom, i64]), "nominal_pa_case_c": float(TCW[inom, i64])}
        d["at_8v4"] = {"nominal_w": float(S[inom, i84])}
        d["curves"] = {"nominal": S[inom].tolist()}
        d["reach_3v97"] = {"nominal": reach(S[inom])}
        d["corners"] = {"nominal": corners[inom]}
        for nm, mask in sets.items():
            if mask is None:
                continue
            w64, c64, t64 = lo_at(mask, i64)
            curve = S[mask].min(axis=0)
            d["at_6v4"][nm + "_w"] = w64
            d["at_6v4"][nm + "_margin_db"] = float(10 * np.log10(w64 / P.REQ012_LO))
            d["at_6v4"][nm + "_pa_case_c"] = t64
            d["at_8v4"][nm + "_w"] = float(curve[i84])
            d["curves"][nm] = curve.tolist()
            d["reach_3v97"][nm] = reach(curve)
            d["corners"][nm] = c64
        d["at_8v4"]["module_high_w"] = float(M[m & design, i84].max())
        d["at_8v4"]["pa_case_high_c"] = float(TCW[m & design, i84].max())
        d["module_high_curve_w"] = M[m & design].max(axis=0).tolist()
        d["pack_current_max_a"] = float(IP[m & design].max())
        by[k] = d
    unc_lo = sum(u[1] for u in P.CLOSURE_UNC)
    unc_hi = sum(u[2] for u in P.CLOSURE_UNC)
    res = {"run": RUNS3[key], "revision": REVISION, "ltspice": prov, "n_corners": len(corners), "vpack": vp.tolist(),
           "pins_dbm": pins, "pins_mw": [10 ** (p / 10) for p in pins], "vgg_top_6v4": vtop[0], "vgg_top_8v4": vtop84,
           "clamp_grid_v": CLAMP_GRID_V, "clamp_top_v": vtop,
           "open_loop_target_w": target, "vgg_offsets": offs, "label": label, "loss_db": LOSS3, "feed_levels": [l[0] for l in FEED3_LEVELS],
           "feed_25c_ohm": {l[0]: feed3_at(None, j) for j, l in enumerate(FEED3_LEVELS)},
           "feed_parts_25c": {l[0]: feed3_parts(None, "soak", j) for j, l in enumerate(FEED3_LEVELS)},
           "unmodelled_db": [unc_lo, unc_hi], "by_tc": by, "kd_cases": kd_cases,
           "module_high_8v4_all_w": float(max(by[k]["at_8v4"]["module_high_w"] for k in by)),
           "vg_6v4": vg64}
    worst = lambda key: float(min(by[k]["at_6v4"][key] for k in kd_cases))
    for kk in ("nominal_w", "low_typ_lpfmed_w", "low_typ_lpf99_w", "low_typ_lpfworst_w", "low_min_lpfmed_w",
               "low_min_lpf99_w", "low_min_lpfworst_w", "lever_pfet_typ_lpfworst_w", "lever_r14_typ_w", "lever_both_typ_w"):
        res["worst_kd_6v4_" + kk] = worst(kk)
    res["lowest_typ_lpfworst_8v4_all_kd_w"] = float(min(by[k]["at_8v4"]["low_typ_lpfworst_w"] for k in kd_cases))
    top = np.array([c["ivgg"] == max(offs) for c in corners])
    res["lowest_typ_lpf99_8v4_top_w"] = float(S[np.isin(tck, kd_cases) & typ & design & top & (loss <= 1.03 + 1e-9), i84].min())
    res["lowest_typ_lpf99_8v4_all_kd_w"] = float(min(by[k]["at_8v4"]["low_typ_lpf99_w"] for k in kd_cases))
    res["lowest_typ_lpfworst_min_over_range_all_kd_w"] = float(min(min(by[k]["curves"]["low_typ_lpfworst"]) for k in kd_cases))
    verdict(key, f"A5 open loop at 8.4 V: module output at most {8.0 if target <= 8.0 else 10.0:g} W in every case (clamp)", res["module_high_8v4_all_w"] <= (8.0 if target <= 8.0 else 10.0),
            detail=f"{res['module_high_8v4_all_w']:.2f} W")
    res["module_high_all_v_w"] = float(max(max(by[k]["module_high_curve_w"]) for k in by))
    ceil = 8.0 if target <= 8.0 else 10.0
    verdict(key, f"A5 open loop from 6.4 to 8.4 V: module output at most {ceil:g} W at every pack voltage and case (clamp)",
            res["module_high_all_v_w"] <= ceil, detail=f"{res['module_high_all_v_w']:.2f} W")
    verdict(key, "A5 nominal corner at least 3.97 W at 6.4 V in every key-down case", res["worst_kd_6v4_nominal_w"] >= P.REQ012_LO,
            detail=f"{res['worst_kd_6v4_nominal_w']:.2f} W")
    verdict(key, "A5 lowest corner (typical module, LPF at most its median) at least 3.97 W at 6.4 V, every key-down case",
            res["worst_kd_6v4_low_typ_lpfmed_w"] >= P.REQ012_LO, detail=f"{res['worst_kd_6v4_low_typ_lpfmed_w']:.2f} W")
    verdict(key, "A5 lowest corner (typical module, LPF worst case) at least 3.97 W at 6.4 V, every key-down case",
            res["worst_kd_6v4_low_typ_lpfworst_w"] >= P.REQ012_LO, detail=f"{res['worst_kd_6v4_low_typ_lpfworst_w']:.2f} W")
    verdict(key, "A5 lowest corner (typical module, LPF worst case) at least 3.97 W at 8.4 V with the clamp, every key-down case",
            res["lowest_typ_lpfworst_8v4_all_kd_w"] >= P.REQ012_LO, detail=f"{res['lowest_typ_lpfworst_8v4_all_kd_w']:.2f} W")
    res["verdicts"] = VERDICTS.get(key, {})
    (out / "result.json").write_text(json.dumps(res, indent=0, default=str))
    plot_p4(out, res, key)
    write_p4_md(out, res)
    copy_inputs(out, [deck])
    res["kept_raw"] = raw_manifest(out)
    (out / "result.json").write_text(json.dumps(res, indent=0, default=str))
    print(key, json.dumps({k: v for k, v in res.items() if k.startswith("worst_") or k in ("vgg_top_8v4", "module_high_8v4_all_w",
                                                                                            "lowest_typ_lpfworst_8v4_all_kd_w")}, default=str))
    return res


TC_COL = P.TC_COL
TC_SHORT = P.TC_SHORT


def plot_p4(out: Path, r: dict, key: str = "p4"):
    vp = np.array(r["vpack"])
    by = r["by_tc"]
    fig, ax = plt.subplots(figsize=(9.2, 7.2))
    ref = by["t25a"]
    ax.plot(vp, ref["curves"]["nominal"], color=COL["a5"], lw=2.2, label="nominal corner, 25 C key-down, -0.005 dB/K")
    for k in r["kd_cases"]:
        ax.plot(vp, by[k]["curves"]["low_typ_lpfworst"], color=TC_COL[k], lw=1.1, ls="--",
                label=f"lowest, typical module, LPF worst case (1.76 dB): {by[k]['label']}")
    ax.plot(vp, ref["curves"]["low_typ_lpfmed"], color=INK2, lw=1.5, label="lowest, typical module, LPF at most its median: 25 C key-down")
    ax.plot(vp, ref["curves"]["low_min_lpfmed"], color=COL["aux"], lw=1.5, ls="-.",
            label="lowest, datasheet-minimum module, LPF at most its median: 25 C key-down")
    ax.plot(vp, by["coldhi"]["module_high_curve_w"], color=INK2, lw=1.2, ls=(0, (1, 1)),
            label=f"module output, highest corner, -10 C start, ALC open (clamp top {r['vgg_top_6v4']:.2f} to {r['vgg_top_8v4']:.2f} V)")
    ax.axhline(8.0, color=INK2, lw=1, ls=":", label="8 W: module stability guarantee (module output)")
    ax.axhline(10.0, color=INK2, lw=1.6, ls=":", label="10 W: module maximum rating (module output)")
    P.add_req_lines(ax)
    ax.set_xlim(6.4, 8.4)
    ax.set_ylim(0, 11)
    ax.set_xlabel("Pack voltage, read in receive (V)")
    ax.set_ylabel("Available power, ALC at its top (W)")
    ax.set_title(f"{key}: A5 {'as adopted (D-9 clamp' if key == 'p4' else 'with clamp scenario B (10 W ceiling, 0.03 V window'}; select-on-test pad on the bandpass chain, D-14 LPF, feed reads)\n"
                 f"power at the SMA versus pack voltage, LTspice, {r['n_corners']} corners", fontsize=9.5)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.1), ncol=2, fontsize=6.6)
    fig.tight_layout()
    fig.savefig(out / f"power_a5_{'design' if key == 'p4' else 'clampb'}_sma.png", dpi=150)
    plt.close(fig)
    fig, ax = plt.subplots(figsize=(10.4, 6.6))
    keys = [k for k in by if k != "coldhi"]
    x = np.arange(len(keys))
    series = [("nominal_w", "nominal corner", COL["a5"], "o"),
              ("low_typ_lpfmed_w", "lowest, typical module, LPF at most its median (0.74 dB)", INK2, "^"),
              ("low_typ_lpf99_w", "lowest, typical module, LPF at most its MC 99th percentile (0.93 dB)", "#0e7a54", "s"),
              ("low_typ_lpfworst_w", "lowest, typical module, LPF worst case (1.76 dB)", INK, "v"),
              ("low_min_lpf99_w", "lowest, datasheet-minimum module, LPF at most its MC 99th percentile", COL["aux"], "D"),
              ("lever_both_typ_w", "lever: P-FET pair at most 0.06 ohm and the r14 LPF (worst 1.24 dB), typical module", "#b3401a", "*")]
    allv = []
    for j, (kk, lab, col, mk) in enumerate(series):
        ys = [by[k]["at_6v4"][kk] for k in keys]
        allv += ys
        ax.plot(x + (j - (len(series) - 1) / 2) * 0.11, ys, mk, color=col, ms=6.5, ls="none", label=lab)
    P.add_req_lines(ax)
    ax.axhline(4.0, color=COL["ok"], lw=1.0, ls="--", label="4.0 W: D-10 low-pack setpoint limit at 6.4 V")
    ax.set_xticks(x)
    ax.set_xticklabels([TC_SHORT[k] for k in keys], fontsize=6.8)
    ax.set_ylim(np.floor((min(allv) - 0.25) * 2) / 2, 6.6)
    ax.set_ylabel("Power at the SMA at 6.4 V pack (W)")
    ax.set_title(f"{key}: A5 {'as adopted' if key == 'p4' else 'with clamp scenario B'}, power at the SMA at the 6.4 V pack end per temperature case (revision 3)\n"
                 "PA coefficient -0.005 or -0.015 dB/K above a 25 C case (estimate)", fontsize=9)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.16), ncol=1, fontsize=7.2)
    fig.tight_layout()
    fig.savefig(out / f"power_a5_{'design' if key == 'p4' else 'clampb'}_temperature.png", dpi=150)
    plt.close(fig)


def write_p4_md(out: Path, r: dict):
    by = r["by_tc"]
    L = [f"# {r['run']}: A5 output power at the SMA, {'the adopted design (D-9 clamp)' if not r['label'] else 'clamp scenario B'} (revision 3)", "",
         f"Drive band from s2: {r['pins_mw'][0]:.1f} / {r['pins_mw'][1]:.1f} / {r['pins_mw'][2]:.1f} mW. Clamp: VGG "
         f"{r['vgg_top_6v4'] + min(r['vgg_offsets']):.2f} to {r['vgg_top_6v4']:.2f} V at 6.4 V, top tracking the open-loop ceiling to {r['vgg_top_8v4']:.3f} V at 8.4 V "
         f"(open-loop target {r['open_loop_target_w']} W).{r['label']} LPF plus relay {r['loss_db']} dB. Feed at 25 C part temperature: "
         + ", ".join(f"{k} {v:.3f} ohm" for k, v in r["feed_25c_ohm"].items()) + ". All figures estimates.", "",
         "| Case | Nominal (W) | Lowest, typ., LPF median | typ., LPF MC 99 % | typ., LPF worst | min. module, LPF median | min., LPF MC 99 % | Lever: P-FET and r14 LPF, typ. |",
         "|---|---|---|---|---|---|---|---|"]
    for k, d in by.items():
        a = d["at_6v4"]
        L.append(f"| {d['label']} | {a['nominal_w']:.2f} | {a['low_typ_lpfmed_w']:.2f} ({a['low_typ_lpfmed_margin_db']:+.2f} dB) | "
                 f"{a['low_typ_lpf99_w']:.2f} ({a['low_typ_lpf99_margin_db']:+.2f}) | {a['low_typ_lpfworst_w']:.2f} ({a['low_typ_lpfworst_margin_db']:+.2f}) | "
                 f"{a['low_min_lpfmed_w']:.2f} ({a['low_min_lpfmed_margin_db']:+.2f}) | {a['low_min_lpf99_w']:.2f} ({a['low_min_lpf99_margin_db']:+.2f}) | "
                 f"{a['lever_both_typ_w']:.2f} ({a['lever_both_typ_margin_db']:+.2f}) |")
    L += ["", "Pack voltage at which each lowest corner reaches 3.97 W (V; None: not reached by 8.4 V):", "",
          "| Case | nominal | typ., LPF median | typ., LPF MC 99 % | typ., LPF worst | min., LPF MC 99 % |", "|---|---|---|---|---|---|"]
    for k, d in by.items():
        rr = d["reach_3v97"]
        L.append(f"| {d['label']} | {rr['nominal']} | {rr['low_typ_lpfmed']} | {rr['low_typ_lpf99']} | {rr['low_typ_lpfworst']} | {rr['low_min_lpf99']} |")
    L += ["", f"At 8.4 V with the clamp: module highest corner {r['module_high_8v4_all_w']:.2f} W over every case; lowest corner "
          f"(typical module, LPF worst) {r['lowest_typ_lpfworst_8v4_all_kd_w']:.2f} W at worst over the key-down cases.",
          f"Largest pack current at key-down (design corners): " + ", ".join(f"{d['label']} {d['pack_current_max_a']:.2f} A" for d in by.values()) + ".",
          "", "Every quoted lowest corner with its parameters is in `result.json` (`by_tc.<case>.corners`).",
          f"Plots `power_a5_{'design' if not r['label'] else 'clampb'}_sma.png`, `power_a5_{'design' if not r['label'] else 'clampb'}_temperature.png`; deck `power_a5_design.cir`.", ""]
    (out / "result.md").write_text("\n".join(L))


# ---------------------------------------------------------------- s3: REQ-SYS-012 low-pack basis and verdicts
S3_COVER = [  # (key, label) of the coverage sets, from p4
    ("nominal_w", "nominal corner"),
    ("low_typ_lpfmed_w", "lowest, typical module, LPF at most its Monte Carlo median"),
    ("low_typ_lpf99_w", "lowest, typical module, LPF at most its Monte Carlo 99th percentile"),
    ("low_typ_lpfworst_w", "lowest, typical module, LPF at its searched worst case"),
    ("low_min_lpfmed_w", "lowest, datasheet-minimum module, LPF median"),
    ("low_min_lpf99_w", "lowest, datasheet-minimum module, LPF MC 99th percentile"),
    ("low_min_lpfworst_w", "lowest, datasheet-minimum module, LPF worst case"),
    ("lever_pfet_typ_lpfworst_w", "lever: P-FET pair at most 0.06 ohm, typical module, LPF worst"),
    ("lever_both_typ_w", "levers: P-FET pair and the r14 LPF, typical module"),
]
S3_BASIS = "low_typ_lpf99_w"   # the proposed basis of the delta value (typical module, LPF 99th percentile)
D10_SETPOINT_6V4_W = 4.0


# The D-9 clamp at 8.4 V: one clamp value serves both the open-loop ceiling (highest corner, -10 C start) and the
# closed-loop reach (lowest corner, steady key-down); both are at the same pack voltage, so the conflict does not depend
# on the clamp's shape in pack voltage. The trade is computed with the Python replica of the p4 module model
# (py_module_w), checked against the p4 deck at the D-9 design point.
CLAMP_TOPS = [2.86, 2.95, 3.00, 3.05, 3.10, 3.20, 3.30]
CLAMP_WINDOWS = [0.20, 0.03]     # the D-9 divider window (LM2940 +/-5 %, 1 % resistors) and a reference-based one (est.)


def clamp_trade(p4: dict) -> dict:
    T = P.a5_tables()
    xg, g135, g155 = a5_vgg_tables()
    pins = p4["pins_dbm"]
    kd = p4["kd_cases"]
    def high(v):
        return max(py_module_w(8.4, feed3_at("coldhi", 0), eta, pins[2], f, v, True, "coldhi", T, xg, g135, g155)
                   for eta in P.A5_ETA for f in P.FREQS)
    def low(v, lossmax=1.03):
        best = 1e9
        for k in kd:
            tc = P.tc_by_key(k)
            for lv in range(3):
                rf = feed3_at(k, lv)
                for eta in P.A5_ETA:
                    for pin in pins:
                        for f in P.FREQS:
                            pm = py_module_w(8.4, rf, eta, pin, f, v, True, k, T, xg, g135, g155)
                            for L in [x for x in LOSS3_DESIGN if x <= lossmax]:
                                best = min(best, pm * 10 ** (-(L + (L - P.LOSS_RELAY_DB) * P.copper_db_per_db(tc)) / 10))
        return best
    chk_hi = high(p4["vgg_top_8v4"])
    chk_lo = low(p4["vgg_top_8v4"])
    deck_hi = p4["module_high_8v4_all_w"]
    deck_lo = p4["lowest_typ_lpf99_8v4_top_w"]
    ok = abs(chk_hi / deck_hi - 1) < 0.005 and abs(chk_lo / deck_lo - 1) < 0.005
    verdict("s3", "check: the Python replica equals the p4 deck at 8.4 V within 0.5 % (highest module, lowest at the window top)", ok,
            "check", f"{chk_hi:.3f} against {deck_hi:.3f} W; {chk_lo:.3f} against {deck_lo:.3f} W")
    rows = []
    for top in CLAMP_TOPS:
        r = {"top_v": top, "high_module_w": float(high(top))}
        for wdw in CLAMP_WINDOWS:
            r[f"low_lpf99_w_window_{wdw:.2f}"] = float(low(top - wdw))
        rows.append(r)
    return {"rows": rows, "replica_check": {"high_w": chk_hi, "deck_high_w": deck_hi, "low_w": chk_lo, "deck_low_w": deck_lo}}


def s3_rows(pr: dict) -> list[dict]:
    by, kd = pr["by_tc"], pr["kd_cases"]
    unc_lo, unc_hi = pr["unmodelled_db"]
    rows = []
    for key, lab in S3_COVER:
        w = min(by[k]["at_6v4"][key] for k in kd)
        kw = min(kd, key=lambda k: by[k]["at_6v4"][key])
        m = 10 * np.log10(w / P.REQ012_LO)
        m5 = 10 * np.log10(w / P.REQ012_NOM)
        reach = [by[k]["reach_3v97"].get(key[:-2]) for k in kd]
        w84 = min(by[k]["at_8v4"][key] for k in kd)
        rows.append({"key": key, "label": lab, "worst_w": float(w), "worst_case": by[kw]["label"],
                     "margin_db": float(m), "margin_with_terms_db": [float(m + unc_lo), float(m + unc_hi)],
                     "dev_from_5w_db": float(m5), "dev_from_5w_with_terms_db": float(m5 + unc_lo),
                     "delivered_with_d10_w": float(min(D10_SETPOINT_6V4_W, w)), "worst_8v4_w": float(w84),
                     "pack_v_reaches_3v97_worst": (None if any(x is None for x in reach) else float(max(reach)))})
    return rows


def s3_proposal(pr: dict, rows: list[dict], tag: str) -> dict:
    """Low limit at 6.4 V: the basis worst with the unmodelled terms, rounded to the next 0.1 dB below 5 W; the -1 dB
    bound from the pack voltage where the basis reaches 3.97 W in every key-down case (the envelope with the terms)."""
    by, kd = pr["by_tc"], pr["kd_cases"]
    unc_lo = pr["unmodelled_db"][0]
    vp = np.array(pr["vpack"])
    basis = next(r for r in rows if r["key"] == S3_BASIS)
    x_db = float(np.ceil(-basis["dev_from_5w_with_terms_db"] * 10 - 1e-9) / 10)
    env = np.min([by[k]["curves"][S3_BASIS[:-2]] for k in kd], axis=0)
    env_t = env * 10 ** (unc_lo / 10)
    ok = env_t >= P.REQ012_LO
    v1 = None
    if ok.any():
        j = int(np.argmax(ok))
        if ok[j:].all():
            v1 = float(np.ceil(vp[j] * 10 - 1e-9) / 10)
    out = {"x_db": x_db, "low_end_w": float(5.0 * 10 ** (-x_db / 10)), "v_full_band": v1, "envelope_w": env.tolist()}
    if v1 is not None:
        lim_db = np.where(vp >= v1, -1.0, -x_db + (x_db - 1.0) * (vp - 6.4) / max(v1 - 6.4, 1e-9))
        lim_w = 5.0 * 10 ** (lim_db / 10)
        out["limit_line_w"] = lim_w.tolist()
        out["limit_under_envelope_with_terms"] = bool(np.all(env_t >= lim_w - 1e-6))
        verdict("s3", f"check: the proposed REQ-SYS-012 limit line lies under the basis with the unmodelled terms ({tag})",
                out["limit_under_envelope_with_terms"], "check")
    return out


def run_s3():
    out = rundir("s3")
    p4 = json.loads((rundir("p4") / "result.json").read_text())
    p5 = json.loads((rundir("p5") / "result.json").read_text())
    unc_lo, unc_hi = p4["unmodelled_db"]
    vp = np.array(p4["vpack"])
    rows4, rows5 = s3_rows(p4), s3_rows(p5)
    prop4, prop5 = s3_proposal(p4, rows4, "D-9 as specified"), s3_proposal(p5, rows5, "clamp scenario B")
    res = {"run": RUNS3["s3"], "revision": REVISION, "power_runs": [RUNS3["p4"], RUNS3["p5"]], "unmodelled_db": [unc_lo, unc_hi],
           "basis": S3_BASIS, "d10_setpoint_6v4_w": D10_SETPOINT_6V4_W, "vpack": vp.tolist(),
           "d9": {"rows": rows4, "proposal": prop4, "vgg_top_8v4": p4["vgg_top_8v4"], "module_high_8v4_w": p4["module_high_8v4_all_w"]},
           "clamp_b": {"rows": rows5, "proposal": prop5, "vgg_top_8v4": p5["vgg_top_8v4"], "module_high_8v4_w": p5["module_high_8v4_all_w"]}}
    res["clamp_trade"] = clamp_trade(p4)
    b4 = next(r for r in rows4 if r["key"] == S3_BASIS)
    b5 = next(r for r in rows5 if r["key"] == S3_BASIS)
    verdict("s3", "A5 REQ-SYS-012 as baselined (5 W -1 dB at 6.4 V) on the basis (typical module, LPF MC 99th percentile, every key-down case, unmodelled terms), D-9 clamp",
            b4["margin_with_terms_db"][0] >= 0, detail=f"{b4['margin_with_terms_db'][0]:+.2f} dB")
    verdict("s3", "A5 REQ-SYS-012 lower bound at 8.4 V on the basis, D-9 clamp as specified (8 W open-loop ceiling)",
            b4["worst_8v4_w"] >= P.REQ012_LO, detail=f"{b4['worst_8v4_w']:.2f} W")
    verdict("s3", "A5 REQ-SYS-012 lower bound at 8.4 V on the basis, clamp scenario B (10 W ceiling, 0.03 V window)",
            b5["worst_8v4_w"] >= P.REQ012_LO, detail=f"{b5['worst_8v4_w']:.2f} W")
    res["verdicts"] = VERDICTS.get("s3", {})
    # plot
    fig, axs = plt.subplots(1, 3, figsize=(19.0, 7.0), gridspec_kw={"width_ratios": [1.2, 1.0, 1.0]})
    ax = axs[0]
    for pr, rw, prop, tag, ls in ((p4, rows4, prop4, "D-9 as specified", "--"), (p5, rows5, prop5, "clamp B", "-")):
        by, kd = pr["by_tc"], pr["kd_cases"]
        for key, lab, col in (("nominal", "nominal", COL["a5"]), ("low_typ_lpf99", "lowest, typ., LPF MC 99 % (basis)", "#0e7a54"),
                              ("low_typ_lpfworst", "lowest, typ., LPF worst", INK), ("low_min_lpf99", "lowest, min. module, LPF MC 99 %", COL["aux"])):
            e = np.min([by[k]["curves"][key] for k in kd], axis=0)
            ax.plot(vp, e, color=col, lw=1.5, ls=ls, label=f"{tag}: {lab}")
    env = np.array(prop5["envelope_w"])
    ax.fill_between(vp, env * 10 ** (unc_lo / 10), env, color="#0e7a54", alpha=0.15, label="clamp B basis with the unmodelled terms")
    if prop5.get("limit_line_w"):
        ax.plot(vp, prop5["limit_line_w"], color=COL["a4"], lw=2.2,
                label=f"proposed low limit (clamp B): 5 W -{prop5['x_db']:.1f} dB at 6.4 V, -1 dB from {prop5['v_full_band']:.1f} V")
    P.add_req_lines(ax)
    ax.set_xlim(6.4, 8.4)
    ax.set_ylim(1.5, 6.8)
    ax.set_xlabel("Pack voltage, read in receive (V)")
    ax.set_ylabel("Available power at the SMA (W), ALC at its top;\nminimum over the key-down cases")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncol=2, fontsize=6.5)
    ax.set_title("s3: REQ-SYS-012 basis, A5\n(dashed: D-9 as specified, p4; solid: clamp scenario B, p5)", fontsize=9)
    ax = axs[1]
    labs = [r["label"].replace("lowest, ", "").replace("Monte Carlo", "MC") for r in rows4]
    y = np.arange(len(rows4))[::-1]
    for yy, r4, r5 in zip(y, rows4, rows5):
        for r, dy, col in ((r4, 0.15, COL["a4"]), (r5, -0.15, COL["a5"])):
            lo, hi = r["margin_with_terms_db"]
            ax.plot([lo, hi], [yy + dy, yy + dy], color=col, lw=4, solid_capstyle="butt", alpha=0.45)
            ax.plot(r["margin_db"], yy + dy, "o", color=col, ms=5)
    ax.plot([], [], "o-", color=COL["a4"], label="D-9 as specified (VGG 3.30 to 3.50 V at 6.4 V)")
    ax.plot([], [], "o-", color=COL["a5"], label="clamp scenario B (VGG 3.47 to 3.50 V at 6.4 V)")
    ax.axvline(0, color=INK, lw=1.4)
    ax.set_yticks(y)
    ax.set_yticklabels(labs, fontsize=6.4)
    ax.set_xlabel("Margin to 3.97 W at 6.4 V, worst key-down case (dB)\nbar: with the unmodelled terms")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), fontsize=7)
    ax.set_title("Margin at 6.4 V per coverage set", fontsize=9)
    ax = axs[2]
    ct = res["clamp_trade"]["rows"]
    ax.plot([r["high_module_w"] for r in ct], [r["low_lpf99_w_window_0.20"] for r in ct], "o-", color=COL["a4"],
            label="D-9 divider window 0.20 V (lowest at top - 0.20 V)")
    ax.plot([r["high_module_w"] for r in ct], [r["low_lpf99_w_window_0.03"] for r in ct], "s-", color=COL["a5"],
            label="reference-based window 0.03 V (est.)")
    for r in ct:
        ax.annotate(f"{r['top_v']:.2f} V", (r["high_module_w"], r["low_lpf99_w_window_0.03"]), textcoords="offset points",
                    xytext=(4, 4), fontsize=6.5, color=INK2)
    ax.axvline(8.0, color=INK, lw=1.2, ls=":", label="8 W: stability guarantee (D-9 open-loop criterion)")
    ax.axvline(10.0, color=INK, lw=1.4, label="10 W: module maximum rating")
    ax.axhline(P.REQ012_LO, color=INK, lw=2.0, ls="--", label="3.97 W: REQ-SYS-012 lower bound")
    ax.set_xlabel("Open-loop module output at 8.4 V (W)\n(highest corner, -10 C start)")
    ax.set_ylabel("Lowest at the SMA at 8.4 V (W)\n(typical module, LPF MC 99 %, key-down)")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), fontsize=6.8)
    ax.set_title("The clamp at 8.4 V: open-loop ceiling against reach\n(label: clamp top; Python replica of the p4 model)", fontsize=9)
    fig.tight_layout(w_pad=3.0)
    fig.savefig(out / "req012_basis.png", dpi=150, bbox_inches="tight")
    plt.close(fig)
    (out / "result.json").write_text(json.dumps(res, indent=1, default=float))
    L = [f"# {res['run']}: REQ-SYS-012 low-pack basis for the re-baseline CR (revision 3)", "",
         f"From p4 ({RUNS3['p4']}, D-9 as specified: VGG 3.30 to 3.50 V at 6.4 V, open-loop ceiling 8 W at 8.4 V) and p5 "
         f"({RUNS3['p5']}, clamp scenario B: VGG 3.47 to 3.50 V at 6.4 V, ceiling at the 10 W rating, 0.03 V window). "
         f"Unmodelled terms {unc_lo:+.2f} / {unc_hi:+.2f} dB. All estimates.", ""]
    for tag, rw, prop, pr in (("D-9 as specified (p4)", rows4, prop4, p4), ("Clamp scenario B (p5)", rows5, prop5, p5)):
        L += [f"## {tag}: clamp top at 8.4 V {pr['vgg_top_8v4']:.3f} V, highest module at 8.4 V {pr['module_high_8v4_all_w']:.2f} W", "",
              "| Coverage | Worst key-down case | At 6.4 V (W) | Margin to 3.97 W (dB) | With the terms (dB) | From 5 W with the terms (dB) | With the D-10 4.0 W limit (W) | At 8.4 V (W) | Pack V reaching 3.97 W in every case |",
              "|---|---|---|---|---|---|---|---|---|"]
        for r in rw:
            L.append(f"| {r['label']} | {r['worst_case']} | {r['worst_w']:.2f} | {r['margin_db']:+.2f} | {r['margin_with_terms_db'][0]:+.2f} to "
                     f"{r['margin_with_terms_db'][1]:+.2f} | {r['dev_from_5w_with_terms_db']:+.2f} | {r['delivered_with_d10_w']:.2f} | "
                     f"{r['worst_8v4_w']:.2f} | {r['pack_v_reaches_3v97_worst'] if r['pack_v_reaches_3v97_worst'] is not None else 'not by 8.4 V'} |")
        L += ["", f"Delta on the basis ({S3_BASIS}): 5 W +1/-{prop['x_db']:.1f} dB ({prop['low_end_w']:.2f} W) at 6.4 V; the -1 dB bound "
              + (f"from {prop['v_full_band']:.1f} V (limit line under the basis with the terms: {'PASS' if prop.get('limit_under_envelope_with_terms') else 'FAIL'})."
                 if prop["v_full_band"] is not None else "is not reached at any pack voltage up to 8.4 V."), ""]
    L += ["## The clamp at 8.4 V (Python replica of the p4 model)", "",
          f"Check against the deck: {res['clamp_trade']['replica_check']['high_w']:.3f} / {res['clamp_trade']['replica_check']['deck_high_w']:.3f} W highest, "
          f"{res['clamp_trade']['replica_check']['low_w']:.3f} / {res['clamp_trade']['replica_check']['deck_low_w']:.3f} W lowest.", "",
          "| Clamp top at 8.4 V (V) | Highest module, -10 C start (W) | Lowest, window 0.20 V (W) | Lowest, window 0.03 V (W) |", "|---|---|---|---|"]
    for r in res["clamp_trade"]["rows"]:
        L.append(f"| {r['top_v']:.2f} | {r['high_module_w']:.2f} | {r['low_lpf99_w_window_0.20']:.2f} | {r['low_lpf99_w_window_0.03']:.2f} |")
    L += ["", "Plot `req012_basis.png`; the verdicts of every revision 3 run in `verdicts.json`.", ""]
    (out / "result.md").write_text("\n".join(L))
    (out / "verdicts.json").write_text(json.dumps(VERDICTS, indent=1))
    copy_inputs(out, [])
    print("s3", json.dumps({"d9": {k: v for k, v in prop4.items() if k not in ("envelope_w", "limit_line_w")},
                            "b": {k: v for k, v in prop5.items() if k not in ("envelope_w", "limit_line_w")}}))
    return res

# ---------------------------------------------------------------- main
EXPECTED: dict[str, dict[str, bool]] = {  # the verdict list of the analysis record section R3.10 (2026-09-29)
    'd6': {
        'check: one .raw step per corner': True,
        'A5 lumped CLK1 pin load at most 15 pF (Si5351 Table 7)': True,
        'A5 equivalent CLK1 pin load at most 15 pF at every corner (bandpass chain)': True,
        'A5 3f at the GVA-84+ input at least 25 dB below f': True,
        'A5 GVA-84+ input below +13 dBm': True,
        'A5 module input 10 to 30 mW at every corner (fixed 18 dB pad, bandpass chain)': False,
    },
    'd7': {
        'check: 10 ps step and 400 ns settling against 20 ps and 250 ns within 0.02 dB (power) and 0.5 dB (3f)': True,
        'A5 module input at most 30 mW at any coax length (fixed pad, bandpass chain)': False,
    },
    'k1': {
        'check: one .raw step per RF case': True,
        'check: one DC sweep per diode set and temperature': True,
        'check: one bracketed equilibrium per RF case': True,
        'A5 select-on-test reading (method M2, both polarities) within the +/-1.0 dB allocation (worst-case sum)': True,
        'Revision 2 reading (forward drop at DC only, M0) within +/-1.0 dB at 25 C with no harmonic': True,
    },
    's2': {
        'A5 select-on-test drive 10 to 30 mW in service with the k1 reading bound (bandpass chain)': True,
        'A5 select-on-test drive 10 to 30 mW at the +/-1.0 dB reading allocation (bandpass chain)': True,
        'A5 select-on-test drive 10 to 30 mW with a tinySA Ultra reading alone (+/-2 dB published)': False,
    },
    'p4': {
        'check: one .raw step per corner': True,
        'check: PA case temperature equals the thermal law within 0.01 K at every pack voltage': True,
        'check: VGG 3.30 to 3.50 V at 6.4 V': True,
        'A5 open loop at 8.4 V: module output at most 8 W in every case (clamp)': True,
        'A5 open loop from 6.4 to 8.4 V: module output at most 8 W at every pack voltage and case (clamp)': True,
        'A5 nominal corner at least 3.97 W at 6.4 V in every key-down case': False,
        'A5 lowest corner (typical module, LPF at most its median) at least 3.97 W at 6.4 V, every key-down case': False,
        'A5 lowest corner (typical module, LPF worst case) at least 3.97 W at 6.4 V, every key-down case': False,
        'A5 lowest corner (typical module, LPF worst case) at least 3.97 W at 8.4 V with the clamp, every key-down case': False,
    },
    'p5': {
        'check: one .raw step per corner': True,
        'check: PA case temperature equals the thermal law within 0.01 K at every pack voltage': True,
        'check: VGG 3.47 to 3.50 V at 6.4 V': True,
        'A5 open loop at 8.4 V: module output at most 10 W in every case (clamp)': True,
        'A5 open loop from 6.4 to 8.4 V: module output at most 10 W at every pack voltage and case (clamp)': True,
        'A5 nominal corner at least 3.97 W at 6.4 V in every key-down case': False,
        'A5 lowest corner (typical module, LPF at most its median) at least 3.97 W at 6.4 V, every key-down case': False,
        'A5 lowest corner (typical module, LPF worst case) at least 3.97 W at 6.4 V, every key-down case': False,
        'A5 lowest corner (typical module, LPF worst case) at least 3.97 W at 8.4 V with the clamp, every key-down case': False,
    },
    's3': {
        'check: the proposed REQ-SYS-012 limit line lies under the basis with the unmodelled terms (clamp scenario B)': True,
        'check: the Python replica equals the p4 deck at 8.4 V within 0.5 % (highest module, lowest at the window top)': True,
        'A5 REQ-SYS-012 as baselined (5 W -1 dB at 6.4 V) on the basis (typical module, LPF MC 99th percentile, every key-down case, unmodelled terms), D-9 clamp': False,
        'A5 REQ-SYS-012 lower bound at 8.4 V on the basis, D-9 clamp as specified (8 W open-loop ceiling)': False,
        'A5 REQ-SYS-012 lower bound at 8.4 V on the basis, clamp scenario B (10 W ceiling, 0.03 V window)': True,
    },
}


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    what = args[0] if args else "all"
    order = ["d6", "d7", "k1", "s2", "p4", "p5", "s3"]
    todo = order if what == "all" else [what]
    fns = {k: globals().get(f"run_{k}") for k in order}
    fns["p5"] = lambda: run_p4("p5", CLAMPB_OFF, CLAMPB_TARGET_W, CLAMPB_LABEL)
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
