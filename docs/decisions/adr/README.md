# Architecture Decision Records (ADR) index

Records of decisions that constrain later work (charter section 5 row "Architecture Decision Records", section 6 id `ADR-NNN`, section 11 rule 6). Process: `docs/process/06-risk-and-decision-analysis.md` section 14 (decision classes, ADR versus trade study, revisiting). Template: `docs/templates/adr.md`. Decision reporting follows SE HB §6.8 (decision needed, criteria, alternatives, evaluation, recommendation, final decision) in the one-page ADR form; a decision that compares alternatives against weighted criteria is a trade study `docs/decisions/trade-studies/TS-NNN-*.md`, and the ADR then records the chosen option.

## Rules

1. One ADR records one decision. File name `ADR-NNN-<slug>.md`; `NNN` is `max(existing) + 1`, three digits, never reused. `tools/traceability.py` resolves `ADR-NNN` in requirement `source_ids` to the file whose name starts with `ADR-NNN`.
2. Status is one of Proposed, Accepted, Superseded by ADR-MMM, Rejected. An Accepted ADR is never edited except to change Status to Superseded and add the superseding id (CM plan `docs/process/05-configuration-and-data-management.md` Table 4-1 row 13); a changed decision is a new ADR.
3. An ADR is Accepted only when section 6 holds the owner's disposition transcribed verbatim with its date (Form 1), or Claude's class 2 record (Form 2). The ADRs below that record decisions the owner had already taken quote the owner's stakeholder input `SI-NNN` from `docs/requirements/l0-stakeholder/stakeholder-inputs.md` as that transcription.
4. A Proposed ADR presents a baseline proposal from research for the owner's decision at the review named in its Status; its section 6 holds the proposed memo wording until the owner's disposition is transcribed.
5. Every ADR names its stakeholder inputs, the research findings that inform it (`docs/research/<file>.md F<n>`), the requirements it creates or changes (ids allocated by the requirement authors; the ADR is cited in `source_ids`), its consequences for interfaces, verification, safety, cost, schedule and risk, and its revisit conditions.
6. Independent review: every ADR is read by a reviewer agent that is not its author before the next life-cycle review (06 section 14.2 row "Review"; 01 section 3.2 row S3). The header field "Independent reviewer" records the result.

## Index

| ID | Title | Status | Decision authority | Stakeholder inputs | Main research sources | Related ids |
|---|---|---|---|---|---|---|
| [ADR-001](ADR-001-class-a-rigor-and-review-gates.md) | Class A software rigor, Criticality-1 system rigor and the five-gate review structure | Accepted | Robin | SI-015, SI-020 | verification-tooling-inventory F18; rustos-toolchain-proof F1 to F6 | RSK-009, RSK-010, TPM-003, TPM-012; `rmm.json`, `se-compliance-matrix.json` |
| [ADR-002](ADR-002-2m-only-rev-a-70cm-ready.md) | 2 m band only in rev A with a 70 cm-ready architecture | Accepted | Robin | SI-002, SI-024, SI-006 | part97-regulatory-basis F1, F2; regulatory-corpus-and-operators F9; 2m-cw-transceiver-reference-designs F16, F20; pa-device-candidates F17 | ADR-013, ADR-016, TPM-009, ICD-TX-ANT |
| [ADR-003](ADR-003-true-cw-a1a-5w.md) | True CW (A1A) emission at 5 W nominal output | Accepted | Robin | SI-003, SI-004 | part97-regulatory-basis F1 to F3, F6 to F8; regulatory-corpus-and-operators F6, F7; pa-device-candidates F18 to F20; rf-exposure-evaluation F2, F7 | HZ-001, HZ-003, HZ-004, RSK-001, RSK-006, RSK-011, TPM-004, TPM-007 |
| [ADR-004](ADR-004-pico2-module-micro-usb.md) | Raspberry Pi Pico 2 module as controller, with its micro-USB for programming and charging | Accepted | Robin | SI-007, SI-022 | rustos-toolchain-proof F1 to F5, F11, F14, F15; pcbway-fabrication-and-assembly F16; power-tree-and-charging F1 to F4; emulator-accreditation-and-timer-irq F13 | HZ-002, HZ-004, RSK-003, RSK-008, ICD-CTL-USB, TPM-009 to TPM-011 |
| [ADR-005](ADR-005-2s-18650-holders.md) | Two 18650 Li-ion cells in series in user-replaceable holders | Accepted | Robin | SI-023 | power-tree-and-charging F3, F5 to F7, F11, F13, F23; pa-device-candidates F18, F19 | HZ-002, RSK-007, ICD-PWR-CELL, TPM-001, TPM-002, TPM-008 |
| [ADR-006](ADR-006-rotary-encoder-tuning.md) | Rotary encoder tuning and a minimal control set | Accepted | Robin | SI-006 | display-and-ui-parts F12, F14 to F16; rustos-toolchain-proof F11 | ADR-009, ADR-016 |
| [ADR-007](ADR-007-pcbway-turnkey-smt-kit-model.md) | PCBWay turnkey surface-mount assembly with owner-soldered through-hole parts (kit model) | Accepted | Robin | SI-009, SI-031 | pcbway-fabrication-and-assembly F15 to F22; pcbway-export-and-vendor-questions Parts 1 to 3; display-and-ui-parts F17, F18 | RSK-004, TPM-014; charter section 12 row "Assembly model" |
| [ADR-008](ADR-008-openscad-freecad-step-pcbway-cnc.md) | Enclosure authored in OpenSCAD, exported to STEP through headless FreeCAD, machined by PCBWay CNC in aluminum | Accepted | Robin | SI-008, SI-032 | enclosure-cnc-and-openscad-pipeline A1 to A11, B1 to B6; verification-tooling-inventory F11; antenna-and-erp F8 | HZ-003, RSK-006, ICD-TX-ANT, TPM-001, TPM-014 |
| [ADR-009](ADR-009-straight-key-and-paddle-trs.md) | Straight key and iambic paddle on one 3.5 mm TRS jack with a built-in keyer | Accepted | Robin | SI-018, SI-034 | keyer-and-key-interfaces F1 to F3, F7, F11; keyer-verification-and-key-input-network F2 to F6, F11, F13, F14; display-and-ui-parts F17 to F19 | HZ-004, RSK-012, SW-KEYER, ICD-CTL-KEY, TPM-013 |
| [ADR-010](ADR-010-semi-break-in-only.md) | Semi break-in only; full QSK excluded from rev A | Accepted | Robin | SI-036, SI-035 | tr-switch-candidates F4, F5, recommendation; keyer-and-key-interfaces F9; keyer-verification-and-key-input-network F11 | HZ-004, TPM-013; T/R trade study at PDR |
| [ADR-011](ADR-011-host-first-software-verification.md) | Host-first software verification through rustos api traits; emulation optional and never for timing | Accepted | Robin | SI-026, SI-010 | rustos-toolchain-proof F2, F7, F8, F13; rp2350-emulation-options; emulator-accreditation-and-timer-irq F5 to F13; keyer-verification-and-key-input-network F8, F9 | RSK-003, ACC-EMU-001 (proposed), 04 section 4 and 5.2 |
| [ADR-012](ADR-012-pa-device-sourcing-constraint.md) | Power-amplifier device must be stocked at DigiKey, Mouser or a PCBWay turnkey distributor | Accepted | Robin | SI-028 | pa-device-candidates F2 to F14, F16, F18, F21; pcbway-fabrication-and-assembly F17, F18 | RSK-005, TPM-004, TPM-007, TPM-014; PA trade study at PDR |
| [ADR-013](ADR-013-synthesizer-by-cost-performance-trade.md) | Synthesizer selected by a cost and performance trade study at PDR | Accepted | Robin | SI-029 | 2m-cw-transceiver-reference-designs F16 to F21, Table 2; cw-selectivity-options 12 to 14; power-tree-and-charging F23 | RSK-002, RSK-005, TPM-002, TPM-006, TPM-008; synthesizer TS at PDR |
| [ADR-014](ADR-014-licensed-operators-only.md) | Licensed operators only; occupational exposure tier for operators, general population for everyone else | Accepted | Robin | SI-030, SI-019 | regulatory-corpus-and-operators F2 to F5; rf-exposure-evaluation F1 to F3, F5 to F8; part97-regulatory-basis F6 to F8 | HZ-001; ADR-015 |
| [ADR-015](ADR-015-operator-model-ops-a-guest-lock.md) | Operator model OPS-A with a receive-only guest lock | Proposed, pending owner decision at SRR | Robin | SI-019, SI-030 | regulatory-corpus-and-operators F2, F4, F5; part97-regulatory-basis F10 | ADR-014 |
| [ADR-016](ADR-016-full-2m-band-coverage.md) | Frequency coverage of the full US 2 m band, 144.000 to 148.000 MHz | Accepted | Robin | SI-024 | part97-regulatory-basis F1, F4, F5, F11; regulatory-corpus-and-operators F8 | RSK-002, TPM-006; ADR-023 |
| [ADR-017](ADR-017-open-source-mit.md) | Open-source publication of the whole design under the MIT license | Accepted | Robin | SI-025 | part97-regulatory-basis F9; pcbway-export-and-vendor-questions F21, F23; pa-device-candidates implication 6 | RMM rows SWE-147, SWE-148, SWE-027 c; ADR-012, ADR-025 |
| [ADR-018](ADR-018-ltspice-telemetry-opt-out.md) | LTspice batch runs with usage telemetry disabled | Accepted | Robin (ratified) | SI-027 | ltspice-batch-macos F1 to F6, F8, F10 to F12; verification-tooling-inventory F12, F13 | `tools/toolchain.lock.md`; tool-validation record |
| [ADR-019](ADR-019-rustos-upstream-drivers.md) | New peripheral drivers are developed upstream in rustos, not in a cwht-local HAL crate | Accepted | Robin | SI-033, SI-007 | rustos-toolchain-proof F7 to F10, F15, F16, work-package table; emulator-accreditation-and-timer-irq F12 | 07 sections 17, 19, 21; CM OQ-5; make/buy TS (SWE-033) |
| [ADR-020](ADR-020-battery-life-target.md) | Battery-life target of 8 hours at a 1:9 transmit-to-receive ratio | Accepted | Robin | SI-034 | power-tree-and-charging F3, F19, F23; pa-device-candidates F19; rf-exposure-evaluation F7; display-and-ui-parts D-UI-02 | TPM-008 (definition change requested), TPM-002; ADR-013 |
| [ADR-021](ADR-021-tinysa-ultra-purchase.md) | Purchase of a tinySA Ultra as the spurious-emission verification instrument | Accepted | Robin | SI-034, SI-021 | part97-regulatory-basis F2; regulatory-corpus-and-operators RF-10, ACTION-9; pa-device-candidates risk 10; keyer-verification-and-key-input-network R-KN6 | RSK-011, TPM-007, OQ-VV-001 |
| [ADR-022](ADR-022-harmonic-suppression-target.md) | Harmonic and spurious suppression: 60 dB design target above the 53 dB regulatory floor at 5 W | Proposed, pending owner decision at SRR | Robin | SI-014, SI-003 | part97-regulatory-basis F2; pa-device-candidates F1, F16 to F18, F20; regulatory-corpus-and-operators F9; tr-switch-candidates TR-05 | RSK-001, RSK-011, TPM-007 (planned value reconciliation) |
| [ADR-023](ADR-023-tcxo-and-band-edge-guard.md) | Frequency reference TCXO of plus or minus 2.5 ppm or better and a 1 kHz band-edge guard | Proposed, pending owner decision at SRR | Robin | SI-014, SI-024, SI-033 | regulatory-corpus-and-operators F7, F8; part97-regulatory-basis F11; keyer-verification-and-key-input-network F11, F12; 2m-cw-transceiver-reference-designs F20, F21 | RSK-002, TPM-006; ADR-013, ADR-016 |
| [ADR-024](ADR-024-keyer-speed-range.md) | Keyer speed range 5 to 50 WPM | Accepted | Robin | SI-033, SI-018 | keyer-and-key-interfaces F4, F6; keyer-verification-and-key-input-network F7, F8, F11, F14; regulatory-corpus-and-operators F6, F7; tr-switch-candidates F4 | HZ-004, RSK-012, TPM-013, SW-KEYER |
| [ADR-025](ADR-025-build-quantity-cap.md) | Build quantity: five boards fabricated, three assembled, a hard cap of five complete units | Accepted (SI-035 default; assembled count confirmed at CDR) | Robin | SI-035, SI-019, SI-025 | pcbway-export-and-vendor-questions F21 to F23; pcbway-fabrication-and-assembly F20, F22; part97-regulatory-basis F9 | RSK-008, TPM-014, 47 CFR 15.23 |

## Decisions expected at PDR (not yet ADRs)

Recorded here so the numbering plan is visible; each becomes `ADR-026` onward when decided, and each trade study produces exactly one ADR (06 section 14.2).

- Receiver architecture and CW selectivity (candidates A and B of `docs/research/cw-selectivity-options.md`): trade study, then ADR.
- Synthesizer and TCXO grade (ADR-013 method; ADR-023 ceiling): trade study, then ADR.
- PA device and ALC topology (ADR-003, ADR-012, ADR-022 constraints): trade study, then ADR.
- T/R element within semi break-in (ADR-010 scope): trade study, then ADR.
- Power tree parts: charger, protector, holders, buck, LDO (ADR-005 proposals): trade study, then ADR.
- Emulator selection and accreditation `ACC-EMU-001` (ADR-011): ADR.
- Firmware architecture: `SW-<SUB>` module set, internal ICDs, single-core rule, NVIC policy (ADR-011, ADR-019): ADR.
- rustos work packages, one ADR each when the trait shape is fixed (ADR-019).
- Enclosure alloy, finish and the build123d comparison on the smoke-test shell (ADR-008): ADR.
- Board thickness 1.0 mm versus 1.6 mm, via fill method, panelization (ADR-007): ADR.
- Audio chain (PWM baseline with DNP I2S footprint, TPA6132A2, level policy) and display parts (ADR-006): trade study or ADR per 06 section 14.1.
- rustos pinning method (CM plan OQ-5): ADR.

## Open items for the owner at SRR (from the ADRs above)

1. ADR-015, ADR-022, ADR-023 need a disposition (Proposed).
2. ADR-002 section 2: confirm the five-point meaning of "70 cm-ready".
3. ADR-013 section 2: confirm the USD 15 per unit cost band for "costs are similar".
4. ADR-020: TPM-008's duty definition and target must change to 8 h at 1:9 (TPM owner).
5. ADR-022: reconcile TPM-007's planned 10 dB margin with the 60 dBc design target (7 dB margin).
6. ADR-010: TPM-013 sub-measure (b) latency of 5 ms is not reachable with a relay first-element lead-in; restate at PDR.
7. ADR-011: `docs/process/07-software-engineering-plan.md` section 17.1 names `rp2350-emu` while the accreditation study proposes c1570/rp2350js as `ACC-EMU-001`; the PDR emulator ADR resolves it.
8. ADR-025: confirm the SI-035 default (3 assembled) or choose 5 assembled at CDR.
