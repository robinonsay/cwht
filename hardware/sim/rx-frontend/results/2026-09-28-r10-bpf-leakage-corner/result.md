# 2026-09-28-r10-bpf-leakage-corner: result

Checker: worst_case.py check r10. Question (review finding 5): how much stray input-to-output capacitance per section is tolerable when the tolerances and ports are at their corners, with the leak phase unknown?
Worst-phase bound: the leak is an ideal copy of the section input voltage times exp(j phi) through the stray C; phi takes 16 values and is chosen worst separately at the tuned and at the image frequency, per section (a bound: one physical leak has one phase). Design-input corner: mode B, aligned at 50 ohm, residual +/-0.3 %, every internal port within VSWR 1.2, coil Q 100. LTspice can take only a real SGN (+1 or -1), so its re-simulation checks the model at those phases (agreement 0.01 dB), not the bound.

## 2 + 3 + 3, IF 8 MHz (revision 1 proposal)

| stray C per section (pF) | nominal, 50 ohm (dB) | mode B corner, 50 ohm ports (dB) | design-input corner, VSWR 1.2 ports (dB) |
|---|---|---|---|
| 0 | 86.0 | 75.6 | 72.1 |
| 0.003 | 85.7 | 75.4 | 71.9 |
| 0.01 | 84.9 | 75.0 | 71.4 |
| 0.02 | 83.9 | 74.4 | 70.8 |
| 0.03 | 82.9 | 73.7 | 70.2 |
| 0.05 | 81.0 | 72.6 | 69.0 |
| 0.1 | 77.0 | 69.9 | 66.4 |

At the proposed stray limit of 0.03 pF per section: design-input corner 70.2 dB, **PASS**, margin +0.2 dB.

| LTspice case | numpy (dB) | LTspice (dB) | agree |
|---|---|---|---|
| design-input corner, stray 0 pF, SGN from the tuned-frequency worst phase | 72.07 | 72.07 | yes |
| design-input corner, stray 0.03 pF, SGN from the tuned-frequency worst phase | 73.87 | 73.87 | yes |
| design-input corner, stray 0.03 pF, SGN from the image-frequency worst phase | 70.28 | 70.28 | yes |
| design-input corner, stray 0.1 pF, SGN from the tuned-frequency worst phase | 78.98 | 78.98 | yes |
| design-input corner, stray 0.1 pF, SGN from the image-frequency worst phase | 66.64 | 66.64 | yes |

## 2 + 3 + 4, IF 8 MHz (margin lever, new here)

| stray C per section (pF) | nominal, 50 ohm (dB) | mode B corner, 50 ohm ports (dB) | design-input corner, VSWR 1.2 ports (dB) |
|---|---|---|---|
| 0 | 103.9 | 91.4 | 87.8 |
| 0.003 | 102.1 | 90.6 | 86.9 |
| 0.01 | 98.8 | 88.9 | 85.2 |
| 0.02 | 95.3 | 86.8 | 83.0 |
| 0.03 | 92.5 | 84.1 | 80.1 |
| 0.05 | 88.3 | 79.9 | 75.8 |
| 0.1 | 81.2 | 73.1 | 69.0 |

At the proposed stray limit of 0.03 pF per section: design-input corner 80.1 dB, **PASS**, margin +10.1 dB.

| LTspice case | numpy (dB) | LTspice (dB) | agree |
|---|---|---|---|
| design-input corner, stray 0 pF, SGN from the tuned-frequency worst phase | 87.77 | 87.77 | yes |
| design-input corner, stray 0.03 pF, SGN from the tuned-frequency worst phase | 81.97 | 81.97 | yes |
| design-input corner, stray 0.03 pF, SGN from the image-frequency worst phase | 80.17 | 80.17 | yes |
| design-input corner, stray 0.1 pF, SGN from the tuned-frequency worst phase | 75.38 | 75.38 | yes |
| design-input corner, stray 0.1 pF, SGN from the image-frequency worst phase | 69.21 | 69.21 | yes |

## 2 + 3 + 2, IF 10 MHz (alternative)

| stray C per section (pF) | nominal, 50 ohm (dB) | mode B corner, 50 ohm ports (dB) | design-input corner, VSWR 1.2 ports (dB) |
|---|---|---|---|
| 0 | 86.8 | 78.9 | 75.1 |
| 0.003 | 86.3 | 78.6 | 74.8 |
| 0.01 | 85.3 | 77.9 | 74.2 |
| 0.02 | 83.9 | 77.0 | 73.3 |
| 0.03 | 82.7 | 76.2 | 72.5 |
| 0.05 | 80.6 | 74.7 | 71.0 |
| 0.1 | 76.5 | 71.6 | 67.6 |

At the proposed stray limit of 0.03 pF per section: design-input corner 72.5 dB, **PASS**, margin +2.5 dB.

| LTspice case | numpy (dB) | LTspice (dB) | agree |
|---|---|---|---|
| design-input corner, stray 0 pF, SGN from the tuned-frequency worst phase | 75.11 | 75.11 | yes |
| design-input corner, stray 0.03 pF, SGN from the tuned-frequency worst phase | 77.59 | 77.59 | yes |
| design-input corner, stray 0.03 pF, SGN from the image-frequency worst phase | 72.52 | 72.52 | yes |
| design-input corner, stray 0.1 pF, SGN from the tuned-frequency worst phase | 76.72 | 76.72 | yes |
| design-input corner, stray 0.1 pF, SGN from the image-frequency worst phase | 67.71 | 67.71 | yes |

![leakage_corner.png](leakage_corner.png)

LTspice agreement with every numpy prediction: yes.
