# ADR-022: Harmonic and spurious suppression: 60 dB design target above the 53 dB regulatory floor at 5 W

| Field | Value |
|---|---|
| ID | ADR-022 |
| Status | Proposed, pending owner decision at SRR |
| Date proposed | 2026-09-25 |
| Date decided | pending (SRR) |
| Decision authority | Robin (owner; the decision fixes a regulatory L1 requirement value and drives filter order, PA topology and enclosure partitioning) |
| Author | Claude (technical data manager invocation, 2026-09-25) |
| Independent reviewer | Pending: reviewer agent invocation before SRR (01 section 3.2 row S3; 06 section 14.2) |
| Life-cycle phase | Pre-A / A |
| Baseline affected | baseline/srr (functional baseline: regulatory L1 requirement) |
| Change request | none (pre-baseline) |

## 1. Context

47 CFR 97.307(e) requires, for a transmitter of 25 W or less between 30 and 225 MHz, that each spurious emission supplied to the antenna transmission line not exceed 25 uW and be at least 40 dB below the fundamental. At 5.0 W (37.0 dBm) the 25 uW (-16.0 dBm) cap binds and requires 53.0 dB of suppression; the 40 dB clause is not binding. Vendor harmonic data for candidate PA devices are single-lot or absent; SMD inductor self-resonance and layout leakage erode simulated filter attenuation; the second harmonic falls in a Federal aeronautical band, the third in the 70 cm amateur band shared with Federal radiolocation, and the seventh in the 1030 MHz aeronautical radionavigation band. A design margin policy has to be fixed before the PA and filter trades at PDR (DECISION-4 of the Part 97 report).

- Driving inputs and expectations: SI-014 (Part 97), SI-003 (5 W), SI-010 (proof before power-on), SI-034 (tinySA)
- Requirements that constrain the decision: the 5 W ceiling (ADR-003) and the ALC that holds it across the pack voltage
- Hazards in play: none (interference is a regulatory harm, not a personal-injury hazard)
- Research consulted: `docs/research/part97-regulatory-basis.md` F2 (arithmetic: 53.0 dB at 5 W, 53.8 dB at 6 W, 60 dB at the 25 W tier; measurement point and span; harmonic bands), REQ-candidate RF-04 (60 dB target, spur not above -23 dBm, about 7 dB margin), RISK RF-1, RF-2, DECISION-4; `docs/research/pa-device-candidates.md` F1 (10 uW floor equals 57.0 dBc at 5 W), F16 (harmonic data quality ranking), F17 (required filter attenuation: goals 40 dB at 288 to 296 MHz and 35 dB at 432 to 444 MHz with insertion loss not above 0.5 dB at 148 MHz, including a 5 dB implementation margin; 7th-order Chebyshev or 5th-order elliptic reaches it on paper), F18 (without ALC the cap tightens to 55.9 dBc at 8.4 V), F20 (gate-bias ALC degrades 2fo toward class C, absorbed by the 40 dB goal), implication 2; `docs/research/regulatory-corpus-and-operators.md` F9 (victim services at 2f, 3f, 7f), REQ-candidate RF-10, RISK RF-4, RF-5; `docs/research/tr-switch-candidates.md` TR-05 (LPF at the antenna port after the T/R node); `docs/plan/tpm.json` TPM-007 (margin = achieved dBc minus 53; planned value 10 dB by analysis)
- Guidance consulted: 47 CFR 97.307(c), (e), 97.3(a)(43) (eCFR 2026-09-23); 47 CFR 2.1057(a)(1) (span by analogy); SE HB App. C (quantified with units and tolerance); SE HB §6.8

## 2. Decision (proposed)

The L1 regulatory requirement reads: at every power step and every frequency in 144.000 to 148.000 MHz, each spurious emission delivered to the antenna port is at most 25 uW (-16.0 dBm) and at least 40 dB below the fundamental (47 CFR 97.307(e)); at 5.0 W this is at least 53.0 dB below carrier. The design target, written as a derived L2 transmitter requirement, is at least 60 dB below carrier at 5 W (each spur at most -23 dBm, 5 uW) at every instant of the keying envelope, which gives about 7 dB of margin over the floor and also meets the 60 dB relative clause of the over-25 W tier. The harmonic low-pass filter goals, measured at the assembled filter's own terminals, are at least 40 dB at 288 to 296 MHz and at least 35 dB at 432 to 444 MHz with passband insertion loss at most 0.5 dB at 148 MHz; the filter sits at the antenna port after the T/R node. The ALC holds 5.0 W within plus or minus 0.5 dB above 6.4 V so the absolute cap does not tighten at full charge. The measurement span is 9 kHz to 1.5 GHz with 2f, 3f and 7f reported individually. Verification: Analysis (LTspice behavioural PA harmonics plus S-parameter filter simulation with vendor inductor self-resonance models) at PDR and CDR, then Bench with the tinySA Ultra through a calibrated attenuator into 50 ohms (ADR-021) at TRR and on every unit.

## 3. Alternatives considered

| Option | Description | Why not chosen (or why chosen) |
|---|---|---|
| A (proposed) | 53 dB floor as the regulatory requirement; 60 dBc design target; 40/35 dB filter goals | About 7 dB margin against one-lot vendor data and layout erosion; the target coincides with the higher regulatory tier; achievable with a 7th-order or elliptic filter |
| B | 53 dB minimum only | Rejected: zero margin; a 3 dB layout erosion (RISK RF-1) would fail the ATP |
| C | 57 dBc (the 10 uW "need not be reduced below" floor) | Not chosen: 4 dB margin; no natural filter design point |
| D | 70 dBc | Rejected: 9th-order filter or a shielded cavity, higher insertion loss (each 0.5 dB costs 11 percent of 5 W), no regulatory or interference need |

No trade study: a margin policy on a regulatory value (06 section 14.1 class 2 content presented to the owner because it changes the functional baseline).

## 4. Consequences

### 4.1 Requirements created or changed

| Requirement | Relationship | Note |
|---|---|---|
| REQ-SYS-NNN (spurious emissions per 97.307(e): at most 25 uW and at least 40 dB below carrier at every power step; L1 author allocates) | new, regulatory, traces to SI-014 with `47CFR97.307(e)` in `source_ids`, this ADR supporting | Bench with the tinySA; Analysis before build |
| REQ-TX-NNN (design target at least 60 dBc at 5 W at every instant of the envelope) | new at PDR, parent the L1 requirement, self-derived margin from this ADR | |
| REQ-TX-NNN (filter goals 40 dB at 288 to 296 MHz, 35 dB at 432 to 444 MHz, insertion loss at most 0.5 dB at 148 MHz, at the filter terminals) | new at PDR | NanoVNA S21 of the built filter |
| REQ-TX-NNN (ALC: 5.0 W plus or minus 0.5 dB above 6.4 V) | new at PDR (ADR-003 tolerance TBR closes here) | |
| REQ-TX-NNN (harmonics of concern reported individually at 2f, 3f, 7f; candidate RF-10) | new at PDR | Bench procedure |

### 4.2 Interfaces, design and code

- ICDs affected: `ICD-TX-ANT` (measurement point is the antenna port)
- Design elements created or changed: harmonic LPF (7th-order Chebyshev or 5th-order elliptic, 165 to 170 MHz cutoff, PDR design), PA line-up with gate-bias ALC (PA TS), enclosure partitioning and shielding between PA and filter
- New `SW-<SUB>` modules created by this ADR: none
- ICDs created by this ADR: none

### 4.3 Verification and safety

- Verification cases to add or change: TC-TX-NNN (Analysis: PA harmonic content plus filter response with parasitics, pass at 60 dBc), TC-TX-NNN (Bench: spurious scan 9 kHz to 1.5 GHz at 0.5, 1, 2, 5 W at 144.0, 146.0 and 148.0 MHz), TC-TX-NNN (Bench: filter S21 on the NanoVNA against the 40/35 dB goals)
- Evidence class implications: Analysis reduces risk before the build; the credit run is Bench on the delivered unit (charter section 9); the instrument is the tinySA (ADR-021)
- Hazard analysis update required: no
- Safety-critical software scope changed: no

### 4.4 Cost, schedule, risk

- BOM impact: a 7th-order or elliptic filter (about 7 to 9 reactive parts) and a directional coupler with detector for the ALC
- Gate affected: PDR (filter and PA design), CDR (analysis with tolerances), TRR (bench)
- Risks opened, closed or re-scored: RSK-011 (measurement) mitigated by ADR-021; proposed risks RF-1 (layout and SRF erosion), RF-4 (3f in the 70 cm weak-signal segment), RF-5 (7f at 1030 MHz) are addressed by the 60 dB target; RSK-001 (PA model infidelity) feeds the Analysis confidence
- TPMs affected: TPM-007. Note: TPM-007's planned value is 10 dB margin (63 dBc achieved) by analysis, while this ADR proposes a 60 dBc design target (7 dB margin). The two must be reconciled at SRR: either the TPM planned analysis value stays at 63 dBc as a stretch above the 60 dBc requirement, or the TPM planned value becomes 7 dB. The ADR author recommends keeping the requirement at 60 dBc and stating TPM-007's planned analysis value as 7 dB with 10 dB as the goal

## 5. Compliance and tailoring

none (the regulatory requirement replaces the spectrum-certification items marked NA in 01 section 3.5)

## 6. Decision record

Pending. Proposed wording for the SRR decision memo: "The spurious-emission requirement is written at the 97.307(e) values (25 uW, 40 dB); the design target is 60 dB below carrier at 5 W with the 40 dB at 288 MHz and 35 dB at 432 MHz filter goals; TPM-007's planned value is restated as 7 dB margin with 10 dB as goal." The owner's disposition will be transcribed here verbatim with its date; until then this ADR is Proposed.

## 7. Related

- Supersedes: none
- Superseded by: none
- Trade study: PA device and topology TS at PDR (the target is a criterion); no TS for the margin itself
- Review where presented: SRR (decision requested); PDR (filter design against the goals)
- Revisit conditions: the PDR Analysis shows 60 dBc unreachable with the stocked PA device and a 7th-order filter (then the owner chooses between a higher-order filter, a different device under ADR-012, or a target between 57 and 60 dBc); the chosen device's measured harmonics make 40/35 dB filter goals unnecessary (the goals may relax by a superseding ADR, the 60 dBc target stays)
