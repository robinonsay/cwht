# 2026-09-28-d2-drive-a5: A5 drive chain (WP-PDR-21 drive window)

Verdict, module input window 10 to 30 mW: **FAIL** at all 270 corners (210 in the window, 0 above 30 mW, 60 below 10 mW); on the TS-012 criterion corners only (source 25 and 50 ohm, gain 22.5 and 25.0 dB, 144 to 148 MHz, nominal Si5351 edge and VDDO, all P1dB sets): **FAIL** (27 of 36).

Verdict, 3f at the GVA-84+ input at least 25 dB below the fundamental: **PASS** (worst -34.4 dBc).
GVA-84+ input at most -7.5 dBm against the +13 dBm maximum rating: **PASS**.

| Quantity | Min | Nominal | Max |
|---|---|---|---|
| Power into the PA input (mW) | 6.0 | 12.6 | 29.5 |
| Power into the PA input (dBm) | 7.76 | 11.01 | 14.70 |
| CLK1 pin swing, peak to peak (V) | 2.22 | - | 3.24 |

- Lowest corner: source 50 ohm, GVA gain 22.5 dB, P1dB set min, 148 MHz, Si5351 case low (VDDO 3.2 V, edge 1.5 ns, duty 0.45).
- Highest corner: source 25 ohm, GVA gain 25.3 dB, P1dB set high, 144 MHz, Si5351 case high (VDDO 3.4 V, edge 0.5 ns, duty 0.50).
- Nominal corner: source 50 ohm, GVA gain 24.1 dB, P1dB set typ, 146 MHz, Si5351 case nom (VDDO 3.3 V, edge 1.0 ns, duty 0.50).
- Pad insertion loss between 50 ohm terminations (E24 values): {'a5_in': 18.416, 'a5_out': 2.995, 'a4_in': 11.971}.

- Spread of the drive over all corners 6.94 dB against a window of 4.77 dB (10 to 30 mW).
- A fixed pad 0.00 dB larger would bring the maximum to 30 mW and the minimum to 6.0 mW.

Plots: `drive_a5_corners.png` (power into the PA input per corner with the window), `drive_a5_h3.png` (3f at the GVA-84+ input). Per-corner numbers: `corners.json`. Deck `drive_a5.cir`; LTspice log and raw beside it.
