"""Coupled-resonator band-pass filter synthesis for the cwht receiver front end (WP-PDR-19, TS-012 pre-order item).

Topology (every filter): shunt parallel-LC resonators to ground, series (top) capacitor coupling between
adjacent resonators, series capacitor from each 50 ohm port into the end resonator. Element values come from
the low-pass prototype g-values by the standard coupling-coefficient method:
    k(i,i+1) = FBW / sqrt(g_i g_(i+1)),  Qe1 = g0 g1 / FBW,  Qen = g_n g_(n+1) / FBW
(Matthaei, Young and Jones, "Microwave Filters, Impedance-Matching Networks and Coupling Structures", 1964,
chapter 8; Hong and Lancaster, "Microstrip Filters for RF/Microwave Applications", 2001, eqs. 8.11 to 8.13).
The end series capacitor Cs is chosen so that 50 ohm in series with Cs, converted to parallel form, loads the end
resonator to Qe; its parallel-equivalent capacitance and the coupling capacitors are subtracted from the shunt
capacitance so that every resonator node resonates at f0 (the admittance-inverter pi of -Ck, Ck, -Ck).

Losses: coil unloaded Q (series resistance w0 L / Qu at f0), capacitor ESR from a capacitor Q (C0G at VHF,
estimate), optional ground inductance in series with each resonator's return.

This module is imported by make_decks.py (LTspice netlists, the evidence) and by explore.py (a numpy
nodal-analysis pre-check used only to choose which designs to simulate). Nothing here is a result.
"""
import math

F0 = math.sqrt(144.0e6 * 148.0e6)  # geometric centre of the 2 m band, 145.99 MHz
Z0 = 50.0


def cheby_g(n, ripple_db):
    """Chebyshev low-pass prototype g0..g(n+1) (Matthaei table formulas)."""
    if ripple_db <= 0:
        g = [1.0] + [2 * math.sin((2 * k - 1) * math.pi / (2 * n)) for k in range(1, n + 1)] + [1.0]
        return g
    beta = math.log(1 / math.tanh(ripple_db / 17.37))
    gam = math.sinh(beta / (2 * n))
    a = [math.sin((2 * k - 1) * math.pi / (2 * n)) for k in range(1, n + 1)]
    b = [gam ** 2 + math.sin(k * math.pi / n) ** 2 for k in range(1, n + 1)]
    g = [1.0, 2 * a[0] / gam]
    for k in range(2, n + 1):
        g.append(4 * a[k - 2] * a[k - 1] / (b[k - 2] * g[k - 1]))
    g.append(1.0 if n % 2 else 1 / math.tanh(beta / 4) ** 2)
    return g


def synth(n, bw_hz, ripple_db=0.1, l_res=82e-9, f0=F0):
    """Return a dict with the element values of an n-resonator top-C coupled filter."""
    g = cheby_g(n, ripple_db)
    fbw = bw_hz / f0
    w0 = 2 * math.pi * f0
    c_res = 1.0 / (w0 ** 2 * l_res)  # total node capacitance at f0
    x = w0 * l_res  # resonator reactance
    k = [fbw / math.sqrt(g[i] * g[i + 1]) for i in range(1, n)]
    ck = [ki * c_res for ki in k]
    qe_in = g[0] * g[1] / fbw
    qe_out = g[n] * g[n + 1] / fbw
    zl_out = Z0 * g[n + 1] if g[n + 1] != 1.0 else Z0  # even-order Chebyshev load (not used: we use odd or accept mismatch)

    def end_cap(qe, r0=Z0):
        rp = qe * x
        a = math.sqrt(r0 / (rp - r0))  # w Cs r0
        cs = a / (w0 * r0)
        cp = cs / (1 + a ** 2)  # parallel-equivalent capacitance
        return cs, cp

    cs_in, cp_in = end_cap(qe_in)
    cs_out, cp_out = end_cap(qe_out)
    csh = []
    for i in range(n):
        c = c_res
        if i > 0:
            c -= ck[i - 1]
        if i < n - 1:
            c -= ck[i]
        if i == 0:
            c -= cp_in
        if i == n - 1:
            c -= cp_out
        csh.append(c)
    return dict(n=n, bw=bw_hz, ripple=ripple_db, f0=f0, l_res=l_res, g=g, k=k, ck=ck, cs_in=cs_in,
                cs_out=cs_out, csh=csh, qe_in=qe_in, qe_out=qe_out, c_res=c_res)


def netlist_block(d, prefix, n_in, n_out, qu_param="QU", qc_param="QC", lvia_param="LVIA", tol=None):
    """LTspice lines for one filter from node n_in to node n_out. Coil series resistance and capacitor ESR are
    written as expressions of the .param names so that .step can sweep Q. tol: optional dict of multiplying
    parameter names per element kind ('ck', 'cs', 'csh', 'l') for Monte Carlo tables."""
    w0 = 2 * math.pi * d["f0"]
    lines = [f"* {prefix}: {d['n']}-resonator top-C coupled, design BW {d['bw']/1e6:.2f} MHz, ripple {d['ripple']} dB, L {d['l_res']*1e9:.0f} nH"]
    n = d["n"]
    node = lambda i: f"{prefix}r{i+1}"
    def cap(name, a, b, val, mult=None):
        v = f"{val*1e12:.4f}p" if mult is None else f"{{{val*1e12:.4f}p*{mult}}}"
        esr = f"{{1/(2*pi*{d['f0']:.6g}*{val:.6e}*{qc_param})}}"
        return f"C{prefix}{name} {a} {b} {v} Rser={esr}"
    m = (lambda kind, i: None) if tol is None else (lambda kind, i: tol(kind, prefix, i))
    lines.append(cap("sin", n_in, node(0), d["cs_in"], m("cs", 0)))
    for i in range(n):
        gnd = f"{prefix}g{i+1}"
        lmul = m("l", i)
        lval = f"{d['l_res']*1e9:.4f}n" if lmul is None else f"{{{d['l_res']*1e9:.4f}n*{lmul}}}"
        lines.append(f"L{prefix}{i+1} {node(i)} {gnd} {lval} Rser={{2*pi*{d['f0']:.6g}*{d['l_res']:.6e}/{qu_param}}}")
        lines.append(cap(f"sh{i+1}", node(i), gnd, d["csh"][i], m("csh", i)))
        lines.append(f"L{prefix}v{i+1} {gnd} 0 {{{lvia_param}}}")
        if i < n - 1:
            lines.append(cap(f"k{i+1}", node(i), node(i + 1), d["ck"][i], m("ck", i)))
    lines.append(cap("sout", node(n - 1), n_out, d["cs_out"], m("cs", 1)))
    return lines
