# Harmonic low-pass filter analysis for the TS-012 finalists

| Field | Value |
|---|---|
| Product | Analysis note (08 section 3.4), WP-PDR-21 LPF item of TS-012 revision 4 section 7.3, PDR draft revision 2, 2026-09-28 |
| Author | Claude, analysis author (TS-012 discriminating analyses, owner approval of 2026-09-28: "you should go ahead and run the simulations and analysis", `docs/plan/status/status-2026-09-28.md` section 1). Revision 2 the same day, fixing the Major findings finding-1, finding-2 and finding-3 and the Minor findings finding-4 and finding-5 of the independent review of revision 1 |
| Status | Draft, not reviewed. Re-review of revision 2 is needed before the owner relies on it. The values below are proposals until an independent review approves this record (plan rule C10) |
| Review record | Independent review of revision 1 (findings relayed to the author 2026-09-28; the record is filed by the reviewer). Section 9 maps each finding to its fix |
| Serves | TS-012 choice between A4 and A5 (C5 evidence, section 7.1 harmonic risks); REQ-TX-009, 010, 011 TBR values; REQ-SYS-017, 018 and REQ-TX-007, 008 pre-build supporting evidence; REQ-SYS-012 power budget of A5 (filter loss term); HZ-008 K1 |
| Model, checker, plots | `hardware/sim/tx-lpf/` (`lpf_model.py`, `lpf_nodal.py`, `worst_case.py`, `run_lpf.py`, `retune_screen.py`, `README.md`). Revision 2 results: `hardware/sim/tx-lpf/results/2026-09-28-r1-nominal`, `r8` to `r14` (worst case and Monte Carlo per build), `r15` (harmonic budget) and `r16` (trap screen). Revision 1 runs `r2` to `r7` and `r5` are kept as the record and are superseded |
| Checker exit status | `run_lpf.py all` exits 1: every check passes and criteria fail (listed in section 5 and 7). 0 means every criterion met, 2 means a check failed and the results must not be used (review finding-5) |
| Evidence status | Developer evidence. LTspice 26.0.2 through `tools/ltspice-batch.sh` blob `88b71475` (ACC-LTSPICE-001, every run's wrapper line in its `ltspice_provenance.txt`); venv Python 3.13.5 (TV-001), numpy 2.5.3, scipy 1.18.1, matplotlib 3.11.2, spicelib 1.6.3 (class B entries without a TV record of their own) |

## 1. Purpose

TS-012 revision 4 asks, before the order, for an LTspice run of the 7-pole Chebyshev harmonic low-pass filter (fc 165 MHz; BOM 22 pF, 68 nH, 39 pF, 82 nH, 39 pF, 68 nH, 22 pF; Coilcraft 1812SMS and 1206 C0G) with the inductor Q and self-resonance and the pad and via parasitics, with the pass criteria: at least 40 dB at 288 to 296 MHz, 35 dB at 432 to 444 MHz and passband loss at most 0.5 dB (section 7.3, WP-PDR-21). This note answers:

1. Does the filter as specified meet those criteria and REQ-TX-011 (40 dB from 576 MHz to 1.5 GHz), nominally and at the worst case over component tolerance and parasitics, with the catalog Coilcraft coils and with coils hand-wound from the owner's 24 AWG enamelled wire?
2. Combined with each finalist's PA harmonic levels, does the transmitter meet 47 CFR 97.307(e) at every power step, every pack voltage from 6.4 to 8.4 V and every instant of the keying envelope, and the REQ-SYS-018 60 dBc target at the 5 W step?
3. What must change or be decided before the order?

The limit used is the one 97.307(e) sets for a transmitter of mean power 25 W or less between 30 and 225 MHz: a spurious emission supplied to the antenna transmission line "must not exceed 25 uW and must be at least 40 dB below the mean power of the fundamental emission, but need not be reduced below the power of 10 uW" (`docs/references/md/regulatory/47cfr-97.307.md`, eCFR 2026-09-23). The 60 dB figure in the first sentence of (e) is for transmitters above 25 W and is not used. At every cwht power step (0.5 to 6.3 W with the +1 dB tolerance) 25 uW (-16.0 dBm) is the binding bound (54 dBc at 6.3 W); the 10 uW floor binds only below 0.25 W, which the keying-ramp check covers.

## 2. Method

1. **Decks.** Written by `run_lpf.py` from `lpf_model.py` and run only through `tools/ltspice-batch.sh`. AC analysis, 50 ohm source and load, 2 V source so that S21 = V(out) and S11 = V(in) - 1. Nominal deck (r1): 0.5 to 1600 MHz in 0.5 MHz steps. Revision 2 decks (r8 to r14, r16): `.ac list` on the grid `lpf_model.FREQS` (914 points: 2 MHz steps from 2 to 1600 MHz, the carriers 144 to 148 MHz in 0.25 MHz steps, and n times each of those carriers for n = 2 to 10), 259 steps each:
   - steps 1 and 2: every L and C at -tol and +tol with nominal parasitics (revision 1's two corners, kept for comparison);
   - steps 3 to 252: uniform random draws over the whole parameter box (numpy seeds 21008 to 21016);
   - steps 253 to 259: the worst-case corners that the corner search (item 4) found, one per metric.
   Every parameter of every step is in the run's `mc_values.csv` and bound into the deck by `table(run, ...)`.
2. **Filter topology with parasitics.** Each shunt capacitor: pad capacitance to ground in parallel with C + ESR + ESL + ground via inductance. Each coil: track inductance split both sides, L + R (R from the Q at 150 MHz) with Cpar across (Cpar from the self-resonant frequency) plus the pad-to-pad fringe. Mutual coupling between adjacent coils (K24, K46) and between the first and last coil (K26), and a direct input-to-output leakage capacitance, stand in for layout coupling. **Revision 2: the coupling coefficients are signed** (review finding-1). The sign depends on the winding sense and the orientation of each coil on the board, which the layout does not fix, so each K ranges from minus to plus its bound (section 3). The nominal stays at the positive mid value, so run r1 is unchanged.
3. **Parameter box.** Every parameter of every part varies independently over the ranges of section 3: 39 parameters per build (C, ESR, ESL, via L and pad C of each of the four capacitors; L, Q, SRF, fringe C and track L of each of the three coils; K24, K46, K26 and the leakage C). Independence is conservative: on one board the four capacitors share the via rule and the board thickness, and parts from one reel are correlated, which the analysis does not credit.
4. **Worst case by corner search (revision 2, review finding-1).** Revision 1 reported the worst of 252 Monte Carlo steps as the worst case. With 39 independent parameters a uniform draw almost never lands near a corner, so that sample worst is not a bound. `worst_case.py` searches the box for the instance that makes each metric worst: bounded quasi-Newton (scipy L-BFGS-B on the normalised box) from 9 starts (the nominal, the vertex the first-order sensitivities point to, the worst Monte Carlo step of that metric, and 6 seeded random vertices), each followed by a coordinate pass that tries both bounds of every parameter until no move improves the metric. The fast evaluator is `lpf_nodal.py`, a nodal model of exactly the deck's circuit; every corner is then run in LTspice and **every verdict comes from the LTspice numbers**. A search is not a proof of the global worst; the report gives, per metric, the start that found the worst and the value from every start (`result.json`, `search`), and in r8 to r14 every one of the 39 parameters of every corner sits at a bound.
5. **Known answers and cross-checks.** (a) The ideal exact-value filter against the analytic 0.1 dB Chebyshev: maximum error 0.0005 dB over 0.5 to 1600 MHz where the analytic value is under 150 dB (criterion 0.05 dB): **PASS** (run r1). The analytic values reproduce the adversarial C8 recomputation cited in TS-012: 47.9 dB at 288 MHz, 76.0 dB at 432 MHz. (b) The nodal model against LTspice at every step and every frequency of every revision 2 run: largest difference 1.7e-4 dB in r8 to r14 and 1.4e-3 dB in r16 (criterion 0.01 dB): **PASS**. (c) Every corner's metric in LTspice equals the search value within 0.01 dB: **PASS** in every run. (d) The L4 value that LTspice echoes by `.meas` equals `mc_values.csv`, and the `.meas` S21 at 288 MHz equals the `.raw` value within 0.001 dB, for every step: **PASS** in every run.
6. **Metrics.** Insertion loss IL = -S21 (dB), the maximum over 144 to 148 MHz; its dissipative part |S21|^2 / (1 - |S11|^2) is reported beside it. Attenuation A per harmonic band = the minimum of -S21 over n x 144 to n x 148 MHz, n = 2 to 10. **Revision 2 (review finding-4): the harmonic budget uses A(nf) - IL(f)**, the minimum over the carriers f of 144 to 148 MHz of the attenuation at the carrier's harmonic less the passband loss at that carrier, in the same filter instance. The PA harmonic ratio is relative to the carrier at the PA output, and the carrier at the antenna is lower by IL(f), so the harmonic relative to the antenna carrier is H - A(nf) + IL(f). Revision 1 left out the IL term.
7. **Harmonic budget (run r15).** Harmonic at the antenna = carrier at the step +1 dB + PA harmonic ratio - [A(nf) - IL(f)], for every step (0.5, 1, 2, 5 W at +1 dB), every pack voltage (6.4, 7.2, 8.4 V; review finding-3) and n = 2 to 10, against the 97.307(e) limit at that carrier level; the 60 dBc target is checked as a ratio at the 5 W step at each pack voltage; the keying ramp is checked at 400 instantaneous levels from 1 mW to 6.3 W at each pack voltage with the limit at each level (the 10 uW floor included). Two bases are reported: the worst case (the worst of every LTspice step of the build, which is the corner) and the Monte Carlo worst (steps 1 to 252). The verdict is on the worst case.
8. **PA harmonic state per pack voltage (revision 2, review finding-3).** The ALC holds the carrier at the step at every pack voltage, so the carrier at the antenna does not change; the PA's operating state does. A5 at the 5 W step: at 6.4 V the module runs at or near its full output (4.5 to 5.1 W at the module, TS-012 section 7.3) and at 7.2 V the step is 0.8 dB under the 6 W guarantee point, so both take the datasheet maxima (an estimate outside the guarantee's exact condition); at 8.4 V the module could make about 10.5 W (`docs/research/pa-device-candidates.md` F8), so 5 W is a VGG back-off state outside the 6 W, 7.2 V guarantee, and the back-off convention (-17 dBc 2f, -25 dBc 3f and above) applies. The lower steps take the back-off convention at every pack voltage. A4 takes its F17 assumption at every step and pack voltage.
9. **Retune (revision 1).** Revision 1 chose the set 18 pF, 68 nH, 33 pF, 82 nH, 33 pF, 68 nH, 18 pF with `retune_screen.py` (ABCD model, stacked corner). Revision 2 runs it as r11 and r12 and withdraws it (section 5).
10. **Value screen (revision 2).** To answer section 7 item 1, symmetric E24 sets of the same 7-pole topology (C1 18 to 22 pF, C3 30 to 39 pF, L2 56 or 68 nH, L4 68 or 82 nH) at 5 % and at 2 % tolerance were screened with the corner search in its quick form (nominal and sensitivity-vertex starts; `worst_case.search(quick=True)`). No set reaches 0.5 dB at the worst case. The two 2 % builds that keep the 60 dBc target within reach (the BOM values and 22/68/36/82) were then run in full as r13 and r14. A variant with trap capacitors across the outer coils (10/47/20/68 pF and nH, 5.6 pF across L2 and L6) was screened because it had the lowest loss of a nominal screen of about 7000 trap sets; its full run is r16.

## 3. Inputs and sources

| Input | Value | Source and confidence |
|---|---|---|
| Filter design | 7-pole Chebyshev, 0.1 dB ripple, ripple cut-off 165 MHz, shunt C first; exact g-values give 22.8 pF, 68.6 nH, 40.4 pF, 75.9 nH | TS-012 section 7.3; g-values computed (C) |
| BOM values | 22 pF, 68 nH, 39 pF, 82 nH, 39 pF, 68 nH, 22 pF | TS-012 section 8.3 rows 4, 5 and E1 (D for the parts, the values are TS-012's) |
| Coilcraft 1812SMS-68N | L at 150 MHz, 5 % (J) or 2 % (G); Q typ 120, min 100 at 150 MHz; SRF min 1.5 GHz | Coilcraft Document 184-1, revised 12/02/21, read 2026-09-28 at https://www.coilcraft.com/getmedia/c6fe1f83-b176-469d-a071-e2edb068fef2/midi.pdf (D) |
| Coilcraft 1812SMS-82N | Q typ 120, min 100 at 150 MHz; SRF min 1.3 GHz | same (D) |
| Coilcraft 1812SMS-47N (r16 only) | Q typ 135, min 100 at 150 MHz; SRF min 2.1 GHz | same (D) |
| 1812SMS model ranges | Nominal Q 100 (the minimum); Q 100 to 130; SRF from the minimum to 1.3 x the minimum (typical SRF not published) | Q range above typ and SRF spread (E) |
| 1206 C0G capacitors | KEMET C1206C220J1GACTU and C1206C390J1GACTU: J = +/-5 %; the G code of the same series is +/-2 % (runs r13, r14) | part-number convention (D); the G part numbers and their stock are not read (ordering gate) |
| Capacitor ESR and ESL | ESR 0.1 to 0.4 ohm (nominal 0.2); ESL 0.6 to 1.2 nH (nominal 1.0) | typical published ranges for 1206 C0G MLCCs at 100 to 500 MHz; KEMET K-SIM not read (E) |
| Ground via of each shunt C | 0.27 nH (two vias, 0.8 mm board) to 1.30 nH (one via, 1.6 mm board); nominal 0.85 nH | closed form L = 0.2 h (ln(4h/d) + 1) nH, d 0.3 mm (C); board thickness not yet fixed |
| Node pad capacitance | 0.17 to 0.53 pF (1206 pad plus one or two coil pads, 1.6 or 0.8 mm FR4, er 4.5) | parallel-plate (C); er 4.5 (E) |
| Track inductance per coil | 0.5 to 2.0 nH (nominal 1.0) | (E) |
| Pad-to-pad fringe across a coil | 0.02 to 0.08 pF | (E) |
| Coil coupling (revision 2: signed) | adjacent 1812SMS -0.01 to +0.01 (nominal +0.005), air coils -0.03 to +0.03 (nominal +0.015); first to last coil -0.003 to +0.003 (1812SMS), -0.006 to +0.006 (air) | (E), parallel axes 8 to 10 mm apart; the sign follows the winding sense and orientation (review finding-1) |
| Input-to-output leakage | 0.5 to 5 fF (nominal 2 fF) | (E), end pads over a bottom ground pour; this term sets the stopband floor above about 600 MHz |
| Trap capacitor (r16 only) | 5.6 pF +/-0.25 pF (C code), ESR and ESL as the shunt capacitors | part-number convention (D); ESR, ESL (E) |
| Air coils, 24 AWG | wire 0.511 mm bare (ASTM B258, D), 0.56 mm with enamel (E); wound on a 3.0 mm drill shank at 1.0 mm pitch, leads 3 mm: 68 nH = 6.75 turns, 82 nH = 8 turns (calculated 69.6 and 84.5 nH, set by squeezing on the NanoVNA) | Nagaoka (Lundin form) with Rosa's correction (C) |
| Air-coil Q and SRF | Q about 217 and 223 at 146 MHz (skin effect x 1.8 proximity factor); self-capacitance 0.17 to 0.18 pF (Medhurst), SRF about 1.46 and 1.30 GHz; ranges: Q 0.6 to 1.0 x, self-capacitance 0.5 to 1.5 x | (C) with Low confidence (E for the proximity factor) |
| Air-coil tolerance | as wound +/-10 % (run r9); aligned on the NanoVNA +/-3 % (runs r10, r12) | (E) |
| A5 PA harmonics, full state | RA07M1317M: 2fo -25 dBc max, 3fo -30 dBc max at Pout 6 W, VDD 7.2 V, VGG adjusted; used at the 5 W step at 6.4 and 7.2 V | datasheet (Jun 2019) via `docs/research/pa-device-candidates.md` F8, F16 (D at the guarantee point; E at 6.4 V and at 5 W) |
| A5 PA harmonics, back-off state | 2f -17 dBc; 3f and above -25 dBc; used at 0.5, 1 and 2 W at every pack voltage, at the 5 W step at 8.4 V, and at ramp instants below 5 W | (E): AN-VHF-053-A gate-ramp worst 2fo ratio (-17.4 dBc at 0.3 W, F4) applied to the module; 3f degraded 5 dB from the guarantee |
| A5 output at 8.4 V, full drive | about 10.5 W (graph read); `docs/design/analysis/pa-drive-ts012.md` digitizes 10.9 W typical at 155 MHz | F8 (E, graph read) |
| A5 4f and above | equal to the 3f value of the state | (E), no data |
| A4 PA harmonics | AFT05MS004N: no vendor harmonic data (datasheet Rev. 0, 7/2014, searched 2026-09-28 at https://www.nxp.com/docs/en/data-sheet/AFT05MS004N.pdf: no harmonic or dBc entry). Taken at 2fo -15 dBc, 3fo and above -20 dBc at every step and pack voltage | F17 assumption for a raw single-ended class-AB stage (E, Low); the hand-derived match may give more |
| Power steps | 0.5, 1, 2 W (REQ-SYS-011) and 5 W (REQ-SYS-012), each at +1 dB | requirements (D) |
| Pack voltages | 6.4, 7.2 and 8.4 V | REQ-SYS-017, REQ-TX-007, REQ-SYS-012 (D) |
| A5 module output at the 6.4 V pack end | 4.46 to 5.13 W; relay loss 0.1 dB | TS-012 revision 4 section 7.3 (E, graph read; `pa-drive-ts012.md` shows this is a nominal range, not a bound) |

## 4. Results

### 4.1 Nominal (run r1)

| Build | IL max 144-148 (dB) | RL min (dB) | 2f (dB) | 3f (dB) | 576-1500 MHz (dB) | 7f (dB) |
|---|---|---|---|---|---|---|
| Ideal exact values | 0.100 | 16.4 | 47.9 | 76.0 | 94.5 | 129.4 |
| Ideal BOM values | 0.005 | 29.7 | 47.2 | 75.2 | 93.8 | 128.7 |
| 1812SMS with parasitics | **0.699** | 30.9 | 58.8 | 87.0 | 77.6 | 96.1 |
| Air coils with parasitics | 0.491 | 31.0 | 57.4 | 84.9 | 77.1 | 95.0 |

Loss decomposition of the nominal 1812SMS build: coil loss alone 0.42 dB, capacitor ESR alone 0.28 dB (estimate-driven). The parasitics raise the stopband attenuation near 2f and 3f (each shunt capacitor's ESL and via inductance resonate it at 590 to 790 MHz, so its reactance at 288 MHz is that of a capacitor about 15 to 30 % larger) and pull the passband edge down from about 170 to about 162 MHz, which raises the loss at 148 MHz. Above about 600 MHz the stopband floor is set by the assumed input-to-output leakage and coil coupling, not by the ladder. Run r1 was rerun in revision 2 with identical numbers; its plot now marks the A(nf) - IL(f) each finalist needs over 6.4 to 8.4 V.

![Nominal S21 with the harmonic limit points](../../../hardware/sim/tx-lpf/results/2026-09-28-r1-nominal/s21_nominal_wide.png)

![Nominal passband loss](../../../hardware/sim/tx-lpf/results/2026-09-28-r1-nominal/il_nominal_passband.png)

![Nominal input return loss](../../../hardware/sim/tx-lpf/results/2026-09-28-r1-nominal/rl_nominal_passband.png)

### 4.2 Worst case and Monte Carlo per build (runs r8 to r14)

Worst case: the corner of section 2 item 4, run in LTspice. Monte Carlo: 252 steps, the median and the 99th percentile (loss) or 1st percentile (attenuation). All values in dB.

| Run | Build | IL: worst case / MC 99 % / MC median | 2f: worst case / MC 1 % | 3f worst case | 576-1500 MHz worst case | A(2f) - IL(f): worst case / MC worst | Worst-case verdict (0.5 dB; 40, 35, 40 dB) |
|---|---|---|---|---|---|---|---|
| r8 | 1812SMS J, BOM 22/68/39/82 | **2.82** / 1.12 / 0.77 | 45.1 / 52.9 | 70.1 | 61.8 | 44.5 / 51.9 | FAIL (IL) |
| r9 | Air as wound +/-10 %, BOM | **5.34** / 1.42 / 0.73 | **39.7** / 48.8 | 63.1 | 59.3 | 39.3 / 47.3 | FAIL (IL, REQ-TX-009) |
| r10 | Air aligned +/-3 %, BOM | **3.38** / 1.03 / 0.67 | 41.8 / 49.5 | 64.2 | 59.6 | 41.3 / 48.3 | FAIL (IL) |
| r11 | 1812SMS J, retuned 18/68/33/82 | **1.39** / 0.67 / 0.53 | **38.3** / 45.9 | 64.8 | 62.7 | 37.9 / 44.4 | FAIL (IL, REQ-TX-009) |
| r12 | Air aligned +/-3 %, retuned | **1.56** / 0.62 / 0.45 | **35.6** / 43.3 | 59.1 | 60.6 | 35.2 / 41.6 | FAIL (IL, REQ-TX-009) |
| r13 | 1812SMS G and C0G G (2 %), BOM | **1.76** / 0.93 / 0.74 | 47.1 / 53.3 | 71.0 | 61.9 | 46.5 / 51.8 | FAIL (IL) |
| r14 | 1812SMS G and C0G G (2 %), 22/68/36/82 | **1.24** / 0.80 / 0.65 | 45.6 / 51.4 | 71.1 | 61.9 | 45.0 / 50.4 | FAIL (IL) |

- **Passband loss: no build meets 0.5 dB at the worst case, and none meets it at the Monte Carlo median** (lowest median 0.45 dB, aligned air coils with the retuned values). Revision 1's proposed 0.75 dB criterion is not met at the worst case by any build either (lowest 1.24 dB, r14), so that proposal is withdrawn.
- **Where the worst-case loss comes from.** For the BOM values the loss corner is every L and C at its +tol bound, every ESR at 0.4 ohm, every Q at 100, and the adjacent couplings at -0.01: all of it within the section 3 ranges, and all parts high is the one-reel case rather than an unlikely mixed stack. It pulls the cut-off down onto the band edge (plot `il_wc_passband.png`). The dissipative part of that loss is 1.74 dB of the 2.82 dB for r8, 1.37 of 1.76 dB for r13 and 0.78 of 1.39 dB for r11. Revision 1's two corners moved L and C only, with nominal parasitics and positive K; they give 1.07 dB (r8) and 0.58 dB (r11) at +tol.
- **Stopband.** 3f and 576 MHz to 1.5 GHz pass in every build at the worst case (at least 59.1 and 59.3 dB against 35 and 40 dB). **REQ-TX-009 (40 dB at 2f) fails at the worst case for both retuned builds (38.3, 35.6 dB) and for the as-wound air coils (39.7 dB)**; the BOM values with catalog coils keep 45.1 dB (J) and 47.1 dB (G).
- **The two-via layout rule is the lowest-2f corner.** In every build the 2f worst-case corner has every shunt capacitor's ground via at 0.27 nH, the low end of the range (two vias on a 0.8 mm board, section 7 item 5). At the nominal BOM 1812SMS build, 0.27 nH instead of 1.30 nH lowers 2f from 61.3 to 55.8 dB, lowers the loss by 0.08 dB and raises the 576 MHz to 1.5 GHz attenuation from 72.7 to 87.4 dB (nodal model). The worst-case 2f figures above already include this corner. Revision 1 did not say so.
- **Signed coupling.** The IL corners of every 1812SMS build take the adjacent couplings at -0.01; revision 1's positive-only range could not reach them.
- **Comparison with the reviewer's corners.** The review found, inside revision 1's ranges, retuned 1812SMS loss 0.81 to 0.90 dB and 2f 41.4 dB, retuned air coils 0.74 to 0.86 dB and 40.2 dB, and BOM 1812SMS 1.94 dB and 48.9 dB. The corner search is at least as severe in every case: 1.39 and 38.3 dB, 1.56 and 35.6 dB, 2.82 and 45.1 dB.

Plots per run (the S21 spread with the corners and the needed levels, the 2f and 3f bands, the passband with the corners and criteria, and the distributions with the worst case and the limits):

![r8 S21, 1812SMS, BOM values](../../../hardware/sim/tx-lpf/results/2026-09-28-r8-wc-1812sms-bom/s21_wc_wide.png)

![r8 passband loss](../../../hardware/sim/tx-lpf/results/2026-09-28-r8-wc-1812sms-bom/il_wc_passband.png)

![r8 harmonic bands](../../../hardware/sim/tx-lpf/results/2026-09-28-r8-wc-1812sms-bom/harmonic_bands_wc.png)

![r8 distributions](../../../hardware/sim/tx-lpf/results/2026-09-28-r8-wc-1812sms-bom/mc_wc_histograms.png)

![r9 S21, air coils as wound, BOM values](../../../hardware/sim/tx-lpf/results/2026-09-28-r9-wc-air-aswound-bom/s21_wc_wide.png)

![r9 passband loss](../../../hardware/sim/tx-lpf/results/2026-09-28-r9-wc-air-aswound-bom/il_wc_passband.png)

![r9 harmonic bands](../../../hardware/sim/tx-lpf/results/2026-09-28-r9-wc-air-aswound-bom/harmonic_bands_wc.png)

![r9 distributions](../../../hardware/sim/tx-lpf/results/2026-09-28-r9-wc-air-aswound-bom/mc_wc_histograms.png)

![r10 S21, air coils aligned, BOM values](../../../hardware/sim/tx-lpf/results/2026-09-28-r10-wc-air-aligned-bom/s21_wc_wide.png)

![r10 passband loss](../../../hardware/sim/tx-lpf/results/2026-09-28-r10-wc-air-aligned-bom/il_wc_passband.png)

![r10 harmonic bands](../../../hardware/sim/tx-lpf/results/2026-09-28-r10-wc-air-aligned-bom/harmonic_bands_wc.png)

![r10 distributions](../../../hardware/sim/tx-lpf/results/2026-09-28-r10-wc-air-aligned-bom/mc_wc_histograms.png)

![r11 S21, 1812SMS, retuned](../../../hardware/sim/tx-lpf/results/2026-09-28-r11-wc-1812sms-retuned/s21_wc_wide.png)

![r11 passband loss](../../../hardware/sim/tx-lpf/results/2026-09-28-r11-wc-1812sms-retuned/il_wc_passband.png)

![r11 harmonic bands](../../../hardware/sim/tx-lpf/results/2026-09-28-r11-wc-1812sms-retuned/harmonic_bands_wc.png)

![r11 distributions](../../../hardware/sim/tx-lpf/results/2026-09-28-r11-wc-1812sms-retuned/mc_wc_histograms.png)

![r12 S21, air coils aligned, retuned](../../../hardware/sim/tx-lpf/results/2026-09-28-r12-wc-air-aligned-retuned/s21_wc_wide.png)

![r12 passband loss](../../../hardware/sim/tx-lpf/results/2026-09-28-r12-wc-air-aligned-retuned/il_wc_passband.png)

![r12 harmonic bands](../../../hardware/sim/tx-lpf/results/2026-09-28-r12-wc-air-aligned-retuned/harmonic_bands_wc.png)

![r12 distributions](../../../hardware/sim/tx-lpf/results/2026-09-28-r12-wc-air-aligned-retuned/mc_wc_histograms.png)

![r13 S21, 2 % parts, BOM values](../../../hardware/sim/tx-lpf/results/2026-09-28-r13-wc-1812sms-bom-2pct/s21_wc_wide.png)

![r13 passband loss](../../../hardware/sim/tx-lpf/results/2026-09-28-r13-wc-1812sms-bom-2pct/il_wc_passband.png)

![r13 harmonic bands](../../../hardware/sim/tx-lpf/results/2026-09-28-r13-wc-1812sms-bom-2pct/harmonic_bands_wc.png)

![r13 distributions](../../../hardware/sim/tx-lpf/results/2026-09-28-r13-wc-1812sms-bom-2pct/mc_wc_histograms.png)

![r14 S21, 2 % parts, 22/68/36/82](../../../hardware/sim/tx-lpf/results/2026-09-28-r14-wc-1812sms-22-36-2pct/s21_wc_wide.png)

![r14 passband loss](../../../hardware/sim/tx-lpf/results/2026-09-28-r14-wc-1812sms-22-36-2pct/il_wc_passband.png)

![r14 harmonic bands](../../../hardware/sim/tx-lpf/results/2026-09-28-r14-wc-1812sms-22-36-2pct/harmonic_bands_wc.png)

![r14 distributions](../../../hardware/sim/tx-lpf/results/2026-09-28-r14-wc-1812sms-22-36-2pct/mc_wc_histograms.png)

### 4.3 Trap variant, screened and rejected (run r16)

Trap capacitors across the outer coils give the lowest loss of any set screened (worst case 0.67 dB, MC median 0.27 dB) but fail REQ-TX-011 badly at the worst case: **9.9 dB from 576 MHz to 1.5 GHz** (MC worst 36.6 dB), and 2f 40.0 dB. Above the shunt capacitors' self-resonance (their ESL and via L) the shunt arms turn inductive while the trap capacitors bypass the coils, so the ladder passes the 7f to 10f region at some corners. This answers TS-012's "trap fitted on the LPF footprint" lever for this topology: a trap across a series coil is not a fix without a stopband re-check up to 1.5 GHz.

![r16 S21, trap variant](../../../hardware/sim/tx-lpf/results/2026-09-28-r16-wc-1812sms-trap-screen/s21_wc_wide.png)

### 4.4 Harmonic budget per finalist (run r15)

Needed A(nf) - IL(f) for the 60 dBc target at 5 W: A5 43 dB at 2f and 35 dB at 3f and above (binding at 8.4 V with the back-off convention; 35 and 30 dB at 6.4 and 7.2 V); A4 45 and 40 dB at every pack voltage. For 97.307(e) the binding case is 2f at the 5 W step: A5 37 dB (8.4 V), A4 39 dB.

| Finalist | Filter build | 97.307(e), every step and pack voltage: min margin (dB) | Ramp min margin (dB) | 60 dBc at 6.4 / 7.2 / 8.4 V: margin (dB) | 60 dBc verdict | MC worst: 97.307(e) / 60 dBc (dB) |
|---|---|---|---|---|---|---|
| A5 | 1812SMS J, BOM | PASS 7.5 | 7.5 | +9.5 / +9.5 / +1.5 | PASS | 14.9 / +8.9 |
| A5 | Air as wound, BOM | PASS 2.3 | 2.3 | +4.3 / +4.3 / -3.7 | FAIL | 10.3 / +4.3 |
| A5 | Air aligned, BOM | PASS 4.3 | 4.3 | +6.3 / +6.3 / -1.7 | FAIL | 11.3 / +5.3 |
| A5 | 1812SMS J, retuned | PASS 0.9 | 0.9 | +2.9 / +2.9 / -5.1 | FAIL | 7.4 / +1.4 |
| A5 | Air aligned, retuned | **FAIL -1.8** | -1.8 | +0.2 / +0.2 / -7.8 | FAIL | 4.6 / -1.4 |
| A5 | 1812SMS G, C0G G, BOM | PASS 9.5 | 9.5 | +11.5 / +11.5 / +3.5 | PASS | 14.8 / +8.8 |
| A5 | 1812SMS G, C0G G, 22/68/36/82 | PASS 8.0 | 8.0 | +10.0 / +10.0 / +2.0 | PASS | 13.4 / +7.4 |
| A4 | 1812SMS J, BOM | PASS 5.5 | 5.5 | -0.5 / -0.5 / -0.5 | FAIL | 12.9 / +6.9 |
| A4 | Air as wound, BOM | PASS 0.3 | 0.3 | -5.7 at each | FAIL | 8.3 / +2.3 |
| A4 | Air aligned, BOM | PASS 2.3 | 2.3 | -3.7 at each | FAIL | 9.3 / +3.3 |
| A4 | 1812SMS J, retuned | **FAIL -1.1** | -1.1 | -7.1 at each | FAIL | 5.4 / -0.6 |
| A4 | Air aligned, retuned | **FAIL -3.8** | -3.8 | -9.8 at each | FAIL | 2.6 / -3.4 |
| A4 | 1812SMS G, C0G G, BOM | PASS 7.5 | 7.5 | +1.5 at each | PASS | 12.8 / +6.8 |
| A4 | 1812SMS G, C0G G, 22/68/36/82 | PASS 6.0 | 6.0 | -0.03 at each | FAIL | 11.4 / +5.4 |

The limiting order is 2f in every case: A5 at the 5 W step at 8.4 V (back-off convention), A4 at the 5 W step. The 7f harmonic (1008 to 1036 MHz, aeronautical radionavigation, HZ-008) has A(7f) - IL(f) of at least 70.9 dB at the worst case of every 7-pole build, so at 6.3 W the 7f harmonic is at most -52.9 dBm for A4 and -57.9 dBm for A5, at least 36.9 and 41.9 dB inside 25 uW.

![Harmonic budget per finalist](../../../hardware/sim/tx-lpf/results/2026-09-28-r15-harmonic-budget-rev2/harmonic_budget.png)

![Harmonic margins per build and pack voltage](../../../hardware/sim/tx-lpf/results/2026-09-28-r15-harmonic-budget-rev2/harmonic_margins.png)

### 4.5 Consequence for the A5 power budget (REQ-SYS-012 at the 6.4 V pack end)

TS-012 section 7.3 gives 4.46 to 5.13 W at the module and subtracts 0.4 dB of LPF and 0.1 dB of relay loss: 3.97 to 4.57 W at the SMA against the 3.97 W floor (0.0 to 0.6 dB margin). With the loss found here (same module figures and relay loss):

| Filter build | LPF loss used: MC median / MC worst / worst case (dB) | Margin to 3.97 W with the MC median (dB) | with the MC worst (dB) | with the worst case (dB) |
|---|---|---|---|---|
| TS-012 assumption | 0.40 | 0.0 to +0.6 | | |
| 1812SMS J, BOM | 0.77 / 1.16 / 2.82 | -0.36 to +0.24 | -0.75 to -0.14 | **-2.41 to -1.80** |
| 1812SMS J, retuned | 0.53 / 0.68 / 1.39 | -0.13 to +0.48 | -0.28 to +0.33 | **-0.99 to -0.38** |
| Air aligned, retuned | 0.45 / 0.67 / 1.56 | -0.04 to +0.57 | -0.27 to +0.34 | -1.16 to -0.55 |
| 1812SMS G, C0G G, BOM | 0.74 / 1.00 / 1.76 | -0.33 to +0.27 | -0.60 to +0.01 | **-1.36 to -0.75** |
| 1812SMS G, C0G G, 22/68/36/82 | 0.65 / 0.82 / 1.24 | -0.24 to +0.37 | -0.41 to +0.19 | -0.84 to -0.23 |

Revision 1 put A5's margin at about -0.3 to +0.5 dB with the retuned filter; the review found -0.49 to +0.11 dB at the extreme corners it tried; at the searched worst case it is -0.99 to -0.38 dB for that filter, and -1.36 to -0.75 dB for the build section 7 recommends. The 4.46 to 5.13 W module range is itself a nominal range (`pa-drive-ts012.md` section 4.4), so these margins are not bounds either. A4 already misses REQ-SYS-012 at 6.4 V (about 3.2 W, TS-012 section 7.1), and the higher-attenuation BOM values it needs lose 0.4 to 2.4 dB more than the 0.4 dB TS-012 allows for the filter.

![A5 power margin at 6.4 V per filter build](../../../hardware/sim/tx-lpf/results/2026-09-28-r15-harmonic-budget-rev2/a5_power_margin_6v4.png)

## 5. Verdicts per finalist

**Filter criteria (WP-PDR-21), common to both finalists.** Passband loss 0.5 dB: **FAIL** in every build at the worst case. REQ-TX-009 at the worst case: **PASS** with catalog coils and the BOM values (45.1 dB at J, 47.1 dB at G), **FAIL** with the retuned values (38.3 dB) and with as-wound air coils (39.7 dB). REQ-TX-010 and REQ-TX-011: **PASS** in every 7-pole build.

**A5 (RA07M1317M module, TCXO).**
- 97.307(e): **PASS** at every step, pack voltage and ramp instant with the catalog-coil builds (worst-case margin 7.5 dB J, 9.5 dB G with the BOM values; 0.9 dB with the retuned values). It binds at the 5 W step at 8.4 V, where the ratio is the back-off estimate.
- 60 dBc target at 5 W (REQ-SYS-018): **PASS with the BOM values** (+1.5 dB J, +3.5 dB G at 8.4 V; +9.5 and +11.5 dB at 6.4 and 7.2 V), **FAIL with the retuned values** (-5.1 dB at 8.4 V). Revision 1's "PASS on guaranteed maxima" was wrong: the binding case is the 8.4 V back-off state, which the guarantee does not cover, and the verdict there rests on the -17 dBc estimate.
- REQ-SYS-012 at 6.4 V: the recommended filter (section 7 item 1) takes -0.33 to +0.27 dB at its median loss and -1.36 to -0.75 dB at its worst-case loss (section 4.5).

**A4 (AFT05MS004N, hand-derived match, no TCXO).**
- 97.307(e): **PASS on an assumption** with the BOM values (5.5 dB J, 7.5 dB G), **FAIL** with the retuned values (-1.1 dB), under 2fo -15 dBc and 3fo -20 dBc, which no vendor data supports or bounds.
- 60 dBc target at 5 W: **FAIL with J parts** (-0.5 dB), **PASS with 2 % parts** (+1.5 dB), both on the assumption.
- Its harmonic margin cannot be confirmed until the first article is measured on the tinySA, which the owner will buy later.

**Discriminator.** On the legal limit the filter does not separate the finalists: both pass with the BOM values and catalog coils, and both fail with the retuned values. With the worst case and the pack-voltage cases the evidence gap narrows: A5's binding case (8.4 V, 5 W) now also rests on an estimate, the back-off ratio, while at 6.4 and 7.2 V it rests on the datasheet maxima with 9.5 to 11.5 dB of margin. A4 rests on the F17 assumption in every state, with smaller margins (-0.5 to +1.5 dB on the 60 dBc target). This still supports the C5 scores of TS-012 (A5 5, A4 2) and the A4 harmonic Red (16) of section 7.1; it moves no score. It adds a filter-loss term to A5's REQ-SYS-012 risk (section 4.5).

## 6. Limitations

1. **The worst case is a search result, not a proof.** In every build the reported worst value is reached from at least three of the nine starts (for the retuned 1812SMS loss, 1.39 dB, from three; the nominal and sensitivity starts stop at 1.33 dB), other starts stop at local worsts up to 3.2 dB lower (r9 loss), and in r8 to r14 every corner puts all 39 parameters at a bound. A worse corner is not excluded.
2. **The parameter box treats every part as independent** and every estimated range (ESR, ESL, via L, pad C, K, leakage) as a hard bound. That is conservative where parts are correlated and not conservative if a real value lies outside an estimated range.
3. **Capacitor ESR is an estimate** and carries 0.28 dB of the 0.70 dB nominal loss; every worst-case loss corner takes ESR 0.4 ohm on all four capacitors. KEMET's K-SIM data for the part numbers were not read.
4. **The Coilcraft SPICE and S-parameter models were not used.** Reading them needs a file download, which this task excludes. The coils are modelled from the datasheet table (Q at 150 MHz as a fixed series R, SRF as a parallel C). A fixed R gives a Q that rises with frequency, and near the SRF the lumped model is approximate.
5. **Air-coil Q, self-capacitance, tolerance and coupling are estimates** (Medhurst proximity factor, lumped self-capacitance). Wire lengths are 81 to 95 mm, so above about 1 GHz the coils behave partly as transmission lines, which the lumped model does not capture.
6. **Stopband floor above about 600 MHz is set by assumed layout terms** (input-to-output leakage 0.5 to 5 fF, coil coupling). Real board leakage, ground-return current paths and radiation from the coax and SMA are not modelled. The NanoVNA bench cases TC-TX-009 to 011 close this, within the NanoVNA floor of about 70 dB.
7. **Terminations are 50 ohm.** The PA's output impedance and the antenna's impedance at the harmonics are not 50 ohm, so the attenuation in service differs from S21 (REQ-TX-012 covers the mismatched load separately).
8. **The PA harmonic levels are estimates** except A5's full state at its guarantee point: the A5 back-off ratio (which now binds A5's verdicts at 8.4 V), A5 at 5 W at 6.4 V, A5 4f and above, and every A4 value. For A4 in particular, a raw 2fo worse than -15 dBc at 5 W cuts the margins one for one.
9. **Not modelled:** the relay contact (G5V-2) and the 40 dB monitor tap at the output (a 5 kohm-class tap loads 50 ohm by about 0.04 dB); temperature (C0G and air-core TCL are small); power handling (1812SMS Irms 2.5 A for 82 nH against about 0.36 A rms at 6.3 W in 50 ohm, more inside the ladder near the band edge; C0G 100 V rating against about 25 V peak at 6.3 W; neither is limiting).
10. **The 0.5 dB loss goal counts mismatch.** The dissipative part alone is lower (MC median 0.49 dB retuned, 0.72 dB BOM for 1812SMS).

## 7. What closes before the order

1. **Filter values (lead SE proposal, owner decision with the TS-012 choice).** Keep the BOM values 22/68/39/82 for either finalist; **revision 1's retune to 18/33 pF is withdrawn** (it fails REQ-TX-009 at the worst case and the 60 dBc target for both finalists). Order the 2 % grades: Coilcraft 1812SMS-68NG and -82NG and the G (2 %) tolerance code of the same KEMET C0G series for the 22 and 39 pF. This is the only build analysed that meets REQ-TX-009 and the 60 dBc target at the worst case for both finalists (A5 +3.5 dB at 8.4 V, A4 +1.5 dB) and it cuts the worst-case loss from 2.82 to 1.76 dB. The G part numbers, prices and stock are read at the ordering gate. If the 2 % parts are not available, the J (5 %) BOM build still passes 97.307(e) for both finalists and the 60 dBc target for A5 (+1.5 dB), and misses it for A4 by 0.5 dB.
2. **Passband-loss criterion (owner decision, TBR).** No build of this topology meets 0.5 dB at the worst case, or at the Monte Carlo median; revision 1's 0.75 dB proposal is withdrawn because no build meets it at the worst case either. The proposal: keep 0.5 dB as the design goal, not a pass criterion; carry the worst-case loss (1.76 dB for the recommended build) as the bound in the A5 REQ-SYS-012 budget and the TS-012 risk row, with the median (0.74 dB) as the expected value; measure the loss on every unit with the NanoVNA (TC-TX-009 to 011, at 144, 146 and 148 MHz) and enter the measured value in the REQ-SYS-012 check. The resulting A5 margin at 6.4 V is -0.33 to +0.27 dB at the median loss and -1.36 to -0.75 dB at the worst-case loss (section 4.5), on top of the drive and module findings of `pa-drive-ts012.md`. Levers that reduce the loss need a price read and a rerun: capacitors with a published ESR below 0.2 ohm at 146 MHz (item 3); the 22/68/36/82 set at 2 % (r14: worst case 1.24 dB, but the A4 60 dBc margin drops to -0.03 dB).
3. **Read the capacitor ESR.** Read the KEMET K-SIM ESR at 146 MHz for the chosen values, or pick a part whose datasheet gives ESR, and rerun r13 with the read range (`lpf_model.CAP_ESR`).
4. **REQ-TX-009, 010, 011 TBR values (review finding-2).** Revision 1's "keep 40, 35 and 40 dB" is withdrawn: it held only for A5 on the datasheet state. What each finalist needs for the 60 dBc target, as A(nf) - IL(f) at the filter:

   | Finalist | 2f (REQ-TX-009) | 3f (REQ-TX-010) | 4f to 10f (REQ-TX-011) | Basis |
   |---|---|---|---|---|
   | A4 | 45 dB | 40 dB | 40 dB | F17 assumption, every pack voltage |
   | A5 | 43 dB | 35 dB | 35 dB (REQ-SYS-018 keeps 40 dB as the self-resonance guard) | back-off convention at 8.4 V; 35, 30, 30 dB at 6.4 and 7.2 V |

   Proposal: set REQ-TX-009, 010 and 011 to the values of the chosen finalist (A4: 45, 40, 40 dB; A5: 43, 35, 40 dB), and state them as attenuation at the harmonic less the passband loss at the carrier, so that the filter loss is not counted twice (review finding-4). The recommended build meets both rows at the worst case (46.5, 69.9 and 60.9 dB).
5. **Layout rules for the RF board (inputs to the layout, checked at CDR):** two ground vias per shunt capacitor at its pad (kept: it lowers the loss and raises the 576 MHz to 1.5 GHz attenuation by about 15 dB, but it is the lowest-2f corner, about 5.5 dB below one via at 1.6 mm, and the worst-case 2f figures include it); a solid bottom ground pour under the filter; filter input and output at opposite ends with at least 20 mm between the end pads; adjacent coils at least 8 mm apart or at right angles (the coupling sign is free, section 3); no trap capacitor across a series coil without a stopband rerun to 1.5 GHz (section 4.3).
6. **Unchanged, after the order:** NanoVNA S21 on every unit (TC-TX-009 to 011, plus the passband loss at 144, 146 and 148 MHz). The tinySA sweep before first on-air use (TS-012 section 7.3), at each step and at 6.4 and 8.4 V, is the only closure for A4's harmonic assumption and for A5's back-off ratio at 8.4 V; it waits for the tinySA purchase the owner has deferred.

## 8. References

- TS-012 revision 4, `docs/decisions/trade-studies/TS-012-design-to-cost-hand-built.md` (commit `7d0d450`), sections 1, 7.1, 7.3, 8 and 8.3.
- INSP-110, `docs/reviews/PDR/checklists/ts-012-design-to-cost.md`; adversarial C8 (LPF ideal attenuation) and the RF feasibility table in TS-012 section 9.
- `docs/design/analysis/pa-drive-ts012.md` section 4.4 (A5 output at 6.4 and 8.4 V).
- 47 CFR 97.307, `docs/references/md/regulatory/47cfr-97.307.md` (eCFR issue 2026-09-23).
- REQ-SYS-011, 012, 017, 018 (`docs/requirements/sys/requirements.md`); REQ-TX-007, 008, 009, 010, 011 (`docs/requirements/tx/requirements.md`).
- `docs/research/pa-device-candidates.md` F4, F8, F16, F17, F18.
- Coilcraft Document 184-1 and 184-2 (Midi Spring 1812SMS), revised 12/02/21, https://www.coilcraft.com/getmedia/c6fe1f83-b176-469d-a071-e2edb068fef2/midi.pdf, read 2026-09-28.
- NXP (Freescale) AFT05MS004N data sheet Rev. 0, 7/2014, https://www.nxp.com/docs/en/data-sheet/AFT05MS004N.pdf, read 2026-09-28.
- G. L. Matthaei, L. Young, E. M. T. Jones, Microwave Filters, Impedance-Matching Networks, and Coupling Structures, eq. 4.05-2 (Chebyshev prototype).

## 9. Disposition of the review findings on revision 1

| Finding | Fix in revision 2 |
|---|---|
| finding-1 (Major): Monte Carlo maximum reported as the worst case; independent draws; corners move L and C only; K only positive | Corner search over the whole box, run in LTspice, is the worst case (section 2 items 3 and 4, section 4.2); K signed (section 3); the 0.75 dB proposal and the retune withdrawn (section 7 items 1 and 2); REQ-TX-009 and REQ-SYS-012 margins restated (sections 4.2, 4.5); the two-via rule stated as the lowest-2f corner (section 4.2, section 7 item 5) |
| finding-2 (Major): "keep 40 and 35 dB" not supported for A4 | Allocation per finalist from the budget (section 7 item 4) |
| finding-3 (Major): 6.4 and 8.4 V cases missing; A5 5 W at 8.4 V is a back-off state | Pack voltage in the budget with the PA state per voltage (section 2 item 8, section 4.4); A5's 60 dBc verdict restated (section 5) |
| finding-4 (Minor): passband loss left out of the spur formula | A(nf) - IL(f) of the same instance in every budget (section 2 item 6) |
| finding-5 (Minor): `run_lpf.py` always exits 0 | Exit status 0, 1 or 2 (header table; `README.md`) |

## Change log

| Revision | Date | Change |
|---|---|---|
| 1 | 2026-09-28 | First issue: runs r1 to r7 |
| 2 | 2026-09-28 | Review of revision 1, findings 1 to 5 (section 9): corner-search worst case with signed coupling (runs r8 to r14), trap screen (r16), budget with A(nf) - IL(f) and the 6.4, 7.2 and 8.4 V cases (r15), exit status; retune and 0.75 dB proposal withdrawn; recommendation changed to the BOM values with 2 % parts |
