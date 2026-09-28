"""Numpy nodal-analysis pre-check of the filter candidates (design-space scan used only to choose which designs
to run in LTspice; the LTspice runs are the evidence). Prints a table; writes nothing."""
import math, sys
import numpy as np
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from bpf_design import synth, F0

def s21(d, f, qu, qc=800.0, lvia=0.0):
    n = d["n"]; w = 2 * np.pi * f
    wq0 = 2 * np.pi * d["f0"]
    def zc(c): return 1 / (1j * w * c) + 1 / (wq0 * c * qc)
    zl = 1j * w * d["l_res"] + wq0 * d["l_res"] / qu
    # nodes: 0 = input port node (after 50 ohm source), 1..n resonators, n+1 output port node
    N = n + 2
    Y = np.zeros((len(f), N, N), dtype=complex)
    def add(a, b, y):
        Y[:, a, a] += y; Y[:, b, b] += y; Y[:, a, b] -= y; Y[:, b, a] -= y
    def addg(a, y): Y[:, a, a] += y
    addg(0, 1 / 50.0); addg(N - 1, 1 / 50.0)
    add(0, 1, 1 / zc(d["cs_in"]))
    add(n, N - 1, 1 / zc(d["cs_out"]))
    for i in range(n):
        zsh = 1 / (1 / zl + 1 / zc(d["csh"][i])) + 1j * w * lvia
        addg(i + 1, 1 / zsh)
        if i < n - 1:
            add(i + 1, i + 2, 1 / zc(d["ck"][i]))
    I = np.zeros((len(f), N), dtype=complex); I[:, 0] = 2 / 50.0  # 2 V source behind 50 ohm (Norton)
    V = np.linalg.solve(Y, I[..., None])[..., 0]
    return V[:, N - 1]  # = S21 with a 2 V source

def db(x): return 20 * np.log10(np.abs(x))

if __name__ == "__main__":
    fb = np.linspace(144e6, 148e6, 81)
    for IF in (8e6, 10e6, 12e6):
        print(f"=== IF {IF/1e6:.0f} MHz, low-side LO: image {144-2*IF/1e6:.0f} to {148-2*IF/1e6:.0f} MHz")
        for (n1, n2) in ((2, 3), (3, 3), (2, 3, 2) if False else (3, 4), (2, 2)):
            for bw in (5e6, 6e6, 8e6):
                for qu in (100, 150):
                    d1 = synth(n1, bw); d2 = synth(n2, bw)
                    t1 = s21(d1, fb, qu); t2 = s21(d2, fb, qu)
                    fi = fb - 2 * IF
                    i1 = s21(d1, fi, qu); i2 = s21(d2, fi, qu)
                    rej = (db(t1) + db(t2)) - (db(i1) + db(i2))
                    print(f"n={n1}+{n2} bw={bw/1e6:.0f} Qu={qu}: BPF1 loss {-db(t1).min():5.2f} dB, BPF2 loss {-db(t2).min():5.2f}, total worst {-(db(t1)+db(t2)).min():5.2f}; min image rej {rej.min():6.1f} dB")
