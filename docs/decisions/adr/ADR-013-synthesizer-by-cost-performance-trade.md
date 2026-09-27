# ADR-013: Synthesizer selected by a cost and performance trade study at PDR

| Field | Value |
|---|---|
| ID | ADR-013 |
| Status | Accepted |
| Date proposed | 2026-09-25 |
| Date decided | 2026-09-25 |
| Decision class | 1 (`docs/process/06-risk-and-decision-analysis.md` section 14.1 items (b) synthesizer; (c) HZ-008 causes C7 and C8 and the `SW-SYNTH` component of 07 section 14.1). Owner-directed method (SI-029). Trade study: the synthesizer and reference trade study (not yet created; it takes the next free TS number when created, because the label TS-002 in `docs/design/concept.md` section 11.2 now belongs to the firmware make/buy study) |
| Decision authority | Robin (owner; the decision fixes the decision rule for a critical part) |
| Author | Claude (technical data manager invocation, 2026-09-25) |
| Independent reviewer | INSP-011 (`docs/reviews/SRR/checklists/adrs-001-to-025.md`): iterations 1 to 3 (2026-09-25 and 2026-09-26) and the post-SRR-ruling deltas 1 and 2 (2026-09-26); verdict APPROVED with liens at delta 2. The liens against this file are fixed by the 2026-09-27 errata of section 8, verified at the next INSP-011 delta iteration. That record, not this row, carries every later result |
| Life-cycle phase | Pre-A / A |
| Baseline affected | none until PDR (the TS outcome enters the allocated baseline) |
| Change request | none |

## 1. Context

Four synthesizer families can generate a 144 MHz-class LO: the Si5351A (about USD 1 to 2, 24 mA, but at 144 MHz its output divider is only 6 and reported phase noise is about -110 to -115 dBc/Hz at 10 kHz), the LMX2571 (USD 9 to 14, 39 mA, about -133 dBc/Hz derived), the ADF4351 and MAX2871 (USD 14 to 25, 120 to 170 mA). Phase noise bounds reciprocal mixing and receiver dynamic range; current draw drives battery life (ADR-020). The owner directed a cost and performance trade and gave the decision rule: if costs are similar, choose the best-performing synthesizer for this application (SI-029).

- Driving inputs and expectations: SI-029, SI-004 (narrow CW), SI-034 (battery life), SI-002 (70 cm-ready enhancing criterion, ADR-002), SI-028 (turnkey stock)
- Requirements that constrain the decision: none yet; TPM-006 (frequency stability) and TPM-008 (battery life) are the measures the trade must respect
- Hazards in play (`docs/safety/hazards.json` 0.5.0-pha): HZ-008 (causes C7 and C8: a frequency-control software fault, or the synthesizer unlocked or locked to a wrong value; REQ-SYS-154 and REQ-SYS-182, control K7)
- Research consulted: `docs/research/2m-cw-transceiver-reference-designs.md` F16, F17 (Si5351A data and VHF phase-noise reports), F18 (ADF4351), F19 (MAX2871, datasheet not read), F20 (LMX2571: best fit on paper), F21 (reference oscillators), Table 2 (comparison), implication 14, risk 9, action 20; `docs/research/cw-selectivity-options.md` implications 12 to 14 (IF kept as a synthesizer parameter; two selectivity candidates); `docs/research/power-tree-and-charging.md` F23 (LO current 30, 39 or 120 to 170 mA moves battery life from 13.0 to 9.5 to 6.4 h at 1:9); `docs/research/regulatory-corpus-and-operators.md` F8 (reference tolerance sets the band-edge guard, ADR-023)
- Guidance consulted: 06 section 14.1 class 1 (b) (synthesizer is a critical part: formal trade study), 14.3 to 14.5 (criteria, weights, uncertainty, recommendation); SE HB §6.8.1.2.1 to §6.8.1.2.5; SE HB Table 6.8-1
- Assumptions the decision rests on, and how and by when each is confirmed:
  1. "Similar cost" means within USD 15 per unit. Confirmed by the owner at SRR (README open item 3).
  2. The Low-confidence VHF phase-noise figures are resolved before scoring. Confirmed by reading the datasheet plots (action 20) before the trade study is scored at PDR.

## 2. Decision

The synthesizer is chosen by the synthesizer and reference trade study (not yet created; it takes the next free TS number when created, because the label TS-002 in `docs/design/concept.md` section 11.2 now belongs to the firmware make/buy study) before PDR, following 06 section 14.3, with the owner's rule written into the decision method: mandatory criteria first (LO coverage for the receiver architecture selected in the companion architecture trade, including 144.000 to 148.000 MHz with the BFO offset; turnkey stock at CDR per ADR-012; supply from the 3.3 V or 5 V rail; accepts the TCXO reference of ADR-023), then a cost band test: if the unit costs of the surviving candidates at the build quantity lie within a band the owner sets (proposed USD 15 per unit, TBR at SRR), the best-performing candidate on the weighted performance criteria wins regardless of cost; otherwise the full weighted matrix including cost decides. Performance criteria: phase noise at 10 kHz offset at the LO frequency, spurious output, current draw against TPM-008, frequency step and lock time for the tuning UX, and 70 cm LO coverage as an enhancing criterion (ADR-002). Candidates: Si5351A-B, LMX2571, ADF4351, MAX2871; a fixed overtone LO with a tunable IF is evaluated inside the receiver architecture trade, not here. Every score cell carries linked evidence and a confidence; the LMX2571 and Si5351 VHF phase-noise figures are Low confidence until measured or datasheet plots are read (action 20).

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
| REQ-RX and REQ-TX (LO phase noise, spurious, current; values from the trade study outcome) | not created: after the synthesizer and reference trade study at PDR; the L1 requirements REQ-SYS-024 (receive passband width, TBR) and REQ-SYS-031 (reciprocal mixing dynamic range, TBR) cite this ADR | The trade study produces exactly one ADR (06 section 14.2); expectation CON-028 names this ADR |
| REQ-SYS-010 (carrier frequency accuracy, TBR) | allocated; cites ADR-023 | TPM-006 provisional plus or minus 1 ppm |

### 4.2 Interfaces, design and code

- ICDs affected: none until the TS names the bus (I2C or SPI) and control register map
- Design elements created or changed: synthesizer block, reference oscillator (ADR-023), LO filtering
- New `SW-<SUB>` modules created by this ADR: none (a synthesizer driver module follows the TS)
- ICDs created by this ADR: none

### 4.3 Verification and safety

- Verification cases to add or change: selectivity TC-SYS-018 and reciprocal-mixing dynamic range TC-SYS-019 (Simulation, REQ-SYS-024 and REQ-SYS-031); carrier frequency error TC-SYS-009 (Simulation, REQ-SYS-010); the RX L2 phase-noise proxy case (Bench with the tinySA where its dynamic range allows, otherwise Analysis from datasheet plots) and a Bench frequency check against a known reference are allocated with the RX and TX L2 requirements and the synthesizer trade study at PDR (no id yet)
- Evidence class implications: phase noise cannot be measured on the owner's bench; the TS scores it by datasheet and report evidence with confidence marks
- Hazard analysis update required: yes, at the trade study outcome (HZ-008 cause C8 is re-assessed for the chosen part)
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
- Trade study: the synthesizer and reference trade study (not yet created; it takes the next free TS number when created, because the label TS-002 in `docs/design/concept.md` section 11.2 now belongs to the firmware make/buy study), created before PDR; coupled with TS-001 (receiver architecture) and the reference oscillator decision (ADR-023)
- Review where presented: SRR (method); PDR (outcome)
- Revisit conditions: 06 section 14.6 (a register trigger names it, a CR changes a criterion, new information moves a Low-confidence score by two levels, or the owner asks)

## 8. Change log

- 2026-09-26: one-time pre-baseline correction under INSP-011 ruling R-1 option (A), as directed by the lead SE: Decision class row and section 1 Assumptions line added (F-01); hazard line and "Hazard analysis update required" re-derived against `docs/safety/hazards.json` 0.4.0-pha (F-02); section 4.1 placeholder ids replaced by the ids the requirement authors allocated, or marked not created with the reason (F-03); trade study references resolved to the named, not yet created synthesizer and reference trade study (F-03, erratum E-9); in section 2 only the placeholder trade study id was replaced by the study's name. Content from `reconciliation-srr.md` sections 2, 3, 5.1 and 6, re-checked against the requirement, hazard and expectation files of 2026-09-26; that register is superseded by this file for this ADR. The decision of section 2 is unchanged. Minor findings are liens, fixed before PDR: none against this file. The edit of an Accepted ADR rests on the owner's approval of R-1 (A) in the SRR decision memo and the matching sentence in `docs/process/05-configuration-and-data-management.md` Table 4-1 row 13 (both pending). Class 1 choices without a trade study wait on ruling R-2 (owner). Author: Claude (ADR author invocation).
- 2026-09-27 (PDR errata, WP-PDR-14; SRR liens L-6 and, where named, L-4 and L-7): Independent reviewer row names the INSP-011 results through the post-SRR-ruling delta 2 and points to the record for later results, replacing "verification pending at INSP-011 iteration 3" (F-13); hazard line stamp 0.4.0-pha changed to 0.5.0-pha, the version at HEAD, after re-checking the line against it (F-13; for ADR-015, 022, 023 and 026 also SRR lien L-7); section 4.3 placeholders replaced by TC-SYS-009, 018 and 019, the L2 cases stated as allocated at PDR (F-14). The 2026-09-26 correction also replaced the placeholder trade study id in section 2 by the study's name (disclosed in the first entry above); no decision content changed, and the owner's approval of SRR decision 105 covers it ("F-12 is noted with this decision", `docs/reviews/SRR/decision-memo.md` section 8, decision 105). This is the one exception to "decision sections unchanged" that the README now states (F-12). Route: the SRR decision memo carries these findings as liens to be fixed in the product before the PDR readiness declaration (RFA-SRR-006: "Fix each finding in its product"); they are applied by the ADR correction route the owner approved as SRR decision 105 (corrections outside section 2, each logged in this section), as the README paragraph "PDR errata" records. The decision of section 2 is unchanged. The first entry's "(both pending)" no longer holds: SRR decision 105 approved R-1 option (A) on 2026-09-26 and the 05 Table 4-1 row 13 sentence is in place (INSP-011 F-13). Author: Claude (ADR author invocation, WP-PDR-14).
