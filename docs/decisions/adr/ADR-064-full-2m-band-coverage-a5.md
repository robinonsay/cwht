# ADR-064: Frequency coverage of the full US 2 m band, 144.000 to 148.000 MHz, restated for the A5 design (supersedes ADR-016)

| Field | Value |
|---|---|
| ID | ADR-064 |
| Status | Proposed. For the owner's confirmation at PDR session S1 (OD-10 part 1, with ADR-056 items 2 to 4). On the S1 disposition it becomes Accepted by a Status-line edit, and ADR-016's Status becomes "Superseded by ADR-064" (README rule 2; WP-PDR-02). It stays Proposed while its independent review runs, because README rule 2 allows no edit of an Accepted ADR and review fixes must be made in place |
| Date proposed | 2026-09-29 |
| Date decided | Pending (S1). The parts restated unchanged were decided on 2026-09-25 (ADR-016; owner, SI-024). Two values that ADR-016 left open were ruled at SRR on 2026-09-26: the 1.2 kHz band-edge guard (SRR decision 25, recorded in ADR-023) and the power-on presets (SRR decision 26). The A5 changes were decided with the owner's A5 decision of 2026-09-29 (ADR-056 section 2 item 1): A5 has no display and no tuning encoder (TS-012 descopes D1 and D5) |
| Decision class | 1 (`docs/process/06-risk-and-decision-analysis.md` section 14.1 item (c): HZ-008 and the carrier limits of the `SW-SYNTH` component of 07 section 14.1), as ADR-016. Owner-directed (SI-024), recorded without a trade study for the coverage under SEMP customization 11 (`docs/plan/semp.md` section 9.0 and section 5.17), item (i), as ADR-016 was (SRR decision 106). The A5 changes come from TS-012, a class 1 study (06 section 14.1 item (b), the display as a critical part), and are recorded by ADR-056, the one ADR of TS-012 (06 section 14.2; section 2 item 3, the TS-010 row). This ADR takes no new decision on the coverage or the carrier limit and is not a second ADR of TS-012: it restates ADR-016 so that ADR-016 can be superseded in full. One part of section 2 is this record's own proposal, not stated in TS-012: the Morse announcement of the CW-only segment when the set frequency enters it, and in the frequency read-back and each status announcement while it is inside it (marked "proposed reading" in section 2). The owner confirms or corrects it with her S1 disposition of this record |
| Decision authority | Robin (owner; the decision fixes a functional-baseline performance requirement, and the A5 changes alter baseline content through CR-018) |
| Author | Claude (technical data manager invocation, WP-PDR-54, 2026-09-29) |
| Independent reviewer | INSP-134 with its software assurance pair INSP-135 (pending). One review record covers ADR-060 to ADR-066 (lead SE ruling of 2026-09-29 on the corrected reading of ruling 1 and on item 4 (ADR-056 section 7), ruling (d); `docs/process/07-software-engineering-plan.md` section 2.1.1 row 3, because the decision constrains the carrier limits of `SW-SYNTH`; the INSP-130 precedent of one record for a set of ADRs). Both must be APPROVED before S1, because OD-10 part 1 rests on this record |
| Life-cycle phase | B |
| Baseline affected | baseline/srr (functional baseline) through CR-018, dispositioned at S1 (OD-40); baseline/pdr |
| Change request | none for this record. The requirement and ConOps changes it restates are carried by CR-018, the re-baseline CR (WP-PDR-53). CR-018 is a provisional number (PDR work plan WP-PDR-53; TS-012 section 8.12): the CR is not yet filed and has no file, and every mention of CR-018 in this record means that provisional re-baseline CR |

## 1. Context

ADR-016 (Accepted, 2026-09-25) fixes continuous tuning across the whole US 2 m band, a firmware limit on the transmit carrier at each band edge, no lock to the band-plan CW segment, and proposed defaults. One clause of its section 2 needs a display: the default "144.000 to 144.100 MHz CW-only segment indicated on the display". The owner's A5 decision of 2026-09-29 (ADR-056 section 2 item 1; `docs/decisions/trade-studies/TS-012-design-to-cost-hand-built.md` section 10) removes the display ("No display; Morse-only audio UI", TS-012 section 8.8 descope D1) and the tuning encoder ("Tuning by Morse direct entry, pot fine window and paddle steps", descope D5). So the clause cannot be met as written (ADR-056 section 7 item 4). ADR-016's other display clause, the carrier limit "enforced independently of the display and tuning logic so that a display fault cannot key outside the band", stays true with no display (ADR-056 section 7 item 4). Full-band coverage and the band-edge limit survive (ADR-056 section 7 item 4; TS-012 section 8.10, REQ-SYS-008, 009 and REQ-TX-002 "Keep (TCXO fitted, D-17)").

Two values in ADR-016 section 2 were written before SRR and were ruled there. They are not A5 changes, and this ADR states them as ruled:
- **The guard.** ADR-016 gives "144.001 to 147.999 MHz (the 1 kHz band-edge guard proposed in ADR-023)". SRR decision 25 set the guard to 1.2 kHz, and ADR-023 was accepted with it: "The transmit carrier is confined to 144.0012 to 147.9988 MHz (a 1.2 kHz guard at each edge, TBR ...)" (ADR-023 section 2 item (2)). REQ-SYS-008 and REQ-TX-002 read 144.0012 to 147.9988 MHz (TBR). ADR-016's own revisit condition names this case: a wider guard narrows the carrier range "by the same superseding ADR".
- **The presets.** ADR-016 section 2 marks its defaults "proposed, pending SRR" and names 144.100 and 144.200 MHz. SRR decision 26 was adopted with the consent agenda: "Full band without a lock; presets 144.050 and 144.100 MHz with the CW-only segment highlighted" (`docs/reviews/SRR/decision-memo.md`, decision 26).

ADR-016 section 8 has no reading of these two values against SRR decisions 25 and 26. That is not changed here: cross item to the lead SE, the ADR author and WP-PDR-02 (lead SE ruling of 2026-09-29 on the INSP-134 findings, part (3)).

An Accepted ADR is not edited (README rule 2; `docs/process/05-configuration-and-data-management.md` Table 4-1 row 13), and rule 2 has no partial supersession. The lead SE ruled on 2026-09-29 (ruling (c) of the ruling on the corrected reading of ruling 1 and on item 4, recorded in ADR-056 section 7) that ADR-016 follows ruling 2, the ADR-026 precedent, where ADR-026 restated ADR-010 and superseded it in full, and numbered this restatement ADR-064. This ADR therefore restates every unchanged part of ADR-016 verbatim or near-verbatim, states the A5 changes with their sources, and supersedes ADR-016 in full on the S1 disposition.

ADR-016's context, restated: 47 CFR 97.301(a) gives every US license class from Technician up the whole 144 to 148 MHz band in ITU Region 2, and 97.305 permits CW on all of it; the voluntary ARRL band plan puts CW in 144.00 to 144.10 MHz with 144.200 MHz as the weak-signal calling frequency. A design could lock the transmitter to the CW segment with an expert unlock, or cover the whole band. The owner chose full coverage (SI-024). The band edges then interact with the keying bandwidth and the reference tolerance (ADR-023).

- Driving inputs and expectations: SI-024, SI-005 (tune to a frequency and chat), SI-030 (Technician and above: full 2 m privileges), SI-002, as ADR-016. For the A5 changes: the owner inputs of status note 2026-09-27 sections 6 and 8 (the Morse-code audio menu), which take the next free SI ids when CR-018 appends them (TS-012 section 8.10, "L0, interfaces and hazards").
- Requirements that constrain the decision: at ADR-016, none. Now: REQ-SYS-008, REQ-SYS-021 and REQ-TX-002, created from ADR-016; REQ-SYS-009 and REQ-SYS-182 (the inhibit outside the guard and the independent frequency verification).
- Hazards in play (`docs/safety/hazards.json` 0.5.0-pha): HZ-008 (out-of-band emission; REQ-SYS-008 and REQ-TX-002 cite ADR-016 and carry it; controls K4 and K7 rest on the carrier range). K4 already states the 1.2 kHz guard ("carrier limited to 144.0012 to 147.9988 MHz (TBR; the 1.2 kHz guard ratified by SRR package decision 25)"). For A5, K7 runs on route R3 (D-17; ADR-056 section 4.3).
- Research consulted: as ADR-016: `docs/research/part97-regulatory-basis.md` F1 (97.305: CW permitted on the entire band; 144.000 to 144.100 MHz CW-only), F4 (97.301(a), 97.303: no US 2 m sharing constraint), F5 (ARRL plan: voluntary, 144.000 to 144.100 CW, 144.200 calling, EME at the bottom), F11 (band edges and keying bandwidth), REQ-candidates RF-01, RF-02, OPS-01, DECISION-3, RISK RF-3; `docs/research/regulatory-corpus-and-operators.md` F8 (1 kHz guard: carrier 144.001 to 147.999 MHz, before SRR decision 25 widened it). For the A5 changes: TS-012 sections 8.1, 8.3 (row 9), 8.7, 8.8 (D1, D5, D15), 8.10 and 8.14 (D-17); `docs/design/analysis/frequency-budget.md` (route R3).
- Guidance consulted: 47 CFR 97.301(a), 97.305, 97.307(b) (eCFR 2026-09-23); SE HB §6.8; 06 sections 14.1, 14.2 and 14.6; README rules 1 to 6.
- Assumptions the decision rests on, and how and by when each is confirmed:
  1. The synthesizer covers 144.000 to 148.000 MHz plus the BFO offset. ADR-016 had this confirmed by the synthesizer and reference trade study at PDR, which was TS-007; TS-007 is superseded by TS-012 (ADR-056 section 2 item 2). For A5 the synthesizer is the Adafruit Si5351A breakout for the LO, the transmit carrier and the BFO (TS-012 section 8.3 row 9), whose output ends at 200 MHz (D15). Confirmed by the frequency budget and clock plan of WP-PDR-20, which carries TS-007's remaining analyses (ADR-056 section 2 item 2), before S2.
  2. The band-edge check closes by tinySA or by Analysis. Confirmed when the tinySA RBW is verified on receipt (ACTION-9), as ADR-016. The owner buys the tinySA Ultra later, inside the separate equipment cap (TS-012 exception EX-13).
  3. An operator hears the CW-segment announcement only with headphones plugged in (TS-012 D1: "No UI without headphones except the LED"). The segment is a voluntary band-plan aid, not a transmit limit, so an operator without headphones loses the aid only. Confirmed with the Morse-menu usability run of the UI design (WP-PDR-33).

## 2. Decision

The receiver and transmitter tune continuously across 144.000 to 148.000 MHz. The transmit carrier is confined by firmware to 144.0012 to 147.9988 MHz (TBR; the 1.2 kHz band-edge guard of ADR-023, set by SRR decision 25, in place of the 144.001 to 147.999 MHz and the 1 kHz guard that ADR-016 gave when ADR-023 proposed it; not an A5 change), enforced independently of the display and tuning logic so that a display fault cannot key outside the band; the receiver may tune to the edges. **(A5 reading.)** A5 has no display (TS-012 D1), so the clause stays true; its "tuning logic" includes the Morse menu's frequency entry, the fine-tuning potentiometer and the paddle steps, and the independent frequency verification checks the set frequency against the guard before PA_EN (HZ-008 K7, on route R3 for A5, D-17). There is no lock to the band-plan CW segment and no expert unlock. Defaults: power-on presets in the weak-signal segment at 144.050 and 144.100 MHz (as ruled by SRR decision 26, in place of ADR-016's proposed 144.100 and 144.200 MHz; not an A5 change), and the 144.000 to 144.100 MHz CW-only segment highlighted. **(Changed for A5; proposed reading of this record, not stated in TS-012.)** The segment is announced in Morse in the headphones, in place of being indicated on the display, which A5 does not have (TS-012 D1 and section 8.7): the radio announces it when the set frequency enters the segment, by Morse direct entry, the fine-tuning potentiometer or a paddle step, and the frequency read-back and each status announcement name it while the set frequency is inside it. The words sent are fixed by the UI design of WP-PDR-33. The handbook explains the voluntary band plan. **(Changed for A5.)** Tuning is by Morse direct frequency entry, a fine-tuning potentiometer window of +/-5 kHz around the entered centre at 20 Hz resolution or better, and a paddle step mode of 10 Hz to 10 kHz (TS-012 D5 and section 8.7; REQ-SYS-058, carried by CR-018), in place of a tuning knob; the step sizes within those bounds are a UI design item at PDR (WP-PDR-33). The receiver BFO and sidetone offset are adjustable in 10 Hz steps (proposed).

## 3. Alternatives considered

| Option | Description | Why not chosen (or why chosen) |
|---|---|---|
| A (chosen) | Full 144.000 to 148.000 MHz with a 1.2 kHz transmit guard at each edge (ADR-023); CW-only segment announced in Morse | Owner direction (SI-024); lawful for every operator class in the population; a synthesizer covers it trivially (as ADR-016). The Morse announcement is the A5 medium (TS-012 D1) |
| A-016 | ADR-016 as decided: CW-only segment indicated on the display | Not possible: A5 has no display (TS-012 D1) |
| B | Lock to 144.000 to 144.300 MHz with an expert unlock | Rejected by the owner (as ADR-016); adds UI state and a way to be "locked out" on a hilltop; SRR decision 26 confirmed "Full band without a lock" |
| C | CW segment only, 144.000 to 144.100 MHz | Rejected (as ADR-016): excludes the 144.200 calling frequency and simplex chat elsewhere in the band |

No trade study: the owner's direction fixed coverage; the presets are class 2 proposals, ruled at SRR (decision 26). The announcement medium and the tuning controls are TS-012's (ADR-056).

## 4. Consequences

### 4.1 Requirements created or changed

When this ADR is Accepted, each requirement that cites ADR-016 adds ADR-064 to `source_ids`, carried by CR-018 (cross item to the CR-018 author): REQ-SYS-008, REQ-SYS-021 and REQ-TX-002.

| Requirement | Relationship | Note |
|---|---|---|
| REQ-SYS-008 (transmit frequency range with band-edge guard, TBR), REQ-SYS-021 (receive frequency range), REQ-TX-002 (transmit carrier frequency range, TBR) | allocated; all cite ADR-016, REQ-SYS-008 and REQ-TX-002 also ADR-023; hazard HZ-008 on REQ-SYS-008 and REQ-TX-002; kept (TS-012 section 8.10: "Keep (TCXO fitted, D-17)"; REQ-SYS-021 is not in section 8.10) | 144.0012 to 147.9988 MHz (TBR) at the 1.2 kHz guard of SRR decision 25. HZ-008 K4 (008, REQ-TX-002) |
| REQ-SYS-009 (transmit inhibit outside the guard, TBR; cites ADR-023), REQ-SYS-182 (independent frequency verification before and during transmit, TBR) | allocated; hazard HZ-008; candidate RF-01; kept (TS-012 section 8.10: REQ-SYS-182 "Keep ... on route R3") | ADR-016 read "HostUnit boundary tests at 143.999 and 148.001 MHz; Bench with the tinySA", points outside the band that a firmware with no 1.2 kHz guard would also pass. **(Updated, not an A5 change.)** The test points are those of the REQ-SYS-009 verification note, inside the guard: HostUnit key events at 143.999 to 144.0011 MHz and 147.9989 to 148.000 MHz produce no PA_EN; Bench keyed at 144.0005 and 147.9995 MHz with the tinySA (closing case TC-SYS-008). HZ-008 K4 (009) and K7 (182) |
| Presets and CW-segment indication (candidate OPS-01) | not created: carried to the PDR UI design (WP-PDR-33, `docs/design/analysis/ui-design.md`), now with the Morse announcement of section 2 | Inspection, Demonstration (as ADR-016). The presets are SRR decision 26's |
| REQ-SYS-058 (tuning), REQ-SYS-164 (band crossing time) | changed, carried by CR-018 (TS-012 section 8.10) | Neither cites ADR-016; listed because section 2 restates the tuning controls. REQ-SYS-058 as section 2 states it; REQ-SYS-164: any in-band frequency reached by Morse direct entry within 30 s (TBR) |
| REQ-SYS-060 (status content) | changed, carried by CR-018 (TS-012 section 8.10: "Announce the same items in Morse on demand") | Does not cite ADR-016; SRR decision 26 lists it among the requirements it affects. The status announcement names the CW-only segment while the frequency is in it (section 2) |
| ConOps OPS-003 step 1 and OPS-020 step 4 (the CW-only segment "highlighted on the display") | changed with the ConOps display content, carried by CR-018 (TS-012 section 8.10, "HSI and ConOps display content replaced by the Morse menu") | `docs/conops/conops.md` sections OPS-003 and OPS-020 |

### 4.2 Interfaces, design and code

- ICDs affected: none (as ADR-016).
- Design elements created or changed: frequency plan data (band edges, guard, presets) in `cwht-core`; synthesizer configuration range, which for A5 is the Si5351A with the TG2520SMN TCXO on XA (TS-012 section 8.3 rows 9 and 29; ADR-056 section 2 item 1). **(Changed for A5.)** The CW-segment announcement is part of the Morse menu's status and read-back output (TS-012 section 8.7, "status and fault announcements"); the Morse-menu module is named by WP-PDR-32 and WP-PDR-35 (ADR-056 section 4.2).
- New `SW-<SUB>` modules created by this ADR: none.
- ICDs created by this ADR: none.

### 4.3 Verification and safety

- Verification cases to add or change (ADR-016's WP-PDR-14 reading, carried): receive tuning range TC-SYS-016 (Bench, REQ-SYS-021); transmit carrier limits and inhibit TC-SYS-008 and TC-TX-002 (Bench, REQ-SYS-008 and REQ-TX-002); keyed spectrum TC-TX-006 (Simulation); the SW L2 carrier-limit case (HostUnit) is allocated with the SW L2 requirements at PDR (no id yet). **(Changed for A5.)** TC-SYS-008 and TC-TX-002 are not carried unchanged: TC-SYS-008 reads "the display transmit-state field" and passes on "the display shows the guard inhibit", and TC-TX-002 has the frequency "commanded with the tuning control and read from the display". For A5 each sets the frequency by Morse direct entry and reads it back in Morse, and TC-SYS-008 reads the guard inhibit from the Morse transmit-state reason (REQ-SYS-060 as CR-018 changes it; the words are the UI design's, WP-PDR-33). Cross item to the CR-018 author. **For A5:** the CW-segment announcement is checked in the UI design analysis of WP-PDR-33 and by a HostUnit case with the Morse-menu L2 requirements (WP-PDR-35; no id yet), and on the unit by decoding the audio capture.
- Evidence class implications: the band-edge check depends on the tinySA RBW (ACTION-9 of the corpus report, Low confidence that a 100 Hz class RBW exists); Analysis covers the keying spectrum (as ADR-016). The tinySA is not yet bought (assumption 2).
- Hazard analysis update required: yes (HZ-008 controls K4 and K7 rest on the carrier range; as ADR-016). For A5, K7 runs on route R3 (D-17), its text for R3 is requested of WP-PDR-16b (TS-012 section 8.10, row REQ-SYS-182), and its "a disagreement enters Fault-safe with the cause shown" becomes the Morse and LED cause message of the fault annunciation (REQ-SYS-067 as carried by CR-018; ADR-056 section 4.3). The CW-segment announcement carries no hazard control: the segment is voluntary and the carrier limit does not depend on it.
- Safety-critical software scope changed: no by this ADR. ADR-016's "pending the SWE-134 scoping of the transmit inhibit" was answered at SRR: frequency control is safety-critical (SRR decision 9, which removes single point failure row 4; 07 section 14.1). For A5, `SW-SAFE` gains the FC0 check with a threshold of 5.0 kHz (ADR-056 section 4.3; TS-012 section 8.10, row REQ-SYS-182).

### 4.4 Cost, schedule, risk

- Cost: none (as ADR-016).
- Gate affected: PDR (S1 disposition; frequency plan, UI design), as ADR-016's PDR entry; SRR (L1) is past.
- Risks opened, closed or re-scored: RSK-002 (LO error) relates through the guard, and is re-read on the TCXO and route R3 (ADR-056 section 4.4); proposed risk "band-edge violation by reference drift" (REG-6) is mitigated by ADR-023 (as ADR-016).
- TPMs affected: TPM-006 (frequency stability).

## 5. Compliance and tailoring

none

## 6. Decision record

The coverage is the owner's, on record before this ADR:

> Owner (2026-09-25, SI-024): "Frequency coverage: the full US 2 m band, 144.000 to 148.000 MHz."

Transcribed from chat into `stakeholder-inputs.md` (ADR-016 section 6). The guard and the presets were ruled at SRR: decision 25 (key decision K12, the 1.2 kHz guard; ADR-023 section 6) and decision 26, "Adopted with the consent agenda: Full band without a lock; presets 144.050 and 144.100 MHz with the CW-only segment highlighted" (`docs/reviews/SRR/decision-memo.md`), under the owner's disposition:

> Owner (2026-09-26, SRR disposition, `docs/reviews/SRR/minutes.md` section "Disposition"): "I approve of this and the SRR."

The display and the tuning encoder are given up by the owner's A5 decision, recorded in ADR-056 section 6 (Form 1) and TS-012 section 10; A5 includes "A Morse-code audio menu with two buttons and two potentiometers, in place of the display and encoders" (ADR-056 section 2 item 1):

> Owner (2026-09-29, in chat; status note 2026-09-29 section 5, after the A5 parts lifecycle report): "A5"

**Proposed memo wording for S1 (OD-10 part 1; README rule 4).** "Confirm ADR-064. It restates ADR-016, full coverage of the 2 m band from 144 to 148 MHz with no lock to the CW part of the band, with two changes for A5, because A5 has no screen and no tuning knob. When the frequency moves into the CW-only part of the band, 144.000 to 144.100 MHz, the radio tells you in Morse, and a status request says so too. That announcement is this record's proposal: the A5 study removes the screen but does not say how the CW part is shown, so please confirm it or say how you want it. You tune by sending the frequency in Morse, then fine-tune with a knob within 5 kHz either side, or step with the paddle. The limit that stops the radio transmitting outside the band is unchanged and does not depend on the menu. The record also writes in two values you already decided at SRR: the 1.2 kHz margin at each band edge and the start-up frequencies 144.050 and 144.100 MHz. ADR-064 is Accepted and ADR-016 becomes Superseded by ADR-064." Owner's disposition: not yet given. It is transcribed here with its date at S1.

## 7. Related

- Supersedes: ADR-016, in full, on the S1 disposition (ADR-016's Status then reads "Superseded by ADR-064", set by WP-PDR-02). Until then ADR-016 stays Accepted and in force.
- Superseded by: none.
- Trade study: none for the coverage; TS-012 for the announcement medium, the tuning controls and the synthesizer (ADR-056).
- Review where presented: PDR session S1 (OD-10 part 1). ADR-016 was presented at SRR.
- Related records: ADR-056 (section 7 item 4), ADR-023; CR-018.
- Revisit conditions:
  - The guard changes from the 1.2 kHz of ADR-023 (then the carrier range changes by the same superseding ADR; ADR-016's condition, with ADR-023 now decided).
  - A regional band plan change (ACTION-4 of the Part 97 report) moves the presets (as ADR-016).
  - The TCXO becomes unavailable, so that route R3 no longer holds and REQ-SYS-182 would need widening (TS-012 section 8.10, row REQ-SYS-182; section 10 revisit condition).
  - A display is added in a later build: a superseding ADR.

## 8. Change log

- 2026-09-29: created by the technical data manager (WP-PDR-54), on the lead SE ruling of 2026-09-29 on the corrected reading of ruling 1 and on item 4 (ADR-056 section 7), rulings (c) and (d): ADR-016 is contradicted only in its CW-segment display clause (and its tuning-knob basis, TS-012 D5), README rule 2 has no partial supersession, so this ADR restates ADR-016 in full with the A5 changes and supersedes it on the S1 disposition, as ADR-026 did for ADR-010. The number is the one the ruling gives, in the order ADR-060 to ADR-066; it is max(existing) + 1 (README rule 1) when the lead SE files ADR-060 to ADR-066 in that order, before CR-003 and CR-006 create theirs (ruling (d)). ADR-016's section 8 readings are carried: the independent reviewer reading is replaced by this record's own review, the hazard stamp is 0.5.0-pha, and the verification cases are those of its WP-PDR-14 reading. Found in drafting and stated as ruled, not as A5 changes: ADR-016 section 2 still gives the 1 kHz guard (144.001 to 147.999 MHz) and the proposed presets 144.100 and 144.200 MHz, and no section 8 entry of ADR-016 reads them against SRR decisions 25 and 26; this ADR states 144.0012 to 147.9988 MHz (TBR) and 144.050 and 144.100 MHz. The CW-segment announcement is this record's Morse reading of the display clause, for the owner's confirmation at S1. Author: Claude (technical data manager invocation).
- 2026-09-29 (fix round 1 of INSP-134 and INSP-135, iteration 1; plan WP-PDR-54, rule C1): the decision is unchanged. INSP-134 finding-5: the Decision class row, section 2 and the memo say that the CW-segment announcement is this record's proposed reading, not stated in TS-012, for the owner at S1. INSP-134 finding-6: TC-SYS-008 and TC-TX-002, which read the display, change with CR-018. INSP-135 finding-6: the REQ-SYS-009 row keeps ADR-016's text and marks the update to the verification-note points inside the 1.2 kHz guard. The ADR-016 section 8 gap on SRR decisions 25 and 26 is recorded as a cross item to the lead SE, the ADR author and WP-PDR-02 (lead SE ruling part (3)). Author: Claude (technical data manager invocation, WP-PDR-54).
