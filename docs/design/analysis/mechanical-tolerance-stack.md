# Mechanical tolerance stack, load path, drop and drip analysis

| Field | Value |
|---|---|
| Product | Analysis note (08 section 3.4), WP-PDR-27, PDR draft revision 0, 2026-09-27 |
| Author | Claude, ME designer (WP-PDR-27 author invocation) |
| Status | Draft. **AT RISK (CR-003, CR-006):** written on the option C design of TS-011 (CR-003 revision 3, Submitted) and the one-unit build of CR-006 revision 2 (Submitted) |
| Serves | REQ-SYS-105, 107, 108, 110, 111, 116, 117, 168 (G11 TBR proposals for 105, 107, 116, 117, 168); TS-011 mandatory criteria M1 to M3 and M6 and enhancing criterion C5; TS-004 stiffness criterion K2; ICD-TX-ANT 3.2.2 "PCB connection" choice (TBR) and ICD-CTL-USB 3.2.2 wall opening; the board outline and envelope handed to WP-PDR-37 and WP-PDR-39 |
| Model, checker, plots | `hardware/sim/enclosure/tolerance_stack.py` (stacks S1 to S9 and loads L1 to L3, `--check`), `hardware/sim/enclosure/envelope_drawing.py` (geometric checks E1 to E6, `--check`), data `hardware/enclosure/board-outline.json`; outputs `hardware/sim/enclosure/out/tolerance-stack.csv`; plots `docs/reviews/PDR/figures/tolerance-stack.png` and `docs/reviews/PDR/figures/board-outline-envelope.png` (both rendered and inspected 2026-09-27) |
| Review record | `docs/reviews/PDR/checklists/analysis-mechanical-tolerance-stack.md` |
| Evidence status | Developer evidence (venv Python with numpy and matplotlib, class B, no TV record of their own). The printed-part (FDM) tolerances are the author's planning values for an H2C print, with Low confidence, until the fit-check coupon of WP-PDR-39 measures them |

## 1. Questions

1. Do the option C parts line up well enough that every plug seats, every shaft and bushing clears its hole, the display's active area shows through its window, the heat path clamps at the right pressure, and the antenna port needs no stressed joint?
2. Does the port retention carry the REQ-SYS-105 moment with margin?
3. Do the cells, the board, the heatsink and the display survive the REQ-SYS-116 drop by a stated load path?
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

Commands (both `CHECK PASS` on 2026-09-27):
- `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/hardware/sim/enclosure/tolerance_stack.py --check`
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

## 5. Port retention (REQ-SYS-105, HZ-009)

The SMA bulkhead jack passes through a D-hole in a 6061 port block, 12 x 20 x 12 mm, from PCBWay with the board order. The D-flat stops rotation under the 0.45 to 0.56 N m coupling torque (ICD-TX-ANT 3.2.2) and under the 0.90 N m stainless rating. The block is captured in a pocket between the two printed shells and screwed by two M3 screws into heat-set inserts.

| Check (L1) | Value | Capacity | Margin |
|---|---|---|---|
| Couple of 4.0 N m on the shortest block arm, 12 mm | 333 N | n/a | n/a |
| Bearing stress on the 12 x 12 mm pocket face | 2.31 MPa | 45 MPa (Low) | 19.4 |
| Load per M3 insert, if the screws alone react the couple | 167 N | 500 N (Low) | 3.0 |

The weakest element is the insert pull-out, margin 3.0 on a planning value. It passes the M2 margin rule of TS-011 (1.5) and scores C5 = 3. The return-loss part of REQ-SYS-105 (1 dB, TBR) is met by construction: the load path goes through metal only, from the jack to the block to the inserts, and never through the pigtail. The TC-SYS-072 proof load confirms it on the unit after the CR-006 spare-board dry run (CR-003 R3-F1).

## 6. Drop (REQ-SYS-116, 1.0 m TBR)

| Check (L2) | Stop 1.0 mm | Stop 0.5 mm | Design rule and capacity |
|---|---|---|---|
| Impact energy | 3.63 J | 3.63 J | n/a |
| Peak deceleration | 1000 g | 2000 g | first cut (Low) |
| Cell bearing on the back-shell ribs (two ribs 18 x 3 mm per cell) | 4.4 MPa | 8.7 MPa | the cells are braced by the ribs and the cell door, not by the holder springs; 45 MPa (Low) |
| Load per board boss (6 bosses, board and parts 35 g) | 57 N | 114 N | M3 insert shear and pull-out at least 500 N (Low) |
| Heatsink (50 g) | about 490 N | about 980 N | carried by the back-shell pocket ledges, 160 mm2 (3 to 6 MPa), not by the board or the gap pad |
| Display glass (3.6 g) | 35 N | 70 N | glass seated on the full pocket floor behind the lens (S4b) |

The antenna fitted in the drop is a flexible whip. Its bending into the port is bounded by the whip's own stiffness and is not computed here. REQ-SYS-116 stays an analysis target (OD-33) and closes on the delivered configuration after the enclosure choice (CR-003 section 5 item 3). Proposed value: keep 1.0 m.

## 7. Rain (REQ-SYS-117, IPX2 TBR) and pinch (REQ-SYS-168)

- **IPX2** (dripping water at up to 15 degrees tilt, upright with plugs inserted). Upright puts the antenna end (+X) up. That face carries only the SMA through the port block, sealed by the pocket fit and a gasket. The heatsink fins sit in channels outside the sealed volume: water entering the guard slots runs down the fins and out of the lower slots. The heatsink base gasket, which is also the bond gasket, seals the interior. The front face (display lens bonded, encoder bushings nut-sealed, buttons with printed skirts) is vertical when upright. The jack and USB openings are on the lower end face. Proposed value: keep IPX2, closed by Test on the delivered unit after the choice.
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
- **Proposed values:** REQ-SYS-105 keep 1 dB; REQ-SYS-107 keep 20 mm and 10 mohm; REQ-SYS-116 keep 1.0 m; REQ-SYS-117 keep IPX2; REQ-SYS-168 keep 4 mm and 25 mm.
- **Cross items:**
  - ICD-CTL-USB 3.2.2 opening to 12.6 x 10.6 mm (WP-PDR-36);
  - ICD-TX-ANT 3.2.2 "PCB connection" to the RG-316 pigtail (WP-PDR-36);
  - display glass pocket and flex routing (WP-PDR-25, 39);
  - support posts under the buttons (WP-PDR-37, 39).

## 11. Limitations

- The FDM tolerances are planning values; the fit-check coupon of WP-PDR-39 (a printed pocket, boss and hole set measured with calipers, OQ-VV-002) replaces them.
- The strength values are recalled typical data, not the chosen filament's datasheet (TS-011 Appendix B.3 item 3).
- The drop deceleration is a first cut. No dynamic analysis is made, and none is planned before CDR. The closing evidence is the drop test on the delivered unit.
- The whip's contribution to the drop is not computed.
- Developer evidence only (tools not accredited).
