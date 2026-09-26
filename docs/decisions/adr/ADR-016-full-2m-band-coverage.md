# ADR-016: Frequency coverage of the full US 2 m band, 144.000 to 148.000 MHz

| Field | Value |
|---|---|
| ID | ADR-016 |
| Status | Accepted |
| Date proposed | 2026-09-25 |
| Date decided | 2026-09-25 |
| Decision authority | Robin (owner; the decision fixes a functional-baseline performance requirement) |
| Author | Claude (technical data manager invocation, 2026-09-25) |
| Independent reviewer | Pending: reviewer agent invocation before SRR (01 section 3.2 row S3; 06 section 14.2) |
| Life-cycle phase | Pre-A / A |
| Baseline affected | baseline/srr (functional baseline, to be tagged at SRR) |
| Change request | none (pre-baseline) |

## 1. Context

47 CFR 97.301(a) gives every US license class from Technician up the whole 144 to 148 MHz band in ITU Region 2, and 97.305 permits CW on all of it; the voluntary ARRL band plan puts CW in 144.00 to 144.10 MHz with 144.200 MHz as the weak-signal calling frequency. A design could lock the transmitter to the CW segment with an expert unlock, or cover the whole band. The owner chose full coverage (SI-024). The band edges then interact with the keying bandwidth and the reference tolerance (ADR-023).

- Driving inputs and expectations: SI-024, SI-005 (tune to a frequency and chat), SI-030 (Technician and above: full 2 m privileges), SI-002
- Requirements that constrain the decision: none yet
- Hazards in play: none (out-of-band transmission is a regulatory and mission hazard handled as a requirement, 03 section 4.2)
- Research consulted: `docs/research/part97-regulatory-basis.md` F1 (97.305: CW permitted on the entire band; 144.000 to 144.100 MHz CW-only), F4 (97.301(a), 97.303: no US 2 m sharing constraint), F5 (ARRL plan: voluntary, 144.000 to 144.100 CW, 144.200 calling, EME at the bottom), F11 (band edges and keying bandwidth), REQ-candidates RF-01, RF-02, OPS-01, DECISION-3, RISK RF-3; `docs/research/regulatory-corpus-and-operators.md` F8 (1 kHz guard: carrier 144.001 to 147.999 MHz)
- Guidance consulted: 47 CFR 97.301(a), 97.305, 97.307(b) (eCFR 2026-09-23); SE HB §6.8

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
| REQ-SYS-NNN (frequency coverage 144.000 to 148.000 MHz receive; transmit carrier 144.001 to 147.999 MHz; L1 author allocates) | new, traces to SI-024, this ADR and ADR-023 supporting | Guard value carries a `tbr` until ADR-023 is decided |
| REQ-SW-NNN (transmit inhibit outside the carrier range enforced independently of display logic; candidate RF-01) | new, mission-critical; SWE-134 scoping candidate | HostUnit boundary tests at 143.999 and 148.001 MHz; Bench with the tinySA |
| REQ-SW-NNN (presets and CW-segment indication; candidate OPS-01) | new, proposed | Inspection, Demonstration |

### 4.2 Interfaces, design and code

- ICDs affected: none
- Design elements created or changed: frequency plan data (band edges, guard, presets) in `cwht-core`; synthesizer configuration range
- New `SW-<SUB>` modules created by this ADR: none
- ICDs created by this ADR: none

### 4.3 Verification and safety

- Verification cases to add or change: TC-SYS-NNN (tuning range, Bench), TC-SW-NNN (carrier limit enforcement, HostUnit), TC-TX-NNN (band-edge emission stays inside the band, Bench with the tinySA at narrow RBW plus Analysis of the keying spectrum)
- Evidence class implications: the band-edge check depends on the tinySA RBW (ACTION-9 of the corpus report, Low confidence that a 100 Hz class RBW exists); Analysis covers the keying spectrum
- Hazard analysis update required: no
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
