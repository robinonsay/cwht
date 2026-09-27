#!/usr/bin/env python3
"""TS-007 decision matrix, phase-noise derivations, battery-life deltas and the sensitivity runs
of 06 section 14.4 (weight +/-10 on each criterion; each Low-confidence cell +/-1).

Product: docs/decisions/trade-studies/TS-007-synthesizer-and-reference.md sections 4 to 6 and
Appendix A. Run from the repository root:

    .venv/bin/python hardware/sim/freq/ts007_matrix.py [--plot]

Exit 0 when the recomputed totals equal the totals written in the study (constants TOTALS below)
and the robustness verdict printed equals VERDICT; exit 1 otherwise. Standard library only for
the numbers; matplotlib renders the figure. Class B script without a TV record: developer
evidence (05 section 9.1).
"""
from __future__ import annotations

import argparse
import math
import sys
from fractions import Fraction as F
from pathlib import Path

# --- Criteria and weights (TS-007 section 3.1) ---
CRIT = ["C1", "C2", "C3", "C4", "C5", "C6", "C7"]
NAMES = {
    "C1": "Phase noise at 144 MHz",
    "C2": "Supply current of the frequency-generation block",
    "C3": "Specified spurious output",
    "C4": "Tuning and changeover behaviour",
    "C5": "Firmware and driver effort",
    "C6": "First-power-on confidence",
    "C7": "70 cm output capability",
}
W = {"C1": 35, "C2": 20, "C3": 10, "C4": 10, "C5": 10, "C6": 10, "C7": 5}
# --- Scores and confidence (TS-007 section 4) ---
S = {
    "A1": {"C1": 2, "C2": 5, "C3": 1, "C4": 3, "C5": 5, "C6": 3, "C7": 1},
    "A2": {"C1": 5, "C2": 2, "C3": 5, "C4": 3, "C5": 3, "C6": 3, "C7": 5},
}
CONF = {
    "A1": {"C1": "Low", "C2": "Medium", "C3": "Low", "C4": "Low", "C5": "Medium", "C6": "Low", "C7": "High"},
    "A2": {"C1": "Medium", "C2": "Medium", "C3": "High", "C4": "Low", "C5": "Medium", "C6": "Low", "C7": "High"},
}
TOTALS = {"A1": 295, "A2": 380}
VERDICT = "Robust"
# Cost-in variant (section 6 item 7): cost criterion C8 at weight 15, others rescaled to 85.
COST_SCORE = {"A1": 5, "A2": 1}

# --- Phase-noise derivations (section 4, C1) ---
PN_QCX_HF = (-135.6, 7.0e6)       # F17: QCX -135.6 dBc/Hz at 10 kHz; carrier band not stated in F17: 7.0 MHz assumed (40 m)
PN_QCX_HF_20M = (-135.6, 14.0e6)  # same figure if the measured QCX was a 20 m unit (upper end of the range)
PN_KE5FX = (-127.0, 19.99e6)      # F17: -127 dBc/Hz at 10 kHz at 19.99 MHz
PN_SI_VHF_REPORT = -112.0         # F17: unverified secondary report at 156.2 MHz
PN_LMX_480 = (-123.0, 480e6, 12.5e3)   # F20: -123 dBc/Hz at 12.5 kHz at 480 MHz (datasheet)
LMX_NORM_FLOOR = -231.0           # F20: normalized PLL floor
LMX_NORM_FLICKER = -124.0         # F20: normalized 1/f (1 GHz carrier, 10 kHz offset convention)
F_PFD = 25e6                      # TCXO 25 MHz, no doubler (assumption)
F_OUT = 144e6
BW_DB = 10 * math.log10(500)      # 500 Hz CW bandwidth (REQ-SYS-031 "in 500 Hz")
RMDR_REQ = 85.0                   # REQ-SYS-031 (TBR)
BLOCK_2K = -60.0                  # REQ-SYS-029: -60 dBm at 2 kHz
MDS = -140.0                      # REQ-SYS-022 (TBR): noise in 500 Hz

# --- Battery-life model of docs/research/power-tree-and-charging.md F23 (expected scenario) ---
V_NOM, CAP, USABLE, EFF, KEY = 7.2, 3.0, 0.90, 0.90, 0.45
I5_EXPECTED_LMX = 0.260           # F23 "expected": LMX2571 (39 mA) included, A on 5 V bus
I_LMX = 0.039                     # F20: 39 mA in synthesizer mode
I_SI3, I_SI1 = 0.030, 0.026       # Table 2 of the reference report: 24 mA core + 2 mA per output (3 outputs; 1 output)
I_ADF = 0.150                     # F18: ADF4351 about 120 to 170 mA; midpoint (pruned alternative)
IBIAS, IPA = 0.250, 1.30


def pn_scale(pn, f_from, f_to):
    return pn + 20 * math.log10(f_to / f_from)


def phase_noise():
    si_qcx = pn_scale(PN_QCX_HF[0], PN_QCX_HF[1], F_OUT)
    si_ke = pn_scale(PN_KE5FX[0], PN_KE5FX[1], F_OUT)
    lmx_direct = pn_scale(PN_LMX_480[0], PN_LMX_480[1], F_OUT)
    floor = LMX_NORM_FLOOR + 20 * math.log10(F_OUT) - 10 * math.log10(F_PFD)
    flick = lambda off: LMX_NORM_FLICKER + 20 * math.log10(F_OUT / 1e9) - 10 * math.log10(off / 1e4)
    comb = lambda off: 10 * math.log10(10 ** (floor / 10) + 10 ** (flick(off) / 10))
    return {
        "Si5351A from QCX HF (F17), 10 kHz, 7 MHz assumed": si_qcx,
        "Si5351A from QCX HF (F17), 10 kHz, 14 MHz assumed": pn_scale(PN_QCX_HF_20M[0], PN_QCX_HF_20M[1], F_OUT),
        "Si5351A from KE5FX 20 MHz (F17), 10 kHz": si_ke,
        "Si5351A secondary report (F17, 156 MHz), 10 kHz": PN_SI_VHF_REPORT,
        "LMX2571 datasheet 480 MHz scaled (F20), 12.5 kHz": lmx_direct,
        "LMX2571 in-band normalized model (F20), 10 kHz": comb(1e4),
        "LMX2571 in-band normalized model (F20), 2 kHz": comb(2e3),
    }


def rmdr(pn):
    return -pn - BW_DB


def l2k_limit():
    """Largest L(2 kHz) that keeps REQ-SYS-029 (loss of a -130 dBm signal <= 3 dB)."""
    # (S+N)/N initial with S = 10 N: 11; allowed (S+N+X)/(N+X) = 11 / 10**0.3; X is reciprocal-mixing noise
    r = 11 / (10 ** 0.3)
    x_over_n = (11 - r) / (r - 1)
    x_dbm = MDS + 10 * math.log10(x_over_n)
    return x_dbm - BLOCK_2K - BW_DB


def life(i5):
    irx = i5 * 5.0 / (V_NOM * EFF)
    itx = irx + IBIAS + KEY * IPA
    ah = CAP * USABLE
    return ah / (0.1 * itx + 0.9 * irx)


def battery():
    base = I5_EXPECTED_LMX - I_LMX
    return {"A1 (Si5351A, 3 outputs)": (base + I_SI3, life(base + I_SI3)),
            "A2 (LMX2571 + Si5351A BFO, 1 output)": (base + I_LMX + I_SI1, life(base + I_LMX + I_SI1)),
            "pruned: ADF4351 + Si5351A BFO": (base + I_ADF + I_SI1, life(base + I_ADF + I_SI1)),
            "F23 expected (LMX2571 only, reference)": (I5_EXPECTED_LMX, life(I5_EXPECTED_LMX))}


def total(alt, w=W, s=S, extra=None):
    t = F(0)
    for c in w:
        sc = s[alt][c] if c in s[alt] else extra[alt]
        t += F(w[c]) * sc
    return t


def rescaled(c_changed, delta):
    """Weight of c_changed moved by delta (clamped at 0), the others rescaled to keep 100."""
    new_c = max(0, W[c_changed] + delta)
    rest = 100 - W[c_changed]
    factor = F(100 - new_c, rest)
    w = {c: (F(new_c) if c == c_changed else F(W[c]) * factor) for c in W}
    return w


def sensitivity():
    rows = []
    flips = []
    base_top = max(S, key=lambda a: total(a))
    for c in CRIT:
        for d in (+10, -10):
            w = rescaled(c, d)
            t = {a: total(a, w) for a in S}
            top = max(t, key=t.get)
            rows.append((f"weight {c} {d:+d}", t, top))
            if top != base_top:
                flips.append(rows[-1][0])
    for a in S:
        for c in CRIT:
            if CONF[a][c] != "Low":
                continue
            for d in (+1, -1):
                s2 = {x: dict(S[x]) for x in S}
                s2[a][c] = min(5, max(1, s2[a][c] + d))
                t = {x: total(x, W, s2) for x in S}
                top = max(t, key=t.get)
                rows.append((f"cell {c}-{a} {d:+d}", t, top))
                if top != base_top:
                    flips.append(rows[-1][0])
    # combined worst case for the recommendation: every Low cell of A1 +1 and of A2 -1
    s3 = {x: dict(S[x]) for x in S}
    for c in CRIT:
        if CONF["A1"][c] == "Low":
            s3["A1"][c] = min(5, s3["A1"][c] + 1)
        if CONF["A2"][c] == "Low":
            s3["A2"][c] = max(1, s3["A2"][c] - 1)
    t = {x: total(x, W, s3) for x in S}
    tops = [x for x in t if t[x] == max(t.values())]
    rows.append(("combined (beyond 14.4): all Low cells against the leader", t, "tie" if len(tops) > 1 else tops[0]))
    # cost-in variant
    w_cost = {c: F(W[c]) * F(85, 100) for c in W}
    w_cost["C8"] = F(15)
    t = {a: total(a, w_cost, extra=COST_SCORE) for a in S}
    rows.append(("cost-in variant (C8 cost weight 15)", t, max(t, key=t.get)))
    return base_top, rows, flips


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--plot", action="store_true")
    a = ap.parse_args(argv)
    rc = 0
    assert sum(W.values()) == 100, "weights must sum to 100"
    print("PHASE NOISE (dBc/Hz at 144 MHz) and RMDR in 500 Hz:")
    for k, v in phase_noise().items():
        print(f"  {k}: {v:.1f} dBc/Hz, RMDR {rmdr(v):.1f} dB (REQ-SYS-031 85 dB: margin {rmdr(v) - RMDR_REQ:+.1f} dB)")
    print(f"  REQ-SYS-029 limit on L(2 kHz): {l2k_limit():.1f} dBc/Hz")
    print("BATTERY LIFE, F23 expected-scenario model (1:9):")
    for k, (i5, h) in battery().items():
        print(f"  {k}: 5 V bus {i5*1000:.0f} mA, life {math.floor(h*10)/10:.1f} h (TPM-008 PDR margin 9.6 h, threshold 8 h)")
    print("TOTALS:")
    for alt in S:
        t = total(alt)
        ok = t == TOTALS[alt]
        rc |= (not ok)
        print(f"  {alt}: {t} ({float(t)/5:.1f} %) {'matches' if ok else 'DIFFERS FROM'} study value {TOTALS[alt]}")
    top, rows, flips = sensitivity()
    print("SENSITIVITY (06 section 14.4):")
    for name, t, tp in rows:
        print(f"  {name}: " + ", ".join(f"{x} {float(v):.1f}" for x, v in t.items()) + f" -> top {tp}")
    verdict = "Robust" if not flips else "Not robust"
    print(f"VERDICT: {verdict} (top {top}; rank changes: {flips if flips else 'none'})")
    rc |= (verdict != VERDICT)
    if a.plot:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(12.5, 5.8))
        names = [r[0] for r in rows]
        a1 = [float(r[1]["A1"]) for r in rows]
        a2 = [float(r[1]["A2"]) for r in rows]
        y = range(len(rows))
        ax.barh([i + 0.2 for i in y], a2, height=0.4, label="A2 LMX2571 + Si5351A BFO")
        ax.barh([i - 0.2 for i in y], a1, height=0.4, label="A1 Si5351A only")
        ax.axvline(float(total("A2")), color="tab:blue", ls=":", lw=0.8)
        ax.axvline(float(total("A1")), color="tab:orange", ls=":", lw=0.8)
        ax.set_yticks(list(y))
        ax.set_yticklabels(names, fontsize=7)
        ax.invert_yaxis()
        ax.set_xlabel("weighted total (maximum 500); dotted lines = baseline totals")
        ax.set_title(f"TS-007 sensitivity runs (06 section 14.4): verdict {verdict}, developer evidence", fontsize=10)
        ax.legend(fontsize=8, loc="upper left", bbox_to_anchor=(1.01, 1.0))
        ax.grid(alpha=0.3, axis="x")
        fig.tight_layout()
        out = Path("docs/reviews/PDR/figures/ts-007-sensitivity.png")
        fig.savefig(out, dpi=130)
        print(f"figure: {out}")
    return rc


if __name__ == "__main__":
    sys.exit(main())
