# Run 2026-09-28-r1-nominal: nominal S21 of the TS-012 harmonic LPF

Deck `lpf_r1.cir`, LTspice AC 0.5 to 1600 MHz in 0.5 MHz steps, 50 ohm source and load. S21 = V(out) with a 2 V AC source.

Known answer (ideal exact element values against the analytic 0.1 dB Chebyshev): max error 0.0005 dB where the analytic value is under 150 dB; **PASS** (criterion 0.05 dB).

| Variant | IL max 144-148 (dB) | RL min (dB) | 2f min (dB) | 3f min (dB) | 576-1500 MHz min (dB) | 7f (dB) | Verdict (40/35/40 dB, 0.5 dB) |
|---|---|---|---|---|---|---|---|
| ideal exact | 0.100 | 16.4 | 47.9 | 76.0 | 94.5 | 129.4 | PASS |
| ideal BOM values | 0.005 | 29.7 | 47.2 | 75.2 | 93.8 | 128.7 | PASS |
| Coilcraft 1812SMS + parasitics | 0.699 | 30.9 | 58.8 | 87.0 | 77.6 | 96.1 | FAIL: IL |
| 24 AWG air coils + parasitics | 0.491 | 31.0 | 57.4 | 84.9 | 77.1 | 95.0 | PASS |

Loss decomposition of the nominal 1812SMS build (max over 144 to 148 MHz): coil loss alone 0.420 dB, capacitor ESR alone 0.283 dB.

Plots: `s21_nominal_wide.png`, `il_nominal_passband.png`, `rl_nominal_passband.png`.
