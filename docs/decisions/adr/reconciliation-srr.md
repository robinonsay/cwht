# ADR reconciliation register for SRR (INSP-011)

**Purpose.** This file applies the findings of the independent review INSP-011 (`docs/reviews/SRR/checklists/adrs-001-to-025.md`, findings F-01 to F-10) to the ADR set without editing an Accepted ADR. `docs/process/05-configuration-and-data-management.md` Table 4-1 row 13 says an ADR is "Superseded, never edited; the status field is the only editable line", and README rule 2 says the same for Accepted ADRs. Each finding's fix names the owner as the one who chooses the route for Accepted ADRs, so this register holds every correction in a form that serves any route the owner picks (section 7, ruling R-1). **Author:** Claude (ADR author invocation applying INSP-011, 2026-09-25). **Independent reviewer:** pending, INSP-011 iteration 2. **Inputs, at the state read on 2026-09-25:** `docs/safety/hazards.json` version 0.3.0-pha (HZ-001 to HZ-015); `docs/requirements/sys/requirements.json`, `docs/requirements/tx/requirements.json`, `docs/requirements/sw/sw-keyer/requirements.json`; `docs/requirements/l0-stakeholder/expectations.json`; `docs/process/rmm.json` as committed in 4e3f891; `docs/process/07-software-engineering-plan.md` section 14.1; `docs/process/06-risk-and-decision-analysis.md` section 14.1; `docs/decisions/trade-studies/TS-001-receiver-and-pa-concept.md` and `TS-002-firmware-runtime-make-buy.md` (both Draft).

## 1. What changed in the ADR files, and what did not

| File | Change in this revision | Findings applied in the file | Authority for the edit |
|---|---|---|---|
| ADR-015 (Proposed) | Decision class row, Assumptions line, hazard line, section 3 class note, section 4.1 ids, section 4.3 hazard and scope lines, reviewer field | F-01, F-02, F-03 | README rule 4: a Proposed ADR is revised until the owner's disposition is transcribed |
| ADR-022 (Proposed) | As ADR-015; the "class 2 content" sentence corrected; the ALC value stated as the design target of REQ-SYS-012 | F-01, F-02, F-03, F-04 (ALC wording) | README rule 4 |
| ADR-023 (Proposed) | As ADR-015; operating range aligned to REQ-SYS-010 and REQ-SYS-114 (-10 to +45 C); TS numbering note | F-01, F-02, F-03, F-04 | README rule 4; F-04 fix "align ADR-023 before its SRR disposition" |
| ADR-025 (Accepted) | Status line set to "Accepted"; the qualifier stays in section 6, which already states it | F-09 | Table 4-1 row 13: the status field is the editable line |
| ADR-026 (new, Proposed) | Restates ADR-010 with the hang and lead-in values of REQ-SYS-044, REQ-SYS-136, REQ-SYS-160, REQ-SYS-161; supersedes ADR-010 on acceptance (package decision 47) | F-01, F-02, F-03, F-04 for ADR-010 | README rule 2: a changed decision is a new ADR |
| README.md | Index row for ADR-026; status of ADR-025; link to this register; PDR list and open items updated | F-01 (display class), F-03 (TS ids) | The index is not an ADR |
| ADR-001 to ADR-014, ADR-016 to ADR-021, ADR-024 (Accepted) | **Not edited.** Their corrections are sections 2 to 6 below, applied by the route of ruling R-1 | F-01 to F-08, F-10 | Table 4-1 row 13 forbids the edit until the owner rules |

## 2. Decision class, trade study and hazards per ADR (F-01, F-02)

Column "Hazards in play" is the replacement for line 22 of each ADR, re-derived against `hazards.json` 0.3.0-pha in both directions: the hazards whose record names the ADR, the `hazard_ids` of the requirements that cite the ADR (section 4), and the hazards whose causes or controls the decision fixes. Column "HA update" is the replacement for the "Hazard analysis update required" line of section 4.3. Class 1 items are the letters of 06 section 14.1: (a) architecture choice, (b) single-source or critical part, (c) a choice touching a hazard or a component of 07 section 14.1, (f) a change to a KDR requirement or an MOE, (g) Analysis substituted for Test on a regulatory requirement, (h) software acquisition versus development. "Owner-directed" means section 6 of the ADR quotes an SI-NNN that fixes the choice.

| ADR | Status | Decision class (06 section 14.1) | Trade study | Hazards in play (0.3.0-pha) | HA update | 07 section 14.1 components touched |
|---|---|---|---|---|---|---|
| ADR-001 | Accepted | 2: a process convention (the rigor election and the gate structure); it changes no hazard cause or control. Decision authority stays Robin because it fixes baseline content | none | HZ-001 to HZ-015. The election binds the SWE-134 provisions to the firmware roles of HZ-001 to HZ-008, HZ-010, HZ-011, HZ-012 and HZ-014 (`docs/safety/hazard-analysis.md` section 6.2). Replaces "HZ-001 to HZ-005" | yes. The section 4.3 scope line reads, per charter section 10: keying, PA enable, charging supervision, thermal protection, audio output limiting and the shared safe-state manager, plus mission-critical frequency control and configuration load; 07 section 14.1 is the authoritative list (F-05) | all (sets their rigor) |
| ADR-002 | Accepted | 2: the band scope is a stakeholder expectation (NGO-008, CON-022) and "70 cm-ready" is a recorded convention; no class 1 item | none | none new. HZ-001, HZ-006 and HZ-008 are evaluated for 144 to 148 MHz only (the third harmonic of 2 m falls in the 70 cm band, HZ-008) | no | none |
| ADR-003 | Accepted | 1: (c) HZ-001, HZ-003, HZ-004, HZ-006, HZ-008, HZ-012. Owner-directed (SI-003, SI-004) | TS-001 (draft), sub-decision P, for the PA device-and-supply concept; TS-003 at PDR for the line-up. No TS for the emission type and the 5 W ceiling: ruling R-2 item (i) | HZ-001, HZ-003, HZ-004 (as written) plus HZ-006 (bystander exposure at 5 W), HZ-008 (REQ-SYS-012 carries it; the 25 uW cap binds at 5 W) and HZ-012 (RF burn at 5 W) | yes: HZ-001, HZ-003, HZ-004, HZ-006, HZ-008 and HZ-012 all scale with the 5 W level | SW-TXSEQ (power step, ALC set-point), SW-KEYER |
| ADR-004 | Accepted | 1: (b) single-source part (the Pico 2 module); (c) HZ-002, HZ-004, HZ-011, HZ-014; (h) for the runtime. Owner-directed (SI-007, SI-022) | TS-002 (draft) for the runtime and HAL; no TS for the module: R-2 item (i) | HZ-002 (charge path through the module connector), HZ-004 (image integrity through the USB loader), HZ-011 (charging while transmitting: REQ-SYS-090, REQ-SYS-092), HZ-014 (firmware load leaving an unsafe state: REQ-SYS-132, REQ-SYS-133; control K4 relies on USB being present during every load) | yes: HZ-002, HZ-011, HZ-014. The section 4.1 row "transmit inhibited by hardware while charging" is HZ-011 control K1 (REQ-SYS-092), not an HZ-002 control | SW-PWR, SW-BOOT, pico2 drivers |
| ADR-005 | Accepted | 1: (a) power architecture; (b) battery cell and charger; (c) HZ-002, HZ-007, HZ-011. Owner-directed for the cell format (SI-023) | none yet: the power tree parts TS at PDR (README "Decisions expected at PDR"). No TS for the cell format: R-2 item (i) | HZ-002 (as written) plus HZ-007 (discharge-side faults: protector, fuse, reverse insertion, holders; REQ-SYS-084 to REQ-SYS-087, REQ-SYS-166) and HZ-011 (charging paused while receiving, REQ-SYS-093) | yes: HZ-002, HZ-007, HZ-011 controls | SW-PWR |
| ADR-006 | Accepted | 1: (b) the display is a critical part; (c) the firmware volume law runs in SW-AUDIO (HZ-005) and encoder tuning input is the mission-critical SW-DISPLAY. Owner-directed for the encoder (SI-006) | none: the display and audio choices go to a trade study at PDR (class 1 (b)); line 40 "part-level choices are class 2" is wrong for the display (section 6 item E-5) | HZ-005 (volume law in firmware: controls K2 default cap and K3 limiter run in SW-AUDIO) and HZ-013 (knob-to-bezel clearance of the printed knobs, REQ-SYS-111). Replaces "none" | yes: HZ-005 and HZ-013. Line 63 "no" is wrong | SW-AUDIO, SW-DISPLAY |
| ADR-007 | Accepted | 1: (c) HZ-015 names this ADR; HZ-007 cause C8. Owner-directed (SI-009, SI-031) | none: R-2 item (i); board details in TS-004 at PDR | HZ-015 (owner hand assembly; REQ-SYS-137 and REQ-SYS-138 carry it; control K3 is this ADR's part split) and HZ-007 (cause C8, soldering with cells in the holders). Replaces "none directly" | yes: HZ-015 K3 and HZ-007 C8. Line 62 "no" is wrong | none |
| ADR-008 | Accepted | 1: (a) enclosure concept; (c) HZ-003, HZ-009, HZ-013. Owner-directed (SI-008, SI-032) | none: R-2 item (i); alloy and finish ADR at PDR | HZ-003 (as written) plus HZ-009 (SMA jack retained by the enclosure boss, anodize masking: REQ-SYS-105, REQ-SYS-107) and HZ-013 (machined edges and pinch points: REQ-SYS-110, REQ-SYS-111, REQ-SYS-168) | yes: HZ-009 K1, K4, K6 and HZ-013 K1, K3, K4 are enclosure design controls. Line 66 "no" is wrong | none |
| ADR-009 | Accepted | 1: (c) HZ-001, HZ-004, HZ-010, HZ-014, and SW-KEYER. Owner-directed (SI-018, SI-034) | none: R-2 item (i); key-type detection and envelope shaping TS at PDR | HZ-004, HZ-001 (as written) plus HZ-010 (ESD and RF pickup on the key inputs: REQ-SW-KEYER-019, REQ-SYS-047 to REQ-SYS-051) and HZ-014 (interlock re-run after every reset: REQ-SW-KEYER-022) | yes: HZ-004 (as written), HZ-010, HZ-014 | SW-KEYER, pico2 GPIO |
| ADR-010 | Accepted; ADR-026 proposed to supersede it | 1: (a) T/R architecture class; (c) HZ-004, HZ-005, HZ-008. Owner-directed (SI-036) | none for the mode: R-2 item (i); T/R element TS at PDR | as ADR-026 section 1: HZ-004, HZ-005, HZ-008 | yes: HZ-004, HZ-005 (ADR-026 section 4.3) | SW-TXSEQ, SW-KEYER |
| ADR-011 | Accepted | 1: (a) firmware task structure (single NVIC priority, run-to-completion handlers); (c) it fixes the verification approach of every component of 07 section 14.1. Owner-directed (SI-026) | TS-002 (draft) for the runtime the approach builds on; emulator selection ADR at PDR | HZ-004 (as written) plus every hazard with a firmware role, whose software controls take HostUnit as primary evidence: HZ-001 to HZ-008, HZ-010, HZ-011, HZ-012, HZ-014 | no: the hazard verification notes already assign HostUnit and Bench evidence | all of 07 section 14.1 |
| ADR-012 | Accepted | 1: (b) RF power device (this ADR fixes a mandatory criterion of its selection); (c) HZ-001, HZ-003, HZ-008. Owner-directed (SI-028) | TS-001 (draft), sub-decision P, applies the criterion (PD54008L-E recommended); TS-003 at PDR | HZ-003 (as written) plus HZ-001 and HZ-008 (REQ-SYS-012 carries both) | yes: HZ-008 control K2 names the Mitsubishi RD07MUS2B line-up "sourced per SI-028", a device this ADR excludes as consignment-only (section 5 row V-6). Line 62 "no" is wrong | SW-TXSEQ (ALC set-point) |
| ADR-013 | Accepted | 1: (b) synthesizer. Owner-directed method (SI-029) | synthesizer and reference TS, not yet created (section 6 item E-9) | HZ-008 (causes C7 and C8: a frequency-control software fault, or the synthesizer unlocked or locked to a wrong value; REQ-SYS-154, REQ-SYS-182). Replaces "none" | yes, at the TS outcome: HZ-008 C8 is re-assessed for the chosen part | SW-SYNTH |
| ADR-014 | Accepted | 1: (c) HZ-001, HZ-006. Owner-directed (SI-030) | none: R-2 item (i); the rule text leaves one lawful configuration | HZ-001 (as written) plus HZ-006 (general-population tier for everyone who is not the operating licensee; REQ-SYS-121 carries both) | yes: HZ-001 and HZ-006 | SW-TXSEQ (power step and tune limits) |
| ADR-015 | Proposed | fixed in the file (class 1 (c)) | in the file | in the file (HZ-006, HZ-008) | in the file | SW-TXSEQ (guest lock) |
| ADR-016 | Accepted | 1: (c) HZ-008, and the carrier limits of the mission-critical SW-SYNTH. Owner-directed (SI-024) | none: R-2 item (i) | HZ-008 (out-of-band emission; REQ-SYS-008 and REQ-TX-002 carry it). Replaces "none" | yes: HZ-008 K4 and K7 rest on the carrier range. Line 61 "no" is wrong | SW-SYNTH |
| ADR-017 | Accepted | 2: licence choice; no class 1 item | none | none (as written) | no | none |
| ADR-018 | Accepted | 2: tool configuration (as its section 3 states) | none | none (as written) | no | none |
| ADR-019 | Accepted | 1: (h) runtime and HAL acquisition versus development (SWE-033); (c) the pico2 drivers are in 07 section 14.1. Owner-directed (SI-033) | TS-002 (draft) | HZ-004 (as written) plus the hazards whose firmware controls run on the GPIO, TIMER, PWM, ADC, watchdog, critical-section and clock drivers: HZ-001 to HZ-008, HZ-010, HZ-011, HZ-012, HZ-014 | no: the hazard records already name the runtime components | pico2 drivers (WP-SW-01, 02, 03, 04, 07, 09, 11) |
| ADR-020 | Accepted | 2: it sets the MOE-004 target before any baseline and decides no hazard control; the low-battery cutoff that ends the run is HZ-007 control K4, used and not changed | none | none (as written); HZ-007 K4 is used, not changed | no | none |
| ADR-021 | Accepted | 1: (c) HZ-008 (control K5 is spurious verification with this instrument); the purchase avoids the class 1 (g) trade. Owner-directed (SI-034) | none: R-2 item (i) | HZ-008 (REQ-SYS-017 and REQ-TX-007 cite this ADR and carry it). Replaces "none" | yes: HZ-008 K5 names the instrument. Line 60 "no" is wrong | none |
| ADR-022 | Proposed | fixed in the file (class 1 (c)) | in the file | in the file (HZ-008, HZ-001, HZ-003) | in the file | SW-TXSEQ (ALC set-point) |
| ADR-023 | Proposed | fixed in the file (class 1 (b), (c)) | in the file | in the file (HZ-008, HZ-006) | in the file | SW-SYNTH, SW-TXSEQ (envelope) |
| ADR-024 | Accepted | 1: (c) HZ-004, HZ-008, and SW-KEYER. Owner-directed range (SI-033) | none: R-2 item (i) | HZ-004 (as written) plus HZ-008 (50 WPM is the worst case of the keying bandwidth: REQ-SYS-015 and REQ-TX-006 carry it) | yes: HZ-008 K4. Line 63 "no" is wrong | SW-KEYER |
| ADR-025 | Accepted | 2: build quantity under a regulatory cap (spends money, so Robin decides) | none | none (as written) | no | none |
| ADR-026 | Proposed | in the file (class 1 (a), (c)) | in the file | in the file (HZ-004, HZ-005, HZ-008) | in the file | SW-TXSEQ, SW-KEYER |

Result: 16 of the 22 Accepted ADRs are class 1 by the letter of 06 section 14.1. ADR-012, ADR-013 and ADR-019 have a trade study route (TS-001, the synthesizer and reference TS, TS-002). ADR-003, 004, 005, 006, 007, 008, 009, 010, 011, 014, 016, 021 and 024 have no TS for the owner-directed part of the choice. The template admits an ADR without a TS only for class 2 (`docs/templates/adr.md` section 3 comment). Ruling R-2 in section 7 asks the owner for the route.

## 3. Assumptions line per Accepted ADR (F-01)

Each row is the section 1 line "Assumptions the decision rests on, and how and by when each is confirmed" (template section 1; SE HB §6.8.1.2.5 asks that assumptions be documented with the recommendation). ADR-010 is covered by ADR-026 section 1, and the Proposed ADRs carry the line in the file.

| ADR | Assumptions, and how and by when each is confirmed |
|---|---|
| ADR-001 | (1) The toolchain gives Class A evidence except MC/DC instrumentation (RSK-010): toolchain proof, package item H12, before the SRR readiness declaration. (2) Independent agent review stands in for IV&V: the owner's approval of the RMM tailoring rows in the SRR decision memo. (3) The weekend dates are targets: reassessed at each gate's readiness declaration |
| ADR-002 | (1) The five-point meaning of "70 cm-ready" is what the owner intends: owner confirmation at SRR (README open item 2). (2) The 70 cm enhancing criterion adds no rev A cost beyond the synthesizer choice: checked in the synthesizer and reference TS at PDR against TPM-009 |
| ADR-003 | (1) A turnkey-stocked device delivers 5 W from 6.0 to 8.4 V (TS-001 sub-decision P recommends PD54008L-E): TS-003 at PDR and the CDR stock check. (2) The RF Exposure Evaluation supports 5 W under the occupational tier: PDR (REQ-SYS-121). (3) The thermal path carries continuous key-down at 5 W: thermal budget at PDR (REQ-SYS-112) |
| ADR-004 | (1) The module VBUS path carries 500 mA continuously: Bench test on a spare Pico 2 (PWR-USB-02) with TS-005 at PDR. (2) The RP2350 stepping is A2, so the E9 input policy applies: receipt inspection of the modules before TRR. (3) The owner solders the castellated module (ADR-007): owner-solder inspection before first power-on |
| ADR-005 | (1) Two single-cell holders fit the pocket envelope: printed fit check before CDR (REQ-SYS-103). (2) Unprotected 18650 cells with on-board protection meet the HZ-002 and HZ-007 controls: power tree TS at PDR. (3) 3000 mAh class cells give 90 percent usable capacity (Low confidence, ADR-020): discharge curve digitised at PDR |
| ADR-006 | (1) The owner accepts the detented encoder feel: HITL session at PDR. (2) The memory LCD is legible without a backlight (REQ-SYS-165, TBR): display trade at PDR. (3) Encoders, buttons and display are rated to -10 C (REQ-SYS-114): datasheet Inspection at PDR |
| ADR-007 | (1) PCBWay turnkey stocks every surface-mount line (REQ-SYS-140): stock checks with date and time at PDR and CDR. (2) The owner hand-assembles under the HZ-015 procedure: TRR safety line (HZ-015 K5). (3) PCBWay accepts DNP lines for owner-soldered parts: vendor confirmation before CDR (`pcbway-export-and-vendor-questions.md` Part 3) |
| ADR-008 | (1) The FreeCAD CSG import gives a single-solid STEP that passes the acceptance checks: PDR smoke-test shell. (2) PCBWay accepts the STEP plus drawing: instant quote at PDR. (3) Masking and anodize callouts are honoured: receipt inspection before TRR |
| ADR-009 | (1) The owner's key and paddle are wired tip = dit (SI-034): plug check at the PDR HITL session. (2) The debounce and network values (TBR) suit the owner's contacts: bounce capture before the TBR closes at PDR. (3) Menu-only key-type selection is acceptable: HITL session at PDR |
| ADR-011 | (1) The host mock represents silicon behaviour for application logic: contract tests against mock and dev board from FW-B1, before PDR. (2) An emulator can be accredited for event ordering: ACC-EMU-001 in the emulator ADR at PDR. (3) The single-priority design meets every timing budget: software architecture analysis at PDR |
| ADR-012 | (1) At least one stocked device meets 5 W at 144 MHz: TS-001 sub-decision P, then TS-003 at PDR. (2) Stock persists to the order: stock check with date and time at CDR |
| ADR-013 | (1) "Similar cost" means within USD 15 per unit: owner confirmation at SRR (README open item 3). (2) The Low-confidence VHF phase-noise figures are resolved before scoring: datasheet plots read (action 20) before the TS is scored at PDR |
| ADR-014 | (1) Every operator is licensed and has the handbook exposure information: handbook walkthrough with a licensed friend at SAR. (2) The OET 65 Supplement B method with the SAR analogy is an adequate evaluation: RF Exposure Evaluation at PDR, updated with measured antenna gain at CDR and measured power at TRR |
| ADR-016 | (1) The synthesizer covers 144.000 to 148.000 MHz plus the BFO offset: synthesizer and reference TS at PDR. (2) The band-edge check closes by tinySA or by Analysis: tinySA RBW verified on receipt (ACTION-9) |
| ADR-017 | (1) The rustos licence allows MIT publication of cwht: third-party register check (07 section 17.1) at PDR. (2) Units are never marketed (47 CFR 15.23(a)): SAR configuration audit counts units (ADR-025) |
| ADR-018 | (1) The `CaptureAnalytics` key persists across LTspice updates: the wrapper checks it before every run; a toolchain change triggers re-accreditation |
| ADR-019 | (1) The owner, as rustos maintainer, merges the work-package pull requests on the schedule: 07 section 21 risk "rustos driver effort", reviewed at PDR. (2) The pinned path dependency is reproducible: OQ-CM-005 at PDR |
| ADR-020 | (1) 90 percent usable capacity to 3.0 V per cell (Low confidence): discharge curve digitised at PDR. (2) 45 percent key-down within transmit periods represents the owner's operating: owner confirmation at SRR (section 6 of the ADR). (3) The synthesizer and front-end trades keep the expected receiver build: power budget at PDR with 20 percent margin |
| ADR-021 | (1) The tinySA RBW is adequate for the band-edge measurement, or the Analysis path stands: RBW verified on receipt (ACTION-9). (2) A calibrated 30 to 40 dB attenuator rated for 5 W is obtained: cost model line and receipt inspection before TRR. (3) The known-answer check passes: TV-NNN record before TRR |
| ADR-024 | (1) TIMER0 alarms keep element timing within REQ-SYS-042 at the keyer test point under display and encoder load: REQ-SW-KEYER-014, Bench on the dev board (credit false) before PDR and on the delivered unit after TRR. (2) The 15 WPM default suits the population: package decision 45 at SRR |
| ADR-025 | (1) Lending units to friends is "personal use" under 47 CFR 15.23(a) (Low confidence, `pcbway-export-and-vendor-questions.md` F23): a revisit condition; the owner may seek confirmation. (2) The PCBWay fabrication minimum stays 5 boards: CDR quote |

## 4. ADR back-reference from the requirements (F-03)

Generated on 2026-09-25 from `source_ids` of the three requirement files, from every record of `hazards.json` 0.3.0-pha and from `expectations.json` (68 requirement citations of 23 ADRs; ADR-001, ADR-018 and ADR-026 are cited by none). It is the ADR-to-requirement cross-check that the template's section 4.1 comment asks for. Reproduction: load each file with Python `json`, collect every `source_ids` entry matching `ADR-NNN`, and search each hazard and expectation record for `ADR-NNN`. Generating this table in `tools/traceability.py` is proposed as a cross item, so the table stays current without hand edits.

| ADR | Requirements citing it in `source_ids` (hazard ids of each, TBR marked) | Hazards whose record names it | Expectations naming it |
|---|---|---|---|
| ADR-001 | none | none | none |
| ADR-002 | REQ-SYS-145 | none | none |
| ADR-003 | REQ-SYS-001; REQ-SYS-012 (HZ-001, HZ-003, HZ-008) TBR; REQ-TX-001 | none | none |
| ADR-004 | REQ-SYS-090 (HZ-011); REQ-SYS-126 | none | none |
| ADR-005 | REQ-SYS-080 | none | none |
| ADR-006 | REQ-SYS-057; REQ-SYS-165 TBR | none | none |
| ADR-007 | REQ-SYS-137 (HZ-015); REQ-SYS-138 (HZ-015) | HZ-015 | none |
| ADR-008 | REQ-SYS-109 | none | none |
| ADR-009 | REQ-SYS-038; REQ-SYS-039; REQ-SYS-174; REQ-SW-KEYER-001; REQ-SW-KEYER-002 (HZ-004); REQ-SW-KEYER-003; REQ-SW-KEYER-004; REQ-SW-KEYER-005; REQ-SW-KEYER-019 (HZ-004, HZ-010); REQ-SW-KEYER-022 (HZ-004, HZ-014) TBR; REQ-SW-KEYER-024 (HZ-004) | none | none |
| ADR-010 | REQ-SYS-044 TBR; REQ-SYS-160 TBR; REQ-SYS-161 TBR; REQ-SW-KEYER-018 TBR; REQ-SW-KEYER-032 TBR | none | none |
| ADR-011 | REQ-SYS-128; REQ-SYS-129 | none | none |
| ADR-012 | REQ-SYS-012 (HZ-001, HZ-003, HZ-008) TBR; REQ-SYS-140 | none | none |
| ADR-013 | REQ-SYS-024 TBR; REQ-SYS-031 TBR | none | CON-028 |
| ADR-014 | REQ-SYS-121 (HZ-001, HZ-006) | none | none |
| ADR-015 | REQ-SYS-006; REQ-SYS-065 (HZ-006); REQ-SYS-066 (HZ-006); REQ-TX-003 (HZ-008, HZ-006) TBR | none | none |
| ADR-016 | REQ-SYS-008 (HZ-008) TBR; REQ-SYS-021; REQ-TX-002 (HZ-008) TBR | none | none |
| ADR-017 | REQ-SYS-148 | none | none |
| ADR-018 | none | none | none |
| ADR-019 | REQ-SYS-127 | none | none |
| ADR-020 | REQ-SYS-094 | none | none |
| ADR-021 | REQ-SYS-017 (HZ-008); REQ-TX-007 (HZ-008) | none | MOE-006, MOE-010 |
| ADR-022 | REQ-SYS-018 (HZ-008) TBR; REQ-TX-008 (HZ-008) TBR; REQ-TX-009 (HZ-008) TBR; REQ-TX-010 (HZ-008) TBR; REQ-TX-011 (HZ-008) TBR | HZ-008 | none |
| ADR-023 | REQ-SYS-008 (HZ-008) TBR; REQ-SYS-009 (HZ-008) TBR; REQ-SYS-010 (HZ-008) TBR; REQ-SYS-154 (HZ-008) TBR; REQ-SYS-182 (HZ-008) TBR; REQ-TX-002 (HZ-008) TBR; REQ-TX-003 (HZ-008, HZ-006) TBR; REQ-TX-013 (HZ-008) TBR | HZ-008 | none |
| ADR-024 | REQ-SYS-015 (HZ-008) TBR; REQ-SYS-041; REQ-TX-006 (HZ-008) TBR; REQ-SW-KEYER-013; REQ-SW-KEYER-014; REQ-SW-KEYER-015; REQ-SW-KEYER-016 | none | none |
| ADR-025 | REQ-SYS-125 | none | none |
| ADR-026 | none | none | none |

## 5. Section 4.1 placeholder resolution (F-03) and value reconciliation (F-04)

### 5.1 Placeholders in section 4.1 of the Accepted ADRs

Each placeholder row resolves to the ids the requirement authors allocated, or reads "not created" with the reason. "Cites" means the requirement lists the ADR in `source_ids`. Requirements that implement a row without citing the ADR are proposed for a `source_ids` addition by the requirement authors (cross items). ADR-001, ADR-017, ADR-018 and ADR-021 have no placeholder row; for ADR-017 and ADR-021 the 4.1 text "none" is now incomplete, because REQ-SYS-148 cites ADR-017 and REQ-SYS-017 and REQ-TX-007 cite ADR-021.

| ADR | Placeholder row (abridged) | Resolves to | Note |
|---|---|---|---|
| ADR-002 | REQ-SYS-NNN frequency coverage | REQ-SYS-008 (transmit), REQ-SYS-021 (receive), REQ-TX-002 | They cite ADR-016, not ADR-002; REQ-SYS-145 (band-dependent functions partitioned) cites ADR-002 and REQ-SYS-146 (reserved band control) implements point (1) |
| ADR-002 | tagging rule `revA` / `70cm-ready` | not a requirement: a tagging convention checked at requirements validation | |
| ADR-003 | REQ-SYS-NNN emission A1A only | REQ-SYS-001 (cites), REQ-TX-001 (cites) | |
| ADR-003 | REQ-SYS-NNN output power 5.0 W, tolerance plus or minus 0.5 dB | REQ-SYS-012 (cites; plus or minus 1 dB, TBR) | Value difference: section 5.2 row V-3 |
| ADR-003 | REQ-SYS-NNN spurious per 97.307(e) | REQ-SYS-017 and REQ-TX-007 (cite ADR-021), REQ-SYS-018 and REQ-TX-008 (cite ADR-022) | |
| ADR-003 | REQ-SYS-NNN keying envelope and 26 dB bandwidth | REQ-SYS-014, REQ-SYS-015 (cites ADR-024), REQ-TX-005, REQ-TX-006 (cites ADR-024) | |
| ADR-003 | REQ-SYS-NNN power steps and default power | REQ-SYS-011, REQ-SYS-063, REQ-SYS-064, REQ-TX-004 | None cites ADR-003 |
| ADR-004 | REQ-SYS-NNN controller constraint | REQ-SYS-126 (cites) | |
| ADR-004 | charge input 500 mA default, never above 1.5 A | REQ-SYS-090 (cites; HZ-011) | |
| ADR-004 | REQ-SYS-NNN transmit inhibited by hardware while charging | REQ-SYS-092 (HZ-011, HZ-014) | An HZ-011 control, not HZ-002 (section 2) |
| ADR-004 | REQ-SW-NNN firmware image format, hash, CRC trailer | REQ-SYS-132 (image integrity), REQ-SYS-133 (update over USB) at L1; the firmware-wide `docs/requirements/sw/requirements.json` is not created (PDR) | |
| ADR-005 | REQ-SYS-NNN two user-replaceable 18650 cells | REQ-SYS-080 (cites) | |
| ADR-005 | REQ-PWR-NNN charge profile, balancing, protection, temperature window | not created at L2 (PWR file due at PDR); L1 counterparts REQ-SYS-081 to REQ-SYS-089, REQ-SYS-166, REQ-SYS-167 | |
| ADR-005 | REQ-SYS-NNN operating supply 6.0 to 8.4 V, 5.0 W above 6.4 V | REQ-SYS-012 (6.4 to 8.4 V), REQ-SYS-097 (transmit inhibit below 6.4 V), REQ-SYS-098 (power-down) | No single supply-window requirement was created |
| ADR-006 | REQ-SYS-NNN controls | REQ-SYS-057 (cites), REQ-SYS-058, REQ-SYS-059, REQ-SYS-060, REQ-SYS-061, REQ-SYS-165 (cites) | |
| ADR-006 | REQ-CTL-NNN encoder electrical interface | not created (CTL L2 at PDR) | |
| ADR-006 | REQ-SW-NNN tuning step and velocity law | REQ-SYS-058 at L1; L2 not created (PDR) | |
| ADR-007 | REQ-SYS-NNN assembly constraint | REQ-SYS-137 (cites; HZ-015) | |
| ADR-007 | fabrication and assembly data package | REQ-SYS-139 (circuit board fabrication rules) at L1; REQ-ME at CDR not created | |
| ADR-007 | REQ-SYS-NNN no owner-soldered hidden-pad package | REQ-SYS-138 (cites; HZ-015) | |
| ADR-008 | REQ-SYS-NNN enclosure constraint | REQ-SYS-109 (cites), REQ-SYS-175 (antenna port on one end) | |
| ADR-008 | REQ-ME-NNN design data package; DFM rules; anodize masking; SMA boss | not created at L2 (ME file due at PDR); L1 counterparts REQ-SYS-105 (boss load path), REQ-SYS-107 (masked contact area), REQ-SYS-110 (edge break) | |
| ADR-008 | CAD build reproducible from the command line | not a product requirement: tooling rule of 05 section 8.2 step 3 and `tools/toolchain.lock.md` | |
| ADR-009 | REQ-SYS-NNN straight key and REQ-SYS-NNN paddle | REQ-SYS-038, REQ-SYS-039 (both cite) | |
| ADR-009 | REQ-CTL-NNN jack pin-out; inputs, thresholds, network, ESD | REQ-SYS-174 (cites), REQ-SYS-047 to REQ-SYS-051 at L1; REQ-SW-KEYER-019 (cites); REQ-CTL at PDR | |
| ADR-009 | REQ-SW-KEYER-NNN modes, menu selection, interlock, timeouts | REQ-SW-KEYER-001 to 005, 019, 022, 024 (cite); REQ-SW-KEYER-006 to 012, 026; REQ-SYS-040, 052, 053, 054, 056 | |
| ADR-009 | REQ-CTL-NNN hardware PA-enable cutoff | REQ-SYS-055 at L1 (HZ-004 K5) | |
| ADR-011 | REQ-SW-NNN application logic on `api` traits only | REQ-SYS-128 (cites) | |
| ADR-011 | REQ-SW-NNN register access cites the datasheet | not created as a requirement: charter section 9 Inspection rule and 07 coding standard | |
| ADR-011 | REQ-SW-NNN emulation asserts ordering only | not a product requirement: V&V rule of `docs/process/04-verification-and-validation.md` sections 4 and 5.2 | |
| ADR-011 | REQ-SW-NNN single NVIC priority, PWM slices, GPIO via SIO | REQ-SYS-129 (cites) | |
| ADR-011 | REQ-SW-NNN clock driver TICKS and bounded waits | not created: the contract of WP-SW-11 in 07 section 19 (CS-37) | |
| ADR-012 | REQ-SYS-NNN sourcing constraint | REQ-SYS-140 (cites), REQ-SYS-178 (owner-procured parts sourcing) | |
| ADR-012 | REQ-TX-NNN device-agnostic filter goals | REQ-TX-009, REQ-TX-010, REQ-TX-011 (cite ADR-022) | |
| ADR-012 | REQ-TX-NNN power-path ratings for full-charge output | not created; REQ-TX-015 (at most 6.3 W, TBR) and REQ-SYS-153 (high pack voltage lockout) bound the output; RSK-047 carries the rating question to TS-003 and TS-006 | |
| ADR-013 | REQ-RX-NNN and REQ-TX-NNN LO phase noise, spurious, current | not created (after the synthesizer and reference TS at PDR); L1 REQ-SYS-024 and REQ-SYS-031 cite ADR-013 | |
| ADR-013 | REQ-SYS-NNN frequency stability and display accuracy | REQ-SYS-010 (cites ADR-023) | |
| ADR-014 | REQ-SYS-NNN RF exposure evaluation deliverable (RFX-01) | REQ-SYS-121 (cites; HZ-001, HZ-006) | |
| ADR-014 | REQ-SYS-NNN exposure controls (RFX-02) | REQ-SYS-011, REQ-SYS-063, REQ-SYS-064, REQ-SYS-122, REQ-SYS-171, REQ-SYS-172 | None cites ADR-014; cross item proposes adding it to REQ-SYS-122 and REQ-SYS-171 |
| ADR-014 | licensed operators; unlicensed persons receive-only or supervised (OPS-02, OPS-03, DOC-02) | ConOps text and REQ-SYS-122, REQ-SYS-124; guest lock REQ-SYS-065, REQ-SYS-066 (cite ADR-015) | |
| ADR-016 | REQ-SYS-NNN coverage and carrier range | REQ-SYS-008, REQ-SYS-021, REQ-TX-002 (all cite) | |
| ADR-016 | REQ-SW-NNN transmit inhibit outside the carrier range (RF-01) | REQ-SYS-009 (cites ADR-023), REQ-SYS-182 | |
| ADR-016 | REQ-SW-NNN presets and CW-segment indication (OPS-01) | not created: carried to the PDR UI design | |
| ADR-019 | REQ-SW-NNN drivers in rustos behind `api` traits | REQ-SYS-127 (cites) | |
| ADR-019 | REQ-SW-HAL-* trait contracts | not created (PDR, with each work-package ADR) | |
| ADR-020 | MOE-NNN battery life | MOE-004 | |
| ADR-020 | REQ-SYS-NNN 8 h at 1:9 and 6 h at 1:4 | REQ-SYS-094 (cites), REQ-SYS-095 | |
| ADR-020 | REQ-PWR-NNN receive current budget, low-battery cutoff | REQ-SYS-098 (power-down) at L1; REQ-PWR not created (PDR) | |
| ADR-024 | REQ-SYS-NNN speed 5 to 50 WPM | REQ-SYS-041 (cites), REQ-SW-KEYER-015 (cites) | |
| ADR-024 | REQ-SW-KEYER-NNN element timing, tolerance, latency | REQ-SYS-042 (plus or minus 1 percent or 0.5 ms at the keyer test point), REQ-SW-KEYER-013 and 014 (cite; plus or minus 0.5 percent or 0.2 ms), REQ-SYS-043 and REQ-SW-KEYER-017 (latency) | Section 5.2 row V-2 |
| ADR-024 | REQ-SW-KEYER-NNN default 15 WPM, 1 WPM steps, non-volatile, adjustable while sending | REQ-SYS-041, REQ-SYS-135, REQ-SYS-136, REQ-SW-KEYER-016 (cites) | |
| ADR-024 | REQ-SW-KEYER-NNN automatic identification at most 20 WPM | not created: rev A has no automatic identification memory; REQ-SYS-068 (identification reminder) | |
| ADR-025 | REQ-SYS-NNN build quantity cap | REQ-SYS-125 (cites) | |

### 5.2 Values that differ between an ADR and the requirements citing it

| Row | ADR text | Requirement text | Disposition in this revision | Owner ruling |
|---|---|---|---|---|
| V-1 | ADR-010 section 2: "adjustable hang time (default 8 dits of the displayed speed; 6.1 dits and a fixed 50 to 2500 ms selectable)"; "first-element lead-in after a changeover is at most 12 ms" | REQ-SYS-044 and REQ-SW-KEYER-032: hang of 3 to 30 dits (TBR); REQ-SYS-161: the same lead-in of at most 12 ms (TBR) for every element of an over | ADR-026 (Proposed) restates ADR-010 with the requirement values | Package decision 47 at SRR: accepting it makes ADR-026 Accepted and ADR-010 "Superseded by ADR-026" |
| V-2 | ADR-024 section 2: "accurate to plus or minus 1 percent of nominal or plus or minus 0.5 ms, whichever is larger" at the engine output | REQ-SYS-042 (L1): plus or minus 1 percent or 0.5 ms at the keyer test point; REQ-SW-KEYER-013 (L2): plus or minus 0.5 percent or 0.2 ms | Disputed as a contradiction: the ADR value is the L1 value, and REQ-SW-KEYER-013's rationale makes the tighter L2 value a margin allocation below the parent. A keyer meeting the L2 value meets the ADR value. Erratum E-10 moves the ADR's reference point to the keyer test point | none needed for the value; the erratum rides route R-1 |
| V-3 | ADR-003 section 4.1: "tolerance proposed plus or minus 0.5 dB with ALC across 6.4 to 8.4 V" | REQ-SYS-012: "within +/-1 dB (TBR)"; its TBR plan names plus or minus 0.5 dB as the ALC target | Section 2 of ADR-003 decides only the 5 W ceiling, so no decision changes: plus or minus 1 dB is the requirement, plus or minus 0.5 dB the ALC design target (HZ-001 K4, HZ-003 K4, HZ-008 K3; ADR-022 section 2). Erratum on the 4.1 row via route R-1 | The TBR closes at PDR with TS-003 and TS-006, as the requirement's plan states |
| V-4 | ADR-023 section 2: "-10 to +50 C proposed" | REQ-SYS-010 and REQ-SYS-114: -10 C to +45 C (TBR) | Aligned in the file (ADR-023 is Proposed) | With the ADR-023 disposition at SRR |
| V-5 | ADR-022 section 2: filter goals "measured at the assembled filter's own terminals", two bands | REQ-TX-009 to REQ-TX-011: attenuation "between its PA output and antenna port", and a third band, 40 dB from 576 MHz to 1.5 GHz | Recorded in ADR-022 section 4.1; not changed in the proposal, because the reference point is an owner choice | With the ADR-022 disposition at SRR: which reference point stands, and whether the third band joins the ADR |
| V-6 | ADR-012 section 2: consignment-only parts (the RD07MUS2B line-up) are excluded | `hazards.json` HZ-008 control K2: "Mitsubishi RD07MUS2B line-up baseline, sourced per SI-028" | Cross item to the hazard analysis author: K2 should name the TS-001 sub-decision P device class or "the device selected by TS-003" | none (a hazard-record correction) |

## 6. Errata for the Accepted ADRs (F-05 to F-08, F-10, and the TS references of F-03)

Each item is a literal replacement, to be applied by the route of ruling R-1.

| Item | ADR and line | Current text (abridged) | Replacement | Finding |
|---|---|---|---|---|
| E-1 | ADR-001 line 22 | "Hazards in play: HZ-001 to HZ-005 ..." | the ADR-001 row of section 2 | F-02, F-05 |
| E-2 | ADR-001 line 60 | "... apply to keying, PA enable, charging and thermal control (charter section 10)" | "... apply to keying, PA enable, charging supervision, thermal protection, audio output limiting and the shared safe-state manager, and to mission-critical frequency control and configuration load (charter section 10; the authoritative list is 07 section 14.1)" | F-02, F-05 |
| E-3 | ADR-001 line 72 | "Current disposition summary: 74 FC, 16 T, 10 NA of 100 rows (`docs/process/rmm.md`)" | "Current disposition summary: see `docs/process/rmm.md`, generated from `rmm.json`; as committed in 4e3f891, `rmm.json` has 75 FC, 17 T and 8 NA of 100 rows" | F-05 |
| E-4 | ADR-005 line 18 | "A 5 W VHF PA at 55 to 65 percent efficiency draws about 1.6 to 2.2 A during key-down" | "A 5 W two-stage VHF PA line-up draws 11.4 W DC during key-down, about 1.6 A at 7.2 V and 1.9 A at 6.0 V, a line-up efficiency of 44 percent (`docs/research/pa-device-candidates.md` F19; its 55 to 65 percent is the drain efficiency of the final stage alone)" | F-07 |
| E-5 | ADR-006 line 40 | "part-level choices are class 2 and are recorded here as proposals for the PDR UI design" | "the display part is class 1 (b) and is selected by the display and audio trade study at PDR; the encoder and button parts are recorded here as proposals for the PDR UI design" | F-01 |
| E-6 | ADR-017 line 72 | "RMM rows SWE-147, SWE-148 and the reuse and Government-rights rows (SWE-214 to SWE-217) are NA per charter section 12" | "RMM rows SWE-147 and SWE-148 are NA per charter section 12 ('Open personal project; license recorded in the repo'); SWE-214 to SWE-217 (NPR 7150.2D sections 2.1.5.13 to 2.1.5.16) are Center Director requirements with no App. C row, institutional and outside the RMM (charter section 12)" | F-06 |
| E-7 | ADR-017 line 23; ADR-025 lines 23 and 28 | "2.803(a) marketing definition" (line 23 of each); "(47 CFR 2.803(a) marketing definition as quoted in the research)" (ADR-025 line 28) | cite as a research finding: "the 47 CFR 2.803(a) marketing definition as quoted in `docs/research/pcbway-export-and-vendor-questions.md` F21 (High confidence in that report's confidence table; 47 CFR 2.803 is not in the verbatim corpus `docs/references/md/regulatory/`, and F21 notes an amendment published 2026-09-11 that the 2026-09-23 issue text did not yet carry)" | F-08 |
| E-8 | ADR-019 lines 23 and 67 | "Work-package table WP-01 to WP-14"; "PDR (WP-01 to WP-04, WP-09, WP-11 needed for the keyer prototype)" | "Work-package table (research numbering, mapped to WP-SW-01 to WP-SW-13 in 07 section 19)"; "PDR (WP-SW-01 to WP-SW-07, WP-SW-09 and WP-SW-11, per the PDR row of 07 section 3.1; the keyer prototype needs them)" | F-10 |
| E-9 | ADR-004 lines 39 and 91; ADR-011 line 90; ADR-019 lines 36, 39, 73 and 85 | "the make/buy TS", "make/buy trade study of 07 section 17.2" | "TS-002 (`docs/decisions/trade-studies/TS-002-firmware-runtime-make-buy.md`, Draft; decided at SRR; its decision becomes a new ADR)" | F-03 |
| E-9 | ADR-013 lines 28 and 83 | "trade study `TS-NNN`", "synthesizer TS-NNN" | "the synthesizer and reference trade study (not yet created; it takes the next free TS number when created, because the label TS-002 in `docs/design/concept.md` section 11.2 now belongs to the firmware make/buy study)" | F-03 |
| E-9 | ADR-003 line 90; ADR-012 lines 39 and 86 | "PA device and topology TS at PDR" | "TS-001 (concept-level receiver and PA trade, Draft, sub-decision P) and TS-003 (PA device and line-up) with TS-006 (ALC and envelope topology) at PDR, `docs/design/concept.md` section 11.2" | F-03 |
| E-10 | ADR-024 line 28 | "Element and space timing at the engine output is accurate to plus or minus 1 percent of nominal or plus or minus 0.5 ms" | "Element and space timing at the keyer test point is accurate to plus or minus 1 percent of nominal or plus or minus 0.5 ms (REQ-SYS-042); the keyer firmware is allocated plus or minus 0.5 percent or 0.2 ms (REQ-SW-KEYER-013)" | F-04 (row V-2) |
| E-11 | ADR-003 line 48 | "tolerance proposed plus or minus 0.5 dB with ALC across 6.4 to 8.4 V" | "REQ-SYS-012: within plus or minus 1 dB (TBR, closing at PDR); plus or minus 0.5 dB is the ALC design target" | F-04 (row V-3) |
| E-12 | ADR-004 line 49 | "new, hazard control HZ-002" | "REQ-SYS-092; HZ-011 control K1 (also HZ-014 K4)" | F-02 |
| E-13 | every Accepted ADR, line 11 | "Independent reviewer: Pending: reviewer agent invocation before SRR ..." | "INSP-011 (`docs/reviews/SRR/checklists/adrs-001-to-025.md`), with the iteration and result the reviewer records" | README rule 6 |

## 7. Owner rulings requested

These rulings are routed to `docs/reviews/SRR/decisions-for-owner.md` as a cross item. Until the owner rules, this register is the controlling correction of the Accepted ADRs, and the README index links it from every affected row.

**R-1. Route for correcting the Accepted ADRs.** Options:
- (A) One-time pre-baseline correction. Before the `baseline/srr` tag, Claude folds sections 2, 3, 5.1 and 6 into the Accepted ADR files: the Decision class row, the Assumptions line, the hazard and 4.1 lines, the errata and the reviewer field. Decision sections (section 2 of each ADR) are not touched, and any change of decision content goes by a new ADR, as ADR-026 does. This needs a sentence in 05 Table 4-1 row 13 allowing that correction under an INSP record with the owner's approval.
- (B) This register stays as the controlled supplement, baselined with the ADRs, and the README index links it.
- (C) A superseding ADR for each affected Accepted ADR (19 new ADRs besides ADR-026).

Recommendation: (A). It leaves one self-contained file per decision at the functional baseline, and it changes no decision. Default if the owner does not rule: (B).

**R-2. Class 1 choices recorded without a trade study.** Proposed customization of 06 section 14.1, recorded in the SEMP as customization (charter section 1: adjusting formality needs no waiver):
- (i) A class 1 choice that the owner has made as a stakeholder input (SI-NNN), where that direction leaves one viable alternative, is recorded by an ADR alone. Section 3 lists the alternatives in one line each with the reason each is not viable (SE HB §6.8.1.2.2: "a decision matrix for a major decision even if only one alternative is determined to be viable"). Section 1 records the class 1 items and the Assumptions line. The design choices that implement the direction (parts, topology, values) stay class 1 and go through the trade study named in section 7 of the ADR. This covers ADR-003, 004, 005, 006, 007, 008, 009, 010 (and ADR-026 for the mode), 011, 014, 016, 021 and 024 for their owner-directed part.
- (ii) A class 1 value or policy that Claude proposes for the owner's decision (ADR-015, ADR-022, ADR-023, ADR-026 for its values), where the research analysis leaves one viable option, is recorded by an ADR alone when the owner's disposition says so. Otherwise a TS-NNN is opened before the decision.

If the owner declines (i), each ADR listed there needs a TS-NNN before `baseline/srr`, or a waiver of the 06 section 14.1 rule. Recommendation: adopt (i) and (ii).
