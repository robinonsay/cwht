# 2026-09-29-r3-s3-req012-basis: REQ-SYS-012 low-pack basis for the re-baseline CR (revision 3)

From p4 (2026-09-29-r3-p4-power-a5-design, D-9 as specified: VGG 3.30 to 3.50 V at 6.4 V, open-loop ceiling 8 W at 8.4 V) and p5 (2026-09-29-r3-p5-power-a5-clamp-b, clamp scenario B: VGG 3.47 to 3.50 V at 6.4 V, ceiling at the 10 W rating, 0.03 V window). Unmodelled terms -0.15 / +0.07 dB. All estimates.

## D-9 as specified (p4): clamp top at 8.4 V 2.859 V, highest module at 8.4 V 7.90 W

| Coverage | Worst key-down case | At 6.4 V (W) | Margin to 3.97 W (dB) | With the terms (dB) | From 5 W with the terms (dB) | With the D-10 4.0 W limit (W) | At 8.4 V (W) | Pack V reaching 3.97 W in every case |
|---|---|---|---|---|---|---|---|---|
| nominal corner | +45 C, case 100 C bound, -0.015 dB/K | 3.44 | -0.62 | -0.77 to -0.55 | -1.77 | 3.44 | 3.50 | 6.9 |
| lowest, typical module, LPF at most its Monte Carlo median | +45 C, case 100 C bound, -0.015 dB/K | 2.90 | -1.37 | -1.52 to -1.30 | -2.52 | 2.90 | 2.17 | not by 8.4 V |
| lowest, typical module, LPF at most its Monte Carlo 99th percentile | +45 C, case 100 C bound, -0.015 dB/K | 2.76 | -1.59 | -1.74 to -1.52 | -2.73 | 2.76 | 2.07 | not by 8.4 V |
| lowest, typical module, LPF at its searched worst case | +45 C, case 100 C bound, -0.015 dB/K | 2.22 | -2.52 | -2.67 to -2.45 | -3.67 | 2.22 | 1.67 | not by 8.4 V |
| lowest, datasheet-minimum module, LPF median | +45 C, case 100 C bound, -0.015 dB/K | 2.38 | -2.23 | -2.38 to -2.16 | -3.38 | 2.38 | 1.71 | not by 8.4 V |
| lowest, datasheet-minimum module, LPF MC 99th percentile | +45 C, case 100 C bound, -0.015 dB/K | 2.26 | -2.44 | -2.59 to -2.37 | -3.59 | 2.26 | 1.63 | not by 8.4 V |
| lowest, datasheet-minimum module, LPF worst case | +45 C, case 100 C bound, -0.015 dB/K | 1.83 | -3.37 | -3.52 to -3.30 | -4.52 | 1.83 | 1.32 | not by 8.4 V |
| lever: P-FET pair at most 0.06 ohm, typical module, LPF worst | +45 C, case 100 C bound, -0.015 dB/K | 2.42 | -2.15 | -2.30 to -2.08 | -3.30 | 2.42 | 1.73 | not by 8.4 V |
| levers: P-FET pair and the r14 LPF, typical module | +45 C, case 100 C bound, -0.015 dB/K | 2.77 | -1.56 | -1.71 to -1.49 | -2.71 | 2.77 | 1.98 | not by 8.4 V |

Delta on the basis (low_typ_lpf99_w): 5 W +1/-2.8 dB (2.62 W) at 6.4 V; the -1 dB bound is not reached at any pack voltage up to 8.4 V.

## Clamp scenario B (p5): clamp top at 8.4 V 3.120 V, highest module at 8.4 V 9.90 W

| Coverage | Worst key-down case | At 6.4 V (W) | Margin to 3.97 W (dB) | With the terms (dB) | From 5 W with the terms (dB) | With the D-10 4.0 W limit (W) | At 8.4 V (W) | Pack V reaching 3.97 W in every case |
|---|---|---|---|---|---|---|---|---|
| nominal corner | +45 C, case 100 C bound, -0.015 dB/K | 3.48 | -0.57 | -0.72 to -0.50 | -1.72 | 3.48 | 5.35 | 6.9 |
| lowest, typical module, LPF at most its Monte Carlo median | +45 C, case 100 C bound, -0.015 dB/K | 2.96 | -1.28 | -1.43 to -1.21 | -2.43 | 2.96 | 4.65 | 7.45 |
| lowest, typical module, LPF at most its Monte Carlo 99th percentile | +45 C, case 100 C bound, -0.015 dB/K | 2.82 | -1.49 | -1.64 to -1.42 | -2.64 | 2.82 | 4.42 | 7.65 |
| lowest, typical module, LPF at its searched worst case | +45 C, case 100 C bound, -0.015 dB/K | 2.27 | -2.42 | -2.57 to -2.35 | -3.57 | 2.27 | 3.57 | not by 8.4 V |
| lowest, datasheet-minimum module, LPF median | +45 C, case 100 C bound, -0.015 dB/K | 2.43 | -2.13 | -2.28 to -2.06 | -3.27 | 2.43 | 3.78 | not by 8.4 V |
| lowest, datasheet-minimum module, LPF MC 99th percentile | +45 C, case 100 C bound, -0.015 dB/K | 2.32 | -2.34 | -2.49 to -2.27 | -3.49 | 2.32 | 3.60 | not by 8.4 V |
| lowest, datasheet-minimum module, LPF worst case | +45 C, case 100 C bound, -0.015 dB/K | 1.87 | -3.27 | -3.42 to -3.20 | -4.42 | 1.87 | 2.90 | not by 8.4 V |
| lever: P-FET pair at most 0.06 ohm, typical module, LPF worst | +45 C, case 100 C bound, -0.015 dB/K | 2.48 | -2.04 | -2.19 to -1.97 | -3.19 | 2.48 | 3.84 | not by 8.4 V |
| levers: P-FET pair and the r14 LPF, typical module | +45 C, case 100 C bound, -0.015 dB/K | 2.84 | -1.46 | -1.61 to -1.39 | -2.61 | 2.84 | 4.39 | 7.65 |

Delta on the basis (low_typ_lpf99_w): 5 W +1/-2.7 dB (2.69 W) at 6.4 V; the -1 dB bound from 7.8 V (limit line under the basis with the terms: PASS).

## The clamp at 8.4 V (Python replica of the p4 model)

Check against the deck: 7.900 / 7.905 W highest, 3.632 / 3.634 W lowest.

| Clamp top at 8.4 V (V) | Highest module, -10 C start (W) | Lowest, window 0.20 V (W) | Lowest, window 0.03 V (W) |
|---|---|---|---|
| 2.86 | 7.91 | 2.08 | 3.47 |
| 2.95 | 8.83 | 2.94 | 3.91 |
| 3.00 | 9.27 | 3.29 | 4.11 |
| 3.05 | 9.57 | 3.59 | 4.27 |
| 3.10 | 9.82 | 3.83 | 4.38 |
| 3.20 | 10.14 | 4.22 | 4.54 |
| 3.30 | 10.39 | 4.44 | 4.64 |

Plot `req012_basis.png`; the verdicts of every revision 3 run in `verdicts.json`.
