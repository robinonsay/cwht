# ADR-051: WP-SW-11 clock bring-up in rustos `pico2`: crystal, PLL_SYS 150 MHz, 1 µs ticks, bounded waits, measured result, and register access through a host-testable capability

| Field | Value |
|---|---|
| ID | ADR-051 |
| Status | Proposed (for the owner's review and merge of rustos branch `cwht/wp-sw-11` as rustos maintainer, OD-23; FW-B1) |
| Date proposed | 2026-09-27 (revision 2 of 2026-09-27: INSP-095 finding-1 fixed, section 8) |
| Date decided | not decided |
| Decision class | 1 by 06 section 14.1 item (c): the clocks and PLL driver is in the call path of every component of 07 section 14.1 and is itself safety-critical (07 section 14.1 drivers row; 03 section 4.3). The make/buy choice and the work-package list were decided by trade study TS-002 and recorded in ADR-027 (SRR decision 107); this ADR records the work-package design inside that decided alternative A0, as ADR-027 section 2 and 07 section 19 require ("proposed as its own ADR when its trait shape is fixed"). No new trade study is opened: the alternatives in section 3 are design options within A0, not competing architectures. Whether a work-package ADR under TS-002 needs its own trade study is put to the reviewer as a question (section 7) |
| Decision authority | Robin (safety-critical component; the change is to rustos, which the owner maintains; the merge is the approval, ADR-019) |
| Author | Claude (WP-PDR-41 author invocation, firmware developer role, 2026-09-27) |
| Independent reviewer | Pending: design checklist sections A, B, H in `docs/reviews/PDR/checklists/adr-051-wp-sw-11-clocks.md` with its software assurance pair; the rustos code in `docs/reviews/PDR/checklists/code-wp-sw-11.md` and `code-wp-sw-11-software-assurance.md` (plan WP-PDR-41 "Records") |
| Life-cycle phase | B |
| Baseline affected | none now. At merge the rustos pin in `tools/toolchain.lock.md` section 3 moves by a Class I CR (plan section 6.2, PCR-4); the pin is part of `baseline/srr` |
| Change request | none for this ADR; the pin-move CR (PCR-4) is raised on the day of the owner's merge |

## 1. Context

After the bootrom, the RP2350 runs from its ring oscillator, whose frequency "varies with PVT" (datasheet section 8.1.1.2); TIMER0 does not count until its tick generator runs (section 12.8.4 note). Every timing budget of cwht (keyer elements, the 1 kHz input sampling, the watchdog) therefore depends on a clock driver that rustos does not have (`docs/research/rustos-toolchain-proof.md` F8 item 2, F10, High). 07 section 19 makes it work package WP-SW-11, safety-critical, with coding rule CS-37: TICKS enabled explicitly before any TIMER0 or watchdog use, XOSC `STABLE` and PLL `LOCK` waits bounded by a TIMER0-independent loop count, and a clock fault that leaves the safe outputs asserted. 07 section 14.2 assigns it SWE-134 items a, g, j and k. WP-SW-01 (TIMER0) cannot be built before it (plan WP-PDR-41; technology assessment section 3.18 "Gaps").

- Driving inputs and expectations: SI-007 (Rust on rustos), SI-026 (host-first through `api` traits), SI-033 (drivers upstream in rustos), SI-018 (keyer for straight key and paddles)
- Requirements that constrain the decision: REQ-SYS-042 (element and space timing within the larger of ±1 % and ±0.5 ms), REQ-SYS-127 (Rust on rustos), REQ-SYS-128 (host-testable layering), REQ-SYS-130 (safe state first after reset), REQ-SW-KEYER-019 (inputs sampled every 1.000 ms ±0.010 ms)
- Hazards in play (`docs/safety/hazards.json` 0.5.0-pha): the hazards whose firmware controls run on the timing this driver provides, as 07 section 14.1 "Drivers these depend on" row inherits them: HZ-001 to HZ-008, HZ-010, HZ-011, HZ-012, HZ-014 (ADR-019 hazard line); HZ-004 (unintended or stuck transmission) most directly, through keyer and key-down timeouts
- Research consulted: `docs/research/rustos-toolchain-proof.md` F8, F9, F10 (clock tree, TICKS registers, A3 reset-value change, High), "Peripheral to driver map" Clocks row, DECISION "injectable register-access trait"; RP2350 datasheet (rustos `docs/rp2350-datasheet.pdf`, build 2025-02-20) sections 7.5, 8.1.2, 8.1.3, 8.1.5.1, 8.1.5.2, 8.1.6, 8.2, 8.5, 8.6, read through rustos `docs/extracted/rp2350-datasheet.md` at `2ec64c0` by `git show`; rustos clocks ICD `docs/icd/rp2350/clocks/02_programming.md`
- Guidance consulted: SWE-134 items a, g, j, k (NPR 7150.2D section 3.7.3); SWE-219 and SWE-220 (sections 3.7.4, 3.7.5); SWE-058, SWE-060, SWE-062 (chapter 4)
- Assumptions the decision rests on, and how and by when each is confirmed:
  1. The Pico 2 crystal is 12 MHz (Pico 2 datasheet section 2, cited by the research F8 item 2). Confirmed by the dev-board check (section 4.3): the frequency counter reads `clk_sys` 150 MHz ±1 % only if the reference is 12 MHz.
  2. A poll budget of 100 000 register reads bounds every wait with margin at any ROSC frequency: the slowest wait, the crystal start-up of about 1 ms (section 8.2.4), takes at most about 2 400 reads even at a 24 MHz ROSC with ten cycles per read. Confirmed by the poll counts the driver reports (`ClockReport::polls`), read on the development board before CDR.
  3. The owner accepts a crate-private register-access capability in `pico2` (the pilot of PDR decision 93, OD-16, whose recommendation is "adopt only for drivers of safety-critical components"). Confirmed by OD-16 at B1b (Thu 2026-10-01) and by the merge; if OD-16 rules against it, the revisit condition of section 7 applies.

## 2. Decision

rustos `pico2` gains a `clocks` module, delivered on rustos branch `cwht/wp-sw-11` at commit `4a8e825` (revision 2; revision 1 was `213c536`), on `cwht/l-016-6` at `5b39e8e` (which makes `pico2` host-compilable, SRR lien L-016-6). The board declares a `clocks: Rp2350Clocks` device. `Rp2350Clocks::init(handle, &ClockConfig) -> Result<ClocksReady, ClockFault>` consumes the handle and runs, in order: check the configuration (`plan`, before any register write); start the 12 MHz crystal (`FREQ_RANGE 1_15MHZ`, `STARTUP.DELAY` = 47, enable) and wait for `STABLE`; move `clk_sys` to `clk_ref` by clearing `CLK_SYS_CTRL.SRC` alone through the clear alias, leaving the aux select as it is, and wait for `SELECTED`; move `clk_ref` to the crystal, divided by 1; reset `PLL_SYS` through the `RESETS` set and clear aliases; program `REFDIV` 1, `FBDIV` 125, power the PLL and VCO, wait for `LOCK`, set `POSTDIV1` 5 and `POSTDIV2` 2 (1500 MHz / 10 = 150 MHz) and power the post dividers; with `clk_sys` still on `clk_ref`, select `PLL_SYS` on the `clk_sys` aux mux, then move `clk_sys` to aux and wait for `SELECTED`; stop `clk_peri` (clear `ENABLE` alone and wait for `ENABLED` to clear), select `clk_sys` on its aux mux, divide by 1, set `ENABLE` alone and wait for `ENABLED`; start the TIMER0 and watchdog tick generators with `CYCLES` = 12 (1 µs) and wait for `RUNNING`; then measure `clk_sys` and `clk_peri` with the frequency counter over 1 ms against the crystal and accept each only if the hardware `PASS` flag is set and the result lies within ±1 % (148 500 to 151 500 kHz). The driver relies on no reset value (the A3 reset-value change, research F10): it leaves the aux path by clearing `SRC` alone, which works whatever `AUXSRC` holds, and it writes every control field the tree depends on. It changes an aux select only while the generator is off its aux path, as datasheet section 8.1.2.2 requires before any aux mux change ("Failure to do at least one of the above may cause a glitch"): `clk_sys` after `SELECTED` shows `clk_ref`, `clk_peri` after `ENABLED` shows it stopped. `CLK_SYS_CTRL` resets to `AUXSRC` = ROSC and `SRC` = aux (Table 558), so on a cold boot `clk_sys` runs through the aux mux; revision 1 wrote `AUXSRC` and `SRC` in one word there (INSP-095 finding-1). Every wait is a loop of at most `poll_budget` reads (100 000 in `ClockConfig::PICO2_150_MHZ`); a wait that runs out returns the `ClockFault` naming its step, and no later step runs. `ClocksReady` is the only proof of success; it is neither `Clone` nor `Copy`, and the TIMER0 and PWM constructors take `&ClocksReady`, so no timer or PWM output can exist before the tick and `clk_sys` are proven. The driver touches no application output: on a fault the application stays in the safe state it entered first (REQ-SYS-130; CS-37).

Register access goes through a crate-private capability `pico2::common::reg::Regs` (`read(block, offset)`, `write(block, offset, value)`). On the target its only implementation, `Mmio`, turns the pair into one volatile load or store at `block + (offset & 0x3ffc)`, which keeps every access word-aligned inside the block's 16 KiB register and alias window (datasheet section 2.1.3); it holds the only two `unsafe` blocks of the work package. On the host, a scripted register file (`common::reg::fake::FakeRegs`, test builds only) implements it, so the whole bring-up sequence, including every decision and every fault path, runs under `cargo test -p pico2 --lib` against a golden register-write sequence taken from the datasheet steps. Offsets come from `#[repr(C)]` layout structs through `offset_of!`, each checked against its datasheet table by a compile-time assertion.

## 3. Alternatives considered

| Option | Description | Why not chosen (or why chosen) |
|---|---|---|
| A (chosen) | Sequence generic over a crate-private `Regs` capability; `Mmio` on target, scripted register file in host tests; decisions also in pure functions (`plan`, `judge`) | Every decision and every fault path of a safety-critical driver runs on the host with MC/DC pairs (CS-38, SWE-219), and the register sequence itself is checked, not only the decisions. Cost: one trait and a test-only register file; zero run-time cost (monomorphized to the same volatile accesses) |
| B | Raw-pointer MMIO as in the existing `gpio` driver, with only the decisions (`plan`, the wait-loop condition) split into pure functions | Meets CS-38 by the letter, but the sequence and the timeout loops stay target-only: they would be evidenced only by Inspection and the dev-board check, and a missed step (for example no `RUNNING` wait) is invisible to host tests |
| C | Public register-access trait in `api` | `api` carries no register facts by design (`api/src/lib.rs`); a public trait would widen the rustos public surface for a need that is internal to `pico2` |
| D | Port the pico-sdk `clocks_init` sequence without the frequency-counter check | The counter check costs about 2 ms at boot and catches a PLL locked to a wrong frequency or a divider mis-set before any timing depends on it; kept |
| E | Do nothing (stay on the ROSC) | Keyer timing would be off by the ROSC's PVT variation; REQ-SYS-042 and REQ-SW-KEYER-019 cannot be met; TIMER0 does not count at all without the tick |

## 4. Consequences

### 4.1 Requirements created or changed

| Requirement | Relationship | Note |
|---|---|---|
| none | | The L2 `REQ-SW` rows for the target platform rules (07 section 4 item 7: TICKS enabled explicitly, bounded XOSC and PLL waits with a fault path) are written by the L2 software author in WP-PDR-35 and may cite this ADR in `source_ids`; the driver behaviour here is the design that meets them |

### 4.2 Interfaces, design and code

- ICDs affected: none of cwht's. rustos `docs/icd/rp2350/clocks/` (existing) is the register reference; no change to it.
- Design elements: rustos `firmware/pico2/src/clocks/{mod.rs, regs.rs, clocks.rs, tests.rs, clocks_tests.rs}`, `firmware/pico2/src/common/reg.rs` (`Regs`, `Mmio`, `poll`, alias offsets, new `RegAddr` variants `CLOCKS`, `XOSC`, `PLL_SYS`, `TICKS`), `firmware/pico2/src/common/reg/fake.rs` (test only), `firmware/pico2/src/common/board.rs` (device `clocks`), `firmware/pico2/src/lib.rs` (module list; host-build note). cwht side: the `cwht-app` composition root calls `Rp2350Clocks::init` right after driving the safe outputs, and halts in the safe state on `Err` (CS-11 construction arm); the firmware architecture ADR of WP-PDR-32 places this in `SW-BOOT`.
- New `SW-<SUB>` modules: none. ICDs created: none.

### 4.3 Verification and safety

- Evidence at revision 2 (`4a8e825`; author runs, 2026-09-27): 37 host tests of `pico2`, passing with rustc 1.98.0 of the lock. The test register file now starts from the datasheet reset values of `CLK_SYS_CTRL` (`0x41`), `CLK_REF_CTRL` and `CLK_PERI_CTRL`. A new test replays the access log of the whole bring-up, from the reset state and from a restart state (`clk_sys` on `PLL_SYS`, `clk_ref` on the crystal, `clk_peri` running from `PLL_SYS`), and fails on any `AUXSRC` change made while `SELECTED` or `ENABLED` has not shown the generator off its aux path. Two should-panic tests show that the check rejects the revision 1 step 3 and step 8 writes, and the revision 1 `clocks.rs` fails the new test (mutation run). At the top of the stack (`cwht/wp-sw-03` at `48e07ec`, which contains this fix): 101 `pico2` host tests pass natively and under Miri (`cargo +nightly-2026-08-24 miri test -p pico2 --lib`); dev and release target builds without warnings; `tools/complexity_gate.py --max 15` passes (max CC 12 over `api` and `pico2`); `tools/unsafe_audit.py --check` passes (46 sites, all with `// SAFETY:`, none in forbidden crates, unsigned until CDR).
- Evidence at revision 1 (`213c536`; author runs, 2026-09-27, rustc 1.98.0 of the lock): 34 host tests of `pico2` (the golden sequence; each of the 15 `ClockFault` variants is returned by its own step, and where a later block exists that block is left unwritten; the poll budget bounds each wait exactly; every `plan` limit at both edges; `judge` MC/DC pairs for the hardware flag and both window edges), all passing, also under Miri (`cargo +nightly-2026-08-24 miri test -p pico2 --lib`, no undefined behaviour); target build `thumbv8m.main-none-eabihf` dev and release without warnings; `clippy::pedantic` clean on the new files; `tools/complexity_gate.py --max 15` over rustos `api` and `pico2`: max CC 10 in this work package, no function above 12; `tools/unsafe_audit.py --check` passes with the two new `Mmio` sites carrying `// SAFETY:` comments (signatures due before CDR, CS-07).
- Contract test (`api/tests/<periph>_contract.rs`): not applicable, no `api` trait (07 section 19 row WP-SW-11: "no trait; boot-time"). Mock in `cwht-hal-mock`: not applicable for the same reason.
- Dev-board check (07 section 19 closing rule; plan WP-PDR-41): `firmware/devcheck/src/bin/clocks_check.rs`, written by an independent test author (07 section 3.4 phase 2), reported in `docs/vv/reports/devcheck-clocks-r1.md` with `credit: false`. It must show on a bare Pico 2: init returns `Ok`; the measured `clk_sys` and `clk_peri` in kHz; the poll count of each wait against the budget (assumption 2); a 1 Hz LED toggle timed by TIMER0 that holds within ±0.5 s over 60 s against a stopwatch (the tick at 1 µs); and `clk_sys` and `clk_peri` running after init both from a power-on start and from a watchdog restart that leaves `clk_sys` on `PLL_SYS` (the revision 2 step 3 and step 8 order).
- ACC-EMU-001 register-sequence comparison: the clock blocks are outside the candidate emulator's scope unless the emulator ADR (WP-PDR-42) says otherwise; the golden host sequence stands as the reference sequence.
- Evidence class implications: HostUnit for the sequence and decisions; Inspection for the `Mmio` accesses against datasheet sections 2.1.3 and 2.2; Bench `credit: false` on the development board.
- Hazard analysis update required: no (no new cause or control; the driver implements the CS-37 control 07 section 14.2 already assigns).
- Safety-critical software scope (SWE-134 provisions) changed: no. Items a (TICKS before use), g (`STABLE`, `LOCK`, `RUNNING`, `SELECTED` read back, measured frequencies judged), j (every wait bounded independently of TIMER0) and k (a fault per failed step, returned, never a hang) are implemented as 07 section 14.2 states.

### 4.4 Cost, schedule, risk

- BOM, fabrication, enclosure or lead-time impact: none.
- Gate affected: PDR (FW-B1, FM-3); the keyer prototype of WP-PDR-40 needs this merged.
- Risks: RSK-013 (rustos driver effort) progresses by one of the five minimal-keyer packages; no re-score here (WP-PDR-18 owns the register).
- TPMs affected: none. Boot time grows by about 3 ms (crystal start-up about 1 ms, two 1 ms frequency measurements); no TPM tracks it.

## 5. Compliance and tailoring

None. One interpretation is put to the reviewer: coding standard CS-08 requires MMIO "on `#[repr(C)]` register layout structs addressed from `pico2::common::reg::RegAddr`" with integer-to-pointer arithmetic only in that module. Here the layout structs fix every offset (`offset_of!`, compile-time checked) and the only integer-to-pointer arithmetic is `Mmio::address` inside `pico2::common::reg`, but the access itself is a word at `block + offset` rather than a field projection. The author reads this as meeting CS-08's intent; a reviewer who reads it otherwise raises it as a finding against 07 (a CR on CS-08), not as a waiver.

## 6. Decision record (the decision memo for this decision, charter section 4)

Not decided. Proposed memo wording for the owner's disposition (Form 1): "Owner (date): I merge rustos branch `cwht/wp-sw-11` as reviewed, and ADR-051 is Accepted." The disposition is transcribed here with its date, and the pin-move CR (PCR-4) cites it.

## 7. Related

- Supersedes: none
- Superseded by: none
- Trade study: TS-002 (make/buy, decided at SRR; this ADR records a work-package design within its alternative A0). Question to the reviewer: whether 06 section 14.1 item (c) requires a separate trade study for a work-package design under an already decided class 1 study
- Numbering: the next free number by the README rule is ADR-028, but CR-006 claims ADR-028 and the PDR work plan reserves ADR-029 to ADR-050 as provisional numbers of other work packages running in parallel (plan section 3.1 "Numbers"; WP-PDR-19 to 38); the five WP-PDR-41 ADRs take ADR-051 to ADR-055 so that no parallel author collides. Reported to the lead SE
- Related ADRs: ADR-019 (drivers upstream in rustos), ADR-027 (rustos A0), ADR-011 (host-first verification), ADR-052 (WP-SW-09), ADR-053 (WP-SW-01, consumes `ClocksReady`), ADR-055 (WP-SW-03, consumes `ClocksReady`)
- Review where presented: PDR
- Revisit conditions: OD-16 rules against a register-access capability in `pico2` (then the sequence returns to raw-pointer MMIO with only the pure functions host-tested, option B); the dev-board poll counts show less than 10 times margin on any wait; the stepping of the procured Pico 2 modules changes a clock reset value the driver relies on (it relies on none; any such finding is a defect)

## 8. Revision history

| Revision | Date | rustos commit | Change | Review |
|---|---|---|---|---|
| 1 | 2026-09-27 | `213c536` | First issue | INSP-095 iteration 1 (NEEDS CHANGES, finding-1 Major); INSP-106 (assurance NEEDS CHANGES on the concurred finding-1) |
| 2 | 2026-09-27 | `4a8e825` | INSP-095 finding-1: step 3 clears `CLK_SYS_CTRL.SRC` alone and polls `SELECTED`, `AUXSRC` is first written in step 7; step 8 clears `ENABLE` alone, waits for `ENABLED` to clear, then writes `AUXSRC`, the divider and sets `ENABLE`; tests start from the datasheet reset values and check the aux-mux rule of section 8.1.2.2 (sections 2 and 4.3). Minor findings of INSP-095 and INSP-106 are not addressed in this revision (plan rule C1) | INSP-095 and INSP-106 iteration 2 (delta) |
