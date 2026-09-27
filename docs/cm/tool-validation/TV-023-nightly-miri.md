# TV-023: nightly-2026-08-24 for MSR-14 branch and condition coverage and Miri (non-credit)

| Field | Value |
|---|---|
| Record | TV-023 |
| Status | **Validated** (2026-09-27, runs 1 and 2 at commit `d3de579`). Independent review, software assurance review and owner accreditation pending (sections 8 and 9) |
| Class | B, **non-credit** (CM plan section 9.1: "the date-pinned `nightly-2026-08-24` toolchain (MSR-14, non-credit measure only)"): its output is a required supporting measure and never by itself closes a requirement (charter section 10; CS-03; 07 section 9.6 item 3) |
| Governs | SWE-136, SWE-070 through CM plan section 9; SWE-219 as tailored (the MSR-14 element of the SWE-219 record, 07 section 9.6); the SWE-135 defects item through Miri (MSR-08) |
| Due | PDR (CM plan section 13 PDR row: "`nightly-2026-08-24` for the non-credit MSR-14 measure") |
| Lock rows | `tools/toolchain.lock.md` section 1 rows nightly-2026-08-24 (date-pinned), llvm-tools; section 1.1 row nightly-2026-08-24; section 7 rows Rust nightly-2026-08-24 and Miri sysroot crates |
| Work package | WP-PDR-08 |
| Author | Claude, software lead and tool owner |

## 1. Identification

| Item | Value | Command |
|---|---|---|
| Toolchain | `nightly-2026-08-24-aarch64-apple-darwin`: `rustc 1.100.0-nightly (fb6531d55 2026-08-23)` | `rustc +nightly-2026-08-24 --version` |
| Miri | `miri 0.1.0 (fb6531d550 2026-08-23)` with the `rust-src` component and the Miri sysroot in `~/Library/Caches/org.rust-lang.miri` (built 2026-09-26 20:50) | `cargo +nightly-2026-08-24 miri --version` |
| llvm-tools | `llvm-cov` `LLVM version 23.1.0-rust-1.100.0-nightly`, SHA-256 `49939152d7a4d91fe8d11013f3d4b0ba1f72d657f97bc0a8a8d12deb23b8069f`; `llvm-profdata` SHA-256 `5ccef12a53670008df2e09d86a4321d2078183a1c00714d5f02d38a785bac042` | `llvm-cov --version`; `shasum -a 256` |
| Driver | `cargo-llvm-cov 0.9.1` (TV-021) with `RUSTFLAGS=-Zcoverage-options=condition` and `--branch` | |
| Binaries | `rustc` `7076a5f18caf0b455fc8b5c1e287a29e6a0f65f92b211ac8636a79b249a3c603`; `cargo` `8e7dfea13d2c912c380aee5d2e59bd6abb6f2aca283372b7efb34c31b3395b35`; `miri` `e722a39e149c8e27f6f5ad77a670e0ff43ee9e85ddee072b097b6a50f58054ff`; `cargo-miri` `cce4744232fcece2793ab4c3367b84d63957734a9f0fce60c7f98020a488dd0a` | `shasum -a 256` |

**Install source:** rustup, dated channel `nightly-2026-08-24` (`https://static.rust-lang.org/dist/2026-08-24/channel-rust-nightly.toml`); components `miri` and `llvm-tools` added 2026-09-26 19:19 (SRR decision 109), `rust-src` and the Miri sysroot 2026-09-26 20:49 to 20:50 (SRR close-out item 2); installed manifest SHA-256 `0bfdc1def95ad183d9c83f9ee8b646f4d3643ce43118100d8bd99daa52eb7690`, unchanged on 2026-09-27. The sysroot crates fetched by `cargo miri setup` are listed in lock section 7. The floating `nightly` channel is not permitted for any use (lock section 1).

**Fixtures and procedure** (commit `d3de579`): `tools/tests/fixtures/rust/cond-kat/` (tree `cca3b348`; the scratch fixture of `evidence/rust-tools-2026-09-26.sh` section 3 plus feature `complete`); `tools/tests/fixtures/rust/miri-kat/` (tree `bf632e48`; feature `seeded-oob`); stored answers in `pdr-known-answers.json` (blob `0e7d72ac`) sections `cond-kat` and `miri-kat`; procedure `evidence/rust-tv-2026-09-27.sh` (blob `4c7cb753`) sections 11 to 14.

## 2. Purposes covered

1. MSR-14: branch coverage of host-compilable image code and condition coverage of the conditions of each decision, measured on the same HostUnit run as MSR-13, reported beside the independence-pair tables; non-credit (07 section 9.6 item 3).
2. MSR-08: Miri runs the host tests of the host-compilable crates in its undefined-behaviour detector (CS-03; gate G5); non-credit.
3. Nothing else: no build, test or coverage result on this toolchain is release or credit evidence.

## 3. Known-answer test

Run with the TV-020 command and conditions (export layouts, offline, rustup shim, `MIRI_AUTO_OPS=no` so Miri cannot fetch or rebuild its sysroot).

| Id | Check (procedure section) | Pass criterion |
|---|---|---|
| K23-1 | `cond-kat` (`if a && b`, tests `true_true` and `false_any`): `RUSTFLAGS=-Zcoverage-options=condition cargo +nightly-2026-08-24 llvm-cov --locked --branch --text` (section 11) | exit 0; `Branch (3:8): [True: 1, False: 1]` and `Branch (3:13): [True: 1, False: 0]`: the seeded unexercised False outcome of `b` is reported |
| K23-2 | `cond-kat --features complete` (adds `true_false`) (section 11) | exit 0; `Branch (3:8): [True: 2, False: 1]`, `Branch (3:13): [True: 1, False: 1]`: every condition outcome covered |
| K23-3 | Firmware workspace, the G6 MSR-14 command `RUSTFLAGS=-Zcoverage-options=condition cargo +nightly-2026-08-24 llvm-cov nextest --locked --workspace --exclude cwht-app --profile ci --branch --json`, twice (section 12) | exit 0 twice; totals branches 4 of 4, lines 70 of 70, regions 70 of 70, equal between the runs and to the MSR-14 values of TC-SW-TOOL-001 run 3 (TV-013 section 4) |
| K23-4 | `miri-kat`: `cargo +nightly-2026-08-24 miri test --locked` (section 13) | exit 0; 2 passed |
| K23-5 | `miri-kat --features seeded-oob` (section 13) | exit 1; `tests::seeded_out_of_bounds_read` stops with "Undefined Behavior: memory access failed: attempting to access 4 bytes, but got alloc<N>+0x10 which is at or beyond the end of the allocation of size 16 bytes"; the two clean tests pass |
| K23-6 | Gate G5 scope: `cargo +nightly-2026-08-24 miri test --locked -p api --lib` in the export's `firmware/` (section 14) | exit 0 (see limitation 3 for what it covers) |

## 4. Result

| Run | Date and time (CDT) | Commit tested | Result |
|---|---|---|---|
| Lock sanity check and gate scope check (history) | 2026-09-26 19:44 (coverage; Miri blocked); 2026-09-27 (`evidence/sw-gate-miri-scope-2026-09-27.log.txt`: G5 scope clean PASS, a seeded out-of-bounds read in `api` FAIL) | `bfea9c7`; working tree | K23-1 pass (`evidence/rust-tools-2026-09-26.log.txt` section 3); the Miri known answer on `api` pass |
| 1 | 2026-09-27 10:53:42 to 10:54:04 | `d3de579` (export) | **pass**: K23-1 `Branch (3:13): [True: 1, False: 0]`; K23-2 `Branch (3:13): [True: 1, False: 1]`; K23-3 exit 0 twice, `{'branches': (4, 4), 'lines': (70, 70), 'regions': (70, 70), 'functions': (14, 14)}`, runs equal; K23-4 2 passed, exit 0; K23-5 exit 1 with the stored Undefined Behavior message (`alloc54296+0x10`); K23-6 exit 0, 0 tests |
| 2 | 2026-09-27 10:54:05 to 10:54:26 | `d3de579` (export) | **pass**, every value equal to run 1 |

Evidence: `docs/cm/tool-validation/evidence/rust-tv-2026-09-27.log.txt` sections 0 and 11 to 14 of runs 1 and 2.

## 5. Reproducibility

Not required for class B. K23-3 and K23-5 give the same result in both runs.

## 6. Limitations

1. **Non-credit.** Every output of this toolchain is labelled nightly and supporting (charter section 10; CS-03). A requirement is never closed by MSR-14 or MSR-08 alone.
2. `-Zcoverage-options=condition` and `--branch` are unstable features of this dated nightly. A move to another nightly is a new record, not a re-run.
3. **The G5 Miri step exercises no test today.** At the rustos pin `2ec64c0` the `api` crate has no unit test (`test result: ok. 0 passed`), and `pico2` is outside the step until lien L-016-6 (SRR close-out item B). K23-4 and K23-5 show that Miri detects undefined behaviour when a test reaches it; the G5 step detects it only once host tests of `api` and of the host-compilable `pico2` decision functions exist (07 section 8.1; CS-38). This is a coverage gap of the Miri scope, not a tool defect (cross item of WP-PDR-08 for the 07 writer and WP-PDR-41).
4. Miri cannot execute volatile MMIO or the boot path (07 section 8.1); those stay with dev-board checks, Bench cases and driver-to-datasheet Inspection.
5. Condition coverage on this nightly reports each condition of a short-circuit decision as a branch; it is not MC/DC (07 section 8.1 MC/DC row), which is shown by the reviewed independence-pair tables (07 section 9.6).
6. Output is developer evidence until section 9 records the accreditation, and non-credit after it.

## 7. Re-validation triggers

- Any change of the `nightly-2026-08-24` components or of the Miri sysroot; a change of the TV-021 driver version.
- A change of `cond-kat`, `miri-kat` or of their sections of `pdr-known-answers.json`; a change of the G5 Miri or G6 MSR-14 command in `tools/sw_gate.sh`.
- A macOS major version change; a defect found in the tool (an NCR per SWE-201).

## 8. Independent review (CM plan section 9.2 step 3)

Pending, in the combined record `docs/reviews/PDR/checklists/tool-validation-rust-toolchain.md` (TV-020 section 8), with the software assurance second review.

## 9. Accreditation (owner)

Proposed scope statement **ACC-NIGHTLY-001**: "Accredited, as a non-credit supporting measure only, for purposes 1 and 2 for `nightly-2026-08-24-aarch64-apple-darwin` (`rustc 1.100.0-nightly (fb6531d55 2026-08-23)`, `miri 0.1.0 (fb6531d550 2026-08-23)`, LLVM 23.1.0) with `cargo-llvm-cov 0.9.1`."

| Decision | Date | Recorded by |
|---|---|---|
| Pending (owner, after section 8; due PDR, OD-24 (b)) | | |
