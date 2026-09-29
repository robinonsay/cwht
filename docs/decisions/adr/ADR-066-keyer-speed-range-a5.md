# ADR-066: Keyer speed range 5 to 50 WPM, restated for the A5 design with the speed read in Morse (supersedes ADR-024)

| Field | Value |
|---|---|
| ID | ADR-066 |
| Status | Proposed. For the owner's confirmation at PDR session S1 (OD-10 part 1, with ADR-056 items 2 to 4). On the S1 disposition it becomes Accepted by a Status-line edit, and ADR-024's Status becomes "Superseded by ADR-066" (README rule 2; WP-PDR-02). It stays Proposed while its independent review runs, because README rule 2 allows no edit of an Accepted ADR and review fixes must be made in place |
| Date proposed | 2026-09-29 |
| Date decided | Pending (S1). The parts restated unchanged were decided on 2026-09-25 (ADR-024; owner, SI-033). The A5 change follows from the owner's A5 decision of 2026-09-29 (ADR-056 section 2 item 1): no display (TS-012 descope D1) and the Morse-code audio menu (TS-012 section 8.7) |
| Decision class | 1 (`docs/process/06-risk-and-decision-analysis.md` section 14.1 item (c): HZ-004, HZ-008 and the `SW-KEYER` component of `docs/process/07-software-engineering-plan.md` section 14.1), as ADR-024. Owner-directed range (SI-033). No trade study for the speed range: it is recorded under SEMP customization 11 (`docs/plan/semp.md` section 9.0 and section 5.17), item (i), as ADR-024 recorded it (SRR decision 106). The A5 change comes from TS-012, a class 1 study (06 section 14.1 items (b), the display, and (c), the components of 07 section 14.1), and is recorded by ADR-056, the one ADR of TS-012 (06 section 14.2). This ADR takes no new decision and is not a second ADR of TS-012: it restates ADR-024 so that ADR-024 can be superseded in full |
| Decision authority | Robin (owner; the decision fixes a functional-baseline performance value that drives the envelope, T/R and bandwidth worst cases, and the display change is baseline content carried by CR-018) |
| Author | Claude (technical data manager invocation, WP-PDR-54, 2026-09-29) |
| Independent reviewer | INSP-134 with its software assurance pair INSP-135 (pending). One review record covers ADR-060 to ADR-066 (lead SE ruling of 2026-09-29 on the corrected reading of ruling 1 and on item 4, ruling (d), recorded in ADR-056 section 7; 07 section 2.1.1 row 3, since the decision constrains `SW-KEYER`; the INSP-130 precedent of one record for a set of ADRs). Both must be APPROVED before S1, because OD-10 part 1 rests on this record |
| Life-cycle phase | B |
| Baseline affected | baseline/srr (functional baseline) through CR-018, dispositioned at S1 (OD-40); baseline/pdr |
| Change request | none for this record. The requirement changes it restates are carried by CR-018, the re-baseline CR (WP-PDR-53). CR-018 is a provisional number (PDR work plan WP-PDR-53; TS-012 section 8.12): the CR is not yet filed and has no file, and every mention of CR-018 in this record means that provisional re-baseline CR |

## 1. Context

ADR-024 (Accepted, 2026-09-25) sets the keyer speed range to 5 to 50 WPM, with its default, its timing tolerance, its latency and the consequences of the top speed (SI-033). The owner's A5 decision of 2026-09-29 (ADR-056 section 2 item 1; `docs/decisions/trade-studies/TS-012-design-to-cost-hand-built.md` section 10) keeps the range. It changes one clause. ADR-024 has the current speed "visible on the display while adjusting", and A5 has no display: "No display; Morse-only audio UI" (TS-012 descope D1). In A5 the speed is set and read back in the Morse-code audio menu (TS-012 section 8.7). ADR-024's speed control, "press-and-turn or menu, PDR UX item" (its section 4.2), was taken at SRR decision 45 as "15 WPM; press-and-turn with the WPM on the display; no Morse announcement" (consent agenda, adopted as recommended on 2026-09-26; `docs/reviews/SRR/decisions-for-owner.md`). A5 keeps the 15 WPM default and replaces the rest: there is no tuning knob (D5) and no display (D1), and the speed is announced in Morse.

An Accepted ADR is not edited (README rule 2; `docs/process/05-configuration-and-data-management.md` Table 4-1 row 13), and rule 2 has no partial supersession. The lead SE ruled on 2026-09-29 (ADR-056 section 7, ruling (c)) that ADR-024 follows ruling 2, the ADR-026 precedent, where ADR-026 restated ADR-010 and superseded it in full. This ADR therefore restates every unchanged part of ADR-024 verbatim or near-verbatim, states the A5 change with its source, and supersedes ADR-024 in full on the S1 disposition.

ADR-024's context, restated: the keyer speed range sets the shortest element the transmitter must reproduce cleanly, and with it the maximum envelope time, the T/R lead-in budget, the hang time at speed and the worst-case keying bandwidth at the band edge. Field practice spans 5 to 50 or 60 WPM; the research asked the owner to choose the top (D3). The owner accepted 5 to 50 WPM (SI-033).

- Driving inputs and expectations: SI-033 (first sentence), SI-018, SI-036 (semi break-in hang referenced to speed). The owner input behind A5's Morse menu in place of the display is in status note 2026-09-27 (TS-012 section 2; section 8.7, owner direction 8). The owner inputs of that note take the next free SI ids when CR-018 appends them (ADR-056 section 1; TS-012 section 8.10, last paragraph).
- Requirements that constrain the decision: at ADR-024, the envelope of 5 ms 10-to-90 percent (ADR-023, then proposed) and the relay lead-in (ADR-010, since superseded by ADR-026, which ADR-061 restates for A5). Now also: REQ-SYS-041 and REQ-SW-KEYER-015 (created from ADR-024); REQ-SYS-060 and REQ-SYS-062 (the status content and menu depth that carry the speed read-out; changed via CR-018).
- Hazards in play (`docs/safety/hazards.json` 0.5.0-pha): HZ-004 (paddle watchdog counts elements; element length depends on speed) and HZ-008 (50 WPM is the worst case of the keying bandwidth: REQ-SYS-015 and REQ-TX-006 cite ADR-024 and carry it; control K4). The A5 change adds no hazard. The speed is set in the Morse menu with transmit disarmed (TS-012 section 8.7 step 1), and the menu override command path stays safety-critical (SRR decision 9; ADR-056 section 4.3).
- Research consulted: as ADR-024: `docs/research/keyer-and-key-interfaces.md` F4 (PARIS standard: dit = 1200 ms divided by WPM; dah 3 dits; spaces 1, 3, 7 dits), F6 (speed ranges and adjustment UX in the field), F8 (sidetone), D3, REQ-candidate SW-KEY-03; `docs/research/keyer-verification-and-key-input-network.md` F7 (iambic golden vectors), F8 (timing tolerance plus or minus 1 percent or plus or minus 0.5 ms, whichever larger; simulated-clock harness), F11 (at 50 WPM the 24 ms dit is 2.8 times the 8.5 ms full ramp; rise plus fall occupy 42 percent of a dit at the 10-to-90 points; hang 8 dits is 192 ms at 50 WPM and 1920 ms at 5 WPM), F14, implication 1 (SW-KEY-02 revised), D-KN10 (default 15 WPM); `docs/research/regulatory-corpus-and-operators.md` F6, F7 (50 WPM is the worst case for necessary and 26 dB bandwidth); `docs/research/tr-switch-candidates.md` F4 (listening window and lead-in versus speed); `docs/research/part97-regulatory-basis.md` F10 (automatic identification at most 20 WPM). For the A5 change: TS-012 sections 8.7 (Morse menu, item S, status read-out, LED), 8.8 (D1, D5) and 8.10 (rows REQ-SYS-060, 062 and REQ-SW-KEYER-014).
- Guidance consulted: 47 CFR 97.119(b)(1) (eCFR 2026-09-23); SE HB App. C; SE HB §6.8; 06 sections 14.1, 14.2 and 14.6; README rules 1 to 6.
- Assumptions the decision rests on, and how and by when each is confirmed:
  1. **(Changed for A5.)** ADR-024 read "TIMER0 alarms keep element timing within REQ-SYS-042 at the keyer test point under display and encoder load." A5 has no display and no encoder. The load is the Morse menu sender, the pot scan and the FC0 frequency counter at their maximum rates (REQ-SW-KEYER-014, carried by CR-018; TS-012 section 8.10). Confirmed, as ADR-024, by REQ-SW-KEYER-014: Bench on the dev board (credit false) before PDR and on the delivered unit after TRR.
  2. The 15 WPM default suits the population. Confirmed by package decision 45 at SRR (adopted with the consent agenda on 2026-09-26), unchanged.

## 2. Decision

The built-in keyer sends at any speed from 5 to 50 WPM in 1 WPM steps on the PARIS standard (dit = 1200 ms divided by WPM, dah = 3 dits, intra-character space 1 dit, inter-character 3 dits, inter-word 7 dits), default 15 WPM at first boot, stored in non-volatile memory, adjustable while sending (see the open item below).

**(Changed for A5.)** ADR-024 read "with the current speed visible on the display while adjusting". A5 has no display (TS-012 D1), so the current speed is read in Morse instead:
- **Setting.** The speed is set in the Morse menu, item S. The operator sends digits, or steps the value with the paddle (dit down, dah up). The radio reads the value back in Morse, an R applies it, and an N leaves the previous speed. No entry for 20 s (TBR) exits without change (TS-012 section 8.7, steps 3 to 6).
- **Reading.** Outside the menu, a long press of MENU sends the status in Morse, the speed included (TS-012 section 8.7 rules; REQ-SYS-060, carried by CR-018). The menu letters themselves are sent at the keyer speed (section 8.7 step 2).
- **LED.** There is no LED reading of the speed. The Pico 2 LED shows the transmit state and blinks fault codes (section 8.7).

Element and space timing at the keyer test point is within the larger of plus or minus 1 percent and plus or minus 0.5 ms of nominal across the range (REQ-SYS-042, proposed tolerance, from the reconciled keyer study). The keyer firmware is allocated plus or minus 0.5 percent or plus or minus 0.2 ms, whichever is larger (REQ-SW-KEYER-013). This is the reading of ADR-024 erratum E-10 (its section 8 entry of 2026-09-27), carried here; the decided tolerance is unchanged. Paddle-to-element latency is at most 3 ms (proposed).

Consequences fixed by the top speed:
- the envelope's configurable 10-to-90 time never exceeds 8 ms (full transition 13.6 ms, still under a 24 ms dit);
- the semi break-in hang of 8 dits spans 192 ms at 50 WPM to 1920 ms at 5 WPM;
- the first-element lead-in of at most 12 ms is hidden in the element pipeline for paddles. For A5 the lead-in is 10 ms, set by the G5V-2 operate time of 7 ms maximum plus bounce and margin (TS-012 section 8.10 row REQ-SYS-160, 161). That is within the 12 ms, so this consequence is unchanged.

Any automatic identification memory sends at not more than 20 WPM regardless of the keyer speed (97.119(b)(1)). A5's Morse call-sign announcement at power-on and at headphone insertion (REQ-SYS-006, carried by CR-018) is sent on the PWM tone path to the headphones (TS-012 section 8.7: "Morse sender on the PWM tone path"). It is not a transmission and is not an identification memory.

**Open item for A5 (adjustment while sending).** TS-012 section 8.7 sets the speed in the Morse menu. Step 1 disarms transmit in the menu: "the key line goes to the decoder, and only the sidetone path sounds". TS-012 names no control that changes the speed while transmitting. Its section 8.10 lists no change to REQ-SW-KEYER-016 (speed change at the element boundary), whose rationale rests on this clause ("because the speed control is adjustable while sending"). This record restates the clause as decided and does not decide how A5 meets it. Cross item to WP-PDR-32 and WP-PDR-35 (the Morse-menu module and the SW L2 requirements): either they show how the clause is met, or a change to this clause and to REQ-SW-KEYER-016 goes to the owner through CR-018. Either answer then leads to a superseding ADR, or to a revision of this record before S1.

## 3. Alternatives considered

| Option | Description | Why not chosen (or why chosen) |
|---|---|---|
| A (chosen) | 5 to 50 WPM, default 15; speed set and read back in the Morse menu | Owner acceptance (SI-033) and the A5 decision (ADR-056); covers every operator in the population; 50 WPM leaves the 8 ms maximum envelope under half a dit |
| A-024 | ADR-024 as decided, with the speed on the display while adjusting (press-and-turn, SRR decision 45) | Not chosen: A5 has no display (TS-012 D1) and no tuning knob (D5) |
| B | 5 to 40 WPM | Rejected: the owner accepted 50 |
| C | 5 to 60 WPM | Rejected: a 20 ms dit at 60 WPM would make the 8 ms envelope 40 percent of the dit at 10-to-90 and squeeze the relay lead-in; contest speeds are not the use case |
| D | Speed 0 or a TUNE action for a straight carrier | Not an alternative but a companion: a tune carrier at 0.5 W with a 10 s timeout is a separate requirement proposal (research), not decided here |

No trade study: the owner set the range; the tolerance and latency values are class 2 proposals. The A5 change is TS-012's (ADR-056).

## 4. Consequences

### 4.1 Requirements created or changed

When this ADR is Accepted, each requirement that cites ADR-024 adds ADR-066 to `source_ids` (cross item to the CR-018 author).

| Requirement | Relationship | Note |
|---|---|---|
| REQ-SYS-041 (keyer speed range), REQ-SW-KEYER-015 (keyer speed setting range) | allocated; both cite ADR-024; unchanged; not in TS-012 section 8.10 | ADR-024 wrote "Demonstration"; both requirements' method is Test (HostUnit; Bench for REQ-SYS-041). Cross item: add ADR-066 in CR-018 |
| REQ-SYS-015 (occupied bandwidth, TBR), REQ-TX-006 (keying sideband level, TBR) | allocated; both cite ADR-024; hazard HZ-008; REQ-SYS-015 kept (TS-012 section 8.10), REQ-TX-006 not in section 8.10 | 50 WPM is the bandwidth worst case. For A5 both are implemented by the closed VGG envelope loop with the D-9 and D-10 items (TS-012 section 8.10 row REQ-SYS-014, 015, REQ-TX-005). HZ-008 K4 |
| REQ-SYS-042 (element and space timing accuracy at the keyer test point, TBR: plus or minus 1 percent or 0.5 ms), REQ-SW-KEYER-013 (cites ADR-024: plus or minus 0.5 percent or 0.2 ms, the firmware allocation), REQ-SYS-043 and REQ-SW-KEYER-017 (latency, TBR) | allocated; unchanged; not in section 8.10 | The L2 value is a margin allocation below the L1 value (INSP-011 F-04, dispute accepted); HostUnit with the F7 vectors at 0.1 ms; Bench logic capture at 5, 15, 25, 50 WPM |
| REQ-SW-KEYER-014 (timing under display and encoder load, TBR; cites ADR-024 and ADR-006) | changed via CR-018 | **A5 change.** The same error limits while the Morse menu sender, the pot scan and the FC0 frequency counter run at their maximum rates, with no display and no encoder (TS-012 section 8.10). Section 1 assumption 1 |
| REQ-SYS-135 (settings persistence), REQ-SYS-136 (configuration defaults, TBR), REQ-SW-KEYER-016 (speed change at the element boundary), REQ-SW-KEYER-037 (out-of-range keyer setting commands) | allocated; REQ-SW-KEYER-016 and REQ-SW-KEYER-037 cite ADR-024; unchanged; not in section 8.10 | Default 15 WPM (REQ-SYS-136), 1 WPM steps, non-volatile, adjustable while sending. REQ-SW-KEYER-016 carries the open item of section 2 |
| REQ-SYS-060 (status display content), REQ-SYS-062 (menu depth) | do not cite ADR-024; changed via CR-018 | They carry the speed read-out that replaces the display clause. REQ-SYS-060: the status items, speed among them, are announced in Morse on demand, with the transmit state on the LED. REQ-SYS-062: within two Morse-menu levels from menu entry, with R/N confirmation and a 20 s (TBR) time-out (TS-012 section 8.10 proposals). Cross item: add ADR-066 in CR-018, beside ADR-056 |
| REQ-SYS-044, REQ-SW-KEYER-032 (hang in dits of the displayed speed) | changed via CR-018; ADR-026's | "Of the set speed" (TS-012 section 8.10). Restated by ADR-061, not here; listed because the hang is referenced to the keyer speed |
| Automatic identification at most 20 WPM | not created: rev A has no automatic identification memory; REQ-SYS-068 (identification reminder, TBR; announced in Morse via CR-018) | SRR decision 111 (owner ruling 2026-09-26), with decision 21 ruled 'not in revision A': the section 2 clause constrains any future identification memory only and creates no revision A requirement; a memory added later writes the 47 CFR 97.119(b)(1) limit with it |

### 4.2 Interfaces, design and code

- ICDs affected: none.
- Design elements created or changed:
  - The `SW-KEYER` timing engine is driven from TIMER0 alarms (the rustos work package for the timer and alarms, ADR-019; ADR-053), unchanged.
  - **(Changed for A5.)** ADR-024's "UI speed control (press-and-turn or menu, PDR UX item)" becomes item S of the Morse menu (TS-012 section 8.7). It sits in the Morse-menu module that WP-PDR-32 and WP-PDR-35 name (ADR-056 section 4.2), with the speed read-back and the status read-out on the Morse sender. The display and encoder drivers are removed (TS-012 section 8.7, firmware scope).
- New `SW-<SUB>` modules created by this ADR: none (`SW-KEYER` exists from SRR, ADR-009). `SW-DISPLAY` is removed by ADR-056 (section 4.2).
- ICDs created by this ADR: none.

### 4.3 Verification and safety

- Verification cases to add or change: as ADR-024 (its section 8 reading of 2026-09-27):
  - element and space timing: TC-SW-KEYER-013 (HostUnit) and TC-SW-KEYER-014 (Bench);
  - speed range and setting: TC-SW-KEYER-015 (HostUnit);
  - speed change while sending does not truncate the element in progress: TC-SW-KEYER-016 (HostUnit);
  - Bench logic capture of the PARIS timing at the keyer test point: TC-SYS-028 (REQ-SYS-041 and REQ-SYS-042);
  - envelope TC-SYS-013 and keyed spectrum TC-TX-006 (Simulation).
  
  **(Changed for A5.)** TC-SW-KEYER-014 takes the A5 load of REQ-SW-KEYER-014 (the Morse menu sender, the pot scan and the FC0 counter, in place of display frames and encoder detents) with the requirement, carried by CR-018. The speed read-back in Morse, the R/N confirmation and the out-of-range rejection in the menu are allocated with the Morse-menu SW L2 requirements of WP-PDR-35 (HostUnit; no id yet).
- Evidence class implications: HostUnit primary (simulated clock); Bench confirms on hardware; the paddle watchdog (128 identical elements or 30 s) is tested at both ends of the range.
- Hazard analysis update required: yes, as ADR-024: HZ-008 control K4 sets the 26 dB bandwidth at 50 WPM, and the HZ-004 controls already reference element counts. The A5 change adds no hazard. Cross item to the WP-PDR-16 hazard author: HZ-004 K4 (the paddle watchdog, REQ-SYS-054 and REQ-SYS-184) stops keying "with the sidetone continuing and an alert shown". ADR-056 section 4.3 gives Morse and LED readings for K1 and K3 but does not list K4, so K4's alert also needs its Morse or LED reading.
- Safety-critical software scope (SWE-134 provisions) changed: no, as ADR-024. The Morse-menu override path that the speed setting passes through stays safety-critical (SRR decision 9). That is ADR-056's (section 4.3), not this record's.

### 4.4 Cost, schedule, risk

- Cost: none.
- Gate affected: SRR (L1) at ADR-024; for this record PDR (S1 disposition; `SW-KEYER` and Morse-menu requirements by WP-PDR-35).
- Risks opened, closed or re-scored: RSK-012 (keying wrong or unusable) unchanged; the 50 WPM worst case is already used in the bandwidth analysis.
- TPMs affected: TPM-013 (element timing accuracy over 5 to 50 WPM), unchanged.

## 5. Compliance and tailoring

none

## 6. Decision record

The range is the owner's, on record before this ADR:

> Owner (2026-09-25, SI-033, first sentence): "Keyer speed range 5 to 50 WPM accepted."

Transcribed from chat into `stakeholder-inputs.md` (ADR-024 section 6). The default of 15 WPM and the timing tolerance are Claude's proposals from the reconciled keyer study, confirmed at SRR. The display is given up by the owner's A5 decision, recorded in ADR-056 section 6 (Form 1) and TS-012 section 10. A5 includes "A Morse-code audio menu with two buttons and two potentiometers, in place of the display and encoders" (ADR-056 section 2 item 1):

> Owner (2026-09-29, in chat; status note 2026-09-29 section 5, after the A5 parts lifecycle report): "A5"

**Proposed memo wording for S1 (OD-10 part 1; README rule 4).** "Confirm ADR-066. It restates ADR-024, the keyer speed range of 5 to 50 words per minute, starting at 15, in steps of 1. The range does not change. One thing changes for A5: with no display, you set the speed in the Morse menu by sending the number or stepping it with the paddle, the radio sends the new speed back to you in Morse, and you send R to keep it. A long press of the menu button also tells you the speed in Morse. One point is not settled yet: in the Morse menu the transmitter is off, so the design does not yet show how you change speed while sending. The software design will either show it or bring you a change to decide. ADR-066 is Accepted and ADR-024 becomes Superseded by ADR-066." Owner's disposition: not yet given. It is transcribed here with its date at S1.

## 7. Related

- Supersedes: ADR-024, in full, on the S1 disposition (ADR-024's Status then reads "Superseded by ADR-066", set by WP-PDR-02). Until then ADR-024 stays Accepted and in force.
- Superseded by: none.
- Trade study: none for the range (Decision class row); TS-012 for the A5 change (ADR-056).
- Review where presented: PDR session S1 (OD-10 part 1). ADR-024 was presented at SRR.
- Related records: ADR-056; ADR-061 (restates ADR-026: the hang in dits of the set speed); ADR-062 (restates ADR-009: the key jack and the keyer); ADR-023, ADR-019, ADR-053; CR-018.
- Revisit conditions:
  - The owner asks for 60 WPM: then the envelope maximum and relay lead-in are re-derived by a superseding ADR (as ADR-024).
  - The HITL session moves the default speed (as ADR-024).
  - The open item of section 2 (adjustment while sending) is answered by WP-PDR-32 and WP-PDR-35 or by CR-018: a revision of this record before S1, or a superseding ADR after it.

## 8. Change log

- 2026-09-29: created by the technical data manager (WP-PDR-54), on the lead SE ruling of 2026-09-29 on the corrected reading of ruling 1 and on item 4, recorded in ADR-056 section 7. Ruling (c) routes ADR-024 by ruling 2: ADR-024 is contradicted in part (its clause "with the current speed visible on the display while adjusting"), README rule 2 has no partial supersession, so this ADR restates ADR-024 in full with the A5 change and supersedes it on the S1 disposition, as ADR-026 did for ADR-010. Ruling (c) also assigns the number: ADR-060 to ADR-066 are numbered in the order ADR-022, ADR-026, ADR-009, ADR-015, ADR-016, ADR-020, ADR-024. Ruling (d) says they are filed by the lead SE before CR-003 and CR-006 create theirs, each numbered max(existing) + 1 at filing (README rule 1). Ruling (d) also names the review: INSP-134 with its software assurance pair INSP-135. ADR-024's section 8 entries are carried: the SRR decision 106 class row, the SRR decision 111 identification reading, the erratum E-10 reading of the timing tolerance (in section 2), the independent reviewer reading replaced by this record's own review, the hazard stamp 0.5.0-pha, and the verification cases of its WP-PDR-14 reading. The open item on adjustment while sending (section 2) is raised by this record for the reviewer and the lead SE. Author: Claude (technical data manager invocation).
