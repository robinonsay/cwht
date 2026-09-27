"""Plot the TV-014 LTspice known-answer runs against their analytic answers (owner viewing, 2026-09-27).

Reads the .raw files written by tools/ltspice-batch.sh into this folder and writes
rc-lowpass-bode.png and rc-step-response.png next to them.
Usage: .venv/bin/python docs/cm/tool-validation/evidence/ltspice-known-answers-2026-09-27/plot_known_answers.py
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from spicelib import RawRead

HERE = Path(__file__).resolve().parent
R, C_AC, C_TR = 1e3, 159.155e-9, 1e-6

# --- AC: first-order RC low-pass -----------------------------------------------------------------
raw = RawRead(str(HERE / "rc-lowpass.raw"))
f = np.real(raw.get_trace("frequency").get_wave()).astype(float)
v = raw.get_trace("V(out)").get_wave()
mag_db = 20 * np.log10(np.abs(v))
phase = np.degrees(np.angle(v))
fc_theory = 1 / (2 * np.pi * R * C_AC)
h = 1 / (1 + 1j * f / fc_theory)
mag_th = 20 * np.log10(np.abs(h))
fc_meas = 999.999642341  # from rc-lowpass.log (.meas f3db)

fig, (a1, a2, a3) = plt.subplots(3, 1, figsize=(9, 10), sharex=True,
                                 gridspec_kw={"height_ratios": [3, 2, 1.4]})
a1.semilogx(f, mag_db, lw=2.5, label="LTspice 26.0.2 (through tools/ltspice-batch.sh)")
a1.semilogx(f, mag_th, "k--", lw=1.2, label="Analytic 1/(1 + j f/fc)")
a1.axhline(-3.0103, color="gray", lw=0.8, ls=":")
a1.axvline(fc_meas, color="tab:red", lw=1, ls=":")
a1.annotate(f"-3 dB at {fc_meas:.6f} Hz (LTspice .meas)\nanalytic {fc_theory:.6f} Hz\nerror {fc_meas - fc_theory:+.2e} Hz",
            xy=(fc_meas, -3.0103), xytext=(1.6e3, -12), fontsize=10,
            arrowprops=dict(arrowstyle="->", color="tab:red"))
a1.set_ylabel("|V(out)/V(in)| (dB)")
a1.set_title("TV-014 known answer 1: RC low-pass, R = 1 k, C = 159.155 nF (fc = 1 kHz)")
a1.grid(True, which="both", alpha=0.3); a1.legend(loc="lower left")
a2.semilogx(f, phase, lw=2.5, label="LTspice phase")
a2.semilogx(f, np.degrees(np.angle(h)), "k--", lw=1.2, label="Analytic")
a2.set_ylabel("Phase (deg)"); a2.grid(True, which="both", alpha=0.3); a2.legend(loc="lower left")
a3.semilogx(f, mag_db - mag_th, lw=1.5, color="tab:green")
a3.set_ylabel("LTspice minus\nanalytic (dB)"); a3.set_xlabel("Frequency (Hz)")
a3.grid(True, which="both", alpha=0.3)
fig.tight_layout(); fig.savefig(HERE / "rc-lowpass-bode.png", dpi=130); plt.close(fig)

# --- Transient: RC step response ------------------------------------------------------------------
raw = RawRead(str(HERE / "rc-step-tran.raw"))
t = np.abs(np.real(raw.get_trace("time").get_wave()).astype(float))
vo = np.real(raw.get_trace("V(out)").get_wave()).astype(float)
tau = R * C_TR
vth = 1 - np.exp(-t / tau)
vtau, thalf = 0.632120367773, 0.000693147653313  # from rc-step-tran.log (.meas)
fig, (b1, b2) = plt.subplots(2, 1, figsize=(9, 8), sharex=True, gridspec_kw={"height_ratios": [3, 1.4]})
b1.plot(t * 1e3, vo, lw=2.5, label="LTspice 26.0.2 V(out)")
b1.plot(t * 1e3, vth, "k--", lw=1.2, label="Analytic 1 - exp(-t/tau)")
b1.plot([1.0], [vtau], "o", color="tab:red")
b1.annotate(f"V(tau = 1 ms) = {vtau:.9f} V\nanalytic {1 - np.exp(-1):.9f} V", xy=(1.0, vtau), xytext=(1.6, 0.45),
            arrowprops=dict(arrowstyle="->", color="tab:red"), fontsize=10)
b1.plot([thalf * 1e3], [0.5], "s", color="tab:purple")
b1.annotate(f"V = 0.5 V at {thalf*1e3:.9f} ms\nanalytic {np.log(2):.9f} ms", xy=(thalf * 1e3, 0.5), xytext=(1.6, 0.2),
            arrowprops=dict(arrowstyle="->", color="tab:purple"), fontsize=10)
b1.set_ylabel("V(out) (V)"); b1.set_title("TV-014 known answer 2: RC step response, R = 1 k, C = 1 uF (tau = 1 ms)")
b1.grid(True, alpha=0.3); b1.legend(loc="lower right")
b2.plot(t * 1e3, (vo - vth) * 1e6, lw=1.2, color="tab:green")
b2.set_ylabel("LTspice minus\nanalytic (uV)"); b2.set_xlabel("Time (ms)"); b2.grid(True, alpha=0.3)
fig.tight_layout(); fig.savefig(HERE / "rc-step-response.png", dpi=130); plt.close(fig)
print("max |AC error| dB:", float(np.max(np.abs(mag_db - mag_th))), " max |tran error| uV:", float(np.max(np.abs(vo - vth)) * 1e6))
