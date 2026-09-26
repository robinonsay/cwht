# cwht Schedule Baseline (expedited)

**Approved by owner:** 2026-09-25 (Friday). Goal: procurement release (CDR approval) by Sunday 2026-09-27 evening; vendor orders placed Sunday night. Reviews are event-based (NPR 7123.1D §5.1.5); the dates below are targets, and a gate is held only when its entrance criteria in `docs/process/01-lifecycle-and-reviews.md` are met.

This file is also the software schedule of NPR 7150.2D SWE-016 as tailored in `docs/process/rmm.json` (disposition T): the gate milestones below, the firmware milestones of section 1, the dependencies between hardware, software, operations and the rustos project (sections 1 and 2) and the vendor lead times of section 3. Revised 2026-09-26 for INSP-023 finding-1.

| Target | Phase work | Gate / product |
|---|---|---|
| Fri 2026-09-25 evening to Sat morning | ConOps, NGOs/MOEs, L1 requirements, hazard analysis, RMM, risk register, SEMP, V&V approach, research findings, toolchain proof | **SRR** package ready Sat morning; owner review about 1 h |
| Sat 2026-09-26 day | Architecture trade studies (receiver topology, synthesizer, PA, T/R), L2 requirements, ICDs, block-level LTspice with pass/fail checks, V&V plan, integration plan, enclosure envelope | **PDR** package Sat evening; owner review 1 to 2 h; liens permitted where CDR completes the product |
| Sat night to Sun 2026-09-27 afternoon | Full schematic, 4-layer layout, enclosure CAD and STEP, complete analysis package, BOM with live stock checks, fabrication and assembly package, firmware architecture and emulation plan, first-power-on procedure | **CDR** package Sun evening; owner review about 2 h |
| Sun 2026-09-27 night | PCBWay fabrication, assembly and CNC orders; DigiKey order for items PCBWay does not source | **Procurement release** |
| Vendor lead time (section 3: boards expected about 2026-10-15 to 10-17, enclosures about 2026-10-19 to 10-21, 4 weeks outer bound) | Firmware implementation, host tests, emulation scenarios, fit-check prints, receipt inspection | **TRR** on board arrival, then V&V execution and **SAR** |

## 1. Firmware milestones and their dependencies (SWE-016 a, b, c)

The firmware milestones are the build increments FW-B0 to FW-B4 of `docs/process/07-software-engineering-plan.md` sections 3.1 and 3.2, keyed to the gates above, with the four named milestones of the RMM SWE-016 row (HAL bring-up in emulation, keyer complete for straight key and iambic paddles per SI-018, receive chain complete, release candidate) as separate rows. No application module sprint starts before the SRR decision memo (07 section 14). The exit criteria are those of 07 section 3.2; this table adds the dependencies.

| Id | Firmware milestone | Gate | Hardware dependency | Software dependency | Operations dependency (owner) | rustos dependency (07 section 19; section 2) |
|---|---|---|---|---|---|---|
| FM-1 | FW-B0 toolchain proof: workspace builds for host and target, `tools/sw_gate.sh` exits 0, blinky flashed and observed on a bare Pico 2 | SRR | Bare Pico 2 development board (owner's) | `tools/toolchain.lock.md` complete; gate scripts of 07 section 1.2 | Flash and observe steps 11 and 12 of TC-SW-TOOL-001 (package OA-1); toolchain download and rustos manifest rulings (package decisions 109, 110) | rustos at the pinned commit `c54d35a` (lock section 3) |
| FM-2 | HAL bring-up in emulation: the ACC-EMU-001 candidate emulator boots the FW-B0 blinky and reproduces KA-1 to KA-3 (`credit: false`), input to the emulator ADR | PDR | none | FM-1 blinky image; emulator accreditation study `docs/research/emulator-accreditation-and-timer-irq.md` | Emulator ADR decision (Emulation is optional and secondary: event order only) | Boot and GPIO as they exist in rustos `pico2` |
| FM-3 | FW-B1 drivers: WP-SW-01 to WP-SW-07, WP-SW-09 and WP-SW-11 (and WP-SW-14 if package decision 40 adopts REQ-SYS-182) with host mocks, contract tests and dev-board checks | PDR | Bare Pico 2 development board | FM-1; the `cwht-hal-mock` host implementations | Owner merges each work-package pull request as rustos maintainer (ADR-019) | WP-SW-01 to WP-SW-07, 09, 11 (14 conditional) merged upstream |
| FM-4 | Keyer prototype: straight key and iambic paddles with PWM sidetone on the development board; owner HSI verdict on the keyer feel in the PDR decision memo | PDR | Development board with key jack wiring; owner's straight key and paddle (3.5 mm TRS, SI-034) | L2 `SW-KEYER` requirements and cases; FM-3 subset | Owner names the key and paddle (package OA-6) and records the HSI verdict at PDR | WP-SW-01, 02, 03, 09 (the minimal keyer set of RSK-013) |
| FM-5 | Keyer complete: the `SW-KEYER` module implemented to the software design, every TC-SW-KEYER HostUnit case passing, module peer review APPROVED | CDR | none (HostUnit on the host) | FM-4 verdict; firmware architecture ADR at PDR | none | FM-3 traits frozen at their ADRs |
| FM-6 | Receive chain complete: the receive-path firmware (`SW-SYNTH` receive tuning, `SW-AUDIO` mute and restore, `SW-CFG` filter-centre trim, and the firmware CW filter and AGC only if TS-001 selects candidate B) implemented and HostUnit-tested | CDR | Receiver topology and synthesizer selected at PDR (TS-001 and the PDR trade studies); the synthesizer's control bus fixes WP-SW-05 or WP-SW-06 | Firmware architecture ADR at PDR (creates the `SW-<SUB>` modules, 02 section 2.2) | none | WP-SW-03, WP-SW-05 or WP-SW-06 (FW-B1); WP-SW-08 flash store (FW-B2) |
| FM-7 | FW-B2 core logic: all `cwht-core` modules, `cwht-app` composition, all TC-SW HostUnit cases, first coverage and complexity report | CDR | none | FM-5, FM-6 and the remaining modules | none | WP-SW-08, WP-SW-10, WP-SW-12 (FW-B2) |
| FM-8 | Release candidate FW-B3: `release/FW-v0.9.0-rc1`, regression suite, VDD approved for test | TRR | Boards received and receipt-inspected (section 3); integration on the development board before arrival | FM-7 | Owner approves the VDD for test | rustos commit pinned in the VDD |
| FM-9 | Accepted release FW-B4: `release/FW-v1.0.0` after Bench and OnAir NCR closure | SAR | Delivered unit `CWHT-A-001`; tinySA Ultra received with its receipt inspection and TV record before TRR (SI-034, ADR-021) | FM-8 | Owner's Bench and OnAir sessions as licensee; physical configuration audit | rustos pin unchanged since FM-8, or moved by CR |

Hardware and software interactions in the other direction: the CDR pin map and schematic use the FM-3 dev-board results; a driver not demonstrated on hardware by CDR is carried by RSK-013 with its fallback and does not hold the order. Firmware work after CDR (FM-7 to FM-8) runs during the vendor lead time and does not gate the hardware order.

## 2. Cross-project dependency: rustos (SWE-016 d)

cwht firmware depends on rustos, a separate project maintained by the owner (SI-033, ADR-019): every new peripheral driver is a work package of 07 section 19, developed upstream in rustos and merged on the owner's approval. This is a dependency on another project in the sense of SWE-016 d. Its schedule effect: FM-3 and FM-4 (PDR) need WP-SW-01 to WP-SW-07, 09 and 11 merged; FM-6 and FM-7 (CDR) need WP-SW-08, 10 and 12; WP-SW-13 (USB CDC) is optional and deferred to Rev B unless an ADR says otherwise. The risks are RSK-013 (a work package not demonstrated before CDR) and RSK-023 (an upstream change breaking cwht undetected); the control is the pinned commit recorded in the lock and every VDD (`tools/toolchain.lock.md` section 3).

## 3. Vendor lead times (procurement release to TRR)

The CDR order is placed Sunday 2026-09-27 night (Monday 2026-09-28 at PCBWay, GMT+8). PCBWay's final lead time is confirmed by email after its audit and includes fabrication, parts procurement and assembly (`docs/research/pcbway-fabrication-and-assembly.md` F21); the dates below are estimates that the CDR quote and the order confirmation replace.

| Entry | Duration | Source | Estimated window |
|---|---|---|---|
| PCBWay quote response and audit | 1 business day | `pcbway-fabrication-and-assembly.md` F21 (quotation within 1 business day) | 2026-09-28 to 09-29 |
| PCBWay holiday closure | 2026-10-01 to 2026-10-04 (factory closed, GMT+8) | F21; RSK-053 | adds 2 working days to every PCBWay activity in progress |
| Parts import into China for turnkey assembly | at least 5 to 7 working days | F17 ("5-7 working days at least" for parts from overseas distributors); RSK-053 | 2026-09-29 to about 10-07 to 10-09 |
| 4-layer fabrication and stencil | 24 h to 5 days (Advanced PCB 4-layer 5 days, under 1 m²), in parallel with the parts import | F21 (PCBWay builds the PCBs and stencil while parts are in transit) | inside the parts-import window |
| Turnkey assembly | about 3 working days after all parts and PCBs are ready (3 to 5 days advertised) | F21 | about 10-08 to 10-14 |
| CNC aluminum enclosure, anodized | 13 to 15 days to manufacture (one reported small-run order; 6061 milling advertised at 3 to 5 business days) | `docs/research/enclosure-cnc-and-openscad-pipeline.md` A10 (Medium confidence, 2023 order) | 2026-09-29 to about 10-16 to 10-18 with the closure |
| International shipping to the owner | about 3 days courier delivery | A10 (3 days delivery on the reported CNC order); assumed for the PCBA shipment until the CDR quote states it | boards about 10-15 to 10-17; enclosures about 10-19 to 10-21 |
| DigiKey order (items PCBWay does not source) | stocked lines ship directly to the owner; no research finding records a delivery time, so the CDR order confirmation records it | `docs/plan/cost-estimate.md` DigiKey line | before board arrival for stocked lines |
| Zero-stock or single-source lines | early buy at PDR for the build quantity, or an approved alternate in the BOM at CDR | RSK-038 S2, S3; RSK-053 S1 | decided at PDR |

TRR is triggered by the later of board and enclosure arrival plus receipt inspection: about 2026-10-19 to 2026-10-22 on these estimates (the enclosure is the longer path), 4 weeks after the order as the outer bound. A PCBWay quote over 4 weeks, or a PCBWay query open more than 2 working days, triggers the RSK-053 response (the owner answers PCBWay engineering and substitution queries within one working day, RSK-053 S2).

## Schedule risks and levers

1. RID volume at each gate drives re-review cycles (hours each); Claude pre-briefs the top open questions with each package.
2. Layout is the longest single task (Sat night); visual-closure iterations and DRC are planned into it.
3. Live stock checks at CDR may force substitutions; long-lead parts trigger an immediate decision request to the owner.
4. Firmware proof (emulation) continues during vendor lead time and does not gate the hardware order.

Liens policy: a PDR product may be baselined "with liens" when the lien has an owner, a closure plan and a closure gate (CDR). No liens are carried past CDR into procurement without an explicit owner decision recorded in the CDR decision memo.
