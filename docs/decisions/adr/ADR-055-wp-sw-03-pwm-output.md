# ADR-055: WP-SW-03 PWM output: `api::pwm::PwmOutput` on rustos slices 0 to 7, one output per slice, frequency within 0.1 %, glitch-free duty and off

| Field | Value |
|---|---|
| ID | ADR-055 |
| Status | Proposed (for the owner's review and merge of rustos branch `cwht/wp-sw-03` as rustos maintainer, OD-23; FW-B1) |
| Date proposed | 2026-09-27 (revision 2 of 2026-09-27: INSP-099 finding-1 and INSP-105 finding-1 fixed, section 8) |
| Date decided | not decided |
| Decision class | 1 by 06 section 14.1 item (c) (PWM drives the sidetone, whose level is part of the HZ-005 controls, 07 section 14.1 drivers row "PWM (sidetone and audio level)"); a work-package design within TS-002 alternative A0, as ADR-027 requires (see ADR-051 section 7 for the class question) |
| Decision authority | Robin (safety-critical scope; rustos change merged by the owner, ADR-019) |
| Author | Claude (WP-PDR-41 author invocation, firmware developer role, 2026-09-27) |
| Independent reviewer | Pending: `docs/reviews/PDR/checklists/adr-055-wp-sw-03-pwm-output.md` (design checklist sections A, B, H) with its software assurance pair; code in `code-wp-sw-03.md` and `code-wp-sw-03-software-assurance.md` |
| Life-cycle phase | B |
| Baseline affected | none now; the rustos pin moves at merge by a Class I CR (PCR-4) |
| Change request | none for this ADR |

## 1. Context

The keyer prototype of FM-4 needs a PWM sidetone on the development board for the owner's HSI evaluation (07 section 3.2 FW-B1; plan WP-PDR-40), and the Rev A design uses PWM for the sidetone and the LCD backlight (07 section 19 row WP-SW-03, `PwmOutput` with frequency, duty and enable; CS-36: slices 0 to 7 only, each enabled through its own slice enable bit). The audio chain and level policy are decided by TS-010 (WP-PDR-25); this work package only has to produce an exact tone that switches on and off cleanly. rustos has no PWM driver, and no PWM register ICD (`docs/research/rustos-toolchain-proof.md` F9 PWM row; technology assessment section 3.18).

- Driving inputs and expectations: SI-018, SI-026, SI-033
- Requirements that constrain the decision: REQ-SW-KEYER-033 (sidetone gate within 1 ms of key-down), REQ-SW-KEYER-027 and 035 (sidetone gate held or withheld), REQ-SYS-128
- Hazards in play: HZ-005 (hearing damage from headphone level, full-scale tones and clicks): a tone left on, a DC level held high when "off", or a partial pulse at switching are click and level causes; HZ-004 indirectly (the sidetone is the operator's cue that the transmitter is keyed)
- Research consulted: `docs/research/rustos-toolchain-proof.md` F9 (PWM registers, GPIO to slice map), "Peripheral to driver map" sidetone and backlight row; RP2350 datasheet section 12.5 (p1073 to p1087), extracted into the rustos ICD `docs/icd/rp2350/pwm/` by this work package
- Guidance consulted: SWE-134 items c, g, k; SWE-219
- Assumptions the decision rests on, and how and by when each is confirmed:
  1. The sidetone and the backlight are on GPIOs of different PWM slices. Confirmed by the ICD-CTL-SW pin map (WP-PDR-36a); the driver refuses a second output on one slice, so a conflict is found at the first build of the pin map, not in the field.
  2. The sidetone range is within 100 Hz to 3 kHz. Confirmed by TS-010 and the SW-AUDIO requirements; every integer frequency from 100 Hz to 3 kHz in steps of 7 Hz meets the 0.1 % contract in the host tests, and the driver refuses any frequency it cannot make within 0.1 %.

## 2. Decision

rustos gains, on branch `cwht/wp-sw-03` at commit `48e07ec` (revision 2; revision 1 was `6df18af`), on `cwht/wp-sw-02` (merged at `38434b2` by `9df9c57`):

1. **`api::pwm`**: `Duty` in parts per thousand (0 to 1000; `OFF`, `HALF`, `FULL`) and `PwmOutput` with `set_frequency_hz(hz) -> Result<u64, Error>` (the achieved frequency in millihertz), `set_duty(Duty)` and `set_enabled(bool)`. Contract clauses PWM-1 (achieved within 0.1 %), PWM-2 (refused frequency changes nothing), PWM-3 (duty survives frequency changes), PWM-4 (off holds low and on restores the duty, each within the switching latency the implementation states; a duty change lands at the next period), PWM-5 (0 ‰ constant low, 1000 ‰ constant high) and PWM-6 (a new output is off, after a power-on start and after a restart alike) are in the module documentation and checked by `api/tests/pwm_contract.rs`, with three faulty models detected.
2. **`pico2::pwm`**: `Rp2350Pwm::new(handle, &ClocksReady, &Rp2350Gpio)` asserts the PWM reset through the `RESETS` set alias, releases it through the clear alias, waits for `RESET_DONE` (bounded) and clears every slice enable, so every start, a restart that did not reset PWM included, begins with every slice stopped at `CC = 0`, which drives its pin low (section 12.5.3, Tables 1131 to 1135; revision 2, INSP-105 finding-1); it takes `clk_sys` from `ClocksReady` and borrows the GPIO port as proof that `IO_BANK0` and `PADS_BANK0` are out of reset. `output_from_handle::<N>(pin)` maps GPIO `N` to slice `(N / 2) mod 8` and channel `N mod 2` at compile time (Table 1129; `N >= 30` does not compile), refuses a slice whose other channel is already an output (`PwmError::SliceInUse`), then configures the slice with `CC = 0` and starts it before it switches `FUNCSEL` to 4 and clears the pad `OD` and `ISO` bits (isolation last), so the pin comes up low. Frequency: the smallest divider that fits the period in `TOP <= 65534` (so that `CC = TOP + 1`, 100 %, still fits the 16-bit `CC` field), the period rounded to the nearest count, and a refusal (`PwmError::FrequencyOutOfRange`) for 0 Hz, anything outside the divider and period ranges, and any result more than 0.1 % off. Duty is rounded to counts; off is `CC = 0` with the slice running. `CC` and `TOP` are double-buffered by the hardware (section 12.5.2.3): a duty change writes `CC` alone and lands at the next wrap with no partial pulse. An on/off change writes `CC` and then `CTR = TOP`, so the counter wraps at its next count and latches the new `CC` within one count (revision 2, INSP-099 finding-1; section 2.1). `DIV` is not buffered, so a frequency change can alter the one period in progress. PWM interrupts are not used. `timing` and `cc_value` are pure functions; the sequences are generic over the `Regs` capability of ADR-051.
3. **Register ICD**: `docs/icd/rp2350/pwm/` (index, overview and programming model, register map) extracted from datasheet section 12.5, and a row in `docs/icd/rp2350/index.md`.

For the 700 Hz sidetone at `clk_sys` = 150 MHz the driver writes `DIV` = 53/16 (3.3125) and `TOP` = 64 689, giving 700.0003 Hz; for a 20 kHz backlight, `DIV` = 1 and `TOP` = 7 499, exactly 20 kHz.

### 2.1 Switching latency, sidetone onset and envelope (revision 2)

**Latency of each operation.** One counter step lasts `DIV` `clk_sys` cycles, at most 4 095/16 = 255.9 cycles (`MAX_DIV16`), 1.71 µs at 150 MHz; at 700 Hz it is 3.3125 cycles, 22 ns. With `f` the tone frequency:

| Operation | Takes effect | 100 Hz | 300 Hz | 700 Hz | 1 kHz | 3 kHz |
|---|---|---|---|---|---|---|
| `set_enabled(true)` or `set_enabled(false)` | at the next counter step (forced wrap), ≤ 1.71 µs at any frequency | 153 ns | 51 ns | 22 ns | 15 ns | 7 ns |
| `set_duty` | at the next wrap, ≤ `1 / f` | 10 ms | 3.33 ms | 1.43 ms | 1.00 ms | 0.33 ms |
| `set_frequency_hz` | `DIV` at once, `TOP` and `CC` at the next wrap, ≤ one old period | 10 ms | 3.33 ms | 1.43 ms | 1.00 ms | 0.33 ms |

The per-frequency values are one count at the divider `timing` chooses (for example `DIV` = 37/16 at 1 kHz and 53/16 at 700 Hz, as the host tests show); the 1.71 µs bound is reached only with the largest divider, which `timing` uses only below about 9 Hz at 150 MHz. The two register writes of the call add a few bus cycles. Revision 1 switched on and off at the next wrap as `set_duty` still does: up to 1.43 ms at 700 Hz and 10 ms at 100 Hz, above the 1 ms of REQ-SW-KEYER-033 and HZ-005 K4 for every tone below 1 kHz (INSP-099 finding-1).

**Effect of the forced wrap on clicks.** Writing `CTR = TOP` ends the period in progress one count later. At switch-on the output was low (`CC = 0`), so only the low interval before the first pulse is shortened and no extra edge appears. At switch-off the high interval in progress, if any, is cut short once, so the last pulse can be narrower than the others; no level is held and the output is low from the next count. If a natural wrap falls between the `CC` and `CTR` writes, the new `CC` is already latched and the forced wrap shortens that first period to one count: at switch-on one high pulse of at most one count (≤ 1.71 µs) precedes the first full period; at switch-off the output is already low. None of these is a DC step: the output is a two-level square wave either way, and the step from silence to a full-amplitude tone, which the K4 envelope exists to soften, is the same with or without the forced wrap.

**What the "gate" of REQ-SW-KEYER-033 is, and where the rest of K4 is allocated.** REQ-SW-KEYER-033 asks the keyer firmware to assert the sidetone *gate* within 1 ms of key-down, verified by HostUnit on the simulated clock (TC-SW-KEYER-033). The gate is the keyer's command to the sidetone path, the `SW-KEYER` output that `SW-AUDIO` acts on; it is not the audible tone. This driver contributes the last link, from the `set_enabled(true)` call to the first PWM edge, at most 1.71 µs, which leaves the 1 ms of K4 and the 4 ms of REQ-SYS-159 to the keyer and audio logic. The rest of HZ-005 K4 is not met by this driver and is allocated to `SW-AUDIO` (07 section 14.2 row `SW-AUDIO`: ramps, sidetone amplitude limit, fault mute), decided with the audio path by TS-010 (WP-PDR-25) and written as `SW-AUDIO` requirements by WP-PDR-35:

- the 3 to 5 ms sidetone envelope: a square tone from this driver has two levels only, and a duty ramp through `set_duty` steps once per tone period (1.43 ms at 700 Hz, 3.33 ms at 300 Hz), too coarse for a 3 to 5 ms envelope at low tones; TS-010 decides between a PWM carrier at an ultrasonic rate written per sample (the revisit condition of section 7), an analogue envelope stage, or another source;
- "no DC step at any transition" and the K5 condition that the amplifier is enabled only after the source "idled at mid-scale": `CC = 0` (PWM-4, PWM-5) is this driver's defined off level, a constant low, not a mid-scale idle, and not itself an HZ-005 click control; the audio path of TS-010 removes the DC step or `SW-AUDIO` idles the source at mid-scale;
- the safe-state and fault mute of `SW-AUDIO` (a PA fault or SafeState mutes within 10 ms, items j and l): the driver mutes within 1.71 µs of `set_enabled(false)`, so the 10 ms budget is left to the handler path; whether the safe-state mute also de-asserts the amplifier enable of K5 (hardware, CTL, `ICD-CTL-PHONES` section 3.2.6) is a `SW-AUDIO` and ICD decision of WP-PDR-32 and WP-PDR-36, not of this driver.

These allocations are AT RISK on TS-010, which has not selected the audio path. The dev-board check of section 4.3 measures the switching latency; the audible onset and envelope are measured by the closing Bench case of the `SW-AUDIO` and keyer requirements. TC-SW-KEYER-039 adds "the PWM carrier period" to its tolerance, which assumes a carrier this design does not have; with this design the added term is one counter step (≤ 1.71 µs), and the case is reported to its writer (WP-PDR-35) as a cross item.

## 3. Alternatives considered

| Option | Description | Why not chosen (or why chosen) |
|---|---|---|
| A (chosen) | One output per slice; smallest divider for the finest period resolution; off as `CC = 0` with the slice running; on and off forced to the next count by `CTR = TOP` (revision 2) | A frequency change can never move another output; off is a hardware-guaranteed low within one count, with no DC held high; the one period cut short at switching is argued in section 2.1. The envelope and the DC-step and mid-scale controls of HZ-005 K4 and K5 are not provided by this option and are allocated to `SW-AUDIO` (section 2.1) |
| B | Both channels of a slice usable, with a shared frequency | The second output's frequency would change whenever the first is retuned; cwht needs two outputs on two slices anyway |
| C | Off by clearing `CSR.EN` | The counter freezes and the output holds whatever level it had, possibly high; a pending `CC = 0` would never latch |
| D | Phase-correct mode | Halves the frequency resolution for no benefit to a tone or a backlight |
| E | Do nothing | No sidetone on the keyer prototype; FM-4 and the owner's HSI verdict (OD-22) wait |

## 4. Consequences

### 4.1 Requirements created or changed

| Requirement | Relationship | Note |
|---|---|---|
| none | | The sidetone frequency range and level policy are SW-AUDIO requirements after TS-010 (WP-PDR-25 and WP-PDR-35) and may cite this ADR for the 0.1 % frequency accuracy and the glitch-free off |

### 4.2 Interfaces, design and code

- ICDs affected: none of cwht's; ICD-CTL-SW (WP-PDR-36a) assigns the sidetone and backlight pins, on different slices. rustos gains `docs/icd/rp2350/pwm/`.
- Design elements: rustos `api/src/pwm/mod.rs`, `api/tests/pwm_contract.rs` (new); `firmware/pico2/src/pwm/{mod.rs, pwm.rs, tests.rs, pwm_tests.rs}` (new); `firmware/pico2/src/common/reg.rs` (`RegAddr::PWM`), `common/board.rs` (device `pwm`), `lib.rs` (module list). cwht side: the `SW-AUDIO` sidetone generation of `cwht-core` drives `impl PwmOutput`; the keyer's sidetone gate becomes `set_enabled`.
- New `SW-<SUB>` modules: none. ICDs created: none (cwht).

### 4.3 Verification and safety

- Evidence at revision 2 (`48e07ec`; author runs, 2026-09-27): `release` asserts the reset (set alias) before the release (clear alias), with a host test of the whole access order (set, clear, `RESET_DONE` poll, `EN`) and one from a warm start in which `RESETS` shows PWM out of reset; `update_on` writes `CTR = TOP` after `CC` on every on/off change and never for a duty change alone, each with a host test (the writes of revision 1 fail both); the frequency-change and refused-frequency tests account for the switch-on writes. 101 `pico2` host tests pass natively and under Miri; the `api` contract tests pass with the PWM-4 and PWM-6 wording of revision 2; dev and release target builds without warnings; complexity gate and unsafe audit pass (ADR-051 section 4.3). The PWM ICD `01_overview.md` bring-up order gains the reset assert and the on/off step. The scratch composition application of revision 1 was not rebuilt at revision 2.
- Evidence at revision 1 (`6df18af`; author runs, 2026-09-27): 23 new host tests (18 in `pico2`: the 700 Hz and 20 kHz settings; every audio frequency from 100 Hz to 3 kHz in 7 Hz steps within 0.1 % and inside the divider and period ranges; 0 Hz; the 9 Hz and 8 Hz divider edge; the two-count 75 MHz edge; an inexact 7 MHz refused; duty rounding and both ends; off always 0; the release sequence and its timeout; the attach order with `CC = 0` before `FUNCSEL` and isolation released last; a claimed slice refused before any write; the Table 1129 mapping at pins 0, 15, 16, 25, 29; duty and off writing only `CC` in the right half; a frequency change keeping the duty; a refused frequency changing nothing; 5 contract tests in `api`), all passing natively and under Miri; target build without warnings; complexity gate passes; no new `unsafe` site. A scratch application built against the branch tip composes all five work packages (clocks, NVIC, TIMER0 alarm handler, input snapshot, 700 Hz PWM tone gated by the key input) and links for `thumbv8m.main-none-eabihf` (5 980 bytes of text).
- Mock in `cwht-hal-mock`: a recording `PwmOutput` (frequency, duty, on/off history), written after this ADR's review, against PWM-1 to PWM-6.
- Dev-board check: `firmware/devcheck/src/bin/pwm_check.rs` by the independent test author, report `docs/vv/reports/devcheck-pwm-r1.md` (`credit: false`): a 700 Hz tone at 50 % on the development board into headphones through the FM-4 wiring, keyed on and off by the key input; the owner hears the tone start and stop without a click; the pitch is compared with a 700 Hz reference tone (for example a phone tone generator) by ear, and any frequency measurement made is recorded with its instrument. Added at revision 2: the switching latency, a GPIO marker driven just before `set_enabled(true)` and `set_enabled(false)` and the first PWM edge (or the last) captured at 1 MS/s with the Pico-based logic capture, at 100 Hz, 700 Hz and 3 kHz, each within 5 µs over 100 switchings; and a restart case, the tone left running, a watchdog reset whose scope excludes PWM (and a debugger reset), then the PWM pin read low from the new boot until its output is attached.
- ACC-EMU-001: PWM is outside the candidate emulator's peripheral scope unless the emulator ADR says otherwise; the host golden sequence stands as the reference.
- Hazard analysis update required: no new hazard, cause or control; revision 2 states this driver's share of HZ-005 C2 (every start from the PWM reset state) and of K4 (switching latency), and the allocation of the rest of K4 and of the K5 mid-scale idle to `SW-AUDIO` under TS-010 (section 2.1), which the hazard-analysis writer (WP-PDR-16b) may cite. Safety-critical software scope changed: no. SWE-134 a (known state at first start and at restarts, revision 2), c (off to a known low state), g (the achieved frequency is computed and reported, and an inexact one refused) and k (every refusal is an error, with state unchanged).

### 4.4 Cost, schedule, risk

- BOM and lead time: none. Gate: PDR (FW-B1; FM-4 sidetone). RSK-013: the fifth of the five minimal-keyer packages. TPMs: none.

## 5. Compliance and tailoring

None.

## 6. Decision record (the decision memo for this decision, charter section 4)

Not decided. Proposed memo wording (Form 1): "Owner (date): I merge rustos branch `cwht/wp-sw-03` as reviewed, and ADR-055 is Accepted."

## 7. Related

- Supersedes: none. Superseded by: none.
- Trade study: TS-002 (see ADR-051 section 7); TS-010 (audio chain and display, WP-PDR-25) decides the sidetone path the output feeds
- Related ADRs: ADR-011, ADR-019, ADR-027, ADR-051 (`ClocksReady`, `Regs`), ADR-053, ADR-054
- Review where presented: PDR
- Revisit conditions: TS-010 selects an audio path that needs PWM at a sample rate (then the double-buffered `CC` is written per sample from an interrupt or DMA, a new work package); the pin map needs two outputs on one slice; the dev-board check shows the forced wrap does not latch the new `CC` within 5 µs

## 8. Revision history

| Revision | Date | rustos commit | Change | Review |
|---|---|---|---|---|
| 1 | 2026-09-27 | `6df18af` | First issue | INSP-099 iteration 1 (NEEDS CHANGES, finding-1 Major); INSP-105 (assurance NEEDS CHANGES, its finding-1 Major and the concurred INSP-099 finding-1) |
| 2 | 2026-09-27 | `48e07ec` (after merging `cwht/wp-sw-02` at `38434b2`) | INSP-099 finding-1: on/off forced to the next count (`CTR = TOP`), the latency of every operation stated against frequency, the click effect argued, the REQ-SW-KEYER-033 gate defined as the keyer's command, and the K4 envelope and DC step and the K5 idle allocated to `SW-AUDIO` under TS-010 (section 2.1); PWM-4 reworded. INSP-105 finding-1: `release` asserts the PWM reset before releasing it; PWM-6 covers restarts (sections 2 and 4.3). Minor findings of INSP-099 and INSP-105 are not addressed in this revision (plan rule C1), although section 2.1 states the level allocation that INSP-105 finding-2 also asks for | INSP-099 and INSP-105 iteration 2 (delta) |
