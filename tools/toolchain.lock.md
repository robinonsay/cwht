# cwht Toolchain Lock

**Status:** Draft for SRR. **Configuration item:** Table 4-1 row 27 of `docs/process/05-configuration-and-data-management.md` (class CR from SRR). **Governs:** SWE-081 (tool versions are controlled items), SWE-136 (tool validation and accreditation, procedure in CM plan §9). **Machine:** owner's Mac, macOS 26.6.2 (build 25G83), Darwin 25.6.0, arm64. **Observed:** 2026-09-25 by running each command in the "Command" column on this machine. **Regeneration:** re-run every command and replace the "Observed version" cells; any change is a Change Request (CM plan §9.2 step 5) and needs a new or re-run tool validation record `TV-NNN`.

Rules: the versions below are the only versions permitted for work "for the record" (evidence cited by a test case, a release build, a vendor package). A tool at another version produces developer evidence only. Class per CM plan §9.1: A = product-generating, B = evidence-generating, C = informational.

## 1. Locked tools

| Tool | Command | Observed version | Class | Purpose(s) | TV record | Accreditation |
|---|---|---|---|---|---|---|
| kicad-cli (KiCad) | `/Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli version` | `10.0.6` | A (exports), B (ERC, DRC) | Gerber, drill, CPL, BOM and STEP export for PCBWay packages; ERC and DRC inspection evidence; schematic and layout renders for review packages. | TV pending (due PDR) | Not yet validated |
| LTspice | `defaults read /Applications/LTspice.app/Contents/Info.plist CFBundleShortVersionString` | `26.0.2.1` (CFBundleVersion `26.0.2.1`) | B | Circuit simulation for Analysis-class verification (filters, PA bias, matching, supply). | TV pending (due PDR) | Not yet validated |
| rustc | `rustc --version` | `rustc 1.98.0 (88d9e12ae 2026-08-18)` | A | Compile firmware for `thumbv8m.main-none-eabihf`; host builds for HostUnit tests. | TV pending (due PDR) | Not yet validated |
| cargo | `cargo --version` | `cargo 1.98.0 (797e8a9bc 2026-08-05)` | A (build), B (`cargo test`, `cargo clippy`) | Build, test, lint, dependency locking (`Cargo.lock`). | TV pending (due PDR) | Not yet validated |
| rustup active toolchain | `rustup show active-toolchain` | `stable-aarch64-apple-darwin (default)` | A | Selects the compiler above. A `rust-toolchain.toml` pinning `1.98.0` is to be added to the firmware crate at its first commit so the lock is enforced by cargo (CM plan §9.3). | covered by rustc TV | n/a |
| rustup installed targets | `rustup target list --installed` | `aarch64-apple-darwin`, `thumbv8m.main-none-eabihf` | A | Host target (tests) and RP2350 Cortex-M33 target (firmware). | covered by rustc TV | n/a |
| rustup toolchains present | `rustup toolchain list` | `stable-aarch64-apple-darwin (active, default)`, `nightly-aarch64-apple-darwin` | n/a | Nightly is present but not permitted for any release build or credit-bearing evidence build. It may produce supporting (non-credit) branch and condition coverage measurements labelled as such in the coverage report (07 sections 8.1, 9.5 and 9.6, MSR-14); the credit-bearing coverage measure is stable `cargo llvm-cov` region coverage. | n/a | Not permitted for release or credit |
| rustup components (stable) | `rustup component list --installed` | `cargo`, `clippy`, `rust-docs`, `rust-src`, `rust-std` (aarch64-apple-darwin), `rust-std` (thumbv8m.main-none-eabihf), `rustc`, `rustfmt` | A (rustc, rust-std), B (clippy), C (rustfmt, rust-docs, rust-src) | Static analysis (clippy, SWE-135), formatting. | covered by rustc/cargo TV | n/a |
| cargo-installed tools | `cargo install --list` | `cargo-binutils v0.4.0`, `cargo-generate v0.23.14` | B (cargo-binutils: `cargo size`, `cargo objdump`), C (cargo-generate) | Binary size and section inspection for memory budgets; crate scaffolding from `rustos/templates`. | TV pending (due CDR) for cargo-binutils | Not yet validated |
| picotool | `picotool version` | `picotool v2.3.0 (Darwin, AppleClang-21.0.0.21000099, Release)` at `/opt/homebrew/bin/picotool` | A | `uf2 convert` (release UF2), `load` (flash), `verify` (PCA-05), `info` (version read-back). | TV pending (due CDR) | Not yet validated |
| python3 (system) | `python3 --version`; `which python3` | `Python 3.13.5` at `/opt/homebrew/bin/python3` | B | Interpreter for `tools/*.py` through the venv below. | covered by venv TV | n/a |
| python (venv) | `/Users/robinonsay/rust/cwht/.venv/bin/python --version` | `Python 3.13.5` | B | Runs `tools/traceability.py`, schema validation, `tools/csa.py`, sim checkers. | TV pending (due SRR) | Not yet validated |
| git | `git --version` | `git version 2.50.1 (Apple Git-155)` | C (with signing configured, tags are the baseline mechanism) | Version control, signed tags (`gpg.format ssh`). | Not required | Not required |
| docker | `docker version` | Client `29.7.2` (API 1.55, Go 1.26.5, commit a7dcaa6, darwin/arm64, context desktop-linux); Server Docker Desktop `4.89.0 (238018)`, Engine `29.7.2`, containerd `v2.3.3`, runc `1.4.3`, docker-init `0.19.0`, linux/arm64 | C (becomes B if it hosts the RP2350 emulator) | Container host for tooling that is not native on macOS. | Not required unless emulator is containerised (then TV due PDR) | Not required |
| ollama | `ollama --version` | `ollama version is 0.33.3` | C | Embeddings for Claude Context search (`nomic-embed-text`, per `.mcp.json`). Never cited as evidence. | Not required | Not required |
| pdftotext (Poppler) | `pdftotext -v` | `pdftotext version 26.08.0` | C | Reference corpus conversion via `tools/refs/*`. Never cited as evidence. | Not required | Not required |
| OpenSCAD | `/Applications/OpenSCAD-2021.01.app/Contents/MacOS/OpenSCAD --version` | 2021.01 (x86_64 under Rosetta; CLI PNG/STL/3MF/CSG export verified, see docs/research/enclosure-cnc-and-openscad-pipeline.md) | A | Enclosure CAD source; STEP is produced by FreeCAD 1.1.3 headless (`/Applications/FreeCAD.app/Contents/Resources/bin/freecadcmd`, installed 2026-09-25) from the OpenSCAD CSG. | TV pending (due PDR) | Installed |
| RP2350 emulator | to be selected (ADR due PDR) | not selected | B | Emulation-class verification (charter §9). | TV pending (due PDR) | Not selected |
| probe-rs, elf2uf2-rs, flip-link | `probe-rs --version`; `elf2uf2-rs --version`; `flip-link --version` | Not installed | n/a | Not used: `picotool` covers UF2 conversion and flashing; `rustos` supplies its own linker script. Listed so their absence is a recorded decision. | n/a | Not permitted (would need CR) |

### 1.1 Sanity checks (charter §8; CM plan §9.2 step 2)

One row per class A or B tool. The single fixture root is `tools/tests/fixtures/`: each fixture is committed under `tools/tests/fixtures/<tool>/` with its expected output, and Python tools are exercised by the unit tests in `tools/tests/test_<tool>.py` (`.venv/bin/python -m unittest discover -s tools/tests`, run from the repository root). The result column is updated (append the date) every time the check is re-run. Full detail lives in the `TV-NNN` record.

| Tool | Known-answer test (pass criterion) | Fixture | Last run | Result |
|---|---|---|---|---|
| kicad-cli | `pcb drc` on `seeded.kicad_pcb` reports exactly the one seeded clearance violation; `pcb drc` on `clean.kicad_pcb` reports none; Gerber export of `clean.kicad_pcb` matches stored SHA-256 list | `tools/tests/fixtures/kicad/` | not yet run | pending |
| LTspice | batch run (`-b`) of `rc-lowpass.asc` reproduces the stored -3 dB frequency within 1 % | `tools/tests/fixtures/ltspice/` | not yet run | pending |
| rustc / cargo | build the fixture crate for `thumbv8m.main-none-eabihf` twice after `cargo clean`; ELF SHA-256 identical both times; `cargo test` on the fixture with one deliberately failing test exits non-zero | `tools/tests/fixtures/rust/` | not yet run | pending |
| clippy | fixture with one seeded `clippy::correctness` lint fails under the project lint configuration | `tools/tests/fixtures/rust/` | not yet run | pending |
| cargo-llvm-cov (stable) | region coverage of the fixture crate reports 100 % when every branch is exercised and reports the seeded uncovered branch when one test is removed (07 section 8.3) | `tools/tests/fixtures/rust/` | not yet run | pending |
| cargo-binutils | `cargo size` on the fixture ELF equals the section sizes stored from `firmware.map` | `tools/tests/fixtures/rust/` | not yet run | pending |
| picotool | `uf2 convert` of the stored fixture ELF equals the stored UF2 SHA-256; `info` reads back the program name | `tools/tests/fixtures/picotool/` | not yet run | pending |
| tools/release.sh, tools/image_trailer.py | the trailer written into the fixture ELF equals the stored CRC-32 value; `--rebuild-check` on the fixture reports identical ELF and UF2 hashes (05 section 8.1) | `tools/tests/fixtures/rust/` | not yet run | pending |
| python (venv) + jsonschema | `invalid-requirement.json` is rejected with the expected error path; `valid-requirement.json` is accepted | `tools/tests/fixtures/schema/` | not yet run | pending |
| tools/traceability.py, tools/validate_docs.py | `python -m unittest discover -s tools/tests` passes: `valid_project` exits 0 with zero findings; `invalid_project` exits 1 with exactly the seeded codes (orphan requirement, test case without a requirement, duplicate id, TBR on a Verified requirement, software hazard control without a Test case, unresolved `RSK-NNN`, bad report and NCR artifact hashes, writing-rule violations) | `tools/tests/fixtures/valid_project/`, `tools/tests/fixtures/invalid_project/` | 2026-09-25 | pass (39 tests) |
| tools/review_trend.py | reproduces the hand-computed raised, open, closed, withdrawn and overdue counts of `docs/templates/rfa-rid-log.example.json` (01 section 11) | `docs/templates/rfa-rid-log.example.json` | blocked: script due before the SRR readiness declaration | pending |
| OpenSCAD + FreeCAD | CSG export of `cube.scad`, then FreeCAD STEP export has the stored bounding box and one solid | `tools/tests/fixtures/openscad/` | not yet run | pending |
| RP2350 emulator | stored scenario reproduces the stored GPIO and serial trace | `tools/tests/fixtures/emulator/` | blocked: not selected | pending |

## 2. Python virtual environment (`/Users/robinonsay/rust/cwht/.venv`)

Command: `/Users/robinonsay/rust/cwht/.venv/bin/pip list`. Reproduce with `python3 -m venv .venv && .venv/bin/pip install -r tools/requirements.txt`; `tools/requirements.txt` must pin exactly these versions (CM plan §9.3).

| Package | Version | Role |
|---|---|---|
| attrs | 26.1.0 | dependency of jsonschema |
| beautifulsoup4 | 4.15.0 | corpus scraping (`tools/refs/swehb_scrape.py`), class C |
| certifi | 2026.7.22 | dependency of requests |
| charset-normalizer | 3.5.1 | dependency of requests |
| idna | 3.20 | dependency of requests |
| jsonschema | 4.26.0 | requirement and test-case schema validation (class B) |
| jsonschema-specifications | 2025.9.1 | dependency of jsonschema |
| lxml | 6.1.3 | corpus conversion, class C |
| markdownify | 1.2.3 | corpus conversion, class C |
| pip | 26.2.1 | package manager |
| referencing | 0.37.0 | dependency of jsonschema |
| requests | 2.34.2 | corpus download, class C |
| rpds-py | 2026.6.3 | dependency of jsonschema |
| six | 1.17.0 | dependency of markdownify |
| soupsieve | 2.10 | dependency of beautifulsoup4 |
| typing_extensions | 4.16.0 | dependency |
| urllib3 | 2.8.0 | dependency of requests |

## 3. External source dependency

| Dependency | Identification | Command | Observed | Rule |
|---|---|---|---|---|
| `rustos` (firmware platform, Cargo path dependency `../rustos`) | commit SHA on the owner's machine; remote `git@github.com:robinonsay/rustos.git` | `git -C /Users/robinonsay/rust/rustos rev-parse HEAD` | `c54d35aa8e7f9ad30f6508bca458a59c1fc009db` (`c54d35a`, "Fix build") | Every VDD records the `rustos` commit used for the build. Moving the pin is a CR (CM plan Table 4-1 row 26). Pinning method decision: CM plan §14 OQ-5. |

## 4. Host environment

| Item | Command | Observed |
|---|---|---|
| OS | `sw_vers` | macOS 26.6.2, build 25G83 |
| Kernel | `uname -r`; `uname -m` | Darwin 25.6.0, arm64 |
| Shell | login shell | zsh |

## 5. Validation status summary

No tool validation record exists yet (`docs/cm/tool-validation/` is empty). Order of TV work per CM plan §13: SRR needs TV for the venv Python and `jsonschema` and for `tools/traceability.py`; PDR needs LTspice, kicad-cli, OpenSCAD, the emulator and the Rust toolchain; CDR needs picotool and cargo-binutils. Until a tool is Accredited, its output is developer evidence only (CM plan §9.1).

## 6. Change history

| Date | Change | Reference |
|---|---|---|
| 2026-09-25 | Initial lock recorded by running the listed commands. | CM plan §9.3 |
| 2026-09-25 | Fixture root fixed at `tools/tests/fixtures/`; unit-test rows for `traceability.py` and `validate_docs.py` recorded as passing; nightly row reworded (supporting coverage only); rows for stable `cargo-llvm-cov`, `tools/release.sh` and `tools/review_trend.py` added. | Cross-document findings applied before SRR (Log-class change) |
