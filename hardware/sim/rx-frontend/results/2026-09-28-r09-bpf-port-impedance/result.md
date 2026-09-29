# 2026-09-28-r09-bpf-port-impedance: result

Checker: worst_case.py check r09. Question (review finding 2): what do the MMBFJ310 port impedances do to the image rejection and to the BPF1 loss, and what port tolerance must the J310 stages meet?
J310 values: onsemi (Fairchild) MMBFJ309/MMBFJ310 datasheet Rev. 1.5, https://www.onsemi.com/pdf/datasheet/mmbfj310-d.pdf, read 2026-09-28: gfs 8 to 18 mS (1 kHz), Re(yig) 12 mS typ (common gate, 100 MHz, VDS 10 V, ID 10 mA), Csg 4.1 typ / 5.0 max pF and Cdg 2.0 typ / 2.5 max pF (VGS -10 V). Grounded-gate input resistance taken as 1/gfs = 56 to 125 ohm, 83 ohm typical; the drain port impedance is undefined in TS-012 (50 to 200 ohm assumed, estimate).
Alignment: at50 = every resonator aligned on the NanoVNA with the section between 50 ohm ports, then placed in circuit; incircuit = aligned with the J310 ports connected. Coil Q 100, mode B tolerances for the corners.

## 2 + 3 + 3, IF 8 MHz (revision 1 proposal)

J310 port cases (worst image rejection over the band, dB):

| BPF1 and BPF2 load (J310 input) | BPF2 and BPF3 source (J310 drain) | nominal, aligned at 50 | mode B corner, aligned at 50 | mode B corner, aligned in circuit |
|---|---|---|---|---|
| 50 ohm | drain port 50 ohm | 86.0 | 75.6 | 75.6 |
| 50 ohm | drain port 100 ohm | 82.7 | 73.0 | 71.0 |
| 50 ohm | drain port 200 ohm | 80.9 | 72.0 | 67.6 |
| 50 ohm | 200 ohm || 2.5 pF (Cdg max) | 84.1 | 74.9 | 70.8 |
| J310 input 56 ohm (gfs 18 mS max) | drain port 50 ohm | 85.5 | 75.2 | 74.9 |
| J310 input 56 ohm (gfs 18 mS max) | drain port 100 ohm | 82.1 | 72.4 | 70.2 |
| J310 input 56 ohm (gfs 18 mS max) | drain port 200 ohm | 80.2 | 71.3 | 66.8 |
| J310 input 56 ohm (gfs 18 mS max) | 200 ohm || 2.5 pF (Cdg max) | 83.4 | 74.3 | 70.0 |
| J310 input 83 ohm (Re yig 12 mS typ) | drain port 50 ohm | 83.7 | 73.7 | 72.2 |
| J310 input 83 ohm (Re yig 12 mS typ) | drain port 100 ohm | 80.1 | 70.7 | 67.4 |
| J310 input 83 ohm (Re yig 12 mS typ) | drain port 200 ohm | 78.0 | 69.4 | 64.0 |
| J310 input 83 ohm (Re yig 12 mS typ) | 200 ohm || 2.5 pF (Cdg max) | 81.2 | 72.4 | 67.2 |
| J310 input 125 ohm (gfs 8 mS min) | drain port 50 ohm | 82.3 | 72.7 | 69.7 |
| J310 input 125 ohm (gfs 8 mS min) | drain port 100 ohm | 78.4 | 69.5 | 64.8 |
| J310 input 125 ohm (gfs 8 mS min) | drain port 200 ohm | 76.2 | 68.0 | 61.3 |
| J310 input 125 ohm (gfs 8 mS min) | 200 ohm || 2.5 pF (Cdg max) | 79.4 | 70.9 | 64.7 |
| 56 ohm || 5 pF (Csg max) | drain port 50 ohm | 87.2 | 76.9 | 75.6 |
| 56 ohm || 5 pF (Csg max) | drain port 100 ohm | 83.8 | 74.2 | 71.0 |
| 56 ohm || 5 pF (Csg max) | drain port 200 ohm | 81.9 | 73.1 | 67.6 |
| 56 ohm || 5 pF (Csg max) | 200 ohm || 2.5 pF (Cdg max) | 85.2 | 76.2 | 70.8 |
| 125 ohm || 5 pF | drain port 50 ohm | 86.4 | 76.7 | 73.3 |
| 125 ohm || 5 pF | drain port 100 ohm | 82.6 | 73.6 | 68.5 |
| 125 ohm || 5 pF | drain port 200 ohm | 80.4 | 72.0 | 65.1 |
| 125 ohm || 5 pF | 200 ohm || 2.5 pF (Cdg max) | 83.7 | 75.1 | 68.3 |

Every internal port anywhere on a VSWR circle around 50 ohm (8 phases; BPF1's antenna port stays 50 ohm), worst-case corner (dB):

| VSWR | nominal | mode B, aligned at 50 | mode B, aligned in circuit | mode A, aligned at 50 |
|---|---|---|---|---|
| 1 | 86.0 | 75.6 | 75.6 | 70.1 |
| 1.1 | 84.2 | 73.8 | 74.1 | 68.2 |
| 1.2 | 82.3 | 72.1 | 72.6 | 66.3 |
| 1.35 | 79.7 | 69.6 | 70.5 | 63.6 |
| 1.5 | 77.3 | 67.2 | 68.6 | 61.1 |
| 1.75 | 73.5 | 63.6 | 65.9 | 57.3 |
| 2 | 70.1 | 60.3 | 63.6 | 53.9 |

BPF1 worst in-band transducer loss with the J310 input as its load (dB): 50 ohm: 1.70 (Q 120), 1.96 (Q 100); J310 input 56 ohm (gfs 18 mS max): 1.68 (Q 120), 1.93 (Q 100); J310 input 83 ohm (Re yig 12 mS typ): 1.83 (Q 120), 2.06 (Q 100); J310 input 125 ohm (gfs 8 mS min): 2.33 (Q 120), 2.54 (Q 100); 56 ohm || 5 pF (Csg max): 1.81 (Q 120), 2.09 (Q 100); 125 ohm || 5 pF: 2.53 (Q 120), 2.80 (Q 100).

LTspice re-simulation of the named cases:

| case | numpy (dB) | LTspice (dB) | agree |
|---|---|---|---|
| nominal, load 50 ohm, drain port 50 ohm | 86.04 | 86.04 | yes |
| mode B corner, load 50 ohm, drain port 50 ohm | 75.63 | 75.63 | yes |
| nominal, load 50 ohm, drain port 200 ohm | 80.91 | 80.91 | yes |
| mode B corner, load 50 ohm, drain port 200 ohm | 71.95 | 71.95 | yes |
| nominal, load J310 input 83 ohm (Re yig 12 mS typ), drain port 200 ohm | 78.01 | 78.01 | yes |
| mode B corner, load J310 input 83 ohm (Re yig 12 mS typ), drain port 200 ohm | 69.41 | 69.41 | yes |
| nominal, load J310 input 125 ohm (gfs 8 mS min), drain port 50 ohm | 82.26 | 82.26 | yes |
| mode B corner, load J310 input 125 ohm (gfs 8 mS min), drain port 50 ohm | 72.70 | 72.70 | yes |
| nominal, load J310 input 125 ohm (gfs 8 mS min), drain port 200 ohm | 76.22 | 76.22 | yes |
| mode B corner, load J310 input 125 ohm (gfs 8 mS min), drain port 200 ohm | 67.96 | 67.96 | yes |
| nominal, load 125 ohm || 5 pF, drain port 200 ohm | 80.39 | 80.39 | yes |
| mode B corner, load 125 ohm || 5 pF, drain port 200 ohm | 72.02 | 72.02 | yes |
| mode B corner, every internal port on VSWR 1.2 | 72.07 | 72.07 | yes |
| mode B corner, every internal port on VSWR 1.5 | 67.23 | 67.23 | yes |

With the proposed design input (every internal port within VSWR 1.2 of 50 ohm, aligned at 50 ohm, mode B): worst-case corner 72.1 dB, **PASS** (before leakage, r10).

## 2 + 3 + 4, IF 8 MHz (margin lever, new here)

J310 port cases (worst image rejection over the band, dB):

| BPF1 and BPF2 load (J310 input) | BPF2 and BPF3 source (J310 drain) | nominal, aligned at 50 | mode B corner, aligned at 50 | mode B corner, aligned in circuit |
|---|---|---|---|---|
| 50 ohm | drain port 50 ohm | 103.9 | 91.4 | 91.4 |
| 50 ohm | drain port 100 ohm | 100.4 | 88.6 | 86.6 |
| 50 ohm | drain port 200 ohm | 98.4 | 87.3 | 83.1 |
| 50 ohm | 200 ohm || 2.5 pF (Cdg max) | 101.7 | 90.5 | 86.4 |
| J310 input 56 ohm (gfs 18 mS max) | drain port 50 ohm | 103.3 | 90.9 | 90.7 |
| J310 input 56 ohm (gfs 18 mS max) | drain port 100 ohm | 99.8 | 88.0 | 85.8 |
| J310 input 56 ohm (gfs 18 mS max) | drain port 200 ohm | 97.7 | 86.7 | 82.3 |
| J310 input 56 ohm (gfs 18 mS max) | 200 ohm || 2.5 pF (Cdg max) | 101.0 | 89.9 | 85.6 |
| J310 input 83 ohm (Re yig 12 mS typ) | drain port 50 ohm | 101.5 | 89.5 | 88.0 |
| J310 input 83 ohm (Re yig 12 mS typ) | drain port 100 ohm | 97.7 | 86.3 | 83.0 |
| J310 input 83 ohm (Re yig 12 mS typ) | drain port 200 ohm | 95.5 | 84.8 | 79.4 |
| J310 input 83 ohm (Re yig 12 mS typ) | 200 ohm || 2.5 pF (Cdg max) | 98.8 | 88.0 | 82.8 |
| J310 input 125 ohm (gfs 8 mS min) | drain port 50 ohm | 100.1 | 88.5 | 85.5 |
| J310 input 125 ohm (gfs 8 mS min) | drain port 100 ohm | 96.1 | 85.1 | 80.4 |
| J310 input 125 ohm (gfs 8 mS min) | drain port 200 ohm | 93.7 | 83.4 | 76.8 |
| J310 input 125 ohm (gfs 8 mS min) | 200 ohm || 2.5 pF (Cdg max) | 96.9 | 86.5 | 80.3 |
| 56 ohm || 5 pF (Csg max) | drain port 50 ohm | 105.0 | 92.7 | 91.4 |
| 56 ohm || 5 pF (Csg max) | drain port 100 ohm | 101.5 | 89.8 | 86.6 |
| 56 ohm || 5 pF (Csg max) | drain port 200 ohm | 99.4 | 88.5 | 83.1 |
| 56 ohm || 5 pF (Csg max) | 200 ohm || 2.5 pF (Cdg max) | 102.7 | 91.7 | 86.4 |
| 125 ohm || 5 pF | drain port 50 ohm | 104.3 | 92.5 | 89.0 |
| 125 ohm || 5 pF | drain port 100 ohm | 100.3 | 89.2 | 84.2 |
| 125 ohm || 5 pF | drain port 200 ohm | 97.8 | 87.4 | 80.6 |
| 125 ohm || 5 pF | 200 ohm || 2.5 pF (Cdg max) | 101.3 | 90.7 | 84.0 |

Every internal port anywhere on a VSWR circle around 50 ohm (8 phases; BPF1's antenna port stays 50 ohm), worst-case corner (dB):

| VSWR | nominal | mode B, aligned at 50 | mode B, aligned in circuit | mode A, aligned at 50 |
|---|---|---|---|---|
| 1 | 103.9 | 91.4 | 91.4 | 86.4 |
| 1.1 | 102.0 | 89.5 | 89.8 | 84.4 |
| 1.2 | 100.1 | 87.8 | 88.3 | 82.6 |
| 1.35 | 97.5 | 85.2 | 86.3 | 79.9 |
| 1.5 | 95.0 | 82.9 | 84.4 | 77.4 |
| 1.75 | 91.3 | 79.2 | 81.7 | 73.7 |
| 2 | 87.8 | 75.9 | 79.5 | 70.3 |

BPF1 worst in-band transducer loss with the J310 input as its load (dB): 50 ohm: 1.70 (Q 120), 1.96 (Q 100); J310 input 56 ohm (gfs 18 mS max): 1.68 (Q 120), 1.93 (Q 100); J310 input 83 ohm (Re yig 12 mS typ): 1.83 (Q 120), 2.06 (Q 100); J310 input 125 ohm (gfs 8 mS min): 2.33 (Q 120), 2.54 (Q 100); 56 ohm || 5 pF (Csg max): 1.81 (Q 120), 2.09 (Q 100); 125 ohm || 5 pF: 2.53 (Q 120), 2.80 (Q 100).

LTspice re-simulation of the named cases:

| case | numpy (dB) | LTspice (dB) | agree |
|---|---|---|---|
| nominal, load 50 ohm, drain port 50 ohm | 103.89 | 103.89 | yes |
| mode B corner, load 50 ohm, drain port 50 ohm | 91.40 | 91.40 | yes |
| nominal, load 50 ohm, drain port 200 ohm | 98.35 | 98.35 | yes |
| mode B corner, load 50 ohm, drain port 200 ohm | 87.35 | 87.35 | yes |
| nominal, load J310 input 83 ohm (Re yig 12 mS typ), drain port 200 ohm | 95.46 | 95.46 | yes |
| mode B corner, load J310 input 83 ohm (Re yig 12 mS typ), drain port 200 ohm | 84.80 | 84.80 | yes |
| nominal, load J310 input 125 ohm (gfs 8 mS min), drain port 50 ohm | 100.12 | 100.12 | yes |
| mode B corner, load J310 input 125 ohm (gfs 8 mS min), drain port 50 ohm | 88.48 | 88.48 | yes |
| nominal, load J310 input 125 ohm (gfs 8 mS min), drain port 200 ohm | 93.66 | 93.66 | yes |
| mode B corner, load J310 input 125 ohm (gfs 8 mS min), drain port 200 ohm | 83.36 | 83.36 | yes |
| nominal, load 125 ohm || 5 pF, drain port 200 ohm | 97.84 | 97.84 | yes |
| mode B corner, load 125 ohm || 5 pF, drain port 200 ohm | 87.41 | 87.41 | yes |
| mode B corner, every internal port on VSWR 1.2 | 87.77 | 87.77 | yes |
| mode B corner, every internal port on VSWR 1.5 | 82.86 | 82.86 | yes |

With the proposed design input (every internal port within VSWR 1.2 of 50 ohm, aligned at 50 ohm, mode B): worst-case corner 87.8 dB, **PASS** (before leakage, r10).

## 2 + 3 + 2, IF 10 MHz (alternative)

J310 port cases (worst image rejection over the band, dB):

| BPF1 and BPF2 load (J310 input) | BPF2 and BPF3 source (J310 drain) | nominal, aligned at 50 | mode B corner, aligned at 50 | mode B corner, aligned in circuit |
|---|---|---|---|---|
| 50 ohm | drain port 50 ohm | 86.8 | 78.9 | 78.9 |
| 50 ohm | drain port 100 ohm | 82.8 | 75.4 | 73.6 |
| 50 ohm | drain port 200 ohm | 80.3 | 73.4 | 69.6 |
| 50 ohm | 200 ohm || 2.5 pF (Cdg max) | 83.5 | 76.5 | 73.4 |
| J310 input 56 ohm (gfs 18 mS max) | drain port 50 ohm | 86.1 | 78.3 | 78.0 |
| J310 input 56 ohm (gfs 18 mS max) | drain port 100 ohm | 82.1 | 74.7 | 72.7 |
| J310 input 56 ohm (gfs 18 mS max) | drain port 200 ohm | 79.5 | 72.7 | 68.8 |
| J310 input 56 ohm (gfs 18 mS max) | 200 ohm || 2.5 pF (Cdg max) | 82.7 | 75.8 | 72.5 |
| J310 input 83 ohm (Re yig 12 mS typ) | drain port 50 ohm | 83.8 | 76.2 | 75.0 |
| J310 input 83 ohm (Re yig 12 mS typ) | drain port 100 ohm | 79.6 | 72.4 | 69.6 |
| J310 input 83 ohm (Re yig 12 mS typ) | drain port 200 ohm | 76.8 | 70.2 | 65.5 |
| J310 input 83 ohm (Re yig 12 mS typ) | 200 ohm || 2.5 pF (Cdg max) | 80.0 | 73.2 | 69.4 |
| J310 input 125 ohm (gfs 8 mS min) | drain port 50 ohm | 81.8 | 74.5 | 72.0 |
| J310 input 125 ohm (gfs 8 mS min) | drain port 100 ohm | 77.3 | 70.5 | 66.5 |
| J310 input 125 ohm (gfs 8 mS min) | drain port 200 ohm | 74.4 | 68.1 | 62.4 |
| J310 input 125 ohm (gfs 8 mS min) | 200 ohm || 2.5 pF (Cdg max) | 77.6 | 71.0 | 66.3 |
| 56 ohm || 5 pF (Csg max) | drain port 50 ohm | 87.6 | 79.8 | 78.8 |
| 56 ohm || 5 pF (Csg max) | drain port 100 ohm | 83.6 | 76.3 | 73.5 |
| 56 ohm || 5 pF (Csg max) | drain port 200 ohm | 81.0 | 74.3 | 69.6 |
| 56 ohm || 5 pF (Csg max) | 200 ohm || 2.5 pF (Cdg max) | 84.3 | 77.5 | 73.3 |
| 125 ohm || 5 pF | drain port 50 ohm | 86.0 | 78.7 | 76.0 |
| 125 ohm || 5 pF | drain port 100 ohm | 81.6 | 74.6 | 70.7 |
| 125 ohm || 5 pF | drain port 200 ohm | 78.6 | 72.2 | 66.7 |
| 125 ohm || 5 pF | 200 ohm || 2.5 pF (Cdg max) | 81.9 | 75.3 | 70.5 |

Every internal port anywhere on a VSWR circle around 50 ohm (8 phases; BPF1's antenna port stays 50 ohm), worst-case corner (dB):

| VSWR | nominal | mode B, aligned at 50 | mode B, aligned in circuit | mode A, aligned at 50 |
|---|---|---|---|---|
| 1 | 86.8 | 78.9 | 78.9 | 72.5 |
| 1.1 | 84.8 | 77.0 | 77.1 | 70.4 |
| 1.2 | 82.9 | 75.1 | 75.4 | 68.4 |
| 1.35 | 80.2 | 72.4 | 73.1 | 65.5 |
| 1.5 | 77.7 | 69.9 | 71.0 | 62.8 |
| 1.75 | 73.6 | 65.9 | 67.9 | 58.6 |
| 2 | 69.9 | 62.2 | 65.3 | 54.8 |

BPF1 worst in-band transducer loss with the J310 input as its load (dB): 50 ohm: 1.70 (Q 120), 1.96 (Q 100); J310 input 56 ohm (gfs 18 mS max): 1.68 (Q 120), 1.93 (Q 100); J310 input 83 ohm (Re yig 12 mS typ): 1.83 (Q 120), 2.06 (Q 100); J310 input 125 ohm (gfs 8 mS min): 2.33 (Q 120), 2.54 (Q 100); 56 ohm || 5 pF (Csg max): 1.81 (Q 120), 2.09 (Q 100); 125 ohm || 5 pF: 2.53 (Q 120), 2.80 (Q 100).

LTspice re-simulation of the named cases:

| case | numpy (dB) | LTspice (dB) | agree |
|---|---|---|---|
| nominal, load 50 ohm, drain port 50 ohm | 86.75 | 86.75 | yes |
| mode B corner, load 50 ohm, drain port 50 ohm | 78.85 | 78.85 | yes |
| nominal, load 50 ohm, drain port 200 ohm | 80.28 | 80.28 | yes |
| mode B corner, load 50 ohm, drain port 200 ohm | 73.44 | 73.44 | yes |
| nominal, load J310 input 83 ohm (Re yig 12 mS typ), drain port 200 ohm | 76.81 | 76.81 | yes |
| mode B corner, load J310 input 83 ohm (Re yig 12 mS typ), drain port 200 ohm | 70.21 | 70.21 | yes |
| nominal, load J310 input 125 ohm (gfs 8 mS min), drain port 50 ohm | 81.77 | 81.77 | yes |
| mode B corner, load J310 input 125 ohm (gfs 8 mS min), drain port 50 ohm | 74.53 | 74.53 | yes |
| nominal, load J310 input 125 ohm (gfs 8 mS min), drain port 200 ohm | 74.38 | 74.38 | yes |
| mode B corner, load J310 input 125 ohm (gfs 8 mS min), drain port 200 ohm | 68.05 | 68.05 | yes |
| nominal, load 125 ohm || 5 pF, drain port 200 ohm | 78.60 | 78.60 | yes |
| mode B corner, load 125 ohm || 5 pF, drain port 200 ohm | 72.15 | 72.15 | yes |
| mode B corner, every internal port on VSWR 1.2 | 75.11 | 75.11 | yes |
| mode B corner, every internal port on VSWR 1.5 | 69.88 | 69.88 | yes |

With the proposed design input (every internal port within VSWR 1.2 of 50 ohm, aligned at 50 ohm, mode B): worst-case corner 75.1 dB, **PASS** (before leakage, r10).

![ports_sensitivity.png](ports_sensitivity.png)
![bpf1_loss_vs_j310_input.png](bpf1_loss_vs_j310_input.png)

LTspice agreement with every numpy prediction: yes.
