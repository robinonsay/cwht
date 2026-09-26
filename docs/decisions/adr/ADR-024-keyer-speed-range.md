# ADR-024: Keyer speed range 5 to 50 WPM

| Field | Value |
|---|---|
| ID | ADR-024 |
| Status | Accepted |
| Date proposed | 2026-09-25 |
| Date decided | 2026-09-25 |
| Decision class | 1 (`docs/process/06-risk-and-decision-analysis.md` section 14.1 item (c): HZ-004, HZ-008 and the `SW-KEYER` component of 07 section 14.1). Owner-directed range (SI-033). No trade study for the speed range: this ADR alone records it only if the owner adopts ruling R-2 item (i) of `reconciliation-srr.md` section 7 (open; the owner's ruling); otherwise a trade study is opened, or a waiver of 06 section 14.1 is recorded, before `baseline/srr` |
| Decision authority | Robin (owner; the decision fixes a functional-baseline performance value that drives the envelope, T/R and bandwidth worst cases) |
| Author | Claude (technical data manager invocation, 2026-09-25) |
| Independent reviewer | INSP-011 (`docs/reviews/SRR/checklists/adrs-001-to-025.md`): iterations 1 and 2 (2026-09-25) NEEDS CHANGES, findings F-01, F-03 and F-04 (sub-item disputed and accepted) against this file; the Major-finding corrections are applied here on 2026-09-26 (section 8); verification pending at INSP-011 iteration 3 |
| Life-cycle phase | Pre-A / A |
| Baseline affected | baseline/srr (functional baseline, to be tagged at SRR) |
| Change request | none (pre-baseline) |

## 1. Context

The keyer speed range sets the shortest element the transmitter must reproduce cleanly, and with it the maximum envelope time, the T/R lead-in budget, the hang time at speed and the worst-case keying bandwidth at the band edge. Field practice spans 5 to 50 or 60 WPM; the research asked the owner to choose the top (D3). The owner accepted 5 to 50 WPM (SI-033).

- Driving inputs and expectations: SI-033 (first sentence), SI-018, SI-036 (semi break-in hang referenced to speed)
- Requirements that constrain the decision: envelope 5 ms 10-to-90 percent (ADR-023 proposed); relay lead-in (ADR-010)
- Hazards in play (`docs/safety/hazards.json` 0.4.0-pha): HZ-004 (paddle watchdog counts elements; element length depends on speed) and HZ-008 (50 WPM is the worst case of the keying bandwidth: REQ-SYS-015 and REQ-TX-006 cite this ADR and carry it; control K4)
- Research consulted: `docs/research/keyer-and-key-interfaces.md` F4 (PARIS standard: dit = 1200 ms divided by WPM; dah 3 dits; spaces 1, 3, 7 dits), F6 (speed ranges and adjustment UX in the field), F8 (sidetone), D3, REQ-candidate SW-KEY-03; `docs/research/keyer-verification-and-key-input-network.md` F7 (iambic golden vectors), F8 (timing tolerance plus or minus 1 percent or plus or minus 0.5 ms, whichever larger; simulated-clock harness), F11 (at 50 WPM the 24 ms dit is 2.8 times the 8.5 ms full ramp; rise plus fall occupy 42 percent of a dit at the 10-to-90 points; hang 8 dits is 192 ms at 50 WPM and 1920 ms at 5 WPM), F14, implication 1 (SW-KEY-02 revised), D-KN10 (default 15 WPM); `docs/research/regulatory-corpus-and-operators.md` F6, F7 (50 WPM is the worst case for necessary and 26 dB bandwidth); `docs/research/tr-switch-candidates.md` F4 (listening window and lead-in versus speed); `docs/research/part97-regulatory-basis.md` F10 (automatic identification at most 20 WPM)
- Guidance consulted: 47 CFR 97.119(b)(1) (eCFR 2026-09-23); SE HB App. C; SE HB §6.8
- Assumptions the decision rests on, and how and by when each is confirmed:
  1. TIMER0 alarms keep element timing within REQ-SYS-042 at the keyer test point under display and encoder load. Confirmed by REQ-SW-KEYER-014, Bench on the dev board (credit false) before PDR and on the delivered unit after TRR.
  2. The 15 WPM default suits the population. Confirmed by package decision 45 at SRR.

## 2. Decision

The built-in keyer sends at any speed from 5 to 50 WPM in 1 WPM steps on the PARIS standard (dit = 1200 ms divided by WPM, dah = 3 dits, intra-character space 1 dit, inter-character 3 dits, inter-word 7 dits), default 15 WPM at first boot, stored in non-volatile memory, adjustable while sending, with the current speed visible on the display while adjusting. Element and space timing at the engine output is accurate to plus or minus 1 percent of nominal or plus or minus 0.5 ms, whichever is larger, across the range (proposed tolerance, from the reconciled keyer study); paddle-to-element latency is at most 3 ms (proposed). Consequences fixed by the top speed: the envelope's configurable 10-to-90 time never exceeds 8 ms (full transition 13.6 ms, still under a 24 ms dit); the semi break-in hang of 8 dits spans 192 ms at 50 WPM to 1920 ms at 5 WPM; the first-element lead-in of at most 12 ms is hidden in the element pipeline for paddles. Any automatic identification memory sends at not more than 20 WPM regardless of the keyer speed (97.119(b)(1)).

## 3. Alternatives considered

| Option | Description | Why not chosen (or why chosen) |
|---|---|---|
| A (chosen) | 5 to 50 WPM, default 15 | Owner acceptance (SI-033); covers every operator in the population; 50 WPM leaves the 8 ms maximum envelope under half a dit |
| B | 5 to 40 WPM | Rejected: the owner accepted 50 |
| C | 5 to 60 WPM | Rejected: a 20 ms dit at 60 WPM would make the 8 ms envelope 40 percent of the dit at 10-to-90 and squeeze the relay lead-in; contest speeds are not the use case |
| D | Speed 0 or a TUNE action for a straight carrier | Not an alternative but a companion: a tune carrier at 0.5 W with a 10 s timeout is a separate requirement proposal (research), not decided here |

No trade study: the owner set the range; the tolerance and latency values are class 2 proposals.

## 4. Consequences

### 4.1 Requirements created or changed

| Requirement | Relationship | Note |
|---|---|---|
| REQ-SYS-041 (keyer speed range), REQ-SW-KEYER-015 (keyer speed setting range) | allocated; both cite this ADR | Demonstration |
| REQ-SYS-015 (occupied bandwidth, TBR), REQ-TX-006 (keying sideband level, TBR) | allocated; both cite this ADR; hazard HZ-008 | 50 WPM is the bandwidth worst case |
| REQ-SYS-042 (element and space timing accuracy at the keyer test point, TBR: plus or minus 1 percent or 0.5 ms), REQ-SW-KEYER-013 and REQ-SW-KEYER-014 (cite this ADR: plus or minus 0.5 percent or 0.2 ms, the firmware allocation), REQ-SYS-043 and REQ-SW-KEYER-017 (latency, TBR) | allocated | The L2 value is a margin allocation below the L1 value (INSP-011 F-04, dispute accepted); HostUnit with the F7 vectors at 0.1 ms; Bench logic capture at 5, 15, 25, 50 WPM |
| REQ-SYS-135 (settings persistence), REQ-SYS-136 (configuration defaults, TBR), REQ-SW-KEYER-016 (speed change at the element boundary), REQ-SW-KEYER-037 (out-of-range keyer setting commands) | allocated; REQ-SW-KEYER-016 and REQ-SW-KEYER-037 cite this ADR | Default 15 WPM, 1 WPM steps, non-volatile, adjustable while sending; Demonstration |
| Automatic identification at most 20 WPM | not created: rev A has no automatic identification memory; REQ-SYS-068 (identification reminder, TBR) |  |

### 4.2 Interfaces, design and code

- ICDs affected: none
- Design elements created or changed: `SW-KEYER` timing engine driven from TIMER0 alarms (rustos WP for timer and alarms, ADR-019); UI speed control (press-and-turn or menu, PDR UX item)
- New `SW-<SUB>` modules created by this ADR: none (`SW-KEYER` exists from SRR, ADR-009)
- ICDs created by this ADR: none

### 4.3 Verification and safety

- Verification cases to add or change: TC-SW-KEYER-NNN (timing at 5, 15, 25, 50 WPM, HostUnit), TC-SW-KEYER-NNN (speed change while sending does not truncate the element in progress, HostUnit), TC-SYS-NNN (Bench logic capture of a PARIS string at four speeds with a second Pico 2 running a capture firmware, proposed)
- Evidence class implications: HostUnit primary (simulated clock); Bench confirms on hardware; the paddle watchdog (128 identical elements or 30 s) is tested at both ends of the range
- Hazard analysis update required: yes (HZ-008 control K4 sets the 26 dB bandwidth at 50 WPM; the HZ-004 controls already reference element counts)
- Safety-critical software scope changed: no

### 4.4 Cost, schedule, risk

- Cost: none
- Gate affected: SRR (L1), PDR (`SW-KEYER` requirements)
- Risks opened, closed or re-scored: RSK-012 (keying wrong or unusable) unchanged; the 50 WPM worst case is already used in the bandwidth analysis
- TPMs affected: TPM-013 (element timing accuracy over 5 to 50 WPM)

## 5. Compliance and tailoring

none

## 6. Decision record

> Owner (2026-09-25, SI-033, first sentence): "Keyer speed range 5 to 50 WPM accepted."

Transcribed from chat into `stakeholder-inputs.md`. The default of 15 WPM and the timing tolerance are Claude's proposals from the reconciled keyer study, confirmed at SRR.

## 7. Related

- Supersedes: none
- Superseded by: none
- Trade study: none
- Review where presented: SRR
- Revisit conditions: the owner asks for 60 WPM (then the envelope maximum and relay lead-in are re-derived by a superseding ADR); the HITL session moves the default speed

## 8. Change log

- 2026-09-26: one-time pre-baseline correction under INSP-011 ruling R-1 option (A), as directed by the lead SE: Decision class row and section 1 Assumptions line added (F-01); hazard line and "Hazard analysis update required" re-derived against `docs/safety/hazards.json` 0.4.0-pha (F-02); section 4.1 placeholder ids replaced by the ids the requirement authors allocated, or marked not created with the reason (F-03). Content from `reconciliation-srr.md` sections 2, 3, 5.1 and 6, re-checked against the requirement, hazard and expectation files of 2026-09-26; that register is superseded by this file for this ADR. The decision of section 2 is unchanged. Minor findings are liens, fixed before PDR: the reference-point wording of section 2 (erratum E-10, the F-04 sub-item disputed and accepted). The edit of an Accepted ADR rests on the owner's approval of R-1 (A) in the SRR decision memo and the matching sentence in `docs/process/05-configuration-and-data-management.md` Table 4-1 row 13 (both pending). Class 1 choices without a trade study wait on ruling R-2 (owner). Author: Claude (ADR author invocation).
