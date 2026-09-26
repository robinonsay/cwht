# ADR-013: Synthesizer selected by a cost and performance trade study at PDR

| Field | Value |
|---|---|
| ID | ADR-013 |
| Status | Accepted |
| Date proposed | 2026-09-25 |
| Date decided | 2026-09-25 |
| Decision authority | Robin (owner; the decision fixes the decision rule for a critical part) |
| Author | Claude (technical data manager invocation, 2026-09-25) |
| Independent reviewer | Pending: reviewer agent invocation before SRR (01 section 3.2 row S3; 06 section 14.2) |
| Life-cycle phase | Pre-A / A |
| Baseline affected | none until PDR (the TS outcome enters the allocated baseline) |
| Change request | none |

## 1. Context

Four synthesizer families can generate a 144 MHz-class LO: the Si5351A (about USD 1 to 2, 24 mA, but at 144 MHz its output divider is only 6 and reported phase noise is about -110 to -115 dBc/Hz at 10 kHz), the LMX2571 (USD 9 to 14, 39 mA, about -133 dBc/Hz derived), the ADF4351 and MAX2871 (USD 14 to 25, 120 to 170 mA). Phase noise bounds reciprocal mixing and receiver dynamic range; current draw drives battery life (ADR-020). The owner directed a cost and performance trade and gave the decision rule: if costs are similar, choose the best-performing synthesizer for this application (SI-029).

- Driving inputs and expectations: SI-029, SI-004 (narrow CW), SI-034 (battery life), SI-002 (70 cm-ready enhancing criterion, ADR-002), SI-028 (turnkey stock)
- Requirements that constrain the decision: none yet; TPM-006 (frequency stability) and TPM-008 (battery life) are the measures the trade must respect
- Hazards in play: none
- Research consulted: `docs/research/2m-cw-transceiver-reference-designs.md` F16, F17 (Si5351A data and VHF phase-noise reports), F18 (ADF4351), F19 (MAX2871, datasheet not read), F20 (LMX2571: best fit on paper), F21 (reference oscillators), Table 2 (comparison), implication 14, risk 9, action 20; `docs/research/cw-selectivity-options.md` implications 12 to 14 (IF kept as a synthesizer parameter; two selectivity candidates); `docs/research/power-tree-and-charging.md` F23 (LO current 30, 39 or 120 to 170 mA moves battery life from 13.0 to 9.5 to 6.4 h at 1:9); `docs/research/regulatory-corpus-and-operators.md` F8 (reference tolerance sets the band-edge guard, ADR-023)
- Guidance consulted: 06 section 14.1 class 1 (b) (synthesizer is a critical part: formal trade study), 14.3 to 14.5 (criteria, weights, uncertainty, recommendation); SE HB §6.8.1.2.1 to §6.8.1.2.5; SE HB Table 6.8-1

## 2. Decision

The synthesizer is chosen by trade study `TS-NNN` before PDR, following 06 section 14.3, with the owner's rule written into the decision method: mandatory criteria first (LO coverage for the receiver architecture selected in the companion architecture trade, including 144.000 to 148.000 MHz with the BFO offset; turnkey stock at CDR per ADR-012; supply from the 3.3 V or 5 V rail; accepts the TCXO reference of ADR-023), then a cost band test: if the unit costs of the surviving candidates at the build quantity lie within a band the owner sets (proposed USD 15 per unit, TBR at SRR), the best-performing candidate on the weighted performance criteria wins regardless of cost; otherwise the full weighted matrix including cost decides. Performance criteria: phase noise at 10 kHz offset at the LO frequency, spurious output, current draw against TPM-008, frequency step and lock time for the tuning UX, and 70 cm LO coverage as an enhancing criterion (ADR-002). Candidates: Si5351A-B, LMX2571, ADF4351, MAX2871; a fixed overtone LO with a tunable IF is evaluated inside the receiver architecture trade, not here. Every score cell carries linked evidence and a confidence; the LMX2571 and Si5351 VHF phase-noise figures are Low confidence until measured or datasheet plots are read (action 20).

## 3. Alternatives considered

| Option | Description | Why not chosen (or why chosen) |
|---|---|---|
| A (chosen) | Formal trade study with the owner's cost-band rule | Owner direction (SI-029); a critical part under 06 section 14.1 must be traded |
| B | Fix Si5351A now | Rejected: about 20 dB worse phase noise at VHF than at HF (F17); square-wave outputs need filtering; the owner asked for the trade |
| C | Fix LMX2571 now | Rejected: best on paper but its closed-loop 144 MHz plots were not read and its clipped-sine reference penalty couples to the TCXO choice |
| D | Decide at CDR | Rejected: the synthesizer sets the receiver architecture, board area and power budget, all PDR products |

## 4. Consequences

### 4.1 Requirements created or changed

| Requirement | Relationship | Note |
|---|---|---|
| REQ-RX-NNN and REQ-TX-NNN (LO phase noise, spurious, current; values from the TS outcome) | new at PDR, self-derived from the TS and its ADR | The TS produces exactly one ADR (06 section 14.2) |
| REQ-SYS-NNN (frequency stability and display accuracy) | value TBR closing at PDR with the TS | TPM-006 provisional plus or minus 1 ppm |

### 4.2 Interfaces, design and code

- ICDs affected: none until the TS names the bus (I2C or SPI) and control register map
- Design elements created or changed: synthesizer block, reference oscillator (ADR-023), LO filtering
- New `SW-<SUB>` modules created by this ADR: none (a synthesizer driver module follows the TS)
- ICDs created by this ADR: none

### 4.3 Verification and safety

- Verification cases to add or change: TC-RX-NNN (reciprocal mixing or phase-noise proxy: Bench with the tinySA where its dynamic range allows, otherwise Analysis from datasheet plots), TC-SYS-NNN (frequency accuracy, Bench against a known reference)
- Evidence class implications: phase noise cannot be measured on the owner's bench; the TS scores it by datasheet and report evidence with confidence marks
- Hazard analysis update required: no
- Safety-critical software scope changed: no

### 4.4 Cost, schedule, risk

- BOM impact: USD 1 to 25 for the device plus USD 1 to 9 for the TCXO grade
- Gate affected: PDR
- Risks opened, closed or re-scored: RSK-002 (LO frequency error exceeds the CW filter half-bandwidth), RSK-005 (single source) are inputs to the TS per 06 section 13
- TPMs affected: TPM-006 (frequency stability), TPM-002 (power margin), TPM-008 (battery life)

## 5. Compliance and tailoring

none

## 6. Decision record

> Owner (2026-09-25, SI-029): "Synthesizer choice: perform a cost and performance trade; if costs are similar, choose the best-performing synthesizer for this application."

Transcribed from chat into `stakeholder-inputs.md`. The USD 15 cost band is Claude's proposal for "similar" and is confirmed or changed by the owner at SRR.

## 7. Related

- Supersedes: none
- Superseded by: none
- Trade study: synthesizer TS-NNN (created before PDR); coupled with the receiver architecture TS and the reference oscillator decision (ADR-023)
- Review where presented: SRR (method); PDR (outcome)
- Revisit conditions: 06 section 14.6 (a register trigger names it, a CR changes a criterion, new information moves a Low-confidence score by two levels, or the owner asks)
