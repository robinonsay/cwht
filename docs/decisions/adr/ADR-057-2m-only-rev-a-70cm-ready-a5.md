# ADR-057: 2 m band only in rev A with a 70 cm-ready architecture, restated for the A5 design (supersedes ADR-002)

| Field | Value |
|---|---|
| ID | ADR-057 |
| Status | Proposed. For the owner's confirmation at PDR session S1 (OD-10 part 1, with ADR-056 items 2 to 4). On the S1 disposition it becomes Accepted by a Status-line edit, and ADR-002's Status becomes "Superseded by ADR-057" (README rule 2; WP-PDR-02). It stays Proposed while its independent review runs, because README rule 2 allows no edit of an Accepted ADR and review fixes must be made in place |
| Date proposed | 2026-09-29 |
| Date decided | Pending (S1). The parts restated unchanged were decided on 2026-09-25 (ADR-002; owner, SI-002), and the five-point meaning of "70 cm-ready" was confirmed as SRR decision 98 on 2026-09-26 (README, open item 2). The two A5 changes were decided with the owner's A5 decision of 2026-09-29 (ADR-056 section 2 item 1) |
| Decision class | 2 for what ADR-002 decided (`docs/process/06-risk-and-decision-analysis.md` section 14.1 class 2: the band scope is a stakeholder expectation, NGO-008 and CON-022, and the meaning of "70 cm-ready" is a recorded convention; ADR-002 header). The two A5 changes of section 2 points (3) and (4) come from TS-012, a class 1 study (point (3) follows from its synthesizer choice, item (b); point (4) is its descope D8), and are recorded by ADR-056, the one ADR of TS-012 (06 section 14.2). This ADR takes no new decision and is not a second ADR of TS-012: it restates ADR-002 so that ADR-002 can be superseded in full |
| Decision authority | Robin (owner; the decision fixes the functional baseline scope, and the jack change alters baseline content through CR-003 revision 4) |
| Author | Claude (technical data manager invocation, WP-PDR-54 part 1 follow-on, 2026-09-29) |
| Independent reviewer | Pending. The same review as ADR-056 (WP-PDR-54: an independent reviewer with a software assurance pair; the lead SE assigns the record ids and paths). The record must be APPROVED before S1, because OD-10 part 1 rests on it |
| Life-cycle phase | B |
| Baseline affected | baseline/srr (functional baseline) through CR-003 revision 4 and CR-018, both dispositioned at S1 (OD-40); baseline/pdr (the allocated baseline is written on this scope) |
| Change request | none for this record. The requirement changes it restates are carried by CR-003 revision 4 section 1.1a (REQ-SYS-104, REQ-SYS-106) and by CR-018, the re-baseline CR (REQ-SYS-146). CR-018 is a provisional number (PDR work plan WP-PDR-53; TS-012 section 8.12): the CR is not yet filed and has no file, and every mention of CR-018 in this record means that provisional re-baseline CR |

## 1. Context

ADR-002 (Accepted, 2026-09-25) fixes rev A to the 2 m band and says in five points what "70 cm-ready" means; the owner confirmed the five points as SRR decision 98. The owner's A5 decision of 2026-09-29 (ADR-056 section 2 item 1; `docs/decisions/trade-studies/TS-012-design-to-cost-hand-built.md` section 10) changes two of them, points (3) and (4), and gives points (1) and (5) an A5 reading:
- **Point (4), the antenna jack.** ADR-002 names a stainless SMA jack, and SRR decision 80 chose the SMA jack, described there as "female body, stainless, bulkhead-retained by the enclosure boss". A5 fits a gold-plated brass-class edge-mount SMA jack, TE/Linx CONSMA003.062-G, rated about 100 mating cycles against 500 for stainless, on cost (TS-012 section 8.8 descope D8; section 8.3 row 17). The jack is an edge-mount part soldered to the board edge (row 17, "edge mount"; section 8.10 row REQ-SYS-175), which is not the retention SRR decision 80 describes, "bulkhead-retained by the enclosure boss". An edge-mount jack held only by its solder joints is HZ-009 cause C1 ("Jack mounted on the PCB only, carrying the antenna moment into solder joints and copper"). TS-012 does not state how the printed end wall retains it. Sections 2 and 4 carry this to REQ-SYS-105 and HZ-009 K1.
- **Point (3), the 70 cm LO criterion.** ADR-002 has the synthesizer trade carry "LO coverage for a 430 to 450 MHz plan" as an enhancing criterion. TS-012 chose the synthesizer (ADR-056 section 2 item 1), though not by the method of ADR-013 (ADR-056 section 7 item 4), and scored no such criterion (TS-012 section 3.1, criteria C1 to C8). A5 gives up 70 cm (descope D15): the Si5351A output ends at 200 MHz, and the PA module covers 135 to 175 MHz. ADR-002's own revisit condition names this case: the enhancing criterion "is dropped by a superseding ADR, not silently".
- **Points (1) and (5), A5 readings.** Their meaning is kept. The reserved band control becomes a Morse-menu entry in place of a display field (REQ-SYS-146), and the synthesizer joins the band-specific blocks (REQ-SYS-145: "the synthesizer and the module are band-dependent"; both rows of TS-012 section 8.10).

An Accepted ADR is not edited (README rule 2; `docs/process/05-configuration-and-data-management.md` Table 4-1 row 13), and rule 2 has no partial supersession. The lead SE ruled on 2026-09-29 (ruling 2, recorded in ADR-056 section 7) to follow the ADR-026 precedent, where ADR-026 restated ADR-010 and superseded it in full. This ADR therefore restates every unchanged part of ADR-002 verbatim or near-verbatim, states the two A5 changes with their sources, and supersedes ADR-002 in full on the S1 disposition. ADR-002's context stands as the record of why the band was fixed: a dual-band rev A would double the RF hardware (PA, low-pass filter, LNA, T/R switching), the regulatory verification (47 CFR 97.307(e) at two fundamentals) and the RF exposure evaluation, and without a recorded scope the L1 requirements could not fix frequency coverage, and "70 cm-ready" would mean whatever each author assumed.

- Driving inputs and expectations: SI-002, SI-001 (pocket form factor), SI-024 (full 2 m band), SI-006 (band control listed as "future"); NGO-008 and CON-022 (ADR-002 header). For the A5 changes: the owner's A5 decision of 2026-09-29 (ADR-056 section 6) and the owner's USD 300 maximum (status note 2026-09-27 section 10, as TS-012 section 2 quotes it), which takes the next free SI id when CR-018 appends the owner inputs of that note.
- Requirements that constrain the decision: at ADR-002, none; the requirements schema carries the tag `70cm-ready` (`docs/requirements/schema.json`, `tags` description). Now: REQ-SYS-145 and REQ-SYS-146 (section 4.1), and REQ-SYS-104, REQ-SYS-106 and REQ-SYS-175 for the antenna port.
- Hazards in play (`docs/safety/hazards.json` 0.5.0-pha): none new from the band scope. HZ-001, HZ-006 and HZ-008 are evaluated for 144 to 148 MHz only (HZ-001 scales with band; the third harmonic of 2 m falls in the 70 cm band, HZ-008). HZ-009 (antenna connector mechanical failure): its controls K1 and K2 name the stainless 500-cycle jack, which point (4) changes. K1 also requires that "the PCB connection carries no antenna moment" (a pigtail to a board connector, or a PCB-mount bulkhead jack with a documented tolerance stack), and cause C1 is a jack mounted on the PCB only; the edge-mount jack of point (4) is that case unless the end wall retains it.
- Research consulted: as ADR-002: `docs/research/part97-regulatory-basis.md` F1 (A1A permitted on the entire 2 m band), F2 (third harmonic 432 to 444 MHz falls in the 70 cm band); `docs/research/regulatory-corpus-and-operators.md` F9 (US allocations at each 2 m harmonic; 70 cm shared with Federal radiolocation); `docs/research/2m-cw-transceiver-reference-designs.md` F16, F20 (synthesizer ranges: Si5351A 2.5 kHz to 200 MHz, LMX2571 10 to 1344 MHz), Table 1 (single-band reference designs); `docs/research/pa-device-candidates.md` F17 (LPF goal 35 dB at 432 to 444 MHz, the 70 cm band, for rev A). For the A5 changes: `docs/research/antenna-and-erp.md` F8 (brass SMA "Connector Durability 100 matings", stainless "500 mating cycles"; SMA 50 ohm, flexible-cable SMA 0 to 12.4 GHz); `docs/research/pa-device-candidates.md` F8 (RA07M1317M, 135 to 175 MHz); TS-012 sections 3.1, 3.2 (the LMX2571 pruned as reflow-only), 8.3, 8.8 (D8, D15) and 8.10.
- Guidance consulted: 47 CFR 97.301(a) and 97.305 (eCFR 2026-09-23); SE HB §6.8; 06 sections 14.1, 14.2 and 14.6; README rules 1 to 6.
- Assumptions the decision rests on, and how and by when each is confirmed:
  1. The five-point meaning of "70 cm-ready" in section 2, as restated, is what the owner intends. Points (1), (2) and (5) were confirmed as SRR decision 98. The changed points (3) and (4), and the A5 readings of points (1) and (5), are confirmed at S1 with this ADR.
  2. ADR-002's second assumption, that the 70 cm enhancing criterion adds no rev A cost beyond the synthesizer choice, is withdrawn with the criterion (point (3)).
  3. The gold-plated brass-class jack is rated for at least 100 mating cycles at the handbook torque. Confirmed by reading the jack datasheet at WP-PDR-38 (CR-003 revision 4, REQ-SYS-106 `tbr.plan`).
  4. The printed end wall can retain the edge-mount jack so that the 4.0 N m antenna moment of REQ-SYS-105 is carried by the enclosure and not by the jack's solder joints (HZ-009 K1, cause C1). Confirmed by the WP-PDR-27 enclosure work (TS-011 re-scored for A5) with the printed fit check and the static load test of HZ-009 K6, before CDR. If it cannot be shown, the jack choice goes back to the owner with the cost of a bulkhead jack and pigtail.

## 2. Decision

Rev A transmits and receives on 2 m only (144.000 to 148.000 MHz, ADR-016). "70 cm-ready" means, for rev A:
1. The control architecture is band-agnostic: frequency plan, band edges, guard, power steps and tuning limits are data, not code paths, and the UI reserves a band control (SI-006) that rev A does not expose. **(A5 reading.)** With the Morse-code menu of A5, the reservation is an enclosure position, a controller input and a Morse-menu entry, in place of a display field (TS-012 section 8.10, REQ-SYS-146).
2. Requirements that rev B would inherit unchanged are tagged `70cm-ready`, and band-specific requirements are tagged `revA`.
3. **(Changed for A5.)** Rev A carries no 70 cm LO coverage. The synthesizer of A5 (the Adafruit 2045 Si5351A breakout with the TG2520SMN TCXO, ADR-056 section 2 item 1) ends at 200 MHz, and ADR-002's enhancing criterion "LO coverage for a 430 to 450 MHz plan" is dropped (TS-012 descope D15). A 70 cm LO is a rev B choice.
4. **(Changed for A5.)** The antenna port is an SMA female jack usable on both bands, of the gold-plated brass class (TE/Linx CONSMA003.062-G, edge mount), rated about 100 mating cycles (TBR) in place of the stainless jack's 500 (TS-012 descope D8). As SRR decision 80 intended, the enclosure, not the jack's solder joints, carries the antenna moment (REQ-SYS-105, 4.0 N m); the retention of the edge-mount jack in the printed end wall is a PDR design item (section 1 assumption 4).
5. The band-specific blocks are documented as replaceable modules in the architecture, with their interfaces to the common blocks (control, power, audio, keyer) in ICDs. **(A5 reading.)** For A5 they are the PA module and driver, the harmonic low-pass filter, the LNA and front-end filter, the T/R element and the synthesizer (TS-012 section 8.10, REQ-SYS-145: "the synthesizer and the module are band-dependent"). Rev B therefore replaces the band-specific blocks and the firmware data, not the common blocks, so it is not a new radio.

Rev A carries no 70 cm hardware, no dual-band antenna requirement and no 70 cm verification.

## 3. Alternatives considered

| Option | Description | Why not chosen (or why chosen) |
|---|---|---|
| A (chosen) | 2 m only in rev A; architecture and requirement tagging keep the 70 cm path open; A5 jack and synthesizer (points (3) and (4)) | Owner direction (SI-002); A5 decided by the owner (ADR-056); halves RF verification |
| A-002 | ADR-002 as decided: stainless SMA jack and a 70 cm LO enhancing criterion | Not chosen: the A5 jack is the gold-plated brass class on cost (D8), and the synthesizer study TS-012 carried no 70 cm criterion; an LO that reaches 70 cm, such as the LMX2571 (10 to 1344 MHz, `2m-cw-transceiver-reference-designs.md` F20), was pruned as reflow-only (TS-012 section 3.2) |
| B | Dual-band 144/430 MHz rev A | Rejected: two PA line-ups or a broadband PA with two filters, two exposure evaluations, two 97.307(e) campaigns; pocket volume and battery (SI-001, SI-034) do not absorb it on this schedule |
| C | 2 m only with no provision for 70 cm | Rejected by the owner's "keep the path open" |
| D | 70 cm first | Not requested; 2 m CW has the weak-signal segment and the owner's operating interest |

No trade study for the band: the owner's direction fixed it, and the meaning of "70 cm-ready" is a recorded convention (06 section 14.1 class 2 content, decided by the owner because it scopes the baseline). The two A5 changes come from TS-012 (ADR-056).

## 4. Consequences

### 4.1 Requirements created or changed

When this ADR is Accepted, each requirement that cites ADR-002 adds ADR-057 to `source_ids` (cross item to the CR-018 author).

| Requirement | Relationship | Note |
|---|---|---|
| REQ-SYS-008 (transmit frequency range with band-edge guard, TBR), REQ-SYS-021 (receive frequency range), REQ-TX-002 (transmit carrier frequency range, TBR) | allocated; they cite ADR-016, not this ADR | REQ-SYS-008 and REQ-TX-002 kept (TS-012 section 8.10, "Keep (TCXO fitted, D-17)"); REQ-SYS-021 is not in section 8.10 |
| REQ-SYS-145 (band-dependent functions partitioned) | allocated; cites ADR-002; value kept (TS-012 section 8.10) | The synthesizer joins the band-dependent blocks (point (5)). Cross item: add ADR-057 to `source_ids` in CR-018 |
| REQ-SYS-146 (reserved band control) | allocated; implements point (1) without citing ADR-002; reworded via CR-018 | "Reserved enclosure position, controller input and Morse-menu entry" (TS-012 section 8.10) |
| REQ-SYS-104 (antenna connector) | changed via CR-003 revision 4 section 1.1a; does not cite ADR-002 | Statement made material-neutral ("a 50 ohm SMA jack with a female body"); the jack class is recorded in ICD-TX-ANT and the BOM. ADR-056 section 4.1 routes this row to CR-003 revision 4 as well |
| REQ-SYS-106 (antenna port mating life) | changed via CR-003 revision 4 section 1.1a | 500 to 100 mating cycles (TBR); HZ-009 K2 |
| REQ-SYS-105 (antenna port mechanical load path, 4.0 N m) | value kept; rationale and verification note changed via CR-003 revision 4 ("the enclosure carries the moment (a bulkhead-retained jack or another retention in the printed end wall that the PDR enclosure trade sizes ...)") | HZ-009 K1 and K2. With the edge-mount jack of point (4) the load path is not yet stated. Cross item to WP-PDR-27 and WP-PDR-39: show the 4.0 N m moment carried by the end wall with no moment into the jack's solder joints (section 1 assumption 4) |
| REQ-SYS-175 (antenna port on one end face) | kept (TS-012 section 8.10) | Edge-mount SMA on the far end face |
| tagging rule: `revA` for band-specific, `70cm-ready` for band-independent requirements | not a requirement: a tagging convention | Reviewer checks the tag at requirements validation |

### 4.2 Interfaces, design and code

- ICDs affected: `ICD-TX-ANT` (SMA jack common to both bands; CR-003 revision 4 changes its jack row from the stainless 500-cycle jack to the gold-plated brass-class edge-mount jack, CONSMA003.062-G class, and 100 matings, TBR).
- Design elements created or changed: the architecture (WP-PDR-31, written from TS-012 section 8.1) partitions the band-specific modules of point (5) from the common modules; frequency plan held as data in `cwht-core`.
- New `SW-<SUB>` modules created by this ADR: none.
- ICDs created by this ADR: none. The internal ICDs between band-specific and common blocks, including the new RF-board ICD, are WP-PDR-36's (TS-012 section 8.12).

### 4.3 Verification and safety

- Verification cases to add or change: none for 70 cm in rev A; every `regulatory` case is written for 144 to 148 MHz. The jack cases follow CR-003 revision 4: TC-SYS-058 (Inspection, REQ-SYS-104) and TC-SYS-073 (the mating life from the jack datasheet rating and the handbook torque, REQ-SYS-106).
- Evidence class implications: none.
- Hazard analysis update required: yes. HZ-009 K1 and K2 name the stainless 500-cycle jack; CR-003 revision 4 (section 4, safety row) routes the K2 change, 500 to 100 cycles with the handbook advice, to WP-PDR-16b. K1's retention ("retained to the machined enclosure by its bulkhead nut through a boss"; "the PCB connection carries no antenna moment") and cause C1 (a jack mounted on the PCB only) are re-read for the edge-mount jack in the printed end wall: cross item to WP-PDR-16b with the WP-PDR-27 load path (section 4.1, REQ-SYS-105). K3 loses its fold-back clause (ADR-056 section 4.3).
- Safety-critical software scope changed: no.

### 4.4 Cost, schedule, risk

- BOM, fabrication, enclosure or lead-time impact: the jack is USD 4.47 (TS-012 section 8.3 row 17, aggregator read 2026-09-27). No 70 cm cost in rev A: with point (3) the synthesizer carries no 70 cm criterion.
- Gate affected: PDR (S1 disposition; architecture partition), rev B SRR (re-entry).
- Risks opened, closed or re-scored: ADR-002 proposed the risk "70 cm-ready provisions grow rev A scope (board area TPM-009, synthesizer cost) without a rev B commitment"; with point (3) its synthesizer-cost part lapses and its board-area part stays. RSK-025 (antenna port retention fails under the whip side load) is read with the 100-cycle edge-mount jack and its retention in the printed end wall (TS-012 header, related risks; section 1 assumption 4).
- TPMs affected: TPM-009 (PCB area utilization), watched for provision creep.

## 5. Compliance and tailoring

none

## 6. Decision record

The band decision and points (1), (2) and (5) are the owner's, on record before this ADR:

> Owner (2026-09-25, SI-002): "2 m band for the first iteration; 70 cm deferred to a later revision but keep the path open."

Transcribed from chat into `stakeholder-inputs.md` (ADR-002 section 6). The five-point meaning was confirmed as SRR decision 98 (owner ruling 2026-09-26; README, open item 2).

The two A5 changes come from the owner's A5 decision, recorded in ADR-056 section 6 (Form 1) and TS-012 section 10:

> Owner (2026-09-29, in chat; status note 2026-09-29 section 5, after the A5 parts lifecycle report): "A5"

**Proposed memo wording for S1 (OD-10 part 1; README rule 4).** "Confirm ADR-057. It restates ADR-002 with two A5 changes: the antenna jack is a gold-plated brass-class SMA rated about 100 matings (TBR), and rev A carries no 70 cm LO coverage criterion, because the A5 synthesizer ends at 200 MHz. The jack is edge-mounted, and the printed end wall, not the jack's solder joints, carries the antenna moment; how it is retained is a PDR design item. ADR-057 is Accepted and ADR-002 becomes Superseded by ADR-057." Owner's disposition: not yet given. It is transcribed here with its date at S1.

## 7. Related

- Supersedes: ADR-002, in full, on the S1 disposition (ADR-002's Status then reads "Superseded by ADR-057", set by WP-PDR-02). Until then ADR-002 stays Accepted and in force.
- Superseded by: none.
- Trade study: none for the band scope (class 2 content); TS-012 for points (3) and (4), recorded by ADR-056.
- Review where presented: PDR session S1 (OD-10 part 1). ADR-002 was presented at SRR.
- Related records: ADR-056 (the A5 decision; section 7 records the lead SE rulings); ADR-013 and ADR-016; CR-003 revision 4; CR-018; SRR decisions 80 and 98. SRR decision 80 chose the SMA jack "female body, stainless, bulkhead-retained by the enclosure boss"; point (4) changes its material and its mount (edge mount), and keeps its intent that the enclosure carries the antenna moment.
- Revisit conditions: rev B formulation; a later antenna or synthesizer choice that changes points (3) to (5) (a superseding ADR, not silently). ADR-002's condition "a synthesizer or antenna choice that cannot reach 70 cm at similar cost" has triggered with the A5 synthesizer, and this ADR is the superseding ADR it asks for. The jack datasheet read at WP-PDR-38 shows a mating life under 100 cycles (then REQ-SYS-106 and the handbook change by CR).

## 8. Change log

- 2026-09-29: created by the technical data manager (WP-PDR-54 part 1 follow-on), on lead SE ruling 2 of 2026-09-29 (ADR-056 section 7): ADR-002 is contradicted only in part, README rule 2 has no partial supersession, so this ADR restates ADR-002 in full with the A5 changes and supersedes it on the S1 disposition, as ADR-026 did for ADR-010. The number is the next free one, max(existing) + 1 (README rule 1). ADR-056 section 7 as filed (`66f6123`) named point (4) only. Point (3) is added here, and in ADR-056 section 7 (`abe5706`), because A5 also contradicts it (TS-012 descope D15) and ADR-002's revisit condition requires a superseding ADR to record that; it is for the lead SE's confirmation. Author: Claude (technical data manager invocation).
- 2026-09-29: fix round on the findings of the independent review and its software assurance pair (INSP-130, INSP-131; WP-PDR-54). No decision content changes. The lead SE confirmed on 2026-09-29 (WP-PDR-54 fix-round brief) that the change to ADR-002 point (3), the 70 cm LO criterion, belongs in this ADR; the entry above that left it "for the lead SE's confirmation" is closed by this entry (reviewer finding-3). The edge mount of point (4) is carried to its consequences: section 1 (point (4) bullet and the HZ-009 line), a new assumption 4, the section 2 point (4) retention sentence (the intent of SRR decision 80 and REQ-SYS-105, not a new decision), a REQ-SYS-105 row in section 4.1, the HZ-009 K1 and cause C1 line in section 4.3, the memo wording and section 7 (reviewer finding-8). Section 1 point (3) no longer reads ADR-056 section 7 as saying that TS-012 applied ADR-013's method (ADR-056 section 7 item 4). CR-018 is marked as a provisional number with no file (reviewer finding-7). The REQ-SYS-104 note follows ADR-056 section 4.1 as corrected. Author: Claude (technical data manager invocation, WP-PDR-54 fix round).
