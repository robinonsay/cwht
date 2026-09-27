# TS-011: Enclosure concept, option C build candidate with the CNC fallback

| Field | Value |
|---|---|
| ID | TS-011 |
| Status | Draft, revision 0 (2026-09-27, wave 1a draft of WP-PDR-27). **AT RISK (CR-003, CR-006):** drafted on CR-003 revision 3 (`d9a215a`, reviewer re-check of revision 3 recorded in its section 6.4, 0 Major) and CR-006 revision 2 (`39a6b13`), both Submitted and not dispositioned (plan rule C8). Scores that depend on WP-PDR-28a (first-cut thermal per option) and WP-PDR-04 (PCBWay quotes) are the author's screen and are marked Low confidence; they are re-checked in the 1b final before the F0 freeze |
| Decision class trigger | 06 section 14.1 class 1 items (a) architecture choice (enclosure concept), (c) a choice touching hazards HZ-001, HZ-002, HZ-003, HZ-006, HZ-007, HZ-009 and HZ-013 in `docs/safety/hazards.json`, and (d) the owner asked for the study (SRR minutes, "Schedule and enclosure inputs"; SI-037). SEMP customization 11 (i) no longer applies because more than one viable alternative exists (CR-003 section 2) |
| Decision maker | Robin (owner, Decision Authority) |
| Recommender | Claude (ME designer, WP-PDR-27 author invocation, 2026-09-27) |
| Independent reviewer | INSP-NNN in `docs/reviews/PDR/checklists/ts-011-enclosure.md`, filled from `docs/templates/peer-review-checklist-risk.md` section B (06 section 14.2); the analyses it cites have their own records (`analysis-shielding-estimate.md`, `analysis-mechanical-tolerance-stack.md`); the thermal numbers are reviewed with `analysis-thermal-budget.md` (WP-PDR-28) |
| Decide by | PDR (B1b owner session, Thu 2026-10-01, OD-10 and OD-38 final), because the allocated baseline fixes the enclosure concept, the board outline and envelope (REQ-SYS-103, TPM-016), `ICD-TX-ME` and `ICD-CTL-ME`, and the TBR values of G11 |
| Related risks | RSK-006, RSK-007, RSK-018, RSK-025, RSK-026, RSK-030, RSK-039, RSK-043, RSK-044, RSK-052, RSK-053 (CR-003 section 4 Risk row), and the five CR-003 candidates (a) to (e) |
| Related requirements and hazards | Mandatory set of CR-003 section 5 step 10: REQ-SYS-102, 103, 105, 107, 108, 109, 110, 111, 112, 113, 116, 117, 124, 168, 175, 177, 191; also REQ-SYS-104, 106, 114, 115, 139, 146, 181; CON-015, CON-026 (as CR-003 amends them); HZ-001, HZ-002, HZ-003, HZ-006, HZ-007, HZ-009, HZ-013; SI-008, SI-012, SI-032, SI-037, SI-039 (the id CR-003 proposes for the owner inputs of 2026-09-27, appended by CR-003 step 0) |
| Resulting ADR | ADR-038 (provisional, plan section 3.1), superseding ADR-008; written the day the owner decides |
| Dates | opened 2026-09-27; recommended: after the INSP record is APPROVED (plan rule C9); decided: B1b |

## 1. Executive summary

- **Recommendation (one sentence):** build option C as **C1**, an owner-printed PETG two-shell case (H2C, route Ra: legend and jack markings debossed 0.6 mm with a flush contrasting PETG inlay), a sprayed silver-coated-copper coating inside only, a purchased black-anodized extruded heatsink of at most 40 x 58 x 23 mm under the PA pad, spring-loaded against a 0.5 mm gap pad, its fins behind a printed guard with 6 mm slots, a 6061 port block for the SMA jack ordered from PCBWay with the board, and a transparent conductive film in the display window. Hold the PCBWay CNC 6061 enclosure (A) on the same board outline and envelope as the fallback.
- **Closely ranked alternative presented with it:** D, a catalog extruded aluminum body with printed face and end parts (295 of 500 each, a tie; section 5). D is paper only under CR-003 section 5 step 10, and choosing it would need a CON-015 wording change (section 8).
- **Problem requiring a decision (one sentence):** which enclosure concept and which fabrication and marking route go into preliminary design, given the owner's sequence (printed case first, CNC only if it fails), the 48 C bound on every accessible surface and the PA heat path through a poorly conducting PETG wall.
- **Two findings for the owner before the decision:**
  1. **Thermal (REQ-SYS-112).** C1 passes the continuous key-down case at 45 C only if the heatsink's in-situ resistance is at most 5.5 K/W: at 4.1 W the junction is 107.5 C against 110 C (TBR). The author's own physics estimate for a heatsink of that size spans 5.5 to 9 K/W (Low). At 7.5 K/W the junction is 115.7 C continuous, but 101.5 C at the 80 % duty that the hardware key-down limit of REQ-SYS-055 (7.5 to 13 s) allows (section 4, M4). WP-PDR-28 must state which case closes REQ-SYS-112.
  2. **Shielding (REQ-SYS-177).** Any sprayed coating gives less than 20 dB against the magnetic near field of the 1.5 MHz charger and 2.2 MHz buck: 9.5 and 11.8 dB at 0.03 ohm/sq. The CNC wall gives more than 60 dB there. From 12 to 600 MHz every option meets 20 dB once the design rules of section 8 are applied. At 1 GHz every option is marginal, within 3 dB of 20 dB, limited by openings common to all (`docs/design/analysis/shielding-estimate.md`). This goes to the owner as a PCR-9 question: the frequency scope of REQ-SYS-177, or board-level shield cans over the converters.
- **Fabrication and marking route (OD-38):** route Ra, the owner prints on the H2C, 475 of 500 (Robust), against a PCBWay print (220) and a print plus PCBWay laser engraving (190). PCBWay engraving applies to the CNC fallback only.
- **Coating (owner input 7):** MG Chemicals 843AR silver-coated copper aerosol recommended, design value 0.03 ohm/sq or less measured on a coupon; 842AR (silver) if the coupon misses it, 843WB (water-based) if the solvent crazes PETG. Every product value below is **recalled, not read from a datasheet** (no downloads permitted, OD-18, OD-21, OD-25, OD-39); the owner fetches the datasheets of Appendix B before the value is ruled.
- **Robustness verdict (section 6):** Not robust for the main matrix (C1 and D tie; 22 single perturbations, 5 of weight and 17 of score, change the top rank). Robust for the route sub-matrix.
- **Owner's decision (section 10):** pending.

## 2. Problem and decision context

- **Mission and system context:** the enclosure (block B21, `docs/design/concept.md` section 7.8; allocation to ME) holds the board, cells, controls and antenna port in a pocket-sized shell. It carries the antenna load and conducts the PA heat to ambient with every accessible surface at or below 48 C. It is the RF ground and counterpoise return, and it carries the RF exposure legend and the jack markings. ConOps OPS-010 (storage, pocket carry), OPS-012 (build and assembly, as CR-003 amends it), OPS-014 (sustained keying), OPS-017 (bond), OPS-019 (legend). MOE-013 (pocket carry).
- **Decision needed and intended outcome:** one option C design is chosen as the build candidate, with its route, coating product, heatsink rule, SMA retention and marking process. The CNC fallback is designed to the same board outline and envelope, so a fallback needs no new board (CR-003 section 4 Performance margins row). The board outline, Z stack, keep-outs and connector faces are fixed for WP-PDR-37 and WP-PDR-39 (`hardware/enclosure/board-outline.json`). Every G11 TBR, the CR-003 TBRs (REQ-SYS-109, 191, the test finger) and the accessible-surface set for WP-PDR-28 get a proposed value.
- **Constraints:**
  - CON-015 as CR-003 amends it: no owner machining; the printed PETG case is built and evaluated first, the PCBWay CNC enclosure is ordered only if it fails, and a catalog extruded box is an alternative metal fallback. Every custom part has its source in the repository.
  - CON-026 as CR-003 amends it: the owner's H2C prints the case.
  - Owner inputs of 2026-09-27 (status note sections 2 and 3, SI-039 proposed): 48 C on every surface a hand can reach, no flame-rated filament, PETG, one item at a time with the cheapest first, and the legend and jack markings part of the surface.
  - SI-031: the owner solders through-hole parts and exposed pads only.
  - CR-006 revision 2: 5 bare boards fabricated and 1 assembled (`CWHT-A-001`). The 4 bare boards serve as fit-check blanks.
  - PCBWay closure 10-01 to 10-04 (`docs/plan/schedule.md`); CDR procurement release after PDR.
- **Prior related decisions:** ADR-008 (OpenSCAD, FreeCAD STEP, PCBWay CNC; this study's ADR supersedes it). SRR decisions 34 (legend engraved), 51 (jack markings), 83 (6061, bead blast, Type II anodize), 87 (1.0 mm board if four bosses). The concept section 12 descope row "printed enclosure ... needs a metal insert". CR-003 revision 3 and its reviews. TS-001 (PA device PD54008L-E, RthJC 3 C/W, 3.1 to 4.1 W dissipated at 5 W).
- **Research consulted:** `docs/research/enclosure-cnc-and-openscad-pipeline.md` A1 to A11 and B1 to B7; `docs/research/pcbway-export-and-vendor-questions.md` F14 to F18 (thermal DFM); `docs/research/pcbway-fabrication-and-assembly.md` F5, F9, F19 to F22; `docs/research/display-and-ui-parts.md` F2, F10, UI-DSP-05; `docs/research/power-tree-and-charging.md` F19 and R-PWR-03 (switcher frequencies); `docs/icd/ICD-PWR-CELL.md`, `ICD-CTL-USB.md`, `ICD-TX-ANT.md` section 3.2.2. The coating products of Appendix B come from the author's knowledge, not from a fetched source.

## 3. Decision matrix setup and rationale

### 3.1 Criteria and operational definitions

Mandatory criteria are pass or fail; an alternative that fails any is dropped before scoring (SE HB section 6.8.1.2.1). Each is assessed on the design of the option at concept level (design-analysis criteria, CR-003 R2-F3). The option C acceptance set measured on the unit is CR-003 section 5 Effectivity item 3 and is not a criterion here.

| ID | Criterion | Type | Operational definition | Scale | Weight |
|---|---|---|---|---|---|
| M1 | Envelope and mass | Mandatory | REQ-SYS-103: the design fits 140 x 70 x 40 mm (TBR). REQ-SYS-102: the mass estimate is at most 385 g, which is 350 g (TBR) plus 10 % concept-stage estimating uncertainty. The value closes by the WP-PDR-29 bottom-up | pass / fail | n/a |
| M2 | Antenna port | Mandatory | REQ-SYS-105: 4.0 N m reacted without jack rotation, margin at least 1.5 on the weakest element. REQ-SYS-107: counterpoise point within 20 mm (TBR) of the port. REQ-SYS-175: port on one end face | pass / fail | n/a |
| M3 | Access, edges and pinch | Mandatory | REQ-SYS-108: every plug seats; REQ-SYS-110: 0.5 mm edge break is producible by the process; REQ-SYS-111: 1.0 mm knob clearance; REQ-SYS-168: cell-cover closing gap outside 4 to 25 mm (TBR) | pass / fail | n/a |
| M4 | Thermal | Mandatory | Screen of `hardware/sim/enclosure/thermal_screen.py`, 4.1 W (PD54008L-E at 55 % efficiency, TS-001 M5 row). REQ-SYS-113: hottest accessible face at most 48 C after 5 min at 25 C. REQ-SYS-112: junction at most 110 C (TBR) steady at 45 C, continuous key-down | pass / fail | n/a |
| M5 | Shield and bond | Mandatory | REQ-SYS-177 in the radiated reading ("radiated from its enclosure"): total shielding at least 20 dB (TBR) from 12 to 600 MHz. REQ-SYS-109: the farthest point of every conductive part at most 0.1 ohm (TBR) from the jack shell. Source: `docs/design/analysis/shielding-estimate.md` | pass / fail | n/a |
| M6 | Environment | Mandatory | REQ-SYS-116: 1.0 m drop (TBR) survivable by a design load path (cells braced by the case, not the holder springs). REQ-SYS-117: IPX2 (TBR) with no opening on the upper end face except a sealed port | pass / fail | n/a |
| M7 | Markings | Mandatory | REQ-SYS-124: the legend is part of the enclosure surface by its own process (CR-003 revision 3). REQ-SYS-191: the process survives the rub by construction (depth or engraving), to be confirmed on a coupon | pass / fail | n/a |
| M8 | Printed-part heat margin | Mandatory | Filament heat-deflection temperature (PETG 69 C at 0.45 MPa, typical datasheet value, Low) exceeds the peak printed-part temperature at the REQ-SYS-112 condition and +60 C storage (REQ-SYS-115) by at least 5 K (CR-003 F9). For option B, the PCB-plate edge rule (owner input 6) | pass / fail | n/a |
| M9 | No unreducible Red safety risk | Mandatory | 06 section 13 item 2 | pass / fail | n/a |
| C1 | Cost | Enhancing | First-unit enclosure cash outlay in USD, consumables bought for it included (a whole coating can), author estimate until the WP-PDR-04 quotes | 1: > 187.5 / 2: <= 187.5 / 3: <= 125 / 4: <= 87.5 / 5: <= 50 | 25 |
| C2 | Schedule | Enhancing | Days from CDR release to the enclosure in hand on its own critical path | 1: > 13 / 2: <= 13 / 3: <= 8 / 4: <= 5.5 / 5: <= 3 | 15 |
| C3 | Thermal margin | Enhancing | 110 C minus the M4 junction temperature, K | 1: < 5 / 2: >= 5 / 3: >= 8 / 4: >= 11.5 / 5: >= 15 | 15 |
| C4 | Low-frequency shielding | Enhancing | Lowest total H-field shielding at 1.5 and 2.2 MHz, source 10 mm from the wall, dB | 1: < 15 / 2: >= 15 / 3: >= 20 / 4: >= 30 / 5: >= 40 | 10 |
| C5 | Port retention | Enhancing | Ratio of the weakest retention element's capacity to its REQ-SYS-105 load | 1: < 2.25 / 2: >= 2.25 / 3: >= 3 / 4: >= 4 / 5: >= 5 | 10 |
| C6 | Marking route | Enhancing | How early the REQ-SYS-191 marking can be proven | 1: vendor process, no coupon before the order / 3: coupon from a vendor sample before the order / 5: coupon made at home by the same process before the build | 10 |
| C7 | Iteration cost | Enhancing | Cost and days of one correction (reprint or recoat, or re-order) | 1: > USD 100 or > 9.5 d / 2: <= USD 100 and <= 9.5 d / 3: <= USD 50 and <= 5 d / 4: <= USD 32.5 and <= 3.5 d / 5: <= USD 15 and <= 2 d | 10 |
| C8 | Pre-build evidence | Enhancing | Evidence available before board arrival | 1: analysis only / 3: fit-check print or coupon / 5: the delivered enclosure itself measured (coating resistance, fit with a bare board) | 5 |
| | | | | **Sum of weights** | **100** |

Scores 2 and 4 of C6 and C8 sit halfway between the anchors.

Criteria considered (06 section 13 item 1): safety is covered by mandatory M3, M4 (48 C), M8 and M9, and by the hazard rows of section 7. First power-on is C8 (the enclosure does not gate first power-on: the board is powered first on the bench; C8 measures how much of the enclosure is proven before the unit exists). Cost is C1 and C7, schedule is C2, and performance margin is C3, C4 and C5. System security (07 section 16.2) is omitted: the enclosure adds no attack surface. The USB opening exists in every option and the key input is unchanged.

Other criteria considered and not used: mass (it is mandatory M1; as an enhancing criterion it would double-count the case material, which C1 and C3 already reflect); appearance (no requirement; owner input asks for cheapest first).

### 3.2 Alternatives

| ID | Alternative | Description | Source |
|---|---|---|---|
| A | CNC fallback (current baseline, ADR-008) | PCBWay CNC 6061, 1.5 mm walls, bead blast and Type II anodize with masked contact faces. A machined pedestal under the PA pad with a 0.5 mm gap pad, and tapped M3 bosses. Legend and jack markings engraved by PCBWay 0.2 to 0.5 mm deep through the anodize. Same board outline, Z stack and end-face openings as C1 | research A1 to A10; concept 7.8 |
| B | Catalog extruded box with PCBWay-cut plates (paper only) | A catalog extruded aluminum box whose board slides in its internal slots, with end and face plates cut by PCBWay (1.6 mm PCBs with copper, or CNC plates). No owner machining | SI-037; SRR minutes |
| C1 | Printed PETG case, guarded fin heatsink (build candidate) | The Recommendation of section 1 in full; geometry in `hardware/enclosure/board-outline.json` | SI-037, SI-039; this study |
| C2 | Printed PETG case, heatsink inside | The owner's literal "a heat sink to place in the enclosure": the same heatsink fully inside, with its heat leaving through the PETG back wall and the inner air | SRR minutes |
| C3 | Printed PETG case, flat aluminum back plate | A 140 x 70 x 3 mm black-anodized plate (PCBWay CNC for its holes) forms the back face and takes the PA heat through the pad | this study |
| D | Hybrid (paper only) | A catalog extruded aluminum U-channel forms the back and sides and is the heatsink. Printed PETG face and end caps are coated inside and carry every opening and marking. The board mounts to the printed face, and the PA pad presses on the channel floor through a 1.0 mm gap pad | SRR minutes (D); CR-003 step 10 |

Trade tree: the level 1 families are the four of the SRR minutes (A, B, C, D). Within C, level 2 is the heat path (C1 fins through the back behind a guard; C2 internal; C3 flat plate). A C1 variant with exposed fins (C1e) is computed for information and is not scored separately. It meets 48 C with 6.6 K of margin at 5 min, but a pocket or a hand touches the fins, and it gives up the guard's protection (section 4). Pruned before the screen: option B's route "machining-to-drawing service for a catalog enclosure" (SRR minutes route (2)), because no such service is identified in the repository and the owner has no machining tools. The do-nothing alternative is A, the current baseline of ADR-008.

### 3.3 Weight rationale

Cost has the largest weight, 25, because the owner put cost first ("I think the cheapest option is the 3D printed option", status note section 2). Schedule has 15: "one item at a time" puts each enclosure on the critical path to TRR, and a CNC order costs about three weeks (CR-003 Schedule row). Thermal margin has 15 because REQ-SYS-112 and 113 carry HZ-003 and are the known weak point of a PETG case (CR-003 Performance row). Shielding (10) and port retention (10) are baselined performance with safety links (HZ-009). The marking route (10) is the OD-38 criterion the plan names. Iteration cost (10) matters because the owner's fallback rule allows one correction before the CNC order (CR-003 Q2). Pre-build evidence (5) is the smallest because every option is verified on the unit in the end. No weight was set by the owner directly.

### 3.4 Evaluation methods

| Criterion | Method | Tool (tools/toolchain.lock.md) | Evidence artifact |
|---|---|---|---|
| M1 | Mass roll-up by part from volumes and densities; envelope by drawing | venv Python 3.13.5; `envelope_drawing.py` checks E1, E2 | Appendix A.1; `docs/reviews/PDR/figures/board-outline-envelope.png` |
| M2, C5 | Load path hand calculation | `tolerance_stack.py` L1 | `docs/design/analysis/mechanical-tolerance-stack.md` section 5 |
| M3 | Design rules and stacks | `tolerance_stack.py` S2, S3, S5, S8 | same, section 4 |
| M4, C3 | Lumped thermal network, transient and steady | `hardware/sim/enclosure/thermal_screen.py` (numpy 2.5.3, matplotlib 3.11.2, class B, no TV record of their own: developer evidence) | `hardware/sim/enclosure/out/thermal-screen.csv`; `docs/reviews/PDR/figures/ts011-thermal-screen.png` |
| M5, C4 | Schelkunoff slab and slot-aperture estimate; sheet bond resistance | `hardware/sim/enclosure/shielding_estimate.py` | `docs/design/analysis/shielding-estimate.md`; `docs/reviews/PDR/figures/shielding-estimate.png` |
| M6 | Drop deceleration first cut; drip design rule | `tolerance_stack.py` L2 | analysis section 6 |
| M7, C6 | Process comparison (research A8; CR-003 revision 3) | none | section 4 |
| M8 | HDT against peak printed-part temperature | `thermal_screen.py` | CSV columns `hdt_margin_*` |
| C1, C2, C7 | Author estimates (research A10, F21, F22; schedule.md), replaced by the WP-PDR-04 quotes | none | Appendix A.2 |
| C8 | Process inspection | none | section 4 |
| Totals, sensitivity | Weighted sum, 06 section 14.4 runs | `hardware/sim/enclosure/trade_matrix.py` | `hardware/sim/enclosure/out/trade-matrix.txt` |

### 3.5 Setup matrix (before scoring)

| Criterion | Weight | A | B | C1 | C2 | C3 | D |
|---|---|---|---|---|---|---|---|
| M1 to M9 | n/a | | | | | | |
| C1 | 25 | | | | | | |
| C2 | 15 | | | | | | |
| C3 | 15 | | | | | | |
| C4 | 10 | | | | | | |
| C5 | 10 | | | | | | |
| C6 | 10 | | | | | | |
| C7 | 10 | | | | | | |
| C8 | 5 | | | | | | |

### 3.6 Fabrication and marking route (OD-38), a sub-decision inside C

The plan names this as a criterion with its own sensitivity row. It is scored as a sub-matrix among the option C routes and fed into C6 of the main matrix as the best route of each option.

| ID | Route | Description |
|---|---|---|
| Ra | Owner prints on the H2C | PETG on the owner's H2C; legend, jack markings and facade legends debossed 0.6 mm with a flush inlay of a contrasting PETG colour printed by the second nozzle in the same job ("printed into the surface in relief or inlay", REQ-SYS-124 as CR-003 revises it) |
| Rb | PCBWay 3D-print service | Markings modelled in the part. Material and process per the PCBWay offer (research A11 lists FDM, SLA, SLS, MJF); PETG is not confirmed on the PCBWay menu (Low) |
| Rc | Ra or Rb plus PCBWay laser engraving | Laser marking on the printed part, if PCBWay offers it on the printed material (research A8 describes laser marking for metal parts only; Low) |

| ID | Criterion | Operational definition | Anchors | Weight |
|---|---|---|---|---|
| Mandatory | CON-015 (PETG) and REQ-SYS-124 | the route yields a PETG case with the legend part of the surface | pass / fail | n/a |
| R1 | Cost | cash for one case with its markings, USD | 1: >= 150 / 3: 50 / 5: <= 10 | 30 |
| R2 | Lead time and vendor independence | days to a marked case; dependence on the PCBWay closure (10-01 to 10-04) | 1: >= 12 d and closure-dependent / 3: 6 d / 5: <= 2 d, no vendor | 25 |
| R3 | Pre-build marking verification | when the TC-SYS-114 coupon can be made and rubbed | 1: after the order / 3: vendor sample / 5: at home, same process, before the build | 20 |
| R4 | Durability and legibility | depth of the colour contrast against the 500-stroke rub | 1: surface-only contrast / 3: shallow engraving or single-colour relief / 5: contrast through at least 0.5 mm | 25 |

Rb is a conditional pass on the mandatory row (PETG availability at PCBWay unknown, Low).

## 4. Scoring rationale

### 4.1 Mandatory screening

Numbers are from the scripts of section 3.4, run 2026-09-27 (`--check` PASS for each).

| Alternative | M1 | M2 | M3 | M4 | M5 | M6 | M7 | M8 | M9 | Result |
|---|---|---|---|---|---|---|---|---|---|---|
| A | conditional pass (Low): 361 g, above the 350 g TBR, within 385 g | pass: machined boss, D-flat, HEX 8 nut on 2.5 mm 6061 | pass | pass: face 33.0 C at 5 min; Tj 96.4 C | pass: 12 to 600 MHz totals 23.0 to 51.8 dB (the lower of plane wave and H field); bond by masked faces | pass (Medium) | pass: engraved | n/a | pass | kept |
| B | pass (Low): about 339 g | conditional (Low): SMA through a 1.6 mm PCB end plate, retention margin not shown | pass | **fail**: the board slides in the extrusion slots, so it is 1.6 mm (decision 87 "else" branch); Tj 110.8 C at 4.1 W | pass | conditional (Low) | pass: PCB silkscreen is admitted by CR-003 | edge rule conditional (slot-covered edges) | pass | **dropped** (M4) |
| C1 | conditional pass (Low): 375 g, above the 350 g TBR, within 385 g (Appendix A.1) | pass: port block bearing 2.31 MPa (margin 19), insert load 167 N per screw (margin 3.0 on a 500 N planning pull-out, Low); counterpoise 12 mm from the axis | pass with the stacks S2, S3, S5b, S8 | conditional pass (Low): face 28.8 C at 5 min (guard and rim; the fins are not accessible); Tj 107.5 C at an in-situ heatsink resistance of 5.5 K/W | pass with the design rules (window film, gasketed joints): 12 to 600 MHz totals 23.9 to 35.0 dB (the lower of plane wave and H field); bond 0.048 ohm at 0.03 ohm/sq with two bond points per part | conditional pass (Low): cells braced by back-shell ribs (4.4 to 8.7 MPa at 1000 to 2000 g); heatsink in its pocket; +X face carries only the sealed port | pass: debossed inlay 0.6 mm | pass: 16.2 K operating (printed rim 52.8 C), 9.0 K at +60 C storage | pass (HZ-002 and HZ-007 compartment control per CR-003 Q3, section 7) | kept |
| C2 | pass (Low) | as C1 | pass | **fail**: Tj 129.6 C | as C1 | as C1 | pass | **fail**: printed wall at 81.0 C, margin -12.0 K | pass | **dropped** (M4, M8) |
| C3 | pass (Low) | as C1 | pass | **fail**: Tj 124.7 C (a flat plate of 0.0098 m2 cannot shed 4.1 W) | as C1 | as C1 | pass | pass | pass | **dropped** (M4) |
| D | pass (Low): about 342 g | as C1 (port block in the printed end cap) | pass | pass: face 37.4 C; Tj 103.5 C with the 1.0 mm pad | as C1 for the printed face | conditional (Low) | pass | pass: 10.7 K operating, 9.0 K storage | pass | kept |

The M4 result for C1 hangs on the heatsink. The sensitivity printed by `thermal_screen.py` at 45 C steady:

| In-situ heatsink resistance | 4.1 W continuous | 3.33 W continuous (60 % efficiency) | 80 % duty of 4.1 W |
|---|---|---|---|
| 4.5 K/W | 103.4 C | 92.4 C | 91.7 C |
| 5.5 K/W (design point) | 107.5 C | 95.7 C | 95.0 C |
| 6.5 K/W | 111.6 C | 99.1 C | 98.3 C |
| 7.5 K/W | 115.7 C | 102.4 C | 101.5 C |
| 8.5 K/W | 119.8 C | 105.7 C | 104.8 C |

REQ-SYS-055 (the hardware key-down limit, 7.5 to 13 s TBR) makes a truly continuous key-down impossible on the unit. REQ-SYS-112's analysis case is continuous by statement, and WP-PDR-28 decides whether it stays so (CR-003 REQ-SYS-113 rationale, "the unit cannot sustain it"). C1 is kept as a conditional pass. Its C3 score is Low confidence, and section 6 names the heatsink datasheet as the value of information.

### 4.2 Enhancing scores (surviving alternatives A, C1, D)

| Criterion | Alternative | Measured value | Score | Confidence | Evidence |
|---|---|---|---|---|---|
| C1 | A | about USD 280 for one CNC set, anodized and engraved, with shipping (research A10: USD 258 to 370 for small 2023 orders) | 1 | L | research A10; WP-PDR-04 quote pending |
| C1 | C1 | about USD 140: coating can 60, port block 45 (PCBWay CNC minimum order USD 25 plus a shipping share), heatsink 15, springs, gasket, inserts and ITO film 15, filament 5 | 2 | L | Appendix A.2 |
| C1 | D | about USD 150: extrusion and shipping 35, coating 60, port block 45, filament and parts 10 | 2 | L | Appendix A.2 |
| C2 | A | 13 to 15 days of manufacture plus about 3 days of shipping, after the closure | 1 | M | `schedule.md` lines 51 and 54; research A10 |
| C2 | C1 | about 3 days: print about 1 day, coat and cure 24 h, assemble; the port block rides with the board order and is not on the case's critical path | 5 | M | Appendix A.2 |
| C2 | D | catalog extrusion delivery about 5 days, printing in parallel | 4 | L | author estimate |
| C3 | A | 13.6 K | 4 | L | thermal screen |
| C3 | C1 | 2.5 K at 5.5 K/W | 1 | L | thermal screen |
| C3 | D | 6.5 K | 2 | L | thermal screen |
| C4 | A | 66.3 dB | 5 | M | shielding estimate |
| C4 | C1 | 9.5 dB | 1 | L | shielding estimate |
| C4 | D | 9.3 dB | 1 | L | shielding estimate |
| C5 | A | 5 or more (the SMA nut on a 2.5 mm 6061 boss; research F8 via ICD-TX-ANT) | 5 | M | ICD-TX-ANT 3.2.2 |
| C5 | C1 | 3.0 (insert pull-out, planning value) | 3 | L | tolerance analysis L1 |
| C5 | D | 3.0 (same port block in a printed end cap) | 3 | L | as C1 |
| C6 | A | PCBWay engraving: coupon only as a vendor sample | 3 | M | research A8 |
| C6 | C1 | route Ra: coupon printed and rubbed at home before the build | 5 | M | section 4.3 |
| C6 | D | route Ra on the printed face and ends | 5 | M | as C1 |
| C7 | A | a re-order: about USD 280 and 17 days | 1 | M | research A10 |
| C7 | C1 | reprint of a shell (USD 3) and a recoat (a third of a can, USD 20), 2 to 3 days | 4 | M | Appendix A.2 |
| C7 | D | reprint of the face or end caps and a recoat, about USD 23, 2 to 3 days (an extrusion problem means a re-order, 5 days) | 4 | L | author estimate |
| C8 | A | fit-check print of the CNC model only | 3 | M | research A11 |
| C8 | C1 | the delivered case itself printed, coated, measured (coupon Rs, bond, fit with a bare board of CR-006) before board arrival | 5 | M | CR-006 section 3.1 A |
| C8 | D | as C1 | 5 | M | as C1 |

### 4.3 Route sub-matrix scores (OD-38)

| Criterion | Ra | Rb | Rc | Confidence and evidence |
|---|---|---|---|---|
| R1 cost | 5 (about USD 5 of PETG) | 2 (PCBWay FDM or MJF case with shipping, about USD 60 to 120) | 1 (Rb plus engraving setup) | Ra M (owner filament); Rb and Rc L (no quote; OD-38 preliminary: no print quote requested) |
| R2 lead and independence | 5 (1 day, no vendor) | 2 (about 5 to 10 days with shipping, waits for 10-05) | 1 | M; `schedule.md` closure row |
| R3 marking verification | 5 (coupon at home) | 3 | 3 | H for Ra; M for Rb and Rc |
| R4 durability and legibility | 4 (colour through 0.6 mm; inlay bond of PETG to PETG, Low) | 2 (single-colour relief, contrast by shadow only) | 3 (laser marks on plastic are shallow, contrast uncertain, Low) | L |

Route Ra is recommended for option C. PCBWay engraving is the marking route of the CNC fallback (research A8: engraving 0.2 to 0.5 mm; artwork as SVG on the drawing, A2), which is how "PCBWay would have to do it" reads for a metal part (plan OD-38).

**Per-route verification and release content (plan WP-PDR-27 route paragraph):**

| Item | Ra (recommended) | Rb | Rc | CNC fallback |
|---|---|---|---|---|
| REQ-SYS-124 closing (TC-SYS-086) | callout inspection on the print model: debossed 0.6 mm, inlay colour named, face named | callout on the PCBWay print drawing | as Rb plus the engraving SVG | engraving callout on the PCBWay drawing, SVG artwork |
| REQ-SYS-191 coupon (TC-SYS-114 note) | H2C coupon of the legend, jack-marking and facade areas in the same filament pair and settings | PCBWay sample part | as Rb | engraved sample from PCBWay |
| Legible under the coating? | yes: the coating is inside only; every exterior face is masked when spraying, so no marking is ever coated | same | same | not coated |
| Cost line (WP-PDR-46) | about USD 5 per case | USD 60 to 120 (no quote) | Rb plus engraving | inside the CNC quote |
| Lead time against the 10-01 to 10-04 closure | none | order after 10-05 | same | order after 10-05, about 17 days |
| Release package `ME-ENC-rev<X>-<n>` (05 line 154 as CR-003 F10 generalizes it) | OpenSCAD CSG, `.3mf` print model with the slicer settings, coating instruction (Appendix B.4), heatsink, spring, gasket, insert and film part numbers, port block STEP and drawing | PCBWay print order package | same plus SVG | CSG, STEP, drawing, SVG (held) |

## 5. Final decision matrix

| Criterion | Weight | A score | A weighted | C1 score | C1 weighted | D score | D weighted |
|---|---|---|---|---|---|---|---|
| C1 cost | 25 | 1 | 25 | 2 | 50 | 2 | 50 |
| C2 schedule | 15 | 1 | 15 | 5 | 75 | 4 | 60 |
| C3 thermal margin | 15 | 4 | 60 | 1 | 15 | 2 | 30 |
| C4 low-frequency shielding | 10 | 5 | 50 | 1 | 10 | 1 | 10 |
| C5 port retention | 10 | 5 | 50 | 3 | 30 | 3 | 30 |
| C6 marking route | 10 | 3 | 30 | 5 | 50 | 5 | 50 |
| C7 iteration cost | 10 | 1 | 10 | 4 | 40 | 4 | 40 |
| C8 pre-build evidence | 5 | 3 | 15 | 5 | 25 | 5 | 25 |
| **Total** | **100** | | **255** | | **295** | | **295** |
| **Percent of maximum** | | | 51.0 % | | 59.0 % | | 59.0 % |
| **Rank** | | | 3 | | 1 (tie) | | 1 (tie) |

Route sub-matrix: Ra 475 (95.0 %), Rb 220 (44.0 %), Rc 190 (38.0 %).

## 6. Uncertainty and sensitivity statement

1. **Weight sensitivity.** Computed by `trade_matrix.py`. From the tie, a weight change breaks it one way or the other. C2 schedule +10 puts C1 first (319.1 against D 307.4), and -10 puts D first. C3 thermal +10 puts D first, and -10 puts C1 first. C4 low-frequency shielding +10 puts A first (282.2 against 273.3 for C1 and D). Route sub-matrix: no change.
2. **Score sensitivity.** 10 Low-confidence cells, in 17 of their +1 and -1 moves, change the top rank. Among them: C1 cost 2 to 3 puts C1 first (320); C1 thermal 1 to 2 puts C1 first (310); D thermal 2 to 1 puts C1 first (280); D cost 2 to 3 puts D first (320). The full list is in `hardware/sim/enclosure/out/trade-matrix.txt`. Route sub-matrix: no change.
3. **Assumptions and their evidence:**
   - The PA dissipates 4.1 W at worst, RthJC is 3 C/W (TS-001 M5 row), the via array is 4.7 K/W at 1.0 mm (research F16), the gap pad is 0.74 K/W (F18). TS-004 selects the 1.0 mm board; at 1.6 mm, C1 fails M4 (119.4 C).
   - The C1 heatsink reaches 5.5 K/W in situ. This is an assumption with Low confidence; section 8 design rule 3 turns it into a selection rule.
   - Every coating value is recalled (Appendix B), not read.
   - Costs and lead times are the author's estimates before the WP-PDR-04 quotes.
   - The FDM tolerances are planning values until the WP-PDR-39 fit-check coupon.
   - The mass roll-up uses densities and envelope volumes (Appendix A.1).
4. **Robustness verdict:** Not robust. C1 and D tie at 295, and both the weights and the Low cells move the top rank either way. A reaches the top only with the low-frequency shielding weight raised by 10.
5. **Value of information** (06 section 14.4 item 4):
   - The heatsink datasheet: a catalog part at most 40 x 58 x 23 mm with a published natural-convection curve. The owner fetches it, 1 hour, before B1b. If it shows 5.5 K/W or better in situ, C1's C3 score rises to 2 and C1 leads alone (310).
   - WP-PDR-28a, the first-cut thermal per option (Tue 09-29), replaces the author's screen.
   - A catalog extrusion datasheet for D: inside dimensions for a 62 mm board and 14.86 mm holders, and price.
   - The WP-PDR-04 PCBWay quotes, which price the port block and the CNC fallback.

   None of these was performed before this draft: they are owner downloads (OD-18, OD-39) or other work packages. The recommendation therefore presents C1 and D together (06 section 14.5), with C1 as the lead SE's choice for the reasons of section 8.
6. **Limitations of the methods and tools (SE HB section 6.8.1.2.5):**
   - The thermal model is lumped. Heatsink resistance, convection and radiation coefficients are estimates, and the guard and rim nodes are observers that take no credit for the heat they carry.
   - The shielding model is a Schelkunoff slab plus slot apertures summed in power. It is not a field solver, and its aperture and seam terms carry about +/-6 dB.
   - The tolerance stacks use planning FDM values.
   - Every script runs on the venv Python whose numpy and matplotlib have no TV record of their own (`tools/toolchain.lock.md` section 2, class B). All numbers are developer evidence until the analysis records are APPROVED and the tools accredited (plan rule C10).
   - No PCBWay or DigiKey quote exists yet.

## 7. Risks and benefits of the surviving alternatives

| Alternative | Risk statement | L | C (driving dimension) | Score / band | Would be entered as |
|---|---|---|---|---|---|
| C1 | Given a heatsink of at most 40 x 58 x 23 mm behind a guard in natural convection, there is a possibility that its in-situ resistance exceeds 5.5 K/W, adversely impacting the PA junction margin of REQ-SYS-112, leading to a larger heatsink, a CR on the analysis case, or the CNC fallback | 3 | 3 (performance margin) | 9 Yellow | merge into RSK-006 (CR-003 candidate (d)) |
| C1 | Given a sprayed coating of about 0.03 ohm/sq on PETG, there is a possibility that the 1.5 and 2.2 MHz converter fields leave the case less than 20 dB below their board-level level, adversely impacting REQ-SYS-177 and the owner's near-field acceptance measurement, leading to a CR on the REQ-SYS-177 scope, board shield cans, or the CNC fallback | 4 | 3 (performance margin) | 12 Red | new, CR-003 candidate (a) |
| C1 | Given a solvent-borne acrylic coating on PETG, there is a possibility of crazing or poor adhesion, adversely impacting the shield and the bond, leading to a recoat with 843WB or a different product | 3 | 2 (cost) | 6 Yellow | CR-003 candidate (a) |
| C1 | Given PETG with a heat-deflection temperature near 69 C, there is a possibility of creep at the port block and bosses during +60 C storage, adversely impacting REQ-SYS-105 and REQ-SYS-115, leading to a filament CR (CON-015, PCR-9) | 2 | 3 (performance margin) | 6 Yellow | CR-003 candidate (b) |
| C1 | Given a PETG case with no flame rating (SI-039), there is a possibility that a venting cell ignites the case, adversely impacting HZ-002 and HZ-007, leading to fire beyond the unit | 2 | 5 (safety) | 10 Red (safety override, 06 section 7 rule 2) | RSK-007 (CR-003 candidate (e)); the compartment control of OQ-SAF-010 (WP-PDR-16) is the mitigation, and the owner accepts the residual as SMA TA (OD-05) |
| C1 | Given a mass roll-up of 375 g, there is a possibility that the unit exceeds 350 g, adversely impacting REQ-SYS-102 and MOE-013, leading to a TBR value of 380 g or mass reductions | 4 | 2 (performance margin) | 8 Yellow | TPM-001 (WP-PDR-29) |
| A | Given a CNC order after an option C failure, there is a possibility of a 3-week TRR slip and a USD 280 spend, adversely impacting schedule and cost, leading to TRR about 11-26 instead of 11-05 | 3 | 3 (schedule) | 9 Yellow | RSK-053 (CR-003 candidate (c)) |
| A | Given 1.5 mm 6061 walls, there is a possibility that the unit exceeds 350 g (361 g estimate), adversely impacting REQ-SYS-102 | 3 | 2 (performance margin) | 6 Yellow | TPM-001 |
| D | Given a catalog extrusion whose inside must hold a 62 mm board and 14.86 mm holders within 70 x 40 mm outside, there is a possibility that no stocked extrusion fits, adversely impacting REQ-SYS-103, leading to option C1 or A | 3 | 3 (performance margin) | 9 Yellow | not entered (D paper only) |
| D | Given the PA pad pressed on the extrusion floor through a 1.0 mm pad across a +/-0.5 mm stack, there is a possibility of poor contact, adversely impacting REQ-SYS-112 | 3 | 3 (performance margin) | 9 Yellow | not entered |

Aggregate risk per alternative (maximum score): C1 12 (Red, low-frequency shielding) and 10 Red by safety override (fire; common to C1 and D, which share printed PETG parts); A 9; D 10 by the same safety override.

| Alternative | Benefits beyond the scored criteria |
|---|---|
| C1 | Exactly the owner's direction and the concept the owner preferred at SRR ("option C plus we could buy a heat sink"); every part except the port block is in the owner's hands; the four spare bare boards of CR-006 give fit checks at home |
| A | Best thermal, shielding and robustness; already designed in the research; the held package costs nothing until ordered |
| D | Metal back and sides give most of A's thermal and robustness benefit at C's cost; the printed parts keep the home-made markings |

## 8. Recommendation

- **Recommended alternative:** C1, with route Ra and the coating of Appendix B, presented together with D (tie at 295, 59.0 %; 06 section 14.5). A stays the held CNC fallback.
- **Rationale for C1 over D at the tie:**
  1. **Owner direction.** CON-015 as CR-003 revision 3 words it names "an H2C-printed PETG case with a conductive coating and a heatsink" as the item built first, and CR-003 step 10 puts D on paper. Choosing D needs a change to the CR-003 text before disposition, or a later CR.
  2. **Evidence.** C1's thermal weakness is decided by one catalog datasheet (value of information 1). D's unknowns are a stocked extrusion that fits and a floor contact through a 1 mm pad: two items with no data in the repository.
  3. **Margin to gain.** Every C1 correction is a reprint or a recoat, which is the correction step of CR-003 Q2.

  If the owner weighs thermal margin higher, D is the better paper choice (section 6 item 1).
- **Design rules that make C1 pass its mandatory criteria** (inputs to WP-PDR-37, 39, 28, 36 and the release package):
  1. Board 130 x 62 x 1.0 mm (TS-004) on six M3 bosses. Z stack 30 mm, and the heatsink and guard use up to 10 mm beyond the back (40 mm total, REQ-SYS-103). Everything else is per `hardware/enclosure/board-outline.json`.
  2. The PA sits over a 15 x 15 mm mask-free pad above the heatsink footprint, at the +X end, near the port.
  3. **Heatsink selection rule.** A catalog extruded aluminum heatsink, black anodized, footprint at most 40 x 58 mm, overall height at most 23 mm, flat base at least 3 mm, and no holes needed. Its datasheet natural-convection resistance must be 4.5 K/W or less at a 30 K rise, so that it is 5.5 K/W or less in situ behind the guard. It is spring-loaded against the gap pad by two compression springs in the guard frame (tolerance stack S6c), and bonded to the coating by a conductive fabric-over-foam gasket on the pocket ledge.
  4. **Guard.** Slots 6.0 mm wide; fin tips at least 2.5 mm behind the guard's outer face (the finger enters 0.80 mm; `envelope_drawing.py` E5).
  5. **Printed-part isolation.** No PETG face touches the heatsink except through the gasket (printed rim at most 52.8 C at the REQ-SYS-112 condition). A printed wall and at least 3 mm of air separate the heatsink pocket from the cell bay, and WP-PDR-28 computes the cell temperature.
  6. **Port block.** 6061, 12 x 20 x 12 mm, from PCBWay with the board order. It carries the SMA D-hole, a tapped M3 counterpoise hole 12 mm from the axis, and two M3 screws into heat-set inserts. It is captured between the shells, and the SMA is joined to the board by an RG-316 pigtail about 35 mm long (stack S1).
  7. **Joints.** Every shell joint is a 3 mm overlapping lip, coated on both mating faces, with a continuous conductive gasket. Two or more bond points per coated part, at its ends, are M3 screws with toothed washers on coated lands.
  8. **Display window.** An ITO-coated PET film of at most 20 ohm/sq behind the lens, edge-bonded to the coating. The display glass is located in a front-shell pocket, not on the board (stack S4b).
  9. **USB opening.** 12.6 x 10.6 mm (stack S5b). This is a change request to ICD-CTL-USB's 12.0 x 10.0 (WP-PDR-36).
  10. **Coating.** Inside only, exterior masked; 843AR at a design value of 0.03 ohm/sq or less, measured on a coupon sprayed in the same session (Appendix B.4).
  11. **Markings.** Route Ra. The legend is on the y = 0 side face, the jack markings on the -X end face, 3.5 mm sans-serif characters with at least 0.6 mm stroke.
  12. **Cell door.** Slides in grooves whose frame overlaps its leading edge by 3 mm, so no accessible closing gap opens between 4 and 25 mm (REQ-SYS-168).
  13. **Drip.** No opening on the +X face except the sealed port. The heatsink base gasket seals the interior from the fin channels.
- **Impacts of adopting the recommendation:**
  - **Requirements:** proposed values in the table below, and PCR-9 candidates:
    - REQ-SYS-177 frequency scope, if the owner does not accept board shield cans;
    - REQ-SYS-115 lower bound: the LS013B7DH03 storage rating is -10 C (`display-and-ui-parts.md` F2) against -20 C (TBR); cross item to WP-PDR-25 and 28;
    - REQ-SYS-102, if 380 g is ruled.
  - **Interfaces:** ICD-TX-ME and ICD-CTL-ME are written on C1 and A (WP-PDR-36), with ICD-CTL-USB at 12.6 x 10.6 and ICD-TX-ANT's PCB connection row set to the RG-316 pigtail.
  - **Cost:** option C line about USD 140 for the first case (Appendix A.2); the CNC fallback shown separately at about USD 280 until the quote (WP-PDR-46).
  - **Schedule:** none on the critical path. The option C case is made before board arrival.
  - **Verification:** TC-SYS-077 uses the scripted finger check (a TV record is required, CR-003 R3-F3), TC-SYS-107 uses the coating value, TC-SYS-114 uses a route Ra coupon, TC-SYS-075 uses the bond chain of rule 7.
- **Corrective actions if the recommendation is adopted late** (after B1b): the WP-PDR-37 floorplan starts on this outline at risk. Only the heatsink footprint and the port block keep-out move if D is chosen.

**Proposed values** (developer evidence, closing at the PDR memo on APPROVED records, rule C10):

| Item | Current (TBR) | Proposed | Basis |
|---|---|---|---|
| REQ-SYS-102 mass | 350 g | 380 g, or 350 g with the mass reductions of Appendix A.1; WP-PDR-29 decides on its bottom-up | Appendix A.1 (C1 375 g, A 361 g) |
| REQ-SYS-103 envelope | 140 x 70 x 40 mm | keep: C1 uses 140 x 70 x 30 mm plus 10 mm of heatsink and guard | `board-outline.json`; E2 |
| REQ-SYS-105 return-loss change | 1 dB | keep | tolerance analysis section 5 |
| REQ-SYS-106 mating life return-loss change | 1 dB | keep (stainless SMA, 500-cycle class, ICD-TX-ANT 3.2.2) | ICD-TX-ANT |
| REQ-SYS-107 counterpoise | 20 mm, 10 mohm | keep: 12 mm by design; 6061 port block with a toothed washer | tolerance S9 |
| REQ-SYS-109 bond | 0.1 ohm | keep: 0.048 ohm computed at 0.03 ohm/sq with two bond points | shielding analysis section 6 |
| REQ-SYS-113 test finger | 12 mm | 12 mm diameter, hemispherical tip, straight, 80 mm reach, swept from every outward direction (recalled from IEC 61032 probe B, not in the corpus, Low) | CR-003 REQ-SYS-113 rationale |
| REQ-SYS-114 operating range | -10 to +45 C | keep (PETG, coating and heatsink ratings exceed it) | section 4.1 M8 |
| REQ-SYS-115 storage range | -20 to +60 C | keep +60 C (PETG margin 9.0 K, Low); -20 C is flagged against the display's -10 C storage rating | M8; display F2 |
| REQ-SYS-116 drop | 1.0 m | keep (analysis target, OD-33) | tolerance L2 |
| REQ-SYS-117 rain | IPX2 | keep (OD-33) | rule 13 |
| REQ-SYS-139 board thickness | 1.0 mm | 1.0 mm (TS-004) | TS-004 |
| REQ-SYS-168 pinch gap | 4 mm and 25 mm | keep (recalled from ISO 13857 and ISO 13854 practice, not in the corpus, Low) | rule 12 |
| REQ-SYS-177 shielding | 20 dB | keep at 20 dB for 12 MHz and above; the switcher fundamentals go to the owner (PCR-9 or board shield cans) | shielding analysis |
| REQ-SYS-191 rub | 15 s water, 15 s IPA, 500 dry strokes at 5 N | keep; confirmed on the route Ra coupon before the build | section 4.3 |

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

- NASA/SP-2016-6105 Rev 2 (SE HB) section 6.8.1.2.1 to 6.8.1.2.7, section 6.8.1.3.1 and Table 6.8-1 (corpus `docs/references/md/nasa-se-handbook/22-6-8-decision-analysis.md`).
- `docs/process/06-risk-and-decision-analysis.md` sections 6, 7, 8, 13, 14 and 16.
- 47 CFR 15.23(b) (corpus: 47cfr-15.23.md, eCFR issue 2026-09-23): good engineering practice for the digital section, which REQ-SYS-177 implements.
- `docs/cm/cr/CR-003-solution-neutral-enclosure.md` revision 3 (sections 1, 4, 5, 6.4, 12); `docs/cm/cr/CR-006-build-sequence-one-unit-first.md` revision 2.
- `docs/plan/status/status-2026-09-27.md` sections 2 to 4; `docs/plan/pdr-work-plan.md` WP-PDR-27, OD-10, OD-33, OD-38.
- Research reports named in section 2; ICDs ICD-PWR-CELL, ICD-CTL-USB, ICD-TX-ANT.
- Analyses of this work package: `docs/design/analysis/shielding-estimate.md`, `docs/design/analysis/mechanical-tolerance-stack.md`; scripts under `hardware/sim/enclosure/`; data `hardware/enclosure/board-outline.json`.

## Appendix A. Supporting analysis

### A.1 Mass roll-up (Low; densities 2.70 g/cm3 for 6061, 1.27 for PETG)

| Item | A | C1 | D |
|---|---|---|---|
| Common: 2 cells 96, 2 holders about 22, board and SMT parts about 35, Pico 2 3, display 3.6, 2 encoders about 16, 2 knobs about 8, 2 jacks 4, SMA 4, 2 buttons 2, screws and pads about 10 | 204 | 204 | 204 |
| Case | 6061, 0.0364 m2 x 1.5 mm = 147 g, pedestal and bosses 10 | PETG, (0.0364 - 0.0023) m2 x 2.0 mm = 87 g, bosses, ribs and guard frame 15 | extrusion about 85, printed face and ends about 40 |
| Heatsink, port block, springs, gasket, inserts, film, coating | none | 50 + 8 + 8 + 3 | port block 8, gasket and coating 5 |
| **Total** | **361 g** | **375 g** | **342 g** (rounded) |

Mass reductions for C1, if 350 g is kept: 1.6 mm walls away from the bosses and the port end (about -15 g), and a 40 g heatsink if the datasheet allows (about -10 g). Together they reach about 350 g, at the cost of heatsink margin.

### A.2 Cost and schedule estimates (Low; author's estimates for the first unit, USD, 2026-09-27)

- **C1 (about USD 140):** coating aerosol, one can for two to three cases, about 60; port block about 45 (research A10: PCBWay CNC minimum order USD 25, plus a shipping share on the board order); heatsink about 15; springs, fabric-over-foam gasket, M3 heat-set inserts and ITO film about 15; PETG in two colours, including one reprint, about 5.
- **A (about USD 280):** research A10 (small 2023 orders USD 258 to 370).
- **D (about USD 150):** extrusion about 25 plus shipping 10, coating 60, port block 45, filament and parts about 10.
- **Schedule:** C1 print 1 day, coat and cure 24 h, assemble 1 day. A: 13 to 15 days of manufacture plus about 3 days of shipping, ordered only after option C fails.

### A.3 Literature and research search

Claude Context searches on 2026-09-27 over `/Users/robinonsay/rust/cwht`:
- "enclosure trade study option C printed PETG conductive coating CNC fallback TS-011";
- "design reader report items enclosure board thickness TS-004 ...";
- "PCBWay 4-layer board thickness ... via fill";
- "PD54008L-E thermal resistance";
- "display candidate size active area window";
- "switching frequency of buck regulator and charger";
- "47 CFR 15.23";
- "SE HB 6.8 decision analysis Table 6.8-1";
- "envelope 140 x 70 x 40 stack height 18650 holders".

The design reader report the plan cites for items 10, 11, 22, 23, 40, 43, 95 and 96 is not in the repository (no search hit). Those items are closed here by their subjects as the plan names them (outline, thickness, heatsink, shielding, coating, legend), and the return reports the gap.

### A.4 Decision metrics

Opened and drafted 2026-09-27. Six alternatives, three dropped at the mandatory screen. Eight enhancing criteria, no revision yet.

## Appendix B. Conductive coating research (owner input 7)

**Status of this appendix.** No download or web access was permitted for this work package (owner permissions OD-18, OD-21, OD-25, OD-39 and A-1 are not given). Every product value below is the author's recollection of the manufacturers' published technical data sheets (TDS), with confidence Low unless stated. None of these values closes a TBR until the owner fetches the TDS listed in B.3 and the values are re-read from it.

### B.1 Candidates

| Product (manufacturer) | Filler, binder, carrier | Published surface resistivity (recalled) | Service temperature (recalled) | Cure (recalled) | Fit for cwht |
|---|---|---|---|---|---|
| **843AR Super Shield silver-coated copper, aerosol** (MG Chemicals) | silver-coated copper flake, acrylic, solvent-borne aerosol | about 0.02 to 0.05 ohm/sq at the recommended dry film of about 1 to 2 mil (25 to 50 um) | about -40 to +120 C | touch dry in minutes; full properties after about 24 h at room temperature (a heat cure is offered, not usable on PETG) | **Recommended.** Best conductivity per dollar of the aerosol class; oxidation of copper is slowed by the silver and the coating is inside only; adhesion to plastics published as good on ABS, PC and similar (PETG to be confirmed on a coupon) |
| 842AR Super Shield silver, aerosol (MG Chemicals) | silver flake, acrylic | about 0.01 ohm/sq or lower | similar | similar | Fallback if the 843AR coupon exceeds 0.03 ohm/sq; about two to three times the price |
| 843WB silver-coated copper, water-based (MG Chemicals) | as 843AR, water-borne | somewhat higher than 843AR | similar | longer air dry | Fallback if the solvent of 843AR crazes PETG |
| 841AR Super Shield nickel, aerosol (MG Chemicals) | nickel flake, acrylic | about 0.5 to 1 ohm/sq | similar | similar | Not recommended: the bond of REQ-SYS-109 fails (0.89 ohm at 0.7 ohm/sq, shielding analysis section 6) and the low-frequency shielding is lower still |
| 838AR Total Ground carbon, aerosol (MG Chemicals) | carbon, acrylic | tens of ohm/sq (ESD grade) | similar | similar | Not suitable (ESD grade, not EMI) |
| CHO-SHIELD conductive coatings (Parker Chomerics) | silver or silver-copper in various binders | about 0.01 to 0.1 ohm/sq by grade | by grade | by grade | Industrial packaging and minimum quantities; kept as a reference class only |
| GRAPHIT 33 (CRC Kontakt Chemie) | graphite, aerosol | high (ESD grade) | by TDS | by TDS | Not suitable |

The owner's GPS work used a "metal spray paint" whose name is not known (status note section 2). A copper or nickel aerosol of the classes above fits that description.

### B.2 Selection

843AR is recommended. It is the only class that meets both REQ-SYS-109 (0.1 ohm, with margin at 0.03 ohm/sq) and the 12 to 600 MHz shielding with margin, at an aerosol price, applied by the owner with no equipment. The recalled values set the design value **Rs <= 0.03 ohm/sq** (the shielding estimate and bond calculation use it). The coupon test of B.4 confirms it before the case is coated.

### B.3 Datasheets the owner should fetch (no downloads by agents)

1. MG Chemicals 843AR technical data sheet and safety data sheet (current revision): surface resistivity versus dry film thickness, coverage per can, adhesion by substrate, service temperature, solvent list, cure schedule.
2. MG Chemicals 842AR and 843WB technical data sheets (the two fallbacks).
3. The filament technical data sheet of the PETG the owner will print (the Bambu Lab or other brand actually used): heat-deflection temperature at 0.45 MPa and 1.8 MPa (ISO 75), and chemical resistance to the coating's solvent.
4. A catalog extruded heatsink datasheet meeting section 8 rule 3, with its natural-convection resistance curve, searched at DigiKey or Mouser with the filters: footprint at most 40 x 58 mm, height at most 23 mm, black anodized, extruded, board-level or bolt-on.
5. An ITO-coated PET film datasheet (sheet resistance at most 20 ohm/sq, visible transmission), for the display window; cross item to WP-PDR-25 for REQ-SYS-165 legibility.
6. For D only: a catalog extruded aluminum U-channel or tube with inside dimensions for a 62 mm board and 14.86 mm holders.

### B.4 Coating instruction draft (for the release package) and coupon tests before the build

1. **Coupon (owner, at home, before coating the case):**
   - Print a 10 x 100 x 2 mm PETG strip and a 40 x 40 mm cross-hatch square in the case filament.
   - Scuff with 400 grit, wipe with isopropyl alcohol, dry.
   - Spray the case interior and the coupons in the same session.
2. **Sheet resistance.** After 24 h, drive 0.10 A from the bench supply (current-limited) along the 10-square strip through the end clamps. Read the voltage between two points 80 mm apart (8 squares) on the multimeter: Rs = V / (0.10 x 8). Pass at 0.03 ohm/sq or less, which is 24 mV or less.
3. **Adhesion.** Cut a 1 mm cross-hatch with a knife, apply tape, pull. Pass when no squares lift (the ASTM D3359 method B scale is recalled, not in the corpus).
4. **Solvent attack.** Inspect the coupon back face through the PETG for whitening or crazing after 24 h. If present, change to 843WB.
5. **Bond.** Fit an M3 screw with a toothed washer on a coated land of the strip. Four-wire from the screw to the far end at 0.1 A: pass at 0.1 ohm or less.
6. **Application to the case:**
   - Mask every exterior face and the display window opening.
   - Leave the bond lands and joint lips coated.
   - Apply two to three light coats to about 50 um.
   - Cure 24 h at room temperature, never heated.
   - Repeat steps 2 and 5 on the case at its bond points and farthest points before assembly: the option C acceptance item (c) data (CR-003 section 5 item 3).

## Change log

| Revision | Date | Change | Reason |
|---|---|---|---|
| 0 | 2026-09-27 | Initial draft, wave 1a | WP-PDR-27 |
