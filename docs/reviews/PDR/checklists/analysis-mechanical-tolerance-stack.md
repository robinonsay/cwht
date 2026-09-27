---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md section 13;
# docs/process/08-agent-briefing.md sections 3.4 and 3.5). Independent review of the WP-PDR-27 tolerance
# stack, load path, drop and drip analysis note, record path as PDR work plan WP-PDR-27 names it. Iteration 1
# at freeze F0 (rule C2, freeze commit 70a3a33).
# Checklist applied: docs/templates/peer-review-checklist-analysis.md revision A as on its CR-012 branch
# (cr/CR-012-pdr-checklist-templates at 7784672, blob 0386cc6e; CR-012 Submitted, not merged).
# tools/validate_docs.py requires the checklist field to name a template that exists on main, so the field
# names peer-review-checklist-design revision B (section J, enclosure) and checklist_analysis records the
# template actually applied, as INSP-056 did. The delta iteration after CR-012 merges switches the field.
id: INSP-084
checklist: peer-review-checklist-design
checklist_revision: B
checklist_analysis: "docs/templates/peer-review-checklist-analysis.md@0386cc6e78da65578b1cce8b2f793cd3db224921 (revision A, CR-012 branch head 7784672)"
checklist_file: docs/reviews/PDR/checklists/analysis-mechanical-tolerance-stack.md
product: docs/design/analysis/mechanical-tolerance-stack.md
# product_commit (iteration 3, delta): 433a944, the WP-PDR-27 shielding revision 2 commit that changed
# board-outline.json 9d4d36a9 to d7977cf3 (jack feature text only). Every blob below equals git rev-parse
# 433a944:<path>, HEAD:<path> and git hash-object at HEAD e2d3226; all are on main. product_files_iteration_2 keeps
# the 70d11ef blobs; product_files_iteration_1 keeps the 70a3a33 blobs.
product_commit: "433a944f9489505ced8fefabfeeab156bdf76e0c"
product_files: ["docs/design/analysis/mechanical-tolerance-stack.md@b31768da93013553dadf9d076cde850e1e2ed2e3", "hardware/sim/enclosure/tolerance_stack.py@376e403c255c8cffcb4694e8160394f3a158a07b", "hardware/sim/enclosure/drop_and_axial.py@3513caaa66caac267aa905fd54a19949eb66ea92", "hardware/sim/enclosure/envelope_drawing.py@5de2223bfedb3d45734cf066eeccf3df28629b0a", "hardware/enclosure/board-outline.json@d7977cf385e8f76af8ad098497333b2f606cf1f8", "hardware/sim/enclosure/out/tolerance-stack.csv@3e17c2097f3fcc3fdb3f24b50713622c3da8dd2f", "hardware/sim/enclosure/out/drop-and-axial.csv@91d97bf4a8923ab2af48037cefbeb3dccba848b5", "docs/reviews/PDR/figures/tolerance-stack.png@2ee6e410cec881db08c928d37b590d785d559c04", "docs/reviews/PDR/figures/drop-and-axial.png@0f68e1063c0c94573bd2d4fad0c3392035dc9386", "docs/reviews/PDR/figures/board-outline-envelope.png@a2c08e0ef04ec036465ddeb9bd2f6a16d7fb5dfe"]
product_files_iteration_2: ["docs/design/analysis/mechanical-tolerance-stack.md@b31768da93013553dadf9d076cde850e1e2ed2e3", "hardware/sim/enclosure/tolerance_stack.py@376e403c255c8cffcb4694e8160394f3a158a07b", "hardware/sim/enclosure/drop_and_axial.py@3513caaa66caac267aa905fd54a19949eb66ea92", "hardware/sim/enclosure/envelope_drawing.py@5de2223bfedb3d45734cf066eeccf3df28629b0a", "hardware/enclosure/board-outline.json@9d4d36a984b07456a4860c6f1d6354297b42808d", "hardware/sim/enclosure/out/tolerance-stack.csv@3e17c2097f3fcc3fdb3f24b50713622c3da8dd2f", "hardware/sim/enclosure/out/drop-and-axial.csv@91d97bf4a8923ab2af48037cefbeb3dccba848b5", "docs/reviews/PDR/figures/tolerance-stack.png@2ee6e410cec881db08c928d37b590d785d559c04", "docs/reviews/PDR/figures/drop-and-axial.png@0f68e1063c0c94573bd2d4fad0c3392035dc9386", "docs/reviews/PDR/figures/board-outline-envelope.png@a2c08e0ef04ec036465ddeb9bd2f6a16d7fb5dfe"]
product_files_iteration_1: ["docs/design/analysis/mechanical-tolerance-stack.md@78409153455c926873119ef8a981ea688bd4d453", "hardware/sim/enclosure/tolerance_stack.py@376e403c255c8cffcb4694e8160394f3a158a07b", "hardware/sim/enclosure/envelope_drawing.py@20815e7581c34c9498e6c8d3972cc738e5c63e8a", "hardware/enclosure/board-outline.json@27dbacc7dda7f79e6cba3234ee77f6453e304906", "hardware/sim/enclosure/out/tolerance-stack.csv@3e17c2097f3fcc3fdb3f24b50713622c3da8dd2f", "docs/reviews/PDR/figures/tolerance-stack.png@2ee6e410cec881db08c928d37b590d785d559c04", "docs/reviews/PDR/figures/board-outline-envelope.png@ff8aa6c2befd4660f2bf353893ab5673d24f79e3"]
analysis_kind: [worst-case, other]
product_size: 13 stacks (S1 to S9 with variants), 3 load checks (L1 to L3), 6 envelope checks (E1 to E6), 2 checkers, 1 data file, 2 plots
tools_used: ["venv Python 3.13.5 (TV-001 accredits the interpreter; numpy and matplotlib class B without a TV record; no TV record covers hardware/sim/enclosure/*.py; developer evidence per 05 section 9.1)"]
values_proposed: ["REQ-SYS-105: 1 dB return-loss change (keep; tbr.plan step not executed: finding-2)", "REQ-SYS-107: 20 mm and 10 mohm (keep; 10 mohm not computed: finding-2)", "REQ-SYS-116: 1.0 m (keep; per face with the antenna fitted, rows D1 to D20, rules 6 and 17 to 20: supported at iteration 2)", "REQ-SYS-117: IPX2 (keep; finding-4)", "REQ-SYS-168: 4 mm and 25 mm (keep; supported by the sliding-door design rule)"]
renders_inspected: 4
sprint: PDR-prep
author_agent: "author:WP-PDR-27 wave 1a (Claude as ME designer)"
reviewer_agent: "reviewer:WP-PDR-27-analysis-tolerance-iter1 (independent; authored no part of WP-PDR-27); iteration 2 by reviewer:WP-PDR-27-analysis-tolerance-iter2 (independent; authored no part of WP-PDR-27 and no part of its revision 1); iteration 3 (drift delta) by reviewer:WP-PDR-27-analysis-tolerance-iter3 (independent; authored no part of WP-PDR-27, of its revision 1 or of the shielding revision 2)"
criticality: neither
assurance_required: false
assurance_reviewer_agent: none
iteration: 3
readiness_met: true
# reviewer_verdict (iteration 3, drift delta): APPROVED; finding-1 (Major) Verified at iteration 2; findings 2 to 7
# and the new finding-8 are Minor and Open (liens due at the CDR readiness declaration, plan rule C1)
reviewer_verdict: APPROVED
assurance_verdict: not-required
# verdict (iteration 3): still held at NEEDS CHANGES (CR-012 not merged at e2d3226). No SA pair is required. The applied analysis template is still only on cr/CR-012
# (blob 0386cc6e), so, per the lead SE convention of 2026-09-27, the record verdict is set to APPROVED in the
# CR-012 merge commit (or the commit right after it) if that blob is unchanged
verdict: NEEDS CHANGES
findings_major: 1
findings_minor: 7
findings_open: 7
findings_fixed: 0
findings_verified: 1
findings_deferred: 0
assurance_tasks_applied: []
deferred_rids: []
items_no: [CK-ANA-B1, CK-ANA-D3, CK-ANA-E3, CK-ANA-E5, CK-ANA-F1]
effort_turns: 67
effort_minutes: 100
record_status: Open
date: 2026-09-27
date_closed: null
---

# Peer review record: mechanical tolerance stack, load path, drop and drip (INSP-084, iteration 1)

**Product:** `docs/design/analysis/mechanical-tolerance-stack.md` (`78409153`) with `hardware/sim/enclosure/tolerance_stack.py` (`376e403c`), `envelope_drawing.py` (`20815e75`), the data file `hardware/enclosure/board-outline.json` (`27dbacc7`), the output `out/tolerance-stack.csv` (`3e17c209`) and the figures `tolerance-stack.png` (`2ee6e410`) and `board-outline-envelope.png` (`ff8aa6c2`), at freeze commit `70a3a33` (rule C2). Every blob equals `git rev-parse HEAD:<path>` and `git hash-object <path>` at `HEAD` `4ef04ee` on 2026-09-27. No product blob lives on a `cr/` branch. AT RISK on CR-003 revision 3 and CR-006 revision 2 (header Status).

**Checklist:** the item set of `peer-review-checklist-analysis.md` revision A (CR-012 branch, blob `0386cc6e`). `analysis_kind` worst-case (tolerance stacks) and other (load, drop, drip, envelope): sections A to F, G7, H, I. G1 to G6 and J are N/A.

**Acceptance criteria (rule C7, every case the governing clauses enumerate):**
- REQ-SYS-105: "4.0 N m antenna-port bending moment in any direction without jack rotation and within 1 dB (TBR) return-loss change"; `tbr.plan`: "The enclosure analysis at PDR confirms the return-loss limit with the NanoVNA repeatability".
- REQ-SYS-107: "within 20 mm (TBR) of the antenna port with at most 10 mohm (TBR) to the connector shell".
- REQ-SYS-108: "fully seated mating plugs at the key jack, headphone jack and micro-USB receptacle through its enclosure openings" (three plugs).
- REQ-SYS-110: "every external edge and cutout edge ... at least 0.5 mm". REQ-SYS-111: 1.0 mm knob radial clearance.
- REQ-SYS-116: "1.0 m (TBR) drop onto a hard floor on each face with the antenna fitted" (six faces; antenna fitted).
- REQ-SYS-117: "10 min of IEC 60529 IPX2 (TBR) dripping water while upright with plugs inserted".
- REQ-SYS-168: every closing gap of the cell cover below 4 mm or above 25 mm "throughout the cover's travel".
- Plan WP-PDR-27 output: "mechanical-tolerance-stack.md (SMA bulkhead with metal insert at 4.0 N.m, encoder bushings, jack noses, display window)"; "drop and IPX2 analysis"; "board outline and envelope drawing for WP-PDR-37 and 39".

**Search rule.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` (analysis checklist, SRR decision 87, record rules) preceded every `grep`. The rustos tree was not read.

## Findings (iteration 1)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | reviewer | Major | CK-ANA-F1 | note section 6 (drop, one generic column pair; "The antenna fitted in the drop is a flexible whip ... not computed here"); section 4 S2 and S5 (radial only); section 10 proposed value "REQ-SYS-116 keep 1.0 m" | Cases the governing requirements name are missing. (a) REQ-SYS-116 names "each face" and "with the antenna fitted". The note gives one deceleration for the whole unit and three internal load paths (cells, board, heat sink, display) without saying which face each covers. The faces load different parts: the back face lands on the guard and the heat-sink pocket, the front face on the display lens and encoder knobs, the +X end on the port block and the fitted antenna, the -X end on the jacks and USB opening. The +X impact with the whip fitted puts a moment into the port block, which is the REQ-SYS-105 load path (L1 margin 3.0 on a Low planning value), and it is explicitly not computed. (b) REQ-SYS-108 requires "fully seated" plugs, an axial condition; S2 and S5 check radial clearance only, and no stack gives the plug engagement depth through the 2.0 mm wall plus the S7 board-to-wall gap for the key jack, headphone jack and USB receptacle. The proposed REQ-SYS-116 value and the M3 "every plug seats" pass of TS-011 rest on these cases. Fix: add one drop row per face (or per distinct load path, with the faces it bounds named), including the +X face with the whip fitted as a moment on the port block against the L1 capacity; add axial stacks for the three plugs (and the encoder bushing thread engagement through the front wall, which the plan's "encoder bushings" item implies) | Open | Pending | |
| <a id="finding-2"></a>finding-2 | reviewer | Minor | CK-ANA-E5 | note sections 5 and 10 (REQ-SYS-105 "met by construction", REQ-SYS-107 "keep 20 mm and 10 mohm") | Two proposed values do not execute their `tbr.plan` step. REQ-SYS-105's plan asks the PDR analysis to confirm the 1 dB limit "with the NanoVNA repeatability"; the note argues only that the load avoids the pigtail and gives no repeatability figure against 1 dB. REQ-SYS-107's 10 mohm is not computed: the chain is jack shell, nut and toothed washer to the 6061 port block, then the tapped M3 counterpoise hole, and the block's finish (bare, conversion-coated or anodized) is not stated. Fix: state the NanoVNA repeatability basis (for example from the TV record of the NanoVNA, or mark it an owner input) and compute the counterpoise-to-shell resistance with the block finish named | Open | Pending | |
| <a id="finding-3"></a>finding-3 | reviewer | Minor | CK-ANA-B1 | note section 4 S6c ("compression set by the spring force, not by the stack"); TS-011 section 8 rule 3 | The spring-loaded heat sink passes S6c on travel (worst 0.50 mm inside +/-0.6 mm), but the spring force is not sized. The gap pad value the thermal chain uses (0.74 K/W, research F18) holds at a stated compression or pressure; the two springs must give that pressure over the whole travel and must not overload the 1.0 mm board between its bosses. Fix: size the spring rate and preload against the pad's pressure and the board deflection (L3 method), or name the check as a WP-PDR-39 input | Open | Pending | |
| <a id="finding-4"></a>finding-4 | reviewer | Minor | CK-ANA-F1, F2 | note section 7 (IPX2 and edge break) | Two cases are argued only in part. (a) IPX2 drips water with the enclosure tilted up to 15 degrees in each of four positions; the note treats the upright position and says the front face is vertical, but at a 15 degree tilt the front face takes drips, and the buttons "with printed skirts" are not shown to shed them (the display lens is bonded and the encoder bushings nut-sealed). (b) REQ-SYS-110 covers "every external edge and cutout edge"; the note states the 1.0 mm fillet for the printed outer edges and the CNC chamfer, but not the cutout edges of the openings and the guard slots. Fix: add the tilt positions and the button seal, and the cutout-edge rule | Open | Pending | |
| <a id="finding-5"></a>finding-5 | reviewer | Minor | CK-ANA-D3, E3 | note section 9 rows E2 and E6; section 4 S3; section 2 row "Loads" (0.37 kg) | Near-zero margins are reported as passes without comparing them with the tolerances the note itself uses. E2 is 30 + 10 = 40 mm against the 40 mm envelope and E6 is 23.0 mm against 23.02 mm, both with 0 to 0.02 mm margin while a printed feature carries +/-0.20 mm (section 2); S3 passes by 0.10 mm on Low planning values. The unit mass is taken as 0.37 kg against the TS-011 roll-up of 375 g (rounded away from the conservative side; the drop energy changes from 3.68 to 3.63 J, no verdict changes). Fix: state these as zero-margin items with the consequence (a 0.5 mm envelope allowance, a heat-sink height cap below 23 mm, or a coupon check), and use 0.375 kg | Open | Pending | |

One Major finding is open, so the reviewer verdict is NEEDS CHANGES. The stacks, load checks and envelope checks that the note does compute are correct (re-checked below), and the four decisions it takes (RG-316 pigtail, display glass in the front shell, 12.6 x 10.6 mm USB opening, spring-loaded heat sink) follow from failing variants that are recorded.

### Per-case results (section F)

| Case | Condition | Governing id and limit | Result | Margin with sign | Uncertainty | Reviewer re-check | Finding ids |
|---|---|---|---|---|---|---|---|
| C-1 | 4.0 N m moment, shortest block arm 12 mm, bearing on the printed pocket | REQ-SYS-105; TS-011 M2 margin >= 1.5 | 333 N, 2.31 MPa against 45 MPa | margin 19.4 | strength Low | hand: 4.0 / 0.012 = 333 N; 333 / 144 mm^2 = 2.31 MPa | none |
| C-2 | Same, reacted by the two M3 inserts | REQ-SYS-105; M2 >= 1.5 | 167 N per insert against 500 N | margin 3.0 | pull-out Low | hand: 333 / 2 = 167 N | none |
| C-3 | Moment in the other directions (longer 20 mm arm) and about the jack axis | REQ-SYS-105 "any direction" | bounded by C-1 and C-2 (the 12 mm arm is the shortest); rotation held by the D-flat under 0.90 N m | positive | Low | reasoning checked | none |
| C-4 | Return-loss change within 1 dB | REQ-SYS-105 | "met by construction", no figure | not computed | not stated | not re-checked | finding-2 |
| C-5 | Counterpoise distance and resistance | REQ-SYS-107: 20 mm, 10 mohm | 12 mm by design (S9 worst 0.10 mm); resistance not computed | +8 mm; resistance none | CNC +/-0.10 mm | S9 re-run | finding-2 |
| C-6 | Key jack and headphone jack admitted and fully seated | REQ-SYS-108 | radial S2: worst 0.65 against 1.50 mm; axial not analysed | +0.85 mm radial | FDM Low | re-run: same | finding-1 |
| C-7 | USB receptacle admitted and fully seated | REQ-SYS-108 | radial S5b: 0.90 against 1.00 mm (S5a at the ICD 12.0 x 10.0 fails); axial not analysed | +0.10 mm radial | FDM Low | re-run: same | finding-1, finding-5 |
| C-8 | Edge break, external and cutout edges | REQ-SYS-110: 0.5 mm | 1.0 mm fillet on printed outer edges; CNC 0.5 mm chamfer; cutouts not stated | +0.5 mm on stated edges | none stated | reading | finding-4 |
| C-9 | Knob radial clearance | REQ-SYS-111: 1.0 mm | S8 worst 0.75 against 1.00 mm (recess = knob + 4.0 mm) | +0.25 mm | FDM Low | re-run: same | none |
| C-10 | Drop, each of six faces, antenna fitted | REQ-SYS-116: 1.0 m | one generic case: 1000 to 2000 g; cells 4.4 to 8.7 MPa on ribs; boss 57 to 114 N; heat sink 490 to 980 N on 160 mm^2 | per face not given | stop distance Low | hand: v^2 = 19.62; 19.62 / (2 x 0.001) / 9.81 = 1000 g; 0.048 x 9810 / 108 mm^2 = 4.36 MPa; 0.035 x 9810 / 6 = 57 N | finding-1 |
| C-11 | IPX2, upright, plugs inserted, 15 degree tilt positions | REQ-SYS-117 | upright argued; tilt positions not | not given | none | reading | finding-4 |
| C-12 | Cell cover closing gap throughout travel | REQ-SYS-168: < 4 or > 25 mm | sliding door overlapped 3 mm by the frame, gap stays below 4 mm | positive by design | none | reading | none |
| C-13 | Display active area in the window | plan item "display window" | S4b 0.30 against 0.48 mm (S4a on the board fails) | +0.18 mm | FDM and adhesive Low | re-run: same | none |
| C-14 | Encoder bushing in its hole | plan item "encoder bushings" | S3 0.65 against 0.75 mm | +0.10 mm | FDM Low | re-run: same | finding-5 |
| C-15 | SMA bulkhead with metal part at 4.0 N m | plan item | port block and pigtail (S1 rigid variant fails, recorded) | C-1, C-2 | as above | re-run: same | none |
| C-16 | Envelope and heat-sink height | REQ-SYS-103: 40 mm; TS-011 rule 3 | E2 40.0 against 40 mm; E6 23.0 against 23.02 mm | 0.00 and +0.02 mm | FDM +/-0.20 mm | `envelope_drawing.py --check` re-run | finding-5 |
| C-17 | Board stiffness | TS-004 K2 | 3.17 mm (120 mm span), 0.76 mm (74.5 mm) at 1.0 mm, 10 N; posts under the buttons | posts rule | E Low | hand: 10 x 120^3 / (48 x 22 000 x 5.17) = 3.17 mm | none |

## Readiness criteria

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | Frozen: every `product_files` blob equals `git rev-parse 70a3a33:<path>` | Yes | 7 of 7 equal, and equal at `HEAD` `4ef04ee` |
| R2 | The checkers run by the commands the note names and exit as stated | Yes | Scratchpad export of `70a3a33`: `tolerance_stack.py --check` and `envelope_drawing.py --check` exit 0, `CHECK PASS` |
| R3 | `validate_docs.py` on a JSON product | N/A | `board-outline.json` is not under a schema convention of `validate_docs.py` |
| R4 | Author's return states question, assumptions, inputs, results, limitations, values and tools | Yes | Author summary and note sections 1 to 11 |
| R5 | No `TBD`; every TBR relied on named by id | Yes | Search, then grep: no `TBD` in the note; TBRs named with their REQ ids |
| R6 | Every render the note cites exists | Yes | Both PNGs present |

## A. Question, scope and traceable inputs

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-A1 | Yes | Header "Serves": REQ-SYS-105, 107, 108, 110, 111, 116, 117, 168, TS-011 M1 to M3, M6, C5, TS-004 K2, ICD-TX-ANT 3.2.2 and ICD-CTL-USB 3.2.2; every id exists |
| CK-ANA-A2 | Yes | Design data `board-outline.json` (blob above), TS-011 section 8; AT RISK on CR-003 and CR-006 stated |
| CK-ANA-A3 | Yes | Section 2 input table: each contributor has a source or is labelled the author's planning value (Low); PCBWay drill and outline tolerances from `pcbway-fabrication-and-assembly.md` F9 (High); display dimensions from `display-and-ui-parts.md` F2 and UI-DSP-05; cell mass from ICD-PWR-CELL 3.2.1 |
| CK-ANA-A4 | Yes | Every contributor checked against the checker source (`STACKS` lists) and every sum recomputed: S1 0.10 + 0.20 + 0.10 + 0.20 + 0.10 + 0.10 = 0.80; S2 and S3 0.15 + 0.20 + 0.10 + 0.20 = 0.65; S4a 0.80, S4b 0.30; S5 0.30 + 0.10 + 0.20 + 0.10 + 0.20 = 0.90; S6a and S6c 0.50; S6b 0.10; S7 0.70; S8 0.75; S9 0.10. Allowances recomputed from the stated dimensions: S2 (9.0 - 6.0) / 2 = 1.5; S3 (8.5 - 7.0) / 2 = 0.75; S4 (24.0 - 23.04) / 2 = 0.48; S5a (12.0 - 10.6) / 2 = 0.70; S5b 1.00. All equal the CSV |
| CK-ANA-A5 | Yes | Assumptions stated with their confidence and replacement (WP-PDR-39 coupon, filament datasheet); the direction of the mass rounding is finding-5 |
| CK-ANA-A6 | Yes | Consequences sent as cross items: ICD-CTL-USB and ICD-TX-ANT to WP-PDR-36, display pocket to WP-PDR-25 and 39, support posts to WP-PDR-37 and 39 |

## B. Model validity

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-B1 | No | Worst-case sum with RSS for information, closed-form loads and a simply supported beam, each stated; the drop stopping distance is labelled Low. Missing: the spring force model behind S6c (finding-3) |
| CK-ANA-B2 | N/A | No vendor model |
| CK-ANA-B3 | Yes | Closed-form textbook relations (couple, v^2 / (2 s), 48 E I beam), each reproduced by hand below |
| CK-ANA-B4 | N/A | No numerical settings |
| CK-ANA-B5 | Yes | Hand checks in the per-case table (C-1, C-2, C-10, C-17) and A4; all agree with the checker |
| CK-ANA-B6 | Yes | Section 11 lists the uncertainty sources (FDM planning values, recalled strengths, first-cut drop); the worst-case method bounds the stacks |

## C. Tools, validation status and reproducibility

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-C1 | Yes | venv Python with numpy and matplotlib, class B (header "Evidence status") |
| CK-ANA-C2 | Yes | No TV record; every number marked developer evidence |
| CK-ANA-C3 | Yes | Two headless commands in section 3 |
| CK-ANA-C4 | Yes | Re-run on a scratchpad export of `70a3a33`: both exit 0; `tolerance-stack.csv`, `tolerance-stack.png` and `board-outline-envelope.png` hash to the frozen blobs (byte-identical) |
| CK-ANA-C5 | N/A | No TV record |

## D. Units, arithmetic and consistency

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-D1 | Yes | mm, N, N m, MPa, g, J used consistently |
| CK-ANA-D2 | Yes | Section 4 table equals `tolerance-stack.csv`; sections 5, 6 and 8 equal the checker's printed loads; section 9 equals the `envelope_drawing.py` output (E1 2.00 mm, E5 0.80 against 2.5 mm, E6 23.0 against 23.02); the same values appear in TS-011 and TS-004 |
| CK-ANA-D3 | No | Mass rounded down from 375 g to 0.37 kg (finding-5) |
| CK-ANA-D4 | Yes | Allowances in `STACKS` equal the dimensions in their basis strings; REQ ids in the comments |

## E. Results, margins, proposed values and credit

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-E1 | Yes | 4.0 N m, 20 mm, 1.0 mm, 1.0 m, IPX2, 4 and 25 mm quoted with their ids |
| CK-ANA-E2 | Yes | Margins as allowance minus worst case; signs right |
| CK-ANA-E3 | No | Zero and near-zero margins reported as passes without comparison with the tolerances used (finding-5) |
| CK-ANA-E4 | Yes | Both checkers assert every stack verdict and every E check and exit 1 on a difference |
| CK-ANA-E5 | No | REQ-SYS-105 and REQ-SYS-107 `tbr.plan` steps not executed (finding-2); REQ-SYS-116 value rests on the missing cases (finding-1) |
| CK-ANA-E6 | N/A | No TPM estimate (the mass TPM is TS-011 and WP-PDR-29) |
| CK-ANA-E7 | Yes | No credit claimed; REQ-SYS-105, 107, 116, 117 are Test-method requirements, and the note says the closing evidence is the test on the delivered unit |

## F. Every case named

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-F1 | No | Per-case table: the six drop faces with the antenna fitted and the axial seating of the three plugs are missing (finding-1); the IPX2 tilt positions and the cutout edges are argued only in part (finding-4) |
| CK-ANA-F2 | Yes | Failing variants recorded (S1, S4a, S5a, S6a) so they are not reintroduced |
| CK-ANA-F3 | Yes | Worst-case sum of all contributors in each stack |
| CK-ANA-F4 | Yes | For the near-limit stacks the two largest contributors are the FDM values, replaced by the WP-PDR-39 coupon (section 11) |

## G7. Worst-case

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-G7-1 | Yes | Extreme-value sum used for the verdict, RSS shown for information without an independence claim |
| CK-ANA-G7-2 | N/A | No temperature or ageing tolerances of the derating kind; the PETG strength derating for 45 C is stated as a planning value |

## H. Hazards, risks and records

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-H1 | Yes | Port retention serves HZ-009 (section 5 heading); no control edited |
| CK-ANA-H2 | Yes | PETG creep at the port block and bosses is carried as a TS-011 section 7 risk (CR-003 candidate (b)) |
| CK-ANA-H3 | N/A | Revision 0 at its first freeze |

## I. Visual closure

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-I1 | Yes | `docs/reviews/PDR/figures/tolerance-stack.png` and `docs/reviews/PDR/figures/board-outline-envelope.png` opened with the Read tool (2 renders) |
| CK-ANA-I2 | Yes | Tolerance plot: worst-case bars (dark pass, red fail), RSS bars, allowance ticks, each row labelled with worst, RSS and allowance, S9 off-scale noted in the title; values equal the CSV. Envelope drawing: plan view and X-Z section with the REQ-SYS-103 line and the E1 to E6 footer; cosmetic issues (a label arrow on a boss, empty X range to 200 mm) are noted in INSP-081 and change no value |

## Items N/A

CK-ANA-G1 to G6, CK-ANA-J1 to J3 (criticality neither), CK-ANA-B2, B4, C5, E6, G7-2, H3, readiness R3.

## Cross items for the lead SE (not findings on the note)

- **X-1.** The checklist field names `peer-review-checklist-design` because the analysis template is on the CR-012 branch only; switch it at the delta after CR-012 merges.
- **X-2.** Status note 2026-09-27 section 6 (after the freeze) may change the construction method and SI-031; the board outline and the port block from PCBWay then iterate under rule C8.
- **X-3.** The ICD changes the note proposes (ICD-CTL-USB 12.6 x 10.6 mm, ICD-TX-ANT pigtail) go to WP-PDR-36 as requests; REQ-SYS-108 names a "micro-USB receptacle", which the ICD-CTL-USB writer should confirm against the Pico 2 connector.

## Commands

- `git rev-parse 70a3a33:<path>`, `git rev-parse HEAD:<path>` and `git hash-object <path>` at `4ef04ee` for the 7 product files: equal.
- Scratchpad export of `70a3a33`: `tolerance_stack.py --check` exit 0, `envelope_drawing.py --check` exit 0; outputs byte-identical.
- `.venv/bin/python tools/validate_docs.py`: this record passes.

## Measurements (SWE-089)

Items checked 40 (A1 to A6, B1 to B6, C1 to C5, D1 to D4, E1 to E7, F1 to F4, G7-1, G7-2, H1 to H3, I1, I2) plus readiness 6; items answered No 5; findings 1 Major, 4 Minor; fixed 0, deferred 0; iteration 1; renders inspected 2; inputs checked 24 (every stack contributor and allowance); effort about 30 turns and 45 minutes (session shared with INSP-081 to INSP-083).

## Iteration 2: delta verification of finding-1 (Major) (2026-09-27, HEAD `d1148c2`)

**Scope (rule C1).** Iteration 2 is a delta that verifies the fix of finding-1 only. Findings 2 to 5 (Minor) were not addressed by the author (note change log, revision 1 row; section 7 marks the IPX2 text as the revision 0 text with finding-4 open) and are not re-reviewed. Product: the 10 blobs of front matter `product_files`, committed as `70d11ef` (note revision 1, re-freeze F0). Each equals `git rev-parse 70d11ef:<path>`, `git rev-parse HEAD:<path>` and `git hash-object <path>` (10 of 10). `git log 70d11ef..HEAD` shows no later change to any product file. No blob is on a `cr/` branch. Checklist as iteration 1: `peer-review-checklist-analysis.md` revision A, blob `0386cc6e`, still only on `cr/CR-012-pdr-checklist-templates` at `7784672` (not merged at `d1148c2`).

**Independence (rule C4).** This invocation authored no part of WP-PDR-27 and no part of revision 1. It edited no product file.

**Search first (charter section 11 rule 1).** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search. `grep` then only pinned lines in known paths (the note, `drop_and_axial.py`, `board-outline.json`). The rustos tree was not read.

**Reproduction.** On a `git archive 70d11ef` export in the scratchpad: `drop_and_axial.py --check`, `tolerance_stack.py --check` and `envelope_drawing.py --check` each exit 0 with `CHECK PASS`; the regenerated `drop-and-axial.csv`, `tolerance-stack.csv`, `drop-and-axial.png`, `tolerance-stack.png` and `board-outline-envelope.png` hash to the frozen blobs (5 of 5 byte-identical).

### Verification of finding-1, case by case (rule C7)

| # | Case the finding named | Check | Result |
|---|---|---|---|
| 1 | (a) REQ-SYS-116 "each face": one row per face or per distinct load path, with the faces named | Section 6 rows D1 to D20 and the "Face by face" paragraph: -Z back (D1 to D4), +Z front (D5 to D12), +/-Y sides (D13 to D15), +X end (D16 to D19), -X end (D20, and the end face lands because the jacks are recessed, rule 21); the heat sink in plane is stated (1.6 MPa on 600 mm2) | Yes |
| 2 | (a) the loads each face drives into different parts: guard and heat-sink pocket, display lens and knobs, port block and antenna, jacks and USB | D1, D2 (back); D5 with rule 17 (knob tops recessed), D12 (display glass); D16 to D19 (port block); A1 to A3 and rule 21 (jack noses recessed so the -X face lands on the case) | Yes |
| 3 | (a) the +X impact with the whip fitted as a moment on the port block against the L1 capacity | D16: 8.0 N m (a 10 N push on a 40 cm whip, 4.0 N m, times 2 for a suddenly applied load; `antenna-and-erp.md` F8) on the 12 mm arm, 667 N on 144 mm2 = 4.63 MPa against 45 MPa, margin 9.7; D17: the same moment on the two inserts alone, 333 N each against 500 N, margin 1.50, at the M2 rule and named as the bound. The whip's base yield assumption is stated in section 11 | Yes |
| 4 | (a) revision 0 load paths that fail are found and replaced | D6 (heat sink into the board, 48 mm span): hand 490 N x 0.048 / 4 = 5.88 N m on Z = 0.062 x 0.001^2 / 6 = 1.033e-8 m3 gives 569 MPa, margin 0.70 at 1000 g (CSV 569.61, 0.70); D7 with the two rule 18 posts: 490 / (2 x 28.27 mm2) = 8.67 MPa (CSV 8.67); D8 posts 45 / 8.67 = 5.19 (CSV). D9 fails and D10 passes with four posts; D14 fails and D15 passes with rule 20; D18 not shown and D19 passes with the rule 6 flange. Each replaced design is kept as a failing row, as section 10 says | Yes |
| 5 | (b) REQ-SYS-108 "fully seated": axial stacks for the key jack, headphone jack and USB receptacle | Section 4.1 A1, A2: nose recess 1.0 mm +/- (0.15 + 0.20 + 0.10 + 0.20) = 0.35 to 1.65 mm; radial room (9.0 - 7.0) / 2 - 0.65 = 0.35 mm for the admitted plug (rule 21). A3: 3.0 + 2.0 - 1.3 = 3.7 mm +/- 0.9 = 2.8 to 4.6 mm, inside the 8.0 mm overmold length, with the O1 shroud section kept to the receptacle face | Yes (the admitted-plug definition: new finding-7, Minor) |
| 6 | (b) encoder bushing thread engagement through the front wall | A4: need 2.6 + 2.0 + 0.5 + 2.0 = 7.1 mm plus 0.9 mm of stack; a 7 mm bushing is 1.0 mm short (fail, recorded); A5: a 9 mm bushing leaves 1.0 mm (pass), rule 22 | Yes (the rule 22 inner jam nut is not stacked: new finding-6, Minor) |
| 7 | The unit mass (iteration 1 finding-5 remark) | 0.375 kg used in section 6 (3.68 J) | Yes (finding-5 otherwise not in the delta) |

**Result: finding-1 Verified.**

### Findings (iteration 2)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| finding-1 | reviewer | Major | CK-ANA-F1 | note sections 4.1 and 6; `drop_and_axial.py` | See iteration 1 | Verified (iteration 2, revision 1 at 70d11ef) | n/a | |
| finding-2 | reviewer | Minor | CK-ANA-E5 | note sections 5 and 10 | Not in the delta | Open | Pending | CDR readiness declaration (lien) |
| finding-3 | reviewer | Minor | CK-ANA-B1 | note section 4 S6c | Not in the delta | Open | Pending | CDR readiness declaration (lien) |
| finding-4 | reviewer | Minor | CK-ANA-F1, F2 | note section 7 | Not in the delta | Open | Pending | CDR readiness declaration (lien) |
| finding-5 | reviewer | Minor | CK-ANA-D3, E3 | note section 9 E2, E6; S3 | Not in the delta (the 0.375 kg part is now used) | Open | Pending | CDR readiness declaration (lien) |
| <a id="finding-6"></a>finding-6 | reviewer | Minor | CK-ANA-F1 | note section 4.1 A5 and rule 22; `drop_and_axial.py` `ENC_GAP_BODY_TO_WALL` (2.6 mm), `NUT` (2.0 mm) | Rule 22 runs an inner jam nut against the wall inner face, inside the 2.6 mm gap between the encoder body top and the wall. The A5 stack checks the outer thread only; the same 0.9 mm of Z contributors that it applies can close the gap to 1.7 mm, less than a 2.0 mm nut, and the body cannot then be held off the wall by the jam nut as the rule intends. Fix: add the jam-nut fit to A5 (gap at the worst case against the nut thickness) and set the body-to-wall gap, a thin jam nut, or a spacer so it passes | Open | Pending | CDR readiness declaration (lien) |
| <a id="finding-7"></a>finding-7 | reviewer | Minor | CK-ANA-E5 | note section 4.1 A1, A2 and rule 21 ("the admitted plug for REQ-SYS-108 is one whose overmold is at most 7.0 mm over its first 2 mm") | REQ-SYS-108 requires "fully seated mating plugs" at the key and headphone jacks with no plug-size limit. The pass is now conditional on a plug definition that narrows the requirement, and it is not checked against the plugs the owner will use (the owner's straight key and paddle are to be named at OD-22; common 3.5 mm cables have overmolds of 8 mm or more, which would stop at the face 0.35 to 1.65 mm short of full seating). Fix: state the definition as a proposed REQ-SYS-108 interpretation for the owner (with ICD-CTL-KEY), check it against the OD-22 key, paddle and headphone plugs, or widen the opening | Open | Pending | CDR readiness declaration (lien) |

Neither new finding is Major: each concerns a rule the fix added, with a design step that closes it, and neither changes a drop or axial verdict of the recommended design.

### Visual closure (iteration 2)

Two renders opened with the Read tool (renders_inspected 4 cumulative):
- `docs/reviews/PDR/figures/drop-and-axial.png` (new): horizontal bars of the margin at 2000 g for D1 to D20 with 1000 g diamonds, hatched for the revision 0 design and plain for revision 1 rules, coloured pass, not shown and fail, the dashed 1.5 line (M2 rule) and a dotted 1.0 line; bars off the 12 scale carry their value; the right-hand text lists A1 to A5 with verdicts and rules. The values match the CSV (for example D6 0.35, D17 1.50, D18 1.47, D19 2.45). The D6 and D9 value labels overlap their diamonds, cosmetic.
- `docs/reviews/PDR/figures/board-outline-envelope.png` (revised): the rule 18 posts appear as triangles at the positions of `board-outline.json`, and the rule 14 sensors in the PA pad. The jack recess of rule 21 and the port-block flange of rule 6 are not drawn in the X-Z section; the section is a Z-stack view and the note gives both rules in text, so not a finding.
- `docs/reviews/PDR/figures/tolerance-stack.png` is byte-identical to iteration 1 and was not re-reviewed.

### Cross items (iteration 2, returned to Claude)

- X-1. The record `verdict` is held only for the CR-012 merge (lead SE convention of 2026-09-27); no SA pair is required.
- X-2. The rule 18 posts that D7, D8 and D10 need touch the hot board; INSP-081 iteration 2 finding-8 bounds them for M8 (94.1 C at the post near the PA).
- X-3. The plugs-inserted state also matters to shielding (INSP-083 iteration 2 finding-5): a jack sleeve bonded at the wall (its possible fix) changes the jack mounting and the A1 and A2 stacks.

### Completion criteria (SWE-088), iteration 2

Reviewer side met: no Major is open, readiness is met (R1, R2 and R4 to R6 re-checked at `70d11ef`), and findings 2 to 7 are Minor liens due at the CDR readiness declaration (plan rule C1; PDR package section 15). `reviewer_verdict: APPROVED`. The record `verdict` stays NEEDS CHANGES until CR-012 merges with the analysis template blob `0386cc6e` unchanged; it is then set to APPROVED in that merge commit or the commit right after it.

```
ITERATION 2 (2026-09-27, HEAD d1148c2, product commit 70d11ef): REVIEWER VERDICT: APPROVED; RECORD VERDICT: NEEDS CHANGES (held for the CR-012 merge only)
FINDINGS:
- [Major] finding-1: Verified (drop rows D1 to D20 per face and load path, +X whip moment D16 and D17 against the L1 capacity; axial stacks A1 to A3; encoder thread A4 and A5; rules 6 and 17 to 22).
- [Minor] finding-2 to finding-5: Open, not in the delta (liens).
- [Minor] finding-6 (new): the rule 22 inner jam nut is not stacked (1.7 mm worst-case gap against a 2.0 mm nut) (lien).
- [Minor] finding-7 (new): the rule 21 admitted-plug definition narrows REQ-SYS-108 and is unchecked against the OD-22 plugs (lien).
MEASUREMENTS: blobs equal HEAD 10/10; checkers 3 of 3 CHECK PASS; outputs byte-identical 5/5; cases 7 (7 Yes, 2 with a new Minor); hand checks 6; renders inspected 2 (4 cumulative); major open=0; minor open=6; turns=25; minutes=40 (cumulative 55 and 85); iteration=2
```

## Iteration 3: drift delta on board-outline.json (2026-09-27, HEAD `e2d3226`)

**Scope (rule C1).** Iteration 3 is a delta on the one product blob that drifted after the iteration 2 freeze: `hardware/enclosure/board-outline.json` `9d4d36a9` became `d7977cf3` on main at `433a944` (WP-PDR-27 shielding revision 2, INSP-083 finding-5). `git log 70d11ef..HEAD` over the ten product paths lists `433a944` only. The other nine blobs are unchanged and equal `git rev-parse HEAD:<path>` and `git hash-object <path>` at `e2d3226` (10 of 10 with the new blob). No product blob is on a `cr/` branch. Checklist as iterations 1 and 2 (analysis template revision A, blob `0386cc6e`, still only on `cr/CR-012-pdr-checklist-templates` at `7784672`).

**Independence (rule C4).** This invocation authored no part of WP-PDR-27, its revision 1 or the shielding revision 2, and edited no product file.

**Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` (shielding rule O2 revision 2, gasket ring) ran before any `grep`; `grep` then only pinned lines in known paths. The rustos tree was not read.

### Hunks read (`git diff 9d4d36a9 d7977cf3`, 2 hunks, 3 changed lines)

| # | Hunk | Change | Numeric effect | Effect on this note |
|---|---|---|---|---|
| 1 | line 3, `revision` | "1 (... TS-011 revision 1 ...)" to "2 (... TS-011 revision 2: jack features per shielding rules O2 and O4, INSP-083 finding-5 ...)" | none | none |
| 2 | `minus_x[0]` and `minus_x[1]` `feature` (key and headphone jack) | Adds to the collar text: "bonding land for the metal nose of the jack (its sleeve contact) through a conductive gasket ring all round (shielding rule O2, revision 2)" and "tip and ring filtered within 5 mm of the jack pins to the sleeve pin (shielding rule O4)"; `y` 18.0 / 52.0 and `z` 21.9 unchanged | none (text fields; no checker reads them for a value) | A new part in the jack opening, the gasket ring, which stacks A1 and A2 do not include: finding-8 |

The O4 filters are board parts (WP-PDR-37) and touch no stack, drop row or envelope check. The metal nose is the S2 nose (6.0 mm, `shielding-estimate.md` section 2 row "Jack parts"), so S2 is unchanged; the shielding note states the ring adds "no constraint to stack S2" with at most 5 N of side force, which holds for the radial stack.

**Reproduction.** On a `git archive e2d3226` export in the scratchpad (removed afterwards): `tolerance_stack.py --check`, `drop_and_axial.py --check` and `envelope_drawing.py --check` each exit 0 with `CHECK PASS`; `tolerance-stack.csv`, `drop-and-axial.csv`, `tolerance-stack.png`, `drop-and-axial.png` and `board-outline-envelope.png` hash to the `product_files` blobs (5 of 5 byte-identical). The feature text is not rendered, so no render changed and none was re-opened (renders_inspected stays 4).

### Findings (iteration 3)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| finding-1 | reviewer | Major | CK-ANA-F1 | note sections 4.1 and 6 | See iteration 1 | Verified (iteration 2); unaffected by the drift | n/a | |
| finding-2 to finding-7 | reviewer | Minor | as iteration 2 | as iteration 2 | Not in the delta | Open | Pending | CDR readiness declaration (lien) |
| <a id="finding-8"></a>finding-8 | reviewer | Minor | CK-ANA-F1 | `board-outline.json` `minus_x` features (rule O2 revision 2 gasket ring); note section 4.1 A1, A2 | Stacks A1 and A2 pass REQ-SYS-108 "fully seated" on a clear 9.0 mm opening: a plug overmold of at most 7.0 mm reaches the nose face 0.35 to 1.65 mm behind the outer face with 0.35 mm of radial room. The revised data file puts a conductive gasket ring "all round" the 6.0 mm nose in that same annulus, and the shielding model places its contact ring at the 2 mm wall depth (`shielding-estimate.md` section 3, "8 slots of 3 mm at the 2 mm wall depth"), which is where the nose face and the plug's first 2 mm sit. The ring's axial position is not stated. If any of it lies ahead of the nose face plane, its bore is the nose diameter (6.0 mm), smaller than the 7.0 mm admitted overmold, and the plug stops on the ring short of full seating; the note, unchanged, does not stack it. Fix: state the ring's axial extent (behind the nose face plane, for example on the collar land) in the data file and add it to A1 and A2 as a contributor, or narrow the admitted-plug overmold to what clears the ring, keeping finding-7 in view | Open | Pending | CDR readiness declaration (lien) |

finding-8 is Minor: the change is text in planning data, no computed verdict changes, and placing the ring behind the nose face closes it with no design change elsewhere. It is the case iteration 2 cross item X-3 foresaw.

### Completion criteria (SWE-088), iteration 3

Reviewer side still met: no Major is open, readiness R1 (re-frozen at `433a944`), R2 and R4 to R6 hold at `e2d3226`, and findings 2 to 8 are Minor liens due at the CDR readiness declaration. `reviewer_verdict: APPROVED`. The record `verdict` stays NEEDS CHANGES, held for the CR-012 merge only (analysis template blob `0386cc6e` unchanged on its branch at `7784672`); it is set to APPROVED in that merge commit or the commit right after it.

```
ITERATION 3 (2026-09-27, HEAD e2d3226, product commit 433a944, drift delta): REVIEWER VERDICT: APPROVED; RECORD VERDICT: NEEDS CHANGES (held for the CR-012 merge only)
FINDINGS:
- [Major] finding-1: Verified (iteration 2), unaffected.
- [Minor] finding-2 to finding-7: Open, not in the delta (liens).
- [Minor] finding-8 (new): the rule O2 revision 2 gasket ring sits in the jack opening annulus that A1 and A2 assume clear for the 7.0 mm admitted plug; axial position unstated and not stacked (lien).
MEASUREMENTS: drifted blobs 1 (board-outline.json 9d4d36a9 to d7977cf3); hunks read 2 (3 lines); blobs equal HEAD 10/10; checkers 3 of 3 CHECK PASS; outputs byte-identical 5/5; renders inspected 0 (4 cumulative); major open=0; minor open=7; turns=12; minutes=15 (cumulative 67 and 100); iteration=3
```
