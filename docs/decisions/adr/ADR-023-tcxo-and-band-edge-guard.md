# ADR-023: Frequency reference TCXO of plus or minus 2.5 ppm or better and a 1 kHz band-edge guard

| Field | Value |
|---|---|
| ID | ADR-023 |
| Status | Proposed, pending owner decision at SRR |
| Date proposed | 2026-09-25 |
| Date decided | pending (SRR) |
| Decision class | 1 (`docs/process/06-risk-and-decision-analysis.md` section 14.1 items (b) selection of a critical part: the TCXO; (c) touches HZ-008, which names this ADR, and HZ-006 through REQ-TX-003; also the mission-critical frequency control `SW-SYNTH` and the envelope unit of `SW-TXSEQ` in `docs/process/07-software-engineering-plan.md` section 14.1). The TCXO grade and part go through the synthesizer and reference TS at PDR. No TS for the tolerance ceiling, guard and envelope convention: a proposal from research, admitted without a TS only if the owner's SRR disposition applies the customization of `reconciliation-srr.md` section 6 item (ii); otherwise a TS-NNN is opened before the decision |
| Decision authority | Robin (owner; the decision fixes a regulatory L1 requirement value and the reference oscillator class) |
| Author | Claude (technical data manager invocation, 2026-09-25) |
| Independent reviewer | INSP-011 iteration 1 (2026-09-25): NEEDS CHANGES, findings F-01 to F-04 apply; this revision (2026-09-25, ADR author invocation applying INSP-011) carries the fixes; re-review pending in INSP-011 iteration 2 |
| Life-cycle phase | Pre-A / A |
| Baseline affected | baseline/srr (functional baseline: regulatory L1 requirement) |
| Change request | none (pre-baseline) |

## 1. Context

47 CFR 97.307(b) requires emissions resulting from modulation to be confined to the band. A keyed carrier near 144.000 or 148.000 MHz has sidebands whose 26 dB bandwidth is 292 Hz in the worst case computed (continuous dits at 50 WPM with a 5 ms full-transition raised-cosine edge; 177 Hz for PARIS text with an 8 ms full transition), and the carrier itself has a frequency error set by the reference oscillator. A crystal-only reference of 20 to 30 ppm would need a 3.2 to 4.7 kHz guard and would miss a 100 Hz wide CW signal by several dits of pitch; a TCXO of plus or minus 2.5 ppm gives plus or minus 370 Hz at 148 MHz and lets a 1 kHz guard hold even the stronger criterion that every sideband beyond the edge is below -60 dB relative to the mean power. The Pico 2 module's 12 MHz crystal is not specified for RF synthesis, and its 12th harmonic lands on 144.000 MHz. The keying envelope convention must be stated because "5 ms" means different things for the full transition and for the 10 to 90 percent time.

- Driving inputs and expectations: SI-014, SI-024 (full band including the edges), SI-004 (narrow CW: the operator must find and hold a 100 Hz wide signal), SI-033 (50 WPM sets the worst case)
- Requirements that constrain the decision: frequency coverage (ADR-016); keyer speed (ADR-024)
- Hazards in play (`docs/safety/hazards.json` 0.3.0-pha): HZ-008 (harmonic and spurious emissions into safety-of-life and other radio services; HZ-008 names this ADR; cause C5 is a plain-crystal reference or hard keying, which items (1) and (3) of section 2 remove; controls K4 envelope and K7 independent frequency verification rest on the guard and tolerance; REQ-SYS-008 to REQ-SYS-010, REQ-SYS-154, REQ-SYS-182, REQ-TX-002, REQ-TX-003 and REQ-TX-013 cite this ADR and carry HZ-008); HZ-006 (REQ-TX-003, RF isolation with PA enable deasserted, cites this ADR and carries HZ-006)
- Research consulted: `docs/research/regulatory-corpus-and-operators.md` F7 (26 dB bandwidth table; hard keying 7 to 8 times wider; convention warning: a 5 ms 10-to-90 time is an 8.5 ms full transition), F8 (band-edge guard analysis; error versus ppm; 1 kHz guard holds the 26 dB criterion to about 5.7 ppm and the -60 dB criterion to about 2.6 ppm; TCXO of plus or minus 2.5 ppm recommended), REQ-candidates RF-02, RF-07, RF-09, RISK REG-6, DECISION-9, DECISION-11, ACTION-11; `docs/research/part97-regulatory-basis.md` F11 (band edges), REQ-candidate RF-02, RISK RF-3; `docs/research/keyer-verification-and-key-input-network.md` F11 (envelope 5 ms 10-to-90 percent raised cosine; full ramp 8.5 ms; 3 to 8 ms configurable), F12; `docs/research/2m-cw-transceiver-reference-designs.md` F21 (TCXO candidates: Epson TG2520SMN plus or minus 0.5 ppm, Abracon ATX-13 plus or minus 0.5 ppm, SiTime SiT5356 plus or minus 0.1 to 0.25 ppm with I2C trim, QRP Labs module plus or minus 0.25 ppm; a stock crystal puts the LO kilohertz off), F20 (LMX2571 is 5 dB noisier with a clipped-sine reference), REQ-candidate stability plus or minus 50 Hz; `docs/plan/tpm.json` TPM-006 (provisional target plus or minus 1 ppm, TBR closing at PDR with the reference TS)
- Guidance consulted: 47 CFR 97.307(a), (b), 97.3(a)(8) (eCFR 2026-09-23); 47 CFR 2.202; SE HB App. C; SE HB §6.8
- Assumptions the decision rests on, and how and by when each is confirmed:
  1. Catalog TCXOs meet plus or minus 2.5 ppm total (initial, temperature over -10 to +45 C, one year of aging) with margin (`2m-cw-transceiver-reference-designs.md` F21 lists 0.1 to 0.5 ppm parts). Confirmed by datasheet Inspection in the synthesizer and reference TS at PDR.
  2. The worst-case sideband arithmetic of `regulatory-corpus-and-operators.md` F7 and F8 (292 Hz 26 dB bandwidth; 1 kHz guard holds the -60 dB criterion to about 2.6 ppm) holds for the built envelope. Confirmed by Analysis on the LTspice envelope at PDR and CDR, then by Bench (tinySA, if its RBW allows) and OnAir listening at TRR.
  3. PA envelope distortion does not widen the 26 dB bandwidth beyond 350 Hz. Confirmed at TRR; a failure is a revisit condition (section 7).

## 2. Decision (proposed)

(1) The RF synthesizer reference is a TCXO with total frequency tolerance of plus or minus 2.5 ppm or better over initial accuracy, the operating temperature range of REQ-SYS-114 (-10 to +45 C, TBR; the previous revision proposed -10 to +50 C, aligned to REQ-SYS-010 and REQ-SYS-114 per INSP-011 finding F-04) and one year of aging, independent of the Pico 2 module's 12 MHz crystal, with a firmware calibration offset. The TCXO grade below that ceiling (0.5, 0.25 or 0.1 ppm) and its output type (clipped sine or square wave, which couples to the synthesizer choice) are decided with the synthesizer trade study (ADR-013) against TPM-006's operational stability target. (2) The transmit carrier is confined to 144.001 to 147.999 MHz (a 1 kHz guard at each edge), enforced in firmware independently of the display logic (ADR-016). (3) The keying envelope convention for every requirement is the 10 to 90 percent time of a raised-cosine (Hann) transition: 5 ms nominal, configurable 3 to 8 ms, no overshoot and no mid-ramp reversal; the corresponding full 0 to 100 percent transition is 8.5 ms nominal (5.1 to 13.6 ms), and the measured 26 dB bandwidth with continuous dits at 50 WPM is at most 350 Hz. (4) The declared necessary bandwidth for documentation is 208HA1A (ADR-003). (5) No system, SPI, PWM or USB clock harmonic of the controller falls on 144.000 to 148.000 MHz by design; the module crystal's 12th harmonic at 144.000 MHz is one reason the guard starts at 144.001 MHz and the frequency plan avoids the band.

## 3. Alternatives considered

| Option | Description | Why not chosen (or why chosen) |
|---|---|---|
| A (proposed) | TCXO at most plus or minus 2.5 ppm; 1 kHz guard; 5 ms 10-to-90 envelope | Holds the -60 dB sideband criterion at the edge; display good to a few hundred hertz; loses only the last kilohertz, which the voluntary band plan reserves for EME |
| B | Looser reference with a 2 kHz or wider guard | Not recommended: gives up 2 kHz at each edge and a frequency display too coarse to find a 100 Hz wide signal |
| C | Crystal-only reference (20 to 30 ppm) | Rejected: needs a 3.2 to 4.7 kHz guard; the LO is kilohertz off and drifts |
| D | Envelope specified as 5 ms full transition (2.95 ms 10-to-90) | Not chosen: faster edges widen the 26 dB bandwidth by 130 to 160 Hz; the reconciled keyer study fixed 5 ms 10-to-90 as the nominal; either convention is lawful, the requirement must simply name one |

No trade study for the tolerance ceiling and guard (a regulatory value pair); the TCXO grade and part go through the synthesizer and reference TS. The choice is class 1 (header), so the ADR without a TS stands only under the owner's ruling on `reconciliation-srr.md` section 6.

## 4. Consequences

### 4.1 Requirements created or changed

| Requirement | Relationship | Note |
|---|---|---|
| REQ-SYS-010 (carrier within plus or minus 2.5 ppm, TBR, from -10 C to +45 C for one year); candidate RF-09 | allocated at L1, cites this ADR; HZ-008 | Inspection (datasheet), Bench (frequency at temperature extremes if a freezer and heat test is available, else Analysis) |
| REQ-SYS-008 (transmit range 144.001 to 147.999 MHz with the guard) and REQ-TX-002 (same at L2); candidate RF-02 | allocated, cite this ADR and ADR-016; HZ-008; TBR | HostUnit, Bench |
| REQ-SYS-009 (transmit inhibit outside the guard) | allocated, cites this ADR; HZ-008; TBR | |
| REQ-SYS-014 (raised-cosine rises and falls, 3 to 8 ms 10-to-90, TBR), REQ-SYS-015 (26 dB bandwidth at most 350 Hz, TBR), REQ-TX-005 (envelope reproduction), REQ-TX-006 (keying sidebands); candidate RF-07 | allocated; REQ-SYS-015 and REQ-TX-006 cite ADR-024, and REQ-SYS-014 and REQ-TX-005 cite no ADR although item (3) of section 2 is their source | Cross item to the requirement authors: add ADR-023 to their `source_ids` |
| REQ-SYS-034 (internally generated receive responses); candidate RF-08, no controller clock harmonic in band | allocated at L1 as a receive-side limit (HZ-008 control K6, clock plan); does not cite this ADR; no separate design-rule requirement created | Analysis (clock harmonic map), Bench (birdie scan) |
| REQ-SYS-154 (synthesizer fault response), REQ-SYS-182 (independent frequency verification), REQ-TX-003 (RF isolation with PA enable deasserted), REQ-TX-013 (synthesizer frequency sample) | allocated, cite this ADR as the source of the guard and tolerance; HZ-008 (REQ-TX-003 also HZ-006) | The verification function itself is package decision 40 (HZ-008 control K7), not a decision of this ADR |
| TPM-006 | value TBR stays open until the synthesizer and reference TS | This ADR fixes the ceiling (2.5 ppm), not the operational target |

### 4.2 Interfaces, design and code

- ICDs affected: none external; the synthesizer reference input is part of the synthesizer block interface at PDR
- Design elements created or changed: TCXO block, frequency plan data (guard, calibration offset), envelope shaper (DAC or filtered PWM to the PA bias node), clock plan for SPI, PWM and system clocks
- New `SW-<SUB>` modules created by this ADR: none
- ICDs created by this ADR: none

### 4.3 Verification and safety

- Verification cases to add or change: TC-SYS-NNN (frequency accuracy against a known reference, Bench), TC-TX-NNN (band-edge emission inside the band, Bench and Analysis), TC-TX-NNN (envelope shape and 26 dB bandwidth, Analysis on the LTspice envelope with the `bw.py` method), TC-SYS-NNN (clock harmonic map, Analysis; birdie scan, Bench)
- Evidence class implications: the close-in bandwidth stays Analysis unless the tinySA RBW is adequate (ADR-021); temperature testing is informal (freezer and heat) or Analysis
- Hazard analysis update required: yes (HZ-008 names this ADR; cause C5 and controls K4 and K7 depend on items (1) to (3) of section 2; the hazard analysis and this ADR now agree)
- Safety-critical software scope changed: no by this ADR; frequency control (`SW-SYNTH`) is mission-critical in 07 section 14.1, and whether it becomes safety-critical is the owner's package decision 9 (OQ-SAF-014)

### 4.4 Cost, schedule, risk

- BOM impact: TCXO USD 0.44 to 9 depending on grade
- Gate affected: SRR (values), PDR (grade and part with the synthesizer TS)
- Risks opened, closed or re-scored: RSK-002 (LO frequency error exceeds the CW filter half-bandwidth) gains this ADR as mitigation; proposed risk REG-6 (band-edge violation by reference drift) is mitigated
- TPMs affected: TPM-006

## 5. Compliance and tailoring

none

## 6. Decision record

Pending. Proposed wording for the SRR decision memo: "Reference tolerance at most plus or minus 2.5 ppm total, TCXO independent of the module crystal; transmit carrier 144.001 to 147.999 MHz; envelope convention 5 ms 10-to-90 percent raised cosine, 3 to 8 ms configurable; necessary bandwidth documented as 208HA1A." The owner's disposition will be transcribed here verbatim with its date; until then this ADR is Proposed.

## 7. Related

- Supersedes: none
- Superseded by: none
- Trade study: synthesizer and reference TS at PDR (ADR-013) selects the TCXO grade and part. `docs/design/concept.md` section 11.2 labels that study TS-002, but TS-002 is now the firmware runtime make/buy study, so the synthesizer and reference study takes the next free TS id when it is created (cross item to the concept author)
- Review where presented: SRR (decision requested)
- Revisit conditions: the owner prefers alternative B (then ADR-016's carrier range narrows by the same superseding ADR); the synthesizer TS finds the 2.5 ppm ceiling too loose for the CW filter (then TPM-006 tightens the operational requirement; the regulatory ceiling stays); the PA envelope distortion measured at TRR widens the 26 dB bandwidth beyond 350 Hz (then the 3 to 8 ms range or the nominal is revisited by CR)
