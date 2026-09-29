# 2026-09-29-r3-d6-drive-a5-bpf: A5 drive chain with the D-13 drive bandpass (revision 3)

8100 corners: 270 part corners (Si5351 25 and 50 ohm, 3 edge and VDDO cases, GVA-84+ gain 22.5 to 25.3 dB, 3 P1dB sets, 144, 146, 148 MHz) x coax 5, 10, 15 cm x 5 bandpass tolerance cases x coil Q 100 and 135; fixed 18 dB pad (18.42 dB); 25 C. All values estimates (graph reads and est. parasitics).

| Quantity | Min | Nominal | Max | Limit | Verdict |
|---|---|---|---|---|---|
| Power into the module (mW) | 5.5 | 12.5 | 39.1 | 10 to 30 | FAIL: 1356 under 10 mW, 565 over 30 mW |
| TS-012 criterion corners (mW) | 7.8 | - | 30.3 | 10 to 30 | - |
| 3f at the GVA-84+ input (dBc) | - | - | -33.8 | at most -25 | PASS |
| GVA-84+ input (dBm) | - | - | -6.2 | below +13 | PASS |
| GVA-84+ output (dBm) | - | - | 18.9 | P1dB min 19.4 | informative |
| CLK1 pin equivalent shunt C (pF) | -0.5 | - | 11.0 | at most 15 | PASS |
| CLK1 pin impedance magnitude (ohm) | 34 | - | 76 | - | informative |
| CLK1 swing at the tap (Vpp) | 1.33 | - | 3.40 | - | input to WP-PDR-20 |

Nominal part corner with the bandpass (nominal parts, Q 100): 12.5 mW, +0.38 dB against the revision 1 low-pass chain (d2, 11.4 mW).

Per bandpass case (810 part corners each):

| Case | Min (mW) | Max (mW) | Nominal part corner (mW) |
|---|---|---|---|
| nom, Q 100 | 6.1 | 36.3 | 12.5 |
| low, Q 100 | 5.7 | 36.7 | 12.4 |
| high, Q 100 | 5.6 | 36.2 | 12.5 |
| low, coupling high, Q 100 | 6.0 | 36.9 | 12.3 |
| high, coupling low, Q 100 | 5.5 | 35.4 | 12.4 |
| nom, Q 135 | 6.4 | 38.1 | 13.2 |
| low, Q 135 | 6.1 | 39.1 | 13.1 |
| high, Q 135 | 6.0 | 38.1 | 13.3 |
| low, coupling high, Q 135 | 6.3 | 38.6 | 13.0 |
| high, coupling low, Q 135 | 5.8 | 37.4 | 13.2 |

- Lowest corner: source 50 ohm, GVA gain 22.5 dB, P1dB set min, 148 MHz, Si5351 case low (VDDO 3.2 V, edge 1.5 ns, duty 0.45), coax 15.0 cm, bandpass high, coupling low, Q 100.
- Highest corner: source 25 ohm, GVA gain 25.3 dB, P1dB set high, 144 MHz, Si5351 case high (VDDO 3.4 V, edge 0.5 ns, duty 0.50), coax 5.0 cm, bandpass low, Q 135.

Plot `drive_a5_bpf_corners.png`; every corner in `corners.json`; deck `drive_a5_bpf.cir`.
