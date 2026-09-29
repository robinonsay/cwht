# 2026-09-28-r11-cascade-tpm005: result

Checker: cascade.py (revision 2). MDS = -147.0 dBm + NF (500 Hz). REQ-SYS-022: MDS at most -140 dBm (TBR); TC-SYS-017 acceptance: at most -140 dBm at every tolerance corner. TPM-005 (rx-mds, docs/plan/tpm.json): PDR margin policy -142 dBm or better (Green); Yellow from -142 to -137 dBm; Red worse than -137 dBm.
Filter losses: numpy nodal solver on the deck netlists (run r07: within 0.002 dB of LTspice). Every device value is an estimate (stage notes below).

| configuration | BPF worst loss per section: nominal Q 120 / J310 port / TC-SYS-017 corner (dB) | NF nominal / J310 port / corner / stack (dB) | MDS nominal / J310 port / corner / stack (dBm) | REQ-SYS-022 nominal / J310 / corner / stack | TPM-005 nominal / J310 / corner / stack | gain to mixer (dB) | image: corner mode B / + ports / + stray (dB) | half-IF at antenna, nominal / stack (dBm) |
|---|---|---|---|---|---|---|---|---|
| A5 as TS-012 rev 4 (BPF 2+3, IF 8) | 1.70, 3.76 / 2.33, 3.76 / 2.83, 6.72 | 5.84 / 6.47 / 8.05 / 10.52 | -141.2 / -140.5 / -139.0 / -136.5 | PASS / PASS / FAIL / FAIL | Yellow / Yellow / Yellow / Red | 18.2 | 45.0 / n/a / n/a | -174 / -182 |
| A5 + BPF3 (2+3+3, IF 8) | 1.70, 3.76, 3.76 / 2.33, 3.76, 3.76 / 2.83, 6.72, 6.72 | 5.81 / 6.44 / 9.04 / 13.29 | -141.2 / -140.6 / -138.0 / -133.7 | PASS / PASS / FAIL / FAIL | Yellow / Yellow / Yellow / Red | 14.5 | 75.6 / 72.1 / 70.2 | -177 / -189 |
| A5 + BPF3 of 4 (2+3+4, IF 8) | 1.70, 3.76, 6.19 / 2.33, 3.76, 6.19 / 2.83, 6.72, 11.95 | 6.35 / 6.98 / 12.06 / 17.57 | -140.7 / -140.0 / -134.9 / -129.4 | PASS / PASS / FAIL / FAIL | Yellow / Yellow / Red / Red | 12.1 | 91.4 / 87.8 / 80.1 | -180 / -194 |
| A5, IF 10 MHz, 2+3+2 (alternative) | 1.70, 3.76, 1.70 / 2.33, 3.76, 1.70 / 2.83, 6.72, 3.11 | 5.53 / 6.16 / 7.90 / 11.19 | -141.5 / -140.8 / -139.1 / -135.8 | PASS / PASS / FAIL / FAIL | Yellow / Yellow / Yellow / Red | 16.5 | 78.9 / 75.1 / 72.5 | -175 / -185 |
| A4 as TS-012 rev 4 (BPF 2+3, JFET mixer) | 1.70, 3.76 / 2.33, 3.76 / 2.83, 6.72 | 5.71 / 6.34 / 7.86 / 10.06 | -141.3 / -140.7 / -139.2 / -136.9 | PASS / PASS / FAIL / FAIL | Yellow / Yellow / Yellow / Red | 18.2 | 45.0 / n/a / n/a | -152 / -160 |
| A4 + BPF3 (2+3+3, JFET mixer) | 1.70, 3.76, 3.76 / 2.33, 3.76, 3.76 / 2.83, 6.72, 6.72 | 5.50 / 6.13 / 8.26 / 12.04 | -141.5 / -140.9 / -138.7 / -135.0 | PASS / PASS / FAIL / FAIL | Yellow / Yellow / Yellow / Red | 14.5 | 75.6 / 72.1 / 70.2 | -156 / -167 |
| A4 + BPF3 of 4 (2+3+4, JFET mixer) | 1.70, 3.76, 6.19 / 2.33, 3.76, 6.19 / 2.83, 6.72, 11.95 | 5.87 / 6.50 / 10.68 / 15.95 | -141.1 / -140.5 / -136.3 / -131.1 | PASS / PASS / FAIL / FAIL | Yellow / Yellow / Red / Red | 12.1 | 91.4 / 87.8 / 80.1 | -158 / -172 |

Ring: matched conversion gain -5.14 dB (LTspice r05); worst half-IF IIP2 51.8 dBm. JFET mixer: worst valid half-IF IIP2 30.1 dBm.

Stage values (estimates unless marked sim):

- relay: G5V-2 pole, 1N5711 clamp pair and input trace: 0.3 dB nominal, 0.5 dB corner (estimate, Low: signal relay not rated at VHF)
- j310: MMBFJ310 grounded gate: gain 12 dB nominal / 10 dB corner, NF 2.5 / 3.0 dB (estimate from onsemi MMBFJ310 datasheet Gpg 16 dB typ at 100 MHz and NF 3.0 dB typ at 450 MHz, both at VDS 10 V, ID 10 mA; derated for the 5 V rail and tuned-drain loss)
- ring: diode ring, 4 x 1N5711: conversion loss = LTspice r05 Gc (matched set) + 1.0 dB nominal / + 2.0 dB corner for BN-43-202 core and winding loss not modelled (estimate); SSB NF = loss
- jfet: single J310 mixer (A4): conversion gain +3 dB nominal / 0 dB corner, SSB NF 10 / 12 dB (estimate, Low: no A4 schematic or measurement exists; typical of a source-injected JFET mixer)
- diplexer: diplexer 0.5 dB (estimate)
- pma: 2N3904 post-mixer amplifier: gain 15 dB, NF 5 dB nominal / 6 dB corner (estimate)
- xtal: 6-pole 500 Hz ladder at 8.000 MHz: loss 10 dB nominal / 12 dB corner (estimate from docs/research/cw-selectivity-options.md F7: 10.7 dB for 6 poles at 9 MHz, Rs 15 ohm); at 10 MHz +1 dB (f0/B scaling, estimate)
- ifa: two 2N3904 IF stages: 20 dB each, NF 5 dB (estimate); product detector NF 15 dB (estimate)
- image_noise: two-section front ends: the second J310's own output noise in the image band reaches the mixer unfiltered, so its noise counts twice (term F_J2 / G_before_J2 added; conservative, input taken at 290 K)

Stage tables (nominal):

**A5 as TS-012 rev 4 (BPF 2+3, IF 8)**: relay, clamps NF 0.30 G -0.30; BPF1 NF 1.70 G -1.70; J310 #1 NF 2.50 G +12.00; BPF2 NF 3.76 G -3.76; J310 #2 NF 2.50 G +12.00; diode ring NF 6.14 G -6.14; diplexer NF 0.50 G -0.50; 2N3904 PMA NF 5.00 G +15.00; crystal ladder NF 10.00 G -10.00; IF amp 1 NF 5.00 G +20.00; IF amp 2 NF 5.00 G +20.00; product det. NF 15.00 G +0.00; image-noise term 0.51 dB

**A5 + BPF3 (2+3+3, IF 8)**: relay, clamps NF 0.30 G -0.30; BPF1 NF 1.70 G -1.70; J310 #1 NF 2.50 G +12.00; BPF2 NF 3.76 G -3.76; J310 #2 NF 2.50 G +12.00; BPF3 NF 3.76 G -3.76; diode ring NF 6.14 G -6.14; diplexer NF 0.50 G -0.50; 2N3904 PMA NF 5.00 G +15.00; crystal ladder NF 10.00 G -10.00; IF amp 1 NF 5.00 G +20.00; IF amp 2 NF 5.00 G +20.00; product det. NF 15.00 G +0.00

**A5 + BPF3 of 4 (2+3+4, IF 8)**: relay, clamps NF 0.30 G -0.30; BPF1 NF 1.70 G -1.70; J310 #1 NF 2.50 G +12.00; BPF2 NF 3.76 G -3.76; J310 #2 NF 2.50 G +12.00; BPF3 NF 6.19 G -6.19; diode ring NF 6.14 G -6.14; diplexer NF 0.50 G -0.50; 2N3904 PMA NF 5.00 G +15.00; crystal ladder NF 10.00 G -10.00; IF amp 1 NF 5.00 G +20.00; IF amp 2 NF 5.00 G +20.00; product det. NF 15.00 G +0.00

**A5, IF 10 MHz, 2+3+2 (alternative)**: relay, clamps NF 0.30 G -0.30; BPF1 NF 1.70 G -1.70; J310 #1 NF 2.50 G +12.00; BPF2 NF 3.76 G -3.76; J310 #2 NF 2.50 G +12.00; BPF3 NF 1.70 G -1.70; diode ring NF 6.14 G -6.14; diplexer NF 0.50 G -0.50; 2N3904 PMA NF 5.00 G +15.00; crystal ladder NF 11.00 G -11.00; IF amp 1 NF 5.00 G +20.00; IF amp 2 NF 5.00 G +20.00; product det. NF 15.00 G +0.00

**A4 as TS-012 rev 4 (BPF 2+3, JFET mixer)**: relay, clamps NF 0.30 G -0.30; BPF1 NF 1.70 G -1.70; J310 #1 NF 2.50 G +12.00; BPF2 NF 3.76 G -3.76; J310 #2 NF 2.50 G +12.00; JFET mixer NF 10.00 G +3.00; diplexer NF 0.50 G -0.50; 2N3904 PMA NF 5.00 G +15.00; crystal ladder NF 10.00 G -10.00; IF amp 1 NF 5.00 G +20.00; IF amp 2 NF 5.00 G +20.00; product det. NF 15.00 G +0.00; image-noise term 0.52 dB

**A4 + BPF3 (2+3+3, JFET mixer)**: relay, clamps NF 0.30 G -0.30; BPF1 NF 1.70 G -1.70; J310 #1 NF 2.50 G +12.00; BPF2 NF 3.76 G -3.76; J310 #2 NF 2.50 G +12.00; BPF3 NF 3.76 G -3.76; JFET mixer NF 10.00 G +3.00; diplexer NF 0.50 G -0.50; 2N3904 PMA NF 5.00 G +15.00; crystal ladder NF 10.00 G -10.00; IF amp 1 NF 5.00 G +20.00; IF amp 2 NF 5.00 G +20.00; product det. NF 15.00 G +0.00

**A4 + BPF3 of 4 (2+3+4, JFET mixer)**: relay, clamps NF 0.30 G -0.30; BPF1 NF 1.70 G -1.70; J310 #1 NF 2.50 G +12.00; BPF2 NF 3.76 G -3.76; J310 #2 NF 2.50 G +12.00; BPF3 NF 6.19 G -6.19; JFET mixer NF 10.00 G +3.00; diplexer NF 0.50 G -0.50; 2N3904 PMA NF 5.00 G +15.00; crystal ladder NF 10.00 G -10.00; IF amp 1 NF 5.00 G +20.00; IF amp 2 NF 5.00 G +20.00; product det. NF 15.00 G +0.00

Verdict REQ-SYS-022 at the TC-SYS-017 filter corner, proposed configurations: FAIL for A5-R1, A4-R1. No configuration meets the TPM-005 PDR margin policy (-142 dBm) in any case.

Checker exit status: 1.

![cascade_nf_gain.png](cascade_nf_gain.png)

![cascade_verdicts.png](cascade_verdicts.png)
