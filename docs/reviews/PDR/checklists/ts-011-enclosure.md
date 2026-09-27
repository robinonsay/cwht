---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md section 13;
# docs/process/06-risk-and-decision-analysis.md sections 14.3 step 6 and 16). Independent review of TS-011
# with docs/templates/peer-review-checklist-risk.md section B (PDR work plan WP-PDR-27, record path as the
# plan names it). Iteration 1 at freeze F0 (rule C2, freeze commit 70a3a33). The software assurance pair is a
# separate invocation (07 section 2.1.1 row "Trade studies and ADRs": the decision fixes the heat path and
# the heat-sink node that the SW-SAFE thermal unit senses, 07 section 14.1 row "Thermal protection"), filed
# as docs/reviews/PDR/checklists/ts-011-enclosure-software-assurance.md.
id: INSP-081
checklist: peer-review-checklist-risk
checklist_revision: A
checklist_file: docs/reviews/PDR/checklists/ts-011-enclosure.md
product: docs/decisions/trade-studies/TS-011-enclosure.md
product_commit: "70a3a33"
product_blob: 8d2708f1b0175d73945b7ee32d9d49937f4a51e9
# product_files: the study and the WP-PDR-27 files it scores from; the two analysis notes have their own
# records (INSP-083, INSP-084) and are not repeated here
product_files: ["docs/decisions/trade-studies/TS-011-enclosure.md@8d2708f1b0175d73945b7ee32d9d49937f4a51e9", "hardware/enclosure/board-outline.json@27dbacc7dda7f79e6cba3234ee77f6453e304906", "hardware/sim/enclosure/thermal_screen.py@78892ca27ace63c1bbd5965b730b0ccd6e85ab53", "hardware/sim/enclosure/envelope_drawing.py@20815e7581c34c9498e6c8d3972cc738e5c63e8a", "hardware/sim/enclosure/trade_matrix.py@c76b0f70d05a64c282a9066204a64ffe1e217fde", "hardware/sim/enclosure/out/thermal-screen.csv@a8c7d5b1b5f345172a036b590342f67b0adcc273", "hardware/sim/enclosure/out/trade-matrix.txt@c6023d697716d2c024c0033948aaeaa3aa3b7c0e", "docs/reviews/PDR/figures/ts011-thermal-screen.png@47d81e61ee7039b3126158c577170af30686752a", "docs/reviews/PDR/figures/board-outline-envelope.png@ff8aa6c2befd4660f2bf353893ab5673d24f79e3"]
product_size: 6 alternatives (A, B, C1, C2, C3, D; B, C2, C3 dropped at the mandatory screen), 9 mandatory and 8 enhancing criteria; route sub-matrix of 3 routes and 4 criteria; 22 rank-changing perturbations
sprint: PDR-prep
author_agent: "author:WP-PDR-27 wave 1a (Claude as ME designer)"
reviewer_agent: "reviewer:WP-PDR-27-ts-011-iter1 (independent; authored no part of WP-PDR-27)"
# criticality: TS-011 selects the PA-to-ambient heat path and the heat sink whose temperature REQ-SYS-181
# senses and against which the SW-SAFE thermal unit thresholds (REQ-SYS-118, 155) act (07 section 14.1 row
# "Thermal protection", safety-critical, HZ-003)
criticality: safety-critical
assurance_required: true
assurance_reviewer_agent: "pending (separate invocation; paired record docs/reviews/PDR/checklists/ts-011-enclosure-software-assurance.md)"
iteration: 1
readiness_met: true
reviewer_verdict: NEEDS CHANGES
assurance_verdict: pending
# verdict: NEEDS CHANGES while a Major finding is open and until the software assurance pair returns
# APPROVED (07 section 2.1.1; rule C9); the lead SE sets it
verdict: NEEDS CHANGES
findings_major: 2
findings_minor: 4
findings_open: 6
findings_fixed: 0
findings_verified: 0
findings_deferred: 0
deferred_rids: []
items_no: [CK-RSK-B5, CK-RSK-B7, CK-RSK-B8]
effort_turns: 60
effort_minutes: 95
record_status: Open
date: 2026-09-27
date_closed: null
---

# Peer review record: TS-011 enclosure concept (INSP-081, iteration 1)

**Product:** `docs/decisions/trade-studies/TS-011-enclosure.md` blob `8d2708f1` at freeze commit `70a3a33` (freeze F0, PDR work plan rule C2), with the files it scores from: `hardware/enclosure/board-outline.json` (`27dbacc7`), `hardware/sim/enclosure/thermal_screen.py` (`78892ca2`), `envelope_drawing.py` (`20815e75`), `trade_matrix.py` (`c76b0f70`), outputs `out/thermal-screen.csv` (`a8c7d5b1`) and `out/trade-matrix.txt` (`c6023d69`), figures `ts011-thermal-screen.png` (`47d81e61`) and `board-outline-envelope.png` (`ff8aa6c2`). Every blob equals `git rev-parse HEAD:<path>` and `git hash-object <path>` at `HEAD` `4ef04ee` on 2026-09-27. No product blob lives on a `cr/` branch. The shielding and tolerance analyses the study cites are reviewed in INSP-083 (`analysis-shielding-estimate.md`) and INSP-084 (`analysis-mechanical-tolerance-stack.md`).

**Checklist:** `docs/templates/peer-review-checklist-risk.md` revision A, section B (items CK-RSK-B1 to B10, 06 section 16 "Trade study" items 1 to 10). Section A is N/A (the product is a trade study).

**AT RISK.** The study is drafted on CR-003 revision 3 (`d9a215a`, re-checked in CR-003 section 6.4 with 0 Major and 5 Minor, verified at lines 392 to 420) and CR-006 revision 2, both Submitted (plan rule C8). This review takes the CR-003 revision 3 text as the governing text where the study says so (REQ-SYS-109 bond, REQ-SYS-113 "every accessible surface" with the 12 mm finger, CON-015, CON-026).

**Acceptance criteria (rule C7, every case the governing clauses enumerate):**
- 06 section 14.3 steps 1 to 5 and the template sections 1 to 9 filled; section 10 empty.
- 06 section 13 item 1: each of safety, first power-on, cost, schedule, performance margin and system security used as a criterion or omitted with a reason.
- 06 section 14.4 items 1 to 5: weight +/-10 on each of the 8 enhancing criteria (16 runs); +/-1 on every Low-confidence cell; robustness verdict; value of information; method limitations.
- 06 section 14.5: single recommendation, or the closely ranked set when totals differ by less than 25 points or the verdict is Not robust.
- 06 section 13 item 2: every surviving alternative's risks in the four-part format on the 06 section 6 and 7 scales; no Red safety risk that no identified step reduces to Yellow.
- Plan WP-PDR-27 TS-011 outputs, each checked: options C (build), A (held), B and D (paper); the mandatory set REQ-SYS-102, 103, 105, 107 to 113, 116, 117, 124, 168, 175, 177, 191; the PETG heat-deflection margin "at peak wall and boss temperature and at +60 C storage"; the coating research (published surface resistivity, adhesion to PETG, thickness, cure, service temperature, one product recommended); the OD-38 route criterion with its own sensitivity row, routes (a), (b), (c) and the CNC engraving, and for each route the REQ-SYS-124 and 191 verification, legibility under the coating, cost line, lead time against the 10-01 to 10-04 closure and release package content; the accessible-surface set of the 12 mm finger applied to the assembly model, handed to WP-PDR-28; proposed values for REQ-SYS-102, 103, 105, 106, 107, 114 to 117, 139, 168, 177, 109, 191 and the finger size.
- CR-003 section 4 Performance margins row and F9 resolution (line 341): the heat-deflection margin "at the peak wall and boss temperature (REQ-SYS-112 condition) and at +60 C storage" as a mandatory criterion.

**Search rule.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` (risk checklist section B, analysis checklist, SRR decision 87, 47 CFR 15.23, SE HB 6.8 mandatory screening, INSP numbering) preceded every `grep`; `grep` was used only to pin lines in CR-003, 06, 07 and the research reports at the hits. The rustos tree was not read.

## Findings (iteration 1)

| Finding | Severity | Item | Location | Description | State | Deferred to |
|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | Major | CK-RSK-B7, B8, B9 | TS-011 section 1 finding 1; section 4.1 row C1 column M4 and the heat-sink table; section 6 items 2 to 5; section 7 row C1 heat sink; section 8 rule 3; `thermal_screen.py` `ALTS["C1"]` (`r_amb=5.5`) | The recommended alternative survives mandatory M4 (REQ-SYS-112, 110 C at 45 C, 4.1 W continuous) only at an in-situ heat-sink resistance at the favourable end of the author's own estimate ("5.5 to 9 K/W (Low)"). Reviewer computation with the screen's own chain (3.0 + 4.7 + 1.0 + 0.74 + 0.3 = 9.74 K/W below the heat sink): C1 fails M4 above (110 - 45) / 4.1 - 9.74 = **6.11 K/W**, so most of the stated range fails, and the midpoint (7.25 K/W) gives about 114.7 C. The same screen drops B at 110.8 C (0.8 K over) on its point estimate. The uncertainty statement moves only enhancing cells (06 section 14.4 item 2) and never the mandatory verdict that decides whether C1 is in the matrix at all, so the Not robust verdict understates the uncertainty and the recommendation (C1 over D at the tie) rests on an unstated condition. Three statements that support the recommendation are also wrong or unsourced: (a) section 6 item 5 says a datasheet showing "5.5 K/W or better in situ" raises C1's C3 score to 2 and C1 leads alone at 310, but at 5.5 K/W the margin is the 2.5 K already scored 1; score 2 (margin >= 5 K) needs 4.89 K/W or less; (b) section 1 finding 1 and section 4.1 say REQ-SYS-055 limits operation to "80 % duty", but REQ-SYS-055 (`requirements.json`: "end antenna-port RF ... 7.5 s to 13 s (TBR) into any continuous key-down") sets no off-time, so no duty bound follows from it; (c) section 8 rule 3 turns a datasheet value of 4.5 K/W "at a 30 K rise" into 5.5 K/W in situ behind the guard with no source for the 1 K/W guard penalty, and no catalog part at 40 x 58 x 23 mm is shown to reach 4.5 K/W. The section 7 heat-sink risk is scored L3 (25 to 50 %) although the author's range puts most outcomes above the pass threshold, which reads as L4 on the 06 section 6 scale (Red 12 with consequence 3) | Open | |
| <a id="finding-2"></a>finding-2 | Major | CK-RSK-B5 | TS-011 section 3.1 M8; section 4.1 column M8 (C1 "printed rim 52.8 C", D 10.7 K); `thermal_screen.py` `steady()` (printed node is the rim or guard only) | Mandatory M8 is the PETG heat-deflection margin that CR-003 (section 4 Performance margins row; F9 resolution, line 341) and plan WP-PDR-27 name "at the peak wall and boss temperature". The screen evaluates only the printed rim and guard nodes coupled to the heat sink. The printed bosses, which carry the board through brass inserts and M3 screws on the board ground copper, are not evaluated, nor is any printed wall facing the board near the PA. With the screen's own chain at the REQ-SYS-112 condition (45 C, 4.1 W, 5.5 K/W), the board copper under the PA is at about 72 to 76 C (junction 107.5 C minus 4.1 W x 3.0 K/W = 95.2 C at the top pad, 75.9 C below the via array, 71.8 C at the pad face), above the 69 C HDT the study uses; the nearest bosses (board points (126.5, 4) and (126.5, 58)) are about 38 mm from the PA centre. Their temperature is not bounded, so M8 is not shown for C1 or for D (whose board mounts to the printed face). A boss above 64 C fails the 5 K rule | Open | |
| <a id="finding-3"></a>finding-3 | Minor | CK-RSK-B5 | TS-011 section 3.1 M1 and M5 | Two mandatory criteria are defined off the requirement text without saying so as a screening convention. M1 passes a mass estimate up to 385 g (350 g TBR plus a 10 % estimating allowance), so A (361 g) and C1 (375 g) pass a requirement both exceed. M5 reads REQ-SYS-177 as "20 dB from 12 to 600 MHz", while REQ-SYS-177 names every digital and switching-converter fundamental and harmonic and its closing case TC-SYS-107 computes them "to 1.5 GHz". The shielding model gives every option below 20 dB above about 1 GHz (INSP-083 finding-1), so M5 as the requirement reads is failed by all options and does not discriminate. Fix: label M1 and M5 passes "conditional" with the allowance and the frequency scope stated, and cite the INSP-083 disposition in M5 | Open | |
| <a id="finding-4"></a>finding-4 | Minor | CK-RSK-B7 | TS-011 section 6 item 2 | "10 Low-confidence cells" is 12 in the section 4.2 table and in `trade_matrix.py`: A (C1, C3), C1 (C1, C3, C4, C5), D (C1, C2, C3, C4, C5, C7). The list of 17 rank-changing moves in `out/trade-matrix.txt` is right; only the count is wrong | Open | |
| <a id="finding-5"></a>finding-5 | Minor | CK-RSK-B8 | TS-011 section 4.1 column M9; section 7 row C1 fire and the aggregate line | M9 (06 section 13 item 2) passes C1 and D on "the compartment control per CR-003 Q3", but section 7 carries the fire risk at 10 Red by the safety override with owner acceptance of the residual as its answer. Owner acceptance is not a step that reduces a risk to Yellow. The study should show the step that does: the compartment control of OQ-SAF-010 (WP-PDR-16) bounding the consequence at 4 ("fire or smoke contained to the unit", 06 section 7 safety column), giving L2 x C4 = 8 Yellow, or else record M9 as conditional on WP-PDR-16 | Open | |
| <a id="finding-6"></a>finding-6 | Minor | CK-RSK-B5 | TS-011 section 8 rule 4 and section 4.1 M4 ("the fins are not accessible"); plan WP-PDR-27 output "accessible-surface set for REQ-SYS-113 from the 12 mm test finger (TBR) applied to the assembly model, handed to WP-PDR-28" | The plan output is not delivered. The study checks one geometry, the finger in a 6.0 mm guard slot (`envelope_drawing.py` E5, 0.80 mm penetration against a 2.5 mm recess, re-checked: 6 - sqrt(36 - 9) = 0.80 mm). No list of accessible faces exists (guard, rim, shells, port block and SMA body, antenna), and M4's "hottest accessible face" takes max(guard, rim) without that list. The assembly model is WP-PDR-39, so the set may be due at the 1b final; the study should say so and name the faces it assumed | Open | |

Two Major findings are open, so the reviewer verdict is NEEDS CHANGES. Both concern the mandatory screen of the recommended alternative; neither says C1 is the wrong choice. After the fix the recommendation may stand as "C1, conditional on an in-situ heat-sink resistance of 6.1 K/W or less and a boss temperature of 64 C or less, else D or A", which 06 section 14.5 allows.

## Readiness criteria

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | `validate_docs.py` exits 0 on this record | Yes | Run with this record at `4ef04ee`: the record passes (see Commands); the 8 failing records at that commit are other records, unchanged by this record |
| R2 | Section A only | N/A | The product is a trade study |
| R3 | Sections 1 to 9 filled, section 10 empty | Yes | TS-011 lines 17 to 347 filled; section 10 (lines 349 to 356) has empty fields |
| R4 | Author's return names the decision need and gate | Yes | Author summary in the brief ("The build candidate is C1 ... C1 and D ... tie at 295 of 500 ... Not robust"); header row "Decide by: PDR (B1b owner session, Thu 2026-10-01, OD-10 and OD-38 final)" |

## B. Trade study (06 section 16, items 1 to 10)

| Id | Answer | Evidence |
|---|---|---|
| CK-RSK-B1 | Yes | Header "Decision class trigger": 06 section 14.1 class 1 items (a) enclosure concept (named verbatim in 06 line "architecture choice (... enclosure concept)"), (c) HZ-001, 002, 003, 006, 007, 009, 013, (d) owner request. Decision maker Robin; gate PDR, B1b, OD-10 and OD-38 |
| CK-RSK-B2 | Yes | Section 3.1: enhancing C1 to C8 each with an operational definition and a 1 to 5 scale; C6 and C8 carry 1 / 3 / 5 anchors with the stated halfway rule (line 71); M1 to M9 pass or fail. "Criteria considered" (line 73) covers safety (M3, M4, M8, M9), first power-on (C8, with the reason the enclosure does not gate it), cost (C1, C7), schedule (C2), performance margin (C3, C4, C5) and system security (omitted: no attack surface). Mandatory definitions off the requirement text: finding-3 |
| CK-RSK-B3 | Yes | 25 + 15 + 15 + 10 + 10 + 10 + 10 + 5 = 100, integers (also asserted by `trade_matrix.py`); rationale section 3.3 per weight, citing the owner's "cheapest option" quote (status note section 2); "No weight was set by the owner directly". Route sub-matrix 30 + 25 + 20 + 25 = 100 |
| CK-RSK-B4 | Yes | Families A, B, C, D of the SRR minutes; C split by heat path into C1, C2, C3; C1e computed for information; pruned: option B route "machining-to-drawing service" with reason; do-nothing is A (ADR-008 baseline). Routes Ra, Rb, Rc plus the CNC engraving route, as the plan lists them |
| CK-RSK-B5 | No | Every enhancing cell has a value, score, confidence and evidence (section 4.2, 24 rows); every score was checked against its anchor: C1 cost 280 / 140 / 150 gives 1 / 2 / 2; C2 about 17 d / 3 d / 5 d gives 1 / 5 / 4; C3 13.6 / 2.5 / 6.5 K gives 4 / 1 / 2 (thermal CSV `margin_112_k` 13.6, 2.5, 6.5); C4 66.3 / 9.5 / 9.3 dB gives 5 / 1 / 1 (`shielding.csv`); C5 >= 5 / 3.0 / 3.0 gives 5 / 3 / 3; C7 USD 280 and 17 d gives 1, USD 23 and 2 to 3 d gives 4. Defects in the mandatory cells: M4 and M8 of C1 (finding-1, finding-2), M1 and M5 definitions (finding-3), the accessible-surface basis of M4 (finding-6) |
| CK-RSK-B6 | Yes | Recomputed by hand: A = 25 + 15 + 60 + 50 + 50 + 30 + 10 + 15 = 255; C1 = 50 + 75 + 15 + 10 + 30 + 50 + 40 + 25 = 295; D = 50 + 60 + 30 + 10 + 30 + 50 + 40 + 25 = 295. Route: Ra = 150 + 125 + 100 + 100 = 475; Rb = 60 + 50 + 60 + 50 = 220; Rc = 30 + 25 + 60 + 75 = 190. Equal to section 5 and to `trade_matrix.py --check` (exit 0, output byte-identical to the frozen `trade-matrix.txt`) |
| CK-RSK-B7 | No | Items 1 to 6 of section 6 are present and follow 06 section 14.4: 16 weight runs (5 change the rank, re-checked for C2 +10: rescale factor 75/85, C1 = 2 x 25 x 0.882 + 5 x 25 + ... = 319.1, as printed), Low-cell runs (17 rank-changing moves), verdict Not robust, value of information with cost and gate, method limitations (lumped model, slab model, FDM planning values, class B libraries, no quotes). Defects: the mandatory M4 condition is left out of the sensitivity and the value-of-information arithmetic is wrong (finding-1); the Low-cell count (finding-4) |
| CK-RSK-B8 | No | Section 7: ten risks in the four-part format with L, C, driving dimension and band; bands recomputed on the 06 section 8 table (4 x 3 = 12 Red; 3 x 3 = 9, 3 x 2 = 6, 2 x 3 = 6, 4 x 2 = 8 Yellow; 2 x 5 = 10 Red by the safety override, 06 section 7 rule 2). Defects: the heat-sink likelihood (finding-1) and the M9 step (finding-5). Register requests name RSK-006, RSK-007, RSK-053, TPM-001 and the CR-003 candidates; the register is written only by WP-PDR-18 (plan section 5.3) |
| CK-RSK-B9 | Yes | Section 8 presents C1 and D together at the 295 tie (06 section 14.5, Not robust and 0 points apart) and states the reasons for leading with C1 (owner direction in the CR-003 CON-015 text, verified at CR-003 line 168: "an H2C-printed PETG case with a conductive coating and a heatsink is built and evaluated first"; evidence cost; correction step). A at 255 is 40 points behind and is the held fallback. The item passes as a form; its basis is weakened by finding-1 |
| CK-RSK-B10 | Yes | Section 9 "None recorded"; section 10 fields empty. The reviewer's disagreement is with two mandatory screen cells (finding-1, finding-2), not with the ranking; if the author keeps the unconditional C1 recommendation after the fixes, 06 section 14.5 requires this disagreement in the Dissent section |

## Plan output coverage (rule C7, WP-PDR-27 TS-011 outputs)

| Plan output | Where in TS-011 | Result |
|---|---|---|
| Options C build, A held, B and D paper only | sections 3.2, 8 | Present |
| Mandatory set REQ-SYS-102, 103, 105, 107 to 113, 116, 117, 124, 168, 175, 177, 191 (17 ids) | M1 (102, 103), M2 (105, 107, 175), M3 (108, 110, 111, 168), M4 (112, 113), M5 (109, 177), M6 (116, 117), M7 (124, 191) | Present, all 17; definitions of M1 and M5: finding-3 |
| PETG heat-deflection margin at peak wall and boss temperature and at +60 C storage | M8 | Storage present (69 - 60 = 9.0 K); boss and wall near the PA missing: finding-2 |
| Coating research: published surface resistivity, adhesion to PETG, thickness, cure, service temperature, one recommended product | Appendix B.1 to B.4 | Present for 843AR (resistivity 0.02 to 0.05 ohm/sq at 25 to 50 um, adhesion "PETG to be confirmed on a coupon", cure 24 h, -40 to +120 C), six other products; recommended 843AR. Every value is recalled, not read (no download permitted; OD-18, OD-21, OD-25, OD-39); the study says so and lists the datasheets for the owner (B.3). Not a finding: the owner permissions are outside the author's control; the values cannot close a TBR until read (rule C10) |
| OD-38 route criterion with its own sensitivity row; routes (a), (b), (c); CNC engraving | sections 3.6, 4.3, 5, 6 items 1 and 2 | Present; route sub-matrix Robust (re-run: no perturbation changes Ra) |
| Per route: REQ-SYS-124 and 191 verification, legibility under the coating, cost line, lead time against 10-01 to 10-04, release package content | section 4.3 table (6 rows by 4 routes) | Present |
| Accessible-surface set of the 12 mm finger on the assembly model, to WP-PDR-28 | section 8 rule 4, E5 only | Missing: finding-6 |
| Proposed values: REQ-SYS-102, 103, 105, 106, 107, 114, 115, 116, 117, 139, 168, 177, 109, 191, finger size | section 8 "Proposed values" (15 rows) | Present, all 15 |
| Durability plan for the legend, jack markings and every other marking with the pre-build coupon rub (TC-SYS-114 note) | section 4.3 (coupon of the legend, jack-marking and facade areas in the same filament pair; exterior never coated); section 8 rule 11 | Present |

## Independent checks (evidence for B5 to B7)

- **Thermal chain.** Steady junction at 45 C for C1: 45 + 4.1 x (5.5 + 0.3 + 3.0 + 4.7 + 1.0 + 0.74) = 45 + 4.1 x 15.24 = 107.5 C (study 107.5). A: 45 + 4.1 x (2.6 + 0.5 + 9.44) = 96.4 C. D: 45 + 4.1 x (3.3 + 0.8 + 9.44 + 0.74) = 103.5 C. B at 1.6 mm: 45 + 4.1 x (2.9 + 0.8 + 3.0 + 7.6 + 1.0 + 0.74) = 110.8 C. All equal the CSV. Pass threshold for C1: 6.11 K/W (finding-1). TS-004 line: at 1.6 mm 107.5 + 4.1 x 2.9 = 119.4 C, as stated.
- **B dropped on the 1.6 mm board.** The study applies SRR decision 87's "else 1.6 mm" branch to a slot-mounted board; CR-003 line 157 states the same reading ("a slot-mounted board (option B, a paper fallback only) falls in the 'else 1.6 mm' branch"). Accepted.
- **Transient.** C1 hot-node time constant 5.5 K/W x 50 g x 0.896 J/(g K) = 246 s; the guard node at 5 min, 28.8 C, is the accessible maximum (the hot node is hidden by the guard); C1e 41.4 C. Consistent with the plot.
- **Route and main matrices.** Recomputed above (B6); weight C4 +10 puts A first (282.2), re-checked.
- **Reproduction.** `git archive 70a3a33 hardware/sim/enclosure hardware/enclosure docs/reviews/PDR/figures` into the scratchpad; `thermal_screen.py --check`, `envelope_drawing.py --check`, `trade_matrix.py --check` each exit 0 with `CHECK PASS`; the regenerated `thermal-screen.csv`, `trade-matrix.txt`, `ts011-thermal-screen.png` and `board-outline-envelope.png` hash to the frozen blobs (byte-identical).
- **Citations.** 47 CFR 15.23(b) (corpus: 47cfr-15.23.md, eCFR issue 2026-09-23) exists and reads "good engineering practices"; SE HB 6.8.1.2.1 mandatory screening and Table 6.8-1 are the template's basis; CR-003 section 6.4 re-check of revision 3 exists (lines 392 to 420, 0 Major, 5 Minor).

## Visual closure

Two renders opened with the Read tool:
- `docs/reviews/PDR/figures/ts011-thermal-screen.png`: the left panel shows the hottest accessible face against time for the seven cases, with the 48 C line and the 5 min marker labelled; the right panel shows the steady junction per option against the dashed 110 C line, with the TS-004 footer. The values agree with the CSV (C1 108 rounded, B 111, C2 130, C3 125). The curves for A, B, C3 and D start above 25 C at t = 0 because the heat-entry node adds P x r_spread at once, which is conservative.
- `docs/reviews/PDR/figures/board-outline-envelope.png`: the plan view gives the board 130 x 62 on six bosses, the holder keep-out, the heat sink 40 x 58 and the PA pad; the X-Z section gives the Z stack, the heat sink below the board through the back wall, and the guard at -10 mm on the REQ-SYS-103 line. The label arrow "board 130 x 62 x 1.0 mm" points at a boss rather than the board edge, and the section's X axis runs to 200 mm with empty space. Both are cosmetic and not findings.

## Items N/A

CK-RSK-A1 to CK-RSK-A11 and readiness R2 (the product is a trade study, not the register).

## Cross items for the lead SE (not findings on TS-011)

- **X-1.** Status note 2026-09-27 sections 6 to 8 (commits `4ef04ee` and `96dcca9`, after the freeze; section 8 supersedes section 6 where they differ): the first complete radio costs under USD 200 all in (firm); size is negotiable; listed-price parts only; a Morse-code audio menu and no display; a JLCPCB bare board soldered by the owner. Each can move this study: C1's first-case cost of about USD 140 against the USD 200 cap for the whole radio, the PCBWay port block ordered with the board (section 8 rule 6), the ITO display window (rule 8, shielding window term), the envelope and mass criteria if size is traded, and the WP-PDR-04 quotes in value of information item 4. These are later owner inputs, not defects of the frozen study, so no finding; the rule C8 re-check before F1, and the fixes of finding-1 and finding-2, should be made on the new constraints.
- **X-2.** The thermal numbers are the author's screen; `analysis-thermal-budget.md` (WP-PDR-28) supersedes them. Finding-1 and finding-2 should be carried into the WP-PDR-28a brief (heat-sink threshold, boss and board-facing wall temperatures, and the 85 C sensor inhibit against the 110 C junction through the same chain: at 5.5 K/W the heat sink runs about 40 K below the junction).
- **X-3.** The software assurance pair is required (07 section 2.1.1; criticality safety-critical, set here because the study fixes the heat-sink node REQ-SYS-181 senses and the chain the REQ-SYS-118 threshold relies on). The lead SE may overrule the criticality with a reason in this record.
- **X-4.** Appendix A.3 reports that the design reader report cited by the plan (items 10, 11, 22, 23, 40, 43, 95, 96) is not in the repository. The reviewer's search found none either. This is for the plan owner.

## Commands

- `git rev-parse HEAD:<path>` and `git hash-object <path>` at `4ef04ee` for the 9 product files: equal to the blobs above.
- Scratchpad export of `70a3a33`: `.venv/bin/python hardware/sim/enclosure/thermal_screen.py --check` exit 0; `envelope_drawing.py --check` exit 0; `trade_matrix.py --check` exit 0; outputs byte-identical to the frozen blobs.
- `.venv/bin/python tools/validate_docs.py`: this record passes (see the return for the totals).

## Measurements (SWE-089)

Items checked 10 (section B) plus readiness 4 and 9 plan-output rows; items answered No 3 (CK-RSK-B5, B7, B8); findings 2 Major, 4 Minor; fixed 0, deferred 0; iteration 1; renders inspected 2; effort about 60 turns and 95 minutes (session shared with INSP-082 to INSP-084).
