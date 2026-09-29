# 2026-09-29-r3-p5-power-a5-clamp-b: A5 output power at the SMA, clamp scenario B (revision 3)

Drive band from s2: 11.0 / 17.3 / 27.3 mW. Clamp: VGG 3.47 to 3.50 V at 6.4 V, top tracking the open-loop ceiling to 3.120 V at 8.4 V (open-loop target 9.9 W). clamp scenario B (s3 trade): 10 W ceiling, 0.03 V window. LPF plus relay [0.84, 1.03, 1.34, 1.86] dB. Feed at 25 C part temperature: low 0.238 ohm, mid 0.345 ohm, bound 0.452 ohm, lever 0.314 ohm. All figures estimates.

| Case | Nominal (W) | Lowest, typ., LPF median | typ., LPF MC 99 % | typ., LPF worst | min. module, LPF median | min., LPF MC 99 % | Lever: P-FET and r14 LPF, typ. |
|---|---|---|---|---|---|---|---|
| 25 C, start of key-down (case 25 C) | 4.56 | 3.92 (-0.06 dB) | 3.75 (-0.25) | 3.10 (-1.08) | 3.23 (-0.90) | 3.09 (-1.09) | 3.75 (-0.25) |
| 25 C, key-down, -0.005 dB/K | 4.31 | 3.57 (-0.47 dB) | 3.40 (-0.68) | 2.76 (-1.58) | 2.97 (-1.26) | 2.83 (-1.47) | 3.45 (-0.61) |
| 25 C, key-down, -0.015 dB/K | 4.15 | 3.39 (-0.69 dB) | 3.23 (-0.89) | 2.63 (-1.79) | 2.84 (-1.46) | 2.71 (-1.67) | 3.25 (-0.87) |
| -10 C, key-down, PA no cold gain | 4.29 | 3.52 (-0.52 dB) | 3.37 (-0.71) | 2.78 (-1.56) | 2.95 (-1.29) | 2.82 (-1.49) | 3.44 (-0.63) |
| -10 C, start of key-down, PA +0.53 dB | 4.88 | 4.07 (+0.11 dB) | 3.91 (-0.07) | 3.27 (-0.84) | 3.41 (-0.67) | 3.27 (-0.85) | 3.98 (+0.01) |
| +45 C, key-down, -0.005 dB/K | 4.16 | 3.42 (-0.65 dB) | 3.25 (-0.86) | 2.63 (-1.80) | 2.85 (-1.44) | 2.72 (-1.65) | 3.31 (-0.79) |
| +45 C, key-down, -0.015 dB/K | 3.86 | 3.16 (-0.99 dB) | 3.01 (-1.21) | 2.43 (-2.14) | 2.64 (-1.77) | 2.52 (-1.98) | 3.02 (-1.18) |
| +45 C, case 100 C bound, -0.005 dB/K | 4.03 | 3.36 (-0.73 dB) | 3.19 (-0.95) | 2.58 (-1.88) | 2.78 (-1.54) | 2.65 (-1.76) | 3.25 (-0.87) |
| +45 C, case 100 C bound, -0.015 dB/K | 3.48 | 2.96 (-1.28 dB) | 2.82 (-1.49) | 2.27 (-2.42) | 2.43 (-2.13) | 2.32 (-2.34) | 2.84 (-1.46) |

Pack voltage at which each lowest corner reaches 3.97 W (V; None: not reached by 8.4 V):

| Case | nominal | typ., LPF median | typ., LPF MC 99 % | typ., LPF worst | min., LPF MC 99 % |
|---|---|---|---|---|---|
| 25 C, start of key-down (case 25 C) | 6.4 | 6.45 | 6.6 | 7.3 | 7.3 |
| 25 C, key-down, -0.005 dB/K | 6.4 | 6.8 | 6.95 | 7.8 | 7.7 |
| 25 C, key-down, -0.015 dB/K | 6.4 | 7.0 | 7.2 | None | 7.95 |
| -10 C, key-down, PA no cold gain | 6.4 | 6.85 | 7.0 | 7.85 | 7.7 |
| -10 C, start of key-down, PA +0.53 dB | 6.4 | 6.4 | 6.5 | 7.1 | 7.1 |
| +45 C, key-down, -0.005 dB/K | 6.4 | 6.95 | 7.15 | 8.0 | 7.85 |
| +45 C, key-down, -0.015 dB/K | 6.5 | 7.3 | 7.5 | None | None |
| +45 C, case 100 C bound, -0.005 dB/K | 6.4 | 7.0 | 7.2 | 8.0 | 7.9 |
| +45 C, case 100 C bound, -0.015 dB/K | 6.9 | 7.45 | 7.65 | None | None |

At 8.4 V with the clamp: module highest corner 9.90 W over every case; lowest corner (typical module, LPF worst) 3.57 W at worst over the key-down cases.
Largest pack current at key-down (design corners): 25 C, start of key-down (case 25 C) 2.93 A, 25 C, key-down, -0.005 dB/K 2.75 A, 25 C, key-down, -0.015 dB/K 2.48 A, -10 C, key-down, PA no cold gain 2.68 A, -10 C, start of key-down, PA +0.53 dB 3.20 A, +45 C, key-down, -0.005 dB/K 2.69 A, +45 C, key-down, -0.015 dB/K 2.35 A, +45 C, case 100 C bound, -0.005 dB/K 2.70 A, +45 C, case 100 C bound, -0.015 dB/K 2.34 A.

Every quoted lowest corner with its parameters is in `result.json` (`by_tc.<case>.corners`).
Plots `power_a5_clampb_sma.png`, `power_a5_clampb_temperature.png`; deck `power_a5_design.cir`.
