# hardware/sim/freq: frequency plan, clock plan and transmit clock spur analyses

Block of the WP-PDR-20 analyses (synthesizer, reference, frequency budget, clock plan). Every result the owner reviews is in `results/<run-id>/` with its plots, its result file with pass or fail and the numbers, the LTspice `.log` and `.raw` (kept by the `.gitignore` exception for `hardware/sim/**/results/**`), the deck and the script that made it.

## Scripts and decks

| File | What it does | Product |
|---|---|---|
| `clock_plan.py` | Harmonic map of every clock against the 2 m receive band, the CW segment, the IF, the image and the LO band (ADR-031 rules). Standard library; `--plot` renders the figure | `docs/design/analysis/clock-plan.md`, ADR-031 |
| `freq_budget.py` | Frequency error budget and counter timebase (REQ-SYS-182, REQ-TX-013) | `docs/design/analysis/frequency-budget.md` |
| `ts007_matrix.py` | TS-007 synthesizer and reference trade matrix | TS-007 |
| `r3_a5.py` | Route R3 for A5 (WP-PDR-20a): Si5351A relock budget from the data sheet and AN619 on 2^n x 1 us FC0 counts, XOSC/TCXO ratio freshness over the longest over with the TCXO's own terms from the TG2520SMN brief sheet (imports the WP-PDR-28a thermal model unchanged), the A5 R3 budget with the drift term split by check, what the key-down count verifies and the A5 band-edge guard with the settle residual at the ramp, the receive-only squaring-stage lines; the A5 reference budget with the TG2520SMN and the three options for the calibration bound (revision 4). numpy, matplotlib; `--run-id` writes `results/<run-id>/` | `docs/design/analysis/frequency-budget.md` sections 3.4 and 3.5 and the A5 rows of section 3.1 (revision 4) |
| `tx_spur_plan.py` | TS-012 transmit clock spur plan: every clock line from 118 to 175 MHz while transmitting, at the GVA-84+ input and at the antenna, for plans B0, B1, P and PB and for finalists A4 and A5 | `docs/design/analysis/spurs-ts012.md` |
| `tx_spur_filters.cir` | LTspice AC deck: drive low-pass with the 18 dB pad, option C10 drive bandpass, harmonic 7-pole low-pass (ideal and inductor Q 60) | as above |
| `tx_spur_bpf_tol.cir` | LTspice AC deck: tolerance corners (every L and every C at 0.95, 1, 1.05) of the option C10 drive bandpass | as above |
| `tx_spur_c7_tap.cir` | LTspice transient deck (revision 1): the /8 prescaler tap on CLK1 with a series resistor of 0 to 330 ohm, 144 corners; checks a valid 74LVC1G80 clock (VIH, VIL, tW, transition rate) | as above |
| `tx_spur_c7_iso.cir` | LTspice AC deck (revision 1): reverse isolation of the tap's series resistor for the flip-flop kickback (current into the pin; ground bounce behind CI) | as above |
| `tx_spur_trap.cir` | LTspice AC deck (revision 1): 150 MHz series-LC trap T1 on a 50 ohm node, L 47 nH to 2.2 uH, Q 60 and 100; attenuation at 150 MHz against carrier loss | as above |

LTspice runs only through `tools/ltspice-batch.sh` (ACC-LTSPICE-001, blob `88b71475`); the GUI is never opened. `.raw` files are parsed with spicelib from the project venv.

## Runs

### `results/r3a5-20260929-03/` (2026-09-29): WP-PDR-20a revision 4, the Major finding-13 of INSP-111 (`frequency-budget.md` revision 4; governs)

Reproduce from the repository root:

```
.venv/bin/python hardware/sim/freq/r3_a5.py --run-id r3a5-20260929-03
```

No LTspice deck in this run. The checker exits **0**: 43 PASS, 0 FAIL, 24 INFO lines. Its console output is `checker-output.txt`. Every revision 3 case line is unchanged, and the five revision 3 figures are byte-identical to those of `r3a5-20260929-02`.

| Output | Content |
|---|---|
| `results.json` | As revision 3, plus `reference_a5`: TG2520SMN uncalibrated totals on both fo-TC readings, the correct-calibration residual, each case's reference error and -60 dB edge margin, the option (b) guards, the option (c) delta, the two-unit offsets and the C-10 re-read |
| `reference-budget-a5.png` | Reference error per case against R-M3 (1.5 ppm), REQ-SYS-010 (2.5 ppm) and the A5 guard limit (2.972 ppm); margin of the -60 dB point inside the band per case |
| `relock-sequence.png`, `ratio-freshness.png`, `xosc-slope.png`, `r3-budget-and-buffer.png`, `settle-and-guard.png` | As revision 3 (same bytes) |
| `r3_a5.py` | Copy of the script as run |

Summary:
- **A5 reference.** The TG2520SMN totals 2.7 ppm (fo-TC band referred to +25 C) or 3.2 ppm (band as a 1.0 ppm window, governs) before calibration, against the 1.5 ppm R-M3 test. After a correct calibration it is 2.034 ppm, inside REQ-SYS-010, with a range of at least +/-1.5 ppm.
- **Wrong calibration value.** Within +/-0.9 ppm it puts the -60 dB point 92.8 to 166.8 Hz beyond 148.000 MHz; no fixed range protects the guard. Options for the owner: a TCXO that meets R-M3; a 1.4 or 1.5 kHz guard; a software check within 0.97 ppm of the stored factory offset.

`reference-budget-a5.png` was opened and inspected after each render; the other five PNGs are byte-identical to the revision 3 figures inspected then (visual closure, 2026-09-29).

### `results/r3a5-20260929-02/` (2026-09-29): WP-PDR-20a revision 3, the Major findings of INSP-056 (11, 12) and INSP-111 (7) (`frequency-budget.md` revision 3; superseded by `r3a5-20260929-03`)

Reproduce from the repository root:

```
.venv/bin/python hardware/sim/freq/r3_a5.py --run-id r3a5-20260929-02
```

No LTspice deck in this run. The checker exits **0**: 38 PASS, 0 FAIL, 14 INFO lines. Its console output is `checker-output.txt`.

| Output | Content |
|---|---|
| `results.json` | As the revision 2 run, plus: `relock` proposed L_max, the fallback gap and the FC0 times; `settle` (the linear-tail bound on a count, the slewing detection time, S_RAMP, the M-1(c) resolution, the A5 guard); `freshness` TCXO terms, both allocations, the M-2(a) limits; the TG2520SMN source with its PDF SHA-256 |
| `relock-sequence.png` | Key-down timelines on the 2^n x 1 us counts (proposed 1.9 ms deadline; ramp at 12 ms; TS-012 fallback); sourced Si5351A timing values against the settle budget (log) |
| `ratio-freshness.png` | MAIN-node change over the 190 s window; ratio drift bound (XOSC plus TCXO) against the ratio age with the 2.5 and 8.0 ppm allocations and the ceilings |
| `xosc-slope.png` | As revision 2 |
| `r3-budget-and-buffer.png` | d and T + d per check; 25 MHz harmonics against the receive windows |
| `settle-and-guard.png` | Linear-tail bound on the interval-12 count against T; the A5 upper-edge guard with the settle residual and the M-1(c) resolution |
| `r3_a5.py` | Copy of the script as run |

Summary:
- **Relock.** On 2^n x 1 us counts L max is 1.904 ms with the TS-012 ramp (proposed deadline 1.9 ms), 3.904 ms with the ramp at 12 ms, and -0.192 ms at interval 13; the TS-012 fallback keeps 0.308 ms from PA_EN to its ramp.
- **What the count verifies.** A linear PLL tail shifts an interval-12 count by at most 2 891 Hz, inside T, so the frequency at the ramp rests on the 5 Hz settle residual allocation, closed by M-1(c). The A5 guard margin is 70.0 Hz and the REQ-TX-006 limit 820.0 Hz.
- **Freshness.** With the TCXO terms (1.0 ppm band, 0.4 ppm step) the drift over the longest over is 7.52 ppm. The budget closes with A_kd = 10 s and 2.5 ppm at the key-down check (margin 260.0 Hz) and 8.0 ppm at interval 13 (margin 1 446.0 Hz).

Every PNG of this run was opened and inspected after rendering (visual closure, 2026-09-29).

### `results/r3a5-20260929-01/` (2026-09-29): WP-PDR-20a, route R3 for A5 (`frequency-budget.md` revision 2, section 3.4; superseded by `r3a5-20260929-02`)

Reproduce from the repository root:

```
.venv/bin/python hardware/sim/freq/r3_a5.py --run-id r3a5-20260929-01
```

No LTspice deck in this run. The checker exits **0**: 23 PASS, 0 FAIL, 10 INFO lines. Its console output is `checker-output.txt`.

| Output | Content |
|---|---|
| `results.json` | Every case line; `relock` (C6 write times at 400, 256 and 100 kHz, L max per sequence, the sourced TFREQ and TRDY values); `freshness` (slope bound, A_kd, window, main-bay change per layout and ambient with the tornado, drift over the over, the interval-12 and interval-13 ceilings and the allocation); `budget` (d, margin and undetected bound per check); `buffer_lines`; the sources with their PDF SHA-256 |
| `relock-sequence.png` | Key-down timelines per sequence variant; sourced Si5351A timing values against the settle budget (log) |
| `ratio-freshness.png` | MAIN-node change over the 190 s window; drift bound against the ratio age with the allocations and ceilings |
| `xosc-slope.png` | Admissible AT-cut curves in the Table 596 band; slope envelope over -10 to +65 C |
| `r3-budget-and-buffer.png` | d and T + d per check; 25 MHz harmonics against the receive windows |
| `r3_a5.py` | Copy of the script as run |

Summary:
- **Relock.** Neither the data sheet nor AN619 gives a relock time, so the 1 ms allocation is not confirmed. The writes take 0.650 ms at 400 kHz. L max is 2.0 ms with the TS-012 ramp and 4.0 ms with the ramp at 12 ms; interval 13 at the changeover leaves 0 ms. The design response is the lock-gated start, closed by measurement M-1.
- **Freshness.** The drift over the longest over is 6.12 ppm, over the 1 ppm allocation. The budget closes with A_kd = 10 s at the key-down check and 6.5 ppm at interval 13. The margins are 482.0 Hz (interval 12) and 1 668.0 Hz (interval 13).
- **Squaring stage.** No 25 MHz harmonic falls in a receive window; the 150 MHz transmit line is unchanged with the stage off.

Every PNG of this run was opened and inspected after rendering (visual closure, 2026-09-29).

### `results/txspur-20260928-02/` (2026-09-28): revision 1 of the spur plan (fixes review finding-1 and finding-2 of revision 0)

Reproduce from the repository root:

```
for d in tx_spur_filters tx_spur_bpf_tol tx_spur_c7_tap tx_spur_c7_iso tx_spur_trap; do
  tools/ltspice-batch.sh -t 900 -o hardware/sim/freq/results/txspur-20260928-02 -b hardware/sim/freq/$d.cir; done
.venv/bin/python hardware/sim/freq/tx_spur_plan.py --run-id txspur-20260928-02
```

Every LTspice run exited 0 through the wrapper (`*.wrapper.txt` holds each wrapper result line); the checker exits **1: residual lines** (TS-012 7.3 met by wording only). Its console output is `checker-output.txt`.

| Output | Content |
|---|---|
| `results.json` | Per plan and finalist: the TS-012 criterion in the numbers and by wording, residual lines over 60 dBc and over 25 uW (at the three carriers and over the band), each residual line with its credited and its named-only changes (`cases.<plan>/<finalist>/<carrier>.residual_lines`); `c7` (valid clock and isolation per resistor, every corner); `t1_trap` (sizing and verdict); filter checks; C10 corners; ADR-031 re-check; exit-status meaning |
| `lines.csv` | Every line with the residual flags and the columns `credited_in_numbers` and `named_not_credited` |
| `spectrum-gva-A5-144.050.png`, `spectrum-gva-A4-144.050.png` | Every line of B0, B1, P, PB against -61 and -68 dBm at the GVA-84+ input |
| `antenna-P-PB-144.050.png`, `antenna-P-PB-147.950.png` | Plans P and PB for A5 and A4 at the SMA, -16 and -23 dBm limits, residual lines labelled |
| `worst-line-vs-carrier.png` | Strongest line, residual lines over -23 dBm and over -16 dBm across 144.010 to 147.990 MHz |
| `c7-prescaler-tap.png` | CP pin swing per series resistor against VIH and VIL (with the 0.10 V margin), worst-corner waveforms, LTspice isolation against the revision 0 formula |
| `t1-trap.png` | T1 relative suppression against carrier loss (Q 60, 100; 147.990 and 144.050 MHz) with the 11.0 and 4.0 dB needs; trap responses |
| `filters.png`, `c10-tolerance.png` | As in run 01 (same decks, re-run) |
| `*.log`, `*.raw` and the other LTspice outputs; `*.cir`, `tx_spur_plan.py` | LTspice outputs of the five decks; copies of the decks and the script as run |

Summary (line levels ESTIMATES of Low confidence; filters, C7 and T1 from LTspice):

| Plan | Worst line at the SMA, high estimate (A5 and A4) | Residual lines over -23 dBm over the band | Of which over -16 dBm (25 uW) | TS-012 criterion |
|---|---|---|---|---|
| B0, B1 | -0.4 dBm (/8 prescaler 7/8 fc) | 16 to 19 | 10 | not met |
| P | -4.3 dBm (/8 kickback 7/8 fc) | 10 to 12 | 4 | met by wording only (residual lines) |
| PB | -12.1 dBm (150.000 MHz, and the /8 kickback at 9/8 fc) | 6 to 8 | 3 | met by wording only (residual lines) |

- **C7 (finding-2).** Revision 0's 330 ohm tap stops the 74LVC1G80 clock: the pin misses VIH and VIL by 0.26 V at the low corner. Its isolation is 5.5 dB in LTspice, not the 23 dB claimed. The largest valid value is 47 ohm (0.23 V margin), which buys 0.4 dB. The /8 kickback sidebands are therefore residual lines.
- **T1 (finding-1).** No trap size gives the 11.0 dB relative suppression that 60 dBc needs at 147.990 MHz (best 9.2 dB). For 25 uW, 4.0 dB costs 1.7 dB of carrier. T1 is withdrawn as the fallback.
- A4 and A5 differ by at most 0.8 dB on every residual line, so the spur plan still does not discriminate between them.

Every PNG of this run was opened and inspected after rendering (visual closure, 2026-09-28).

### `results/txspur-20260928-01/` (2026-09-28, superseded by run 02): TS-012 transmit clock spur plan (WP-PDR-20 pre-order item, TS-012 revision 4)

Kept for the record. Its "PASS" for P and PB was the TS-012 wording only (review finding-1), and its C7 credit of 23 dB was invalid (finding-2).

Reproduce from the repository root:

```
tools/ltspice-batch.sh -o hardware/sim/freq/results/txspur-20260928-01 -b hardware/sim/freq/tx_spur_filters.cir
tools/ltspice-batch.sh -o hardware/sim/freq/results/txspur-20260928-01 -b hardware/sim/freq/tx_spur_bpf_tol.cir
.venv/bin/python hardware/sim/freq/tx_spur_plan.py --run-id txspur-20260928-01
```

| Output | Content |
|---|---|
| `results.json` | Pass or fail per plan and finalist, worst line, every line over the 60 dBc target with its named change, filter checks, C10 tolerance corners, ADR-031 receive-band re-check of clk_sys 96 MHz |
| `lines.csv` | Every line (plan, finalist, carrier 144.050, 146.000, 147.950 MHz): frequency, source, injection point, low and high estimate at the SMA and referred to the GVA-84+ input, verdicts at 60 dBc and 25 uW, basis, change named |
| `spectrum-gva-A5-144.050.png`, `spectrum-gva-A4-144.050.png` | Every line against the -61 dBm (25 uW) and -68 dBm (60 dBc) limits at the GVA-84+ input, plans B0, B1, P and PB |
| `antenna-PB-144.050.png`, `antenna-PB-147.950.png` | Plan PB at the SMA for A5 and A4, with the harmonic low-pass response and the -16 and -23 dBm limits |
| `worst-line-vs-carrier.png` | Strongest line and number of lines over -23 dBm across 144.010 to 147.990 MHz, every plan and finalist |
| `filters.png` | LTspice filter transfers against the analytic prototypes (agreement to 0.003 dB) |
| `c10-tolerance.png` | Option C10 bandpass at its nine tolerance corners, against its passband criterion |
| `tx_spur_filters.*`, `tx_spur_bpf_tol.*` | LTspice `.log`, `.raw`, `.op.raw`, `.db` of the two decks |
| `tx_spur_filters.cir`, `tx_spur_bpf_tol.cir`, `tx_spur_plan.py` | Copies of the decks and the script as run (the block copies one level up are the maintained ones) |

Summary (all line levels are ESTIMATES of Low confidence; filters from LTspice):

| Plan | A5 worst line at the SMA (high estimate) | A4 | Lines over -23 dBm (high estimate), over 144.010 to 147.990 MHz (A5; A4) | TS-012 criterion |
|---|---|---|---|---|
| B0: TS-012 revision 4 as written (clk_sys 125 MHz, clk_adc continuous, /8 on a plain 100 pF tap, PLL B running) | -0.4 dBm (the /8 prescaler 7/8 fc product) | -0.4 dBm | 17 to 19; 16 to 18 | not met as written |
| B1: ADR-031 values (clk_sys 150 MHz) | -0.4 dBm | -0.4 dBm | 17 to 19; 16 to 18 | not met as written |
| P: proposed clock, firmware and layout changes C1 to C8, L1 to L5, F1, F3 | -11.2 dBm (25 MHz x 5 at 125 MHz, Si5351 feedthrough) | -11.7 dBm | 8 to 10; 8 to 10 | PASS (every line has a named change) |
| PB: P plus option C10 drive bandpass | -12.1 dBm (25 MHz x 6 at 150.000 MHz) | -12.7 dBm | 4 to 6; 4 to 6 | PASS |

The one line that no clock choice moves and no filter reaches is 150.000 MHz (25 MHz x 6 on the Si5351 output, 2 MHz above the band). It passes the 60 dBc target only if the Si5351 puts it at least 60 dB under the carrier at the CLK1 pin; no datasheet figure exists, so it rests on the tinySA sweep (fallback: unpopulated 150 MHz trap footprint T1). A4 and A5 differ by under 1 dB on every line: the spur plan does not discriminate between the finalists. Option C10 passes its tolerance check with 2 % parts (passband within 0.7 dB, 125 MHz rejection at least 14.6 dB) and fails with 5 % parts (3.7 dB, 9.0 dB), so it needs G-tolerance inductors and 2 % C0G capacitors. Details, inputs and limitations: `docs/design/analysis/spurs-ts012.md`.
