# 2026-09-28-p1-power-a5: A5 output power at the SMA versus pack voltage (REQ-SYS-012)

Verdict, lowest corner at least 3.97 W at the SMA from 6.4 to 8.4 V (typical module): **FAIL** (lowest 3.71 W).
Nominal corner at least 5.0 W (the ALC set point is reachable) over the range: **FAIL**.
Datasheet-minimum module (6.5 W at 7.2 V), lowest corner at least 3.97 W: **FAIL** (3.03 W at 6.4 V; nominal corner with that module 3.90 W).

| At the pack voltage | Nominal (W) | Lowest corner (W) | Highest corner (W) |
|---|---|---|---|
| 6.4 V | 4.87 | 3.71 | 5.43 |
| 8.4 V | 8.14 | - | 8.99 |

- Drain voltage at 6.4 V: nominal 5.76 V, lowest 5.36 V (key-down sag).
- Module or device output at 8.4 V: nominal 9.13 W, highest corner 9.86 W (ALC open; the ALC must hold 5 W).
- Drive corners used (from 2026-09-28-d2-drive-a5): [7.757379277221447, 11.00793735315364, 14.701309905787326].
- Lowest corner at 6.4 V: {'irf': 0.45, 'ieta': 0.45, 'ipin': 7.757379277221447, 'ifr': 148000000.0, 'ivgg': 3.08, 'isp': 'typ', 'iloss': 0.6}.
- Nominal corner: {'irf': 0.35, 'ieta': 0.6, 'ipin': 11.00793735315364, 'ifr': 146000000.0, 'ivgg': 3.5, 'isp': 'typ', 'iloss': 0.5}.
- Lowest corner at 6.4 V with VGG at 3.5 V (no clamp limit): 4.03 W.
- Module output at the highest corner (open loop, VGG 3.5 V): above 8 W (stability guarantee) from 7.5 V; above 10 W (maximum rating) from nowhere below 8.4 V.
- Lowest corner at 6.4 V with the drain feed at most 0.35 ohm: 3.94 W; with that and VGG at 3.5 V: 4.31 W; datasheet-minimum module with both: 3.50 W.
- Lowest corner reaches 3.97 W from 6.65 V (typical module) and from 7.4 V (datasheet-minimum module).

Plot: `power_a5_sma.png`. Deck `power_a5.cir`; LTspice log and raw beside it; numbers in `result.json`.
