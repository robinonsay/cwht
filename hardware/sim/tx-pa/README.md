# hardware/sim/tx-pa: PA drive window and output power (TS-012, WP-PDR-21 pre-order item)

Block owner: Claude (analysis author). Analysis record: `docs/design/analysis/pa-drive-ts012.md`.
Question: for each TS-012 finalist (A4: AFT05MS004N with a hand match, no TCXO; A5: RA07M1317M module with TCXO),
what drive reaches the PA across tolerances and the CLK1-to-RF-board coax, what load the chain puts on the Si5351
CLK1 pin, whether the RA07M1317M input window of 10 to 30 mW is kept (and with what margin to its 30 mW rating), and
what power reaches the SMA from 6.4 to 8.4 V pack against REQ-SYS-012 (5 W +/-1 dB, 3.97 to 6.30 W) at 25 C and over
REQ-SYS-114's -10 to +45 C.

## Files

| File | What it is |
|---|---|
| `run_pa.py` | Deck writer, LTspice runner (only through `tools/ltspice-batch.sh`, ACC-LTSPICE-001), `.raw` reader (spicelib 1.6.3), checker and plotter. `run_pa.py all` reproduces every run below |
| `digitize_ra07.py`, `digitize_aft05.py` | Graph readers for the datasheet curves (render at 400 dpi with pdftoppm, locate the grid, track the curve); they write `data/*.csv` and an overlay PNG per curve (red or blue marks on the datasheet crop) for visual closure |
| `data/` | Digitized curves: RA07M1317M Pout versus Pin (7.2 V, VGG 3.5 V), Pout versus VDD (Pin 20 mW, VGG 3.5 V) and Pout versus VGG (7.2 V, Pin 20 mW), each at 135 and 155 MHz; AFT05MS004N Pout versus Pin at 7.5 V in the NXP 136 to 174 MHz reference circuit (Figure 13, 135 and 155 MHz). All typical data, graph reads (estimates) |
| `decks/` | The revision 1 LTspice decks as run (copies of the ones in `results/`; `drive_a5_pinpad.cir` is d5's `drive_a5.cir`, `power_a5_sot.cir` is p3's `power_a5.cir`), plus `gva_check.cir` of d1 |
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

## Runs, revision 1 (2026-09-28, review of the analysis note: Major findings 1 and 2, Minor finding 3)

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
- Temperature cases: the drain feed per temperature is computed part by part (`FEED_PARTS` in `run_pa.py`) and
  scaled so that 25 C gives exactly 0.26 / 0.35 / 0.45 ohm; the PA factor and the output-loss copper term are
  `TC_CASES`. Both carry their source or "est." in the script.
- `CWHT_PA_REPLOT=1` re-reads an existing `.raw` when the deck is byte-identical (same SHA-256 as recorded), to redraw
  plots without a new LTspice run. The committed revision 1 `.log` and `.raw` files of d2, d3, d5 and p1 to p3 come
  from one run of `run_pa.py all`; their plots and result files were then redrawn from those raws with the final
  script after a plot-title change (`CWHT_PA_REPLOT=1`), and d4 and s1 were rerun with it. The copy of `run_pa.py`
  in each run folder is that final script.
