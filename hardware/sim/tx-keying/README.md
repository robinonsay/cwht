# hardware/sim/tx-keying: keying envelope and key clicks for the TS-012 finalists (WP-PDR-22 pre-order item)

LTspice transients of the transmit keying envelope loop for the two TS-012 revision 4 finalists (A4: NXP
AFT05MS004N discrete PA with gate-bias control; A5: Mitsubishi RA07M1317M module with VGG control), with the
FFT of the RF envelope against REQ-SYS-014, REQ-SYS-015 (TC-SYS-013 method), REQ-TX-005 and REQ-TX-006, and
the RF level at key-up against REQ-TX-014 and REQ-SYS-183. Analysis record:
`docs/design/analysis/keying-ts012.md`.

| File | What it is |
|---|---|
| `det_char.cir` | 146 MHz transient of the TS-012 ALC detector (series 1N5711W, zero bias, 2.2 k / 180 ohm tap, 47 k load): static law, 13 amplitudes |
| `det_char_biased.cir` | 146 MHz transient of the mitigated detector (shunt 1N5711W biased at about 21 uA, matched reference diode) |
| `keying_run.py` | Generator, runner and checker: writes the keying decks, runs them through `tools/ltspice-batch.sh`, parses the `.raw` with spicelib, computes per element the 10-to-90 % rise and fall (asserted against REQ-TX-005 +/-10 % and TC-SYS-013 +/-0.5 ms separately), shape error, overshoot, and over elements 3 to 8 the 26 dB bandwidth, the 10 Hz sideband cells and the key-up level; element 1 (trim starting from mid-rail) is reported on its own; draws the plots and writes `result.json` and `result.csv`; holds the threshold budget (`THRESHOLD_BUDGET`, record section 3.2); also the analytic PWM carrier ripple and loop margin |
| `keying_a4_asis.cir`, `keying_a5_asis.cir` | Envelope-domain decks of the loop as TS-012 revision 4 section 7.3 describes it (generated; revision 1: A5 from the digitized curves) |
| `keying_a4_sweep0.cir`, `keying_a5_sweep0.cir` | Revision 0 mitigated design, threshold sweep -0.30 to +0.30 V at 0.5 and 5 W, 7.4 V pack (generated) |
| `keying_a4_fix.cir`, `keying_a5_fix.cir` | Revision 1 design: 4 steps x 3 packs x 3 settings x 5 record corners (nominal; compensated and stored-trim budget worst-case sums with the offset), 180 runs (generated; revision 1: 3 corners, 108 runs) |
| `keying_a4_sweep1.cir`, `keying_a5_sweep1.cir` | Revision 1 design, threshold sweep -0.30 to +0.30 V, 4 steps, 7.4 V pack (generated) |
| `keying_a4_sens.cir`, `keying_a5_sens.cir` | Revision 2 (INSP-116 finding-13): element 1 only, VSH -0.30 to +0.30 V in 0.02 V, 4 steps x 3 settings x 7 cases (nominal, VOS +/-1 mV, packs 6.4 and 8.4 V, sub-threshold slope 65 and 150 dB/V), 2604 runs (generated) |
| `expected_states.json` | Revision 2 (finding-11): the expected FAIL states (criterion, runs) of every r2 run id with the reason; each `deck`/`replot` stage exits 3 when its FAIL states differ, and `--accept` refuses a FAIL of a criterion the design must pass |
| `keying_a4_mitig.cir`, `keying_a5_mitig.cir` | Revision 0 mitigated decks (5 W only, +/-0.1 V corners), superseded; kept because the revision 0 runs used them |
| `results/<run-id>/` | One directory per run (owner rule): deck, LTspice `.log`, `.raw`, `.op.raw`, wrapper output, `result.json` and `result.csv` (pass/fail and numbers), PNG plots, the script as run |

Run (LTspice only through the accredited wrapper, ACC-LTSPICE-001; a 108 to 156-step deck takes 30 to 60 s
of LTspice once the wrapper lock is free, plus about 1 min of analysis):

```
tools/ltspice-batch.sh -t 600 -o hardware/sim/tx-keying/results/2026-09-28-det-char -b hardware/sim/tx-keying/det_char.cir
tools/ltspice-batch.sh -t 600 -o hardware/sim/tx-keying/results/2026-09-28-det-char-biased -b hardware/sim/tx-keying/det_char_biased.cir
.venv/bin/python hardware/sim/tx-keying/keying_run.py detchar
.venv/bin/python hardware/sim/tx-keying/keying_run.py deck a4 asis     # and a5; then sweep0, fix, sweep1, sens for each
.venv/bin/python hardware/sim/tx-keying/keying_run.py summary
.venv/bin/python hardware/sim/tx-keying/keying_run.py replot a5 fix    # re-analyse an existing .raw, no LTspice
```

Exit status (revision 2, INSP-116 finding-11): 0 when the run's FAIL states equal those recorded for its run id
in `expected_states.json`; 3 when a criterion fails unexpectedly or an expected FAIL passes (both printed and
written to `result.json` key `expected_state_check`); 2 on an LTspice wrapper error. `summary` exits 3 if the
feedforward PWM at 122 kHz fails REQ-TX-006, a loop phase margin is under 45 degrees, or any run is not as
expected. `deck FIN VAR --accept` records the states (refused if an element-3-to-8 criterion of `fix` or `sweep1`
fails). The `sens` deck takes about 4 to 6 min of LTspice. The `setpoint` criterion (top power within 0.5 dB of
the setpoint) is this analysis's model-health check, not a requirement.

Conditions of every keying run: 50 WPM continuous dits (24 ms on, 24 ms off, 8 elements; spectrum over
elements 3 to 8, an integer number of periods; time checks on every element 3 to 8, and on element 1 when the
deck saves it), envelope settings 3, 5 and 8 ms (10-to-90 %), key-down sequence of TS-012 section 7.3 (relay
command at t0, contact closed 7.5 ms, CLK1 and GVA-84+ bias at 8 ms, ramp start 10 ms after key-down, drive
gated 1 ms after the ramp end). Revision 1: power steps 0.5, 1, 2 and 5 W (REQ-SYS-011, REQ-SYS-012,
REQ-SYS-064) and packs 6.4, 7.4 and 8.4 V (TC-TX-005), drain after key-down sag A5 5.5 / 6.7 / 7.9 V and
A4 6.1 / 7.1 / 8.1 V; the setpoint is limited at a low pack to 90 % of what the PA makes (A5 4.0 W at 6.4 V;
A4 2.8 W at 6.4 V and 3.9 W at 7.4 V). A threshold corner VSH moves the simulated PA curve against the nominal
firmware feedforward table (VSH < 0: earlier onset).

## Runs

| Run | What | Result (details in the run's `result.json`) |
|---|---|---|
| `2026-09-28-det-char` | TS-012 detector law at 146 MHz (0.0625 ns Gear; convergence checked) | Square law below about 1 V peak at the load (10 mW); the output equals the 10.6 mV idle-bias offset at 1.70 V peak (-22.4 dB re 5 W) and the 4.5 mV MCP6002 offset at 1.23 V (-25.2 dB): the loop cannot see the bottom 22 to 25 dB of the envelope |
| `2026-09-28-det-char-biased` | Biased detector law at 146 MHz (0.25 ns Gear) | About 21 dB more output in the square-law region; the 4.5 mV offset is reached at 0.37 V (-35.5 dB) |
| (revision 0, superseded) `2026-09-28-a4-asis` | A4, loop as written, 6 runs | **FAIL** every run: rise 1.6 to 7.5 ms against 3/5/8 ms, shape error 10 to 19 %, 26 dB bandwidth up to 417 Hz (3 ms, 6.1 V), worst cell beyond 750 Hz -49.8 dB, level at the drive gate -3.4 to +2.5 dBm (tail the loop cannot see), 3.2 W top at 6.1 V against the 5 W setpoint (integrator wound to the rail) |
| (revision 0, superseded) `2026-09-28-a5-asis` | A5, loop as written, 6 runs | **FAIL** every run, worse than A4: rise 1.3 to 5.7 ms, shape error 18 to 27 %, 26 dB bandwidth up to 542 Hz, worst cell -48.3 dB, level at the gate +5.3 to +9.9 dBm; VGG is about 2.1 V at the gate, not under 1.2 V as TS-012 states |
| (revision 0, superseded) `2026-09-28-a4-mitig` | A4, mitigated loop, 30 runs (5 corners) | PASS every keying criterion at every corner: rise and fall within 0.06 ms of the setting, shape error at most 2.5 %, 26 dB bandwidth 292 / 208 / 125 Hz, worst cell beyond 750 Hz -67.2 dB, no overshoot; FAIL REQ-TX-014 on the gate-off leakage estimate (-19.5 dBm, Crss path) |
| (revision 0, superseded) `2026-09-28-a5-mitig` | A5, mitigated loop, 30 runs (5 corners) | PASS every keying criterion at every corner with less margin than A4: rise 3.29 ms at the 3 ms setting at the -0.1 V threshold corner (+9.7 %, REQ-TX-005 limit 10 %), shape error at most 3.3 %, worst cell -64.1 dB; REQ-TX-014 not shown (modelled leakage -17.5 dBm at 30 dB module isolation; the datasheet's "up to 60 dB" would give -47 dBm) |
| (revision 0, superseded) `2026-09-28-summary` | Worst cases of the four runs, PWM carrier ripple (analytic), loop margin (analytic) | `summary.png`, `pwm_ripple.png`, `summary.json`: the feedforward PWM at 30.5 kHz puts carrier sidebands at -43 dBc (A5) and -50 dBc (A4): it must run at 122 kHz (10-bit) or take a third pole; loop phase margin at least 75 degrees |
| (revision 1, superseded) `2026-09-28-r1-a4-asis` | A4, loop as written, 6 runs (5 W, 6.4 and 8.4 V) | **FAIL** every run: 10-90 error -45 to +16 %, shape error 10 to 19 %, 26 dB bandwidth up to 417 Hz, worst cell -49.8 dB, level at the gate -3.4 to +2.5 dBm, 3.22 W top at 6.4 V against 5 W (unchanged from revision 0: A4 table unchanged) |
| (revision 1, superseded) `2026-09-28-r1-a5-asis` | A5, loop as written, 6 runs, digitized table | **FAIL** every run, worse than A4: 10-90 error -59 to -31 %, shape error 18 to 29 %, 26 dB bandwidth up to 583 Hz, worst cell -46.9 dB, level at the gate +5.2 to +8.0 dBm, 4.34 W top at 6.4 V |
| (revision 1, superseded) `2026-09-28-r1-a4-sweep0` | A4, revision 0 mitigated design, VSH -0.30 to +0.30 V, 0.5 and 5 W, 7.4 V, 78 runs | Tolerable window (all criteria, interpolated): **0.5 W -0.079 to +0.111 V**, 5 W -0.207 to beyond +0.30 V. Reproduces the review: -0.1 V at 0.5 W gives rise 3.38 ms at 3 ms (+12.7 %) and 5.53 ms at 5 ms |
| (revision 1, superseded) `2026-09-28-r1-a5-sweep0` | A5, same, 78 runs | Window **0.5 W -0.053 to +0.067 V**, 5 W -0.115 to +0.197 V. Reproduces the review: -0.1 V at 0.5 W gives rise 3.40 / 5.68 / 9.01 ms and shape 6.2 %; +0.1 V gives 2.57 ms |
| (revision 1, superseded) `2026-09-28-r1-a4-sweep1` | A4, revision 1 design, VSH -0.30 to +0.30 V, 4 steps, 7.4 V, 156 runs | Elements 3 to 8 (held trim): **PASS over the whole sweep** at every step. Element 1 (trim from mid-rail): window -0.168 to +0.211 V (worst step, 2 W) |
| (revision 1, superseded) `2026-09-28-r1-a5-sweep1` | A5, same, 156 runs | Elements 3 to 8: **PASS over the whole sweep**. Element 1: window **-0.084 to +0.137 V** (2 W), about half of A4's |
| (revision 1, superseded) `2026-09-28-r1-a4-fix` | A4, revision 1 design, 108 runs (4 steps x 3 packs x 3 settings x nominal and the compensated-budget corners -0.164 V / +1 mV and +0.086 V / -1 mV) | Elements 3 to 8 PASS every keying criterion in every run (10-90 error at most 2.2 %, shape at most 0.9 %, 26 dB bandwidth 292 / 208 / 125 Hz, worst cell -69.1 dB); element 1 PASS REQ-TX-005 in every run (at most +6.1 %), TC-SYS-013 shape 5.05 and 5.1 % in 2 runs (3 ms, 2 W, -0.164 V, 6.4 and 7.4 V); REQ-TX-014 FAIL (leakage estimate -19.5 dBm) |
| (revision 1, superseded) `2026-09-28-r1-a5-fix` | A5, same, 108 runs | Elements 3 to 8 PASS every keying criterion in every run (at most 1.9 %, shape 0.9 %, worst cell -69.4 dB, VGG at most 3.14 V); element 1 **FAIL** in 18 runs, every one at the -0.164 V corner (rise +14 to +18 %, shape up to 7.2 %); REQ-TX-014 not shown (-17.5 dBm modelled) |
| (revision 1, superseded) `2026-09-28-r1-summary` | Worst cases of the r1 runs, windows against the threshold budgets, PWM carrier ripple, loop margin | `summary.png`, `windows.png`, `pwm_ripple.png`, `summary.json`: loop phase margin at least 58 degrees with the +7 dB tap (crossover up to 4.1 kHz). Correction (INSP-116 finding-10): this row said "PWM result unchanged from revision 0", which was wrong: with the digitized A5 table the ripple is A5 -40.6 / -58.1 / -76.1 dBc at 30.5 / 61 / 122 kHz (slope 59.2 V/V), so 61 kHz fails for A5 |
| `2026-09-28-r2-a4-asis`, `2026-09-28-r2-a5-asis` | Loop as written, revision 2 rerun | Byte-identical `result.csv` to r1 (same decks): **FAIL** as in r1. Expected states recorded |
| `2026-09-28-r2-a4-sweep0`, `2026-09-28-r2-a5-sweep0` | Revision 0 design sweep, revision 2 rerun | Identical to r1: windows at 0.5 W A4 -0.079 / +0.111 V, A5 -0.053 / +0.067 V (**FAIL** against the budgets); `window.png` redrawn with the revision 2 budget bands |
| `2026-09-28-r2-a4-sweep1`, `2026-09-28-r2-a5-sweep1` | Revision 1 design sweep, revision 2 rerun | Identical to r1: elements 3 to 8 **PASS over the whole sweep**; element 1 window A4 -0.168 / +0.211, A5 -0.084 / +0.137 V (0.05 V grid) |
| `2026-09-28-r2-a4-fix` | A4, revision 1 design, 180 runs (4 steps x 3 packs x 3 settings x nominal, compensated -0.179 V / +1 mV and +0.096 V / -1 mV, stored-trim -0.107 V / +1 mV and +0.190 V / -1 mV) | Elements 3 to 8 PASS every keying criterion in every run (10-90 error at most 2.2 %, shape 0.9 %, worst cell -69.1 dB, VGS at most 2.60 V). Element 1: **PASS in all 72 stored-trim corner runs** (at most 6.6 %, shape 4.8 %); **FAIL in 5 of 36 compensated-low runs** (3 ms, 0.5 and 2 W; up to 16.9 %, shape 5.5 %): the stored trim is needed for A4 too. REQ-TX-014 FAIL (leakage estimate -19.5 dBm) |
| `2026-09-28-r2-a5-fix` | A5, same, 180 runs (compensated -0.171 / +0.099 V, stored-trim -0.110 / +0.182 V) | Elements 3 to 8 PASS every keying criterion (at most 1.9 %, shape 0.9 %, worst cell -69.2 dB, VGG at most 3.24 V). Element 1: **FAIL in 17 of 72 stored-trim corner runs** (up to 13.5 %, shape 6.2 %) and 18 of 36 compensated-low runs (up to 18.9 %, shape 7.5 %). REQ-TX-014 not shown (-17.5 dBm modelled) |
| `2026-09-28-r2-a4-sens` | A4, element 1, 2604 runs, 0.02 V | Windows (worst over steps; interpolated, grid edges in the json): nominal **-0.169 / +0.211 V**; offset +/-1 mV -0.163 / +0.205; pack 6.4 V -0.170 / +0.213; 8.4 V -0.171 / +0.213; 65 dB/V -0.163 / +0.267; 150 dB/V -0.130 / +0.172. `sens_curves.png`, `sens_windows.png` |
| `2026-09-28-r2-a5-sens` | A5, same | Nominal **-0.085 / +0.137 V**; offset -0.080 / +0.132; 6.4 V -0.083 / +0.135; 8.4 V -0.084 / +0.134; 65 dB/V -0.118 / +0.149; 150 dB/V -0.064 / +0.118. A4/A5 width ratio 1.6 to 1.8 in every case |
| `2026-09-28-r2-summary` | Worst cases of the r2 runs (rev. 1 design split into stored-trim and compensated corners), element-1 windows of every case against every budget, PWM carrier ripple, loop margin, design-rule and expected-state checks | `summary.png`, `windows.png`, `pwm_ripple.png`, `summary.json`. Stored-trim worst-case sum: **A4 PASS** (margin 0.021 V; 0.015 V with the offset; holds up to about 127 dB/V), **A5 FAIL** (-0.045 V; fails in every case). Compensated worst-case sum: both FAIL (A4 -0.009 V). PWM feedforward sidebands A5 -40.6 / **-58.1 (61 kHz FAIL by 1.9 dB)** / -76.1 dBc, A4 -49.8 / -67.3 / -85.3 dBc (slopes 59.2 and 20.6 V/V); 122 kHz rule PASS; phase margin at least 58.4 degrees; every run AS EXPECTED; exit 0 |

Model limitations (the record's section 7 has the full list): the threshold budget terms are estimates
(record section 3.2; revision 2 takes the die temperature terms per finalist from thermal-ts012.md sections 4.1
and 8); envelope-domain PA model from datasheet graph reads (no AM-to-PM, no memory, no harmonic content), sub-threshold slope below the graphs an estimate
(100 dB/V; 65 and 150 dB/V run as cases in `sens`), detector diode parameters of the HSMS-280x family used for the 1N5711W, gate-off leakage an
estimate, PWM carrier ripple analytic (the decks carry the duty staircase only).
