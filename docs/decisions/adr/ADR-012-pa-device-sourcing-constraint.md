# ADR-012: Power-amplifier device must be stocked at DigiKey, Mouser or a PCBWay turnkey distributor

| Field | Value |
|---|---|
| ID | ADR-012 |
| Status | Accepted |
| Date proposed | 2026-09-25 |
| Date decided | 2026-09-25 |
| Decision class | 1 (`docs/process/06-risk-and-decision-analysis.md` section 14.1 items (b) RF power device: this ADR fixes a mandatory criterion of its selection; (c) HZ-001, HZ-003, HZ-008). Owner-directed (SI-028). Trade study: TS-001 (Draft) sub-decision P applies the criterion (PD54008L-E recommended); TS-003 at PDR selects the line-up |
| Decision authority | Robin (owner; the decision constrains the PA trade study and procurement) |
| Author | Claude (technical data manager invocation, 2026-09-25) |
| Independent reviewer | INSP-011 (`docs/reviews/SRR/checklists/adrs-001-to-025.md`): iterations 1 and 2 (2026-09-25) NEEDS CHANGES, findings F-01, F-02 and F-03 against this file; the Major-finding corrections are applied here on 2026-09-26 (section 8); verification pending at INSP-011 iteration 3 |
| Life-cycle phase | Pre-A / A |
| Baseline affected | baseline/srr (functional baseline); PDR allocated baseline (PA trade) |
| Change request | none (pre-baseline) |

## 1. Context

The PA study found that the technically best-documented 7.2 V device (Mitsubishi RD07MUS2B with RD01MUS2B driver, measured VHF harmonics, nonlinear model) has no catalog-distributor stock, a 25-piece evaluation-pallet MOQ, a US NOS seller marked "no longer available for export", and would reach PCBWay only as consigned parts, which makes the owner an exporter. The NXP AFT05MS006N has no authorized stock at all; AFT05MS004N is stocked at Newark and Mouser while stock lasts but is end-of-life. The owner ruled: the PA device must be readily sourced from DigiKey, Mouser or PCBWay's turnkey distributors; no bespoke or consignment-only parts (SI-028).

- Driving inputs and expectations: SI-028, SI-009 and SI-031 (turnkey assembly), SI-025 (open-source design others can build), SI-020 (procurement release at CDR)
- Requirements that constrain the decision: none yet (ADR-003 fixes 5 W)
- Hazards in play (`docs/safety/hazards.json` 0.4.0-pha): HZ-003 (thermal path depends on the device package), HZ-001 and HZ-008 (REQ-SYS-012, which cites this ADR, carries both; HZ-008 control K2 names the device TS-001 selects per SI-028 and this ADR)
- Research consulted: `docs/research/pa-device-candidates.md` F2 to F7 (RD series data and sourcing), F8 (RA07M1317M module: consigned, flange mounting order conflicts with turnkey), F9 (AFT05MS006N: no authorized stock), F10 (AFT05MS004N: Newark 1,519 and Mouser 72 in stock, EOL), F11 (AFIC901N: factory order only), F13, F14 (PD54008L-E, GRF5604: stocked, technical fit unproven or poor), F16 (harmonic data quality ranking), F18 (droop), F21 (PCBWay turnkey versus consigned rules; export question), implications 5 to 8 and risks 9 to 13; `docs/research/pcbway-fabrication-and-assembly.md` F17 (turnkey from DigiKey, Mouser, Farnell element14, Arrow, Avnet, or a BOM-linked distributor), F18 (consigned overage rules); `docs/research/2m-cw-transceiver-reference-designs.md` F22 to F24, risk 6
- Guidance consulted: charter section 11 rule 2 (evidence, not assertion: broker stock fails it); 06 section 14.1 class 1 (b) (RF power device is a critical part: trade study); SE HB §6.8
- Assumptions the decision rests on, and how and by when each is confirmed:
  1. At least one stocked device meets 5 W at 144 MHz. Confirmed by TS-001 sub-decision P, then TS-003 at PDR.
  2. Stock persists to the order. Confirmed by a stock check with date and time at CDR.

## 2. Decision

The PA final device and its driver device are mandatory-criterion parts in the PA trade study: at the CDR stock check, each must be in stock at DigiKey, Mouser or a distributor PCBWay buys from turnkey (Farnell element14 or Newark, Arrow, Avnet, or a distributor named by link in the BOM and accepted by PCBWay) in a quantity covering the build plus the owner's reserve, sourced by PCBWay turnkey. Consignment-only parts, factory-order-only parts, evaluation pallets and broker stock are excluded. A device that meets the criterion but is end-of-life (AFT05MS004N class) may be baselined only with a lifetime reserve bought by the owner at PDR and a footprint-compatible alternate identified, and the published design must state the substitution path (SI-025). The harmonic filter and driver design are kept device-agnostic so a substitute can drop in. Stock checks are recorded with date and time in the BOM at PDR and again at CDR.

## 3. Alternatives considered

| Option | Description | Why not chosen (or why chosen) |
|---|---|---|
| A (chosen) | Turnkey-stocked PA and driver as a mandatory criterion | Owner direction (SI-028); no export or consignment logistics; reproducible by others under MIT |
| B | Consign RD07MUS2B and RD01MUS2B bought from Mitsubishi US, Richardson RFPD or RF Parts | Rejected by SI-028; MOQ 25 pallet, "no export" marking, consigned-part overage rules |
| C | RA07M1317M flange module (guaranteed harmonics) | Rejected: consigned and PCBWay would need to confirm the heat-sink-before-solder mounting order |
| D | Broker stock of AFT05MS006N | Rejected: counterfeit risk incompatible with charter rule 11.2 |

The PA device itself is decided by TS-001 (concept-level receiver and PA trade, Draft, sub-decision P) and TS-003 (PA device and line-up) with TS-006 (ALC and envelope topology) at PDR, `docs/design/concept.md` section 11.2 (TS-003 and TS-006 are the proposed numbers of that section, confirmed when each file is created) (class 1 (b)); this ADR fixes one of its mandatory criteria.

## 4. Consequences

### 4.1 Requirements created or changed

| Requirement | Relationship | Note |
|---|---|---|
| REQ-SYS-140 (parts sourcing) | allocated; cites this ADR | The PA device is the driving case; REQ-SYS-178 (owner-procured parts sourcing) covers the owner-bought lines |
| REQ-TX-009, REQ-TX-010, REQ-TX-011 (harmonic attenuation goals, TBR) | allocated; they cite ADR-022 | Device-agnostic filter goals |
| Power-path ratings for the full-charge, full-drive output of the chosen device unless ALC bounds it | not created; REQ-TX-015 (output power ceiling for the RF exposure evaluation, TBR) and REQ-SYS-153 (high pack voltage transmit lockout, TBR) bound the output; RSK-047 carries the rating question to TS-003 and TS-006 | `pa-device-candidates.md` implication 4 |
| REQ-SYS-012 (rated output power with level control, TBR) | allocated; cites this ADR and ADR-003; hazards HZ-001, HZ-003, HZ-008 | Listed because the requirement cites this ADR |

### 4.2 Interfaces, design and code

- ICDs affected: none
- Design elements created or changed: PA line-up footprint designed for a primary device and a footprint-compatible alternate where one exists
- New `SW-<SUB>` modules created by this ADR: none
- ICDs created by this ADR: none

### 4.3 Verification and safety

- Verification cases to add or change: TC-SYS-NNN (BOM stock inspection with timestamps at PDR and CDR, Inspection)
- Evidence class implications: with no vendor harmonic data for most stocked devices, the LTspice behavioural PA model and the tinySA measurement (ADR-021) carry the harmonic evidence
- Hazard analysis update required: yes (HZ-008 control K2); applied in `docs/safety/hazards.json` 0.4.0-pha, whose K2 names the device TS-001 selects from stocked parts per SI-028 and this ADR and records the consignment-only RD07MUS2B as excluded (`reconciliation-srr.md` row V-6)
- Safety-critical software scope changed: no

### 4.4 Cost, schedule, risk

- BOM impact: a lifetime reserve purchase (for example 100 pieces at about USD 4.21 for AFT05MS004N) if an EOL device is baselined
- Gate affected: PDR (trade and reserve purchase), CDR (stock check)
- Risks opened, closed or re-scored: RSK-005 (single-source RF power device or synthesizer unavailable at order time) is re-scored with this constraint as its main mitigation; new risk proposed: "no stocked device has vendor VHF harmonic data" (control: behavioural model plus tinySA); the export-classification risk (implication 12) is retired
- TPMs affected: TPM-004 (PA efficiency), TPM-007 (spurious margin), TPM-014 (unit cost)

## 5. Compliance and tailoring

none

## 6. Decision record

> Owner (2026-09-25, SI-028): "Power amplifier device must be readily sourced from DigiKey, Mouser or PCBWay's turnkey distributors; no bespoke or consignment-only parts."

Transcribed from chat into `stakeholder-inputs.md`.

## 7. Related

- Supersedes: none
- Superseded by: none
- Trade study: TS-001 (Draft, sub-decision P) and TS-003 with TS-006 at PDR (`docs/design/concept.md` section 11.2); this ADR supplies a mandatory criterion
- Review where presented: SRR
- Revisit conditions: no stocked device meets 5 W at 144 MHz from 6.0 to 8.4 V with acceptable harmonics (then the owner is asked to relax SI-028 or ADR-003 by a superseding ADR); a catalog distributor begins stocking the RD series

## 8. Change log

- 2026-09-26: one-time pre-baseline correction under INSP-011 ruling R-1 option (A), as directed by the lead SE: Decision class row and section 1 Assumptions line added (F-01); hazard line and "Hazard analysis update required" re-derived against `docs/safety/hazards.json` 0.4.0-pha (F-02); section 4.1 placeholder ids replaced by the ids the requirement authors allocated, or marked not created with the reason (F-03); trade study references resolved to TS-001 and the proposed TS-003 and TS-006 (F-03, erratum E-9). Content from `reconciliation-srr.md` sections 2, 3, 5.1 and 6, re-checked against the requirement, hazard and expectation files of 2026-09-26; that register is superseded by this file for this ADR. The decision of section 2 is unchanged. Minor findings are liens, fixed before PDR: none against this file. The edit of an Accepted ADR rests on the owner's approval of R-1 (A) in the SRR decision memo and the matching sentence in `docs/process/05-configuration-and-data-management.md` Table 4-1 row 13 (both pending). Class 1 choices without a trade study wait on ruling R-2 (owner). Author: Claude (ADR author invocation).
