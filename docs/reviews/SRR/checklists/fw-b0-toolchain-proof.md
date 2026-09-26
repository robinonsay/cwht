---
id: INSP-016
checklist: peer-review-checklist-code
checklist_revision: B
checklist_file: docs/reviews/SRR/checklists/fw-b0-toolchain-proof.md
# product: the FW-B0 toolchain proof of 07 sections 3.1 and 3.2 (SRR package section 2 item H12),
# reviewed as one product: the firmware workspace, the gate script, the case and its run 1 report
product: firmware/ (FW-B0 workspace), tools/sw_gate.sh, docs/test_cases/sw-tool/test_cases.json, docs/vv/reports/TC-SW-TOOL-001-r1.md
# product_commit: iteration 3 review baseline (committed); product_files lists every reviewed file
# as path@blob from git rev-parse HEAD:<path> (record drift rule, SRR package section 2.3, R13)
product_commit: "adcfe0946d2f1b5cd8f41a8f91eb4219a7fb99a1"
product_files:
  - "docs/test_cases/sw-tool/test_cases.json@fee1e7246af59d5e8a43ed1b9cdf483854053fdc"
  - "docs/vv/reports/TC-SW-TOOL-001-r1.md@04bc3354352139eb30b33fadff43e1c9b61d0d8e"
  - "docs/vv/reports/TC-SW-TOOL-001-r1/blink-rate-prediction.txt@78f1ac59aeaf1254d2e4ba0b6c2c5972cb94d5a9"
  - "docs/vv/reports/TC-SW-TOOL-001-r1/blinky-build.txt@2aa80fcc749a3b2fb5e949341ad7f6344dfaf227"
  - "docs/vv/reports/TC-SW-TOOL-001-r1/cwht-app.elf@6d9965a04a81895a5a2e355e685aa07ae5f65f7a"
  - "docs/vv/reports/TC-SW-TOOL-001-r1/cwht-app.map@e5557024967701cbee3661601e39572bf22afa80"
  - "docs/vv/reports/TC-SW-TOOL-001-r1/cwht-app.uf2@640951c4994cbc5e8a45e8f89eff3879795da144"
  - "docs/vv/reports/TC-SW-TOOL-001-r1/gate-known-answer.sh@eaaca0e699da5312e85c5750e7228cfc1d87a5c4"
  - "docs/vv/reports/TC-SW-TOOL-001-r1/gate-known-answer.txt@df92abe952c77acfbbf48d61a90491be3b9e3fe5"
  - "docs/vv/reports/TC-SW-TOOL-001-r1/host-build-test.txt@ca478c7e9eb0243b0561e744b10165ebf28ee652"
  - "docs/vv/reports/TC-SW-TOOL-001-r1/rustos-blinky.elf@5dd8b02ad79c8544fed5e6059e2a4626bcabe822"
  - "docs/vv/reports/TC-SW-TOOL-001-r1/rustos-blinky.uf2@f0e9fb343ed9c24f0e5b791fc344b51093c48ab9"
  - "docs/vv/reports/TC-SW-TOOL-001-r1/sw-gate-full.txt@3fca1c2c9510e9dfd34b24c71811f703743899d9"
  - "docs/vv/reports/TC-SW-TOOL-001-r1/sw-gate-keep-going.txt@b31755e2afac05c3c217180147f2f04a80ade42c"
  - "docs/vv/reports/TC-SW-TOOL-001-r1/uf2-info.txt@ea4694c2a3fa09a86fc227d32f2fe5edb5a1362e"
  - "docs/vv/reports/TC-SW-TOOL-001-r1/versions.txt@22e56c97597f7dae54d5a9168162a9ffb0fc620a"
  - "firmware/.cargo/config.toml@b677319fa0fe9b62431d01fa8b749bbd7e585b0d"
  - "firmware/.config/nextest.toml@00b81042cf7f73ff6ffa67f013b4c78ef6884a63"
  - "firmware/Cargo.lock@784605ca28b94ea0d3ace66a5797c11cbbced80d"
  - "firmware/Cargo.toml@7799f6b63e26e8fca0c2cb68270c3ff9d7841d05"
  - "firmware/clippy.toml@42020b54612e1bcb2c64149353575b6fa6883d96"
  - "firmware/cwht-app/Cargo.toml@236df1403dc94cc8534e9397d6addc819dc3c053"
  - "firmware/cwht-app/build.rs@41dea79e96a75c4919491630fd5a83978d3c9f18"
  - "firmware/cwht-app/src/main.rs@e32006a582bc49af6b2b12e8856015173210afd0"
  - "firmware/cwht-core/Cargo.toml@3774fca09cead334004aeaa00e07eb2c6ff9d941"
  - "firmware/cwht-core/src/heartbeat.rs@f38b716a57d7e88bdbcb0cc5d20fb270ea75e71f"
  - "firmware/cwht-core/src/lib.rs@01c49f60f82689aab61570e7200bf9bf4064cbd1"
  - "firmware/cwht-core/tests/heartbeat.rs@718a0246da10eec9c8f3be5d939d326e2133cb4c"
  - "firmware/cwht-hal-mock/Cargo.toml@565c5597b2b4e0d4611fd2e1079f653cd4337f41"
  - "firmware/cwht-hal-mock/src/gpio.rs@fc8872bd420ecbd4760d2f2fc05b236ee842c801"
  - "firmware/cwht-hal-mock/src/lib.rs@f5141c137073e0493a455681aa1d5ae18f53db38"
  - "firmware/cwht-hal-mock/tests/gpio.rs@f1b302bcfa7f55105ad73d8b01d98d0fb7901312"
  - "firmware/deny.toml@4cd6de9c2f49c9da254ca05cb31973286c9ac2c8"
  - "firmware/emu/README.md@ae79ea6c77595157c0774a136735191196c03d99"
  - "firmware/rust-toolchain.toml@ca29c2548ff35887352c340bf5c5b49475758ddb"
  - "firmware/rustfmt.toml@dce38290b859775f8e3732df729561b198f991a3"
  - "tools/sw_gate.sh@54b138005b3f3d86e148446c7b0295845cd69e8d"
product_size: 8 Rust and 10 TOML files plus Cargo.lock and emu/README.md (678 lines under firmware/, excluding target/); sw_gate.sh 300 lines; test_cases.json 117 lines; report 170 lines with 14 artifacts
sprint: FW-B0 (07 section 3.2)
author_agent: author:fw-b0 (Claude, software lead; uncommitted working tree on 28e49e6)
reviewer_agent: reviewer:fw-b0
criticality: neither
assurance_required: false
assurance_reviewer_agent: none
iteration: 3
readiness_met: false
reviewer_verdict: NEEDS CHANGES
assurance_verdict: not-required
verdict: NEEDS CHANGES
findings_major: 2
findings_minor: 10
findings_open: 2
findings_fixed: 9
findings_verified: 9
findings_deferred: 1
assurance_findings_major: 0
assurance_findings_minor: 0
assurance_tasks_applied: []
unsafe_sites_reviewed: 0
deferred_rids: []
items_no: [CK-CODE-C1, CK-CODE-C4, CK-CODE-C7, CK-CODE-D1, CK-CODE-D9, CK-CODE-G5, CK-CODE-H2, K5, K6, K7]
effort_turns: 72
effort_minutes: 105
record_status: Open
date: 2026-09-26
date_closed: null
---

# Peer review record INSP-016: FW-B0 toolchain proof

**Checklist:** `docs/templates/peer-review-checklist-code.md` revision B (items CK-CODE-A1 to J4), applied to every Rust file of the workspace, plus reviewer-added section K for the three non-Rust products (gate script, case, report), because no template covers a gate script or a verification report and the assignment names them as one product with the code. **Record format:** 01 section 13 (Peer review record row) and 08 section 3.2. **Scope note (SWE-087 d):** the template asks for one file per review; the assignment defines the FW-B0 set as one product, so each item below names the file it was answered on.

**Verdict (iteration 3, 2026-09-26, at HEAD `adcfe09`): NEEDS CHANGES.** F-01 and F-02 (Major) stay Open on owner rulings (package decisions 108, 109, 110 and owner action OA-1); F-04 (Minor) is a lien; the other nine findings are Closed (section "Iteration 3" below). **Iteration 1 verdict: NEEDS CHANGES.** Two Major findings: the FW-B0 exit criterion of 07 section 3.2 is not met (the gate exits 1, reproduced), and `cwht-app` carries a second decision in target-only code against CS-11 and CS-38 without an approved deviation. Ten Minor findings. The workspace itself is sound: every build, test, format and lint result in the report reproduced exactly, the release ELF rebuilt bit-identical in a separate target directory, all 14 artifact SHA-256 values and the procedure blob match, and all seven gate known-answer runs reproduced.

## Product files (git hash-object, 2026-09-25)

| Blob | File |
|---|---|
| `7799f6b63e26e8fca0c2cb68270c3ff9d7841d05` | `firmware/Cargo.toml` |
| `784605ca28b94ea0d3ace66a5797c11cbbced80d` | `firmware/Cargo.lock` |
| `ca29c2548ff35887352c340bf5c5b49475758ddb` | `firmware/rust-toolchain.toml` |
| `dce38290b859775f8e3732df729561b198f991a3` | `firmware/rustfmt.toml` |
| `42020b54612e1bcb2c64149353575b6fa6883d96` | `firmware/clippy.toml` |
| `4cd6de9c2f49c9da254ca05cb31973286c9ac2c8` | `firmware/deny.toml` |
| `416883d5ce997a47c5586348c7102689b6333915` | `firmware/.cargo/config.toml` |
| `00b81042cf7f73ff6ffa67f013b4c78ef6884a63` | `firmware/.config/nextest.toml` |
| `236df1403dc94cc8534e9397d6addc819dc3c053` | `firmware/cwht-app/Cargo.toml` |
| `41dea79e96a75c4919491630fd5a83978d3c9f18` | `firmware/cwht-app/build.rs` |
| `64b2b3e49e7388d16f4beac22a0d56cbe1954433` | `firmware/cwht-app/src/main.rs` |
| `3774fca09cead334004aeaa00e07eb2c6ff9d941` | `firmware/cwht-core/Cargo.toml` |
| `01c49f60f82689aab61570e7200bf9bf4064cbd1` | `firmware/cwht-core/src/lib.rs` |
| `f38b716a57d7e88bdbcb0cc5d20fb270ea75e71f` | `firmware/cwht-core/src/heartbeat.rs` |
| `718a0246da10eec9c8f3be5d939d326e2133cb4c` | `firmware/cwht-core/tests/heartbeat.rs` |
| `565c5597b2b4e0d4611fd2e1079f653cd4337f41` | `firmware/cwht-hal-mock/Cargo.toml` |
| `f5141c137073e0493a455681aa1d5ae18f53db38` | `firmware/cwht-hal-mock/src/lib.rs` |
| `59b991e2450d16874d845cb957e1d0900e7866e4` | `firmware/cwht-hal-mock/src/gpio.rs` |
| `f1b302bcfa7f55105ad73d8b01d98d0fb7901312` | `firmware/cwht-hal-mock/tests/gpio.rs` |
| `ae79ea6c77595157c0774a136735191196c03d99` | `firmware/emu/README.md` |
| `d74436ab93d20e1ab5889ea4bd1ab12ca5e5b691` | `tools/sw_gate.sh` (SHA-256 `6bae8445...d9473d`, equal to the value in `gate-known-answer.txt`) |
| `04d08adfffce810b6933f42d242ef124f88f4162` | `docs/test_cases/sw-tool/test_cases.json` (equals the report's `procedure_blob`) |
| `3b180d100096a782ce13f4ba2a40470969693f4b` | `docs/vv/reports/TC-SW-TOOL-001-r1.md` |
| `22e56c97597f7dae54d5a9168162a9ffb0fc620a` | `docs/vv/reports/TC-SW-TOOL-001-r1/versions.txt` |
| `ca478c7e9eb0243b0561e744b10165ebf28ee652` | `docs/vv/reports/TC-SW-TOOL-001-r1/host-build-test.txt` |
| `3fca1c2c9510e9dfd34b24c71811f703743899d9` | `docs/vv/reports/TC-SW-TOOL-001-r1/sw-gate-full.txt` |
| `b31755e2afac05c3c217180147f2f04a80ade42c` | `docs/vv/reports/TC-SW-TOOL-001-r1/sw-gate-keep-going.txt` |
| `eaaca0e699da5312e85c5750e7228cfc1d87a5c4` | `docs/vv/reports/TC-SW-TOOL-001-r1/gate-known-answer.sh` |
| `df92abe952c77acfbbf48d61a90491be3b9e3fe5` | `docs/vv/reports/TC-SW-TOOL-001-r1/gate-known-answer.txt` |
| `2aa80fcc749a3b2fb5e949341ad7f6344dfaf227` | `docs/vv/reports/TC-SW-TOOL-001-r1/blinky-build.txt` |
| `5dd8b02ad79c8544fed5e6059e2a4626bcabe822` | `docs/vv/reports/TC-SW-TOOL-001-r1/rustos-blinky.elf` |
| `f0e9fb343ed9c24f0e5b791fc344b51093c48ab9` | `docs/vv/reports/TC-SW-TOOL-001-r1/rustos-blinky.uf2` |
| `6d9965a04a81895a5a2e355e685aa07ae5f65f7a` | `docs/vv/reports/TC-SW-TOOL-001-r1/cwht-app.elf` |
| `640951c4994cbc5e8a45e8f89eff3879795da144` | `docs/vv/reports/TC-SW-TOOL-001-r1/cwht-app.uf2` |
| `e5557024967701cbee3661601e39572bf22afa80` | `docs/vv/reports/TC-SW-TOOL-001-r1/cwht-app.map` |
| `ea4694c2a3fa09a86fc227d32f2fe5edb5a1362e` | `docs/vv/reports/TC-SW-TOOL-001-r1/uf2-info.txt` |
| `78f1ac59aeaf1254d2e4ba0b6c2c5972cb94d5a9` | `docs/vv/reports/TC-SW-TOOL-001-r1/blink-rate-prediction.txt` |

## Reviewer's own runs (2026-09-25 local, 2026-09-26T04:03Z gate time stamps)

All with `RUSTUP_TOOLCHAIN=stable`, `RUSTUP_AUTO_INSTALL=0`; `rustc 1.98.0 (88d9e12ae 2026-08-18)`, equal to the lock rustc row. rustos HEAD `c54d35aa8e7f9ad30f6508bca458a59c1fc009db` (lock row), `api/` and `firmware/` clean before and after.

| Run | Command (in `firmware/` unless stated) | Exit | Result |
|---|---|---|---|
| 1 | `cargo build` | 0 | host crates build |
| 2 | `cargo test` | 0 | 10 passed (5 `cwht-core`, 5 `cwht-hal-mock`), 0 failed |
| 3 | `cargo fmt --check` | 0 | no diff |
| 4 | `cargo clippy --workspace --exclude cwht-app --all-targets -- -D warnings` | 0 | no warning |
| 5 | `cargo clippy -p cwht-app --target thumbv8m.main-none-eabihf -- -D warnings` | 0 | no warning |
| 6 | `cargo build -p cwht-app --release --target thumbv8m.main-none-eabihf` with `CARGO_TARGET_DIR` in the reviewer's scratch directory (clean build) | 0 | FLASH 1608 B (0.04 %), RAM 8200 B (1.54 %); ELF SHA-256 `3992e5d8...80ec1`, identical to the report's `cwht-app.elf`; one rustc warning `linker_messages` (finding-12) |
| 7 | `sh tools/sw_gate.sh` (repo root) | 1 | G0 to G3: 11 PASS; `FAIL G4 traceability` (violations in `docs/requirements/sw/sw-keyer/`, `docs/requirements/tx/`, none in a product file) |
| 8 | `sh tools/sw_gate.sh --keep-going` | 1 | 2 FAIL (G4; G5 cargo deny: `api` and `pico2` unlicensed, `pico2` wildcard path dependency), 9 MISSING, 3 geiger PASS, G6 stable coverage PASS; same result lines as `sw-gate-keep-going.txt` |
| 9 | `sh docs/vv/reports/TC-SW-TOOL-001-r1/gate-known-answer.sh <scratch>` | 0 | KA-0 to KA-6 all MATCH, same first FAIL lines as `gate-known-answer.txt` |
| 10 | clippy on the KA-4 copy | 101 | three distinct errors: `usage of an unsafe block`, `use of a disallowed method core::mem::transmute`, `unnecessary transmute`: the report's "three independent detections" claim holds |
| 11 | `shasum -a 256` on the 14 artifacts; `git hash-object` on the case file | 0 | all 14 equal the front matter; blob equals `procedure_blob` |

Numbers checked against sources: the ring oscillator range 4.6 MHz to 19.6 MHz, nominal 11 MHz (rustos `docs/extracted/rp2350-datasheet.md` lines 37428 to 37429); the delay constant `movw #0x4b40` / `movt #0x4c` = 5 000 000 in `blink-rate-prediction.txt`; the blink windows recomputed (blinky 66 to 132 cycles per 64 spins gives 13.4 to 114.0 per 60 s, nominal 63.0; cwht-app 3 to 6 cycles per spin gives 4.6 to 39.2, nominal 16.5), all equal; `rust-size` sections 272 + 20 + 1316 = 1608 B, equal to the linker FLASH figure; the gate memory limits 70 % and 75 % used equal the TPM-010 red line "below 30 %" unused and the TPM-011 red line "below 25 %" unused (`docs/plan/tpm.json`); the three requirement statements of the report section 1 equal `docs/requirements/sys/requirements.json` (REQ-SYS-127 and 128 Inspection, REQ-SYS-133 Demonstration, all Draft); "rule 7.3.12" and the `SUPPORT` row resolve in `docs/process/04-verification-and-validation.md` (lines 83, 124, 251, 283).

## Readiness criteria

| # | Criterion | Answer | Evidence |
|---|---|---|---|
| R1 | Gate G1 passes on the crates | Yes | runs 3 to 5 above |
| R2 | File at most 500 lines; functions at most 60 lines | Yes | largest file `cwht-hal-mock/src/gpio.rs` 135 lines; clippy `too_many_lines` at threshold 60 (`clippy.toml:2`) passes |
| R3 | The design unit is Active and named in `// @design` | No | no software design exists before PDR (`docs/design/software-design.md` is a CDR product, 07 section 3.1); the tags `cwht-core/heartbeat`, `cwht-hal-mock/gpio`, `cwht-app/main` name units that no design document defines. Inherent to FW-B0, so no finding is raised; this is why `readiness_met` is false |
| R4 | `@req` tag for every requirement assigned | N/A | the brief assigns no `REQ-SW-*` (`heartbeat.rs:7-8`) |
| R5 | Test author's file exists | Yes, with finding-4 | `cwht-core/tests/heartbeat.rs`, `cwht-hal-mock/tests/gpio.rs` |
| R6 | `tools/unsafe_audit.py --check` for `pico2` or `api` | N/A | no rustos file is in this product; rustos is read only |

## Participants

Author agent `author:fw-b0` (absent). Reviewer agent `reviewer:fw-b0`. Software assurance reviewer not required: no file contains `unsafe` and no file belongs to a component of 07 section 14.1 (`criticality: neither`). Owner for dispositions.

## A. Environment, dependencies and build

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-A1 | Yes | `cwht-core/src/lib.rs:13`, `cwht-hal-mock/src/lib.rs:11`, `cwht-app/src/main.rs:10-11` (`#![no_std]`, `#![no_main]`); grep for `alloc`, `std::`, `Box`, `Vec`, `String`, `format!` finds only `build.rs:8-9` (`std::env`, `std::path`), which is a host build script, not image code; gate G2 allocator-symbol check PASS |
| CK-CODE-A2 | Yes | dependencies are `api`, `pico2` (rustos by path) and the workspace crates only (`Cargo.lock`, 5 packages); `deny.toml:23-29` denies every other crate; gate G2 image dependency set PASS |
| CK-CODE-A3 | Yes | no `#[cfg` and no `debug_assert!` in any `.rs` file |

## B. Unsafe code

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-B1 | Yes | workspace lint `unsafe_code = "forbid"` (`Cargo.toml:30`) and `#![forbid(unsafe_code)]` in each crate root and in `build.rs:6`; grep finds no `unsafe` block; geiger `:)` for all three crates (run 8) |
| CK-CODE-B2 to B8 | N/A | no `unsafe` in the product; no `pico2` or `api` file in scope; no `static mut` (`static_mut_refs = "deny"`, `Cargo.toml:32`); CS-10 functions banned in `clippy.toml:4-16` and shown effective by run 10 |

## C. Panics, errors and arithmetic

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-C1 | No | no `unwrap`, `expect`, `panic!`, indexing or slicing in source (`gpio.rs:59` uses `get(..).unwrap_or(&[])`); but `main.rs:36-38` adds a second halt arm, `let Ok(mut led) = gpio.output_from_handle(..) else { safe_state_halt() }`, beyond the single board `take()` arm CS-11 permits (finding-2) |
| CK-CODE-C2 | Yes | `Heartbeat::step` returns `Result<bool, P::Error>` (`heartbeat.rs:48`); `MockGpioError` is a module enum (`gpio.rs:12-15`); `main.rs:42` `let Ok(_level) = ..` is irrefutable because `Rp2350GpioOut` has `Error = Infallible` (rustos `firmware/pico2/src/gpio/gpio.rs`), so no error is dropped; no `let _ =` on a `Result` |
| CK-CODE-C3 | N/A | no design error table exists (R3); the one error enum has one variant used only by tests |
| CK-CODE-C4 | No | `gpio.rs:77` `checked_sub(1)` and `gpio.rs:83` `saturating_add(1)` carry no comment on the choice CS-14 asks for (finding-5); `for _ in 0..count` (`heartbeat.rs:61`) has no arithmetic |
| CK-CODE-C5 | Yes | no `as` cast in any `.rs` file; `as_conversions = "deny"` (`Cargo.toml:48`) |
| CK-CODE-C6 | Yes | no `f32` or `f64` in any file (none is safety-critical in any case) |
| CK-CODE-C7 | No | `main.rs:56-59`: the panic handler only halts; it writes no safe-state register, records no marker and requests no watchdog reset (CS-12). FW-B0 has no safe-state outputs, which the comment says, but no deferral to a gate is recorded (finding-3) |

## D. Structure, complexity and target platform rules

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-D1 | No | no G5 complexity output exists: `rust-code-analysis-cli` is not installed and `tools/complexity_gate.py` is not written (run 8, two MISSING lines); clippy `cognitive_complexity` at 15 passes, which is not the CS-17 measure (finding-1) |
| CK-CODE-D2 | Yes | loops: `main.rs:40` main loop, `main.rs:50` halt loop, `heartbeat.rs:61` over `0..count`; no recursion |
| CK-CODE-D3 | Yes | no `match` on an enum in `cwht-core`; `gpio.rs:75-79` matches an `Option<u32>` with explicit arms and no `_ =>`; `wildcard_enum_match_arm = "deny"` |
| CK-CODE-D4 | Yes | no `#[allow]` or `#[expect]`; shadow lints denied (`Cargo.toml:50-52`) and clippy clean |
| CK-CODE-D5 | N/A | no interrupt handler |
| CK-CODE-D6 | Yes | nothing references core 1 |
| CK-CODE-D7 | Yes | longest function `MockOutput::write` 14 lines; nesting depth at most 3 |
| CK-CODE-D8 | N/A | no NVIC, IO_BANK0 interrupt, PWM or TICKS access in the product; GPIO goes through the rustos driver |
| CK-CODE-D9 | No | `main.rs` is tagged `// @target-only` (line 2) and holds two decisions (the `take()` match and the `output_from_handle` match), so its cyclomatic complexity is 3 against the CS-38 limit of 1 plus the `take()` match; the report section 9 item 5 raises the rule conflict as a recommendation only, with no CR or deviation (finding-2) |

## E. Correctness against design and requirements

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-E1 | N/A | no design to compare (R3); the behaviour matches the file's own contract: `Heartbeat::step` toggles and keeps the level on a failed write (`heartbeat.rs:48-53`, test `failed_write_keeps_level_and_retries_same_transition`) |
| CK-CODE-E2 | Yes | the one constant `BLINK_HALF_PERIOD_SPINS` (`heartbeat.rs:20`) carries its unit in the name and its source in the doc comment; no requirement value applies |
| CK-CODE-E3 to E8 | N/A | no keyer, register, guard, I/O read-back, `safe_state()` or integrity code in FW-B0 |
| CK-CODE-E9 | Yes | every public item is used by `cwht-app` or by a test; `MockInput` is test tooling exercised by `input_reads_set_level_and_injected_fault` |

## F. Traceability tags

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-F1 | Yes | `// @design` headers at `main.rs:1`, `heartbeat.rs:1`, `gpio.rs:1`; correctness against a design cannot be judged before the design exists (R3) |
| CK-CODE-F2 | N/A | no requirement assigned |
| CK-CODE-F3 | Yes | the units are the FW-B0 infrastructure that 07 section 3.2 names ("Workspace skeleton ... blinky"); the files state that they implement no `REQ-SW-*` (`heartbeat.rs:7-8`, `cwht-core/tests/heartbeat.rs:1-2`) |

## G. Secure coding

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-G1 | N/A | no external input in FW-B0 |
| CK-CODE-G2 | N/A | no key line |
| CK-CODE-G3 | Yes | `HISTORY_CAPACITY` named (`gpio.rs:8`); writes past capacity are dropped through `get_mut` (`gpio.rs:81`) |
| CK-CODE-G4 | N/A | no diagnostic interface, no event log |
| CK-CODE-G5 | No | the G5 output shows `FAIL G5 cargo deny` and MISSING for `cargo audit`, deny advisories, unsafe audit, complexity and Miri (run 8); zero findings is not shown (finding-1) |

## H. Tests and testability

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-H1 | Yes | `Heartbeat::step` is generic over `api::common::Write<bool>`; `spin_wait` takes the spin action as a closure, so the host test counts calls (`heartbeat.rs:60`); no `RegAddr` in `cwht-core` |
| CK-CODE-H2 | No | tests pass twice with identical result sets (run 7, G3), but both test files were written by the code author (report section 2: "Claude created the firmware workspace"; author summary) (finding-4) |
| CK-CODE-H3 | N/A | no safety-critical file |

## I. Documentation and style

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-I1 | Yes | `missing_docs = "deny"` for every member (`Cargo.toml:31`, `[lints] workspace = true` in each crate); every `pub` item has a doc comment; clippy clean |
| CK-CODE-I2 | Yes | `BLINK_HALF_PERIOD_SPINS`, `HISTORY_CAPACITY`, `writes_before_fault` carry units or meaning |
| CK-CODE-I3 | Yes | runs 3 to 5 |
| CK-CODE-I4 | Yes | comments state reasons (for example `main.rs:22-24` on the private `entry` module, `main.rs:41` on the irrefutable pattern); no commented-out code |

## J. Common review traps

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-J1 | Yes | `Rp2350::take`, `Rp2350Gpio::new`, `output_from_handle`, `board.pins.led`, `pico2::entry!` exist in rustos `c54d35a` (target clippy and build compile against them, runs 5 and 6) |
| CK-CODE-J2 | Yes | `pin.write(next)` (`heartbeat.rs:50`), `gpio.output_from_handle(..)` (`main.rs:36`) are trait calls |
| CK-CODE-J3 | N/A | no compound requirement |
| CK-CODE-J4 | Yes | line counts measured with `wc -l` (678 lines under `firmware/` excluding `target/`, 20 files) |

## K. Reviewer-added checks: gate script, case and report (not template items)

| Id | Check | Answer | Evidence |
|---|---|---|---|
| K1 | Every build, test and lint result claimed in the report reproduces | Yes | runs 1 to 6, 11 |
| K2 | The gate result lines claimed in the report reproduce, including the counts (11 PASS through G3; 9 MISSING) | Yes | runs 7 and 8 |
| K3 | The known-answer runs reproduce and discriminate | Yes | runs 9 and 10 |
| K4 | Artifact hashes and procedure blob match; the release image is reproducible | Yes | run 11; run 6 rebuilt the ELF bit-identical in a clean target directory |
| K5 | The FW-B0 content and exit criteria of 07 section 3.2 are met | No | gate exit 1; `tools/emu_run.sh` (a FW-B0 deliverable of 07 section 1.2 row "Scripts"), `tools/unsafe_audit.py`, `tools/complexity_gate.py`, `tools/measurements.py` not written; section 8 tools not all installed; `tools/toolchain.lock.md` section 1.1 sanity checks for rustc and cargo, nextest, llvm-cov, audit, deny, geiger, binutils and picotool read "not yet run"; steps 11 and 12 Pending owner (finding-1) |
| K6 | The gate script is robust and its header matches its behaviour | No | findings 6 and 7 |
| K7 | Every claim in the report is backed by a cited artifact and every deviation from the plan is recorded | No | findings 8 to 11 |
| K8 | The case meets the dev-board rule of 04 section 4: `type` Bench, `Article: pico2-devboard-1.`, `Credit: false (dev-board run, charter section 3).`, `Credit row: SUPPORT.`, and the `Configuration:`, `Safety:`, `Environment:` lines; numeric acceptance criteria; named artifacts | Yes | `docs/test_cases/sw-tool/test_cases.json:13-14, 31, 36-113`; `validate_docs.py` passes the file |
| K9 | The report records the run honestly: `result: Blocked`, `credit: false`, no requirement status changed, no NCR needed for an absent prerequisite | Yes | report front matter lines 8-9 and sections 7 and 9 |
| K10 | rustos is unmodified | Yes | `git -C /Users/robinonsay/rust/rustos status --porcelain -- api firmware Cargo.toml Cargo.lock .cargo` empty; HEAD equals the lock row |

## Findings

| Finding | Origin | Severity | Item | Location | Description | State | Disposition |
|---|---|---|---|---|---|---|---|
| F-01 <a id="finding-1"></a>finding-1 | reviewer | Major | K5, CK-CODE-D1, CK-CODE-G5 | `tools/sw_gate.sh` result; 07 section 3.2 row FW-B0; 07 line 28 | The FW-B0 exit criterion is not met: `tools/sw_gate.sh` exits 1 in both modes (reproduced: FAIL G4, FAIL G5 cargo deny, 9 MISSING), so SRR package item H12 and criterion row 20 stay Not met. Four of the gaps are software-lead deliverables that need no download: `tools/emu_run.sh` (07 section 1.2 says it is written in FW-B0 as the SKIP-line stub), `tools/unsafe_audit.py`, `tools/complexity_gate.py`, `tools/measurements.py`. The rest need owner-approved installs (pinned 1.98.0, `miri` and `llvm-tools` on `nightly-2026-08-24`, `rust-code-analysis-cli`, RustSec database), the rustos manifest change for cargo deny, and a clean repository-wide traceability run for G4. The second exit criterion (lock lists every tool with version and sanity-check result) is also not met. Fix: write the four scripts; obtain the owner's approval for the installs and record them in the lock; run and record the lock section 1.1 sanity checks; re-run the gate to exit 0 and file run 2 after steps 11 and 12 | Open | Open (iteration 2). Not addressed in the author return: none of `tools/emu_run.sh`, `tools/unsafe_audit.py`, `tools/complexity_gate.py`, `tools/measurements.py` exists, the lock sanity checks are not recorded and the gate is not shown to exit 0 in full mode (the reviewer `--keep-going` run KA-8 still lists 9 MISSING). Major stays Open. **Iteration 3: Open, owner ruling needed (decisions 109 and 110, OA-1).** The four scripts are committed at HEAD; reviewer run IT3-1 exits 1 with 2 FAIL (G5 cargo deny; G5 unsafe audit, 36 rustos sites without CS-06 SAFETY comments) and 5 MISSING; lock section 1.1 rows for cargo-llvm-cov, nightly, cargo-nextest, cargo-audit, cargo-deny, cargo-geiger, cargo-binutils still read "not yet run" (`tools/toolchain.lock.md:69-75`) |
| F-02 <a id="finding-2"></a>finding-2 | reviewer | Major | CK-CODE-C1, CK-CODE-D9 | `firmware/cwht-app/src/main.rs:36-38` | Target-only code holds a second decision, the `output_from_handle` `let ... else` halt arm, which CS-11 (only the `take()` `None` arm) and CS-38 (straight-line except the `take()` match) do not permit; the rustos driver returns `GpioError`, so the arm is needed, and the report (section 9 item 5) proposes changing the rules, but no CR or recorded deviation covers the code as filed (charter section 11 rule 5). Fix: an owner-dispositioned CR amending CS-11 and CS-38 to admit driver-construction failure arms that call `safe_state_halt()`, or an entry in `docs/cm/deviations.md`, cited by a comment at `main.rs:36` | Open | Open (iteration 2). Partly addressed: `main.rs:36-40` now cites deviation D8, recorded in report section 2 line 71 and section 9 item 5. The fix asked for an owner-dispositioned CR or an entry in `docs/cm/deviations.md`; neither exists (`docs/cm/` holds only `tool-validation/`, no `cr/` folder and no `deviations.md`). A deviation written in the run report by the author is not an approved deviation (charter section 11 rule 5; 07 section 10.2 action tracking). Author agrees it closes on the owner disposition. Major stays Open. **Iteration 3: Open, owner ruling needed (decision 108).** `main.rs:36-40` now cites `docs/cm/cr/CR-001-cs11-cs38-driver-construction-arms.md`, but CR-001 front matter reads `status: Submitted`, `disposition: null` (lines 4, 18) and `docs/cm/deviations.md` does not exist at HEAD |
| F-03 <a id="finding-3"></a>finding-3 | reviewer | Minor | CK-CODE-C7 | `firmware/cwht-app/src/main.rs:55-59` | The panic handler halts only; CS-12 content (safe-state registers, marker, watchdog reset) is absent. Acceptable for a board with no safe-state outputs, but the deferral is recorded only in a doc comment. Fix: record the deferral with its gate (FW-B1 sprint record or package open-items list) and cite it in the comment | Verified | Closed. `main.rs:60-64` cites deferral FD-1; report section 9 deferral table row FD-1 (line 170) names CS-12, the gate FW-B1 and the evidence. Adding FD-1 to the package open-items list remains a cross item |
| F-04 <a id="finding-4"></a>finding-4 | reviewer | Minor | CK-CODE-H2 | `firmware/cwht-core/tests/heartbeat.rs`, `firmware/cwht-hal-mock/tests/gpio.rs` | Both test files were written by the author of the code they test (charter section 2 and section 11 rule 4). No requirement is verified by them, which keeps this Minor. Fix: have an independent test-author invocation review or replace the tests, or have 07 section 3.2 state that FW-B0 toolchain-proof tests are exempt | Lien | Open (iteration 2). Not addressed in the author return; no independent test-author review exists and 07 section 3.2 carries no exemption. **Iteration 3: Lien: fix before PDR** (convergence rule of 2026-09-26; package item R4, Routine). Both test files are unchanged at HEAD (blobs `718a0246`, `f1b302bc`) |
| F-05 <a id="finding-5"></a>finding-5 | reviewer | Minor | CK-CODE-C4 | `firmware/cwht-hal-mock/src/gpio.rs:77, 83` | `checked_sub(1)` and `saturating_add(1)` carry no comment on why that arithmetic form was chosen (CS-14). Fix: one comment per site (the `Some(0)` arm makes the `checked_sub` total; `len` cannot pass `HISTORY_CAPACITY` because `get_mut` gates the increment) | Verified | Closed. `gpio.rs` `write`: one CS-14 comment above the `checked_sub` arm and one above the `saturating_add`; both reasons are correct (the `Some(0)` arm returns first; `get_mut` succeeding bounds `len`). `cargo fmt --check` exit 0 and reviewer KA-0 clippy PASS |
| F-06 <a id="finding-6"></a>finding-6 | reviewer | Minor | K6 | `tools/sw_gate.sh:176-189` | When a nextest run fails, the `cp` to `runN-junit.xml` is skipped but the comparison step still reads `run1-junit.xml` and `run2-junit.xml`, which may be left from an earlier invocation; in `--keep-going` mode the line `PASS G3 identical result sets` can then print against stale files (the overall gate still fails). Fix: `rm -f` both files before the loop and fail the comparison when either is absent or older than the run | Verified | Closed. `sw_gate.sh:235` removes both copies; lines 245-246 fail the comparison when either is absent. Reviewer KA-8 (stale identical `run1/run2-junit.xml` planted, failing test seeded, `--keep-going`): stale files removed, `FAIL G3 identical result sets (JUnit file of run 1 or run 2 not written by this invocation)`, exit 1 |
| F-07 <a id="finding-7"></a>finding-7 | reviewer | Minor | K6 | `tools/sw_gate.sh:21-23` versus lines 129, 133, 155, 165; case step 6 | The header says `--keep-going` "runs G1 to G6 past a FAIL" and names only G0 as stopping, and case step 6 says it "runs every step", but G2 build, link-map presence, `rust-nm` and `cargo tree` failures call `fatal()` and stop the script. Fix: document the G2 stops in the header and the case, or convert them to `fail()` where the later steps can still run | Verified | Closed. `fatal()` now appears only at setup (line 89) and G0 (lines 94-119); every G2 check uses `fail()` and the ELF, map and `rust-nm` steps are gated on `G2_BUILT` (lines 133-218); header lines 26-30 and case step 6 state that only setup and G0 failures stop the script |
| F-08 <a id="finding-8"></a>finding-8 | reviewer | Minor | K7 | report section 2 deviations; `tools/sw_gate.sh:4-5, 21` | The gate adds a G0 toolchain-identity step that 07 section 8.4 and Annex C do not list, and `--quick` runs G0 to G3 where 07 section 8.4 says G1 to G3; deviations D1 to D5 do not record this. Fix: add a deviation to the report and raise the 07 section 8.4 update (cross item) | Verified | Closed. Deviation D7 in report section 2 (line 70) and gate header lines 21-22; the 07 section 8.4 and Annex C update stays a cross item |
| F-09 <a id="finding-9"></a>finding-9 | reviewer | Minor | K7 | report section 5, "Reproducibility" | The statement that the cwht-app UF2 was identical before and after a rebuild that changed only debug information cites `uf2-info.txt`, which records one set of hashes and no rebuild (charter section 11 rule 2). The reviewer's clean rebuild (run 6) did reproduce the ELF bit for bit, so the claim can be evidenced. Fix: record the rebuild and both hashes in an artifact, or delete the sentence | Verified | Closed. Report section 5 "Reproducibility" (line 130) now claims rebuild identity for the blinky only, backed by `blinky-build.txt` (two identical SHA-256 `ef16271d...`), cites reviewer run 6 for cwht-app, and assigns the cwht-app rebuild record to run 2 |
| F-10 <a id="finding-10"></a>finding-10 | reviewer | Minor | K7 | report sections 2 and 3; 07 section 3.2 row FW-B0 | 07 asks for a "blinky on the cwht pin map"; `cwht-app` drives the Pico 2 on-board LED (GPIO25) because the pin map (`docs/icd/ICD-CTL-SW.md`, a PDR product, 07 row o) does not exist (`docs/icd/` is empty). The substitution is sound but is not recorded as a deviation. Fix: add it to the deviation list | Verified | Closed. Deviation D6 (report line 69), configuration note (line 79) and deferral FD-2 (line 171) |
| F-11 <a id="finding-11"></a>finding-11 | reviewer | Minor | K7 | report section 1 (REQ-SYS-128 row) and section 9; `tools/toolchain.lock.md` cargo-llvm-cov row | The report cites 100 percent line and region coverage, while the lock's cargo-llvm-cov row says its TV is due "before FW-B0 coverage is cited". The report does label all output as developer evidence (section 3), so the conflict is one of wording. Fix: mark the coverage figure at each citation as developer evidence pending the cargo-llvm-cov TV, or file that TV first | Verified | Closed. Every coverage citation (report lines 55, 93, 127, 155) carries the developer-evidence and cargo-llvm-cov TV pending label |
| F-12 <a id="finding-12"></a>finding-12 | reviewer | Minor | K6 | `firmware/.cargo/config.toml:9` | `--print-memory-usage` makes every target build emit the rustc warning `linker_messages` (reproduced in run 6), so the G2 log always carries a warning and a new build warning would not stand out; G1 checks clippy only. Fix: take the memory figures from the link map (measurements.py) and have G2 fail on any compiler warning other than a documented expected one | Verified | Closed. `--print-memory-usage` removed (`.cargo/config.toml`, blob `b677319f`); G2 fails on any `^warning` line (`sw_gate.sh:142-149`) and takes memory from the link map and `link.ld` MEMORY. Reviewer KA-0: no warning line, FLASH 1608 B (0.04 %), RAM 8200 B (1.54 %), equal to run 1; reviewer KA-7 (`cargo:warning` in `build.rs`): `FAIL G2 no compiler warning`, exit 1 |

## Cross items (outside this product; for the owners of those files)

- `tools/toolchain.lock.md` section 1.2 row `tools/sw_gate.sh` still reads "not written"; the rustup row (line 16) says the `firmware/` pin is "not yet committed". Update both as Log changes.
- `docs/process/07-software-engineering-plan.md` section 8.4 and Annex C: add G0 and the `MISSING` exit status 3; reconcile the FW-B0 need for `tools/unsafe_audit.py`, `tools/complexity_gate.py` and `tools/measurements.py` with the lock section 1.2 due dates (CDR, CDR, PDR).
- rustos (owner): `publish = false` and `license` in `api/Cargo.toml` and `firmware/pico2/Cargo.toml` (report section 9 item 3) to clear gate G5 cargo deny.

## Closure (iteration 2, 2026-09-25, reviewer:fw-b0, new invocation)

**Author return:** fixed F-02 (partly), F-03, F-05 to F-12; disputed none; F-01 and F-04 not addressed. **Result:** 9 Verified (F-03, F-05 to F-12), 3 Open (F-01 Major, F-02 Major, F-04 Minor), 0 Deferred, 0 disputes. The record stays `record_status: Open` and `verdict: NEEDS CHANGES` (07 section 10.2: Closed only when every finding is Verified or Deferred).

Revised product files (git hash-object, 2026-09-25; unlisted files unchanged from the table above):

| Blob | File |
|---|---|
| `b677319fa0fe9b62431d01fa8b749bbd7e585b0d` | `firmware/.cargo/config.toml` |
| `b2464fb270ad04a15f9c75dd0b56e8ec386cf309` | `firmware/cwht-app/src/main.rs` |
| `fc8872bd420ecbd4760d2f2fc05b236ee842c801` | `firmware/cwht-hal-mock/src/gpio.rs` |
| `93bffdeb67579e427ce1b776529a2862787faea1` | `tools/sw_gate.sh` (362 lines, SHA-256 `fe206ee7...433d0b`) |
| `fee1e7246af59d5e8a43ed1b9cdf483854053fdc` | `docs/test_cases/sw-tool/test_cases.json` |
| `04bc3354352139eb30b33fadff43e1c9b61d0d8e` | `docs/vv/reports/TC-SW-TOOL-001-r1.md` |

The 14 run 1 artifacts are unchanged (`shasum -a 256` equal to the report front matter, including `cwht-app.elf` `3992e5d8...`); the report records the post-run edits in its section 10 without altering the run 1 results.

Reviewer runs of iteration 2 (seeded copies of `firmware/` plus the revised `tools/sw_gate.sh` and `tools/toolchain.lock.md` in the reviewer scratch directory, same construction as `gate-known-answer.sh`; `RUSTUP_TOOLCHAIN=stable`, rustc 1.98.0, rustos `c54d35a`):

| Run | Seed and mode | Exit | First FAIL line and result |
|---|---|---|---|
| KA-0 | unmodified, `--quick` | 0 | no FAIL; 11 PASS G0 to G3 plus `G2 no compiler warning`; FLASH 1608 B of 4194304 B (0.04 %), RAM 8200 B of 532480 B (1.54 %); no `warning` line in the G2 log |
| KA-6 | unwrap in `cwht-app`, `--quick` | 1 | `FAIL G1 clippy target` (regression check of run 1 KA-6) |
| KA-7 | `println!("cargo:warning=...")` in `cwht-app/build.rs`, `--quick` | 1 | `FAIL G2 no compiler warning` |
| KA-8 | identical stale `run1-junit.xml` and `run2-junit.xml` planted, failing host test seeded, `--keep-going` | 1 | `FAIL G3 host tests run 1`, `FAIL G3 host tests run 2`, `FAIL G3 identical result sets (JUnit file of run 1 or run 2 not written by this invocation)`; stale files gone after the run; 9 MISSING still reported |

Open items needed to close the record: F-01 (four scripts, owner-approved installs, lock sanity checks, gate exit 0 and run 2), F-02 (owner-dispositioned CR amending CS-11 and CS-38, or an owner-approved entry in `docs/cm/deviations.md`), F-04 (independent test-author review of the two test files, or a 07 section 3.2 exemption by CR).

## Iteration 3 (2026-09-26, reviewer:fw-b0, new invocation)

**Review baseline:** HEAD `adcfe0946d2f1b5cd8f41a8f91eb4219a7fb99a1`. Every reviewed file is named with its committed blob (`git rev-parse HEAD:<path>`) in the front matter `product_files` (37 files). Against the iteration 2 table, two files changed: `firmware/cwht-app/src/main.rs` (reviewed `b2464fb2`, not in the object store; HEAD `e32006a5`) and `tools/sw_gate.sh` (reviewed `93bffdeb`; HEAD `54b13800`). The other 35 blobs equal the iteration 1 and 2 tables. **Rule applied:** convergence rule of the lead SE, 2026-09-26 (charter section 4 item 3: a Minor RID is fixed before the next review and does not block the baseline): only Major findings change products in this round; every Minor finding is dispositioned "Lien: fix before PDR".

**Search:** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` (record drift rule) before any manual search; `grep -n` used afterwards only to pin lines.

**Changed text reviewed (scan for new Major defects):**

- `main.rs` (diff against the iteration 2 quote): the comment at lines 36-40 now cites CR-001 and states "owner disposition before FW-B1", which matches CR-001 section 1 item 4 and package decision 108 ("Needed by: SRR memo (before FW-B1)"). Code unchanged: the two halt arms at lines 32-34 and 41-43 are the ones F-02 names. No new defect.
- `tools/sw_gate.sh` (`git diff 93bffdeb 54b13800`, two hunks): header lines 44-48 name the three scripts and state that the inline Python checks run only when `tools/measurements.py` is absent, which lines 159-162 and 249-252 implement; line 331 removes the three G6 outputs before G6, so the G6 measurements step reads only files this invocation wrote (reviewer run IT3-1: `MSR-14 NOT PRODUCED`, `emulation report NOT PRODUCED`). `PASS G6 emulation` on the stub's `SKIP` line is what 07 section 8.4 row G6 specifies before PDR ("or the `SKIP` line before PDR", 07 line 357). No new defect.
- Outside this product but read as evidence for F-01: `docs/vv/reports/TC-SW-TOOL-001-r2.md` (blob `de5c9403`), `tools/emu_run.sh` (`17f102aa`), `tools/unsafe_audit.py` (`cc3aaa2a`), `tools/complexity_gate.py` (`9214fefb`), `tools/measurements.py` (`abe25acb`), CR-001 (`d582073e`). The run 2 result lines (2 FAIL, 5 MISSING, exit 1) equal reviewer run IT3-1. Their own review belongs to the records of those products (TV-011 to TV-013; a run 2 report review is a cross item).

**Reviewer run of iteration 3** (repository root, `RUSTUP_AUTO_INSTALL=0`, rustc 1.98.0 via stable per G0, rustos HEAD `c54d35aa8e7f9ad30f6508bca458a59c1fc009db`; `git status --porcelain firmware tools` empty before and after):

| Run | Command | Exit | Result |
|---|---|---|---|
| IT3-1 | `sh tools/sw_gate.sh --keep-going` (gate time stamp 2026-09-26T08:15:00Z, repo `adcfe09`) | 1 | G0 to G4 all PASS (G4 traceability now PASS; FLASH 1608 B 0.04 %, RAM 8200 B 1.54 % through `tools/measurements.py --link-map`; G3 identical result sets through `--diff-runs`); `FAIL G5 cargo deny (bans, licenses, sources)`; `FAIL G5 unsafe audit` (36 rustos `api` and `pico2` sites without a CS-06 `// SAFETY:` comment); 3 geiger PASS; `PASS G6 coverage (stable, MSR-13)`; `SKIP emulation: no accepted emulator ADR` then `PASS G6 emulation`; `PASS G6 measurements`; 5 MISSING (cargo audit database, cargo deny advisories database, `rust-code-analysis-cli`, Miri, nightly llvm-tools); final line `sw_gate: FAIL (2 step(s) failed, 5 prerequisite(s) missing)` |

**Disposition table (iteration 3):**

| Finding | Severity | Iteration 3 disposition | Evidence at HEAD `adcfe09` |
|---|---|---|---|
| F-01 | Major | **Open**, owner ruling needed: package decisions 109 (downloads) and 110 (rustos licence, manifests and the SAFETY-comment work item), owner action OA-1 (steps 11 and 12) | Claude-owned part done: `tools/emu_run.sh`, `tools/unsafe_audit.py`, `tools/complexity_gate.py`, `tools/measurements.py` committed (blobs above). Not met: gate exit 1 (IT3-1: FAIL G5 cargo deny, FAIL G5 unsafe audit, 5 MISSING); lock section 1.1 sanity checks for cargo-llvm-cov, nightly, cargo-nextest, cargo-audit, cargo-deny, cargo-geiger, cargo-binutils read "not yet run" (`tools/toolchain.lock.md:69-75`; the ones that need no download remain Claude's); steps 11 and 12 Pending owner (`TC-SW-TOOL-001-r2.md` status paragraph). 07 section 3.2 FW-B0 exit criterion not met |
| F-02 | Major | **Open**, owner ruling needed: package decision 108 (CR-001) | `main.rs:36-40` cites CR-001; `docs/cm/cr/CR-001-cs11-cs38-driver-construction-arms.md:4` `status: Submitted`, `:18` `disposition: null`; no `docs/cm/deviations.md` in HEAD |
| F-03 | Minor | Closed | `main.rs:60-64` cites FD-1; `TC-SW-TOOL-001-r1.md:170` row FD-1 (report blob unchanged `04bc3354`) |
| F-04 | Minor | **Lien: fix before PDR** | test files unchanged (`718a0246`, `f1b302bc`); no independent test-author review; package item R4 |
| F-05 | Minor | Closed | `firmware/cwht-hal-mock/src/gpio.rs:77-79` and `:85-87` CS-14 comments (blob `fc8872bd`, unchanged since iteration 2) |
| F-06 | Minor | Closed | `tools/sw_gate.sh:237` removes both JUnit copies; `:247-248` fails the comparison when either is absent |
| F-07 | Minor | Closed | `tools/sw_gate.sh:76` `fatal()` used only at `:91` (setup) and `:96-121` (G0); header `:26-30`; case blob `fee1e724` unchanged |
| F-08 | Minor | Closed | `TC-SW-TOOL-001-r1.md:70` deviation D7; `tools/sw_gate.sh:21-22` |
| F-09 | Minor | Closed | `TC-SW-TOOL-001-r1.md:130` |
| F-10 | Minor | Closed | `TC-SW-TOOL-001-r1.md:69` (D6), `:79`, `:171` (FD-2) |
| F-11 | Minor | Closed | `TC-SW-TOOL-001-r1.md:55, 93, 127, 155` |
| F-12 | Minor | Closed | `firmware/.cargo/config.toml:6` (no `--print-memory-usage`, blob `b677319f`); `tools/sw_gate.sh:144-151` fails G2 on any `^warning` line; IT3-1 `PASS G2 no compiler warning` |

New findings of iteration 3: none (no new Major, no new Minor).

**Lien table (carried by the package as Routine items, "Lien: fix before PDR"):**

| Lien | Finding | Item | Closure action | Owner | Due |
|---|---|---|---|---|---|
| L-016-1 | F-04 (Minor) | CK-CODE-H2 | An independent test-author invocation reviews or replaces `firmware/cwht-core/tests/heartbeat.rs` and `firmware/cwht-hal-mock/tests/gpio.rs`, or a CR exempts FW-B0 toolchain-proof tests in 07 section 3.2; this record then verifies it | Test-author invocation (package item R4); Claude dispatches | Before PDR |

**Verdict (iteration 3): NEEDS CHANGES.** Two Major findings remain Open (F-01, F-02), both waiting on owner rulings; under the convergence rule the record cannot be APPROVED while a Major is Open. One lien (F-04). `record_status` stays Open. When decisions 108 to 110 and OA-1 are done, this reviewer verifies CR-001 dispositioned (F-02) and a gate exit 0 with run 3 and the lock sanity rows recorded (F-01).

## Completion criteria check (SWE-088)

Iteration 3: still not met (F-01 and F-02 Major open on owner rulings; F-04 a lien; gate exits 1). Iteration 2: still not met (two Major findings open, F-04 open, gate not passing). Iteration 1 text follows. Not met: readiness R3 is not met (inherent to FW-B0), two Major findings are open, and the gate does not pass. `tools/validate_docs.py` passes on this record. No unsafe entry exists to sign.

## Verdict

```
ITERATION 3 (2026-09-26, HEAD adcfe09): VERDICT: NEEDS CHANGES
- [Major] F-01 Open (owner rulings: decisions 109, 110; OA-1): gate exits 1 (FAIL G5 cargo deny, FAIL G5 unsafe audit, 5 MISSING).
- [Major] F-02 Open (owner ruling: decision 108): CR-001 Submitted, not dispositioned.
- [Minor] F-04 Lien: fix before PDR (tests written by the code author).
- F-03, F-05 to F-12 Closed.
MEASUREMENTS (iteration 3): turns=22; minutes=30; new major=0; new minor=0; liens=1

ITERATION 1: VERDICT: NEEDS CHANGES
FINDINGS:
- [Major] K5 tools/sw_gate.sh: gate exits 1 (FAIL G4, FAIL G5 cargo deny, 9 MISSING); FW-B0 exit criterion of 07 section 3.2 not met.
- [Major] CK-CODE-D9 firmware/cwht-app/src/main.rs:36: second decision in target-only code (CS-11, CS-38) without CR or deviation.
- [Minor] CK-CODE-C7 main.rs:56: panic handler lacks CS-12 content; deferral not recorded.
- [Minor] CK-CODE-H2 tests written by the code author.
- [Minor] CK-CODE-C4 gpio.rs:77, 83: no comment on the arithmetic choice (CS-14).
- [Minor] K6 sw_gate.sh:176: G3 may compare stale JUnit files.
- [Minor] K6 sw_gate.sh:21: --keep-going description omits the G2 stops.
- [Minor] K7 report: G0 and --quick scope deviation from 07 section 8.4 not recorded.
- [Minor] K7 report section 5: UF2 rebuild claim lacks its artifact.
- [Minor] K7 report: on-board LED instead of the cwht pin map not recorded as a deviation.
- [Minor] K7 report: coverage cited before the cargo-llvm-cov TV the lock row requires.
- [Minor] K6 .cargo/config.toml:9: persistent linker_messages warning in every target build.
ITEMS N/A: CK-CODE-B2 to B8 (no unsafe), C3, D5, D8, E1, E3 to E8, F2, G1, G2, G4, H3, J3; R4, R6
MEASUREMENTS: size=678 lines firmware + 300 gate + 117 case + 170 report; turns=36; minutes=50; major=2; minor=10; unsafe_sites=0
```
