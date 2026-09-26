# ADR-005: Two 18650 Li-ion cells in series in user-replaceable holders

| Field | Value |
|---|---|
| ID | ADR-005 |
| Status | Accepted |
| Date proposed | 2026-09-25 |
| Date decided | 2026-09-25 |
| Decision class | 1 (`docs/process/06-risk-and-decision-analysis.md` section 14.1 items (a) power architecture; (b) battery cell and charger; (c) HZ-002, HZ-007, HZ-011). Owner-directed for the cell format (SI-023). Trade study: the power tree parts study at PDR (README "Decisions expected at PDR") for the charger, protector and holders. No trade study for the cell format: this ADR alone records it only if the owner adopts ruling R-2 item (i) of `reconciliation-srr.md` section 7 (open; the owner's ruling); otherwise a trade study is opened, or a waiver of 06 section 14.1 is recorded, before `baseline/srr` |
| Decision authority | Robin (owner; the decision fixes the power source of the functional baseline) |
| Author | Claude (technical data manager invocation, 2026-09-25) |
| Independent reviewer | INSP-011 (`docs/reviews/SRR/checklists/adrs-001-to-025.md`): iterations 1 and 2 (2026-09-25) NEEDS CHANGES, findings F-01, F-02, F-03 and F-07 against this file; the Major-finding corrections are applied here on 2026-09-26 (section 8); verification pending at INSP-011 iteration 3 |
| Life-cycle phase | Pre-A / A |
| Baseline affected | baseline/srr (functional baseline, to be tagged at SRR) |
| Change request | none (pre-baseline) |

## 1. Context

A 5 W VHF PA at 55 to 65 percent efficiency draws about 1.6 to 2.2 A during key-down; the 7.2 V discrete PA device class (ADR-012 candidates) wants a 6 to 8.4 V drain supply. The owner chose two 18650 cells in series in a holder so cells are user-replaceable (SI-023). The choice fixes the PA supply window (6.0 to 8.4 V), the charger topology (boost from 5 V USB, ADR-004), the protection circuit, the enclosure volume and mass, and the battery-life budget (ADR-020).

- Driving inputs and expectations: SI-023, SI-022 (charge from USB), SI-034 (8 h at 1:9), SI-001 (pocket), SI-019 (units in friends' hands: replaceable cells matter)
- Requirements that constrain the decision: none yet
- Hazards in play (`docs/safety/hazards.json` 0.4.0-pha): HZ-002 (Li-ion charging and thermal event), HZ-007 (discharge-side faults: protector, fuse, reverse insertion, holders; REQ-SYS-084 to REQ-SYS-087, REQ-SYS-166) and HZ-011 (charging paused while receiving, control K2, REQ-SYS-093)
- Research consulted: `docs/research/power-tree-and-charging.md` F3 (charge rates: 500 mA USB gives about 280 mA, about 10 h), F5 to F7 (BQ25887 candidate: 2S boost charger with balancing and ADC), F11 (S-8252 plus dual N-FET protection, BQ29209 second OV layer), F13 (Keystone 1043P single-cell THT holder in stock; two give the four terminals a mid-tap needs; dual holders unverified), F23 (battery-life table: 9.5 h expected at 1:9), section I (safety provisions); `docs/research/pa-device-candidates.md` F18 (2.4 to 3.2 dB output spread across 6.0 to 8.4 V; ALC needed), F19 (11.4 W DC at 5 W; about 1.5 h continuous key-down)
- Guidance consulted: SWE-134 (charging supervision is safety-critical software, 03 section 4.3); SE HB §6.8
- Assumptions the decision rests on, and how and by when each is confirmed:
  1. Two single-cell holders fit the pocket envelope. Confirmed by a printed fit check before CDR (REQ-SYS-103).
  2. Unprotected 18650 cells with on-board protection meet the HZ-002 and HZ-007 controls. Confirmed by the power tree parts study at PDR.
  3. 3000 mAh class cells give 90 percent usable capacity (Low confidence, ADR-020). Confirmed by the discharge curve digitised at PDR.

## 2. Decision

The power source is two 18650 Li-ion cells in series (2S, 6.0 to 8.4 V, nominal 7.2 V) in two single-cell through-hole holders (Keystone 1043P class, proposed part) so that the pack exposes four terminals for a mid-tap, per-cell sensing and charge balancing. Cells are user-replaceable unprotected high-drain cells (Samsung INR18650-30Q class, proposed); protection is on the board: a 2S protector (ABLIC S-8252 class with dual N-FET, proposed) plus an independent secondary over-voltage protector (BQ29209 class, proposed). The PA is fed from the protected pack directly with ALC (ADR-003); a 5 V synchronous buck feeds VSYS and a low-noise LDO the 3.3 V analog rail (proposed power tree). Charging is a 2S CC-CV boost charger from the USB input (BQ25887 class, proposed, ADR-004) with JEITA temperature windows, balancing and a safety timer. A mechanical power switch isolates the buck enable and PA rail; charger and protector stay live (about 25 uA). Part selections marked proposed are decided by the power trade study at PDR (06 section 14.1 class 1 (b): battery cell and charger).

## 3. Alternatives considered

| Option | Description | Why not chosen (or why chosen) |
|---|---|---|
| A (chosen) | 2S 18650 in two single-cell holders, board protection, boost charging from USB | Owner direction (SI-023); matches the 7.2 V PA device class; four terminals for balancing |
| B | 1S 18650 with a boost converter for the PA | Rejected: 12 W at 3.0 to 4.2 V means 3 to 4 A input, a switching converter next to the receiver, and efficiency loss |
| C | Soldered pouch or hard pack with built-in protection | Rejected by SI-023 (user-replaceable) |
| D | 3S | Rejected: 12.6 V exceeds the 7.2 V PA device class; boost from 5 V USB to 12.6 V at useful current is impractical |
| E | One dual 18650 holder | Deferred: terminal count unverified (F13, Low confidence); two singles guarantee the mid-tap |

No trade study for the cell format (owner direction); the charger, protector and holder part numbers go through the power TS at PDR.

## 4. Consequences

### 4.1 Requirements created or changed

| Requirement | Relationship | Note |
|---|---|---|
| REQ-SYS-080 (two 18650 cells in holders) | allocated; cites this ADR |  |
| REQ-PWR (charge profile, balancing, protection thresholds, temperature window; candidates PWR-CHG-01, PWR-CHG-02, PWR-PROT-*) | not created at L2: the PWR file is due at PDR; the L1 counterparts are REQ-SYS-081 to REQ-SYS-089, REQ-SYS-166 and REQ-SYS-167 (hazards HZ-002, HZ-007) | Values from `power-tree-and-charging.md` implications |
| REQ-SYS-012 (5 W from 6.4 to 8.4 V, TBR), REQ-SYS-097 (low-battery transmit inhibit, TBR), REQ-SYS-098 (low-battery power-down, TBR) | allocated; none cites this ADR | No single supply-window requirement (6.0 to 8.4 V) was created; ties to the ADR-003 tolerance TBR |

### 4.2 Interfaces, design and code

- ICDs affected: `ICD-PWR-CELL` (external stub before SRR: cell format, polarity, holder terminals, mid-tap)
- Design elements created or changed: power tree (charger, protector, buck, LDO, PA rail switch); enclosure cavity for two 77 x 20.65 x 14.86 mm holders (about 41 x 77 mm footprint)
- New `SW-<SUB>` modules created by this ADR: none (charging supervision is named by the architecture ADR)
- ICDs created by this ADR: none

### 4.3 Verification and safety

- Verification cases to add or change: TC-PWR-NNN (charge profile with dummy cells and a bench supply; balancing with two cells set 300 mV apart; protector trip points), TC-VAL-NNN (battery-life run, ADR-020)
- Evidence class implications: Bench (bench supply, multimeter) suffices; no oscilloscope needed for CC-CV
- Hazard analysis update required: yes (HZ-002 controls: charger limits, protector, secondary OV, firmware supervision; HZ-007 controls K1 to K5; HZ-011 control K2)
- Safety-critical software scope changed: no (charging supervision already in scope)

### 4.4 Cost, schedule, risk

- BOM impact: two holders about USD 3 each, charger about USD 3 to 5, protector and FETs, secondary OV about USD 1; cells bought by the owner
- Gate affected: PDR (power TS)
- Risks opened, closed or re-scored: RSK-007 (cell thermal event inside the enclosure) stays open; mitigations are the protector layers and JEITA windows
- TPMs affected: TPM-001 (mass: two cells about 96 g plus holders), TPM-002 (power margin), TPM-008 (battery life)

## 5. Compliance and tailoring

none

## 6. Decision record

> Owner (2026-09-25, SI-023): "Battery: two 18650 Li-ion cells (2S) in a holder so cells are user-replaceable."

Transcribed from chat into `stakeholder-inputs.md`.

## 7. Related

- Supersedes: none
- Superseded by: none
- Trade study: power tree, charger and protection TS at PDR (part selections)
- Review where presented: SRR
- Revisit conditions: the enclosure envelope cannot hold two holders side by side at the pocket size (then a dual holder with verified terminals, same ADR intent); the PA trade selects a device outside the 6 to 8.4 V class

## 8. Change log

- 2026-09-26: one-time pre-baseline correction under INSP-011 ruling R-1 option (A), as directed by the lead SE: Decision class row and section 1 Assumptions line added (F-01); hazard line and "Hazard analysis update required" re-derived against `docs/safety/hazards.json` 0.4.0-pha (F-02); section 4.1 placeholder ids replaced by the ids the requirement authors allocated, or marked not created with the reason (F-03). Content from `reconciliation-srr.md` sections 2, 3, 5.1 and 6, re-checked against the requirement, hazard and expectation files of 2026-09-26; that register is superseded by this file for this ADR. The decision of section 2 is unchanged. Minor findings are liens, fixed before PDR: F-07 (erratum E-4, the key-down current of section 1). The edit of an Accepted ADR rests on the owner's approval of R-1 (A) in the SRR decision memo and the matching sentence in `docs/process/05-configuration-and-data-management.md` Table 4-1 row 13 (both pending). Class 1 choices without a trade study wait on ruling R-2 (owner). Author: Claude (ADR author invocation).
