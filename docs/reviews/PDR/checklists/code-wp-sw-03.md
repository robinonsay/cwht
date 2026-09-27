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
product_commit: "6df18afc4c98f278c93aafc2a2ca345333b69640"
product_files: ["docs/decisions/adr/ADR-055-wp-sw-03-pwm-output.md@7b2a9d920d57d0a03e4b995de811cad0e68215c3", "docs/sprints/SW-05-wp-sw-03-pwm.md@975d9268b5b455d7436b919e67fe02d948014764", "docs/sprints/index.md@fb217bcb6ff684b8117f104970a4e091a4899b1c", "rustos:api/src/pwm/mod.rs@1c13d0ad73ffb972a59399d9b93ce11b1b7d406f", "rustos:api/tests/pwm_contract.rs@7df5fdd237aefba2b13ec72d62945ba38092146b", "rustos:api/src/lib.rs@5e79e2b739469c8c077c9a637814977e956e88a5", "rustos:firmware/pico2/src/pwm/mod.rs@9c8ed4c4ba7c2b279cd736c518897206b40689f4", "rustos:firmware/pico2/src/pwm/pwm.rs@75bca4e87fe68c4f61906e27b18b0d43cc07fb9f", "rustos:firmware/pico2/src/pwm/pwm_tests.rs@c3286c6d9db9bb776f1d8c2e79107eff1755e60e", "rustos:firmware/pico2/src/pwm/tests.rs@c0a59856277c6e45e70dab78f3b6fe058ac4da2b", "rustos:firmware/pico2/src/common/board.rs@eeb8407e77a93718c7e0a2cb320fa2ec6b25f4cc", "rustos:firmware/pico2/src/common/reg.rs@ec94f2cdee391615d8fd88b0650a3f830bc2ef80", "rustos:firmware/pico2/src/lib.rs@5122df422db03e15da04aa9cc784d4b96d437ec0", "rustos:docs/icd/rp2350/pwm/index.md@17e8dabbc10f7a54ce6e50cb0cd50d97378af8f7", "rustos:docs/icd/rp2350/pwm/01_overview.md@346e561de8e7aea729ffb4e6274d0778d327634b", "rustos:docs/icd/rp2350/pwm/02_registers.md@7f93b2004a0d0065bec0342e5f7a0bc28acb5a7a", "rustos:docs/icd/rp2350/index.md@426a75dfd588af945bba6b5533da819b93d18a75"]
product_size: 1101 lines added in 6df18af, of which about 470 non-test Rust lines (pwm/mod.rs 165 before its test module, pwm.rs 226, api pwm 80) and 197 ICD lines; ADR-055 90 lines; SW-05 61 lines
sprint: SW-05-wp-sw-03-pwm
author_agent: "author:WP-PDR-41 wave 1a (Claude, firmware developer role)"
reviewer_agent: "reviewer:WP-PDR-41-code (independent code reviewer, iteration 1; authored no part of WP-PDR-41)"
# criticality: 07 section 14.1 drivers row (PWM for sidetone and audio level), inherited from SW-AUDIO and SW-KEYER (HZ-005)
criticality: safety-critical
assurance_required: true
assurance_reviewer_agent: "pending: separate software assurance invocation, record docs/reviews/PDR/checklists/code-wp-sw-03-software-assurance.md (plan WP-PDR-41 Records; 07 section 2.1.1 Code row)"
iteration: 1
readiness_met: false
reviewer_verdict: NEEDS CHANGES
assurance_verdict: pending
verdict: NEEDS CHANGES
findings_major: 1
findings_minor: 1
findings_open: 2
findings_fixed: 0
findings_verified: 0
findings_deferred: 0
assurance_findings_major: 0
assurance_findings_minor: 0
assurance_tasks_applied: []
unsafe_sites_reviewed: 0
deferred_rids: []
items_no: [CK-CODE-D7, CK-CODE-E1, CK-CODE-E2, CK-CODE-H2, CK-CODE-I1, CK-CODE-I3]
effort_turns: 14
effort_minutes: 35
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
