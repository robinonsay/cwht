# 2026-09-30-r5-p4-power-a5-design: A5 D-9 (8 W), the added unit case of finding-31 (revision 5)

Deck: the revision 4 deck of `2026-09-29-r4-p4-power-a5-design` with one unit case, +2.49 dB true (believed +1.5 dB, the reject threshold), read low: true spread +2.487 dB above the typical curve, reading error -0.987 dB, believed +1.500 dB. Step target 6.293 W (design 7.9 W, g- 0.987 dB). 1944 LTspice steps. All figures estimates.

Checks and verdicts:
- check: the step terms and the step target equal revision 4's (g-, g+, target within 1e-9): **PASS** (g- 0.9874 dB, g+ 0.8886 dB)
- check: the added case's believed spread (true + error) equals the reject threshold (+1.5 dB) within 1e-9 dB: **PASS** (true +2.4874 dB, error -0.9874 dB)
- check: one .raw step per corner: **PASS** (1944 steps)
- check: PA case temperature equals the thermal law within 0.01 K at every pack voltage: **PASS** (largest difference 7.63e-06 K)
- check: the deck clamp equals the checker's per-unit clamp within LTspice's reltol (0.1 % + 0.1 mV) at every pack voltage: **PASS** (largest difference 0.87 of the tolerance)
- check: VGG at most 3.50 V at every corner and pack voltage: **PASS** (highest 3.5000 V)
- check: pack current equals IBUS + Pmod / (eta Vd) within 0.2 % (reltol on V(pmod) and V(d)) at every corner and pack voltage: **PASS** (largest deviation 0.1108 %)
- check: the Python replica equals the deck at 6.4 and 8.4 V within 0.5 % (module output and pack current, every corner): **PASS** (largest deviation 0.100 %)
- A5 open loop, the added unit case (true +1.5 + g- dB, read low; believed at the reject threshold), 6.4 to 8.4 V, every case: module output at most 8 W: **PASS** (7.736 W)

Clamp top: 2.846 to 3.500 V at 6.4 V, 2.669 to 2.715 V at 8.4 V.

| Temperature case | Highest module output (W) | Pack current, 6.4 to 8.4 V (A) | Pack current at 6.4 V (A) | Module dissipation, 6.4 to 8.4 V (W) | PA case, highest (C) |
|---|---|---|---|---|---|
| 25 C, start of key-down (case 25 C) | 7.45 | 3.58 | 3.58 | 8.89 | 25.0 |
| 25 C, key-down, -0.005 dB/K | 6.91 | 3.30 | 3.30 | 8.32 | 75.8 |
| 25 C, key-down, -0.015 dB/K | 6.59 | 3.08 | 3.08 | 7.65 | 71.7 |
| -10 C, key-down, PA no cold gain | 6.91 | 3.22 | 3.22 | 8.08 | 39.4 |
| -10 C, start of key-down, PA +0.53 dB | 7.74 | 3.70 | 3.70 | 9.42 | -10.0 |
| +45 C, key-down, -0.005 dB/K | 6.71 | 3.20 | 3.20 | 8.09 | 94.4 |
| +45 C, key-down, -0.015 dB/K | 6.19 | 2.92 | 2.92 | 7.22 | 89.1 |
| +45 C, case 100 C bound, -0.005 dB/K | 6.57 | 3.18 | 3.18 | 8.05 | 100.0 |
| +45 C, case 100 C bound, -0.015 dB/K | 5.81 | 2.83 | 2.83 | 7.01 | 100.0 |

Plot `power_a5_added_case_d9.png`. Deck `power_a5_step.cir`; LTspice log beside it; `.raw` per `raw.sha256` when over 5,000,000 bytes.
