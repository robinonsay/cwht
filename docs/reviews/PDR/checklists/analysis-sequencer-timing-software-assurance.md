---
# Peer-review record front matter (charter sections 2 and 5; docs/process/01-lifecycle-and-reviews.md section 13
# is the single field list; docs/process/07-software-engineering-plan.md sections 2.1.1, 10.2 and 15).
# This is the paired software assurance record (07 section 10.2) of the WP-PDR-23a file review, at the record path
# that PDR work plan WP-PDR-23 "Records" implies for analysis-sequencer-timing.md ("reviewer plus SA (sequencer is
# SW-TXSEQ safety-critical)"; plan section 3.0 row 23).
# Checklist applied: docs/templates/peer-review-checklist-software-assurance.md revision A AS ON ITS CR-012 BRANCH
# (cr/CR-012-pdr-checklist-templates at 7784672, blob 5b13528504868b2add0f0b1e329c63aa2b54cdf4; CR-012 not merged,
# still the case at HEAD 249356b). tools/validate_docs.py fails a record whose `checklist` names a template absent
# from main, so `checklist` names peer-review-checklist-design revision B (the INSP-075 and INSP-111 form) and
# `assurance_checklist` names the template actually applied.
# id: INSP-123, as iteration 1 proposed. At HEAD 249356b the highest id on main is INSP-135; INSP-122 and INSP-123
# are unused on main. The returned text of the WP-PDR-22 D-18 software assurance pair also proposes INSP-123, so the
# two collide; the lead SE renumbers one of them at filing (cross item X-5).
# Filing note: this text is the whole record: iteration 1 verbatim from its returned record text (only its title
# line is split into the record title and an "Iteration 1" heading, and the State cells of finding-1 and finding-2
# in its finding table read Verified, their state since iteration 2), the delta iteration 2 verbatim from its
# returned text, then the delta iteration 3. The front matter carries the iteration 3 state.
id: INSP-123
checklist: peer-review-checklist-design
checklist_revision: B
assurance_checklist: "docs/templates/peer-review-checklist-software-assurance.md@5b13528504868b2add0f0b1e329c63aa2b54cdf4 (revision A, branch cr/CR-012-pdr-checklist-templates at 7784672)"
checklist_file: docs/reviews/PDR/checklists/analysis-sequencer-timing-software-assurance.md
product: docs/design/analysis/sequencer-timing.md
# product_commit and product_files (iteration 3, the delta; rule C2 re-freeze F0): sequencer-timing.md revision 2
# with its checker, model, states file, README and render, committed at 249356b (on main; HEAD at the review). Each
# blob equals git rev-parse 249356b:<path>, git rev-parse HEAD:<path> and git hash-object <path>, for these 6 files
# and the 37 files of the four r2 run folders (43 of 43 equal). The four r2 run folders hold seq_run.py and
# relay_model.py byte-equal to the working copies; the run-folder copy of the render equals the figure.
# r2-s2-coil/coil_tran.raw (8,010,152 bytes) is untracked under CR-017 C2; its SHA-256 49905b7b...88dd73ff equals
# the committed raw.sha256
product_commit: "249356bab72557ebfd4307aa7e329d213f85f268"
product_files: ["docs/design/analysis/sequencer-timing.md@b6a5e31af5390f0606d038ca87c2e240536c6ef5", "docs/reviews/PDR/figures/timing-diagram.png@49db873d7a3940ede1135f4be449c6338a444e01", "hardware/sim/tx-seq/seq_run.py@d28ab4a171a7a6e5232d0273bd7213d0cd9e9b01", "hardware/sim/tx-seq/relay_model.py@0285c9c923925f331508a9ad8dcd73355b57fda1"]
# supporting files of the same commit, read with the product (iteration 3)
product_support_files: ["hardware/sim/tx-seq/expected_states.json@b45bc1b5", "hardware/sim/tx-seq/README.md@71e0d9d9", "hardware/sim/tx-seq/results/2026-09-29-r2-s1-drive/result.json@02366903", "hardware/sim/tx-seq/results/2026-09-29-r2-s1-drive/s1-coil-current.png@b35f9622", "hardware/sim/tx-seq/results/2026-09-29-r2-s1-drive/s1-coil-voltage-vs-pack.png@6b2906ff", "hardware/sim/tx-seq/results/2026-09-29-r2-s2-coil/result.json@78eaec2e", "hardware/sim/tx-seq/results/2026-09-29-r2-s2-coil/raw.sha256@ba9a0a12", "hardware/sim/tx-seq/results/2026-09-29-r2-s2-coil/s2-coil-transient.png@1fd58321", "hardware/sim/tx-seq/results/2026-09-29-r2-s3-operate/result.json@9323eeed", "hardware/sim/tx-seq/results/2026-09-29-r2-s3-operate/runs.json@49491ce8", "hardware/sim/tx-seq/results/2026-09-29-r2-s3-operate/s3-keydown-hold.png@ca5db560", "hardware/sim/tx-seq/results/2026-09-29-r2-s3-operate/s3-limiter-setpoint.png@bbfc5327", "hardware/sim/tx-seq/results/2026-09-29-r2-s3-operate/s3-operate-vs-coil-temperature.png@6262e1c0", "hardware/sim/tx-seq/results/2026-09-29-r2-s3-operate/s3-release.png@0e445bec", "hardware/sim/tx-seq/results/2026-09-29-r2-s4-sequence/result.json@03815632", "hardware/sim/tx-seq/results/2026-09-29-r2-s4-sequence/icd-tx-sw-timing-table.csv@71d6a4f7", "hardware/sim/tx-seq/results/2026-09-29-r2-s4-sequence/s4-keydown-budget.png@17aa3f02", "hardware/sim/tx-seq/results/2026-09-29-r2-s4-sequence/s4-margins.png@d7c2c8c5", "hardware/sim/tx-seq/results/2026-09-29-r2-s4-sequence/s4-stale-ratio.png@3ea0ceea"]
product_commit_iteration_2: "fb120d298a96de0e838e16d0cb5bad4f254f90bf"
product_files_iteration_2: ["docs/design/analysis/sequencer-timing.md@e4c9ad923beb817238c1ae4ef69dd1f59bc7f5d2", "docs/reviews/PDR/figures/timing-diagram.png@2b0f7678d55578a5bac51c3b1a5b576041e1b98e", "hardware/sim/tx-seq/seq_run.py@fbcad58599374c6520b47c71d87a6a10dfa3eee5", "hardware/sim/tx-seq/relay_model.py@0285c9c923925f331508a9ad8dcd73355b57fda1"]
product_support_files_iteration_2: ["hardware/sim/tx-seq/expected_states.json@2b730325", "hardware/sim/tx-seq/README.md@f29da6c8", "hardware/sim/tx-seq/results/2026-09-29-r1-s1-drive/result.json@3060f960", "hardware/sim/tx-seq/results/2026-09-29-r1-s1-drive/s1-coil-current.png@b35f9622", "hardware/sim/tx-seq/results/2026-09-29-r1-s1-drive/s1-coil-voltage-vs-pack.png@5716d91a", "hardware/sim/tx-seq/results/2026-09-29-r1-s2-coil/result.json@31d475bd", "hardware/sim/tx-seq/results/2026-09-29-r1-s2-coil/raw.sha256@2044ef92", "hardware/sim/tx-seq/results/2026-09-29-r1-s2-coil/s2-coil-transient.png@2335644a", "hardware/sim/tx-seq/results/2026-09-29-r1-s3-operate/result.json@c4890893", "hardware/sim/tx-seq/results/2026-09-29-r1-s3-operate/runs.json@c9ceb5a1", "hardware/sim/tx-seq/results/2026-09-29-r1-s3-operate/s3-release.png@1a89371b", "hardware/sim/tx-seq/results/2026-09-29-r1-s3-operate/s3-limiter-setpoint.png@48855f68", "hardware/sim/tx-seq/results/2026-09-29-r1-s3-operate/s3-operate-vs-coil-temperature.png@77bc91ca", "hardware/sim/tx-seq/results/2026-09-29-r1-s4-sequence/result.json@34758ff9", "hardware/sim/tx-seq/results/2026-09-29-r1-s4-sequence/icd-tx-sw-timing-table.csv@93657322", "hardware/sim/tx-seq/results/2026-09-29-r1-s4-sequence/s4-keydown-budget.png@17aa3f02", "hardware/sim/tx-seq/results/2026-09-29-r1-s4-sequence/s4-margins.png@d7c2c8c5", "hardware/sim/tx-seq/results/2026-09-29-r1-s4-sequence/s4-stale-ratio.png@d1e990e7"]
product_commit_iteration_1: "95adefc"
product_files_iteration_1: ["docs/design/analysis/sequencer-timing.md@8a628de6783ab811a78b6643da2f8288a5a4d331", "docs/reviews/PDR/figures/timing-diagram.png@c73c949737ca1b32c8cae43cd6f6b8d33dcaa500", "hardware/sim/tx-seq/seq_run.py@8de9e1c21919cecb43131fece12dcc90803f5abf", "hardware/sim/tx-seq/relay_model.py@1140d549bac1a393149a14cb3b4e1a7c518e41dc"]
product_support_files_iteration_1: ["hardware/sim/tx-seq/expected_states.json@3610deb4", "hardware/sim/tx-seq/README.md@df16e5d8", "hardware/sim/tx-seq/results/2026-09-29-s1-drive/result.json@0dd2cc7e", "hardware/sim/tx-seq/results/2026-09-29-s2-coil/result.json@205b9313", "hardware/sim/tx-seq/results/2026-09-29-s3-operate/result.json@cbbaee43", "hardware/sim/tx-seq/results/2026-09-29-s3-operate/runs.json@67530a83", "hardware/sim/tx-seq/results/2026-09-29-s4-sequence/result.json@cda544dd", "hardware/sim/tx-seq/results/2026-09-29-s4-sequence/icd-tx-sw-timing-table.csv@b2aea5b8"]
# inputs read at iteration 3 (not reviewed), at HEAD 249356b
input_files_iteration_3: ["docs/plan/pdr-work-plan.md (revision 6 at HEAD; WP-PDR-23 section, rules C1 to C13)", "docs/requirements/sys/requirements.json (REQ-SYS-097, 088, 156; REQ-SYS-097 TBR 'the power trade study at PDR fixes the value')", "docs/process/07-software-engineering-plan.md (section 14.1 line 590, SW-TXSEQ low-voltage transmit inhibit; section 14.2 row h, line 622; module row line 633)", "docs/safety/hazards.json (HZ-007 K4; HZ-008 causes and controls K1 to K7)", "docs/icd/ICD-PWR-CELL.md (per-cell supervision, two dissimilar paths)", "docs/conops/conops.md (OPS-009)", "docs/requirements/l0-stakeholder/expectations.md (MOE-004)", "docs/decisions/trade-studies/TS-012-design-to-cost-hand-built.md (section 8.1 line 602, section 8.7 line 815, section 8.12 line 991: unchanged)", "hardware/sim/tx-pa/results/2026-09-29-r3-p4-power-a5-design (WP-PDR-21 revision 3 at f1070cf: power_a5_design.cir, result.md, raw.sha256; the untracked power_a5_design.raw, 20,405,166 bytes, SHA-256 886371f6...a57306 equal to raw.sha256)"]
input_files_iteration_2: ["docs/plan/pdr-work-plan.md (revision 6 at HEAD; WP-PDR-23 section, rules C1 to C13)", "docs/safety/hazards.json (HZ-004 C5, C6, C10, K4, K5, K6, K8, K12, K13; HZ-008 C5, C6; HZ-014 C5, K3, K8)", "docs/requirements/sys/requirements.json (REQ-SYS-036, 097, 119, 156, 180)", "docs/test_cases/sys/test_cases.json (TC-SYS-108)", "docs/process/07-software-engineering-plan.md (section 14.2 row i, line 623)", "docs/decisions/trade-studies/TS-012-design-to-cost-hand-built.md (section 7.3 feed budget, line 515; section 8.1 diagram, line 602; section 8.7 'Firmware scope added (WP-PDR-35, 41)', line 815; section 8.12 row WP-PDR-23, line 991)", "docs/design/analysis/pa-permit-gate-d18.md revision 1 (sections 5.3 and 5.5: backwave level, driver-supply fall time)", "docs/design/analysis/thermal-budget.md at HEAD (D-5 mentions, routed by note section 6.1 item 7)"]
# inputs read at iteration 1 (not reviewed), blobs at HEAD ea462ec
input_files: ["docs/process/07-software-engineering-plan.md@bfe05f43 (sections 2.1.1, 14.1 line 590, 14.2 rows a to l, lines 615 to 626, SW-TXSEQ module rows 633 and 645)", "docs/safety/hazards.json@81cacde4 (HZ-004 C6, C10, K5, K6, K8, K12; HZ-008 C5, C6, K2, K4; HZ-014 K3, K8)", "docs/safety/hazard-analysis.md@52c8ce16 (section 7 rows b, c, g, h, i, j; section 8.2)", "docs/requirements/sys/requirements.json@f128235e (REQ-SYS-004, 036, 044, 119, 120, 156, 160, 161, 180, 182)", "docs/process/03-software-classification-and-rmm.md@ed270f44 (section 5 rows a to l)", "docs/decisions/trade-studies/TS-012-design-to-cost-hand-built.md@b9333386 (section 8.1 diagram, 8.3 row 12, 8.10 row REQ-SYS-055/120/180/092, 8.12 row WP-PDR-23, 8.14 D-5, D-18)", "docs/plan/pdr-work-plan.md@fd521750 (section 3.0 row 23, WP-PDR-23, rules C1 to C13)", "docs/reviews/PDR/checklists/ts-012-design-to-cost-software-assurance.md (INSP-118, for duplicates)", "tools/toolchain.lock.md (TV-014, ACC-LTSPICE-001)", "docs/process/rmm.json (SWE-070)"]
# paired_record: the WP-PDR-23a file review record docs/reviews/PDR/checklists/analysis-sequencer-timing.md is not
# filed at HEAD 249356b; its returned text proposes INSP-122, and its delta on revision 2 runs concurrently under its
# own invocation (cross item X-2); the lead SE writes its INSP id here at filing
paired_record: "pending (docs/reviews/PDR/checklists/analysis-sequencer-timing.md, INSP-122 proposed by its returned text, not filed at HEAD 249356b)"
# product_type: 07 section 2.1.1 has no row for a stand-alone analysis note (cross item X-1). The note fixes
# SW-TXSEQ and SW-SAFE design values and the D-5 relay drive (option E: TR_DRV a static level, coil voltage bounded
# by a hardware limiter), the input of the HZ-004 K12 backstop and of the PA-path gate, and the ICD-TX-SW timing
# table, so the section B row `design` is applied, plus the tasks of the other SWEs it implements
product_type: design
# criticality: 07 section 14.1 line 590 "PA enable and TX sequencer" (SW-TXSEQ), safety-critical; the PA_EN,
# safe_state() and ratio-age rows touch SW-SAFE (line 594), safety-critical
criticality: safety-critical
product_size: "iteration 3: 1 note revision 2 (532 lines; git diff fb120d2 249356b on the note and the script: 354 insertions, 91 deletions; 40 criteria, 40 timing-table rows, 7 bench measurements, new section 14 finding map), 1 sequence script (1981 lines, 17 checks, 2 new), 1 relay model (235 lines, unchanged), 1 render; 4 runs (2 LTspice, 2 Python). Iteration 2: 1 note (492 lines), 1 script (1758 lines, 15 checks), 1 model, 1 render, 4 runs. Iteration 1: 1 note (366 lines, 29 criteria, 35 rows), 1 script (1272 lines, 13 checks), 1 model (210 lines), 1 render, 4 runs"
sprint: PDR-prep
author_agent: "author:WP-PDR-23a (Claude, analysis author invocations of 2026-09-29, RF designer role; revision 0, revision 1 for the six Major findings, revision 2 for the two Major findings of the file review's delta iteration)"
reviewer_agent: "sa-reviewer:WP-PDR-23a-sequencer-timing-iter3 (independent; authored no part of WP-PDR-23a; not the iteration 1 or iteration 2 assurance reviewer)"
reviewer_agent_iteration_2: "sa-reviewer:WP-PDR-23a-sequencer-timing-iter2"
reviewer_agent_iteration_1: "sa-reviewer:WP-PDR-23a-sequencer-timing-iter1"
assurance_required: true
assurance_reviewer_agent: "sa-reviewer:WP-PDR-23a-sequencer-timing-iter3 (software assurance function, iteration 3; iteration 1 by sa-reviewer:WP-PDR-23a-sequencer-timing-iter1, iteration 2 by sa-reviewer:WP-PDR-23a-sequencer-timing-iter2; paired file review pending, docs/reviews/PDR/checklists/analysis-sequencer-timing.md, by the WP-PDR-23a independent reviewer)"
# iteration 3 is the delta on revision 2, which fixed the two Major findings of the paired file review's delta
# iteration (its finding-13 and finding-14; rule C1). This record had no open Major at iteration 2; iteration 3
# checks what revision 2 changes under the assurance lens
iteration: 3
# readiness_met: R1 to R3 hold at iteration 3. R4 holds for independence and for "in progress" (the file review's
# delta runs under its own invocation; its record is not filed at HEAD 249356b, cross item X-2)
readiness_met: true
# reviewer_verdict and assurance_verdict at iteration 3: APPROVED. finding-1 and finding-2 (Major) stay Verified
# (finding-2 criterion (2c) restated, see the iteration 3 section). finding-3 to finding-13 stay Minor liens;
# finding-14 to finding-16 (iteration 3) are new Minor liens (rule C1). Iteration 2: APPROVED. Iteration 1:
# NEEDS CHANGES (finding-1, finding-2)
reviewer_verdict: APPROVED
assurance_verdict: APPROVED
reviewer_verdict_iteration_2: APPROVED
assurance_verdict_iteration_2: APPROVED
reviewer_verdict_iteration_1: NEEDS CHANGES
assurance_verdict_iteration_1: NEEDS CHANGES
# verdict: set by Claude as software lead (07 section 10.2). Held at NEEDS CHANGES: the paired file review
# (iteration 1 and its deltas) is not filed and does not yet name this record, and the checklist applied exists only
# on cr/CR-012-pdr-checklist-templates (lead SE convention of 2026-09-27). The software lead sets APPROVED when the
# paired record carries the pairing with its own APPROVED verdict and CR-012 merges with the template blob unchanged
verdict: NEEDS CHANGES
# findings (all iterations): finding-1 and finding-2 (iteration 1, Major, Verified at iteration 2, still Verified at
# iteration 3); finding-3 to finding-8 (iteration 1, Minor, Open liens); finding-9 to finding-13 (iteration 2, Minor,
# Open liens; finding-9 and finding-10 facts moved by revision 2); finding-14 to finding-16 (iteration 3, Minor, Open)
findings_major: 2
findings_minor: 14
findings_open: 14
findings_fixed: 0
findings_verified: 2
findings_deferred: 0
assurance_findings_major: 2
assurance_findings_minor: 14
assurance_tasks_applied: ["swe-134 7.1 task 5", "swe-087 7.1 task 2", "swe-088 7.1 task 2", "swe-057 7.1 task 2", "swe-058 7.1 task 1", "swe-058 7.1 task 3", "swe-058 7.1 task 4", "swe-058 7.1 task 5", "swe-134 7.1 task 1", "swe-134 7.1 task 4", "swe-134 7.1 task 6", "swe-205 7.1 task 1", "swe-205 7.1 task 5", "swe-070 7.1 task 1", "swe-136 7.1 task 1", "swe-192 7.1 task 1", "swe-089 7.1 task 1", "swe-081 7.1 task 2"]
assurance_tasks_applied_iteration_2: ["swe-134 7.1 task 5", "swe-057 7.1 task 2", "swe-058 7.1 task 1", "swe-058 7.1 task 3", "swe-058 7.1 task 4", "swe-058 7.1 task 5", "swe-134 7.1 task 1", "swe-134 7.1 task 4", "swe-134 7.1 task 6", "swe-205 7.1 task 1", "swe-205 7.1 task 5", "swe-136 7.1 task 1", "swe-192 7.1 task 1", "swe-087 7.1 task 2", "swe-088 7.1 task 2", "swe-089 7.1 task 1", "swe-081 7.1 task 2"]
assurance_tasks_applied_iteration_1: ["swe-134 7.1 task 5", "swe-022 7.1 task 1", "swe-057 7.1 task 2", "swe-058 7.1 task 1", "swe-058 7.1 task 2", "swe-058 7.1 task 3", "swe-058 7.1 task 4", "swe-058 7.1 task 5", "swe-134 7.1 task 1", "swe-134 7.1 task 4", "swe-134 7.1 task 6", "swe-205 7.1 task 3", "swe-052 7.1 task 1", "swe-070 7.1 task 1", "swe-136 7.1 task 1", "swe-192 7.1 task 1", "swe-205 7.1 task 1", "swe-205 7.1 task 4", "swe-205 7.1 task 5", "swe-052 7.1 task 2", "swe-087 7.1 task 1", "swe-089 7.1 task 1", "swe-081 7.1 task 2"]
swe134_items_checked: [b, c, f, g, h, i, j]
swe134_items_checked_iteration_2: [a, b, c, f, g, h, i, j]
swe134_items_checked_iteration_1: [a, b, c, e, f, g, h, i, j, k, l]
deferred_rids: []
# items_no at iteration 3: the rows applied in the delta that answer No, each carrying an open Minor lien; the
# earlier No rows not re-applied (SA-C-a, SA-C-e, SA-C-k, SA-F1) stay with their liens finding-6, finding-7 and
# finding-8
items_no: ["swe-058 7.1 task 1", "swe-070 7.1 task 1", "swe-134 7.1 task 1", "swe-134 7.1 task 6", "swe-205 7.1 task 5", SA-C-c, SA-C-g, SA-C-h, SA-C-i, SA-D6]
items_no_iteration_2: ["swe-058 7.1 task 1", "swe-134 7.1 task 1", "swe-134 7.1 task 6", "swe-205 7.1 task 5", SA-C-a, SA-C-c, SA-C-h, SA-C-i, SA-D6]
items_no_iteration_1: ["swe-057 7.1 task 2", "swe-058 7.1 task 1", "swe-058 7.1 task 3", "swe-058 7.1 task 4", "swe-134 7.1 task 1", "swe-134 7.1 task 4", "swe-134 7.1 task 6", "swe-070 7.1 task 1", "swe-205 7.1 task 1", "swe-205 7.1 task 5", SA-C-a, SA-C-c, SA-C-e, SA-C-f, SA-C-g, SA-C-h, SA-C-i, SA-C-j, SA-C-k, SA-D1, SA-D6, SA-F1]
# effort: iteration 1 62 turns, 130 minutes; iteration 2 48 turns, 80 minutes; iteration 3 42 turns, 80 minutes
effort_turns: 152
effort_minutes: 290
record_status: Open
date: 2026-09-29
date_iteration_2: 2026-09-29
date_iteration_3: 2026-09-29
date_closed: null
---

# Peer review record INSP-123: software assurance pair of the WP-PDR-23a file review, sequencer timing

## Iteration 1 (2026-09-29; revision 0 at 95adefc)

**Product.** `docs/design/analysis/sequencer-timing.md` revision 0, blob `8a628de6`, at freeze commit `95adefc` (freeze F0, rule C2), with `timing-diagram.png` (`c73c9497`), `seq_run.py` (`8de9e1c2`) and `relay_model.py` (`1140d549`), the four blobs of the author's hand-off. Each equals `git rev-parse 95adefc:<path>`, `HEAD:<path>` at HEAD `ea462ec` and `git hash-object <path>`. `git log 95adefc..HEAD` touches no product path, and `95adefc` is on main. `expected_states.json`, the README and the s1 to s4 run folders of the same commit were read with the product. **Checklist applied:** `docs/templates/peer-review-checklist-software-assurance.md` revision A as on its CR-012 branch (blob `5b135285`, branch head `7784672`, not merged; see the front matter). **Paired record:** the WP-PDR-23a file review `docs/reviews/PDR/checklists/analysis-sequencer-timing.md` is not filed at HEAD `ea462ec` (X-2).

**Scope and acceptance criteria (rule C7).** Every task that section B assigns to the rows "Every product type" and `design`, and the section 7.1 tasks of the other SWEs the note implements (SWE-070 and SWE-136 for the models and LTspice, SWE-205, SWE-192, SWE-052). The SWE-134 items a to l as 07 section 14.2 allocates them to `SW-TXSEQ` (module row line 633: "a to l"), each checked against the values and design changes the note proposes. The cases the 07 rows enumerate:
- row a, reset and bootrom state of every RF-relevant output, the T/R drive included;
- row b, the only path to a carrier (T/R to TX, settle time elapsed, row h prerequisites true, then `PA_EN`), and cold switching on key-down, on key-up and on every path out of Transmit;
- row c, the `safe_state()` order (`PA_EN` first so that the T/R change is cold);
- row e, a `PA_EN` request rejected unless T/R is commanded TX and settled;
- row g, integrity of each safety-relevant input and output the note adds;
- row h, the "T/R in TX and settled" prerequisite;
- row i, no single software event producing RF with the T/R not in TX, and no software choice defeating a hardware control;
- row j, the response times the note sets or changes.

For each new or changed software function, the software contributions by action, inaction and incorrect action, and their routing to the hazard data writer (WP-PDR-16, plan section 5.3).

**Independence (rule C4; 07 section 2.1).** This invocation authored no part of the note, the scripts, the runs or the render, is not the WP-PDR-23a file reviewer, and edited no product file. The author, the file reviewer and this assurance reviewer are three different invocations. The counter-examples and numbers below are this reviewer's own.

**Search first (charter section 11 rule 1; rule C3).** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search. Queries covered the WP-PDR-23a record and SA pair; the SW-TXSEQ rows of 07 sections 14.1 and 14.2 and the T/R settle prerequisite; the transmission-length backstop and the node it watches; and owner actions on developer evidence. `grep -n` then only pinned lines in the note, the scripts, 07, `hazard-analysis.md`, TS-012 and the plan. Python extraction read the `hazards.json`, `requirements.json` and run rows. No rustos file was read.

## Record

### Findings

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | assurance | Major | swe-205 7.1 task 1; swe-134 7.1 tasks 1 and 6; swe-057 7.1 task 2; SA-C-i; SA-D1; SA-D6 | Note section 6.1 item 2 ("T/R drive at 100 % from t0 for 25 ms, then a 25 kHz PWM"); section 8 rows KD-04, KD-17, KU-06 (signal `TR_DRV`, "PWM"); `timing-diagram.png` panel (b) row "T/R drive: 100 % then 25 kHz hold"; the note names neither REQ-SYS-180, HZ-004 K12, HZ-014 K8 nor TC-SYS-108 | **The proposed hold PWM turns the signal that the firmware-independent transmission-length backstop watches into a 25 kHz waveform, and the note does not analyse or route that interaction.** HZ-004 K12 reads: "a second monostable watches the T/R transmit drive and removes the PA-path enable ... when the drive has stayed in transmit continuously for 150 s to 180 s (TBR), re-arming only when the drive returns to receive". HZ-014 K8 is the same control. REQ-SYS-180 defines continuous transmit as "the T/R drive held in transmit, with no pause longer than the hang time", and TC-SYS-108 captures "the T/R drive". In A5 the backstop is LM393 #1 (TS-012 section 8.1, row 27; WP-PDR-26), and no record names its input node. With D-5 as recommended, the drive line is low for 8 to 40 % of every 40 us period from t0 + 25 ms to the end of the over (duty 0.60 to 0.92 by the section 4.3 rule). A monostable that re-arms on a drive-low level, or on any drive edge, is re-armed every 40 us, so it never expires. The backstop is the only hardware element that bounds a toggling TX_KEY stream (HZ-004 K12; `hazard-analysis.md` section 8.2 row 3; HZ-004 C4, C9, C10 and HZ-014 C5). If it never expires, that branch has no hardware bound, the SWE-134 i argument of 07 section 14.2 row i and `hazard-analysis.md` section 7 row i fails, and the single point failure row 3 that decision 38 closed is open again. The same applies to the K12 proposal "the PA-path gate also requires the T/R transmit drive" (confirmed at PDR): a raw PWM on that gate input would chop the PA path at 25 kHz while keyed. The design change comes from this note and its ICD rows, so the gap is the note's. INSP-118 (TS-012 SA pair) did not raise it | Verified | Pending | |
| <a id="finding-2"></a>finding-2 | assurance | Major | swe-205 7.1 task 1; swe-134 7.1 tasks 1 and 4; swe-058 7.1 tasks 3 and 4; SA-C-f; SA-C-g; SA-C-i; SA-D1 | Note section 4.3 (the H1 hold at a 5.0 V average: "1.07 x the worst unit's must-operate current at an 85 C coil"; "Hold duty rule (proposed): D = min(1, 5.0 V / (V_pack,receive - 0.9 V))"); section 6.1 item 2 ("Firmware owns the duty"); section 4.2 reading (the late-contact failure mechanism); section 6.2 row WP-PDR-23b (drop-out named only "under shock") | **The recommended D-5 design makes the T/R hold during key-down depend on a firmware-computed PWM duty and pull-in timer. The note states no integrity provision for them and does not route this new software contribution to the hazard data.** Before D-5, any drive-on level held the relay. After it, the hold depends on three things: a duty computed from a pack reading, a PWM slice configuration, and a 25 ms pull-in timer. The note's own margin is 7 % at an 85 C coil (1.07 x). Reviewer run of the frozen `relay_model.py` (13 accepted H1 sets; Commands): at an 85 C coil the datasheet-guaranteed hold is lost when the pack reading is high by 6.2 % (at 6.35, 7.4 and 8.4 V). The worst accepted model set drops out at +20.5 % (at 23 C: +29 % and +46 %). A duty write error, a stale reading or a wrong PWM divider or top value does the same. A drop-out during key-down causes three effects: (a) the TX contact opens under RF, which is hot switching against 07 section 14.2 row b; (b) pole B releases the RX-input ground while the PA is keyed; (c) the mechanism of note section 4.2: "the detector sits after pole A, the loop integrates into an open contact, and VGG steps when the contact closes (a key click, and above the 8 W stability limit at 8.4 V)", which is HZ-008 C5 and C6. The other direction is a pull-in phase that never ends: the coil stays at 168 % of rating for the whole over. That is the K19 case, which the note limits to "25 ms per over" but does not bound against a firmware fault. `hazards.json` has no relay-hold cause (HZ-008 K2 names only the relay's harmonics). 07 section 14.2 row g reads back `PA_EN` and `TX_KEY` only, and no T/R drive or contact read-back is stated. The only detection is REQ-SYS-156 (Fault-safe within 100 ms of an implausible detector reading), which the note does not name for this case | Verified | Pending | |
| <a id="finding-3"></a>finding-3 | assurance | Minor | swe-134 7.1 task 1; swe-058 7.1 task 1; SA-C-h | Note section 2 row "Lead-in L" and s4 input `t_settle` (7.5 ms, "operate 7 ms + bounce 0.5 ms"); section 8 rows KD-10 (7.5), KD-11 (7.5), KD-12 (max 7.610, options C and D); section 5 K1a (datasheet point only); `timing-diagram.png` panel (a): the `PA_EN` edge at 10.5 ms is left of the end of the contact band at 10.61 ms | **The "T/R in TX and settled" prerequisite is set earlier than the note's own worst-case contact settle for the recommended option C.** 07 section 14.2 rows b and h make "settle time elapsed" a condition of `PA_EN`, and the note makes the prerequisite time-based at 7.5 ms (datasheet 7 ms at 23 C plus 0.5 ms). Its s3 result for option C is 7.11 ms plus 0.5 ms bounce, 7.610 ms at an 85 C coil (KD-12). `PA_EN` therefore rises up to 0.11 ms before the contacts have settled. For options A and B it rises with the contacts open, or not yet made. The consequence stays cold, because TX_KEY at t0 + 8.0 ms is after 7.61 ms, so the finding is Minor. But no criterion compares `t_settle` with KD-12, and the prerequisite's meaning is broken in the corner the note recommends. Fix: set the settle time from the K1b result of the fitted option with a stated margin. For option C, at least 7.61 ms, for example 7.75 ms, which still precedes TX_KEY at 8.0 ms and keeps K6. Add the criterion `t_settle` >= KD-12 max to s4. State in section 6.2 (to WP-PDR-32 and 35) that the prerequisite is a timer whose validity depends on the fitted coil, so that the design either keeps the timer with that condition or adds a contact read-back (for example of pole B) | Open | Pending | |
| <a id="finding-4"></a>finding-4 | assurance | Minor | swe-134 7.1 task 1; swe-058 7.1 task 4; SA-C-c | Note section 8 rows FP-01 to FP-03 (FP-03 "T/R to receive after PA_EN low", 0 to 0.05 ms after FP-01; `seq_run.py` line 971 labels it "(cold)"); FP-02 (RF at the off level within 0.1 ms, class E); section 5 K16 (checks only the 20 ms budget) | **The fault-path and reset-path cold switching is claimed by order only; the relay's opening delay that it rests on is neither computed nor checked.** 07 section 14.2 row c puts `PA_EN` first "so that the T/R change is cold". The note allows the T/R drive off 0 to 0.05 ms after `PA_EN` low, and RF reaches the off level within 0.1 ms (E). The TX contact starts to open when the armature leaves the closed stop. In `runs.json` of s3 (reviewer extraction; confirmed by reviewer run, Commands) that happens 0.235 ms after drive-off in the fastest accepted set from the H1 5.0 V hold at 85 C (`tau0.6_rho2_sig2`), and 0.004 ms from the standard-coil 63 % hold. The margin with the recommended coil is therefore 0.085 to 0.135 ms against a class E bound. On a watchdog or panic reset the pads release `PA_EN` and the T/R drive at the same instant, with no firmware order at all. Fix: add a criterion "RF at the off level before the TX contact leaves" over the band, with the D-18 gate's turn-off from `pa-permit-gate-d18.md`. Where firmware runs, either state a minimum `PA_EN`-low-to-T/R-off interval in the FP rows, or state that none is needed and why. Send the reset-path case to WP-PDR-23b and a logic-capture item to BM-3 | Open | Pending | |
| <a id="finding-5"></a>finding-5 | assurance | Minor | swe-134 7.1 task 6; SA-C-j; SA-D6 | Note Summary bullet 4 of "Other findings" (07 section 14.2 row j "needs restating (to WP-PDR-32 and 35, and the 07 owner)"); section 4.4; section 6.2 rows | **The key-up restatement is routed without the governing hazard-analysis text and without the new bound.** 03 section 5 makes `hazard-analysis.md` section 7 the provision text and numbers, and its row j reads "key-up to envelope fall start within one sample plus the 5 ms open debounce" (writer WP-PDR-16). The note routes the change only to WP-PDR-32 and 35 and to the 07 owner. It also gives the new response only from the keyer edge (fall start one lead-in later; last TX_KEY low 14 to 19.04 ms later), not from the contact opening that row j references. From the jack the new bound is 5 ms debounce, plus up to 1 ms sample, plus 10.043 ms to the fall start, which is 16.04 ms; RF is off at the end of the fall, up to 24.04 ms. The 07 row j sentence "`PA_EN` falls after the fall completes ..., one configured envelope time later (HZ-008 K4)" also becomes "at the end of the over" under D-18. Fix: state both bounds from the contact opening in section 4.4 and as a timing-table row. Add WP-PDR-16 (`hazard-analysis.md` section 7 row j and the HZ-008 K4 reference) to the section 6.2 routing | Open | Pending | |
| <a id="finding-6"></a>finding-6 | assurance | Minor | swe-134 7.1 task 1; SA-C-a | Note section 6.1 item 2 ("the reset and bootrom state is off (the NC contacts connect the antenna to the receiver)"); section 8 row KD-04; no pull-down named for `TR_DRV` in the note or in TS-012 (TS-012 section 8.1 gives 4.7 kohm pull-downs to TX_KEY and PA_EN only) | **The reset state of the T/R drive is asserted without the hardware provision that makes it hold.** HZ-004 K6 and HZ-014 K3 count "the T/R relay's unpowered state connects the antenna to the receiver" as part of the reset and bootloader layer of REQ-SYS-119. For TX_KEY and PA_EN they add external 4.7 kohm pull-downs "inside the RP2350-E9 '8.2 kohm or less' guidance", because the internal pull-down (36 to 113 kohm, HZ-004 C6) does not hold a pad low under E9. The relay driver input has no such provision. With the H1 coil a pad that floats high during bootloader or firmware load pulls the relay in: the must-operate current is 20.5 mA (s1), which a 2N3904 or an AO3400A supplies from a gate or base near 2 V. That removes the relay layer of K6 in those states. Fix: request an external pull-down on the relay driver input (4.7 kohm class, inside the E9 guidance) in section 6.1 for WP-PDR-37. Carry it in the KD-04 row and in the request to WP-PDR-36a, and send the K6 and HZ-014 K3 wording to WP-PDR-16 | Open | Pending | |
| <a id="finding-7"></a>finding-7 | assurance | Minor | swe-134 7.1 task 1; swe-058 7.1 task 1; SA-C-e; SA-C-k | Note section 4.6 ("the smallest lead-in the ordering allows grows 1:1 with any relock time beyond the allocation"); K8, K8b; section 8 rows KD-09 (max 8.0), KD-11 ("never after TX_KEY"); section 6.2 row WP-PDR-32, 35 ("PA_EN = both prerequisites, never after TX_KEY") | **The note sets the rule "PA_EN never after TX_KEY" but not what the sequencer does when the frequency check or the lock is late.** The latest lock-gated FC0 start that keeps the order is t0 + 1.903 ms (K8b), and WP-PDR-20a M-1 has not measured the relock yet. A late check leaves three behaviours open: hold TX_KEY and the ramp, which breaks the constant lead-in of REQ-SYS-161 and K2b for the first element; drop the element; or abort the over to receive and log. There is also a fourth case: a permit that arrives after TX_KEY would release the D-18 clamp with the envelope reference already rising, a power step (HZ-008 C5). 07 section 14.2 row e covers this case only if the late permit is rejected for that element. Fix: state the response and the rejection of a late permit in section 4.6 and as a timing-table row. Carry both to WP-PDR-32 and 35 with the error class (07 section 14.2 row k) | Open | Pending | |
| <a id="finding-8"></a>finding-8 | assurance | Minor | swe-070 7.1 task 1; SA-F1 | Note header row "Evidence status" ("`seq_run.py` and `relay_model.py` have no TV record"); section 7 (the REQ-SYS-160 and 161 proposals "conditional on section 6.1 or BM-2"); section 6.1 (the D-5 coil choice rests on the class E model for options B, C and D, section 10 item 1) | **The D-5 recommendation and the conditions on the two TBR proposals rest on unaccredited Python models, and no owner action or assurance risk records that.** `rmm.json` SWE-070 (FC) plans validation evidence for "LTspice decks and Python checkers" before their results are used. LTspice itself is accredited (ACC-LTSPICE-001, TV-014). The note states the developer-evidence status correctly. Rule C10 sends the values to the owner after this record is APPROVED, so the owner would rule on developer evidence unless a TV record exists or the owner accepts it. This is the same gap as INSP-075 finding-5, which is still Open, and plan section 6.1 has no owner action for either. Fix: before S2, file a class B TV record for `relay_model.py`, or add the owner action to plan section 6.1 for both records. For the TV record, candidates are the s2 closed-form and LTspice cross-checks (`closed_form`, `model_vs_ltspice_rise`) as known answers, and a seeded error in the calibration anchor. In both cases submit the concern to the risk register writer (WP-PDR-18) as an entry tagged `assurance` | Open | Pending | |

Two Major findings: `assurance_verdict` NEEDS CHANGES (07 section 10.2; rule C1).

**What would fix the two Major findings:**
- **finding-1.** State which signal the backstop senses in transmit: a separate "T/R commanded TX" level; the drive filtered with a time constant between the 40 us PWM period and the shortest hang (72 ms, 3 dits at 50 WPM); or the coil current. Show in s4 that this signal is continuous through the pull-in, the hold PWM and the hang, and that it returns to receive only at the hang expiry. Carry the result as an ICD-TX-SW row. Route it to:
  - WP-PDR-26 (the LM393 #1 backstop input);
  - WP-PDR-16 (the HZ-004 K12 and HZ-014 K8 text "watches the T/R transmit drive");
  - WP-PDR-22 and D-18 (the proposed T/R input of the PA-path gate);
  - WP-PDR-37;
  - WP-PDR-43 (TC-SYS-108 logs "the T/R drive").
- **finding-2.** Name the software causes and route them to WP-PDR-16 for HZ-008 (C5 and C6) and for the 07 row b cold-switching provision:
  - a hold duty too low: a wrong pack reading, a duty write error, a PWM configuration error;
  - a pull-in phase that does not end.

  In the section 6.2 request to WP-PDR-32 and 35, set the integrity provisions. The duty comes from a range- and plausibility-checked pack reading, with a stated measurement tolerance that fits inside the hold margin. Alternatively, raise the hold target so that it does (for example 5.5 V: 1.18 x at 85 C, about 0.18 W). The duty and the PWM configuration are held with their complement or read back (SWE-134 f, g). The pull-in phase has a bound that one software fault cannot defeat, or its failure is analysed against the K19 derating. Name the detection that remains (REQ-SYS-156, 100 ms) and its exposure, and add a firmware fault-injection case to BM-4.

The rest stands from the assurance lens:
- the key-down schedule K1, K2, K2b, K3 to K7 and the end-of-over order of 07 row b (KU-04 to KU-06, K10, K11);
- the ICD-TX-SW owner split (`PA_EN` only by SW-SAFE, TX_KEY by SW-TXSEQ; 07 section 14.1 line 590, TS-012 D-18, REQ-SYS-120);
- the rejection of the interval-13 fallback (K9);
- the relock-margin finding (K8, K8b);
- the key-bounce conditions (K3b, K17), routed to WP-PDR-40;
- the K16 budget against REQ-SYS-004 and the 10 ms of `hazard-analysis.md` section 7 row j.

The file review is not filed, so no concurrence can be stated (X-2).

### Task table

| Task | Safety-critical designation (SWEHB 8.10 section 6) | Applied | Result and evidence | Relief (N/A only) | Finding ids |
|---|---|---|---|---|---|
| swe-134 7.1 task 5 (every type) | SC | Yes | This record is the assurance participation in the review of a product that sets `SW-TXSEQ` and `SW-SAFE` design values (07 section 14.1 lines 590 and 594) | | none |
| swe-022 7.1 task 1 (every type) | SC | Yes | Performed against the software assurance plan, 07 section 15, by this review | NASA-STD-8739.8 part: `rmm.json` SWE-022 T (standard not in the corpus) | none |
| swe-057 7.1 task 1 (design) | | N/A | The note has no software architecture content | 07 section 2.1.1 row "Design": the architecture product is the software section of `docs/design/architecture.md` (WP-PDR-32) | |
| swe-057 7.1 task 2 (design) | | No | The hold PWM on `TR_DRV` meets its purpose (D-5 thermal relief) but, unconstrained, defeats the independent backstop that watches the same line | | finding-1 |
| swe-058 7.1 task 1 (design) | | No | Each value was checked against its requirement and 07 row. The settle prerequisite disagrees with the note's own KD-12 (finding-3). The late-check response is not defined (finding-7) | | finding-3, finding-7 |
| swe-058 7.1 task 2 (design) | | Yes | The sequence is stated as event times with owners per signal (section 8), consistent with 07 section 14.2 row b and the D-18 owner split. No code units are defined, and none is needed at analysis maturity | | none |
| swe-058 7.1 task 3 (design) | | No | The hold PWM adds an undesired behaviour: a firmware duty or configuration fault drops the relay under RF | | finding-2 |
| swe-058 7.1 task 4 (design) | SC | No | Cold switching (07 row b) is not kept against a software hold fault, and the fault-path cold switching is claimed without its basis | | finding-2, finding-4 |
| swe-058 7.1 task 5 (design) | | Yes | This record's own design analysis: hold margin against a pack over-read and the TX-contact opening time on the frozen model (Commands); hand re-computation of K1, K3, K3b, K5, K8, K8b, K9, K10, K12-D, K14, K16, K17 and the option A and C must-operate ratios at 85 C (all agree) | | finding-2, finding-4 |
| swe-134 7.1 task 1 (design) | SC | No | Section C: items a, c, e, f, g, h, i, j, k are not fully met by the values and design changes as stated | | finding-1 to finding-7 |
| swe-134 7.1 task 4 (design) | SC | No | The `SW-SAFE` permit's "T/R in TX and settled" input is a `SW-TXSEQ` timer on its own command. The hold duty, a new safety datum, has no stated protection | | finding-2, finding-3 |
| swe-134 7.1 task 6 (design) | SC | No | The proposed design would disagree with HZ-004 K12, HZ-014 K8, REQ-SYS-180's "T/R drive held in transmit" and `hazard-analysis.md` section 7 row j unless they change with it. None is in the routing | | finding-1, finding-5, finding-6 |
| swe-143 7.1 task 1 (design) | | N/A | No architecture review is held on this product | 07 section 2.1.1 row "Design": the SWE-143 review is the WP-PDR-32 architecture review with SA | |
| swe-205 7.1 task 3 (design) | SC | Yes | The note adds or moves no component. The hold PWM and the settle timer stay in `SW-TXSEQ`, and `PA_EN` stays in `SW-SAFE` (07 section 14.1) | | none |
| swe-052 7.1 task 1 (design) | | Yes | Section 1 traces each criterion to its requirement or 07 row. No code exists at this maturity | | none |
| swe-070 7.1 task 1 (models) | | No | `seq_run.py` and `relay_model.py` have no TV record; the D-5 choice and the TBR conditions rest on them (developer evidence, 05 section 9.1) | | finding-8 |
| swe-136 7.1 task 1 (tool) | | Yes | LTspice 26.0.2 through `tools/ltspice-batch.sh` is accredited (ACC-LTSPICE-001, TV-014, `tools/toolchain.lock.md` line 269). The s1 and s2 logs carry "LTspice 26.0.2 for MacOS". matplotlib renders only | | none |
| swe-192 7.1 task 1 | SC | Yes | REQ-SYS-004, 119, 120, 156, 180 and 182 (hazard-tracing) have method Test with closing cases; REQ-SYS-160 and 161 (Test) carry no `hazard_ids`. R3 run: 0 violations. The note claims no closure | | none |
| swe-205 7.1 task 1 | SC | No | Three software contributions introduced by the recommended design are not routed to the hazard data: the backstop defeat by the hold PWM, the hold duty and pull-in faults, and the undriven T/R drive in reset | | finding-1, finding-2, finding-6 |
| swe-205 7.1 task 4 | SC | Yes | Section D, SA-D3 | | none |
| swe-205 7.1 task 5 | SC | No | The software safety analysis updates the design needs (the HZ-004 K12 branch, the hold-fault causes, the row j key-up text) are not requested | | finding-1, finding-2, finding-5 |
| swe-052 7.1 task 2 | SC | Yes | Section D, SA-D3: HZ-004 K5, K6, K8, K12 and HZ-008 K4, K7 trace to their requirements and back | | none |
| swe-134 7.1 task 3 | SC | N/A | No loaded data is set by the note (the hold duty rule is code, not loaded data) | 07 section 9.7 (loaded data, SWE-193 cases) | |
| swe-087 7.1 task 1 | | Yes | This record and the file review are the peer review of the product, reported in `docs/reviews/PDR/checklists/` | | none |
| swe-087 7.1 task 2, swe-088 7.1 task 2 | | N/A | Iteration 1: no finding is fixed yet | 07 section 10.2 (fixes verified in the delta iteration) | |
| swe-088 7.1 task 1 | | N/A | The paired file review is not filed at HEAD `ea462ec`; SA-A4 cannot be answered | 07 section 10.2 (the software lead checks the pairing at filing; X-2) | |
| swe-089 7.1 task 1 | | Yes | Section E, SA-E2 (this record); the paired record's measurements are checked at filing (X-2) | | none |
| swe-081 7.1 task 2 | SC | Yes | The product is committed on main at `95adefc`; `hazards.json` and `hazard-analysis.md` are under CM (05 Table 4-1); the uncommitted `coil_tran.raw` matches its committed `raw.sha256` (bb627b82...996eae, 7,114,568 bytes; CR-017 C2) | | none |

## Readiness criteria

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | Frozen, and the same blobs as the paired record | Yes (own part) | `git rev-parse 95adefc:<path>` = `HEAD:<path>` = `git hash-object` for the 4 blobs. The paired record's list is checked at filing (X-2) |
| R2 | Row and criticality identified | Yes | `product_type` design and `criticality` safety-critical from 07 section 14.1 line 590 (`SW-TXSEQ`) and line 594 (`SW-SAFE`); routing by plan WP-PDR-23 (X-1) |
| R3 | validate_docs and traceability clean for the ids touched | Yes | `tools/traceability.py --report-only --output <scratch>/traceability-report.md`: 245 requirements, 173 test cases, 0 violations, 2 warnings (REQ-SYS-125, 148 SYS_UNALLOCATED, not ids of this product); `docs/vv/` unchanged. The record's front matter was checked with the `tools/validate_docs.py` functions (Commands) |
| R4 | Paired review filed or in progress by its own invocation; this reviewer independent | Yes (in progress) | The WP-PDR-23a file review runs under its own invocation; its record is not filed at HEAD `ea462ec`. This invocation is neither the author nor that reviewer |

## A. Dispatch, independence and record integrity

| Id | Answer | Evidence |
|---|---|---|
| SA-A1 | Yes, with X-1 | Routed by PDR work plan WP-PDR-23 ("independent reviewer plus SA (sequencer is SW-TXSEQ safety-critical)") and section 3.0 row 23. 07 section 2.1.1 has no row for a stand-alone analysis note (INSP-075 X-1, still open) |
| SA-A2 | Yes (own part) | Author `author:WP-PDR-23a`; this reviewer; the file reviewer is a third invocation (not filed, X-2) |
| SA-A3 | Yes (own part) | Same `product` and 4 blobs as the author's hand-off; the paired record's list is checked at filing (X-2) |
| SA-A4 | N/A | The paired record is not filed at HEAD `ea462ec`; the software lead checks SWE-088 criteria a to d at filing (X-2) |

## B. SWE-to-task table

| Id | Answer | Evidence |
|---|---|---|
| SA-B1 | Yes | Task table: row "Every product type", row `design`, and the tasks of SWE-070, SWE-136, SWE-192, SWE-205, SWE-052, SWE-134 task 3, SWE-087, SWE-088, SWE-089 and SWE-081. `assurance_tasks_applied` lists every Yes and No row |
| SA-B2 | Yes | N/A rows cite 07 section 2.1.1 row "Design", 07 section 9.7 and 07 section 10.2. The only SC task answered N/A is swe-134 task 3, relieved by 07 section 9.7 |
| SA-B3 | Yes | Every No row cites a finding |

## C. SWE-134 items a to l (07 section 14.2 shared rows and the `SW-TXSEQ` module rows, lines 633 and 645)

| Id | Answer | Evidence |
|---|---|---|
| SA-C-a | No | TX_KEY and `PA_EN` hold RF off at reset by their pull-downs. The T/R drive's reset state is asserted without a pull-down (finding-6) |
| SA-C-b | Yes | Key-down: the carrier path runs T/R write, check, `PA_EN`, TX_KEY, ramp (section 4.1; `timing-diagram.png` panel (a)). Key-up: fall, TX_KEY low, hang, then `PA_EN` low, CLK1 off and T/R off inside 0.5 ms (KU-04 to KU-06). Both follow 07 row b. The settle value is finding-3; hot switching from a hold fault is finding-2 (item i) |
| SA-C-c | No | The FP order puts `PA_EN` first, but the cold T/R change rests on an unstated 0.235 ms opening delay against a 0.1 ms class E bound, and on nothing on the reset path (finding-4) |
| SA-C-d | N/A | The note sets no operator override |
| SA-C-e | No | "PA_EN never after TX_KEY" is stated, but the rejection of a late permit and the response to a late check are not (finding-7) |
| SA-C-f | No | The hold duty and the pull-in timer are new safety data with no complement or read-back stated (finding-2) |
| SA-C-g | No | No read-back of the T/R drive or the contacts, and no plausibility check of the pack reading that sets the duty (finding-2) |
| SA-C-h | No | The "T/R in TX and settled" timer (7.5 ms) is shorter than KD-12 max 7.61 ms for option C (finding-3). The frequency prerequisite is met: K5 7.097 ms before 7.5 ms, margin K8 0.903 ms |
| SA-C-i | No | A hold PWM that the backstop cannot integrate removes the only hardware bound on a toggling stream (finding-1). One hold-duty or PWM-configuration fault drops the relay under RF (finding-2). REQ-SYS-120's two conditions are kept (KD-11, KD-13; D-18) |
| SA-C-j | No | K16 is 1.1 ms against 20 ms (REQ-SYS-004) and 10 ms (`hazard-analysis.md` section 7 row j). The new key-up bound from the contact opening is not stated, and the governing row j text is not routed (finding-5) |
| SA-C-k | No | The late-check error path has no defined response (finding-7) |
| SA-C-l | Yes | `safe_state()` (FP-01 to FP-03) is reachable from every sequence state in the table; the order is unchanged from 07 row c |

## D. Software safety analysis and hazard traceability

| Id | Answer | Evidence |
|---|---|---|
| SA-D1 | No | SWEHB `swe-205` section 7.7.2 walked. Four considerations apply. **Control of safety-critical hardware:** the relay hold PWM (finding-2). **Interlocks and inhibits:** the backstop (finding-1) and the reset pull-downs (finding-6). **Common cause and independence:** `TR_DRV` shared between the sequencer and the backstop (finding-1), and the settle timer on SW-TXSEQ's own command feeding the SW-SAFE permit (finding-3). **Timing of safety responses:** row j (finding-5). None of these contributions is in `hazards.json` |
| SA-D2 | Yes | The note changes no component or criterion; 07 section 14.1 and 03 section 4.3 unchanged |
| SA-D3 | Yes | R3: 0 violations, no `HAZARD_CONTROL_UNTRACED` or `HAZARD_INVERSE`. HZ-004 K12 `control_req_ids` REQ-SYS-180, and K8 REQ-SYS-120 (with REQ-SW-KEYER-030, 034 and REQ-TX-014), match the requirements' `hazard_ids` |
| SA-D4 | N/A | No `SW-TXSEQ` requirement exists at this maturity (`docs/requirements/sw/` holds `sw-keyer` only); WP-PDR-35 writes them |
| SA-D5 | Yes | Every hazard-tracing requirement in scope has a closing Test case (R3; `rmm.json` SWE-192 FC) |
| SA-D6 | No | The hazard-analysis updates the proposed design needs are not requested (findings 1, 2, 5) |

## E. Peer review, change and configuration assurance

| Id | Answer | Evidence |
|---|---|---|
| SA-E1 | N/A | First review of the product; no earlier findings |
| SA-E2 | Yes | This record carries the SWE-089 fields of 07 section 10.3; the paired record's are checked at filing (X-2) |
| SA-E3 | Yes | `git show --stat 95adefc` adds only the WP-PDR-23a files (39 files, 12,555 insertions). No requirement, hazard, ICD or trade-study file is edited, so no CR route applies. `tools/check_commit_msg.py --range 95adefc~1..95adefc`: PASS (Refs REQ-SYS-160, 161, 120, 182, HZ-004, TS-012, WP-PDR-23a). The one raw file above 5,000,000 bytes is kept uncommitted with `raw.sha256`, which matches it (CR-017 C2) |
| SA-E4 | N/A | No test is run for credit; the scripts are developer evidence (finding-8) |

## F. Assurance risks, metrics and reporting

| Id | Answer | Evidence |
|---|---|---|
| SA-F1 | No | The model-accreditation concern is not submitted as an `assurance` risk entry (finding-8). The other concerns are product defects (findings 1 to 7) |
| SA-F2 | Yes | Front matter: `assurance_findings_major` 2, `assurance_findings_minor` 6, `items_no`, effort |
| SA-F3 | Yes | Verdict, open findings, tasks applied and reliefs are in this record |

## Cross items for the software lead (not findings on the note)

- **X-1.** 07 section 2.1.1 still has no row for stand-alone analysis notes that set values of a section 14.1 component (INSP-075 X-1). This record runs on the plan's routing (WP-PDR-23).
- **X-2.** The paired file review record `analysis-sequencer-timing.md` is not filed at HEAD `ea462ec`. At filing, the software lead writes its INSP id into `paired_record` here and transcribes this pairing into it (`assurance_reviewer_agent`, `assurance_verdict` NEEDS CHANGES). The software lead also checks SA-A3 (same blobs) and SA-A4 (checklist and SWE-088 a to d) there. INSP-122 is left free for it.
- **X-3.** Finding-1 reaches beyond this note. The backstop input must be fixed in WP-PDR-26 and in the HZ-004 K12 and REQ-SYS-180 texts whichever D-5 option is built, because the TS-012 D-5 first option ("coil held by PWM after pull-in") has the same property. It should also be carried to the TS-012 record (WP-PDR-54).
- **X-4.** `frequency-budget.md` (K8, K8b, rows KD-06 to KD-09) and `pa-permit-gate-d18.md` (KD-14, finding-4's RF-off bound) are under review. A change in either re-opens those rows in the delta iteration, as the note's header states.

## Commands

- `git rev-parse 95adefc:<path>`, `HEAD:<path>` and `git hash-object <path>` for the 4 product files: equal. `git log 95adefc..HEAD` on the product paths: empty. `git merge-base --is-ancestor 95adefc HEAD`: true.
- `git archive 95adefc hardware/sim/tx-seq tools docs/reviews/PDR/figures/timing-diagram.png | tar -x` into the scratchpad, then `.venv/bin/python hardware/sim/tx-seq/seq_run.py s3` and `s4` there: 13 of 13 checks PASS. The 29 verdicts equal `expected_states.json` and note section 5. Of s3, `result.json`, `result.md`, `runs.json` and both PNGs are byte-identical to `95adefc` (`cmp`). Of s4, `result.json`, `result.md`, the timing-table CSV and Markdown, three PNGs, and the regenerated `docs/reviews/PDR/figures/timing-diagram.png` are byte-identical.
- s1 re-run in a second scratch copy through `tools/ltspice-batch.sh` with `CWHT_LTSPICE_LOCK_WAIT=7200`. Batch result PASS: deck sha256 befa821a..., "LTspice 26.0.2 for MacOS", LTspice exit 0. `result.md`, `drive_dc.cir` and `s1-coil-current.png` are byte-identical. `result.json` differs only in the batch provenance lines and in the `.raw` sha256, because the `.raw` carries its run date. `drive_dc.log` differs only in the temp path, the start time and the elapsed time (0.331 against 0.332 s). The script exits 1, as expected with FAIL and OPEN criteria.
- s2 (LTspice) was not re-run: `ltspice-batch: busy: another LTspice run held the lock for more than 580 s`, twice, because another invocation's long run held the lock. The committed s2 `result.md`, `result.json` and `coil_tran.log` were read instead ("LTspice 26.0.2 for MacOS"; checks steps, closed_form and ripple PASS; LTspice against closed form within 0.4 %).
- Reviewer script `sa_hold.py` (scratchpad; imports the frozen `relay_model.py` unchanged; `D_SLOW` of `seq_run.py` line 159):
  - The 13 accepted H1 sets reproduce s3. The model drop-out average is at most 4.039 V at 85 C (3.248 V at 23 C). The datasheet-guaranteed hold is at least 4.664 V at 85 C (3.750 V at 23 C).
  - Duty rule against a pack over-read: the guarantee is lost at x1.062 to x1.065, and the worst set drops out at x1.205 to x1.213 (85 C, packs 6.35 to 8.4 V).
  - TX-contact opening after drive-off from the 5.0 V hold at 85 C: 0.235 ms (`tau0.6_rho2_sig2`) to 9.688 ms. The same minimum is extracted from the committed `runs.json`, whose standard-coil 63 % hold gives 0.004 ms.
  - Render `sa-hold-margin.png`, opened and inspected: panel (a) hold average against the over-read with both thresholds; panel (b) the opening times per set against the FP-02 and FP-03 bounds.
- Renders opened and inspected: `timing-diagram.png` (panel (a) shows the `PA_EN` edge at 10.5 ms before the end of the option C and D contact band at 10.61 ms, finding-3; panel (b) shows the T/R drive as a PWM line to the hang expiry, finding-1); `s1-coil-current.png`; `s2-coil-transient.png`; `s3-operate-vs-coil-temperature.png`; `s3-release.png`; `s4-keydown-budget.png`; `s4-margins.png`. Axes, limits and labels agree with note sections 3 and 4.
- `tools/traceability.py --report-only --output <scratch>/traceability-report.md`: exit 0, 0 violations; `git status docs/vv/` clean.
- `tools/check_commit_msg.py --range 95adefc~1..95adefc`: PASS.
- `shasum -a 256 hardware/sim/tx-seq/results/2026-09-29-s2-coil/coil_tran.raw` equals `raw.sha256`; 7,114,568 bytes.
- The front matter of this record was checked with the `tools/validate_docs.py` functions, in memory, against HEAD. `parse_front_matter` and `parse_front_matter_subset` both parse it. `validate_mapping` against `PEER_REVIEW_RECORD_SCHEMA` gives 0 errors, and the `peer-review-checklist-design` template is present on main. `check_record_drift` against `head_blobs` gives 0 errors and 0 notes. The id INSP-123 is unused on main, on the branches and in the working tree. The file-level `validate_docs.py` run falls to the lead SE at filing, because a new record file is not created by this invocation.

## Measurements (SWE-089)

Tasks in the task table: 29 rows (23 applied Yes or No, 6 N/A); tasks answered No: 10. Section items checked: 38 (R1 to R4, SA-A1 to A4, B1 to B3, C-a to C-l, D1 to D6, E1 to E4, F1 to F3), answered No: 12. Findings: 2 Major, 6 Minor; fixed 0; deferred 0. Iteration 1. Effort: 62 turns, about 130 minutes. Renders inspected: 8 (7 of the product, 1 reviewer). Reviewer re-runs: s1, s3 and s4 reproduced (data byte-identical); s2 not re-run (LTspice lock held by another invocation). One reviewer script (13 sets, 2 checks).

## Verdict

```
ASSURANCE VERDICT: NEEDS CHANGES
PRODUCT: docs/design/analysis/sequencer-timing.md@8a628de6, docs/reviews/PDR/figures/timing-diagram.png@c73c9497, hardware/sim/tx-seq/seq_run.py@8de9e1c2, hardware/sim/tx-seq/relay_model.py@1140d549 at 95adefc; PAIRED RECORD: pending (analysis-sequencer-timing.md, not filed)
PRODUCT TYPE: design (routed by PDR work plan WP-PDR-23; X-1); CRITICALITY: safety-critical
FINDINGS:
- [Major] swe-205 7.1 task 1 (SA-C-i) the 25 kHz hold PWM on TR_DRV defeats the HZ-004 K12 / REQ-SYS-180 backstop that watches the T/R drive; not analysed or routed.
- [Major] swe-205 7.1 task 1 (SA-C-f, g, i) the firmware-set hold duty and pull-in timer can drop the relay under RF (6.2 % pack over-read loses the guaranteed hold at 85 C) or overdrive it; no integrity provision, not in the hazard data.
- [Minor] swe-134 7.1 task 1 (SA-C-h) "T/R in TX and settled" at 7.5 ms precedes the note's own option C settle of 7.61 ms; no criterion compares them.
- [Minor] swe-134 7.1 task 1 (SA-C-c) fault and reset path cold switching rests on an unstated 0.235 ms contact-opening delay against a 0.1 ms class E RF-off bound.
- [Minor] swe-134 7.1 task 6 (SA-C-j) the key-up restatement omits hazard-analysis section 7 row j (WP-PDR-16) and the bound from the contact opening (16.04 ms to fall start, 24.04 ms to RF off).
- [Minor] swe-134 7.1 task 1 (SA-C-a) no pull-down on the relay driver input for the reset and bootloader states (HZ-004 K6, RP2350-E9).
- [Minor] swe-134 7.1 task 1 (SA-C-e, k) no response defined for a late frequency check or a permit arriving after TX_KEY.
- [Minor] swe-070 7.1 task 1 (SA-F1) no TV record for relay_model.py and seq_run.py and no owner action on developer evidence; no assurance risk entry.
TASKS APPLIED: swe-134 7.1 task 5, swe-022 7.1 task 1, swe-057 7.1 task 2, swe-058 7.1 tasks 1 to 5, swe-134 7.1 tasks 1, 4, 6, swe-205 7.1 tasks 1, 3, 4, 5, swe-052 7.1 tasks 1, 2, swe-070 7.1 task 1, swe-136 7.1 task 1, swe-192 7.1 task 1, swe-087 7.1 task 1, swe-089 7.1 task 1, swe-081 7.1 task 2
TASKS N/A (relief): swe-057 7.1 task 1 and swe-143 7.1 task 1 (07 section 2.1.1 row Design, WP-PDR-32); swe-134 7.1 task 3 (07 section 9.7); swe-087 7.1 task 2 and swe-088 7.1 task 2 (07 section 10.2); swe-088 7.1 task 1 (paired record not filed, 07 section 10.2, X-2)
SWE-134 ITEMS CHECKED: a, b, c, e, f, g, h, i, j, k, l
MEASUREMENTS: size=1 note, 2 scripts, 1 render, 4 runs; tasks=29; tasks_no=10; turns=62; minutes=130; major=2; minor=6
```

## Delta iteration 2 (2026-09-29; revision 1 at fb120d2)

**Product.** `docs/design/analysis/sequencer-timing.md` revision 1, blob `e4c9ad92`, with `seq_run.py` (`fbcad585`), `relay_model.py` (`0285c9c9`), `timing-diagram.png` (`2b0f7678`), `expected_states.json` (`2b730325`), the README (`f29da6c8`) and the four run folders `2026-09-29-r1-s1-drive` to `-r1-s4-sequence`. They were committed at `8ca7d05`, and `fb120d2` added the run-folder copy of the render (rule C2, re-freeze F0). Each of the 42 files equals `git rev-parse fb120d2:<path>`, `HEAD:<path>` at HEAD `9edebee` and `git hash-object <path>`. `fb120d2` is on main, and no later commit touches the product, `docs/safety`, `docs/requirements`, `docs/test_cases`, TS-012 or 07. The revision 0 runs are kept unchanged as the record of revision 0. **Paired record:** the file review's delta runs concurrently and is not filed at HEAD `9edebee` (X-2).

**Scope (rule C1).** This delta verifies the fixes of finding-1 and finding-2, the two Major findings. It also checks what those fixes change, under the assurance lens:
- the D-5 recommendation, now option E (a 6.3 V hardware coil-supply limiter, an AO3400A on a static TR_DRV level, no PWM);
- TR_DRV as the input of the K12 backstop and of the PA-path gate, and the 30 ms re-arm qualification;
- the option E failure-mode table (note section 4.9);
- the moved relay timing (KD-12, KU-07) against the software prerequisites that depend on it;
- the stale-ratio firmware rule (section 4.8), where it gives SW-TXSEQ and SW-SAFE new behaviour.

Iteration 1's Minor findings (finding-3 to finding-8) are not re-reviewed. Their state is recorded below, and a Minor finding whose facts the fix changed is re-stated as a new finding.

**Acceptance criteria (rule C7).**

finding-1 is Verified when all of the following hold:
- (1a) the signal that K12 and the PA-path gate watch is named;
- (1b) that signal is one continuous "transmit" level through the whole over (pull-in, hold and hang), and returns to receive only at KU-06 or FP-03, as shown in s4 and carried as an ICD-TX-SW row;
- (1c) no TR_DRV pattern that leaves the relay in transmit can restart the backstop count;
- (1d) the result is routed to WP-PDR-26, 16, 22, 37 and 43;
- (1e) the fix opens no new Major gap.

finding-2 is Verified when all of the following hold:
- (2a) every firmware-set coil-drive parameter (the duty from a pack reading, the PWM set-up, the pull-in timer) is either removed or given an integrity provision;
- (2b) the coil voltage stays under the maximum in every firmware state;
- (2c) the key-down hold is guaranteed by the datasheet without a firmware reading;
- (2d) the remaining causes are named with their detection (REQ-SYS-156) and routed to WP-PDR-16;
- (2e) the fix opens no new Major gap.

**Independence (rule C4; 07 section 2.1).** This invocation authored no part of WP-PDR-23a, is not the file reviewer, and is not the iteration 1 assurance reviewer. It edited no product file and made no commit. The numbers below marked as reviewer results are this reviewer's own.

**Search first (charter section 11 rule 1; rule C3).** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search. Queries:
- the WP-PDR-23a sequencer timing software assurance review record;
- the sequencer SA pair, iteration 1, the hold PWM and the K12 backstop;
- the RF level with TX_KEY high and the envelope reference clamped before the ramp.

`grep`, `sed -n` and Python reads of `hazards.json`, `requirements.json`, `test_cases.json` and the run JSON were used afterwards only to pin lines and values. No rustos file was read.

### Commands run by the assurance reviewer (iteration 2 evidence)

- **Blob identity.** For the 42 product files, `git rev-parse fb120d2:<path>`, `HEAD:<path>` and `git hash-object` are equal (42 of 42). `md5` of `seq_run.py` and `relay_model.py` in the four r1 `scripts/` folders equals the working copies. `cmp` of `docs/reviews/PDR/figures/timing-diagram.png` against the r1-s4 copy: equal. `git diff --stat fb120d2 HEAD` on the product paths, `docs/safety`, `docs/requirements`, `docs/test_cases`, TS-012, 07 and `docs/reviews/PDR/figures` is empty.
- **Raw file.** `shasum -a 256` of the untracked `r1-s2-coil/coil_tran.raw` (8,013,112 bytes) gives `f8f577f6...c3f67e9d`, equal to the committed `raw.sha256` (CR-017 C2). `r1-s1-drive/drive_dc.raw` (579,766 bytes) is committed.
- **Independent re-run.** A detached worktree at `fb120d2` was made in the scratchpad, and there `.venv/bin/python hardware/sim/tx-seq/seq_run.py all --expect` exited 0. All 15 checks pass, and the 40 verdicts equal `expected_states.json` and note section 5. LTspice ran only through `tools/ltspice-batch.sh` (batch result PASS, "LTspice 26.0.2 for MacOS", LTspice exit 0, deck sha256 equal to the committed provenance). The batch waited for another invocation's LTspice lock, then ran. `git status` after the run:
  - the s3 and s4 outputs (including `runs.json` and both timing tables), all ten PNGs of the four run folders and the regenerated `docs/reviews/PDR/figures/timing-diagram.png`: byte-identical to `fb120d2`;
  - s1 and s2 `result.json` differ only in the batch provenance lines (lock wait, output directory) and in the `.raw` SHA-256, because the `.raw` carries its run date;
  - the `.log` files differ only in paths and times.

  The main working tree was not touched, and the worktree was restored afterwards.
- **Commit and repository checks.**
  - `tools/check_commit_msg.py --range 8ca7d05~1..fb120d2`: PASS for both commits (Refs REQ-SYS-160, 161, 180, 156, 036, 114, HZ-004, HZ-008, HZ-014, TS-012, WP-PDR-23a).
  - `git show --stat 8ca7d05`: only WP-PDR-23a files; no requirement, hazard, ICD, test-case or trade-study file is edited (plan section 5.3).
  - `tools/traceability.py --report-only --output <scratch>`: 245 requirements, 173 test cases, 0 violations, 2 warnings (REQ-SYS-125 and 148 SYS_UNALLOCATED, not ids of this product).
  - `tools/validate_docs.py`: 121 passed, 0 failed.
  - This whole record text, placed at its path in a scratch worktree at HEAD `9edebee`, passes `tools/validate_docs.py` there.
- **Reviewer script `sa23a_it2.py`** (scratchpad). It reads the committed r1-s3 `result.json` and `runs.json` and the r1-s4 `result.json`. Render `sa23a-it2-checks.png`, opened and inspected:
  - **Panel (a): the key-down hold (K15-E) against the drain-feed resistance at 2 A.** The hold is 1.051 x (steep slope) and 1.079 x (shallow slope) at the note's 0.45 ohm, equal to K15-E. The guarantee is lost at 0.578 ohm (steep) or 0.642 ohm (shallow), against the TS-012 budget of 0.26 to 0.45 ohm and its order check of at most 0.35 ohm.
  - **Panel (b): TR_DRV low to the TX (NO) contact starting to open**, for option E's three holds at -10, 23 and 85 C, 13 accepted sets and 3 slopes, freewheel diode. The minimum is 0.215 ms (5.25 V key-down hold, 85 C coil, set `tau0.6_rho2_sig2`, slope 0.535 %/K). The note's section 4.9 basis, the fastest no-diode release to rest, is 1.13 ms (finding-10).
  - **Panel (c): the TR_DRV-low axis.** It shows the option E release maximum plus NC bounce (25.36 ms from TR_DRV low), KU-07 (25.86 ms from t_h, the K21-E basis) and the limiter pass-element short case: 27.80 ms at 8.40 V and -10 C, 28.80 ms with ordering and bounce, where the note gives 28.67 (finding-13). It also shows BM-3 (29.0 ms), T_rearm (30 ms) and the shortest hang (72 ms) (finding-11).
- **Hand checks against the note.**
  - K19-E: 6.3 V x 1.02 = 6.426 V, 128.5 % of 5 V, against 151 % at 70 C.
  - K15-E: worst-unit must-operate at 85 C is 3.75 V x (1 + 0.005347 x 62) = 4.993 V (steep) or 4.866 V (shallow); 5.25 / 4.993 = 1.051 and 5.25 / 4.866 = 1.079.
  - K22-CD: with D = 5.0 / (V_read - 0.9) and 0.9 V of sag, the hold ratio 1.028 is lost when 6.35 x e / 5.45 = 0.028, that is at a reading 2.4 % high; the ratio 1.001 at 0.09 %. This agrees with the note's "0.1 to 2.4 %".
  - K21-E: T_rearm 30 ms against 0.5 + 24.86 + 0.5 = 25.86 ms.
- **Figures opened and inspected before citing:**
  - `timing-diagram.png`: panel (a) shows the option E contact band ending at t0 + 8.39 ms, to the right of both the PA_EN edge (t0 + 7.5) and the TX_KEY edge (t0 + 8.0) (finding-9). Panel (b) shows TR_DRV as one level from t0 to the hang expiry;
  - `s1-coil-voltage-vs-pack.png`: E at 126 % nominal, 128.5 % at the tolerance top, flat above 6.5 V; C and D reach 168 % at 8.4 V against 167, 156 and 151 %;
  - `s1-coil-current.png`: the legend runs slightly past the right-hand plot edge, the defect the author reports; readable;
  - `s2-coil-transient.png`, with the E_rise_hot and E_dc_cold panels;
  - `s4-margins.png`: unchanged in content from revision 0 (bounce limits 1.957 and 0.9 ms; key-up margin above 52 ms at 50 WPM);
  - `s3-operate-vs-coil-temperature.png`, `s3-release.png` and `s3-limiter-setpoint.png`;
  - `s4-keydown-budget.png` (no relay-settle bar; see finding-9) and `s4-stale-ratio.png`: in panel (a) the not-radiated elements carry no TR_DRV, PA_EN or TX_KEY, and TR_DRV, PA_EN and TX_KEY rise at the first element after the 82.8 ms refresh;
  - the reviewer's `sa23a-it2-checks.png`.

### Verification of finding-1 (Major)

| Criterion | Result | Evidence |
|---|---|---|
| (1a) Watched signal named | Met | Note section 4.9: the K12 backstop (HZ-004 K12, HZ-014 K8, REQ-SYS-180) and the PA-path gate's T/R input both take the TR_DRV level. The same appears in section 6.1 item 3 and section 6.2 rows WP-PDR-22, 26 and 37 |
| (1b) One continuous transmit level, back to receive only at KU-06 or FP-03 | Met | Option E has no pull-in phase and no PWM. TR_DRV is written only at t0, KU-06 and FP-03 (section 6.2 row WP-PDR-32, 35), which gives 2 edges per over (K21-E, reproduced). ICD rows KD-04 and KD-17 ("TR_DRV stays high until KU-06"), and KU-06. `timing-diagram.png` panel (b) draws one level through a 50 WPM over and the 3-dit hang. The stale-ratio outcome keeps TR_DRV low for the not-radiated elements (SR-02) |
| (1c) No TR_DRV pattern that keeps the relay in transmit restarts the count | Met, with Minor liens | The backstop is level-triggered and re-arms only after TR_DRV has been low for at least T_rearm = 30 ms. That is longer than the slowest option E release, 25.86 ms from t_h (K21-E). A 25 kHz or any other PWM put on TR_DRV by a pin-map error (the HZ-014 C5 class) no longer restarts the count, which is stronger than the revision 0 text of K12. The re-arm rationale is misstated and does not match REQ-SYS-180's definition of continuous transmit (finding-11). The limiter-short release is quoted from no run (finding-13). Neither lets a fault that keeps the relay in transmit re-arm the backstop |
| (1d) Routed | Met | Section 6.2 routes to WP-PDR-26 (level trigger, 30 ms re-arm), WP-PDR-16 (the K12 text), WP-PDR-22 (the gate's T/R input), WP-PDR-37 and 38 (no PWM slice on the pin) and WP-PDR-43 (BM-7: 2 edges per over, and a 5 ms dip under RF). TC-SYS-108 and the REQ-SYS-180 rationale are not named; that gap is part of finding-11 |
| (1e) No new Major gap | Met | Finding-9 to finding-13 are Minor. None of them lets a single fault restore RF past a hardware control, and none defeats the backstop for a toggling TX_KEY stream |

### Verification of finding-2 (Major)

| Criterion | Result | Evidence |
|---|---|---|
| (2a) Firmware-set coil parameters removed or protected | Met | Option E removes all three. The firmware only switches TR_DRV, and the coil voltage is set by the limiter's set point, fixed in hardware (section 6.1 items 2 and 3; K22-E). Options C and D, which keep them, are rejected (K22-CD FAIL, reproduced: a reading 0.09 to 2.4 % high loses the hold) |
| (2b) Coil voltage under the maximum in every firmware state | Met | At most 6.426 V, 128.5 %, peak equal to average, against 151 % at 70 C (K19-E). This holds with TR_DRV high for any time, because no firmware state raises the limiter output |
| (2c) Key-down hold guaranteed without a reading | Met | 1.051 to 1.079 x at 5.25 V with the limiter in dropout at the 5.45 V key-down rail (K15-E, reproduced by hand). The hold rests on the TS-012 feed-budget estimate, not on a firmware value. Reviewer panel (a): the guarantee holds up to 0.578 ohm of feed resistance, 0.128 ohm above the budget's top. The same estimate already sets REQ-SYS-012 (TS-012 section 7.3), and BM-6 measures the limiter at 5.45 V |
| (2d) Remaining causes named with detection and routed | Met | Section 4.9 lists single faults of the limiter, the driver, the coil, the diode and TR_DRV. It names a new HZ-008 cause, "T/R contact open or reopened under RF by a relay coil supply fault", with REQ-SYS-156 as the detection (Fault-safe within 100 ms (TBR)) and D-9 as the bound. This goes to WP-PDR-16, and the sizing of the VGG step to WP-PDR-22. No firmware-set cause remains, so none is added |
| (2e) No new Major gap | Met | The hold no longer depends on software. The residual hazard, a hardware coil-supply fault under RF, is the same kind of fault as the revision 0 late contact. It has the same detection and the same bound |

**SWE-080 and SWE-205 view of the change.** Option E moves a safety function from firmware to hardware: the coil-voltage bound and the hold. It also removes three software contributions (a wrong duty, a wrong PWM set-up, a pull-in that never ends). For the software products:
- **Pin map and ICD-TX-SW.** TR_DRV stays one GPIO. It is now a plain level with a pull-down, with no PWM slice. It fans out to the relay driver, the backstop and the PA-path gate.
- **SW-TXSEQ.** Its obligations shrink: it no longer computes a duty and runs no timer. Revision 1 adds two obligations: TR_DRV is written only at t0, KU-06 and FP-03, and the stale-ratio rule applies.
- **SW-SAFE.** It keeps "no PA_EN on a ratio older than A_kd" (R-FRESH-2). SW-TXSEQ's own rule, "no changeover while the ratio is aged", sits in front of it. The two are dissimilar checks on one condition, and a failure of the SW-TXSEQ rule ends in a T/R change with no PA_EN, which is safe.
- **TS-012 firmware-scope text.** It still says "coil held by PWM" (finding-12).

### State of the iteration 1 Minor findings

| Finding | State at iteration 2 | Note |
|---|---|---|
| finding-3 | Open (lien) | Not addressed (rule C1). Revision 1 moved KD-12 past TX_KEY, so its consequence argument no longer holds: finding-9 |
| finding-4 | Open (lien), partly mitigated | With the gate's T/R input on TR_DRV (requested from WP-PDR-22), a TR_DRV fall acts on the PA path in hardware, including on the reset path where the pads release together. The basis quoted for it is the wrong event: finding-10 |
| finding-5 | Open (lien) | Not addressed; unchanged |
| finding-6 | Open (lien), partly addressed | Section 6.1 item 3 now names "a pull-down so that reset and bootrom read off" on the driver gate. Its value against the RP2350-E9 guidance (8.2 kohm or less), the KD-04 row, and the HZ-004 K6 and HZ-014 K3 wording for WP-PDR-16 are not given |
| finding-7 | Open (lien) | Not addressed; unchanged |
| finding-8 | Open (lien) | Not addressed. `relay_model.py` was revised (slope law, force scale) and still has no TV record. The D-5 choice between options B and E now rests on it more heavily (operate times, K1b-E margin 1.11 ms) |

### Findings (iteration 2)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-9"></a>finding-9 | assurance | Minor | swe-134 7.1 task 1; swe-058 7.1 task 1; SA-C-h | Note section 4.1 rows "'T/R in TX and settled' true (7 + 0.5 ms) 7.5", "TX_KEY high 8.0", "relay contacts made and bounce ended, option E worst case (r1) 8.39"; section 8 rows KD-10 (7.5), KD-11 (7.5 to 8.0), KD-12 (max 8.388), KD-13 (8.0); `timing-diagram.png` panel (a) | **With the slope band of revision 1, the recommended option's worst-case contact settle comes after both RF conditions are set.** The 07 section 14.2 row h prerequisite "T/R in TX and settled" is a 7.5 ms timer. KD-12 for option E now ends at t0 + 8.388 ms. In that corner, PA_EN rises 0.89 ms before the contacts have settled. TX_KEY then powers the GVA-84+ and releases the D-18 VGG clamp 0.39 ms before they settle. The consequence is small. With the driver powered and VGG at 0 V, the level at the PA output is -14.7 to -16 dBm (L1) or about -10 dBm (L4) (`pa-permit-gate-d18.md` section 5.3), at least 47 dB under the 5 W carrier. So 07 row b's "below -20 dBc" is met, and the ramp at t0 + 10.0 ms starts 1.61 ms after the latest settle. That is why this finding is Minor. It replaces the consequence argument of finding-3 ("TX_KEY at t0 + 8.0 ms is after 7.61 ms"), which revision 1 made untrue. Finding-3's fix, a settle time of at least KD-12 max, now reaches t0 + 8.39 ms or more (BM-2 accepts up to 8.5 ms). That conflicts with TX_KEY at 8.0 ms and with K6 (PA_EN before TX_KEY). Fix: state the resolution in section 4.1 and the timing table. One way is to delay the first element's TX_KEY until PA_EN, for example PA_EN and TX_KEY at t0 + 8.5 ms: a 1.5 ms TX_KEY lead, the driver settled by 9.5 ms (K7), and a relock margin of 1.40 ms; WP-PDR-22 would confirm that the keying loop accepts the shorter lead. The other way is to keep the 2 ms lead and say that the row h timer does not mean the contacts have settled, with the backwave argument above. Add the criterion t_settle >= KD-12 max, or its stated exception, to s4 | Open | Pending | |
| <a id="finding-10"></a>finding-10 | assurance | Minor | swe-134 7.1 task 1; swe-058 7.1 task 4; SA-C-c | Note section 4.9, K21 paragraph: "A TR_DRV low then removes the PA output within the gate's microseconds, well before the contacts can open (the fastest no-diode release in the band is 1.13 ms)"; failure-mode row "TR_DRV (firmware) a dip or pulse inside an over"; section 9 BM-7; section 8 rows FP-02 (0.1 ms, class E) and FP-03 | **The cold-switching claim for a TR_DRV dip under RF cites the wrong event, and the number that applies is 5 times smaller.** 1.13 ms is the fastest release to rest with no freewheel path, the datasheet anchor. The event that matters is the NO (transmit) contact starting to open with the freewheel diode fitted. In the committed r1-s3 `runs.json` that happens from 0.215 ms after TR_DRV low (option E key-down hold 5.25 V, 85 C coil, set `tau0.6_rho2_sig2`, steep slope; reviewer panel (b)). The claim still holds for the carrier. The D-18 clamp takes VGG down and the driver supply falls below 3.1 V within about 20 us, so at 0.215 ms the level is at most the backwave, below 07 row b's -20 dBc. It does not hold for the RF-off level: in the D-18 run the driver supply falls below 0.1 V 0.77 to 0.78 ms after TX_KEY falls (`pa-permit-gate-d18.md` section 5.3). FP-02's 0.1 ms (class E) is therefore not consistent with the D-18 run. Fix: in section 4.9 and in the WP-PDR-22 request, quote the NO-opening minimum (0.215 ms) against the gate's measured times from `pa-permit-gate-d18.md`, and state the result as "carrier removed before the contact opens; RF-off level reached later". Correct FP-02 or give its basis. Make the BM-7 acceptance a capture of pole A against the RF-present indicator. This also gives finding-4 its missing number | Open | Pending | |
| <a id="finding-11"></a>finding-11 | assurance | Minor | swe-134 7.1 tasks 1 and 6; swe-205 7.1 task 5; SA-C-i; SA-D6 | Note section 4.9: "It is shorter than every hang (72 ms or more) and than the release margin, so a real return to receive always re-arms it"; `seq_run.py` INPUTS `t_rearm`; section 6.2 rows WP-PDR-26 and WP-PDR-16; REQ-SYS-180 rationale ("Continuous transmit: the T/R drive held in transmit, with no pause longer than the hang time (REQ-SYS-044)"); TC-SYS-108 (no TR_DRV-dip case) | **The 30 ms re-arm qualification is sound in the direction the note needs, but its stated rationale is wrong, and it does not match the requirement's definition of continuous transmit.** (a) Whether K12 re-arms depends on how long TR_DRV stays low after KU-06. That is the operator's gap before the next key-down, not the hang. An operator who keys again within 30 ms of KU-06 gets no re-arm, so the count runs on across both overs, and the backstop can end a legitimate over early. This can happen even though the relay may already have released (option E end-of-over release: nominal set 8.6 to 8.8 ms at 23 C, fastest accepted set 3.2 ms at 85 C). So "a real return to receive always re-arms it" is not true. The effect is on availability, on the safe side. (b) Under a firmware fault, a TR_DRV low of 30 to 72 ms re-arms K12, although REQ-SYS-180's rationale still calls that transmission continuous (no pause longer than the hang). TC-SYS-108 has no TR_DRV-dip case. With the requested gate input, RF is removed during every dip, so the exposure is limited by the duty of the dips, and the finding is Minor. Fix: correct the sentence. State the basis of T_rearm's range: the lower bound is the slowest release a single fault leaves (the limiter-short case, 28.80 ms, finding-13). Any upper bound trades false trips on a quick re-key against the dip length a fault can use to re-arm. Route to WP-PDR-16 and the REQ-SYS-180 writer a definition of continuous transmit that the hardware can observe ("TR_DRV not low for T_rearm or longer"). Route to WP-PDR-43 TC-SYS-108 cases for a TR_DRV dip just under and just over T_rearm | Open | Pending | |
| <a id="finding-12"></a>finding-12 | assurance | Minor | swe-134 7.1 task 6; swe-205 7.1 task 5; SA-D6 | Note section 6.2 row WP-PDR-54, which names 7.3, D-5, rows 2, 12 and 22 of 8.3, the limiter row and the section 8.1 block-diagram label. Not named: TS-012 section 8.7, paragraph "Firmware scope added (WP-PDR-35, 41)", which reads "transmit sequencing (relay, ...; the relay coil held by PWM after pull-in, D-5)" (line 815 at HEAD), and TS-012 section 8.12 row WP-PDR-23, "its coil held by PWM after pull-in or the high-sensitivity coil (D-5)" (line 991) | **The TS-012 text that sets the firmware scope still tells WP-PDR-35 and 41 to put a hold PWM on the relay drive.** Revision 1's request to WP-PDR-54 does not include it. Finding-1 is fixed only if no PWM ever reaches TR_DRV: section 6.2 asks WP-PDR-32 and 35 for "never a PWM slice", and K21-E depends on it. Until the scope paragraph changes, the firmware authors have two contradicting sources. X-3 of iteration 1 flagged the same risk for the D-5 first option. Fix: add both TS-012 passages to the WP-PDR-54 request, with the section 6.1 wording | Open | Pending | |
| <a id="finding-13"></a>finding-13 | assurance | Minor | swe-058 7.1 task 1; SA-C-i | Note section 4.9 failure-mode row "Limiter, pass element short": "release at -10 C from 8.4 V 27.67 ms, 28.67 ms with ordering and bounce (still inside 30)"; K21-E (compares T_rearm only with the option E limiter corners) | **The slowest release a single fault leaves is quoted from no run output, and K21-E does not include it.** The committed r1-s3 results give 27.80 ms for an 8.40 V hold at -10 C (`result.md` rows C, D full cold; `runs.json` maximum 27.803 ms, set `tau2.4_rho4_sig0.5`). With ordering and bounce that is 28.80 ms, not 28.67 ms. The margin to T_rearm and to the 30 ms share is 1.20 ms, not 1.33 ms. Nothing changes state, so the finding is Minor. But this is the case T_rearm must exceed if a latent limiter short is not to let a TR_DRV dip re-arm the backstop with the contacts still in transmit. Fix: take the figure from the run, or add the E pass-short hold to s3 as a run output. Include it in K21-E's comparison and in the finding-11 range | Open | Pending | |

No Major finding is open: `assurance_verdict` APPROVED at iteration 2 (07 section 10.2; rule C1). Finding-3 to finding-13 are Minor liens, due at the CDR readiness declaration unless the author closes them earlier.

**What else was checked and holds (assurance lens):**
- **K19 and the reading of "maximum voltage".** The reading of ratings note 3 and the graph note as a limit on the imposed (peak) voltage is the conservative one for firmware. With it, no duty or timer value can make a pack-fed PWM compliant. So the decision does not rest on a firmware parameter (`s1-coil-voltage-vs-pack.png`).
- **The option E failure-mode table.** It covers the limiter (output low or open, high dropout, pass short), the driver short, open driver, coil or diode, the open diode, and a TR_DRV dip. Each has an effect, a detection or bound, and a destination. The AO3400A drain-source short leaves TR_DRV low, so the gate holds the PA path off and K12 stays unarmed. That is correct, with no RF because PA_EN and TX_KEY stay low.
- **The stale-ratio rule.** Outcome (b), the rule in section 4.8, keeps REQ-SYS-120 and REQ-SYS-182 in both SW-TXSEQ and SW-SAFE. Its HostUnit cases include both sides of A_kd and a closure held across the refresh end. The REQ-SYS-160 effect (K20-c) goes to the owner only after this record and its pair are APPROVED (rule C10).
- **K12-E and KU-07.** The release is now run at -10, 23 and 85 C from every hold. The worst case is 25.86 ms at -10 C, against the 30 ms share. BM-3's 29.0 ms acceptance sits inside T_rearm.
- **Option B remains the fallback** (section 6.1 item 8) only with bench measurements BM-1 to BM-3. It keeps a static TR_DRV, so K21 does not depend on the coil choice.

### Task table (iteration 2, delta)

| Task | Safety-critical designation (SWEHB 8.10 section 6) | Applied | Result and evidence | Relief (N/A only) | Finding ids |
|---|---|---|---|---|---|
| swe-134 7.1 task 5 (every type) | SC | Yes | This record is the assurance participation in the delta review of a product that sets `SW-TXSEQ` and `SW-SAFE` design values | | none |
| swe-087 7.1 task 2, swe-088 7.1 task 2 | | Yes | Both Major fixes verified against criteria (1a) to (1e) and (2a) to (2e), with reviewer re-runs. The Minor liens' states are recorded | | none |
| swe-057 7.1 task 2 (design) | | Yes | TR_DRV no longer carries a waveform that defeats the independent backstop; the D-5 purpose (coil power at most 0.22 W at 85 C) is met in hardware | | none |
| swe-058 7.1 task 1 (design) | | No | The row h settle timer disagrees with the moved KD-12 (finding-9). The limiter-short release figure is not from a run (finding-13) | | finding-9, finding-13 |
| swe-058 7.1 task 3 (design) | | Yes | The undesired behaviours of iteration 1 (a firmware duty or configuration fault drops the relay; a stuck pull-in overdrives it) are removed by design (K22-E) | | none |
| swe-058 7.1 task 4 (design) | SC | Yes | Cold switching on a TR_DRV dip holds for the carrier (below 07 row b's -20 dBc at the NO-contact opening). Its quoted basis is corrected by finding-10 | | finding-10 |
| swe-058 7.1 task 5 (design) | | Yes | Reviewer design analysis: the feed-resistance margin of K15-E, the NO-contact opening over the band, the TR_DRV-low axis, and hand checks of K15-E, K19-E, K21-E and K22-CD (Commands) | | finding-10, finding-11, finding-13 |
| swe-134 7.1 task 1 (design) | SC | No | Items h, c and i carry Minor gaps (section C below) | | finding-9, finding-10, finding-11 |
| swe-134 7.1 task 4 (design) | SC | Yes | The hold duty, the safety datum of iteration 1 that had no protection, no longer exists. The ratio age that the stale-ratio rule reads is checked twice, by SW-TXSEQ and by SW-SAFE | | none |
| swe-134 7.1 task 6 (design) | SC | No | The design no longer disagrees with HZ-004 K12 in substance. The REQ-SYS-180 definition and TC-SYS-108 are not routed (finding-11), and the TS-012 firmware-scope text still says PWM (finding-12) | | finding-11, finding-12 |
| swe-205 7.1 task 1 | SC | Yes | Software contributions of the recommended design: the duty, PWM and timer causes are removed, TR_DRV writes are limited to t0, KU-06 and FP-03, and the stale-ratio rule is set. Hardware causes are routed to WP-PDR-16 with REQ-SYS-156 named | | none |
| swe-205 7.1 task 5 | SC | No | The design needs of the safety analysis are mostly requested (section 6.2). Missing: the REQ-SYS-180 and TC-SYS-108 updates (finding-11), and the TS-012 scope text (finding-12) | | finding-11, finding-12 |
| swe-136 7.1 task 1 (tool) | | Yes | LTspice 26.0.2 only through `tools/ltspice-batch.sh` (ACC-LTSPICE-001, TV-014); provenance lines in the s1 and s2 `result.json` | | none |
| swe-192 7.1 task 1 | SC | Yes | R3 re-run: 0 violations. The note claims no closure | | none |
| swe-089 7.1 task 1 | | Yes | Section F measurements below | | none |
| swe-081 7.1 task 2 | SC | Yes | The product is committed on main at `8ca7d05` and `fb120d2`. The only raw file above 5,000,000 bytes is kept untracked with a matching `raw.sha256` (CR-017 C2) | | none |
| swe-070 7.1 task 1 (models) | | Not re-applied | finding-8 stays Open | | finding-8 |

### SWE-134 items (iteration 2)

| Id | Answer | Evidence |
|---|---|---|
| SA-C-a | No | The TR_DRV pull-down is now named (section 6.1 item 3), but its value and the K6 and K3 routing are not given (finding-6, partly addressed) |
| SA-C-b | Yes | Key-down and key-up orders are unchanged; TR_DRV is one level; the key-up is cold (K10) |
| SA-C-c | No | The fault path and a TR_DRV dip are cold for the carrier, with the new gate input. The quoted basis is the wrong event, and FP-02 disagrees with the D-18 run (finding-10; finding-4) |
| SA-C-f | Yes | No firmware-set coil-drive datum remains (K22-E) |
| SA-C-g | Yes | The relay hold and the coil voltage no longer depend on any software input or output. The ratio age is checked in two components |
| SA-C-h | No | The "T/R in TX and settled" timer (7.5 ms) precedes KD-12 max (8.39 ms), and TX_KEY (8.0 ms) does too (finding-9) |
| SA-C-i | No | Finding-1 and finding-2 are Verified. One residual Minor gap remains: the re-arm rationale and the REQ-SYS-180 definition (finding-11). REQ-SYS-120's two conditions are kept |
| SA-C-j | Yes | K12-E 25.86 ms against the 30 ms share, from -10 to 85 C; K16 unchanged at 1.1 ms |

### Readiness (iteration 2)

| # | Result | Evidence |
|---|---|---|
| R1 | Yes (own part) | 42 of 42 blobs equal at `fb120d2`, at HEAD `9edebee` and in the working tree. The paired record's list is checked at filing (X-2) |
| R2 | Yes | `design`, safety-critical, unchanged from iteration 1 |
| R3 | Yes | validate_docs 121 passed; traceability 0 violations; this record text validates at its path |
| R4 | Yes (in progress) | The file review's delta runs under its own invocation. This invocation is neither the author, nor that reviewer, nor the iteration 1 assurance reviewer |

### D, E and F (iteration 2)

| Id | Answer | Evidence |
|---|---|---|
| SA-D1 | Yes | SWEHB `swe-205` section 7.7.2, re-walked for the change. **Control of safety-critical hardware:** the relay hold is now in hardware. **Interlocks:** K12 is level-triggered with a re-arm qualification (finding-11 Minor). **Common cause:** TR_DRV feeds the driver, K12 and the gate. A stuck-high TR_DRV makes K12 count and expire. A stuck-low TR_DRV keeps receive and blocks the PA path. Neither is unsafe. **Timing:** finding-9 and finding-10 |
| SA-D6 | No | Hazard and requirement text updates are requested except REQ-SYS-180, TC-SYS-108 and the TS-012 scope text (finding-11, finding-12) |
| SA-E1 | Yes | The two Major findings are verified with evidence; no finding is closed without evidence; the Minor liens stay Open |
| SA-E3 | Yes | `8ca7d05` and `fb120d2` edit only WP-PDR-23a files; check_commit_msg PASS; CR-017 C2 kept |
| SA-F2 | Yes | Front matter: `assurance_findings_major` 2 (both Verified), `assurance_findings_minor` 11, `items_no`, effort |

### Cross items for the software lead (iteration 2)

- **X-2 (open).** Neither the paired file review record nor its delta is filed at HEAD `9edebee`. At filing, the software lead writes its id into `paired_record` here, transcribes this pairing and `assurance_verdict` APPROVED into it, and checks SA-A3 and SA-A4 there.
- **X-5 (new).** Id collision. The returned texts of this record and of the WP-PDR-22 D-18 software assurance pair both propose INSP-123. Three returned file-review texts propose INSP-122: the D-18 file review, the thermal-budget file review, and this record's pair. The lead SE assigns distinct ids at filing and updates `paired_record` in each pair.
- **X-6 (new).** The option E limiter adds a part, a quiescent current and up to 0.11 W of dissipation. These reach WP-PDR-24 (power budget), WP-PDR-28 (thermal; `thermal-budget.md` at HEAD still describes the D-5 PWM hold) and the TS-012 ordering-gate cost. They are routed in note section 6.1 items 2, 6 and 7, and are not assurance findings.

### Measurements (SWE-089, iteration 2)

Tasks in the iteration 2 table: 17 rows (16 applied Yes or No, 1 not re-applied); tasks answered No: 4. Section items checked: 19 (R1 to R4, SA-C-a, b, c, f, g, h, i, j, SA-D1, D6, E1, E3, F2, and the two verification tables); answered No: 6. Findings: iteration 2 adds 5 Minor; the 2 Major of iteration 1 are Verified; 6 iteration 1 Minor stay Open (2 partly addressed). Effort: 48 turns, about 80 minutes. Renders inspected: 11 (10 of the product, the render counted once, and 1 reviewer). Reviewer re-runs: s1 to s4 with `--expect`, 15 of 15 checks, 40 of 40 verdicts; data byte-identical. One reviewer script (3 checks, 1 render).

### Verdict format (iteration 2)

```
ASSURANCE VERDICT: APPROVED (iteration 2, delta)
PRODUCT: docs/design/analysis/sequencer-timing.md@e4c9ad92, docs/reviews/PDR/figures/timing-diagram.png@2b0f7678, hardware/sim/tx-seq/seq_run.py@fbcad585, hardware/sim/tx-seq/relay_model.py@0285c9c9 at fb120d2 (runs 2026-09-29-r1-s1 to s4); PAIRED RECORD: pending (analysis-sequencer-timing.md, not filed)
PRODUCT TYPE: design (routed by PDR work plan WP-PDR-23; X-1); CRITICALITY: safety-critical
FINDINGS:
- [Major] finding-1 Verified: TR_DRV is one static level per over (2 edges); K12 level-triggered with a 30 ms re-arm qualification above the 25.86 ms release; gate T/R input on TR_DRV; routed to WP-PDR-16, 22, 26, 37, 43.
- [Major] finding-2 Verified: option E removes every firmware-set coil-drive parameter; coil at most 128.5 % in any firmware state; key-down hold 1.051 x with no reading; hardware causes routed to WP-PDR-16 with REQ-SYS-156 as detection.
- [Minor] finding-9 swe-134 7.1 task 1 (SA-C-h) option E contacts settle at t0 + 8.39 ms, after PA_EN (7.5) and TX_KEY (8.0); backwave only, but the row h timer and finding-3's fix now conflict with the TX_KEY lead.
- [Minor] finding-10 swe-134 7.1 task 1 (SA-C-c) the TR_DRV-dip cold-switching claim cites the 1.13 ms release; the NO contact opens from 0.215 ms; RF-off level at 0.77 ms, not FP-02's 0.1 ms.
- [Minor] finding-11 swe-134 7.1 task 6 (SA-C-i) the T_rearm rationale ("a real return to receive always re-arms it") is wrong, and REQ-SYS-180's continuous-transmit definition and TC-SYS-108 are not reconciled.
- [Minor] finding-12 swe-205 7.1 task 5 (SA-D6) TS-012 section 8.7 firmware scope and section 8.12 row WP-PDR-23 still say "coil held by PWM"; not in the WP-PDR-54 request.
- [Minor] finding-13 swe-058 7.1 task 1 the limiter-short release is 28.80 ms by the run, not 28.67; not in K21-E.
- finding-3 to finding-8 (Minor, iteration 1): Open liens; finding-6 and finding-4 partly addressed.
TASKS APPLIED: swe-134 7.1 tasks 1, 4, 5, 6; swe-057 7.1 task 2; swe-058 7.1 tasks 1, 3, 4, 5; swe-205 7.1 tasks 1, 5; swe-136 7.1 task 1; swe-192 7.1 task 1; swe-087 7.1 task 2; swe-088 7.1 task 2; swe-089 7.1 task 1; swe-081 7.1 task 2
TASKS N/A (relief): none at iteration 2; swe-070 7.1 task 1 not re-applied (finding-8 stays Open)
SWE-134 ITEMS CHECKED: a, b, c, f, g, h, i, j
MEASUREMENTS: tasks=17; tasks_no=4; turns=48; minutes=80; major=0 open (2 verified); minor=11 open
```

## Delta iteration 3 (2026-09-29; revision 2 at 249356b)

**Product.** `docs/design/analysis/sequencer-timing.md` revision 2, blob `b6a5e31a`, with `seq_run.py` (`d28ab4a1`), `relay_model.py` (`0285c9c9`, unchanged since revision 1), `timing-diagram.png` (`49db873d`), `expected_states.json` (`b45bc1b5`), the README (`71e0d9d9`) and the four run folders `2026-09-29-r2-s1-drive` to `-r2-s4-sequence`, all committed at `249356b` (rule C2, re-freeze F0). Each of the 43 files equals `git rev-parse 249356b:<path>`, `HEAD:<path>` (HEAD is `249356b`) and `git hash-object <path>`. The revision 1 and revision 0 runs are kept unchanged as the records of those revisions. **Paired record:** the file review's delta on revision 2 runs concurrently and is not filed at HEAD `249356b` (X-2). The paired file review numbers its own findings; its finding-13 and finding-14, which revision 2 answers, are written below as "review finding-13" and "review finding-14" so that they are not confused with this record's finding-13 and finding-14.

**Scope (rule C1).** This record had no open Major finding after iteration 2. Revision 2 fixes the two Major findings of the file review's delta iteration: review finding-13 (the option E key-down rail floor behind K15-E) and review finding-14 (the trigger of the REQ-SYS-160 stale-ratio condition). Whether those fixes are correct as analysis is the file review's question. This delta checks what they change under the assurance lens:
- whether finding-1 and finding-2 (Major, Verified at iteration 2) still meet their criteria at `249356b`;
- K15-E, now OPEN in the recommended design: the residual drop-out under RF, its detection, and its routing to the hazard data;
- the new dependence of the relay's pull-in and hold on the pack floor that REQ-SYS-097 sets, which a `SW-TXSEQ` prerequisite enforces;
- K22-E as restated;
- the stale-ratio restatement, where it touches the `SW-TXSEQ` and `SW-SAFE` rule and TC-SYS-102;
- the moved relay timing (KD-12) and the lower key-down hold against this record's own Minor liens (finding-9, finding-10);
- the two new checks as evidence.

**Acceptance criteria (rule C7).**
- (3a) finding-1 criteria (1a) to (1e) still hold at `249356b`;
- (3b) finding-2 criteria (2a) to (2e) still hold, or any change is recorded with its consequence;
- (3c) every software contribution or software dependency that revision 2 introduces is named and routed;
- (3d) the stale-ratio restatement leaves the `SW-TXSEQ` and `SW-SAFE` rule, the timing-table rows and the TC-SYS-102 set-up consistent;
- (3e) revision 2 opens no new Major gap.

**Independence (rule C4; 07 section 2.1).** This invocation authored no part of WP-PDR-23a, is not the file reviewer, and is neither the iteration 1 nor the iteration 2 assurance reviewer. It edited no product file and made no commit. Numbers marked as reviewer results are this reviewer's own.

**Search first (charter section 11 rule 1; rule C3).** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search. Queries:
- the WP-PDR-23a software assurance review record and the key-down hold K15-E;
- the low-battery transmission refusal at 3.20 V per cell measured in receive and the component that owns it.

`grep`, `sed -n` and Python reads of the run JSON, `hazards.json` and the p4 `.raw` were used afterwards only to pin lines and values. No rustos file was read.

### Commands run by the assurance reviewer (iteration 3 evidence)

- **Blob identity.** For the 43 product files, `git rev-parse 249356b:<path>`, `HEAD:<path>` and `git hash-object` are equal (43 of 43). `cmp` of `seq_run.py` and `relay_model.py` in the four r2 `scripts/` folders against the working copies: equal. `cmp` of `docs/reviews/PDR/figures/timing-diagram.png` against the r2-s4 copy: equal. `git show --stat 249356b`: 42 files, only WP-PDR-23a files; no requirement, hazard, ICD, test-case or trade-study file is edited (plan section 5.3).
- **Raw files.** `shasum -a 256` of the untracked `r2-s2-coil/coil_tran.raw` (8,010,152 bytes) gives `49905b7b...88dd73ff`, equal to the committed `raw.sha256` (CR-017 C2). The WP-PDR-21 input `2026-09-29-r3-p4-power-a5-design/power_a5_design.raw` (20,405,166 bytes) is untracked in the main working tree; its SHA-256 `886371f6...a57306` equals the `raw.sha256` committed at `f1070cf`.
- **Independent re-run, clean checkout.** A detached worktree at `249356b` was made in the scratchpad. There `.venv/bin/python hardware/sim/tx-seq/seq_run.py all --expect` exited 0 with 17 checks PASS and 40 verdicts equal to `expected_states.json` and note section 5. LTspice ran only through `tools/ltspice-batch.sh` ("LTspice 26.0.2 for MacOS"). `git status` after the run:
  - the s3 outputs (`result.json`, `result.md`, `runs.json`, four PNGs), the s4 timing tables and PNGs, and the regenerated `docs/reviews/PDR/figures/timing-diagram.png`: byte-identical to `249356b`;
  - s1 and s2 `result.json`, `.log` and `.raw` differ only in batch provenance, paths, times and the run date inside the `.raw`;
  - **s4 `result.json` differs in one block: `p4_feed_current` reads `"pass": true, "note": "p4 .raw not present: inputs used as recorded, not re-derived"`** (finding-16).
- **Re-run with the p4 `.raw` present.** The main tree's `power_a5_design.raw` was copied into the worktree (hash as above) and `seq_run.py s4 --expect` re-run: exit 0; `p4_feed_current` re-derives 2.1403 A (1,728 corners, +45 C bound), 2.2151 A (432 corners, -10 C bound) and 2.2335 A (1,728 corners, lever), each within 1 mA of the input; s4 outputs byte-identical to `249356b`. The worktree was removed afterwards; nothing in the main working tree was touched.
- **Commit and repository checks.**
  - `tools/check_commit_msg.py --range 249356b~1..249356b`: PASS (Refs REQ-SYS-097, 160, 156, 012, TC-SYS-102, TS-012, WP-PDR-23a, WP-PDR-21).
  - `tools/traceability.py --report-only --output <scratch>`: 245 requirements, 173 test cases, 0 violations, 2 warnings (REQ-SYS-125 and 148 SYS_UNALLOCATED, not ids of this product).
  - `tools/validate_docs.py` at HEAD: 123 passed, 0 failed. This whole record text, placed at its path in the scratch worktree, passes `tools/validate_docs.py` there (124 passed, 0 failed; see also X-9).
- **Reviewer script `sa23a_it3.py`** (scratchpad; imports the frozen `seq_run.py` and `relay_model.py` unchanged; reads the r2-s1 driver fits and the p4 `.raw`). Render `sa23a-it3-checks.png`, opened and inspected:
  - **Panel (a): K1b-E against the pack at the start of a transmission.** Worst operate time plus 0.5 ms bounce at an 85 C coil over the 13 accepted H1 sets and both design slopes, with the coil fed min(6.174 V, pack less 0.146 A x 0.614 ohm less the 0.10 V dropout). At 6.30 V: 8.567 ms, equal to the note. The worst case reaches the ramp at t0 + 10 ms at a pack of **6.075 V**. Above about 6.36 V the limiter regulates and the curve is flat at 8.29 ms.
  - **Panel (b): K15-E against the pack floor** (closed form, 85 C coil, 0.10 V discharge, 0.10 V dropout). At 6.30 V: 0.9797 and 1.0053 x with the feed bound, 1.0499 and 1.0773 x with the lever, equal to the note. The ratio reaches 1.0 at a pack of **6.401 V** (steep slope) and 6.274 V (shallow) with the feed bound, and at **6.051 V** (steep) and 5.924 V (shallow) with the lever.
  - **Panel (c): the p4 key-down current against the pack**, maximum over each feed-bound group. The current rises with the pack from 6.4 V to 7.1 V (the loop is out of regulation there) and falls above it. Near 6.4 V it changes by +0.21 A per volt, so by extrapolation the current at 6.30 V is about 2.119 A, below the 2.140 A used. The largest current in the sweep, 2.306 A, is at 7.1 V, where the rail is 5.80 V, higher than at 6.4 V. The note's statement "the current falls with the pack, so this bounds it" holds, and 6.4 V is the limiting pack for the rail. Lowest drain rail in the hot group: 5.19 V at 6.4 V.
- **Reviewer extraction from the committed r2-s3 `runs.json`.**
  - TR_DRV low to the TX (NO) contact starting to open, option E, freewheel diode: minimum **0.147 ms** from the 4.89 V key-down hold at an 85 C coil (set `tau0.6_rho2_sig2`, steep slope); 0.167 ms from the 4.99 V hold. Iteration 2's figure was 0.215 ms from the 5.25 V hold (finding-10).
  - The slowest option E release is 24.86 ms (6.43 V hold, -10 C, set `tau2.4_rho4_sig0.5`), 25.86 ms with ordering and bounce, equal to K12-E. The limiter pass-short case (8.40 V hold, -10 C) is still 27.80 ms in the run (finding-13).
- **Hand checks.**
  - Rail floors: 6.30 - 2.140 x 0.5646 = 5.092 V; less 0.10 V: 4.992 V; less the 0.10 V dropout: 4.892 V at the coil. Worst unit's must-operate at 85 C: 3.75 x (1 + 0.005347 x 62) = 4.993 V (steep), 3.75 x (1 + 0.0048 x 62) = 4.866 V (shallow); 4.892 / 4.993 = 0.980 and 4.892 / 4.866 = 1.005.
  - Pull-in floor: 6.30 - (0.111 + 0.035) x 0.614 = 6.210 V; less 0.10 V: 6.110 V.
  - Stale-ratio trigger: 10 - 1.083 - 0.0833 = 8.834 s; with the 7.2 s hang (30 dits at 5 WPM), 1.63 s of keying.
- **Figures opened and inspected before citing:**
  - `s3-keydown-hold.png`: panel (a) marks the 5.09 V (0.9997) and 4.99 V (0.9797) points on the revision 2 dropout line and the lever point at 5.34 V (1.0499); panel (b) the hold against the discharge;
  - `s3-limiter-setpoint.png`: the key-down hold is flat at 0.980 for every set point (the limiter is in dropout at the lowest rail); the pull-in reaches the 10 ms limit near a 6.0 V set point;
  - `s3-operate-vs-coil-temperature.png`: option E at 6.11 V crosses the 9.5 ms operate limit only above about 90 C at the band's slow edge;
  - `timing-diagram.png`: panel (a) shows the option E contact band ending at t0 + 8.57 ms, right of both the PA_EN edge (t0 + 7.5) and the TX_KEY edge (t0 + 8.0) (finding-9); panel (b) shows TR_DRV as one level to the hang expiry;
  - `s4-stale-ratio.png`: the x-axis label now reads "after an over longer than 8.83 s"; the not-radiated elements carry no TR_DRV, PA_EN or TX_KEY;
  - `s1-coil-voltage-vs-pack.png`, `s3-release.png`, `s4-keydown-budget.png`, `s4-margins.png`: content as at iteration 2 apart from the r2 floor labels;
  - the reviewer's `sa23a-it3-checks.png`.

### Re-check of finding-1 (Major, Verified at iteration 2)

| Criterion | Result at iteration 3 | Evidence |
|---|---|---|
| (1a) to (1d) | Still met | Revision 2 does not touch TR_DRV, the K12 level trigger, the 30 ms re-arm, the gate's T/R input or their routing. K21-E is unchanged (T_rearm 30 ms against the 25.86 ms release, K12-E reproduced). Rows KD-04, KD-17 and KU-06 are unchanged. `timing-diagram.png` panel (b) still draws one TR_DRV level per over |
| (1e) | Still met | The new findings of this iteration are Minor. None lets a single fault restore RF past a hardware control or defeat the backstop |

### Re-check of finding-2 (Major, Verified at iteration 2)

| Criterion | Result at iteration 3 | Evidence |
|---|---|---|
| (2a) Firmware-set coil parameters removed | Still met | Option E has no duty, no PWM and no pull-in timer. The only coil-drive firmware action is the TR_DRV level (K22-E) |
| (2b) Coil voltage under the maximum in every firmware state | Still met | At most 6.426 V, 128.5 %, against 151 % at 70 C (K19-E, unchanged) |
| (2c) Key-down hold guaranteed by the datasheet without a firmware reading | **Restated: partly met** | The hold still uses no firmware-set coil parameter. But the datasheet guarantee is no longer shown at the worst corner: K15-E is 0.980 to 1.005 x at 4.89 V (reproduced by hand and in reviewer panel (b)). Iteration 2 recorded this criterion as met at 1.051 to 1.079 x. That rested on the TS-012 feed budget (0.45 ohm at 2 A from a 6.35 V receive rail); iteration 2's own reviewer panel put the loss of the guarantee at 0.578 ohm, and the WP-PDR-21 revision 3 bound (0.5646 ohm at 2.140 A) with a 6.30 V start and the 0.10 V discharge lies past it. This record corrects that entry. The shortfall is a hardware margin, not a software contribution, so finding-2 stays Verified. Two things about it are assurance gaps and are raised below: the residual is not in the hazard proposal (finding-14), and the pack floor that the hold now rests on is set by a firmware prerequisite and a TBR value (finding-15) |
| (2d) Remaining causes named with detection and routed | Partly met | The fault causes are as at iteration 2. The no-fault drop-out at the worst corner, which revision 2 itself describes in section 4.3, is not among them (finding-14) |
| (2e) No new Major gap | Met | See the finding table; each new finding is Minor, with the reason stated |

### Review of what revision 2 changes (assurance lens)

- **K15-E OPEN in the recommended design.** Note section 4.3 says so plainly and names both closing paths: the WP-PDR-21 C2 P-FET lever (1.050 to 1.077 x), which the owner already decides for REQ-SYS-012, or BM-1 on the fitted relay (must-operate at most 4.89 V with the coil at 85 C). It also states the consequence: "a hot unit at the worst datasheet limit could drop out under RF near the end of a long over at the lowest pack", hot switching and a VGG step on reclosure, detected by REQ-SYS-156. From the assurance lens the statement is correct and complete as analysis. The model band gives hold / release at least 1.13 at that corner (section 4.3 table), so the class E model predicts no drop-out: what is missing is the datasheet guarantee, not a predicted failure. At that corner the pack is at its lowest, so the 8.4 V stability-limit mechanism of HZ-008 C6 does not apply. Its routing is finding-14.
- **The pack floor.** Revision 2 takes 6.30 V from REQ-SYS-097 ("refuse to start a transmission while either cell, measured in receive, reads below 3.20 V +/-0.05 V (TBR)"), the lower edge of its tolerance. 07 section 14.1 line 590 places that inhibit in `SW-TXSEQ`, and 07 section 14.2 row h (line 622) makes it a `PA_EN` prerequisite. The cells are read by two dissimilar paths (`ICD-PWR-CELL.md`, per-cell supervision row). So K1b-E and K15-E now rest on a safety-critical firmware prerequisite and on a TBR value that "the power trade study at PDR fixes". Reviewer panels (a) and (b) give the margins: K1b-E holds down to a pack of 6.075 V; K15-E with the lever holds down to 6.051 V (steep slope); without the lever it would need 6.401 V. See finding-15.
- **K22-E.** The restatement "(r2) K22-E no longer quotes the hold ratio as part of its test: its hardware margin is K15-E's question" is correct. The unchanged sentence before it, "the key-down hold is set by the pack, the feed and the limiter with no reading used", is no longer accurate: the lowest pack is set by the REQ-SYS-097 reading (finding-15).
- **The key-down current basis.** Reviewer panel (c) confirms that 2.140 A at 6.4 V bounds the current at 6.30 V and that 6.4 V is the limiting pack for the rail. The new check `p4_feed_current` reproduces the three currents when the `.raw` is present; it passes without re-deriving them when it is not (finding-16).
- **Stale-ratio restatement (review finding-14).** The firmware rule was already stated on the ratio age in revision 1 (section 4.8: `SW-TXSEQ` starts no changeover while the ratio is older than A_kd and a refresh is in progress; `SW-SAFE` sets no PA_EN on such a ratio). Revision 2 aligns K20-c, SR-01, the section 7 condition (2) and the TC-SYS-102 set-up with it. The arithmetic (8.83 s, 1.63 s of keying) is reproduced. The HostUnit cases (ratio age 10.1 s and 9.9 s, and a closure held across the refresh end) test both sides of A_kd. Criterion (3d) is met. One note for WP-PDR-35 and 43, not a finding: the TC-SYS-102 case "with the age injected" should inject the age through the HostUnit time source, not through a hook left in the flight build.
- **The lower pull-in floor and the settle prerequisite.** KD-12 now ends at t0 + 8.567 ms. PA_EN at t0 + 7.5 ms is 1.07 ms before the worst-case settle and TX_KEY at t0 + 8.0 ms is 0.57 ms before it; the ramp at t0 + 10.0 ms is 1.43 ms after it. The backwave argument of finding-9 still holds. Finding-9's first suggested fix (PA_EN and TX_KEY at t0 + 8.5 ms) no longer covers the settle; it would need t0 + 8.6 ms or later.
- **The lower key-down hold and the NO-contact opening.** With the 4.89 V hold the TX contact starts to open from 0.147 ms after TR_DRV low (reviewer extraction), not 0.215 ms. The D-18 clamp and the driver supply below 3.1 V within about 20 us (`pa-permit-gate-d18.md` section 5.3) are still well inside that, so the carrier claim of finding-10 still holds; its quoted basis (1.13 ms) is now almost 8 times the event that matters.

### State of the earlier Minor findings

| Finding | State at iteration 3 | Note |
|---|---|---|
| finding-3 | Open (lien) | Not addressed (rule C1); superseded in magnitude by finding-9 |
| finding-4 | Open (lien), partly mitigated | As at iteration 2 |
| finding-5 | Open (lien) | Not addressed; unchanged |
| finding-6 | Open (lien), partly addressed | As at iteration 2: the pull-down is named (section 6.1 item 3) without its value or the KD-04 row |
| finding-7 | Open (lien) | Not addressed; unchanged |
| finding-8 | Open (lien) | Not addressed. `relay_model.py` is unchanged; `seq_run.py` grew by 223 lines and two checks and still has no TV record. K1b-E's margin now rests on the model at a lower pull-in voltage (1.43 ms) |
| finding-9 | Open (lien), facts moved | KD-12 max 8.567 ms (was 8.388). PA_EN precedes the settle by 1.07 ms and TX_KEY by 0.57 ms; the ramp follows it by 1.43 ms. The t0 + 8.5 ms option of its fix no longer suffices |
| finding-10 | Open (lien), facts moved | NO-contact opening minimum 0.147 ms (was 0.215 ms), from the lower key-down hold. The carrier claim still holds; the note still cites 1.13 ms |
| finding-11 | Open (lien) | Not addressed; T_rearm and K21-E unchanged |
| finding-12 | Open (lien) | Not addressed; TS-012 lines 602, 815 and 991 still say "coil held by PWM" at HEAD |
| finding-13 | Open (lien) | Not addressed; the note still gives 27.67 and 28.67 ms, the run 27.80 and 28.80 ms |

### Findings (iteration 3)

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-14"></a>finding-14 | assurance | Minor | swe-205 7.1 task 5; swe-134 7.1 task 6; SA-C-i; SA-D6 | Note section 4.3 K15-E bullet ("Until then, a hot unit at the worst datasheet limit could drop out under RF near the end of a long over at the lowest pack ... detected by REQ-SYS-156 (section 4.9, limiter row)"); section 4.9 failure-mode table, row "Limiter: output low, open or high dropout" and its proposed HZ-008 cause "T/R contact open or reopened under RF by a relay coil supply fault (limiter or driver)"; section 6.2 rows WP-PDR-16 and WP-PDR-21; section 9 BM-1; Summary bullet 5 ("dropout at most 0.2 V") | **The residual of K15-E, a drop-out under RF with no fault, is not in the hazard proposal, has no closing gate, and the Summary still carries the withdrawn dropout value.** (a) The HZ-008 cause that section 4.9 proposes to WP-PDR-16 is limited to a coil-supply fault. Revision 2 shows a second route to the same effect with every part in tolerance: a worst-case unit, a coil at 85 C, the pack at the REQ-SYS-097 floor, the feed at its bound, late in a long over (0.980 to 1.005 x). The section 4.3 text points to the limiter-fault row for its detection, but that row and the WP-PDR-16 request do not carry the no-fault case. (b) K15-E closes by the owner's REQ-SYS-012 lever decision or by BM-1, and no gate is named by which one of them must happen. BM-1 closes it only for the fitted relay; a replacement relay would need BM-1 again, and the note does not say so. (c) Summary bullet 5 still reads "dropout at most 0.2 V", while section 6.1 item 2 and INPUTS `v_lim_do` require 0.10 V. A limiter chosen to the Summary's figure gives 0.960 x, the note's own figure. Minor: the note states K15-E OPEN correctly and names its detection (REQ-SYS-156) and bound (D-9); the model band predicts no drop-out (hold / release at least 1.13); the stability-limit mechanism does not apply at the lowest pack. Fix: add a no-fault row to the section 4.9 table and name it in the WP-PDR-16 request as a second condition of the proposed HZ-008 cause until K15-E closes; state the gate by which K15-E closes (for example the CDR readiness declaration, and in any case before the first transmission into an antenna) and send it to the owner with the REQ-SYS-012 lever decision; add to BM-1 that it is repeated for any replacement relay; correct the Summary to 0.10 V | Open | Pending | |
| <a id="finding-15"></a>finding-15 | assurance | Minor | swe-205 7.1 task 1; swe-134 7.1 task 1; swe-058 7.1 task 1; SA-C-g; SA-C-h | Note section 2 row "(r2) Pack at the start of a transmission, lowest" (6.30 V, class R, REQ-SYS-097); section 4.3; section 4.9 K22 paragraph ("the key-down hold is set by the pack, the feed and the limiter with no reading used"); section 6.2 row WP-PDR-24 (reports the rail only); section 9 BM-1 (4.89 V) and BM-2 (6.11 V). REQ-SYS-097 TBR: "the power trade study at PDR fixes the value". 07 section 14.1 line 590 and section 14.2 row h, line 622 (`SW-TXSEQ` low-voltage inhibit, a `PA_EN` prerequisite) | **The relay's pull-in (K1b-E) and hold (K15-E) now rest on the REQ-SYS-097 low-voltage prerequisite, which is firmware and a TBR, and the note neither states that dependence as a constraint nor routes it.** Revision 2 takes the pack floor as the lower edge of the REQ-SYS-097 tolerance, 3.15 V per cell. That floor exists only because the `SW-TXSEQ` row h prerequisite refuses a transmission below it, using a cell reading. Reviewer panels (a) and (b): K1b-E is lost below a pack of 6.075 V (3.04 V per cell); K15-E with the lever is lost below 6.051 V (steep slope, about 3.03 V per cell); without the lever it would need 6.401 V. So a REQ-SYS-097 lower edge set below about 3.04 V per cell by the power trade study, or a reading or threshold error of more than about 0.22 V of pack beyond the tolerance, removes K1b-E (late contact into an open NO contact, a VGG step at closure) and, with the lever taken, K15-E. MOE-004 shows pressure on that threshold: its endurance floors have margin "only if the receiver current stays near 260 mA". The section 6.2 WP-PDR-24 row reports the rail but asks for no limit on the threshold. The HZ-008 cause proposed to WP-PDR-16 does not name the REQ-SYS-097 prerequisite as one of its controls (it traces to HZ-007 K4 only). BM-1's 4.89 V and BM-2's 6.11 V are tied to the 6.30 V floor and would move with it. The K22 sentence quoted above is no longer accurate. Minor: at the present REQ-SYS-097 value both results stand as the note states them; the prerequisite is already in a safety-critical component with a two-path cell reading and a closing case (TC-SYS-069); the needed error is several times the requirement's own tolerance; and the effect has the REQ-SYS-156 detection. Fix: state in section 6.2 (and section 7 if the owner sees it there) a constraint on the REQ-SYS-097 TBR: the lower edge not below the pack that keeps K1b-E and K15-E (reviewer figures 6.075 V and 6.051 V with the lever, about 3.04 V per cell; the author re-derives them), and route it to the power trade study and WP-PDR-24 with the REQ-SYS-097 TBR; name the `SW-TXSEQ` row h low-voltage prerequisite (REQ-SYS-097) as a control of the proposed HZ-008 cause in the WP-PDR-16 request; tie BM-1 and BM-2 to the floor in force; correct the K22 sentence (for example "no firmware-set coil parameter; the lowest pack is the REQ-SYS-097 prerequisite") | Open | Pending | |
| <a id="finding-16"></a>finding-16 | assurance | Minor | swe-070 7.1 task 1; swe-058 7.1 task 5; SA-E3 | `seq_run.py` `p4_feed_check`, the early return `{"pass": True, "note": "p4 .raw not present: inputs used as recorded, not re-derived"}`; note section 3.4 ("On 2026-09-29 all 17 checks pass") and section 14 row review finding-13 ("the key-down currents re-derived from the WP-PDR-21 p4 `.raw`, SHA-256 checked") | **The new check `p4_feed_current` reports PASS when its evidence is missing.** The p4 `.raw` (20,405,166 bytes) is kept out of git under CR-017 C2, so it exists only in the working tree where WP-PDR-21 ran. In any other checkout (a clone, a worktree, a CI run, a later reviewer) the check returns PASS without reading anything, `--expect` exits 0, and the log prints "check s4.p4_feed_current: PASS". Reviewer re-run in a clean worktree at `249356b` shows exactly that; with the `.raw` copied in (hash equal to `raw.sha256`) the check re-derives 2.1403, 2.2151 and 2.2335 A and the s4 output is byte-identical to the commit. The inputs are correct (reviewer panel (c)). The defect is in the evidence: a "17 of 17 checks pass" statement does not show whether the currents that decide K15-E were re-derived. Minor: the values are right and the committed `result.json` records the re-derivation. Fix: give the check a third state (for example "not run: `.raw` absent") that is not counted as PASS and that `--expect` reports; or keep PASS only when the `.raw` was read, and state the condition in section 3.4 and the README | Open | Pending | |

No Major finding is open: `assurance_verdict` APPROVED at iteration 3 (07 section 10.2; rule C1). finding-14 to finding-16 are Minor liens raised after the first APPROVED verdict, due at the CDR readiness declaration unless the author closes them earlier, like finding-3 to finding-13.

**Why none of the three is Major.** The template makes a missing software contribution to a hazard a Major. finding-15 is closest to it. The contribution it names is not new: the REQ-SYS-097 prerequisite already sits in the safety-critical `SW-TXSEQ` component with a two-path cell reading, and its closing case exists. What is new is that the relay's timing now depends on its value, which must be written down and sent to the owner of that value. At the value in force the note's conclusions stand. This is a routing and constraint gap, not a software cause missing from the hazard data. If the power trade study moves the REQ-SYS-097 lower edge below about 3.04 V per cell before this finding is fixed, this record's assessment changes and the finding becomes Major.

### Task table (iteration 3, delta)

| Task | Safety-critical designation (SWEHB 8.10 section 6) | Applied | Result and evidence | Relief (N/A only) | Finding ids |
|---|---|---|---|---|---|
| swe-134 7.1 task 5 (every type) | SC | Yes | This record is the assurance participation in the delta review of a product that sets `SW-TXSEQ` and `SW-SAFE` design values | | none |
| swe-087 7.1 task 2, swe-088 7.1 task 2 | | Yes | finding-1 and finding-2 re-checked against their criteria at `249356b`; (2c) restated with its evidence; the earlier Minor liens' states recorded | | none |
| swe-057 7.1 task 2 (design) | | Yes | Revision 2 leaves TR_DRV and the D-5 purpose unchanged | | none |
| swe-058 7.1 task 1 (design) | | No | The pack floor the design uses is a TBR enforced by firmware and is not stated as a constraint (finding-15); the settle prerequisite and the moved KD-12 (finding-9); the limiter-short figure (finding-13) | | finding-9, finding-13, finding-15 |
| swe-058 7.1 task 3 (design) | | Yes | No undesired software behaviour is added by revision 2 | | none |
| swe-058 7.1 task 4 (design) | SC | Yes | Cold switching on a TR_DRV dip holds for the carrier at the new 0.147 ms opening; the no-fault drop-out under RF is analysed and detected (REQ-SYS-156); its routing is finding-14 | | finding-10, finding-14 |
| swe-058 7.1 task 5 (design) | | Yes | Reviewer design analysis: K1b-E and K15-E against the pack floor, the p4 current against the pack, the NO-contact opening and the slowest releases from the r2 runs, hand checks (Commands) | | finding-15, finding-16 |
| swe-134 7.1 task 1 (design) | SC | No | Items g and h carry the pack-floor dependence (finding-15); item c and i as below | | finding-9, finding-10, finding-15 |
| swe-134 7.1 task 4 (design) | SC | Yes | No new safety datum without protection: the pack reading that now bounds the relay's margin is the existing two-path reading of the REQ-SYS-097 prerequisite | | none |
| swe-134 7.1 task 6 (design) | SC | No | The proposed HZ-008 cause does not carry the no-fault drop-out or the REQ-SYS-097 control; the earlier routing gaps remain (finding-11, finding-12) | | finding-11, finding-12, finding-14, finding-15 |
| swe-205 7.1 task 1 | SC | Yes | Software contributions of the recommended design: unchanged from iteration 2. The REQ-SYS-097 prerequisite is identified here as a condition of the relay's margin (finding-15) | | finding-15 |
| swe-205 7.1 task 5 | SC | No | The design needs of the safety analysis are not all requested: the no-fault drop-out and the REQ-SYS-097 control in the HZ-008 proposal, the K15-E closing gate (finding-14, finding-15), and the earlier gaps (finding-11, finding-12) | | finding-11, finding-12, finding-14, finding-15 |
| swe-070 7.1 task 1 (models) | | No | Still no TV record (finding-8); the new check `p4_feed_current` passes with its evidence absent (finding-16) | | finding-8, finding-16 |
| swe-136 7.1 task 1 (tool) | | Yes | LTspice 26.0.2 only through `tools/ltspice-batch.sh` (ACC-LTSPICE-001, TV-014); provenance lines in the r2-s1 and r2-s2 `result.json` | | none |
| swe-192 7.1 task 1 | SC | Yes | R3 re-run: 0 violations. The note claims no closure | | none |
| swe-089 7.1 task 1 | | Yes | Measurements below | | none |
| swe-081 7.1 task 2 | SC | Yes | The product is committed on main at `249356b`; the only raw file above 5,000,000 bytes is kept untracked with a matching `raw.sha256` (CR-017 C2); the WP-PDR-21 `.raw` the note reads matches its committed `raw.sha256` | | none |

### SWE-134 items (iteration 3)

| Id | Answer | Evidence |
|---|---|---|
| SA-C-b | Yes | Key-down and key-up orders unchanged; TR_DRV one level; key-up cold (K10) |
| SA-C-c | No | Unchanged gap of finding-4 and finding-10; the NO contact now opens from 0.147 ms |
| SA-C-f | Yes | No firmware-set coil-drive datum (K22-E) |
| SA-C-g | No | The pack reading of the REQ-SYS-097 prerequisite now bounds the relay's pull-in and hold margins; this use of it is not stated or routed (finding-15). The reading itself keeps its two paths |
| SA-C-h | No | "T/R in TX and settled" at t0 + 7.5 ms precedes KD-12 max t0 + 8.567 ms (finding-9). The REQ-SYS-097 prerequisite now also carries the relay's floor (finding-15) |
| SA-C-i | No | finding-1 and finding-2 stay Verified. Residual Minor gaps: the no-fault drop-out under RF not in the hazard proposal (finding-14), the re-arm rationale (finding-11) |
| SA-C-j | Yes | K12-E 25.86 ms against the 30 ms share; K16 1.1 ms; the stale-ratio window 82.8 ms, unchanged |

### Readiness (iteration 3)

| # | Result | Evidence |
|---|---|---|
| R1 | Yes (own part) | 43 of 43 blobs equal at `249356b`, at HEAD and in the working tree. The paired record's list is checked at filing (X-2) |
| R2 | Yes | `design`, safety-critical, unchanged |
| R3 | Yes | validate_docs 123 passed at HEAD; traceability 0 violations; this record text validates at its path |
| R4 | Yes (in progress) | The file review's delta runs under its own invocation. This invocation is not the author, that reviewer, or an earlier assurance reviewer |

### D, E and F (iteration 3)

| Id | Answer | Evidence |
|---|---|---|
| SA-D1 | Yes | SWEHB `swe-205` section 7.7.2 re-walked for revision 2. **Control of safety-critical hardware:** the hold stays in hardware; its margin at the worst corner is not shown (K15-E, finding-14). **Interlocks and inhibits:** the REQ-SYS-097 inhibit now also bounds the relay's pull-in and hold (finding-15). **Common cause:** a low pack lowers both the pull-in voltage and the key-down hold, and both are bounded by the same prerequisite. **Timing:** finding-9 and finding-10, facts moved |
| SA-D6 | No | The hazard-analysis updates the revised design needs are not all requested (finding-14, finding-15; finding-11, finding-12 remain) |
| SA-E1 | Yes | Both Major findings re-checked with evidence; the change to (2c) is recorded with its basis; no finding closed without evidence |
| SA-E3 | Yes, with finding-16 | `249356b` edits only WP-PDR-23a files; check_commit_msg PASS; CR-017 C2 kept for `coil_tran.raw`. The retained p4 `.raw` is used as evidence by a check that passes without it (finding-16) |
| SA-F2 | Yes | Front matter: `assurance_findings_major` 2 (both Verified), `assurance_findings_minor` 14, `items_no`, effort |

### Cross items for the software lead (iteration 3)

- **X-2 (open).** The paired file review record and its deltas are not filed at HEAD `249356b`. At filing, the software lead writes its id into `paired_record` here, transcribes this pairing and `assurance_verdict` APPROVED into it, and checks SA-A3 and SA-A4 there.
- **X-5 (open).** The INSP-122 and INSP-123 id collisions stand as recorded at iteration 2.
- **X-7 (new).** Revision 2 takes its feed bound and key-down currents from `pa-drive-ts012.md` revision 3 (`f1070cf`, WP-PDR-21), which is under review. A change there re-opens K15-E, K1b-E, KD-12, BM-1, BM-2 and BM-6 here, and finding-15's margins. The owner's C2 P-FET lever decision in that record decides K15-E.
- **X-8 (new).** Note section 6.2 routes to WP-PDR-24 that the switched pack rail reaches 5.09 V at key-down (4.99 V after the discharge). WP-PDR-24 should confirm that the supplies of the safety-critical firmware and the PA_EN and TX_KEY pull-down states stay in regulation at that rail. This is not a finding on this note.
- **X-9 (new).** A trial run of `tools/validate_docs.py` with `verdict: APPROVED` on this text fails one rule: `findings_open` is 14 while the latest iteration's finding table shows 3 open findings. When the software lead sets the record verdict, the 11 earlier Minor liens are counted the way the lead SE convention counts liens of an earlier iteration (INSP-073 re-pin precedent: a lien counted apart from `findings_open`), or the check is run as it stands then. With `verdict: NEEDS CHANGES`, as filed, the record passes.

### Measurements (SWE-089, iteration 3)

Tasks in the iteration 3 table: 17 rows (17 applied Yes or No); tasks answered No: 5. Section items checked: 21 (R1 to R4, SA-C-b, c, f, g, h, i, j, SA-D1, D6, E1, E3, F2, and the two re-check tables and the change review); answered No: 5 (SA-C-c, g, h, i, SA-D6). Findings: iteration 3 adds 3 Minor; the 2 Major of iteration 1 stay Verified (criterion (2c) restated); the 11 earlier Minor findings stay liens (finding-9 and finding-10 facts moved). Effort: 42 turns, about 80 minutes. Renders inspected: 11 (10 of the product, the render counted once, and 1 reviewer). Reviewer re-runs: s1 to s4 with `--expect` in a clean worktree (17 of 17 checks, 40 of 40 verdicts; data byte-identical except the `p4_feed_current` block), and s4 again with the p4 `.raw` present (byte-identical). One reviewer script (3 analyses, 1 render).

### Verdict format (iteration 3)

```
ASSURANCE VERDICT: APPROVED (iteration 3, delta)
PRODUCT: docs/design/analysis/sequencer-timing.md@b6a5e31a, docs/reviews/PDR/figures/timing-diagram.png@49db873d, hardware/sim/tx-seq/seq_run.py@d28ab4a1, hardware/sim/tx-seq/relay_model.py@0285c9c9 at 249356b (runs 2026-09-29-r2-s1 to s4); PAIRED RECORD: pending (analysis-sequencer-timing.md, INSP-122 proposed, not filed)
PRODUCT TYPE: design (routed by PDR work plan WP-PDR-23; X-1); CRITICALITY: safety-critical
FINDINGS:
- [Major] finding-1 still Verified: TR_DRV one static level per over; K12 level-triggered with the 30 ms re-arm; unchanged by revision 2.
- [Major] finding-2 still Verified: no firmware-set coil-drive parameter; coil at most 128.5 %. Criterion (2c) restated: the datasheet hold guarantee at the worst corner is not shown (K15-E 0.980 to 1.005 x), a hardware margin; iteration 2's 1.051 x rested on the TS-012 feed budget.
- [Minor] finding-14 swe-205 7.1 task 5 (SA-C-i, SA-D6) the no-fault drop-out under RF (K15-E) is not in the HZ-008 cause proposed to WP-PDR-16; no gate for closing K15-E; BM-1 not repeated for a replacement relay; Summary still says dropout 0.2 V.
- [Minor] finding-15 swe-205 7.1 task 1 (SA-C-g, h) K1b-E and K15-E rest on the REQ-SYS-097 low-voltage prerequisite (SW-TXSEQ row h, TBR): K1b-E lost below a 6.075 V pack, K15-E with the lever below 6.051 V; no constraint routed to the TBR owner; K22 text says "no reading used".
- [Minor] finding-16 swe-070 7.1 task 1 (SA-E3) check p4_feed_current passes when the retained p4 .raw is absent (clean checkout), so "17 checks pass" does not show the currents were re-derived.
- finding-3 to finding-13 (Minor): Open liens; finding-9 (KD-12 now 8.567 ms) and finding-10 (NO contact opens from 0.147 ms) facts moved.
TASKS APPLIED: swe-134 7.1 tasks 1, 4, 5, 6; swe-057 7.1 task 2; swe-058 7.1 tasks 1, 3, 4, 5; swe-205 7.1 tasks 1, 5; swe-070 7.1 task 1; swe-136 7.1 task 1; swe-192 7.1 task 1; swe-087 7.1 task 2; swe-088 7.1 task 2; swe-089 7.1 task 1; swe-081 7.1 task 2
TASKS N/A (relief): none at iteration 3
SWE-134 ITEMS CHECKED: b, c, f, g, h, i, j
MEASUREMENTS: tasks=17; tasks_no=5; turns=42; minutes=80; major=0 open (2 verified); minor=14 open
```
