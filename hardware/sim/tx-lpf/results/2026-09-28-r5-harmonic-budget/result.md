# Run 2026-09-28-r5-harmonic-budget: harmonic budget per finalist

Spur at the antenna = carrier at the step +1 dB + PA harmonic ratio - worst Monte Carlo LPF attenuation in the harmonic band (runs r2 to r4). Limit: 47 CFR 97.307(e) for 25 W or less: at most 25 uW, at least 40 dB below the carrier, need not be below 10 uW; 25 uW binds at every step (0.5 to 6.3 W). Target: REQ-SYS-018 60 dBc at the 5 W step. Ramp: every instantaneous level 1 mW to 6.3 W.

| Finalist | Filter build | 97.307(e) all steps | Min margin (dB) | Ramp min margin (dB) | 60 dBc at 5 W | Min margin (dB) |
|---|---|---|---|---|---|---|
| A5 | Coilcraft 1812SMS (J, 5 %), BOM values | PASS | 21.4 | 18.4 | PASS | 19.4 |
| A5 | 24 AWG air coils as wound (+/-10 %), BOM values | PASS | 17.7 | 14.8 | PASS | 15.8 |
| A5 | 24 AWG air coils aligned (+/-3 %), BOM values | PASS | 18.9 | 16.0 | PASS | 16.9 |
| A5 | Coilcraft 1812SMS (J, 5 %), retuned 18/33 pF | PASS | 11.8 | 8.8 | PASS | 9.8 |
| A5 | 24 AWG air coils aligned (+/-3 %), retuned 18/33 pF | PASS | 10.8 | 7.8 | PASS | 8.8 |
| A4 | Coilcraft 1812SMS (J, 5 %), BOM values | PASS | 15.4 | 15.4 | PASS | 9.4 |
| A4 | 24 AWG air coils as wound (+/-10 %), BOM values | PASS | 11.8 | 11.8 | PASS | 5.8 |
| A4 | 24 AWG air coils aligned (+/-3 %), BOM values | PASS | 12.9 | 12.9 | PASS | 6.9 |
| A4 | Coilcraft 1812SMS (J, 5 %), retuned 18/33 pF | PASS | 5.8 | 5.8 | FAIL | -0.2 |
| A4 | 24 AWG air coils aligned (+/-3 %), retuned 18/33 pF | PASS | 4.8 | 4.8 | FAIL | -1.2 |

PA harmonic inputs (at the PA output): A5 2f -25 dBc, 3f and above -30 dBc at the 5 W step (RA07M1317M datasheet maxima at 6 W; 4f and above estimated equal to 3f); at 0.5, 1 and 2 W 2f -17 dBc and 3f and above -25 dBc (estimates). A4 2f -15 dBc, 3f and above -20 dBc at every step (estimate; no vendor data).

Plot: `harmonic_budget.png`.
