"""Screen symmetric E-series value sets for a parasitic-compensated 7-pole low-pass (run r6 input).

Frequency-domain ABCD model of the same topology as the LTspice decks (shunt branch: pad C in parallel
with C + ESR + ESL + via L; series branch: trace L in series with (L + R) parallel Cpar), without the
coil-to-coil coupling and the input-output leakage (they change the stopband, not the passband loss).
Used only to choose candidate values; every verdict comes from the LTspice Monte Carlo of the chosen set.
Its agreement with LTspice is checked on the r1 nominal 1812SMS build (known answer printed by main()).
"""
from __future__ import annotations

import itertools
import math

import numpy as np

import lpf_model as M

CAPS_E24 = [15e-12, 16e-12, 18e-12, 20e-12, 22e-12, 24e-12, 27e-12, 30e-12, 33e-12, 36e-12, 39e-12, 43e-12]
COILS_1812 = [47e-9, 56e-9, 68e-9, 82e-9]


def s21(f, p: dict) -> np.ndarray:
    w = 2 * np.pi * np.asarray(f, dtype=float)
    abcd = np.tile(np.eye(2, dtype=complex), (w.size, 1, 1))
    order = ["C1", "L2", "C3", "L4", "C5", "L6", "C7"]
    for name in order:
        if name.startswith("C"):
            zc = p[name + "ESR"] + 1 / (1j * w * p[name + "C"]) + 1j * w * (p[name + "ESL"] + p[name + "Lvia"])
            y = 1 / zc + 1j * w * p[name + "Cpad"]
            m = np.zeros_like(abcd)
            m[:, 0, 0] = 1
            m[:, 1, 0] = y
            m[:, 1, 1] = 1
        else:
            zl = p[name + "R"] + 1j * w * p[name + "L"]
            zp = 1 / (1 / zl + 1j * w * p[name + "C"])
            z = zp + 1j * w * p[name + "Ltr"]
            m = np.zeros_like(abcd)
            m[:, 0, 0] = 1
            m[:, 0, 1] = z
            m[:, 1, 1] = 1
        abcd = abcd @ m
    a, b, c, d = abcd[:, 0, 0], abcd[:, 0, 1], abcd[:, 1, 0], abcd[:, 1, 1]
    return 2 / (a + b / M.Z0 + c * M.Z0 + d)


def with_values(kind: str, vals: list[float], corner: int, worst_loss: bool) -> dict:
    p = M.sample_filter(kind, None, 0.03 if kind == "air" else None, corner=corner, vals=vals)
    if worst_loss:
        for i in M.CAP_POS:
            p[f"C{i + 1}ESR"] = M.CAP_ESR[2]
    return p


def evaluate(kind: str, vals: list[float]) -> dict:
    fpb = np.linspace(M.F_LO, M.F_HI, 9)
    il = max(float(np.max(-20 * np.log10(np.abs(s21(fpb, with_values(kind, vals, c, True)))))) for c in (-1, 1))
    fs2 = np.linspace(288e6, 296e6, 5)
    fs3 = np.linspace(432e6, 444e6, 5)
    p_lo = with_values(kind, vals, -1, False)
    a2 = float(np.min(-20 * np.log10(np.abs(s21(fs2, p_lo)))))
    a3 = float(np.min(-20 * np.log10(np.abs(s21(fs3, p_lo)))))
    return {"il_worst": il, "att2_lo": a2, "att3_lo": a3}


def screen(kind: str, coils: list[float]) -> list[tuple]:
    out = []
    for c1, c3 in itertools.product(CAPS_E24, CAPS_E24):
        if c3 < c1:
            continue
        for l2, l4 in itertools.product(coils, coils):
            if kind == "1812" and (l2 not in M.COILCRAFT or l4 not in M.COILCRAFT):
                continue
            vals = [c1, l2, c3, l4, c3, l2, c1]
            e = evaluate(kind, vals)
            if e["att2_lo"] >= 45.0 and e["att3_lo"] >= 40.0:
                out.append((e["il_worst"], vals, e))
    out.sort(key=lambda t: t[0])
    return out


def main():
    # known answer against LTspice r1 (nominal 1812SMS build, couplings and leakage excluded here)
    p = M.sample_filter("1812")
    s = s21(np.array([146e6, 148e6, 288e6]), p)
    print("ABCD nominal 1812SMS BOM: S21 dB at 146, 148, 288 MHz:", np.round(20 * np.log10(np.abs(s)), 3))
    return p


if __name__ == "__main__":
    main()
