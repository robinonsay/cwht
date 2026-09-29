# Run 2026-09-28-r16-wc-1812sms-trap-screen: worst case and Monte Carlo, Screened and rejected: 1812SMS (J), 10/47/20/68 with 5.6 pF traps across L2 and L6

Deck `lpf_r16.cir`, 259 steps: 1 and 2 every L and C at -tol and +tol (nominal parasitics); 3 to 252 uniform random over the parameter box (seed 21016, coil coupling signed); 253 to 259 the worst-case corners that `worst_case.py` found, one per metric. Every parameter of every step is in `mc_values.csv`. LTspice `.ac list` on the grid of `lpf_model.FREQS` (2 MHz to 1.6 GHz, the carriers 144 to 148 MHz in 0.25 MHz steps and every harmonic of each).

Checks: nodal model against LTspice at every step and frequency, max 1.43e-03 dB (criterion 0.01 dB) **PASS**; every corner's metric in LTspice equals the search value within 0.01 dB **PASS**; L4 echo **PASS**; .meas S21 at 288 MHz against the .raw **PASS**.

| Quantity (dB) | Worst case (corner search, LTspice) | Monte Carlo worst | MC 1st/99th pct | MC median | Rev. 1 corner -tol / +tol | Limit | Verdict (worst case) |
|---|---|---|---|---|---|---|---|
| IL max 144-148 MHz | 0.67 | 0.34 | 0.33 | 0.27 | 0.27 / 0.34 | <= 0.5 | FAIL |
| Min atten. 288-296 MHz | 39.99 | 48.91 | 50.09 | 57.87 | 51.92 / 63.33 | >= 40 | FAIL |
| Min atten. 432-444 MHz | 47.84 | 54.17 | 55.17 | 59.43 | 62.35 / 62.70 | >= 35 | PASS |
| Min atten. 576-1500 MHz | 9.89 | 36.58 | 41.13 | 62.33 | 56.35 / 53.73 | >= 40 | FAIL |
| Min A(2f) - IL(f) | 39.70 | 48.67 | 49.85 | 57.61 | 51.65 / 63.03 | - | - |
| Min A(3f) - IL(f) | 47.52 | 53.94 | 54.93 | 59.16 | 62.08 / 62.40 | - | - |
| Min A(nf) - IL(f), n 4 to 10 | 10.17 | 43.25 | 44.52 | 64.66 | 69.63 / 53.79 | - | - |

Revision 1's proposed 0.75 dB criterion at the worst case: **met** (0.67 dB).

Dissipative part of the loss (|S21|^2 / (1 - |S11|^2)): MC median 0.26 dB, MC worst 0.31 dB, worst of every step 0.39 dB. Input return loss 144 to 148 MHz: MC median 23.4 dB, worst of every step 12.1 dB.

Worst A(nf) - IL(f) per harmonic, every step (dB): 2f 39.7, 3f 47.5, 4f 53.3, 5f 59.8, 6f 60.6, 7f 40.2, 8f 10.2, 9f 31.1, 10f 41.6

Monte Carlo yield (steps 1 to 252 meeting all four filter criteria): 99.2 %.

Worst-case corner of the 2f attenuation, ground-via inductance of each shunt capacitor (nH): C1 0.27, C3 0.27, C5 0.27, C7 0.27 (range 0.27 to 1.30 nH; the low end is two vias per capacitor on a 0.8 mm board).

Corner search per metric (value, the start it came from, parameters at a bound):

- IL max 144-148 MHz: 0.669 dB from 'nominal' (45 of 45 parameters at a bound; nominal 0.271 dB).
- Min atten. 288-296 MHz: 39.988 dB from 'worst Monte Carlo step 246' (45 of 45 parameters at a bound; nominal 64.578 dB).
- Min atten. 432-444 MHz: 47.845 dB from 'nominal' (45 of 45 parameters at a bound; nominal 62.330 dB).
- Min atten. 576-1500 MHz: 9.895 dB from 'sensitivity vertex' (43 of 45 parameters at a bound; nominal 54.801 dB).
- Min A(2f) - IL(f): 39.700 dB from 'worst Monte Carlo step 246' (45 of 45 parameters at a bound; nominal 64.307 dB).
- Min A(3f) - IL(f): 47.522 dB from 'nominal' (45 of 45 parameters at a bound; nominal 62.064 dB).
- Min A(nf) - IL(f), n = 4 to 10: 10.166 dB from 'random vertex 1' (38 of 45 parameters at a bound; nominal 69.230 dB).

Plots: `s21_wc_wide.png`, `harmonic_bands_wc.png`, `il_wc_passband.png`, `mc_wc_histograms.png`.
