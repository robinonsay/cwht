---
# Peer-review record front matter (charter section 5; docs/process/07-software-engineering-plan.md
# section 10.2). To review a product, copy this whole file to
# docs/reviews/<REVIEW>/checklists/<product-slug>.md: that copy is the single peer-review record
# (there is no peer-reviews/ folder). Fill every field below, answer every applicable checklist item and
# fill the findings table. Both front-matter parsers (PyYAML and the subset parser of
# tools/validate_docs.py) strip a comment on its own line and a comment written after a value
# (" # ..."); this template keeps each comment on its own line for readability, and comment lines
# may stay or be deleted when filing. tools/validate_docs.py checks the record against the field
# list of docs/process/01-lifecycle-and-reviews.md section 13 (its PEER_REVIEW_RECORD_SCHEMA) and
# fails while the id, checklist_file, product_commit or date placeholder is left in place.
# Search first: 'grep' in an evidence column means: run mcp__claude-context__search_code on
# /Users/robinonsay/rust/cwht first (charter section 11 rule 1), then grep -n only to pin the hit.
#
# id: next free INSP-NNN (never reused, charter section 6)
id: INSP-NNN
checklist: peer-review-checklist-test
checklist_revision: B
# checklist_file: this record's own path
checklist_file: docs/reviews/<REVIEW>/checklists/<product-slug>.md
# product: exact path of the case file, test file, scenario or dev-board check
product: docs/test_cases/sw-txseq/test_cases.json
# product_commit: quoted so that an all-digit hash stays a string
product_commit: "<commit>"
# product_size: N cases or N test functions
product_size: 18 tests
sprint: SW-NN-<module>
# author_agent: the test author
author_agent: <invocation id>
# implementation_author_agent: author of the code under test, so independence can be checked
implementation_author_agent: <invocation id>
# reviewer_agent: authored neither the test nor the implementation
reviewer_agent: <invocation id>
# criticality: safety-critical | mission-critical | neither (plan section 14.1)
criticality: safety-critical
# assurance_required: true | false, from the table of plan section 2.1.1
assurance_required: true
# assurance_reviewer_agent: invocation id, or none when assurance_required is false
assurance_reviewer_agent: <invocation id>
# iteration: 1 to 3
iteration: 1
readiness_met: true
# reviewer_verdict: APPROVED | NEEDS CHANGES (the file reviewer)
reviewer_verdict: NEEDS CHANGES
# assurance_verdict: APPROVED | NEEDS CHANGES | not-required
assurance_verdict: NEEDS CHANGES
# verdict: set by the software lead; APPROVED only when reviewer_verdict is APPROVED and
# assurance_verdict is APPROVED or not-required
verdict: NEEDS CHANGES
findings_major: 0
findings_minor: 0
findings_open: 0
findings_fixed: 0
findings_verified: 0
findings_deferred: 0
assurance_findings_major: 0
assurance_findings_minor: 0
# assurance_tasks_applied: SWEHB section 7.1 tasks applied, for example [swe-134 7.1 task 3]
assurance_tasks_applied: []
# decision_tables_checked: number of design decision tables checked against @mcdc tests
decision_tables_checked: 0
# deferred_rids: RID-<REVIEW>-NNN entered for each Deferred finding at record closure
deferred_rids: []
# items_no: checklist ids answered No
items_no: []
effort_turns: 0
effort_minutes: 0
# record_status: Open | Closed (set by the software lead, plan section 10.2)
record_status: Open
date: 2026-MM-DD
date_closed: null
---

# Peer review checklist: test cases, test code and emulation scenarios

**Product types:** software verification cases `docs/test_cases/sw-<sub>/test_cases.json` (`TC-SW-<SUB>-NNN`) before they become `Active`; host test files `firmware/**/tests/*.rs` and in-file test modules; emulation scenarios under `firmware/emu/`; dev-board check binaries `firmware/devcheck/`; software Bench and OnAir procedures (SWE-087 e). **Governing:** `docs/process/04-verification-and-validation.md` sections 4, 5.2, 6, 8 (procedure content and the section 8.3 procedure checklist, which this checklist includes), 9, 12; ADR-011 (Emulation for event ordering only, never timing); `docs/process/07-software-engineering-plan.md` sections 2.1.1 and 9; NPR 7150.2D SWE-065, SWE-066, SWE-068, SWE-071, SWE-186, SWE-189, SWE-190, SWE-191, SWE-192, SWE-193, SWE-219; charter sections 2, 9, 11 rule 4; `docs/test_cases/schema.json`. **Used by:** an independent reviewer agent that authored neither the test nor the implementation; a second, software assurance reviewer where the table of plan section 2.1.1 says Yes. The assurance reviewer applies SWEHB topic `8-01` (off-nominal testing) and the `# 7. Software Assurance` section of `docs/references/md/swehb/swe-062-*.md`, `swe-065-*.md`, `swe-066-*.md`, `swe-134-*.md` (section 7.1 task 3: safety-critical loaded data tested), `swe-189-*.md`, `swe-190-*.md` and `swe-219-*.md`, writes its verdict and findings into this record and lists the tasks applied in `assurance_tasks_applied`.

Answer every item Yes, No or N/A with evidence (case id and field, or `file:line`). **Major**: a case that could pass with a stub implementation, a missing off-nominal or independence-pair test for a safety-critical decision, a non-deterministic test, a case whose method or type contradicts the credit rules (in particular an Emulation case that asserts or credits timing), a missing hazard test, an acceptance criterion weaker than the requirement. **Minor**: naming, artifact description, wording.

## Record

This file, copied to `docs/reviews/<REVIEW>/checklists/<product-slug>.md`, is the single peer-review record for the product (charter section 5; plan section 10.2). Slug: `test-<module>` for a case file, `test-code-<module>` for a test file, `scenario-ops-<nnn>` for an emulation scenario, `devcheck-<periph>` for a dev-board check. `<REVIEW>` is the next gate the product feeds. The front matter above is the first thing in the file, unfenced.

### Findings (filled by the reviewer and the assurance reviewer)

| Finding | Origin | Severity | Item | Location | Description | State | Deferred to |
|---|---|---|---|---|---|---|---|
| F-01 | reviewer or assurance | Major or Minor | CK-TEST-xx | case id and field, or `file:line` | what is wrong and what would fix it | Open, Fixed, Verified or Deferred | `RID-<REVIEW>-NNN` and the owner decision reference, for Deferred only |

## Readiness criteria

| # | Criterion | Evidence |
|---|---|---|
| R1 | `tools/validate_docs.py` exits 0 for the case file; `tools/traceability.py` reports every `requirement_ids` entry exists | tool output |
| R2 | Test code compiles and runs on the host: `cargo nextest run -p <crate> --profile ci` passes, or the author's return names the failing tests and the implementation gap they expose (tests written before code may fail and still be reviewable) | run log |
| R3 | `automation_ref` of every automated case points to an existing test function or scenario, named with the case id in the function name (`tc_sw_keyer_003_...`) | paths |
| R4 | The test author is a different invocation from the implementation author (front matter) | sprint record |
| R5 | The requirements under test are `Active`, or the brief names the CR | status |

## Participants

Test-author agent (absent); reviewer agent; software assurance reviewer where the table of plan section 2.1.1 says Yes (for this checklist: cases, test code and scenarios of the safety-critical and mission-critical components and units of plan section 14.1); owner for deferrals and as witness for Bench and OnAir procedures.

## A. Case record content (schema; 04 section 8; SWE-065 b)

| Id | Check | Evidence |
|---|---|---|
| CK-TEST-A1 | `id` follows `TC-SW-<SUB>-NNN` for the module of the file; `title` states the scenario and expected behavior | fields |
| CK-TEST-A2 | `requirement_ids` lists every requirement the case closes and nothing it does not test; each listed requirement's `verification_method` equals the case's `verification_method` | requirement files |
| CK-TEST-A3 | `type` is valid for the method and for the software credit rule of 04 section 5.2 and ADR-011: HostUnit for platform-independent logic, including its timing on the mock clock (0.1 ms resolution); Emulation only for a requirement that states an event order, and only when every peripheral the scenario relies on is inside `ACC-EMU-001` (plan section 9.4 item 3); Bench with the Pico-based logic capture for target timing, peripherals, interrupts, clocks and power states; the `setup` field states which credit row applies. An Emulation case typed against a requirement that states a duration, latency, rate, frequency or timeout is Major | `type`, `setup` |
| CK-TEST-A4 | `setup` names the configuration: crate and feature set, mock state, mock clock start, scenario image (release tag `release/FW-vX.Y.Z` or `release/FW-vX.Y.Z-rcN`, 05-configuration-and-data-management.md section 4.3), emulator and commit with `ACC-EMU-001`, device models, dev-board or unit serial | `setup` |
| CK-TEST-A5 | `procedure` is a numbered list of single actions, each with the expected observation, written so a different agent can run it without the author | `procedure` |
| CK-TEST-A6 | `acceptance_criteria` is quantitative with units and a tolerance equal to or tighter than the requirement; it names the observable (pin trace, return value, timestamp difference on the mock clock or the logic capture, event order, display text) | `acceptance_criteria` versus requirement |
| CK-TEST-A7 | `expected_artifacts` lists the log, JUnit, trace or event-sequence CSV or plot the run produces, with `artifact_type`; Bench cases list photos of the setup | field |
| CK-TEST-A8 | `instruments` (Bench, OnAir) are drawn from the inventory of 04 section 6.1: NanoVNA; tinySA Ultra with the calibrated 30 to 40 dB attenuator (purchase committed by the owner in SI-034 and recorded in ADR-021; its receipt recorded by ADR before TRR, charter section 9); Pico-based logic capture; 50 ohm dummy load; bench supply; multimeter. A credit-bearing Bench case that uses the tinySA Ultra or the logic capture names its TV record (`docs/cm/tool-validation/TV-NNN-tinysa.md`, `TV-NNN-logic-capture.md`) in `setup`; the 04 section 6.2 limits are respected (for example the close-in keying spectrum on the tinySA is not credit-bearing) | field |
| CK-TEST-A9 | `status` is `Draft` until this review; the record `verdict: APPROVED` is the condition for `Active` | field |

## B. Independence and derivation (charter sections 2 and 11 rule 4; IEEE 1012 intent)

| Id | Check | Evidence |
|---|---|---|
| CK-TEST-B1 | The test author did not author the implementation file under test (front matter ids differ) | record |
| CK-TEST-B2 | Expected values are derived from the requirement and design tables (dot = 1200/WPM ms, guard tables, decision tables), not copied from the implementation's constants; the derivation is shown in a comment or the `procedure` | test code comments |
| CK-TEST-B3 | The test does not reach into private state to force outcomes; it drives inputs through the `api` mocks and asserts outputs and observable state | test code |

## C. Strength of assertions (rustos methodology "stub-replacement check")

| Id | Check | Evidence |
|---|---|---|
| CK-TEST-C1 | Stub-replacement check: if the function under test returned `Ok(())` or a constant without doing anything, would this test fail? If not, the test is Major | each test function |
| CK-TEST-C2 | Every test asserts observable outputs or state changes (pin writes recorded by the mock, timestamps, returned values, event log entries), not only a status code | assertions |
| CK-TEST-C3 | Nominal, boundary and off-nominal cases exist for each requirement: minimum and maximum values (5 and 50 WPM per SI-033; the transmit guard edges 144.001 and 147.999 MHz and the outside values 144.000 and 148.000 MHz, REQ-SYS-009; the debounce make and open times of `REQ-SW-KEYER`, HZ-010), invalid inputs, corrupted data, sensor out of range, stuck values | case list |
| CK-TEST-C4 | Each SWE-134 provision under test has a negative test: the hazardous action does not occur when one condition is missing (key closure alone never raises `PA_EN`; T/R not settled blocks `PA_EN`; the guest lock blocks `PA_EN`; corrupted flag forces safe state; charge enable stays de-asserted while T/R is in TX; audio output never exceeds the clamp when gain or sidetone amplitude is driven to maximum; a corrupted image trailer or configuration record never enables a safety-critical output; a missed monitor dispatch never lets the watchdog be kicked) | `TC-SW-SAFE-*`, `TC-SW-TXSEQ-*`, `TC-SW-PWR-*`, `TC-SW-AUDIO-*`, `TC-SW-BOOT-*`, `TC-SW-SCHED-*` |
| CK-TEST-C5 | Sequence tests cover every permutation the design forbids (SWE-134 e) and every prerequisite false alone (SWE-134 h) | sequence cases |
| CK-TEST-C6 | State machine tests cover every cell of the design transition table (state, event), including rejected pairs and their logging | test count versus table size |
| CK-TEST-C7 | Timing assertions use the mock clock with explicit tolerances that come from the requirement (HostUnit), or the Bench logic-capture measurement with the capture's sample period counted in the tolerance (element timing error, key-up to `PA_EN` low 2 ms, over-temperature response 100 ms); no timing assertion uses emulator cycle counts or emulated durations (ADR-011; 04 section 5.2) | assertions |
| CK-TEST-C8 | One scenario or behavior per test function; no test that exercises several acceptance criteria and fails ambiguously | test structure |

## D. Determinism and repeatability (SWE-186; plan section 9.2)

| Id | Check | Evidence |
|---|---|---|
| CK-TEST-D1 | No wall-clock reads, no `std::thread::sleep`, no real file, network or serial I/O in host tests; time advances only through the mock clock | grep |
| CK-TEST-D2 | Pseudo-random inputs use a constant seed printed on failure | grep |
| CK-TEST-D3 | Tests do not depend on execution order or shared static state; each test builds its own fixture; the mock is reset in the fixture | fixtures |
| CK-TEST-D4 | The test passes twice in a row with identical (classname, name, outcome) sets in the author's run log (gate G3 form, plan section 8.4) | run log |
| CK-TEST-D5 | No `#[ignore]` without a `// CS-21 waiver` style comment naming the owner decision; no `should_panic` in flight-logic tests | grep |

## E. Coverage attribution and MC/DC (SWE-189, SWE-190, SWE-219; plan sections 9.5, 9.6)

| Id | Check | Evidence |
|---|---|---|
| CK-TEST-E1 | Every test function carries `// @verify REQ-SW-<SUB>-NNN` with ids that exist and match the case's `requirement_ids` (CS-24) | tags |
| CK-TEST-E2 | For safety-critical components and units: every decision in the design decision table has its MC/DC independence-pair tests tagged `// @mcdc <module>/D<nn> c<k>`, one pair per condition, with all other conditions held constant; the author's nightly branch and condition report (MSR-14, plan section 9.6) shows both outcomes for every condition of the decision, or the gap is listed with its disposition in the author's return | tags versus decision table; MSR-14 output |
| CK-TEST-E3 | The module's uncovered host-compilable lines after this test file (from `cargo llvm-cov` on the author's run) are listed with their SWE-189 disposition (requirement missing, test missing, dead, deactivated), and each target-only line with `target-only: verified by <TC-ID>` (plan section 9.5 item 2), in the author's return | coverage output |
| CK-TEST-E4 | Coverage claims come from executed test runs, never from an instrumented development build or estimation (SWE-190) | run log |

## F. Emulation scenarios (plan section 9.4; ADR-011)

| Id | Check | Evidence |
|---|---|---|
| CK-TEST-F1 | The scenario loads the release image (tag named), boots through the bootrom and starts from reset, not from an injected state | scenario |
| CK-TEST-F2 | Stimuli (key, paddle, encoder, ADC values, device model responses) are ordered and derived from an `OPS-NNN` scenario or a requirement; TIMER0 microseconds appear only as sequence keys; the mapping is in the scenario header | header |
| CK-TEST-F3 | Assertions are on the order of captured register-visible events and pin transitions only; no assertion on a duration, frequency or timeout (a scenario that asserts one is a `Procedure-correction` NCR, 04 section 5.2); the event-sequence CSV is an `expected_artifact` | assertions |
| CK-TEST-F4 | Every peripheral the scenario relies on is inside the `ACC-EMU-001` scope (boot, Cortex-M33 execution, TIMER0 alarms and NVIC entry, SIO GPIO, UART0, I2C0 and SPI0 byte streams, ADC plumbing, PWM slices 0 to 7; ADR-011 section 2) and `setup` names `ACC-EMU-001` and the emulator commit; otherwise the case is supporting evidence and `setup` names the HostUnit or Bench case that closes the requirement | `setup` |
| CK-TEST-F5 | Fault injection scenarios exist where the design requires them: corrupted image trailer, corrupted configuration copies, memory poke of a complement-stored flag, forced panic, watchdog expiry, stuck key to time-out, each asserting the order of the safe-state pin writes | scenario list |

## G. Regression and hazard coverage (SWE-191, SWE-192)

| Id | Check | Evidence |
|---|---|---|
| CK-TEST-G1 | The test is included in the default `cargo nextest run --profile ci` or the `tools/emu_run.sh --all` set (no opt-in feature flag hides it) | manifest, scenario registry |
| CK-TEST-G2 | Every requirement with `hazard_ids` in this module has at least one case with method Test in this file set (SWE-192) | traceability report |
| CK-TEST-G3 | Cybersecurity mitigation cases (plan section 16.4) are present for `SW-BOOT`, `SW-CFG`, `SW-KEYER`, `SW-DIAG` and run in the regression set | case list |
| CK-TEST-G4 | Loaded data acceptance cases (SWE-193) for firmware image load and configuration values (nominal, out-of-range, corrupted) exist | `TC-SW-CFG-*`, `TC-SW-BOOT-*` |

## H. Bench and OnAir procedures (software cases run on the unit; 04 sections 8.3, 11, 13)

| Id | Check | Evidence |
|---|---|---|
| CK-TEST-H1 | Safety notes present: transmit steps into the dummy load only; bench supply current limit per stage; PA thermal limit; stuck-key abort; headphone level | `setup`, `procedure` |
| CK-TEST-H2 | Stop rule stated: on any discrepancy the step stops and an NCR is opened before continuing (04 section 10.1) | `procedure` |
| CK-TEST-H3 | Witness (owner) and conductor roles named; the firmware version and `picotool verify` step precede the first powered step | `procedure` |
| CK-TEST-H4 | Both key types are exercised where keying is involved (SI-018): straight key and iambic paddles, at least two speeds | `procedure` |
| CK-TEST-H5 | Report expectations match `docs/templates/verification-report.md` front matter (artifacts with hashes, instruments with calibration and the session reference check of the logic capture or the tinySA) | `expected_artifacts` |

## I. Test plan and procedure consistency (SWE-071, SWE-068)

| Id | Check | Evidence |
|---|---|---|
| CK-TEST-I1 | The case is consistent with the software section of `docs/vv/plan.md` (class, phase, campaign) | plan |
| CK-TEST-I2 | Evaluation criteria for the report are unambiguous: pass, fail and blocked conditions are stated so the evaluator does not judge | `acceptance_criteria` |
| CK-TEST-I3 | If the requirement changed by CR since the case was written, the case reflects the new value (the CR lists this case) | CR log |

## Completion criteria (SWE-088)

`verdict: APPROVED` when readiness R1 to R5 held, every applicable item answered with evidence, zero open Major findings, Minor findings fixed or deferred with an owner decision reference and a gate, the assurance reviewer returned `APPROVED` where plan section 2.1.1 says Yes, the front matter measurements are filled (cases or test functions reviewed, turns, minutes, findings by severity, decision tables checked), and `.venv/bin/python tools/validate_docs.py` passes on the record itself. On `APPROVED` the software lead sets the case `status` to `Active`. On record closure every Deferred finding becomes `RID-<REVIEW>-NNN` in the log of its named gate and is listed in `deferred_rids` (plan section 10.2).

## Verdict format

```
VERDICT: APPROVED | NEEDS CHANGES
FINDINGS:
- [Major] CK-TEST-C1 firmware/cwht-core/tests/txseq_test.rs:57 tc_sw_txseq_004: asserts only Ok(()); assert PA_EN mock write sequence.
- [Major] CK-TEST-E2 TC-SW-SAFE-008: decision D07 lacks independence pair for condition c3 (temperature).
- [Minor] CK-TEST-A7 TC-SW-KEYER-011: expected_artifacts missing the timing CSV.
ITEMS N/A: CK-TEST-F1 to F5 (HostUnit file), CK-TEST-H1 to H5
MEASUREMENTS: size=18 tests; turns=2; minutes=20; major=2; minor=1
```
