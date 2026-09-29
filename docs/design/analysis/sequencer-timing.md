# Sequencer timing: key-down and key-up sequence, T/R relay drive and hold, ICD-TX-SW timing table (WP-PDR-23a)

| Field | Value |
|---|---|
| Product | `docs/design/analysis/sequencer-timing.md` (analysis note, `analysis_kind`: timing, worst-case; simulation of the relay coil drive; reduced-order electromechanical model of the relay), **revision 0**, 2026-09-29 |
| Work package | WP-PDR-23a (`docs/plan/pdr-work-plan.md` revision 6, section 3.0 row 23 and section 4.1): "the key-down and key-up sequence with pass criteria (ramp start at least 10 ms after the relay command, lead-in at most 12 ms, key-to-RF at most 15 ms, clamps held and integrator parked until ramp start); the D-5 relay hold; `sequencer-timing.md` with the ICD-TX-SW timing table and its render". TS-012 revision 8 section 8.12 adds "the frequency check finished before PA_EN". WP-PDR-23b (NanoVNA isolation plan, stuck-relay cases, the G6 values) is not in this record |
| Author | Claude, analysis author invocation (RF designer role), 2026-09-29 |
| Status | Draft, frozen at F0 by the commit that adds it (rule C2), for independent review with its software assurance pair (SW-TXSEQ is safety-critical; plan WP-PDR-23: reviewer plus SA). Proposes values and design changes; it edits no requirement, hazard, ICD or trade-study file (plan section 5.3) |
| Design basis | TS-012 revision 8 (`bb5dee7`): section 7.3 "Revision 6: key-down sequence, frequency check and PA permit", section 8.1, section 8.3 rows 2 (G5V-2-DC5) and 12 (2N3904BU, relay driver), section 8.12 row WP-PDR-23, section 8.14 D-5, D-11, D-17, D-18; decision A5 (section 10) |
| Inputs from records under review | `frequency-budget.md` revision 2 (`7593cea`, WP-PDR-20a; INSP-056 iteration 3 and INSP-111 iteration 2 NEEDS CHANGES at this date): the C6 write time and the lock-gated FC0 start. `pa-permit-gate-d18.md` revision 0 (`078f2f7`, WP-PDR-22; not yet reviewed): the D-18 gate turn-on time. Each use is marked in section 2; a change in either record is re-checked in the delta iteration |
| Decks, scripts and results | `hardware/sim/tx-seq/` (README.md there lists every run). Runs `2026-09-29-s1-drive`, `2026-09-29-s2-coil`, `2026-09-29-s3-operate`, `2026-09-29-s4-sequence` in `hardware/sim/tx-seq/results/`. Timing diagram: `docs/reviews/PDR/figures/timing-diagram.png` (written by s4) |
| Tool | LTspice 26.0.2 through `tools/ltspice-batch.sh` only (ACC-LTSPICE-001); `.raw` read with spicelib in the repo venv; Python 3.13 with numpy, scipy (solve_ivp) and matplotlib |
| Evidence status | **Developer evidence** (05 section 9.1): `seq_run.py` and `relay_model.py` have no TV record. The relay model is an estimate anchored to datasheet limits (section 3.3). Every criterion state is compared with `expected_states.json` by `seq_run.py all --expect` (exit 0 on 2026-09-29) |
| Serves | REQ-SYS-160, REQ-SYS-161 (TBRs close at PDR); REQ-SYS-120, REQ-SYS-182 ordering; 07 section 14.2 rows b, c and h (the T/R and PA_EN order); HZ-004 K8 timing; TS-012 D-5; inputs to WP-PDR-23b for REQ-SYS-004, 036, 044, 159 and REQ-SW-KEYER-032; the ICD-TX-SW timing table that WP-PDR-36a writes; TC-SYS-102, TC-SYS-030, TC-SYS-024 methods |

## Summary

- **The sequence meets every criterion the plan names, as a schedule** (section 4.1): the ramp starts 10.000 ms after the T/R command (K1), the lead-in is 9.980 to 10.043 ms on every element against 12 ms, equal within 0.063 ms (K2, K2b), straight-key contact to RF rise is 13.043 ms against 15 ms (K3), the frequency check ends at t0 + 7.097 ms before PA_EN at t0 + 7.5 ms (K5), PA_EN precedes TX_KEY at t0 + 8 ms (K6), and the VGG clamp and the parked integrator hold until the ramp (K4).
- **The relay does not close inside that lead-in with the drive TS-012 lists** (section 4.2). The 7 ms operate time the 10 ms lead-in rests on is a datasheet value at the rated 5.0 V on a coil at 23 C. The G5V-2's must-operate voltage rises with coil temperature, about 0.39 % per K, because the pick-up current is fixed. In the PA bay (relay ambient 61.4 C at the duty limit and 67.1 C continuous, `thermal-ts012.md`):
  - **Option A, as listed** (standard DC5 coil on the 5 V bus, 2N3904 driver): a worst-case unit (must-operate at the datasheet's 75 % maximum) is not guaranteed to pull in at all at a 75 C coil, and needs about 12.6 ms (nominal model set) at a 49 C coil at 4.75 V (K1b-A **FAIL**).
  - **Option B** (the same coil, AO3400A driver): 9.65 ms at 49 C, 14.1 ms at 75 C, no pull-in in some model sets at 75 C (K1b-B **FAIL**).
  - **Options C and D** (the high-sensitivity **G5V-2-H1 DC5** coil fed from the switched pack rail, with the BOM's 2N3904 or an AO3400A): at most 7.11 ms at 6.35 V and an 85 C coil over the whole model band, 2.39 ms inside the ramp start with the 0.5 ms bounce (K1b-C, K1b-D **PASS**, estimate).
- **D-5 relay hold** (section 4.3). With the standard coil, a hold at 63 % of the coil voltage (the thermal note's assumption) is below the worst unit's must-operate current (0.64 x); the datasheet does not guarantee it and the model band drops it out in some sets (K15-B **OPEN**, bench). With the H1 coil, a hold at the rated 5.0 V average by 25 kHz PWM from the pack is guaranteed by the datasheet (1.07 x the worst unit's must-operate current at an 85 C coil; K15-D PASS), dissipates about 0.15 W against 0.5 W, and the H1 is rated to 70 C ambient against the standard coil's 65 C. Pull-in at the full pack is 168 % of rated for 25 ms against the H1's 180 % maximum at 23 C; its derating curve at 70 C is a graph read at the gate (K19 **OPEN**).
- **Recommended design change** (section 6.1): D-5 takes its own second option, the G5V-2-H1 DC5 coil, fed from the switched pack rail, pulled in at 100 % for 25 ms and held at a 5.0 V average by a 25 kHz PWM whose duty follows the pack voltage, with a plain freewheel diode rated for the coil current (the BOM has none; the 1N5711W is not one). The 2N3904 driver can stay (option C).
- **Other findings** (section 6.2):
  - The TS-012 interval-13 fallback (check at t0 + 11 ms, ramp at t0 + 11.5 ms) does not fit: the count alone ends at t0 + 11.19 ms on the 4.096 ms bound, and with PA_EN before a 2 ms TX_KEY lead the ramp would be at t0 + 13.19 ms, over 12 ms (K9 **FAIL**). It works only by letting PA_EN follow TX_KEY and taking the D-18 gate's 0.25 ms turn-on bound, with 0.06 ms to spare and no relock margin. WP-PDR-20a (RL-6) reached the same conclusion for the relock trigger.
  - The relock margin beyond the 1 ms allocation is 0.903 ms (K8), not the 3 ms of the TS-012 revisit condition; the latest lock-gated FC0 start is t0 + 1.903 ms (K8b), not the 2.0 ms of `frequency-budget.md` RL-4, which used a 4.0 ms interval.
  - REQ-SYS-160 holds only for a key bounce of at most 1.957 ms (sample-aligned worst case, K3b); REQ-SYS-159 (sidetone, 4 ms) only for 0.9 ms (K17). Both are conditions on the key for the WP-PDR-40 bounce capture.
  - 07 section 14.2 row j states the key-up response as "the envelope fall starts within the next 1 ms sample; PA_EN falls after the fall completes". With the constant lead-in of REQ-SYS-161 the fall starts one lead-in (10 ms) after the keyer edge, and with D-18 PA_EN stays high for the over while TX_KEY follows each element. The row needs restating (to WP-PDR-32 and 35, and the 07 owner).
- **Key-up and end of over** (section 4.4): with a 3-dit hang at 50 WPM the T/R is released 52.96 ms after the last TX_KEY low (K10, cold switching), so the REQ-SYS-044 floor of 3 dits holds against the relay and envelope timing (K11). The release takes at most 13.92 ms of the 50 ms of REQ-SYS-036 with the freewheel diode (K12, model band).
- **Proposed values** (section 7, to the owner only after this record is APPROVED, rule C10): REQ-SYS-160 keep 15 ms and REQ-SYS-161 keep 12 ms, with the design lead-in of 10 ms and the key-bounce condition stated; both conditional on the D-5 change or on bench measurement BM-2 of the fitted relay.

## 1. Question and scope

The question: does the A5 sequence of TS-012 section 7.3 (revision 6) meet its pass criteria, does the relay it relies on close inside the lead-in at every pull-in corner, how is the relay held at reduced power (D-5), and what timing table does ICD-TX-SW carry?

In scope:
- the first element of an over (the changeover), every later element, and the end of the over;
- the frequency check before PA_EN (D-17) and the PA permit (D-18) as timing, not as circuits;
- the T/R relay: coil drive, pull-in, hold and release, for four drive options;
- the fault path's RF-off timing (REQ-SYS-004) as an input to WP-PDR-23b.

Out of scope: the keying loop's envelope and spectrum (WP-PDR-22, `keying-ts012.md`), the D-18 gate circuit (`pa-permit-gate-d18.md`), the relay's RF isolation and stuck-relay cases (WP-PDR-23b), the Si5351A relock time itself (WP-PDR-20a, measurement M-1), the receiver's recovery after the relay releases (WP-PDR-19, TC-SYS-024).

Requirements and criteria checked (texts at HEAD, `docs/requirements/sys/requirements.json`):

| Id | Text (short) | How it is checked |
|---|---|---|
| Plan criterion 1 | ramp start at least 10 ms after the relay command | K1 schedule; K1a, K1b the physical basis (contacts made and bounce ended before the ramp) |
| REQ-SYS-161 | same lead-in of at most 12 ms (TBR) on every radiated element of an over | K2 (value), K2b (equality within the 0.5 ms of TC-SYS-102) |
| REQ-SYS-160 | RF rise within 15 ms (TBR) of each straight-key closure | K3; K3b the key-bounce condition |
| Plan criterion 4 | clamps held and integrator parked until ramp start | K4 |
| TS-012 rev 8 8.12 | frequency check finished before PA_EN | K5; K8, K8b, K9 the relock margin and the interval-13 fallback |
| REQ-SYS-120, D-18 | RF only with key-down and the permit; PA_EN before TX_KEY | K6, K7 |
| 07 section 14.2 rows b, c | T/R changes only while the envelope is below -20 dBc; PA_EN first, T/R last | K1b (key-down), K10 (key-up), FP-01 to FP-03 (fault) |
| D-5 | relay coil held at reduced power by PWM after pull-in, or the H1 coil | K13, K14, K15, K19 |
| REQ-SYS-036, 044, 004, 159 (23b values) | recovery 50 ms; hang 3 to 30 dits; RF off 20 ms; sidetone 4 ms | K12, K11, K16, K17 (inputs, no value proposed) |

## 2. Inputs

Class: R requirement; D datasheet; DD derived from datasheets; A allocation (a design value this note proposes); E estimate. `seq_run.py` holds every input in its `INPUTS` table and prints it into the s4 `result.json`.

| Input | Value | Class | Source |
|---|---|---|---|
| Key sampling; make filter | 1.000 ms; 2 consecutive closed samples, key-down asserted within 2 ms of the first closed sample | R | REQ-SW-KEYER-019, 020, 018 |
| Keyer test point after the T/R write | 0 to 20 us, same TIMER0 alarm service | A | this note |
| C6 changeover writes (MSNA first, CLK1 on, CLK0 and CLK2 off, PLL B parked), 400 kHz, no reg 177 reset | 0.650 ms | DD | `frequency-budget.md` rev 2 RL-2 (under review) |
| Writes plus PLL settle allocation | 1.0 ms after t0 | A | TS-012 7.3 rev 6; WP-PDR-20a M-1 confirms |
| FC0 interval 12; interval 13; FC0_DELAY | 4.096 ms; 8.192 ms ("1 us x 2**interval", the Table 582 wording, which bounds the 0.98 us device value); at most 7 clk_ref cycles, 0.6 us | D | RP2350 datasheet section 8.1.4, Tables 542 and 582 |
| Lock-status read, compare, PA_EN write | 2.0 ms | A | `frequency-budget.md` C-14 |
| G5V-2 operate time; release time | 7 ms max; 3 ms max (rated voltage, coil 23 C; both coils) | D | Omron G5V-2 datasheet, Characteristics (text in the web-fetch cache used for TS-012 revision 3) |
| G5V-2 must-operate; must-release | 75 % of rated max; 5 % min; at a coil temperature of 23 C | D | same, Ratings, notes 1 and 2 |
| Coils | DC5 standard: 100 mA, 50 ohm, about 500 mW, max 120 %; H1 DC5: 30 mA, 166.7 ohm, about 150 mW, max 180 %; +/-10 % at 23 C | D | same, Ratings |
| Ambient rating | standard -25 to 65 C; H1 -25 to 70 C | D | same, Characteristics |
| Bounce | 0.5 ms (0.3 to 0.5 ms read from the operate bounce-distribution graph, 12 VDC sample) | DD | TS-012 revision 3 graph read; used for the NC contact too (E) |
| Copper resistance coefficient | 0.00393 /K | R (handbook) | annealed copper at 20 C |
| Coil temperature at pull-in | 23 C (datasheet point); 49 C (nominal: 25 C outside, PA bay about +16 K, coil self-heating about +8 K); 75 C (45 C outside, relay ambient 61.4 C at the duty limit, plus up to 14 K of self-heating); 85 C (45 C continuous, 67.1 C, plus up to 18 K) | DD, E | `thermal-ts012.md` table (relay ambient A5); self-heating from a coil-to-ambient resistance of 40 to 80 K/W (E) at the hold power |
| 5 V bus | 4.75 to 5.25 V | D | LM2940 SNVS769J section 6.5 (TS-012 7.3) |
| Switched pack rail at pull-in | 6.35 V (6.4 V, the REQ-SYS-097 transmit floor, less about 0.05 V of feed drop in receive) to 8.4 V; 5.5 V lowest during key-down (0.9 V of feed drop at 2 A) | R, E | REQ-SYS-012, 097; TS-012 feed budget (0.26 to 0.45 ohm) |
| 2N3904 VCE(sat) | 0.30 V max at 50 mA, 5 mA base, used as a floor at every current; the LTspice model gives 0.04 to 0.11 V | D | onsemi 2N3904 datasheet; LTspice standard.bjt |
| AO3400A on-resistance at a 3.3 V gate | 29 to 32 mohm (VDMOS fit, class E; datasheet 48 mohm max at 2.5 V) | E, D | s1 check `mos_ron_range_mohm` |
| Freewheel diode | 1N4148 (LTspice model) in s2; in s3 a diode with no junction drop, the slowest decay | D, E | LTspice standard.dio |
| Lead-in L (T/R command to ramp start) | 10.0 ms | A | TS-012 7.3 |
| TX_KEY lead before each ramp; tail after each ramp | 2.0 ms; 1.0 ms | A | `keying-ts012.md` timing, TS-012 7.3 rev 6 |
| Driver supply and bias settled after the gate permits | 1.0 ms allocation | A | `pa-permit-gate-d18.md` rev 0: powered within 1.2 us, turn-on at most 0.25 ms (not yet reviewed) |
| Envelope reference PWM period (ramp-start quantisation) | 0.0427 ms (12 bit at clk_sys 96 MHz) | DD | TS-012 D-12 C1 |
| Ramp settings; speeds; hang | 3 to 8 ms; 5 to 50 WPM; 3 to 30 dits | R | REQ-SYS-014; REQ-SW-KEYER-015; REQ-SYS-044 |
| End-of-over ordering (PA_EN low, CLK1 off, prescaler off, T/R off) | within 0.5 ms | A | 07 section 14.2 row b order |
| REQ-SYS-036 share for the T/R release | 30 ms of 50 ms (the receiver keeps 20 ms) | A | this note, for WP-PDR-19 and 23b |
| Inhibit to PA_EN low; PA_EN low to RF off | 1.0 ms (A); 0.1 ms (E) | A, E | SW-SAFE service; D-18 gate in microseconds |
| D-5 pull-in time; hold PWM | 25 ms at 100 %; 25 kHz | A | this note |

## 3. Method

### 3.1 Sequence model (s4)

`seq_run.py s4` builds the key-down schedule of the first element of an over as event times after t0, the T/R drive write, and checks each criterion of section 1 as an inequality between events (K1 to K19). Per element, TX_KEY rises L - 2 ms after the keyer edge and falls 1 ms after the ramp ends; the ramp starts at the first envelope-PWM boundary at or after keyer edge + L. The end of the over is scheduled from the hang expiry. The relay's physical timing enters from s3. The s4 outputs are the criteria table, the ICD-TX-SW timing table (CSV and Markdown), the timing diagram and the budget and margin plots.

Detection worst case: the first sample after the first make comes at most 1 ms later, and key-down is asserted at most 2 ms after it (REQ-SW-KEYER-018), so t0 is at most 3 ms after the first make with no bounce. A bouncing key can open at every sample until the bounce ends at B, so t0 is at most B + 3 ms (K3b, K17).

### 3.2 Relay drive options and the LTspice runs (s1, s2)

| Option | Coil | Supply at the coil | Driver | Status |
|---|---|---|---|---|
| A | G5V-2 DC5 standard | 5 V bus, 4.75 to 5.25 V | 2N3904 (TS-012 8.3 row 12) | as TS-012 lists it |
| B | G5V-2 DC5 standard | 5 V bus | AO3400A (row 22 part) | driver change only |
| C | G5V-2-H1 DC5 | switched pack rail, 6.35 to 8.4 V | 2N3904 | D-5's second option, fed from the pack |
| D | G5V-2-H1 DC5 | switched pack rail | AO3400A | as C, MOSFET driver |

- **s1** (`drive_dc.cir`, DC sweep 4.5 to 8.6 V, 16 coil resistances x 2 driver temperatures): the coil current and the driver drop for both drivers from a 3.3 V GPIO. The drop fits at 70 C feed s3: 2N3904 0.0146 V + 0.49 ohm x i (then floored at the datasheet 0.30 V), AO3400A 0.031 ohm x i. Plot `s1-coil-current.png`: at an 85 C coil on a +10 % unit, the standard coil's current at 4.75 V is 69.4 mA (AO3400A) or 68.7 mA (2N3904 model) against the worst unit's 68.2 mA must-operate current; the H1's is 27.8 mA against 20.5 mA.
- **s2** (`coil_tran.cir`, 6 cases): pull-in rise to the must-operate current, 25 kHz hold PWM, and decay through the 1N4148 after the drive stops, with a fixed coil inductance (the open-gap value for the rise, the closed-gap value for the hold). The runs agree with the closed-form R-L results within 0.39 % (check `closed_form`). Hold ripple is at most 2.27 % (check `ripple`). Plot `s2-coil-transient.png`.

### 3.3 Relay electromechanical model (s3)

The datasheet gives limits, not dynamics. `relay_model.py` is a one-magnetic-circuit model (flux linkage L(g) i with L falling from Lc at the closed gap to Lo = Lc / rho at the open gap, co-energy force, a preloaded spring whose force rises by sigma from open to closed, armature mass m, stops at both ends). It is anchored to the datasheet as follows:
1. The spring preload is set so that the armature starts to move at the must-operate current of a worst-case unit, Ipu = 0.75 x 5.0 V / R23. That current does not change with temperature; the coil resistance does, which is why the must-operate voltage rises about 0.39 % per K.
2. m is solved so that the operate time at 5.0 V on a 23 C coil is the datasheet's 7.0 ms (check `calibration_ref_7ms`, deviation under 0.01 ms). The unit is therefore at both datasheet limits at once, the worst case the datasheet allows.
3. Second anchor: the release time with no freewheel path (the datasheet's test condition) must be at most 3 ms. Parameter sets that fail it are rejected.

The three unknowns form a class E band: open-gap time constant tau_o = Lo / R23 of 0.6, 1.2 and 2.4 ms, rho of 2, 3 and 4, sigma of 0.5, 1 and 2 (27 sets per coil). Of these, 3 cannot reach 7 ms at all and 11 fail the release anchor; **13 per coil are accepted**, among them the nominal set (1.2 ms, 3, 1). The accepted sets give a no-diode release of 1.13 to 2.90 ms and a release-to-pick-up current ratio of 0.31 to 0.87. The model's no-motion limit reproduces the s2 LTspice rise times within 0.25 % (check `model_vs_ltspice_rise`).

For each option, supply (min, nominal, max) and coil-temperature corner, s3 runs every accepted set and reports the nominal set and the band. It also sweeps the coil temperature from 20 to 100 C at the lowest supply, and runs the release from the hold current at an 85 C coil.

### 3.4 Checks

Every stage asserts its checks (README): s1 step count and driver ranges; s2 closed forms and ripple; s3 calibration, accepted-set count, the nominal set, the LTspice cross-check; s4 schedule order and the upstream checks. On 2026-09-29 all 13 checks pass. `seq_run.py all` exits 1 (checks pass; K1b-A, K1b-B and K9 FAIL, K15-B and K19 OPEN, as this note reports); `seq_run.py all --expect` exits 0.

## 4. Results

### 4.1 Key-down schedule, first element of an over (s4; interval 12)

| Event (after t0, the T/R write) | Time (ms) |
|---|---|
| keyer test point edge | 0 to 0.02 |
| C6 writes done | 0.650 |
| PLL settled, FC0 starts (allocation; lock-gated start at the first LOL_A = 0 read, latest t0 + 1.903) | 1.0 |
| FC0 interval 12 ends | 5.097 |
| lock read and compare done | 7.097 |
| "T/R in TX and settled" true (7 + 0.5 ms) | 7.5 |
| PA_EN high | 7.5 |
| TX_KEY high: D-18 gate permits, VGG clamp off, GVA-84+ on | 8.0 |
| driver settled (allocation) | 9.0 |
| reference clamp released, ramp starts | 10.000 to 10.043 |
| hold PWM | 25 |

Plots: `docs/reviews/PDR/figures/timing-diagram.png` panel (a); `s4-keydown-budget.png` panel (a).

### 4.2 Relay pull-in at the corners (s3)

Ratio of the worst unit's must-operate voltage to the voltage at the coil (above 1: no guaranteed pull-in):

| Option | 23 C coil | 49 C | 75 C | 85 C |
|---|---|---|---|---|
| A (4.75 V less 0.30 V) | 0.843 | 0.929 | **1.015** | **1.048** |
| B (4.75 V) | 0.790 | 0.871 | 0.951 | 0.982 |
| C (6.35 V less 0.30 V) | 0.620 | 0.683 | 0.747 | 0.771 |
| D (6.35 V) | 0.591 | 0.651 | 0.711 | 0.735 |

Operate time to contact make at the lowest supply, worst-case unit (nominal set; band of the 13 accepted sets in brackets; "none" = no pull-in):

| Option | 23 C coil | 49 C | 75 C | 85 C |
|---|---|---|---|---|
| A | 9.11 (9.01 to 10.69) | 12.59 (11.80 to none) | none | none |
| B | 7.77 (7.75 to 8.13) | 9.65 (9.27 to 12.39) | 14.10 (12.69 to none) | 19.56 (16.57 to none) |
| C | 5.20 (4.87 to 5.23) | 5.74 (5.47 to 5.75) | 6.44 (6.10 to 6.61) | 6.77 (6.40 to 7.11) |
| D | 4.89 (4.55 to 4.92) | 5.35 (5.03 to 5.36) | 5.91 (5.56 to 5.94) | 6.17 (5.78 to 6.32) |

With the 0.5 ms bounce the limit is 9.5 ms. At the nominal 5.0 V and 5.25 V supplies options A and B are faster but still fail at 75 and 85 C (`result.md` of s3 gives all 48 rows). Plot `s3-operate-vs-coil-temperature.png`.

Reading:
- The TS-012 criterion as written passes (K1, K1a) because it compares the lead-in with the datasheet value at the datasheet point. The physical criterion it stands for, contacts made and bounce ended before the ramp, fails for the drive TS-012 lists (option A) in every corner above the datasheet point at the lowest bus voltage, and for option B from about 49 C. The failure is not a model artefact at 75 and 85 C for option A: the ratio above 1 means the datasheet itself does not guarantee operation.
- A late contact is the failure mode TS-012 7.3 (adversarial R-1) designed the 10 ms lead-in against: the detector sits after pole A, the loop integrates into an open contact, and VGG steps when the contact closes (a key click, and above the 8 W stability limit at 8.4 V); the mid-ramp plausibility check (REQ-SYS-156) detects it only after the fact.
- The H1 coil from the pack (C, D) keeps the must-operate ratio at 0.77 or less at every corner, and every accepted set closes by 7.11 ms at 85 C, 2.39 ms inside the limit.

### 4.3 D-5 relay hold (s2, s3)

| Case | Hold current at 85 C | Hold / worst unit's must-operate current | Hold / release current (model band, lowest) | Coil power |
|---|---|---|---|---|
| Standard, full 5 V (no D-5) | 76.4 mA | 1.02 | 1.18 | about 0.5 W |
| Standard, 63 % PWM (thermal note assumption) | 48.1 mA | **0.64** | **0.74** (drops out in part of the band) | about 0.2 W |
| H1, full pack 8.4 V (no hold) | 40.5 mA | 1.80 | 2.08 | up to about 0.47 W |
| H1, 5.0 V average PWM (proposed) | 24.1 mA | **1.07** | 1.24 | about 0.15 W |

- A relay that operates at a current holds at that current (the closed-gap force is larger), so a hold current at or above the worst unit's must-operate current is guaranteed by the datasheet. The standard-coil hold at 63 % is not (K15-B OPEN: bench check of the fitted unit's drop-out, as TS-012 D-5 already says). The H1 hold at 5.0 V is (K15-D PASS).
- Hold duty rule (proposed): D = min(1, 5.0 V / (V_pack,receive - 0.9 V)), so the average stays at or above 5.0 V at the lowest key-down rail. At 8.4 V the average without sag is 5.6 V (0.19 W at 23 C).
- 25 kHz keeps the ripple at 2.27 % or less (s2, K13) and above the audio band. Its edges are a new dense-class PWM line for the spur plan (request to WP-PDR-20b).
- Pull-in at 100 % lasts 25 ms, at least twice the worst option C and D operate time of 7.11 ms (K14).
- Pull-in at 8.4 V is 168 % of the H1's rating against its 180 % maximum at 23 C, for 25 ms per over; the maximum falls with ambient on the datasheet graph, which is not text-readable. K19 stays OPEN until that curve is read at the gate. If it is under 168 % at 70 C, the pull-in duty is capped (for example 90 % at 25 kHz, 7.6 V average, ratio at 85 C still 0.82).

### 4.4 Key-up and end of the over (s3, s4)

- Every element's fall starts one lead-in after the keyer key-up; the last TX_KEY low comes 14 to 19.04 ms after the last keyer key-up (ramp 3 to 8 ms).
- At the hang expiry t_h: PA_EN low (after checking TX_KEY low and the envelope idle), CLK1 off by I2C and the prescaler supply off, then the T/R drive off, all within 0.5 ms (07 row b order).
- Cold-switching margin at key-up: 3 dits at 50 WPM (72 ms) against 19.04 ms, 52.96 ms (K10). The margin grows at lower speeds (`s4-margins.png` panel (b)). The REQ-SYS-044 floor of 3 dits is therefore not limited by the relay or the envelope (K11).
- Release with the freewheel diode (s3, `s3-release.png`): from the H1 hold, 6.32 ms (nominal set) to 12.92 ms (band); with ordering and NC bounce 13.92 ms of the 30 ms share of REQ-SYS-036 (K12-D). From the standard coil at full voltage 12.46 ms (K12-A). A zener clamp would shorten it but would defeat the PWM hold, which needs a freewheel path through a plain diode.
- Fault path: PA_EN low within 1.0 ms of detection and RF at the off level within a further 0.1 ms, 1.1 ms against the 20 ms of REQ-SYS-004 (K16); T/R to receive after PA_EN (07 row c order).

### 4.5 Elements during the over

- At 50 WPM with 8 ms ramps the TX_KEY windows of successive dits are 13.0 ms apart (K18). For a straight key sending faster than that, the merge rule keeps TX_KEY high when the next rise is due before the previous fall (table row EL-06).
- Lead-in on every element: 10.000 to 10.043 ms (PWM quantisation only); the first element 9.980 to 10.043 ms because the keyer test point follows the T/R write by up to 20 us (K2, K2b).

### 4.6 Relock margin and the interval-13 fallback (s4, `s4-keydown-budget.png` panel (b))

- With PA_EN before TX_KEY and the 2 ms lead, the smallest lead-in the ordering allows grows 1:1 with any relock time beyond the allocation. It reaches 10 ms at 0.903 ms of excess (K8) and 12 ms at 2.903 ms. The latest lock-gated FC0 start that still sets PA_EN by TX_KEY is t0 + 1.903 ms (K8b).
- Interval 13 at the changeover needs a lead-in of 13.193 ms with that ordering, or 11.443 ms if PA_EN may follow TX_KEY and the D-18 turn-on bound of 0.25 ms is taken (K9). The TS-012 fallback of 11.5 ms is therefore rejected as written; it is possible only with the ordering change and no relock margin (0.06 ms).

### 4.7 Key bounce

A sample-aligned bounce B adds up to B to t0. REQ-SYS-160 holds for B up to 1.957 ms (K3b); REQ-SYS-159 for B up to 0.9 ms (K17). `s4-margins.png` panel (a). The keyer study's input I-7 gives up to 10 ms of bounce for generic switches (Curtis, Ganssle), so the owner's key must be captured (WP-PDR-40).

## 5. Criteria (state list; `expected_states.json`)

| Id | State | Criterion | Value |
|---|---|---|---|
| K1 | PASS | ramp start at least 10 ms after the T/R command | 10.000 ms (+0.043 ms quantisation) |
| K1a | PASS | contacts made and bounce ended before the ramp at the datasheet point | 7.5 ms |
| K1b-A | **FAIL** | the same at every corner, option A (as listed) | no pull-in at 75 and 85 C; 12.59 ms at 49 C |
| K1b-B | **FAIL** | option B | 9.65 ms at 49 C (band to 12.39); no pull-in in part of the band at 75 C |
| K1b-C | PASS | option C | at most 7.11 ms (+0.5 bounce) |
| K1b-D | PASS | option D | at most 6.32 ms |
| K2 | PASS | lead-in at most 12 ms (REQ-SYS-161) | 9.980 to 10.043 ms |
| K2b | PASS | lead-in equal within 0.5 ms | 0.063 ms |
| K3 | PASS | contact to RF rise at most 15 ms (REQ-SYS-160), no bounce | 13.043 ms |
| K3b | CONDITION | largest key bounce for K3 | 1.957 ms |
| K4 | PASS | clamps held and integrator parked until the ramp | VGG clamp off at t0 + 8, reference at t0 + 10 |
| K5 | PASS | frequency check before PA_EN | 7.097 against 7.5 ms |
| K6 | PASS | PA_EN before TX_KEY | 7.5 against 8.0 ms |
| K7 | PASS | driver settled before the ramp | 9.0 ms |
| K8 | INFO | relock margin beyond the 1 ms allocation | 0.903 ms (TS-012 assumes 3 ms) |
| K8b | INFO | latest lock-gated FC0 start | t0 + 1.903 ms |
| K9 | **FAIL** | interval-13 fallback inside 12 ms with the proposed ordering | needs 13.193 ms |
| K10 | PASS | cold switching at key-up | 52.96 ms margin |
| K11 | PASS | REQ-SYS-044 floor against relay and envelope timing | 72 against 19.04 ms |
| K12-A | PASS | T/R release share of REQ-SYS-036, options A, B | 13.46 ms of 30 |
| K12-D | PASS | T/R release share of REQ-SYS-036, options C, D | 13.92 ms of 30 |
| K13 | PASS | hold PWM ripple | 2.27 % |
| K14 | PASS | pull-in duration at least twice the operate time (C, D) | 25 against 14.2 ms |
| K15-B | **OPEN** | standard-coil 63 % hold guaranteed | 0.64 x (bench) |
| K15-D | PASS | H1 5.0 V hold guaranteed | 1.07 x |
| K16 | PASS | RF off on an inhibit (REQ-SYS-004 input) | 1.1 ms |
| K17 | PASS | sidetone onset (REQ-SYS-159 input), no bounce | 3.1 ms; bounce up to 0.9 ms |
| K18 | PASS | TX_KEY windows at 50 WPM, 8 ms ramps | 13.0 ms gap |
| K19 | **OPEN** | H1 pull-in at 8.4 V against its maximum voltage at 70 C | 168 % against 180 % at 23 C |

## 6. Design recommendations and requests to other writers (this note edits none of their files)

### 6.1 D-5: the relay drive (to the lead SE for the A5 design; WP-PDR-37, 38, 54, 04)

1. **Coil and supply.** Fit the G5V-2-H1 DC5 (D-5's own second option), fed from the switched pack rail on the RF board, not the 5 V bus. Keep the 2N3904 driver (option C), or use an AO3400A (option D, 0.8 ms more margin).
2. **Drive.** T/R drive at 100 % from t0 for 25 ms, then a 25 kHz PWM at D = min(1, 5.0 V / (V_pack,receive - 0.9 V)). Firmware owns the duty; the reset and bootrom state is off (the NC contacts connect the antenna to the receiver).
3. **Freewheel diode.** A plain diode rated for the coil current across the coil (for example a 1N4148, 200 mA average, if the owner's stock has one). The TS-012 section 8.3 BOM has none, and the 1N5711W is not rated for it. No zener clamp (it would defeat the PWM hold).
4. **Gate reads (OD-42 price-check list).** The G5V-2-H1-DC5 price and lifecycle; its maximum-voltage curve at 70 C (K19).
5. **Thermal (WP-PDR-28).** Coil power 0.15 W (H1 hold) instead of 0.5 W; relay ambient rating 70 C (H1) instead of 65 C, against the 67.1 C continuous and 61.4 C duty-limited bay air.
6. If the H1 is not bought: option B with the bench measurements BM-1 to BM-3 on the fitted unit (a unit whose must-operate voltage is typical, not at the 75 % limit, may pass), and the risk entry below; option A is not viable at the hot corners.

### 6.2 Other requests

| To | Request |
|---|---|
| WP-PDR-54 (TS-012 record) | 7.3 rev 6: the interval-13 fallback "ramp moves to 11.5 ms" does not fit (K9); the revisit condition "relock exceeds the 1 ms allocation by more than the 3 ms between the check and the ramp" should read 0.9 ms with the 2 ms TX_KEY lead (K8); D-5 wording per section 6.1; row 2 and row 12 of 8.3 |
| WP-PDR-20a (`frequency-budget.md`) | RL-4: the latest FC0 start is t0 + 1.903 ms on the 4.096 ms interval bound (K8b), not 2.0 ms; RL-6 agrees with K9 |
| WP-PDR-20b (spur plan) | the 25 kHz relay-hold PWM on the RF board is a new dense-class PWM line |
| WP-PDR-32, 35 (SW architecture and L2) | SW-TXSEQ requirements: t0 = the T/R write, keyer test point in the same service; ramp at t0 + L on every element; PA_EN = both prerequisites, never after TX_KEY; TX_KEY L - 2 ms before and 1 ms after each ramp, with the merge rule; the D-5 drive and duty rule; the end-of-over order. 07 section 14.2 row j's key-up response needs restating for the constant lead-in and the D-18 PA_EN (Summary) |
| WP-PDR-36a (ICD-TX-SW) | the timing table of section 8, from the APPROVED revision of this note |
| WP-PDR-40 (bench session) | capture the owner's straight-key and paddle bounce against 1.957 ms (REQ-SYS-160) and 0.9 ms (REQ-SYS-159) |
| WP-PDR-23b | stuck and dropped relay cases, including a drop-out under shock at the hold current (the H1's shock malfunction rating is 100 m/s2 against 200 m/s2); the G6 values with the inputs of K11, K12, K16, K17 |
| WP-PDR-18 (risk register) | proposed entry: "Given a G5V-2 standard coil on the 5 V bus in the 61 to 67 C PA bay, there is a possibility that the T/R contacts close after the ramp start or not at all, adversely impacting REQ-SYS-014, 015 and the module's stability limit, leading to a key click or a Fault-safe on the first element", mitigated by section 6.1 |
| WP-PDR-43 (V&V plan) | bench measurements BM-1 to BM-5 (section 9) |

## 7. Proposed TBR values (rule C10: to the owner only after this note's record is APPROVED)

| Requirement | Value at HEAD | Proposal | Basis |
|---|---|---|---|
| REQ-SYS-161 | 12 ms (TBR) | **Keep 12 ms.** Design lead-in 10 ms (margin 1.96 ms), equal within 0.063 ms | K2, K2b; conditional on section 6.1 or BM-2 |
| REQ-SYS-160 | 15 ms (TBR) | **Keep 15 ms**, with the key-bounce assumption of at most 1.957 ms stated in its verification note | K3, K3b; WP-PDR-40 capture |

No other value is proposed here; REQ-SYS-004, 036, 044, 159, 176, 183, REQ-TX-016 and REQ-SW-KEYER-032 are the WP-PDR-23b set.

## 8. ICD-TX-SW timing table (run `2026-09-29-s4-sequence`, `icd-tx-sw-timing-table.csv`)

Times in ms after the reference event; "-" = not applicable. Signals are working names for WP-PDR-36a's pin map.

| Id | Event | Signal | Owner | Ref. | Min | Nom | Max | Serves | Basis |
|---|---|---|---|---|---|---|---|---|---|
| KD-01 | straight-key contact first make | KEY tip | operator | - | 0 | 0 | 0 | REQ-SYS-160 reference | R |
| KD-02 | key-down asserted; T/R drive written = t0 | TR_DRV | SW-KEYER, SW-TXSEQ | KD-01 | 1.0 | 2.0 | 3.0 (+ bounce) | REQ-SW-KEYER-018, 020; REQ-SYS-160 | R |
| KD-03 | keyer test point edge, same TIMER0 service | KEYER_TP | SW-KEYER | t0 | 0 | 0.01 | 0.02 | REQ-SYS-161 reference | A |
| KD-04 | T/R drive 100 % (pull-in), coil from the pack rail | TR_DRV | SW-TXSEQ | t0 | 0 | 0 | 0 | D-5 | A |
| KD-05 | prescaler supply on | PRESC_EN | SW-TXSEQ | t0 | 0 | 0 | 0.02 | D-17, D-18 | A |
| KD-06 | C6 writes, MSNA first (400 kHz) | I2C0 | SW-SYNTH | t0 | 0.650 | 0.650 | 0.650 | TS-012 7.3 C6 | DD |
| KD-07 | FC0 start, lock-gated (first LOL_A = 0) | - | SW-SYNTH | t0 | 0.650 | 1.000 | 1.903 | REQ-SYS-182 | A (20a M-1) |
| KD-08 | FC0 interval 12 on GPIN0 ends | GPIN0 | SW-SAFE | t0 | 4.746 | 5.097 | 6.000 | REQ-SYS-182, 154 | D |
| KD-09 | lock read, compare, permit decision | - | SW-SYNTH, SW-SAFE | t0 | 4.746 | 7.097 | 8.000 | REQ-SYS-182; 07 row h | A |
| KD-10 | "T/R in TX and settled" true | - | SW-TXSEQ | t0 | 7.5 | 7.5 | 7.5 | 07 row h | A |
| KD-11 | PA_EN high, never after TX_KEY | PA_EN | SW-SAFE | t0 | 7.5 | 7.5 | 8.0 | REQ-SYS-120; D-18 | A |
| KD-12 | T/R contacts made, bounce ended (C, D; worst unit) | relay | G5V-2-H1 | t0 | 3.261 | - | 7.610 | 07 row b | E |
| KD-13 | TX_KEY high: gate permits, VGG clamp off, driver on | TX_KEY | SW-TXSEQ | t0 | 8.0 | 8.0 | 8.0 | D-18 | A |
| KD-14 | driver supply and bias settled | GVA-84+ VCC | hardware | KD-13 | 0.0012 | - | 1.0 | loop start state | A; D-18 note |
| KD-15 | reference clamp released, ramp starts | ENV_REF | SW-TXSEQ | t0 | 10.000 | 10.000 | 10.043 | REQ-SYS-160, 161 | A |
| KD-16 | mid-ramp plausibility check | ADC | SW-TXSEQ, SW-SAFE | KD-15 | 1.5 | 2.5 | 4.0 | REQ-SYS-156 | A |
| KD-17 | T/R drive to hold PWM, 25 kHz, 5.0 V average | TR_DRV | SW-TXSEQ | t0 | 25 | 25 | 25 | D-5 | A |
| EL-01 | keyer element start | KEYER_TP | SW-KEYER | - | 0 | 0 | 0 | REQ-SYS-161 reference | R |
| EL-02 | TX_KEY high | TX_KEY | SW-TXSEQ | EL-01 | 8.0 | 8.0 | 8.0 | D-18 | A |
| EL-03 | ramp start | ENV_REF | SW-TXSEQ | EL-01 | 10.000 | 10.000 | 10.043 | REQ-SYS-161 | A |
| EL-04 | fall start after the keyer element end | ENV_REF | SW-TXSEQ | element end | 10.000 | 10.000 | 10.043 | REQ-SYS-014 | A |
| EL-05 | TX_KEY low after the fall ends | TX_KEY | SW-TXSEQ | fall end | 1.0 | 1.0 | 1.0 | REQ-TX-014 | A |
| EL-06 | merge rule: TX_KEY stays high if the next rise is due first | TX_KEY | SW-TXSEQ | - | - | - | - | no TX_KEY gap under 0 ms | A |
| KU-01 | last keyer key-up; hang starts | KEYER_TP | SW-KEYER | - | 0 | 0 | 0 | REQ-SYS-044 | R |
| KU-02 | last TX_KEY low | TX_KEY | SW-TXSEQ | KU-01 | 14.0 | 16.0 | 19.043 | cold switching | A |
| KU-03 | hang expiry t_h | - | SW-KEYER | KU-01 | 72 | - | 7200 | REQ-SYS-044 | R |
| KU-04 | PA_EN low (TX_KEY low and envelope idle checked) | PA_EN | SW-SAFE | t_h | 0 | 0.01 | 0.02 | 07 row b | A |
| KU-05 | CLK1 off (I2C), prescaler supply off | I2C0, PRESC_EN | SW-SYNTH, SW-TXSEQ | t_h | 0.02 | 0.1 | 0.3 | REQ-SYS-183 | A |
| KU-06 | T/R drive off | TR_DRV | SW-TXSEQ | t_h | 0.3 | 0.3 | 0.5 | 07 row b | A |
| KU-07 | NC contacts made, bounce ended (C, D) | relay | G5V-2-H1 | t_h | - | 7.32 | 13.92 | REQ-SYS-036 (30 ms share) | E |
| KU-08 | receive sensitivity within 3 dB of MDS | - | receiver | t_h | - | - | 50 | REQ-SYS-036 | R |
| FP-01 | fault detected; safe_state(): PA_EN low first | PA_EN | SW-SAFE | detection | 0 | - | 1.0 | REQ-SYS-004, 130 | A |
| FP-02 | gate clamps VGG, driver unpowered: RF-off level | hardware | hardware | FP-01 | 0 | - | 0.1 | REQ-SYS-004, 183 | E |
| FP-03 | T/R to receive after PA_EN low | TR_DRV | SW-SAFE | FP-01 | 0 | - | 0.05 | 07 row c | A |
| FB-13 | interval-13 fallback: check done (not adopted) | - | SW-SAFE | t0 | 11.193 | 11.193 | 11.193 | K9 | D, A |

The CSV and Markdown in the run folder carry the verification column for each row as well. Render: `docs/reviews/PDR/figures/timing-diagram.png` (panel (a) the first element, panel (b) a short over at 50 WPM with the end of the over).

## 9. Bench measurements that turn the estimates into data (to WP-PDR-43 and 40)

| Id | Measurement | Acceptance |
|---|---|---|
| BM-1 | must-operate and drop-out voltage of the fitted relay at 23 C and with the coil at 75 C or more (heat gun, thermocouple of D-16) | must-operate at 23 C at most 75 % of rated; drop-out at the hot coil under the hold average by at least 2 x |
| BM-2 | operate time plus bounce (logic capture of the T/R drive and of pole B's contact) at the lowest supply of the fitted option with the coil hot | at most 8.5 ms (1.5 ms to the ramp) |
| BM-3 | release time to the NC contact with the freewheel diode, from the hold, coil hot | at most 29.5 ms |
| BM-4 | hold stability: taps on the case at the hold duty while capturing pole B | no interruption |
| BM-5 | straight-key and paddle bounce of the owner's keys (WP-PDR-40) | at most 1.957 ms (REQ-SYS-160), 0.9 ms (REQ-SYS-159), or the conditions go to the owner |

## 10. Uncertainty and limitations

1. **The relay model is class E.** It is a lumped magnetic circuit without saturation, eddy currents or contact-spring detail. It is anchored only at the datasheet limits and swept over a band that the release anchor prunes. The conclusion that option A cannot be guaranteed at 75 and 85 C does not depend on the model: it follows from the datasheet must-operate limit and the copper coefficient (section 4.2 first table). The operate times of options B, C and D do depend on it.
2. **Worst-case unit.** The unit is at both datasheet limits at once (75 % must-operate and 7 ms operate). A typical unit is faster. The analysis claims no typical figure.
3. **Coil temperature corners** add an estimated self-heating (40 to 80 K/W) to the thermal note's bay air, which is itself an estimate with a stated band. A long over at full power without D-5 would heat the standard coil further (up to about 107 C), which only worsens options A and B.
4. **Bounce** is a graph read at 12 VDC and rated overdrive; higher overdrive (H1 at 8.4 V) may bounce longer. BM-2 measures it.
5. **Inputs under review.** The 0.650 ms C6 write time and the lock-gated start come from `frequency-budget.md` revision 2, and the 0.25 ms turn-on bound from `pa-permit-gate-d18.md` revision 0. A change there changes K8, K8b, K9 and rows KD-06 to KD-09; the 1 ms allocations of this note do not depend on them.
6. **Software latencies** (0.02 ms keyer test point, 2 ms compare, 0.5 ms end-of-over order, 1 ms inhibit response) are allocations for WP-PDR-32 to confirm in the software timing analysis.
7. **Not covered:** the receiver's recovery after the release (WP-PDR-19), the relay's RF isolation (23b), the keying loop's response to a late contact (22).

## 11. Reproduction and visual closure

```
cd /Users/robinonsay/rust/cwht
.venv/bin/python hardware/sim/tx-seq/seq_run.py all --expect    # exit 0; about 40 s
```

Plots, each opened and inspected by the author before this note cites it (rule C5): `results/2026-09-29-s1-drive/s1-coil-current.png`; `results/2026-09-29-s2-coil/s2-coil-transient.png`; `results/2026-09-29-s3-operate/s3-operate-vs-coil-temperature.png` and `s3-release.png`; `results/2026-09-29-s4-sequence/timing-diagram.png` (identical to `docs/reviews/PDR/figures/timing-diagram.png`), `s4-keydown-budget.png` and `s4-margins.png`. `coil_tran.raw` (7,114,568 bytes) is kept in its run folder and not committed; its SHA-256 is in `raw.sha256` (CR-017 C2).

## 12. References

- `docs/plan/pdr-work-plan.md` revision 6, WP-PDR-23 and 23a; status note `docs/plan/status/status-2026-09-29.md` section 8.
- TS-012 revision 8, `docs/decisions/trade-studies/TS-012-design-to-cost-hand-built.md` (`bb5dee7`).
- `docs/design/analysis/frequency-budget.md` revision 2 (`7593cea`); `pa-permit-gate-d18.md` revision 0 (`078f2f7`); `keying-ts012.md` revision 2 (`be86c02`); `thermal-ts012.md`; `keyer-host-study.md` (input I-7).
- `docs/process/07-software-engineering-plan.md` section 14.2 rows b, c, h, j; `docs/test_cases/sys/test_cases.json` TC-SYS-024, 030, 102.
- Omron G5V-2 datasheet, https://omronfs.omron.com/en_US/ecb/products/pdf/en-g5v_2.pdf (text as extracted for TS-012 revision 3; Characteristics, Ratings, notes 1 to 3, graphs named but not digitized).
- RP2350 datasheet section 8.1.4, Tables 542 and 582; onsemi 2N3904; AOS AO3400A Rev 3.1; TI LM2940 SNVS769J.

## Change history

| Revision | Date | Change | Commit |
|---|---|---|---|
| 0 | 2026-09-29 | First issue (WP-PDR-23a), frozen at F0 for the independent review and its SA pair | this commit |
