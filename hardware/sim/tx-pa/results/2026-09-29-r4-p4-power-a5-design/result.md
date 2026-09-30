# 2026-09-29-r4-p4-power-a5-design: A5 output power at the SMA with the per-unit clamp step, ceiling 8 W (revision 4)

Drive band (r4-s2): 10.99 / 18.20 / 27.37 mW. Step: design value 7.9 W, g- 0.987 dB, g+ 0.889 dB, step target 6.293 W. VGG window offsets [-0.2, -0.1, 0.0] V. LPF plus relay [0.84, 1.03, 1.34, 1.86] dB. All figures estimates.

| Unit case | Highest module output, any case and pack voltage (W) | Clamp top at 6.4 V (V) | Clamp top at 8.4 V (V) |
|---|---|---|---|
| typical, read exactly | 6.30 | 3.336 to 3.500 | 2.749 to 2.834 |
| typical, read high by the bound | 5.54 | 2.942 to 3.500 | 2.700 to 2.750 |
| typical, read low by the bound | 7.74 | 3.500 to 3.500 | 2.843 to 2.998 |
| +1.5 dB (trim-range top), read high | 5.57 | 2.759 to 3.006 | 2.630 to 2.670 |
| +1.5 dB (trim-range top), read low | 7.74 | 3.029 to 3.500 | 2.719 to 2.782 |
| datasheet minimum, read high | 5.46 | 3.500 to 3.500 | 2.769 to 2.869 |
| datasheet minimum, read low | 7.73 | 3.500 to 3.500 | 3.068 to 3.500 |

At 6.4 V per temperature case (W; margin to 3.97 W in dB):

| Case | Nominal | Step basis, LPF median | Step basis, LPF MC 99 % | Step basis, LPF worst | Typical read exactly, LPF MC 99 % | Min. module, LPF MC 99 % | Levers, step basis |
|---|---|---|---|---|---|---|---|
| 25 C, start of key-down (case 25 C) | 4.51 | 1.47 (-4.31) | 1.41 (-4.50) | 1.16 (-5.33) | 3.67 (-0.35) | 3.02 (-1.20) | 1.31 (-4.81) |
| 25 C, key-down, -0.005 dB/K | 4.27 | 1.44 (-4.42) | 1.37 (-4.63) | 1.11 (-5.53) | 3.33 (-0.76) | 2.77 (-1.57) | 1.27 (-4.96) |
| 25 C, key-down, -0.015 dB/K | 4.11 | 1.41 (-4.49) | 1.35 (-4.70) | 1.09 (-5.60) | 3.17 (-0.98) | 2.65 (-1.76) | 1.25 (-5.03) |
| -10 C, key-down, PA no cold gain | 4.25 | 1.45 (-4.38) | 1.38 (-4.58) | 1.14 (-5.42) | 3.30 (-0.80) | 2.76 (-1.58) | 1.29 (-4.89) |
| -10 C, start of key-down, PA +0.53 dB | 4.84 | 1.65 (-3.81) | 1.59 (-3.98) | 1.33 (-4.76) | 3.83 (-0.16) | 3.20 (-0.94) | 1.49 (-4.27) |
| +45 C, key-down, -0.005 dB/K | 4.12 | 1.39 (-4.56) | 1.32 (-4.77) | 1.07 (-5.70) | 3.19 (-0.95) | 2.66 (-1.75) | 1.22 (-5.12) |
| +45 C, key-down, -0.015 dB/K | 3.82 | 1.31 (-4.81) | 1.25 (-5.03) | 1.01 (-5.96) | 2.95 (-1.29) | 2.46 (-2.08) | 1.15 (-5.38) |
| +45 C, case 100 C bound, -0.005 dB/K | 3.99 | 1.32 (-4.79) | 1.26 (-5.00) | 1.01 (-5.93) | 3.13 (-1.04) | 2.59 (-1.86) | 1.16 (-5.35) |
| +45 C, case 100 C bound, -0.015 dB/K | 3.45 | 1.12 (-5.51) | 1.06 (-5.73) | 0.86 (-6.66) | 2.76 (-1.59) | 2.26 (-2.44) | 0.98 (-6.08) |

At 8.4 V per temperature case (W):

| Case | Nominal | Step basis, LPF MC 99 % | Typical read exactly, LPF MC 99 % | Min. module, LPF MC 99 % |
|---|---|---|---|---|
| 25 C, start of key-down (case 25 C) | 3.33 | 0.77 | 1.53 | 1.39 |
| 25 C, key-down, -0.005 dB/K | 3.19 | 0.75 | 1.48 | 1.35 |
| 25 C, key-down, -0.015 dB/K | 3.09 | 0.74 | 1.46 | 1.33 |
| -10 C, key-down, PA no cold gain | 3.23 | 0.76 | 1.51 | 1.37 |
| -10 C, start of key-down, PA +0.53 dB | 3.69 | 0.87 | 1.73 | 1.57 |
| +45 C, key-down, -0.005 dB/K | 3.09 | 0.72 | 1.44 | 1.31 |
| +45 C, key-down, -0.015 dB/K | 2.87 | 0.69 | 1.35 | 1.23 |
| +45 C, case 100 C bound, -0.005 dB/K | 2.96 | 0.68 | 1.36 | 1.24 |
| +45 C, case 100 C bound, -0.015 dB/K | 2.52 | 0.58 | 1.15 | 1.04 |

Highest module output over every corner and pack voltage: 7.74 W (ceiling 8 W).
Largest pack current at key-down (design corners): 25 C, start of key-down (case 25 C) 3.19 A, 25 C, key-down, -0.005 dB/K 3.00 A, 25 C, key-down, -0.015 dB/K 2.76 A, -10 C, key-down, PA no cold gain 2.96 A, -10 C, start of key-down, PA +0.53 dB 3.41 A, +45 C, key-down, -0.005 dB/K 2.93 A, +45 C, key-down, -0.015 dB/K 2.62 A, +45 C, case 100 C bound, -0.005 dB/K 2.91 A, +45 C, case 100 C bound, -0.015 dB/K 2.54 A.

Every quoted lowest corner with its parameters is in `result.json` (`by_tc.<case>.corners`).
Plots `power_a5_step_d9_sma.png`, `power_a5_step_d9_temperature.png`; deck `power_a5_step.cir`.
