# ADR-016: Frequency coverage of the full US 2 m band, 144.000 to 148.000 MHz

| Field | Value |
|---|---|
| ID | ADR-016 |
| Status | Accepted |
| Date proposed | 2026-09-25 |
| Date decided | 2026-09-25 |
| Decision class | 1 (`docs/process/06-risk-and-decision-analysis.md` section 14.1 item (c): HZ-008 and the carrier limits of the `SW-SYNTH` component of 07 section 14.1). Owner-directed (SI-024). No trade study for the coverage: this ADR alone records it only if the owner adopts ruling R-2 item (i) of `reconciliation-srr.md` section 7 (open; the owner's ruling); otherwise a trade study is opened, or a waiver of 06 section 14.1 is recorded, before `baseline/srr` |
| Decision authority | Robin (owner; the decision fixes a functional-baseline performance requirement) |
| Author | Claude (technical data manager invocation, 2026-09-25) |
| Independent reviewer | INSP-011 (`docs/reviews/SRR/checklists/adrs-001-to-025.md`): iterations 1 and 2 (2026-09-25) NEEDS CHANGES, findings F-01, F-02 and F-03 against this file; the Major-finding corrections are applied here on 2026-09-26 (section 8); verification pending at INSP-011 iteration 3 |
| Life-cycle phase | Pre-A / A |
| Baseline affected | baseline/srr (functional baseline, to be tagged at SRR) |
| Change request | none (pre-baseline) |

## 1. Context

47 CFR 97.301(a) gives every US license class from Technician up the whole 144 to 148 MHz band in ITU Region 2, and 97.305 permits CW on all of it; the voluntary ARRL band plan puts CW in 144.00 to 144.10 MHz with 144.200 MHz as the weak-signal calling frequency. A design could lock the transmitter to the CW segment with an expert unlock, or cover the whole band. The owner chose full coverage (SI-024). The band edges then interact with the keying bandwidth and the reference tolerance (ADR-023).

- Driving inputs and expectations: SI-024, SI-005 (tune to a frequency and chat), SI-030 (Technician and above: full 2 m privileges), SI-002
- Requirements that constrain the decision: none yet
- Hazards in play (`docs/safety/hazards.json` 0.4.0-pha): HZ-008 (out-of-band emission; REQ-SYS-008 and REQ-TX-002 cite this ADR and carry it; controls K4 and K7 rest on the carrier range)
- Research consulted: `docs/research/part97-regulatory-basis.md` F1 (97.305: CW permitted on the entire band; 144.000 to 144.100 MHz CW-only), F4 (97.301(a), 97.303: no US 2 m sharing constraint), F5 (ARRL plan: voluntary, 144.000 to 144.100 CW, 144.200 calling, EME at the bottom), F11 (band edges and keying bandwidth), REQ-candidates RF-01, RF-02, OPS-01, DECISION-3, RISK RF-3; `docs/research/regulatory-corpus-and-operators.md` F8 (1 kHz guard: carrier 144.001 to 147.999 MHz)
- Guidance consulted: 47 CFR 97.301(a), 97.305, 97.307(b) (eCFR 2026-09-23); SE HB §6.8
- Assumptions the decision rests on, and how and by when each is confirmed:
  1. The synthesizer covers 144.000 to 148.000 MHz plus the BFO offset. Confirmed by the synthesizer and reference trade study at PDR.
  2. The band-edge check closes by tinySA or by Analysis. Confirmed when the tinySA RBW is verified on receipt (ACTION-9).

## 2. Decision

The receiver and transmitter tune continuously across 144.000 to 148.000 MHz. The transmit carrier is confined by firmware to 144.001 to 147.999 MHz (the 1 kHz band-edge guard proposed in ADR-023), enforced independently of the display and tuning logic so that a display fault cannot key outside the band; the receiver may tune to the edges. There is no lock to the band-plan CW segment and no expert unlock. Defaults (proposed, pending SRR): power-on presets in the weak-signal segment (144.100 and 144.200 MHz) and the 144.000 to 144.100 MHz CW-only segment indicated on the display; the handbook explains the voluntary band plan. Tuning step sizes are a UI design item at PDR; the receiver BFO and sidetone offset are adjustable in 10 Hz steps (proposed).

## 3. Alternatives considered

| Option | Description | Why not chosen (or why chosen) |
|---|---|---|
| A (chosen) | Full 144.000 to 148.000 MHz with a 1 kHz transmit guard at each edge | Owner direction (SI-024); lawful for every operator class in the population; a synthesizer covers it trivially |
| B | Lock to 144.000 to 144.300 MHz with an expert unlock | Rejected by the owner; adds UI state and a way to be "locked out" on a hilltop |
| C | CW segment only, 144.000 to 144.100 MHz | Rejected: excludes the 144.200 calling frequency and simplex chat elsewhere in the band |

No trade study: the owner's direction fixed coverage; the presets are class 2 proposals.

## 4. Consequences

### 4.1 Requirements created or changed

| Requirement | Relationship | Note |
|---|---|---|
| REQ-SYS-008 (transmit frequency range with band-edge guard, TBR), REQ-SYS-021 (receive frequency range), REQ-TX-002 (transmit carrier frequency range, TBR) | allocated; all cite this ADR, REQ-SYS-008 and REQ-TX-002 also ADR-023; hazard HZ-008 on REQ-SYS-008 and REQ-TX-002 | Guard value carries a `tbr` until ADR-023 is decided |
| REQ-SYS-009 (transmit inhibit outside the guard, TBR; cites ADR-023), REQ-SYS-182 (independent frequency verification before and during transmit, TBR) | allocated; hazard HZ-008; candidate RF-01 | HostUnit boundary tests at 143.999 and 148.001 MHz; Bench with the tinySA |
| Presets and CW-segment indication (candidate OPS-01) | not created: carried to the PDR UI design | Inspection, Demonstration |

### 4.2 Interfaces, design and code

- ICDs affected: none
- Design elements created or changed: frequency plan data (band edges, guard, presets) in `cwht-core`; synthesizer configuration range
- New `SW-<SUB>` modules created by this ADR: none
- ICDs created by this ADR: none

### 4.3 Verification and safety

- Verification cases to add or change: TC-SYS-NNN (tuning range, Bench), TC-SW-NNN (carrier limit enforcement, HostUnit), TC-TX-NNN (band-edge emission stays inside the band, Bench with the tinySA at narrow RBW plus Analysis of the keying spectrum)
- Evidence class implications: the band-edge check depends on the tinySA RBW (ACTION-9 of the corpus report, Low confidence that a 100 Hz class RBW exists); Analysis covers the keying spectrum
- Hazard analysis update required: yes (HZ-008 controls K4 and K7 rest on the carrier range)
- Safety-critical software scope changed: pending the SWE-134 scoping of the transmit inhibit

### 4.4 Cost, schedule, risk

- Cost: none
- Gate affected: SRR (L1), PDR (frequency plan)
- Risks opened, closed or re-scored: RSK-002 (LO error) relates through the guard; proposed risk "band-edge violation by reference drift" (REG-6) is mitigated by ADR-023
- TPMs affected: TPM-006 (frequency stability)

## 5. Compliance and tailoring

none

## 6. Decision record

> Owner (2026-09-25, SI-024): "Frequency coverage: the full US 2 m band, 144.000 to 148.000 MHz."

Transcribed from chat into `stakeholder-inputs.md`.

## 7. Related

- Supersedes: none
- Superseded by: none
- Trade study: none
- Review where presented: SRR
- Revisit conditions: ADR-023 is rejected in favour of a wider guard (then the carrier range narrows by the same superseding ADR); a regional band plan change (ACTION-4 of the Part 97 report) moves the presets

## 8. Change log

- 2026-09-26: one-time pre-baseline correction under INSP-011 ruling R-1 option (A), as directed by the lead SE: Decision class row and section 1 Assumptions line added (F-01); hazard line and "Hazard analysis update required" re-derived against `docs/safety/hazards.json` 0.4.0-pha (F-02); section 4.1 placeholder ids replaced by the ids the requirement authors allocated, or marked not created with the reason (F-03). Content from `reconciliation-srr.md` sections 2, 3, 5.1 and 6, re-checked against the requirement, hazard and expectation files of 2026-09-26; that register is superseded by this file for this ADR. The decision of section 2 is unchanged. Minor findings are liens, fixed before PDR: none against this file. The edit of an Accepted ADR rests on the owner's approval of R-1 (A) in the SRR decision memo and the matching sentence in `docs/process/05-configuration-and-data-management.md` Table 4-1 row 13 (both pending). Class 1 choices without a trade study wait on ruling R-2 (owner). Author: Claude (ADR author invocation).
