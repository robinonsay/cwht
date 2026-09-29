# Run 2026-09-28-r9-wc-air-aswound-bom: worst case and Monte Carlo, 24 AWG air coils as wound (+/-10 %), BOM values

Deck `lpf_r9.cir`, 259 steps: 1 and 2 every L and C at -tol and +tol (nominal parasitics); 3 to 252 uniform random over the parameter box (seed 21009, coil coupling signed); 253 to 259 the worst-case corners that `worst_case.py` found, one per metric. Every parameter of every step is in `mc_values.csv`. LTspice `.ac list` on the grid of `lpf_model.FREQS` (2 MHz to 1.6 GHz, the carriers 144 to 148 MHz in 0.25 MHz steps and every harmonic of each).

Checks: nodal model against LTspice at every step and frequency, max 1.74e-04 dB (criterion 0.01 dB) **PASS**; every corner's metric in LTspice equals the search value within 0.01 dB **PASS**; L4 echo **PASS**; .meas S21 at 288 MHz against the .raw **PASS**.

| Quantity (dB) | Worst case (corner search, LTspice) | Monte Carlo worst | MC 1st/99th pct | MC median | Rev. 1 corner -tol / +tol | Limit | Verdict (worst case) |
|---|---|---|---|---|---|---|---|
| IL max 144-148 MHz | 5.34 | 1.86 | 1.42 | 0.73 | 0.37 / 1.06 | <= 0.5 | FAIL |
| Min atten. 288-296 MHz | 39.74 | 47.63 | 48.80 | 58.22 | 51.18 / 63.40 | >= 40 | FAIL |
| Min atten. 432-444 MHz | 63.05 | 69.95 | 70.66 | 79.17 | 84.58 / 85.59 | >= 35 | PASS |
| Min atten. 576-1500 MHz | 59.27 | 67.19 | 69.21 | 78.87 | 77.35 / 76.90 | >= 40 | PASS |
| Min A(2f) - IL(f) | 39.27 | 47.29 | 48.15 | 57.67 | 50.83 / 62.72 | - | - |
| Min A(3f) - IL(f) | 62.45 | 69.25 | 69.91 | 78.53 | 84.21 / 84.92 | - | - |
| Min A(nf) - IL(f), n 4 to 10 | 55.81 | 67.04 | 68.55 | 78.62 | 77.49 / 76.34 | - | - |

Revision 1's proposed 0.75 dB criterion at the worst case: **not met** (5.34 dB).

Dissipative part of the loss (|S21|^2 / (1 - |S11|^2)): MC median 0.59 dB, MC worst 0.98 dB, worst of every step 2.47 dB. Input return loss 144 to 148 MHz: MC median 14.9 dB, worst of every step 3.2 dB.

Worst A(nf) - IL(f) per harmonic, every step (dB): 2f 39.3, 3f 62.4, 4f 71.2, 5f 79.1, 6f 79.6, 7f 70.9, 8f 64.9, 9f 60.1, 10f 55.8

Monte Carlo yield (steps 1 to 252 meeting all four filter criteria): 6.0 %.

Worst-case corner of the 2f attenuation, ground-via inductance of each shunt capacitor (nH): C1 0.27, C3 0.27, C5 0.27, C7 0.27 (range 0.27 to 1.30 nH; the low end is two vias per capacitor on a 0.8 mm board).

Corner search per metric (value, the start it came from, parameters at a bound):

- IL max 144-148 MHz: 5.340 dB from 'nominal' (39 of 39 parameters at a bound; nominal 0.491 dB).
- Min atten. 288-296 MHz: 39.745 dB from 'nominal' (39 of 39 parameters at a bound; nominal 57.431 dB).
- Min atten. 432-444 MHz: 63.050 dB from 'random vertex 2' (39 of 39 parameters at a bound; nominal 84.856 dB).
- Min atten. 576-1500 MHz: 59.273 dB from 'nominal' (39 of 39 parameters at a bound; nominal 77.114 dB).
- Min A(2f) - IL(f): 39.274 dB from 'nominal' (39 of 39 parameters at a bound; nominal 56.989 dB).
- Min A(3f) - IL(f): 62.447 dB from 'nominal' (39 of 39 parameters at a bound; nominal 84.415 dB).
- Min A(nf) - IL(f), n = 4 to 10: 55.807 dB from 'nominal' (39 of 39 parameters at a bound; nominal 77.132 dB).

Plots: `s21_wc_wide.png`, `harmonic_bands_wc.png`, `il_wc_passband.png`, `mc_wc_histograms.png`.
