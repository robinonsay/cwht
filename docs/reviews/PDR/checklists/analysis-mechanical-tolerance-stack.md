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
product_commit: "70a3a33"
product_files: ["docs/design/analysis/mechanical-tolerance-stack.md@78409153455c926873119ef8a981ea688bd4d453", "hardware/sim/enclosure/tolerance_stack.py@376e403c255c8cffcb4694e8160394f3a158a07b", "hardware/sim/enclosure/envelope_drawing.py@20815e7581c34c9498e6c8d3972cc738e5c63e8a", "hardware/enclosure/board-outline.json@27dbacc7dda7f79e6cba3234ee77f6453e304906", "hardware/sim/enclosure/out/tolerance-stack.csv@3e17c2097f3fcc3fdb3f24b50713622c3da8dd2f", "docs/reviews/PDR/figures/tolerance-stack.png@2ee6e410cec881db08c928d37b590d785d559c04", "docs/reviews/PDR/figures/board-outline-envelope.png@ff8aa6c2befd4660f2bf353893ab5673d24f79e3"]
analysis_kind: [worst-case, other]
product_size: 13 stacks (S1 to S9 with variants), 3 load checks (L1 to L3), 6 envelope checks (E1 to E6), 2 checkers, 1 data file, 2 plots
tools_used: ["venv Python 3.13.5 (TV-001 accredits the interpreter; numpy and matplotlib class B without a TV record; no TV record covers hardware/sim/enclosure/*.py; developer evidence per 05 section 9.1)"]
values_proposed: ["REQ-SYS-105: 1 dB return-loss change (keep; tbr.plan step not executed: finding-2)", "REQ-SYS-107: 20 mm and 10 mohm (keep; 10 mohm not computed: finding-2)", "REQ-SYS-116: 1.0 m (keep; cases missing: finding-1)", "REQ-SYS-117: IPX2 (keep; finding-4)", "REQ-SYS-168: 4 mm and 25 mm (keep; supported by the sliding-door design rule)"]
renders_inspected: 2
sprint: PDR-prep
author_agent: "author:WP-PDR-27 wave 1a (Claude as ME designer)"
reviewer_agent: "reviewer:WP-PDR-27-analysis-tolerance-iter1 (independent; authored no part of WP-PDR-27)"
criticality: neither
assurance_required: false
assurance_reviewer_agent: none
iteration: 1
readiness_met: true
reviewer_verdict: NEEDS CHANGES
assurance_verdict: not-required
verdict: NEEDS CHANGES
findings_major: 1
findings_minor: 4
findings_open: 5
findings_fixed: 0
findings_verified: 0
findings_deferred: 0
assurance_tasks_applied: []
deferred_rids: []
items_no: [CK-ANA-B1, CK-ANA-D3, CK-ANA-E3, CK-ANA-E5, CK-ANA-F1]
effort_turns: 30
effort_minutes: 45
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
