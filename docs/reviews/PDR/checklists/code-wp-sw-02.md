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
product_commit: "f85a19085760f7c34803c094e918f6115c21da3d"
product_files: ["docs/decisions/adr/ADR-054-wp-sw-02-sio-input-snapshot.md@848102d2dac6d026a4718ae1fd57eb5f270c8245", "docs/sprints/SW-04-wp-sw-02-sio-snapshot.md@1686ecc09144d6ef16644522eff1cd0fb65f3584", "docs/sprints/index.md@fb217bcb6ff684b8117f104970a4e091a4899b1c", "rustos:api/src/gpio/mod.rs@f0250c93e08856270a702324b19fda0b04e9199b", "rustos:api/tests/gpio_snapshot_contract.rs@0918c1933350c2b159924d480a1738768f4b34c2", "rustos:firmware/pico2/src/gpio/gpio.rs@d7ea7a706b4131e5625aac2755845882c172e807", "rustos:firmware/pico2/src/gpio/mod.rs@d71011bf3934812b52eaac6fa3ccebaae0067a41", "rustos:firmware/pico2/src/gpio/snapshot.rs@6b5ddac5ff90032bf07c9ba9fac4f4fa96378a5b"]
product_size: 409 lines added and 3 removed in f85a190, of which about 185 non-test lines (api gpio 72, snapshot.rs 69 before its test module, gpio.rs 37 changed, gpio/mod.rs 1); ADR-054 86 lines; SW-04 60 lines
sprint: SW-04-wp-sw-02-sio-snapshot
author_agent: "author:WP-PDR-41 wave 1a (Claude, firmware developer role)"
reviewer_agent: "reviewer:WP-PDR-41-code (independent code reviewer, iteration 1; authored no part of WP-PDR-41)"
# criticality: 07 section 14.1 drivers row (GPIO through SIO), inherited from the keyer input path (HZ-004, HZ-010)
criticality: safety-critical
assurance_required: true
assurance_reviewer_agent: "pending: separate software assurance invocation, record docs/reviews/PDR/checklists/code-wp-sw-02-software-assurance.md (plan WP-PDR-41 Records; 07 section 2.1.1 Code row)"
iteration: 1
readiness_met: false
reviewer_verdict: NEEDS CHANGES
assurance_verdict: pending
verdict: NEEDS CHANGES
findings_major: 1
findings_minor: 2
findings_open: 3
findings_fixed: 0
findings_verified: 0
findings_deferred: 0
assurance_findings_major: 0
assurance_findings_minor: 0
assurance_tasks_applied: []
unsafe_sites_reviewed: 0
deferred_rids: []
items_no: [CK-CODE-D7, CK-CODE-H2, CK-CODE-I1, CK-CODE-I3]
effort_turns: 10
effort_minutes: 25
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
