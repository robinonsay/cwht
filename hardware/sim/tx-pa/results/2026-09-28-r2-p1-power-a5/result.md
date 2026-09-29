# 2026-09-28-r2-p1-power-a5: A5 output power at the SMA versus pack voltage (REQ-SYS-012), revision 2

Drive: drive as designed (fixed 18 dB pad, coax 5 to 15 cm). Every figure is an estimate built on graph-read typical vendor curves and estimated feed, efficiency, loss and thermal terms (analysis record section 3); the corners bound the stated input ranges, not the unknowns listed as limitations.

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
| 25 C, start of key-down (case 25 C) | 0.260 / 0.350 / 0.450 | 25.0 / 25.0 | 4.33 | 3.48 | 2.75 | 3.94 (-0.04) | 3.11 (-1.06) | 3.19 | 4.61 (+0.65) | 5.29 | 6.9 | 9.84 |
| 25 C, key-down, -0.005 dB/K | 0.276 / 0.394 / 0.534 | 45.6 / 58.7 | 4.09 | 3.19 | 2.47 | 3.66 (-0.36) | 2.83 (-1.46) | 2.99 | 4.37 (+0.42) | 5.08 | 7.2 | 9.38 |
| 25 C, key-down, -0.015 dB/K | 0.276 / 0.394 / 0.534 | 44.8 / 56.8 | 3.94 | 3.04 | 2.36 | 3.46 (-0.60) | 2.68 (-1.71) | 2.85 | 4.09 (+0.13) | 4.86 | 7.45 | 8.76 |
| -10 C, key-down, PA no cold gain | 0.318 / 0.452 / 0.613 | 10.3 / 23.4 | 4.09 | 3.16 | 2.49 | 3.68 (-0.34) | 2.89 (-1.38) | 3.02 | 4.41 (+0.45) | 5.11 | 7.25 | 9.45 |
| -10 C, start of key-down, PA +0.53 dB | 0.303 / 0.409 / 0.529 | -10.0 / -10.0 | 4.68 | 3.67 | 2.95 | 4.20 (+0.24) | 3.38 (-0.71) | 3.45 | 4.98 (+0.98) | 5.75 | 6.7 | 10.68 |
| +45 C, key-down, -0.005 dB/K | 0.293 / 0.418 / 0.568 | 65.0 / 77.6 | 3.94 | 3.06 | 2.35 | 3.52 (-0.53) | 2.70 (-1.67) | 2.89 | 4.23 (+0.27) | 4.92 | 7.35 | 9.12 |
| +45 C, key-down, -0.015 dB/K | 0.293 / 0.418 / 0.568 | 63.6 / 74.9 | 3.66 | 2.83 | 2.17 | 3.22 (-0.91) | 2.47 (-2.06) | 2.65 | 3.83 (-0.16) | 4.54 | 7.75 | 8.23 |
| +45 C, case 100 C bound, -0.005 dB/K | 0.293 / 0.418 / 0.568 | 100.0 / 100.0 | 3.81 | 2.99 | 2.30 | 3.45 (-0.61) | 2.65 (-1.76) | 2.81 | 4.15 (+0.19) | 4.77 | 7.45 | 8.96 |
| +45 C, case 100 C bound, -0.015 dB/K | 0.293 / 0.418 / 0.568 | 100.0 / 100.0 | 3.29 | 2.62 | 2.01 | 3.00 (-1.21) | 2.31 (-2.36) | 2.43 | 3.58 (-0.45) | 4.10 | 7.95 | 7.71 |

Corners at 6.4 V in the reference case, 25 C, key-down, -0.005 dB/K (full parameter sets):
- Nominal (4.09 W): 25 C, key-down, -0.005 dB/K; drain feed level 0.35 ohm at 25 C part temperature (0.394 ohm in this case); efficiency 0.60; PA input 10.57 dBm; 146 MHz; VGG 3.27 V; typical module; output loss 0.84 dB (copper term +0.063 dB); PA case 45.6 C at 6.4 V.
- Lowest, LPF worst case (2.47 W): 25 C, key-down, -0.005 dB/K; drain feed level 0.45 ohm at 25 C part temperature (0.534 ohm in this case); efficiency 0.45; PA input 7.31 dBm; 148 MHz; VGG 3.08 V; typical module; output loss 1.86 dB (copper term +0.151 dB).
- Lowest, LPF at most its median (3.19 W): 25 C, key-down, -0.005 dB/K; drain feed level 0.45 ohm at 25 C part temperature (0.534 ohm in this case); efficiency 0.45; PA input 7.31 dBm; 148 MHz; VGG 3.08 V; typical module; output loss 0.84 dB (copper term +0.063 dB).
- Highest (5.08 W): 25 C, key-down, -0.005 dB/K; drain feed level 0.26 ohm at 25 C part temperature (0.276 ohm in this case); efficiency 0.60; PA input 15.50 dBm; 144 MHz; VGG 3.46 V; typical module; output loss 0.5 dB (copper term +0.034 dB).
- Lowest with every design lever at its best (4.37 W): 25 C, key-down, -0.005 dB/K; drain feed level 0.26 ohm at 25 C part temperature (0.276 ohm in this case); efficiency 0.45; PA input 7.31 dBm; 148 MHz; VGG 3.46 V; typical module; output loss 0.5 dB (copper term +0.034 dB).
- Lowest with the C2 and C3 levers, LPF at most its median (3.66 W): 25 C, key-down, -0.005 dB/K; drain feed level 0.35 ohm at 25 C part temperature (0.394 ohm in this case); efficiency 0.45; PA input 7.31 dBm; 148 MHz; VGG 3.3 V; typical module; output loss 0.84 dB (copper term +0.063 dB); PA case 58.7 C at 6.4 V.
- Lowest with the C2 and C3 levers, LPF worst case (2.83 W): 25 C, key-down, -0.005 dB/K; drain feed level 0.35 ohm at 25 C part temperature (0.394 ohm in this case); efficiency 0.45; PA input 7.31 dBm; 148 MHz; VGG 3.3 V; typical module; output loss 1.86 dB (copper term +0.151 dB); PA case 58.7 C at 6.4 V.
- Datasheet-minimum module, lowest with the levers, LPF at most its median (2.99 W): 25 C, key-down, -0.005 dB/K; drain feed level 0.35 ohm at 25 C part temperature (0.394 ohm in this case); efficiency 0.45; PA input 7.31 dBm; 144 MHz; VGG 3.3 V; datasheet-minimum module; output loss 0.84 dB (copper term +0.063 dB).
- Worst key-down case (+45 C, case 100 C bound, -0.015 dB/K), lowest with the levers, LPF at most its median (3.00 W): +45 C, case 100 C bound, -0.015 dB/K; drain feed level 0.35 ohm at 25 C part temperature (0.418 ohm in this case); efficiency 0.45; PA input 7.31 dBm; 148 MHz; VGG 3.3 V; typical module; output loss 0.84 dB (copper term +0.092 dB).

- Drain voltage at 6.4 V, reference case: nominal 5.72 V, lowest 5.23 V (key-down sag).
- Module output at 8.4 V, reference case: nominal 8.32 W, highest corner 9.38 W (ALC open; the ALC must hold 5 W).
- Nominal corner reaches 3.97 W from 6.4 V and 5.0 W from 7.15 V in the reference case.
- Drive corners used (from 2026-09-28-r1-d2-drive-a5): [7.309240051163477, 10.574659210423574, 15.496228427664747].
- Sensitivity at 6.4 V in the reference case (dB spread across each input's values, averaged over the other corners; the temperature row over the low-bound cases): output loss 1.48; temperature (the low-bound cases) 1.22; module spread (typical against datasheet minimum) 0.91; drain feed 0.56; VGG clamp 0.37; drive 0.34; efficiency 0.27; frequency 0.03.
- Open loop at 8.4 V (VGG at the clamp maximum 3.46 V), highest corner: 9.38 W in the reference case, 10.68 W at the -10 C start of key-down with the +0.53 dB estimate; above 8 W (stability conditions) from 7.7 V (reference) and 7.2 V (-10 C); above 10 W (maximum rating) from nowhere below 8.4 V (reference) and 8.1 V (-10 C) (input to WP-PDR-22).

Plots: `power_a5_sma.png` (versus pack voltage, with the lowest corner per temperature case), `power_a5_temperature.png` (at 6.4 V per temperature case, against 3.97 W). Deck `power_a5.cir`; LTspice log and raw beside it; numbers in `result.json`.
