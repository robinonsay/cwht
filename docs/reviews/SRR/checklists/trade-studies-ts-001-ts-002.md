---
id: INSP-013
checklist: peer-review-checklist-design
checklist_revision: B
checklist_file: docs/reviews/SRR/checklists/trade-studies-ts-001-ts-002.md
product: docs/decisions/trade-studies/
# product_commit: HEAD of the working tree at review time. Both product files are untracked at
# this commit (git status "??"), so the reviewed content is identified by the blob hashes in the
# "Product files reviewed" table below. Iteration 1 reviewed TS-001 46a8ed17 and TS-002 7b7d165b;
# iteration 2 verified the fixes in TS-001 652ad575 and TS-002 ae80decd (revision 1 of each).
product_commit: "28e49e6"
# product_files: the committed blobs (git rev-parse HEAD:<path> at 400e59d, first committed at e597e49) that the delta verification of 2026-09-26 (iteration 3, R13) approves
product_files: ["docs/decisions/trade-studies/TS-001-receiver-and-pa-concept.md@2a0c40a8d86cc6858e011b735a00ff4cd7e54caf", "docs/decisions/trade-studies/TS-002-firmware-runtime-make-buy.md@574cee3dda830327b0aa17af361f863da2bc546c"]
product_size: 2 trade studies (revision 1: TS-001 686 lines, TS-002 361 lines), 3 plus 1 decision matrices
sprint: SRR-prep
author_agent: "author:trades (Claude trade study author invocation, 2026-09-25, named as Recommender in both TS headers)"
reviewer_agent: "reviewer:trades"
criticality: neither
assurance_required: false
assurance_reviewer_agent: none
iteration: 3
readiness_met: true
reviewer_verdict: APPROVED
assurance_verdict: not-required
verdict: APPROVED
findings_major: 2
findings_minor: 9
findings_open: 0
findings_fixed: 0
findings_verified: 10
findings_deferred: 1
assurance_findings_major: 0
assurance_findings_minor: 0
assurance_tasks_applied: []
deferred_rids: []
# items_no: iteration 1 answered No on CK-DES-H1, CK-DES-H4, CK-RSK-B3, B5, B7, B8 and B10;
# every one is Yes in iteration 2 (section "Closure (iteration 2)")
items_no: []
# effort: iteration 1 48 turns and 55 minutes; iteration 2 20 turns and 25 minutes
effort_turns: 74
effort_minutes: 95
record_status: Open
date: 2026-09-25
date_closed: null
---

# Peer review record INSP-013: trade studies TS-001 and TS-002

**Checklist:** `docs/templates/peer-review-checklist-design.md` revision B, sections A, B and H as `docs/process/08-agent-briefing.md` section 3.1 assigns to trade studies, with the other sections marked N/A. By assignment the decision-analysis criteria of `docs/process/06-risk-and-decision-analysis.md` section 14 are applied as well. They are applied as the ten trade-study items of 06 section 16, under the ids 06 section 16 gives them (`CK-RSK-B1` to `B10`). The minimum content judged is SRR entrance row 5 (`docs/process/01-lifecycle-and-reviews.md` section 4.3: alternative concepts analyzed, with a trade summary giving criteria and scores), SRR success criterion 8 (01 section 4.4), and the SWE-033 make/buy record (NPR 7150.2D section 3.1.2; section 6.1 item t). **Gate:** SRR, package items H5 and H14 (`docs/reviews/SRR/package.md` section 2). **Answer legend:** Yes = Pass, No = Fail, N/A = not applicable. Every answer carries its evidence.

**Search-first compliance:** `mcp__claude-context__search_code` was run on `/Users/robinonsay/rust/cwht` before any manual search. The queries covered the SRR H5 and H14 shortfalls with SWE-033, and the Inrad and KVG filter data with the ladder Monte Carlo. `grep -n` was used afterwards only to pin the lines the hits pointed to. Known paths were read directly.

**Criticality and assurance:** `assurance_required: false` because the single dispatch rule, the table of `docs/process/07-software-engineering-plan.md` section 2.1.1, has no trade-study row. However, the TS-002 header asks for an `assurance_reviewer_agent`, because the runtime drivers are in the call path of the 07 section 14.1 components. No assurance reviewer was dispatched with this review. The conflict goes back to Claude as a process issue (see finding-9 for the product side). This reviewer did check, as evidence, the three SWEHB `swe-033` section 7.1 tasks (items S3 to S5 below), but that check does not replace the assurance function's confirmation.

**Process note (not a product finding).** Both TS headers name their reviewer record as `checklists/ts-00N-<slug>.md`, filled from `peer-review-checklist-risk.md` section B. That is the rule of 06 sections 14.2, 14.3 step 6 and 16, and of 01 section 13. This assignment instead combines both studies in one record at this path and names the design checklist. The 06 section 16 items are applied in full below, so no check is lost. The slug and checklist choice, and the header edits it implies, are returned to Claude.

## Product files reviewed

`git status --short docs/decisions/trade-studies/` shows `??`: neither file is committed. Blob hashes are from `git hash-object` on 2026-09-25.

| File | Blob | Lines | Result | Findings that apply |
|---|---|---|---|---|
| TS-001-receiver-and-pa-concept.md | 46a8ed17b3df8419aa353490855f69ed757912a8 | 613 | Fail | 1 to 7 |
| TS-002-firmware-runtime-make-buy.md | 7b7d165b5f98397b38493921cc056f7ef47cf7ac | 361 | Fail (Minor only) | 8 to 10 |
| TS-001-receiver-and-pa-concept.md, revision 1 (iteration 2) | 652ad57554aaf7d077b4e19de99a87d746981fc0 | 686 | Pass | 1 to 7 Verified |
| TS-002-firmware-runtime-make-buy.md, revision 1 (iteration 2) | ae80decd6cb429dc00da5b52e40ce4b9cec93414 | 361 | Pass | 8 to 10 Verified |

## Numbers verified against their sources

**Recomputation.** The Appendix A.3 script of TS-001 was extracted verbatim and run with `.venv/bin/python`, together with a report wrapper. It reproduces every total and sensitivity figure quoted in TS-001 sections 5 and 6, TS-002 sections 5 and 6, and the TS-001 A.3 results table:

| Matrix | Totals | Smallest lead under weight perturbation | Smallest lead under Low-cell perturbation | All Low cells against the leader |
|---|---|---|---|---|
| R2 | A 400, B 330 | 20.5 (C7 +10, C9 +10) | 60 | A 390, B 340 |
| P | P1 460, P3 280, P4 265, P2 195 | 152.5 (C1 -10) | 170 | P1 460, P3 300, P4 285, P2 205 |
| P fallback | P3 280, P4 265, P2 195 | 2.9 (C6 +10) | 5 | P4 285, P3 250, P2 205 |
| P fallback, value-of-information case (P2 C1 = C2 = 3) | P3 280, P2 275, P4 265 | | | |
| TS-002 | A0 400, A1 265, A2 220, A3 220 | 80.6 (C3 +10) | 115 | A0 400, A1 355, A2 310, A3 295 |

The script's weight and score dictionaries match the matrices of the two studies cell by cell. The Low-cell lists (`lowR`, `lowP`, `lowF`) match the Low confidence tags in the scoring tables.

**Additional recomputations by this reviewer** (same functions):

- R2 with A-C3 = 3 gives A 370, B 330. With A-C3 = 1 it gives A 340, B 330, inside the 25-point closeness rule of 06 section 14.5 (finding-1).
- R2 with B-C1 = 2 gives B 310 (finding-7).
- R2 with C4 weight 15 (the others rescaled) gives A 404.8, B 323.8.
- P with C3 and C5 at weight 15 (the others rescaled) gives P1 459.1, P3 277.3, P4 263.6, P2 200.0 (finding-5).
- TS-002 with C2 and C4 at weight 0 (the others rescaled) gives A0 387.5, A1 293.8, A2 237.5, A3 237.5 (dissent D-2).

**Source checks, correct as written:**

- 47 CFR 97.307(e) (corpus `47cfr-97.307.md` line 25): 25 uW and at least 40 dB below, for a transmitter of 25 W or less. 10 log10(5 / 25e-6) = 53.0 dB.
- `requirements.json` values: REQ-SYS-012, 017, 018, 022, 024 to 030, 033, 094, 103, 112, 137, 140 and 147. There are 18 `priority: KDR` rows.
- MOE-001 to 007, 010 and 013 titles match their use.
- TPM-002 SRR history is `red` (cbe -189). RSK-008 has score 20. RSK-001, 005, 006, 027, 038 and 047 have score 12.
- `cw-selectivity-options.md`: F2 (XF-90S52-LF 1.0 kHz, 60 dB at +/-1.3 kHz, IL 5.0 dB, BF-01 19.4 mm); F3 (#111 400 Hz, shape factor 2.0, USD 118); F8 (4-pole 1.0 kHz: IL 3.5 / 4.8 / 6.6 dB, att. 46 / 39 dB, 98.5 % strict yield; 500 Hz 4-pole 14.5 %, 6-pole 0.0 %); F12 (PCM1808 USD 0.5687 at 10, LCSC 28,195); F13 (-47 dBm); F1 (-39 dBm at 1 km); F16 (LT5517 about 35 dB, 90 mA); F18 current ranges.
- `pa-turnkey-candidates-followup.md`: F2, F3 (RthJC 3 C/W, 20:1), F5 (-70 dBc max at 5 W; 4.5 to 5.0 W at 6.0 V), F8 (Mouser 3,430, DigiKey 1,988, USD 6.16 and 6.63 at 10), F9 (9.6 to 10.6 W; 9 to 12 C), F12, F14 (Mouser 7,409, USD 4.59), F15, F17 (a) and (b) stock and prices, F19, F20 (GVA-84+ USD 2.99).
- Anchor interpolations, recomputed: P1 C3 = 3.5, rounded to 4; P1 C6 = 4.6, rounded to 5; P4 C6 = 1.8, rounded to 2; R2 A-C4 = 4.7, rounded to 5; R2 B-C4 = 2.3, rounded to 2; B-C2 = 4.5, rounded to 4.
- C7 multiples of the 25-piece quantity: 137x, 80x, 296x, 15x, 28x and 53x are as stated.
- `rustos-toolchain-proof.md`: F2 (0 tests), F4 (2,008 B flash, 8,200 B RAM), F6 (13 clippy warnings, 71 rustfmt hunks, `unsafe` lines 11 plus 42), F13 (2 host tests).
- `/Users/robinonsay/rust/rustos/README.md` lines 44 to 47 quoted correctly. There is no LICENSE file at the rustos root, and rustos HEAD is `c54d35a`.
- 07 section 19: 12 work packages plus optional WP-SW-13, nine of them with Needed-by FW-B1.
- ADR-019 section 3 rows B, C and D.
- Corpus identifiers: SE-23 at NPR 7123.1D section 3.2.18.1; App. G Table G-3 item 5.2 "Alternative concepts that have been analyzed"; SWE-033 at 3.1.2; SWE-027 at 3.1.14; SWE-146 at 3.8.1; SWE-211 at 4.5.14; NPR 7150.2D section 6.1 item t (`06-chapter6.md` line 51); SWEHB `swe-033` section 7.1 tasks 1 to 3; `swehb/7-03-acquisition-guidance.md` exists; SE HB `22-6-8-decision-analysis.md` (sections 6.8.1.2.1 to 6.8.1.2.7, Table 6.8-1 at line 370).
- Risk bands of section 7 in both studies against the 06 section 8 matrix: correct in every row.

**Source checks, incorrect or unsupported:** findings 1, 2, 3, 4 and 6.

## Readiness criteria (design checklist R1 to R4)

| # | Answer | Evidence |
|---|---|---|
| R1 | N/A | Neither study produces a figure (TS-001 A.4: "Figures: none produced"). The cited Monte Carlo plots belong to `docs/research/` |
| R2 | N/A | Trade studies have no `design_refs`. Requirement traceability is checked under CK-RSK-B2 and S1 instead |
| R3 | N/A | The studies are inputs to the SRR baseline, and the L1 requirements are still Draft. Both studies cite TBR values by requirement id |
| R4 | Yes | The author summary lists the H5 and H14 scope and the template sections kept. All 20 template headings are present in both files (`grep -n "^#"` against `docs/templates/trade-study.md`) |

`readiness_met: true`. The tools were run before the review: `validate_docs.py` exit 1 on `docs/design/allocation.json` only (schema missing, outside this product); `traceability.py --report-only` exit 0; `render_risk.py --check --gate SRR --hazards` exit 0.

## Participants

Author agent absent (author:trades). Reviewer agent reviewer:trades. No software assurance reviewer (see "Criticality and assurance" above). The owner dispositions the findings, and rules on SRR decisions 54, 55 and 58 with the studies.

## A. Architecture content (SWE-057 note; NPR 7150.2D section 4.2.2)

| Id | Answer | Evidence |
|---|---|---|
| CK-DES-A1 to A8 | N/A | A trade study selects an architecture family and a device. It does not define software components, quality attributes, interfaces, states or the concurrency model. TS-002 section 2 names the affected components (`api`, `pico2`, the 07 section 14.1 modules), and this is consistent with 07 section 1.2 |

## B. Traceability (SWE-052 Table 1; charter section 7)

| Id | Answer | Evidence |
|---|---|---|
| CK-DES-B1, B3, B4 | N/A | No design units |
| CK-DES-B2 | N/A | No software control is allocated. The hazards touched are named: TS-001 names HZ-003 and HZ-008, and TS-002 names HZ-001 to 005, 007 and 014. All exist in `hazards.json` with matching titles |
| CK-DES-B5 | N/A | Not a CR |

## C to G

| Id | Answer | Evidence |
|---|---|---|
| CK-DES-C1 to C15, D1 to D13, E1 to E4, F1 to F3, G1, G2 | N/A | No software design content. TS-002 section 2 lists the SWE-027 and SWE-211 obligations that would fall on bought code, which is what G1 and G2 will later check |

## H. Consistency and presentation

| Id | Answer | Evidence |
|---|---|---|
| CK-DES-H1 | No | TS-001 P M1 omits the driver device, which ADR-012 section 2 makes a mandatory-criterion part (finding-3). TS-001 recommends P2 as a fallback candidate against REQ-SYS-112 (finding-2) |
| CK-DES-H2 | N/A | No figures |
| CK-DES-H3 | N/A | The 500-line limit binds design files that have an index file. The trade-study template is one file with fixed section numbers. TS-001 has 613 lines and TS-002 has 361 (`wc -l`) |
| CK-DES-H4 | No | Several citations misread their sources: implication 12, Kuhne F7, power-tree F23, RSK-058 status and the drop list (findings 1, 4 and 6). All corpus identifiers exist (see the verification section) |

## Sections I and J

| Id | Answer | Evidence |
|---|---|---|
| CK-DES-I1 to I8, J1 to J10 | N/A | Not an ICD or a hardware design product |

## 06 section 16 trade-study items (decision-analysis criteria of 06 section 14)

| Id | TS-001 | TS-002 | Evidence |
|---|---|---|---|
| CK-RSK-B1 (class rule; decision maker and gate stated) | Yes | Yes | TS-001 cites class 1 (a), (b) and (c), owner, PDR. TS-002 cites class 1 (h) and (c), owner, SRR |
| CK-RSK-B2 (operational definitions and anchors; mandatory pass/fail; "Criteria considered" covers all six dimensions) | Yes | Yes | TS-001 3.1: R2 C1 to C9 and P C1 to C9 with 1/3/5 anchors, and a Criteria considered list with system security omitted for a reason. TS-002 3.1: C1 to C7 with the same, cost omitted for a reason. R1 has mandatory criteria only (see finding-4) |
| CK-RSK-B3 (integer weights summing to 100 with rationale) | No | Yes | All sums are 100. TS-001 3.3 states a weight rule that three rows do not follow and does not explain why (finding-5) |
| CK-RSK-B4 (decision space covered; do-nothing present or explained; pruned listed) | Yes | Yes | TS-001: 4 families, 2 selectivity candidates plus 4 pruned, 7 PA candidates plus 7 pruned, and the do-nothing option explained for R2. TS-002: A0 to A3 plus 5 pruned; do-nothing is rustos as it stands, explained in 3.2. The R1 pruning rule is covered by finding-4 |
| CK-RSK-B5 (every cell links evidence and carries a confidence) | No | Yes | Every cell has an F-number and a confidence. TS-001 A-C3 (Medium) and B-C1 do not follow from their evidence, and the A M1 pass rests on a misread (findings 1 and 7). TS-002 mandatory M3 for A1 to A3 is passed without the license text being read (finding-8, Minor) |
| CK-RSK-B6 (totals recompute) | Yes | Yes | See the recomputation table |
| CK-RSK-B7 (06 section 14.4 statement, including limitations; verdict consistent) | No | Yes | TS-001 R2 is declared Robust while its decisive cell A-C3 is excluded from the score sensitivity, and A-C3 = 1 puts A and B within 25 points (finding-1). TS-002 items 1 to 6 are complete and consistent |
| CK-RSK-B8 (risks of every surviving alternative in four-part format on the 06 scales) | No | Yes | TS-001 section 7 has 17 rows with correct bands. The P2 thermal row understates an exceedance of REQ-SYS-112 as "approaching its limit" (finding-2), and P1 has no driver-gain risk (finding-3). TS-002 has 9 rows with correct bands |
| CK-RSK-B9 (recommendation is the highest total, or the deviation is explained) | Yes | Yes | R2 A 400, P P1 460 and TS-002 A0 400 are each the highest. The P fallback is presented as a closely ranked set per 06 section 14.5, and the difference from package decision 58 is flagged in TS-001 8.3 |
| CK-RSK-B10 (Dissent present; Decision section empty) | Yes | No | Both have a Dissent section ("None recorded"). TS-002 section 10 carries author text, "Proposed revisit triggers" (finding-10) |

## SRR minimum content and SWE-033

| Id | Check | Answer | Evidence |
|---|---|---|---|
| S1 | SRR entrance row 5: at least one concept-level TS covering receiver architecture family and PA topology, with a trade summary of criteria and scores | Yes, content present; not yet acceptable | TS-001 R1 (4 families), R2 (weighted matrix) and P (weighted matrix, 7 candidates). The row is met in scope. The two Major findings must close before the study supports the interim rulings on decisions 54 and 58 |
| S2 | SRR success criterion 8: evaluation criteria identified and prioritized; existing assets considered (G-3 s4, s9) | Yes | Weighted criteria with MOE and KDR drivers. Existing assets considered: the STEVAL-TDR003V1 reference design, the RA07M1317M module, the Kuhne transverter module (F-D), the commercial filters, and rustos (TS-002 A0) |
| S3 | SWE-033 options a to f of NPR 7150.2D section 3.1.2 (SWEHB `swe-033` section 1.1) addressed; component-level make/buy disposition | Yes | TS-002 section 2 option table and component table (runtime, application logic, LCD driver, `core`, toolchain, host tools, emulator). 07 section 17.2 scoring items are all present; SI-007 is used as the decision rule, which 3.1 explains |
| S4 | SWEHB `swe-033` section 7.1 task 1 (options evaluated) and task 3 (risks of the decision assessed) evidenced | Yes | TS-002 sections 3 to 7. The confirmation belongs to the assurance function (finding-9) |
| S5 | SWEHB `swe-033` section 7.1 task 2 (flow-down of SE, SA and safety requirements to acquisition) evidenced | Yes | TS-002 section 7 cites SWE-027 a to f and SWE-211 for A1 to A3, and the full 07 process for A0 |
| S6 | NPR 7150.2D section 6.1 item t record identified | Yes | TS-002 header "Decision class trigger" row |

## Findings

| Finding | Origin | Severity | Item | Location | Description | State | Deferred to | Disposition |
|---|---|---|---|---|---|---|---|---|
| F-01 | reviewer | Major | CK-RSK-B5, B7 | TS-001 section 4 R2 M1 row A; C3 row A; section 6 item 4 | Candidate A's mandatory M1 pass and its C3 = 5 rest on an untoleranced nominal value and a misread of implication 12. The R2 "Robust" verdict depends on that unperturbed cell | Verified | | Closed: TS-001 section 4 R2 mandatory row A (conditional pass, implication 12 read correctly as a 250 Hz post-detector position, F15); C3 row A scored 1, Low, in `lowR` of A.3; section 6 items 2 and 4 (Not robust); 8.3 closely ranked A 330, B 310. Re-run by this reviewer: A 330, B 310, seven weight flips, all-Low tie 320/320 |
| F-02 | reviewer | Major | CK-DES-H1, CK-RSK-B8 | TS-001 3.1 P M1 to M4; section 4 P2 M4; section 7 P2 thermal row; 8.3; 8.4 decision 58 | P2 (GRF5604) is recommended as a fallback candidate although its own evidence puts Tj above the REQ-SYS-112 KDR value. No mandatory criterion screens REQ-SYS-112 | Verified | | Closed: TS-001 3.1 P M5 (REQ-SYS-112 screen); section 4 P2 M5 fail (45 + 80 = 125 C against 110 C, followup F15); section 7 P2 thermal row L4 x C4 = 16 Red (06 section 6 row 4 and section 7 row 4 anchors); 8.3 and 8.4 decision 58 name P3 then P4 and state the two re-entry routes |
| F-03 | reviewer | Minor | CK-DES-H1, CK-RSK-B8 | TS-001 3.1 P M1; section 4 P1 M2; section 7 | ADR-012 makes the driver a mandatory-criterion part. P1's M2 evidence is for the line-up with the obsolete PD84001, and the replacement driver is "marginal" (followup F20); no risk row covers it | Verified | | Closed: TS-001 3.1 P M1 covers final and driver (ADR-012 section 2); section 4 P1 M1 driver stock and M2 conditional on the TS-003 driver budget (followup F5, F20, ACTION 18); section 7 P1 drive-margin row, 9 Yellow, under RSK-027 (Proposed, "PA output power below the 5 W requirement") |
| F-04 | reviewer | Minor | CK-RSK-B4, CK-DES-H4 | TS-001 3.1 M-R1; 3.2 F-A and F-B rows | F-A passes M-R1 without the "published measured design" its operational definition requires. F-B passes both mandatory criteria but is pruned unscored with four alternatives. The Kuhne image-rejection figure is misquoted | Verified | | Closed: TS-001 3.1 M-R1 widened to admit a front-end filter analysis with confidence and a PDR evidence item; 3.2 F-A row (Low, ideal Butterworth figures reproduced by this reviewer: 47.0, 49.9, 78.3, 94.0 dB); F-B dominance argument with numbers (battery 19.4 to 16.7 h reproduced); Kuhne F7 now "at least 60 dB", only the Anglian F6 above 70 dB |
| F-05 | reviewer | Minor | CK-RSK-B3 | TS-001 3.3 | The stated weight rule ("KDR together with an MOE gets 15 to 20") is not applied to R2 C4, P C3 or P C5, and no exception is given | Verified | | Closed: TS-001 3.3 rule paragraph names the four exception rows and the table gives a reason for R2 C4, P C3 and P C5; weight-15 totals reproduced (A 339.4, B 303.9; P1 458.8, P3 276.2, P4 263.1) |
| F-06 | reviewer | Minor | CK-DES-H4 | TS-001 8.4 decision 55; 3.3 R2 C4 row; 8.4 decision 58 | Three source misreadings: the LNA-alone battery-life claim, the RSK-058 status, and a drop list that disagrees with 3.2 | Verified | | Closed: (a) 8.4 decision 55 now changes only the LNA in the F23 model (19.4 to 14.2 h, 13.0 to 10.4 h, reproduced against the F23 script); (b) 3.3 R2 C4 row says RSK-058 Proposed at 12 (`register.json`); (c) 3.2 prunes AFT05MS003N (followup F10) and the 8.4 drop list carries AFT09MS007N |
| F-07 | reviewer | Minor | CK-RSK-B5 | TS-001 section 4 R2 C1 row B | B-C1 averages the two sides of the channel (39 and 46 dB) as if they were a range. The worse side scores 2 | Verified | | Closed: TS-001 section 4 R2 C1 row B scores the worse side, 39 dB, as 2 (2.2 interpolated); section 5 B-C1 = 2 |
| F-08 | reviewer | Minor | CK-RSK-B5 | TS-002 section 4 M3 rows A1 to A3 | The mandatory license criterion is passed on "assumed from general knowledge, not read" | Verified | | Closed: TS-002 section 4 M3 rows A1 to A3 cite crates.io license fields; this reviewer read the same API records on 2026-09-25 (rp235x-hal 0.4.0, cortex-m-rt 0.7.7, embassy-rp 0.10.0, rtic 2.3.1 "MIT OR Apache-2.0"; rp235x-pac 0.2.0 BSD-3-Clause, in the `firmware/deny.toml` allow list); transitive crates recorded as not assessed in section 6 item 3 |
| F-09 | reviewer | Minor | CK-DES-H1 | TS-002 section 7 "Software assurance tasks"; header "Independent reviewer" row | The author declares SWEHB `swe-033` tasks 1 to 3 met, task 1 by a review record that did not exist yet. Confirmation is the assurance function's (charter section 2) | Verified | | Closed: TS-002 section 7 now reads "Evidence offered" for tasks 1 to 3 with the confirmation left to an assurance record; the header row refers the dispatch question to Claude. The 07 section 2.1.1 question itself stays a process item for Claude (not a product defect) |
| F-10 | reviewer | Minor | CK-RSK-B10 | TS-002 section 10 | The Decision section carries author content ("Proposed revisit triggers") before the owner decides | Verified | | Closed: TS-002 section 10 is empty; the proposed revisit triggers are in section 8 |

### finding-1

<a id="finding-1"></a>**F-01, Major, Verified (iteration 2).**

**What the study says.** TS-001 section 4 passes candidate A on M1 (REQ-SYS-024: -6 dB bandwidth 400 to 600 Hz, TBR) because "#111 400 Hz sits at the lower edge of the 400 to 600 Hz window". It adds that "XF-90S52-LF is 1.0 kHz and needs the optional audio filter of implication 12 to reach 500 Hz. Either way a path exists".

**What the sources say.**

- `cw-selectivity-options.md` implication 12 describes that audio filter as an "optional Hi-Per-Mite-class audio filter for a 250 Hz narrow position". F15 gives it 200 Hz at 3 dB, after the detector.
- So the KVG path does not produce a 400 to 600 Hz channel. Only the Inrad #111 path remains.
- #111's nominal 400 Hz is exactly the lower limit, and its tolerance and termination are unquoted (F3: "termination impedance is not on the web page (open item)"; TS-001 C3 row: "centre tolerance not yet quoted").

**Effect on the score.**

- C3 measures the "fraction of assembled units meeting the M1 set". A part whose nominal value sits on the limit cannot be scored 5 (at least 98 %) at Medium confidence on this evidence.
- Recomputed with the A.3 functions: A-C3 = 3 gives A 370. A-C3 = 1 gives A 340 against B 330, inside the 25-point closeness rule of 06 section 14.5.
- Because A-C3 is tagged Medium, it is excluded from the score sensitivity. The section 6 item 4 "R2 is Robust" verdict therefore rests on the one cell the evidence does not support.

**Expected fix.**

1. Correct the implication-12 reading.
2. Make A's M1 a conditional pass pending the Inrad bandwidth tolerance and termination (quote, package decision 101), or state that the REQ-SYS-024 lower limit must move by CR.
3. Retag A-C3 as Low, add it to `lowR`, and re-run section 6. If the result falls within 25 points, present A and B as closely ranked. The planning-baseline wording of 8.1 and decision 54 can stand if it says so.

**Citation:** 06 sections 14.4 item 2 and 14.5; `cw-selectivity-options.md` F3, F15, implication 12; REQ-SYS-024.

### finding-2

<a id="finding-2"></a>**F-02, Major, Verified (iteration 2).**

**The conflict.** REQ-SYS-112 (priority KDR, TBR) reads: "hold the PA junction at or below 110 C (TBR) during continuous key-down at the 5 W step in 45 C ambient". TS-001's own evidence for P2 conflicts with it:

- followup F15, quoted in section 4 P2 M4 and C4: "a junction rise of about 80 C, Tj about 140 C at a 60 C package base".
- Even with the package base at the 45 C ambient, Tj is about 125 C.

**How the study treats it.**

- None of P M1 to M4 screens REQ-SYS-112. M4 uses the 190 C device limit instead.
- The section 7 P2 thermal row says "approaching its limit ... adversely impacting REQ-SYS-112" at likelihood 3, but on the study's estimate the requirement value is exceeded, not approached.
- 8.3 and 8.4 then recommend naming P2 among the fallback candidates in the decision 58 interim ruling. They also present the value-of-information case (P2 at 275, "level with P3 at 280") without stating that P2 cannot meet REQ-SYS-112 as written.
- Package decision 58 lists REQ-SYS-112 among its affected requirements, so the owner would rule without seeing the conflict.

**Expected fix.**

1. Add a mandatory criterion for REQ-SYS-112, or state in 8.3 that selecting P2 needs either a CR on REQ-SYS-112 or a thermal design, with evidence, that brings stage-2 Tj to 110 C or below at 45 C ambient.
2. Re-rate the P2 thermal risk (an exceedance statement, with likelihood 4 or 5 on the 06 section 6 anchors).
3. Update 8.3 and 8.4 so the owner sees the conflict before ruling on decision 58.

**Citation:** REQ-SYS-112; followup F12, F15; 06 sections 6, 13 item 2; package section 13.1 decision 58.

### finding-3

<a id="finding-3"></a>**F-03, Minor, Verified (iteration 2).**

**The gap.** ADR-012 section 2 reads: "The PA final device and its driver device are mandatory-criterion parts in the PA trade study". TS-001 P M1 screens the "Final device" only. P1's M2 pass cites the STEVAL-TDR003V1 result ("5 W at the 6.0 V pack cut-off with 10 dBm drive", followup F5). That figure is for the two-stage line-up with the PD84001 driver, which F5 reports is no longer available. The stocked replacements (GVA-84+, PGA-103+) are "marginal if the PD54008L-E final has only 14 to 17 dB of gain at 144 MHz" (F20). Section 7 carries no driver or drive-margin risk for P1.

**Expected fix.**

1. Extend P M1 to the driver, as ADR-012 requires. GVA-84+ passes on stock (F20).
2. Mark P1's M2 as conditional on the driver gain budget of the PDR TS-003.
3. Add a four-part P1 risk for drive margin in section 7.

**Citation:** ADR-012 section 2; followup F5, F20; 06 section 13 item 2.

### finding-4

<a id="finding-4"></a>**F-04, Minor, Verified (iteration 2).**

**The problems.**

1. M-R1 is defined as "At least 70 dB image and IF rejection ... by a published measured design of the family". F-A is passed on "crystal-IF superhets are the reference pattern" (reference report implication 13). Implication 13 gives no image-rejection value, and the reference report gives none for a 9 MHz IF single-conversion design at 144 MHz.
2. F-B passes both M-R1 and M-R2 but is "pruned before scoring". 06 section 14.3 step 2 provides for pruning with a trade tree "if more than five" alternatives; R1 has four. The dominance argument ("F-B carries every R2 cost plus a conversion") is reasonable but not quantified.
3. F-B's pass cites "image rejection above 70 dB in the Anglian and Kuhne designs (F6, F7)". Reference report F7 gives the Kuhne MKU 144 G2 "spurious rejection min 60 dB". Only the Anglian (F6) is above 70 dB.

**Expected fix.**

1. Cite a measured image rejection for a single-conversion design with an IF near 9 MHz, or add a front-end filter analysis with a confidence tag and a PDR evidence item.
2. Either score R1 or state the dominance argument with numbers (LO current, parts count) and the rule that admits it.
3. Correct the Kuhne figure.

**Citation:** `2m-cw-transceiver-reference-designs.md` F6, F7, implication 13; 06 section 14.3 step 2.

### finding-5

<a id="finding-5"></a>**F-05, Minor, Verified (iteration 2).**

**The inconsistency.** TS-001 3.3 states: "A criterion that moves a KDR together with an MOE gets 15 to 20; one that moves a single KDR or a top register risk gets 10". Its own driver table breaks the rule in three rows, with no stated exception:

- R2 C4 (MOE-004 and REQ-SYS-094, a KDR): weight 10.
- P C3 (MOE-004 and REQ-SYS-094): weight 10.
- P C5 (MOE-010 and REQ-SYS-022, a KDR): weight 10.

R2 C2 has an explicit exception. R2 C9 is covered by the general "envelope fit gets 5" sentence.

**Effect.** Recomputed with those three weights at 15: R2 gives A 404.8, B 323.8; P gives P1 459.1, P3 277.3, P4 263.6, P2 200.0. No rank changes.

**Expected fix:** state the exception per row, or restate the rule to match the weights.

**Citation:** 06 section 14.3 step 1; section 16 trade-study item 3.

### finding-6

<a id="finding-6"></a>**F-06, Minor, Verified (iteration 2).**

Three source misreadings:

- **(a) Decision 55.** 8.4 says "The LNA choice alone moves the receive-only life from 19.4 h (low build) toward 8.3 h (high build) (`power-tree-and-charging.md` F23)". The two F23 rows differ in the LO (Si5351 against ADF4351 class), the LNA (30 mA against PGA-103+) and the backlight (none against 40 mA) together, so the LNA's share is not stated.
- **(b) RSK-058 status.** 3.3 says "RSK-058 is open at 12". `register.json` gives RSK-058 score 12 with status Proposed.
- **(c) Drop list.** The decision 58 drop list in 8.4 names AFT05MS003N, which is not among the 3.2 alternatives or pruned parts (it appears only in followup F10). It omits AFT09MS007N, which 3.2 prunes.

**Expected fix:** correct the three statements, or add the missing dispositions.

**Citation:** `power-tree-and-charging.md` F23 table; `docs/risk/register.json` RSK-058; followup F10, F16.

### finding-7

<a id="finding-7"></a>**F-07, Minor, Verified (iteration 2).**

**The problem.** R2 C1 is "Attenuation of a signal 2 kHz from the channel centre". B's cell reads "39 dB (-2 kHz) and 46 dB (+2 kHz), 5th percentile" and scores 3. That matches the midpoint rule applied to 42.5 dB. The two numbers are the two sides of the channel, not an uncertainty range. A signal on the weaker side sees 39 dB, which interpolates to 2.2 and rounds to 2.

**Effect.** Recomputed: B 310, with no rank change.

**Expected fix:** score the worse side, or state why the average represents the operational definition.

**Citation:** TS-001 3.1 scoring rule; `cw-selectivity-options.md` F8 table.

### finding-8

<a id="finding-8"></a>**F-08, Minor, Verified (iteration 2).**

**The problem.** TS-002 section 4 passes A1 to A3 on M3 (license) with "permissive license assumed from general knowledge, not read". A mandatory criterion is a screen, and a pass needs evidence (SE HB section 6.8.1.2.1; charter section 11 rule 2). The ranking is unaffected, because the three alternatives are kept and lose on the enhancing criteria.

**Expected fix:** read the license fields of the three projects (crate metadata, which needs no crate download), or record M3 as "not assessed; assumed pass; no effect on the ranking" in section 6 item 3.

**Citation:** 06 section 14.3 step 4; SE HB section 6.8.1.2.1.

### finding-9

<a id="finding-9"></a>**F-09, Minor, Verified (iteration 2).**

**The problem.** TS-002 section 7 states, for example, that "Task 1 (confirm the options were evaluated) is met by sections 2 to 5 and by the independent review record". It declares SWEHB `swe-033` section 7.1 tasks 1 to 3 met. Those are confirmations by the software assurance function (charter section 2; the SWEHB tab is headed "Tasking for Software Assurance"), and the review record did not exist when the text was written. The TS-002 header also requires an `assurance_reviewer_agent`, but 07 section 2.1.1, the single dispatch rule, has no trade-study row.

**Expected fix:**

1. Reword the text as "evidence offered for tasks 1 to 3", with the confirmation left to the assurance reviewer's record.
2. Claude resolves whether the assurance review is required (07 section 2.1.1 row, or delete the header claim).

**Citation:** charter section 2; `swehb/swe-033-acquisition-vs-development-assessment.md` section 7.1; 07 section 2.1.1.

### finding-10

<a id="finding-10"></a>**F-10, Minor, Verified (iteration 2).**

**The problem.** TS-002 section 10 carries "Proposed revisit triggers for the owner to adopt with the decision", with four bullets. The template comment for section 10 says "Filled only by transcription of the owner's decision ... Left empty until then". 06 section 16 trade-study item 10 requires the Decision section to be empty until the owner decides.

**Expected fix:** move the proposed triggers to section 8 and leave section 10 empty.

**Citation:** `docs/templates/trade-study.md` section 10 comment; 06 sections 14.5, 14.6, 16 item 10.

## Dissent (for the Dissent sections of the studies, 06 section 14.5)

- **D-1 (TS-001 P fallback).** This reviewer agrees that the fallback cannot be ranked today. However, once finding-2 is applied, P2 can only be a fallback together with a REQ-SYS-112 CR or a thermal design. That makes the package decision 58 default (GRF5604 as the fallback) harder to support than the study's joint recommendation suggests.
- **D-2 (TS-002 criteria independence).** C1 (external crate count), C2 (register auditability) and C4 (unsafe surface) all grow with the amount of third-party code in the image, and together they carry 40 of the 100 weight points. The study does not discuss this dependence. Recomputed with C2 and C4 removed and the rest rescaled: A0 387.5, A1 293.8. The recommendation stands.

## Verdict (iteration 1; superseded by "Closure (iteration 2)" below)

```
VERDICT: NEEDS CHANGES
FINDINGS:
- [Major] CK-RSK-B5/B7 TS-001 section 4 R2 A M1 and C3: pass and score rest on an untoleranced nominal and a misread of implication 12; robustness depends on the unperturbed cell.
- [Major] CK-DES-H1/CK-RSK-B8 TS-001 P2: recommended fallback candidate exceeds REQ-SYS-112 on the study's own Tj estimate; no mandatory screen.
- [Minor] CK-DES-H1 TS-001 P M1: driver omitted against ADR-012; P1 M2 evidence uses the obsolete driver.
- [Minor] CK-RSK-B4 TS-001 R1: F-A M-R1 evidence missing; F-B pruned unscored; Kuhne misquoted.
- [Minor] CK-RSK-B3 TS-001 3.3: weight rule not applied to R2 C4, P C3, P C5.
- [Minor] CK-DES-H4 TS-001 8.4 and 3.3: power-tree F23, RSK-058 status, drop list.
- [Minor] CK-RSK-B5 TS-001 R2 C1 B: two-sided average scored as a range.
- [Minor] CK-RSK-B5 TS-002 M3: license passed unread.
- [Minor] CK-DES-H1 TS-002 section 7: assurance tasks declared met by the author.
- [Minor] CK-RSK-B10 TS-002 section 10: author content in the Decision section.
ITEMS N/A: CK-DES-A1 to A8, B1 to B5, C1 to C15, D1 to D13, E1 to E4, F1 to F3, G1, G2, H2, I1 to I8, J1 to J10 (trade study products)
MEASUREMENTS: size=2 studies (974 lines, 4 matrices); turns=48; minutes=55; major=2; minor=8
```

## Closure (iteration 2, 2026-09-25)

**Re-review scope.** The author reported F-01 to F-10 fixed and none disputed. The reviewer (`reviewer:trades`, new invocation, same role; did not edit the product) opened revision 1 of both studies (TS-001 blob 652ad575, 686 lines; TS-002 blob ae80decd, 361 lines) and checked each fix against its source. Search first: `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any `grep` (query: TS-001 candidate A conditional pass, P2 GRF5604 REQ-SYS-112 mandatory criterion). `grep -n` then pinned lines in `cw-selectivity-options.md` (F2, F3, implication 12, ACTION 15), `2m-cw-transceiver-reference-designs.md` (F1, F2, F6 to F8, implication 13), `pa-turnkey-candidates-followup.md` (F5, F10, F14, F15, F20, ACTIONs 15 to 18), `power-tree-and-charging.md` F23, 06 sections 6 and 7, and package section 13.1 decision 101.

**Recomputation.** Both listings of TS-001 Appendix A.3 were extracted verbatim and run with `.venv/bin/python` (exit 0). Every total and sensitivity figure in TS-001 sections 3.3, 5, 6, 8.3 and 8.4 and in the A.3 results table is reproduced: R2 A 330, B 310, seven weight flips (C1 -10, C3 +10, C4 -10, C5 -10, C7 +10, C8 +10, C9 +10), smallest remaining lead 6.7 (C2 +10), no Low-cell flip (smallest lead 10), all Low cells against the leader A 320, B 320; A-C3 = 3 or 5 gives A 360 or 390; A-C8 = 2 gives A 340; P P1 460, P3 280, P4 265 (152.5, 170; 460/300/285); fallback P3 280, P4 265 (2.9, 5; P4 285, P3 250); P2 re-entry 195 or 275; TS-002 A0 400, A1 265, A2 220, A3 220 (80.6, 115; 400/355/310/295). The weight-15 cases of TS-001 3.3 were recomputed with the same functions: A 339.4, B 303.9; P1 458.8, P3 276.2, P4 263.1. The second listing reproduces the Butterworth figures of section 3.2 and A.3 and the battery figures of 3.2 and 8.4 (19.4/13.0, 16.7/11.7, 14.2/10.4 h), and its F23 inputs (180 mA low build, 150 mA bias, 1.20 A PA, 0.45 key factor) match the F23 script of `power-tree-and-charging.md`.

**Dispositions.** Closed (Verified): F-01 to F-10, each with its evidence in the Disposition column of the findings table. Disputed accepted: none (nothing was disputed). Open: none.

**Iteration 2 answers** (items answered No in iteration 1):

| Item | Answer | Evidence |
|---|---|---|
| CK-DES-H1 | Yes | F-02, F-03 and F-09 closed: P M1 covers the driver as ADR-012 section 2 requires; P2 is no longer offered as a fallback against REQ-SYS-112; TS-002 section 7 offers evidence and leaves confirmation to the assurance function |
| CK-DES-H4 | Yes | F-01, F-04 and F-06 closed: implication 12, Kuhne F7, power-tree F23, RSK-058 status and the drop list now match their sources |
| CK-RSK-B3 (TS-001) | Yes | F-05 closed |
| CK-RSK-B5 | Yes | F-01, F-07 and F-08 closed: A-C3 1 (Low), B-C1 on the worse side, M3 of A1 to A3 on read license metadata |
| CK-RSK-B7 (TS-001) | Yes | F-01 closed: A-C3 is in the Low-cell run and the R2 verdict is Not robust, with A and B presented as closely ranked (06 section 14.5) |
| CK-RSK-B8 (TS-001) | Yes | F-02 and F-03 closed: the P2 thermal row states an exceedance at 16 Red; the P1 drive-margin row is in four-part form at 9 Yellow |
| CK-RSK-B10 (TS-002) | Yes | F-10 closed: section 10 empty in both studies; TS-001 and TS-002 section 9 record dissent D-1 and D-2 |
| CK-RSK-B9 | Yes (re-checked) | R2 A 330 is the highest total and is presented with B as a closely ranked pair; P P1 460 highest; the fallback departure from package decision 58 is explained in TS-001 8.3 |
| S1 | Yes | The two Major findings are closed, so TS-001 supports the interim rulings on decisions 54, 55 and 58 |

**Observations (not findings; for the author, no effect on the ranking).**

- TS-001 section 4 A M1 and section 6 item 5 ask the Inrad quote for the -6 dB bandwidth tolerance. `cw-selectivity-options.md` ACTION 15 names only the termination impedance and case drawing, so the tolerance question should be written into the package decision 101 correspondence when it is sent.
- TS-001 3.2 F-A calls the family the "FT-290R and IC-202 pattern" with an IF near 9 MHz. Those radios use 10.81 and 10.7 MHz (reference report F1, F2). The study already carries 10.7 MHz as an IF sub-choice, and a 10.7 MHz IF moves the image further from the signal, so the Low-confidence M-R1 pass is not weakened.

**Process items returned to Claude (unchanged from iteration 1, not product findings).** (1) The record path and checklist choice against the 06 section 14.2 slug rule. (2) Whether TS-002 needs a software assurance review: 07 section 2.1.1 has no trade-study row, while the TS-002 header asks for one (F-09 part 2).

**Tool runs (iteration 2).**

| Command | Exit | Result |
|---|---|---|
| `.venv/bin/python tools/validate_docs.py` | 1 | 27 passed, 1 failed, 28 checked; this record PASS as a peer_review_record; the only failure is `docs/design/allocation.json` ("schema not found: docs/design/allocation.schema.json"), outside this product |
| `.venv/bin/python tools/traceability.py --report-only` | 0 | 231 requirements, 167 test cases, 0 violations, 42 warnings; none names TS-001 or TS-002 |
| `.venv/bin/python tools/render_risk.py --check --gate SRR --hazards docs/safety/hazards.json` | 1 (run twice) | "HZ-008: related_risk_ids does not name RSK-046, which carries it"; outside this product (no RSK-046 row is cited by either study) |

Counts: 10 findings, 10 Closed (Verified), 0 Disputed accepted, 0 Open; open Major 0, open Minor 0.

```
VERDICT (iteration 2): APPROVED
FINDINGS: none open (F-01 to F-10 Verified)
MEASUREMENTS: size=2 studies (1,047 lines, 4 matrices); verified=10; open=0; major_open=0; minor_open=0; iteration=2; turns=20; minutes=25
```

`record_status` stays `Open` for the lead SE to set `Closed` with `date_closed` once every finding is Verified or Deferred, which is now the case.

## Delta verification (iteration 3, 2026-09-26, SRR package items R13, H5 and H14)

**Scope.** Iteration 2 approved the working-tree blobs TS-001 `652ad575` and TS-002 `ae80decd`, which are not in the git object store, so the difference to the committed files cannot be shown by `git diff`. The committed files are TS-001 blob `2a0c40a8` and TS-002 blob `574cee3d` (`git rev-parse HEAD:<path>` at `400e59d`; first committed at `e597e49`). The verifier is the integrator invocation of 2026-09-26, which did not author either study (charter section 11 rule 4). Search first: `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any `grep`.

| Check on the committed blobs | Result |
|---|---|
| Size equals the approved revision 1 (TS-001 686 lines, TS-002 361 lines; product_size above) | Yes: 686 and 361 lines |
| Both TS-001 Appendix A.3 listings extracted verbatim (lines 571 to 637 and 645 to 655) and run with `.venv/bin/python` | Exit 0 both; every total and sensitivity figure of the iteration 2 recomputation is reproduced: R2 A 330, B 310, seven weight flips, smallest remaining lead 6.7, all Low A 320, B 320; P P1 460, P3 280, P4 265 (152.5, 170); fallback P3 280, P4 265 (2.9, 5); A-C3 3 or 5 gives A 360 or 390; A-C8 2 gives A 340; P2 re-entry 195 or 275; TS-002 A0 400, A1 265, A2 220, A3 220 (80.6, 115); filter and battery figures (19.4/13.0, 16.7/11.7, 14.2/10.4 h) as in the A.3 results table |
| F-01, F-07: A-C3 1 (Low), B-C1 scored on the worse side | TS-001 line 346 (C3 row, A 1) and line 277 (B-C1, 39 dB on the worse side, score 2); revision table line 686 |
| F-02, F-03: P M1 covers the driver; P M5 added for REQ-SYS-112 | TS-001 line 83 (M1 names final and driver device, ADR-012 section 2) and line 676 (P M5 added) |
| F-08: TS-002 M3 license criterion | TS-002 line 86 (M3 mandatory, pass/fail on the license terms) |
| F-10: section 10 empty; dissent in section 9 | TS-001 lines 517 and 523, TS-002 lines 314 and 320: section 10 reads "Empty until the owner decides" with blank fields |

<a id="finding-11"></a>**finding-11, Minor, Lien: fix before PDR.** Location: TS-001 and TS-002 header "Status" row. Both committed Status lines still read "awaiting the reviewer's verification of the fixes", although INSP-013 approved revision 1 at iteration 2 and this delta verification confirms the committed blobs (package section 15 item 60). Fix: the trade study author updates both Status lines. Disposition under the convergence rule of 2026-09-26: Lien, fix before PDR, carried by the package as a Routine item.

**Lien table.**

| Finding | Severity | Disposition | Owner | Due |
|---|---|---|---|---|
| finding-11 | Minor | Lien: fix before PDR | Trade study author (Claude) | PDR readiness declaration |

**Result.** The committed blobs carry the revision 1 content that iteration 2 verified; no Major finding. Findings: 11, of which 10 Closed (Verified) and 1 Lien. The process items returned to Claude at iteration 2 (the record path and the TS-002 software assurance record) are unchanged and remain in package H1 (c).

```
VERDICT (iteration 3, delta verification): APPROVED (with liens)
PRODUCT: TS-001@2a0c40a8d86cc6858e011b735a00ff4cd7e54caf, TS-002@574cee3dda830327b0aa17af361f863da2bc546c
FINDINGS: finding-11 Minor, Lien: fix before PDR
MEASUREMENTS: verified=10; lien=1; open_major=0; iteration=3; turns=6; minutes=15
```
