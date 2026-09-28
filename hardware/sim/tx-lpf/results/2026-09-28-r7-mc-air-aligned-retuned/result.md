# Run 2026-09-28-r7-mc-air-aligned-retuned: Monte Carlo, 24 AWG air coils aligned (+/-3 %), retuned 18/33 pF

Deck `lpf_r7.cir` (252 steps: run 1 all L and C at -tol, run 2 at +tol, runs 3 to 252 uniform random, seed 21007; every value in `mc_values.csv`). LTspice AC 2 to 1600 MHz in 2 MHz steps.

Log cross-checks (L4 value echoed by .meas equals the CSV for every step; .meas S21 at 288 MHz equals the .raw value within 0.001 dB for every step): **PASS**.

| Quantity | Worst | 1st pct | Median | Corner -tol | Corner +tol | Limit | Verdict |
|---|---|---|---|---|---|---|---|
| IL max 144-148 MHz (dB) | 0.65 | 0.56 | 0.42 | 0.31 | 0.40 | <= 0.5 | FAIL |
| Min atten. 288-296 MHz (dB) | 43.79 | 44.89 | 49.49 | 45.49 | 52.19 | >= 40 | PASS |
| Min atten. 432-444 MHz (dB) | 67.97 | 68.31 | 76.32 | 82.92 | 82.80 | >= 35 | PASS |
| Min atten. 576-1500 MHz (dB) | 67.47 | 69.62 | 78.24 | 79.07 | 78.25 | >= 40 | PASS |

Dissipative part of the loss (|S21|^2 / (1 - |S11|^2), max over 144 to 148 MHz): worst 0.52 dB, median 0.38 dB; the rest of the insertion loss is mismatch from detuning.

Input return loss over 144 to 148 MHz: worst 13.2 dB, median 21.6 dB (reported, no criterion).

Worst attenuation per harmonic band (dB): 2f 43.8, 3f 68.0, 4f 74.7, 5f 82.9, 6f 92.2, 7f 86.1, 8f 77.8, 9f 72.2, 10f 68.0

Yield (runs meeting all four criteria): 89.3 %.

Plots: `s21_mc_wide.png`, `il_mc_passband.png`, `mc_histograms.png`.

Value screen (`retune_screen.json`, ABCD model, stacked worst corner with every ESR at 0.4 ohm): BOM [22, 68, 39, 82, 39, 68, 22] gives 1.14 dB, the chosen set [18, 68, 33, 82, 33, 68, 18] gives 0.62 dB with 46.7 dB at 2f; best of 18763 passing sets [18, 68, 30, 90, 30, 68, 18] gives 0.55 dB.
