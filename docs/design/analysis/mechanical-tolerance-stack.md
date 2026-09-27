# Mechanical tolerance stack, load path, drop and drip analysis

| Field | Value |
|---|---|
| Product | Analysis note (08 section 3.4), WP-PDR-27, PDR draft revision 1, 2026-09-27 (fixes INSP-084 finding-1; change log at the end) |
| Author | Claude, ME designer (WP-PDR-27 author invocation) |
| Status | Draft. **AT RISK (CR-003, CR-006):** written on the option C design of TS-011 (CR-003 revision 3, Submitted) and the one-unit build of CR-006 revision 2 (Submitted) |
| Serves | REQ-SYS-105, 107, 108, 110, 111, 116, 117, 168 (G11 TBR proposals for 105, 107, 116, 117, 168); TS-011 mandatory criteria M1 to M3 and M6 and enhancing criterion C5; TS-004 stiffness criterion K2; ICD-TX-ANT 3.2.2 "PCB connection" choice (TBR) and ICD-CTL-USB 3.2.2 wall opening; the board outline and envelope handed to WP-PDR-37 and WP-PDR-39 |
| Model, checker, plots | `hardware/sim/enclosure/tolerance_stack.py` (stacks S1 to S9 and loads L1 to L3, `--check`, unchanged in revision 1), `hardware/sim/enclosure/drop_and_axial.py` (revision 1: drop rows D1 to D20 per face and load path, axial rows A1 to A5, `--check`), `hardware/sim/enclosure/envelope_drawing.py` (geometric checks E1 to E6, `--check`), data `hardware/enclosure/board-outline.json`; outputs `hardware/sim/enclosure/out/tolerance-stack.csv` and `out/drop-and-axial.csv`; plots `docs/reviews/PDR/figures/tolerance-stack.png`, `docs/reviews/PDR/figures/drop-and-axial.png` and `docs/reviews/PDR/figures/board-outline-envelope.png` (all rendered and inspected 2026-09-27) |
| Review record | `docs/reviews/PDR/checklists/analysis-mechanical-tolerance-stack.md` |
| Evidence status | Developer evidence (venv Python with numpy and matplotlib, class B, no TV record of their own). The printed-part (FDM) tolerances are the author's planning values for an H2C print, with Low confidence, until the fit-check coupon of WP-PDR-39 measures them |

## 1. Questions

1. Do the option C parts line up well enough that every plug seats fully (radially and axially, REQ-SYS-108), every shaft and bushing clears its hole, the display's active area shows through its window, the heat path clamps at the right pressure, and the antenna port needs no stressed joint?
2. Does the port retention carry the REQ-SYS-105 moment with margin?
3. Do the cells, the board, the heatsink, the display and the antenna port survive the REQ-SYS-116 drop on each face, with the antenna fitted, by a stated load path?
4. Does the design meet REQ-SYS-117 IPX2 and REQ-SYS-168 by construction?
5. Which values are proposed for the TBRs these requirements carry?

## 2. Inputs

| Contributor | Value (+/-) | Source and confidence |
|---|---|---|
| Printed feature position from its part datum (H2C, PETG) | 0.20 mm | author's planning value (Low); measured on the WP-PDR-39 coupon |
| Heat-set insert position after installation | 0.20 mm | author's planning value (Low) |
| M3 screw (3.0 mm) float in a 3.2 mm board hole | 0.10 mm radial | geometry |
| Board feature from its holes | 0.10 mm | PCBWay drill position +/-0.075 mm (`pcbway-fabrication-and-assembly.md` F9, High) rounded up |
| Through-hole part position on the board | 0.15 mm | hole +/-0.08 mm (F9) plus body float (Low) |
| Machined feature with a drawing callout | 0.10 mm | research A5 (class f equivalent on a callout, Medium) |
| Machined block in a printed pocket | 0.10 mm per side | design clearance |
| Pico 2 module on its castellations, owner-soldered | 0.30 mm | author's planning value (Low; SI-031 hand assembly) |
| Board outline | 0.20 mm routed | F9 (High) |
| Display glass in its board adhesive | 0.30 mm | author's planning value (Low) |
| USB plug overmold | 10.6 x 8.5 mm | ICD-CTL-USB 3.2.2 (display F21) |
| Display | active 23.04 mm, glass 26.6 x 30.3 mm, window 24.0 mm, pocket 27.0 x 30.7 mm | `display-and-ui-parts.md` F2, UI-DSP-05 |
| Jack nose | 6.0 mm (planning; the part is chosen by WP-PDR-38) | author (Low) |
| Encoder bushing | 7.0 mm (planning; the part is chosen by WP-PDR-25 and 39) | author (Low) |
| Loads | REQ-SYS-105 moment 4.0 N m; unit mass 0.37 kg (TS-011 Appendix A.1); cell 48 g; board and parts 35 g; drop 1.0 m | requirements; ICD-PWR-CELL 3.2.1 |
| Strength values | PETG compressive strength 45 MPa (derated for 45 C); M3 heat-set insert pull-out in PETG 500 N; FR-4 flexural modulus 22 GPa | planning values recalled from typical data (Low) |

## 3. Method

Each stack is the list of independent contributors along one alignment. The worst case is their sum and the root-sum-square (RSS) is shown for information. The design passes when the worst case is at most the allowance the design gives. The load checks are closed-form: the couple of a moment on the port block, the drop deceleration from v^2 / (2 s) with a stopping distance s of 0.5 to 1.0 mm for a filleted PETG corner on a hard floor (Low), and the board deflection of a simply supported beam under a centre load. The envelope checks are geometric tests on `board-outline.json`.

Revision 1 adds, per face, the load of each internal mass at the same two decelerations on the element that carries it, and the margin (capacity over load). The pass rule is the TS-011 M2 rule, margin at least 1.5 at 2000 g. A row between 1.0 and 1.5 is reported as not shown and a row below 1.0 fails. The unit mass is 0.375 kg (TS-011 Appendix A.1). Axial stacks sum the X or Z contributors that set how deep a plug must enter or how much bushing thread remains.

Commands (all `CHECK PASS` on 2026-09-27):
- `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/hardware/sim/enclosure/tolerance_stack.py --check`
- `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/hardware/sim/enclosure/drop_and_axial.py --check`
- `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/hardware/sim/enclosure/envelope_drawing.py --check`

## 4. Tolerance stacks

| Stack | Alignment | Worst / RSS (mm) | Allowance (mm) | Verdict | Decision taken from it |
|---|---|---|---|---|---|
| S1 | SMA axis to the board, if the jack were board-mounted rigidly | 0.80 / 0.35 | 0.10 | fails | The SMA is a bulkhead jack in the port block, joined to the board by an RG-316 pigtail about 35 mm long, owner-soldered to board pads (compliant). This closes the ICD-TX-ANT 3.2.2 "PCB connection" choice (TBR) for the pigtail |
| S2 | Jack nose in a 9.0 mm opening | 0.65 / 0.34 | 1.50 | passes | Opening 9.0 mm; nose flush to 0.5 mm proud of the outer face |
| S3 | Encoder bushing in an 8.5 mm hole | 0.65 / 0.34 | 0.75 | passes | Hole 8.5 mm for a 7.0 mm bushing; the panel nut covers the gap |
| S4a | Display active area in the 24.0 mm window, glass on the board | 0.80 / 0.42 | 0.48 | fails | not used |
| S4b | Display active area in the 24.0 mm window, glass in a front-shell pocket | 0.30 / 0.22 | 0.48 | passes | The front shell locates the glass (UI-DSP-05 pocket); the flex takes the board offset |
| S5a | USB plug in the 12.0 x 10.0 mm opening of ICD-CTL-USB | 0.90 / 0.44 | 0.70 | fails | not used |
| S5b | USB plug in a 12.6 x 10.6 mm opening | 0.90 / 0.44 | 1.00 | passes | Proposed change to ICD-CTL-USB 3.2.2 (to WP-PDR-36) |
| S6a | Gap pad compression, heatsink fixed in a printed pocket | 0.50 / 0.26 | 0.10 | fails | not used |
| S6b | Gap pad compression, CNC pedestal on the same part as the bosses | 0.10 / 0.07 | 0.10 | passes | CNC fallback keeps the concept 7.8 pedestal |
| S6c | Gap pad compression, spring-loaded heatsink | 0.50 / 0.26 | 0.60 (spring travel) | passes | Option C heatsink spring-loaded against the 0.5 mm pad by two compression springs in the guard frame (TS-011 section 8 rule 3) |
| S7 | Board edge to the inner wall | 0.70 / 0.36 | 2.00 | passes | 2.0 mm design clearance kept |
| S8 | Knob skirt in a recess (REQ-SYS-111) | 0.75 / 0.35 | 1.00 | passes | If knobs sit in recesses, recess diameter = knob diameter + 4.0 mm |
| S9 | Counterpoise hole to the SMA axis (REQ-SYS-107) | 0.10 / 0.10 | 8.0 | passes | Tapped M3 in the port block 12 mm from the axis |

### 4.1 Axial stacks and thread engagement (revision 1, REQ-SYS-108 "fully seated")

From `out/drop-and-axial.csv`, rows A1 to A5. S2, S3 and S5 above are radial; these rows are along the plug axis (X) or the bushing axis (Z).

| Row | Item | Stack | Allowance | Verdict | Rule taken from it |
|---|---|---|---|---|---|
| A1, A2 | Key jack and headphone jack: plug fully seated through the -X wall | Nose face recess 1.0 mm nominal; X contributors THT part 0.15, insert 0.20, screw float 0.10, printed face 0.20 give 0.35 to 1.65 mm. A plug overmold of at most 7.0 mm diameter over its first 2 mm, centred on a nose that sits up to 0.65 mm off the opening centre (S2), keeps 0.35 mm of radial room in the 9.0 mm opening | recess above 0 (the end face lands in a drop, not the jack); recess at most 2.0 mm; radial room above 0 | pass | **Rule 21:** the jack nose face sits 1.0 mm behind the -X outer face (revision 0 had it flush to 0.5 mm proud, which puts a drop on the jack's solder joints). The admitted plug for REQ-SYS-108 is one whose overmold is at most 7.0 mm over its first 2 mm (definition carried to WP-PDR-36, ICD-CTL-KEY and the operations handbook) |
| A3 | Micro-USB: plug fully seated through the shroud of shielding rule O1 | Receptacle face 3.7 mm behind the outer face (3.0 mm board-edge gap plus 2.0 mm wall less a 1.3 mm receptacle overhang, Low), with module solder 0.30, module 0.10, insert 0.20, float 0.10 and printed face 0.20: 2.8 to 4.6 mm | the 10.6 x 8.5 mm overmold enters up to 8.0 mm (Low) and keeps the S5b clearance over the whole depth | pass | **Rule O1 geometry:** the shroud keeps the 12.6 x 10.6 mm section from the wall to the receptacle face plane and closes there with an end flange cut to the receptacle shell, bonded by a conductive gasket (`shielding-estimate.md` section 7 item 2). The overmold face seats on the flange |
| A4 | Encoder bushing thread through the front wall, 7 mm bushing | Body top (6.5 mm body, Low) 2.6 mm below the wall inner face, wall 2.0, toothed washer 0.5 (rule O3), nut 2.0: 7.1 mm needed; Z contributors insert 0.20, boss height 0.20, body height 0.30, wall 0.20: 0.9 mm | full nut engagement at the worst case | **fail** (-1.0 mm) | |
| A5 | The same with a 9 mm bushing | as A4 | as A4 | pass (+1.0 mm) | **Rule 22:** encoder bushing thread at least 9 mm from the body (WP-PDR-25 and WP-PDR-38 part choice). An inner jam nut is run down against the wall inner face at assembly, so tightening the panel nut clamps the wall between the two nuts and does not pull the board |

## 5. Port retention (REQ-SYS-105, HZ-009)

The SMA bulkhead jack passes through a D-hole in a 6061 port block, 12 x 20 x 12 mm, from PCBWay with the board order. The D-flat stops rotation under the 0.45 to 0.56 N m coupling torque (ICD-TX-ANT 3.2.2) and under the 0.90 N m stainless rating. The block is captured in a pocket between the two printed shells and screwed by two M3 screws into heat-set inserts.

| Check (L1) | Value | Capacity | Margin |
|---|---|---|---|
| Couple of 4.0 N m on the shortest block arm, 12 mm | 333 N | n/a | n/a |
| Bearing stress on the 12 x 12 mm pocket face | 2.31 MPa | 45 MPa (Low) | 19.4 |
| Load per M3 insert, if the screws alone react the couple | 167 N | 500 N (Low) | 3.0 |

The weakest element is the insert pull-out, margin 3.0 on a planning value. It passes the M2 margin rule of TS-011 (1.5) and scores C5 = 3. The return-loss part of REQ-SYS-105 (1 dB, TBR) is met by construction: the load path goes through metal only, from the jack to the block to the inserts, and never through the pigtail. The TC-SYS-072 proof load confirms it on the unit after the CR-006 spare-board dry run (CR-003 R3-F1).

## 6. Drop (REQ-SYS-116, 1.0 m TBR), per face with the antenna fitted

REQ-SYS-116 names "each face" and "with the antenna fitted". Revision 0 gave one generic column pair. Revision 1 gives one row per face and per internal load path (`drop_and_axial.py`, `out/drop-and-axial.csv`, `docs/reviews/PDR/figures/drop-and-axial.png`, rendered and inspected). Impact energy 0.375 kg x 9.81 x 1.0 m = 3.68 J; peak deceleration 1000 g at a 1.0 mm stop and 2000 g at 0.5 mm (Low). Loads and margins at 1000 g / 2000 g. Capacities are planning values (Low): PETG compressive 45 MPa and flexural 60 MPa (derated for 45 C), FR-4 through-thickness compressive 250 MPa and flexural 400 MPa, M3 heat-set insert pull-out 500 N, cell-holder body bearing 40 MPa.

| Row | Face | Case | Carrier | Load | Margin | Verdict | Rule |
|---|---|---|---|---|---|---|---|
| D1 | -Z back | the unit lands on the guard frame (it protrudes 10 mm) | guard frame and ribs, 33 % solid over 48 x 66 mm | 3.5 / 7.0 MPa | 12.8 / 6.4 | pass | rule 4: 3 mm guard ribs |
| D2 | -Z back | heat sink on its pocket ledges | back-shell ledges, 160 mm2 | 3.1 / 6.1 MPa | 14.7 / 7.3 | pass | |
| D3 | -Z back | cells on the back-shell ribs | two rib pairs, 216 mm2 | 4.4 / 8.7 MPa | 10.3 / 5.2 | pass | |
| D4 | -Z back | board and holders on the boss tops | six boss annuli | 3.4 / 6.8 MPa | 13.3 / 6.7 | pass | |
| D5 | +Z front | the unit lands on the flat front face | front shell, about 8000 mm2 | 0.5 / 0.9 MPa | 98 / 49 | pass | rule 17: knob tops at least 0.5 mm below the front face in their recesses, so the face lands and not a knob |
| D6 | +Z front | heat sink driven toward the board, revision 0 (no post) | board in bending over the 48 mm span between the bosses at x 78.5 and 126.5 | 570 / 1140 MPa | 0.70 / 0.35 | **fail** | |
| D7 | +Z front | the same with two front-shell posts | board in compression under two 6 mm posts | 8.7 / 17.3 MPa | 28.8 / 14.4 | pass | **rule 18** |
| D8 | +Z front | the two posts themselves | printed posts | 8.7 / 17.3 MPa | 5.2 / 2.6 | pass | rule 18 |
| D9 | +Z front | cells and holders driven toward the board, revision 0 (no post) | board in bending over the 74.5 mm span between the bosses at x 4 and 78.5 | 2090 / 4170 MPa | 0.19 / 0.10 | **fail** | |
| D10 | +Z front | the same with four front-shell posts over the holder bodies | printed posts on the board over the holders | 10.2 / 20.5 MPa | 4.4 / 2.2 | pass | **rule 18** |
| D11 | +Z front | the board pulls on its six inserts | insert pull-out | 57 / 114 N | 8.7 / 4.4 | pass | |
| D12 | +Z front | display glass on its pocket floor | front-shell pocket | 0.04 / 0.09 MPa | over 500 | pass | |
| D13 | +Y, -Y sides | cells sideways on the rib pairs | two rib pairs | 4.4 / 8.7 MPa | 10.3 / 5.2 | pass | |
| D14 | X and Y in plane | board and holders in plane on plain bosses, revision 0 | boss root in bending, 15.9 mm tall, 7.5 mm diameter | 35.8 / 71.6 MPa | 1.68 / 0.84 | **fail** | |
| D15 | X and Y in plane | the same with four gussets per boss | gusseted boss root | 8.9 / 17.9 MPa | 6.7 / 3.4 | pass | **rule 20** |
| D16 | +X end | whip fitted, corner impact: the whip bends the port. The moment is bounded by twice the 4.0 N m of REQ-SYS-105 (a 10 N push on a 40 cm whip, `antenna-and-erp.md` F8), with a factor 2 for a suddenly applied load (Low) | port block bearing on its printed pocket, 12 mm arm, 144 mm2 | 4.6 MPa | 9.7 | pass | rule 6: the block is captured between the shells |
| D17 | +X end | the same moment if the two screws alone carried it | two inserts in pull-out | 333 N | 1.50 | pass, at the rule | the captured pocket (D16) is the design path; D17 is the bound |
| D18 | +X end | end-on, the connector strikes first, revision 0 | port block's 20 x 12 mm inner face on its pocket | 15.3 / 30.7 MPa | 2.9 / 1.47 | not shown | |
| D19 | +X end | the same with a 20 x 20 x 2 mm inner flange on the block | pocket face 20 x 20 mm | 9.2 / 18.4 MPa | 4.9 / 2.5 | pass | **rule 6 (revision 1)** |
| D20 | +X, -X ends | cells along X on the holder end walls, which bear on back-shell end ribs | holder end walls, 2 x 20 x 14 mm | 1.7 / 3.4 MPa | 24 / 12 | pass | **rule 19** |

Face by face: the back face lands on the guard frame (D1 to D4); the front face lands on its flat face (D5, rule 17) and drives the heat sink, the cells and the holders toward the board, which revision 0 would crack (D6, D9) and rule 18 carries through the board in compression into the front shell (D7, D8, D10); the side faces load the cell ribs and the bosses in plane (D13 to D15); the +X face, with the whip fitted, loads the port block by a moment (D16, D17) or end-on (D18, D19); the -X face lands on its end face, the jacks being recessed (rule 21, section 4.1), and the cells bear on the end ribs (D20). The heat sink in plane is carried by the pocket side walls (bearing about 1.6 MPa at 2000 g on 600 mm2, not tabulated).

**Rules taken from this section** (TS-011 revision 1 section 8):
- **Rule 17.** Knob tops at least 0.5 mm below the front face in their REQ-SYS-111 recesses.
- **Rule 18.** Printed posts from the front shell bear on 6 mm copper-free pads on the board top: two within 10 mm of the PA pad edge, and four over the holder bodies (the two button posts of `board-outline.json` count if they sit over the holders). They carry a front-face drop through the board in compression. These posts touch the board where it runs hot at the REQ-SYS-112 condition, so they are part of the TS-011 M8 set: they pass M8 only with the filament route of TS-011 revision 1 (M8 row).
- **Rule 19.** The holder end walls bear on back-shell end ribs with at most 0.2 mm clearance, so cells in an X impact load the back shell, not the board.
- **Rule 20.** Every board boss carries four 1.5 mm gussets to the back wall.
- **Rule 6 (revision 1).** The port block carries a 20 x 20 x 2 mm inner flange bearing on its pocket.

REQ-SYS-116 stays an analysis target (OD-33) and closes on the delivered configuration after the enclosure choice (CR-003 section 5 item 3). Proposed value: keep 1.0 m.

## 7. Rain (REQ-SYS-117, IPX2 TBR) and pinch (REQ-SYS-168)

- **IPX2** (dripping water at up to 15 degrees tilt, upright with plugs inserted; revision 0 text, INSP-084 finding-4 open). Upright puts the antenna end (+X) up. That face carries only the SMA through the port block, sealed by the pocket fit and a gasket. The heatsink fins sit in channels outside the sealed volume: water entering the guard slots runs down the fins and out of the lower slots. The heatsink base gasket, which is also the bond gasket, seals the interior. The front face (display lens bonded, encoder bushings nut-sealed, buttons with printed skirts) is vertical when upright. The jack and USB openings are on the lower end face. Proposed value: keep IPX2, closed by Test on the delivered unit after the choice.
- **Pinch.** The cell door slides in grooves. The frame overlaps its leading edge by 3 mm, so no closing gap a 12 mm finger can enter opens between 4 and 25 mm during travel; the gap stays below 4 mm. Proposed value: keep 4 mm and 25 mm (values recalled from ISO 13857 and ISO 13854 practice, not in the corpus, Low).
- **Edge break (REQ-SYS-110).** Every printed outer edge carries a 1.0 mm fillet in the model (`board-outline.json` envelope). The CNC fallback carries a 0.5 mm minimum chamfer on the drawing. Checked by the TC-SYS-076 scripts on the models.

## 8. Board stiffness (TS-004 criterion K2)

| Check (L3) | 1.0 mm board | 1.2 mm | 1.6 mm |
|---|---|---|---|
| Deflection under 10 N at the middle of a 120 mm span (four corner bosses only) | 3.17 mm | 1.83 mm | 0.77 mm |
| Deflection across the 74.5 mm span of the six-boss layout | 0.76 mm | 0.44 mm | 0.19 mm |

A button that moves the board 0.76 mm feels soft and flexes the solder joints of nearby parts. With the 1.0 mm board of TS-004, a printed support post under each board-mounted button brings the button deflection close to zero. The encoders are panel-nut mounted, so their push loads go into the front shell, not the board. This rule is in `board-outline.json` (support posts).

## 9. Envelope checks (`envelope_drawing.py`)

| Check | Result |
|---|---|
| E1 board 130 x 62 mm inside the 136 x 66 mm inner outline with at least 1.5 mm | 2.00 mm, passes |
| E2 Z stack contiguous 0 to 30 mm; case plus heatsink and guard at most 40 mm (REQ-SYS-103) | 30 + 10 = 40 mm, passes |
| E3 heatsink footprint clear of the six boss keep-outs and the holder keep-out | passes |
| E4 PA thermal pad inside the heatsink footprint | passes |
| E5 12 mm finger through a 6.0 mm guard slot does not reach the fin tips | 0.80 mm penetration against 2.5 mm recess, passes |
| E6 heatsink overall height fits between the gap pad and the envelope, guard included | 23.0 mm against 23.02 mm available, passes (no margin: the heatsink rule of TS-011 caps it at 23 mm) |

## 10. Conclusions and proposed values

- Every alignment of the option C design passes worst-case with four decisions this analysis makes:
  - the RG-316 pigtail to the SMA;
  - the display glass located in the front shell;
  - the 12.6 x 10.6 mm USB opening;
  - the spring-loaded heatsink.

  The rejected variants (S1, S4a, S5a, S6a) fail and are recorded so that WP-PDR-39 does not reintroduce them.
- **Revision 1 decisions** (sections 4.1 and 6): rules 17 to 22, the rule 6 flange and the rule O1 shroud geometry. The revision 0 designs they replace fail or are not shown (D6, D9, D14, D18, A4) and are recorded so that WP-PDR-39 does not reintroduce them.
- **Proposed values:** REQ-SYS-105 keep 1 dB; REQ-SYS-107 keep 20 mm and 10 mohm; REQ-SYS-116 keep 1.0 m; REQ-SYS-117 keep IPX2; REQ-SYS-168 keep 4 mm and 25 mm.
- **Cross items:**
  - ICD-CTL-USB 3.2.2 opening to 12.6 x 10.6 mm (WP-PDR-36);
  - ICD-TX-ANT 3.2.2 "PCB connection" to the RG-316 pigtail (WP-PDR-36);
  - display glass pocket and flex routing (WP-PDR-25, 39);
  - support posts under the buttons (WP-PDR-37, 39);
  - rule 18 post pads (6 mm, copper-free) near the PA pad and over the holders, and rule 21 jack set-back (WP-PDR-37);
  - the admitted-plug definition of rule 21 (WP-PDR-36, ICD-CTL-KEY; operations handbook);
  - rule 22 bushing length (WP-PDR-25, WP-PDR-38).

## 11. Limitations

- The FDM tolerances are planning values; the fit-check coupon of WP-PDR-39 (a printed pocket, boss and hole set measured with calipers, OQ-VV-002) replaces them.
- The strength values are recalled typical data, not the chosen filament's datasheet (TS-011 Appendix B.3 item 3).
- The drop deceleration is a first cut. No dynamic analysis is made, and none is planned before CDR. The closing evidence is the drop test on the delivered unit.
- The whip's contribution to the drop is bounded, not computed: D16 takes twice the REQ-SYS-105 moment, which assumes that a whip whose base yields or flexes near 4.0 N m (the class of `antenna-and-erp.md` F8) is fitted. A stiffer antenna needs its own check (WP-PDR-38 antenna choice).
- The drop capacities are planning values and the stop distance is a first cut (Low); the gusset gain of rule 20 (factor 4 on the section modulus) is an estimate.
- Developer evidence only (tools not accredited).

## Change log

| Revision | Date | Change | Reason |
|---|---|---|---|
| 0 | 2026-09-27 | Initial draft, wave 1a | WP-PDR-27 |
| 1 | 2026-09-27 | Questions 1 and 3 widened; section 3 method for the per-face rows; new section 4.1 (axial stacks A1 to A5, rules 21 and 22, rule O1 geometry); section 6 rewritten per face and load path with the antenna fitted (rows D1 to D20, rules 17 to 20 and the rule 6 flange); section 10 decisions and cross items; section 11 limitations. New script `hardware/sim/enclosure/drop_and_axial.py` with `out/drop-and-axial.csv` and `docs/reviews/PDR/figures/drop-and-axial.png`; `tolerance_stack.py` unchanged | INSP-084 finding-1 (Major) |
