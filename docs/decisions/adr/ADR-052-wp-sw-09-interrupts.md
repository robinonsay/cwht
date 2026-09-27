# ADR-052: WP-SW-09 interrupts in rustos: overridable IRQ vectors, a one-priority NVIC trait, and a critical-section cell for state shared with handlers

| Field | Value |
|---|---|
| ID | ADR-052 |
| Status | Proposed (for the owner's review and merge of rustos branch `cwht/wp-sw-09` as rustos maintainer, OD-23; FW-B1) |
| Date proposed | 2026-09-27 (revision 2 of 2026-09-27: INSP-096 finding-1 fixed, section 8) |
| Date decided | not decided |
| Decision class | 1 by 06 section 14.1 item (c) (the interrupt plumbing and critical section are drivers of the 07 section 14.1 components, and CS-34 is a safety design rule); a work-package design within TS-002 alternative A0, as ADR-027 requires (the ADR-051 "Decision class" row and its section 7 question apply equally) |
| Decision authority | Robin (safety-critical scope; rustos change merged by the owner as maintainer, ADR-019) |
| Author | Claude (WP-PDR-41 author invocation, firmware developer role, 2026-09-27) |
| Independent reviewer | Pending: `docs/reviews/PDR/checklists/adr-052-wp-sw-09-interrupts.md` (design checklist sections A, B, H) with its software assurance pair; code in `code-wp-sw-09.md` and `code-wp-sw-09-software-assurance.md` |
| Life-cycle phase | B |
| Baseline affected | none now; the rustos pin moves at merge by a Class I CR (PCR-4) |
| Change request | none for this ADR |

## 1. Context

rustos `pico2` builds its 68-entry vector table as a constant in which every device interrupt points at `DefaultHandler`: an application cannot install a handler, there is no NVIC enable code and no critical-section primitive (`docs/research/rustos-toolchain-proof.md` F8 item 1, High). cwht's execution model needs two alarm handlers (keyer element timing on ALARM0, the 1 kHz sampling and scheduler tick on ALARM1; 07 section 5 item 1), all at one NVIC priority (REQ-SYS-129; CS-34), with state shared between those handlers and thread code without `static mut` (CS-09). 07 section 19 makes this work package WP-SW-09; every interrupt-using driver depends on it.

- Driving inputs and expectations: SI-007, SI-026, SI-033
- Requirements that constrain the decision: REQ-SYS-129 (every firmware interrupt handler at one NVIC priority level), REQ-SYS-128 (host-testable layering), REQ-SW-KEYER-019 (1 ms sampling from a timer handler)
- Hazards in play: as ADR-051 (the drivers row of 07 section 14.1): HZ-004 most directly, since a handler that preempts another or a lost update of shared keyer state can delay key-up
- Research consulted: `docs/research/rustos-toolchain-proof.md` F8 item 1 (the `PROVIDE` pattern and NVIC register addresses), "Peripheral to driver map" Interrupt plumbing row; `docs/research/emulator-accreditation-and-timer-irq.md` (the emulators characterized for ADR-011 do not model NVIC priorities, 07 CS-34); RP2350 datasheet sections 3.2 (Table 94, p82 and p83), 3.7.4.5 (PRIMASK, p134), 3.7.5 (Tables 192 to 195, p179)
- Guidance consulted: SWE-134 items a, c, k (NPR 7150.2D section 3.7.3); SWE-219, SWE-220
- Assumptions the decision rests on, and how and by when each is confirmed:
  1. Only core 0 runs rustos code; core 1 stays in its bootrom wait state (CS-23). The critical section masks interrupts on the running core only, so this is what makes `CsCell` sound. Confirmed by the firmware architecture ADR (WP-PDR-32, single-core rule) and by Inspection that no code launches core 1.
  2. `PROVIDE(<IRQ> = DefaultHandler)` in `link.ld` is overridden by a strong definition in the application with the linker rustc uses for `thumbv8m.main-none-eabihf` (`rust-lld`). Confirmed by the author's link test of section 4.3 (vector table slot 62 took the application handler, the others `DefaultHandler`).

## 2. Decision

rustos gains, on branch `cwht/wp-sw-09` at commit `c6e5100` (revision 2; revision 1 was `9305f59`), on `cwht/wp-sw-11` (merged at `4a8e825` by `8b67385`):

1. **Overridable vectors.** `link.ld` provides each of the 52 RP2350 device-interrupt symbols of Table 94 (`TIMER0_IRQ_0` to `SPAREIRQ_IRQ_5`) as `PROVIDE(<name> = DefaultHandler)`, and `VECTOR_TABLE` slots 16 to 67 point at those symbols. The 52 slot entries, the extern block that declares the symbols and the `Vector` word type live in `pico2::irq::vectors` (target builds only); `VECTOR_TABLE` stays in `lib.rs` with the core exceptions 0 to 15 and its link section, and fills slots 16 to 67 through the `const fn` `irq::with_device_interrupts`, so the table is still computed at compile time with the same contents. `lib.rs` does not grow: it is 564 lines after this package against 588 before it, its two new module lines included (CS-18; INSP-096 finding-1). `pico2::interrupt!(LINE, handler)` defines one handler: it checks at compile time that `LINE` is a variant of `pico2::irq::Irq` and that `handler` has type `fn()`, then defines the unmangled `extern "C" fn LINE()` that calls it.
2. **`api::irq::InterruptController`**, a portable trait with `enable`, `disable`, `is_enabled`, `pend`, `unpend` and `is_pending` for a numbered line, and **no priority operation**. Its contract, clauses IRQ-1 to IRQ-6 in the module documentation, is checked by `api/tests/irq_contract.rs` against a reference model, and three faulty models show that each check detects its clause.
3. **`pico2::irq::Rp2350Nvic`** (board device `nvic`) implements it with one write to `NVIC_ISER`, `NVIC_ICER`, `NVIC_ISPR` or `NVIC_ICPR`, or one read, per call; line numbers above 51 are rejected before any access. No `NVIC_IPR` register is written anywhere in `pico2`, so every enabled line keeps priority 0 and no handler preempts another (REQ-SYS-129).
4. **`pico2::critical_section`**: `with(f)` reads `PRIMASK`, masks with `cpsid i`, runs `f` with a `CriticalSection` token, and writes back the exact `PRIMASK` value it read, so nested sections stay masked. `CsCell<T>` is a `static`-friendly cell reachable only through a token: `replace` moves a value in and out, `with_mut` lends `&mut T` for a closure, and a borrow flag turns a nested access to the same cell into `Err(Busy)` instead of a second `&mut`. This module is the only place in `pico2` that masks interrupts (CS-09).

## 3. Alternatives considered

| Option | Description | Why not chosen (or why chosen) |
|---|---|---|
| A (chosen) | `PROVIDE` defaults with a checked `interrupt!` macro; trait without priorities; PRIMASK save and restore; `CsCell` with move-in/move-out and a borrow flag | Stable Rust, no dependency, matches the `cortex-m-rt` convention the research names; the one-priority rule is enforced by the absence of any priority path |
| B | A run-time handler table (`static` array of function pointers set by the application) | Needs a mutable static read in every handler entry and an indirection; registration order becomes a run-time property that host tests cannot see |
| C | `critical-section` crate or `cortex-m` crate primitives | CS-02: zero external runtime crates in the image |
| D | `CsCell` returning `&mut T` without a borrow flag (the `cortex-m` `Mutex<RefCell>` pattern without `RefCell`) | Unsound under nested critical sections: two `with_mut` of one cell would alias `&mut` |
| E | Do nothing | No alarm handler can run; the keyer and the 1 kHz sampling of 07 section 5 cannot be built |

## 4. Consequences

### 4.1 Requirements created or changed

| Requirement | Relationship | Note |
|---|---|---|
| none | | REQ-SYS-129 is met by construction here; the L2 `REQ-SW` row for the one-priority rule (07 section 4 item 7) is written in WP-PDR-35 and may cite this ADR |

### 4.2 Interfaces, design and code

- ICDs affected: none.
- Design elements: rustos `api/src/irq/mod.rs` (new), `api/src/lib.rs` (module list), `api/tests/irq_contract.rs` (new); `firmware/pico2/src/irq/mod.rs`, `firmware/pico2/src/critical_section.rs` (new); `firmware/pico2/link.ld` (52 `PROVIDE` lines); `firmware/pico2/src/irq/vectors.rs` (new in revision 2: vector slots 16 to 67 through `with_device_interrupts`, the extern block of the 52 symbols, and the `Vector` type moved from `lib.rs`); `firmware/pico2/src/lib.rs` (module list; `VECTOR_TABLE` calls `irq::with_device_interrupts`); `firmware/pico2/src/common/reg.rs` (`RegAddr::NVIC`); `firmware/pico2/src/common/board.rs` (device `nvic`). cwht side: handlers are defined in `cwht-app` with `pico2::interrupt!` and call `cwht-core` functions; the handler bodies and what they share are designed by the firmware architecture ADR (WP-PDR-32) and the `SW-SCHED` design.
- New `SW-<SUB>` modules: none. ICDs created: none.

### 4.3 Verification and safety

- Evidence at revision 2 (`c6e5100`; author runs, 2026-09-27): the move changes no behaviour and no host test; 49 `pico2` host tests pass on the branch; dev target build clean; `rustfmt` and `clippy::pedantic` clean on `irq/mod.rs` and `irq/vectors.rs`; `lib.rs` 564 lines (588 before the package, 704 at revision 1). The unsafe sites move, not change: the extern block of the 52 symbols and the `Sync` impl of `Vector` are now in `irq/vectors.rs`, each with its `// SAFETY:` comment; `tools/unsafe_audit.py --check` passes at the top of the stack (`48e07ec`), as do Miri and the complexity gate (ADR-051 section 4.3). The slot-62 link test of revision 1 is not repeated at revision 2 (no scratch application was linked); the dev-board check below confirms the vector placement on the target.
- Evidence at revision 1 (`9305f59`; author runs, 2026-09-27): 16 new host tests (12 in `pico2`: Table 94 line numbers, word and bit split, rejection of lines 52 and above with no register access, exactly one bit written per call in the right group, no offset at or beyond `NVIC_IPR0`; `CsCell` replace, `with_mut`, nested `Busy` for both operations, flag cleared after use, distinct cells nesting; 4 contract tests in `api`), all passing natively and under Miri; target build without warnings; a scratch application linked against the branch with `pico2::interrupt!(SPAREIRQ_IRQ_0, ...)` shows vector slot 62 holding the application's handler and slots 16, 17 and 67 holding `DefaultHandler` (read back from the linked ELF's `.vector_table` with `rust-objcopy`); `tools/unsafe_audit.py --check` passes with seven new sites, each with a `// SAFETY:` comment (two `asm!` blocks, the `Sync` impl and two access blocks of `CsCell`, the macro's `no_mangle` attribute, the extern block of the 52 symbols); complexity: no new function above CC 12 except the contract check `check_out_of_range` at 13 (yellow, test code).
- Mock in `cwht-hal-mock`: a recording `InterruptController` (enabled and pending bit sets, rejected-line count) is written after this ADR's review fixes the trait shape, against the same IRQ clauses (plan WP-PDR-41; 07 section 3.5).
- Dev-board check: `firmware/devcheck/src/bin/irq_check.rs` by the independent test author, report `docs/vv/reports/devcheck-irq-r1.md` (`credit: false`): a software-pended spare line reaches its handler; a disabled line does not; two lines pended together run in line-number order and neither handler interrupts the other (the one-priority rule on silicon, CS-34 "TC-SW-HAL-* dev-board check").
- ACC-EMU-001: the candidate emulator does not model NVIC priorities (07 CS-34), so the one-priority property is outside its scope; handler reachability is inside it if the emulator ADR accepts NVIC pending.
- Hazard analysis update required: no. Safety-critical software scope changed: no.

### 4.4 Cost, schedule, risk

- BOM and lead time: none. Gate: PDR (FW-B1). RSK-013: second of five minimal-keyer packages. TPMs: none.

## 5. Compliance and tailoring

None. CS-10 permits inline assembly only in `pico2` boot code; the two `asm!` statements of `critical_section::with` (`mrs`/`cpsid i` and `msr PRIMASK`) are in `pico2` but not in boot code. The author reads CS-10's intent (assembly confined to `pico2`) as met; the reviewer decides whether this needs a CS-10 wording change through 07's writer (plan section 5.3) rather than a waiver.

## 6. Decision record (the decision memo for this decision, charter section 4)

Not decided. Proposed memo wording (Form 1): "Owner (date): I merge rustos branch `cwht/wp-sw-09` as reviewed, and ADR-052 is Accepted."

## 7. Related

- Supersedes: none. Superseded by: none.
- Trade study: TS-002 (see ADR-051 section 7 for the class question and the numbering note)
- Related ADRs: ADR-011, ADR-019, ADR-027, ADR-051 (the branch base), ADR-053 (alarms raise `TIMER0_IRQ_0..3` through these vectors)
- Review where presented: PDR
- Revisit conditions: the firmware architecture ADR (WP-PDR-32) starts core 1 or adopts nested priorities (then `CsCell` needs a multicore lock and this ADR is superseded); a linker other than `rust-lld` is adopted

## 8. Revision history

| Revision | Date | rustos commit | Change | Review |
|---|---|---|---|---|
| 1 | 2026-09-27 | `9305f59` | First issue | INSP-096 iteration 1 (NEEDS CHANGES, finding-1 Major); INSP-102 (assurance APPROVED, 3 Minor) |
| 2 | 2026-09-27 | `c6e5100` (after merging `cwht/wp-sw-11` at `4a8e825`) | INSP-096 finding-1 (CS-18): the device-interrupt entries, their extern block and the `Vector` type move from `lib.rs` to `irq/vectors.rs`; `lib.rs` does not grow (sections 2 and 4.2). The pre-existing excess of `lib.rs` over 500 lines (550 at `2ec64c0`) is reported to the owner as a rustos item. Minor findings of INSP-096 and INSP-102 are not addressed in this revision (plan rule C1) | INSP-096 and INSP-102 iteration 2 (delta) |
