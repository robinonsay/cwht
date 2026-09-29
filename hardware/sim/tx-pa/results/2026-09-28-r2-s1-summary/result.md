# 2026-09-28-r2-s1-summary: summary, select-on-test pad, overdrive and closure margins (revision 2)

Verdicts:
- A5 select-on-test drive 10 to 30 mW in service, reading allocation +/-1.0 dB: **PASS** (11.3 to 26.5 mW, overdrive margin +0.54 dB).
- A5 select-on-test drive 10 to 30 mW with a tinySA Ultra reading alone (+/-2 dB published): **FAIL** (overdrive margin -0.46 dB).
- A5 option d5 select-on-test drive 10 to 30 mW, reading allocation +/-1.0 dB: **PASS** (11.4 to 26.3 mW).

## A5 select-on-test drive pad (estimate)

| Interface | Frequency span in a unit (dB) | Half the pad set's largest gap (dB) | Band half-width, worst-case sum (dB) | Same, RSS (dB) | In-service drive (mW) | Overdrive margin to 30 mW (dB) | Margin above 10 mW (dB) | Break-even reading (+/- dB) | Pad set (dB) | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| as designed (coax, 18 dB pad on the RF board) | 0.34 | 0.38 | 1.85 | 1.13 | 11.3 to 26.5 | +0.54 (RSS +1.27) | +0.53 | 1.54 | 14 pads, 13.48 to 22.04 (13.51 to 21.50 needed) | **PASS** |
| option d5 (6 dB at the pin, 12 dB on the RF board) | 0.29 | 0.38 | 1.82 | 1.12 | 11.4 to 26.3 | +0.57 (RSS +1.27) | +0.56 | 1.57 | 16 pads, 7.81 to 15.92 (8.02 to 15.73 needed) | **PASS** |

Half-width = frequency span / 2 + half the pad set's largest gap + level reading (allocation +/-1.0 dB; no characterization at 17 mW yet) + drift over -10 to +45 C and supply (0.3 dB, est.: GVA-84+ 0.04 dB from its datasheet coefficient, passives under 0.05 dB, Si5351 edge and swing 0.2 dB).

Sensitivity to the level reading (as designed):

| Reading (+/- dB) | In-service drive (mW) | Overdrive margin (dB) | Margin above 10 mW (dB) | Verdict |
|---|---|---|---|---|
| 0.5 | 12.7 to 23.6 | +1.04 | +1.03 | **PASS** |
| 1.0 | 11.3 to 26.5 | +0.54 | +0.53 | **PASS** |
| 1.5 | 10.1 to 29.7 | +0.04 | +0.03 | **PASS** |
| 2.0 | 9.0 to 33.4 | -0.46 | -0.47 | **FAIL** |

The tinySA Ultra's published absolute accuracy is +/-2 dB after level calibration (tinysa.org/wiki/pmwiki.php?n=TinySA4.Specification, read 2026-09-28).

E24 1 % pi pads of the as-designed set (largest gap 0.77 dB, return loss at least 25 dB):

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

E24 1 % pi pads of the option d5 set (largest gap 0.75 dB): 7.81 dB (130, 56, 130); 8.50 dB (120, 62, 120); 9.23 dB (100, 62, 100); 9.66 dB (110, 75, 110); 10.07 dB (100, 75, 100); 10.56 dB (82, 68, 82); 11.01 dB (82, 75, 82); 11.44 dB (91, 91, 91); 11.97 dB (82, 91, 82); 12.47 dB (82, 100, 82); 12.99 dB (82, 110, 82); 13.48 dB (75, 110, 75); 14.06 dB (68, 110, 68); 14.57 dB (68, 120, 68); 15.32 dB (75, 150, 75); 15.92 dB (68, 150, 68).

## A5 overdrive margin against 30 mW

| Case | Margin (dB) |
|---|---|
| fixed pad, coax 5 cm | -0.00 |
| fixed pad, coax 10 cm | -0.29 |
| fixed pad, coax 15 cm | -0.73 |
| fixed pad, any length (d4) | -2.10 |
| option: 6 dB at the pin, fixed pad (d5) | -1.42 |
| select-on-test, as designed, reading +/-1.0 dB | +0.54 |
| select-on-test, option d5, reading +/-1.0 dB | +0.57 |
| select-on-test, tinySA Ultra alone (+/-2 dB) | -0.46 |

Fixed-pad rows carry a further 0.1 dB temperature allowance (estimate) not included above.

## A5 closure margin at 6.4 V (lowest corner, typical module, C2 and C3: feed at most 0.35 ohm at 25 C, VGG 3.3 V)

| Temperature case | PA case (C) | p1, LPF median (W; margin dB; with the terms) | p1, LPF worst (W; margin dB; with the terms) | p3, LPF median (W; margin dB; with the terms) | p3, LPF worst (W; margin dB; with the terms) | Datasheet-minimum module, p1, LPF median (dB) |
|---|---|---|---|---|---|---|
| 25 C, start of key-down (case 25 C) | 25.0 | 3.94; -0.04; -0.19 to +0.03 | 3.11; -1.06; -1.21 to -0.99 | 4.10; +0.14; -0.01 to +0.21 | 3.24; -0.88; -1.03 to -0.81 | -0.95 |
| 25 C, key-down, -0.005 dB/K | 58.7 | 3.66; -0.36; -0.51 to -0.29 | 2.83; -1.46; -1.61 to -1.39 | 3.81; -0.19; -0.34 to -0.12 | 2.95; -1.29; -1.44 to -1.22 | -1.23 |
| 25 C, key-down, -0.015 dB/K | 56.8 | 3.46; -0.60; -0.75 to -0.53 | 2.68; -1.71; -1.86 to -1.64 | 3.59; -0.44; -0.59 to -0.37 | 2.78; -1.54; -1.69 to -1.47 | -1.44 |
| -10 C, key-down, PA no cold gain | 23.4 | 3.68; -0.34; -0.49 to -0.27 | 2.89; -1.38; -1.53 to -1.31 | 3.82; -0.17; -0.32 to -0.10 | 3.01; -1.20; -1.35 to -1.13 | -1.19 |
| +45 C, key-down, -0.005 dB/K | 77.6 | 3.52; -0.53; -0.68 to -0.46 | 2.70; -1.67; -1.82 to -1.60 | 3.66; -0.36; -0.51 to -0.29 | 2.81; -1.50; -1.65 to -1.43 | -1.39 |
| +45 C, key-down, -0.015 dB/K | 74.9 | 3.22; -0.91; -1.06 to -0.84 | 2.47; -2.06; -2.21 to -1.99 | 3.35; -0.74; -0.89 to -0.67 | 2.57; -1.89; -2.04 to -1.82 | -1.75 |
| +45 C, case 100 C bound, -0.005 dB/K | 100.0 | 3.45; -0.61; -0.76 to -0.54 | 2.65; -1.76; -1.91 to -1.69 | 3.59; -0.44; -0.59 to -0.37 | 2.76; -1.58; -1.73 to -1.51 | -1.51 |
| +45 C, case 100 C bound, -0.015 dB/K | 100.0 | 3.00; -1.21; -1.36 to -1.14 | 2.31; -2.36; -2.51 to -2.29 | 3.14; -1.03; -1.18 to -0.96 | 2.41; -2.17; -2.32 to -2.10 | -2.14 |

Terms not carried as corners (added to the margin as a range):
- RA07M1317M curve graph read: -0.07 / +0.07 dB (+/-0.1 W reading error at about 6 W (estimate)).
- GVA-84+ in LM2940 dropout at 6.4 V (drive down, module near saturation): -0.05 / +0.00 dB (slope of the digitized RA07M1317M Pout-Pin curve at 7.2 V: about 0.08 dB per dB of drive from 7 to 10 dBm and 0.005 dB per dB above, for up to 0.5 dB less drive (estimate)).
- GVA-84+ gain at 146 MHz below its 0.1 GHz value (finding-8): -0.03 / +0.00 dB (Rev. F typical gain 24.1 dB at 0.1 GHz and 21.7 dB at 1.0 GHz: 0.1 to 0.4 dB less at 146 MHz, times the 0.08 dB/dB module slope (estimate)).

Plots: `pin_at_pa_vs_pack.png`, `pout_at_sma_vs_pack.png`, `a5_closure_margin.png`, `a5_overdrive_margin.png`, `a5_sot_reading_sensitivity.png`.
