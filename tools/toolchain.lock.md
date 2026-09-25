# cwht Toolchain Lock

**Status:** Draft for SRR. **Configuration item:** Table 4-1 row 27 of `docs/process/05-configuration-and-data-management.md` (class CR from SRR). **Governs:** SWE-081 (tool versions are controlled items; the SWE-081 note names compiler versions and environment settings), SWE-136 (tool validation and accreditation, procedure in CM plan §9). **Machine:** owner's Mac, macOS 26.6.2 (build 25G83), Darwin 25.6.0, arm64. **Observed:** 2026-09-25, every command in the "Command" column run on this machine; re-run in full later the same day (second observation), differences recorded in §6. **Regeneration:** re-run every command and replace the "Observed version" cells; a version change of an accredited tool is a Change Request (CM plan §9.2 step 5) and needs a new or re-run tool validation record `TV-NNN`; adding a row for a newly installed tool is a Log-class change until that tool has a TV record.

Rules: the versions below are the only versions permitted for work "for the record" (evidence cited by a test case, a release build, a vendor package). A tool at another version produces developer evidence only. Class per CM plan §9.1: A = product-generating, B = evidence-generating, C = informational. Install source is recorded so the TV record can reproduce the installation (CM plan §9.2 step 1).

## 1. Locked tools

| Tool | Command | Observed version | Install source | Class | Purpose(s) | TV record | Accreditation |
|---|---|---|---|---|---|---|---|
| kicad-cli (KiCad) | `/Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli version` | `10.0.6` | KiCad macOS bundle | A (exports), B (ERC, DRC) | Gerber, drill, CPL, BOM and STEP export for PCBWay packages; ERC and DRC inspection evidence; schematic and layout renders for review packages. | TV pending (due PDR) | Not yet validated |
| LTspice | `defaults read /Applications/LTspice.app/Contents/Info.plist CFBundleShortVersionString` | `26.0.2.1` (`CFBundleVersion` also `26.0.2.1`) | Analog Devices macOS bundle; telemetry opt-out per SI-027 | B | Circuit simulation for Analysis-class verification (filters, PA bias, matching, supply). | TV pending (due PDR) | Not yet validated |
| rustc | `rustc --version` | `rustc 1.98.0 (88d9e12ae 2026-08-18)` | rustup, channel `stable` | A | Compile firmware for `thumbv8m.main-none-eabihf`; host builds for HostUnit tests. | TV pending (due PDR) | Not yet validated |
| cargo | `cargo --version` | `cargo 1.98.0 (797e8a9bc 2026-08-05)` | rustup, channel `stable` | A (build), B (`cargo test`, `cargo clippy`) | Build, test, lint, dependency locking (`Cargo.lock`). | TV pending (due PDR) | Not yet validated |
| rustup active toolchain | `rustup show active-toolchain` | `stable-aarch64-apple-darwin (default)` | rustup | A | Selects the compiler above. A `rust-toolchain.toml` pinning `1.98.0` is added to the firmware crate at its first commit so the lock is enforced by cargo (CM plan §9.3). | covered by rustc TV | n/a |
| rustup installed targets | `rustup target list --installed` | `aarch64-apple-darwin`, `thumbv8m.main-none-eabihf` | rustup | A | Host target (tests) and RP2350 Cortex-M33 target (firmware). | covered by rustc TV | n/a |
| rustup toolchains present | `rustup toolchain list` | `stable-aarch64-apple-darwin (active, default)`, `nightly-aarch64-apple-darwin` | rustup | n/a | Nightly is present but not permitted for any release build or credit-bearing evidence build. It may produce supporting (non-credit) branch and condition coverage measurements labelled as such in the coverage report (07 sections 8.1, 9.5 and 9.6, MSR-14); the credit-bearing coverage measure is stable `cargo llvm-cov` region coverage. | n/a | Not permitted for release or credit |
| rustup components (stable) | `rustup component list --installed` | `cargo`, `clippy`, `rust-docs`, `rust-src`, `rust-std` (aarch64-apple-darwin), `rust-std` (thumbv8m.main-none-eabihf), `rustc`, `rustfmt` | rustup | A (rustc, rust-std), B (clippy), C (rustfmt, rust-docs, rust-src) | Static analysis (clippy, SWE-135), formatting. | covered by rustc/cargo TV | n/a |
| llvm-tools (LLVM binaries used by cargo-llvm-cov and cargo-binutils) | `rustup component list \| grep llvm`; `ls ~/.rustup/toolchains/stable-aarch64-apple-darwin/lib/rustlib/aarch64-apple-darwin/bin/`; `rust-objcopy --version` | rustup does not mark `llvm-tools-aarch64-apple-darwin` as installed, yet `llvm-cov`, `llvm-profdata`, `llvm-objcopy`, `llvm-size`, `llvm-nm`, `rust-lld` and others are present in the toolchain's `rustlib/aarch64-apple-darwin/bin/`, and `rust-objcopy --version` reports `llvm-objcopy` | Unknown (not rustup-tracked); the TV record for cargo-llvm-cov must establish and pin the source, preferably by running `rustup component add llvm-tools` so the component becomes tracked | B | Coverage instrumentation readout (`llvm-cov`, `llvm-profdata`), section sizes (`llvm-size`), object copy for release images. | covered by cargo-llvm-cov and cargo-binutils TVs | Not yet validated |
| cargo-installed tools (tracked) | `cargo install --list` | `cargo-audit v0.22.2` (`cargo-audit`); `cargo-binutils v0.4.0` (`cargo-cov`, `cargo-nm`, `cargo-objcopy`, `cargo-objdump`, `cargo-profdata`, `cargo-readobj`, `cargo-size`, `cargo-strip` and the `rust-*` shims) | `cargo install` from crates.io (`~/.cargo/.crates.toml`) | see the per-tool rows | see the per-tool rows | see the per-tool rows | see the per-tool rows |
| cargo-llvm-cov | `cargo llvm-cov --version` | `cargo-llvm-cov 0.9.1` | Prebuilt binary `~/.cargo/bin/cargo-llvm-cov` dated 2026-09-25 11:44, not tracked by `cargo install --list`; exact source recorded in its TV | B | Credit-bearing region coverage on stable (07 sections 8.1, 8.3, 9.5; SWE-189, SWE-190); supporting branch coverage on nightly labelled non-credit. | TV pending (due PDR, before FW-B0 coverage is cited) | Not yet validated |
| cargo-audit | `cargo audit --version` | `cargo-audit-audit 0.22.2` | `cargo install cargo-audit` (tracked), binary dated 2026-09-25 11:47 | B | RustSec advisory check of `Cargo.lock` (07 section 8.4 gate G5, MSR-09; SWE-207). | TV pending (due CDR) | Not yet validated |
| cargo-deny | `cargo deny --version` | `cargo-deny 0.20.2` | Prebuilt binary `~/.cargo/bin/cargo-deny` dated 2026-09-25 11:48, not tracked by `cargo install --list` | B | Licence, ban and advisory policy check (07 gate G5, MSR-10). | TV pending (due CDR) | Not yet validated |
| cargo-geiger | `cargo geiger --version` | `cargo-geiger 0.13.0` | Prebuilt binary `~/.cargo/bin/cargo-geiger` dated 2026-09-25 11:46, not tracked by `cargo install --list` | B | Unsafe-usage counts per crate (07 gate G5, MSR-11), alongside `tools/unsafe_audit.py`. | TV pending (due CDR) | Not yet validated |
| cargo-nextest | `cargo nextest --version` | `cargo-nextest 0.9.146 (8af696ddc 2026-09-21)` | Prebuilt binary `~/.cargo/bin/cargo-nextest` dated 2026-09-25 11:45, not tracked by `cargo install --list` | B | Test runner for HostUnit suites (07 section 13 VDD toolchain list); `cargo test` remains the reference runner until the TV record covers nextest. | TV pending (due PDR, with the Rust toolchain) | Not yet validated |
| cargo-binutils | `cargo size --version`; `rust-objcopy --version` | `cargo-size 0.4.0`; `llvm-objcopy, compatible with GNU objcopy` | `cargo install cargo-binutils` (tracked) | B | `cargo size` and `cargo objdump` for flash and RAM budgets (07 MSR-18, MSR-19); section inspection of release ELFs. | TV pending (due CDR) | Not yet validated |
| cargo-generate | `cargo generate --version` | `cargo generate-generate 0.23.14` | Binary `~/.cargo/bin/cargo-generate` dated 2026-08-30; no longer listed by `cargo install --list` (it was at the first observation) | C | Crate scaffolding from `rustos/templates`. Never cited as evidence. | Not required | Not required |
| rust-code-analysis-cli | `rust-code-analysis-cli --version` | Not installed (no binary in `~/.cargo/bin`) | to be installed at FW-B0 (07 sections 8.1 and 8.4) | B | Cyclomatic complexity per function for the SWE-220 limit of 15 (07 gate G5 with `tools/complexity_gate.py`). Until installed and accredited, complexity is not measured for the record. | TV pending (due CDR) | Not installed |
| cargo-binstall | `ls ~/.cargo/bin \| grep binstall` | Not installed | n/a | C | Listed so the origin of the untracked prebuilt binaries above is not mistaken for binstall; their source is recorded in each TV record. | Not required | Not required |
| cargo-miri | `cargo miri --version` | Component `miri` not available for `stable-aarch64-apple-darwin` (rustup proxy present, tool absent) | n/a | n/a | Not used. Listed so the proxy in `~/.cargo/bin` is not mistaken for an installed tool. | n/a | Not permitted (would need CR) |
| picotool | `picotool version` | `picotool v2.3.0 (Darwin, AppleClang-21.0.0.21000099, Release)` at `/opt/homebrew/bin/picotool` | Homebrew `picotool 2.3.0` | A | `uf2 convert` (release UF2), `load` (flash), `verify` (PCA-05), `info` (version read-back). | TV pending (due CDR) | Not yet validated |
| python3 (system) | `python3 --version`; `which python3` | `Python 3.13.5` at `/opt/homebrew/bin/python3` | Homebrew | B | Interpreter for `tools/*.py` through the venv below. | covered by venv TV | n/a |
| python (venv) | `/Users/robinonsay/rust/cwht/.venv/bin/python --version` | `Python 3.13.5` | `python3 -m venv .venv` from the Homebrew interpreter | B | Runs `tools/traceability.py`, `tools/validate_docs.py`, the renderers, schema validation, `tools/csa.py`, sim checkers. | TV pending (due SRR) | Not yet validated |
| git | `git --version` | `git version 2.50.1 (Apple Git-155)` | Xcode Command Line Tools | C (tags are the baseline mechanism; signing per CM plan §4.4 once configured) | Version control, annotated tags, remote `origin` (`git@github.com:robinonsay/cwht.git`). | Not required | Not required |
| docker | `docker version` | Client `29.7.2` (API 1.55, Go 1.26.5, commit a7dcaa6, darwin/arm64, context desktop-linux); Server Docker Desktop `4.89.0 (238018)`, Engine `29.7.2`, containerd `v2.3.3`, runc `1.4.3`, docker-init `0.19.0`, linux/arm64 | Docker Desktop | C (becomes B if it hosts the RP2350 emulator) | Container host for tooling that is not native on macOS. | Not required unless the emulator is containerised (then TV due PDR) | Not required |
| ollama | `ollama --version` | `ollama version is 0.33.3` | Ollama macOS app | C | Embeddings for Claude Context search (`nomic-embed-text`, per `.mcp.json`). Never cited as evidence. | Not required | Not required |
| pdftotext (Poppler) | `pdftotext -v` | `pdftotext version 26.08.0` | Homebrew `poppler 26.08.0` | C | Reference corpus conversion via `tools/refs/*`. Never cited as evidence. | Not required | Not required |
| OpenSCAD | `/Applications/OpenSCAD-2021.01.app/Contents/MacOS/OpenSCAD --version` | `OpenSCAD version 2021.01` (x86_64 under Rosetta). `/Applications/OpenSCAD.app` does not exist; the versioned bundle name is the installed path. | OpenSCAD 2021.01 macOS bundle; CLI PNG, STL, 3MF and CSG export verified in `docs/research/enclosure-cnc-and-openscad-pipeline.md` | A | Enclosure CAD source (`hardware/enclosure/*.scad`); CSG export feeding FreeCAD. | TV pending (due PDR) | Not yet validated |
| FreeCAD (headless) | `defaults read /Applications/FreeCAD.app/Contents/Info.plist CFBundleVersion`; CLI `/Applications/FreeCAD.app/Contents/Resources/bin/freecadcmd` | `1.1.3` (`CFBundleShortVersionString` is empty in this bundle) | Homebrew cask, approved by SI-032, installed 2026-09-25 | A | STEP export from the OpenSCAD CSG for the CNC package (`hardware/releases/ME-ENC-rev<X>-<n>/cwht-ENC-rev<X>.step`). | TV pending (due PDR, shared with OpenSCAD) | Not yet validated |
| shasum | `shasum --version` | `6.04` (Perl `Digest::SHA`, macOS) | macOS | B | Writes and checks `SHA256SUMS` in every release directory (CM plan §8.1 step 4, §8.2, PCA-01, PCA-06). | covered by the `tools/release.sh` TV | Not yet validated |
| RP2350 emulator | to be selected (ADR due PDR) | not selected | n/a | B | Emulation-class verification (charter §9). | TV pending (due PDR) | Not selected |
| probe-rs, elf2uf2-rs, flip-link | `probe-rs --version`; `elf2uf2-rs --version`; `flip-link --version` | Not installed | n/a | n/a | Not used: `picotool` covers UF2 conversion and flashing; `rustos` supplies its own linker script. Listed so their absence is a recorded decision. | n/a | Not permitted (would need CR) |

### 1.1 Sanity checks (charter §8; CM plan §9.2 step 2)

One row per class A or B tool. The single fixture root is `tools/tests/fixtures/`: each fixture is committed under `tools/tests/fixtures/<tool>/` with its expected output, and Python tools are exercised by the unit tests in `tools/tests/test_<tool>.py` (`.venv/bin/python -m unittest discover -s tools/tests`, run from the repository root). The result column is updated (append the date) every time the check is re-run. Full detail lives in the `TV-NNN` record.

| Tool | Known-answer test (pass criterion) | Fixture | Last run | Result |
|---|---|---|---|---|
| kicad-cli | `pcb drc` on `seeded.kicad_pcb` reports exactly the one seeded clearance violation; `pcb drc` on `clean.kicad_pcb` reports none; Gerber export of `clean.kicad_pcb` matches stored SHA-256 list | `tools/tests/fixtures/kicad/` | not yet run | pending |
| LTspice | batch run (`-b`) of `rc-lowpass.asc` reproduces the stored -3 dB frequency within 1 % | `tools/tests/fixtures/ltspice/` | not yet run | pending |
| rustc / cargo | build the fixture crate for `thumbv8m.main-none-eabihf` twice after `cargo clean`; ELF SHA-256 identical both times; `cargo test` on the fixture with one deliberately failing test exits non-zero | `tools/tests/fixtures/rust/` | not yet run | pending |
| clippy | fixture with one seeded `clippy::correctness` lint fails under the project lint configuration | `tools/tests/fixtures/rust/` | not yet run | pending |
| cargo-llvm-cov (stable) + llvm-tools | region coverage of the fixture crate reports 100 % when every branch is exercised and reports the seeded uncovered branch when one test is removed (07 section 8.3) | `tools/tests/fixtures/rust/` | not yet run | pending |
| cargo-nextest | the fixture crate with one deliberately failing test exits non-zero and names that test; with the failing test removed exits 0 with the stored test count | `tools/tests/fixtures/rust/` | not yet run | pending |
| cargo-audit | a fixture `Cargo.lock` pinning a crate version with a known RustSec advisory reports exactly that advisory id; the clean fixture lock reports none | `tools/tests/fixtures/rust/` | not yet run | pending |
| cargo-deny | a fixture `deny.toml` banning one licence flags the seeded crate and nothing else | `tools/tests/fixtures/rust/` | not yet run | pending |
| cargo-geiger | the fixture crate with one `unsafe` block reports exactly one unsafe expression and zero unsafe functions | `tools/tests/fixtures/rust/` | not yet run | pending |
| cargo-binutils | `cargo size` on the fixture ELF equals the section sizes stored from `firmware.map` | `tools/tests/fixtures/rust/` | not yet run | pending |
| rust-code-analysis-cli | the fixture function with a stored cyclomatic complexity of 16 is reported as 16 and rejected by `tools/complexity_gate.py --max 15` | `tools/tests/fixtures/rust/` | blocked: not installed | pending |
| picotool | `uf2 convert` of the stored fixture ELF equals the stored UF2 SHA-256; `info` reads back the program name | `tools/tests/fixtures/picotool/` | not yet run | pending |
| tools/release.sh, tools/image_trailer.py, shasum | the trailer written into the fixture ELF equals the stored CRC-32 value; `--rebuild-check` on the fixture reports identical ELF and UF2 hashes; `shasum -a 256 -c SHA256SUMS` passes on the fixture directory and fails when one byte is changed (05 section 8.1) | `tools/tests/fixtures/rust/` | not yet run | pending |
| python (venv) + jsonschema | `invalid-requirement.json` is rejected with the expected error path; `valid-requirement.json` is accepted | `tools/tests/fixtures/schema/` | not yet run | pending |
| tools/traceability.py, tools/validate_docs.py | `python -m unittest discover -s tools/tests` passes: `valid_project` exits 0 with zero findings; `invalid_project` exits 1 with exactly the seeded codes (orphan requirement, test case without a requirement, duplicate id, TBR on a Verified requirement, software hazard control without a Test case, unresolved `RSK-NNN`, bad report and NCR artifact hashes, writing-rule violations) | `tools/tests/fixtures/valid_project/`, `tools/tests/fixtures/invalid_project/` | 2026-09-25 (twice) | pass (39 tests, both runs) |
| tools/review_trend.py | reproduces the hand-computed raised, open, closed, withdrawn and overdue counts of `docs/templates/rfa-rid-log.example.json` (01 section 11) | `docs/templates/rfa-rid-log.example.json` | blocked: script due before the SRR readiness declaration | pending |
| OpenSCAD + FreeCAD | CSG export of `cube.scad` with OpenSCAD 2021.01, then `freecadcmd` STEP export has the stored bounding box and one solid | `tools/tests/fixtures/openscad/` | not yet run | pending |
| RP2350 emulator | stored scenario reproduces the stored GPIO and serial trace | `tools/tests/fixtures/emulator/` | blocked: not selected | pending |

## 2. Python virtual environment (`/Users/robinonsay/rust/cwht/.venv`)

Command: `/Users/robinonsay/rust/cwht/.venv/bin/pip list` (36 packages on the second observation; 17 at the first). Reproduce with `python3 -m venv .venv && .venv/bin/pip install -r tools/requirements.txt`; `tools/requirements.txt` must pin exactly these versions (CM plan §9.3). On 2026-09-25 it lists nine unpinned names (`beautifulsoup4`, `markdownify`, `jsonschema`, `requests`, `lxml`, `pyyaml`, `spicelib`, `PyLTSpice`, `numpy`); pinning it is CM plan §14.1 item AL-4. Roles from `pip show` (`Required-by`).

| Package | Version | Class | Role |
|---|---|---|---|
| attrs | 26.1.0 | B | dependency of jsonschema |
| beautifulsoup4 | 4.15.0 | C | corpus scraping (`tools/refs/swehb_scrape.py`) |
| certifi | 2026.7.22 | C | dependency of requests |
| charset-normalizer | 3.5.1 | C | dependency of requests |
| clipin | 1.0.0 | B | dependency of spicelib |
| contourpy | 1.4.0 | B | dependency of matplotlib |
| cycler | 0.12.1 | B | dependency of matplotlib |
| Deprecated | 1.3.1 | B | dependency of ltspice |
| fonttools | 4.66.0 | B | dependency of matplotlib |
| idna | 3.20 | C | dependency of requests |
| jsonschema | 4.26.0 | B | requirement, test-case, RMM, risk and RFA/RID schema validation (`tools/validate_docs.py`) |
| jsonschema-specifications | 2025.9.1 | B | dependency of jsonschema |
| kiwisolver | 1.5.1 | B | dependency of matplotlib |
| ltspice | 1.0.6 | B | LTspice `.raw` reader for simulation checkers (`hardware/sim/`) |
| lxml | 6.1.3 | C | corpus conversion |
| markdownify | 1.2.3 | C | corpus conversion |
| matplotlib | 3.11.2 | B | plots for review packages, TPM trends (`tools/review_trend.py`, `tools/render_tpm.py`) and simulation checkers |
| numpy | 2.5.3 | B | numeric core for simulation checkers and budgets |
| packaging | 26.3 | B | dependency of matplotlib |
| pillow | 12.3.0 | B | dependency of matplotlib and spicelib |
| pip | 26.2.1 | C | package manager |
| psutil | 7.2.2 | B | dependency of spicelib |
| PyLTSpice | 6.0.1 | B | LTspice batch driver (`-b` runs, `.raw` parsing) for Analysis evidence |
| pyparsing | 3.3.3 | B | dependency of matplotlib |
| python-dateutil | 2.9.0.post0 | B | dependency of matplotlib |
| PyYAML | 6.0.3 | B | front-matter parsing of CRs, VDDs and baseline records by `tools/csa.py`; no package requires it |
| referencing | 0.37.0 | B | dependency of jsonschema |
| requests | 2.34.2 | C | corpus download |
| rpds-py | 2026.6.3 | B | dependency of jsonschema |
| scipy | 1.18.1 | B | dependency of spicelib; filter and matching calculations in budgets |
| six | 1.17.0 | B | dependency of python-dateutil |
| soupsieve | 2.10 | C | dependency of beautifulsoup4 |
| spicelib | 1.6.3 | B | dependency of PyLTSpice; netlist editing and raw-file reading |
| typing_extensions | 4.16.0 | C | dependency |
| urllib3 | 2.8.0 | C | dependency of requests |
| wrapt | 2.4.1 | B | dependency of Deprecated |

## 3. External source dependency

| Dependency | Identification | Command | Observed | Rule |
|---|---|---|---|---|
| `rustos` (firmware platform, Cargo path dependency `../rustos`) | commit SHA on the owner's machine; remote `git@github.com:robinonsay/rustos.git` | `git -C /Users/robinonsay/rust/rustos rev-parse HEAD` | `c54d35aa8e7f9ad30f6508bca458a59c1fc009db` (`c54d35a`, "Fix build"), unchanged at the second observation | Every VDD records the `rustos` commit used for the build. Moving the pin is a CR (CM plan Table 4-1 row 26). Pinning method decision: CM plan §14 OQ-CM-005. |

## 3a. Review slide toolchain (charter §4 item 2)

| Tool | Version / source | Command | Observed | Notes |
|---|---|---|---|---|
| `asciidoctor` (Asciidoctor.js, npm, project-local) | `tools/slides/package.json` pin `^3.0.4`; install `cd tools/slides && npm install` | `node -e "console.log(require('./tools/slides/node_modules/asciidoctor/package.json').version)"` | 3.0.4 | `tools/slides/node_modules/` is git-ignored; `package-lock.json` is the lock. The Ruby `asciidoctor 2.0.26` at `/usr/local/bin` is not used for decks. |
| `@asciidoctor/reveal.js` (npm) | pin `^5.2.0` | as above with the package path | 5.2.0 | Converts `<review>.adoc` to reveal.js HTML. |
| `reveal.js` (npm) | pin `^5.2.1` (reveal.js 6.x moves `plugin/` under `dist/` and breaks converter 5.2.0 asset paths; keep 5.x) | as above | 5.2.1 | Copied next to each deck as `docs/reviews/<REVIEW>/slides/reveal.js/` so the HTML is offline and self-contained (about 5 MB). |
| Chromium headless shell (Playwright cache) | `~/Library/Caches/ms-playwright/chromium_headless_shell-1223/chrome-headless-shell-mac-arm64/chrome-headless-shell` | `ls ~/Library/Caches/ms-playwright/` | build 1223 present (also `chromium-1223`, `ffmpeg-1011`) | Used by `tools/slides/render_deck.py` with `--headless --screenshot --virtual-time-budget=4000` per slide fragment `#/N`; no GUI and no macOS privacy permission (charter §11 rule 8). If the cache is purged: `npx playwright install chromium-headless-shell`. |
| `tools/slides/render_deck.py` | repo | `.venv/bin/python tools/slides/render_deck.py <deck.adoc> [--size WxH]` | fixture deck renders 4 slides; known-answer test `tools/tests/test_render_deck.py` passes | Output: `<deck>.html`, `reveal.js/`, `png/slide-NN.png`; every PNG is inspected by the author before the review. |

## 4. Host environment

| Item | Command | Observed |
|---|---|---|
| OS | `sw_vers` | macOS 26.6.2, build 25G83 |
| Kernel | `uname -r`; `uname -m` | Darwin 25.6.0, arm64 |
| Shell | login shell | zsh |
| Repository remote | `git -C /Users/robinonsay/rust/cwht remote -v` | `origin git@github.com:robinonsay/cwht.git` (fetch and push); `main` in sync with `origin/main` at `3a4711d` |
| Tag signing | `git config gpg.format`; `git config user.signingkey`; `git config tag.gpgSign` | all unset (unsigned annotated tags are compliant until configured, charter §8, CM plan §4.4; `~/.ssh/id_ed25519.pub` exists) |

## 5. Validation status summary

No tool validation record exists yet (`docs/cm/tool-validation/` does not exist). Order of TV work per CM plan §13: SRR needs TV for the venv Python and `jsonschema` and for `tools/traceability.py` and `tools/validate_docs.py`; PDR needs LTspice, kicad-cli, OpenSCAD with FreeCAD, the emulator, the Rust toolchain with cargo-llvm-cov, llvm-tools and cargo-nextest; CDR needs picotool, cargo-binutils, cargo-audit, cargo-deny, cargo-geiger and rust-code-analysis-cli (after installation at FW-B0). Until a tool is Accredited, its output is developer evidence only (CM plan §9.1).

## 6. Change history

| Date | Change | Reference |
|---|---|---|
| 2026-09-25 | Initial lock recorded by running the listed commands. | CM plan §9.3 |
| 2026-09-25 | Fixture root fixed at `tools/tests/fixtures/`; unit-test rows for `traceability.py` and `validate_docs.py` recorded as passing; nightly row reworded (supporting coverage only); rows for stable `cargo-llvm-cov`, `tools/release.sh` and `tools/review_trend.py` added. | Cross-document findings applied before SRR (Log-class change) |
| 2026-09-25 | OpenSCAD 2021.01 and FreeCAD 1.1.3 recorded. | commit `3a4711d` |
| 2026-09-25 | Second full observation. Differences from the first: `cargo install --list` now tracks `cargo-audit v0.22.2` and `cargo-binutils v0.4.0` only (`cargo-generate` 0.23.14 binary still present but untracked); new rows for `cargo-llvm-cov 0.9.1`, `cargo-deny 0.20.2`, `cargo-geiger 0.13.0`, `cargo-nextest 0.9.146`, `llvm-tools` (present in the toolchain directory, not rustup-tracked), `rust-code-analysis-cli` (not installed), `cargo-binstall` (not installed), `cargo-miri` (unavailable), `shasum 6.04`, FreeCAD `1.1.3` with its `defaults read` command; OpenSCAD row states that `/Applications/OpenSCAD.app` does not exist; venv grew from 17 to 36 packages (PyLTSpice, spicelib, ltspice, matplotlib, numpy, scipy, PyYAML and their dependencies) and `tools/requirements.txt` is recorded as unpinned (AL-4); install-source column added; §4 records the remote and the unset signing configuration; §1.1 gains rows for the new tools. All other versions unchanged. | CM plan §9.3 (Log-class change before SRR) |
| 2026-09-25 | Review slide toolchain recorded (§3a): project-local Asciidoctor.js 3.0.4, @asciidoctor/reveal.js 5.2.0, reveal.js pinned to 5.2.1, Chromium headless shell 1223, `tools/slides/render_deck.py` with its known-answer test. Owner directive: every gate review is presented slide by slide. | charter §4 item 2 (owner directive 2026-09-25) |
