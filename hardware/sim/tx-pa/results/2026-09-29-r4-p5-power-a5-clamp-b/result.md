# 2026-09-29-r4-p5-power-a5-clamp-b: A5 output power at the SMA with the per-unit clamp step, ceiling 10 W (revision 4)

Drive band (r4-s2): 10.99 / 18.20 / 27.37 mW. Step: design value 9.9 W, g- 0.987 dB, g+ 0.889 dB, step target 7.887 W. VGG window offsets [-0.03, -0.015, 0.0] V. LPF plus relay [0.84, 1.03, 1.34, 1.86] dB. All figures estimates.

| Unit case | Highest module output, any case and pack voltage (W) | Clamp top at 6.4 V (V) | Clamp top at 8.4 V (V) |
|---|---|---|---|
| typical, read exactly | 7.89 | 3.500 to 3.500 | 2.858 to 3.128 |
| typical, read high by the bound | 6.97 | 3.500 to 3.500 | 2.766 to 2.896 |
| typical, read low by the bound | 9.65 | 3.500 to 3.500 | 3.058 to 3.500 |
| +1.5 dB (trim-range top), read high | 6.98 | 2.890 to 3.500 | 2.679 to 2.741 |
| +1.5 dB (trim-range top), read low | 9.65 | 3.500 to 3.500 | 2.799 to 2.965 |
| datasheet minimum, read high | 6.84 | 3.500 to 3.500 | 2.893 to 3.345 |
| datasheet minimum, read low | 8.56 | 3.500 to 3.500 | 3.500 to 3.500 |

At 6.4 V per temperature case (W; margin to 3.97 W in dB):

| Case | Nominal | Step basis, LPF median | Step basis, LPF MC 99 % | Step basis, LPF worst | Typical read exactly, LPF MC 99 % | Min. module, LPF MC 99 % | Levers, step basis |
|---|---|---|---|---|---|---|---|
| 25 C, start of key-down (case 25 C) | 4.57 | 3.91 (-0.06) | 3.75 (-0.25) | 3.09 (-1.08) | 3.75 (-0.25) | 3.09 (-1.10) | 3.75 (-0.25) |
| 25 C, key-down, -0.005 dB/K | 4.32 | 3.56 (-0.47) | 3.40 (-0.68) | 2.76 (-1.58) | 3.40 (-0.68) | 2.83 (-1.47) | 3.45 (-0.61) |
| 25 C, key-down, -0.015 dB/K | 4.15 | 3.39 (-0.69) | 3.23 (-0.89) | 2.63 (-1.79) | 3.23 (-0.89) | 2.71 (-1.67) | 3.25 (-0.87) |
| -10 C, key-down, PA no cold gain | 4.30 | 3.52 (-0.52) | 3.37 (-0.71) | 2.77 (-1.56) | 3.37 (-0.71) | 2.82 (-1.49) | 3.44 (-0.63) |
| -10 C, start of key-down, PA +0.53 dB | 4.89 | 4.07 (+0.11) | 3.91 (-0.07) | 3.27 (-0.84) | 3.91 (-0.07) | 3.27 (-0.85) | 3.98 (+0.01) |
| +45 C, key-down, -0.005 dB/K | 4.16 | 3.42 (-0.65) | 3.25 (-0.87) | 2.62 (-1.80) | 3.25 (-0.87) | 2.72 (-1.65) | 3.31 (-0.79) |
| +45 C, key-down, -0.015 dB/K | 3.87 | 3.16 (-0.99) | 3.01 (-1.21) | 2.43 (-2.14) | 3.01 (-1.21) | 2.52 (-1.98) | 3.02 (-1.18) |
| +45 C, case 100 C bound, -0.005 dB/K | 4.03 | 3.35 (-0.73) | 3.19 (-0.95) | 2.58 (-1.88) | 3.19 (-0.95) | 2.65 (-1.76) | 3.25 (-0.87) |
| +45 C, case 100 C bound, -0.015 dB/K | 3.49 | 2.96 (-1.28) | 2.82 (-1.49) | 2.27 (-2.42) | 2.82 (-1.49) | 2.32 (-2.34) | 2.84 (-1.46) |

At 8.4 V per temperature case (W):

| Case | Nominal | Step basis, LPF MC 99 % | Typical read exactly, LPF MC 99 % | Min. module, LPF MC 99 % |
|---|---|---|---|---|
| 25 C, start of key-down (case 25 C) | 5.89 | 4.08 | 5.40 | 4.50 |
| 25 C, key-down, -0.005 dB/K | 5.55 | 3.91 | 5.11 | 4.30 |
| 25 C, key-down, -0.015 dB/K | 5.27 | 3.67 | 4.67 | 3.99 |
| -10 C, key-down, PA no cold gain | 5.64 | 4.00 | 5.09 | 4.37 |
| -10 C, start of key-down, PA +0.53 dB | 6.43 | 4.57 | 5.97 | 5.01 |
| +45 C, key-down, -0.005 dB/K | 5.37 | 3.78 | 4.94 | 4.16 |
| +45 C, key-down, -0.015 dB/K | 4.91 | 3.42 | 4.37 | 3.73 |
| +45 C, case 100 C bound, -0.005 dB/K | 5.22 | 3.64 | 4.81 | 4.01 |
| +45 C, case 100 C bound, -0.015 dB/K | 4.49 | 3.09 | 4.09 | 3.40 |

Highest module output over every corner and pack voltage: 9.65 W (ceiling 10 W).
Largest pack current at key-down (design corners): 25 C, start of key-down (case 25 C) 3.52 A, 25 C, key-down, -0.005 dB/K 3.29 A, 25 C, key-down, -0.015 dB/K 2.96 A, -10 C, key-down, PA no cold gain 3.19 A, -10 C, start of key-down, PA +0.53 dB 3.79 A, +45 C, key-down, -0.005 dB/K 3.22 A, +45 C, key-down, -0.015 dB/K 2.81 A, +45 C, case 100 C bound, -0.005 dB/K 3.24 A, +45 C, case 100 C bound, -0.015 dB/K 2.80 A.

Every quoted lowest corner with its parameters is in `result.json` (`by_tc.<case>.corners`).
Plots `power_a5_step_clampb_sma.png`, `power_a5_step_clampb_temperature.png`; deck `power_a5_step.cir`.
