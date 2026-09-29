# 2026-09-28-r08-bpf-tolerance-corners: result

Checker: worst_case.py check r08. Requirement: REQ-SYS-033, image response at least 70 dB (TBR) below the in-band response at every tuned frequency 144.0 to 148.0 MHz (100 kHz spacing, TC-SYS-021). Acceptance (fixed before the run): (a) the worst-case corner of the tolerance box passes; (b) a Monte Carlo is a yield estimate only (zero runs below 70 dB in N runs bounds the failing fraction at 1 - 0.05^(1/N) with 95 % confidence).
Coil Q 100, capacitor Q 500, 5 nH vias, residual tuning +/-0.3 % in frequency (estimate), 50 ohm ports. Numpy Monte Carlo N = 20000, seed 20260936; LTspice re-simulates every corner (agreement limit 0.01 dB) and runs a 1000-run Monte Carlo of 2 + 3 + 3.

| configuration | nominal Q 100 (dB) | case | worst-case corner (dB) at tuned MHz | LTspice corner (dB) | MC 20k min / p0.1 / p1 / median (dB) | MC runs below 70 dB (95 % interval) | verdict (corner) |
|---|---|---|---|---|---|---|---|
| 2 + 3, IF 8 MHz (TS-012 revision 4) | 51.3 | mode A, no re-alignment (rev 1 model) | 27.35 at 148.0 | 27.35 | 34.2 / 37.0 / 40.0 / 50.5 | 20000 of 20000 = 100 % (99.98 to 100 %) | **FAIL** |
| 2 + 3, IF 8 MHz (TS-012 revision 4) | 51.3 | mode B, no re-alignment (rev 1 model) | 39.77 at 148.0 | 39.77 | 43.5 / 44.7 / 46.0 / 51.2 | 20000 of 20000 = 100 % (99.98 to 100 %) | **FAIL** |
| 2 + 3, IF 8 MHz (TS-012 revision 4) | 51.3 | mode A, aligned at 50 ohm | 41.22 at 148.0 | 41.22 | 44.5 / 45.3 / 46.6 / 51.1 | 20000 of 20000 = 100 % (99.98 to 100 %) | **FAIL** |
| 2 + 3, IF 8 MHz (TS-012 revision 4) | 51.3 | mode B, aligned at 50 ohm | 45.01 at 148.0 | 45.01 | 46.8 / 47.7 / 48.3 / 51.1 | 20000 of 20000 = 100 % (99.98 to 100 %) | **FAIL** |
| 2 + 3 + 3, IF 8 MHz (revision 1 proposal) | 86.0 | mode A, no re-alignment (rev 1 model) | 49.09 at 148.0 | 49.09 | 63.6 / 68.1 / 72.1 / 84.9 | 65 of 20000 = 0.325 % (0.2509 to 0.4141 %) | **FAIL** |
| 2 + 3 + 3, IF 8 MHz (revision 1 proposal) | 86.0 | mode B, no re-alignment (rev 1 model) | 67.23 at 148.0 | 67.23 | 74.9 / 77.3 / 79.2 / 85.9 | 0 of 20000 = 0 % (0 to 0.01844 %) | **FAIL** |
| 2 + 3 + 3, IF 8 MHz (revision 1 proposal) | 86.0 | mode A, aligned at 50 ohm | 70.12 at 148.0 | 70.12 | 76.9 / 78.3 / 80.1 / 85.8 | 0 of 20000 = 0 % (0 to 0.01844 %) | **PASS** |
| 2 + 3 + 3, IF 8 MHz (revision 1 proposal) | 86.0 | mode B, aligned at 50 ohm | 75.63 at 148.0 | 75.63 | 79.5 / 80.9 / 82.0 / 85.8 | 0 of 20000 = 0 % (0 to 0.01844 %) | **PASS** |
| 2 + 3 + 4, IF 8 MHz (margin lever, new here) | 103.9 | mode A, no re-alignment (rev 1 model) | 64.68 at 148.0 | 64.68 | 82.6 / 85.6 / 89.4 / 102.7 | 0 of 20000 = 0 % (0 to 0.01844 %) | **FAIL** |
| 2 + 3 + 4, IF 8 MHz (margin lever, new here) | 103.9 | mode B, no re-alignment (rev 1 model) | 81.75 at 148.0 | 81.75 | 91.8 / 93.7 / 96.0 / 103.7 | 0 of 20000 = 0 % (0 to 0.01844 %) | **PASS** |
| 2 + 3 + 4, IF 8 MHz (margin lever, new here) | 103.9 | mode A, aligned at 50 ohm | 86.43 at 148.0 | 86.43 | 94.2 / 95.8 / 97.6 / 103.6 | 0 of 20000 = 0 % (0 to 0.01844 %) | **PASS** |
| 2 + 3 + 4, IF 8 MHz (margin lever, new here) | 103.9 | mode B, aligned at 50 ohm | 91.40 at 148.0 | 91.40 | 96.9 / 98.0 / 99.2 / 103.6 | 0 of 20000 = 0 % (0 to 0.01844 %) | **PASS** |
| 2 + 3 + 2, IF 10 MHz (alternative) | 86.8 | mode A, no re-alignment (rev 1 model) | 54.82 at 148.0 | 54.82 | 68.1 / 70.4 / 74.2 / 85.7 | 13 of 20000 = 0.065 % (0.03461 to 0.1111 %) | **FAIL** |
| 2 + 3 + 2, IF 10 MHz (alternative) | 86.8 | mode B, no re-alignment (rev 1 model) | 72.84 at 148.0 | 72.84 | 77.9 / 80.0 / 81.4 / 86.6 | 0 of 20000 = 0 % (0 to 0.01844 %) | **PASS** |
| 2 + 3 + 2, IF 10 MHz (alternative) | 86.8 | mode A, aligned at 50 ohm | 72.52 at 148.0 | 72.52 | 77.8 / 79.5 / 81.1 / 86.6 | 0 of 20000 = 0 % (0 to 0.01844 %) | **PASS** |
| 2 + 3 + 2, IF 10 MHz (alternative) | 86.8 | mode B, aligned at 50 ohm | 78.85 at 148.0 | 78.85 | 81.6 / 82.8 / 83.5 / 86.6 | 0 of 20000 = 0 % (0 to 0.01844 %) | **PASS** |

Interior search: a bounded L-BFGS-B minimisation from the worst vertex and six random interior points at the worst tuned frequency found no point below the vertex (column `corner_polished_db` in result.json), so each corner is a vertex of the box.

Residual tuning after alignment (mode B, aligned at 50 ohm), worst-case corner (dB):

| configuration | +/-0.1 % | +/-0.2 % | +/-0.3 % | +/-0.5 % | +/-0.75 % | +/-1 % | +/-1.5 % |
|---|---|---|---|---|---|---|---|
| 2 + 3, IF 8 MHz (TS-012 revision 4) | 46.1 | 45.6 | 45.0 | 43.9 | 42.3 | 40.7 | 36.8 |
| 2 + 3 + 3, IF 8 MHz (revision 1 proposal) | 77.4 | 76.5 | 75.6 | 73.8 | 71.3 | 68.7 | 62.3 |
| 2 + 3 + 4, IF 8 MHz (margin lever, new here) | 93.4 | 92.4 | 91.4 | 89.3 | 86.4 | 83.2 | 75.1 |
| 2 + 3 + 2, IF 10 MHz (alternative) | 80.1 | 79.5 | 78.9 | 77.6 | 75.8 | 74.0 | 69.6 |

LTspice Monte Carlo of 2 + 3 + 3 at IF 8 MHz, N = 1000, seed 20261036:

| case | LTspice min / p1 / median (dB) | runs below 70 dB | 95 % bound or interval on the failing fraction | numpy 20k min / median, same case (dB) | max numpy-LTspice difference, same draws (dB) |
|---|---|---|---|---|---|
| mode A, no re-alignment (rev 1 model) | 67.6 / 71.5 / 85.1 | 4 | 0.11 to 1 % | 63.6 / 84.9 | 4.6e-04 |
| mode A, aligned at 50 ohm | 78.2 / 79.9 / 85.9 | 0 | < 0.3 % (zero failures) | 76.9 / 85.8 | 3.9e-04 |
| mode B, aligned at 50 ohm | 80.6 / 81.9 / 85.9 | 0 | < 0.3 % (zero failures) | 79.5 / 85.8 | 3.8e-04 |

![corners_summary.png](corners_summary.png)
![mc20k_distributions.png](mc20k_distributions.png)
![corner_vs_residual.png](corner_vs_residual.png)
![corner_2p3p3_ltspice.png](corner_2p3p3_ltspice.png)

Verdict (proposed configuration 2 + 3 + 3, mode B, aligned at 50 ohm, 50 ohm ports): **PASS**; LTspice agreement with every numpy prediction: yes.
Mode A (TS-012 20 % capacitors) and the no-re-alignment model are reported, not proposed. Ports and leakage are added in r09 and r10.
