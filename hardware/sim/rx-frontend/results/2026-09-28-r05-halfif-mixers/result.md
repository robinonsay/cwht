# 2026-09-28-r05-halfif-mixers: result

Checker: check_halfif.py. This run characterizes the mixers; the REQ-SYS-033 verdict for the half-IF response is made in the cascade run (r06) with the front-end gain and the filter attenuation at the half-IF frequency.

## halfif_ring: A5 diode ring, 4 x 1N5711

| set | LO duty | Gc (dB) | zero-RF floor at 8 MHz (dBm) | half-IF tone levels (dBm) | IF response re wanted at same level (dBc) | points used | fitted slope, all points (dB/dB) | IIP2 half-IF (dBm, slope 2, worst valid point) |
|---|---|---|---|---|---|---|---|---|
| 0 | 50 % | -5.14 | -232.9 | -40, -30, -20, -10, 0 | -77.8, -77.8, -77.8, -77.9, -78.4 | n, n, n, n, n | 0.99 | >= 67.8 |
| 1 | 45 % | -5.15 | - | -20, -10, 0 | -70.7, -70.5, -63.6 | n, n, y | 1.35 | 63.6 |
| 2 | 55 % | -5.19 | - | -20, -10, 0 | -68.1, -61.8, -57.3 | n, y, y | 1.54 | 51.8 |
| 3 | 45 % | -5.24 | - | -20, -10, 0 | -74.2, -68.8, -58.7 | n, n, y | 1.77 | 58.7 |
| 4 | 55 % | -5.21 | - | -20, -10, 0 | -74.6, -66.3, -59.5 | n, y, y | 1.76 | 56.3 |

Relative (time-step) floor used: -77.8 dBc (from the matched set when its response has slope near 1, else -84 dBc).

![halfif_ring_halfif.png](halfif_ring_halfif.png)

## halfif_jfet: A4 single J310 mixer

| set | LO duty | Gc (dB) | zero-RF floor at 8 MHz (dBm) | half-IF tone levels (dBm) | IF response re wanted at same level (dBc) | points used | fitted slope, all points (dB/dB) | IIP2 half-IF (dBm, slope 2, worst valid point) |
|---|---|---|---|---|---|---|---|---|
| 0 | 50 % | -12.19 | - | -20, -15, -8, -5 | -50.4, -48.1, -41.5, -38.5 | y, y, y, y | 1.81 | 30.4 |
| 1 | 45 % | -12.00 | - | -20, -5 | -50.1, -35.7 | y, y | 1.96 | 30.1 |

Relative (time-step) floor used: -84.0 dBc (from the matched set when its response has slope near 1, else -84 dBc).

Cases that did not complete in LTspice (not used): case 2 (140 MHz, -150 dBm, duty 50 %); case 4 (140 MHz, -10 dBm, duty 50 %); case 6 (140 MHz, 0 dBm, duty 50 %); case 8 (140 MHz, -150 dBm, duty 45 %); case 10 (140 MHz, -10 dBm, duty 45 %); case 12 (140 MHz, 0 dBm, duty 45 %); case 13 (140 MHz, -100 dBm, duty 50 %); case 14 (140 MHz, -120 dBm, duty 50 %)

![halfif_jfet_halfif.png](halfif_jfet_halfif.png)

