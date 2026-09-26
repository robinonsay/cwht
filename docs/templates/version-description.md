---
release: FW-vX.Y.Z
version: X.Y.Z
tag: release/FW-vX.Y.Z
commit: <full SHA of the source commit S, which the tag points to (CM plan §8.1 step 2)>
embedded_version: vX.Y.Z+<short S>          # as printed by the build (CM plan §4.3); copied, never recomputed
release_date: YYYY-MM-DD
build_date: YYYY-MM-DD
builder: <machine (sw_vers, uname -m) and user (id -un)>
target: thumbv8m.main-none-eabihf
board: Raspberry Pi Pico 2 (RP2350) on cwht mainboard HW-MB-rev<X>
hardware_compatibility: [HW-MB-rev<X>-<n>]
previous_release: FW-vX.Y.Z-1 | none
release_type: <internal candidate | for test | accepted>
rustos_commit: <full SHA>
toolchain_lock_commit: <SHA of the last commit touching tools/toolchain.lock.md at S>
requirements_baseline: <baseline tag of the requirement set, e.g. baseline/pdr>
design_baseline: <baseline tag of the design set, e.g. baseline/cdr, or none>
status: Draft            # Draft | Reviewed | Approved
---

# Version Description: cwht firmware FW-vX.Y.Z

Template: `docs/templates/version-description.md`. Requirement: SWE-063 (a version description for each release), content per SWEHB 5.16 items a to j and 07 §13; procedure: `docs/process/05-configuration-and-data-management.md` §8.1. Location: `firmware/releases/VDD-vX.Y.Z.md`. Sections 1 to 8 are written before the artifacts commit A (§8.1 step 7) and are then immutable; section 9 is fill-once, written in the post-tag record commit (§8.1 step 11). Every file hash is SHA-256 and equals the `SHA256SUMS` file in `firmware/releases/vX.Y.Z/`.

## 1. Identification (SWEHB 5.16 a)

| Field | Value |
|---|---|
| Release identifier | FW-vX.Y.Z |
| Git tag (annotated; signed once the owner's key is configured, CM plan §4.4) and source commit S | `release/FW-vX.Y.Z` on `<S>`; the artifacts commit A and the tag verification output are in §9 |
| Firmware crate and `Cargo.toml` version | `<crate name>`, `X.Y.Z` |
| Embedded version string (`picotool info -a`) | program name `cwht`, version `vX.Y.Z+<short S>` |
| Compatible hardware releases | HW-MB-rev<X>-<n>; ME-ENC-rev<X>-<n> (if the enclosure affects firmware behaviour) |
| Effective baseline at release | `baseline/<cdr or sar>` plus CRs: <list> |
| Release type | <initial, feature (MINOR), fix (PATCH) or incompatible (MAJOR)>; <internal candidate, for test, or accepted> |

## 2. Inventory of released files (SWEHB 5.16 b, f, g)

| File (`firmware/releases/vX.Y.Z/`) | SHA-256 | Size (bytes) | Purpose |
|---|---|---|---|
| `cwht-FW-vX.Y.Z.elf` | | | Flash via `picotool load -u -x -t elf`; source for `picotool verify`; carries the CRC-32 trailer in its `.image_trailer` section |
| `cwht-FW-vX.Y.Z.uf2` | | | Drag-and-drop flashing in BOOTSEL mode (converted from the trailer-complete ELF) |
| `firmware.map` | | | Linker map (memory budget evidence) |
| `picotool-info.txt` | | | Read-back of binary info |
| `flavours/<flavour>/cwht-FW-vX.Y.Z-<flavour>.elf` and `.uf2` (one pair per test flavour, if built) | | | Instrumented or fault-injection build for credited Bench runs only; Cargo feature named here; never delivered on a unit (CM plan §8.1, build flavours) |
| `SHA256SUMS` | n/a (the manifest itself) | | Manifest of the files above (CM plan §8.1 step 4 e) |

| Image integrity (CM plan §8.1 step 4; 07 CS-32, SWE-134 f) | Value |
|---|---|
| CRC-32 trailer (IEEE 802.3, over the image bytes preceding the `.image_trailer` section) as printed by `tools/image_trailer.py write` | `0x________` |
| Trailer check at boot | verified by `TC-SW-BOOT-*` on this release: report path |
| Flash and RAM usage (MSR-18, MSR-19, from `firmware.map`) | <bytes used of bytes available> |

## 3. Inventory of software contents and life-cycle data (SWEHB 5.16 c; 07 §13)

| Item | Identification |
|---|---|
| Firmware crate sources | `firmware/` at S; tree hash `git rev-parse <S>:firmware` |
| `Cargo.lock` | blob hash `git ls-tree <S> -- firmware/Cargo.lock`; dependency list with versions from `cargo tree --locked` pasted below |
| `rustos` (reused software) | commit `<SHA>` (path dependency); remote `git@github.com:robinonsay/rustos.git`; differences from the previous VDD's commit summarised; third-party register row of 07 §17.1 |
| Third-party crates (reused software) | one row each from `Cargo.lock`: name, version, licence, purpose, in image yes or no; policy: zero external crates in the image (07 §17.1) |
| SWE-203 advisory review | `cargo audit` and RustSec review result for this `Cargo.lock`, date, advisories found and their disposition |
| Linker script and memory layout | `link.ld` origin (rustos commit), flash and RAM sizes |
| Generated tables (07 §17.4) | file, generator, size, blob hash; or None |
| Life-cycle data defining this version | requirements baseline tag; design baseline tag; test case set commit (`git log -1 --format=%H <S> -- docs/test_cases`); traceability report commit and path |

Safety-critical and mission-critical components (one row per module of 07 §14.1, the single authoritative list, charter §10; add a row if 07 §14.1 adds a module):

| Module | Class (07 §14.1) | Decision-table and independence-pair record (`INSP-NNN`, 07 §9.6) | Stable region coverage, credit (MSR-13) | Nightly branch and condition coverage, non-credit (MSR-14, `nightly-2026-08-24`) | Max cyclomatic complexity (SWE-220 limit 15; general rule 07 §7.4 for mission-critical) |
|---|---|---|---|---|---|
| SW-KEYER | safety-critical | | | | |
| SW-TXSEQ | safety-critical | | | | |
| SW-PWR | safety-critical | | | | |
| SW-SAFE (thermal monitor and safe-state manager) | safety-critical | | | | |
| SW-AUDIO | safety-critical | | | | |
| SW-BOOT | safety-critical | | | | |
| pico2 drivers (GPIO, TIMER, PWM, ADC, watchdog, critical section) | safety-critical | | | | |
| SW-SYNTH | mission-critical | n/a (SWE-219 does not apply, 03 §4.3) | | n/a | |
| SW-CFG | mission-critical | n/a (SWE-219 does not apply, 03 §4.3) | | n/a | |
| SW-DISPLAY | mission-critical | n/a (SWE-219 does not apply, 03 §4.3) | | n/a | |

Coverage report: `docs/vv/reports/TC-SW-COV-001-r<N>.md`. Any shortfall or exceedance is listed in the §7 waivers table with its decision memo.

## 4. Build environment and instructions (SWEHB 5.16 d, e; from `tools/toolchain.lock.md` at S)

| Tool | Version | TV record |
|---|---|---|
| rustc | | |
| cargo | | |
| rustup active toolchain in `firmware/` (`rustup show active-toolchain`) | | covered by rustc TV |
| target | `thumbv8m.main-none-eabihf` | covered by rustc TV |
| clippy | | |
| picotool | | |
| llvm-tools / cargo-llvm-cov (coverage, 07 §8.1) | | |
| nightly-2026-08-24 (MSR-14 only, non-credit) | | |
| cargo-audit | | |
| cargo-deny | | |
| cargo-geiger | | |
| cargo-nextest | | |
| rust-code-analysis-cli (complexity, 07 §8.4) | | |
| tools/release.sh, tools/image_trailer.py | blob hashes at S | |
| OS | | n/a |

Rows follow the toolchain list of `docs/process/07-software-engineering-plan.md` §13. Write "not used in this release" for a tool that did not run; never leave a cell blank.

| Build fact | Value |
|---|---|
| Build date and time | YYYY-MM-DD HH:MM (local) |
| Builder machine and user | <`sw_vers -productVersion`, `uname -m`, `id -un`> |

Environment settings in force for the build (SWE-081 note: compiler versions and environment settings):

| Setting | Value |
|---|---|
| `RUSTFLAGS` | <value or unset> |
| Other `CARGO_*` and `RUST*` variables (`env \| grep -E '^(CARGO\|RUST)'`) | <list or none> |
| `CWHT_BUILD_ID` | `vX.Y.Z+<short S>` |
| `firmware/.cargo/config.toml` | blob hash `git ls-tree <S> -- firmware/.cargo/config.toml` |
| `firmware/rust-toolchain.toml` | blob hash `git ls-tree <S> -- firmware/rust-toolchain.toml` |
| Release profile settings (07 CS-04) | <opt-level, lto, codegen-units, debug, panic, from `Cargo.toml`> |

Exact build commands as printed by `tools/release.sh X.Y.Z` (CM plan §8.1 steps 3 and 4), with every working-directory change explicit:

```
cd /Users/robinonsay/rust/cwht/firmware
CWHT_BUILD_ID=vX.Y.Z+<short S> cargo build --release --locked --target thumbv8m.main-none-eabihf -p cwht-app
cd /Users/robinonsay/rust/cwht
cp firmware/target/thumbv8m.main-none-eabihf/release/cwht-app firmware/releases/vX.Y.Z/cwht-FW-vX.Y.Z.elf
.venv/bin/python tools/image_trailer.py write firmware/releases/vX.Y.Z/cwht-FW-vX.Y.Z.elf        # prints the CRC-32 recorded in §2
cd /Users/robinonsay/rust/cwht/firmware/releases/vX.Y.Z
picotool uf2 convert cwht-FW-vX.Y.Z.elf cwht-FW-vX.Y.Z.uf2 --family rp2350-arm-s
picotool info -a cwht-FW-vX.Y.Z.elf > picotool-info.txt
shasum -a 256 *.elf *.uf2 *.map picotool-info.txt > SHA256SUMS
```

Regeneration and reproducibility check (SWEHB 5.16 e; CM plan §8.1 step 6; 07 §13): `tools/release.sh --rebuild-check X.Y.Z` run from `/Users/robinonsay/rust/cwht` at S on YYYY-MM-DD after `cargo clean`; every hash <equal | not equal (NCR-NNN)>.

## 5. Changes since the previous release (SWEHB 5.16 i)

| Type | ID | Title | Effect on operator or hardware |
|---|---|---|---|
| CR | | | |
| NCR closed | | | |
| Requirement added/changed | REQ- | | |

Requirements volatility contribution of this release (CM plan §5.4): <n added, n modified, n retired of N>.

## 6. Verification status of this release

| Item | Evidence |
|---|---|
| Gate log | `tools/sw_gate.sh` exit 0 at S: log path |
| Traceability report at S | `<path>`; result clean |
| HostUnit tests | report `<docs/vv/reports/...>`; pass/fail counts (MSR-23) |
| Emulation scenarios | report path; scenarios passed |
| Regression | `TC-SW-REG-001` report path |
| Bench / OnAir tests (if run on this exact release) | report paths, TC ids |
| Requirements implemented and verified by this release | every `REQ-SW-*` allocated to the release with its status (Verified, Closed, or dispositioned with the CR id), or reference to the verification matrix at S |
| Requirements deferred to a later release | REQ id, target release, deferring CR or decision memo; or None |
| Security and coding-standard confirmation (SWEHB 5.16 j) | `cargo audit` (no unresolved advisory), `cargo deny check` (licences, bans, advisories), `cargo geiger` and `tools/unsafe_audit.py --check` (every unsafe site signed), `clippy -D warnings` under the coding-standard lint configuration (07 §7, Annex B), complexity gate: results with dates, all from gate G5 of `tools/sw_gate.sh` at S |
| SWE-194 pre-delivery check (CM plan §8.1 step 1) | (a) every `REQ-SW-*` allocated to this release is Verified or Closed, or dispositioned by an approved CR (`tools/traceability.py` on `rel/FW-vX.Y.Z`): yes/no; (b) all targeted CRs Closed or re-dispositioned by the owner: yes/no; (c) all designated NCRs Closed: yes/no. For a candidate: (a) reads "every allocated requirement implemented" (CM plan §8.1 step 1 a) |

## 7. Known problems, open items and limitations (SWEHB 5.16 h)

Open NCRs:

| NCR | Severity | Description | Operator impact | Workaround | Planned fix (CR or release) |
|---|---|---|---|---|---|
| | | | | | |

Open CRs affecting this release (not implemented in it):

| CR | Status | Title | Operator impact | Workaround | Target release |
|---|---|---|---|---|---|
| | | | | | |

Waivers in force for this release (CM plan §2 product waiver; CSA item 12):

| Waiver id (`CR-NNN` or `<memo path>#W<n>`) | Requirement or target (REQ id, SWE-219 or SWE-220 with module) | Rationale | Approving decision memo or CR | End condition |
|---|---|---|---|---|
| | | | | |

| Item | Value |
|---|---|
| Deactivated code (07 §9.5) | every deactivated item: file and function, activating configuration, reason; or None |
| Other limitations | |

## 8. Installation, read-back and first boot (SWEHB 5.16 b, e)

1. Hold BOOTSEL while connecting USB; confirm the device with `picotool info`.
2. From `/Users/robinonsay/rust/cwht`: `picotool load -u -x -t elf firmware/releases/vX.Y.Z/cwht-FW-vX.Y.Z.elf` (or copy the `.uf2` to the RP2350 volume).
3. Re-enter BOOTSEL; `picotool verify firmware/releases/vX.Y.Z/cwht-FW-vX.Y.Z.elf` must report a match; `picotool info -a` must show `vX.Y.Z+<short S>`.
4. Expected first-boot behaviour: the radio enters SafeState, then Receive; a fault code is shown if any start-up check fails (07 §13); a corrupted image trailer is refused and the unit stays in SafeState with its fault code (07 §9.7).
5. Record the result in the unit's `docs/vv/adp/CWHT-A-NNN/as-built.md`, including the line `Installed release: vX.Y.Z+<short S>; picotool verify match; YYYY-MM-DD` (CM plan §8.3 step 2).

## 9. Review, approval and tag verification (fill-once, CM plan §8.1 step 11)

| Step | By | Date | Result |
|---|---|---|---|
| Independent review of this VDD against the template and the release directory at the artifacts commit | <reviewer agent> | | |
| Owner release approval (for a candidate: approval to test), transcribed from chat or written directly | Owner | | Approved |
| Artifacts commit A (`release(fw): artifacts FW-vX.Y.Z`) | Claude | | `<SHA>` |
| `git tag -v release/FW-vX.Y.Z` (signed) or `git cat-file -p release/FW-vX.Y.Z` (unsigned) output | Claude | | <paste below> |
| `git ls-remote --tags origin release/FW-vX.Y.Z` after push | Claude | | <hash> |

```
<verbatim tag verification output>
```

Reviewer checklist: every front-matter field filled; every file in the release directory listed with a matching hash; `commit` equals the tag's target (`git rev-parse release/FW-vX.Y.Z^{commit}`); `git diff --name-only <S> <A>` lists only the release directory and this VDD; `rustos` commit and `Cargo.lock` hash equal those at S; build environment equals `tools/toolchain.lock.md` at S; one row per 07 §14.1 module in §3; every CR listed in §5 is Closed; every open NCR and open CR affecting the release appears in §7; every waiver in CSA item 12 that affects the release appears in §7; installation steps tested on one unit.
