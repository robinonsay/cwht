# TV-021: cargo-llvm-cov 0.9.1 with the llvm-tools of Rust 1.98.0

| Field | Value |
|---|---|
| Record | TV-021 |
| Status | **Validated** (2026-09-27, runs 1 and 2 at commit `d3de579`; runs 3 and 4 at commit `c28dd60` with the seeded `lcov` check K21-4, after review INSP-040 iteration 1 finding-2). Independent review (delta iteration), software assurance review and owner accreditation pending (sections 8 and 9) |
| Class | B, evidence-generating (credit-bearing line, region and function coverage, MSR-13; gate G6 of 07 section 8.4) |
| Governs | SWE-136, SWE-070 through CM plan section 9; SWE-189 and SWE-190 through 07 section 9.5; the SWE-135 coverage item (07 section 8.2) |
| Due | PDR (CM plan section 13 PDR row: "`cargo-llvm-cov` with llvm-tools") |
| Lock rows | `tools/toolchain.lock.md` section 1 rows cargo-llvm-cov, llvm-tools, cargo-installed tools; section 1.1 row cargo-llvm-cov (stable) + llvm-tools |
| Work package | WP-PDR-08 |
| Author | Claude, software lead and tool owner |

## 1. Identification

| Item | Value | Command |
|---|---|---|
| cargo-llvm-cov | `cargo-llvm-cov 0.9.1` | `cargo llvm-cov --version` |
| Binary | `~/.cargo/bin/cargo-llvm-cov`, SHA-256 `aa14e9c0d0632b6c940852f1edbf4d54223012c3e9fcdaab40a3ed7c288b7129`, 3 755 264 bytes, dated 2026-09-25 11:44 | `shasum -a 256` |
| llvm-cov (stable pin) | `~/.rustup/toolchains/1.98.0-aarch64-apple-darwin/lib/rustlib/aarch64-apple-darwin/bin/llvm-cov`, SHA-256 `479d56bef693273f9917440ff1f116cc1d4fd5a99e067613d30592e9deab95ad`, `LLVM version 22.1.8-rust-1.98.0-stable` | `llvm-cov --version` |
| llvm-profdata (stable pin) | same directory, SHA-256 `8219cc21b846b087e2f7d2dd6ded6b8aec62f9390209d50eebb4fa3e00370ecf` | `shasum -a 256` |
| Compiler | the TV-020 toolchain (`rustc 1.98.0`, `-C instrument-coverage`) | |

**Install source:** crates.io. `~/.cargo/.crates2.json` records `cargo-llvm-cov 0.9.1 (registry+https://github.com/rust-lang/crates.io-index)`, profile `release`, target `aarch64-apple-darwin`, built by `rustc 1.98.0 (88d9e12ae 2026-08-18)`. The binary predates the tracking entry (the lock recorded it on 2026-09-25 as "prebuilt, not tracked"; `cargo install --list` tracks it from 2026-09-26 19:20), so the tracking metadata is the only provenance record (limitation 4). The llvm-tools come from the rustup component `llvm-tools-aarch64-apple-darwin` of the pinned toolchain, verified by rustup against the 1.98.0 channel manifest (TV-020 section 1).

**Fixtures and procedure** (commit `d3de579`): `tools/tests/fixtures/rust/cov-kat/` (tree `970e59d5`; committed in `a3cacee` from the scratch fixture of `evidence/rust-tools-2026-09-26.sh` section 6); stored answers in `tools/tests/fixtures/rust/pdr-known-answers.json` (blob `0e7d72ac` for runs 1 and 2; blob `00256755` at commit `c28dd60` for runs 3 and 4, which adds the entry `cov-kat.seeded-gap-lcov`) section `cov-kat`; procedure `docs/cm/tool-validation/evidence/rust-tv-2026-09-27.sh` (blob `4c7cb753`) sections 7 and 8 for runs 1 and 2, and `rust-tv-2026-09-27-r3.sh` (blob `42ad521a`, commit `c28dd60`) sections 7 and 8 for runs 3 and 4 (section 7 adds K21-4); the firmware workspace of the commit with rustos exported from the pin `2ec64c0`.

## 2. Purposes covered

1. Line, region and function coverage of the host-compilable crates on the pinned stable toolchain, as credit-bearing evidence (MSR-13; 07 sections 8.1 and 9.5), by `cargo llvm-cov` and `cargo llvm-cov nextest` (the runner is TV-022).
2. Enforcement of the 100 percent thresholds with `--fail-under-lines 100 --fail-under-regions 100` (exit non-zero below the threshold).
3. Export of `lcov` (read by `tools/measurements.py --coverage`, TV-013) and of the text report that names each uncovered line; each export has a seeded fault (K21-2 text, K21-4 `lcov`).

## 3. Known-answer test

Run with the TV-020 command and conditions (export layouts, offline, rustup shim).

| Id | Check (procedure section) | Pass criterion |
|---|---|---|
| K21-1 | `cov-kat`: `cargo +1.98.0 llvm-cov --locked --summary-only --fail-under-lines 100 --fail-under-regions 100` (section 7) | exit 0; TOTAL lines 13 of 13, functions 3 of 3, regions 7 of 7, each 100.00 percent |
| K21-2 | `cov-kat --features seeded-gap` (the else-arm test removed): `--text` with the same thresholds (section 7) | exit 1; exactly one line with count 0, line 6 (`1`) |
| K21-3 | Firmware workspace, the G6 MSR-13 command `cargo +1.98.0 llvm-cov nextest --locked --workspace --exclude cwht-app --profile ci --lcov --output-path <f> --fail-under-lines 100 --fail-under-regions 100`, twice (section 8) | both exit 0 with 10 tests passed; the two `lcov` files identical after the export root is removed from the source paths; totals `cwht-core` lines 17 of 17, functions 4 of 4 and `cwht-hal-mock` lines 53 of 53, functions 10 of 10, equal to the MSR-13 values of TC-SW-TOOL-001 run 3 (TV-013 section 4) |
| K21-4 | `cov-kat --features seeded-gap`: `cargo +1.98.0 llvm-cov --locked --features seeded-gap --lcov --output-path <f>`, then `tools/measurements.py --coverage <f>` (section 7; INSP-040 finding-2) | exit 0; each printed as a PASS or FAIL line against `pdr-known-answers.json` `cov-kat.seeded-gap-lcov`: K21-4a the zero-count `DA` lines are exactly `DA:6,0`; K21-4b `LF:6`; K21-4c `LH:5`; K21-4d `measurements.py --coverage` prints `lines 5/6 = 83.33 %`. Provenance of the answer: hand-derived from `src/lib.rs` (a line record for lines 2, 3, 4, 6 and 8 of `sign` and line 12 of the test `negative`; the test `positive`, line 15, is compiled out; line 6 is the only line not executed), stated in the fixture entry. An export that dropped the zero-count line or wrote `LH` equal to `LF` fails K21-4a or K21-4c and K21-4d (mutation check in the appendix of the runs 3 and 4 evidence) |

## 4. Result

| Run | Date and time (CDT) | Commit tested | Result |
|---|---|---|---|
| Lock sanity check (history) | 2026-09-26 19:44 | `bfea9c7` (scratch fixture) | K21-1 and K21-2 pass (lock section 1.1; `evidence/rust-tools-2026-09-26.log.txt` section 6) |
| 1 | 2026-09-27 10:53:42 to 10:54:04 | `d3de579` (export) | **pass**: K21-1 `TOTAL 13 0 100.00% 3 0 100.00% 7 0 100.00%`, exit 0; K21-2 `6| 0| 1`, exit 1; K21-3 exit 0 twice, "lcov run 1 and run 2 identical", `cwht-core` 17 of 17 lines and 4 of 4 functions, `cwht-hal-mock` 53 of 53 and 10 of 10 |
| 2 | 2026-09-27 10:54:05 to 10:54:26 | `d3de579` (export) | **pass**, every value equal to run 1 |
| 3 | 2026-09-27 11:54:23 to 11:54:36 | `c28dd60` (export, procedure `rust-tv-2026-09-27-r3.sh`) | **pass**: K21-1 and K21-2 as runs 1 and 2; K21-4 exit 0, `DA:2,1 DA:3,1 DA:4,1 DA:6,0 DA:8,1 DA:12,1`, `LF:6`, `LH:5`, `measurements.py --coverage` exit 0 with `lines 5/6 = 83.33 %`, K21-4a to K21-4d PASS; K21-3 exit 0 twice, lcov identical, `cwht-core` 17 of 17 lines, `cwht-hal-mock` 53 of 53 |
| 4 | 2026-09-27 11:54:37 to 11:54:50 | `c28dd60` (export, second scratch root) | **pass**, every value equal to run 3 |
| K21-4 mutation check | 2026-09-27 11:55 | the run 3 `lcov` export, three mutated copies | each mutant fails: zero-count line dropped (`LF:5`) fails K21-4a, K21-4b, K21-4d; `LH:6` fails K21-4c, K21-4d; `DA:6,1` with `LH:6` fails K21-4a, K21-4c, K21-4d |

Evidence: `docs/cm/tool-validation/evidence/rust-tv-2026-09-27.log.txt` sections 0, 7 and 8 of runs 1 and 2; `docs/cm/tool-validation/evidence/rust-tv-2026-09-27-r3.log.txt` sections 0, 7 and 8 of runs 3 and 4 and the appendix (K21-4 mutation check).

## 5. Reproducibility

Not required for class B. K21-3 shows it anyway: two runs give identical `lcov` data.

## 6. Limitations

1. Statement and region coverage only. `cargo llvm-cov` lists an unstable `--mcdc` flag that has no effect without compiler support (07 section 8.1); branch and condition coverage is the non-credit MSR-14 measure of TV-023. MC/DC is shown by the reviewed independence-pair tables of 07 section 9.6.
2. Coverage of target-only code (`cwht-app`, the MMIO and boot code of `pico2`) is not measured (07 section 9.5 item 2); `--exclude cwht-app` is part of every command.
3. The `lcov` source paths are absolute paths of the build layout; comparisons strip the layout root first (as K21-3 does).
4. Provenance of the binary rests on cargo's install metadata (section 1). A rebuild from the crates.io source, `cargo install cargo-llvm-cov --version 0.9.1 --locked` into a scratch root, would allow a hash comparison of the build, but it is a download and is proposed to the owner, not made (section 9 note).
5. Output is developer evidence until section 9 records the accreditation.

## 7. Re-validation triggers

- A version change of `cargo-llvm-cov` or of the toolchain whose `llvm-tools` it drives (TV-020 triggers).
- A change of `cov-kat`, of `pdr-known-answers.json` section `cov-kat`, or of the G6 command in `tools/sw_gate.sh`.
- A macOS major version change; a defect found in the tool (an NCR per SWE-201).

## 8. Independent review (CM plan section 9.2 step 3)

| Iteration | Date | Record and reviewer | Verdict | Majors | Author action |
|---|---|---|---|---|---|
| 1 | 2026-09-27 | INSP-040 (`docs/reviews/PDR/checklists/tool-validation-rust-toolchain.md`, commit `1b93d83`), independent reviewer | NEEDS CHANGES (2 Major, 5 Minor, for TV-020 to TV-023) | finding-2 (purpose 3 `lcov` export without a seeded fault) | fixed: K21-4 with the answer in `pdr-known-answers.json` (`c28dd60`), runs 3 and 4, mutation check; delta iteration requested |

Iteration 1 was held in the combined record `docs/reviews/PDR/checklists/tool-validation-rust-toolchain.md` (TV-020 section 8); the software assurance second review is pending.

## 9. Accreditation (owner)

Proposed scope statement **ACC-LLVMCOV-001**: "Accredited for purposes 1 to 3 for `cargo-llvm-cov 0.9.1` (binary SHA-256 `aa14e9c0...7129`) with the `llvm-tools` of the Rust `1.98.0` toolchain (LLVM 22.1.8), on the host-compilable crates of the firmware workspace."

| Decision | Date | Recorded by |
|---|---|---|
| Pending (owner, after section 8; due PDR, OD-24 (b)). Optional with it: permission for the provenance rebuild of limitation 4 | | |
