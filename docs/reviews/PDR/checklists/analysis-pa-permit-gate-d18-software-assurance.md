---
# Peer-review record front matter (charter sections 2 and 5; docs/process/01-lifecycle-and-reviews.md
# section 13 is the single field list; docs/process/07-software-engineering-plan.md sections 2.1.1, 10.2
# and 15). This is the software assurance pair of the WP-PDR-22 D-18 analysis (PDR work plan revision 7,
# section 3.0 row 22: "SA pair"; WP-PDR-22 section: "Reviewer: independent reviewer plus SA (cutoff and ALC
# units)"). The gate is part of the HZ-004 K5 and K8 controls, whose firmware side is SW-SAFE (PA_EN
# writer), SW-KEYER (TX_KEY drive) and SW-TXSEQ, all safety-critical in 07 section 14.1.
# Checklist applied: docs/templates/peer-review-checklist-software-assurance.md revision A AS ON ITS CR-012
# BRANCH (cr/CR-012-pdr-checklist-templates at 7784672, blob 5b13528504868b2add0f0b1e329c63aa2b54cdf4; not
# merged, absent from main at f8dcf8c). tools/validate_docs.py fails a record whose `checklist` names a
# template absent from main, so `checklist` names peer-review-checklist-design at its main revision B (the
# INSP-111 form); `assurance_checklist` names the template actually applied.
# id: the brief assigned no id. The highest id on main (f8dcf8c), on every local branch and in the working
# tree is INSP-118. Iteration 1 of this record (returned as record text, not filed at f8dcf8c) proposed
# INSP-120 and left INSP-119 for the paired file review. The lead SE confirms or renumbers the id when filing.
# Filing note: this text is the whole record, iteration 1 (verbatim from its returned record text, only its
# title line split into the record title and an "Iteration 1" heading) and iteration 2 (the delta below).
id: INSP-120
checklist: peer-review-checklist-design
checklist_revision: B
assurance_checklist: "docs/templates/peer-review-checklist-software-assurance.md@5b13528504868b2add0f0b1e329c63aa2b54cdf4 (revision A, branch cr/CR-012-pdr-checklist-templates at 7784672)"
checklist_file: docs/reviews/PDR/checklists/analysis-pa-permit-gate-d18-software-assurance.md
product: docs/design/analysis/pa-permit-gate-d18.md
# product_commit and product_files (iteration 2, the delta; rule C2 re-freeze F0): pa-permit-gate-d18.md
# revision 1 with the revision 1 checker, decks and runs 2026-09-29-d18r1-*, committed at c397ab1 on main
# (git merge-base --is-ancestor c397ab1 main is true). Each blob equals git rev-parse c397ab1:<path>, git
# rev-parse HEAD:<path> at HEAD f8dcf8c and git hash-object <path> (git diff --stat c397ab1 HEAD on the
# product paths, docs/safety, docs/requirements, TS-012 and 07 is empty). The record blob a6bcc2b1 and the
# script blob 5a06cfd8 equal the author summary. The three d18r1 run folders hold d18_run.py at the same
# blob 5a06cfd8. The generated decks are byte-identical to the run copies (cmp). d18r1-keyup/d18_keyup.raw
# (11,633,088 bytes) is untracked under CR-017 C2; its SHA-256 04fb27d3...96ff5 equals the committed
# raw.sha256. The as-drawn run 2026-09-29-d18-asis of revision 0 is reused unchanged (deck blob 191ba96d).
product_commit: "c397ab171b4c564c402f806bd617a796e74a96d1"
product_files: ["docs/design/analysis/pa-permit-gate-d18.md@a6bcc2b14710730d6c5bee3a61a4cbcfda919e19", "hardware/sim/tx-pa-permit/README.md@f085dc40f83668fda775303dd5d2a734462dde5d", "hardware/sim/tx-pa-permit/d18_run.py@5a06cfd879f2f885a42f41fcb7667be42abaa48e", "hardware/sim/tx-pa-permit/d18_keyup.cir@bce02858a570d9f7decc4d9910fe73caaee0ecea", "hardware/sim/tx-pa-permit/d18_asis.cir@191ba96d9acfbf5cbebd7401458080297567ce68", "hardware/sim/tx-pa-permit/d18_seq.cir@de50be4d518f8a117e7b1ce627d72e7f91e695c5", "hardware/sim/tx-pa-permit/results/2026-09-29-d18r1-keyup/result.json@72ec935d2d26d0d0c5285b4f4a0de2825f9c8215", "hardware/sim/tx-pa-permit/results/2026-09-29-d18r1-keyup/raw.sha256@fcfa74faa7999ed69eeba0440ed0fa0b35b3992d", "hardware/sim/tx-pa-permit/results/2026-09-29-d18r1-keyup/keyup_timeline.png@0f2baec0ca34108fb9dc60decd743494620ab0c6", "hardware/sim/tx-pa-permit/results/2026-09-29-d18r1-keyup/keyup_edges.png@28d9fde0d5c8c48daceac94de4ff6a770e853d05", "hardware/sim/tx-pa-permit/results/2026-09-29-d18r1-keyup/keyup_metrics.png@6a09ad7a48e070b0b6e568de76126ea0a0cb46f1", "hardware/sim/tx-pa-permit/results/2026-09-29-d18r1-keyup/level_cases.png@1e96eecf124c3acaf937807924b5c2d2bb8cd99e", "hardware/sim/tx-pa-permit/results/2026-09-29-d18r1-keyup/off_states.png@07640f12eab0dbb725dfeb3b8f54696d6c08a2ee", "hardware/sim/tx-pa-permit/results/2026-09-29-d18r1-seq/result.json@66e3ce29fb12b01ede582f40533a84e6a9a59414", "hardware/sim/tx-pa-permit/results/2026-09-29-d18r1-seq/d18_seq.raw@78d72824b470f439e1cefe59e75ba7ae5e9f6d71", "hardware/sim/tx-pa-permit/results/2026-09-29-d18r1-seq/seq_cases.png@2b60e05ff102ab1ed99accaa4807b4ceef70a2aa", "hardware/sim/tx-pa-permit/results/2026-09-29-d18r1-seq/cutoff_levels.png@34e92fde1007c0c021fa4ce63f06e94bcab3f753", "hardware/sim/tx-pa-permit/results/2026-09-29-d18r1-summary/summary.json@df81781b6176c18fe729cb340c717cd0489696e6", "hardware/sim/tx-pa-permit/results/2026-09-29-d18-asis/result.json@1b1a51f9f521260e65007c3a3f429721b5f093dc", "hardware/sim/tx-pa-permit/results/2026-09-29-d18-asis/raw.sha256@9072b7b3276aa1905b5366841e65e6b02dcebcee", "hardware/sim/tx-pa-permit/results/2026-09-29-d18-asis/asis_keyup.png@3fb64a679b62fb090e8b3afb498e0eee150d5476"]
product_commit_iteration_1: "078f2f7618be52a9d35d2133e77778c8d0582d17"
product_files_iteration_1: ["docs/design/analysis/pa-permit-gate-d18.md@b8361270902be239833ca9e33e1a2571226c9a3c", "hardware/sim/tx-pa-permit/README.md@cf1c08881eaf66756e469ae8f1994a6a514fab9c", "hardware/sim/tx-pa-permit/d18_run.py@a6916e0fb481586516c7e7901d45c3a4fc4c442a", "hardware/sim/tx-pa-permit/d18_keyup.cir@c0bdd5158cacc9882626b7f8bf0930105950f5b7", "hardware/sim/tx-pa-permit/d18_asis.cir@191ba96d9acfbf5cbebd7401458080297567ce68", "hardware/sim/tx-pa-permit/d18_seq.cir@16ea43784e87230b66f2e13f2a0b8ae7526e4e39", "hardware/sim/tx-pa-permit/results/2026-09-29-d18-keyup/result.json@ee1c17713701dae4c97ba1a9ab7cacb6129c9e1d", "hardware/sim/tx-pa-permit/results/2026-09-29-d18-keyup/raw.sha256@4584e215e2e6193cff4aa389e1c652e9e6416a11", "hardware/sim/tx-pa-permit/results/2026-09-29-d18-keyup/keyup_timeline.png@29a7879235e3ede67f507e861dc13706243ee634", "hardware/sim/tx-pa-permit/results/2026-09-29-d18-keyup/keyup_edges.png@4f639026aaa8d12cced8b42bc45b8737f062b463", "hardware/sim/tx-pa-permit/results/2026-09-29-d18-keyup/keyup_metrics.png@76a212c0e3a50d250a4bfa8c7b853c7e820b18a0", "hardware/sim/tx-pa-permit/results/2026-09-29-d18-keyup/level_cases.png@890bf7cbf4b2a658b36efd0ead7b939e7631c1c7", "hardware/sim/tx-pa-permit/results/2026-09-29-d18-asis/result.json@1b1a51f9f521260e65007c3a3f429721b5f093dc", "hardware/sim/tx-pa-permit/results/2026-09-29-d18-asis/raw.sha256@9072b7b3276aa1905b5366841e65e6b02dcebcee", "hardware/sim/tx-pa-permit/results/2026-09-29-d18-asis/asis_keyup.png@3fb64a679b62fb090e8b3afb498e0eee150d5476", "hardware/sim/tx-pa-permit/results/2026-09-29-d18-seq/result.json@d2741ca5c5c631222a63f7e137de98ea8183c55c", "hardware/sim/tx-pa-permit/results/2026-09-29-d18-seq/seq_cases.png@74a7aeee4411e8b7214738152c9812e6cf4a7fee", "hardware/sim/tx-pa-permit/results/2026-09-29-d18-summary/summary.json@6f2999468754221e855e71153fdcb2e4c75069ac"]
# inputs read at iteration 2 (not reviewed), at HEAD f8dcf8c
input_files_iteration_2: ["docs/plan/pdr-work-plan.md (revision 7; WP-PDR-22 section, rules C1 to C13)", "docs/safety/hazards.json 0.5.0-pha (HZ-004 controls K5, K8, K12, fault_tolerance; HZ-003 fault_tolerance thermistor-failure branch, K9)", "docs/process/07-software-engineering-plan.md (section 14.2 row i)", "docs/safety/hazard-analysis.md (section 7 row l; single-point table rows 1 and 8)", "docs/conops/conops.md (section 3.4 note on the backstop and hardware cut-off, Appendix D item D19)", "docs/decisions/trade-studies/TS-012-design-to-cost-hand-built.md@bb5dee7 (section 8.10 row REQ-SYS-055, 120, 180, 092; row REQ-SYS-181; section 8.14 D-18)", "docs/design/analysis/sequencer-timing.md (inputs row: the D-18 gate turn-on time from revision 0)", "the iteration 1 record text of this record (returned to the lead SE, not filed)", "docs/references/md/swehb/ (swe-057, 080, 134 section 7.1)", "docs/templates/peer-review-checklist-software-assurance.md@5b135285 (git show, branch cr/CR-012)"]
# inputs read at iteration 1 (not reviewed), at HEAD c9f611d
input_files: ["docs/plan/pdr-work-plan.md (revision 7; section 3.0 row 22, WP-PDR-22 section, rules C1 to C13, PR-21)", "docs/decisions/trade-studies/TS-012-design-to-cost-hand-built.md@bb5dee7 (section 7.3 revision 6 'Hardware gate (D-18)' and 'During the over'; section 8.1 diagram 'clamps on the ref/VGG node (wired-OR)'; section 8.10 rows REQ-TX-014, REQ-SYS-055/120/180/092, REQ-SYS-183; section 8.14 D-18)", "docs/decisions/adr/ADR-056-a5-hand-built-design.md (D-18 rows)", "docs/reviews/PDR/checklists/ts-012-design-to-cost-software-assurance.md (INSP-118 finding-9)", "docs/reviews/PDR/checklists/ts-012-design-to-cost.md (INSP-110 finding-24)", "docs/safety/hazards.json 0.5.0-pha (HZ-004 causes C6, C10; controls K5, K6, K8, K12; single_point_failures; fault_tolerance)", "docs/requirements/sys/requirements.json (REQ-SYS-055, 092, 119, 120, 180, 181, 183 with verification notes)", "docs/requirements/tx/requirements.json (REQ-TX-014)", "docs/process/07-software-engineering-plan.md (sections 2.1.1, 4 item 3, 10.2, 14.1, 14.2 rows a, c, e, g, h, i, j)", "docs/process/05-configuration-and-data-management.md (section 9.1)", "docs/research/keyer-verification-and-key-input-network.md (RP2350-E9 quotation, item 5 pad reset states)", "docs/risk/register.json (RSK-024)", "docs/references/md/swehb/ (swe-022, 027, 033, 039, 052, 057, 070, 080, 081, 087, 088, 089, 134, 136, 184, 205 section 7.1)", "docs/templates/peer-review-checklist-software-assurance.md@5b135285 (git show, branch cr/CR-012)"]
paired_record: "not yet filed (file review of the same product, INSP-119 proposed; its iteration 1 and its delta are dispatched by the lead SE under plan WP-PDR-22)"
# product_type: the analysis selects design D18-2B among alternatives (record section 2) and fixes the
# hardware interface of two safety-critical firmware outputs (PA_EN, TX_KEY), so it is routed as the
# 07 section 2.1.1 row "Trade studies and ADRs whose decision constrains a safety-critical ... component"
# (the INSP-111 practice). The template has no analysis row (INSP-032 finding-2, a lien; cross item X-4)
product_type: trade-study-or-adr
# criticality: safety-critical. 07 section 14.1 rows "PA enable and TX sequencer" (SW-TXSEQ, PA_EN gate),
# "Safe-state manager" (SW-SAFE, the PA-permit flag, REQ-SYS-120) and "Keyer and keying output" (SW-KEYER,
# TX_KEY drive); HZ-004 firmware_role.components names all three
criticality: safety-critical
product_size: "iteration 2: 1 analysis note revision 1 (550 lines; git diff 078f2f7 c397ab1 of 206 changed lines: new section 5.8, 6 new static rows, 7 new sequencing cases, F-6 and F-7, R-1 revised), 1 revised checker (1256 lines, 20 sequencing cases, 21 static checks, 4 state windows x 4 isolation cases for REQ-SYS-183), 3 revision 1 runs, 2 new figures. Iteration 1: 1 analysis note revision 0 (434 lines; 10 sections, 5 findings for other records F-1 to F-5, 3 recommendations R-1 to R-3); 1 generator and checker (1026 lines, 16 key-up criteria, 13 sequencing cases, 15 static checks); 3 decks (52, 36 and 13 cases); 4 runs; 7 figures"
sprint: PDR-prep
author_agent: "author:WP-PDR-22 D-18 analysis (Claude, analysis author invocations of 2026-09-29; revision 0, and revision 1 for the two Major findings)"
reviewer_agent: "sa-reviewer:WP-PDR-22-d18-iteration-2"
reviewer_agent_iteration_1: "sa-reviewer:WP-PDR-22-d18-iteration-1"
assurance_required: true
assurance_reviewer_agent: "sa-reviewer:WP-PDR-22-d18-iteration-2 (software assurance function, iteration 2; iteration 1 by sa-reviewer:WP-PDR-22-d18-iteration-1; paired file review not yet filed, dispatched by the lead SE under plan WP-PDR-22)"
# iteration 2 is the delta that verifies the Major fix (rule C1); one more delta iteration is allowed before
# escalation to the owner (07 section 10.2)
iteration: 2
# readiness_met: R1 to R3 hold at iteration 2. R4 holds for independence (this invocation authored no part of
# WP-PDR-22, is not the file reviewer and is not the iteration 1 assurance reviewer); the paired file review's
# delta is dispatched concurrently and not filed at f8dcf8c (cross item X-1)
readiness_met: true
# reviewer_verdict and assurance_verdict at iteration 2: APPROVED. finding-1 (Major) is Verified; no Major is
# open; finding-2 to finding-6 (iteration 1) and finding-7 to finding-10 (iteration 2) are Minor liens (rule C1).
# Iteration 1: NEEDS CHANGES (finding-1)
reviewer_verdict: APPROVED
assurance_verdict: APPROVED
reviewer_verdict_iteration_1: NEEDS CHANGES
assurance_verdict_iteration_1: NEEDS CHANGES
# verdict: set by Claude as software lead (07 section 10.2). Held at NEEDS CHANGES: the paired file review
# (iteration 1 and its delta) is not filed and does not yet name this record, and the checklist applied exists
# only on cr/CR-012-pdr-checklist-templates (lead SE convention of 2026-09-27). The software lead sets APPROVED
# when the paired record carries the pairing with its own APPROVED verdict and CR-012 merges with the template
# blob unchanged
verdict: NEEDS CHANGES
# findings (all iterations): finding-1 (iteration 1, Major, Verified at iteration 2); finding-2 to finding-6
# (iteration 1, Minor, Open liens); finding-7 to finding-10 (iteration 2, Minor, Open liens)
findings_major: 1
findings_minor: 9
findings_open: 9
findings_fixed: 0
findings_verified: 1
findings_deferred: 0
assurance_findings_major: 1
assurance_findings_minor: 9
assurance_tasks_applied: ["swe-134 7.1 task 5", "swe-134 7.1 task 6", "swe-057 7.1 task 2", "swe-080 7.1 task 1", "swe-080 7.1 task 2", "swe-134 7.1 task 1", "swe-205 7.1 task 1", "swe-039 7.1 task 4", "swe-081 7.1 task 2", "swe-087 7.1 task 2", "swe-089 7.1 task 1"]
assurance_tasks_applied_iteration_1: ["swe-134 7.1 task 5", "swe-022 7.1 task 1", "swe-033 7.1 task 1", "swe-033 7.1 task 2", "swe-033 7.1 task 3", "swe-039 7.1 task 4", "swe-057 7.1 task 2", "swe-134 7.1 task 4", "swe-134 7.1 task 6", "swe-136 7.1 task 1", "swe-070 7.1 task 1", "swe-205 7.1 task 3", "swe-134 7.1 task 1", "swe-205 7.1 task 1", "swe-184 7.1 task 1", "swe-052 7.1 task 2", "swe-080 7.1 task 1", "swe-080 7.1 task 2", "swe-081 7.1 task 2", "swe-087 7.1 task 2", "swe-089 7.1 task 1"]
swe134_items_checked: [a, c, e, g, i, j, l]
swe134_items_checked_iteration_1: [a, c, e, g, i, j, l]
deferred_rids: []
# items_no at iteration 2: the rows applied in the delta that still answer No, each carrying an open Minor
# lien; the iteration 1 No rows not re-applied (swe-033 task 2, swe-136, swe-070, swe-184, SA-D4) stay with
# their liens finding-3 and finding-6
items_no: ["swe-134 7.1 task 6", "swe-134 7.1 task 1", SA-C-g, SA-C-i, SA-C-l]
items_no_iteration_1: ["swe-033 7.1 task 2", "swe-057 7.1 task 2", "swe-134 7.1 task 6", "swe-136 7.1 task 1", "swe-070 7.1 task 1", "swe-134 7.1 task 1", "swe-184 7.1 task 1", "swe-080 7.1 task 1", SA-C-g, SA-C-i, SA-C-l, SA-D4]
# effort: iteration 1 48 turns, 85 minutes; iteration 2 40 turns, 75 minutes
effort_turns: 88
effort_minutes: 160
record_status: Open
date: 2026-09-29
date_iteration_2: 2026-09-29
date_closed: null
---

# Peer review record INSP-120: software assurance pair of the WP-PDR-22 D-18 PA-permit gate analysis

## Iteration 1 (2026-09-29; revision 0 at 078f2f7)

**Product.** `docs/design/analysis/pa-permit-gate-d18.md` revision 0, blob `b8361270`, with its generator and checker `d18_run.py` (`a6916e0f`), the three decks, the four runs and the seven figures, all committed at the freeze commit `078f2f7` on `main` (rule C2, freeze F0). Every blob of `product_files` equals `git rev-parse 078f2f7:<path>` and `HEAD:<path>` at `c9f611d`. The author summary's frozen record blob `b8361270902be239833ca9e33e1a2571226c9a3c` is the reviewed blob. **Paired record:** the file review of the same product, dispatched under plan WP-PDR-22 and not yet filed (cross item X-1).

**Checklist.** `docs/templates/peer-review-checklist-software-assurance.md` revision A as on its CR-012 branch (`7784672`, blob `5b135285`): readiness R1 to R4, sections A to F, the section B row `trade-study-or-adr` plus the row "Every product type", and the section 7.1 tasks of the other SWEs the product touches (front matter explains the `checklist` field).

**Acceptance criteria (rule C7).**
- The three parts of INSP-118 finding-9 ((a) level interface, (b) unpowered state and power-up order, (c) interval-13 fallback timing) and INSP-110 finding-24, each answered with evidence.
- The WP-PDR-22 D-18 scope of the plan (section 3.0 row 22): gate supply rail, level interface to the 5 V P-FET, unpowered state, and the key-up case that CR-018 needs for the REQ-TX-014 restatement.
- Every HZ-004 control that acts on the gate or on its node: K5 (cutoff monostable, input Q), K6 (pull-downs, reset pad states), K8 (two conditions), and K12 (backstop, "at the same node as K5"; its proposed T/R-drive input). With them, every requirement that shares the VGG node and uses the REQ-SYS-183 level as RF off: REQ-SYS-055, 092, 180, 181.
- The 07 section 14.2 rows the gate implements in hardware for SW-SAFE, SW-KEYER and SW-TXSEQ: a, c, e, g, i, j, l. Rows b, d, f, h and k are firmware functions that the gate neither implements nor constrains.
- The software contributions of HZ-004 walked by action, inaction and incorrect action (SWEHB `swe-205` 7.1 task 1), limited to those the gate changes.

**Independence (rule C4).** This invocation authored no part of WP-PDR-22 (the record, the checker, the decks, the runs, the figures) and no part of TS-012, INSP-110 or INSP-118. It is not the file reviewer of this product. It edited no product file.

**Search first (charter section 11 rule 1).** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: WP-PDR-22 D-18 PA permit gate software assurance review; the software assurance checklist template and its analysis product type). `grep -n`, `sed -n`, `awk` and Python reads of `hazards.json`, `requirements.json` and `result.json` were used afterwards only to pin lines and values. The rustos tree was not read.

## Commands run by the assurance reviewer (evidence)

- `git rev-parse HEAD:docs/design/analysis/pa-permit-gate-d18.md` and `git hash-object` on the working file: both `b8361270902be239833ca9e33e1a2571226c9a3c`. `git diff --stat 078f2f7 HEAD` on the product paths, `docs/safety`, `docs/requirements`, TS-012 and 07: empty.
- `shasum -a 256` of `d18_keyup.raw` and `d18_asis.raw`: `a76348c3...9444` and `954c7259...9fa5`, equal to the committed `raw.sha256` files. The three generated decks equal their run copies (SHA-256 `20048185...`, `74242e81...`, `897d2e12...`), and each `wrapper.txt` records `result: PASS`, LTspice 26.0.2, exit 0 (ACC-LTSPICE-001).
- A Python read of the committed `result.json` files: key-up `all_cases_pass` true for all 16 criteria, `failing_cases` empty; as-drawn 25 of 36 driver powered, 21 of 36 over -30 dBm; all 13 sequencing cases as required or as expected. These equal record sections 5.1, 5.3 and 5.5.
- The isolation chain re-derived by hand: drive -5.27 dBm (`10 log 26.5 + 3.00 - 22.5`), bound -0.49 dBm, unpowered GVA-84+ 19.57 dB, break-even 21.23 and 26.01 dB, L1 -58.34 dBm and L4 -33.99 dBm. All equal the record.
- The checker's own `antenna_dbm()` imported read-only (`sys.dont_write_bytecode`, working tree left clean) and evaluated with the driver powered (TX5 4.75 and 5.2 V) and VGG clamped (7.9 mV): L1 -16.0 / -14.7, L2 -15.4 / -14.7, L3 -46.0 / -44.7, L4 -10.6 / -9.9 dBm (finding-1).
- `tools/check_commit_msg.py --range 078f2f7~1..078f2f7`: `PASS 078f2f7: rows 24, 49; Refs: REQ-TX-014, REQ-SYS-120, HZ-004, INSP-118, INSP-110, TS-012, WP-PDR-22`.
- `tools/validate_docs.py` at `c9f611d`: 110 passed, 7 failed; all 7 are record drift on other products' records, none on this product. `tools/traceability.py --report-only --output <scratchpad>/traceability-report.md`: 0 violations, 2 warnings (REQ-SYS-125, 148, unrelated). The front matter of this record passes `validate_mapping(PEER_REVIEW_RECORD_SCHEMA)` in memory.
- Figures opened and inspected before citing: `keyup_timeline.png`, `keyup_edges.png`, `keyup_metrics.png`, `level_cases.png`, `asis_keyup.png`, `seq_cases.png`.

## Findings (iteration 1)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | assurance | Major | `swe-134 7.1 task 6`, `swe-057 7.1 task 2`, `swe-080 7.1 task 1`, SA-C-i, SA-C-l | Record section 2 (U1 inputs TX_KEY, PA_EN, Q only); section 5.3 (backwave); section 5.7 row "U1 output stuck high" ("still ends RF in 7.5 to 13 s"); sections 6.1 and 6.2; TS-012 section 7.3 ("The existing wired-OR clamps of REQ-SYS-055, 180, 181 and 092 stay on the same node") | The firmware-independent cutoffs other than K5 clamp only VGG and leave the driver powered, so by the record's own model they reach -9.9 to -16 dBm, not the -57 dBm REQ-SYS-183 level their closing cases require. See the note after this table | Open | Pending | |
| <a id="finding-2"></a>finding-2 | assurance | Minor | `swe-134 7.1 task 6`, SA-D1 | Record sections 2 and 6.2; HZ-004 K12 ("proposed with it, the PA-path gate also requires the T/R transmit drive ... (confirmed at PDR)") | The PDR confirmation of K12's proposed T/R-drive input to the PA-path gate is neither made nor declined. See the note | Open | Pending | |
| <a id="finding-3"></a>finding-3 | assurance | Minor | `swe-184 7.1 task 1`, `swe-134 7.1 task 1`, `swe-033 7.1 task 2`, SA-C-i, SA-D4 | Record sections 1 (table row "HZ-004 K8, 07 section 14.2 row i"), 5.2 (E9 row), 6.2 | The firmware-side conditions on which the gate's safety argument rests are not stated as assumptions or routed as derived software requirements. See the note | Open | Pending | |
| <a id="finding-4"></a>finding-4 | assurance | Minor | `swe-134 7.1 task 1`, SA-C-g, SA-C-l | Record section 5.7 ("latent afterwards" rows F2, F3, P-FET short, U1 stuck high, F4, F5); section 6.4 R-2 ("not needed to close the lien"); section 9 | The latent single faults of the permit path cannot be detected in service, and R-2, the only in-service means, is offered as optional without the hazard reasoning. See the note | Open | Pending | |
| <a id="finding-5"></a>finding-5 | assurance | Minor | SA-C-c | Record section 7 F-3 ("for example by SW-SAFE disabling CLK1 as part of `safe_state()`"); 07 section 14.2 row c | The suggested remedy puts a fallible I2C write into `safe_state()`, against 07 section 14.2 row c. See the note | Open | Pending | |
| <a id="finding-6"></a>finding-6 | assurance | Minor | `swe-136 7.1 task 1`, `swe-070 7.1 task 1` | Record header row "Evidence status"; section 9; REQ-TX-014 verification note ("Pre-build (supporting): Simulation ...") | The checker's output is to be cited as the pre-build evidence of REQ-TX-014 and REQ-SYS-120, but no TV record is planned. See the note | Open | Pending | |

**finding-1 (the other hardware cutoffs do not remove the driver supply).**
- **Defect.** D18-2B removes the GVA-84+ supply only through U1, whose inputs are TX_KEY, PA_EN and Q (section 2). TS-012 keeps the other firmware-independent cutoffs as wired-OR clamps on the reference and VGG node only (section 7.3; section 8.1 diagram: "clamps on the ref/VGG node (wired-OR, on at reset): NAND(TX_KEY, PA_EN, Q) clamp FET, LM393 #2 10 s cutoff, LM393 #1 150-180 s backstop, LM393 #1 95 C trip on the sink NTC (REQ-SYS-181), LM393 #2 cell 60 C, VBUS inhibit"). These cutoffs exist for the case where firmware does not end RF, so TX_KEY and PA_EN can both be high. Q is retriggered by every TX_KEY edge (HZ-004 K5), so it stays high during normal keying or a toggling stream. U1 then permits in each element: the driver is powered and only VGG is clamped.
- **The record's own model gives that state.** It is the backwave of section 5.3, "-14.7 to -16 dBm on L1 and about -10 dBm on L4, with the driver powered and VGG at 0 V", and the 8 to 15 ms span of `keyup_timeline.png`. The reviewer's evaluation with the checker's `antenna_dbm()` at VGG 7.9 mV (the wound-loop clamp level) gives:
  - L1 -16.0 to -14.7 dBm;
  - L2 -15.4 to -14.7 dBm;
  - L3 -46.0 to -44.7 dBm (module at "up to 60 dB");
  - L4 -10.6 to -9.9 dBm.
- **Consequence.** Each of these requirements uses the REQ-SYS-183 level (-57 dBm) as RF off, and each has a closing Test in exactly this state:
  - REQ-SYS-180 (K12), TC-SYS-108: TX_KEY toggled with the firmware timeouts disabled, and RF "stays at the REQ-SYS-183 level until the return to receive";
  - REQ-SYS-181, TC-SYS-109: keyed, "held at the REQ-SYS-183 level at or above T_trip ... while PA_EN stays asserted";
  - REQ-SYS-092, TC-SYS-066: TX_KEY asserted with USB applied.

  The shortfall is 11 to 47 dB in every isolation case, including L3. The same holds for K5's own VGG clamp when U1 fails stuck high: section 5.7 says that clamp "still ends RF in 7.5 to 13 s", but it leaves -14.7 dBm (L1), the level the record gives for F2 in the row above. TS-012 section 8.10 records REQ-SYS-183 as "designed out by the key-up sequence and the D-18 gate", and HZ-004 K12 "removes the PA-path enable at the same node as K5". After D18-2B that is no longer true for K12: K5 now also acts through U1, and K12 does not. SWE-134 item i names these cutoffs as the hardware bounds outside software (07 section 14.2 row i, "Outside software").
- **Why Major.** The D-18 wording that section 6.1 proposes for TS-012 and the schematic (WP-PDR-37), and the K8 safe state of section 6.2, would carry a design that fails three hazard-control closing cases by the record's own numbers. CR-018 is about to rest the REQ-TX-014 restatement and its HZ-004 note on this record. This is not a 5 W exposure: the carrier at power is ended, and the residual is at most about 100 uW. The template's Major rule applies because the row i and row l provisions do not reach the level the hazard controls require at this maturity, and because the product would be wrong and unverifiable as written (07 section 10.2, Method row).
- **Fix (either).**
  - **(a) Bring the cutoffs into the permit.** Put the open-collector outputs of LM393 #1 (the backstop and the sink trip), and the VBUS inhibit where its output allows, on the Q node, under the existing 10 kohm pull-up to the 5 V bus. The Q node then reads "Q and no cutoff", ahead of U1 input C, and each cutoff removes the driver supply as well as clamping VGG. Recheck the Q-high static row of section 5.2 with the added leakage, and the Q-low row with each comparator's VOL. Add sequencing cases with each cutoff asserted while TX_KEY toggles, PA_EN is held high and CLK1 runs, and state the level. With the driver unpowered this is the key-up level: -58.3 dBm on L1, and on the bounds as in section 5.4. This is the node that K12's text already names ("the same node as K5").
  - **(b) If (a) is not adopted,** state in sections 5.7, 6.1 and 6.2 that REQ-SYS-180, 181 and 092 (and K5 under a U1 stuck-high fault) reach only the driver-powered level (-9.9 to -16 dBm; -44.7 dBm on L3). Route it as a defect to TS-012 (D-18 and the section 8.1 diagram), WP-PDR-26 (monostables and trips), WP-PDR-16b (K5, K12 and HZ-003 K9 texts) and the owners of REQ-SYS-180, 181, 092 and 183, before CR-018 carries the restatement.
  - In either case, correct the "still ends RF" wording of section 5.7.

**finding-2 (K12's proposed T/R-drive input is not addressed).**
- **Defect.** HZ-004 K12 says: "proposed with it, the PA-path gate also requires the T/R transmit drive, so a TX_KEY stream with T/R in receive gives no PA output (confirmed at PDR)". This record fixes the PA-path gate at PDR as a three-input AND of TX_KEY, PA_EN and Q. It neither includes the T/R drive nor records the proposal as declined. Section 6.2 proposes K8 wording to WP-PDR-16b without it.
- **Why Minor.** The input is a proposal, not an adopted control. The toggling-stream bound itself is K12's monostable. No stated requirement fails.
- **Fix.** State the choice in sections 2 and 6.2 and route it to WP-PDR-16b:
  - either the T/R drive joins the permit (a four-input part, or an open-collector stage on the Q node as in finding-1 (a)), with a sequencing case;
  - or K12's "PA-path gate also requires the T/R transmit drive" is withdrawn, with the reason.

**finding-3 (firmware-side conditions of the gate's argument are not flowed down).**
- **Defect.** The hardware half is shown correctly: a single line high gives no RF (cases L3, L4 and `pre_permit_off` 0 V). But 07 section 14.2 row i claims more: "a single GPIO write or a single corrupted flag cannot produce RF". With a hardware AND as the combining element, that claim also needs conditions the record neither states as assumptions nor sends to the software writers. The SW-SAFE file must carry "the hardware interlocks assumed" (07 section 4 item 3; SWE-184). The conditions are:
  - (i) **Write-level independence.** TX_KEY and PA_EN are never raised by one write: the RP2350 SIO output is one 32-bit register, and a whole-register store or a wrong mask raises both. They also never share a pad function: HZ-004 C10 names a periodic output on "TX_KEY (and PA_EN)", for example the A and B outputs of one PWM slice, which the AND then passes on every coincident high.
  - (ii) **E9 is a pad-configuration order constraint.** The section 5.2 E9 row (0.56 V against 0.8 V, 0.24 V margin, break-even 170 uA) rests on "typically around 120uA", which is not a limit. E9 flows only with input enable on and output enable off, and reset pads have IE = 0 (`keyer-verification-and-key-input-network.md` item 5). The margin therefore holds for any leakage if firmware drives each line low before, or together with, setting IE = 1.
  - (iii) **The writer rule.** PA_EN is written only by SW-SAFE (TS-012 D-18). The record relies on it but does not list it among the conditions.
- **Why Minor.** Each condition is already implied by 07 section 14.2 rows a and i, or by TS-012. The record's hardware conclusions stand. What is missing is the flow-down to the products that must implement them.
- **Fix.** Add a short "Software assumptions" list to section 6 with (i) to (iii), routed as follows:
  - to WP-PDR-35 (REQ-SW-SAFE rows and the SWE-184 assumptions);
  - to WP-PDR-32 (single-bit SET and CLR writes by the owning module only);
  - to WP-PDR-36a (TX_KEY and PA_EN on different PWM slices; FUNCSEL = SIO confirmed at boot and in the row g read-back; the pad order of (ii) in ICD-CTL-SW);
  - to WP-PDR-16b (the K8 wording names them).

**finding-4 (latent faults of the permit path, and R-2).**
- **Defect.** Section 5.7 shows that several single faults are "latent afterwards": branch P open or shorted (F2, F3), a DMP3099L drain-source short, U1 stuck high, and branch C open or shorted (F4, F5). Once the unit is built, nothing detects them. 07 section 14.2 row g reads back PA_EN and TX_KEY at the pad, which cannot see the realised gate state. So none of these faults is found until a second fault makes it matter (with finding-1, a branch-P fault already costs REQ-TX-014). Also, SWE-134 item l (software places the system in a safe state) is lost under a branch-P fault or U1 stuck high: PA_EN low then leaves the driver powered. The software's remaining means is disabling CLK1 (see finding-5). R-2, a TX5 sense line to a spare GPIO, is the only in-service detection means for the branch-P faults. Section 6.4 offers it as "not needed to close the lien" and "only if the pin map has one left", without the hazard reasoning. The closing case of REQ-SYS-120 (TC-SYS-083, "PA_EN logged by the logic capture") also logs the input to the gate, not its outputs.
- **Why Minor.** Each latent fault needs a second event before RF at power results (section 5.7). The record states the latency honestly. The decision belongs to WP-PDR-16b and 32.
- **Fix.**
  - State in section 5.7 the exposure time: the unit's life after the build test.
  - Send R-2 to WP-PDR-16b and 32 as an SA-relevant decision with that reasoning: it detects F2, F3 and the P-FET short before each PA_EN, and it restores row l detection.
  - Note for the TC-SYS-083 and REQ-SYS-119 bench cases (section 9) that the capture includes TX5 and the clamp gate, not only PA_EN.

**finding-5 (F-3's remedy conflicts with 07 section 14.2 row c).**
- **Defect.** F-3 proposes bounding the CLK1-left-on case "by SW-SAFE disabling CLK1 as part of `safe_state()`". 07 section 14.2 row c requires that "`safe_state()` is written without any fallible call and without loops over data". An Si5351A output disable is an I2C transaction, which can fail, stall or be refused by the bus.
- **Why Minor.** F-3 is a suggestion to other records, not a design item of this one.
- **Fix.** Reword F-3 so the remedy runs outside `safe_state()`: the end-of-over path of SW-TXSEQ, with its read-back and a fault on failure. Or use a hardware means (for example the Si5351A output-enable input, if the chosen module brings it out, driven from a GPIO or from the gate). Route it to WP-PDR-32 with the REQ-SYS-183 owner.

**finding-6 (the checker has no validation plan although its output is to be cited).**
- **Defect.** The record classes itself as "Developer evidence (05 section 9.1): the checker has no TV record". The REQ-TX-014 verification note names "Pre-build (supporting): Simulation of the envelope modulator and PA with TX_KEY low". REQ-SYS-120 and REQ-SYS-119 name pre-build simulations of the same gate and pull-down network, and this record is the only such simulation. 05 section 9.1 class B covers output "cited as verification, inspection, audit or review evidence" and needs a "TV record before first cited use". The record does not say whether it will be cited, or name the TV need.
- **Why Minor.** Nothing is cited for credit yet. LTspice itself is accredited (ACC-LTSPICE-001). The checker already carries seeded-fault known answers: the `asis` stage must detect the as-drawn defect, and F2 to F5 must reach their expected states, each exiting 3 otherwise. A TV record is therefore cheap.
- **Fix.** Add to the evidence row that `d18_run.py` needs a TV-NNN record (class B, known-answer test with the `asis` and F2 to F5 seeds) before its output is cited by a TC case. Until then it stays supporting design evidence for CR-018 only.

### Task table

| Task | Safety-critical designation (SWEHB 8.10 section 6) | Applied | Result and evidence | Relief (N/A only) | Finding ids |
|---|---|---|---|---|---|
| swe-134 7.1 task 5 | SC | Yes | This record is the assurance participation in the review of a product routed by the plan (WP-PDR-22 "SA pair") and by the 07 section 2.1.1 row for decisions that constrain safety-critical components | | none |
| swe-022 7.1 task 1 | SC | Yes | Performed against 07 section 15 with the CR-012 template | NASA-STD-8739.8 part: `rmm.json` SWE-022 T (standard not in the corpus) | none |
| swe-033 7.1 task 1 | | Yes | The decision acquires no software. It selects hardware parts (74LVC1G11, 2N3904, passives) against the alternatives of section 2 | | none |
| swe-033 7.1 task 2 | SC | No | The software safety obligations that the gate places on SW-SAFE, SW-KEYER, the architecture and the pin map are not flowed to WP-PDR-32, 35, 36a and 16b | | finding-3 |
| swe-033 7.1 task 3 | | Yes | Section 6.3 states the E5 (g) cost change, +0.63 to +0.91 USD, against the USD 0.17 ordering-gate margin, with options, and routes it to the TS-012 author. R-1 states the U1 common element | | none |
| swe-039 7.1 task 4 | | Yes | Source data assessed: datasheet rows of section 4 against the model constants in `MODEL`, `MODELS`, `static_checks()`; isolation chain re-derived (commands above); decks equal to the runs; raw hashes; result.json equal to the record tables; `CRIT` limits equal to section 3.2 | | none |
| swe-057 7.1 task 2 | | No | The architecture of the permit path does not meet the RF-off level of REQ-SYS-180, 181 and 092 in their fault state | | finding-1 |
| swe-134 7.1 task 4 | SC | Yes | Hardware partition: one stage per output, so a branch fault defeats one output (section 5.7, F2 to F5 simulated). U1 is stated as the common element (R-1). The firmware side (PA_EN owned by SW-SAFE, TX_KEY by SW-KEYER) is carried by finding-3 | | none |
| swe-134 7.1 task 6 | SC | No | Not consistent with HZ-004 K12 ("at the same node as K5"; the T/R-drive proposal) or with REQ-SYS-183 as TS-012 section 8.10 records it | | finding-1, finding-2 |
| swe-136 7.1 task 1 | | No | LTspice through `tools/ltspice-batch.sh` is accredited (ACC-LTSPICE-001; `wrapper.txt` PASS). The checker whose output is to be cited has no TV plan | | finding-6 |
| swe-070 7.1 task 1 | | No | The decision rests on a behavioural U1 model and VDMOS fits (limitations 1 and 2, stated), with datasheet limits checked separately (section 5.2); the model's use as cited evidence has no validation plan | | finding-6 |
| swe-205 7.1 task 3 | SC | Yes | No software component is added or moved: PA_EN stays with SW-SAFE, TX_KEY with SW-KEYER (TS-012 D-18; ADR-056) | | none |
| swe-134 7.1 task 1 | SC | No | Items a, c, e and j are implemented in hardware as shown. Items g, i and l have gaps at this maturity (section C) | | finding-1, finding-3, finding-4 |
| swe-205 7.1 task 1 | SC | Yes | Walked for the gate. **Action:** a single stuck line (L3, L4: no RF); the U1 output stuck high (R-1 routes it to WP-PDR-16b). **Inaction:** PA_EN never cleared (L2 and L1 show the gate follows Q and PA_EN). **Incorrect action:** one write raising both lines, or a shared pad function, already HZ-004 C10 and 07 row i, whose flow-down is finding-3. No contribution is missing from `hazards.json` because of this record | | none |
| swe-184 7.1 task 1 | SC | No | The hardware interlock assumptions that SW-SAFE must record (07 section 4 item 3) are not listed or routed | | finding-3 |
| swe-052 7.1 task 2 | SC | Yes | REQ-TX-014 and REQ-SYS-120 trace to HZ-004 K8 (`control_req_ids`), and REQ-SYS-055 and 180 to K5 and K12; traceability report 0 violations | | none |
| swe-080 7.1 task 1 | SC | No | The hardware change D18-2B is analysed for REQ-TX-014 and REQ-SYS-120 but not for the requirements that share its node (REQ-SYS-180, 181, 092, 183) | | finding-1 |
| swe-080 7.1 task 2 | | Yes | (a) Tracked: a new record with runs; (b) the D-18 change reaches TS-012 and the schematic only through F-1 and CR-018, after review; (c), (d) not yet implemented or tested (section 9 names the bench cases) | | none |
| swe-081 7.1 task 2 | SC | Yes | Record, checker, decks and results are committed at `078f2f7`; the two raws over 5,000,000 bytes are hashed (CR-017 C2) and the hashes match | | none |
| swe-087 7.1 task 2 | | Yes | INSP-118 finding-9 (a), (b), (c) and INSP-110 finding-24 are each addressed with evidence (sections D and E below) | | none |
| swe-089 7.1 task 1 | | Yes | This record carries the SWE-089 measurements; the paired record is not yet filed (X-1) | | none |
| swe-088 7.1 task 1 | | N/A | The paired file review is not filed at `c9f611d`; the check of its criteria a to d follows its filing | 07 section 10.2 (the assurance record is paired with a filed file review); cross item X-1 | none |
| swe-027 7.1 task 1 | | N/A | No COTS, OSS or reused software is acquired or used by the product; LTspice and spicelib are tools, covered by swe-136 | Not SC; the row applies only when a reused or OSS component is chosen (section B row text) | none |

## Readiness criteria

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | Product committed and frozen | Yes | `078f2f7` on `main`; blob `b8361270` equal at `HEAD` `c9f611d` and in the working tree. Equality with the paired record's list is pending its filing (X-1) |
| R2 | 07 section 2.1.1 row and criticality identified | Yes | `trade-study-or-adr`; safety-critical (07 section 14.1 rows "PA enable and TX sequencer", "Safe-state manager", "Keyer and keying output") |
| R3 | `validate_docs.py` and `traceability.py --report-only` | Yes | 7 failures, all record drift on other products' records; traceability 0 violations |
| R4 | Paired file review filed or in progress; independence | Yes | Dispatched concurrently under plan WP-PDR-22; this invocation is neither author nor file reviewer |

## A. Dispatch, independence and record integrity

| Id | Answer | Evidence |
|---|---|---|
| SA-A1 | Yes | Plan revision 7 section 3.0 row 22 ("SA pair") and the WP-PDR-22 section ("independent reviewer plus SA (cutoff and ALC units)"); 07 section 2.1.1 row "Trade studies and ADRs ... constrains a safety-critical ... component", safety-critical column Yes; 07 section 14.1 rows named in R2 |
| SA-A2 | Yes | Author (analysis author invocation, record header row "Author"), file reviewer (not yet filed), and this invocation: three different invocations |
| SA-A3 | Yes, pending X-1 | Product and blobs as in `product_files`; the paired record must name the same blobs at `078f2f7` |
| SA-A4 | N/A at this iteration | Paired record not filed (X-1); relief as for swe-088 task 1 |

## B. SWE-to-task table

| Id | Answer | Evidence |
|---|---|---|
| SA-B1 | Yes | Task table: row "Every product type", row `trade-study-or-adr` (including the conditional swe-136, swe-070 and swe-205 task 3 rows) and the section 7.1 tasks of SWE-134 (task 1), SWE-205 (task 1), SWE-184, SWE-052, SWE-080, SWE-081, SWE-087, SWE-088 and SWE-089. `assurance_tasks_applied` lists every Yes and No row |
| SA-B2 | Yes | Two N/A rows: swe-088 task 1 (07 section 10.2), swe-027 task 1 (no reused or OSS software). No SC task is N/A |
| SA-B3 | Yes | Every No row carries finding-1, 2, 3, 4 or 6 |

## C. SWE-134 items (07 section 14.2 rows the gate implements in hardware)

| Id | Answer | Evidence |
|---|---|---|
| SA-C-a | Yes | Either power-up order, GPIOs high impedance with the pull-downs and E9 leakage, U1 unpowered or open: driver at most 36 mV, VGG at most 1.07 V only while the bus ramps (S1, S2, F1; `seq_cases.png`); K6 pull-downs kept; base pull-downs make an unpowered or open U1 safe (INSP-118 finding-9 (b) answered) |
| SA-C-c | Yes | `safe_state()` drives PA_EN low first (07 row c). The gate then removes the driver in under 20 us to 3.1 V and 0.78 ms to 0.1 V, and clamps VGG in 0.08 to 0.12 us (L2 case; `keyup_edges.png`). The F-3 remedy is finding-5 |
| SA-C-e | Yes | The gate permits only with both lines high in either order: `pre_permit_off` 0 V in all 52 cases, covering PA_EN before TX_KEY (nominal) and TX_KEY before PA_EN (interval-13 fallback) |
| SA-C-g | No | Output integrity of the realised gate state has no in-service means (finding-4) |
| SA-C-i | No | The hardware half holds for single lines (L3, L4). The hardware bounds outside software (07 row i) do not reach RF off with the driver powered (finding-1), and the write-level conditions are not flowed (finding-3) |
| SA-C-j | Yes | Hardware response times are bounded by simulation against limits: driver under 0.1 V within 0.77 to 0.78 ms (limit 1 ms), clamp within 0.12 us, turn-on 0.5 to 1.2 us (limit 0.25 ms), over 52 corners (`keyup_metrics.png`). This is consistent with 07 row j ("PA_EN falls after the fall completes") |
| SA-C-l | No | Under a branch-P fault or a U1 stuck-high fault, the software's safe-state command (PA_EN low) no longer unpowers the driver (section 5.7; finding-4) |

Items b, d, f, h and k are firmware functions that the gate neither implements nor constrains; they are not answered here.

## D. Software safety analysis and hazard traceability

| Id | Answer | Evidence |
|---|---|---|
| SA-D1 | Yes | swe-205 task 1 row. The new hardware single points (U1 common element; the latent branch-P faults) are routed to WP-PDR-16b (R-1, section 6.2). The K12 T/R-drive proposal is finding-2 |
| SA-D2 | Yes | No component is added or renamed; criticality unchanged (swe-205 task 3 row) |
| SA-D3 | Yes | Traceability report 0 violations for REQ-TX-014, REQ-SYS-055, 119, 120, 180, 181, 183 |
| SA-D4 | No | finding-3 |
| SA-D5 | Yes | REQ-TX-014 closes by Test TC-TX-014; REQ-SYS-120 by TC-SYS-083; REQ-SYS-180 by TC-SYS-108; REQ-SYS-181 by TC-SYS-109 (all Test). Their pass levels are what finding-1 checks |
| SA-D6 | Yes | Section 6.2 routes the K8 wording to WP-PDR-16b; its content changes with finding-1 |

## E. Peer review, change and configuration assurance

| Id | Answer | Evidence |
|---|---|---|
| SA-E1 | Yes | **INSP-118 finding-9:** (a) level interface: VGS 0.0 V not permitted, -4.26 V or beyond permitted (section 5.3); (b) unpowered state and order: S1, S2, S3, F1 and the base pull-downs (section 5.5); (c) fallback: driver powered 0.55 to 1.2 us after PA_EN, against a 0.5 ms lead (section 5.6). **INSP-110 finding-24:** the as-drawn defect reproduced in 25 of 36 cases (`asis_keyup.png`), fix D18-2B. The finding-9 routing to WP-PDR-16b is section 6.2 |
| SA-E2 | Yes | This record's front matter; the file review's is pending (X-1) |
| SA-E3 | Yes | `078f2f7` subject type `sim`, `Refs:` REQ-TX-014, REQ-SYS-120, HZ-004, INSP-118, INSP-110, TS-012, WP-PDR-22; `check_commit_msg.py` PASS (rows 24, 49). A new analysis record needs no CR; the TS-012 and schematic changes go by F-1 and CR-018 |
| SA-E4 | N/A | No credit test run on a release is part of the product |

## F. Assurance risks, metrics and reporting

| Id | Answer | Evidence |
|---|---|---|
| SA-F1 | Yes | No assurance concern outside the findings. The latent-fault exposure of finding-4 belongs to RSK-024 (HZ-004's risk) through WP-PDR-16b; no new risk entry is submitted |
| SA-F2 | Yes | Front matter: counts, `items_no`, effort |
| SA-F3 | Yes | Verdict block below |

## Cross items for the lead SE

- **X-1.** The paired file review of this product is not filed at `c9f611d`. When it is, it names this record in `paired_record` and `assurance_reviewer_agent`, and copies `assurance_verdict`. SA-A3 and SA-A4 are then checked in a delta of this record.
- **X-2.** The id INSP-120 is proposed (highest existing INSP-118; INSP-119 left for the file review). Confirm or renumber at filing.
- **X-3.** The checklist applied is on the unmerged CR-012 branch (the INSP-111 convention). The software lead's record verdict also waits for that merge.
- **X-4.** The template has no `analysis` product type (INSP-032 finding-2, a lien). This record uses `trade-study-or-adr`, as INSP-111 did.
- **X-5.** Finding-1 affects CR-018's timing. The plan says CR-018 needs this record APPROVED before it carries the REQ-TX-014 restatement (row 22, rule C10). The REQ-TX-014 key-up result itself (-58.3 dBm by estimate, -34.0 dBm at the bounds) is not disputed by this record. Only the gate's inputs and the claims of sections 5.7, 6.1 and 6.2 are.

## What was checked and holds

- The defect is real and correctly bounded: 25 of 36 driver powered and 21 of 36 over -30 dBm as drawn.
- The fix holds in all 52 key-up corners with the loop wound to the rail.
- The unpowered and brown-out states are safe, and each branch fault defeats one output only.
- The REQ-TX-014 key-up levels reproduce by hand.
- The raw-file retention follows CR-017 C2.

These are sound and are not reopened by the findings.

## Verdict format

```
ASSURANCE VERDICT: NEEDS CHANGES
PRODUCT: docs/design/analysis/pa-permit-gate-d18.md@b8361270 (+ d18_run.py@a6916e0f, decks, runs 2026-09-29-d18-*) at 078f2f7; PAIRED RECORD: not yet filed (X-1)
PRODUCT TYPE: trade-study-or-adr; CRITICALITY: safety-critical
FINDINGS:
- [Major] swe-134 7.1 task 6 / SA-C-i: REQ-SYS-180, 181, 092 (and K5 under U1 stuck high) clamp VGG only; with the driver powered the level is -9.9 to -16 dBm (L3 -44.7), not the -57 dBm REQ-SYS-183 level of TC-SYS-108, 109, 066.
- [Minor] swe-134 7.1 task 6: HZ-004 K12's proposed T/R-drive input to the PA-path gate neither confirmed nor declined.
- [Minor] swe-184 7.1 task 1: firmware-side conditions (single-bit writes, no shared pad function, E9 pad order, PA_EN writer) not flowed down.
- [Minor] SA-C-g / SA-C-l: latent permit-path faults undetectable in service; R-2 offered without hazard reasoning; TC-SYS-083 logs only PA_EN.
- [Minor] SA-C-c: F-3 remedy puts a fallible I2C write in safe_state(), against 07 row c.
- [Minor] swe-136 / swe-070: checker output to be cited as REQ-TX-014 and REQ-SYS-120 pre-build evidence without a TV plan.
TASKS APPLIED: 21 (see assurance_tasks_applied)
TASKS N/A (relief): swe-088 7.1 task 1 (07 section 10.2, paired record not filed); swe-027 7.1 task 1 (no reused or OSS software)
SWE-134 ITEMS CHECKED: a, c, e, g, i, j, l
MEASUREMENTS: size=434-line record, 1026-line checker, 101 cases, 7 figures; tasks=23; tasks_no=8; turns=48; minutes=85; major=1; minor=5
```

## Delta iteration 2 (2026-09-29; revision 1 at c397ab1)

**Product.** `docs/design/analysis/pa-permit-gate-d18.md` revision 1, blob `a6bcc2b1`, with the revision 1 checker `d18_run.py` (`5a06cfd8`), the revised decks `d18_keyup.cir` (`bce02858`) and `d18_seq.cir` (`de50be4d`), the runs `2026-09-29-d18r1-keyup`, `-seq` and `-summary`, and the reused as-drawn run `2026-09-29-d18-asis`, all committed at `c397ab1` on `main` (rule C2, re-freeze F0). Every blob of `product_files` equals `git rev-parse c397ab1:<path>`, `HEAD:<path>` at `f8dcf8c` and `git hash-object <path>`. The record and script blobs equal those of the author summary. **Paired record:** the file review (INSP-119 proposed), whose iteration 1 and delta are not filed at `f8dcf8c` (cross item X-1).

**Scope (rule C1).** A delta that verifies the fix of finding-1, the only Major. It also checks what the fix itself changes: the D1 path, the shared Q node, the static rows, the added sequencing cases, and the revised wording of sections 5.7, 6.1, 6.2, 6.4 and 7 under the assurance lens. Iteration 1's Minor findings (finding-2 to finding-6) are not re-reviewed. Their state is recorded below, and revision 1 leaves each of them unchanged, as its section 11 says. The reviewer's finding-1 (the REQ-SYS-120 level) belongs to the paired file review. It is read here only where the new section 5.8 and F-6 bear on SWE-134 item i.

**Acceptance criteria (rule C7).** Finding-1 is Verified when all of the following hold:
- **(a) Each cutoff reaches the key-up state.** This covers REQ-SYS-180 (K12), REQ-SYS-181 (HZ-003 K9), the cell 60 C trip and REQ-SYS-092. With TX_KEY and PA_EN high and the monostable retriggered, each one unpowers the driver and clamps VGG, with evidence.
- **(b) The static rows are rechecked.** The Q-high row includes the added leakage, and the Q-low rows use each pull's VOL.
- **(c) The sequencing cases are added** and come out as the record states.
- **(d) The 52 key-up corners are unchanged** by the added parts.
- **(e) "Still ends RF" is corrected** for U1 stuck high.
- **(f) The fix does not open a new Major gap.** No new single point may defeat a cutoff that TS-012 wired independently of U1, and the software-facing claims must stay consistent with HZ-004, HZ-003 and 07 section 14.2 rows i and l.

**Independence (rule C4).** This invocation authored no part of WP-PDR-22, TS-012, INSP-110 or INSP-118. It is not the file reviewer, and it is not the iteration 1 assurance reviewer. It edited no product file and made no commit.

**Search first (charter section 11 rule 1).** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search. The queries were:
- the WP-PDR-22 D-18 software assurance pair record;
- the pair's finding-1, the cutoffs that clamp only VGG;
- firmware sensing of the cutoff monostable or backstop, and SW-SAFE's observation of a hardware cutoff.

`grep`, `sed -n` and Python reads of `result.json`, `summary.json` and `hazards.json` were used afterwards only to pin lines and values. The rustos tree was not read.

### Commands run by the assurance reviewer (iteration 2 evidence)

- **Blob identity.** `git rev-parse c397ab1:<path>`, `git rev-parse HEAD:<path>` at `f8dcf8c` and `git hash-object` all give `a6bcc2b1...` for the record and `5a06cfd8...` for the script, and the script blob is the same in all three d18r1 run folders. `git diff --stat c397ab1 HEAD` on `hardware/sim/tx-pa-permit`, the record, `docs/safety`, `docs/requirements`, TS-012 and 07 is empty.
- **Decks.** `cmp` of the generated decks against the run copies: both equal. Each `wrapper.txt` shows `result: PASS`, LTspice 26.0.2 and exit 0 (ACC-LTSPICE-001).
- **Raw file.** `shasum -a 256` of the untracked `d18r1-keyup/d18_keyup.raw` (11,633,088 bytes) gives `04fb27d3...96ff5`, equal to the committed `raw.sha256` (CR-017 C2). `d18r1-seq/d18_seq.raw` (2,711,084 bytes) is committed.
- **Independent re-analysis.** A detached worktree at `c397ab1` was made in the scratchpad, with the untracked key-up raw copied in. In it, `d18_run.py replot seq` and `d18_run.py replot keyup` both exit 0 ("20 cases; not as required: none"; all 52 key-up criteria pass). `git status` after the runs shows no change to any committed output: the regenerated `result.json` files and figures are byte-identical to the committed ones. The main working tree was not touched.
- **`result.json` of `d18r1-seq`,** read case by case:

  | Case | Q | Driver supply at the end | VGG at the end | Level L1 / L4 | Result |
  |---|---|---|---|---|---|
  | C1 | 0.701 V | 1.4e-8 V | 7.8 mV | -58.3 / -34.0 dBm | Passes |
  | C2 | inhibit held from power-up | never permitted | at most 0.40 V during the bus ramp | - | Passes |
  | C3 | 0.001 V | off | clamped | -58.3 / -34.0 dBm | Passes |
  | C4 (D1 open) | 0.700 V | off | 7.8 mV | - | Passes |
  | A1 | 4.99 V | 4.97 V | 0.701 V | -14.7 / -9.9 dBm (L3 -44.7) | As expected |
  | F6 | 0.701 V | powered | 1.123 V (D1 1.21 mA) | as A1 | As expected |
  | F7 | 0.195 V | powered | 0.636 V (D1 1.49 mA) | as A1 | As expected |

  The 13 revision 0 cases give the revision 0 results.
- **`summary.json` of `d18r1-summary`.** `keyup_max_abs_delta_vs_rev0`: bus dip 0.20 mV, inrush 0.049 A, turn-off 3.3 us, turn-on 11 ns, key-up levels 0.0 dB. There are 21 static checks, and every revision 1 row equals record section 5.2. `req_sys_183_off_states` gives L1 -58.34 dBm (+1.34 dB), L2 -38.77, L3 -88.34 and L4 -33.99 dBm in all four windows, with `as_expected: true`.
- **The new static rows, re-derived by hand:**
  - Q high: 4.75 V - 10 k x (4 x 20 nA + 10 uA + 1 uA + 12.8 uA) = 4.511 V.
  - D1 current with U1 stuck high: (5.25 - 1.13) / 2.7 k - 1.13 / 5.1 k = 1.30 mA.
  - VF from the fit (Is 1.07 nA, N 1.05, Rs 36.9 ohm) at 1.30 mA: 0.428 V, so VGG = 0.7 + 0.428 = 1.128 V.
  - LM393 sink: 0.525 + 1.30 = 1.83 mA.

  All four equal section 5.2.
- **Commit and repository checks.**
  - `tools/check_commit_msg.py --range c397ab1~1..c397ab1`: PASS (rows 24, 49; `Refs:` REQ-SYS-120, 183, 180, 181, 092, 055, REQ-TX-014, HZ-004, TS-012, WP-PDR-22).
  - `tools/validate_docs.py` at `f8dcf8c`: 117 passed, 0 failed.
  - `tools/traceability.py --report-only`: 0 violations, 2 warnings (REQ-SYS-125, 148; unrelated).
  - The whole of this record text, placed at its path in the scratch worktree, passes `tools/validate_docs.py --root <worktree>` for this record.
- **Figures.** Opened and inspected before citing: `off_states.png`, `cutoff_levels.png` and `seq_cases.png` (all 20 panels; C1, C3 and C4 show the driver falling at 20 ms, and A1, F6 and F7 show the driver held with VGG stepping to 0.7, 1.1 and 0.64 V).

### Verification of finding-1

| Criterion | Result | Evidence |
|---|---|---|
| (a) Each cutoff reaches the key-up state | Met | Section 2 puts the backstop, the 95 C trip, the cell 60 C trip and the VBUS inhibit on the Q node under its 10 kohm pull-up. C1 (LM393 at its 0.7 V VOL maximum) and C3 (VBUS inhibit) end with the driver under 0.1 V within 1 ms and VGG at 7.8 mV. Their level is the key-up level, -58.3 dBm (L1) and -34.0 dBm (L4). This is also inside REQ-SYS-181's 100 ms. C2 holds the inhibit from power-up |
| (b) Static rows | Met | Six revision 1 rows in section 5.2, re-derived above. Q high is 4.51 V against VIH 2.0 V. Q low is 0.70 V (LM393) or 0.01 V (inhibit) against VIL 0.8 V. The ground-offset allowance on the 0.10 V margin is finding-8 |
| (c) Sequencing cases | Met | C1 to C4, A1, F6 and F7 were added, 20 cases in all. Every case comes out as required or as expected, and the replot reproduces them |
| (d) Key-up corners unchanged | Met | The largest change is 0.20 mV of bus dip, and the key-up levels are identical (`keyup_max_abs_delta_vs_rev0`) |
| (e) "Still ends RF" corrected | Met | Section 5.7's U1 row, section 6.2's last bullet and R-1 now say the cutoffs end the 5 W carrier only to -9.9 to -14.7 dBm (L3 -44.7) with U1 stuck high, and that the RF-off level then needs firmware |
| (f) No new Major gap | Met, with Minor liens | D1 keeps a path from every cutoff to VGG that does not pass through U1 (F6, F7), as the TS-012 wiring had. That path is one shared diode and is latent (finding-7). The Q-low margin carries no ground-offset allowance (finding-8). The shared-node constraint and the release behaviour are not carried into the D-18 wording (finding-9). The 07 section 14.2 row i text is not in F-6's routing (finding-10). None of these reopens the fault-free result or leaves a single fault that restores the 5 W carrier: with U1 stuck high, D1 still takes VGG under the module's conduction region, and firmware (K3, the reference clamp, CLK1) still acts |

**SWE-080 task 1 (impact of the hardware change on software products).**
- **Pin map and ICD-TX-SW.** The fix adds no GPIO and no signal.
- **SW-SAFE and SW-TXSEQ.** Nothing changes in their obligations: PA_EN stays the SW-SAFE output, and TX_KEY stays with SW-KEYER.
- **`sequencer-timing.md` revision 0 (WP-PDR-23a).** It takes "the D-18 gate turn-on time" from revision 0 of this record. Revision 1 changes that time by 11 ns, so no re-check is needed.
- **Firmware's view of the cutoffs.** The firmware still cannot tell which hardware cutoff acted (ConOps Appendix D item D19), as before the fix. Now that every cutoff unpowers the driver, though, R-2's TX5 sense line would observe all of them (cross item X-6).

Finding-1 is **Verified**.

### Findings (iteration 2)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| finding-1 | assurance (iteration 1) | Major | `swe-134 7.1 task 6`, `swe-057 7.1 task 2`, `swe-080 7.1 task 1`, SA-C-i, SA-C-l | Record sections 2, 5.2, 5.5, 5.7, 6.1, 6.2, 6.4 R-1 (revision 1) | The other hardware cutoffs clamped only VGG. Fixed by option (a): they now pull the Q node, and D1 runs from VGG to Q. Verified against criteria (a) to (f) above | Verified | | |
| finding-2 | assurance (iteration 1) | Minor | `swe-134 7.1 task 6`, SA-D1 | Record sections 2 and 6.2 | HZ-004 K12's proposed T/R-drive input is neither confirmed nor declined. Unchanged in revision 1. The Q node of the fix is now the natural place for it, as the iteration 1 note said | Open (lien, rule C1; owner the WP-PDR-22 author with WP-PDR-16b; due at the CDR readiness declaration) | Pending | |
| finding-3 | assurance (iteration 1) | Minor | `swe-184 7.1 task 1`, `swe-134 7.1 task 1`, `swe-033 7.1 task 2`, SA-C-i, SA-D4 | Record sections 1, 5.2, 6.2 | The firmware-side conditions of the gate's argument are not flowed down. Unchanged | Open (lien, rule C1; owner the WP-PDR-22 author with WP-PDR-32, 35, 36a, 16b; due at the CDR readiness declaration) | Pending | |
| finding-4 | assurance (iteration 1) | Minor | `swe-134 7.1 task 1`, SA-C-g, SA-C-l | Record sections 5.7, 6.4 R-2, 9 | Latent permit-path faults cannot be detected in service, and R-2 is offered without the hazard reasoning. Unchanged. finding-7 adds D1 to its list | Open (lien, rule C1; owner the WP-PDR-22 author with WP-PDR-16b and 32; due at the CDR readiness declaration) | Pending | |
| finding-5 | assurance (iteration 1) | Minor | SA-C-c | Record section 7 F-3 | F-3 still names `safe_state()` for the CLK1 disable ("Disabling CLK1 in `safe_state()` helps only ..."), against 07 section 14.2 row c. Unchanged | Open (lien, rule C1; owner the WP-PDR-22 author with WP-PDR-32; due at the CDR readiness declaration) | Pending | |
| finding-6 | assurance (iteration 1) | Minor | `swe-136 7.1 task 1`, `swe-070 7.1 task 1` | Record header row "Evidence status" | No TV plan for the checker whose output is to be cited. Unchanged. Revision 1 adds known-answer seeds that a TV record could use: A1, F6 and F7 must reach their expected states | Open (lien, rule C1; owner the WP-PDR-22 author with the tool owner; due before first cited use, at the latest the CDR readiness declaration) | Pending | |
| <a id="finding-7"></a>finding-7 | assurance (iteration 2) | Minor | `swe-134 7.1 task 1`, `swe-134 7.1 task 6`, SA-C-g | Record section 2 (D1), section 5.7 row "D1 open" ("Not detectable in service"), section 9 ("with U1's output jumpered to 3V3 (bench prototype only), VGG at most 1.2 V"); HZ-004 `fault_tolerance`; HZ-003 `fault_tolerance` (thermistor-failure branch) | **D1 is the only path from every hardware cutoff to VGG that does not pass through U1, and it is latent. The only test of it is written for the prototype and measures a voltage, not the level.** See the note | Open (lien, rule C1; owner the WP-PDR-22 author with WP-PDR-16b and WP-PDR-43; due at the CDR readiness declaration) | Pending | |
| <a id="finding-8"></a>finding-8 | assurance (iteration 2) | Minor | SA-C-i, `swe-134 7.1 task 6` | Record section 5.2 rows "Q low (LM393 VOL, full range, 4 mA ...)" and "Rev. 1: Q low with one LM393 cutoff on" (0.70 V against 0.8 V, margin 0.10 V); section 6.4 R-3 | **The 0.10 V margin of the Q low against U1's VIL has no allowance for ground offset, and revision 1 makes three more cutoffs rely on it while the PA draws its full current.** See the note | Open (lien, rule C1; owner the WP-PDR-22 author with WP-PDR-37; due at the CDR readiness declaration) | Pending | |
| <a id="finding-9"></a>finding-9 | assurance (iteration 2) | Minor | `swe-134 7.1 task 6`, SA-C-l | Record section 6.1 (D-18 wording), section 6.2 (K8 wording), section 7 F-4 | **The constraint the fix puts on the shared Q node, and the permit's behaviour when a non-latching cutoff releases, are not carried into the D-18 and HZ-004 wording.** See the note | Open (lien, rule C1; owner the WP-PDR-22 author with WP-PDR-26, 16b and 35; due at the CDR readiness declaration) | Pending | |
| <a id="finding-10"></a>finding-10 | assurance (iteration 2) | Minor | `swe-134 7.1 task 6`, SA-C-i, SA-D6 | Record section 7 F-6 and section 6.2; 07 section 14.2 row i ("so a single GPIO write or a single corrupted flag cannot produce RF"; "Outside software: ..."), REQ-SW-SAFE-009 | **F-6 routes the REQ-SYS-120 level conflict to HZ-004 K8 but not to 07 section 14.2 row i, which makes the same claim for SWE-134 item i.** See the note | Open (lien, rule C1; owner the WP-PDR-22 author with the software lead (07) and WP-PDR-35; due with the owner's F-6 ruling, at the latest the CDR readiness declaration) | Pending | |

**finding-7 (D1 is the only U1-independent path and is latent).**
- **Defect.** In TS-012 each cutoff pulled the VGG node directly. In revision 1 every cutoff reaches VGG either through U1 and branch C, or through the single diode D1. This covers the monostable K5, the backstop K12, the 95 C trip (HZ-003 K9), the cell 60 C trip and the VBUS inhibit. Section 5.7 states that D1 open is latent and "not detectable in service" (case C4). Once D1 is open, a U1 stuck-high fault leaves none of the five cutoffs any effect: the driver stays powered, the clamp is released, and VGG is under loop and firmware control. Two hazard analysis statements rest on these cutoffs acting independently of firmware:
  - HZ-004 `fault_tolerance`: "single-fault tolerant with dissimilar controls ... hardware monostable K5";
  - HZ-003 `fault_tolerance`: the thermistor-failure branch is single-fault tolerant with K9, "which does not share the thermistor or any firmware path".

  In each branch the hardware leg is now (U1 or D1). With D1 latent-open, U1 alone carries it.
- **The test.** Section 9 has the one test that exercises D1. It jumpers U1's output to 3V3 on the "bench prototype only" and measures VGG at most 1.2 V, not the antenna level. The claim that 1.13 V is "under the module's dead zone (to about 2.3 V)" rests on the lowest point of the digitized typical curve (2.32 V, `d18_run.py` `_a5_table`) and the 100 dB/V extension below it (E). That is not a datasheet limit.
- **Why Minor.** Two faults are needed (D1 open and U1 stuck high), and the firmware controls still act. In fault-free operation revision 1 is better than TS-012, and D1 gives the U1 stuck-high case the TS-012 level (F6, F7).
- **Fix.**
  - In section 9, run the D1 test on every unit built, not only the prototype. That needs a test pad at U1's output, or an equivalent injection. Name it for WP-PDR-43 as a TRR and ATP check, and measure the antenna level in that state with the TC-TX-014 set-up, not only VGG.
  - In section 5.7, state the exposure: the time from one D1 test to the next.
  - Send D1 to WP-PDR-16b, so that the HZ-004 and HZ-003 `fault_tolerance` texts and the single-point list count D1 open as a latent fault in the hardware leg.

**finding-8 (Q-low margin without ground offset).**
- **Defect.** Section 5.2 gives the Q low at 0.70 V (LM393 VOL maximum, full range, 4 mA) against U1's VIL of 0.8 V: a margin of 0.10 V. It allows nothing for a ground difference between the LM393 outputs and U1's ground pin. After revision 1, the backstop, the 95 C trip and the cell 60 C trip rely on this margin as well as the monostable, and the 95 C trip acts only during long keying at full drain current. R-3 gives layout rules for the P-FET parts only.
- **Consequence.** A ground difference above 0.10 V puts U1 input C in the band between VIL and VIH, where the permit is not guaranteed to fall. D1 then still takes VGG to about 1.1 to 1.2 V, so the outcome is the A1 level, -14.7 dBm (L1), not RF at power.
- **Why Minor.** The consequence is bounded by D1, and U1's typical threshold is well above VIL. But this is the only guaranteed-level check of the fix's main path.
- **Fix.**
  - Add to R-3 (WP-PDR-37) that U1, the four LM393 outputs and the VBUS inhibit share a ground return that carries no PA or regulator current, or bound the offset by analysis and state it in section 5.2.
  - Add to section 9 a check of V(Q) at U1's pin during a 5 W key-down into the dummy load, with each LM393 cutoff forced in turn: at most 0.8 V.

**finding-9 (shared-node constraint and release behaviour not in the D-18 wording).**
- **Defect 1: the feedback rule.** F-4 states the constraint the fix creates: the monostable and the backstop "must take no feedback (hysteresis or latch) from the shared node, or take it through their own output resistor". It is routed only to WP-PDR-26. The D-18 wording proposed for TS-012 and the schematic (section 6.1) and the K8, K5 and K12 wording (section 6.2) leave it out, so the schematic writer (WP-PDR-37) and the hazard writer (WP-PDR-16b) do not receive it.
- **Defect 2: what happens when a cutoff releases.** Revision 1 does not say what the permit does when a non-latching cutoff releases while TX_KEY and PA_EN are still high. Three cutoffs are non-latching: the 95 C trip once its hysteresis clears, the cell 60 C trip, and the VBUS inhibit when USB is unplugged. Section 5.3 shows the driver returning within 1.2 us, and the clamp releasing within 0.12 us, with the loop state at that moment (possibly wound after RF was removed). Before the fix only the VGG clamp was released in this case, so the release itself is not new. But the permit now carries it, and no firmware input observes it (cross item X-6).
- **Why Minor.** No requirement fails in the analysed cases. Defect 1 is a routing gap, and defect 2 is WP-PDR-22 loop and WP-PDR-26 timer scope.
- **Fix.**
  - Add the F-4 constraint to the section 6.1 D-18 wording and to the K5 and K12 routing in section 6.2.
  - Ask WP-PDR-26 for a case with another cutoff pulling Q during and after the timed interval, and ask the WP-PDR-22 loop rerun for the release case with the loop wound.
  - Route to WP-PDR-35 the question of whether SW-SAFE must clear PA_EN when it sees RF lost while keyed.

**finding-10 (07 section 14.2 row i is not in F-6's routing).**
- **Defect.** Section 5.8 shows two states at -58.3 dBm by estimate (+1.3 dB) and -34.0 dBm at the drive bound, against REQ-SYS-120's RF-off level:
  - "one line only", which is the single-GPIO-write state;
  - "after a cutoff with CLK1 running", which covers REQ-SYS-055, 180, 181 and 092.

  07 section 14.2 row i, the SWE-134 item i argument, says "a single GPIO write or a single corrupted flag cannot produce RF" and cites REQ-SYS-120 and those hardware bounds "outside software". REQ-SW-SAFE-009 carries the row. F-6 and section 6.2 send the level conflict to the owner, CR-018, WP-PDR-16b (K8) and WP-PDR-23, but not to the owner of 07 row i or to WP-PDR-35. SWE-134 task 6 needs the software safety argument and the hazard analysis to use the same RF-off level.
- **Why Minor.** The conflict itself is stated and routed. This is one missing route.
- **Fix.** Add 07 section 14.2 row i (software lead, by the 07 change route) and REQ-SW-SAFE-009 (WP-PDR-35) to F-6, so that row i is worded on the level the owner chooses, as K8 will be.

### Task table (iteration 2, delta)

| Task | Safety-critical designation (SWEHB 8.10 section 6) | Applied | Result and evidence | Relief (N/A only) | Finding ids |
|---|---|---|---|---|---|
| swe-134 7.1 task 5 | SC | Yes | This delta is the assurance participation in the re-freeze review (plan WP-PDR-22 "SA pair"; rule C1) | | none |
| swe-134 7.1 task 6 | SC | No | The cutoffs are now consistent with HZ-004 K12 ("at the same node as K5") and REQ-SYS-183's state (finding-1 Verified). The K12 T/R-drive proposal (finding-2), the latent D1 in the `fault_tolerance` texts (finding-7), the shared-node wording (finding-9) and 07 row i (finding-10) remain | | finding-2, finding-7, finding-9, finding-10 |
| swe-057 7.1 task 2 | | Yes | The permit path now carries every firmware-independent cutoff to both outputs (C1, C3), with an independent VGG path (D1: F6, F7) | | none |
| swe-080 7.1 task 1 | SC | Yes | The hardware change is analysed for every requirement on the node: REQ-SYS-055, 092, 180, 181, 183, 120 and REQ-TX-014 (sections 5.5, 5.8). Its software impact is assessed above: no new signal, no change of writer, and sequencer-timing's turn-on input unchanged by 11 ns | | none |
| swe-080 7.1 task 2 | | Yes | (a) Tracked: revision 1 with runs, revision history section 11. (b) TS-012 7.3 and 8.1 changes go by F-1 and F-7 after review; the record edits no TS-012 text. (c), (d) Bench cases added in section 9 | | none |
| swe-134 7.1 task 1 | SC | No | Items a, c, e and j hold, re-checked on the new cases (C2 power-up with the inhibit; driver off within 1 ms after each cutoff). Items g, i and l keep their liens | | finding-3, finding-4, finding-7, finding-8 |
| swe-205 7.1 task 1 | SC | Yes | Walked for the change. **Action:** a cutoff pulling Q (C1, C3). **Incorrect action:** D1 short (safe, cannot transmit) and D1 open (latent, finding-7). **Inaction:** U1 stuck high (F6, F7, routed by R-1). No software contribution to `hazards.json` is added or removed by the fix | | none |
| swe-039 7.1 task 4 | | Yes | New source data assessed. The 1N5711W fit was checked against both VF maxima (1.128 V re-derived). The added leakage terms and the static rows were re-derived, and the replot reproduces every result | | none |
| swe-081 7.1 task 2 | SC | Yes | Revision 1 record, checker, decks and results are committed at `c397ab1`. The key-up raw over 5,000,000 bytes is hashed (CR-017 C2) and the hash matches | | none |
| swe-087 7.1 task 2 | | Yes | finding-1 of this record is answered with evidence (verification table above) | | none |
| swe-089 7.1 task 1 | | Yes | Front matter carries the iteration 2 measurements | | none |
| swe-088 7.1 task 1 | | N/A | The paired file review is not filed at `f8dcf8c`; the check of its criteria follows its filing | 07 section 10.2; cross item X-1 | none |

### SWE-134 items (iteration 2)

| Id | Answer | Evidence |
|---|---|---|
| SA-C-a | Yes | C2: USB first, inhibit held, TX_KEY and PA_EN driven high from 3 ms, bus at 8 ms. Never permitted; VGG at most 0.40 V during the bus ramp |
| SA-C-c | Yes | Unchanged: PA_EN low removes the driver and clamps VGG (L2). The F-3 remedy stays finding-5 |
| SA-C-e | Yes | Unchanged, `pre_permit_off` 0 V in 52 cases |
| SA-C-g | No | finding-4 (unchanged) and finding-7 (D1 latent) |
| SA-C-i | No | The hardware bounds outside software now reach the key-up state (finding-1 Verified). finding-3 remains, as do finding-8 (Q-low margin) and finding-10 (row i text on the level) |
| SA-C-j | Yes | Each cutoff removes the driver to under 0.1 V within 1 ms (C1, C3), inside REQ-SYS-181's 100 ms |
| SA-C-l | No | finding-4 (unchanged) and finding-9 (release of a non-latching cutoff) |

### Readiness (iteration 2)

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | Product committed and frozen | Yes | `c397ab1` on `main`; blobs equal at `f8dcf8c` and in the working tree |
| R2 | 07 section 2.1.1 row and criticality | Yes | As iteration 1 |
| R3 | `validate_docs.py` and `traceability.py --report-only` | Yes | 117 passed, 0 failed; 0 violations |
| R4 | Paired review in progress; independence | Yes | Paired delta dispatched under WP-PDR-22; this invocation is neither author, file reviewer nor the iteration 1 assurance reviewer |

### Cross items for the lead SE (iteration 2)

- **X-1 (open).** The paired file review (INSP-119 proposed) and its delta are not filed. When they are, the file review names this record, and SA-A3 and SA-A4 are checked.
- **X-2 (open).** INSP-120 is kept as proposed. Filing this text files both iterations.
- **X-3 (open).** CR-012 is not merged; the record verdict waits for it.
- **X-5 (updated).** Under this assurance lens, CR-018 may rest the REQ-TX-014 restatement on this record once the paired review is also APPROVED. The owner's F-6 choice must travel with it (record section 6.1).
- **X-6 (new).** Every hardware cutoff now unpowers the driver, so R-2's TX5 sense line would give SW-SAFE the one observation ConOps Appendix D item D19 needs ("the class the controller assigns when it observes the backstop or the hardware cut-off act"). This adds weight to finding-4's request that WP-PDR-16b and 32 decide R-2 with the hazard reasoning.
- **X-7 (new).** INSP-118 finding-9 is verified on this fix only when a TS-012 or ADR-056 revision adopts D18-2B with revision 1's Q-node wiring and D1 (F-1, F-7). That is INSP-118 X-12's condition. The cost moves to +0.63 to +1.22 USD against A5's USD 0.17 ordering-gate margin (section 6.3). That is INSP-110's lens, and it is noted here only because it could drive a later design change to this control.

### Verdict format (iteration 2)

```
ASSURANCE VERDICT: APPROVED
PRODUCT: docs/design/analysis/pa-permit-gate-d18.md@a6bcc2b1 (+ d18_run.py@5a06cfd8, decks, runs 2026-09-29-d18r1-*, as-drawn run reused) at c397ab1; PAIRED RECORD: not yet filed (X-1)
PRODUCT TYPE: trade-study-or-adr; CRITICALITY: safety-critical
FINDINGS:
- [Major, Verified] finding-1: every hardware cutoff now pulls the Q node (C1, C3 at the key-up level); D1 keeps a VGG path outside U1 (F6, F7); "still ends RF" corrected.
- [Minor, Open lien] finding-2 to finding-6: iteration 1, unchanged by revision 1.
- [Minor] finding-7, swe-134 task 1 / SA-C-g: D1 is the only U1-independent cutoff path, latent in service; its test is prototype-only and measures VGG, not the level.
- [Minor] finding-8, SA-C-i: Q-low margin 0.10 V against VIL with no ground-offset allowance, now carrying REQ-SYS-180, 181 and the cell trip at full PA current.
- [Minor] finding-9, SA-C-l: F-4 shared-node constraint and non-latching cutoff release not carried into the D-18 and K5/K8/K12 wording.
- [Minor] finding-10, SA-C-i: 07 section 14.2 row i and REQ-SW-SAFE-009 missing from F-6's routing of the REQ-SYS-120 level.
TASKS APPLIED: 11 (delta; see assurance_tasks_applied)
TASKS N/A (relief): swe-088 7.1 task 1 (07 section 10.2, paired record not filed)
SWE-134 ITEMS CHECKED: a, c, e, g, i, j, l
MEASUREMENTS: size=550-line record revision 1 (206-line delta), 1256-line checker, 20 sequencing cases, 21 static checks, 2 new figures; tasks=12; tasks_no=2; turns=40; minutes=75; major=0 new (1 verified); minor=4 new (9 open)
```
