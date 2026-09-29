# Run 2026-09-28-r13-wc-1812sms-bom-2pct: worst case and Monte Carlo, Coilcraft 1812SMS (G, 2 %) and C0G (G, 2 %), BOM values 22/68/39/82

Deck `lpf_r13.cir`, 259 steps: 1 and 2 every L and C at -tol and +tol (nominal parasitics); 3 to 252 uniform random over the parameter box (seed 21013, coil coupling signed); 253 to 259 the worst-case corners that `worst_case.py` found, one per metric. Every parameter of every step is in `mc_values.csv`. LTspice `.ac list` on the grid of `lpf_model.FREQS` (2 MHz to 1.6 GHz, the carriers 144 to 148 MHz in 0.25 MHz steps and every harmonic of each).

Checks: nodal model against LTspice at every step and frequency, max 1.05e-04 dB (criterion 0.01 dB) **PASS**; every corner's metric in LTspice equals the search value within 0.01 dB **PASS**; L4 echo **PASS**; .meas S21 at 288 MHz against the .raw **PASS**.

| Quantity (dB) | Worst case (corner search, LTspice) | Monte Carlo worst | MC 1st/99th pct | MC median | Rev. 1 corner -tol / +tol | Limit | Verdict (worst case) |
|---|---|---|---|---|---|---|---|
| IL max 144-148 MHz | 1.76 | 1.00 | 0.93 | 0.74 | 0.63 / 0.80 | <= 0.5 | FAIL |
| Min atten. 288-296 MHz | 47.15 | 52.40 | 53.28 | 57.59 | 57.05 / 60.52 | >= 40 | PASS |
| Min atten. 432-444 MHz | 71.00 | 73.75 | 76.15 | 86.32 | 86.81 / 87.27 | >= 35 | PASS |
| Min atten. 576-1500 MHz | 61.92 | 66.16 | 69.23 | 80.21 | 77.69 / 77.45 | >= 40 | PASS |
| Min A(2f) - IL(f) | 46.48 | 51.84 | 52.53 | 56.89 | 56.48 / 59.84 | - | - |
| Min A(3f) - IL(f) | 69.89 | 72.91 | 75.53 | 85.61 | 86.23 / 86.60 | - | - |
| Min A(nf) - IL(f), n 4 to 10 | 60.94 | 65.84 | 68.99 | 80.07 | 77.59 / 77.18 | - | - |

Revision 1's proposed 0.75 dB criterion at the worst case: **not met** (1.76 dB).

Dissipative part of the loss (|S21|^2 / (1 - |S11|^2)): MC median 0.72 dB, MC worst 0.96 dB, worst of every step 1.37 dB. Input return loss 144 to 148 MHz: MC median 24.3 dB, worst of every step 10.2 dB.

Worst A(nf) - IL(f) per harmonic, every step (dB): 2f 46.5, 3f 69.9, 4f 77.7, 5f 84.9, 6f 84.7, 7f 75.7, 8f 69.6, 9f 64.9, 10f 60.9

Monte Carlo yield (steps 1 to 252 meeting all four filter criteria): 0.0 %.

Worst-case corner of the 2f attenuation, ground-via inductance of each shunt capacitor (nH): C1 0.27, C3 0.27, C5 0.27, C7 0.27 (range 0.27 to 1.30 nH; the low end is two vias per capacitor on a 0.8 mm board).

Corner search per metric (value, the start it came from, parameters at a bound):

- IL max 144-148 MHz: 1.759 dB from 'nominal' (39 of 39 parameters at a bound; nominal 0.699 dB).
- Min atten. 288-296 MHz: 47.147 dB from 'nominal' (39 of 39 parameters at a bound; nominal 58.796 dB).
- Min atten. 432-444 MHz: 71.004 dB from 'nominal' (39 of 39 parameters at a bound; nominal 87.014 dB).
- Min atten. 576-1500 MHz: 61.917 dB from 'nominal' (39 of 39 parameters at a bound; nominal 77.568 dB).
- Min A(2f) - IL(f): 46.484 dB from 'nominal' (39 of 39 parameters at a bound; nominal 58.174 dB).
- Min A(3f) - IL(f): 69.893 dB from 'nominal' (39 of 39 parameters at a bound; nominal 86.393 dB).
- Min A(nf) - IL(f), n = 4 to 10: 60.944 dB from 'nominal' (39 of 39 parameters at a bound; nominal 77.397 dB).

Plots: `s21_wc_wide.png`, `harmonic_bands_wc.png`, `il_wc_passband.png`, `mc_wc_histograms.png`.
