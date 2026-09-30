# Run `2026-09-29-a5-closure-r2`: WP-PDR-28a thermal closure of A5, revision 1

Analysis record: `docs/design/analysis/thermal-budget.md` revision 1 (fix of the three Major review findings: the
REQ-SYS-181 backstop stack, the REQ-SYS-118 setpoint basis, and the worst pattern the duty cap allows).
Runner: `hardware/sim/thermal/a5_closure.py`. It uses the INSP-112-frozen `thermal_model.py` and `ts012_thermal.py`
unchanged (copies in `scripts/`, SHA-256 in `results.md`). Every temperature is an estimate from the lumped model of
`docs/design/analysis/thermal-ts012.md`. Run `2026-09-29-a5-closure-r1` (revision 0) is kept unchanged as the
record of what the review found.

Commands (from the repository root; LTspice only through `tools/ltspice-batch.sh`):

```
.venv/bin/python hardware/sim/thermal/a5_closure.py --run-id 2026-09-29-a5-closure-r2           # about 40 to 60 min
.venv/bin/python hardware/sim/thermal/a5_closure.py --check --run-id 2026-09-29-a5-closure-r2   # exit 1 on any difference
```

| File | What it is |
|---|---|
| `results.md` | Verdict set (C01 to C25) and proposed-values block, as the record states them; duties; closed-loop inhibit table with the governing state, its stack and band; backstop table (SRR value and proposal, time above 90 C); worst cap pattern (box bound and usability runs, cap and one step above); bench acceptance; LTspice check; bands; script SHA-256 |
| `verdict_set.csv`, `summary.csv` | The verdict set and every metric per layout, machine readable |
| `inputs.csv` | 125 inputs with value, range, class (D, DD, R, E), source, tornado use, and whether 28a added it |
| `tornado.csv`, `bands.csv` | One-at-a-time sweep of 88 inputs on the three layouts; RSS bands, also without the sink-path inputs the bench replaces |
| `protection_screen.csv`, `backstop_screen.csv` | One-at-a-time closed-loop screens of the REQ-SYS-118 inhibit and the REQ-SYS-181 backstop: the stacked inputs (role `stacked`, with the adverse end chosen) and the RSS-band inputs (role `RSS band`) |
| `inhibit.csv`, `backstop.csv`, `cap_pattern.csv`, `cap_pattern_verdicts.csv`, `bench_acceptance.csv`, `duty_sweep.csv` | Case data behind the plots |
| `cl_box_vs_duty.png` | Junction, case, PETG, PA-bay air, cells and main-bay air versus duty, A5-DC and A5-CL, with the cap, bands and the worst-pattern bounds |
| `cl_margins.png` | Margin of every verdict with its band, three layouts |
| `cl_inhibit_backstop.png` | REQ-SYS-118 inhibit on the flange NTC in closed loop (five cases, governing band), zoom on the first trip, REQ-SYS-181 backstop alone at the SRR value and at the proposal |
| `cl_protection_screen.png` | Closed-loop screen of both protection cases: which inputs are stacked, which form the band |
| `cl_cap_pattern.png` | Worst burst pattern the cap allows, 4 h: usability with the inhibit, box bound without it, cap selection against one step above |
| `cl_bench_acceptance.png` | In-situ sink acceptance value from the junction and case bounds |
| `cl_tornado.png` | A5-CL tornado, six box and junction metrics |
| `cl_ltspice_crosscheck.png`, `ltspice/` | LTspice 26.0.2 electrical analogue of A5-CL (deck, `.log`, `.raw` under 1 MB, `.op.raw`, wrapper output) against the Python solver |
| `scripts/` | The runner and the two model files as run |
| `run-stdout.txt`, `check-stdout.txt` | Console output of the run and of `--check` |
