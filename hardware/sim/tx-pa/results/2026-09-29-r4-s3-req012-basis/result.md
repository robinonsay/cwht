# 2026-09-29-r4-s3-req012-basis: REQ-SYS-012 basis with the per-unit clamp step (revision 4)

From 2026-09-29-r4-p4-power-a5-design (D-9 8 W ceiling) and 2026-09-29-r4-p5-power-a5-clamp-b (clamp scenario B, 10 W ceiling, 0.03 V window), each with the per-unit clamp step of 2026-09-29-r4-s4-clamp-step. The step basis: module typical to +1.5 dB (the trim range), the step's reading anywhere in its bound, LPF at most its MC 99th percentile, every key-down case. Unmodelled terms -0.15 / +0.07 dB. All estimates.

## D-9 8 W ceiling with the step (r4-p4): step target 6.293 W, highest module 7.74 W

| Coverage | Worst key-down case | At 6.4 V (W) | Margin to 3.97 W (dB) | With the terms (dB) | From 5 W with the terms (dB) | At 8.4 V (W) | Lowest over 6.4 to 8.4 V (W, at V) |
|---|---|---|---|---|---|---|---|
| nominal corner (typical unit read exactly) | +45 C, case 100 C bound, -0.015 dB/K | 3.45 | -0.62 | -0.77 to -0.55 | -1.76 | 2.52 | 2.52 (8.40) |
| lowest, step basis, LPF at most its Monte Carlo median | +45 C, case 100 C bound, -0.015 dB/K | 1.12 | -5.51 | -5.66 to -5.44 | -6.66 | 0.61 | 0.61 (8.40) |
| lowest, step basis, LPF at most its Monte Carlo 99th percentile | +45 C, case 100 C bound, -0.015 dB/K | 1.06 | -5.73 | -5.88 to -5.66 | -6.88 | 0.58 | 0.58 (8.40) |
| lowest, step basis, LPF at its searched worst case | +45 C, case 100 C bound, -0.015 dB/K | 0.86 | -6.66 | -6.81 to -6.59 | -7.81 | 0.46 | 0.46 (8.40) |
| lowest, typical unit read exactly, LPF MC 99th percentile (informative) | +45 C, case 100 C bound, -0.015 dB/K | 2.76 | -1.59 | -1.74 to -1.52 | -2.74 | 1.15 | 1.15 (8.40) |
| lowest, datasheet-minimum module, LPF median | +45 C, case 100 C bound, -0.015 dB/K | 2.38 | -2.23 | -2.38 to -2.16 | -3.38 | 1.10 | 1.10 (8.40) |
| lowest, datasheet-minimum module, LPF MC 99th percentile | +45 C, case 100 C bound, -0.015 dB/K | 2.26 | -2.44 | -2.59 to -2.37 | -3.59 | 1.04 | 1.04 (8.40) |
| lowest, datasheet-minimum module, LPF worst case | +45 C, case 100 C bound, -0.015 dB/K | 1.83 | -3.38 | -3.53 to -3.31 | -4.53 | 0.84 | 0.84 (8.40) |
| lever: P-FET pair at most 0.06 ohm, step basis, LPF worst | +45 C, case 100 C bound, -0.015 dB/K | 0.86 | -6.66 | -6.81 to -6.59 | -7.81 | 0.46 | 0.46 (8.40) |
| levers: P-FET pair and the r14 LPF, step basis | +45 C, case 100 C bound, -0.015 dB/K | 0.98 | -6.08 | -6.23 to -6.01 | -7.23 | 0.53 | 0.53 (8.40) |

No limit line of the stated form found.

## Clamp scenario B with the step (r4-p5): step target 7.887 W, highest module 9.65 W

| Coverage | Worst key-down case | At 6.4 V (W) | Margin to 3.97 W (dB) | With the terms (dB) | From 5 W with the terms (dB) | At 8.4 V (W) | Lowest over 6.4 to 8.4 V (W, at V) |
|---|---|---|---|---|---|---|---|
| nominal corner (typical unit read exactly) | +45 C, case 100 C bound, -0.015 dB/K | 3.49 | -0.56 | -0.71 to -0.49 | -1.71 | 4.49 | 3.49 (6.40) |
| lowest, step basis, LPF at most its Monte Carlo median | +45 C, case 100 C bound, -0.015 dB/K | 2.96 | -1.28 | -1.43 to -1.21 | -2.43 | 3.25 | 2.96 (6.40) |
| lowest, step basis, LPF at most its Monte Carlo 99th percentile | +45 C, case 100 C bound, -0.015 dB/K | 2.82 | -1.49 | -1.64 to -1.42 | -2.64 | 3.09 | 2.82 (6.40) |
| lowest, step basis, LPF at its searched worst case | +45 C, case 100 C bound, -0.015 dB/K | 2.27 | -2.42 | -2.57 to -2.35 | -3.57 | 2.49 | 2.27 (6.40) |
| lowest, typical unit read exactly, LPF MC 99th percentile (informative) | +45 C, case 100 C bound, -0.015 dB/K | 2.82 | -1.49 | -1.64 to -1.42 | -2.64 | 4.09 | 2.82 (6.40) |
| lowest, datasheet-minimum module, LPF median | +45 C, case 100 C bound, -0.015 dB/K | 2.43 | -2.13 | -2.28 to -2.06 | -3.28 | 3.58 | 2.43 (6.40) |
| lowest, datasheet-minimum module, LPF MC 99th percentile | +45 C, case 100 C bound, -0.015 dB/K | 2.32 | -2.34 | -2.49 to -2.27 | -3.49 | 3.40 | 2.32 (6.40) |
| lowest, datasheet-minimum module, LPF worst case | +45 C, case 100 C bound, -0.015 dB/K | 1.87 | -3.27 | -3.42 to -3.20 | -4.42 | 2.75 | 1.87 (6.40) |
| lever: P-FET pair at most 0.06 ohm, step basis, LPF worst | +45 C, case 100 C bound, -0.015 dB/K | 2.48 | -2.05 | -2.20 to -1.98 | -3.20 | 2.49 | 2.48 (6.40) |
| levers: P-FET pair and the r14 LPF, step basis | +45 C, case 100 C bound, -0.015 dB/K | 2.84 | -1.46 | -1.61 to -1.39 | -2.61 | 2.85 | 2.84 (6.40) |

Delta on the basis: 5 W +1/-2.7 dB (2.69 W) at 6.4 V, rising linearly in dB to +1/-2.3 dB (2.94 W) at 6.70 V, and +1/-2.3 dB from there to 8.4 V.

Plot `req012_basis_r4.png`; the verdicts of every revision 4 run in `verdicts.json`.
