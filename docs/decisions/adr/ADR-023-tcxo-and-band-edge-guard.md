# ADR-023: Frequency reference TCXO of plus or minus 2.5 ppm or better and a 1 kHz band-edge guard

| Field | Value |
|---|---|
| ID | ADR-023 |
| Status | Proposed, pending owner decision at SRR |
| Date proposed | 2026-09-25 |
| Date decided | pending (SRR) |
| Decision authority | Robin (owner; the decision fixes a regulatory L1 requirement value and the reference oscillator class) |
| Author | Claude (technical data manager invocation, 2026-09-25) |
| Independent reviewer | Pending: reviewer agent invocation before SRR (01 section 3.2 row S3; 06 section 14.2) |
| Life-cycle phase | Pre-A / A |
| Baseline affected | baseline/srr (functional baseline: regulatory L1 requirement) |
| Change request | none (pre-baseline) |

## 1. Context

47 CFR 97.307(b) requires emissions resulting from modulation to be confined to the band. A keyed carrier near 144.000 or 148.000 MHz has sidebands whose 26 dB bandwidth is 292 Hz in the worst case computed (continuous dits at 50 WPM with a 5 ms full-transition raised-cosine edge; 177 Hz for PARIS text with an 8 ms full transition), and the carrier itself has a frequency error set by the reference oscillator. A crystal-only reference of 20 to 30 ppm would need a 3.2 to 4.7 kHz guard and would miss a 100 Hz wide CW signal by several dits of pitch; a TCXO of plus or minus 2.5 ppm gives plus or minus 370 Hz at 148 MHz and lets a 1 kHz guard hold even the stronger criterion that every sideband beyond the edge is below -60 dB relative to the mean power. The Pico 2 module's 12 MHz crystal is not specified for RF synthesis, and its 12th harmonic lands on 144.000 MHz. The keying envelope convention must be stated because "5 ms" means different things for the full transition and for the 10 to 90 percent time.

- Driving inputs and expectations: SI-014, SI-024 (full band including the edges), SI-004 (narrow CW: the operator must find and hold a 100 Hz wide signal), SI-033 (50 WPM sets the worst case)
- Requirements that constrain the decision: frequency coverage (ADR-016); keyer speed (ADR-024)
- Hazards in play: none (regulatory and mission)
- Research consulted: `docs/research/regulatory-corpus-and-operators.md` F7 (26 dB bandwidth table; hard keying 7 to 8 times wider; convention warning: a 5 ms 10-to-90 time is an 8.5 ms full transition), F8 (band-edge guard analysis; error versus ppm; 1 kHz guard holds the 26 dB criterion to about 5.7 ppm and the -60 dB criterion to about 2.6 ppm; TCXO of plus or minus 2.5 ppm recommended), REQ-candidates RF-02, RF-07, RF-09, RISK REG-6, DECISION-9, DECISION-11, ACTION-11; `docs/research/part97-regulatory-basis.md` F11 (band edges), REQ-candidate RF-02, RISK RF-3; `docs/research/keyer-verification-and-key-input-network.md` F11 (envelope 5 ms 10-to-90 percent raised cosine; full ramp 8.5 ms; 3 to 8 ms configurable), F12; `docs/research/2m-cw-transceiver-reference-designs.md` F21 (TCXO candidates: Epson TG2520SMN plus or minus 0.5 ppm, Abracon ATX-13 plus or minus 0.5 ppm, SiTime SiT5356 plus or minus 0.1 to 0.25 ppm with I2C trim, QRP Labs module plus or minus 0.25 ppm; a stock crystal puts the LO kilohertz off), F20 (LMX2571 is 5 dB noisier with a clipped-sine reference), REQ-candidate stability plus or minus 50 Hz; `docs/plan/tpm.json` TPM-006 (provisional target plus or minus 1 ppm, TBR closing at PDR with the reference TS)
- Guidance consulted: 47 CFR 97.307(a), (b), 97.3(a)(8) (eCFR 2026-09-23); 47 CFR 2.202; SE HB App. C; SE HB §6.8

## 2. Decision (proposed)

(1) The RF synthesizer reference is a TCXO with total frequency tolerance of plus or minus 2.5 ppm or better over initial accuracy, the operating temperature range (-10 to +50 C proposed) and one year of aging, independent of the Pico 2 module's 12 MHz crystal, with a firmware calibration offset. The TCXO grade below that ceiling (0.5, 0.25 or 0.1 ppm) and its output type (clipped sine or square wave, which couples to the synthesizer choice) are decided with the synthesizer trade study (ADR-013) against TPM-006's operational stability target. (2) The transmit carrier is confined to 144.001 to 147.999 MHz (a 1 kHz guard at each edge), enforced in firmware independently of the display logic (ADR-016). (3) The keying envelope convention for every requirement is the 10 to 90 percent time of a raised-cosine (Hann) transition: 5 ms nominal, configurable 3 to 8 ms, no overshoot and no mid-ramp reversal; the corresponding full 0 to 100 percent transition is 8.5 ms nominal (5.1 to 13.6 ms), and the measured 26 dB bandwidth with continuous dits at 50 WPM is at most 350 Hz. (4) The declared necessary bandwidth for documentation is 208HA1A (ADR-003). (5) No system, SPI, PWM or USB clock harmonic of the controller falls on 144.000 to 148.000 MHz by design; the module crystal's 12th harmonic at 144.000 MHz is one reason the guard starts at 144.001 MHz and the frequency plan avoids the band.

## 3. Alternatives considered

| Option | Description | Why not chosen (or why chosen) |
|---|---|---|
| A (proposed) | TCXO at most plus or minus 2.5 ppm; 1 kHz guard; 5 ms 10-to-90 envelope | Holds the -60 dB sideband criterion at the edge; display good to a few hundred hertz; loses only the last kilohertz, which the voluntary band plan reserves for EME |
| B | Looser reference with a 2 kHz or wider guard | Not recommended: gives up 2 kHz at each edge and a frequency display too coarse to find a 100 Hz wide signal |
| C | Crystal-only reference (20 to 30 ppm) | Rejected: needs a 3.2 to 4.7 kHz guard; the LO is kilohertz off and drifts |
| D | Envelope specified as 5 ms full transition (2.95 ms 10-to-90) | Not chosen: faster edges widen the 26 dB bandwidth by 130 to 160 Hz; the reconciled keyer study fixed 5 ms 10-to-90 as the nominal; either convention is lawful, the requirement must simply name one |

No trade study for the tolerance ceiling and guard (a regulatory value pair); the TCXO grade and part go through the synthesizer TS.

## 4. Consequences

### 4.1 Requirements created or changed

| Requirement | Relationship | Note |
|---|---|---|
| REQ-SYS-NNN (frequency reference total tolerance at most plus or minus 2.5 ppm; candidate RF-09; L1 author allocates) | new, regulatory support for 97.307(b), traces to SI-014, SI-024 | Inspection (datasheet), Bench (frequency at temperature extremes if a freezer and heat test is available, else Analysis) |
| REQ-SYS-NNN (transmit carrier 144.001 to 147.999 MHz; candidate RF-02) | new (shared with ADR-016) | HostUnit, Bench |
| REQ-SYS-NNN (keying envelope: raised cosine, 5 ms 10-to-90 percent nominal, 3 to 8 ms configurable, no overshoot; 26 dB bandwidth at most 350 Hz at 50 WPM continuous dits; candidate RF-07) | new, regulatory 97.307(a), (b) | Analysis (envelope FFT on the simulated PA output), Bench (tinySA max-hold if RBW allows), OnAir listening |
| REQ-SYS-NNN (no controller clock harmonic in 144.000 to 148.000 MHz; candidate RF-08) | new, design rule | Analysis (clock harmonic map), Bench (birdie scan) |
| TPM-006 | value TBR stays open until the synthesizer TS | This ADR fixes the ceiling (2.5 ppm), not the operational target |

### 4.2 Interfaces, design and code

- ICDs affected: none external; the synthesizer reference input is part of the synthesizer block interface at PDR
- Design elements created or changed: TCXO block, frequency plan data (guard, calibration offset), envelope shaper (DAC or filtered PWM to the PA bias node), clock plan for SPI, PWM and system clocks
- New `SW-<SUB>` modules created by this ADR: none
- ICDs created by this ADR: none

### 4.3 Verification and safety

- Verification cases to add or change: TC-SYS-NNN (frequency accuracy against a known reference, Bench), TC-TX-NNN (band-edge emission inside the band, Bench and Analysis), TC-TX-NNN (envelope shape and 26 dB bandwidth, Analysis on the LTspice envelope with the `bw.py` method), TC-SYS-NNN (clock harmonic map, Analysis; birdie scan, Bench)
- Evidence class implications: the close-in bandwidth stays Analysis unless the tinySA RBW is adequate (ADR-021); temperature testing is informal (freezer and heat) or Analysis
- Hazard analysis update required: no
- Safety-critical software scope changed: no

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
- Trade study: synthesizer and reference TS at PDR (ADR-013) selects the TCXO grade and part
- Review where presented: SRR (decision requested)
- Revisit conditions: the owner prefers alternative B (then ADR-016's carrier range narrows by the same superseding ADR); the synthesizer TS finds the 2.5 ppm ceiling too loose for the CW filter (then TPM-006 tightens the operational requirement; the regulatory ceiling stays); the PA envelope distortion measured at TRR widens the 26 dB bandwidth beyond 350 Hz (then the 3 to 8 ms range or the nominal is revisited by CR)
