# Run 2026-09-28-r8-wc-1812sms-bom: worst case and Monte Carlo, Coilcraft 1812SMS (J, 5 %), BOM values 22/68/39/82

Deck `lpf_r8.cir`, 259 steps: 1 and 2 every L and C at -tol and +tol (nominal parasitics); 3 to 252 uniform random over the parameter box (seed 21008, coil coupling signed); 253 to 259 the worst-case corners that `worst_case.py` found, one per metric. Every parameter of every step is in `mc_values.csv`. LTspice `.ac list` on the grid of `lpf_model.FREQS` (2 MHz to 1.6 GHz, the carriers 144 to 148 MHz in 0.25 MHz steps and every harmonic of each).

Checks: nodal model against LTspice at every step and frequency, max 8.63e-05 dB (criterion 0.01 dB) **PASS**; every corner's metric in LTspice equals the search value within 0.01 dB **PASS**; L4 echo **PASS**; .meas S21 at 288 MHz against the .raw **PASS**.

| Quantity (dB) | Worst case (corner search, LTspice) | Monte Carlo worst | MC 1st/99th pct | MC median | Rev. 1 corner -tol / +tol | Limit | Verdict (worst case) |
|---|---|---|---|---|---|---|---|
| IL max 144-148 MHz | 2.82 | 1.16 | 1.12 | 0.77 | 0.56 / 1.07 | <= 0.5 | FAIL |
| Min atten. 288-296 MHz | 45.08 | 52.46 | 52.88 | 57.79 | 54.40 / 63.09 | >= 40 | PASS |
| Min atten. 432-444 MHz | 70.14 | 74.30 | 75.95 | 85.57 | 86.57 / 87.74 | >= 35 | PASS |
| Min atten. 576-1500 MHz | 61.77 | 67.70 | 68.32 | 78.58 | 77.88 / 77.29 | >= 40 | PASS |
| Min A(2f) - IL(f) | 44.48 | 51.89 | 52.26 | 57.04 | 53.88 / 62.28 | - | - |
| Min A(3f) - IL(f) | 68.52 | 73.62 | 75.36 | 84.92 | 86.02 / 86.93 | - | - |
| Min A(nf) - IL(f), n 4 to 10 | 60.06 | 67.45 | 68.08 | 78.34 | 77.86 / 76.73 | - | - |

Revision 1's proposed 0.75 dB criterion at the worst case: **not met** (2.82 dB).

Dissipative part of the loss (|S21|^2 / (1 - |S11|^2)): MC median 0.72 dB, MC worst 1.04 dB, worst of every step 1.74 dB. Input return loss 144 to 148 MHz: MC median 20.0 dB, worst of every step 6.6 dB.

Worst A(nf) - IL(f) per harmonic, every step (dB): 2f 44.5, 3f 68.5, 4f 76.1, 5f 83.1, 6f 83.3, 7f 74.6, 8f 68.6, 9f 64.0, 10f 60.1

Monte Carlo yield (steps 1 to 252 meeting all four filter criteria): 0.0 %.

Worst-case corner of the 2f attenuation, ground-via inductance of each shunt capacitor (nH): C1 0.27, C3 0.27, C5 0.27, C7 0.27 (range 0.27 to 1.30 nH; the low end is two vias per capacitor on a 0.8 mm board).

Corner search per metric (value, the start it came from, parameters at a bound):

- IL max 144-148 MHz: 2.816 dB from 'nominal' (39 of 39 parameters at a bound; nominal 0.699 dB).
- Min atten. 288-296 MHz: 45.078 dB from 'nominal' (39 of 39 parameters at a bound; nominal 58.796 dB).
- Min atten. 432-444 MHz: 70.145 dB from 'nominal' (39 of 39 parameters at a bound; nominal 87.014 dB).
- Min atten. 576-1500 MHz: 61.768 dB from 'nominal' (39 of 39 parameters at a bound; nominal 77.568 dB).
- Min A(2f) - IL(f): 44.479 dB from 'nominal' (39 of 39 parameters at a bound; nominal 58.174 dB).
- Min A(3f) - IL(f): 68.518 dB from 'nominal' (39 of 39 parameters at a bound; nominal 86.393 dB).
- Min A(nf) - IL(f), n = 4 to 10: 60.063 dB from 'nominal' (39 of 39 parameters at a bound; nominal 77.397 dB).

Plots: `s21_wc_wide.png`, `harmonic_bands_wc.png`, `il_wc_passband.png`, `mc_wc_histograms.png`.
