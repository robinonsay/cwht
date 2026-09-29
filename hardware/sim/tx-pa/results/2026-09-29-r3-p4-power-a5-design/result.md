# 2026-09-29-r3-p4-power-a5-design: A5 output power at the SMA, the adopted design (D-9 clamp) (revision 3)

Drive band from s2: 11.0 / 17.3 / 27.3 mW. Clamp: VGG 3.30 to 3.50 V at 6.4 V, top tracking the open-loop ceiling to 2.859 V at 8.4 V (open-loop target 7.9 W). LPF plus relay [0.84, 1.03, 1.34, 1.86] dB. Feed at 25 C part temperature: low 0.238 ohm, mid 0.345 ohm, bound 0.452 ohm, lever 0.314 ohm. All figures estimates.

| Case | Nominal (W) | Lowest, typ., LPF median | typ., LPF MC 99 % | typ., LPF worst | min. module, LPF median | min., LPF MC 99 % | Lever: P-FET and r14 LPF, typ. |
|---|---|---|---|---|---|---|---|
| 25 C, start of key-down (case 25 C) | 4.51 | 3.83 (-0.16 dB) | 3.67 (-0.35) | 3.03 (-1.18) | 3.15 (-1.00) | 3.02 (-1.19) | 3.66 (-0.35) |
| 25 C, key-down, -0.005 dB/K | 4.26 | 3.49 (-0.56 dB) | 3.33 (-0.76) | 2.71 (-1.66) | 2.90 (-1.36) | 2.77 (-1.57) | 3.38 (-0.70) |
| 25 C, key-down, -0.015 dB/K | 4.10 | 3.32 (-0.77 dB) | 3.17 (-0.98) | 2.58 (-1.88) | 2.78 (-1.55) | 2.65 (-1.76) | 3.19 (-0.96) |
| -10 C, key-down, PA no cold gain | 4.24 | 3.46 (-0.61 dB) | 3.30 (-0.80) | 2.72 (-1.64) | 2.89 (-1.39) | 2.76 (-1.58) | 3.36 (-0.72) |
| -10 C, start of key-down, PA +0.53 dB | 4.83 | 3.99 (+0.02 dB) | 3.83 (-0.16) | 3.21 (-0.93) | 3.33 (-0.76) | 3.20 (-0.94) | 3.89 (-0.09) |
| +45 C, key-down, -0.005 dB/K | 4.11 | 3.35 (-0.74 dB) | 3.19 (-0.95) | 2.57 (-1.89) | 2.79 (-1.53) | 2.66 (-1.74) | 3.24 (-0.89) |
| +45 C, key-down, -0.015 dB/K | 3.82 | 3.10 (-1.08 dB) | 2.95 (-1.29) | 2.38 (-2.23) | 2.59 (-1.86) | 2.46 (-2.08) | 2.96 (-1.28) |
| +45 C, case 100 C bound, -0.005 dB/K | 3.98 | 3.29 (-0.82 dB) | 3.13 (-1.04) | 2.52 (-1.97) | 2.72 (-1.64) | 2.59 (-1.86) | 3.18 (-0.97) |
| +45 C, case 100 C bound, -0.015 dB/K | 3.44 | 2.90 (-1.37 dB) | 2.76 (-1.59) | 2.22 (-2.52) | 2.38 (-2.23) | 2.26 (-2.44) | 2.77 (-1.56) |

Pack voltage at which each lowest corner reaches 3.97 W (V; None: not reached by 8.4 V):

| Case | nominal | typ., LPF median | typ., LPF MC 99 % | typ., LPF worst | min., LPF MC 99 % |
|---|---|---|---|---|---|
| 25 C, start of key-down (case 25 C) | 6.4 | 6.55 | 6.7 | None | None |
| 25 C, key-down, -0.005 dB/K | 6.4 | 6.85 | 7.05 | None | None |
| 25 C, key-down, -0.015 dB/K | 6.4 | 7.1 | None | None | None |
| -10 C, key-down, PA no cold gain | 6.4 | 6.9 | 7.1 | None | None |
| -10 C, start of key-down, PA +0.53 dB | 6.4 | 6.4 | 6.55 | None | None |
| +45 C, key-down, -0.005 dB/K | 6.4 | 7.05 | None | None | None |
| +45 C, key-down, -0.015 dB/K | 6.55 | None | None | None | None |
| +45 C, case 100 C bound, -0.005 dB/K | 6.4 | 7.1 | None | None | None |
| +45 C, case 100 C bound, -0.015 dB/K | 6.9 | None | None | None | None |

At 8.4 V with the clamp: module highest corner 7.90 W over every case; lowest corner (typical module, LPF worst) 1.67 W at worst over the key-down cases.
Largest pack current at key-down (design corners): 25 C, start of key-down (case 25 C) 2.67 A, 25 C, key-down, -0.005 dB/K 2.54 A, 25 C, key-down, -0.015 dB/K 2.33 A, -10 C, key-down, PA no cold gain 2.52 A, -10 C, start of key-down, PA +0.53 dB 2.90 A, +45 C, key-down, -0.005 dB/K 2.48 A, +45 C, key-down, -0.015 dB/K 2.21 A, +45 C, case 100 C bound, -0.005 dB/K 2.47 A, +45 C, case 100 C bound, -0.015 dB/K 2.14 A.

Every quoted lowest corner with its parameters is in `result.json` (`by_tc.<case>.corners`).
Plots `power_a5_design_sma.png`, `power_a5_design_temperature.png`; deck `power_a5_design.cir`.
