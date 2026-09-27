# ADR-027: Firmware runtime and HAL: rustos (`api` traits and the `pico2` runtime and HAL), extended upstream (TS-002 option A0)

| Field | Value |
|---|---|
| ID | ADR-027 |
| Status | Accepted |
| Date proposed | 2026-09-25 (TS-002 opened and recommended A0) |
| Date decided | 2026-09-26 (SRR decision 107 of `docs/reviews/SRR/decisions-for-owner.md`, owner ruling) |
| Decision class | 1 (`docs/process/06-risk-and-decision-analysis.md` section 14.1 items (h) software acquisition versus development, SWE-033, for the runtime, HAL and PAC; (c) the runtime drivers GPIO, TIMER, PWM, ADC, watchdog, critical section and clocks are in the call path of the components listed in `docs/process/07-software-engineering-plan.md` section 14.1). Trade study: TS-002 (`docs/decisions/trade-studies/TS-002-firmware-runtime-make-buy.md`), the NPR 7150.2D section 6.1 item t make/buy record; this ADR is the one ADR that TS-002 produces (06 section 14.2) |
| Decision authority | Robin (owner, Decision Authority, SMA Technical Authority, and rustos maintainer; the decision fixes the software architecture baseline and the rustos dependency) |
| Author | Claude (ADR author invocation, 2026-09-26, SRR post-ruling work R16) |
| Independent reviewer | TS-002 (the analysis this ADR records): INSP-013 (`docs/reviews/SRR/checklists/trade-studies-ts-001-ts-002.md`) reviewer verdict APPROVED with liens on the committed blob `574cee3d`; software assurance record INSP-027 APPROVED with liens on the same blob (SRR package section 2.4). This ADR file: first reviewed at the INSP-011 post-SRR-ruling delta (`docs/reviews/SRR/checklists/adrs-001-to-025.md`, 2026-09-26, APPROVED with liens F-15 and F-16; delta 2 the same), a reviewer agent that is not its author (README rule 6; 06 section 14.2 row "Review"). The two liens are fixed by the 2026-09-27 errata of section 8, verified at the next INSP-011 delta iteration. The records, not this row, carry every later result |
| Life-cycle phase | Pre-A / A |
| Baseline affected | baseline/srr (functional baseline; software plan, SRR package item H14); allocated baseline at PDR (firmware architecture) |
| Change request | none (pre-baseline) |

## 1. Context

The firmware needs a runtime and a hardware-abstraction layer for the RP2350 on the Pico 2 module (ADR-004). The layer must be verified at Class A rigor (ADR-001), tested host-first through injected traits (SI-026, ADR-011, REQ-SYS-128), and fit the single-priority, SIO-only design rules (REQ-SYS-129; 07 section 7.7). The owner directed Rust on rustos (SI-007) with new drivers developed upstream in rustos (SI-033, ADR-019). NPR 7150.2D still requires the acquisition-versus-development record (SWE-033; 07 section 17.2), and the SRR package carried it as item H14. TS-002 compared four alternatives: A0, rustos extended upstream; A1, `rp235x-hal` with `cortex-m-rt`; A2, Embassy; A3, RTIC 2 over `rp235x-hal`. Without this decision FW-B0 cannot close and the rustos work packages of FW-B1 cannot start (07 section 3.2).

- Driving inputs and expectations: SI-007, SI-015, SI-025, SI-026, SI-033
- Requirements that constrain the decision: REQ-SYS-127 (firmware language and platform), REQ-SYS-128 (host-testable application layering), REQ-SYS-129 (single interrupt priority design rule)
- Hazards in play (`docs/safety/hazards.json` 0.5.0-pha): the hazards reached through the components of 07 section 14.1 whose firmware controls run on the runtime drivers: HZ-001, HZ-002, HZ-003, HZ-004, HZ-005, HZ-007 and HZ-014 (TS-002 header row "Related requirements and hazards"); HZ-008 through control K7 (independent frequency verification before PA_EN), whose counter is work package WP-SW-14, required since SRR decision 40 adopted REQ-SYS-182 (owner ruling 2026-09-26, key decision K2)
- Research consulted: `docs/research/rustos-toolchain-proof.md` F2, F6, F7, F8, F13 (what rustos provides, its gaps, the demonstrated host testing through injected traits) and its work-package table (WP-13, the hygiene item); `docs/research/emulator-accreditation-and-timer-irq.md` F7, F8, F12 (emulator coverage against the work packages)
- Guidance consulted: SWE-033, SWE-027, SWE-211, SWE-146; NPR 7150.2D section 6.1 item t (make/buy record); SE HB §6.8
- Assumptions the decision rests on, and how and by when each is confirmed:
  1. The owner, as rustos maintainer, reviews and merges the work-package pull requests on the schedule of 07 section 19. Tracked by RSK-013; re-scored at PDR, and a Red score at a gate is revisit trigger 2 (section 7).
  2. An upstream rustos change made for another user does not break a cwht contract undetected. Tracked by RSK-023; controlled by the pinned rustos commit recorded in every VDD and by the contract tests of each work package (07 sections 17.1 and 19).
  3. The rustos hygiene item (`rustos-toolchain-proof.md` WP-13: clippy warnings, rustfmt hunks, `api` unit tests) is done before FW-B0 so the `-D warnings` gate passes. Confirmed by the FW-B0 toolchain proof (`TC-SW-TOOL-001`) re-run before PDR.
  4. The rustos licence and manifest work items approved in SRR decision 110 (MIT licence, `publish = false` and `license` fields, and the CS-06 `// SAFETY:` comments above the 36 unsafe sites) clear gate G5. Confirmed by the FW-B0 re-run (`cargo deny check bans licenses sources` and `tools/unsafe_audit.py --check`).

## 2. Decision

The cwht firmware is built on the owner's rustos: the portable `api` traits and the `pico2` runtime and HAL, with zero external runtime, HAL or PAC crates. rustos is extended upstream, as ADR-019 records, by the work packages of `docs/process/07-software-engineering-plan.md` section 19: WP-SW-01 (TIMER0 time base and alarms), WP-SW-02 (SIO input sampling), WP-SW-03 (PWM), WP-SW-04 (ADC), WP-SW-05 (I2C master), WP-SW-06 (SPI master), WP-SW-07 (watchdog), WP-SW-08 (flash store), WP-SW-09 (critical section and NVIC helpers), WP-SW-10 (UART), WP-SW-11 (clocks and PLL, safety-critical), WP-SW-12 (CRC-32 in `cwht-core`), and WP-SW-14 (frequency counter for the frequency verification unit, safety-critical; required because SRR decision 40 adopted REQ-SYS-182). WP-SW-13 (USB CDC device) stays optional and is recommended against for revision A, as 07 section 19 states. Each work package is a sprint of 07 section 3.4 with the file inventory of section 3.5 (trait in `api`, implementation in `pico2` with a datasheet citation on every register access, mock in `cwht-hal-mock`, contract tests, dev-board check), proposed as its own ADR when its trait shape is fixed, and merged on the owner's approval as rustos maintainer; a row closes only on the completion rule at the end of 07 section 19. `rp235x-hal` with `cortex-m-rt`, Embassy and RTIC are not used. The decision is revisited when any of the four triggers of TS-002 section 8, adopted with this decision, occurs (section 7).

## 3. Alternatives considered

| Option | Description | Why not chosen (or why chosen) |
|---|---|---|
| A0 (chosen) | rustos `api` plus `pico2`, extended upstream by the 07 section 19 work packages; hand-written registers with datasheet citations; zero external crates | Highest total, 400 of 500 (80 %); robust under every weight and score perturbation of TS-002 section 6 (smallest lead 80.6 points); the only alternative with host testing through injected traits demonstrated here and with mechanisms that match the design rules and the emulator credit scope; matches SI-007 and SI-033 |
| A1 | `rp235x-hal` with `cortex-m-rt` and `embedded-hal` traits | Not chosen: 265 (53 %); ten or more external crates to verify to developed-code level under Class A (SWE-027 item e, SWE-211), SVD-generated PAC not reviewed against the datasheet (07 section 17.4) |
| A2 | Embassy (`embassy-rp`, `embassy-executor`, `embassy-time`) | Not chosen: 220 (44 %); the same verification burden, and async GPIO waits on IO_BANK0 edge interrupts that the emulator mis-decodes (`emulator-accreditation-and-timer-irq.md` F8) |
| A3 | RTIC 2 over `rp235x-hal` | Not chosen: 220 (44 %); the same verification burden, and priority-based preemption that REQ-SYS-129 does not permit |
| Do nothing | rustos as it stands (boot, vector table, GPIO only) | Not viable: no interrupt path, clocks, timer, PWM, ADC, I2C, SPI, watchdog or flash store; cannot meet REQ-SYS-042 or any timed requirement (TS-002 section 3.2) |

Pruned before scoring (TS-002 section 3.2): a cwht-local `pico2-ext` crate (SI-033; ADR-019 option B), an own HAL over an `svd2rust` PAC (ADR-019 option D; SWE-146), RTIC over rustos `pico2`, the pico-sdk in C through FFI and a C RTOS (SI-007). The weighted matrix, the sensitivity analysis, the per-alternative risks and the reviewer dissent D-2 are in TS-002 sections 5 to 7 and 9.

## 4. Consequences

### 4.1 Requirements created or changed

| Requirement | Relationship | Note |
|---|---|---|
| REQ-SYS-127 (firmware language and platform) | allocated; cites ADR-019; implemented by this decision | Cross item to the requirement authors: add ADR-027 to its `source_ids` |
| REQ-SYS-128 (host-testable application layering), REQ-SYS-129 (single interrupt priority design rule) | allocated; cite ADR-011; constrain this decision (criteria C5 and C6 of TS-002) | No change |
| Software requirement (no id allocated yet): drivers live in rustos `pico2` behind `api` traits with no cwht-local register access, verified by Inspection (`cargo tree`) | not created at SRR; ADR-019 section 4.1 names it; written by the software requirement authors with the firmware architecture ADR at PDR | TS-002 section 8 "Impacts" |
| REQ-SW-HAL-* trait contracts | not created at SRR; written with each work package at PDR (07 section 19) | One set per work package ADR |

### 4.2 Interfaces, design and code

- ICDs affected: `ICD-CTL-SW` (pin map and peripheral allocation, PDR); the rustos `docs/icd/rp2350/` register extractions for TIMER, PWM, ADC, WATCHDOG and QMI (ADR-019 section 4.2; 07 section 19 column "Register ICD available in rustos")
- Design elements created or changed: `rustos/api` traits and `rustos/firmware/pico2` drivers per work package; `cwht-hal-mock` host implementations; `cwht-core` CRC-32 (WP-SW-12)
- New `SW-<SUB>` modules created by this ADR: none
- ICDs created by this ADR: none

### 4.3 Verification and safety

- Verification cases to add or change: the contract tests and dev-board checks of 07 section 19 per work package (HostUnit against the mock; Bench with `credit: false` on the bare development board); the register-sequence comparison for peripherals inside the `ACC-EMU-001` candidate scope (07 section 9.4 item 4); the FW-B0 toolchain proof `TC-SW-TOOL-001` re-run after the hygiene and SRR decision 110 work items
- Evidence class implications: HostUnit is the primary software evidence (ADR-011); PIO-based WP-SW-14 is outside the `ACC-EMU-001` candidate scope, so its closing evidence is HostUnit plus dev-board and Bench checks (07 section 19)
- Hazard analysis update required: no new cause or control; WP-SW-11 and WP-SW-14 implement safety-critical functions already listed in 07 section 14.1 and HZ-008 control K7
- Safety-critical software scope (SWE-134 provisions) changed: no; the drivers under the 07 section 14.1 components are in scope already, and the unsafe audit (CS-06, CS-07) covers every rustos unsafe site

### 4.4 Cost, schedule, risk

- BOM, fabrication, enclosure or lead-time impact: none; no cost-model delta (TS-002 section 8)
- Gate affected: SRR (SWE-033 part of item H14 closes on this decision); FW-B0 (toolchain proof); FW-B1 and FW-B2 (work packages per 07 sections 3.2 and 19); PDR (work-package ADRs and trait shapes)
- Risks opened, closed or re-scored: RSK-013 (rustos driver effort, 9 Yellow) and RSK-023 (single maintainer, 8 Yellow) carry a history entry naming TS-002 and this ADR (cross item to the risk register owner); the hygiene risk (5 Yellow) is carried as a step of RSK-013 (the research WP-13); RSK-003, RSK-010, RSK-015, RSK-020 and RSK-021 unchanged
- TPMs affected: none

## 5. Compliance and tailoring

RMM row SWE-033 (NPR 7150.2D, Class A): the implementation text cites TS-002 and this ADR as the acquisition-versus-development record (cross item to the RMM owner, TS-002 section 8 "Impacts"). No tailoring.

## 6. Decision record

> Owner (2026-09-26, SRR session, `docs/reviews/SRR/minutes.md` section "Rulings"): "I concur with your recommendations for the key decisions."

Recorded ruling (minutes, same section): key decision K9 of package section 13.1.1, which contains SRR decision 107, is ruled as recommended; the ruling text is the "Recommendation" cell of decision 107 in `docs/reviews/SRR/decisions-for-owner.md` Part 1: "Approve A0 with the four revisit triggers of TS-002 section 8."

> Owner (2026-09-26, SRR disposition, `docs/reviews/SRR/minutes.md` section "Disposition"): "I approve of this and the SRR."

Class 1 (item (h)): the decision is recorded in TS-002 section 10 (cross item to the TS-002 author: fill section 10 with this ruling; the TS-002 Status line reads Decided). The SRR decision memo carries the same ruling. SRR decision 110 (the rustos licence, MIT, and the two rustos work items), ruled in the same key decision K9, is recorded in the software plan and the tool records, not in this ADR.

## 7. Related

- Supersedes: none
- Superseded by: none
- Trade study: TS-002 (`docs/decisions/trade-studies/TS-002-firmware-runtime-make-buy.md`)
- Review where presented: SRR, decided 2026-09-26 (SRR decision 107, key decision K9); ADR-004, ADR-011 and ADR-019 are the decisions it builds on
- Revisit conditions (the four triggers of TS-002 section 8, adopted by SRR decision 107): (1) the owner as rustos maintainer declines an `api` addition a work package needs (the ADR-019 revisit condition); (2) RSK-013 turns Red at a gate; (3) a qualified Rust runtime or HAL for Cortex-M33 with Class A-grade evidence becomes available; (4) the owner directs a CR that relaxes CS-02. A trigger is handled by the revisiting rule of 06 section 14.6; a changed decision is a new ADR that supersedes this one.

## 8. Change log

- 2026-09-26: created under SRR decision 107 (owner ruling 2026-09-26, key decision K9: approve TS-002 option A0 with the four revisit triggers of TS-002 section 8), at the next free number as the decision row and the ADR README "Decisions expected at PDR" list planned. Author: Claude (ADR author invocation, SRR post-ruling work R16).
- 2026-09-27 (PDR errata, WP-PDR-14; SRR liens L-6 and, where named, L-4 and L-7): Independent reviewer row names the INSP-011 post-SRR-ruling delta as the first review of this file instead of "pending" (F-16); hazard line stamp 0.4.3-pha changed to 0.5.0-pha, the version at HEAD, after re-checking the line against it (F-13; for ADR-015, 022, 023 and 026 also SRR lien L-7); section 4.1 third row describes the software requirement without the placeholder id `REQ-SW-NNN` (F-15). Route: the SRR decision memo carries these findings as liens to be fixed in the product before the PDR readiness declaration (RFA-SRR-006: "Fix each finding in its product"); they are applied by the ADR correction route the owner approved as SRR decision 105 (corrections outside section 2, each logged in this section), as the README paragraph "PDR errata" records. The decision of section 2 is unchanged. Author: Claude (ADR author invocation, WP-PDR-14).
