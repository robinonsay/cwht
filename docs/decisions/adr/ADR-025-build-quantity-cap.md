# ADR-025: Build quantity: five boards fabricated, three assembled, a hard cap of five complete units

| Field | Value |
|---|---|
| ID | ADR-025 |
| Status | Accepted |
| Date proposed | 2026-09-25 |
| Date decided | 2026-09-25 |
| Decision class | 2 (`docs/process/06-risk-and-decision-analysis.md` section 14.1 class 2: build quantity under a regulatory cap). Decision authority stays Robin because the decision spends money |
| Decision authority | Robin (owner; the decision spends money at CDR and fixes the regulatory quantity cap) |
| Author | Claude (technical data manager invocation, 2026-09-25) |
| Independent reviewer | INSP-011 (`docs/reviews/SRR/checklists/adrs-001-to-025.md`): iterations 1 and 2 (2026-09-25) NEEDS CHANGES, findings F-01, F-03, F-08 and F-09 against this file; the Major-finding corrections are applied here on 2026-09-26 (section 8); verification pending at INSP-011 iteration 3 |
| Life-cycle phase | Pre-A / A |
| Baseline affected | baseline/srr (functional baseline); product baseline at CDR (order quantities) |
| Change request | none (pre-baseline) |

## 1. Context

47 CFR 15.23(a) exempts from equipment authorization devices that are not marketed, are not constructed from a kit, and are built in quantities of five or less for personal use; cwht's digital section (RP2350, LCD, converters, USB charging) is what that rule reaches, since the amateur transmitter itself needs no authorization. PCBWay quotes fabrication from 5 pieces and assembles from 1 with a setup fee, assembling only boards it fabricated. The owner wants several units so friends can operate together (SI-019). The research recommendation (5 fabricated, 3 assembled, at most 5 complete units) was recorded as standing unless the owner objects (SI-035); a later report recommended assembling all five.

- Driving inputs and expectations: SI-035, SI-019, SI-025 (open design, not marketed), SI-020 (procurement release at CDR)
- Requirements that constrain the decision: none yet
- Hazards in play (`docs/safety/hazards.json` 0.4.0-pha): none
- Research consulted: `docs/research/pcbway-export-and-vendor-questions.md` F21 (15.23(a) and (b) text; 2.803(a) marketing definition; the five-unit cap comes from the Part 15 digital section), F22 (vendor quantities: fabrication from 5, assembly from 1 to 5), F23 (options A: 5 fabricated and 5 assembled, all kept and lent; B: 5 fabricated and 3 assembled with 2 spare boards; C: more than 5 requires authorization; recommendation A; legal caveat on "personal use" and lending, Low confidence), D-PCB-06; `docs/research/pcbway-fabrication-and-assembly.md` F20 (quantities), F22 (cost signals); `docs/research/part97-regulatory-basis.md` F9 (no authorization for the amateur-built transceiver; not more than five copies without revisiting 15.23); `docs/plan/tpm.json` TPM-014 (budget and quantity set by the owner at SRR)
- Guidance consulted: 47 CFR 15.23, 47 CFR 97.315 (eCFR 2026-09-23); SE HB §6.8
- Assumptions the decision rests on, and how and by when each is confirmed:
  1. Lending units to friends is "personal use" under 47 CFR 15.23(a) (Low confidence, `docs/research/pcbway-export-and-vendor-questions.md` F23). A revisit condition; the owner may seek confirmation.
  2. The PCBWay fabrication minimum stays 5 boards. Confirmed by the CDR quote.

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
| REQ-SYS-125 (build quantity cap) | allocated; cites this ADR; `47CFR15.23` in `source_ids` | Inspection (build records, `docs/vv/adp/` unit count) |
| none for the assembled count |  | Order quantity is a product-baseline (CDR) parameter, recorded in the cost model and the assembly package |

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

## 8. Change log

- 2026-09-26: one-time pre-baseline correction under INSP-011 ruling R-1 option (A), as directed by the lead SE: Decision class row and section 1 Assumptions line added (F-01); hazard line and "Hazard analysis update required" re-derived against `docs/safety/hazards.json` 0.4.0-pha (F-02); section 4.1 placeholder ids replaced by the ids the requirement authors allocated, or marked not created with the reason (F-03). Content from `reconciliation-srr.md` sections 2, 3, 5.1 and 6, re-checked against the requirement, hazard and expectation files of 2026-09-26; that register is superseded by this file for this ADR. The decision of section 2 is unchanged. Minor findings are liens, fixed before PDR: F-08 (erratum E-7, the 47 CFR 2.803(a) citation); F-09 was closed at iteration 2. The edit of an Accepted ADR rests on the owner's approval of R-1 (A) in the SRR decision memo and the matching sentence in `docs/process/05-configuration-and-data-management.md` Table 4-1 row 13 (both pending). Class 1 choices without a trade study wait on ruling R-2 (owner). Author: Claude (ADR author invocation).
- 2026-09-27 (PDR errata, WP-PDR-14; SRR liens L-6 and, where named, L-4 and L-7): Independent reviewer row names the INSP-011 results through the post-SRR-ruling delta 2 and points to the record for later results, replacing "verification pending at INSP-011 iteration 3" (F-13); hazard line stamp 0.4.0-pha changed to 0.5.0-pha, the version at HEAD, after re-checking the line against it (F-13; for ADR-015, 022, 023 and 026 also SRR lien L-7); section 1 cites 47 CFR 2.803(a) as a research finding with its confidence tag (F-08, erratum E-7). F-08, section 2 part: section 2 is not edited. Its citation "(47 CFR 2.803(a) marketing definition as quoted in the research)" is read as the research finding `docs/research/pcbway-export-and-vendor-questions.md` F21 (High confidence in that report's confidence table), not as a verbatim-corpus citation: 47 CFR 2.803 is not in `docs/references/md/regulatory/`. If the owner adds it under PDR plan item OD-24 (a), later citations use the corpus file. Route: the SRR decision memo carries these findings as liens to be fixed in the product before the PDR readiness declaration (RFA-SRR-006: "Fix each finding in its product"); they are applied by the ADR correction route the owner approved as SRR decision 105 (corrections outside section 2, each logged in this section), as the README paragraph "PDR errata" records. The decision of section 2 is unchanged. The first entry's "(both pending)" no longer holds: SRR decision 105 approved R-1 option (A) on 2026-09-26 and the 05 Table 4-1 row 13 sentence is in place (INSP-011 F-13). Author: Claude (ADR author invocation, WP-PDR-14).
- 2026-09-27 (correction of the WP-PDR-14 entry above; INSP-053 finding-1, `docs/reviews/PDR/checklists/adrs-001-to-027.md`): the entry above records edits in place of 3 lines outside section 8 made after the `baseline/srr` tag, which 05 Table 4-1 row 13, the Record class of 05 section 4.2 and README rule 2 do not allow. Its "Route" sentence is withdrawn: the SRR lien direction (RFA-SRR-006) does not amend row 13, and the decision 105 route was the exception before the tag only. Those 3 lines are restored to their `baseline/srr` text, and each change the entry above lists is carried here as a reading of the restored line, which governs wherever that line is cited (finding ids as in the entry above): (1) header row "Independent reviewer", read as "INSP-011 (`docs/reviews/SRR/checklists/adrs-001-to-025.md`): iterations 1 to 3 (2026-09-25 and 2026-09-26) and the post-SRR-ruling deltas 1 and 2 (2026-09-26); verdict APPROVED with liens at delta 2. The liens against this file are fixed by the 2026-09-27 errata of section 8, verified at the next INSP-011 delta iteration. That record, not this row, carries every later result"; (2) section 1, line "Hazards in play", for the stamp "0.4.0-pha" read "0.5.0-pha": the line was re-checked against `hazards.json` 0.5.0-pha on 2026-09-27 and its hazard list and every control and cause id it cites hold at that version unchanged; (3) section 1, line "Research consulted", F21 parenthesis, for "2.803(a) marketing definition;" read "47 CFR 2.803(a) marketing definition as quoted in that report, High confidence in its confidence table, since 47 CFR 2.803 is not in the verbatim corpus `docs/references/md/regulatory/` and F21 notes an amendment published 2026-09-11;". Every other statement of the entry above stands as written. The decision of section 2 is unchanged, and `git diff baseline/srr` of this file shows added lines only. Verification: the next INSP-053 iteration. Author: Claude (ADR author invocation, WP-PDR-14).
