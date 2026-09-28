# Run 2026-09-28-r4-mc-air-aligned: Monte Carlo, 24 AWG air coils aligned (+/-3 %), BOM values

Deck `lpf_r4.cir` (252 steps: run 1 all L and C at -tol, run 2 at +tol, runs 3 to 252 uniform random, seed 21003; every value in `mc_values.csv`). LTspice AC 2 to 1600 MHz in 2 MHz steps.

Log cross-checks (L4 value echoed by .meas equals the CSV for every step; .meas S21 at 288 MHz equals the .raw value within 0.001 dB for every step): **PASS**.

| Quantity | Worst | 1st pct | Median | Corner -tol | Corner +tol | Limit | Verdict |
|---|---|---|---|---|---|---|---|
| IL max 144-148 MHz (dB) | 0.99 | 0.83 | 0.59 | 0.42 | 0.65 | <= 0.5 | FAIL |
| Min atten. 288-296 MHz (dB) | 51.93 | 52.25 | 57.73 | 53.84 | 60.97 | >= 40 | PASS |
| Min atten. 432-444 MHz (dB) | 72.17 | 72.84 | 80.60 | 84.40 | 85.53 | >= 35 | PASS |
| Min atten. 576-1500 MHz (dB) | 65.98 | 67.16 | 77.41 | 77.43 | 76.84 | >= 40 | PASS |

Dissipative part of the loss (|S21|^2 / (1 - |S11|^2), max over 144 to 148 MHz): worst 0.79 dB, median 0.55 dB; the rest of the insertion loss is mismatch from detuning.

Input return loss over 144 to 148 MHz: worst 11.9 dB, median 21.0 dB (reported, no criterion).

Worst attenuation per harmonic band (dB): 2f 51.9, 3f 72.2, 4f 80.8, 5f 91.7, 6f 92.9, 7f 82.0, 8f 75.3, 9f 70.4, 10f 66.5

Yield (runs meeting all four criteria): 15.1 %.

Plots: `s21_mc_wide.png`, `il_mc_passband.png`, `mc_histograms.png`.
