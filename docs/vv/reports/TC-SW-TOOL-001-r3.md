---
test_case: TC-SW-TOOL-001
run: 3
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
source_commit: "0bcea39554d684ba28d6680208a523fd79a8ebba"
firmware_elf_sha256: "388d1d16dae55d33fcc0c69d33689abcf6d056bcc16e44a18abab2ac2300a5bf"
requirements_baseline: "none (SRR approved with liens 2026-09-26; baseline/srr not yet tagged)"
procedure_commit: "0bcea39"
procedure_blob: "fee1e7246af59d5e8a43ed1b9cdf483854053fdc"
toolchain_lock: "tools/toolchain.lock.md blob 0ad60317be7e509c1e1968d2d9f4813f3904253f at 0bcea39, run from a temporary copy whose rustos row names the branch commit 2ec64c0f15c8cd2dbcaa241abffdd72f8cae467c (deviation D12)"
harness_versions: "n/a"
instruments:
  - "Host only: owner's Mac (macOS 26.6.2, arm64); no board connected in this run (steps 11 and 12 not run, section 4); tools/toolchain.lock.md rows as re-observed 2026-09-26; no calibration applicable"
ncr_ids: []
artifacts:
  - "docs/vv/reports/TC-SW-TOOL-001-r3/versions.txt sha256=f4af263c7b431f665a133669d74d0efaa17c330bb1c92a2e0e3eaf0751ad8700"
  - "docs/vv/reports/TC-SW-TOOL-001-r3/host-build-test.txt sha256=ab59264a47e440b6d46d77f4ee9afe9e42546826d3e82fcccef7206d979c8c36"
  - "docs/vv/reports/TC-SW-TOOL-001-r3/unsafe-audit.txt sha256=1ddb07405917a83db308ed41cbcbb1e38dff660206a0dbcdd47bd95f8c9dff40"
  - "docs/vv/reports/TC-SW-TOOL-001-r3/sw-gate-full.txt sha256=51a1265895fe46c1ff64a9db35c2eedfb377308462d5af8a800a06fa9ee98e2f"
  - "docs/vv/reports/TC-SW-TOOL-001-r3/sw-gate-keep-going.txt sha256=a0804e4e0740591346676f6ddb15625507e2edeccf0fcfa4d827ea21c2d27824"
  - "docs/vv/reports/TC-SW-TOOL-001-r3/complexity-diagnostic.txt sha256=d5e50a48fda9a3fcd3e076466c9c6a7e1c079ef6982500e113379dc3f7a952c2"
  - "docs/vv/reports/TC-SW-TOOL-001-r3/gate-known-answer.sh sha256=3d27b795a11a7c839d4ccfb15523b435d58e031be35970fe557d1a875b3eb90d"
  - "docs/vv/reports/TC-SW-TOOL-001-r3/gate-known-answer.txt sha256=1165adb94d1a9c3fa7359735f626ad442268d5c9592bcc6b3c798bcfc57a1138"
  - "docs/vv/reports/TC-SW-TOOL-001-r3/run3.sh sha256=48024517b617eee84f668444c5e2e4309949c0b7ba2090a5f1eb233421f5fff6"
  - "docs/vv/reports/TC-SW-TOOL-001-r3/rustup-guard.sh sha256=9b1ea18c5d5983d7311c0011ecba4a5add1841e99dbc630ed9dc3ad698269828"
  - "docs/vv/reports/TC-SW-TOOL-001-r3/rustos-build-test.txt sha256=e2e50e17cc2fad3527e7e77ffaf62f399a4ced81cdd257d380462de0aafd8621"
  - "docs/vv/reports/TC-SW-TOOL-001-r3/blinky-build.txt sha256=fde743073c3b19d0c8d915897acf88cdda9f32fff90b4ab035fa96738a1c7916"
  - "docs/vv/reports/TC-SW-TOOL-001-r3/rustos-blinky.elf sha256=3c0ac0747a761bf9880e21f80ba613cfcb5e8f5ddddbdea7af85dbf8952bbd08"
  - "docs/vv/reports/TC-SW-TOOL-001-r3/rustos-blinky.uf2 sha256=c45b526837c0831206763eb3134a8e71c854059ff7442c19e51f39edf03308d3"
  - "docs/vv/reports/TC-SW-TOOL-001-r3/cwht-app-build.txt sha256=af3184e85fbb386d2eb13fe408c93d5976444e10f1ea57c04df5a4ba8f7a2e66"
  - "docs/vv/reports/TC-SW-TOOL-001-r3/cwht-app.elf sha256=388d1d16dae55d33fcc0c69d33689abcf6d056bcc16e44a18abab2ac2300a5bf"
  - "docs/vv/reports/TC-SW-TOOL-001-r3/cwht-app.uf2 sha256=4e0bd133a10b6e29f72f00023ec407cd1885b8550a685b881c7be213462b3529"
  - "docs/vv/reports/TC-SW-TOOL-001-r3/cwht-app.map sha256=a6cfe01b3597a9dbd7cfbfe72433a620e95d8fd5202fdcd348e1fb050f8bf4b2"
  - "docs/vv/reports/TC-SW-TOOL-001-r3/uf2-info.txt sha256=7a799b520144c24c44977fdde2ffe461f249644f719727dd1818a56667029e1f"
  - "docs/vv/reports/TC-SW-TOOL-001-r3/blink-rate-prediction.txt sha256=0ebd6da2ddd0e171622baa085bc8da006d597e51baa34a0158be03443551edd5"
mop_values: []
---

# Verification report: TC-SW-TOOL-001 run 3

**Status of this run: Blocked.** Claude ran steps 1 to 10 and 13 on 2026-09-26 between 19:28 and 19:41 CDT, after the owner's SRR rulings (minutes of 2026-09-26): decision 109 (the four toolchain installs, made 19:18 to 19:20 and recorded in `tools/toolchain.lock.md`) and decision 110 (the rustos MIT licence and the manifest and SAFETY-comment work item, made on a rustos branch). The run is against that branch: the gate ran on a temporary copy of cwht whose `../rustos` is the branch worktree, and nothing in the cwht repository or the owner's rustos checkout changed for it. The gate exits 1 with 0 MISSING and 2 FAIL: G5 complexity and G5 Miri (section 7). This is a dev-board case: `credit: false`, credit row `SUPPORT`, and it changes the status of no requirement (docs/process/04-verification-and-validation.md section 4, rule 7.3.12). Runs 1 and 2 are not edited.

**The rustos pin does not move with this run.** The work item is on the rustos branch `cwht/wp-sw-licence-manifest-safety` at `2ec64c0f15c8cd2dbcaa241abffdd72f8cae467c`, committed in the worktree `/Users/robinonsay/rust/rustos-wp-sw-licence`, not pushed and not merged. The `tools/toolchain.lock.md` section 3 pin stays at `c54d35a`. It moves only when the owner, as rustos maintainer, merges the branch and a CR moves the lock pin. Until then the repository gate runs on `c54d35a` and keeps the run 2 FAILs of G5 cargo deny and G5 unsafe audit.

## 1. Objectives and degree to which they were met

The case, its objective and its requirements are unchanged (case blob `fee1e724` at `0bcea39`). The objective is the FW-B0 exit criterion of docs/process/07-software-engineering-plan.md section 3.2 and the SRR toolchain-proof product of 07 section 3.1 (SRR package item H12, post-ruling item R16 (a)).

| Requirement | Acceptance criterion (this case) | Measured or observed, run 3 | Met? |
|---|---|---|---|
| REQ-SYS-127 | Rust workspace builds for `thumbv8m.main-none-eabihf` against rustos by path; image runs on a Pico 2 | Release build on the pinned `1.98.0`, exit 0, no warning; FLASH 1608 B (0.04 %), RAM 8200 B (1.54 %) through `tools/measurements.py --link-map`; dependency set `cwht-app`, `cwht-core`, `api`, `pico2`; loadable sections identical to run 2; on-board run: see steps 11 and 12 (section 4) | Partially (supporting only; closes by Inspection, row I) |
| REQ-SYS-128 | `cwht-core` and `cwht-hal-mock` build and test on the host; the same `cwht-core` links into the target image | Host build exit 0; 10 of 10 tests pass, twice, identical result sets (G3); 100 percent lines and regions of both host crates (G6, developer evidence) | Met for this case (supporting only; closes by Inspection, row I) |
| REQ-SYS-133 | `picotool load -v` of both UF2 images succeeds and the images run | Both UF2 files of run 3 are byte-identical to the run 2 files; `picotool info -a`: RP2350, ARM Secure, one image def block each; load not run in run 3 (section 4, steps 11 and 12) | Not in this run (supporting only; closes by Demonstration on the delivered unit, row D) |

## 2. Description of the activity and deviations

Order of execution: the decision 109 installs (19:18 to 19:20; `docs/cm/tool-validation/evidence/rust-tools-2026-09-26.log.txt` section 0); the rustos worktree and branch (`git -C /Users/robinonsay/rust/rustos worktree add /Users/robinonsay/rust/rustos-wp-sw-licence -b cwht/wp-sw-licence-manifest-safety` from `c54d35a`); the work item edits; the rustos build and test (`rustos-build-test.txt`); the branch commit `2ec64c0`; then `run3.sh` (steps 1 to 6 and 8 to 10, 19:28 to 19:29) and `gate-known-answer.sh` (step 7, 19:30 to 19:41). The layout was removed after the run.

Deviations from the case, and from runs 1 and 2 (none affects credit, because the run carries none):

- D1 (pinned 1.98.0 absent, gate on stable) is **closed**: the pin is installed (decision 109); G0 reports "pinned toolchain 1.98.0 installed; firmware/rust-toolchain.toml selects it".
- D4 stays closed (G2 and G3 through `tools/measurements.py`, 0 `INTERIM` lines in every run).
- D8 (second decision in `cwht-app/src/main.rs`): CR-001 was approved as SRR decision 108 and applied to 07 CS-11, CS-12 and CS-38 (`4364ebb`). The comment at `main.rs:36-40` still reads "owner disposition before FW-B1" (cross item to the CR-001 implementer).
- D9 (independent rebuild in step 4) and D10 (audit list generated with `--write`) are repeated. For D10 the list is regenerated inside the temporary layout only, because the committed `firmware/unsafe-audit.md` describes the pinned rustos `c54d35a`.
- D11 (new). **Temporary layout.** `tools/sw_gate.sh` takes rustos from `$ROOT/../rustos`, and `firmware/Cargo.toml` takes it from `../../rustos`. So the run uses `<scratch>/r3/cwht`, a `git archive` of cwht `HEAD` `0bcea39` holding committed content only, with `.venv` linked, and `<scratch>/r3/rustos`, a symbolic link to the worktree. `firmware/Cargo.toml` is unchanged; its path dependency resolves through the link. The layout, the known-answer copies and all build directories were deleted after the run.
- D12 (new). **Lock copy.** G0 compares the rustos `HEAD` with the lock's rustos row and stops by design on a mismatch. The lock copy in the layout therefore names the branch commit `2ec64c0`. This one row is the only difference from `HEAD` (`versions.txt`, "temporary lock copy" section). The repository lock is not changed.
- D13 (new). **No download.** Every command ran with `RUSTUP_AUTO_INSTALL=0`, `CARGO_NET_OFFLINE=true` and `MIRI_AUTO_OPS=no`. A `rustup` shim came first on `PATH` (`rustup-guard.sh`); it refuses `component add`, `toolchain install` and `self update` and forwards everything else. The guard was needed: cargo-miri runs `rustup component add rust-src` by itself, and two probes before the guard existed downloaded `rust-src`, which was removed at once (lock section 1.4 finding 8).
- D14 (new). In KA-8 (`--keep-going`) the G5 Miri step stopped at cargo-miri's interactive install prompt. At 19:40:53 the conductor ended the waiting process, so G5 Miri reported FAIL, as it did in step 6. KA-8's criterion is unaffected (note at the end of `gate-known-answer.txt`).
- D15 (new). Steps 11 and 12 were not run in run 3 (section 4).

## 3. Configuration under test and differences from the operational configuration

- Article: `pico2-devboard-1`, not connected in this run.
- cwht commit `0bcea39554d684ba28d6680208a523fd79a8ebba`, committed content only (D11). `firmware/` and every gate script equal `HEAD`. The gate scripts are `tools/sw_gate.sh` `54b13800`, `tools/measurements.py` `abe25acb`, `tools/unsafe_audit.py` `cc3aaa2a`, `tools/complexity_gate.py` `9214fefb` and `tools/emu_run.sh` `17f102aa` (`versions.txt`).
- rustos branch `cwht/wp-sw-licence-manifest-safety`, commit `2ec64c0f15c8cd2dbcaa241abffdd72f8cae467c`, whose parent is the lock pin `c54d35a`. The worktree's `api/`, `firmware/`, `Cargo.toml`, `Cargo.lock`, `.cargo` and `LICENSE` are clean. The owner's checkout `/Users/robinonsay/rust/rustos` was neither read nor written beyond `git rev-parse HEAD` and the `worktree add`; its uncommitted work of the owner's own is untouched. The branch diff against `c54d35a` has three parts:
  - `LICENSE`: MIT, the cwht text and holder.
  - `license = "MIT"` and `publish = false` in `api/Cargo.toml` and `firmware/pico2/Cargo.toml`.
  - 178 comment lines in `api/src/device/mod.rs`, `firmware/pico2/src/common/reset.rs`, `firmware/pico2/src/gpio/gpio.rs` and `firmware/pico2/src/lib.rs`: a `// SAFETY:` comment directly above each of the 36 sites, stating the invariant and why it holds, with the RP2350 datasheet section for every MMIO access (CS-06).

  No Rust code line changed: the `.rs` diff has 0 lines that are not added `//` comments. rustos `cargo build`, `cargo test` (0 unit tests, 3 ignored doc examples, as at `c54d35a`) and `cargo build -p pico2` for the target, debug and release, exit 0. The pico2 clippy warning set is identical to `c54d35a` (13 pre-existing warnings; `rustos-build-test.txt`).
- Tools: pinned `rustc 1.98.0 (88d9e12ae 2026-08-18)` with clippy, rustfmt and llvm-tools; `nightly-2026-08-24` with `miri` and `llvm-tools` and without `rust-src`; `rust-code-analysis-cli` 0.0.25; RustSec databases at `e2111519`; cargo-nextest 0.9.146, cargo-llvm-cov 0.9.1, cargo-audit 0.22.2, cargo-deny 0.20.2, cargo-geiger 0.13.0, picotool 2.3.0; rustup 1.29.1 (lock section 1.4 finding 7). The Python tools TV-002 to TV-010 are Accredited from 2026-09-26 (SRR decision 114). TV-011 to TV-013 and the Rust tools are not, so their outputs are developer evidence (CM plan section 9.1; SWE-136, NPR 7150.2D section 4.4.8).
- Images: `cwht-app.elf` SHA-256 `388d1d16...a5bf`, which differs from run 2 (`622cbe2a...9802f`) only outside the loadable sections: `.vector_table`, `.boot_info` and `.text` are byte-identical (`.rodata` and `.data` are empty), and so is `cwht-app.uf2` (`4e0bd133...3529`). The rustos blinky ELF (`3c0ac074...bd08`) differs from run 2 in the same way. All five loadable sections are identical, and so is `rustos-blinky.uf2` (`c45b5268...08d3`). The comment lines moved source line numbers in the debug information only.
- Differences from the operational configuration: as run 1 section 3.

## 4. Results of each step

| Step | Procedure text (as run) | Expected | Observation | Artifact | Pass/Fail |
|---|---|---|---|---|---|
| 1 | Record configuration; rustos commit and rustc against the lock | Lock rows match; rustos code clean | cwht `0bcea39`; rustos worktree `2ec64c0` clean, equal to the lock copy's row (D12); rustc in `firmware/` from the pin, equal to the lock row; every tool version recorded | `versions.txt` | Pass |
| 2 | `cargo build` on the host | exit 0 | exit 0 | `host-build-test.txt` | Pass |
| 3 | `cargo test` on the host | all pass, at least 10 | 10 passed, 0 failed (5 `heartbeat`, 5 `gpio`) | `host-build-test.txt` | Pass |
| 4 | Target build; no warning; map written; memory from gate G2 | exit 0, no warning, map | `PASS G2 build`, `PASS G2 no compiler warning`; FLASH 1608 B of 4194304 B (0.04 %), RAM 8200 B of 532480 B (1.54 %); no allocator symbol; dependency set workspace plus rustos. D9: two clean rebuilds give the gate build's SHA-256 `388d1d16...a5bf` | `sw-gate-full.txt`, `cwht-app.map`, `cwht-app-build.txt` | Pass |
| 5 | fmt, host clippy, target clippy with `-D warnings` (gate G1) | no diff, no warning | `PASS G1 cargo fmt --check`, `PASS G1 clippy host`, `PASS G1 clippy target` | `sw-gate-full.txt` | Pass |
| 6 | `tools/sw_gate.sh` and `tools/sw_gate.sh --keep-going` | exit 0 (FW-B0 exit criterion) | Stopping run: G0 to G4 PASS, G5 cargo audit, cargo deny (bans, licenses, sources), deny advisories, the three geiger checks and the unsafe audit PASS, then `FAIL G5 complexity`, exit 1. Keep-going run: 24 gate-step PASS lines, 2 FAIL (`G5 complexity`, `G5 Miri (nightly, non-credit, MSR-08)`), **0 MISSING** (5 in run 2), 1 SKIP line (emulation stub), exit 1. G6 stable coverage 100 percent, G6 branch and condition coverage PASS (MSR-14 now produced), G6 measurements PASS | `sw-gate-full.txt`, `sw-gate-keep-going.txt`, `unsafe-audit.txt`, `complexity-diagnostic.txt` | Blocked |
| 7 | Gate known-answer runs KA-0 to KA-8 | KA-0 exit 0; KA-1 to KA-7 exit 1 at the seeded gate; KA-8 exit 1 with the G3 comparison FAIL | All nine MATCH, first FAIL lines as in run 2: KA-1 and KA-4 `FAIL G1 clippy host`, KA-2 `FAIL G1 cargo fmt --check`, KA-3 `FAIL G3 host tests run 1`, KA-5 `FAIL G0` (now against the pinned toolchain), KA-6 `FAIL G1 clippy target`, KA-7 `FAIL G2 no compiler warning`; KA-8 exit 1 with `FAIL G3 identical result sets (JUnit file of run 1 or run 2 not written by this invocation)`, stale files removed (D14). 0 `INTERIM` lines | `gate-known-answer.sh`, `gate-known-answer.txt` | Pass |
| 8 | Fresh rustos blinky (branch templates/pico2, path form to the worktree), two builds | two identical SHA-256 | both `3c0ac074...bd08`; loadable sections identical to run 2 | `blinky-build.txt`, `rustos-blinky.elf` | Pass |
| 9 | `picotool uf2 convert` and `picotool info -a` for both images | RP2350, ARM Secure, one image def block each | all four commands exit 0; both RP2350, ARM Secure, one image def block; both UF2 files byte-identical to run 2 | `uf2-info.txt`, `rustos-blinky.uf2`, `cwht-app.uf2` | Pass |
| 10 | Blink-rate prediction | windows computed | `.text` of both images identical to run 2, so the run 2 prediction holds unchanged: 10 to 120 and 3 to 45 cycles in 60 s | `blink-rate-prediction.txt` | Pass |
| 11 | Flash and observe the rustos blinky | load verified, reboot exit 0, 10 to 120 cycles in 60 s | **Not run in run 3.** The owner reversed the PDR deferral of OA-1 during the SRR session, and Claude ran this step with the owner on 2026-09-26 at 19:17 to 19:18 CDT with the run 1 and 2 image `rustos-blinky.uf2` (`c45b5268...08d3`): load and verify OK, reboot exit 0, 60 to 63 cycles in 60 s, Pass (`docs/reviews/SRR/minutes.md`, "OA-1 and OA-2 performed"). The run 3 UF2 is the same file byte for byte. The minutes file the raw outputs with run 4 | none in run 3 | Not run (see observation) |
| 12 | Flash and observe cwht-app | load verified, reboot exit 0, 3 to 45 cycles in 60 s | **Not run in run 3**, as step 11: performed at 19:20 CDT with `cwht-app.uf2` (`4e0bd133...3529`), 18 cycles in 60 s, Pass (minutes). The run 3 UF2 is the same file byte for byte | none in run 3 | Not run (see observation) |
| 13 | Record versions, commits, blob and hashes | recorded | this report and its front matter | this file | Pass |
| 14 | Stop rule | NCR on discrepancy | no product discrepancy in the cwht workspace or the rustos branch; the two FAIL lines come from a gate invocation defect, an analyzer counting convention and an absent component (section 7), proposed for disposition, not NCRs | none | n/a |

Reconciling this run with its brief: the brief said steps 11 and 12 stay Pending owner, OA-1 being deferred to PDR by the SRR approval. The minutes committed at `0a6f461` during this run record that the deferral was reversed and that OA-1 was performed. This report therefore records steps 11 and 12 as not run in run 3, not as pending.

## 5. Analysis of results

- **Decision 110 work item.** On the branch, `PASS G5 cargo deny (bans, licenses, sources)`: `api` and `pico2` are now MIT and `publish = false`, so the deny policy treats them as private path crates. `PASS G5 unsafe audit` also holds: the same 37 sites (block 16, fn 11, impl 1, extern 3, attribute 6, same items), 0 without SAFETY, 37 unsigned, which is a note until CDR. Run 2's FAIL items B1 and B2 therefore close on the branch. They close in the repository gate when the pin moves.
- **Decision 109 installs.** The five run 2 MISSING items are gone. G5 cargo audit and deny advisories PASS on the fetched database. G6 branch and condition coverage PASS on nightly `llvm-tools` (MSR-14: branches 4 of 4, lines 70 of 70, regions 70 of 70). G0 now uses the pinned `1.98.0`. The two remaining items are new FAILs, described next.
- **G5 complexity FAIL (two causes).**
  - (a) Invocation. `tools/sw_gate.sh` passes three paths to one `--paths` option, and `rust-code-analysis-cli` 0.0.25 accepts one value per occurrence. The analyzer exits with an argument error, and `tools/complexity_gate.py` reads empty input and stops with an input error.
  - (b) Convention. With one `--paths` per path (diagnostic, outside the gate, `complexity-diagnostic.txt`), the tool reports 52 functions, maximum CC 5, none above 12. It also reports one CS-38 failure, `cwht-app/src/main.rs:54 safe_state_halt CC 2`, because the analyzer counts a bare `loop` as a decision.
  - The lock sanity check shows the same convention difference on the complexity fixture. The analyzer counts every `match` arm and does not count `let ... else` (lock section 1.4 findings 9 and 10; TV-012 limitation 1).
  - Neither cause is a defect in the cwht or rustos code. Fixing (a) is a change to `tools/sw_gate.sh`. Fixing (b) is a decision for the 07 owner: accept the analyzer's counts or normalize them, and give CS-38 a rule for halt loops.
- **G5 Miri FAIL.** Miri on `nightly-2026-08-24` needs the `rust-src` component and a sysroot build that fetches std's dependency crates from crates.io. Neither is in decision 109, and the download guard refused `rustup component add rust-src` (D13). Closing it needs a new owner approval of those downloads. It then has to be seen whether `pico2`, whose code contains Arm instructions, builds under Miri on the host at all. That is not predicted here.
- **Reproducibility.** Two clean cwht-app builds and the gate build give one SHA-256. Two blinky builds give one SHA-256. Both UF2 files equal run 2, which shows the comment-only nature of the work item in the images (SWE-186 for the host tests by G3; NPR 7150.2D section 4.4.6).
- **Known-answer runs.** All nine match with the pinned toolchain in the loop. The G0, G1, G2 warning and G3 decisions still discriminate.

## 6. Data tables, plots and pictures

All data are text logs, scripts and images in `docs/vv/reports/TC-SW-TOOL-001-r3/`, listed with SHA-256 in the front matter. No plot or photograph is produced by steps 1 to 10. `run3.sh` and `gate-known-answer.sh` are the exact procedures run, and `rustup-guard.sh` is the D13 shim.

Gate result summary (`--keep-going`):

| Gate | PASS | FAIL | MISSING | SKIP |
|---|---|---|---|---|
| G0 | 1 | 0 | 0 | 0 |
| G1 | 3 | 0 | 0 | 0 |
| G2 | 5 | 0 | 0 | 0 |
| G3 | 3 | 0 | 0 | 0 |
| G4 | 1 | 0 | 0 | 0 |
| G5 | 7 (cargo audit; cargo deny; deny advisories; geiger 3; unsafe audit) | 2 (complexity; Miri) | 0 | 0 |
| G6 | 4 (stable coverage; branch and condition coverage; emulation stub; measurements) | 0 | 0 | 1 (emulation line) |

## 7. Non-conformances and discrepancies

| NCR | Severity | Step | Summary | Disposition | Retest planned |
|---|---|---|---|---|---|
| None | | | | | |

Status of the run 2 blocking items and the new ones (none is a defect of the cwht workspace or the rustos branch):

| # | Gate line | Run 3 status | Closes on | Owner |
|---|---|---|---|---|
| B1 | `G5 cargo deny (bans, licenses, sources)` | PASS on the branch | the owner's merge of the branch and the CR that moves the lock pin | Robin (rustos maintainer, CCB) |
| B2 | `G5 unsafe audit` | PASS on the branch | the same merge and CR; `firmware/unsafe-audit.md` is regenerated with `--write` in that CR's commit | Robin; Claude regenerates the list |
| B3 | `G5 cargo audit`, `G5 cargo deny advisories` | PASS (decision 109) | closed | none |
| B4 | `G5 complexity` | installed (decision 109), now FAIL (B8, B9) | B8 and B9 | see B8, B9 |
| B5 | `G5 Miri`, `G6 branch and condition coverage` | coverage PASS; Miri FAIL (B10) | B10 | see B10 |
| B6 | G0 pinned toolchain | closed (decision 109) | closed | none |
| B7 | steps 11 and 12 | performed with the owner 2026-09-26 19:17 to 19:20 on byte-identical UF2 files (minutes); raw outputs to run 4 | run 4 filing | Claude |
| B8 | `G5 complexity` (invocation) | FAIL: one `--paths` for three paths | a `tools/sw_gate.sh` change: one `--paths` per path | `tools/sw_gate.sh` maintainer |
| B9 | `G5 complexity` (convention) | CS-38 FAIL on `safe_state_halt` (bare `loop` is CC 2) | the 07 owner's CC convention for CS-17 and CS-38 and a halt-loop rule, then TV-012 re-derived | 07 owner (Claude), Robin as CCB |
| B10 | `G5 Miri` | FAIL: `rust-src` absent, sysroot crates not fetched | a new owner approval of `rust-src` on `nightly-2026-08-24` and of the Miri sysroot crate download | Robin |

## 8. Status of enabling equipment after the run

- cwht repository: unchanged by the run. The layout was a `git archive` in the scratch area and was deleted.
- rustos: the owner's checkout is unchanged (the same `HEAD` `c54d35a`, the same uncommitted work of the owner's own). The new worktree `/Users/robinonsay/rust/rustos-wp-sw-licence` and branch `cwht/wp-sw-licence-manifest-safety` remain for the owner's review.
- Toolchains: as installed under decision 109. The two `rust-src` downloads by cargo-miri were removed, and rustup is 1.29.1 by its own self-update (lock section 1.4 findings 7 and 8).

## 9. Conclusions and recommendations

Verdict: Blocked. On the rustos branch every gate step passes except two. G5 complexity fails on a gate invocation defect and an analyzer counting convention. G5 Miri fails because its component is absent. The five MISSING items and the two FAILs of run 2 are closed by decisions 109 and 110, the latter only on the branch. The FW-B0 exit criterion (gate exit 0) is not met. No requirement status changes (dev-board case, `credit: false`).

Recommendations:

1. Owner, as rustos maintainer: review and merge `cwht/wp-sw-licence-manifest-safety` (`2ec64c0`), then approve the CR that moves the `tools/toolchain.lock.md` section 3 pin and regenerates `firmware/unsafe-audit.md` (B1, B2).
2. Owner: rule on the `rust-src` and Miri sysroot downloads (B10), and accept rustup 1.29.1 or direct a reinstall of 1.29.0 (lock section 1.4 finding 7).
3. `tools/sw_gate.sh` maintainer: pass one `--paths` per path to `rust-code-analysis-cli`, and set `CARGO_NET_OFFLINE=true` for the audit step (B8; lock section 1.4 findings 10 and 11).
4. 07 owner: fix the CC counting convention for CS-17 and CS-38 and a rule for halt loops (B9); TV-012 then re-derives its fixture from real analyzer output.
5. Claude: file run 4 with the OA-1 and OA-2 raw outputs (minutes), and re-run the gate after items 1 to 4.

Deferrals FD-1 and FD-2 of run 1 stand unchanged.

## 10. As-run procedure

Steps 1 to 10 and 13 as written in `docs/test_cases/sw-tool/test_cases.json` (blob `fee1e724`, unchanged). They were run by `run3.sh` and `gate-known-answer.sh` with deviations D1 to D15 of section 2, and step 5 ran as gate G1 within step 6. Steps 11 and 12 were not run in this run (section 4).

## 11. Answers to INSP-016 findings (author response for the reviewer's next iteration)

INSP-016 (`docs/reviews/SRR/checklists/fw-b0-toolchain-proof.md`) had two open Major findings on rulings. The reviewer, not the author, changes the record.

| Finding | Severity | Author response | What closes it |
|---|---|---|---|
| finding-1 | Major | Decisions 109 and 110 are carried out. The installs are made and recorded, and the lock section 1.1 sanity checks are run and recorded: pass for rustc, cargo and clippy on `1.98.0`, cargo-llvm-cov, nightly coverage, cargo-nextest, cargo-audit, cargo-deny, cargo-geiger and cargo-binutils; fail for rust-code-analysis-cli on the counting convention; Miri blocked. The rustos work item is on its branch. On that branch the gate has 0 MISSING and 2 FAIL (B8 to B10). OA-1 is done (minutes). | B8 to B10, the owner's merge and pin CR (B1, B2), then a gate exit 0 |
| finding-2 | Major | CR-001 approved as SRR decision 108 and applied to 07 (`4364ebb`); the `main.rs` comment still names the pending disposition (D8, cross item) | Reviewer verification of the CR-001 application |

## 12. Authentication and authorization

- Results authenticated by (conductor): claude, 2026-09-26
- Witnessed by: owner, not applicable to run 3 (no owner-performed step; the owner witnessed steps 11 and 12 on the byte-identical images at 19:17 to 19:20, recorded in the SRR minutes and filed with run 4)
- Authorization of acceptability (owner): pending
