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
# product_commit (iteration 2): 70d11ef, the WP-PDR-27 revision 1 commit that fixes finding-1 and finding-2
# (re-freeze F0, rule C2). Every blob below equals git rev-parse 70d11ef:<path>, HEAD:<path> and git
# hash-object <path> at HEAD d1148c2; all are on main. product_files_iteration_1 keeps the 70a3a33 blobs.
product_commit: "70d11ef54a5bc477cda9e9fa01e7295e1365f147"
product_blob: 16fc3d6bce1d74d56ecb9642300ce054ece8421f
# product_files: the study and the WP-PDR-27 files it scores from (revision 1 adds board_field_thermal.py and
# its outputs); the two analysis notes and drop_and_axial.py have their own records (INSP-083, INSP-084)
product_files: ["docs/decisions/trade-studies/TS-011-enclosure.md@16fc3d6bce1d74d56ecb9642300ce054ece8421f", "hardware/enclosure/board-outline.json@9d4d36a984b07456a4860c6f1d6354297b42808d", "hardware/sim/enclosure/thermal_screen.py@78892ca27ace63c1bbd5965b730b0ccd6e85ab53", "hardware/sim/enclosure/envelope_drawing.py@5de2223bfedb3d45734cf066eeccf3df28629b0a", "hardware/sim/enclosure/trade_matrix.py@c76b0f70d05a64c282a9066204a64ffe1e217fde", "hardware/sim/enclosure/board_field_thermal.py@12b7e3d63cd0ef2921dd80f040a3526b8080cd19", "hardware/sim/enclosure/out/thermal-screen.csv@a8c7d5b1b5f345172a036b590342f67b0adcc273", "hardware/sim/enclosure/out/trade-matrix.txt@c6023d697716d2c024c0033948aaeaa3aa3b7c0e", "hardware/sim/enclosure/out/board-field-thermal.csv@2462fc4d9aad8d75c2ba452d9446b067ddea5316", "docs/reviews/PDR/figures/ts011-thermal-screen.png@47d81e61ee7039b3126158c577170af30686752a", "docs/reviews/PDR/figures/board-outline-envelope.png@a2c08e0ef04ec036465ddeb9bd2f6a16d7fb5dfe", "docs/reviews/PDR/figures/ts011-board-field-thermal.png@4751eaeddafafaa921d97b3e2dd1c33f0e97f0f7"]
product_files_iteration_1: ["docs/decisions/trade-studies/TS-011-enclosure.md@8d2708f1b0175d73945b7ee32d9d49937f4a51e9", "hardware/enclosure/board-outline.json@27dbacc7dda7f79e6cba3234ee77f6453e304906", "hardware/sim/enclosure/thermal_screen.py@78892ca27ace63c1bbd5965b730b0ccd6e85ab53", "hardware/sim/enclosure/envelope_drawing.py@20815e7581c34c9498e6c8d3972cc738e5c63e8a", "hardware/sim/enclosure/trade_matrix.py@c76b0f70d05a64c282a9066204a64ffe1e217fde", "hardware/sim/enclosure/out/thermal-screen.csv@a8c7d5b1b5f345172a036b590342f67b0adcc273", "hardware/sim/enclosure/out/trade-matrix.txt@c6023d697716d2c024c0033948aaeaa3aa3b7c0e", "docs/reviews/PDR/figures/ts011-thermal-screen.png@47d81e61ee7039b3126158c577170af30686752a", "docs/reviews/PDR/figures/board-outline-envelope.png@ff8aa6c2befd4660f2bf353893ab5673d24f79e3"]
product_size: 6 alternatives (A, B, C1, C2, C3, D; B, C2, C3 dropped at the mandatory screen), 9 mandatory and 8 enhancing criteria; route sub-matrix of 3 routes and 4 criteria; 22 rank-changing perturbations
sprint: PDR-prep
author_agent: "author:WP-PDR-27 wave 1a (Claude as ME designer)"
reviewer_agent: "reviewer:WP-PDR-27-ts-011-iter1 (independent; authored no part of WP-PDR-27); iteration 2 by reviewer:WP-PDR-27-ts-011-iter2 (independent; authored no part of WP-PDR-27 and no part of its revision 1)"
# criticality: TS-011 selects the PA-to-ambient heat path and the heat sink whose temperature REQ-SYS-181
# senses and against which the SW-SAFE thermal unit thresholds (REQ-SYS-118, 155) act (07 section 14.1 row
# "Thermal protection", safety-critical, HZ-003)
criticality: safety-critical
assurance_required: true
assurance_reviewer_agent: "pending (separate invocation; paired record docs/reviews/PDR/checklists/ts-011-enclosure-software-assurance.md)"
iteration: 2
readiness_met: true
# reviewer_verdict (iteration 2): APPROVED; finding-1 and finding-2 (Major) Verified; findings 3 to 6 and the new
# findings 7 and 8 are Minor and Open (liens due at the CDR readiness declaration, plan rule C1)
reviewer_verdict: APPROVED
# assurance_verdict: pending the iteration 2 delta of the software assurance pair INSP-087 (its finding-1, Major,
# is fixed in TS-011 revision 1 rule 14 and is verified by a separate assurance invocation, not by this reviewer)
assurance_verdict: pending
# verdict: held at NEEDS CHANGES until the SA pair INSP-087 returns APPROVED (07 section 2.1.1; rule C9); that
# pair applies the software-assurance template that is still only on cr/CR-012 (blob 5b135285), so under the
# lead SE convention of 2026-09-27 the lead SE sets this verdict when both hold
verdict: NEEDS CHANGES
findings_major: 2
findings_minor: 6
findings_open: 6
findings_fixed: 0
findings_verified: 2
findings_deferred: 0
deferred_rids: []
items_no: [CK-RSK-B5, CK-RSK-B7, CK-RSK-B8]
effort_turns: 100
effort_minutes: 160
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

## Iteration 2: delta verification of finding-1 and finding-2 (Major) (2026-09-27, HEAD `d1148c2`)

**Scope (rule C1).** Iteration 2 is a delta that verifies the fixes of finding-1 and finding-2 only. Findings 3 to 6 (Minor) were not addressed by the author (TS-011 change log, revision 1 row), except the M5 definition that the INSP-083 fix rewrote, and are not re-reviewed. Product: the 12 blobs of front matter `product_files`, committed as `70d11ef` (TS-011 revision 1, re-freeze F0). Each equals `git rev-parse 70d11ef:<path>`, `git rev-parse HEAD:<path>` and `git hash-object <path>` (12 of 12). `git log 70d11ef..HEAD` shows no later change to any product file. No blob is on a `cr/` branch. Checklist as iteration 1: `peer-review-checklist-risk.md` revision A, section B (on main). The fix of INSP-087 finding-1 (rule 14, the K9 sensing point) is in the same revision; it is verified by the separate software assurance invocation of INSP-087, not here (rule C4, 07 section 2.1.1).

**Independence (rule C4).** This invocation authored no part of WP-PDR-27 and no part of revision 1. It edited no product file.

**Search first (charter section 11 rule 1).** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (WP-PDR-27 records; the owner's thermocouple, OQ-VV-003 and owner-actions E-02). `grep` then only pinned lines in known paths (TS-011, the plan, the clock plan). The rustos tree was not read.

**Reproduction.** On a `git archive 70d11ef` export in the scratchpad: `thermal_screen.py --check`, `trade_matrix.py --check`, `envelope_drawing.py --check` and `board_field_thermal.py --check` each exit 0 with `CHECK PASS` (the board model takes about 18 s). The regenerated `thermal-screen.csv`, `trade-matrix.txt`, `board-field-thermal.csv`, `ts011-thermal-screen.png`, `board-outline-envelope.png` and `ts011-board-field-thermal.png` hash to the frozen blobs (6 of 6 byte-identical).

### Verification of finding-1, case by case (rule C7)

| # | Case the finding named | Check | Result |
|---|---|---|---|
| 1 | M4 made conditional on the in-situ heat-sink resistance, threshold stated | TS-011 section 1 finding 1, section 4.1 C1 M4 cell ("conditional (Low), threshold 6.11 K/W"), heat-sink table row 6.11 K/W at 110.0 C, section 8 conditions table row 1, `board-outline.json` `in_situ_thermal_resistance_max_k_per_w` 6.11. Hand: (110 - 45) / 4.1 - 9.74 = 6.114 K/W; `board_field_thermal.py` item 1 prints 6.11 | Yes |
| 2 | Most of the author's 5.5 to 9 K/W range fails; midpoint value | Section 1 and section 6 item 2 say so; 7.25 K/W gives 45 + 4.1 x 16.99 = 114.7 C (script 114.7); 9.0 K/W gives 121.8 C (script 121.8) | Yes |
| 3 | The mandatory condition enters the sensitivity (06 section 14.4 item 2) and the robustness verdict | Section 6 item 2 "Mandatory-screen sensitivity": above 6.11 K/W C1 leaves the matrix and D leads A; section 6 item 4 and section 1 robustness line state the mandatory screen is not robust | Yes |
| 4 | (a) value of information: C3 score 2 threshold | Section 6 item 5: 4.89 K/W. Hand: (105 - 45) / 4.1 - 9.74 = 4.894 K/W; the C3 anchors (section 3.1: 2 at >= 5 K, 3 at >= 8 K) give 4.89 and 4.16 K/W, as the new heat-sink table shows. Between 4.89 and 6.11 C1 stays at 295, stated | Yes |
| 5 | (b) the 80 % duty claim from REQ-SYS-055 | Withdrawn in section 1 finding 1 and below the section 4.1 heat-sink table, with the reason (REQ-SYS-055 sets no off-time); the 80 % column is removed from TS-011. The frozen `thermal_screen.py` still prints its 80 % duty line (unchanged script, iteration 1 output) but TS-011 no longer cites it | Yes |
| 6 | (c) the unsourced 1 K/W guard penalty and the catalog part | Section 8 rule 3 withdraws it and states a model (`board_field_thermal.py` item 2): free-air radiation from the envelope less the base face, in situ only the fin-tip face radiating through the 0.67 open fraction, convection fraction 0.7 to 0.9 (Low). Reviewer hand run: h_rad = 5.93 W/(m2 K) at 55 C to 25 C, envelope 0.00683 m2, radiative conductance 0.0405 W/K, convective 0.1817 W/K for a 4.5 K/W part; in situ 7.33 / 6.47 / 5.79 K/W at 0.7 / 0.8 / 0.9 (script identical). Catalog value needed for 6.11 K/W: 3.83 to 4.71 K/W (script), 4.28 K/W at 0.8 in `board-outline.json`. "No part of 40 x 58 x 23 mm is shown to reach it" is stated, and the in-situ measurement before the case is committed is added (rule 3; method: new finding-7, Minor) | Yes |
| 7 | Heat-sink risk likelihood | Section 7 row C1 heat sink: L4 (50 to 80 %) x C3 = 12 Red, with the reason and the mitigation (rule 3 measurement); the aggregate line updated. The new filament risk row (L3 x C3 = 9 Yellow) is consistent with the 06 section 8 table | Yes |
| 8 | Recommendation states the condition and the fallback (06 section 14.5) | Section 1 and section 8: C1 "on three conditions", condition 1 with threshold, the step that settles it, when, and the fallback (A; D on paper with a CON-015 change and condition 2). Section 8 rationale adds that on the author's estimates the fallback to A is the more likely outcome. Section 9 records the reviewer's disagreement as resolved in the study | Yes |
| 9 | The board model does not move the threshold the wrong way | `board_field_thermal.py` with the whole line-up (4.1 W plus 1.0 to 2.3 W and 0.3 W) gives Tj 94 to 107.7 C at 6.11 K/W (CSV `tj_max_c` 107.7), below the screen's 110.0 C, because the board sheds heat laterally; the screen threshold is the conservative one and is the one used. The reproduction case (no lateral loss) gives 107.48 C against the screen's 107.48 C (script line "reproduction") | Yes |

**Result: finding-1 Verified.**

### Verification of finding-2, case by case (rule C7)

| # | Case the finding named | Check | Result |
|---|---|---|---|
| 1 | M8 evaluated at the printed bosses that carry the board | Section 3.1 M8 definition (revision 1) names the bosses and the walls; section 4.1 M8 bound table. CSV: C1 at 6.11 K/W boss with the screw on the copper 81.4 C central, 94.0 C worst; C1 at 5.5 K/W 79.7 / 91.9 C; D 83.1 / 93.7 C. The boss is taken at the board temperature at the hole (conservative: the model credits no heat loss into the boss) | Yes |
| 2 | M8 evaluated at the printed walls facing the board | Front wall (and, for C1, the back wall outside the heat-sink footprint) by a local balance with no lateral spreading in the PETG, over a disc of the board-to-wall gap radius: C1 64.8 C central, 58.7 to 72.7 C; D 64.1 C, 58.4 to 71.4 C (CSV). The no-spreading assumption raises the peak, so it is an upper bound as stated | Yes |
| 3 | The board temperature near the PA with the rest of the line-up | Two-layer finite-difference board, 1 mm cells, PA pad nodes tied to the screen's chain, the rest of the RF section at 1.0 or 2.3 W (source stated: 11.4 W DC line-up, `pa-device-candidates.md` F19), 32-case sweep of 5 inputs for C1 and 16 for D; the worst case is the M8 bound. Board 70 to 94 C at the holes (section 4.1 table; plot) | Yes |
| 4 | PETG verdict for C1 and D, and the 5 K rule | PETG limit 69 - 5 = 64 C; every boss fails, the walls fail in the upper half of the sweep: M8 fails for C1 and D in PETG (section 4.1 rows C1 and D). The PA66 standoff variant (insert 50.6 to 56.6 C) passes the bosses but not the walls and is not adopted, with the reason | Yes |
| 5 | The route to a pass | Rule 15: filament HDT at 0.45 MPa of 99 C or more (94.0 + 5); `hdt_needed_c1` 99.0 C, `hdt_needed_d` 98.7 C (CSV). It needs a CON-015 change, named as condition 2 with its fallback (A) and as a CR with its section 6 review before the owner is asked (rule C6) | Yes (the rule 18 posts are outside the bound: new finding-8, Minor) |
| 6 | +60 C storage | Kept: 9.0 K with PETG, larger with the rule 15 filament (section 4.1 C1 M8 cell; proposed values REQ-SYS-115) | Yes |
| 7 | The conditional recommendation the iteration 1 record suggested | Section 8 conditions 1 and 2 with A as the fallback, which is the form iteration 1 said 06 section 14.5 allows | Yes |

**Result: finding-2 Verified.**

### Findings (iteration 2)

| Finding | Severity | Item | Location | Description | State | Deferred to |
|---|---|---|---|---|---|---|
| finding-1 | Major | CK-RSK-B7, B8, B9 | TS-011 sections 1, 4.1, 6, 7, 8 | See iteration 1 | Verified (iteration 2, revision 1 at 70d11ef) | |
| finding-2 | Major | CK-RSK-B5 | TS-011 sections 3.1 M8, 4.1; `board_field_thermal.py` | See iteration 1 | Verified (iteration 2, revision 1 at 70d11ef) | |
| finding-3 | Minor | CK-RSK-B5 | TS-011 section 3.1 M1 (M5 rewritten by the INSP-083 fix) | Not in the delta. The M5 part is now written as TC-SYS-107 reads it, with the not-shown rule; the M1 part stands | Open | CDR readiness declaration (lien) |
| finding-4 | Minor | CK-RSK-B7 | TS-011 section 6 item 2 | Not in the delta ("10 Low-confidence cells" still reads 10; 12 in the table) | Open | CDR readiness declaration (lien) |
| finding-5 | Minor | CK-RSK-B8 | TS-011 section 4.1 M9, section 7 | Not in the delta | Open | CDR readiness declaration (lien) |
| finding-6 | Minor | CK-RSK-B5 | TS-011 section 8 rule 4, M4 | Not in the delta | Open | CDR readiness declaration (lien) |
| <a id="finding-7"></a>finding-7 | Minor | CK-RSK-B7 (value of information) | TS-011 section 8 rule 3 (in-situ measurement) and section 6 item 5 | The measurement that settles condition 1 is not shown to bound the in-situ resistance from above. (a) The power resistor on the heat-sink base loses part of its 4.1 W from its own housing and leads directly to the air; with that heat not passing the heat sink, R = (T_base - T_amb) / 4.1 W reads low, which is the non-conservative direction for a pass at 6.11 K/W. (b) The method names "the owner's thermocouple", but whether the owner has one is open (04 section 6.3 OQ-VV-003; `docs/reviews/PDR/owner-actions.md` row E-02, "Buy unless your multimeter has a thermocouple input"). (c) It runs at room ambient while M4 is at 45 C; the natural-convection resistance at the same rise changes little, but the difference is not stated. Fix: insulate the resistor's exposed faces (or measure its own loss with the heat sink replaced by an insulating block) and state the correction; name OQ-VV-003 or E-02 as a precondition of condition 1; state the ambient effect or bound it | Open | CDR readiness declaration (lien) |
| <a id="finding-8"></a>finding-8 | Minor | CK-RSK-B5 | TS-011 section 4.1 M8 bound and section 8 rules 15 and 18; `board_field_thermal.py` `m8_case` (six holes and the walls only); `board-outline.json` `front_shell_posts` | Rule 18 adds printed front-shell posts that bear on the board, two of them 5 mm from the PA pad edge (board points (100, 18) and (100, 44)), and rule 18 and `board-outline.json` say they are M8 parts that pass with the rule 15 filament. The M8 bound that sets rule 15 (94.0 C, HDT 99 C) covers only the six boss holes and the walls. Reviewer run of the frozen `solve_board` over the same 32-case sweep, taking the maximum board top temperature over each 6 mm post contact: C1 at 6.11 K/W worst 94.1 C at (100, 18) and 93.3 C at (100, 44) (central 83.7 and 82.8 C); D worst 91.6 C. So the post near the PA needs HDT 99.1 C, 0.1 K above the rule 15 value; the other four posts are at 74 to 82 C. No verdict changes at the precision of the model, but the stated bound omits a part the study itself names. Fix: add the rule 18 posts to the M8 set of `board_field_thermal.py` and state the HDT to the next whole degree (100 C), or move the two posts off the PA region | Open | CDR readiness declaration (lien) |

Neither new finding is Major: finding-7 concerns how condition 1 is measured, not whether the condition, the threshold or the fallback is stated; finding-8 moves the rule 15 value by 0.1 K.

### Visual closure (iteration 2)

Three renders opened with the Read tool (renders_inspected 3 in this delta):
- `docs/reviews/PDR/figures/ts011-board-field-thermal.png` (new): two board maps (C1 at 6.11 K/W and D, worst case of the sweep, 45 C, 4.1 W plus 2.3 W), each with the six holes labelled 71, 84, 94 (C1) and 74, 84, 94 (D), the PA pad outlined and, for C1, the heat-sink footprint dotted; the note "whole board above 64 C" (minima 71 and 74 C). The right panel gives the M8 bars per case (boss with the screw on the copper, PA66 standoff variant, wall) with central-input diamonds, the 64 C PETG limit and the 94 C rule 15 limit. The values match the CSV (boss 91.9 / 94.0 / 93.7 C; walls 71.5 / 72.7 / 71.4 C). The front-shell posts are not drawn (finding-8).
- `docs/reviews/PDR/figures/board-outline-envelope.png` (revised): the heat-sink label now reads "<= 6.1 K/W in situ (M4)", the six rule 18 posts are drawn as triangles and NTC-1 and NTC-2 inside the PA pad square, with a legend; the posts at enclosure (105, 22) and (105, 48) match `board-outline.json` board points (100, 18) and (100, 44) with the (5, 4) board offset. The iteration 1 cosmetic points (label arrow to a boss, empty X-Z axis to 200 mm) remain; not findings.
- `docs/reviews/PDR/figures/ts011-thermal-screen.png`: byte-identical to iteration 1, re-opened; unchanged.

### Cross items (iteration 2, returned to Claude)

- X-5. INSP-083 iteration 2 raises a new Major (finding-5: the rule O2 jack-collar credit does not hold with a plug inserted). TS-011 section 1 finding 3, the M5 cells of C1 and D ("every source passes from 12.5 MHz to 1.5 GHz") and condition 3 rest on that analysis and will change with its fix; this record does not raise it again.
- X-6. The record verdict waits for the INSP-087 iteration 2 delta (software assurance invocation), which verifies rule 14, the K9 trip values (CSV rows `k9_option`, 104.3 to 110.3 C at the pad) and the three requests of section 8 "Requests to other writers". This reviewer notes only that the numbers in those rows reproduce.
- X-7. Condition 2 needs a CR on CON-015 (an L0 constraint). The study names it but none is raised; per rule C6 the lead SE raises it with its section 6 impact review before B1b if the owner is to be asked there.
- X-1 to X-4 of iteration 1 still apply (X-1: the owner inputs of status note sections 6 to 8, including the USD 200 cap, before the rule C8 re-check).

### Completion criteria (SWE-088), iteration 2

Reviewer side met: no Major is open, readiness is met (R1, R3 and R4 re-checked at `70d11ef`), and findings 3 to 8 are Minor liens due at the CDR readiness declaration (plan rule C1; PDR package section 15). `reviewer_verdict: APPROVED`. The record `verdict` stays NEEDS CHANGES until the software assurance pair INSP-087 returns APPROVED (07 section 2.1.1; rule C9).

```
ITERATION 2 (2026-09-27, HEAD d1148c2, product commit 70d11ef): REVIEWER VERDICT: APPROVED; RECORD VERDICT: NEEDS CHANGES (held for the SA pair INSP-087)
FINDINGS:
- [Major] finding-1: Verified (M4 threshold 6.11 K/W stated and made a condition with fallback A; C3 score 2 at 4.89 K/W; 80 % duty withdrawn; guard model 1.3 to 2.8 K/W; risk L4 x C3 = 12 Red).
- [Major] finding-2: Verified (bosses 69 to 94 C and walls 58 to 73 C bounded by the board model; PETG fails M8; rule 15 HDT 99 C as condition 2).
- [Minor] finding-3 to finding-6: Open, not in the delta (liens).
- [Minor] finding-7 (new): the rule 3 in-situ measurement reads low (resistor housing loss), assumes a thermocouple (OQ-VV-003) (lien).
- [Minor] finding-8 (new): the rule 18 posts are outside the M8 bound; 94.1 C at the post near the PA (lien).
MEASUREMENTS: blobs equal HEAD 12/12; checkers 4 of 4 CHECK PASS; outputs byte-identical 6/6; cases 16 (16 Yes, 2 with a new Minor); renders inspected 3; major open=0; minor open=6; turns=40; minutes=65 (cumulative 100 and 160); iteration=2
```
