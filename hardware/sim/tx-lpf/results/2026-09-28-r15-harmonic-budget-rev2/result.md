# Run 2026-09-28-r15-harmonic-budget-rev2: harmonic budget per finalist, revision 2

Harmonic at the antenna = carrier at the step +1 dB + PA harmonic ratio - [A(nf) - IL(f)], where A(nf) - IL(f) is the worst over the carriers 144 to 148 MHz of the attenuation at the harmonic less the passband loss at that carrier, in the same filter instance (review finding-4). Worst case: the worst of every LTspice step of runs r8 to r14 (Monte Carlo and the worst-case corners); Monte Carlo worst: steps 1 to 252 only. Pack voltages 6.4, 7.2 and 8.4 V (REQ-SYS-017, REQ-TX-007, REQ-SYS-012; review finding-3): A5 at the 5 W step takes the datasheet maxima at 6.4 and 7.2 V and the back-off convention at 8.4 V; every lower step takes the back-off convention (lpf_model.pa_state). Limit: 47 CFR 97.307(e), 25 uW binds at every step. Target: REQ-SYS-018 60 dBc at the 5 W step.

| Finalist | Filter build | 97.307(e): min margin (dB), where | Ramp min margin (dB) | 60 dBc at 6.4 / 7.2 / 8.4 V: margin (dB) | 60 dBc verdict | Monte Carlo worst: 97.307(e) / 60 dBc min margin (dB) |
|---|---|---|---|---|---|---|
| A5 | Coilcraft 1812SMS (J, 5 %), BOM values 22/68/39/82 | PASS 7.5 (2f, 5 W, 8.4 V) | 7.5 | +9.48 / +9.48 / +1.48 | PASS | 14.9 / +8.9 |
| A5 | 24 AWG air coils as wound (+/-10 %), BOM values | PASS 2.3 (2f, 5 W, 8.4 V) | 2.3 | +4.27 / +4.27 / -3.73 | FAIL | 10.3 / +4.3 |
| A5 | 24 AWG air coils aligned (+/-3 %), BOM values | PASS 4.3 (2f, 5 W, 8.4 V) | 4.3 | +6.34 / +6.34 / -1.66 | FAIL | 11.3 / +5.3 |
| A5 | Coilcraft 1812SMS (J, 5 %), retuned 18/68/33/82 | PASS 0.9 (2f, 5 W, 8.4 V) | 0.9 | +2.87 / +2.87 / -5.13 | FAIL | 7.4 / +1.4 |
| A5 | 24 AWG air coils aligned (+/-3 %), retuned 18/68/33/82 | FAIL -1.8 (2f, 5 W, 8.4 V) | -1.8 | +0.25 / +0.25 / -7.75 | FAIL | 4.6 / -1.4 |
| A5 | Coilcraft 1812SMS (G, 2 %) and C0G (G, 2 %), BOM values 22/68/39/82 | PASS 9.5 (2f, 5 W, 8.4 V) | 9.5 | +11.48 / +11.48 / +3.48 | PASS | 14.8 / +8.8 |
| A5 | Coilcraft 1812SMS (G, 2 %) and C0G (G, 2 %), 22/68/36/82 | PASS 8.0 (2f, 5 W, 8.4 V) | 8.0 | +9.97 / +9.97 / +1.97 | PASS | 13.4 / +7.4 |
| A4 | Coilcraft 1812SMS (J, 5 %), BOM values 22/68/39/82 | PASS 5.5 (2f, 5 W, 6.4 V) | 5.5 | -0.52 / -0.52 / -0.52 | FAIL | 12.9 / +6.9 |
| A4 | 24 AWG air coils as wound (+/-10 %), BOM values | PASS 0.3 (2f, 5 W, 6.4 V) | 0.3 | -5.73 / -5.73 / -5.73 | FAIL | 8.3 / +2.3 |
| A4 | 24 AWG air coils aligned (+/-3 %), BOM values | PASS 2.3 (2f, 5 W, 6.4 V) | 2.3 | -3.66 / -3.66 / -3.66 | FAIL | 9.3 / +3.3 |
| A4 | Coilcraft 1812SMS (J, 5 %), retuned 18/68/33/82 | FAIL -1.1 (2f, 5 W, 6.4 V) | -1.1 | -7.13 / -7.13 / -7.13 | FAIL | 5.4 / -0.6 |
| A4 | 24 AWG air coils aligned (+/-3 %), retuned 18/68/33/82 | FAIL -3.8 (2f, 5 W, 6.4 V) | -3.8 | -9.75 / -9.75 / -9.75 | FAIL | 2.6 / -3.4 |
| A4 | Coilcraft 1812SMS (G, 2 %) and C0G (G, 2 %), BOM values 22/68/39/82 | PASS 7.5 (2f, 5 W, 6.4 V) | 7.5 | +1.48 / +1.48 / +1.48 | PASS | 12.8 / +6.8 |
| A4 | Coilcraft 1812SMS (G, 2 %) and C0G (G, 2 %), 22/68/36/82 | PASS 6.0 (2f, 5 W, 6.4 V) | 6.0 | -0.03 / -0.03 / -0.03 | FAIL | 11.4 / +5.4 |

A5 power at the SMA at the 6.4 V pack end (REQ-SYS-012 floor 3.97 W; module 4.46 to 5.13 W from TS-012 section 7.3, relay 0.1 dB):

| Filter build | Loss MC median / MC worst / worst case (dB) | Margin with the MC median loss (dB) | with the MC worst (dB) | with the worst case (dB) |
|---|---|---|---|---|
| Coilcraft 1812SMS (J, 5 %), BOM values 22/68/39/82 | 0.77 / 1.16 / 2.82 | -0.36 to +0.24 | -0.75 to -0.14 | -2.41 to -1.80 |
| 24 AWG air coils as wound (+/-10 %), BOM values | 0.73 / 1.86 / 5.34 | -0.33 to +0.28 | -1.46 to -0.85 | -4.94 to -4.33 |
| 24 AWG air coils aligned (+/-3 %), BOM values | 0.67 / 1.08 / 3.38 | -0.26 to +0.35 | -0.67 to -0.07 | -2.97 to -2.37 |
| Coilcraft 1812SMS (J, 5 %), retuned 18/68/33/82 | 0.53 / 0.68 / 1.39 | -0.13 to +0.48 | -0.28 to +0.33 | -0.99 to -0.38 |
| 24 AWG air coils aligned (+/-3 %), retuned 18/68/33/82 | 0.45 / 0.67 / 1.56 | -0.04 to +0.57 | -0.27 to +0.34 | -1.16 to -0.55 |
| Coilcraft 1812SMS (G, 2 %) and C0G (G, 2 %), BOM values 22/68/39/82 | 0.74 / 1.00 / 1.76 | -0.33 to +0.27 | -0.60 to +0.01 | -1.36 to -0.75 |
| Coilcraft 1812SMS (G, 2 %) and C0G (G, 2 %), 22/68/36/82 | 0.65 / 0.82 / 1.24 | -0.24 to +0.37 | -0.41 to +0.19 | -0.84 to -0.23 |

PA harmonic inputs at the PA output: A5 full state 2f -25 dBc, 3f and above -30 dBc (RA07M1317M datasheet maxima at 6 W, 7.2 V; 4f and above estimated equal to 3f); A5 back-off state 2f -17 dBc, 3f and above -25 dBc (estimates). A4 2f -15 dBc, 3f and above -20 dBc at every step and pack voltage (estimate; no vendor data).

Plots: `harmonic_budget.png`, `harmonic_margins.png`, `a5_power_margin_6v4.png`.
