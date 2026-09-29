# hardware/sim/tx-seq: T/R and keying sequence timing, relay drive and hold (WP-PDR-23a)

Block owner: Claude (analysis author). Analysis record: `docs/design/analysis/sequencer-timing.md` (revision 1).
Question: does the A5 key-down and key-up sequence of TS-012 section 7.3 (revision 6) meet its pass criteria (ramp
start at least 10 ms after the relay command, lead-in at most 12 ms, key-to-RF at most 15 ms, the frequency check
finished before PA_EN, clamps held and integrator parked until the ramp start), does the Omron G5V-2 relay really
close inside that lead-in at every pull-in corner, how is its coil held at reduced power (D-5), and what timing
table goes into ICD-TX-SW.

## Files

| File | What it is |
|---|---|
| `seq_run.py` | Stage runner: deck writer, LTspice runner (only through `tools/ltspice-batch.sh`, ACC-LTSPICE-001), `.raw` reader (spicelib), relay-model sweep, sequence model, checker, plots, timing table. `seq_run.py all` reproduces every run below |
| `relay_model.py` | Reduced-order electromechanical model of the G5V-2, anchored to its datasheet (must-operate 75 %, operate 7 ms, release 3 ms, coil resistance +/-10 %); the unknown magnetic and spring parameters are a class E band (record section 3.3). Revision 1: a must-operate voltage slope per run (`s_mo`; the H1 graph band 0.48 to 0.51 %/K; `None` keeps the revision 0 copper law) |
| `expected_states.json` | The expected state of every criterion (the list of the record section 5); `--expect` compares against it |
| `results/<run-id>/` | Per run: `result.json`, `result.md`, the PNG plots and `scripts/` (copies of both scripts); s1 and s2 also the deck, the LTspice `.log` and `.raw` (kept in git by the `.gitignore` exception) |

## Runs (2026-09-29)

Revision 1 runs (the record's revision 1; `seq_run.py` as committed reproduces these):

| Run id | Stage | What | Outputs |
|---|---|---|---|
| `2026-09-29-r1-s1-drive` | s1 | As s1 below, plus branch E: the coil-supply limiter (behavioural, 6.3 V set point, 0.2 V dropout) feeding the coil and an AO3400A on a static gate | `drive_dc.cir`, `.log`, `.raw` (579,766 bytes, committed); `s1-coil-current.png`; `s1-coil-voltage-vs-pack.png` (the voltage imposed on the H1 coil against the pack, against the datasheet maximum-voltage curve; K19) |
| `2026-09-29-r1-s2-coil` | s2 | As s2 below, plus E_rise_hot (6.15 V, 85 C) and E_dc_cold (6.43 V static hold at -10 C, then off), 8 cases | `coil_tran.cir`, `.log`; `coil_tran.raw` is over the CR-017 C2 limit: kept in the folder, not committed, with `raw.sha256`; `s2-coil-transient.png` |
| `2026-09-29-r1-s3-operate` | s3 | Relay model with the H1 must-operate slope band (0.48 and 0.51 %/K; copper kept as the comparison): operate at 5 options x 3 supplies x 5 coil temperatures (-10 C added); release from every hold at -10, 23 and 85 C; option E set-point trade | `s3-operate-vs-coil-temperature.png`, `s3-release.png`, `s3-limiter-setpoint.png`, `runs.json` |
| `2026-09-29-r1-s4-sequence` | s4 | Sequence model: K1 to K22 (K19 split, K20 to K22 new), the ICD-TX-SW timing table with the SR rows, the timing diagram, the budget, margin and stale-ratio plots | `icd-tx-sw-timing-table.csv` and `.md`, `timing-diagram.png` (also `docs/reviews/PDR/figures/timing-diagram.png`), `s4-keydown-budget.png`, `s4-margins.png`, `s4-stale-ratio.png` |

Revision 0 runs (kept as the record of revision 0; each folder holds its own script copy):

| Run id | Stage | What | Outputs |
|---|---|---|---|
| `2026-09-29-s1-drive` | s1 | LTspice DC: coil current and driver drop for the 2N3904 and AO3400A low-side drivers, both coils, 32 steps (coil resistance x driver temperature 25 and 70 C) | `drive_dc.cir`, `.log`, `.raw`; `s1-coil-current.png`; driver-drop fits used by s3 |
| `2026-09-29-s2-coil` | s2 | LTspice transient: pull-in current rise, 25 kHz hold PWM average and ripple, freewheel decay, 6 cases; closed-form cross-check | `coil_tran.cir`, `.log`; `coil_tran.raw` is 7,114,568 bytes, over the 5,000,000-byte limit of CR-017 C2: kept in the folder, not committed, with `raw.sha256`; `s2-coil-transient.png` |
| `2026-09-29-s3-operate` | s3 | Relay model: operate time at 4 drive options x 3 supplies x 4 coil temperatures over 13 accepted parameter sets per coil; release from the hold current; hold margin | `s3-operate-vs-coil-temperature.png`, `s3-release.png`, `runs.json` (every model run) |
| `2026-09-29-s4-sequence` | s4 | Sequence model: every criterion K1 to K19, the ICD-TX-SW timing table, the timing diagram, the key-down budget and margin plots | `icd-tx-sw-timing-table.csv` and `.md`, `timing-diagram.png` (also written to `docs/reviews/PDR/figures/timing-diagram.png`), `s4-keydown-budget.png`, `s4-margins.png` |

## Reproduce and exit status

```
cd /Users/robinonsay/rust/cwht
.venv/bin/python hardware/sim/tx-seq/seq_run.py all            # about 40 s with the LTspice lock free
.venv/bin/python hardware/sim/tx-seq/seq_run.py all --expect   # exit 0 when every state matches expected_states.json
```

`seq_run.py` prints every check and verdict. Exit **0** when every check passes and every criterion is PASS, INFO
or CONDITION; **1** when every check passes and at least one criterion is FAIL or OPEN (the results are valid and
report it; the revision 1 run exits 1: K1b-A, K1b-B, K9, K19-CD, K20-a, K20-c, K21-CD and K22-CD FAIL, K15-B OPEN, as the record states);
**2** when a check fails (the results must not be used); with `--expect`, **3** when a state differs from
`expected_states.json`, else 0.

Checks: s1 step count, MOSFET on-resistance and 2N3904 saturation ranges, drop-fit residuals, the limiter branch against its closed form (revision 1); s2 step count, LTspice
against the closed forms (rise to the must-operate current, hold average, decay) within 3 %, hold ripple at most
5 %; s3 calibration to 7 ms at the datasheet point, at least 10 accepted parameter sets per coil, the nominal set
accepted, the model's no-motion limit against the s2 LTspice rise within 1 %, the slope law (revision 1); s4 schedule
order and the upstream checks.

Tools: LTspice 26.0.2 for MacOS through the wrapper (every run exit 0); Python 3.13 repo venv with numpy, scipy,
matplotlib and spicelib. Developer evidence (05 section 9.1): the scripts have no TV record.
