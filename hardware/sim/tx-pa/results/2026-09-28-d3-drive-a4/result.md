# 2026-09-28-d3-drive-a4: A4 drive chain (WP-PDR-21 drive window)

Verdict, AFT05 drive at or below the 0.2 W ruggedness-test level (informative, not a rating): **PASS** (0 corners above).

Verdict, 3f at the GVA-84+ input at least 25 dB below the fundamental: **PASS** (worst -34.5 dBc).
GVA-84+ input at most -1.1 dBm against the +13 dBm maximum rating: **PASS**.

| Quantity | Min | Nominal | Max |
|---|---|---|---|
| Power into the PA input (mW) | 50.3 | 95.8 | 167.9 |
| Power into the PA input (dBm) | 17.02 | 19.81 | 22.25 |
| CLK1 pin swing, peak to peak (V) | 2.22 | - | 3.24 |

- Lowest corner: source 50 ohm, GVA gain 22.5 dB, P1dB set min, 148 MHz, Si5351 case low (VDDO 3.2 V, edge 1.5 ns, duty 0.45).
- Highest corner: source 25 ohm, GVA gain 25.3 dB, P1dB set high, 144 MHz, Si5351 case high (VDDO 3.4 V, edge 0.5 ns, duty 0.50).
- Nominal corner: source 50 ohm, GVA gain 24.1 dB, P1dB set typ, 146 MHz, Si5351 case nom (VDDO 3.3 V, edge 1.0 ns, duty 0.50).
- Pad insertion loss between 50 ohm terminations (E24 values): {'a5_in': 18.416, 'a5_out': 2.995, 'a4_in': 11.971}.

Plots: `drive_a4_corners.png` (power into the PA input per corner with the window), `drive_a4_h3.png` (3f at the GVA-84+ input). Per-corner numbers: `corners.json`. Deck `drive_a4.cir`; LTspice log and raw beside it.
