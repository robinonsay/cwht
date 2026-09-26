# ADR-020: Battery-life target of 8 hours at a 1:9 transmit-to-receive ratio

| Field | Value |
|---|---|
| ID | ADR-020 |
| Status | Accepted |
| Date proposed | 2026-09-25 |
| Date decided | 2026-09-25 |
| Decision class | 2 (`docs/process/06-risk-and-decision-analysis.md` section 14.1 class 2: it sets the MOE-004 target before any baseline and decides no hazard control; the low-battery cutoff that ends the run is HZ-007 control K4, used and not changed). Decision authority stays Robin because the decision fixes a measure of effectiveness |
| Decision authority | Robin (owner; the decision fixes a measure of effectiveness and its L1 requirement) |
| Author | Claude (technical data manager invocation, 2026-09-25) |
| Independent reviewer | INSP-011 (`docs/reviews/SRR/checklists/adrs-001-to-025.md`): iterations 1 and 2 (2026-09-25) NEEDS CHANGES, findings F-01 and F-03 against this file; the Major-finding corrections are applied here on 2026-09-26 (section 8); verification pending at INSP-011 iteration 3 |
| Life-cycle phase | Pre-A / A |
| Baseline affected | baseline/srr (functional baseline: MOE and L1) |
| Change request | none (pre-baseline) |

## 1. Context

Battery life decides the receiver current budget, the synthesizer choice, the LNA class and the backlight. The power study modelled three receiver builds on a 3000 mAh 2S pack: low (Si5351, 30 mA LNA, no backlight) 13.0 h at 1:9; expected (LMX2571, 60 mA LNA, 20 mA backlight) 9.5 h; high (ADF4351-class LO, PGA-103+ at 5 V, 40 mA backlight) 6.4 h. The owner accepted the target of 8 h at 1:9 (SI-034). The current TPM-008 definition uses a different duty (3 min transmit at 50 percent key-down per 10 min, that is 3:7) with a provisional 4 h target and must be brought into line.

- Driving inputs and expectations: SI-034 (second sentence), SI-023 (2S 18650), SI-003 (5 W), SI-005, SI-019 (a day of playing radio)
- Requirements that constrain the decision: none yet; TPM-008 and TPM-002 are the measures
- Hazards in play (`docs/safety/hazards.json` 0.4.0-pha): none; HZ-007 control K4 (the low-battery cutoff that ends the run) is used, not changed
- Research consulted: `docs/research/power-tree-and-charging.md` F23 (battery-life model and table; assumptions: 45 percent key-down during transmit, 0.90 buck efficiency, 90 percent usable capacity at Low confidence), F3 (charge time about 10 h at 500 mA), F19 (buck and quiescent currents), implications 10 to 18 (power budget candidates); `docs/research/pa-device-candidates.md` F19 (11.4 W DC at 5 W); `docs/research/rf-exposure-evaluation.md` F7 (the 1:9 figure is the ConOps nominal case, not the exposure compliance case); `docs/research/display-and-ui-parts.md` D-UI-02 (no backlight in build 1)
- Guidance consulted: SE HB §4.1 (MOEs from stakeholder expectations, via 02 section 6); SE HB §6.8
- Assumptions the decision rests on, and how and by when each is confirmed:
  1. 90 percent usable capacity to 3.0 V per cell (Low confidence). Confirmed by the discharge curve digitised at PDR.
  2. 45 percent key-down within transmit periods represents the owner's operating. Confirmed by the owner at SRR (section 6).
  3. The synthesizer and front-end trades keep the expected receiver build. Confirmed by the power budget at PDR with 20 percent margin.

## 2. Decision

The radio operates for at least 8 hours from a full charge to the low-battery cutoff on the duty cycle: 10 percent of the time transmitting (with 45 percent key-down at 5 W within the transmit periods) and 90 percent receiving with the display on and audio at normal headphone level; and for at least 6 hours at a 1:4 ratio (floor, proposed). This is a measure of effectiveness (MOE) and an L1 requirement verified by Analysis at PDR and CDR (TPM-002 mode powers times derated capacity) and by a Bench run at SAR. The target makes the "expected" receiver build the minimum acceptable: an ADF4351-class synthesizer at 120 to 170 mA with a 97 mA LNA and a 40 mA backlight does not meet it, so those choices need compensating savings to survive their trades. No backlight in rev A (ADR-006) and the synthesizer current criterion (ADR-013) follow. TPM-008's definition and planned value are to be changed by the TPM owner to this duty and to 8 h (margin policy unchanged: at least 20 percent above target by analysis at PDR).

## 3. Alternatives considered

| Option | Description | Why not chosen (or why chosen) |
|---|---|---|
| A (chosen) | 8 h at 1:9; 6 h floor at 1:4 | Owner acceptance (SI-034); a full afternoon of operating; leaves the synthesizer trade room for the LMX2571-class device |
| B | 4 h (TPM-008 provisional) | Rejected: a half-day radio; the owner accepted 8 h |
| C | 12 h | Rejected: forces the low build (Si5351-class LO, 30 mA LNA) and removes the synthesizer trade's freedom |
| D | 8 h at 1:4 | Rejected: same effect as C on the budget; 1:4 is kept as a 6 h floor |

No trade study: the owner set the target; the trades that must respect it are the synthesizer and receiver front-end trades at PDR.

## 4. Consequences

### 4.1 Requirements created or changed

| Requirement | Relationship | Note |
|---|---|---|
| MOE-004 (battery life for a day out) | allocated by the L0 author; traces to SI-034 |  |
| REQ-SYS-094 (battery life at 1:9), REQ-SYS-095 (battery life at 1:4, TBR) | allocated; REQ-SYS-094 cites this ADR | Analysis (PDR, CDR), Bench (SAR) |
| REQ-PWR (receive current budget allocation per block; low-battery cutoff) | not created at L2 (the PWR file is due at PDR); L1 counterparts REQ-SYS-097 (low-battery transmit inhibit, TBR) and REQ-SYS-098 (low-battery power-down, TBR) | From the F23 model |

### 4.2 Interfaces, design and code

- ICDs affected: none
- Design elements created or changed: power budget `docs/design/budgets.md`; synthesizer and LNA current as trade criteria; no backlight
- New `SW-<SUB>` modules created by this ADR: none
- ICDs created by this ADR: none

### 4.3 Verification and safety

- Verification cases to add or change: TC-SYS-NNN (battery-life Analysis from the power budget), TC-VAL-NNN (SAR Bench run: full charge to cutoff on a scripted 1:9 duty using the internal keyer memory into the dummy load, witnessed)
- Evidence class implications: the Bench run takes 8 hours or more; it is a validation scenario with the owner present at start and end
- Hazard analysis update required: no
- Safety-critical software scope changed: no

### 4.4 Cost, schedule, risk

- Cost: none in parts; constrains the synthesizer and LNA choices
- Gate affected: PDR (budget), SAR (run)
- Risks opened, closed or re-scored: new risk proposed: "usable capacity assumption (90 percent to 3.0 V per cell) is Low confidence; the 30Q discharge curve was not digitised" (control: digitise the curve at PDR; Bench run at SAR)
- TPMs affected: TPM-008 (definition and target changed to this ADR), TPM-002 (allocations set with the power TS)

## 5. Compliance and tailoring

none

## 6. Decision record

> Owner (2026-09-25, SI-034, second sentence): "Battery-life target accepted: 8 h at a 1:9 transmit-to-receive ratio."

Transcribed from chat into `stakeholder-inputs.md`. The 45 percent key-down assumption within transmit periods and the 6 h floor at 1:4 are Claude's proposals from the power study, confirmed at SRR.

## 7. Related

- Supersedes: none
- Superseded by: none
- Trade study: synthesizer TS (ADR-013) and receiver front-end TS at PDR consume this target as a criterion
- Review where presented: SRR
- Revisit conditions: the PDR budget shows the expected build below 8 h with 20 percent margin (then a receiver current reduction, a backlight removal is already taken, or an owner decision on the target); a cell other than the 3000 mAh class is baselined

## 8. Change log

- 2026-09-26: one-time pre-baseline correction under INSP-011 ruling R-1 option (A), as directed by the lead SE: Decision class row and section 1 Assumptions line added (F-01); hazard line and "Hazard analysis update required" re-derived against `docs/safety/hazards.json` 0.4.0-pha (F-02); section 4.1 placeholder ids replaced by the ids the requirement authors allocated, or marked not created with the reason (F-03). Content from `reconciliation-srr.md` sections 2, 3, 5.1 and 6, re-checked against the requirement, hazard and expectation files of 2026-09-26; that register is superseded by this file for this ADR. The decision of section 2 is unchanged. Minor findings are liens, fixed before PDR: none against this file. The edit of an Accepted ADR rests on the owner's approval of R-1 (A) in the SRR decision memo and the matching sentence in `docs/process/05-configuration-and-data-management.md` Table 4-1 row 13 (both pending). Class 1 choices without a trade study wait on ruling R-2 (owner). Author: Claude (ADR author invocation).
