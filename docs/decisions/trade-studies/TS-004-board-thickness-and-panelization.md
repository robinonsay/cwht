# TS-004: Board thickness, via fill and panelization

| Field | Value |
|---|---|
| ID | TS-004 |
| Status | Draft, revision 0 (2026-09-27, wave 1a draft of WP-PDR-27). **AT RISK (CR-003, CR-006):** the thermal screen uses the option C heat path of TS-011 (CR-003 revision 3, Submitted) and the quote set of one assembled board of CR-006 revision 2 (Submitted). Cost and lead-time scores are Low confidence until the WP-PDR-04 instant quotes (`docs/reviews/PDR/owner-actions.md` section 2.4, rows Q-01 to Q-08) are in |
| Decision class trigger | 06 section 14.1 class 1 item (c): the choice touches HZ-003 (PA junction and accessible surface temperature through the via array). Named as a PDR study in `docs/design/concept.md` section 11.2 (row TS-004) |
| Decision maker | Robin (owner, Decision Authority) |
| Recommender | Claude (ME designer, WP-PDR-27 author invocation, 2026-09-27) |
| Independent reviewer | INSP-NNN in `docs/reviews/PDR/checklists/ts-004-board-thickness-and-panelization.md`, from `docs/templates/peer-review-checklist-risk.md` section B |
| Decide by | PDR (B1b, OD-10), because the allocated baseline fixes REQ-SYS-139 (TBR 1.0 mm) and the board outline gates the layout after PDR (`docs/plan/schedule.md` lever 2) |
| Related risks | RSK-006, RSK-026 (thermal path); RSK-044 (CAD pipeline, through the board outline) |
| Related requirements and hazards | REQ-SYS-112, REQ-SYS-113, REQ-SYS-137, REQ-SYS-139, REQ-SYS-140; HZ-003; SRR decision 87 (1.0 mm if the enclosure gives four bosses, else 1.6 mm); NGO-027 |
| Resulting ADR | ADR-039 (provisional, plan section 3.1), written the day the owner decides |
| Dates | opened 2026-09-27; recommended: after the INSP record is APPROVED (rule C9); decided: B1b |

## 1. Executive summary

- **Recommendation (one sentence):** T1, a 1.0 mm 4-layer board on the PCBWay standard stackup, with via-in-pad under the PA and QFN pads resin filled and capped (IPC-4761 Type VII, "All vias filled with resin and capped"), built as a single 130 x 62 mm board with two 5 mm tab-routed rails (P1), because it is the only thickness at which the option C heat path of TS-011 meets REQ-SYS-112 (107.5 C against 110 C TBR at 4.1 W). It also leads the matrix by 105 points when that screen is relaxed.
- **Problem requiring a decision (one sentence):** board thickness, via treatment under the PA and panelization, which together set the PA via-array thermal resistance, the board stiffness under the controls, the PCBWay assembly acceptance and the outline delivered to the layout.
- **Robustness verdict (section 6):** Robust. T1 is the only survivor of the mandatory screen on the option C path. On the relaxed screen (CNC fallback path, where all four thicknesses pass) T1 still leads with no perturbation changing the rank. Robust for panelization.
- **Owner's decision (section 10):** pending.

## 2. Problem and decision context

- **Mission and system context:**
  - The PA (PD54008L-E, TS-001) sinks its heat through a 25-via array (0.30 mm drill, 0.65 mm pitch) to a mask-free bottom pad pressed on the enclosure heat path. That path is a spring-loaded heatsink in option C and a pedestal in the CNC fallback (TS-011).
  - The via array's thermal resistance scales with board thickness: 4.7 K/W at 1.0 mm and 7.6 K/W at 1.6 mm with a 25 um barrel (`docs/research/pcbway-export-and-vendor-questions.md` F16).
  - The board carries panel-mounted encoders and board-mounted buttons, and the two cell holders hang below it (ICD-PWR-CELL 3.2.2).
- **Decision needed and intended outcome:** REQ-SYS-139's thickness value, the via fill option on the PCBWay order, and the panel form, so that WP-PDR-37 lays out on a fixed outline (`hardware/enclosure/board-outline.json`) and WP-PDR-38 and WP-PDR-46 price the order.
- **Constraints:**
  - SRR decision 87 (owner ruling 2026-09-26): 1.0 mm if the enclosure gives four bosses, else 1.6 mm. Option C and the CNC fallback both give six (TS-011).
  - PCBWay standard 4-layer stackups: the outer prepreg is the same 7628 at every thickness, so the 50 ohm microstrip geometry does not change (F5, F6 of `pcbway-fabrication-and-assembly.md`).
  - PCBWay assembles via-in-pad only resin filled (PCBWAY-FAB F15, cited in export F15 and F19).
  - Panelization is required below 50 x 100 mm, and rails when copper is within 3.5 mm of the long edges (F19).
  - CR-006: 5 boards fabricated, 1 assembled.
- **Prior related decisions:** ADR-007 (turnkey SMT, Type VII under the PA and QFN pads proposed); concept 7.8 and section 12 descope row (1.6 mm if bosses fail).
- **Research consulted:** `pcbway-fabrication-and-assembly.md` F5, F6, F9, F19 to F22; `pcbway-export-and-vendor-questions.md` F14 to F19; `docs/decisions/trade-studies/TS-011-enclosure.md`; `docs/design/analysis/mechanical-tolerance-stack.md` section 8.

## 3. Decision matrix setup and rationale

### 3.1 Criteria and operational definitions

| ID | Criterion | Type | Operational definition | Scale | Weight |
|---|---|---|---|---|---|
| M1 | PCBWay standard capability | Mandatory | standard stackup exists at the thickness; drill aspect ratio at most 8 for 0.30 mm; the via option is on the order form (F5, F9, F15) | pass / fail | n/a |
| M2 | 50 ohm geometry unchanged | Mandatory | same outer prepreg (7628, Dk 4.74) above L2 ground (F5, F6) | pass / fail | n/a |
| M3 | REQ-SYS-112 on the build-candidate heat path | Mandatory | junction at most 110 C (TBR) at 45 C, 4.1 W continuous, on the option C path of TS-011 (heatsink 5.5 K/W in situ): `thermal_screen.py`; a via array with voided joints adds 1.2 K/W (AN4005 allows 20 % voiding, export F14; Low) | pass / fail | n/a |
| M4 | PCBWay assembly acceptance | Mandatory | the via treatment under exposed pads is accepted for turnkey assembly without a review flag (F15, F19) | pass / fail | n/a |
| M5 | Decision 87 | Mandatory | 1.0 mm only with four or more bosses under the board | pass / fail | n/a |
| K1 | Via-array resistance | Enhancing | K/W of the 25-via array including the joint | 1: >= 7.6 / 2: <= 6.6 / 3: <= 5.6 / 4: <= 5.15 / 5: <= 4.7 | 35 |
| K2 | Stiffness | Enhancing | support posts needed beyond the six bosses to hold a 10 N button press under 0.3 mm (analysis L3) | 1: >= 4 / 3: 2 / 5: 0 | 15 |
| K3 | Cost | Enhancing | 5 boards with the via option, USD (quotes Q-01 to Q-08) | 1: >= 200 / 3: 130 / 5: <= 70 | 20 |
| K4 | Lead time | Enhancing | fabrication days with the via option | 1: >= 10 / 3: 8 / 5: <= 5 | 10 |
| K5 | Assembly risk | Enhancing | solder voiding under the PA pad and the chance of a review flag | 2: unfilled via-in-pad under a window-pane paste pattern (F19 option b) / 5: filled and capped (F19 option a) | 20 |
| | | | | **Sum** | **100** |

Criteria considered (06 section 13 item 1): safety through M3 (HZ-003); first power-on through K5 (a voided PA joint is a first-power-on thermal risk); cost K3; schedule K4; performance margin K1 and K2. System security omitted: the board thickness adds no attack surface. The criterion "mechanical fit of through-hole pins and connector heights" was considered and dropped because it scores the same for every alternative. Pin protrusion differs by 0.6 mm, inside the 9.1 mm top zone.

### 3.2 Alternatives

| ID | Thickness | Via treatment | Source |
|---|---|---|---|
| T1 | 1.0 mm (current REQ-SYS-139 value, TBR) | Type VII resin fill and cap | F5, F15; ADR-007 |
| T2 | 1.6 mm | Type VII | F5 |
| T3 | 1.0 mm | unfilled vias, window-pane paste over the PA pad | export F19 option (b) |
| T4 | 1.2 mm | Type VII | F5 (standard stackup exists) |

The via array is not varied (0.30 mm, 0.65 mm pitch, 25 vias): it is the largest drill PCBWay tents and the densest pitch its rules allow (export F16). Heavier plating (35 um) is a quote question (email item 3(c)), not an alternative; it would lower every alternative's K1 equally.

**Panelization sub-decision:**

| ID | Form | Criteria (weights) |
|---|---|---|
| P1 | single board with two 5 mm tab-routed rails on the long edges, mouse bites, fiducials and tooling holes in the rails | P-a assembly acceptance (40): rails meet F19 whatever the edge copper; P-b layout freedom (30): no 3.5 mm keep-out on the long edges (about 11 % of the board); P-c depanel finish (15): the owner breaks the tabs and files the nubs, and the edges sit inside the case; P-d cost (15): about 16 % more panel area (Low) |
| P2 | single board, no rails, every part at least 3.5 mm from the long edges | as above |

### 3.3 Weight rationale

K1 has the largest weight, 35, because the via array is the second-largest resistance in the junction chain and the option C path has the least margin (TS-011 section 4). K3 cost and K5 assembly risk have 20 each: the owner put cost first, and a voided PA joint is a first-power-on failure that SI-010 weighs. K2 has 15 because stiffness is solvable by printed posts. K4 has 10 because fabrication runs in parallel with the parts import (`schedule.md`).

### 3.4 Evaluation methods

| Criterion | Method | Evidence |
|---|---|---|
| M1, M2, M4 | vendor capability data | F5, F6, F9, F15, F19 |
| M3, K1 | lumped thermal chain | `hardware/sim/enclosure/thermal_screen.py` (TS-004 line: 107.5 C at 1.0 mm, 111.6 C at 1.2 mm, 119.4 C at 1.6 mm) |
| K2 | beam deflection | `hardware/sim/enclosure/tolerance_stack.py` L3 |
| K3, K4 | author estimates, replaced by the instant quotes | owner-actions section 2.4 |
| K5 | vendor rule and AN4005 practice | export F14, F15, F19 |
| Totals, sensitivity | `hardware/sim/enclosure/trade_matrix.py` | `out/trade-matrix.txt` |

## 4. Scoring rationale

### 4.1 Mandatory screening

| Alternative | M1 | M2 | M3 (Tj at 45 C) | M4 | M5 | Result |
|---|---|---|---|---|---|---|
| T1 | pass (aspect 3.3) | pass | pass: 107.5 C | pass | pass (six bosses) | kept |
| T2 | pass (aspect 5.3) | pass | **fail**: 119.4 C | pass | pass | dropped |
| T3 | pass | pass | **fail**: 112.4 C (the screen's 107.5 C plus 4.1 W x 1.2 K/W of voiding, by hand) | conditional: an unfilled via-in-pad may be flagged at review (F19) | pass | dropped |
| T4 | pass | pass | **fail**: 111.6 C | pass | not in decision 87's rule (conditional) | dropped |

On the CNC fallback path (pedestal, 2.6 K/W) all four pass M3: 96.4 C at 1.0 mm and about 108 C at 1.6 mm. The board must serve both enclosures (TS-011), so the option C path decides. Section 6 item 3 runs the matrix with the screen relaxed.

### 4.2 Enhancing scores

| Criterion | T1 | T2 | T3 | T4 | Confidence and evidence |
|---|---|---|---|---|---|
| K1 | 5 (4.7 K/W) | 1 (7.6) | 2 (5.9 with voiding) | 2 (5.7) | M (F16); T3 L |
| K2 | 3 (two posts) | 5 (none: 0.19 mm) | 3 | 3 (0.44 mm, posts) | M (L3) |
| K3 | 3 (about USD 130 with Type VII) | 3 | 5 (about USD 70) | 3 | L: the F22 page price of USD 48 for a 100 x 100 mm 4-layer prototype, plus the Type VII surcharge (F15: 2.5 to 3 times the via cost, secondary source) |
| K4 | 3 (about 8 days) | 3 | 5 (about 5 days) | 3 | L: F21 (5 days, 4-layer advanced), F15 (+2 to 3 days) |
| K5 | 5 | 5 | 2 | 5 | M: F15, F19 |

Panelization: P1 = 5, 5, 3, 4; P2 = 3, 2, 5, 5 (P-a M, P-b H, P-c M, P-d L).

## 5. Final decision matrix

Surviving alternative T1 alone. The relaxed-screen matrix (all four) is shown so that the recommendation does not depend on the screen:

| Criterion | Weight | T1 | T2 | T3 | T4 |
|---|---|---|---|---|---|
| K1 | 35 | 175 | 35 | 70 | 70 |
| K2 | 15 | 45 | 75 | 45 | 45 |
| K3 | 20 | 60 | 60 | 100 | 60 |
| K4 | 10 | 30 | 30 | 50 | 30 |
| K5 | 20 | 100 | 100 | 40 | 100 |
| **Total** | **100** | **410 (82.0 %)** | 300 (60.0 %) | 305 (61.0 %) | 305 (61.0 %) |
| **Rank** | | 1 | 4 | 2 (tie) | 2 (tie) |

Panelization: P1 455 (91.0 %), P2 330 (66.0 %).

## 6. Uncertainty and sensitivity statement

1. **Weight sensitivity:** no single +10 or -10 weight change moves the top rank of either matrix (`trade_matrix.py`).
2. **Score sensitivity:** no single Low-confidence cell moved by +1 or -1 moves the top rank of either matrix.
3. **Assumptions and their evidence:**
   - PA dissipation 4.1 W and RthJC 3 C/W (TS-001).
   - Via figures from F16 at a 25 um wall.
   - The option C heatsink at 5.5 K/W in situ (TS-011, Low). If WP-PDR-28 or the heatsink datasheet finds more margin, T2 could pass M3, and it still ranks last in the relaxed matrix.
   - Cost and lead-time estimates until the quotes.
   - FR-4 modulus 22 GPa (Low).
4. **Robustness verdict:** Robust.
5. **Value of information:** not required by the verdict. The instant quotes Q-01 to Q-08 are expected by 09-30 (OD-04) and will be entered before the F0 freeze; they can change K3 and K4 by one step, which section 6 item 2 shows does not change the rank.
6. **Limitations of the methods and tools:**
   - The thermal chain is the lumped screen of TS-011, developer evidence, superseded by WP-PDR-28.
   - The voiding penalty for T3 is an estimate from AN4005's 20 % voiding figure.
   - The stiffness model is a simply supported beam, not a plate.
   - No vendor quote exists yet.

## 7. Risks and benefits

| Alternative | Risk statement | L | C (driving dimension) | Score / band | Would be entered as |
|---|---|---|---|---|---|
| T1 | Given a 1.0 mm board and board-mounted buttons, there is a possibility that a button press flexes the board and cracks a nearby joint, adversely impacting first power-on reliability, leading to rework | 2 | 2 (first power-on) | 4 Green | not entered; the support-post rule mitigates it |
| T1 | Given the Type VII surcharge is unpublished (F15), there is a possibility that it exceeds the estimate by more than USD 100, adversely impacting cost | 2 | 2 (cost) | 4 Green | RSK-052 (quote) |
| P1 | Given tab-routed rails, there is a possibility of edge nubs that bind the board in the case pocket, adversely impacting assembly | 2 | 1 (performance margin) | 2 Green | not entered; 2.0 mm pocket clearance (S7) |

| Alternative | Benefits beyond the scored criteria |
|---|---|
| T1 | Thinner stack leaves 0.6 mm more in the top zone; a lighter board (about 9 g less than 1.6 mm: 8060 mm2 x 0.6 mm x 1.85 g/cm3) |
| P1 | PCBWay handles the board on any edge-copper layout; fiducials and tooling holes off the board |

## 8. Recommendation

- **Recommended:** T1, 1.0 mm with Type VII via-in-pad under the PA and QFN exposed pads, on a single 130 x 62 mm board with two 5 mm tab-routed rails (P1). Total 410 (82 %), robust.
- **Rationale:** T1 is the only thickness at which the option C heat path meets REQ-SYS-112. It also has the lowest via-array resistance and no assembly flag. Decision 87's four-boss condition is met with six bosses.
- **Impacts:**
  - REQ-SYS-139 value 1.0 mm (TBR closed at PDR).
  - The PCBWay order carries "Via in pad" and "All vias filled with resin and capped" (quote rows Q-06 and Q-08).
  - Two printed support posts under the buttons (`board-outline.json`).
  - WP-PDR-37 lays out on the outline with the rails added by PCBWay or in the panel file.
  - Cost from the quote (WP-PDR-46); schedule impact +2 to 3 days of fabrication inside the parts-import window (none on the critical path).
- **Corrective action if adopted late:** none needed. 1.0 mm is the current REQ-SYS-139 value and the layout starts on it.

**Proposed values:** REQ-SYS-139: 1.0 mm (TBR closed). TS-004 has no other TBR.

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

- SE HB section 6.8 and Table 6.8-1 (corpus `22-6-8-decision-analysis.md`); `docs/process/06-risk-and-decision-analysis.md` sections 13, 14, 16.
- `docs/research/pcbway-fabrication-and-assembly.md` F5, F6, F9, F15, F19 to F22; `docs/research/pcbway-export-and-vendor-questions.md` F14 to F19.
- `docs/decisions/trade-studies/TS-011-enclosure.md`; `docs/design/analysis/mechanical-tolerance-stack.md`; `hardware/enclosure/board-outline.json`.
- `docs/reviews/PDR/owner-actions.md` section 2.4 (quote rows). Its line 188 names this study under WP-PDR-26; TS-004 belongs to WP-PDR-27 (plan section 3.6), a cross item returned to the owner-actions author.

## Appendix A. Supporting analysis

- **Search:** Claude Context queries on 2026-09-27 ("PCBWay 4-layer board thickness 1.0 mm 1.6 mm via fill Type VII panel rails", "design reader report items enclosure board thickness TS-004 via fill panelization four bosses decision 87").
- **Detailed analysis:** `hardware/sim/enclosure/thermal_screen.py` (TS-004 line), `tolerance_stack.py` (L3), `trade_matrix.py`; figure `docs/reviews/PDR/figures/ts011-thermal-screen.png` (footer carries the TS-004 junction figures).
- **Decision metrics:** opened and drafted 2026-09-27; four thickness and via alternatives, three dropped at M3; two panel alternatives.

## Change log

| Revision | Date | Change | Reason |
|---|---|---|---|
| 0 | 2026-09-27 | Initial draft, wave 1a | WP-PDR-27 |
