# ADR-058: Raspberry Pi Pico 2 module as controller, with its micro-USB for firmware loading only (supersedes ADR-004)

| Field | Value |
|---|---|
| ID | ADR-058 |
| Status | Proposed. For the owner's confirmation at PDR session S1 (OD-10 part 1, with ADR-056 items 2 to 4). On the S1 disposition it becomes Accepted by a Status-line edit, and ADR-004's Status becomes "Superseded by ADR-058" (README rule 2; WP-PDR-02). It stays Proposed while its independent review runs, because README rule 2 allows no edit of an Accepted ADR and review fixes must be made in place |
| Date proposed | 2026-09-29 |
| Date decided | Pending (S1). The parts restated unchanged were decided on 2026-09-25 (ADR-004; owner, SI-007 and SI-022). The A5 change, no charge path through USB, was decided with the owner's A5 decision of 2026-09-29 (ADR-056 section 2 item 1) |
| Decision class | 1 (`docs/process/06-risk-and-decision-analysis.md` section 14.1 items (b) single-source part, the Pico 2 module; (c) HZ-004, HZ-011, HZ-014 and the component `SW-PWR` of `docs/process/07-software-engineering-plan.md` section 14.1; (h) for the runtime). ADR-004 also named HZ-002, whose USB charging cause A5 removes. The module stays owner-directed (SI-007) and is recorded without a trade study under SEMP customization 11 (`docs/plan/semp.md` section 9.0 and section 5.17), item (i), as ADR-004 recorded it (SRR decision 106). The runtime and HAL are TS-002, decided as SRR decision 107 and recorded by ADR-027. The A5 change was chosen in TS-012, a class 1 study (items (a) power architecture and (b) battery charger), and is recorded by ADR-056, the one ADR of TS-012 (06 section 14.2). This ADR takes no new decision and is not a second ADR of TS-012: it restates ADR-004 so that ADR-004 can be superseded in full |
| Decision authority | Robin (owner; the decision fixes the controller and the only external data connector, and the charge-path removal changes baseline content through CR-018) |
| Author | Claude (technical data manager invocation, WP-PDR-54 part 1 follow-on, 2026-09-29) |
| Independent reviewer | Pending. The same review as ADR-056 (WP-PDR-54: an independent reviewer with a software assurance pair, since the decision touches `SW-PWR`; the lead SE assigns the record ids and paths). The record must be APPROVED before S1, because OD-10 part 1 rests on it |
| Life-cycle phase | B |
| Baseline affected | baseline/srr (functional baseline) through CR-018, dispositioned at S1 (OD-40); baseline/pdr |
| Change request | none for this record. The requirement changes it restates are carried by CR-018, the re-baseline CR (WP-PDR-53) |

## 1. Context

ADR-004 (Accepted, 2026-09-25) fixes the Raspberry Pi Pico 2 module as the controller and makes its micro-USB the radio's only USB connector, for firmware loading and for battery charging (SI-007, SI-022). The owner's A5 decision of 2026-09-29 (ADR-056 section 2 item 1; `docs/decisions/trade-studies/TS-012-design-to-cost-hand-built.md` section 10) keeps the controller ("The controller stays the Pico 2 with Rust on rustos (ADR-004, ADR-027)", ADR-056 section 2 item 1) and removes the charge path. The cells are charged outside the radio in an XTAR MC1, and "USB on the radio is for firmware only" (TS-012 section 8.1; descope D2; exception EX-4). That gives up the charging half of SI-022 and CON-010 (D2). TS-012 section 3.2 had re-checked in-radio charging under the USD 300 maximum and pruned it for build 1.

An Accepted ADR is not edited (README rule 2; `docs/process/05-configuration-and-data-management.md` Table 4-1 row 13), and rule 2 has no partial supersession. The lead SE ruled on 2026-09-29 (ruling 2, recorded in ADR-056 section 7) to follow the ADR-026 precedent, where ADR-026 restated ADR-010 and superseded it in full. This ADR therefore restates every unchanged part of ADR-004 verbatim or near-verbatim, states the A5 change with its sources, and supersedes ADR-004 in full on the S1 disposition.

ADR-004's context, restated without the charging budget: the owner directed the Raspberry Pi Pico 2 (RP2350) as the controller with firmware in Rust on the owner's `rustos` (SI-007), and a single connector, the module's own micro-USB (SI-022). The choice fixes the CPU (Cortex-M33, `thumbv8m.main-none-eabihf`), the bootloader path (BOOTSEL UF2), the pin budget, the assembly category of the module, and two clock harmonics that land on 144.000 MHz.

- Driving inputs and expectations: SI-007, SI-022 (its charging half given up by A5, descope D2), SI-011 (Claude produces everything), SI-026 (host-first software), SI-031 (owner solders modules with exposed pads); CON-010 (USB for firmware and charging, changed to firmware only by CR-018). TS-012 section 8.10 lists SI-022 and SI-031 as superseded by the owner inputs of status note 2026-09-27 sections 6, 8 and 10 and the decision's lifecycle condition, which take the next free SI ids when CR-018 appends them.
- Requirements that constrain the decision: at ADR-004, none. Now: REQ-SYS-126 and REQ-SYS-090 (created from ADR-004), REQ-SYS-092 (hardware transmit inhibit with USB power), REQ-SYS-133 (firmware update over USB with the cells removed).
- Hazards in play (`docs/safety/hazards.json` 0.5.0-pha):
  - HZ-002: ADR-004's cause "charging through the module connector" is removed, since the radio has no charger. HZ-002 is re-scoped to the COTS charger and the handbook (ADR-056 section 4.3).
  - HZ-004: firmware image integrity through the USB loader.
  - HZ-011 (charging while transmitting): control K1, the hardware transmit inhibit on VBUS (REQ-SYS-092), and K6, the firmware VBUS layer, stay. Controls K2 (charging paused while receiving, REQ-SYS-093) and K4 (the charge input current limit) lose their object with no in-radio charger.
  - HZ-014 (firmware load leaving an unsafe state: REQ-SYS-132, REQ-SYS-133): control K4 relies on USB being present during every load, unchanged.
- Research consulted: as ADR-004: `docs/research/rustos-toolchain-proof.md` F1 to F5 (host build, cross build, UF2 conversion all work), F11 (RP2350-E9: no internal pull-downs on A2 silicon), F14 (pin budget fits with margin), F15 (bootrom flash API for configuration); `docs/research/pcbway-fabrication-and-assembly.md` F16 (Pico 2 as a castellated SMT module: recommended footprint, no Pico 2 KiCad footprint yet); `docs/research/power-tree-and-charging.md` F1 (USB 2.0: 500 mA configured), F2 (micro-B contacts about 1.8 A; Pico 2 publishes no rating for its connector or VBUS copper); `docs/research/display-and-ui-parts.md` baseline row "USB" (12.0 x 10.0 mm wall opening); `docs/research/emulator-accreditation-and-timer-irq.md` F13 (A2 bootrom embedded in the emulator; owner boards may be A3 or A4). ADR-004's charging findings (`power-tree-and-charging.md` F3 and F4: charge time at 500 mA, BQ25887 PSEL and DCP detection) no longer bear on this decision. For the A5 change: TS-012 sections 3.2 (in-radio 2S charging re-check), 8.1, 8.8 (D2), 8.9 (EX-2, EX-4), 8.10 and 8.13 (Q3, Q5); `docs/design/analysis/mechanical-tolerance-stack.md` stack S5b (USB opening).
- Guidance consulted: SWE-063 (version description records the image hash), SWE-134 (safe state before any output); SE HB §6.8; 06 sections 14.1, 14.2 and 14.6; README rules 1 to 6.
- Assumptions the decision rests on, and how and by when each is confirmed:
  1. The module is the only load on USB and stays within the 500 mA of REQ-SYS-090 (TS-012 section 8.10: "Keep (Pico only on USB ...)"). Confirmed by the WP-PDR-24 power work with the TS-005 remnant study (firmware loading and the VBUS inhibit), decided at S2, and by the TC-SYS-050 input-current step. ADR-004's assumption that the module VBUS path carries 500 mA of charge current continuously is withdrawn with the charge path.
  2. The RP2350 stepping is A2, so the E9 input policy applies. Confirmed by receipt inspection of the modules before TRR (as ADR-004).
  3. The owner solders the castellated module flat, and the module counts as through-hole compatible (TS-012 exception EX-2, owner question Q5). Confirmed by the owner's answer to Q5 and by the owner-solder inspection before first power-on.

## 2. Decision

The controller is the Raspberry Pi Pico 2 module (ordering code SC1631, RP2350 in ARM mode, 4 MB flash) mounted as a castellated surface-mount module on the main board. The firmware is Rust on `rustos` with zero external runtime crates (ADR-027). The module's micro-B connector is the only USB connector on the radio, and it loads firmware through the RP2350 bootrom (BOOTSEL, UF2, `picotool`).

**(Changed for A5.)** The micro-B supplies no charge power. The radio has no charger: the cells are charged outside the radio (ADR-059; TS-012 descope D2), and VBUS is used on the board only to sense USB presence for the hardware transmit inhibit. The radio draws at most 500 mA from VBUS, the module being the only load on USB (REQ-SYS-090). ADR-004's charge input limit, its DCP identification rule and its 1.5 A ceiling lapse with the charge path, and so does the charge pause while receiving (proposed in ADR-004 from `power-tree-and-charging.md` D-PWR-07).

Transmit is inhibited by hardware while VBUS is present (REQ-SYS-092). **(Changed for A5.)** The module is soldered by the owner under the owner hand assembly of A5 (ADR-056 section 2 item 1; TS-012 exception EX-2), which replaces the kit model of ADR-007. No SWD header is populated in delivered units.

## 3. Alternatives considered

| Option | Description | Why not chosen (or why chosen) |
|---|---|---|
| A (chosen) | Pico 2 module, its micro-B for firmware loading only; cells charged outside the radio | Owner direction for the module (SI-007) and the single connector (SI-022); A5 for the charge path (ADR-056); a tested module with crystal, flash and USB already laid out; one connector, one wall opening |
| A-004 | ADR-004 as decided: Pico 2 micro-B for load and charge, VBUS to a boost charger for the 2S pack | Not chosen: TS-012 section 3.2 found the USB-input 2S charger ICs LCSC-only, at an estimated USD 7 to 14 capped in parts plus USD 0 to 23 capped of LCSC shipping, and the Catastrophic HZ-002 charger chain back in the box beside a PA sink that dissipates 8.5 to 10 W; pruned for build 1 (owner question Q3) |
| B | Bare RP2350 on the main board | Rejected: adds USB, crystal and QSPI flash layout and a second set of first-power-on risks (RSK-008); loses the module's own test coverage; contrary to SI-007 |
| C | Pico 2 plus a separate USB-C charge connector | Rejected by SI-022 (single connector), and there is no in-radio charging in build 1 |
| D | Pico 2 W or another RP2350 board | Not requested; wireless adds nothing to a CW radio and a radio interferer |

No trade study for the module: the owner's direction eliminated the alternatives. The make/buy record for the runtime (SWE-033) is TS-002 (`docs/decisions/trade-studies/TS-002-firmware-runtime-make-buy.md`), decided as SRR decision 107 and recorded by ADR-027. The charge-path change is TS-012's (ADR-056).

## 4. Consequences

### 4.1 Requirements created or changed

When this ADR is Accepted, each requirement that cites ADR-004 adds ADR-058 to `source_ids` (cross item to the CR-018 author).

| Requirement | Relationship | Note |
|---|---|---|
| REQ-SYS-126 (controller module) | allocated; cites ADR-004; unchanged | Named solution permitted at L1 because it is an owner constraint (02 section 4.2). Cross item: add ADR-058 in CR-018 |
| REQ-SYS-090 (USB input current, at most 500 mA) | allocated; cites ADR-004; value kept (TS-012 section 8.10: "Keep (Pico only on USB ...)") | ADR-004's note on limits above 500 mA and up to 1.5 A lapses with the charge path. Cross item: add ADR-058 in CR-018 |
| REQ-SYS-092 (hardware transmit inhibit with USB power) | allocated; does not cite ADR-004; kept (TS-012 section 8.10) | HZ-011 control K1 (also HZ-014 K4) |
| REQ-SYS-093 (charging paused while receiving) | retired via CR-018 (no in-radio charging) | ADR-004 section 2 proposed it (D-PWR-07) |
| REQ-SYS-070 (charge state indication), REQ-SYS-091 (charge time) | retired via CR-018 | "the MC1 indicates" (TS-012 section 8.10) |
| REQ-SYS-132 (firmware image integrity), REQ-SYS-133 (firmware update over USB) | allocated at L1; neither cites ADR-004; unchanged | The image format, hash and CRC trailer requirement at L2 belongs in the firmware-wide `docs/requirements/sw/requirements.json` (PDR); 07 section 16.2 |

### 4.2 Interfaces, design and code

- ICDs affected: `ICD-CTL-USB` (connector; firmware only, no charge path, via CR-018, ADR-056 section 4.2; data lines not used by the radio, as ADR-004), `ICD-PWR-CELL` (no in-radio charging).
- Design elements created or changed:
  - The power tree input stage (VBUS to charger) of ADR-004 is removed. VBUS reaches only the hardware transmit inhibit on the clamp node (TS-012 section 8.1; the 2N3904 VBUS inhibit of section 8.3 row 12).
  - Module footprint from the Pico 2 datasheet section 3.2, since no official Pico 2 KiCad footprint exists (as ADR-004); the module is soldered flat by its castellations (TS-012 section 8.1, Boards).
  - The micro-USB opening is in the printed PETG case, on the far end face or on a side wall as the layout sets it (TS-012 section 8.5; WP-PDR-37 and 39). ADR-004 gave 12.0 x 10.0 mm; the tolerance stack proposes 12.6 x 10.6 mm to WP-PDR-36 (`mechanical-tolerance-stack.md` S5b).
- New `SW-<SUB>` modules created by this ADR: none. `SW-PWR` loses its charging functions (section 4.3).
- ICDs created by this ADR: none.

### 4.3 Verification and safety

- Verification cases to add or change: TC-SYS-050 keeps its REQ-SYS-090 input-current step and loses the REQ-SYS-070 and REQ-SYS-093 steps with those requirements (carried by CR-018); TC-SYS-058 (Inspection, REQ-SYS-126) is unchanged. The SW-BOOT image load accept and reject case (SWE-193) and the ME connector-opening fit case on the printed shell are allocated with their L2 requirements at PDR (no id yet), as ADR-004.
- Evidence class implications: ADR-004's Bench test at 0.5, 1.0 and 1.5 A on a spare Pico 2 (PWR-USB-02) is no longer needed, because nothing lifts the 500 mA ceiling.
- Hazard analysis update required: yes (WP-PDR-16, 0.6.0-pha).
  - HZ-002 loses the cause "charging through the module path" (ADR-056 section 4.3).
  - HZ-011 keeps K1, K3 and K6. K2, K4 and the charging lines of K5 lose their object. HZ-011 is not named in TS-012 or in ADR-056 section 4.3; cross item to the WP-PDR-16 hazard author.
  - HZ-014 K4 is unchanged.
- Safety-critical software scope (SWE-134 provisions) changed: yes. `SW-PWR` (07 section 14.1) loses its charging supervision: charger status, the dual-path charge check of REQ-SYS-088, the temperature window, charge disable, the charge-state watchdog and the charge pause of HZ-011 K2. Its discharge-side functions and the GPIO24 VBUS reading (HZ-011 K6) stay. The determination is re-run in WP-PDR-17 (ADR-056 section 4.3).

### 4.4 Cost, schedule, risk

- BOM impact: Pico 2 USD 5.00 (TS-012 section 8.3 row 8). ADR-004's charge time of about 10 h at 500 mA no longer applies: the XTAR MC1 charges one cell at a time, about 6 h per cell at 0.5 A (D2).
- Gate affected: PDR (S1 disposition; the TS-005 remnant at S2), CDR (footprint and opening).
- Risks opened, closed or re-scored:
  - RSK-003 (emulator peripherals) and RSK-008 (first power-on) remain.
  - RSK-033 (Pico 2 USB power path overheats at the charging current) loses its cause, since no charge current flows through the module. Proposed to the WP-PDR-18 writer for retirement.
  - ADR-004's proposed risk "Pico 2 module VBUS path unrated above 500 mA" lapses for the same reason.
- TPMs affected: TPM-009 (board area: the module is 51 x 21 mm), TPM-010 and TPM-011 (flash and RAM margins on a 4 MB, 520 KB device).

Clock note for the RF design (as ADR-004): the module's 12 MHz crystal has its 12th harmonic at 144.000 MHz and the 48 MHz USB clock its 3rd; the frequency plan therefore keeps the transmit guard of ADR-023 and the SPI, PWM and system clocks away from 144.000 to 148.000 MHz (`part97-regulatory-basis.md` RF-08). For A5 the transmit clock plan of TS-012 D-12 carries it (clk_sys = clk_peri = 96 MHz, PLL_USB off when USB is not enumerated), and WP-PDR-20a revises ADR-031 (ADR-056 section 7).

## 5. Compliance and tailoring

RMM row SWE-027 (third-party register) lists rustos `api` and `pico2` and Rust `core` as the only code in the image (07 section 17.1); SWE-157 (debug port) reads "SWD pads unpopulated and enclosed" (07 section 22). No new tailoring.

## 6. Decision record

The controller and the single connector are the owner's, on record before this ADR:

> Owner (2026-09-25, SI-007): "Raspberry Pi Pico 2 as the controller; firmware in Rust built on the owner's `rustos`."

> Owner (2026-09-25, SI-022): "USB strategy: use the Pico 2 module's micro-USB connector for both firmware loading and battery charging (single connector, simplest)."

Transcribed from chat into `stakeholder-inputs.md` (ADR-004 section 6). The charging half of SI-022 is given up by the owner's A5 decision, recorded in ADR-056 section 6 (Form 1) and TS-012 section 10; A5 includes "The cells are charged outside the radio in an XTAR MC1. USB on the radio loads firmware only" (ADR-056 section 2 item 1):

> Owner (2026-09-29, in chat; status note 2026-09-29 section 5, after the A5 parts lifecycle report): "A5"

**Proposed memo wording for S1 (OD-10 part 1; README rule 4).** "Confirm ADR-058. It restates ADR-004 with the A5 change: the Pico 2's micro-USB loads firmware only, and the radio has no charge path. ADR-058 is Accepted and ADR-004 becomes Superseded by ADR-058." Owner's disposition: not yet given. It is transcribed here with its date at S1.

## 7. Related

- Supersedes: ADR-004, in full, on the S1 disposition (ADR-004's Status then reads "Superseded by ADR-058", set by WP-PDR-02). Until then ADR-004 stays Accepted and in force.
- Superseded by: none.
- Trade study: none for the module (Decision class row); TS-002 for the runtime and HAL (ADR-027); TS-012 for the charge-path change (ADR-056); the TS-005 remnant for the USB input policy of firmware loading and the VBUS inhibit (WP-PDR-24, decided at S2).
- Review where presented: PDR session S1 (OD-10 part 1). ADR-004 was presented at SRR.
- Related records: ADR-056, ADR-059, ADR-027, ADR-031; CR-018.
- Revisit conditions:
  - An RP2350 silicon revision other than A2 changes the E9 input policy (as ADR-004).
  - ADR-004's PWR-USB-02 condition lapses with the charge path, and its PCBWay turnkey condition lapses with ADR-007.
  - In-radio charging is wanted in a later build (TS-012 Q3: "Revisit for a later build"): a superseding ADR, after a new trade study.
  - TS-005 at S2 chooses a USB input policy that section 2 does not allow: a superseding ADR.

## 8. Change log

- 2026-09-29: created by the technical data manager (WP-PDR-54 part 1 follow-on), on lead SE ruling 2 of 2026-09-29 (ADR-056 section 7): ADR-004 is contradicted only in part, README rule 2 has no partial supersession, so this ADR restates ADR-004 in full with the A5 change and supersedes it on the S1 disposition, as ADR-026 did for ADR-010. The number is the next free one after ADR-057 (README rule 1). ADR-004's section 8 readings are carried: the independent reviewer reading is replaced by this record's own review, the hazard stamp is 0.5.0-pha, and the verification cases are those of its WP-PDR-14 reading. Author: Claude (technical data manager invocation).
