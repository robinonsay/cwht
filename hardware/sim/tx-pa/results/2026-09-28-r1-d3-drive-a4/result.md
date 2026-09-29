# 2026-09-28-r1-d3-drive-a4: A4 drive chain (WP-PDR-21 drive window), revision 1

Interface (TS-012 section 8.1 layout): CLK1 on the main board, 50 ohm coax of 5, 10, 15 cm (VF 0.66, est.) to the drive LPF on the RF board. Lumped load on the CLK1 pin: tap 5 pF + stub 2 pF = 7 pF (estimates) against the Si5351 Table 7 maximum of 15 pF: **PASS**. All corners at 25 C; the drive moves by at most 0.1 dB over -10 to +45 C (estimate, see the analysis record).

Verdict, AFT05 drive at or below the 0.2 W ruggedness-test level (informative, not a rating): **PASS** (0 corners above; margin +0.46 dB, +0.36 dB with the temperature allowance).

Verdict, 3f at the GVA-84+ input at least 25 dB below the fundamental: **PASS** (worst -30.9 dBc).
GVA-84+ input at most -0.2 dBm against the +13 dBm maximum rating: **PASS**. GVA-84+ output: nominal 19.5 dBm, highest 22.6 dBm.

| Quantity | Min | Nominal | Max |
|---|---|---|---|
| Power into the PA input (mW) | 45.8 | 89.4 | 180.0 |
| Power into the PA input (dBm) | 16.61 | 19.51 | 22.55 |
| CLK1 pin swing, peak to peak (V) | 1.66 | - | 3.66 |
| CLK1 pin load at f, equivalent shunt C (pF; informative) | 13.6 | - | 24.6 |
| CLK1 pin load at f, magnitude (ohm) | 36.3 | - | 64.6 |

| Coax (cm) | Min (mW) | Max (mW) | Criterion corners (mW) | Above 0.2 W | Overdrive margin (dB) |
|---|---|---|---|---|---|
| 5 | 46.8 | 170.5 | 63.3 to 151.3 | 0 | +0.69 |
| 10 | 45.8 | 174.7 | 62.3 to 156.4 | 0 | +0.59 |
| 15 | 46.0 | 180.0 | 62.5 to 163.4 | 0 | +0.46 |

- Lowest corner: source 50 ohm, GVA gain 22.5 dB, P1dB set min, 148 MHz, Si5351 case low (VDDO 3.2 V, edge 1.5 ns, duty 0.45), coax 10.0 cm.
- Highest corner: source 25 ohm, GVA gain 25.3 dB, P1dB set high, 144 MHz, Si5351 case high (VDDO 3.4 V, edge 0.5 ns, duty 0.50), coax 15.0 cm.
- Nominal corner: source 50 ohm, GVA gain 24.1 dB, P1dB set typ, 146 MHz, Si5351 case nom (VDDO 3.3 V, edge 1.0 ns, duty 0.50), coax 10.0 cm.
- Pad insertion loss between 50 ohm terminations (E24 values): {'a5_in': 18.416, 'a5_out': 2.995, 'a4_in': 11.971, 'pin': 5.904, 'a5_in_rf': 11.971}.

Plots: `drive_a4_corners.png` (power into the PA input per corner and coax length, with the limits), `drive_a4_h3.png` (3f at the GVA-84+ input), `drive_a4_pinload.png` (load on the CLK1 pin against Table 7). Per-corner numbers: `corners.json`. Deck `drive_a4.cir`; LTspice log and raw beside it.
