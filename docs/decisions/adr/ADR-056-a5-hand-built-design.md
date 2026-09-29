# ADR-056: Hand-built A5 design for the first cwht (TS-012 alternative A5)

| Field | Value |
|---|---|
| ID | ADR-056 |
| Status | Proposed. Section 2 item 1, the A5 decision, was taken by the owner in chat on 2026-09-29 (section 6, Form 1). Items 2 to 4 are for the owner's confirmation at PDR session S1 (OD-10 part 1). The record stays Proposed while its independent review and software assurance pair run, because README rule 2 allows no edit of an Accepted ADR and review fixes must be made in place. It becomes Accepted by a Status-line edit once the review record is APPROVED and section 6 holds the S1 disposition of items 2 to 4 |
| Date proposed | 2026-09-29 (this record; TS-012 first presented A5 as a finalist in revision 2, 2026-09-27) |
| Date decided | 2026-09-29 for item 1 (owner, in chat; `docs/plan/status/status-2026-09-29.md` sections 4 and 5). Items 2 to 4: at S1, pending |
| Decision class | 1 (`docs/process/06-risk-and-decision-analysis.md` section 14.1 items (a) architecture choice: receiver topology, PA topology, LO scheme, power architecture, enclosure concept; (b) critical parts: RF power device, synthesizer, TCXO, CW filter, battery charger, display; (c) choices that touch HZ-002, HZ-003, HZ-004, HZ-005, HZ-007, HZ-008 and HZ-015 and the components of `docs/process/07-software-engineering-plan.md` section 14.1; (d) the owner asked for the study; (f) changes to KDR requirements REQ-SYS-012, 112, 137, 140). Trade study: TS-012 (`docs/decisions/trade-studies/TS-012-design-to-cost-hand-built.md`). This ADR is the one ADR that TS-012 produces (06 section 14.2) |
| Decision authority | Robin (owner, Decision Authority). The choice is class 1, and through CR-018 it changes baseline content, including KDR requirements. The decision spends no money: the order waits for the ordering gate (section 2 item 1(b)) |
| Author | Claude (technical data manager invocation, WP-PDR-54 part 1, 2026-09-29) |
| Independent reviewer | Pending. The review is by an independent reviewer with a software assurance pair, because the decision constrains components of 07 section 14.1 (PDR work plan WP-PDR-54; 07 section 2.1.1). The lead SE assigns the record ids and paths. The record must be APPROVED before S1, because OD-10 part 1 rests on it (plan section 3.0a "Order"). The study this ADR records was reviewed as INSP-110 iteration 3 re-issue 2 (`docs/reviews/PDR/checklists/ts-012-design-to-cost.md`, `c5e4930`, reviewer APPROVED) and INSP-118 iteration 2 (`ts-012-design-to-cost-software-assurance.md`, `ff2fd8c`, assurance APPROVED). Both record verdicts are held at NEEDS CHANGES for Minor liens |
| Life-cycle phase | B |
| Baseline affected | baseline/srr (functional baseline) through CR-018 and CR-003 revision 4 and CR-006 revision 3, all dispositioned at S1 (OD-40); baseline/pdr (the allocated baseline is written on this architecture) |
| Change request | none for this record. The requirement changes it causes are carried by CR-018 (the re-baseline CR, WP-PDR-53), CR-003 revision 4 and CR-006 revision 3 |

## 1. Context

The SRR concept (A0: PCBWay turnkey 4-layer board, PD54008L-E PA, display and encoders, in-radio charging, about USD 610 per unit over three units) did not fit the owner's later direction. The first radio costs at most USD 300 all in, with a target of USD 200. The owner solders it on bare boards at home. A Morse-code audio menu replaces the display (status note 2026-09-27 sections 6, 8, 10 and 11, as TS-012 section 2 quotes them). TS-012 re-derived the architecture under that ceiling. It scored five alternatives and took two finalists, A4 and A5, through six pre-order analyses and three review cycles. The study recommended A4 with the TCXO and A5's diode-ring mixer (300 against A5's 270, A2 at 305 not analysed; TS-012 sections 5 and 8). Every PDR trade and analysis of WP-PDR-19 to 28, and the architecture, L2 files, ICDs and schematic after them, depend on this choice. Without it the allocated baseline cannot be written.

- Driving inputs and expectations: SI-013, SI-022, SI-028, SI-031, SI-034. The owner inputs of status note 2026-09-27 sections 6, 8, 10 and 11 take the next free SI ids when CR-018 appends them. Expectations: CON-010, CON-015, CON-026, NGO-027, NGO-028, MOE-007, MOE-013 (TS-012 section 2).
- Requirements that constrain the decision: REQ-SYS-012 and REQ-SYS-112 (KDR; A5 holds each only with the delta of section 4.1); REQ-SYS-017 and REQ-SYS-018 (25 uW and 60 dBc; ADR-022); REQ-SYS-120 (two independent conditions for RF output); REQ-SYS-182 and REQ-SYS-154 (independent frequency verification; held as written on route R3); REQ-SYS-147 (cost); REQ-SYS-013 (survival into SWR 10:1).
- Hazards in play (`docs/safety/hazards.json` 0.5.0-pha): HZ-002, HZ-003, HZ-004, HZ-005, HZ-007, HZ-008, HZ-015.
- Research consulted: the seven block research reports and the three architecture and three judge reports that TS-012 section 11 lists; `docs/research/pa-device-candidates.md` F8, F10, F16 to F20; `docs/research/a5-parts-lifecycle-2026-09-29.md` (`f193784`, 39 of 39 parts Active).
- Analysis records the study rests on: the six pre-order analyses of TS-012 section 9 tables R5-1 and R6-1 (thermal, PA drive and output power, harmonic LPF, receiver BPF, transmit clock spurs, keying envelope); the receiver BPF note `docs/design/analysis/rx-bpf-ts012.md` revision 4 (`63122e7`; INSP-117 iteration 3 re-issue 1, reviewer APPROVED, `123f048`).
- Guidance consulted: SE HB §6.8; 06 sections 14.1, 14.2, 14.5 and 14.6.
- Assumptions the decision rests on, and how and by when each is confirmed:
  1. The ordering-gate worst case, recomputed from the owner's browser reads (OD-42), stays at or below USD 300 after guards G1 to G4. This is confirmed by WP-PDR-38 before S2 and again at the ordering gate after CDR. If it fails, revisit condition (c) of TS-012 section 10 applies.
  2. Every A5 part is still Active at the maker when ordered. This was confirmed on 2026-09-29 (`f193784`) and is re-checked at the ordering gate (TS-012 section 10, revisit condition (b)).
  3. The open thermal items close with a no-cost or gate-affordable change: long-session cells 58.9 C against 55 C; PETG face 60.1 C against 60 C; module case about 106 C against the 90 C guidance. This is confirmed by the WP-PDR-28a record before S1. If an item does not close, it goes to the owner (TS-012 section 10, revisit condition (d)).
  4. The WP-PDR-19 front-end redesign recovers REQ-SYS-022 at the TC-SYS-017 corner, where it now reads -134.9 dBm and TPM-005 is Red. This is confirmed by the WP-PDR-19 record before S2. If it fails, it is a TS-012 revisit condition.

## 2. Decision

1. **A5 is the hand-built design of the first cwht (decided 2026-09-29).** It is TS-012 alternative A5, "hybrid H1", as recorded in TS-012 section 10 (revision 7, `6497900`):
   - **Transmitter.** A Mitsubishi RA07M1317M-501 module PA, bought from RF Parts and driven by a Mini-Circuits GVA-84+. A spare GVA-84+ is bought.
   - **Frequency generation.** An Adafruit 2045 Si5351A breakout with its 25 MHz crystal removed and an Epson TG2520SMN TCXO on XA.
   - **Receiver.** A single-conversion superhet:
     - G5V-2 T/R relay, with pole B grounding the receiver input in transmit;
     - a 2 + 3 + 4 resonator band-pass filter at IF 8 MHz between two MMBFJ310 grounded-gate stages;
     - a diode-ring mixer (four 1N5711W, two BN-43-202 cores);
     - a 6-pole 500 Hz ladder of 8.000 MHz crystals matched on the NanoVNA;
     - a JFET product detector and analog audio, with PWM-derived AGC and volume.
   - **User interface.** A Morse-code audio menu with two buttons and two potentiometers, in place of the display and encoders (TS-012 section 8.7).
   - **Power.** Two P28A cells in 1043P holders with S-8252AAO pack protection. The cells are charged outside the radio in an XTAR MC1. USB on the radio loads firmware only.
   - **Boards.** Two JLCPCB 2-layer 1.6 mm bare boards, soldered by the owner.
   - **Enclosure.** An owner-printed PETG case, with the Boyd 530002B02500G sink as the end wall behind a wrap-around finger guard.
   - **Design items.** The design items D-1 to D-18 of TS-012 section 8.14 at their A5 values. D-15 is at the note revision 4 figures: 75.37 dB worst-case image rejection over REQ-SYS-114, and +/-0.62 % alignment acceptance at 20 to 30 C. D-17 is frequency verification on route R3. D-18 is the PA_EN permit, with its open lien.

   The block diagram is TS-012 section 8.1. The controller stays the Pico 2 with Rust on rustos (ADR-004, ADR-027).

   The decision carries the four conditions of TS-012 section 10:
   - (a) The requirement deltas of section 8.10, A5 rows only, go to CR-018.
   - (b) **Ordering gate.** Nothing is ordered until the recomputed worst case is at or below USD 300 after guards G1 to G4. Guard G6 (revert to the End-of-Life AFT05) is not available without a new owner decision.
   - (c) The three open thermal items of assumption 3 are PDR design items.
   - (d) Owner questions Q5, Q6 and Q7 and follow-on decisions 1 to 6 are put to the owner separately. This ADR does not decide them.
2. **TS-001 and TS-007 are superseded by TS-012 (for confirmation at S1).**
   - TS-001's receiver and PA concept is replaced by TS-012 section 8.1 and D-15: the ladder is re-admitted, the Inrad #111 and the 24-bit ADC are dropped, the diode ring is used, and the PA is chosen by TS-012.
   - TS-007's synthesizer and reference are replaced by TS-012 section 8.3 and D-17: the Adafruit Si5351A with the TG2520SMN on XA, in place of the TS-007 recommendation of an LMX2571 with an Si5351A for the BFO. TS-012 section 3.2 prunes the LMX2571 as reflow-only.
   - Neither study is re-scored or decided. Its Status row reads "Superseded by TS-012 (ADR-056)" (06 section 14.6).
   - Their remaining analyses continue as value-bearing analyses under plan rule C10: WP-PDR-19 for TS-001 (MDS redesign, `rx-cascade.md`, G1 values) and WP-PDR-20 for TS-007 (route R3 budget, relock time, ratio freshness, clock plan and ADR-031 revision, G2 values).
3. **Five planned studies are not written, because TS-012 and this ADR decide them (for confirmation at S1).** Their provisional numbers, and the provisional ADR numbers ADR-029 to ADR-050 of the PDR work plan, are not taken. Each WP's analyses stay under rule C10.

   | Planned study | What decides it | TS-012 section |
   |---|---|---|
   | TS-003 PA line-up | RA07M1317M-501 module with a GVA-84+ driver, select-on-test drive pad, drive bandpass, output LPF | 8.1, 8.3; D-7, D-13, D-14 |
   | TS-006 ALC, keying envelope and cutoff node | Pack-dependent VGG clamp; keying loop items 1 to 10; PA_EN permit NAND of TX_KEY, PA_EN and the cutoff monostable driving the VGG clamp FET and the GVA-84+ supply P-FET | 8.14 D-9, D-10, D-18 |
   | TS-008 T/R element | Omron G5V-2, non-RF-rated, with an RX-grounding pole; isolation measured on the NanoVNA before first transmission | 8.3; exception EX-14 |
   | TS-009 battery and charger | Charging outside the radio in an XTAR MC1; in-radio charge protection layers removed; pack parts S-8252AAO, 2 x AO3400A, MF-R300, DMP3099L | 8.8 D2, D14; 8.3 |
   | TS-010 audio and display | No display; Morse-code audio menu; audio chain NE5532 and MCP6002 on the 5 V bus with a capped attenuator | 8.8 D1; 8.7; 8.3 |

4. **SWR fold-back is closed on the module's load ruggedness, with no fold-back (for confirmation at S1).** SRR decision 60 left open a choice: fit a directional coupler with SWR fold-back, or rely on device ruggedness. It is closed on ruggedness. The RA07M1317M is specified for a load VSWR of 20:1 at all phases at 9.2 V and 7 W without degradation. That covers REQ-SYS-013 (60 s of 5 W keying at 80 % duty into any load up to SWR 10:1, open and short included; TS-012 section 7.3, "Load ruggedness (REQ-SYS-013)"). A5 fits no directional coupler and no fold-back. The 1N5711 detector on the LPF output serves the ALC loop only.

**Not decided here:**
- TS-004 and TS-011 are re-scored within the A5 envelope by WP-PDR-27.
- TS-005 is written as a remnant by WP-PDR-24.

All three are decided at S2 (OD-10 part 2). The spare module (AB-A, Q7) is decided at the ordering gate.

## 3. Alternatives considered

| Option | Description | Why not chosen (or why chosen) |
|---|---|---|
| A5 (chosen) | Module PA with TCXO, diode ring, spare GVA-84+ (section 2 item 1) | Chosen by the owner, 270 of 500 (54 %, rank 5, M1 conditional). The owner's condition that the design use no outdated components holds: A5's PA is in current production, and 39 of 39 parts were read Active on 2026-09-29. A5 keeps the vendor-guaranteed harmonics, stability and 20:1 ruggedness (C5), the removal of the hand match (C4), and a REQ-SYS-181 backstop about 52 K below the device rating |
| A4 + U3 (recommended by the study) | AFT05MS004NT1 PA with the required TCXO and A5's diode-ring mixer | Not chosen: 300, rank 2. Its PA is End of Life, which fails the owner's condition. Guard G6 (A5 to A4) is therefore closed without a new owner decision |
| A4 | The same with the JFET mixer | Not chosen: 285; same End-of-Life PA |
| A2 | RD01MUS2 plus RD07MUS2B discrete pair, in-radio charger | Not chosen: 305, first on the matrix, not a finalist and not analysed. Its PA pair is new-old stock, "no longer available for export" (TS-012 section 8.13 Q1). By choosing among A4 and A5, the owner confirmed that choice set, so the A2 analysis was not run |
| A3 | Module PA, no hand-wound parts, sink inside the case | Not chosen: 285; fails M1 on estimated lines |
| A1 | Minimum cost as submitted | Not chosen: fails M4 |
| A0 (do nothing) | SRR concept, PCBWay turnkey, about USD 610 per unit | Not viable: fails M1 (the USD 300 maximum) |

The weighted matrix, sensitivity (robustness verdict Not robust), per-alternative risks and dissent are in TS-012 sections 5 to 7 and 9. The SWR fold-back alternative of item 4 (directional coupler and fold-back) is not chosen: the module's rated ruggedness covers REQ-SYS-013 with a margin of two in VSWR, and a coupler adds parts, loss and cost under the ceiling.

## 4. Consequences

### 4.1 Requirements created or changed

The A5 rows of TS-012 section 8.10 are carried by CR-018. Each requirement CR-018 changes cites this ADR in `source_ids` (cross item to the CR-018 author). The main rows:

| Requirement | Relationship | Note |
|---|---|---|
| REQ-SYS-012 (KDR) | value changed via CR-018 | Low-pack delta: 5 W +1/-1.5 dB (TBR) at 6.4 V. Firm delta or bench check with the delta as fallback, decided by the owner (follow-on decision 2) |
| REQ-SYS-112 (KDR), REQ-SYS-118 | changed via CR-018 | Duty-limited corner, and the REQ-SYS-118 inhibit on the flange NTC at about 81 C (D-6; follow-on decision 1) |
| REQ-SYS-137 (KDR) | retired via CR-018 | The owner hand-assembles every part |
| REQ-SYS-140 (KDR) | reworded via CR-018 | Catalog distributor or maker shop with a published price and stock; RF Parts named for the module (EX-3) |
| REQ-TX-014 | restated via CR-018 | With its HZ-004 note, after the D-18 lien fix (follow-on decision 4) |
| REQ-SYS-013 | allocated; implemented by this decision (item 4) | Unchanged value. Cross item: add ADR-056 to its `source_ids` in CR-018 |
| REQ-SYS-182, REQ-SYS-154, REQ-SYS-120, REQ-SYS-181 | allocated; kept as written | Route R3 (D-17); PA permit (D-18); backstop value kept |
| REQ-SYS-022 | kept; at risk | A5 nominal MDS -140.7 dBm; -134.9 dBm at the TC-SYS-017 corner; the WP-PDR-19 redesign follows |
| REQ-SYS-006, 057 to 070, 096, 146, 163 to 165, 171; REQ-SW-KEYER-014, 023, 032 | changed or retired via CR-018 | The Morse-menu UI rows of TS-012 section 8.10 |
| REQ-SYS-081 to 093, 167, 185, 186 | retired, reallocated or reworded via CR-018 | Charging outside the radio |
| REQ-SYS-094, 101, 102, 103, 104, 106, 109, 124, 138, 139, 144, 147, 172, 177, 178; REQ-SYS-083, 084 | changed via CR-018 (109 and 124 with CR-003 revision 4) | Power, mechanical, build and cost rows of section 8.10 |

No requirement is self-derived from this ADR.

### 4.2 Interfaces, design and code

- **ICDs affected:**
  - ICD-TX-ANT: gold-plated brass-class SMA, 100 cycles (TBR);
  - ICD-CTL-USB: firmware only, no charge path;
  - ICD-PWR-CELL: no in-radio charging;
  - ICD-CTL-PHONES: MCP6002 on the 5 V bus with the capped attenuator.
  
  The PDR ICDs ICD-CTL-SW, ICD-RX-TX and ICD-TX-SW are written on A5 by WP-PDR-36, including FC0 on GPIN0 and GPIN1, PA_EN and the relay sequence.
- **Design elements:**
  - `docs/design/architecture.md` is written from TS-012 section 8.1 (WP-PDR-31).
  - The software architecture adds the Morse menu and decoder, the FC0 counter and SW-SAFE frequency check, and PA_EN written only by the safe-state manager (WP-PDR-32).
  - `docs/design/concept.md` gets a note that A5 replaces its concept blocks (WP-PDR-02).
- **New `SW-<SUB>` modules created by this ADR:** none. SW-DISPLAY is removed, and the Morse-menu module is named by WP-PDR-32 and WP-PDR-35.
- **ICDs created by this ADR:** none.

### 4.3 Verification and safety

- **Verification cases to add or change:** the rows CR-018 carries for the section 8.10 deltas; the bench checks of TS-012 section 7.3 and the design items (NanoVNA BPF alignment and relay isolation, select-on-test drive pad at about 17 mW, tinySA harmonic sweep, in-situ sink and NTC-offset measurements, thermocouple surface check). For item 4, the REQ-SYS-013 case uses the module datasheet rating (Analysis) and a bench open and short check.
- **Scope of the item 4 closure.** The module rating covers the module. Two cases are not covered by it:
  - The parts after the module carry the standing wave into 10:1: the output LPF (1206 C0G, 100 V rated in the BOM), the relay contact and the SMA. As an estimate, holding 5 W forward, that is up to about 41 V and 0.81 A peak. Cross item to WP-PDR-21: confirm the part ratings in the LPF record.
  - An ALC open-loop fault puts out at most 8 W at 8.4 V (D-9), above the 7 W rating condition. That is a second fault on top of the mismatch, bounded by REQ-SYS-156 (Fault-safe within 100 ms, TBR) and outside REQ-SYS-013's 5 W keying condition.
- **Evidence classes:** Simulation (LTspice, accredited ACC-LTSPICE-001) for the RF and keying analyses; Bench with the NanoVNA, tinySA Ultra (when bought), multimeter and a thermocouple thermometer (D-16); HostUnit for the Morse menu, FC0 check and safe-state manager.
- **Hazard analysis update required:** yes (WP-PDR-16, 0.6.0-pha):
  - HZ-002 is re-scoped to the COTS charger and the handbook.
  - HZ-003 covers the sink outside the end wall, the wrap-around guard, and the module case against the 90 C guidance.
  - HZ-004 control K8 names PA_EN and the D-18 NAND.
  - HZ-005: every menu tone passes through the capped sidetone path.
  - HZ-007 gains a new heating cause (the sink's inner face and the cell 60 C trip).
  - HZ-008 control K7 runs on route R3.
  - HZ-015 adds the heat gun.
- **Safety-critical software scope (SWE-134 provisions) changed:** yes. SW-SAFE gains the FC0 check with a threshold of 5.0 kHz, and the PA_EN permit is written only by the safe-state manager. The Morse-menu override path stays safety-critical (SRR decision 9). The safety-critical determination is re-run in WP-PDR-17 (OD-35 at S2).

### 4.4 Cost, schedule, risk

- **BOM and cost:** planning USD 248.83. The worst case is USD 316.51, or 299.83 after guards G1 and G2. No money is spent by this decision: the order waits for the ordering gate after CDR, and the BOM and gate figure are WP-PDR-38.
- **Gate affected:** PDR. S1 disposes OD-40 (the A5 CR set) and OD-10 part 1 (items 2 to 4), and S2 disposes OD-10 part 2. The ordering gate follows CDR.
- **Risks** (entries by the WP-PDR-18 writer: `trade_study_ids` TS-012, `adr_ids` ADR-056):
  - RSK-004 (turnkey assembly defects) is retired.
  - RSK-038 (end of life at the order) is re-scored on the lifecycle check.
  - RSK-052 (cost above the model) takes the USD 300 gate.
  - RSK-006 takes the module case against the 90 C guidance.
  - RSK-007 takes the long-session cells at 58.9 C.
  - RSK-026 (hand-hold surfaces) is re-read on the wrap-around guard, which alone meets REQ-SYS-113.
  - RSK-002 and RSK-046 are re-read on the TCXO and route R3.
  - The TS-012 section 7.1 A5 risk scores go to the register.
- **TPMs affected:**
  - TPM-005 (MDS) is Red at the TC-SYS-017 corner.
  - TPM-014 (unit cost) is re-based on the USD 200 target and USD 300 maximum.
  - TPM-001 (mass), TPM-002 (power by mode) and TPM-016 (envelope) are re-rolled by WP-PDR-29.

## 5. Compliance and tailoring

None. Every class 1 choice this ADR records (06 section 14.1 items (a), (b), (c), (d), (f)) was evaluated in the class 1 study TS-012. TS-012 was reviewed with the section B checklist (INSP-110) and its software assurance pair (INSP-118), and went to the owner with its Dissent section (06 sections 14.3 to 14.5). The "not written" dispositions of item 3 open no exception to 06 section 14.1: TS-012 is the study of record for each of those choices, and this ADR is its one ADR (06 section 14.2).

## 6. Decision record (the decision memo for this decision, charter section 4)

**Item 1 (Form 1).** The approval was given in chat between reviews and is transcribed verbatim in `docs/plan/status/status-2026-09-29.md` section 4 (`f35eb78`) and section 5 (`13176ee`). This ADR is the decision memo for it (06 section 14.5; charter section 2).

> Owner (2026-09-29, in chat; status note 2026-09-29 section 4): "This is a good write up. I'm leaning towards A5 if it doesn't use outdated components"

> Owner (2026-09-29, in chat; status note 2026-09-29 section 5, after the A5 parts lifecycle report): "A5"

What was put to the owner:
- **Section 4:** three options (1 choose A4, recommended; 2 choose A5; 3 analyse A2 first), with the revision 6 cost figures.
- **Section 5:** the lifecycle check (`f193784`, 39 of 39 Active; A4's AFT05MS004N End of Life) and A5's trade-offs in plain terms:
  - costs and the ordering gate;
  - about twice A4's heat in the case;
  - the three open thermal items;
  - 4.1 to 6.8 W for a typical unit, and under 3.97 W at 6.4 V for the worst-case unit.

The study went to the owner as revision 6, with its Dissent section and the reviews INSP-110 iteration 3 re-issue 2 and INSP-118 iteration 2. The lead SE's reading of the owner's rationale is in TS-012 section 10: the owner applied parts lifecycle as a screen on top of the matrix, not as a re-scoring. Class 1: the same decision is recorded in TS-012 section 10 (revision 7, `6497900`).

**Items 2 to 4 (proposed memo wording for S1, OD-10 part 1; README rule 4).** "Confirm TS-001 and TS-007 as superseded by TS-012. Confirm that TS-003, TS-006, TS-008, TS-009 and TS-010 are not written, because TS-012 and ADR-056 decide them. Close SWR fold-back (SRR decision 60) on the RA07M1317M's 20:1 load ruggedness, with no fold-back." Owner's disposition: not yet given. It is transcribed here with its date at S1.

## 7. Related

- **Supersedes:** none at filing.
- **Superseded by:** none.
- **Trade study:** TS-012. It supersedes TS-001 and TS-007 (item 2).
- **Review where presented:**
  - Item 1: decided between reviews in chat, 2026-09-29.
  - Items 2 to 4: PDR session S1 (OD-10 part 1).
  - The whole record: PDR.
- **Accepted ADRs that A5 contradicts, for the lead SE's route at S1** (README rule 2 allows only "Superseded by ADR-MMM"; the Status lines change after the S1 disposition, by WP-PDR-02):
  - **Wholly contradicted, proposed "Superseded by ADR-056" on the S1 disposition:**
    - ADR-006: rotary encoders and LCD; replaced by the Morse menu, D1 and D5.
    - ADR-007: PCBWay turnkey; replaced by owner hand assembly (TS-012 section 2, "Prior related decisions").
    - ADR-012: PA stocked at DigiKey, Mouser or a PCBWay distributor; the module is from RF Parts (EX-3).
  - **Superseded by records of their own:**
    - ADR-008 by the enclosure ADR of CR-003 (CR-003 section 5 step 11).
    - ADR-025 by ADR-028 of CR-006.
  - **Contradicted in part only, route open:**
    - ADR-002 item (4), the stainless SMA; A5 uses gold-plated brass (D8).
    - ADR-004, the charge path from VBUS; A5 has no in-radio charging (D2).
    - ADR-005, in-radio charge balancing and the secondary over-voltage protector; removed by D14.
  - **Not contradicted, and they stay:** ADR-013 and ADR-023. TS-012 is the synthesizer trade ADR-013 called for, and the TG2520SMN (+/-0.5 ppm) meets ADR-023.
- **Other records:**
  - TS-007's reviews INSP-055 and INSP-074 end with the study superseded (lead SE disposition).
  - ADR-031 (clock plan) is revised by WP-PDR-20a for D-12.
- **Revisit conditions:** those of TS-012 section 10 (revisions 5, 6 and 7), adopted with this decision. In particular:
  - the worst case is over USD 300 after G1 to G4;
  - an A5 part is found not Active at the gate;
  - RF Parts shows the module out of stock;
  - the thermal items do not close;
  - the owner declines the REQ-SYS-112 delta;
  - REQ-SYS-022 is not shown at the TC-SYS-017 corner;
  - the Si5351A relock or TCXO ratio freshness fails its allocation;
  - the TCXO becomes unavailable.
  
  A trigger is handled by 06 section 14.6: a new TS that cites TS-012, and a superseding ADR.

## 8. Change log

- 2026-09-29: created by the technical data manager, WP-PDR-54 part 1 (`docs/plan/pdr-work-plan.md` revision 6). It records the owner's A5 decision of 2026-09-29 as the decision memo between reviews, and the OD-10 part 1 items for S1 (plan section 3.0a). The number is the next free one, max(existing) + 1 (README rule 1; TS-012 "Resulting ADR" row). Author: Claude (technical data manager invocation).
