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
| `keying_a4_fix.cir`, `keying_a5_fix.cir` | Revision 1 design: 4 steps x 3 packs x 3 settings x 3 record corners, 108 runs (generated) |
| `keying_a4_sweep1.cir`, `keying_a5_sweep1.cir` | Revision 1 design, threshold sweep -0.30 to +0.30 V, 4 steps, 7.4 V pack (generated) |
| `keying_a4_mitig.cir`, `keying_a5_mitig.cir` | Revision 0 mitigated decks (5 W only, +/-0.1 V corners), superseded; kept because the revision 0 runs used them |
| `results/<run-id>/` | One directory per run (owner rule): deck, LTspice `.log`, `.raw`, `.op.raw`, wrapper output, `result.json` and `result.csv` (pass/fail and numbers), PNG plots, the script as run |

Run (LTspice only through the accredited wrapper, ACC-LTSPICE-001; a 108 to 156-step deck takes 30 to 60 s
of LTspice once the wrapper lock is free, plus about 1 min of analysis):

```
tools/ltspice-batch.sh -t 600 -o hardware/sim/tx-keying/results/2026-09-28-det-char -b hardware/sim/tx-keying/det_char.cir
tools/ltspice-batch.sh -t 600 -o hardware/sim/tx-keying/results/2026-09-28-det-char-biased -b hardware/sim/tx-keying/det_char_biased.cir
.venv/bin/python hardware/sim/tx-keying/keying_run.py detchar
.venv/bin/python hardware/sim/tx-keying/keying_run.py deck a4 asis     # and a5; then sweep0, fix, sweep1 for each
.venv/bin/python hardware/sim/tx-keying/keying_run.py summary
.venv/bin/python hardware/sim/tx-keying/keying_run.py replot a5 fix    # re-analyse an existing .raw, no LTspice
```

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
| `2026-09-28-r1-a4-asis` | A4, loop as written, 6 runs (5 W, 6.4 and 8.4 V) | **FAIL** every run: 10-90 error -45 to +16 %, shape error 10 to 19 %, 26 dB bandwidth up to 417 Hz, worst cell -49.8 dB, level at the gate -3.4 to +2.5 dBm, 3.22 W top at 6.4 V against 5 W (unchanged from revision 0: A4 table unchanged) |
| `2026-09-28-r1-a5-asis` | A5, loop as written, 6 runs, digitized table | **FAIL** every run, worse than A4: 10-90 error -59 to -31 %, shape error 18 to 29 %, 26 dB bandwidth up to 583 Hz, worst cell -46.9 dB, level at the gate +5.2 to +8.0 dBm, 4.34 W top at 6.4 V |
| `2026-09-28-r1-a4-sweep0` | A4, revision 0 mitigated design, VSH -0.30 to +0.30 V, 0.5 and 5 W, 7.4 V, 78 runs | Tolerable window (all criteria, interpolated): **0.5 W -0.079 to +0.111 V**, 5 W -0.207 to beyond +0.30 V. Reproduces the review: -0.1 V at 0.5 W gives rise 3.38 ms at 3 ms (+12.7 %) and 5.53 ms at 5 ms |
| `2026-09-28-r1-a5-sweep0` | A5, same, 78 runs | Window **0.5 W -0.053 to +0.067 V**, 5 W -0.115 to +0.197 V. Reproduces the review: -0.1 V at 0.5 W gives rise 3.40 / 5.68 / 9.01 ms and shape 6.2 %; +0.1 V gives 2.57 ms |
| `2026-09-28-r1-a4-sweep1` | A4, revision 1 design, VSH -0.30 to +0.30 V, 4 steps, 7.4 V, 156 runs | Elements 3 to 8 (held trim): **PASS over the whole sweep** at every step. Element 1 (trim from mid-rail): window -0.168 to +0.211 V (worst step, 2 W) |
| `2026-09-28-r1-a5-sweep1` | A5, same, 156 runs | Elements 3 to 8: **PASS over the whole sweep**. Element 1: window **-0.084 to +0.137 V** (2 W), about half of A4's |
| `2026-09-28-r1-a4-fix` | A4, revision 1 design, 108 runs (4 steps x 3 packs x 3 settings x nominal and the compensated-budget corners -0.164 V / +1 mV and +0.086 V / -1 mV) | Elements 3 to 8 PASS every keying criterion in every run (10-90 error at most 2.2 %, shape at most 0.9 %, 26 dB bandwidth 292 / 208 / 125 Hz, worst cell -69.1 dB); element 1 PASS REQ-TX-005 in every run (at most +6.1 %), TC-SYS-013 shape 5.05 and 5.1 % in 2 runs (3 ms, 2 W, -0.164 V, 6.4 and 7.4 V); REQ-TX-014 FAIL (leakage estimate -19.5 dBm) |
| `2026-09-28-r1-a5-fix` | A5, same, 108 runs | Elements 3 to 8 PASS every keying criterion in every run (at most 1.9 %, shape 0.9 %, worst cell -69.4 dB, VGG at most 3.14 V); element 1 **FAIL** in 18 runs, every one at the -0.164 V corner (rise +14 to +18 %, shape up to 7.2 %); REQ-TX-014 not shown (-17.5 dBm modelled) |
| `2026-09-28-r1-summary` | Worst cases of the r1 runs, windows against the threshold budgets, PWM carrier ripple, loop margin | `summary.png`, `windows.png`, `pwm_ripple.png`, `summary.json`: loop phase margin at least 58 degrees with the +7 dB tap (crossover up to 4.1 kHz); PWM result unchanged from revision 0 |

Model limitations (the record's section 7 has the full list): the threshold budget terms are estimates
(record section 3.2); envelope-domain PA model from datasheet graph reads (no AM-to-PM, no memory, no harmonic content), sub-threshold slope below the graphs an estimate
(100 dB/V), detector diode parameters of the HSMS-280x family used for the 1N5711W, gate-off leakage an
estimate, PWM carrier ripple analytic (the decks carry the duty staircase only).
