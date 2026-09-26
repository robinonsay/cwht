# ADR-012: Power-amplifier device must be stocked at DigiKey, Mouser or a PCBWay turnkey distributor

| Field | Value |
|---|---|
| ID | ADR-012 |
| Status | Accepted |
| Date proposed | 2026-09-25 |
| Date decided | 2026-09-25 |
| Decision authority | Robin (owner; the decision constrains the PA trade study and procurement) |
| Author | Claude (technical data manager invocation, 2026-09-25) |
| Independent reviewer | Pending: reviewer agent invocation before SRR (01 section 3.2 row S3; 06 section 14.2) |
| Life-cycle phase | Pre-A / A |
| Baseline affected | baseline/srr (functional baseline); PDR allocated baseline (PA trade) |
| Change request | none (pre-baseline) |

## 1. Context

The PA study found that the technically best-documented 7.2 V device (Mitsubishi RD07MUS2B with RD01MUS2B driver, measured VHF harmonics, nonlinear model) has no catalog-distributor stock, a 25-piece evaluation-pallet MOQ, a US NOS seller marked "no longer available for export", and would reach PCBWay only as consigned parts, which makes the owner an exporter. The NXP AFT05MS006N has no authorized stock at all; AFT05MS004N is stocked at Newark and Mouser while stock lasts but is end-of-life. The owner ruled: the PA device must be readily sourced from DigiKey, Mouser or PCBWay's turnkey distributors; no bespoke or consignment-only parts (SI-028).

- Driving inputs and expectations: SI-028, SI-009 and SI-031 (turnkey assembly), SI-025 (open-source design others can build), SI-020 (procurement release at CDR)
- Requirements that constrain the decision: none yet (ADR-003 fixes 5 W)
- Hazards in play: HZ-003 (thermal path depends on the device package)
- Research consulted: `docs/research/pa-device-candidates.md` F2 to F7 (RD series data and sourcing), F8 (RA07M1317M module: consigned, flange mounting order conflicts with turnkey), F9 (AFT05MS006N: no authorized stock), F10 (AFT05MS004N: Newark 1,519 and Mouser 72 in stock, EOL), F11 (AFIC901N: factory order only), F13, F14 (PD54008L-E, GRF5604: stocked, technical fit unproven or poor), F16 (harmonic data quality ranking), F18 (droop), F21 (PCBWay turnkey versus consigned rules; export question), implications 5 to 8 and risks 9 to 13; `docs/research/pcbway-fabrication-and-assembly.md` F17 (turnkey from DigiKey, Mouser, Farnell element14, Arrow, Avnet, or a BOM-linked distributor), F18 (consigned overage rules); `docs/research/2m-cw-transceiver-reference-designs.md` F22 to F24, risk 6
- Guidance consulted: charter section 11 rule 2 (evidence, not assertion: broker stock fails it); 06 section 14.1 class 1 (b) (RF power device is a critical part: trade study); SE HB §6.8

## 2. Decision

The PA final device and its driver device are mandatory-criterion parts in the PA trade study: at the CDR stock check, each must be in stock at DigiKey, Mouser or a distributor PCBWay buys from turnkey (Farnell element14 or Newark, Arrow, Avnet, or a distributor named by link in the BOM and accepted by PCBWay) in a quantity covering the build plus the owner's reserve, sourced by PCBWay turnkey. Consignment-only parts, factory-order-only parts, evaluation pallets and broker stock are excluded. A device that meets the criterion but is end-of-life (AFT05MS004N class) may be baselined only with a lifetime reserve bought by the owner at PDR and a footprint-compatible alternate identified, and the published design must state the substitution path (SI-025). The harmonic filter and driver design are kept device-agnostic so a substitute can drop in. Stock checks are recorded with date and time in the BOM at PDR and again at CDR.

## 3. Alternatives considered

| Option | Description | Why not chosen (or why chosen) |
|---|---|---|
| A (chosen) | Turnkey-stocked PA and driver as a mandatory criterion | Owner direction (SI-028); no export or consignment logistics; reproducible by others under MIT |
| B | Consign RD07MUS2B and RD01MUS2B bought from Mitsubishi US, Richardson RFPD or RF Parts | Rejected by SI-028; MOQ 25 pallet, "no export" marking, consigned-part overage rules |
| C | RA07M1317M flange module (guaranteed harmonics) | Rejected: consigned and PCBWay would need to confirm the heat-sink-before-solder mounting order |
| D | Broker stock of AFT05MS006N | Rejected: counterfeit risk incompatible with charter rule 11.2 |

The PA device itself is decided by the PA trade study at PDR (class 1 (b)); this ADR fixes one of its mandatory criteria.

## 4. Consequences

### 4.1 Requirements created or changed

| Requirement | Relationship | Note |
|---|---|---|
| REQ-SYS-NNN (sourcing constraint: every BOM line is available turnkey from PCBWay's distributors or DigiKey; L1 author allocates) | new, constraint traced to SI-028 and SI-009 | The PA device is the driving case |
| REQ-TX-NNN (harmonic filter goals at the filter terminals independent of the PA device; ADR-022) | new at PDR | Device-agnostic filter |
| REQ-TX-NNN (power-path ratings for the full-charge, full-drive output of the chosen device unless ALC bounds it) | new at PDR | `pa-device-candidates.md` implication 4 |

### 4.2 Interfaces, design and code

- ICDs affected: none
- Design elements created or changed: PA line-up footprint designed for a primary device and a footprint-compatible alternate where one exists
- New `SW-<SUB>` modules created by this ADR: none
- ICDs created by this ADR: none

### 4.3 Verification and safety

- Verification cases to add or change: TC-SYS-NNN (BOM stock inspection with timestamps at PDR and CDR, Inspection)
- Evidence class implications: with no vendor harmonic data for most stocked devices, the LTspice behavioural PA model and the tinySA measurement (ADR-021) carry the harmonic evidence
- Hazard analysis update required: no
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
- Trade study: PA device and topology TS at PDR (this ADR supplies a mandatory criterion)
- Review where presented: SRR
- Revisit conditions: no stocked device meets 5 W at 144 MHz from 6.0 to 8.4 V with acceptable harmonics (then the owner is asked to relax SI-028 or ADR-003 by a superseding ADR); a catalog distributor begins stocking the RD series
