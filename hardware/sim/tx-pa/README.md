# hardware/sim/tx-pa: PA drive window and output power (TS-012, WP-PDR-21 pre-order item)

Block owner: Claude (analysis author). Analysis record: `docs/design/analysis/pa-drive-ts012.md`.
Question: for each TS-012 finalist (A4: AFT05MS004N with a hand match, no TCXO; A5: RA07M1317M module with TCXO),
what drive reaches the PA across tolerances and the CLK1-to-RF-board coax, what load the chain puts on the Si5351
CLK1 pin, whether the RA07M1317M input window of 10 to 30 mW is kept (and with what margin to its 30 mW rating), and
what power reaches the SMA from 6.4 to 8.4 V pack against REQ-SYS-012 (5 W +/-1 dB, 3.97 to 6.30 W) at 25 C and over
REQ-SYS-114's -10 to +45 C. Current revision of the record: 2 (2026-09-28).

## Files

| File | What it is |
|---|---|
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
