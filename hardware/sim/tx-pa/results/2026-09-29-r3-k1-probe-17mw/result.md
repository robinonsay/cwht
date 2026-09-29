# 2026-09-29-r3-k1-probe-17mw: the select-on-test level reading at about 17 mW (revision 3)

Diode probe across the 50 ohm load that replaces the module, read on the Fluke 174; forward drop measured at DC at the meter's own current and at 11 times it (1.00 Mohm across the meter). LTspice: RF periodic steady state (9360 steps) and DC forward drop; the checker solves the equilibrium hold voltage and applies the reading equations. All figures are estimates (surrogate diode model).

| Quantity | Range (dB, read minus true) |
|---|---|
| M0 (revision 2: Vpk = Vdc + Vf at DC), 25 C, no harmonic | -0.727 to -0.417 |
| M1 (with the conduction term), 25 C, no harmonic | -0.046 to +0.009 |
| M1, every case (harmonics, DC at +/-5 K) | -0.363 to +0.339 |
| M1, every case without the 2f cases | -0.336 to +0.323 |
| M2 (M1 in both polarities, averaged), every case | -0.336 to +0.323 |

Terms added in the worst direction: Fluke 174 0.066 dB; ideality from the two DC readings 0.195 dB; 1 % load 0.043 dB.

**Reading bound, method M2: +/-0.64 dB** (M1: +/-0.67 dB), against the +/-1.0 dB allocation of revision 2.

Plot `probe_reading_error.png`; every case in `result.json` (`rows`); decks `probe_rf.cir`, `probe_dc.cir`.
