# ADR-025: Build quantity: five boards fabricated, three assembled, a hard cap of five complete units

| Field | Value |
|---|---|
| ID | ADR-025 |
| Status | Accepted |
| Date proposed | 2026-09-25 |
| Date decided | 2026-09-25 |
| Decision authority | Robin (owner; the decision spends money at CDR and fixes the regulatory quantity cap) |
| Author | Claude (technical data manager invocation, 2026-09-25) |
| Independent reviewer | Pending: reviewer agent invocation before SRR (01 section 3.2 row S3; 06 section 14.2) |
| Life-cycle phase | Pre-A / A |
| Baseline affected | baseline/srr (functional baseline); product baseline at CDR (order quantities) |
| Change request | none (pre-baseline) |

## 1. Context

47 CFR 15.23(a) exempts from equipment authorization devices that are not marketed, are not constructed from a kit, and are built in quantities of five or less for personal use; cwht's digital section (RP2350, LCD, converters, USB charging) is what that rule reaches, since the amateur transmitter itself needs no authorization. PCBWay quotes fabrication from 5 pieces and assembles from 1 with a setup fee, assembling only boards it fabricated. The owner wants several units so friends can operate together (SI-019). The research recommendation (5 fabricated, 3 assembled, at most 5 complete units) was recorded as standing unless the owner objects (SI-035); a later report recommended assembling all five.

- Driving inputs and expectations: SI-035, SI-019, SI-025 (open design, not marketed), SI-020 (procurement release at CDR)
- Requirements that constrain the decision: none yet
- Hazards in play: none
- Research consulted: `docs/research/pcbway-export-and-vendor-questions.md` F21 (15.23(a) and (b) text; 2.803(a) marketing definition; the five-unit cap comes from the Part 15 digital section), F22 (vendor quantities: fabrication from 5, assembly from 1 to 5), F23 (options A: 5 fabricated and 5 assembled, all kept and lent; B: 5 fabricated and 3 assembled with 2 spare boards; C: more than 5 requires authorization; recommendation A; legal caveat on "personal use" and lending, Low confidence), D-PCB-06; `docs/research/pcbway-fabrication-and-assembly.md` F20 (quantities), F22 (cost signals); `docs/research/part97-regulatory-basis.md` F9 (no authorization for the amateur-built transceiver; not more than five copies without revisiting 15.23); `docs/plan/tpm.json` TPM-014 (budget and quantity set by the owner at SRR)
- Guidance consulted: 47 CFR 15.23, 47 CFR 97.315 (eCFR 2026-09-23); SE HB §6.8

## 2. Decision

Five bare boards are fabricated by PCBWay. Three are assembled by PCBWay in the first order (the SI-035 default); the owner may raise the assembled count to five at CDR (the research option A) when the CDR cost model and the confidence in the design support it, and the two unassembled boards otherwise remain rework or re-spin spares. Across every revision of cwht the number of complete units built is capped at five until an ADR revises the cap with a regulatory assessment; units are the owner's personal units, lent to friends for joint operation and never sold, leased, advertised or offered as kits (47 CFR 2.803(a) marketing definition as quoted in the research). Extra owner-installed parts (for example two spare Pico 2 modules) may be ordered; extra assembled boards may not. The published design (ADR-017) states the cap's basis so that others building it understand their own 15.23 posture.

## 3. Alternatives considered

| Option | Description | Why not chosen (or why chosen) |
|---|---|---|
| A (research option B, chosen as the default) | 5 fabricated, 3 assembled, 2 spare boards; cap 5 complete units | SI-035 default; leaves room for a rework spin without exceeding the cap; lower first-order cost |
| B (research option A) | 5 fabricated, 5 assembled, all lent | Recommended by the later report; available to the owner at CDR; costs two more assembled boards and uses the whole cap on rev A |
| C | More than 5 complete units | Rejected: requires Supplier's Declaration of Conformity testing of the digital section or a redesign around an authorized module; out of scope |
| D | 1 or 2 units | Rejected: SI-019 wants several people operating together; fabrication minimum is 5 boards anyway |

No trade study: a quantity decision under a regulatory cap; recorded here with the owner's default.

## 4. Consequences

### 4.1 Requirements created or changed

| Requirement | Relationship | Note |
|---|---|---|
| REQ-SYS-NNN (constraint: at most five complete units built across all revisions; units not marketed; L1 author allocates) | new, constraint traced to SI-035, SI-025 with `47CFR15.23` cited in `source_ids` | Inspection (build records, `docs/vv/adp/` unit count) |
| none for the assembled count | | Order quantity is a product-baseline (CDR) parameter, recorded in the cost model and the assembly package |

### 4.2 Interfaces, design and code

- ICDs affected: none
- Design elements created or changed: unit serials `CWHT-A-001` to at most `CWHT-A-005` (05 section 4.3); cost model quantity
- New `SW-<SUB>` modules created by this ADR: none
- ICDs created by this ADR: none

### 4.3 Verification and safety

- Verification cases to add or change: none; the configuration audit at SAR counts the units
- Evidence class implications: none
- Hazard analysis update required: no
- Safety-critical software scope changed: no

### 4.4 Cost, schedule, risk

- Cost: assembly for 3 versus 5 boards (the PCBWay assembly quote scales with quantity and unique parts); the enclosure order matches the assembled count
- Gate affected: CDR (order quantities), SAR (unit count)
- Risks opened, closed or re-scored: RSK-008 (first power-on fails and a second spin is required) is the reason for the two spare boards in the default; new risk proposed: "the 15.23 'personal use' reading for lent units is Low confidence" (control: units lent, never transferred; owner may seek confirmation)
- TPMs affected: TPM-014 (unit cost is divided by the build quantity)

## 5. Compliance and tailoring

none

## 6. Decision record

> Owner (2026-09-25, SI-035, second sentence): "build quantity recommendation (5 bare boards, 3 assembled, at most 5 complete units) stands unless the owner objects."

Transcribed from chat into `stakeholder-inputs.md`. The acceptance is by the owner's stated default; the SRR decision memo records confirmation or objection, and the assembled count (3 or 5) is confirmed in the CDR decision memo.

## 7. Related

- Supersedes: none
- Superseded by: none
- Trade study: none
- Review where presented: SRR (default confirmed), CDR (assembled count)
- Revisit conditions: the owner wants more than five units (regulatory assessment first); the first three units pass acceptance and the owner wants the remaining two assembled (a second PCBWay assembly order within the cap, no ADR change)
