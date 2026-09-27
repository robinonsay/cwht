---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md section 13;
# docs/process/07-software-engineering-plan.md section 10.2). Checklist: docs/templates/peer-review-checklist-code.md
# revision B, as PDR work plan WP-PDR-41 "Reviewer" and "Records" name. Product: rustos work package WP-SW-02
# (GPIO input snapshot through SIO) on rustos branch cwht/wp-sw-02 at f85a190 (stacked on cwht/wp-sw-01 at
# a1cd160), with its design record ADR-054 and sprint record SW-04 (cwht main 618e441), frozen before this review
# (rule C2). The blobs are on an unmerged rustos branch, so the record verdict is held until the owner's merge and
# the pin-move CR (lead SE convention of 2026-09-27).
id: INSP-098
checklist: peer-review-checklist-code
checklist_revision: B
checklist_file: docs/reviews/PDR/checklists/code-wp-sw-02.md
product: "rustos cwht/wp-sw-02: api/src/gpio/mod.rs (InputLevels, InputSnapshot), firmware/pico2/src/gpio/snapshot.rs and the input tracking in firmware/pico2/src/gpio/gpio.rs (WP-SW-02)"
# product_commit (iteration 2): the rustos branch head of cwht/wp-sw-02, 38434b2, the finding-1 fix on the merge
# 5d4637f of cwht/wp-sw-01 58fe739 into f85a190 (iteration 1). Blobs equal git rev-parse 38434b2:<path> (rustos)
# and git rev-parse e3ce2cb:<path>, HEAD:<path> and git hash-object at HEAD 5c16930 (cwht)
product_commit: "38434b26dd74ebf288a63eff42331d73913e6087"
product_files: ["docs/decisions/adr/ADR-054-wp-sw-02-sio-input-snapshot.md@ae2afdd838fb08909d88e727c7bb6b6dce509dc8", "docs/sprints/SW-04-wp-sw-02-sio-snapshot.md@a79d4d99185c92aa7ddff700b570e5a8e4a27884", "docs/sprints/index.md@7ae0cbcc6087d45ab4df10cac623d453ca13c395", "rustos:api/src/gpio/mod.rs@f0250c93e08856270a702324b19fda0b04e9199b", "rustos:api/tests/gpio_snapshot_contract.rs@0918c1933350c2b159924d480a1738768f4b34c2", "rustos:firmware/pico2/src/gpio/gpio.rs@cdb5fc92052e74727106486163d3965454538979", "rustos:firmware/pico2/src/gpio/mod.rs@d71011bf3934812b52eaac6fa3ccebaae0067a41", "rustos:firmware/pico2/src/gpio/snapshot.rs@00e2c30105014dc7d970e0b45491e5bd84ebe6e3"]
product_files_iteration_1: ["docs/decisions/adr/ADR-054-wp-sw-02-sio-input-snapshot.md@848102d2dac6d026a4718ae1fd57eb5f270c8245", "docs/sprints/SW-04-wp-sw-02-sio-snapshot.md@1686ecc09144d6ef16644522eff1cd0fb65f3584", "docs/sprints/index.md@fb217bcb6ff684b8117f104970a4e091a4899b1c", "rustos:api/src/gpio/mod.rs@f0250c93e08856270a702324b19fda0b04e9199b", "rustos:api/tests/gpio_snapshot_contract.rs@0918c1933350c2b159924d480a1738768f4b34c2", "rustos:firmware/pico2/src/gpio/gpio.rs@d7ea7a706b4131e5625aac2755845882c172e807", "rustos:firmware/pico2/src/gpio/mod.rs@d71011bf3934812b52eaac6fa3ccebaae0067a41", "rustos:firmware/pico2/src/gpio/snapshot.rs@6b5ddac5ff90032bf07c9ba9fac4f4fa96378a5b"]
product_size: 409 lines added and 3 removed in f85a190, of which about 185 non-test lines (api gpio 72, snapshot.rs 69 before its test module, gpio.rs 37 changed, gpio/mod.rs 1); ADR-054 86 lines; SW-04 60 lines
sprint: SW-04-wp-sw-02-sio-snapshot
author_agent: "author:WP-PDR-41 wave 1a (Claude, firmware developer role)"
reviewer_agent: "reviewer:WP-PDR-41-code (independent code reviewer, iterations 1 and 2; authored no part of WP-PDR-41)"
# criticality: 07 section 14.1 drivers row (GPIO through SIO), inherited from the keyer input path (HZ-004, HZ-010)
criticality: safety-critical
assurance_required: true
assurance_reviewer_agent: "sa-reviewer:WP-PDR-41-code-wp-sw-02, record INSP-104 docs/reviews/PDR/checklists/code-wp-sw-02-software-assurance.md (07 section 2.1.1 Code row; iteration 2 delta pending)"
paired_record: INSP-104
iteration: 2
# readiness_met: false: R3 (the ADR is still Proposed) and R5 (no independent test-author file yet) still do not hold;
# unchanged by revision 2, which the lead SE dispatched with them open (iteration 1 section Readiness)
readiness_met: false
# reviewer_verdict: APPROVED at iteration 2 (finding-1 Verified at 38434b2; findings 2 and 3 Minor, carried Open); open Minor findings become liens under rule C1,
# owner the firmware developer, due at the CDR readiness declaration
reviewer_verdict: APPROVED
# assurance_verdict: INSP-104 (the paired software assurance record) was NEEDS CHANGES at iteration 1; its iteration 2 delta on
# the fix commit is a separate invocation and has not run, so this record carries pending
assurance_verdict: pending
# verdict: held at NEEDS CHANGES. The reviewer verdict is APPROVED at iteration 2, but the software assurance delta
# of the paired record is not yet filed, readiness R3 and R5 do not hold, and the reviewed blobs exist only on unmerged
# rustos branches (lead SE convention of 2026-09-27). The software lead sets verdict when the owner's merge and the PCR-4
# pin-move CR bring the blobs into a configuration cwht consumes, or in the commit right after it
verdict: NEEDS CHANGES
findings_major: 1
findings_minor: 2
findings_open: 2
findings_fixed: 0
findings_verified: 1
findings_deferred: 0
assurance_findings_major: 0
assurance_findings_minor: 0
assurance_tasks_applied: []
unsafe_sites_reviewed: 0
deferred_rids: []
items_no: [CK-CODE-D7, CK-CODE-H2, CK-CODE-I1, CK-CODE-I3]
effort_turns: 18
effort_minutes: 40
record_status: Open
date: 2026-09-27
date_closed: null
---

# Peer review record INSP-098: WP-SW-02 SIO input snapshot (rustos `api::gpio` and `pico2::gpio`), code review, iteration 1

**Product:** rustos branch `cwht/wp-sw-02` at `f85a190` (parent `cwht/wp-sw-01` `a1cd160`), the blobs of `product_files` (checked with `git rev-parse f85a190:<path>`: all equal to the brief), with ADR-054 and SW-04 at cwht `618e441`. **Checklist:** `docs/templates/peer-review-checklist-code.md` revision B. **Independence (rule C4):** this invocation authored no part of WP-PDR-41. **Search first:** as INSP-095.

**Acceptance criteria (rule C7):** readiness R1 to R6; every item CK-CODE-A1 to CK-CODE-J4; CS-22 (ALARM1 sampling), CS-29 and CS-35 (SIO only, no `IO_BANK0` edge interrupt); clauses SNP-1 to SNP-4; the mask check (empty, stray, accepted); the 07 section 19 closing rule.

## Commands run by the reviewer (evidence)

| # | Command | Result |
|---|---|---|
| C1 | host tests at `f85a190` | pico2 77 passed (6 new); api `gpio_snapshot_contract` 5 passed |
| C2 | target build dev and release | no warning |
| C3 | Miri at the stack head (INSP-095 C3) | clean |
| C4 | clippy `-D warnings` and pedantic, filtered to the lines this commit changed (`git blame -L 150,200 f85a190` of `gpio.rs`) | `needless_return` (a default lint) at `gpio.rs:156` (changed line) and `gpio.rs:195` (new line), written in the file's pre-existing `return` style; nothing in `snapshot.rs` or `api/src/gpio/mod.rs` |
| C5 | `cargo fmt --check` at `2ec64c0` and at the stack head, `gpio.rs` | 35 differences before, 38 after: the commit adds three, the `use` of `snapshot` placed out of order and its neighbours (`gpio.rs:38-44`) |
| C6 | `git show 2ec64c0:firmware/pico2/src/gpio/gpio.rs \| wc -l` and at `f85a190` | 512, then 546 |
| C7 | datasheet: `SIO.GPIO_IN` offset `0x004` (section 3.1.11, Table 16); `MAX_GPIO_PIN` = 30 (`common/mod.rs:40`) | agree; `GPIO_IN` covers GPIO 0 to 31, so one read covers every Pico 2 pin |

## Readiness criteria

| # | Holds | Evidence |
|---|---|---|
| R1 | No (crate level) | pre-existing debt; finding-2 |
| R2 | No | `gpio.rs` 546 lines (finding-1); `lib.rs` 705 (INSP-096 finding-1) |
| R3 | No | ADR-054 Proposed |
| R4 | N/A | rustos code |
| R5 | No | SW-04 phase 2 open; contract test an author draft (SW-04 line 46, disclosed) |
| R6 | Yes | no new `unsafe` |

## Checklist answers

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-A1 to A3 | Yes | `no_std`; no manifest change; `InputSnapshot` impl gated on `target_os = "none"` only |
| CK-CODE-B1 to B7 | N/A | no `unsafe` added; the read goes through `Regs` (`snapshot.rs:55-57`), offset from the `Sio` layout with a compile-time assert (`snapshot.rs:51-52`) |
| CK-CODE-B8 | Yes | `input_snapshot` needs the port (`&self`), and only pins already made inputs through their consumed `PinHandle` can be named |
| CK-CODE-C1 | Yes | no panic path; `BIT` bound checked at compile time (`gpio.rs`, `assert!(N < MAX_GPIO_PIN)`) |
| CK-CODE-C2 | Yes | `GpioError::NotInput { mask }` carries the stray pins |
| CK-CODE-C3 | Yes | empty and stray masks refused before a sampler exists |
| CK-CODE-C4, C5, C6 | Yes | bit operations only; no casts; no floating point |
| CK-CODE-C7 | N/A | |
| CK-CODE-D1, D2 | Yes | CC at most 3; no loop |
| CK-CODE-D3, D4 | N/A, Yes | not `cwht-core`; no new `allow` |
| CK-CODE-D5 | Yes | the sampler is `Copy` and one `GPIO_IN` load, fit for the ALARM1 handler of CS-22 (ADR-054 section 2 item 2) |
| CK-CODE-D6 | Yes | |
| CK-CODE-D7 | No | finding-1 |
| CK-CODE-D8 | Yes | CS-35: SIO `GPIO_IN` only; no `IO_BANK0` interrupt register and no pad write in the package |
| CK-CODE-D9 | Yes | `check_snapshot_mask` and `read_inputs` host-tested; the trait method is one call |
| CK-CODE-E1 | Yes | ADR-054 section 2; the trait name departs from the 07 section 19 row (finding-3) |
| CK-CODE-E2 | Yes | no timing constant |
| CK-CODE-E3 | N/A | |
| CK-CODE-E4 | Yes | C7 |
| CK-CODE-E5 | Yes | the "configured input" prerequisite is enforced (`check_snapshot_mask`, `snapshot.rs:42-48`) |
| CK-CODE-E6 | Yes | `InputLevels::new` masks the bits, so SNP-2 holds by construction |
| CK-CODE-E7 to E9 | N/A, N/A, Yes | |
| CK-CODE-F1 to F3 | N/A | rustos code |
| CK-CODE-G1 | Yes | the mask is validated at the boundary; debounce and rate are `cwht-core` duties (CS-29) |
| CK-CODE-G2 | Yes | the snapshot reports levels only; no key-line logic here |
| CK-CODE-G3, G4 | N/A | |
| CK-CODE-G5 | Partial | as INSP-096 |
| CK-CODE-H1 | Yes | `read_inputs` generic over `Regs` |
| CK-CODE-H2 | No | R5 |
| CK-CODE-H3 | Yes | mask decision pairs: empty, stray, accepted |
| CK-CODE-I1 | No | new items documented; crate-level `deny(missing_docs)` absent (pre-existing) |
| CK-CODE-I2 | Yes | |
| CK-CODE-I3 | No | finding-2 |
| CK-CODE-I4 | Yes | |
| CK-CODE-J1 to J4 | Yes | C1, C2, C6 |

**07 section 19 closing rule (WP-SW-02 row):** contract test drafted by the author, mock not written, dev-board report not filed; not closable at this commit.

## Findings

| Finding | Origin | Severity | Item | Location | Description | State | Deferred to |
|---|---|---|---|---|---|---|---|
| finding-1 | reviewer | Major | CK-CODE-D7 | `gpio/gpio.rs` (512 to 546 lines) | CS-18 file length: 34 avoidable lines added to a file already over 500 | Open | |
| finding-2 | reviewer | Minor | CK-CODE-I3 | `gpio/gpio.rs:38-44`, `:156`, `:171-172`, `:195` | new lines fail `rustfmt` and `clippy -D warnings` | Open | |
| finding-3 | reviewer | Minor | CK-CODE-E1 | ADR-054 section 2 | `InputSnapshot::snapshot` replaces the 07 section 19 row's `SioInputs::snapshot()` without a note | Open | |

### finding-1

**Major, CK-CODE-D7 (CS-18).** `firmware/pico2/src/gpio/gpio.rs` is 512 lines at `2ec64c0` and 546 at `f85a190`. The author disclosed this (SW-04 line 30, "CS-18 cross item"), but the growth is avoidable: `input_snapshot`, the `NotInput` handling and the `BIT` constant can sit in an `impl` block in `snapshot.rs` (an inherent `impl Rp2350Gpio` may live in any module of the crate, with `inputs` made `pub(crate)`), leaving `gpio.rs` with the one-line recording of the input bit. The same rule is applied to `lib.rs` in INSP-096 finding-1. **Fix:** move the additions out of `gpio.rs` so that the package does not grow it, and record the pre-existing 512-line excess as a rustos item for the owner; or an owner-approved CS-18 waiver for the file, cited here.

### finding-2

**Minor, CK-CODE-I3 (CS-26, CS-27).** The commit's new and changed lines in `gpio.rs` follow the file's pre-existing style rather than the gate: the `use crate::gpio::snapshot::{...}` is placed after the `api::` imports (`gpio.rs:44`), which `rustfmt` reorders, and `input_snapshot` opens its brace on its own line (`:171-172`) (C5: three new `rustfmt` differences); `return Self{...}` (`:156`) and `return Ok(pin);` (`:195`) are `clippy::needless_return` under `-D warnings` (C4). SW-04 line 30 reports the new code clippy-clean. The file's pre-existing debt is not this package's, but the new lines should not add to it. **Fix:** format the new and changed lines as `rustfmt` does and write them without `return`, and report the lint result as measured.

### finding-3

**Minor, CK-CODE-E1.** The 07 section 19 row WP-SW-02 names the addition "a batched `SioInputs::snapshot()`"; ADR-054 introduces `api::gpio::InputSnapshot::snapshot()` returning `InputLevels`, and says nothing of the name in the plan row. The shape is better (a fixed, checked mask); the departure should be recorded so that the 07 row and the `cwht-hal-mock` author use the same name. **Fix:** one sentence in ADR-054 section 2 or 4.2 recording the name and pointing the 07 section 19 row update to the writer of 07.

## Measurements (SWE-089)

Lines reviewed: about 185 non-test lines, the 174-line contract draft and 6 developer tests; ADR-054 and SW-04 in full. Unsafe sites: 0. Findings: 1 Major, 2 Minor. Effort: 10 turns, 25 minutes.

## Record verdict

`reviewer_verdict: NEEDS CHANGES` on finding-1. Iteration 2 is a delta that verifies finding-1. `verdict` stays `NEEDS CHANGES` until the software assurance record is filed APPROVED and the blobs reach a configuration cwht consumes.

## Iteration 2: delta verification of finding-1 (Major) (2026-09-27, cwht HEAD `5c16930`)

**Scope (rule C1).** Iteration 2 is a delta that verifies the finding-1 fix only. Findings 2 and 3 (Minor) were not touched (ADR-054 section 8) and are not re-reviewed. Product: rustos `cwht/wp-sw-02` at `38434b2`, whose parent `5d4637f` merges `cwht/wp-sw-01` at `58fe739` into the iteration 1 head `f85a190`; the package delta is `git diff 5d4637f 38434b2` (`gpio/gpio.rs` 52, `gpio/snapshot.rs` 70 changed lines), with ADR-054, SW-04 and the sprint index at cwht `e3ce2cb`. Checklist as at iteration 1.

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
| D9 | `wc -l` (through `git show`) of `gpio/gpio.rs` and `gpio/snapshot.rs` at `2ec64c0`, `f85a190`, `38434b2`, `48e07ec`; `git diff 2ec64c0 38434b2 -- firmware/pico2/src/gpio/gpio.rs` | `gpio.rs` 512, 546, 512, 512; `snapshot.rs` absent, 125, 177, 177; against rustos master the package changes 4 places in `gpio.rs` (struct doc, the field, `new`, `input_from_handle`) and adds no line |

### Verification of finding-1, case by case (rule C7)

| Case | Required by finding-1 | At `38434b2` | Result |
|---|---|---|---|
| `input_snapshot` | out of `gpio.rs` | inherent `impl Rp2350Gpio` in `snapshot.rs` | Verified |
| `NotInput` handling | out of `gpio.rs` | `snapshot::NotInput { mask }`, its own public type in the public `gpio::snapshot` module; the `GpioError::NotInput` variant and its `Debug` arm are removed, so `GpioError` is again as on rustos master | Verified |
| `BIT` constant | out of `gpio.rs` | inherent `impl<const N: usize> Rp2350GpioIn<N>` in `snapshot.rs`, with the compile-time `N < MAX_GPIO_PIN` assert; referenced by `track_input`, so it is still checked for every input pin built | Verified |
| Input recording | one-line call in `gpio.rs` | `input_from_handle` is `self.track_input(Rp2350GpioIn::new_input(handle, pull))`; `track_input` in `snapshot.rs` records the bit only on `Ok`, as revision 1 did with `?` | Verified |
| No growth of `gpio.rs` | package adds no line | 512 before and after (D9) | Verified |
| Construction guard | (unchanged property) | `inputs` is `pub(super)`, visible in `gpio` and its child `snapshot`; the struct literal cannot be written outside `gpio`, so `new` with its `DeviceHandle` stays the only public route, as the struct doc now states | Verified |
| Pre-existing excess recorded | rustos item for the owner | ADR-054 section 2 and SW-04 "Phase 1, revision 2": 512 lines, excess predates the package, reported to the owner as a rustos item | Verified |

Behaviour: the mask rule is unchanged (`check_snapshot_mask` now returns `NotInput`); the two rejection tests compare the value directly; 81 host tests at `38434b2` and 101 at `48e07ec` pass (D2). The public signature of `Rp2350Gpio::input_snapshot` changes its error type from `GpioError` to `NotInput`; nothing outside the package used the iteration 1 variant, and ADR-054 section 2 records the change.

### Checklist items re-answered for the fix

| Id | Iteration 2 answer | Evidence |
|---|---|---|
| CK-CODE-D7 | No, pre-existing only | the package no longer grows `gpio.rs` (finding-1 Verified); `gpio.rs` is still 512 lines from before cwht touched it, reported to the owner; `snapshot.rs` 177 |
| CK-CODE-E1 | Yes | ADR-054 section 2 states the `NotInput` type |

### Findings (current state at iteration 2)

| Finding | Origin | Severity | Item | Location | Description | State | Deferred to |
|---|---|---|---|---|---|---|---|
| finding-1 | reviewer | Major | CK-CODE-D7 | `gpio/gpio.rs` (512 to 546 lines at `f85a190`; 512 at `38434b2`) | CS-18 file length: 34 avoidable lines added to a file already over 500 | Verified (`38434b2`) | |
| finding-2 | reviewer | Minor | CK-CODE-I3 | `gpio/gpio.rs:38-44`, `:156`, `:171-172`, `:195` (iteration 1 lines) | new lines fail `rustfmt` and `clippy -D warnings` | Open (lien, rule C1) | CDR readiness declaration |
| finding-3 | reviewer | Minor | CK-CODE-E1 | ADR-054 section 2 | `InputSnapshot::snapshot` replaces the 07 section 19 row's `SioInputs::snapshot()` without a note | Open (lien, rule C1) | CDR readiness declaration |

No new finding. Of the finding-2 lines, those that moved to `snapshot.rs` are now rustfmt-clean (D8) and the lines left in `gpio.rs` raise no clippy report (D7); finding-2 stays Open for the author to confirm against the whole list at the next revision.

### Measurements (SWE-089), iteration 2

Lines reviewed: the 122 changed lines of `5d4637f..38434b2` and the 18 changed lines of ADR-054 and SW-04. Unsafe sites: none. Findings: 0 new. Effort of this iteration: about 10 turns and 15 minutes (front matter totals include iteration 1).

### Record verdict, iteration 2

`reviewer_verdict: APPROVED`: finding-1 is Verified and no Major is open. Minor findings 2 and 3 become liens under rule C1 (owner the firmware developer, due at the CDR readiness declaration). `verdict` stays `NEEDS CHANGES` until the paired software assurance record INSP-104 files its iteration 2 delta APPROVED, readiness R3 and R5 hold, and the owner's merge with the PCR-4 pin-move CR brings `38434b2` into a configuration cwht consumes.
