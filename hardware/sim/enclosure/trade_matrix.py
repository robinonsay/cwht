#!/usr/bin/env python3
"""Weighted decision matrices and the 06 section 14.4 sensitivity runs for TS-011 and TS-004.

Matrices: TS-011 main (alternatives surviving the mandatory screen), TS-011 fabrication and
marking route (OD-38), TS-004 thickness and via fill (surviving alternative plus the relaxed-screen
run of TS-004 section 6 item 3), TS-004 panelization. For each matrix: weighted totals (maximum
500), rank, weight sensitivity (each weight +10 and -10, clamped at 0, others rescaled to keep the
sum 100), and score sensitivity (each Low-confidence cell +1 and -1 within 1 to 5).
Scores, confidences and evidence are tabulated in the study files; this script only computes.
Run: .venv/bin/python hardware/sim/enclosure/trade_matrix.py [--check]
Writes hardware/sim/enclosure/out/trade-matrix.txt. --check exits 1 if a total, the top rank or a
robustness verdict differs from EXPECTED (the values stated in the studies).
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "hardware/sim/enclosure/out/trade-matrix.txt"

# Each matrix: criteria [(id, weight)], alternatives {alt: {crit: (score, confidence)}}
MATRICES = {
    "TS-011 main": dict(
        criteria=[("C1 cost", 25), ("C2 schedule", 15), ("C3 thermal margin", 15), ("C4 low-frequency shielding", 10),
                  ("C5 port retention", 10), ("C6 marking route", 10), ("C7 iteration cost", 10), ("C8 pre-build evidence", 5)],
        alts={
            "A": {"C1 cost": (1, "L"), "C2 schedule": (1, "M"), "C3 thermal margin": (4, "L"), "C4 low-frequency shielding": (5, "M"),
                  "C5 port retention": (5, "M"), "C6 marking route": (3, "M"), "C7 iteration cost": (1, "M"),
                  "C8 pre-build evidence": (3, "M")},
            "C1": {"C1 cost": (2, "L"), "C2 schedule": (5, "M"), "C3 thermal margin": (1, "L"), "C4 low-frequency shielding": (1, "L"),
                   "C5 port retention": (3, "L"), "C6 marking route": (5, "M"), "C7 iteration cost": (4, "M"),
                   "C8 pre-build evidence": (5, "M")},
            "D": {"C1 cost": (2, "L"), "C2 schedule": (4, "L"), "C3 thermal margin": (2, "L"), "C4 low-frequency shielding": (1, "L"),
                  "C5 port retention": (3, "L"), "C6 marking route": (5, "M"), "C7 iteration cost": (4, "L"),
                  "C8 pre-build evidence": (5, "M")},
        }),
    "TS-011 route (OD-38)": dict(
        criteria=[("R1 cost", 30), ("R2 lead time and vendor independence", 25), ("R3 pre-build marking verification", 20),
                  ("R4 durability and legibility", 25)],
        alts={
            "Ra": {"R1 cost": (5, "M"), "R2 lead time and vendor independence": (5, "H"), "R3 pre-build marking verification": (5, "H"),
                   "R4 durability and legibility": (4, "L")},
            "Rb": {"R1 cost": (2, "L"), "R2 lead time and vendor independence": (2, "M"), "R3 pre-build marking verification": (3, "M"),
                   "R4 durability and legibility": (2, "L")},
            "Rc": {"R1 cost": (1, "L"), "R2 lead time and vendor independence": (1, "M"), "R3 pre-build marking verification": (3, "M"),
                   "R4 durability and legibility": (3, "L")},
        }),
    "TS-004 thickness and via fill (relaxed screen, all four)": dict(
        criteria=[("K1 via-array resistance", 35), ("K2 stiffness", 15), ("K3 cost", 20), ("K4 lead time", 10), ("K5 assembly risk", 20)],
        alts={
            "T1": {"K1 via-array resistance": (5, "M"), "K2 stiffness": (3, "M"), "K3 cost": (3, "L"), "K4 lead time": (3, "L"),
                   "K5 assembly risk": (5, "M")},
            "T2": {"K1 via-array resistance": (1, "M"), "K2 stiffness": (5, "M"), "K3 cost": (3, "L"), "K4 lead time": (3, "L"),
                   "K5 assembly risk": (5, "M")},
            "T3": {"K1 via-array resistance": (2, "L"), "K2 stiffness": (3, "M"), "K3 cost": (5, "L"), "K4 lead time": (5, "L"),
                   "K5 assembly risk": (2, "M")},
            "T4": {"K1 via-array resistance": (2, "M"), "K2 stiffness": (3, "M"), "K3 cost": (3, "L"), "K4 lead time": (3, "L"),
                   "K5 assembly risk": (5, "M")},
        }),
    "TS-004 panelization": dict(
        criteria=[("P-a assembly acceptance", 40), ("P-b layout freedom", 30), ("P-c depanel finish", 15), ("P-d cost", 15)],
        alts={
            "P1": {"P-a assembly acceptance": (5, "M"), "P-b layout freedom": (5, "H"), "P-c depanel finish": (3, "M"),
                   "P-d cost": (4, "L")},
            "P2": {"P-a assembly acceptance": (3, "L"), "P-b layout freedom": (2, "H"), "P-c depanel finish": (5, "M"),
                   "P-d cost": (5, "L")},
        }),
}

EXPECTED = {
    "TS-011 main": dict(totals={"A": 255, "C1": 295, "D": 295}, robust=False),
    "TS-011 route (OD-38)": dict(totals={"Ra": 475, "Rb": 220, "Rc": 190}, top="Ra", robust=True),
    "TS-004 thickness and via fill (relaxed screen, all four)": dict(totals={"T1": 410, "T2": 300, "T3": 305, "T4": 305},
                                                                     top="T1", robust=True),
    "TS-004 panelization": dict(totals={"P1": 455, "P2": 330}, top="P1", robust=True),
}


def totals(criteria, alts, weights=None, override=None):
    w = weights or {c: wt for c, wt in criteria}
    out = {}
    for a, cells in alts.items():
        tot = 0.0
        for c, _ in criteria:
            s = cells[c][0]
            if override and (a, c) in override:
                s = override[(a, c)]
            tot += w[c] * s
        out[a] = tot
    return out


def top_set(tot):
    best = max(tot.values())
    return sorted(a for a, v in tot.items() if abs(v - best) < 1e-9)


def rescale(criteria, target, delta):
    base = {c: float(wt) for c, wt in criteria}
    new_t = max(0.0, base[target] + delta)
    others = sum(v for c, v in base.items() if c != target)
    k = (100.0 - new_t) / others
    return {c: (new_t if c == target else v * k) for c, v in base.items()}


def analyse(name, m):
    lines = [f"== {name}"]
    crit, alts = m["criteria"], m["alts"]
    assert sum(w for _, w in crit) == 100, f"{name}: weights do not sum to 100"
    base = totals(crit, alts)
    top0 = top_set(base)
    ranked = sorted(base.items(), key=lambda kv: -kv[1])
    lines.append("totals: " + ", ".join(f"{a} {v:.0f} ({v / 5:.1f} %)" for a, v in ranked))
    lines.append(f"top: {top0}")
    changes = []
    for c, _ in crit:
        for d in (10, -10):
            t = totals(crit, alts, weights=rescale(crit, c, d))
            ts = top_set(t)
            if ts != top0:
                changes.append(f"weight {c} {d:+d}: top {ts} ({', '.join(f'{a} {v:.1f}' for a, v in t.items())})")
    for a, cells in alts.items():
        for c, (s, conf) in cells.items():
            if conf != "L":
                continue
            for d in (1, -1):
                ns = min(5, max(1, s + d))
                if ns == s:
                    continue
                t = totals(crit, alts, override={(a, c): ns})
                ts = top_set(t)
                if ts != top0:
                    changes.append(f"score {a}/{c} {s}->{ns}: top {ts} ({', '.join(f'{x} {v:.0f}' for x, v in t.items())})")
    robust = not changes and len(top0) == 1
    lines.append("perturbations that change the top rank: " + ("none" if not changes else ""))
    lines += [f"  {x}" for x in changes]
    lines.append(f"robustness: {'Robust' if robust else 'Not robust'}")
    return base, top0, robust, lines


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    all_lines, errs = [], []
    for name, m in MATRICES.items():
        base, top0, robust, lines = analyse(name, m)
        all_lines += lines + [""]
        exp = EXPECTED[name]
        for a, v in exp["totals"].items():
            if abs(base[a] - v) > 1e-9:
                errs.append(f"{name} {a}: total {base[a]}, expected {v}")
        if "top" in exp and top0 != [exp["top"]]:
            errs.append(f"{name}: top {top0}, expected {exp['top']}")
        if robust != exp["robust"]:
            errs.append(f"{name}: robust {robust}, expected {exp['robust']}")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(all_lines) + "\n")
    print("\n".join(all_lines))
    if args.check:
        for e in errs:
            print("MISMATCH:", e)
        print("CHECK", "FAIL" if errs else "PASS")
        return 1 if errs else 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
