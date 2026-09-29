# Run 2026-09-28-r14-wc-1812sms-22-36-2pct: worst case and Monte Carlo, Coilcraft 1812SMS (G, 2 %) and C0G (G, 2 %), 22/68/36/82

Deck `lpf_r14.cir`, 259 steps: 1 and 2 every L and C at -tol and +tol (nominal parasitics); 3 to 252 uniform random over the parameter box (seed 21014, coil coupling signed); 253 to 259 the worst-case corners that `worst_case.py` found, one per metric. Every parameter of every step is in `mc_values.csv`. LTspice `.ac list` on the grid of `lpf_model.FREQS` (2 MHz to 1.6 GHz, the carriers 144 to 148 MHz in 0.25 MHz steps and every harmonic of each).

Checks: nodal model against LTspice at every step and frequency, max 9.33e-05 dB (criterion 0.01 dB) **PASS**; every corner's metric in LTspice equals the search value within 0.01 dB **PASS**; L4 echo **PASS**; .meas S21 at 288 MHz against the .raw **PASS**.

| Quantity (dB) | Worst case (corner search, LTspice) | Monte Carlo worst | MC 1st/99th pct | MC median | Rev. 1 corner -tol / +tol | Limit | Verdict (worst case) |
|---|---|---|---|---|---|---|---|
| IL max 144-148 MHz | 1.24 | 0.82 | 0.80 | 0.65 | 0.58 / 0.67 | <= 0.5 | FAIL |
| Min atten. 288-296 MHz | 45.56 | 50.98 | 51.40 | 55.36 | 54.62 / 58.02 | >= 40 | PASS |
| Min atten. 432-444 MHz | 71.08 | 74.79 | 76.91 | 85.52 | 87.88 / 88.18 | >= 35 | PASS |
| Min atten. 576-1500 MHz | 61.92 | 68.74 | 69.69 | 79.41 | 77.69 / 77.45 | >= 40 | PASS |
| Min A(2f) - IL(f) | 44.97 | 50.36 | 50.88 | 54.77 | 54.10 / 57.41 | - | - |
| Min A(3f) - IL(f) | 70.27 | 74.23 | 76.36 | 84.89 | 87.30 / 87.56 | - | - |
| Min A(nf) - IL(f), n 4 to 10 | 61.42 | 68.51 | 69.54 | 79.31 | 77.64 / 77.31 | - | - |

Revision 1's proposed 0.75 dB criterion at the worst case: **not met** (1.24 dB).

Dissipative part of the loss (|S21|^2 / (1 - |S11|^2)): MC median 0.60 dB, MC worst 0.76 dB, worst of every step 0.86 dB. Input return loss 144 to 148 MHz: MC median 19.9 dB, worst of every step 10.7 dB.

Worst A(nf) - IL(f) per harmonic, every step (dB): 2f 45.0, 3f 70.3, 4f 77.8, 5f 85.0, 6f 84.7, 7f 75.8, 8f 69.8, 9f 65.2, 10f 61.4

Monte Carlo yield (steps 1 to 252 meeting all four filter criteria): 0.4 %.

Worst-case corner of the 2f attenuation, ground-via inductance of each shunt capacitor (nH): C1 0.27, C3 0.27, C5 0.27, C7 0.27 (range 0.27 to 1.30 nH; the low end is two vias per capacitor on a 0.8 mm board).

Corner search per metric (value, the start it came from, parameters at a bound):

- IL max 144-148 MHz: 1.242 dB from 'random vertex 6' (39 of 39 parameters at a bound; nominal 0.623 dB).
- Min atten. 288-296 MHz: 45.562 dB from 'nominal' (39 of 39 parameters at a bound; nominal 56.336 dB).
- Min atten. 432-444 MHz: 71.081 dB from 'sensitivity vertex' (39 of 39 parameters at a bound; nominal 88.033 dB).
- Min atten. 576-1500 MHz: 61.921 dB from 'nominal' (39 of 39 parameters at a bound; nominal 77.568 dB).
- Min A(2f) - IL(f): 44.966 dB from 'nominal' (39 of 39 parameters at a bound; nominal 55.767 dB).
- Min A(3f) - IL(f): 70.267 dB from 'worst Monte Carlo step 70' (39 of 39 parameters at a bound; nominal 87.433 dB).
- Min A(nf) - IL(f), n = 4 to 10: 61.423 dB from 'nominal' (39 of 39 parameters at a bound; nominal 77.473 dB).

Plots: `s21_wc_wide.png`, `harmonic_bands_wc.png`, `il_wc_passband.png`, `mc_wc_histograms.png`.
