# Run 2026-09-28-r12-wc-air-aligned-retuned: worst case and Monte Carlo, 24 AWG air coils aligned (+/-3 %), retuned 18/68/33/82

Deck `lpf_r12.cir`, 259 steps: 1 and 2 every L and C at -tol and +tol (nominal parasitics); 3 to 252 uniform random over the parameter box (seed 21012, coil coupling signed); 253 to 259 the worst-case corners that `worst_case.py` found, one per metric. Every parameter of every step is in `mc_values.csv`. LTspice `.ac list` on the grid of `lpf_model.FREQS` (2 MHz to 1.6 GHz, the carriers 144 to 148 MHz in 0.25 MHz steps and every harmonic of each).

Checks: nodal model against LTspice at every step and frequency, max 1.45e-04 dB (criterion 0.01 dB) **PASS**; every corner's metric in LTspice equals the search value within 0.01 dB **PASS**; L4 echo **PASS**; .meas S21 at 288 MHz against the .raw **PASS**.

| Quantity (dB) | Worst case (corner search, LTspice) | Monte Carlo worst | MC 1st/99th pct | MC median | Rev. 1 corner -tol / +tol | Limit | Verdict (worst case) |
|---|---|---|---|---|---|---|---|
| IL max 144-148 MHz | 1.56 | 0.67 | 0.62 | 0.45 | 0.31 / 0.40 | <= 0.5 | FAIL |
| Min atten. 288-296 MHz | 35.63 | 41.85 | 43.29 | 49.56 | 45.49 / 52.19 | >= 40 | FAIL |
| Min atten. 432-444 MHz | 59.15 | 67.13 | 67.30 | 75.94 | 82.92 / 82.80 | >= 35 | PASS |
| Min atten. 576-1500 MHz | 60.58 | 66.52 | 69.58 | 80.60 | 79.07 / 78.25 | >= 40 | PASS |
| Min A(2f) - IL(f) | 35.25 | 41.58 | 42.97 | 49.14 | 45.21 / 51.82 | - | - |
| Min A(3f) - IL(f) | 58.75 | 66.85 | 66.93 | 75.56 | 82.61 / 82.40 | - | - |
| Min A(nf) - IL(f), n 4 to 10 | 60.34 | 66.55 | 69.74 | 80.61 | 79.35 / 78.40 | - | - |

Revision 1's proposed 0.75 dB criterion at the worst case: **not met** (1.56 dB).

Dissipative part of the loss (|S21|^2 / (1 - |S11|^2)): MC median 0.40 dB, MC worst 0.54 dB, worst of every step 0.78 dB. Input return loss 144 to 148 MHz: MC median 20.8 dB, worst of every step 7.4 dB.

Worst A(nf) - IL(f) per harmonic, every step (dB): 2f 35.2, 3f 58.7, 4f 72.0, 5f 82.2, 6f 88.8, 7f 77.4, 8f 70.4, 9f 65.0, 10f 60.3

Monte Carlo yield (steps 1 to 252 meeting all four filter criteria): 76.6 %.

Worst-case corner of the 2f attenuation, ground-via inductance of each shunt capacitor (nH): C1 0.27, C3 0.27, C5 0.27, C7 0.27 (range 0.27 to 1.30 nH; the low end is two vias per capacitor on a 0.8 mm board).

Corner search per metric (value, the start it came from, parameters at a bound):

- IL max 144-148 MHz: 1.563 dB from 'nominal' (39 of 39 parameters at a bound; nominal 0.355 dB).
- Min atten. 288-296 MHz: 35.626 dB from 'nominal' (39 of 39 parameters at a bound; nominal 48.899 dB).
- Min atten. 432-444 MHz: 59.147 dB from 'worst Monte Carlo step 170' (39 of 39 parameters at a bound; nominal 82.610 dB).
- Min atten. 576-1500 MHz: 60.576 dB from 'nominal' (39 of 39 parameters at a bound; nominal 78.632 dB).
- Min A(2f) - IL(f): 35.246 dB from 'nominal' (39 of 39 parameters at a bound; nominal 48.574 dB).
- Min A(3f) - IL(f): 58.747 dB from 'random vertex 2' (39 of 39 parameters at a bound; nominal 82.255 dB).
- Min A(nf) - IL(f), n = 4 to 10: 60.335 dB from 'sensitivity vertex' (39 of 39 parameters at a bound; nominal 78.847 dB).

Plots: `s21_wc_wide.png`, `harmonic_bands_wc.png`, `il_wc_passband.png`, `mc_wc_histograms.png`.
