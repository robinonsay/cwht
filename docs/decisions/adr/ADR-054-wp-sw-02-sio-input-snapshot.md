# ADR-054: WP-SW-02 input sampling through SIO: `api::gpio::InputSnapshot`, every input of a group read in one `GPIO_IN` load

| Field | Value |
|---|---|
| ID | ADR-054 |
| Status | Proposed (for the owner's review and merge of rustos branch `cwht/wp-sw-02` as rustos maintainer, OD-23; FW-B1) |
| Date proposed | 2026-09-27 (revision 2 of 2026-09-27: INSP-098 finding-1 fixed, section 8) |
| Date decided | not decided |
| Decision class | 1 by 06 section 14.1 item (c) (GPIO sampling feeds the keyer, a 07 section 14.1 component); a work-package design within TS-002 alternative A0, as ADR-027 requires (see ADR-051 section 7 for the class question) |
| Decision authority | Robin (safety-critical scope; rustos change merged by the owner, ADR-019) |
| Author | Claude (WP-PDR-41 author invocation, firmware developer role, 2026-09-27) |
| Independent reviewer | Pending: `docs/reviews/PDR/checklists/adr-054-wp-sw-02-sio-input-snapshot.md` (design checklist sections A, B, H) with its software assurance pair; code in `code-wp-sw-02.md` and `code-wp-sw-02-software-assurance.md` |
| Life-cycle phase | B |
| Baseline affected | none now; the rustos pin moves at merge by a Class I CR (PCR-4) |
| Change request | none for this ADR |

## 1. Context

cwht reads the key or paddle contacts, the encoder A/B, the buttons and the jack detect by sampling them every millisecond from the TIMER0 ALARM1 handler, never by `IO_BANK0` edge interrupts (CS-35); edges and debounce are derived in `cwht-core` from consecutive timestamped samples (07 section 5 item 1; REQ-SW-KEYER-019 to 021). A snapshot in which the dit contact was read before a transition and the dah contact after it would give the iambic logic a combination that never existed. rustos has `GpioPinIn::read()` per pin only (07 section 19 row WP-SW-02: "add a batched `SioInputs::snapshot()` returning all input levels in one SIO read").

- Driving inputs and expectations: SI-018 (straight key and paddles), SI-034 (3.5 mm TRS key jack), SI-026, SI-033
- Requirements that constrain the decision: REQ-SW-KEYER-019 (sampling every 1.000 ms ±0.010 ms), REQ-SW-KEYER-020, 021 (debounce by consecutive samples), REQ-SW-KEYER-022 (key-closed interlock by samples), REQ-SW-KEYER-039 (operator events distinct only from different samples), REQ-SYS-048 and REQ-SYS-162 (debounce times)
- Hazards in play: HZ-004 (a wrong key reading can key or hold the transmitter), HZ-010 (ESD and RF pickup on the key inputs; the sampling and debounce design is part of its control set)
- Research consulted: `docs/research/rustos-toolchain-proof.md` F11 (RP2350-E9: inputs are pull-up, switch to ground, Schmitt on, High), "Peripheral to driver map" encoder and key row (1 kHz sampling recommended); RP2350 datasheet sections 3.1.3 and 3.1.11 (SIO `GPIO_IN`, Table 16, p55)
- Guidance consulted: SWE-134 items g, i; SWE-219
- Assumptions the decision rests on, and how and by when each is confirmed:
  1. All cwht key, paddle, encoder and button inputs are on GPIO 0 to 29 (the RP2350A has no others), so one 32-bit `GPIO_IN` load covers them. Confirmed by the ICD-CTL-SW pin map (WP-PDR-36a).

## 2. Decision

rustos gains, on branch `cwht/wp-sw-02` at commit `38434b2` (revision 2; revision 1 was `f85a190`), on `cwht/wp-sw-01` (merged at `58fe739` by `5d4637f`):

1. **`api::gpio::InputLevels`** (level bits and the mask of pins they cover; bits outside the mask are always 0 by construction; `level(pin) -> Option<bool>`) and **`api::gpio::InputSnapshot::snapshot() -> Result<InputLevels, Error>`**, with contract clauses SNP-1 (fixed mask), SNP-2 (0 outside the mask), SNP-3 (each level equals the pin's level at the sample instant) and SNP-4 (one instant) in the trait documentation, checked by `api/tests/gpio_snapshot_contract.rs`; a pin-by-pin reader whose inputs change mid-read is caught by the SNP-4 check.
2. **`pico2`**: `Rp2350Gpio` records the pins it configures as inputs; `Rp2350Gpio::input_snapshot(mask)` returns an `Rp2350InputSnapshot` only if `mask` is non-empty and every pin in it is one of those inputs (`pico2::gpio::snapshot::NotInput` otherwise, carrying the offending pins; revision 1 used a `GpioError::NotInput` variant); the snapshot reads `SIO.GPIO_IN` once and masks it. It touches no `IO_BANK0` interrupt register and no pad setting (CS-35). The snapshot value is `Copy`, so the ALARM1 handler can own one. The mask check is a pure function; the read is generic over the `Regs` capability of ADR-051. The existing pin API is unchanged.

## 3. Alternatives considered

| Option | Description | Why not chosen (or why chosen) |
|---|---|---|
| A (chosen) | A sampler for a fixed mask of pins the port configured as inputs; one `GPIO_IN` load | All levels from one instant (SNP-4); only pins the owner made inputs can be observed |
| B | Read each `GpioPinIn` in turn in the handler | Levels from different instants; five to eight SIO loads instead of one |
| C | A snapshot of all 30 pins with no mask | Would expose pins other drivers own (outputs, ADC inputs) to the keyer's sample; an owner could not reason about which pins a module reads |
| D | `IO_BANK0` edge interrupts | Excluded by CS-35 and REQ-SYS-129's one-priority execution model; debounce would need timestamps in the edge handler |
| E | Do nothing | The keyer samples pin by pin (option B) |

## 4. Consequences

### 4.1 Requirements created or changed

| Requirement | Relationship | Note |
|---|---|---|
| none | | The sampling rule "all key, paddle, encoder and button inputs in one read per tick" may be written as a `REQ-SW` or `SW-KEYER` row in WP-PDR-35 citing this ADR |

### 4.2 Interfaces, design and code

- ICDs affected: none; ICD-CTL-SW (WP-PDR-36a) assigns the pins the mask names. rustos `docs/icd/rp2350/gpio/` covers `GPIO_IN`.
- Design elements: rustos `api/src/gpio/mod.rs` (additions), `api/tests/gpio_snapshot_contract.rs` (new), `firmware/pico2/src/gpio/snapshot.rs` (new: `Rp2350InputSnapshot`, the `NotInput` error, and inherent `impl` blocks holding `Rp2350Gpio::input_snapshot`, the `track_input` recording used by `input_from_handle`, and `Rp2350GpioIn::BIT`), `firmware/pico2/src/gpio/gpio.rs` (the `inputs` record replaces the `_private` field and keeps the struct literal unwritable outside the `gpio` module; `input_from_handle` calls `track_input` in one line; the struct doc says what it holds), `firmware/pico2/src/gpio/mod.rs` (module list). `gpio.rs` does not grow: 512 lines before and after this package (revision 1: 546; CS-18, INSP-098 finding-1). Its pre-existing excess over the 500-line limit is left to the owner as rustos maintainer and reported as a rustos item.
- New `SW-<SUB>` modules: none. ICDs created: none.

### 4.3 Verification and safety

- Evidence at revision 2 (`38434b2`; author runs, 2026-09-27): the move changes no behaviour; the two mask-rejection tests now compare with `NotInput { mask }` directly; 81 `pico2` host tests pass on the branch; target build clean; `rustfmt` and `clippy::pedantic` clean on `snapshot.rs` and on the changed `gpio.rs` lines; Miri, complexity and unsafe audit at the top of the stack as ADR-051 section 4.3.
- Evidence at revision 1 (`f85a190`; author runs, 2026-09-27): 11 new host tests (6 in `pico2`: mask accepted, stray pin rejected with the offending bits, empty mask rejected, exactly one `GPIO_IN` read masked to the group, levels follow the register, pin bit constants; 5 contract tests in `api`), all passing natively and under Miri; target build without warnings; complexity gate passes; no new `unsafe` site.
- Mock in `cwht-hal-mock`: a scriptable `InputSnapshot` fed from a time-indexed level table, written after this ADR's review, against SNP-1 to SNP-3 (SNP-4 holds for a table by construction).
- Dev-board check: `firmware/devcheck/src/bin/sio_check.rs` by the independent test author, report `docs/vv/reports/devcheck-sio-r1.md` (`credit: false`): the owner's straight key and paddle on the development-board key jack wiring of FM-4 (until the ICD-CTL-SW pin map exists) show each contact's state on the LED, sampled at 1 kHz from ALARM1; a snapshot with a mask naming an output pin is refused.
- ACC-EMU-001: SIO GPIO input is inside the candidate scope (07 section 9.1 Integration row: "scripted stimuli on SIO GPIO"); the register-sequence comparison is recorded if the emulator is accepted.
- Hazard analysis update required: no. Safety-critical software scope changed: no. SWE-134 g is served by the single-instant sample the keyer's input checks run on.

### 4.4 Cost, schedule, risk

- BOM and lead time: none. Gate: PDR (FW-B1; FM-4). RSK-013: fourth of five minimal-keyer packages. TPMs: none.

## 5. Compliance and tailoring

None.

## 6. Decision record (the decision memo for this decision, charter section 4)

Not decided. Proposed memo wording (Form 1): "Owner (date): I merge rustos branch `cwht/wp-sw-02` as reviewed, and ADR-054 is Accepted."

## 7. Related

- Supersedes: none. Superseded by: none.
- Trade study: TS-002 (see ADR-051 section 7)
- Related ADRs: ADR-009 (straight key and paddle on one TRS jack), ADR-011, ADR-019, ADR-027, ADR-051 (`Regs`), ADR-053 (the ALARM1 tick that samples)
- Review where presented: PDR
- Revisit conditions: the pin map places a key input above GPIO 31 (not possible on the RP2350A); the Bench latency of REQ-SW-KEYER-017 or 018 is not met with 1 ms sampling (then edge detection is reconsidered by a CR on CS-35)

## 8. Revision history

| Revision | Date | rustos commit | Change | Review |
|---|---|---|---|---|
| 1 | 2026-09-27 | `f85a190` | First issue | INSP-098 iteration 1 (NEEDS CHANGES, finding-1 Major); INSP-104 (assurance NEEDS CHANGES on the concurred finding-1) |
| 2 | 2026-09-27 | `38434b2` (after merging `cwht/wp-sw-01` at `58fe739`) | INSP-098 finding-1 (CS-18): `input_snapshot`, the `NotInput` error (now its own type), `BIT` and the input recording move to `snapshot.rs`; `gpio.rs` does not grow (sections 2 and 4.2). Minor findings of INSP-098 and INSP-104 are not addressed in this revision (plan rule C1) | INSP-098 and INSP-104 iteration 2 (delta) |
