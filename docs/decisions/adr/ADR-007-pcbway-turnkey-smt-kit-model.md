# ADR-007: PCBWay turnkey surface-mount assembly with owner-soldered through-hole parts (kit model)

| Field | Value |
|---|---|
| ID | ADR-007 |
| Status | Accepted |
| Date proposed | 2026-09-25 |
| Date decided | 2026-09-25 |
| Decision class | 1 (`docs/process/06-risk-and-decision-analysis.md` section 14.1 item (c): HZ-015 names this ADR, control K3; HZ-007 cause C8). Owner-directed (SI-009, SI-031). Trade study: board details in TS-004 at PDR (proposed number, `docs/design/concept.md` section 11.2). No trade study for the assembly model: this ADR alone records it under SEMP customization 11 (`docs/plan/semp.md` section 9.0 and section 5.17), which customizes 06 section 14.1, item (i) (ruling R-2 of `reconciliation-srr.md` section 7, adopted by the owner as SRR decision 106 on 2026-09-26) |
| Decision authority | Robin (owner; the decision spends money at CDR and sets the assembly baseline) |
| Author | Claude (technical data manager invocation, 2026-09-25) |
| Independent reviewer | INSP-011 (`docs/reviews/SRR/checklists/adrs-001-to-025.md`): iterations 1 and 2 (2026-09-25) NEEDS CHANGES, findings F-01, F-02 and F-03 against this file; the Major-finding corrections are applied here on 2026-09-26 (section 8); verification pending at INSP-011 iteration 3 |
| Life-cycle phase | Pre-A / A |
| Baseline affected | baseline/srr (functional baseline); product baseline at CDR states the part categories |
| Change request | none (pre-baseline) |

## 1. Context

The owner first asked for a fully assembled PCB from PCBWay turnkey with no hand soldering (SI-009), then accepted a kit model: PCBWay assembles all surface-mount parts and the owner hand-solders through-hole components and simple pads, but no BGA, QFN or other hidden-pad package (SI-031). The amendment removes the uncertainty about PCBWay reflowing a castellated module, removes consignment logistics for parts PCBWay does not stock, and lets the owner fit mechanical parts (holders, jacks, encoders) against the enclosure at assembly time.

- Driving inputs and expectations: SI-009, SI-031, SI-011 (owner does no PCB layout), SI-028 (turnkey-stocked PA device), SI-020 (procurement release at CDR)
- Requirements that constrain the decision: none yet
- Hazards in play (`docs/safety/hazards.json` 0.4.0-pha): HZ-015 (owner hand assembly; REQ-SYS-137 and REQ-SYS-138 cite this ADR and carry it; control K3 is this ADR's part split, control K5 the TRR safety line) and HZ-007 (cause C8, soldering or rework with cells in the holders). Owner-soldered joints in the PA path or battery path are inspected before power-on (V&V plan stage 0)
- Research consulted: `docs/research/pcbway-fabrication-and-assembly.md` F15 (assembly capabilities: 0201, 0.25 mm pitch, QFN, BGA, THT by hand or machine, IPC-A-610 Class 2), F16 (Pico 2 castellated module: recommended footprint, paste 163 percent, no published PCBWay policy), F17 (turnkey from authorized distributors: DigiKey, Mouser, Farnell element14, Arrow, Avnet, or a BOM-linked supplier), F18 (consigned-parts overage rules), F20 (fabrication minimum 5; assembly from 1 with setup fee), F21 (lead times), F22 (cost signals); `docs/research/pcbway-export-and-vendor-questions.md` Part 1 (kicad-cli 10.0.6 export recipe verified), Part 2 (PA thermal DFM, Type VII via fill), Part 3 (vendor confirmation email); `docs/research/display-and-ui-parts.md` F17, F18, D-UI-06 (SJ1-3535N THT jack versus Switchcraft SMT alternative)
- Guidance consulted: NPR 7123.1D SE-24 to SE-31 marked NA (no contracts; catalog services, charter section 12); SE HB §6.8
- Assumptions the decision rests on, and how and by when each is confirmed:
  1. PCBWay turnkey stocks every surface-mount line (REQ-SYS-140). Confirmed by stock checks with date and time at PDR and CDR.
  2. The owner hand-assembles under the HZ-015 procedure. Confirmed by the TRR safety line (HZ-015 K5).
  3. PCBWay accepts DNP lines for owner-soldered parts. Confirmed by the vendor before CDR (`docs/research/pcbway-export-and-vendor-questions.md` Part 3).

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
| REQ-SYS-137 (turnkey surface-mount assembly) | allocated; cites this ADR; hazard HZ-015 |  |
| REQ-SYS-139 (circuit board fabrication rules, TBR) | allocated at L1; does not cite this ADR | The fabrication and assembly data package (Gerbers with KiCad names, drill, stackup, impedance note; BOM with distributor links, CPL, DNP list) is CDR content; no REQ-ME requirement is created for it yet |
| REQ-SYS-138 (owner hand-soldered parts) | allocated; cites this ADR; hazard HZ-015 | Inspection of the BOM categories |

### 4.2 Interfaces, design and code

- ICDs affected: none
- Design elements created or changed: BOM category field; footprints for owner-soldered parts chosen for hand soldering (Pico 2 `HandSolder` style footprint, THT jacks and encoders); panel or single board with 3.5 mm copper-free edges (D-PCB-04, PDR)
- New `SW-<SUB>` modules created by this ADR: none
- ICDs created by this ADR: none

### 4.3 Verification and safety

- Verification cases to add or change: TC-SYS-NNN receipt inspection (visual against renders and BOM, polarity, dimensions); TC-SYS-NNN owner-solder inspection before power-on (continuity of the PA and battery paths, no bridges); ATP includes both
- Evidence class implications: Inspection (loupe, multimeter) at receipt; the owner is the assembler for the THT lines, so the assembly of those lines is not vendor evidence
- Hazard analysis update required: yes (HZ-015 control K3 and HZ-007 cause C8); the hazard analysis may also add "cold joint in the battery or PA path" as a cause under HZ-002 and HZ-003 with the inspection as control
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

## 8. Change log

- 2026-09-26: one-time pre-baseline correction under INSP-011 ruling R-1 option (A), as directed by the lead SE: Decision class row and section 1 Assumptions line added (F-01); hazard line and "Hazard analysis update required" re-derived against `docs/safety/hazards.json` 0.4.0-pha (F-02); section 4.1 placeholder ids replaced by the ids the requirement authors allocated, or marked not created with the reason (F-03). Content from `reconciliation-srr.md` sections 2, 3, 5.1 and 6, re-checked against the requirement, hazard and expectation files of 2026-09-26; that register is superseded by this file for this ADR. The decision of section 2 is unchanged. Minor findings are liens, fixed before PDR: none against this file. The edit of an Accepted ADR rests on the owner's approval of R-1 (A) in the SRR decision memo and the matching sentence in `docs/process/05-configuration-and-data-management.md` Table 4-1 row 13 (both pending). Class 1 choices without a trade study wait on ruling R-2 (owner). Author: Claude (ADR author invocation).
- 2026-09-26 (after the SRR rulings): Decision class row updated under SRR decision 106 (owner ruling 2026-09-26), which adopts ruling R-2 of `reconciliation-srr.md` section 7 as SEMP customization 11 of 06 section 14.1 (`docs/plan/semp.md` section 9.0): the class 1 owner-directed choice of this ADR is recorded by this ADR alone under item (i); the implementing design choices stay class 1 and go through the trade study the row names. The correction entry above now rests on SRR decision 105 (owner ruling 2026-09-26, R-1 option (A) approved) and on the 05 Table 4-1 row 13 sentence, which is in place. The decision of section 2 is unchanged. Author: Claude (ADR author invocation, SRR post-ruling work R16).
- 2026-09-27 (PDR errata, WP-PDR-14; SRR liens L-6 and, where named, L-4 and L-7): Independent reviewer row names the INSP-011 results through the post-SRR-ruling delta 2 and points to the record for later results, replacing "verification pending at INSP-011 iteration 3" (F-13); hazard line stamp 0.4.0-pha changed to 0.5.0-pha, the version at HEAD, after re-checking the line against it (F-13; for ADR-015, 022, 023 and 026 also SRR lien L-7); section 4.3 placeholders replaced by TC-SYS-091, the receipt and owner-solder inspections stated as allocated in the V&V plan (F-14). Route: the SRR decision memo carries these findings as liens to be fixed in the product before the PDR readiness declaration (RFA-SRR-006: "Fix each finding in its product"); they are applied by the ADR correction route the owner approved as SRR decision 105 (corrections outside section 2, each logged in this section), as the README paragraph "PDR errata" records. The decision of section 2 is unchanged. Author: Claude (ADR author invocation, WP-PDR-14).
- 2026-09-27 (correction of the WP-PDR-14 entry above; INSP-053 finding-1, `docs/reviews/PDR/checklists/adrs-001-to-027.md`): the entry above records edits in place of 3 lines outside section 8 made after the `baseline/srr` tag, which 05 Table 4-1 row 13, the Record class of 05 section 4.2 and README rule 2 do not allow. Its "Route" sentence is withdrawn: the SRR lien direction (RFA-SRR-006) does not amend row 13, and the decision 105 route was the exception before the tag only. Those 3 lines are restored to their `baseline/srr` text, and each change the entry above lists is carried here as a reading of the restored line, which governs wherever that line is cited (finding ids as in the entry above): (1) header row "Independent reviewer", read as "INSP-011 (`docs/reviews/SRR/checklists/adrs-001-to-025.md`): iterations 1 to 3 (2026-09-25 and 2026-09-26) and the post-SRR-ruling deltas 1 and 2 (2026-09-26); verdict APPROVED with liens at delta 2. The liens against this file are fixed by the 2026-09-27 errata of section 8, verified at the next INSP-011 delta iteration. That record, not this row, carries every later result"; (2) section 1, line "Hazards in play", for the stamp "0.4.0-pha" read "0.5.0-pha": the line was re-checked against `hazards.json` 0.5.0-pha on 2026-09-27 and its hazard list and every control and cause id it cites hold at that version unchanged; (3) section 4.3, line "Verification cases to add or change", read as "Verification cases to add or change: assembly split TC-SYS-091 (Inspection, REQ-SYS-137 and REQ-SYS-138); the receipt inspection (visual against renders and BOM, polarity, dimensions) and the owner-solder inspection before power-on (continuity of the PA and battery paths, no bridges) are allocated with the receipt-inspection and ATP procedures of the V&V plan (no id yet); ATP includes both". Every other statement of the entry above stands as written. The decision of section 2 is unchanged, and `git diff baseline/srr` of this file shows added lines only. Verification: the next INSP-053 iteration. Author: Claude (ADR author invocation, WP-PDR-14).
