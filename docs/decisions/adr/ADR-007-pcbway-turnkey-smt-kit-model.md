# ADR-007: PCBWay turnkey surface-mount assembly with owner-soldered through-hole parts (kit model)

| Field | Value |
|---|---|
| ID | ADR-007 |
| Status | Accepted |
| Date proposed | 2026-09-25 |
| Date decided | 2026-09-25 |
| Decision authority | Robin (owner; the decision spends money at CDR and sets the assembly baseline) |
| Author | Claude (technical data manager invocation, 2026-09-25) |
| Independent reviewer | Pending: reviewer agent invocation before SRR (01 section 3.2 row S3; 06 section 14.2) |
| Life-cycle phase | Pre-A / A |
| Baseline affected | baseline/srr (functional baseline); product baseline at CDR states the part categories |
| Change request | none (pre-baseline) |

## 1. Context

The owner first asked for a fully assembled PCB from PCBWay turnkey with no hand soldering (SI-009), then accepted a kit model: PCBWay assembles all surface-mount parts and the owner hand-solders through-hole components and simple pads, but no BGA, QFN or other hidden-pad package (SI-031). The amendment removes the uncertainty about PCBWay reflowing a castellated module, removes consignment logistics for parts PCBWay does not stock, and lets the owner fit mechanical parts (holders, jacks, encoders) against the enclosure at assembly time.

- Driving inputs and expectations: SI-009, SI-031, SI-011 (owner does no PCB layout), SI-028 (turnkey-stocked PA device), SI-020 (procurement release at CDR)
- Requirements that constrain the decision: none yet
- Hazards in play: none directly; owner-soldered joints in the PA path or battery path are inspected before power-on (V&V plan stage 0)
- Research consulted: `docs/research/pcbway-fabrication-and-assembly.md` F15 (assembly capabilities: 0201, 0.25 mm pitch, QFN, BGA, THT by hand or machine, IPC-A-610 Class 2), F16 (Pico 2 castellated module: recommended footprint, paste 163 percent, no published PCBWay policy), F17 (turnkey from authorized distributors: DigiKey, Mouser, Farnell element14, Arrow, Avnet, or a BOM-linked supplier), F18 (consigned-parts overage rules), F20 (fabrication minimum 5; assembly from 1 with setup fee), F21 (lead times), F22 (cost signals); `docs/research/pcbway-export-and-vendor-questions.md` Part 1 (kicad-cli 10.0.6 export recipe verified), Part 2 (PA thermal DFM, Type VII via fill), Part 3 (vendor confirmation email); `docs/research/display-and-ui-parts.md` F17, F18, D-UI-06 (SJ1-3535N THT jack versus Switchcraft SMT alternative)
- Guidance consulted: NPR 7123.1D SE-24 to SE-31 marked NA (no contracts; catalog services, charter section 12); SE HB §6.8

## 2. Decision

PCBWay fabricates the 4-layer board (proposed 1.0 mm thickness pending the enclosure boss layout, Type VII via fill under the PA and QFN pads) and performs turnkey surface-mount assembly with parts bought from its authorized distributors or from a distributor named by link in the BOM; no substitutes without owner approval. The owner hand-solders the through-hole parts and modules with exposed pads: the Pico 2 module castellations, the two 18650 holders, the two 3.5 mm jacks, the two encoders, the two buttons, and any through-hole relay or connector. No part with hidden pads (QFN, BGA, DFN with a thermal pad only) is assigned to the owner. The product baseline at CDR lists every BOM line in one of the two categories (PCBWay SMT, owner THT), and the assembly package to PCBWay marks the owner lines DNP. Receipt inspection and the owner's soldering are followed by the staged power-on of the V&V plan.

## 3. Alternatives considered

| Option | Description | Why not chosen (or why chosen) |
|---|---|---|
| A (chosen) | PCBWay turnkey SMT; owner solders THT and exposed-pad modules | Owner acceptance (SI-031); avoids the unconfirmed module-reflow path (F16); no consigned parts; owner fits mechanical parts to the enclosure |
| B | Full turnkey including THT and the Pico 2 module | Viable (PCBWay does THT, F15) and remains the fallback if the owner later declines soldering; not chosen because module placement is unconfirmed and THT mechanical parts are better fitted against the enclosure |
| C | Fully owner-built kit from consigned parts | Rejected: 0402 passives, QFN charger and headphone amplifier, RF layout parts; contrary to SI-009 and SI-011 |
| D | Another assembler | Not considered: the owner named PCBWay (SI-009) and the fabrication and CNC orders go to one vendor |

No trade study: the owner's acceptance eliminated the alternatives; the sourcing mode is recorded as D-PCB-03 resolved in favour of "turnkey SMT plus owner THT".

## 4. Consequences

### 4.1 Requirements created or changed

| Requirement | Relationship | Note |
|---|---|---|
| REQ-SYS-NNN (assembly constraint: surface-mount parts are placed by PCBWay turnkey; through-hole parts are owner-installed; L1 author allocates) | new, constraint traced to SI-009 and SI-031 | |
| REQ-ME-NNN or REQ-SYS-NNN (fabrication data package: Gerbers with KiCad names, drill, IPC-2581 or ODB++ optional, stackup, impedance note; assembly package: BOM with distributor links, CPL, DNP list) | new at CDR | From `pcbway-fabrication-and-assembly.md` requirements candidates and the CDR checklist |
| REQ-SYS-NNN (no owner-soldered hidden-pad package) | new, constraint traced to SI-031 | Inspection of the BOM categories |

### 4.2 Interfaces, design and code

- ICDs affected: none
- Design elements created or changed: BOM category field; footprints for owner-soldered parts chosen for hand soldering (Pico 2 `HandSolder` style footprint, THT jacks and encoders); panel or single board with 3.5 mm copper-free edges (D-PCB-04, PDR)
- New `SW-<SUB>` modules created by this ADR: none
- ICDs created by this ADR: none

### 4.3 Verification and safety

- Verification cases to add or change: TC-SYS-NNN receipt inspection (visual against renders and BOM, polarity, dimensions); TC-SYS-NNN owner-solder inspection before power-on (continuity of the PA and battery paths, no bridges); ATP includes both
- Evidence class implications: Inspection (loupe, multimeter) at receipt; the owner is the assembler for the THT lines, so the assembly of those lines is not vendor evidence
- Hazard analysis update required: no; the hazard analysis may add "cold joint in the battery or PA path" as a cause under HZ-002 and HZ-003 with the inspection as control
- Safety-critical software scope changed: no

### 4.4 Cost, schedule, risk

- BOM, fabrication, enclosure or lead-time impact: assembly quote covers SMT only; THT parts ordered from DigiKey by the owner; PCBWay factory closures 2026-10-01 to 10-04 affect lead time
- Gate affected: CDR (procurement release), TRR (assembled unit)
- Risks opened, closed or re-scored: RSK-004 (turnkey assembly defects on RF and fine-pitch parts) stays open; new risk proposed: "owner-soldered joint defect in a power path", mitigated by the pre-power-on inspection
- TPMs affected: TPM-014 (unit cost)

## 5. Compliance and tailoring

Charter section 12 tailoring register row "Assembly model (SI-031): Customized". No RMM row; NPR 7123.1D SE-24 to SE-31 remain NA. Recorded in the SEMP as customization; no CR (pre-baseline).

## 6. Decision record

> Owner (2026-09-25, SI-009): "Fully assembled PCB from PCBWay turnkey (no hand soldering); parts from DigiKey or equivalent."

> Owner (2026-09-25, SI-031): "Kit assembly model accepted: PCBWay assembles all surface-mount parts; the owner is willing to hand-solder through-hole components and simple pads (no BGA/QFN or other hidden-pad packages)."

SI-031 amends SI-009; both transcribed from chat into `stakeholder-inputs.md`.

## 7. Related

- Supersedes: none (SI-009 was never an ADR)
- Superseded by: none
- Trade study: none
- Review where presented: SRR; part categories confirmed at CDR
- Revisit conditions: PCBWay confirms in writing that it reflows the Pico 2 module and solders the THT lines within the quote (then option B by a superseding ADR if the owner prefers); the owner withdraws the soldering offer
