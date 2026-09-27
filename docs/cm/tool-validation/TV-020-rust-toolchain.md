# TV-020: Rust toolchain 1.98.0 (rustc, cargo, clippy)

| Field | Value |
|---|---|
| Record | TV-020 |
| Status | **Validated** (2026-09-27, runs 1 and 2 at commit `d3de579`; runs 3 and 4 at commit `c28dd60` on the restated purpose 4 and the mechanical K20-4 and K20-5 criteria, after review INSP-040 iteration 1 finding-1). Independent review (delta iteration), software assurance review and owner accreditation pending (sections 8 and 9) |
| Class | A for `rustc` and `cargo build` (the firmware image; CM plan section 9.1); B for `cargo test` and `clippy` (HostUnit and static-analysis evidence) |
| Governs | SWE-136 (NPR 7150.2D section 4.4.8), SWE-070 (section 4.5.6) through CM plan section 9; 07 sections 8.3 and 17.3 (toolchain accreditation: sanity checks, MSR-28, byte-identical rebuild of the rustos blinky, HostUnit suite twice identical); SWE-135 and SWE-061 through clippy and the lint table of 07 Annex B |
| Due | PDR (CM plan section 13 PDR row: "the Rust toolchain (`rustc`, `cargo`, `clippy`, ...)"; `tools/toolchain.lock.md` section 5) |
| Lock rows | `tools/toolchain.lock.md` section 1 rows rustc, cargo, rustup active toolchain, rustup installed targets, rustup components (stable); section 1.1 rows rustc / cargo and clippy; section 1.3; section 7 row Rust 1.98.0 |
| Work package | WP-PDR-08 (`docs/plan/pdr-work-plan.md` section 3.3) |
| Author | Claude, software lead and tool owner |

07 section 17.3 names this record `TV-NNN-rustc.md`; the PDR work plan names it `TV-020-rust-toolchain.md` because it covers `cargo` and `clippy` too. The two names designate this file.

**Reading of 07 section 17.3 "byte-identical rebuild of the rustos blinky" in this record (INSP-040 finding-1).** It means two clean rebuilds of the blinky from the same source at one absolute path give byte-identical ELF files and byte-identical loadable images (K20-4). It does not mean a rebuild at an arbitrary path reproduces the committed reference `docs/vv/reports/TC-SW-TOOL-001-r3/rustos-blinky.elf`: that ELF, and the order of functions in its loadable image, are reproducible only at the absolute path it was built at (limitation 1). The same reading applies to MSR-28 (K20-5). The matching wording change of 07 section 17.3 is a cross item of WP-PDR-08 for the 07 writer of plan section 5.3.

## 1. Identification

| Item | Value | Command |
|---|---|---|
| Toolchain | `1.98.0-aarch64-apple-darwin`, selected in `firmware/` by `firmware/rust-toolchain.toml` (blob `ca29c254`; channel `1.98.0`, components clippy, rustfmt, llvm-tools, target `thumbv8m.main-none-eabihf`, profile minimal) | `cd firmware && rustup show active-toolchain` gives `1.98.0-aarch64-apple-darwin (overridden by '.../firmware/rust-toolchain.toml')` |
| rustc | `rustc 1.98.0 (88d9e12ae 2026-08-18)`, commit-hash `88d9e12ae178fab0fb5cc050a94da85685d449ea`, LLVM 22.1.8 | `rustc +1.98.0 --version`; `rustc +1.98.0 -vV` |
| cargo | `cargo 1.98.0 (797e8a9bc 2026-08-05)` | `cargo +1.98.0 --version` |
| clippy | `clippy 0.1.98 (88d9e12ae1 2026-08-18)` | `cargo +1.98.0 clippy --version` |
| rustup | `rustup 1.29.1 (d95a37b6a 2026-08-13)`, auto-self-update disabled (lock section 1, owner acceptance 2026-09-26) | `rustup --version` |

**Install source:** rustup, dated channel `1.98.0`, installed 2026-09-26 19:18 to 19:19 CDT by `rustup toolchain install 1.98.0 --profile minimal --component clippy,rustfmt,llvm-tools --target thumbv8m.main-none-eabihf` (SRR decision 109, owner ruling 2026-09-26; lock section 1.3). Upstream manifest `https://static.rust-lang.org/dist/channel-rust-1.98.0.toml`; rustup verified every component against the SHA-256 values in that manifest at installation. Installed copy of the manifest (`lib/rustlib/multirust-channel-manifest.toml`): SHA-256 `b17aaaeded2ac77b968b406613ec319b001f105793900a6f852a72a03e241ba9` (lock section 7, re-observed 2026-09-27).

**Binaries** (`~/.rustup/toolchains/1.98.0-aarch64-apple-darwin/bin/`, SHA-256 observed 2026-09-27 in section 0 of both runs):

| Binary | SHA-256 |
|---|---|
| `rustc` | `a11618eca0956a8aa4372c2bc898690b513cbdfa2cb9125b2a5301e360ed5b49` |
| `cargo` | `1de2e84c15443b70444eecfa959ff9099dd8c1a5606b6d9ef5bc0ea9c25bc7f9` |
| `clippy-driver` | `6a1ccc398ad5466587424fd97625bad2a9296d4ef031a853b99eb80362f6e1e9` |
| `cargo-clippy` | `bf89162b33afa0518da4004ab5f0e13f5b5cd143e6349a1720a003944910837b` |

**Fixtures and procedure** (git objects at commit `d3de579` for runs 1 and 2, the fixtures committed in `a3cacee` and the procedure fixed in `d3de579`; at commit `c28dd60` for runs 3 and 4, where only `pdr-known-answers.json` and the new procedure differ, `git diff --stat d3de579 c28dd60` on `kat-target`, `kat-host`, `known-answers.json` and `firmware/` being empty):

| Path | Git object | Role |
|---|---|---|
| `tools/tests/fixtures/rust/kat-target/` | tree `1eae87cd` | no_std image for `thumbv8m.main-none-eabihf` (SRR fixture, unchanged) |
| `tools/tests/fixtures/rust/kat-host/` | tree `d70d2554` | host library with the project lint tables; features `seeded-fail`, `seeded-lint`, `seeded-unwrap` (SRR fixture, unchanged) |
| `tools/tests/fixtures/rust/known-answers.json` | blob `6311da66` | stored answers of the two fixtures above |
| `tools/tests/fixtures/rust/pdr-known-answers.json` | blob `0e7d72ac` (runs 1 and 2); blob `00256755` (runs 3 and 4, commit `c28dd60`: sections `rustos-blinky` and `cwht-app` restated as same-path criteria with the cross-path comparison as an observation) | stored answers of the blinky and `cwht-app` checks (sections `rustos-blinky`, `cwht-app`) |
| `docs/cm/tool-validation/evidence/rust-tv-2026-09-27.sh` | blob `4c7cb753` | the procedure of runs 1 and 2 (sections 0 to 6 are this record's) |
| `docs/cm/tool-validation/evidence/rust-tv-2026-09-27-r3.sh` | blob `42ad521a` (commit `c28dd60`) | the procedure of runs 3 and 4: sections 0 to 8 of the first procedure, with sections 4 and 5 printing mechanical PASS or FAIL lines for the same-path criteria and OBSERVATION lines for the layout B build and the reference |
| `firmware/Cargo.toml`, `firmware/Cargo.lock`, `firmware/clippy.toml` | blobs `7799f6b6`, `784605ca`, `42020b54` | the workspace, lock file and lint configuration built and tested |
| rustos | commit `2ec64c0f15c8cd2dbcaa241abffdd72f8cae467c` (lock section 3 pin), exported with `git archive` from the commit object | `api`, `firmware/pico2`, `templates/pico2` |

## 2. Purposes covered

1. `rustc` and `cargo build --release --locked` compile the firmware image crates for `thumbv8m.main-none-eabihf` with the CS-04 release profile (class A: the image of every release).
2. `cargo test` builds and runs the host tests of the host-compilable crates (HostUnit, charter section 9), as the reference runner; a failing test makes it exit non-zero and name the test (class B). The credited runner of gate G3 is `cargo-nextest` (TV-022).
3. `cargo clippy` with the project lint configuration (`firmware/Cargo.toml` `[workspace.lints]` and `firmware/clippy.toml`, 07 Annex B) reports every lint of the table as an error under `-D warnings` (MSR-07; SWE-135 defects item; CS-27) (class B).
4. Build reproducibility at one absolute path (MSR-28; 07 section 17.3; `tools/release.sh --rebuild-check`): two clean builds of the same source at the same absolute path, in different target directories, give byte-identical ELF files and byte-identical loadable images (`rust-objcopy -O binary`). Identity across different absolute paths is not claimed (limitation 1); builds at a second path and the committed references are compared as observations only.

## 3. Known-answer test

Run on `git archive` exports of the commit tested, layout A `<scratch>/A/{cwht,rustos}` and layout B `<scratch>/B/x/{cwht,rustos}`, offline (`CARGO_NET_OFFLINE=true`, `RUSTUP_AUTO_INSTALL=0`) with the rustup shim of TC-SW-TOOL-001 run 3 deviation D13 first on `PATH`, so no check can download. Runs 1 and 2 used the first procedure; runs 3 and 4 and every later run use the second, whose K20-4 and K20-5 criteria are mechanical (INSP-040 finding-1):

```
sh docs/cm/tool-validation/evidence/rust-tv-2026-09-27.sh <scratch> <guard-dir> <commit>      # runs 1 and 2
sh docs/cm/tool-validation/evidence/rust-tv-2026-09-27-r3.sh <scratch> <guard-dir> <commit>   # runs 3 and 4 onward
```

| Id | Check (procedure section) | Pass criterion |
|---|---|---|
| K20-1 | `kat-target`: three `cargo +1.98.0 build --release --locked` in three target directories, one of them in layout B (section 1) | three ELF SHA-256 values identical and equal to the stored `3201d382b9b1e32ec69da84ae966fd40671ecd820e32de6ef3135fb69f66df7d` |
| K20-2 | `kat-host`: `cargo +1.98.0 test --locked`, then `--features seeded-fail` (section 2) | clean exit 0 with 3 passed; seeded exit 101 naming `tests::seeded_failure`, 3 passed and 1 failed |
| K20-3 | `kat-host`: `cargo +1.98.0 clippy --locked --all-targets -- -D warnings` clean, `--features seeded-lint`, `--features seeded-unwrap` (section 3) | clean exit 0; `seeded-lint` exit 101 with exactly `clippy::absurd_extreme_comparisons` (correctness group); `seeded-unwrap` exit 101 with exactly `clippy::unwrap_used`, which clippy allows by default, so the project lint table is shown in force |
| K20-4 | rustos blinky: `templates/pico2` of the pin with the three-line `Cargo.toml` diff of `docs/vv/reports/TC-SW-TOOL-001-r3/blinky-build.txt`, two clean builds in layout A (target directories `b1`, `b2`) and one in layout B (section 4) | pass criteria, each a `cmp` printed as a PASS or FAIL line: K20-4a the two layout A ELF files byte-identical; K20-4b the two layout A loadable images (`rust-objcopy -O binary`) byte-identical. Observations, printed and recorded but never a pass criterion: the layout B loadable image and the loadable image of the reference `docs/vv/reports/TC-SW-TOOL-001-r3/rustos-blinky.elf` (`c6d27ba1...31df`, 2008 bytes) against layout A, and their allocated-section tables (`rust-size -A`, name and size) against layout A |
| K20-5 | MSR-28: `cwht-app` `cargo +1.98.0 build -p cwht-app --release --locked --target thumbv8m.main-none-eabihf`, two clean builds in layout A (target directories `a1`, `a2`) and one in layout B (section 5) | pass criteria, each a `cmp` printed as a PASS or FAIL line: K20-5a the two layout A ELF files byte-identical; K20-5b the two layout A loadable images byte-identical. Observations, never a pass criterion: the layout B loadable image and the loadable image of the FW-B0 reference `docs/vv/reports/TC-SW-TOOL-001-r3/cwht-app.elf` (built at `0bcea39`; `firmware/` sources unchanged since, only `firmware/unsafe-audit.md` differs; `828bca35...61f4`) against layout A, and their allocated-section tables against layout A |
| K20-6 | HostUnit suite twice (07 section 17.3; SWE-186): `cargo +1.98.0 nextest run --locked --workspace --exclude cwht-app --profile ci` twice, and `cargo +1.98.0 test --locked --workspace --exclude cwht-app` twice (section 6) | both nextest runs 10 passed; the (classname, name, outcome) sets of the two JUnit files identical and all passed, by an independent stdlib comparison and by `tools/measurements.py --diff-runs`; the sorted `cargo test` outputs of the two runs identical |

## 4. Result

| Run | Date and time (CDT) | Commit tested | Result |
|---|---|---|---|
| Lock sanity checks (history) | 2026-09-25 23:28 and 23:29 (`+stable`, equal to 1.98.0); 2026-09-26 19:44 (`+1.98.0`) | `28e49e6`; `bfea9c7` | K20-1 to K20-3 pass (lock section 1.1 rows rustc / cargo and clippy; `evidence/rust-2026-09-25.log.txt`, `evidence/rust-tools-2026-09-26.log.txt` section 1) |
| 1 | 2026-09-27 10:53:42 to 10:54:04 | `d3de579` (export) | **pass**: K20-1 three ELF `3201d382...df7d` equal to the stored value; K20-2 clean 3 passed exit 0, seeded exit 101 `tests::seeded_failure`; K20-3 clean exit 0, `absurd_extreme_comparisons` exit 101, `unwrap_used` exit 101; K20-4 layout A ELF `4685cbfa...` twice, layout B ELF `a32fae1f...`, the three loadable images `c6d27ba1...31df` equal to the reference; K20-5 layout A ELF `b5bb665a...` twice, layout B ELF `2201af96...`, the three loadable images `828bca35...61f4` equal to the reference; K20-6 nextest 10 passed twice, 10 identical triples, all passed, `measurements.py --diff-runs` "PASS identical result sets, all passed (SWE-186)", `cargo test` outputs identical (16 lines) |
| 2 | 2026-09-27 10:54:05 to 10:54:26 | `d3de579` (export, second scratch root) | **pass**, every result equal to run 1 except the ELF hashes of K20-4 and K20-5, which depend on the absolute build path (limitation 1): K20-4 layout A `c17844ce...` twice, layout B `accd1699...`, loadable images `c6d27ba1...31df`; K20-5 layout A `cda502de...` twice, layout B `8dc64084...`, loadable images `828bca35...61f4` |
| 3 | 2026-09-27 11:54:23 to 11:54:36, procedure `rust-tv-2026-09-27-r3.sh` | `c28dd60` (export, scratch root `r3`) | **pass** on the restated criteria: K20-1 three ELF `3201d382...df7d` equal to the stored value; K20-2 and K20-3 as runs 1 and 2; K20-4a and K20-4b PASS (layout A ELF `643d56aa...` twice, loadable images `c6d27ba1...31df` twice); K20-5a and K20-5b PASS (layout A ELF `a7903b8f...` twice, loadable images `828bca35...61f4` twice); K20-6 nextest 10 passed twice, triples identical, all passed, `measurements.py --diff-runs` PASS, `cargo test` outputs identical. Observations: K20-4 layout B loadable image `7c20cba4...6857` **differs** from layout A (section tables equal, 2008 bytes), the reference loadable image equal to layout A; K20-5 layout B and reference loadable images equal to layout A, section tables equal |
| 4 | 2026-09-27 11:54:37 to 11:54:50, same procedure | `c28dd60` (export, scratch root `r4`) | **pass**, every PASS line and every observation equal to run 3; the ELF hashes differ from run 3 because the absolute path differs (K20-4 layout A `5e8fe954...` twice; K20-5 layout A `f0f6a5f8...` twice), the loadable images equal to run 3 |

Evidence: `docs/cm/tool-validation/evidence/rust-tv-2026-09-27.log.txt` (runs 1 and 2, sections 0 to 6; the appendix holds the dry run of 10:50 on a scratch clone whose blinky loadable image differed, limitation 1); `docs/cm/tool-validation/evidence/rust-tv-2026-09-27-r3.log.txt` (runs 3 and 4, sections 0 to 6). Runs 1 and 2 were judged against the earlier K20-4 criterion, whose escape clause ("or, where it differs, differing only by function order") made it a hand judgement; INSP-040 finding-1 withdrew that criterion, and runs 3 and 4 are the credit runs for purpose 4.

## 5. Reproducibility (class A)

Same absolute path: pass in runs 1 to 4 for `kat-target`, blinky and `cwht-app` (byte-identical ELF from two clean target directories), and in runs 3 and 4 also for the loadable images by the mechanical K20-4b and K20-5b checks. Across paths: the `kat-target` ELF is identical in every directory (no debug information, no path dependency); for the blinky and `cwht-app` neither the ELF nor the loadable image is claimed identical (limitation 1), and runs 3 and 4 observed a blinky loadable image at layout B that differs from layout A. The class A criterion of CM plan section 9.2 step 1 ("run twice, identical output hash") is met for the ELF and the loadable image at one absolute path, which is the condition of ACC-RUST-001.

## 6. Limitations

1. **The ELF depends on the absolute build path.** The `cwht-app` release profile keeps debug information (`[optimized + debuginfo]`), which names the build path (7 strings in the layout A image). For the rustos blinky, the crate disambiguator hashes in the symbol names (for example `_RNvCs9Bc0GV4RA3w_5pico2...` against `_RNvCs225Rjk9CTJ1_5pico2...`) are derived from the absolute path of each path dependency, and the linker orders functions by symbol, so a build at another path can swap `main` and `rust_begin_unwind`: same section sizes, different bytes. The dry run of 10:50 shows it (evidence appendix: layout A loadable `7c20cba4...` against `c6d27ba1...` for layout B and the reference). Runs 3 and 4 show it again (layout B blinky loadable `7c20cba4...` against `c6d27ba1...` at layout A), and the reviewer's run of INSP-040 showed it at both of its layouts. Consequence for purpose 4, MSR-28 and `tools/release.sh --rebuild-check` (CM plan section 8.1, due before the first release candidate): the release and its rebuild are made at one fixed absolute path, and the ELF, loadable image and UF2 are compared there; a rebuild at another path is not a valid MSR-28 check and is not covered by ACC-RUST-001. `cwht-app` takes the rustos `api` crate by path (`firmware/Cargo.toml`), so the same mechanism applies to it; its loadable image was equal across paths in runs 1 to 4, which is chance, not a property of the tool.
2. MSR-28 is defined against "the release hash" (07 section 11.2). No release exists yet (the first candidate is FW-B2), so K20-5 uses the FW-B0 image of TC-SW-TOOL-001-r3 as the reference. The check is repeated on every release by `tools/release.sh` once written.
3. 07 section 8.3 expects "the committed `blinky.elf`" of rustos. The rustos pin `2ec64c0` holds no ELF (its tree has only the `templates/pico2` sources); the reference is the cwht evidence file `docs/vv/reports/TC-SW-TOOL-001-r3/rustos-blinky.elf`, built from the same pin on 2026-09-26.
4. The HostUnit suite at this commit is the FW-B0 set (10 tests in `cwht-core` and `cwht-hal-mock`; no `REQ-SW-*` is verified yet). K20-6 shows the toolchain property (two runs identical), not the suite's adequacy, which is the business of the coverage report (TC-SW-COV-001) at each release.
5. The installation is verified by rustup's manifest check at install time and by the recorded binary hashes; the binaries were not re-downloaded and compared (no download is approved for that).
6. Ferrocene is an option (07 section 8.1), not adopted for Rev A. 07 section 17.3 says the option is recorded "in the accreditation ADR"; no such ADR exists and none is assigned by the PDR work plan (cross item of WP-PDR-08).
7. Output is developer evidence until section 9 records the accreditation (CM plan section 9.1).

## 7. Re-validation triggers

- Any change of the toolchain: a new `rustc`, `cargo` or `clippy` version, a component added or removed, a change of `firmware/rust-toolchain.toml` (after accreditation a CR, Class I, CM plan section 5.1 row "Version change of an Accredited tool").
- A change of the fixtures `kat-target`, `kat-host`, `known-answers.json` or `pdr-known-answers.json`; a change of the lint configuration (`firmware/Cargo.toml` `[workspace.lints]`, `firmware/clippy.toml`) for purpose 3.
- A move of the rustos pin (lock section 3) for K20-4 and K20-5.
- A macOS major version change (CM plan section 9.2 step 4); each new baseline (class A expiry: re-run section 3 and append the result).
- A defect found in the tool (an NCR per SWE-201).

## 8. Independent review (CM plan section 9.2 step 3)

| Iteration | Date | Record and reviewer | Verdict | Majors | Author action |
|---|---|---|---|---|---|
| 1 | 2026-09-27 | INSP-040 (`docs/reviews/PDR/checklists/tool-validation-rust-toolchain.md`, commit `1b93d83`), independent reviewer | NEEDS CHANGES (2 Major, 5 Minor) | finding-1 (purpose 4 and K20-4 cross-layout claim) | fixed: purpose 4, K20-4, K20-5, limitation 1, section 5, ACC-RUST-001 and `pdr-known-answers.json` restated as same-path identity with mechanical criteria (`c28dd60`), runs 3 and 4; delta iteration requested. Minor findings 3 to 7 left open for the reviewer's disposition (rule C1) |

Iteration 1 text: Record `docs/reviews/PDR/checklists/tool-validation-rust-toolchain.md` (one record for TV-020 to TV-023, one section per TV record), independent reviewer plus a software assurance second review (PDR work plan WP-PDR-08; 07 section 2.1.1), with `docs/templates/peer-review-checklist-tool-validation.md` once WP-PDR-03 has written it. The reviewer re-runs section 3 on the frozen commit and checks each stored answer against its source.

## 9. Accreditation (owner)

Proposed scope statement **ACC-RUST-001**: "Accredited for purposes 1 to 4 for the Rust toolchain `1.98.0-aarch64-apple-darwin` (rustc `1.98.0 (88d9e12ae 2026-08-18)`, cargo `1.98.0 (797e8a9bc 2026-08-05)`, clippy `0.1.98 (88d9e12ae1 2026-08-18)`), with the binary hashes of section 1. Purpose 4 covers reproducibility of the ELF and the loadable image between clean builds of the same source at one absolute path; identity of builds made at different absolute paths, and reproduction of a reference image built at another path, are not covered (limitation 1)."

| Decision | Date | Recorded by |
|---|---|---|
| Pending (owner, after section 8; due PDR, OD-24 (b)) | | |

## Annex A. E-14 software part: the 07 coding standard and static-analysis set against the lock (2026-09-27)

PDR entrance row E-14 needs the Rust coding standard (07 section 7, SWE-061) and the static-analysis set (07 section 8, SWE-135) with confirmed versions. Each tool 07 sections 7 and 8 name, against `tools/toolchain.lock.md` section 1 (read at `d3de579`) and the version observed on 2026-09-27:

| 07 item | Tool (07 section 8.1) | Version in 07 | Version in the lock | Observed 2026-09-27 | TV record | Agreement |
|---|---|---|---|---|---|---|
| CS-27 lints, MSR-07 | `cargo clippy` | with `rustc 1.98.0` | `clippy 0.1.98 (88d9e12ae1 2026-08-18)` (section 1.1) | `clippy 0.1.98 (88d9e12ae1 2026-08-18)` | TV-020 | agree |
| MSR-08, CS-03 | Miri on `nightly-2026-08-24` | "Not installed ... to be installed in FW-B0" | `miri 0.1.0 (fb6531d550 2026-08-23)` with `rust-src` and the sysroot (installed 2026-09-26) | `miri 0.1.0 (fb6531d550 2026-08-23)` | TV-023 | **07 stale** (installed since 2026-09-26) |
| MSR-09 | `cargo audit` | 0.22.2 | `cargo-audit-audit 0.22.2` | not re-observed (outside this record) | due CDR | agree |
| MSR-10 | `cargo deny` | 0.20.2 | `cargo-deny 0.20.2` | not re-observed | due CDR | agree |
| MSR-11 | `cargo geiger` | 0.13.0 | `cargo-geiger 0.13.0` | not re-observed | due CDR | agree |
| MSR-13 | `cargo llvm-cov` | 0.9.1 | `cargo-llvm-cov 0.9.1` | `cargo-llvm-cov 0.9.1` | TV-021 | agree |
| MSR-14 | `cargo +nightly-2026-08-24 llvm-cov --branch` | "`llvm-tools` to be installed in FW-B0" | `llvm-tools` on `nightly-2026-08-24` installed 2026-09-26 | LLVM `23.1.0-rust-1.100.0-nightly` | TV-023 | **07 stale** (installed since 2026-09-26) |
| MSR-17, CS-17 | `rust-code-analysis-cli` | 0.0.25, installed 2026-09-26 | 0.0.25 | not re-observed | TV-012 (due CDR) | agree |
| SWE-186 runner | `cargo nextest` | 0.9.146 | `cargo-nextest 0.9.146 (8af696ddc 2026-09-21)` | same | TV-022 | agree |
| G5 Miri scope | `cargo +nightly-2026-08-24 miri test -p api -p pico2 --lib` (07 section 8.4) | `-p api -p pico2` | gate runs `-p api` only (SRR close-out item B; lien L-016-6) | `-p api --lib` runs 0 tests at the pin (TV-023 limitation 3) | TV-023 | **07 differs from the gate** (known lien) |
| SWE-135 for `tools/**/*.py` | none in 07 section 8 (03 section 6.5 item X9) | none | ruff and coverage.py selected, not installed (lock section 1) | not installed | TV-024 (Draft) | **07 lacks the row** |

07 section 7 (CS-01 to CS-38) needs no tool version beyond the rows above. The three "07 stale" or "07 lacks" rows are cross items of WP-PDR-08 for the 07 writer of the PDR phase (work plan section 5.3: WP-PDR-17, then WP-PDR-13, then WP-PDR-47).
