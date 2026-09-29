# 2026-09-28-r1-d5-drive-a5-pinpad: A5 drive chain (WP-PDR-21 drive window), revision 1

**Design-request option, not the TS-012 revision 4 design:** a 6 dB pi pad (150.0, 36.0, 150.0) ohm (E24 1 %) on the main board at the CLK1 pin, before the coax, and a 12 dB pad (82.0, 91.0, 82.0) ohm on the RF board in place of the 18 dB pad (total 17.88 dB against 18.42 dB).

Interface (TS-012 section 8.1 layout): CLK1 on the main board, 50 ohm coax of 5, 10, 15 cm (VF 0.66, est.) to the drive LPF on the RF board. Lumped load on the CLK1 pin: tap 5 pF + stub 2 pF = 7 pF (estimates) against the Si5351 Table 7 maximum of 15 pF: **PASS**. All corners at 25 C; the drive moves by at most 0.1 dB over -10 to +45 C (estimate, see the analysis record).

Verdict, module input window 10 to 30 mW: **FAIL** at all 810 corners (617 in the window, 112 above 30 mW, 81 below 10 mW); on the TS-012 criterion corners only (source 25 and 50 ohm, gain 22.5 and 25.0 dB, 144 to 148 MHz, nominal Si5351 edge and VDDO, all P1dB sets, all coax lengths): **FAIL** (74 of 108).
Overdrive margin, fixed pad (highest corner against 30 mW): -1.42 dB; -1.52 dB with the 0.1 dB temperature allowance.

Verdict, 3f at the GVA-84+ input at least 25 dB below the fundamental: **PASS** (worst -35.4 dBc).
GVA-84+ input at most -5.9 dBm against the +13 dBm maximum rating: **PASS**. GVA-84+ output: nominal 14.5 dBm, highest 19.2 dBm.

| Quantity | Min | Nominal | Max |
|---|---|---|---|
| Power into the PA input (mW) | 6.7 | 14.2 | 41.6 |
| Power into the PA input (dBm) | 8.29 | 11.52 | 16.19 |
| CLK1 pin swing, peak to peak (V) | 1.59 | - | 2.54 |
| CLK1 pin load at f, equivalent shunt C (pF; informative) | 9.6 | - | 11.9 |
| CLK1 pin load at f, magnitude (ohm) | 42.9 | - | 52.0 |

| Coax (cm) | Min (mW) | Max (mW) | Criterion corners (mW) | Above 30 mW | Below 10 mW | Overdrive margin (dB) |
|---|---|---|---|---|---|---|
| 5 | 6.8 | 39.6 | 9.6 to 30.8 | 32 | 27 | -1.21 |
| 10 | 6.7 | 40.5 | 9.6 to 31.5 | 37 | 27 | -1.30 |
| 15 | 6.8 | 41.6 | 9.6 to 32.4 | 43 | 27 | -1.42 |

- Lowest corner: source 50 ohm, GVA gain 22.5 dB, P1dB set min, 148 MHz, Si5351 case low (VDDO 3.2 V, edge 1.5 ns, duty 0.45), coax 10.0 cm.
- Highest corner: source 25 ohm, GVA gain 25.3 dB, P1dB set high, 144 MHz, Si5351 case high (VDDO 3.4 V, edge 0.5 ns, duty 0.50), coax 15.0 cm.
- Nominal corner: source 50 ohm, GVA gain 24.1 dB, P1dB set typ, 146 MHz, Si5351 case nom (VDDO 3.3 V, edge 1.0 ns, duty 0.50), coax 10.0 cm.
- Pad insertion loss between 50 ohm terminations (E24 values): {'a5_in': 18.416, 'a5_out': 2.995, 'a4_in': 11.971, 'pin': 5.904, 'a5_in_rf': 11.971}.

- Spread of the drive over all corners 7.91 dB against a window of 4.77 dB (10 to 30 mW).

Plots: `drive_a5_corners.png` (power into the PA input per corner and coax length, with the limits), `drive_a5_h3.png` (3f at the GVA-84+ input), `drive_a5_pinload.png` (load on the CLK1 pin against Table 7). Per-corner numbers: `corners.json`. Deck `drive_a5.cir`; LTspice log and raw beside it.
