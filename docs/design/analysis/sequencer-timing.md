# Sequencer timing: key-down and key-up sequence, T/R relay drive and hold, ICD-TX-SW timing table (WP-PDR-23a)

| Field | Value |
|---|---|
| Product | `docs/design/analysis/sequencer-timing.md` (analysis note, `analysis_kind`: timing, worst-case; simulation of the relay coil drive; reduced-order electromechanical model of the relay), **revision 2**, 2026-09-29 (revision 1: `8ca7d05`; revision 0: `95adefc`) |
| Work package | WP-PDR-23a (`docs/plan/pdr-work-plan.md` revision 6, section 3.0 row 23 and section 4.1): "the key-down and key-up sequence with pass criteria (ramp start at least 10 ms after the relay command, lead-in at most 12 ms, key-to-RF at most 15 ms, clamps held and integrator parked until ramp start); the D-5 relay hold; `sequencer-timing.md` with the ICD-TX-SW timing table and its render". TS-012 revision 8 section 8.12 adds "the frequency check finished before PA_EN". WP-PDR-23b (NanoVNA isolation plan, stuck-relay cases, the G6 values) is not in this record |
| Author | Claude, analysis author invocation (RF designer role), 2026-09-29 |
| Status | Draft, **revision 2 for re-freeze (rule C2) and the next delta iteration** of the independent review and its software assurance pair (SW-TXSEQ is safety-critical; plan WP-PDR-23: reviewer plus SA). Revision 1 fixed the Major findings of iteration 1 (section 13); revision 2 fixes only the two new Major findings of the delta iteration (rule C1; section 14). Proposes values and design changes; it edits no requirement, hazard, ICD or trade-study file (plan section 5.3) |
| Findings answered | Independent review, iteration 1: finding-1 (CK-ANA-A4/E3, the H1 maximum coil voltage), finding-2 (CK-ANA-A4/B3, the H1 must-operate slope), finding-3 (CK-ANA-F1/F3, the release at -10 C), finding-4 (CK-ANA-F2/A6, the stale-ratio key-down case). Software assurance pair, iteration 1: finding-1 (swe-205 7.1 task 1, SA-C-i: the hold PWM on the line the K12 backstop and the PA-path gate watch), finding-2 (swe-205 7.1 task 1, SA-C-f/g/i: firmware-set coil drive parameters without integrity). All six are Major (revision 1). **Revision 2**, delta iteration: finding-13 (CK-ANA-A4/E3/F3, the option E key-down rail floor behind K15-E) and finding-14 (CK-ANA-E5/A5, the trigger of the REQ-SYS-160 stale-ratio condition), both Major |
| Design basis | TS-012 revision 8 (`bb5dee7`): section 7.3 "Revision 6: key-down sequence, frequency check and PA permit", section 8.1, section 8.3 rows 2 (G5V-2-DC5), 12 (2N3904BU) and 22 (AO3400A), section 8.12 row WP-PDR-23, section 8.14 D-5, D-11, D-17, D-18; decision A5 (section 10) |
| Inputs from records under review | `frequency-budget.md` revision 4 (`d030ce2`, WP-PDR-20a; revision 2 at `7593cea` was the revision 0 input): the C6 write time (0.650 ms), the lock-gated FC0 start (L_max 1.9 ms), A_kd = 10 s, R-FRESH-1, R-FRESH-2 and the 82.8 ms refresh (B-19). `pa-permit-gate-d18.md` revision 1 (`c397ab1`, WP-PDR-22; revision 0 at `078f2f7` was the revision 0 input): the D-18 gate turn-on bound of 0.25 ms. Re-checked for revision 1: every value this note uses is unchanged between those revisions. (r2) `frequency-budget.md` revision 4 FR-2r: the receive ratio age of at most 1.083 s. `pa-drive-ts012.md` revision 3 (`f1070cf`, WP-PDR-21, under review): the feed bound at key-down (0.5646 ohm at +45 C, 0.614 ohm at -10 C; 0.3841 ohm with the C2 P-FET lever) from section R3.5, and the key-down pack current at 6.4 V read from the `.raw` of run `2026-09-29-r3-p4-power-a5-design` (SHA-256 checked against its `raw.sha256`) |
| Datasheet read for revision 1 | Omron G5V-2 datasheet K046-E1-06 (`https://omronfs.omron.com/en_US/ecb/products/pdf/en-g5v_2.pdf`, PDF SHA-256 `7a0edd8490dca7c983db239a794a4d26223e8d95c534689de0c6068c1fc9d55a`, web-fetch tool; text by pdftotext, page 2 graphs rendered at 600 dpi in the scratchpad and read by eye): Ratings table and notes 1 to 3; the graphs "Ambient Temperature vs. Maximum Coil Voltage" and "Ambient Temperature vs. Must Operate or Must Release Voltage", both for the G5V-2-H1 |
| Decks, scripts and results | `hardware/sim/tx-seq/` (README.md there lists every run). **Revision 2 runs:** `2026-09-29-r2-s1-drive`, `2026-09-29-r2-s2-coil`, `2026-09-29-r2-s3-operate`, `2026-09-29-r2-s4-sequence` in `hardware/sim/tx-seq/results/`; each folder holds the same `seq_run.py` and `relay_model.py` as the working copy. The revision 1 runs `2026-09-29-r1-*` and the revision 0 runs `2026-09-29-s1-drive` to `2026-09-29-s4-sequence` stay as the records of those revisions, each with its own script copy. Timing diagram: `docs/reviews/PDR/figures/timing-diagram.png` (written by r1-s4) |
| Tool | LTspice 26.0.2 through `tools/ltspice-batch.sh` only (ACC-LTSPICE-001); `.raw` read with spicelib in the repo venv; Python 3.13 with numpy, scipy (solve_ivp) and matplotlib |
| Evidence status | **Developer evidence** (05 section 9.1): `seq_run.py` and `relay_model.py` have no TV record. The relay model is an estimate anchored to datasheet limits and, in revision 1, to the H1 must-operate graph (section 3.3). Every criterion state is compared with `expected_states.json` by `seq_run.py all --expect` (exit 0 on 2026-09-29) |
| Serves | REQ-SYS-160, REQ-SYS-161 (TBRs close at PDR); REQ-SYS-120, REQ-SYS-182 ordering; REQ-SYS-180 and HZ-004 K12 (the line the backstop watches); 07 section 14.2 rows b, c and h (the T/R and PA_EN order); HZ-004 K8 timing; TS-012 D-5; inputs to WP-PDR-23b for REQ-SYS-004, 036, 044, 159 and REQ-SW-KEYER-032; the ICD-TX-SW timing table that WP-PDR-36a writes; TC-SYS-102, TC-SYS-030, TC-SYS-024 methods |

## Summary

- **The sequence meets every criterion the plan names, as a schedule** (section 4.1): the ramp starts 10.000 ms after the T/R command (K1), the lead-in is 9.980 to 10.043 ms on every element against 12 ms, equal within 0.063 ms (K2, K2b), straight-key contact to RF rise is 13.043 ms against 15 ms (K3), the frequency check ends at t0 + 7.097 ms before PA_EN at t0 + 7.5 ms (K5), PA_EN precedes TX_KEY at t0 + 8 ms (K6), and the VGG clamp and the parked integrator hold until the ramp (K4). Revision 1 does not change the schedule.
- **The relay does not close inside that lead-in with the drive TS-012 lists** (section 4.2). The 7 ms operate time the 10 ms lead-in rests on is a datasheet value at the rated 5.0 V on a coil at 23 C. The must-operate voltage rises with coil temperature. In the PA bay (relay ambient 61.4 C at the duty limit and 67.1 C continuous, `thermal-ts012.md`):
  - **Option A, as listed** (standard DC5 coil on the 5 V bus, 2N3904 driver): a worst-case unit is not guaranteed to pull in at a 75 C coil, and needs about 12.6 ms (nominal model set) at a 49 C coil at 4.75 V (K1b-A **FAIL**). Option B (AO3400A): 9.65 ms at 49 C, no pull-in in part of the band at 75 C (K1b-B **FAIL**). Unchanged from revision 0.
  - **The H1 coil (options C, D, E).** Revision 1 takes the H1 must-operate slope from its datasheet graph, 0.48 to 0.51 %/K (the band used here, 0.48 to 0.535 %/K referenced to 23 C, also covers the 0.51 %/K taken from 20 C), not the copper 0.393 %/K of revision 0. The worst operate time at an 85 C coil is then 8.36 ms for option C (revision 0: 7.11), 7.13 ms for option D (6.32) and, with the revision 2 rail floor, 8.07 ms for the recommended option E (revision 1: 7.89 ms). All pass with the 0.5 ms bounce (K1b-C, D, E **PASS**, estimate; E has 1.43 ms to the limit).
- **Maximum coil voltage (K19, finding-1).** The datasheet graph gives the H1 maximum coil voltage as 180 % up to about 54 C, falling to about 167 % at 61.4 C, 156 % at 67.1 C and 151 % at the 70 C ambient rating. Ratings note 3 defines it as "the highest voltage that can be imposed on the relay coil", and the graph note says it is the top of the supply's varying range, not a continuous voltage. **The limit therefore applies to the imposed voltage, which for a PWM drive is the on-phase (peak) voltage, not the average.** A PWM from the pack imposes the pack voltage, up to 168 % at 8.4 V, whatever its duty: capping the pull-in average at 150 % does not meet it (K19-CD **FAIL**).
- **Recommended D-5 drive, option E** (section 6.1): the H1 coil fed from the switched pack rail **through a hardware coil-supply limiter** (a low-dropout regulator set to 6.3 V +/-2 %, dropout at most 0.2 V), with the AO3400A low-side driver on a **static TR_DRV level**: no pull-in phase, no PWM, no firmware-set duty.
  - The coil sees at most 6.43 V, 128.5 % of rated, peak equal to average, against 151 % at 70 C (K19-E **PASS**, 22.5 points of margin). This is the capped pull-in the review asks for, at 150 % or less, made in hardware.
  - **Hold (r2, finding-13).** Revision 1 took the lowest key-down rail as 5.45 V. That left out two things: REQ-SYS-097 lets a transmission start with the pack at 6.30 V (3.20 V -0.05 V per cell), and the WP-PDR-21 revision 3 feed bound is 0.5646 ohm at +45 C key-down, where the modelled pack current reaches 2.14 A. The rail then falls to 5.09 V, and to 4.99 V after a 0.1 V discharge allowance during the over. With the limiter dropout tightened from 0.20 to 0.10 V, the coil sees 4.89 V: **0.980 to 1.005 times** the worst unit's must-operate voltage at an 85 C coil, and 0.9997 to 1.026 at the start of the over. The datasheet guarantee is not shown (K15-E **OPEN**). It closes if the WP-PDR-21 P-FET lever is taken (1.050 to 1.077 times, already an owner item there), or by bench measurement BM-1 of the fitted relay. The revision 0 PWM hold at 5.0 V falls to 1.001 to 1.028 times with the graph slope (K15-D, PASS by 0.1 %; options C and D are rejected on other grounds).
  - Coil power at most 0.221 W at 85 C, inside the 0.225 W the 85 C coil corner assumes.
- **Release at -10 C (K12, finding-3).** Revision 1 runs the release at -10, 23 and 85 C from every hold the option applies at the end of an over. The worst case is at -10 C: option E 25.86 ms (from 6.43 V) against the 30 ms share, margin 4.14 ms (K12-E **PASS**); options C and D 24.78 ms from the 5.83 V end-of-over average of the duty rule (K12-D, margin 5.22 ms; revision 0 gave 13.92 ms at 85 C only).
- **Stale-ratio key-down (K20, finding-4; r2, finding-14).** When the operator keys within the 82.8 ms ratio refresh and the frequency reference ratio is then older than A_kd = 10 s (frequency-budget.md R-FRESH-2; this can happen after an over as short as 8.83 s, 1.63 s of keying with a 7.2 s hang, because the ratio can already be 1.083 s old when the over starts), this note fixes the outcome as **"elements not radiated"**: the elements that start before the refresh ends are sounded but not radiated, and the changeover is taken at the first keyer element after it, so every radiated element keeps the 10 ms lead-in (K20-b **PASS**; at most 2 elements at 50 WPM, 1 at 25 WPM or slower). The "late element" outcome is rejected: it gives a lead-in of up to 92.8 ms (K20-a **FAIL**, REQ-SYS-161). **In either outcome a straight-key closure in that window gets no RF rise within 15 ms, so REQ-SYS-160 as written is not met in this case** (K20-c **FAIL**). This goes to the owner with the REQ-SYS-160 proposal of section 7.
- **The backstop line (K21, SA finding-1).** With option E, TR_DRV is one static level for the whole over (2 edges per over), so the REQ-SYS-180 backstop (HZ-004 K12, HZ-014 K8) and the PA-path gate's T/R input see "in transmit" as a level. Revision 0's hold PWM put 50,000 edges per second on that line (K21-CD **FAIL**). Revision 1 also asks WP-PDR-26 that the backstop re-arm only after TR_DRV has been low for at least 30 ms, which is longer than the slowest release (K21-E **PASS**).
- **Firmware-set coil parameters (K22, SA finding-2).** In options C and D the firmware sets the duty from a pack reading, the PWM and the 25 ms pull-in. With the graph slope, a pack reading 0.1 to 2.4 % high already loses the guaranteed hold, and a stuck pull-in holds 168 % continuously (K22-CD **FAIL**). In option E the firmware only switches TR_DRV on and off. The coil voltage is bounded in hardware in every firmware state (K22-E **PASS**). The remaining failure modes are hardware faults, listed with their detection in section 4.9 and proposed to WP-PDR-16 for `hazards.json`.
- **Unchanged from revision 0**: the interval-13 fallback does not fit (K9 **FAIL**); the relock margin is 0.903 ms (K8, K8b); the key-bounce conditions (K3b, K17); the 07 section 14.2 row j restatement; key-up cold switching (K10, K11).
- **Proposed values** (section 7, to the owner only after this record is APPROVED, rule C10): REQ-SYS-161 keep 12 ms; REQ-SYS-160 keep 15 ms with the key-bounce condition and, new in revision 1, the stale-ratio case stated (revision 2: on the ratio's age, not on the over length), or a WP-PDR-20a design that removes the case. Both depend on D-5 option E or on bench measurement BM-2 of the fitted relay.

## 1. Question and scope

The question: does the A5 sequence of TS-012 section 7.3 (revision 6) meet its pass criteria, does the relay it relies on close inside the lead-in at every pull-in corner, how is the relay held at reduced power (D-5), and what timing table does ICD-TX-SW carry?

In scope:
- the first element of an over (the changeover), every later element, and the end of the over;
- the key-down on a ratio older than A_kd (R-FRESH-2; revision 1);
- the frequency check before PA_EN (D-17) and the PA permit (D-18) as timing, not as circuits;
- the T/R relay: coil drive, pull-in, hold and release, for five drive options, and the TR_DRV line as the K12 backstop and the PA-path gate see it;
- the fault path's RF-off timing (REQ-SYS-004) as an input to WP-PDR-23b.

Out of scope: the keying loop's envelope and spectrum (WP-PDR-22, `keying-ts012.md`), the D-18 gate circuit (`pa-permit-gate-d18.md`), the backstop monostable circuit (WP-PDR-26), the relay's RF isolation and stuck-relay cases (WP-PDR-23b), the Si5351A relock time itself (WP-PDR-20a, measurement M-1), the receiver's recovery after the relay releases (WP-PDR-19, TC-SYS-024), the choice of the limiter part (WP-PDR-37, 38; section 6.1).

Requirements and criteria checked (texts at HEAD, `docs/requirements/sys/requirements.json`):

| Id | Text (short) | How it is checked |
|---|---|---|
| Plan criterion 1 | ramp start at least 10 ms after the relay command | K1 schedule; K1a, K1b the physical basis (contacts made and bounce ended before the ramp) |
| REQ-SYS-161 | same lead-in of at most 12 ms (TBR) on every radiated element of an over | K2 (value), K2b (equality within the 0.5 ms of TC-SYS-102); K20-a, K20-b (stale ratio) |
| REQ-SYS-160 | RF rise within 15 ms (TBR) of each straight-key closure | K3; K3b the key-bounce condition; K20-c (stale ratio) |
| Plan criterion 4 | clamps held and integrator parked until ramp start | K4 |
| TS-012 rev 8 8.12 | frequency check finished before PA_EN | K5; K8, K8b, K9 the relock margin and the interval-13 fallback |
| REQ-SYS-120, D-18 | RF only with key-down and the permit; PA_EN before TX_KEY | K6, K7 |
| 07 section 14.2 rows b, c | T/R changes only while the envelope is below -20 dBc; PA_EN first, T/R last | K1b (key-down), K10 (key-up), FP-01 to FP-03 (fault) |
| D-5 | relay coil held at reduced power by PWM after pull-in, or the H1 coil | K13, K14, K15, K19, K22 |
| REQ-SYS-180, HZ-004 K12, HZ-014 K8 | the backstop watches the T/R transmit drive | K21 |
| REQ-SYS-036, 044, 004, 159 (23b values) | recovery 50 ms; hang 3 to 30 dits; RF off 20 ms; sidetone 4 ms | K12 (at -10, 23 and 85 C), K11, K16, K17 (inputs, no value proposed) |

## 2. Inputs

Class: R requirement; D datasheet; DD derived from datasheets (including graph reads); A allocation (a design value this note proposes); E estimate. `seq_run.py` holds every input in its `INPUTS` table and prints it into the s4 `result.json`. Rows marked (r1) are new or changed in revision 1.

| Input | Value | Class | Source |
|---|---|---|---|
| Key sampling; make filter | 1.000 ms; 2 consecutive closed samples, key-down asserted within 2 ms of the first closed sample | R | REQ-SW-KEYER-019, 020, 018 |
| Keyer test point after the T/R write | 0 to 20 us, same TIMER0 alarm service | A | this note |
| C6 changeover writes (MSNA first, CLK1 on, CLK0 and CLK2 off, PLL B parked), 400 kHz, no reg 177 reset | 0.650 ms | DD | `frequency-budget.md` RL-2 (revisions 2 to 4, unchanged) |
| Writes plus PLL settle allocation | 1.0 ms after t0 | A | TS-012 7.3 rev 6; WP-PDR-20a M-1 confirms |
| FC0 interval 12; interval 13; FC0_DELAY | 4.096 ms; 8.192 ms ("1 us x 2**interval", the Table 582 wording, which bounds the 0.98 us device value); at most 7 clk_ref cycles, 0.6 us | D | RP2350 datasheet section 8.1.4, Tables 542 and 582 |
| Lock-status read, compare, PA_EN write | 2.0 ms | A | `frequency-budget.md` C-14 |
| G5V-2 operate time; release time | 7 ms max; 3 ms max (rated voltage, coil 23 C; both coils) | D | Omron G5V-2 datasheet, Characteristics |
| G5V-2 must-operate; must-release | 75 % of rated max; 5 % min; at a coil temperature of 23 C | D | same, Ratings, notes 1 and 2 |
| (r1) G5V-2-H1 must-operate voltage slope | 0.48 %/K from 23 C, and 0.51 %/K from 20 C (0.5347 %/K from 23 C: the same must-operate voltage at 85 C); applied to the 75 % worst unit | DD | datasheet graph "Ambient Temperature vs. Must Operate or Must Release Voltage", G5V-2-H1, 10 samples; review finding-2 read 0.48 to 0.51 %/K; this author's re-read of the same graph gives 0.46 to 0.49 %/K of the 23 C value (max, mean and min lines 0.26 to 0.32 points of rated per K); section 3.3 |
| Coils | DC5 standard: 100 mA, 50 ohm, about 500 mW, max 120 %; H1 DC5: 30 mA, 166.7 ohm, about 150 mW, max 180 % (at 23 C); +/-10 % at 23 C | D | same, Ratings |
| (r1) G5V-2-H1 maximum coil voltage against ambient (3 to 24 VDC) | 180 % up to about 54 C, then straight down to 151 % at 70 C: 166.6 % at 61.4 C, 156.3 % at 67.1 C | DD | datasheet graph "Ambient Temperature vs. Maximum Coil Voltage" (knee read at 53.9 C, end at 69.8 C, 151 %) |
| (r1) Meaning of "maximum voltage" | "the highest voltage that can be imposed on the relay coil" (Ratings note 3); the graph "refers to the maximum value in a varying range of operating power voltage, not a continuous voltage" (graph note) | D | same, page 2. Read here as a limit on the imposed voltage at any instant, so on the PWM on-phase voltage |
| Ambient rating | standard -25 to 65 C; H1 -25 to 70 C | D | same, Characteristics |
| Bounce | 0.5 ms (0.3 to 0.5 ms read from the operate bounce-distribution graph, 12 VDC sample) | DD | TS-012 revision 3 graph read; used for the NC contact too (E) |
| Copper resistance coefficient | 0.00393 /K | R (handbook) | annealed copper at 20 C |
| Coil temperature corners | (r1) -10 C (REQ-SYS-114 lowest ambient, coil at ambient); 23 C (datasheet point); 49 C (nominal: 25 C outside, PA bay about +16 K, coil self-heating about +8 K); 75 C (45 C outside, relay ambient 61.4 C at the duty limit, plus up to 14 K of self-heating); 85 C (45 C continuous, 67.1 C, plus up to 18 K, i.e. up to 0.225 W at 80 K/W) | R, DD, E | REQ-SYS-114; `thermal-ts012.md` table (relay ambient A5); self-heating from a coil-to-ambient resistance of 40 to 80 K/W (E) |
| 5 V bus | 4.75 to 5.25 V | D | LM2940 SNVS769J section 6.5 (TS-012 7.3) |
| Switched pack rail, options C and D (revision 1 basis, kept for the comparison) | 6.35 V in receive (6.4 V less about 0.05 V of feed drop) to 8.4 V; 5.45 V lowest during key-down (0.9 V of feed drop at 2 A) | R, E | REQ-SYS-012, 097; TS-012 feed budget (0.26 to 0.45 ohm) |
| (r2) Pack at the start of a transmission, lowest | 6.30 V: REQ-SYS-097 refuses a transmission below 3.20 V +/-0.05 V per cell, measured in receive, so both cells at 3.15 V may start one | R | REQ-SYS-097 |
| (r2) Feed at key-down | 0.5646 ohm at +45 C and 0.614 ohm at -10 C (bound, every part at its datasheet maximum or upper value); 0.3841 ohm at +45 C with the C2 P-FET lever (a pair of at most 0.06 ohm, not adopted) | DD | `pa-drive-ts012.md` revision 3 section R3.5 (`f1070cf`); `run_a5_r3.py` `feed3_at` |
| (r2) Pack current at key-down | 2.140 A (+45 C, bound), 2.215 A (-10 C, bound), 2.233 A (+45 C, lever): the largest over the design corners at 6.4 V, 5 V bus included, used at 6.30 V too (the current falls with the pack) | DD | `.raw` of run `2026-09-29-r3-p4-power-a5-design` (SHA-256 `886371f6...`), re-derived by the s4 check `p4_feed_current` |
| (r2) Current through the feed in receive | 0.111 A (revision 1 basis, 0.05 V at 0.45 ohm) plus the coil's own 0.035 A at pull-in | E | TS-012 feed budget; s1 |
| (r2) Pack fall during an over | 0.10 V below the receive reading at the start (review finding-13; the sensitivity is plotted) | E | `s3-keydown-hold.png` panel (b) |
| (r2) Option E rail floors | pull-in (receive, t0): 6.30 V - 0.146 A x 0.614 ohm = **6.21 V**; key-down at +45 C: 6.30 - 2.140 x 0.5646 = **5.09 V** at the start of the over, **4.99 V** after the discharge; with the lever 5.34 V after the discharge; at -10 C 4.84 V after the discharge | R, DD, E | this note, `rail_rx_floor`, `rail_kd_floor` in `seq_run.py` |
| (r2) Ratio age in receive | at most 1.083 s (1 s refresh period plus the 82.8 ms refresh) | DD | `frequency-budget.md` revision 4, FR-2r |
| 2N3904 VCE(sat) | 0.30 V max at 50 mA, 5 mA base, used as a floor at every current; the LTspice model gives 0.04 to 0.11 V | D | onsemi 2N3904 datasheet; LTspice standard.bjt |
| AO3400A on-resistance at a 3.3 V gate | 29 to 32 mohm (VDMOS fit, class E; datasheet 48 mohm max at 2.5 V) | E, D | s1 check `mos_ron_range_mohm` |
| (r1) Option E coil-supply limiter | set point 6.30 V +/-2 % over -10 to 85 C; dropout at most **0.10 V** (r2; revision 1: 0.20 V) at up to 60 mA over -10 to 85 C; input rating above 8.4 V | A | this note: a part requirement, read at the OD-42 gate for the part WP-PDR-37 and 38 choose (section 6.1) |
| Freewheel diode | 1N4148 (LTspice model) in s2; in s3 a diode with no junction drop, the slowest decay | D, E | LTspice standard.dio |
| Lead-in L (T/R command to ramp start) | 10.0 ms | A | TS-012 7.3 |
| TX_KEY lead before each ramp; tail after each ramp | 2.0 ms; 1.0 ms | A | `keying-ts012.md` timing, TS-012 7.3 rev 6 |
| Driver supply and bias settled after the gate permits | 1.0 ms allocation | A | `pa-permit-gate-d18.md` revisions 0 and 1: powered within 1.2 us, turn-on at most 0.25 ms |
| Envelope reference PWM period (ramp-start quantisation) | 0.0427 ms (12 bit at clk_sys 96 MHz) | DD | TS-012 D-12 C1 |
| Ramp settings; speeds; hang | 3 to 8 ms; 5 to 50 WPM; 3 to 30 dits | R | REQ-SYS-014; REQ-SW-KEYER-015; REQ-SYS-044 |
| End-of-over ordering (PA_EN low, CLK1 off, prescaler off, T/R off) | within 0.5 ms | A | 07 section 14.2 row b order |
| REQ-SYS-036 share for the T/R release | 30 ms of 50 ms (the receiver keeps 20 ms) | A | this note, for WP-PDR-19 and 23b |
| Inhibit to PA_EN low; PA_EN low to RF off | 1.0 ms (A); 0.1 ms (E) | A, E | SW-SAFE service; D-18 gate in microseconds |
| D-5 pull-in time; hold PWM (options C and D only) | 25 ms at 100 %; 25 kHz, D = min(1, 5.0 V / (V_pack,receive - 0.9 V)) | A | revision 0 proposal, kept for the comparison |
| (r1) Ratio refresh; A_kd | 82.8 ms (50 ms stage settle plus the 32.768 ms interval-15 count); 10 s | DD, A | `frequency-budget.md` revision 4, B-19, R-FRESH-1 and R-FRESH-2 |
| (r1) Backstop re-arm qualification T_rearm | TR_DRV low continuously for at least 30 ms | A | this note, to WP-PDR-26 (section 4.9) |

## 3. Method

### 3.1 Sequence model (s4)

`seq_run.py s4` builds the key-down schedule of the first element of an over as event times after t0, the T/R drive write, and checks each criterion of section 1 as an inequality between events (K1 to K22). Per element, TX_KEY rises L - 2 ms after the keyer edge and falls 1 ms after the ramp ends; the ramp starts at the first envelope-PWM boundary at or after keyer edge + L. The end of the over is scheduled from the hang expiry. The relay's physical timing enters from s3. Revision 1 adds the stale-ratio schedule (section 4.8). The s4 outputs are the criteria table, the ICD-TX-SW timing table (CSV and Markdown), the timing diagram and the budget, margin and stale-ratio plots.

Detection worst case: the first sample after the first make comes at most 1 ms later, and key-down is asserted at most 2 ms after it (REQ-SW-KEYER-018), so t0 is at most 3 ms after the first make with no bounce. A bouncing key can open at every sample until the bounce ends at B, so t0 is at most B + 3 ms (K3b, K17).

### 3.2 Relay drive options and the LTspice runs (s1, s2)

| Option | Coil | Supply at the coil | Driver | TR_DRV | Status |
|---|---|---|---|---|---|
| A | G5V-2 DC5 standard | 5 V bus, 4.75 to 5.25 V | 2N3904 (TS-012 8.3 row 12) | static | as TS-012 lists it |
| B | G5V-2 DC5 standard | 5 V bus | AO3400A (row 22 part) | static | driver change only |
| C | G5V-2-H1 DC5 | switched pack rail, 6.35 to 8.4 V | 2N3904 | 25 ms at 100 %, then 25 kHz PWM | revision 0 recommendation; rejected (K19-CD, K21-CD, K22-CD) |
| D | G5V-2-H1 DC5 | switched pack rail | AO3400A | as C | as C |
| E (r1) | G5V-2-H1 DC5 | switched pack rail through the 6.3 V limiter: (r2) 6.11 V (the 6.21 V receive floor less the 0.10 V dropout; the set point's low corner is 6.17 V) to 6.43 V at pull-in; 4.89 V at the lowest key-down rail (4.99 V) | AO3400A | static | **recommended (section 6.1)** |

- **s1** (`drive_dc.cir`, DC sweep 4.5 to 8.6 V, 16 coil resistances x 2 driver temperatures): the coil current and the driver drop for both drivers from a 3.3 V GPIO, and (r1) branch E: a behavioural limiter, min(6.3 V, V_pack - 0.1 V) (r2 dropout), feeding a coil and an AO3400A on a static gate. The drop fits at 70 C feed s3: 2N3904 0.0144 V + 0.495 ohm x i (then floored at the datasheet 0.30 V), AO3400A 0.031 ohm x i. Branch E matches its closed form within 1.5 mV (check `limiter_closed_form`). Plots: `s1-coil-current.png` (at an 85 C coil on a +10 % unit the H1's current at 6.35 V is 27.8 mA against the worst unit's 21.9 mA must-operate current with the slope); (r1) `s1-coil-voltage-vs-pack.png`, the voltage imposed on the H1 coil against the pack for C, D (PWM) and E, against the maximum-voltage curve.
- **s2** (`coil_tran.cir`, 8 cases): pull-in rise to the must-operate current, 25 kHz hold PWM, and decay through the 1N4148 after the drive stops, with a fixed coil inductance (the open-gap value for the rise, the closed-gap value for the hold). (r1) E_rise_hot (r2: 6.11 V, 85 C coil, +10 % unit) and E_dc_cold (a static 6.43 V hold on a -10 % unit at -10 C, 49.2 mA, then off). The runs agree with the closed-form R-L results within 0.39 % (check `closed_form`). Hold ripple of the PWM cases is at most 2.26 % (check `ripple`). Plot `s2-coil-transient.png`.

### 3.3 Relay electromechanical model (s3)

The datasheet gives limits, not dynamics. `relay_model.py` is a one-magnetic-circuit model (flux linkage L(g) i with L falling from Lc at the closed gap to Lo = Lc / rho at the open gap, co-energy force, a preloaded spring whose force rises by sigma from open to closed, armature mass m, stops at both ends). It is anchored to the datasheet as follows:
1. The spring preload is set so that the armature starts to move at the must-operate current of a worst-case unit at 23 C, Ipu = 0.75 x 5.0 V / R23.
2. m is solved so that the operate time at 5.0 V on a 23 C coil is the datasheet's 7.0 ms (check `calibration_ref_7ms`, deviation under 0.01 ms). The unit is therefore at both datasheet limits at once, the worst case the datasheet allows.
3. Second anchor: the release time with no freewheel path (the datasheet's test condition) must be at most 3 ms. Parameter sets that fail it are rejected.
4. **(r1) Temperature.** The coil resistance rises by the copper coefficient. The must-operate voltage at a coil temperature T is V_mo23 (1 + s_mo (T - 23)); the model scales the whole spring force by the square of the resulting must-operate current ratio, (1 + s_mo (T - 23))^2 / k_cu(T)^2, so the pick-up and release currents move together (the graph's must-release line rises with the must-operate line). For the standard coil s_mo is the copper coefficient (the revision 0 law: constant must-operate current); options A and B fail with it already, and a steeper slope would only worsen them. For the H1, s_mo is the graph band. Check `slope_law`: the law reduces exactly to revision 0 for the copper case, and gives the band's must-operate voltage at 85 C.

The H1 slope band. The review read 0.48 to 0.51 %/K. This author's re-read of the same graph gives 0.46 to 0.49 %/K of the 23 C value. The review's operate times (option C 8.00 to 8.40 ms, D 6.91 to 7.16 ms at 85 C) and hold ratio (1.00 to 1.02) are reproduced within 0.05 ms and 0.01 when its slope is taken from 20 C rather than 23 C (option C 8.02 to 8.36 ms, D 6.92 to 7.13 ms, hold 1.001 to 1.016 in a check run). The design band therefore takes 0.48 %/K from 23 C and 0.51 %/K from 20 C (0.5347 %/K from 23 C). This bounds both reads and both reference points, and each result below is the worse of the two slopes.

The three unknowns form a class E band: open-gap time constant tau_o = Lo / R23 of 0.6, 1.2 and 2.4 ms, rho of 2, 3 and 4, sigma of 0.5, 1 and 2 (27 sets per coil). Of these, 3 cannot reach 7 ms at all and 11 fail the release anchor; **13 per coil are accepted**, among them the nominal set (1.2 ms, 3, 1). The accepted sets give a no-diode release of 1.13 to 2.90 ms. The model's no-motion limit reproduces the s2 LTspice rise times within 0.25 % (check `model_vs_ltspice_rise`, which now includes E_rise_hot).

For each option, supply (min, nominal, max), coil-temperature corner and (H1) slope, s3 runs every accepted set and reports the nominal set and the band; the copper law is kept for the H1 options as the revision 0 comparison. It sweeps the coil temperature from -10 to 100 C at the lowest supply. (r1) It runs the release from every hold the option applies at the end of an over at -10, 23 and 85 C, and a set-point trade for option E (5.8 to 7.4 V).

### 3.4 Checks

Every stage asserts its checks (README): s1 step count, driver ranges, drop fits and (r1) the limiter branch; s2 closed forms and ripple; s3 calibration, accepted-set count, the nominal set, the LTspice cross-check and (r1) the slope law; s4 schedule order and the upstream checks; (r2) s3 `hold_ratio_closed_form` (the model's key-down hold ratio equals V / V_mo,worst at 85 C) and s4 `p4_feed_current` (the key-down currents re-derived from the WP-PDR-21 p4 `.raw`, SHA-256 checked, within 1 mA). On 2026-09-29 all 17 checks pass. `seq_run.py all` exits 1 (checks pass; K1b-A, K1b-B, K9, K19-CD, K20-a, K20-c, K21-CD and K22-CD FAIL, K15-B and (r2) K15-E OPEN, as this note reports); `seq_run.py all --expect` exits 0.

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
| relay contacts made and bounce ended, option E worst case (r2, at the 6.11 V pull-in floor) | 8.57 |
| driver settled (allocation) | 9.0 |
| reference clamp released, ramp starts | 10.000 to 10.043 |

Revision 0's row "hold PWM at t0 + 25" is withdrawn: with option E, TR_DRV stays at one level until the end of the over. Plots: `docs/reviews/PDR/figures/timing-diagram.png` panel (a); `s4-keydown-budget.png` panel (a).

### 4.2 Relay pull-in at the corners (s3)

Ratio of the worst unit's must-operate voltage to the voltage at the coil (above 1: no guaranteed pull-in). Standard coil on the copper law; H1 with the steep end of the slope band (0.5347 %/K from 23 C):

| Option (coil voltage) | -10 C coil | 23 C | 49 C | 75 C | 85 C |
|---|---|---|---|---|---|
| A (4.75 V less 0.30 V) | 0.733 | 0.843 | 0.929 | **1.015** | **1.048** |
| B (4.75 V) | 0.687 | 0.789 | 0.870 | 0.951 | 0.982 |
| C (6.35 V less 0.30 V) | 0.510 | 0.620 | 0.706 | 0.792 | 0.825 |
| D (6.35 V) | 0.486 | 0.591 | 0.673 | 0.755 | 0.786 |
| E (r2: 6.11 V) | 0.505 | 0.614 | 0.699 | 0.784 | 0.817 |

Operate time to contact make at the lowest supply, worst-case unit (nominal set; band of the 13 accepted sets and, for the H1, both slopes, in brackets; "none" = no pull-in):

| Option | -10 C coil | 23 C | 49 C | 75 C | 85 C | 85 C, copper law (rev 0) |
|---|---|---|---|---|---|---|
| A | 7.13 (6.91 to 7.38) | 9.11 (9.01 to 10.69) | 12.59 (11.80 to none) | none | none | none |
| B | 6.41 (6.06 to 6.61) | 7.77 (7.75 to 8.13) | 9.65 (9.27 to 12.39) | 14.10 (12.69 to none) | 19.56 (16.57 to none) | none |
| C | 4.59 (4.10 to 4.68) | 5.20 (4.87 to 5.23) | 5.93 (5.63 to 5.94) | 7.00 (6.52 to 7.40) | 7.58 (6.90 to **8.36**) | 7.11 |
| D | 4.36 (3.88 to 4.44) | 4.89 (4.55 to 4.92) | 5.50 (5.15 to 5.51) | 6.34 (5.89 to 6.49) | 6.77 (6.23 to **7.13**) | 6.32 |
| E (r2, 6.11 V) | 4.54 (4.05 to 4.63) | 5.14 (4.80 to 5.16) | 5.84 (5.52 to 5.85) | 6.85 (6.39 to 7.19) | 7.39 (6.76 to **8.07**) | 6.93 |

With the 0.5 ms bounce the limit is 9.5 ms. At the nominal and highest supplies every option is faster (`result.md` of r2-s3 gives all 75 rows). The option E row is revision 2's: the pull-in floor moved from 6.15 V to 6.11 V (section 4.3); revision 1 gave 7.89 ms at 85 C. With revision 1's 0.20 V dropout the floor would be 6.01 V; the review's 6.05 V gives 8.36 ms. Plot `s3-operate-vs-coil-temperature.png` (panel (b) zooms on C, D and E).

Reading:
- The TS-012 criterion as written passes (K1, K1a) because it compares the lead-in with the datasheet value at the datasheet point. The physical criterion it stands for, contacts made and bounce ended before the ramp, fails for the drive TS-012 lists (option A) in every corner above the datasheet point at the lowest bus voltage, and for option B from about 49 C. The option A failure at 75 and 85 C does not depend on the model: the ratio above 1 means the datasheet itself does not guarantee operation.
- A late contact is the failure mode TS-012 7.3 (adversarial R-1) designed the 10 ms lead-in against: the detector sits after pole A, the loop integrates into an open contact, and VGG steps when the contact closes (a key click, and above the 8 W stability limit at 8.4 V); the mid-ramp plausibility check (REQ-SYS-156) detects it only after the fact.
- The H1 coil keeps the must-operate ratio at 0.83 or less at every corner. With the graph slope the worst case at 85 C rises by 1.25 ms (C), 0.81 ms (D) and (r2) 1.14 ms (E) against the copper law. Every accepted set still closes before the limit: option E by 8.07 ms (r2), 1.43 ms inside it. KD-12 changes to 3.83 to 8.57 ms (revision 1: 8.39 ms; revision 0: 3.26 to 7.61 ms for C and D), and the BM-2 acceptance changes with it (section 9).

### 4.3 D-5 relay hold and the maximum coil voltage (s1, s2, s3)

Hold current against the worst unit's must-operate current at an 85 C coil (the steep and the shallow end of the H1 slope band; the release current ratio over the model band):

| Case | Coil voltage | Hold current at 85 C | Hold / worst unit's must-operate current | Hold / release current (model band, lowest) | Coil power |
|---|---|---|---|---|---|
| Standard, full 5 V bus at 4.75 V (A, B, no D-5) | 4.75 V | 76.4 mA | 1.018 | 1.18 | about 0.5 W |
| Standard, 63 % PWM (thermal note assumption) | 2.99 V | 48.1 mA | **0.642** | **0.74** (drops out in part of the band) | about 0.2 W |
| H1, 5.0 V average PWM in key-down (C, D) | 5.00 V | 24.1 mA | **1.001 to 1.028** (rev 0: 1.072) | 1.16 | about 0.15 W |
| H1, limiter in dropout at the 5.45 V key-down rail (E, revision 1 basis, withdrawn) | 5.25 V | 25.3 mA | 1.051 to 1.079 | 1.21 | 0.13 W |
| (r2) H1, E, key-down rail 5.09 V: pack 6.30 V, feed bound, start of the over | 4.99 V | 24.1 mA | **0.9997 to 1.026** | 1.15 | 0.12 W |
| (r2) H1, E, the same after the 0.10 V discharge (K15-E) | 4.89 V | 23.6 mA | **0.980 to 1.005** | 1.13 | 0.12 W |
| (r2) H1, E, WP-PDR-21 P-FET lever, after the discharge | 5.24 V | 25.3 mA | **1.050 to 1.077** | 1.21 | 0.13 W |
| (r2) H1, E, -10 C key-down (feed 0.614 ohm, 2.215 A), after the discharge, coil at -10 C | 4.74 V | 32.7 mA | 1.502 to 1.535 | 1.73 | 0.15 W |
| H1, limiter at its high corner (E, receive and most of key-down) | 6.43 V | 31.0 mA | 1.287 to 1.321 | 1.49 | 0.20 W (0.221 W on a -10 % unit) |

- A relay that operates at a current holds at that current (the closed-gap force is larger), so a hold current at or above the worst unit's must-operate current is guaranteed by the datasheet. The standard-coil hold at 63 % is not (K15-B OPEN: bench check of the fitted unit's drop-out, as TS-012 D-5 already says).
- With the graph slope, the revision 0 H1 hold at 5.0 V keeps its guarantee by 0.1 % at the steep end of the band (K15-D PASS, 1.001). A pack reading 0.1 to 2.4 % high removes it (K22-CD).
- **Option E's hold does not depend on any reading, but (r2, finding-13) its datasheet guarantee at the lowest rail is not shown.** Revision 1 took the lowest key-down rail as 6.35 V less 0.9 V (0.45 ohm at 2 A). Revision 2 restates it (section 2 and `s3-keydown-hold.png`):
  - The pack can start a transmission at **6.30 V**: REQ-SYS-097 is 3.20 V +/-0.05 V per cell, and the lower edge of the tolerance is the design case.
  - The feed is the WP-PDR-21 revision 3 bound, **0.5646 ohm at +45 C key-down**, not TS-012's 0.45 ohm at 25 C. The key-down pack current at that bound is up to **2.140 A** (p4 corners at 6.4 V). The drop is 1.208 V, so the rail is **5.09 V** at the start of the over. The coil taps the switched pack rail after the DMP3099L pair (TS-012 section 7.3 power path), so the whole feed except the PA's drain chokes (about 0.01 ohm) is common to it; the chokes are kept in the bound, a slight overstatement.
  - The pack's reading is taken in receive before the over; during an over the pack discharges further. Revision 2 carries 0.10 V (class E, the review's figure): **4.99 V**.
  - With the limiter in dropout the coil sees the rail less the dropout. At revision 1's 0.20 V the coil sees 4.79 V (0.960 x). Revision 2 tightens the part requirement to **0.10 V at 60 mA over -10 to 85 C**, which low-dropout regulators with a P-channel pass device meet at this current: **4.89 V, 0.980 to 1.005 x** at an 85 C coil (steep and shallow ends of the slope band). At the start of the over it is 0.9997 to 1.026 x. No dropout requirement closes it: even with no dropout the coil would see 4.99 V after the discharge, 0.9997 x.
  - The coil's own temperature. The review notes that the coil runs cooler than the 85 C corner at the low hold (about 78 C). Its temperature is set by its average power over the over, and in the key-up gaps the limiter passes up to 6.24 V at the lowest pack. With that voltage all the time, a -10 % unit and 80 K/W, the coil reaches at most **83.8 C** (0.984 x at 4.89 V). A nominal unit held at 4.89 V reaches 76.6 C (1.014 x). The 85 C corner is kept; the 1.2 K difference does not change the verdict.
  - The cold end is not limiting: at -10 C the feed is 0.614 ohm and the rail after the discharge 4.84 V, but the cold coil needs much less (1.50 x).
  - **K15-E is OPEN.** It closes in one of two ways. (i) The WP-PDR-21 C2 P-FET lever (a pair of at most 0.06 ohm), which the owner already has to decide for REQ-SYS-012: the feed falls to 0.3841 ohm at +45 C, the rail to 5.34 V after the discharge, and the hold to **1.050 to 1.077 x** (PASS). (ii) BM-1 on the fitted relay: a must-operate voltage of at most 4.89 V with the coil at 85 C or more. Until then, a hot unit at the worst datasheet limit could drop out under RF near the end of a long over at the lowest pack. That is hot switching and a VGG step on reclosure, detected by REQ-SYS-156 (section 4.9, limiter row).
  - A lower-voltage H1 coil, which would keep the limiter regulating at the lowest rail, does not exist: the datasheet's ordering table (re-read for revision 2, same PDF SHA-256) lists the G5V-2-H1 in 5, 12, 24 and 48 VDC only.
  - At every rail above the dropout region the limiter holds 6.17 to 6.43 V.
- **Maximum coil voltage.** `s1-coil-voltage-vs-pack.png` panel (a) plots the voltage imposed on the coil against the pack voltage. For C and D the on-phase of any PWM imposes the pack voltage less the driver drop (AO3400A about 1 mV). That is 168 % at 8.4 V, whether the drive is the 100 % pull-in, a pull-in capped at a 150 % average or the hold. Panel (b) plots the datasheet curve against the relay ambient: 167 % at 61.4 C, 156 % at 67.1 C, 151 % at 70 C. Ratings note 3 makes the maximum "the highest voltage that can be imposed on the relay coil", and the graph note says the curve is "the maximum value in a varying range of operating power voltage, not a continuous voltage". So the limit applies to the peak, and a PWM average does not satisfy it (K19-CD **FAIL**). The imposed voltage exceeds the limit from 7.55 V of pack at 70 C, 7.82 V at 67.1 C and 8.33 V at 61.4 C.
- Option E imposes at most 6.43 V, 128.5 %, with peak equal to average, at every pack voltage and in every firmware state (K19-E **PASS**, 22.5 points under 151 %).
- Coil power and the 85 C corner. At 85 C, E dissipates at most 0.221 W on a -10 % unit at the limiter's high corner. The 85 C coil corner assumes up to 0.225 W (18 K at 80 K/W over the 67.1 C bay air), so the corner holds. The C and D hold at 5.6 V dissipated about 0.15 to 0.19 W.
- **Set point.** `s3-limiter-setpoint.png` (r2) shows the trade over 5.8 to 7.4 V at the revision 2 floors. Below about 6.2 V the pull-in at 85 C slows past the limit (6.0 V: 10.05 ms with bounce). From about 6.24 V the pull-in is set by the 6.21 V receive floor less the 0.10 V dropout (6.11 V, 8.57 ms with bounce), the release at -10 C slows by about 0.17 ms per 0.1 V, and the imposed voltage and coil power rise. The key-down hold does not depend on the set point: at the lowest rail the limiter is in dropout (lower-left panel, 0.980 x at every set point). 6.3 V is kept.
- The revision 0 items for options C and D are kept for the comparison only: 25 kHz keeps the ripple at 2.26 % or less (K13), and the 25 ms pull-in is at least twice the worst operate time of 8.36 ms (K14). Option E has neither a PWM nor a timed pull-in.

### 4.4 Key-up and end of the over (s3, s4)

- Every element's fall starts one lead-in after the keyer key-up; the last TX_KEY low comes 14 to 19.04 ms after the last keyer key-up (ramp 3 to 8 ms).
- At the hang expiry t_h: PA_EN low (after checking TX_KEY low and the envelope idle), CLK1 off by I2C and the prescaler supply off, then TR_DRV low, all within 0.5 ms (07 row b order).
- Cold-switching margin at key-up: 3 dits at 50 WPM (72 ms) against 19.04 ms, 52.96 ms (K10). The margin grows at lower speeds (`s4-margins.png` panel (b)). The REQ-SYS-044 floor of 3 dits is therefore not limited by the relay or the envelope (K11).
- **(r1) Release with the freewheel diode at -10, 23 and 85 C** (s3, `s3-release.png`). The hold at the end of an over is the receive-rail value: the PA is off, so the rail has recovered from the key-down sag.

  | Option and hold at the end of an over | -10 C | 23 C | 85 C | Worst with ordering and NC bounce | Criterion |
  |---|---|---|---|---|---|
  | A, B: 4.75 V bus | 20.63 | 16.97 | 12.46 | 21.63 ms | K12-A PASS, margin 8.37 ms |
  | C, D: duty-rule average 5.6 V (8.4 V pack) to 5.83 V (6.35 V pack) | 23.35 to 23.78 | 18.66 to 19.04 | 13.37 to 13.67 | 24.78 ms | K12-D PASS, margin 5.22 ms |
  | E: limiter (r2) 6.11 to 6.43 V | 24.31 to 24.86 | 19.50 to 19.98 | 14.04 to 14.43 | 25.86 ms | K12-E PASS, margin 4.14 ms |

  (band maxima in ms; nominal set for E at -10 C: 10.59 ms). The worst case is always at -10 C. A cold coil has a lower resistance, so it carries more current and a longer L/R decay, and its must-release current is lower. Revision 0 ran only an 85 C coil at a 5.0 V hold and reported 13.92 ms. With the review's figures for the duty-rule hold at -10 C (23.6 to 24.0 ms) this run agrees within 0.3 ms (23.35 to 23.78 ms). The cold case keeps the 30 ms share with 4.14 ms to spare for option E, not the 16 ms that revision 0 implied.
- A zener clamp in series with the freewheel diode would shorten the release. Revision 0 ruled it out because it would defeat the PWM hold. Option E has no PWM, so a clamp is now possible, but it is not needed for K12 and is not proposed.
- Fault path: PA_EN low within 1.0 ms of detection and RF at the off level within a further 0.1 ms, 1.1 ms against the 20 ms of REQ-SYS-004 (K16); T/R to receive after PA_EN (07 row c order).

### 4.5 Elements during the over

- At 50 WPM with 8 ms ramps the TX_KEY windows of successive dits are 13.0 ms apart (K18). For a straight key sending faster than that, the merge rule keeps TX_KEY high when the next rise is due before the previous fall (table row EL-06).
- Lead-in on every element: 10.000 to 10.043 ms (PWM quantisation only); the first element 9.980 to 10.043 ms because the keyer test point follows the T/R write by up to 20 us (K2, K2b).

### 4.6 Relock margin and the interval-13 fallback (s4, `s4-keydown-budget.png` panel (b))

- With PA_EN before TX_KEY and the 2 ms lead, the smallest lead-in the ordering allows grows 1:1 with any relock time beyond the allocation. It reaches 10 ms at 0.903 ms of excess (K8) and 12 ms at 2.903 ms. The latest lock-gated FC0 start that still sets PA_EN by TX_KEY is t0 + 1.903 ms (K8b); `frequency-budget.md` revision 3 adopted L_max = 1.9 ms from the same arithmetic.
- Interval 13 at the changeover needs a lead-in of 13.193 ms with that ordering, or 11.443 ms if PA_EN may follow TX_KEY and the D-18 turn-on bound of 0.25 ms is taken (K9). The TS-012 fallback of 11.5 ms is therefore rejected as written; it is possible only with the ordering change and no relock margin (0.06 ms).

### 4.7 Key bounce

A sample-aligned bounce B adds up to B to t0. REQ-SYS-160 holds for B up to 1.957 ms (K3b); REQ-SYS-159 for B up to 0.9 ms (K17). `s4-margins.png` panel (a). The keyer study's input I-7 gives up to 10 ms of bounce for generic switches (Curtis, Ganssle), so the owner's key must be captured (WP-PDR-40).

### 4.8 Key-down on a stale ratio (r1; R-FRESH-2; s4, `s4-stale-ratio.png`)

The case (`frequency-budget.md` revision 4, section 3.4.2): the squaring stage runs in receive only, so the XOSC-to-TCXO ratio is not refreshed during an over. R-FRESH-1 starts one refresh (82.8 ms) when receive resumes at the hang expiry. If the operator keys again before it completes, and the ratio at that key-down is older than A_kd = 10 s, R-FRESH-2 forbids PA_EN on that ratio: one refresh completes first. That record leaves the choice to this WP: a late element, or elements not radiated.

**(r2, finding-14) When the case arises.** The rule works on the ratio's age at the key-down, not on the length of the over. The age is the time since the last completed refresh. In receive the ratio is never older than 1.083 s (`frequency-budget.md` revision 4, FR-2r: the 1 s refresh period plus the 82.8 ms refresh). No refresh runs from the first key-down of an over to its hang expiry. So at a key-down 0 to 83.3 ms after the hang expiry (SR-01 up to 0.5 ms, then the refresh), the age is the over (first key-down to hang expiry) plus up to 1.083 s plus up to 83.3 ms:
- the case **can** arise after an over longer than 10 - 1.083 - 0.083 = **8.83 s**, depending on where the receive refresh stood when the over began;
- it **always** arises after an over longer than 10 s;
- the over includes the hang. With the longest hang (30 dits at 5 WPM, 7.2 s) an over of 8.83 s is **1.63 s of keying**: at 5 WPM, a few characters.

Revision 1 said "after an over longer than 10 s". That is the sufficient condition only. A TC-SYS-102 case written from it that keys again just after the hang expiry of a 9 s over (for example 1.8 s of keying and the 7.2 s hang) would expect RF that the design may correctly withhold. The firmware rule and rows SR-02 to SR-04 were already stated on the ratio age; revision 2 restates SR-01, K20-c and the section 7 condition the same way.

| Outcome | What happens | Lead-in of radiated elements (REQ-SYS-161) | Contact to RF (REQ-SYS-160) | State |
|---|---|---|---|---|
| (a) late element | the changeover waits for the refresh; the first element is radiated late | up to 92.84 ms on the first element against 10 ms on the rest: not equal, not at most 12 ms | up to 95.84 ms | K20-a **FAIL** (rejected) |
| (b) elements not radiated (**proposed**) | every keyer element that starts before the refresh ends is sounded (sidetone, REQ-SYS-159 unchanged) but not radiated: no T/R write, no PA_EN, no TX_KEY. The changeover (t0) is taken at the first keyer element start at or after the refresh end, with the normal rows KD-02 to KD-17 | 9.980 to 10.043 ms on every radiated element (equal within 0.063 ms) | no RF for the elements not radiated | K20-b **PASS** |
| REQ-SYS-160 in this case, either outcome | a straight-key closure inside the 82.8 ms window has no RF rise within 15 ms | - | not met as written | K20-c **FAIL** (to the owner, section 7) |

- Why (b): REQ-SYS-161 (adopted by SRR decision 47) exists so that every radiated element and space keeps its timing. Outcome (a) shifts one element by up to 83 ms, which at 50 WPM is more than three dits: it garbles the character and breaks REQ-SYS-161. Outcome (b) removes whole elements and leaves every radiated element and space unchanged. Both outcomes keep REQ-SYS-120 and 182 (no PA_EN on an aged ratio), so both are on the safe side, as `frequency-budget.md` says.
- How much is lost: at most the elements that start inside 82.8 ms. For continuous dits that is 2 elements at 50 WPM and 1 at 25 WPM or slower (element period 2 dits). (r2) The case needs a ratio older than 10 s at the key-down, which an over longer than 8.83 s can give (1.63 s of keying with a 7.2 s hang), and a pause after it only slightly longer than the hang: at most 83.3 ms longer.
- Relay: the T/R had released (at most 25.86 ms after t_h, K12-E) long before the deferred changeover, so the changeover is an ordinary cold one.
- No FC0 conflict: in outcome (b) the refresh is never abandoned for this case, because the changeover waits for it. The abandon rule of `frequency-budget.md` then applies only to a key-down on a ratio younger than A_kd.
- Firmware rule (for WP-PDR-32 and 35): SW-TXSEQ starts no changeover while the ratio is older than A_kd and a refresh is in progress; at the refresh end it starts the changeover at the next keyer element start. SW-SAFE sets no PA_EN on a ratio older than A_kd (R-FRESH-2, unchanged). HostUnit cases: ratio age 10.1 s with a key-down at t_r + 1 ms, at 5 and 50 WPM; the same at 9.9 s (normal changeover, refresh abandoned); a straight-key closure held across the refresh end (not radiated; the next closure radiated with L). Table rows SR-01 to SR-04.
- Ways to remove the case, for WP-PDR-20a to judge; this note does not change their record: (i) run the refresh in the last 82.8 ms of the hang time, with TX_KEY low and the driver unpowered, where the hang is at least 82.8 ms (3 dits at 43 WPM or slower); (ii) keep the ratio fresh during the over in key-up gaps. Either needs the squaring stage powered in transmit states, which `frequency-budget.md` 3.4.3 and the spur plan (WP-PDR-20b) decide.

### 4.9 The TR_DRV line and the relay drive's integrity (r1; SA findings 1 and 2)

**The line the backstop and the PA-path gate watch (K21).** HZ-004 K12 (REQ-SYS-180, shared as HZ-014 K8) is "a second monostable [that] watches the T/R transmit drive", and the PA-path gate proposed with it "also requires the T/R transmit drive". Both assume the drive is a level that is high for the whole over.
- Options C and D put a 25 kHz PWM on TR_DRV from t0 + 25 ms: 50,000 edges per second. A monostable triggered on an edge, or re-armed on drive-low, restarts every 40 us and never expires. That removes the only hardware bound on a toggling TX_KEY stream (hazard-analysis section 8.2 row 3). The gate's T/R input would switch the PA path at 25 kHz. K21-CD **FAIL**; revision 0 did not analyse this.
- Option E: TR_DRV has 2 edges per over, a rise at t0 and a fall at KU-06 (K21-E **PASS**). Requests: to WP-PDR-26 (the backstop circuit), trigger on the TR_DRV level, not on edges, and re-arm only after TR_DRV has been low continuously for at least T_rearm = 30 ms. That is longer than the slowest release (KU-07 maximum 25.86 ms), so a firmware TR_DRV dip too short to release the relay cannot restart the 150 to 180 s count. It is shorter than every hang (72 ms or more) and than the release margin, so a real return to receive always re-arms it. To WP-PDR-22 (the gate), take the gate's T/R input from the same TR_DRV level. A TR_DRV low then removes the PA output within the gate's microseconds, well before the contacts can open (the fastest no-diode release in the band is 1.13 ms), so a firmware TR_DRV fault under RF is switched cold. To WP-PDR-35: SW-TXSEQ never writes TR_DRV inside an over except at KU-06 and FP-03, and never puts a PWM slice on its pad (the HZ-014 C5 pin-map class of error).

**Firmware-set coil drive parameters (K22).** In options C and D the firmware sets three things: the hold duty from a pack reading, the PWM configuration and the 25 ms pull-in. None has an integrity provision.
- With the graph slope, a pack reading 0.1 to 2.4 % high gives a key-down average below the worst unit's must-operate voltage at 85 C, so the guaranteed hold is gone (the steep and shallow ends of the band; revision 0's margin was 7 %).
- A drop-out under RF is hot switching (07 row b). It is also the note's own VGG-step mechanism on reclosure (HZ-008 C5 key click and C6 above the stability limit).
- A stuck pull-in holds 168 % continuously, over the maximum at every bay ambient (K19).
- K22-CD **FAIL**. Option E removes all three: the firmware only switches TR_DRV, the coil voltage is set by the limiter and bounded to 128.5 % in any firmware state, and the key-down hold is set by the pack, the feed and the limiter with no reading used (K22-E **PASS**). (r2) K22-E no longer quotes the hold ratio as part of its test: its hardware margin is K15-E's question (OPEN, section 4.3), not a firmware one.

**Option E hardware failure modes and their detection** (single faults; proposed to WP-PDR-16 for `hazards.json` and to WP-PDR-23b for the stuck-relay cases; this note edits neither):

| Element | Fault | Effect | Detection or bound | Proposal |
|---|---|---|---|---|
| Limiter | output low, open or high dropout | no pull-in, late contact, or drop-out during key-down: RF into the open NO contact; drop-out under RF is hot switching and a VGG step on reclosure | REQ-SYS-156: the detector after pole A reads low against the drive, Fault-safe within 100 ms (TBR); first element at the mid-ramp check (KD-16, 1.5 to 4 ms after the ramp start); the step is bounded by the D-9 pack-dependent VGG clamp. The late-contact and open-loop runs of WP-PDR-22 give the size of the step | new HZ-008 cause "T/R contact open or reopened under RF by a relay coil supply fault (limiter or driver), VGG step at reclosure", controls REQ-SYS-156 (detection) and D-9 (bound); REQ-SYS-156 named as its detection |
| Limiter | pass element short (output = pack) | coil at up to 168 % continuously, over the maximum voltage; faster operate; release at -10 C from 8.4 V 27.67 ms, 28.67 ms with ordering and bounce (still inside 30) | no RF effect; not detected in service | not a hazard cause (no hazardous effect); a reliability item for the WP-PDR-23b stuck-relay list and the BM-6 check at build |
| AO3400A | drain-source short | relay in transmit whenever powered: receiver input grounded by pole B, antenna on the PA path, no RF without PA_EN and TX_KEY; TR_DRV low, so the gate holds the PA path off and K12 is not armed | operator: no receive; WP-PDR-23b stuck-relay case | existing HZ-004 and 23b stuck-relay cases |
| AO3400A, coil, diode | open driver or coil, shorted diode | as "limiter output low" | as above | as above |
| Freewheel diode | open | drain avalanche at turn-off (AO3400A 30 V), faster release | none in service; BM-3 | 23b list |
| TR_DRV (firmware) | a dip or pulse inside an over | the PA-path gate removes the PA output at once (cold); the backstop does not re-arm for a dip under 30 ms | K21-E; the gate (WP-PDR-22) | the K12 text states "TR_DRV is a static level; re-arm after at least 30 ms low" (to WP-PDR-16 and 26) |

## 5. Criteria (state list; `expected_states.json`)

| Id | State | Criterion | Value |
|---|---|---|---|
| K1 | PASS | ramp start at least 10 ms after the T/R command | 10.000 ms (+0.043 ms quantisation) |
| K1a | PASS | contacts made and bounce ended before the ramp at the datasheet point | 7.5 ms |
| K1b-A | **FAIL** | the same at every corner, option A (as listed) | no pull-in at 75 and 85 C; 12.59 ms at 49 C |
| K1b-B | **FAIL** | option B | 9.65 ms at 49 C (band to 12.39); no pull-in in part of the band at 75 C |
| K1b-C | PASS | option C (H1 slope band) | at most 8.36 ms (+0.5 bounce) |
| K1b-D | PASS | option D | at most 7.13 ms |
| K1b-E | PASS | option E (recommended) | (r2) at most 8.07 ms at the 6.11 V floor (+0.5 bounce = 8.57 against 10) |
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
| K12-A | PASS | T/R release share of REQ-SYS-036, options A, B, worst of -10, 23, 85 C | 21.63 ms of 30 (at -10 C) |
| K12-D | PASS | the same, options C, D (end-of-over hold 5.6 to 5.83 V) | 24.78 ms of 30 (at -10 C) |
| K12-E | PASS | the same, option E (r2: 6.11 to 6.43 V) | 25.86 ms of 30 (at -10 C) |
| K13 | PASS | hold PWM ripple (C, D only) | 2.26 % |
| K14 | PASS | pull-in duration at least twice the operate time (C, D only) | 25 against 16.7 ms |
| K15-B | **OPEN** | standard-coil 63 % hold guaranteed | 0.64 x (bench) |
| K15-D | PASS | H1 5.0 V PWM hold guaranteed (C, D) | 1.001 to 1.028 x |
| K15-E | **OPEN** | (r2) H1 hold at the lowest key-down coil voltage guaranteed (E): pack 6.30 V, feed bound 0.5646 ohm at 2.140 A, 0.10 V discharge, dropout 0.10 V | 0.980 to 1.005 x at 4.89 V (0.9997 to 1.026 x at the start of the over); 1.050 to 1.077 x with the WP-PDR-21 P-FET lever; closes by the lever or BM-1 |
| K16 | PASS | RF off on an inhibit (REQ-SYS-004 input) | 1.1 ms |
| K17 | PASS | sidetone onset (REQ-SYS-159 input), no bounce | 3.1 ms; bounce up to 0.9 ms |
| K18 | PASS | TX_KEY windows at 50 WPM, 8 ms ramps | 13.0 ms gap |
| K19-CD | **FAIL** | voltage imposed on the H1 coil against its maximum at the bay ambient (C, D; any PWM) | 168 % against 167, 156 and 151 % at 61.4, 67.1 and 70 C |
| K19-E | PASS | the same, option E (peak = average) | 128.5 % against 151 % |
| K20-a | **FAIL** | stale ratio, outcome (a) late element: REQ-SYS-161 | lead-in up to 92.84 ms (rejected) |
| K20-b | PASS | stale ratio, outcome (b) not radiated: REQ-SYS-161 on every radiated element; relay released first | 9.980 to 10.043 ms; at most 2 elements not radiated |
| K20-c | **FAIL** | REQ-SYS-160 in the stale-ratio window, either outcome | (r2) closures within 83.3 ms of the hang expiry, with the ratio older than 10 s, get no RF rise within 15 ms: possible after an over longer than 8.83 s (1.63 s of keying with a 7.2 s hang), always after one longer than 10 s (to the owner) |
| K21-CD | **FAIL** | TR_DRV a static level for the over (C, D) | 50 k edges per second |
| K21-E | PASS | TR_DRV a static level; T_rearm longer than the release (E) | 2 edges per over; 30 against 25.86 ms |
| K22-CD | **FAIL** | no firmware-set coil parameter can remove the hold or overdrive the coil (C, D) | 0.1 to 2.4 % reading error loses the hold; stuck pull-in 168 % |
| K22-E | PASS | the same (E) | no firmware-set coil parameter; (r2) the hold's hardware margin is K15-E |

Revision 0's K19 (OPEN) is replaced by K19-CD and K19-E. The FAIL states of K19-CD, K21-CD and K22-CD reject options C and D. They are not open items of the recommended design. (r2) K15-E is an open item of the recommended design (section 4.3).

## 6. Design recommendations and requests to other writers (this note edits none of their files)

### 6.1 D-5: the relay drive, option E (to the lead SE for the A5 design; WP-PDR-37, 38, 54, 04)

1. **Coil.** Fit the G5V-2-H1 DC5 (D-5's own second option), on the RF board.
2. **Coil supply: a hardware coil-supply limiter** between the switched pack rail and the coil. It is a linear low-dropout regulator whose output feeds only the coil and its freewheel diode. Part requirements (class A; each is read from the chosen part's datasheet at the OD-42 gate):
   - output 6.3 V +/-2 % over -10 to 85 C, fixed or set by a divider;
   - dropout at most **0.10 V** at 60 mA over -10 to 85 C (r2, finding-13; revision 1: 0.20 V). At the lowest key-down rail the limiter is in dropout, so every 0.1 V here is 0.02 of the K15-E hold ratio;
   - input rating above 8.4 V with the pack's transients;
   - output current at least 60 mA (the cold -10 % unit at 6.43 V draws 49 mA);
   - stable with the coil load and the output capacitor the datasheet asks for.
   The quiescent current goes to the WP-PDR-24 power budget. Revision 1 proposes the requirements, not a part: the part and its cost go to WP-PDR-37 and 38 and to the TS-012 ordering-gate recompute.
3. **Driver and drive.** An AO3400A low-side switch (the row 22 part; one more than the two the protector uses), gate from TR_DRV through the usual series resistor, with a pull-down so that reset and bootrom read off (the NC contacts connect the antenna to the receiver). **TR_DRV is a static GPIO level: high from t0 to KU-06, no PWM, no pull-in phase, no firmware-set duty.** The 2N3904 is not recommended with the limiter: its 0.30 V floor would take another 0.3 V off the key-down hold (0.92 x at the revision 2 floor).
4. **Freewheel diode.** A plain diode rated for the coil current across the coil (for example a 1N4148, 200 mA average, if the owner's stock has one). The TS-012 section 8.3 BOM has none, and the 1N5711W is not rated for it.
5. **Why not the PWM hold of revision 0 (options C, D).** The imposed on-phase voltage is 168 % at 8.4 V against the maximum curve (K19-CD). The PWM on TR_DRV defeats the K12 backstop and the PA-path gate's T/R input (K21-CD). The duty, the PWM and the pull-in are firmware-set values with no integrity provision, and the hold margin is gone at a 0.1 to 2.4 % reading error (K22-CD). Moving the PWM to a separate pin would answer K21 only. Fixing K19 and K22 as well would need a regulated supply anyway, so option E removes the PWM.
6. **Gate reads (OD-42 price-check list).** The G5V-2-H1-DC5 price and lifecycle; the limiter part against item 2.
7. **Thermal (WP-PDR-28).** Coil power at most 0.22 W at an 85 C coil (0.32 W on a cold -10 % unit at -10 C), instead of 0.5 W. The relay ambient rating is 70 C (H1) instead of 65 C, against the 67.1 C continuous and 61.4 C duty-limited bay air. Add the limiter's own dissipation, at most (8.4 - 6.17) V x 49 mA = 0.11 W.
8. If the H1 is not bought: option B with the bench measurements BM-1 to BM-3 on the fitted unit (a unit whose must-operate voltage is typical, not at the 75 % limit, may pass), and the risk entry below; option A is not viable at the hot corners.

### 6.2 Other requests

| To | Request |
|---|---|
| WP-PDR-54 (TS-012 record) | 7.3 rev 6: the interval-13 fallback "ramp moves to 11.5 ms" does not fit (K9); the revisit condition "relock exceeds the 1 ms allocation by more than the 3 ms between the check and the ramp" should read 0.9 ms with the 2 ms TX_KEY lead (K8); D-5 wording per section 6.1 (option E: the H1 coil through a coil-supply limiter, static drive, no PWM); rows 2, 12 and 22 of 8.3 and the limiter row; the block diagram label "coil held by PWM (D-5)" |
| WP-PDR-20a (`frequency-budget.md`) | R-FRESH-2 outcome fixed as "elements not radiated" (section 4.8); the two ways to remove the case, for that record's judgement; RL-4 agrees with K8b |
| WP-PDR-20b (spur plan) | revision 0's 25 kHz relay-hold PWM line is withdrawn (option E has none) |
| WP-PDR-22 (D-18 gate, keying loop) | the PA-path gate's T/R input is the TR_DRV level (section 4.9); size the VGG step of a relay drop-out under RF in the late-contact and open-loop runs, and confirm REQ-SYS-156 detects it within its 100 ms (TBR) |
| WP-PDR-26 (hardware timers) | the K12 backstop watches the TR_DRV level, not its edges, and re-arms only after TR_DRV has been low continuously for at least 30 ms (K21-E) |
| WP-PDR-16 (hazard analysis) | the option E failure-mode table of section 4.9: a new HZ-008 cause for a relay coil supply fault under RF with REQ-SYS-156 as its detection; the K12 text states that the T/R transmit drive is a static level with the 30 ms re-arm qualification; options C and D are not adopted, so no firmware-set coil-drive cause is added |
| WP-PDR-32, 35 (SW architecture and L2) | SW-TXSEQ requirements: t0 = the T/R write, keyer test point in the same service; ramp at t0 + L on every element; PA_EN = both prerequisites, never after TX_KEY; TX_KEY L - 2 ms before and 1 ms after each ramp, with the merge rule; TR_DRV a static level written only at t0, KU-06 and FP-03, never a PWM slice; the end-of-over order; the R-FRESH-2 outcome (b) rule and its HostUnit cases (section 4.8). 07 section 14.2 row j's key-up response needs restating for the constant lead-in and the D-18 PA_EN (revision 0 Summary) |
| WP-PDR-36a (ICD-TX-SW) | the timing table of section 8, from the APPROVED revision of this note |
| WP-PDR-37, 38 (schematic, BOM) | option E per section 6.1: the limiter part against the part requirements, the third AO3400A, the freewheel diode, TR_DRV to the relay driver, the K12 backstop and the PA-path gate, with no PWM slice on its pin |
| WP-PDR-40 (bench session) | capture the owner's straight-key and paddle bounce against 1.957 ms (REQ-SYS-160) and 0.9 ms (REQ-SYS-159) |
| WP-PDR-23b | stuck and dropped relay cases, including a drop-out under shock at the hold current (the H1's shock malfunction rating is 100 m/s2 against 200 m/s2) and the section 4.9 limiter and driver faults; the G6 values with the inputs of K11, K12, K16, K17 |
| WP-PDR-18 (risk register) | proposed entry: "Given a G5V-2 standard coil on the 5 V bus in the 61 to 67 C PA bay, there is a possibility that the T/R contacts close after the ramp start or not at all, adversely impacting REQ-SYS-014, 015 and the module's stability limit, leading to a key click or a Fault-safe on the first element", mitigated by section 6.1 |
| WP-PDR-43 (V&V plan) | bench measurements BM-1 to BM-7 (section 9) |
| (r2) WP-PDR-21 (`pa-drive-ts012.md`) and the owner | the C2 P-FET lever (a pair of at most 0.06 ohm) also closes K15-E: the option E key-down hold goes from 0.980 to 1.050 x at the lowest pack and a hot relay (section 4.3). One decision serves both records; if it is not taken, K15-E closes only by BM-1 on the fitted unit |
| (r2) WP-PDR-24 (power budget) | the switched pack rail at key-down reaches 5.09 V at the REQ-SYS-097 floor with the feed bound (4.99 V after 0.1 V of discharge). The LM2940-5 input needed for the 4.75 V bus floor at that rail is for that record to check; this note uses 4.75 V for options A and B only |

## 7. Proposed TBR values (rule C10: to the owner only after this note's record is APPROVED)

| Requirement | Value at HEAD | Proposal | Basis |
|---|---|---|---|
| REQ-SYS-161 | 12 ms (TBR) | **Keep 12 ms.** Design lead-in 10 ms (margin 1.96 ms), equal within 0.063 ms, on every radiated element, including after a stale-ratio key-down | K2, K2b, K20-b; conditional on section 6.1 or BM-2 |
| REQ-SYS-160 | 15 ms (TBR) | **Keep 15 ms**, with two conditions stated in its verification note, for the owner to accept or reject: (1) key bounce of at most 1.957 ms; (2) (r2, stated on the ratio age) a closure within 83.3 ms of the hang expiry, when the frequency reference ratio is then more than 10 s old, is sounded but not radiated (R-FRESH-2). The ratio can be that old after an over (first key-down to hang expiry) longer than 8.83 s, which with the longest hang (7.2 s) is 1.63 s of keying, and always is after an over longer than 10 s. The TC-SYS-102 procedure sets the case up by the ratio age (for example a HostUnit or Emulation case with the age injected, and on the bench an over of more than 10 s), not by the over length alone. If the owner does not accept (2), WP-PDR-20a is asked to remove the case (section 4.8) | K3, K3b, K20-c; WP-PDR-40 capture |

No other value is proposed here; REQ-SYS-004, 036, 044, 159, 176, 183, REQ-TX-016 and REQ-SW-KEYER-032 are the WP-PDR-23b set.

## 8. ICD-TX-SW timing table (run `2026-09-29-r2-s4-sequence`, `icd-tx-sw-timing-table.csv`)

Times in ms after the reference event; "-" = not applicable. Signals are working names for WP-PDR-36a's pin map. Rows changed or added in revision 1: KD-04, KD-12, KD-17, KU-06, KU-07, SR-01 to SR-04. Rows changed in revision 2: KD-12 (the 6.11 V pull-in floor), SR-01 (stated on the ratio age).

| Id | Event | Signal | Owner | Ref. | Min | Nom | Max | Serves | Basis |
|---|---|---|---|---|---|---|---|---|---|
| KD-01 | straight-key contact first make | KEY tip | operator | - | 0 | 0 | 0 | REQ-SYS-160 reference | R |
| KD-02 | key-down asserted; T/R drive written = t0 | TR_DRV | SW-KEYER, SW-TXSEQ | KD-01 | 1.0 | 2.0 | 3.0 (+ bounce) | REQ-SW-KEYER-018, 020; REQ-SYS-160 | R |
| KD-03 | keyer test point edge, same TIMER0 service | KEYER_TP | SW-KEYER | t0 | 0 | 0.01 | 0.02 | REQ-SYS-161 reference | A |
| KD-04 | T/R drive on: TR_DRV high, a static level (no PWM); coil through the limiter (option E) | TR_DRV (GPIO level) | SW-TXSEQ | t0 | 0 | 0 | 0 | D-5; K12 and the PA-path gate watch TR_DRV | A |
| KD-05 | prescaler supply on | PRESC_EN | SW-TXSEQ | t0 | 0 | 0 | 0.02 | D-17, D-18 | A |
| KD-06 | C6 writes, MSNA first (400 kHz) | I2C0 | SW-SYNTH | t0 | 0.650 | 0.650 | 0.650 | TS-012 7.3 C6 | DD |
| KD-07 | FC0 start, lock-gated (first LOL_A = 0) | - | SW-SYNTH | t0 | 0.650 | 1.000 | 1.903 | REQ-SYS-182 | A (20a M-1) |
| KD-08 | FC0 interval 12 on GPIN0 ends | GPIN0 | SW-SAFE | t0 | 4.746 | 5.097 | 6.000 | REQ-SYS-182, 154 | D |
| KD-09 | lock read, compare, permit decision | - | SW-SYNTH, SW-SAFE | t0 | 4.746 | 7.097 | 8.000 | REQ-SYS-182; 07 row h | A |
| KD-10 | "T/R in TX and settled" true | - | SW-TXSEQ | t0 | 7.5 | 7.5 | 7.5 | 07 row h | A |
| KD-11 | PA_EN high, never after TX_KEY | PA_EN | SW-SAFE | t0 | 7.5 | 7.5 | 8.0 | REQ-SYS-120; D-18 | A |
| KD-12 | T/R contacts made, bounce ended (option E; worst unit; H1 slope band; r2 pull-in floor 6.11 V) | relay | G5V-2-H1 | t0 | 3.826 | - | 8.567 | 07 row b | E |
| KD-13 | TX_KEY high: gate permits, VGG clamp off, driver on | TX_KEY | SW-TXSEQ | t0 | 8.0 | 8.0 | 8.0 | D-18 | A |
| KD-14 | driver supply and bias settled | GVA-84+ VCC | hardware | KD-13 | 0.0012 | - | 1.0 | loop start state | A; D-18 note |
| KD-15 | reference clamp released, ramp starts | ENV_REF | SW-TXSEQ | t0 | 10.000 | 10.000 | 10.043 | REQ-SYS-160, 161 | A |
| KD-16 | mid-ramp plausibility check | ADC | SW-TXSEQ, SW-SAFE | KD-15 | 1.5 | 2.5 | 4.0 | REQ-SYS-156 | A |
| KD-17 | no pull-in or hold phase: TR_DRV stays high until KU-06 (revision 0's hold PWM at t0 + 25 ms withdrawn) | TR_DRV (GPIO level) | SW-TXSEQ | t0 | - | - | - | D-5; REQ-SYS-180 | A |
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
| KU-06 | T/R drive off: TR_DRV low | TR_DRV | SW-TXSEQ | t_h | 0.3 | 0.3 | 0.5 | 07 row b | A |
| KU-07 | NC contacts made, bounce ended (option E, worst of -10, 23, 85 C) | relay | G5V-2-H1 | t_h | - | 11.59 | 25.86 | REQ-SYS-036 (30 ms share) | E |
| KU-08 | receive sensitivity within 3 dB of MDS | - | receiver | t_h | - | - | 50 | REQ-SYS-036 | R |
| FP-01 | fault detected; safe_state(): PA_EN low first | PA_EN | SW-SAFE | detection | 0 | - | 1.0 | REQ-SYS-004, 130 | A |
| FP-02 | gate clamps VGG, driver unpowered: RF-off level | hardware | hardware | FP-01 | 0 | - | 0.1 | REQ-SYS-004, 183 | E |
| FP-03 | T/R to receive after PA_EN low | TR_DRV | SW-SAFE | FP-01 | 0 | - | 0.05 | 07 row c | A |
| FB-13 | interval-13 fallback: check done (not adopted) | - | SW-SAFE | t0 | 11.193 | 11.193 | 11.193 | K9 | D, A |
| SR-01 | receive resumes; ratio refresh starts = t_r. Rows SR-02 to SR-04 apply when the ratio is older than A_kd at the closure (r2: possible after an over longer than 8.83 s) | - | SW-SAFE | t_h | 0 | 0.3 | 0.5 | R-FRESH-1 | A |
| SR-02 | keyer elements that start before the refresh ends: sidetone only, no T/R write, no PA_EN | KEYER_TP, sidetone | SW-KEYER, SW-TXSEQ, SW-SAFE | t_r | 0 | - | 82.8 | R-FRESH-2; REQ-SYS-120, 182; REQ-SYS-160 not met (K20-c) | DD, A |
| SR-03 | ratio refresh complete | - | SW-SAFE | t_r | 82.8 | 82.8 | 82.8 | frequency-budget.md B-19 | DD |
| SR-04 | first keyer element start at or after SR-03: the changeover (t0), rows KD-02 to KD-17 | TR_DRV | SW-TXSEQ | SR-03 | 0 | - | 480 (one element period at 5 WPM) | REQ-SYS-161 | A |

The CSV and Markdown in the run folder carry the verification column for each row as well. Render: `docs/reviews/PDR/figures/timing-diagram.png` (panel (a) the first element, panel (b) a short over at 50 WPM with the end of the over). The stale-ratio rows are drawn in `s4-stale-ratio.png`.

## 9. Bench measurements that turn the estimates into data (to WP-PDR-43 and 40)

| Id | Measurement | Acceptance |
|---|---|---|
| BM-1 | must-operate and drop-out voltage of the fitted H1 at 23 C and with the coil at 85 C or more (heat gun, thermocouple of D-16) | must-operate at 23 C at most 75 % of rated; (r2) must-operate at the hot coil at most **4.89 V**, the lowest option E key-down coil voltage (section 4.3). This closes K15-E for the fitted unit if the WP-PDR-21 P-FET lever is not taken; with the lever the limit is 5.24 V |
| BM-2 | operate time plus bounce (logic capture of TR_DRV and of pole B's contact), (r2) coil supplied at **6.11 V** (the pull-in floor: the 6.21 V receive floor less the 0.10 V dropout, from a bench supply) with the coil at 85 C or more | (r2) at most **8.7 ms** (1.3 ms to the ramp; the model's worst unit gives 8.57 ms). A value above 8.7 ms and at most 9.5 ms still meets the criterion, but shows the model under-predicts: the model is re-anchored and the result goes to the owner |
| BM-3 | release time to the NC contact with the freewheel diode, (r1) from the limiter's high corner (6.43 V), at room temperature and on the REQ-SYS-114 cold-day check | (r1) at most 29.0 ms including NC bounce at the coldest reached; at room temperature at most 21 ms (the model's 23 C worst plus 1 ms) as the early warning |
| BM-4 | hold stability: taps on the case at the (r2) 4.89 V key-down hold while capturing pole B | no interruption |
| BM-5 | straight-key and paddle bounce of the owner's keys (WP-PDR-40) | at most 1.957 ms (REQ-SYS-160), 0.9 ms (REQ-SYS-159), or the conditions go to the owner |
| BM-6 (r1) | limiter output with the coil as load, from a bench supply at (r2) 4.99, 6.21 and 8.4 V, at room temperature and with the limiter heated to 85 C | (r2) at least 4.89 V at 4.99 V (dropout at most 0.10 V); at least 6.11 V at 6.21 V; at most 6.43 V at 8.4 V |
| BM-7 (r1) | logic capture of TR_DRV over a test over; a fault-injection TR_DRV dip of 5 ms under RF into the dummy load | 2 TR_DRV edges per over; on the dip, the PA output removed by the gate before pole A opens, and the backstop count not restarted |

## 10. Uncertainty and limitations

1. **The relay model is class E.** It is a lumped magnetic circuit without saturation, eddy currents or contact-spring detail. It is anchored only at the datasheet limits and swept over a band that the release anchor prunes. The conclusion that option A cannot be guaranteed at 75 and 85 C does not depend on the model: it follows from the datasheet must-operate limit and the copper coefficient (section 4.2 first table). The operate and release times of options B to E do depend on it.
2. **Worst-case unit.** The unit is at both datasheet limits at once (75 % must-operate and 7 ms operate). A typical unit is faster. The analysis claims no typical figure.
3. **(r1) The H1 slope is a graph read** of 10 samples, applied proportionally to the 75 % worst unit. The band covers two reads and two reference temperatures (section 3.3). A proportional slope on the 75 % unit is the steeper of the two ways to apply it (the additive form, 0.26 to 0.32 points of rated per K, gives a lower must-operate voltage at 85 C). The spring-force scaling that carries it into the dynamics is a modelling choice; the hold ratios of K15 do not depend on it.
4. **(r1) The maximum-voltage curve is a graph read** (knee at about 54 C, 151 % at 70 C). K19-E has 22.5 points of margin, so the read does not decide it. K19-CD fails for any read within a few percent.
5. **Coil temperature corners** add an estimated self-heating (40 to 80 K/W) to the thermal note's bay air, which is itself an estimate with a stated band. Option E's highest coil power (0.221 W at 85 C on a -10 % unit) sits 0.004 W inside the 85 C corner's assumption.
6. **(r1) The limiter is a behavioural model** (a set point and a constant dropout). Its load and line transients, its start-up and its stability with the coil are part checks at WP-PDR-37 and BM-6. The pull-in happens in receive, before TX_KEY at t0 + 8 ms, so the key-down sag does not act on it. The key-down hold uses the lowest rail. (r2) That rail rests on the WP-PDR-21 revision 3 feed bound and p4 current (under review) and on a 0.10 V discharge allowance (class E; `s3-keydown-hold.png` panel (b) shows the hold against it). The feed bound is used for the receive state too, which overstates its drop there. The key-down current is taken at 6.4 V and used at 6.30 V, which overstates it by about 1.5 %.
7. **Bounce** is a graph read at 12 VDC and rated overdrive; BM-2 measures it.
8. **Inputs under review.** The 0.650 ms C6 write time, the lock-gated start, A_kd and the 82.8 ms refresh come from `frequency-budget.md` revision 4, and the 0.25 ms turn-on bound from `pa-permit-gate-d18.md` revision 1. A change there changes K8, K8b, K9, K20 and rows KD-06 to KD-09 and SR-01 to SR-04; the 1 ms allocations of this note do not depend on them.
9. **Software latencies** (0.02 ms keyer test point, 2 ms compare, 0.5 ms end-of-over order, 1 ms inhibit response) are allocations for WP-PDR-32 to confirm in the software timing analysis.
10. **Not covered:** the receiver's recovery after the release (WP-PDR-19), the relay's RF isolation (23b), the keying loop's response to a late contact or a drop-out (22), the backstop circuit (26).

## 11. Reproduction and visual closure

```
cd /Users/robinonsay/rust/cwht
.venv/bin/python hardware/sim/tx-seq/seq_run.py all --expect    # exit 0; about 6 min with the LTspice lock free
                                                                 # (CWHT_LTSPICE_LOCK_WAIT raises the lock wait)
```

Plots, each opened and inspected by the author before this note cites it (rule C5), all in `hardware/sim/tx-seq/results/`:
- `2026-09-29-r2-s1-drive/s1-coil-current.png` and `s1-coil-voltage-vs-pack.png`;
- `2026-09-29-r2-s2-coil/s2-coil-transient.png`;
- `2026-09-29-r2-s3-operate/s3-operate-vs-coil-temperature.png`, `s3-release.png`, `s3-limiter-setpoint.png` and (r2) `s3-keydown-hold.png`;
- `2026-09-29-r2-s4-sequence/timing-diagram.png` (identical to `docs/reviews/PDR/figures/timing-diagram.png`), `s4-keydown-budget.png`, `s4-margins.png` and `s4-stale-ratio.png`.

`coil_tran.raw` of r2-s2 (8,010,152 bytes) is kept in its run folder and not committed; its SHA-256 `49905b7b...88dd73ff` is in `raw.sha256` (CR-017 C2). `drive_dc.raw` of r2-s1 (579,766 bytes) is committed. (Revision 1: r1-s2 `coil_tran.raw`, 8,013,112 bytes, SHA-256 `f8f577f6...c3f67e9d`.)

## 12. References

- `docs/plan/pdr-work-plan.md` revision 6, WP-PDR-23 and 23a; status note `docs/plan/status/status-2026-09-29.md` section 8.
- TS-012 revision 8, `docs/decisions/trade-studies/TS-012-design-to-cost-hand-built.md` (`bb5dee7`).
- `docs/design/analysis/frequency-budget.md` revision 4 (`d030ce2`); `pa-permit-gate-d18.md` revision 1 (`c397ab1`); `keying-ts012.md` revision 2 (`be86c02`); `thermal-ts012.md`; `keyer-host-study.md` (input I-7).
- `docs/process/07-software-engineering-plan.md` section 14.2 rows b, c, h, j; `docs/safety/hazards.json` HZ-004 K12, HZ-008 C5 and C6, HZ-014 C5 and K8; `docs/safety/hazard-analysis.md` section 5 and section 8.2 row 3; `docs/test_cases/sys/test_cases.json` TC-SYS-024, 030, 102.
- Omron G5V-2 datasheet K046-E1-06, https://omronfs.omron.com/en_US/ecb/products/pdf/en-g5v_2.pdf (SHA-256 `7a0edd84...fc9d55a`): Ratings and notes 1 to 3, Characteristics, page 2 graphs "Ambient Temperature vs. Maximum Coil Voltage" and "Ambient Temperature vs. Must Operate or Must Release Voltage".
- RP2350 datasheet section 8.1.4, Tables 542 and 582; onsemi 2N3904; AOS AO3400A Rev 3.1; TI LM2940 SNVS769J.

## 13. Revision 1: the Major findings and where each is fixed

| Finding | Fix | Where | New result |
|---|---|---|---|
| Review finding-1 (CK-ANA-A4/E3): the 168 % pull-in exceeds the H1 maximum from its graph; state whether the limit applies to the PWM average or the peak | Graph read and applied. The limit applies to the imposed (peak) voltage (ratings note 3, graph note), so no PWM cap meets it. The capped pull-in (150 % or less) is made in hardware: option E, a 6.3 V coil-supply limiter with a static drive, is the recommendation | sections 2, 3.2, 4.3, 5 (K19-CD, K19-E), 6.1; `seq_run.py` s1 branch E, `vmax_h1_pct`, K19 split; plot `s1-coil-voltage-vs-pack.png` | C, D 168 % against 167/156/151 % (FAIL); E at most 128.5 % against 151 % (PASS) |
| Review finding-2 (CK-ANA-A4/B3): H1 must-operate slope 0.48 to 0.51 %/K, not 0.393 %/K; KD-12 and BM-2 change | Slope band in the model (0.48 %/K from 23 C to 0.51 %/K from 20 C), applied to operate, hold and release; KD-12 and BM-2 restated | sections 2, 3.3, 4.2, 4.3, 8 (KD-12), 9 (BM-1, BM-2); `relay_model.py` `k_mo`, `force_scale`, `i_pickup`; s3 slopes; check `slope_law` | C at most 8.36 ms (review 8.00 to 8.40), D 7.13 ms (6.91 to 7.16), E 7.89 ms; D hold 1.001 to 1.028 (review 1.00 to 1.02), E hold 1.051 to 1.079; KD-12 3.83 to 8.39 ms; BM-2 at 6.15 V, coil 85 C, at most 8.5 ms |
| Review finding-3 (CK-ANA-F1/F3): the release is analysed only at 85 C with 5.0 V; at -10 C with the duty-rule 5.6 to 5.83 V it is 23.6 to 24.0 ms | Release at -10, 23 and 85 C from every end-of-over hold of each option | sections 2 (corners), 4.4, 5 (K12-A, D, E), 8 (KU-07), 9 (BM-3); s3 `REL_TEMPS`, `_release_holds`; plot `s3-release.png` | C, D 24.78 ms with ordering and bounce (release 23.35 to 23.78 ms); E 25.86 ms, margin 4.14 ms |
| Review finding-4 (CK-ANA-F2/A6): the R-FRESH-2 stale-ratio key-down case is missing | Outcome fixed as "elements not radiated"; the late element rejected; the REQ-SYS-160 effect stated and sent to the owner | sections 1, 4.8, 5 (K20-a, b, c), 6.2, 7, 8 (SR-01 to SR-04); s4 `stale_ratio_case`; plot `s4-stale-ratio.png` | every radiated element keeps 9.980 to 10.043 ms; at most 2 elements not radiated; REQ-SYS-160 not met in the 82.8 ms window (FAIL, to the owner) |
| SA finding-1 (swe-205 7.1 task 1, SA-C-i): the 25 kHz hold PWM on TR_DRV defeats the K12 monostable and the PA-path gate's T/R input | TR_DRV is a static level (option E); the backstop's level trigger and 30 ms re-arm qualification, and the gate's T/R input, routed | sections 4.9, 5 (K21-CD, K21-E), 6.1 item 3, 6.2 (WP-PDR-16, 22, 26, 35, 37, 43), 8 (KD-04, KD-17, KU-06), 9 (BM-7) | E: 2 edges per over, T_rearm 30 ms against a 25.86 ms release (PASS); C, D: 50 k edges per second (FAIL) |
| SA finding-2 (swe-205 7.1 task 1, SA-C-f/g/i): firmware-set duty, PWM and pull-in with no integrity provision; nothing in hazards.json; REQ-SYS-156 detection not named | Option E has no firmware-set coil parameter; the remaining hardware failure modes are tabulated with their detection (REQ-SYS-156 named) and proposed to WP-PDR-16 | sections 4.9, 5 (K22-CD, K22-E), 6.1, 6.2 (WP-PDR-16, 22, 23b), 9 (BM-6) | C, D: a 0.1 to 2.4 % reading error loses the hold, a stuck pull-in holds 168 % (FAIL); E: coil voltage bounded in hardware in every firmware state (PASS) |

Minor findings of iteration 1 are not addressed in this revision (rule C1). The schedule results (sections 4.1, 4.5 to 4.7) and their criteria are unchanged.

## 14. Revision 2: the Major findings of the delta iteration and where each is fixed

| Finding | Fix | Where | New result |
|---|---|---|---|
| Review finding-13 (CK-ANA-A4/E3/F3): K15-E rests on a 5.45 V key-down rail; the REQ-SYS-097 tolerance (an over can start at 6.30 V) and the WP-PDR-21 r3 feed bound (0.5646 ohm at +45 C key-down, `f1070cf`) are left out; with them the hold is 0.995 to 1.021 x at an 85 C coil and the pull-in corner moves to 6.05 V | The rail floor restated: pack 6.30 V; feed bound 0.5646 ohm (+45 C) and 0.614 ohm (-10 C) with the modelled key-down current from the p4 `.raw` (2.140 and 2.215 A, larger than 2 A); 0.10 V discharge allowance; receive floor with the feed bound and the coil's own current. Limiter dropout requirement tightened to 0.10 V. K15-E shown at the restated floor and marked **OPEN**, with its two closing paths (the WP-PDR-21 P-FET lever, or BM-1). K22-E restated so that it tests firmware parameters only. KD-12, BM-1, BM-2, BM-4 and BM-6 restated | sections 2, 3.2, 4.1, 4.2, 4.3, 4.4, 4.9, 5, 6.1 items 2, 3 and 7, 6.2 (WP-PDR-21, 24), 8 (KD-12), 9, 10 item 6; `seq_run.py` `rail_rx_floor`, `rail_kd_floor`, holds `kd_hot0`, `kd_hot`, `kd_lever`, `kd_cold`, `coil_temp_lowpack`, checks `hold_ratio_closed_form` and `p4_feed_current`; plot `s3-keydown-hold.png` | E hold 0.980 to 1.005 x at 4.89 V (0.9997 to 1.026 x at the start of the over; 1.050 to 1.077 x with the lever; coil's own temperature at most 83.8 C, 0.984 x): K15-E OPEN. Pull-in floor 6.11 V: operate 8.07 ms, 8.57 ms with bounce (K1b-E PASS, KD-12 to 8.567 ms). K12-E unchanged at 25.86 ms |
| Review finding-14 (CK-ANA-E5/A5): the REQ-SYS-160 condition (2) for the owner, "after an over longer than 10 s", states the wrong trigger; the rule works on the ratio's age at t0, which includes up to 1.083 s of age in receive (FR-2r) | The condition, K20-c and SR-01 restated on the ratio's age at the closure; the over lengths that can give it computed from A_kd, the receive age, the ordering and the refresh; the TC-SYS-102 set-up stated on the ratio age | Summary, sections 2, 4.8, 5 (K20-c), 7 (REQ-SYS-160), 8 (SR-01); `seq_run.py` `stale_ratio_case` (`over_min_s`, `keying_min_s`), K20-c, SR-01, `s4-stale-ratio.png` label | the case can arise after an over longer than 8.83 s (1.63 s of keying with the 7.2 s hang) and always does after one longer than 10 s; closures within 83.3 ms of the hang expiry. K20-a, K20-b and K20-c states unchanged |

Minor findings are not addressed (rule C1). Options C and D keep the revision 1 rail values (`v_rx_min`, `v_kd_min`) as the comparison; their rejection rests on K19-CD, K21-CD and K22-CD, which do not depend on the floor, and a lower floor would only worsen them.

## Change history

| Revision | Date | Change | Commit |
|---|---|---|---|
| 0 | 2026-09-29 | First issue (WP-PDR-23a), frozen at F0 for the independent review and its SA pair | `95adefc` |
| 1 | 2026-09-29 | The six Major findings of iteration 1 (review findings 1 to 4, SA findings 1 and 2; section 13). H1 must-operate slope and maximum-voltage curve read from the datasheet graphs; the limit applies to the imposed (peak) voltage. D-5 recommendation changed to option E (H1 coil through a 6.3 V coil-supply limiter, AO3400A, static TR_DRV, no PWM). Release at -10, 23 and 85 C. The R-FRESH-2 outcome fixed as "elements not radiated", with the REQ-SYS-160 condition to the owner. TR_DRV as a static level for the K12 backstop and the PA-path gate; option E failure modes with their detection. New runs `2026-09-29-r1-s1-drive` to `-r1-s4-sequence`; criteria K1b-E, K12-E, K15-E, K19-CD, K19-E, K20-a to c, K21-CD, K21-E, K22-CD, K22-E; timing-table rows KD-04, KD-12, KD-17, KU-06, KU-07, SR-01 to SR-04; BM-1 to BM-4 restated, BM-6 and BM-7 added. Inputs re-checked against `frequency-budget.md` revision 4 and `pa-permit-gate-d18.md` revision 1: values unchanged. Minor findings not addressed (rule C1) | `8ca7d05` |
| 2 | 2026-09-29 | The two Major findings of the delta iteration (review finding-13 and finding-14; section 14). Option E rail floor restated from the REQ-SYS-097 tolerance (6.30 V), the WP-PDR-21 revision 3 feed bound and its p4 key-down current, and a 0.10 V discharge allowance; limiter dropout requirement 0.10 V; K15-E OPEN (0.980 to 1.005 x; closes by the WP-PDR-21 P-FET lever or BM-1); pull-in floor 6.11 V (K1b-E 8.57 ms, KD-12); K22-E restated; BM-1, BM-2, BM-4, BM-6 restated. The stale-ratio case, K20-c, SR-01 and the REQ-SYS-160 condition (2) stated on the ratio's age (possible after an over longer than 8.83 s). New runs `2026-09-29-r2-s1-drive` to `-r2-s4-sequence`; new plot `s3-keydown-hold.png`; checks `hold_ratio_closed_form` and `p4_feed_current`. Minor findings not addressed (rule C1) | this commit |
