"""Worst-case (extreme value) corner search of the TS-012 harmonic LPF (revision 2, review finding-1).

Revision 1 reported the worst of 252 Monte Carlo steps as the worst case. With about 39 independent
parameters a uniform draw almost never lands near a corner, so the sample worst is not a bound. This
module searches the full parameter box (lpf_model.param_bounds: every parameter of every part independent,
the coil couplings signed) for the instance that makes each metric worst:

    il       maximum insertion loss over 144 to 148 MHz                              (maximised)
    att2     minimum attenuation over 288 to 296 MHz                                  (minimised)
    att3     minimum attenuation over 432 to 444 MHz                                  (minimised)
    atthi    minimum attenuation over 576 MHz to 1.5 GHz (REQ-TX-011)                 (minimised)
    eff2     minimum over carriers f of A(2f) - IL(f): the second harmonic relative
             to the carrier that reaches the antenna (review finding-4)              (minimised)
    eff3     the same for 3f                                                          (minimised)
    effhi    the same for 4f to 10f                                                   (minimised)

Search, per metric: bounded quasi-Newton (scipy L-BFGS-B on the normalised box) from several starts (the
nominal, the vertex the first-order sensitivities point to, the worst Monte Carlo instances, and seeded
random vertices), each followed by a coordinate pass that tries both bounds of every parameter until no
move improves the metric. The result is the worst instance found. It is a search, not a proof of the
global worst, so run_lpf.py reports it with the stated starts and checks it in LTspice; every verdict
comes from the LTspice run of the corners found here (lpf_nodal is the fast evaluator only).
"""
from __future__ import annotations

import numpy as np
from scipy.optimize import minimize

import lpf_model as M
import lpf_nodal as N

F_PB = M.PB_FINE                                             # 144.0 .. 148.0 MHz, 0.25 MHz steps


def _band(lo, hi):
    return M.FREQS[(M.FREQS >= lo - 1) & (M.FREQS <= hi + 1)]


F_BAND = {n: _band(*M.harmonic_band(n)) for n in M.HARMONICS}   # the deck grid inside each band
F_HI_BAND = _band(576e6, 1500e6)                                  # REQ-TX-011 band on the deck grid
F_IL = _band(M.F_LO, M.F_HI)
METRICS = ("il", "att2", "att3", "atthi", "eff2", "eff3", "effhi")
SENSE = {"il": -1.0}                                         # sign applied so that the search minimises
N_RANDOM = 10
SEED = 31000


class Space:
    def __init__(self, kind: str, vals, coil_tol=None, cap_tol: float = 0.05, traps: dict | None = None):
        self.kind = kind
        self.b = M.param_bounds(kind, vals, coil_tol, cap_tol, traps)
        self.names = M.free_names(traps)
        self.lo = np.array([self.b[n][0] for n in self.names])
        self.nom = np.array([self.b[n][1] for n in self.names])
        self.hi = np.array([self.b[n][2] for n in self.names])

    def to_free(self, x) -> dict:
        v = self.lo + np.clip(x, 0, 1) * (self.hi - self.lo)
        return dict(zip(self.names, v))

    def to_x(self, free: dict) -> np.ndarray:
        v = np.array([free[n] for n in self.names])
        return np.clip((v - self.lo) / (self.hi - self.lo), 0, 1)

    def x_nom(self):
        return (self.nom - self.lo) / (self.hi - self.lo)

    def deck(self, x) -> dict:
        return M.deck_params(self.kind, self.to_free(x))


def metric_value(p: dict, metric: str) -> float:
    """Metric of one deck-parameter dict (dB, natural sense: loss or attenuation)."""
    if metric == "il":
        s21, _ = N.s_params(F_IL, p)
        return float(np.max(-N.db(s21)))
    if metric in ("att2", "att3"):
        s21, _ = N.s_params(F_BAND[2 if metric == "att2" else 3], p)
        return float(np.min(-N.db(s21)))
    if metric == "atthi":
        s21, _ = N.s_params(F_HI_BAND, p)
        return float(np.min(-N.db(s21)))
    orders = {"eff2": [2], "eff3": [3], "effhi": list(range(4, 11))}[metric]
    fs = np.concatenate([F_PB] + [n * F_PB for n in orders])
    s21, _ = N.s_params(fs, p)
    a = -N.db(s21)
    il = a[:F_PB.size]
    worst = 1e9
    for k, _n in enumerate(orders):
        seg = a[F_PB.size * (k + 1):F_PB.size * (k + 2)]
        worst = min(worst, float(np.min(seg - il)))
    return worst


def search(space: Space, metric: str, extra_starts=(), n_random: int = N_RANDOM, seed: int = SEED,
           quick: bool = False) -> dict:
    sgn = SENSE.get(metric, 1.0)

    def g(x):
        return sgn * metric_value(space.deck(x), metric)

    n = len(space.names)
    x0 = space.x_nom()
    # first-order sensitivities at the nominal: step every parameter to each bound
    base = g(x0)
    grad_vertex = np.empty(n)
    for i in range(n):
        xl, xh = x0.copy(), x0.copy()
        xl[i], xh[i] = 0.0, 1.0
        grad_vertex[i] = 0.0 if g(xl) < g(xh) else 1.0
    starts = [("nominal", x0), ("sensitivity vertex", grad_vertex)]
    for name, fr in extra_starts:
        starts.append((name, space.to_x(fr)))
    rng = np.random.default_rng(seed)
    for k in range(0 if quick else n_random):
        starts.append((f"random vertex {k + 1}", rng.integers(0, 2, n).astype(float)))
    best = None
    trail = []
    for name, xs in starts:
        r = minimize(g, xs, method="L-BFGS-B", bounds=[(0, 1)] * n,
                     options={"maxiter": 60 if quick else 200, "eps": 1e-6})
        x = np.clip(r.x, 0, 1)
        fx = g(x)
        # coordinate pass over the two bounds of every parameter
        for _sweep in range(2 if quick else 6):
            moved = False
            for i in range(n):
                for v in (0.0, 1.0):
                    if x[i] == v:
                        continue
                    xt = x.copy()
                    xt[i] = v
                    ft = g(xt)
                    if ft < fx - 1e-9:
                        x, fx, moved = xt, ft, True
            if not moved:
                break
        trail.append({"start": name, "value_dB": sgn * fx})
        if best is None or fx < best[1]:
            best = (x, fx, name)
    x, fx, name = best
    at_bound = int(np.sum((x < 1e-6) | (x > 1 - 1e-6)))
    return {"metric": metric, "value_dB": sgn * fx, "nominal_dB": sgn * base, "from_start": name,
            "free": space.to_free(x), "deck": space.deck(x), "x": x.tolist(),
            "params_at_a_bound": at_bound, "n_params": n, "starts": trail}
