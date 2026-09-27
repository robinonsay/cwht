---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md section 13;
# docs/process/07-software-engineering-plan.md section 10.2). Checklist: docs/templates/peer-review-checklist-code.md
# revision B, as PDR work plan WP-PDR-41 "Reviewer" and "Records" name. Product: rustos work package WP-SW-03
# (PWM output, api::pwm, PWM register ICD) on rustos branch cwht/wp-sw-03 at 6df18af (stacked on cwht/wp-sw-02 at
# f85a190), with its design record ADR-055 and sprint record SW-05 (cwht main 618e441), frozen before this review
# (rule C2). The blobs are on an unmerged rustos branch, so the record verdict is held until the owner's merge and
# the pin-move CR (lead SE convention of 2026-09-27).
id: INSP-099
checklist: peer-review-checklist-code
checklist_revision: B
checklist_file: docs/reviews/PDR/checklists/code-wp-sw-03.md
product: "rustos cwht/wp-sw-03: api/src/pwm/mod.rs, firmware/pico2/src/pwm/ and docs/icd/rp2350/pwm/ (WP-SW-03)"
# product_commit (iteration 2): the rustos branch head of cwht/wp-sw-03, 48e07ec, the finding-1 fix (and the
# INSP-105 finding-1 fix) on the merge 9df9c57 of cwht/wp-sw-02 38434b2 into 6df18af (iteration 1). Blobs equal
# git rev-parse 48e07ec:<path> (rustos) and git rev-parse e3ce2cb:<path>, HEAD:<path> and git hash-object at
# HEAD 5c16930 (cwht)
product_commit: "48e07ec7d651f8f323f8b82b2af5d5647afe0fe3"
product_files: ["docs/decisions/adr/ADR-055-wp-sw-03-pwm-output.md@c2c7cc999e033340195dd7363fe661b91ece0318", "docs/sprints/SW-05-wp-sw-03-pwm.md@d904d7deaa3553e5685244931a0b96730a8ee8dc", "docs/sprints/index.md@7ae0cbcc6087d45ab4df10cac623d453ca13c395", "rustos:api/src/pwm/mod.rs@b859f3705320a2d88bcd6839c540b8068ef6b6ab", "rustos:api/tests/pwm_contract.rs@7df5fdd237aefba2b13ec72d62945ba38092146b", "rustos:api/src/lib.rs@5e79e2b739469c8c077c9a637814977e956e88a5", "rustos:firmware/pico2/src/pwm/mod.rs@9c8ed4c4ba7c2b279cd736c518897206b40689f4", "rustos:firmware/pico2/src/pwm/pwm.rs@92b634e18bcbd4316a92edbfcef66b228b85a93c", "rustos:firmware/pico2/src/pwm/pwm_tests.rs@82d96ce9f75326f3254ebced6a4ff3b64d4b53ff", "rustos:firmware/pico2/src/pwm/tests.rs@c0a59856277c6e45e70dab78f3b6fe058ac4da2b", "rustos:firmware/pico2/src/common/board.rs@eeb8407e77a93718c7e0a2cb320fa2ec6b25f4cc", "rustos:firmware/pico2/src/common/reg.rs@ec94f2cdee391615d8fd88b0650a3f830bc2ef80", "rustos:firmware/pico2/src/lib.rs@46107a9e0e48a88f4ce1c53441bb8bc482c818b2", "rustos:docs/icd/rp2350/pwm/index.md@17e8dabbc10f7a54ce6e50cb0cd50d97378af8f7", "rustos:docs/icd/rp2350/pwm/01_overview.md@98ae5870e970cfdfe644dcb19a3dd7823552b32c", "rustos:docs/icd/rp2350/pwm/02_registers.md@7f93b2004a0d0065bec0342e5f7a0bc28acb5a7a", "rustos:docs/icd/rp2350/index.md@426a75dfd588af945bba6b5533da819b93d18a75"]
product_files_iteration_1: ["docs/decisions/adr/ADR-055-wp-sw-03-pwm-output.md@7b2a9d920d57d0a03e4b995de811cad0e68215c3", "docs/sprints/SW-05-wp-sw-03-pwm.md@975d9268b5b455d7436b919e67fe02d948014764", "docs/sprints/index.md@fb217bcb6ff684b8117f104970a4e091a4899b1c", "rustos:api/src/pwm/mod.rs@1c13d0ad73ffb972a59399d9b93ce11b1b7d406f", "rustos:api/tests/pwm_contract.rs@7df5fdd237aefba2b13ec72d62945ba38092146b", "rustos:api/src/lib.rs@5e79e2b739469c8c077c9a637814977e956e88a5", "rustos:firmware/pico2/src/pwm/mod.rs@9c8ed4c4ba7c2b279cd736c518897206b40689f4", "rustos:firmware/pico2/src/pwm/pwm.rs@75bca4e87fe68c4f61906e27b18b0d43cc07fb9f", "rustos:firmware/pico2/src/pwm/pwm_tests.rs@c3286c6d9db9bb776f1d8c2e79107eff1755e60e", "rustos:firmware/pico2/src/pwm/tests.rs@c0a59856277c6e45e70dab78f3b6fe058ac4da2b", "rustos:firmware/pico2/src/common/board.rs@eeb8407e77a93718c7e0a2cb320fa2ec6b25f4cc", "rustos:firmware/pico2/src/common/reg.rs@ec94f2cdee391615d8fd88b0650a3f830bc2ef80", "rustos:firmware/pico2/src/lib.rs@5122df422db03e15da04aa9cc784d4b96d437ec0", "rustos:docs/icd/rp2350/pwm/index.md@17e8dabbc10f7a54ce6e50cb0cd50d97378af8f7", "rustos:docs/icd/rp2350/pwm/01_overview.md@346e561de8e7aea729ffb4e6274d0778d327634b", "rustos:docs/icd/rp2350/pwm/02_registers.md@7f93b2004a0d0065bec0342e5f7a0bc28acb5a7a", "rustos:docs/icd/rp2350/index.md@426a75dfd588af945bba6b5533da819b93d18a75"]
product_size: 1101 lines added in 6df18af, of which about 470 non-test Rust lines (pwm/mod.rs 165 before its test module, pwm.rs 226, api pwm 80) and 197 ICD lines; ADR-055 90 lines; SW-05 61 lines
sprint: SW-05-wp-sw-03-pwm
author_agent: "author:WP-PDR-41 wave 1a (Claude, firmware developer role)"
reviewer_agent: "reviewer:WP-PDR-41-code (independent code reviewer, iterations 1 and 2; authored no part of WP-PDR-41)"
# criticality: 07 section 14.1 drivers row (PWM for sidetone and audio level), inherited from SW-AUDIO and SW-KEYER (HZ-005)
criticality: safety-critical
assurance_required: true
assurance_reviewer_agent: "sa-reviewer:WP-PDR-41-code-wp-sw-03, record INSP-105 docs/reviews/PDR/checklists/code-wp-sw-03-software-assurance.md (07 section 2.1.1 Code row; iteration 2 delta pending, including its own finding-1)"
paired_record: INSP-105
iteration: 2
# readiness_met: false: R3 (the ADR is still Proposed) and R5 (no independent test-author file yet) still do not hold;
# unchanged by revision 2, which the lead SE dispatched with them open (iteration 1 section Readiness)
readiness_met: false
# reviewer_verdict: APPROVED at iteration 2 (finding-1 Verified at 48e07ec; finding-2 Minor, carried Open); open Minor findings become liens under rule C1,
# owner the firmware developer, due at the CDR readiness declaration
reviewer_verdict: APPROVED
# assurance_verdict: INSP-105 (the paired software assurance record) was NEEDS CHANGES (with its own Major, finding-1) at iteration 1; its iteration 2 delta on
# the fix commit is a separate invocation and has not run, so this record carries pending
assurance_verdict: pending
# verdict: held at NEEDS CHANGES. The reviewer verdict is APPROVED at iteration 2, but the software assurance delta
# of the paired record is not yet filed, readiness R3 and R5 do not hold, and the reviewed blobs exist only on unmerged
# rustos branches (lead SE convention of 2026-09-27). The software lead sets verdict when the owner's merge and the PCR-4
# pin-move CR bring the blobs into a configuration cwht consumes, or in the commit right after it
verdict: NEEDS CHANGES
findings_major: 1
findings_minor: 1
findings_open: 1
findings_fixed: 0
findings_verified: 1
findings_deferred: 0
assurance_findings_major: 0
assurance_findings_minor: 0
assurance_tasks_applied: []
unsafe_sites_reviewed: 0
deferred_rids: []
items_no: [CK-CODE-D7, CK-CODE-H2, CK-CODE-I1, CK-CODE-I3]
effort_turns: 32
effort_minutes: 70
record_status: Open
date: 2026-09-27
date_closed: null
---

# Peer review record INSP-099: WP-SW-03 PWM output (rustos `api::pwm` and `pico2::pwm`), code review, iteration 1

**Product:** rustos branch `cwht/wp-sw-03` at `6df18af` (parent `cwht/wp-sw-02` `f85a190`), the blobs of `product_files` (checked with `git rev-parse 6df18af:<path>`: all equal to the brief), with ADR-055 and SW-05 at cwht `618e441`. **Checklist:** `docs/templates/peer-review-checklist-code.md` revision B. **Independence (rule C4):** this invocation authored no part of WP-PDR-41. **Search first:** as INSP-095.

**Acceptance criteria (rule C7):** readiness R1 to R6; every item CK-CODE-A1 to CK-CODE-J4; CS-36 (slices 0 to 7, own `CSR.EN`) and CS-37 (`&ClocksReady`); clauses PWM-1 to PWM-6; the `timing` refusals (0 Hz, divider range, period range, 0.1 %) and the ADR-055 worked values (700 Hz, 20 kHz); the attach order; each register of the PWM ICD against datasheet section 12.5.3; the requirements and hazard control ADR-055 section 1 names as constraining (REQ-SW-KEYER-033, 027, 035; HZ-005); the 07 section 19 closing rule.

## Commands run by the reviewer (evidence)

| # | Command | Result |
|---|---|---|
| C1 | host tests at `6df18af` | pico2 95 passed (18 new); api `pwm_contract` 5 passed |
| C2 | target build dev and release | no warning |
| C3 | Miri at `6df18af` (INSP-095 C3) | 95 passed, clean |
| C4 | clippy `-D warnings` and pedantic, filtered to the package files | `module_inception` at `pwm/mod.rs:29` (`-D warnings`); no other |
| C5 | complexity gate (INSP-095 C7) | PASS; `timing` the package maximum, below 12 |
| C6 | worked values by hand: 700 Hz at 150 MHz, smallest divider in sixteenths with period at most 65 535 counts is 53 (3.3125, since 52 gives 65 934 counts); period 64 690 counts; 150e6 / (3.3125 × 64 690) = 700.0003 Hz. 20 kHz: divider 16, period 7 500, exact | agree with ADR-055 section 2 |
| C7 | register check: `PWM_BASE` `0x400a_8000`, slice stride `0x14`, `EN` at `0x0f0` (`12 × 0x14`), `DIV` `INT` 11:4 and `FRAC` 3:0, `FUNCSEL` 4 = PWM, pad `ISO` bit 8 and `OD` bit 7, `RESETS` bit 16; GPIO `N` to slice `(N / 2) mod 8` for `N < 30` | agree with sections 12.5.2 and 12.5.3 and the ICD pages |
| C8 | `REQ-SW-KEYER-033` and HZ-005 K4 read from `docs/requirements/sw/sw-keyer/requirements.json` and `docs/safety/hazards.json` | 033: "The keyer firmware shall assert the sidetone gate within 1 ms of each key-down assertion" (Draft); K4 (Proposed): "sidetone onset within 1 ms of key-down with a 3 to 5 ms envelope; no DC step at any transition" |

## Readiness criteria

| # | Holds | Evidence |
|---|---|---|
| R1 | No (crate level) | pre-existing debt; finding-2 |
| R2 | No | `lib.rs` 706 lines (INSP-096 finding-1); the package files are at most 229 lines |
| R3 | No | ADR-055 Proposed |
| R4 | N/A | rustos code |
| R5 | No | SW-05 phase 2 open; contract test an author draft (SW-05 line 47, disclosed) |
| R6 | Yes | no new `unsafe` |

## Checklist answers

| Id | Answer | Evidence |
|---|---|---|
| CK-CODE-A1 to A3 | Yes | `no_std`; no manifest change; `new`, `output_from_handle` and the trait impl gated on `target_os = "none"` only |
| CK-CODE-B1 to B7 | N/A | no `unsafe`; access through `Regs`; `SliceRegs` layout with compile-time asserts (`pwm/mod.rs:33-58`); pad bits cleared through the clear alias (`pwm.rs:147`) |
| CK-CODE-B8 | Yes | `Rp2350Pwm::new(_handle: DeviceHandle<Self>, &ClocksReady, &Rp2350Gpio)`; `output_from_handle` consumes `PinHandle<N>` |
| CK-CODE-C1 | Yes | no panic path; `SLICE` bound checked at compile time (`pwm.rs:52-55`) |
| CK-CODE-C2, C3 | Yes | `PwmError::{ResetTimeout, SliceInUse, FrequencyOutOfRange}`; a refused frequency leaves state unchanged (`frequency_on` updates `period` only on success, PWM-2) |
| CK-CODE-C4 | Yes | `timing` in `u64` with the range checks before the `u32::try_from` (`pwm/mod.rs:123-152`); `cc_value` at most 1000 × 65 535 in `u32` |
| CK-CODE-C5, C6 | Yes | no numeric `as`; no floating point |
| CK-CODE-C7 | N/A | |
| CK-CODE-D1, D2 | Yes | C5; one bounded `poll` |
| CK-CODE-D3, D4 | N/A, Yes | |
| CK-CODE-D5 | N/A | PWM interrupts not used |
| CK-CODE-D6 | Yes | |
| CK-CODE-D7 | No | package files within CS-18; `lib.rs` (INSP-096 finding-1) |
| CK-CODE-D8 | Yes | CS-36: `SLICE = (N >> 1) & 7`, slices 0 to 7 only; each output enabled by its own `CSR.EN` (`pwm.rs:145`); `release` clears the global `EN` alias once at construction (`pwm.rs:121`), a disable, not an enable |
| CK-CODE-D9 | Yes | decisions in `timing`, `cc_value`, `attach`'s claim check; target methods one call each |
| CK-CODE-E1 | No | finding-1 |
| CK-CODE-E2 | No | finding-1 (the 1 ms onset of REQ-SW-KEYER-033 is not met or analysed); `DEFAULT_HZ`, `MAX_PERIOD`, `MAX_DIV16` named and cited |
| CK-CODE-E3 | N/A | |
| CK-CODE-E4 | Yes | C7; attach order `CSR = 0`, `DIV`, `TOP`, `CC = 0`, `CTR = 0`, `CSR.EN`, then `FUNCSEL`, then pad `ISO`/`OD` clear (`pwm.rs:140-147`) as ADR-055 and ICD `01_overview.md` state |
| CK-CODE-E5 | Yes | a claimed slice is refused before any write (`pwm.rs:134-137`) |
| CK-CODE-E6 | Yes | the driver keeps the duty and on state and recomputes `CC` on each change; no read-back needed for a double-buffered write |
| CK-CODE-E7 to E9 | N/A, N/A, Yes | |
| CK-CODE-F1 to F3 | N/A | rustos code |
| CK-CODE-G1 | Yes | frequency and duty validated (`timing`, `Duty::from_permille`) |
| CK-CODE-G2 to G4 | N/A | |
| CK-CODE-G5 | Partial | as INSP-096 |
| CK-CODE-H1 | Yes | `attach`, `frequency_on`, `update_on` generic over `Regs` |
| CK-CODE-H2 | No | R5 |
| CK-CODE-H3 | Yes | `timing` refusal edges and the 0.1 % sweep; duty ends and rounding |
| CK-CODE-I1 | No | new items documented; crate-level `deny(missing_docs)` absent (pre-existing) |
| CK-CODE-I2 | Yes | |
| CK-CODE-I3 | No | finding-2 |
| CK-CODE-I4 | Yes | |
| CK-CODE-J1 to J4 | Yes | C1, C2 |

**PWM ICD (`docs/icd/rp2350/pwm/`):** register list, fields and the double-buffering description agree with section 12.5; no finding. **07 section 19 closing rule (WP-SW-03 row):** contract test drafted by the author, mock not written, dev-board report not filed, the keyer prototype image with PWM sidetone (plan WP-PDR-41 Outputs) not built; not closable at this commit.

## Findings

| Finding | Origin | Severity | Item | Location | Description | State | Deferred to |
|---|---|---|---|---|---|---|---|
| finding-1 | reviewer | Major | CK-CODE-E1, CK-CODE-E2 | ADR-055 lines 22, 23, 44; `pwm.rs:189-199`; `api/src/pwm/mod.rs:18-19` | onset and envelope against REQ-SW-KEYER-033 and HZ-005 K4 not analysed; onset can exceed 1 ms | Open | |
| finding-2 | reviewer | Minor | CK-CODE-I3 | `pwm/mod.rs:29`; SW-05 line 31 | `module_inception` under `-D warnings` | Open | |

### finding-1

**Major, CK-CODE-E1 and CK-CODE-E2.** ADR-055 section 1 names REQ-SW-KEYER-033 ("assert the sidetone gate within 1 ms of each key-down assertion") and HZ-005 (clicks) as constraining the decision (lines 22 and 23). HZ-005 K4, which lists REQ-SW-KEYER-033 among its control requirements, asks for "sidetone onset within 1 ms of key-down with a 3 to 5 ms envelope; no DC step at any transition" (C8). The chosen design switches the tone by writing `CC` (`update_on`, `pwm.rs:189-199`), and `CC` is double-buffered, so the change takes effect at the next counter wrap (PWM-4, `api/src/pwm/mod.rs:18-19`): the audible onset lags the call by up to one tone period, 1.43 ms at 700 Hz and 10 ms at the 100 Hz end of ADR-055 assumption 2, already above 1 ms for every tone below 1 kHz before any handler latency. ADR-055 does not analyse this latency, nor where the 3 to 5 ms envelope of K4 comes from: its "no partial pulse (HZ-005 clicks)" claim (line 44) addresses a partial pulse, not the step from silence to a full-amplitude square wave, which is the click K4's envelope exists to prevent. Whether the "gate" of REQ-SW-KEYER-033 is the keyer's command or the audible tone, the ADR must say which, and show the other half is allocated. **Fix:** in ADR-055, state the worst-case onset latency of `set_enabled(true)` and `set_duty` as a function of frequency; either force an early wrap on enable (for example `CTR` written to `TOP` so the new `CC` latches within one count) with the effect on clicks argued, or allocate the 1 ms onset and the 3 to 5 ms envelope to the SW-AUDIO design (a duty ramp over several periods through `set_duty`) and record that REQ-SW-KEYER-033's "gate" is the command; add the latency case to the contract or the dev-board check.

### finding-2

**Minor, CK-CODE-I3 (CS-21, CS-27).** `module_inception` at `pwm/mod.rs:29` fails `clippy -D warnings`; SW-05 line 31 reports the code clean apart from it. **Fix:** as INSP-095 finding-6.

## Measurements (SWE-089)

Lines reviewed: about 470 non-test Rust lines, 197 ICD lines, the 187-line contract draft and 18 developer tests; ADR-055 and SW-05 in full. Unsafe sites: 0. Findings: 1 Major, 1 Minor. Effort: 14 turns, 35 minutes.

## Record verdict

`reviewer_verdict: NEEDS CHANGES` on finding-1. Iteration 2 is a delta that verifies finding-1 (an ADR-055 revision and, if the design changes, the code). `verdict` stays `NEEDS CHANGES` until the software assurance record is filed APPROVED and the blobs reach a configuration cwht consumes.

## Iteration 2: delta verification of finding-1 (Major) (2026-09-27, cwht HEAD `5c16930`)

**Scope (rule C1).** Iteration 2 is a delta that verifies the finding-1 fix. Finding-2 (Minor) was not touched and is not re-reviewed. The same fix commit also carries the fix of INSP-105 finding-1 (the software assurance record's own Major: `release` asserts the PWM reset first); that finding belongs to INSP-105 and is verified by its iteration 2 delta, not here; its code was read only to check that it does not disturb the finding-1 fix. Product: rustos `cwht/wp-sw-03` at `48e07ec`, whose parent `9df9c57` merges `cwht/wp-sw-02` at `38434b2` into the iteration 1 head `6df18af`; the package delta is `git diff 9df9c57 48e07ec` (`api/src/pwm/mod.rs` 14, `docs/icd/rp2350/pwm/01_overview.md` 11, `pwm/pwm.rs` 46, `pwm/pwm_tests.rs` 68 changed lines), with ADR-055, SW-05 and the sprint index at cwht `e3ce2cb`. Checklist as at iteration 1.

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
| D9 | Datasheet and ICD: rustos `docs/icd/rp2350/pwm/02_registers.md` at `48e07ec` (`CHn_CTR` at `0x14n + 0x08`, RW, Table 1133) and the extract at `2ec64c0` (Table 1133 at line 81903); `pwm/mod.rs` `CTR = offset_of!(SliceRegs, ctr)` | the `CTR` write goes to the slice's own counter register |
| D10 | Requirement and hazard texts: `docs/requirements/sw/sw-keyer/requirements.md` REQ-SW-KEYER-033 (statement, verification note: HostUnit, "sidetone gate edge measured on the simulated clock"); `docs/vv/traceability-report.md` row REQ-SW-KEYER-033 (TC-SW-KEYER-039 Bench: "first sidetone PWM edge no later than 1.0 ms plus one PWM carrier period"); 07 section 14.2 `SW-AUDIO` rows (lines 593 and 635) | used for the gate and allocation cases below |

### Verification of finding-1, case by case (rule C7)

The fix request named five parts: the worst-case latency against frequency; either a forced early wrap with the click effect argued or an allocation of the onset and envelope to `SW-AUDIO`; the meaning of the REQ-SW-KEYER-033 gate; the allocation of the other half; and a latency case in the contract or the dev-board check.

| Case | At `48e07ec` and ADR-055 blob `c2c7cc9` | Result |
|---|---|---|
| Worst-case latency of each operation against frequency | ADR-055 section 2.1 table: on/off at the next counter step, at most `MAX_DIV16` 4095/16 = 255.9 `clk_sys` cycles = 1.71 µs at 150 MHz, any frequency; `set_duty` and `set_frequency_hz` at the next wrap, at most `1 / f` (10 ms at 100 Hz, 1.43 ms at 700 Hz). Checked: 700 Hz uses `DIV` 53/16 (3.3125 cycles, 22 ns; the host test's `DIV` 53); 100 Hz needs a period of 1.5 M cycles in `TOP <= 65534`, so `DIV` at least 22.9, 153 ns per count as tabled | Verified |
| Forced early wrap | `update_on` (`pwm.rs:207-227`) writes `CC`, then, only when on/off changes (`switched = on != self.on`), `CTR = period - 1` = `TOP` of this slice; the counter wraps at its next count and latches the double-buffered `CC` (section 12.5.2.3, ICD `01_overview.md` new item 5). `period >= MIN_PERIOD` = 2 keeps `period - 1` from underflowing (comment at the site). One output per slice (ADR-055 option A), so resetting `CTR` touches no other output | Verified |
| Click effect argued | section 2.1 "Effect of the forced wrap on clicks": switch-on from `CC = 0` only shortens a low interval; switch-off can cut one high interval short, then low; a natural wrap between the two writes gives at most one high pulse of one count (at most 1.71 µs) at switch-on; no DC step is introduced, and the silence-to-tone step is the same with or without the forced wrap. I checked the case table against trailing-edge mode (output high while the counter is below `CC`): at `CTR = TOP` the output is low for any old `CC <= TOP`, so the forced wrap itself creates no edge except at 100 % duty, where the level is already high and stays high until the new `CC` latches | Verified |
| Meaning of the REQ-SW-KEYER-033 gate | section 2.1: the gate is the keyer's command to the sidetone path (the `SW-KEYER` output), not the audible tone; this matches the requirement's HostUnit verification note ("sidetone gate edge measured on the simulated clock", D10). The driver's share, call to first PWM edge, is at most 1.71 µs | Verified |
| Allocation of the rest of K4 (3 to 5 ms envelope, no DC step) and the K5 mid-scale idle | section 2.1 allocates them to `SW-AUDIO` (07 section 14.2: "start-up and mode-change ramps", "sidetone amplitude limit", "fault mute", D10), decided with the audio path by TS-010 and written as `SW-AUDIO` requirements by WP-PDR-35, marked AT RISK on TS-010 (rule C8); section 3 option A and the hazard-analysis bullet of section 4.3 say the driver does not provide them | Verified |
| Latency case in the contract or the dev-board check | PWM-4 of `api::pwm` states a switching latency; the dev-board check (section 4.3) adds a GPIO marker and a 1 MS/s capture at 100 Hz, 700 Hz and 3 kHz, each switching within 5 µs over 100 switchings; the host tests `on_off_writes_cc_in_the_right_half_then_forces_a_wrap` and `duty_change_while_on_or_off_writes_only_cc` fix the register writes; a revisit condition is added if the dev board shows the latch later than 5 µs | Verified |

The INSP-105 finding-1 change (`release` writes `RESETS.RESET` bit 16 through `ALIAS_SET` before the clear, `pwm.rs:125-126`, with two host tests) runs once in `Rp2350Pwm::new`, before any output exists, and does not touch `update_on`; it does not affect the finding-1 fix.

Cross items the author reports and I confirm (no finding here): TC-SW-KEYER-039 adds "one PWM carrier period" to its tolerance, but this design has no carrier and the added term is one counter step (to the WP-PDR-35 test-case writer); the `SW-AUDIO` allocation is AT RISK until TS-010 selects the audio path and WP-PDR-35 writes the requirements, and should be checked by the reviewers of those products.

### Checklist items re-answered for the fix

| Id | Iteration 2 answer | Evidence |
|---|---|---|
| CK-CODE-E1 | Yes | PWM-4 and ADR-055 section 2.1 state the switching latency the driver implements; the gate and allocation are written down |
| CK-CODE-E2 | Yes | every latency is stated with its unit and frequency, and the 1.71 µs bound is derived from `MAX_DIV16` and `clk_sys` |
| CK-CODE-C4 on the new site | Yes | `self.period - 1` carries its bound comment (`MIN_PERIOD` = 2) |
| CK-CODE-H3 | Yes | both sides of `switched` tested (on/off change writes `CTR`; duty change while on or off does not) |

### Findings (current state at iteration 2)

| Finding | Origin | Severity | Item | Location | Description | State | Deferred to |
|---|---|---|---|---|---|---|---|
| finding-1 | reviewer | Major | CK-CODE-E1, CK-CODE-E2 | ADR-055 section 2.1; `pwm.rs:207-227`; `api/src/pwm/mod.rs:18-22` | onset and envelope against REQ-SW-KEYER-033 and HZ-005 K4 not analysed; onset could exceed 1 ms | Verified (`48e07ec`, ADR-055 `c2c7cc9`) | |
| finding-2 | reviewer | Minor | CK-CODE-I3 | `pwm/mod.rs:29`; SW-05 line 31 | `module_inception` under `-D warnings` | Open (lien, rule C1) | CDR readiness declaration |

No new finding.

### Measurements (SWE-089), iteration 2

Lines reviewed: the 139 changed lines of `9df9c57..48e07ec` and the 62 changed lines of ADR-055 and SW-05, with the REQ-SW-KEYER-033 text, its two closing cases and the 07 `SW-AUDIO` rows. Unsafe sites: none. Findings: 0 new. Effort of this iteration: about 18 turns and 35 minutes (front matter totals include iteration 1).

### Record verdict, iteration 2

`reviewer_verdict: APPROVED`: finding-1 is Verified and no Major is open. Minor finding-2 becomes a lien under rule C1 (owner the firmware developer, due at the CDR readiness declaration). `verdict` stays `NEEDS CHANGES` until the paired software assurance record INSP-105 files its iteration 2 delta APPROVED (it holds its own Major, finding-1, whose fix is in the same commit), readiness R3 and R5 hold, and the owner's merge with the PCR-4 pin-move CR brings `48e07ec` into a configuration cwht consumes.
