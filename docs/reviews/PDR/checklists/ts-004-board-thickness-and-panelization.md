---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md section 13;
# docs/process/06-risk-and-decision-analysis.md sections 14.3 step 6 and 16). Independent review of TS-004
# with docs/templates/peer-review-checklist-risk.md section B (PDR work plan WP-PDR-27, record path as the
# plan names it). Iteration 1 at freeze F0 (rule C2, freeze commit 70a3a33).
id: INSP-082
checklist: peer-review-checklist-risk
checklist_revision: A
checklist_file: docs/reviews/PDR/checklists/ts-004-board-thickness-and-panelization.md
product: docs/decisions/trade-studies/TS-004-board-thickness-and-panelization.md
product_commit: "70a3a33"
product_blob: 03eb004d28ec84b9419fc43d1efc6ad7374c1393
product_files: ["docs/decisions/trade-studies/TS-004-board-thickness-and-panelization.md@03eb004d28ec84b9419fc43d1efc6ad7374c1393", "hardware/sim/enclosure/thermal_screen.py@78892ca27ace63c1bbd5965b730b0ccd6e85ab53", "hardware/sim/enclosure/tolerance_stack.py@376e403c255c8cffcb4694e8160394f3a158a07b", "hardware/sim/enclosure/trade_matrix.py@c76b0f70d05a64c282a9066204a64ffe1e217fde", "hardware/sim/enclosure/out/trade-matrix.txt@c6023d697716d2c024c0033948aaeaa3aa3b7c0e", "hardware/enclosure/board-outline.json@27dbacc7dda7f79e6cba3234ee77f6453e304906", "docs/reviews/PDR/figures/ts011-thermal-screen.png@47d81e61ee7039b3126158c577170af30686752a"]
product_size: 4 thickness and via alternatives (T1 to T4; T2 to T4 dropped at M3) and 2 panel forms; 5 mandatory and 5 enhancing criteria, panel sub-decision 4 criteria
sprint: PDR-prep
author_agent: "author:WP-PDR-27 wave 1a (Claude as ME designer)"
reviewer_agent: "reviewer:WP-PDR-27-ts-004-iter1 (independent; authored no part of WP-PDR-27)"
# criticality: the study sets the board thickness and via treatment inside the heat path whose node and
# sensor TS-011 selects; it selects no 07 section 14.1 component, sensor or threshold (lead SE may overrule)
criticality: neither
assurance_required: false
assurance_reviewer_agent: none
iteration: 1
readiness_met: true
reviewer_verdict: APPROVED
assurance_verdict: not-required
verdict: APPROVED
findings_major: 0
findings_minor: 2
findings_open: 2
findings_fixed: 0
findings_verified: 0
findings_deferred: 0
deferred_rids: []
items_no: []
effort_turns: 20
effort_minutes: 30
record_status: Open
date: 2026-09-27
date_closed: null
---

# Peer review record: TS-004 board thickness, via fill and panelization (INSP-082, iteration 1)

**Product:** `docs/decisions/trade-studies/TS-004-board-thickness-and-panelization.md` blob `03eb004d` at freeze commit `70a3a33` (freeze F0, rule C2), with the files it scores from: `thermal_screen.py` (`78892ca2`, TS-004 line), `tolerance_stack.py` (`376e403c`, L3), `trade_matrix.py` (`c76b0f70`) and its output `trade-matrix.txt` (`c6023d69`), `board-outline.json` (`27dbacc7`) and the figure `ts011-thermal-screen.png` (`47d81e61`, footer carries the TS-004 figures). Every blob equals `git rev-parse HEAD:<path>` and `git hash-object <path>` at `HEAD` `4ef04ee` on 2026-09-27. No product blob lives on a `cr/` branch. The study is AT RISK on CR-003 revision 3 and CR-006 revision 2 (header Status), both Submitted.

**Checklist:** `docs/templates/peer-review-checklist-risk.md` revision A, section B (CK-RSK-B1 to B10). Section A is N/A.

**Acceptance criteria (rule C7):**
- 06 section 14.3 steps 1 to 5 and template sections 1 to 9 filled; section 10 empty.
- 06 section 13 item 1: the six consequence dimensions used or omitted with a reason.
- 06 section 14.4 items 1 to 5 for both matrices: weight +/-10 on each of the 5 thickness criteria and 4 panel criteria (18 runs); +/-1 on every Low cell; verdict; value of information; limitations.
- SRR decision 87 as the REQ-SYS-139 `tbr.plan` states it ("1.0 mm if the enclosure gives four bosses, else 1.6 mm; TS-004 at PDR decides from the boss layout and the quotes").
- Plan WP-PDR-27 output: "TS-004 with ADR-039"; the thickness, via fill and panel form handed to WP-PDR-37 (outline); REQ-SYS-139 value proposed (G11).

**Search rule.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` (SRR decision 87, REQ-SYS-139, PCBWay via fill, risk checklist section B) preceded every `grep`. The rustos tree was not read.

## Findings (iteration 1)

| Finding | Severity | Item | Location | Description | State | Deferred to |
|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | Minor | CK-RSK-B7 | TS-004 section 6 item 3 (third assumption) and item 4 | The mandatory screen M3 uses the TS-011 option C heat sink at 5.5 K/W in situ (Low). The study states only the favourable direction ("if WP-PDR-28 ... finds more margin, T2 could pass M3"). The other direction is the one INSP-081 finding-1 raises: above 6.11 K/W, T1 also fails M3 on the option C path and no alternative survives the screen. The recommendation does not change, because T1 has the lowest junction temperature of the four under any heat-sink value and leads the relaxed matrix by 105 points. The robustness statement should say that T1 is chosen under either outcome and that a failed M3 goes back to TS-011, not to TS-004 | Open | |
| <a id="finding-2"></a>finding-2 | Minor | CK-RSK-B2 | TS-004 section 3.1, K5 scale "2: unfilled ... / 5: filled and capped"; K2, K3, K4 scales (1 / 3 / 5) | K5 has anchors only at 2 and 5, so scores 1, 3 and 4 have no meaning, and the study gives no interpolation rule for scores 2 and 4 of K2 to K4 (TS-011 line 71 and TS-001 section 3.1 state theirs). No cell uses an undefined score (T1 to T4 score 2 or 5 on K5, and 1, 3 or 5 elsewhere, except K1, whose anchors cover 1 to 5), so no total changes. Fix: state K5 as a two-level criterion (2 or 5) with the reason, and add the interpolation sentence | Open | |

No Major finding. The recommendation (T1 and P1) follows from the evaluation, and the sensitivity statement is complete for the enhancing criteria.

## Readiness criteria

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | `validate_docs.py` exits 0 on this record | Yes | Run with this record at `4ef04ee` (see Commands) |
| R2 | Section A only | N/A | The product is a trade study |
| R3 | Sections 1 to 9 filled, section 10 empty | Yes | TS-004 sections 1 to 9 filled; section 10 fields empty |
| R4 | Author's return names the decision need and gate | Yes | Author summary: "1.0 mm board with Type VII via-in-pad and two 5 mm tab-routed rails, 410 of 500, robust"; header "Decide by: PDR (B1b, OD-10)" |

## B. Trade study (06 section 16, items 1 to 10)

| Id | Answer | Evidence |
|---|---|---|
| CK-RSK-B1 | Yes | Header: 06 section 14.1 class 1 item (c) (HZ-003 through the via array), and the study named in `docs/design/concept.md` section 11.2; decision maker Robin; gate PDR, B1b |
| CK-RSK-B2 | Yes | Section 3.1: K1 to K5 each with an operational definition and scale; M1 to M5 pass or fail. "Criteria considered": safety M3 (HZ-003), first power-on K5, cost K3, schedule K4, performance margin K1 and K2, system security omitted with a reason; one criterion considered and dropped (pin fit, same for all, 0.6 mm inside the 9.1 mm zone). Anchor gap: finding-2 |
| CK-RSK-B3 | Yes | 35 + 15 + 20 + 10 + 20 = 100; panel 40 + 30 + 15 + 15 = 100; integers; rationale section 3.3 (K1 largest because the via array is the second-largest resistance in the chain; K3 and K5 at 20 from the owner's cost priority and SI-010) |
| CK-RSK-B4 | Yes | T1 is the current REQ-SYS-139 value (the baseline alternative); T2 1.6 mm, T3 unfilled vias with window-pane paste, T4 1.2 mm; the via array geometry and 35 um plating are explained as not varied (fixed by PCBWay rules, or a quote question that shifts all equally); panel P1 and P2 |
| CK-RSK-B5 | Yes | Every cell has a value, score, confidence and evidence (section 4.2): K1 4.7 / 7.6 / 5.9 / 5.7 K/W scored 5 / 1 / 2 / 2 on the anchors (5.9 and 5.7 are above 5.6 and at most 6.6); K2 from L3 (re-checked below); K3 and K4 Low with the F15, F21, F22 basis; K5 M from F15, F19. Mandatory cells: T2 119.4 C, T4 111.6 C, T3 112.4 C (107.5 + 4.1 x 1.2), all over 110 C; T4 also outside decision 87 (conditional); T3 conditional on M4 |
| CK-RSK-B6 | Yes | Recomputed by hand: T1 = 175 + 45 + 60 + 30 + 100 = 410; T2 = 35 + 75 + 60 + 30 + 100 = 300; T3 = 70 + 45 + 100 + 50 + 40 = 305; T4 = 70 + 45 + 60 + 30 + 100 = 305. P1 = 200 + 150 + 45 + 60 = 455; P2 = 120 + 60 + 75 + 75 = 330. Equal to section 5 and to `trade_matrix.py` |
| CK-RSK-B7 | Yes | Section 6 items 1 to 6 follow 06 section 14.4: weight runs and Low-cell runs for both matrices, none changes the rank (re-run output "perturbations that change the top rank: none" for both); verdict Robust; value of information "not required by the verdict", with the quotes named; limitations (lumped chain, voiding estimate, beam model, no quote). The mandatory-screen direction is incomplete: finding-1 (Minor, as it cannot change the choice) |
| CK-RSK-B8 | Yes | Section 7: three risks in the four-part format (2 x 2 = 4 Green, 2 x 2 = 4 Green, 2 x 1 = 2 Green, correct on the 06 section 8 table), with register routing (RSK-052) or the mitigation that makes an entry unnecessary |
| CK-RSK-B9 | Yes | T1 is the only survivor of the mandatory screen and the highest total of the relaxed matrix (410 against 305); P1 is the highest panel total (455 against 330) |
| CK-RSK-B10 | Yes | Section 9 "None recorded"; section 10 fields empty. No reviewer dissent |

## Independent checks (evidence for B5 to B7)

- **Via array.** F16 of `docs/research/pcbway-export-and-vendor-questions.md` gives 4.7 K/W at 1.0 mm and 7.6 K/W at 1.6 mm (25 vias, 0.30 mm, 25 um); the 1.2 mm value 5.7 K/W is scaled by barrel length (4.7 x 1.2 = 5.64, rounded up, conservative). Aspect ratios 1.0 / 0.30 = 3.3 and 1.6 / 0.30 = 5.3, under 8.
- **Junction.** 107.5 + 4.1 x (5.7 - 4.7) = 111.6 C; 107.5 + 4.1 x (7.6 - 4.7) = 119.4 C; CNC path 96.4 + 11.9 = 108.3 C at 1.6 mm ("about 108"). Equal to the study and the thermal screen output.
- **Stiffness (L3).** Simply supported beam, b = 62 mm, E = 22 GPa, 10 N: 1.0 mm gives I = 62 x 1^3 / 12 = 5.17 mm^4 and d = 10 x 120^3 / (48 x 22 000 x 5.17) = 3.17 mm; across 74.5 mm, 0.76 mm; 1.6 mm across 74.5 mm, 0.19 mm. Equal to `tolerance_stack.py`. The full-width beam is not conservative for a point press (limitation stated as "not a plate").
- **Mass benefit.** 130 x 62 = 8060 mm^2 x 0.6 mm x 1.85 g/cm^3 = 8.9 g ("about 9 g").
- **Decision 87 and CR-003.** REQ-SYS-139 `tbr.plan` (read from `requirements.json`) and CR-003 line 157 ("Decision 87's rule is construction-neutral and stands as written") agree with the M5 reading; six bosses in `board-outline.json` `mounting.holes`.
- **Reproduction.** Scratchpad export of `70a3a33`: `trade_matrix.py --check`, `thermal_screen.py --check`, `tolerance_stack.py --check` each exit 0, outputs byte-identical to the frozen blobs.

## Visual closure

`docs/reviews/PDR/figures/ts011-thermal-screen.png` opened with the Read tool (1 render): the footer "TS-004 (C1 path): Tj = 107.5 C at 1.0 mm, 111.6 C at 1.2 mm, 119.4 C at 1.6 mm" agrees with the study section 3.4.

## Items N/A

CK-RSK-A1 to CK-RSK-A11 and readiness R2 (the product is a trade study).

## Cross items for the lead SE (not findings on TS-004)

- **X-1.** Status note 2026-09-27 sections 6 to 8 (commits `4ef04ee` and `96dcca9`, after the freeze; section 8 supersedes section 6 where they differ): the board becomes a JLCPCB bare board soldered by the owner with an iron and a heat gun, parts with a hidden exposed thermal pad are flagged, and the radio costs under USD 200 all in. M1 and M4 (PCBWay capability and turnkey assembly acceptance), K3 to K5 and the Type VII via-in-pad order option assume PCBWay fabrication and turnkey SMT assembly, and a filled, capped via-in-pad under a PA pad soldered by hand with a heat gun is a different assembly-risk case. These are later owner inputs, not defects of the frozen study, so no finding; TS-004 iterates under rule C8. The statement in section 6 item 5 that the quotes "will be entered before the F0 freeze" is stale at this freeze: any value entered now is a delta iteration of this record (rule C2).
- **X-2.** TS-004 section 11 notes that `docs/reviews/PDR/owner-actions.md` line 188 names this study under WP-PDR-26; that is for the owner-actions author.

## Commands

- `git rev-parse HEAD:<path>` and `git hash-object <path>` at `4ef04ee` for the 7 product files: equal to the blobs above.
- Scratchpad export of `70a3a33`: the three checkers exit 0 (`CHECK PASS`).
- `.venv/bin/python tools/validate_docs.py`: this record passes.

## Measurements (SWE-089)

Items checked 10 (section B) plus readiness 4; items answered No 0; findings 0 Major, 2 Minor; fixed 0, deferred 0; iteration 1; renders inspected 1; effort about 20 turns and 30 minutes (session shared with INSP-081, 073, 074).
