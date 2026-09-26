# ADR-019: New peripheral drivers are developed upstream in rustos, not in a cwht-local HAL crate

| Field | Value |
|---|---|
| ID | ADR-019 |
| Status | Accepted |
| Date proposed | 2026-09-25 |
| Date decided | 2026-09-25 |
| Decision class | 1 (`docs/process/06-risk-and-decision-analysis.md` section 14.1 items (h) runtime and HAL acquisition versus development, SWE-033; (c) the `pico2` drivers are in 07 section 14.1). Owner-directed (SI-033). Trade study: TS-002 (Draft) |
| Decision authority | Robin (owner and rustos maintainer; the decision fixes the software architecture and the rustos dependency) |
| Author | Claude (technical data manager invocation, 2026-09-25) |
| Independent reviewer | INSP-011 (`docs/reviews/SRR/checklists/adrs-001-to-025.md`): iterations 1 and 2 (2026-09-25) NEEDS CHANGES, findings F-01, F-03 and F-10 against this file; the Major-finding corrections are applied here on 2026-09-26 (section 8); verification pending at INSP-011 iteration 3 |
| Life-cycle phase | Pre-A / A |
| Baseline affected | baseline/srr (functional baseline; software plan); allocated baseline at PDR (architecture) |
| Change request | none (pre-baseline) |

## 1. Context

rustos today provides boot, vector table, reset handler, linker script, board definition and a GPIO driver. cwht needs clocks and PLL, TIMER0 alarms, NVIC and critical sections, I2C, SPI, ADC, PWM, watchdog, non-volatile flash storage and, if the audio trade selects an I2S DAC, a PIO I2S driver. They could be written in a cwht-local `pico2-ext` crate or upstream in rustos `api` and `pico2`. The owner ruled: upstream in rustos (SI-033).

- Driving inputs and expectations: SI-033 (second sentence), SI-007 (Rust on rustos), SI-026 (host-first through `api` traits), SI-025 (open source)
- Requirements that constrain the decision: none yet
- Hazards in play (`docs/safety/hazards.json` 0.4.0-pha): HZ-004 (the timer, watchdog and GPIO drivers sit under the keyer and PA enable) and the hazards whose firmware controls run on the GPIO, TIMER, PWM, ADC, watchdog, critical-section and clock drivers: HZ-001 to HZ-008, HZ-010, HZ-011, HZ-012 and HZ-014
- Research consulted: `docs/research/rustos-toolchain-proof.md` F7 (what `api` provides), F8 (what `pico2` provides and the gaps), F9 (address map, reset bits and IRQ numbers per peripheral), F10 (the keyer timebase needs a clock driver that does not exist), F15 (bootrom flash API for configuration), F16 (rustos hygiene items), "Driver extension map", "Work-package table" WP-01 to WP-14, DECISION "where new drivers live: extend rustos upstream (recommended)", DECISION "injectable register-access trait", open item 5; `docs/research/emulator-accreditation-and-timer-irq.md` F12 (peripheral coverage matrix against the work packages); `docs/process/07-software-engineering-plan.md` section 3.4 (sprint structure), 3.5 (file inventory per work package), 17.1 (third-party register: rustos as path dependency pinned in the VDD), 17.2 (make/buy TS, SWE-033), 19 (WP-SW-01 to WP-SW-13), 21 (software risks: rustos driver effort, single maintainer); `docs/process/05-configuration-and-data-management.md` OQ-5 (pinning method decided at PDR)
- Guidance consulted: SWE-033 (acquisition versus development), SWE-027 (third-party register), SWE-146 (auto-generated code: none; registers hand-written with citations), SWE-057, SWE-058; SE HB §6.8
- Assumptions the decision rests on, and how and by when each is confirmed:
  1. The owner, as rustos maintainer, merges the work-package pull requests on the schedule. Tracked by the 07 section 21 risk "rustos driver effort" (RSK-013), reviewed at PDR.
  2. The pinned path dependency is reproducible. Confirmed by the OQ-CM-005 ADR at PDR.

## 2. Decision

Every new peripheral driver cwht needs is developed upstream in rustos: the trait in `rustos/api`, the implementation in `rustos/firmware/pico2` with a datasheet citation on every register access, contract tests, and a dev-board check, delivered as reviewed pull requests that the owner merges as rustos maintainer. The work packages are those of 07 section 19 (clocks and PLL, TIMER0 alarms, NVIC and critical sections, I2C, SPI, ADC, PWM, watchdog, flash store, UART, and optional PIO I2S), each run as a sprint of 07 section 3.4 with the file inventory of 3.5 and proposed as its own ADR in cwht when its trait shape is fixed. cwht-local code is limited to `cwht-core` (application logic), `cwht-app` (target binary), `cwht-hal-mock` (host implementations of the traits) and `firmware/emu` (scenarios); no cwht-local HAL or register crate exists. cwht consumes rustos as a path dependency with the commit recorded in the lock file and in every VDD (the CM plan's OQ-5 default; conversion to a git dependency or submodule is decided at PDR). No SVD-generated peripheral access crate is used.

## 3. Alternatives considered

| Option | Description | Why not chosen (or why chosen) |
|---|---|---|
| A (chosen) | Upstream in rustos via reviewed PRs; pinned commit in cwht | Owner direction (SI-033); one HAL, one audit trail, benefits the owner's other rustos users; matches the zero-external-crate policy |
| B | cwht-local `pico2-ext` crate | Rejected: two HALs for one chip; duplicates rustos conventions; drivers under the keyer would live outside the owner's OS |
| C | Third-party HAL (rp-hal, Embassy, RTIC) | Rejected by SI-007 and the zero-external-runtime-crate policy; recorded in TS-002 (`docs/decisions/trade-studies/TS-002-firmware-runtime-make-buy.md`, Draft; decided at SRR; its decision becomes a new ADR) (SWE-033) |
| D | Generate a PAC with `svd2rust` | Rejected: rustos house style is hand-written registers with citations; the SVD would become an unreviewed input (07 section 17.4) |

TS-002 (`docs/decisions/trade-studies/TS-002-firmware-runtime-make-buy.md`, Draft; decided at SRR; its decision becomes a new ADR), the make/buy record of 07 section 17.2, records the cost of this choice (the work packages) and its benefit (complete audit).

## 4. Consequences

### 4.1 Requirements created or changed

| Requirement | Relationship | Note |
|---|---|---|
| REQ-SYS-127 (firmware language and platform) | allocated; cites this ADR | Drivers implemented in rustos `pico2` behind `api` traits, no cwht-local register access; Inspection (`cargo tree`, module list) |
| REQ-SW-HAL-* (trait contracts per peripheral) | not created: written at PDR with each work-package ADR | Contract tests against mock and dev board |

### 4.2 Interfaces, design and code

- ICDs affected: the RP2350 datasheet sections cited per driver are the hardware ICD (ADR-011); rustos `docs/icd/rp2350/` extractions for TIMER, PWM, ADC, WATCHDOG and QMI are added by the work packages
- Design elements created or changed: rustos `api` traits (time, bus, pwm, adc, watchdog, nv, irq), `pico2` drivers, `cwht-hal-mock` mocks; cwht `Cargo.toml` path dependency and lock
- New `SW-<SUB>` modules created by this ADR: none
- ICDs created by this ADR: none

### 4.3 Verification and safety

- Verification cases to add or change: contract tests per trait (HostUnit against the mock), dev-board check binaries (`credit: false`), emulator accreditation entry per peripheral (accredited or not)
- Evidence class implications: driver-to-datasheet traceability is Inspection evidence (charter section 9); the unsafe audit covers every `pico2` driver
- Hazard analysis update required: no (the hazard records already name the runtime components)
- Safety-critical software scope changed: no; the timer, watchdog and GPIO drivers are in the safety-critical call path and get the same rigor

### 4.4 Cost, schedule, risk

- Cost: none in parts; effort of about twelve work packages before PDR and CDR on the compressed schedule (07 section 21 risk "rustos driver effort"); PDR liens permitted
- Gate affected: PDR (WP-01 to WP-04, WP-09, WP-11 needed for the keyer prototype), CDR (remaining)
- Risks opened, closed or re-scored: 07 section 21 risks "rustos driver effort" and "single maintainer of rustos" are to be opened in the register by the software lead; mitigation: ordering by need, contract tests on every rustos change, pinned commit
- TPMs affected: TPM-010, TPM-011 (flash and RAM margins) once drivers exist

## 5. Compliance and tailoring

RMM row SWE-027 register text changes to "zero external runtime crates" (07 section 22 CR request at SRR); SWE-146 row changes to `build.rs` constant tables only; SWE-033 is satisfied by TS-002 (`docs/decisions/trade-studies/TS-002-firmware-runtime-make-buy.md`, Draft; decided at SRR; its decision becomes a new ADR). Recorded by the CR named in 07 section 22.

## 6. Decision record

> Owner (2026-09-25, SI-033, second sentence): "New peripheral drivers are developed upstream in rustos (the owner's OS), not in a cwht-local crate."

Transcribed from chat into `stakeholder-inputs.md`.

## 7. Related

- Supersedes: none
- Superseded by: none
- Trade study: TS-002 (`docs/decisions/trade-studies/TS-002-firmware-runtime-make-buy.md`, Draft; decided at SRR; its decision becomes a new ADR), the firmware runtime and HAL make/buy (SWE-033, 07 section 17.2)
- Review where presented: SRR; per-work-package ADRs at PDR
- Revisit conditions: the owner as rustos maintainer declines an `api` addition (then that trait lives in `cwht-core` as an application-level abstraction over an existing rustos trait, not in a new HAL crate); the pinning method changes at PDR (OQ-5)

## 8. Change log

- 2026-09-26: one-time pre-baseline correction under INSP-011 ruling R-1 option (A), as directed by the lead SE: Decision class row and section 1 Assumptions line added (F-01); hazard line and "Hazard analysis update required" re-derived against `docs/safety/hazards.json` 0.4.0-pha (F-02); section 4.1 placeholder ids replaced by the ids the requirement authors allocated, or marked not created with the reason (F-03); trade study references resolved to TS-002 (F-03, erratum E-9). Content from `reconciliation-srr.md` sections 2, 3, 5.1 and 6, re-checked against the requirement, hazard and expectation files of 2026-09-26; that register is superseded by this file for this ADR. The decision of section 2 is unchanged. Minor findings are liens, fixed before PDR: F-10 (erratum E-8, the work-package numbering of sections 1 and 7). The edit of an Accepted ADR rests on the owner's approval of R-1 (A) in the SRR decision memo and the matching sentence in `docs/process/05-configuration-and-data-management.md` Table 4-1 row 13 (both pending). Class 1 choices without a trade study wait on ruling R-2 (owner). Author: Claude (ADR author invocation).
