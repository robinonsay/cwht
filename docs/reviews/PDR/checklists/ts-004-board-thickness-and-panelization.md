---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md section 13;
# docs/process/06-risk-and-decision-analysis.md sections 14.3 step 6 and 16). Independent review of TS-004
# with docs/templates/peer-review-checklist-risk.md section B (PDR work plan WP-PDR-27, record path as the
# plan names it). Iteration 1 at freeze F0 (rule C2, freeze commit 70a3a33).
# Iteration 2 (delta, rules C1 and C2) at main e2d3226: one product blob drifted after the freeze,
# hardware/enclosure/board-outline.json 27dbacc7 -> d7977cf3 (commits 70d11ef and 433a944, TS-011
# revisions 1 and 2). The other six blobs are unchanged. Every blob below is on main; none is branch-only.
id: INSP-082
checklist: peer-review-checklist-risk
checklist_revision: A
checklist_file: docs/reviews/PDR/checklists/ts-004-board-thickness-and-panelization.md
product: docs/decisions/trade-studies/TS-004-board-thickness-and-panelization.md
product_commit: "e2d3226"
product_blob: 03eb004d28ec84b9419fc43d1efc6ad7374c1393
product_files: ["docs/decisions/trade-studies/TS-004-board-thickness-and-panelization.md@03eb004d28ec84b9419fc43d1efc6ad7374c1393", "hardware/sim/enclosure/thermal_screen.py@78892ca27ace63c1bbd5965b730b0ccd6e85ab53", "hardware/sim/enclosure/tolerance_stack.py@376e403c255c8cffcb4694e8160394f3a158a07b", "hardware/sim/enclosure/trade_matrix.py@c76b0f70d05a64c282a9066204a64ffe1e217fde", "hardware/sim/enclosure/out/trade-matrix.txt@c6023d697716d2c024c0033948aaeaa3aa3b7c0e", "hardware/enclosure/board-outline.json@d7977cf385e8f76af8ad098497333b2f606cf1f8", "docs/reviews/PDR/figures/ts011-thermal-screen.png@47d81e61ee7039b3126158c577170af30686752a"]
product_size: 4 thickness and via alternatives (T1 to T4; T2 to T4 dropped at M3) and 2 panel forms; 5 mandatory and 5 enhancing criteria, panel sub-decision 4 criteria
sprint: PDR-prep
author_agent: "author:WP-PDR-27 wave 1a (Claude as ME designer)"
reviewer_agent: "reviewer:WP-PDR-27-ts-004-iter2 (delta; independent; authored no part of WP-PDR-27 or of TS-011 revisions 1 and 2)"
# criticality: the study sets the board thickness and via treatment inside the heat path whose node and
# sensor TS-011 selects; it selects no 07 section 14.1 component, sensor or threshold (lead SE may overrule)
criticality: neither
assurance_required: false
assurance_reviewer_agent: none
iteration: 2
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
effort_turns: 32
effort_minutes: 50
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

## Iteration 2: delta on the drifted blob (2026-09-27, main HEAD `e2d3226`)

**Scope (rules C1 and C2).** Iteration 1 was APPROVED with no Major finding, so this delta verifies only that the product set still supports the record after the one blob that changed since the freeze. `git rev-parse HEAD:<path>` and `git hash-object <path>` at `e2d3226` equal each other for all 7 product files. Six equal their iteration 1 blobs. `hardware/enclosure/board-outline.json` moved from `27dbacc7` (the `70a3a33` draft) to `d7977cf3` through `70d11ef` (TS-011 revision 1) and `433a944` (TS-011 revision 2). The old blob survives only on the stale `cr/CR-014` branch; the new one is on main, so the record verdict is not held under the lead SE convention. The TS-004 study itself (`03eb004d`) did not change.

**Independence and search.** This invocation authored no part of WP-PDR-27, TS-004 or TS-011 revisions 1 and 2, and edited no product file. `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` (delta iteration practice, record drift rule) ran before any `grep`; `grep` afterwards only pinned lines in known paths (the plan rules C1 and C2, TS-004 references to the outline, the validator). The rustos tree was not read.

**Hunks read (`git diff 27dbacc7 d7977cf3`, 100 insertions, 9 deletions, 9 hunks), each against the TS-004 lens:**

| Hunk | Change | Effect on TS-004 |
|---|---|---|
| 1 `revision` | 0 to 2, TS-011 revision 2 jack features | None |
| 2 `sources` | adds `board_field_thermal.py` and `drop_and_axial.py` | None |
| 3 `mounting` | adds `boss_gussets` and six `front_shell_posts` (6 mm, top side, copper-free pads) | None. `board.thickness` 1.0, `board.outline` 130 x 62, `board.panelization` (two 5 mm tab-routed rails) and the six `mounting.holes` are unchanged, so M5 (decision 87, six bosses) and P1 still hold. The front-shell posts bear on the board top against a front-face drop; the K2 criterion is button-press deflection toward the back, carried by the unchanged `support_posts` (count 2, basis TS-004 L3), so K2 and its scores are unchanged |
| 4 `keepouts_top` | adds post pads and the NTC-1 and NTC-2 3 x 3 mm keepouts | None. The sensors sit on the top copper of the PA thermal pad; the Type VII filled and capped via array of T1 leaves that surface plated flat, so nothing in the via-fill choice conflicts |
| 5 `heatsink` | in-situ maximum 5.5 to 6.11 K/W; 5.5 kept as `in_situ_thermal_resistance_design_point_k_per_w`; catalog limit 4.28 K/W; guard slot and rib widths | Consistent with M3. TS-004 M3 screens at 5.5 K/W, now the design point. The 6.11 K/W maximum is the T1 threshold: chain 9.74 K/W below the heat sink (which includes the 1.0 mm via array, 4.7 K/W), and 45 + 4.1 x (9.74 + 6.11) = 110.0 C; 45 + 4.1 x (9.74 + 5.5) = 107.5 C, equal to TS-004 M3 for T1. T2 adds 2.9 K/W and still fails M3 anywhere in the range. This quantifies the direction finding-1 asks TS-004 to state; it does not close finding-1, because TS-004 section 6 is unchanged |
| 6 `port_block` | adds a 20 x 20 x 2 mm inner flange | None |
| 7, 8 `end_faces.minus_x` | jack collars, gasket ring, filtering rule; USB shroud | None (end-wall features off the board) |
| 9 new `thermal_sensors`, `case_filament` | NTC placement rule 14; PC-class filament rule 15 | None on thickness, via fill or panel form. The filament rule concerns M8 of TS-011, not a TS-004 criterion |

**Reproduction.** On main at `e2d3226`: `trade_matrix.py --check`, `thermal_screen.py --check` and `tolerance_stack.py --check` each exit 0; none of the three reads `board-outline.json`, and `git status` shows no tracked output change afterwards.

**Visual closure.** No render changed (`ts011-thermal-screen.png` still `47d81e61`, inspected at iteration 1); no render is needed for this delta.

### Findings (iteration 2; current state of every finding of this record)

| Finding | Severity | State | Disposition |
|---|---|---|---|
| finding-1 | Minor | Open | Unchanged: TS-004 section 6 still states only the favourable direction. The outline now carries the 6.11 K/W T1 threshold, which is the number the fix sentence should cite. Lien due the CDR readiness declaration under rule C1 if not fixed before the TS-004 re-issue of cross item X-1 |
| finding-2 | Minor | Open | Unchanged: K5 anchors and the K2 to K4 interpolation rule not stated. Lien as finding-1 |

No new finding. No Major finding.

### Record verdict (iteration 2)

`reviewer_verdict: APPROVED` and `verdict: APPROVED`: zero Major findings, two Minor findings open as liens (rule C1), readiness met, and every blob of `product_files` equals `git rev-parse HEAD:<path>` on main. Cross item X-1 stands (the design-to-cost pivot of the status note will re-plan TS-004; any re-issue is a new delta iteration of this record under rule C2).

### Commands (iteration 2)

- `git rev-parse HEAD:<path>` and `git hash-object <path>` at `e2d3226` for the 7 product files: equal; one changed blob (`d7977cf3`).
- `git log --oneline 70a3a33..HEAD -- hardware/enclosure/board-outline.json`: `70d11ef`, `433a944`.
- `git diff 27dbacc7 d7977cf3`: 9 hunks, all read.
- The three enclosure checkers `--check`: exit 0.
- `.venv/bin/python tools/validate_docs.py`: this record passes (see return).

### Measurements (SWE-089, iteration 2)

Blobs re-checked 7; drifted 1; hunks read 9; new findings 0; open Minor 2 (liens); renders inspected 0 (none changed); effort about 12 turns and 20 minutes; cumulative 32 turns and 50 minutes.
