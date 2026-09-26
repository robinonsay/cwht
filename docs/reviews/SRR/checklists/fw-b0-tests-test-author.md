---
id: INSP-028
checklist: peer-review-checklist-test
checklist_revision: B
checklist_file: docs/reviews/SRR/checklists/fw-b0-tests-test-author.md
# product: the FW-B0 host test files (SRR package section 2.1 item R4; closes the INSP-016 finding-4 review option)
product: firmware/cwht-core/tests/heartbeat.rs, firmware/cwht-hal-mock/tests/gpio.rs
# product_commit: review baseline (committed); product_files lists every reviewed file as
# path@blob from git rev-parse HEAD:<path> at adcfe0946d2f1b5cd8f41a8f91eb4219a7fb99a1
# (the two test files are the product; the code under test and the run configuration are read as context)
product_commit: "adcfe0946d2f1b5cd8f41a8f91eb4219a7fb99a1"
product_files:
  - "firmware/cwht-core/tests/heartbeat.rs@718a0246da10eec9c8f3be5d939d326e2133cb4c"
  - "firmware/cwht-hal-mock/tests/gpio.rs@f1b302bcfa7f55105ad73d8b01d98d0fb7901312"
  - "firmware/cwht-core/src/heartbeat.rs@f38b716a57d7e88bdbcb0cc5d20fb270ea75e71f"
  - "firmware/cwht-hal-mock/src/gpio.rs@fc8872bd420ecbd4760d2f2fc05b236ee842c801"
  - "firmware/cwht-core/src/lib.rs@01c49f60f82689aab61570e7200bf9bf4064cbd1"
  - "firmware/cwht-hal-mock/src/lib.rs@f5141c137073e0493a455681aa1d5ae18f53db38"
  - "firmware/.config/nextest.toml@00b81042cf7f73ff6ffa67f013b4c78ef6884a63"
  - "firmware/Cargo.toml@7799f6b63e26e8fca0c2cb68270c3ff9d7841d05"
  - "docs/test_cases/sw-tool/test_cases.json@fee1e7246af59d5e8a43ed1b9cdf483854053fdc"
product_size: 10 test functions (heartbeat.rs 5, 53 lines; gpio.rs 5, 60 lines); no in-file test module, emulation scenario or dev-board check exists in firmware/ at HEAD
sprint: FW-B0
# author_agent: the test author; implementation_author_agent: the author of the code under test (the same invocation, which is INSP-016 finding-4)
author_agent: "author:fw-b0 (Claude, software lead)"
implementation_author_agent: "author:fw-b0 (Claude, software lead)"
reviewer_agent: "reviewer:INSP-028"
criticality: neither
assurance_required: false
assurance_reviewer_agent: none
iteration: 1
readiness_met: true
reviewer_verdict: APPROVED
assurance_verdict: not-required
verdict: APPROVED
findings_major: 0
findings_minor: 4
findings_open: 0
findings_lien: 4
findings_fixed: 0
findings_verified: 0
findings_deferred: 0
assurance_findings_major: 0
assurance_findings_minor: 0
assurance_tasks_applied: []
decision_tables_checked: 0
deferred_rids: []
items_no: [CK-TEST-B1, CK-TEST-B2, CK-TEST-C3, CK-TEST-C8, CK-TEST-E1]
effort_turns: 30
effort_minutes: 45
record_status: Open
date: 2026-09-26
date_closed: null
---

# Peer review record INSP-028: FW-B0 host tests, independent test-author lens

**Checklist:** `docs/templates/peer-review-checklist-test.md` revision B (readiness R1 to R5, items CK-TEST-A1 to I3). **Record format:** 01 section 13 (Peer review record row), 08 section 3.2, and the iteration 3 records of this folder (INSP-011, INSP-017). **Gate:** SRR, package section 2.1 item R4 ("Independent test-author review of `firmware/cwht-core/tests/heartbeat.rs` and `firmware/cwht-hal-mock/tests/gpio.rs`"), which closes the review option of INSP-016 finding-4 (`fw-b0-toolchain-proof.md`: "have an independent test-author invocation review or replace the tests"). **Answer legend:** Yes = Pass, No = Fail, N/A = not applicable, each with evidence.

**Verdict (iteration 1, 2026-09-26, committed blobs at HEAD `adcfe09`): APPROVED (with liens).** No Major finding. The ten tests are deterministic, pass twice with identical result sets, give 100 percent line, region and function coverage of both units under test, and kill 8 of 9 seeded mutants, including every stub replacement. Four Minor findings: one untested recovery path (finding-1), an undocumented expected value (finding-2), missing CS-24 tags with no CS-24 form for tests that verify no requirement (finding-3), and two multi-behaviour tests (finding-4). Under the convergence rule of the lead SE (2026-09-26, charter section 4 item 3), each is dispositioned "Lien: fix before PDR".

## Scope, independence and method

- **Independence.** This invocation (`reviewer:INSP-028`) wrote neither the tests nor the code under test (`author:fw-b0`, INSP-016 front matter) and did not edit either. Review baseline: HEAD `adcfe0946d2f1b5cd8f41a8f91eb4219a7fb99a1`; `git diff --stat HEAD -- firmware` is empty, so the working tree that was run equals the committed blobs of `product_files`.
- **Search first (charter section 11 rule 1).** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: firmware host tests and INSP-016 finding-4; test functions of the firmware crates; the peer-review record schema; CS-24 `@verify` tags). `git ls-files firmware` and `git grep '#\[test\]\|cfg(test)' HEAD -- firmware` then pinned the complete test set: 10 `#[test]` functions in the two product files, no `cfg(test)` module, no `firmware/devcheck/`, and `firmware/emu/` holds only `README.md`.
- **Lens.** Test-author view: read the requirement basis first (none: TC-SW-TOOL-001 is supporting evidence and verifies no `REQ-SW-*`, `heartbeat.rs:1-2`, `cwht-core/src/heartbeat.rs:7-8`), then judged each test against the documented behaviour of the unit (doc comments of `Heartbeat::step`, `spin_wait`, `MockOutput`, `MockInput`), then checked assertion strength by mutation.
- **Toolchain.** `RUSTUP_TOOLCHAIN=stable`, `rustc 1.98.0 (88d9e12ae 2026-08-18)`, equal to the `tools/toolchain.lock.md` rustc row; no download triggered. rustos at `c54d35aa8e7f9ad30f6508bca458a59c1fc009db`, equal to the lock rustos row (line 206). No tool has a TV record yet, so every run below is developer evidence (CM plan section 9.1).

### Runs (2026-09-26, reviewer, host `firmware/`, target directories in the session scratchpad)

| Run | Command | Exit | Result |
|---|---|---|---|
| T1 | `cargo nextest run --workspace --exclude cwht-app --profile ci` | 0 | 10 run, 10 passed, 0 skipped; 4 binaries |
| T2 | same, repeated | 0 | 10 passed; JUnit `(classname, name, outcome)` sets of T1 and T2 compared by script: 10 entries, identical (gate G3 form, 07 section 8.4) |
| C1 | `cargo llvm-cov nextest --workspace --exclude cwht-app --profile ci --show-missing-lines` | 0 | `cwht-core/src/heartbeat.rs` regions 20/20, functions 4/4, lines 17/17; `cwht-hal-mock/src/gpio.rs` regions 50/50, functions 10/10, lines 53/53; total 100.00 percent, no missing line |
| M1 | mutant script on a `git archive HEAD firmware` copy (rustos by symlink), `cargo nextest run --no-fail-fast` per mutant | see table | 9 mutants, 8 killed, 1 survived |

| Mutant | Change to the unit under test | Result |
|---|---|---|
| H1 | `Heartbeat::step` skips `pin.write` (stub replacement: returns `Ok(next)` without acting) | Killed by `first_step_drives_high_then_alternates`, `failed_write_keeps_level_and_retries_same_transition` |
| H2 | stored level updated before the write | Killed by `failed_write_keeps_level_and_retries_same_transition` |
| H3 | `spin_wait` calls `spin` `count - 1` times | Killed by `spin_wait_calls_spin_exactly_count_times` |
| H4 | `Heartbeat::new` starts high | Killed by three tests including `default_equals_new` |
| H5 | after a failed write, `step` writes the old level instead of retrying the transition | **Survived** (finding-1) |
| G1 | `MockOutput` fault counter decrements by 2 | Killed by `output_fails_after_scripted_count` |
| G2 | `MockOutput` sets the level on a faulted write | Killed by `output_fails_after_scripted_count` and the heartbeat failure test |
| G3 | `MockOutput` history wraps instead of saturating | Killed by `output_history_saturates_at_capacity` |
| G4 | `MockInput::read` ignores the fault flag | Killed by `input_reads_set_level_and_injected_fault` |

**Facts checked against sources.** `LED: usize = 25` (`heartbeat.rs:8`) equals rustos `firmware/pico2/src/common/board.rs:113` (`led: 25`) at `c54d35a`; the expected `5_000_000` (`heartbeat.rs:52`) equals the rustos blinky delay loop `for _ in 0..5_000_000` at `templates/pico2/src/main.rs:57` at `c54d35a`; TC-SW-TOOL-001 `automation_ref` is `tools/sw_gate.sh`, and its acceptance criterion "at least 10 tests" for step 3 is met by the 10 functions. SWE citations verified in `docs/references/md/npr-7150-2d/`: SWE-062 (4.4.5), SWE-066 (4.5.3), SWE-186 (4.4.6), SWE-189 (4.5.9), SWE-190 (4.5.10), SWE-087 (5.3.2), SWE-088 (5.3.3), SWE-089 (5.3.4).

### Findings (filled by the reviewer)

| Finding | Origin | Severity | Item | Location | Description | State | Deferred to |
|---|---|---|---|---|---|---|---|
| F-01 <a id="finding-1"></a>finding-1 | reviewer | Minor | CK-TEST-C3 (C1 applied by mutation) | `firmware/cwht-core/tests/heartbeat.rs:24-34` | The test name and the `Heartbeat::step` doc (`src/heartbeat.rs:46-47`, "the next step retries the same transition") claim a retry, but `MockOutput::failing_after` never recovers and records only successful writes, so the value a failed write attempted is unobservable and no step after a failure ever succeeds. Mutant H5 (the step after a failure writes the old level) passes all ten tests. The recovery path is untested. Fix: give the mock a fail-then-recover script (for example fail the n-th write only) or an attempted-writes log, and assert `Ok(false)` and history `[true, false]` on the step after the failure; or rename the test to what it shows ("failed write keeps level") | Lien | PDR (lien) |
| F-02 <a id="finding-2"></a>finding-2 | reviewer | Minor | CK-TEST-B2 | `firmware/cwht-core/tests/heartbeat.rs:50-53` | `half_period_spin_count_equals_rustos_blinky_delay` asserts the literal `5_000_000` with no derivation in the test; the source is named only in the implementation doc comment (`src/heartbeat.rs:14-15`). The value is correct (rustos `templates/pico2/src/main.rs:57` at the lock commit `c54d35a`), but the test is a change detector on the constant and says nowhere what would make it wrong. Fix: a comment in the test citing the rustos file, line and lock commit (`tools/toolchain.lock.md` rustos row), and the reason the two must stay equal (TC-SW-TOOL-001 blink-rate prediction) | Lien | PDR (lien) |
| F-03 <a id="finding-3"></a>finding-3 | reviewer | Minor | CK-TEST-E1 (CS-24) | all ten test functions; `firmware/cwht-hal-mock/tests/gpio.rs:1-2` | CS-24 (07 section 7.5) requires `// @verify REQ-SW-<SUB>-NNN` above each test function; none of the ten carries one, and CS-24 has no form for a test that verifies no requirement (toolchain proof, mock self-test). `heartbeat.rs:1-2` states at file level that no `REQ-SW-*` is verified; `gpio.rs:1-2` does not. Fix: 07 CS-24 defines the tag for support tests (for example `// @verify none: TC-SW-TOOL-001 support`) or an explicit exemption for FW-B0 and mock self-tests, and both files apply it; the `gpio.rs` header states that no requirement is verified (cross item X1) | Lien | PDR (lien) |
| F-04 <a id="finding-4"></a>finding-4 | reviewer | Minor | CK-TEST-C8 | `firmware/cwht-hal-mock/tests/gpio.rs:49-60`; `firmware/cwht-core/tests/heartbeat.rs:24-34` | `input_reads_set_level_and_injected_fault` exercises four behaviours in one function (initial level, `set_level`, fault injection and clearing, `Default`); the heartbeat failure test combines the kept level with the repeated failure. A failure would not say which behaviour broke. Fix: one behaviour per test function | Lien | PDR (lien) |

**Lien table (convergence rule, lead SE direction 2026-09-26).**

| Finding | Severity | Disposition | Owner | Due |
|---|---|---|---|---|
| finding-1 | Minor | Lien: fix before PDR | Test author for FW-B1 (independent of `author:fw-b0`); mock change by the `cwht-hal-mock` author | PDR readiness declaration |
| finding-2 | Minor | Lien: fix before PDR | Test author for FW-B1 | PDR readiness declaration |
| finding-3 | Minor | Lien: fix before PDR | 07 author (Claude, software lead) for the CS-24 form; test author for the tags | PDR readiness declaration |
| finding-4 | Minor | Lien: fix before PDR | Test author for FW-B1 | PDR readiness declaration |

## Readiness criteria

| # | Criterion | Answer | Evidence |
|---|---|---|---|
| R1 | `validate_docs.py` exits 0 for the case file; `traceability.py` resolves every `requirement_ids` entry | Yes | `validate_docs.py` PASS for `docs/test_cases/sw-tool/test_cases.json` and for this record (the run exits 1 only on another record, tool runs below); `traceability.py --report-only` exit 0, 0 violations; TC-SW-TOOL-001 cites REQ-SYS-127, 128, 133, all present |
| R2 | Test code compiles and runs on the host with `--profile ci` | Yes | runs T1 and T2 |
| R3 | `automation_ref` of every automated case points to an existing test function or scenario | Yes | the only case, TC-SW-TOOL-001, names `tools/sw_gate.sh` (exists), which runs these tests in G3; no case names a test function, so the case-id naming rule has no function to apply to |
| R4 | The test author is a different invocation from the implementation author | Yes, by the review route | the authors are the same (`author:fw-b0`; front matter records both honestly; CK-TEST-B1 No). INSP-016 finding-4 names two fixes, "review or replace"; this record is the independent test-author review, which is what package item R4 schedules. Readiness is taken as met on that basis for this supporting-evidence test set only |
| R5 | The requirements under test are `Active`, or the brief names the CR | N/A | no requirement is under test (`heartbeat.rs:1-2`); TC-SW-TOOL-001 is `credit: false`, SUPPORT row |

## Participants

Test author and implementation author `author:fw-b0` (absent). Reviewer `reviewer:INSP-028`. Software assurance reviewer not required: no file belongs to a component of 07 section 14.1 (`criticality: neither`; `validate_docs.py` assurance rule finds no `sw-<sub>` module in the product). Owner for dispositions.

## A. Case record content

| Id | Answer | Evidence |
|---|---|---|
| CK-TEST-A1 to A9 | N/A | the product is test code; the case record TC-SW-TOOL-001 is INSP-016's product and is not re-reviewed here |

## B. Independence and derivation

| Id | Answer | Evidence |
|---|---|---|
| CK-TEST-B1 | No | same invocation authored tests and code (INSP-016 finding-4; report `TC-SW-TOOL-001-r1.md` section 9 item 6). Not raised again here; this record is the review fix that finding names (cross item X2) |
| CK-TEST-B2 | No | expected values are derived from documented behaviour (alternation from `Heartbeat` doc, exact call count from `spin_wait` doc, history order and saturation from `MockOutput` docs), except `heartbeat.rs:52`, whose derivation is not stated in the test (finding-2) |
| CK-TEST-B3 | Yes | every test drives public API only (`step`, `level`, `history`, `write`, `read`, `set_level`, `set_fault`, `failing_after`); no private field is reached; `api::common::{Read, Write}` traits are the input path |

## C. Strength of assertions

| Id | Answer | Evidence |
|---|---|---|
| CK-TEST-C1 | Yes | stub replacement H1 (write skipped, constant return) killed; every function under test has a mutant killed (M1 table) |
| CK-TEST-C2 | Yes | assertions are on recorded pin history and level, returned values and call counts (for example `heartbeat.rs:19-21`, `gpio.rs:15-16, 26-28, 38-39`), never only on `Ok` |
| CK-TEST-C3 | No | boundaries present: `failing_after(0)` (`gpio.rs:43-47`), history capacity (`gpio.rs:20-29`), spin counts 0, 1, 2, 1000 (`heartbeat.rs:43`); off-nominal paths present for write and read faults; the recovery after a failed step is not tested (finding-1) |
| CK-TEST-C4 | N/A | no SWE-134 provision in FW-B0 |
| CK-TEST-C5 | N/A | no sequence design |
| CK-TEST-C6 | N/A | no state machine (the two-state heartbeat has no transition table in any design) |
| CK-TEST-C7 | N/A | no timing assertion; `spin_wait` is checked by call count, not duration |
| CK-TEST-C8 | No | finding-4 |

## D. Determinism and repeatability (SWE-186)

| Id | Answer | Evidence |
|---|---|---|
| CK-TEST-D1 | Yes | `git grep` over the two files: no `std::time`, `Instant`, `SystemTime`, `thread::sleep`, `std::fs`, `std::net` or serial use; both crates under test are `#![no_std]` |
| CK-TEST-D2 | N/A | no pseudo-random input |
| CK-TEST-D3 | Yes | each test builds its own `MockOutput`, `MockInput` and `Heartbeat`; no `static` in either file; nextest runs each test in its own process |
| CK-TEST-D4 | Yes | T1 and T2 identical result sets (10 entries); INSP-016 run 7 (G3) also shows it |
| CK-TEST-D5 | Yes | no `#[ignore]` and no `should_panic` in either file |

## E. Coverage attribution and MC/DC (SWE-189, SWE-190, SWE-219)

| Id | Answer | Evidence |
|---|---|---|
| CK-TEST-E1 | No | no `// @verify` tag on any of the ten functions; CS-24 has no form for support tests (finding-3) |
| CK-TEST-E2 | N/A | `criticality: neither`; no decision table exists |
| CK-TEST-E3 | Yes | run C1: no uncovered host-compilable line or region in either unit, so no SWE-189 disposition is owed; target-only code is in `cwht-app`, outside this product |
| CK-TEST-E4 | Yes | coverage measured from an executed test run (C1, `cargo llvm-cov nextest`), not estimated (SWE-190) |

## F. Emulation scenarios

| Id | Answer | Evidence |
|---|---|---|
| CK-TEST-F1 to F5 | N/A | no scenario exists (`firmware/emu/` holds only `README.md`) |

## G. Regression and hazard coverage (SWE-191, SWE-192)

| Id | Answer | Evidence |
|---|---|---|
| CK-TEST-G1 | Yes | both crates are `default-members` (`firmware/Cargo.toml:10`); the tests run under the default `cargo nextest run --workspace --exclude cwht-app --profile ci` of gate G3 with no feature flag (T1) |
| CK-TEST-G2 | N/A | no requirement with `hazard_ids` in this set |
| CK-TEST-G3 | N/A | no cybersecurity module in FW-B0 |
| CK-TEST-G4 | N/A | no loaded data in FW-B0 |

## H. Bench and OnAir procedures

| Id | Answer | Evidence |
|---|---|---|
| CK-TEST-H1 to H5 | N/A | host tests only |

## I. Test plan and procedure consistency

| Id | Answer | Evidence |
|---|---|---|
| CK-TEST-I1 | Yes | the tests are the HostUnit part of the FW-B0 toolchain proof named in 07 section 3.1 (line 149) and section 3.2 (line 160); `credit: false` |
| CK-TEST-I2 | Yes | pass and fail are the `assert!` outcomes; TC-SW-TOOL-001 acceptance "every host test of step 3 passes (at least 10 tests)" is unambiguous |
| CK-TEST-I3 | N/A | no requirement under test; no CR |

## Cross items (outside this record's scope; not edited)

- **X1** (07 author): CS-24 form or exemption for tests that verify no requirement (finding-3).
- **X2** (INSP-016 reviewer): this record is the independent test-author review that INSP-016 finding-4 names as its first fix. Recommended INSP-016 disposition: finding-4 closed by INSP-028 as to the review; the test quality items it found are carried here as liens finding-1 to finding-4.
- **X3** (risk owner, RSK-063 host-mock fidelity, `docs/risk/register.json` mitigation step S1): the `gpio.rs` tests show the mock does what its own docs say; they do not show that it matches the silicon. That remains the contract-test step S1 due at PDR, not a finding here.

### Tool runs (2026-09-26, HEAD `adcfe09`, after writing this record)

| Command | Exit | Result |
|---|---|---|
| `.venv/bin/python tools/validate_docs.py` | 1 | this record PASS with the drift rule applied (every `product_files` blob equals HEAD); the one failure is `technology-assessment.md` (INSP-014, iteration 4, being edited by another invocation in the working tree), not this record |
| `.venv/bin/python tools/traceability.py --report-only` | 0 | 237 requirements, 170 test cases, 0 violations, 2 warnings (REQ-SYS-125, REQ-SYS-148 `SYS_UNALLOCATED`) |

### Closure block (iteration 1)

- Test functions reviewed: 10. Items answered No: 5 (CK-TEST-B1, B2, C3, C8, E1). Findings: 4 (0 Major, 4 Minor). Closed: 0. Lien: 4 (finding-1 to finding-4). Disputed: 0. Unresolved of the higher severity: none.
- Verdict: APPROVED (with liens), per the convergence rule.
- `record_status` stays Open (set to Closed by the software lead); `date_closed` null.

## Verdict

```
VERDICT: APPROVED (with liens) (iteration 1)
PRODUCT: firmware/cwht-core/tests/heartbeat.rs@718a0246, firmware/cwht-hal-mock/tests/gpio.rs@f1b302bc (HEAD adcfe09)
FINDINGS:
- [Minor] finding-1 CK-TEST-C3 heartbeat.rs:24-34: Lien: fix before PDR; retry after a failed write untested, mutant H5 survives.
- [Minor] finding-2 CK-TEST-B2 heartbeat.rs:50-53: Lien: fix before PDR; derivation of 5_000_000 not stated in the test.
- [Minor] finding-3 CK-TEST-E1 both files: Lien: fix before PDR; no @verify tags, CS-24 lacks a support-test form (X1).
- [Minor] finding-4 CK-TEST-C8 gpio.rs:49-60, heartbeat.rs:24-34: Lien: fix before PDR; several behaviours per test.
ITEMS N/A: CK-TEST-A1 to A9, C4 to C7, D2, E2, F1 to F5, G2 to G4, H1 to H5, I3; R5
MEASUREMENTS: size=10 tests; turns=30; minutes=45; major=0; minor=4; closed=0; lien=4; open_major=0; mutants=9 (8 killed); coverage lines 100 percent; iteration=1
```
