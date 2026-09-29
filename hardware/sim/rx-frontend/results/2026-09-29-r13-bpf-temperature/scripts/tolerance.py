"""Tolerance model, alignment model, port model and worst-case corner search for the rx-frontend band-pass
sections (revision 2 of docs/design/analysis/rx-bpf-ts012.md; review findings 1, 2 and 5).

Library only; the runs are made by worst_case.py. Every response is computed with bpf_nodal.py on the netlist
lines that make_decks.py writes, so the elements, values and losses are those of the LTspice decks.

Tolerance box of each section (the r01/r03 distributions, bounds used as the corners):
  mode A (TS-012 condition): end and coupling capacitors x [0.8, 1.2];
  mode B (proposed part specification): coupling capacitors +/-0.15 pF (C0G B tolerance +/-0.1 pF plus
         +/-0.05 pF of board stray), end capacitors +/-0.25 pF (C tolerance);
  both:  residual resonator tuning error after alignment RES = +/-0.3 % in frequency (estimate), drawn as
         L x [1 - 2 RES, 1 + 2 RES] = [0.994, 1.006] exactly as make_decks.py does.
Coil Q 100 (catalog minimum of the 1812SMS series; hand-wound estimate) and capacitor Q 500 (estimate) are the
loss corners; ground via 5 nH per resonator (TS-012 condition).

Alignment models (the review showed that the choice decides the result, so both are reported):
  "none"     : revision 1 model. Capacitor errors detune the resonators and the L residual is added on top,
               i.e. the capacitors are fitted after the coils were aligned, or alignment is never repeated.
  "at50"     : each resonator is re-tuned after assembly (coil turns squeezed on the NanoVNA) so that its node,
               with the neighbouring nodes shorted (Dishal's method), resonates at f0 with the section between
               50 ohm ports; the residual RES remains. The L multiplier is (residual) x C_node,nominal / C_node,actual.
  "incircuit": the same, with the section's real port admittances (J310 input, J310 drain) in place.
Alignment cannot correct coupling or external-Q errors; it only removes resonator detuning.

Ports: a shunt R and a shunt C at each port (source side: R_s || C_s behind the source; load side R_l || C_l).
"""
import itertools, math
import numpy as np
from scipy.optimize import minimize
from bpf_design import synth, netlist_block
import bpf_nodal as bn

L_RES = 56e-9
QC = 500
LVIA = 5e-9
RES = 0.003
BW = 6e6


class Port:
    def __init__(self, r=50.0, c=0.0, label=None):
        self.r, self.c = r, c
        self.label = label or (f"{r:g} ohm" + (f" || {c*1e12:g} pF" if c else ""))

    def __repr__(self):
        return self.label


P50 = Port(50.0, 0.0, "50 ohm")


class Section:
    """One band-pass section: n resonators, index k (1 = BPF1), tolerance mode, residual RES."""

    def __init__(self, n, k, mode="B", res=RES, bw=BW, lmap="first", shift=(0.0, 0.0), cwiden=0.0):
        """lmap "first" (r08 to r12): L x [1 - 2 res, 1 + 2 res]. lmap "exact" (r13, review iteration 3 finding-16):
        the resonator frequency multiplier after alignment and drift is [(1 - res)(1 + shift[0]), (1 + res)(1 + shift[1])],
        so L x [((1 + res)(1 + shift[1]))^-2, ((1 - res)(1 + shift[0]))^-2]; shift is the post-alignment temperature
        drift of the resonator frequency (r13). cwiden widens the coupling and end capacitor box by the relative
        post-alignment capacitor drift (r13): bounds (1 - a)(1 - cwiden), (1 + a)(1 + cwiden)."""
        self.n, self.k, self.mode, self.res = n, k, mode, res
        self.lmap, self.shift, self.cwiden = lmap, tuple(shift), cwiden
        if lmap == "first" and (shift != (0.0, 0.0) or cwiden):
            raise ValueError("shift and cwiden need lmap='exact'")
        self.d = d = synth(n, bw, 0.1, L_RES)
        self.bounds = {}
        self.kind = {}

        def tol(kind, prefix, i):
            if kind not in ("ck", "cs", "l"):
                return None
            key = f"m{kind}{prefix}{i}"
            if key not in self.bounds:
                if kind in ("ck", "cs"):
                    if mode == "A":
                        a = 0.2
                    elif mode == "B":
                        c = d["ck"][i] if kind == "ck" else (d["cs_in"] if i == 0 else d["cs_out"])
                        a = (0.15e-12 if kind == "ck" else 0.25e-12) / c
                    elif mode == "0":
                        a = 0.0
                    else:
                        raise ValueError(mode)
                    self.bounds[key] = ((1 - a) * (1 - cwiden), (1 + a) * (1 + cwiden))
                elif lmap == "first":
                    # res is a frequency residual; L carries twice it (f ~ L^-1/2), as make_decks.py draws it
                    self.bounds[key] = (1 - 2 * res, 1 + 2 * res)
                elif lmap == "exact":
                    self.bounds[key] = (((1 + res) * (1 + self.shift[1])) ** -2, ((1 - res) * (1 + self.shift[0])) ** -2)
                else:
                    raise ValueError(lmap)
                self.kind[key] = (kind, i)
            return key

        self.lines = netlist_block(d, f"b{k}", "i", "o", tol=tol)
        self.keys = list(self.bounds)
        self.w0 = 2 * math.pi * d["f0"]

    def base_ns(self, qu=100.0):
        return dict(QU=qu, QC=QC, LVIA=LVIA)

    # ---- alignment -------------------------------------------------------------------------------
    def _end_c(self, cs, port):
        w0 = self.w0
        zp = 1.0 / (1.0 / np.asarray(port.r, float) + 1j * w0 * np.asarray(port.c, float))
        y = 1.0 / (1.0 / (1j * w0 * cs) + zp)
        return y.imag / w0

    def node_c(self, mult, pin, pout):
        """Node capacitance of every resonator with the neighbours shorted (drawn capacitor multipliers)."""
        d, k, n = self.d, self.k, self.n
        g = lambda key: mult.get(key, 1.0)
        out = []
        for i in range(n):
            c = d["csh"][i]
            if i > 0:
                c = c + d["ck"][i - 1] * g(f"mckb{k}{i-1}")
            if i < n - 1:
                c = c + d["ck"][i] * g(f"mckb{k}{i}")
            if i == 0:
                c = c + self._end_c(d["cs_in"] * g(f"mcsb{k}0"), pin)
            if i == n - 1:
                c = c + self._end_c(d["cs_out"] * g(f"mcsb{k}1"), pout)
            out.append(c)
        return out

    def ns_for(self, mult, align="at50", pin=P50, pout=P50, qu=100.0):
        """Parameter namespace for multipliers mult (dict key -> value or array). The L entries of mult are the
        residual; with alignment they are scaled by C_node,ref / C_node,actual where the reference is the
        nominal section between 50 ohm ports (the synthesis condition)."""
        ns = self.base_ns(qu)
        for key in self.keys:
            ns[key] = np.asarray(mult.get(key, 1.0), float)
        if align != "none":
            ref = self.node_c({}, P50, P50)
            if align == "at50":
                act = self.node_c(ns, P50, P50)
            elif align == "incircuit":
                act = self.node_c(ns, pin, pout)
            else:
                raise ValueError(align)
            for i in range(self.n):
                key = f"mlb{self.k}{i}"
                ns[key] = ns[key] * ref[i] / act[i]
        return ns

    def resp_db(self, freqs, mult, align="at50", pin=P50, pout=P50, qu=100.0, cst=0.0, phi=0.0):
        ns = self.ns_for(mult, align, pin, pout, qu)
        return bn.s21_db(self.lines, freqs, ns, rs=pin.r, rl=pout.r, cin=pin.c, cout=pout.c, cst=cst, phi=phi)

    def vertices(self):
        keys = self.keys
        V = np.array(list(itertools.product((0, 1), repeat=len(keys))))
        mult = {key: np.where(V[:, j] == 1, self.bounds[key][1], self.bounds[key][0]) for j, key in enumerate(keys)}
        return V, mult

    def draws(self, rng, n):
        return {key: rng.uniform(lo, hi, n) for key, (lo, hi) in self.bounds.items()}


def chain_sections(spec, mode, res=RES, **kw):
    return [Section(n, k, mode, res, **kw) for k, n in enumerate(spec, 1)]


def tune_grid(step=100e3):
    """Tuned frequencies 144.000 to 148.000 MHz; TC-SYS-021 asks for 100 kHz spacing."""
    return np.round(np.arange(144.0e6, 148.0e6 + 1, step))


def rejection_matrix(sec, tune, IF, mult, **kw):
    """Section rejection R_k(f) = S21(f) - S21(f - 2 IF) in dB, shape (..., len(tune))."""
    fr = np.concatenate([tune, tune - 2 * IF])
    h = sec.resp_db(fr, mult, **kw)
    return h[..., :len(tune)] - h[..., len(tune):], h[..., :len(tune)]


def worst_corner(sec, tune, IF, polish_at=None, n_random=12, seed=1, **kw):
    """Worst-case corner of one section: for every tuned frequency, the minimum of R_k over the vertices of
    the tolerance box, then a bounded local minimisation (L-BFGS-B, numerical gradient) from the best vertex
    and from n_random random interior points at the tuned frequencies in polish_at. Returns dict with
    rmin (per tuned f, vertex search), the vertex index per f, and the polished minimum per polish f."""
    V, mult = sec.vertices()
    R, _ = rejection_matrix(sec, tune, IF, mult, **kw)
    iv = np.argmin(R, axis=0)
    out = {"rmin_vertex": R.min(axis=0), "vertex_index": iv, "vertices": V, "polish": {}}
    keys = sec.keys
    lo = np.array([sec.bounds[k][0] for k in keys]); hi = np.array([sec.bounds[k][1] for k in keys])
    for f in (polish_at if polish_at is not None else []):
        j = int(np.argmin(np.abs(tune - f)))
        ff = np.array([tune[j]])

        def obj(x):
            m = {k: x[i] for i, k in enumerate(keys)}
            r, _ = rejection_matrix(sec, ff, IF, m, **kw)
            return float(np.ravel(r)[0])

        x0s = [np.where(V[iv[j]] == 1, hi, lo)]
        rng = np.random.default_rng(seed)
        x0s += [rng.uniform(lo, hi) for _ in range(n_random)]
        best = (np.inf, None)
        span = np.where(hi > lo, hi - lo, 1.0)
        for x0 in x0s:
            # optimise in normalised coordinates so the numerical gradient step suits every parameter
            u0 = np.where(hi > lo, (x0 - lo) / span, 0.0)
            res = minimize(lambda u: obj(lo + u * span), u0, method="L-BFGS-B", bounds=[(0, 1)] * len(keys),
                           options={"eps": 1e-4, "maxiter": 200})
            if res.fun < best[0]:
                best = (res.fun, lo + res.x * span)
        out["polish"][float(tune[j])] = {"r_db": best[0], "x": {k: float(best[1][i]) for i, k in enumerate(keys)},
                                         "vertex_r_db": float(R[iv[j], j])}
    return out


def corner_mult(sec, vertex_row):
    return {key: (sec.bounds[key][1] if vertex_row[j] == 1 else sec.bounds[key][0]) for j, key in enumerate(sec.keys)}


def loss_corner(sec, tune, **kw):
    """Worst in-band loss corner of one section over the tolerance box (vertex search): returns the maximum
    over vertices of the worst in-band loss, and the vertex."""
    V, mult = sec.vertices()
    h = sec.resp_db(tune, mult, **kw)
    loss = -h.min(axis=-1)
    i = int(np.argmax(loss))
    return float(loss[i]), V[i]


def clopper_pearson(k, n, conf=0.95):
    """Two-sided Clopper-Pearson interval for a binomial fraction (k failures of n)."""
    from scipy.stats import beta
    a = 1 - conf
    lo = 0.0 if k == 0 else beta.ppf(a / 2, k, n - k + 1)
    hi = 1.0 if k == n else beta.ppf(1 - a / 2, k + 1, n - k)
    return float(lo), float(hi)


def zero_fail_upper(n, conf=0.95):
    """One-sided upper confidence bound on the failure fraction after 0 failures in n runs: 1 - (1-conf)^(1/n)."""
    return 1 - (1 - conf) ** (1.0 / n)


def n_for_zero_fail(p, conf=0.95):
    return int(math.ceil(math.log(1 - conf) / math.log(1 - p)))
