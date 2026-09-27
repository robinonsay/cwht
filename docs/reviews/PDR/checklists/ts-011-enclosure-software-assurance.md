---
# Peer-review record front matter (charter sections 2 and 5; docs/process/01-lifecycle-and-reviews.md
# section 13 is the single field list; docs/process/07-software-engineering-plan.md sections 2.1.1, 10.2
# and 15). This is the paired software assurance record (07 section 10.2 Record row) of the trade-study
# review INSP-081 (docs/reviews/PDR/checklists/ts-011-enclosure.md, reviewer
# reviewer:WP-PDR-27-ts-011-iter1, committed f6a4a4b), at the path INSP-081 names in its front matter and
# cross item X-3, and that plan section 3.1 "Records" sets for SA pairs. Dispatch: 07 section 2.1.1 row
# "Trade studies and ADRs whose decision constrains a safety-critical or mission-critical component";
# rules C4 and C9 of the plan.
# Checklist applied: docs/templates/peer-review-checklist-software-assurance.md revision A AS ON ITS CR-012
# BRANCH (cr/CR-012-pdr-checklist-templates at 7784672, blob 5b13528504868b2add0f0b1e329c63aa2b54cdf4; not
# merged, absent from main). tools/validate_docs.py fails a record whose `checklist` names a template absent
# from main, and the lead SE convention of 2026-09-27 does not change the validator, so the `checklist` field
# names peer-review-checklist-risk revision A, the checklist INSP-081 applied (section B, trade studies,
# 08 section 3.5), and `assurance_checklist` names the template actually applied (the INSP-074 form). The
# product blobs are all on main; only the template is branch-only.
# id: the brief assigned no id. INSP-087 is above every id on main (highest INSP-084), on every cr/ branch
# and in the working tree at c91a9eb (the untracked tool-validation-tv-015-to-tv-019.md already carries INSP-085,
# and INSP-086 is left free for a concurrent wave record).
id: INSP-087
checklist: peer-review-checklist-risk
checklist_revision: A
assurance_checklist: "docs/templates/peer-review-checklist-software-assurance.md@5b13528504868b2add0f0b1e329c63aa2b54cdf4 (revision A, branch cr/CR-012-pdr-checklist-templates at 7784672)"
checklist_file: docs/reviews/PDR/checklists/ts-011-enclosure-software-assurance.md
product: docs/decisions/trade-studies/TS-011-enclosure.md
# product_commit and product_files: equal to INSP-081 iteration 1 (readiness R1; rule C2). Each blob equals
# git rev-parse 70a3a33:<path>, git rev-parse HEAD:<path> and git hash-object <path> at HEAD c91a9eb
# (checked 2026-09-27): the products are not branch-only
product_commit: "70a3a33"
product_blob: 8d2708f1b0175d73945b7ee32d9d49937f4a51e9
product_files: ["docs/decisions/trade-studies/TS-011-enclosure.md@8d2708f1b0175d73945b7ee32d9d49937f4a51e9", "hardware/enclosure/board-outline.json@27dbacc7dda7f79e6cba3234ee77f6453e304906", "hardware/sim/enclosure/thermal_screen.py@78892ca27ace63c1bbd5965b730b0ccd6e85ab53", "hardware/sim/enclosure/envelope_drawing.py@20815e7581c34c9498e6c8d3972cc738e5c63e8a", "hardware/sim/enclosure/trade_matrix.py@c76b0f70d05a64c282a9066204a64ffe1e217fde", "hardware/sim/enclosure/out/thermal-screen.csv@a8c7d5b1b5f345172a036b590342f67b0adcc273", "hardware/sim/enclosure/out/trade-matrix.txt@c6023d697716d2c024c0033948aaeaa3aa3b7c0e", "docs/reviews/PDR/figures/ts011-thermal-screen.png@47d81e61ee7039b3126158c577170af30686752a", "docs/reviews/PDR/figures/board-outline-envelope.png@ff8aa6c2befd4660f2bf353893ab5673d24f79e3"]
# inputs read (not reviewed)
input_files: ["docs/reviews/PDR/checklists/ts-011-enclosure.md (INSP-081, committed f6a4a4b)", "docs/process/07-software-engineering-plan.md (sections 2.1.1, 14.1, 14.2, 15)", "docs/safety/hazards.json (HZ-003 causes, firmware_role, K2, K7, K9)", "docs/safety/hazard-analysis.md (HZ-003 row and paragraph)", "docs/requirements/sys/requirements.json (REQ-SYS-112, 113, 118, 155, 181)", "docs/test_cases/sys/test_cases.md (TC-SYS-109)", "docs/risk/register.json (RSK-006, RSK-026)", "docs/plan/pdr-work-plan.md (sections 1, 3.1, WP-PDR-27, WP-PDR-28, 5)", "docs/references/md/swehb/ (swe-022, 027, 033, 039, 057, 070, 080, 081, 086, 087, 089, 134, 136, 205 section 7.1)"]
paired_record: INSP-081
product_type: trade-study-or-adr
# criticality: safety-critical. TS-011 selects the PA-to-ambient heat path, the heat sink and the chain from
# the PA junction to the node that the REQ-SYS-181 cut-off senses and to the PA thermistor that the SW-SAFE
# thermal unit reads (07 section 14.1 row "Thermal protection", SW-SAFE thermal unit with SW-TXSEQ actuation,
# HZ-003, criteria b and e; hazards.json HZ-003 firmware_role.safety_critical true). INSP-081 sets the same
# criticality with the same basis (its cross item X-3)
criticality: safety-critical
product_size: 1 trade study (459 lines; 6 alternatives, 3 dropped at the screen, 9 mandatory and 8 enhancing criteria, route sub-matrix of 3 routes), 1 data file, 3 scripts, 2 outputs, 2 figures
sprint: PDR-prep
author_agent: "author:WP-PDR-27 wave 1a (Claude as ME designer)"
reviewer_agent: "sa-reviewer:WP-PDR-27-ts-011"
assurance_required: true
assurance_reviewer_agent: "sa-reviewer:WP-PDR-27-ts-011 (software assurance function; paired file review INSP-081 by reviewer:WP-PDR-27-ts-011-iter1)"
iteration: 1
readiness_met: true
# reviewer_verdict and assurance_verdict: NEEDS CHANGES at iteration 1 (rule C1): one Major finding open
reviewer_verdict: NEEDS CHANGES
assurance_verdict: NEEDS CHANGES
# verdict: set by Claude as software lead (07 section 10.2). NEEDS CHANGES: a Major finding is open here and
# two are open in INSP-081. The template applied is branch-only (lead SE convention of 2026-09-27), so even
# after the fixes the record verdict is set only when CR-012 merges with the template blob unchanged
verdict: NEEDS CHANGES
findings_major: 1
findings_minor: 2
findings_open: 3
findings_fixed: 0
findings_verified: 0
findings_deferred: 0
assurance_findings_major: 1
assurance_findings_minor: 2
assurance_tasks_applied: ["swe-134 7.1 task 5", "swe-022 7.1 task 1", "swe-033 7.1 task 1", "swe-033 7.1 task 2", "swe-033 7.1 task 3", "swe-039 7.1 task 4", "swe-057 7.1 task 2", "swe-134 7.1 task 4", "swe-134 7.1 task 6", "swe-205 7.1 task 1", "swe-205 7.1 task 3", "swe-080 7.1 task 1", "swe-080 7.1 task 2", "swe-081 7.1 task 2", "swe-086 7.1 task 1", "swe-087 7.1 task 2", "swe-089 7.1 task 1"]
swe134_items_checked: [a, b, c, d, e, f, g, h, i, j, k, l]
deferred_rids: []
items_no: ["swe-057 7.1 task 2", "swe-134 7.1 task 6", "swe-080 7.1 task 1", "swe-080 7.1 task 2", SA-C-i, SA-C-j, SA-D6, SA-E3]
effort_turns: 30
effort_minutes: 55
record_status: Open
date: 2026-09-27
date_closed: null
---

# Peer review record INSP-087: software assurance pair of INSP-081, TS-011 enclosure concept (WP-PDR-27)

**Product.** `docs/decisions/trade-studies/TS-011-enclosure.md` blob `8d2708f1` at freeze commit `70a3a33` (freeze F0, rule C2), with the eight files it scores from: `hardware/enclosure/board-outline.json` (`27dbacc7`), `hardware/sim/enclosure/thermal_screen.py` (`78892ca2`), `envelope_drawing.py` (`20815e75`), `trade_matrix.py` (`c76b0f70`), `out/thermal-screen.csv` (`a8c7d5b1`), `out/trade-matrix.txt` (`c6023d69`), `docs/reviews/PDR/figures/ts011-thermal-screen.png` (`47d81e61`) and `board-outline-envelope.png` (`ff8aa6c2`). These are the nine `product_files` of INSP-081. Each is equal at `70a3a33`, at `HEAD` (`c91a9eb`) and in the working tree. No product blob lives on a `cr/` branch. **Paired record:** INSP-081 (`ts-011-enclosure.md`), reviewer verdict NEEDS CHANGES at iteration 1 with two Major and four Minor findings.

**Checklist.** `docs/templates/peer-review-checklist-software-assurance.md` revision A as on its CR-012 branch (`7784672`, blob `5b135285`): sections R and A to F, the section B row `trade-study-or-adr`, and the row "Every product type". The template is branch-only; the front matter explains the `checklist` field.

**AT RISK.** The product is drafted on CR-003 revision 3 and CR-006 revision 2, both Submitted (plan rule C8). This review takes the CR-003 revision 3 text where the study does. None of the findings below depends on the disposition.

**Acceptance criteria (rule C7).**
- Every task of the section B rows `trade-study-or-adr` and "Every product type" is in the task table.
- Every other SWE the product implements or touches is added. The study is the risk-driven decision of RSK-006, which is software-tagged (SWE-086). It is a hardware change whose outputs feed a safety-critical software unit (SWE-080 task 1). It creates Record-class items (SWE-080 task 2, SWE-081 task 2).
- The SWE-134 items that 07 section 14.2 allocates to the components the study constrains are checked at trade-study maturity. For the `SW-SAFE` thermal unit these are a, d, g, h, j, k and l. For its `SW-TXSEQ` actuation they are a, b, c and e. Item i is checked because 07 section 14.2 row i names REQ-SYS-181 as the only bound of the thermistor-failure branch. Item f is checked because the thermal thresholds are guarded configuration fields (07 section 14.1, configuration guard row).
- The HZ-003 software contributions are checked by action, inaction and incorrect action (SWEHB `swe-205` 7.1 task 1). Each HZ-003 control that the decision moves is checked: K2 (the firmware inhibit on the PA thermistor), K7 (the thermal budget) and K9 (the firmware-independent cut-off).

**Independence (rule C4).** This invocation authored no part of WP-PDR-27 (TS-011, TS-004, the two analyses, the scripts, the outline, the figures). It is not the file reviewer of INSP-081 to INSP-084. It edited no product file.

**Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search. Queries: the `SW-SAFE` thermal unit, REQ-SYS-181 and the 07 section 14.1 thermal row; the SWEHB `swe-205` section 7.1 tasking. `grep`, `awk` and short Python reads of the JSON files were used afterwards only to pin lines, to extract the SWEHB section 7.1 task lists and to read REQ-SYS-112, 113, 118, 155, 181 and HZ-003. The index returned INSP-081 under its earlier id (INSP-071). The committed record at `f6a4a4b` carries INSP-081, so it was read by path. The rustos repository was not read.

## Findings (iteration 1)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | assurance | Major | `swe-134 7.1 task 6`, `swe-057 7.1 task 2`, `swe-080 7.1 task 1`, SA-C-i, SA-D6 | TS-011 section 3.1 M4, M9; section 4.1 row C1 columns M4 and M9; section 7; section 8 rules 2, 3 and 5; `board-outline.json` (no sensor entry); `thermal_screen.py` `steady()` and `r_junction_to_entry()` | **The recommended heat path decides whether the firmware-independent cut-off K9 (REQ-SYS-181) bounds the junction, and the study neither places its sensor nor assesses the result.** 07 section 14.2 row i makes REQ-SYS-181 the only bound of the thermistor-failure branch of HZ-003 (Critical), and M9 passes C1 on HZ-002 and HZ-007 alone. The governing texts give two sensing points. `hazards.json` HZ-003 K9 says "a second NTC at the PA". REQ-SYS-181, its rationale and TC-SYS-109 say "a second heat-sink sensor" and "heat-sink sensor". C1 makes the two points about 28 K apart, because its heat sink is a separate purchased part outside the shell, spring-loaded against the gap pad (rule 3), with "no holes needed". Take the study's own chain at 4.1 W (3.0 + 4.7 + 1.0 + 0.74 + 0.3 = 9.74 K/W from junction to heat-sink node). **(a) Sensor on the C1 heat sink.** The cut-off trips at about Tj = 95 + 4.1 x 9.74 = **134.9 C** (137.9 C at the 98 C band edge). That is 25 K above REQ-SYS-112, against the K9 TBR plan "below the device rating" and the HZ-003 effect "junction can pass 150 C, with device failure". At 45 C the heat sink reaches 95 C only when the in-situ resistance is 12.2 K/W or more, more than twice the design point. A sensor on the heat sink is also decoupled by the heat-path fault it is meant to back up. A lifted spring or gap pad (HZ-003 C2) leaves the heat sink cool while the board heats. A with a pedestal gives 135.8 C, and D gives 140.0 C. **(b) Sensor at the PA pad** (the top-side thermal pad of the PA): trip at about Tj = 95 + 4.1 x 3.0 = 107.3 C. The REQ-SYS-181 rationale requires the band 92 to 98 C to lie above the 88 C upper bound of REQ-SYS-118, "so firmware acts first". Under (b) that order rests only on the two thresholds at one node. Under (a) it rests on location. The study states neither reading. Its section 8 rules place the PA pad and the heat sink but give no sensor mount, no wire route to a removable part, and no keep-out in `board-outline.json`. It sends no request to the hazard, requirement or thermal writers. The ranking does not change, because the 9.44 K/W from the junction to the heat-sink entry is in every surviving option (D adds 0.74 K/W). **Why Major:** the answer decides whether K9 holds the junction below the device rating in the recommended design. That is a safety conclusion the owner needs at B1b (rule C9), not a record-keeping gap. **Fix:** (1) In section 8, add a rule that names the REQ-SYS-181 sensing point for C1 and A. Put it on the board at the PA thermal pad, as K9 reads, or on the heat sink with the threshold re-derived. Give its mount and route, and the matching `board-outline.json` keep-out. (2) In section 4.1 M9 or section 7, state the junction temperature at which K9 trips for each surviving option, and state the heat-sink-decoupling case. (3) In section 8 "Impacts", add three requests. To WP-PDR-16b: align the HZ-003 K9 sensing point with REQ-SYS-181. To the REQ-SYS-181 writer (WP-PDR-11, then 02, then 45; plan section 5.3): the matching wording. To WP-PDR-28: confirm the 95 C threshold against the device rating on the chosen chain (WP-PDR-28 output "relation to the 95 C cutoff and 85 C firmware inhibit"). INSP-081 finding-1 (heat-sink resistance) and cross item X-2 are related. They are not raised again here. This finding adds the K9 placement and effectiveness, which INSP-081 does not raise | Open | Pending | |
| <a id="finding-2"></a>finding-2 | assurance | Minor | `swe-134 7.1 task 6`, `swe-080 7.1 task 1`, SA-C-j | TS-011 section 1 finding 1; section 3.1 M4 and C3; section 4.1 M4 heat-sink table; section 6 item 5 | **At the C1 design point, the safety-critical firmware inhibit acts before the REQ-SYS-112 case that M4 and C3 score.** REQ-SYS-118 senses "the PA thermistor at the PA device on the board thermal pad" and ends RF above 85 C +/-3 C. On the study's chain, that pad runs 4.1 x 3.0 = 12.3 K below the junction. At the M4 condition (45 C, 4.1 W continuous, 5.5 K/W), C1's pad is at 95.2 C, so the inhibit ends RF at Tj about 97.3 C (94.3 to 100.3 C across the tolerance band). The 107.5 C of M4 is never reached in operation. In continuous key-down, C1 reaches the inhibit at an ambient of about 34.8 C, D at 38.8 C and A at 45.9 C. At 80 % duty and 45 C, C1's average pad temperature is 85.1 C, at the threshold. The safety conclusion holds: the inhibit is on the safe side, and it caps the junction below 110 C while the thermistor works. However, the study presents C3 as a 2.5 K junction margin and section 1 finding 1 as a pass at 107.5 C. It does not state that the operating limit of every surviving option in hot ambient is the safety-critical inhibit, whose threshold and fold-back are TBR (HZ-003 K2; WP-PDR-28 output "whether a firmware thermal fold-back requirement is needed"). As a result, the owner sees neither the operational cost (OPS-014 "HOT: wait" in warm ambient) nor the input to the threshold decision. **Fix:** add one sentence to section 4.1 M4 and to section 6 item 3. Give the pad temperature and the ambient at which REQ-SYS-118 acts for A, C1 and D. Add it to the WP-PDR-28 inputs in section 8 "Impacts" with the chain values (pad-to-junction 12.3 K; pad-to-heat-sink 27.6 K for C1) | Open | Pending | |
| <a id="finding-3"></a>finding-3 | assurance | Minor | `swe-080 7.1 task 2`, SA-E3 | Freeze commit `70a3a33`, trailers | The commit that creates TS-011 and the other WP-PDR-27 products has no `Refs:` trailer, although it touches 05 Table 4-1 rows 12, 23, 24, 33 and 49. Its only trailer is `Co-Authored-By` (`git log -1 --format='%B' 70a3a33`). 05 section 4.5 requires `Refs:` on every commit that touches a Table 4-1 row file. `tools/check_commit_msg.py --range 70a3a33^..70a3a33` reports "FAIL REFS_MISSING 70a3a33: touches rows 12, 23, 24, 33, 49 and has no Refs: trailer". That tool is not yet accredited (TV-019), so the trailer read above is the evidence. No class-CR row is past its CR-from event, so no `CR:` trailer was needed. This is the INSP-074 finding-4 pattern (`9ac2c42`). **Fix:** history is not rewritten. The lead SE lists `70a3a33` in the CSA change log as a RID candidate for the PDR (the `configuration-status.md` practice for commits without mandatory trailers), and the TS-011 revision commit carries `Refs: TS-011` (or `Refs: WP-PDR-27`) | Open | Pending | |

One Major finding is open, so the assurance verdict is NEEDS CHANGES (rule C1). Finding-1 does not change the ranking or say that C1 is the wrong choice. It says that the recommended design must name where the firmware-independent thermal cut-off senses, and must show that the cut-off still bounds the junction there. INSP-081's two Major findings (the heat-sink resistance and the boss temperature) stand on their own. Their fixes change the chain values that finding-1 and finding-2 use, so all three are fixed on the same revision.

### Task table

| Task | Safety-critical designation (SWEHB 8.10 section 6) | Applied | Result and evidence | Relief (N/A only) | Finding ids |
|---|---|---|---|---|---|
| swe-134 7.1 task 5 | SC | Yes | This record is the assurance participation in the review of a product that 07 section 2.1.1 routes (row "Trade studies and ADRs", safety-critical column Yes) | | none |
| swe-022 7.1 task 1 | SC | Yes | Performed against the project software assurance plan, 07 section 15, with this template. The NASA-STD-8739.8 part is relieved (next column) | NASA-STD-8739.8 part: `rmm.json` SWE-022 T (standard not in the corpus) | none |
| swe-033 7.1 task 1 | | Yes | No software make-or-buy option arises. The decision buys hardware only (heat sink, port block, coating, film, gasket) and prints the case. The firmware runtime make/buy stays TS-002's (07 section 17.2). No vendor software, firmware or generated data comes with any purchased part | | none |
| swe-033 7.1 task 2 | SC | Yes | No software acquisition activity exists, so no software engineering, assurance or safety requirement needs flowing to a supplier. The hardware selection rules that carry HZ-003 (section 8 rule 3, heat sink) are an engineering matter. Their omission of the K9 sensor is finding-1 under swe-057 and swe-134 | | none |
| swe-033 7.1 task 3 | | Yes | Section 7 assesses ten risks in the four-part format (checked in INSP-081 CK-RSK-B8). No software acquisition risk exists. The software-side thermal risk goes to SA-F1 | | none |
| swe-039 7.1 task 4 | | Yes | Trade study and source data assessed. The screen was re-run on a `git archive 70a3a33` export in the scratchpad: `thermal_screen.py --check` and `trade_matrix.py --check` each gave "CHECK PASS". The regenerated `thermal-screen.csv` (`a8c7d5b1`) and `trade-matrix.txt` (`c6023d69`) are byte-identical to the frozen blobs. The node temperatures that findings 1 and 2 use come from `steady()` and `r_junction_to_entry()` of the same script, evaluated at 4.1 W and 45 C for A, C1 and D. Source-data confidence is copied as the study states it (Low for the heat sink and the recalled coating data) | | none |
| swe-057 7.1 task 2 | | No | The decision fixes part of the physical architecture that the `SW-SAFE` thermal unit and K9 depend on: heat path, heat-sink part and mounting, and PA pad position (section 8 rules 1 to 3, 5). It does not show that the REQ-SYS-181 safety requirement is met in that architecture | | finding-1 |
| swe-134 7.1 task 4 | SC | Yes | Partitioning and isolation are unchanged. The decision adds no software component, datum or interface type. The thermistor input and the inhibit path of the thermal unit keep the isolation of 07 section 5 item 5 and CS-39. K9 stays independent of firmware in every option | | none |
| swe-134 7.1 task 6 | SC | No | The SWE-134 implementation must stay consistent with the hazard analysis. For item i, the thermistor-failure bound (REQ-SYS-181) depends on a sensing point that `hazards.json` K9 and REQ-SYS-181 state differently, and that C1 makes material (finding-1). For item j, the relation of the inhibit threshold to the scored junction case is not stated (finding-2) | | finding-1, finding-2 |
| swe-027 7.1 task 1 | | N/A | Condition not met: the decision acquires no COTS, GOTS, MOTS, OSS or reused software (07 section 17.1 register unchanged) | Conditional task of the section B row ("reused or OSS component chosen"); 07 section 17.1 | none |
| swe-136 7.1 task 1 | | N/A | Condition not met: the decision selects no software tool, emulator or model for the software. The OpenSCAD and slicer files of the release package produce hardware under ADR-008 and TV-015. The screen scripts are stated as developer evidence without a TV record (section 3.4; section 6 item 6) | Conditional task of the section B row ("when the decision selects a tool"); 07 section 17.3 | none |
| swe-070 7.1 task 1 | | N/A | As swe-136: no model or simulation qualifies flight software or equipment here. The thermal screen is decision support, and WP-PDR-28 supersedes it | Conditional task of the section B row; 07 section 17.3 | none |
| swe-205 7.1 task 1 | SC | Yes | HZ-003 C4 names the software contributions: "Thermal fold-back or inhibit does not act: sensor reading cold, wrong threshold, stalled monitor task". These cover inaction (stalled monitor, cold sensor) and incorrect action (wrong threshold). The action contribution, power and bias set by firmware, is criterion b in `firmware_role.statement`. The decision adds no software contribution. It changes the size of the "wrong threshold" cause through the chain, which task 6 carries | | none |
| swe-205 7.1 task 3 | SC | Yes | No software component is added or moved. The 07 section 14.1 "Thermal protection" row (`SW-SAFE` thermal unit with `SW-TXSEQ` actuation) and HZ-003 `firmware_role.components` stand for every option | | none |
| swe-080 7.1 task 1 | SC | No | A hardware change that feeds a software product is analysed for its safety impact. The heat path and heat sink set the temperatures that the thermal unit reads and that K9 senses. The study states the impact on neither (findings 1 and 2) | | finding-1, finding-2 |
| swe-080 7.1 task 2 | | No | Change route of the product files: the Record-class TS-011 (05 Table 4-1 row 12) and the row 23, 24, 33 and 49 files are created at the F0 freeze without the `Refs:` trailer that 05 section 4.5 requires | | finding-3 |
| swe-081 7.1 task 2 | SC | Yes | The safety-relevant product and its hazard data are under configuration management. TS-011 and its eight files are committed at `70a3a33`. `docs/safety/hazards.json` is row-controlled with the single writer WP-PDR-16b (plan section 5.3) | | none |
| swe-086 7.1 task 1 | | Yes | The study serves RSK-006 (tag `software`, Open) and RSK-026. It sends its risk entries to the register writer WP-PDR-18 as requests (section 7 "Would be entered as"): RSK-006 merge, RSK-007, RSK-053, TPM-001 and the CR-003 candidates. This follows plan section 5.3. The assurance risk of SA-F1 goes the same way | | none |
| swe-087 7.1 task 2 | | Yes | The six findings of INSP-081 are Open with named fixes. No finding is closed without evidence (iteration 1) | | none |
| swe-089 7.1 task 1 | | Yes | INSP-081 carries the SWE-089 measurements (front matter `effort_turns` 60, `effort_minutes` 95, finding counts, `items_no`, and its Measurements section). This record carries its own | | none |

## Readiness criteria

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | Product committed and frozen; `product_files` equal to the paired record's | Yes | `git rev-parse 70a3a33:<path>`, `git rev-parse HEAD:<path>` and `git hash-object <path>` for the nine files: `8d2708f1`, `27dbacc7`, `78892ca2`, `20815e75`, `c76b0f70`, `a8c7d5b1`, `c6023d69`, `47d81e61`, `ff8aa6c2`, equal to INSP-081 `product_files`. TS-011 history: only `70a3a33` |
| R2 | Product type and criticality identified | Yes | 07 section 2.1.1 row "Trade studies and ADRs whose decision constrains a safety-critical ... component" (`trade-study-or-adr`). Criticality safety-critical by the 07 section 14.1 row "Thermal protection" (`SW-SAFE` thermal unit with `SW-TXSEQ`, HZ-003, criteria b and e), the same as INSP-081 |
| R3 | `validate_docs.py` on the product files; `traceability.py --report-only --output <scratch>` clean for the ids the product touches | Yes | `traceability.py --report-only --output` to the scratchpad: exit 0, "245 requirements, 173 test cases, 0 violation(s), 2 warning(s)" (REQ-SYS-125 and REQ-SYS-148, not touched by TS-011); `git status docs/vv` clean. `validate_docs.py`: see the Commands section |
| R4 | Paired file review filed under its own invocation; this reviewer is neither author nor file reviewer | Yes | INSP-081 `author_agent` "author:WP-PDR-27 wave 1a (Claude as ME designer)", `reviewer_agent` "reviewer:WP-PDR-27-ts-011-iter1"; this record `reviewer_agent` "sa-reviewer:WP-PDR-27-ts-011" |

## A. Dispatch, independence and record integrity

| Id | Answer | Evidence |
|---|---|---|
| SA-A1 | Yes | 07 section 2.1.1 row 3, safety-critical column Yes. The study fixes the heat path, which constrains the `SW-SAFE` thermal unit and its `SW-TXSEQ` actuation (07 section 14.1 "Thermal protection") |
| SA-A2 | Yes | Three invocations: author "author:WP-PDR-27 wave 1a", file reviewer "reviewer:WP-PDR-27-ts-011-iter1", assurance reviewer "sa-reviewer:WP-PDR-27-ts-011". INSP-081 names this pair as a separate invocation (its `assurance_reviewer_agent` "pending (separate invocation; paired record ...)") |
| SA-A3 | Yes | Same product, same nine blobs, same commit `70a3a33`. No product change after either review |
| SA-A4 | Yes | INSP-081 applied `peer-review-checklist-risk.md` section B, the checklist 08 section 3.5 assigns to trade studies. Items B1 to B10 are answered with evidence, and B5, B7 and B8 are answered No with six findings. `swe-088` 7.1 task 1, criteria a to d: checklist used, readiness recorded (R1 to R4), findings tracked with state, measurements recorded |

## B. SWE-to-task table

| Id | Answer | Evidence |
|---|---|---|
| SA-B1 | Yes | The task table holds every task of the rows `trade-study-or-adr` and "Every product type". It adds swe-205 task 1, swe-080 tasks 1 and 2, swe-081 task 2, swe-086, swe-087 task 2 and swe-089 for the SWEs the product implements or touches. `assurance_tasks_applied` lists every Yes and No row |
| SA-B2 | Yes | The three N/A rows (swe-027, swe-136, swe-070) are conditional tasks whose condition is not met, each with the 07 section named. No SC task is N/A |
| SA-B3 | Yes | Each No row cites a finding (finding-1 to finding-3) |

## C. SWE-134 items a to l (trade-study maturity: the recommendation neither precludes nor weakens the 07 section 14.2 provision)

| Id | Answer | Evidence |
|---|---|---|
| SA-C-a | Yes | The thermal-unit row a provision holds for every option: the temperature prerequisite of `PA_EN` is false until the first valid in-range reading. It does not depend on the enclosure |
| SA-C-b | Yes | The `SW-TXSEQ` states and the thermal inhibit transition are unaffected. The decision adds no mode |
| SA-C-c | Yes | `safe_state()` drives `PA_EN` low first (07 section 14.2 row c) in every option |
| SA-C-d | Yes | Rev A offers no override of the thermal inhibit (07 section 14.2 row d), and the study adds none |
| SA-C-e | Yes | The `PA_EN` sequencing rejections (row e) do not depend on the enclosure |
| SA-C-f | Yes | The thermal thresholds are range-checked fields of the configuration guard (07 section 14.1). Their values are TBR (finding-2 feeds them), and the guard provision is not affected |
| SA-C-g | Yes | The range check of REQ-SYS-155 (-20 C to +150 C) is not precluded. The pad runs at most about 95 to 100 C in operation for C1, so the upper bound keeps its fault-detection meaning. The plausibility cross-check with the RP2350 on-die sensor (REQ-SYS-155 rationale, an L2 item) needs the pad-to-board offset, which differs by option. WP-PDR-28 carries it |
| SA-C-h | Yes | "PA temperature below the inhibit limit" stays a single `PA_EN` prerequisite (07 section 14.2 row h) in every option |
| SA-C-i | No | 07 section 14.2 row i: "the thermistor-failure branch is bounded only by the hardware PA over-temperature cut-off (REQ-SYS-181, 95 C)". The bound depends on the sensing point, which the study leaves undefined. On the C1 heat sink it corresponds to Tj about 135 C (finding-1) |
| SA-C-j | No | Row j: "a reading above 85 C ends RF within 100 ms". The 100 ms response is not affected. The relation of the sensed pad to the hazardous junction is 12.3 K on the study's chain, which makes the inhibit the operating limit before the scored REQ-SYS-112 case. The study does not state it (finding-2). The thermal time constants (C1 heat-sink node about 246 s, INSP-081) are long compared with 100 ms |
| SA-C-k | Yes | Sensor and ADC errors degrade to inhibit (row k) in every option |
| SA-C-l | Yes | Over-temperature leads to SafeState on repeat (row l) in every option |

## D. Software safety analysis and hazard traceability

| Id | Answer | Evidence |
|---|---|---|
| SA-D1 | Yes | HZ-003 C4 names the software contributions (task table, swe-205 task 1). The SWEHB `swe-205` section 7.7.2 considerations were walked. **Control of safety-critical hardware:** firmware sets PA bias and power (criterion b). **Inhibits:** K2, with K9 as the firmware-independent layer. **Common-cause faults:** a heat-path fault that also decouples a sensor mounted on the heat sink (finding-1). **Operator disabling of controls:** none in rev A. No software contribution is missing from `hazards.json`. The common-cause point concerns the hardware control K9 and is carried by finding-1 |
| SA-D2 | Yes | The components the decision constrains are in 07 section 14.1 with criteria b and e, the union of HZ-003 `firmware_role.criteria`. No component is added or renamed |
| SA-D3 | N/A | No software requirement is written at trade maturity. The system ids the study touches (REQ-SYS-112, 113, 181) report no traceability violation (R3) |
| SA-D4 | N/A | No safety-tagged software requirement is written by this product |
| SA-D5 | N/A | No hazard-tracing software requirement is written by this product |
| SA-D6 | No | The software safety analysis rests on K9 bounding the thermistor-failure branch (`hazard-analysis.md` HZ-003 row, residual "Critical-E Low with K9, REQ-SYS-181"). The study changes the chain on which that bound depends and sends no update request (finding-1) |

## E. Peer review, change and configuration assurance

| Id | Answer | Evidence |
|---|---|---|
| SA-E1 | Yes | Iteration 1: there are no earlier iterations. INSP-081's six findings are Open with named fixes |
| SA-E2 | Yes | Both records carry the SWE-089 fields (front matter) |
| SA-E3 | No | `70a3a33` has no `Refs:` trailer (finding-3). No `CR:` trailer was required: TS-011 is Record class, and rows 23, 24, 33 and 49 are not past their CR-from event |
| SA-E4 | N/A | Test and code rows only; there is no test or credit run here |

## F. Assurance risks, metrics and reporting

| Id | Answer | Evidence |
|---|---|---|
| SA-F1 | Yes | One assurance concern that is not a product defect goes to the register writer WP-PDR-18, as a member of RSK-006 (tag `software`) with tag `assurance`. It reads: "Given thermal thresholds for the firmware inhibit (REQ-SYS-118) and the hardware cut-off (REQ-SYS-181) that are derived from a lumped screen whose heat-sink resistance is Low confidence and whose sensing points are not yet fixed, there is a possibility that the PDR values of the `SW-SAFE` thermal unit and of K9 are set on a chain that the built unit does not have, adversely impacting the SWE-134 i and j provisions of 07 section 14.2 for HZ-003, leading to a re-derivation of safety-critical thresholds after CDR and a re-run of TC-SYS-081 and TC-SYS-109." The lead SE forwards it (cross item X-3) |
| SA-F2 | Yes | Front matter: findings by severity and state, `assurance_findings_major` 1, `assurance_findings_minor` 2, `items_no`, effort |
| SA-F3 | Yes | The package "Software assurance findings" section can take from this record: assurance verdict NEEDS CHANGES; one Major and two Minor findings, all Open; 17 tasks applied, 3 N/A with their conditions; SWE-022 relief used |

## Cross items for the lead SE (not findings on TS-011)

- **X-1.** INSP-081 still reads `assurance_reviewer_agent: "pending (...)"` and `assurance_verdict: pending`, and it has no `paired_record`. Its reviewer updates it to `paired_record: INSP-087`, names this reviewer and copies `assurance_verdict: NEEDS CHANGES` (07 section 10.2 Record row). Record verdicts then follow rule C1 and the lead SE convention for the branch-only template.
- **X-2.** The sensing-point conflict between `hazards.json` HZ-003 K9 ("a second NTC at the PA") and REQ-SYS-181 and TC-SYS-109 ("heat-sink sensor") exists in the baseline whatever TS-011 decides. The TS-011 fix names the point for the design. The two data files are aligned by their writers: WP-PDR-16b for `hazards.json`, and the plan section 5.3 writer order for `requirements.json` and `test_cases.json`. The lead SE routes both requests with the TS-011 revision.
- **X-3.** The SA-F1 risk request goes to WP-PDR-18, the register's single writer (plan section 5.3).
- **X-4.** The WP-PDR-28a brief should carry finding-1 part (3) and the finding-2 chain values, together with INSP-081 cross item X-2. WP-PDR-28 owns "relation to the 95 C cutoff and 85 C firmware inhibit" and "whether a firmware thermal fold-back requirement is needed".
- **X-5.** The TS-004 decision (1.0 mm board) sets the 4.7 K/W via term of the same chain. Its record INSP-082 is outside this pair's scope. If the lead SE routes TS-004 to assurance on the same basis, the chain values of findings 1 and 2 apply there too.

## Commands

- `git rev-parse 70a3a33:<path>`, `git rev-parse HEAD:<path>`, `git hash-object <path>` for the nine product files: equal to `product_files`.
- `git archive 70a3a33 hardware/sim/enclosure hardware/enclosure docs/reviews/PDR/figures` into the scratchpad; `.venv/bin/python hardware/sim/enclosure/thermal_screen.py --check` and `trade_matrix.py --check`: exit 0, "CHECK PASS"; the regenerated CSV and matrix output hash to `a8c7d5b1` and `c6023d69`.
- Node temperatures: `steady()` and `r_junction_to_entry()` of `thermal_screen.py`, imported in the venv, at 4.1 W and 45 C. C1: heat-sink node 67.5 C, entry 68.8 C, Tj 107.5 C, pad 95.2 C. Tj at a 95 C heat-sink sensor: A 135.8 C, C1 134.9 C, D 140.0 C. Tj at 95 C on the pad: 107.3 C. Tj at the 85 C inhibit on the pad: 97.3 C. Ambient at which the pad reaches 85 C in continuous key-down: A 45.9 C, C1 34.8 C, D 38.8 C. C1 at 80 % duty: Tj 95.0 C, pad 85.1 C.
- `.venv/bin/python tools/traceability.py --report-only --output <scratchpad>/traceability-report.md`: exit 0, 0 violations; `docs/vv/` unchanged.
- `.venv/bin/python tools/check_commit_msg.py --range 70a3a33^..70a3a33`: "FAIL REFS_MISSING" (tool not accredited, TV-019 pending; the evidence is the commit message itself).
- `.venv/bin/python tools/validate_docs.py`: this record passes (see the return).

## Visual closure

Both product figures were opened with the Read tool:
- `docs/reviews/PDR/figures/ts011-thermal-screen.png` (`47d81e61`): the left panel shows the hottest accessible face against time for seven cases, with the 48 C line and the 5 min marker. The right panel shows the steady junction per option against the dashed 110 C line (C1 108, A 96, D 104, rounded). It shows no sensor or inhibit threshold, which is consistent with finding-2.
- `docs/reviews/PDR/figures/board-outline-envelope.png` (`ff8aa6c2`): the plan view shows the heat sink 40 x 58 under the 15 x 15 PA pad at the +X end, with six bosses. The X-Z section shows the heat sink below the board and through the back wall behind the guard. Neither view shows a thermistor, a cut-off sensor or a keep-out for either, which is consistent with finding-1.

## Measurements (SWE-089)

Tasks in the table: 20 (17 applied, 3 N/A). Tasks answered No: 4. Checklist items answered No: 4 (SA-C-i, SA-C-j, SA-D6, SA-E3). SWE-134 items checked: 12. Findings: 1 Major, 2 Minor, all Open. Iteration 1. Renders inspected: 2. Effort: 30 turns, about 55 minutes.
