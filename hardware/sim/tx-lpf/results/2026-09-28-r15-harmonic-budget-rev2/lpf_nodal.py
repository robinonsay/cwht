"""Nodal (MNA) model of the LTspice filter deck, for the worst-case corner search (revision 2).

Same circuit as run_lpf.filter_real(): 50 ohm source (2 V) and load; each shunt capacitor is its pad
capacitance to ground in parallel with C + ESR + ESL + via L; each coil is trace L/2, then (L + R) in
parallel with Cpar (+ fringe), then trace L/2; the three coil inductances are mutually coupled by K24,
K46 and K26 (M = K sqrt(L1 L2), the LTspice K statement), and CIO joins the input and the output node.

Unknowns: 10 node voltages (in, a1, a2, out; y1 and y3 of each coil) and 3 coil branch currents.
Used only to search for the parameter corners; every verdict comes from LTspice runs of the corners it
finds. Its agreement with LTspice is a known-answer check of run_lpf.py (every Monte Carlo step of the
revision 2 runs is recomputed here and compared with the .raw).
"""
from __future__ import annotations

import numpy as np

import lpf_model as M

NODES = ["in", "a1", "a2", "out", "y1_2", "y3_2", "y1_4", "y3_4", "y1_6", "y3_6"]
NI = {n: k for k, n in enumerate(NODES)}
NN = len(NODES)
COILS = [(2, "in", "a1"), (4, "a1", "a2"), (6, "a2", "out")]
CAPS = [(1, "in"), (3, "a1"), (5, "a2"), (7, "out")]


def s_params(f, p: dict) -> tuple[np.ndarray, np.ndarray]:
    """(S21, S11) at the frequencies f (Hz) for a deck-parameter dict p. S21 = V(out), S11 = V(in) - 1."""
    w = 2 * np.pi * np.asarray(f, dtype=float)
    nf = w.size
    jw = 1j * w
    size = NN + 3
    A = np.zeros((nf, size, size), dtype=complex)
    rhs = np.zeros((nf, size), dtype=complex)

    def gadd(a, b, y):
        ia = NI[a] if a != "0" else None
        ib = NI[b] if b != "0" else None
        if ia is not None:
            A[:, ia, ia] += y
        if ib is not None:
            A[:, ib, ib] += y
        if ia is not None and ib is not None:
            A[:, ia, ib] -= y
            A[:, ib, ia] -= y

    # source (Norton: 2 V behind 50 ohm) and load
    gadd("in", "0", np.full(nf, 1 / M.Z0, dtype=complex))
    rhs[:, NI["in"]] = 2.0 / M.Z0
    gadd("out", "0", np.full(nf, 1 / M.Z0, dtype=complex))
    # shunt capacitors
    for n, node in CAPS:
        c = f"C{n}"
        z = p[c + "ESR"] + 1 / (jw * p[c + "C"]) + jw * (p[c + "ESL"] + p[c + "Lvia"])
        gadd(node, "0", jw * p[c + "Cpad"] + 1 / z)
    # coils: trace halves, Cpar, coupled branch (L + R) from y1 to y3
    Ls = {}
    for k, (n, a, b) in enumerate(COILS):
        ln = f"L{n}"
        y1, y3 = f"y1_{n}", f"y3_{n}"
        ltr = p[ln + "Ltr"] / 2
        gadd(a, y1, 1 / (jw * ltr))
        gadd(y3, b, 1 / (jw * ltr))
        gadd(y1, y3, jw * p[ln + "C"])
        ct = p.get(ln + "Ct", 0.0)
        if ct:
            # optional trap capacitor across the coil (screen of revision 2 section 7): C + ESR + ESL
            zt = p.get(ln + "CtESR", 0.2) + jw * p.get(ln + "CtESL", 1.0e-9) + 1 / (jw * ct)
            gadd(y1, y3, 1 / zt)
        Ls[n] = p[ln + "L"]
        br = NN + k
        A[:, NI[y1], br] += 1
        A[:, NI[y3], br] -= 1
        A[:, br, NI[y1]] += 1
        A[:, br, NI[y3]] -= 1
        A[:, br, br] -= p[ln + "R"] + jw * p[ln + "L"]
    kk = {(2, 4): p["K24"], (4, 6): p["K46"], (2, 6): p["K26"]}
    idx = {2: NN, 4: NN + 1, 6: NN + 2}
    for (a, b), kv in kk.items():
        m = kv * np.sqrt(Ls[a] * Ls[b])
        A[:, idx[a], idx[b]] -= jw * m
        A[:, idx[b], idx[a]] -= jw * m
    gadd("in", "out", jw * p["Cio"])
    x = np.linalg.solve(A, rhs[..., None])[..., 0]
    return x[:, NI["out"]], x[:, NI["in"]] - 1.0


def db(x):
    return 20 * np.log10(np.maximum(np.abs(x), 1e-30))
