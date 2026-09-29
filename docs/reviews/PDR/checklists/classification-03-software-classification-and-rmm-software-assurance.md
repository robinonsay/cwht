---
# Peer-review record front matter (charter sections 2 and 5; docs/process/01-lifecycle-and-reviews.md
# section 13; docs/process/07-software-engineering-plan.md sections 2.1.1, 10.2 and 15). This is the
# paired software assurance record of INSP-037 (docs/reviews/PDR/checklists/classification-03-software-
# classification-and-rmm.md, the independent classification assessment of the WP-PDR-17 wave 0 change set,
# CR-010), at the record path PDR work plan WP-PDR-17 "Records" names.
# Checklist applied: docs/templates/peer-review-checklist-software-assurance.md revision A as on its CR-012
# branch (cr/CR-012-pdr-checklist-templates at 7784672, blob 5b135285; CR-012 Submitted, not merged).
# tools/validate_docs.py requires the checklist field to name a template that exists on main, so the field
# names peer-review-checklist-classification revision A (the checklist of the paired record and of the SRR
# pair INSP-017) and checklist_software_assurance records the template actually applied (the INSP-047 form);
# the delta after CR-012 merges switches the field.
# Product: the same five blobs as INSP-037 product_files. The four product files exist only on the unmerged
# branch cr/CR-010-apply-srr-decisions-9-and-40 at 5cd87cf (base ab2af2d); the CR file blob is on main.
# Lead SE convention (2026-09-27, INSP-031 practice): reviewer_verdict and assurance_verdict are set here;
# the record verdict stays held until the CR-010 merge brings the blobs to main.
# Iteration 2 (2026-09-29, re-pin delta; lead SE rulings (2) and (3) of 2026-09-29, CR-010 section 9): 07 is
# re-pinned from 3ae7d73b (CR-010) to 0ad37a43, the combined CR-010 plus CR-013 text on
# cr/CR-013-process-04-07-semp-srr-liens (41c588c, unchanged at the branch head 1a486e4); the other three
# product blobs are unchanged; the CR-010 file is dropped from product_files (section "Iteration 2").
id: INSP-050
checklist: peer-review-checklist-classification
checklist_revision: A
checklist_software_assurance: "docs/templates/peer-review-checklist-software-assurance.md@5b13528504868b2add0f0b1e329c63aa2b54cdf4 (revision A, CR-012 branch head 7784672)"
checklist_file: docs/reviews/PDR/checklists/classification-03-software-classification-and-rmm-software-assurance.md
product: docs/process/03-software-classification-and-rmm.md
# product_commit: iteration 1 was the CR-010 branch head 5cd87cf. Iteration 2: 41c588c, the CR-013 commit (parent
# 5cd87cf) that holds all four product blobs below; the CR-013 branch head 1a486e4 holds the same four blobs
product_commit: "41c588cddc9a97cec536482dc2bd164e2bf81ea3"
# product_files iteration 2: 07 3ae7d73b replaced by 0ad37a43 (lead SE ruling (3): main holds 3ae7d73b only between
# the CR-010 and CR-013 merge commits, and this record's verdict is set in the CR-013 merge commit). The entry
# "docs/cm/cr/CR-010-apply-srr-decisions-9-and-40.md@ebce01d6359441d53690c437d32b8ca305790b28" is dropped (lead SE
# ruling (2); INSP-060 and INSP-032 precedent): sections 1 to 4 of CR-010, which this record reviewed, are unchanged
# from ebce01d6 to 27604ce9, and the section 5 hunks fill only the Done column of steps 3 to 6; the CR file is a
# record on main appended at each lifecycle step, so a pin would drift at the merge (section "Iteration 2")
product_files: ["docs/process/03-software-classification-and-rmm.md@1e03b873b404deeaa86ba2393806cda74996187d", "docs/process/07-software-engineering-plan.md@0ad37a43a9d365408b78488f6c2b02933af56837", "docs/process/rmm.json@a907a087f1302e275ea56bdb7bba89638777a319", "docs/process/rmm.md@17ea4733a4d41b54424619f8682db815b05d4ebf"]
# input_files: read, not reviewed, at main HEAD 13a4f66: the hazard source of record (0.5.0-pha), the SRR memo,
# and the paired record INSP-037 (iteration 2). Iteration 2 adds, read at main 9fda694: the CR-010 file (27604ce9), the
# CR-013 file (the change record of the 07 delta), and 07 at 3ae7d73b (the blob iteration 1 reviewed, the delta base)
input_files: ["docs/safety/hazards.json@81cacde47d4f2066ecac3947f3acf65e646b1ad0", "docs/reviews/SRR/decision-memo.md@110102bf003f1c4c28cc9365c9af7dee39e79abd", "docs/reviews/PDR/checklists/classification-03-software-classification-and-rmm.md@915959cb03c130b93f16e94379ac7ffa15e73fb9", "docs/cm/cr/CR-010-apply-srr-decisions-9-and-40.md@27604ce92a6c7cf086c4027cfb699e3b598ddf98", "docs/cm/cr/CR-013-process-04-07-semp-srr-liens.md@fef1f9d9892e825025e713db5e4b855ca52e5d77", "docs/process/07-software-engineering-plan.md@3ae7d73b01810e47fd10251d798e0a047aaa72dd"]
paired_record: INSP-037
product_type: plans
# criticality: safety-critical, as the paired record. 03 and 07 are routed by the 07 section 2.1.1 row
# "Software plans" (Yes in every column); the change set states the determination of safety-critical
# components (07 section 14.1 rows of the frequency-word path, the frequency verification unit and the menu
# override command path), so section C is answered for those components at plan maturity
criticality: safety-critical
product_size: 4 files changed on the branch (03 fifth revision, 07 revision A.8, rmm.json 5 implementation fields, rmm.md render; 72 insertions, 71 deletions) plus the CR-010 file (revision 2, 14 impact fields). Iteration 2 delta: 07 3ae7d73b to 0ad37a43 (CR-013, 22 insertions, 26 deletions, 18 hunks), CR-010 ebce01d6 to 27604ce9 (sections 1 to 5 read; 88 insertions, 22 deletions in all)
sprint: PDR-prep
author_agent: "author:WP-PDR-17 wave 0 (Claude as software lead, 03 and 07 author; CR-010 originator)"
reviewer_agent: "sa-reviewer:WP-PDR-17-classification"
assurance_required: true
assurance_reviewer_agent: "sa-reviewer:WP-PDR-17-classification (software assurance function; paired file review INSP-037 by reviewer:WP-PDR-17-classification)"
# iteration 2: re-pin delta on 07 0ad37a43 and the CR-010 file (section "Iteration 2")
iteration: 2
readiness_met: true
# reviewer_verdict and assurance_verdict: APPROVED; 0 Major, 3 Minor (rule C1: Minor findings ride with the
# first APPROVED verdict and become liens due at the CDR readiness declaration if not fixed)
# Iteration 2: unchanged. No new finding; finding-1 to finding-3 were not fixed before the CR-010 step 4 freeze, so
# they are liens due the CDR readiness declaration (rule C1)
reviewer_verdict: APPROVED
assurance_verdict: APPROVED
# verdict: held at NEEDS CHANGES while the reviewed blobs exist only on the CR-010 branch (lead SE convention;
# INSP-037 finding-7). The software lead sets APPROVED in the CR-010 merge commit, or the commit right after
# it, when the four blobs reach main unchanged and INSP-037 is APPROVED. If CR-010 step 4 changes a blob, this
# record first gets a delta iteration.
# Iteration 2 (lead SE ruling (3), 2026-09-29): the software lead sets APPROVED in the CR-013 merge commit, not the
# CR-010 one; CR-010 and CR-013 merge back to back, and the four blobs above are on main only after the CR-013 merge
verdict: NEEDS CHANGES
findings_major: 0
findings_minor: 3
# findings_open: 3 at iteration 1. Iteration 2: 0, because finding-1 to finding-3 are now liens (a lien is not Open;
# the INSP-037 and INSP-032 practice), shown in the iteration 2 finding table
findings_open: 0
findings_fixed: 0
findings_verified: 0
findings_deferred: 0
assurance_findings_major: 0
assurance_findings_minor: 3
assurance_tasks_applied: ["swe-134 7.1 task 5", "swe-022 7.1 task 1", "swe-013 7.1 task 1", "swe-013 7.1 task 2", "swe-024 7.1 task 1", "swe-024 7.1 task 2", "swe-024 7.1 task 3", "swe-039 7.1 task 7", "swe-039 7.1 task 8", "swe-121 7.1 task 1", "swe-125 7.1 task 1", "swe-139 7.1 task 1", "swe-087 7.1 task 3", "swe-090 7.1 task 1", "swe-154 7.1 task 1", "swe-156 7.1 task 1", "swe-036 7.1 task 1", "swe-036 7.1 task 2", "swe-020 7.1 task 1", "swe-176 7.1 task 1", "swe-205 7.1 task 1", "swe-205 7.1 task 2", "swe-205 7.1 task 3", "swe-205 7.1 task 4", "swe-205 7.1 task 5", "swe-023 7.1 task 1", "swe-134 7.1 task 1", "swe-134 7.1 task 4", "swe-134 7.1 task 6", "swe-219 7.1 task 1", "swe-220 7.1 task 1", "swe-220 7.1 task 2"]
swe134_items_checked: [a, b, c, d, e, f, g, h, i, j, k, l]
deferred_rids: []
items_no: [SA-C-a, SA-C-h, SA-D1, "swe-205 7.1 task 1", "swe-205 7.1 task 2", "swe-205 7.1 task 3", "swe-134 7.1 task 1", "swe-220 7.1 task 1"]
# effort: iteration 1 45 turns, 70 minutes; iteration 2 adds 30 turns, 45 minutes
effort_turns: 75
effort_minutes: 115
record_status: Open
date: 2026-09-27
date_closed: null
---

# Peer review record INSP-050: software assurance pair of INSP-037, WP-PDR-17 wave 0 change set (CR-010, SRR decisions 9 and 40)

**Product.** The four branch blobs of `cr/CR-010-apply-srr-decisions-9-and-40` at `5cd87cf` (base `ab2af2d`): 03 `1e03b873` (fifth revision), 07 `3ae7d73b` (revision A.8), `rmm.json` `a907a087`, `rmm.md` `17ea4733`; and the vehicle `docs/cm/cr/CR-010-apply-srr-decisions-9-and-40.md` blob `ebce01d6` (revision 2) on `main`. Identity checked with `git ls-tree cr/CR-010-apply-srr-decisions-9-and-40` (branch still at `5cd87cf`) and `git rev-parse HEAD:<path>` at `main` `13a4f66`: all five equal INSP-037 `product_files`. `git log baseline/srr..HEAD` on the four product paths is empty, so `main` still holds the baseline blobs. The change was read as `git diff --word-diff ab2af2d 5cd87cf` and the branch files at the changed sections and the sections they govern (03 sections 4.1 to 5, 6.5, 9; 07 sections 2.1.1, 3.1, 14.1, 14.2, 19; the five `rmm.json` rows).

**Checklist.** `docs/templates/peer-review-checklist-software-assurance.md` revision A **as on its CR-012 branch** (`cr/CR-012-pdr-checklist-templates` at `7784672`, blob `5b135285`; not merged; `git rev-parse main:<path>` fails). Sections R, A to F applied. `product_type` plans (07 section 2.1.1 row "Software plans" names 03 and 07; Yes in every column). `criticality` safety-critical, as in INSP-037, because the change set is the determination of three safety-critical components; section C is answered at plan maturity for those components (the provision and its allocation exist in 07 section 14.2 and 03 section 5).

**Acceptance criteria (rule C7).** Every task of the section B row "Every product type"; the `plans` row with its "for 07" and "for 03" lists; the section 7.1 tasks of every other SWE whose `rmm.json` row the product changes (SWE-023, SWE-134, SWE-205, SWE-219, SWE-220); SWE-134 items a to l for the frequency-word path, the frequency verification unit and the menu override command path (07 section 14.2 module rows at lines 642 to 644; 03 section 5 rows a to l); every CR-010 section 5 verification item; INSP-037 findings 1 to 7 re-read under the assurance lens.

**Independence (rule C4).** This invocation authored no part of WP-PDR-17, CR-010 or the branch commit, did not write INSP-037 (`reviewer:WP-PDR-17-classification`), and edited no product file. **Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: "INSP-037 peer review WP-PDR-17 CR-010"; "validate_docs peer review record schema paired_record checklist_software_assurance assurance_reviewer_agent"; "SWEHB 7.1 Tasking for Software Assurance SWE-205 safety-critical determination confirm software components"). One `git status`, `git branch` and `ls` of the checklists folder ran in the same first batch as the tool load (listing known paths, not a search). `grep -n`, `git grep` and read-only scripts were used afterwards only to pin lines, extract the SWEHB section 7.1 lists and compare JSON.

**Scope boundary.** As INSP-037: the wave 0 change set and the determination text it touches. The full PDR re-run (section 4.2 re-transcription, module assignment of the menu path, `SW-SYNTH` unit split, drivers joining the safety-critical row, OQ-SAF-014 closure) is later WP-PDR-17 work with its own iterations of both records.

## Record

### Findings

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | assurance | Minor | SA-D1, swe-205 7.1 tasks 1 to 3 | 03 section 6.5 items X14 (line 342) and X16 (line 345), "Owner; due" cells; 03 section 4.1 step 3 (line 102); `hazards.json` 0.5.0-pha HZ-001, HZ-004, HZ-005, HZ-006 and HZ-008 `firmware_role.components` | 03 section 4.1 step 3 keeps a type (ii) component traceable through this record only until "the next `hazards.json` change", in which the hazard analysis author adds it. X14 (safe-state manager and scheduler for HZ-008) was due "with the next `hazards.json` change after package decisions 9 and 40", and X16 (menu override command path for HZ-001, HZ-004, HZ-005, HZ-006) "after the owner's ruling on X20". That change happened: 0.5.0-pha (`bfea9c7`, "apply the SRR owner rulings of 2026-09-26", an ancestor of the CR base `ab2af2d`) applied decisions 9 and 40 and named neither component (script over the committed file: HZ-008 components are the word path, the verification unit and the TX sequencer prerequisite; HZ-001, 004, 005, 006 name no menu component). The fifth revision edits both rows and restates the due as "with the next `hazards.json` change", a trigger already passed without action, and names no WP; OQ-SAF-014 (close_by SRR) is still Open. So the hazard data do not yet carry the known incorrect-action contribution of the menu path or the HZ-008 components (swe-205 tasks 1 to 3), and the route that should put them there has no live due. Severity: Minor, because 03 section 4.3 and 07 section 14.1 already determine these components safety-critical with SWE-134, 219 and 220 applied, so no safety conclusion or rigor changes; the missing entries are a defect of `hazards.json`, which the WP-PDR-16 safety review and its SA pair judge. Fix: in 03 X14 and X16 state that 0.5.0-pha did not apply them and set owner and due to WP-PDR-16b (0.6.0-pha, the sole `hazards.json` writer from plan section 5.3) before F1, with OQ-SAF-014 re-dated there; cross item X-2 | Open | Pending | |
| <a id="finding-2"></a>finding-2 | assurance | Minor | SA-C-a, SA-C-h, swe-134 7.1 task 1 | 07 section 14.2 row a (branch line 615, "when REQ-SYS-182 is adopted, `PA_EN` is refused until the first frequency verification passes") and the `SW-TXSEQ` module row (line 633, "the frequency-verified prerequisite when REQ-SYS-182 is adopted (HZ-008 K7; h)"); CR-010 section 5 "Verification of the implementation" | Two SWE-134 provisions of a safety-critical function still read as conditional on decision 40, which the owner made (memo line 213, "Adopt with the 10 kHz window and 100 ms"). CR-010 section 5 lists "if REQ-SYS-182 is adopted" occurrences as resolved, and INSP-037 V1 answered Yes; both lines use "when" and were missed. 07 section 14.2 is the provision text the WP-PDR-35 author turns into `REQ-SW-SAFE-001` and the `SW-TXSEQ` item h requirement, so a conditional there invites an optional requirement. Severity: Minor, because row h (line 622), the frequency verification unit module row (line 644, item a) and section 14.1 state the same provisions without condition, and section 14.1 says the decline paths no longer apply. Fix: drop "when REQ-SYS-182 is adopted" in both lines and cite "REQ-SYS-182, SRR decision 40", in the CR-010 branch before the step 4 freeze (then a delta of INSP-037 and this record), or as a lien through the 07 writer order of plan section 5.3 | Open | Pending | |
| <a id="finding-3"></a>finding-3 | assurance | Minor | swe-220 7.1 task 1, swe-125 7.1 task 1 | `rmm.json` SWE-220 `implementation` (branch line 673 onward), a row CR-010 rewrites | The row states the SWE-220 measure as "rust-code-analysis (cyclomatic metric) in the CI check and recorded in docs/plan/tpm.json". 07 defines it otherwise: CS-17 (line 264) and section 8.1 (line 324) take the `rust-code-analysis-cli` 0.0.25 count plus one per `let ... else`, which the analyzer does not count and `tools/complexity_gate.py` adds (CR-005, 07 revision A.6), gate G5 (line 356) runs `complexity_gate.py --max 15`, and MSR-17 (line 516) records it in `docs/plan/measurements.json` (mirrored to `tpm.json` by `tools/measurements.py`, line 494). The RMM is the compliance statement of SWE-220; read alone it names a measure that under-counts against the limit of 15 for exactly the functions CR-005 corrected, now including the three components CR-010 adds to the row. Severity: Minor, since 07 governs the measure and the gate implements it. Fix: restate the row as "measured by gate G5 (07 section 8.4): `rust-code-analysis-cli` count plus one per `let ... else` (07 CS-17, CR-005) through `tools/complexity_gate.py --max 15`, recorded as MSR-17 in `docs/plan/measurements.json`" in CR-010 or at the PDR re-run (WP-PDR-17 `rmm.json` writer slot) | Open | Pending | |

**INSP-037 findings under the assurance lens (not raised again; 07 section 10.2, template finding rules).** finding-1 (Major, Verified at iteration 2): concur; re-measured independently at `5cd87cf` in a detached scratch worktree (removed after use): `validate_docs: 45 passed, 5 failed, 50 checked`, the five being INSP-017, INSP-009, INSP-006 (`cm-plan-05.md`), INSP-018 and INSP-010; `render_rmm.py --check` exit 0 with the counts CR-010 states. finding-2 (03 header scope), finding-3 (0.5.0-pha difference statement), finding-6 (03 item f): concur at Minor, record-keeping only. finding-4 (RFX-D4 "pending" though SRR decision 33 ruled "Convenience function", memo line 215): concur at Minor; under swe-134 task 6 the accumulator is outside every prerequisite in 07 row h in both outcomes, so no provision is missing. finding-5 (`rmm.json` SWE-205 concurrence state): concur at Minor; it is also the swe-176 task 1 record gap (task table). finding-7 (verdict hold not named in CR-010 step 6): concur; this record applies the same hold.

### Task table

| Task | Safety-critical designation (SWEHB 8.10 section 6) | Applied | Result and evidence | Relief (N/A only) | Finding ids |
|---|---|---|---|---|---|
| swe-134 7.1 task 5 | SC | Yes | This review is the assurance participation in the review of 03 and 07, which 07 section 2.1.1 routes here (row "Software plans") | | none |
| swe-022 7.1 task 1 | SC | Yes | Performed against the project software assurance plan (07 section 15, no hunk in the diff) by this record; the NASA-STD-8739.8 part is relieved | `rmm.json` SWE-022 T (standard not in the corpus) | none |
| swe-013 7.1 task 1 | SC | Yes | 03 and 07 keep their content for the PDR-prep event, with tailoring unchanged (script: only the five `implementation` fields of `rmm.json` differ; `disposition`, `tailoring_rationale`, `residual_risk`, `status`, `meta` equal). Two stale conditionals remain in 07 section 14.2 | | finding-2 |
| swe-013 7.1 task 2 | SC | Yes | 07 is the software assurance and software safety plan (07 section 2.1.1 row, section 15); section 15 is unchanged by the diff (hunks at 07 lines 147, 212, 540, 578, 591, 615, 639, 784, 805, 852, 883) | | none |
| swe-024 7.1 task 1 | SC | Yes | The change states owner rulings only; no NPR 7150.2D relief is added or removed (CR-010 section 4 "Software classification and tailoring"; INSP-037 V4); SWE-219 T and SWE-220 FC keep their dispositions with a wider named scope | | finding-3 |
| swe-024 7.1 task 2 | SC | Yes | Corrective action closure: INSP-037 finding-1 closed with rationale in CR-010 section 6.2 and verified at INSP-037 iteration 2; INSP-009 finding-10 (decision 9 and 40 part) is closed by the change text and verified at the CR-010 step 5 INSP-009 delta | | none |
| swe-024 7.1 task 3 | SC | Yes | Changed commitments recorded: WP-SW-14 made required for FW-B1 (07 sections 3.1, 19, 21), RSK-013 re-assessment routed to WP-PDR-18 (CR-010 Risk field), `schedule.md` FM-3 named as consequential (CR-010 Schedule field); the FW-B1 exit of WP-SW-14 is carried as an SE-45 lien to CDR by plan section 7 (observation O-2) | | none |
| swe-039 7.1 task 7 | | Yes | Assurance findings are kept in this record; INSP-037 findings in its lien table (INSP-037 iteration 2 findings table) | | none |
| swe-039 7.1 task 8 | SC | Yes | CR-010 section 6.2 responds to INSP-037 finding-1; the INSP-037 Minor findings carry owner and due; this record's owner ruling column is Pending for Claude's transcription (01 section 10.1) | | none |
| swe-121 7.1 task 1 | SC | Yes | No tailoring changes; the RMM approval of SRR decision 6 (`meta.approval`, equal on the branch) still covers every T and NA row; `render_rmm.py --check` at `5cd87cf`: "FC=75, T=17, NA=8", equal to `main` | | none |
| swe-121 7.1 task 2 | SC | N/A | A tailoring matrix of NASA-STD-8739.8 requirements cannot be built without the standard | `rmm.json` SWE-022 T | none |
| swe-125 7.1 task 1 | SC | Yes | The RMM is maintained with the change: 100 rows, same ids, five `implementation` fields changed, `rmm.md` current (`render_rmm.py --check` exit 0 at `5cd87cf`); one edited row misstates the SWE-220 measure | | finding-3 |
| swe-125 7.1 task 2 | SC | N/A | The NASA-STD-8739.8 matrix cannot be kept without the standard | `rmm.json` SWE-022 T | none |
| swe-139 7.1 task 1 | SC | Yes | Class A rigor kept: no requirement relieved; SWE-134, 219, 220 now apply without condition to the three determined components (03 section 4.4; `rmm.json` SWE-219 and SWE-220 rows name them) | | none |
| swe-087 7.1 task 3 | | Yes | 07 is the SA and software safety plan; this record is the peer review of its change | | none |
| swe-090 7.1 task 1 | | Yes | 07 section 11 (measurement catalog) has no hunk; the change adds no measure | | none |
| swe-154 7.1 task 1 | | Yes | 07 section 16 has no hunk; the CR-010 Cybersecurity field "None" is correct (no USB load or key-input path change); the SRR assurance of section 16 (INSP-018) stands | | none |
| swe-156 7.1 task 1 | | Yes | As swe-154 task 1: the section 16.2 assessment is unchanged | | none |
| swe-159 7.1 tasks 1 and 2 | | N/A | Cybersecurity mitigation testing is not at plan maturity; section 16.4 places it with the release verification | 07 section 16.4 | none |
| swe-036 7.1 task 1 | SC | Yes | 07 section 1.3 (records and deliverables) and section 3.1 task list: the only change is WP-SW-14 in the FW-B1 list, stated in section 3.1 and section 19; section 1.3 has no hunk | | none |
| swe-036 7.1 task 2 | SC | Yes | The "Owner action on receipt" column of 07 section 1.3 is unchanged; the owner's action on this change is the CR-010 disposition (section 7) and merge approval (section 10) | | none |
| swe-020 7.1 task 1 | SC | Yes | Concur with the classification: no hunk in 03 sections 3 to 3.3; section 9 "Software class" and "Per-item classification" rows unchanged (INSP-037 CL-1, CL-2, re-checked in the diff) | | none |
| swe-176 7.1 task 1 | SC | Yes | 03 section 9 and the RMM are updated with the rulings; the SWE-205 row's concurrence sentence is stale (INSP-037 finding-5); 03 sections 3.3 and 9 still name only the SRR records INSP-009 and INSP-017, and the PDR iteration records (INSP-037, this record) are to be named at the re-run with the 03 author's section 3.3 update | | none |
| swe-205 7.1 task 1 | SC | No | The hazard data lack the menu path's incorrect-action contribution to HZ-001, 004, 005, 006 that 03 section 4.3 records (script over `hazards.json` 0.5.0-pha) | | finding-1 |
| swe-205 7.1 task 2 | SC | No | The hazard reports do not identify the menu override command path, nor the safe-state manager and scheduler for HZ-008, although 03 section 4.3 and 07 section 14.1 determine them | | finding-1 |
| swe-205 7.1 task 3 | SC | No | Same as task 2 for the hazard analysis (`hazard-analysis.md` sections 6.2 and 7, items X14 and X16) | | finding-1 |
| swe-205 7.1 task 4 | SC | Yes | `traceability.py --report-only --output <scratch>/tr.md` at `main`: 245 requirements, 173 test cases, 0 violations, 2 warnings (REQ-SYS-125, REQ-SYS-148, not touched); HZ-008 K7 `control_req_ids` holds REQ-SYS-154, REQ-SYS-182, REQ-TX-003, REQ-TX-013 and `requirement_ids` holds REQ-SYS-182; no `docs/vv` file written (`git status` clean there) | | none |
| swe-205 7.1 task 5 | SC | Yes | The determination records the rulings consistently: 03 section 4.3, 07 section 14.1 and the rows of 03 section 5 name the same three components; the residual of `hazard-analysis.md` section 8.3 for a declined decision 40 is stated as not in force (03 section 4.3) | | finding-1 |
| swe-023 7.1 task 1 | SC | Yes | At plan maturity the `rmm.json` SWE-023 row lists every safety-critical component and data, the three determined components now without condition, with SWE-134, 219 and 220; relief for the standard's own list is on record | `rmm.json` SWE-023 T (the standard's list; criteria applied through 07 section 14) | none |
| swe-134 7.1 task 1 | SC | No | Items a to l are allocated to the three components (07 section 14.2 module rows at lines 642 to 644 are supersets of 03 section 5, as 07 requires); two provisions for items a and h still read conditional | | finding-2 |
| swe-134 7.1 task 4 | SC | Yes | Logical isolation: the word path shares no code with the verification unit (07 line 642, item i; 14.1 row "no code path shared"); the menu path isolation is covered both ways, by its own row (line 643) and by the receiving-side validation of row d and CS-39, which "apply in both outcomes" (07 section 14.1 owner-decision paragraph) | | none |
| swe-134 7.1 task 6 | SC | Yes | 03 section 5 Hazards column equals `swe134_items` of `hazards.json` 0.5.0-pha for all 12 rows (script, 0 mismatches); HZ-008 appears in rows a, b, f, g, h, i, k, l and in no other, matching its `swe134_items` | | none |
| swe-219 7.1 task 1 | SC | Yes | 100 percent MC/DC is addressed for the three components by the 07 section 9.6 three-element method (`rmm.json` SWE-219 names them; 03 section 4.4 scope names them and the drivers row); the shortfall route (owner waiver W<n>) is unchanged | | none |
| swe-220 7.1 task 1 | SC | No | No code exists; at plan maturity the RMM statement of the measure differs from the 07 CS-17 and CR-005 measure the gate applies | | finding-3 |
| swe-220 7.1 task 2 | SC | Yes | The limit of 15 and the single waiver rule (07 section 14.3) apply to the three components; `rmm.json` SWE-220 and 03 section 4.4 name them | | none |

## Readiness criteria

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | Product committed and frozen; `product_files` equal to the paired record's list | Yes | `git ls-tree cr/CR-010-apply-srr-decisions-9-and-40` (head `5cd87cf`) gives the four blobs; `git rev-parse HEAD:docs/cm/cr/CR-010-apply-srr-decisions-9-and-40.md` at `13a4f66` gives `ebce01d6`; equal to INSP-037 `product_files` |
| R2 | 07 section 2.1.1 row and criticality identified | Yes | Row "Software plans" (07 line 116 names 03 and "this plan"); Yes in every column; criticality safety-critical as in INSP-037 (the product is the determination of 07 section 14.1 rows) |
| R3 | `validate_docs.py` exit 0 on the product's files; traceability shows no violation for the ids touched | Yes | At `5cd87cf` (scratch worktree, removed): 45 passed, 5 failed, all five failures SRR records with record drift (CR-010 section 4 Verification), no product file fails; traceability 0 violations (swe-205 task 4 row) |
| R4 | Paired file review filed under its own invocation; this reviewer authored nothing and is not that reviewer | Yes | INSP-037 at iterations 1 (`f2f528f`) and 2 (`e750119`), `author_agent` "author:WP-PDR-17 wave 0", `reviewer_agent` "reviewer:WP-PDR-17-classification"; this invocation is `sa-reviewer:WP-PDR-17-classification` |

## A. Dispatch, independence and record integrity

| Id | Answer | Evidence |
|---|---|---|
| SA-A1 | Yes | 07 section 2.1.1 row "Software plans" names 03 (SWE-205 determination) and 07; Yes for safety-critical |
| SA-A2 | Yes | Three invocations: author (WP-PDR-17 wave 0), file reviewer (`reviewer:WP-PDR-17-classification`), this assurance reviewer; INSP-037 names the pair as "not yet assigned" (cross item X-1) |
| SA-A3 | Yes | Same `product`, `product_commit` `5cd87cf` and five blobs; no product change since either review (branch head unchanged; CR file unchanged since `02e7b52`) |
| SA-A4 | Yes | INSP-037 applied `peer-review-checklist-classification.md` revision A (R1 to R3, CL-1 to CL-9), the CR section 5 list (V1 to V7) and the 14 impact fields, each with evidence; SWE-088 criteria a to d met. Its V1 "Yes" missed two conditionals (finding-2 here) |

## B. SWE-to-task table

| Id | Answer | Evidence |
|---|---|---|
| SA-B1 | Yes | Task table: "Every product type" row; `plans` row with the "for 07" (swe-036) and "for 03" (swe-020, swe-176, swe-205 tasks 1 to 5) lists; and swe-023, swe-134 tasks 1, 4, 6, swe-219, swe-220 for the `rmm.json` rows the product rewrites. `assurance_tasks_applied` lists every Yes and No row |
| SA-B2 | Yes | N/A rows: swe-121 task 2 and swe-125 task 2 (`rmm.json` SWE-022 T); swe-159 tasks 1 and 2 (07 section 16.4). No SC task of the safety-critical product is N/A without relief |
| SA-B3 | Yes | swe-205 tasks 1 to 3 carry finding-1; swe-134 task 1 carries finding-2; swe-220 task 1 carries finding-3 |

## C. SWE-134 items a to l (the frequency-word path, the frequency verification unit and the menu override command path, at plan maturity)

Plan maturity means: the item is allocated in 03 section 5 or in the component's 07 section 14.2 module row, with provision text there and a reserved `REQ-SW-SAFE-NNN` id; requirements come at WP-PDR-35.

| Id | Answer | Evidence |
|---|---|---|
| SA-C-a | No, on finding-2 | Word path (line 642: starts unprogrammed, `PA_EN` frequency prerequisite false until read back and verified), verification unit (line 644), menu path (line 643: no override pending at any start); 03 row a names the unit and the menu path. Shared row a (line 615) still conditional |
| SA-C-b | Yes | Word path and verification unit state machines (lines 642, 644); 03 row b names the word path; 07 supersets 03 |
| SA-C-c | Yes | Not allocated to the three by 03 row c or their module rows; termination is the safe-state manager's `safe_state()` (row c), which the Fault-safe entry of both frequency components calls (row l) |
| SA-C-d | Yes | Menu path: action and separate confirmation from two distinct operator events (line 643); receiving-side validation in row d holds in both architecture outcomes |
| SA-C-e | Yes | Menu path: confirmation accepted only after its own action and within its window (line 643; 03 row e) |
| SA-C-f | Yes | Set frequency held with its complement in both frequency components (lines 642, 644; 03 row f) |
| SA-C-g | Yes | Register read-back and lock detect (word path), count plausibility (verification unit), debounced and range-checked events (menu path) |
| SA-C-h | No, on finding-2 | Word path band-edge limit and verification unit agreement are unconditional prerequisites (row h line 622; lines 642, 644); the `SW-TXSEQ` module row (line 633) still conditional |
| SA-C-i | Yes | Verification unit independent of `SW-SYNTH` in code and timebase; menu path: one gesture never yields both events; row i names REQ-SYS-182 |
| SA-C-j | Yes | Not allocated to the three: HZ-008 `swe134_items` hold no j, and 03 section 5 row j follows it; whether HZ-008 gains j (the 100 ms of decision 40) is item X14 for the hazard analysis author, whose due is finding-1 |
| SA-C-k | Yes | "All" in 03 row k; module rows: bus, counter and menu errors make the prerequisite false or cancel the override |
| SA-C-l | Yes | Disagreement or an off-frequency synthesizer enters Fault-safe with the cause shown (REQ-SYS-154; lines 642, 644); 03 row l keeps the safe-state manager as the item's owner, 07 is a superset |

## D. Software safety analysis and hazard traceability

| Id | Answer | Evidence |
|---|---|---|
| SA-D1 | No, on finding-1 | `hazards.json` 0.5.0-pha records HZ-008 C7 for the word path, but not the menu path's contribution to HZ-001, 004, 005, 006 nor the HZ-008 roles of the safe-state manager and scheduler. SWEHB `swe-205` section 7.7.2 considerations that apply: operator disabling of controls (the menu path generates the SWE-134 d overrides) and interlocks and inhibits (the frequency-verified `PA_EN` prerequisite) |
| SA-D2 | Yes | 03 section 4.3 and 07 section 14.1 equal the union rule of 03 section 4.1 step 3 over `hazards.json` with the stated type (ii) findings (INSP-037 CL-5, CL-8); no union changes (CR-010 section 4 Safety) |
| SA-D3 | Yes | 0 violations (swe-205 task 4 row); HZ-008 K7 traces to REQ-SYS-182 both ways |
| SA-D4 | N/A | No software requirement is created or changed; the reserved `REQ-SW-SAFE-001` to 012 are written by WP-PDR-35 |
| SA-D5 | N/A | No hazard-tracing requirement is created or changed; 03 section 5 lead keeps Test verification (SWE-192) for every provision |
| SA-D6 | Yes, with finding-1 | The software safety analysis is not re-issued by this CR; 0.5.0-pha already records the rulings (CR-010 Safety field); the open X14 and X16 updates are finding-1 |

## E. Peer review, change and configuration assurance

| Id | Answer | Evidence |
|---|---|---|
| SA-E1 | Yes | INSP-037 finding-1 closed with evidence (iteration 2, re-measured here); INSP-009 finding-10 (decisions 9 and 40 not applied) is addressed by the change text and verified by the INSP-009 delta at CR-010 step 5; INSP-017 finding-9 and finding-10 (liens to PDR) are outside the wave 0 scope and remain with the 03 author |
| SA-E2 | Yes | INSP-037 and this record carry `findings_*`, `items_no`, `effort_turns`, `effort_minutes`, `iteration` (07 section 10.3) |
| SA-E3 | Yes | CR route: CR file on `main` with `Refs: CR-010` (`9fd0962`, `02e7b52`); branch commit `5cd87cf` carries `CR: CR-010`; `git log baseline/srr..HEAD` on the four product paths is empty, so nothing bypassed the CR. The safety determination and the hazard data are under configuration control (03 and 07 Table 4-1 rows 2 and 3; `hazards.json` 0.5.0-pha committed at `bfea9c7`) |
| SA-E4 | N/A | No item under test and no credit run |

## F. Assurance risks, metrics and reporting

| Id | Answer | Evidence |
|---|---|---|
| SA-F1 | Yes | No assurance concern outside the findings needs a risk entry: RSK-046 and RSK-013, which the change touches, are re-assessed by WP-PDR-18 (CR-010 Risk field) |
| SA-F2 | Yes | Front matter carries `findings_*` and `assurance_findings_*` (the same three findings, counted once), `items_no`, effort |
| SA-F3 | Yes | Verdict, open findings, tasks applied and reliefs are stated in this record |

## Completion criteria and verdict

Readiness R1 to R4 were true; every task SA-B1 requires is in the task table; sections A to F are answered, with SA-D4, SA-D5 and SA-E4 N/A with their reasons; zero Major findings. The three Minor findings are open; this record follows plan rule C1 and 08 section 3.2 ("Minor findings ride with APPROVED"), as INSP-037 and INSP-047 do. They are written for the CR-010 author to fix before the step 4 freeze; a finding not fixed then is a lien due at the CDR readiness declaration (rule C1). **`reviewer_verdict: APPROVED`, `assurance_verdict: APPROVED`.** With INSP-037 `reviewer_verdict: APPROVED`, both reviews are APPROVED, but the four reviewed blobs exist only on the unmerged CR branch, so the record `verdict` is held at NEEDS CHANGES under the lead SE convention of 2026-09-27; the software lead sets it to APPROVED in the CR-010 merge commit, or the commit right after it, when the blobs reach `main` unchanged.

## Cross items (returned to Claude)

- **X-1.** INSP-037 still reads `assurance_reviewer_agent: "not yet assigned ..."` and `assurance_verdict: NEEDS CHANGES` and has no `paired_record`. Its reviewer updates it to `paired_record: INSP-050`, names this reviewer and copies `assurance_verdict: APPROVED` (07 section 10.2 Record row; each reviewer updates only its own record).
- **X-2.** For WP-PDR-16b (sole `hazards.json` writer, plan section 5.3) and the WP-PDR-16 safety review with its SA pair: X14 and X16 of 03 section 6.5 (components for HZ-001, 004, 005, 006 and HZ-008; `hazard-analysis.md` section 7 rows d and j) were not applied at 0.5.0-pha; OQ-SAF-014 is Open with `close_by` SRR. See finding-1.
- **X-3.** After CR-012 merges, the delta iteration of this record switches `checklist` to `peer-review-checklist-software-assurance` revision A and drops `checklist_software_assurance`.
- **X-4.** If CR-010 step 4 (rebase) or a fix of finding-2 or finding-3 changes any of the four blobs, INSP-037 and this record each get a delta iteration naming the new blobs before step 5.

## Observations (no finding)

- **O-1.** The synthesizer bus driver (WP-SW-05 or WP-SW-06) serves the frequency-word path, which is safety-critical since SRR decision 9; 03 section 4.3 drivers row defers it to the PDR re-run until the bus is selected. Plan WP-PDR-41 builds neither before PDR and plan section 7 carries their FW-B1 exit to CDR, so no driver code is written under lower rigor first. The re-run adds the selected bus driver, as the WP-PDR-17 outputs list says.
- **O-2.** 07 section 3.1 and section 19 now place WP-SW-14 in FW-B1 (PDR) without condition, while plan section 7 carries its FW-B1 exit as an SE-45 lien to CDR. The CR-010 Schedule field ("None new") is accurate for the plan text and could cite that plan row.
- **O-3.** 07 section 22 moves `SW-SYNTH` to the safety-critical tuple of `tools/validate_docs.py` after the merge; 07 section 2.1.1 already routes mission-critical products to assurance, so only the reported class changes and no routing gap exists meanwhile.

## Commands

| Command | Exit | Result |
|---|---|---|
| `git ls-tree cr/CR-010-apply-srr-decisions-9-and-40 <four paths>`; `git rev-parse HEAD:<CR path>` at `13a4f66` | 0 | Five blobs equal INSP-037 `product_files` |
| `git show cr/CR-012-pdr-checklist-templates:docs/templates/peer-review-checklist-software-assurance.md` | 0 | Template revision A, blob `5b135285` |
| `git diff --word-diff ab2af2d 5cd87cf` | 0 | 4 files, 72 insertions, 71 deletions |
| Section 7.1 extraction from `docs/references/md/swehb/swe-NNN-*.md` for SWE-013, 020, 022, 023, 024, 036, 039, 087, 090, 121, 125, 134, 139, 154, 156, 159, 176, 205, 219, 220 | 0 | Task texts used in the task table |
| JSON comparison of `rmm.json` at `ab2af2d` and `5cd87cf` | 0 | Only SWE-023, 134, 205, 219, 220 `implementation` differ |
| Script: 03 section 5 Hazards column against `swe134_items` of `hazards.json` 0.5.0-pha | 0 | 12 rows, 0 mismatches |
| Script: `firmware_role.components` of HZ-001, 004, 005, 006, 008, 012 in 0.5.0-pha | 0 | No menu component; HZ-008 names neither the safe-state manager nor the scheduler (finding-1) |
| Scan of the branch 03 and 07 for "is adopted", "if adopted", "proposed", "conditional", "declin" | 0 | 07 lines 615 and 633 conditional (finding-2); other hits historical or intentionally kept |
| Exact-substring check of the decision 9, 40 and 33 quotes in the SRR memo | 0 | Found at memo lines 214, 213, 215 |
| `git worktree add --detach <scratch>/wt-cr010 5cd87cf`; `tools/render_rmm.py --check`; `tools/validate_docs.py`; `git worktree remove` | 0; 1 | render_rmm exit 0 (100 rows; FC 75, T 17, NA 8; In place 40); validate_docs 45 passed, 5 failed (the five SRR drift records) |
| `.venv/bin/python tools/traceability.py --report-only --output <scratch>/tr.md` | 0 | 245 requirements, 173 test cases, 0 violations, 2 warnings; no `docs/vv` file changed |
| `.venv/bin/python tools/validate_docs.py` on the `main` working tree | 1 | 63 passed, 8 failed, 71 checked; this record PASS (drift notes only, for the branch-only blobs); the eight failures are records of other work packages, none naming a product file of this review |

## Verdict format

```
ASSURANCE VERDICT: APPROVED (record verdict held NEEDS CHANGES: reviewed blobs on the unmerged CR-010 branch)
PRODUCT: 03@1e03b873, 07@3ae7d73b, rmm.json@a907a087, rmm.md@17ea4733 at 5cd87cf; CR-010@ebce01d6 (main); PAIRED RECORD: INSP-037
PRODUCT TYPE: plans; CRITICALITY: safety-critical
FINDINGS:
- [Minor] swe-205 7.1 tasks 1 to 3 (SA-D1) 03 X14 and X16 were due at the next hazards.json change; 0.5.0-pha applied decisions 9 and 40 without them, and the fifth revision restates the passed trigger.
- [Minor] swe-134 7.1 task 1 (SA-C-a, SA-C-h) 07 section 14.2 row a and the SW-TXSEQ row still say "when REQ-SYS-182 is adopted".
- [Minor] swe-220 7.1 task 1 rmm.json SWE-220 states the raw rust-code-analysis measure and tpm.json, not the 07 CS-17 and CR-005 measure (plus one per let-else, gate G5, MSR-17).
TASKS APPLIED: swe-134 tasks 1, 4, 5, 6; swe-022 task 1; swe-013 tasks 1, 2; swe-024 tasks 1 to 3; swe-039 tasks 7, 8; swe-121 task 1; swe-125 task 1; swe-139 task 1; swe-087 task 3; swe-090 task 1; swe-154 task 1; swe-156 task 1; swe-036 tasks 1, 2; swe-020 task 1; swe-176 task 1; swe-205 tasks 1 to 5; swe-023 task 1; swe-219 task 1; swe-220 tasks 1, 2
TASKS N/A (relief): swe-121 task 2 and swe-125 task 2 (rmm.json SWE-022 T); swe-159 tasks 1 and 2 (07 section 16.4)
SWE-134 ITEMS CHECKED: a, b, c, d, e, f, g, h, i, j, k, l (three determined components, plan maturity)
MEASUREMENTS: size=4 files plus CR; tasks=36; tasks_no=5; turns=45; minutes=70; major=0; minor=3
```

## Iteration 2: re-pin delta on 07 `0ad37a43` and the CR-010 file (2026-09-29, `main` `9fda694`, branch heads `7963f78` and `1a486e4`)

**Why.** Lead SE rulings of 2026-09-29, recorded in CR-010 section 9 (`6ff9e35`) and CR-013 section 9 (`d30e7d2`). Ruling (3): INSP-037 and this record name 07 at `0ad37a43`, the combined CR-010 plus CR-013 text, and their record verdicts are set in the CR-013 merge commit; CR-010 and CR-013 merge back to back, so `main` holds 07 `3ae7d73b` only between the two merge commits. Ruling (2): a re-pin drops the CR file from `product_files` when the CR sections the record reviewed are unchanged, with the reason stated, so that later record-text edits of the CR file cannot make the record drift; otherwise the reviewer makes a delta. At iteration 1 this record pinned 07 `3ae7d73b` and the CR-010 file at `ebce01d6`; on `main` the CR-010 file is now `27604ce9`, so both pins would fail the record drift rule when the verdict is set.

**Scope (rule C1).** A delta, not a re-review. It reads (a) every hunk of `git diff 3ae7d73b 0ad37a43` (the CR-013 change to 07) under this record's assurance lens, to see whether any hunk changes an answer, a task result or a finding of iteration 1; and (b) every hunk of `git diff ebce01d6 27604ce9` (the CR-010 file) in the sections this record reviewed, sections 1 to 5 and the header. The CR-013 hunks as a change to 07 are the scope of INSP-059 and its pair INSP-073; this delta does not review them again, and it does not review the 07 section 17.1 licence row (lead SE ruling (4) gives that row to a verifier allowed to read committed rustos objects; this invocation read no rustos object). The other three product blobs are unchanged: `git rev-parse 41c588c:<path>` and `git rev-parse 1a486e4:<path>` give 03 `1e03b873`, `rmm.json` `a907a087` and `rmm.md` `17ea4733`, equal to `5cd87cf`, and `git log 5cd87cf..1a486e4` on the three paths is empty. Checklist as at iteration 1.

**Independence (rule C4) and search first.** A new invocation of this record's software assurance reviewer role (07 section 2.1.1), `sa-reviewer:WP-PDR-17-classification`. It authored no part of CR-010, CR-012 or CR-013, of their branch commits, of their record deltas (`e54ce91`, `7963f78`, `8d9efdf`, `b6cc8f8`, `1a486e4`) or of INSP-037, and it edited no product file. `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any `grep` (queries: "INSP-050 CR-010 software assurance record product_files findings_open"; "INSP-060 drops CR file from product_files reason record-text edits drift"; "findings_open counts liens Minor findings ride with APPROVED lesson L1 findings_open 0"). `git` and `grep -n` were used afterwards only to pin lines and blobs.

### The CR-013 hunks of 07 (`3ae7d73b` to `0ad37a43`; 18 hunks, 22 insertions, 26 deletions)

The sections iteration 1 reviewed (2.1.1, 3.1, 14.1, 14.2, 19) and the lines its answers cite:

| 07 location at `0ad37a43` | Hunk? | Effect on this record |
|---|---|---|
| Section 2.1.1 (row "Software plans"), section 3.1, section 14.1 (lines 579 to 608), section 19 (lines 768 to 792) | No | SA-A1, R2, swe-024 task 3, swe-205 task 5, swe-023 task 1, SA-D2 and observation O-2 stand. WP-SW-14 is still required for FW-B1 without condition (section 19 line 787) |
| Section 14.2 row a (line 615) and the `SW-TXSEQ` module row (line 633) | No | Both still read "when REQ-SYS-182 is adopted" (`grep -n` over the blob). finding-2 is unchanged |
| Section 14.2 row i (line 623) | Yes | The L1 column now also names REQ-SYS-181 (HZ-003 K9, SRR decision 39). The provision text, the verification unit's independence from `SW-SYNTH` and the REQ-SYS-182 citation are unchanged, so SA-C-i and swe-134 tasks 1 and 4 stand |
| Section 14.2 module rows (lines 642 to 644), section 14.3 | No | SA-C-a to SA-C-l and swe-220 task 2 stand |
| Section 22, row "Hazard analysis follow-ups" (line 854) | Yes | Items X14 and X16 of 03 section 6.5 now have a due: "PDR hazard analysis re-issue 0.6.0-pha (WP-PDR-16)". This is the 07 half of the route finding-1 asked for. The 03 half is not done: 03 is unchanged at `1e03b873`, and its X14 and X16 rows still restate the trigger "with the next `hazards.json` change" that 0.5.0-pha passed. finding-1 stays a lien, now with a live due in 07 |
| Section 22, row "03 alignment with section 14" (line 853) | Yes | Restates the done scheduler part and keeps the 07 part of X13 open for WP-PDR-17. No effect on this record's answers |
| CS-17 (line 264), section 8.1 complexity row (line 324), G5 (line 356), MSR-17 (line 516) | G5 only | The G5 hunk changes the Miri command only; G5 still runs `rust-code-analysis-cli` piped to `tools/complexity_gate.py --max 15`. The 07 measure that finding-3 compares with `rmm.json` SWE-220 is unchanged, and so is that row (`rmm.json` `a907a087`). finding-3 is unchanged |
| Section 11.1 (lines 465, 492) | Yes | Storage and evidence-preservation text only; section 11.2 (the measure catalog) has no hunk and no measure is added, so swe-090 task 1 stands |
| Sections 1.3, 15 and 16 | No | swe-036 tasks 1 and 2, swe-013 task 2, swe-022 task 1, swe-154 and swe-156 stand |
| Section 1.2 (line 31), 8.1 (lines 317, 331), 8.3 (line 344), 9.5 (line 401), 10.2 (line 446), 17.1 (line 728), 22 other rows (lines 849 to 867), 23 (line 882), Annex C (line 969) | Yes | Outside the sections this record reviewed. INSP-059 and INSP-073 review them; none changes a classification, criticality or SWE-134 allocation (INSP-073 SA-D2: "No 07 section 14.1 hunk") |

Result: no answer, task result or finding of iteration 1 changes because of the CR-013 hunks. No new finding.

### The CR-010 file (`ebce01d6` to `27604ce9`; dropped from `product_files`)

`git diff ebce01d6 27604ce9` (88 insertions, 22 deletions) changes: the front matter `status` (Submitted to Verified), `disposition` (Approved) and `disposition_date` (2026-09-28); the status sentence of the lead paragraph; in section 5, only the Done column of steps 3 to 6 (the step text of every row and the "Verification of the implementation" paragraph are unchanged); section 6.3 appended after section 6.2 (sections 6.1 and 6.2 unchanged); and sections 7 to 11 filled. Sections 1 to 4 (the change description, the reason, the alternatives and the 14 impact fields) are unchanged. The step 4 Done cell confirms that no rebase was made and the four blobs are the ones iteration 1 froze. None of these changes bears on an answer of this record. The CR file is therefore dropped from `product_files` and identified here as reviewed at `ebce01d6`, with the later hunks read at `27604ce9`. A later change to CR-010 sections 1 to 5 needs a delta of this record.

### Findings (iteration 2; current state of every finding of this record)

| Finding | Severity | State | Disposition |
|---|---|---|---|
| finding-1 | Minor | Lien: fix before CDR | Not fixed before the CR-010 step 4 freeze (rule C1). 03 `1e03b873` X14 and X16 still restate the passed trigger; 07 `0ad37a43` section 22 now gives them the due 0.6.0-pha (WP-PDR-16). Owner: the 03 author and the hazard analysis author (WP-PDR-16); due the CDR readiness declaration, or earlier with the 0.6.0-pha re-issue |
| finding-2 | Minor | Lien: fix before CDR | Not fixed: 07 `0ad37a43` lines 615 and 633 still read "when REQ-SYS-182 is adopted" (also CR-010 section 6.3 IR2-F4 and section 9). Owner: the 07 author (plan section 5.3 writer order); due the CDR readiness declaration |
| finding-3 | Minor | Lien: fix before CDR | Not fixed: `rmm.json` `a907a087` SWE-220 still states the raw analyzer measure and `tpm.json`. Owner: the `rmm.json` writer of WP-PDR-17; due the CDR readiness declaration |

Open Major: 0. New findings in this delta: 0.

### Checks run

- Blobs: `git rev-parse 41c588c:<path>` and `git rev-parse 1a486e4:<path>` give the four `product_files` blobs; `git rev-parse cr/CR-010-apply-srr-decisions-9-and-40:<path>` gives the same three non-07 blobs and 07 `3ae7d73b`; `git log ab2af2d..main` on the four paths is empty, so `main` still holds the baseline blobs; `git merge-tree --write-tree main cr/CR-013-process-04-07-semp-srr-liens` reports no conflict.
- 07 hunks: `git diff -U0 3ae7d73b 0ad37a43` (18 hunks, numstat 22 and 26) and `git diff --word-diff` on each hunk in the table above; `grep -n "REQ-SYS-182 is adopted"` over both blobs (lines 615 and 633 in each).
- CR-010 file: `git diff ebce01d6 27604ce9` hunk list and removed lines (only empty cells of sections 7 to 10 and the old front matter state are removed).
- `tools/validate_docs.py` on `main` with this delta in the working tree: this record PASS (drift of the branch-only blobs printed as notes, as expected for a held verdict).
- Pair (SA-A3): INSP-037 as re-pinned at `e3491d3` names the same `product_commit` `41c588c` and the same four `product_files` blobs, and drops the CR-010 file for the same reason.
- Verdict trial: a detached scratch worktree of `main` at `e3491d3`, trial `git merge --no-ff 7963f78` (CR-010) then `git merge --no-ff 1a486e4` (CR-013); `git rev-parse HEAD:<path>` there gives the four `product_files` blobs. With this record copied in at `verdict: APPROVED`: this record PASS with no drift note; `validate_docs.py` 117 passed, 0 failed. Negative control: the iteration 1 text at `verdict: APPROVED` FAILS on the two old pins (07 `3ae7d73b` differs from `0ad37a43`; CR-010 `ebce01d6` differs from `27604ce9`). The worktree was removed and no ref was kept.

### Record verdict (iteration 2)

**`reviewer_verdict: APPROVED`, `assurance_verdict: APPROVED`**, unchanged, with liens finding-1 to finding-3 (Minor, due the CDR readiness declaration). The record `verdict` stays **NEEDS CHANGES** under the lead SE convention: 07 `0ad37a43` reaches `main` only with the CR-013 merge. The software lead sets `verdict: APPROVED` in the CR-013 merge commit (lead SE ruling (3)), with the four blobs unchanged and INSP-037 re-pinned to the same four blobs and APPROVED. If a lien fix changes any of the four blobs before that merge, this record first gets a further delta.

```
DELTA ITERATION 2 (2026-09-29): ASSURANCE VERDICT: APPROVED (unchanged); record verdict held until the CR-013 merge commit (lead SE ruling 3)
PRODUCTS: 03@1e03b873, rmm.json@a907a087, rmm.md@17ea4733 (unchanged); 07 3ae7d73b -> 0ad37a43 (CR-013 41c588c, unchanged at 1a486e4); CR-010 file dropped (reviewed at ebce01d6; hunks to 27604ce9 read)
CHECKS: 18 CR-013 hunks of 07 read; 1 in a reviewed section (14.2 row i, L1 column only); section 22 X14/X16 due now set in 07
FINDINGS: finding-1, finding-2, finding-3 Minor liens due CDR (not fixed at the step 4 freeze); new findings 0; open Major 0
MEASUREMENTS: hunks=18 (07) plus 8 (CR file); table rows checked=10; new findings=0; iteration 2 turns=30, minutes=45; cumulative turns=75, minutes=115
```
