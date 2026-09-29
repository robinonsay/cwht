# 2026-09-29-r3-s2-sot-pad: select-on-test pad for the D-13 bandpass chain (revision 3)

Units: 2700 (source R, GVA gain, P1dB set, Si5351 case, coax 5 to 15 cm, bandpass case, coil Q). The pad is chosen at build at 146 MHz for 17.3 mW, with the unit's own coax in place; in service only frequency, the pad step, the reading and drift remain.

| Term | dB |
|---|---|
| Frequency span within a unit (144 to 148 MHz), half | 0.565 |
| Half the pad set's largest gap | 0.385 |
| Level reading, k1 method M2 bound | 0.640 |
| Drift: revision 2 terms 0.3 dB plus the bandpass coil TCL 0.087 dB | 0.387 |
| **Half-width, worst-case sum (RSS)** | **1.978 (1.014)** |

In-service drive 11.0 to 27.3 mW: overdrive margin +0.41 dB (+1.38 dB RSS), margin above 10 mW +0.40 dB: **PASS**. At the +/-1.0 dB allocation: 10.1 to 29.6 mW. Break-even reading +/-1.05 dB.

Pad losses the units need: 13.82 to 21.87 dB (coax 5 to 15 cm); 13.90 to 21.92 dB at any coax length (d7).

Pad set (14 E24 1 % pi pads, largest gap 0.77 dB):

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

| Reading uncertainty (dB) | Band (mW) | Overdrive margin (dB) | Verdict |
|---|---|---|---|
| +/-0.25 | 12.0 to 24.9 | +0.80 | PASS |
| +/-0.50 | 11.3 to 26.4 | +0.55 | PASS |
| +/-0.64 | 11.0 to 27.3 | +0.41 | PASS |
| +/-1.00 | 10.1 to 29.6 | +0.05 | PASS |
| +/-1.50 | 9.0 to 33.3 | -0.45 | FAIL |
| +/-2.00 | 8.0 to 37.3 | -0.95 | FAIL |

Plot `sot_band.png`.
