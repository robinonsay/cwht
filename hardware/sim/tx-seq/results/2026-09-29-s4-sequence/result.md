# s4 sequence criteria

| Id | State | Criterion | Value | Limit | Basis |
|---|---|---|---|---|---|
| K1 | PASS | ramp start at least 10 ms after the T/R command | 10.000 ms (+0.043 ms PWM quantisation, later only) | >= 10 ms | schedule (A) |
| K1a | PASS | contacts made and bounce ended before the ramp, datasheet point (rated 5.0 V at the coil, coil 23 C) | 7.5 ms | <= 10.0 ms | D, DD |
| K1b-A | FAIL | option A: contacts made and bounce ended before the ramp at every corner, worst-case unit (model band) | worst no pull-in at min supply, nom coil; at the lowest supply: 49 C coil 12.59 ms nominal set (band to no pull-in), 75 C coil no pull-in (band to no pull-in) | operate + 0.5 ms <= 10.0 ms | E model anchored to D (s3) |
| K1b-B | FAIL | option B: contacts made and bounce ended before the ramp at every corner, worst-case unit (model band) | worst no pull-in at min supply, hot_dl coil; at the lowest supply: 49 C coil 9.65 ms nominal set (band to 12.39 ms), 75 C coil 14.10 ms (band to no pull-in) | operate + 0.5 ms <= 10.0 ms | E model anchored to D (s3) |
| K1b-C | PASS | option C: contacts made and bounce ended before the ramp at every corner, worst-case unit (model band) | worst 7.11 ms at min supply, hot_c coil; at the lowest supply: 49 C coil 5.74 ms nominal set (band to 5.75 ms), 75 C coil 6.44 ms (band to 6.61 ms) | operate + 0.5 ms <= 10.0 ms | E model anchored to D (s3) |
| K1b-D | PASS | option D: contacts made and bounce ended before the ramp at every corner, worst-case unit (model band) | worst 6.32 ms at min supply, hot_c coil; at the lowest supply: 49 C coil 5.35 ms nominal set (band to 5.36 ms), 75 C coil 5.91 ms (band to 5.94 ms) | operate + 0.5 ms <= 10.0 ms | E model anchored to D (s3) |
| K2 | PASS | lead-in at most 12 ms (REQ-SYS-161), every element | 9.980 to 10.043 ms | <= 12 ms | schedule (A); REQ-SYS-161 |
| K2b | PASS | lead-in equal over the over within 0.5 ms (TC-SYS-102) | spread 0.063 ms | <= 0.5 ms | schedule (A) |
| K3 | PASS | straight-key contact to RF rise at most 15 ms (REQ-SYS-160), key bounce 0 | 13.043 ms (3.0 detection + 10.0 lead-in + 0.043) | <= 15 ms | R, schedule |
| K3b | CONDITION | largest key bounce for which K3 holds (bounce aligned with samples, worst case) | 1.957 ms | condition on the key (WP-PDR-40 bounce capture) | R, schedule |
| K4 | PASS | clamps held and integrator parked until the ramp: the D-18 clamp on VGG releases only at TX_KEY with PA_EN high; the reference is held at 0 V until the ramp start | VGG clamp released at 8.0 ms, reference released at 10.0 ms | both at or before the ramp; reference exactly at it | schedule (A); D-18 |
| K5 | PASS | frequency check complete before PA_EN (interval 12) | check done 7.097 ms, PA_EN 7.500 ms | check <= PA_EN | D, A; D-17 |
| K6 | PASS | PA_EN before TX_KEY | 7.500 <= 8.000 ms | PA_EN <= TX_KEY | schedule (A) |
| K7 | PASS | driver supply and bias settled before the ramp | 9.000 ms | <= 10.0 ms | A (t_drv allocation); pa-permit-gate-d18.md rev 0 |
| K8 | INFO | Si5351A relock margin beyond the 1 ms allocation (interval 12) | 0.903 ms (TS-012 revisit condition assumes 3 ms) | >= 0 | schedule |
| K9 | FAIL | interval-13 fallback (TS-012: check at t0 + 11, ramp at t0 + 11.5) inside the 12 ms lead-in, with PA_EN before TX_KEY and the 2 ms TX_KEY lead | needs L >= 13.193 ms; only with PA_EN after TX_KEY and the D-18 turn-on bound of 0.25 ms (pa-permit-gate-d18.md rev 0) L >= 11.443 ms, i.e. 0.06 ms margin at 11.5 ms with no relock margin | <= 12 ms | schedule |
| K8b | INFO | latest lock-gated FC0 start that still sets PA_EN by TX_KEY (interval 12) | t0 + 1.903 ms (frequency-budget.md rev 2 RL-4 gives 2.0 ms on a 4.0 ms interval) | input to WP-PDR-20a | D, A |
| K10 | PASS | cold switching at key-up: T/R released only after TX_KEY is low (50 WPM, 3-dit hang, 8 ms fall) | margin 52.96 ms | >= 0 | R, schedule |
| K11 | PASS | REQ-SYS-044 floor of 3 dits against the relay and envelope timing (input to WP-PDR-23b) | 72 ms hang against 19.04 ms of lead-in, fall and tail | hang >= that | R, schedule |
| K12-A | PASS | option A (and B): T/R release share of REQ-SYS-036 (ordering, release from 76 mA with the freewheel diode, NC bounce) | 13.46 ms (nominal set 7.16) | <= 30 ms of 50 | E model (s3) |
| K12-D | PASS | option D (and C): T/R release share of REQ-SYS-036 (ordering, release from 24 mA with the freewheel diode, NC bounce) | 13.92 ms (nominal set 7.32) | <= 30 ms of 50 | E model (s3) |
| K13 | PASS | hold PWM ripple at 25 kHz | 2.27 % | <= 5 % | LTspice (s2) |
| K14 | PASS | D-5 pull-in at 100 % lasts at least twice the worst operate time (options C, D) | 25 ms against 2 x 7.11 ms | t_pi >= 2 t_op | A, E (s3) |
| K15-B | OPEN | option B: hold at 63 % of the coil voltage guaranteed by the datasheet (hold current at least the worst unit's must-operate current) | 0.64 x; model band: hold/release current down to 0.74 | >= 1.0 | D; E model |
| K15-D | PASS | options C and D: hold at 5.0 V average guaranteed by the datasheet | 1.07 x (coil 85 C) | >= 1.0 | D |
| K16 | PASS | RF off on an inhibit (REQ-SYS-004, input to WP-PDR-23b) | 1.1 ms | <= 20 ms | A, E |
| K17 | PASS | sidetone onset (REQ-SYS-159, input to WP-PDR-23b), key bounce 0 | 3.1 ms; holds for bounce up to 0.9 ms | <= 4 ms | R, A |
| K18 | PASS | per-element TX_KEY windows do not overlap at 50 WPM with 8 ms ramps | gap 13.0 ms | >= 0 (else TX_KEY stays high: merge rule) | R, schedule |
| K19 | OPEN | options C and D: pull-in at the full pack against the H1 maximum coil voltage (180 % at 23 C) | 168 % for 25 ms | <= 180 % at 23 C; the curve at 70 C is a graph read at the gate | D |

Checks: schedule_monotonic PASS, upstream_checks PASS
