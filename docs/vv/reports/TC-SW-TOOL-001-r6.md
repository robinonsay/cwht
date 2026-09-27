---
test_case: TC-SW-TOOL-001
run: 6
requirement_ids: [REQ-SYS-127, REQ-SYS-128, REQ-SYS-133]
validates: []
verification_method: Demonstration
type: Bench
credit: false
result: Pass
date: 2026-09-27
conductor: claude
witness: owner
article: pico2-devboard-1
firmware_version: "n/a"
source_commit: "bb2485ea52d378da7b8c8a326238f9418579bd4f"
firmware_elf_sha256: "14e431498a4be04328098d2b860f75af630a2bee180e03b6dd5486256cb2f6a9"
requirements_baseline: "none (SRR approved with liens 2026-09-26; baseline/srr not yet tagged)"
procedure_commit: "bb2485e"
procedure_blob: "fee1e7246af59d5e8a43ed1b9cdf483854053fdc"
toolchain_lock: "tools/toolchain.lock.md blob 04819139c8a10cc6a970d7d08684f7487bf968bb at bb2485e (rustos row 2ec64c0f15c8cd2dbcaa241abffdd72f8cae467c from CR-004; run from the committed file, no temporary edit)"
harness_versions: "n/a"
instruments:
  - "Host only: owner's Mac (macOS 26.6.2, arm64); no board connected in this run (steps 11 and 12 cite run 4, section 4); tools/toolchain.lock.md rows as re-observed 2026-09-27 08:21 CDT (versions.txt); no calibration applicable"
ncr_ids: []
artifacts:
  - "docs/vv/reports/TC-SW-TOOL-001-r6/versions.txt sha256=4204bc78d39c78985991aca2286c6ba89d9d49f7a71a0dd86962ab7b582cf261"
  - "docs/vv/reports/TC-SW-TOOL-001-r6/host-build-test.txt sha256=6fadea4f96b35a8bccad507eecffad775faa7256ed0e3e91d971610fad6b28bd"
  - "docs/vv/reports/TC-SW-TOOL-001-r6/unsafe-audit.txt sha256=007eabe628864be272c79b24d5b7631b1a75a78e8807c9eaa0e2c9da0a7eacb3"
  - "docs/vv/reports/TC-SW-TOOL-001-r6/sw-gate-full.txt sha256=c3e0d645b77c66526e595e8e2b657871255fe32190a7d759c44e1e7b5aee32e1"
  - "docs/vv/reports/TC-SW-TOOL-001-r6/sw-gate-keep-going.txt sha256=9985814ac20cb4dca6aa3ea2169c766f71a676f052e3282a5e887b3da3554f69"
  - "docs/vv/reports/TC-SW-TOOL-001-r6/gate-known-answer.sh sha256=b8bf4f61c7b6ac7cb84054cf912831b1bd84861a34f90d8c7f46eb6ca5f9cb1d"
  - "docs/vv/reports/TC-SW-TOOL-001-r6/gate-known-answer.txt sha256=7e2191eb9eed723e4399a867779157e3a2b9eecdae25b635b513451230b7ee62"
  - "docs/vv/reports/TC-SW-TOOL-001-r6/run6.sh sha256=a86dbc4e349dc6c059b892403dc6fa29fadefe88921f92a92d6de34731c5a6b0"
  - "docs/vv/reports/TC-SW-TOOL-001-r6/rustup-guard.sh sha256=9b1ea18c5d5983d7311c0011ecba4a5add1841e99dbc630ed9dc3ad698269828"
  - "docs/vv/reports/TC-SW-TOOL-001-r6/blinky-build.txt sha256=93c44d4fa79377f2ed9f5fd171855d9cba3be8cd877bc867cee89950d6babae0"
  - "docs/vv/reports/TC-SW-TOOL-001-r6/rustos-blinky.elf sha256=35062bec04ca31878608fde1f54e777424807c6cfddfe05785312a78fbb4ee92"
  - "docs/vv/reports/TC-SW-TOOL-001-r6/rustos-blinky.uf2 sha256=c45b526837c0831206763eb3134a8e71c854059ff7442c19e51f39edf03308d3"
  - "docs/vv/reports/TC-SW-TOOL-001-r6/cwht-app-build.txt sha256=77421595017a0289663ad487d597101a14ddcdbfafafc4385ee494d0047d9663"
  - "docs/vv/reports/TC-SW-TOOL-001-r6/cwht-app.elf sha256=14e431498a4be04328098d2b860f75af630a2bee180e03b6dd5486256cb2f6a9"
  - "docs/vv/reports/TC-SW-TOOL-001-r6/cwht-app.uf2 sha256=4e0bd133a10b6e29f72f00023ec407cd1885b8550a685b881c7be213462b3529"
  - "docs/vv/reports/TC-SW-TOOL-001-r6/cwht-app.map sha256=9f7bf67362e7630d3e5ccd62dd2aa7b198cfd14af0141bb33d8fdfd2aa61e7b3"
  - "docs/vv/reports/TC-SW-TOOL-001-r6/uf2-info.txt sha256=cf292fbbef4471d8248fb5341fcbf419db6109ba941cd9a2f3e1161a84989436"
  - "docs/vv/reports/TC-SW-TOOL-001-r6/blink-rate-prediction.txt sha256=bf0469f6d9e74d284d9d407b09a29eb63c396074ff485d543375d47bd0a14411"
  - "docs/vv/reports/TC-SW-TOOL-001-r6/elf-diff.sh sha256=cf3161f34722700c47ed456af6fefec8ff38e90b2a9cd7902b2afa72e97fbb6b"
  - "docs/vv/reports/TC-SW-TOOL-001-r6/elf-diff.txt sha256=bc6c00c87bd0740e3880d4b1a000fed3546a65b649f0374bec0dbff0111ec951"
  - "docs/vv/reports/TC-SW-TOOL-001-r6/layout-after.txt sha256=36cbc914595d23dd3a2a9e797cefbddadfa2ff9a1f7bfeb30b60cd425cdc3135"
  - "docs/vv/reports/TC-SW-TOOL-001-r6/download-check.txt sha256=e63294002f3ff3af20ede088c294e541bc3f92f2b4975214e8609b37eb58b7f8"
mop_values: []
---

# Verification report: TC-SW-TOOL-001 run 6

**Status of this run: Pass.** Run 6 is the automated gate part of the case (steps 1 to 10 and 13), run after SRR close-out items A and B were applied. The owner ruled both items on 2026-09-27 (minutes `786822a`, "Close-out decisions A to C and repository protection"; owner statement "Done and added. I approve the other recommendations"). Claude ran it on 2026-09-27 between 08:21 and 08:23 CDT on the run 5 layout method: a `git archive` of cwht `bb2485e`, a `git archive` export of rustos `2ec64c0`, and a local clone of the owner's rustos repository at `2ec64c0` for gate G0 (D20). The run 3 download guard was first on `PATH`. **The gate exits 0 in both modes.** The stopping run ends `sw_gate: PASS (G0 to G6)`. The `--keep-going` run has 26 gate-step PASS lines (29 PASS lines with the FLASH, RAM and G3 detail sub-result lines), 0 FAIL, 0 MISSING and 1 SKIP (the emulation stub line), and it also ends `sw_gate: PASS (G0 to G6)` (section 6). Both UF2 images are byte-identical to runs 3 and 5 and to the run 1 files that run 4 loaded and verified on the board, so steps 11 and 12 stand on run 4. This is a dev-board case: `credit: false`, credit row `SUPPORT`, and it changes the status of no requirement (docs/process/04-verification-and-validation.md section 4, rule 7.3.12). Runs 1 to 5 are not edited.

## 1. Objectives and degree to which they were met

The case, its objective and its requirements are unchanged (case blob `fee1e724` at `bb2485e`). The objective is the FW-B0 exit criterion of docs/process/07-software-engineering-plan.md section 3.2 and the SRR toolchain-proof product of 07 section 3.1 (SRR package item H12; baseline record section 0.1, precondition P6).

| Requirement | Acceptance criterion (this case) | Measured or observed, run 6 | Met? |
|---|---|---|---|
| REQ-SYS-127 | Rust workspace builds for `thumbv8m.main-none-eabihf` against rustos by path; image runs on a Pico 2 | Release build on the pinned `1.98.0`, exit 0, no warning. FLASH 1608 B (0.04 %) and RAM 8200 B (1.54 %), from `tools/measurements.py --link-map`. Dependency set `cwht-app`, `cwht-core`, `api`, `pico2`. Loadable sections identical to run 5. On-board run: run 4, on the byte-identical UF2 (section 4, steps 11 and 12) | Partially (supporting only; closes by Inspection, row I) |
| REQ-SYS-128 | `cwht-core` and `cwht-hal-mock` build and test on the host; the same `cwht-core` links into the target image | Host build exit 0. 10 of 10 tests pass, twice, with identical result sets (G3). 100 percent lines and regions of both host crates (G6, developer evidence) | Met for this case (supporting only; closes by Inspection, row I) |
| REQ-SYS-133 | `picotool load -v` of both UF2 images succeeds and the images run | Both run 6 UF2 files are byte-identical to the files loaded and verified in run 4 (`cmp` exit 0). `picotool info -a`: RP2350, ARM Secure, one image def block each | Met for this case by run 4 on the same bytes (supporting only; closes by Demonstration on the delivered unit, row D) |

## 2. Description of the activity and deviations

Order of execution:

1. `run6.sh`: steps 1 to 6 and 8 to 10, 08:21:44 to 08:22:09 CDT. The gate time stamps are 13:21:49Z for the stopping run and 13:21:57Z for `--keep-going`.
2. `gate-known-answer.sh`: step 7, 08:22:23 to 08:22:40.
3. `elf-diff.sh`: the section 3 ELF comparison, 08:23 (D22).
4. The download check over `gate-known-answer.txt`, appended to `download-check.txt` at 08:23.

The layout, the known-answer copies and all build directories were deleted after the run.

Inputs changed since run 5 (`git diff --stat fb22b7a bb2485e`, gate inputs only):

- `tools/sw_gate.sh`, blob `29a37127` (`495a0c3`, close-out item B): the G5 Miri command changes from `-p api -p pico2 --lib` to `-p api --lib`, the host-compilable scope of 07 section 8.1. A comment and the header's G5 line give the reason and name FW-B1 as the point where the exclusion ends.
- `tools/complexity_gate.py`, blob `ddf10798` (`106bc3a`, CR-005 amendment 1, close-out item A): the bare `loop` of `cwht-app::main` is credited to the CS-38 allowance of `main`. TV-012 run 3 re-validated the script at `0da559a`.
- `tools/toolchain.lock.md`, blob `04819139`: the `tools/sw_gate.sh` row records the item B change and its re-validation.

No file under `firmware/` changed, and neither did `firmware/Cargo.toml`, `Cargo.lock`, `.cargo`, `rust-toolchain.toml` or `firmware/unsafe-audit.md` (`versions.txt` blobs equal run 5). rustos is the same commit `2ec64c0`, `master` in the owner's repository.

Deviations from the case, and from runs 1 to 5 (none affects credit, because the run carries none):

- D1 and D4 stay closed. The pinned `1.98.0` is in use, and every gate invocation, including KA-0 to KA-8, has 0 `INTERIM` lines.
- D8 is unchanged: the comment at `cwht-app/src/main.rs:36-40` still reads "owner disposition before FW-B1" (cross item of run 3, still open; not a gate input). `main.rs` is blob `e32006a5`, the same as run 5.
- D9 repeated: two independent clean rebuilds (step 4). D10 not repeated: the committed `firmware/unsafe-audit.md` (blob `18ef484b`) is checked as committed.
- D12 stays closed: the lock in the layout is the committed file (`diff` exit 0 in `versions.txt`).
- D13 repeated, with the same settings as run 5:
  - `RUSTUP_AUTO_INSTALL=0`, `CARGO_NET_OFFLINE=true` and `MIRI_AUTO_OPS=no`.
  - The run 3 `rustup` shim first on `PATH` (`rustup-guard.sh`, byte-identical to runs 3 and 5, sha256 `9b1ea18c...9828`).
  - stdin from `/dev/null` for every command.

  The check is now recorded (`download-check.txt`): the pattern "Downloading", "Updating crates", "downloading component", "rustup-guard" or "Installing" matches 0 lines in each of the nine run 6 logs.
- D14 does not recur: Miri ran without a prompt in the gate and in KA-8.
- D19 carried: steps 11 and 12 are not repeated (section 4).
- D20 carried unchanged. The owner's rustos working tree holds uncommitted work of the owner's own and was neither read nor written. The layout has two rustos trees: `<scratch>/r6/rustos-export`, the `git archive 2ec64c0` export, and `<scratch>/r6/rustos`, a local clone of the owner's repository (`git clone --no-hardlinks --no-checkout`, objects only, then `checkout --detach 2ec64c0`) that gives G0 its commit identity. The clone's tree equals the export: `diff -r` with `.git` excluded exits 0, 364 files each (`versions.txt`). It still equals the export after the run, with `target` also excluded (`layout-after.txt`). The build, the audit and the gate read the clone, so every result is bound to the commit.
- D21 carried: KA-8 records every result line. Its extra FAIL groups now come only from the known-answer copy itself. `G4 traceability` fails because the copy holds no `tools/traceability.py` or `docs/`. `G5 unsafe audit` fails because the copy links rustos through a symbolic link, which `tools/unsafe_audit.py` resolves. The run 5 KA-8 FAILs of `G5 complexity` and `G5 Miri` are gone; both now PASS inside KA-8.
- D22 (new). **ELF comparison script.** Run 5 wrote `elf-diff.txt` by hand commands, and `run6.sh` carries an ELF block for it. That block took its section list from `rust-size -A`, which omits `.symtab`, `.shstrtab` and `.strtab`. `elf-diff.sh` repeats the comparison over every section `rust-readobj --sections` lists, the run 5 method, and adds the `.strtab` symbol-name difference. It overwrote the `run6.sh` output at 08:23, before the layout was deleted. `run6.sh` is filed as it ran. The first output agreed with the second on every section it listed.

## 3. Configuration under test and differences from the operational configuration

- Article: `pico2-devboard-1`, not connected in this run.
- cwht commit `bb2485ea52d378da7b8c8a326238f9418579bd4f`, committed content only (`git archive`, `.venv` linked). Gate scripts and inputs (`versions.txt`):

  | File | Blob |
  |---|---|
  | `tools/sw_gate.sh` | `29a37127` (file sha256 `cd804ba0...8dcf1`, the value the item B re-validation recorded in the lock) |
  | `tools/measurements.py` | `abe25acb` |
  | `tools/unsafe_audit.py` | `cc3aaa2a` |
  | `tools/complexity_gate.py` | `ddf10798` (TV-012 run 3) |
  | `tools/emu_run.sh` | `17f102aa` |
  | `firmware/unsafe-audit.md` | `18ef484b` |
- rustos commit `2ec64c0f15c8cd2dbcaa241abffdd72f8cae467c` (parent `c54d35a`). It equals the lock row and `git -C /Users/robinonsay/rust/rustos rev-parse master`, both before and after the run (D20).
- Tools: the same versions as run 5 (`versions.txt` differs from run 5 only in the cwht commit and the three changed blobs):
  - pinned `rustc 1.98.0 (88d9e12ae 2026-08-18)`, with clippy, rustfmt and llvm-tools;
  - `nightly-2026-08-24` with `miri`, `llvm-tools` and `rust-src`, `miri 0.1.0 (fb6531d550 2026-08-23)`, Miri sysroot in `~/Library/Caches/org.rust-lang.miri`;
  - rustup 1.29.1 with `auto_self_update = "disable"`;
  - Python 3.13.5 (`python@3.13` pinned);
  - `rust-code-analysis-cli` 0.0.25;
  - RustSec databases at `e2111519`;
  - cargo-nextest 0.9.146, cargo-llvm-cov 0.9.1, cargo-audit 0.22.2, cargo-deny 0.20.2, cargo-geiger 0.13.0;
  - picotool 2.3.0.

  TV-011 to TV-013 and the Rust tools are not Accredited, so their outputs are developer evidence (CM plan section 9.1; SWE-136).
- Images (`uf2-info.txt`, `cwht-app-build.txt`, `blinky-build.txt`, `elf-diff.txt`):
  - `cwht-app.uf2` `4e0bd133...3529` and `rustos-blinky.uf2` `c45b5268...08d3` are **byte-identical** to the run 3 files, the run 5 files, and the run 1 files that run 4 loaded and verified on the board. `cmp` exits 0 for all six comparisons, and the SHA-256 values equal the run 4 load-time values (`docs/vv/reports/TC-SW-TOOL-001-r4/image-identity.txt`).
  - The ELF files are not byte-identical to run 5: `cwht-app.elf` is `14e43149...f6a9` against `104f40fa...4b48`, and `rustos-blinky.elf` is `35062bec...ee92` against `e826dbf0...fb61`. Both pairs have the same length (172864 B and 134504 B). Every loadable section (`.vector_table`, `.boot_info`, `.text`, `.rodata`, `.data`) is identical, and so are `.debug_loc`, `.debug_abbrev`, `.debug_aranges`, `.debug_ranges`, `.debug_frame`, `.symtab`, `.shstrtab`, `.comment` and `.ARM.attributes`. For cwht-app, `.debug_info`, `.debug_str`, `.debug_line` and `.strtab` differ; for the blinky, only `.strtab` differs.
  - Cause: this is the run 5 mechanism with a one-character path change. The source and the rustos commit are the same as run 5; only the layout directory changed, from `<scratch>/r5` to `<scratch>/r6`. The debug information records those absolute paths. Cargo's `-C metadata` hash for a path dependency includes the path, and the hash appears in the mangled symbol names in `.strtab`: 7 differing names of equal length in each file, for example `cwht_app.54672e91d79acd62-cgu.0` against `cwht_app.4e406d9f02e6aa5b-cgu.0`. The link map (`cwht-app.map`) has the same addresses and sizes as run 5; its 19 differing lines are object-file paths and hash names only. Within the layout, two clean rebuilds and the gate build give one SHA-256 for `cwht-app` (`14e43149...f6a9`), and two builds give one for the blinky (`35062bec...ee92`).
- Differences from the operational configuration: as run 1 section 3.

## 4. Results of each step

| Step | Procedure text (as run) | Expected | Observation | Artifact | Pass/Fail |
|---|---|---|---|---|---|
| 1 | Record configuration; rustos commit and rustc against the lock | Lock rows match; rustos code clean | cwht `bb2485e`; lock copy equal to the commit; the lock's rustos row is `2ec64c0`. rustos clone at `2ec64c0`, clean, with a tree equal to the export (D20), the lock row and rustos `master`. rustc in `firmware/` comes from the pin and equals the lock row. Every tool version is recorded | `versions.txt` | Pass |
| 2 | `cargo build` on the host | exit 0 | exit 0 | `host-build-test.txt` | Pass |
| 3 | `cargo test` on the host | all pass, at least 10 | 10 passed, 0 failed (5 `heartbeat`, 5 `gpio`) | `host-build-test.txt` | Pass |
| 4 | Target build; no warning; map written; memory from gate G2 | exit 0, no warning, map | `PASS G2 build` and `PASS G2 no compiler warning`. FLASH 1608 B of 4194304 B (0.04 %), RAM 8200 B of 532480 B (1.54 %), MSR-18 and MSR-19 Green. `PASS G2 link map (measurements.py)`, `PASS G2 no allocator symbol`, `PASS G2 image dependency set`. D9: two clean rebuilds and the gate build give one SHA-256, `14e43149...f6a9`. The `--keep-going` build equals the stopping-run build (`cmp` exit 0). Loadable sections identical to run 5 | `sw-gate-full.txt`, `cwht-app.map`, `cwht-app-build.txt` | Pass |
| 5 | fmt, host clippy, target clippy with `-D warnings` (gate G1) | no diff, no warning | `PASS G1 cargo fmt --check`, `PASS G1 clippy host`, `PASS G1 clippy target` | `sw-gate-full.txt` | Pass |
| 6 | `tools/sw_gate.sh` and `tools/sw_gate.sh --keep-going` | exit 0 (FW-B0 exit criterion) | Stopping run: every step from G0 to G6 PASS, ending `sw_gate: PASS (G0 to G6)`, `sw_gate exit status: 0`. Keep-going run: 26 gate-step PASS lines (29 with the FLASH, RAM and G3 detail sub-result lines), 0 FAIL, 0 MISSING, 1 SKIP line (emulation stub), `sw_gate: PASS (G0 to G6)`, exit 0. The two steps that failed in run 5: see the note after this table. G6 stable coverage is 100 percent lines and regions (cwht-core 17 of 17 lines, cwht-hal-mock 53 of 53). MSR-14: branches 4 of 4, lines 70 of 70, regions 70 of 70. `PASS G6 measurements` | `sw-gate-full.txt`, `sw-gate-keep-going.txt`, `unsafe-audit.txt` | Pass |
| 7 | Gate known-answer runs KA-0 to KA-8 | KA-0 exit 0; KA-1 to KA-7 exit 1 at the seeded gate; KA-8 exit 1 with the G3 comparison FAIL | All nine MATCH, with the same first FAIL lines as runs 3 and 5. KA-1 and KA-4: `FAIL G1 clippy host`. KA-2: `FAIL G1 cargo fmt --check`. KA-3: `FAIL G3 host tests run 1`. KA-5: `FAIL G0 rustc ...`. KA-6: `FAIL G1 clippy target`. KA-7: `FAIL G2 no compiler warning`. KA-8: exit 1 with `FAIL G3 identical result sets (JUnit file of run 1 or run 2 not written by this invocation)`, and the stale files are removed. In KA-8, `PASS G5 complexity` and `PASS G5 Miri`; its other FAIL lines are explained by D21. 0 `INTERIM` lines. The rustos clone is clean after all nine runs | `gate-known-answer.sh`, `gate-known-answer.txt` | Pass |
| 8 | Fresh rustos blinky (templates/pico2 of the pinned commit, path form), two builds | two identical SHA-256 | both `35062bec...ee92`; loadable sections identical to run 5 (section 3 gives the non-loadable difference) | `blinky-build.txt`, `rustos-blinky.elf`, `elf-diff.txt` | Pass |
| 9 | `picotool uf2 convert` and `picotool info -a` for both images | RP2350, ARM Secure, one image def block each | all four commands exit 0; both images RP2350, ARM Secure, one image def block; both UF2 files byte-identical to runs 1, 3 and 5 and to the files run 4 loaded | `uf2-info.txt`, `rustos-blinky.uf2`, `cwht-app.uf2` | Pass |
| 10 | Blink-rate prediction | windows computed | `.text` of both images is identical to run 5 (and so to run 3), so the run 2 prediction holds unchanged: 10 to 120 cycles in 60 s for the blinky, 3 to 45 for cwht-app | `blink-rate-prediction.txt` | Pass |
| 11 | Flash and observe the rustos blinky | load verified, reboot exit 0, 10 to 120 cycles in 60 s | **Not repeated in run 6; stands on run 4.** Run 4 step 11 loaded `rustos-blinky.uf2` `c45b5268...08d3`, "Verifying Flash ... OK", reboot exit 0, 60 to 63 cycles in 60 s, Pass. The run 6 UF2 is the same file byte for byte (`cmp` exit 0) | run 4 `step11-info.txt`, `step11-load.txt`, `step11-observation.txt`; `uf2-info.txt` | Pass (run 4) |
| 12 | Flash and observe cwht-app | load verified, reboot exit 0, 3 to 45 cycles in 60 s | **Not repeated in run 6; stands on run 4.** Run 4 step 12 loaded `cwht-app.uf2` `4e0bd133...3529`, verify OK, reboot exit 0, 18 cycles in 60 s, Pass. The run 6 UF2 is the same file byte for byte | run 4 `step12-load.txt`, `step12-observation.txt`; `uf2-info.txt` | Pass (run 4) |
| 13 | Record versions, commits, blob and hashes | recorded | this report and its front matter | this file | Pass |
| 14 | Stop rule | NCR on discrepancy | no discrepancy | none | n/a |

Step 6, the two steps that failed in run 5:

- **`G5 complexity` now passes.** The tool reports `COUNT .../cwht-app/src/main.rs:30 main CC 4 = analyzer 2 + 2 let ... else (CR-005)` and `ALLOWANCE CS-38 .../cwht-app/src/main.rs: 4 (2 CS-11 failure arm(s), 1 CS-19 halt loop(s), 1 CS-19 main loop(s); CR-001, CR-005)`. Its MSR-17 line reads `MSR-17 functions 52, max_cc 5, mean_cc 1.46, above_12 0, above_15 0 ... target_only_above_1 2`. The result is `complexity_gate: PASS (0 failure(s), 0 CS-19 report(s))`, then `PASS G5 complexity`.
- **`G5 Miri` now passes.** The command is `cargo +nightly-2026-08-24 miri test -p api --lib`; `api` runs 0 tests, `ok`, then `PASS G5 Miri (nightly, non-credit, MSR-08)`.

## 5. Analysis of results

- **Close-out item A (CR-005 amendment 1) in the repository gate.** The run 5 blocker B9 is closed. `cwht-app::main` has CC 4: analyzer 2, of which 1 is the CS-19 main `loop`, plus 2 `let ... else`. That equals its own CS-38 allowance: base 1, plus 2 CS-11 failure arms, plus 1 for the main loop. The file's printed allowance also counts the `safe_state_halt` halt loop (1 in this file: the panic handler at `main.rs:65` calls `safe_state_halt` and holds no bare `loop` of its own). The tool checks each function against its own items (07 revision A.7 CS-38; CR-005 section 12.2 item 2), so no allowance is pooled. `target_only_above_1 2` counts the two functions above CC 1 in target-only files: `main` and `safe_state_halt`, each within its own allowance. CS-17 passes: 52 functions, maximum CC 5, mean 1.46, none above 12 (MSR-17). The gate result equals the one TV-012 run 3 predicted at `0da559a`.
- **Close-out item B (G5 Miri scope) in the repository gate.** The run 5 blocker B11 is closed. The gate compiles only `api` under Miri, which builds and runs on the aarch64-apple-darwin host. `pico2` is no longer asked to compile for a Mach-O host. The result equals the item B re-validation (`docs/cm/tool-validation/evidence/sw-gate-miri-scope-2026-09-27.log.txt`, clean layout `PASS G5 Miri`). MSR-08 stays empty (0 tests): this is the run 5 recommendation 5 lien (INSP-016 X-8), due PDR, and not a gate failure.
- **Earlier closures hold.** CR-004 (B1, B2) still holds: `PASS G5 cargo deny (bans, licenses, sources)` and `PASS G5 unsafe audit` on the committed list. The unsafe audit shows 37 sites (block 16, fn 11, impl 1, extern 3, attr 6), 0 without SAFETY, and 37 unsigned, which is a note until CDR. Close-out item 2 (B10) holds: Miri runs with no prompt and no download. The F-14 invocation fix (B8) holds: the analyzer reads all three roots, 52 functions.
- **FW-B0 exit criterion.** `tools/sw_gate.sh` exits 0 in both modes on a clean export of the committed cwht `bb2485e` and rustos `2ec64c0`, with nothing installed or downloaded. This meets the 07 section 3.2 FW-B0 exit criterion.
- **Reproducibility.** Within the layout, two clean cwht-app builds and the gate builds give one SHA-256, and two blinky builds give one SHA-256. Across layouts, the loadable bytes and both UF2 files equal runs 1 to 5. The non-loadable differences come only from the build path, as in run 5 (section 3). G3 shows SWE-186 for the host tests: two runs with identical result sets.
- **Known-answer runs.** All nine match on the changed gate. The G0, G1, G2 warning and G3 decisions still discriminate. In KA-8, G5 complexity and G5 Miri now pass on the copy, which confirms that the two changes do not depend on the layout.

## 6. Data tables, plots and pictures

All data are text logs, scripts and images in `docs/vv/reports/TC-SW-TOOL-001-r6/`, listed with SHA-256 in the front matter. Steps 1 to 10 produce no plot or photograph. The scripts:

- `run6.sh` and `gate-known-answer.sh` are the exact procedures run. They are the run 5 scripts with the run 6 paths, the ELF and UF2 comparisons against run 5 added, and the ELF and download-check blocks added to `run6.sh`.
- `elf-diff.sh` is the D22 comparison.
- `rustup-guard.sh` is the D13 shim.

The data files:

- `elf-diff.txt` is the section-by-section ELF comparison of section 3.
- `layout-after.txt` is the layout state after the run (D20).
- `download-check.txt` is the D13 check.

Gate result summary (`--keep-going`). Sub-result lines such as FLASH, RAM, the G3 comparison detail, COUNT, ALLOWANCE and MSR lines are not counted. The G6 emulation SKIP line is counted once as SKIP, and its `PASS G6 emulation` step line as PASS.

| Gate | PASS | FAIL | MISSING | SKIP |
|---|---|---|---|---|
| G0 | 1 | 0 | 0 | 0 |
| G1 | 3 | 0 | 0 | 0 |
| G2 | 5 (build; no compiler warning; link map; no allocator symbol; image dependency set) | 0 | 0 | 0 |
| G3 | 3 (host tests run 1; run 2; identical result sets) | 0 | 0 | 0 |
| G4 | 1 | 0 | 0 | 0 |
| G5 | 9 (cargo audit; cargo deny; deny advisories; geiger 3; unsafe audit; complexity; Miri) | 0 | 0 | 0 |
| G6 | 4 (stable coverage; branch and condition coverage; emulation stub; measurements) | 0 | 0 | 1 (emulation line) |
| Total | 26 gate steps (29 PASS lines with FLASH, RAM and the G3 detail line) | 0 | 0 | 1 |

Run 5 counted 24 gate-step PASS lines with 2 FAIL. Run 6 has 26 gate-step PASS lines and 0 FAIL: run 5's 24 plus the two former FAILs.

Image identity:

| Image | Run 6 SHA-256 | Run 5 | Run 3 | Run 1 file loaded in run 4 | Byte-identical |
|---|---|---|---|---|---|
| `cwht-app.uf2` | `4e0bd133...3529` | `4e0bd133...3529` | `4e0bd133...3529` | `4e0bd133...3529` | yes (`cmp` exit 0, three comparisons) |
| `rustos-blinky.uf2` | `c45b5268...08d3` | `c45b5268...08d3` | `c45b5268...08d3` | `c45b5268...08d3` | yes (`cmp` exit 0, three comparisons) |
| `cwht-app.elf` | `14e43149...f6a9` | `104f40fa...4b48` | `388d1d16...a5bf` | n/a | no: loadable sections identical to run 5; debug and symbol-name sections differ by build path |
| `rustos-blinky.elf` | `35062bec...ee92` | `e826dbf0...fb61` | `3c0ac074...bd08` | n/a | no: loadable sections identical to run 5; `.strtab` differs by build path |

## 7. Non-conformances and discrepancies

| NCR | Severity | Step | Summary | Disposition | Retest planned |
|---|---|---|---|---|---|
| None | | | | | |

Status of the blocking items of runs 3 to 5:

| # | Gate line or item | Run 6 status | Closes on | Owner |
|---|---|---|---|---|
| B1, B2 | `G5 cargo deny (bans, licenses, sources)`, `G5 unsafe audit` | Closed (run 5); PASS again | closed | none |
| B7 | steps 11 and 12 | Closed by run 4; the run 6 UF2 files are byte-identical, so run 4 stands | closed | none |
| B8 | `G5 complexity` (invocation) | Closed (run 5); the analyzer reads all three roots (52 functions) | closed | none |
| B9 | `G5 complexity` (convention) | **Closed**: `PASS G5 complexity` in the repository gate on the CR-005 amendment 1 tool (close-out item A; TV-012 run 3) | closed | none |
| B10 | `G5 Miri` (component) | Closed (run 5); no prompt, no download | closed | none |
| B11 | `G5 Miri` (scope) | **Closed**: `PASS G5 Miri` with `-p api --lib` (close-out item B). The FW-B1 lien that returns `pico2` to Miri once it is host-compilable stays with the owner as rustos maintainer and a pin CR, as the gate comment states | closed for the gate; FW-B1 lien open | Robin (rustos `cfg_attr`), then the `tools/sw_gate.sh` maintainer |

## 8. Status of enabling equipment after the run

- cwht repository: unchanged by the run. The layout was a `git archive` in the scratch area, deleted after the run. This filing adds only this report and its artifact directory.
- rustos: the owner's repository is unchanged. `master` is at `2ec64c0` before and after, and the working tree was not read or written (D20). The scratch clone and export were deleted.
- Toolchains: as installed under decision 109 and close-out items 2, 3 and 12. Nothing was installed, updated or downloaded by the run (D13, `download-check.txt`).
- Board `pico2-devboard-1`: not used. It still holds `kat-target.uf2` from run 4 OA-2.

## 9. Conclusions and recommendations

Verdict: Pass. On the committed cwht `bb2485e` and the pinned rustos `2ec64c0`, `tools/sw_gate.sh` exits 0 in both modes: 26 gate steps pass, 0 FAIL, 0 MISSING, and 1 SKIP line (the emulation stub, by design until the PDR emulator ADR). The two run 5 blockers are closed by the owner's close-out rulings: B9 by item A (CR-005 amendment 1) and B11 by item B (G5 Miri on host-compilable crates). The known-answer runs KA-0 to KA-8 all match. Both UF2 images are byte-identical to the images the owner loaded and observed in run 4, so steps 11 and 12 stand on run 4. The FW-B0 exit criterion (gate exit 0) is met. No requirement status changes (dev-board case, `credit: false`).

Recommendations:

1. INSP-016 reviewer: re-issue the record on this run. The F-01 criterion (FW-B0 gate exit 0) is now shown; the reviewer, not the author, changes the record.
2. Baseline record owner: update precondition P6 of `docs/reviews/SRR/baseline-record.md` and `docs/reviews/SRR/baseline-check.md` with this run. That change is out of this conductor's scope and is listed as a cross item.
3. Carried liens due PDR, not fixed now (charter section 4 item 3):
   - INSP-016 F-16, run 5 recommendation 4: G0 on a `git archive` export needs the clone of D20.
   - INSP-016 X-8, run 5 recommendation 5: MSR-08 is empty while `api` has 0 unit tests.
   - The FW-B1 lien of item B: `pico2` host-compilability through `cfg_attr`.
   - D8: the stale comment in `cwht-app/src/main.rs`.

Deferrals FD-1 and FD-2 of run 1 stand unchanged.

## 10. As-run procedure

`run6.sh` and `gate-known-answer.sh` ran steps 1 to 10 and 13 as written in `docs/test_cases/sw-tool/test_cases.json` (blob `fee1e724`, unchanged), with deviations D1 to D22 of section 2. Step 5 ran as gate G1 within step 6. Steps 11 and 12 are not repeated; they cite run 4 on byte-identical images (section 4).

## 11. Answers to INSP-016 findings (author response for the reviewer's next iteration)

The reviewer, not the author, changes the record (`docs/reviews/SRR/checklists/fw-b0-toolchain-proof.md`).

| Finding | Severity | Author response | What closes it |
|---|---|---|---|
| finding-1 (F-01) | Major | Run 6 on the committed `bb2485e` and the pinned `2ec64c0`: `tools/sw_gate.sh` exits 0 in both modes, with 0 FAIL and 0 MISSING. B9 and B11 were closed by close-out items A and B, the rest by run 5. KA-0 to KA-8 MATCH. Steps 11 and 12 stand on run 4 with byte-identical UF2 files | reviewer verification of this run |
| finding-15 (F-15) | Minor (lien) | The gate's Miri command is narrowed to `-p api --lib` (close-out item B, `495a0c3`). In the repository gate, `PASS G5 Miri`. `pico2` returns to the command at FW-B1 through the owner's rustos `cfg_attr` change and a pin CR | reviewer verification; the FW-B1 part stays a lien |

## 12. Authentication and authorization

- Results authenticated by (conductor): claude, 2026-09-27
- Witnessed by: owner, not applicable to run 6. No step was owner-performed; steps 11 and 12 stand on run 4, witnessed 2026-09-26 19:17 to 19:23 CDT, on byte-identical images.
- Authorization of acceptability (owner): pending
