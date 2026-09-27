# ADR-055: WP-SW-03 PWM output: `api::pwm::PwmOutput` on rustos slices 0 to 7, one output per slice, frequency within 0.1 %, glitch-free duty and off

| Field | Value |
|---|---|
| ID | ADR-055 |
| Status | Proposed (for the owner's review and merge of rustos branch `cwht/wp-sw-03` as rustos maintainer, OD-23; FW-B1) |
| Date proposed | 2026-09-27 |
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

rustos gains, on branch `cwht/wp-sw-03` at commit `6df18af` (on `cwht/wp-sw-02`):

1. **`api::pwm`**: `Duty` in parts per thousand (0 to 1000; `OFF`, `HALF`, `FULL`) and `PwmOutput` with `set_frequency_hz(hz) -> Result<u64, Error>` (the achieved frequency in millihertz), `set_duty(Duty)` and `set_enabled(bool)`. Contract clauses PWM-1 (achieved within 0.1 %), PWM-2 (refused frequency changes nothing), PWM-3 (duty survives frequency changes), PWM-4 (off holds low from the next period; on restores the duty), PWM-5 (0 ‰ constant low, 1000 ‰ constant high) and PWM-6 (a new output is off) are in the module documentation and checked by `api/tests/pwm_contract.rs`, with three faulty models detected.
2. **`pico2::pwm`**: `Rp2350Pwm::new(handle, &ClocksReady, &Rp2350Gpio)` releases PWM from reset (bounded wait) and clears every slice enable; it takes `clk_sys` from `ClocksReady` and borrows the GPIO port as proof that `IO_BANK0` and `PADS_BANK0` are out of reset. `output_from_handle::<N>(pin)` maps GPIO `N` to slice `(N / 2) mod 8` and channel `N mod 2` at compile time (Table 1129; `N >= 30` does not compile), refuses a slice whose other channel is already an output (`PwmError::SliceInUse`), then configures the slice with `CC = 0` and starts it before it switches `FUNCSEL` to 4 and clears the pad `OD` and `ISO` bits (isolation last), so the pin comes up low. Frequency: the smallest divider that fits the period in `TOP <= 65534` (so that `CC = TOP + 1`, 100 %, still fits the 16-bit `CC` field), the period rounded to the nearest count, and a refusal (`PwmError::FrequencyOutOfRange`) for 0 Hz, anything outside the divider and period ranges, and any result more than 0.1 % off. Duty is rounded to counts; off is `CC = 0` with the slice running. `CC` and `TOP` are double-buffered by the hardware (section 12.5.2.3), so duty and off changes land at the next wrap with no partial pulse; `DIV` is not buffered, so a frequency change can alter the one period in progress. PWM interrupts are not used. `timing` and `cc_value` are pure functions; the sequences are generic over the `Regs` capability of ADR-051.
3. **Register ICD**: `docs/icd/rp2350/pwm/` (index, overview and programming model, register map) extracted from datasheet section 12.5, and a row in `docs/icd/rp2350/index.md`.

For the 700 Hz sidetone at `clk_sys` = 150 MHz the driver writes `DIV` = 53/16 (3.3125) and `TOP` = 64 689, giving 700.0003 Hz; for a 20 kHz backlight, `DIV` = 1 and `TOP` = 7 499, exactly 20 kHz.

## 3. Alternatives considered

| Option | Description | Why not chosen (or why chosen) |
|---|---|---|
| A (chosen) | One output per slice; smallest divider for the finest period resolution; off as `CC = 0` with the slice running | A frequency change can never move another output; off is a hardware-guaranteed low from the next wrap, with no DC held high and no partial pulse (HZ-005 clicks) |
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

- Evidence at the branch commit (author runs, 2026-09-27): 23 new host tests (18 in `pico2`: the 700 Hz and 20 kHz settings; every audio frequency from 100 Hz to 3 kHz in 7 Hz steps within 0.1 % and inside the divider and period ranges; 0 Hz; the 9 Hz and 8 Hz divider edge; the two-count 75 MHz edge; an inexact 7 MHz refused; duty rounding and both ends; off always 0; the release sequence and its timeout; the attach order with `CC = 0` before `FUNCSEL` and isolation released last; a claimed slice refused before any write; the Table 1129 mapping at pins 0, 15, 16, 25, 29; duty and off writing only `CC` in the right half; a frequency change keeping the duty; a refused frequency changing nothing; 5 contract tests in `api`), all passing natively and under Miri; target build without warnings; complexity gate passes; no new `unsafe` site. A scratch application built against the branch tip composes all five work packages (clocks, NVIC, TIMER0 alarm handler, input snapshot, 700 Hz PWM tone gated by the key input) and links for `thumbv8m.main-none-eabihf` (5 980 bytes of text).
- Mock in `cwht-hal-mock`: a recording `PwmOutput` (frequency, duty, on/off history), written after this ADR's review, against PWM-1 to PWM-6.
- Dev-board check: `firmware/devcheck/src/bin/pwm_check.rs` by the independent test author, report `docs/vv/reports/devcheck-pwm-r1.md` (`credit: false`): a 700 Hz tone at 50 % on the development board into headphones through the FM-4 wiring, keyed on and off by the key input; the owner hears the tone start and stop without a click; the pitch is compared with a 700 Hz reference tone (for example a phone tone generator) by ear, and any frequency measurement made is recorded with its instrument.
- ACC-EMU-001: PWM is outside the candidate emulator's peripheral scope unless the emulator ADR says otherwise; the host golden sequence stands as the reference.
- Hazard analysis update required: no. Safety-critical software scope changed: no. SWE-134 c (off to a known low state), g (the achieved frequency is computed and reported, and an inexact one refused) and k (every refusal is an error, with state unchanged).

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
- Revisit conditions: TS-010 selects an audio path that needs PWM at a sample rate (then the double-buffered `CC` is written per sample from an interrupt or DMA, a new work package); the pin map needs two outputs on one slice
