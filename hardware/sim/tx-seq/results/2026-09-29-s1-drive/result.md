# s1 relay coil drive, DC operating points

Deck `drive_dc.cir`, LTspice exit 0, log first line `LTspice 26.0.2 for MacOS`.

| Driver | drop(i) fit at 70 C | residual |
|---|---|---|
| 2N3904 | 0.0146 V + 0.492 ohm x i | 6.8 mV |
| AO3400A | 0.0000 V + 0.031 ohm x i | 0.0 mV |

Checks: steps PASS, mos_ron_range_mohm PASS, q_vcesat_range_v PASS, fit_resid PASS
