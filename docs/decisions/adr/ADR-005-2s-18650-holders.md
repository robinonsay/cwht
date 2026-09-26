# ADR-005: Two 18650 Li-ion cells in series in user-replaceable holders

| Field | Value |
|---|---|
| ID | ADR-005 |
| Status | Accepted |
| Date proposed | 2026-09-25 |
| Date decided | 2026-09-25 |
| Decision authority | Robin (owner; the decision fixes the power source of the functional baseline) |
| Author | Claude (technical data manager invocation, 2026-09-25) |
| Independent reviewer | Pending: reviewer agent invocation before SRR (01 section 3.2 row S3; 06 section 14.2) |
| Life-cycle phase | Pre-A / A |
| Baseline affected | baseline/srr (functional baseline, to be tagged at SRR) |
| Change request | none (pre-baseline) |

## 1. Context

A 5 W VHF PA at 55 to 65 percent efficiency draws about 1.6 to 2.2 A during key-down; the 7.2 V discrete PA device class (ADR-012 candidates) wants a 6 to 8.4 V drain supply. The owner chose two 18650 cells in series in a holder so cells are user-replaceable (SI-023). The choice fixes the PA supply window (6.0 to 8.4 V), the charger topology (boost from 5 V USB, ADR-004), the protection circuit, the enclosure volume and mass, and the battery-life budget (ADR-020).

- Driving inputs and expectations: SI-023, SI-022 (charge from USB), SI-034 (8 h at 1:9), SI-001 (pocket), SI-019 (units in friends' hands: replaceable cells matter)
- Requirements that constrain the decision: none yet
- Hazards in play: HZ-002 (Li-ion charging and thermal event)
- Research consulted: `docs/research/power-tree-and-charging.md` F3 (charge rates: 500 mA USB gives about 280 mA, about 10 h), F5 to F7 (BQ25887 candidate: 2S boost charger with balancing and ADC), F11 (S-8252 plus dual N-FET protection, BQ29209 second OV layer), F13 (Keystone 1043P single-cell THT holder in stock; two give the four terminals a mid-tap needs; dual holders unverified), F23 (battery-life table: 9.5 h expected at 1:9), section I (safety provisions); `docs/research/pa-device-candidates.md` F18 (2.4 to 3.2 dB output spread across 6.0 to 8.4 V; ALC needed), F19 (11.4 W DC at 5 W; about 1.5 h continuous key-down)
- Guidance consulted: SWE-134 (charging supervision is safety-critical software, 03 section 4.3); SE HB §6.8

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
| REQ-SYS-NNN (power source constraint: two user-replaceable 18650 cells in series; L1 author allocates) | new, constraint traced to SI-023 | |
| REQ-PWR-NNN (charge profile, balancing, protection thresholds, temperature window; candidates PWR-CHG-01, PWR-CHG-02, PWR-PROT-*) | new at PDR, parent the L1 power requirement, hazard HZ-002 | Values from `power-tree-and-charging.md` implications |
| REQ-SYS-NNN (operating supply 6.0 to 8.4 V; output holds 5.0 W above 6.4 V) | new | Ties to ADR-003 tolerance TBR |

### 4.2 Interfaces, design and code

- ICDs affected: `ICD-PWR-CELL` (external stub before SRR: cell format, polarity, holder terminals, mid-tap)
- Design elements created or changed: power tree (charger, protector, buck, LDO, PA rail switch); enclosure cavity for two 77 x 20.65 x 14.86 mm holders (about 41 x 77 mm footprint)
- New `SW-<SUB>` modules created by this ADR: none (charging supervision is named by the architecture ADR)
- ICDs created by this ADR: none

### 4.3 Verification and safety

- Verification cases to add or change: TC-PWR-NNN (charge profile with dummy cells and a bench supply; balancing with two cells set 300 mV apart; protector trip points), TC-VAL-NNN (battery-life run, ADR-020)
- Evidence class implications: Bench (bench supply, multimeter) suffices; no oscilloscope needed for CC-CV
- Hazard analysis update required: yes (HZ-002 controls: charger limits, protector, secondary OV, firmware supervision)
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
