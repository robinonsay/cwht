# TS-001: Receiver architecture, CW selectivity and PA device-and-supply concept

| Field | Value |
|---|---|
| ID | TS-001 |
| Status | Draft, revision 1 (findings F-01 to F-07 of INSP-013 applied; awaiting the reviewer's verification of the fixes) |
| Decision class trigger | 06 section 14.1 class 1 items (a) architecture choice (receiver topology, PA topology), (b) selection of a single-source or critical part (RF power device, CW filter) and (c) a choice touching hazards HZ-003 and HZ-008 in `docs/safety/hazards.json` |
| Decision maker | Robin (owner, Decision Authority) |
| Recommender | Claude (trade study author invocation, 2026-09-25) |
| Independent reviewer | INSP-013 in `docs/reviews/SRR/checklists/trade-studies-ts-001-ts-002.md`, one record for TS-001 and TS-002, filled from `docs/templates/peer-review-checklist-design.md` sections A, B and H plus the 06 section 16 trade-study items. The record path and checklist differ from the 06 section 14.2 slug rule; INSP-013 returns that choice to Claude. Iteration 1: NEEDS CHANGES (2 Major, 8 Minor); revision 1 applies F-01 to F-07 |
| Decide by | PDR, because the allocated baseline fixes the RX and TX L2 specifications, `ICD-RX-CTL` (demodulated audio for candidate A, I2S for candidate B) and the PA rail (`docs/design/concept.md` section 11.2; 06 section 14.2 "Timing" row). At SRR this report is the concept-level trade that `docs/process/01-lifecycle-and-reviews.md` section 4.3 row 5 requires (NPR 7123.1D App. G Table G-3 item 5.2, "Alternative concepts that have been analyzed") and the analysis behind SRR package decisions 54, 55 and 58, which the owner rules in the SRR decision memo as interim direction (section 8.4) |
| Related risks | RSK-001, RSK-005, RSK-006, RSK-008, RSK-013, RSK-027, RSK-031, RSK-036, RSK-037, RSK-038, RSK-040, RSK-047, RSK-058 |
| Related requirements and hazards | REQ-SYS-012, REQ-SYS-013, REQ-SYS-017, REQ-SYS-018, REQ-SYS-022, REQ-SYS-024 to REQ-SYS-030, REQ-SYS-033, REQ-SYS-094, REQ-SYS-103, REQ-SYS-112, REQ-SYS-137, REQ-SYS-140, REQ-SYS-147, REQ-SYS-152; HZ-003, HZ-008; SI-001, SI-009, SI-010, SI-019, SI-028, SI-031 |
| Resulting ADR | ADR-NNN, the next free number at decision time (ADR-027 or later, because ADR-026 is the proposed successor of ADR-010; `docs/decisions/adr/README.md` rule 1), written the day the owner decides |
| Dates | opened 2026-09-25; recommended: on filing of the independent review record; decided: at PDR |

## 1. Executive summary

The study covers three linked sub-decisions. **R1** is the receiver architecture family, **R2** is the CW selectivity architecture inside that family (candidate A against candidate B) and **P** is the PA device and its supply and level-control topology.

- **Recommendation (one sentence):** keep the single-conversion superhet family (R1), carry selectivity candidates A (Inrad #111 8-pole crystal filter with analog AGC) and B (1.0 kHz tolerance-designed ladder, 24-bit I2S ADC and DSP) into Phase B as a closely ranked pair with A as the planning baseline (R2: A 330 of 500, 66 %; B 310, 62 %; not robust), adopt ST PD54008L-E run directly from the protected pack with gate-bias ALC as the primary PA (P1: 460, 92 %), and name the 12.5 V boost with PD55015-E (280) and then PD55008-E (265) jointly as fallback candidates, since GRF5604 fails the REQ-SYS-112 junction screen.
- **Conditions on the recommendation:** A's selectivity pass is conditional on the Inrad #111 bandwidth tolerance and termination quote, because its 400 Hz nominal sits on the REQ-SYS-024 lower limit (section 4). P1's rated-output pass is conditional on the driver gain budget of TS-003 at PDR, because the vendor result used an obsolete driver. GRF5604 re-enters the fallback set only with a CR on REQ-SYS-112 or vendor data showing lower stage-2 dissipation (section 8.3).
- **Problem requiring a decision (one sentence):** which receiver family, which selectivity architecture and which PA device-and-supply concept go into preliminary design. The choice must hold the 500 Hz CW channel and the 25 uW spurious limit of 47 CFR 97.307(e), be built by PCBWay turnkey under SI-028 and SI-031, and meet the 8 h battery life of REQ-SYS-094.
- **Robustness verdict (section 6):** Not robust for R2 (seven single-weight perturbations put B first, and A leads by 20 points, inside the 25-point closeness rule). Robust for the P primary. Not robust for the fallback order within P.
- **Owner's decision (section 10):** pending. Interim SRR rulings requested on package decisions 54, 55 and 58 (section 8.4).

## 2. Problem and decision context

- **Mission and system context:** receive path blocks B08 to B11 (RX) and transmit blocks B01 to B07 (TX) of `docs/design/concept.md` sections 5 and 7. ConOps scenarios: nominal CW contacts on open ground and from a hilltop, a weak friend next to a strong one, and battery life over a day out (`docs/conops/conops.md`). Measures of effectiveness: MOE-001, MOE-002, MOE-003 (first power-on), MOE-004 (battery), MOE-006 (spurious compliance), MOE-007 (cost), MOE-010 (weak signal next to a strong one) and MOE-013 (pocket carry) (`docs/requirements/l0-stakeholder/expectations.json`). Key driving requirements in play: REQ-SYS-012, REQ-SYS-017, REQ-SYS-018, REQ-SYS-022, REQ-SYS-094, REQ-SYS-103, REQ-SYS-112, REQ-SYS-137 and REQ-SYS-140 (18 KDRs listed in `docs/reviews/SRR/traceability-report.md` section 1.3).
- **Decision needed and intended outcome:** after the decision, the preliminary design has one receiver family and one selectivity architecture. That fixes the IF, the RX current budget, `ICD-RX-CTL` and whether rustos needs PIO, DMA and I2S drivers. It also has one PA device-and-supply topology, which fixes the PA rail, the ALC and envelope node and the harmonic filter basis. The final device line-up (driver, match, filter values, early buy) and the ALC detail are then worked in TS-003 and TS-006 at PDR (concept section 11.2), both of which cite this study.
- **Scope boundary with the PDR studies of concept section 11.2:**
  - The concept row "TS-001 CW selectivity architecture" is this study; its PDR evidence list is section 6 item 5 below.
  - Concept TS-003 "PA device and line-up" narrows to the line-up of the device this study selects (driver, match, LPF values, lifetime reserve), with the device choice taken here. That scope change is proposed to the concept author (return item) and ruled by the owner with decision 58.
  - The ALC and envelope topology stays in TS-006 (package decision 59). The synthesizer stays in its own study (ADR-013); this study assumes an LO of the Si5351A or LMX2571 class and scores nothing that depends on the choice between them.
- **Constraints:**
  - SI-028 and ADR-012: the PA device is stocked at DigiKey, Mouser or a PCBWay turnkey distributor, with no consignment-only parts.
  - SI-009, SI-031 and ADR-007: PCBWay places every surface-mount part (REQ-SYS-137). The owner solders through-hole parts and simple pads only.
  - REQ-SYS-140: every turnkey-placed part and the PA device come from those distributors.
  - SI-010: works at first power-on.
  - SI-019: several units for friends, so unit-to-unit repeatability matters.
  - SI-034 and ADR-020: 8 h at 1:9.
  - 47 CFR 97.307(e) (corpus: `47cfr-97.307.md`, eCFR issue 2026-09-23): at 5.0 W the 25 uW cap binds at 53.0 dB below carrier; the project design target is 60 dB (ADR-022, proposed).
  - Cost ceiling: USD 610 per unit (REQ-SYS-147, TBR).
  - Owner bench: NanoVNA, tinySA Ultra with attenuator, dummy load; no oscilloscope (SI-013, SI-034).
- **Prior related decisions and lessons learned:** ADR-002 (70 cm-ready), ADR-003 (true CW at 5 W), ADR-007, ADR-010 (semi break-in with a relay T/R), ADR-011 (host-first software), ADR-012, ADR-013, ADR-019 (drivers upstream in rustos), ADR-020, ADR-022 and ADR-023 (proposed). The concept-level alternative sets of `docs/design/concept.md` section 11.1 are the starting point. `docs/lessons-learned.md` does not exist yet, so there are no lessons-learned entries to cite.
- **Research consulted:** `docs/research/cw-selectivity-options.md` (F1 to F18, implications 1 to 18), `docs/research/pa-turnkey-candidates-followup.md` (F1 to F20, implications 1 to 18), `docs/research/pa-device-candidates.md` (F1 to F21), `docs/research/2m-cw-transceiver-reference-designs.md` (F6 to F16, implications 13 to 19), `docs/research/power-tree-and-charging.md` (F17, F18, F22, F23) and `docs/research/pcbway-fabrication-and-assembly.md` (F16, F17).

## 3. Decision matrix setup and rationale

### 3.1 Criteria and operational definitions

Mandatory criteria are pass or fail; an alternative that fails any of them is dropped before scoring (SE HB §6.8.1.2.1). Enhancing criteria are scored 1 to 5 against the anchors. Intermediate scores (2, 4) are interpolated linearly between anchors, and a measured value is scored at the midpoint of its reported range, rounded to the nearest integer (SE HB §6.8.1.2.4).

**Decision R1 (receiver family), screening criteria only** (the family is chosen by the trade tree of section 3.2; no weighted matrix):

| ID | Criterion | Type | Operational definition | Scale | Weight |
|---|---|---|---|---|---|
| M-R1 | Image and IF response rejection achievable | Mandatory | At least 70 dB image and IF rejection (REQ-SYS-033, TBR), shown by a published measured design of the family or, where the corpus holds none, by a front-end filter analysis with a stated confidence and a named PDR evidence item (definition widened in revision 1, INSP-013 finding-4) | pass / fail | n/a |
| M-R2 | Fits the handheld | Mandatory | One enclosure within 140 x 70 x 40 mm (REQ-SYS-103, TBR) on the 2S pack (SI-001, SI-023) | pass / fail | n/a |

**Decision R2 (selectivity architecture):**

| ID | Criterion | Type | Operational definition (what is measured, unit, method) | Scale anchors (1 / 3 / 5) | Weight |
|---|---|---|---|---|---|
| M1 | Selectivity TBR set reachable | Mandatory | -6 dB bandwidth 400 to 600 Hz, -60 dB bandwidth at most 2.5 kHz, at least 60 dB from 2 to 5 kHz, at least 80 dB beyond 5 kHz, ripple at most 2 dB (REQ-SYS-024 to REQ-SYS-028), met by datasheet or by simulation of the chain | pass / fail | n/a |
| M2 | Buildable in the kit model | Mandatory | Every surface-mount part turnkey-placeable without hand matching (REQ-SYS-137); every owner-soldered part through-hole or a simple pad (SI-031); every turnkey-placed part stocked per REQ-SYS-140 | pass / fail | n/a |
| M3 | No unreducible Red safety risk | Mandatory | 06 section 13 item 2 on the register scales | pass / fail | n/a |
| C1 | Adjacent-signal protection | Enhancing | Attenuation of a signal 2 kHz from the channel centre ahead of the first gain-controlled or full-scale-limited stage (analog AGC or ADC), dB, 5th-percentile unit; datasheet or Monte Carlo | 1: < 30 dB / 3: 45 dB / 5: >= 60 dB | 20 |
| C2 | Sensitivity cost | Enhancing | Insertion loss of the selectivity element after the post-mixer amplifier, dB, median unit; datasheet or Monte Carlo | 1: >= 10 dB / 3: 7 dB / 5: <= 4 dB | 10 |
| C3 | Unit-to-unit repeatability | Enhancing | Fraction of assembled units meeting the M1 set without hand selection or tuning, percent; vendor specification or Monte Carlo | 1: < 50 % / 3: 90 % / 5: >= 98 % | 15 |
| C4 | Receive current of the block | Enhancing | Current of the selectivity block with its IF amplifier, detector and ADC, mA at 3.3 or 5 V; research estimate | 1: >= 60 mA / 3: 45 mA / 5: <= 30 mA | 10 |
| C5 | Firmware scope | Enhancing | rustos work packages and `cwht-core` modules added beyond the set of `docs/process/07-software-engineering-plan.md` section 19 to realize the selectivity; count | 1: >= 3 added drivers plus a new module / 3: one added driver or one new module / 5: none | 15 |
| C6 | First-power-on confidence | Enhancing | Best pre-build evidence available for the selectivity path | 1: analysis with an unvalidated model only / 3: simulation or host tests of the whole path, one element untested on hardware / 5: every element measured or demonstrated on hardware before the build | 10 |
| C7 | Unit cost | Enhancing | Cost of the selectivity element and its converter parts per unit at quantity 10, USD; vendor page or distributor snapshot | 1: >= 100 / 3: 25 / 5: <= 5 | 5 |
| C8 | Supply depth | Enhancing | Sources and published stock for the parts that set selectivity | 1: one source, quote-only or no published stock / 3: one source with catalogue stock, or two quote-only sources / 5: two or more sources with published stock | 10 |
| C9 | Envelope fit | Enhancing | Tallest part of the block above the board, mm; datasheet case drawing | 1: >= 15 mm / 3: 10 mm / 5: <= 5 mm | 5 |
| | | | | **Sum of weights** | **100** |

**Decision P (PA device and supply-and-control topology):**

| ID | Criterion | Type | Operational definition (what is measured, unit, method) | Scale anchors (1 / 3 / 5) | Weight |
|---|---|---|---|---|---|
| M1 | Sourcing (SI-028) | Mandatory | Final device and driver device (ADR-012 section 2 makes both mandatory-criterion parts) each in active production and stocked at minimum order quantity 1 by DigiKey, Mouser, Farnell element14 or Newark, Arrow or Avnet on the snapshot date, in a quantity readily covering the build plus reserve (REQ-SYS-140; ADR-012) | pass / fail | n/a |
| M2 | Rated output with level control | Mandatory | 5.0 W at the 5 W step held within +/-1 dB over 6.4 to 8.4 V pack (REQ-SYS-012, TBR), shown by vendor data or by a fixed-rail topology with device headroom | pass / fail | n/a |
| M3 | Turnkey package | Mandatory | Package placeable by PCBWay turnkey (REQ-SYS-137); no flange module that must be screwed down before its leads are soldered | pass / fail | n/a |
| M4 | No unreducible Red safety risk | Mandatory | 06 section 13 item 2 | pass / fail | n/a |
| M5 | Junction temperature screen (REQ-SYS-112) | Mandatory | Necessary condition for REQ-SYS-112 (KDR, TBR: PA junction at or below 110 C during continuous key-down at the 5 W step in 45 C ambient): 45 C plus the junction-to-case (or junction-to-base) rise at 5 W, taken with zero case-to-ambient rise (the most favourable bound), is at or below 110 C; vendor thermal resistance times derived dissipation. Sufficiency is shown by the thermal budget at PDR (added in revision 1, INSP-013 finding-2) | pass / fail | n/a |
| C1 | Harmonic data quality | Enhancing | Best vendor harmonic evidence for the device in its VHF circuit at 5 W | 1: none / 3: device-level typical harmonics at VHF / 5: system-level maximum at 5 W with a vendor harmonic filter | 20 |
| C2 | Matching and model maturity at 144 to 148 MHz | Enhancing | Vendor design data available for the band | 1: no VHF data, custom tune needed / 3: vendor circuit in a nearby VHF band or voltage to re-tune / 5: complete vendor 135 to 175 MHz reference design with BOM, layout and measured curves | 20 |
| C3 | DC input at 5 W | Enhancing | Pack power drawn during key-down at 5 W out including any converter loss, W; vendor curves or derived budget | 1: >= 12 W / 3: 10.5 W / 5: <= 9 W | 10 |
| C4 | Thermal margin | Enhancing | Junction-to-case (or junction-to-base) temperature rise at 5 W continuous, C; RthJC times dissipation | 1: >= 80 C / 3: 40 C / 5: <= 15 C | 10 |
| C5 | Receiver compatibility | Enhancing | New switching converters introduced by the topology next to the -140 dBm receiver | 1: a new switcher of 15 W or more on the PA rail / 3: a new switcher of 10 W class that can be off in receive / 5: no new switcher | 10 |
| C6 | Unit cost | Enhancing | Final device plus topology-specific parts (driver, converter) per unit at quantity 10, USD; distributor snapshot | 1: >= 25 / 3: 15 / 5: <= 8 | 5 |
| C7 | Supply depth and lifecycle | Enhancing | Distributors holding at least 10 times the project quantity (25 pieces: 5 units plus a 20-piece reserve, followup implication 9) at MOQ 1, and lifecycle signals | 1: one distributor below 10 times / 3: one distributor at 100 times or more, or two at 10 times or more / 5: two or more at 100 times or more, no NRND or obsolescence signal in the device family | 10 |
| C8 | Level-control and envelope integration | Enhancing | How the ALC loop and the keying envelope reach the device | 1: needs an added control element and a separate envelope node, neither characterized / 3: drive-level control through one added element / 5: one vendor-characterized node serves ALC and envelope | 10 |
| C9 | Mismatch ruggedness | Enhancing | Vendor-stated load mismatch survival | 1: none stated / 3: stated below 10:1 or only at reduced drive / 5: 20:1 all phases at or above the operating voltage | 5 |
| | | | | **Sum of weights** | **100** |

**Criteria considered** (mandatory line, 06 section 13 item 1):

- **Safety:** used as mandatory M3 (R2), M4 (P) and M5 (P, the REQ-SYS-112 junction screen). The PA thermal margin is also scored as C4 of P because HZ-003 is in play. Selectivity touches no hazard: the acoustic ceiling of HZ-005 is set by passive parts after the audio source (concept section 8).
- **First power-on:** used as R2 C6 and P C2 (MOE-003; RSK-008 is the top register risk at score 20).
- **Cost:** used as R2 C7 and P C6.
- **Schedule:** used as R2 C5, since firmware work packages are the schedule driver of RSK-013, and as P C2, since a custom tune or a missing reference circuit is the schedule driver of the PA.
- **Performance margin:** used as R2 C1, C2 and C4, and as P C1, C3 and C8.
- **System security:** omitted from both. Neither sub-decision changes an attack surface of `docs/process/07-software-engineering-plan.md` section 16.2 (USB firmware load, key input). Candidate B adds code but no external interface.

Other criteria considered and not used, with reason:

- 70 cm reuse (SI-002): both selectivity candidates sit at an IF that concept section 10 item 3 already makes band-agnostic, and every PA candidate is replaced in rev B.
- Selectable bandwidth: a benefit of B, recorded in section 7 rather than scored, because the TBR set asks for one 500 Hz channel.
- Mass: the PA and filter differences are a few grams against a 350 g allocation (TPM-001).

### 3.2 Alternatives

**R1 receiver family** (trade tree; concept section 11.1 row "Receiver architecture family"):

| ID | Alternative | Screening result |
|---|---|---|
| F-A | Single-conversion superhet at 144 MHz, tunable LO, about 9 MHz crystal IF (FT-290R and IC-202 pattern) | Passes M-R1 by analysis, Low confidence: the corpus holds no measured image rejection for a single-conversion 2 m design with an IF near 9 MHz (reference report F1, F2 and implication 13 give none). The image lies 18 MHz from the signal: 126 to 130 MHz with low-side LO, 162 to 166 MHz with high-side LO. An ideal 3-pole Butterworth band-pass at 146 MHz with the Anglian's bandwidth (1 dB bandwidth 4 MHz, so 5.0 MHz at 3 dB; reference report F6) gives 47.0 dB at 162 MHz and 49.9 dB at 130 MHz, short of 70 dB. Two such sections (the Anglian places a noise-matching filter and a 3-pole band-pass in its receive path, F6) give at least 94 dB, and one 5-pole section at least 78 dB; IF rejection at 9 MHz exceeds 150 dB for one section (Appendix A.3, second listing). The model is lossless and ideal, with no strays, coupling or mixer-port leakage, hence Low. PDR evidence item: the front-end filter design and simulation with at least five resonators ahead of the mixer, closed at CDR by TC-SYS-021. Passes M-R2. **Kept; R2 is decided inside it** |
| F-B | Internal transverter: fixed 116 MHz overtone LO to a 28 MHz IF, then an HF back end | Passes M-R1: image rejection above 70 dB measured in the Anglian (reference report F6). The other two transverters in the report state less: the Kuhne MKU 144 G2 specifies spurious rejection of at least 60 dB (F7) and the Elecraft XV144 image rejection above 60 dB (F8). With the 116 MHz LO the image sits at 88 MHz, where one ideal 3-pole section gives 89 dB (Appendix A.3, second listing). Passes M-R2. **Pruned by dominance, not scored** (argument quantified below the table) |
| F-C | Direct conversion I/Q at 144 MHz with DSP | **Fails M-R1.** G4JNT's 144 MHz receiver targets 20 to 25 dB opposite-sideband rejection (reference report F12). An integrated demodulator (LT5517) is limited to about 35 dB by its I/Q mismatch and draws 90 mA; Si5351 quadrature stops near 110 MHz (`cw-selectivity-options.md` F16) |
| F-D | Commercial transverter plus an HF CW rig | **Fails M-R2**: two boxes. The Kuhne module alone runs from 12 to 14 V at 370 mA (reference report F7). Kept as the project-level fallback of concept section 11.1 |

**F-B pruning argument.** 06 section 14.3 step 2 asks for pruned alternatives to be recorded with the reason. Its trade-tree clause applies above five alternatives and R1 has four, so the pruning of F-B rests on dominance, stated here with numbers:

- F-B's 28 MHz back end still needs a selectivity element of the R2 kind: a crystal filter or ladder at 28 MHz, or a second conversion to a 9 MHz filter (reference report implication 13). On R2 C1, C2, C3, C5, C7, C8 and C9 F-B can therefore score at most what the chosen R2 candidate scores inside F-A.
- It adds a 116 MHz overtone crystal oscillator with a buffer to mixer drive level, a second mixer and its IF filter, so one more oscillator is untested before the build (R2 C6 no better than F-A).
- It adds receive current in every receive hour. In the battery model of `power-tree-and-charging.md` F23, recomputed here, each 30 mA added on the 5 V bus moves the low-build receive-only life from 19.4 h to 16.7 h and the 1:9 life from 13.0 h to 11.7 h, with TPM-002 red. The corpus gives no current for a 116 MHz LO chain (the Kuhne LO delivers more than 100 mW, F7); 15 to 30 mA is this author's estimate, Low (R2 C4 no better than F-A).
- F-B's advantages are the image margin (89 dB from one section against 47 dB) and a 28 MHz LO. F-A buys the same margin with one more passive 3-pole section that draws no current, and the LO choice belongs to ADR-013.

F-B is no better than F-A on any R2 criterion and worse on C4 and C6, so it is pruned as dominated. Confidence: Medium for the structural argument, Low for the current figure.

**R2 selectivity (inside F-A).** The current baseline is concept section 7.3, which carries both candidates. A do-nothing alternative is not applicable because the radio needs a CW channel filter.

| ID | Alternative | Description | Source |
|---|---|---|---|
| A | Commercial 8-pole crystal filter superhet | Inrad #111 (400 Hz, 9.0106 MHz, 8 poles, shape factor 2.0), between a post-mixer amplifier and an IF amplifier with analog AGC. Product detector with the synthesizer as BFO. Firmware does keyer, sidetone, BFO and display only. KVG XF-90S52-LF (1.0 kHz, 9.000 MHz) does not meet REQ-SYS-024 (section 4, M1) and stays in A only as a quote item for a 400 to 600 Hz KVG type | `cw-selectivity-options.md` F2, F3, implication 12 |
| B | Roofed DSP back end | Tolerance-designed 4-pole 1.0 kHz ladder from +/-30 ppm SMD crystals, fixed-gain IF, product detector, PCM1808 24-bit ADC at 48 kS/s over PIO I2S, DSP band-pass 250/500/1000 Hz with digital AGC and sidetone mixing | `cw-selectivity-options.md` F8, F12, F13, implication 12, 13 |

R2 alternatives pruned before scoring, with reason (`cw-selectivity-options.md` F18 and implications 6, 8; concept section 11.1):

- 500 Hz ladder from catalogue crystals: fails M1 in practice, with Monte Carlo strict yield of 14.5 % (4-pole) and 0 % (6-pole) (F8).
- RP2350 12-bit ADC as the audio sampler: its 60 to 70 dB practical in-channel range forces analog AGC ahead of the ADC, and so pumping (F11, F13); this is RSK-037.
- Op-amp audio filter alone: nothing protects the detector or AGC (F15).
- I/Q at 144 MHz: F-C above; SoftRock-VHF I/Q is the documented fallback if crystals and cans both become unobtainable (F17).

Sub-choices carried inside A and B rather than scored:

- IF of 9.000, 9.0106 or 10.7 MHz, chosen with the filter purchase (implication 14).
- Roofing bandwidth 1.0 kHz for B (implication 13).
- Front-end LNA, low-current stage against a 0.5 dB NF MMIC (package decision 55): section 8.4.

**P PA device and topology.** The current baseline is the Mitsubishi RD07MUS2B line-up of `pa-device-candidates.md` implication 5 (P0), superseded in the research by the SI-028 follow-up. Every candidate that `pa-turnkey-candidates-followup.md` F16 found at 5 W or more in any authorized catalogue is listed:

| ID | Alternative | Description | Source |
|---|---|---|---|
| P0 | Mitsubishi RD01MUS2B driver + RD07MUS2B final, direct 2S, gate-bias ALC (prior research baseline) | Measured VHF harmonics (AN-VHF-053-A); consigned parts only | `pa-device-candidates.md` F3, F4, F7, F21 |
| P1 | ST PD54008L-E final, direct from the protected pack (6.0 to 8.4 V), VAPC gate-bias ALC and envelope; STEVAL-TDR003V1 match, bias network and 7-element elliptic LPF re-tuned to 144 to 148 MHz; stocked 5 V MMIC driver in place of the obsolete PD84001 | Only 7 V-class device at 5 W or more in volume production and stocked at two turnkey distributors | followup F2 to F9, F20, implication 1 |
| P2 | Guerrilla RF GRF5604 on a dedicated 5.0 V, 3 A buck rail, drive-level ALC and envelope | 36 dB two-stage InGaP HBT, no driver; 460 MHz reference tune only | followup F12 to F15, implication 2 |
| P3 | ST PD55015-E on a 12.5 V boost rail (TPS61088 class) | ST 155 to 165 MHz board at 20 V and 30 W to re-tune | followup F6, F17 (b), F18, F19 |
| P4 | ST PD55008-E on a 12.5 V boost rail | Small-signal S-parameters from 100 MHz; no VHF circuit | followup F17 (a), F18, F19 |
| P5 | NXP AFT05MS004N on its datasheet 136 to 174 MHz reference circuit | End of life, finite authorized stock | followup F10, F11; `pa-device-candidates.md` F10 |
| P6 | Mitsubishi RA07M1317M module | Guaranteed harmonics; flange module | `pa-device-candidates.md` F8 |

P alternatives pruned before scoring, with reason:

- NXP AFT05MS006N and AFT09MS007N: no authorized stock (F9, F12 of `pa-device-candidates.md`); screened with P5.
- NXP AFT05MS003N: "no longer manufactured (discontinued)" and a 3.2 W part, below 5 W; the only stock found is Rochester Electronics priced per 10,000 (followup F10).
- NXP AFIC901N: a 1 W driver-class part, factory order only (F11 there).
- ST PD55003-E: 3 W P1dB, too small for 5 W with margin (followup F17 (c)).
- NXP MRF1513NT1: no longer manufactured (F17 (d)).
- Renesas RQA0009 and Toshiba 2SK3476: obsolete or not for export (F15 there).
- Ampleon, MACOM, Qorvo, CEL: no 7 V VHF device in their catalogues (F15 there; followup F16). Infineon, Microchip and Toshiba were not swept parametrically (Low confidence, followup F16); this is a limitation in section 6 item 6.

### 3.3 Weight rationale

Weights derive from the MOEs each criterion measures and the KDRs it moves. A criterion that moves a KDR together with an MOE gets 15 to 20; one that moves a single KDR or a top register risk gets 10; cost and envelope fit get 5 because the differences they measure are small against their allocations (REQ-SYS-147 USD 610; REQ-SYS-103 40 mm). Four rows depart from the rule, each with its reason in the table: R2 C2, R2 C4, P C3 and P C5 (revision 1, INSP-013 finding-5). With R2 C4 at 15 the R2 totals become A 339.4 and B 303.9; with P C3 and P C5 at 15 the P totals become P1 458.8, P3 276.2 and P4 263.1 (the other weights rescaled; Appendix A.3). No rank changes. The owner set no weight directly.

| Decision | Criterion | Weight | Driving MOE, KDR, stakeholder input or risk |
|---|---|---|---|
| R2 | C1 adjacent-signal protection | 20 | MOE-010 is this criterion; REQ-SYS-026, REQ-SYS-029, REQ-SYS-030 |
| R2 | C2 sensitivity cost | 10 | REQ-SYS-022 (KDR); MOE-001, MOE-010. Weighted below C1 because the filter sits after the post-mixer amplifier, so its loss moves system NF only weakly |
| R2 | C3 repeatability | 15 | MOE-003; REQ-SYS-137 (KDR); SI-019 (units for friends) |
| R2 | C4 receive current | 10 | MOE-004; REQ-SYS-094 (KDR); TPM-002 is red and RSK-058 is Proposed at score 12. Exception to the KDR-plus-MOE rule: the selectivity block is a small part of the receive draw, which the LO, LNA and backlight choices dominate (180 to 420 mA on the 5 V bus across the `power-tree-and-charging.md` F23 builds, against a 17.5 mA difference between the A and B midpoints, `cw-selectivity-options.md` F18), and both cells are Low-confidence estimates, so it is weighted as a single-KDR criterion |
| R2 | C5 firmware scope | 15 | Schedule dimension: RSK-013 (rustos driver effort). Every added driver carries Class A evidence (07 section 19 closure rule) |
| R2 | C6 first-power-on confidence | 10 | MOE-003; SI-010; RSK-008 |
| R2 | C7 unit cost | 5 | MOE-007; REQ-SYS-147 |
| R2 | C8 supply depth | 10 | REQ-SYS-140 (KDR); RSK-038 |
| R2 | C9 envelope fit | 5 | MOE-013; REQ-SYS-103 (KDR) |
| P | C1 harmonic data | 20 | MOE-006; REQ-SYS-017 and REQ-SYS-018 (KDR); the 06 section 7 regulatory rule scores any 97.307 departure at 4 or more |
| P | C2 matching and model maturity | 20 | MOE-003; REQ-SYS-012 (KDR); RSK-001, RSK-008; the schedule of the PA design |
| P | C3 DC input | 10 | MOE-004; REQ-SYS-094 (KDR); TPM-002. Exception to the KDR-plus-MOE rule: the surviving candidates span 10.0 to 10.1 W at their midpoints (section 4), 0.1 W against the 3 W span of the scale anchors, so the criterion barely discriminates and is weighted as a single-KDR criterion |
| P | C4 thermal margin | 10 | REQ-SYS-112 (KDR); HZ-003; RSK-006 |
| P | C5 receiver compatibility | 10 | MOE-010; REQ-SYS-022 (KDR); RSK-040. Exception to the KDR-plus-MOE rule: the criterion scores a risk to REQ-SYS-022 (switcher spurs), not a measured degradation, and that risk is also carried by RSK-040 with its converter-off-in-receive mitigation, so it is weighted as a top-register-risk criterion |
| P | C6 unit cost | 5 | MOE-007; REQ-SYS-147 |
| P | C7 supply depth and lifecycle | 10 | REQ-SYS-140 (KDR); SI-028; RSK-005, RSK-038 |
| P | C8 level control and envelope | 10 | REQ-SYS-011, REQ-SYS-012 (KDR), REQ-SYS-014; HZ-008 |
| P | C9 mismatch ruggedness | 5 | REQ-SYS-013, REQ-SYS-152; RSK-031. Weighted low because REQ-SYS-013 asks only 10:1 and decision 60 may add SWR fold-back |

### 3.4 Evaluation methods

| Criterion | Method | Tool and version (`tools/toolchain.lock.md`) | Evidence artifact |
|---|---|---|---|
| R2 C1, C2, C3 | Datasheet comparison (A); LTspice Monte Carlo, 200 runs per case (B) | LTspice 26.0.2 through CrossOver wine; spicelib 1.6.3; no TV record yet (H12) | `docs/research/cw-selectivity-options.md` F2, F3, F7, F8; `docs/research/sim/cw-selectivity/out/mc_*.json`; `docs/research/figures/cw-selectivity/mc_*.png` |
| R2 C4 | Research estimate | none | `cw-selectivity-options.md` F18 (Low) |
| R2 C5 | Count against the rustos work-package list | none | `cw-selectivity-options.md` F14; `docs/process/07-software-engineering-plan.md` section 19 |
| R2 C6 | Evidence-class assessment | none | `cw-selectivity-options.md` F18 row "Risk to first power-on", implications 16 to 18 |
| R2 C7, C8 | Vendor page and distributor snapshot, 2026-09-25 | web fetch by the research agent | `cw-selectivity-options.md` F2, F3, F5, F12 |
| R2 C9 | Case drawing | none | `cw-selectivity-options.md` F2 (KVG BF-01) |
| P C1, C2, C8, C9 | Datasheet, application-note and evaluation-board comparison | pdftotext; graph reads at 100 dpi | `pa-turnkey-candidates-followup.md` F3 to F7, F12, F15, F17; `pa-device-candidates.md` F3, F4 |
| P C3, C4 | Derived budget from vendor curves | Python arithmetic by the research agent | followup F9, F15, F19; `power-tree-and-charging.md` F23 |
| P C5 | Topology inspection | none | followup F9, F15, F19; `power-tree-and-charging.md` F17, F22 |
| P C6, C7 | Distributor snapshot, 2026-09-25 17:29 to 17:44 UTC | OEMsTrade aggregator with distributor attribution; DigiKey keyword pages | followup F8, F14, F17, F18, F20 |
| Sensitivity (section 6) | Recomputation of totals under the 06 section 14.4 perturbations | Python 3 script of Appendix A.3 with the project venv interpreter | Appendix A.3 |

### 3.5 Setup matrix (before scoring)

| Criterion (R2) | Weight | A | B |
|---|---|---|---|
| M1 | n/a | | |
| M2 | n/a | | |
| M3 | n/a | | |
| C1 | 20 | | |
| C2 | 10 | | |
| C3 | 15 | | |
| C4 | 10 | | |
| C5 | 15 | | |
| C6 | 10 | | |
| C7 | 5 | | |
| C8 | 10 | | |
| C9 | 5 | | |

| Criterion (P) | Weight | P0 | P1 | P2 | P3 | P4 | P5 | P6 |
|---|---|---|---|---|---|---|---|---|
| M1 | n/a | | | | | | | |
| M2 | n/a | | | | | | | |
| M3 | n/a | | | | | | | |
| M4 | n/a | | | | | | | |
| M5 | n/a | | | | | | | |
| C1 | 20 | | | | | | | |
| C2 | 20 | | | | | | | |
| C3 | 10 | | | | | | | |
| C4 | 10 | | | | | | | |
| C5 | 10 | | | | | | | |
| C6 | 5 | | | | | | | |
| C7 | 10 | | | | | | | |
| C8 | 10 | | | | | | | |
| C9 | 5 | | | | | | | |

## 4. Scoring rationale

Mandatory screening, R2:

| Alternative | M1 | M2 | M3 | Result |
|---|---|---|---|---|
| A | **conditional pass**: Inrad #111 is 400 Hz nominal at -6 dB with shape factor 2.0, so about 0.8 kHz at -60 dB (F3). 400 Hz is exactly the lower limit of REQ-SYS-024 (400 to 600 Hz, TBR), and the #111 bandwidth tolerance and termination impedance are not quoted (F3 open item). The pass holds if the Inrad quote (package decision 101; `cw-selectivity-options.md` ACTION 15) states at least 400 Hz at -6 dB over tolerance, or if the owner moves the REQ-SYS-024 lower limit by CR at the PDR TBR closure. KVG XF-90S52-LF is 1.0 kHz at -6 dB (F2) and does not meet REQ-SYS-024. The optional Hi-Per-Mite-class audio filter of implication 12 is a 250 Hz narrow position after the detector (200 Hz at 3 dB, F15), not a route from the 1.0 kHz can to a 400 to 600 Hz channel; a 500 Hz audio filter would be a design outside the research and would leave the AGC exposed to the 1.0 kHz passband (the exposure C1 measures). Revision 1 corrects the implication-12 reading of revision 0 (INSP-013 finding-1) | pass: a through-hole can soldered by the owner (SI-031; PCBWay THT service also possible, F2). REQ-SYS-140 binds turnkey-placed parts, and the can is not one | pass: no hazard | kept, conditional on M1 |
| B | pass: DSP sets the 500 Hz channel and more than 100 dB inside the roof. The 1.0 kHz roof gives -60 dB at 6.4 kHz, so the -60 dB bandwidth of REQ-SYS-025 is met by the DSP filter rather than by the crystal (F8, F18) | pass: SMD crystals, no matching, 98.5 % strict yield (F8); PCM1808 in 14-TSSOP, turnkey (F12) | pass: no hazard | kept |

Mandatory screening, P:

| Alternative | M1 | M2 | M3 | M4 | M5 | Result |
|---|---|---|---|---|---|---|
| P0 | **fail**: no authorized-distributor stock of RD07MUS2B, RD01MUS2B or RD08MUS2; consignment only (`pa-device-candidates.md` F7, F21; followup F16) | pass (F4, F18 there) | pass | pass | not assessed (dropped at M1) | dropped |
| P1 | pass: final Active, Mouser 3,430 and DigiKey 1,988 at MOQ 1 (followup F2, F8); driver Mini-Circuits GVA-84+, Mouser 2,754 and DigiKey 2,016 cut tape, or PGA-103+, Mouser 4,419 (F20) | **conditional pass**: STEVAL-TDR003V1 reaches 4.5 to 5.0 W at 6.0 V with 10 dBm drive and 5 W at 7.2 V, so gate-bias ALC can hold 5.0 W over 6.4 to 8.4 V (F5, graph read). That line-up used the PD84001 driver, which is no longer available (F5). The stocked 5 V drivers are +21 to +22 dBm P1dB parts, marginal if the final has only 14 to 17 dB of gain at 144 MHz (F20; the gain range is inferred there and unverified). The pass holds subject to the driver gain budget of TS-003 at PDR (followup ACTION 18); GRF5504 is the stocked higher-power driver (F14, F20) and PD54003L-E has no stock at MOQ 1 (F20) | pass: PowerFLAT 5x5, MSL 3, SMT; PCBWay confirmation pending (followup ACTION 17) | pass | pass: 45 C plus a 9 to 12 C junction-to-case rise (3 C/W, 3.1 to 4.1 W; F3, F9) gives 54 to 57 C, leaving about 53 C for the case-to-ambient path | kept |
| P2 | pass: Mouser 7,409 at MOQ 1 (F14); no driver stage | pass: 6 W Psat at 5 V on a fixed rail (F12, F15) | pass: QFN-16 3 x 3 mm, SMT | pass: the thermal consequence is safety 3 (section 7), below Red in the safety dimension | **fail**: stage 2 rises about 80 C at 5 W (20 C/W, F12, F15), so Tj is about 125 C with the package base at the 45 C ambient and about 140 C at a 60 C base, above 110 C. No thermal design lowers a junction-to-base rise; P2 re-enters only with a CR raising the REQ-SYS-112 value (TBR, closes at PDR) or with vendor data showing stage-2 dissipation at or below 3.25 W at 5 W out (a 65 C rise at 20 C/W). Added in revision 1 (INSP-013 finding-2) | dropped |
| P3 | pass: DigiKey 376, Mouser 134 plus 573, Arrow 715 (F17 (b)); a GVA-84+ class driver as for P1 (F20) | pass: fixed 12.5 V rail, 15 W device | pass: PowerSO-10RF, SMT | pass | pass, Low: 3 to 5 W dissipated; PD55015-E RthJC is not tabulated in the report, and at the PD55008-E value of 1.8 C/W the rise is 5 to 9 C (F17, F19) | kept |
| P4 | pass: Mouser 1,322, Arrow 1,200, Newark 34 (F17 (a)); driver as P3 | pass: fixed 12.5 V rail, 8 W device | pass: PowerSO-10RF | pass | pass: 1.8 C/W with 3 to 5 W dissipated, a 5 to 9 C rise (F17 (a), F19) | kept |
| P5 | **fail**: End of Life, no PCN or last-time-buy date found, Mouser 72 and Newark 1,519 "until stocks are exhausted"; not "readily sourced" under SI-028 (followup F10, F11). ADR-012 would admit an end-of-life device only with a lifetime reserve and an identified alternate; package decision 58 proposes dropping it | pass | pass | pass | not assessed (dropped at M1) | dropped |
| P6 | **fail**: brokers only (`pa-device-candidates.md` F8) | pass | **fail**: flange module to be screwed to the heat sink before its leads are hand-soldered (F8 there) | pass | not assessed (dropped at M1) | dropped |

Enhancing scores, R2 (evidence cited as `docs/research/cw-selectivity-options.md` F<n> unless another file is named):

| Criterion | Alt. | Measured value and unit | Score | Confidence | Evidence |
|---|---|---|---|---|---|
| C1 | A | At least 60 dB at +/-2 kHz: #111 about 0.8 kHz at -60 dB from shape factor 2.0, so 60 dB is reached at +/-0.4 kHz. The analog AGC sits after the filter and sees only the channel | 5 | Medium (#111 -60 dB width derived from the shape factor; termination impedance unknown) | F3, F18 |
| C1 | B | 39 dB on the worse side (-2 kHz; 46 dB at +2 kHz), 5th percentile of the 1.0 kHz 4-pole ladder ahead of the ADC. An adjacent signal can arrive on either side, so the worse side is scored: 39 dB interpolates to 2.2 between the 1 (30 dB) and 3 (45 dB) anchors. Revision 0 scored the average of the two sides as if it were a range (INSP-013 finding-7) | 2 | Medium (spread assumptions Medium, F8) | F8 table row "4-pole 1.0 kHz", F13 |
| C2 | A | About 7 dB (#111 "500 Hz: < 7 dB"; the legacy KVG XF-9NB 500 Hz type 6.5 dB) | 3 | Medium | F2, F3 |
| C2 | B | 4.8 dB median (3.5 dB p5, 6.6 dB p95) | 4 | Medium | F8 |
| C3 | A | Factory-built can, no hand selection, but the only M1 part (#111) has a nominal -6 dB bandwidth equal to the REQ-SYS-024 lower limit and an unquoted tolerance (F3; open item 1). With a tolerance symmetric about nominal about half the units fall below 400 Hz, the 1 anchor (below 50 %); a quoted minimum of 400 Hz would make it 5. Scored 1 until the quote; the cases 3 and 5 are in section 6 item 5. Revision 0 scored 5 at Medium (INSP-013 finding-1) | 1 | Low (tolerance unquoted) | F3, implication 4 |
| C3 | B | 98.5 % strict yield in 200 runs (95 % interval about +/-1.7 points at that yield); the 500 Hz channel is set by the deterministic DSP filter | 5 | Medium | F8, F9 |
| C4 | A | 25 to 40 mA (IF amplifier, detector); midpoint 32.5 mA | 5 | Low (estimate) | F18 |
| C4 | B | 40 to 60 mA (IF amplifier 10 to 20 mA, PCM1808 14.5 mA, DSP load); midpoint 50 mA | 2 | Low (estimate) | F12, F18 |
| C5 | A | None added: selectivity needs no firmware; the AGC read-out uses the ADC of WP-SW-04 | 5 | High | F18 row "Firmware effort"; 07 section 19 |
| C5 | B | Three drivers (PIO, DMA, I2S receive) that rustos lacks, plus a DSP module (decimation, CW filter, digital AGC, sidetone mixing), `SW-DSP` in concept section 7 | 1 | High | F14; `docs/design/concept.md` section 7 row SW |
| C6 | A | The can is measurable with the NanoVNA at 9 MHz on receipt, before the board order; the analog AGC is simulation evidence | 4 | Medium | F18 row "Risk to first power-on"; implication 16 |
| C6 | B | DSP is HostUnit-testable with recorded IF audio; PIO I2S is untested on rustos and the loopback of implication 18 is not done; the ladder rests on an unaccredited LTspice flow | 3 | Medium | F14, F18; implications 16, 18 |
| C7 | A | USD 118 (Inrad #111 product page, 2026-09-25); KVG unquoted | 1 | Medium | F3 |
| C7 | B | Four crystals at about USD 0.3 to 1 each plus PCM1808 at USD 0.57 (LCSC, 10 pieces); about USD 2 to 5 | 5 | Low (crystal price from search snippets only, open item 10) | F12; open item 10 |
| C8 | A | One source for the M1 path: Inrad #111, stock not shown, one item in the line discontinued (F3). KVG is quote-only and its current sheet has no 400 to 600 Hz type (F2), so it no longer counts as a second source. Revised from 2 in revision 1, as a consequence of the M1 correction; a KVG quote for a 500 Hz type would make it 2 or 3 | 1 | Medium | F2, F3; implication 7 |
| C8 | B | Commodity crystals from ECS and Abracon; PCM1808 28,195 at LCSC and reported at DigiKey; TI store out of stock on the day; second-source ADC chosen at PDR | 4 | Medium | F5, F12; implication 9 |
| C9 | A | Inrad #111 case dimensions unknown (F3 open item 1); the KVG BF-01 8-pole 9 MHz can, 19.4 mm tall, is taken as the class value | 1 | Low (Inrad case open item 1) | F2, F3 |
| C9 | B | SMD HC-49/US crystals and a 14-TSSOP; heights not tabulated in the report | 5 | Low | F10 (a), F12 |

Enhancing scores, P (evidence cited as `docs/research/pa-turnkey-candidates-followup.md` F<n> unless another file is named). P2 fails M5 and is not totalled in section 5; its rows are kept for the re-entry case of section 8.3:

| Criterion | Alt. | Measured value and unit | Score | Confidence | Evidence |
|---|---|---|---|---|---|
| C1 | P1 | Harmonics -70 dBc maximum at 5 W with ST's 7-element elliptic LPF (STEVAL-TDR003V1 Table 3) | 5 | High | F5 |
| C1 | P2 | No harmonic specification anywhere | 1 | High | F12, F15 |
| C1 | P3 | None on the device; the ST 155 to 165 MHz board data (20 V) states no harmonics | 1 | High | F6, F17 (b) |
| C1 | P4 | None | 1 | High | F17 (a) |
| C2 | P1 | Complete ST 135 to 175 MHz, 7.2 V two-stage reference design (schematic, BOM, Gerbers, measured gain, current and efficiency at 5, 6 and 7.2 V); the PD84001 driver is obsolete and must be replaced; ADS model only | 4 | High | F5, F7, F20 |
| C2 | P2 | 450 to 470 MHz reference tune only; 144 MHz is a custom tune on request, with a 5 to 10 % fractional bandwidth so the UHF tune cannot be reused | 1 | High | F12, F15 |
| C2 | P3 | Active ST board at 155 to 165 MHz but 20 V and 30 W; needs a 12.5 V, 5 W re-tune | 3 | Medium | F6, F17 (b) |
| C2 | P4 | Small-signal S-parameters from 100 MHz; large-signal impedances only at 480 to 520 MHz; no VHF circuit | 2 | Medium | F17 (a) |
| C3 | P1 | 9.6 to 10.6 W at 47 to 52 % PAE; midpoint 10.1 W | 4 | Medium | F9 |
| C3 | P2 | About 10 W into the 5 V rail at about 50 % PAE, plus buck loss at the 0.90 efficiency the power budget assumes: about 11.1 W from the pack | 2 | Low (PAE at 5 W and buck efficiency both assumed) | F15; `power-tree-and-charging.md` F23 |
| C3 | P3 | 9.1 to 10.9 W from the pack including 0.55 to 0.87 W converter loss; midpoint 10.0 W | 4 | Low (converter efficiency estimated, not in the datasheet curves) | F19 |
| C3 | P4 | Same derivation as P3 | 4 | Low | F19 |
| C4 | P1 | 9 to 12 C rise at 3 C/W with 3.1 to 4.1 W dissipated | 5 | Medium | F3, F9 |
| C4 | P2 | About 80 C rise in stage 2 at 20 C/W with about 5 W dissipated; Tj about 140 C at a 60 C base | 1 | Medium | F12, F15 |
| C4 | P3 | Dissipation 3 to 5 W; PD55015-E RthJC not tabulated in the report (the smaller PD55008-E is 1.8 C/W) | 5 | Low | F17 |
| C4 | P4 | 1.8 C/W with 3 to 5 W dissipated: 5 to 9 C | 5 | Medium | F17 (a), F19 |
| C5 | P1 | No new switcher; PA on the protected pack | 5 | High | F9; `power-tree-and-charging.md` F17 |
| C5 | P2 | A 3 A, 5 V buck stage that must hold overshoot below 5 % against a 5.25 V absolute maximum; about 10 W, can be off in receive | 3 | Medium | F15 |
| C5 | P3 | An 18 W boost switcher at 0.5 to 2.2 MHz on the receiver board: off in receive, pre-charged before key-down, ripple appears as AM sidebands, harmonics as birdies | 1 | High | F19 |
| C5 | P4 | Same converter as P3 | 1 | High | F19 |
| C6 | P1 | USD 6.16 to 6.63 at 10 pieces plus a GVA-84+ class driver at USD 2.99: about USD 9.4 | 5 | Medium | F8, F20 |
| C6 | P2 | USD 4.59 at 10 pieces, no driver; the 3 A buck parts are not priced in the report | 5 | Low | F14, F15 |
| C6 | P3 | USD 16.79 to 18.63 plus USD 5 to 6 of converter parts plus a driver: about USD 26 | 1 | Medium | F17 (b), F19, F20 |
| C6 | P4 | USD 12.47 plus USD 5 to 6 plus a driver: about USD 21 | 2 | Medium | F17 (a), F19, F20 |
| C7 | P1 | Mouser 3,430 (137 times the 25-piece project quantity) and DigiKey cut tape 1,988 (80 times), both at MOQ 1. This scores above the 3 anchor, but short of 5 for two reasons: it is a 2007 part with NRND and obsolescence signals in its family (STEVAL-TDR003V1 NRND, PD84001 driver obsolete), and DigiKey is below 100 times | 4 | Medium | F2, F5, F8; implication 9 |
| C7 | P2 | One distributor at MOQ 1 (Mouser 7,409, 296 times); Verical only at MOQ 1,500; DigiKey none; new product (datasheet Release 0, 2024) | 3 | Medium | F12, F14 |
| C7 | P3 | DigiKey 376, Mouser 707, Arrow 715: three at 10 times or more, none of the three at 100 times at MOQ 1 in a single line | 3 | Medium | F17 (b) |
| C7 | P4 | Mouser 1,322 and Arrow 1,200 at 10 times or more; Newark 34 | 3 | Medium | F17 (a) |
| C8 | P1 | ST's own VAPC gate-bias node (4 to 5 V at 5 W) serves ALC and envelope; vendor-characterized | 5 | High | F5 |
| C8 | P2 | Drive-level control only (shutdown switches in microseconds, too fast for a 5 ms envelope); one added element (exciter level or PIN attenuator); VCC steps are coarse | 3 | Medium | F15 |
| C8 | P3 | Gate bias or converter-feedback power control; neither characterized at VHF | 4 | Low | F19 |
| C8 | P4 | As P3 | 4 | Low | F19 |
| C9 | P1 | 20:1 all phases (datasheet; STEVAL load mismatch 20:1) | 5 | High | F3, F5 |
| C9 | P2 | Input limited to 6 dBm into a 3.5:1 mismatch (absolute maximum) | 2 | High | F12 |
| C9 | P3 | 20:1 (ST board) | 5 | High | F6 |
| C9 | P4 | 20:1 at 15.5 V | 5 | High | F17 (a) |

## 5. Final decision matrix

Weighted score = weight x score; maximum 500; percent = total / 5.

**R2 selectivity** (revision 1 cells: A-C3 5 to 1, A-C8 2 to 1, B-C1 3 to 2):

| Criterion | Weight | A score | A weighted | B score | B weighted |
|---|---|---|---|---|---|
| C1 | 20 | 5 | 100 | 2 | 40 |
| C2 | 10 | 3 | 30 | 4 | 40 |
| C3 | 15 | 1 | 15 | 5 | 75 |
| C4 | 10 | 5 | 50 | 2 | 20 |
| C5 | 15 | 5 | 75 | 1 | 15 |
| C6 | 10 | 4 | 40 | 3 | 30 |
| C7 | 5 | 1 | 5 | 5 | 25 |
| C8 | 10 | 1 | 10 | 4 | 40 |
| C9 | 5 | 1 | 5 | 5 | 25 |
| **Total** | **100** | | **330** | | **310** |
| **Percent of maximum** | | | 66 % | | 62 % |
| **Rank** | | | 1 | | 2 |

**P PA device and topology** (P0, P5 and P6 dropped at M1, P2 at M5):

| Criterion | Weight | P1 score | P1 weighted | P3 score | P3 weighted | P4 score | P4 weighted |
|---|---|---|---|---|---|---|---|
| C1 | 20 | 5 | 100 | 1 | 20 | 1 | 20 |
| C2 | 20 | 4 | 80 | 3 | 60 | 2 | 40 |
| C3 | 10 | 4 | 40 | 4 | 40 | 4 | 40 |
| C4 | 10 | 5 | 50 | 5 | 50 | 5 | 50 |
| C5 | 10 | 5 | 50 | 1 | 10 | 1 | 10 |
| C6 | 5 | 5 | 25 | 1 | 5 | 2 | 10 |
| C7 | 10 | 4 | 40 | 3 | 30 | 3 | 30 |
| C8 | 10 | 5 | 50 | 4 | 40 | 4 | 40 |
| C9 | 5 | 5 | 25 | 5 | 25 | 5 | 25 |
| **Total** | **100** | | **460** | | **280** | | **265** |
| **Percent of maximum** | | | 92 % | | 56 % | | 53 % |
| **Rank** | | | 1 | | 2 | | 3 |

For the re-entry case only, P2's section 4 cells total 195 (39 %), or 275 if Guerrilla RF supplies a 144 MHz tune with harmonic data (C1 and C2 each from 1 to 3); neither total makes P2 eligible while it fails M5.

## 6. Uncertainty and sensitivity statement

Computed with the script of Appendix A.3. The fallback order of P was also computed with P1 removed, because package decision 58 asks the owner to name a fallback.

1. **Weight sensitivity.** Each weight was moved by +10 and -10 points, clamped at 0, with the others rescaled proportionally to sum to 100.
   - R2: seven perturbations put B first: C1 -10 (B by 15.0), C3 +10 (29.4), C4 -10 (11.1), C5 -10 (24.7), C7 +10 (24.2), C8 +10 (15.6) and C9 +10 (24.2). Among the others the smallest lead of A is 6.7 points (C2 +10).
   - P: no perturbation changes the top rank; the smallest lead of P1 is 152.5 points (C1 -10).
   - P fallback set (P3, P4): no single weight perturbation changes the top rank. The lead of P3 over P4 falls to 2.9 points at C6 +10.
2. **Score sensitivity.** Each Low-confidence cell was moved by +1 and -1.
   - R2 (cells A-C3, A-C4, B-C4, B-C7, A-C9, B-C9): no single-cell change of top rank; smallest lead 10 points (A-C4 -1, or B-C4 +1). A-C3 is Low from revision 1; revision 0 tagged it Medium and so left the decisive cell out of this run (INSP-013 finding-1).
   - P (cells P3-C3, P4-C3, P3-C4, P3-C8, P4-C8): no change of top rank; smallest lead 170 points.
   - P fallback set: no single-cell change of top rank; smallest lead 5 points.
   - As an additional check beyond 06 section 14.4, every Low cell was moved against the leader at once. R2 becomes a tie, A 320 and B 320, and P stays P1 460 against P3 300. In the fallback set the order becomes P4 285, P3 250.
3. **Assumptions and their evidence:**
   - Research estimates of receive current (F18, Low) stand in for the PDR budget.
   - The Inrad #111 -60 dB width is taken from its shape factor, and its -6 dB tolerance is taken as symmetric about the 400 Hz nominal until quoted (A-C3, A M1).
   - The F-A image rejection rests on an ideal lossless Butterworth front-end model (section 3.2, Low).
   - The P1 driver is a stocked 5 V MMIC whose drive margin depends on an unverified 14 to 17 dB final gain (followup F20).
   - The ladder spread model (Cm sigma 3 %, Rs 8 to 30 ohm) is an informed estimate (F8, Medium).
   - The STEVAL-TDR003V1 curves are graph reads (followup F5, Medium) and ST's circuit is assumed to transfer to the cwht layout after re-tuning.
   - Stock and prices are the 2026-09-25 aggregator snapshot (followup method item 4).
   - GRF5604 PAE at 5 W and the buck efficiency are assumed (F15; power-tree F23).
   - The project quantity for C7 is 25 pieces (5 units plus the 20-piece reserve of followup implication 9).
4. **Robustness verdict:** R2 is **Not robust**: the seven weight perturbations of item 1 put B first, and A leads by 20 points, inside the 25-point closeness rule of 06 section 14.5, so A and B are presented as closely ranked (section 8.3). Revision 0 declared R2 Robust at A 400 against B 330; the change comes from the three corrected cells (A-C3, A-C8, B-C1). P is Robust for the primary: P1 stays first under every perturbation. The P fallback order is **Not robust**: P3 and P4 differ by 15 points, less than the 25-point closeness rule, and the simultaneous Low-cell run puts P4 first. P2 is outside the set because it fails M5 (section 4).
5. **Value of information.**
   - R2: the decisive measurement is the Inrad #111 quote with the -6 dB bandwidth tolerance and the termination impedance (`cw-selectivity-options.md` ACTION 15; package decision 101), one vendor request due before PDR. A quoted minimum of 400 Hz sets A-C3 to 5 (A 390 against B 310); a tolerance that leaves about 90 % of units at or above 400 Hz sets it to 3 (A 360); a symmetric tolerance about 400 Hz leaves it at 1 (A 330) and M1 then needs a REQ-SYS-024 CR. A KVG quote for a 400 to 600 Hz type would raise A-C8 to 2 (A 340). The request was not made before this recommendation, so A and B are presented together (section 8.3).
   - R2, other PDR evidence (concept section 11.2), which raises the Medium cells:
     - the case drawing in the same Inrad quote, which moves A-C9;
     - the PIO I2S loopback with a PCM1808 breakout (ACTION 18; package decision 102), which moves B-C6;
     - the bottom-up receive budget (RSK-058 S1), which moves C4;
     - the re-run of the ladder Monte Carlo with measured crystal parameters (ACTION 16).
   - P fallback: the PDR behavioural models of P3 and P4 (followup "What must happen at PDR" item 1). The Guerrilla RF request for a 144 to 148 MHz GRF5604 tune with measured harmonics, VCC transient tolerance and stage-2 dissipation at 5 W (followup ACTION 15) is the only route by which P2 could pass M5 without a CR; it is one email, due before PDR. Neither was performed before this recommendation, so the fallback candidates are presented together (section 8.3).
6. **Limitations of the evaluation methods and tools (SE HB §6.8.1.2.5):**
   - The LTspice ladder model has no PCB strays, leakage or temperature (F9). Its flow has no TV record yet (package H12), so B-C1 to B-C3 rest on an unaccredited tool.
   - Every PA score is datasheet or application-note evidence; no cwht simulation of any PA candidate exists (RSK-001), and the ST model is ADS-only.
   - Graph reads carry about +/-0.3 dB and +/-0.05 A (followup method item 2).
   - Distributor pages were read through an aggregator because DigiKey and Mouser detail pages refused automated fetches.
   - The catalogue sweep for P did not cover Infineon, Microchip and Toshiba parametrically (followup F16, Low).
   - The receive currents are placeholders until the architecture is chosen (`power-tree-and-charging.md` confidence table).
   - The front-end filter figures of R1 come from an ideal Butterworth formula (Appendix A.3, second listing), not a circuit simulation; they carry no component Q, strays or mixer-port leakage.
   - The M5 screen uses vendor thermal resistances (GRF5604: infrared, DC only, on the evaluation board, followup F12) and derived dissipation; the case-to-ambient path is left to the PDR thermal budget.

## 7. Risks and benefits of the surviving alternatives

Scales of `docs/process/06-risk-and-decision-analysis.md` sections 6 to 8 (score = likelihood x maximum consequence; Red at 12 or more).

| Alternative | Risk statement | L | C (driving dimension) | Score / band | Would be entered as |
|---|---|---|---|---|---|
| A | Given the only 9 MHz CW filter meeting the M1 set is the single-source through-hole Inrad #111 with stock not shown, and KVG's current sheet has no 400 to 600 Hz type (`cw-selectivity-options.md` F2, F3), there is a possibility of no filter being obtainable in the project quantity by the CDR order, adversely impacting the RX selectivity block, leading to a redesign onto candidate B and a slip of CDR | 3 | 3 (schedule) | 9 / Yellow | child of RSK-038 |
| A | Given the Inrad #111 nominal -6 dB bandwidth equals the REQ-SYS-024 lower limit of 400 Hz and its tolerance is unquoted (F3), there is a possibility of delivered filters falling below 400 Hz, adversely impacting REQ-SYS-024, leading to a REQ-SYS-024 CR or a move to candidate B | 3 | 3 (performance margin) | 9 / Yellow | new RSK-NNN if A is selected |
| A | Given the Inrad case is undrawn and the KVG class can (BF-01) is 19.4 mm tall (F2, F3), there is a possibility of the can not fitting the 40 mm envelope stack over the PA pedestal and panel parts, adversely impacting REQ-SYS-103, leading to an envelope CR | 2 | 3 (performance margin) | 6 / Yellow | child of RSK-043 |
| B | Given candidate B needs PIO, DMA and I2S drivers that rustos lacks and a DSP module (F14), there is a possibility of those drivers not being demonstrated on hardware before CDR, adversely impacting the receive function and the CDR schedule, leading to a slip of one design iteration | 3 | 3 (schedule) | 9 / Yellow | child of RSK-013 |
| B | Given the fixed-gain window ends near -47 dBm at the antenna (F13) while a friend at 1 km arrives near -39 dBm (F1), there is a possibility of ADC overload within the roofing passband during a nearby contact, adversely impacting MOE-010, leading to distorted audio unless the operator engages a step attenuator | 3 | 2 (performance margin) | 6 / Yellow | new RSK-NNN |
| B | Given the TI store was out of stock of PCM1808 on 2026-09-25 (F12), there is a possibility of the ADC being unavailable at the turnkey order, adversely impacting REQ-SYS-140, leading to a second-source ADC swap | 2 | 2 (schedule) | 4 / Green | child of RSK-038 |
| P1 | Given PD54008L-E dates from 2007 and ST has put its VHF board on NRND and its driver out of production (followup F2, F5), there is a possibility of an NRND notice for the device before the CDR order, adversely impacting the TX line-up, leading to a redesign onto the fallback | 2 | 4 (schedule) | 8 / Yellow | RSK-005 (history entry naming TS-001) |
| P1 | Given ST publishes only an ADS model and cwht's LTspice model will be behavioural (followup F7), there is a possibility of the model mis-predicting gain or harmonic level at 144 MHz, adversely impacting the spurious margin of REQ-SYS-018, leading to a filter change after the first unit is measured | 3 | 4 (performance margin, 06 section 7 regulatory rule) | 12 / Red | RSK-001 (history entry naming TS-001) |
| P1 | Given the STEVAL-TDR003V1 6.0 V result used the obsolete PD84001 driver and the stocked 5 V MMIC drivers reach +21 to +22 dBm P1dB against an unverified 14 to 17 dB final gain at 144 MHz (followup F5, F20), there is a possibility of the drive falling short of 5.0 W at the 6.0 V pack cut-off, adversely impacting REQ-SYS-012 and the ALC headroom of M2, leading to a higher-power driver (GRF5504) and a re-layout of the driver stage at PDR | 3 | 3 (schedule) | 9 / Yellow | RSK-027 (history entry naming TS-001) |
| P1 | Given heat leaves the PowerFLAT package only through its source pad (followup F3, F9), there is a possibility of the via fill or pedestal contact being inadequate, adversely impacting REQ-SYS-112, leading to a thermal fold-back at 5 W | 2 | 3 (safety) | 6 / Yellow | RSK-006 |
| P2 (dropped at M5; row kept for the re-entry case) | Given GRF5604 harmonics and a 144 MHz tune are unpublished (F12, F15), there is a possibility of the raw second harmonic exceeding the 40 dB filter goal's assumption, adversely impacting REQ-SYS-017, leading to a filter redesign or a device change | 3 | 4 (performance margin, regulatory rule) | 12 / Red | new RSK-NNN if selected |
| P2 (dropped at M5; row kept for the re-entry case) | Given stage 2 runs about 80 C above its package base at 5 W (F12, F15), so that the junction reaches about 125 C even with the base at the 45 C ambient, there is a possibility of the junction exceeding the 110 C of REQ-SYS-112 in every 5 W key-down at 45 C ambient, adversely impacting REQ-SYS-112 (KDR) and HZ-003, leading to a CR on REQ-SYS-112 or a power fold-back below 5 W. Likelihood 4: a known deficiency with no mitigation in progress (06 section 6). Consequence 4: a KDR not met (06 section 7); safety 3. Revision 0 stated this as "approaching its limit" at 9 (INSP-013 finding-2) | 4 | 4 (performance margin) | 16 / Red | RSK-006 (history entry) if P2 re-enters |
| P3 | Given an 18 W boost switcher shares the board with a -140 dBm receiver (F19), there is a possibility of switching spurs and AM sidebands appearing in receive or on the carrier, adversely impacting REQ-SYS-022 and REQ-SYS-017, leading to shielding or a layout iteration | 3 | 4 (performance margin, regulatory rule) | 12 / Red | RSK-040 (history entry) |
| P3 | Given ST's VHF board for PD55015-E is at 20 V and 30 W (F6), there is a possibility of the 12.5 V re-tune missing efficiency or stability targets, adversely impacting REQ-SYS-012, leading to an extra design iteration | 3 | 3 (schedule) | 9 / Yellow | RSK-027 |
| P4 | As the P3 converter risk | 3 | 4 (performance margin) | 12 / Red | RSK-040 |
| P4 | Given PD55008-E has no VHF circuit (F17 (a)), there is a possibility of an in-house match missing its targets, adversely impacting REQ-SYS-012, leading to a design iteration | 3 | 3 (schedule) | 9 / Yellow | RSK-027 |

Aggregate risk per alternative (maximum score): A 9, B 9, P1 12, P3 12, P4 12; P2, dropped at M5, would carry 16. No surviving alternative carries a Red safety risk; the Red entries are performance margin under the regulatory rule. Every Red entry has an identified step toward Yellow: the tinySA Ultra verification (ADR-021) and the 40 and 35 dB filter goals for the harmonic risks, and shielding with converter-off-in-receive for P3 and P4.

| Alternative | Benefits beyond the scored criteria |
|---|---|
| A | The classic superhet pattern with the least firmware in the receive path. The 500 Hz channel is shaped before any gain control, and the can can be measured on the owner's NanoVNA before the board order |
| B | Selectable 250, 500 and 1000 Hz bandwidths. The same DSP chain serves a later I/Q back end (F17). Receive audio is available as samples for HostUnit regression with recorded IF audio (F14) |
| P1 | A complete vendor VHF line-up, including a harmonic filter topology with system-level -70 dBc data. The same gate-bias node serves ALC and the keying envelope (concept section 7.2) |
| P2 (dropped at M5) | No driver stage; a fixed rail removes pack droop; vendor applications support offered |
| P3, P4 | A fixed rail removes droop, allows drain-voltage power steps, and gives a higher load impedance for a lower-loss match (F19) |

## 8. Recommendation

### 8.1 Recommended alternatives

- **R1:** family F-A, the single-conversion superhet with an IF near 9 MHz (screening, section 3.2), with at least five front-end resonators ahead of the mixer to reach the 70 dB image rejection of REQ-SYS-033 (Low, PDR evidence item).
- **R2:** A (330, 66 %) and B (310, 62 %) are closely ranked and the ranking is not robust (section 6), so both are presented for the owner's choice (section 8.3). The recommended use of that choice is to carry both into Phase B with A, the highest total, as the planning baseline for the PDR receive budget, `ICD-RX-CTL` draft and cost model.
- **P:** P1, ST PD54008L-E direct from the protected pack with VAPC gate-bias ALC and the STEVAL-TDR003V1 match and LPF re-tuned, with a stocked 5 V MMIC driver, total 460 (92 %). Its M2 pass is conditional on the TS-003 driver gain budget.

### 8.2 Rationale

- **R2:** A leads on the criteria tied to the adjacent-signal MOE and the schedule. It shapes the channel before the AGC, needs no new firmware and draws less current. B leads on repeatability, cost, supply depth and height. Four of A's cells rest on the unquoted Inrad data (M1, C3, C8, C9), so the Inrad quote decides between them: at a quoted minimum of 400 Hz A leads by 80 points; at a symmetric tolerance A needs a REQ-SYS-024 CR to stay eligible.
- **P:** P1 is the highest total and robust. It is the only candidate with vendor VHF harmonic data and a complete vendor VHF circuit, and it adds no converter next to the receiver.

### 8.3 Closely ranked alternatives presented for the owner's choice

**R2.** A (330) and B (310) differ by 20 points, below the 25-point rule of 06 section 14.5, and seven single-weight perturbations put B first. Recommendation: carry both into Phase B with A as the planning baseline, and fix the choice at PDR on the Inrad quote (section 6 item 5). If the quote gives a symmetric tolerance about 400 Hz, A fails M1 unless the owner moves the REQ-SYS-024 lower limit by CR, and B becomes the only eligible candidate.

**P fallback.** P3 (280) and P4 (265) are within 25 points, and the simultaneous Low-cell run reverses them. Recommendation: name the 12.5 V boost with PD55015-E, then PD55008-E (P3, P4), jointly as the fallback candidates, and fix the order at PDR on their behavioural models.

GRF5604 (P2) is not a fallback candidate as REQ-SYS-112 stands. Its stage-2 junction reaches about 125 C with the package base at the 45 C ambient (followup F15), against the 110 C of REQ-SYS-112 (KDR, TBR), and no thermal design lowers a junction-to-base rise. It can return in one of two ways:

- a CR on REQ-SYS-112 at its PDR TBR closure, raising the junction limit to at least 125 C at 45 C ambient with a thermal budget as evidence; or
- Guerrilla RF data showing stage-2 dissipation at or below 3.25 W at 5 W out.

Even then, its total is 195 today and 275 with a vendor 144 MHz tune and harmonic data. This differs from the package decision 58 default, which names GRF5604 as the fallback and the boost path as the reserve. Decision 58 lists REQ-SYS-112 among its affected requirements, so the owner rules with this conflict in view. The research ordering (followup implication 2) weighs the boost's receiver risk above its data maturity; this matrix weighs data maturity (C1, C2 at 40 of 100), and the REQ-SYS-112 screen removes GRF5604 in any case.

### 8.4 SRR interim direction requested of the owner

These rulings go in `docs/reviews/SRR/decision-memo.md`; they are not this study's section 10 decision.

- **Decision 54 (selectivity candidates and the TBR set):** carry A and B into Phase B as the closely ranked pair of section 8.3, with A as the planning baseline, roofing 1.0 kHz for B, the IF chosen with the filter purchase, no 500 Hz ladder and no RP2350 ADC audio; adopt the selectivity TBR set, noting that A's eligibility against the REQ-SYS-024 lower limit depends on the Inrad tolerance quote (package decision 101). This matches the package default and adds the planning-baseline designation and the condition.
- **Decision 55 (front-end current):** plan the lower-current front-end stage (2 to 3 dB NF, about 30 mA) instead of the 0.5 dB NF MMIC at 97 mA. Two reasons, both from the research:
  - A system NF of 7 dB already meets MDS -140 dBm (REQ-SYS-022; `cw-selectivity-options.md` F1; reference report F14).
  - Receive current drives battery life, with TPM-002 red. The F23 builds of `power-tree-and-charging.md` span 19.4 h (low) to 8.3 h (high) of receive-only life, but those rows differ in the LO, the LNA and the backlight together. Changing only the LNA of the low build from 30 mA to the 97 mA MMIC, in the F23 model recomputed here, moves receive-only life from 19.4 h to 14.2 h and the 1:9 life from 13.0 h to 10.4 h.

  The cascade noise budget at PDR confirms the choice; this matches the package default.
- **Decision 58 (PA device, fallback and drop list):** adopt P1 as the primary, as the package default proposes. Name P3 then P4 jointly as the fallback candidates in place of the package default (GRF5604 fallback, boost reserve), because GRF5604 fails the REQ-SYS-112 screen (section 8.3); GRF5604 returns only with a REQ-SYS-112 CR or vendor dissipation data. Send the Guerrilla RF request before PDR anyway (package decision 101), since it answers the dissipation question. Drop list: AFT05MS004N, AFT05MS003N, AFT05MS006N, AFT09MS007N, AFIC901N and all Mitsubishi RD and RA parts (each dispositioned in section 3.2 or 4).

### 8.5 Impacts of adopting the recommendation

- **Requirements to derive at PDR:**
  - an L2 TX device-constraint requirement traced to SI-028 (followup implication 4);
  - L2 RX selectivity requirements refining REQ-SYS-024 to REQ-SYS-030;
  - an L2 TX harmonic-filter requirement including "at least 40 dB from 288 MHz to 1.5 GHz" (followup implication 6);
  - an L2 PA control-interface requirement for the gate-bias node and forward-power sample (followup implication 7);
  - if the Inrad quote gives a tolerance that reaches below 400 Hz and A is kept, a CR on the REQ-SYS-024 lower limit; if GRF5604 is to return as a fallback, a CR on REQ-SYS-112 (section 8.3).

  The requirement ids are allocated by the requirements author, citing this study and its ADR in `source_ids`.
- **Interfaces:**
  - `ICD-RX-CTL` carries demodulated audio and AGC read-out (A), with the I2S option documented until PDR (B).
  - `ICD-TX-PWR` carries the PA rail direct from the protected pack (P1).
  - `ICD-TX-CTL` carries the VAPC-equivalent node.
- **Cost model delta** (`docs/plan/cost-estimate.md`):
  - A is about USD 118 per unit (Inrad list price), against about USD 2 to 5 for B.
  - P1 device plus driver is about USD 9.4 per unit at quantity 10.
  - The 20-piece PD54008L-E lifetime reserve is about USD 125 (followup implication 9).
- **Schedule delta:** none for A. B would add three rustos work packages and a DSP module to FW-B1 and FW-B2.
- **Verification cases to add at PDR:**
  - the front-end filter simulation for the F-A image rejection (section 3.2), feeding TC-SYS-021 at CDR;
  - a Bench receipt case sweeping the purchased filter with the NanoVNA at 9 MHz (A);
  - if B returns, a dev-board PIO I2S loopback with `credit: false`;
  - the existing spurious-emission Bench cases of REQ-SYS-017 and REQ-SYS-018 remain the closing evidence for the PA.
- **Corrective actions if the recommendation is adopted late:**
  - If the filter quotes fail after PDR, switching to B costs the three drivers and the DSP module (one design iteration, RSK-013).
  - If PD54008L-E becomes unavailable after CDR, the fallback named at PDR is laid out against the device-agnostic LPF and driver design (ADR-012).

## 9. Dissent

| Who | Date | Dissent (criteria, weights, scores or recommendation) | How it was addressed |
|---|---|---|---|
| reviewer:trades (INSP-013 dissent D-1) | 2026-09-25 | Agrees the P fallback cannot be ranked today, but holds that once the REQ-SYS-112 conflict is disclosed, GRF5604 can be a fallback only together with a REQ-SYS-112 CR or a thermal design, which makes the package decision 58 default (GRF5604 as the fallback) harder to support than revision 0's joint recommendation suggested | Accepted in revision 1: mandatory M5 drops GRF5604 from the fallback set, section 8.3 states the two routes by which it could return, and section 8.4 decision 58 recommends P3 then P4 in place of the package default |

## 10. Decision

Empty until the owner decides (06 section 14.5; charter section 2).

- **Decision:**
- **Decided by:**
- **Rationale as stated by the owner:**
- **Records produced:**
- **Revisit conditions:**
- **Lessons learned (SE HB sections 6.8.1.2.7 and 6.8.1.3.1):**

## 11. References

- NASA/SP-2016-6105 Rev 2 (SE HB) §6.8, §6.8.1.2.1 to §6.8.1.2.7, Table 6.8-1 (`docs/references/md/nasa-se-handbook/22-6-8-decision-analysis.md`)
- NPR 7123.1D §3.2.18.1 [SE-23]; App. G Table G-3 item 5.2 (`docs/references/md/npr-7123-1d/03-chapter3.md`, `13-appendixg.md`)
- 47 CFR 97.307(e) (corpus: `docs/references/md/regulatory/47cfr-97.307.md`, eCFR issue 2026-09-23)
- `docs/process/06-risk-and-decision-analysis.md` sections 6 to 8, 13, 14; `docs/process/01-lifecycle-and-reviews.md` section 4.3 row 5; `docs/templates/trade-study.md`
- `docs/design/concept.md` sections 5, 7, 10, 11; `docs/reviews/SRR/package.md` section 2 item H5 and section 13.1 decisions 54, 55, 58, 59, 60, 91, 101, 102
- `docs/research/cw-selectivity-options.md` (2026-09-25) with `docs/research/sim/cw-selectivity/` and `docs/research/figures/cw-selectivity/`
- `docs/research/pa-turnkey-candidates-followup.md` (2026-09-25); `docs/research/pa-device-candidates.md` (2026-09-25)
- `docs/research/2m-cw-transceiver-reference-designs.md` (2026-09-25); `docs/research/power-tree-and-charging.md` (2026-09-25)
- ADR-002, ADR-003, ADR-007, ADR-010, ADR-011, ADR-012, ADR-013, ADR-019, ADR-020, ADR-021, ADR-022, ADR-023 (`docs/decisions/adr/`)
- `docs/requirements/sys/requirements.json` (REQ-SYS ids above); `docs/requirements/l0-stakeholder/expectations.json` (MOE ids above); `docs/risk/register.json` (RSK ids above); `docs/safety/hazards.json` (HZ-003, HZ-008)

## Appendix A. Supporting analysis

### A.1 Literature and research search

Claude Context searches over `/Users/robinonsay/rust/cwht` (2026-09-25) were run before any manual search. Queries: "SRR readiness shortfalls H5 trade studies H14 make/buy SWE-033"; "PDR trade studies TS-001 selectivity TS-002 synthesizer TS-003 PA device defined in concept"; "key driving requirements KDR list". They located:

- package section 2;
- concept sections 7 and 11;
- ADR-012 and ADR-013;
- register entries RSK-005 and RSK-058;
- technology assessment section 7;
- the KDR table of the SRR traceability report.

Corpus identifiers were then pinned by `grep` in `docs/references/md/`: SE HB 6.8.1.2.1 to 6.8.1.2.7 and Table 6.8-1; SE-23; App. G Table G-3 item 5.2; 47 CFR 97.307(e). Research reports were read in full: cw-selectivity-options, pa-turnkey-candidates-followup, pa-device-candidates, and the relevant sections of 2m-cw-transceiver-reference-designs and power-tree-and-charging.

### A.2 Previous related decisions and dissent

Concept section 11.1 (18 concept-level alternative sets dispositioned), ADR-012 (sourcing constraint), ADR-013 (synthesizer method) and ADR-022 (harmonic target, proposed). No prior trade study exists; this is the first file in `docs/decisions/trade-studies/`.

### A.3 Detailed analysis: totals and sensitivity script

Run with `/Users/robinonsay/rust/cwht/.venv/bin/python` on 2026-09-25; it prints the totals and every perturbation result quoted in sections 3.3, 5 and 6 of this study and of TS-002. Revision 1 changes cells A-C3 (5 to 1, now Low), A-C8 (2 to 1) and B-C1 (3 to 2), removes P2 from `sP` (it fails M5; its cells are kept as `sP2` for the re-entry case) and adds the report block. It is reproduced here so a reviewer can recompute (CK-RSK-B6):

```python
def totals(w, s):
    return {a: sum(w[c] * s[a][c] for c in w) for a in s}

def rank(t):
    return sorted(t, key=lambda a: -t[a])

def weight_sens(w, s):
    top = rank(totals(w, s))[0]; out = []
    for c in w:
        for d in (+10, -10):
            new = max(0.0, w[c] + d); rest = sum(v for k, v in w.items() if k != c)
            nw = {k: (new if k == c else w[k] * (100 - new) / rest) for k in w}
            t = totals(nw, s); r = rank(t)
            out.append((c, d, r[0], round(t[r[0]] - t[r[1]], 1), r[0] != top))
    return out

def score_sens(w, s, low):
    top = rank(totals(w, s))[0]; out = []
    for (a, c) in low:
        for d in (+1, -1):
            ns = {k: dict(v) for k, v in s.items()}; ns[a][c] = min(5, max(1, s[a][c] + d))
            t = totals(w, ns); r = rank(t)
            out.append((a, c, d, r[0], round(t[r[0]] - t[r[1]], 1), r[0] != top))
    return out

def all_low_against_top(w, s, low):
    top = rank(totals(w, s))[0]; ns = {k: dict(v) for k, v in s.items()}
    for (a, c) in low:
        ns[a][c] = min(5, max(1, s[a][c] + (-1 if a == top else +1)))
    return totals(w, ns)

wR = dict(C1=20, C2=10, C3=15, C4=10, C5=15, C6=10, C7=5, C8=10, C9=5)
sR = {"A": dict(C1=5, C2=3, C3=1, C4=5, C5=5, C6=4, C7=1, C8=1, C9=1),
      "B": dict(C1=2, C2=4, C3=5, C4=2, C5=1, C6=3, C7=5, C8=4, C9=5)}
lowR = [("A", "C3"), ("A", "C4"), ("B", "C4"), ("B", "C7"), ("A", "C9"), ("B", "C9")]
wP = dict(C1=20, C2=20, C3=10, C4=10, C5=10, C6=5, C7=10, C8=10, C9=5)
sP = {"P1": dict(C1=5, C2=4, C3=4, C4=5, C5=5, C6=5, C7=4, C8=5, C9=5),
      "P3": dict(C1=1, C2=3, C3=4, C4=5, C5=1, C6=1, C7=3, C8=4, C9=5),
      "P4": dict(C1=1, C2=2, C3=4, C4=5, C5=1, C6=2, C7=3, C8=4, C9=5)}
lowP = [("P3", "C3"), ("P4", "C3"), ("P3", "C4"), ("P3", "C8"), ("P4", "C8")]
# P2 (GRF5604) fails mandatory M5 (REQ-SYS-112); its scores are kept for the re-entry case only.
sP2 = dict(C1=1, C2=1, C3=2, C4=1, C5=3, C6=5, C7=3, C8=3, C9=2)
wF = dict(C1=20, C2=10, C3=20, C4=10, C5=15, C6=15, C7=10)
sF = {"A0": dict(C1=5, C2=5, C3=1, C4=4, C5=5, C6=5, C7=4),
      "A1": dict(C1=1, C2=2, C3=4, C4=1, C5=3, C6=4, C7=3),
      "A2": dict(C1=1, C2=2, C3=4, C4=1, C5=2, C6=2, C7=3),
      "A3": dict(C1=1, C2=2, C3=4, C4=1, C5=2, C6=2, C7=3)}
lowF = [(a, c) for a in ("A1", "A2", "A3") for c in ("C1", "C3", "C4", "C5", "C6", "C7") if (a, c) != ("A3", "C6")]

if __name__ == "__main__":
    def report(name, w, s, low):
        t = totals(w, s); ws = weight_sens(w, s); ss = score_sens(w, s, low)
        print(name, {k: t[k] for k in rank(t)})
        keep = [x for x in ws if not x[4]]
        print("  weight flips", [x[:4] for x in ws if x[4]], "smallest lead otherwise", min(x[3] for x in keep), [x[:2] for x in keep if x[3] == min(y[3] for y in keep)])
        print("  score flips", [x for x in ss if x[5]], "smallest lead", min(x[4] for x in ss))
        print("  all low vs top", all_low_against_top(w, s, low))
    report("R2", wR, sR, lowR)
    report("P", wP, sP, lowP)
    fb = {k: v for k, v in sP.items() if k != "P1"}
    report("P fallback", wP, fb, lowP)
    for c3 in (3, 5):
        s = {k: dict(v) for k, v in sR.items()}; s["A"]["C3"] = c3; print("R2 A-C3 =", c3, totals(wR, s))
    s = {k: dict(v) for k, v in sR.items()}; s["A"]["C8"] = 2; print("R2 A-C8 = 2", totals(wR, s))
    p2 = dict(fb); p2["P2"] = sP2; print("P2 re-entry today", totals(wP, p2))
    v = dict(sP2); v["C1"] = 3; v["C2"] = 3; p2["P2"] = v; print("P2 re-entry with vendor data", totals(wP, p2))
    report("TS-002", wF, sF, lowF)
```

The weight-15 cases of section 3.3 use the same functions with R2 C4, or P C3 and P C5, set to 15 and the other weights rescaled to sum to 100.

Second listing, the R1 front-end filter figures (ideal lossless Butterworth band-pass, bandpass-to-lowpass mapping x = |f/f0 - f0/f| / (B/f0), attenuation 10 log10(1 + x^(2n))) and the F23 battery-model recomputations of sections 3.2 and 8.4 (the F23 script of `power-tree-and-charging.md` with only the named 5 V bus load changed):

```python
import math
f0 = 146.0; B = 4.0 / ((10**0.1 - 1) ** (1 / 6))    # 3 dB bandwidth from the Anglian 1 dB bandwidth of 4 MHz: 5.01 MHz
def A(f, n=3):
    x = abs(f / f0 - f0 / f) / (B / f0); return 10 * math.log10(1 + x ** (2 * n))
for img in (126, 130, 162, 166, 88, 9.0):             # F-A images (low- and high-side LO), F-B image, 9 MHz IF
    print(img, round(A(img), 1), round(A(img, 5), 1), round(2 * A(img), 1))
V, E, ah = 7.2, 0.9, 2.7                               # F23: 7.2 V nominal, 0.90 buck, 3000 mAh x 90 %
def pack(i5): return i5 * 5 / (V * E)
for name, i5 in (("low", 0.180), ("low + 30 mA", 0.210), ("low, 97 mA LNA", 0.247)):
    irx = pack(i5); itx = irx + 0.150 + 0.45 * 1.20
    print(name, round(ah / irx, 1), round(ah / (0.1 * itx + 0.9 * irx), 1))
```

Results (2026-09-25, revision 1):

| Matrix | Totals | Weight perturbations that change the top rank | Smallest lead under weight perturbation | Low-cell perturbations that change the top rank | All Low cells against the leader |
|---|---|---|---|---|---|
| TS-001 R2 | A 330, B 310 | seven: C1 -10, C3 +10, C4 -10, C5 -10, C7 +10, C8 +10, C9 +10 (B first) | 6.7 among the others (C2 +10) | none (smallest lead 10) | A 320, B 320 |
| TS-001 R2, A-C3 = 3 or 5 (Inrad quote cases) | A 360 or 390, B 310 | not run | not run | not run | not run |
| TS-001 P | P1 460, P3 280, P4 265 | none | 152.5 | none (170) | P1 460, P3 300, P4 285 |
| TS-001 P fallback (P1 removed) | P3 280, P4 265 | none | 2.9 | none (5) | P4 285, P3 250 |
| TS-001 P2 re-entry case (fails M5) | P2 195, or 275 with Guerrilla RF data | not run | not run | not run | not run |
| TS-002 | A0 400, A1 265, A2 220, A3 220 | none | 80.6 | none (115) | A0 400, A1 355, A2 310, A3 295 |

Second listing (2026-09-25): one 3-pole section 56.1, 49.9, 47.0, 52.5, 89.3 and 160.4 dB at 126, 130, 162, 166, 88 and 9 MHz; one 5-pole section 93.5, 83.1, 78.3, 87.5, 148.8 and 267.3 dB; two 3-pole sections 112.2, 99.7, 94.0, 105.0, 178.6 and 320.8 dB. Battery model: low build 19.4 h receive-only and 13.0 h at 1:9; plus 30 mA 16.7 h and 11.7 h; 97 mA LNA 14.2 h and 10.4 h.

### A.4 Decision metrics

- Time from open to recommendation: same day (2026-09-25).
- Alternatives: 4 families (R1), 2 selectivity candidates plus 4 pruned (R2), 7 PA candidates with 4 dropped at screening and 8 pruned (P).
- Criteria: 2 plus 3 plus 5 mandatory; 9 plus 9 enhancing.
- Criteria revisions: 3 in revision 1 (M-R1 widened to admit a front-end filter analysis; P M1 extended to the driver device; P M5 added for REQ-SYS-112).
- Figures: none produced; no render in this study needs visual closure.

## Change log

Revisions before the decision only; after the decision the file is immutable except for the Status line (06 section 14.6).

| Revision | Date | Change | Reason |
|---|---|---|---|
| 0 | 2026-09-25 | Initial | SRR package item H5 (01 section 4.3 row 5) |
| 1 | 2026-09-25 | R2: implication-12 reading corrected, A M1 made conditional on the Inrad tolerance, A-C3 1 (Low), A-C8 1, B-C1 2 (worse side); R2 now A 330, B 310, not robust, closely ranked. R1: M-R1 widened, F-A front-end filter analysis, F-B dominance quantified, Kuhne figure corrected. P: M1 extended to the driver, M5 (REQ-SYS-112) added, P2 dropped at M5, P1 M2 conditional on the driver budget, P1 drive-margin risk added, P2 thermal risk re-rated to 16. Weight exceptions stated; decision 55 and 58 text, RSK-058 status and the drop list corrected; reviewer dissent D-1 recorded | INSP-013 findings F-01 to F-07 |
