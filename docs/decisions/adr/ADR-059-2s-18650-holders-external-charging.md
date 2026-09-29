# ADR-059: Two 18650 Li-ion cells in series in user-replaceable holders, with pack protection on the board and charging outside the radio (supersedes ADR-005)

| Field | Value |
|---|---|
| ID | ADR-059 |
| Status | Proposed. For the owner's confirmation at PDR session S1 (OD-10 part 1, with ADR-056 items 2 to 4). On the S1 disposition it becomes Accepted by a Status-line edit, and ADR-005's Status becomes "Superseded by ADR-059" (README rule 2; WP-PDR-02). It stays Proposed while its independent review runs, because README rule 2 allows no edit of an Accepted ADR and review fixes must be made in place |
| Date proposed | 2026-09-29 |
| Date decided | Pending (S1). The cell format restated unchanged was decided on 2026-09-25 (ADR-005; owner, SI-023). The A5 power tree (pack parts, no in-radio charging) was decided with the owner's A5 decision of 2026-09-29 (ADR-056 section 2 item 1) |
| Decision class | 1 (`docs/process/06-risk-and-decision-analysis.md` section 14.1 items (a) power architecture; (b) battery cell and charger; (c) HZ-002, HZ-007, HZ-011 and the component `SW-PWR` of `docs/process/07-software-engineering-plan.md` section 14.1), as ADR-005. The cell format stays owner-directed (SI-023) and is recorded without a trade study under SEMP customization 11 (`docs/plan/semp.md` section 9.0 and section 5.17), item (i), as ADR-005 recorded it (SRR decision 106). The pack parts and charging outside the radio were chosen in TS-012, a class 1 study, and are recorded by ADR-056, the one ADR of TS-012 (06 section 14.2). The power parts study that ADR-005 deferred them to (TS-009 in the PDR work plan) is not written, because TS-012 and ADR-056 decide it (ADR-056 section 2 item 3, for confirmation at S1). This ADR takes no new decision and is not a second ADR of TS-012: it restates ADR-005 so that ADR-005 can be superseded in full |
| Decision authority | Robin (owner; the decision fixes the power source of the functional baseline, and the A5 power tree changes baseline content through CR-018) |
| Author | Claude (technical data manager invocation, WP-PDR-54 part 1 follow-on, 2026-09-29) |
| Independent reviewer | Pending. The same review as ADR-056 (WP-PDR-54: an independent reviewer with a software assurance pair, since the decision touches `SW-PWR`; the lead SE assigns the record ids and paths). The record must be APPROVED before S1, because OD-10 part 1 rests on it |
| Life-cycle phase | B |
| Baseline affected | baseline/srr (functional baseline) through CR-018, dispositioned at S1 (OD-40); baseline/pdr |
| Change request | none for this record. The requirement changes it restates are carried by CR-018, the re-baseline CR (WP-PDR-53) |

## 1. Context

ADR-005 (Accepted, 2026-09-25) records the owner's choice of two 18650 cells in series in holders, so that cells are user-replaceable (SI-023), and a proposed power tree around them: a 2S boost charger from USB with balancing (BQ25887 class), a 2S protector (S-8252 class) with an independent secondary over-voltage protector (BQ29209 class), a 5 V buck and a 3.3 V analog LDO. The owner's A5 decision of 2026-09-29 (ADR-056 section 2 item 1; `docs/decisions/trade-studies/TS-012-design-to-cost-hand-built.md` section 10) keeps the cell format and changes the power tree:
- the cells are charged outside the radio in an XTAR MC1 (descope D2; exception EX-4);
- the in-radio charge protection layers and balancing are removed, and the S-8252 keeps its over-voltage and under-voltage thresholds in the pack (descope D14);
- an LM2940-5 LDO feeds a 5 V bus, with no 3.3 V analog LDO (descope D13);
- the pack parts are named (TS-012 sections 8.1 and 8.3).

An Accepted ADR is not edited (README rule 2; `docs/process/05-configuration-and-data-management.md` Table 4-1 row 13), and rule 2 has no partial supersession. The lead SE ruled on 2026-09-29 (ruling 2, recorded in ADR-056 section 7) to follow the ADR-026 precedent, where ADR-026 restated ADR-010 and superseded it in full. This ADR therefore restates every unchanged part of ADR-005 verbatim or near-verbatim, states the A5 changes with their sources, and supersedes ADR-005 in full on the S1 disposition.

ADR-005's context, restated with its correction of 2026-09-27 and the A5 figures: a 5 W two-stage VHF PA line-up draws 11.4 W DC during key-down, about 1.6 A at 7.2 V and 1.9 A at 6.0 V (`docs/research/pa-device-candidates.md` F19). The A5 module draws about 0.2 A more than a discrete PA at key-down, and the key-down load is about 2.0 A (TS-012 section 8.10, rows REQ-SYS-094 and REQ-SYS-085). The choice fixes the PA supply window (6.0 to 8.4 V), the protection circuit, the enclosure volume and mass, and the battery-life budget (ADR-020).

- Driving inputs and expectations: SI-023, SI-022 (charge from USB; its charging half given up by A5, descope D2), SI-034 (8 h at 1:9), SI-001 (pocket), SI-019 (units in friends' hands: replaceable cells matter). The owner's USD 300 maximum (status note 2026-09-27 section 10, as TS-012 section 2 quotes it) takes the next free SI id when CR-018 appends the owner inputs of that note.
- Requirements that constrain the decision: at ADR-005, none. Now: REQ-SYS-080 (created from ADR-005) and the L1 power rows of section 4.1.
- Hazards in play (`docs/safety/hazards.json` 0.5.0-pha):
  - HZ-002 (Li-ion charging and thermal event): re-scoped to the COTS charger and the handbook (ADR-056 section 4.3).
  - HZ-007 (discharge-side faults: protector, fuse, reverse insertion, holders; REQ-SYS-084 to REQ-SYS-087, REQ-SYS-166): gains a heating cause from the PA bay inside the case (TS-012 section 8.10, L0 paragraph; ADR-056 section 4.3).
  - HZ-011 (charging paused while receiving, control K2, REQ-SYS-093): K2 loses its object with no in-radio charger.
- Research consulted: as ADR-005: `docs/research/power-tree-and-charging.md` F3, F5 to F7 (charger candidates), F11 (S-8252 plus dual N-FET protection, BQ29209 second OV layer), F13 (Keystone 1043P single-cell THT holder in stock; two give the four terminals a mid-tap needs; dual holders unverified), F23 (battery-life table), section I (safety provisions); `docs/research/pa-device-candidates.md` F18 (2.4 to 3.2 dB output spread across 6.0 to 8.4 V; ALC needed), F19 (11.4 W DC at 5 W). For the A5 changes: TS-012 sections 3.2 (in-radio charging re-check), 8.1, 8.3, 8.5, 8.8 (D2, D13, D14), 8.9 (EX-4), 8.10 and 8.13 (Q2, Q3), with the ABLIC S-8252 Series datasheet Rev.4.0_00 and the AOS AO3400A datasheet Rev 3.1 values as TS-012 records them; `docs/research/pa-device-candidates.md` F8 (RA07M1317M: VDD 7.2 V, VDD maximum 9.2 V operating and 12 V rating).
- Guidance consulted: SWE-134 (charging supervision was safety-critical software, 03 section 4.3); SE HB §6.8; 06 sections 14.1, 14.2 and 14.6; README rules 1 to 6.
- Assumptions the decision rests on, and how and by when each is confirmed:
  1. Two single-cell holders fit the envelope. A5 puts about 21 mm of cells in holders in the body height (TS-012 section 8.5). Confirmed by a printed fit check before CDR (REQ-SYS-103), as ADR-005.
  2. Unprotected 18650 cells with the in-pack protection of section 2 meet the HZ-007 controls, and the external charger with the handbook meets the HZ-002 controls. Confirmed by the WP-PDR-24 pack protection work (the S-8252AAO windows of REQ-SYS-083 to REQ-SYS-085) and the WP-PDR-16 hazard update, before S2.
  3. The fitted cells give the capacity REQ-SYS-094 needs: the P28A is 2.8 Ah (2.6 Ah minimum) against ADR-005's 3000 mAh class (Low confidence, ADR-020). Confirmed by the WP-PDR-29 battery-life budget, with the test cell that CR-018 sets.

## 2. Decision

The power source is two 18650 Li-ion cells in series (2S, 6.0 to 8.4 V, nominal 7.2 V) in two single-cell through-hole holders (Keystone 1043P), so that the pack exposes four terminals for a mid-tap and per-cell sensing. Cells are user-replaceable unprotected cells: **(changed for A5)** the Molicel P28A, 2.8 Ah (2.6 Ah minimum), unprotected flat top, bought with the radio (TS-012 section 8.3), in place of ADR-005's proposed Samsung INR18650-30Q class.

**Protection is on the board, in the pack (changed for A5).** It has these parts (TS-012 sections 8.1 and 8.3):
- an ABLIC S-8252AAO-M6T1U 2S protector (VCU 4.250 V, VDL 2.500 V, VDIOV 0.200 V; datasheet Rev.4.0_00 Table 2) with two AO3400A N-FETs in the pack negative lead;
- a Bourns MF-R300 PTC in the pack lead.

There is no secondary over-voltage protector and no charge balancing in the radio (descope D14); the S-8252AAO over-voltage layer backs up the external charger (REQ-SYS-083 as reworded by CR-018).

**Charging (changed for A5).** The radio has no charger. The cells are taken out and charged one at a time in an XTAR MC1 one-bay USB Li-ion charger (0.5 A), powered by the owner's USB adapter (descope D2; exception EX-4). USB on the radio loads firmware only (ADR-058).

**Rails (changed for A5).** The PA module (RA07M1317M, ADR-056) is fed from the protected pack directly, through two DMP3099L P-FETs for reverse polarity and rail switching, with ALC on its gate bias (ADR-003; TS-012 D-9 and D-10). An LM2940-5 LDO feeds the 5 V bus, and a third DMP3099L switches the transmit 5 V rail. There is no 5 V buck and no 3.3 V analog LDO; the op-amps run on the 5 V bus (TS-012 section 8.1; descope D13). A cell NTC trips at 60 C and clamps the transmitter (TS-012 section 8.1, note 1).

**Power switch.** A mechanical power switch (E-Switch EG1218) drives the gates of the rail P-FETs, which remove power from the loads; the protector stays live (off current about 10 to 20 uA, TS-012 section 8.10). This is the owner's interpretation of REQ-SYS-101 in TS-012 section 8.10, carried by CR-018.

**Part selection.** The parts are those of TS-012 section 8.3, decided with A5 (ADR-056 section 2 item 1). ADR-005 left them to a power trade study at PDR; that study (TS-009) is not written (ADR-056 section 2 item 3).

## 3. Alternatives considered

| Option | Description | Why not chosen (or why chosen) |
|---|---|---|
| A (chosen) | 2S 18650 in two single-cell holders, pack protection on the board, cells charged outside the radio | Owner direction for the cells (SI-023); matches the 7.2 V PA class of the RA07M1317M module (`pa-device-candidates.md` F8); four terminals for per-cell protection; A5 for the power tree (ADR-056) |
| A-005 | ADR-005 as decided: in-radio 2S CC-CV boost charger from USB with balancing, JEITA windows and a safety timer, and a secondary OV protector | Not chosen: TS-012 section 3.2 found the USB-input 2S charger ICs LCSC-only and no leaded USB-to-2S charger IC with a Mouser listing, at an estimated USD 7 to 14 capped in parts plus USD 0 to 23 capped of LCSC shipping, and the Catastrophic HZ-002 charger chain back in the box beside a PA sink that dissipates 8.5 to 10 W; pruned for build 1 (owner question Q3) |
| B | 1S 18650 with a boost converter for the PA | Rejected: 12 W at 3.0 to 4.2 V means 3 to 4 A input, a switching converter next to the receiver, and efficiency loss |
| C | Soldered pouch or hard pack with built-in protection | Rejected by SI-023 (user-replaceable) |
| D | 3S | Rejected: 12.6 V exceeds the module's 12 V VDD rating and its 9.2 V operating maximum (`pa-device-candidates.md` F8) |
| E | One dual 18650 holder | Deferred: terminal count unverified (`power-tree-and-charging.md` F13, Low confidence); two singles guarantee the mid-tap |

No trade study for the cell format (owner direction). The pack parts and the charging choice are TS-012's (ADR-056).

## 4. Consequences

### 4.1 Requirements created or changed

When this ADR is Accepted, each requirement that cites ADR-005 adds ADR-059 to `source_ids` (cross item to the CR-018 author). The A5 rows below are those of TS-012 section 8.10, "Power and charging".

| Requirement | Relationship | Note |
|---|---|---|
| REQ-SYS-080 (two 18650 cells in holders) | allocated; cites ADR-005; unchanged | Cross item: add ADR-059 in CR-018 |
| REQ-SYS-081 (charge termination), REQ-SYS-082 (charge temperature window) | reallocated via CR-018 to the external charger and the handbook | HZ-002. The MC1 termination voltage and tolerance are not on the seller page (TBR; owner reads its product sheet, TS-012 section 8.11 item 6) |
| REQ-SYS-083 (independent cell over-voltage protection) | reworded via CR-018 | S-8252AAO VCU 4.250 V, +/-25 mV from -10 to +60 C: proposed 4.225 to 4.30 V (TBR), the layer backing up the external charger |
| REQ-SYS-084 (cell under-voltage cutoff) | at risk; value proposed via CR-018 | S-8252AAO VDL 2.500 V is +/-0.050 V at 25 C only and -0.085 / +0.060 V over -40 to +85 C; proposed 2.415 to 2.560 V (TBR), or keep and record at risk until the PDR protector-variant selection |
| REQ-SYS-085 (over-current and short-circuit protection) | kept | Trip 2.97 to 7.0 A across two AO3400A; key-down load about 2.0 A |
| REQ-SYS-087 (cell insertion check) | changed via CR-018 | Refuse to arm transmit, in place of refusing charging |
| REQ-SYS-088, 089, 091, 093, 167, 185 | retired via CR-018 | No in-radio charging (REQ-SYS-185 is the further over-voltage layer that ADR-005's secondary protector served) |
| REQ-SYS-186 (separate cell-sense paths per layer) | reworded via CR-018 | For the one remaining in-pack layer plus the firmware monitor |
| REQ-SYS-070 (charge state indication) | retired via CR-018 | The MC1 indicates |
| REQ-SYS-094 (battery life at 1:9) | changed via CR-018 | Test with the fitted 2.8 Ah P28A cells, or keep 3.0 Ah as the test cell; estimate 8 to 14 h; WP-PDR-29 budgets it (ADR-020) |
| REQ-SYS-100 (current drawn when switched off) | kept | Off current about 10 to 20 uA against 50 uA |
| REQ-SYS-101 (mechanical power switch) | changed via CR-018 | The EG1218 (0.2 A) drives the rail P-FET gates that remove power (owner interpretation) |
| REQ-SYS-012 (5 W, TBR), REQ-SYS-097 (low-battery transmit inhibit, TBR), REQ-SYS-098 (low-battery power-down, TBR) | allocated; none cites ADR-005 | REQ-SYS-012 changes via CR-018 to 5 W +1/-1.5 dB at the 6.4 V end (TBR; ADR-056). REQ-SYS-097 and 098 are not in TS-012 section 8.10 and stay |
| REQ-SYS-086 (reverse cell insertion), REQ-SYS-099 (cell over-temperature lockout), REQ-SYS-166 (rails held off for out-of-window cells) | allocated; none cites ADR-005; not in TS-012 section 8.10 | HZ-007. REQ-SYS-099 asks for the loads to be powered down at 60 C; the A5 diagram shows the cell 60 C trip on the transmitter clamp node. Cross item to WP-PDR-24: state how REQ-SYS-099 is met |
| REQ-PWR L2 (protection thresholds, insertion check; candidates PWR-PROT-*) | not created at L2: the PWR file is written by WP-PDR-34 | ADR-005's charge-profile and balancing candidates (PWR-CHG-01, PWR-CHG-02) lapse with in-radio charging |

### 4.2 Interfaces, design and code

- ICDs affected: `ICD-PWR-CELL` (cell format, polarity, holder terminals, mid-tap; 1043P holders and the external charger via CR-018; ADR-056 section 4.2: "no in-radio charging").
- Design elements created or changed:
  - The power tree of TS-012 section 8.1: S-8252AAO with two AO3400A in the pack negative lead, MF-R300, two DMP3099L as the reverse-polarity and rail switch with the EG1218 driving their gates, the module drain from the pack, LM2940-5 to the 5 V bus, a third DMP3099L for the transmit 5 V, and the supply filters F1 and F3 of D-12.
  - The holders sit on the bottom of the main board at the antenna end, away from the heat sink (TS-012 section 8.1, Boards).
  - The enclosure cavity takes two holders of 77 x 20.65 x 14.86 mm (about 41 x 77 mm footprint), as ADR-005.
- New `SW-<SUB>` modules created by this ADR: none. `SW-PWR` loses its charging functions (section 4.3).
- ICDs created by this ADR: none.

### 4.3 Verification and safety

- Verification cases to add or change: TC-SYS-058 (Inspection, REQ-SYS-080) is unchanged; TC-SYS-067 (Bench, REQ-SYS-094; ADR-020) runs with the test cell CR-018 sets. The PWR L2 cases (protector trip points; the insertion check) are allocated with the PWR L2 requirements at PDR (no id yet). ADR-005's charge-profile and balancing cases lapse.
- Evidence class implications: Bench (bench supply, multimeter) suffices, as ADR-005.
- Hazard analysis update required: yes (WP-PDR-16, 0.6.0-pha).
  - HZ-002 is re-scoped to the COTS charger and the handbook (ADR-056 section 4.3). Controls K1 (charger IC), K3 (secondary 2S over-voltage protector), K4 (dual dissimilar sensing), K5 (insertion check for charging), K6 (charge pause) and K9 (a sense path per layer) name in-radio charging parts or functions that A5 does not fit. K2, the S-8252-class protector, stays as the in-pack layer. K8, the handbook, takes the charging instructions.
  - HZ-007: K1 is the S-8252AAO with its datasheet values, K2 the MF-R300, and K6 the EG1218 driving the rail P-FET gates. HZ-007 gains the heating cause of ADR-056 section 4.3 (the sink's inner face and the cell 60 C trip).
  - HZ-011: K2 loses its object (REQ-SYS-093 retired).
- Safety-critical software scope (SWE-134 provisions) changed: yes. `SW-PWR` (07 section 14.1) loses its charging supervision: charger status, the dual-path charge check, the temperature window, charge disable and the charge-state watchdog. Its discharge side stays: rail enable on the cell-voltage window, the transmit-inhibit and power-down thresholds, the cell over-temperature lockout, and the gauge and low-battery warning. The determination is re-run in WP-PDR-17 (ADR-056 section 4.3).

### 4.4 Cost, schedule, risk

- BOM impact (TS-012 section 8.3):
  - Mouser, aggregator reads of 2026-09-27: two 1043P holders USD 5.90; S-8252AAO USD 1.66; two AO3400A USD 1.04; MF-R300 USD 0.50; three DMP3099L USD 1.20; LM2940CT-5.0 USD 2.04.
  - 18650BatteryStore, listed sale prices: two P28A cells USD 11.98 and the XTAR MC1 USD 4.99, inside the radio's cap (TS-012 section 8.4).
  - No charger IC, balancer or secondary protector.
- Gate affected: PDR (S1 disposition; the WP-PDR-24 pack protection work: the S-8252AAO windows of REQ-SYS-083 to 085, the drain-feed budget of at most 0.35 ohm, the MF-R300 and the LM2940 rails).
- Risks opened, closed or re-scored: RSK-007 (Li-ion cell thermal event inside the enclosure) stays open. With A5 the long-session cells reach 58.9 C against the 55 C criterion, an open thermal item of WP-PDR-28a (TS-012 section 10 condition 3; ADR-056 section 4.4). The charger-side mitigations of ADR-005 (JEITA windows, the secondary OV layer) leave the radio with the charger.
- TPMs affected: TPM-001 (mass: cells 92 to 96 g, holders 12 to 16 g; TS-012 section 8.5), TPM-002 (power margin), TPM-008 (battery life; REQ-SYS-094 estimate 8 to 14 h, WP-PDR-29).

## 5. Compliance and tailoring

none

## 6. Decision record

The cell format is the owner's, on record before this ADR:

> Owner (2026-09-25, SI-023): "Battery: two 18650 Li-ion cells (2S) in a holder so cells are user-replaceable."

Transcribed from chat into `stakeholder-inputs.md` (ADR-005 section 6). The A5 power tree comes from the owner's A5 decision, recorded in ADR-056 section 6 (Form 1) and TS-012 section 10:

> Owner (2026-09-29, in chat; status note 2026-09-29 section 5, after the A5 parts lifecycle report): "A5"

The owner's statement that no cells or charger are owned, which led the study to price the P28A cells and the MC1 (TS-012 section 8.13 Q2):

> Owner (2026-09-27, status note 2026-09-27 section 11): "I don't have any 18650s or chargers."

**Proposed memo wording for S1 (OD-10 part 1; README rule 4).** "Confirm ADR-059. It restates ADR-005 with the A5 power tree: two P28A cells in 1043P holders with S-8252AAO pack protection, no charger, balancing or secondary over-voltage protector in the radio, and the cells charged outside the radio in an XTAR MC1. ADR-059 is Accepted and ADR-005 becomes Superseded by ADR-059." Owner's disposition: not yet given. It is transcribed here with its date at S1.

## 7. Related

- Supersedes: ADR-005, in full, on the S1 disposition (ADR-005's Status then reads "Superseded by ADR-059", set by WP-PDR-02). Until then ADR-005 stays Accepted and in force.
- Superseded by: none.
- Trade study: none for the cell format (Decision class row); TS-012 for the pack parts and the charging choice (ADR-056); TS-009 not written (ADR-056 section 2 item 3).
- Review where presented: PDR session S1 (OD-10 part 1). ADR-005 was presented at SRR.
- Related records: ADR-056, ADR-058, ADR-003, ADR-020; CR-018.
- Revisit conditions:
  - The enclosure cannot hold two holders side by side at the chosen size (then a dual holder with verified terminals, same ADR intent), as ADR-005.
  - The PA changes to a device outside the 6 to 8.4 V class (a TS-012 revisit, then a superseding ADR).
  - A pack part of section 2 is found not Active at the ordering gate (TS-012 section 10 revisit condition (b)).
  - The long-session cell temperature does not close with a no-cost or gate-affordable change (TS-012 section 10 revisit condition (d)).
  - In-radio charging is wanted in a later build (TS-012 Q3: "Revisit for a later build"): a superseding ADR, after a new trade study.

## 8. Change log

- 2026-09-29: created by the technical data manager (WP-PDR-54 part 1 follow-on), on lead SE ruling 2 of 2026-09-29 (ADR-056 section 7): ADR-005 is contradicted only in part, README rule 2 has no partial supersession, so this ADR restates ADR-005 in full with the A5 changes and supersedes it on the S1 disposition, as ADR-026 did for ADR-010. The number is the next free one after ADR-058 (README rule 1). ADR-005's section 8 readings are carried: the key-down current of section 1 is the corrected F19 figure, the hazard stamp is 0.5.0-pha, and the verification cases are those of its WP-PDR-14 reading. Author: Claude (technical data manager invocation).
