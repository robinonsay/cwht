# hardware/sim/thermal: PA, heat sink and PETG case thermal model (WP-PDR-28)

Lumped thermal RC network of the transmit PA, the Boyd 530002B02500G heat sink and the owner-printed
PETG case, for the two TS-012 revision 4 finalists (A4: NXP AFT05MS004N on a hand-built PA board;
A5: Mitsubishi RA07M1317M module). Analysis record: `docs/design/analysis/thermal-ts012.md`.

| File | What it is |
|---|---|
| `thermal_model.py` | The model: every input with its value, range, class and source (`P`), the digitized Boyd natural-convection curve, the network builder for the four layouts, steady and transient solvers, surface and hot-face post-processing |
| `ts012_thermal.py` | The runner: runs every case, writes a results directory, draws the plots, writes and runs the LTspice electrical analogue through `tools/ltspice-batch.sh` and compares it with the Python solver |
| `results/<run-id>/` | One directory per run (owner rule): `verdicts.md` (pass/fail and numbers), `summary.csv`, `inputs.csv`, `duty_sweep.csv`, `tornado.csv`, the PNG plots, `ltspice/` (deck `.net`, LTspice `.log`, `.raw`, `.op.raw`, wrapper output), `scripts/` (the model and runner as run), `run-stdout.txt` |

Run (about 1 minute; LTspice only through the accredited wrapper, ACC-LTSPICE-001):

```
.venv/bin/python hardware/sim/thermal/ts012_thermal.py --run-id <run-id>
```

Input classes in `inputs.csv`: **D** datasheet value, **DD** derived from a datasheet (drawing dimension,
graph read, arithmetic on datasheet values), **R** requirement or TS-012 pass criterion, **E** estimate
(engineering judgement, Low confidence; every E input carries a low and a high used by the tornado).

Layouts: **A5-R4** and **A4-R4** are TS-012 revision 4 as written (sink end wall at the web of the profile,
inner half of the fins inside the case, guard 3 mm over the end face only; A4 without a bulkhead).
**A5-DC** and **A4-DC** carry the design changes of the analysis record section 7 (whole sink outside
the case end wall, FR4 spare-board end wall with its copper facing the sink, guard wrapping the sink,
larger PA-bay slots, PWM relay hold, main-bay slots).

## Runs

### `2026-09-28-ts012-r1` (TS-012 WP-PDR-28 pre-order thermal item)

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
