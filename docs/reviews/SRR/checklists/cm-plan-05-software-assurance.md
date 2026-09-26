---
# Peer-review record front matter (charter section 5; docs/process/01-lifecycle-and-reviews.md section 13
# is the single field list; docs/process/08-agent-briefing.md section 3.2; template
# docs/templates/peer-review-checklist-requirements.md revision C, section G and item A8, the checklist
# 08 section 3.1 routes "plans and process documents" to).
# This is the separate software assurance record of the software configuration management plan
# (NPR 7150.2D section 6.1 item d; 07 section 2.1.1 row "Software plans": Yes in every column; 07 section 22
# row "Assurance routing of 05 and TS-002"; INSP-006 cross item X-2; SRR package item R6 and decision 118 (a)).
# The paired file review of the same committed blob is INSP-006, docs/reviews/SRR/checklists/cm-plan-05.md
# (reviewer:cm-plan). The slug is the INSP-006 slug plus "-software-assurance" (07 section 10.2 Record row).
id: INSP-030
checklist: peer-review-checklist-requirements
checklist_revision: C
checklist_file: docs/reviews/SRR/checklists/cm-plan-05-software-assurance.md
product: docs/process/05-configuration-and-data-management.md
# product_commit: review baseline HEAD; the product blob is git rev-parse HEAD:<path> at that commit
# (last commit touching 05 is 0ab3d6e; the same blob INSP-006 iteration 3 verified at adcfe09)
# iteration 1 baseline: ade0e097c51f27a4d28755161becf75064fc8bee. Iteration 2 (re-issue, package item R19 (b), no further
# product review): HEAD 860e84e; git log ade0e09..HEAD on 05 is empty, so the product blob is unchanged
product_commit: "860e84e6346d09d69f83f584bc94855c638b4531"
product_blob: "63ed566240ffc7f055b65f93f579a6bb1498e9f1"
# product_files: re-checked at the iteration 2 re-issue equal to git rev-parse HEAD:<path> and git hash-object at HEAD 860e84e
product_files: ["docs/process/05-configuration-and-data-management.md@63ed566240ffc7f055b65f93f579a6bb1498e9f1"]
# inputs read (not reviewed), committed blobs at HEAD 860e84e. Iteration 1 read at ade0e09: tools/toolchain.lock.md@2687fb04,
# tools/validate_docs.py@33ab5a83, docs/reviews/SRR/checklists/cm-plan-05.md@d688ff4b (the other six are unchanged since ade0e09);
# the cm-plan-05.md blob now read carries the 05 author self-check filed at 8ef95d3 and the INSP-006 re-issue of 09d48be
input_files: ["docs/process/07-software-engineering-plan.md@d0f8baf614b49e9c99d8fe2169093d02626ac50d", "docs/process/rmm.json@30fcde240eeb6a147359de8c5d8cdd93364dc9c8", "docs/process/00-charter.md@131608b78e178432e34f8eb9fc385dae07020c6d", "docs/templates/version-description.md@030e8865c656ea0924ecd0196e7e1c6076bede3d", "docs/templates/change-request.md@c1e03e6de00f6f81dd005e9ca243da633c2e29f6", "docs/cm/cr/CR-001-cs11-cs38-driver-construction-arms.md@d582073ec6067ac9a64030ce8b5d66971c27da13", "tools/toolchain.lock.md@0ad60317be7e509c1e1968d2d9f4813f3904253f", "tools/validate_docs.py@3aa0368147b9af3e6e1546f808afb7aedf7f2226", "docs/reviews/SRR/checklists/cm-plan-05.md@b2cf5a0e2338cd1aadeaa82769a5602057c28426"]
product_size: 16 sections, 672 lines; Table 4-1 with 55 rows, Tables 4-2 and 6-1; release procedure of 12 steps (section 8.1), FCA-01 to FCA-10, PCA-01 to PCA-10
sprint: SRR-prep
author_agent: "author:cm-plan (Claude lead SE, CM function; revision 3 of 2026-09-25 with the 2026-09-26 edits of Table 4-1 row 13 and AL-15)"
reviewer_agent: "sa-reviewer:cm-plan"
criticality: neither
assurance_required: true
# assurance_reviewer_agent: this record IS the software assurance review; its reviewer is distinct from the
# author (author:cm-plan) and from the file reviewer of the paired record INSP-006 (reviewer:cm-plan)
assurance_reviewer_agent: "sa-reviewer:cm-plan (software assurance function; paired file review INSP-006 by reviewer:cm-plan)"
paired_record: INSP-006
# iteration 2: re-issue without a further product review (package item R19 (b); R15-F3); see "Iteration 2" at the end
iteration: 2
# readiness_met: iteration 1 false on R3 only (no author self-check of 05 on record). Iteration 2 true: R3 is met by the
# 05 author self-check filed at 8ef95d3 in docs/reviews/SRR/checklists/cm-plan-05.md (package item R7; INSP-006 cross item X-5);
# R1 and R4 Met, R2 and R5 N/A as answered at iteration 1.
readiness_met: true
# reviewer_verdict and assurance_verdict: APPROVED (with liens) under the lead SE convergence rule of 2026-09-26:
# 0 Major, 4 Minor, every Minor a lien "fix before PDR". Iteration 1 record verdict was NEEDS CHANGES on readiness R3 only.
# Iteration 2 record verdict APPROVED (with liens finding-1 to finding-4): reviewer and assurance APPROVED, readiness met,
# no Major finding open, the named product blob equals HEAD (07 section 10.2; SWE-088 b, c)
reviewer_verdict: APPROVED
assurance_verdict: APPROVED
verdict: APPROVED
findings_major: 0
findings_minor: 4
findings_open: 0
findings_fixed: 0
findings_verified: 0
# findings_deferred: the four liens (fix before PDR), carried by the package as Routine items, not RIDs
findings_deferred: 4
assurance_findings_major: 0
assurance_findings_minor: 4
assurance_tasks_applied: [swe-079 7.1 task 1, swe-080 7.1 task 1, swe-080 7.1 task 2, swe-080 7.1 task 3, swe-081 7.1 task 1, swe-081 7.1 task 2, swe-082 7.1 task 1, swe-082 7.1 task 2, swe-083 7.1 task 1, swe-084 7.1 task 1, swe-085 7.1 task 1, swe-085 7.1 task 2, swe-063 7.1 task 1, swe-063 7.1 task 2, swe-136 7.1 task 1, swe-187 7.1 task 1, swe-187 7.1 task 2, swe-013 7.1 task 1]
deferred_rids: []
# items_no: iteration 2 answers (R3 moved from No to Yes at the re-issue; every other answer unchanged)
items_no: [CK-REQ-G1, CK-REQ-G3, CK-REQ-G4, SA-080-1, SA-081-2, SA-082-1, SA-063-1, SA-063-2, SA-136-1]
# effort: iteration 1 42 turns, 60 min; iteration 2 (re-issue) 20 turns, 25 min
effort_turns: 62
effort_minutes: 85
record_status: Open
date: 2026-09-26
date_closed: null
---

# Peer review record INSP-030: software assurance review of the Configuration Management and Technical Data Management Plan (05)

**Product.** `docs/process/05-configuration-and-data-management.md`, committed blob `63ed5662` at review baseline HEAD `ade0e09` (`git rev-parse HEAD:docs/process/05-configuration-and-data-management.md` = `63ed566240ffc7f055b65f93f579a6bb1498e9f1`; `git status` clean; last commit touching it `0ab3d6e`). It is the blob INSP-006 iteration 3 verified at `adcfe09`, so the two records of the pair name the same product.

**Why an assurance record.** The committed 07 (blob `d0f8baf6`) section 2.1.1 row "Software plans" routes "the software CM plan `docs/process/05-configuration-and-data-management.md` (§6.1 item d)" to the software assurance reviewer with Yes in every column, on the basis of SWEHB `swe-013` section 7.1 task 1 and section 7.2 item 1. 07 section 22 row "Assurance routing of 05 and TS-002" (line 856) makes the dispatch due before the SRR readiness declaration; INSP-006 cross item X-2, SRR package item R6 and decision 118 (default (a)) carry it. The TS-002 half of that row is INSP-027.

**Lens.** Software assurance of a Class A software CM plan: NPR 7150.2D section 5.1, SWE-079 to SWE-085 (`npr-7150-2d/05-chapter5.md` lines 13 to 35) as dispositioned in `docs/process/rmm.json` (all FC; SWE-079 to SWE-082 In place, SWE-083 to SWE-085 Planned), with the SWEHB section 7.1 software assurance tasks of each page; release and version description (SWE-063, SWE-085, SWE-194); tool validation and accreditation (SWE-136, SWE-070); control of items before test (SWE-187); SWEHB 5.06 minimum SCMP content (`5-06-scmp-software-configuration-management-plan.md` lines 30 to 43). **Checklist:** `docs/templates/peer-review-checklist-requirements.md` revision C: readiness R1 to R5, section G (CK-REQ-G1 to G8) and CK-REQ-A8, the "plans and process documents" row (08 section 3.1; 07 section 10.1 row b). `docs/templates/peer-review-checklist-software-assurance.md` does not exist (08 section 3.5: due before PDR), so, per 07 section 15 and as INSP-018 and INSP-027 did, the SWEHB section 7.1 tasks are applied directly as items SA-NNN-n. **Answer legend:** Yes, No, N/A; every answer carries evidence.

**Search-first compliance.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (queries: "author self-check readiness R3 peer review record section G plans process documents"; "SWE-079 SWE-080 SWE-081 SWE-082 SWE-083 SWE-084 SWE-085 configuration management software assurance tasks 7.1"; "07 section 2.1.1 software plans assurance routing software CM plan 05 section 22 row Assurance routing of 05 and TS-002"; "author self-check of the CM plan 05 against checklist section G acceptance criteria"). The tool was available. `grep -n`, `awk`, `sed -n` and read-only Python were used afterwards only to pin lines the hits pointed at and to recompute the Table 4-1 matching; known paths were read directly.

**Independence.** This reviewer did not author 05, 07, the RMM, the templates or CR-001, is a different invocation from reviewer:cm-plan (INSP-006), and edited no product file and no other record. INSP-006 was read after this reviewer's own checks of 05 sections 3, 5, 7, 8 and 9 were done; the section "Concurrence with INSP-006" records the result.

**Convergence rule (lead SE direction 2026-09-26, applying charter section 4 item 3).** Only Major findings change products in this round. Every Minor finding is dispositioned "Lien: fix before PDR" in the lien table below and carried by the package as a Routine item.

## Findings

Ids follow the `finding-<n>` anchor rule of 01 section 13. Severity: Major blocks the baseline; Minor is fixed before the next review. No Major finding was raised: each of the four is a gap in who performs a software assurance task or in the alignment of a plan text, none makes the functional baseline wrong, none misquotes a NASA requirement, and each has a safe interim path under 07 section 2.1.1, which already governs the dispatch of every software assurance review.

| Finding | Origin | Severity | Item | Location | Description | State | Deferred to | Disposition |
|---|---|---|---|---|---|---|---|---|
| <a id="finding-1"></a>finding-1 | assurance | Minor | SA-080-1, SA-082-1, SA-063-2, CK-REQ-G3, CK-REQ-G1 | 05 section 5.2 rows "Assessed" (line 250) and "Verified" (line 254); section 3 rows "Independent reviewer" and "Software assurance" (lines 58, 60); section 7.4 (line 365); section 8.1 step 8 (line 384) | The plan gives the software assurance function no part in change control or release. The CR impact review (Assessed), the CR implementation check (Verified), the VDD and release-directory check (section 8.1 step 8) and the interim record checks (section 7.4) are assigned to "the independent reviewer" only, and the Assessed trigger is "Class I, or Class II when requirements, ICDs, hazards or test cases are affected". Nothing routes a CR to the software assurance reviewer when it changes a product that 07 section 2.1.1 marks Yes (for example 07 or 03, both Table 4-1 rows 2 and 3, CR-controlled from SRR) or when its Safety field (section 5.3, line 265) names a 07 section 14.1 component. The section 3 "Software assurance" row describes review-time audits, while section 7.4 gives the same checks to "the independent reviewer", so it is not stated whether these are one role or two. The gap is live: CR-001 (`docs/cm/cr/CR-001-cs11-cs38-driver-construction-arms.md`, Submitted, package decision 108) changes 07 CS-11, CS-12 and CS-38, its Safety field (line 53) names "the safe-state entry path of the safe-state manager (07 §14.1)", and its section 6 (line 81) reads "Not required: Class II, no requirement, ICD, hazard or test impact", which the 05 rule permits. SWEHB `swe-080-track-and-evaluate-changes.md` section 7.1 task 1 (line 627: analyze proposed changes "for impacts, particularly safety and security"); `swe-082-authorizing-changes.md` section 7.1 task 1 (line 696: "software assurance has participation in software control activities"); `swe-063-release-version-description.md` section 7.1 task 2 (line 725: for each release, confirm the security and coding-standard scans and their results). Fix: (a) in section 5.2 Assessed and Verified, add the software assurance reviewer whenever the CR changes a 07 section 2.1.1 Yes product or its Safety field names a 07 section 14.1 component, with the assessment written in the CR's section 6 and 9; (b) in section 8.1 step 8, have the software assurance reviewer confirm VDD section 6 row "Security and coding-standard confirmation" and the gate log at S; (c) state in section 3 that the section 7.4 checks are the software assurance audit of SWE-082 and SWE-085 (task 2 of each) performed by the software assurance reviewer, or name both roles explicitly; mirror the rule in `docs/templates/change-request.md` section 6 | Lien | PDR | Lien: fix before PDR. The CR-001 instance is returned to Claude as cross item X-1 |
| <a id="finding-2"></a>finding-2 | assurance | Minor | SA-136-1, SA-063-1, CK-REQ-G4, CK-REQ-G1 | `docs/process/rmm.json` (blob `30fcde24`) rows SWE-136, SWE-063 and SWE-085 against 05 section 9.2 step 3 (line 453), section 13 rows SRR and CDR (lines 585, 587), section 4.4 Product row (line 165) and section 8.1 last paragraph (line 392) | The RMM rows that record the Class A disposition of three CM requirements disagree with the plan on how and when they are met. (a) SWE-136: the RMM says "Accreditation is the owner's approval of the lock file at PDR and its re-check at TRR" and plans four TV records for SRR; 05 section 9.2 step 3 makes accreditation the owner's decision recorded in each TV file ("Accredited for purposes 1 to n at version v"), which the TV records follow (for example `TV-003-validate-docs.md` section 9, scope statement ACC-VALDOCS-001), and section 13 requires ten SRR TV records "each reviewed and accredited" (TV-001 to TV-010 exist; package decision 114 records their accreditation). (b) SWE-063 ("Planned for TRR: the first VDD for the release under test") and SWE-085 ("Planned for TRR: tools/release.sh and the first firmware/releases/vX.Y.Z/ release"): 05 places the first release candidate, with its VDD and the `tools/release.sh` TV record, before CDR (section 4.4 Product row "the first candidate precedes CDR, 07 §3.1"; section 13 CDR row "before the first release candidate (`release/FW-v0.9.0-rc1`, 07 §3.1 FW-B2)"; section 8.1 "Release candidates follow the same twelve steps ... with its own VDD"). SWEHB `swe-136-software-tool-accreditation.md` section 7.1 task 1 (line 609) asks assurance to confirm that the tools are validated and accredited; with two different accreditation rules in force the confirmation has no single criterion. INSP-006 finding-7 aligned the SWE-082 and SWE-085 implementation texts (AL-15) but not these clauses. Fix (RMM owner, 03 author; cross-document, as AL-15): restate the three RMM implementation texts from 05 sections 9.2, 13 and 4.4 and re-run `tools/render_rmm.py --check`; 05 lists the item as a new section 14.1 alignment row | Lien | PDR | Lien: fix before PDR |
| <a id="finding-3"></a>finding-3 | assurance | Minor | SA-063-1, SA-081-1, SA-085-1 | 05 section 8.1 paragraph "Build flavours" (line 390); section 4.3 row "Firmware release" (line 152); section 8.3 step 2 (line 423); section 8.4 "Anomaly contact rule" (line 431) | Instrumented and fault-injection flavours are built "by the same script at S with its Cargo feature", and the build identity embedded in every image is `CWHT_BUILD_ID=vX.Y.Z+<short S>` (section 8.1 step 3), so a flavour and the delivered image carry the same `picotool info` program version and the same version the radio shows. Only `picotool verify` against the released ELF tells them apart. A fault-injection image (injection commands, section 8.1) on a unit is a hazard-control defeat path, and the anomaly contact rule identifies the unit's software by "the firmware version string (`picotool info -a` or the version shown by the radio)", which cannot name the flavour. SWEHB `swe-063-release-version-description.md` section 7.1 task 1 (line 723: a correct version description for each release) and `swe-081-identify-software-cm-items.md` section 7.1 task 1 (line 709: configuration items and their versions identified). Fix: give each flavour its own embedded build identity (for example `vX.Y.Z+<short S>.<flavour>` set by `tools/release.sh`), list it in VDD section 2, and make section 8.3 step 2 and PCA-05 reject any version string with a flavour suffix on a delivered unit | Lien | PDR | Lien: fix before PDR (before the first flavour build; the cases that need flavours run after TRR) |
| <a id="finding-4"></a>finding-4 | assurance | Minor | SA-081-2 | 05 Table 4-1 row 25 (line 111); section 6 CSA item 2 (line 292); section 5.3 Safety field (line 265) | Firmware is one CI (`firmware/`), and neither Table 4-1 nor the CSA identifies which files implement the safety-critical and mission-critical components of 07 section 14.1. The Class I rule (section 2: a change that affects safety) and the CR Safety field (list the 07 section 14.1 modules affected) therefore rest on the CR author's judgement of which paths are safety-critical, and the CSA cannot show the level and last change of the safety-critical code as a set. Hazard reports and safety analyses are identified and controlled (rows 15 and 48, every change Class I), so this concerns code and design only. SWEHB `swe-081-identify-software-cm-items.md` section 7.1 task 2 (line 711: "Assess that the software safety-critical items are configuration-managed") and its section 7.4 guidance (line 804: "Clearly defined procedures for identifying safety-critical CIs"). Fix: when `docs/design/software-design.md` fixes the code-unit boundaries at PDR (07 line 607), add to row 25 Notes (or a new row) the map from each 07 section 14.1 component to its paths, add a criticality column to CSA item 2, and make the CR Safety field cite that map | Lien | PDR | Lien: fix before PDR |

## Lien table

| Finding | Severity | Disposition | Owner | Due |
|---|---|---|---|---|
| finding-1 | Minor | Lien: fix before PDR | 05 author (CM function); CR template owner for the mirror | PDR readiness declaration |
| finding-2 | Minor | Lien: fix before PDR | RMM owner (03 author); 05 author for the section 14.1 alignment row | PDR readiness declaration |
| finding-3 | Minor | Lien: fix before PDR | 05 author; `tools/release.sh` author (before its TV record, due CDR) | PDR readiness declaration |
| finding-4 | Minor | Lien: fix before PDR | 05 author with the software design author | PDR readiness declaration |

After the SRR baseline 05 is CR-controlled (Table 4-1 row 2, CR from SRR), so the four liens are applied by one Class II CR against 05 before the PDR readiness declaration, the vehicle section 4.4 already names for the PDR rows of Table 4-2.

## Readiness criteria

| # | Criterion | Answer | Evidence |
|---|---|---|---|
| R1 | The product validates: `tools/validate_docs.py` exits 0 | Yes for the product | 05 is Markdown and not schema-validated. Run at `ade0e09` before this record: 47 passed, 1 failed; the failure is `docs/reviews/SRR/checklists/hazard-analysis.md` (INSP-008 record drift after commit `ade0e09` changed `hazards.json` and `hazard-analysis.md`), outside this product (cross item X-4) |
| R2 | `tools/traceability.py` reports no violation for the ids in the file | N/A | 05 defines no REQ or TC id; the run is in "Tool runs" |
| R3 | The author's return states the self-check against sections A to G and the brief's acceptance criteria | No | No author self-check of 05 is on record: none came with this assignment, none is in the product, and the claude-context search above found none (INSP-006 R3 reached the same result at iteration 3). SRR package item R7 lists INSP-006; decision 115 is the waiver route. This record's verdict follows the INSP-006 R3 outcome |
| R4 | Every TBR has owner, plan, close_by; no TBD in the file | Yes | `grep -c -w TBD` on 05: 0; "TBR" occurs only as a subject (CSA item 13, FCA-09) |
| R5 | For a CR: impact assessment attached | N/A | Not a CR |

## Plan review items (CK-REQ-G1 to G8 and A8; assurance lens)

| Id | Answer | Evidence |
|---|---|---|
| CK-REQ-G1 | No | Consistent with charter section 8 (baselines, annotated tags pushed to `origin`, signing optional, CR for non-editorial change, FCA and PCA at SAR, SWE-136 tool validation) and with 07 sections 13 (VDD content defers to 05 section 4.3 identifiers and section 8.1 steps) and 7.3 (07 names 05 section 8.1 as governing). Disagreements: finding-2 (RMM SWE-136, SWE-063, SWE-085) and finding-1 (05 section 5.2 against 07 section 2.1.1) |
| CK-REQ-G2 | Yes | Every step names its artifact, path and id (sections 4.4, 5.2, 8.1, 8.2, 9.2; CR, TV, FW, HW-MB, ME-ENC, CWHT-A schemes); no "as appropriate" or "should consider"; open questions carry "Needed by" and a default (section 14) |
| CK-REQ-G3 | No | Owner as CCB, ETA and approver; Claude as CM function; persons who change at each level (section 3, SWE-082 c). The software assurance role has no part in CR assessment or release (finding-1) |
| CK-REQ-G4 | No | SWE-045, SWE-082 and SWE-085 implementation texts now match (INSP-006 finding-1 and finding-7 closed); SWE-136, SWE-063 and SWE-085 planned-for clauses do not (finding-2) |
| CK-REQ-G5 | Yes | CM security: push only by Claude with the owner's SSH identity (sections 3, 10.3), branch and tag protection OQ-CM-001, `SHA256SUMS` and `git fsck --full` (section 10.3), CRC-32 image trailer verified at boot (section 8.1 step 4, SWE-134 f), redaction check before CDR (section 10.3), no credentials or addresses committed; verified by the git known-answer test (section 9.2 table) and PCA-05. The software cybersecurity assessment is 07 section 16, which 05 cites |
| CK-REQ-G6 | Yes | Table 6-1 gives the four CM metrics with computation, threshold, response and storage; volatility per section 5.4 (MSR-02) |
| CK-REQ-G7 | Yes | Re-checked on this machine 2026-09-26: `git version 2.50.1 (Apple Git-155)`, `picotool v2.3.0`, both equal to `tools/toolchain.lock.md`; the honest limits (OpenSCAD cannot write STEP, kicad-cli time stamps and the normalization table, `freecadcmd` exit status, LTspice launcher form) are stated. `tools/sw_gate.sh` has no TV record while `TC-SW-TOOL-001-r2` is cited as developer evidence (observation 3) |
| CK-REQ-G8 | Yes | Pinned in the corpus: SWE-079 to SWE-085 at NPR 7150.2D 5.1.2 to 5.1.8 (`05-chapter5.md` lines 13, 15, 17, 21, 31, 33, 35); SWEHB section 7.1 tasks at `swe-079` line 584, `swe-080` lines 627 to 636, `swe-081` lines 709 and 711, `swe-082` lines 696 and 698, `swe-083` line 626, `swe-084` line 671, `swe-085` lines 884 and 886, `swe-063` lines 723 and 725, `swe-136` line 609, `swe-187` lines 704 and 706; SWEHB 5.06 items 1 to 8 at lines 30 to 43. INSP-006 CK-REQ-G8 verified the rest; no NASA requirement is presented as a quotation it is not |
| CK-REQ-A8 | Yes | Control classes, levels L0 to L3, release identifiers and the VDD section numbers used in 05 (VDD sections 2, 3, 4, 6, 7, 9) match `docs/templates/version-description.md` (blob `030e8865`); no em dash |

## Software assurance tasks applied (SWEHB section 7.1 tabs)

| Id | SWEHB task | Answer | Evidence |
|---|---|---|---|
| SA-079-1 | `swe-079` 7.1 task 1: assess that a software CM plan has been developed and complies with NPR 7150.2 and project guidance | Yes | SWEHB 5.06 items: 1 and 2 organization and responsibilities (section 3), 3 policies (header "Governing text"), 4 functions: identification (section 4), control (section 5), status accounting (section 6), audits and reviews (section 7), auto-generation tools and their inputs and outputs (rows 3, 18, 35 and section 4.5 "Generated files"), 5 schedule (section 13), 6 resources and tools (section 3 Resources, section 9), 7 plan maintenance (section 15), 8 release and delivery (section 8). Compliance per SWE in section 16; exceptions are finding-1 and finding-2 |
| SA-080-1 | `swe-080` 7.1 task 1: analyze proposed changes for impacts, particularly safety and security | No | Section 5.3 has Safety and Cybersecurity impact fields, but no assurance analysis is assigned (finding-1; CR-001 instance, cross item X-1) |
| SA-080-2 | `swe-080` 7.1 task 2: changes tracked, approved before implementation, implementation complete, changes tested | Yes | Section 5.2 states Submitted, Dispositioned before Implemented, the Implemented and Verified content, and the merge gate in section 4.5 ("requires the CR file to show `disposition: Approved`" before the merge) |
| SA-080-3 | `swe-080` 7.1 task 3: software changes follow the change control process | Yes | Section 5.1 names the vehicle for every situation; section 4.5 Checks and Table 6-1 row "Commits lacking mandatory trailers" (threshold 0) detect a change outside the process |
| SA-081-1 | `swe-081` 7.1 task 1: configuration items and their versions identified | Yes, with finding-3 | Table 4-1 (55 rows, matching rule, append-only rows) and section 4.3 identifiers. Audit at HEAD `ade0e09`: all 1,069 tracked files match exactly one row, 0 unmatched, 0 ambiguous (scratch script applying the section 4.2 rule). Flavour identity is finding-3 |
| SA-081-2 | `swe-081` 7.1 task 2: safety-critical items configuration-managed, including hazard reports and safety analysis | No | Hazard reports and analyses: rows 15 and 48, every change Class I. Safety-critical code and design are not identified as a set (finding-4) |
| SA-082-1 | `swe-082` 7.1 task 1: software assurance participates in software control activities | No | finding-1 |
| SA-082-2 | `swe-082` 7.1 task 2: audit against the CM procedures | Yes | Section 7.4 and the section 3 "Software assurance" row define the audit (tags, CSA, trailers, merges, Table 4-1 matching). This reviewer's spot audit at `ade0e09`: Table 4-1 matching clean (SA-081-1); no `baseline/*` or `release/*` tag exists (none is due before the SRR memo); commit messages since `d4cce27` carry no `Refs:` trailer, which section 4.5 row "Applicability" permits before the SRR readiness declaration; `origin/main` is at `d4cce27`, one commit behind `main` (section 10.4 pushes at session end). Execution gaps are cross item X-2 |
| SA-083-1 | `swe-083` 7.1 task 1: the project maintains configuration status records | Yes for the plan | Section 6 defines 13 CSA sections with sources, the hand-written interim form before every review, and Table 6-1. Execution: `docs/process/configuration-status.md` and `docs/cm/deviations.md` are not tracked at `ade0e09` although section 13 row SRR lists "first CSA issued" (cross item X-2) |
| SA-084-1 | `swe-084` 7.1 task 1: configuration audits performed to determine the correct versions and conformance to records | Yes | FCA-01 to FCA-10 and PCA-01 to PCA-10 (section 7), hash-based (FCA-03, FCA-04, PCA-01, PCA-05 to PCA-07); delta audit per post-SAR release (section 8.4); owner participation (SWE-045) |
| SA-085-1 | `swe-085` 7.1 task 1: procedures for storage, processing, distribution, release and support of deliverable software | Yes, with finding-3 | Section 8.1 (source commit S, artifacts commit A, `--locked` build, CRC-32 trailer, reproducibility check, `--check-artifacts` guard, tag on S), section 8.3 (flash, verify, as-built line, release candidates only on the bench unit, hand-over pack), section 8.4 (maintenance, delta audit, archive), section 10.4 (remote, bundle fallback, retention) |
| SA-085-2 | `swe-085` 7.1 task 2: audits that the project follows the deliverable-software procedures | N/A at SRR | No release exists; the section 7.4 checks and PCA-05 to PCA-08 are the planned audits (performer: finding-1) |
| SA-063-1 | `swe-063` 7.1 task 1: a correct VDD for each release | No | Every release and candidate gets a VDD from `docs/templates/version-description.md` (section 8.1 steps 5 and 11, PCA-07), and the template's section numbers match the 05 references. Two defects in the confirmation basis: flavour identity (finding-3) and the RMM plan date for the first VDD (finding-2) |
| SA-063-2 | `swe-063` 7.1 task 2: each release scanned for security defects and coding-standard compliance, results confirmed | No | The scans run (section 8.1 step 1 (d), gate G5; VDD section 6 row "Security and coding-standard confirmation"); the confirmation is not assigned to software assurance (finding-1) |
| SA-136-1 | `swe-136` 7.1 task 1: tools needed to create and maintain software validated and accredited | No | Section 9 (classes A to C, TV procedure, known-answer tests with seeded faults, re-validation triggers, lock) is complete; TV-001 to TV-013 exist; the accreditation rule differs between 05 and the RMM (finding-2) |
| SA-187-1 | `swe-187` 7.1 task 1: items under test are under CM before testing | Yes | Section 7.3 items 1 to 4: tagged release with VDD, report front-matter fields, procedure blob; "A commit that is not tagged produces developer evidence only" |
| SA-187-2 | `swe-187` 7.1 task 2: items kept under CM through the end of testing | Yes | Release candidate directories never pruned (section 8.1); FCA-03 and FCA-04 hash checks; test configuration record per TRR and delta TRR (section 7.3 item 4) |
| SA-013-1 | `swe-013` 7.1 task 1: the plan is in place with expected content | Yes | The CM plan exists at L1 (INSP-006, reviewer APPROVED with liens) with the content of SA-079-1; this record supplies the assurance review 07 section 2.1.1 requires |

## Observations (not findings)

1. **VDD section list in 07.** 07 section 13 lists twelve unnumbered VDD sections in an order that differs from the nine numbered sections of `docs/templates/version-description.md`, which 05 cites by number (VDD sections 2, 3, 6, 7, 9). 07 states that 05 section 8.1 governs and the template carries every 07 item, so there is no conflict of content; the 07 author may align the order at the next revision.
2. **Hazard list control between SRR and PDR.** Row 15 (hazards) is CR-controlled from PDR while the 03 and 07 safety-critical determinations that transcribe it are CR-controlled from SRR (rows 2 and 3). A hazard change that alters `firmware_role` or `swe134_items` forces a CR against 03 or 07, so the determination cannot drift silently; commit `ade0e09` (hazards 0.4.3-pha, status changes only) is an example of a permitted Log change.
3. **Gate script TV record.** `tools/sw_gate.sh` is class B (section 9.1) with its TV record due CDR (section 13; lock line 122), and its run `TC-SW-TOOL-001-r2` is cited in the SRR package. Section 13 requires a TV record "before that first cited use"; the package marks the run developer evidence (package section 2, entrance-figure dagger), which the lock rule "Until a tool is Accredited, its output is developer evidence only" permits. INSP-016 holds the FW-B0 findings; not duplicated.
4. **OQ-CM-001 default.** The default "risk `RSK-NNN` entered by Claude" has no register entry yet (no risk in `docs/risk/register.json` mentions branch or tag protection); it becomes due only if the owner leaves OQ-CM-001 undecided at SRR (package decision 15).

## Concurrence with INSP-006

Read after the checks above. This review agrees with INSP-006 iteration 3 on the closure of finding-1 to finding-9 (re-read at the same blob: SWE-045 row line 656, Table 4-2, section 10.4 retention, Table 6-1, UF2 size line 380, class B list line 446, AL-15 Closed with the RMM texts matching) and on its liens finding-10 (row 13 ADR exception) and finding-11 (status line and row 9 schema list). INSP-006 is a file review against section G; this record's four findings are assurance findings not in INSP-006. No INSP-006 finding is disputed or re-opened. INSP-006 front matter still reads `assurance_reviewer_agent: "pending ..."` and `assurance_verdict: pending`; under 07 section 10.2 the INSP-006 reviewer now names this record in `assurance_reviewer_agent` and `paired_record: INSP-030` and copies `assurance_verdict: APPROVED` (cross item X-3). This reviewer does not edit INSP-006.

## Cross items (outside this record's scope, returned to Claude)

- **X-1 (before package decision 108).** CR-001 names a 07 section 14.1 safety-critical component in its Safety field and changes 07 (a 07 section 2.1.1 Yes product), yet records "Not required" for the independent review of its impact assessment. Under 07 section 2.1.1 and the intent of finding-1, dispatch an independent and software assurance assessment of the CR-001 impact section before the owner rules decision 108.
- **X-2 (SRR execution of 05 section 13 row SRR).** `docs/process/configuration-status.md` (first CSA, hand-written until `tools/csa.py`) and `docs/cm/deviations.md` do not exist at `ade0e09`; neither is an item of package section 2.1 (R1 to R16). Add the first CSA, and the section 7.4 interim record check by the independent reviewer, to the package item list before the readiness declaration, or record why they wait for the memo.
- **X-3 (07 section 10.2 pairing).** INSP-006 names this record (`paired_record: INSP-030`, `assurance_reviewer_agent`, `assurance_verdict: APPROVED`) at its re-issue (package item R8). Add `docs/process/05-configuration-and-data-management.md` and `docs/decisions/trade-studies/TS-002-firmware-runtime-make-buy.md` to `tools/validate_docs.py` `ASSURANCE_WHOLE_PRODUCTS` (07 section 22 line 856; INSP-027 cross item 1). Package item R6 is answered by this record; decision 118 needs no ruling.
- **X-4 (validator failure at `ade0e09`).** `tools/validate_docs.py` fails on `docs/reviews/SRR/checklists/hazard-analysis.md` (INSP-008, APPROVED) by the record drift rule: commit `ade0e09` (item R9) changed `hazards.json` to `c6bf757e` and `hazard-analysis.md` to `49ec53f8`, while the record names `37d6cc83` and `b5ce99e9`. The INSP-008 reviewer re-records the committed blobs (delta check of the status edits), or the R9 commit's record change is completed.
- **X-5.** Carry finding-1 to finding-4 as Routine lien items in the package lien list.

## Tool runs (2026-09-26, this reviewer, HEAD `ade0e09`)

| Command | Exit | Result |
|---|---|---|
| `.venv/bin/python tools/validate_docs.py` (before this record) | 1 | 47 passed, 1 failed, 48 checked; the failure is `docs/reviews/SRR/checklists/hazard-analysis.md` (record drift after `ade0e09`, cross item X-4) |
| `.venv/bin/python tools/validate_docs.py` (after this record) | 1 | 46 passed, 3 failed, 49 checked; this record PASS as a peer_review_record; the three failures are other records being edited in the working tree by concurrent closure passes (`conops-and-concept.md`, `schedule-and-cost-estimate.md`: APPROVED with a finding line read as Major and Open) and `hazard-analysis.md` (cross item X-4); none concerns 05 |
| `.venv/bin/python tools/traceability.py --report-only` | 0 | 238 requirements, 170 test cases, 0 violations, 3 warnings (REQ-SYS-125 and REQ-SYS-148 `SYS_UNALLOCATED`, and the INSP-026 finding-5 `HAZARD_INVERSE` lien); none concerns an id in 05; the rewritten `docs/vv/traceability-report.md` and `traceability.json` were restored with `git checkout` (outside this record's scope) |
| Table 4-1 matching (read-only scratch script over `git ls-files`) | 0 | 1,069 tracked files, 0 unmatched, 0 matched by two rows of equal precedence |
| `git --version`; `picotool version` | 0 | `git version 2.50.1 (Apple Git-155)`; `picotool v2.3.0`; equal to the lock |

## Participants

Author agent `author:cm-plan` (absent). File reviewer `reviewer:cm-plan` (paired record INSP-006, separate invocation). Software assurance reviewer `sa-reviewer:cm-plan` (this record). Owner (Robin, SMA TA) for the disposition of the findings and of readiness R3 (decision 115). Visual products: none produced or changed by this review.

## Measurements (SWE-089)

Product size: 05, 672 lines, 16 sections, Table 4-1 with 55 rows. Items checked: 32 (R1 to R5, CK-REQ-G1 to G8, CK-REQ-A8, 18 SA items). Items answered No: 10 (front matter `items_no`). Items N/A: 3 (R2, R5, SA-085-2). Findings: 0 Major, 4 Minor, all from the assurance function, all Lien; fixed 0, verified 0, deferred 4 (liens). Iteration 1. Effort: 42 agent turns, 60 minutes.

```
VERDICT: record NEEDS CHANGES on readiness R3 only; reviewer_verdict APPROVED (with liens); assurance_verdict APPROVED (with liens)
PRODUCT: docs/process/05-configuration-and-data-management.md@63ed566240ffc7f055b65f93f579a6bb1498e9f1 (HEAD ade0e09)
FINDINGS:
- [Minor] SA-080-1, SA-082-1, SA-063-2 05 sections 3, 5.2, 7.4, 8.1 step 8: software assurance has no part in CR assessment or release confirmation (finding-1). Lien: fix before PDR
- [Minor] SA-136-1, SA-063-1 rmm.json SWE-136, SWE-063, SWE-085 disagree with 05 sections 9.2, 13, 4.4 (finding-2). Lien: fix before PDR
- [Minor] SA-063-1, SA-081-1 05 section 8.1 build flavours carry the release's embedded version string (finding-3). Lien: fix before PDR
- [Minor] SA-081-2 05 Table 4-1 row 25 and CSA item 2: safety-critical code not identified as a CI set (finding-4). Lien: fix before PDR
ITEMS N/A: R2, R5, SA-085-2; CK-REQ-A1 to A7, B1 to B7, C1 to C8, D1 to D4, E1 to E6, F1 to F4 (product is a plan)
MEASUREMENTS: size=672 lines; items=32; no=10; major=0; minor=4; lien=4; open_major=0; iteration=1; turns=42; minutes=60
```

## Iteration 2: re-issue (2026-09-26, SRR package item R19 (b), readiness finding R15-F3; no further product review)

**Scope and independence.** Written by a new invocation of `sa-reviewer:cm-plan` in the reviewer role (software assurance function). It did not author 05, the RMM, the 05 author self-check or INSP-006, and it edited no product file and no other record; the text above this section is the iteration 1 record and is left as written (audit trail). The only hold of iteration 1 was readiness R3 ("Why" in the R3 row and the front matter comment of iteration 1); it was not a finding. The convergence rule of 2026-09-26 (charter section 4 item 3) applies: no product content changes in this run, and every Minor finding stays a lien, "fix before PDR".

**Search first.** `mcp__claude-context__search_code` on `/Users/robinonsay/rust/cwht` ran before any manual search (query: "author self-check of 05 CM plan against checklist section G readiness R3 cm-plan-05"; the tool was available and its first hit was the INSP-006 re-issue text on R3, its fifth the INSP-006 re-issue banner). `grep -n`, `sed -n`, `awk` and `git` were used afterwards only to pin lines, read the `8ef95d3` diff and check blobs; known paths were read directly.

**Product state.** HEAD `860e84e6346d09d69f83f584bc94855c638b4531`, working tree clean for this record's product. `git rev-parse HEAD:docs/process/05-configuration-and-data-management.md` = `63ed566240ffc7f055b65f93f579a6bb1498e9f1`, the blob of `product_files`; `git log ade0e09..HEAD` on 05 is empty (17 commits since the iteration 1 baseline, none touching 05). No delta verification is needed. Of the inputs, six are unchanged; three changed and were re-read: `tools/toolchain.lock.md` (`0ad60317`; only the TV-003 row for the R18 validator run changed, the git 2.50.1 and picotool v2.3.0 rows that CK-REQ-G7 relies on are unchanged, and `git --version` and `picotool version` on this machine still print them), `tools/validate_docs.py` (`3aa03681`, the R18 record state rule) and `docs/reviews/SRR/checklists/cm-plan-05.md` (`b2cf5a0e`, carrying the author self-check). No finding or answer of iteration 1 cites a changed line.

**Readiness R3 against the 05 author self-check (`8ef95d3`).** R3 of `docs/templates/peer-review-checklist-requirements.md` revision C reads "The author's return states the self-check against sections A to G below and lists the brief's acceptance criteria". This record uses the same checklist and revision on the same product blob as INSP-006, so the self-check filed in INSP-006 is the author return R3 asks for here (iteration 1 R3 row: "This record's verdict follows the INSP-006 R3 outcome"; INSP-006 re-issue cross item X-5; package item R19 (b)). Checked against the `8ef95d3` diff:
- It is filed by `author:cm-plan` (the `author_agent` of this record) and is insertions only in `cm-plan-05.md`: 48 lines, one appended section; no reviewer field of INSP-006 or of this record was touched.
- It lists five acceptance criteria AC-1 to AC-5, each with source and result, and states why they are taken from the governing documents (no author brief for revisions 2 and 3 is on record). Each traces to a governing document and none is weaker than the checklist.
- It answers every applicable item for "plans and process documents" (CK-REQ-A8 and G1 to G8; A1 to F4 N/A for a plan) with evidence.
- It names the product blob it checked, `63ed5662`, equal to this record's `product_files` and to HEAD.

R3 is therefore **Yes**. The INSP-006 reviewer reached the same answer at `09d48be`.

**Differences between the author's answers and this record's (observation O-5, not a finding).** The self-check was filed at `8ef95d3`, before this record existed (`898d582`), so it could not respond to finding-1 to finding-4. Its CK-REQ-G3 and CK-REQ-G4 answers are Yes, while this record answers No on finding-1 (software assurance has no part in CR assessment or release) and finding-2 (RMM SWE-136, SWE-063, SWE-085 against 05 sections 9.2, 13 and 4.4). The reviewer's answers govern (the self-check says so of its own table: "the reviewer's answers above govern"); R3 asks that the self-check be stated, not that it agree. Its author statement "disputes no finding", and nothing in it contradicts the evidence of finding-1 to finding-4. The software assurance items SA-NNN-n are SWEHB section 7.1 tasks applied by this reviewer and are outside the checklist sections A to G that R3 names. The author's item S-1 (Table 4-2 annotations) is a file-review matter carried by INSP-006 observation O-6 and lien L-2; S-3 (the assurance pairing) is discharged by this record.

**Spot checks of the self-check claims used here, at HEAD `860e84e`.** 0 em dashes (U+2014) and 0 whole-word `TBD` in 05 (AC-4, R4); `git version 2.50.1 (Apple Git-155)` and `picotool v2.3.0` equal the lock (G7). The Table 4-1 matching of AC-3 was checked by this reviewer at iteration 1 (1,069 of 1,069) and is not re-run: 05 is unchanged, and files added since are outside this re-issue.

**Findings at iteration 2.** No finding changes state and no new finding is raised.

| Finding | Severity | State | Closes on |
|---|---|---|---|
| finding-1 | Minor | Lien: fix before PDR | Lien table row finding-1 (05 author; CR template owner) |
| finding-2 | Minor | Lien: fix before PDR | Lien table row finding-2 (RMM owner; 05 author) |
| finding-3 | Minor | Lien: fix before PDR | Lien table row finding-3 (05 author; `tools/release.sh` author) |
| finding-4 | Minor | Lien: fix before PDR | Lien table row finding-4 (05 author with the software design author) |

No Major finding exists; `findings_open` stays 0 and `findings_deferred` 4.

**Answers changed at iteration 2.** R3 changes from No to Yes. Every other answer of iteration 1 stands: R1 Yes for the product, R2 N/A, R4 Yes, R5 N/A; CK-REQ-G1, G3, G4 No on the liens; SA-080-1, SA-081-2, SA-082-1, SA-063-1, SA-063-2, SA-136-1 No on the liens; every other item Yes or N/A as recorded.

**Completion criteria (SWE-088 b, c; 07 section 10.2) at iteration 2: met.** Reviewer verdict APPROVED; assurance verdict APPROVED; readiness met; zero open Major findings; the named product blob equals HEAD. `verdict: APPROVED` (with liens finding-1 to finding-4). The paired file review INSP-006 already carries `paired_record: INSP-030` and `assurance_verdict: APPROVED`, equal to this record's assurance verdict (01 section 13 paired form), so no INSP-006 change follows. `record_status` stays Open for the software lead, who sets Closed when the four liens are dispositioned (07 section 10.2).

**Cross items at iteration 2 (outside this record's scope, returned to Claude).**
- **X-1 (open, unchanged).** CR-001 independent and software assurance assessment before package decision 108.
- **X-2 (open, unchanged).** `docs/process/configuration-status.md` and `docs/cm/deviations.md` still do not exist at `860e84e`; 05 section 13 row SRR lists the first CSA.
- **X-3 (INSP-006 part done; tool part open).** INSP-006 names this record (`09d48be`). `tools/validate_docs.py` `ASSURANCE_WHOLE_PRODUCTS` (blob `3aa03681`, line 253) still omits 05 and TS-002.
- **X-4 (in progress elsewhere).** The INSP-008 drift is package item R17; `hazard-analysis.md` is modified in the working tree by another invocation at the time of these runs and is not part of this commit.
- **X-6 (new).** `tools/validate_docs.py` now fails `docs/reviews/SRR/checklists/tool-validation-tv-001-to-tv-010.md` (INSP-015, APPROVED) by the record drift rule: it names `tools/validate_docs.py@33ab5a83` and `tools/tests/test_validate_docs.py@4fb5bcc7`, while HEAD holds `3aa03681` and `c70d2c93` after the R18 commit `96af250`. The INSP-015 reviewer delta-verifies the R18 change against TV-003 run 6 and re-records the blobs. Not a defect of 05.
- **X-7.** Package section 2 row H1 (d), section 2.1 item R19 (b), section 2.4 row INSP-030, and row 12 of the entrance checklist: record verdict APPROVED with liens finding-1 to finding-4 (R15-F3 answered).

**Tool runs (iteration 2, 2026-09-26, HEAD `860e84e`, repository root, `.venv/bin/python`).**

| Command | Exit | Result |
|---|---|---|
| `tools/validate_docs.py` (with this record edited) | 1 | 48 passed, 1 failed, 49 checked; this record PASS as a peer_review_record with `verdict: APPROVED` (record state rule of `3aa03681`); the failure is `tool-validation-tv-001-to-tv-010.md` (cross item X-6). `hazard-analysis.md` PASS on another invocation's working-tree edit (X-4) |
| `-m unittest discover -s tools/tests` | 1 | 400 tests, 1 failure: `test_validate_docs.RepositoryTests.test_repository_exit_zero`, the repository-content test, on the X-6 failure above |
| `tools/traceability.py --report-only` | 0 | 238 requirements, 170 test cases, 0 violations, 3 warnings (REQ-SYS-125 and REQ-SYS-148 `SYS_UNALLOCATED`; REQ-SW-KEYER-039 `HAZARD_INVERSE`); none concerns 05; `docs/vv/traceability-report.md` and `traceability.json` restored with `git checkout` (lien L-5) |
| `tools/render_risk.py --check --gate SRR --hazards docs/safety/hazards.json` | 0 | 65 risks, 159 candidates, 0 warnings, hazard cross-check passes; `register.md` current |
| `git rev-parse HEAD:<05>`; `git log ade0e09..HEAD -- <05>` | 0 | `63ed5662`, equal to `product_files`; empty |
| `git --version`; `picotool version` | 0 | `git version 2.50.1 (Apple Git-155)`; `picotool v2.3.0`; equal to the lock |

**Measurements (SWE-089) at iteration 2.** Items re-checked: 1 (R3) plus the product-blob and pairing checks; items answered No: 9 (front matter `items_no`); findings 0 Major, 4 Minor, all Lien; fixed 0, verified 0, deferred 4. Iteration 2: 20 agent turns, 25 minutes (totals 62 turns, 85 minutes).

```
ITERATION 2 (2026-09-26, HEAD 860e84e, package item R19 (b)): VERDICT: APPROVED (with liens finding-1 to finding-4)
READINESS: R1 Yes (product), R2 N/A, R3 Yes (05 author self-check at 8ef95d3), R4 Yes, R5 N/A
PRODUCT: docs/process/05-configuration-and-data-management.md@63ed566240ffc7f055b65f93f579a6bb1498e9f1 (unchanged since ade0e09)
FINDINGS: finding-1 to finding-4 Minor, Lien: fix before PDR; no new finding; count of open Major findings 0
MEASUREMENTS: items=32; no=9; major=0; minor=4; lien=4; open_major=0; iteration=2; turns=62; minutes=85
```
