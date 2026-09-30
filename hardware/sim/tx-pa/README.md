# hardware/sim/tx-pa: PA drive window and output power (TS-012, WP-PDR-21 pre-order item)

Block owner: Claude (analysis author). Analysis record: `docs/design/analysis/pa-drive-ts012.md`.
Question: for each TS-012 finalist (A4: AFT05MS004N with a hand match, no TCXO; A5: RA07M1317M module with TCXO),
what drive reaches the PA across tolerances and the CLK1-to-RF-board coax, what load the chain puts on the Si5351
CLK1 pin, whether the RA07M1317M input window of 10 to 30 mW is kept (and with what margin to its 30 mW rating), and
what power reaches the SMA from 6.4 to 8.4 V pack against REQ-SYS-012 (5 W +/-1 dB, 3.97 to 6.30 W) at 25 C and over
REQ-SYS-114's -10 to +45 C. Current revision of the record: 4 (2026-09-29; A5 only: the two Major findings of the revision 3 review).

## Files

| File | What it is |
|---|---|
| `run_a5_r4.py` | Revision 4 (A5 only, the two Major findings of the revision 3 review): runs r4-s2, r4-p4, r4-p5, r4-s4, r4-s3 (below). Imports `run_a5_r3.py` and `run_pa.py`; LTspice only through `tools/ltspice-batch.sh`; `raw.sha256` for every `.raw` over 5,000,000 bytes (CR-017). `run_a5_r4.py all --expect` reproduces and checks every revision 4 verdict |
| `run_a5_r3.py` | Revision 3 (A5 only): runs d6, d7, k1, s2, p4, p5, s3 (below). Imports the helpers, inputs and GVA-84+ model of `run_pa.py`; LTspice only through `tools/ltspice-batch.sh`; writes `raw.sha256` for every `.raw` over 5,000,000 bytes (CR-017). `run_a5_r3.py all --expect` reproduces and checks every revision 3 verdict |
| `run_pa.py` | Deck writer, LTspice runner (only through `tools/ltspice-batch.sh`, ACC-LTSPICE-001), `.raw` reader (spicelib 1.6.3), checker and plotter. `run_pa.py all` reproduces every current run below; exit status in the section below |
| `digitize_ra07.py`, `digitize_aft05.py` | Graph readers for the datasheet curves (render at 400 dpi with pdftoppm, locate the grid, track the curve); they write `data/*.csv` and an overlay PNG per curve (red or blue marks on the datasheet crop) for visual closure |
| `data/` | Digitized curves: RA07M1317M Pout versus Pin (7.2 V, VGG 3.5 V), Pout versus VDD (Pin 20 mW, VGG 3.5 V) and Pout versus VGG (7.2 V, Pin 20 mW), each at 135 and 155 MHz; AFT05MS004N Pout versus Pin at 7.5 V in the NXP 136 to 174 MHz reference circuit (Figure 13, 135 and 155 MHz). All typical data, graph reads (estimates) |
| `decks/` | The current LTspice decks as run (copies of the ones in `results/`): the drive decks of revision 1 (`drive_a5_pinpad.cir` is d5's `drive_a5.cir`), the power decks of revision 2 (`power_a5_sot.cir` is p3's `power_a5.cir`), plus `gva_check.cir` of d1 |
| `results/<run-id>/` | Per run: the deck, the LTspice `.log` and `.raw` (kept in git by the `.gitignore` exception), `result.json` and `result.md` (numbers and pass/fail), PNG plots with the limits drawn, and a copy of `run_pa.py` |

Datasheets read (public vendor PDFs fetched 2026-09-28 through the web-fetch tool, cached outside the repository, not
committed; SHA-256 of the files read):
- Mitsubishi RA07M1317M, publication date Jun. 2019: https://www.mitsubishielectric.com/semiconductors/hf/products/datasheet/ra07m1317m.pdf (`5a847a09c011c164...`)
- NXP AFT05MS004N Rev. 0, 7/2014: https://www.nxp.com/docs/en/data-sheet/AFT05MS004N.pdf (`84cd9fae494c6283...`)
- Mini-Circuits GVA-84+ Rev. F: https://www.minicircuits.com/pdfs/GVA-84+.pdf (`49daf1cbb9681715...`)
- Skyworks Si5351A/B/C-B Rev. 1.3: https://www.skyworksinc.com/-/media/Skyworks/SL/documents/public/data-sheets/Si5351-B.pdf (`f3bc5285fccafa3f...`): Table 7 (load capacitance at most 15 pF; edge, duty at TA -40 to 85 C) and section 7.6 Figure 16 (50 ohm trace) read again for revision 1
- Molicel INR-18650-P28A data sheet (INR18650P28A-V1-80093): https://www.molicel.com/wp-content/uploads/INR18650P28A-V1-80093.pdf (`05db826b40db2106...`): DC IR 20 mohm; discharge-temperature curves (graph read)
- Adafruit product page 2045 (Si5351A breakout), read 2026-09-28: https://www.adafruit.com/product/2045 (outputs on a header or "an optional SMA connector")
- Revision 3, read 2026-09-29 through the web-fetch tool (cached outside the repository, not committed):
  - Diodes Inc. DMP3099L, DS36081 Rev. 5-2, May 2025: https://www.diodes.com/assets/Datasheets/DMP3099L.pdf (`06f3030318ba16b2...`): RDS(on) maxima, Figs. 3 and 5
  - Alpha and Omega AO3400A Rev 3.1, July 2023: https://www.aosmd.com/res/datasheets/AO3400A.pdf (`9c60d0b6c1ddc760...`): RDS(on) maxima, Figs. 3 and 4
  - Bourns MF-R series REV. AR 09/26: https://www.bourns.com/docs/Product-Datasheets/mfr.pdf (`d22f0f06c8909784...`): MF-R300 Rmin, Rmax, R1max, thermal derating table
  - Coilcraft Document 184-1, Midi Spring 1812SMS: https://www.coilcraft.com/getmedia/c6fe1f83-b176-469d-a071-e2edb068fef2/midi.pdf (`e8ce1b27f9bea463...`): values, tolerance codes, Q, SRF, TCL

To reproduce the digitized data: `.venv/bin/python hardware/sim/tx-pa/digitize_ra07.py <ra07m1317m.pdf> hardware/sim/tx-pa/data`
and the same for `digitize_aft05.py`. To reproduce every revision 1 result: `.venv/bin/python hardware/sim/tx-pa/run_pa.py all`
(d2 to s1; about 5 minutes of LTspice when no other run holds the lock; set `CWHT_LTSPICE_LOCK_WAIT` if one does).
`run_pa.py d1` reruns the unchanged GVA-84+ model check.

## Exit status and verdict check (revision 2, review finding-5)

`run_pa.py` prints every verdict it records and exits **0** when every criterion is met and every check passes,
**1** when every check passes and at least one criterion fails (the results are valid and report the failure), and
**2** when a check fails (one `.raw` step per corner, the time-step check, the GVA-84+ model check, the PA case
temperature against the thermal law: the results must not be used). With `--expect` it compares every verdict with the
list in `EXPECTED` (the list of the analysis record section 8.1) and exits **3** if any differs, **0** if none does.
`run_pa.py all` writes every verdict to `results/2026-09-28-r2-s1-summary/verdicts.json`. On 2026-09-28
`run_pa.py all` exits 1 (checks pass; the fixed-pad drive window, REQ-SYS-012 at the 6.4 V end and the open-loop
8 W limit fail, as the record reports) and `run_pa.py all --expect` exits 0.

## Runs, revision 4 (2026-09-29, A5 only: review of revision 3, Major findings 1 and 2)

LTspice 26.0.2 for MacOS through the wrapper; every run exit 0. All values are estimates. The d6, d7 and k1 runs of
revision 3 are the inputs, unchanged. `run_a5_r4.py all` exits 1 (every check passes; criteria fail as the record
section R4.10 lists) and `run_a5_r4.py all --expect` exits 0. The final outputs were written by
`CWHT_PA_REPLOT=1 run_a5_r4.py all --expect`, which re-read each `.raw` of an unchanged deck; the copies of
`run_a5_r4.py`, `run_a5_r3.py` and `run_pa.py` in every revision 4 folder equal the committed scripts. The power
decks carry the per-unit clamp in closed form (record section R4.4); the output loss is applied by the checker to
`V(pmod)`, so each deck has 13608 steps for 54432 corners.

| Run id | Deck (SHA-256 prefix) | What it does | Result |
|---|---|---|---|
| `2026-09-29-r4-s2-sot-pad` | none (post-processing of r3-d6, -d7, -k1) | Select-on-test band with one-sided in-unit terms from the 146 MHz value (finding-1); target re-centred | +0.36 / -0.78 dB from 146 MHz; target 18.2 mW; 10.99 to 27.37 mW with the M2 reading, 10.12 to 29.74 mW at +/-1.0 dB: **PASS**; 17.3 mW at +/-1.0 dB 9.62 mW: **FAIL**. Plot `sot_band_r4.png` |
| `2026-09-29-r4-p4-power-a5-design` | `power_a5_step.cir` (`ff6f622f66d4ce5a`) | Power path with the D-9 8 W ceiling as a per-unit build step (step target 6.29 W; 7 unit cases: typical, +1.5 dB, datasheet minimum, each read at the bound) | Open loop at most 7.74 W: **PASS**. Step basis (LPF MC 99 %) 1.06 W at 6.4 V and 0.58 W at 8.4 V. Plots `power_a5_step_d9_sma.png`, `power_a5_step_d9_temperature.png`; `.raw` kept (15.6 MB) |
| `2026-09-29-r4-p5-power-a5-clamp-b` | `power_a5_step.cir` (`ff44551d88286654`) | The same with clamp scenario B (10 W ceiling, 0.03 V window; step target 7.89 W) | Open loop at most 9.65 W: **PASS**. Step basis 2.82 W at 6.4 V and 3.09 W at 8.4 V. Plots `power_a5_step_clampb_sma.png`, `power_a5_step_clampb_temperature.png`; `.raw` kept (15.6 MB) |
| `2026-09-29-r4-s4-clamp-step` | none (Python replica of the deck model, checked against r4-p4 and r4-p5) | Fixed clamp against the module's upper spread; the step's terms; the step over the module spread; the reading break-even | Revision 3 clamp at +0.3 dB: 10.51 W (**FAIL**); step terms g- 0.99 dB, g+ 0.89 dB; reach at 8.4 V needs the reading within about 2 %. Plot `clamp_step.png` |
| `2026-09-29-r4-s3-req012-basis` | none (post-processing of r4-p4 and r4-p5) | REQ-SYS-012 basis with the step; the delta; `verdicts.json` of every revision 4 run | Scenario B: 5 W +1/-2.7 dB at 6.4 V, -2.3 dB from 6.7 V; D-9 with the step: no delta of the form. Plot `req012_basis_r4.png` |

Every revision 4 PNG was opened and inspected after rendering (visual closure, 2026-09-29).

## Runs, revision 3 (2026-09-29, A5 only: WP-PDR-21 in wave W-A of the PDR work plan revision 6)

LTspice 26.0.2 for MacOS through the wrapper; every run exit 0. All values are estimates. `run_a5_r3.py all` exits 1
(every check passes; criteria fail as the record section R3.10 lists) and `run_a5_r3.py all --expect` exits 0. The
final outputs were written by `CWHT_PA_REPLOT=1 run_a5_r3.py all --expect`, which re-read each `.raw` of an
unchanged deck; the copies of `run_a5_r3.py` and `run_pa.py` in every revision 3 folder equal the committed scripts.
Every `.raw` over 5,000,000 bytes stays in its folder on the owner's Mac and is named in the folder's `raw.sha256`
(CR-017); `shasum -a 256 -c raw.sha256` in the folder checks it.

| Run id | Deck (SHA-256 prefix) | What it does | Result |
|---|---|---|---|
| `2026-09-29-r3-d6-drive-a5-bpf` | `drive_a5_bpf.cir` (`b527e31c4c91cb8b`) | A5 drive chain with the D-13 drive bandpass (1812SMS-47NG, Q 100 and 135; 16 pF at 2 %, 7.5 and 2.4 pF at +/-0.1 pF; five tolerance cases) and the fixed 18 dB pad; 8100 corners; 250 ns transient | Fixed pad **FAIL**: 5.5 to 39.1 mW, nominal 12.5 mW. Pin load -0.5 to 11.0 pF (inside 15 pF). 3f -33.8 dBc. CLK1 swing 1.33 to 3.40 Vpp. Plot `drive_a5_bpf_corners.png`; `.raw` kept (230.9 MB) |
| `2026-09-29-r3-d7-coax-bound-bpf` | `coax_a5_bpf.cir` (`2856d8655a59446f`), `tstep_a5_bpf.cir` (`d9b25ae0f2bc4fd6`) | Bandpass chain over every coax length (0.5 to 70 cm, extreme part corners, Q 100 and 135); 15 corners at 10 ps and 400 ns against d6 | 6.0 to 38.7 mW at any length; pad need 13.90 to 21.92 dB. Numerical check 0.0028 dB: **PASS**. Plot `coax_length_bound_bpf.png`; `coax_a5_bpf.raw` kept (24.8 MB) |
| `2026-09-29-r3-k1-probe-17mw` | `probe_rf.cir` (`0fead6babdbc07b1`), `probe_dc.cir` (`a1b94e911c3a6528`) | The select-on-test level reading: diode probe periodic steady state (9360 steps: 8 diode sets, 10 / 17.3 / 30 mW, harmonic cases, both polarities, hold-voltage grid) and the DC forward drop at 20, 25, 30 C | Reading bound +/-0.64 dB (method M2) against the +/-1.0 dB allocation: **PASS**; revision 2's DC-drop-only reading reads 0.42 to 0.73 dB low. Plot `probe_reading_error.png`; `probe_rf.raw` kept (123.6 MB) |
| `2026-09-29-r3-s2-sot-pad` | none (post-processing of d6, d7, k1) | Select-on-test pad set and in-service band on the bandpass chain | 14 pads, 13.48 to 22.04 dB; 11.0 to 27.3 mW, overdrive margin +0.41 dB: **PASS**; tinySA alone -0.95 dB: **FAIL**. Plot `sot_band.png` |
| `2026-09-29-r3-p4-power-a5-design` | `power_a5_design.cir` (`b137d0a486641f14`) | A5 power path with the adopted design: s2 drive band, D-9 clamp (VGG 3.30 to 3.50 V at 6.4 V; top tracking the 8 W open-loop ceiling), D-14 LPF, read feed; 15552 corners | 6.4 V, 25 C key-down: nominal 4.26 W, lowest (typ., LPF median) 3.49 W; worst key-down case 3.44 and 2.90 W. 8.4 V: open loop 7.90 W; lowest (typ., LPF MC 99 %) 2.07 W. Plots `power_a5_design_sma.png`, `power_a5_design_temperature.png`; `.raw` kept (20.4 MB) |
| `2026-09-29-r3-p5-power-a5-clamp-b` | `power_a5_design.cir` (`2d03e7ba368175f4`) | p4 with clamp scenario B (10 W ceiling, 0.03 V window; VGG 3.47 to 3.50 V at 6.4 V) | 6.4 V worst key-down case: nominal 3.48 W, lowest (typ., LPF MC 99 %) 2.82 W; 8.4 V: 4.42 W; open loop at most 9.94 W. Plots `power_a5_clampb_sma.png`, `power_a5_clampb_temperature.png`; `.raw` kept (20.4 MB) |
| `2026-09-29-r3-s3-req012-basis` | none (post-processing of p4 and p5; the clamp trade by the Python replica of the module model, checked against p4) | The REQ-SYS-012 basis for CR-018; the D-9 clamp trade at 8.4 V; `verdicts.json` of every revision 3 run | Scenario B: 5 W +1/-2.7 dB at 6.4 V, -1 dB from 7.8 V; D-9 as specified: no -1 dB reach at any pack voltage. Plot `req012_basis.png` |

Every revision 3 PNG was opened and inspected after rendering (visual closure, 2026-09-29).

## Runs, revision 2 (2026-09-28, iteration 2 of the review: Major finding-9, Minor findings 3 to 8 and 10, cross items X-4 to X-6)

LTspice 26.0.2 for MacOS through the wrapper; every run exit 0, no warning in any log. All values are estimates.
What changed in the model (details in the analysis record sections 2, 3 and 3.1):
- **One thermal state per question (finding-9).** Every low-bound temperature case is steady key-down at its ambient:
  the PA case is solved in the deck (`V(tc)` = ambient + Rth case to ambient x (Pout (1/eta - 1) + Pin); Rth 6.11 K/W
  for A5 and 9.6 K/W for A4 from WP-PDR-28), and the drain-feed parts and the LPF copper term sit at their own
  key-down temperatures. The high-side open-loop case is the start of a key-down from a -10 C soak; a 25 C start of
  key-down row (PA case 25 C, the datasheet condition) is informative. The checker recomputes the thermal law from the
  `.raw` and requires agreement within 0.01 K (7.6e-6 K found).
- **VGG (finding-3):** 3.08 / 3.27 / 3.46 V (the revision-4 clamp: minimum, nominal, maximum) and 3.30 V (the C3
  lever minimum). 3.5 V is no longer used.
- **Output loss (cross item X-5):** 0.5 / 0.84 / 1.86 dB, the TS-012 allocation and the WP-PDR-21 LPF revision 2
  recommended build (run r13 at commit 92e3805: 0.74 dB Monte Carlo median, 1.76 dB worst case) plus the 0.1 dB relay,
  replacing 0.4 / 0.5 / 0.6 dB and the uncertainty term that rested on the withdrawn LPF runs r6 and r7.
- **Select-on-test pad (finding-4):** a set of 14 real E24 pads with adjacent losses at most 0.77 dB apart; the
  step term is half that gap; the level reading is an allocation of +/-1.0 dB with its sensitivity.

| Run id | Deck (SHA-256 prefix) | What it does | Result |
|---|---|---|---|
| `2026-09-28-r2-p1-power-a5` | `power_a5.cir` (`e01cd46d9ddb0f14`) | A5 power path, 11664 corners: feed 3 x efficiency 2 x drive 3 (d2) x frequency 3 x VGG 4 x module spread 2 x output loss 3 x 9 temperature cases | 25 C key-down, 6.4 V: nominal 4.09 W (-0.005 dB/K) and 3.94 W (-0.015 dB/K); lowest with C2 and C3, LPF median, 3.66 and 3.46 W (-0.36 and -0.60 dB): **FAIL**. Over every key-down case the C2 and C3 figure is -0.34 to -1.21 dB (LPF median) and -1.38 to -2.36 dB (LPF worst): **FAIL**. Open loop at 8.4 V: module 9.38 W (25 C key-down), 10.68 W (-10 C start, +0.53 dB): 8 W and 10 W **FAIL**. Plots `power_a5_sma.png`, `power_a5_temperature.png` |
| `2026-09-28-r2-p2-power-a4` | `power_a4.cir` (`0cb13db4b6881b42`) | A4 power path, 13122 corners (d3 drive, n, match loss, same feed, loss and temperature cases) | 25 C key-down, 6.4 V: nominal 3.06 W, lowest 1.69 W (LPF median) and 1.31 W (LPF worst): **FAIL**; the lowest corner stays under 3.97 W up to 8.4 V in every case (worst 1.03 W). Plots `power_a4_sma.png`, `power_a4_temperature.png` |
| `2026-09-28-r2-p3-power-a5-sot` | `power_a5.cir` (`e0557851af3c9c76`) | p1 with the drive band the select-on-test pad leaves (11.3 / 17.3 / 26.5 mW, s1) | 25 C key-down, 6.4 V: C2 and C3, LPF median, 3.81 and 3.59 W (-0.19 and -0.44 dB): **FAIL**; every key-down case -0.17 to -1.03 dB; 25 C start of key-down +0.14 dB. Plots as p1, titled with the select-on-test drive |
| `2026-09-28-r2-s1-summary` | none (post-processing of d2 to p3) | Select-on-test pad set, band, reading sensitivity and overdrive margin; A5 closure margin with the terms not carried as corners, at the LPF median and worst case; both finalists on one page; `verdicts.json` | Select-on-test: 11.3 to 26.5 mW at a +/-1.0 dB reading, overdrive margin +0.54 dB (**PASS**, estimate); break-even reading +/-1.54 dB; with the tinySA Ultra's published +/-2 dB alone -0.46 dB (**FAIL**). Plots `pin_at_pa_vs_pack.png`, `pout_at_sma_vs_pack.png`, `a5_closure_margin.png`, `a5_overdrive_margin.png`, `a5_sot_reading_sensitivity.png` |

The drive runs d2 to d5 keep their revision 1 folders below: their decks did not change. The revision 2 checker
re-read d2, d3 and d5 from their revision 1 `.raw` (`CWHT_PA_REPLOT=1`, same deck SHA-256) and rewrote
`result.json` (a verdict block), the d2 and d5 `result.md` (the verdict sentence, finding-7 item ii) and the script
copy; their numbers and plots are unchanged. d4 was rerun in LTspice with the revision 2 checker (same decks; the
`.log` and `.raw` are new files, the numbers and plot are identical).

Every PNG of revision 2 was opened and inspected after rendering (visual closure, 2026-09-28).

## Runs, revision 1 (2026-09-28, review of the analysis note: Major findings 1 and 2, Minor finding 3)

The drive runs d2 to d5 below are current. The power runs p1 to p3 and the summary s1 of revision 1 are superseded
by revision 2 (finding-9: their 25 C case put the PA case at 25 C; VGG 3.5 V; output loss 0.4 to 0.6 dB).

LTspice 26.0.2 for MacOS through the wrapper; every run exit 0. All values are estimates (graph-read typical
vendor curves and estimated terms; the analysis record classes each input).

| Run id | Deck (SHA-256 prefix) | What it does | Result |
|---|---|---|---|
| `2026-09-28-d1-gva-model` | `gva_check.cir` (`eb121249e9fa0473`) | Unchanged from revision 0. GVA-84+ behavioural model (Rapp limiter on the instantaneous voltage, p 2.70) swept -20 to +4 dBm in at 146 MHz for three P1dB sets | **PASS**: 1 dB points 19.37, 20.37, 21.37 dBm against 19.4, 20.4, 21.4; 3 dB points 20.69, 21.69, 22.69 against 20.7, 21.7, 22.7. Plot `gva_compression.png` |
| `2026-09-28-r1-d2-drive-a5` | `drive_a5.cir` (`5e142606a8284afc`) | A5 chain with the interface as designed (TS-012 section 8.1): Si5351 CLK1 trapezoid source (25 or 50 ohm; VDDO, edge and duty cases), 7 pF lumped on the pin (tap and stub, est.), 50 ohm coax 5 / 10 / 15 cm (VF 0.66, est.) to the RF board, 3-pole drive LPF, 18 dB pad, GVA-84+, 3 dB pad, 50 ohm module input; 810 corners; fundamental, 3f and the pin impedance by DFT | **FAIL** on the 10 to 30 mW window: 5.4 to 35.5 mW, nominal 11.4 mW; 195 of 810 under 10 mW, 28 over 30 mW (1 / 9 / 18 per coax length); overdrive margin -0.73 dB. 3f at most -30.9 dBc: **PASS**. Pin load: lumped 7 pF against the 15 pF of Table 7 (**PASS**); line-fed equivalent 13.6 to 24.7 pF at f (outside what Table 7 covers). Plots `drive_a5_corners.png`, `drive_a5_h3.png`, `drive_a5_pinload.png` |
| `2026-09-28-r1-d3-drive-a4` | `drive_a4.cir` (`070ff766154aab9b`) | A4 chain: same source, interface and LPF, 12 dB pad, GVA-84+ near its P1dB, 50 ohm AFT05 reference-circuit input; 810 corners | 45.8 to 180.0 mW, nominal 89.4 mW; none above the 0.2 W ruggedness-test drive (**PASS**, informative; margin +0.46 dB). 3f -30.9 dBc worst: **PASS**. Plots `drive_a4_corners.png`, `drive_a4_h3.png`, `drive_a4_pinload.png` |
| `2026-09-28-r1-d4-coax-bound` | `coax_a5.cir` (`564ecf0ab0dda83d`), `coax_a4.cir` (`87961cecb6f6e64e`), `tstep_a5.cir` (`85832f6ab1fd011d`), `tstep_a4.cir` (`b12afa63a12b060e`) | The five extreme part corners at 144, 146, 148 MHz over coax lengths 0.5 to 70 cm (every electrical length); and 15 corners rerun at a 10 ps step against the 20 ps of d2 and d3 | A5 5.4 to 48.6 mW over any length (overdrive margin -2.10 dB); A4 45.8 to 195.9 mW (+0.09 dB). Time-step check: largest difference 0.0005 dB: **PASS**. Plot `coax_length_bound.png` |
| `2026-09-28-r1-d5-drive-a5-pinpad` | `drive_a5.cir` (`0629835d89f560b1`) | Design-request option DR-PAD-1 (not the TS-012 design): d2 with a 6 dB pad (150 / 36 / 150 ohm) at the CLK1 end of the coax and a 12 dB pad on the RF board | Pin load 9.6 to 11.9 pF equivalent (under 15 pF at every corner); drive 6.7 to 41.6 mW (spread 7.9 dB, so the select-on-test pad is still needed); 3f -35.4 dBc. Plots as d2 |
| `2026-09-28-r1-p1-power-a5` | `power_a5.cir` (`fa74131e525bafa9`) | A5 power path: pack EMF swept 6.4 to 8.4 V; drain feed 0.26 / 0.35 / 0.45 ohm at 25 C, recomputed per part at -10 C and +45 C; 5 V bus 0.25 A; module current Pout/(eta Vd) so LTspice solves the key-down sag; module from the digitized curves with the d2 drive corners, VGG 3.5 V or 3.08 V, typical or datasheet-minimum module, output loss 0.4 / 0.5 / 0.6 dB; 7 temperature cases (PA factor -0.005 or -0.015 dB/K above 25 C at case 80 or 100 C; cold 0 or +0.53 dB); 4536 corners | 25 C, 6.4 V: nominal 4.85 W, lowest **3.68 W: FAIL** against 3.97 W, lowest with C2 and C3 4.28 W (+0.32 dB). Over -10 to +45 C the lever corner is -0.86 to +0.32 dB: **FAIL** at +45 C. Open loop at 8.4 V: 9.90 W at 25 C, 10.76 W at -10 C (+0.53 dB). Plots `power_a5_sma.png`, `power_a5_temperature.png` |
| `2026-09-28-r1-p2-power-a4` | `power_a4.cir` (`ffbcaa3aa83dd160`) | A4 power path: same feed, bus and temperature cases; AFT05 Pout(Pin) at 7.5 V scaled by (Vd/7.5)^n, n 1.8 / 2.0 / 2.3; hand-match extra loss 0 / 0.25 / 0.5 dB; d3 drive corners; 10206 corners | 25 C, 6.4 V: nominal 3.48 W, lowest **1.90 W: FAIL**; the lowest corner stays under 3.97 W at every pack voltage and temperature (worst 1.42 W at 6.4 V). Plots `power_a4_sma.png`, `power_a4_temperature.png` |
| `2026-09-28-r1-p3-power-a5-sot` | `power_a5.cir` (`7f00281ccfc0b714`) | p1 with the drive range the select-on-test pad leaves (11.0 / 17.3 / 27.2 mW, s1 estimate) | 25 C, 6.4 V: lowest 3.83 W (FAIL); with C2 and C3 4.45 W (+0.49 dB); over -10 to +45 C -0.68 to +0.49 dB. Plots as p1 |
| `2026-09-28-r1-s1-summary` | none (post-processing of d2 to p3) | Select-on-test pad band, pad set and overdrive margin; A5 closure margin at 6.4 V with the terms not carried as corners; both finalists on one page | Select-on-test: 11.0 to 27.2 mW, overdrive margin +0.42 dB worst-case sum, pad set 13 to 22 dB (**PASS**, estimate). Closure margin with C2 and C3 at 25 C: -0.01 to +0.39 (fixed pad), +0.16 to +0.56 (select-on-test) dB with the unmodelled terms. Plots `pin_at_pa_vs_pack.png`, `pout_at_sma_vs_pack.png`, `a5_closure_margin.png`, `a5_overdrive_margin.png` |

Every PNG above was opened and inspected after rendering (visual closure, 2026-09-28), as were the eight digitizer
overlays in `data/`.

## Runs, revision 0 (superseded, kept for history)

`2026-09-28-d2-drive-a5`, `-d3-drive-a4`, `-p1-power-a5`, `-p2-power-a4`, `-p3-power-a5-sot` and `-s1-summary`.
The revision 1 power and summary folders (`2026-09-28-r1-p1` to `-r1-s1`) are also superseded, by revision 2.
They modelled the CLK1 pin with the drive LPF's 18 pF and the 5 pF tap directly on it (23 pF, not the design:
review finding-1) and every power curve at 25 C only (finding-2). Their folders keep their decks, logs, raws,
results and the revision 0 script copy.

## Modelling notes (details and sources in the analysis record)

- The drive chain is a transient model because the Si5351 output is a square wave: its fundamental depends on the
  edge time, and the 3f criterion needs the harmonic. The PA stages are modelled at the power level (volts on a node
  stand for watts) because the datasheets give power curves, not device models.
- The CLK1-to-RF-board coax is an LTspice lossless line (`T` element, Td = length / (0.66 c), Z0 50 ohm). The pin
  load is V(clk)/I(Rsrc) at the fundamental, reported as an equivalent shunt capacitance Im(Y)/(2 pi f).
- The drive and power runs are linked by the drive corners: p1 and p2 read the minimum, nominal and maximum PA input
  of d2 and d3 from their `result.json`; p3 reads the s1 select-on-test band.
- Temperature cases (revision 2): the drain feed per case is computed part by part (`FEED_CELLS`, `FEED_PARTS` in
  `run_pa.py`: each part at the ambient plus its key-down rise, with its temperature coefficient) and scaled so that
  every part at 25 C gives exactly 0.26 / 0.35 / 0.45 ohm; the PA case is solved in the deck (`Btc`, `RTH_CA`); the
  PA coefficient, the no-gain-below-25-C rule and the copper term are `TC_CASES`, `CU_TC`, `BAY_RISE_KD`. Each carries
  its source or "est." in the script.
- `CWHT_PA_REPLOT=1` re-reads an existing `.raw` when the deck is byte-identical (same SHA-256 as recorded in the
  run's `result.json`), to redraw plots and results without a new LTspice run. The revision 2 power `.raw` files come
  from one LTspice run each (p1 at 20:20, p2 at 20:34, p3 at 20:39 on 2026-09-28); the final revision 2 script then
  re-read every run with `CWHT_PA_REPLOT=1` and `--expect`. The copy of `run_pa.py` in every current run folder
  (d2 to d5, p1 to p3, s1) equals the committed script.
