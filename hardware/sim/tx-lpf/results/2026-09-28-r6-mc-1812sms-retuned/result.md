# Run 2026-09-28-r6-mc-1812sms-retuned: Monte Carlo, Coilcraft 1812SMS (J, 5 %), retuned 18/33 pF

Deck `lpf_r6.cir` (252 steps: run 1 all L and C at -tol, run 2 at +tol, runs 3 to 252 uniform random, seed 21006; every value in `mc_values.csv`). LTspice AC 2 to 1600 MHz in 2 MHz steps.

Log cross-checks (L4 value echoed by .meas equals the CSV for every step; .meas S21 at 288 MHz equals the .raw value within 0.001 dB for every step): **PASS**.

| Quantity | Worst | 1st pct | Median | Corner -tol | Corner +tol | Limit | Verdict |
|---|---|---|---|---|---|---|---|
| IL max 144-148 MHz (dB) | 0.71 | 0.67 | 0.52 | 0.42 | 0.58 | <= 0.5 | FAIL |
| Min atten. 288-296 MHz (dB) | 44.80 | 46.28 | 49.71 | 45.94 | 54.20 | >= 40 | PASS |
| Min atten. 432-444 MHz (dB) | 71.31 | 72.93 | 80.21 | 85.00 | 84.72 | >= 35 | PASS |
| Min atten. 576-1500 MHz (dB) | 68.99 | 69.73 | 79.64 | 79.52 | 78.71 | >= 40 | PASS |

Dissipative part of the loss (|S21|^2 / (1 - |S11|^2), max over 144 to 148 MHz): worst 0.63 dB, median 0.49 dB; the rest of the insertion loss is mismatch from detuning.

Input return loss over 144 to 148 MHz: worst 12.6 dB, median 21.5 dB (reported, no criterion).

Worst attenuation per harmonic band (dB): 2f 44.8, 3f 71.3, 4f 77.3, 5f 84.8, 6f 94.1, 7f 87.9, 8f 79.5, 9f 73.8, 10f 69.5

Yield (runs meeting all four criteria): 36.5 %.

Plots: `s21_mc_wide.png`, `il_mc_passband.png`, `mc_histograms.png`.

Value screen (`retune_screen.json`, ABCD model, stacked worst corner with every ESR at 0.4 ohm): BOM [22, 68, 39, 82, 39, 68, 22] gives 1.51 dB, the chosen set [18, 68, 33, 82, 33, 68, 18] gives 0.81 dB with 46.0 dB at 2f; best of 505 passing sets [24, 56, 36, 68, 36, 56, 24] gives 0.78 dB.
