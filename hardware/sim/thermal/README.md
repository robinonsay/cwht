# hardware/sim/thermal: PA, heat sink and PETG case thermal model (WP-PDR-28)

Lumped thermal RC network of the transmit PA, the Boyd 530002B02500G heat sink and the owner-printed
PETG case, for the two TS-012 revision 4 finalists (A4: NXP AFT05MS004N on a hand-built PA board;
A5: Mitsubishi RA07M1317M module). Analysis record: `docs/design/analysis/thermal-ts012.md` (revision 1;
review INSP-112).

| File | What it is |
|---|---|
| `thermal_model.py` | The model: every input with its value, range, class and source (`P`, 112 inputs; `build()` has no numeric input of its own), the digitized Boyd natural-convection curve, the network builder for the four layouts, steady and transient solvers, the closed-loop REQ-SYS-118 inhibit (`inhibit_run`, NTC offset and lag), surface and hot-face post-processing |
| `ts012_thermal.py` | The runner and checker: runs every case, the tornado over every ranged input and the RSS bands, the verdict set, writes a results directory, draws the plots, writes and runs the LTspice electrical analogue through `tools/ltspice-batch.sh` and compares it with the Python solver. `--check` compares the verdict set with the block the analysis note states and exits 1 on any difference |
| `results/<run-id>/` | One directory per run (owner rule): `verdicts.md` (verdict set with bands, trip sequence, inhibit cases, other numbers), `verdict_set.csv`, `summary.csv`, `inputs.csv`, `tornado.csv`, `bands.csv`, `trips.csv`, `inhibit.csv`, `levers.csv`, `duty_sweep.csv`, the PNG plots, `ltspice/` (deck `.net`, LTspice `.log`, `.raw`, `.op.raw`, wrapper output), `scripts/` (the model and runner as run), `run-stdout.txt`, `check-stdout.txt` |

Run (about 3 minutes; LTspice only through the accredited wrapper, ACC-LTSPICE-001):

```
.venv/bin/python hardware/sim/thermal/ts012_thermal.py --run-id <run-id>
.venv/bin/python hardware/sim/thermal/ts012_thermal.py --check --run-id <run-id>   # exit 1 on any difference
```

Input classes in `inputs.csv`: **D** datasheet value, **DD** derived from a datasheet (drawing dimension,
graph read, arithmetic on datasheet values), **R** requirement or TS-012 pass criterion, **E** estimate
(engineering judgement, Low confidence). Every input with a low and a high is swept by the tornado (column
`in_tornado`), except the four NTC inputs, which the explicit inhibit cases vary.

Verdicts: **PASS** value plus its RSS band within the limit; **OPEN** nominal within the limit but the band
crosses it (not shown to pass); **FAIL** nominal over the limit.

Layouts: **A5-R4** and **A4-R4** are TS-012 revision 4 as written (sink end wall at the web of the profile,
inner half of the fins inside the case, guard 3 mm over the end face only; A4 without a bulkhead).
**A5-DC** and **A4-DC** carry the design changes of the analysis record section 8 (whole sink outside
the case end wall, FR4 spare-board end wall with its copper facing the sink, guard wrapping the sink,
larger PA-bay slots, PWM relay hold, main-bay slots).

## Runs

### `2026-09-28-ts012-r2` (revision 1 of the note; INSP-112 iteration 1 fixes)

Scripts: `thermal_model.py` SHA-256 `54b5ecf4ca41d2535fadcab0f93801b380b4dfe2ebe24e4debbaaf39ba3e66e0`, `ts012_thermal.py` SHA-256 `09cf75ef57932c5fcd15da3355f1d3cfcc3ab508cfabe1b88f5da8b371b97ce0`
(copies in `results/2026-09-28-ts012-r2/scripts/`). LTspice 26.0.2 deck SHA-256 `bf655e99ea6a92c407ebf328bc27139c2d8effb758a9715edd368f7170e18e36`.
`--check` exit 0 (`check-stdout.txt`).

| Result (45 C ambient, 8.4 V pack, 5 W at the SMA unless stated; estimates) | Limit | A5-R4 | A5-DC | A4-R4 | A4-DC |
|---|---|---|---|---|---|
| PA dissipation, W | - | 9.94 | 9.94 | 5.55 | 5.55 |
| Junction, continuous key-down, steady (RSS band up), C | 110 | 142.1 (+28.1) FAIL | 126.0 (+20.0) FAIL | 131.0 (+19.7) FAIL | 122.7 (+20.3) FAIL |
| Junction after 5 min continuous (HZ-003 K7), C | 110 | 109.2 OPEN | 107.1 OPEN | 107.6 OPEN | 106.5 OPEN |
| Largest duty holding 110 C (13 s key-downs), nominal | - | 40 % | 60 % | 45 % | 60 % |
| Junction peak at 50 % duty, C | 110 | 114.6 FAIL | 104.4 OPEN | 111.9 FAIL | 105.6 OPEN |
| Inhibit on the PA-case NTC at 85 C, +3 C tolerance, closed loop, C | 110 | 111.5 FAIL | 111.3 FAIL | 117.5 FAIL | 117.0 FAIL |
| Inhibit setpoint that holds 110 C (+3 C, sensor offset and lag adverse), C | - | 80.4 | 80.9 | 75.9 | 77.1 |
| First protection with the NTC on the sink (continuous from soak) | - | 85 C at 5.2 min | 85 C at 5.7 min | 85 C at 12.8 min (junction 123 C) | none acts |
| Hottest reachable surface, 25 C, 5 min, C | 48 | 64.2 FAIL (fin tips) | 32.3 PASS | 49.7 FAIL (fin tips) | 29.5 PASS |
| Hottest PETG, duty-limited corner, C | 60 | 70.7 FAIL | 60.1 FAIL | 58.7 OPEN | 56.5 OPEN |
| Main-bay air, 50 % duty 30 min, C | 55 | 58.6 FAIL | 55.0 OPEN | 61.8 FAIL | 53.2 OPEN |
| Cells, long session at the duty limit, C | 55 | 59.6 FAIL | 58.9 FAIL | 61.5 FAIL | 55.2 FAIL |
| LTspice analogue against the Python solver (A5-DC) | 0.5 K | | 0.016 K PASS | | |

The full verdict set (V01 to V22) is in `verdicts.md` and in section 5 of the note.

Plots (each opened and checked, 2026-09-28): `tj_vs_time_45C.png` (junction and the moments each
protection would act), `tj_vs_duty.png`, `surfaces_25C_5min.png`, `petg_and_cells_45C.png`, `tornado.png`
(A5-DC and A4-DC, four metrics, RSS band shaded), `margins_vs_band.png` (every verdict with its band),
`inhibit_bound.png` (closed-loop inhibit, four cases, and a zoom on the first trip), `sink_catalog_curve.png`,
`network_a5dc.png` (re-laid out: no line crosses a box it does not end at), `ltspice_crosscheck.png`.

Reading: neither finalist meets REQ-SYS-112 as written. With the no-cost changes and a duty limit, both hold
110 C up to about 60 % duty at 45 C on nominal inputs, but inside a band of 12 to 16 K. The 85 C inhibit does
not hold 110 C at its +3 C tolerance for either finalist; the setpoints that do are about 81 C (A5) and
77 C (A4) at a PA-case NTC. A5 puts about twice the PA heat into the case; most box verdicts of both are
inside their bands. Verdicts, limitations, requests and what closes before the order are in the analysis record.


### `2026-09-28-ts012-r1` (revision 0 of the note; superseded by r2)

Kept unchanged for the INSP-112 trail. Known defects, fixed in r2: the PETG and FR4 wall heat capacities were 1000 times too small (transients only); the A4-DC long-session cells (55.17 C) are FAIL here but were reported as a pass in revision 0 of the note; no uncertainty bands; the inhibit bound has no sensor offset or lag.

Scripts: `thermal_model.py` SHA-256 `a5843f9a...69cac`, `ts012_thermal.py` SHA-256 `7f576ee8...aeb5ce96cf`
(copies in `results/2026-09-28-ts012-r1/scripts/`). LTspice 26.0.2 deck SHA-256 `b804c278...b4901`.

| Result (45 C ambient, 8.4 V pack, 5 W at the SMA unless stated) | Limit | A5-R4 | A5-DC | A4-R4 | A4-DC |
|---|---|---|---|---|---|
| PA dissipation, W (estimate) | - | 9.94 | 9.94 | 5.55 | 5.55 |
| Junction, continuous key-down, steady, C | 110 | 142 FAIL | 126 FAIL | 131 FAIL | 123 FAIL |
| Junction range, favourable to adverse input stack, C | 110 | 112 to 183 | 97 to 174 | 101 to 180 | 92 to 174 |
| Largest duty holding 110 C (10 s key-downs) | - | 40 % | 60 % | 45 % | 60 % |
| Junction peak at 50 % duty, C | 110 | 114 FAIL | 104 PASS | 112 FAIL | 105 PASS |
| Junction bound by an 85 C (+3 C) PA-case inhibit, C | 110 | 108 PASS | 108 PASS | 112 FAIL | 112 FAIL |
| Hottest accessible surface, 25 C, 5 min, C | 48 | 66 FAIL (fin tips) | 37 PASS | 50 FAIL (fin tips) | 33 PASS |
| Hottest PETG, duty-limited corner, C | 60 | 71 FAIL | 60.1 FAIL (0.1 K) | 59 PASS | 56 PASS |
| Cells / main-bay air, 50 % duty 30 min, C | 55 | 52 / 59 FAIL | 51 / 55.4 FAIL (0.4 K) | 53 / 62 FAIL | 50 / 54 PASS |
| PA-bay air (relay rating 65 C), duty-limited corner, C | 65 | 70 FAIL | 61 PASS | 64 PASS | 57 PASS |
| LTspice analogue against the Python solver (A5-DC) | 0.5 K | | 0.017 K PASS | | |

Plots (each opened and checked, 2026-09-28): `tj_vs_time_45C.png`, `tj_vs_duty.png`,
`surfaces_25C_5min.png`, `petg_and_cells_45C.png`, `tornado.png`, `sink_catalog_curve.png`,
`network_a5dc.png`, `ltspice_crosscheck.png`. In `network_a5dc.png` every line to AMB ends at the AMB
box; the resistance label sits at the middle of its line.

Reading: neither finalist meets REQ-SYS-112 as written (continuous key-down at 45 C). With the
no-cost changes and a firmware duty limit, both hold 110 C up to about 60 % key-down duty at 45 C.
Both hold it for continuous key-down at 25 C (A5-DC 106 C, A4-DC 103 C). The verdicts, limitations
and what closes before the order are in the analysis record.
