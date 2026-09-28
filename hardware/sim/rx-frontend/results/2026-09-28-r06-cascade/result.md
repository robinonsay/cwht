# 2026-09-28-r06-cascade: result

Checker: cascade.py. MDS = -147.0 dBm + NF (500 Hz). REQ-SYS-022: MDS at most -140 dBm (TBR). REQ-SYS-033: image and half-IF responses at least 70 dB below the in-band response (TBR).

| configuration | BPF worst loss per section, nominal Q 120 (dB) | same, MC mode B p95 (dB) | NF nominal / filter corner / stack (dB) | MDS nominal / filter corner / stack (dBm) | REQ-SYS-022 (nominal and filter corner) | gain to mixer (dB) | image rej: Q 100 / Q 120 / MC B min / MC A min (dB) | REQ-SYS-033 image | half-IF equivalent at antenna, nominal / corner (dBm) | REQ-SYS-033 half-IF | isolation needed, antenna to mixer at the image (dB) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A5 as TS-012 rev 4 (BPF 2+3, IF 8) | 1.70, 3.76 | 2.31, 6.04 | 5.84 / 7.24 / 9.58 | -141.2 / -139.8 / -137.4 | PASS nominal, FAIL filter corner | 18.2 | 51.3 / 52.0 / 46.2 / 38.7 | FAIL | -174 / -181 | PASS | 88 |
| A5 + BPF3 (2+3+3, IF 8), proposed | 1.70, 3.76, 3.76 | 2.31, 6.04, 5.98 | 5.81 / 7.88 / 11.73 | -141.2 / -139.1 / -135.3 | PASS nominal, FAIL filter corner | 14.5 | 86.0 / 87.3 / 78.1 / 70.6 | PASS | -177 / -187 | PASS | 84 |
| A5 + BPF3 + 3 dB pad before the ring | 1.70, 3.76, 3.76 | 2.31, 6.04, 5.98 | 6.52 / 9.21 / 13.92 | -140.5 / -137.8 / -133.1 | PASS nominal, FAIL filter corner | 11.5 | 86.0 / 87.3 / 78.1 / 70.6 | PASS | -180 / -190 | PASS | 81 |
| A5, IF 10 MHz, BPF 2+3+2 (alternative) | 1.70, 3.76, 1.70 | 2.31, 6.04, 2.36 | 5.54 / 6.94 / 9.85 | -141.5 / -140.1 / -137.2 | PASS | 16.5 | 86.7 / 87.7 / 80.5 / 70.6 | PASS | -175 / -183 | PASS | 87 |
| A4 as TS-012 rev 4 (BPF 2+3, JFET mixer) | 1.70, 3.76 | 2.31, 6.04 | 5.71 / 7.06 / 9.15 | -141.3 / -139.9 / -137.9 | PASS nominal, FAIL filter corner | 18.2 | 51.3 / 52.0 / 46.2 / 38.7 | FAIL | -152 / -159 | PASS | 88 |
| A4 + BPF3 (2+3+3, JFET mixer) | 1.70, 3.76, 3.76 | 2.31, 6.04, 5.98 | 5.50 / 7.23 / 10.60 | -141.5 / -139.8 / -136.4 | PASS nominal, FAIL filter corner | 14.5 | 86.0 / 87.3 / 78.1 / 70.6 | PASS | -156 / -165 | PASS | 84 |

Ring: matched conversion gain -5.14 dB (LTspice, IF port into 50 ohm); worst half-IF IIP2 over the mismatched sets 51.8 dBm; relative time-step floor -77.8 dBc.
JFET mixer: worst valid half-IF IIP2 30.1 dBm.

Stage values (estimates unless marked sim):

- relay: G5V-2 pole, 1N5711 clamp pair and input trace: 0.3 dB nominal, 0.5 dB corner (estimate, Low: signal relay not rated at VHF)
- j310: MMBFJ310 grounded gate: gain 12 dB nominal / 10 dB corner, NF 2.5 / 3.0 dB (estimate from onsemi MMBFJ310 datasheet Gpg 16 dB typ at 100 MHz and NF 3.0 dB typ at 450 MHz, both at VDS 10 V, ID 10 mA; derated for the 5 V rail and tuned-drain loss)
- pad: 3 dB pad between BPF3 and the ring (proposed with the third section: fixes the filter termination against the ring's LO-varying RF port)
- ring: diode ring, 4 x 1N5711: conversion loss = LTspice r05 Gc (matched set) + 1.0 dB nominal / + 2.0 dB corner for BN-43-202 core and winding loss not modelled (estimate); SSB NF = loss
- jfet: single J310 mixer (A4): conversion gain +3 dB nominal / 0 dB corner, SSB NF 10 / 12 dB (estimate, Low: no A4 schematic or measurement exists; typical of a source-injected JFET mixer)
- diplexer: diplexer 0.5 dB (estimate)
- pma: 2N3904 post-mixer amplifier: gain 15 dB, NF 5 dB nominal / 6 dB corner (estimate)
- xtal: 6-pole 500 Hz ladder at 8.000 MHz: loss 10 dB nominal / 12 dB corner (estimate from docs/research/cw-selectivity-options.md F7: 10.7 dB for 6 poles at 9 MHz, Rs 15 ohm); at 10 MHz +1 dB (f0/B scaling, estimate)
- ifa: two 2N3904 IF stages: 20 dB each, NF 5 dB (estimate); product detector NF 15 dB (estimate)
- image_noise: two-section front ends: the second J310's own output noise in the image band reaches the mixer unfiltered, so its noise counts twice (term F_J2 / G_before_J2 added; conservative, input taken at 290 K)

Stage tables (nominal):

**A5 as TS-012 rev 4 (BPF 2+3, IF 8)**: relay, clamps NF 0.30 G -0.30; BPF1 NF 1.70 G -1.70; J310 #1 NF 2.50 G +12.00; BPF2 NF 3.76 G -3.76; J310 #2 NF 2.50 G +12.00; diode ring NF 6.14 G -6.14; diplexer NF 0.50 G -0.50; 2N3904 PMA NF 5.00 G +15.00; crystal ladder NF 10.00 G -10.00; IF amp 1 NF 5.00 G +20.00; IF amp 2 NF 5.00 G +20.00; product det. NF 15.00 G +0.00; image-noise term 0.51 dB

**A5 + BPF3 (2+3+3, IF 8), proposed**: relay, clamps NF 0.30 G -0.30; BPF1 NF 1.70 G -1.70; J310 #1 NF 2.50 G +12.00; BPF2 NF 3.76 G -3.76; J310 #2 NF 2.50 G +12.00; BPF3 NF 3.76 G -3.76; diode ring NF 6.14 G -6.14; diplexer NF 0.50 G -0.50; 2N3904 PMA NF 5.00 G +15.00; crystal ladder NF 10.00 G -10.00; IF amp 1 NF 5.00 G +20.00; IF amp 2 NF 5.00 G +20.00; product det. NF 15.00 G +0.00

**A5 + BPF3 + 3 dB pad before the ring**: relay, clamps NF 0.30 G -0.30; BPF1 NF 1.70 G -1.70; J310 #1 NF 2.50 G +12.00; BPF2 NF 3.76 G -3.76; J310 #2 NF 2.50 G +12.00; BPF3 NF 3.76 G -3.76; 3 dB pad NF 3.00 G -3.00; diode ring NF 6.14 G -6.14; diplexer NF 0.50 G -0.50; 2N3904 PMA NF 5.00 G +15.00; crystal ladder NF 10.00 G -10.00; IF amp 1 NF 5.00 G +20.00; IF amp 2 NF 5.00 G +20.00; product det. NF 15.00 G +0.00

**A5, IF 10 MHz, BPF 2+3+2 (alternative)**: relay, clamps NF 0.30 G -0.30; BPF1 NF 1.70 G -1.70; J310 #1 NF 2.50 G +12.00; BPF2 NF 3.76 G -3.76; J310 #2 NF 2.50 G +12.00; BPF3 NF 1.70 G -1.70; diode ring NF 6.14 G -6.14; diplexer NF 0.50 G -0.50; 2N3904 PMA NF 5.00 G +15.00; crystal ladder NF 11.00 G -11.00; IF amp 1 NF 5.00 G +20.00; IF amp 2 NF 5.00 G +20.00; product det. NF 15.00 G +0.00

**A4 as TS-012 rev 4 (BPF 2+3, JFET mixer)**: relay, clamps NF 0.30 G -0.30; BPF1 NF 1.70 G -1.70; J310 #1 NF 2.50 G +12.00; BPF2 NF 3.76 G -3.76; J310 #2 NF 2.50 G +12.00; JFET mixer NF 10.00 G +3.00; diplexer NF 0.50 G -0.50; 2N3904 PMA NF 5.00 G +15.00; crystal ladder NF 10.00 G -10.00; IF amp 1 NF 5.00 G +20.00; IF amp 2 NF 5.00 G +20.00; product det. NF 15.00 G +0.00; image-noise term 0.52 dB

**A4 + BPF3 (2+3+3, JFET mixer)**: relay, clamps NF 0.30 G -0.30; BPF1 NF 1.70 G -1.70; J310 #1 NF 2.50 G +12.00; BPF2 NF 3.76 G -3.76; J310 #2 NF 2.50 G +12.00; BPF3 NF 3.76 G -3.76; JFET mixer NF 10.00 G +3.00; diplexer NF 0.50 G -0.50; 2N3904 PMA NF 5.00 G +15.00; crystal ladder NF 10.00 G -10.00; IF amp 1 NF 5.00 G +20.00; IF amp 2 NF 5.00 G +20.00; product det. NF 15.00 G +0.00

![cascade_nf_gain.png](cascade_nf_gain.png)

![cascade_verdicts.png](cascade_verdicts.png)
