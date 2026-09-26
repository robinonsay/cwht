# ADR-004: Raspberry Pi Pico 2 module as controller, with its micro-USB for programming and charging

| Field | Value |
|---|---|
| ID | ADR-004 |
| Status | Accepted |
| Date proposed | 2026-09-25 |
| Date decided | 2026-09-25 |
| Decision class | 1 (`docs/process/06-risk-and-decision-analysis.md` section 14.1 items (b) single-source part, the Pico 2 module; (c) HZ-002, HZ-004, HZ-011, HZ-014; (h) for the runtime). Owner-directed (SI-007, SI-022). Trade study: TS-002 (Draft) for the runtime and HAL. No trade study for the module: this ADR alone records it only if the owner adopts ruling R-2 item (i) of `reconciliation-srr.md` section 7 (open; the owner's ruling); otherwise a trade study is opened, or a waiver of 06 section 14.1 is recorded, before `baseline/srr` |
| Decision authority | Robin (owner; the decision fixes the controller and the only external data and charge connector) |
| Author | Claude (technical data manager invocation, 2026-09-25) |
| Independent reviewer | INSP-011 (`docs/reviews/SRR/checklists/adrs-001-to-025.md`): iterations 1 and 2 (2026-09-25) NEEDS CHANGES, findings F-01, F-02 and F-03 against this file; the Major-finding corrections are applied here on 2026-09-26 (section 8); verification pending at INSP-011 iteration 3 |
| Life-cycle phase | Pre-A / A |
| Baseline affected | baseline/srr (functional baseline, to be tagged at SRR) |
| Change request | none (pre-baseline) |

## 1. Context

The owner directed the Raspberry Pi Pico 2 (RP2350) as the controller with firmware in Rust on the owner's `rustos` (SI-007), and a single connector: the module's own micro-USB for firmware loading and battery charging (SI-022). The choice fixes the CPU (Cortex-M33, `thumbv8m.main-none-eabihf`), the bootloader path (BOOTSEL UF2), the pin budget, the USB power budget for charging a 2S pack, the assembly category of the module, and two clock harmonics that land on 144.000 MHz.

- Driving inputs and expectations: SI-007, SI-022, SI-011 (Claude produces everything), SI-026 (host-first software), SI-031 (owner solders modules with exposed pads)
- Requirements that constrain the decision: none yet
- Hazards in play (`docs/safety/hazards.json` 0.4.0-pha): HZ-002 (charging through the module connector), HZ-004 (firmware image integrity through the USB loader), HZ-011 (charging while transmitting: REQ-SYS-090, which cites this ADR, control K4; REQ-SYS-092, control K1) and HZ-014 (firmware load leaving an unsafe state: REQ-SYS-132, REQ-SYS-133; control K4 relies on USB being present during every load)
- Research consulted: `docs/research/rustos-toolchain-proof.md` F1 to F5 (host build, cross build, UF2 conversion all work), F11 (RP2350-E9: no internal pull-downs on A2 silicon), F14 (pin budget fits with margin), F15 (bootrom flash API for configuration); `docs/research/pcbway-fabrication-and-assembly.md` F16 (Pico 2 as a castellated SMT module: recommended footprint, paste zones 163 percent, no Pico 2 KiCad footprint yet, no published PCBWay policy for reflowing it); `docs/research/power-tree-and-charging.md` F1 (USB 2.0: 500 mA configured; BC1.2 DCP 1.5 A), F2 (micro-B contacts about 1.8 A; Pico 2 publishes no rating for its connector or VBUS copper), F3 (500 mA gives about 280 mA charge, about 10 h to full), F4 (BQ25887 PSEL default 500 mA; DCP detection via USBPHY_AS_GPIO unverified); `docs/research/display-and-ui-parts.md` baseline row "USB" (12.0 x 10.0 mm wall opening); `docs/research/emulator-accreditation-and-timer-irq.md` F13 (A2 bootrom embedded in the emulator; owner boards may be A3 or A4)
- Guidance consulted: SWE-063 (version description records the image hash), SWE-134 (safe state before any output); SE HB §6.8
- Assumptions the decision rests on, and how and by when each is confirmed:
  1. The module VBUS path carries 500 mA continuously. Confirmed by a Bench test on a spare Pico 2 (PWR-USB-02) with the TS-005 USB input policy study at PDR (proposed number, `docs/design/concept.md` section 11.2).
  2. The RP2350 stepping is A2, so the E9 input policy applies. Confirmed by receipt inspection of the modules before TRR.
  3. The owner solders the castellated module (ADR-007). Confirmed by the owner-solder inspection before first power-on.

## 2. Decision

The controller is the Raspberry Pi Pico 2 module (ordering code SC1631, RP2350 in ARM mode, 4 MB flash) mounted as a castellated surface-mount module on the main board; the firmware is Rust on `rustos` with zero external runtime crates. The module's micro-B connector is the only USB connector on the radio: it loads firmware through the RP2350 bootrom (BOOTSEL, UF2, `picotool`) and it supplies charge power, taken from the module's VBUS castellation (pin 40) ahead of the module's Schottky diode, to a boost charger for the 2S pack. The charge input current limit defaults to 500 mA (USB 2.0 configured budget); any higher limit requires a positive DCP identification or an explicit operator setting and never exceeds 1.5 A. Transmit is inhibited by hardware while VBUS is present; receive is allowed while charging with charging paused (proposed, `power-tree-and-charging.md` D-PWR-07). The module is an owner-soldered part under the kit model (ADR-007). No SWD header is populated in delivered units.

## 3. Alternatives considered

| Option | Description | Why not chosen (or why chosen) |
|---|---|---|
| A (chosen) | Pico 2 module, its micro-B for load and charge | Owner direction (SI-007, SI-022); a tested module with crystal, flash and USB already laid out; one connector, one wall opening |
| B | Bare RP2350 on the main board | Rejected: adds USB, crystal and QSPI flash layout and a second set of first-power-on risks (RSK-008); loses the module's own test coverage; contrary to SI-007 |
| C | Pico 2 plus a separate USB-C charge connector | Rejected by SI-022 (single connector); USB-C would lift the 500 mA ceiling but adds a connector, an opening and a PD or BC1.2 controller |
| D | Pico 2 W or another RP2350 board | Not requested; wireless adds nothing to a CW radio and a radio interferer |

No trade study: the owner's direction eliminated the alternatives; the make/buy record for the runtime (SWE-033) is TS-002 (`docs/decisions/trade-studies/TS-002-firmware-runtime-make-buy.md`, Draft; decided at SRR; its decision becomes a new ADR), named in `docs/process/07-software-engineering-plan.md` section 17.2.

## 4. Consequences

### 4.1 Requirements created or changed

| Requirement | Relationship | Note |
|---|---|---|
| REQ-SYS-126 (controller module) | allocated; cites this ADR | Named solution permitted at L1 because it is an owner constraint (02 section 4.2) |
| REQ-SYS-090 (USB input current, at most 500 mA, TBR) | allocated; cites this ADR; hazard HZ-011 (control K4) | Candidates PWR-USB-01 and PWR-USB-02; any limit above 500 mA, never above 1.5 A, is the TS-005 USB input policy study at PDR. Verification: Inspection (PSEL strap, register default), Bench (current-limited supply) |
| REQ-SYS-092 (hardware transmit inhibit with USB power) | allocated; does not cite this ADR | HZ-011 control K1 (also HZ-014 K4), not an HZ-002 control; D-PWR-07 |
| REQ-SYS-132 (firmware image integrity), REQ-SYS-133 (firmware update over USB) | allocated at L1; neither cites this ADR | The image format, hash and CRC trailer requirement at L2 belongs in the firmware-wide `docs/requirements/sw/requirements.json`, not created (PDR); 07 section 16.2 |

### 4.2 Interfaces, design and code

- ICDs affected: `ICD-CTL-USB` (external stub before SRR: connector, VBUS pin 40 tap, data lines not used by the radio), `ICD-PWR-CELL`
- Design elements created or changed: power tree input stage (VBUS to charger), module footprint (from the Pico 2 datasheet section 3.2, since no official Pico 2 KiCad footprint exists), enclosure wall opening 12.0 x 10.0 mm
- New `SW-<SUB>` modules created by this ADR: none
- ICDs created by this ADR: none (stubs are created by the ICD process before SRR, 02 section 3.5)

### 4.3 Verification and safety

- Verification cases to add or change: TC-PWR-NNN (input current limit), TC-SW-BOOT-NNN (image load accept and reject, SWE-193), TC-ME-NNN (connector opening fit on the printed shell)
- Evidence class implications: the module's VBUS copper is unrated; a Bench test at 0.5, 1.0 and 1.5 A on a spare Pico 2 (PWR-USB-02) is the only way to lift the 500 mA ceiling
- Hazard analysis update required: yes (HZ-002 cause "charging through the module path"; HZ-011 controls K1 and K4; HZ-014 control K4)
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
- Trade study: TS-002 (`docs/decisions/trade-studies/TS-002-firmware-runtime-make-buy.md`, Draft; decided at SRR; its decision becomes a new ADR), the firmware runtime and HAL make/buy (SWE-033, 07 section 17.2), which records the cost of the rustos choice; none for the module (section 1, Decision class row)
- Review where presented: SRR
- Revisit conditions: the PWR-USB-02 Bench test shows the module path cannot carry 500 mA continuously; PCBWay confirms it can reflow the module in turnkey (then the assembly category changes under ADR-007, not this ADR); RP2350 silicon revision other than A2 changes the E9 input policy

## 8. Change log

- 2026-09-26: one-time pre-baseline correction under INSP-011 ruling R-1 option (A), as directed by the lead SE: Decision class row and section 1 Assumptions line added (F-01); hazard line and "Hazard analysis update required" re-derived against `docs/safety/hazards.json` 0.4.0-pha (F-02); section 4.1 placeholder ids replaced by the ids the requirement authors allocated, or marked not created with the reason (F-03); trade study references resolved to TS-002 (F-03, erratum E-9). Content from `reconciliation-srr.md` sections 2, 3, 5.1 and 6, re-checked against the requirement, hazard and expectation files of 2026-09-26; that register is superseded by this file for this ADR. The decision of section 2 is unchanged. Minor findings are liens, fixed before PDR: none against this file. The edit of an Accepted ADR rests on the owner's approval of R-1 (A) in the SRR decision memo and the matching sentence in `docs/process/05-configuration-and-data-management.md` Table 4-1 row 13 (both pending). Class 1 choices without a trade study wait on ruling R-2 (owner). Author: Claude (ADR author invocation).
