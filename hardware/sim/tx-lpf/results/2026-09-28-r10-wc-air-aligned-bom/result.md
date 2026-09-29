# Run 2026-09-28-r10-wc-air-aligned-bom: worst case and Monte Carlo, 24 AWG air coils aligned (+/-3 %), BOM values

Deck `lpf_r10.cir`, 259 steps: 1 and 2 every L and C at -tol and +tol (nominal parasitics); 3 to 252 uniform random over the parameter box (seed 21010, coil coupling signed); 253 to 259 the worst-case corners that `worst_case.py` found, one per metric. Every parameter of every step is in `mc_values.csv`. LTspice `.ac list` on the grid of `lpf_model.FREQS` (2 MHz to 1.6 GHz, the carriers 144 to 148 MHz in 0.25 MHz steps and every harmonic of each).

Checks: nodal model against LTspice at every step and frequency, max 8.88e-05 dB (criterion 0.01 dB) **PASS**; every corner's metric in LTspice equals the search value within 0.01 dB **PASS**; L4 echo **PASS**; .meas S21 at 288 MHz against the .raw **PASS**.

| Quantity (dB) | Worst case (corner search, LTspice) | Monte Carlo worst | MC 1st/99th pct | MC median | Rev. 1 corner -tol / +tol | Limit | Verdict (worst case) |
|---|---|---|---|---|---|---|---|
| IL max 144-148 MHz | 3.38 | 1.08 | 1.03 | 0.67 | 0.42 / 0.65 | <= 0.5 | FAIL |
| Min atten. 288-296 MHz | 41.85 | 48.66 | 49.47 | 59.19 | 53.84 / 60.97 | >= 40 | PASS |
| Min atten. 432-444 MHz | 64.23 | 70.94 | 71.81 | 79.85 | 84.40 / 85.53 | >= 35 | PASS |
| Min atten. 576-1500 MHz | 59.59 | 67.15 | 67.55 | 78.23 | 77.43 / 76.84 | >= 40 | PASS |
| Min A(2f) - IL(f) | 41.34 | 48.28 | 49.02 | 58.60 | 53.46 / 60.44 | - | - |
| Min A(3f) - IL(f) | 63.57 | 70.37 | 71.16 | 79.30 | 84.00 / 85.00 | - | - |
| Min A(nf) - IL(f), n 4 to 10 | 57.64 | 66.74 | 67.25 | 78.11 | 77.53 / 76.68 | - | - |

Revision 1's proposed 0.75 dB criterion at the worst case: **not met** (3.38 dB).

Dissipative part of the loss (|S21|^2 / (1 - |S11|^2)): MC median 0.60 dB, MC worst 0.91 dB, worst of every step 1.81 dB. Input return loss 144 to 148 MHz: MC median 19.8 dB, worst of every step 5.2 dB.

Worst A(nf) - IL(f) per harmonic, every step (dB): 2f 41.3, 3f 63.6, 4f 72.2, 5f 80.1, 6f 81.5, 7f 72.8, 8f 66.8, 9f 62.0, 10f 57.6

Monte Carlo yield (steps 1 to 252 meeting all four filter criteria): 9.5 %.

Worst-case corner of the 2f attenuation, ground-via inductance of each shunt capacitor (nH): C1 0.27, C3 0.27, C5 0.27, C7 0.27 (range 0.27 to 1.30 nH; the low end is two vias per capacitor on a 0.8 mm board).

Corner search per metric (value, the start it came from, parameters at a bound):

- IL max 144-148 MHz: 3.377 dB from 'nominal' (39 of 39 parameters at a bound; nominal 0.491 dB).
- Min atten. 288-296 MHz: 41.849 dB from 'nominal' (39 of 39 parameters at a bound; nominal 57.431 dB).
- Min atten. 432-444 MHz: 64.234 dB from 'random vertex 2' (39 of 39 parameters at a bound; nominal 84.856 dB).
- Min atten. 576-1500 MHz: 59.587 dB from 'nominal' (39 of 39 parameters at a bound; nominal 77.114 dB).
- Min A(2f) - IL(f): 41.335 dB from 'nominal' (39 of 39 parameters at a bound; nominal 56.989 dB).
- Min A(3f) - IL(f): 63.575 dB from 'nominal' (39 of 39 parameters at a bound; nominal 84.415 dB).
- Min A(nf) - IL(f), n = 4 to 10: 57.644 dB from 'sensitivity vertex' (39 of 39 parameters at a bound; nominal 77.132 dB).

Plots: `s21_wc_wide.png`, `harmonic_bands_wc.png`, `il_wc_passband.png`, `mc_wc_histograms.png`.
