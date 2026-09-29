# 2026-09-28-r2-p3-power-a5-sot: A5 output power at the SMA versus pack voltage (REQ-SYS-012), revision 2

Drive: select-on-test drive pad (in-service band of s1). Every figure is an estimate built on graph-read typical vendor curves and estimated feed, efficiency, loss and thermal terms (analysis record section 3); the corners bound the stated input ranges, not the unknowns listed as limitations.

Thermal state (revision 2, finding-9): the key-down cases are steady key-down at their ambient, with the PA case solved from the dissipation (Rth case to ambient 6.11 K/W, WP-PDR-28) and the feed parts and the copper term at their key-down temperatures; the soak rows are the start of a key-down. Output loss [0.5, 0.84, 1.86] dB (LPF revision 2 run r13 plus the relay: allocation, median, worst case). Reference case for the "25 C" figures: 25 C, key-down, -0.005 dB/K.

Verdicts:
- check: one .raw step per corner: **PASS** (11664 steps, 11664 corners).
- check: PA case temperature solved by LTspice equals the thermal law within 0.01 K: **PASS** (largest difference 7.63e-06 K at 6.4 V).
- A5 lowest corner at least 3.97 W from 6.4 to 8.4 V, 25 C key-down: **FAIL**.
- A5 lowest corner at least 3.97 W from 6.4 to 8.4 V, every key-down case: **FAIL**.
- A5 nominal corner at least 3.97 W at 6.4 V, every key-down case: **FAIL**.
- A5 lowest with C2 and C3, LPF at its median, at least 3.97 W at 6.4 V, 25 C key-down: **FAIL**.
- A5 lowest with C2 and C3, LPF at its median, at least 3.97 W at 6.4 V, every key-down case: **FAIL**.
- A5 lowest with C2 and C3, LPF at its worst case, at least 3.97 W at 6.4 V, every key-down case: **FAIL**.
- A5 open loop at 8.4 V: module output at most 8 W (stability conditions), every case: **FAIL**.
- A5 open loop at 8.4 V: module output at most 10 W (maximum rating), every case: **FAIL**.

| Temperature case | Feed low / C2 / high (ohm) | PA case at 6.4 V, nominal / C2 and C3 corner (C) | Nominal at 6.4 V (W) | Lowest, LPF median (W) | Lowest, LPF worst (W) | With C2 and C3, LPF median (W; margin dB) | With C2 and C3, LPF worst (W; margin dB) | Datasheet-minimum module, C2 and C3, LPF median (W) | Every design lever at its best (W; margin dB) | Highest at 6.4 V (W) | Lowest (LPF median) reaches 3.97 W from (V) | Output at 8.4 V, highest (W) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 25 C, start of key-down (case 25 C) | 0.260 / 0.350 / 0.450 | 25.0 / 25.0 | 4.40 | 3.63 | 2.87 | 4.10 (+0.14) | 3.24 (-0.88) | 3.33 | 4.82 (+0.84) | 5.26 | 6.75 | 9.77 |
| 25 C, key-down, -0.005 dB/K | 0.276 / 0.394 / 0.534 | 45.9 / 60.1 | 4.15 | 3.31 | 2.57 | 3.81 (-0.19) | 2.95 (-1.29) | 3.12 | 4.56 (+0.60) | 5.05 | 7.1 | 9.33 |
| 25 C, key-down, -0.015 dB/K | 0.276 / 0.394 / 0.534 | 45.2 / 58.1 | 4.00 | 3.16 | 2.45 | 3.59 (-0.44) | 2.78 (-1.54) | 2.97 | 4.26 (+0.31) | 4.83 | 7.3 | 8.71 |
| -10 C, key-down, PA no cold gain | 0.318 / 0.452 / 0.613 | 10.7 / 24.8 | 4.15 | 3.28 | 2.59 | 3.82 (-0.17) | 3.01 (-1.20) | 3.15 | 4.58 (+0.62) | 5.07 | 7.1 | 9.39 |
| -10 C, start of key-down, PA +0.53 dB | 0.303 / 0.409 / 0.529 | -10.0 / -10.0 | 4.75 | 3.81 | 3.06 | 4.37 (+0.41) | 3.51 (-0.54) | 3.60 | 5.20 (+1.17) | 5.71 | 6.55 | 10.61 |
| +45 C, key-down, -0.005 dB/K | 0.293 / 0.418 / 0.568 | 65.3 / 78.9 | 4.00 | 3.18 | 2.44 | 3.66 (-0.36) | 2.81 (-1.50) | 3.01 | 4.42 (+0.46) | 4.89 | 7.25 | 9.06 |
| +45 C, key-down, -0.015 dB/K | 0.293 / 0.418 / 0.568 | 63.9 / 76.1 | 3.72 | 2.94 | 2.26 | 3.35 (-0.74) | 2.57 (-1.89) | 2.77 | 3.99 (+0.02) | 4.51 | 7.6 | 8.18 |
| +45 C, case 100 C bound, -0.005 dB/K | 0.293 / 0.418 / 0.568 | 100.0 / 100.0 | 3.87 | 3.11 | 2.39 | 3.59 (-0.44) | 2.76 (-1.58) | 2.93 | 4.34 (+0.39) | 4.74 | 7.3 | 8.90 |
| +45 C, case 100 C bound, -0.015 dB/K | 0.293 / 0.418 / 0.568 | 100.0 / 100.0 | 3.35 | 2.73 | 2.10 | 3.14 (-1.03) | 2.41 (-2.17) | 2.54 | 3.75 (-0.25) | 4.07 | 7.8 | 7.66 |

Corners at 6.4 V in the reference case, 25 C, key-down, -0.005 dB/K (full parameter sets):
- Nominal (4.15 W): 25 C, key-down, -0.005 dB/K; drain feed level 0.35 ohm at 25 C part temperature (0.394 ohm in this case); efficiency 0.60; PA input 12.38 dBm; 146 MHz; VGG 3.27 V; typical module; output loss 0.84 dB (copper term +0.063 dB); PA case 45.9 C at 6.4 V.
- Lowest, LPF worst case (2.57 W): 25 C, key-down, -0.005 dB/K; drain feed level 0.45 ohm at 25 C part temperature (0.534 ohm in this case); efficiency 0.45; PA input 10.53 dBm; 148 MHz; VGG 3.08 V; typical module; output loss 1.86 dB (copper term +0.151 dB).
- Lowest, LPF at most its median (3.31 W): 25 C, key-down, -0.005 dB/K; drain feed level 0.45 ohm at 25 C part temperature (0.534 ohm in this case); efficiency 0.45; PA input 10.53 dBm; 148 MHz; VGG 3.08 V; typical module; output loss 0.84 dB (copper term +0.063 dB).
- Highest (5.05 W): 25 C, key-down, -0.005 dB/K; drain feed level 0.26 ohm at 25 C part temperature (0.276 ohm in this case); efficiency 0.60; PA input 14.23 dBm; 144 MHz; VGG 3.46 V; typical module; output loss 0.5 dB (copper term +0.034 dB).
- Lowest with every design lever at its best (4.56 W): 25 C, key-down, -0.005 dB/K; drain feed level 0.26 ohm at 25 C part temperature (0.276 ohm in this case); efficiency 0.45; PA input 10.53 dBm; 148 MHz; VGG 3.46 V; typical module; output loss 0.5 dB (copper term +0.034 dB).
- Lowest with the C2 and C3 levers, LPF at most its median (3.81 W): 25 C, key-down, -0.005 dB/K; drain feed level 0.35 ohm at 25 C part temperature (0.394 ohm in this case); efficiency 0.45; PA input 10.53 dBm; 148 MHz; VGG 3.3 V; typical module; output loss 0.84 dB (copper term +0.063 dB); PA case 60.1 C at 6.4 V.
- Lowest with the C2 and C3 levers, LPF worst case (2.95 W): 25 C, key-down, -0.005 dB/K; drain feed level 0.35 ohm at 25 C part temperature (0.394 ohm in this case); efficiency 0.45; PA input 10.53 dBm; 148 MHz; VGG 3.3 V; typical module; output loss 1.86 dB (copper term +0.151 dB); PA case 60.1 C at 6.4 V.
- Datasheet-minimum module, lowest with the levers, LPF at most its median (3.12 W): 25 C, key-down, -0.005 dB/K; drain feed level 0.35 ohm at 25 C part temperature (0.394 ohm in this case); efficiency 0.45; PA input 10.53 dBm; 148 MHz; VGG 3.3 V; datasheet-minimum module; output loss 0.84 dB (copper term +0.063 dB).
- Worst key-down case (+45 C, case 100 C bound, -0.015 dB/K), lowest with the levers, LPF at most its median (3.14 W): +45 C, case 100 C bound, -0.015 dB/K; drain feed level 0.35 ohm at 25 C part temperature (0.418 ohm in this case); efficiency 0.45; PA input 10.53 dBm; 148 MHz; VGG 3.3 V; typical module; output loss 0.84 dB (copper term +0.092 dB).

- Drain voltage at 6.4 V, reference case: nominal 5.71 V, lowest 5.24 V (key-down sag).
- Module output at 8.4 V, reference case: nominal 8.46 W, highest corner 9.33 W (ALC open; the ALC must hold 5 W).
- Nominal corner reaches 3.97 W from 6.4 V and 5.0 W from 7.1 V in the reference case.
- Drive corners used (from 2026-09-28-r1-d2-drive-a5 with the select-on-test pad residual (s1 method)): [10.52634770890448, 12.380461031287954, 14.23457435367143].
- Sensitivity at 6.4 V in the reference case (dB spread across each input's values, averaged over the other corners; the temperature row over the low-bound cases): output loss 1.48; temperature (the low-bound cases) 1.22; module spread (typical against datasheet minimum) 0.91; drain feed 0.57; VGG clamp 0.37; efficiency 0.28; drive 0.13; frequency 0.03.
- Open loop at 8.4 V (VGG at the clamp maximum 3.46 V), highest corner: 9.33 W in the reference case, 10.61 W at the -10 C start of key-down with the +0.53 dB estimate; above 8 W (stability conditions) from 7.7 V (reference) and 7.25 V (-10 C); above 10 W (maximum rating) from nowhere below 8.4 V (reference) and 8.15 V (-10 C) (input to WP-PDR-22).

Plots: `power_a5_sma.png` (versus pack voltage, with the lowest corner per temperature case), `power_a5_temperature.png` (at 6.4 V per temperature case, against 3.97 W). Deck `power_a5.cir`; LTspice log and raw beside it; numbers in `result.json`.
