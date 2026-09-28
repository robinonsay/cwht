# 2026-09-28-p2-power-a4: A4 output power at the SMA versus pack voltage (REQ-SYS-012)

Verdict, lowest corner at least 3.97 W at the SMA from 6.4 to 8.4 V: **FAIL** (lowest 2.05 W).
Nominal corner at least 5.0 W (the ALC set point is reachable) over the range: **FAIL**.

| At the pack voltage | Nominal (W) | Lowest corner (W) | Highest corner (W) |
|---|---|---|---|
| 6.4 V | 3.54 | 2.05 | 4.49 |
| 8.4 V | 6.14 | - | 7.59 |

- Drain voltage at 6.4 V: nominal 5.96 V, lowest 5.65 V (key-down sag).
- Module or device output at 8.4 V: nominal 6.89 W, highest corner 8.32 W (ALC open; the ALC must hold 5 W).
- Drive corners used (from 2026-09-28-d3-drive-a4): [0.05030334650783131, 0.09582817710328338, 0.16787708538658472].
- Lowest corner at 6.4 V: {'irf': 0.45, 'ieta': 0.55, 'ipin': 0.05030334650783131, 'ifr': 144000000.0, 'in': 2.3, 'imatch': 0.5, 'iloss': 0.6}.
- Nominal corner: {'irf': 0.35, 'ieta': 0.67, 'ipin': 0.09582817710328338, 'ifr': 146000000.0, 'in': 2.0, 'imatch': 0.25, 'iloss': 0.5}.
- Lowest corner at 6.4 V with n = 2 and the reference-circuit match loss: 2.41 W.
- Lowest corner at 6.4 V with the drive at or above nominal: 2.84 W; lowest corner at 8.4 V: 3.76 W.
- Nominal corner reaches 3.97 W from 6.8 V and 5.0 W from 7.6 V.

Plot: `power_a4_sma.png`. Deck `power_a4.cir`; LTspice log and raw beside it; numbers in `result.json`.
