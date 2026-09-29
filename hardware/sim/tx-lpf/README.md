# tx-lpf: transmit harmonic low-pass filter (WP-PDR-21, TS-012)

Block: the 7-pole Chebyshev harmonic low-pass filter at the antenna port that TS-012 revision 4 section 7.3
names for both finalists (A4 and A5). Analysis record: `docs/design/analysis/lpf-ts012.md` (revision 2).

## Files

| File | What it is |
|---|---|
| `lpf_model.py` | Every input number with its source tag (D datasheet, C computed, E estimate): the filter design, the Coilcraft 1812SMS, 24 AWG air-coil and 1206 C0G models, board parasitics, the parameter box (`param_bounds`, signed coil coupling since revision 2), the `.ac list` grid (`FREQS`), the 47 CFR 97.307(e) limit, and the PA harmonic inputs of A4 and A5 per power step and pack voltage (`pa_state`) |
| `lpf_nodal.py` | Nodal model of exactly the deck's circuit, the fast evaluator of the corner search. Checked against LTspice at every step and frequency of every run (criterion 0.01 dB) |
| `worst_case.py` | Worst-case corner search over the whole parameter box, one corner per metric (loss, 2f, 3f, 576 MHz to 1.5 GHz, and A(nf) - IL(f) for 2f, 3f, 4f to 10f) |
| `run_lpf.py` | Deck writer, runner (only through `tools/ltspice-batch.sh`, ACC-LTSPICE-001), `.raw` reader (spicelib), checker and plots. `run_lpf.py all` reproduces r1, r8 to r16 |
| `retune_screen.py` | Revision 1's ABCD screen of symmetric E24 value sets (the input to the withdrawn retune; no verdict comes from it) |
| `results/<run-id>/` | Per run: the deck (`.cir`), the LTspice `.log`, `.raw`, `.op.raw`, `.db` and `.log.raw`, `ltspice_provenance.txt` (wrapper result line and deck SHA-256), `result.json` and `result.md` (numbers, pass or fail), the PNG plots with the limits drawn on them, and copies of the scripts that made them. Worst-case runs add `mc_values.csv` (every parameter of every step, and which steps are corners) |

The `.raw` files of the worst-case runs are about 11 MB each (259 steps x 914 points x 2 nodes, complex double);
they are kept in git by the `.gitignore` rule for `hardware/sim/**/results/**`.

## Exit status (revision 2, review finding-5)

`run_lpf.py` exits 0 when every criterion is met and every check passes, 1 when every check passes and at least one
criterion fails (the results are valid and report the failure), and 2 when a check fails (known answer, nodal model
against LTspice, corner values, `.meas` cross-checks: the results must not be used). It prints every failed item.
`run_lpf.py all` exits **1** on 2026-09-28: the passband-loss criterion fails in every build, REQ-TX-009 fails in r9,
r11, r12 and r16, REQ-TX-011 in r16, and the budget items listed under r15 below.

## Runs, revision 2 (2026-09-28)

Pass criteria of the filter (TS-012 section 7.3 WP-PDR-21; REQ-TX-009, 010, 011): at least 40 dB at 288 to 296 MHz,
35 dB at 432 to 444 MHz, 40 dB from 576 MHz to 1.5 GHz, passband loss at most 0.5 dB at 144 to 148 MHz. "Worst case"
is the worst of every LTspice step of the run, which is the corner the search found (steps 253 to 259); "MC" is steps
1 to 252 (two revision 1 corners and 250 uniform draws over the box). Every run passes all its checks.

| Run | What | IL 144-148 MHz: worst case / MC median (dB) | 2f worst case (dB) | 3f worst case (dB) | 576-1500 MHz worst case (dB) | Verdict at the worst case |
|---|---|---|---|---|---|---|
| `2026-09-28-r1-nominal` | Nominal: ideal exact (known answer against the analytic Chebyshev, max error 0.0005 dB, PASS), ideal BOM values, 1812SMS with parasitics, air coils with parasitics | 1812SMS 0.70; air 0.49 (nominal) | 58.8 / 57.4 | 87.0 / 84.9 | 77.6 / 77.1 | 1812SMS FAIL on IL only; air PASS nominal |
| `2026-09-28-r8-wc-1812sms-bom` | 1812SMS J, BOM 22/68/39/82 | 2.82 / 0.77 | 45.1 | 70.1 | 61.8 | FAIL (IL) |
| `2026-09-28-r9-wc-air-aswound-bom` | Air coils as wound +/-10 %, BOM | 5.34 / 0.73 | 39.7 | 63.1 | 59.3 | FAIL (IL, REQ-TX-009) |
| `2026-09-28-r10-wc-air-aligned-bom` | Air coils aligned +/-3 %, BOM | 3.38 / 0.67 | 41.8 | 64.2 | 59.6 | FAIL (IL) |
| `2026-09-28-r11-wc-1812sms-retuned` | 1812SMS J, retuned 18/68/33/82 (withdrawn) | 1.39 / 0.53 | 38.3 | 64.8 | 62.7 | FAIL (IL, REQ-TX-009) |
| `2026-09-28-r12-wc-air-aligned-retuned` | Air coils aligned, retuned (withdrawn) | 1.56 / 0.45 | 35.6 | 59.1 | 60.6 | FAIL (IL, REQ-TX-009) |
| `2026-09-28-r13-wc-1812sms-bom-2pct` | 1812SMS G and C0G G (2 %), BOM values (recommended) | 1.76 / 0.74 | 47.1 | 71.0 | 61.9 | FAIL (IL) |
| `2026-09-28-r14-wc-1812sms-22-36-2pct` | 1812SMS G and C0G G (2 %), 22/68/36/82 | 1.24 / 0.65 | 45.6 | 71.1 | 61.9 | FAIL (IL) |
| `2026-09-28-r16-wc-1812sms-trap-screen` | Trap variant 10/47/20/68 with 5.6 pF across L2 and L6 (screened, rejected) | 0.67 / 0.27 | 40.0 | 47.8 | **9.9** | FAIL (IL, REQ-TX-009, REQ-TX-011) |
| `2026-09-28-r15-harmonic-budget-rev2` | PA harmonic minus [A(nf) - IL(f)] of r8 to r14, every step at +1 dB, every pack voltage (6.4, 7.2, 8.4 V), every ramp instant, against 97.307(e) and the 60 dBc target | n/a | n/a | n/a | n/a | 97.307(e) PASS for both finalists with the BOM values (A5 7.5 / 9.5 dB, A4 5.5 / 7.5 dB, J / G parts), FAIL with the retuned values for A4 (-1.1 dB) and with the aligned-air retuned values for both. 60 dBc: A5 PASS with the BOM values (+1.5 / +3.5 dB at 8.4 V), A4 PASS only with 2 % parts (+1.5 dB; -0.5 dB with J) |

## Runs, revision 1 (superseded, kept as the record)

`2026-09-28-r2-mc-1812sms`, `r3-mc-air-aswound`, `r4-mc-air-aligned`, `r6-mc-1812sms-retuned`,
`r7-mc-air-aligned-retuned` (Monte Carlo with positive-only coil coupling; the "worst" there is the sample worst of
252 steps, which review finding-1 showed is not a worst case) and `r5-harmonic-budget` (left out the passband loss
and the pack-voltage cases, findings 3 and 4). Each is reproduced by the copy of the scripts in its own folder; the
current `run_lpf.py` refuses those run names.

## Plots

- r1: `s21_nominal_wide.png` (S21 to 1.6 GHz with the A(nf) - IL(f) each finalist needs and the REQ-TX masks),
  `il_nominal_passband.png` (loss with the 0.5 dB goal), `rl_nominal_passband.png` (input return loss).
- r8 to r14, r16: `s21_wc_wide.png` (MC spread and envelope, the loss, 2f and 576-1500 MHz corners, the needed
  levels and masks), `harmonic_bands_wc.png` (2f and 3f bands with REQ-TX-009, 010 and the 60 dBc needs of A4 and A5),
  `il_wc_passband.png` (MC, the revision 1 corners, the worst-case loss corner, the 0.5 dB criterion and the withdrawn
  0.75 dB proposal), `mc_wc_histograms.png` (distributions with the limit dashed and the worst case solid).
- r15: `harmonic_budget.png` (harmonic at the antenna per order, 5 W step and lower steps, worst pack voltage, per
  finalist, filled worst case and hollow MC worst, against 25 uW and the 60 dBc target), `harmonic_margins.png`
  (60 dBc and 97.307(e) margins per build and pack voltage), `a5_power_margin_6v4.png` (A5 REQ-SYS-012 margin at
  6.4 V per build for the MC median, MC worst and worst-case loss).

## Reproduce

```
.venv/bin/python hardware/sim/tx-lpf/run_lpf.py all
```

LTspice runs wait for the shared one-run lock (`CWHT_LTSPICE_LOCK_WAIT` is set to 3600 s by the script). The Monte
Carlo draws use fixed numpy seeds (21008 to 21016) and the corner search fixed seeds (31000), so a rerun reproduces
every number. The whole set takes about 25 minutes of CPU, most of it the corner search.
