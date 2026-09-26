# ADR-004: Raspberry Pi Pico 2 module as controller, with its micro-USB for programming and charging

| Field | Value |
|---|---|
| ID | ADR-004 |
| Status | Accepted |
| Date proposed | 2026-09-25 |
| Date decided | 2026-09-25 |
| Decision authority | Robin (owner; the decision fixes the controller and the only external data and charge connector) |
| Author | Claude (technical data manager invocation, 2026-09-25) |
| Independent reviewer | Pending: reviewer agent invocation before SRR (01 section 3.2 row S3; 06 section 14.2) |
| Life-cycle phase | Pre-A / A |
| Baseline affected | baseline/srr (functional baseline, to be tagged at SRR) |
| Change request | none (pre-baseline) |

## 1. Context

The owner directed the Raspberry Pi Pico 2 (RP2350) as the controller with firmware in Rust on the owner's `rustos` (SI-007), and a single connector: the module's own micro-USB for firmware loading and battery charging (SI-022). The choice fixes the CPU (Cortex-M33, `thumbv8m.main-none-eabihf`), the bootloader path (BOOTSEL UF2), the pin budget, the USB power budget for charging a 2S pack, the assembly category of the module, and two clock harmonics that land on 144.000 MHz.

- Driving inputs and expectations: SI-007, SI-022, SI-011 (Claude produces everything), SI-026 (host-first software), SI-031 (owner solders modules with exposed pads)
- Requirements that constrain the decision: none yet
- Hazards in play: HZ-002 (charging through the module connector), HZ-004 (firmware image integrity through the USB loader)
- Research consulted: `docs/research/rustos-toolchain-proof.md` F1 to F5 (host build, cross build, UF2 conversion all work), F11 (RP2350-E9: no internal pull-downs on A2 silicon), F14 (pin budget fits with margin), F15 (bootrom flash API for configuration); `docs/research/pcbway-fabrication-and-assembly.md` F16 (Pico 2 as a castellated SMT module: recommended footprint, paste zones 163 percent, no Pico 2 KiCad footprint yet, no published PCBWay policy for reflowing it); `docs/research/power-tree-and-charging.md` F1 (USB 2.0: 500 mA configured; BC1.2 DCP 1.5 A), F2 (micro-B contacts about 1.8 A; Pico 2 publishes no rating for its connector or VBUS copper), F3 (500 mA gives about 280 mA charge, about 10 h to full), F4 (BQ25887 PSEL default 500 mA; DCP detection via USBPHY_AS_GPIO unverified); `docs/research/display-and-ui-parts.md` baseline row "USB" (12.0 x 10.0 mm wall opening); `docs/research/emulator-accreditation-and-timer-irq.md` F13 (A2 bootrom embedded in the emulator; owner boards may be A3 or A4)
- Guidance consulted: SWE-063 (version description records the image hash), SWE-134 (safe state before any output); SE HB §6.8

## 2. Decision

The controller is the Raspberry Pi Pico 2 module (ordering code SC1631, RP2350 in ARM mode, 4 MB flash) mounted as a castellated surface-mount module on the main board; the firmware is Rust on `rustos` with zero external runtime crates. The module's micro-B connector is the only USB connector on the radio: it loads firmware through the RP2350 bootrom (BOOTSEL, UF2, `picotool`) and it supplies charge power, taken from the module's VBUS castellation (pin 40) ahead of the module's Schottky diode, to a boost charger for the 2S pack. The charge input current limit defaults to 500 mA (USB 2.0 configured budget); any higher limit requires a positive DCP identification or an explicit operator setting and never exceeds 1.5 A. Transmit is inhibited by hardware while VBUS is present; receive is allowed while charging with charging paused (proposed, `power-tree-and-charging.md` D-PWR-07). The module is an owner-soldered part under the kit model (ADR-007). No SWD header is populated in delivered units.

## 3. Alternatives considered

| Option | Description | Why not chosen (or why chosen) |
|---|---|---|
| A (chosen) | Pico 2 module, its micro-B for load and charge | Owner direction (SI-007, SI-022); a tested module with crystal, flash and USB already laid out; one connector, one wall opening |
| B | Bare RP2350 on the main board | Rejected: adds USB, crystal and QSPI flash layout and a second set of first-power-on risks (RSK-008); loses the module's own test coverage; contrary to SI-007 |
| C | Pico 2 plus a separate USB-C charge connector | Rejected by SI-022 (single connector); USB-C would lift the 500 mA ceiling but adds a connector, an opening and a PD or BC1.2 controller |
| D | Pico 2 W or another RP2350 board | Not requested; wireless adds nothing to a CW radio and a radio interferer |

No trade study: the owner's direction eliminated the alternatives; the make/buy record for the runtime (SWE-033) is the trade study named in `docs/process/07-software-engineering-plan.md` section 17.2.

## 4. Consequences

### 4.1 Requirements created or changed

| Requirement | Relationship | Note |
|---|---|---|
| REQ-SYS-NNN (controller constraint: the system shall use the Raspberry Pi Pico 2 module; L1 author allocates) | new, constraint traced to SI-007, this ADR supporting | Named solution permitted at L1 because it is an owner constraint (02 section 4.2) |
| REQ-SYS-NNN or REQ-PWR-NNN (charge input from the module's USB, 500 mA default, never above 1.5 A) | new, traces to SI-022; candidate PWR-USB-01 and PWR-USB-02 | Verification: Inspection (PSEL strap, register default), Bench (current-limited supply) |
| REQ-SYS-NNN (transmit inhibited by hardware while charging) | new, hazard control HZ-002 | Proposed, D-PWR-07 |
| REQ-SW-NNN (firmware loaded as `rp2350-arm-s` UF2 with IMAGE_DEF; image hash in the VDD; CRC trailer checked before any safety-critical output) | new, self-derived from this ADR and SWE-134 | `rp2350-emulation-options.md` REQ-candidate; 07 section 16.2 |

### 4.2 Interfaces, design and code

- ICDs affected: `ICD-CTL-USB` (external stub before SRR: connector, VBUS pin 40 tap, data lines not used by the radio), `ICD-PWR-CELL`
- Design elements created or changed: power tree input stage (VBUS to charger), module footprint (from the Pico 2 datasheet section 3.2, since no official Pico 2 KiCad footprint exists), enclosure wall opening 12.0 x 10.0 mm
- New `SW-<SUB>` modules created by this ADR: none
- ICDs created by this ADR: none (stubs are created by the ICD process before SRR, 02 section 3.5)

### 4.3 Verification and safety

- Verification cases to add or change: TC-PWR-NNN (input current limit), TC-SW-BOOT-NNN (image load accept and reject, SWE-193), TC-ME-NNN (connector opening fit on the printed shell)
- Evidence class implications: the module's VBUS copper is unrated; a Bench test at 0.5, 1.0 and 1.5 A on a spare Pico 2 (PWR-USB-02) is the only way to lift the 500 mA ceiling
- Hazard analysis update required: yes (HZ-002 cause "charging through the module path")
- Safety-critical software scope changed: no (charging supervision is already in scope)

### 4.4 Cost, schedule, risk

- BOM impact: Pico 2 about USD 5; two spares recommended (ADR-025); charge time about 10 h at 500 mA is accepted
- Gate affected: PDR (power tree), CDR (footprint and opening)
- Risks opened, closed or re-scored: RSK-003 (emulator peripherals), RSK-008 (first power-on) remain; new risk proposed: "Pico 2 module VBUS path unrated above 500 mA" (Low confidence in F2)
- TPMs affected: TPM-009 (board area: the module is 51 x 21 mm), TPM-010 and TPM-011 (flash and RAM margins on a 4 MB, 520 KB device)

Clock note for the RF design: the module's 12 MHz crystal has its 12th harmonic at 144.000 MHz and the 48 MHz USB clock its 3rd; the frequency plan therefore keeps the transmit guard of ADR-023 and the SPI, PWM and system clocks away from 144.000 to 148.000 MHz (design rule for PDR; `part97-regulatory-basis.md` RF-08).

## 5. Compliance and tailoring

RMM row SWE-027 (third-party register) lists rustos `api` and `pico2` and Rust `core` as the only code in the image (07 section 17.1); SWE-157 (debug port) reads "SWD pads unpopulated and enclosed" (07 section 22). No new tailoring.

## 6. Decision record

> Owner (2026-09-25, SI-007): "Raspberry Pi Pico 2 as the controller; firmware in Rust built on the owner's `rustos`."

> Owner (2026-09-25, SI-022): "USB strategy: use the Pico 2 module's micro-USB connector for both firmware loading and battery charging (single connector, simplest)."

Transcribed from chat into `stakeholder-inputs.md`.

## 7. Related

- Supersedes: none
- Superseded by: none
- Trade study: firmware runtime and HAL make/buy TS (SWE-033, 07 section 17.2), which records the cost of the rustos choice; none for the module
- Review where presented: SRR
- Revisit conditions: the PWR-USB-02 Bench test shows the module path cannot carry 500 mA continuously; PCBWay confirms it can reflow the module in turnkey (then the assembly category changes under ADR-007, not this ADR); RP2350 silicon revision other than A2 changes the E9 input policy
