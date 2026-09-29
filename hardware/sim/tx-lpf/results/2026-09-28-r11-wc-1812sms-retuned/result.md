# Run 2026-09-28-r11-wc-1812sms-retuned: worst case and Monte Carlo, Coilcraft 1812SMS (J, 5 %), retuned 18/68/33/82

Deck `lpf_r11.cir`, 259 steps: 1 and 2 every L and C at -tol and +tol (nominal parasitics); 3 to 252 uniform random over the parameter box (seed 21011, coil coupling signed); 253 to 259 the worst-case corners that `worst_case.py` found, one per metric. Every parameter of every step is in `mc_values.csv`. LTspice `.ac list` on the grid of `lpf_model.FREQS` (2 MHz to 1.6 GHz, the carriers 144 to 148 MHz in 0.25 MHz steps and every harmonic of each).

Checks: nodal model against LTspice at every step and frequency, max 1.03e-04 dB (criterion 0.01 dB) **PASS**; every corner's metric in LTspice equals the search value within 0.01 dB **PASS**; L4 echo **PASS**; .meas S21 at 288 MHz against the .raw **PASS**.

| Quantity (dB) | Worst case (corner search, LTspice) | Monte Carlo worst | MC 1st/99th pct | MC median | Rev. 1 corner -tol / +tol | Limit | Verdict (worst case) |
|---|---|---|---|---|---|---|---|
| IL max 144-148 MHz | 1.39 | 0.68 | 0.67 | 0.53 | 0.42 / 0.58 | <= 0.5 | FAIL |
| Min atten. 288-296 MHz | 38.32 | 44.87 | 45.90 | 49.46 | 45.94 / 54.20 | >= 40 | FAIL |
| Min atten. 432-444 MHz | 64.85 | 71.20 | 72.68 | 81.38 | 85.00 / 84.72 | >= 35 | PASS |
| Min atten. 576-1500 MHz | 62.70 | 68.52 | 69.31 | 81.02 | 79.52 / 78.71 | >= 40 | PASS |
| Min A(2f) - IL(f) | 37.87 | 44.42 | 45.41 | 49.00 | 45.54 / 53.66 | - | - |
| Min A(3f) - IL(f) | 64.38 | 70.74 | 72.19 | 80.86 | 84.58 / 84.14 | - | - |
| Min A(nf) - IL(f), n 4 to 10 | 62.22 | 68.51 | 69.30 | 80.97 | 79.71 / 78.70 | - | - |

Revision 1's proposed 0.75 dB criterion at the worst case: **not met** (1.39 dB).

Dissipative part of the loss (|S21|^2 / (1 - |S11|^2)): MC median 0.49 dB, MC worst 0.62 dB, worst of every step 0.78 dB. Input return loss 144 to 148 MHz: MC median 22.1 dB, worst of every step 8.8 dB.

Worst A(nf) - IL(f) per harmonic, every step (dB): 2f 37.9, 3f 64.4, 4f 78.5, 5f 86.9, 6f 89.7, 7f 78.3, 8f 71.4, 9f 66.3, 10f 62.2

Monte Carlo yield (steps 1 to 252 meeting all four filter criteria): 33.7 %.

Worst-case corner of the 2f attenuation, ground-via inductance of each shunt capacitor (nH): C1 0.27, C3 0.27, C5 0.27, C7 0.27 (range 0.27 to 1.30 nH; the low end is two vias per capacitor on a 0.8 mm board).

Corner search per metric (value, the start it came from, parameters at a bound):

- IL max 144-148 MHz: 1.395 dB from 'worst Monte Carlo step 59' (39 of 39 parameters at a bound; nominal 0.496 dB).
- Min atten. 288-296 MHz: 38.323 dB from 'nominal' (39 of 39 parameters at a bound; nominal 50.158 dB).
- Min atten. 432-444 MHz: 64.848 dB from 'random vertex 2' (39 of 39 parameters at a bound; nominal 84.505 dB).
- Min atten. 576-1500 MHz: 62.695 dB from 'nominal' (39 of 39 parameters at a bound; nominal 79.088 dB).
- Min A(2f) - IL(f): 37.871 dB from 'nominal' (39 of 39 parameters at a bound; nominal 49.697 dB).
- Min A(3f) - IL(f): 64.379 dB from 'random vertex 2' (39 of 39 parameters at a bound; nominal 84.010 dB).
- Min A(nf) - IL(f), n = 4 to 10: 62.220 dB from 'worst Monte Carlo step 215' (39 of 39 parameters at a bound; nominal 79.182 dB).

Plots: `s21_wc_wide.png`, `harmonic_bands_wc.png`, `il_wc_passband.png`, `mc_wc_histograms.png`.
