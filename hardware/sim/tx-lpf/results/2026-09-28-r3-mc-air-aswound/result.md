# Run 2026-09-28-r3-mc-air-aswound: Monte Carlo, 24 AWG air coils as wound (+/-10 %), BOM values

Deck `lpf_r3.cir` (252 steps: run 1 all L and C at -tol, run 2 at +tol, runs 3 to 252 uniform random, seed 21002; every value in `mc_values.csv`). LTspice AC 2 to 1600 MHz in 2 MHz steps.

Log cross-checks (L4 value echoed by .meas equals the CSV for every step; .meas S21 at 288 MHz equals the .raw value within 0.001 dB for every step): **PASS**.

| Quantity | Worst | 1st pct | Median | Corner -tol | Corner +tol | Limit | Verdict |
|---|---|---|---|---|---|---|---|
| IL max 144-148 MHz (dB) | 1.30 | 1.19 | 0.68 | 0.37 | 1.06 | <= 0.5 | FAIL |
| Min atten. 288-296 MHz (dB) | 50.77 | 51.52 | 58.05 | 51.18 | 63.40 | >= 40 | PASS |
| Min atten. 432-444 MHz (dB) | 70.81 | 72.20 | 79.94 | 84.58 | 85.59 | >= 35 | PASS |
| Min atten. 576-1500 MHz (dB) | 65.81 | 67.76 | 78.11 | 77.35 | 76.90 | >= 40 | PASS |

Dissipative part of the loss (|S21|^2 / (1 - |S11|^2), max over 144 to 148 MHz): worst 0.87 dB, median 0.55 dB; the rest of the insertion loss is mismatch from detuning.

Input return loss over 144 to 148 MHz: worst 8.9 dB, median 16.0 dB (reported, no criterion).

Worst attenuation per harmonic band (dB): 2f 50.8, 3f 70.8, 4f 79.6, 5f 89.3, 6f 92.4, 7f 81.8, 8f 75.1, 9f 70.2, 10f 66.3

Yield (runs meeting all four criteria): 6.3 %.

Plots: `s21_mc_wide.png`, `il_mc_passband.png`, `mc_histograms.png`.
