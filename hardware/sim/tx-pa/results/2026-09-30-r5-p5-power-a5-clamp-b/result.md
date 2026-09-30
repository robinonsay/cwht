# 2026-09-30-r5-p5-power-a5-clamp-b: A5 scenario B (10 W), the added unit case of finding-31 (revision 5)

Deck: the revision 4 deck of `2026-09-29-r4-p5-power-a5-clamp-b` with one unit case, +2.49 dB true (believed +1.5 dB, the reject threshold), read low: true spread +2.487 dB above the typical curve, reading error -0.987 dB, believed +1.500 dB. Step target 7.887 W (design 9.9 W, g- 0.987 dB). 1944 LTspice steps. All figures estimates.

Checks and verdicts:
- check: the step terms and the step target equal revision 4's (g-, g+, target within 1e-9): **PASS** (g- 0.9874 dB, g+ 0.8886 dB)
- check: the added case's believed spread (true + error) equals the reject threshold (+1.5 dB) within 1e-9 dB: **PASS** (true +2.4874 dB, error -0.9874 dB)
- check: one .raw step per corner: **PASS** (1944 steps)
- check: PA case temperature equals the thermal law within 0.01 K at every pack voltage: **PASS** (largest difference 1.53e-05 K)
- check: the deck clamp equals the checker's per-unit clamp within LTspice's reltol (0.1 % + 0.1 mV) at every pack voltage: **PASS** (largest difference 0.97 of the tolerance)
- check: VGG at most 3.50 V at every corner and pack voltage: **PASS** (highest 3.5000 V)
- check: pack current equals IBUS + Pmod / (eta Vd) within 0.2 % (reltol on V(pmod) and V(d)) at every corner and pack voltage: **PASS** (largest deviation 0.1133 %)
- check: the Python replica equals the deck at 6.4 and 8.4 V within 0.5 % (module output and pack current, every corner): **PASS** (largest deviation 0.100 %)
- A5 open loop, the added unit case (true +1.5 + g- dB, read low; believed at the reject threshold), 6.4 to 8.4 V, every case: module output at most 10 W: **PASS** (9.648 W)

Clamp top: 3.108 to 3.500 V at 6.4 V, 2.725 to 2.816 V at 8.4 V.

| Temperature case | Highest module output (W) | Pack current, 6.4 to 8.4 V (A) | Pack current at 6.4 V (A) | Module dissipation, 6.4 to 8.4 V (W) | PA case, highest (C) |
|---|---|---|---|---|---|
| 25 C, start of key-down (case 25 C) | 9.35 | 3.95 | 3.93 | 11.13 | 25.0 |
| 25 C, key-down, -0.005 dB/K | 8.64 | 3.68 | 3.68 | 10.37 | 88.4 |
| 25 C, key-down, -0.015 dB/K | 8.18 | 3.32 | 3.32 | 9.43 | 82.6 |
| -10 C, key-down, PA no cold gain | 8.63 | 3.56 | 3.56 | 9.79 | 49.8 |
| -10 C, start of key-down, PA +0.53 dB | 9.65 | 4.22 | 4.22 | 11.71 | -10.0 |
| +45 C, key-down, -0.005 dB/K | 8.38 | 3.60 | 3.60 | 10.08 | 106.6 |
| +45 C, key-down, -0.015 dB/K | 7.69 | 3.15 | 3.15 | 8.91 | 99.4 |
| +45 C, case 100 C bound, -0.005 dB/K | 8.27 | 3.62 | 3.62 | 10.14 | 100.0 |
| +45 C, case 100 C bound, -0.015 dB/K | 7.29 | 3.14 | 3.14 | 8.90 | 100.0 |

Plot `power_a5_added_case_clampb.png`. Deck `power_a5_step.cir`; LTspice log beside it; `.raw` per `raw.sha256` when over 5,000,000 bytes.
