# 2026-09-28-d1-gva-model: GVA-84+ behavioural model check

Verdict: **PASS** (fitted 1 dB point within 0.1 dB and 3 dB point within 0.15 dB of the targets)

| P1dB set | P1dB target (dBm) | P1dB in LTspice | P3dB target | P3dB in LTspice | Pass |
|---|---|---|---|---|---|
| min | 19.4 | 19.37 | 20.7 | 20.69 | yes |
| typ | 20.4 | 20.37 | 21.7 | 21.69 | yes |
| high | 21.4 | 21.37 | 22.7 | 22.69 | yes |

Plot: `gva_compression.png`. Deck `gva_check.cir`; LTspice log `gva_check.log`, raw `gva_check.raw`.
