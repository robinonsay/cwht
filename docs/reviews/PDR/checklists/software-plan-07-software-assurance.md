---
# Peer-review record front matter (charter sections 2 and 5; docs/process/01-lifecycle-and-reviews.md
# section 13; docs/process/07-software-engineering-plan.md sections 2.1.1, 10.2 and 15). This is the
# paired software assurance record of INSP-059 (docs/reviews/PDR/checklists/software-plan-07.md, the PDR
# delta of INSP-010 on the CR-013 prototype), and it is the PDR delta of the SRR assurance record INSP-018
# (docs/reviews/SRR/checklists/software-plan-07-software-assurance.md) that PDR work plan WP-PDR-13 names
# ("INSP-010, INSP-018 ... delta iterations (SA for 07)"), filed as a new PDR record (plan section 3.1).
# Checklist applied: docs/templates/peer-review-checklist-software-assurance.md revision A AS ON ITS CR-012
# BRANCH (cr/CR-012-pdr-checklist-templates at 7784672, blob 5b135285; CR-012 Submitted, not merged; the
# template does not exist on main). tools/validate_docs.py fails a record whose `checklist` names a template
# absent from main, so the field names peer-review-checklist-requirements revision C (section G and CK-REQ-A8,
# the checklist of the paired record INSP-059 and of the SRR pair INSP-018), and checklist_software_assurance
# records the template actually applied (the INSP-047 and INSP-050 form); the delta after CR-012 merges
# switches the field.
# Product: the same blob as INSP-059 product_files. The 07 blob exists only on the unmerged branch
# cr/CR-013-process-04-07-semp-srr-liens at 41c588c (parent 5cd87cf, the CR-010 change set); the CR file is
# on main. Lead SE convention (2026-09-27, INSP-031 practice): reviewer_verdict and assurance_verdict are set
# here; the record verdict stays held until the CR-013 merge brings the blob to main.
# Iteration 2 (2026-09-29, re-pin delta; lead SE ruling (2) of 2026-09-29): the 07 blob is unchanged at the
# CR-013 branch head 1a486e4; no CR file is in product_files, so none is dropped; findings_open is reconciled
# with the finding tables (section "Iteration 2").
id: INSP-073
checklist: peer-review-checklist-requirements
checklist_revision: C
checklist_software_assurance: "docs/templates/peer-review-checklist-software-assurance.md@5b13528504868b2add0f0b1e329c63aa2b54cdf4 (revision A, CR-012 branch head 7784672)"
checklist_file: docs/reviews/PDR/checklists/software-plan-07-software-assurance.md
product: docs/process/07-software-engineering-plan.md
# product_commit: the CR-013 branch head, as in INSP-059 (frozen, rule C2). Iteration 2: kept; the branch head is now
# 1a486e4, whose later commits are record commits that leave the 07 blob unchanged
product_commit: "41c588cddc9a97cec536482dc2bd164e2bf81ea3"
# product_files: the 07 blob only, unchanged at iteration 2. The CR-013 file was never a product_files entry (it is in
# input_files, which the record drift rule does not read), so lead SE ruling (2) has no CR entry to drop
product_files: ["docs/process/07-software-engineering-plan.md@0ad37a43a9d365408b78488f6c2b02933af56837"]
# input_files: read, not reviewed. The CR file now on main (revision with the section 6.1 review
# 10b94d9), the CR-010 base blob, the baseline blob, the SRR assurance record whose liens this delta verifies,
# the paired record, and the sources the liens are checked against (blobs equal git rev-parse HEAD:<path> at main 1a240f8)
# Iteration 2 adds the CR-013 file as read at main 2b0d963 (fef1f9d9)
input_files: ["docs/cm/cr/CR-013-process-04-07-semp-srr-liens.md@21b8a3db861a88334f285b78acb520d02cb29e23", "docs/cm/cr/CR-013-process-04-07-semp-srr-liens.md@fef1f9d9892e825025e713db5e4b855ca52e5d77", "docs/process/07-software-engineering-plan.md@3ae7d73b01810e47fd10251d798e0a047aaa72dd", "docs/process/07-software-engineering-plan.md@bfe05f4327e79fa15c24d2cf8c14249804f946a8", "docs/reviews/SRR/checklists/software-plan-07-software-assurance.md@9076d5a2d59a827d869057f00b40c8644274de02", "docs/reviews/PDR/checklists/software-plan-07.md@ccea98d61590a7240444328a0c8af604c4f8add8", "docs/safety/hazard-analysis.md@52c8ce16856499afc1b701e1ddb103788fcb1af9", "tools/sw_gate.sh@29a37127312e242bce2aa8f41602e3bcd4360f2f", "tools/toolchain.lock.md@4e978efc474adaf34337affe75addc51d5ab3d59"]
paired_record: INSP-059
product_type: plans
# criticality: safety-critical, as INSP-059 and INSP-018. 07 is the 07 section 2.1.1 "Software plans" product
# (Yes in every column) and states the safety-critical provisions of 07 sections 9.5, 9.6 and 14
criticality: safety-critical
product_size: 07 revision A.9, 23 sections and annexes A to D (1010 lines at 0ad37a43); CR-013 delta 14 change items, 22 insertions, 26 deletions against 3ae7d73b; SRR liens in scope INSP-018 finding-8, finding-9, finding-11
sprint: PDR-prep
author_agent: "author:WP-PDR-13 (Claude, software lead as 07 author; CR-013 originator)"
reviewer_agent: "sa-reviewer:WP-PDR-13-software-plan"
assurance_required: true
assurance_reviewer_agent: "sa-reviewer:WP-PDR-13-software-plan (software assurance function; paired file review INSP-059 by reviewer:software-plan)"
# iteration 2: re-pin delta and count reconciliation (section "Iteration 2")
iteration: 2
# readiness_met: true. R3 is answered on the product's files (07 has no validator failure); the 7 failures at
# 41c588c are SRR record drift that CR-013 section 4 discloses (INSP-059 R1 answers its own checklist's R1 No)
readiness_met: true
# reviewer_verdict and assurance_verdict: APPROVED. INSP-018 finding-9 and finding-11 Verified, finding-8 fixed
# for the done part with its remainder carried by INSP-059 finding-2 (concurred); 0 Major; 1 new Minor finding,
# a lien due the CDR readiness declaration (plan rule C1), since INSP-018 was already APPROVED
reviewer_verdict: APPROVED
assurance_verdict: APPROVED
# verdict: held at NEEDS CHANGES while the reviewed 07 blob exists only on the CR-013 branch (lead SE
# convention) and while the paired INSP-059 record verdict is held. The software lead sets APPROVED in the
# CR-013 merge commit, or the commit right after it, when blob 0ad37a43 reaches main unchanged and INSP-059
# is APPROVED. If CR-013 step 4 or 5 (rebase, lien fixes) changes the blob, both records first get a delta.
# Iteration 2: unchanged; set in the CR-013 merge commit (lead SE ruling (3)), after INSP-059 is paired and APPROVED
verdict: NEEDS CHANGES
findings_major: 0
findings_minor: 1
# findings_open: 1 at iteration 1, which contradicted the iteration 1 lien table (finding-1 "Lien (plan rule C1)", the
# later row and so the current state). Iteration 2: 0, because finding-1 is a lien and a lien is not Open (the
# INSP-037, INSP-032 and INSP-015 practice); the iteration 2 finding table shows it
findings_open: 0
findings_fixed: 0
findings_verified: 0
findings_deferred: 0
assurance_findings_major: 0
assurance_findings_minor: 1
assurance_tasks_applied: ["swe-134 7.1 task 5", "swe-022 7.1 task 1", "swe-013 7.1 task 1", "swe-013 7.1 task 2", "swe-024 7.1 task 1", "swe-024 7.1 task 2", "swe-024 7.1 task 3", "swe-039 7.1 task 7", "swe-039 7.1 task 8", "swe-121 7.1 task 1", "swe-125 7.1 task 1", "swe-139 7.1 task 1", "swe-087 7.1 task 1", "swe-087 7.1 task 2", "swe-087 7.1 task 3", "swe-089 7.1 task 1", "swe-090 7.1 task 1", "swe-154 7.1 task 1", "swe-156 7.1 task 1", "swe-036 7.1 task 1", "swe-036 7.1 task 2", "swe-136 7.1 task 1", "swe-135 7.1 task 2", "swe-135 7.1 task 7", "swe-027 7.1 task 1", "swe-219 7.1 task 1", "swe-134 7.1 task 1", "swe-134 7.1 task 6"]
swe134_items_checked: [a, b, c, d, e, f, g, h, i, j, k, l]
deferred_rids: []
items_no: ["swe-136 7.1 task 1"]
# effort: iteration 1 42 turns, 65 minutes; iteration 2 adds 12 turns, 20 minutes
effort_turns: 54
effort_minutes: 85
record_status: Open
date: 2026-09-27
date_closed: null
---

# Peer review record INSP-073: software assurance pair of INSP-059, 07 revision A.9 (CR-013), PDR delta of INSP-018

**Product.** `docs/process/07-software-engineering-plan.md` blob `0ad37a43` (revision A.9, draft) on branch `cr/CR-013-process-04-07-semp-srr-liens` at `41c588c`, parent `5cd87cf` (CR-010 change set, 07 blob `3ae7d73b`); baseline blob `bfe05f43` (`baseline/srr`, still the `main` blob: `git log baseline/srr..main -- <07>` is empty). Identity checked with `git rev-parse 41c588c:<07>` and `git hash-object` of the `git show` output: `0ad37a43`, equal to INSP-059 `product_files`; the branch head is still `41c588c`. The CR-013 change was read as `git diff --word-diff 5cd87cf 41c588c -- <07>` (hunks at branch lines 31, 317, 331, 344, 356, 401, 446, 465, 492, 623, 728, 849 to 863, 882, 969). The CR-010 hunks are INSP-037 and INSP-050 scope and are not re-reviewed. Change record: CR-013 on `main`, now blob `21b8a3db` (the section 6.1 impact review of `10b94d9` added; INSP-059 read `560fe69a`); status Submitted, Class II.

**Checklist.** `docs/templates/peer-review-checklist-software-assurance.md` revision A **as on its CR-012 branch** (`cr/CR-012-pdr-checklist-templates` at `7784672`, blob `5b135285`; not merged, absent from `main`). Sections R, A to F applied. `product_type` plans (07 section 2.1.1 row "Software plans", Yes in every column). `criticality` safety-critical, as INSP-059 and INSP-018. Section C is answered at plan maturity: the items the delta touches (c, i, k, l through the CS-11 arms and row i) are checked on the text; the others are checked as unchanged by diff (no 07 section 14.1 or 14.2 hunk other than row i).

**Acceptance criteria (rule C7).** INSP-018 finding-8, finding-9 and finding-11, each part of the fix as INSP-018 states it (finding-11: branch line 356, the Annex C line, and the section 8.1 Miri row naming the FW-B1 end); every task of the section B rows "Every product type" and `plans` with its "for 07" list; the section 7.1 tasks of the other SWEs the changed text implements (SWE-136 for section 8.3, SWE-135 for sections 8.1 and 8.4, SWE-027 for section 17.1, SWE-219 and SWE-134 for sections 1.2, 9.5 and 14.2 row i, SWE-087 and SWE-089 for the section 22 lien closures); the INSP-059 findings and "Facts for the software assurance pair" re-read under the assurance lens.

**Independence (rule C4).** This invocation authored no part of WP-PDR-13, CR-013, CR-010 or either branch commit, did not write INSP-059 (`reviewer:software-plan`) or the CR-013 section 6.1 review, and edited no product file. **Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: "PDR peer review checklist 07 software plan CR-013 WP-PDR-13 INSP record"; "validate_docs peer review record schema optional fields paired_record assurance_verdict equal"; "OQ-SW-001 rustos licence open question status"; "SWEHB 7.1 Tasking for Software Assurance SWE-136 software tool accreditation"). One read of the known engineering-record path failed before the first query (the brief named this record's path); it was a read, not a search. `grep -n`, `git grep` and read-only Python were used afterwards only to pin lines, list INSP ids and extract the SWEHB section 7.1 lists. The rustos repository was read only with `git show` of committed objects. **LTspice** was not run.

## Record

### Findings

| Finding | Origin | Severity | Item | Location | Description | State | Owner ruling | Deferred to |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | assurance | Minor | swe-136 7.1 task 1 | 07 blob `0ad37a43` section 8.3, branch line 344, the sentence rewritten by CR-013 (change item "Section 8.3: TV schedule aligned with 05 section 13 (05 AL-13)") | The sentence restates the 05 section 13 schedule "for the software tools" and calls 05 section 13 the single authoritative schedule, but its CDR list omits three tools that 05 section 13 row CDR names and that 07 itself owns or uses: `tools/release.sh` and `tools/image_trailer.py` ("before the first release candidate (`release/FW-v0.9.0-rc1`, 07 §3.1 FW-B2)"), and `shasum`. 07 lists `tools/release.sh` with `tools/image_trailer.py` as software items (section 1.2 Scripts row, line 28), and its release procedure (line 573) has `tools/image_trailer.py` write the CRC-32 trailer that the image verifies at boot (CS-32, the SWE-134 f provision), so it is a product-generating tool of the flashed image. INSP-059 ("CDR row ... all in 07") and CR-013 section 6.1 ("07 section 8.3 equals 05 section 13 row by row for the software tools") did not list these tools. A reader who takes the 07 list as the software TV schedule would not plan TV records for the two release scripts. Severity: Minor, because the same sentence names 05 section 13 as governing, neither script exists yet (`git ls-tree main tools/`), and its first-use rule ("a tool used for the record before its gate needs its TV record before that first cited use") still covers them. Fix: add "`tools/release.sh` and `tools/image_trailer.py` (before the first release candidate, FW-B2) and `shasum`" to the CDR part of the sentence, or drop the restated list and keep only the pointer to 05 section 13 | Open | Pending | |

**INSP-059 findings under the assurance lens (not raised again).** finding-1 (section 8.1 Miri and branch-coverage status cells still "to be installed in FW-B0"): concur at Minor. It is also the swe-135 7.1 task 2 view of the tool status, and CS-03 carries the same stale statement (observation O-1). finding-2 (section 22 closes the paired-record row although INSP-009 and INSP-017 carry no `paired_record`): concur at Minor. It is the remainder of INSP-018 finding-8 (lien table below). finding-3 (section 22 lead-in still "Log-controlled edits ... carried in the SRR package", charter `4e3f891`): concur at Minor. Under swe-024 task 3 the change route of the open items is misstated, but each re-dated row names its PDR writer, so no commitment is lost.

### Verification of the INSP-018 liens (delta)

| INSP-018 finding | Location in blob `0ad37a43` | Check | Result |
|---|---|---|---|
| finding-8 (section 22 row "Paired assurance record fields" listed done work as open) | Section 22 lead-in, line 849; the row is gone from the table | The done part is true on `main`: 01 section 13 (line 899) defines the optional `paired_record` field and the rule that the file review's `assurance_verdict` equals the assurance record's. `tools/validate_docs.py` `PEER_REVIEW_RECORD_SCHEMA` accepts the field (records with it pass). INSP-010 has `paired_record: INSP-018` and names it in `assurance_reviewer_agent`. INSP-018 asked to keep "only what remains (INSP-009 naming INSP-017 and the `assurance_verdict` copy rule, if still open)". That remainder is still open: INSP-009 has no `paired_record` field and names INSP-017 only inside `assurance_reviewer_agent` ("sa-reviewer:classification (INSP-017)"), and INSP-017 has no `paired_record`. 07 section 10.2 Record row (line 451) requires both records of a pair to carry it and cites "INSP-009 with INSP-017" as the SRR practice. The lead-in's "INSP-009 names INSP-017" is literally true but does not meet the 07 section 10.2 rule | Fixed for the done part; the remainder is INSP-059 finding-2 (concurred; not raised again) |
| finding-9 (section 14.2 row i called REQ-SYS-181 a "07 addition") | Section 14.2 row i, L1 column, line 623 | Row i now reads "REQ-SYS-055, 071, 083, 092, 119, 120, 180, 181, 182 (180, 181 and 182 adopted by SRR decisions 38, 39 and 40; 181 is HZ-003 K9), as `hazard-analysis.md` section 7 row i names them". `hazard-analysis.md` on `main` (blob `52c8ce16`, line 226) lists the same nine ids with "180, 181 and 182 adopted at SRR by package decisions 38, 39 and 40". `hazards.json` 0.5.0-pha HZ-003 K9 has `control_req_ids: [REQ-SYS-181]` (package decision 39). The section 22 "Hazard analysis follow-ups" row now agrees with row i. Under swe-134 task 6 the row is consistent with the system hazard analysis. The allocation is unchanged | Verified |
| finding-11 (G5 Miri command still `-p pico2`; section 8.1 silent on the FW-B1 end) | Section 8.4 G5 row, line 356; Annex C G5 line, line 969; section 8.1 Miri row, Notes cell, line 317 | Line 356: `cargo +nightly-2026-08-24 miri test -p api --lib (MSR-08, CS-03; api only until pico2 is host-compilable, SRR close-out item B, FW-B1 lien, section 8.1 Miri row)`. Line 969: `miri test -p api --lib` with "-p pico2 returns at FW-B1, close-out item B". `tools/sw_gate.sh` on `main` (blob `29a37127`, line 337) runs `miri test -p api --lib`, so the plan and the gate script now state the same command. The Miri row Notes cell now states the `api`-only scope at rustos `2ec64c0` and why (the two `link_section` statics the Mach-O host rejects), and that the `pico2` decision functions join at FW-B1 through the owner's `cfg_attr` change and a lock-pin CR (plan register PCR-10, `pdr-work-plan.md` line 1088). SRR minutes "Close-out decisions A to C" item B matches. No `-p pico2` Miri invocation remains. The row's status cell is still stale; that is INSP-059 finding-1 | Verified |

The SRR record INSP-018 still names blob `bfe05f43` with its liens as "Lien: fix before PDR". Its update at the merge is CR-013 section 6.1 IR-F1, done by its own reviewer (cross item X-2).

### Task table

| Task | Safety-critical designation (SWEHB 8.10 section 6) | Applied | Result and evidence | Relief (N/A only) | Finding ids |
|---|---|---|---|---|---|
| swe-134 7.1 task 5 | SC | Yes | This record is the assurance participation in the review of 07, which 07 section 2.1.1 routes here (row "Software plans") | | none |
| swe-022 7.1 task 1 | SC | Yes | Performed against the project software assurance plan (07 section 15, no hunk in the CR-013 diff) by this record. The NASA-STD-8739.8 part is relieved | `rmm.json` SWE-022 T (standard not in the corpus) | none |
| swe-013 7.1 task 1 | SC | Yes | 07 keeps its content for the PDR-prep event: CR-013 closes SRR liens and re-dates open items, and changes no tailoring (`rmm.json` is not in the CR-013 diff: `git diff --stat 5cd87cf 41c588c` lists 04, 07 and the SEMP only). One restated schedule is incomplete | | finding-1 |
| swe-013 7.1 task 2 | SC | Yes | 07 is the software assurance and software safety plan (07 section 2.1.1 row, section 15). Section 15 has no hunk | | none |
| swe-024 7.1 task 1 | SC | Yes | Class II change, no NPR 7150.2D relief added or removed (CR-013 section 4; section 6.1 "Software classification and tailoring") | | none |
| swe-024 7.1 task 2 | SC | Yes | Corrective-action closure with rationale: INSP-018 finding-9 and finding-11 closed with evidence (lien table above). finding-8 is closed for its done part, but the remainder was dropped without rationale; INSP-059 finding-2 carries it | | none |
| swe-024 7.1 task 3 | SC | Yes | Changed commitments recorded: each re-dated section 22 row names its writer and gate (WP-PDR-09, 16, 17, 18, 47; OD-31 via `owner-actions.md` section 11). The lead-in's stated change route is stale (INSP-059 finding-3, concurred) | | none |
| swe-039 7.1 task 7 | | Yes | Assurance findings are kept in this record. The INSP-018 liens and their state are in the lien table above | | none |
| swe-039 7.1 task 8 | SC | Yes | CR-013 section 1.2 answers each INSP-018 lien with a change item (items 2, 5, 9, 11, 14). The owner ruling column is Pending for Claude's transcription (01 section 10.1) | | none |
| swe-121 7.1 task 1 | SC | Yes | No tailoring changes in CR-013. The RMM approval of SRR decision 6 still covers every T and NA row | | none |
| swe-121 7.1 task 2 | SC | N/A | A tailoring matrix of NASA-STD-8739.8 requirements cannot be built without the standard | `rmm.json` SWE-022 T | none |
| swe-125 7.1 task 1 | SC | Yes | The RMM is maintained. The closed section 22 row "RMM rows SWE-089, SWE-090 and SWE-094" is true at `41c588c`: SWE-089 and SWE-090 name `docs/plan/measurements.json`, SWE-094 is not left as "Planned for PDR", and all three read `In place` (read-only script over `git show 41c588c:docs/process/rmm.json`) | | none |
| swe-125 7.1 task 2 | SC | N/A | The NASA-STD-8739.8 matrix cannot be kept without the standard | `rmm.json` SWE-022 T | none |
| swe-139 7.1 task 1 | SC | Yes | Class A rigor is kept. The CS-11 arms are admitted by CR-001 (SRR decision 108) and are not a new relief. The MC/DC scope is not widened or narrowed (CR-013 section 6.1 "Safety") | | none |
| swe-087 7.1 task 1 | | Yes | Peer reviews of the change are performed and reported: INSP-059 (file review) and this record, on the same blob | | none |
| swe-087 7.1 task 2 | | Yes | Accepted findings addressed: INSP-018 finding-9 and 11 and INSP-010 finding-14, 16, 17, 18, 20, 22 (INSP-059). INSP-018 finding-8 is addressed in part (INSP-059 finding-2) | | none |
| swe-087 7.1 task 3 | | Yes | 07 is the SA and software safety plan. This record is the peer review of its change | | none |
| swe-089 7.1 task 1 | | Yes | Peer review measurements are recorded: both records carry the 07 section 10.3 fields. The section 22 row "Evidence preservation of the SRR roll-up" (INSP-010 finding-15) correctly stays open, because `tools/measurements.py --check-records` fails the superseded 2026-09-26 roll-up records (INSP-059 check of `check_records`, concurred). It names both options, the TV-013 re-run and the WP-PDR-47 roll-up | | none |
| swe-090 7.1 task 1 | | Yes | Section 11.1 now states the schema and fixture as committed at `1d423e5` and `tools/measurements.py` at `3de1e2d` (both commits exist; subjects read with `git log -1`). TV-013 is on `main` (`docs/cm/tool-validation/TV-013-measurements.md`) | | none |
| swe-154 7.1 task 1 | | Yes | Section 16 has no hunk. The CR-013 Cybersecurity field "None" is correct | | none |
| swe-156 7.1 task 1 | | Yes | The section 16.2 assessment is unchanged. The OSS licence change of rustos (section 17.1) adds no cybersecurity risk: the dependency is owner-developed and `publish = false` | | none |
| swe-159 7.1 tasks 1 and 2 | | N/A | Cybersecurity mitigation testing is not at plan maturity; section 16.4 places it with the release verification | 07 section 16.4 | none |
| swe-036 7.1 task 1 | SC | Yes | 07 section 1.3 (records and deliverables) has no hunk. The revision row A.9 (line 882) records the change as "pending CR-013 disposition" | | none |
| swe-036 7.1 task 2 | SC | Yes | The "Owner action on receipt" column of section 1.3 is unchanged. The owner's action on this change is the CR-013 disposition (CR-013 section 7, requested at B1b or B2) | | none |
| swe-136 7.1 task 1 | | No | Section 8.3 now defers to 05 section 13 as the single schedule. PDR items were checked on `main`: TV-020 (Rust toolchain), TV-021 (`cargo-llvm-cov`), TV-022 (`cargo-nextest`), TV-023 (nightly with Miri) and TV-013 (`tools/measurements.py`) exist. The emulator TV is due by PDR. The restated CDR list omits `tools/release.sh`, `tools/image_trailer.py` and `shasum` | | finding-1 |
| swe-135 7.1 task 2 | | Yes | The G5 static-analysis set is used with its checkers (`cargo audit`, `cargo deny`, `cargo geiger --forbid-only`, `tools/unsafe_audit.py --check`, the complexity gate, Miri on `api`), and the plan and `tools/sw_gate.sh` now agree on the Miri scope. The section 8.1 status cells are stale (INSP-059 finding-1, concurred) | | none |
| swe-135 7.1 task 7 | | Yes | The G5 pass criteria (line 356, "no advisory, no violation, no unsigned unsafe, no CC > 15, no target-only CC above the CS-38 allowance, no Miri failure") are unchanged by CR-013 | | none |
| swe-027 7.1 task 1 | | Yes | Section 17.1 rustos `api` and `pico2` rows fill conditions a to f. Condition c (licence) now reads MIT at `2ec64c0`. Checked with `git -C /Users/robinonsay/rust/rustos show`: `2ec64c0:LICENSE` begins "MIT License", "Copyright (c) 2026 Robin Onsay"; `api/Cargo.toml` and `firmware/pico2/Cargo.toml` at `2ec64c0` have `license = "MIT"` and `publish = false` (lines 5 and 6); `c54d35a` has no `LICENSE`. The lock section 3 pin is `2ec64c0` (CR-004). `firmware/THIRD-PARTY-NOTICES.md` does not exist yet; the section 22 row "rustos license notice" keeps it open for WP-PDR-47 | | none |
| swe-219 7.1 task 1 | SC | Yes | 100 percent MC/DC is addressed for the safety-critical components by the section 9.6 method. The only target-only decisions on the safety-critical path are the CS-11 failure arms of `cwht-app::main`. These are the board `take()` `None` arm and the `Err` arm of each rustos driver constructor that returns `Result`. Each is listed in the MC/DC table as `target-only: Inspection` with a stated rationale: each arm calls `safe_state_halt()` alone (CS-11 line 253, CS-38 line 300), and CR-001 section 5 has the code reviewer inspect each arm. Sections 1.2 (line 31) and 9.5 item 3 (line 401) now name all the arms, not only `take()`. The disposition is the owner's ruling (SRR decision 108) | | none |
| swe-134 7.1 task 1 | SC | Yes | Items a to l stay allocated as at `3ae7d73b` (INSP-050). The only 14.2 hunk is row i, where the L1 column is now complete. The CS-11 arms are provisions of items c, k and l (termination and error paths end in `safe_state_halt()`) | | none |
| swe-134 7.1 task 6 | SC | Yes | Row i agrees with `hazard-analysis.md` section 7 row i and `hazards.json` HZ-003 K9 (INSP-018 finding-9 above). The section 22 "Hazard analysis follow-ups" row now dates items X14 and X16 to the 0.6.0-pha re-issue (WP-PDR-16), which is the route INSP-050 finding-1 asked for | | none |

## Readiness criteria

| # | Criterion | Result | Evidence |
|---|---|---|---|
| R1 | Product committed and frozen; `product_files` equal to the paired record's list | Yes | `git rev-parse 41c588c:docs/process/07-software-engineering-plan.md` gives `0ad37a43`, equal to INSP-059 `product_files`; branch head unchanged at `41c588c` |
| R2 | 07 section 2.1.1 row and criticality identified | Yes | Row "Software plans" (07 section 2.1.1, Yes in every column); criticality safety-critical as in INSP-059 and INSP-018 |
| R3 | `validate_docs.py` exit 0 on the product's files; traceability shows no violation for the ids touched | Yes (disclosed) | Detached scratch worktree of `41c588c` (removed after use): `validate_docs: 43 passed, 7 failed, 50 checked`. All seven failures are the SRR record-drift entries CR-013 section 4 names (INSP-005, 006, 009, 010, 017, 018, 021). No failure is in 07 itself. `traceability.py --report-only --output <scratch>/tr.md`: 245 requirements, 173 test cases, 0 violations, 2 warnings (`SYS_UNALLOCATED` REQ-SYS-125, 148). No `docs/vv` file changed. The paired record answers its own checklist's R1 No on the same facts |
| R4 | Paired file review filed under its own invocation; this reviewer authored nothing and is not that reviewer | Yes | INSP-059 committed at `ecdfd1f`, `author_agent` "author:WP-PDR-13", `reviewer_agent` "reviewer:software-plan"; this invocation is `sa-reviewer:WP-PDR-13-software-plan` |

## A. Dispatch, independence and record integrity

| Id | Answer | Evidence |
|---|---|---|
| SA-A1 | Yes | 07 section 2.1.1 row "Software plans" names "this plan"; Yes for safety-critical |
| SA-A2 | Yes | Three invocations: author (WP-PDR-13), file reviewer (`reviewer:software-plan`, INSP-059), this assurance reviewer. INSP-059 names the pair as "not yet assigned" (cross item X-1) |
| SA-A3 | Yes | Same `product`, `product_commit` `41c588c` and blob `0ad37a43`. No product change since INSP-059 (branch head unchanged) |
| SA-A4 | Yes | INSP-059 applied `peer-review-checklist-requirements.md` revision C, R1 to R5, section G and A8, and 11 delta rows, each with evidence; SWE-088 criteria a to d met. Its section 8.3 row "Correct" missed the release tools (finding-1 here) |

## B. SWE-to-task table

| Id | Answer | Evidence |
|---|---|---|
| SA-B1 | Yes | Task table: the "Every product type" row, and the `plans` row with its "for 07" list (swe-036 tasks 1 and 2). It also covers swe-136, swe-135 tasks 2 and 7, swe-027, swe-219, swe-134 tasks 1 and 6, and swe-087 tasks 1 and 2 and swe-089 for the SWEs whose text CR-013 changes. `assurance_tasks_applied` lists every Yes and No row |
| SA-B2 | Yes | N/A rows: swe-121 task 2 and swe-125 task 2 (`rmm.json` SWE-022 T); swe-159 tasks 1 and 2 (07 section 16.4). No SC task is N/A without relief |
| SA-B3 | Yes | swe-136 task 1 carries finding-1 |

## C. SWE-134 items a to l (07 as a whole, at plan maturity; delta scope)

| Id | Answer | Evidence |
|---|---|---|
| SA-C-a | Yes | Unchanged by CR-013 (no 14.1 hunk, no 14.2 hunk except row i); INSP-050 answer on `3ae7d73b` stands, with its finding-2 as the open item of that record |
| SA-C-b | Yes | Unchanged by CR-013 |
| SA-C-c | Yes | CS-11 arms: every driver-construction and board-`take()` failure ends in `safe_state_halt()` with no other statement (CS-11 line 253); sections 1.2 and 9.5 now state all of them |
| SA-C-d | Yes | Unchanged by CR-013 |
| SA-C-e | Yes | Unchanged by CR-013 |
| SA-C-f | Yes | Unchanged by CR-013. The image CRC trailer (CS-32) depends on `tools/image_trailer.py`, whose TV scheduling in 07 is finding-1; the provision itself is unchanged |
| SA-C-g | Yes | Unchanged by CR-013 |
| SA-C-h | Yes | Unchanged by CR-013; INSP-050 finding-2 (conditional wording) is that record's item |
| SA-C-i | Yes | Row i L1 column now names REQ-SYS-181 (HZ-003 K9) with 180 and 182, equal to the hazard analysis; the single-event argument text is unchanged |
| SA-C-j | Yes | Unchanged by CR-013 |
| SA-C-k | Yes | The `Err` arms of the rustos driver constructors are handled, none silently ignored (CS-11; CR-001) |
| SA-C-l | Yes | The failure arms reach the safe state from the boot path of `cwht-app::main` (section 9.5 item 3: "on the safe-state entry path of the safe-state manager") |

## D. Software safety analysis and hazard traceability

| Id | Answer | Evidence |
|---|---|---|
| SA-D1 | Yes | CR-013 changes no hazard data and no software contribution (CR-013 section 4 Safety; section 6.1 "Safety"). The open contributions of 03 items X14 and X16 are routed to 0.6.0-pha (section 22 row, INSP-050 finding-1) |
| SA-D2 | Yes | No 07 section 14.1 hunk; the criticality list is the CR-010 one, which INSP-050 reviewed |
| SA-D3 | Yes | 0 violations at `41c588c` (R3); HZ-003 K9 traces to REQ-SYS-181 and row i now names it |
| SA-D4 | N/A | No software requirement is created or changed |
| SA-D5 | N/A | No hazard-tracing requirement is created or changed |
| SA-D6 | Yes | The software safety analysis is not re-issued by this CR; the route to the 0.6.0-pha re-issue is stated in section 22 |

## E. Peer review, change and configuration assurance

| Id | Answer | Evidence |
|---|---|---|
| SA-E1 | Yes | INSP-018 finding-9 and 11 closed with evidence; finding-8 in part, the remainder carried by INSP-059 finding-2; none closed without evidence |
| SA-E2 | Yes | INSP-059 and this record carry `findings_*`, `items_no`, `effort_turns`, `effort_minutes`, `iteration` |
| SA-E3 | Yes | 07 is 05 Table 4-1 row 2 (CR from SRR). CR file on `main` with `Refs: CR-013` (`8470350`); branch commit `41c588c` carries `CR: CR-013`; `git log baseline/srr..main -- <07>` is empty, so nothing bypassed the CR |
| SA-E4 | N/A | No item under test and no credit run |

## F. Assurance risks, metrics and reporting

| Id | Answer | Evidence |
|---|---|---|
| SA-F1 | Yes | No assurance concern outside the finding needs a risk entry; the evidence-preservation gap is an open 07 section 22 row with an owner decision (CR-013 section 12 Q2) |
| SA-F2 | Yes | Front matter carries `findings_*` and `assurance_findings_*` (the same finding, counted once), `items_no`, effort |
| SA-F3 | Yes | Verdict, open finding, liens verified, tasks applied and reliefs are stated in this record |

## Observations (no finding)

- **O-1.** CS-03 (line 235) still says the dated nightly "has neither `miri` nor `llvm-tools`" and that "In FW-B0 the software lead runs `rustup toolchain install ... --component miri --component llvm-tools`". The lock (`nightly-2026-08-24 (date-pinned)` row, line 21; history row of 2026-09-26) records both installed. The statement is dated 2026-09-25 and so reads as history, but it is the same staleness as INSP-059 finding-1 and can be fixed with it.
- **O-2.** INSP-059 O-1 (the section 22 rows "Assurance routing of 05 and TS-002" and "Tool constants" go stale when `cr/CR-014-tool-liens-srr` merges) is concurred. CR-013 section 6.1 IR-F2 covers the re-statement at the rebase.

## Completion criteria and verdict

Readiness R1 to R4 were true. Every task SA-B1 requires is in the task table. Sections A to F are answered, with SA-D4, SA-D5 and SA-E4 N/A and their reasons. INSP-018 finding-9 and finding-11 are Verified. finding-8 is fixed for its done part, and its remainder is INSP-059 finding-2. There are zero Major findings. The one new Minor finding is open. INSP-018 was already APPROVED, so under plan rule C1 it is a lien due at the CDR readiness declaration unless the 07 author fixes it at the CR-013 rebase (step 5). **`reviewer_verdict: APPROVED`, `assurance_verdict: APPROVED`.** The record `verdict` is held at NEEDS CHANGES under the lead SE convention of 2026-09-27: the reviewed blob exists only on the unmerged CR-013 branch, and the paired INSP-059 record verdict is itself held. The software lead sets APPROVED in the CR-013 merge commit, or the commit right after it, when blob `0ad37a43` reaches `main` unchanged. If a lien fix changes the blob before the merge, both records get a delta iteration first.

## Lien table

| Finding | Severity | Disposition | Owner | Due |
|---|---|---|---|---|
| finding-1 | Minor | Lien (plan rule C1) | 07 author (Claude, software lead) | CDR readiness declaration (or at the CR-013 rebase, step 5) |

## Cross items (returned to Claude)

- **X-1.** INSP-059 still reads `assurance_reviewer_agent: "not yet assigned ..."`, `assurance_verdict: NEEDS CHANGES` and has no `paired_record`. Its reviewer updates it to `paired_record: INSP-073`, names this reviewer and copies `assurance_verdict: APPROVED` (07 section 10.2 Record row; each reviewer updates only its own record).
- **X-2.** At the CR-013 merge the SRR record INSP-018 (`product_files` blob `bfe05f43`) needs its own delta note by its reviewer, naming blob `0ad37a43` and recording finding-8 (in part), finding-9 and finding-11 as Verified by this record (CR-013 section 6.1 IR-F1).
- **X-3.** After CR-012 merges, the delta iteration of this record switches `checklist` to `peer-review-checklist-software-assurance` revision A and drops `checklist_software_assurance`.
- **X-4.** INSP-059 and CR-013 section 6.1 each state that 07 section 8.3 equals 05 section 13 for the software tools. finding-1 qualifies both statements; their writers decide whether a note is needed.

## Commands

| Command | Exit | Result |
|---|---|---|
| `git rev-parse 41c588c:<07>`; `git show 41c588c:<07> \| git hash-object --stdin` | 0 | `0ad37a43`, equal to INSP-059 |
| `git rev-parse cr/CR-012-pdr-checklist-templates:docs/templates/peer-review-checklist-software-assurance.md` | 0 | `5b135285` at `7784672` |
| `git diff --word-diff 5cd87cf 41c588c -- <07>` | 0 | The 14 CR-013 change items; hunks listed in the Product paragraph |
| `git log baseline/srr..main -- <07>`; `git log -1 --format=%B 41c588c` | 0 | Empty; trailer `CR: CR-013` |
| `git show main:docs/safety/hazard-analysis.md` line 226; script over `docs/safety/hazards.json` HZ-003 K9 | 0 | Row i lists 181; K9 `control_req_ids` REQ-SYS-181, 0.5.0-pha |
| `grep -n miri` over the extracted blob and `tools/sw_gate.sh` | 0 | 07 lines 317, 356, 969; gate line 337 `miri test -p api --lib` |
| `git -C /Users/robinonsay/rust/rustos show 2ec64c0:LICENSE`, `:api/Cargo.toml`, `:firmware/pico2/Cargo.toml`; `log -1 2ec64c0` | 0 | MIT; `license = "MIT"`, `publish = false`; subject as 07 quotes |
| `git show main:docs/process/05-configuration-and-data-management.md` section 13 | 0 | CDR row names `tools/release.sh`, `tools/image_trailer.py`, `shasum` (finding-1) |
| Section 7.1 extraction from `docs/references/md/swehb/swe-NNN-*.md` for SWE-013, 022, 024, 027, 036, 039, 087, 089, 090, 121, 125, 134, 135, 136, 139, 154, 156, 159, 219 | 0 | Task texts used in the task table |
| `git worktree add --detach <scratch>/wt-cr013 41c588c`; `tools/validate_docs.py`; `tools/traceability.py --report-only --output <scratch>/tr.md`; `git worktree remove` | 1; 0 | 43 passed, 7 failed (SRR drift); 0 violations, 2 warnings; worktree removed |

## Verdict format

```
ASSURANCE VERDICT: APPROVED (record verdict held NEEDS CHANGES: reviewed blob on the unmerged CR-013 branch; paired INSP-059 held)
PRODUCT: docs/process/07-software-engineering-plan.md@0ad37a43 at 41c588c; PAIRED RECORD: INSP-059
PRODUCT TYPE: plans; CRITICALITY: safety-critical
LIENS VERIFIED: INSP-018 finding-9, finding-11; finding-8 fixed in part (remainder = INSP-059 finding-2, concurred)
FINDINGS:
- [Minor] swe-136 7.1 task 1 07 s8.3 CDR list omits tools/release.sh, tools/image_trailer.py and shasum that 05 s13 names.
CONCURRED (not raised again): INSP-059 finding-1, finding-2, finding-3 (Minor)
TASKS APPLIED: swe-134 tasks 1, 5, 6; swe-022 task 1; swe-013 tasks 1, 2; swe-024 tasks 1 to 3; swe-039 tasks 7, 8; swe-121 task 1; swe-125 task 1; swe-139 task 1; swe-087 tasks 1 to 3; swe-089 task 1; swe-090 task 1; swe-154 task 1; swe-156 task 1; swe-036 tasks 1, 2; swe-136 task 1; swe-135 tasks 2, 7; swe-027 task 1; swe-219 task 1
TASKS N/A (relief): swe-121 task 2 and swe-125 task 2 (rmm.json SWE-022 T); swe-159 tasks 1 and 2 (07 section 16.4)
SWE-134 ITEMS CHECKED: a to l (c, i, k, l on the changed text; others unchanged by diff)
MEASUREMENTS: size=1010 lines, 14 change items; tasks=31; tasks_no=1; turns=42; minutes=65; major=0; minor=1
```

## Iteration 2: re-pin delta and count reconciliation (2026-09-29, `main` `2b0d963`, branch head `1a486e4`)

**Why.** Before the CR-013 merge commit sets this record's verdict (lead SE ruling (3) of 2026-09-29), two things were checked. (a) The pins, under lead SE ruling (2): a record re-pin drops a CR file from `product_files` when the CR sections it reviewed are unchanged, with the reason. (b) The counts: the front matter read `findings_open: 1`, while the finding tables read 0 open. The iteration 1 findings table lists finding-1 as Open, and the lien table after it lists finding-1 as "Lien (plan rule C1)". Under the record state rule of `tools/validate_docs.py`, the later row is the current state, so the tables show 0 open Minor findings. With `verdict: APPROVED` the record would have failed ("findings_open is 1 and the latest iteration's finding tables show 0 open Minor finding(s)").

**Scope (rule C1).** A delta. The product is unchanged, so no item is re-answered. This delta confirms the pin, states the current state of finding-1 and reconciles the counts. Checklist as at iteration 1.

**Independence (rule C4) and search first.** A new invocation of this record's software assurance reviewer role (07 section 2.1.1), `sa-reviewer:WP-PDR-13-software-plan`. It authored no part of CR-010, CR-012 or CR-013, of their branch commits or record deltas, or of INSP-059, and it edited no product file. It read no rustos object. `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any `grep` (queries: "INSP-050 CR-010 software assurance record product_files findings_open"; "INSP-060 drops CR file from product_files reason record-text edits drift"; "findings_open counts liens Minor findings ride with APPROVED lesson L1 findings_open 0"). `git` and `grep -n` were used afterwards only to pin lines and blobs.

### Pin (lead SE ruling (2))

- **07 blob unchanged.** `git rev-parse 41c588c:docs/process/07-software-engineering-plan.md` and `git rev-parse 1a486e4:<same>` both give `0ad37a43`, and `git log --oneline 41c588c..1a486e4 -- <07>` is empty. The commits after `41c588c` on the branch are record commits (`8d9efdf`, `b6cc8f8`, `1a486e4`) and the merges `eff05e0` and `3aab75b` of the CR-010 record commits `e54ce91` and `7963f78`. `product_files` stays as at iteration 1. `product_commit` stays `41c588c`, the commit INSP-059 names.
- **No CR file to drop.** This record never pinned a CR file in `product_files`. The CR-013 file is in `input_files` (read, not reviewed), and the record drift rule reads only `product_files` and `product_blob`. Later record-text edits of CR-013 therefore cannot make this record drift. The current CR-013 blob (`fef1f9d9`, `main` `2b0d963`) is added to `input_files` as read. Its changes since `21b8a3db` are in the front matter, the lead paragraph and sections 4 to 11. Section 1, whose change items this record used as a basis, is unchanged.
- **Licence row.** The swe-027 row of iteration 1 checked the 07 section 17.1 licence condition with `git show` of committed rustos objects. Under lead SE ruling (4), the CR-013 section 9 licence verifier later verified that row against rustos `2ec64c0` and `c54d35a` (`9fda694`, "Verified"). This delta did not repeat the check.

### Findings (iteration 2; current state of every finding of this record)

| Finding | Severity | State | Disposition |
|---|---|---|---|
| finding-1 | Minor | Lien: fix before CDR | Not fixed at the CR-013 rebase (step 5): 07 `0ad37a43` section 8.3 (line 344) still leaves `tools/release.sh`, `tools/image_trailer.py` and `shasum` out of the restated CDR list. INSP-018 was already APPROVED, so it is a lien (plan rule C1). Owner: the 07 author (Claude, software lead); due the CDR readiness declaration |

Open Major: 0. Open Minor: 0 (finding-1 is a lien). New findings in this delta: 0. Counts after reconciliation: `findings_minor` 1, `findings_open` 0, `findings_fixed` 0, `findings_verified` 0, `findings_deferred` 0 (a lien is not a Deferred RID; `deferred_rids` stays empty), `assurance_findings_minor` 1.

### Checks run

- `git rev-parse` of the 07 path at `41c588c` and `1a486e4`; `git log 41c588c..1a486e4 -- <07>` empty; `grep -n image_trailer` over the extracted blob (lines 28 and 573 name it; line 344 does not).
- `tools/validate_docs.py` on `main` with this delta in the working tree: this record PASS (drift of the branch-only blob printed as a note, as expected for a held verdict).
- Verdict trial: a detached scratch worktree of `main` at `e3491d3` (no record or product path of this delta changed between `e3491d3` and `2b0d963`), trial `git merge --no-ff 7963f78` (CR-010), then `git merge --no-ff 1a486e4` (CR-013). `git rev-parse HEAD:<07>` there gives `0ad37a43`. With this record copied in at `verdict: APPROVED`, this record PASSES with no drift note, and `validate_docs.py` gives 117 passed, 0 failed. Negative control: the iteration 1 text at `verdict: APPROVED` FAILS on the record state rule alone ("findings_open is 1 and the latest iteration's finding tables show 0 open Minor finding(s)"). The worktree was removed and no ref was kept.

### Record verdict (iteration 2)

**`reviewer_verdict: APPROVED`, `assurance_verdict: APPROVED`**, unchanged, with lien finding-1 (Minor, due the CDR readiness declaration). The record `verdict` stays **NEEDS CHANGES** under the lead SE convention, because 07 `0ad37a43` reaches `main` only with the CR-013 merge. The software lead sets `verdict: APPROVED` in the CR-013 merge commit (lead SE ruling (3)), with the blob unchanged and INSP-059 APPROVED. INSP-059 must also carry `paired_record: INSP-073`, this reviewer and `assurance_verdict: APPROVED` (cross item X-1, still open at `2b0d963`: INSP-059 reads "not yet assigned" and `assurance_verdict: NEEDS CHANGES`). Its reviewer makes that update.

```
DELTA ITERATION 2 (2026-09-29): ASSURANCE VERDICT: APPROVED (unchanged); record verdict held until the CR-013 merge commit (lead SE ruling 3)
PRODUCT: docs/process/07-software-engineering-plan.md@0ad37a43 (41c588c; unchanged at 1a486e4); no CR file in product_files (CR-013 is an input only)
COUNTS: findings_open 1 -> 0 (finding-1 is a lien in the tables); minor 1; open Major 0
FINDINGS: finding-1 Minor lien due CDR (not fixed at the CR-013 rebase); new findings 0
MEASUREMENTS: blobs re-identified=1; iteration 2 turns=12, minutes=20; cumulative turns=54, minutes=85
```
