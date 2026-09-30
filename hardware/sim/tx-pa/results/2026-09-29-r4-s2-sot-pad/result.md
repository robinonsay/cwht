# 2026-09-29-r4-s2-sot-pad: select-on-test pad on the D-13 bandpass chain, one-sided terms (revision 4, finding-1)

Units: 2700 (d6). The pad is chosen at 146 MHz with the unit's own coax in place. Per unit the drive over 144 to 148 MHz moves from its 146 MHz value by at most +0.360 dB and -0.777 dB (revision 3 used +/-0.565 dB, half the 1.131 dB span).

| Term | Upward (dB) | Downward (dB) |
|---|---|---|
| Frequency, one-sided from the 146 MHz value | 0.360 | 0.777 |
| Half the pad set's largest gap | 0.385 | 0.385 |
| Level reading, k1 method M2 | 0.640 | 0.640 |
| Drift in service | 0.387 | 0.387 |
| **Sum** | **1.772** | **2.189** |

Target re-centred: sqrt(10 x 30) x 10^((down - up)/20) = 18.17 mW, taken as **18.2 mW (TBR)**.

In service at 18.2 mW with the M2 reading: 10.99 to 27.37 mW, margins +0.41 dB above 10 mW and +0.40 dB below 30 mW: **PASS**.
At the +/-1.0 dB allocation: 10.12 to 29.74 mW (**PASS**). Break-even reading +/-1.04 dB.
Revision 3 target 17.3 mW with the one-sided terms: M2 10.45 to 26.02 mW; +/-1.0 dB 9.62 to 28.27 mW (**FAIL**); +/-0.8 dB 10.07 to 26.99 mW; break-even +/-0.83 dB.

Pad losses needed at 18.2 mW: 13.60 to 21.65 dB. Pad set (14 E24 1 % pi pads, largest gap 0.77 dB):

| Loss (dB) | Shunt, series, shunt (ohm) | Return loss (dB) |
|---|---|---|
| 13.48 | 75, 110, 75 | 38.6 |
| 14.06 | 68, 110, 68 | 26.8 |
| 14.57 | 68, 120, 68 | 29.3 |
| 15.32 | 75, 150, 75 | 30.9 |
| 15.92 | 68, 150, 68 | 42.6 |
| 16.52 | 62, 150, 62 | 27.5 |
| 17.09 | 68, 180, 68 | 37.9 |
| 17.79 | 68, 200, 68 | 32.5 |
| 18.44 | 68, 220, 68 | 29.6 |
| 19.14 | 56, 200, 56 | 25.4 |
| 19.88 | 68, 270, 68 | 25.8 |
| 20.52 | 62, 270, 62 | 37.8 |
| 21.29 | 62, 300, 62 | 33.6 |
| 22.04 | 56, 300, 56 | 33.0 |

| Reading uncertainty (dB) | Band at the target (mW) | Margin above 10 mW (dB) | Margin below 30 mW (dB) | Verdict |
|---|---|---|---|---|
| +/-0.25 | 12.03 to 25.02 | +0.80 | +0.79 | PASS |
| +/-0.50 | 11.35 to 26.50 | +0.55 | +0.54 | PASS |
| +/-0.64 | 10.99 to 27.37 | +0.41 | +0.40 | PASS |
| +/-0.80 | 10.60 to 28.40 | +0.25 | +0.24 | PASS |
| +/-1.00 | 10.12 to 29.74 | +0.05 | +0.04 | PASS |
| +/-1.50 | 9.02 to 33.37 | -0.45 | -0.46 | FAIL |
| +/-2.00 | 8.04 to 37.44 | -0.95 | -0.96 | FAIL |

Plot `sot_band_r4.png`.
