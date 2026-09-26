---
# Peer-review record front matter (charter section 5; docs/process/07-software-engineering-plan.md
# section 10.2). To review a file, copy this whole file to
# docs/reviews/<REVIEW>/checklists/<product-slug>.md: that copy is the single peer-review record
# (there is no peer-reviews/ folder). Fill every field below, answer every checklist item and
# fill the findings table. Both front-matter parsers (PyYAML and the subset parser of
# tools/validate_docs.py) strip a comment on its own line and a comment written after a value
# (" # ..."); this template keeps each comment on its own line for readability, and comment lines
# may stay or be deleted when filing. tools/validate_docs.py checks the record against the field
# list of docs/process/01-lifecycle-and-reviews.md section 13 (its PEER_REVIEW_RECORD_SCHEMA) and
# fails while the id, checklist_file, product_commit or date placeholder is left in place.
# Search first: 'grep' in an evidence column means: run mcp__claude-context__search_code on
# /Users/robinonsay/rust/cwht first (charter section 11 rule 1), then grep -n only to pin the hit.
#
# id: next free INSP-NNN (never reused, charter section 6)
id: INSP-NNN
checklist: peer-review-checklist-code
checklist_revision: B
# checklist_file: this record's own path
checklist_file: docs/reviews/<REVIEW>/checklists/<product-slug>.md
# product: exact path of the one file under review (SWE-087 d)
product: firmware/cwht-core/src/txseq/guard.rs
# product_commit: quoted so that an all-digit hash stays a string
product_commit: "<commit>"
# product_size: lines of code
product_size: 212 LOC
sprint: SW-NN-<module>
author_agent: <invocation id>
# reviewer_agent: never the author
reviewer_agent: <invocation id>
# criticality: safety-critical | mission-critical | neither (plan section 14.1)
criticality: safety-critical
# assurance_required: true | false, from the table of plan section 2.1.1 (true for any file with unsafe)
assurance_required: true
# assurance_reviewer_agent: invocation id, or none when assurance_required is false
assurance_reviewer_agent: <invocation id>
# iteration: 1 to 3
iteration: 1
readiness_met: true
# reviewer_verdict: APPROVED | NEEDS CHANGES (the file reviewer)
reviewer_verdict: NEEDS CHANGES
# assurance_verdict: APPROVED | NEEDS CHANGES | not-required
assurance_verdict: NEEDS CHANGES
# verdict: set by the software lead; APPROVED only when reviewer_verdict is APPROVED and
# assurance_verdict is APPROVED or not-required
verdict: NEEDS CHANGES
findings_major: 0
findings_minor: 0
findings_open: 0
findings_fixed: 0
findings_verified: 0
findings_deferred: 0
assurance_findings_major: 0
assurance_findings_minor: 0
# assurance_tasks_applied: SWEHB section 7.1 tasks applied, for example [swe-134 7.1 task 2]
assurance_tasks_applied: []
# unsafe_sites_reviewed: number of unsafe blocks and unsafe fns reviewed in this file
unsafe_sites_reviewed: 0
# deferred_rids: RID-<REVIEW>-NNN entered for each Deferred finding at record closure
deferred_rids: []
# items_no: checklist ids answered No
items_no: []
effort_turns: 0
effort_minutes: 0
# record_status: Open | Closed (set by the software lead, plan section 10.2)
record_status: Open
date: 2026-MM-DD
date_closed: null
---

# Peer review checklist: Rust code

**Product types:** any file under `firmware/` (`cwht-app`, `cwht-core`, `cwht-hal-mock`, `devcheck`, and any Rust code of the emulation harness under `firmware/emu/`) and the rustos crates as changed for cwht (`rustos/api`, `rustos/firmware/pico2`). One file per review (SWE-087 d). **Governing:** `docs/process/07-software-engineering-plan.md` section 7 (coding standard CS-01 to CS-38), section 8 (static analysis), section 14 (safety), section 16 (cybersecurity), section 2.1.1 (when the software assurance review is required); ADR-011 (target platform rules); NPR 7150.2D SWE-060, SWE-061, SWE-135, SWE-185, SWE-207, SWE-134, SWE-220, SWE-052; charter sections 8, 10, 11. **Used by:** an independent reviewer agent that did not author the file; a second, software assurance reviewer where the table of plan section 2.1.1 says Yes. The assurance reviewer applies SWEHB topics `6-9` (generic programming practices checklist) and `6-10` (general good programming practices checklist) and the `# 7. Software Assurance` section of `docs/references/md/swehb/swe-060-*.md`, `swe-061-*.md`, `swe-134-*.md` (section 7.1 task 2: source code satisfies items a to l) and `swe-135-*.md`, writes its verdict and findings into this record and lists the tasks applied in `assurance_tasks_applied`.

Answer every item Yes, No or N/A with `file:line` evidence. **Major**: a deviation from the design or requirement, a panic path, an `unsafe` site without a valid SAFETY argument, a missing or wrong traceability tag, a security rule broken, a complexity or bound violation, a target platform rule broken, a safety provision weakened. **Minor**: naming, documentation wording, non-blocking style. Findings cite the `CS-NN` rule where one applies.

## Record

This file, copied to `docs/reviews/<REVIEW>/checklists/<product-slug>.md`, is the single peer-review record for the reviewed file (charter section 5; plan section 10.2). Slug: `code-<module>-<unit>` (for example `code-keyer-iambic`), `code-pico2-<periph>` for a rustos driver file. `<REVIEW>` is the next gate the product feeds. The front matter above is the first thing in the file, unfenced.

### Findings (filled by the reviewer and the assurance reviewer)

| Finding | Origin | Severity | Item | Location | Description | State | Deferred to |
|---|---|---|---|---|---|---|---|
| F-01 | reviewer or assurance | Major or Minor | CK-CODE-xx | `file:line` | what is wrong, the CS-NN rule, and what would fix it | Open, Fixed, Verified or Deferred | `RID-<REVIEW>-NNN` and the owner decision reference, for Deferred only |

## Readiness criteria (all true; the software lead confirms before dispatching the reviewer)

| # | Criterion | Evidence |
|---|---|---|
| R1 | Gate G1 passes on the crate: `cargo fmt --check`, `cargo clippy --all-targets -- -D warnings` for host, and for `thumbv8m.main-none-eabihf` when the crate is in the image | gate log |
| R2 | The file is at most 500 lines; functions at most 60 lines (CS-18) | `wc -l`, clippy `too_many_lines` |
| R3 | The design unit the file implements is `Active` (CDR design or approved CR) and is named in the `// @design` header tag | design section |
| R4 | `tools/traceability.py` finds a `// @req` tag for every requirement the brief assigned to the file | tool output |
| R5 | The test author's file for this module exists (or its sprint is running in parallel) so the reviewer can check testability claims | test file path |
| R6 | For `pico2` or `api`: `tools/unsafe_audit.py --check` passes (every `unsafe` has a SAFETY comment) | tool output |

## Participants

Author agent (absent); reviewer agent; software assurance reviewer where the table of plan section 2.1.1 says Yes (for this checklist: files of the safety-critical and mission-critical components and units of plan section 14.1, and every file that contains `unsafe`); owner for deferrals.

## A. Environment, dependencies and build (CS-01 to CS-04)

| Id | Check | Evidence |
|---|---|---|
| CK-CODE-A1 | Image crate files begin with `#![no_std]` (and `#![no_main]` for `cwht-app`); no `extern crate alloc`, no `std::`, no `Box`, `Vec`, `String`, `format!` | file header, grep |
| CK-CODE-A2 | No new dependency in `Cargo.toml`; if a dev-dependency was added it is in the third-party register (plan section 17.1) | manifest diff |
| CK-CODE-A3 | No `#[cfg]` that changes flight behavior between test and release except `cfg(test)` on test modules; no `debug_assert!` relied on for safety | grep `cfg` |

## B. Unsafe code (CS-05 to CS-10)

| Id | Check | Evidence |
|---|---|---|
| CK-CODE-B1 | Crates other than `pico2` and `api` have `#![forbid(unsafe_code)]` and the file contains no `unsafe` | header, grep |
| CK-CODE-B2 | Each `unsafe` block or `unsafe fn` in `pico2` or `api` has a `// SAFETY:` comment immediately above stating the invariant, why it holds here, and for MMIO the datasheet section and page; the reviewer judges the argument valid (aliasing, alignment, validity, volatile access, ownership handle consumed) | each site |
| CK-CODE-B3 | `unsafe fn` bodies use explicit inner `unsafe {}` blocks (`unsafe_op_in_unsafe_fn` deny) and are as small as possible; safe wrappers are the public surface | sites |
| CK-CODE-B4 | MMIO goes through `read_volatile` and `write_volatile` on `#[repr(C)]` register structs addressed from `RegAddr`; atomic alias offsets are used for fields shared across contexts (CS-08) | register code |
| CK-CODE-B5 | No `static mut`; shared state uses atomics with the ordering justified in a comment, or the `pico2` critical-section cell (CS-09) | grep |
| CK-CODE-B6 | No `transmute`, `zeroed`, `uninitialized`, `unreachable_unchecked`, `*_unchecked` slice methods, `union`, inline `asm!` outside boot code (CS-10) | grep, clippy disallowed lists |
| CK-CODE-B7 | The unsafe audit list `firmware/unsafe-audit.md` has an entry for every site in the file and the entry text equals the SAFETY comment; the reviewer signs each entry with the `INSP-NNN` id of this record | audit file |
| CK-CODE-B8 | Once-per-boot constructors consume a `DeviceHandle` or `PinHandle` (rustos pattern); no path re-creates a handle in safe code | constructors |

## C. Panics, errors and arithmetic (CS-11 to CS-16)

| Id | Check | Evidence |
|---|---|---|
| CK-CODE-C1 | No `unwrap`, `expect`, `panic!`, `unreachable!`, `todo!`, `unimplemented!`, direct indexing `a[i]` or slicing `a[i..j]`, `process::exit`; the only board `take()` `None` arm calls `safe_state_halt()` (CS-11) | grep, clippy |
| CK-CODE-C2 | Every fallible function returns `Result<T, E>` with a module-specific `enum E` (no `u32` codes, no `&str`); infallible operations use `Infallible`; every `Result` and `Option` is handled or propagated; no `let _ =` on a `Result` (CS-13) | signatures, grep |
| CK-CODE-C3 | Each error variant maps to a response class from the design error table (retry bounded, degrade, safe state, reset); the mapping is visible in the code (match on the variant), not a generic catch-all | error handling sites |
| CK-CODE-C4 | Arithmetic is `checked_`, `saturating_` or `wrapping_` with a comment on the choice; timer arithmetic uses `wrapping_sub` on the 64-bit tick with the wrap argument stated (CS-14) | arithmetic sites |
| CK-CODE-C5 | No `as` numeric casts; `From` and `TryFrom` with an error arm on truncation (CS-15) | grep `as ` |
| CK-CODE-C6 | Files of safety-critical components and units contain no `f32`/`f64`; fixed-point scaling is documented with the scale constant and range (CS-16) | grep |
| CK-CODE-C7 | The panic handler (if in this file) writes safe-state registers directly, records the marker, requests a watchdog reset, and calls nothing fallible (CS-12) | panic handler |

## D. Structure, complexity and target platform rules (CS-17 to CS-23, CS-34 to CS-38)

| Id | Check | Evidence |
|---|---|---|
| CK-CODE-D1 | Every function has cyclomatic complexity at most 15 per `rust-code-analysis-cli` (gate G5 output attached to the review), and safety-critical decisions have at most 4 conditions | G5 output |
| CK-CODE-D2 | No recursion; every loop is over a finite range or slice or has a compile-time bound; the only `loop {}` are the main loop and halt loops (CS-19) | grep `loop`, `while` |
| CK-CODE-D3 | `match` on enums is exhaustive without `_ =>` in `cwht-core`; state machines are one `match (state, event)` that matches the design transition table cell by cell (CS-20) | match sites versus design table |
| CK-CODE-D4 | No shadowing; every `#[allow]` or `#[expect]` has the `// CS-NN waiver: <reason> (INSP-NNN)` comment and the reason is acceptable (CS-21) | grep `allow`, `expect` |
| CK-CODE-D5 | Interrupt handlers only read cause, timestamp, sample SIO inputs (ALARM1 handler), enqueue or set a flag, re-arm and acknowledge; no data loops, no safety-critical output writes except the safe-state path; a GPIO duration marker exists where the design names one (CS-22) | handler bodies |
| CK-CODE-D6 | Single-core assumptions hold: nothing starts core 1 (CS-23) | grep |
| CK-CODE-D7 | Nesting depth at most 4; functions at most 60 lines; file at most 500 lines (CS-18) | inspection |
| CK-CODE-D8 | Target platform rules of ADR-011: no NVIC priority register write and no nested interrupt (CS-34); GPIO only through SIO registers, no GPIO coprocessor instructions and no IO_BANK0 edge-interrupt enable (CS-35); PWM slices 0 to 7 only, each with its own enable (CS-36); TICKS enabled before TIMER0 or watchdog use and every XOSC or PLL wait bounded with a fault return (CS-37) | grep for NVIC, IO_BANK0 interrupt, PWM slice and TICKS accesses |
| CK-CODE-D9 | Target-only code (`cwht-app`, `pico2` MMIO, boot and vector table, files tagged `// @target-only`) is straight-line except the board `take()` match; every decision of a safety-critical driver is in a host-compilable function (CS-38) | G5 complexity output, function bodies |

## E. Correctness against design and requirements (SWE-060, SWE-058)

| Id | Check | Evidence |
|---|---|---|
| CK-CODE-E1 | The file implements exactly the design unit named in `// @design`, with the public signatures of the design (names, types, error enum); every difference is a finding (design defect or code defect) | design section |
| CK-CODE-E2 | Timing constants equal the requirement values with units in the identifier (`dot_len_us`, `debounce_make_us`, `debounce_open_us`, `watchdog_ms`) and cite the requirement in a comment; no magic numbers | constants |
| CK-CODE-E3 | Keyer logic (if in scope) matches the design tables for straight key, iambic A and B, dit and dah memory, squeeze, weighting and speed range (SI-018) | keyer file versus design |
| CK-CODE-E4 | Register writes match the datasheet: field positions, reset sequence, read-back where the design requires it; the doc comment cites section and page (CS-25) | register code versus ICD |
| CK-CODE-E5 | Guard conditions and prerequisite checks exist exactly as the design specifies (SWE-134 e, h); a missing prerequisite is Major | guard functions |
| CK-CODE-E6 | Output read-back and input validation exist as designed (SWE-134 g; CS-29) | I/O code |
| CK-CODE-E7 | Safe-state path: `safe_state()` in this file (if present) is infallible, loop-free over data, writes `PA_EN` low, `TR_TX` low, keyer idle, charge inhibit asserted, audio muted, in that order (SWE-134 c, l; plan section 14.2) | function body |
| CK-CODE-E8 | Complement-stored flags and CRC checks are implemented and checked where the design says (SWE-134 f; CS-32) | integrity code |
| CK-CODE-E9 | No dead code: every function is reachable from a requirement-tagged path or is a test helper; unused items are removed, not `#[allow(dead_code)]` | grep |

## F. Traceability tags (CS-24; SWE-052)

| Id | Check | Evidence |
|---|---|---|
| CK-CODE-F1 | `// @design <module>/<unit>` header present and correct | header |
| CK-CODE-F2 | Every function implementing a requirement has `// @req REQ-SW-<SUB>-NNN` on the line above; the ids exist and belong to this module; every requirement in the brief appears at least once | grep, brief |
| CK-CODE-F3 | Functions that implement no requirement are infrastructure justified in the design (CK-DES-B1) | design |

## G. Secure coding (CS-29 to CS-33; SWE-207, SWE-185)

| Id | Check | Evidence |
|---|---|---|
| CK-CODE-G1 | Every external input is validated at the boundary (debounce, rate, range, length, CRC) before use | input paths |
| CK-CODE-G2 | The key line affects only the keyer state machine; no menu or configuration logic reads it (CS-30) | grep for key input uses |
| CK-CODE-G3 | Fixed-size buffers with named capacity constants; copies bounded by `min` of lengths (CS-31) | buffers |
| CK-CODE-G4 | Diagnostic interface handlers cannot change state other than `reboot` (CS-33); no personal data is written to the event log or configuration (plan section 16.6) | handler, log writes |
| CK-CODE-G5 | Gate G5 static analysis output (`cargo audit`, `cargo deny check`, `cargo geiger --forbid-only`, `tools/unsafe_audit.py --check`, `rust-code-analysis-cli` with `tools/complexity_gate.py`, and the nightly Miri run `cargo +nightly-2026-08-24 miri test` for `api` and `pico2`, plan section 8.4) is attached to the review and shows zero findings for this crate; clippy is gate G1 and is covered by readiness R1 and CK-CODE-I3 | G5 log |

## H. Tests and testability (SWE-062)

| Id | Check | Evidence |
|---|---|---|
| CK-CODE-H1 | The unit is exercisable through `api` traits with the mock clock; no hidden dependency on real time or hardware (a hard-coded `RegAddr` read in `cwht-core` is Major) | dependencies |
| CK-CODE-H2 | The independent test author's tests for this file exist and pass (G3), and the test file was not written by this file's author | sprint record |
| CK-CODE-H3 | For safety-critical files: each decision in the design's decision table has its MC/DC test functions (`// @mcdc` tags) in the test file, and the decision has at most 4 conditions with no nested boolean expression hidden in a helper that the table does not list | test file, decision table |

## I. Documentation and style (CS-25 to CS-28)

| Id | Check | Evidence |
|---|---|---|
| CK-CODE-I1 | Every `pub` item has a doc comment stating purpose, units, ranges, errors and (for registers) the datasheet citation; `#![deny(missing_docs)]` present | docs |
| CK-CODE-I2 | Names follow CS-28 with units in identifiers; register and field names match the datasheet | identifiers |
| CK-CODE-I3 | `cargo fmt --check` and gate G1 clippy clean (R1) | gate |
| CK-CODE-I4 | Comments explain why, not what; no commented-out code | text |

## J. Common review traps (from rustos lessons learned; check explicitly)

| Id | Check | Evidence |
|---|---|---|
| CK-CODE-J1 | Every `api` or `pico2` symbol used exists with that exact name and signature in the current tree (`cargo doc`); no fabricated API names | `cargo check` on both targets, doc |
| CK-CODE-J2 | Trait methods are called as the trait defines them (`read`, `write`, `output_from_handle`), not invented free functions | call sites |
| CK-CODE-J3 | Compound requirements ("X and Y") are implemented atomically as the requirement states, not as two independent partial paths | logic |
| CK-CODE-J4 | The file's line count and function lengths were measured, not estimated | `wc -l`, clippy |

## Completion criteria (SWE-088)

`verdict: APPROVED` when readiness R1 to R6 held, every item answered with evidence, zero open Major findings, Minor findings fixed or deferred with an owner decision reference and a gate, every `unsafe` entry in the audit list signed, the assurance reviewer returned `APPROVED` where plan section 2.1.1 says Yes, the measurements (lines reviewed, turns, minutes, findings by severity, unsafe sites reviewed) are in the front matter, and `.venv/bin/python tools/validate_docs.py` passes on the record itself. On record closure every Deferred finding becomes `RID-<REVIEW>-NNN` in the log of its named gate and is listed in `deferred_rids` (plan section 10.2).

## Verdict format

```
VERDICT: APPROVED | NEEDS CHANGES
FINDINGS:
- [Major] CK-CODE-C1 firmware/cwht-core/src/txseq/guard.rs:88: `prereqs[idx]` indexing (CS-11); use `get`.
- [Major] CK-CODE-E5 firmware/cwht-core/src/txseq/guard.rs:41: TX time-out prerequisite missing versus software-design.md section 6.3.
- [Minor] CK-CODE-I2 firmware/cwht-core/src/txseq/guard.rs:12: `settle` lacks unit; rename `settle_us`.
ITEMS N/A: CK-CODE-B2 to CK-CODE-B8 (crate forbids unsafe)
MEASUREMENTS: size=212 LOC; turns=3; minutes=18; major=2; minor=1; unsafe_sites=0
```
