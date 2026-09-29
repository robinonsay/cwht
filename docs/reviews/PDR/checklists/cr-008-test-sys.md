---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md section 13
# is the single field list; docs/process/08-agent-briefing.md section 3.2). Checklist:
# docs/templates/peer-review-checklist-test.md revision B, as INSP-025 used for the TC-SYS cases.
# This record is the INSP-025 delta iteration that PDR work plan WP-PDR-11 names ("Reviewer: INSP-003 and
# INSP-025 delta iterations"), filed under PDR per plan section 3.1 "Records". Its companion for the L1
# requirements (the INSP-003 delta) is docs/reviews/PDR/checklists/cr-008-requirements-sys.md (INSP-044).
# The product is the TC-SYS part of CR-008 (Submitted, proposed Class I), prototyped on branch
# cr/CR-008-srr-liens-l1-and-tc-sys at c629198 and frozen there (plan rule C2).
# CR file re-pin delta (2026-09-29, main 0680af9; WP-PDR-55): delta under plan rule C1 on the drift of the CR file,
# 3b9266ff (4dab5dc) to aa65e826 (cccbfda, a244b05, 6485bd3, a17af87, 9c40ef9, 726cd44); the CR sections this record
# used changed (section 4 Interfaces row, section 5, front matter), so a delta, not a removal. Iteration stays 1: a re-pin
# delta is not a new review iteration (INSP-003 convention).
id: INSP-045
checklist: peer-review-checklist-test
checklist_revision: B
checklist_file: docs/reviews/PDR/checklists/cr-008-test-sys.md
product: docs/test_cases/sys/test_cases.json
# product_commit: the branch head that holds the frozen blobs (base ab2af2d on main); the CR file is on main at 4dab5dc
# re-pin delta: product_commit stays c629198 (the four frozen blobs, equal at the branch head e26ce46); the CR file is on main at 726cd44
product_commit: "c6291980c83e6e1e55b66ceff2e0b89222669b97"
# product_files at iteration 1: the four as below and docs/cm/cr/CR-008-srr-liens-l1-and-tc-sys.md@3b9266ff0d9d29e7d1b70febd1fe7cfbd86ab3dd
product_files: ["docs/requirements/sys/requirements.json@a73449377e8d055f5d247130b8850bf3f5a151d9", "docs/requirements/sys/requirements.md@4e110b16027fbe446e846a8c5f9d2dc5c2899af6", "docs/test_cases/sys/test_cases.json@117c08dedd65171f88d5bff015d0914db97b3065", "docs/test_cases/sys/test_cases.md@00e4454f5c836df0eac430b9ec9f95b99630d316", "docs/cm/cr/CR-008-srr-liens-l1-and-tc-sys.md@aa65e8261da4193707b561dba6e8a841451cf88f"]
product_size: 114 cases (Bench 77, Simulation 23, Inspection 14; Test 71, Analysis 23, Inspection 14, Demonstration 6), all Draft; 65 added or changed (1 added, 28 with content changes, 36 photograph only)
sprint: PDR-prep
author_agent: "test-author:WP-PDR-11 (same invocation as the L1 requirements author; CR-008 section 4 independence note)"
# implementation_author_agent: no schematic, layout or firmware under these cases exists
implementation_author_agent: none (no design or code under test exists)
reviewer_agent: "reviewer:WP-PDR-11-INSP-025-delta"
# criticality: system L1 cases (module SYS), not a software component of 07 section 14.1 (as INSP-025)
criticality: neither
assurance_required: false
assurance_reviewer_agent: none
iteration: 1
readiness_met: true
reviewer_verdict: APPROVED
assurance_verdict: not-required
# verdict: held at NEEDS CHANGES on the completion criterion "validate_docs.py passes on the record" only.
# The reviewed blobs are on the CR branch, not in main HEAD; tools/validate_docs.py fails an APPROVED
# record whose product_files are not in HEAD (record drift rule). The software lead sets APPROVED when
# CR-008 merges with these blobs unchanged (section "Record verdict"; precedent INSP-031). The re-pin delta keeps the hold.
verdict: NEEDS CHANGES
# re-pin delta counts: finding-1 to finding-3 Open to Lien (rule C1: CR-008 dispositioned Approved on 2026-09-28 without a
# revision; due at the CDR readiness declaration), counted in findings_deferred; no new finding. Was open 3, deferred 0
findings_major: 0
findings_minor: 3
findings_open: 0
findings_fixed: 0
findings_verified: 0
findings_deferred: 3
assurance_findings_major: 0
assurance_findings_minor: 0
assurance_tasks_applied: []
decision_tables_checked: 0
deferred_rids: []
items_no: [CK-TEST-A6]
# effort: iteration 1 (40 turns, 80 min) plus the re-pin delta (12 turns, 25 min)
effort_turns: 52
effort_minutes: 105
record_status: Open
date: 2026-09-27
date_closed: null
---

# Peer review record INSP-045: CR-008, TC-SYS case liens of INSP-025 (WP-PDR-11, INSP-025 delta)

**Product.** The TC-SYS cases `docs/test_cases/sys/test_cases.json` (blob `117c08de`) and their rendering `test_cases.md` (blob `00e4454f`) on branch `cr/CR-008-srr-liens-l1-and-tc-sys` at `c629198`, checked against the amended L1 requirements (blob `a7344937`) and CR-008 (blob `3b9266ff` on `main` at `4dab5dc`). Blob identity checked with `git rev-parse`; on `main` the files equal `baseline/srr`, so the diff reviewed is `baseline/srr` to `c629198`.

**Checklist.** `docs/templates/peer-review-checklist-test.md` revision B, sections A, H and I for Bench, Simulation and Inspection system cases as INSP-025 applied them; sections B to G (test code, mock clock, coverage, emulation, regression) are N/A for L1 system cases with no code, as in INSP-025.

**Acceptance criteria (rule C7, every case the governing clauses enumerate).** Every lien of the INSP-025 lien table after the delta (finding-2, 3, 4, 5, 7 for TC-SYS-073, 8, 9, 10, 11, 12) on every case each names; the case side of INSP-003 finding-25 (TC-SYS-013, 030, 031, 034, 038, 050, 056, 064, 065, 102) and finding-31 (i) (TC-SYS-111, 112, 113); new TC-SYS-116; the CR-008 section 5 items "for each of the 57 photograph additions that the case is Bench and had no photo", "the TC-SYS-060 guard arithmetic at the six points", "the TC-SYS-064 points", "that TC-SYS-111 can reach constant current with one cell at 3.70 V", and "no other line changed". Each case change was read as author-written and checked against the requirement text alone (CR-008 section 4 independence note).

**Independence (rule C4).** This invocation authored no part of WP-PDR-11, CR-008 or the branch, and edited no product file. **Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` was queried before any manual search (queries listed in INSP-044); `grep -n` only pinned lines. **Method.** Field-level diff of every case by script; the rendering checked section by section against the JSON by script (every title, type, method, status, requirement id, setup, step, criterion, instrument, artifact and `automation_ref` present in its `### TC-SYS-NNN` section: 114 sections, 0 mismatches; the same script gives 0 mismatches on `baseline/srr`).

## Record

### Findings (filled by the reviewer)

| Finding | Origin | Severity | Item | Location | Description | State |
|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | reviewer | Minor | CK-TEST-A6, CK-TEST-A5 | TC-SYS-036 `setup`, `procedure`, `acceptance_criteria` | The INSP-025 finding-10 fix adds to the criterion "the capture shows TX_KEY keying through the whole of each hand-keyed minute", but the case never captures TX_KEY: the Configuration captures "both key inputs at the test pads" only, and no step connects TX_KEY to a channel. TC-SYS-105, fixed for the same finding, adds the step "connect TX_KEY to a capture channel" and the setup sentence; TC-SYS-036 does not. As written the new clause cannot be evaluated, so a run is blocked or judged by eye. Minor: it blocks a run rather than passing a bad unit, and the key-input criterion, the purpose of REQ-SYS-051, is unaffected. Fix: add TC-SYS-105's TX_KEY capture sentence and step to TC-SYS-036 | Open |
| <a id="finding-2"></a>finding-2 | reviewer | Minor | CK-TEST-A6, CK-TEST-C2 (INSP-025 finding-11, INSP-003 finding-31 (ii), residual) | TC-SYS-111 `setup`, `acceptance_criteria`; REQ-SYS-185 `verification_note` | Holding the other cell at 3.70 V keeps the pack (7.95 to 8.10 V over the sweep) below the 8.40 V pack regulation, so a pack-regulating charger stays in constant current, as CR-008 section 5 asks to confirm. But the charger of HZ-002 K1 (`docs/safety/hazards.json`: "BQ25887 class: 2S CC-CV to 4.20 V +/-0.5 percent per cell with battery OVP", with balancing) may act per cell: per-cell regulation or cell over-voltage protection would cut the current while the raised cell is between 4.20 V and 4.40 V whatever the layer under test does. The criterion now judges the path by the charge current alone and keeps the switching-element voltage as data, the reverse of the finding-11 fix ("decide open and closed by the switching-element voltage with a numeric threshold ... keep the current as supporting data"). A per-cell charger cut below 4.30 V fails a good unit (the "stays above 1 mA below the trip" clause); a charger cut inside 4.30 to 4.35 V could pass a unit whose layer does not open, so the "independently of charger" part of REQ-SYS-185 is not shown. Minor, not Major: the charger is not selected until PDR (TS on the power tree), the case is Draft until TRR, and the recorded switching-element voltage exposes the case. Fix: add to the criterion that the voltage across the layer's switching element exceeds a stated threshold at the trip (the layer itself opened), or add a setup condition that the charger's per-cell regulation, balancing and cell OVP are disabled or set above 4.40 V, confirmed from the selected charger's datasheet at PDR | Open |
| <a id="finding-3"></a>finding-3 | reviewer | Minor | CK-TEST-A6, CK-TEST-I2 | TC-SYS-034 `acceptance_criteria` | The new criterion records "the delay from 2 ms and 5 ms to each acceptance ... as data; its bound is the keying latency of REQ-SYS-043". REQ-SYS-043 bounds only a paddle-initiated element start ("within 3 ms of paddle closure while no element is in progress"); it does not bound a straight-key closure (REQ-SYS-160, 15 ms to the RF rise, is the nearest) or any key opening (no L1 bound; REQ-SYS-042 element timing applies only to keyer-generated elements). The sentence is data-only and does not change pass or fail, so it is Minor. Fix: name REQ-SYS-043 for paddle closures and REQ-SYS-160 for straight-key closures, and state that openings carry no L1 upper bound (a PDR item for REQ-SW-KEYER-021 with WP-PDR-35 and WP-PDR-40) | Open |

**Counts.** 3 findings, all Minor; open Major 0. Under plan rule C1 each Minor finding is a lien if CR-008 is not revised before its disposition. The TC-SYS-065 residual (5 mA "charging stopped" level taken from siblings) is INSP-044 finding-1, not counted here.

### Lien verification (INSP-025 lien table after the delta; case side of INSP-003 finding-25 and 31)

| Lien | Required fix | Evidence on the frozen blob | Result |
|---|---|---|---|
| INSP-025 finding-2 | TC-SYS-003: connect attenuator and tinySA, S21 sweep, calibration-output check; TC-SYS-008 step 5: tinySA level at each out-of-range frequency | TC-SYS-003 Configuration: "the antenna port goes to the calibrated power attenuator and the tinySA Ultra (zero span at the set frequency, max-hold) for every attempt of F1 to F4"; new step 2 connects both, sweeps S21 on the NanoVNA to 1.5 GHz and runs the calibration-output check; steps F1, F2 (flags, inhibits, USB alone) and F4 read the tinySA level; artifacts gain the S21 Touchstone file and the traces; `instruments` already list the tinySA through the calibrated attenuator, the NanoVNA and the dummy load. TC-SYS-008 step 5 reads "the display transmit-state field and the tinySA level at the set frequency (zero span, max-hold)" at 144.0005, 147.9995, 144.0011, 147.9989, 143.999 and 148.000 MHz | Verified |
| INSP-025 finding-3 | TC-SYS-014 wording in the ten RF-off criteria | Character diff of each criterion: TC-SYS-003, 008, 047, 066, 082, 083, 101, 108, 109 add ", corrected for the attenuator and increased by the tinySA level accuracy"; TC-SYS-066 also adds "on the tinySA Ultra"; TC-SYS-110 adds it to both of its RF-off clauses; nothing else changed in those criteria; each case's setup names the attenuator and its instruments the tinySA | Verified |
| INSP-025 finding-4 | TC-SYS-064 points at the threshold plus the fixture setting accuracy | Setup defines a (cell-simulator setting uncertainty plus multimeter accuracy, recorded); points 300 mV + a, 2.5 V - a, 4.3 V + a, 100 mV + a; each is on the violating side of its threshold, so a compliant unit is never required to refuse inside its window and the point is as close to the limit as the fixture allows (04 section 8.2). Steps and criterion use the same points; the 5 mA and 0.5 V levels now come from REQ-SYS-087, 088 and 166 | Verified |
| INSP-025 finding-5 | TC-SYS-061 cites the room-temperature companion only | TC-SYS-061 title "... at room temperature", criterion "at 18 C to 28 C", "The 0 C to 45 C span is REQ-SYS-194, closed by TC-SYS-116"; `requirement_ids` REQ-SYS-083 only. New TC-SYS-116: Analysis, Simulation, `automation_ref` `hardware/sim/checks/protector_threshold_temp.py` (planned), design data at `baseline/cdr`, a BOM and schematic diff check, worst-case threshold at every temperature from 0 C to 45 C inside 4.25 to 4.30 V, the "Analysis accepted per RSK-NNN" risk sentence of the file's Analysis cases, two artifacts with `artifact_type` | Verified |
| INSP-025 finding-7 | TC-SYS-073 names its checker (TC-SYS-086 moot, Inspection) | `automation_ref` `hardware/sim/checks/sma_mating_life.py` (planned); Configuration says what it computes; new run step; artifact `mating-life-check.log.txt` of type `log` | Verified |
| INSP-025 finding-8 | Setup photograph on the 56 listed Bench cases plus TC-SYS-112 | Script: 57 cases gained a `photo` entry, exactly the 56 of the finding plus TC-SYS-112 (symmetric difference empty); all 57 are Bench and had no photo; every Bench case of the file now has one; each entry cites 04 section 8.1 (line 310 maps setup layouts to a `photo` entry); 36 of the 57 changed only by this entry; no artifact was removed except the TC-SYS-060 bracket report, replaced by a wider description of the same file | Verified |
| INSP-025 finding-9 | TC-SYS-060 guarded inward at every point | T_cold_stop = -2 C + e, T_cold_run = +2 C - e, T_warm_run = 43 C + e, T_warm_stop = 47 C - e, T_hot_on = 58 C + e, T_hot_off = 62 C - e. Arithmetic, cold threshold (charging stops below it): stopped at a setting of -2 + e means the true temperature is at least -2 C, so the threshold is above -2 C; running at +2 - e means the true temperature is at most +2 C, so the threshold is at or below +2 C. The warm (43, 47) and REQ-SYS-099 (58, 62) points bracket 45 +/- 2 C and 60 +/- 2 C the same way. A passing unit therefore has every threshold inside its tolerance whatever the fixture error, the sentence the finding said was untrue is now true, and the accepted guard band is stated. Steps and criterion use the six named points | Verified |
| INSP-025 finding-10 | Word spaces of at least 10 dits; the capture shows full-length keying | TC-SYS-105: fixture word spaces of 10 dits (0.6 s at 20 WPM; qualifying gap 7 x 60 ms = 420 ms, below 500 ms), hand keying with 10-dit word spaces, TX_KEY on a capture channel, pulse-train check step, logic capture in `instruments`, criterion clause. TC-SYS-036: 10-dit word spaces in the hand-keyed minute and the criterion clause, but no TX_KEY capture (finding-1) | Verified for TC-SYS-105; TC-SYS-036 residual finding-1 |
| INSP-025 finding-11 | Other cell low enough for current to flow; decide the state by a measure that is not the charger's | Other cell at 3.70 V (pack 7.95 to 8.10 V over the sweep, below the 8.40 V pack regulation, so current flows below the trip: confirmed); the REQ-SYS-087 refusal also disabled (the 4.25 V against 3.70 V difference would otherwise trigger it); open judged by the 1 mA of REQ-SYS-185. Per-cell charger action is not excluded (finding-2) | Verified in part; residual finding-2 |
| INSP-025 finding-12 | `test_cases.md` summary lists TC-SYS-049 with the fitted cases | The 2026-09-26 revision line now lists TC-SYS-049 "(the generator kept at 0.5 W in four 110 s entries)" among the cases fitted to the limits, with "(corrected by CR-008, INSP-025 finding-12)"; a 2026-09-27 revision line summarizes CR-008; counts 114 cases, 189 of 189, Analysis 23, Demonstration 6, Inspection 14, Test 71; Bench 77, Inspection 14, Simulation 23 equal the JSON (script) | Verified |
| INSP-003 finding-25 (case side) | Each case takes its value from the requirement | TC-SYS-013 ("tolerances are those of REQ-SYS-014"), 030 (REQ-SYS-044), 031 (REQ-SYS-045), 050 (REQ-SYS-093, now "below 5 mA" with meter accuracy added), 056 (REQ-SYS-077, one capture sample period added), 064 (REQ-SYS-087, 088, 166), 102 (REQ-SYS-161); one-sided bounds with the 04 section 8.2 rule inward: TC-SYS-034 (each duration less one sample period against the 2 ms and 5 ms minima), 038 (each time plus one sample period against 5 s, 30 s, 2 s; the +0.1 s allowances removed); TC-SYS-065 takes +/-2 min from REQ-SYS-167 but supplies the "stopped" level itself (INSP-044 finding-1). No "test author's" value remains except TC-SYS-103 (the D-UI-01 legibility metric, outside these findings) (script over every case) | Verified (residuals INSP-044 finding-1, finding-3 here) |
| INSP-003 finding-31 (i) (case side) | TC-SYS-111, 112, 113 take their values from the requirements | TC-SYS-111: 1 mA "the level of REQ-SYS-185"; TC-SYS-112: "The 20 mV band is that of REQ-SYS-186" (defined as the voltage each layer acted at in the baseline, within 20 mV); TC-SYS-113: 120 s and 60 s "measured from the button edge with one capture sample period added", the 0.1 s allowance removed | Verified |


### Case checks (the 28 cases with content changes and TC-SYS-116)

Every case below was read in full at `c629198` against the amended requirement text. The per-case result is in the case table that follows.

- TC-SYS-003, 008: Lien rows finding-2 and finding-3. TC-SYS-003's Environment line still ends "dummy load on the antenna port", which the new Configuration overrides "for every attempt of F1 to F4"; the F5 to F9 attempts keep the dummy load, so the two are consistent (observation, no finding).
- TC-SYS-013, 030, 031, 050, 056, 065, 102: criteria equal the amended statements (REQ-SYS-014, 044, 045, 093, 077, 167, 161); decision rules correct (meter accuracy added to the 5 mA reading; one sample period added to the 20 ms removal delay). TC-SYS-065: INSP-044 finding-1.
- TC-SYS-034: inward rule correct for the minima (duration less one sample period must still be at least 2 ms or 5 ms); the count check keeps a unit that never accepts from passing; finding-3 on the recorded-delay sentence.
- TC-SYS-036, 105: lien row finding-10; finding-1.
- TC-SYS-038: every bound (5 s, 30 s, 2 s) applied with one sample period added, the direction that cannot pass a late unit; the 1.2-times and 0.8-times gap runs and the 5 WPM squeeze data unchanged; consistent with the REQ-SYS-184 note (finding-27 of INSP-003).
- TC-SYS-047, 066, 082, 083, 101, 108, 109, 110: RF-off wording only (lien row finding-3).
- TC-SYS-060, 061, 064, 073: lien rows finding-9, 5, 4, 7.
- TC-SYS-111: lien row finding-11; finding-2.
- TC-SYS-112, 113: lien row finding-31 (i).
- TC-SYS-116: lien row finding-5. `requirement_ids` REQ-SYS-194, method Analysis equal to the requirement's; type Simulation with `automation_ref` (planned, as every Simulation case of the file that has no checker yet); `instruments` empty (design data only); Draft.

### Case table (every added or changed case, 65 rows)

| Case | Type | Fields changed | Lien(s) | Check | Result |
|---|---|---|---|---|---|
| TC-SYS-003 | Bench | setup, procedure, acceptance_criteria, expected_artifacts | INSP-025 finding-2; INSP-025 finding-3; INSP-025 finding-8 | see "Case checks" | Verified |
| TC-SYS-004 | Bench | expected_artifacts | INSP-025 finding-8 | photo entry added (04 section 8.1 line 310); Bench; no photo before; nothing else changed | Verified |
| TC-SYS-007 | Bench | expected_artifacts | INSP-025 finding-8 | photo entry added (04 section 8.1 line 310); Bench; no photo before; nothing else changed | Verified |
| TC-SYS-008 | Bench | procedure, acceptance_criteria, expected_artifacts | INSP-025 finding-2; INSP-025 finding-3; INSP-025 finding-8 | see "Case checks" | Verified |
| TC-SYS-013 | Simulation | acceptance_criteria | INSP-003 finding-25 | see "Case checks" | Verified |
| TC-SYS-014 | Bench | expected_artifacts | INSP-025 finding-8 | photo entry added (04 section 8.1 line 310); Bench; no photo before; nothing else changed | Verified |
| TC-SYS-015 | Bench | expected_artifacts | INSP-025 finding-8 | photo entry added (04 section 8.1 line 310); Bench; no photo before; nothing else changed | Verified |
| TC-SYS-016 | Bench | expected_artifacts | INSP-025 finding-8 | photo entry added (04 section 8.1 line 310); Bench; no photo before; nothing else changed | Verified |
| TC-SYS-022 | Bench | expected_artifacts | INSP-025 finding-8 | photo entry added (04 section 8.1 line 310); Bench; no photo before; nothing else changed | Verified |
| TC-SYS-025 | Bench | expected_artifacts | INSP-025 finding-8 | photo entry added (04 section 8.1 line 310); Bench; no photo before; nothing else changed | Verified |
| TC-SYS-027 | Bench | expected_artifacts | INSP-025 finding-8 | photo entry added (04 section 8.1 line 310); Bench; no photo before; nothing else changed | Verified |
| TC-SYS-028 | Bench | expected_artifacts | INSP-025 finding-8 | photo entry added (04 section 8.1 line 310); Bench; no photo before; nothing else changed | Verified |
| TC-SYS-029 | Bench | expected_artifacts | INSP-025 finding-8 | photo entry added (04 section 8.1 line 310); Bench; no photo before; nothing else changed | Verified |
| TC-SYS-030 | Bench | acceptance_criteria, expected_artifacts | INSP-003 finding-25; INSP-025 finding-8 | see "Case checks" | Verified |
| TC-SYS-031 | Bench | acceptance_criteria, expected_artifacts | INSP-003 finding-25; INSP-025 finding-8 | see "Case checks" | Verified |
| TC-SYS-033 | Bench | expected_artifacts | INSP-025 finding-8 | photo entry added (04 section 8.1 line 310); Bench; no photo before; nothing else changed | Verified |
| TC-SYS-034 | Bench | acceptance_criteria, expected_artifacts | INSP-003 finding-25; INSP-025 finding-8 | see "Case checks" | finding-3 |
| TC-SYS-036 | Bench | setup, procedure, acceptance_criteria, expected_artifacts | INSP-025 finding-10; INSP-025 finding-8 | see "Case checks" | finding-1 |
| TC-SYS-037 | Bench | expected_artifacts | INSP-025 finding-8 | photo entry added (04 section 8.1 line 310); Bench; no photo before; nothing else changed | Verified |
| TC-SYS-038 | Bench | acceptance_criteria, expected_artifacts | INSP-003 finding-25; INSP-025 finding-8 | see "Case checks" | Verified |
| TC-SYS-039 | Bench | expected_artifacts | INSP-025 finding-8 | photo entry added (04 section 8.1 line 310); Bench; no photo before; nothing else changed | Verified |
| TC-SYS-041 | Bench | expected_artifacts | INSP-025 finding-8 | photo entry added (04 section 8.1 line 310); Bench; no photo before; nothing else changed | Verified |
| TC-SYS-042 | Bench | expected_artifacts | INSP-025 finding-8 | photo entry added (04 section 8.1 line 310); Bench; no photo before; nothing else changed | Verified |
| TC-SYS-045 | Bench | expected_artifacts | INSP-025 finding-8 | photo entry added (04 section 8.1 line 310); Bench; no photo before; nothing else changed | Verified |
| TC-SYS-047 | Bench | acceptance_criteria, expected_artifacts | INSP-025 finding-3; INSP-025 finding-8 | see "Case checks" | Verified |
| TC-SYS-048 | Bench | expected_artifacts | INSP-025 finding-8 | photo entry added (04 section 8.1 line 310); Bench; no photo before; nothing else changed | Verified |
| TC-SYS-050 | Bench | acceptance_criteria | INSP-003 finding-25 | see "Case checks" | Verified |
| TC-SYS-051 | Bench | expected_artifacts | INSP-025 finding-8 | photo entry added (04 section 8.1 line 310); Bench; no photo before; nothing else changed | Verified |
| TC-SYS-053 | Bench | expected_artifacts | INSP-025 finding-8 | photo entry added (04 section 8.1 line 310); Bench; no photo before; nothing else changed | Verified |
| TC-SYS-056 | Bench | acceptance_criteria, expected_artifacts | INSP-003 finding-25; INSP-025 finding-8 | see "Case checks" | Verified |
| TC-SYS-057 | Bench | expected_artifacts | INSP-025 finding-8 | photo entry added (04 section 8.1 line 310); Bench; no photo before; nothing else changed | Verified |
| TC-SYS-059 | Bench | expected_artifacts | INSP-025 finding-8 | photo entry added (04 section 8.1 line 310); Bench; no photo before; nothing else changed | Verified |
| TC-SYS-060 | Bench | setup, procedure, acceptance_criteria, expected_artifacts | INSP-025 finding-9; INSP-025 finding-8 | see "Case checks" | Verified |
| TC-SYS-061 | Bench | title, acceptance_criteria, expected_artifacts | INSP-025 finding-5, X1; INSP-025 finding-8 | see "Case checks" | Verified |
| TC-SYS-062 | Bench | expected_artifacts | INSP-025 finding-8 | photo entry added (04 section 8.1 line 310); Bench; no photo before; nothing else changed | Verified |
| TC-SYS-064 | Bench | setup, procedure, acceptance_criteria, expected_artifacts | INSP-025 finding-4; INSP-003 finding-25; INSP-025 finding-8 | see "Case checks" | Verified |
| TC-SYS-065 | Bench | acceptance_criteria, expected_artifacts | INSP-003 finding-25; INSP-025 finding-8 | see "Case checks" | INSP-044 finding-1 |
| TC-SYS-066 | Bench | acceptance_criteria, expected_artifacts | INSP-025 finding-3; INSP-025 finding-8 | see "Case checks" | Verified |
| TC-SYS-067 | Bench | expected_artifacts | INSP-025 finding-8 | photo entry added (04 section 8.1 line 310); Bench; no photo before; nothing else changed | Verified |
| TC-SYS-068 | Bench | expected_artifacts | INSP-025 finding-8 | photo entry added (04 section 8.1 line 310); Bench; no photo before; nothing else changed | Verified |
| TC-SYS-069 | Bench | expected_artifacts | INSP-025 finding-8 | photo entry added (04 section 8.1 line 310); Bench; no photo before; nothing else changed | Verified |
| TC-SYS-070 | Bench | expected_artifacts | INSP-025 finding-8 | photo entry added (04 section 8.1 line 310); Bench; no photo before; nothing else changed | Verified |
| TC-SYS-071 | Bench | expected_artifacts | INSP-025 finding-8 | photo entry added (04 section 8.1 line 310); Bench; no photo before; nothing else changed | Verified |
| TC-SYS-073 | Simulation | setup, procedure, expected_artifacts, automation_ref | INSP-025 finding-7 | see "Case checks" | Verified |
| TC-SYS-081 | Bench | expected_artifacts | INSP-025 finding-8 | photo entry added (04 section 8.1 line 310); Bench; no photo before; nothing else changed | Verified |
| TC-SYS-082 | Bench | acceptance_criteria, expected_artifacts | INSP-025 finding-3; INSP-025 finding-8 | see "Case checks" | Verified |
| TC-SYS-083 | Bench | acceptance_criteria, expected_artifacts | INSP-025 finding-3; INSP-025 finding-8 | see "Case checks" | Verified |
| TC-SYS-089 | Bench | expected_artifacts | INSP-025 finding-8 | photo entry added (04 section 8.1 line 310); Bench; no photo before; nothing else changed | Verified |
| TC-SYS-090 | Bench | expected_artifacts | INSP-025 finding-8 | photo entry added (04 section 8.1 line 310); Bench; no photo before; nothing else changed | Verified |
| TC-SYS-094 | Bench | expected_artifacts | INSP-025 finding-8 | photo entry added (04 section 8.1 line 310); Bench; no photo before; nothing else changed | Verified |
| TC-SYS-095 | Bench | expected_artifacts | INSP-025 finding-8 | photo entry added (04 section 8.1 line 310); Bench; no photo before; nothing else changed | Verified |
| TC-SYS-096 | Bench | expected_artifacts | INSP-025 finding-8 | photo entry added (04 section 8.1 line 310); Bench; no photo before; nothing else changed | Verified |
| TC-SYS-100 | Bench | expected_artifacts | INSP-025 finding-8 | photo entry added (04 section 8.1 line 310); Bench; no photo before; nothing else changed | Verified |
| TC-SYS-101 | Bench | acceptance_criteria, expected_artifacts | INSP-025 finding-3; INSP-025 finding-8 | see "Case checks" | Verified |
| TC-SYS-102 | Bench | acceptance_criteria, expected_artifacts | INSP-003 finding-25; INSP-025 finding-8 | see "Case checks" | Verified |
| TC-SYS-104 | Bench | expected_artifacts | INSP-025 finding-8 | photo entry added (04 section 8.1 line 310); Bench; no photo before; nothing else changed | Verified |
| TC-SYS-105 | Bench | setup, procedure, acceptance_criteria, instruments, expected_artifacts | INSP-025 finding-10 | see "Case checks" | Verified |
| TC-SYS-106 | Bench | expected_artifacts | INSP-025 finding-8 | photo entry added (04 section 8.1 line 310); Bench; no photo before; nothing else changed | Verified |
| TC-SYS-108 | Bench | acceptance_criteria | INSP-025 finding-3 | see "Case checks" | Verified |
| TC-SYS-109 | Bench | acceptance_criteria, expected_artifacts | INSP-025 finding-3; INSP-025 finding-8 | see "Case checks" | Verified |
| TC-SYS-110 | Bench | acceptance_criteria, expected_artifacts | INSP-025 finding-3; INSP-025 finding-8 | see "Case checks" | Verified |
| TC-SYS-111 | Bench | setup, procedure, acceptance_criteria | INSP-025 finding-11; INSP-003 finding-31 | see "Case checks" | finding-2 |
| TC-SYS-112 | Bench | acceptance_criteria, expected_artifacts | INSP-003 finding-31; INSP-025 finding-8 | see "Case checks" | Verified |
| TC-SYS-113 | Bench | acceptance_criteria | INSP-003 finding-31 | see "Case checks" | Verified |
| TC-SYS-116 | Simulation | added | INSP-025 finding-5, X1 | see "Case checks" | Verified |

## Readiness criteria

| Id | Criterion | Answer and evidence |
|---|---|---|
| R1 | `tools/validate_docs.py` exits 0 for the case file; every `requirement_ids` entry exists | Yes on the export of `c629198`: `test_cases.json` PASS; `tools/traceability.py`: 0 violations, 114 TC-SYS cases, 189 of 189 live SYS requirements covered |
| R2 | Test code compiles and runs | N/A: system cases, no test code (as INSP-025) |
| R3 | `automation_ref` of every automated case points to an existing test | N/A for Bench and Inspection; the two Simulation references touched (TC-SYS-073, 116) name planned checkers, the file's convention for Simulation cases before CDR |
| R4 | Test author differs from the implementation author | Yes: no implementation exists. The test author and the L1 requirements author were one invocation (CR-008 section 4; cross item X-4 of INSP-044) |
| R5 | Requirements under test `Active`, or the brief names the CR | Yes: every cited requirement is Active except REQ-SYS-194 (Draft), which CR-008 adds |

## Participants

Test author: WP-PDR-11 author invocation. Reviewer: this invocation (`reviewer:WP-PDR-11-INSP-025-delta`). Software assurance: not required (07 section 2.1.1 row "Test cases ...", column "Neither"; as INSP-025).

## A. Case record content

| Item | Answer | Evidence |
|---|---|---|
| CK-TEST-A1 | Yes | TC-SYS-116 follows TC-SYS-114 and TC-SYS-115, both claimed by CR-003 (TC-SYS-115 withdrawn in its revision 2 and never reused); title states scenario and result |
| CK-TEST-A2 | Yes | TC-SYS-116 cites REQ-SYS-194 (Analysis = Analysis); TC-SYS-061 cites REQ-SYS-083 only (Test = Test); no other `requirement_ids` changed |
| CK-TEST-A3 | Yes | TC-SYS-116 Simulation for an Analysis requirement (credit row A); no other type changed |
| CK-TEST-A4 | Yes | Configurations of TC-SYS-003, 060, 064, 105, 111 state the new connections, points and guard terms; the rendering matches the JSON (script) |
| CK-TEST-A5 | Yes | New steps are numbered single actions (TC-SYS-003 step 2, TC-SYS-073 run step, TC-SYS-105 capture step, TC-SYS-116 steps 1 to 5); the TC-SYS-036 missing step is recorded under A6 as finding-1 |
| CK-TEST-A6 | No | Criteria are quantitative and take their values from the requirements, with the 04 section 8.2 rule applied in the right direction at every point checked. No: finding-1 (TC-SYS-036 clause not observable as configured), finding-2 (TC-SYS-111 does not exclude the charger), finding-3 (TC-SYS-034 bound citation) |
| CK-TEST-A7 | Yes | Every Bench case lists a `photo` entry (INSP-025 A7 was No for finding-8, now closed); new artifacts carry `artifact_type` |
| CK-TEST-A8 | Yes | New instruments are from the 04 section 6.1 inventory (Pico logic capture on TC-SYS-105; tinySA, attenuator and NanoVNA already on TC-SYS-003) |
| CK-TEST-A9 | Yes | All 114 cases Draft |

## H. Bench and OnAir procedures (applied to the changed Bench cases as INSP-025 did)

| Item | Answer | Evidence |
|---|---|---|
| CK-TEST-H1 | Yes | Safety notes unchanged; TC-SYS-003 transmissions go into the calibrated attenuator, which the safety note already allows; TC-SYS-111 keeps the cell-handling note |
| CK-TEST-H2 | Yes | Stop and NCR step kept in every changed case |
| CK-TEST-H3 | Yes | Unchanged firmware and picotool steps |
| CK-TEST-H4 | Yes | TC-SYS-003 keeps "with the straight key and then with the paddle"; TC-SYS-036 and 105 keep both key types |
| CK-TEST-H5 | Yes | Calibration and version record step kept; TC-SYS-003 records the S21 file and the tinySA calibration-output check; TC-SYS-105 adds the capture pulse-train check |

## I. Test plan and procedure consistency

| Item | Answer | Evidence |
|---|---|---|
| CK-TEST-I1 | N/A | `docs/vv/plan.md` does not exist yet (PDR product) |
| CK-TEST-I2 | Yes | Pass and fail are stated as one decision rule in every changed criterion; the data-only sentence of TC-SYS-034 is finding-3 (recorded under A6) |
| CK-TEST-I3 | Yes | Every case whose cited requirement CR-008 changes (TC-SYS-013, 030, 031, 038, 050, 056, 061, 064, 065, 102, 111, 112) is updated and listed in CR-008 section 4 Verification |

ITEMS N/A: sections B to G (no test code, mock clock, coverage, emulation or regression set for L1 system cases, as INSP-025), CK-TEST-I1, readiness R2 and R3.

## Cross items (outside this product; not findings against it)

- X-1: INSP-044 finding-1 (REQ-SYS-089 and 167 "stop charging" level) is the requirement side of the TC-SYS-065 residual.
- X-2 (tool owner, INSP-025 X3): no committed script renders `test_cases.md`; CR-008 used an uncommitted script that reproduces the `baseline/srr` rendering. The section-by-section check of this record found 0 mismatches.
- X-3 (WP-PDR-35, WP-PDR-40): REQ-SW-KEYER-020 and 021 guarantee more than 1 ms and 4 ms of contact, while REQ-SYS-048 and 162 require 2 ms and 5 ms, which TC-SYS-034 now checks inward (CR-008 section 4).

## Record verdict

Reviewer verdict **APPROVED**, readiness met, three Minor findings (liens under rule C1 if CR-008 is not revised before its disposition). Every INSP-025 lien carried by WP-PDR-11 is Verified on the frozen blob, finding-10 and finding-11 with the residuals finding-1 and finding-2. No Major finding. The record `verdict` stays NEEDS CHANGES only because `tools/validate_docs.py` fails an APPROVED record whose `product_files` are not in `main` HEAD; the software lead sets `verdict: APPROVED` when CR-008 merges with these blobs unchanged (or a delta iteration verifies new blobs). Software assurance pair: not required.

## Verdict format

```
VERDICT: APPROVED (record verdict held at NEEDS CHANGES until CR-008 merges; drift rule)
FINDINGS:
- [Minor] finding-1 CK-TEST-A6 TC-SYS-036: criterion needs TX_KEY on the capture; no step or setup connects it.
- [Minor] finding-2 CK-TEST-A6 TC-SYS-111: charge current alone cannot exclude per-cell charger regulation or cell OVP; add a switching-element threshold or disable the charger's per-cell action.
- [Minor] finding-3 CK-TEST-A6 TC-SYS-034: REQ-SYS-043 bounds paddle closures only; name REQ-SYS-160 and state openings have no L1 bound.
ITEMS N/A: sections B to G, CK-TEST-I1, R2, R3
MEASUREMENTS: size=114 cases (65 added or changed); items_checked=A1-A9, H1-H5, I1-I3, R1-R5; items_no=1; major=0; minor=3; fixed=0; deferred=0; iteration=1; turns=40; minutes=80
```

## Re-pin delta on the CR file (2026-09-29, main `0680af9`; WP-PDR-55)

**Scope (plan rule C1, record drift rule).** The record named the CR file at `3b9266ff` (`4dab5dc`). `main` changed it six times after that: `cccbfda` (section 6.1), `a244b05` (revision 2), `6485bd3` (section 6.3), `a17af87` (disposition), `9c40ef9` (section 9 check, step 7 Done cell) and `726cd44` (section 8, step 3 and 5 Done cells). The result is `aa65e826`, the blob at `main` `0680af9`. This record used the CR's section 1.6, its section 4 Verification row and independence note, and the section 5 checks named in the acceptance criteria. Sections 4 and 5 changed, so this is a delta, and the CR file is re-pinned at `aa65e826`. The four frozen blobs have not changed: `git rev-parse e26ce46:<path>` (the branch head) equals `c629198:<path>` for `requirements.json` `a7344937`, `requirements.md` `4e110b16`, `test_cases.json` `117c08de` and `test_cases.md` `00e4454f`. The branch commits after `c629198` (`ebeb069`, `a36a828`, `e26ce46`) touch none of them.

**Independence (rule C4).** This invocation authored no part of CR-008, of its sections 6 to 9, of steps 3 and 5, of this record's iteration 1, or of the INSP-025 delta at `ebeb069`. It wrote the INSP-003 and INSP-008 updates at `e26ce46` and the INSP-044 re-pin delta (`f31d830`, `39257a8`), all of them records, not this product. It edited no product file. **Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran first (query: CR-008 SRR liens, REQ-SYS-194, INSP-003 and INSP-008 delta). After it, `git diff -U0 3b9266ff aa65e826` and `sed -n` only pinned lines.

### Hunks read (`git diff -U0 3b9266ff aa65e826`: 19 hunks, 157 insertions, 22 deletions; case lens)

| Hunk (new lines) | Section | Change | Effect on this record |
|---|---|---|---|
| 4; 11 to 14; 17 and 18 | Front matter | `status` Dispositioned; `affected_cis` adds row 10; `affected_paths` adds the three ICDs and `render_icd_figures.py`; `affected_ids` adds the three ICD ids; `related` adds WP-PDR-36 and 40; `disposition` Approved 2026-09-28 | No TC id added or removed. `affected_ids` still names 29 of the 65 changed cases, which is R1-F2 of CR section 6.1. That is a CR-document item the owner accepted as a lien. This record's CK-TEST-I3 answer rests on the section 4 Verification row, not on `affected_ids` |
| 141 | 4 | Interfaces row rewritten (revision 2): ICD-CTL-PHONES asymmetric plug detect (question 2a), ICD-PWR-CELL and ICD-CTL-KEY wording, step 9 routing | TC-SYS-056 (REQ-SYS-077) passes if the amplifier enable is low "allowing at most 20 ms after each removal edge" (`117c08de`). That criterion stands under 2a, which the owner chose (section 12 answers). ICD-CTL-PHONES line 228 (TC-SYS-056 row) stays true (section 6.3). Under 2a no case changes. The section 4 Verification row, the independence note and section 1.6 are unchanged, so the CK-TEST-I3 and A1 to A9 evidence stands |
| 162, 164; 166 and 167 | 5 | Done cells of steps 3, 5 and 7; new step 9 (ICD alignment, off the branch) | Only status cells and a downstream ICD step. No case step, and none of the section 5 checks this record ran (57 photos, TC-SYS-060 points, TC-SYS-064 points, TC-SYS-111 constant current, "no other line changed"), is altered |
| 184 to 255 | 6.1 to 6.3 (new) | Impact reviews rounds 1 and 2 and the author response | The round 1 case counts equal this record's: 64 modified, of which 36 change only artifacts and 57 gain a photo, and TC-SYS-116 added. Its SWE-071 list (TC-SYS-013, 030, 031, 038, 050, 056, 061, 064, 065, 102, 111, 112) equals the CK-TEST-I3 list. R1-F1 to R1-F5 and R2-F1 to R2-F3 name no case defect. R2-F3 (a), the 10 ms removal TBR with no bench source, concerns the ICD TBR table, and TC-SYS-056 checks the 20 ms end result, not the debounce. Concur, not counted here |
| 258 to 275 | 7 | Disposition Approved, Class I, 2026-09-28, the section 6 Minors accepted as liens | The CR was dispositioned without a revision, so under rule C1 finding-1 to finding-3 of this record become liens due at the CDR readiness declaration, as the iteration 1 counts said they would |
| 279 to 293 | 8 | Implementation record and commit rows (`ebeb069`, `a36a828`) | Checked against the branch. No case file is in either commit |
| 305 to 347 | 9 | Configuration manager pre-merge check and update | CM record. Its note that this record names the CR at `3b9266ff` is what this delta clears |
| 352 | 10 | "Owner merge approval" filled with the 2026-09-28 reading | Recorded as INSP-044 finding-2 (Minor, Open, fix before the merge). Not counted again here |
| 363 to 367 | 11 | History rows (round 1, revision 2, round 2, disposition, 2026-09-29 check) | Status record only |
| 372 to 374; 377 and 378 | 12 | Question 2 split into 2a and 2b (revision 2); answers recorded with the disposition (Q2: 2a) | Under 2b, TC-SYS-056 would have changed on the branch. Under 2a it does not, so no further case delta is needed |

### Findings at the re-pin delta

| Finding | Severity | State | Basis |
|---|---|---|---|
| finding-1 | Minor | Lien (rule C1; due at the CDR readiness declaration) | Was Open. CR-008 was dispositioned without a revision; TC-SYS-036 at `117c08de` is unchanged |
| finding-2 | Minor | Lien (rule C1; due at the CDR readiness declaration) | Was Open; TC-SYS-111 at `117c08de` is unchanged |
| finding-3 | Minor | Lien (rule C1; due at the CDR readiness declaration) | Was Open; TC-SYS-034 at `117c08de` is unchanged |

No new finding. Open Major 0 and open Minor 0.

### Record verdict at the re-pin delta

`reviewer_verdict: APPROVED`, readiness met (R1 to R5 as at iteration 1, on the unchanged blobs). `product_files` names the CR at `aa65e826` and the four branch blobs at `c629198`. `verdict` stays NEEDS CHANGES under the lead SE convention until the merge commit sets it. The merge and its CM record will change the CR file again (`merge_sha`, sections 8 to 10). At that point, re-pin after a delta of those hunks, or take the CR file out of `product_files`, as the INSP-044 re-pin delta notes.

```
VERDICT (re-pin delta, 2026-09-29): APPROVED (record verdict held at NEEDS CHANGES until CR-008 merges; drift rule)
FINDINGS: finding-1, finding-2, finding-3 [Minor] Lien (rule C1, due CDR readiness declaration); no new finding
PRODUCTS: CR-008@aa65e826 (was 3b9266ff); requirements.json@a7344937, requirements.md@4e110b16, test_cases.json@117c08de, test_cases.md@00e4454f (c629198, equal at the branch head e26ce46)
MEASUREMENTS (re-pin delta): hunks=19; files_changed=1; product blobs re-identified=4 of 4 unchanged; turns=12; minutes=25; major=0; minor_new=0
```
