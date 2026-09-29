# 2026-09-28-r1-p1-power-a5: A5 output power at the SMA versus pack voltage (REQ-SYS-012), revision 1

Every figure is an estimate built on graph-read typical vendor curves and estimated feed, efficiency and loss terms (analysis record section 3); the corners bound the stated input ranges, not the unknowns listed as limitations.

Verdict, lowest corner at least 3.97 W from 6.4 to 8.4 V (typical module), at 25 C: **FAIL**; over every temperature case (the cold case with no PA gain): **FAIL** (worst 2.77 W at 6.4 V).
Verdict, lowest corner with the C2 and C3 levers (feed at most 0.35 ohm at 25 C, VGG 3.5 V) at least 3.97 W at 6.4 V over every temperature case: **FAIL** (worst 3.26 W; 25 C 4.28 W).

| Temperature case | Feed low / C2 / high (ohm) | Nominal at 6.4 V (W) | Lowest at 6.4 V (W) | Lowest with C2 and C3 (W) | Margin with C2 and C3 (dB) | Datasheet-minimum module with C2 and C3 (W) | Highest at 6.4 V (W) | Lowest reaches 3.97 W from (V) | Module or device output at 8.4 V, highest (W) |
|---|---|---|---|---|---|---|---|---|---|
| 25 C | 0.260 / 0.350 / 0.450 | 4.85 | 3.68 | 4.28 | +0.32 | 3.47 | 5.45 | 6.7 | 9.90 |
| -10 C, PA +0 dB | 0.302 / 0.411 / 0.540 | 4.69 | 3.50 | 4.10 | +0.14 | 3.36 | 5.32 | 6.85 | 9.69 |
| -10 C, PA +0.53 dB | 0.302 / 0.411 / 0.540 | 5.16 | 3.81 | 4.50 | +0.54 | 3.70 | 5.89 | 6.55 | 10.76 |
| +45 C, case 80 C, -0.005 dB/K | 0.293 / 0.417 / 0.568 | 4.34 | 3.21 | 3.81 | -0.18 | 3.11 | 4.95 | 7.15 | 9.20 |
| +45 C, case 80 C, -0.015 dB/K | 0.293 / 0.417 / 0.568 | 3.91 | 2.92 | 3.45 | -0.62 | 2.80 | 4.44 | 7.5 | 8.25 |
| +45 C, case 100 C, -0.005 dB/K | 0.293 / 0.417 / 0.568 | 4.26 | 3.16 | 3.74 | -0.26 | 3.05 | 4.85 | 7.25 | 9.02 |
| +45 C, case 100 C, -0.015 dB/K | 0.293 / 0.417 / 0.568 | 3.69 | 2.77 | 3.26 | -0.86 | 2.64 | 4.17 | 7.75 | 7.77 |

Corners at 25 C and 6.4 V (full parameter sets):
- Nominal (4.85 W): 25 C; drain feed level 0.35 ohm at 25 C (0.350 ohm at this temperature); efficiency 0.60; PA input 10.57 dBm; 146 MHz; VGG 3.5 V; typical module; output loss 0.5 dB (+0.0 dB copper term).
- Lowest (3.68 W): 25 C; drain feed level 0.45 ohm at 25 C (0.450 ohm at this temperature); efficiency 0.45; PA input 7.31 dBm; 148 MHz; VGG 3.08 V; typical module; output loss 0.6 dB (+0.0 dB copper term).
- Highest (5.45 W): 25 C; drain feed level 0.26 ohm at 25 C (0.260 ohm at this temperature); efficiency 0.60; PA input 15.50 dBm; 144 MHz; VGG 3.5 V; typical module; output loss 0.4 dB (+0.0 dB copper term).
- Lowest with the C2 and C3 levers (4.28 W; revision 0 quoted 4.31 W for this corner): 25 C; drain feed level 0.35 ohm at 25 C (0.350 ohm at this temperature); efficiency 0.45; PA input 7.31 dBm; 148 MHz; VGG 3.5 V; typical module; output loss 0.6 dB (+0.0 dB copper term).
- Datasheet-minimum module, lowest with the levers (3.47 W): 25 C; drain feed level 0.35 ohm at 25 C (0.350 ohm at this temperature); efficiency 0.45; PA input 7.31 dBm; 148 MHz; VGG 3.5 V; datasheet-minimum module; output loss 0.6 dB (+0.0 dB copper term).
- Worst temperature case (+45 C, case 100 C, -0.015 dB/K), lowest with the levers: +45 C, case 100 C, -0.015 dB/K; drain feed level 0.35 ohm at 25 C (0.417 ohm at this temperature); efficiency 0.45; PA input 7.31 dBm; 148 MHz; VGG 3.5 V; typical module; output loss 0.6 dB (+0.1 dB copper term).

- Drain voltage at 6.4 V, 25 C: nominal 5.76 V, lowest 5.35 V (key-down sag).
- Module or device output at 8.4 V, 25 C: nominal 9.09 W, highest corner 9.90 W (ALC open; the ALC must hold 5 W).
- Drive corners used (from 2026-09-28-r1-d2-drive-a5): [7.309240051163477, 10.574659210423574, 15.496228427664747].
- Sensitivity at 6.4 V (dB spread across each input's values, averaged over the other corners; 25 C except the temperature row): temperature (-10 to +45 C cases) 1.20; module spread (typical against datasheet minimum) 0.95; drain feed 0.44; VGG clamp 0.41; drive 0.36; output loss 0.20; efficiency 0.20; frequency 0.03.
- Open loop at 8.4 V, highest corner: 9.90 W at 25 C, 10.76 W at -10 C with the +0.53 dB estimate; above 8 W (stability guarantee) from 7.5 V at 25 C and 7.2 V at -10 C; above 10 W (maximum rating) from nowhere below 8.4 V at 25 C and 8.1 V at -10 C (input to WP-PDR-22).

Plots: `power_a5_sma.png` (versus pack voltage, with the lowest corner per temperature case), `power_a5_temperature.png` (at 6.4 V per temperature case, against 3.97 W). Deck `power_a5.cir`; LTspice log and raw beside it; numbers in `result.json`.
