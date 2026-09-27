---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md section 13;
# docs/process/08-agent-briefing.md sections 3.2 and 3.4). Independent review of the WP-PDR-33 UI design
# analysis at the record path PDR work plan WP-PDR-33 "Records" names. Iteration 1 at freeze F0 (rule C2).
# Checklists applied: docs/templates/peer-review-checklist-analysis.md revision A as on its CR-012 branch
# (cr/CR-012-pdr-checklist-templates at 7784672, blob 0386cc6e; CR-012 Submitted, not merged), and for the
# eight renders the items of docs/templates/peer-review-checklist-visual-product.md revision A named in
# section I below. tools/validate_docs.py requires the checklist field to name a template that exists on
# main, so the field names peer-review-checklist-design revision B and checklist_analysis records the
# template actually applied (the INSP-038 and INSP-050 form); the delta after CR-012 merges switches it.
id: INSP-072
checklist: peer-review-checklist-design
checklist_revision: B
checklist_analysis: "docs/templates/peer-review-checklist-analysis.md@0386cc6e78da65578b1cce8b2f793cd3db224921 (revision A, CR-012 branch head 7784672)"
checklist_file: docs/reviews/PDR/checklists/analysis-ui-design.md
product: docs/design/analysis/ui-design.md
# product_commit (iteration 2): 8c12b5a, the WP-PDR-33 revision 2 commit that fixes findings 1 and 2 (freeze F0
# again, rule C2). The 14 blobs below equal git rev-parse 8c12b5a:<path>, HEAD:<path> and git hash-object at
# HEAD 4b51f7f; all are on main. product_files_iteration_1 keeps the 82cf086 blobs.
product_commit: "8c12b5ad9134ce7f3b2605be4a61dc3fac392807"
product_files: ["docs/design/analysis/ui-design.md@90cdbd95f18c0564fece3e0a1e152d820382b3c2", "docs/design/analysis/ui-design/ui_model.py@e554bf0df564b76f5fb936e07a2dc83fca4cdf05", "docs/design/analysis/ui-design/check_ui_design.py@21bc1d9c634b1fe33fe63618ad7c79d011406d0f", "docs/design/analysis/ui-design/ui-design-results.json@ff7128c0d2cdbd78301eb79e331df830d4345c8e", "docs/design/analysis/ui-design/ui-tuning-step-law.png@97abc3c93a538af0630e9acd2e11b11c45db2af9", "docs/reviews/PDR/figures/display-layout-receive.png@9ff2916a2b6db6a445b8fbd06d057e424b849284", "docs/reviews/PDR/figures/display-layout-transmit.png@3243c62dd8c1d4923581fab7f42088054ac76b84", "docs/reviews/PDR/figures/display-layout-tune.png@77112396af22cdf14d9872933ba473a1ae76e9ba", "docs/reviews/PDR/figures/display-layout-key-inhibit.png@420c4a3dd1f8f68bdab5791e43816bf7f4cae91a", "docs/reviews/PDR/figures/display-layout-id-reminder.png@42edfb328a13ee8e1a56098f5efbbf1211dcf0eb", "docs/reviews/PDR/figures/display-layout-menu-level-1.png@6a034579826ac17db38f2c23ab15de15d3563aa2", "docs/reviews/PDR/figures/display-layout-menu-level-2-keyer.png@c4ab87d1f02c40984bc901c111cf0f60bfeddb51", "docs/reviews/PDR/figures/display-layout-menu-level-2-keyer-straight.png@4db31b14d2e931876138e52dafbafbecbf5e7720", "docs/reviews/PDR/figures/display-layout-cal-trim.png@c5b63bc102750ef60b8f43042b5fe8fb291a8895"]
product_files_iteration_1: ["docs/design/analysis/ui-design.md@4ef24520995d037098990ae236a2c8921767e22d", "docs/design/analysis/ui-design/ui_model.py@58ce1f9b98cabab1bce292dca2992b7af7da729c", "docs/design/analysis/ui-design/check_ui_design.py@875e4628f1dce1882fe7ee3e1e65a86399131ed8", "docs/design/analysis/ui-design/ui-design-results.json@8c3b21586be4711ccb2ecd592b6e8a94ffdb3af7", "docs/design/analysis/ui-design/ui-tuning-step-law.png@97abc3c93a538af0630e9acd2e11b11c45db2af9", "docs/reviews/PDR/figures/display-layout-receive.png@9ff2916a2b6db6a445b8fbd06d057e424b849284", "docs/reviews/PDR/figures/display-layout-transmit.png@3243c62dd8c1d4923581fab7f42088054ac76b84", "docs/reviews/PDR/figures/display-layout-tune.png@77112396af22cdf14d9872933ba473a1ae76e9ba", "docs/reviews/PDR/figures/display-layout-key-inhibit.png@420c4a3dd1f8f68bdab5791e43816bf7f4cae91a", "docs/reviews/PDR/figures/display-layout-id-reminder.png@42edfb328a13ee8e1a56098f5efbbf1211dcf0eb", "docs/reviews/PDR/figures/display-layout-menu-level-1.png@6a034579826ac17db38f2c23ab15de15d3563aa2", "docs/reviews/PDR/figures/display-layout-menu-level-2-keyer.png@c4ab87d1f02c40984bc901c111cf0f60bfeddb51"]
analysis_kind: [timing, other]
# product_size: iteration 1 text first; iteration 2 (8c12b5a): note 317 lines, model 638 lines, checker 274 lines and
# 41 assertions, 1 plot, 9 display renders
product_size: 1 note (286 lines, 12 sections), 1 model (567 lines), 1 checker (246 lines, 33 assertions), 1 results file, 1 plot, 7 display renders; 9 requirement values (G14 design part), 13 per-case rows in this record
tools_used: ["venv Python 3.13.5 (TV-001, accredited for schema validation only; not for this model)", "ui_model.py and check_ui_design.py at 82cf086 (iteration 1) and 8c12b5a (iteration 2) (no TV record)", "Pillow 12.3.0 and matplotlib 3.11.2 (renders and plot, no TV record)"]
values_proposed: ["REQ-SYS-058: 10 Hz to 10 kHz (unchanged), step table of note section 3.4", "REQ-SYS-061: 4.0 mm (unchanged)", "REQ-SYS-062: two levels (unchanged), 24 items with the Straight-input setting as MODE values; REQ-SYS-035 trim on a service calibration screen outside the operator tree", "REQ-SYS-067: 1 s (unchanged), 25 distinct messages including REQ-SYS-134, 155 and 156", "REQ-SYS-068: 9 min 00 s +/-5 s (unchanged)", "REQ-SYS-136: Iambic A, 15 WPM, 600 Hz, 8-dit hang, 5 ms (unchanged)", "REQ-SYS-164: 30 s at 2 rev/s (unchanged)", "REQ-SYS-165: 300 lux (unchanged), with the lens condition of note section 6.2", "REQ-SW-KEYER-014: 50 frames/s and 50 detents/s per encoder (unchanged)"]
renders_inspected: 10
sprint: PDR-prep
author_agent: "author:WP-PDR-33 wave 1a (Claude as ME/UI designer)"
reviewer_agent: "reviewer:WP-PDR-33-ui-design-iter1 (independent; authored no part of WP-PDR-33); iteration 2 by reviewer:WP-PDR-33-ui-design-iter2 (independent; authored no part of WP-PDR-33 and no part of its revision 2)"
# criticality: the note declares SW-DISPLAY (mission-critical, 07 section 14.1). assurance_required: false,
# because a stand-alone analysis note is not a row of 07 section 2.1.1 (template guidance) and PDR work plan
# WP-PDR-33 names no assurance pair for this record; section J is answered by this reviewer. Cross item X-2
# asks the lead SE to confirm, since the note also carries preliminary SW-DISPLAY design content
criticality: mission-critical
assurance_required: false
assurance_reviewer_agent: none
iteration: 2
readiness_met: true
# reviewer_verdict (iteration 2): APPROVED; findings 1 and 2 (Major) Verified; findings 3 to 6 and the new findings 7
# and 8 are Minor and Open (liens due at the CDR readiness declaration, plan rule C1)
reviewer_verdict: APPROVED
assurance_verdict: not-required
# verdict: held at NEEDS CHANGES. No SA pair is required (assurance_required false; cross item X-2 still open with
# the lead SE). The applied analysis template is still only on cr/CR-012 (blob 0386cc6e), so, per the lead SE
# convention of 2026-09-27 as INSP-075 applies it, the record verdict is set to APPROVED in the CR-012 merge commit
# (or the commit right after it) if that blob is unchanged
verdict: NEEDS CHANGES
findings_major: 2
findings_minor: 6
findings_open: 6
findings_fixed: 0
findings_verified: 2
findings_deferred: 0
assurance_tasks_applied: [swe-070 7.1 task 1, swe-134 7.1 task 1]
deferred_rids: []
items_no: [CK-ANA-F1, CK-ANA-A4, CK-ANA-G6-2, CK-ANA-J1]
effort_turns: 54
effort_minutes: 80
record_status: Open
date: 2026-09-27
date_closed: null
---

# Peer review record: UI design analysis (INSP-072, iteration 1)

**Product:** `docs/design/analysis/ui-design.md` blob `4ef24520` at freeze commit `82cf086` (freeze F0, PDR work plan rule C2), with `ui_model.py` (`58ce1f9b`), `check_ui_design.py` (`875e4628`), `ui-design-results.json` (`8c3b2158`), the plot `ui-tuning-step-law.png` (`97abc3c9`) and the seven renders `docs/reviews/PDR/figures/display-layout-{receive,transmit,tune,key-inhibit,id-reminder,menu-level-1,menu-level-2-keyer}.png`. Every blob equals `git rev-parse 82cf086:<path>` and `HEAD:<path>` on 2026-09-27. No product blob lives on a `cr/` branch.

**Checklist:** `docs/templates/peer-review-checklist-analysis.md` revision A (CR-012 branch blob `0386cc6e`), sections R, A to F, G6, H, I, J (analysis_kind timing and other; criticality mission-critical, so J is answered by this reviewer). The render checks of `peer-review-checklist-visual-product.md` revision A are applied inside section I.

**Acceptance criteria (rule C7).** The G14 design-part TBRs of plan section 10.2 (REQ-SYS-058, 061, 062, 067, 068, 136, 164, 165; REQ-SW-KEYER-014; REQ-SW-KEYER-036 is in the keyer study, INSP-071), each with the cases its `description`, `tbr.plan`, `verification_note` and rationale name at `docs/requirements/sys/requirements.json` blob `f128235e` and `docs/requirements/sw/sw-keyer/requirements.json` blob `f9141160`; the WP-PDR-33 output list (menu tree, step table and crossing time with a host usability run, character height, 300 lux floor, fault latency, ID reminder, defaults, display layout renders); REQ-SYS-060, which the note claims in its per-case table.

**Search rule.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` (record rules, RF exposure separation values, 07 section 2.1.1) preceded every `grep`. No rustos file was read.

## Findings (iteration 1)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | reviewer | Major | CK-ANA-F1 | Note section 3.3 menu tree; section 6.3 ("Every one of the 24 operator settings"); `ui_model.py` `MENU_TREE` and `NON_MENU_CONTROLS` | REQ-SYS-062 bounds "every operator setting". Two settings that requirements name are not in the tree. First, the Straight-input setting of REQ-SW-KEYER-002 ("from the tip, the ring or either contact as the operator's Straight-input setting selects"): the key-mode codes of section 3.2 list only ST and SO, and no item or MODE value selects ring-only or either contact. Second, the per-unit receive filter-centre trim of REQ-SYS-035, whose verification note is a "Bench demonstration in the calibration menu": the tree has no calibration entry, and the note does not say whether that menu is inside or outside the REQ-SYS-062 scope. The "all 24 items" evidence is therefore incomplete for the value that goes to the owner. Fix: add the Straight-input selection (as MODE values or an item), and add the calibration trim as a level-2 item, or state with a reason that the calibration menu is outside "operator setting". Then recount and re-render the level-2 screens that change | Verified (iteration 2, revision 2 at 8c12b5a) | Pending | |
| <a id="finding-2"></a>finding-2 | reviewer | Major | CK-ANA-F1 | Note section 3.6 message table; section 7 row "Each Table 3.4-4 cause with a text" | REQ-SYS-067 requires a distinct message "for each detected fault type", and its rationale names REQ-SYS-088, 089, 134, 155, 156 and 167. The table maps only ConOps Table 3.4-4 rows 1 to 19. REQ-SYS-155 (PA temperature reading out of range, Fault-safe) and REQ-SYS-156 (implausible forward-power reading, Fault-safe) have no row there and no banner here. The REQ-SYS-134 indication that a stored setting was replaced by its default has none either. The note routes only rows 21 to 23 to the ConOps writer. Fix: add banners for these fault types, or list them as open cases with a request to the ConOps writer (WP-PDR-10). Restate the "distinct" and latency results over the complete set | Verified (iteration 2, revision 2 at 8c12b5a) | Pending | |
| <a id="finding-3"></a>finding-3 | reviewer | Minor | CK-ANA-F1, CK-ANA-I2 | Note section 3.6 ("drawn over lines 3 and 4 of the status screen"); section 7 row REQ-SYS-060; renders `display-layout-key-inhibit.png`, `display-layout-id-reminder.png` | REQ-SYS-060 requires all six status items in Receive outside menus, and the KEY inhibit and the ID reminder occur in Receive. The key-inhibit render drops the power step (and the separation reminder). The ID-reminder render drops the battery state (and the separation reminder), and that banner stays until the next key-down. The per-case table checks only the receive, transmit and tune renders. Fix: keep the power step and battery state visible under a banner (for example on the banner's second line or line 1), and add the banner screens to the REQ-SYS-060 row | Open | Pending | |
| <a id="finding-4"></a>finding-4 | reviewer | Minor | CK-ANA-A4 | Note input I-10; renders `display-layout-transmit.png` ("KEEP 0.6M" at 5 W), `display-layout-tune.png` ("KEEP 1.0M"), `display-layout-receive.png` | I-10 cites REQ-SYS-069 but takes its values from ConOps section 3.5.1 item 5 (0.5 W 0.2 m, 1 W 0.3 m, 2 W 0.4 m, 5 W 0.6 m, tune 1.0 m). The REQ-SYS-069 rationale gives, rounded up, 0.3, 0.3, 0.5 and 0.7 m while keying and 0.4, 0.5, 0.7 and 1.1 m during tune at 0.5, 1, 2 and 5 W. The 5 W render shows 0.1 m less than the requirement's figure. No proposed value of the note depends on it, and REQ-SYS-069 stays TBR to the PDR RF exposure evaluation. Fix: take the displayed values from REQ-SYS-069 and `docs/design/analysis/rf-exposure-evaluation.md`, or label them placeholders in the note and the render captions, and send the ConOps and REQ-SYS-069 disagreement to the ConOps writer | Open | Pending | |
| <a id="finding-5"></a>finding-5 | reviewer | Minor | CK-ANA-G6-2 | Note section 6.5 table; `ui_model.py` `fault_latency_budget` | The 25 frames/s limit of section 3.5 can hold a banner frame back until 40 ms after the previous frame started. The budget has no line for that hold-off (at most about 23 ms beyond the 16.8 ms frame in flight). The 20 ms detection-to-report item is taken from REQ-SW-KEYER-023 for all causes "by the same rule" with no requirement behind it. The total stays near 600 ms, under 1 s, so the conclusion holds. Fix: add the hold-off line, and state the detection-to-report assumption as a numbered assumption with its request to WP-PDR-35 | Open | Pending | |
| <a id="finding-6"></a>finding-6 | reviewer | Minor | CK-ANA-A3, CK-ANA-E3 | Note sections 4 (A-U1 to A-U3), 6.2, 8 row REQ-SYS-165, 9 R-U1 | REQ-SYS-165 closes by Analysis, and this note is its first issue. The legibility criteria it passes against (20 arcmin, 3 cd/m2, 3:1) have no corpus source (L-U1). The "Confirmed: 300 lux" also holds only if an AR-coated lens is used or the specular case is accepted, and that condition exists only as request R-U1 with no requirement to carry it. Fix: state in section 8 that the value goes to the owner with the criteria A-U1 to A-U3 for ratification and the lens condition as an explicit owner choice. Route the lens constraint to the ME L2 writer (WP-PDR-34) as a requirement request, not only to the enclosure WPs | Open | Pending | |
| <a id="finding-7"></a>finding-7 | reviewer (iteration 2) | Minor | CK-ANA-F1, CK-ANA-H1 | Note section 3.3 "Calibration trim" and section 3.1 row "FUNC held while switching on"; render `display-layout-cal-trim.png` | The service calibration screen holds one item, RX TRIM (REQ-SYS-035). Two other sources name a second per-unit calibration: REQ-SYS-144 ("stored firmware calibration of pitch centre and reference trim") and the ConOps maintenance row "Calibration" ("Per-unit pitch offset centre and frequency reference trim stored at acceptance; re-trim by the owner against an off-air reference"). The note does not say where the frequency reference trim is set. `docs/design/analysis/frequency-budget.md` section 3.2 makes that constant safety-relevant (HZ-008 cause C7, a range of at most +/-0.9 ppm), and the configuration guard lists "frequency calibration". The note also does not say whether guest lock (REQ-SYS-066) gates the FUNC-at-switch-on entry, although its own reason for leaving the operator tree is that "any operator or guest" could change a setting there. Minor: REQ-SYS-062 and the finding-1 result do not depend on it. Fix: place the reference trim on the service screen (or name where it is set, with its range), and state the access rule for the screen (for example, not entered while guest lock is set). Send both to the SW L2 writer with R-U3 | Open | Pending | |
| <a id="finding-8"></a>finding-8 | reviewer (iteration 2) | Minor | CK-ANA-G6-2, CK-ANA-F1 | Note section 3.6 row REQ-SYS-134 ("shown after Self-test until the next control input"); section 6.5 and A-U10 | Section 6.5 claims the 1 s latency for the REQ-SYS-134 message, because the detection at configuration load comes after display initialisation (A-U10). The message table then says the banner is "shown after Self-test". Self-test "lasts a few seconds" (`docs/conops/conops.md` Table 3.4-1, Self-test row), and that row checks the "stored configuration (an invalid setting is replaced by its default and shown ...)" during Self-test. Read as written, the banner can appear more than 1 s after detection, which contradicts the section 6.5 claim. Minor: the design can meet 1 s by drawing the banner at detection. Fix: state that the banner is drawn within the section 6.5 budget during Self-test and kept after Self-test until the next control input, or restate the REQ-SYS-134 latency case | Open | Pending | |

Two Major findings: `reviewer_verdict` NEEDS CHANGES (07 section 10.2; PDR work plan rule C1). The step table and crossing time, the character height, the menu depth for the listed items, the ID reminder timing, the defaults and the keyer timing load were re-checked and stand.

## Readiness criteria

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | Frozen blobs | Yes | `git rev-parse 82cf086:<path>` equals every `product_files` blob; HEAD equals them too |
| R2 | Checker runs by one command with the stated result | Yes | On an export of `82cf086`: `.venv/bin/python docs/design/analysis/ui-design/check_ui_design.py`: 33 PASS, "0 failed assertion(s)", exit 0 |
| R3 | validate_docs on JSON under a schema | N/A | The results file has no schema |
| R4 | Author return states question, assumptions, inputs, results, limitations, values, tools | Yes | Note sections 1, 2, 4, 6, 8, 10, 11 |
| R5 | No TBD; TBRs named | Yes | No "TBD" string; every TBR named by id with its `tbr.plan` (section 1 table) |
| R6 | Every cited render exists beside its source | Yes | The plot is in `docs/design/analysis/ui-design/`; the seven renders are in `docs/reviews/PDR/figures/`, the path the plan names |

## A. Question, scope and traceable inputs

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-A1 | Yes | Section 1 names REQ-SYS-058, 061, 062, 067, 068, 136, 164, 165 and REQ-SW-KEYER-014, with the `tbr.plan` steps quoted as in the files |
| CK-ANA-A2 | Yes | Inputs cited by blob: requirements `f128235e`, `f9141160`; research `11c497ba`; ConOps `6c3fbb2b`. Each equals HEAD. No AT RISK dependency is claimed. The window geometry of I-11 feeds CR-003 work, but no result here depends on the CR |
| CK-ANA-A3 | Yes, with finding-6 | Every input has a source or is a labelled assumption (A-U1 to A-U9). The unsourced legibility criteria are finding-6 |
| CK-ANA-A4 | No | I-1 to I-9 and I-11 agree with their sources: 0.18 mm pitch, 14 percent reflectivity, CR 21, 16.8 ms frame, 24 detents, 5 ms button bounce, the 97.119(a) text in the corpus, the ranges of REQ-SYS-041, 044, 045 and 014. I-10 disagrees with the REQ-SYS-069 it cites (finding-4) |
| CK-ANA-A5 | Yes | A-U1 to A-U9 are stated with direction and invalidation |
| CK-ANA-A6 | Yes | No requirement or interface file is edited. Requests R-U1 to R-U5 go to named WPs. No CR is triggered |

## B. Model validity

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-B1 | Yes | Lambertian reflection, Fresnel lens with summed double reflection, the rate-dependent step with grid landing, and a scripted operator are each stated (sections 3.4, 6.2; `ui_model.py`) |
| CK-ANA-B2 | N/A | No vendor model |
| CK-ANA-B3 | Yes | The digit height is measured from the frame buffer (23 dot rows), not taken from the font constant. The crossing time is hand-checked in section 5 (400/48 = 8.33 s) |
| CK-ANA-B4 | N/A | No numerical solver settings; the step simulation is exact per detent |
| CK-ANA-B5 | Yes | Reviewer hand calculations. 23 x 0.18 = 4.14 mm, 28.5 arcmin at 0.5 m (4.0 mm: 27.5). L = 300 x 0.14 / pi = 13.37 cd/m2. Plain lens: R = 0.0387, R_total = 0.0745, T_display = 0.854, veil = 0.0745 x 76.4 = 5.69 cd/m2, CR = (11.42 + 5.69)/(0.544 + 5.69) = 2.74. Floor: 3 pi/(0.14 x 0.854) = 78.8 lux. Latency 20 + 20 + 2 + 16.8 + 16.8 + 500 = 575.6 ms. ID late error 0.027 + 0.020 + 0.0336 + 0.5 = 0.58 s. Bus 1/16.8 ms = 59.5 frames/s. 50 detents/s x 4 states = 5 ms per state. All agree |
| CK-ANA-B6 | Yes | Uncertainty is bounded by assumption: A-U5 (LC response), A-U7 (crystal), A-U8 (encoder phase). Each margin (424 ms, 4.4 s, 21.7 s) exceeds its bound |

## C. Tools, validation status and reproducibility

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-C1 | Yes | Python 3.13.5, Pillow 12.3.0 and matplotlib 3.11.2 match `tools/toolchain.lock.md` (lines 37, 197 and 203) |
| CK-ANA-C2 | Yes | Developer evidence, stated in the header and section 10. No closing credit for REQ-SYS-165 (its method is Analysis) until a TV record covers the model or the owner rules on developer evidence (cross item X-1) |
| CK-ANA-C3 | Yes | One headless command |
| CK-ANA-C4 | Yes | Reviewer re-run on an export of `82cf086`: exit 0, 33 PASS. The results JSON, the plot and all seven renders are byte-identical to the frozen blobs (`cmp`) |
| CK-ANA-C5 | N/A | No TV record |

## D. Units, arithmetic and consistency

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-D1 | Yes | Units are stated on every quantity: mm, arcmin, lux, cd/m2, ms, s, Hz, detents/s, rev/s |
| CK-ANA-D2 | Yes | The note's numbers equal the results file: 4.14 mm, 2.74, 5.06, 10.0, 78.8 lux, 575.6 ms, -0.027/+0.58 s, 8.33 s, usability run 10.5 s and 275 detents with error 0 Hz |
| CK-ANA-D3 | Yes | Rounding is toward the limit (for example 575.6 ms is not rounded down) |
| CK-ANA-D4 | Yes | Checker constants carry their requirement ids |

## E. Results, margins, proposed values and credit

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-E1 | Yes | Each acceptance value is quoted with its id. 47 CFR 97.119(a) (corpus: 47cfr-97.119.md, eCFR issue 2026-09-23) is quoted verbatim, "at least every 10 minutes during a communication" |
| CK-ANA-E2 | Yes | Margins are limit minus result with the right sign. No TPM applies |
| CK-ANA-E3 | Yes, with finding-6 | The plain-lens specular case below 3:1 is reported as not passing, with limitation L-U2 and request R-U1. The condition's routing is finding-6 |
| CK-ANA-E4 | Yes | `check_ui_design.py` exits 1 on any failed assertion; 33 assertions |
| CK-ANA-E5 | Yes | Section 8 gives id, value, branch and margin for each of the nine values, and no CR is triggered. The REQ-SYS-058 and 164 `tbr.plan` "HostUnit usability run" is executed as a scripted Python operator, which section 10 states, with the person-in-the-loop part routed to WP-PDR-40 (R-U5) |
| CK-ANA-E6 | N/A | No TPM value |
| CK-ANA-E7 | Yes | Section 10: REQ-SYS-061 closes by Inspection of the flight renderer's frame at CDR and REQ-SYS-165 by Analysis. The others are Test or Demonstration, closed after TRR |

## F. Every case named

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-F1 | No | Per-case table below. REQ-SYS-062 misses two settings (finding-1). REQ-SYS-067 misses the fault types of REQ-SYS-155, 156 and 134 (finding-2). REQ-SYS-060 misses the banner screens (finding-3) |
| CK-ANA-F2 | Yes | The off-nominal cases are covered: the cold LC response (A-U5 at -10 C), the plain-lens specular case, and tuning stops at both band edges |
| CK-ANA-F3 | Yes | Worst combinations are stated: the minimum reflectivity with the white specular surround; the fault just after a UI tick with a frame in flight at the cold response |
| CK-ANA-F4 | Yes | The only margin within twice its uncertainty is the digit height (0.14 mm, less than one dot). Its sensitivity is stated, with free rows available for a larger digit |

### Per-case results

| Case | Condition | Governing id and limit | Result (checker output) | Margin with sign | Uncertainty | Reviewer re-check | Finding ids |
|---|---|---|---|---|---|---|---|
| U-1 | Frequency digits at 0.18 mm pitch | REQ-SYS-061: at least 4.0 mm | 4.14 mm (23 dots measured) | +0.14 mm | 1 dot | hand check; render inspected | none |
| U-2 | 0.5 m, 300 lux: no lens, plain lens (white and room surround), AR lens | REQ-SYS-165 with A-U1 to A-U3 | CR 21.0, 2.74, 5.06, 10.0; background 13.4 to 17.1 cd/m2 | +3.8 x luminance floor; contrast below 3:1 in the plain-lens specular case | assumption based | hand check of the plain-lens case | finding-6 |
| U-3 | Illuminance above 300 lux | REQ-SYS-165 "or more" | contrast independent of illuminance | not applicable | none | argument checked | none |
| U-4 | Every operator setting | REQ-SYS-062: two levels | 24 listed items at level 2 or above; Straight-input and calibration trim absent | not shown | not applicable | enumeration against the requirement files | finding-1 |
| U-5 | Slow and fast turning | REQ-SYS-058: 10 Hz to 10 kHz | 10 Hz below 5 detents/s, 10 kHz at 20 detents/s and above | not applicable | none | re-run: same | none |
| U-6 | Band crossing at 2 rev/s | REQ-SYS-164: 30 s | 8.33 s (400 detents at 10 kHz plus 1 slow detent) | +21.7 s | none | hand check | none |
| U-7 | Scripted usability run and full band | REQ-SYS-058, 164 `tbr.plan` | 10.5 s, 275 detents, 0 Hz error; 14.0 s full band | not applicable | scripted operator (L-U4) | re-run: same | none |
| U-8 | Each detected fault type has a distinct message | REQ-SYS-067 | 22 distinct banners for Table 3.4-4 rows 1 to 19; REQ-SYS-155, 156, 134 absent | not shown | not applicable | enumeration against the REQ-SYS-067 rationale | finding-2 |
| U-9 | Fault message latency | REQ-SYS-067: 1 s | 575.6 ms (about 600 ms with the rate-limit hold-off) | +424 ms (about +400 ms) | A-U5 | hand check | finding-5 |
| U-10 | Reminder at 540 s after the first key-down | REQ-SYS-068: 9 min 00 s +/-5 s | -0.027 s / +0.58 s | +4.4 s | A-U7, A-U5 | hand check | none |
| U-11 | Configuration reset | REQ-SYS-136 | five defaults on their ranges; 8-dit hang at 15 WPM 640 ms, above a 560 ms word space | not applicable | none | hand check against REQ-SYS-040, 041, 044, 045, 014 | none |
| U-12 | Receive, Transmit-keyed and Tune screens, including banner screens in Receive | REQ-SYS-060 | six items on receive, transmit and tune renders; key-inhibit and ID-reminder renders drop power step and battery state | not applicable | not applicable | renders inspected | finding-3 |
| U-13 | 50 frames/s and 50 detents/s per encoder | REQ-SW-KEYER-014 | 2 x the 25 frames/s design; 84 percent of the 59.5 frames/s bus; 5 ms per quadrature state | not applicable | A-U8 | hand check | none |

## G6. Timing

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-G6-1 | Yes | The time base is stated: a 20 ms UI tick, the 1.1 MHz SPI (16.8 ms frame), the 1 kHz encoder sampler and a crystal of +/-50 ppm (A-U7) |
| CK-ANA-G6-2 | No | The latency path omits the frame-rate hold-off (finding-5). The total still meets the limit |
| CK-ANA-G6-3 | Yes | No duration comes from Emulation |
| CK-ANA-G6-4 | N/A | The display latency bounds an indication, not a hazard response. The REQ-SW-KEYER-023 KEY inhibit acts before the display, within 20 ms |

## H. Hazards, risks and records

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-H1 | Yes | No hazard control changes. The separation display (HZ-006 K5) is finding-4 |
| CK-ANA-H2 | Yes | No risk is raised or retired |
| CK-ANA-H3 | Yes | Section 12, revision 1 |

## I. Visual closure (with `peer-review-checklist-visual-product.md` items)

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-I1 | Yes | All eight renders were opened with the Read tool (renders_inspected 8), and all regenerate byte-identically |
| CK-ANA-I2 | Yes, with finding-3 | `ui-tuning-step-law.png`: two panels. The step against detent rate is on log axes with units and the 2 rev/s marker. The crossing time against rev/s shows the 30 s limit labelled REQ-SYS-164 and the 8.3 s point at 2 rev/s. The seven display renders are captioned with the panel, dot count, pitch and 4x scale. The text fits in 128 dots, the inverted bands are legible, and the digits match "146.520.00". The content gaps on two banner screens are finding-3, and the separation values finding-4 |

## J. Software assurance items (criticality mission-critical, answered by this reviewer)

| Id | Answer | Evidence |
|---|---|---|
| CK-ANA-J1 | No | SWEHB `swe-070` section 7.1 task 1: the model is not validated or accredited (CK-ANA-C2). The note marks its results developer evidence, which is the required disclosure. Credit waits on a TV record or an owner ruling (cross item X-1) |
| CK-ANA-J2 | Yes | SWEHB `swe-134` section 7.1 task 1: the note sets no SWE-134 item value. The displayed frequency comes from the synthesizer value, never the request (section 3.5), which is consistent with the 07 section 14.2 SW-DISPLAY row item (g) |
| CK-ANA-J3 | Yes | `assurance_tasks_applied` lists both tasks; their results are stated in J1 and J2 |

## Items N/A

CK-ANA-B2, B4, C5, E6, G6-4; sections G1 to G5 and G7 (analysis_kind is timing and other).

## Cross items for the lead SE (not findings on the note)

- X-1. Rule C10 and CK-ANA-C2: as for INSP-071, the values rest on a model with no TV record. REQ-SYS-165 is an Analysis-method requirement whose closing evidence this note is meant to become.
- X-2. Assurance routing. The note declares SW-DISPLAY mission-critical and carries preliminary SW-DISPLAY design content (menu tree, message table, step table). 07 section 2.1.1 routes the "module sections" of a mission-critical design to the assurance reviewer. It has no row for a stand-alone analysis, and the plan names no pair for this record. The lead SE confirms whether an assurance pair is needed. This record assumes not.
- X-3. The ConOps and REQ-SYS-069 separation values disagree (0.6 m against 0.7 m at 5 W; 1.0 m against 0.4 to 1.1 m in tune). This is outside this note, for the WP-PDR-10 and RF exposure writers.

## Commands

- `git rev-parse 82cf086:<path>` and `HEAD:<path>` for each product file: all equal.
- `git archive 82cf086 | tar -x` into the scratchpad, then `.venv/bin/python docs/design/analysis/ui-design/check_ui_design.py`: exit 0, 33 PASS, 0 failed. `cmp` of the regenerated results, plot and seven renders: identical.
- Requirement enumerations with the venv Python over `docs/requirements/sys/requirements.json` and `docs/requirements/sw/sw-keyer/requirements.json`: statements naming a menu, setting or operator selection (finding-1), and the REQ-SYS-067 rationale ids (finding-2).
- `/Users/robinonsay/rust/cwht/.venv/bin/python /Users/robinonsay/rust/cwht/tools/validate_docs.py`: run on the record before its commit.

## Measurements (SWE-089)

Items checked 42 (R1 to R6, A1 to A6, B1 to B6, C1 to C5, D1 to D4, E1 to E7, F1 to F4, G6-1 to G6-4, H1 to H3, I1, I2, J1 to J3); items answered No 4 (CK-ANA-A4, F1, G6-2, J1); findings 2 Major, 4 Minor; fixed 0; deferred 0; iteration 1; effort 30 turns, about 45 minutes; renders inspected 8; per-case rows 13; inputs checked 11.

## Iteration 2: delta verification of findings 1 and 2 (Major) (2026-09-27, HEAD `4b51f7f`)

**Scope (rule C1).** Iteration 2 is a delta that verifies the fixes of finding-1 and finding-2 only. Findings 3 to 6 (Minor) were not touched by the author (note header "Status") and are not re-reviewed. Product: the 14 blobs of front matter `product_files`, committed as `8c12b5a` (WP-PDR-33 revision 2). Each one equals `git rev-parse 8c12b5a:<path>`, `git rev-parse HEAD:<path>` and `git hash-object <path>` (script, 14 of 14). `git log 8c12b5a..HEAD` shows no later change to any product file. All blobs are on main. The checklist is the one of iteration 1: `peer-review-checklist-analysis.md` revision A, blob `0386cc6e`, still only on `cr/CR-012-pdr-checklist-templates` at `7784672`, with the `peer-review-checklist-visual-product.md` items for the renders.

**Independence (rule C4).** This invocation authored no part of WP-PDR-33 and no part of revision 2. It did not edit any product file.

**Search first (charter section 11 rule 1).** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (the WP-PDR-33 records; the frequency reference calibration trim). `grep` then only pinned lines in known paths (the note, `ui_model.py`, `docs/conops/conops.md`). Requirement texts were read with the venv Python from `docs/requirements/sys/requirements.json` (blob `f128235e`), `docs/requirements/sw/sw-keyer/requirements.json` (`f9141160`) and `docs/requirements/l0-stakeholder/expectations.json`.

**Reproduction.** On a `git archive 8c12b5a` export in the scratchpad: `.venv/bin/python docs/design/analysis/ui-design/check_ui_design.py`: 41 PASS, "0 failed assertion(s)", exit 0. `cmp` of the regenerated `ui-design-results.json`, `ui-tuning-step-law.png` and all nine `display-layout-*.png` with the frozen blobs: identical.

### Verification of finding-1, case by case (rule C7)

| # | Case | Check | Result |
|---|---|---|---|
| 1 | The REQ-SW-KEYER-002 Straight-input setting ("from the tip, the ring or either contact as the operator's Straight-input setting selects") is reachable | Note section 3.3 "MODE values": STR TIP (SO), STR RING (SR), STR BOTH (ST) under KEYER > MODE, level 2. `ui_model.py` `MODE_VALUES` carries the three sources "REQ-SW-KEYER-002 tip / ring / either", and the checker asserts it (`mode_values` in the results) | Yes |
| 2 | Every REQ-SYS-040 mode (Straight, Iambic A, Iambic B, Ultimatic, Bug) is still a MODE value | `mode_values`: IAMB A, IAMB B, ULTIMATIC, BUG and the three Straight values; checker assertion "KEYER > MODE offers every REQ-SYS-040 mode" | Yes |
| 3 | The mono-plug path of REQ-SYS-056 and REQ-SYS-163 still works | STR TIP is the Straight-on-tip choice (ADR-009 default tip; REQ-SW-KEYER-002 rationale "With the tip setting the ring is ignored"). One MODE selection sets it, and REQ-SYS-163 accepts that selection with a closed input. The note gives this as the reason not to add a separate item | Yes |
| 4 | The REQ-SYS-035 calibration trim: in the tree, or stated outside "operator setting" with a reason | Section 3.3 "Calibration trim": outside REQ-SYS-062 because NGO-012 says "the filter-centre offset is a per-unit calibration stored at acceptance over +/-500 Hz in 10 Hz steps, not an operator control" (quote checked verbatim against `expectations.json`). The trim sits on a service calibration screen, which is the "calibration menu" of the REQ-SYS-035 verification note and TC-SYS-023. The checker asserts that REQ-SYS-035 is on that screen and not among the operator-tree sources | Yes (scope of the screen: finding-7, Minor) |
| 5 | Recount of the items against REQ-SYS-062 | `MENU_TREE`: KEYER 8, AUDIO 4, TX 4, SETUP 4 = 20 menu items at level 2, plus 4 direct controls (`NON_MENU_CONTROLS`) = 24; `max_items_per_category` 8. Nothing is deeper than level 2 | Yes |
| 6 | The level-2 screens that change are re-rendered | `display-layout-menu-level-2-keyer-straight.png` (MODE in edit on "<STR RING>", the widest bracketed value) and `display-layout-cal-trim.png` are new. The checker asserts that every MODE value fits the 124-dot bar. Both renders opened: see visual closure below | Yes |
| 7 | Status codes stay distinct and fit | 7 values and 7 codes distinct (checker). The status line of the receive render shows the 2-character code ("IA") in the same place | Yes |

**Result: finding-1 Verified.**

### Verification of finding-2, case by case (rule C7)

| # | Case | Check | Result |
|---|---|---|---|
| 1 | REQ-SYS-155 fault type has a distinct message | "PA SENSOR / REPORT", class Latched. That matches the requirement ("shall enter Fault-safe within 100 ms (TBR) of its PA temperature reading leaving -20 C to +150 C (TBR)") | Yes |
| 2 | REQ-SYS-156 fault type has a distinct message | "PWR SENSOR / REPORT" (10 characters), class Latched, matching "shall enter Fault-safe ... forward-power reading leaving the plausible range" | Yes |
| 3 | The REQ-SYS-134 indication (a setting replaced by its default) has a message | "SETTINGS / DEFAULTED", an indication that does not stop transmission. That is consistent with ConOps Table 3.4-1 Self-test row ("an invalid setting is replaced by its default and shown, REQ-SYS-134; this is not a failure") | Yes (timing wording: finding-8, Minor) |
| 4 | The other rationale ids (REQ-SYS-088, 089, 167) are covered | ConOps Table 3.4-4 row 13 cites REQ-SYS-088 ("CELL SENSE"). Row 15 cites REQ-SYS-089 (safety timer) and covers "current not falling", which is REQ-SYS-167 ("constant-voltage charge current falls by less than 20 mA ... over 60 min"). Both rows already have banners | Yes |
| 5 | "Distinct" restated over the complete set | `message_count_total` 25 (22 for rows 1 to 19 and 3 added); the checker asserts all 25 distinct and every line at most 10 characters | Yes |
| 6 | Latency restated over the complete set | Section 6.5: the same 575.6 ms budget. REQ-SYS-155 and 156 report through the safe-state path. REQ-SYS-134 is detected at configuration load after display initialisation (new assumption A-U10, request R-U2). The table's "shown after Self-test" wording conflicts with that claim (finding-8, Minor). The claim holds if the banner is drawn at detection | Yes, with finding-8 |
| 7 | The ConOps gap is routed to its writer | R-U6 to WP-PDR-10: rows for REQ-SYS-155 and 156, the REQ-SYS-134 indication, and the service screen in section 3.5.1. No ConOps file is edited (plan section 5.3) | Yes |

**Result: finding-2 Verified.**

### New findings (iteration 2)

<a id="finding-7"></a>**finding-7, Minor, Open.** The service calibration screen omits the frequency reference trim that REQ-SYS-144 and the ConOps maintenance row name, and it states no access rule against guest lock. See the findings table. **Citation:** REQ-SYS-144; `docs/conops/conops.md` maintenance table row "Calibration"; `docs/design/analysis/frequency-budget.md` section 3.2 (HZ-008 C7); REQ-SYS-066.

<a id="finding-8"></a>**finding-8, Minor, Open.** "shown after Self-test" in the REQ-SYS-134 row conflicts with the 1 s latency claim of section 6.5 and with the ConOps Self-test row. See the findings table. **Citation:** REQ-SYS-067 ("within 1 s (TBR) of detection"); `docs/conops/conops.md` Table 3.4-1 Self-test row.

### Visual closure (iteration 2)

All 10 figures of the product were opened with the Read tool (renders_inspected 10): the plot and the nine renders. `display-layout-menu-level-2-keyer-straight.png` (new) shows the KEYER header with "1/8", four rows with MODE inverted, the edit bar "<STR RING>" inside the frame with a margin at both ends, and the soft labels BACK and SET. Its caption wraps onto two lines inside the image width. `display-layout-cal-trim.png` (new) shows the CAL header with "1/1", RX TRIM inverted, the range line "+/-500 HZ" and step line "10 HZ STEP", the value bar "<-30 HZ>", and the soft labels EXIT and STORE. The labels match the section 3.3 text (exit on MENU, store after a push). The seven iteration 1 renders and the plot are byte-identical to iteration 1 and were re-opened; the finding-3 and finding-4 observations of iteration 1 still apply (not in the delta).

### Cross items (iteration 2, returned to Claude)

- X-4. The record `verdict` is held only for the CR-012 merge (lead SE convention of 2026-09-27). No SA pair is required unless the lead SE decides otherwise on X-2.
- X-5. The status code "ST" changed meaning between revisions: in revision 1 it meant Straight, and now it means Straight from either contact. SO is now the tip-only (mono-plug) choice. The WP-PDR-35 L2 writer (R-U3) and the ConOps writer (R-U6) should use the revision 2 codes.
- X-6. Rule C10 and X-1 still hold: the values rest on developer evidence.

### Completion criteria (SWE-088), iteration 2

Reviewer side met: no Major is open, readiness is met (R1 to R6 re-checked at `8c12b5a`), and findings 3 to 8 are Minor liens due at the CDR readiness declaration (plan rule C1; PDR package section 15). `reviewer_verdict: APPROVED`. The record `verdict` stays NEEDS CHANGES until CR-012 merges with the analysis template blob `0386cc6e` unchanged. It is then set to APPROVED in that merge commit or the commit right after it.

```
ITERATION 2 (2026-09-27, HEAD 4b51f7f, product commit 8c12b5a): REVIEWER VERDICT: APPROVED; RECORD VERDICT: NEEDS CHANGES (held for the CR-012 merge only)
FINDINGS:
- [Major] finding-1: Verified (Straight-input setting as MODE values STR TIP, STR RING, STR BOTH; REQ-SYS-035 trim outside the operator tree for the NGO-012 reason; 24 items recounted; two renders added).
- [Major] finding-2: Verified (banners for REQ-SYS-155, 156 and 134; 088, 089 and 167 mapped to rows 13 and 15; 25 messages distinct; latency restated; R-U6).
- [Minor] finding-3 to finding-6: Open, not in the delta (liens).
- [Minor] finding-7 (new): service calibration screen omits the frequency reference trim and states no guest-lock access rule (lien).
- [Minor] finding-8 (new): REQ-SYS-134 banner "shown after Self-test" conflicts with the 1 s latency claim (lien).
MEASUREMENTS: blobs equal HEAD 14/14; checker 41 PASS exit 0; outputs byte-identical 11/11; cases 14 (14 Yes, 2 with a new Minor); renders inspected 10; major open=0; minor open=6; turns=24; minutes=35 (cumulative 54 and 80); iteration=2
