---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md section 13;
# docs/process/07-software-engineering-plan.md section 10.2). Checklist: docs/templates/peer-review-checklist-code.md
# revision B, as PDR work plan WP-PDR-41 "Reviewer" and "Records" name. Product: rustos work package WP-SW-01
# (TIMER0 time base and alarms, api::time, timer register ICD) on rustos branch cwht/wp-sw-01 at a1cd160 (stacked
# on cwht/wp-sw-09 at 9305f59), with its design record ADR-053 and sprint record SW-03 (cwht main 618e441),
# frozen before this review (rule C2). The blobs are on an unmerged rustos branch, so the record verdict is held
# until the owner's merge and the pin-move CR (lead SE convention of 2026-09-27).
id: INSP-097
checklist: peer-review-checklist-code
checklist_revision: B
checklist_file: docs/reviews/PDR/checklists/code-wp-sw-01.md
product: "rustos cwht/wp-sw-01: api/src/time/mod.rs, firmware/pico2/src/timer/ and docs/icd/rp2350/timer/ (WP-SW-01)"
# product_commit (iteration 2): the rustos branch head of cwht/wp-sw-01, 58fe739, the finding-1 fix on the merge
# 698929d of cwht/wp-sw-09 c6e5100 into a1cd160 (iteration 1). Blobs equal git rev-parse 58fe739:<path> (rustos)
# and git rev-parse e3ce2cb:<path>, HEAD:<path> and git hash-object at HEAD 5c16930 (cwht)
product_commit: "58fe739e964435996001ed61a47423409010a09d"
product_files: ["docs/decisions/adr/ADR-053-wp-sw-01-timer0-time-base-and-alarms.md@71f0b629402dbe8c596825b21e97d4a1905c7b0d", "docs/sprints/SW-03-wp-sw-01-timer0.md@1cea48ef0db4fb9558c1a8d51698395fc7c520b8", "docs/sprints/index.md@7ae0cbcc6087d45ab4df10cac623d453ca13c395", "rustos:api/src/time/mod.rs@3c6c567381ecbb37a39bb9bdb16f3e2012cb955a", "rustos:api/tests/time_contract.rs@f9293ee88a267cadc319f7c79664498ae4b0379e", "rustos:api/src/lib.rs@a189e7bdc5c3fdc3249836997691e7c7397f77b5", "rustos:firmware/pico2/src/timer/mod.rs@4004047d3c725929ff3e806377b394bd10f201ee", "rustos:firmware/pico2/src/timer/tests.rs@ed14e12ea380af12f91382589f4f3af8feba3542", "rustos:firmware/pico2/src/timer/timer.rs@e24f1d525e11029df5b43521914ed84dc1bd6322", "rustos:firmware/pico2/src/timer/timer_tests.rs@bbe9427594a88e8547e27daacd5c1fe03218421b", "rustos:firmware/pico2/src/common/board.rs@c69de18ce76e4bfbd6bc9041af8f92a875830659", "rustos:firmware/pico2/src/common/reg.rs@93e97f73e735698b7a12c2e5129a4ee6eda9720c", "rustos:firmware/pico2/src/common/reset.rs@4f26beb0c8b53258f1bc78f112eaf56360af4915", "rustos:firmware/pico2/src/lib.rs@5393076ccf56ebfa2ea17056284f8f7cb341f044", "rustos:docs/icd/rp2350/timer/index.md@11c66ca302a4429a4a9f3d5f93180844d7acf509", "rustos:docs/icd/rp2350/timer/01_overview.md@39bb74ec115f35c8d1671f520fe1413a40fabe8c", "rustos:docs/icd/rp2350/timer/02_programming.md@be5fe7f2bc4a12e59f0a4321b965c29fe82da65f", "rustos:docs/icd/rp2350/timer/03_registers.md@ca7ea335deede210c1b4222a2a23cd1290facb1d", "rustos:docs/icd/rp2350/index.md@41ba1c62d239fc2508cc8bf87388647021607d03"]
product_files_iteration_1: ["docs/decisions/adr/ADR-053-wp-sw-01-timer0-time-base-and-alarms.md@471b900f52211b6096259c62c651c19fa6df789e", "docs/sprints/SW-03-wp-sw-01-timer0.md@8fed7b88be09a0294df2c0b00b513e15876a2cbb", "docs/sprints/index.md@fb217bcb6ff684b8117f104970a4e091a4899b1c", "rustos:api/src/time/mod.rs@f62b496149a3813b8fd3281523f2c3c001fa97b2", "rustos:api/tests/time_contract.rs@f9293ee88a267cadc319f7c79664498ae4b0379e", "rustos:api/src/lib.rs@a189e7bdc5c3fdc3249836997691e7c7397f77b5", "rustos:firmware/pico2/src/timer/mod.rs@a1ef29c8ffaf56c1b4c23c92d9da944f958480ee", "rustos:firmware/pico2/src/timer/tests.rs@247eeb82a4623ba75bd12a94fbd5efd2e2b78c27", "rustos:firmware/pico2/src/timer/timer.rs@e24f1d525e11029df5b43521914ed84dc1bd6322", "rustos:firmware/pico2/src/timer/timer_tests.rs@e1657cab15530f62d291a7dba99ab0ec18577416", "rustos:firmware/pico2/src/common/board.rs@c69de18ce76e4bfbd6bc9041af8f92a875830659", "rustos:firmware/pico2/src/common/reg.rs@93e97f73e735698b7a12c2e5129a4ee6eda9720c", "rustos:firmware/pico2/src/common/reset.rs@4f26beb0c8b53258f1bc78f112eaf56360af4915", "rustos:firmware/pico2/src/lib.rs@dcd1c254e01474c56ce2f43a97afb26171c25579", "rustos:docs/icd/rp2350/timer/index.md@11c66ca302a4429a4a9f3d5f93180844d7acf509", "rustos:docs/icd/rp2350/timer/01_overview.md@39bb74ec115f35c8d1671f520fe1413a40fabe8c", "rustos:docs/icd/rp2350/timer/02_programming.md@be5fe7f2bc4a12e59f0a4321b965c29fe82da65f", "rustos:docs/icd/rp2350/timer/03_registers.md@ca7ea335deede210c1b4222a2a23cd1290facb1d", "rustos:docs/icd/rp2350/index.md@41ba1c62d239fc2508cc8bf87388647021607d03"]
product_size: 1429 lines added in a1cd160, of which about 590 non-test Rust lines (timer/mod.rs 179 before its test module, timer.rs 252, api time 158) and 231 ICD lines; ADR-053 88 lines; SW-03 61 lines
sprint: SW-03-wp-sw-01-timer0
author_agent: "author:WP-PDR-41 wave 1a (Claude, firmware developer role)"
reviewer_agent: "reviewer:WP-PDR-41-code (independent code reviewer, iterations 1 and 2; authored no part of WP-PDR-41)"
# criticality: 07 section 14.1 drivers row (TIMER alarms), inherited from the keyer, scheduler and safe-state components
criticality: safety-critical
assurance_required: true
assurance_reviewer_agent: "sa-reviewer:WP-PDR-41-code-wp-sw-01, record INSP-103 docs/reviews/PDR/checklists/code-wp-sw-01-software-assurance.md (07 section 2.1.1 Code row; iteration 2 delta pending)"
paired_record: INSP-103
iteration: 2
# readiness_met: false: R3 (the ADR is still Proposed) and R5 (no independent test-author file yet) still do not hold;
# unchanged by revision 2, which the lead SE dispatched with them open (iteration 1 section Readiness)
readiness_met: false
# reviewer_verdict: APPROVED at iteration 2 (finding-1 and finding-2 Verified at 58fe739; findings 3 to 5 Minor, carried Open); open Minor findings become liens under rule C1,
# owner the firmware developer, due at the CDR readiness declaration
reviewer_verdict: APPROVED
# assurance_verdict: INSP-103 (the paired software assurance record) was NEEDS CHANGES at iteration 1; its iteration 2 delta on
# the fix commit is a separate invocation and has not run, so this record carries pending
assurance_verdict: pending
# verdict: held at NEEDS CHANGES. The reviewer verdict is APPROVED at iteration 2, but the software assurance delta
# of the paired record is not yet filed, readiness R3 and R5 do not hold, and the reviewed blobs exist only on unmerged
# rustos branches (lead SE convention of 2026-09-27). The software lead sets verdict when the owner's merge and the PCR-4
# pin-move CR bring the blobs into a configuration cwht consumes, or in the commit right after it
verdict: NEEDS CHANGES
findings_major: 1
findings_minor: 4
findings_open: 3
findings_fixed: 0
findings_verified: 2
findings_deferred: 0
assurance_findings_major: 0
assurance_findings_minor: 0
assurance_tasks_applied: []
# unsafe_sites_reviewed: none new (C6 of INSP-095: the package adds no unsafe site)
unsafe_sites_reviewed: 0
deferred_rids: []
items_no: [CK-CODE-C5, CK-CODE-D7, CK-CODE-H2, CK-CODE-I1, CK-CODE-I3]
effort_turns: 30
effort_minutes: 60
record_status: Open
date: 2026-09-27
date_closed: null
---

# Peer review record INSP-097: WP-SW-01 TIMER0 time base and alarms (rustos `api::time` and `pico2::timer`), code review, iteration 1

**Product:** rustos branch `cwht/wp-sw-01` at `a1cd160` (parent `cwht/wp-sw-09` `9305f59`), the blobs of `product_files` (each checked with `git rev-parse a1cd160:<path>`: all equal to the brief), with ADR-053 and SW-03 at cwht `618e441`; read with `git show` and in a detached scratch worktree (removed after the review). **Checklist:** `docs/templates/peer-review-checklist-code.md` revision B. **Independence (rule C4):** this invocation authored no part of WP-PDR-41. **Search first:** as INSP-095.

**Acceptance criteria (rule C7):** readiness R1 to R6; every item CK-CODE-A1 to CK-CODE-J4; CS-14 (timer wrap argument), CS-22, CS-34 and CS-37 (the `&ClocksReady` prerequisite) for this package; each register of the timer ICD `03_registers.md` against datasheet section 12.8.5; the three decisions `select_time`, `plan_arm`, `after_arm` against their truth tables and datasheet sections 12.8.3 and 12.8.4.1; clauses CLK-1, CLK-2 and ALM-1 to ALM-6; the 07 section 19 closing rule.

## Commands run by the reviewer (evidence)

| # | Command | Result |
|---|---|---|
| C1 | host tests at `a1cd160` | pico2 71 passed (25 new); api `time_contract` 5 passed |
| C2 | target build dev and release | no warning |
| C3 | Miri at the stack head (INSP-095 C3) | clean |
| C4 | clippy `-D warnings` and pedantic, filtered to the package files | `module_inception` at `timer/mod.rs:32` (`-D warnings`); pedantic `cast_possible_truncation` at `timer_tests.rs:16` |
| C5 | complexity gate (INSP-095 C7) | PASS; no package function above CC 12 |
| C6 | datasheet check against the rustos extract at `2ec64c0`: section 12.8.3 ("The alarms match on the lower 32 bits"; "Writing the time to the ALARM register sets the ARMED bit as a side effect"; "Once the alarm has fired, the ARMED bit clears to 0"), section 12.8.4.1 and the SDK `timer_busy_wait_until` listing of section 12.8.4.3 (reached means `timerawl >= target`) | offsets, reset values and field meanings of `TimerRegs` (`timer/mod.rs:36-84`) and of `03_registers.md` agree; TIMER0 base `0x400b_0000`, `RESETS` bit 23 agree; the section does not state whether a write of `ALARMn` that lands in the microsecond of the match fires (finding-1) |

## Readiness criteria

| # | Holds | Evidence |
|---|---|---|
| R1 | No (crate level) | pre-existing debt (INSP-095); finding-5 |
| R2 | No | `lib.rs` 705 lines (INSP-096 finding-1); the package's own files are at most 255 lines |
| R3 | No | ADR-053 Proposed |
| R4 | N/A | rustos code |
| R5 | No | SW-03 phase 2 open; contract test is an author draft (SW-03 line 47, disclosed) |
| R6 | Yes | no new `unsafe` |

## Checklist answers

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-A1 | Yes | `#![no_std]`; test-only `std` |
| CK-CODE-A2 | Yes | no manifest change |
| CK-CODE-A3 | Yes | `cfg(target_os = "none")` on constructors and trait impls only |
| CK-CODE-B1 to B7 | N/A | no `unsafe` in the package; register access through `Regs` (B4: offsets from `#[repr(C)]` `TimerRegs` with a compile-time assert; `INTE` through the set alias, `ARMED` and `INTR` write-1-to-clear, so no read-modify-write) |
| CK-CODE-B8 | Yes | `Rp2350Timer0::new(_handle: DeviceHandle<Self>, _clocks: &ClocksReady)`; `split` consumes the timer, each alarm exists once |
| CK-CODE-C1 | Yes | no panic path in flight code |
| CK-CODE-C2 | Yes | `TimerError`, `AlarmError`; `Rp2350Clock` uses `Infallible` |
| CK-CODE-C3 | Yes | `ResetTimeout`, `TooFar`, `NotArmed` each a distinct return; `Missed` becomes `Scheduled::Due`, which the caller acts on (ALM-1) |
| CK-CODE-C4 | Yes | 64-bit time, no wrap in practice (584 000 years, `api/src/time/mod.rs:3-5`); `at - now` only after `at > now` (`timer/mod.rs:132-136`); `Duration::from_millis` bound stated (`api/src/time/mod.rs:94`) |
| CK-CODE-C5 | No | flight code has no numeric `as` (the low word by byte destructuring, `timer/mod.rs:138-140`), but the developer test `timer_tests.rs:15-16` uses truncating `as u32` casts (finding-5) |
| CK-CODE-C6 | Yes | no floating point |
| CK-CODE-C7 | N/A | |
| CK-CODE-D1, D2 | Yes | C5; the one loop is `poll` with `RESET_POLL_BUDGET` |
| CK-CODE-D3 | N/A | not `cwht-core`; `Rp2350Alarm::irq` has a `_` arm (finding-3) |
| CK-CODE-D4 | Yes | no new `allow` |
| CK-CODE-D5 | N/A | no handler here; the handler pattern (`take_fired`, re-arm at the previous target plus 1000 µs) is documented in `timer.rs:8-18` and ADR-053 section 4.2 |
| CK-CODE-D6 | Yes | |
| CK-CODE-D7 | No | package files within CS-18; `lib.rs` above 500 lines (INSP-096 finding-1) |
| CK-CODE-D8 | Yes | CS-37 prerequisite enforced by `&ClocksReady` (`timer.rs:110`); CS-34 untouched (no NVIC write) |
| CK-CODE-D9 | Yes | trait methods one call each; decisions in `select_time`, `plan_arm`, `after_arm` |
| CK-CODE-E1 | Yes | ADR-053 section 2 shapes (`Clock::now`, `Alarm::schedule_at/cancel/is_armed/take_fired`, `Scheduled::{Armed, Due}`) |
| CK-CODE-E2 | Yes | `MAX_SPAN_US`, `RESET_POLL_BUDGET` named and cited |
| CK-CODE-E3 | N/A | |
| CK-CODE-E4 | No | finding-1 (the missed-match boundary); the other register behaviour agrees with C6; the SDK four-read time selection is correct (`select_time`, `timer/mod.rs:109-112`) |
| CK-CODE-E5 | No | finding-1: the post-arm check that ADR-053 section 2 and SWE-134 g rely on has a gap at `now == at` |
| CK-CODE-E6 | Yes | `ARMED` and `INTR` read back after the arm (`timer.rs:186-188`); `take_fired` clears only after a read saw the bit (`timer.rs:210-217`) |
| CK-CODE-E7, E8 | N/A | |
| CK-CODE-E9 | Yes | |
| CK-CODE-F1 to F3 | N/A | rustos code |
| CK-CODE-G1 | Yes | `at` validated by `plan_arm` (`Due`, `TooFar`) before any arm |
| CK-CODE-G2 to G4 | N/A | |
| CK-CODE-G5 | Partial | as INSP-096 |
| CK-CODE-H1 | Yes | `schedule`, `read_time`, `release` generic over `Regs`; `api::time` gives the host a mock-clock seam |
| CK-CODE-H2 | No | R5 |
| CK-CODE-H3 | Yes | MC/DC pairs for `after_arm` (`timer/tests.rs:53-78`) and `plan_arm`; they encode the finding-1 boundary as `Pending` (`tests.rs:60`) |
| CK-CODE-I1 | No | new items documented; crate-level `deny(missing_docs)` absent (pre-existing) |
| CK-CODE-I2 | Yes | register names as Table 1226 |
| CK-CODE-I3 | No | finding-5 |
| CK-CODE-I4 | Yes | |
| CK-CODE-J1 to J4 | Yes | C1, C2; `wc -l` measured |

**Timer ICD (`docs/icd/rp2350/timer/`):** the register list, reset values and access types (`DBGPAUSE` `0x6`, `ARMED` and `INTR` WC) and the alias statement agree with section 12.8.5; no finding. **07 section 19 closing rule (WP-SW-01 row):** contract test drafted by the author, mock not written, dev-board report not filed, ACC-EMU-001 comparison pending WP-PDR-42; not closable at this commit.

## Findings

| Finding | Origin | Severity | Item | Location | Description | State | Deferred to |
|---|---|---|---|---|---|---|---|
| finding-1 | reviewer | Major | CK-CODE-E4, CK-CODE-E5 | `timer/mod.rs:159-178`; `timer.rs:186-199`; `timer/tests.rs:60` | missed-match check treats `armed` with `now == at` as pending | Open | |
| finding-2 | reviewer | Minor | CK-CODE-E1 | `api/src/time/mod.rs:17-23` | ALM-1 and ALM-2 do not cover a target that passes during the call | Open | |
| finding-3 | reviewer | Minor | CK-CODE-D3 | `timer.rs:86-94` | `Rp2350Alarm::<N>::irq()` compiles for `N > 3` and returns `TIMER0_IRQ_3` | Open | |
| finding-4 | reviewer | Minor | CK-CODE-E9 | `common/reset.rs:16-19`; `clocks/regs.rs:65-68` | two sets of constants for the `RESETS` offsets | Open | |
| finding-5 | reviewer | Minor | CK-CODE-I3, CK-CODE-C5 | `timer/mod.rs:32`; `timer_tests.rs:15-16`; SW-03 line 31 | `module_inception` under `-D warnings` and truncating `as` casts, while SW-03 reports the code clean | Open | |

### finding-1

**Major, CK-CODE-E4 and CK-CODE-E5 (SWE-134 g, k; ADR-053 alternative A).** `schedule` reads the time after writing `ALARMn` and calls `after_arm(armed, intr, now, at)` (`timer.rs:186-189`), which reports `Missed` only when `now > at` (`timer/mod.rs:166-172`); the MC/DC test fixes `after_arm(true, false, 200, 200) == Pending` (`timer/tests.rs:60`). If the write lands in the microsecond in which the counter already equals `at`, and the comparator matches only when the counter changes to the value (section 12.8.3 says the alarms "match on the lower 32 bits" and does not say that a write during the matching microsecond fires), then the alarm stays armed, the post-arm read sees `now == at`, and the driver returns `Armed` for a match that will next occur 2^32 µs (71 minutes) later: the silent wait ADR-053 section 3 option A exists to exclude, on the keyer element alarm (HZ-004) or the 1 kHz tick. `plan_arm` admits `at = now + 1`, so the window is a real fraction of the arms made one microsecond ahead. Treating `now >= at` with `armed` as `Missed` is safe under either comparator behaviour (the alarm is disarmed and `Due` returned, and the caller acts at once), and it matches the SDK's own "reached" test in section 12.8.4.3 (`timerawl >= target`). **Fix:** `Missed` when `armed && now >= at`; update the truth table (`timer/mod.rs:159-164`), the ALM clause text (finding-2) and the MC/DC pair (`tests.rs:60` becomes `Missed`); or, if the author keeps `>`, cite evidence that a write in the matching microsecond fires (a dev-board case in the WP-SW-01 check).

### finding-2

**Minor, CK-CODE-E1.** ALM-1 returns `Due` for `at` "not later than the clock at the time of the call" and ALM-2 returns `Armed` for `at` "later than the clock" (`api/src/time/mod.rs:17-23`). The `Missed` path (`timer.rs:191-194`) returns `Due` for an `at` that was later than the clock when the call began and passed during it, which the clauses as worded assign to `Armed`. **Fix:** word both clauses against the clock as read at the end of the call ("`Due` when the target is not later than the clock when `schedule_at` returns"), which the reference model and the contract checks then state.

### finding-3

**Minor, CK-CODE-D3.** `Rp2350Alarm::<N>::irq()` (`timer.rs:86-94`) is an associated function that does not reference `Self::VALID`, so `Rp2350Alarm::<7>::irq()` compiles and returns `TIMER0_IRQ_3` through the `_` arm; the compile-time bound is enforced only by `new`. **Fix:** `let () = Self::VALID;` at the start of `irq`, and match `3 =>` explicitly.

### finding-4

**Minor, CK-CODE-E9.** WP-SW-01 adds `RESET_OFFSET` and `RESET_DONE_OFFSET` to `common/reset.rs` (lines 16 to 19), while WP-SW-11 defines `RESETS_RESET` and `RESETS_RESET_DONE` for the same registers in `clocks/regs.rs:65-68`. Two constants for one register invite drift. **Fix:** make the clocks driver use the `common::reset` constants and delete its copies.

### finding-5

**Minor, CK-CODE-I3 and CK-CODE-C5 (CS-15, CS-21).** `module_inception` at `timer/mod.rs:32` fails `clippy -D warnings` (a default lint), and `timer_tests.rs:15-16` builds the time with `(t >> 32) as u32` and `t as u32` (pedantic `cast_possible_truncation`; CS-15 forbids `as` numeric casts). SW-03 line 31 reports the new code clean "apart from the rustos house-style `module_inception`". **Fix:** byte destructuring or `u32::try_from` in the test helper, a CS-21 waiver comment (or rename) for the module name, and the lint result reported as measured.

## Measurements (SWE-089)

Lines reviewed: about 590 non-test Rust lines, 231 ICD lines, the 342-line contract draft and the 25 developer tests; ADR-053 and SW-03 in full. Unsafe sites: 0. Findings: 1 Major, 4 Minor. Effort: 18 turns, 40 minutes.

## Record verdict

`reviewer_verdict: NEEDS CHANGES` on finding-1. Iteration 2 is a delta that verifies finding-1. `verdict` stays `NEEDS CHANGES` until the software assurance record is filed APPROVED and the blobs reach a configuration cwht consumes.

## Iteration 2: delta verification of finding-1 (Major) and the finding-2 wording (2026-09-27, cwht HEAD `5c16930`)

**Scope (rule C1).** Iteration 2 is a delta that verifies the finding-1 fix. The ALM-1 and ALM-2 wording of finding-2 (Minor) is part of the finding-1 fix as iteration 1 wrote it ("the ALM clause text (finding-2)"), the author changed it, and it is verified here; findings 3 to 5 (Minor) were not touched and are not re-reviewed. Product: rustos `cwht/wp-sw-01` at `58fe739`, whose parent `698929d` merges `cwht/wp-sw-09` at `c6e5100` into the iteration 1 head `a1cd160`; the package delta is `git diff 698929d 58fe739` (`api/src/time/mod.rs` 15, `timer/mod.rs` 20, `timer/tests.rs` 7, `timer/timer_tests.rs` 11 changed lines), with ADR-053, SW-03 and the sprint index at cwht `e3ce2cb`. Checklist as at iteration 1.

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
| D9 | Datasheet: rustos `docs/extracted/rp2350-datasheet.md` at `2ec64c0` (`git show`), section 12.8.4.3, SDK `timer_busy_wait_until`, extract lines 89212 to 89230 | the SDK waits `while (hi == hi_target && timer->timerawl < (uint32_t) target)`: a target equal to the time counts as reached, the test ADR-053 cites |

### Verification of finding-1 and finding-2, case by case (rule C7)

| Case | Required | At `58fe739` | Result |
|---|---|---|---|
| Decision | `Missed` when `armed && now >= at` | `after_arm` (`timer/mod.rs:172-184`): `if armed { if now >= at { Missed } else { Pending } }`; the doc of `AfterArm::Missed` gives the reason and the SDK reference | Verified |
| Truth table | column `now >= at` | `timer/mod.rs:165-170` | Verified |
| MC/DC pair of condition L | `(200, 200)` becomes `Missed` | `timer/tests.rs:60` `(199, 200)` Pending; `:67` `(200, 200)` Missed, `(201, 200)` Missed; the L pair is now `(199,200)` against `(200,200)`, which isolates the `>=` edge; the A and I pairs are unchanged | Verified |
| Driver path | still armed at `now == at` gives `Due` and disarms | new `schedule_still_armed_when_the_time_equals_the_target_is_due_and_disarmed` (`timer_tests.rs:119-127`): time reads 99 before and 100 after the write, `ARMED` 1, target 100: `Ok(Scheduled::Due)` and the last two writes disarm (`ARMED` 1) and clear `INTR`; unchanged `timer.rs` (blob `e24f1d5`) calls `after_arm` with these values | Verified |
| Safety under both comparator behaviours | the change is safe whether or not a write in the matching microsecond fires | if it fires, `ARMED` has cleared and `INTR` is set: row `0 1 any` gives `Pending`, reported `Armed` with the fire latched (ALM-2 "possibly before the call returns"); if not, `Missed` disarms and reports `Due`; a fire latched after the read is discarded by the disarm, so the call never reports `Due` with a fire latched (ALM-1) | Verified |
| ALM-1 and ALM-2 wording (finding-2) | cover a target that passes during the call | ALM-1: `Due` for `at` not later than the clock at the start of the call, and possibly for an `at` reached while the call runs, never with a fire latched; ALM-2: `Armed`, or `Due` under ALM-1 when the clock reaches `at` during the call, and after `Armed` exactly one fire (`api/src/time/mod.rs:17-26`) | Verified |
| ADR-053 | decision, alternative A and dev-board case follow | sections 2, 3 row A and 4.3 updated; the dev-board check gains an `at` equal to the time read at arming, 10 000 repetitions, no 71-minute wait | Verified |

Observation (no finding): `api/tests/time_contract.rs` (unchanged) checks ALM-2 by requiring `Armed` for `at` 500 µs ahead of a reference model whose clock does not move during a call; the revised ALM-2 also allows `Due` if the clock reaches `at` during the call, which a model with a frozen clock never does, so the check stays valid for the models it runs against.

### Checklist items re-answered for the fix

| Id | Iteration 2 answer | Evidence |
|---|---|---|
| CK-CODE-E4 | Yes | table above, rows Decision and Driver path, with section 12.8.3 and the SDK test (D9) |
| CK-CODE-E5 | Yes | an alarm armed in the matching microsecond can no longer be reported `Armed` while it waits 2^32 µs |
| CK-CODE-E1 | Yes | ALM-1 and ALM-2 now state the call-window case the driver implements |
| CK-CODE-H3 | Yes | MC/DC pair for L updated to the new edge |

### Findings (current state at iteration 2)

| Finding | Origin | Severity | Item | Location | Description | State | Deferred to |
|---|---|---|---|---|---|---|---|
| finding-1 | reviewer | Major | CK-CODE-E4, CK-CODE-E5 | `timer/mod.rs:165-184`; `timer/tests.rs:60-68`; `timer_tests.rs:119-127` | missed-match check treated `armed` with `now == at` as pending | Verified (`58fe739`) | |
| finding-2 | reviewer | Minor | CK-CODE-E1 | `api/src/time/mod.rs:17-26` | ALM-1 and ALM-2 did not cover a target that passes during the call | Verified (`58fe739`) | |
| finding-3 | reviewer | Minor | CK-CODE-D3 | `timer.rs:86-94` | `Rp2350Alarm::<N>::irq()` compiles for `N > 3` and returns `TIMER0_IRQ_3` | Open (lien, rule C1) | CDR readiness declaration |
| finding-4 | reviewer | Minor | CK-CODE-E9 | `common/reset.rs:16-19`; `clocks/regs.rs:65-68` | two sets of constants for the `RESETS` offsets | Open (lien, rule C1) | CDR readiness declaration |
| finding-5 | reviewer | Minor | CK-CODE-I3, CK-CODE-C5 | `timer/mod.rs:32`; `timer_tests.rs:15-16`; SW-03 line 31 | `module_inception` under `-D warnings` and truncating `as` casts, while SW-03 reports the code clean | Open (lien, rule C1) | CDR readiness declaration |

No new finding.

### Measurements (SWE-089), iteration 2

Lines reviewed: the 53 changed lines of `698929d..58fe739`, the unchanged `timer.rs` `schedule` path, and the 22 changed lines of ADR-053 and SW-03. Unsafe sites: none. Findings: 0 new. Effort of this iteration: about 12 turns and 20 minutes (front matter totals include iteration 1).

### Record verdict, iteration 2

`reviewer_verdict: APPROVED`: finding-1 and finding-2 are Verified and no Major is open. Minor findings 3 to 5 become liens under rule C1 (owner the firmware developer, due at the CDR readiness declaration). `verdict` stays `NEEDS CHANGES` until the paired software assurance record INSP-103 files its iteration 2 delta APPROVED, readiness R3 and R5 hold, and the owner's merge with the PCR-4 pin-move CR brings `58fe739` into a configuration cwht consumes.
