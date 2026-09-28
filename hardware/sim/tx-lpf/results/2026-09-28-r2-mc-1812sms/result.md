# Run 2026-09-28-r2-mc-1812sms: Monte Carlo, Coilcraft 1812SMS (J, 5 %), BOM values

Deck `lpf_r2.cir` (252 steps: run 1 all L and C at -tol, run 2 at +tol, runs 3 to 252 uniform random, seed 21001; every value in `mc_values.csv`). LTspice AC 2 to 1600 MHz in 2 MHz steps.

Log cross-checks (L4 value echoed by .meas equals the CSV for every step; .meas S21 at 288 MHz equals the .raw value within 0.001 dB for every step): **PASS**.

| Quantity | Worst | 1st pct | Median | Corner -tol | Corner +tol | Limit | Verdict |
|---|---|---|---|---|---|---|---|
| IL max 144-148 MHz (dB) | 1.21 | 1.10 | 0.76 | 0.56 | 1.07 | <= 0.5 | FAIL |
| Min atten. 288-296 MHz (dB) | 54.40 | 54.71 | 58.67 | 54.40 | 63.09 | >= 40 | PASS |
| Min atten. 432-444 MHz (dB) | 75.39 | 76.17 | 83.02 | 86.57 | 87.74 | >= 35 | PASS |
| Min atten. 576-1500 MHz (dB) | 66.57 | 68.03 | 78.10 | 77.88 | 77.29 | >= 40 | PASS |

Dissipative part of the loss (|S21|^2 / (1 - |S11|^2), max over 144 to 148 MHz): worst 0.96 dB, median 0.71 dB; the rest of the insertion loss is mismatch from detuning.

Input return loss over 144 to 148 MHz: worst 11.4 dB, median 19.8 dB (reported, no criterion).

Worst attenuation per harmonic band (dB): 2f 54.4, 3f 75.4, 4f 83.9, 5f 92.7, 6f 93.5, 7f 82.9, 8f 76.1, 9f 71.1, 10f 67.1

Yield (runs meeting all four criteria): 0.0 %.

Plots: `s21_mc_wide.png`, `il_mc_passband.png`, `mc_histograms.png`.
