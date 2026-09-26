---
test_case: TC-SW-TOOL-001
run: 2
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
source_commit: "400e59d34835aed359049df9dad1329dfd372380"
firmware_elf_sha256: "622cbe2a6b8e5d2a12ac5a94306a49dd7ecde1f31c5eb937e3e85b6066b9802f"
requirements_baseline: "none (pre-SRR)"
procedure_commit: "400e59d"
procedure_blob: "fee1e7246af59d5e8a43ed1b9cdf483854053fdc"
toolchain_lock: "tools/toolchain.lock.md working-tree blob 77262c791d971190309ff16c05c9fa8b52139447 on 400e59d (uncommitted edits of 2026-09-26 by the tool maintainer)"
harness_versions: "n/a"
instruments:
  - "Host USB port; owner's Mac (macOS 26.6.2, arm64) with picotool 2.3.0; USB 5 V supply and BOOTSEL load path only; tools/toolchain.lock.md picotool row; no calibration applicable"
  - "Stopwatch; phone clock; 60 s count window; not a credited instrument (credit false); no calibration applicable"
ncr_ids: []
artifacts:
  - "docs/vv/reports/TC-SW-TOOL-001-r2/versions.txt sha256=604d2ace807213b93a4f798e44a49bde3ba6ad910f7a77b6eea278e022f59bad"
  - "docs/vv/reports/TC-SW-TOOL-001-r2/host-build-test.txt sha256=d5bc7c7fea95ea9a63beb5611208be7abc9930e924c1598461410e026bb99705"
  - "docs/vv/reports/TC-SW-TOOL-001-r2/sw-gate-full-a.txt sha256=e35d52efa817cc8542cd232173bfd744a4582986e5f39aa5e7f812162392d55a"
  - "docs/vv/reports/TC-SW-TOOL-001-r2/sw-gate-keep-going-a.txt sha256=82c2e33f84bd9aeda5a0289d5b9d9d1183ae22547776b0ec3b65dbeaa25f976d"
  - "docs/vv/reports/TC-SW-TOOL-001-r2/unsafe-audit.txt sha256=cfb9c2556b19b51081d63d72d48c74ec1efc0408944eb6718a42cecf2c8600d9"
  - "docs/vv/reports/TC-SW-TOOL-001-r2/sw-gate-full.txt sha256=e723989657eb35d96a53661e6ca8224a3e38ff87fbb2cf5f76c78d3a16f119e4"
  - "docs/vv/reports/TC-SW-TOOL-001-r2/sw-gate-keep-going.txt sha256=d3d50f83f58572abdff7d975f7bf1cfb2805cf4617545f87572ef95acf5b41f1"
  - "docs/vv/reports/TC-SW-TOOL-001-r2/gate-known-answer.sh sha256=bd8af403451ad9adb8a17959090a6dc312f6a9a9a6e247a0d9888db0396632db"
  - "docs/vv/reports/TC-SW-TOOL-001-r2/gate-known-answer.txt sha256=d72e4f1715a6ea4c14cbec20fb3f9782e5beaf3ea6b229f32461e6df0f3e2f6e"
  - "docs/vv/reports/TC-SW-TOOL-001-r2/blinky-build.txt sha256=45326dcf5f28b455d15e7ba11ed26fd20918057c05702f34f2ec03442a5bdd28"
  - "docs/vv/reports/TC-SW-TOOL-001-r2/rustos-blinky.elf sha256=ef16271deaaf37714cca58bc3cb789f4c94f8a9f98a1c4b343b676e5716ba8c1"
  - "docs/vv/reports/TC-SW-TOOL-001-r2/rustos-blinky.uf2 sha256=c45b526837c0831206763eb3134a8e71c854059ff7442c19e51f39edf03308d3"
  - "docs/vv/reports/TC-SW-TOOL-001-r2/cwht-app-build.txt sha256=f32b0385a7fefb2967164824937835e0a2f7c00ab20c6a45069744f2e243b5fc"
  - "docs/vv/reports/TC-SW-TOOL-001-r2/cwht-app.elf sha256=622cbe2a6b8e5d2a12ac5a94306a49dd7ecde1f31c5eb937e3e85b6066b9802f"
  - "docs/vv/reports/TC-SW-TOOL-001-r2/cwht-app.uf2 sha256=4e0bd133a10b6e29f72f00023ec407cd1885b8550a685b881c7be213462b3529"
  - "docs/vv/reports/TC-SW-TOOL-001-r2/cwht-app.map sha256=759c59cfe88aab22682e357194a3fca82077b464cd1a828f3bfba3351217d946"
  - "docs/vv/reports/TC-SW-TOOL-001-r2/uf2-info.txt sha256=fbc7edd83b0ecea159c88da1e34edce4496b93c90ab85619e474eb8f90c3e59f"
  - "docs/vv/reports/TC-SW-TOOL-001-r2/blink-rate-prediction.txt sha256=8d335983f2fd6e9e07ec5805f48c65f72f03f2c2ba2915ecf098ae3dce6cdd17"
mop_values: []
---

# Verification report: TC-SW-TOOL-001 run 2

**Status of this run: Blocked.** Claude executed steps 1 to 10 and 13 on 2026-09-26 between 02:43 and 02:48 CDT, after the tool maintainer wrote the three scripts of SRR package item R3 (`tools/measurements.py`, `tools/unsafe_audit.py`, `tools/complexity_gate.py`). The gate of step 6 still exits 1. Every remaining gate item needs one of three owner actions: package decision 109 (downloads), decision 110 (rustos licence and manifests), or a new rustos work item for the missing CS-06 SAFETY comments that this run found (section 7). Steps 11 and 12 (flash and observe) are **Pending owner** (package OA-1). This is a dev-board case: `credit: false`, credit row `SUPPORT`, and it changes the status of no requirement (docs/process/04-verification-and-validation.md section 4, rule 7.3.12). Run 1 (`docs/vv/reports/TC-SW-TOOL-001-r1.md`) is not edited.

## 1. Objectives and degree to which they were met

The case, its objective and its requirements are unchanged from run 1 (case blob `fee1e724`, equal to HEAD `400e59d`). The objective is the FW-B0 exit criterion of docs/process/07-software-engineering-plan.md section 3.2 and the SRR toolchain-proof product of 07 section 3.1 (SRR package section 2 item H12, item R3).

| Requirement | Acceptance criterion (this case) | Measured or observed, run 2 | Met? |
|---|---|---|---|
| REQ-SYS-127 | Rust workspace builds for `thumbv8m.main-none-eabihf` against rustos by path; image runs on a Pico 2 | Release build exit 0, no warning, FLASH 1608 B (0.04 %), RAM 8200 B (1.54 %) (gate G2 through `tools/measurements.py --link-map`); dependency set `cwht-app`, `cwht-core`, `api`, `pico2` only; on-board run pending owner (step 12) | Partially (supporting only; closes by Inspection, row I) |
| REQ-SYS-128 | `cwht-core` and `cwht-hal-mock` build and test on the host; the same `cwht-core` links into the target image | Host build exit 0; 10 of 10 tests pass, twice, identical result sets (gate G3 through `tools/measurements.py --diff-runs`); 100 percent lines and functions of both host crates, 100 percent regions (developer evidence, cargo-llvm-cov TV pending) | Met for this case (supporting only; closes by Inspection, row I) |
| REQ-SYS-133 | `picotool load -v` of both UF2 images over the micro-USB succeeds and the images run | Both UF2 images rebuilt and byte-identical to run 1; `picotool info -a`: RP2350, ARM Secure, one image def block each; load pending owner (steps 11 and 12) | Not yet (supporting only; closes by Demonstration on the delivered unit, row D) |

## 2. Description of the activity and deviations

Claude re-ran the procedure on HEAD `400e59d` with the working-tree gate and scripts of the tool maintainer. The step 1 configuration record was written between gate run A and gate run B, not first; each gate log carries its own time stamp and the repository HEAD. Order of execution: gate run A (full and `--keep-going`, started 07:43:56 and 07:44:03 UTC), `tools/unsafe_audit.py --write` to generate `firmware/unsafe-audit.md` (CS-07), step 1, steps 2 and 3, gate run B (full and `--keep-going`, started 07:45:17 and 07:45:18 UTC), step 7, step 8, the cwht-app rebuild, steps 9 and 10. No download or install was made: every cargo command ran with `RUSTUP_AUTO_INSTALL=0`, the blinky and the cwht-app rebuilds with `CARGO_NET_OFFLINE=true`, and the rustos checkout was read only.

Deviations D1 to D8 of run 1 apply unchanged, except as follows (none affects credit, because the run carries none):

- D1 (pinned 1.98.0 toolchain not installed; the gate runs on stable, whose `rustc --version` equals the lock row) still applies. **Pending owner decision 109.**
- D4 (interim inline G2 and G3 checks) is closed: the gate took G2 and G3 through `tools/measurements.py` in both gate runs and in all nine known-answer runs (0 `INTERIM` lines in each, `gate-known-answer.txt`).
- D8 (second decision in `cwht-app/src/main.rs`) is now covered by `docs/cm/cr/CR-001-cs11-cs38-driver-construction-arms.md`, which the comment at `main.rs:36-40` cites (committed blob `e32006a5`). **Pending owner decision 108.**
- D9 (new). Step 4 is extended by an independent rebuild: `cwht-app` was built twice more with `CARGO_TARGET_DIR` in the scratch directory, and the three ELF SHA-256 values (two clean builds and the gate G2 build) were compared, as run 1 section 5 promised for run 2 (`cwht-app-build.txt`).
- D10 (new). Gate run A found `firmware/unsafe-audit.md` absent (CS-07; `tools/unsafe_audit.py` states the list is generated with `--write`). Claude generated it (`firmware/unsafe-audit.md`, 37 rows, all unsigned, git blob `b232d77a`) and re-ran the gate as run B. Both runs are recorded; run B is the result of this report.

## 3. Configuration under test and differences from the operational configuration

- Article: `pico2-devboard-1`, a bare Raspberry Pi Pico 2 (RP2350), not yet connected for this run.
- cwht commit `400e59d34835aed359049df9dad1329dfd372380`. Every `firmware/` file equals HEAD except the new untracked `firmware/unsafe-audit.md` (not a build input). Working-tree files of the gate that differ from HEAD (tool maintainer, 2026-09-26): `tools/sw_gate.sh` blob `54b13800` (HEAD `93bffdeb`: header and G6 output removal only), `tools/toolchain.lock.md` blob `77262c79`; untracked `tools/measurements.py` `abe25acb`, `tools/unsafe_audit.py` `cc3aaa2a`, `tools/complexity_gate.py` `9214fefb`; `tools/emu_run.sh` `17f102aa` equals HEAD (`versions.txt`).
- rustos `c54d35aa8e7f9ad30f6508bca458a59c1fc009db`, equal to the lock rustos row; `api/`, `firmware/`, `Cargo.toml`, `Cargo.lock` and `.cargo` clean (other rustos paths carry the owner's own staged renames under `docs/tutorials/`, outside the gate's scope).
- Images: `cwht-app.elf` SHA-256 `622cbe2a...9802f`, which differs from run 1 (`3992e5d8...80ec1`) only in debug information (the comment edits after run 1 moved source lines): the loadable sections `.vector_table`, `.boot_info`, `.text` and `.rodata` are byte-identical to run 1, and so is `cwht-app.uf2` (`4e0bd133...3529`). `rustos-blinky.elf` and `.uf2` are identical to run 1.
- Tools: as run 1 (rustc 1.98.0 88d9e12ae on the stable channel, cargo 1.98.0, cargo-nextest 0.9.146, cargo-llvm-cov 0.9.1, cargo-deny 0.20.2, cargo-geiger 0.13.0, cargo-audit 0.22.2 not run, cargo-binutils, picotool 2.3.0, Python 3.13.5). New: the three R3 scripts, with TV-011 to TV-013 filed as Validated and not accredited, so their output is developer evidence (CM plan section 9.1; SWE-136, NPR 7150.2D section 4.4.8).
- Differences from the operational configuration: as run 1 section 3 (bare dev board, USB power, on-board LED on GPIO25, deviation D6).

## 4. Results of each step

| Step | Procedure text (as run) | Expected | Observation | Artifact | Pass/Fail |
|---|---|---|---|---|---|
| 1 | Record configuration; rustos commit and rustc against the lock | Lock rows match; rustos code clean | rustos HEAD `c54d35a` equals the lock row, code directories clean; rustc equals the lock row; pinned 1.98.0 absent (D1); `nightly-2026-08-24` has no `miri` or `llvm-tools`; no RustSec database; `rust-code-analysis-cli` not installed | `versions.txt` | Pass |
| 2 | `cargo build` on the host | exit 0 | exit 0 | `host-build-test.txt` | Pass |
| 3 | `cargo test` on the host | all pass, at least 10 | 10 passed, 0 failed (5 `heartbeat`, 5 `gpio`) | `host-build-test.txt` | Pass |
| 4 | Target build; no warning; map written; memory from gate G2 | exit 0, no warning, map | exit 0; `PASS G2 no compiler warning`; FLASH 1608 B of 4194304 B (0.04 %, red line 70 %), RAM 8200 B of 532480 B (1.54 %, red line 75 %) from `measurements.py --link-map`; no allocator symbol; dependency set workspace plus rustos. D9: two clean rebuilds give the same SHA-256 as the gate build | `sw-gate-full.txt`, `cwht-app.map`, `cwht-app-build.txt` | Pass |
| 5 | fmt, host clippy, target clippy with `-D warnings` (gate G1) | no diff, no warning | `PASS G1 cargo fmt --check`, `PASS G1 clippy host`, `PASS G1 clippy target` | `sw-gate-full.txt` | Pass |
| 6 | `tools/sw_gate.sh` and `tools/sw_gate.sh --keep-going` | exit 0 (FW-B0 exit criterion) | Run B: G0 to G4 PASS (13 steps; G4 traceability now passes). Stopping run: `FAIL G5 cargo deny (bans, licenses, sources)`, exit 1. Keep-going run: 2 FAIL (G5 cargo deny; G5 unsafe audit, 36 rustos sites without a SAFETY comment), 5 MISSING (cargo audit database, cargo deny advisory database, `rust-code-analysis-cli`, Miri, nightly `llvm-tools`), geiger 3 PASS, G6 stable coverage PASS, G6 emulation prints `SKIP emulation: no accepted emulator ADR`, G6 measurements PASS (MSR-14 and emulation outputs reported NOT PRODUCED); exit 1. Run A differed only in the unsafe audit, which also reported the absent audit list (D10); MISSING count 5 in both, down from 9 in run 1 | `sw-gate-full.txt`, `sw-gate-keep-going.txt`, `sw-gate-full-a.txt`, `sw-gate-keep-going-a.txt`, `unsafe-audit.txt` | Blocked |
| 7 | Gate known-answer runs KA-0 to KA-8 | KA-0 exit 0; KA-1 to KA-7 exit 1 at the seeded gate; KA-8 exit 1 with the G3 comparison FAIL | All nine MATCH: KA-0 exit 0; KA-1 and KA-4 `FAIL G1 clippy host`; KA-2 `FAIL G1 cargo fmt --check`; KA-3 `FAIL G3 host tests run 1`; KA-5 `FAIL G0`; KA-6 `FAIL G1 clippy target`; KA-7 `FAIL G2 no compiler warning`; KA-8 exit 1, `FAIL G3 identical result sets (JUnit file of run 1 or run 2 not written by this invocation)`, stale files removed. 0 `INTERIM` lines in each run | `gate-known-answer.sh`, `gate-known-answer.txt` | Pass |
| 8 | Fresh rustos blinky, two builds | two identical SHA-256 | both `ef16271d...ba8c1`, equal to run 1 | `blinky-build.txt`, `rustos-blinky.elf` | Pass |
| 9 | `picotool uf2 convert` and `picotool info -a` for both images | RP2350, ARM Secure, one image def block each | all four commands exit 0; both RP2350, ARM Secure, one image def block at 0x10000110; both UF2 byte-identical to run 1 | `uf2-info.txt`, `rustos-blinky.uf2`, `cwht-app.uf2` | Pass |
| 10 | Blink-rate prediction from the disassembly | windows computed | delay loops unchanged (blinky 66 instructions per 64 spins; cwht-app 3 per spin); windows unchanged: 10 to 120 and 3 to 45 cycles in 60 s | `blink-rate-prediction.txt` | Pass |
| 11 | Flash and observe the rustos blinky | load verified, reboot exit 0, 10 to 120 cycles in 60 s | **Pending owner** (OA-1) | `flash-rustos-blinky.txt` (to be written) | Pending owner |
| 12 | Flash and observe cwht-app | load verified, reboot exit 0, 3 to 45 cycles in 60 s | **Pending owner** (OA-1) | `flash-cwht-app.txt` (to be written) | Pending owner |
| 13 | Record versions, commits, blob and hashes | recorded | this report and its front matter | this file | Pass |
| 14 | Stop rule | NCR on discrepancy | no product discrepancy in the cwht workspace; the G5 items are rustos or owner-download items (section 7), proposed for owner disposition, not NCRs | none | n/a |

Steps 11 and 12 follow the owner steps of run 1 section 4 unchanged. Because the run 2 UF2 files are byte-identical to the run 1 files, the images the procedure names under `docs/vv/reports/TC-SW-TOOL-001-r1/` are the images of this run; run 3 records the owner steps.

## 5. Analysis of results

- Effect of item R3. With the three scripts present, G2 and G3 run through `tools/measurements.py` and give the same values as the run 1 interim checks (1608 B, 8200 B; 10 identical passing cases), and G5 now runs the unsafe audit. The gate reports 5 MISSING items instead of 9: the four script items of run 1 are gone. The complexity step cannot run end to end because `rust-code-analysis-cli` is absent (decision 109), so `tools/complexity_gate.py` was not exercised by the gate (TV-012 records the same open end-to-end check).
- G4 traceability passes (exit 0) where run 1 failed on requirements then in authoring.
- G5 unsafe audit (new FAIL). 37 unsafe sites in rustos `api` and `firmware/pico2` (block 16, fn 11, impl 1, extern 3, attribute 6), 36 without the `// SAFETY:` comment CS-06 requires (07 section 7.2); 0 sites in the cwht crates (CS-05 holds, and geiger confirms `#![forbid(unsafe_code)]` in all three). The sources are rustos code, read only for cwht agents (SI-033), so the fix is a rustos work item for the owner as rustos maintainer. The audit list itself (CS-07) now exists; its 37 entries are unsigned, which is a note until CDR (`unsafe_audit.py --gate SRR`).
- G5 cargo deny: unchanged from run 1 (`api` and `pico2` unlicensed; the `pico2` path dependency counts as a wildcard); closes on decision 110.
- Known-answer runs. The nine seeded runs now include KA-7 and KA-8 of the revised case, run on copies that carry the three scripts, so they show the G0, G1, G2 warning and G3 decisions discriminate with the scripts in the loop.
- Reproducibility. Two clean cwht-app builds and the gate build give one SHA-256; the blinky rebuilds equal run 1; both UF2 files equal run 1 (SWE-186 is shown for the host tests by G3; NPR 7150.2D section 4.4.6).
- Log reading note. `tools/measurements.py` prints its own lines beginning `PASS` (for example `PASS FLASH used ...`, `PASS identical result sets ...`) inside the gate log, so a count of lines starting with `PASS` over-counts gate steps by three. The step results above count only the gate's `PASS <step>` lines (cross item to the tool maintainer).

## 6. Data tables, plots and pictures

All data are text logs and images in `docs/vv/reports/TC-SW-TOOL-001-r2/`, listed with SHA-256 in the front matter. No plot or photograph is produced by steps 1 to 10.

Gate result summary (run B, `--keep-going`):

| Gate | PASS | FAIL | MISSING | SKIP |
|---|---|---|---|---|
| G0 | 1 | 0 | 0 | 0 |
| G1 | 3 | 0 | 0 | 0 |
| G2 | 5 | 0 | 0 | 0 |
| G3 | 3 | 0 | 0 | 0 |
| G4 | 1 | 0 | 0 | 0 |
| G5 | 3 (geiger) | 2 (cargo deny; unsafe audit) | 4 (cargo audit DB, deny advisory DB, rust-code-analysis-cli, Miri) | 0 |
| G6 | 3 (coverage, emulation stub, measurements) | 0 | 1 (nightly branch and condition coverage) | 1 (emulation line) |

## 7. Non-conformances and discrepancies

| NCR | Severity | Step | Summary | Disposition | Retest planned |
|---|---|---|---|---|---|
| None | | | | | |

Items that block the gate (none is a defect of the cwht workspace). Each is **Pending owner decision**; Claude downloaded, installed and edited nothing outside its scope to clear them:

| # | Gate line | Cause | Closes on | Owner |
|---|---|---|---|---|
| B1 | `FAIL G5 cargo deny (bans, licenses, sources)` | rustos `api` and `pico2` carry no `license` and no `publish = false` | Decision 110 (rustos licence and manifest work item), then a gate re-run | Robin (rustos maintainer) |
| B2 | `FAIL G5 unsafe audit` | 36 rustos sites without a CS-06 SAFETY comment (list in `unsafe-audit.txt` and `firmware/unsafe-audit.md`) | A rustos work item adding the SAFETY comments (with datasheet section for MMIO, CS-06), proposed as an addition to decision 110; then `tools/unsafe_audit.py --write` and a gate re-run | Robin (rustos maintainer); Claude regenerates the list |
| B3 | `MISSING G5 cargo audit`, `MISSING G5 cargo deny advisories` | RustSec advisory database absent | Decision 109 (one `cargo audit` without `--no-fetch`, one `cargo deny fetch`) | Robin |
| B4 | `MISSING G5 complexity` | `rust-code-analysis-cli` not installed | Decision 109 (`cargo install rust-code-analysis-cli --locked`) | Robin |
| B5 | `MISSING G5 Miri`, `MISSING G6 branch and condition coverage` | `miri` and `llvm-tools` absent on `nightly-2026-08-24` | Decision 109 (`rustup toolchain install nightly-2026-08-24 --component miri --component llvm-tools`) | Robin |
| B6 | NOTE lines of G0 (D1) | pinned 1.98.0 toolchain absent | Decision 109 (`rustup toolchain install 1.98.0 ...`) | Robin |
| B7 | steps 11 and 12 | flash and observe | OA-1 | Robin, with Claude running every command |

Expected consequence once B4 is installed: `tools/complexity_gate.py` applies CS-38 to `cwht-app/src/main.rs` (tagged `// @target-only`), whose `output_from_handle` arm is the second decision of deviation D8. The gate then fails G5 complexity until CR-001 (decision 108) is approved and the gate's CS-38 allowance follows it, or a waiver is named (07 section 14.3). This is a prediction, not a run result.

## 8. Status of enabling equipment after the run

No change. The rustos checkout was read only (`git status` of its code directories clean after the run). No toolchain, component, crate or database was added (`versions.txt`).

## 9. Conclusions and recommendations

Verdict: Blocked. Every gate step the software lead can close without the owner now passes: G0 to G4, the geiger forbid checks, stable coverage at 100 percent (developer evidence), the emulation stub and the G6 measurements, with the R3 scripts in the loop and nine known-answer runs matching. The FW-B0 exit criterion (gate exit 0) is not met; the two FAIL and five MISSING items of section 7 close only on decisions 109 and 110 plus the rustos SAFETY-comment work item, and steps 11 and 12 await OA-1. No requirement status changes (dev-board case, `credit: false`).

Recommendations:

1. Owner: rule decision 109 (downloads) and decision 110 (licence and manifests), and add to decision 110 the rustos SAFETY-comment work item for the 36 sites of B2.
2. Owner: perform OA-1 (steps 11 and 12) with the run 1 image paths (byte-identical to run 2).
3. Claude, after 1 and 2: record the installs in `tools/toolchain.lock.md`, regenerate `firmware/unsafe-audit.md`, re-run the gate to exit 0 and file run 3 with the flash records.
4. Tool maintainer: the lock section 1.1 sanity checks still read "not yet run" for cargo-nextest, cargo-llvm-cov, cargo-audit, cargo-deny, cargo-geiger and cargo-binutils (INSP-016 finding-1 second exit criterion); the `tools/unsafe_audit.py` lock row still says the list is "not yet generated"; and `measurements.py` result lines that begin with `PASS` should not mimic gate step lines.

Deferrals FD-1 and FD-2 of run 1 stand unchanged.

## 10. As-run procedure

Steps 1 to 10 and 13 as written in `docs/test_cases/sw-tool/test_cases.json` (blob `fee1e724`, unchanged from HEAD; the procedure did not change, so the case file is not edited), with deviations D1 to D3, D5 to D10 of section 2. Step 5 was run as gate G1 within step 6. Steps 11 and 12 not yet run.

## 11. Answers to INSP-016 findings that close without the owner (author response for the reviewer's next iteration)

INSP-016 (`docs/reviews/SRR/checklists/fw-b0-toolchain-proof.md`, iteration 2) has three open findings. The author response below is input for the reviewer; the reviewer, not the author, changes the record.

| Finding | Severity | Author response | What closes it |
|---|---|---|---|
| finding-1 | Major | Fixed as far as the author can go: `tools/emu_run.sh` (SKIP-line stub, `PASS G6 emulation`), `tools/unsafe_audit.py`, `tools/complexity_gate.py` and `tools/measurements.py` exist (TV-011 to TV-013 Validated); `firmware/unsafe-audit.md` generated; the gate re-run end to end in both modes, 5 MISSING down from 9, G4 now PASS; KA-0 to KA-8 reproduced with the scripts in the copies; this run 2 filed | Decisions 109 and 110 plus the rustos SAFETY-comment work item (section 7, B1 to B6), the lock sanity checks (tool maintainer), then a gate exit 0 and run 3 after OA-1. The finding stays Major and Open until then; it cannot close without the owner |
| finding-2 | Major | The comment at `main.rs:36-40` now cites `docs/cm/cr/CR-001-cs11-cs38-driver-construction-arms.md` (committed blob `e32006a5`, which differs from the reviewed blob `b2464fb2`; the reviewer re-reads the committed file, package section 2.3) | Decision 108 (owner disposition of CR-001) |
| finding-4 | Minor | Not an author fix (the author may not review its own tests, charter section 11 rule 4). Under the convergence rule of 2026-09-26 (charter section 4 item 3) the author proposes the disposition "Lien: fix before PDR", carried by the package as a Routine item: an independent test-author invocation reviews `firmware/cwht-core/tests/heartbeat.rs` and `firmware/cwht-hal-mock/tests/gpio.rs` (package item R4) | Reviewer disposition as a lien |

Committed blobs of the INSP-016 product files at HEAD `400e59d` (for the reviewer's `product_files`, package item R13): `firmware/.cargo/config.toml` `b677319f`, `firmware/cwht-app/src/main.rs` `e32006a5`, `firmware/cwht-hal-mock/src/gpio.rs` `fc8872bd`, `tools/sw_gate.sh` `93bffdeb` (working tree `54b13800`, uncommitted tool-maintainer edit), `docs/test_cases/sw-tool/test_cases.json` `fee1e724`, `docs/vv/reports/TC-SW-TOOL-001-r1.md` `04bc3354`.

## 12. Authentication and authorization

- Results authenticated by (conductor): claude, 2026-09-26
- Witnessed by: owner, pending (steps 11 and 12)
- Authorization of acceptability (owner): pending
