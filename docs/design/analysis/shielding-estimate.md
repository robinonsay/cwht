# Shielding and bond estimate per enclosure option

| Field | Value |
|---|---|
| Product | Analysis note (08 section 3.4), WP-PDR-27, PDR draft revision 0, 2026-09-27 |
| Author | Claude, ME designer (WP-PDR-27 author invocation) |
| Status | Draft. **AT RISK (CR-003):** REQ-SYS-109 is taken in its CR-003 revision 3 wording (bond of every conductive enclosure part at 0.1 ohm TBR), which is Submitted and not dispositioned (plan rule C8) |
| Serves | REQ-SYS-177 (20 dB, TBR) and REQ-SYS-109 (0.1 ohm, TBR, CR-003) value proposals; TS-011 mandatory criterion M5 and enhancing criterion C4; the pre-build analyses TC-SYS-107 and TC-SYS-075 setup (CR-003 section 1.6) |
| Model, checker, plot | `hardware/sim/enclosure/shielding_estimate.py` (model and checker in one script, `--check`), outputs `hardware/sim/enclosure/out/shielding.csv` and `out/bond.csv`, plot `docs/reviews/PDR/figures/shielding-estimate.png` (rendered and inspected 2026-09-27) |
| Review record | `docs/reviews/PDR/checklists/analysis-shielding-estimate.md` (`peer-review-checklist-analysis.md`, on the CR-012 branch until its merge) |
| Evidence status | Developer evidence. The script runs on the venv Python 3.13.5 (TV-001) with numpy 2.5.3 and matplotlib 3.11.2, which are class B entries of `tools/toolchain.lock.md` section 2 without a TV record of their own. The values below are proposals until this record is APPROVED (plan rule C10) |

## 1. Question

1. Does each enclosure option of TS-011 keep the digital and switching-converter fundamentals and harmonics at least 20 dB below their board-level near-field levels, as REQ-SYS-177 requires? If not, where and why not?
2. Does a sprayed coating meet the REQ-SYS-109 bond of 0.1 ohm from the farthest point of a coated part to the antenna-jack shell? At which surface resistivity?
3. Which design rules make the answers yes, and which part of the requirement no enclosure rule can reach?

REQ-SYS-177 is read two ways, because its statement says "radiated from its enclosure" while the owner's measurement method is a spectrum analyzer with a near-field H-field probe (status note section 3 row 8):
- (R) **radiated:** plane-wave shielding, Zw = 377 ohm;
- (H) **magnetic near field:** Zw = 2 pi f mu0 r with the source r = 10 mm from the wall, the front-stack clearance of the envelope drawing rounded up.

Both are reported. TS-011 screens on (R), the requirement's wording, and scores the (H) shortfall as criterion C4.

## 2. Inputs and sources

| Input | Value | Source and confidence |
|---|---|---|
| Source frequencies | 1.5 MHz (charger boost, BQ25887 class); 2.2 MHz (5 V buck, TPS62913 class); 12 MHz (Pico 2 crystal); 48 MHz (USB PLL); 144 MHz (12th of 12 MHz, 3rd of 48 MHz); 150 MHz (RP2350 system clock); 300 and 600 MHz (its 2nd and 4th); 1 GHz (upper edge of the evaluated range, author choice) | `docs/research/power-tree-and-charging.md` F19, R-PWR-03; `docs/research/display-and-ui-parts.md` F10 (Medium) |
| 6061 wall (A) | conductivity 2.5e7 S/m, 1.5 mm | concept 7.8 (1.5 mm minimum wall); 6061 conductivity about 40 % IACS, textbook value (Medium) |
| PCB plate (B) | copper 70 um in total (1 oz both faces bonded) | `pcbway-fabrication-and-assembly.md` F5 (1 oz outer) |
| Coating (C1, D) | Rs 0.01 to 20 ohm/sq swept; design value 0.03 ohm/sq; dry film 50 um | TS-011 Appendix B (recalled product values, Low); the design value is this note's proposal |
| Display window | 24 x 24 mm (diagonal 34 mm); ITO film 10 ohm/sq behind the lens (design rule) | `display-and-ui-parts.md` UI-DSP-05 (window); ITO film class value recalled (Low) |
| Other openings | USB 12 x 10 mm (diagonal 15.6), two jack holes 9 mm, two encoder holes 8.4 mm | ICD-CTL-USB 3.2.2; `hardware/enclosure/board-outline.json`; `docs/design/analysis/mechanical-tolerance-stack.md` S2, S3 |
| Opening depth | wall thickness: 1.5 mm (A), 1.6 mm (B), 2.0 mm (C1, D) | outline JSON |
| Joints | overlapping lip 3 mm; continuous conductive gasket modelled as contacts every 3 mm; variant: screws every 15 mm without gasket | design rule proposed here (TS-011 section 8 rule 7) |
| Joint length | A 0.42 m, B 0.56 m, C1 0.66 m, D 0.56 m | perimeters of the parts of each option in the envelope drawing (Low) |
| Bond geometry | part 140 mm long; M3 washer contact radius 3.5 mm; probe tip radius 0.5 mm; 0.010 ohm screw contact | envelope drawing; contact value author's planning (Low) |

## 3. Method

- **Wall.** The exact transmission of a uniform conductive slab between media of wave impedance Zw (Schelkunoff form). For a coating it reduces to the thin-film result SE = 20 log10(1 + Zw / (2 Rs)) when the film is thinner than its skin depth. For 6061 it gives the thick-wall absorption plus reflection.
- **Openings and joints.** Each opening leaks with amplitude 2L/lambda (L its largest dimension, L < lambda/2), reduced by the below-cutoff attenuation 27.3 d/L dB of its depth d. Joints are slots of the contact spacing with the 3 mm lip as depth.
- **Summation.** The wall and every leak add in power (random phase): SE = -20 log10 sqrt(T_wall^2 + sum T_i^2).
- **Bond.** The resistance between two small circular contacts on an infinite sheet, R = Rs/(2 pi) (ln(d/a1) + ln(d/a2)), plus the screw contact.
- **Checker.** `--check` asserts the verdicts of section 4 (the `EXPECTED` table in the script) and exits 1 on any difference. Run: `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/hardware/sim/enclosure/shielding_estimate.py --check`, result `CHECK PASS` on 2026-09-27.

## 4. Results

### 4.1 Total shielding, design rules applied (window film, gasketed joints), dB

Plane wave / H field. From `out/shielding.csv`.

| f MHz | Source | A | B | C1 | D | C1, window without film | C1, screw joints at 15 mm |
|---|---|---|---|---|---|---|---|
| 1.5 | charger boost | 76.2 / 69.6 | 76.4 / 48.2 | 73.6 / **9.5** | 73.6 / **9.5** | 69.1 | 64.9 |
| 2.2 | 5 V buck | 72.9 / 66.3 | 73.1 / 51.9 | 71.8 / **11.8** | 71.8 / **11.8** | 66.3 | 61.7 |
| 12 | Pico 2 crystal | 58.1 / 51.8 | 58.3 / 51.9 | 59.1 / 24.5 | 59.2 / 24.5 | 52.0 | 47.2 |
| 48 | USB PLL | 46.1 / 40.6 | 46.3 / 40.7 | 47.2 / 35.0 | 47.2 / 35.0 | 40.0 | 35.1 |
| 144 | 12th of 12 MHz | 36.5 / 32.6 | 36.8 / 32.7 | 37.7 / 33.0 | 37.7 / 33.1 | 30.4 | 25.6 |
| 150 | RP2350 clock | 36.2 / 32.3 | 36.4 / 32.5 | 37.3 / 32.8 | 37.3 / 32.8 | 30.1 | 25.2 |
| 300 | 2nd of 150 | 30.2 / 27.7 | 30.4 / 27.9 | 31.3 / 28.5 | 31.3 / 28.5 | 24.0 | **19.2** |
| 600 | 4th of 150 | 24.1 / 23.0 | 24.4 / 23.1 | 25.3 / 23.9 | 25.3 / 23.9 | **18.0** | **13.2** |
| 1000 | range edge | 19.7 / 19.1 | 19.9 / 19.3 | 20.8 / 20.2 | 20.8 / 20.2 | 13.6 | 8.7 |

The wall alone of C1 at 0.03 ohm/sq gives 76 to 81 dB in the plane wave and 9.5, 11.8, 24.5, 36.2, 45.8 dB (H field) at 1.5, 2.2, 12, 48 and 144 MHz. Above about 12 MHz the openings, not the walls, set the total of every option.

### 4.2 Verdicts (checker)

| Option | 12 to 600 MHz, rules applied, both readings >= 20 dB | 1.5 and 2.2 MHz, H field >= 20 dB | 12 to 600 MHz with the window open | 12 to 600 MHz with screw-only joints | 1 GHz within 3 dB of 20 dB (marginal) |
|---|---|---|---|---|---|
| A | pass (min 23.0) | pass (66.3) | fail (600 MHz) | fail | marginal (19.1) |
| B | pass (min 23.1) | pass (48.2) | fail | fail | marginal (19.3) |
| C1 | pass (min 23.9) | **fail (9.5)** | fail | fail | marginal (20.2) |
| D | pass (min 23.9) | **fail (9.5)** | fail | fail | marginal (20.2) |

### 4.3 Coating sweep (H field, wall only, source 10 mm)

At 1.5 MHz a coating needs about 0.007 ohm/sq to reach 20 dB, better than any aerosol of TS-011 Appendix B: 0.01 ohm/sq gives about 16.8 dB (plot, left panel). A nickel-class coating (0.7 ohm/sq) reaches 20 dB only above about 150 MHz. A carbon-class coating (20 ohm/sq) stays below 20 dB over the whole range.

## 5. Margins against the requirement (proposed value 20 dB)

| Case | Governing id and limit | Result | Margin | Uncertainty |
|---|---|---|---|---|
| C1, 12 to 600 MHz, rules applied | REQ-SYS-177: 20 dB (TBR) | 23.9 dB minimum (600 MHz, H field) | +3.9 dB | about +/-6 dB (aperture and joint model) |
| C1, 144 to 150 MHz (the in-band birdie sources of CON-009) | REQ-SYS-177 | 32.8 dB | +12.8 dB | as above |
| C1, 1.5 and 2.2 MHz, H field | REQ-SYS-177 | 9.5 and 11.8 dB | -10.5 and -8.2 dB | the wall term is the most certain in the model (+/-2 dB from Rs) |
| A, 1.5 and 2.2 MHz, H field | REQ-SYS-177 | 69.6 and 66.3 dB (openings limit) | +46 dB | as above |
| All options, 1 GHz | REQ-SYS-177 | 19.1 to 20.8 dB | -0.9 to +0.8 dB | about +/-6 dB: not discriminating |

## 6. Bond resistance (REQ-SYS-109, CR-003 revision 3)

| Rs (ohm/sq) | Bond points per part | Farthest point | R to the jack shell (ohm) | At most 0.1 ohm (TBR) |
|---|---|---|---|---|
| 0.01 | 1 / 2 | 140 / 70 mm | 0.0248 / 0.0226 | yes |
| **0.03** | 1 / 2 | 140 / 70 mm | 0.0545 / **0.0479** | yes |
| 0.1 | 1 / 2 | 140 / 70 mm | 0.158 / 0.136 | no |
| 0.7 | 1 / 2 | 140 / 70 mm | 1.05 / 0.894 | no |

Every other link of the chain is metal to metal: jack shell, port block through the nut and a toothed washer, M3 screws on coated lands, the coating, the heatsink through its conductive gasket. So the coating path decides the value. At Rs of 0.03 ohm/sq or less with two bond points per coated part, 0.1 ohm holds with a factor of 2 margin. Above about 0.07 ohm/sq it does not.

## 7. Conclusions and design rules

1. From 12 to 600 MHz every option meets 20 dB once the design rules hold:
   - a transparent conductive film in the display window;
   - continuous gasketed, lipped joints;
   - openings at the sizes of the stacks.

   Without the film, all options fall below 20 dB at 600 MHz. With screw-only joints, they fall below from about 300 MHz. These rules go to TS-011 section 8 (rules 7 and 8), to WP-PDR-39 (model) and WP-PDR-25 (display legibility through the film).
2. At the switcher fundamentals, 1.5 and 2.2 MHz, no sprayed coating gives 20 dB in the magnetic near field. The CNC wall does, with 46 dB of margin. The owner's H-probe measurement in the option C acceptance set (CR-003 section 5 item 3 (b)) will therefore show less than 20 dB there. This is a **question for the owner**, carried by TS-011 and plan PCR-9. Choose one of:
   - (a) a CR scoping REQ-SYS-177 to 10 MHz and above, with the converter fundamentals controlled by layout, synchronisation and filtering (R-PWR-03);
   - (b) board-level shield cans over the two converters, counted as part of the transceiver's shielding, which needs a definition of "board-level near-field level" (measured with the cans off) in the TC-SYS-107 procedure;
   - (c) accept that option C fails this item and order the CNC fallback.

   The lead SE recommends (b) plus the clarification. Tinplated steel cans absorb strongly at 1.5 MHz (skin depth about 11 um against 0.2 mm, an estimate). They also reduce receiver self-interference, whatever the enclosure.
3. At 1 GHz every option is marginal. The USB, jack and encoder openings set it, and they are common to all options, so this does not discriminate. The birdie survey at TRR and the near-field probe measurement close it.
4. **REQ-SYS-109:** propose to keep 0.1 ohm, with a coating design value of at most 0.03 ohm/sq (coupon, TS-011 Appendix B.4) and two bond points per coated part.
5. **REQ-SYS-177:** propose to keep 20 dB, with the frequency question of item 2 put to the owner.

## 8. Limitations

- The model is not a field solver. The slot formula is conservative for an open slot and uncertain for a gasketed joint, whose leakage depends on the gasket's transfer impedance (not modelled). The power sum assumes random phase. The aperture and joint terms together carry about +/-6 dB.
- The near-field (H) wave impedance assumes a small loop source at 10 mm. A closer source (a converter inductor near the back wall) lowers the H-field shielding further.
- Coating resistivities are recalled values (Low). The design value is a requirement on the coating, verified by the coupon, not a property of a chosen product.
- Developer evidence only. The tools are not accredited, and no measurement exists yet: the near-field probe (owner-actions E-01) and its TV record come before the option C shielding measurement (CR-003 section 5 step 19).

## 9. Proposed values (for the PDR memo, on an APPROVED record)

- REQ-SYS-177: 20 dB (keep), with the owner's choice among section 7 item 2 (a), (b) and (c).
- REQ-SYS-109: 0.1 ohm (keep), with coating Rs of at most 0.03 ohm/sq and two bond points per coated part.
