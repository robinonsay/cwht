# TV-022: cargo-nextest 0.9.146 and the HostUnit harness

| Field | Value |
|---|---|
| Record | TV-022 |
| Status | **Validated** (2026-09-27, runs 1 and 2 at commit `d3de579`). Independent review, software assurance review and owner accreditation pending (sections 8 and 9) |
| Class | B, evidence-generating: the HostUnit runner of gate G3 (the primary credited software evidence, charter section 9) and the host test harness of 03 section 4.3.1 |
| Governs | SWE-136, SWE-070 through CM plan section 9; SWE-186 (repeatability) and SWE-191 (regression) through 07 sections 9.2 and 9.3; 03 section 4.3.1 host test harness row and section 6.5 item X10 (seeded failing independence-pair test and seeded mock fault) |
| Due | PDR (CM plan section 13 PDR row: "`cargo-nextest`"; 03 section 4.3.1: "a `TV-NNN` record before the first credited run") |
| Lock rows | `tools/toolchain.lock.md` section 1 row cargo-nextest; section 1.1 row cargo-nextest |
| Work package | WP-PDR-08 |
| Author | Claude, software lead and tool owner |

**Scope.** 03 section 4.3.1 defines the host test harness as `cwht-hal-mock`, the test functions of `cwht-core` and the `cargo nextest` runs. This record validates the runner and the harness's fault path: a failing test, a failing independence pair and an injected mock fault must each make the run exit non-zero and appear as failed in the JUnit report. The contract tests of `cwht-hal-mock` against the dev-board drivers (ADR-019 section 4.3) and the independent code review of every `cwht-hal-mock` change are the other two provisions of that row and are not part of this record.

## 1. Identification

| Item | Value | Command |
|---|---|---|
| cargo-nextest | `cargo-nextest 0.9.146 (8af696ddc 2026-09-21)` | `cargo nextest --version` |
| Binary | `~/.cargo/bin/cargo-nextest`, SHA-256 `ab1c2c2a7e7590dfc6aef2f12dc13322729af87c2d16c35c5b85003220bbe487`, 25 806 080 bytes, dated 2026-09-25 11:45 | `shasum -a 256` |
| Profile | `firmware/.config/nextest.toml` (blob `00b81042`): profile `ci`, `retries = 0`, `fail-fast = false`, JUnit `junit.xml` | |
| Harness crates | `firmware/cwht-core`, `firmware/cwht-hal-mock` at the commit tested | |
| Compiler | the TV-020 toolchain | |

**Install source:** crates.io. `~/.cargo/.crates2.json` records `cargo-nextest 0.9.146 (registry+https://github.com/rust-lang/crates.io-index)`, profile `release`, target `aarch64-apple-darwin`, built by `rustc 1.98.0 (88d9e12ae 2026-08-18)`; as for TV-021 the binary predates the tracking entry, so the metadata is the provenance record (limitation 5).

**Fixtures and procedure** (commit `d3de579`): `tools/tests/fixtures/rust/kat-host/` (tree `d70d2554`, feature `seeded-fail`); `tools/tests/fixtures/rust/harness-seeded/` (tree `dbc9eae4`; committed in `a3cacee`): decision KAT/D01 `permit = a && b` in `src/lib.rs` with its two MC/DC independence pairs as named tests in `tests/harness.rs` (07 section 9.6 item 2 form), a heartbeat test through a `cwht-hal-mock` `MockOutput`, and a test of the injected-fault path, built against the real `cwht-core` and `cwht-hal-mock` by path; features `seeded-pair` (condition `b` masked) and `seeded-mock-fault` (the healthy mock replaced by `MockOutput::failing_after(1)`); stored answers in `pdr-known-answers.json` (blob `0e7d72ac`) section `harness-seeded`; procedure `evidence/rust-tv-2026-09-27.sh` (blob `4c7cb753`) sections 9 and 10.

## 2. Purposes covered

1. Run the HostUnit tests of the host-compilable workspace crates, each in its own process, with the `ci` profile, and exit non-zero naming every failed test (gate G3; 07 section 9.2).
2. Write the JUnit report whose (classname, name, outcome) triples gate G3 compares between two runs (SWE-186) and which is kept as the regression artifact (SWE-191, 07 section 9.3).
3. Harness fault path (03 section 6.5 item X10): a failing MC/DC independence-pair test and a fault injected through `cwht-hal-mock` each make the run exit non-zero and appear as failed in the JUnit report.
4. Runner of `cargo llvm-cov nextest` for the coverage measures of TV-021 and TV-023.

## 3. Known-answer test

Run with the TV-020 command and conditions (export layouts, offline, rustup shim).

| Id | Check (procedure section) | Pass criterion |
|---|---|---|
| K22-1 | `kat-host --features seeded-fail`: `cargo +1.98.0 nextest run --locked` (section 9) | exit 100; `FAIL ... kat-host tests::seeded_failure`; 4 run, 3 passed, 1 failed |
| K22-2 | `kat-host` clean (section 9) | exit 0; 3 run, 3 passed (the stored count) |
| K22-3 | `harness-seeded` clean: `cargo +1.98.0 nextest run --locked --profile ci` (section 10) | exit 0; 5 run, 5 passed; JUnit 5 testcases, 0 failed |
| K22-4 | `harness-seeded --features seeded-pair` (section 10) | exit 100; exactly `harness-seeded::harness d01_c2_false` failed; JUnit 5 testcases, failed `['d01_c2_false']`; the reference runner `cargo +1.98.0 test` exits 101 with 4 passed and 1 failed (`d01_c2_false`) |
| K22-5 | `harness-seeded --features seeded-mock-fault` (section 10) | exit 100; exactly `harness-seeded::harness heartbeat_through_mock_toggles` failed; JUnit failed `['heartbeat_through_mock_toggles']` |
| K22-6 | `harness-seeded --features seeded-pair,seeded-mock-fault` (section 10) | exit 100; exactly the two tests of K22-4 and K22-5 failed; JUnit failed `['d01_c2_false', 'heartbeat_through_mock_toggles']` |
| K22-7 | Firmware workspace twice with the `ci` profile (TV-020 K20-6, procedure section 6) | 10 passed twice; identical (classname, name, outcome) sets |

## 4. Result

| Run | Date and time (CDT) | Commit tested | Result |
|---|---|---|---|
| Lock sanity check (history) | 2026-09-26 19:44 | `bfea9c7` | K22-1 and K22-2 pass (lock section 1.1; `evidence/rust-tools-2026-09-26.log.txt` section 7) |
| 1 | 2026-09-27 10:53:42 to 10:54:04 | `d3de579` (export) | **pass**: K22-1 exit 100, `FAIL [...] (3/4) kat-host tests::seeded_failure`, 4 run 3 passed 1 failed; K22-2 exit 0, 3 passed; K22-3 exit 0, 5 passed, JUnit 0 failed; K22-4 exit 100, `d01_c2_false`, JUnit `['d01_c2_false']`, `cargo test` exit 101 with 4 passed 1 failed; K22-5 exit 100, JUnit `['heartbeat_through_mock_toggles']`; K22-6 exit 100, JUnit `['d01_c2_false', 'heartbeat_through_mock_toggles']`; K22-7 10 passed twice, identical |
| 2 | 2026-09-27 10:54:05 to 10:54:26 | `d3de579` (export) | **pass**, every outcome equal to run 1 (the execution order within a run differs, as nextest schedules tests in parallel; the result sets do not) |

Evidence: `docs/cm/tool-validation/evidence/rust-tv-2026-09-27.log.txt` sections 6, 9 and 10 of runs 1 and 2.

## 5. Reproducibility

Not required for class B. The result sets of runs 1 and 2 are identical for every case; the JUnit files differ in time stamps, durations and run identifiers only, which is why gate G3 compares triples (07 section 8.1, test runner row).

## 6. Limitations

1. The independence pair of K22-4 belongs to a fixture decision, not to a safety-critical decision of the image: at FW-B0 no `cwht-core` decision has more than one condition. The check shows that the harness reports a failed pair; the pairs of the real decisions are written with the detailed design and reviewed with the coverage report (07 section 9.6; CDR).
2. The seeded tests must be re-run at every release (03 section 4.3.1; item X10). No release procedure exists yet (`tools/release.sh`, before the first candidate); until it runs them, the re-run is the procedure of this record, section 10, on the release commit (cross item for the release procedure and TC-SW-REG-001).
3. cargo-nextest 0.9.146 writes the `ci` JUnit file under the workspace `target/nextest/ci/` even when `--target-dir` names another directory (observed 2026-09-27; fixed in the procedure at `d3de579`). Scripts read the JUnit file from the workspace `target/`.
4. The harness fixture builds `cwht-core` and `cwht-hal-mock` by relative path and, through them, rustos `api` at `../../rustos`; it is built only in an export layout with rustos exported from the pin beside it, never against the owner's rustos working tree.
5. Provenance of the binary rests on cargo's install metadata (as TV-021 limitation 4).
6. Output is developer evidence until section 9 records the accreditation.

## 7. Re-validation triggers

- A version change of `cargo-nextest` or of the TV-020 toolchain; a change of `firmware/.config/nextest.toml`.
- A change of `kat-host`, `harness-seeded`, `pdr-known-answers.json` section `harness-seeded`, or of the `cwht-hal-mock` fault-injection interface (`MockOutput::failing_after`, `MockGpioError::Injected`).
- A macOS major version change; a defect found in the tool (an NCR per SWE-201).

## 8. Independent review (CM plan section 9.2 step 3)

Pending, in the combined record `docs/reviews/PDR/checklists/tool-validation-rust-toolchain.md` (TV-020 section 8), with the software assurance second review. The reviewer checks that each seeded fault fails for the stated reason (the pair loses condition `b`; the mock refuses the second write) and not for a build or configuration error.

## 9. Accreditation (owner)

Proposed scope statement **ACC-NEXTEST-001**: "Accredited for purposes 1 to 4 for `cargo-nextest 0.9.146` (binary SHA-256 `ab1c2c2a...e487`) with the `ci` profile of `firmware/.config/nextest.toml` and the `cwht-hal-mock` fault path, on the TV-020 toolchain."

| Decision | Date | Recorded by |
|---|---|---|
| Pending (owner, after section 8; due PDR, OD-24 (b)) | | |
