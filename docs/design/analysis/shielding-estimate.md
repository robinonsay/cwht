# Shielding and bond estimate per enclosure option

| Field | Value |
|---|---|
| Product | Analysis note (08 section 3.4), WP-PDR-27, PDR draft revision 1, 2026-09-27 (fixes INSP-083 finding-1; change log at the end) |
| Author | Claude, ME designer (WP-PDR-27 author invocation) |
| Status | Draft. **AT RISK (CR-003):** REQ-SYS-109 is taken in its CR-003 revision 3 wording (bond of every conductive enclosure part at 0.1 ohm TBR), which is Submitted and not dispositioned (plan rule C8) |
| Serves | REQ-SYS-177 (20 dB, TBR) and REQ-SYS-109 (0.1 ohm, TBR, CR-003) value proposals; TS-011 mandatory criterion M5 and enhancing criterion C4; the pre-build analyses TC-SYS-107 and TC-SYS-075 setup (CR-003 section 1.6) |
| Model, checker, plot | `hardware/sim/enclosure/shielding_estimate.py` (model and checker in one script, `--check`), outputs `hardware/sim/enclosure/out/shielding.csv`, `out/shielding-sources.csv` (revision 1: every source and harmonic to 1.5 GHz) and `out/bond.csv`, plot `docs/reviews/PDR/figures/shielding-estimate.png` (revision 1, three panels, rendered and inspected 2026-09-27) |
| Review record | `docs/reviews/PDR/checklists/analysis-shielding-estimate.md` (`peer-review-checklist-analysis.md`, on the CR-012 branch until its merge) |
| Evidence status | Developer evidence. The script runs on the venv Python 3.13.5 (TV-001) with numpy 2.5.3 and matplotlib 3.11.2, which are class B entries of `tools/toolchain.lock.md` section 2 without a TV record of their own. The values below are proposals until this record is APPROVED (plan rule C10) |

## 1. Question

1. Does each enclosure option of TS-011 keep every digital and switching-converter fundamental and every harmonic to 1.5 GHz at least 20 dB below its board-level near-field level, as REQ-SYS-177 requires and its closing case TC-SYS-107 computes ("every clock and switching-converter fundamental and its harmonics to 1.5 GHz", procedure step 1)? If not, where and why not?
2. Does a sprayed coating meet the REQ-SYS-109 bond of 0.1 ohm from the farthest point of a coated part to the antenna-jack shell? At which surface resistivity?
3. Which design rules make the answers yes, and which part of the requirement no enclosure rule can reach?

REQ-SYS-177 is read two ways, because its statement says "radiated from its enclosure" while the owner's measurement method is a spectrum analyzer with a near-field H-field probe (status note section 3 row 8):
- (R) **radiated:** plane-wave shielding, Zw = 377 ohm;
- (H) **magnetic near field:** Zw = 2 pi f mu0 r with the source r = 10 mm from the wall, the front-stack clearance of the envelope drawing rounded up.

Both are reported, and every verdict of revision 1 uses the lower of the two. TS-011 (revision 1) screens M5 on that verdict and scores the (H) shortfall below 4 MHz as criterion C4; its scope goes to the owner (section 7 item 3).

## 2. Inputs and sources

| Input | Value | Source and confidence |
|---|---|---|
| Sources (revision 1) | Every source of the WP-PDR-20 clock plan, `docs/design/analysis/clock-plan.md` revision 2 sections 2 and 2.1 (`4153acf`), 19 in all, each with its fundamental and every harmonic to 1.5 GHz, the tolerance band ends included: XOSC 12 MHz; clk_usb and clk_adc 48 MHz; clk_sys 150 MHz; TCXO 25 MHz; SPI SCK 18.75 MHz; QSPI SCK 37.5 MHz and 12.5 MHz (boot); PCM1808 SCKI 12.5 MHz (only if TS-001 keeps option B); BFO 9.0 to 10.7 MHz; prescaler 18 MHz (TX only); 5 V buck 2.4 MHz (synchronised); charger boost 1.5 MHz +/-10 % (off in operation, counted because REQ-SYS-177 names every converter); residual sources R-1 (RP2350 core regulator, 3 MHz typical, +/-20 % assumed, Low), R-2 (Pico 2 RT6150, about 2 MHz, Low), R-3 (charge pump 300 to 500 kHz), R-4 (I2C SCL 357 to 397 kHz), R-5 (RP2350 low-power oscillator, 32.768 kHz +/-20 %, always running); audio PWM 150 kHz; the RP2350 ring oscillator, 4.6 to 24.0 MHz (runs from power-up until the clocks driver moves off it; off in operation by clock-plan rule 11, counted for the boot interval). The converter harmonics between 1.5 and 12 MHz are therefore all in the set. The table of section 4.1 keeps illustrative spot frequencies | clock plan revision 2; `docs/research/power-tree-and-charging.md` F19, F20; `docs/research/display-and-ui-parts.md` F10 (Medium) |
| 6061 wall (A) | conductivity 2.5e7 S/m, 1.5 mm | concept 7.8 (1.5 mm minimum wall); 6061 conductivity about 40 % IACS, textbook value (Medium) |
| PCB plate (B) | copper 70 um in total (1 oz both faces bonded) | `pcbway-fabrication-and-assembly.md` F5 (1 oz outer) |
| Coating (C1, D) | Rs 0.01 to 20 ohm/sq swept; design value 0.03 ohm/sq; dry film 50 um | TS-011 Appendix B (recalled product values, Low); the design value is this note's proposal |
| Display window | 24 x 24 mm (diagonal 34 mm); ITO film 10 ohm/sq behind the lens (design rule) | `display-and-ui-parts.md` UI-DSP-05 (window); ITO film class value recalled (Low) |
| Other openings | Revision 0 set: USB 12 x 10 mm (diagonal 15.6), two jack holes 9 mm, two encoder holes 8.4 mm, each at the wall depth. Revision 1 set (rules O1 to O3 of section 7): USB receptacle mouth about 7.5 mm with 5 mm depth behind a bonded shroud; jack holes 9 mm with 8 mm depth (collar); encoder holes closed by bonded bushings, 8 contact slots of 3 mm per hole | ICD-CTL-USB 3.2.2; `hardware/enclosure/board-outline.json`; `docs/design/analysis/mechanical-tolerance-stack.md` S2, S3; receptacle mouth and depth are planning values (Low) |
| Opening depth | wall thickness: 1.5 mm (A), 1.6 mm (B), 2.0 mm (C1, D) | outline JSON |
| Joints | overlapping lip 3 mm; continuous conductive gasket modelled as contacts every 3 mm; variant: screws every 15 mm without gasket | design rule proposed here (TS-011 section 8 rule 7) |
| Joint length | A 0.42 m, B 0.56 m, C1 0.66 m, D 0.56 m | perimeters of the parts of each option in the envelope drawing (Low) |
| Bond geometry | part 140 mm long; M3 washer contact radius 3.5 mm; probe tip radius 0.5 mm; 0.010 ohm screw contact | envelope drawing; contact value author's planning (Low) |

## 3. Method

- **Wall.** The exact transmission of a uniform conductive slab between media of wave impedance Zw (Schelkunoff form). For a coating it reduces to the thin-film result SE = 20 log10(1 + Zw / (2 Rs)) when the film is thinner than its skin depth. For 6061 it gives the thick-wall absorption plus reflection.
- **Openings and joints.** Each opening leaks with amplitude 2L/lambda (L its largest dimension, L < lambda/2), reduced by the below-cutoff attenuation 27.3 d/L dB of its depth d. Joints are slots of the contact spacing with the 3 mm lip as depth.
- **Summation.** The wall and every leak add in power (random phase): SE = -20 log10 sqrt(T_wall^2 + sum T_i^2).
- **Bond.** The resistance between two small circular contacts on an infinite sheet, R = Rs/(2 pi) (ln(d/a1) + ln(d/a2)), plus the screw contact.
- **Every source and harmonic (revision 1).** The total (the lower of plane wave and H field) is computed on a grid of 1400 log-spaced points from 0.02 to 1500 MHz and read at every harmonic of every source, at the nominal frequency and at both tolerance-band ends. Per source the worst verdict over its harmonics is reported: **fail** below 20 dB; **not shown** when 20 dB is met by less than the case's uncertainty; **pass** otherwise (analysis checklist E3). The uncertainty is 6 dB for every case: the aperture and joint terms carry about +/-6 dB (section 8), and the H-field wall term, which Rs moves by only +/-2 dB, moves by about 5 dB when the source is 5 mm from the wall instead of 10 mm (INSP-083 finding-2).
- **Checker.** `--check` asserts the verdicts of section 4 (the `EXPECTED`, `EXPECTED_REV1` and `EXPECTED_BOND` tables in the script) and exits 1 on any difference. Run: `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/hardware/sim/enclosure/shielding_estimate.py --check`, result `CHECK PASS` on 2026-09-27 (revision 1).

## 4. Results

### 4.1 Total shielding at spot frequencies, dB (lower of plane wave and H field)

Revision 0 openings / openings with rules O1 to O3 (section 7), window film and gasketed joints in both. From `out/shielding.csv` (revision 0 openings, both readings, and the window and joint variants) and the script's `total_se` (rules O1 to O3).

| f MHz | Source | A | B | C1 | D |
|---|---|---|---|---|---|
| 0.033 | R-5 LPOSC | 40.1 / 40.1 | **16.0** / **16.0** | **0.4** / **0.4** | **0.4** / **0.4** |
| 1.5 | charger boost, R-2 | 69.6 / 70.6 | 48.2 / 48.2 | **9.5** / **9.5** | **9.5** / **9.5** |
| 2.4 | 5 V buck (synchronised) | 65.5 / 66.5 | 52.7 / 52.8 | **12.4** / **12.4** | **12.4** / **12.4** |
| 3 | R-1, harmonics of the dense sources | 63.6 / 64.6 | 54.9 / 55.0 | **13.9** / **13.9** | **13.9** / **13.9** |
| 6 | harmonics of the dense sources | 57.6 / 58.7 | 57.0 / 57.8 | **19.0** / **19.0** | **19.0** / **19.0** |
| 9 | BFO (IF 9 MHz) | 54.2 / 55.3 | 54.2 / 55.2 | 22.2 / 22.2 | 22.2 / 22.2 |
| 12 | XOSC | 51.8 / 52.9 | 51.9 / 52.9 | 24.5 / 24.5 | 24.5 / 24.5 |
| 48 | clk_usb, clk_adc | 40.6 / 41.9 | 40.7 / 42.0 | 35.0 / 35.2 | 35.0 / 35.2 |
| 150 | clk_sys | 32.3 / 34.5 | 32.5 / 34.6 | 32.8 / 34.6 | 32.8 / 34.6 |
| 300 | 2nd of 150 MHz | 27.7 / 31.1 | 27.9 / 31.2 | 28.5 / 31.5 | 28.5 / 31.5 |
| 600 | 4th of 150 MHz | 23.0 / 28.5 | 23.1 / 28.6 | 23.9 / 29.0 | 23.9 / 29.1 |
| 900 | 6th of 150 MHz | 20.0 / 27.2 | 20.2 / 27.3 | 21.0 / 27.8 | 21.0 / 27.9 |
| 1050 | 7th of 150 MHz | **18.8** / 26.7 | **19.0** / 26.8 | **19.8** / 27.4 | **19.8** / 27.4 |
| 1200 | 8th of 150 MHz, 25th of 48 MHz | **17.7** / 26.3 | **17.9** / 26.4 | **18.7** / 26.9 | **18.8** / 27.0 |
| 1500 | 10th of 150 MHz (TC-SYS-107 edge) | **15.9** / 25.4 | **16.1** / 25.6 | **17.0** / 26.2 | **17.0** / 26.3 |

Bold: below 20 dB. With the revision 0 openings every option is below 20 dB from about 0.9 to 1.05 GHz up to 1.5 GHz, the CNC fallback included (INSP-083 finding-1 confirmed). The USB opening (15.6 mm) dominates there. With rules O1 to O3 the top of the range recovers by 8 to 9 dB. The wall of a coating sets the total of C1 and D below about 30 MHz, and there it is below 20 dB up to about 7 MHz in the H field.

The window and joint variants of revision 0 (window without film, screw-only joints at 15 mm) still fall below 20 dB from 600 MHz and from 300 MHz (`out/shielding.csv` columns `se_plane_open_window_db`, `se_plane_screw_joints_db`), so rules 7 and 8 of TS-011 stay.

### 4.2 Verdict per source (every harmonic to 1.5 GHz), rules O1 to O3 applied

From `out/shielding-sources.csv`. "Lowest" is the lowest total over the fundamental and every harmonic to 1.5 GHz, the tolerance band ends included; the uncertainty of every case is 6 dB (section 3).

| Source (harmonics to 1.5 GHz) | C1 and D: lowest dB at MHz | C1 and D verdict | A: lowest dB at MHz | A verdict (B within 0.2 dB of A) |
|---|---|---|---|---|
| XOSC 12 MHz (125) | 24.5 at 12.0 (wall) | not shown | 25.4 at 1500 | not shown |
| clk_usb and clk_adc 48 MHz (31) | 26.2 at 1488 | pass | 25.5 at 1488 | not shown |
| clk_sys 150 MHz (10) | 26.2 at 1500 | pass | 25.4 at 1500 | not shown |
| TCXO 25 MHz (60) | 26.2 at 1500 | pass | 25.4 at 1500 | not shown |
| SPI SCK 18.75 MHz (80) | 26.2 at 1500 | pass | 25.4 at 1500 | not shown |
| QSPI SCK 37.5 MHz (40) | 26.2 at 1500 | pass | 25.4 at 1500 | not shown |
| QSPI SCK 12.5 MHz, boot (120) | 24.8 at 12.5 (wall) | not shown | 25.4 at 1500 | not shown |
| PCM1808 SCKI 12.5 MHz, option B only (120) | 24.8 at 12.5 (wall) | not shown | 25.4 at 1500 | not shown |
| BFO 9.0 to 10.7 MHz (166) | 22.2 at 9.0 (wall) | not shown | 25.4 at 1498 | not shown |
| prescaler 18 MHz, TX only (84) | 26.2 at 1497 | pass | 25.4 at 1497 | not shown |
| 5 V buck 2.4 MHz (625) | 12.4 at 2.4 (wall) | **fail**, 2.4 to 4.8 MHz | 25.4 at 1500 | not shown |
| charger boost 1.5 MHz +/-10 % (1111) | 8.9 at 1.35 (wall) | **fail**, 1.35 to 6.75 MHz | 25.4 at 1500 | not shown |
| R-1 core regulator 3 MHz (624) | 12.4 at 2.4 (wall) | **fail**, 2.4 to 6.0 MHz | 25.4 at 1500 | not shown |
| R-2 RT6150 about 2 MHz (1000) | 9.5 at 1.5 (wall) | **fail**, 1.5 to 6.0 MHz | 25.4 at 1500 | not shown |
| R-3 charge pump 300 to 500 kHz (4999) | 2.9 at 0.3 (wall) | **fail**, 0.3 to 6.8 MHz | 25.4 at 1500 | not shown |
| R-4 I2C SCL (4201) | 3.3 at 0.36 (wall) | **fail**, 0.36 to 6.8 MHz | 25.4 at 1500 | not shown |
| audio PWM 150 kHz (10000) | 1.6 at 0.15 (wall) | **fail**, 0.15 to 6.75 MHz | 25.4 at 1500 | not shown |
| R-5 LPOSC 32.768 kHz +/-20 % (57220) | 0.3 at 0.03 (wall) | **fail**, 0.03 to 6.8 MHz | 25.4 at 1500 | not shown (B fails, 14.3 dB at 33 kHz) |
| RP2350 ROSC 4.6 to 24 MHz, boot only (325) | 17.0 at 4.6 (wall) | **fail** at 4.6 MHz | 25.4 at 1496 | not shown |

Every source of the clock plan has harmonics up to 1.5 GHz, so every source of A and B inherits the 1.5 GHz case (25.4 dB and 25.6 dB, margins 5.4 and 5.6 dB, not shown). C1 and D pass there with 6.2 and 6.3 dB, only just more than the uncertainty.

### 4.3 Verdicts (checker)

| Option | Revision 0 openings: 12 to 600 MHz, both readings >= 20 dB | 1.5 and 2.2 MHz, H field >= 20 dB | Revision 0 openings: 750 to 1500 MHz >= 20 dB | Every source, rules O1 to O3: failing sources | Every source, rules O1 to O3: not shown |
|---|---|---|---|---|---|
| A | pass (min 23.0) | pass (66.3) | **fail** (15.9 at 1500 MHz) | none | all 19 (the 1.5 GHz case, 25.4 dB) |
| B | pass (min 23.1) | pass (48.2) | **fail** (16.1) | R-5 (14.3 dB at 33 kHz) | the other 18 (25.6 dB) |
| C1 | pass (min 23.9) | **fail (9.5)** | **fail** (17.0) | 9: the 8 sources below 4 MHz and the boot-time ROSC (0.03 to 6.8 MHz) | 4: XOSC 12 MHz, QSPI 12.5 MHz, PCM1808 12.5 MHz, BFO |
| D | pass (min 23.9) | **fail (9.5)** | **fail** (17.0) | as C1 | as C1 |

### 4.4 Coating sweep (H field, wall only, source 10 mm)

At 1.5 MHz a coating needs about 0.007 ohm/sq to reach 20 dB, better than any aerosol of TS-011 Appendix B: 0.01 ohm/sq gives about 16.8 dB (plot, left panel). A nickel-class coating (0.7 ohm/sq) reaches 20 dB only above about 150 MHz. A carbon-class coating (20 ohm/sq) stays below 20 dB over the whole range. Below 0.3 MHz no coating gives more than a few dB in the H field; the 6061 wall of A gives 60 dB or more down to 0.1 MHz.

## 5. Margins against the requirement (proposed value 20 dB)

Every case below carries the 6 dB uncertainty of section 3; a margin smaller than that is reported as not shown, never as a pass (analysis checklist E3).

| Case | Governing id and limit | Result | Margin | Status |
|---|---|---|---|---|
| C1 and D, 12.5 MHz up to 1.5 GHz, rules O1 to O3 | REQ-SYS-177: 20 dB (TBR); TC-SYS-107 to 1.5 GHz | 24.8 dB at 12.5 MHz rising to 36 dB near 80 MHz, then 26.2 dB at 1.5 GHz | +4.8 to +6.2 dB at the ends | not shown at 12 to 12.5 MHz; pass (6.2 dB) at 1.5 GHz, only just |
| C1 and D, 12 MHz (XOSC) and 9 to 10.7 MHz (BFO) | REQ-SYS-177 | 24.5 and 22.2 dB | +4.5 and +2.2 dB | not shown |
| C1 and D, sources below 4 MHz and their harmonics to about 7 MHz, and the ROSC at boot | REQ-SYS-177 | 0.3 to 19 dB (H field) | -19.7 to -1.0 dB | fail |
| C1, 144 to 150 MHz (the in-band birdie sources of CON-009) | REQ-SYS-177 | 34.6 dB | +14.6 dB | pass |
| A and B, every source (the 1.5 GHz case) | REQ-SYS-177; TC-SYS-107 | 25.4 and 25.6 dB | +5.4 and +5.6 dB | not shown |
| A, sources below 4 MHz | REQ-SYS-177 | 40 dB or more (40.1 dB at 33 kHz, 58 dB or more from 1.5 MHz) | +20 dB or more | pass |
| Every option, revision 0 openings, 0.9 to 1.5 GHz | REQ-SYS-177; TC-SYS-107 | 15.9 to 20.0 dB | down to -4.1 dB | fail (the revision 0 statement of section 7 item 3, "marginal", is withdrawn) |

## 6. Bond resistance (REQ-SYS-109, CR-003 revision 3)

| Rs (ohm/sq) | Bond points per part | Farthest point | R to the jack shell (ohm) | At most 0.1 ohm (TBR) |
|---|---|---|---|---|
| 0.01 | 1 / 2 | 140 / 70 mm | 0.0248 / 0.0226 | yes |
| **0.03** | 1 / 2 | 140 / 70 mm | 0.0545 / **0.0479** | yes |
| 0.1 | 1 / 2 | 140 / 70 mm | 0.158 / 0.136 | no |
| 0.7 | 1 / 2 | 140 / 70 mm | 1.05 / 0.894 | no |

Every other link of the chain is metal to metal: jack shell, port block through the nut and a toothed washer, M3 screws on coated lands, the coating, the heatsink through its conductive gasket. So the coating path decides the value. At Rs of 0.03 ohm/sq or less with two bond points per coated part, 0.1 ohm holds with a factor of 2 margin. Above about 0.07 ohm/sq it does not.

## 7. Conclusions and design rules

1. **Joints and window (revision 0 rules, kept).** Every option needs a transparent conductive film in the display window and continuous gasketed, lipped joints. Without the film all options fall below 20 dB at 600 MHz; with screw-only joints they fall below from about 300 MHz. These rules are TS-011 section 8 rules 7 and 8, and go to WP-PDR-39 (model) and WP-PDR-25 (display legibility through the film). If the display is dropped (status note 2026-09-27 section 6, not yet a requirement change), the window term goes and the film rule with it.
2. **Openings (revision 1 rules O1 to O3, new).** With the revision 0 openings every option, the CNC fallback included, is below 20 dB from about 0.9 to 1.05 GHz up to 1.5 GHz, and the USB opening (15.6 mm) sets it. The rules below recover 8 to 9 dB at 1.5 GHz. They apply to every option and go to TS-011 section 8 (rule 16), WP-PDR-39 and WP-PDR-36 (ICD-CTL-USB, ICD-CTL-KEY):
   - **O1 USB shroud.** The micro-USB receptacle sits at the inner end of a coated shroud (printed for C1 and D, machined for A) that joins the 12.6 x 10.6 mm wall opening to the receptacle shell. A conductive gasket bonds the shroud to the shell all round, so the only leak into the interior is the receptacle mouth (about 7.5 x 2.5 mm) with its own 5 mm depth below cutoff. The mouth and depth are planning values (Low) until WP-PDR-38 chooses the part.
   - **O2 Jack collars.** Each 3.5 mm jack nose passes through a coated collar 6 mm deep behind the 2 mm wall (8 mm below-cutoff depth for the 9 mm opening), bonded to the coating.
   - **O3 Bonded encoder bushings.** Each encoder's metal bushing is bonded to the coated front wall by its panel nut and a toothed washer on a coated land, so metal closes the hole and only the contact ring leaks.

   With O1 to O3, C1 and D pass from 12.5 MHz to 1.5 GHz for every clock except the fundamentals near 12 MHz (XOSC, QSPI boot SCK, PCM1808 SCKI) and the BFO, which the coating wall limits to 22 to 25 dB. Those four are **not shown** (margin 2.2 to 4.8 dB, below 6 dB). A and B are **not shown** at 1.5 GHz (25.4 and 25.6 dB), which every source reaches through its harmonics. No further opening rule is proposed at PDR, because the remaining leaks (joints, encoder rings, window) are spread over many small terms.
3. **Sources below 4 MHz (C1 and D).** No sprayed coating gives 20 dB in the magnetic near field below about 7 MHz. That range holds the fundamentals and low harmonics of eight sources and the boot-time ROSC: the synchronised 5 V buck, the charger boost, residual sources R-1 to R-5, the audio PWM and the ROSC. The CNC wall of A gives 40 dB or more there. Board shield cans (revision 0 item 2 (b)) can cover the buck and the charger, and R-1, R-2, R-5 and the ROSC only with a can over the whole Pico 2 module. They cannot cover the I2C lines (R-4) or the audio PWM traces, which run across the board. So option (b) alone no longer closes the item. **Question for the owner**, carried by TS-011 and plan PCR-9, now in this form:
   - (a) a CR scoping REQ-SYS-177 to 10 MHz and above, with the sources below it controlled by layout, filtering, the clock-plan rules and the REQ-SYS-034 receiver Test (the lead SE's recommendation for option C);
   - (b) (a) plus board-level shield cans over the 5 V buck and the charger, as good practice for the receiver, whatever the enclosure;
   - (c) keep REQ-SYS-177 over the whole range and order the CNC fallback (A), which fails no source but is itself not shown at 1.5 GHz (item 2).
4. **Scope of the 1.5 GHz edge.** Whatever the owner rules in item 3, every option is within 6 dB of 20 dB at 1.5 GHz by this model. REQ-SYS-177 is an Analysis requirement closed by TC-SYS-107 on the CDR design data (04 section 5.1 item 5), so a TRR measurement cannot close it. The CDR analysis (TC-SYS-107 with the STEP openings and the worst-case corners of its step 4) must show the margin, or the owner accepts the not-shown cases by name in the same PCR-9 ruling. The near-field probe measurement of the option C acceptance set (CR-003 section 5 item 3 (b)) is supporting data only.
5. **REQ-SYS-109:** propose to keep 0.1 ohm, with a coating design value of at most 0.03 ohm/sq (coupon, TS-011 Appendix B.4) and two bond points per coated part.
6. **REQ-SYS-177:** propose to keep 20 dB. The frequency scope (item 3) and the not-shown cases (items 2 and 4) go to the owner with PCR-9.

## 8. Limitations

- The model is not a field solver. The slot formula is conservative for an open slot and uncertain for a gasketed joint, whose leakage depends on the gasket's transfer impedance (not modelled). The power sum assumes random phase. The aperture and joint terms together carry about +/-6 dB.
- The near-field (H) wave impedance assumes a small loop source at 10 mm. A closer source (a converter inductor near the back wall) lowers the H-field shielding further.
- Coating resistivities are recalled values (Low). The design value is a requirement on the coating, verified by the coupon, not a property of a chosen product.
- Developer evidence only. The tools are not accredited, and no measurement exists yet: the near-field probe (owner-actions E-01) and its TV record come before the option C shielding measurement (CR-003 section 5 step 19).

## 9. Proposed values (for the PDR memo, on an APPROVED record)

- REQ-SYS-177: 20 dB (keep), with the owner's choice among section 7 item 3 (a), (b) and (c), and the not-shown cases of section 7 items 2 and 4 named in the same ruling (PCR-9).
- REQ-SYS-109: 0.1 ohm (keep), with coating Rs of at most 0.03 ohm/sq and two bond points per coated part.

## Change log

| Revision | Date | Change | Reason |
|---|---|---|---|
| 0 | 2026-09-27 | Initial draft, wave 1a | WP-PDR-27 |
| 1 | 2026-09-27 | Section 1 question 1, section 2 source row and openings row, section 3 (every source and harmonic, 6 dB uncertainty), section 4 (spot table to 1.5 GHz, per-source verdicts, checker verdicts), section 5 (status column; not shown cases), section 7 (opening rules O1 to O3; the sources below 4 MHz; the owner question restated; the 1.5 GHz edge), section 9 wording. Sources per clock plan revision 2 (19, with R-5 and the ROSC). Script: `CLOCK_SOURCES`, `OPENINGS`, `per_source`, `EXPECTED_REV1`, new output `out/shielding-sources.csv`, three-panel plot | INSP-083 finding-1 (Major) |
