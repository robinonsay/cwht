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
| `keying_run.py` | Generator, runner and checker: writes the keying decks, runs them through `tools/ltspice-batch.sh`, parses the `.raw` with spicelib, computes rise and fall, shape error, overshoot, 26 dB bandwidth, 10 Hz sideband cells and key-up level, draws the plots and writes `result.json` and `result.csv`; also the analytic PWM carrier ripple and loop margin |
| `keying_a4_asis.cir`, `keying_a5_asis.cir` | Envelope-domain decks of the loop as TS-012 revision 4 section 7.3 describes it (generated) |
| `keying_a4_mitig.cir`, `keying_a5_mitig.cir` | Envelope-domain decks of the mitigated loop, with corners (generated) |
| `results/<run-id>/` | One directory per run (owner rule): deck, LTspice `.log`, `.raw`, `.op.raw`, wrapper output, `result.json` and `result.csv` (pass/fail and numbers), PNG plots, the script as run |

Run (LTspice only through the accredited wrapper, ACC-LTSPICE-001; each deck takes about 10 s once the
wrapper lock is free):

```
tools/ltspice-batch.sh -t 600 -o hardware/sim/tx-keying/results/2026-09-28-det-char -b hardware/sim/tx-keying/det_char.cir
tools/ltspice-batch.sh -t 600 -o hardware/sim/tx-keying/results/2026-09-28-det-char-biased -b hardware/sim/tx-keying/det_char_biased.cir
.venv/bin/python hardware/sim/tx-keying/keying_run.py detchar
.venv/bin/python hardware/sim/tx-keying/keying_run.py deck a4 asis     # and a5 asis, a4 mitig, a5 mitig
.venv/bin/python hardware/sim/tx-keying/keying_run.py summary
.venv/bin/python hardware/sim/tx-keying/keying_run.py replot a5 mitig    # re-analyse an existing .raw, no LTspice
```

Conditions of every keying run: 50 WPM continuous dits (24 ms on, 24 ms off, 8 elements, analysis over
elements 3 to 8, an integer number of periods), envelope settings 3, 5 and 8 ms (10-to-90 %), drain voltage
at the low and high pack ends after key-down sag (A5 5.5 and 7.9 V, A4 6.1 and 8.1 V), key-down sequence
of TS-012 section 7.3 (relay command at t0, contact closed 7.5 ms, CLK1 and GVA-84+ bias at 8 ms, ramp start
10 ms after key-down, drive gated 1 ms after the ramp end).

## Runs

| Run | What | Result (details in the run's `result.json`) |
|---|---|---|
| `2026-09-28-det-char` | TS-012 detector law at 146 MHz (0.0625 ns Gear; convergence checked) | Square law below about 1 V peak at the load (10 mW); the output equals the 10.6 mV idle-bias offset at 1.70 V peak (-22.4 dB re 5 W) and the 4.5 mV MCP6002 offset at 1.23 V (-25.2 dB): the loop cannot see the bottom 22 to 25 dB of the envelope |
| `2026-09-28-det-char-biased` | Biased detector law at 146 MHz (0.25 ns Gear) | About 21 dB more output in the square-law region; the 4.5 mV offset is reached at 0.37 V (-35.5 dB) |
| `2026-09-28-a4-asis` | A4, loop as written, 6 runs | **FAIL** every run: rise 1.6 to 7.5 ms against 3/5/8 ms, shape error 10 to 19 %, 26 dB bandwidth up to 417 Hz (3 ms, 6.1 V), worst cell beyond 750 Hz -49.8 dB, level at the drive gate -3.4 to +2.5 dBm (tail the loop cannot see), 3.2 W top at 6.1 V against the 5 W setpoint (integrator wound to the rail) |
| `2026-09-28-a5-asis` | A5, loop as written, 6 runs | **FAIL** every run, worse than A4: rise 1.3 to 5.7 ms, shape error 18 to 27 %, 26 dB bandwidth up to 542 Hz, worst cell -48.3 dB, level at the gate +5.3 to +9.9 dBm; VGG is about 2.1 V at the gate, not under 1.2 V as TS-012 states |
| `2026-09-28-a4-mitig` | A4, mitigated loop, 30 runs (5 corners) | PASS every keying criterion at every corner: rise and fall within 0.06 ms of the setting, shape error at most 2.5 %, 26 dB bandwidth 292 / 208 / 125 Hz, worst cell beyond 750 Hz -67.2 dB, no overshoot; FAIL REQ-TX-014 on the gate-off leakage estimate (-19.5 dBm, Crss path) |
| `2026-09-28-a5-mitig` | A5, mitigated loop, 30 runs (5 corners) | PASS every keying criterion at every corner with less margin than A4: rise 3.29 ms at the 3 ms setting at the -0.1 V threshold corner (+9.7 %, REQ-TX-005 limit 10 %), shape error at most 3.3 %, worst cell -64.1 dB; REQ-TX-014 not shown (modelled leakage -17.5 dBm at 30 dB module isolation; the datasheet's "up to 60 dB" would give -47 dBm) |
| `2026-09-28-summary` | Worst cases of the four runs, PWM carrier ripple (analytic), loop margin (analytic) | `summary.png`, `pwm_ripple.png`, `summary.json`: the feedforward PWM at 30.5 kHz puts carrier sidebands at -43 dBc (A5) and -50 dBc (A4): it must run at 122 kHz (10-bit) or take a third pole; loop phase margin at least 75 degrees |

Model limitations (the record's section 7 has the full list): envelope-domain PA model from datasheet
graph reads (no AM-to-PM, no memory, no harmonic content), sub-threshold slope below the graphs an estimate
(100 dB/V), detector diode parameters of the HSMS-280x family used for the 1N5711W, gate-off leakage an
estimate, PWM carrier ripple analytic (the decks carry the duty staircase only).
