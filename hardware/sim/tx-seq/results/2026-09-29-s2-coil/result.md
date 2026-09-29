# s2 relay coil transient

Deck `coil_tran.cir`, LTspice exit 0.

| Case | t to Ipu (ms) LTspice / closed form | hold mA LTspice / cf | ripple % | decay to 1/2 (ms) | decay to 5 % rated (ms) |
|---|---|---|---|---|---|
| A_rise_hot | 3.887 / 3.893 | nan / nan | nan | nan | nan |
| B_hold_hot | 11.665 / 11.680 | 39.63 / 39.55 | 2.27 | 1.44 | 3.37 |
| D_rise_hot | 1.280 / 1.280 | nan / nan | nan | nan | nan |
| D_hold_hot | 3.839 / 3.839 | 25.34 / 25.27 | 1.54 | 1.70 | 5.35 |
| D_rise_cold | 0.680 / 0.678 | nan / nan | nan | nan | nan |
| D_hold_cold | 2.037 / 2.035 | 41.06 / 40.90 | 1.36 | 2.39 | 7.96 |

Checks: steps PASS, closed_form PASS, ripple PASS
