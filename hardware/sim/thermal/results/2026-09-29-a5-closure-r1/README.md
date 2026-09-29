# Run `2026-09-29-a5-closure-r1`: WP-PDR-28a thermal closure of A5

Analysis record: `docs/design/analysis/thermal-budget.md` revision 0. Runner: `hardware/sim/thermal/a5_closure.py`.
It uses the INSP-112-frozen `thermal_model.py` and `ts012_thermal.py` unchanged (copies in `scripts/`, SHA-256 in `results.md`).
Every temperature is an estimate from the lumped model of `docs/design/analysis/thermal-ts012.md`.

Commands (from the repository root; LTspice only through `tools/ltspice-batch.sh`):

```
.venv/bin/python hardware/sim/thermal/a5_closure.py --run-id 2026-09-29-a5-closure-r1           # about 6 to 15 min
.venv/bin/python hardware/sim/thermal/a5_closure.py --check --run-id 2026-09-29-a5-closure-r1   # exit 1 on any difference
```

| File | What it is |
|---|---|
| `results.md` | Verdict set (C01 to C27) and proposed-values block, as the record states them; duties; closed-loop inhibit and backstop tables; worst cap pattern; bench acceptance; LTspice check; bands; script SHA-256 |
| `verdict_set.csv`, `summary.csv` | The verdict set and every metric per layout, machine readable |
| `inputs.csv` | 124 inputs with value, range, class (D, DD, R, E), source, tornado use, and whether 28a added it |
| `tornado.csv`, `bands.csv` | One-at-a-time sweep of 88 inputs on the three layouts; RSS bands, also without the sink-path inputs the bench replaces |
| `inhibit.csv`, `backstop.csv`, `cap_pattern.csv`, `bench_acceptance.csv`, `duty_sweep.csv` | Case data behind the plots |
| `cl_box_vs_duty.png` | Junction, case, PETG, PA-bay air, cells and main-bay air versus duty, A5-DC and A5-CL, with the cap and bands |
| `cl_margins.png` | Margin of every verdict with its band, three layouts |
| `cl_inhibit_backstop.png` | REQ-SYS-118 inhibit on the flange NTC in closed loop (four cases), zoom on the first trip, REQ-SYS-181 backstop alone |
| `cl_cap_pattern.png` | Worst burst pattern the 35 % / 10 min cap allows, 4 h |
| `cl_bench_acceptance.png` | In-situ sink acceptance value from the junction and case bounds |
| `cl_tornado.png` | A5-CL tornado, six box and junction metrics |
| `cl_ltspice_crosscheck.png`, `ltspice/` | LTspice 26.0.2 electrical analogue of A5-CL (deck, `.log`, `.raw` under 1 MB, `.op.raw`, wrapper output) against the Python solver |
| `scripts/` | The runner and the two model files as run |
| `run-stdout.txt`, `check-stdout.txt` | Console output of the run and of `--check` |

Plots opened and checked by the author on 2026-09-29 (visual closure, rule C5).
