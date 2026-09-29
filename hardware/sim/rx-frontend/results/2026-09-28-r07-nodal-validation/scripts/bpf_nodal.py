"""Numpy nodal AC solver for the rx-frontend band-pass filter sections (review fix of INSP findings 1, 2 and 5 on
docs/design/analysis/rx-bpf-ts012.md, revision 2).

Purpose. LTspice (tools/ltspice-batch.sh, ACC-LTSPICE-001) stays the evidence. This solver is a search tool: it
evaluates the SAME netlist lines that make_decks.py writes (bpf_design.netlist_block), parsed here, so it can
be run on 20,000 Monte Carlo draws and on every corner of a tolerance box, which LTspice cannot do in a
reasonable raw-file size. Its agreement with LTspice is checked on every LTspice run of the block by
validate_nodal.py (run r07); every worst-case corner it finds is re-simulated in LTspice (run r09).

Model semantics (identical to LTspice for these element kinds):
  - C name a b value [Rser=expr]: capacitor with a series resistance;
  - L name a b value [Rser=expr]: inductor with a series resistance;
  - values and expressions may use the .param names (QU, QC, LVIA, the Monte Carlo multipliers m...), pi and
    the SPICE suffixes f p n u m k Meg;
  - ports: an ideal source of amplitude VS behind RS into the input node, RL from the output node to ground;
  - optional stray capacitance CST from an ideal copy of the input voltage times exp(j PHI) to the output node
    (the r04 deck uses PHI = 0 and pi, i.e. SGN = +1 and -1).
All parameters may be numpy arrays; they broadcast against each other (e.g. one axis of runs) and the
frequency axis is appended last before the node axes."""
import math, re
import numpy as np

SUFFIX = [("meg", 1e6), ("f", 1e-15), ("p", 1e-12), ("n", 1e-9), ("u", 1e-6), ("m", 1e-3), ("k", 1e3), ("g", 1e9), ("t", 1e12)]


def _num(tok, ns):
    tok = tok.strip()
    if tok.startswith("{") and tok.endswith("}"):
        return _expr(tok[1:-1], ns)
    return _si(tok)


def _si(tok):
    t = tok.lower()
    m = re.match(r"^([-+]?[0-9.]+(?:e[-+]?[0-9]+)?)([a-z]*)$", t)
    if not m:
        raise ValueError(f"bpf_nodal: cannot parse value {tok!r}")
    v, suf = float(m.group(1)), m.group(2)
    for s, mult in SUFFIX:
        if suf.startswith(s):
            return v * mult
    return v


def _expr(e, ns):
    # SPICE numbers with suffixes inside an expression, e.g. 4.8700p*mcsb10 or 5n
    def rep(m):
        return repr(_si(m.group(0)))
    e2 = re.sub(r"(?<![A-Za-z_0-9.])[0-9.]+(?:e[-+]?[0-9]+)?(?:meg|Meg|MEG|[fpnumkgt])(?![A-Za-z_0-9])", rep, e)
    env = {"pi": math.pi, "sqrt": np.sqrt}
    env.update(ns)
    return eval(e2, {"__builtins__": {}}, env)


def parse(lines):
    """Return a list of (kind, a, b, value_token, rser_token or None) from netlist_block lines."""
    els = []
    for ln in lines:
        s = ln.strip()
        if not s or s.startswith("*"):
            continue
        parts = s.split()
        kind = parts[0][0].upper()
        if kind not in "CL":
            raise ValueError(f"bpf_nodal: unsupported element {s!r}")
        a, b, val = parts[1], parts[2], parts[3]
        rser = None
        for p in parts[4:]:
            if p.lower().startswith("rser="):
                rser = p[5:]
        els.append((kind, a, b, val, rser))
    return els


def solve(lines, n_in, n_out, freqs, ns, rs=50.0, rl=50.0, vs=2.0, cst=0.0, phi=0.0, cin=0.0, cout=0.0):
    """AC node voltage at n_out for a source VS behind RS into n_in and RL at n_out.
    freqs: 1-D array (Hz). ns: parameter namespace (scalars or broadcastable arrays).
    rs, rl, cst, phi, cin, cout: scalars or arrays broadcastable with the parameters; cin and cout are shunt
    capacitances at the input and output port nodes (the J310 source-gate capacitance, for example).
    Returns complex array of shape broadcast(params) + (len(freqs),)."""
    els = parse(lines)
    nodes = []
    for _, a, b, _, _ in els:
        for x in (a, b):
            if x != "0" and x not in nodes:
                nodes.append(x)
    for x in (n_in, n_out):
        if x not in nodes:
            nodes.append(x)
    idx = {x: i for i, x in enumerate(nodes)}
    N = len(nodes)
    w = 2 * np.pi * np.asarray(freqs, float)
    vals = []
    shapes = [np.shape(rs), np.shape(rl), np.shape(cst), np.shape(phi), np.shape(cin), np.shape(cout)]
    for kind, a, b, val, rser in els:
        v = np.asarray(_num(val, ns), float)
        r = np.asarray(0.0 if rser is None else _num(rser, ns), float)
        vals.append((kind, a, b, v, r))
        shapes += [v.shape, r.shape]
    bshape = np.broadcast_shapes(*shapes)
    Y = np.zeros(bshape + (len(w), N, N), dtype=complex)

    def stamp(a, b, y):
        y = np.broadcast_to(y, bshape + (len(w),))
        if a != "0":
            Y[..., idx[a], idx[a]] += y
        if b != "0":
            Y[..., idx[b], idx[b]] += y
        if a != "0" and b != "0":
            Y[..., idx[a], idx[b]] -= y
            Y[..., idx[b], idx[a]] -= y

    for kind, a, b, v, r in vals:
        v = v[..., None]; r = r[..., None]
        if kind == "C":
            z = r + 1.0 / (1j * w * v)
        else:
            z = r + 1j * w * v
        stamp(a, b, 1.0 / z)
    gs = 1.0 / np.asarray(rs, float)[..., None]
    gl = 1.0 / np.asarray(rl, float)[..., None]
    stamp(n_in, "0", gs)
    stamp(n_out, "0", gl)
    for node, cc in ((n_in, cin), (n_out, cout)):
        cc = np.asarray(cc, float)[..., None]
        if np.any(cc != 0):
            stamp(node, "0", 1j * w * cc)
    c = np.asarray(cst, float)[..., None]
    if np.any(c != 0):
        yc = np.broadcast_to(1j * w * c, bshape + (len(w),))
        ph = np.broadcast_to(np.exp(1j * np.asarray(phi, float))[..., None], bshape + (len(w),))
        Y[..., idx[n_out], idx[n_out]] += yc
        Y[..., idx[n_out], idx[n_in]] -= yc * ph
    I = np.zeros(bshape + (len(w), N), dtype=complex)
    I[..., idx[n_in]] = vs * np.broadcast_to(gs, bshape + (len(w),))
    V = np.linalg.solve(Y, I[..., None])[..., 0]
    return V[..., idx[n_out]]


def s21_db(lines, freqs, ns, rs=50.0, rl=50.0, **kw):
    """Transducer gain in dB, |S21|^2 = |Vout|^2 RS / RL for a 2 V source (equals 20 log |V(o)| at 50/50); a
    shunt port capacitance draws no power, so the formula holds with cin and cout."""
    v = solve(lines, "i", "o", freqs, ns, rs=rs, rl=rl, vs=2.0, **kw)
    return 20 * np.log10(np.abs(v)) + 10 * np.log10(np.asarray(rs, float) / np.asarray(rl, float))[..., None]
