# hardware/sim/tx-pa: PA drive window and output power (TS-012, WP-PDR-21 pre-order item)

Block owner: Claude (analysis author). Analysis record: `docs/design/analysis/pa-drive-ts012.md`.
Question: for each TS-012 finalist (A4: AFT05MS004N with a hand match, no TCXO; A5: RA07M1317M module with TCXO),
what drive reaches the PA across tolerances, whether the RA07M1317M input window of 10 to 30 mW is kept, and
what power reaches the SMA from 6.4 to 8.4 V pack against REQ-SYS-012 (5 W +/-1 dB, 3.97 to 6.30 W).

## Files

| File | What it is |
|---|---|
| `run_pa.py` | Deck writer, LTspice runner (only through `tools/ltspice-batch.sh`, ACC-LTSPICE-001), `.raw` reader (spicelib 1.6.3), checker and plotter. `run_pa.py all` reproduces every run below |
| `digitize_ra07.py`, `digitize_aft05.py` | Graph readers for the datasheet curves (render at 400 dpi with pdftoppm, locate the grid, track the curve); they write `data/*.csv` and an overlay PNG per curve (red or blue marks on the datasheet crop) for visual closure |
| `data/` | Digitized curves: RA07M1317M Pout versus Pin (7.2 V, VGG 3.5 V), Pout versus VDD (Pin 20 mW, VGG 3.5 V) and Pout versus VGG (7.2 V, Pin 20 mW), each at 135 and 155 MHz; AFT05MS004N Pout versus Pin at 7.5 V in the NXP 136 to 174 MHz reference circuit (Figure 13, 135 and 155 MHz). All typical data, graph reads (estimates) |
| `decks/` | The six LTspice decks as run (copies of the ones in `results/`) |
| `results/<run-id>/` | Per run: the deck, the LTspice `.log` and `.raw` (kept in git by the `.gitignore` exception), `result.json` and `result.md` (numbers and pass/fail), PNG plots with the limits drawn, and a copy of `run_pa.py` |

Datasheets read (public vendor PDFs fetched 2026-09-28 through the web-fetch tool, cached outside the repository, not
committed; SHA-256 of the files read):
- Mitsubishi RA07M1317M, publication date Jun. 2019: https://www.mitsubishielectric.com/semiconductors/hf/products/datasheet/ra07m1317m.pdf (`5a847a09c011c164...`)
- NXP AFT05MS004N Rev. 0, 7/2014: https://www.nxp.com/docs/en/data-sheet/AFT05MS004N.pdf (`84cd9fae494c6283...`)
- Mini-Circuits GVA-84+ Rev. F: https://www.minicircuits.com/pdfs/GVA-84+.pdf (`49daf1cbb9681715...`)
- Skyworks Si5351A/B/C-B Rev. 1.3: https://www.skyworksinc.com/-/media/Skyworks/SL/documents/public/data-sheets/Si5351-B.pdf (`f3bc5285fccafa3f...`)

To reproduce the digitized data: `.venv/bin/python hardware/sim/tx-pa/digitize_ra07.py <ra07m1317m.pdf> hardware/sim/tx-pa/data`
and the same for `digitize_aft05.py`. To reproduce every result: `.venv/bin/python hardware/sim/tx-pa/run_pa.py all`
(about 3 minutes of LTspice when no other run holds the lock; set `CWHT_LTSPICE_LOCK_WAIT` if one does).

## Runs (2026-09-28, LTspice 26.0.2 for MacOS through the wrapper, every run exit 0 with no warning in its log)

| Run id | Deck (SHA-256 prefix) | What it does | Result |
|---|---|---|---|
| `2026-09-28-d1-gva-model` | `gva_check.cir` (`eb121249e9fa0473`) | GVA-84+ behavioural model (Rapp limiter on the instantaneous voltage, p 2.70) swept -20 to +4 dBm in at 146 MHz for three P1dB sets | **PASS**: 1 dB points 19.37, 20.37, 21.37 dBm against 19.4, 20.4, 21.4; 3 dB points 20.69, 21.69, 22.69 against 20.7, 21.7, 22.7. Plot `gva_compression.png` |
| `2026-09-28-d2-drive-a5` | `drive_a5.cir` (`716d88f42bdf6547`) | A5 chain: Si5351 CLK1 trapezoid source (25 or 50 ohm; VDDO, edge and duty cases) -> 3-pole drive LPF -> 18 dB pad -> GVA-84+ -> 3 dB pad -> 50 ohm module input; 270 corners; fundamental and 3f by DFT of the last three periods | **FAIL** on the 10 to 30 mW window: 6.0 to 29.5 mW, nominal 12.6 mW; 60 of 270 corners under 10 mW, none over 30 mW; TS-012 criterion corners 8.5 to 22.7 mW (27 of 36 inside). 3f at the GVA input at most -34.4 dBc: **PASS**. Plots `drive_a5_corners.png`, `drive_a5_h3.png` |
| `2026-09-28-d3-drive-a4` | `drive_a4.cir` (`b7767c8896983e0d`) | A4 chain: same source and LPF -> 12 dB pad -> GVA-84+ near its P1dB -> 50 ohm AFT05 reference-circuit input; 270 corners | 50 to 168 mW, nominal 96 mW; none above the 0.2 W ruggedness-test drive (**PASS**, informative). 3f -34.5 dBc worst: **PASS**. Plots `drive_a4_corners.png`, `drive_a4_h3.png` |
| `2026-09-28-p1-power-a5` | `power_a5.cir` (`23ee0fcc697e8f33`) | A5 power path: pack EMF swept 6.4 to 8.4 V, drain feed 0.26 / 0.35 / 0.45 ohm, 5 V bus 0.25 A, module current Pout/(eta Vd) so LTspice solves the key-down sag; module from the digitized curves with the d2 drive corners, VGG 3.5 V or the 3.08 V lowest clamp, typical or datasheet-minimum module, output loss 0.4 / 0.5 / 0.6 dB; 648 corners | Typical module: nominal 4.87 W at 6.4 V, lowest corner **3.71 W: FAIL** against 3.97 W (4.03 W with VGG at 3.5 V); datasheet-minimum module lowest 3.03 W. At 8.4 V the open-loop module reaches 9.86 W (above 8 W from 7.5 V). Plot `power_a5_sma.png` |
| `2026-09-28-p2-power-a4` | `power_a4.cir` (`42731ac9919be622`) | A4 power path: same feed and bus; AFT05 Pout(Pin) at 7.5 V scaled by (Vd/7.5)^n, n 1.8 / 2.0 / 2.3; hand-match extra loss 0 / 0.25 / 0.5 dB; d3 drive corners; 1458 corners | Nominal 3.54 W at 6.4 V (6.14 W at 8.4 V), lowest corner **2.05 W: FAIL**; the lowest corner stays under 3.97 W at every pack voltage (3.76 W at 8.4 V). Plot `power_a4_sma.png` |
| `2026-09-28-p3-power-a5-sot` | `power_a5_sot.cir` in `decks/` (`96183f7eae97dd3d`) | p1 with the drive range a select-on-test pad leaves (11.0 / 17.3 / 27.2 mW, estimate of s1) | Lowest corner 3.83 W at 6.4 V (FAIL); 4.08 W with the drain feed at most 0.35 ohm, 4.16 W with VGG at 3.5 V, 4.45 W with both. Plot `power_a5_sma.png` |
| `2026-09-28-s1-summary` | none (post-processing of d2, d3, p1, p2, p3) | Both finalists on one page; select-on-test pad residual for A5 | Plots `pin_at_pa_vs_pack.png` (Pin at the PA versus pack voltage, window lines) and `pout_at_sma_vs_pack.png` (Pout at the SMA versus pack voltage, REQ-SYS-012 lines); `result.json` |

Every PNG above was opened and inspected after rendering (visual closure, 2026-09-28), as were the eight digitizer
overlays in `data/`.

## Modelling notes (details and sources in the analysis record)

- The drive chain is a transient model because the Si5351 output is a square wave: its fundamental depends on the
  edge time, and the 3f criterion needs the harmonic. The PA stages are modelled at the power level (volts on a node
  stand for watts) because the datasheets give power curves, not device models.
- The drive and power runs are linked by the drive corners: p1 and p2 read the minimum, nominal and maximum PA input
  of d2 and d3 from their `result.json`.
- `CWHT_PA_REPLOT=1` re-reads an existing `.raw` when the deck is byte-identical (same SHA-256 as recorded), to redraw
  plots without a new LTspice run. The committed `.log` and `.raw` files come from one full run of `run_pa.py all`;
  the plots and result files were then redrawn from them with the final script (the copy in each run folder).
