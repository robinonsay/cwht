---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md section 13;
# docs/process/07-software-engineering-plan.md section 10.2). Checklist: docs/templates/peer-review-checklist-code.md
# revision B, as PDR work plan WP-PDR-41 "Reviewer" and "Records" name. Product: rustos work package WP-SW-09
# (critical section, NVIC helpers, overridable interrupt vectors) on rustos branch cwht/wp-sw-09 at 9305f59
# (stacked on cwht/wp-sw-11 at 213c536), with its design record ADR-052 and sprint record SW-02 (cwht main
# 618e441), frozen before this review (rule C2). The blobs are on an unmerged rustos branch, so the record
# verdict is held until the owner's merge and the pin-move CR (lead SE convention of 2026-09-27).
id: INSP-096
checklist: peer-review-checklist-code
checklist_revision: B
checklist_file: docs/reviews/PDR/checklists/code-wp-sw-09.md
product: "rustos cwht/wp-sw-09: api/src/irq/mod.rs, firmware/pico2/src/irq/mod.rs, firmware/pico2/src/critical_section.rs, firmware/pico2/link.ld and the vector table of firmware/pico2/src/lib.rs (WP-SW-09)"
# product_commit (iteration 2): the rustos branch head of cwht/wp-sw-09, c6e5100, the finding-1 fix on the merge
# 8b67385 of cwht/wp-sw-11 4a8e825 into 9305f59 (iteration 1). Blobs equal git rev-parse c6e5100:<path> (rustos)
# and git rev-parse e3ce2cb:<path>, HEAD:<path> and git hash-object at HEAD 5c16930 (cwht)
product_commit: "c6e5100b237a5995c2ec9852b8f8b340fc3b506b"
product_files: ["docs/decisions/adr/ADR-052-wp-sw-09-interrupts.md@58c06b4f4c2866332065520d296a4a7494113a5c", "docs/sprints/SW-02-wp-sw-09-interrupts.md@e02db842240d91cad7ab066f2543297efb3addb9", "docs/sprints/index.md@7ae0cbcc6087d45ab4df10cac623d453ca13c395", "rustos:firmware/pico2/src/lib.rs@1f3a4c919e3ca69f3ac2ab06f49d11aa9d808383", "rustos:firmware/pico2/src/irq/mod.rs@7f395b2732727a5a68d7a97a52577044198dc870", "rustos:firmware/pico2/src/irq/vectors.rs@8034c93a4cbf3f6de11ad1767c7d8b143820f165", "rustos:firmware/pico2/src/critical_section.rs@1f7e011a2f1383b1627f814591726fd937f81320", "rustos:firmware/pico2/link.ld@f157f6fa1016b7032c89a3f05db8282d2123c336", "rustos:api/src/irq/mod.rs@260fa0a6ff3eef4bff31511a726ca0577267a248", "rustos:api/src/lib.rs@12d5d0ef9e672bcc1791f4086c9825798535d6a7", "rustos:api/tests/irq_contract.rs@9f118d179919c8801e41346f836f03a52b12bf50", "rustos:firmware/pico2/src/common/board.rs@7a88c173087b85a8e69347a70f5c6d174d48e6a6", "rustos:firmware/pico2/src/common/reg.rs@f0b8f8732b516609444594dc73b3dc7a317bc19a", "rustos:firmware/pico2/src/common/reg/fake.rs@02e31cf54132c43b9dfba6607e1bc2ed6786d22f"]
product_files_iteration_1: ["docs/decisions/adr/ADR-052-wp-sw-09-interrupts.md@f1ee2e75ae027ffe868366ffeaef417f2a7b19b3", "docs/sprints/SW-02-wp-sw-09-interrupts.md@4adccaf6954561d621236fd72c9d476f16d598dc", "docs/sprints/index.md@fb217bcb6ff684b8117f104970a4e091a4899b1c", "rustos:api/src/irq/mod.rs@260fa0a6ff3eef4bff31511a726ca0577267a248", "rustos:api/src/lib.rs@12d5d0ef9e672bcc1791f4086c9825798535d6a7", "rustos:api/tests/irq_contract.rs@9f118d179919c8801e41346f836f03a52b12bf50", "rustos:firmware/pico2/link.ld@f157f6fa1016b7032c89a3f05db8282d2123c336", "rustos:firmware/pico2/src/critical_section.rs@1f7e011a2f1383b1627f814591726fd937f81320", "rustos:firmware/pico2/src/irq/mod.rs@f1366bfc74315d2d539da8f2b61106f2b1bc3959", "rustos:firmware/pico2/src/lib.rs@6008ddba48a8af1106e4607363bdec1321f7bf54", "rustos:firmware/pico2/src/common/board.rs@7a88c173087b85a8e69347a70f5c6d174d48e6a6", "rustos:firmware/pico2/src/common/reg.rs@f0b8f8732b516609444594dc73b3dc7a317bc19a", "rustos:firmware/pico2/src/common/reg/fake.rs@02e31cf54132c43b9dfba6607e1bc2ed6786d22f"]
product_size: 1027 lines added and 3 removed in 9305f59, of which about 620 non-test lines (irq/mod.rs 312 before its test module, critical_section.rs 148, lib.rs 116, link.ld 56, api irq 58); ADR-052 89 lines; SW-02 61 lines
sprint: SW-02-wp-sw-09-interrupts
author_agent: "author:WP-PDR-41 wave 1a (Claude, firmware developer role)"
reviewer_agent: "reviewer:WP-PDR-41-code (independent code reviewer, iterations 1 and 2; authored no part of WP-PDR-41)"
# criticality: 07 section 14.1 drivers row names the critical section among the drivers the safety-critical
# components depend on (inherited criticality)
criticality: safety-critical
assurance_required: true
assurance_reviewer_agent: "sa-reviewer:WP-PDR-41-code-wp-sw-09, record INSP-102 docs/reviews/PDR/checklists/code-wp-sw-09-software-assurance.md (07 section 2.1.1 Code row and every file with unsafe; iteration 2 delta pending)"
paired_record: INSP-102
iteration: 2
# readiness_met: false: R3 (the ADR is still Proposed) and R5 (no independent test-author file yet) still do not hold;
# unchanged by revision 2, which the lead SE dispatched with them open (iteration 1 section Readiness)
readiness_met: false
# reviewer_verdict: APPROVED at iteration 2 (finding-1 Verified at c6e5100; findings 2 to 6 Minor, carried Open); open Minor findings become liens under rule C1,
# owner the firmware developer, due at the CDR readiness declaration
reviewer_verdict: APPROVED
# assurance_verdict: INSP-102 (the paired software assurance record) was APPROVED at iteration 1; its iteration 2 delta on
# the fix commit is a separate invocation and has not run, so this record carries pending
assurance_verdict: pending
# verdict: held at NEEDS CHANGES. The reviewer verdict is APPROVED at iteration 2, but the software assurance delta
# of the paired record is not yet filed, readiness R3 and R5 do not hold, and the reviewed blobs exist only on unmerged
# rustos branches (lead SE convention of 2026-09-27). The software lead sets verdict when the owner's merge and the PCR-4
# pin-move CR bring the blobs into a configuration cwht consumes, or in the commit right after it
verdict: NEEDS CHANGES
findings_major: 1
findings_minor: 5
findings_open: 5
findings_fixed: 0
findings_verified: 1
findings_deferred: 0
assurance_findings_major: 0
assurance_findings_minor: 0
assurance_tasks_applied: []
# unsafe_sites_reviewed: the seven new sites (two asm blocks, the CsCell Sync impl, two CsCell access blocks,
# the interrupt! no_mangle attribute, the extern block of the 52 handler symbols) and the Mmio pair re-read for
# the new RegAddr::NVIC variant
unsafe_sites_reviewed: 9
deferred_rids: []
items_no: [CK-CODE-B2, CK-CODE-B6, CK-CODE-B7, CK-CODE-D7, CK-CODE-H2, CK-CODE-I1, CK-CODE-I3]
effort_turns: 35
effort_minutes: 70
record_status: Open
date: 2026-09-27
date_closed: null
---

# Peer review record INSP-096: WP-SW-09 interrupts and critical section (rustos `api` and `pico2`), code review, iteration 1

**Product:** rustos branch `cwht/wp-sw-09` at `9305f59` (parent `cwht/wp-sw-11` `213c536`), the blobs of `product_files` (each checked with `git rev-parse 9305f59:<path>`: all equal to the brief), with ADR-052 and SW-02 at cwht `618e441`. Read with `git show` and in a detached scratch worktree (removed after the review); the owner's rustos working tree was not read. **Checklist:** `docs/templates/peer-review-checklist-code.md` revision B. **Independence (rule C4):** this invocation authored no part of WP-PDR-41. **Search first:** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (see INSP-095); the new ADR and sprint files were not yet indexed and were read by path.

**Acceptance criteria (rule C7):** readiness R1 to R6; every item CK-CODE-A1 to CK-CODE-J4; CS-09, CS-10, CS-22, CS-23 and CS-34 (07 sections 7.2, 7.4, 7.7) for this package; the 52 lines of Table 94 (name, number, vector slot, `PROVIDE` line, extern declaration); each `InterruptController` method against NVIC Tables 192 to 195; contract clauses IRQ-1 to IRQ-6; each `unsafe` site; the two questions ADR-052 puts to the reviewer (section 5 CS-10 reading; assumption 2, the `PROVIDE` override); the 07 section 19 closing rule.

## Commands run by the reviewer (evidence)

| # | Command | Result |
|---|---|---|
| C1 | `cargo +1.98.0 test --offline -p pico2 --lib` and `-p api` at `9305f59` | pico2 46 passed (12 new); api `irq_contract` 4 passed |
| C2 | target build dev and release at `9305f59` | no warning |
| C3 | Miri at the stack head `6df18af` (INSP-095 C3) | 95 pico2 and all api tests pass, no undefined behaviour (includes every `CsCell` test) |
| C4 | clippy `-D warnings` and `-W clippy::pedantic`, host and target, short format, filtered to the package files | default lints: no new error in the package files; pedantic: `semicolon_if_nothing_returned` at `critical_section.rs:61` and `:68` (target build) |
| C5 | complexity gate (INSP-095 C7) | PASS; `api/tests/irq_contract.rs:48` `check_out_of_range` CC 13 (yellow, test code), no package function above 12 in flight code |
| C6 | unsafe audit scan (INSP-095 C8) | PASS; the seven new sites all carry `// SAFETY:` |
| C7 | Table 94 cross-check: the `Irq` enum (`irq/mod.rs:58-163`), the 52 `PROVIDE` lines (`link.ld`), vector slots 16 to 67 and the extern block (`lib.rs`) compared name by name and number by number | all 52 agree; slot = 16 + line for every entry |
| C8 | `wc -l firmware/pico2/src/lib.rs` at `213c536` and `9305f59` | 588, then 704 |

## Readiness criteria

| # | Holds | Evidence |
|---|---|---|
| R1 | No (crate level) | pre-existing `pico2` clippy and fmt debt (INSP-095 C4, C6); the package files add only the pedantic items of finding-6 |
| R2 | No | `lib.rs` 704 lines (finding-1) |
| R3 | No | ADR-052 Proposed |
| R4 | N/A | rustos code |
| R5 | No | SW-02 phase 2 open; the contract test `api/tests/irq_contract.rs` is an author draft awaiting the test author's adoption (SW-02 line 47, disclosed) |
| R6 | Yes | C6 |

## Checklist answers

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-A1 | Yes | `#![no_std]` both crates; `std` only in test modules |
| CK-CODE-A2 | Yes | no manifest change |
| CK-CODE-A3 | Yes | `cfg(target_os = "none")` on `with`, the `InterruptController` impl and `Rp2350Nvic::new`; host/target split only |
| CK-CODE-B1 | N/A | `api` and `pico2` |
| CK-CODE-B2 | No | the seven new SAFETY arguments are valid for what they claim, except that the `CsCell` argument omits the non-maskable contexts (finding-4); the pre-existing `Mmio` argument no longer holds for the new `RegAddr::NVIC` (finding-2) |
| CK-CODE-B3 | Yes | no `unsafe fn`; each block one expression; `CsCell` exposes a safe surface |
| CK-CODE-B4 | Yes | NVIC offsets from a `#[repr(C)]` layout with a compile-time assert (`irq/mod.rs:180-199`); access through `Regs`; NVIC has separate set and clear words, so no alias is needed |
| CK-CODE-B5 | Yes | no `static mut`; `CsCell` is the CS-09 cell; `critical_section` is the only masking site |
| CK-CODE-B6 | No | `asm!` outside boot code (finding-3) |
| CK-CODE-B7 | No | audit list regenerated at the pin move (SW-02 line 37); carried to PCR-4 |
| CK-CODE-B8 | Yes | `Rp2350Nvic::new(_handle: DeviceHandle<Self>)`; device `nvic` in `board.rs` |
| CK-CODE-C1 | Yes | no panic path in flight code; `VECTOR_TABLE` indexing is const-evaluated (an out-of-range slot is a compile error) |
| CK-CODE-C2 | Yes | `NoSuchLine` for every method; `Busy` for `CsCell` |
| CK-CODE-C3 | Yes | `NoSuchLine` only for a line above 51 (a caller defect); `Busy` for a nested access, `f` not run |
| CK-CODE-C4 | Yes | `locate` uses `/` and `%` on a `u16` below 52 and `usize::from` (`irq/mod.rs:210-215`) |
| CK-CODE-C5 | Yes | `Irq as u16` is the enum discriminant of a `#[repr(u16)]` enum (`irq/mod.rs:169`), disclosed in SW-02 |
| CK-CODE-C6 | Yes | no floating point |
| CK-CODE-C7 | N/A | no panic handler |
| CK-CODE-D1 | Yes | C5 |
| CK-CODE-D2 | Yes | no loop in flight code of the package |
| CK-CODE-D3 | N/A | not `cwht-core` |
| CK-CODE-D4 | Yes | `#[allow(non_camel_case_types)]` (`irq/mod.rs:57`) and `#[allow(non_snake_case)]` in the macro carry the datasheet-name reason on the line above, the rustos form of the CS-28 exception; no new unreasoned `allow` |
| CK-CODE-D5 | N/A | this package defines no handler body; `interrupt!` forwards to `fn()` |
| CK-CODE-D6 | Yes | nothing starts core 1; `CsCell` soundness rests on it (ADR-052 assumption 1) |
| CK-CODE-D7 | No | finding-1 |
| CK-CODE-D8 | Yes | CS-34: no `NVIC_IPR` write anywhere (`no_priority_register_is_ever_addressed`, `irq/mod.rs:379-388`, and no other `RegAddr::NVIC` writer); CS-35 to CS-37 not touched |
| CK-CODE-D9 | Yes | trait methods on the target are one call each; decisions in `locate`, host-tested |
| CK-CODE-E1 | Yes | the shapes of ADR-052 section 2 items 1 to 4; the placement of `with` in `pico2` departs from the 07 section 19 row (finding-5) |
| CK-CODE-E2 | Yes | `LINES = 52` from Table 94; register offsets from Tables 192 to 195 |
| CK-CODE-E3 | N/A | |
| CK-CODE-E4 | Yes | C7; NVIC `ISER`/`ICER`/`ISPR`/`ICPR` at PPB `0x0e100`, `0x0e180`, `0x0e200`, `0x0e280`, two words each |
| CK-CODE-E5 | Yes | a line above 51 is rejected before any access (`out_of_range_lines_touch_no_register`) |
| CK-CODE-E6 | Yes | `is_enabled` and `is_pending` read back the hardware |
| CK-CODE-E7, E8 | N/A | |
| CK-CODE-E9 | Yes | every item is reachable through the trait, the macro or the board |
| CK-CODE-F1 to F3 | N/A | rustos code (plan WP-PDR-41); the commit cites ADR-052 |
| CK-CODE-G1 | Yes | the line number is validated at the boundary (`locate`) |
| CK-CODE-G2 to G4 | N/A | |
| CK-CODE-G5 | Partial | C3, C5, C6 run; `cargo audit`, `deny`, `geiger` not run (no dependency change; no download permission for the advisory database) |
| CK-CODE-H1 | Yes | `write_line` and `read_line` generic over `Regs`; `CsCell` host-tested with a token built by the test |
| CK-CODE-H2 | No | R5 |
| CK-CODE-H3 | Yes | `locate` boundary pairs (51 and 52); `CsCell` flag true and false for both operations |
| CK-CODE-I1 | No | new items documented; crate-level `#![deny(missing_docs)]` absent (pre-existing, INSP-095) |
| CK-CODE-I2 | Yes | `Irq` names equal the Table 94 names and the handler symbols |
| CK-CODE-I3 | No | finding-6 |
| CK-CODE-I4 | Yes | |
| CK-CODE-J1, J2 | Yes | C1, C2 |
| CK-CODE-J3 | Yes | "enable with no priority argument" is one mechanism: no priority path exists |
| CK-CODE-J4 | Yes | C8 |

**ADR-052 assumption 2 (`PROVIDE` override by a strong definition under `rust-lld`):** plausible and standard `cortex-m-rt` practice; the reviewer did not relink the author's scratch application. The dev-board check (a pended spare line reaches its handler) is the confirming evidence; until it runs the assumption stays open. **07 section 19 closing rule (WP-SW-09 row):** contract test drafted by the author (R5), mock not written, dev-board report not filed, unsafe signatures open; not closable at this commit.

## Findings

| Finding | Origin | Severity | Item | Location | Description | State | Deferred to |
|---|---|---|---|---|---|---|---|
| finding-1 | reviewer | Major | CK-CODE-D7 | `lib.rs` (588 to 704 lines) | CS-18 file length: 116 avoidable lines added to a file already over 500 | Open | |
| finding-2 | reviewer | Minor | CK-CODE-B2 | `reg.rs:106`, `:165-171`, `:180-194` | `Mmio` SAFETY text and `address` doc invalid for `RegAddr::NVIC` | Open | |
| finding-3 | reviewer | Minor | CK-CODE-B6 | `critical_section.rs:60-62`, `:67-69` | `asm!` outside boot code against the letter of CS-10 | Open | |
| finding-4 | reviewer | Minor | CK-CODE-B2 | `critical_section.rs:94-99`, `:116-124` | `CsCell` SAFETY omits NMI and HardFault, which `PRIMASK` does not mask | Open | |
| finding-5 | reviewer | Minor | CK-CODE-E1 | ADR-052 section 2 item 4; `critical_section.rs:52` | `critical_section::with` in `pico2` and target-only, where the 07 section 19 row puts it in the `api` column | Open | |
| finding-6 | reviewer | Minor | CK-CODE-I3 | `critical_section.rs:61`, `:68`; SW-02 line 31 | pedantic lint on new code, while SW-02 reports the new code pedantic-clean | Open | |

### finding-1

**Major, CK-CODE-D7 (CS-18: file length at most 500 lines).** `firmware/pico2/src/lib.rs` grows from 588 lines (`213c536`) to 704 (`9305f59`): 52 vector slot assignments and a 60-line extern block of the 52 handler symbols. The file already exceeded 500 lines at `2ec64c0` (550; INSP-095 finding-7), but this addition is avoidable: the extern block and the table of device-interrupt entries can live in the new `irq` module (for example `irq/vectors.rs` exporting a `const` array of the 52 entries that `VECTOR_TABLE` copies), so the package need not grow the file. SW-02 line 39 reports CS-18 only for `gpio.rs`. **Fix:** move the device-interrupt entries and their extern block out of `lib.rs` so that the package adds no lines to it, and record the pre-existing excess of `lib.rs` as a rustos item for the owner; or, if the owner wants the table in `lib.rs`, a CS-21-style waiver of CS-18 for that file approved by the owner and cited here.

### finding-2

**Minor, CK-CODE-B2 (CS-06).** The two `Mmio` SAFETY comments (`reg.rs:180-194` at `9305f59`) and the `address` doc ("never outside it", `reg.rs:165-171`) bound every access by "the block's 16 KiB register and alias window (section 2.1.3)". The new `RegAddr::NVIC = 0xe000_e100` (`reg.rs:106`) is a Cortex-M33 private-peripheral address, not a 4 KiB-aligned APB block, and has no section 2.1.3 aliases; `offset & 0x3ffc` from it reaches `NVIC_IPR0` (`+0x300`) and the SCB (for example `AIRCR` at `+0xc0c`). Memory safety still holds (every such address is device memory, never Rust-owned), and the CS-34 guarantee rests on the callers' offsets, which `no_priority_register_is_ever_addressed` tests. The written argument is wrong for this variant. **Fix:** state the per-block window in the SAFETY text (the NVIC window being the four two-word groups up to `0x188`), or mask NVIC offsets to that window in `address`.

### finding-3

**Minor, CK-CODE-B6 (CS-10).** CS-10 allows inline assembly only in `pico2` boot code; `critical_section::with` holds two `asm!` blocks (`mrs`/`cpsid i`, `msr PRIMASK`) outside it. CS-09 requires the critical-section cell in `pico2`, and stable Rust has no other way to read and write `PRIMASK`, so the two rules conflict as written. ADR-052 section 5 asks the reviewer to decide: this is a defect of the CS-10 wording, not of the code, and it is resolved by a CS-10 amendment ("boot code and the critical-section primitive") through the writer of 07 (plan section 5.3), not by a waiver. The finding stays open until that amendment is dispositioned.

### finding-4

**Minor, CK-CODE-B2 (CS-06, CS-09).** The `Sync` argument for `CsCell` (`critical_section.rs:94-99`) rests on "accesses never overlap on core 0" because a token exists only while interrupts are masked. `PRIMASK` does not mask NMI or HardFault. `replace` (`:116-124`) checks the borrow flag and then forms a `&mut` without setting the flag, so an NMI or HardFault context that reached the same cell during a `replace` would alias it. No such context exists today (`interrupt!` accepts only `Irq` lines, and `OnHardFault` is a `pico2` halt loop), so the code is sound in this crate, but the SAFETY text does not state the restriction it depends on. **Fix:** add to the SAFETY comment and the module doc that no NMI or HardFault handler may touch a `CsCell`, and that rustos provides no NMI hook.

### finding-5

**Minor, CK-CODE-E1.** The 07 section 19 row WP-SW-09 lists `critical_section::with` in the "`api` trait to add" column. ADR-052 places `with` and `CsCell` in `pico2`, with `with` compiled for the target only (`critical_section.rs:52`), so `cwht-core` cannot name it on the host. The ADR does not record this departure from the plan row or say how `cwht-core` code that shares state with a handler is written and tested on the host. **Fix:** record the placement decision and its rationale in ADR-052 section 2 or 5, and refer the host-side sharing pattern to the firmware architecture ADR (WP-PDR-32).

### finding-6

**Minor, CK-CODE-I3.** `clippy::pedantic` `semicolon_if_nothing_returned` fires at `critical_section.rs:61` and `:68` on the target build (the only build in which `with` exists). SW-02 line 31 reports the new code "`clippy::pedantic` clean ... apart from the rustos house-style `module_inception`". **Fix:** add the two semicolons, and report the G1 and pedantic results in the sprint record as measured on both targets.

## Measurements (SWE-089)

Lines reviewed: about 620 non-test lines plus the 189-line contract draft and the 12 developer tests; ADR-052 and SW-02 in full. Unsafe sites reviewed: 9. Findings: 1 Major, 5 Minor. Effort: 20 turns, 45 minutes (the shared evidence runs are counted in INSP-095).

## Record verdict

`reviewer_verdict: NEEDS CHANGES` on finding-1. Iteration 2 is a delta that verifies finding-1 on a new frozen commit. `verdict` stays `NEEDS CHANGES` until the software assurance record is filed APPROVED and the blobs reach a configuration cwht consumes.

## Iteration 2: delta verification of finding-1 (Major) (2026-09-27, cwht HEAD `5c16930`)

**Scope (rule C1).** Iteration 2 is a delta that verifies the finding-1 fix only. Findings 2 to 6 (Minor) were not touched (ADR-052 section 8) and are not re-reviewed. Product: rustos `cwht/wp-sw-09` at `c6e5100`, whose parent `8b67385` merges `cwht/wp-sw-11` at `4a8e825` into the iteration 1 head `9305f59`; the package delta is `git diff 8b67385 c6e5100` (`irq/mod.rs` 5, `irq/vectors.rs` 163 new, `lib.rs` 148 changed lines), with ADR-052, SW-02 and the sprint index at cwht `e3ce2cb`, the blobs of front matter `product_files`. Checklist as at iteration 1.

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
| D9 | `wc -l firmware/pico2/src/lib.rs` (through `git show`) at `213c536`, `9305f59`, `8b67385`, `c6e5100` and at the later stack heads | 588, 704, 704, 564; then 565 (`58fe739`), 565 (`38434b2`), 566 (`48e07ec`) |
| D10 | Link test (the author did not repeat it at revision 2): a scratch `#![no_std]` `#![no_main]` binary depending on `pico2` by path, with `pico2::entry!`, `pico2::interrupt!(SPAREIRQ_IRQ_0, ..)` and `pico2::interrupt!(TIMER0_IRQ_0, ..)`, built `--release` for `thumbv8m.main-none-eabihf` with `-C link-arg=-Tlink.ld` against the worktree at `9305f59` and at `c6e5100`; `.vector_table` dumped with the toolchain's `llvm-objdump -s`, symbols with `llvm-nm` | the two `.vector_table` sections are byte-identical; 68 words; slot 0 `0x20082000`, slot 1 `OnReset`, slot 3 `OnHardFault`; slots 16 (`TIMER0_IRQ_0`) and 62 (`SPAREIRQ_IRQ_0`) hold the application handler (`0x10000125`, the two empty handlers folded to one address by the linker), slots 17, 63 and 67 `DefaultHandler` (`0x10000131`) |
| D11 | Slot map: the 52 `t[n] = Vector { handler: NAME }` lines of `lib.rs` at `9305f59` against the 52 `t[n] = handler(NAME)` lines of `irq/vectors.rs` at `c6e5100`; the 52 names of both extern blocks | identical slot numbers, names and order |

### Verification of finding-1, case by case (rule C7)

| Case | Required by finding-1 | At `c6e5100` | Result |
|---|---|---|---|
| The 52 device-interrupt entries | out of `lib.rs` | in `irq/vectors.rs` `with_device_interrupts`, a `const fn` over `[Vector; 68]` that `VECTOR_TABLE` calls (`lib.rs:563`); the table stays a compile-time constant in `.vector_table` (D10) | Verified |
| The extern block of the 52 symbols | out of `lib.rs` | in `irq/vectors.rs`, with its `// SAFETY:` comment unchanged in substance (D6 counts it) | Verified |
| The package adds no lines to `lib.rs` | no growth | 564 lines against 588 before the package (D9): the package now removes 24 lines, because the `Vector` union and its `Sync` impl moved too | Verified |
| No behaviour change | (implicit in a move) | slot map identical (D11); linked table byte-identical (D10); 49 host tests and target builds (D2, D3) | Verified |
| Pre-existing excess recorded as a rustos item | record it for the owner | ADR-052 section 8 and SW-02 "Phase 1, revision 2" say `lib.rs` 564 lines, the excess predates the package and is reported to the owner as a rustos item | Verified |

Visibility: `irq::vectors` is private and target-only; `Vector` and `with_device_interrupts` are `pub(crate)` and re-exported as `pub(crate)` from `irq`, so the public API of `pico2` is unchanged. The `// SAFETY:` text of the `Sync` impl and of the extern block is unchanged.

### Checklist items re-answered for the fix

| Id | Iteration 2 answer | Evidence |
|---|---|---|
| CK-CODE-D7 | No, pre-existing only | the package no longer grows `lib.rs` (finding-1 Verified); `lib.rs` is still above 500 lines from before cwht touched it, which INSP-095 finding-7 (Minor) carries; `irq/mod.rs` 394 and `irq/vectors.rs` 163 lines |
| CK-CODE-B2, B6 on the moved code | as iteration 1 | the moved `unsafe impl Sync` and extern block keep their SAFETY arguments; findings 2 to 4 unchanged |
| CK-CODE-J1 | Yes | D3, D10 |

### Findings (current state at iteration 2)

| Finding | Origin | Severity | Item | Location | Description | State | Deferred to |
|---|---|---|---|---|---|---|---|
| finding-1 | reviewer | Major | CK-CODE-D7 | `lib.rs` (588 to 704 lines at `9305f59`; 564 at `c6e5100`) | CS-18 file length: 116 avoidable lines added to a file already over 500 | Verified (`c6e5100`) | |
| finding-2 | reviewer | Minor | CK-CODE-B2 | `reg.rs:106`, `:165-171`, `:180-194` | `Mmio` SAFETY text and `address` doc invalid for `RegAddr::NVIC` | Open (lien, rule C1) | CDR readiness declaration |
| finding-3 | reviewer | Minor | CK-CODE-B6 | `critical_section.rs:60-62`, `:67-69` | `asm!` outside boot code against the letter of CS-10 | Open (lien, rule C1) | CDR readiness declaration |
| finding-4 | reviewer | Minor | CK-CODE-B2 | `critical_section.rs:94-99`, `:116-124` | `CsCell` SAFETY omits NMI and HardFault, which `PRIMASK` does not mask | Open (lien, rule C1) | CDR readiness declaration |
| finding-5 | reviewer | Minor | CK-CODE-E1 | ADR-052 section 2 item 4; `critical_section.rs:52` | `critical_section::with` in `pico2` and target-only, where the 07 section 19 row puts it in the `api` column | Open (lien, rule C1) | CDR readiness declaration |
| finding-6 | reviewer | Minor | CK-CODE-I3 | `critical_section.rs:61`, `:68`; SW-02 line 31 | pedantic lint on new code, while SW-02 reports the new code pedantic-clean | Open (lien, rule C1) | CDR readiness declaration |

No new finding.

### Measurements (SWE-089), iteration 2

Lines reviewed: the 316 changed lines of `8b67385..c6e5100` and the 18 changed lines of ADR-052 and SW-02; the merge `8b67385` was checked only for conflict-free content (its WP-SW-11 part is INSP-095's delta). Unsafe sites: 2 moved (the `Sync` impl and the extern block), text re-read, none added. Findings: 0 new. Effort of this iteration: about 15 turns and 25 minutes (front matter totals include iteration 1).

### Record verdict, iteration 2

`reviewer_verdict: APPROVED`: finding-1 is Verified and no Major is open. Minor findings 2 to 6 become liens under rule C1 (owner the firmware developer, due at the CDR readiness declaration). `verdict` stays `NEEDS CHANGES` until the paired software assurance record INSP-102 re-checks the moved unsafe sites in its iteration 2 delta, readiness R3 and R5 hold, and the owner's merge with the PCR-4 pin-move CR brings `c6e5100` into a configuration cwht consumes.
