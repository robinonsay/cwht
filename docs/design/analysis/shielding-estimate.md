# Shielding and bond estimate per enclosure option

| Field | Value |
|---|---|
| Product | Analysis note (08 section 3.4), WP-PDR-27, PDR draft revision 2, 2026-09-27 (revision 1 fixed INSP-083 finding-1; revision 2 fixes finding-5, the plug-inserted state; change log at the end) |
| Author | Claude, ME designer (WP-PDR-27 author invocation) |
| Status | Draft. **AT RISK (CR-003):** REQ-SYS-109 is taken in its CR-003 revision 3 wording (bond of every conductive enclosure part at 0.1 ohm TBR), which is Submitted and not dispositioned (plan rule C8) |
| Serves | REQ-SYS-177 (20 dB, TBR) and REQ-SYS-109 (0.1 ohm, TBR, CR-003) value proposals; TS-011 mandatory criterion M5 and enhancing criterion C4; the pre-build analyses TC-SYS-107 and TC-SYS-075 setup (CR-003 section 1.6) |
| Model, checker, plot | `hardware/sim/enclosure/shielding_estimate.py` (model and checker in one script, `--check`), outputs `hardware/sim/enclosure/out/shielding.csv`, `out/shielding-sources.csv` (revision 1: every source and harmonic to 1.5 GHz; revision 2 adds the port states of section 3) and `out/bond.csv`, plot `docs/reviews/PDR/figures/shielding-estimate.png` (revision 2, three panels, rendered and inspected 2026-09-27) |
| Review record | `docs/reviews/PDR/checklists/analysis-shielding-estimate.md` (`peer-review-checklist-analysis.md`, on the CR-012 branch until its merge) |
| Evidence status | Developer evidence. The script runs on the venv Python 3.13.5 (TV-001) with numpy 2.5.3 and matplotlib 3.11.2, which are class B entries of `tools/toolchain.lock.md` section 2 without a TV record of their own. The values below are proposals until this record is APPROVED (plan rule C10) |

## 1. Question

1. Does each enclosure option of TS-011 keep every digital and switching-converter fundamental and every harmonic to 1.5 GHz at least 20 dB below its board-level near-field level, as REQ-SYS-177 requires and its closing case TC-SYS-107 computes ("every clock and switching-converter fundamental and its harmonics to 1.5 GHz", procedure step 1)? If not, where and why not?
2. Does a sprayed coating meet the REQ-SYS-109 bond of 0.1 ohm from the farthest point of a coated part to the antenna-jack shell? At which surface resistivity?
3. Which design rules make the answers yes, and which part of the requirement no enclosure rule can reach?
4. (Revision 2, INSP-083 finding-5.) Do the answers hold in the operating state, with the key or paddle plug in the key jack, headphones in the phones jack and a cable in the USB receptacle? The key jack holds a plug in every transmit and receive state, REQ-SYS-117 names the "plugs inserted" state, and TC-SYS-107 covers every aperture at its worst-case corner.

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
| Port states (revision 2) | Empty: no plug and no cable. Plugged: a 3.5 mm plug in the key jack and in the phones jack and a micro-USB cable in the receptacle, all at once (the worst case; each plug only adds leak terms, except the USB plug, whose mated seam replaces the empty mouth) | INSP-083 finding-5; REQ-SYS-117 ("plugs inserted"); TC-SYS-107 procedure step 4 |
| Jack parts (revision 2, rule O2) | Metal-nose 3.5 mm jack: the nose (6.0 mm outside, 3.6 mm bore, metal for 5 mm) is the sleeve contact. Conductive gasket ring between the nose and the collar bore, compliant over the stack S2 radial gap of 0.85 to 2.15 mm | planning values (Low) until WP-PDR-38 chooses the part; nose 6.0 mm per `mechanical-tolerance-stack.md` inputs; bore 3.6 mm for a 3.5 mm plug |
| Jack-line filters (revision 2, rule O4) | Key tip and ring: series 1 kohm thick film (0.05 pF parasitic) and 10 nF shunt. Phones tip and ring: series ferrite bead of the 600 ohm at 100 MHz class (modelled as 700 ohm in parallel with 1.2 uH and 0.5 pF, plus 0.05 ohm) and 10 nF shunt. Each shunt capacitor modelled with 0.6 nH and 0.05 ohm (0402 with its via). Each filter within 5 mm of the jack pin, returned to the jack's bonded sleeve pin | author's planning values, recalled class values (Low); WP-PDR-37 places them, WP-PDR-38 chooses them |
| Conducted-term model (revision 2) | Board-level noise source 50 ohm; cable common-mode load 150 ohm; coupling of the board-level noise onto a jack line at the jack pins K = 1 (0 dB) | 150 ohm is the usual common-mode impedance of conducted-emission practice (recalled, not in the corpus, Low); K = 1 is a bound, since no layout exists (WP-PDR-37) |
| USB with a cable (revision 2) | The plug shell fills the receptacle mouth and mates the receptacle shell, which rule O1 bonds to the shroud; the leak is the mated seam, modelled as the two long sides of the plug shell (6.9 mm) with 3 mm engagement depth. The USB conductors stay inside the cable shield, which the plug shell bonds to the shroud at the wall | micro-USB plug shell size recalled (Low); ICD-CTL-USB 3.2.2 |
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
- **Port states (revision 2).** Below-cutoff attenuation exists only for an empty opening. With a plug in a jack, the plug sleeve and the metal around it form a coaxial line, which has no cutoff, and the plug's tip and ring conductors leave the shield on the cable. So each port state has its own leak set (`STATES` in the script):
  - `rev1_plug`: rules O1 to O3 of revision 1 with the ports plugged. Each jack is its 9 mm opening with no depth credit, and the USB is the mated seam. The unfiltered jack conductors are not bounded by any model here, so no case of this state is reported as a pass: every verdict is capped at "not shown".
  - `rev2`: rules O1 to O4 with the ports empty. Each jack leaks at its gasket contact ring (8 slots of 3 mm at the 2 mm wall depth, the O3 model) and through the empty nose bore (3.6 mm, 5 mm deep).
  - `rev2_plug`: rules O1 to O4 with the ports plugged. The plug fills the bore. Its sleeve is bonded at the wall through the nose, so the coaxial line between the plug sleeve and the nose is not driven from inside, and the jack leaks at its contact ring. Each of the four jack lines (key tip and ring, phones tip and ring) adds a conducted term T = K x |H|. H is the voltage transfer of its O4 filter from the 50 ohm source into the 150 ohm cable common-mode load, relative to no filter, and K = 1 is the bound of section 2. The USB leaks at its mated seam.
  - The governing revision 2 verdict per source is the worse of `rev2` and `rev2_plug` at every harmonic (TC-SYS-107 worst case, `rev2_worst` in the output).
- **Checker.** `--check` asserts the verdicts of section 4 (the `EXPECTED`, `EXPECTED_REV1`, `EXPECTED_REV2`, `EXPECTED_SCOPE` and `EXPECTED_BOND` tables in the script) and exits 1 on any difference. Run: `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/hardware/sim/enclosure/shielding_estimate.py --check`, result `CHECK PASS` on 2026-09-27 (revision 2). The revision 0 and revision 1 outputs are unchanged by revision 2: `shielding.csv` and `bond.csv` are byte-identical, and `shielding-sources.csv` keeps its revision 1 rows and adds the rows of the new states.

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

### 4.2 Verdict per source (every harmonic to 1.5 GHz), rules O1 to O3 applied, ports empty (revision 1; superseded for the verdict by section 4.6)

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

Every source of the clock plan has harmonics up to 1.5 GHz, so every source of A and B inherits the 1.5 GHz case (25.4 dB and 25.6 dB, margins 5.4 and 5.6 dB, not shown). C1 and D pass there with 6.2 and 6.3 dB, only just more than the uncertainty. **These are empty-port results. They do not hold with a plug inserted (section 4.5).**

### 4.3 Verdicts (checker, revisions 0 and 1)

| Option | Revision 0 openings: 12 to 600 MHz, both readings >= 20 dB | 1.5 and 2.2 MHz, H field >= 20 dB | Revision 0 openings: 750 to 1500 MHz >= 20 dB | Every source, rules O1 to O3: failing sources | Every source, rules O1 to O3: not shown |
|---|---|---|---|---|---|
| A | pass (min 23.0) | pass (66.3) | **fail** (15.9 at 1500 MHz) | none | all 19 (the 1.5 GHz case, 25.4 dB) |
| B | pass (min 23.1) | pass (48.2) | **fail** (16.1) | R-5 (14.3 dB at 33 kHz) | the other 18 (25.6 dB) |
| C1 | pass (min 23.9) | **fail (9.5)** | **fail** (17.0) | 9: the 8 sources below 4 MHz and the boot-time ROSC (0.03 to 6.8 MHz) | 4: XOSC 12 MHz, QSPI 12.5 MHz, PCM1808 12.5 MHz, BFO |
| D | pass (min 23.9) | **fail (9.5)** | **fail** (17.0) | as C1 | as C1 |

### 4.4 Coating sweep (H field, wall only, source 10 mm)

At 1.5 MHz a coating needs about 0.007 ohm/sq to reach 20 dB, better than any aerosol of TS-011 Appendix B: 0.01 ohm/sq gives about 16.8 dB (plot, left panel). A nickel-class coating (0.7 ohm/sq) reaches 20 dB only above about 150 MHz. A carbon-class coating (20 ohm/sq) stays below 20 dB over the whole range. Below 0.3 MHz no coating gives more than a few dB in the H field; the 6061 wall of A gives 60 dB or more down to 0.1 MHz.

### 4.5 Port states (revision 2, INSP-083 finding-5)

Total shielding in dB, the lower of plane wave and H field, from the script's `total_se` for each state of section 3. Columns per option: rules O1 to O3 with the ports empty (revision 1) / rules O1 to O3 plugged, aperture only / rules O1 to O4 empty / rules O1 to O4 plugged.

| f MHz | A | B | C1 | D |
|---|---|---|---|---|
| 0.033 | 40.1 / 40.1 / 40.1 / **0.0** | **16.0** / **16.0** / **16.0** / **0.0** | **0.4** / **0.4** / **0.4** / **0.0** | as C1 |
| 0.15 | 73.0 / 72.9 / 73.0 / **0.0** | 28.0 / 28.0 / 28.0 / **0.0** | **1.6** / **1.6** / **1.6** / **0.0** | as C1 |
| 1.5 | 70.6 / 69.8 / 70.5 / **8.2** | 48.2 / 48.2 / 48.2 / **8.2** | **9.5** / **9.5** / **9.5** / **5.7** | as C1 |
| 2.4 | 66.5 / 65.8 / 66.5 / **12.4** | 52.8 / 52.8 / 52.8 / **12.4** | **12.4** / **12.4** / **12.4** / **9.4** | as C1 |
| 4.8 | 60.6 / 59.8 / 60.5 / **19.9** | 58.1 / 57.6 / 58.1 / **19.9** | **17.3** / **17.3** / **17.3** / **15.4** | as C1 |
| 9 | 55.3 / 54.5 / 55.2 / 28.4 | 55.2 / 54.4 / 55.2 / 28.4 | 22.2 / 22.2 / 22.2 / 21.3 | as C1 |
| 10 | 54.4 / 53.6 / 54.3 / 30.0 | 54.4 / 53.6 / 54.4 / 30.0 | 23.0 / 23.0 / 23.0 / 22.2 | as C1 |
| 12 | 52.9 / 52.0 / 52.8 / 32.9 | 52.9 / 52.1 / 52.9 / 32.9 | 24.5 / 24.5 / 24.5 / 23.9 | as C1 |
| 150 | 34.5 / 32.8 / 34.4 / 34.3 | 34.6 / 32.9 / 34.5 / 34.4 | 34.6 / 32.9 / 34.6 / 34.5 | as C1 |
| 600 | 28.5 / 23.9 / 28.3 / 27.8 | 28.6 / 23.9 / 28.4 / 27.9 | 29.0 / 24.1 / 29.0 / 28.4 | 29.1 / 24.1 / 29.0 / 28.4 |
| 1050 | 26.7 / **19.9** / 26.2 / 24.8 | 26.8 / **19.9** / 26.4 / 25.0 | 27.4 / 20.0 / 27.2 / 25.5 | as C1 |
| 1200 | 26.3 / **18.8** / 25.7 / 23.9 | 26.4 / **18.9** / 25.9 / 24.0 | 26.9 / **19.0** / 26.7 / 24.5 | 27.0 / **19.0** / 26.8 / 24.6 |
| 1500 | 25.4 / **17.1** / 24.7 / 22.0 | 25.6 / **17.1** / 24.9 / 22.1 | 26.2 / **17.2** / 25.9 / 22.6 | 26.3 / **17.2** / 26.0 / 22.6 |

Bold: below 20 dB. What the plugged state does:

- **With the revision 1 rules, a plug removes the collar credit.** The aperture alone gives 17.1 to 17.2 dB at 1.5 GHz in every option, below 20 dB from about 1.05 GHz, as the reviewer computed (INSP-083 finding-5). The unfiltered tip and ring conductors add a leak that no term of this model bounds. **Every source fails in every option** in this state (`rev1_plug`: 19 of 19), because every source has a harmonic above 1.05 GHz. Rule O2 of revision 1 is therefore withdrawn as a shielding credit (section 7 item 2).
- **With rules O1 to O4, from 10 MHz up nothing fails in any option in either state.** The lowest totals from 10 MHz to 1.5 GHz are A 22.0 dB and B 22.1 dB (at 1.5 GHz, plugged), and C1 and D 22.3 dB (at 10 MHz, coating wall with the plugged lines) and 22.6 dB at 1.5 GHz. Every margin is 2.0 to 2.6 dB, below the 6 dB uncertainty: **not shown**. At 1.5 GHz the phones-line bead, whose 0.5 pF parasitic limits its impedance, and the USB mated seam set the plugged total. The empty-port total with O4 is 0.3 dB lower than revision 1 at 1.5 GHz (C1 25.9 against 26.2 dB), because the gasket contact rings of the jacks leak more than the empty 8 mm collars.
- **Below about 5 MHz the plugged state fails in every option, A included**, through the conducted term of the jack lines. With K = 1 the phones filter gives 0.5 dB at 150 kHz, 11.2 dB at 1.5 MHz and 22.9 dB at 4.8 MHz, and the key filter 15.9 dB at 33 kHz and 19.6 dB at 150 kHz (script `line_t`). The fail is a bound, not a prediction: the real coupling of the board-level noise onto a jack line depends on the layout and the audio reconstruction filter, With a coupling 26 dB below K = 1 (20 dB plus the 6 dB uncertainty) on every jack line, A fails no source: each low source is then limited by its own harmonics near 1.5 GHz and is not shown (author's run of the script with K scaled). No part of the design shows that coupling yet.

### 4.6 Verdict per source, rules O1 to O4, worse of empty and plugged ports (revision 2, governing)

From `out/shielding-sources.csv` rows `rev2_worst`. "Limiting" is the term that carries more than half the leak power at the lowest point ("openings and joints" when no single class does).

| Source (harmonics to 1.5 GHz) | C1 and D: lowest dB at MHz, limiting | C1 and D verdict | A: lowest dB at MHz, limiting | A verdict (B within 0.2 dB of A) |
|---|---|---|---|---|
| XOSC 12 MHz | 22.6 at 1500, openings and joints | not shown | 22.0 at 1500, openings and joints | not shown |
| clk_usb and clk_adc 48 MHz | 22.7 at 1488 | not shown | 22.0 at 1488 | not shown |
| clk_sys 150 MHz | 22.6 at 1500 | not shown | 22.0 at 1500 | not shown |
| TCXO 25 MHz | 22.6 at 1500 | not shown | 22.0 at 1500 | not shown |
| SPI SCK 18.75 MHz | 22.6 at 1500 | not shown | 22.0 at 1500 | not shown |
| QSPI SCK 37.5 MHz | 22.6 at 1500 | not shown | 22.0 at 1500 | not shown |
| QSPI SCK 12.5 MHz, boot | 22.6 at 1500 | not shown | 22.0 at 1500 | not shown |
| PCM1808 SCKI 12.5 MHz, option B only | 22.6 at 1500 | not shown | 22.0 at 1500 | not shown |
| BFO 9.0 to 10.7 MHz | 21.3 at 9.0, wall | not shown | 22.0 at 1498 | not shown |
| prescaler 18 MHz, TX only | 22.6 at 1497 | not shown | 22.0 at 1497 | not shown |
| 5 V buck 2.4 MHz | 9.4 at 2.4, wall | **fail**, 2.4 to 7.2 MHz | 12.4 at 2.4, jack lines | **fail**, 2.4 to 4.8 MHz |
| charger boost 1.5 MHz +/-10 % | 5.0 at 1.35, jack lines | **fail**, 1.35 to 7.5 MHz | 7.3 at 1.35, jack lines | **fail**, 1.35 to 4.5 MHz |
| R-1 core regulator 3 MHz | 9.4 at 2.4, wall | **fail**, 2.4 to 7.2 MHz | 12.4 at 2.4, jack lines | **fail**, 2.4 to 4.8 MHz |
| R-2 RT6150 about 2 MHz | 5.7 at 1.5, jack lines | **fail**, 1.5 to 7.5 MHz | 8.2 at 1.5, jack lines | **fail**, 1.5 to 4.5 MHz |
| R-3 charge pump 300 to 500 kHz | 0.0 at 0.3, jack lines | **fail**, 0.3 to 7.8 MHz | 0.0 at 0.3, jack lines | **fail**, 0.3 to 4.8 MHz |
| R-4 I2C SCL | 0.0 at 0.36, jack lines | **fail**, 0.36 to 7.85 MHz | 0.0 at 0.36, jack lines | **fail**, 0.36 to 4.76 MHz |
| audio PWM 150 kHz | 0.0 at 0.15, jack lines | **fail**, 0.15 to 7.8 MHz | 0.0 at 0.15, jack lines | **fail**, 0.15 to 4.8 MHz |
| RP2350 ROSC 4.6 to 24 MHz, boot only | 15.0 at 4.6, wall | **fail** at 4.6 MHz | 19.4 at 4.6, jack lines | **fail** at 4.6 MHz |
| R-5 LPOSC 32.768 kHz | 0.0 at 0.03, jack lines | **fail**, 0.03 to 7.86 MHz | 0.0 at 0.03, jack lines | **fail**, 0.03 to 4.84 MHz |

Checker (`EXPECTED_REV2`, `EXPECTED_SCOPE`): in every option the failing set is the same nine sources (the eight below 4 MHz and the boot-time ROSC), and the other ten are not shown. No harmonic fails at or above 10 MHz (the highest failing harmonic is 4.84 MHz for A and B and 7.86 MHz for C1 and D). In the `rev1_plug` state all 19 sources fail in every option.

## 5. Margins against the requirement (proposed value 20 dB)

Every case below carries the 6 dB uncertainty of section 3; a margin smaller than that is reported as not shown, never as a pass (analysis checklist E3).

| Case | Governing id and limit | Result | Margin | Status |
|---|---|---|---|---|
| C1 and D, 12.5 MHz up to 1.5 GHz, rules O1 to O3, ports empty (revision 1) | REQ-SYS-177: 20 dB (TBR); TC-SYS-107 to 1.5 GHz | 24.8 dB at 12.5 MHz rising to 36 dB near 80 MHz, then 26.2 dB at 1.5 GHz | +4.8 to +6.2 dB at the ends | superseded: the pass at 1.5 GHz does not hold with a plug inserted (next rows) |
| Every option, rules O1 to O3, ports plugged (revision 2 case) | REQ-SYS-177; TC-SYS-107 every aperture, worst case | 17.1 to 17.2 dB at 1.5 GHz (aperture only); the unfiltered jack lines are not bounded | down to -2.9 dB | fail, every source (19 of 19) |
| Every option, rules O1 to O4, worse of empty and plugged, 10 MHz to 1.5 GHz | REQ-SYS-177; TC-SYS-107 | A 22.0, B 22.1 dB at 1.5 GHz; C1 and D 22.3 dB at 10 MHz and 22.6 dB at 1.5 GHz | +2.0 to +2.6 dB | not shown (10 sources in every option) |
| Every option, rules O1 to O4, plugged, below about 5 MHz | REQ-SYS-177 | 0.0 to 19.9 dB (jack-line conducted bound, K = 1) | down to -20 dB | fail (nine sources in every option, A included) |
| C1 and D, 12 MHz (XOSC) and 9 to 10.7 MHz (BFO) | REQ-SYS-177 | 24.5 and 22.2 dB | +4.5 and +2.2 dB | not shown |
| C1 and D, sources below 4 MHz and their harmonics to about 7 MHz, and the ROSC at boot | REQ-SYS-177 | 0.3 to 19 dB (H field) | -19.7 to -1.0 dB | fail |
| C1, 144 to 150 MHz (the in-band birdie sources of CON-009) | REQ-SYS-177 | 34.6 dB | +14.6 dB | pass |
| A and B, every source (the 1.5 GHz case), ports empty | REQ-SYS-177; TC-SYS-107 | 25.4 and 25.6 dB (rules O1 to O3); 24.7 and 24.9 dB (rules O1 to O4) | +4.7 to +5.6 dB | not shown |
| A, sources below 4 MHz, ports empty | REQ-SYS-177 | 40 dB or more (40.1 dB at 33 kHz, 58 dB or more from 1.5 MHz) | +20 dB or more | pass empty; fail plugged (row above) |
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
   - **O2 Jack collars (revision 1; withdrawn as a shielding credit in revision 2).** Each 3.5 mm jack nose passes through a coated collar 6 mm deep behind the 2 mm wall (8 mm below-cutoff depth for the 9 mm opening), bonded to the coating. The 8 mm credit holds only for an empty jack: with a plug in, the plug sleeve and the collar form a coaxial line with no cutoff (INSP-083 finding-5, section 4.5).
   - **O2 Bonded metal-nose jacks (revision 2, replaces the collar credit).** Each 3.5 mm jack is a part whose metal nose is its sleeve contact (WP-PDR-38 selects it; planning 6.0 mm nose, 3.6 mm bore, 5 mm of metal, Low). The nose passes through the coated collar, which stays as the bonding land, and a conductive gasket ring (fabric-over-foam or spring-finger) bonds it to the collar bore all round. The ring must keep contact over the stack S2 radial gap of 0.85 to 2.15 mm and push the nose sideways by no more than 5 N, so it adds no constraint to stack S2 or to the jack's solder joints (planning values; WP-PDR-39 and WP-PDR-38). With a plug in, the plug sleeve is then bonded to the shield at the wall through the nose, and the coaxial line between the sleeve and the nose has no drive from inside. The leak is the gasket contact ring (8 slots of 3 mm at the 2 mm depth, the O3 model), plus the nose bore when the jack is empty. The jack's sleeve pin is board ground, so each jack also bonds board ground to the shield at the -X end, as the SMA port does at the +X end.
   - **O4 Filtered jack lines (revision 2, new).** Each tip and ring line of both jacks passes through a filter within 5 mm of its jack pin, returned to the jack's bonded sleeve pin: key lines 1 kohm series and 10 nF shunt; phones lines a 600 ohm at 100 MHz class ferrite bead in series and 10 nF shunt (planning values of section 2). These are the "filtered feedthroughs" the REQ-SYS-177 rationale names as a means. The key lines carry a switch closure against the RP2350 input pull-up, so 1 kohm in series is negligible. The phones shunt is 796 ohm at 20 kHz against a 32 ohm earphone; whether the headphone amplifier drives 10 nF stably is for WP-PDR-25 (amplifier datasheet not read, Low). The filters go to WP-PDR-37 (schematic and floorplan) and WP-PDR-36 (ICD-CTL-KEY and the phones interface).
   - **USB with a cable (revision 2, stated).** With a cable in, the plug shell fills the receptacle mouth and mates the receptacle shell that O1 bonds to the shroud. The leak is then the mated seam, and the USB conductors stay inside the cable shield, which the plug shell bonds at the wall. The seam gives about -32 dB at 1.5 GHz, 9 dB more leak than the empty mouth (section 2 row "USB with a cable").
   - **O3 Bonded encoder bushings.** Each encoder's metal bushing is bonded to the coated front wall by its panel nut and a toothed washer on a coated land, so metal closes the hole and only the contact ring leaks.

   Revision 1 concluded that with O1 to O3, C1 and D pass from 12.5 MHz to 1.5 GHz. That holds only with every port empty, and **it is withdrawn** (INSP-083 finding-5). With the plugs in and the revision 1 rules, every option falls to 17.1 to 17.2 dB at 1.5 GHz by the aperture alone, and the unfiltered jack lines are not bounded: every source fails. With O1 to O4, the worse of the empty and plugged states gives, **from 10 MHz to 1.5 GHz, no fail in any option but no pass either**: every source whose harmonics reach 1.5 GHz is **not shown** at 22.0 dB (A), 22.1 dB (B) and 22.6 dB (C1 and D), and the BFO at 21.3 dB at 9 MHz in C1 and D (section 4.6). **Below about 5 MHz the plugged state fails in every option**, A included, by the conducted bound of the jack lines (K = 1, section 4.5), and C1 and D fail there by the coating wall as well. No further opening rule is proposed at PDR, because the remaining leaks at 1.5 GHz (joints, contact rings, window, USB seam, the phones bead) are spread over many small terms; a better bead on the phones lines and the layout coupling are the CDR levers (item 4).
3. **Sources below 4 MHz (C1 and D).** No sprayed coating gives 20 dB in the magnetic near field below about 7 MHz. That range holds the fundamentals and low harmonics of eight sources and the boot-time ROSC: the synchronised 5 V buck, the charger boost, residual sources R-1 to R-5, the audio PWM and the ROSC. The CNC wall of A gives 40 dB or more there. Board shield cans (revision 0 item 2 (b)) can cover the buck and the charger, and R-1, R-2, R-5 and the ROSC only with a can over the whole Pico 2 module. They cannot cover the I2C lines (R-4) or the audio PWM traces, which run across the board. So option (b) alone no longer closes the item. **Question for the owner**, carried by TS-011 and plan PCR-9, now in this form:
   - (a) a CR scoping REQ-SYS-177 to 10 MHz and above, with the sources below it controlled by layout, filtering, the clock-plan rules and the REQ-SYS-034 receiver Test (the lead SE's recommendation for option C);
   - (b) (a) plus board-level shield cans over the 5 V buck and the charger, as good practice for the receiver, whatever the enclosure;
   - (c) keep REQ-SYS-177 over the whole range and order the CNC fallback (A). Revision 1 said A fails no source. With a plug inserted (revision 2) A fails the same nine sources below about 5 MHz by the jack-line conducted bound, and is not shown at 1.5 GHz (22.0 dB). So (c) removes those fails only if the CDR layout analysis shows the coupling onto every jack line 26 dB or more below the bound (section 4.5), and even then A is not shown at 1.5 GHz; otherwise the owner accepts those cases by name.

   The plug-inserted cases go into the same ruling by name (revision 2): (1) the ten sources not shown from 10 MHz up in every option (22.0 to 22.6 dB, plugged, at 1.5 GHz; the BFO at 21.3 dB in C1 and D); (2) the nine sources below about 5 MHz that fail plugged in every option through the jack lines; (3) under (a) and (b), the plugged state adds no fail at or above 10 MHz.
4. **Scope of the 1.5 GHz edge.** Whatever the owner rules in item 3, every option is within 6 dB of 20 dB at 1.5 GHz by this model (22.0 to 22.6 dB with the ports plugged and rules O1 to O4). REQ-SYS-177 is an Analysis requirement closed by TC-SYS-107 on the CDR design data (04 section 5.1 item 5), so a TRR measurement cannot close it. The CDR analysis (TC-SYS-107 with the STEP openings and the worst-case corners of its step 4, both port states, the chosen jack, gasket, bead and capacitor parts, and the layout coupling onto the jack lines in place of K = 1) must show the margin, or the owner accepts the not-shown cases by name in the same PCR-9 ruling. TC-SYS-107 names apertures and seams but not conductors that leave on a cable; the request to its writer (plan section 5.3 order) is to add the plugged state and the filtered jack lines to its step 2 list. The near-field probe measurement of the option C acceptance set (CR-003 section 5 item 3 (b)) is supporting data only.
5. **REQ-SYS-109:** propose to keep 0.1 ohm, with a coating design value of at most 0.03 ohm/sq (coupon, TS-011 Appendix B.4) and two bond points per coated part.
6. **REQ-SYS-177:** propose to keep 20 dB. The frequency scope (item 3), the not-shown cases (items 2 and 4) and the plug-inserted cases (item 3, revision 2) go to the owner with PCR-9.

## 8. Limitations

- The model is not a field solver. The slot formula is conservative for an open slot and uncertain for a gasketed joint, whose leakage depends on the gasket's transfer impedance (not modelled). The power sum assumes random phase. The aperture and joint terms together carry about +/-6 dB.
- The near-field (H) wave impedance assumes a small loop source at 10 mm. A closer source (a converter inductor near the back wall) lowers the H-field shielding further.
- Coating resistivities are recalled values (Low). The design value is a requirement on the coating, verified by the coupon, not a property of a chosen product.
- **Plugged state (revision 2).** The conducted term uses K = 1, a bound: it takes the board-level noise to appear in full on each jack line at the jack. The real coupling is set by the WP-PDR-37 layout and, for the phones lines, by the audio reconstruction filter (WP-PDR-25). The filter parts are planning values; the bead's parasitic capacitance and the capacitor's inductance set the 1.5 GHz term and are recalled class values (Low). The coaxial line between a plug sleeve and a bonded metal nose is taken as undriven. Its residual drive, the voltage across the sleeve contact, is not modelled and is checked on the chosen part at CDR. The USB cable shield's transfer impedance is a property of the owner's cable and is not modelled.
- Developer evidence only. The tools are not accredited, and no measurement exists yet: the near-field probe (owner-actions E-01) and its TV record come before the option C shielding measurement (CR-003 section 5 step 19).

## 9. Proposed values (for the PDR memo, on an APPROVED record)

- REQ-SYS-177: 20 dB (keep), with the owner's choice among section 7 item 3 (a), (b) and (c), the not-shown cases of section 7 items 2 and 4 and the plug-inserted cases of section 7 item 3 (revision 2) named in the same ruling (PCR-9), with rules O1, O2 (revision 2), O3 and O4 as the design basis.
- REQ-SYS-109: 0.1 ohm (keep), with coating Rs of at most 0.03 ohm/sq and two bond points per coated part.

## Change log

| Revision | Date | Change | Reason |
|---|---|---|---|
| 0 | 2026-09-27 | Initial draft, wave 1a | WP-PDR-27 |
| 2 | 2026-09-27 | Plug-inserted state: section 1 question 4; section 2 rows for the port states, the jack parts, the jack-line filters, the conducted-term model and the USB with a cable; section 3 port-state method and checker; new sections 4.5 (port states) and 4.6 (governing verdict per source); sections 4.2 and 4.3 marked as empty-port results; section 5 rows; section 7 item 2 (O2 collar credit withdrawn, O2 bonded metal-nose jacks, O4 filtered jack lines, the USB cable stated, the revision 1 conclusion withdrawn), item 3 option (c) and the plug-inserted cases for PCR-9, item 4 (CDR analysis inputs; TC-SYS-107 request), item 6; section 8 limitation; section 9. Script: `STATES`, `FILTERS`, `line_t`, the `rev1_plug`, `rev2`, `rev2_plug` and `rev2_worst` states, `EXPECTED_REV2`, `EXPECTED_SCOPE`, the limiting term "jack lines (conducted)", the middle and right plot panels. Minor findings 2 to 4 are not addressed | INSP-083 finding-5 (Major) |
| 1 | 2026-09-27 | Section 1 question 1, section 2 source row and openings row, section 3 (every source and harmonic, 6 dB uncertainty), section 4 (spot table to 1.5 GHz, per-source verdicts, checker verdicts), section 5 (status column; not shown cases), section 7 (opening rules O1 to O3; the sources below 4 MHz; the owner question restated; the 1.5 GHz edge), section 9 wording. Sources per clock plan revision 2 (19, with R-5 and the ROSC). Script: `CLOCK_SOURCES`, `OPENINGS`, `per_source`, `EXPECTED_REV1`, new output `out/shielding-sources.csv`, three-panel plot | INSP-083 finding-1 (Major) |
