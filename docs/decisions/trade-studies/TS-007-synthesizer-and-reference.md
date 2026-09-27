# TS-007: Synthesizer and frequency reference

| Field | Value |
|---|---|
| ID | TS-007 |
| Status | In review |
| Decision class trigger | `docs/process/06-risk-and-decision-analysis.md` section 14.1 class 1, two items. (b) Selection of critical parts: the synthesizer and the TCXO. (c) The choice touches HZ-008 (causes C5, C7, C8; controls K4, K6, K7) and two components of `docs/process/07-software-engineering-plan.md` section 14.1: the SW-SYNTH transmit frequency-word path and the SW-SAFE frequency verification unit, both proposed safety-critical by SRR decision 9. The study therefore also needs the software assurance second review of 07 section 2.1.1 |
| Decision maker | Robin (owner, Decision Authority) |
| Recommender | Claude (author, RF designer TX invocation, WP-PDR-20) |
| Independent reviewer | INSP number assigned by the lead SE, in `docs/reviews/PDR/checklists/ts-007-synthesizer-and-reference.md` (`docs/templates/peer-review-checklist-risk.md` section B). Software assurance pair: `docs/reviews/PDR/checklists/ts-007-synthesizer-and-reference-software-assurance.md`. Both reach APPROVED before the owner decides (PDR work plan rule C9) |
| Decide by | PDR, owner session B1a (Tue 2026-09-29). The allocated baseline fixes the transmitter and receiver frequency-generation architecture, the power budget (TPM-008) and the frequency-control software components |
| Related risks | RSK-002 (step S2 "frequency-stability" artifact), RSK-035, RSK-040, RSK-041, RSK-046 (step S2 "synthesizer" artifact) |
| Related requirements and hazards | REQ-SYS-008, 009, 010, 029, 031, 034, 046, 076, 154, 182; REQ-TX-002, 013; HZ-008; SI-002, SI-028, SI-029, SI-031; TPM-006, TPM-008 |
| Resulting ADR | ADR-030 (provisional number; written after the owner's decision, 06 section 14.2) |
| Dates | opened 2026-09-27; recommended 2026-09-27; decided pending |

## 1. Executive summary

- **Recommendation (one sentence):** Alternative A2. The LMX2571 generates the receive LO and the transmit carrier. The Si5351A-B-GT generates only the BFO. Both share one 25.000 MHz LVCMOS TCXO of the SiT5356 class, which must pass datasheet acceptance test R-M3 (uncalibrated total at most 1.5 ppm). A2 leads because its phase noise at 144 MHz is about 23 dB better than the Si5351A's (section 4, C1) and its spurious output is specified. The price difference lies within the owner's USD 15 "similar cost" band (SI-029, ADR-013, SRR decision 56).
- **Problem requiring a decision (one sentence):** which synthesizer and which reference oscillator generate the 144 MHz LO, the transmit carrier and the BFO, given the phase-noise, band-edge, battery-life and safety constraints?
- **Robustness verdict (section 6):** Robust for the synthesizer choice. The reference part is decided as an acceptance test plus a preferred class. Section 8 names the part when a datasheet shows it passes.
- **Owner's decision (section 10):** pending.

**Scope and the merge of two planned artifacts.** The risk register names two separate study artifacts:
- RSK-002 step S2 names `TS-NNN-frequency-stability.md`: reference grade, filter bandwidth and receiver incremental tuning.
- RSK-046 step S2 names `TS-NNN-synthesizer.md`: the ADR-013 study with the frequency error budget.

One study covers both (PDR work plan WP-PDR-20), for two reasons. First, the reference grade and the synthesizer are coupled: the LMX2571 loses about 5 dB of phase noise with a clipped-sine reference (reference report F20), and the Si5351A takes only a 25 or 27 MHz reference (F16). Second, one frequency error budget serves both risks (`docs/design/analysis/frequency-budget.md`).

The other two items of RSK-002 step S2 are decided elsewhere, not dropped:
- the CW filter bandwidth is TS-001's selectivity decision (WP-PDR-19);
- receiver incremental tuning is a software requirement (RSK-002 step S3, WP-PDR-35).

## 2. Problem and decision context

- **Mission and system context.** Frequency generation belongs to TX (SRR decision 56: "TX owns frequency generation"). It feeds three consumers:
  - the receiver LO of the single-conversion superhet near 9 or 10.7 MHz IF (TS-001 family F-A);
  - the BFO or second LO of either selectivity candidate (TS-001 A: product detector with "the synthesizer as BFO"; B: second conversion ahead of the PCM1808);
  - the transmit carrier.

  The scenarios served are OPS-003 (receive) and OPS-020 (transmit near the band edges). The MOE is MOE-010, weak-signal reception. The frequency word and the verification unit are safety-critical by SRR decision 9 (HZ-008 C7).
- **Decision needed and intended outcome.** After the decision:
  - the preliminary design has one synthesizer line-up and one reference class;
  - the TX and CTL L2 files can state the synthesizer interface (I2C, SPI, GPIN sample);
  - rustos knows which bus drivers carry safety-critical traffic (07 WP-SW-05, WP-SW-06, WP-SW-14);
  - the frequency TBRs of group G2 close on one design.
- **Constraints.**
  - SI-029: cost and performance trade; best performer if costs are similar.
  - ADR-013 decision rule and SRR decision 56 confirm the USD 15 band and name phase noise and tuning clicks as criteria.
  - ADR-012 and SI-028: DigiKey or Mouser stock.
  - SI-031: turnkey-placeable surface-mount parts.
  - ADR-023: TCXO of +/-2.5 ppm or better, independent of the Pico 2 crystal.
  - REQ-SYS-008 to 010: guard and tolerance.
  - REQ-SYS-029 and 031: close-in phase noise.
  - TPM-008: battery life of 8 h at 1:9 (ADR-020).
  - REQ-SYS-182: an independent counter of the carrier.
- **Prior decisions and lessons.**
  - ADR-013 (method), ADR-023 (reference ceiling and guard), ADR-026 (semi break-in, 12 ms lead-in), ADR-016 (full band).
  - TS-001 section 8 (family F-A, selectivity A or B open; IF 9.000, 9.0106 or 10.7 MHz, chosen with the filter purchase).
  - SRR decisions 25, 40, 56.
  - Lesson L5 of the PDR work plan: every case named.
- **Research consulted.**
  - `docs/research/2m-cw-transceiver-reference-designs.md` F16 to F21, Table 2, implications 9 and 14, confidence table, open items 1, 2 and 11.
  - `docs/research/power-tree-and-charging.md` F23 (battery-life model).
  - `docs/research/audio-output-and-hearing-safety.md` F11 (tuning clicks).
  - `docs/research/display-and-ui-parts.md` F10 (clock harmonics).
  - `docs/research/regulatory-corpus-and-operators.md` F7, F8.
  - RP2350 datasheet sections 8.1.3 and 8.2.1.1 (rustos `docs/extracted/rp2350-datasheet.md` at commit `2ec64c0f`, read with `git show`).

## 3. Decision matrix setup and rationale

### 3.1 Criteria and operational definitions

**Part A: synthesizer.** Mandatory criteria are pass or fail (SE HB section 6.8.1.2.1).

| ID | Criterion | Type | Operational definition | Scale | Weight |
|---|---|---|---|---|---|
| M1 | Coverage | Mandatory | The alternative generates the transmit carrier 144.0012 to 147.9988 MHz (REQ-TX-002) and the low-side receive LO for every TS-001 IF candidate (133.300 to 139.000 MHz), each in a configuration inside the datasheet ranges of the research report | pass / fail | n/a |
| M2 | Outputs | Mandatory | RX LO, TX carrier and BFO (IF +/- 1 kHz) are available when the semi break-in sequence needs them (ADR-026) | pass / fail | n/a |
| M3 | Frequency error | Mandatory | The frequency word errs by 5 Hz or less, the allocation of `frequency-budget.md` section 2, so the +/-370 Hz budget at 148 MHz holds (concept section 11.2 mandatory criterion) | pass / fail | n/a |
| M4 | Reference | Mandatory | Accepts the 25.000 MHz TCXO of Part B (ADR-023) | pass / fail | n/a |
| M5 | Sourcing and assembly | Mandatory | Stocked at DigiKey or Mouser (ADR-012, SI-028); a surface-mount package PCBWay places (SI-031) | pass / fail | n/a |
| M6 | Supply | Mandatory | Runs from the 3.3 V rail (ADR-013 mandatory list) | pass / fail | n/a |
| M7 | Battery life | Mandatory | TPM-008 threshold met: at least 8 h at 1:9 in the battery-life model of power research F23 (expected scenario, with this alternative's frequency-generation current) | pass / fail | n/a |
| M8 | Safety | Mandatory | No Red safety risk that no identified step reduces to Yellow (06 section 13 item 2) | pass / fail | n/a |
| C1 | Phase noise at 144 MHz | Enhancing | Single-sideband phase noise of the RX LO at 10 kHz offset at 144 MHz, dBc/Hz: datasheet or measured value scaled by 20 log(f2/f1), from the research report. Reciprocal-mixing dynamic range (RMDR) = -L - 10 log(500 Hz) | 1: -107 or worse (RMDR 80 dB or less) / 3: -112 (RMDR 85 dB, REQ-SYS-031 floor with zero margin) / 5: -125 or better (RMDR 98 dB or more); linear between anchors | 35 |
| C2 | Supply current | Enhancing | Current of the synthesizer ICs of the alternative at 3.3 V (TCXO excluded, it is common), mA, from the research report | 1: 80 or more / 3: 50 / 5: 30 or less; linear | 20 |
| C3 | Spurious output | Enhancing | Specified spurious level of the RF outputs (LO and TX carrier), dBc, from the datasheet | 1: no specified level / 3: -60 dBc specified / 5: -75 dBc or better specified | 10 |
| C4 | Tuning and changeover | Enhancing | Click-free tuning steps (RSK-041; REQ-SYS-076), bus traffic in receive, RX-to-TX changeover inside the 12 ms lead-in (ADR-026) | 1: PLL reset on every write, or changeover beyond the lead-in / 3: click-free by driver discipline and changeover inside the lead-in, but unverified at 144 MHz or with in-band bus traffic / 5: click-free steps demonstrated at 144 MHz, no retune at changeover, no in-band bus lines | 10 |
| C5 | Firmware and driver effort | Enhancing | New bus drivers and devices in the safety-critical frequency-word path (07 section 14.1, WP-SW-05, WP-SW-06) | 1: two new drivers, both in the safety-critical path / 3: two drivers, one in the safety-critical path / 5: one driver | 10 |
| C6 | First-power-on confidence | Enhancing | Evidence before the build that the part works at 144 MHz as used | 1: no heritage and no vendor data at VHF / 3: vendor datasheet data at VHF, or amateur heritage at HF only / 5: measured amateur or vendor heritage at 144 MHz | 10 |
| C7 | 70 cm output | Enhancing | Output range covers 420 to 450 MHz (ADR-002, SI-002) | 1: no / 5: yes | 5 |
| | | | | **Sum of weights** | **100** |

**Cost rule (not weighted).** ADR-013 and SI-029, with the band confirmed by SRR decision 56:
- if the unit costs of the surviving alternatives differ by USD 15 or less, the weighted performance matrix decides regardless of cost;
- otherwise cost enters the matrix.

Section 6 item 7 also runs the matrix with cost as a weighted criterion, because the test passes with a small margin (section 4).

Criteria considered (mandatory line, 06 section 13 item 1):
- **Safety:** used as M8. It is not a scored criterion, because both alternatives feed the same controls. The HZ-008 K4 guard and bound on the calibration constant, and the K7 counter on the carrier sample, are identical for both (`frequency-budget.md` section 3.3).
- **First power-on:** used as C6.
- **Cost:** used as the ADR-013 cost-band rule, not weighted, because the alternatives lie inside the band. A cost-weighted variant is in section 6.
- **Schedule:** used as C5 (driver effort). There is no lead-time difference: both parts are stocked (M5).
- **Performance margin:** used as C1, C2 and C3.
- **System security:** omitted. The synthesizer sits on internal buses, and neither alternative touches the 07 section 16.2 attack surfaces (USB firmware loading, key input).

Other criteria considered and not used, with reason:
- **"Filtering needed for square-wave outputs"** (concept section 11.2). Every candidate output at 133 to 148 MHz comes from a divider and carries odd harmonics. The LO and exciter filters are sized for either alternative in WP-PDR-19 and WP-PDR-21, and no evidence in the corpus discriminates the two alternatives here.
- **Lock time for tuning.** Folded into C4.

**Part B: reference.** Rule-based. Every rule is mandatory, and a preference follows.

| ID | Criterion | Operational definition | Source |
|---|---|---|---|
| R-M1 | Frequency | 25.000 MHz | `clock-plan.md` rule 7 (26 MHz x 5 = 130.000 MHz, the image of 148.000 MHz at IF 9.000 low side; 27 MHz x 5 = 135.000 MHz in the LO band); F16: the Si5351A takes 25 or 27 MHz |
| R-M2 | Output form | LVCMOS (square) | F20: about 5 dB worse LMX2571 phase noise with a clipped-sine reference |
| R-M3 | Uncalibrated total | 1.5 ppm or less: initial tolerance, reflow shift, temperature -10 to +45 C, one-year aging, supply and load, from the datasheet | `frequency-budget.md` section 3.2 (guard-protecting identity, case C-8) |
| R-M4 | Sourcing | Surface mount, stocked at DigiKey or Mouser, PCBWay-placeable | ADR-012, SI-028, SI-031 |
| R-C | Preference | 0.1 ppm temperature-stability class over 0.25 over 0.5. Only 0.1 ppm keeps two calibrated units inside the 250 Hz half-passband for a year (RSK-002) | `frequency-budget.md` section 3.2 table |

### 3.2 Alternatives

**Part A**

| ID | Alternative | Description | Source |
|---|---|---|---|
| A0 | Current baseline: no synthesizer chosen | The functional baseline holds no synthesizer. Deferring the choice to CDR is ADR-013 option D, rejected there because the synthesizer sets the receiver architecture, board area and power budget, which are PDR products. Listed for completeness, not scored | ADR-013 section 3 |
| A1 | Si5351A-B-GT alone, with the TCXO | Three outputs. CLK0 is the RX LO from PLL A, CLK1 the TX carrier from PLL B, each through an integer output divider of 6 with the fractional PLL tuned. CLK2 is the BFO. I2C control | F16, F17, F21; Table 2 |
| A2 | LMX2571 (RX LO and TX carrier) plus Si5351A-B-GT (BFO only), one shared TCXO | LMX2571 on SPI, retuned between the RX LO and the TX carrier at each changeover (FastLock below 1.5 ms). The Si5351A runs one output at the BFO, written only at mode changes, not while tuning | F16, F20, F21; Table 2 |

Alternatives pruned before scoring (trade tree), with reason:
- **ADF4351 and MAX2871.** Current of 120 to 170 mA (F18; MAX2871 current not captured, F19). With a Si5351A BFO, the F23 model gives 6.9 h at 1:9, which fails M7. The phase noise derived at VHF is no better than the Si5351A's (F18: about -113 dBc/Hz).
- **LMX2571 alone.** Fails M2: one VCO, so it cannot hold the BFO and the LO at once.
- **LMX2571 with a fixed crystal-oscillator BFO.** No catalogue oscillator at a BFO frequency (IF +/- sidetone offset) is evidenced in the corpus. Kept as a CDR refinement that would save about 20 mA (section 8).
- **Fixed 116 MHz overtone LO with a tunable IF.** This belongs to the receiver architecture and was pruned in TS-001 (family F-B).

**Part B**

| ID | Candidate | Description | Source |
|---|---|---|---|
| RB1 | SiTime SiT5356, 25.000 MHz, LVCMOS | MEMS Super-TCXO, 1 to 60 MHz, +/-0.1, 0.2 or 0.25 ppm stability, LVCMOS or clipped sine, I2C digital tuning, in production | F21 (Medium) |
| RB2 | Epson TG2520SMN, 25.000 MHz | 10 to 55 MHz, +/-0.5 ppm, about USD 0.44 at 3 k; output form not in the corpus | F21 (Medium) |

Pruned:
- **Abracon ATX-13:** 26 MHz only in the corpus, fails R-M1.
- **QRP Labs TCXO module:** a module, not a placeable part, fails R-M4.
- **A generic +/-2.5 ppm TCXO:** fails R-M3.
- **Crystal only:** ADR-023 option C, rejected.

### 3.3 Weight rationale

- **C1, 35.** SI-029 asks for the best performer "for this application". ADR-013 lists phase noise first among its performance criteria, and SRR decision 56 confirms it as a criterion. Phase noise sets reciprocal mixing (REQ-SYS-031) and adjacent-signal desensitization (REQ-SYS-029), which are the receiver's contribution to MOE-010. It is the only criterion with an L1 requirement at stake with no design fallback, since filtering does not remove reciprocal mixing.
- **C2, 20.** TPM-008 is an owner acceptance value (ADR-020). The current difference moves battery life by about 0.9 h in the F23 model.
- **C3, 10.** Spurious lines on the LO or carrier become receive birdies or transmit spurs. The TX harmonic filter covers harmonics, not close-in spurs.
- **C4, 10.** SRR decision 56 names tuning clicks. RSK-041 and REQ-SYS-076 bound them.
- **C5, 10.** Schedule and verification cost of safety-critical code (SWE-219, SWE-220 apply to the frequency-word path).
- **C6, 10.** The first-power-on consideration of 06 section 13.
- **C7, 5.** An enhancing criterion by ADR-002.

No weight was set by the owner directly.

### 3.4 Evaluation methods

| Criterion | Method | Tool | Evidence artifact |
|---|---|---|---|
| M1, M2, M4, M5, M6 | Datasheet comparison through the research report | none | reference report F16, F20, F21 |
| M3 | Budget analysis | `hardware/sim/freq/freq_budget.py` (developer evidence) | `docs/design/analysis/frequency-budget.md` section 3.2 |
| M7, C2 | Battery-life model of power research F23 with each alternative's current | `hardware/sim/freq/ts007_matrix.py` (developer evidence) | Appendix A |
| C1 | Phase-noise scaling 20 log(f2/f1) from measured and datasheet values; RMDR; REQ-SYS-029 limit at 2 kHz | `ts007_matrix.py` | Appendix A |
| C3, C6, C7 | Datasheet comparison | none | F16, F17, F20 |
| C4 | Datasheet comparison, practice report, clock plan | `hardware/sim/freq/clock_plan.py` | `clock-plan.md` rules 3 and 4; audio research F11 |
| C5 | Driver count against 07 section 19 (WP-SW-05, WP-SW-06) and 07 section 14.1 | none | 07 sections 14.1, 19 |
| Totals and sensitivity | Recomputation | `ts007_matrix.py` | section 6 |

### 3.5 Setup matrix (before scoring)

| Criterion | Weight | A1 | A2 |
|---|---|---|---|
| M1 to M8 | n/a | | |
| C1 | 35 | | |
| C2 | 20 | | |
| C3 | 10 | | |
| C4 | 10 | | |
| C5 | 10 | | |
| C6 | 10 | | |
| C7 | 5 | | |

## 4. Scoring rationale

**Mandatory screening, Part A**

| Alternative | M1 | M2 | M3 | M4 | M5 | M6 | M7 | M8 | Result |
|---|---|---|---|---|---|---|---|---|---|
| A1 | pass. VCO 864.0 to 888.0 MHz for the TX carrier and 799.8 to 834.0 MHz for the LO, both with divider 6, inside 600 to 900 MHz. LO and TX are the two frequencies above 112.5 MHz the part allows (F16, High) | pass. Three outputs (F16) | pass. 3.97 Hz step at divider 6 with a 20-bit denominator, error 2.0 Hz or less. Medium: AN619 register map not in the corpus | pass. 25 MHz reference into XA (F16: 25 or 27 MHz; heritage of TCXO use with the Si5351A, F21). Medium | pass. 5,087 in stock (F21, 2026-09-25); 10-MSOP | pass. 3.3 V CMOS (F16). Medium | pass. 9.7 h (Appendix A) | pass (section 7) | kept |
| A2 | pass. 10 to 1344 MHz (F20, High) | pass. LMX2571 LO and TX, Si5351A BFO | pass. The 5 Hz word error is a SW-SYNTH design requirement verified by HostUnit (RSK-046 step S3). Medium | pass. OSCin 10 to 150 MHz; square wave preferred (F20, High) | pass. 1,309 in stock (F20, 2026-09-25); 36-pin WQFN 6 x 6 mm | pass, **Low**: the supply range is not in the corpus. TI positions the part for battery PMR radios (F20). Confirmation is value-of-information item 4 | pass. 8.8 h (Appendix A) | pass (section 7) | kept |
| ADF4351 + Si5351A | pass | pass | pass | pass | pass | pass | **fail**, 6.9 h | | dropped |

**Cost-band test (ADR-013).** The difference A2 - A1 is the LMX2571 plus its loop-filter and output-match passives. The Si5351A-B-GT is in both. The research price signal for the LMX2571 is USD 8.75 to 14.46 at quantity 1 (F20, findchips, 2026-09-25). The passives are estimated at USD 0.30 (engineering estimate, Low). So the difference is **USD 9.05 to 14.76, inside the USD 15 band**, with USD 0.24 to spare at the top of the price range. This test is Low-confidence. It is re-run on a dated DigiKey quote (value-of-information item 3), and section 6 item 7 shows the recommendation holds even if the band is exceeded.

**Enhancing scores**

| Criterion | Alternative | Measured value | Score | Confidence | Evidence |
|---|---|---|---|---|---|
| C1 | A1 | L(10 kHz) at 144 MHz estimated -109.3 to -115.4 dBc/Hz. From the QCX -135.6 dBc/Hz at HF scaled from 7 or 14 MHz (the QCX band is not stated in F17). -109.8 from KE5FX at 19.99 MHz. The unverified -112 report at 156 MHz. Central value -110 dBc/Hz gives RMDR 83 dB, 2 dB under the REQ-SYS-031 floor of 85 dB (TBR). The REQ-SYS-029 limit at 2 kHz is -106.1 dBc/Hz; the value at 2 kHz is not in the corpus | 2 | Low | F17 (Medium for HF, Low for VHF); Appendix A |
| C1 | A2 | -133.5 dBc/Hz at 12.5 kHz, from the datasheet -123 dBc/Hz at 480 MHz scaled by 10.5 dB. RMDR 106.5 dB, 21.5 dB above the floor. The normalized in-band model gives -133.2 dBc/Hz at 2 kHz, 27 dB under the REQ-SYS-029 limit | 5 | Medium | F20 (High for the datasheet values, Medium for the scaling); Appendix A |
| C2 | A1 | 30 mA (24 mA core + 2 mA x 3 outputs) | 5 | Medium | Table 2; F16 |
| C2 | A2 | 65 mA (LMX2571 39 mA + Si5351A 26 mA with one output) | 2 | Medium | F20; Table 2 |
| C3 | A1 | No spurious level specified for the outputs in the corpus. Fractional-divider spurs reported by the community, not quantified | 1 | Low | F16, F17 |
| C3 | A2 | Spurs "better than -75 dBc" specified. The Si5351A BFO at 9 to 10.7 MHz is not an RF output | 5 | High | F20 |
| C4 | A1 | Click-free steps need a driver that writes only the PLL or multisynth registers (G0UPL practice, audio F11, Medium). TX and RX on separate PLLs, so no retune at changeover. But every tuning step sends I2C traffic at 400 kHz, whose coherent lines fall across the band (`clock-plan.md` rule 3; level unknown) | 3 | Low | audio F11; `clock-plan.md` |
| C4 | A2 | FastLock below 1.5 ms, inside the 12 ms lead-in with 4.5 ms to spare (`frequency-budget.md` C-14.A2). Tuning traffic on SPI at 18.75 MHz, a clear-set clock with no in-band line. Behaviour on numerator-only updates not in the corpus | 3 | Low | F20; `frequency-budget.md`; `clock-plan.md` rule 4 |
| C5 | A1 | One I2C driver (WP-SW-05) in the safety-critical path | 5 | Medium | 07 sections 14.1, 19 |
| C5 | A2 | SPI driver (WP-SW-06, also used by the display) for the LMX2571 in the safety-critical path, plus the I2C driver for the BFO outside that path | 3 | Medium | 07 sections 14.1, 19 |
| C6 | A1 | Amateur heritage at HF (QCX, KX2, uBITX); nothing measured at 144 MHz | 3 | Low | F17 |
| C6 | A2 | Vendor datasheet specified to 1344 MHz with values at 480 MHz; no amateur heritage | 3 | Low | F20 |
| C7 | A1 | Output ceiling 200 MHz | 1 | High | F16 |
| C7 | A2 | 10 to 1344 MHz | 5 | High | F20 |

**Part B screening (reference)**

| Candidate | R-M1 | R-M2 | R-M3 | R-M4 | Result |
|---|---|---|---|---|---|
| RB1 SiT5356 | pass (25 MHz inside 1 to 60 MHz) | pass (LVCMOS option) | **not shown**: the stability class is known, but initial tolerance, reflow and aging are not in the corpus | **not shown**: stock and price not captured (reference report action 21) | preferred class, pending datasheet |
| RB2 TG2520SMN | pass (25 MHz inside 10 to 55 MHz) | **not shown** | **not shown** | **not shown** | alternate, pending datasheet |

## 5. Final decision matrix (Part A)

| Criterion | Weight | A1 score | A1 weighted | A2 score | A2 weighted |
|---|---|---|---|---|---|
| C1 | 35 | 2 | 70 | 5 | 175 |
| C2 | 20 | 5 | 100 | 2 | 40 |
| C3 | 10 | 1 | 10 | 5 | 50 |
| C4 | 10 | 3 | 30 | 3 | 30 |
| C5 | 10 | 5 | 50 | 3 | 30 |
| C6 | 10 | 3 | 30 | 3 | 30 |
| C7 | 5 | 1 | 5 | 5 | 25 |
| **Total** | **100** | | **295** | | **380** |
| **Percent of maximum** | | | 59.0 % | | 76.0 % |
| **Rank** | | | 2 | | 1 |

The totals are recomputed by `hardware/sim/freq/ts007_matrix.py` (exit status 0 when they equal these values).

## 6. Uncertainty and sensitivity statement

1. **Weight sensitivity.** Each weight was moved by +10 and -10 (clamped at 0), with the others rescaled proportionally. The top rank changes for none of the 14 runs. The closest run is C2 +10: A1 320.6, A2 357.5.
2. **Score sensitivity.** Each Low-confidence cell (A1: C1, C3, C4, C6; A2: C4, C6) was moved by +1 and -1. The top rank changes for none of the 12 runs. The closest run is C1-A1 +1: A1 330, A2 380.
3. **Assumptions and their evidence.**
   - A1's phase noise at 144 MHz scales from HF measurements, which assumes the divider adds no floor above the VCO noise. Supported by the -112 dBc/Hz secondary report (F17).
   - A2's value scales the 480 MHz datasheet figure by 20 log(480/144). That assumes the output divider's floor is below -133 dBc/Hz (F20: "if the divider noise floor allows").
   - The battery-life model is power research F23 (Low confidence on usable capacity). The comparison uses only its current differences.
   - Price signals are quantity 1 on 2026-09-25.
4. **Robustness verdict: Robust.** No single weight or Low-cell move changes the leader, and the lead is 85 points (17 % of the maximum). A stress case beyond 06 section 14.4 moves every Low cell against A2 at once (A1 +1 on C1, C3, C4 and C6; A2 -1 on C4 and C6). It gives a tie at 360 to 360. So the recommendation rests on the A2 cells that are not Low: C1 (Medium, datasheet) and C3 (High, datasheet).
5. **Value of information** (none performed before this recommendation, because no downloads or purchases are permitted in this wave):
   1. A primary-source or bench measurement of Si5351A phase noise at 144 MHz. It would move A1 C1 from Low. The owner's bench has no phase-noise-capable analyzer (reference report action 22). It must precede B1a to change the decision; otherwise it becomes a CDR confirmation only if A1 is chosen.
   2. The LMX2571 closed-loop plots at a VHF output (reference report action 20; datasheet download needs owner permission). This confirms C1 for A2. It is due before CDR, and needs an owner download permission of the OD-18 or OD-39 kind (PDR work plan section 6.1).
   3. A dated DigiKey quote for the LMX2571 and the SiT5356 grades (OD-39 stock checks). This confirms the cost-band test and R-M4 by B1a.
   4. The LMX2571 datasheet: supply range (M6), SPI clock ceiling (`clock-plan.md` rule 4 assumes 18.75 MHz is allowed), and retune behaviour. Due before CDR.
   5. SiT5356 and TG2520SMN datasheets for R-M2 and R-M3. Due before the CDR BOM (WP-PDR-38).
6. **Limitations of the methods and tools** (SE HB section 6.8.1.2.5):
   - No score rests on a measurement at 144 MHz.
   - All device values come from one research report of 2026-09-25, which quotes datasheets and community reports. The datasheets were not re-read, because no download is permitted this wave.
   - The three scripts in `hardware/sim/freq/` have no TV record, so their outputs are developer evidence (05 section 9.1). Their arithmetic is small and hand-checkable (Appendix A).
   - The battery-life model is a research model, not the TPM-008 budget of WP-PDR-29.
7. **Cost-weighted variant.** If the cost-band test fails on a dated quote, cost enters as C8 at weight 15, with the other weights scaled to 85, scored A1 5, A2 1. Then A2 338.0 and A1 325.8: A2 still leads, but by 12.2 points, under the 25-point closeness threshold. The owner would then be presented both.

## 7. Risks and benefits of the surviving alternatives

Scores use the register scales (06 sections 6 and 7; Red 12 or more, Yellow 5 to 11, Green 4 or less).

| Alternative | Risk statement | L | C (driving dimension) | Score / band | Would be entered as |
|---|---|---|---|---|---|
| A1 | Given the Si5351A at divider 6 with an estimated -110 dBc/Hz at 10 kHz, there is a possibility of reciprocal-mixing dynamic range below the 85 dB of REQ-SYS-031 and desensitization beyond REQ-SYS-029, adversely impacting weak-signal reception (MOE-010), leading to a CR that lowers the floor, or a synthesizer change after CDR | 3 | 3 (performance margin) | 9 Yellow | RSK-035 re-score |
| A1 | Given the TX carrier held on PLL B at six times the carrier frequency while receiving, there is a possibility of leakage at the operating frequency plus the sidetone offset, adversely impacting receive sensitivity at the operating frequency, leading to a birdie on the station being worked | 2 | 3 (performance margin) | 6 Yellow | RSK-040 member |
| A1 | Given I2C traffic at 400 kHz on every tuning step, there is a possibility of audible tuning noise from the coherent dense lines, adversely impacting the tuning feel (RSK-041, REQ-SYS-076), leading to driver or layout rework | 3 | 2 (performance margin) | 6 Yellow | RSK-041 member |
| A2 | Given 65 mA for frequency generation, there is a possibility of battery life below the TPM-008 PDR margin of 9.6 h (8.8 h in the F23 model), adversely impacting TPM-008, leading to a Yellow TPM at PDR and a current-reduction step at CDR (fixed-oscillator BFO, about -20 mA) | 3 | 3 (performance margin) | 9 Yellow | new register entry request (TPM-008 family) |
| A2 | Given LMX2571 properties not in the corpus (supply range, SPI ceiling, retune behaviour), there is a possibility that a property differs from the assumptions of M6 and C4, adversely impacting the TX and CTL interfaces, leading to a schematic change before CDR | 2 | 3 (schedule) | 6 Yellow | new register entry request |
| A2 | Given a price margin of USD 0.24 in the cost-band test, there is a possibility that a dated quote exceeds USD 15, adversely impacting the ADR-013 decision rule, leading to the cost-weighted matrix of section 6 item 7 (still A2, closely ranked) | 3 | 1 (cost) | 3 Green | none (recorded here) |
| Both | Given the BFO's 16th harmonic in the band for IF 9.0106 MHz (and at 144.000 to 144.016 MHz for IF 9.000 with the BFO above the IF), there is a possibility of an in-band birdie, adversely impacting REQ-SYS-034, leading to a BFO filter and shield or an IF change (`clock-plan.md` section 4) | 3 | 3 (performance margin) | 9 Yellow | RSK-040 member |

Safety (M8): neither alternative has a Red safety risk. The HZ-008 C7 and C8 causes are controlled identically by K4 (guard, and the bound on the calibration constant) and K7 (the FC0 count of the prescaled carrier), `frequency-budget.md` section 3.

| Alternative | Benefits beyond the scored criteria |
|---|---|
| A1 | One part and one driver; lowest BOM cost; known HF heritage; the TX carrier needs no retune at changeover |
| A2 | Direct FSK and FastLock features (F20) for later modes; the receive LO and the transmit carrier come from one VCO, so no second VCO runs at six times the carrier while receiving; the BFO's Si5351A is written only at mode changes; 70 cm reuse in revision B (ADR-002) |

Aggregate risk (maximum score): A1 9, A2 9.

## 8. Recommendation

- **Recommended alternative (Part A):** A2, total 380 (76.0 %).
- **Rationale:** highest total. Its lead rests on datasheet-backed phase noise and spurious specifications, which carry the heaviest weight and the requirement with no design fallback (REQ-SYS-031, REQ-SYS-029). The cost-band rule of SI-029 applies, because the price difference is inside USD 15 on the research price signal.
- **Recommended reference (Part B):** a 25.000 MHz LVCMOS TCXO of the SiT5356 class, in the 0.1 ppm grade (R-C), accepted at CDR when its datasheet shows R-M3 and R-M4. The 0.25 ppm grade is acceptable with yearly re-calibration in the operations handbook (RSK-002 step S4). TG2520SMN is the alternate if its datasheet shows R-M2 and R-M3. The owner is asked to decide the class and the acceptance test now. The part number is fixed at the CDR BOM (WP-PDR-38) on the datasheets of value-of-information item 5.
- **Closely ranked alternatives presented for the owner's choice:** none in the base matrix (85 points apart). A1 becomes closely ranked only in the cost-weighted variant of section 6 item 7.
- **Impacts of adopting the recommendation:**
  - **Requirements** (TBR values proposed by this study and its analyses, rule C10):
    - REQ-SYS-031 at 85 dB, unchanged (A2 margin 21.5 dB). With A1 the floor would have to fall to about 82 dB by CR.
    - REQ-SYS-008, 009, 010, 154, 182; REQ-TX-002, 013: `frequency-budget.md` section 4.
    - REQ-SYS-034: `clock-plan.md` section 5.
    - L2 TX requirements to derive (WP-PDR-34): synthesizer LO and carrier from the LMX2571; carrier sample through a divide-by-8 prescaler to an RP2350 GPIN pin.
    - L2 SW requirements (WP-PDR-35): calibration constant bounded at +/-0.9 ppm; FC0 frequency verification; LMX2571 SPI at a clear-set SCK.
  - **Interfaces:** `ICD-CTL-SW` pin map (WP-PDR-36a) gains the LMX2571 SPI chip select, the Si5351A on I2C and two GPIN pins.
  - **Cost model:** about +USD 9 to 15 per unit against A1 (WP-PDR-46).
  - **Schedule:** no change. WP-SW-05 and WP-SW-06 are both planned for FW-B1 (07 section 19).
  - **TPM-008:** the F23-model estimate moves from 9.5 h to 8.8 h. That is Yellow against the 9.6 h PDR margin, so WP-PDR-29 and WP-PDR-24 confirm it on their budget. The CDR refinement is a fixed-oscillator BFO if TS-001 keeps option B, saving about 20 mA.
  - **Verification cases:** a Bench phase-noise or reciprocal-mixing check of REQ-SYS-031 at TRR (WP-PDR-43 instruments).
- **Corrective actions if the recommendation is adopted late:** WP-PDR-31 (architecture) and WP-PDR-36a (pin map) draft on A2 from Wed 09-30. If B1a slips to B1b, they draft on both line-ups, and the TX and CTL L2 files carry the synthesizer as a TBR interface until B1b.

## 9. Dissent

| Who | Date | Dissent | How it was addressed |
|---|---|---|---|
| None recorded | | | |

## 10. Decision

- **Decision:**
- **Decided by:**
- **Rationale as stated by the owner:**
- **Records produced:**
- **Revisit conditions:**
- **Lessons learned:**

## 11. References

- NASA/SP-2016-6105 Rev 2 (SE HB) section 6.8 and Table 6.8-1 (corpus `docs/references/md/nasa-se-handbook/`).
- `docs/process/06-risk-and-decision-analysis.md` sections 13, 14; `docs/process/07-software-engineering-plan.md` sections 2.1.1, 14.1, 19.
- ADR-002, ADR-012, ADR-013, ADR-016, ADR-020, ADR-023, ADR-026; TS-001; SRR decisions 9, 25, 40, 56 (`docs/reviews/SRR/decision-memo.md`, `decisions-for-owner.md`).
- `docs/research/2m-cw-transceiver-reference-designs.md` F16 to F21, Table 2 (2026-09-25); `power-tree-and-charging.md` F23; `audio-output-and-hearing-safety.md` F11; `display-and-ui-parts.md` F10; `regulatory-corpus-and-operators.md` F7, F8.
- RP2350 datasheet (build 2025-02-20) sections 8.1.1.4, 8.1.3 (Tables 541, 582 to 585), 8.2.1.1 (Table 596), via rustos `docs/extracted/rp2350-datasheet.md` at commit `2ec64c0f`.
- 47 CFR 97.301(a), 97.305(a), (c), 97.307(b) (corpus `docs/references/md/regulatory/`, eCFR issue 2026-09-23).

## Appendix A. Supporting analysis

- **Literature and research search:** Claude Context searches of `/Users/robinonsay/rust/cwht` on 2026-09-27 for:
  - the synthesizer candidates and the band-edge guard;
  - LMX2571 phase noise and current;
  - the RP2350 frequency counter and GPIN;
  - tool validation for Python analysis scripts;
  - design reader items.

  The hits were ADR-013, ADR-023, concept sections 7.4 and 11.2, the technology assessment section 3.1, reference report F16 to F21, and the 07 WP-SW-14 row. The RP2350 frequency counter was found in the rustos committed datasheet extract (read with `git show`). No new web source was consulted: downloads are not permitted in this wave.
- **Previous related decisions and dissent:** ADR-013 (method; options B, C, D rejected), ADR-023 (ceiling and guard), SRR decision 56 (band and criteria). No dissent recorded against them.
- **Detailed analysis** (all developer evidence; commands from the repository root):
  - `.venv/bin/python hardware/sim/freq/ts007_matrix.py --plot`: phase-noise scaling, RMDR, the REQ-SYS-029 limit, battery life per alternative, totals, 14 weight runs, 12 cell runs, the stress case and the cost variant. Figure `docs/reviews/PDR/figures/ts-007-sensitivity.png`, inspected.
  - `.venv/bin/python hardware/sim/freq/freq_budget.py --plot` (`docs/design/analysis/frequency-budget.md`).
  - `.venv/bin/python hardware/sim/freq/clock_plan.py --plot` (`docs/design/analysis/clock-plan.md`).
- **Hand checks (known answers):**
  - -135.6 + 20 log(144/7) = -109.3 dBc/Hz.
  - -123 + 20 log(144/480) = -133.5 dBc/Hz.
  - RMDR = -L - 27.0 dB.
  - REQ-SYS-029: a -130 dBm signal is 10 dB over the -140 dBm noise, so (S+N)/N is 11 (10.41 dB). A 3 dB loss allows reciprocal-mixing noise of 1.222 N, which gives L(2 kHz) at most -140 + 0.87 + 60 - 27.0 = -106.1 dBc/Hz.
  - F23 model: life = 2.7 Ah / (0.1 I_tx + 0.9 I_rx), with I_rx = I_5V x 5 / (7.2 x 0.9). A1: I_5V = 0.251 A gives 9.7 h. A2: 0.286 A gives 8.8 h.
- **Decision metrics:** opened and recommended the same day; 2 scored alternatives (4 pruned); 8 mandatory and 7 enhancing criteria; no criteria revisions.

## Change log

| Revision | Date | Change | Reason |
|---|---|---|---|
| 0 | 2026-09-27 | Initial; frozen for the section B review and the software assurance review (freeze F0, rule C2) | WP-PDR-20 wave 1a |
