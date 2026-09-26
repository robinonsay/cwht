# ADR-011: Host-first software verification through rustos api traits; emulation optional and never for timing

| Field | Value |
|---|---|
| ID | ADR-011 |
| Status | Accepted |
| Date proposed | 2026-09-25 |
| Date decided | 2026-09-25 |
| Decision authority | Robin (owner; the decision fixes the software architecture and the primary evidence class) |
| Author | Claude (technical data manager invocation, 2026-09-25) |
| Independent reviewer | Pending: reviewer agent invocation before SRR (01 section 3.2 row S3; 06 section 14.2) |
| Life-cycle phase | Pre-A / A |
| Baseline affected | baseline/srr (functional baseline; the V&V plan is baselined at PDR) |
| Change request | none (pre-baseline) |

## 1. Context

SI-010 demands that the radio work at first power-on with the proof done beforehand. For firmware the candidates were whole-binary emulation, host testing of application logic, and dev-board checks. Two studies showed the RP2350 emulators available on macOS do not model seconds (cycle counts consistent, wall time not), lack GPIO edge interrupts and NVIC priorities at the pinned commit, and are single-maintainer projects; they also showed that rustos `api` traits already allow application logic to compile unchanged for the host with mocked drivers. The owner directed the approach in SI-026.

- Driving inputs and expectations: SI-026, SI-010, SI-007, SI-015 (Class A evidence), SI-018 (keyer timing is the first customer)
- Requirements that constrain the decision: none yet
- Hazards in play: HZ-004 (keyer and PA enable are safety-critical software whose tests must be repeatable)
- Research consulted: `docs/research/rustos-toolchain-proof.md` F2 (`cargo test -p api` exercises nothing today), F7, F8 (what `api` and `pico2` provide and lack), F13 (host tests against `api` with mocked GPIO work; a portable `Clock` trait is the missing piece), "Driver extension map", "Host-side testing fit"; `docs/research/rp2350-emulation-options.md` A to D (Wokwi, Renode, QEMU, rp2040js lineage), "Recommendation" (c1570/rp2350js ARM mode), REQ-candidate "timing verified by Bench, not Emulation"; `docs/research/emulator-accreditation-and-timer-irq.md` F5 (cycles consistent, seconds not), F6 (TIMER0 alarm IRQ works), F8 (GPIO edge IRQs mis-decoded), F9 (NVIC priority registers at wrong offsets), F10 (PWM slices 0 to 7 only), F12 (coverage matrix), F13 (accreditation case `ACC-EMU-001`, event-ordering scope); `docs/research/keyer-verification-and-key-input-network.md` F8 (simulated-clock HostUnit harness at 0.1 ms), F9 (emulation restricted to event ordering)
- Guidance consulted: SWE-062, SWE-186 (repeatable unit tests), SWE-073 (validation on target or high-fidelity simulation, limited to accredited scope), SWE-136 (tool accreditation), SWE-187, SWE-211; NPR 7150.2D §3.12.1 Table 1 (design components to code traceability); SE HB §6.8

## 2. Decision

Application logic lives in a `no_std` crate (`cwht-core`) that depends only on the rustos `api` traits and receives every device through dependency injection (generics or trait objects). The same code runs on the macOS or Linux host against a host implementation of the traits (`cwht-hal-mock`, with a simulated clock) and on the Cortex-M33 against rustos `pico2`. HostUnit (host `cargo test` with mocked devices and a simulated clock) is the primary Test evidence for every software requirement that is platform-independent logic, including keyer timing at 0.1 ms resolution on the simulated clock. Drivers are traced to the RP2350 datasheet and the Cortex-M33 documentation as the hardware ICD: every register access in a rustos driver cites the section it implements, checked by Inspection. Hardware integration (real timing, peripherals, interrupts, clocks, power states) is verified on real hardware (Bench on the delivered unit; dev-board checks are risk reduction with `credit: false`). Emulation is optional and secondary: whole-binary scenarios assert event ordering in TIMER0 microseconds and never durations, frequencies or timeouts; credit is limited to the peripherals listed in the accreditation record (`ACC-EMU-001` proposed at PDR: boot, Cortex-M33 execution, TIMER0 alarms and NVIC entry, SIO GPIO, UART0, I2C0 and SPI0 byte streams, ADC plumbing, PWM slices 0 to 7, ordering). Firmware design rules that follow: a single NVIC priority level with run-to-completion handlers, PWM on slices 0 to 7 with per-slice enable, GPIO through SIO only, inputs sampled from the timer alarm.

## 3. Alternatives considered

| Option | Description | Why not chosen (or why chosen) |
|---|---|---|
| A (chosen) | Host-first through `api` traits; hardware on hardware; emulation optional for ordering | Owner direction (SI-026); repeatable, fast, MC/DC-measurable on the host; the proof crate already works (F13) |
| B | Emulation-first (whole binary as primary evidence) | Rejected: seconds are not modelled (F5), GPIO edge IRQs and NVIC priorities missing (F8, F9), single maintainer; would credit timing the emulator cannot show |
| C | Hardware-first on the owner's Pico 2 dev board | Rejected as primary: no logic capture without a second board, not repeatable in CI, contrary to SI-010's "proven beforehand"; kept as `credit: false` dev-board checks |
| D | HAL-coupled application code without an abstraction layer | Rejected: untestable on the host; contrary to SI-026 |

No trade study: the owner's direction fixed the approach; the emulator selection (rp2350js versus Renode) is the ADR due at PDR named in `docs/process/04-verification-and-validation.md` section 4.

## 4. Consequences

### 4.1 Requirements created or changed

| Requirement | Relationship | Note |
|---|---|---|
| REQ-SW-NNN (application logic depends only on `api` traits; no direct register access outside rustos `pico2`) | new, self-derived from this ADR | Inspection (dependency graph, `cargo tree`) |
| REQ-SW-NNN (every `pico2` register access cites the RP2350 datasheet or Cortex-M33 document section) | new, self-derived from this ADR | Inspection; driver-to-datasheet traceability (charter section 9) |
| REQ-SW-NNN (emulation scenarios assert ordering only; timing requirements carry Bench or HostUnit-with-simulated-clock methods) | new, V&V plan rule | `emulator-accreditation-and-timer-irq.md` REQ-candidates |
| REQ-SW-NNN (single NVIC priority; PWM slices 0 to 7; GPIO via SIO) | new, self-derived design rules | 07 coding standard rows |
| REQ-SW-NNN (clock driver enables TICKS explicitly and bounds XOSC and PLL waits with a fault path) | new, self-derived | F3, F5 of the accreditation study |

### 4.2 Interfaces, design and code

- ICDs affected: the RP2350 datasheet and Cortex-M33 documentation are the hardware ICD for drivers (no project ICD file; cited by section)
- Design elements created or changed: crates `cwht-core`, `cwht-app`, `cwht-hal-mock`, `firmware/emu` (07 section 1.2); software architecture record (SWE-057) at PDR
- New `SW-<SUB>` modules created by this ADR: none (module names come from the architecture ADR)
- ICDs created by this ADR: none

### 4.3 Verification and safety

- Verification cases to add or change: HostUnit cases for every platform-independent `REQ-SW-*`; `TC-SW-COV-001` (coverage and complexity), `TC-SW-REG-001` (regression); Emulation cases only where `tools/toolchain.lock.md` accredits the peripheral
- Evidence class implications: HostUnit primary; Emulation secondary with `ACC-EMU-001` scope; Bench for target timing; the 04 section 5.2 credit table already encodes these limits
- Hazard analysis update required: no
- Safety-critical software scope changed: no; MC/DC on safety-critical components is measured on the host (07 section 9.6)

### 4.4 Cost, schedule, risk

- Cost: none in parts; effort in `cwht-hal-mock` and the rustos work packages (ADR-019)
- Gate affected: PDR (V&V plan, software architecture, emulator ADR), CDR (first coverage measurement)
- Risks opened, closed or re-scored: RSK-003 (emulator does not model peripherals) is reduced in consequence because emulation is no longer primary; risk "emulator fidelity" of 07 section 21 stays; new risk proposed: "host mock diverges from silicon behaviour" (control: contract tests run against mock and dev board)
- TPMs affected: none directly

Open reconciliation item: `docs/process/07-software-engineering-plan.md` section 17.1 names `rp2350-emu` (picoem) 0.2.6 as the emulator while the accreditation study proposes c1570/rp2350js at commit `af0114cb` as `ACC-EMU-001`; the PDR emulator ADR resolves which tool the register lists.

## 5. Compliance and tailoring

RMM rows SWE-073 (high-fidelity simulation limited to accredited scope), SWE-136, SWE-062, SWE-186, SWE-187, SWE-211 are satisfied by this approach as written in 04 and 07; no new tailoring.

## 6. Decision record

> Owner (2026-09-25, SI-026): "Software verification approach: layer the software with dependency injection on the rustos api traits so the same application code runs on a macOS/Linux host implementation and on the Cortex-M33; test application logic on the host; test hardware integration on real hardware. Drivers are traced to the RP2350 datasheet and Cortex-M33 documentation as the hardware ICD. Emulation is optional, not the primary evidence."

Transcribed from chat into `stakeholder-inputs.md`.

## 7. Related

- Supersedes: none
- Superseded by: none
- Trade study: firmware runtime and HAL make/buy TS (SWE-033); emulator selection ADR at PDR
- Review where presented: SRR
- Revisit conditions: an emulator gains validated timing (then Emulation may take timing credit by a superseding ADR and a widened accreditation scope); the host mock is shown to diverge from silicon on a credited behaviour
