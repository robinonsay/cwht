# 2026-09-30-r5-s5-pass-population: the population that passes the clamp step's reject rule (revision 5, finding-31)

The reject rule acts on the believed spread (true spread plus reading error): a unit passes when its believed spread is at most +1.5 dB. Revision 4's seven unit cases (runs r4-p4, r4-p5, re-read) and the added case (runs r5-p4, r5-p5). Design feeds (low, mid, bound); ALC at its top; 6.4 to 8.4 V. All figures estimates.

Checks and verdicts:
- check: the revision 4 .raw of 2026-09-29-r4-p4-power-a5-design matches its committed raw.sha256: **PASS**
- check: run_a5_r4.py regenerates the committed revision 4 deck of 2026-09-29-r4-p4-power-a5-design (SHA-256 equal): **PASS**
- A5 open loop, every unit that passes the reject rule (believed spread at most +1.5 dB, true spread up to +1.5 + g- dB), 6.4 to 8.4 V, every case: module output at most 8 W (D-9 (8 W)): **PASS** (7.736 W)
- check: over the passing region the replica's highest pack current is at the added case (true +1.5 + g-, read low) and equals the deck within 0.5 % (D-9 (8 W)): **PASS** (t25a: replica 3.303 A at (+2.49, -0.99) dB, deck 3.303 A; hot45a: replica 3.203 A at (+2.49, -0.99) dB, deck 3.203 A)
- check: the revision 4 .raw of 2026-09-29-r4-p5-power-a5-clamp-b matches its committed raw.sha256: **PASS**
- check: run_a5_r4.py regenerates the committed revision 4 deck of 2026-09-29-r4-p5-power-a5-clamp-b (SHA-256 equal): **PASS**
- A5 open loop, every unit that passes the reject rule (believed spread at most +1.5 dB, true spread up to +1.5 + g- dB), 6.4 to 8.4 V, every case: module output at most 10 W (scenario B (10 W)): **PASS** (9.648 W)
- check: over the passing region the replica's highest pack current is at the added case (true +1.5 + g-, read low) and equals the deck within 0.5 % (scenario B (10 W)): **PASS** (t25a: replica 3.680 A at (+2.49, -0.99) dB, deck 3.680 A; hot45a: replica 3.598 A at (+2.49, -0.99) dB, deck 3.598 A)

## D-9 (8 W)

| Unit case | True (dB) | Error (dB) | Believed (dB) | Passes the rule | Highest module (W) | Pack current 25 C / +45 C key-down (A) | Dissipation 25 C / +45 C key-down (W) |
|---|---|---|---|---|---|---|---|
| typical, read exactly | +0.00 | +0.00 | +0.00 | yes | 6.30 | 2.38 / 2.33 | 6.97 / 6.77 |
| typical, read high by the bound | +0.00 | +0.89 | +0.89 | yes | 5.54 | 2.26 / 2.21 | 6.12 / 5.90 |
| typical, read low by the bound | +0.00 | -0.99 | -0.99 | yes | 7.74 | 2.55 / 2.49 | 8.27 / 8.05 |
| +1.5 dB (trim-range top), read high | +1.50 | +0.89 | +2.39 | no | 5.57 | 2.44 / 2.38 | 6.18 / 5.95 |
| +1.5 dB (trim-range top), read low | +1.50 | -0.99 | +0.51 | yes | 7.74 | 3.00 / 2.93 | 8.32 / 8.09 |
| datasheet minimum, read high | +0.00 | +0.89 | +0.89 | yes | 5.46 | 1.97 / 1.93 | 5.97 / 5.77 |
| datasheet minimum, read low | +0.00 | -0.99 | -0.99 | yes | 7.73 | 2.23 / 2.19 | 8.23 / 8.03 |
| +2.49 dB true (believed +1.5 dB, the reject threshold), read low | +2.49 | -0.99 | +1.50 | yes | 7.74 | 3.30 / 3.20 | 8.32 / 8.09 |

| Temperature case | Pack current, revision 4 cases (A) | Pack current, passing population (A) | Dissipation, revision 4 cases (W) | Dissipation, passing population (W) | PA case, revision 4 / passing (C) |
|---|---|---|---|---|---|
| 25 C, start of key-down (case 25 C) | 3.19 | 3.58 | 8.86 | 8.89 | 25.0 / 25.0 |
| 25 C, key-down, -0.005 dB/K | 3.00 | 3.30 | 8.32 | 8.32 | 75.8 / 75.8 |
| 25 C, key-down, -0.015 dB/K | 2.76 | 3.08 | 7.65 | 7.65 | 71.7 / 71.7 |
| -10 C, key-down, PA no cold gain | 2.96 | 3.22 | 8.08 | 8.08 | 39.4 / 39.4 |
| -10 C, start of key-down, PA +0.53 dB | 3.41 | 3.70 | 9.42 | 9.42 | -10.0 / -10.0 |
| +45 C, key-down, -0.005 dB/K | 2.93 | 3.20 | 8.09 | 8.09 | 94.4 / 94.4 |
| +45 C, key-down, -0.015 dB/K | 2.62 | 2.92 | 7.22 | 7.22 | 89.1 / 89.1 |
| +45 C, case 100 C bound, -0.005 dB/K | 2.91 | 3.18 | 8.05 | 8.05 | 100.0 / 100.0 |
| +45 C, case 100 C bound, -0.015 dB/K | 2.54 | 2.83 | 7.00 | 7.01 | 100.0 / 100.0 |

Highest module output over the passing population: 7.736 W (ceiling 8 W).

## scenario B (10 W)

| Unit case | True (dB) | Error (dB) | Believed (dB) | Passes the rule | Highest module (W) | Pack current 25 C / +45 C key-down (A) | Dissipation 25 C / +45 C key-down (W) |
|---|---|---|---|---|---|---|---|
| typical, read exactly | +0.00 | +0.00 | +0.00 | yes | 7.89 | 2.58 / 2.53 | 8.61 / 8.36 |
| typical, read high by the bound | +0.00 | +0.89 | +0.89 | yes | 6.97 | 2.46 / 2.40 | 7.62 / 7.36 |
| typical, read low by the bound | +0.00 | -0.99 | -0.99 | yes | 9.65 | 2.76 / 2.70 | 10.22 / 9.97 |
| +1.5 dB (trim-range top), read high | +1.50 | +0.89 | +2.39 | no | 6.98 | 2.94 / 2.87 | 7.82 / 7.57 |
| +1.5 dB (trim-range top), read low | +1.50 | -0.99 | +0.51 | yes | 9.65 | 3.29 / 3.22 | 10.30 / 10.02 |
| datasheet minimum, read high | +0.00 | +0.89 | +0.89 | yes | 6.84 | 2.15 / 2.10 | 7.39 / 7.16 |
| datasheet minimum, read low | +0.00 | -0.99 | -0.99 | yes | 8.56 | 2.29 / 2.25 | 8.82 / 8.60 |
| +2.49 dB true (believed +1.5 dB, the reject threshold), read low | +2.49 | -0.99 | +1.50 | yes | 9.65 | 3.68 / 3.60 | 10.37 / 10.08 |

| Temperature case | Pack current, revision 4 cases (A) | Pack current, passing population (A) | Dissipation, revision 4 cases (W) | Dissipation, passing population (W) | PA case, revision 4 / passing (C) |
|---|---|---|---|---|---|
| 25 C, start of key-down (case 25 C) | 3.52 | 3.95 | 11.09 | 11.13 | 25.0 / 25.0 |
| 25 C, key-down, -0.005 dB/K | 3.29 | 3.68 | 10.30 | 10.37 | 87.9 / 88.4 |
| 25 C, key-down, -0.015 dB/K | 2.96 | 3.32 | 9.32 | 9.43 | 81.9 / 82.6 |
| -10 C, key-down, PA no cold gain | 3.19 | 3.56 | 9.79 | 9.79 | 49.8 / 49.8 |
| -10 C, start of key-down, PA +0.53 dB | 3.79 | 4.22 | 11.71 | 11.71 | -10.0 / -10.0 |
| +45 C, key-down, -0.005 dB/K | 3.22 | 3.60 | 10.02 | 10.08 | 106.3 / 106.6 |
| +45 C, key-down, -0.015 dB/K | 2.81 | 3.15 | 8.80 | 8.91 | 98.8 / 99.4 |
| +45 C, case 100 C bound, -0.005 dB/K | 3.24 | 3.62 | 10.08 | 10.14 | 100.0 / 100.0 |
| +45 C, case 100 C bound, -0.015 dB/K | 2.80 | 3.14 | 8.77 | 8.90 | 100.0 / 100.0 |

Highest module output over the passing population: 9.648 W (ceiling 10 W).

Plots `pass_population.png` (the passing region with the replica's pack current), `pack_current_dissipation.png`.
