# 2026-09-28-r1-p2-power-a4: A4 output power at the SMA versus pack voltage (REQ-SYS-012), revision 1

Every figure is an estimate built on graph-read typical vendor curves and estimated feed, efficiency and loss terms (analysis record section 3); the corners bound the stated input ranges, not the unknowns listed as limitations.

Verdict, lowest corner at least 3.97 W from 6.4 to 8.4 V, at 25 C: **FAIL**; over every temperature case (the cold case with no PA gain): **FAIL** (worst 1.42 W at 6.4 V).

| Temperature case | Feed low / C2 / high (ohm) | Nominal at 6.4 V (W) | Lowest at 6.4 V (W) | Highest at 6.4 V (W) | Lowest reaches 3.97 W from (V) | Module or device output at 8.4 V, highest (W) |
|---|---|---|---|---|---|---|
| 25 C | 0.260 / 0.350 / 0.450 | 3.48 | 1.90 | 4.51 | above 8.4 | 8.35 |
| -10 C, PA +0 dB | 0.302 / 0.411 / 0.540 | 3.40 | 1.84 | 4.43 | above 8.4 | 8.18 |
| -10 C, PA +0.53 dB | 0.302 / 0.411 / 0.540 | 3.77 | 2.04 | 4.94 | above 8.4 | 9.09 |
| +45 C, case 80 C, -0.005 dB/K | 0.293 / 0.417 / 0.568 | 3.13 | 1.69 | 4.11 | above 8.4 | 7.77 |
| +45 C, case 80 C, -0.015 dB/K | 0.293 / 0.417 / 0.568 | 2.80 | 1.51 | 3.66 | above 8.4 | 6.95 |
| +45 C, case 100 C, -0.005 dB/K | 0.293 / 0.417 / 0.568 | 3.07 | 1.65 | 4.02 | above 8.4 | 7.62 |
| +45 C, case 100 C, -0.015 dB/K | 0.293 / 0.417 / 0.568 | 2.63 | 1.42 | 3.44 | above 8.4 | 6.53 |

Corners at 25 C and 6.4 V (full parameter sets):
- Nominal (3.48 W): 25 C; drain feed level 0.35 ohm at 25 C (0.350 ohm at this temperature); efficiency 0.67; PA input 89.4 mW; 146 MHz; VDD exponent n 2.0; hand-match extra loss 0.25 dB; output loss 0.5 dB (+0.0 dB copper term).
- Lowest (1.90 W): 25 C; drain feed level 0.45 ohm at 25 C (0.450 ohm at this temperature); efficiency 0.55; PA input 45.8 mW; 144 MHz; VDD exponent n 2.3; hand-match extra loss 0.5 dB; output loss 0.6 dB (+0.0 dB copper term).
- Highest (4.51 W): 25 C; drain feed level 0.26 ohm at 25 C (0.260 ohm at this temperature); efficiency 0.67; PA input 180.0 mW; 148 MHz; VDD exponent n 1.8; hand-match extra loss 0.0 dB; output loss 0.4 dB (+0.0 dB copper term).
- Worst temperature case (+45 C, case 100 C, -0.015 dB/K), lowest: +45 C, case 100 C, -0.015 dB/K; drain feed level 0.45 ohm at 25 C (0.568 ohm at this temperature); efficiency 0.55; PA input 45.8 mW; 144 MHz; VDD exponent n 2.3; hand-match extra loss 0.5 dB; output loss 0.6 dB (+0.1 dB copper term).

- Drain voltage at 6.4 V, 25 C: nominal 5.97 V, lowest 5.65 V (key-down sag).
- Module or device output at 8.4 V, 25 C: nominal 6.77 W, highest corner 8.35 W (ALC open; the ALC must hold 5 W).
- Drive corners used (from 2026-09-28-r1-d3-drive-a4): [0.04584252303370577, 0.08940778495013711, 0.17996843773094262].
- Sensitivity at 6.4 V (dB spread across each input's values, averaged over the other corners; 25 C except the temperature row): drive 2.01; temperature (-10 to +45 C cases) 1.22; hand-match loss 0.44; VDD exponent 0.44; drain feed 0.33; frequency 0.23; output loss 0.20; efficiency 0.10.
- Nominal corner at 25 C reaches 3.97 W from 6.85 V and 5.0 W from 7.7 V.

Plots: `power_a4_sma.png` (versus pack voltage, with the lowest corner per temperature case), `power_a4_temperature.png` (at 6.4 V per temperature case, against 3.97 W). Deck `power_a4.cir`; LTspice log and raw beside it; numbers in `result.json`.
