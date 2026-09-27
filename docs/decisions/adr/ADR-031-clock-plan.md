# ADR-031: Clock plan that keeps controller, bus, switcher and reference clock lines out of the 2 m receive range

| Field | Value |
|---|---|
| ID | ADR-031 |
| Status | Proposed |
| Date proposed | 2026-09-27 |
| Date decided | pending (owner session B2, with the REQ-SYS-034 value ruling; plan rule C10) |
| Decision class | 1 (`docs/process/06-risk-and-decision-analysis.md` section 14.1 item (c)). The plan implements HZ-008 control K6 (`docs/safety/hazards.json` 0.5.0-pha) and sets values of REQ-SYS-034. It is recorded by this ADR alone under SEMP customization 11 item (ii): "a class 1 value Claude proposes that the owner's ADR disposition records without a trade study" (`docs/plan/semp.md` section 9.0 and section 5.17; SRR decision 106). The alternatives are compared in section 3 and quantified in `docs/design/analysis/clock-plan.md`. The TCXO frequency is the one clock value that is also a TS-007 criterion (R-M1) |
| Decision authority | Robin. The ADR is class 1, and it fixes baseline content: REQ-SYS-034 values and HZ-008 K6 text |
| Author | Claude (RF designer TX author invocation, WP-PDR-20, 2026-09-27) |
| Independent reviewer | Pending: `docs/reviews/PDR/checklists/analysis-frequency-budget-and-clock-plan.md`, which reviews `clock-plan.md`. This ADR's own review uses `peer-review-checklist-design.md` sections A, B and H; the lead SE assigns the record (with the WP-PDR-32 ADR reviews or its own) |
| Life-cycle phase | B |
| Baseline affected | baseline/pdr (allocated baseline: ICD-CTL-SW clock table, TX, CTL and SW L2 values) |
| Change request | none. Pre-PDR proposal within the REQ-SYS-034 `tbr.plan`. Section 2 item 5 refines ADR-023 section 2 item (5); see section 7 |

## 1. Context

The receiver's MDS target is -140 dBm (REQ-SYS-022, TBR). Controller, bus and switcher clocks on the same board produce harmonic lines, and any line in 144.000 to 148.000 MHz is a birdie (RSK-040). Two lines cannot be moved:
- the 12th harmonic of the Pico 2 module's 12 MHz crystal;
- the 3rd harmonic of the 48 MHz clocks.

Both fall within +/-9.36 kHz of 144.000 MHz. REQ-SYS-034 already excludes 144.000 to 144.010 MHz for them. Every other clock can be placed.

HZ-008 K6 asks for a clock plan with an "expected birdies" list, but no frequency set has been chosen yet. ADR-023 item (5) states that no controller clock harmonic falls in the band. The 48 MHz ADC clock, which runs whenever the ADC samples, contradicts that statement.

- Driving inputs and expectations: SI-004 (narrow CW weak signals), NGO and MOE-010 (weak-signal reception), SI-024 (full band).
- Requirements that constrain the decision:
  - REQ-SYS-034 (TBR): receive responses at most 3 dB above MDS from 144.010 to 147.999 MHz;
  - REQ-SYS-022 (MDS);
  - REQ-SYS-093 (charging paused while the radio is on);
  - REQ-SYS-182 and REQ-TX-013 (the prescaled carrier sample).
- Hazards in play: HZ-008 (control K6 "clock plan"; `hazards.json` 0.5.0-pha).
- Research consulted:
  - `docs/research/display-and-ui-parts.md` F10 (clock harmonic table);
  - `docs/research/power-tree-and-charging.md` F19, F20 (switcher frequencies);
  - `docs/research/audio-output-and-hearing-safety.md` F1 (PWM audio at 146.48 kHz);
  - `docs/research/2m-cw-transceiver-reference-designs.md` F16 (Si5351A reference and output ranges);
  - RP2350 datasheet sections 8.1 (clock table: clk_adc "Must be 48MHz"), 8.2.1.1 (Table 596), 12.2, 12.3, 12.5, via rustos `docs/extracted/rp2350-datasheet.md` at commit `2ec64c0f`.
- Guidance consulted: 47 CFR 97.305(a), (c) (CW-only segment 144.0 to 144.1 MHz; corpus `47cfr-97.305.md` lines 17, 58); SE HB section 6.8 (decision reporting).
- Assumptions the decision rests on, and how and by when each is confirmed:
  1. The 5 V buck chosen by WP-PDR-24 has a SYNC input. Confirmed at the WP-PDR-24 part choice (B1b). If not, the buck's free-running lines are handled as rule 3 level items, and a CR on REQ-SYS-034 may follow.
  2. The line levels of dense clocks are controllable by layout, edge rate and shielding. Confirmed by the CDR layout review and the TRR bench scan (RSK-040 steps S2 to S4).
  3. The IF and injection side are low-side, with an IF of 9.000, 9.0106 or 10.7 MHz (TS-001). Confirmed by WP-PDR-19 at B1b. `clock-plan.md` section 4 gives the consequences of each IF.

## 2. Decision

The cwht clock plan follows these rules. The frequencies are those checked by `hardware/sim/freq/clock_plan.py`, with 0 rule failures at 2026-09-27.

1. **Clear-class clocks (4 MHz or more).** None has a harmonic line in 144.010 to 147.999 MHz. A clock derived from the RP2350 crystal with 144 MHz / f an integer ("coherent") may put a line only on 144.000 MHz, inside the REQ-SYS-034 exclusion.
2. **CW-only receive segment.** No clock running in operation has a line in 144.010 to 144.100 MHz.
3. **Dense-class clocks (below 4 MHz)** are derived from the RP2350 crystal and coherent with 144.000 MHz. From clk_sys = 150 MHz, that means a divisor that is a multiple of 25. Their frequency is at least 100 kHz, so their lines lie on 144.000 MHz and at or above 144.100 MHz. Their level is controlled by layout and verified by the REQ-SYS-034 Test.
4. **Frequencies:**
   - clk_sys = clk_peri = 150 MHz.
   - TCXO 25.000 MHz.
   - SPI SCK from 150 MHz / d, d even from 2 to 24. The synthesizer SPI uses d = 8 (18.75 MHz), subject to the LMX2571 SPI ceiling (TS-007 value-of-information item 4). A slow display bus uses d a multiple of 50.
   - I2C SCL 400 kHz (divisor 375).
   - Audio and sidetone PWM at TOP + 1 = 1000 (150 kHz). With an IF of 9.000 MHz, use TOP + 1 = 25 x an odd number, so no line lands on the IF.
   - Backlight PWM coherent and at least 100 kHz, or DC.
   - 5 V buck synchronised at 12 MHz / 5 = 2.4 MHz.
   - Carrier-sample prescaler divide by 8, on the TX path only.
   - PCM1808 system clock, only if TS-001 keeps option B: 150 MHz / 12 = 12.5 MHz, not 12.288 MHz.
5. **USB and ADC clocks.** clk_usb runs only while USB is enumerated. clk_adc (48 MHz) runs whenever the ADC samples. Both put their line on the same 144.000 MHz line as the crystal's 12th harmonic. They add level there, not a new line.
6. **Free-running switchers.** A free-running switching regulator may not run while the receiver is on. The charger boost is off while the radio is on (REQ-SYS-093).
7. **Expected birdies.** The expected-birdie list of HZ-008 K6 is `clock-plan.md` section 2 and section 4 for the chosen IF. It is re-generated by the checker whenever a clock changes.

## 3. Alternatives considered

| Option | Description | Why not chosen (or why chosen) |
|---|---|---|
| A (chosen) | Rule-based plan: clear set for fast clocks; crystal-coherent placement for slow ones; synchronised buck | Keeps the CW-only segment and the whole receive range free of clear-class lines, and places every unavoidable dense line on a predictable grid starting at the excluded 144.000 MHz line. Checked by script (`clock-plan.md` section 2: 0 rule failures) |
| B | Only avoid exact in-band harmonics of fast clocks (ADR-023 item (5) as written) | Not chosen. It ignores the 48 MHz ADC clock, which cannot be turned off while the ADC runs. It leaves dense clocks (I2C, PWM, switchers) at arbitrary frequencies, whose lines can land in the CW segment (for example, a free-running 2.2 MHz buck sweeps it) |
| C | Remove the problem by shielding and filtering alone, with free clock choices | Not chosen. The level of a line is a CDR layout result, while its frequency is free to choose now at no cost. Shielding stays a CDR measure for the level (RSK-040 step S3) |
| D | Do nothing until the TRR birdie scan | Not chosen. HZ-008 K6 and RSK-040 step S1 require the plan at PDR. A birdie found at TRR costs a board iteration |

## 4. Consequences

### 4.1 Requirements created or changed

| Requirement | Relationship | Note |
|---|---|---|
| REQ-SYS-034 | TBR values proposed unchanged (range 144.010 to 147.999 MHz; 3 dB above MDS), with this ADR as the clock-plan evidence | Ruled at B2 on the APPROVED analysis record (rule C10) |
| New SW-CTL or SW-SYNTH clock configuration requirements (WP-PDR-35) | new, derived from this ADR | Each divisor of section 2 item 4 is a configuration constant with a HostUnit test of the configuration table |
| New TX L2 requirement for the synchronised buck, or a PWR L2 requirement (WP-PDR-34) | new, derived | SYNC at 2.4 MHz from a crystal-derived clock |

### 4.2 Interfaces, design and code

- ICDs affected: `ICD-CTL-SW` gains a clock table (WP-PDR-36a); `ICD-TX-PWR` or `ICD-PWR-CTL` gains the buck SYNC line (WP-PDR-36a).
- Design elements: clocks configuration of 07 WP-SW-11; SPI and I2C divisors (WP-SW-05, WP-SW-06); PWM slices (WP-SW-03).
- New `SW-<SUB>` modules created by this ADR: none. ICDs created by this ADR: none.

### 4.3 Verification and safety

- Verification cases:
  - the REQ-SYS-034 Test (bench scan with the expected-birdie list, RSK-040 step S4);
  - an Inspection case that runs `clock_plan.py` against the configuration constants of the firmware (WP-PDR-35 and 43).
- Hazard analysis update required: yes. The HZ-008 K6 text gets rules 2, 3, 5 and 6 (request to WP-PDR-16b).
- Safety-critical software scope changed: no. The clocks driver WP-SW-11 is already safety-critical in 07 section 14.1.

### 4.4 Cost, schedule, risk

- BOM: a buck with a SYNC input (WP-PDR-24); no other cost.
- Gate affected: PDR (values), CDR (layout level), TRR (scan).
- Risks: RSK-040 step S1 evidence. The BFO-harmonic finding of `clock-plan.md` section 4 goes to the WP-PDR-18 register pass as a member of RSK-040.
- TPMs affected: none.

## 5. Compliance and tailoring

none

## 6. Decision record

Proposed memo wording, for the owner's disposition at B2. The owner's words are transcribed here when given:

> "Adopt ADR-031: the clock plan of `docs/design/analysis/clock-plan.md` section 3 (clear-set fast clocks, crystal-coherent dense clocks of 100 kHz or more, synchronised 2.4 MHz buck, 25.000 MHz TCXO, prescaler divide by 8), with REQ-SYS-034 kept at 144.010 to 147.999 MHz and 3 dB above MDS; section 2 item 5 refines ADR-023 item (5)."

## 7. Related

- Supersedes: none in full. Section 2 item 5 refines ADR-023 section 2 item (5) for the 48 MHz ADC and USB clocks. ADR-023 is Accepted and in the functional baseline, and README rule 2 allows an Accepted ADR's text to change only by a superseding ADR. The lead SE decides whether this partial refinement needs a CR against `baseline/srr`, or is recorded by a Status note on ADR-023 when ADR-031 is accepted (open item in the WP-PDR-20 return).
- Superseded by: none.
- Trade study: none. SEMP customization 11 item (ii); alternatives in section 3; the quantified comparison is `docs/design/analysis/clock-plan.md`. The TCXO frequency is also criterion R-M1 of TS-007.
- Review where presented: PDR.
- Revisit conditions:
  - any clock added or changed (re-run the checker);
  - the IF or injection side chosen at B1b differs from the assumption;
  - the WP-PDR-24 buck has no SYNC input;
  - the TRR scan finds a line not in the expected list.

## 8. Change log

- 2026-09-27: created, Proposed (WP-PDR-20 wave 1a).
