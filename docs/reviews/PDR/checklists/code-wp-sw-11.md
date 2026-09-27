---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md section 13;
# docs/process/07-software-engineering-plan.md section 10.2). Checklist: docs/templates/peer-review-checklist-code.md
# revision B, as PDR work plan WP-PDR-41 "Reviewer" and "Records" name. Product: rustos work package WP-SW-11
# (clocks, PLL_SYS, TICKS) on rustos branch cwht/wp-sw-11 at 213c536, with its base cwht/l-016-6 at 5b39e8e
# (SRR lien L-016-6, the host-compilable pico2), its design record ADR-051 and sprint record SW-01 (cwht main
# 618e441), frozen before this review (rule C2). The blobs are on unmerged rustos branches, so the record verdict
# is held until the owner's merge and the pin-move CR (PCR-4) bring them into a configuration cwht consumes
# (lead SE convention of 2026-09-27, INSP-031 practice).
id: INSP-095
checklist: peer-review-checklist-code
checklist_revision: B
checklist_file: docs/reviews/PDR/checklists/code-wp-sw-11.md
product: "rustos cwht/wp-sw-11: firmware/pico2/src/clocks/ and firmware/pico2/src/common/reg.rs (WP-SW-11), with cwht/l-016-6 firmware/pico2/src/lib.rs"
# product_commit (iteration 2): the rustos branch head of cwht/wp-sw-11, 4a8e825, the finding-1 fix on top of
# 213c536 (iteration 1). The blobs below equal git rev-parse 4a8e825:<path> (rustos) and git rev-parse
# e3ce2cb:<path>, HEAD:<path> and git hash-object at HEAD 5c16930 (cwht); product_files_iteration_1 keeps the
# 213c536 blobs
product_commit: "4a8e8258ec3640afe15b7588db1e967679bc1d23"
product_files: ["docs/decisions/adr/ADR-051-wp-sw-11-clocks.md@7085cf5ad97de39c8ce35b02cb56df506a68b62f", "docs/sprints/SW-01-wp-sw-11-clocks.md@2384efff9c888c88a32717ed5a3b3573e56660d3", "docs/sprints/index.md@7ae0cbcc6087d45ab4df10cac623d453ca13c395", "rustos:firmware/pico2/src/clocks/clocks.rs@631080987c36a8696b5884aa6dd7a66bf5f3cd4c", "rustos:firmware/pico2/src/clocks/clocks_tests.rs@bf61fcbf2bc6fa3f9586eadbf47278509bc4e5b6", "rustos:firmware/pico2/src/clocks/mod.rs@6aad5a88af7891dc0b48f7734ab164085249114c", "rustos:firmware/pico2/src/clocks/regs.rs@7b2ea2056760edd8d1b06d2cefb0a034e2521f53", "rustos:firmware/pico2/src/clocks/tests.rs@158d75d86168535e2a9d008de077e029baae4b33", "rustos:firmware/pico2/src/common/reg.rs@0f4e3338249d1445ec47a569712f5147549f764b", "rustos:firmware/pico2/src/common/reg/fake.rs@8a61de1ec452aa44d6f42018ca1b46eb83f77575", "rustos:firmware/pico2/src/common/board.rs@06e278af61c3bcaae1d1f67a6e952e70d6bca7c6", "rustos:firmware/pico2/src/lib.rs@0a04c25c374e0fab3a36e4819004767ed305cfd2"]
product_files_iteration_1: ["docs/decisions/adr/ADR-051-wp-sw-11-clocks.md@7f6320cd282cd911cb398c74c986d234fef89795", "docs/sprints/SW-01-wp-sw-11-clocks.md@486f35a1ff2e1b769989eb5cd966c95994041a46", "docs/sprints/index.md@fb217bcb6ff684b8117f104970a4e091a4899b1c", "rustos:l-016-6:firmware/pico2/src/lib.rs@a3b431838acf3d14935b38d19f46706233438fbd", "rustos:firmware/pico2/src/clocks/clocks.rs@685f6ba2c7e667ba902c19bcbbd729a1d2dd26e2", "rustos:firmware/pico2/src/clocks/clocks_tests.rs@9131b879685d517e6d36223f235b289d5babacd3", "rustos:firmware/pico2/src/clocks/mod.rs@b4cd2ebb4cd67b7fde83a2192ef6ae983420a6f6", "rustos:firmware/pico2/src/clocks/regs.rs@959db5cb599505f42b45996a0306ae061ef32279", "rustos:firmware/pico2/src/clocks/tests.rs@158d75d86168535e2a9d008de077e029baae4b33", "rustos:firmware/pico2/src/common/board.rs@06e278af61c3bcaae1d1f67a6e952e70d6bca7c6", "rustos:firmware/pico2/src/common/reg.rs@0f4e3338249d1445ec47a569712f5147549f764b", "rustos:firmware/pico2/src/common/reg/fake.rs@8a61de1ec452aa44d6f42018ca1b46eb83f77575", "rustos:firmware/pico2/src/lib.rs@0a04c25c374e0fab3a36e4819004767ed305cfd2"]
product_size: 1981 lines changed (5b39e8e 29 added; 213c536 1952 added, 1 removed), of which 1013 non-test lines (clocks/mod.rs 321, regs.rs 219, clocks.rs 467 with its test module split out, reg.rs 195 changed); ADR-051 94 lines; SW-01 62 lines
sprint: SW-01-wp-sw-11-clocks
author_agent: "author:WP-PDR-41 wave 1a (Claude, firmware developer role)"
reviewer_agent: "reviewer:WP-PDR-41-code (independent code reviewer, iterations 1 and 2; authored no part of WP-PDR-41)"
# criticality: 07 section 14.1 names clocks and PLL a safety-critical driver (drivers row; ADR-051 decision class 1)
criticality: safety-critical
assurance_required: true
assurance_reviewer_agent: "sa-reviewer:WP-PDR-41-code-wp-sw-11, record INSP-106 docs/reviews/PDR/checklists/code-wp-sw-11-software-assurance.md (07 section 2.1.1 Code row; iteration 2 delta pending)"
paired_record: INSP-106
iteration: 2
# readiness_met: false: R3 (ADR-051 Proposed, not Active), R5 (no independent test-author file yet) and R1 at crate
# level (pre-existing rustos fmt and clippy debt) do not hold; section "Readiness" below; unchanged at iteration 2
readiness_met: false
# reviewer_verdict: APPROVED at iteration 2 (finding-1 Verified at 4a8e825; findings 2 to 7 Minor, carried Open); open Minor findings become liens under rule C1,
# owner the firmware developer, due at the CDR readiness declaration
reviewer_verdict: APPROVED
# assurance_verdict: INSP-106 (the paired software assurance record) was NEEDS CHANGES at iteration 1; its iteration 2 delta on
# the fix commit is a separate invocation and has not run, so this record carries pending
assurance_verdict: pending
# verdict: held at NEEDS CHANGES. The reviewer verdict is APPROVED at iteration 2, but the software assurance delta
# of the paired record is not yet filed, readiness R3 and R5 do not hold, and the reviewed blobs exist only on unmerged
# rustos branches (lead SE convention of 2026-09-27). The software lead sets verdict when the owner's merge and the PCR-4
# pin-move CR bring the blobs into a configuration cwht consumes, or in the commit right after it
verdict: NEEDS CHANGES
findings_major: 1
findings_minor: 6
findings_open: 6
findings_fixed: 0
findings_verified: 1
findings_deferred: 0
assurance_findings_major: 0
assurance_findings_minor: 0
assurance_tasks_applied: []
# unsafe_sites_reviewed: the two Mmio blocks of common/reg.rs (the only new unsafe of WP-SW-11) plus the 9 existing
# lib.rs sites that L-016-6 gates on target_os = "none" (text unchanged, checked for the gating only)
unsafe_sites_reviewed: 11
deferred_rids: []
items_no: [CK-CODE-B7, CK-CODE-C4, CK-CODE-D4, CK-CODE-D7, CK-CODE-E9, CK-CODE-H2, CK-CODE-I1, CK-CODE-I3]
effort_turns: 65
effort_minutes: 130
record_status: Open
date: 2026-09-27
date_closed: null
---

# Peer review record INSP-095: WP-SW-11 clock bring-up (rustos `pico2`), code review, iteration 1

**Product:** rustos branch `cwht/wp-sw-11` at `213c536` (parent `cwht/l-016-6` at `5b39e8e`, parent `master` `2ec64c0`), the blobs of `product_files` (each checked with `git rev-parse <commit>:<path>`: all equal to the brief), with ADR-051 and SW-01 at cwht `618e441`. Read with `git show` and in a detached scratch worktree of the rustos repository (`git worktree add --detach`, removed after the review); the owner's rustos working tree was not read. **Checklist:** `docs/templates/peer-review-checklist-code.md` revision B. **Independence (rule C4):** this invocation authored no part of WP-PDR-41 and edited no product file. **Search first:** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: peer-review record front matter; A3 stepping `CLK_SYS_CTRL` reset values); `grep -n` was used only afterwards to pin lines. The index had no entry for the new ADR-051 to ADR-055 and SW-01 to SW-05 files; they were read by path.

**Acceptance criteria (rule C7, every case the governing clause enumerates):** readiness R1 to R6; every item CK-CODE-A1 to CK-CODE-J4; the target platform rules CS-34 to CS-37 and CS-38 (07 section 7.7) for this package; each bring-up step of ADR-051 section 2 and of the `clocks.rs` step table (steps 1 to 10) against the RP2350 datasheet (rustos `docs/extracted/rp2350-datasheet.md` at `2ec64c0`); each of the 15 `ClockFault` variants and 10 `ClockConfigError` variants; the 07 section 19 closing rule items (contract test, mock, dev-board report, ACC-EMU-001, unsafe signatures, api docs); the three questions ADR-051 puts to the reviewer (section 5 CS-08 reading; section 7 trade-study class; the OD-16 capability pilot as a revisit condition).

## Commands run by the reviewer (evidence)

| # | Command (read-only for both repositories; outputs in the scratchpad) | Result |
|---|---|---|
| C1 | `cargo +1.98.0 test --offline -p pico2 --lib` and `-p api` at each of `5b39e8e`, `213c536` (and the later stack commits) | `5b39e8e`: pico2 builds and links on the host (0 tests); `213c536`: 34 passed, 0 failed |
| C2 | `cargo +1.98.0 build --offline -p pico2 --target thumbv8m.main-none-eabihf`, dev and `--release`, at each commit | no warning, no error |
| C3 | `cargo +nightly-2026-08-24 miri test --offline -p pico2 --lib` at the stack head `6df18af` (contains every WP-SW-11 test) | 95 passed, no undefined behaviour |
| C4 | `cargo clippy -p pico2 -p api --all-targets -- -D warnings`, host and target, at `2ec64c0`, `5b39e8e`, `213c536` | fails at every commit on pre-existing rustos items (`gpio.rs` `needless_return`, `lib.rs` `ptr_as_ptr` and `empty_loop`, `gpio/mod.rs` `module_inception`); `213c536` adds `module_inception` at `clocks/mod.rs:39`; `2ec64c0` also fails the host build on the Mach-O section names, which `5b39e8e` removes |
| C5 | `cargo clippy ... -- -W clippy::pedantic` with `--message-format=short`, filtered to the WP-SW-11 files | only `module_inception` (`clocks/mod.rs:39`) |
| C6 | `cargo fmt --check` at `2ec64c0` and at the stack head | differences only in pre-existing files; none in `clocks/`, `common/reg.rs` or `common/reg/fake.rs` |
| C7 | `rust-code-analysis-cli --metrics --output-format json --paths <wt>/api --paths <wt>/firmware/pico2 \| .venv/bin/python tools/complexity_gate.py --max 15 --yellow 12` at the stack head | PASS; `check_pll` CC 10 (analyzer 9 + 1 `let ... else`), the package maximum; 4 name-based CS-19 reports, all method-name collisions, not cycles |
| C8 | `.venv/bin/python tools/unsafe_audit.py --write` then `--check` with `--audited` the worktree `api` and `firmware/pico2`, `--audit-file` in the scratchpad | PASS; 46 sites at the stack head, 0 without SAFETY; the two WP-SW-11 sites are `common/reg.rs` `read` and `write` |
| C9 | Datasheet check: rustos `docs/extracted/rp2350-datasheet.md` at `2ec64c0` (`git show`), sections 8.1.2.2 (lines 37735 to 37790 of the extract), Table 558 (`CLK_SYS_CTRL`, line 39214), Table 555, Tables 581 to 583 (`FC0_*`), Tables 623, 624, 629 (`TICKS`) | offsets, field positions and enumerated values of `regs.rs` all agree; the sequence of step 3 does not (finding-1) |

## Readiness criteria

| # | Holds | Evidence |
|---|---|---|
| R1 | No (crate level) | C4 to C6: the `pico2` crate fails `-D warnings` and `fmt --check` on pre-existing items; WP-SW-11 adds `module_inception` (finding-6); the new files are fmt-clean |
| R2 | No (one file) | `wc -l` at `213c536`: `clocks.rs` 467, `clocks_tests.rs` 339, `mod.rs` 321, `regs.rs` 219, `tests.rs` 209, `reg.rs` 290, `fake.rs` 192; the longest function (`start_pll_sys`) is 33 lines; but `lib.rs` is 550 lines at `2ec64c0`, 579 at `5b39e8e` and 588 at `213c536` (finding-7) |
| R3 | No | ADR-051 Status "Proposed" (ADR-051 line 6); the design unit is not Active |
| R4 | N/A | CS-24 tags apply to cwht code only (plan WP-PDR-41 "SWE-052 row 4 preparation") |
| R5 | No | SW-01 phase 2 open: `firmware/devcheck/src/bin/clocks_check.rs` not written (SW-01 lines 45 to 49) |
| R6 | Yes | C8 |

The reviewer was dispatched by the lead SE with R3 and R5 open; the answers below take that as given.

## Checklist answers

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-A1 | Yes | `lib.rs` `#![no_std]`; `extern crate std` only in test-only modules (`reg.rs:221` `#[cfg(test)] pub(crate) mod fake;`, `clocks_tests.rs:4`) |
| CK-CODE-A2 | Yes | no `Cargo.toml` in `git diff --stat 2ec64c0 213c536` |
| CK-CODE-A3 | Yes | `#[cfg(target_os = "none")]` gates target-only items (`Mmio`, `init`); L-016-6 gates the runtime items only and leaves the target build unchanged (C2); no `debug_assert!` |
| CK-CODE-B1 | N/A | `pico2` is a crate permitted `unsafe` (CS-05) |
| CK-CODE-B2 | Yes | `reg.rs:174-179` and `:184-188` (at `213c536`): the argument (APB base of Table 7 plus an offset masked to the block's 16 KiB window of section 2.1.3, volatile raw-pointer access, no reference formed) is valid for the six `RegAddr` blocks this package uses. The later `RegAddr::NVIC` variant invalidates part of it (INSP-096 finding-1) |
| CK-CODE-B3 | N/A | no `unsafe fn` added; each block is one expression |
| CK-CODE-B4 | Yes | offsets from `#[repr(C)]` layouts through `offset_of!` with compile-time asserts (`regs.rs:26`, `:53-54`, `:131-148`, `:209-214`); the only integer-to-pointer arithmetic is `Mmio::address` (`reg.rs:165-167`); `RESETS` touched through the set and clear aliases (`clocks.rs:282-283`). Ruling on ADR-051 section 5: this meets CS-08's purpose (every offset checked against its table, one address-forming site in `pico2::common::reg`); no finding and no CR needed. A wording refresh of CS-08 at the next 07 revision is optional |
| CK-CODE-B5 | Yes | no `static mut` in the package |
| CK-CODE-B6 | Yes | none of `transmute`, `zeroed`, `union`, `asm!` in the package files |
| CK-CODE-B7 | No | `firmware/unsafe-audit.md` is regenerated and signed on the pin-move CR branch (SW-01 line 38); no committed entry exists to sign. Not a finding: the obligation is carried to PCR-4 and CS-07 (before CDR) |
| CK-CODE-B8 | Yes | `Rp2350Clocks::init(_handle: DeviceHandle<Self>, ...)` (`clocks.rs:165-170`); device `clocks` in `board.rs` |
| CK-CODE-C1 | Yes | no `unwrap`, `expect`, `panic!`, indexing or slicing outside test code (scan of the non-test lines) |
| CK-CODE-C2 | Yes | `ClockConfigError`, `ClockFault`, `PollTimeout`; every `Result` propagated with `?` or `map_err` |
| CK-CODE-C3 | Yes | each wait maps its timeout to the `ClockFault` of its step (`clocks.rs:228-305`, `:330-406`, `:441-462`); the response (halt in the safe state) is the `cwht-app` construction arm of CS-11 (ADR-051 section 4.2) |
| CK-CODE-C4 | No | finding-4 |
| CK-CODE-C5 | Yes | no numeric `as`; `u32::try_from` for the VCO (`mod.rs:241`); `block as usize` is the enum discriminant in the CS-08 location (`reg.rs:166`) |
| CK-CODE-C6 | Yes | no `f32` or `f64` |
| CK-CODE-C7 | N/A | no panic handler in the package |
| CK-CODE-D1 | Yes | C7: package maximum CC 10 |
| CK-CODE-D2 | Yes | the only loop is `poll` (`reg.rs:212`, bounded by `budget`); no recursion |
| CK-CODE-D3 | N/A | not `cwht-core`; the `match` on `Measurement` is exhaustive (`clocks.rs:448-462`) |
| CK-CODE-D4 | No | finding-5 |
| CK-CODE-D5 | N/A | no interrupt handler |
| CK-CODE-D6 | Yes | nothing starts core 1 |
| CK-CODE-D7 | No | functions and nesting within CS-18 (R2); `lib.rs` above 500 lines (finding-7) |
| CK-CODE-D8 | No | CS-37: TICKS started before any TIMER0 or watchdog use and every wait loop-bounded, but finding-1 opens a path in which `clk_sys` can stop before the bounded wait can run, so the fault return of CS-37 is not guaranteed |
| CK-CODE-D9 | Yes | `init` is one call; every decision is in `bring_up`, `plan`, `judge`, host-tested (CS-38) |
| CK-CODE-E1 | Yes | public shape as ADR-051 section 2 (`init(handle, &ClockConfig) -> Result<ClocksReady, ClockFault>`); ADR-051 records the change from the 07 section 19 row's `Result<(), ClockFault>` to the `ClocksReady` proof |
| CK-CODE-E2 | Yes | units in identifiers (`xosc_hz`, `tolerance_permille`, `poll_budget`, `fc_min_khz`); every constant cites its table |
| CK-CODE-E3 | N/A | no keyer logic |
| CK-CODE-E4 | No | finding-1 (step 3 and step 8 against section 8.1.2.2). All field positions and values agree with the extract (C9), including `FC0_SRC` `0x09` `CLK_SYS` and `0x0a` `CLK_PERI` (Table 583) and `XOSC.STARTUP.DELAY` 47 |
| CK-CODE-E5 | Yes | `plan` runs before any register write (`clocks.rs:191`), and a fault stops the sequence |
| CK-CODE-E6 | Yes | `STABLE`, `SELECTED`, `RESET_DONE`, `LOCK`, `ENABLED`, `RUNNING` read back; `judge` requires both the hardware `PASS` flag and the window (`mod.rs:310-318`); the scope of that check is overstated in ADR-051 (finding-2) |
| CK-CODE-E7 | N/A | the driver writes no application output |
| CK-CODE-E8 | N/A | no integrity data |
| CK-CODE-E9 | No | finding-5 (`ALIAS_XOR` kept alive with `allow(dead_code)`) |
| CK-CODE-F1 to F3 | N/A | rustos code: CS-24 does not apply (plan WP-PDR-41); the commit message cites ADR-051 |
| CK-CODE-G1 | Yes | the only external input, `ClockConfig`, is range-checked by `plan` before use |
| CK-CODE-G2 to G4 | N/A | no key input, buffer or diagnostic handler |
| CK-CODE-G5 | Partial | C3, C7, C8 run by the reviewer; `cargo audit`, `cargo deny` and `cargo geiger` not run (no dependency change, and `cargo deny` fetches an advisory database: no download permission); the formal G5 run is on the PCR-4 branch |
| CK-CODE-H1 | Yes | `bring_up` is generic over `Regs`; no real-time or hardware dependency on the host |
| CK-CODE-H2 | No | no independent test-author file yet (R5) |
| CK-CODE-H3 | Yes | MC/DC pairs for `judge` (`tests.rs:167` onward) and every `plan` limit at both edges in the author's developer tests; the `// @mcdc` tag is a cwht convention (SW-01 line 43) |
| CK-CODE-I1 | No | new `pub` items are documented (a `-W missing_docs` target build reports only pre-existing `api/src/lib.rs:92` and `board.rs:86`), but neither crate carries `#![deny(missing_docs)]` (CS-25). Pre-existing; not a finding of this package |
| CK-CODE-I2 | Yes | register and field names as the datasheet |
| CK-CODE-I3 | No | finding-6 |
| CK-CODE-I4 | Yes | comments explain why; no commented-out code |
| CK-CODE-J1 | Yes | C1, C2 build on both targets |
| CK-CODE-J2 | Yes | `Regs::read`/`write`, `poll` called as defined |
| CK-CODE-J3 | Yes | CS-37 "TICKS enabled and waits bounded" implemented as one sequence, apart from finding-1 |
| CK-CODE-J4 | Yes | measured with `wc -l` and the analyzer |

**07 section 19 closing rule (WP-SW-11 row):** contract test and mock: not applicable (no `api` trait; ADR-051 section 4.3); dev-board report `docs/vv/reports/devcheck-clocks-r1.md`: not yet; ACC-EMU-001: clock blocks outside the candidate scope (ADR-051 section 4.3); unsafe signatures: open (B7); api docs: not applicable. The row is not closable at this commit; SW-01 records all of these as open.

**ADR-051 section 7 question (does 06 section 14.1 item (c) require a separate trade study for a work-package design under TS-002?):** a design-checklist question outside the code checklist. It belongs to the ADR design review with its software assurance pair (07 section 2.1.1 row 3), which SW-01 phase 3 names (`adr-051-wp-sw-11-clocks.md`) but plan WP-PDR-41 "Records" does not. Reported to the lead SE; not answered here.

## Findings

| Finding | Origin | Severity | Item | Location | Description | State | Deferred to |
|---|---|---|---|---|---|---|---|
| finding-1 | reviewer | Major | CK-CODE-E4, CK-CODE-D8 | `clocks.rs:246-250`, `:349`; `clocks_tests.rs:18-90` | aux mux changed while selected (section 8.1.2.2) | Open | |
| finding-2 | reviewer | Minor | CK-CODE-E6 | ADR-051 line 27; `clocks.rs:32-35` | frequency-counter check cannot confirm the crystal frequency | Open | |
| finding-3 | reviewer | Minor | CK-CODE-E2 | `mod.rs:96-102`; ADR-051 lines 28, 94 | poll-budget margin of the step 10 waits below the ADR's own 10x revisit condition | Open | |
| finding-4 | reviewer | Minor | CK-CODE-C4 | `mod.rs:195-210`, `:250`; `reg.rs:213` | plain arithmetic without the CS-14 justification | Open | |
| finding-5 | reviewer | Minor | CK-CODE-D4, CK-CODE-E9 | `reg.rs:108-109` | `allow(dead_code)` without a CS-21 waiver, on an unused constant | Open | |
| finding-6 | reviewer | Minor | CK-CODE-I3 | `clocks/mod.rs:39`; SW-01 line 32 | `module_inception` fails `-D warnings`; the sprint record calls it clean | Open | |
| finding-7 | reviewer | Minor | CK-CODE-D7 | `lib.rs` (550, 579, 588 lines) | CS-18 file length exceeded and grown; not recorded in SW-01 | Open | |

### finding-1

**Major, CK-CODE-E4 and CK-CODE-D8 (CS-37).** Step 3 writes `CLK_SYS_CTRL = AUXSRC_PLL_SYS | SRC_REF` (`0x0`) as one word (`clocks.rs:246-250`). `CLK_SYS_CTRL` resets to `AUXSRC = 0x2` (`ROSC_CLKSRC`) and `SRC = 0x1` (`CLKSRC_CLK_SYS_AUX`) (Table 558, extract lines 39226 and 39255), so on a cold boot `clk_sys` runs from the ROSC through the aux mux, and this write changes the aux mux select from the ROSC to `PLL_SYS` (not yet running) in the same cycle as it asks the glitchless mux to leave aux. Section 8.1.2.2 requires the glitchless mux to be switched away from aux and `SELECTED` polled **before** the aux select changes ("Failure to do at least one of the above may cause a glitch on the clock input of all hardware currently clocked by this clock generator"; the recommended sequence, steps 1 to 3). The aux mux "will glitch when switching" (Table 558 `AUXSRC`), and with its new source stopped the glitchless mux may have no edges to complete the switch: `clk_sys` can glitch or stop, the processor with it, and no bounded wait runs, so the CS-37 fault return is not reached. The same ordering defect, lower in consequence, is at step 8: `clocks.rs:349` writes `CLK_PERI_CTRL = AUXSRC_CLK_SYS` with `ENABLE = 0` in one word, where section 8.1.2.2 (generator without a glitchless mux: disable, wait for the stop, then change the aux select) requires the aux change after the stop. The host tests cannot see either: `FakeRegs` starts every register at 0 (`fake.rs` `get` returns 0) and `healthy()` presets no control register, so the golden sequence (`clocks_tests.rs:49-90`) encodes the defect. **Fix:** step 3 clears only `SRC` (a write to `CLK_SYS_CTRL + ALIAS_CLR` of bit 0, or a read-modify-write keeping `AUXSRC`), polls `SELECTED` for `clk_ref`, and only step 7 writes `AUXSRC`; step 8 clears `ENABLE` alone (clear alias), waits for `ENABLED` to clear, then writes `AUXSRC`, `DIV` and `ENABLE`; the test register file presets the datasheet reset values of `CLK_SYS_CTRL` (`0x41`), `CLK_REF_CTRL` and `CLK_PERI_CTRL`, and a test asserts that no write changes an `AUXSRC` field while `SELECTED` (or `ENABLED`) shows the aux path in use. ADR-051 section 2 ("Every control field is written explicitly") is reworded to match.

### finding-2

**Minor, CK-CODE-E6.** ADR-051 assumption 1 (line 27) says the dev-board check confirms the 12 MHz crystal because "the frequency counter reads `clk_sys` 150 MHz ±1 % only if the reference is 12 MHz". The frequency counter times its window from `clk_ref`, which step 4 makes the crystal, and converts with `FC0_REF_KHZ` = 12 000 (`clocks.rs:418`): it measures the ratio `clk_sys / clk_ref` times 12 000 kHz. A 10 MHz crystal gives `clk_sys` 125 MHz and still reads 150 000 kHz. Step 10 therefore catches divider and PLL errors, not a wrong crystal. The crystal is confirmed only by the 60 s TIMER0 stopwatch check of ADR-051 section 4.3. **Fix:** name the stopwatch check (or a measurement against an independent reference) as the confirmation of assumption 1, and say in the `clocks.rs` module doc (lines 32 to 35) that step 10 checks the tree against the crystal, not the crystal itself.

### finding-3

**Minor, CK-CODE-E2.** The budget argument (`mod.rs:96-102`) covers the crystal start-up while the core runs from the ROSC. The step 10 waits run at `clk_sys` 150 MHz and each lasts about 1 ms (`FC0_INTERVAL` 10, 1.0 ms per Table 582 plus the settle delay); 100 000 polls of at least three cycles each last at least 2 ms, a designed lower-bound margin of about 2x (about 5x at a more realistic seven cycles per poll). ADR-051 section 7 makes "less than 10 times margin on any wait" a revisit condition, so the design as analysed already meets that condition on two waits. **Fix:** give the measurement waits their own budget sized for 10x at 150 MHz, or restate the revisit condition with the per-wait margins, and report both in `ClockReport::polls` on the dev board.

### finding-4

**Minor, CK-CODE-C4 (CS-14).** Plain `*`, `+` and `-` in `plan` (`mod.rs:195-210`: `clk_sys / 1000`, `clk_sys_khz * config.tolerance_permille`, `clk_sys_khz - margin_khz`, `clk_sys_khz + margin_khz`, `pll.postdiv1 << 16`), `check_pll` (`mod.rs:250`, `pll.postdiv1 * pll.postdiv2`) and `poll` (`reg.rs:213`, `reads += 1`) carry no bound argument, except the VCO product (`mod.rs:239-241`). Each is bounded by an earlier check, but under the cwht profile (`overflow-checks = true`, CS-04) a bound that a later change breaks becomes a panic path in a safety-critical driver. **Fix:** a one-line bound comment at each site, or `checked_`/`saturating_` forms.

### finding-5

**Minor, CK-CODE-D4 and CK-CODE-E9 (CS-21).** `#[cfg_attr(not(test), allow(dead_code))]` on `ALIAS_XOR` (`reg.rs:108-109`) has no `// CS-NN waiver: <reason> (INSP-NNN)` comment, and it keeps an item alive that no driver uses ("unused items are removed, not `#[allow(dead_code)]`"). **Fix:** remove `ALIAS_XOR` until a driver writes it (the test register file can keep its own constant), or add the waiver comment citing this record.

### finding-6

**Minor, CK-CODE-I3 (readiness R1).** `clippy -D warnings` fails on `module_inception` at `clocks/mod.rs:39` (a default style lint, not only pedantic), host and target. SW-01 line 32 reports the new code clippy-clean "apart from the rustos house-style `module_inception`", which is accurate for pedantic but hides that G1's `-D warnings` fails on it. **Fix:** a CS-21 waiver comment on the `pub mod clocks;` line citing the rustos house style, or a rename; the sprint record states the G1 result as measured.

### finding-7

**Minor, CK-CODE-D7 (CS-18).** `firmware/pico2/src/lib.rs` is 550 lines at `2ec64c0`, above the 500-line limit before cwht touched it; L-016-6 adds 29 lines (the `#[cfg(target_os = "none")]` attributes and the "Host builds" doc) and WP-SW-11 adds 9 (module list). This growth is small and cannot be moved elsewhere (each attribute sits on its item), so it is Minor here; the WP-SW-09 addition to the same file is avoidable and is Major in INSP-096. SW-01 reports the CS-18 state of `gpio/gpio.rs` but not of `lib.rs`. **Fix:** record the `lib.rs` length in SW-01 and carry the split of `lib.rs` (runtime, vector table, boot metadata) as a rustos item for the owner, with the INSP-096 finding-1 fix.

## Measurements (SWE-089)

Lines reviewed: 1013 non-test lines of `213c536` and the 29-line L-016-6 change, plus the 548 lines of author developer tests skimmed for the golden sequence and fault coverage; ADR-051 and SW-01 in full. Unsafe sites reviewed: 2 new (`reg.rs`) and 9 gated by L-016-6. Findings: 1 Major, 6 Minor. Effort: 40 turns, 90 minutes.

## Record verdict

`reviewer_verdict: NEEDS CHANGES` on finding-1. Iteration 2 is a delta (rule C1) that verifies the finding-1 fix on a new frozen commit and re-runs C1 to C3 and C7. Minor findings 2 to 7 may be fixed in the same commit or, after an APPROVED verdict, become liens under rule C1. `verdict` stays `NEEDS CHANGES` until the software assurance record (`code-wp-sw-11-software-assurance.md`) is filed APPROVED and the reviewed blobs reach a configuration cwht consumes (owner merge, PCR-4).

## Iteration 2: delta verification of finding-1 (Major) (2026-09-27, cwht HEAD `5c16930`)

**Scope (rule C1).** Iteration 2 is a delta that verifies the finding-1 fix only. Findings 2 to 7 (Minor) were not touched by the author (ADR-051 section 8, SW-01 "Phase 1, revision 2") and are not re-reviewed. Product: rustos `cwht/wp-sw-11` at `4a8e825` (revision 1 `213c536` is its parent; `git diff --stat 213c536 4a8e825`: `clocks.rs` 51, `clocks_tests.rs` 168, `mod.rs` 6, `regs.rs` 3 lines changed), with ADR-051, SW-01 and the sprint index at cwht `e3ce2cb`, the blobs of front matter `product_files`. The checklist is `peer-review-checklist-code.md` revision B, as at iteration 1.

**Independence (rule C4).** This invocation authored no part of WP-PDR-41, of revision 2 or of the rustos fix commits, and edited no product file. The rustos repository was read with `git show` and in a detached scratch worktree created with `git worktree add --detach` in the scratchpad and removed after the review; the owner's rustos working tree was not read. A throw-away link application (D10 of INSP-096) was built in the scratchpad, outside both repositories.

**Search first (charter section 11 rule 1).** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran (queries: iteration 2 delta record practice for the `code-wp-sw` records; REQ-SW-KEYER-033 sidetone gate) before any search of product or requirement content. One `grep -n` on the known plan file `docs/plan/pdr-work-plan.md`, to locate the WP-PDR-41 section, ran before the first `search_code` query; that is out of the rule's order and is reported here. Afterwards `grep` only pinned lines in known paths (the plan, the 07 `SW-AUDIO` rows, the validator, the rustos datasheet extract through `git show`). The index returned the new ADR-055 section 2.1 text, so it holds the revision 2 files.

### Commands run by the reviewer (evidence)

| # | Command (read-only for both repositories; outputs in the scratchpad) | Result |
|---|---|---|
| D1 | `git rev-parse <commit>:<path>` for each of the 55 rustos blobs of the brief at its named commit; `git rev-parse e3ce2cb:<path>`, `git rev-parse HEAD:<path>` (HEAD `5c16930`) and `git hash-object <path>` for the 11 cwht blobs | all 66 equal to the brief; `git log e3ce2cb..HEAD` touches none of the cwht product files |
| D2 | `cargo +1.98.0 test --offline -p pico2 --lib` and `-p api` in a detached scratch worktree of the rustos repository at `4a8e825`, `c6e5100`, `58fe739`, `38434b2`, `48e07ec` | pico2 37, 49, 75, 81, 101 passed; api 0, 4, 9, 14, 19 passed; 0 failed at every commit |
| D3 | `cargo +1.98.0 build --offline -p pico2 --target thumbv8m.main-none-eabihf`, dev and `--release`, at the same five commits | no warning, no error |
| D4 | `cargo +nightly-2026-08-24 miri test --offline -p pico2 --lib` at the stack head `48e07ec` | 101 passed, no undefined behaviour |
| D5 | `rust-code-analysis-cli --metrics --output-format json --paths <wt>/api --paths <wt>/firmware/pico2 \| .venv/bin/python tools/complexity_gate.py --max 15 --yellow 12` at `48e07ec` | PASS; 399 functions; the only function above 12 is the contract check `api/tests/irq_contract.rs:48` `check_out_of_range` (CC 13, test code, as INSP-096 C5); 4 name-based CS-19 reports, method-name collisions |
| D6 | `.venv/bin/python tools/unsafe_audit.py --write` then `--check`, `--audited` the worktree `api` and `firmware/pico2`, `--audit-file` in the scratchpad, at `48e07ec` | PASS; 46 sites, 0 without SAFETY, 0 in forbidden crates, all unsigned (signatures due before CDR, CS-07) |
| D7 | `cargo +1.98.0 clippy --offline -p pico2 -p api --all-targets --message-format=short -- -W clippy::pedantic` (host) at `48e07ec`, filtered to the files the fix commits change | no lint on a line the fix commits add or change; the remaining reports are on unchanged lines or are iteration 1 Minor findings (`module_inception` at `clocks/mod.rs:41` and `timer/mod.rs:32`, INSP-095 finding-6 and INSP-097 finding-5; `timer_tests.rs:16` cast, INSP-097 finding-5) |
| D8 | `rustfmt +1.98.0 --edition 2024 --check` on the 13 new or changed Rust files other than `gpio/gpio.rs` | no difference; `gpio.rs` keeps its pre-existing non-rustfmt style (INSP-098 finding-2) |
| D9 | Mutation: the iteration 1 `clocks.rs` (blob `685f6ba`) put back over the `4a8e825` one, with one `#[cfg(test)] use super::CLK_SYS_CTRL_SRC;` line added so the new tests compile; then only the step 8 `ENABLE` clear replaced by the iteration 1 one-word write | first run: 3 of 29 `clocks` tests fail, among them `no_aux_select_changes_while_its_generator_is_on_the_aux_path` with "AUXSRC of 0x3c changed on the aux path" (step 3) and the golden sequence; second run: the same aux-rule test fails with "AUXSRC of 0x48 changed on the aux path" (step 8). Worktree restored with `git checkout` after each run |
| D10 | Datasheet: rustos `docs/extracted/rp2350-datasheet.md` at `2ec64c0` (`git show`), section 8.1.2.2, extract lines 37742 to 37792 | the three conditions before an aux change and the two recommended sequences (with and without a glitchless mux), read against steps 3, 4, 7 and 8 below |

### Verification of finding-1, case by case (rule C7)

The finding named four defects and a test gap; each is checked against section 8.1.2.2 and the code at `4a8e825`.

| Case | Required by finding-1 | At `4a8e825` | Result |
|---|---|---|---|
| Step 3, `clk_sys` leaves aux | clear only `SRC`, keep `AUXSRC`, poll `SELECTED` for `clk_ref` | `clocks.rs:251` writes `CLK_SYS_CTRL_SRC` (bit 0, `regs.rs` new constant, Table 558) to `CLK_SYS_CTRL + ALIAS_CLR`; `:252-260` poll `CLK_SYS_SELECTED` for `1 << CLK_SYS_SRC_REF` under mask `0b11`. This is steps 1 and 2 of the glitchless-mux sequence; on a cold boot `AUXSRC` stays ROSC while the mux leaves it | Verified |
| Step 7, first `AUXSRC` write | only after `SELECTED` shows `clk_ref` | `move_clk_sys_to_pll` (`clocks.rs:315-341`) writes `CLK_SYS_DIV`, then `CLK_SYS_CTRL = AUXSRC_PLL_SYS \| SRC_REF` (glitchless mux still on `clk_ref`, polled in step 3, not moved since), then `SRC_AUX`, then polls `SELECTED` for aux: steps 3 to 5 of the sequence | Verified |
| Step 8, `clk_peri` (no glitchless mux) | clear `ENABLE` alone, wait for `ENABLED` to clear, then `AUXSRC`, `DIV`, `ENABLE` | `clocks.rs:351` clears `CLK_PERI_ENABLE` through `ALIAS_CLR`; `:352-360` wait for `ENABLED` = 0; `:361` writes `CTRL = AUXSRC_CLK_SYS` (enable still clear), `:362` `DIV`, `:363` sets `ENABLE` through `ALIAS_SET`; `:364-372` wait for `ENABLED`. This is the five-step sequence without a glitchless mux, with the `ENABLED` poll the datasheet asks for ("polling the clock generator's CTRL_ENABLED status until it matches the value of CTRL_ENABLE") | Verified |
| Step 4, `clk_ref` (not named by the finding; checked because it also writes a control word with an `AUXSRC` field) | no `AUXSRC` change while `clk_ref` is on aux | `CLK_REF_CTRL = SRC_XOSC` writes `AUXSRC = 0`; `clk_ref` is never put on aux by this driver and resets to the ROSC (Table 555), and the D-series test below covers it in both start states | No defect |
| Test register file | reset values of `CLK_SYS_CTRL` (`0x41`), `CLK_REF_CTRL`, `CLK_PERI_CTRL` | `clocks_tests.rs:15-17` and `healthy()` preset them; `0x41` is `AUXSRC = 0x2` (bits 7:5) with `SRC = 1`, as Table 558 | Verified |
| Test of the rule | a test fails any `AUXSRC` change while `SELECTED` or `ENABLED` shows the aux path | `assert_aux_changes_only_off_the_aux_path` replays the access log for all three generators, models the set and clear aliases, and allows an `AUXSRC` change only after a status read made since the last change of the holding condition; `no_aux_select_changes_while_its_generator_is_on_the_aux_path` runs it from the cold state and from a restart state (`clk_sys` on `PLL_SYS` through aux, `clk_ref` on the crystal, `clk_peri` running from `PLL_SYS`), which exercises the step 8 path with a real `AUXSRC` change; two should-panic tests show it rejects the iteration 1 step 3 and step 8 writes; D9 shows it fails the iteration 1 code and a step-8-only reversion | Verified |
| ADR-051 section 2 wording | "Every control field is written explicitly" reworded | ADR-051 section 2 now says the driver relies on no reset value, leaves the aux path by clearing `SRC` alone, and changes an aux select only off the aux path, quoting section 8.1.2.2; `clocks/mod.rs` module doc says the same; section 4.3 adds a dev-board case from a watchdog restart that leaves `clk_sys` on `PLL_SYS` | Verified |
| CS-37 (CK-CODE-D8) | the fault return of CS-37 is reachable | with no aux change on the aux path, `clk_sys` cannot be glitched or stopped by the driver's own writes, and every wait remains a bounded `poll` with its `ClockFault` | Verified |

Evidence claims of ADR-051 section 4.3 and SW-01 checked: 37 host tests at `4a8e825` (D2), 101 at `48e07ec` natively and under Miri (D2, D4), clean target builds (D3), the mutation result (D9), file lengths `clocks.rs` 466, `clocks_tests.rs` 499, `mod.rs` 323, `regs.rs` 222 (`wc -l`), unsafe audit 46 sites (D6). The ADR's "max CC 12 over `api` and `pico2`" holds for flight code; the gate's maximum over the whole of `api` is 13 in test code (D5), already recorded in INSP-096; not a finding.

### Checklist items re-answered for the fix

| Id | Iteration 2 answer | Evidence |
|---|---|---|
| CK-CODE-E4 | Yes | table above; field positions and values of iteration 1 C9 unchanged (`regs.rs` gains only `CLK_SYS_CTRL_SRC`, bit 0 of Table 558) |
| CK-CODE-D8 | Yes | table above, row CS-37 |
| CK-CODE-C1, C5, D2, D4, E9 on the changed lines | Yes | no `unwrap`, indexing, `as`, loop or `allow` added in non-test code by the fix |
| CK-CODE-H1, H3 | Yes | the new tests run on the host against `FakeRegs`; the golden sequence is updated to the datasheet order |

Items that were No at iteration 1 for other reasons (B7, C4, D4, D7, E9, H2, I1, I3) keep their iteration 1 answers; they belong to Minor findings 4 to 7 or to readiness R5.

### Findings (current state at iteration 2)

| Finding | Origin | Severity | Item | Location | Description | State | Deferred to |
|---|---|---|---|---|---|---|---|
| finding-1 | reviewer | Major | CK-CODE-E4, CK-CODE-D8 | `clocks.rs:251`, `:315-341`, `:351-363`; `clocks_tests.rs` | aux mux changed while selected (section 8.1.2.2) | Verified (`4a8e825`) | |
| finding-2 | reviewer | Minor | CK-CODE-E6 | ADR-051 line 27; `clocks.rs:32-35` | frequency-counter check cannot confirm the crystal frequency | Open (lien, rule C1) | CDR readiness declaration |
| finding-3 | reviewer | Minor | CK-CODE-E2 | `mod.rs:96-102`; ADR-051 lines 28, 94 | poll-budget margin of the step 10 waits below the ADR's own 10x revisit condition | Open (lien, rule C1) | CDR readiness declaration |
| finding-4 | reviewer | Minor | CK-CODE-C4 | `mod.rs:195-210`, `:250`; `reg.rs:213` | plain arithmetic without the CS-14 justification | Open (lien, rule C1) | CDR readiness declaration |
| finding-5 | reviewer | Minor | CK-CODE-D4, CK-CODE-E9 | `reg.rs:108-109` | `allow(dead_code)` without a CS-21 waiver, on an unused constant | Open (lien, rule C1) | CDR readiness declaration |
| finding-6 | reviewer | Minor | CK-CODE-I3 | `clocks/mod.rs:41`; SW-01 line 32 | `module_inception` fails `-D warnings`; the sprint record calls it clean | Open (lien, rule C1) | CDR readiness declaration |
| finding-7 | reviewer | Minor | CK-CODE-D7 | `lib.rs` (550 at `2ec64c0`, 588 at `213c536`, 564 at `c6e5100`) | CS-18 file length exceeded; not recorded in SW-01 | Open (lien, rule C1) | CDR readiness declaration |

No new finding. The finding-7 excess is now smaller than before the packages (INSP-096 iteration 2), but `lib.rs` is still over 500 lines and SW-01 still does not record its length.

### Measurements (SWE-089), iteration 2

Lines reviewed: the 228 changed lines of `213c536..4a8e825` and the 26 changed lines of ADR-051, SW-01 and the index row; the unchanged `common/reg.rs` and `fake.rs` were read for the alias and log semantics the new test relies on. Unsafe sites: none added or changed. Findings: 0 new. Effort of this iteration: about 25 turns and 40 minutes (front matter totals include iteration 1).

### Record verdict, iteration 2

`reviewer_verdict: APPROVED`: finding-1 is Verified and no Major is open. Minor findings 2 to 7 become liens under rule C1 (owner the firmware developer, due at the CDR readiness declaration). `verdict` stays `NEEDS CHANGES` until the paired software assurance record INSP-106 files its iteration 2 delta APPROVED, readiness R3 and R5 hold, and the owner's merge with the PCR-4 pin-move CR brings `4a8e825` into a configuration cwht consumes; the software lead then sets it (lead SE convention of 2026-09-27).
