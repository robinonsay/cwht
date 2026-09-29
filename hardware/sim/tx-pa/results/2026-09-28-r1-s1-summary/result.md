# 2026-09-28-r1-s1-summary: summary, select-on-test pad, overdrive and closure margins (revision 1)

## A5 select-on-test drive pad (estimate)

| Interface | Frequency span in a unit (dB) | Band half-width, worst-case sum (dB) | Same, RSS (dB) | In-service drive (mW) | Overdrive margin to 30 mW (dB) | Margin above 10 mW (dB) | Pad set needed (dB) | Verdict |
|---|---|---|---|---|---|---|---|---|
| as designed (coax, 18 dB pad on the RF board) | 0.34 | 1.97 | 1.17 | 11.0 to 27.2 | +0.42 (RSS +1.22) | +0.41 | 13 to 22 (13.5 to 21.5 needed) | **PASS** |
| option d5 (6 dB at the pin, 12 dB on the RF board) | 0.29 | 1.94 | 1.17 | 11.1 to 27.1 | +0.45 (RSS +1.22) | +0.44 | 8 to 16 (8.0 to 15.7 needed) | **PASS** |

Half-width = frequency span / 2 + pad step / 2 (0.5 dB) + level reading (1.0 dB, diode probe and Fluke 174, est.) + drift over -10 to +45 C and supply (0.3 dB, est.: GVA-84+ 0.04 dB from its datasheet coefficient, passives under 0.05 dB, Si5351 edge and swing 0.2 dB).

E24 1 % pi pads for the as-designed set (return loss at least 25 dB):

| Pad (dB) | Shunt, series, shunt (ohm) | Loss (dB) | Return loss (dB) |
|---|---|---|---|
| 13 | 82, 110, 82 | 12.99 | 34.8 |
| 14 | 75, 120, 75 | 13.98 | at least 60 |
| 15 | 68, 130, 68 | 15.04 | 32.2 |
| 16 | 68, 150, 68 | 15.92 | 42.6 |
| 17 | 62, 160, 62 | 16.94 | 29.1 |
| 18 | 68, 200, 68 | 17.79 | 32.5 |
| 19 | 68, 240, 68 | 19.05 | 27.8 |
| 20 | 68, 270, 68 | 19.88 | 25.8 |
| 21 | 56, 270, 56 | 21.26 | 30.5 |
| 22 | 62, 330, 62 | 21.99 | 31.2 |

## A5 overdrive margin against 30 mW

| Case | Margin (dB) |
|---|---|
| fixed pad, coax 5 cm | -0.00 |
| fixed pad, coax 10 cm | -0.29 |
| fixed pad, coax 15 cm | -0.73 |
| fixed pad, any length (d4) | -2.10 |
| option: 6 dB at the pin, fixed pad (d5) | -1.42 |
| select-on-test pad, as designed | +0.42 |
| select-on-test pad, option d5 | +0.45 |

Fixed-pad rows carry a further 0.1 dB temperature allowance (estimate) not included above.

## A5 closure margin at 6.4 V (lowest corner, typical module, C2 and C3 levers)

| Temperature case | p1 (W) | p1 margin (dB) | p1 range with the unmodelled terms (dB) | p3 (W) | p3 margin (dB) | p3 range (dB) | Datasheet-minimum module, p1 margin (dB) |
|---|---|---|---|---|---|---|---|
| 25 C | 4.28 | +0.32 | -0.01 to +0.39 | 4.45 | +0.49 | +0.16 to +0.56 | -0.58 |
| -10 C, PA +0 dB | 4.10 | +0.14 | -0.19 to +0.21 | 4.27 | +0.31 | -0.02 to +0.38 | -0.73 |
| +45 C, case 80 C, -0.005 dB/K | 3.81 | -0.18 | -0.51 to -0.11 | 3.96 | -0.02 | -0.35 to +0.05 | -1.06 |
| +45 C, case 80 C, -0.015 dB/K | 3.45 | -0.62 | -0.95 to -0.55 | 3.59 | -0.44 | -0.77 to -0.37 | -1.52 |
| +45 C, case 100 C, -0.005 dB/K | 3.74 | -0.26 | -0.59 to -0.19 | 3.89 | -0.09 | -0.42 to -0.02 | -1.15 |
| +45 C, case 100 C, -0.015 dB/K | 3.26 | -0.86 | -1.19 to -0.79 | 3.40 | -0.68 | -1.01 to -0.61 | -1.78 |

Terms not carried as corners (added to the margin as a range):
- output LPF loss above the 0.4 to 0.6 dB allocation: -0.21 / +0.00 dB (WP-PDR-21 LPF runs r6 and r7: worst passband loss 0.71 and 0.65 dB, plus the 0.1 dB relay: up to 0.81 dB against the 0.6 dB top corner here (hardware/sim/tx-lpf README)).
- RA07M1317M curve graph read: -0.07 / +0.07 dB (+/-0.1 W reading error at about 6 W (estimate)).
- GVA-84+ in LM2940 dropout at 6.4 V (drive down, module near saturation): -0.05 / +0.00 dB (slope of the digitized RA07M1317M Pout-Pin curve at 7.2 V: about 0.08 dB per dB of drive from 7 to 10 dBm and 0.005 dB per dB above, for up to 0.5 dB less drive (estimate)).

Plots: `pin_at_pa_vs_pack.png`, `pout_at_sma_vs_pack.png`, `a5_closure_margin.png`, `a5_overdrive_margin.png`.
