---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md
# section 13 is the single field list; docs/process/08-agent-briefing.md section 3.2).
id: INSP-025
checklist: peer-review-checklist-test
checklist_revision: B
checklist_file: docs/reviews/SRR/checklists/test-cases-sys.md
# product: the TC-SYS verification cases (SRR package section 2 H1 (c), 05 Table 4-2 row 17),
# the JSON record and its rendering, reviewed as one product
product: docs/test_cases/sys/test_cases.json
# product_commit: review baseline (committed); product_files lists every reviewed file as
# path@blob from git rev-parse HEAD:<path> (record drift rule, SRR package section 2.3, R13)
# iteration 2: product_commit is the author's fix commit 0f5a529 (finding-1); the blobs are equal at HEAD a712372;
# iteration 1 reviewed HEAD adcfe0946d2f1b5cd8f41a8f91eb4219a7fb99a1 with test_cases.json@4dd2bc3caff32985fe6940fd68e591368202f32a
# and test_cases.md@6a5bcaf2e1b9f99e1736415582a16e20958082f9
product_commit: "0f5a5299ee19bece1e928b09ad3724f5a92ab92c"
product_files:
  - "docs/test_cases/sys/test_cases.json@de113d6a82c772ab60a3e06f4908b95415f33552"
  - "docs/test_cases/sys/test_cases.md@b03105bb28a81fbdbae9fbec51a374699531c697"
product_size: 110 cases (Bench 74, Simulation 25, Inspection 11; Test 68, Analysis 25, Inspection 11, Demonstration 6), all Draft, citing 181 live REQ-SYS
sprint: SRR-prep
# author_agent: the independent test author of the TC-SYS cases (INSP-003 author_agent; test_cases.md header)
author_agent: "test-author:tc-sys (independent test-author invocation, TC-SYS cases)"
# implementation_author_agent: no schematic, layout or firmware under these cases exists at SRR
implementation_author_agent: none (no design or code under test exists)
reviewer_agent: "reviewer:INSP-025"
# criticality: system L1 cases (module SYS), not a software component of 07 section 14.1
criticality: neither
assurance_required: false
assurance_reviewer_agent: none
iteration: 2
readiness_met: true
reviewer_verdict: APPROVED
assurance_verdict: not-required
# verdict: finding-1 (Major) Verified at iteration 2 on 0f5a529; every Minor finding (finding-2 to finding-9)
# is a lien under the convergence rule of 2026-09-26 (charter section 4 item 3): APPROVED (with liens)
verdict: APPROVED
findings_major: 1
findings_minor: 8
findings_open: 0
findings_fixed: 0
findings_verified: 1
# findings_deferred: the eight Minor liens "Lien: fix before PDR", counted as INSP-003 and INSP-004 do
findings_deferred: 8
assurance_findings_major: 0
assurance_findings_minor: 0
assurance_tasks_applied: []
decision_tables_checked: 0
deferred_rids: []
items_no: [CK-TEST-A5, CK-TEST-A6, CK-TEST-A7]
effort_turns: 48
effort_minutes: 90
record_status: Open
date: 2026-09-26
date_closed: null
---

# Peer review record INSP-025: TC-SYS verification cases

**Product.** The Draft closing cases of the L1 system requirements (`docs/reviews/SRR/package.md` section 2 item H1 (c), "`test-sys` for the TC-SYS cases (row 17)"; section 6.5), reviewed on the committed blobs at HEAD `adcfe0946d2f1b5cd8f41a8f91eb4219a7fb99a1`:

| File | Git blob (`git rev-parse HEAD:<path>`) | Last commit touching it | Content |
|---|---|---|---|
| `docs/test_cases/sys/test_cases.json` | `4dd2bc3caff32985fe6940fd68e591368202f32a` | `cb00792` | 110 cases TC-SYS-001 to TC-SYS-110, all Draft |
| `docs/test_cases/sys/test_cases.md` | `6a5bcaf2e1b9f99e1736415582a16e20958082f9` | `cb00792` | Rendering: summary, case index, requirement coverage, 110 case sections |

The working tree equals HEAD for both files (`git status` shows no change under `docs/test_cases/`).

**Iteration 2 (2026-09-26, HEAD `a712372`).** The author reported finding-1 fixed in one commit, `0f5a529` ("TC-SYS-060: bracket the REQ-SYS-082 cold charge threshold at the -2 C and +2 C tolerance edges widened by the fixture tolerance"), which touches only the two products (`git show --stat 0f5a529`: test_cases.json +8 -3, test_cases.md +4 -3) and only case TC-SYS-060. The reviewer read the whole diff and the new blobs `test_cases.json@de113d6a82c772ab60a3e06f4908b95415f33552` and `test_cases.md@b03105bb28a81fbdbae9fbec51a374699531c697` (`git rev-parse HEAD:<path>` at `a712372`, equal to `0f5a529`; working tree clean under `docs/test_cases/sys/`). Search: `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` for the 04 section 8.2 decision rule; two `grep -n` pin reads of known files (04 decision-rule line, the INSP-023 record's iteration-2 field conventions) were made before that query in this invocation and are disclosed here. REQ-SYS-082 text and `verification_note` and the TC-SYS-109 T_trip derivation were read from the committed JSON. The rendering section TC-SYS-060 was compared with the JSON field by field (setup, five steps, criterion, two artifacts): equal.

**Checklist.** `docs/templates/peer-review-checklist-test.md` revision B. The template is written for software cases, test code and scenarios; this record applies every item that has meaning for system Bench, Simulation and Inspection cases and answers the rest N/A with the reason. The governing procedure rules are `docs/process/04-verification-and-validation.md` sections 3, 4, 5.2, 6, 7.3, 8.1, 8.2 and 8.3 (the section 8.3 procedure checklist is part of this checklist).

**Method.** Search first: `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` preceded every manual search (queries: peer-review record lien table and convergence rule; the rendering script for `test_cases.md`). One `ls` of the known directory `docs/reviews/SRR/checklists/` was made in the first command of the review, before the vector search, to open two existing records; it is disclosed here. `grep -n` was used only afterwards to pin lines (validator schema, corpus citations, INSP-003 finding-25). All 110 cases were checked by script against the committed requirement file (method equality, `Credit row:` key against 04 section 5.2 and rule 7.3.3, the `Article:`, `Configuration:`, `Safety:`, `Environment:` and `Credentials:` lines of rule 7.3.7 and section 8.1, the penultimate record step and the final NCR step of section 8.2, procedure length, instruments, key types, artifacts, and the rendering against the JSON field by field); every acceptance criterion was then read against the text of each requirement it cites, and the threshold, power and emission arithmetic was recomputed (for example +/-1 dB about 0.5 W is 0.397 to 0.629 W and about 5 W is 3.972 to 6.295 W; 25 uW is 53.0 dB below 5 W). Regulatory citations were read in the verbatim corpus (eCFR issue 2026-09-23): 47 CFR 97.119(a) (`47cfr-97.119.md` line 17, identification at least every 10 minutes and at the end), 97.3(a)(8) (`47cfr-97.3.md` line 31, 26 dB bandwidth), 1.1307(b) (`47cfr-1.1307.md` line 39), 2.1091 and 2.1093 (file titles). SWE identifiers pinned: SWE-071 (`npr-7150-2d/04-chapter4.md` line 115), SWE-192 (line 143), SWE-087, SWE-088, SWE-089 (`npr-7150-2d/05-chapter5.md` lines 49, 63, 73).

## Tool runs (2026-09-26, HEAD `adcfe09`, repository root, `.venv/bin/python`)

| Command | Exit | Result |
|---|---|---|
| `tools/validate_docs.py` (iteration 2, HEAD `a712372`, after this revision) | 0 | 47 passed, 0 failed; `PASS docs/reviews/SRR/checklists/test-cases-sys.md` (APPROVED with readiness_met true, 0 open findings) |
| `tools/validate_docs.py` | 0 | 38 passed, 0 failed before this record; `docs/test_cases/sys/test_cases.json` PASS against `docs/test_cases/schema.json`. After this record was written: 47 passed, 0 failed (other reviewer records filed in the same session), `PASS docs/reviews/SRR/checklists/test-cases-sys.md` |
| `tools/traceability.py --report-only` | 0 | 237 requirements, 170 test cases, 0 violations, 2 warnings (`SYS_UNALLOCATED` REQ-SYS-125, REQ-SYS-148; not case defects); no tracked file changed |
| `tools/render_risk.py --check --gate SRR --hazards docs/safety/hazards.json` | 0 | 65 risks, 159 candidates, 0 warnings, hazard cross-check passes (the RSK ids the Analysis-closed hazard cases cite exist) |
| `tools/render_rmm.py --check` | 0 | 100 rows; `rmm.md` current |
| `tools/render_compliance.py --check` | 0 | validation passed, render current |
| `python -m unittest discover -s tools/tests` | 0 | 392 tests OK |

## Readiness criteria

| # | Criterion | Answer | Evidence |
|---|---|---|---|
| R1 | `validate_docs.py` exits 0 for the case file; every `requirement_ids` entry exists | Yes | Tool runs above; script: 0 unknown ids, 0 method mismatches; retired REQ-SYS-016 and REQ-SYS-123 are cited by no case |
| R2 | Test code compiles and runs on the host | N/A | No test code: the product is Bench, Simulation and Inspection cases |
| R3 | `automation_ref` points to an existing test function or scenario | N/A | 63 cases name planned scripts (`tools/analyze_logic_capture.py`, `tools/rf_probe_power.py`, `hardware/sim/checks/*`); none exists before the design, and `test_cases.md` summary line 12 makes each a prerequisite of `Active`. The item is re-checked when a case is proposed for `Active` |
| R4 | Test author differs from the implementation author | Yes | No design or code exists; the cases are by the independent test-author invocation (`test_cases.md` line 3; INSP-003 `author_agent`) |
| R5 | Requirements under test are `Active`, or the brief names the CR | N/A | L1 requirements become `Active` only by the SRR decision memo (02 section 8.3); this review is the SRR verification-planning review that package H1 (c) assigns (row 17). The case `status` change to `Active` still waits for this record's APPROVED and, for Bench cases, the TRR memo (08 section 3.1) |

`readiness_met: true`.

## Participants

Test-author agent (absent); reviewer `reviewer:INSP-025` (new invocation; authored neither the cases, the requirements, the allocation nor any record of this package); no software assurance reviewer (module SYS is not in 07 section 14.1 and `tools/validate_docs.py` derives no assurance need for this product); owner for the liens.

## A. Case record content

| Id | Answer | Evidence |
|---|---|---|
| CK-TEST-A1 | Yes | Ids TC-SYS-001 to TC-SYS-110, unique, module `SYS` equals the prefix (rule 7.3.1); each title states the scenario |
| CK-TEST-A2 | Yes | Every cited requirement's `verification_method` equals the case's (script, 0 mismatches). TC-SYS-010 cites REQ-SYS-011 and 012 with `Credit row: SUPPORT.` and says why in `setup` (fixture characterization, 04 section 6.2 output-power row), which 04 section 8.3 item 1 allows |
| CK-TEST-A3 | Yes | Classes allowed for the method (04 section 4 table): Test and Demonstration on Bench, Analysis on Simulation, Inspection on Inspection. `Credit row:` keys: T-HW 67, D 6, A 25, I 11, SUPPORT 1 (TC-SYS-010), each the closing key rule 7.3.3 gives for module SYS; no Emulation or HostUnit case |
| CK-TEST-A4 | Yes | All 74 Bench cases carry `Article:` (CWHT-A-001 with the release tag `release/FW-vX.Y.Z` and its VDD, or the probe fixture for TC-SYS-010), `Configuration:`, `Safety:`, `Environment:` and `Credentials:` (script); design-data cases name the `baseline/cdr` tag |
| CK-TEST-A5 | No | Procedures are numbered single actions ending with the record and NCR steps (script: all 110), none above 25 steps. Exception: finding-2 (TC-SYS-003 and TC-SYS-008 criteria need tinySA observations their procedures never make) |
| CK-TEST-A6 | No | Iteration 2: finding-1 Verified; finding-9 (Minor, lien) records the guard-band direction of the corrected TC-SYS-060 points. Iteration 1: criteria are numeric with units and one decision rule, and most are equal to or tighter than the requirement (for example TC-SYS-069 brackets 3.20 V +/-0.05 V at 3.15 and 3.25 V; TC-SYS-109 derives T_trip from the 98 C bound less sensor and fixture tolerance). Exceptions: finding-1 (Major), finding-3, finding-4, finding-5 |
| CK-TEST-A7 | No | All 110 cases list `expected_artifacts` with `artifact_type`; 56 of 74 Bench cases have no `photo` of the as-run setup that 04 section 8.1 requires (finding-8) |
| CK-TEST-A8 | Yes | Instruments are the 04 section 6.1 inventory or named fixtures under `docs/vv/fixtures/` (planned); the scale case names OQ-VV-002, the multimeter OQ-VV-003; the tinySA generator output is used only as a frequency and relative source, never as a level reference (04 section 6.2 receiver row); the close-in keying spectrum is not measured on the tinySA by any Bench case (it is TC-SYS-013, Analysis). TV records are named through the 04 section 8.1 `Credentials:` line (the lock names each TV record), not by path in `setup` as the item words it; the tinySA and logic-capture TV records do not exist yet (cross item X2) |
| CK-TEST-A9 | Yes | All 110 `status: Draft` |

## B. Independence and derivation

| Id | Answer | Evidence |
|---|---|---|
| CK-TEST-B1 | Yes | No implementation exists; see R4 |
| CK-TEST-B2 | Yes | Expected values come from the requirement text and are recomputed in the criteria (power bands in TC-SYS-011, 045, 046; dit 1200/WPM ms in TC-SYS-028 and 046; 540 s +/-5 s in TC-SYS-048; 1.41 voltage ratio for 3 dB in TC-SYS-022); test-author tolerances are declared (INSP-003 finding-25, lien) |
| CK-TEST-B3 | N/A | No test code |

## C. Strength of assertions

| Id | Answer | Evidence |
|---|---|---|
| CK-TEST-C1 | Yes | Applied to procedures: every criterion is a physical observation on the unit (PA_EN, RF-present indicator, tinySA, probe, multimeter); no criterion passes on a status indication alone |
| CK-TEST-C2 | Yes | Criteria name the observable (capture edges, probe power, tinySA level, display text, current) |
| CK-TEST-C3 | Yes | Guard edges 144.001 and 147.999 MHz keyed, 144.0005, 147.9995, 143.999 and 148.000 MHz inhibited (TC-SYS-008 steps 3 to 5); 5 to 50 WPM with 5, 25 and 50 WPM timed (TC-SYS-028); debounce make and break (TC-SYS-034, HZ-010); cell, pack and temperature thresholds bracketed (TC-SYS-062, 069, 081, 109); off-nominal loads (TC-SYS-012, 100). The cold charge threshold bracket is finding-1 |
| CK-TEST-C4 | Yes | System-level negative tests: either permit alone never gives RF (TC-SYS-083); guest lock (TC-SYS-047); USB inhibit (TC-SYS-066); safe-state order after reset, panic and fault (TC-SYS-082); corrupt image and configuration (TC-SYS-089); audio ceiling (TC-SYS-051, 053); charging paused while on (TC-SYS-050) |
| CK-TEST-C5 | Yes | Forbidden transitions and properties F1 to F9 (TC-SYS-003); key-closed interlock after power-on, reset and mode change (TC-SYS-037) |
| CK-TEST-C6 | Yes | Every allowed transition T01 to T25 (TC-SYS-002) and F1 to F9 (TC-SYS-003) of ConOps section 3.4; the per-cell (state, event) table belongs to the L2 SW cases at PDR |
| CK-TEST-C7 | Yes | Timing on the logic capture with the sample period counted (TC-SYS-028 "widened by one capture sample"; 1 MS/s against 0.25 ms windows in TC-SYS-034); no emulator timing |
| CK-TEST-C8 | N/A | No test functions; multi-requirement cases report per requirement ("reported per requirement") as 04 section 8.2 allows one to a few related requirements per case |

## D, E, F. Determinism, coverage attribution, Emulation

| Id | Answer | Evidence |
|---|---|---|
| CK-TEST-D1 to D5 | N/A | No host test code |
| CK-TEST-E1 to E4 | N/A | No test code; module SYS is not software (coverage belongs to `TC-SW-COV-001`, 04 section 8.2) |
| CK-TEST-F1 to F5 | N/A | No Emulation case |

## G. Regression and hazard coverage

| Id | Answer | Evidence |
|---|---|---|
| CK-TEST-G1 | N/A | No `cargo nextest` or emulator set; Bench regression selection is `traceability.py --regression` (rule 7.3.10) |
| CK-TEST-G2 | Yes | Every hazard-tracing REQ-SYS has a Test closing case or method Analysis with a `verification_note` beginning "Analysis accepted per RSK-" naming an existing risk (rule 7.3.6: `traceability.py` 0 violations; the Analysis cases name RSK-002, 004, 006, 007, 011, 012, 016, 017, 018, all in the register). SWE-192 governs REQ-SW only (04 section 3) |
| CK-TEST-G3 | N/A | Cybersecurity cases belong to the SW modules of 07 section 16.4 |
| CK-TEST-G4 | Yes | System-level loaded-data acceptance: bad images and corrupt or out-of-range configuration (TC-SYS-089), configuration reset defaults (TC-SYS-046); the SW-BOOT and SW-CFG cases follow at PDR |

## H. Bench and OnAir procedures (04 sections 8.3, 11, 13)

| Id | Answer | Evidence |
|---|---|---|
| CK-TEST-H1 | Yes | `Safety:` in all 74 Bench cases: dummy load or attenuator connected before power-on, bystander distance (NGO-019), current limit, battery handling, hot PA; the two antenna blocks (TC-SYS-036 step 4, TC-SYS-105 step 3) run only after the OnAir authorization of `docs/reviews/TRR-Dn/decision-memo.md` (04 section 6.3) and require identification per 47 CFR 97.119 (verified, `47cfr-97.119.md` line 17) |
| CK-TEST-H2 | Yes | Final step "On any discrepancy, stop and open an NCR per ... section 10" in all 74 Bench cases (and the automated-class equivalent in the others) |
| CK-TEST-H3 | Yes | Owner witness stated in the T-HW credit-row text; the owner performs the D cases; firmware version by the `Article:` release tag and the penultimate record step (04 section 8.1). `picotool verify` appears in 15 cases; for system cases the 04 section 8.1 form governs |
| CK-TEST-H4 | Yes | Every keying case uses both the straight key and the paddle (script over 74 Bench cases; SI-018) |
| CK-TEST-H5 | Yes | Penultimate step records calibration state, instrument, capture, tool and firmware versions (all 110); artifacts named per case (photos: finding-8) |

## I. Test plan and procedure consistency

| Id | Answer | Evidence |
|---|---|---|
| CK-TEST-I1 | N/A | `docs/vv/plan.md` does not exist (PDR product, SE-68 per charter section 9) |
| CK-TEST-I2 | Yes | Each criterion is one Pass rule with "otherwise Fail"; Blocked conditions stated where a sweep may be unavailable (TC-SYS-022) |
| CK-TEST-I3 | N/A | No CR has changed a REQ-SYS (only `CR-001`, FW-B0 coding-standard arms); the TBR re-Draft rule is stated in each affected `setup` (SWE-071) |

## Findings

| Finding | Origin | Severity | Item | Location | Description and expected fix | State | Deferred to |
|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | reviewer | Major | CK-TEST-A6, CK-TEST-C3 | TC-SYS-060 `acceptance_criteria`, `setup`, step 1 | REQ-SYS-082 (HZ-002): charge only between 0 C and 45 C, "each threshold within +/-2 C". The criterion passes if charging runs at +1 and +3 C and is stopped at -3 C, which proves only a lower threshold between -3 C and +1 C: a unit that charges at -2.5 C (outside the tolerance, the cold-charging hazard) passes, and a compliant unit whose threshold is +1.5 C fails. The parenthesis "(thresholds within 0 C +/-2 C ...)" is therefore not what the points show, and the points differ from the REQ-SYS-082 `verification_note` ("0 C and 45 C equivalents"). The upper bracket (43 C runs, 47 C stops) and REQ-SYS-099 (58 C, 62 C) are correct. This is the checklist's Major class "an acceptance criterion weaker than the requirement". Fix: bracket the lower threshold at the tolerance edges as for the upper one, stopped at -2 C and running at +2 C, each widened by the NTC fixture's resistor tolerance expressed in degrees (the method TC-SYS-109 uses for T_trip); drop the +1 C run condition; update `setup`, step 1 and the rendering. **Iteration 2: Verified** at `0f5a529` (`test_cases.json@de113d6a`, `test_cases.md@b03105bb`): the -3, -1, +1 and +3 C points are replaced by T_cold_stop (-2 C less the fixture resistor tolerance in degrees), 0 C (data only, the `verification_note` point) and T_cold_run (+2 C plus that tolerance), each computed in the report from the adopted NTC curve; the +1 C run condition is gone, so a compliant unit with a cold threshold anywhere in -2 C to +2 C now passes, and a unit charging at -2.5 C fails unless the fixture tolerance exceeds 0.5 C; step 1, the criterion, `setup` and the rendering agree; a `cell-temp-bracket.txt` report artifact records the derivation; the REQ-SYS-099 and 45 C points are unchanged. The residual escape band equal to the fixture tolerance is finding-9 (Minor) | Verified | none |
| <a id="finding-2"></a>finding-2 | reviewer | Minor | CK-TEST-A5, 04 section 8.3 item 4 | TC-SYS-003 `setup` Configuration and steps; TC-SYS-008 step 5 | TC-SYS-003's criterion requires "no carrier at the set frequency above -57 dBm ... on the tinySA Ultra" for F1 to F4 and lists the tinySA in `instruments` and an RF reading in `forbidden-attempts.csv`, but its Configuration is "as part 1" (TC-SYS-002: dummy load, no tinySA) and no step connects the attenuator and tinySA, sweeps the attenuator S21 or runs the calibration-output check that 04 section 6.1 requires in every tinySA report (TC-SYS-008 steps 2 and 3 show the form). TC-SYS-008 step 5 reads only the display at the out-of-range frequencies while the criterion also needs the tinySA level there. Fix: add the tinySA connection, S21 and calibration steps to TC-SYS-003 and a tinySA reading at each step 5 frequency of TC-SYS-008 | Lien: fix before PDR | PDR readiness declaration |
| <a id="finding-3"></a>finding-3 | reviewer | Minor | CK-TEST-A6, 04 section 8.2 | `acceptance_criteria` of TC-SYS-003, 008, 047, 066, 082, 083, 101, 108, 109, 110 | The RF-off criterion of REQ-SYS-183 reads "no carrier ... above -57 dBm at the antenna port on the tinySA Ultra" without the attenuator correction and the instrument level accuracy, while TC-SYS-014, 100 and 106 state "corrected for the attenuator and increased by the tinySA level accuracy", the decision-rule form 04 section 8.2 requires ("Pass if the reading plus the instrument accuracy is within the limit"). Fix: use the TC-SYS-014 wording in the ten cases | Lien: fix before PDR | PDR readiness declaration |
| <a id="finding-4"></a>finding-4 | reviewer | Minor | CK-TEST-A6 | TC-SYS-064 steps 1 to 4 and `acceptance_criteria` | The test points lie 50 to 100 mV beyond the thresholds they verify: 400 mV for "differ by more than 300 mV" (REQ-SYS-087), 150 mV for "differ by more than 100 mV" (REQ-SYS-088), 2.40 V and 4.40 V for "outside 2.5 V to 4.3 V" (REQ-SYS-087, 166). A unit whose threshold lies in those margins passes; the margin is neither declared as the test author's nor derived from the cell-simulator setting accuracy. The points follow the REQ-SYS-087 `verification_note`, and the missing tolerance is the requirement side of INSP-003 finding-25 (lien). Fix: set each point at the threshold plus the fixture setting accuracy (for example 300 mV plus the accuracy), or state the margin and its basis in the criterion | Lien: fix before PDR | PDR readiness declaration |
| <a id="finding-5"></a>finding-5 | reviewer | Minor | CK-TEST-A6, 04 section 3 | TC-SYS-061 `acceptance_criteria` | REQ-SYS-083 requires the independent over-voltage stop "from 0 C to 45 C"; the closing Test case measures at room temperature only and states that the span "is covered by the supporting threshold analysis". 04 section 3 allows one closing method per requirement; a span only Analysis can cover needs companion requirements. Minor here because the case follows the reviewed `verification_note` of REQ-SYS-083 and discloses the gap, and the fix is a requirement split (cross item X1) after which this case cites the room-temperature companion only | Lien: fix before PDR | PDR readiness declaration |
| <a id="finding-6"></a>finding-6 | reviewer | Minor | CK-TEST-A4 (rendering) | `test_cases.md` sections TC-SYS-019 and TC-SYS-110 `Setup` | The rendering differs from the committed JSON in two places: it cites "TS-002" (the firmware runtime make-buy study, `docs/decisions/trade-studies/TS-002-firmware-runtime-make-buy.md`) where the JSON reads "TS-NNN-synthesizer-reference", the proposed synthesizer and reference study of `docs/design/concept.md` section 11.2. The header says the file is regenerated from the JSON and never edited by hand, but no render script exists (vector search) and the two files disagree; all other fields of the 110 sections match (script). Fix: regenerate the rendering from the JSON (tool owner, cross item X3) | Lien: fix before PDR | PDR readiness declaration |
| <a id="finding-7"></a>finding-7 | reviewer | Minor | CK-TEST-A3, 04 section 8.2 | TC-SYS-073, TC-SYS-086 `automation_ref` (null), `type` Simulation | 04 section 8.2: automated classes, Simulation among them, carry an `automation_ref`. The two Simulation cases have none: TC-SYS-073 is a datasheet computation and TC-SYS-086 a word-for-word comparison of the legend artwork, which is an inspection closed as Analysis because REQ-SYS-124 carries method Analysis (cross item X4). Fix: name the checker script, or record the manual computation form in `setup` and the reason the class is Simulation | Lien: fix before PDR | PDR readiness declaration |
| <a id="finding-8"></a>finding-8 | reviewer | Minor | CK-TEST-A7, 04 section 8.1 | `expected_artifacts` of 56 Bench cases (TC-SYS-003, 004, 007, 008, 014, 015, 016, 022, 025, 027 to 031, 033, 034, 036 to 039, 041, 042, 045, 047, 048, 051, 053, 056, 057, 059 to 062, 064 to 071, 081 to 083, 089, 090, 094 to 096, 100 to 102, 104, 106, 109, 110) | 04 section 8.1 maps "layouts ... of the test setup" to an `expected_artifacts` entry of type `photo` for the as-run setup; these cases list none. Fix: add the setup photograph entry | Lien: fix before PDR | PDR readiness declaration |
| <a id="finding-9"></a>finding-9 | reviewer (iteration 2) | Minor | CK-TEST-A6, 04 section 8.2 | TC-SYS-060 `setup` (T_cold_stop, T_cold_run definition) and `acceptance_criteria` | The corrected points are widened outward: stop at -2 C minus the fixture tolerance, run at +2 C plus it. That guarantees a compliant unit passes, but a unit whose cold threshold lies between -2 C minus the fixture tolerance and -2 C (outside REQ-SYS-082) still passes, so the `setup` claim "one outside it fails whatever the fixture resistor error" is not true, and the direction is opposite to both the 04 section 8.2 decision rule ("Pass if the reading plus the instrument accuracy is within the limit", line 318) and the TC-SYS-109 method it cites (T_trip is 98 C minus the tolerances, inward). The iteration-1 fix text of finding-1 ("widened") is the source of the ambiguity; this is a reviewer-side wording error followed faithfully by the author. Minor, not Major: the escape band is bounded by the fixture resistor tolerance (a fraction of a degree for precision resistors on an NTC), computed and recorded by the case, against the 1 C unbounded slack and the good-unit rejection of finding-1; the 43 C and 47 C points of the upper threshold carry no fixture tolerance at all and have the same question. Fix: guard both thresholds inward per 04 section 8.2 (stop at -2 C plus the fixture tolerance, run at +2 C minus it; likewise 45 C: run at 43 C plus it, stop at 47 C minus it), or keep the outward points and state the accepted escape band and its basis in the criterion, and correct the "whatever the fixture resistor error" sentence | Lien: fix before PDR | PDR readiness declaration |

**Lien table** (convergence rule of 2026-09-26, charter section 4 item 3: a Minor finding is fixed before the next review and does not block the baseline).

| Finding | Severity | Disposition | Owner | Due |
|---|---|---|---|---|
| finding-2 | Minor | Lien: fix before PDR | TC-SYS test author | PDR readiness declaration |
| finding-3 | Minor | Lien: fix before PDR | TC-SYS test author | PDR readiness declaration |
| finding-4 | Minor | Lien: fix before PDR | TC-SYS test author (with the L1 author for the INSP-003 finding-25 tolerances) | PDR readiness declaration |
| finding-5 | Minor | Lien: fix before PDR | L1 requirements author (split, X1), then the TC-SYS test author | PDR readiness declaration |
| finding-6 | Minor | Lien: fix before PDR | TC-SYS test author; tool owner for a render script (X3) | PDR readiness declaration |
| finding-7 | Minor | Lien: fix before PDR | TC-SYS test author | PDR readiness declaration |
| finding-8 | Minor | Lien: fix before PDR | TC-SYS test author | PDR readiness declaration |
| finding-9 | Minor | Lien: fix before PDR | TC-SYS test author | PDR readiness declaration |

## Cross items (outside this product; not findings against it)

- X1 (L1 requirements author, INSP-003): split REQ-SYS-083 into a room-temperature Test companion and a 0 C to 45 C Analysis companion with its "Analysis accepted per RSK-NNN" note (HZ-002), per 04 section 3.
- X2 (checklist owner): CK-TEST-A8 asks for the TV record path in `setup`, 04 section 8.1 prescribes the `Credentials:` line pointing to the lock; readiness R3 and R5 and section H are worded for software cases and have no SRR form for L1 system cases. Align the checklist with 04 section 8.1 and add a system-case row.
- X3 (tool owner): no script renders `docs/test_cases/<module>/test_cases.md` from its JSON, although the TC-SYS, TC-TX and TC-SW-KEYER renderings each claim to be regenerated.
- X4 (L1 requirements author): REQ-SYS-124 (legend marked into the enclosure) carries method Analysis for what is a design-data and as-built inspection (04 section 3 rule: a physical or documentary property is Inspection); the hazard link then needs a Test or the RSK note already present.

## Verdict

**APPROVED (with liens), iteration 2.** finding-1 (Major) is Verified on `0f5a529`: TC-SYS-060 now brackets the REQ-SYS-082 cold threshold at the -2 C and +2 C tolerance edges, the +1 C run condition is removed and the rendering matches the JSON. The diff introduces no new Major defect; it adds finding-9 (Minor, guard-band direction and one inaccurate sentence), carried with finding-2 to finding-8 as eight liens "Lien: fix before PDR" under the convergence rule of 2026-09-26 (charter section 4 item 3). No finding is disputed.

```
VERDICT: APPROVED
PRODUCT: docs/test_cases/sys/test_cases.json@de113d6a82c772ab60a3e06f4908b95415f33552, docs/test_cases/sys/test_cases.md@b03105bb28a81fbdbae9fbec51a374699531c697 (fix commit 0f5a529, HEAD a712372)
FINDINGS:
- [Major] finding-1 CK-TEST-A6 TC-SYS-060: cold charge threshold bracket; Verified at 0f5a529.
- [Minor] finding-2 CK-TEST-A5 TC-SYS-003, 008: tinySA observations required but not in the procedure; Lien: fix before PDR.
- [Minor] finding-3 CK-TEST-A6 ten RF-off criteria omit attenuator correction and tinySA accuracy; Lien: fix before PDR.
- [Minor] finding-4 CK-TEST-A6 TC-SYS-064: test points 50 to 100 mV beyond thresholds; Lien: fix before PDR.
- [Minor] finding-5 CK-TEST-A6 TC-SYS-061: 0 to 45 C span left to supporting analysis; Lien: fix before PDR.
- [Minor] finding-6 test_cases.md TC-SYS-019, 110 cite TS-002, JSON cites TS-NNN-synthesizer-reference; Lien: fix before PDR.
- [Minor] finding-7 TC-SYS-073, 086: Simulation cases without automation_ref; Lien: fix before PDR.
- [Minor] finding-8 56 Bench cases without a setup photo artifact; Lien: fix before PDR.
- [Minor] finding-9 CK-TEST-A6 TC-SYS-060: fixture tolerance applied outward, not per 04 section 8.2; Lien: fix before PDR.
ITEMS N/A: R2, R3, R5, CK-TEST-B3, C8, D1 to D5, E1 to E4, F1 to F5, G1, G3, I1, I3
MEASUREMENTS: size=110 cases; items checked 43; items No 3; major=1; minor=8; open_major=0; verified=1; lien=8; iteration=2; turns=48; minutes=90
```
