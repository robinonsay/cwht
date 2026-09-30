# ADR-065: Battery-life target of 8 hours at a 1:9 transmit-to-receive ratio, restated for the A5 design with no display (supersedes ADR-020)

| Field | Value |
|---|---|
| ID | ADR-065 |
| Status | Proposed. For the owner's confirmation at PDR session S1 (OD-10 part 1, with ADR-056 items 2 to 4). On the S1 disposition it becomes Accepted by a Status-line edit, and ADR-020's Status becomes "Superseded by ADR-065" (README rule 2; WP-PDR-02). It stays Proposed while its independent review runs, because README rule 2 allows no edit of an Accepted ADR and review fixes must be made in place |
| Date proposed | 2026-09-29 |
| Date decided | Pending (S1). The parts restated unchanged were decided on 2026-09-25 (ADR-020; owner, SI-034). The A5 changes follow from the owner's A5 decision of 2026-09-29 (ADR-056 section 2 item 1) and the A5 rows of TS-012 section 8.10: no display (descope D1), and the REQ-SYS-094 test cell |
| Decision class | 2 (`docs/process/06-risk-and-decision-analysis.md` section 14.1 class 2), as ADR-020: it sets the MOE-004 target and decides no hazard control; the low-battery transmit inhibit that ends the run is HZ-007 control K4, used and not changed. Decision authority stays the owner because the decision fixes a measure of effectiveness and a KDR requirement (REQ-SYS-094). The A5 changes come from TS-012, a class 1 study (06 section 14.1 items (b), the display, and (f), the change to the KDR requirement REQ-SYS-094), and are recorded by ADR-056, the one ADR of TS-012 (06 section 14.2). This ADR takes no new decision and is not a second ADR of TS-012: it restates ADR-020 so that ADR-020 can be superseded in full |
| Decision authority | Robin (owner; the decision fixes a measure of effectiveness and its L1 requirement, and the REQ-SYS-094 change is baseline content carried by CR-018) |
| Author | Claude (technical data manager invocation, WP-PDR-54, 2026-09-29) |
| Independent reviewer | INSP-134 with its software assurance pair INSP-135 (pending). One review record covers ADR-060 to ADR-066 (lead SE ruling of 2026-09-29 on the corrected reading of ruling 1 and on item 4, ruling (d), recorded in ADR-056 section 7; `docs/process/07-software-engineering-plan.md` section 2.1.1 row 3; the INSP-130 precedent of one record for a set of ADRs). Both must be APPROVED before S1, because OD-10 part 1 rests on this record |
| Life-cycle phase | B |
| Baseline affected | baseline/srr (functional baseline: MOE and L1) through CR-018, dispositioned at S1 (OD-40); baseline/pdr |
| Change request | none for this record. The requirement change it restates is carried by CR-018, the re-baseline CR (WP-PDR-53). CR-018 is a provisional number (PDR work plan WP-PDR-53; TS-012 section 8.12): the CR is not yet filed and has no file, and every mention of CR-018 in this record means that provisional re-baseline CR |

## 1. Context

ADR-020 (Accepted, 2026-09-25) sets the battery-life target: at least 8 h from a full charge to the low-battery cutoff at 1:9 transmit-to-receive, and a 6 h floor at 1:4 (SI-034). The owner's A5 decision of 2026-09-29 (ADR-056 section 2 item 1; `docs/decisions/trade-studies/TS-012-design-to-cost-hand-built.md` section 10) keeps the target. It changes two parts of ADR-020:
- **Display.** ADR-020's duty cycle is "90 percent receiving with the display on", and it takes "No backlight in rev A (ADR-006)". A5 has no display: "No display; Morse-only audio UI" (TS-012 descope D1). ADR-006 is proposed as superseded by ADR-056 (ADR-056 section 7, lead SE ruling 1).
- **Test cell and budget.** REQ-SYS-094 names fresh 3000 mAh cells. A5 fits Molicel P28A cells, 2.8 Ah (2.6 Ah minimum; TS-012 section 8.3; ADR-059). TS-012 section 8.10 proposes "Test with the fitted 2.8 Ah P28A cells, or keep 3.0 Ah as the test cell; estimate 8 to 14 h (the module draws about 0.2 A more than a discrete PA at key-down); WP-PDR-29 budgets it". ADR-020 also named "the synthesizer current criterion (ADR-013)". ADR-013 is superseded in full by ADR-056 at S1, with no new ADR (lead SE ruling of 2026-09-29 on the corrected reading of ruling 1 and on item 4, ruling (b), recorded in ADR-056 section 7).

An Accepted ADR is not edited (README rule 2; `docs/process/05-configuration-and-data-management.md` Table 4-1 row 13), and rule 2 has no partial supersession. The lead SE ruled on 2026-09-29 (ADR-056 section 7, ruling (c)) that ADR-020 follows ruling 2, the ADR-026 precedent, where ADR-026 restated ADR-010 and superseded it in full. This ADR therefore restates every unchanged part of ADR-020 verbatim or near-verbatim, states each A5 change with its source, and supersedes ADR-020 in full on the S1 disposition.

ADR-020's context, restated: battery life decides the receiver current budget, the synthesizer choice, the LNA class and the backlight. The power study modelled three receiver builds on a 3000 mAh 2S pack: low (Si5351, 30 mA LNA, no backlight) 13.0 h at 1:9; expected (LMX2571, 60 mA LNA, 20 mA backlight) 9.5 h; high (ADF4351-class LO, PGA-103+ at 5 V, 40 mA backlight) 6.4 h. The owner accepted the target of 8 h at 1:9 (SI-034). At ADR-020 the TPM-008 definition used a different duty (3 min transmit at 50 percent key-down per 10 min, that is 3:7) with a provisional 4 h target. `docs/plan/tpm.json` now defines TPM-008 on the 1:9 cycle with a planned value of 8 h, but with 50 percent key-down within the transmit minute, where this decision sets 45 percent, and with "the display and audio on" in receive. The TPM owner brings it into line at PDR (README open item 4).

- Driving inputs and expectations: SI-034 (second sentence), SI-023 (2S 18650), SI-003 (5 W), SI-005, SI-019 (a day of playing radio). The owner input behind A5's Morse menu in place of the display is in status note 2026-09-27 (TS-012 section 2; section 8.7, owner direction 8). The owner inputs of that note take the next free SI ids when CR-018 appends them (ADR-056 section 1; TS-012 section 8.10, last paragraph).
- Requirements that constrain the decision: at ADR-020, none; TPM-008 and TPM-002 were the measures. Now: REQ-SYS-094 and REQ-SYS-095 (created from ADR-020), REQ-SYS-097 (the transmit inhibit that ends the run).
- Hazards in play (`docs/safety/hazards.json` 0.5.0-pha): none decided. HZ-007 control K4 (the REQ-SYS-097 transmit inhibit that ends the run) is used, not changed. A5 changes K4 elsewhere, and this record does not: its "battery gauge and low-battery warning on the LCD" becomes Morse and LED (REQ-SYS-096, carried by CR-018; ADR-056 section 4.1), and its power-down and 60 C lockout have no rail-off actuator in A5 as drawn (ADR-059 section 4.2; ADR-056 section 4.3). The transmit inhibit that ends the run keeps an actuator in A5 as drawn (ADR-058 section 4.3: of the discharge-side functions, "only the transmit inhibit has an actuator in A5 as drawn").
- Research consulted: as ADR-020: `docs/research/power-tree-and-charging.md` F23 (battery-life model and table; assumptions: 45 percent key-down during transmit, 0.90 buck efficiency, 90 percent usable capacity at Low confidence), F3 (charge time about 10 h at 500 mA; no longer bears on this decision, since A5 has no in-radio charging, ADR-059), F19 (buck and quiescent currents), implications 10 to 18 (power budget candidates); `docs/research/pa-device-candidates.md` F19 (11.4 W DC at 5 W); `docs/research/rf-exposure-evaluation.md` F7 (the 1:9 figure is the ConOps nominal case, not the exposure compliance case); `docs/research/display-and-ui-parts.md` D-UI-02 (no backlight in build 1; A5 goes further, with no display). For the A5 changes: TS-012 sections 8.3 (P28A cells), 8.7 (Morse menu and LED), 8.8 (D1) and 8.10 (row REQ-SYS-094).
- Guidance consulted: SE HB §4.1 (MOEs from stakeholder expectations, via 02 section 6); SE HB §6.8; 06 sections 14.1, 14.2 and 14.6; README rules 1 to 6.
- Assumptions the decision rests on, and how and by when each is confirmed:
  1. 90 percent usable capacity to 3.0 V per cell (Low confidence). Confirmed by the discharge curve digitised at PDR. **(Changed for A5.)** The curve is that of the fitted P28A (ADR-059 assumption 3), and of the 3000 mAh class cell as well if CR-018 keeps 3.0 Ah as the test cell.
  2. 45 percent key-down within transmit periods represents the owner's operating. Confirmed by the owner at SRR (ADR-020 section 6), unchanged.
  3. **(Changed for A5.)** ADR-020 read "The synthesizer and front-end trades keep the expected receiver build. Confirmed by the power budget at PDR with 20 percent margin." TS-012 has made those choices (ADR-056 section 2 item 1). The assumption becomes: the A5 receive, key-down and key-up currents, with the module PA drawing about 0.2 A more than a discrete PA at key-down (TS-012 section 8.10 row REQ-SYS-094), give at least 8 h at 1:9. Confirmed by the WP-PDR-29 battery-life budget on P28A cells at PDR with 20 percent margin (TPM-008 margin policy: at least 9.6 h at 1:9 by analysis at PDR).

## 2. Decision

The radio operates for at least 8 hours from a full charge to the low-battery cutoff (the REQ-SYS-097 transmit inhibit, REQ-SYS-094) on the duty cycle: 10 percent of the time transmitting (with 45 percent key-down at 5 W within the transmit periods) and 90 percent receiving with audio at normal headphone level; and for at least 6 hours at a 1:4 ratio (floor; ADR-020 read "floor, proposed"; **updated, not an A5 change:** adopted by SRR decision 76, owner ruling 2026-09-26; REQ-SYS-095, TBR). This is a measure of effectiveness (MOE) and an L1 requirement verified by Analysis at PDR and CDR (TPM-002 mode powers times derated capacity) and by a Bench run at SAR. TPM-008's definition and planned value are to be changed by the TPM owner to this duty and to 8 h (margin policy unchanged: at least 20 percent above target by analysis at PDR).

**(Changed for A5.)** ADR-020 read "90 percent receiving with the display on and audio at normal headphone level". A5 has no display (TS-012 descope D1), so the receive periods run with no display. The only visual indicator is the Pico 2 on-board LED behind a light pipe (D1: "No UI without headphones except the LED"). It shows the transmit state and the low-battery warning and blinks fault codes (TS-012 section 8.7; section 8.10 rows REQ-SYS-060 and REQ-SYS-096). The run includes the LED as those states drive it.

**(Changed for A5.)** The test cell of REQ-SYS-094 is either the fitted 2.8 Ah P28A or the 3.0 Ah class cell kept as the test cell, as CR-018 sets it (TS-012 section 8.10 row REQ-SYS-094). The 8 h at 1:9 target and the 6 h floor at 1:4 are unchanged.

**(Changed for A5.)** ADR-020 read "The target makes the 'expected' receiver build the minimum acceptable: an ADF4351-class synthesizer at 120 to 170 mA with a 97 mA LNA and a 40 mA backlight does not meet it, so those choices need compensating savings to survive their trades. No backlight in rev A (ADR-006) and the synthesizer current criterion (ADR-013) follow." The choices this target constrained are made by TS-012 (ADR-056 section 2 item 1). The radio has no display, and so no backlight (D1), in place of "No backlight in rev A (ADR-006)". The synthesizer is the Adafruit 2045 Si5351A breakout with the Epson TG2520SMN TCXO on XA. ADR-013 is superseded in full by ADR-056 at S1 (ADR-056 section 7, lead SE ruling (b) of 2026-09-29), and its synthesizer current criterion lapses with it. The target now constrains the A5 power budget of WP-PDR-29. TS-012 estimates 8 to 14 h at 1:9 (section 8.10 row REQ-SYS-094).

## 3. Alternatives considered

| Option | Description | Why not chosen (or why chosen) |
|---|---|---|
| A (chosen) | 8 h at 1:9; 6 h floor at 1:4; no display in the receive periods; the test cell set by CR-018 | Owner acceptance (SI-034) and the A5 decision (ADR-056); a full afternoon of operating. **(Changed for A5.)** ADR-020's third reason, "leaves the synthesizer trade room for the LMX2571-class device", lapses: TS-012 chose the Si5351A (ADR-056 section 2 item 1) |
| A-020 | ADR-020 as decided: receive periods with the display on, fresh 3000 mAh cells | Not chosen: A5 has no display (TS-012 D1) and fits the P28A (TS-012 section 8.3; ADR-059) |
| B | 4 h (TPM-008 provisional) | Rejected: a half-day radio; the owner accepted 8 h |
| C | 12 h | Rejected: forces the low build (Si5351-class LO, 30 mA LNA) and removes the synthesizer trade's freedom |
| D | 8 h at 1:4 | Rejected: same effect as C on the budget; 1:4 is kept as a 6 h floor |

Options B to D are ADR-020's, restated with the reasons as decided. The reason given for option C is historical: TS-012 has now made the synthesizer choice, and its A5 estimate of 8 to 14 h at 1:9 (section 8.10) does not show 12 h. No trade study for the target: the owner set it. At ADR-020 the trades that had to respect it were the synthesizer and receiver front-end trades at PDR. For A5 they are TS-012 (ADR-056), and the target is a criterion of the WP-PDR-29 budget.

## 4. Consequences

### 4.1 Requirements created or changed

When this ADR is Accepted, each requirement that cites ADR-020 adds ADR-065 to `source_ids` (cross item to the CR-018 author).

| Requirement | Relationship | Note |
|---|---|---|
| MOE-004 (battery life for a day out) | allocated by the L0 author; traces to SI-034; not in TS-012 section 8.10 | Cross item to the CR-018 author: the MOE-004 cycle names "the display and audio on" in receive and "a fresh pair of 3000 mAh cells", and NGO-025 names the 3000 mAh cells. TS-012 section 8.10 has no MOE-004 or NGO-025 row. Its L0 paragraph replaces the HSI and ConOps display content with the Morse menu |
| REQ-SYS-094 (battery life at 1:9, KDR) | allocated; cites ADR-020; changed via CR-018 | Test cell only: "Test with the fitted 2.8 Ah P28A cells, or keep 3.0 Ah as the test cell; estimate 8 to 14 h" (TS-012 section 8.10). The 8 h at 1:9 value is kept. Its rationale's "display on" goes with this record. Analysis (PDR, CDR), Bench (SAR). Cross item: add ADR-065 in CR-018 |
| REQ-SYS-095 (battery life at 1:4, TBR) | allocated; does not cite ADR-020; not in TS-012 section 8.10 | The 6 h floor is kept. Cross item to the CR-018 author: its statement also names 3000 mAh cells, and the REQ-SYS-094 test-cell choice applies to it |
| REQ-SYS-096 (low-battery warning) | changed via CR-018; not created by ADR-020 | Listed because MOE-004 carries the warning: announced in Morse, and on the LED (TS-012 section 8.10 row 068, 069, 096, 171; timing unchanged). HZ-007 K4 |
| REQ-PWR (receive current budget allocation per block; low-battery cutoff) | not created at L2 (the PWR file is due at PDR); L1 counterparts REQ-SYS-097 (low-battery transmit inhibit, TBR) and REQ-SYS-098 (low-battery power-down, TBR) | From the F23 model at ADR-020; for A5 from the WP-PDR-29 budget. REQ-SYS-097 and 098 are unchanged and not in section 8.10. REQ-SYS-098 has no rail-off actuator in A5 as drawn (ADR-059 section 4.2; ADR-056 section 4.1) |

### 4.2 Interfaces, design and code

- ICDs affected: none.
- Design elements created or changed: the power budget, the PDR budgets product `docs/design/budgets.md`, as ADR-020. For A5, WP-PDR-29 writes it with "power with the module, battery life on P28A cells" (PDR work plan section 3.0 row 29; WP-PDR-29 outputs); its review record is `docs/reviews/PDR/checklists/analysis-budgets.md`. **(Changed for A5.)** ADR-020 listed the "synthesizer and LNA current as trade criteria; no backlight". The synthesizer and LNA are now fixed by TS-012, so their currents are budget inputs, not trade criteria. There is no display and no backlight (D1), and no display driver (TS-012 section 8.7, "Removed: display driver and encoder drivers").
- New `SW-<SUB>` modules created by this ADR: none.
- ICDs created by this ADR: none.

### 4.3 Verification and safety

- Verification cases to add or change: as ADR-020 (its section 8 reading of 2026-09-27). Battery life is TC-SYS-067 (Bench, REQ-SYS-094: full charge to cutoff on a scripted 1:9 duty into the dummy load). The battery-life Analysis from the power budget is the PDR budgets product (WP-PDR-29). The witnessed SAR run is allocated with the validation cases of the V&V plan (no id yet). **(Changed for A5.)** TC-SYS-067 runs with the test cell that CR-018 sets (ADR-059 section 4.3), and with no display (D1). Its time to the transmit inhibit is read from the UART telemetry (REQ-SYS-150), as the REQ-SYS-094 verification note states. That note names no display.
- Evidence class implications: the Bench run takes 8 hours or more. It is a validation scenario with the owner present at start and end.
- Hazard analysis update required: no, for this decision. The A5 re-reads of HZ-007 K4 (the LCD gauge and warning, and the rail-off gap) are ADR-056's and ADR-059's, carried to WP-PDR-16.
- Safety-critical software scope changed: no.

### 4.4 Cost, schedule, risk

- Cost: none in parts. At ADR-020 the target constrained the synthesizer and LNA choices. For A5 those parts are fixed by TS-012, and the P28A cells are in the A5 BOM (ADR-059 section 4.4).
- Gate affected: PDR (S1 disposition; the WP-PDR-29 budget before S2), SAR (run).
- Risks opened, closed or re-scored: ADR-020 proposed the risk "usable capacity assumption (90 percent to 3.0 V per cell) is Low confidence; the 30Q discharge curve was not digitised" (control: digitise the curve at PDR; Bench run at SAR). RSK-058 (receive power draw above its allocation erodes the battery-life margin) now cites that assumption. **(Changed for A5.)** The cell is the P28A (ADR-059), so the curve to digitise is the P28A's. Cross item to the WP-PDR-18 writer: re-read RSK-058 on the A5 figures (the module's extra 0.2 A at key-down, the P28A cells, no display; TS-012 section 8.10 row REQ-SYS-094).
- TPMs affected:
  - TPM-008: its definition and target are to be brought to this ADR (README open item 4). Cross item to the TPM owner (WP-PDR-29; the TPM product is `docs/plan/tpm.json`, reviewed in `docs/reviews/PDR/checklists/tpm-definitions.md`): its definition also names "3000 mAh 18650 cells" and "the display and audio on".
  - TPM-002: allocations are re-rolled by WP-PDR-29 (ADR-056 section 4.4). Its receive mode reads "display on, audio at 50 % volume", which has no display in A5.

## 5. Compliance and tailoring

none

## 6. Decision record

The target is the owner's, on record before this ADR:

> Owner (2026-09-25, SI-034, second sentence): "Battery-life target accepted: 8 h at a 1:9 transmit-to-receive ratio."

Transcribed from chat into `stakeholder-inputs.md` (ADR-020 section 6). The 45 percent key-down assumption within transmit periods and the 6 h floor at 1:4 are Claude's proposals from the power study, confirmed at SRR (SRR decision 76 for the floor). The display is given up by the owner's A5 decision, recorded in ADR-056 section 6 (Form 1) and TS-012 section 10. A5 includes "A Morse-code audio menu with two buttons and two potentiometers, in place of the display and encoders" (ADR-056 section 2 item 1):

> Owner (2026-09-29, in chat; status note 2026-09-29 section 5, after the A5 parts lifecycle report): "A5"

**Proposed memo wording for S1 (OD-10 part 1; README rule 4).** "Confirm ADR-065. It restates ADR-020, the battery-life target: at least 8 hours when 1 minute in 10 is spent transmitting, and at least 6 hours when 2 minutes in 10 are. The targets do not change. Two things change for A5. The radio has no display, so the receiving part of the test runs with no display, and the only light is the LED. The test cells are either the 2.8 Ah P28A cells you will fit or the 3.0 Ah cells named now; you choose which in the re-baseline change at S1. The study estimates 8 to 14 hours for A5, and the power budget before S2 checks it. ADR-065 is Accepted and ADR-020 becomes Superseded by ADR-065." Owner's disposition: not yet given. It is transcribed here with its date at S1.

## 7. Related

- Supersedes: ADR-020, in full, on the S1 disposition (ADR-020's Status then reads "Superseded by ADR-065", set by WP-PDR-02). Until then ADR-020 stays Accepted and in force.
- Superseded by: none.
- Trade study: none for the target (Decision class row); TS-012 for the A5 changes (ADR-056). At ADR-020 the synthesizer TS (ADR-013) and receiver front-end TS at PDR were to take this target as a criterion. For A5 those choices are TS-012's, TS-001 and TS-007 are proposed as superseded by TS-012 (ADR-056 section 2 item 2, for confirmation at S1), and the target is a criterion of the WP-PDR-29 budget.
- Review where presented: PDR session S1 (OD-10 part 1). ADR-020 was presented at SRR.
- Related records: ADR-056, ADR-059 (the P28A cells and the pack), ADR-058 (the transmit inhibit's actuator in A5), ADR-006 and ADR-013 (superseded by ADR-056); CR-018.
- Revisit conditions:
  - The WP-PDR-29 budget shows A5 below 8 h at 1:9 with 20 percent margin (9.6 h at PDR, TPM-008 margin policy). Then a receiver current reduction, or an owner decision on the target. ADR-020's "a backlight removal is already taken" lapses, since A5 has no display.
  - A cell other than the one CR-018 sets as the test cell is baselined. ADR-020's condition "a cell other than the 3000 mAh class is baselined" is met by A5 (the P28A, ADR-059), and this record is the response to it.

## 8. Change log

- 2026-09-29: created by the technical data manager (WP-PDR-54), on the lead SE ruling of 2026-09-29 on the corrected reading of ruling 1 and on item 4, recorded in ADR-056 section 7. Ruling (c) routes ADR-020 by ruling 2: ADR-020 is contradicted in part (its display clause and "No backlight in rev A (ADR-006)"), README rule 2 has no partial supersession, so this ADR restates ADR-020 in full with the A5 changes and supersedes it on the S1 disposition, as ADR-026 did for ADR-010. Ruling (c) also assigns the number: ADR-060 to ADR-066 are numbered in the order ADR-022, ADR-026, ADR-009, ADR-015, ADR-016, ADR-020, ADR-024. Ruling (d) says they are filed by the lead SE before CR-003 and CR-006 create theirs, each numbered max(existing) + 1 at filing (README rule 1). Ruling (d) also names the review: INSP-134 with its software assurance pair INSP-135. ADR-020's section 8 readings are carried: the independent reviewer reading is replaced by this record's own review, the hazard stamp is 0.5.0-pha, and the verification cases are those of its WP-PDR-14 reading. ADR-013's synthesizer current criterion lapses with ADR-013 (ruling (b)). Author: Claude (technical data manager invocation).
- 2026-09-29 (fix round 1 of INSP-134 and INSP-135, iteration 1; plan WP-PDR-54, rule C1): the decision is unchanged. INSP-134 finding-4: the section 2 floor keeps ADR-020's "floor, proposed" and marks the SRR decision 76 update, and option A marks the lapsed synthesizer reason. INSP-134 finding-8: the budget and TPM products are named as the plan gives them, `docs/design/budgets.md` and `docs/plan/tpm.json`, with `analysis-budgets.md` and `tpm-definitions.md` as their review records. Author: Claude (technical data manager invocation, WP-PDR-54).
