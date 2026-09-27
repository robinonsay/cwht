---
test_case: TC-SW-TOOL-001
run: 5
requirement_ids: [REQ-SYS-127, REQ-SYS-128, REQ-SYS-133]
validates: []
verification_method: Demonstration
type: Bench
credit: false
result: Blocked
date: 2026-09-26
conductor: claude
witness: owner
article: pico2-devboard-1
firmware_version: "n/a"
source_commit: "fb22b7aa04e233b2a1614e7ae33d75bb24be0a88"
firmware_elf_sha256: "104f40fa8db928e344284eac5d221120ec25b2d7138219dd0e4c68d4b8134b48"
requirements_baseline: "none (SRR approved with liens 2026-09-26; baseline/srr not yet tagged)"
procedure_commit: "fb22b7a"
procedure_blob: "fee1e7246af59d5e8a43ed1b9cdf483854053fdc"
toolchain_lock: "tools/toolchain.lock.md blob 8ab0218a195f05685cc60a3d35af23f7f1f6e24f at fb22b7a (rustos row 2ec64c0f15c8cd2dbcaa241abffdd72f8cae467c from CR-004; run from the committed file, no temporary edit)"
harness_versions: "n/a"
instruments:
  - "Host only: owner's Mac (macOS 26.6.2, arm64); no board connected in this run (steps 11 and 12 cite run 4, section 4); tools/toolchain.lock.md rows as re-observed 2026-09-26 21:30 CDT (versions.txt); no calibration applicable"
ncr_ids: []
artifacts:
  - "docs/vv/reports/TC-SW-TOOL-001-r5/versions.txt sha256=0d90f98b68541fda39cc1e5872eefa431fa5e82da3c70122d6f9431b1016068b"
  - "docs/vv/reports/TC-SW-TOOL-001-r5/host-build-test.txt sha256=2aed17f635af84da6a89b771c6e162dd2a413db6fd4551633cbe7b0c8447f6cd"
  - "docs/vv/reports/TC-SW-TOOL-001-r5/unsafe-audit.txt sha256=8a48c337f160fe22a6405c3a7f5ca586c62900aac8e0d0698c2bd01b6ef0c17c"
  - "docs/vv/reports/TC-SW-TOOL-001-r5/sw-gate-full.txt sha256=47cf11eec951030a1c7969f291f2d2e54654fe4b3436b49675dffdda3b9d9489"
  - "docs/vv/reports/TC-SW-TOOL-001-r5/sw-gate-keep-going.txt sha256=3becaa9adc9561b673b86bbb4860644fd85367c4d0664cb0f9001eb5c928f2b1"
  - "docs/vv/reports/TC-SW-TOOL-001-r5/gate-known-answer.sh sha256=06c346d386d8eb1ee3f7f930de4b68a76cde9542acab50d854d9c5f0252cf8a0"
  - "docs/vv/reports/TC-SW-TOOL-001-r5/gate-known-answer.txt sha256=d8c48120adaf4d0f129b94f5d217ec4b9f6273271e7dc17042d22042414bb706"
  - "docs/vv/reports/TC-SW-TOOL-001-r5/run5.sh sha256=4a20324938429fcbc77de7332c0fa6e22295094bf63d944a6f463888cf9f1acc"
  - "docs/vv/reports/TC-SW-TOOL-001-r5/rustup-guard.sh sha256=9b1ea18c5d5983d7311c0011ecba4a5add1841e99dbc630ed9dc3ad698269828"
  - "docs/vv/reports/TC-SW-TOOL-001-r5/blinky-build.txt sha256=1a6eaf37228eee7ef9a644c7022b9656dbb3ece5f0d04bc414778291a9c7d7a1"
  - "docs/vv/reports/TC-SW-TOOL-001-r5/rustos-blinky.elf sha256=e826dbf0ddc3fa91d135673d7a9bdfdd1b9921cd903667bfbccd26c57c81fb61"
  - "docs/vv/reports/TC-SW-TOOL-001-r5/rustos-blinky.uf2 sha256=c45b526837c0831206763eb3134a8e71c854059ff7442c19e51f39edf03308d3"
  - "docs/vv/reports/TC-SW-TOOL-001-r5/cwht-app-build.txt sha256=57b7d7987770c49a22dafd4004ae2daa19252da92a0c5acbb7494cff8febd582"
  - "docs/vv/reports/TC-SW-TOOL-001-r5/cwht-app.elf sha256=104f40fa8db928e344284eac5d221120ec25b2d7138219dd0e4c68d4b8134b48"
  - "docs/vv/reports/TC-SW-TOOL-001-r5/cwht-app.uf2 sha256=4e0bd133a10b6e29f72f00023ec407cd1885b8550a685b881c7be213462b3529"
  - "docs/vv/reports/TC-SW-TOOL-001-r5/cwht-app.map sha256=144a152ab950d7232714212480a7fc7840ae3fe1eda7733e73977c5674c58ab2"
  - "docs/vv/reports/TC-SW-TOOL-001-r5/uf2-info.txt sha256=24afab13d841642b779f07d3145f3c52220827763327604b6cecfcddf94cf1fd"
  - "docs/vv/reports/TC-SW-TOOL-001-r5/blink-rate-prediction.txt sha256=4349aaa0256f40538c6dfe4279c392b00410a336ab63b59368637b317378c7f8"
  - "docs/vv/reports/TC-SW-TOOL-001-r5/elf-diff.txt sha256=4a1c84127aac58dde7318665064e147e33369642cc242e719e1c347d477a6c69"
  - "docs/vv/reports/TC-SW-TOOL-001-r5/layout-after.txt sha256=8a6505129fe60eb16e6d430cbd672583d5c9acac96e644059ce792f2b85a27d0"
mop_values: []
---

# Verification report: TC-SW-TOOL-001 run 5

**Status of this run: Blocked.** Run 5 is the automated gate part of the case (steps 1 to 10 and 13) after the SRR close-out decisions (minutes, "Close-out decisions (after the first close-out run)", owner statement "I concur with your recommendations"). Claude ran it on 2026-09-26 between 21:30 and 21:32 CDT on a clean layout: a `git archive` of cwht `fb22b7a` and a `git archive` of rustos `2ec64c0`, with the run 3 download guard first on `PATH`. The gate exits 1. The stopping run fails at `G5 complexity`; the `--keep-going` run has 24 gate-step PASS lines, 2 FAIL (`G5 complexity`, `G5 Miri (nightly, non-credit, MSR-08)`), 0 MISSING and 1 SKIP (section 7). Neither FAIL is a defect of the cwht workspace or the rustos code: the first waits on an open owner decision (CR-005 section 9), the second is a gate scope problem found now that Miri runs at all. Both UF2 images are byte-identical to runs 1 to 4, so steps 11 and 12 stand on run 4. This is a dev-board case: `credit: false`, credit row `SUPPORT`, and it changes the status of no requirement (docs/process/04-verification-and-validation.md section 4, rule 7.3.12). Runs 1 to 4 are not edited.

## 1. Objectives and degree to which they were met

The case, its objective and its requirements are unchanged (case blob `fee1e724` at `fb22b7a`). The objective is the FW-B0 exit criterion of docs/process/07-software-engineering-plan.md section 3.2 and the SRR toolchain-proof product of 07 section 3.1 (SRR package item H12; baseline record section 0.1, precondition P6).

| Requirement | Acceptance criterion (this case) | Measured or observed, run 5 | Met? |
|---|---|---|---|
| REQ-SYS-127 | Rust workspace builds for `thumbv8m.main-none-eabihf` against rustos by path; image runs on a Pico 2 | Release build on the pinned `1.98.0`, exit 0, no warning; FLASH 1608 B (0.04 %), RAM 8200 B (1.54 %) through `tools/measurements.py --link-map`; dependency set `cwht-app`, `cwht-core`, `api`, `pico2`; loadable sections identical to run 3; on-board run: run 4 on the byte-identical UF2 (section 4, steps 11 and 12) | Partially (supporting only; closes by Inspection, row I) |
| REQ-SYS-128 | `cwht-core` and `cwht-hal-mock` build and test on the host; the same `cwht-core` links into the target image | Host build exit 0; 10 of 10 tests pass, twice, identical result sets (G3); 100 percent lines and regions of both host crates (G6, developer evidence) | Met for this case (supporting only; closes by Inspection, row I) |
| REQ-SYS-133 | `picotool load -v` of both UF2 images succeeds and the images run | Both run 5 UF2 files are byte-identical to the files loaded and verified in run 4 (`cmp` exit 0); `picotool info -a`: RP2350, ARM Secure, one image def block each | Met for this case by run 4 on the same bytes (supporting only; closes by Demonstration on the delivered unit, row D) |

## 2. Description of the activity and deviations

Order of execution: `run5.sh` (steps 1 to 6 and 8 to 10, 21:30:04 to 21:30:22 CDT; gate time stamps 02:30:08Z stopping run and 02:30:12Z `--keep-going`), `gate-known-answer.sh` (step 7, 21:31:11 to 21:31:29), then the ELF comparison of section 3 (`elf-diff.txt`, 21:32). The layout, the known-answer copies and all build directories were deleted after the run.

Inputs changed since run 3 (`git diff --stat 0bcea39 fb22b7a`): `firmware/unsafe-audit.md` (CR-004, regenerated for `2ec64c0`), `tools/complexity_gate.py` (CR-005, blob `9cdc9195`), `tools/sw_gate.sh` (INSP-016 finding-14, blob `52b9f803`) and `tools/toolchain.lock.md` (CR-004 pin and close-out items 2, 3 and 12, blob `8ab0218a`). No file under `firmware/cwht-app`, `firmware/cwht-core`, `firmware/cwht-hal-mock`, and none of `firmware/Cargo.toml`, `Cargo.lock`, `.cargo`, `rust-toolchain.toml` changed. rustos is the same commit `2ec64c0` that run 3 built, now `master` after the owner's merge.

Deviations from the case, and from runs 1 to 4 (none affects credit, because the run carries none):

- D1 and D4 stay closed (pinned `1.98.0` in use; 0 `INTERIM` lines in every gate invocation).
- D8 (second decision in `cwht-app/src/main.rs`) is unchanged: the comment at `main.rs:36-40` still reads "owner disposition before FW-B1" although CR-001 was approved as SRR decision 108 (cross item of run 3, still open; not a gate input).
- D9 repeated: two independent clean rebuilds (step 4). D10 not repeated: the committed `firmware/unsafe-audit.md` now describes the pin (CR-004), so the run checks it as committed and does not regenerate it.
- D11 and D12 of run 3 are replaced by D20. D12 is closed: the lock in the layout is the committed file (`diff` exit 0 in `versions.txt`), because CR-004 put `2ec64c0` in the lock's rustos row.
- D13 repeated: `RUSTUP_AUTO_INSTALL=0`, `CARGO_NET_OFFLINE=true`, `MIRI_AUTO_OPS=no`, the run 3 `rustup` shim first on `PATH` (`rustup-guard.sh`, byte-identical to run 3), and, new in run 5, stdin from `/dev/null` for every command. No output shows a download or a guard refusal (`grep` for "Downloading", "Updating crates", "downloading component" and "rustup-guard" finds nothing).
- D14 does not recur: `rust-src` and the Miri sysroot are installed (close-out item 2), so cargo-miri did not prompt.
- D19 carried: steps 11 and 12 are not repeated (section 4).
- D20 (new). **rustos layout.** The owner's rustos working tree holds uncommitted work of the owner's own and was neither read nor written. `firmware/Cargo.toml` takes rustos from `../../rustos`, and gate G0 reads the rustos commit with `git -C "$RUSTOS" rev-parse HEAD` and requires a clean `git status` of the code directories. A plain `git archive` export has no git metadata, so G0 would stop on it with "rustos HEAD none". The layout therefore has two rustos trees: `<scratch>/r5/rustos-export`, the `git archive 2ec64c0` export the brief names, and `<scratch>/r5/rustos`, a local clone of the owner's repository (`git clone --no-hardlinks --no-checkout`, objects only, then `checkout --detach 2ec64c0`). The clone's tree equals the export: `diff -r` with `.git` excluded exits 0, 364 files each (`versions.txt`), and again after the run with `target` also excluded (`layout-after.txt`). The build, the audit and the gate read the clone, so every result is bound to the commit and equals what the export gives. The clone wrote nothing into the owner's repository.
- D21 (new). **KA-8 result lines.** Run 5 records every result line of KA-8 (`--keep-going`). Besides the seeded G3 failure and its consequences (G3 comparison, G6 coverage, G6 branch coverage, G6 measurements), three FAIL groups come from the known-answer copy itself and not from the gate: `G4 traceability` (the copy holds `tools/` scripts and `firmware/` only, not `tools/traceability.py` or `docs/`); `G5 unsafe audit` (the copy links rustos through a symbolic link, `tools/unsafe_audit.py` resolves it and reports the resolved paths, which differ from the committed list's `rustos/...` paths); and the same `G5 complexity` and `G5 Miri` FAILs as step 6. KA-8's criterion (exit 1 and the G3 comparison line FAIL) is met.

## 3. Configuration under test and differences from the operational configuration

- Article: `pico2-devboard-1`, not connected in this run.
- cwht commit `fb22b7aa04e233b2a1614e7ae33d75bb24be0a88`, committed content only (`git archive`, `.venv` linked). The gate scripts are `tools/sw_gate.sh` `52b9f803`, `tools/measurements.py` `abe25acb`, `tools/unsafe_audit.py` `cc3aaa2a`, `tools/complexity_gate.py` `9cdc9195` and `tools/emu_run.sh` `17f102aa`; `firmware/unsafe-audit.md` `18ef484b` (`versions.txt`).
- rustos commit `2ec64c0f15c8cd2dbcaa241abffdd72f8cae467c` (parent `c54d35a`), equal to the lock row and to `git -C /Users/robinonsay/rust/rustos rev-parse master` (D20).
- Tools: pinned `rustc 1.98.0 (88d9e12ae 2026-08-18)` with clippy, rustfmt and llvm-tools; `nightly-2026-08-24` with `miri`, `llvm-tools` and now `rust-src` (close-out item 2), Miri sysroot in `~/Library/Caches/org.rust-lang.miri`, `miri 0.1.0 (fb6531d550 2026-08-23)`; rustup 1.29.1 with `auto_self_update = "disable"` (close-out item 3); `python@3.13` pinned in Homebrew, Python 3.13.5 (close-out item 12); `rust-code-analysis-cli` 0.0.25; RustSec databases at `e2111519`; cargo-nextest 0.9.146, cargo-llvm-cov 0.9.1, cargo-audit 0.22.2, cargo-deny 0.20.2, cargo-geiger 0.13.0, picotool 2.3.0. TV-011 to TV-013 and the Rust tools are not Accredited (TV-012 re-validated at `e34a27b`, ACC-COMPLEXITY-001 conditional on the INSP-015 delta), so their outputs are developer evidence (CM plan section 9.1; SWE-136).
- Images (`uf2-info.txt`, `cwht-app-build.txt`, `blinky-build.txt`, `elf-diff.txt`):
  - `cwht-app.uf2` `4e0bd133...3529` and `rustos-blinky.uf2` `c45b5268...08d3` are **byte-identical** to the run 3 files and to the run 1 files that run 4 loaded and verified on the board (`cmp` exit 0 for all four comparisons; the SHA-256 equal the run 4 load-time values).
  - The ELF files are not byte-identical to run 3: `cwht-app.elf` `104f40fa...4b48` against `388d1d16...a5bf`, `rustos-blinky.elf` `e826dbf0...fb61` against `3c0ac074...bd08`. Every loadable section (`.vector_table`, `.boot_info`, `.text`, `.rodata`, `.data`) is identical, and so are `.debug_loc`, `.debug_abbrev`, `.debug_aranges`, `.debug_ranges`, `.debug_frame`, `.symtab`, `.comment` and `.ARM.attributes`. The differing sections are, for cwht-app, `.debug_info`, `.debug_str`, `.debug_line` and `.strtab`, and for the blinky `.strtab` only.
  - Cause, from the diff of inputs: the source is the same, and only the build directory changed. Run 3 built under `<scratch>/r3/r3/cwht` with rustos through a link to `/Users/robinonsay/rust/rustos-wp-sw-licence`; run 5 builds under `<scratch>/r5/cwht` with rustos at `<scratch>/r5/rustos`. The debug information records those absolute paths, and the cwht-app file is 1168 B shorter for the shorter paths. Cargo derives each crate's `-C metadata` hash from the package identity, which for a path dependency includes its path, and that hash is part of the mangled symbol names in `.strtab` (for example `blinky.8bebe34240b5da1d-cgu.0` against `blinky.9e1d117ba0259f83-cgu.0`, 7 differing names, same length). Two clean rebuilds in the same layout give one SHA-256 for each image (steps 4 and 8).
- Differences from the operational configuration: as run 1 section 3.

## 4. Results of each step

| Step | Procedure text (as run) | Expected | Observation | Artifact | Pass/Fail |
|---|---|---|---|---|---|
| 1 | Record configuration; rustos commit and rustc against the lock | Lock rows match; rustos code clean | cwht `fb22b7a`; lock copy equal to the commit; rustos clone `2ec64c0`, clean, tree equal to the export (D20), equal to the lock row and to rustos `master`; rustc in `firmware/` from the pin, equal to the lock row; every tool version recorded, including the close-out items 2, 3 and 12 state | `versions.txt` | Pass |
| 2 | `cargo build` on the host | exit 0 | exit 0 | `host-build-test.txt` | Pass |
| 3 | `cargo test` on the host | all pass, at least 10 | 10 passed, 0 failed (5 `heartbeat`, 5 `gpio`) | `host-build-test.txt` | Pass |
| 4 | Target build; no warning; map written; memory from gate G2 | exit 0, no warning, map | `PASS G2 build`, `PASS G2 no compiler warning`; FLASH 1608 B of 4194304 B (0.04 %), RAM 8200 B of 532480 B (1.54 %); `PASS G2 no allocator symbol`, `PASS G2 image dependency set`. D9: two clean rebuilds and the gate build give one SHA-256 `104f40fa...4b48`; the `--keep-going` build equals the stopping-run build (`cmp` exit 0); loadable sections identical to run 3 | `sw-gate-full.txt`, `cwht-app.map`, `cwht-app-build.txt` | Pass |
| 5 | fmt, host clippy, target clippy with `-D warnings` (gate G1) | no diff, no warning | `PASS G1 cargo fmt --check`, `PASS G1 clippy host`, `PASS G1 clippy target` | `sw-gate-full.txt` | Pass |
| 6 | `tools/sw_gate.sh` and `tools/sw_gate.sh --keep-going` | exit 0 (FW-B0 exit criterion) | Stopping run: G0 to G4 PASS; G5 cargo audit, cargo deny (bans, licenses, sources), deny advisories, the three geiger checks and the unsafe audit PASS; then `FAIL CS-38 .../cwht-app/src/main.rs:30 main CC 4 > 3` and `FAIL G5 complexity`, `sw_gate: FAIL at G5 complexity`, exit 1. Keep-going run: 24 gate-step PASS lines, 2 FAIL (`G5 complexity`, `G5 Miri (nightly, non-credit, MSR-08)`), 0 MISSING, 1 SKIP line (emulation stub), `sw_gate: FAIL (2 step(s) failed, 0 prerequisite(s) missing)`, exit 1. G6 stable coverage 100 percent lines and regions (70 of 70); MSR-14 branches 4 of 4, lines 70 of 70, regions 70 of 70; G6 measurements PASS | `sw-gate-full.txt`, `sw-gate-keep-going.txt`, `unsafe-audit.txt` | Blocked |
| 7 | Gate known-answer runs KA-0 to KA-8 | KA-0 exit 0; KA-1 to KA-7 exit 1 at the seeded gate; KA-8 exit 1 with the G3 comparison FAIL | All nine MATCH, first FAIL lines as in run 3: KA-1 and KA-4 `FAIL G1 clippy host`, KA-2 `FAIL G1 cargo fmt --check`, KA-3 `FAIL G3 host tests run 1`, KA-5 `FAIL G0 rustc ...`, KA-6 `FAIL G1 clippy target`, KA-7 `FAIL G2 no compiler warning`; KA-8 exit 1 with `FAIL G3 identical result sets (JUnit file of run 1 or run 2 not written by this invocation)`, stale files removed; KA-8 G5 Miri ran to completion without a prompt (D14 gone); extra KA-8 lines explained by D21. 0 `INTERIM` lines. rustos clone clean after all nine | `gate-known-answer.sh`, `gate-known-answer.txt` | Pass |
| 8 | Fresh rustos blinky (templates/pico2 of the pinned commit, path form), two builds | two identical SHA-256 | both `e826dbf0...fb61`; loadable sections identical to run 3 (section 3 gives the non-loadable difference) | `blinky-build.txt`, `rustos-blinky.elf`, `elf-diff.txt` | Pass |
| 9 | `picotool uf2 convert` and `picotool info -a` for both images | RP2350, ARM Secure, one image def block each | all four commands exit 0; both RP2350, ARM Secure, one image def block; both UF2 files byte-identical to runs 1 to 3 and to the files run 4 loaded | `uf2-info.txt`, `rustos-blinky.uf2`, `cwht-app.uf2` | Pass |
| 10 | Blink-rate prediction | windows computed | `.text` of both images identical to run 3, so the run 2 prediction holds unchanged: 10 to 120 and 3 to 45 cycles in 60 s | `blink-rate-prediction.txt` | Pass |
| 11 | Flash and observe the rustos blinky | load verified, reboot exit 0, 10 to 120 cycles in 60 s | **Not repeated in run 5; stands on run 4.** Run 4 step 11 loaded `rustos-blinky.uf2` `c45b5268...08d3`, "Verifying Flash ... OK", reboot exit 0, 60 to 63 cycles in 60 s, Pass. The run 5 UF2 is the same file byte for byte (`cmp` exit 0), so the owner step need not be repeated | run 4 `step11-info.txt`, `step11-load.txt`, `step11-observation.txt`; `uf2-info.txt` | Pass (run 4) |
| 12 | Flash and observe cwht-app | load verified, reboot exit 0, 3 to 45 cycles in 60 s | **Not repeated in run 5; stands on run 4.** Run 4 step 12 loaded `cwht-app.uf2` `4e0bd133...3529`, verify OK, reboot exit 0, 18 cycles in 60 s, Pass. The run 5 UF2 is the same file byte for byte | run 4 `step12-load.txt`, `step12-observation.txt`; `uf2-info.txt` | Pass (run 4) |
| 13 | Record versions, commits, blob and hashes | recorded | this report and its front matter | this file | Pass |
| 14 | Stop rule | NCR on discrepancy | no product discrepancy in the cwht workspace or rustos `2ec64c0`; the two FAIL lines come from an open owner decision on the complexity allowance and from the scope of the gate's Miri command (section 7), proposed for disposition, not NCRs | none | n/a |

## 5. Analysis of results

- **CR-004 in the repository gate.** With the lock pin at `2ec64c0`, G0 passes against the pinned commit and `PASS G5 cargo deny (bans, licenses, sources)` and `PASS G5 unsafe audit` hold on the committed list (37 sites: block 16, fn 11, impl 1, extern 3, attr 6; 0 without SAFETY; 37 unsigned, a note until CDR). Run 3 items B1 and B2 are closed in the repository gate, which is the verification row of CR-004 section 5.
- **Close-out item 2.** Miri now runs: no prompt, no download, sysroot reused. The step fails for a new reason (below).
- **G5 complexity FAIL (open owner decision).** The invocation fix of INSP-016 finding-14 works in the gate: the analyzer reads all three roots and `tools/complexity_gate.py` reports 52 functions, maximum CC 5, mean 1.46, none above 12 (MSR-17), so CS-17 passes. CS-38 has one failure, exactly the result CR-005 section 9 and TV-012 run 2 predicted: `cwht-app/src/main.rs:30 main CC 4 > 3`. `main` is analyzer CC 2 (its CS-19 main `loop` counts) plus 2 for the two `let ... else`, against an allowance of 3 (1 plus 2 CS-11 failure arms, 0 halt loops credited to `main`). `safe_state_halt` passes on its halt-loop allowance. Close-out item 4 gave the +1 allowance to the two CS-19 halt loops (the panic handler and `safe_state_halt`); it did not name the third unbounded loop of CS-19, the main loop of `cwht-app::main`. Closing this needs the owner's decision recorded in CR-005 section 9 (TV-012 limitation 8). It is not a code defect: the code is the code the SRR reviewed.
- **G5 Miri FAIL (gate scope).** The gate runs `cargo +nightly-2026-08-24 miri test -p api -p pico2 --lib` on the host (aarch64-apple-darwin). `api` builds and runs under Miri, with 0 unit tests. `pico2` does not compile for the host: `error: invalid Mach-O section specifier` at `rustos/firmware/pico2/src/lib.rs:149` (`#[unsafe(link_section = ".boot_info")]`) and `:539` (`".vector_table"`). A Mach-O host target needs a `segment,section` specifier, and these ELF section names exist only for the RP2350 image. `pico2` is target-only for the same reason that `cwht-app` is excluded from host clippy. 07 section 8.1 scopes Miri to "the host tests of `api` and of the host-compilable `pico2` decision functions (CS-38)", and `pico2` has no host-compilable part today, so the gate command is wider than the plan. Run 3 could not see this, because Miri stopped earlier on the missing `rust-src`. Neither rustos nor cwht code is at fault.
- **Reproducibility.** Two clean cwht-app builds and the gate builds give one SHA-256, and two blinky builds give one SHA-256. Across layouts, the loadable bytes and both UF2 files equal runs 1 to 4, and the non-loadable differences come only from the build paths (section 3; SWE-186 for the host tests by G3).
- **Known-answer runs.** All nine match on the pinned rustos, with Miri now running to completion inside KA-8. The G0, G1, G2 warning and G3 decisions still discriminate.

## 6. Data tables, plots and pictures

All data are text logs, scripts and images in `docs/vv/reports/TC-SW-TOOL-001-r5/`, listed with SHA-256 in the front matter. Steps 1 to 10 produce no plot or photograph. `run5.sh` and `gate-known-answer.sh` are the exact procedures run, `rustup-guard.sh` is the D13 shim, `elf-diff.txt` is the section-by-section ELF comparison of section 3, and `layout-after.txt` is the layout state after the run (D20).

Gate result summary (`--keep-going`; sub-result lines such as FLASH, RAM and the CS-38 detail are not counted):

| Gate | PASS | FAIL | MISSING | SKIP |
|---|---|---|---|---|
| G0 | 1 | 0 | 0 | 0 |
| G1 | 3 | 0 | 0 | 0 |
| G2 | 5 | 0 | 0 | 0 |
| G3 | 3 | 0 | 0 | 0 |
| G4 | 1 | 0 | 0 | 0 |
| G5 | 7 (cargo audit; cargo deny; deny advisories; geiger 3; unsafe audit) | 2 (complexity; Miri) | 0 | 0 |
| G6 | 4 (stable coverage; branch and condition coverage; emulation stub; measurements) | 0 | 0 | 1 (emulation line) |

Image identity:

| Image | Run 5 SHA-256 | Run 3 | Run 1 file loaded in run 4 | Byte-identical |
|---|---|---|---|---|
| `cwht-app.uf2` | `4e0bd133...3529` | `4e0bd133...3529` | `4e0bd133...3529` | yes (`cmp` exit 0) |
| `rustos-blinky.uf2` | `c45b5268...08d3` | `c45b5268...08d3` | `c45b5268...08d3` | yes (`cmp` exit 0) |
| `cwht-app.elf` | `104f40fa...4b48` | `388d1d16...a5bf` | n/a | no: loadable sections identical, debug and symbol-name sections differ by build path |
| `rustos-blinky.elf` | `e826dbf0...fb61` | `3c0ac074...bd08` | n/a | no: loadable sections identical, `.strtab` differs by build path |

## 7. Non-conformances and discrepancies

| NCR | Severity | Step | Summary | Disposition | Retest planned |
|---|---|---|---|---|---|
| None | | | | | |

Status of the blocking items of runs 3 and 4 and the new one (none is a defect of the cwht workspace or rustos `2ec64c0`):

| # | Gate line or item | Run 5 status | Closes on | Owner |
|---|---|---|---|---|
| B1, B2 | `G5 cargo deny (bans, licenses, sources)`, `G5 unsafe audit` | **Closed**: PASS in the repository gate on the committed lock and list (CR-004) | closed | none |
| B7 | steps 11 and 12 | Closed by run 4; the run 5 UF2 files are byte-identical, so run 4 stands | closed | none |
| B8 | `G5 complexity` (invocation) | **Closed**: the gate reads all three roots (52 functions) | closed | none |
| B9 | `G5 complexity` (convention) | CS-17 PASS; CS-38 FAIL on `cwht-app` `main` CC 4 against allowance 3 (CR-005 section 9; TV-012 limitation 8) | the owner's decision whether the CS-19 main loop of `cwht-app::main` receives the +1 allowance (or another disposition), applied to 07 and `tools/complexity_gate.py` by CR, TV-012 re-validated, then a gate re-run | Robin (decision); 07 owner and tool owner (Claude) apply it |
| B10 | `G5 Miri` (component) | **Closed**: `rust-src` and the sysroot are installed (close-out item 2); Miri runs without prompt or download | closed | none |
| B11 | `G5 Miri` (scope) | New. FAIL: `pico2` does not compile for the Mach-O host (`link_section = ".boot_info"` and `".vector_table"`); `api` passes with 0 tests | a change of the gate's Miri command to the scope of 07 section 8.1 (host-compilable crates only, for example `-p api` until `pico2` has host-compilable decision functions), or a rustos change that applies the two `link_section` attributes only for the target (`cfg_attr(target_os = "none", ...)`), which is the owner's act as rustos maintainer and would need a CR to move the pin; then a gate re-run | `tools/sw_gate.sh` maintainer with the 07 owner (Claude), or Robin as rustos maintainer; the choice is the 07 owner's to propose |

## 8. Status of enabling equipment after the run

- cwht repository: unchanged by the run (the layout was a `git archive` in the scratch area, deleted after the run). This filing adds only this report and its artifact directory.
- rustos: the owner's repository is unchanged: `master` at `2ec64c0` before and after, working tree not read or written (D20). The scratch clone and export were deleted.
- Toolchains: as installed under decision 109 and close-out items 2, 3 and 12. Nothing was installed, updated or downloaded by the run (D13).
- Board `pico2-devboard-1`: not used; it still holds `kat-target.uf2` from run 4 OA-2.

## 9. Conclusions and recommendations

Verdict: Blocked. On the pinned rustos `2ec64c0` every gate step passes except two. G5 complexity fails one CS-38 check that waits on an open owner decision (CR-005 section 9). G5 Miri fails because the gate asks Miri to compile the target-only `pico2` crate on the host. Run 3 items B1, B2, B8 and B10 and run 4's B7 are closed. Both UF2 images are byte-identical to the images the owner loaded and observed in run 4, so steps 11 and 12 do not need to be repeated. The FW-B0 exit criterion (gate exit 0) is not met, so precondition P6 of the baseline record stays Not met. No requirement status changes (dev-board case, `credit: false`).

Recommendations:

1. Owner: decide B9, the CS-38 allowance for the CS-19 main loop of `cwht-app::main` (CR-005 section 9, TV-012 limitation 8). The 07 owner and the tool owner then apply it by CR and re-validate TV-012.
2. 07 owner with the `tools/sw_gate.sh` maintainer: propose the B11 fix, either the gate's Miri command narrowed to the 07 section 8.1 scope or a rustos `cfg_attr` change for the owner as rustos maintainer, and record the choice.
3. Claude: after 1 and 2, run the gate again as run 6 (steps 1 to 10 and 13) on the same layout method (D20). Steps 11 and 12 again cite run 4 if the UF2 files stay byte-identical.
4. `tools/sw_gate.sh` maintainer: G0 cannot run on a plain `git archive` export of rustos (D20). The lock row names the command `git -C /Users/robinonsay/rust/rustos rev-parse master`, while the gate runs `git -C "$RUSTOS" rev-parse HEAD`. Consider a documented way for G0 to accept an export, such as a recorded tree hash. Minor, a lien due PDR.
5. Observation for the 07 owner, Minor, a lien due PDR: Miri on `api` runs 0 unit tests, so MSR-08 is empty until `api` or `pico2` host-compilable code has tests.

Deferrals FD-1 and FD-2 of run 1 stand unchanged.

## 10. As-run procedure

Steps 1 to 10 and 13 are run as written in `docs/test_cases/sw-tool/test_cases.json` (blob `fee1e724`, unchanged), by `run5.sh` and `gate-known-answer.sh`, with deviations D1 to D21 of section 2. Step 5 ran as gate G1 within step 6. Steps 11 and 12 are not repeated; they cite run 4 on byte-identical images (section 4).

## 11. Answers to INSP-016 findings (author response for the reviewer's next iteration)

The reviewer, not the author, changes the record (`docs/reviews/SRR/checklists/fw-b0-toolchain-proof.md`).

| Finding | Severity | Author response | What closes it |
|---|---|---|---|
| finding-1 (F-01) | Major | Run 5 on the pinned `2ec64c0` closes B1, B2, B8 and B10 in the repository gate: 24 PASS, 0 MISSING, 2 FAIL. The gate still exits 1 on B9 (open owner decision, CR-005 section 9) and B11 (gate Miri scope, found now that Miri runs) | B9 and B11 dispositioned and applied, then a gate run with exit 0 |
| finding-14 (F-14) | Minor (lien) | Gate integration shown: `G5 complexity` reads all three roots (52 functions) and reaches `tools/complexity_gate.py`; its FAIL is the B9 convention result, not the invocation | reviewer verification |

## 12. Authentication and authorization

- Results authenticated by (conductor): claude, 2026-09-26
- Witnessed by: owner, not applicable to run 5 (no owner-performed step; steps 11 and 12 stand on run 4, witnessed 2026-09-26 19:17 to 19:23 CDT, on byte-identical images)
- Authorization of acceptability (owner): pending
