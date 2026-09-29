# s3 relay operate and release (electromechanical model)

Accepted parameter sets: std 13, h1 13 of 27 each.

| Option | supply | coil corner | nominal (ms) | band (ms) | sets with no pull-in |
|---|---|---|---|---|---|
| A | min | ref | 9.11 | 9.01 to 10.69 | 0 of 13 |
| A | min | nom | 12.59 | 11.80 to inf | 1 of 13 |
| A | min | hot_dl | inf | inf to inf | 13 of 13 |
| A | min | hot_c | inf | inf to inf | 13 of 13 |
| A | nom | ref | 7.95 | 7.92 to 8.42 | 0 of 13 |
| A | nom | nom | 9.99 | 9.56 to 13.46 | 0 of 13 |
| A | nom | hot_dl | 15.28 | 13.60 to inf | 2 of 13 |
| A | nom | hot_c | 24.69 | 20.02 to inf | 4 of 13 |
| A | max | ref | 7.14 | 7.13 to 7.19 | 0 of 13 |
| A | max | nom | 8.54 | 8.26 to 9.64 | 0 of 13 |
| A | max | hot_dl | 11.14 | 10.30 to 21.00 | 0 of 13 |
| A | max | hot_c | 13.05 | 11.74 to inf | 2 of 13 |
| B | min | ref | 7.77 | 7.75 to 8.13 | 0 of 13 |
| B | min | nom | 9.65 | 9.27 to 12.39 | 0 of 13 |
| B | min | hot_dl | 14.10 | 12.69 to inf | 2 of 13 |
| B | min | hot_c | 19.56 | 16.57 to inf | 3 of 13 |
| B | nom | ref | 7.01 | 7.01 to 7.01 | 0 of 13 |
| B | nom | nom | 8.33 | 8.07 to 9.22 | 0 of 13 |
| B | nom | hot_dl | 10.69 | 9.92 to 17.38 | 0 of 13 |
| B | nom | hot_c | 12.32 | 11.16 to inf | 1 of 13 |
| B | max | ref | 6.42 | 6.26 to 6.43 | 0 of 13 |
| B | max | nom | 7.42 | 7.23 to 7.77 | 0 of 13 |
| B | max | hot_dl | 8.99 | 8.47 to 10.85 | 0 of 13 |
| B | max | hot_c | 9.89 | 9.16 to 13.74 | 0 of 13 |
| C | min | ref | 5.20 | 4.87 to 5.23 | 0 of 13 |
| C | min | nom | 5.74 | 5.47 to 5.75 | 0 of 13 |
| C | min | hot_dl | 6.44 | 6.10 to 6.61 | 0 of 13 |
| C | min | hot_c | 6.77 | 6.40 to 7.11 | 0 of 13 |
| C | nom | ref | 4.30 | 3.94 to 4.32 | 0 of 13 |
| C | nom | nom | 4.62 | 4.27 to 4.64 | 0 of 13 |
| C | nom | hot_dl | 5.00 | 4.63 to 5.01 | 0 of 13 |
| C | nom | hot_c | 5.16 | 4.76 to 5.18 | 0 of 13 |
| C | max | ref | 3.75 | 3.39 to 3.78 | 0 of 13 |
| C | max | nom | 3.98 | 3.63 to 4.00 | 0 of 13 |
| C | max | hot_dl | 4.23 | 3.88 to 4.26 | 0 of 13 |
| C | max | hot_c | 4.34 | 3.96 to 4.36 | 0 of 13 |
| D | min | ref | 4.89 | 4.55 to 4.92 | 0 of 13 |
| D | min | nom | 5.35 | 5.03 to 5.36 | 0 of 13 |
| D | min | hot_dl | 5.91 | 5.56 to 5.94 | 0 of 13 |
| D | min | hot_c | 6.17 | 5.78 to 6.32 | 0 of 13 |
| D | nom | ref | 4.11 | 3.75 to 4.14 | 0 of 13 |
| D | nom | nom | 4.40 | 4.04 to 4.42 | 0 of 13 |
| D | nom | hot_dl | 4.73 | 4.37 to 4.75 | 0 of 13 |
| D | nom | hot_c | 4.87 | 4.48 to 4.89 | 0 of 13 |
| D | max | ref | 3.62 | 3.26 to 3.65 | 0 of 13 |
| D | max | nom | 3.83 | 3.49 to 3.85 | 0 of 13 |
| D | max | hot_dl | 4.06 | 3.71 to 4.09 | 0 of 13 |
| D | max | hot_c | 4.16 | 3.78 to 4.18 | 0 of 13 |

| Release case | hold (mA) | nominal (ms) | band max (ms) | hold / release current, min | hold / worst must-operate |
|---|---|---|---|---|---|
| A|full | 76.4 | 6.16 | 12.46 | 1.18 | 1.02 |
| A|hold63 | 48.1 | 4.83 | 8.93 | 0.74 | 0.64 |
| B|full | 76.4 | 6.16 | 12.46 | 1.18 | 1.02 |
| B|hold63 | 48.1 | 4.83 | 8.93 | 0.74 | 0.64 |
| C|full | 40.5 | 7.82 | 16.91 | 2.08 | 1.80 |
| C|hold5v | 24.1 | 6.32 | 12.92 | 1.24 | 1.07 |
| D|full | 40.5 | 7.82 | 16.91 | 2.08 | 1.80 |
| D|hold5v | 24.1 | 6.32 | 12.92 | 1.24 | 1.07 |

Checks: calibration_ref_7ms PASS, accepted_sets PASS, nominal_accepted PASS, model_vs_ltspice_rise PASS
