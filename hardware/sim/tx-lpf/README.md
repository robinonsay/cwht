# tx-lpf: transmit harmonic low-pass filter (WP-PDR-21, TS-012)

Block: the 7-pole Chebyshev harmonic low-pass filter at the antenna port that TS-012 revision 4 section 7.3
names for both finalists (A4 and A5). Analysis record: `docs/design/analysis/lpf-ts012.md`.

## Files

| File | What it is |
|---|---|
| `lpf_model.py` | Every input number with its source tag (D datasheet, C computed, E estimate): the filter design, the Coilcraft 1812SMS, 24 AWG air-coil and 1206 C0G models, board parasitics, Monte Carlo ranges, the 47 CFR 97.307(e) limit and the PA harmonic inputs of A4 and A5 |
| `run_lpf.py` | Deck writer, runner (only through `tools/ltspice-batch.sh`, ACC-LTSPICE-001), `.raw` reader (spicelib), checker and plots. `run_lpf.py all` reproduces every run below |
| `retune_screen.py` | ABCD screen of symmetric E24 value sets (input to runs r6 and r7 only; no verdict comes from it) |
| `results/<run-id>/` | Per run: the deck (`.cir`), the LTspice `.log`, `.raw`, `.op.raw`, `.db` and `.log.raw`, `ltspice_provenance.txt` (wrapper result line and deck SHA-256), `result.json` and `result.md` (numbers, pass or fail), the PNG plots with the limits drawn on them, and copies of the three scripts that made them. MC runs add `mc_values.csv` (every parameter of every step) |

The Monte Carlo `.raw` files are about 9.7 MB each (252 steps x 800 points x 2 nodes, complex double); they are
kept in git by the `.gitignore` rule for `hardware/sim/**/results/**`.

## Runs (2026-09-28)

Pass criteria of the filter (TS-012 section 7.3 WP-PDR-21; REQ-TX-009, 010, 011): at least 40 dB at 288 to
296 MHz, 35 dB at 432 to 444 MHz, 40 dB from 576 MHz to 1.5 GHz, passband loss at most 0.5 dB at 144 to 148 MHz.
"Worst" is the worst of all Monte Carlo steps including the two tolerance corners.

| Run | What | IL 144-148 MHz, median / worst (dB) | 2f worst (dB) | 3f worst (dB) | 576-1500 MHz worst (dB) | Verdict |
|---|---|---|---|---|---|---|
| `2026-09-28-r1-nominal` | Nominal: ideal exact (known answer against the analytic Chebyshev, max error 0.0005 dB, PASS), ideal BOM values, 1812SMS with parasitics, air coils with parasitics | 1812SMS 0.70; air 0.49 (nominal) | 58.8 / 57.4 | 87.0 / 84.9 | 77.6 / 77.1 | 1812SMS FAIL on IL only; air PASS nominal |
| `2026-09-28-r2-mc-1812sms` | MC, 1812SMS J, BOM 22/68/39/82 | 0.76 / 1.21 | 54.4 | 75.4 | 66.6 | FAIL (IL); stopband PASS |
| `2026-09-28-r3-mc-air-aswound` | MC, air coils as wound +/-10 %, BOM values | 0.68 / 1.30 | 50.8 | 70.8 | 65.8 | FAIL (IL); stopband PASS |
| `2026-09-28-r4-mc-air-aligned` | MC, air coils aligned +/-3 %, BOM values | 0.59 / 0.99 | 51.9 | 72.2 | 66.0 | FAIL (IL); stopband PASS |
| `2026-09-28-r6-mc-1812sms-retuned` | MC, 1812SMS J, retuned 18/68/33/82 | 0.52 / 0.71 | 44.8 | 71.3 | 69.0 | FAIL (IL); stopband PASS |
| `2026-09-28-r7-mc-air-aligned-retuned` | MC, air coils aligned +/-3 %, retuned 18/68/33/82 | 0.42 / 0.65 | 43.8 | 68.0 | 67.5 | FAIL (IL, 89 % yield); stopband PASS |
| `2026-09-28-r5-harmonic-budget` | PA harmonic levels minus the worst MC attenuation, every power step at +1 dB and every ramp instant, against 97.307(e) and the 60 dBc target | n/a | n/a | n/a | n/a | A5 PASS every build (legal margin at least 10.8 dB; 60 dBc margin at least 8.8 dB). A4 PASS legal on an estimate (at least 4.8 dB); 60 dBc FAIL with the retuned values (-0.2 and -1.2 dB), PASS with the BOM values |

Every MC run also passes its two log cross-checks (the L4 value echoed by `.meas` equals `mc_values.csv` for
every step; the `.meas` S21 at 288 MHz equals the `.raw` value within 0.001 dB for every step).

## Plots

- r1: `s21_nominal_wide.png` (S21 to 1.6 GHz with the harmonic limit points of A4 and A5 and the REQ-TX masks),
  `il_nominal_passband.png` (loss with the 0.5 dB goal), `rl_nominal_passband.png` (input return loss).
- r2, r3, r4, r6, r7: `s21_mc_wide.png` (all runs and envelope with the limit points), `il_mc_passband.png`
  (all runs, tolerance corners and the 0.5 dB goal), `mc_histograms.png` (distributions against each limit).
- r5: `harmonic_budget.png` (harmonic at the antenna per order, 5 W step and lower steps, per finalist, against
  25 uW and the 60 dBc target).

## Reproduce

```
.venv/bin/python hardware/sim/tx-lpf/run_lpf.py all
```

LTspice runs wait for the shared one-run lock (`CWHT_LTSPICE_LOCK_WAIT` is set to 3600 s by the script). The
Monte Carlo draws use fixed numpy seeds (21001, 21002, 21003, 21006, 21007), so a rerun reproduces every number.
