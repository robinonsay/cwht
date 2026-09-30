# 2026-09-29-r4-s4-clamp-step: the clamp ceiling as a per-unit build step (revision 4, finding-2)

## (a) Fixed clamp against the module's upper spread (8.4 V, Python replica of the deck model)

| Ceiling | u (dB) | Highest module with the revision 3 clamp (top V) (W) | Fixed top set on +u +0.07 dB (V) | Typical unit's lowest, LPF MC 99 % (W) | With the terms (dB) |
|---|---|---|---|---|---|
| D-9 (8 W) | 0.0 | 7.90 (2.859) | 2.849 | 1.97 | -3.19 |
| D-9 (8 W) | 0.3 | 8.39 (2.859) | 2.815 | 1.67 | -3.91 |
| D-9 (8 W) | 0.5 | 8.73 (2.859) | 2.794 | 1.48 | -4.43 |
| D-9 (8 W) | 1.0 | 9.65 (2.859) | 2.751 | 1.08 | -5.79 |
| D-9 (8 W) | 1.5 | 10.67 (2.859) | 2.722 | 0.90 | -6.61 |
| scenario B (10 W) | 0.0 | 9.90 (3.120) | 3.089 | 4.36 | +0.25 |
| scenario B (10 W) | 0.3 | 10.51 (3.120) | 2.990 | 4.07 | -0.04 |
| scenario B (10 W) | 0.5 | 10.94 (3.120) | 2.950 | 3.91 | -0.22 |
| scenario B (10 W) | 1.0 | 12.06 (3.120) | 2.867 | 3.51 | -0.68 |
| scenario B (10 W) | 1.5 | 13.26 (3.120) | 2.807 | 3.13 | -1.18 |

## (b) Terms of the step (worst-case sum)

| Term | Low side, g- (dB) | High side, g+ (dB) | Class |
|---|---|---|---|
| Open-loop power reading, diode probe at the TC-SYS-010 bound (15 %) | 0.706 | 0.607 | TC-SYS-010 criterion |
| unit output loss (LPF and relay) from the NanoVNA S21 at 144, 146 and 148 MHz | 0.100 | 0.100 | est. |
| trim resolution: half of a 0.1 dB step | 0.050 | 0.050 | est.; WP-PDR-22 sets the step |
| RA07M1317M curve graph read (VGG and VDD curves, from the bench point to the service cases) | 0.070 | 0.070 | est., revision 2 term |
| bench temperature and self-heating during the 3 s reading, projected to the service case | 0.050 | 0.050 | est. |
| drive drift in service (s2 drift 0.39 dB) times the module Pout-Pin slope at 27.4 mW | 0.012 | 0.012 | digitized curve (est.) |
| **Sum** | **0.987** | **0.889** | |

## (c) Replica over the module spread (every key-down case, LPF at most its MC 99th percentile; highest over the open-loop cases)

### p4: ceiling 8 W, step target 6.293 W

| Module | e (dB) | Lowest at 6.4 V (W) | Lowest at 8.4 V (W) | Highest at 6.4 V (W) | Highest at 8.4 V (W) |
|---|---|---|---|---|---|
| datasheet minimum | -0.99 | 2.26 | 3.43 | 5.14 | 7.72 |
| datasheet minimum | +0.00 | 2.26 | 1.83 | 5.14 | 6.29 |
| datasheet minimum | +0.89 | 2.26 | 1.04 | 5.14 | 5.36 |
| typical +0.0 dB | -0.99 | 2.76 | 2.15 | 6.45 | 7.71 |
| typical +0.0 dB | +0.00 | 2.76 | 1.15 | 6.29 | 6.29 |
| typical +0.0 dB | +0.89 | 1.99 | 0.81 | 5.46 | 5.36 |
| typical +0.5 dB | -0.99 | 3.00 | 1.77 | 7.10 | 7.71 |
| typical +0.5 dB | +0.00 | 2.75 | 1.07 | 6.29 | 6.29 |
| typical +0.5 dB | +0.89 | 1.58 | 0.73 | 5.46 | 5.36 |
| typical +1.0 dB | -0.99 | 3.26 | 1.43 | 7.59 | 7.71 |
| typical +1.0 dB | +0.00 | 2.29 | 0.97 | 6.29 | 6.29 |
| typical +1.0 dB | +0.89 | 1.30 | 0.64 | 5.55 | 5.36 |
| typical +1.5 dB | -0.99 | 3.37 | 1.33 | 7.59 | 7.71 |
| typical +1.5 dB | +0.00 | 1.83 | 0.87 | 6.29 | 6.29 |
| typical +1.5 dB | +0.89 | 1.06 | 0.58 | 5.55 | 5.36 |

### p5: ceiling 10 W, step target 7.887 W

| Module | e (dB) | Lowest at 6.4 V (W) | Lowest at 8.4 V (W) | Highest at 6.4 V (W) | Highest at 8.4 V (W) |
|---|---|---|---|---|---|
| datasheet minimum | -0.99 | 2.32 | 3.91 | 5.14 | 8.56 |
| datasheet minimum | +0.00 | 2.32 | 3.91 | 5.14 | 7.89 |
| datasheet minimum | +0.89 | 2.32 | 3.40 | 5.14 | 6.82 |
| typical +0.0 dB | -0.99 | 2.82 | 4.77 | 6.45 | 9.61 |
| typical +0.0 dB | +0.00 | 2.82 | 4.09 | 6.45 | 7.89 |
| typical +0.0 dB | +0.89 | 2.82 | 3.24 | 6.45 | 6.81 |
| typical +0.5 dB | -0.99 | 3.07 | 5.14 | 7.10 | 9.61 |
| typical +0.5 dB | +0.00 | 3.07 | 4.01 | 7.10 | 7.89 |
| typical +0.5 dB | +0.89 | 3.07 | 3.16 | 6.68 | 6.81 |
| typical +1.0 dB | -0.99 | 3.33 | 5.05 | 7.79 | 9.61 |
| typical +1.0 dB | +0.00 | 3.33 | 3.90 | 7.79 | 7.89 |
| typical +1.0 dB | +0.89 | 3.33 | 3.13 | 6.81 | 6.81 |
| typical +1.5 dB | -0.99 | 3.60 | 4.96 | 8.53 | 9.61 |
| typical +1.5 dB | +0.00 | 3.60 | 3.82 | 7.89 | 7.89 |
| typical +1.5 dB | +0.89 | 3.55 | 3.09 | 6.98 | 6.81 |

Replica against the decks at 8.4 V: p4: lowest 0.576 / 0.576 W, highest 7.716 / 7.716 W; p5: lowest 3.091 / 3.090 W, highest 9.609 / 9.609 W

## (d) Reading break-even (step basis at 8.4 V, read high by the bound)

| Ceiling | Reading (+/- %) | g- (dB) | g+ (dB) | Step target (W) | Lowest at 8.4 V (W) | With the terms (dB) |
|---|---|---|---|---|---|---|
| 8 W | 0 | 0.282 | 0.282 | 7.404 | 1.09 | -5.76 |
| 8 W | 2 | 0.369 | 0.368 | 7.256 | 1.01 | -6.10 |
| 8 W | 5 | 0.504 | 0.493 | 7.034 | 0.89 | -6.65 |
| 8 W | 10 | 0.739 | 0.696 | 6.664 | 0.70 | -7.66 |
| 8 W | 15 | 0.987 | 0.889 | 6.293 | 0.58 | -8.53 |
| 8 W | 20 | 1.251 | 1.073 | 5.923 | 0.46 | -9.52 |
| 10 W | 0 | 0.282 | 0.282 | 9.278 | 4.39 | +0.28 |
| 10 W | 2 | 0.369 | 0.368 | 9.093 | 4.16 | +0.05 |
| 10 W | 5 | 0.504 | 0.493 | 8.815 | 3.88 | -0.25 |
| 10 W | 10 | 0.739 | 0.696 | 8.351 | 3.47 | -0.73 |
| 10 W | 15 | 0.987 | 0.889 | 7.887 | 3.09 | -1.24 |
| 10 W | 20 | 1.251 | 1.073 | 7.423 | 2.77 | -1.72 |

Note: at a perfect reading the other step terms alone leave the scenario B basis at 4.39 W at 8.4 V (+0.28 dB with the terms).

Plot `clamp_step.png`.
