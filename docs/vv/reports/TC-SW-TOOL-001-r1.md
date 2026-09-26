---
test_case: TC-SW-TOOL-001
run: 1
requirement_ids: [REQ-SYS-127, REQ-SYS-128, REQ-SYS-133]
validates: []
verification_method: Demonstration
type: Bench
credit: false
result: Blocked
date: 2026-09-25
conductor: claude
witness: owner
article: pico2-devboard-1
firmware_version: "n/a"
source_commit: "n/a"
firmware_elf_sha256: "n/a"
requirements_baseline: "none (pre-SRR)"
procedure_commit: "28e49e6"
procedure_blob: "04d08adfffce810b6933f42d242ef124f88f4162"
toolchain_lock: "tools/toolchain.lock.md@4e3f891"
harness_versions: "n/a"
instruments:
  - "Host USB port; owner's Mac (macOS 26.6.2, arm64) with picotool 2.3.0; USB 5 V supply and BOOTSEL load path only; tools/toolchain.lock.md picotool row; no calibration applicable"
  - "Stopwatch; phone clock; 60 s count window; not a credited instrument (credit false); no calibration applicable"
ncr_ids: []
artifacts:
  - "docs/vv/reports/TC-SW-TOOL-001-r1/versions.txt sha256=9e336a8c8e97dce906f11acf818319b6379feb95529f50ddf7a06ac144e06000"
  - "docs/vv/reports/TC-SW-TOOL-001-r1/host-build-test.txt sha256=85676d5ef6aa6465d445b8fd51477020c90060d4959d6f5c5ba27a636b57991e"
  - "docs/vv/reports/TC-SW-TOOL-001-r1/sw-gate-full.txt sha256=4a9f0c79f1992f937256e4381a58a9562090cbaed908070037aab7694951f90f"
  - "docs/vv/reports/TC-SW-TOOL-001-r1/sw-gate-keep-going.txt sha256=a10d282bfd3e19b1da967150b55a66ca5c34d82df34167946962f6dbdac5e1ec"
  - "docs/vv/reports/TC-SW-TOOL-001-r1/gate-known-answer.sh sha256=b5ce7a1f9a3d7a0953e7172cdd33e8bfd7e0ef8574b5619121d39695bdf22e0f"
  - "docs/vv/reports/TC-SW-TOOL-001-r1/gate-known-answer.txt sha256=7be51befa5c65ae4e088e78e2c26290c838706102b441d9c6beac98b81b0d57c"
  - "docs/vv/reports/TC-SW-TOOL-001-r1/blinky-build.txt sha256=5100ef49b7b7bb5ff19a9246e206a5e91fd77538655caad8d032220c3cc01fbb"
  - "docs/vv/reports/TC-SW-TOOL-001-r1/rustos-blinky.elf sha256=ef16271deaaf37714cca58bc3cb789f4c94f8a9f98a1c4b343b676e5716ba8c1"
  - "docs/vv/reports/TC-SW-TOOL-001-r1/rustos-blinky.uf2 sha256=c45b526837c0831206763eb3134a8e71c854059ff7442c19e51f39edf03308d3"
  - "docs/vv/reports/TC-SW-TOOL-001-r1/cwht-app.elf sha256=3992e5d8ba616271c8df2a0acd00e9c1992d7b1a5459c73f398778f7cf980ec1"
  - "docs/vv/reports/TC-SW-TOOL-001-r1/cwht-app.uf2 sha256=4e0bd133a10b6e29f72f00023ec407cd1885b8550a685b881c7be213462b3529"
  - "docs/vv/reports/TC-SW-TOOL-001-r1/cwht-app.map sha256=e9ba4361ad2d2493acc88a49642a296263ae6b36edb1da6903b5c0e0f8ee1d1a"
  - "docs/vv/reports/TC-SW-TOOL-001-r1/uf2-info.txt sha256=b6cabe75574d27a9018c57d7c09fff4afd1a8352e788f15b7553f2fb53985626"
  - "docs/vv/reports/TC-SW-TOOL-001-r1/blink-rate-prediction.txt sha256=27162483f3c42eb8a0a21b7adef4a2bf8008e85dc67a892c6edef1cfc797f1e6"
mop_values: []
---

# Verification report: TC-SW-TOOL-001 run 1

**Status of this run: Blocked.** Steps 1 to 10 and 13 were executed by Claude on 2026-09-25 and are recorded below. Steps 11 and 12 (flash and observe on the bare Pico 2) are **Pending owner**. The gate of step 6 does not yet exit 0 because of prerequisites outside the firmware workspace (section 7). This is a dev-board case: `credit: false`, credit row `SUPPORT`; it changes the status of no requirement (docs/process/04-verification-and-validation.md section 4, rule 7.3.12).

## 1. Objectives and degree to which they were met

Case title: FW-B0 toolchain proof: firmware workspace host build and test, RP2350 target build, lint gate, `sw_gate.sh` end to end, and rustos blinky and cwht-app flashed on a bare Pico 2 (dev-board case, supporting evidence). Objective: the FW-B0 exit criterion of docs/process/07-software-engineering-plan.md section 3.2 and the SRR toolchain-proof product of 07 section 3.1 (SRR package section 2 item H12).

| Requirement | Shall statement | Acceptance criterion (this case) | Measured or observed | Met? |
|---|---|---|---|---|
| REQ-SYS-127 | The transceiver shall run firmware written in Rust on the rustos operating system. | Rust workspace builds for `thumbv8m.main-none-eabihf` against rustos by path; image runs on a Pico 2 | `cwht-app` release build exit 0, 1608 B flash, 8200 B RAM; dependency set `cwht-app`, `cwht-core`, `api`, `pico2` only; on-board run pending owner (step 12) | Partially (supporting only; closes by Inspection, row I) |
| REQ-SYS-128 | The transceiver shall run application firmware that builds and executes unmodified on a macOS or Linux host against the rustos api traits. | `cwht-core` and `cwht-hal-mock` build and test on the host; the same `cwht-core` links into the target image | Host build exit 0; 10 of 10 tests pass, twice, identical result sets; 100 percent line and region coverage of the two host crates (developer evidence: the cargo-llvm-cov TV that the `tools/toolchain.lock.md` cargo-llvm-cov row requires before FW-B0 coverage is cited is pending, so this figure carries no validated-tool standing); the same `cwht-core` source is linked into `cwht-app` | Met for this case (supporting only; closes by Inspection, row I) |
| REQ-SYS-133 | The transceiver shall accept a firmware image through its micro-USB receptacle with the cells removed. | `picotool load -v` of both UF2 images over the Pico 2 micro-USB succeeds and the images run | UF2 images built and inspected (`picotool info -a`: RP2350, ARM Secure, one image def block); load pending owner (steps 11 and 12) | Not yet (supporting only; closes by Demonstration on the delivered unit, row D) |

## 2. Description of the activity and deviations

Claude created the firmware workspace `firmware/` (crates `cwht-app`, `cwht-core`, `cwht-hal-mock`, placeholder `firmware/emu/`, and the build and quality configuration of 07 section 1.2 and Annex B), wrote `tools/sw_gate.sh`, ran the host build and tests, the target build, the lint and format checks, the gate in its stopping and keep-going forms, seven seeded known-answer runs of the gate, two fresh builds of the rustos blinky, the UF2 conversions and the blink-rate prediction. The case is Draft (not yet reviewed under 04 section 8.3); this run is a developer-evidence run ahead of the review and carries no credit.

Deviations (none affects credit, because the run carries none):

- D1. The pinned toolchain `1.98.0-aarch64-apple-darwin` of `firmware/rust-toolchain.toml` (CS-03; lock section 1.3) is not installed, and installing it is a network download that needs the owner's approval. Every cargo command ran on `stable-aarch64-apple-darwin` with `RUSTUP_TOOLCHAIN=stable` and `RUSTUP_AUTO_INSTALL=0`, after the gate confirmed that its `rustc --version` equals the lock rustc row exactly (`rustc 1.98.0 (88d9e12ae 2026-08-18)`). Same compiler build; the pinned install is an owner action (section 9).
- D2. The rustos README build command (`cargo build --release` at the rustos root, output `target/.../release/demo`) no longer applies: rustos commit 8502402 moved the demo to `templates/pico2`. The blinky was built from the template, copied to a scratch directory, with its two git dependency lines replaced by the local path form that `templates/README.md` gives, so that nothing is downloaded (diff in `blinky-build.txt`).
- D3. The 07 Annex C host commands `cargo clippy --workspace` and `cargo nextest run --workspace` exclude `cwht-app` in the gate, because `cwht-app` is target-only (`#![no_main]`, and rustos `pico2` contains Arm assembly); the target clippy covers `cwht-app`. 07 Annex C marks its commands as abridged.
- D4. `tools/measurements.py` does not exist, so gate G2 (memory report against the TPM-010 and TPM-011 red lines) and G3 (run comparison, SWE-186) use interim inline checks in `tools/sw_gate.sh`, printed as `INTERIM` lines; the gate calls the script once it exists.
- D5. Gate G4 runs `tools/traceability.py` with `--output firmware/target/sw-gate/traceability-report.md` so that the gate never overwrites `docs/vv/traceability-report.md`.
- D6. 07 section 3.2 row FW-B0 asks for a blinky "on the cwht pin map". The pin map is `docs/icd/ICD-CTL-SW.md`, a PDR product (07 section 3.1), which does not exist yet, so `cwht-app` drives the Pico 2 on-board LED (GPIO25, `board.pins.led` of rustos `pico2`). The toolchain proof (build, link, load and run of a cwht image composed from `cwht-core`) is unaffected; the blinky on the cwht pin map is rerun once ICD-CTL-SW exists (INSP-016 finding-10).
- D7. `tools/sw_gate.sh` adds a step G0 (toolchain identity: rustc against the lock rustc row, rustos commit against the lock rustos row, rustos code directories clean) that 07 section 8.4 and Annex C do not list, and `--quick` runs G0 to G3 where 07 section 8.4 says G1 to G3. G0 exists because every later result is meaningless on a different compiler or rustos commit; the 07 section 8.4 and Annex C update (G0, the `--quick` scope, exit status 3 for MISSING) is raised to the 07 author (INSP-016 finding-8).
- D8. Code deviation from 07 CS-11 and CS-38. `cwht-app/src/main.rs` holds a second decision in target-only code: the `let Ok(mut led) = gpio.output_from_handle(..) else { safe_state_halt() }` arm, because the rustos driver constructor returns `Result<_, GpioError>` (rustos `firmware/pico2/src/gpio/gpio.rs`). CS-11 permits only the board `take()` `None` arm and CS-38 only the `take()` match, so the image as built carries cyclomatic complexity 3 in `main` against the CS-38 limit. The arm calls `safe_state_halt()`, the same action CS-11 prescribes for the `take()` failure. A CR amending CS-11 and CS-38 to admit driver-construction failure arms that call `safe_state_halt()` is raised for owner disposition before FW-B1; until it is dispositioned, this deviation and the comment at `main.rs` that cites it are the record (INSP-016 finding-2).

## 3. Configuration under test and differences from the operational configuration

- Article and serial: `pico2-devboard-1`, a bare Raspberry Pi Pico 2 (RP2350) with nothing attached but its micro-USB cable; the owner writes 1 on the board if it is unmarked (step 11). Not yet connected for this run.
- Firmware: no release tag exists (FW-B0 development build), so `firmware_version`, `source_commit` and `firmware_elf_sha256` are "n/a". Images: `cwht-app.elf` built by `cargo build -p cwht-app --release --target thumbv8m.main-none-eabihf` from the `firmware/` working tree (not yet committed) on cwht commit 28e49e6; `rustos-blinky.elf` built from rustos `templates/pico2` at rustos `c54d35aa8e7f9ad30f6508bca458a59c1fc009db` (the lock rustos row; `api/` and `firmware/` clean). Hashes in the front matter `artifacts` list and in `uf2-info.txt`.
- Test harness and emulator: "n/a" for a Bench case; the host steps used cargo 1.98.0, cargo-nextest 0.9.146 and cargo-llvm-cov 0.9.1 (`versions.txt`), all present in `tools/toolchain.lock.md` at 4e3f891. No emulator.
- Requirements baseline, procedure commit and procedure blob: no baseline yet (pre-SRR). The case file `docs/test_cases/sw-tool/test_cases.json` is not yet committed; `procedure_commit` names the HEAD on which it was written and `procedure_blob` is `git hash-object` of the file as run, which equals the blob it will have when committed unchanged.
- Differences from operational configuration: bare Pico 2 development board instead of the radio board; USB power from the host, no cells; no RF, keying, audio or display hardware; the image blinks the on-board LED (GPIO25) only, not a pin of the cwht pin map (deviation D6); the host crates run against `cwht-hal-mock`.
- Instruments: host USB port and picotool for the load; a phone stopwatch for the 60 s count; none credited.
- Tools: rustc 1.98.0 (88d9e12ae 2026-08-18), cargo 1.98.0 (797e8a9bc 2026-08-05), rustup 1.29.0, clippy and rustfmt of the stable toolchain, cargo-nextest 0.9.146, cargo-llvm-cov 0.9.1, cargo-deny 0.20.2, cargo-geiger 0.13.0, cargo-audit 0.22.2 (not run: no advisory database), cargo-binutils 0.4.0 (`rust-nm`, `rust-size`, `rust-objdump`), picotool 2.3.0, Python 3 of `.venv`; each is a row of `tools/toolchain.lock.md`; none has a TV record, so all output is developer evidence (CM plan section 9.1).
- Environment: indoor, room temperature; for steps 11 and 12 the LED must be plainly visible.

## 4. Results of each step

| Step | Procedure text (as run) | Expected | Observation | Artifact | Pass/Fail |
|---|---|---|---|---|---|
| 1 | Record configuration; rustos commit and rustc against the lock | Lock rows match; rustos code clean | rustos HEAD `c54d35a...` equals the lock row; `api/`, `firmware/` clean; rustc equals the lock row; pinned 1.98.0 absent (D1); `nightly-2026-08-24` has no `miri` or `llvm-tools`; no RustSec database | `versions.txt` | Pass |
| 2 | `cargo build` on the host | exit 0 | exit 0 (`cwht-core`, `cwht-hal-mock`, `api`) | `host-build-test.txt` | Pass |
| 3 | `cargo test` on the host | all pass, at least 10 | 10 passed, 0 failed (5 `cwht-core` heartbeat, 5 `cwht-hal-mock` gpio) | `host-build-test.txt` | Pass |
| 4 | `cargo build -p cwht-app --release --target thumbv8m.main-none-eabihf` | exit 0; map written | exit 0; FLASH 1608 B of 4 MB (0.04 %), RAM 8200 B of 520 KB (1.54 %); `cwht-app.map` written | `sw-gate-full.txt`, `cwht-app.map` | Pass |
| 5 | fmt check, host clippy, target clippy with `-D warnings` and the Annex B lint set | no diff, no warning | no diff; no warning on host or target (gate G1) | `sw-gate-full.txt` | Pass |
| 6 | `tools/sw_gate.sh` and `tools/sw_gate.sh --keep-going` | exit 0 (FW-B0 exit criterion) | G0 to G3 PASS (11 steps). Stopping run: FAIL at G4, exit 1. Keep-going run: G4 FAIL, G5 cargo deny FAIL, three geiger steps PASS, G6 stable coverage PASS (100.00 % regions, functions and lines of `cwht-core` and `cwht-hal-mock`; developer evidence, cargo-llvm-cov TV pending), 9 MISSING prerequisites; exit 1 (section 7) | `sw-gate-full.txt`, `sw-gate-keep-going.txt` | Blocked |
| 7 | Gate known-answer runs KA-0 to KA-6 on seeded copies | KA-0 exit 0; KA-1 to KA-6 exit 1 at the seeded gate | All seven MATCH: KA-0 exit 0; KA-1 and KA-4 FAIL G1 clippy host; KA-2 FAIL G1 fmt; KA-3 FAIL G3 run 1; KA-5 FAIL G0; KA-6 FAIL G1 clippy target | `gate-known-answer.sh`, `gate-known-answer.txt` | Pass |
| 8 | Fresh rustos blinky, two builds; compare with rustos root `blinky.elf` | two identical SHA-256 | both `ef16271d...ba8c1`; the rustos root `blinky.elf` (`c90f5bbe...c596`) differs: it is untracked (ignored by `*.elf`), dated 2026-08-30 07:29, before the last `pico2/src/lib.rs` change (c54d35a, 11:16), so the README statement that the committed file matches a fresh build is out of date (section 9) | `blinky-build.txt`, `rustos-blinky.elf` | Pass |
| 9 | `picotool uf2 convert` and `picotool info -a` for both images | RP2350, ARM Secure, one image def block each | both exit 0; both report target chip RP2350, image type ARM Secure, one image def block at 0x10000110, extra security not enabled | `uf2-info.txt`, `rustos-blinky.uf2`, `cwht-app.uf2` | Pass |
| 10 | Blink-rate prediction from the disassembly | windows computed | blinky: 66 instructions per 64 spins, 13.4 to 114 LED cycles in 60 s (nominal 63); cwht-app: 3 instructions per spin, 4.6 to 39 cycles in 60 s (nominal 16.5); acceptance windows 10 to 120 and 3 to 45 | `blink-rate-prediction.txt` | Pass |
| 11 | Flash and observe the rustos blinky (owner steps below) | load verified, reboot exit 0, 10 to 120 cycles in 60 s | **Pending owner** | `flash-rustos-blinky.txt` (to be written) | Pending owner |
| 12 | Flash and observe cwht-app (owner steps below) | load verified, reboot exit 0, 3 to 45 cycles in 60 s | **Pending owner** | `flash-cwht-app.txt` (to be written) | Pending owner |
| 13 | Record versions, commits, blob and hashes | recorded | this report and its front matter | this file | Pass |
| 14 | Stop rule | NCR on discrepancy | no product discrepancy in the cwht workspace; the rustos and prerequisite items of section 7 are proposed for owner disposition, not opened as NCRs by this run | none | n/a |

### Owner steps for 11 and 12 (Claude runs every command; the owner handles the board and counts)

1. Take the bare Pico 2 and its micro-USB cable. If the board has no number on it, write 1 on it (the article is `pico2-devboard-1`).
2. Hold the white **BOOTSEL** button, plug the cable into the Mac, then release BOOTSEL. The board appears as a USB drive named RP2350; ignore the drive (do not copy anything onto it).
3. Tell Claude the board is in BOOTSEL mode. Claude runs, from `/Users/robinonsay/rust/cwht`:
   ```
   picotool info -d
   picotool load -v docs/vv/reports/TC-SW-TOOL-001-r1/rustos-blinky.uf2
   picotool reboot
   ```
   Expected: `info -d` lists one RP2350 device in BOOTSEL mode; `load -v` ends with the verify step passing; `reboot` exits 0 and the drive disappears.
4. Watch the green LED next to the USB connector. Start a stopwatch and count each time the LED turns on, for 60 s. Tell Claude the count and whether on and off look equally long. Pass window: 10 to 120 (predicted about 63).
5. Unplug the cable. Hold BOOTSEL, plug the cable in again, release BOOTSEL, and tell Claude.
6. Claude runs:
   ```
   picotool info -d
   picotool load -v docs/vv/reports/TC-SW-TOOL-001-r1/cwht-app.uf2
   picotool reboot
   ```
7. Count LED turn-ons for 60 s as in item 4. Pass window: 3 to 45 (predicted about 16; slower than the blinky because its delay loop is not unrolled, section 5).
8. Unplug the cable. Claude writes `flash-rustos-blinky.txt` and `flash-cwht-app.txt` with the command output and the counts, adds them to the artifacts list and files run 2 of this case (a filed report is not edited to change its result).

## 5. Analysis of results

- Gate coverage of the FW-B0 criterion. The criterion is `tools/sw_gate.sh` exiting 0. The firmware workspace itself passes every step that has its tool: G0 to G3, the geiger forbid checks and stable coverage at 100 percent (developer evidence, cargo-llvm-cov TV pending). The remaining failures and missing items are outside the workspace (section 7).
- Known-answer runs. Each seeded defect is caught at the intended gate with exit 1, and the unmodified copy exits 0, so the gate's G0, G1 and G3 decisions are shown to discriminate. KA-4 shows three independent detections of one seed: the `forbid(unsafe_code)` lint, the `disallowed-methods` entry for `core::mem::transmute` (CS-10) and clippy's transmute lint.
- Blink rates. The two images use the same 5 000 000 spin count, but LLVM unrolls the blinky loop 64 times (66 instructions per 64 spins) and leaves the `cwht-app` loop at `opt-level = "s"` rolled (3 instructions per spin), so the cwht image is predicted about 3.8 times slower. The absolute rate is uncalibrated because no clock is configured (ring oscillator 4.6 MHz to 19.6 MHz, RP2350 datasheet section 8.3.1 as extracted in rustos `docs/extracted/rp2350-datasheet.md`), and the cycles per instruction are an estimate (1 to 2), since the Cortex-M33 timing tables are not in the project corpus. The windows are therefore wide; they detect a dead image (no blink), a hang (LED fixed) or an image running from a wrong clock by a large factor, not timing accuracy.
- Reproducibility. Two clean builds of the blinky gave identical ELF SHA-256 (`blinky-build.txt`). Run 1 recorded one cwht-app build only, so it makes no rebuild-identity claim for cwht-app; the independent review rebuilt the cwht-app ELF in a clean target directory and obtained the SHA-256 of `cwht-app.elf` (INSP-016, `docs/reviews/SRR/checklists/fw-b0-toolchain-proof.md`, reviewer run 6). Run 2 records a cwht-app rebuild with both hashes in its own artifact.

## 6. Data tables, plots and pictures

All data are text logs and images in `docs/vv/reports/TC-SW-TOOL-001-r1/`, listed with SHA-256 in the front matter. No plot or photograph is produced by steps 1 to 10; steps 11 and 12 record counts in text.

## 7. Non-conformances and discrepancies

| NCR | Severity | Step | Summary | Disposition | Retest planned |
|---|---|---|---|---|---|
| None | | | | | |

Items that block the gate, proposed for owner disposition (none is a defect of the cwht workspace):

- G4 `tools/traceability.py` exits 1 on requirements being authored concurrently by other agents (REQ-SW-KEYER-001 to 033, REQ-TX-001 to 016, REQ-SYS-180 to 182 without cases). No violation names a file of this case.
- G5 `cargo deny check bans licenses sources` fails on the rustos crates: `api` and `pico2` are unlicensed, and `pico2`'s path dependency on `api` counts as a wildcard because neither manifest says `publish = false`. A probe on a scratch copy of the two rustos manifests with `publish = false` added gave `bans ok, licenses ok, sources ok`. Proposed rustos work item in section 9.
- G5 and G6 MISSING (owner-approved downloads): RustSec advisory database for `cargo audit` and `cargo deny advisories`; `rust-code-analysis-cli`; `miri` and `llvm-tools` on `nightly-2026-08-24`; and, for reproducibility, the pinned `1.98.0` toolchain (D1).
- G5 and G6 MISSING (scripts not yet written): `tools/unsafe_audit.py`, `tools/complexity_gate.py`, `tools/emu_run.sh` (the SKIP-line stub of 07 section 1.2), `tools/measurements.py`.

## 8. Status of enabling equipment after the run

No change. The rustos checkout was read only: `git status` of `api/` and `firmware/` is clean after the run; the blinky was built in a scratch copy.

## 9. Conclusions and recommendations

Verdict: Blocked. The firmware workspace builds and tests on the host, builds for the RP2350 target against rustos by path, is clippy- and format-clean under the 07 Annex B lint set, and meets 100 percent line and region coverage on its host crates (developer evidence: the cargo-llvm-cov TV that the `tools/toolchain.lock.md` cargo-llvm-cov row requires before FW-B0 coverage is cited is pending, so this figure carries no validated-tool standing); the gate runs end to end and its G0, G1 and G3 decisions are shown by seven known-answer runs. The FW-B0 exit criterion (gate exit 0) is not met until the section 7 items close, and the flash-and-observe steps await the owner. No requirement status changes (dev-board case, `credit: false`).

Recommendations:

1. Owner: approve the downloads of section 7 (pinned toolchain `rustup toolchain install 1.98.0 --profile minimal --component clippy,rustfmt,llvm-tools --target thumbv8m.main-none-eabihf`; `rustup toolchain install nightly-2026-08-24 --component miri --component llvm-tools` (07 CS-03); `cargo install rust-code-analysis-cli --locked`; the RustSec database by one `cargo audit` run without `--no-fetch` and one `cargo deny fetch`), then Claude records them in `tools/toolchain.lock.md` as Log changes.
2. Owner: perform steps 11 and 12 (section 4, owner steps); Claude files run 2.
3. rustos work item (owner, rustos is read only for cwht agents): add `publish = false` and a `license` field to `api/Cargo.toml` and `firmware/pico2/Cargo.toml`; give `entry!` a `#[doc(hidden)]` on the generated function so that application crates with `missing_docs` need no wrapper module; update the README Building and Flashing sections for the template layout and regenerate or remove the stale root `blinky.elf` and `blinky.uf2`.
4. Software lead: write `tools/emu_run.sh`, `tools/unsafe_audit.py`, `tools/complexity_gate.py` and `tools/measurements.py` (07 section 1.2), then re-run the gate.
5. Process: the CR of deviation D8 (CS-11 and CS-38 to admit driver-construction failure arms that call `safe_state_halt()`); the same CR states where the panic handler lives, because CS-12 places it in `pico2` while rustos leaves it to the application.
6. Independence (INSP-016 finding-4): `cwht-core/tests/heartbeat.rs` and `cwht-hal-mock/tests/gpio.rs` were written by the author of the code they test (charter section 2, section 11 rule 4). They verify no requirement. Either an independent test-author invocation reviews or replaces them before FW-B1 closes, or 07 section 3.2 states that FW-B0 toolchain-proof tests are exempt; the choice is the owner's.

Deferrals recorded by this report (each closes at the gate named):

| Id | Item deferred | Rule | Closes at | Source |
|---|---|---|---|---|
| FD-1 | Panic handler content: safe-state register writes, panic marker in the persistent event log, watchdog reset request. The FW-B0 handler halts only, because FW-B0 has no safe-state outputs and no event log. | 07 CS-12 | FW-B1 (07 section 3.2), with the safe-state manager of 07 section 14 | `cwht-app/src/main.rs` panic handler doc comment; INSP-016 finding-3 |
| FD-2 | Blinky on the cwht pin map | 07 section 3.2 row FW-B0 | rerun after `docs/icd/ICD-CTL-SW.md` exists (PDR) | deviation D6 |

## 10. As-run procedure

Steps 1 to 10 and 13 as written in `docs/test_cases/sw-tool/test_cases.json` (blob 04d08adf), with deviations D1 to D8 of section 2. Steps 11 and 12 not yet run. Step 5 was run as part of step 6 (gate G1) and separately during development; the recorded evidence is the gate log.

Changes after run 1 (applied from the independent review INSP-016; they do not alter the run 1 results above, which stand as recorded against the files as run: gate `tools/sw_gate.sh` blob `d74436ab`, case blob `04d08adf`, and the artifacts of the front matter):

- `tools/sw_gate.sh`: G3 removes both JUnit copies before the runs and fails the comparison when either is absent (finding-6); G2 build, link-map, `rust-nm` and `cargo tree` failures are counted FAIL steps instead of stopping the script, the ELF and map steps run only after a successful build in the same invocation, and the header states that only setup and G0 failures stop the script (finding-7); the header records the G0 and `--quick` scope of deviation D7 (finding-8); G2 takes flash and RAM use from the link map and the rustos `pico2` `link.ld` MEMORY regions and fails on any compiler or linker warning (finding-12).
- `firmware/.cargo/config.toml`: the linker argument `--print-memory-usage` is removed, so a target build no longer emits the rustc warning `linker_messages` (finding-12).
- `firmware/cwht-app/src/main.rs` and `firmware/cwht-hal-mock/src/gpio.rs`: comments only (findings 2, 3 and 5). The changed comment lines move source line numbers, so the next cwht-app ELF differs from `cwht-app.elf` of run 1 in its debug information; run 2 rebuilds and records the image it loads.
- `docs/test_cases/sw-tool/test_cases.json`: step 4 takes the memory figures from gate G2; step 6 describes `--keep-going` as revised; step 7 and the acceptance criteria add KA-7 (seeded build warning, first FAIL at G2 no compiler warning) and KA-8 (stale JUnit files with a failing test, G3 comparison FAIL). Run 2 runs the revised case.

## 11. Authentication and authorization

- Results authenticated by (conductor): claude, 2026-09-25
- Witnessed by: owner, pending (steps 11 and 12)
- Authorization of acceptability (owner): pending
