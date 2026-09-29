# 2026-09-28-r2-p2-power-a4: A4 output power at the SMA versus pack voltage (REQ-SYS-012), revision 2

Drive: drive as designed (fixed 12 dB pad, coax 5 to 15 cm). Every figure is an estimate built on graph-read typical vendor curves and estimated feed, efficiency, loss and thermal terms (analysis record section 3); the corners bound the stated input ranges, not the unknowns listed as limitations.

Thermal state (revision 2, finding-9): the key-down cases are steady key-down at their ambient, with the PA case solved from the dissipation (Rth case to ambient 9.6 K/W, WP-PDR-28) and the feed parts and the copper term at their key-down temperatures; the soak rows are the start of a key-down. Output loss [0.5, 0.84, 1.86] dB (LPF revision 2 run r13 plus the relay: allocation, median, worst case). Reference case for the "25 C" figures: 25 C, key-down, -0.005 dB/K.

Verdicts:
- check: one .raw step per corner: **PASS** (13122 steps, 13122 corners).
- check: PA case temperature solved by LTspice equals the thermal law within 0.01 K: **PASS** (largest difference 9.54e-06 K at 6.4 V).
- A4 lowest corner at least 3.97 W from 6.4 to 8.4 V, 25 C key-down: **FAIL**.
- A4 lowest corner at least 3.97 W from 6.4 to 8.4 V, every key-down case: **FAIL**.
- A4 nominal corner at least 3.97 W at 6.4 V, every key-down case: **FAIL**.

| Temperature case | Feed low / C2 / high (ohm) | PA case at 6.4 V, nominal / hottest corner (C) | Nominal at 6.4 V (W) | Lowest, LPF median (W) | Lowest, LPF worst (W) | Every design lever at its best (W; margin dB) | Highest at 6.4 V (W) | Lowest (LPF median) reaches 3.97 W from (V) | Output at 8.4 V, highest (W) |
|---|---|---|---|---|---|---|---|---|---|
| 25 C, start of key-down (case 25 C) | 0.260 / 0.350 / 0.450 | 25.0 / 25.0 | 3.22 | 1.79 | 1.42 | 2.30 (-2.37) | 4.41 | above 8.4 | 8.35 |
| 25 C, key-down, -0.005 dB/K | 0.276 / 0.394 / 0.534 | 43.7 / 63.1 | 3.06 | 1.69 | 1.31 | 2.22 (-2.52) | 4.24 | above 8.4 | 7.96 |
| 25 C, key-down, -0.015 dB/K | 0.276 / 0.394 / 0.534 | 43.0 / 60.6 | 2.95 | 1.64 | 1.27 | 2.13 (-2.70) | 4.04 | above 8.4 | 7.41 |
| -10 C, key-down, PA no cold gain | 0.318 / 0.452 / 0.613 | 8.6 / 28.4 | 3.08 | 1.70 | 1.34 | 2.25 (-2.47) | 4.29 | above 8.4 | 8.01 |
| -10 C, start of key-down, PA +0.53 dB | 0.303 / 0.409 / 0.529 | -10.0 / -10.0 | 3.53 | 1.96 | 1.58 | 2.55 (-1.93) | 4.85 | above 8.4 | 9.08 |
| +45 C, key-down, -0.005 dB/K | 0.293 / 0.418 / 0.568 | 63.2 / 82.1 | 2.95 | 1.63 | 1.25 | 2.16 (-2.66) | 4.11 | above 8.4 | 7.75 |
| +45 C, key-down, -0.015 dB/K | 0.293 / 0.418 / 0.568 | 61.9 / 78.5 | 2.74 | 1.52 | 1.17 | 1.99 (-3.00) | 3.77 | above 8.4 | 6.95 |
| +45 C, case 100 C bound, -0.005 dB/K | 0.293 / 0.418 / 0.568 | 100.0 / 100.0 | 2.84 | 1.57 | 1.20 | 2.08 (-2.82) | 3.98 | above 8.4 | 7.62 |
| +45 C, case 100 C bound, -0.015 dB/K | 0.293 / 0.418 / 0.568 | 100.0 / 100.0 | 2.44 | 1.35 | 1.03 | 1.77 (-3.52) | 3.40 | above 8.4 | 6.53 |

Corners at 6.4 V in the reference case, 25 C, key-down, -0.005 dB/K (full parameter sets):
- Nominal (3.06 W): 25 C, key-down, -0.005 dB/K; drain feed level 0.35 ohm at 25 C part temperature (0.394 ohm in this case); efficiency 0.67; PA input 89.4 mW; 146 MHz; VDD exponent n 2.0; hand-match extra loss 0.25 dB; output loss 0.84 dB (copper term +0.063 dB); PA case 43.7 C at 6.4 V.
- Lowest, LPF worst case (1.31 W): 25 C, key-down, -0.005 dB/K; drain feed level 0.45 ohm at 25 C part temperature (0.534 ohm in this case); efficiency 0.55; PA input 45.8 mW; 144 MHz; VDD exponent n 2.3; hand-match extra loss 0.5 dB; output loss 1.86 dB (copper term +0.151 dB).
- Lowest, LPF at most its median (1.69 W): 25 C, key-down, -0.005 dB/K; drain feed level 0.45 ohm at 25 C part temperature (0.534 ohm in this case); efficiency 0.55; PA input 45.8 mW; 144 MHz; VDD exponent n 2.3; hand-match extra loss 0.5 dB; output loss 0.84 dB (copper term +0.063 dB).
- Highest (4.24 W): 25 C, key-down, -0.005 dB/K; drain feed level 0.26 ohm at 25 C part temperature (0.276 ohm in this case); efficiency 0.67; PA input 180.0 mW; 148 MHz; VDD exponent n 1.8; hand-match extra loss 0.0 dB; output loss 0.5 dB (copper term +0.034 dB).
- Lowest with every design lever at its best (2.22 W): 25 C, key-down, -0.005 dB/K; drain feed level 0.26 ohm at 25 C part temperature (0.276 ohm in this case); efficiency 0.55; PA input 45.8 mW; 144 MHz; VDD exponent n 2.3; hand-match extra loss 0.0 dB; output loss 0.5 dB (copper term +0.034 dB).
- Worst key-down case (+45 C, case 100 C bound, -0.015 dB/K), lowest, LPF at most its median (1.35 W): +45 C, case 100 C bound, -0.015 dB/K; drain feed level 0.45 ohm at 25 C part temperature (0.568 ohm in this case); efficiency 0.55; PA input 45.8 mW; 144 MHz; VDD exponent n 2.3; hand-match extra loss 0.5 dB; output loss 0.84 dB (copper term +0.092 dB).

- Drain voltage at 6.4 V, reference case: nominal 5.93 V, lowest 5.55 V (key-down sag).
- Device output at 8.4 V, reference case: nominal 6.45 W, highest corner 7.96 W (ALC open; the ALC must hold 5 W).
- Nominal corner reaches 3.97 W from 7.3 V and 5.0 W from 8.25 V in the reference case.
- Drive corners used (from 2026-09-28-r1-d3-drive-a4): [0.04584252303370577, 0.08940778495013711, 0.17996843773094262].
- Sensitivity at 6.4 V in the reference case (dB spread across each input's values, averaged over the other corners; the temperature row over the low-bound cases): drive 1.94; output loss 1.48; temperature (the low-bound cases) 1.24; VDD exponent 0.44; hand-match loss 0.43; drain feed 0.42; frequency 0.22; efficiency 0.15.

Plots: `power_a4_sma.png` (versus pack voltage, with the lowest corner per temperature case), `power_a4_temperature.png` (at 6.4 V per temperature case, against 3.97 W). Deck `power_a4.cir`; LTspice log and raw beside it; numbers in `result.json`.
